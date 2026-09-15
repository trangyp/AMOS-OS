import importlib.util, pathlib, unittest, tempfile
P=pathlib.Path(__file__).resolve().parents[1]/'07_SKILLS'/'amos-managed-autonomy-escalation-rscf'/'scripts'/'managed_autonomy.py'
spec=importlib.util.spec_from_file_location('ma',P); ma=importlib.util.module_from_spec(spec); spec.loader.exec_module(ma)

class T(unittest.TestCase):
    def rt(self, **kw):
        r=ma.Runtime(); lid=r.create('a', **kw); self.addCleanup(r.close); return r,lid
    def ev(self,r,lid,k,pe=1,ae=1): r.add_evidence(lid,k,k,policy_epoch=pe,authority_epoch=ae)
    def test_stable(self): r,l=self.rt(); self.assertEqual(r.decide(l)['output'],'CONTINUE_STABLE')
    def test_soft_to_local(self): r,l=self.rt(); self.ev(r,l,'SOFT_DEGRADATION'); self.assertEqual(r.decide(l)['target_state'],'LOCAL_RECOVERY')
    def test_hard_to_suspend(self): r,l=self.rt(); self.ev(r,l,'HARD_INVARIANT_FAILURE'); self.assertEqual(r.decide(l)['target_state'],'SUSPENDED')
    def test_authority_stale_suspend(self): r,l=self.rt(); self.ev(r,l,'AUTHORITY_STALE'); self.assertEqual(r.decide(l)['target_state'],'SUSPENDED')
    def test_external_block_suspend(self): r,l=self.rt(); self.ev(r,l,'EXTERNAL_BLOCK'); self.assertEqual(r.decide(l)['target_state'],'SUSPENDED')
    def test_gap_assisted(self): r,l=self.rt(); self.ev(r,l,'EVIDENCE_GAP'); self.assertEqual(r.decide(l)['target_state'],'ASSISTED_RECOVERY')
    def test_disagreement_assisted(self): r,l=self.rt(); self.ev(r,l,'PERSISTENT_DISAGREEMENT'); self.assertEqual(r.decide(l)['target_state'],'ASSISTED_RECOVERY')
    def test_local_budget(self):
        r,l=self.rt(max_local=1); self.ev(r,l,'SOFT_DEGRADATION'); r.apply(r.decide(l)); self.assertEqual(r.decide(l)['target_state'],'ASSISTED_RECOVERY')
    def test_assisted_denial_surrender(self): r,l=self.rt(); self.ev(r,l,'ASSISTED_DENIAL'); self.assertEqual(r.decide(l)['target_state'],'SURRENDERED')
    def test_terminal_no_resume(self):
        r,l=self.rt(); self.ev(r,l,'ASSISTED_DENIAL'); r.apply(r.decide(l)); self.ev(r,l,'RECOVERY_SUCCESS'); self.ev(r,l,'ASSISTED_APPROVAL'); self.assertEqual(r.decide(l)['target_state'],'SURRENDERED')
    def test_suspend_needs_both(self):
        r,l=self.rt(); self.ev(r,l,'EXTERNAL_BLOCK'); r.apply(r.decide(l)); self.assertEqual(r.decide(l)['output'],'REMAIN_CONTAINED')
    def test_stale_receipt(self):
        r,l=self.rt(); self.ev(r,l,'SOFT_DEGRADATION'); rec=r.decide(l); r.apply(rec); self.assertRaises(ma.LifecycleError,r.apply,rec)
    def test_epoch_rollback(self): r,l=self.rt(); self.assertRaises(ma.LifecycleError,r.update_epochs,l,policy_epoch=0)
    def test_old_evidence_stale_after_epoch_change(self):
        r,l=self.rt(); self.ev(r,l,'SOFT_DEGRADATION'); r.update_epochs(l,policy_epoch=2); self.assertEqual(r.decide(l)['target_state'],'SUSPENDED')
    def test_receipt_hash(self):
        r,l=self.rt(); rec=r.decide(l); rec['target_state']='SURRENDERED'; self.assertRaises(ma.LifecycleError,r.apply,rec)
    def test_invalid_evidence(self): r,l=self.rt(); self.assertRaises(ma.LifecycleError,self.ev,r,l,'NOPE')
    def test_invalid_config(self):
        r=ma.Runtime(); self.addCleanup(r.close); self.assertRaises(ma.LifecycleError,r.create,'a',max_local=-1)
    def test_ledger(self): r,l=self.rt(); self.ev(r,l,'SOFT_DEGRADATION'); r.apply(r.decide(l)); self.assertTrue(r.verify_ledger())
    def test_ledger_tamper(self):
        r,l=self.rt(); r.db.execute("UPDATE ledger SET payload='{}' WHERE seq=1"); r.db.commit(); self.assertFalse(r.verify_ledger())
    def test_fence_increment(self):
        r,l=self.rt(); self.ev(r,l,'SOFT_DEGRADATION'); out=r.apply(r.decide(l)); self.assertEqual(out['fence_epoch'],1)
    def test_same_state_no_fence_increment(self):
        r,l=self.rt(); rec=r.decide(l); out=r.apply(rec); self.assertEqual(out['fence_epoch'],0)
    def test_context_close(self):
        with ma.Runtime() as r: l=r.create('a'); self.assertEqual(r.decide(l)['current_state'],'STABLE')
    def test_assisted_exhaustion(self):
        r,l=self.rt(max_assisted=0); self.ev(r,l,'EVIDENCE_GAP'); r.apply(r.decide(l)); self.assertEqual(r.decide(l)['target_state'],'SURRENDERED')
    def test_resume_budget_not_reset(self):
        r,l=self.rt(max_local=2); self.ev(r,l,'SOFT_DEGRADATION'); r.apply(r.decide(l)); self.ev(r,l,'RECOVERY_SUCCESS'); r.apply(r.decide(l)); row=r._get(l); self.assertEqual(row['local_attempts'],1)

if __name__=='__main__': unittest.main()
