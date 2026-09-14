from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

RUNTIME = Path(__file__).parents[1] / "07_SKILLS/amos-interactive-evaluation-design-rscf/scripts/evaluation_runtime.py"
spec = importlib.util.spec_from_file_location("amos_eval_runtime", RUNTIME)
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
assert spec.loader is not None
spec.loader.exec_module(mod)
EvaluationRuntime = mod.EvaluationRuntime
EvaluationError = mod.EvaluationError

H = "a" * 64


def make_run(rt: EvaluationRuntime, **overrides):
    args = dict(
        suite_id="suite-1",
        target_id="agent-x",
        target_version="v1",
        environment_id="env-lock-1",
        harness_id="harness-x",
        harness_version="h1",
        evaluator_set_id="eval-set-1",
        evaluator_version="e1",
        model_id="model-fixed",
        model_config_hash=H,
        budget_id="budget-fixed",
        task_cohort_hash="b" * 64,
        evidence_archetype="PROCESS",
        expected_task_count=2,
        trace_id="trace-1",
        roundtrip_receipt_hash="c" * 64,
    )
    args.update(overrides)
    return rt.create_run(**args)


def add_task(rt, run_id, task_id, outcome="PASS", process="PASS", safety="PASS", critical=False):
    return rt.record_task_result(
        run_id,
        task_id,
        outcome_state=outcome,
        process_state=process,
        safety_state=safety,
        recovered=False,
        critical_failure=critical,
        evidence={"artifact_hash": "d" * 64, "status": outcome},
    )


class EvaluationRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.rt = EvaluationRuntime(Path(self.tmp.name) / "eval.db")

    def tearDown(self):
        self.rt.close()
        self.tmp.cleanup()

    def test_run_receipt_binds_identity_without_raw_content(self):
        r = make_run(self.rt)
        add_task(self.rt, r, "t1")
        add_task(self.rt, r, "t2")
        receipt = self.rt.seal_run(r)
        self.assertTrue(receipt["coverage_complete"])
        self.assertEqual(receipt["model_config_hash"], H)
        self.assertEqual(receipt["authority_semantics"], "EVALUATION_DOES_NOT_GRANT_AUTHORITY")
        self.assertNotIn("prompt", receipt)
        self.assertEqual(len(receipt["receipt_hash"]), 64)

    def test_raw_sensitive_evidence_rejected(self):
        r = make_run(self.rt)
        with self.assertRaises(EvaluationError):
            self.rt.record_task_result(
                r, "t1", outcome_state="PASS", process_state="PASS", safety_state="PASS",
                recovered=False, critical_failure=False, evidence={"prompt": "secret"}
            )

    def test_review_continue_is_recorded_not_authority(self):
        r = make_run(self.rt)
        rid = self.rt.record_review(
            r, "t1", stage="TOOL_RESULT", reviewer_id="reviewer", reviewer_version="1",
            decision="CONTINUE", subject_ref="tool:1", subject_hash="e" * 64,
            explanation="looks structurally valid", metadata={"risk": "low"},
        )
        self.assertTrue(rid)
        receipt = self.rt.run_receipt(r)
        self.assertEqual(receipt["review_count"], 1)
        self.assertEqual(receipt["review_semantics"], "REVIEW_DECISION_IS_NOT_RUNTIME_AUTHORITY")

    def test_review_terminate_and_escalate_supported(self):
        for decision in ("TERMINATE", "ESCALATE"):
            r = make_run(self.rt, run_id=f"r-{decision}")
            self.rt.record_review(
                r, "t1", stage="TRAJECTORY", reviewer_id="reviewer", reviewer_version="1",
                decision=decision, subject_ref="trajectory:1", subject_hash="e" * 64,
            )
        self.assertEqual(self.rt.db.execute("SELECT COUNT(*) n FROM reviews").fetchone()["n"], 2)

    def test_invalid_review_decision_rejected(self):
        r = make_run(self.rt)
        with self.assertRaises(EvaluationError):
            self.rt.record_review(
                r, "t1", stage="TRAJECTORY", reviewer_id="reviewer", reviewer_version="1",
                decision="AUTHORIZE", subject_ref="trajectory:1", subject_hash="e" * 64,
            )

    def test_judge_disagreement_preserved(self):
        r = make_run(self.rt)
        self.rt.record_judgment(
            r, "t1", criterion="quality", evaluator_id="judge-a", evaluator_version="1",
            evaluator_kind="MODEL_JUDGE", judgment="PASS", evidence_ref="trace:t1"
        )
        self.rt.record_judgment(
            r, "t1", criterion="quality", evaluator_id="judge-b", evaluator_version="1",
            evaluator_kind="MODEL_JUDGE", judgment="FAIL", evidence_ref="trace:t1"
        )
        consensus = self.rt.judge_consensus(r, "t1", "quality")
        self.assertEqual(consensus["status"], "COMPETING")
        self.assertIsNone(consensus["aggregate_judgment"])

    def test_judge_agreement_can_be_reported_without_ground_truth_promotion(self):
        r = make_run(self.rt)
        for j in ("a", "b"):
            self.rt.record_judgment(
                r, "t1", criterion="quality", evaluator_id=j, evaluator_version="1",
                evaluator_kind="MODEL_JUDGE", judgment="PASS", evidence_ref="trace:t1"
            )
        consensus = self.rt.judge_consensus(r, "t1", "quality")
        self.assertEqual(consensus["status"], "AGREED")
        self.assertEqual(consensus["aggregate_judgment"], "PASS")
        self.assertEqual(self.rt.run_receipt(r)["judge_semantics"], "JUDGE_OUTPUT_IS_EVIDENCE_NOT_GROUND_TRUTH")

    def test_incomplete_sampling_is_not_complete_coverage(self):
        r = make_run(self.rt, expected_task_count=3)
        add_task(self.rt, r, "t1")
        add_task(self.rt, r, "t2")
        receipt = self.rt.seal_run(r)
        self.assertFalse(receipt["coverage_complete"])
        self.assertEqual(receipt["observed_task_count"], 2)

    def test_comparison_allows_harness_version_as_single_mutation_axis(self):
        b = make_run(self.rt, run_id="b", harness_version="h1")
        c = make_run(self.rt, run_id="c", harness_version="h2")
        for r in (b, c):
            add_task(self.rt, r, "t1")
            add_task(self.rt, r, "t2")
            self.rt.seal_run(r)
        cmp = self.rt.compare_runs(b, c)
        self.assertEqual(cmp["state"], "COMPARABLE")

    def test_environment_mismatch_blocks_comparison(self):
        b = make_run(self.rt, run_id="b", environment_id="env-a")
        c = make_run(self.rt, run_id="c", environment_id="env-b", harness_version="h2")
        for r in (b, c):
            add_task(self.rt, r, "t1")
            add_task(self.rt, r, "t2")
            self.rt.seal_run(r)
        cmp = self.rt.compare_runs(b, c)
        self.assertEqual(cmp["state"], "NOT_COMPARABLE")
        self.assertIn("environment_id mismatch", cmp["reasons"])

    def test_evaluator_version_mismatch_blocks_comparison(self):
        b = make_run(self.rt, run_id="b", evaluator_version="e1")
        c = make_run(self.rt, run_id="c", evaluator_version="e2", harness_version="h2")
        for r in (b, c):
            add_task(self.rt, r, "t1")
            add_task(self.rt, r, "t2")
            self.rt.seal_run(r)
        self.assertEqual(self.rt.compare_runs(b, c)["state"], "NOT_COMPARABLE")

    def test_task_cohort_mismatch_blocks_comparison(self):
        b = make_run(self.rt, run_id="b", task_cohort_hash="1" * 64)
        c = make_run(self.rt, run_id="c", task_cohort_hash="2" * 64, harness_version="h2")
        for r in (b, c):
            add_task(self.rt, r, "t1")
            add_task(self.rt, r, "t2")
            self.rt.seal_run(r)
        self.assertEqual(self.rt.compare_runs(b, c)["state"], "NOT_COMPARABLE")

    def test_fixed_and_regressed_tasks_are_separate(self):
        b = make_run(self.rt, run_id="b")
        c = make_run(self.rt, run_id="c", harness_version="h2")
        add_task(self.rt, b, "t1", outcome="FAIL")
        add_task(self.rt, b, "t2", outcome="PASS")
        add_task(self.rt, c, "t1", outcome="PASS")
        add_task(self.rt, c, "t2", outcome="FAIL")
        self.rt.seal_run(b); self.rt.seal_run(c)
        cmp = self.rt.compare_runs(b, c)
        self.assertEqual(cmp["fixed_task_ids"], ["t1"])
        self.assertEqual(cmp["regressed_task_ids"], ["t2"])

    def test_critical_regression_forces_rollback(self):
        b = make_run(self.rt, run_id="b")
        c = make_run(self.rt, run_id="c", harness_version="h2")
        add_task(self.rt, b, "t1", outcome="FAIL")
        add_task(self.rt, b, "t2", outcome="PASS", critical=False)
        add_task(self.rt, c, "t1", outcome="PASS")
        add_task(self.rt, c, "t2", outcome="FAIL", critical=True)
        self.rt.seal_run(b); self.rt.seal_run(c)
        cmp = self.rt.compare_runs(b, c)
        verdict = self.rt.mutation_verdict(cmp, predicted_fix_ids=["t1"], predicted_regression_ids=[], attribution_plausible=True)
        self.assertEqual(verdict["verdict"], "ROLLBACK")
        self.assertEqual(verdict["critical_regression_ids"], ["t2"])

    def test_measured_net_fix_can_keep_mutation(self):
        b = make_run(self.rt, run_id="b")
        c = make_run(self.rt, run_id="c", harness_version="h2")
        add_task(self.rt, b, "t1", outcome="FAIL")
        add_task(self.rt, b, "t2", outcome="PASS")
        add_task(self.rt, c, "t1", outcome="PASS")
        add_task(self.rt, c, "t2", outcome="PASS")
        self.rt.seal_run(b); self.rt.seal_run(c)
        cmp = self.rt.compare_runs(b, c)
        verdict = self.rt.mutation_verdict(cmp, predicted_fix_ids=["t1"], predicted_regression_ids=[], attribution_plausible=True)
        self.assertEqual(verdict["verdict"], "KEEP")
        self.assertEqual(verdict["fix_precision"], 1.0)

    def test_unfrozen_attribution_is_inconclusive(self):
        b = make_run(self.rt, run_id="b")
        c = make_run(self.rt, run_id="c", harness_version="h2")
        add_task(self.rt, b, "t1", outcome="FAIL"); add_task(self.rt, b, "t2")
        add_task(self.rt, c, "t1", outcome="PASS"); add_task(self.rt, c, "t2")
        self.rt.seal_run(b); self.rt.seal_run(c)
        cmp = self.rt.compare_runs(b, c)
        verdict = self.rt.mutation_verdict(cmp, predicted_fix_ids=["t1"], predicted_regression_ids=[], attribution_plausible=False)
        self.assertEqual(verdict["verdict"], "INCONCLUSIVE")

    def test_no_change_is_inconclusive(self):
        b = make_run(self.rt, run_id="b")
        c = make_run(self.rt, run_id="c", harness_version="h2")
        for r in (b, c):
            add_task(self.rt, r, "t1")
            add_task(self.rt, r, "t2")
            self.rt.seal_run(r)
        cmp = self.rt.compare_runs(b, c)
        verdict = self.rt.mutation_verdict(cmp, predicted_fix_ids=[], predicted_regression_ids=[], attribution_plausible=True)
        self.assertEqual(verdict["verdict"], "INCONCLUSIVE")

    def test_prediction_metrics_preserve_misses(self):
        b = make_run(self.rt, run_id="b")
        c = make_run(self.rt, run_id="c", harness_version="h2")
        add_task(self.rt, b, "t1", outcome="FAIL"); add_task(self.rt, b, "t2", outcome="PASS")
        add_task(self.rt, c, "t1", outcome="PASS"); add_task(self.rt, c, "t2", outcome="FAIL")
        self.rt.seal_run(b); self.rt.seal_run(c)
        cmp = self.rt.compare_runs(b, c)
        verdict = self.rt.mutation_verdict(cmp, predicted_fix_ids=["t1", "t9"], predicted_regression_ids=["t2"], attribution_plausible=True)
        self.assertEqual(verdict["fix_precision"], 0.5)
        self.assertEqual(verdict["regression_recall"], 1.0)

    def test_ledger_tamper_is_detected(self):
        r = make_run(self.rt)
        add_task(self.rt, r, "t1")
        self.assertTrue(self.rt.verify_integrity()[0])
        self.rt.db.execute("UPDATE ledger SET payload_json='{}' WHERE seq=1")
        self.rt.db.commit()
        ok, errors = self.rt.verify_integrity()
        self.assertFalse(ok)
        self.assertTrue(errors)

    def test_sealed_run_rejects_late_evidence(self):
        r = make_run(self.rt)
        add_task(self.rt, r, "t1")
        add_task(self.rt, r, "t2")
        self.rt.seal_run(r)
        with self.assertRaises(EvaluationError):
            self.rt.record_judgment(
                r, "t1", criterion="late", evaluator_id="j", evaluator_version="1",
                evaluator_kind="MODEL_JUDGE", judgment="PASS", evidence_ref="x"
            )


if __name__ == "__main__":
    unittest.main()
