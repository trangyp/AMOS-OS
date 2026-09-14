import sys, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
S=ROOT/'07_SKILLS'/'amos-portable-agent-authorization-rscf'/'scripts'
sys.path.insert(0,str(S))
from portable_authorization import AuthorizationRuntime, AuthorizationError, resource_within
from audit_rscf import validate as validate_receipt

NOW=2_000_000_000_000_000_000

def base_rt():
    r=AuthorizationRuntime(); r.set_control_state(policy_id='p',policy_version='1',policy_epoch=1,revocation_epoch=1); return r

def root(rt, **over):
    kw=dict(issuer_id='org',issuer_key_id='key',subject_id='a',actions=['read','write'],resource_prefixes=['repo:root'],recipients=['t1','t2'],not_before_ns=NOW-100,expires_at_ns=NOW+1000,max_uses=3,consequence_ceiling='HIGH',max_delegation_depth=2,policy_id='p',policy_version='1',policy_epoch=1,issued_revocation_epoch=1,signature_policy='REQUIRED',signature_state='VERIFIED_EXTERNAL',verifier_id='v',verifier_version='1',signature_evidence_ref='e:sig')
    kw.update(over); return rt.create_root(**kw)

def child(rt,p,**over):
    kw=dict(issuer_id='a',issuer_key_id='key2',subject_id='b',actions=['read'],resource_prefixes=['repo:root/sub'],recipients=['t1'],not_before_ns=NOW-50,expires_at_ns=NOW+500,max_uses=2,consequence_ceiling='MEDIUM',max_delegation_depth=2,policy_id='p',policy_version='1',policy_epoch=1,issued_revocation_epoch=1,signature_policy='REQUIRED',signature_state='VERIFIED_EXTERNAL',verifier_id='v',verifier_version='1',signature_evidence_ref='e:child')
    kw.update(over); return rt.delegate(p,**kw)

def req(**over):
    q=dict(subject_id='b',action='read',resource='repo:root/sub/file',recipient='t1',consequence='LOW',identity_state='AUTHENTICATED',identity_evidence_ref='id:e'); q.update(over); return q

