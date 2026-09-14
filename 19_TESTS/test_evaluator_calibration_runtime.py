import importlib.util
import json
import math
import pathlib
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
RUNTIME_PATH = ROOT / "07_SKILLS/amos-evaluator-calibration-rscf/scripts/evaluator_calibration.py"
VALIDATOR_PATH = ROOT / "07_SKILLS/amos-evaluator-calibration-rscf/scripts/calibration_contract_check.py"

spec = importlib.util.spec_from_file_location("evaluator_calibration", RUNTIME_PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

vspec = importlib.util.spec_from_file_location("calibration_contract_check", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(vspec)
vspec.loader.exec_module(validator)

CalibrationRuntime = mod.CalibrationRuntime
CalibrationError = mod.CalibrationError


class CalibrationRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.rt = CalibrationRuntime()
        self.cfg = "a" * 64

    def tearDown(self):
        self.rt.close()

    def mk_cal(self, **kw):
        args = dict(
            phase="CALIBRATION", evaluator_id="judge", evaluator_version="1", evaluator_kind="MODEL_JUDGE",
            evaluator_config_hash=self.cfg, cohort_hash="b"*64, expected_count=2,
            reference_source_id="panel", reference_source_version="1", reference_kind="HUMAN",
            reference_independence="INDEPENDENT", score_semantics="PROBABILITY_PASS",
            threshold_value=0.5, threshold_source="CALIBRATION_DERIVED",
        )
        args.update(kw)
        return self.rt.create_session(**args)

    def seal_cal(self, **kw):
        sid = self.mk_cal(**kw)
        self.rt.record_observation(sid, "c1", reference_label="PASS", evaluator_label="PASS", score=0.9, evidence_ref="e:c1")
        self.rt.record_observation(sid, "c2", reference_label="FAIL", evaluator_label="FAIL", score=0.1, evidence_ref="e:c2")
        self.rt.seal_session(sid)
        return sid

    def mk_val(self, parent=None, **kw):
        parent = parent or self.seal_cal()
        args = dict(
            phase="VALIDATION", evaluator_id="judge", evaluator_version="1", evaluator_kind="MODEL_JUDGE",
            evaluator_config_hash=self.cfg, cohort_hash="c"*64, expected_count=2,
            reference_source_id="panel", reference_source_version="1", reference_kind="HUMAN",
            reference_independence="INDEPENDENT", score_semantics="PROBABILITY_PASS",
            threshold_value=0.5, threshold_source="CALIBRATION_DERIVED", parent_calibration_id=parent,
        )
        args.update(kw)
        return self.rt.create_session(**args)

    def seal_val(self, parent=None, rows=None, **kw):
        sid = self.mk_val(parent=parent, **kw)
        rows = rows or [
            ("v1", "PASS", "PASS", 0.8),
            ("v2", "FAIL", "FAIL", 0.2),
        ]
        for task, ref, pred, score in rows:
            self.rt.record_observation(sid, task, reference_label=ref, evaluator_label=pred, score=score, evidence_ref=f"e:{task}")
        self.rt.seal_session(sid)
        return sid

    def test_01_identity_hash_required(self):
        with self.assertRaises(CalibrationError): self.mk_cal(evaluator_config_hash="bad")

    def test_02_invalid_phase_rejected(self):
        with self.assertRaises(CalibrationError): self.mk_cal(phase="TEST")

    def test_03_raw_sensitive_metadata_rejected(self):
        sid = self.mk_cal()
        with self.assertRaises(CalibrationError):
            self.rt.record_observation(sid, "x", reference_label="PASS", evaluator_label="PASS", score=.8, evidence_ref="e", metadata={"prompt":"secret"})

    def test_04_probability_range_enforced(self):
        sid = self.mk_cal()
        with self.assertRaises(CalibrationError):
            self.rt.record_observation(sid, "x", reference_label="PASS", evaluator_label="PASS", score=1.1, evidence_ref="e")

    def test_05_score_forbidden_when_none(self):
        sid = self.mk_cal(score_semantics="NONE", threshold_value=None, threshold_source="NOT_APPLICABLE")
        with self.assertRaises(CalibrationError):
            self.rt.record_observation(sid, "x", reference_label="PASS", evaluator_label="PASS", score=.4, evidence_ref="e")

    def test_06_confusion_counts(self):
        sid = self.mk_cal(expected_count=4)
        rows=[("a","PASS","PASS",.8),("b","FAIL","FAIL",.2),("c","FAIL","PASS",.7),("d","PASS","FAIL",.3)]
        for t,r,p,s in rows: self.rt.record_observation(sid,t,reference_label=r,evaluator_label=p,score=s,evidence_ref="e:"+t)
        report=self.rt.seal_session(sid)
        self.assertEqual(report["confusion"], {"tp":1,"tn":1,"fp":1,"fn":1})
        self.assertAlmostEqual(report["selective_accuracy"], .5)

    def test_07_abstention_is_separate_from_accuracy(self):
        sid=self.mk_cal(expected_count=2)
        self.rt.record_observation(sid,"a",reference_label="PASS",evaluator_label="PASS",score=.8,evidence_ref="e:a")
        self.rt.record_observation(sid,"b",reference_label="FAIL",evaluator_label="ABSTAIN",score=.4,evidence_ref="e:b")
        r=self.rt.seal_session(sid)
        self.assertAlmostEqual(r["selective_accuracy"],1.0)
        self.assertAlmostEqual(r["classification_coverage"],.5)
        self.assertAlmostEqual(r["abstention_rate"],.5)

    def test_08_wilson_interval_is_bounded(self):
        lo,hi=mod.wilson_interval(0,1)
        self.assertEqual(lo,0.0)
        self.assertTrue(0 < hi < 1)
        lo2,hi2=mod.wilson_interval(1,1)
        self.assertTrue(0 < lo2 < 1)
        self.assertEqual(hi2,1.0)

    def test_09_wilson_zero_n_is_unknown(self):
        self.assertIsNone(mod.wilson_interval(0,0))

    def test_10_brier_exact(self):
        self.assertAlmostEqual(mod.brier_score([.9,.1],[1,0]), .01)

    def test_11_ece_exact_fixed_bins(self):
        self.assertAlmostEqual(mod.expected_calibration_error([.9,.1],[1,0],bins=2), .1)

    def test_12_rank_score_does_not_generate_probability_metrics(self):
        sid=self.mk_cal(score_semantics="RANK_SCORE", threshold_value=0.5, threshold_source="FIXED")
        self.rt.record_observation(sid,"a",reference_label="PASS",evaluator_label="PASS",score=10,evidence_ref="e:a")
        r=self.rt.seal_session(sid)
        self.assertIsNone(r["brier_score"])
        self.assertIsNone(r["ece"])

    def test_13_probability_missingness_explicit(self):
        sid=self.mk_cal()
        self.rt.record_observation(sid,"a",reference_label="PASS",evaluator_label="PASS",score=None,evidence_ref="e:a")
        r=self.rt.seal_session(sid)
        self.assertFalse(r["probability_complete"])
        self.assertEqual(r["probability_count"],0)

    def test_14_incomplete_expected_coverage_preserved(self):
        sid=self.mk_cal(expected_count=2)
        self.rt.record_observation(sid,"a",reference_label="PASS",evaluator_label="PASS",score=.8,evidence_ref="e:a")
        r=self.rt.seal_session(sid)
        self.assertAlmostEqual(r["observed_coverage"],.5)

    def test_15_validation_requires_parent(self):
        with self.assertRaises(CalibrationError): self.mk_val(parent_calibration_id=None, parent="missing")

    def test_16_validation_parent_must_be_sealed(self):
        cal=self.mk_cal()
        with self.assertRaises(CalibrationError): self.mk_val(parent=cal)

    def test_17_validation_cohort_must_be_held_out(self):
        cal=self.seal_cal(cohort_hash="d"*64)
        with self.assertRaises(CalibrationError): self.mk_val(parent=cal, cohort_hash="d"*64)

    def test_18_validation_threshold_frozen(self):
        cal=self.seal_cal()
        with self.assertRaises(CalibrationError): self.mk_val(parent=cal, threshold_value=.6)

    def test_19_validation_identity_frozen(self):
        cal=self.seal_cal()
        with self.assertRaises(CalibrationError): self.mk_val(parent=cal, evaluator_version="2")

    def test_20_calibration_phase_cannot_pass_reliability_gate(self):
        cal=self.seal_cal()
        g=self.rt.reliability_gate(cal,{"min_observed_coverage":1.0})
        self.assertEqual(g["verdict"],"INCONCLUSIVE")

    def test_21_validation_policy_pass(self):
        val=self.seal_val()
        g=self.rt.reliability_gate(val,{"min_observed_coverage":1.0,"min_selective_accuracy":.9,"max_brier_score":.1,"require_independent_reference":True,"require_probability_complete":True})
        self.assertEqual(g["verdict"],"PASS")

    def test_22_validation_policy_fail(self):
        val=self.seal_val(rows=[("v1","PASS","FAIL",.2),("v2","FAIL","PASS",.8)])
        g=self.rt.reliability_gate(val,{"min_selective_accuracy":.9})
        self.assertEqual(g["verdict"],"FAIL")

    def test_23_missing_probability_metric_is_inconclusive(self):
        cal=self.seal_cal(score_semantics="RANK_SCORE",threshold_source="FIXED")
        val=self.seal_val(parent=cal,score_semantics="RANK_SCORE",threshold_source="FIXED")
        g=self.rt.reliability_gate(val,{"max_brier_score":.2})
        self.assertEqual(g["verdict"],"INCONCLUSIVE")

    def test_24_reference_independence_gate(self):
        cal=self.seal_cal(reference_independence="RELATED")
        val=self.seal_val(parent=cal,reference_independence="RELATED")
        g=self.rt.reliability_gate(val,{"require_independent_reference":True})
        self.assertEqual(g["verdict"],"FAIL")

    def test_25_unknown_policy_field_rejected(self):
        val=self.seal_val()
        with self.assertRaises(CalibrationError): self.rt.reliability_gate(val,{"magic":1})

    def test_26_invalid_policy_bound_rejected(self):
        val=self.seal_val()
        with self.assertRaises(CalibrationError): self.rt.reliability_gate(val,{"min_selective_accuracy":1.2})

    def _different_evaluator_validation(self, version="2", cfg="d"*64, rows=None, ref="panel"):
        cal=self.seal_cal(evaluator_version=version,evaluator_config_hash=cfg,cohort_hash="e"*64,reference_source_id=ref)
        val=self.seal_val(parent=cal,evaluator_version=version,evaluator_config_hash=cfg,cohort_hash="c"*64,reference_source_id=ref,rows=rows)
        return val

    def test_27_drift_comparable_with_evaluator_version_axis(self):
        b=self.seal_val()
        c=self._different_evaluator_validation(rows=[("v1","PASS","PASS",.7),("v2","FAIL","PASS",.6)])
        d=self.rt.compare_drift(b,c)
        self.assertEqual(d["state"],"COMPARABLE")
        self.assertEqual(d["prediction_change_task_ids"],["v2"])
        self.assertAlmostEqual(d["delta_selective_accuracy"],-.5)

    def test_28_drift_reference_mismatch_not_comparable(self):
        b=self.seal_val()
        c=self._different_evaluator_validation(ref="other-panel")
        d=self.rt.compare_drift(b,c)
        self.assertEqual(d["state"],"NOT_COMPARABLE")
        self.assertTrue(any("reference_source_id" in x for x in d["reasons"]))

    def test_29_drift_task_set_mismatch_not_comparable(self):
        b=self.seal_val()
        c=self._different_evaluator_validation(rows=[("v1","PASS","PASS",.8)])
        d=self.rt.compare_drift(b,c)
        self.assertEqual(d["state"],"NOT_COMPARABLE")
        self.assertIn("observed task set mismatch",d["reasons"])

    def test_30_sealed_session_rejects_late_observation(self):
        sid=self.seal_cal()
        with self.assertRaises(CalibrationError):
            self.rt.record_observation(sid,"late",reference_label="PASS",evaluator_label="PASS",score=.9,evidence_ref="e")

    def test_31_duplicate_observation_rejected(self):
        sid=self.mk_cal()
        self.rt.record_observation(sid,"a",reference_label="PASS",evaluator_label="PASS",score=.8,evidence_ref="e")
        with self.assertRaises(CalibrationError): self.rt.record_observation(sid,"a",reference_label="PASS",evaluator_label="PASS",score=.8,evidence_ref="e")

    def test_32_over_observation_rejected_on_seal(self):
        sid=self.mk_cal(expected_count=1)
        self.rt.record_observation(sid,"a",reference_label="PASS",evaluator_label="PASS",score=.8,evidence_ref="e:a")
        self.rt.record_observation(sid,"b",reference_label="FAIL",evaluator_label="FAIL",score=.2,evidence_ref="e:b")
        with self.assertRaises(CalibrationError): self.rt.seal_session(sid)

    def test_33_ledger_tamper_detected(self):
        sid=self.seal_cal()
        self.assertTrue(self.rt.verify_ledger())
        self.rt.db.execute("UPDATE ledger SET payload_json='{}' WHERE seq=1")
        self.rt.db.commit()
        self.assertFalse(self.rt.verify_ledger())

    def test_34_report_validator_accepts_report(self):
        report=self.rt.report(self.seal_val())
        self.assertTrue(validator.validate(report))

    def test_35_gate_validator_accepts_gate(self):
        val=self.seal_val()
        self.assertTrue(validator.validate(self.rt.reliability_gate(val,{"min_selective_accuracy":.5})))

    def test_36_drift_validator_accepts_drift(self):
        b=self.seal_val(); c=self._different_evaluator_validation()
        self.assertTrue(validator.validate(self.rt.compare_drift(b,c)))

    def test_37_validator_rejects_raw_content(self):
        val=self.seal_val(); gate=self.rt.reliability_gate(val,{})
        gate["prompt"]="secret"
        with self.assertRaises(validator.ContractError): validator.validate(gate)


if __name__ == "__main__":
    unittest.main()
