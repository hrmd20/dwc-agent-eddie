---
name: eddie-claude
description: Edit vertical talking-head videos in EDDIE Claude style — best-take cuts with audited word edges, face-centered alternating zooms, AI noise removal, EDDIE captions, the white text hook and the user's pictures, with frame-accurate audio/video sync. Use when the user requests EDDIE Claude.
---

# EDDIE Claude

Turn a raw 9:16 talking-head recording into a tight short: the cleanest take of every line, the presenter's face centered in every shot, clean audio with chair creaks and room noise removed, stationary EDDIE captions, the 3-second white text hook and the user's own pictures. Current user instructions override these defaults. The other EDDIE styles stay separate choices.

Settings live in `presets/eddie-claude.json` (copied into each project as `eddie.json`). The toolkit is `scripts/eddie_claude.py` beside this file; run `python3 scripts/eddie_claude.py -h` for the steps.

## Inputs and tools

Ask only for what is missing: the raw recording, an output folder, the hook wording and any pictures (and an optional hook image such as a product vial). Keep everything inside the ignored `projects/<name>/` folder.

## Setup (do this for the user)

Before the first edit, check for `.venv/bin/python` in the repository root and that `import faster_whisper, cv2, PIL, imageio_ffmpeg` succeeds with it. If anything is missing, run the setup yourself; do not send the user to install tools:

```sh
bash scripts/setup_eddie_claude.sh            # core tools, a few minutes
bash scripts/setup_eddie_claude.sh --denoise  # adds DeepFilterNet for the strongest noise removal (large download)
```

It creates an ignored `.venv` with `numpy`, `pillow`, `faster-whisper`, `opencv-python-headless<5` (OpenCV 5 removed the face detector used here) and a bundled FFmpeg via `imageio-ffmpeg` when none is installed. Run every toolkit step with `.venv/bin/python` and, if the system has no `ffmpeg`, export `FFMPEG` to the path the setup prints. Without DeepFilterNet the toolkit falls back to FFmpeg's denoiser; tell the user the cleanup is lighter and offer the `--denoise` install. The first transcription downloads the Whisper `small.en` model (about 500 MB) once. Discover local paths; never hardcode a workstation. Nothing here needs a paid service or an account.

## Workflow

Run each step from the repository root with `P=projects/<name>` and `SRC=<raw video>`.

1. **Transcribe** — `eddie_claude.py transcribe $P $SRC`. Read the whole transcript with timings.
2. **Choose takes** — write `$P/takes.json`: a list of `[start, end]` source-second ranges, one per line, in story order. Keep the cleanest complete take of each line and drop abandoned takes ("okay, I'm going to redo this"), repeated openers and restarts. Lead with the strongest hook line. Leave ~0.1 s outside the first and last word; the tool trims to speech.
3. **Clean audio** — `eddie_claude.py clean-audio $P $SRC`. DeepFilterNet removes steady noise; a gate then turns down everything that is not voice by 30 dB, which removes creaks in pauses. The gate opens on measured voice energy in the denoised track, not on transcript word times.
4. **Cut** — `eddie_claude.py cut $P` trims each take to speech, tightens pauses over 0.28 s and drops fragments under 0.2 s, then audits every clip edge.
5. **Fix every flagged edge.** Voice just outside a clip edge means a word may be split. Transcribe a short snippet across the edge and adjust `takes.json`, then rerun `cut`. Known traps:
   - ASR merges stutters: "fella– Fellas" transcribes as one word. Check the opening clip's energy for two separate bursts.
   - ASR ends spelled-out acronyms early: S-H-B-G can run ~1 s past the reported word end. Extend the take until the energy drops.
   - A short burst before speech may be the tail of the previous take. Start the clip in the silent gap after it.
6. **Faces** — `eddie_claude.py faces $P $SRC` finds the face in every clip.
7. **Render** — `eddie_claude.py render $P $SRC` crops each clip centered on the face (face at 30% from the top), alternating 1.12× and 1.30× on every cut. The slight zoom on wide shots is what allows horizontal centering. Every clip is cut on exact frame boundaries, with audio trimmed to the same length, so the audio cannot drift. The output is `renders/cut.mov`.
8. **Captions** — `eddie_claude.py captions $P` re-transcribes the cut and writes `renders/captions.ass` and `captions.srt`. Read the SRT and correct misheard terms in `$P/fixes.json` (`{"heard": "correct"}`), then rerun. Defaults already map "tea"→T and SHPG/S8→SHBG.
9. **Overlays** — write `$P/overlays.json`:
   ```json
   {"hook": {"lines": ["Normal Total Testosterone?", "Check Your Free T"], "emphasis": ["Free", "T"]},
    "hookImage": {"path": "projects/<name>/assets/vial.png", "start": 1.32, "end": 3.76},
    "images": [{"path": "projects/<name>/assets/blood.png", "from": "you need to get", "to": "most testosterone"}]}
   ```
   Images use `from`/`to` phrases from the cut (or `start`/`end` seconds); each shows from the first phrase until the second.
10. **Compose** — `eddie_claude.py compose $P <out.mp4> --overlays $P/overlays.json`.
11. **Verify** — `eddie_claude.py verify $P <out.mp4>`, then look at frames across the video.

## Visual rules

- Captions: white Arial Bold 67, 4 px black outline, shadow 1, stationary at y = 980, up to 3 words per line, breaking at sentence ends and pauses. Case as spoken. No all-caps, no colored or karaoke word highlighting.
- Hook: two white rounded boxes with black Arial Bold 58 text and the emphasis words in red, top at y = 1040, for the first 3 seconds. An optional hook image appears below it at y = 1260 from 1.32 to 3.76 s.
- Pictures: only the user's own, centered below the captions at y = 1040, at most 640 × 400, proportions kept, appearing and disappearing instantly.
- No explainer notes, fact boxes or lower-third cards unless the user asks. An optional thin white progress bar runs along the bottom edge.
- Keep the presenter's face centered in every shot, wide and zoomed.

## Verification before delivery

- Audio and video lengths match (within the AAC tail of about 50 ms) and the frame count equals the planned cut.
- No muted speech: `verify` reports none. If any is reported, fix the gate before delivery.
- Loudness about -14 LUFS, true peak at or below -1.5 dBFS.
- Re-read the cut transcript: no doubled openers, no cut-off words, no leftover retakes.
- Check frames: face centered on the vertical midline in both zoom levels, captions clear of the pictures, hook legible.
- A transcript check supplements listening; it does not prove a join sounds natural. Say so if you could not listen.

Save each revision as a newly named file in the requested folder, leaving the raw recording and earlier versions intact. For a preview request, deliver only the preview. Never commit footage, transcripts, pictures or exports; publish only reusable instructions, presets and scripts.
