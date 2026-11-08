#!/usr/bin/env python3
"""Local WhisperX alignment. --transcript aligns existing segments; omit for independent export ASR."""
import argparse,hashlib,json,os,shlex,subprocess,tempfile
from pathlib import Path
os.environ.setdefault('HF_HUB_DISABLE_TELEMETRY','1')
os.environ.setdefault('DO_NOT_TRACK','1')

def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('media',type=Path);p.add_argument('--out',type=Path,required=True)
 p.add_argument('--transcript',type=Path);p.add_argument('--cache',type=Path,required=True)
 p.add_argument('--runner',default='');p.add_argument('--model',default='small.en')
 a=p.parse_args();a.cache.mkdir(parents=True,exist_ok=True)
 import numpy as np
 import whisperx
 import nltk
 nltk_dir=str(a.cache/'nltk_data');nltk.data.path.insert(0,nltk_dir)
 try:nltk.data.find('tokenizers/punkt_tab/english/')
 except LookupError:nltk.download('punkt_tab',download_dir=nltk_dir,quiet=True,raise_on_error=True)
 from faster_whisper import WhisperModel
 with tempfile.TemporaryDirectory() as tmp:
  raw=Path(tmp)/'audio.f32'
  subprocess.run(shlex.split(a.runner)+['ffmpeg','-v','error','-y','-i',str(a.media),'-vn','-ac','1','-ar','16000','-f','f32le',str(raw)],check=True)
  audio=np.fromfile(raw,dtype=np.float32)
  if a.transcript:
   data=json.loads(a.transcript.read_text());segments=data.get('segments',[])if isinstance(data,dict)else data
   method='aligned_existing_transcript'
  else:
   model=WhisperModel(a.model,device='cpu',compute_type='int8',cpu_threads=6,download_root=str(a.cache))
   ss,_=model.transcribe(audio,language='en',beam_size=5,vad_filter=True)
   segments=[dict(start=s.start,end=s.end,text=s.text)for s in ss]
   method='independent_export_asr_then_alignment'
  model,meta=whisperx.load_align_model(language_code='en',device='cpu',model_dir=str(a.cache))
  result=whisperx.align(segments,model,meta,audio,'cpu',return_char_alignments=False)
  h=hashlib.sha256()
  with a.media.open('rb')as f:
   for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
  result['provenance']=dict(media_sha256=h.hexdigest(),method=method,asr_model=a.model)
  a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,indent=2)+'\n')
  print(a.out)
if __name__=='__main__':main()
