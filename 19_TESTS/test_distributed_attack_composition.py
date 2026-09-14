import importlib.util, pathlib, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]/'07_SKILLS'/'amos-distributed-attack-composition-monitor-rscf'/'scripts'
def load(n,f):
    s=importlib.util.spec_from_file_location(n,ROOT/f);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
M=load('m','composition_monitor.py'); A=load('a','audit_rscf.py')
def ev(i,t,atoms,p='p1',s='s1',ver='ALLOW',epoch=1):return {'event_id':str(i),'ts_ns':t+i,'principal_id':p,'session_id':s,'repo_id':'repo','local_verdict':ver,'atoms':atoms,'effect_hash':'e'+str(i),'target_ref':'target','policy_epoch':epoch,'provenance_ref':'prov'}
class T(unittest.TestCase):
 def setUp(self):self.m=M.Monitor();self.t=M.now_ns();self.m.add_rule('r',['A','B'],100,min_principals=2,min_sessions=2)
 def tearDown(self):self.m.close()
 def test_rule_invalid(self):
  with self.assertRaises(M.MonitorError): self.m.add_rule('x',[],1)
 def test_event_sensitive(self):
  x=ev(1,self.t,['A']);x['token']='x'
  with self.assertRaises(M.MonitorError):self.m.add_event(x)
 def test_event_invalid_verdict(self):
  x=ev(1,self.t,['A']);x['local_verdict']='MAYBE'
  with self.assertRaises(M.MonitorError):self.m.add_event(x)
 def test_no_match_empty(self):self.assertEqual(self.m.evaluate('r',self.t,1)['status'],'NO_COMPOSITION_MATCH')
 def test_missing_rule(self):self.assertEqual(self.m.evaluate('z',self.t,1)['status'],'UNKNOWN_GAP')
 def test_epoch_rule(self):self.assertEqual(self.m.evaluate('r',self.t,2)['status'],'REVALIDATE_COMPOSITION')
 def test_single_event_not_enough(self):self.m.add_event(ev(1,self.t,['A','B']));self.assertEqual(self.m.evaluate('r',self.t+2,1)['status'],'NO_COMPOSITION_MATCH')
 def test_two_principals_sessions_match(self):
  self.m.add_event(ev(1,self.t,['A'],'p1','s1'));self.m.add_event(ev(2,self.t,['B'],'p2','s2'));self.assertEqual(self.m.evaluate('r',self.t+3,1)['status'],'BLOCK_COMPOSITION')
 def test_local_deny_excluded(self):
  self.m.add_event(ev(1,self.t,['A'],'p1','s1'));self.m.add_event(ev(2,self.t,['B'],'p2','s2','DENY'));self.assertEqual(self.m.evaluate('r',self.t+3,1)['status'],'NO_COMPOSITION_MATCH')
 def test_window_excludes_old(self):
  self.m.add_event(ev(1,self.t-1000,['A'],'p1','s1'));self.m.add_event(ev(2,self.t,['B'],'p2','s2'));self.assertEqual(self.m.evaluate('r',self.t+3,1)['status'],'NO_COMPOSITION_MATCH')
 def test_mixed_event_epoch(self):
  self.m.add_event(ev(1,self.t,['A'],'p1','s1',epoch=1));self.m.add_event(ev(2,self.t,['B'],'p2','s2',epoch=2));self.assertEqual(self.m.evaluate('r',self.t+3,1)['status'],'REVALIDATE_COMPOSITION')
 def test_min_cut_excludes_irrelevant(self):
  self.m.add_event(ev(0,self.t,['X'],'p9','s9'));self.m.add_event(ev(1,self.t,['A'],'p1','s1'));self.m.add_event(ev(2,self.t,['B'],'p2','s2'));o=self.m.evaluate('r',self.t+3,1);self.assertEqual(o['minimal_event_ids'],['1','2'])
 def test_receipt_hash(self):
  self.m.add_event(ev(1,self.t,['A'],'p1','s1'));self.m.add_event(ev(2,self.t,['B'],'p2','s2'));o=self.m.evaluate('r',self.t+3,1);h=o.pop('receipt_hash');self.assertEqual(h,M.sha(o))
 def test_auditor(self):
  self.m.add_event(ev(1,self.t,['A'],'p1','s1'));self.m.add_event(ev(2,self.t,['B'],'p2','s2'));self.assertTrue(A.validate(self.m.evaluate('r',self.t+3,1)))
 def test_ledger(self):self.m.add_event(ev(1,self.t,['A']));self.assertTrue(self.m.verify_ledger())
 def test_ledger_tamper(self):self.m.add_event(ev(1,self.t,['A']));self.m.db.execute("UPDATE ledger SET payload='{}' WHERE seq=1");self.assertFalse(self.m.verify_ledger())
 def test_event_hash_stable(self):
  x=ev(1,self.t,['A']);h=self.m.add_event(x);self.assertEqual(len(h),64)
 def test_duplicate_event_rejected(self):
  x=ev(1,self.t,['A']);self.m.add_event(x)
  with self.assertRaises(Exception):self.m.add_event(x)
 def test_rule_three_atoms(self):
  self.m.add_rule('x',['A','B','C'],100,2,2);self.m.add_event(ev(1,self.t,['A','C'],'p1','s1'));self.m.add_event(ev(2,self.t,['B'],'p2','s2'));self.assertEqual(self.m.evaluate('x',self.t+3,1)['status'],'BLOCK_COMPOSITION')
 def test_same_session_blocks_threshold(self):
  self.m.add_event(ev(1,self.t,['A'],'p1','s1'));self.m.add_event(ev(2,self.t,['B'],'p2','s1'));self.assertEqual(self.m.evaluate('r',self.t+3,1)['status'],'NO_COMPOSITION_MATCH')
 def test_same_principal_blocks_threshold(self):
  self.m.add_event(ev(1,self.t,['A'],'p1','s1'));self.m.add_event(ev(2,self.t,['B'],'p1','s2'));self.assertEqual(self.m.evaluate('r',self.t+3,1)['status'],'NO_COMPOSITION_MATCH')
 def test_bound_over_12(self):
  self.m.add_rule('z',['A'],100,1,1)
  for i in range(13):self.m.add_event(ev(i,self.t,['A'],f'p{i}',f's{i}'))
  self.assertEqual(self.m.evaluate('z',self.t+20,1)['status'],'UNKNOWN_GAP')
 def test_unknown_local_not_counted(self):
  self.m.add_event(ev(1,self.t,['A'],'p1','s1','UNKNOWN'));self.m.add_event(ev(2,self.t,['B'],'p2','s2'));self.assertEqual(self.m.evaluate('r',self.t+3,1)['status'],'NO_COMPOSITION_MATCH')
 def test_single_rule_min_principal_one(self):
  self.m.add_rule('x',['A'],100,1,1);self.m.add_event(ev(1,self.t,['A']));self.assertEqual(self.m.evaluate('x',self.t+2,1)['status'],'BLOCK_COMPOSITION')
if __name__=='__main__':unittest.main()
