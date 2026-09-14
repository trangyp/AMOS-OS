import hashlib
import importlib
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / "07_SKILLS" / "amos-observability-driven-harness-evolution-rscf" / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
base = importlib.import_module("harness_evolution_runtime")
guarded = importlib.import_module("harness_evolution_guarded_runtime")
checker = importlib.import_module("harness_evolution_guarded_contract_check")


def h(ch: str) -> str:
    return ch * 64


def receipt(body):
    out = dict(body)
    out["receipt_hash"] = hashlib.sha256(json.dumps(out, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return out


def run_receipt(run_id, version):
    return receipt({
        "schema": "amos.evaluation.run.v1", "run_id": run_id, "suite_id": "s", "target_id": "t",
        "target_version": "1", "environment_id": "e", "harness_id": "h", "harness_version": version,
        "evaluator_set_id": "es", "evaluator_version": "1", "model_id": "m", "model_config_hash": h("a"),
        "budget_id": "b", "task_cohort_hash": h("b"), "evidence_archetype": "PROCESS",
        "expected_task_count": 1, "observed_task_count": 1, "coverage_complete": True,
        "judgment_count": 1, "review_count": 0, "competing_judgment_sets": [], "sealed": True,
        "authority_semantics": "EVALUATION_DOES_NOT_GRANT_AUTHORITY", "judge_semantics": "JUDGE_OUTPUT_IS_EVIDENCE_NOT_GROUND_TRUTH",
        "review_semantics": "REVIEW_DECISION_IS_NOT_RUNTIME_AUTHORITY", "causal_semantics": "SCORE_DELTA_DOES_NOT_PROVE_CAUSAL_ATTRIBUTION",
    })


def comparison(*, critical=True):
    return receipt({
        "schema": "amos.evaluation.comparison.v1", "comparison_id": "c", "baseline_run_id": "r1", "candidate_run_id": "r2",
        "state": "COMPARABLE", "reasons": [], "fixed_task_ids": [], "regressed_task_ids": ["t1"],
        "unchanged_task_ids": [], "critical_regression_task_ids": ["t1"] if critical else [],
        "authority_semantics": "EVALUATION_DOES_NOT_GRANT_AUTHORITY", "causal_semantics": "SCORE_DELTA_DOES_NOT_PROVE_CAUSAL_ATTRIBUTION",
    })


def cal_report():
    return receipt({
        "schema": "amos.evaluator-calibration.report.v1", "session_id": "v", "phase": "VALIDATION",
        "evaluator_id": "judge", "evaluator_version": "1", "evaluator_kind": "MODEL_JUDGE",
        "evaluator_config_hash": h("c"), "cohort_hash": h("d"), "expected_count": 1, "observed_count": 1,
        "observed_coverage": 1.0, "classification_count": 1, "classification_coverage": 1.0,
        "abstention_rate": 0.0, "selective_accuracy": 1.0, "accuracy_ci": [0.2, 1.0],
        "brier_score": 0.1, "ece": 0.1, "probability_complete": True, "reference_independence": "INDEPENDENT",
        "sealed": True, "authority_semantics": "CALIBRATION_EVIDENCE_DOES_NOT_GRANT_AUTHORITY",
        "truth_semantics": "REFERENCE_LABEL_IS_EVIDENCE_NOT_GROUND_TRUTH",
        "calibration_semantics": "CALIBRATED_ON_COHORT_DOES_NOT_IMPLY_GENERALIZATION",
        "agreement_semantics": "AGREEMENT_DOES_NOT_IMPLY_TRUTH",
        "probability_semantics": "SCORE_IS_NOT_A_PROBABILITY_UNLESS_DECLARED_AND_VALIDATED",
        "deployment_semantics": "RELIABILITY_GATE_PASS_DOES_NOT_IMPLY_DEPLOYMENT_VALIDITY",
    })


def cal_gate(verdict="PASS"):
    return receipt({
        "schema": "amos.evaluator-calibration.gate.v1", "session_id": "v", "verdict": verdict, "checks": [],
        "authority_semantics": "CALIBRATION_EVIDENCE_DOES_NOT_GRANT_AUTHORITY",
        "deployment_semantics": "RELIABILITY_GATE_PASS_DOES_NOT_IMPLY_DEPLOYMENT_VALIDITY",
    })


class GuardedRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.rt = guarded.GuardedHarnessEvolutionRuntime()
        self.exp = self.rt.create_experiment(
            target_id="t", target_version="1", harness_id="h", baseline_version="v1", candidate_version="v2",
            suite_id="s", environment_id="e", evaluator_set_id="es", evaluator_version="1", model_id="m",
            model_config_hash=h("a"), budget_id="b", task_cohort_hash=h("b"), evidence_archetype="PROCESS",
            expected_task_count=1, calibrated_evaluator_id="judge", calibrated_evaluator_version="1",
            calibrated_evaluator_config_hash=h("c"), experiment_id="x",
        )
        self.rt.register_component(self.exp, file_path="SKILL.md", component_class="SKILL", baseline_hash=h("d"))
        self.mid = self.rt.create_mutation(self.exp, root_cause_hash=h("e"), evidence_bundle_hash=h("f"), predicted_fix_ids=[], predicted_regression_ids=["t1"], attribution_mode="SINGLE_COMPONENT", mutation_id="mu")
        self.rt.stage_change(self.mid, file_path="SKILL.md", before_hash=h("d"), after_hash=h("1"), rollback_hash=h("d"))
        self.rt.freeze_mutation(self.mid)
        self.rt.record_isolation(self.mid, mode="SINGLE_STEP", prior_shared_verifier_state=False, sanitized_before_agent=False, prior_tests_hidden=True, prior_reward_hidden=True, agent_owned_state_preserved=True, evidence_hash=h("2"))

    def bind(self, verdict="FAIL"):
        comp = comparison()
        gate = cal_gate(verdict)
        self.rt.bind_evaluation(self.mid, baseline_run_receipt=run_receipt("r1", "v1"), candidate_run_receipt=run_receipt("r2", "v2"), comparison_receipt=comp, calibration_report_receipt=cal_report(), calibration_gate_receipt=gate, attribution_plausible=True)
        return comp, gate

    def test_failed_calibration_forces_inconclusive_before_base_decision(self):
        comp, gate = self.bind("FAIL")
        with patch.object(base.HarnessEvolutionRuntime, "decision", side_effect=AssertionError("base decision must not run")):
            out = self.rt.decision(self.mid, comparison_receipt=comp, calibration_gate_receipt=gate)
        self.assertEqual(out["verdict"], "INCONCLUSIVE")

    def test_passed_evidence_delegates_and_rolls_back(self):
        comp, gate = self.bind("PASS")
        out = self.rt.decision(self.mid, comparison_receipt=comp, calibration_gate_receipt=gate)
        self.assertEqual(out["verdict"], "ROLLBACK")

    def test_guarded_validator_rejects_unreliable_rollback(self):
        body = {
            "schema": "amos.harness-evolution.decision.v1", "mutation_id": "m", "verdict": "ROLLBACK",
            "reasons": ["critical regression observed"], "fixed_task_ids": [], "regressed_task_ids": ["t1"],
            "critical_regression_task_ids": ["t1"], "predicted_fix_ids": [], "predicted_regression_ids": ["t1"],
            "fix_precision": 0.0, "regression_recall": 1.0, "comparison_state": "COMPARABLE", "calibration_verdict": "FAIL",
            "isolation_valid": True, "attribution_plausible": True, "authority_semantics": base.AUTHORITY_SEMANTICS,
            "causal_semantics": base.CAUSAL_SEMANTICS, "rollback_semantics": base.ROLLBACK_SEMANTICS,
            "evaluator_semantics": base.EVALUATOR_SEMANTICS,
        }
        with self.assertRaises(checker.ContractError):
            checker.validate(receipt(body))


if __name__ == "__main__":
    unittest.main(verbosity=2)