class T(unittest.TestCase):
 def rt(self):
  r=base_rt(); self.addCleanup(r.close); return r
 def test_resource_boundary(self):
  self.assertTrue(resource_within('repo:root/sub','repo:root')); self.assertFalse(resource_within('repo:rooted','repo:root'))
 def test_root_child_allow(self):
  r=self.rt(); p=root(r); c=child(r,p); self.assertEqual(r.preflight(c,req(),now_ns=NOW)['decision'],'ALLOW')
 def test_wrong_subject(self):
  r=self.rt(); c=child(r,root(r)); self.assertEqual(r.preflight(c,req(subject_id='x'),now_ns=NOW)['decision'],'DENY')
 def test_wrong_action(self):
  r=self.rt(); c=child(r,root(r)); self.assertEqual(r.preflight(c,req(action='write'),now_ns=NOW)['decision'],'DENY')
 def test_wrong_resource(self):
  r=self.rt(); c=child(r,root(r)); self.assertEqual(r.preflight(c,req(resource='repo:other'),now_ns=NOW)['decision'],'DENY')
 def test_wrong_recipient(self):
  r=self.rt(); c=child(r,root(r)); self.assertEqual(r.preflight(c,req(recipient='t2'),now_ns=NOW)['decision'],'DENY')
 def test_consequence(self):
  r=self.rt(); c=child(r,root(r)); self.assertEqual(r.preflight(c,req(consequence='HIGH'),now_ns=NOW)['decision'],'DENY')
 def test_unverified_identity_unknown(self):
  r=self.rt(); c=child(r,root(r)); self.assertEqual(r.preflight(c,req(identity_state='UNVERIFIED'),now_ns=NOW)['decision'],'UNKNOWN')
 def test_invalid_identity_deny(self):
  r=self.rt(); c=child(r,root(r)); self.assertEqual(r.preflight(c,req(identity_state='INVALID'),now_ns=NOW)['decision'],'DENY')
 def test_expired(self):
  r=self.rt(); c=child(r,root(r)); self.assertEqual(r.preflight(c,req(),now_ns=NOW+900)['decision'],'DENY')
 def test_action_widen_reject(self):
  r=self.rt(); p=root(r); self.assertRaises(AuthorizationError,child,r,p,actions=['read','delete'])
 def test_resource_widen_reject(self):
  r=self.rt(); p=root(r); self.assertRaises(AuthorizationError,child,r,p,resource_prefixes=['repo:other'])
 def test_recipient_widen_reject(self):
  r=self.rt(); p=root(r); self.assertRaises(AuthorizationError,child,r,p,recipients=['t1','t3'])
 def test_lifetime_widen_reject(self):
  r=self.rt(); p=root(r); self.assertRaises(AuthorizationError,child,r,p,expires_at_ns=NOW+2000)
 def test_use_widen_reject(self):
  r=self.rt(); p=root(r,max_uses=1); self.assertRaises(AuthorizationError,child,r,p,max_uses=2)
 def test_consequence_widen_reject(self):
  r=self.rt(); p=root(r,consequence_ceiling='LOW'); self.assertRaises(AuthorizationError,child,r,p,consequence_ceiling='MEDIUM')
 def test_issuer_mismatch_reject(self):
  r=self.rt(); p=root(r); self.assertRaises(AuthorizationError,child,r,p,issuer_id='not-a')
 def test_policy_binding_reject(self):
  r=self.rt(); p=root(r); self.assertRaises(AuthorizationError,child,r,p,policy_version='2')
 def test_signature_policy_cannot_weaken(self):
  r=self.rt(); p=root(r); self.assertRaises(AuthorizationError,child,r,p,signature_policy='OPTIONAL',signature_state='NOT_PRESENT',verifier_id=None,verifier_version=None,signature_evidence_ref=None)
 def test_verified_signature_requires_metadata(self):
  r=self.rt(); self.assertRaises(AuthorizationError,root,r,verifier_id=None)
 def test_unverified_required_signature_unknown(self):
  r=self.rt(); p=root(r,signature_state='PRESENT_UNVERIFIED',verifier_id=None,verifier_version=None,signature_evidence_ref=None); self.assertEqual(r.preflight(p,dict(subject_id='a',action='read',resource='repo:root/x',recipient='t1',consequence='LOW',identity_state='AUTHENTICATED',identity_evidence_ref='id'),now_ns=NOW)['decision'],'UNKNOWN')
 def test_invalid_signature_deny(self):
  r=self.rt(); p=root(r,signature_policy='OPTIONAL',signature_state='INVALID',verifier_id=None,verifier_version=None,signature_evidence_ref=None); self.assertEqual(r.preflight(p,dict(subject_id='a',action='read',resource='repo:root/x',recipient='t1',consequence='LOW',identity_state='AUTHENTICATED',identity_evidence_ref='id'),now_ns=NOW)['decision'],'DENY')
 def test_revoked_parent_denies_child(self):
  r=self.rt(); p=root(r); c=child(r,p); r.revoke(p,evidence_ref='rev:e',revocation_epoch=2); self.assertEqual(r.preflight(c,req(),now_ns=NOW)['decision'],'DENY')
 def test_policy_update_stales_old_auth(self):
  r=self.rt(); c=child(r,root(r)); r.set_control_state(policy_id='p',policy_version='2',policy_epoch=2,revocation_epoch=1); self.assertEqual(r.preflight(c,req(),now_ns=NOW)['decision'],'DENY')
 def test_commit_reserves_chain(self):
  r=self.rt(); p=root(r); c=child(r,p); self.assertEqual(r.commit(c,req(),now_ns=NOW)['decision'],'ALLOW'); self.assertEqual(r.db.execute('select used_count from usage where auth_id=?',(p,)).fetchone()[0],1); self.assertEqual(r.db.execute('select used_count from usage where auth_id=?',(c,)).fetchone()[0],1)
 def test_cumulative_limit_across_chain(self):
  r=self.rt(); p=root(r,max_uses=2); c=child(r,p,max_uses=1); self.assertEqual(r.commit(c,req(),now_ns=NOW)['decision'],'ALLOW'); self.assertEqual(r.commit(c,req(),now_ns=NOW)['decision'],'DENY')
 def test_preflight_not_commit(self):
  r=self.rt(); p=root(r,max_uses=1); q=dict(subject_id='a',action='read',resource='repo:root/x',recipient='t1',consequence='LOW',identity_state='AUTHENTICATED',identity_evidence_ref='id'); self.assertEqual(r.preflight(p,q,now_ns=NOW)['decision'],'ALLOW'); self.assertEqual(r.commit(p,q,now_ns=NOW)['decision'],'ALLOW'); self.assertEqual(r.commit(p,q,now_ns=NOW)['decision'],'DENY')
 def test_control_state_unknown(self):
  r=AuthorizationRuntime(); self.addCleanup(r.close); p=r.create_root(issuer_id='org',issuer_key_id='k',subject_id='a',actions=['read'],resource_prefixes=['repo:r'],recipients=['t'],not_before_ns=NOW-1,expires_at_ns=NOW+1,max_uses=1,consequence_ceiling='LOW',max_delegation_depth=0,policy_id='p',policy_version='1',policy_epoch=1,issued_revocation_epoch=1,signature_policy='OPTIONAL',signature_state='NOT_PRESENT'); q=dict(subject_id='a',action='read',resource='repo:r',recipient='t',consequence='LOW',identity_state='AUTHENTICATED',identity_evidence_ref='id'); self.assertEqual(r.preflight(p,q,now_ns=NOW)['decision'],'UNKNOWN')
 def test_depth_bound(self):
  r=self.rt(); p=root(r,max_delegation_depth=1); c=child(r,p,max_delegation_depth=1); self.assertRaises(AuthorizationError,r.delegate,c,issuer_id='b',issuer_key_id='k3',subject_id='c',actions=['read'],resource_prefixes=['repo:root/sub'],recipients=['t1'],not_before_ns=NOW-40,expires_at_ns=NOW+400,max_uses=1,consequence_ceiling='LOW',max_delegation_depth=1,policy_id='p',policy_version='1',policy_epoch=1,issued_revocation_epoch=1,signature_policy='REQUIRED',signature_state='VERIFIED_EXTERNAL',verifier_id='v',verifier_version='1',signature_evidence_ref='e')
 def test_ledger_tamper(self):
  r=self.rt(); root(r); self.assertTrue(r.verify_ledger()); r.db.execute("update ledger set payload_json='{}' where seq=1"); self.assertFalse(r.verify_ledger())
 def test_parent_object_tamper_blocks_delegation(self):
  r=self.rt(); p=root(r); r.db.execute("update authz set actions_json='[\"read\",\"write\",\"delete\"]' where auth_id=?",(p,)); self.assertRaises(AuthorizationError,child,r,p)
 def test_leaf_object_tamper_denies(self):
  r=self.rt(); c=child(r,root(r)); r.db.execute("update authz set resources_json='[\"repo:other\"]' where auth_id=?",(c,)); out=r.preflight(c,req(),now_ns=NOW); self.assertEqual(out['decision'],'DENY'); self.assertTrue(any(x.startswith('authorization_object_hash_mismatch:') for x in out['reasons']))
 def test_receipt_auditor_accepts_runtime_receipt(self):
  r=self.rt(); c=child(r,root(r)); out=r.preflight(c,req(),now_ns=NOW); self.assertEqual(validate_receipt(out),[])
 def test_receipt_auditor_detects_tamper(self):
  r=self.rt(); c=child(r,root(r)); out=r.preflight(c,req(),now_ns=NOW); out['decision']='DENY'; self.assertIn('receipt_hash_mismatch',validate_receipt(out))
 def test_control_epoch_rollback_rejected(self):
  r=self.rt(); self.assertRaises(AuthorizationError,r.set_control_state,policy_id='p',policy_version='0',policy_epoch=0,revocation_epoch=1)
 def test_revocation_epoch_must_advance(self):
  r=self.rt(); p=root(r); self.assertRaises(AuthorizationError,r.revoke,p,evidence_ref='rev:e',revocation_epoch=1)
 def test_missing_identity_evidence_unknown(self):
  r=self.rt(); c=child(r,root(r)); q=req(); q['identity_evidence_ref']=''; self.assertEqual(r.preflight(c,q,now_ns=NOW)['decision'],'UNKNOWN')
 def test_missing_request_field_unknown(self):
  r=self.rt(); c=child(r,root(r)); q=req(); q.pop('recipient'); self.assertEqual(r.preflight(c,q,now_ns=NOW)['decision'],'UNKNOWN')
 def test_context_manager_closes(self):
  import sqlite3
  with AuthorizationRuntime() as r: r.set_control_state(policy_id='p',policy_version='1',policy_epoch=1,revocation_epoch=1)
  self.assertRaises(sqlite3.ProgrammingError,r.db.execute,'select 1')
 def test_sensitive_request_rejected(self):
  r=self.rt(); p=root(r); q=dict(subject_id='a',action='read',resource='repo:root/x',recipient='t1',consequence='LOW',identity_state='AUTHENTICATED',identity_evidence_ref='id',secret='x'); self.assertRaises(AuthorizationError,r.preflight,p,q,now_ns=NOW)

if __name__=='__main__': unittest.main()
