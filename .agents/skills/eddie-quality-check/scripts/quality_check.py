#!/usr/bin/env python3
"""Local, non-destructive export QC. Findings are review candidates, never automatic cuts."""
import argparse, difflib, hashlib, json, math, re, shlex, subprocess
from pathlib import Path


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda: f.read(8*1024*1024), b''): h.update(b)
    return h.hexdigest()


def tokens(text):
    return re.findall(r"[\w]+(?:['’][\w]+)?", text.lower().replace('’', "'"))


def words(data):
    if isinstance(data, dict): data = data.get('segments', data.get('words', []))
    out = []
    for row in data:
        for w in row.get('words', [row]):
            text = str(w.get('word', w.get('text', ''))).strip()
            if not text: raise ValueError('Missing word text')
            a, b = float(w['start']), float(w['end'])
            if not all(math.isfinite(v) for v in (a, b)): raise ValueError('Non-finite word timing')
            out.append(dict(start=a, end=b, text=text))
    if not out: raise ValueError('No word timestamps')
    return out


def speech_findings(ws, duration, cuts, gap=.6):
    findings = []
    def add(kind, start, end, detail):
        findings.append(dict(kind=kind, start=max(0,start), end=max(0,end), detail=detail))
    for i,w in enumerate(ws):
        a,b=w['start'],w['end']
        if a < 0 or b <= a or b > duration+.1: add('word_timing', a,b,w['text'])
        if i and a < ws[i-1]['end']-.02: add('word_overlap',a,b,w['text'])
        prev=ws[i-1]['end'] if i else 0
        if a-prev>gap: add('speech_gap',prev,a,'Review breathing room; do not automatically delete.')
        for n in range(min(8,(len(ws)-i)//2),0,-1):
            left=ws[i:i+n];right=ws[i+n:i+2*n]
            if tokens(' '.join(w['text'] for w in left))==tokens(' '.join(w['text'] for w in right)) and right[0]['start']-left[-1]['end']<2:
                add('repeated_phrase',a,right[-1]['end'],' '.join(x['text'] for x in left));break
    for t in cuts:
        if not math.isfinite(t) or not 0<t<duration: raise ValueError('Cut outside export timeline')
        for w in ws:
            if w['start']-.06 <= t <= w['end']+.08:
                add('cut_near_speech',t,t,'Boundary near '+w['text']+'; inspect original audio/phonemes and listen across join.')
    if duration-ws[-1]['end']<.15:
        add('ending_tail',ws[-1]['start'],duration,'Last word has under 150 ms of trailing room; verify completeness.')
    return findings


def ass_captions(path):
    def sec(s):
        h,m,s=s.split(':');return int(h)*3600+int(m)*60+float(s)
    out=[]
    for line in Path(path).read_text().splitlines():
        if not line.startswith('Dialogue:'):continue
        cols=line.split(',',9)
        # Hooks are separate layers/styles; only spoken Caption style is checked.
        if cols[3].lower() not in ('caption','captions','default'):continue
        out.append(dict(start=sec(cols[1]),end=sec(cols[2]),text=re.sub(r'\{[^}]*\}','',cols[9]).replace('\\N',' ')))
    return out


def caption_findings(caps, ws, duration, one_word):
    findings=[]
    for i,c in enumerate(caps):
        reason=[]
        if not 0 <= c['start'] < c['end'] <= duration+.1:reason.append('invalid timing')
        if i and c['start']<caps[i-1]['end']-.01:reason.append('overlapping captions')
        if one_word and len(c['text'].strip().split())!=1:reason.append('not one word')
        if reason:findings.append(dict(kind='caption',start=c['start'],end=c['end'],detail=', '.join(reason)))
    ct=tokens(' '.join(c['text']for c in caps));wt=tokens(' '.join(w['text']for w in ws))
    if ct!=wt:findings.append(dict(kind='caption_text',start=0,end=duration,detail='Caption text differs from export transcript; review numbers, terms and omissions.'))
    if one_word and len(caps)==len(ws):
        for c,w in zip(caps,ws):
            if abs(c['start']-w['start'])>.15 or abs(c['end']-w['end'])>.2:
                findings.append(dict(kind='caption_sync',start=c['start'],end=c['end'],detail=c['text']))
    return findings


def release_status(checks, findings):
    return 'FINAL_ELIGIBLE' if all(v['status']=='Passed' for v in checks.values()) and not any(f['status']=='open' for f in findings) else 'REVIEW'


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('manifest',type=Path);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--runner',default='',help='Optional wrapper command, e.g. /path/work/run-kit')
    p.add_argument('--reviews',type=Path);p.add_argument('--clips',action='store_true')
    a=p.parse_args();m=json.loads(a.manifest.read_text());a.out.mkdir(parents=True,exist_ok=True)
    def path(k):return (a.manifest.parent/m[k]).resolve()
    media=path('media');runner=shlex.split(a.runner)
    def run(tool,args):return subprocess.run(runner+[tool]+args,capture_output=True,text=True)
    bindings={'manifest':sha(a.manifest),'media':sha(media),'scanner':sha(__file__)}
    for k in ['export_words','source_words','source_media','captions','expected_text']:
        if k in m:bindings[k]=sha(path(k))
    fingerprint=hashlib.sha256(json.dumps(bindings,sort_keys=True).encode()).hexdigest()
    checks={};findings=[]
    def check(name,status,detail):checks[name]=dict(status=status,detail=detail)
    def append(fs):findings.extend(fs)
    pr=run('ffprobe',['-v','error','-show_streams','-show_format','-of','json',str(media)])
    if pr.returncode:raise RuntimeError(pr.stderr)
    probe=json.loads(pr.stdout);duration=float(probe['format']['duration'])
    vs=next(s for s in probe['streams']if s['codec_type']=='video')
    aus=[s for s in probe['streams']if s['codec_type']=='audio']
    dimensions=m.get('dimensions',[2160,3840])
    check('dimensions','Passed'if [vs['width'],vs['height']]==dimensions else 'Needs review',f"{vs['width']}x{vs['height']}; requested {dimensions}")
    check('audio_stream','Passed'if aus else 'Needs review','Audio stream exists'if aus else 'No audio stream')
    vf='blackdetect=d=0.1:pix_th=0.10,freezedetect=n=-50dB:d=0.7'
    cmd=['-hide_banner','-nostats','-i',str(media),'-vf',vf]
    if aus:cmd+=['-af','silencedetect=n=-40dB:d=0.6,ebur128=peak=true']
    r=run('ffmpeg',cmd+['-f','null','-']);(a.out/'technical.log').write_text(r.stderr)
    check('decode','Passed'if r.returncode==0 else 'Needs review','Full-file decode exit '+str(r.returncode))
    for kind,pattern in [('black','black_start:([0-9.]+) black_end:([0-9.]+)'),('silence',r'silence_start: ([0-9.]+)[\s\S]*?silence_end: ([0-9.]+)')]:
        for x,y in re.findall(pattern,r.stderr):append([dict(kind=kind,start=float(x),end=float(y),detail='Signal-based candidate; confirm whether intentional.')])
    for x in re.findall(r'freeze_start: ([0-9.]+)',r.stderr):append([dict(kind='freeze',start=float(x),end=min(duration,float(x)+.7),detail='May be an intentional still; inspect.')])
    if aus:
        peaks=re.findall(r'Peak:\s+(-?[0-9.]+) dBFS',r.stderr)
        check('true_peak','Passed'if peaks and float(peaks[-1])<=-1 else 'Needs review',f"Encoded true peak {peaks[-1] if peaks else 'unavailable'} dBFS; target <= -1")
    loudness=re.findall(r'I:\s+(-?[0-9.]+) LUFS',r.stderr)
    measured=float(loudness[-1]) if loudness else None
    check('integrated_loudness','Passed' if measured is not None and math.isfinite(measured) and abs(measured+14)<=.5 else 'Needs review',f'Encoded integrated loudness {measured} LUFS; target -14 ±0.5')
    check('signal_scan','Passed'if r.returncode==0 and not findings else 'Needs review','See timestamped candidates; not a perceptual audio certification.')
    ws=None
    if 'export_words'in m:
        data=json.loads(path('export_words').read_text())
        provenance=data.get('provenance',{}) if isinstance(data,dict) else {}
        check('independent_export_asr','Passed' if provenance.get('media_sha256')==bindings['media'] and provenance.get('method')=='independent_export_asr_then_alignment' else 'Not checked','Requires independently transcribed exact export with hash-bound provenance')
        try:
            ws=words(data)
        except (KeyError,ValueError,TypeError) as error:
            check('speech_scan','Needs review','Incomplete alignment: '+str(error))
        if ws:
            fs=speech_findings(ws,duration,list(map(float,m.get('cuts',[]))),m.get('gap_seconds',.6));append(fs)
            check('speech_scan','Needs review'if fs else 'Passed','Word timestamps plus repeat/gap/ending candidates')
    else:check('speech_scan','Not checked','Export word transcript required')
    if 'cuts'not in m:check('cut_inventory','Not checked','Supply cut positions on export timeline; [] only for truly uncut source')
    else:check('cut_inventory','Passed',f"{len(m['cuts'])} declared joins; listening remains required")
    if ws and 'captions'in m:
        caps=ass_captions(path('captions'));fs=caption_findings(caps,ws,duration,m.get('one_word',False))
        if not caps:fs.append(dict(kind='caption_missing',start=0,end=duration,detail='No spoken caption events'))
        append(fs);check('caption_scan','Needs review'if fs else 'Passed','ASS timing/content check; rendered placement still requires visual review')
    else:check('caption_scan','Not checked','Export words and spoken ASS captions required')
    if ws and 'expected_text'in m:
        expected=tokens(path('expected_text').read_text());actual=tokens(' '.join(w['text']for w in ws))
        if expected!=actual:append([dict(kind='transcript_difference',start=0,end=duration,detail=' '.join(difflib.unified_diff(expected,actual,lineterm=''))) ])
        check('export_transcript_comparison','Passed'if expected==actual else 'Needs review','Independent ASR comparison is advisory; ASR can hide clipped syllables.')
    else:check('export_transcript_comparison','Not checked','Expected edited transcript and independently transcribed export required')
    for name in ['source_word_boundaries','every_join_listening','full_export_playback','caption_visuals_and_layout','audio_processing_review','ending_review','zoom_text_stability','repeated_sentences_review']:
        check(name,'Not checked','Reviewer must inspect exact export and record evidence')
    if 'source_words'in m and 'source_ranges'in m and 'source_media'in m:
        source_data=json.loads(path('source_words').read_text())
        if source_data.get('provenance',{}).get('media_sha256')!=bindings['source_media']:
            raise ValueError('Source alignment does not match source media')
        sw=words(source_data);boundary=[]
        for start,end in m['source_ranges']:
            if not 0<=start<end:raise ValueError('Invalid source range')
            for t in [start,end]:
                for w in sw:
                    if w['start']+.01<t<w['end']-.01:boundary.append(f"{t}: inside {w['text']}")
        check('source_word_boundaries','Needs review'if boundary else 'Passed','; '.join(boundary)or'No source cut intersects supplied aligned word intervals; listen to joins too.')
    for f in findings:
        f['id']=hashlib.sha256(json.dumps(f,sort_keys=True).encode()).hexdigest()[:12];f['status']='open'
    if a.reviews:
        rev=json.loads(a.reviews.read_text())
        if rev.get('fingerprint')!=fingerprint:raise ValueError('Stale review: export or inputs changed')
        for key,val in rev.get('checks',{}).items():
            if key not in checks or val.get('status')!='Passed' or not val.get('evidence') or not val.get('reviewer'):raise ValueError('Review needs valid check, Passed, evidence, reviewer')
            if key in ('integrated_loudness','true_peak') and checks[key]['status']!='Passed':raise ValueError('Failed loudness/peak measurement requires rerender, not manual override')
            checks[key]=dict(status='Passed',detail=val['evidence'],reviewer=val['reviewer'])
        for f in findings:
            val=rev.get('findings',{}).get(f['id'],{})
            if val.get('resolution')=='intentional' and val.get('evidence') and val.get('reviewer'):f.update(status='resolved',review=val)
    if a.clips:
        times=sorted(set(m.get('cuts',[])+[f['start']for f in findings]+[max(0,duration-5)]))
        for i,t in enumerate(times[:30]):
            clip=a.out/f'review-{i:02}-{t:.2f}.mp4'
            rr=run('ffmpeg',['-v','error','-y','-ss',str(max(0,t-1.5)),'-i',str(media),'-t','4','-vf','scale=-2:640','-c:v','libx264','-preset','ultrafast','-crf','26','-c:a','aac',str(clip)])
            if rr.returncode:raise RuntimeError(rr.stderr)
    report=dict(fingerprint=fingerprint,bindings=bindings,media=str(media),duration=duration,checks=checks,findings=findings,release_status=release_status(checks,findings))
    (a.out/'report.json').write_text(json.dumps(report,indent=2)+'\n')
    lines=['# EDDIE quality check',f"Status: **{report['release_status']}**",f'Fingerprint: `{fingerprint}`','', '| Check | Status | Detail |','|---|---|---|']
    lines += [f"| {k} | {v['status']} | {v['detail'].replace('|','/')} |" for k,v in checks.items()]
    lines+=['','## Findings']+[f"- {f['id']} — {f['start']:.2f}s: {f['kind']} — {f['detail']} ({f['status']})"for f in findings]
    (a.out/'report.md').write_text('\n'.join(lines)+'\n')
    print(report['release_status'],len(findings),'findings;',a.out/'report.md')
    return 0 if report['release_status']=='FINAL_ELIGIBLE'else 2

if __name__=='__main__':raise SystemExit(main())
