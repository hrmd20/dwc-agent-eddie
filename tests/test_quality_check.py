import importlib.util, unittest
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'.claude/skills/eddie-quality-check/scripts/quality_check.py'
spec=importlib.util.spec_from_file_location('qc',P);qc=importlib.util.module_from_spec(spec);spec.loader.exec_module(qc)
def w(t,a,b):return dict(text=t,start=a,end=b)
class QualityChecks(unittest.TestCase):
 def test_cut_clips_dollars(self):
  fs=qc.speech_findings([w('thousand',0,.3),w('dollars',.4,1.1)],1.5,[.85])
  self.assertTrue(any(f['kind']=='cut_near_speech'for f in fs))
 def test_repeated_so(self):
  self.assertTrue(any(f['kind']=='repeated_phrase'for f in qc.speech_findings([w('So',0,.2),w('so',.3,.5)],1,[])))
 def test_repeated_phrase(self):
  ws=[w('when',0,.2),w('you',.2,.3),w('take',.3,.5),w('when',.6,.8),w('you',.8,.9),w('take',.9,1.1)]
  self.assertTrue(any(f['kind']=='repeated_phrase'and f['detail']=='when you take'for f in qc.speech_findings(ws,2,[])))
 def test_natural_pause_not_cut(self):
  fs=qc.speech_findings([w('first',0,.3),w('second',.7,1)],1.5,[])
  self.assertFalse(any(f['kind']=='speech_gap'for f in fs))
 def test_long_gap(self):
  self.assertTrue(any(f['kind']=='speech_gap'for f in qc.speech_findings([w('first',0,.3),w('second',1.1,1.4)],2,[])))
 def test_incomplete_ending(self):
  self.assertTrue(any(f['kind']=='ending_tail'for f in qc.speech_findings([w('patients',0,.99)],1,[])))
 def test_caption_overlap_and_multiword(self):
  cs=[w('hello there',0,.8),w('doctor',.7,1)]
  fs=qc.caption_findings(cs,[w('hello',0,.2),w('there',.2,.8),w('doctor',.8,1)],2,True)
  self.assertTrue(any('not one word'in f['detail']for f in fs));self.assertTrue(any('overlapping'in f['detail']for f in fs))
 def test_missing_listening_blocks_final(self):
  self.assertEqual(qc.release_status({'decode':{'status':'Passed'},'listening':{'status':'Not checked'}},[]),'REVIEW')
 def test_open_finding_blocks_final(self):
  self.assertEqual(qc.release_status({'decode':{'status':'Passed'}},[{'status':'open'}]),'REVIEW')
 def test_resolved_checks_release(self):
  self.assertEqual(qc.release_status({'decode':{'status':'Passed'}},[{'status':'resolved'}]),'FINAL_ELIGIBLE')
 def test_invalid_word_timestamp(self):
  with self.assertRaises(ValueError):qc.words([w('hello',float('nan'),1)])
 def test_one_word_valid(self):
  ws=[w('hello',0,.3),w('doctor',.3,.7)]
  self.assertEqual(qc.caption_findings(ws,ws,1,True),[])
if __name__=='__main__':unittest.main()
