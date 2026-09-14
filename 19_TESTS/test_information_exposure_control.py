import sys,unittest
from pathlib import Path
S=Path(__file__).resolve().parents[1]/'07_SKILLS'/'amos-information-exposure-control'/'scripts';sys.path.insert(0,str(S))
from exposure_control import ExposureRuntime,ExposureError,ACCOUNTANT_KIND,validate_proof_join
from validate_exposure_control import validate_receipt

def rt():
 r=ExposureRuntime();r.set_control_state(policy_id='p',policy_version='1',policy_epoch=1,exposure_epoch=1,accountant_id='acct',accountant_version='1',accountant_kind=ACCOUNTANT_KIND);return r
def origin(r,id='o',limit=5,coalitions=['c']):return r.register_origin(origin_id=id,limit_units=limit,allowed_coalitions=coalitions,policy_id='p',policy_version='1',policy_epoch=1,exposure_epoch=1,accountant_id='acct',accountant_version='1')
def proof(skill='auth',**over):
 p=dict(proof_id='pr:'+skill,skill_id=skill,decision='PASS',effect_hash='e',semantic_transaction_hash='t',policy_id='p',policy_version='1',policy_epoch=1,authority_hash='au',environment_hash='env',capability_contract_hash='cap',proof_epoch=1);p.update(over);return p
def req(charges=None,proofs=None,required=None,**over):
 q=dict(coalition_id='c',effect_hash='e',semantic_transaction_hash='t',authorization_receipt_hash='ar',environment_hash='env',capability_contract_hash='cap',policy_id='p',policy_version='1',policy_epoch=1,exposure_epoch=1,proof_epoch=1,charges=charges or [{'origin_ref':'o','units':2}],required_skills=required or ['auth'],proofs=proofs or [proof()]);q.update(over);return q
