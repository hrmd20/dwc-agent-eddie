#!/usr/bin/env python3
"""EDDIE Claude toolkit: take-based cuts, face-centered zooms, AI noise removal,
EDDIE captions, hook and pictures, with frame-accurate audio/video sync.

Run each step against a private project folder (projects/<name>/):
  transcribe  -> word timestamps for the raw recording
  clean-audio -> DeepFilterNet denoise + voice-energy gate
  cut         -> trims chosen takes (takes.json) to speech and tightens pauses
  audit       -> flags clip edges that start or end inside a word
  faces       -> finds the presenter's face in every clip
  render      -> frame-accurate, face-centered clips joined into renders/cut.mov
  captions    -> transcribes the cut and writes EDDIE captions
  compose     -> burns captions, hook and pictures; masters audio
  verify      -> checks sync, loudness and muted speech
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np

FPS = 30
DEFAULT_REPLACEMENTS = {"tea": "T", "shpg": "SHBG", "s8": "SHBG", "s80": "SHBG"}


def ffmpeg():
    exe = os.environ.get("FFMPEG") or shutil.which("ffmpeg")
    if not exe:
        try:
            import imageio_ffmpeg
            exe = imageio_ffmpeg.get_ffmpeg_exe()
        except ImportError:
            sys.exit("FFmpeg not found. Install it, set FFMPEG, or pip install imageio-ffmpeg.")
    return exe


def ff(*args, capture=False):
    cmd = [ffmpeg(), "-hide_banner", "-v", "error", "-y", *map(str, args)]
    if capture:
        return subprocess.run(cmd[:2] + list(map(str, args)), capture_output=True, text=True).stderr
    subprocess.run(cmd, check=True)


def preset(p):
    f = p / "eddie.json"
    return json.loads(f.read_text()) if f.exists() else {}


def read_wav(path):
    w = wave.open(str(path))
    x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    if w.getnchannels() > 1:
        x = x.reshape(-1, w.getnchannels()).mean(1)
    return x, w.getframerate()


def write_wav(path, x, sr):
    o = wave.open(str(path), "wb")
    o.setnchannels(1)
    o.setsampwidth(2)
    o.setframerate(sr)
    o.writeframes((np.clip(x, -1, 1) * 32767).astype(np.int16).tobytes())
    o.close()


def env_db(x, sr, hop=0.01):
    h = int(sr * hop)
    n = len(x) // h
    return 20 * np.log10(np.sqrt(np.mean(x[: n * h].reshape(n, h) ** 2, 1)) + 1e-9)


def words_of(path):
    return json.loads(Path(path).read_text())


# ---------------------------------------------------------------- transcribe
def transcribe(src, out, model="small.en"):
    from faster_whisper import WhisperModel
    tmp = Path(out).with_suffix(".16k.wav")
    ff("-i", src, "-vn", "-ac", 1, "-ar", 16000, tmp)
    m = WhisperModel(model, device="cpu", compute_type="int8")
    segs, _ = m.transcribe(str(tmp), word_timestamps=True, condition_on_previous_text=False)
    words = []
    for s in segs:
        print(f"[{s.start:7.2f}-{s.end:7.2f}] {s.text}", flush=True)
        words += [{"w": w.word, "s": round(w.start, 3), "e": round(w.end, 3)} for w in s.words]
    tmp.unlink()
    Path(out).write_text(json.dumps(words))


def cmd_transcribe(a):
    p = Path(a.project)
    (p / "transcripts").mkdir(exist_ok=True)
    transcribe(a.source, p / "transcripts" / "source_words.json", a.model)


# --------------------------------------------------------------- clean-audio
def cmd_clean_audio(a):
    p = Path(a.project)
    r = p / "renders"
    r.mkdir(exist_ok=True)
    cfg = preset(p).get("audio", {})
    ff("-i", a.source, "-vn", "-ac", 1, "-ar", 48000, r / "audio_raw.wav")
    x, sr = read_wav(r / "audio_raw.wav")
    try:
        import torch
        from df.enhance import enhance, init_df
        model, st, _ = init_df()
        y = enhance(model, st, torch.from_numpy(x)[None]).squeeze(0).numpy()
        print("DeepFilterNet denoise applied")
    except ImportError:
        print("DeepFilterNet unavailable; using FFmpeg afftdn (install deepfilternet for stronger cleanup)")
        ff("-i", r / "audio_raw.wav", "-af", "afftdn=nr=12:nf=-50", r / "audio_dn.wav")
        y, _ = read_wav(r / "audio_dn.wav")
    write_wav(r / "audio_denoised.wav", y, sr)
    # Gate on the denoised voice energy, never on transcript timings alone:
    # ASR word ends can fall short of spelled-out acronyms (S-H-B-G).
    e = env_db(y, sr)
    n = len(e)
    voice = e > cfg.get("gateOpenDb", -52)
    pre, post = 6, 14  # 60 ms before, 140 ms after voice
    m = np.convolve(voice.astype(float), np.ones(pre + post + 1), "full")[pre:pre + n] > 0
    near = np.zeros(n, bool)
    for w in words_of(p / "transcripts" / "source_words.json"):
        near[max(0, int(w["s"] * 100) - 60): int(w["e"] * 100) + 120] = True
    m &= near  # creaks in long pauses stay closed
    g = np.where(m, 1.0, 10 ** (cfg.get("gateFloorDb", -30) / 20))
    k = np.hanning(7)
    g = np.convolve(g, k / k.sum(), "same")
    gs = np.repeat(g, sr // 100)
    gs = np.pad(gs, (0, len(y) - len(gs)), "edge")[: len(y)]
    write_wav(r / "audio_clean.wav", y * gs, sr)
    print(f"clean audio written; gate open {m.mean():.0%} of the recording")


# ----------------------------------------------------------------------- cut
def cmd_cut(a):
    p = Path(a.project)
    takes = json.loads((p / "takes.json").read_text())
    x, sr = read_wav(p / "renders" / "audio_raw.wav")
    db = env_db(x, sr)
    sp = db > np.percentile(db, 10) + 14
    clips = []
    for ti, (s0, s1) in enumerate(takes):
        i0, i1 = int(s0 * 100), int(s1 * 100)
        idx = np.where(sp[i0:i1])[0]
        if not len(idx):
            continue
        st, en = i0 + idx[0], i0 + idx[-1]
        pieces, cur, k = [], max(st - 6, i0 - 3), st
        while k <= en:  # tighten pauses longer than 0.28 s
            if not sp[k]:
                j = k
                while j <= en and not sp[j]:
                    j += 1
                if j - k >= 28:
                    pieces.append((cur, k + 7))
                    cur = j - 6
                k = j
            else:
                k += 1
        pieces.append((cur, min(en + 14, i1 + 5)))
        clips += [{"take": ti, "s": a0 / 100, "e": a1 / 100} for a0, a1 in pieces if a1 - a0 >= 20]
    (p / "renders" / "clips.json").write_text(json.dumps(clips, indent=1))
    print(f"{len(clips)} clips, {sum(c['e'] - c['s'] for c in clips):.2f} s")
    audit(p)


def audit(p):
    x, sr = read_wav(p / "renders" / "audio_raw.wav")
    db = env_db(x, sr, 0.025)
    sym = lambda v: "#" if v > -40 else ("+" if v > -52 else ".")
    flags = 0
    # Voice within 75 ms outside a clip edge means the cut may split a word.
    for i, c in enumerate(json.loads((p / "renders" / "clips.json").read_text())):
        for edge, t in (("start", c["s"]), ("end", c["e"])):
            j = int(t * 40)
            near = db[max(0, j - 3):j] if edge == "start" else db[j:j + 3]
            if (near > -40).any():
                flags += 1
                view = "".join(sym(v) for v in db[max(0, j - 12):j]) + "|" + "".join(sym(v) for v in db[j:j + 12])
                print(f"CHECK clip {i} {edge} {t:.2f}s  {view}")
    print("edge audit:", "clean" if not flags else f"{flags} edge(s) to review by ear "
          "(a cut-off word, a stutter, or an intended cut between takes)")


def cmd_audit(a):
    audit(Path(a.project))


# --------------------------------------------------------------------- faces
def cmd_faces(a):
    import cv2
    if not hasattr(cv2, "CascadeClassifier"):
        sys.exit("Install opencv-python-headless<5 (OpenCV 5 removed the cascade face detector).")
    p = Path(a.project)
    f = p / "renders" / "clips.json"
    clips = json.loads(f.read_text())
    cap = cv2.VideoCapture(a.source)
    W, H = cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    cc = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    for i, c in enumerate(clips):
        pts = []
        for t in np.linspace(c["s"] + 0.05, c["e"] - 0.05, 6):
            cap.set(cv2.CAP_PROP_POS_MSEC, t * 1000)
            ok, fr = cap.read()
            if not ok:
                continue
            g = cv2.cvtColor(cv2.resize(fr, (int(W / 2), int(H / 2))), cv2.COLOR_BGR2GRAY)
            fs = cc.detectMultiScale(g, 1.1, 6, minSize=(80, 80))
            if len(fs):
                x, y, w, h = max(fs, key=lambda r: r[2] * r[3])
                pts.append(((x + w / 2) * 2, (y + h / 2) * 2))
        if pts:
            c["fx"], c["fy"] = float(np.median([q[0] for q in pts])), float(np.median([q[1] for q in pts]))
        else:
            c["fx"], c["fy"] = W / 2, H * 0.29
            print(f"clip {i}: no face found, using frame center")
    f.write_text(json.dumps(clips, indent=1))
    print("face x per clip:", [round(c["fx"]) for c in clips])


# -------------------------------------------------------------------- render
def cmd_render(a):
    p = Path(a.project)
    cfg = preset(p)
    W, H = cfg.get("canvas", {}).get("width", 1080), cfg.get("canvas", {}).get("height", 1920)
    fr = cfg.get("framing", {})
    zooms, eye = fr.get("zoomLevels", [1.12, 1.30]), fr.get("faceHeightFraction", 0.30)
    clips = json.loads((p / "renders" / "clips.json").read_text())
    out = p / "renders" / "clips"
    out.mkdir(exist_ok=True)
    for old in out.glob("*.mov"):
        old.unlink()
    lst, frames = [], 0
    for i, c in enumerate(clips):
        f0, f1 = round(c["s"] * FPS), round(c["e"] * FPS)  # cut on exact frames: no A/V drift
        n, s = f1 - f0, f0 / FPS
        d = n / FPS
        z = zooms[i % len(zooms)]
        w, h = int(W / z) // 2 * 2, int(H / z) // 2 * 2
        x = max(0, min(W - w, round(c["fx"] - w / 2)))
        y = max(0, min(H - h, round(c["fy"] - eye * h)))
        clip = out / f"c{i:03d}.mov"
        ff("-ss", f"{s:.4f}", "-i", a.source, "-ss", f"{s:.4f}", "-i", p / "renders" / "audio_clean.wav",
           "-map", "0:v", "-map", "1:a", "-frames:v", n,
           "-vf", f"crop={w}:{h}:{x}:{y},scale={W}:{H}:flags=lanczos,setsar=1",
           "-af", f"apad,atrim=end={d:.6f},afade=t=in:d=0.012,afade=t=out:st={d - 0.012:.6f}:d=0.012",
           "-c:v", "libx264", "-preset", "fast", "-crf", 15, "-pix_fmt", "yuv420p", "-r", FPS,
           "-c:a", "pcm_s16le", "-ar", 48000, "-ac", 2, clip)
        lst.append(f"file '{clip.resolve()}'")
        frames += n
    (out / "list.txt").write_text("\n".join(lst))
    ff("-f", "concat", "-safe", 0, "-i", out / "list.txt", "-c", "copy", p / "renders" / "cut.mov")
    print(f"cut.mov: {frames} frames = {frames / FPS:.2f} s")


# ------------------------------------------------------------------ captions
def fixed_words(p):
    cfg = preset(p).get("captions", {})
    rep = {k.lower(): v for k, v in {**DEFAULT_REPLACEMENTS, **cfg.get("replacements", {})}.items()}
    extra = p / "fixes.json"
    if extra.exists():
        rep.update({k.lower(): v for k, v in json.loads(extra.read_text()).items()})
    out = []
    for w in words_of(p / "transcripts" / "cut_words.json"):
        t = w["w"].strip()
        core = re.sub(r"[^\w]", "", t)
        if core.lower() in rep:
            t = t.replace(core, rep[core.lower()])
        out.append({"t": t, "s": w["s"], "e": w["e"]})
    return out


def ts(x):
    n = round(max(0, x) * 100)
    return f"{n // 360000}:{n // 6000 % 60:02}:{n // 100 % 60:02}.{n % 100:02}"


def cmd_captions(a):
    p = Path(a.project)
    transcribe(p / "renders" / "cut.mov", p / "transcripts" / "cut_words.json", a.model)
    cfg = preset(p).get("captions", {})
    words = fixed_words(p)
    mx, cy = cfg.get("maxWords", 3), cfg.get("centerY", 980)
    rows, srt, g = [], [], []
    for i, w in enumerate(words):
        g.append(w)
        nx = words[i + 1] if i + 1 < len(words) else None
        if nx is None or len(g) == mx or re.search(r"[.?!]$", w["t"]) or nx["s"] - w["e"] > 0.35:
            end = min(nx["s"] if nx else w["e"] + 0.4, w["e"] + 0.4)
            text = " ".join(x["t"] for x in g)
            rows.append(f"Dialogue: 0,{ts(g[0]['s'])},{ts(end)},Default,,0,0,0,,{{\\pos(540,{cy})}}{text}")
            srt.append((g[0]["s"], end, text))
            g = []
    dur = words[-1]["e"] + 0.6
    if preset(p).get("progressBar", {}).get("enabled", True):
        ms = int(dur * 1000)
        rows.append(f"Dialogue: 1,{ts(0)},{ts(dur)},Bar,,0,0,0,,{{\\pos(0,0)\\clip(0,1906,0,1920)"
                    f"\\t(0,{ms},\\clip(0,1906,1080,1920))\\p1}}m 0 1906 l 1080 1906 1080 1920 0 1920")
    size, outline = cfg.get("fontSize", 67), cfg.get("outline", 4)
    hdr = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
ScaledBorderAndShadow: yes
[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Arial,{size},&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,{outline},1,5,40,40,0,1
Style: Bar,Arial,20,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    (p / "renders" / "captions.ass").write_text(hdr + "\n".join(rows) + "\n")
    st = lambda t: f"{int(t // 3600):02}:{int(t % 3600 // 60):02}:{int(t % 60):02},{int(t * 1000) % 1000:03}"
    (p / "renders" / "captions.srt").write_text(
        "\n".join(f"{i + 1}\n{st(s)} --> {st(e)}\n{t}\n" for i, (s, e, t) in enumerate(srt)))
    print(f"{len(srt)} captions, {dur:.2f} s; review the wording in renders/captions.srt")


# ------------------------------------------------------------------- compose
def hook_png(lines, emphasis, path, y0):
    from PIL import Image, ImageDraw, ImageFont
    font = None
    for f in ("/System/Library/Fonts/Supplemental/Arial Bold.ttf", "C:/Windows/Fonts/arialbd.ttf",
              "/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf",
              "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"):
        if Path(f).exists():
            font = ImageFont.truetype(f, 58)
            break
    if font is None:
        sys.exit("Arial Bold (or Liberation Sans Bold) not found for the text hook.")
    im = Image.new("RGBA", (1080, 1920))
    d = ImageDraw.Draw(im)
    y = y0
    for line in lines:
        t = Image.new("RGBA", (1080, 120))
        td = ImageDraw.Draw(t)
        x = 0
        for word in line.split():
            td.text((x, 80), word, font=font, fill="red" if word in emphasis else "black", anchor="ls")
            x += font.getlength(word + " ")
        t = t.crop(t.getbbox())
        w, h = t.width + 44, t.height + 36
        x = (1080 - w) // 2
        d.rounded_rectangle((x, y, x + w, y + h), 24, fill="white")
        im.alpha_composite(t, ((1080 - t.width) // 2, y + 18))
        y += h + 10
    im.save(path)


def cue(words, phrase, after=0.0):
    seq = phrase.lower().split()
    for i in range(len(words) - len(seq) + 1):
        if words[i]["s"] >= after and all(
                re.sub(r"[^\w]", "", words[i + k]["t"]).lower() == seq[k] for k in range(len(seq))):
            return words[i]["s"]
    sys.exit(f"overlay cue not found in the cut: '{phrase}'")


def cmd_compose(a):
    p = Path(a.project)
    cfg = preset(p)
    words = fixed_words(p)
    clips = json.loads((p / "renders" / "clips.json").read_text())
    cut_len = sum(round(c["e"] * FPS) - round(c["s"] * FPS) for c in clips) / FPS
    dur = min(words[-1]["e"] + 0.6, cut_len)
    ov =json.loads(Path(a.overlays).read_text()) if a.overlays else {}
    inputs, chain, last = [], [], "0:v"

    def add(png, x, y, enable):
        nonlocal last
        inputs.extend(["-loop", 1, "-i", png])
        tag = f"v{len(chain)}"
        chain.append(f"[{last}][{len(inputs) // 4}:v]overlay={x}:{y}:enable='{enable}':shortest=1[{tag}]")
        last = tag

    hk = ov.get("hook")
    hcfg = cfg.get("hook", {})
    if hk:
        png = p / "renders" / "hook.png"
        hook_png(hk["lines"], hk.get("emphasis", []), png, hcfg.get("top", 1040))
        add(png, 0, 0, f"lt(t,{hcfg.get('durationSeconds', 3)})")
    ic = cfg.get("images", {})
    for im in ov.get("images", []):
        s = im["start"] if "start" in im else cue(words, im["from"])
        e = im["end"] if "end" in im else cue(words, im["to"], s)
        scaled = p / "renders" / f"img_{len(chain)}.png"
        mw, mh = ic.get("maxWidth", 640), ic.get("maxHeight", 400)
        ff("-i", im["path"], "-vf", f"scale='min({mw},iw)':'min({mh},ih)':force_original_aspect_ratio=decrease", scaled)
        add(scaled, "(W-w)/2", ic.get("top", 1040), f"between(t,{s:.2f},{e:.2f})")
    chain.append(f"[{last}]ass={p / 'renders' / 'captions.ass'}[cap]")
    last = "cap"
    hi = ov.get("hookImage")
    if hi:
        add(hi["path"], "(W-w)/2", hi.get("top", 1260), f"between(t,{hi.get('start', 1.32)},{hi.get('end', 3.76)})")
    au = cfg.get("audio", {})
    af = (f"highpass=f=70,acompressor=threshold=-20dB:ratio=3:attack=5:release=120:makeup=2,"
          f"loudnorm=I={au.get('targetLufs', -14)}:TP={au.get('truePeakDb', -1.5)}:LRA=9,aresample=48000")
    ff("-i", p / "renders" / "cut.mov", *inputs, "-filter_complex", ";".join(chain), "-map", f"[{last}]",
       "-map", "0:a", "-af", af, "-t", f"{dur:.2f}", "-c:v", "libx264", "-preset", "medium", "-crf", 18,
       "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", a.out)
    print("wrote", a.out)


# -------------------------------------------------------------------- verify
def cmd_verify(a):
    p = Path(a.project)
    times = []
    for m in ("0:v", "0:a"):
        log = ff("-i", a.out, "-map", m, "-f", "null", "-", capture=True)
        times.append(re.findall(r"time=(\d+):(\d+):([\d.]+)", log)[-1])
    v, au = [int(h) * 3600 + int(mi) * 60 + float(s) for h, mi, s in times]
    loud = ff("-i", a.out, "-af", "ebur128=peak=true", "-f", "null", "-", capture=True)
    lufs = re.findall(r"I:\s+(-?[\d.]+) LUFS", loud)[-1]
    peak = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", loud)[-1]
    print(f"video {v:.2f} s, audio {au:.2f} s (diff {abs(v - au) * 1000:.0f} ms), {lufs} LUFS, peak {peak} dBFS")
    # Speech the gate turned down: voice in the denoised track missing after gating.
    den, sr = read_wav(p / "renders" / "audio_denoised.wav")
    gated, _ = read_wav(p / "renders" / "audio_clean.wav")
    c, g = env_db(den, sr), env_db(gated, sr)
    muted = []
    for k in json.loads((p / "renders" / "clips.json").read_text()):
        for i in range(int(k["s"] * 100), int(k["e"] * 100)):
            if c[i] > -48 and c[i] - g[i] > 6:
                muted.append(i / 100)
    print("muted speech:", "none" if not muted else f"{len(muted) * 10} ms near {sorted(set(round(t) for t in muted))} s")
    if abs(v - au) > 0.1:
        print("WARNING: audio and video lengths differ by more than 100 ms")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name, fn, args in (
            ("transcribe", cmd_transcribe, ("project", "source")),
            ("clean-audio", cmd_clean_audio, ("project", "source")),
            ("cut", cmd_cut, ("project",)),
            ("audit", cmd_audit, ("project",)),
            ("faces", cmd_faces, ("project", "source")),
            ("render", cmd_render, ("project", "source")),
            ("captions", cmd_captions, ("project",)),
            ("compose", cmd_compose, ("project", "out")),
            ("verify", cmd_verify, ("project", "out"))):
        s = sub.add_parser(name)
        for arg in args:
            s.add_argument(arg)
        if name in ("transcribe", "captions"):
            s.add_argument("--model", default="small.en")
        if name == "compose":
            s.add_argument("--overlays", help="overlays.json with hook, hookImage and images")
        s.set_defaults(fn=fn)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
