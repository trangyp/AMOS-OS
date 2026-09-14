import json,tempfile,unittest
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
S=ROOT/'07_SKILLS'/'amos-formal-agent-skill-verification-rscf'/'scripts'
sys.path.insert(0,str(S))
from verify_skill import verify

class T(unittest.TestCase):
 def run_case(self,code,allowed):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d); (p/'scripts').mkdir(); (p/'scripts'/'x.py').write_text(code,encoding='utf-8'); m=p/'m.json'; m.write_text(json.dumps({'allowed_effects':allowed}),encoding='utf-8'); return verify(p,m)
 def test_read_contained(self): self.assertEqual(self.run_case("open('x').read()",['FS_READ'])['verdict'],'CONTAINED')
 def test_write_violation(self): self.assertEqual(self.run_case("open('x','w').write('a')",[])['verdict'],'VIOLATION')
 def test_process(self): self.assertIn('PROCESS_EXEC',self.run_case("import subprocess\nsubprocess.run(['x'])",['PROCESS_EXEC'])['observed_effects'])
 def test_network(self): self.assertIn('NETWORK',self.run_case("import requests\nrequests.get('https://x')",['NETWORK'])['observed_effects'])
 def test_eval(self): self.assertIn('DYNAMIC_CODE',self.run_case("eval('1')",['DYNAMIC_CODE'])['observed_effects'])
 def test_dynamic_import(self): self.assertIn('DYNAMIC_IMPORT',self.run_case("__import__('x')",['DYNAMIC_IMPORT'])['observed_effects'])
 def test_env(self): self.assertIn('ENV_READ',self.run_case("import os\nos.getenv('X')",['ENV_READ'])['observed_effects'])
 def test_pickle(self): self.assertIn('SERIALIZATION_UNSAFE',self.run_case("import pickle\npickle.loads(b'x')",['SERIALIZATION_UNSAFE'])['observed_effects'])
 def test_path_write(self): self.assertIn('FS_WRITE',self.run_case("from pathlib import Path\nPath('x').write_text('a')",['FS_WRITE'])['observed_effects'])
 def test_path_read(self): self.assertIn('FS_READ',self.run_case("from pathlib import Path\nPath('x').read_text()",['FS_READ'])['observed_effects'])
 def test_reflection_unknown(self): self.assertEqual(self.run_case("getattr(x,name)()",[])['verdict'],'UNKNOWN')
 def test_parse_failure(self): self.assertEqual(self.run_case("if :",[])['verdict'],'VIOLATION')
 def test_receipt_hash(self): self.assertEqual(len(self.run_case("x=1",[])['receipt_hash']),64)
 def test_empty_contained(self): self.assertEqual(self.run_case("x=1",[])['verdict'],'CONTAINED')
 def test_multiple_effects(self):
  r=self.run_case("import os,subprocess\nos.getenv('X')\nsubprocess.run(['x'])",['ENV_READ','PROCESS_EXEC']); self.assertEqual(r['verdict'],'CONTAINED')

if __name__=='__main__': unittest.main()