class T(unittest.TestCase):
 def R(self):r=rt();self.addCleanup(r.close);return r
 def test_basic_commit(self):r=self.R();origin(r);self.assertEqual(r.commit(req())['state'],'COMMITTABLE_EXPOSURE');self.assertEqual(r.usage('o','c'),2)
 def test_alias_same_origin_aggregates(self):r=self.R();origin(r);r.add_alias('a','o');x=req(charges=[{'origin_ref':'o','units':1},{'origin_ref':'a','units':2}]);self.assertEqual(r.commit(x)['state'],'COMMITTABLE_EXPOSURE');self.assertEqual(r.usage('o','c'),3)
 def test_alias_does_not_reset_budget(self):r=self.R();origin(r,limit=2);r.add_alias('a','o');self.assertEqual(r.commit(req(charges=[{'origin_ref':'o','units':2}]))['state'],'COMMITTABLE_EXPOSURE');self.assertEqual(r.commit(req(charges=[{'origin_ref':'a','units':1}]))['state'],'BLOCK_BUDGET')
 def test_multi_origin_atomic_success(self):r=self.R();origin(r,'o1');origin(r,'o2');x=req(charges=[{'origin_ref':'o1','units':2},{'origin_ref':'o2','units':3}]);self.assertEqual(r.commit(x)['state'],'COMMITTABLE_EXPOSURE');self.assertEqual((r.usage('o1','c'),r.usage('o2','c')),(2,3))
 def test_multi_origin_atomic_failure(self):r=self.R();origin(r,'o1',1);origin(r,'o2',5);x=req(charges=[{'origin_ref':'o1','units':2},{'origin_ref':'o2','units':3}]);self.assertEqual(r.commit(x)['state'],'BLOCK_BUDGET');self.assertEqual((r.usage('o1','c'),r.usage('o2','c')),(0,0))
 def test_unknown_origin(self):r=self.R();origin(r);self.assertEqual(r.preflight(req(charges=[{'origin_ref':'x','units':1}]))['state'],'REVALIDATE_ORIGIN')
 def test_zero_charge_invalid(self):r=self.R();origin(r);self.assertEqual(r.preflight(req(charges=[{'origin_ref':'o','units':0}]))['state'],'REVALIDATE_ORIGIN')
 def test_wrong_coalition(self):r=self.R();origin(r);self.assertEqual(r.preflight(req(coalition_id='other'))['state'],'DENY_POLICY')
 def test_policy_epoch_stale(self):r=self.R();origin(r);self.assertEqual(r.preflight(req(policy_epoch=0))['state'],'DENY_POLICY')
 def test_exposure_epoch_stale(self):r=self.R();origin(r);self.assertEqual(r.preflight(req(exposure_epoch=0))['state'],'DENY_POLICY')
 def test_control_epoch_rollback(self):r=self.R();self.assertRaises(ExposureError,r.set_control_state,policy_id='p',policy_version='1',policy_epoch=0,exposure_epoch=1,accountant_id='acct',accountant_version='1',accountant_kind=ACCOUNTANT_KIND)
 def test_unsupported_accountant(self):r=ExposureRuntime();self.addCleanup(r.close);self.assertRaises(ExposureError,r.set_control_state,policy_id='p',policy_version='1',policy_epoch=1,exposure_epoch=1,accountant_id='x',accountant_version='1',accountant_kind='EPSILON')
 def test_origin_tamper(self):r=self.R();origin(r);r.db.execute("update origins set limit_units=99 where origin_id='o'");self.assertEqual(r.preflight(req())['state'],'REVALIDATE_ACCOUNTANT')
 def test_accountant_version_change_stales_origin(self):r=self.R();origin(r);r.set_control_state(policy_id='p',policy_version='1',policy_epoch=1,exposure_epoch=2,accountant_id='acct',accountant_version='2',accountant_kind=ACCOUNTANT_KIND);self.assertEqual(r.preflight(req(exposure_epoch=2))['state'],'REVALIDATE_ACCOUNTANT')
 def test_missing_proof(self):r=self.R();origin(r);self.assertEqual(r.preflight(req(required=['auth','x'],proofs=[proof()]))['state'],'REVALIDATE_MISSING_PROOF')
 def test_failed_proof(self):r=self.R();origin(r);self.assertEqual(r.preflight(req(proofs=[proof(decision='FAIL')]))['state'],'REVALIDATE_PROOF_JOIN')
 def test_mixed_proof_epoch(self):a=proof('a');b=proof('b',proof_epoch=2);self.assertEqual(validate_proof_join({'required_skills':['a','b'],'proofs':[a,b]})['state'],'REVALIDATE_PROOF_JOIN')
 def test_mixed_effect(self):a=proof('a');b=proof('b',effect_hash='z');self.assertEqual(validate_proof_join({'required_skills':['a','b'],'proofs':[a,b]})['state'],'REVALIDATE_PROOF_JOIN')
 def test_duplicate_skill_proof(self):a=proof('a');b=proof('a');self.assertEqual(validate_proof_join({'required_skills':['a'],'proofs':[a,b]})['state'],'REVALIDATE_PROOF_JOIN')
 def test_release_proof_binding_mismatch(self):r=self.R();origin(r);self.assertEqual(r.preflight(req(effect_hash='other'))['state'],'REVALIDATE_PROOF_JOIN')
 def test_budget_is_per_coalition(self):r=self.R();origin(r,limit=2,coalitions=['c','d']);self.assertEqual(r.commit(req())['state'],'COMMITTABLE_EXPOSURE');self.assertEqual(r.commit(req(coalition_id='d'))['state'],'COMMITTABLE_EXPOSURE')
 def test_preflight_does_not_reserve(self):r=self.R();origin(r,limit=2);self.assertEqual(r.preflight(req())['state'],'COMMITTABLE_EXPOSURE');self.assertEqual(r.usage('o','c'),0)
 def test_commit_rechecks_budget(self):r=self.R();origin(r,limit=2);self.assertEqual(r.preflight(req())['state'],'COMMITTABLE_EXPOSURE');self.assertEqual(r.commit(req())['state'],'COMMITTABLE_EXPOSURE');self.assertEqual(r.commit(req())['state'],'BLOCK_BUDGET')
 def test_sensitive_field_rejected(self):r=self.R();origin(r);x=req();x['secret']='x';self.assertEqual(r.preflight(x)['state'],'UNKNOWN_GAP')
 def test_receipt_valid(self):r=self.R();origin(r);self.assertEqual(validate_receipt(r.preflight(req())),[])
 def test_receipt_tamper(self):r=self.R();origin(r);x=r.preflight(req());x['state']='BLOCK_BUDGET';self.assertIn('receipt_hash_mismatch',validate_receipt(x))
 def test_ledger_tamper(self):r=self.R();origin(r);self.assertTrue(r.verify_ledger());r.db.execute("update ledger set payload_json='{}' where seq=1");self.assertFalse(r.verify_ledger())
 def test_context_manager_close(self):
  import sqlite3
  with ExposureRuntime() as r:r.set_control_state(policy_id='p',policy_version='1',policy_epoch=1,exposure_epoch=1,accountant_id='a',accountant_version='1',accountant_kind=ACCOUNTANT_KIND)
  self.assertRaises(sqlite3.ProgrammingError,r.db.execute,'select 1')
if __name__=='__main__':unittest.main()
