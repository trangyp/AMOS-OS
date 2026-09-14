import hashlib
import importlib.util
import json
import sqlite3
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ROOT / "07_SKILLS" / "amos-observability-driven-harness-evolution-rscf" / "scripts" / "harness_evolution_runtime.py"
CHECK = ROOT / "07_SKILLS" / "amos-observability-driven-harness-evolution-rscf" / "scripts" / "harness_evolution_contract_check.py"

spec = importlib.util.spec_from_file_location("harness_runtime", RUNTIME)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
HarnessEvolutionRuntime = mod.HarnessEvolutionRuntime
HarnessEvolutionError = mod.HarnessEvolutionError

spec2 = importlib.util.spec_from_file_location("harness_check", CHECK)
chk = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(chk)
ContractError = chk.ContractError


def h(c):
    return c * 64


def receipt(body):
    body = dict(body)
    body["receipt_hash"] = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    return body


def run_receipt(*, run_id, harness_version, overrides=None):
    body = {
        "run_id": run_id,
        "suite_id": "suite",
        "target_id": "amos",
        "target_version": "1",
        "environment_id": "env",
        "harness_id": "harness",
        "harness_version": harness_version,
        "evaluator_set_id": "judge-set",
        "evaluator_version": "1",
        "model_id": "model",
        "model_config_hash": h("a"),
        "budget_id": "budget",
        "task_cohort_hash": h("b"),
        "evidence_archetype": "PROCESS",
        "expected_task_count": 3,
        "observed_task_count": 3,
        "coverage_complete": True,
        "judgment_count": 3,
        "review_count": 0,
        "competing_judgment_sets": [],
        "sealed": True,
        "authority_semantics": "EVALUATION_DOES_NOT_GRANT_AUTHORITY",
        "judge_semantics": "JUDGE_OUTPUT_IS_EVIDENCE_NOT_GROUND_TRUTH",
        "review_semantics": "REVIEW_DECISION_IS_NOT_RUNTIME_AUTHORITY",
    }
    if overrides:
        body.update(overrides)
    return receipt(body)


def comparison(*, fixed=None, regressed=None, critical=None, state="COMPARABLE", reasons=None, baseline="base", candidate="cand"):
    body = {
        "comparison_id": "cmp",
        "baseline_run_id": baseline,
        "candidate_run_id": candidate,
        "state": state,
        "reasons": [] if reasons is None else reasons,
        "fixed_task_ids": [] if fixed is None else fixed,
        "regressed_task_ids": [] if regressed is None else regressed,
        "unchanged_task_ids": [],
        "critical_regression_task_ids": [] if critical is None else critical,
        "causal_semantics": "SCORE_DELTA_DOES_NOT_PROVE_CAUSAL_ATTRIBUTION",
        "authority_semantics": "EVALUATION_DOES_NOT_GRANT_AUTHORITY",
    }
    return receipt(body)


def calibration_report(overrides=None):
    body = {
        "schema": "amos.evaluator-calibration.report.v1",
        "session_id": "cal-val",
        "phase": "VALIDATION",
        "evaluator_id": "judge",
        "evaluator_version": "1",
        "evaluator_kind": "MODEL_JUDGE",
        "evaluator_config_hash": h("c"),
        "cohort_hash": h("9"),
        "expected_count": 3,
        "observed_count": 3,
        "observed_coverage": 1.0,
        "classification_count": 3,
        "classification_coverage": 1.0,
        "selective_accuracy": 1.0,
        "abstention_rate": 0.0,
        "reference_independence": "INDEPENDENT",
        "sealed": True,
        "authority_semantics": "CALIBRATION_EVIDENCE_DOES_NOT_GRANT_AUTHORITY",
        "truth_semantics": "REFERENCE_LABEL_IS_EVIDENCE_NOT_GROUND_TRUTH",
    }
    if overrides:
        body.update(overrides)
    return receipt(body)


def calibration_gate(verdict="PASS", overrides=None):
    body = {
        "schema": "amos.evaluator-calibration.gate.v1",
        "session_id": "cal-val",
        "verdict": verdict,
        "checks": [{"name": "min_selective_accuracy", "state": verdict, "observed": 1.0, "required": 0.8}],
        "authority_semantics": "CALIBRATION_EVIDENCE_DOES_NOT_GRANT_AUTHORITY",
        "deployment_semantics": "RELIABILITY_GATE_PASS_DOES_NOT_IMPLY_DEPLOYMENT_VALIDITY",
    }
    if overrides:
        body.update(overrides)
    return receipt(body)


class HarnessEvolutionRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.rt = HarnessEvolutionRuntime()
        self.exp = self.rt.create_experiment(
            target_id="amos", target_version="1", harness_id="harness", baseline_version="v1", candidate_version="v2",
            suite_id="suite", environment_id="env", evaluator_set_id="judge-set", evaluator_version="1",
            model_id="model", model_config_hash=h("a"), budget_id="budget", task_cohort_hash=h("b"),
            evidence_archetype="PROCESS", expected_task_count=3,
            calibrated_evaluator_id="judge", calibrated_evaluator_version="1", calibrated_evaluator_config_hash=h("c"),
            experiment_id="exp",
        )
        self.rt.register_component(self.exp, file_path="SKILL.md", component_class="SKILL", baseline_hash=h("d"))
        self.rt.register_component(self.exp, file_path="workflow.md", component_class="WORKFLOW", baseline_hash=h("e"))
        self.rt.register_component(self.exp, file_path="locked.md", component_class="POLICY_CONFIG", baseline_hash=h("f"), mutable=False)

    def tearDown(self):
        self.rt.close()

    def make_mutation(self, *, mode="SINGLE_COMPONENT", fixes=("t1",), regs=(), mutation_id="m"):
        return self.rt.create_mutation(
            self.exp, root_cause_hash=h("1"), evidence_bundle_hash=h("2"),
            predicted_fix_ids=fixes, predicted_regression_ids=regs,
            attribution_mode=mode, coupling_reason_hash=h("3") if mode == "COUPLED_SET" else None,
            mutation_id=mutation_id,
        )

    def stage_and_freeze(self, *, mutation_id="m", mode="SINGLE_COMPONENT", two=False):
        self.make_mutation(mode=mode, mutation_id=mutation_id)
        self.rt.stage_change(mutation_id, file_path="SKILL.md", before_hash=h("d"), after_hash=h("4"), rollback_hash=h("d"))
        if two:
            self.rt.stage_change(mutation_id, file_path="workflow.md", before_hash=h("e"), after_hash=h("5"), rollback_hash=h("e"))
        self.rt.freeze_mutation(mutation_id)
        return mutation_id

    def isolate(self, mutation_id="m", *, valid=True):
        return self.rt.record_isolation(
            mutation_id, mode="SHARED_VERIFIER", prior_shared_verifier_state=True,
            sanitized_before_agent=valid, prior_tests_hidden=True, prior_reward_hidden=True,
            agent_owned_state_preserved=True, evidence_hash=h("6"),
        )

    def bind(self, mutation_id="m", *, comp=None, gate=None, report=None, base=None, cand=None, attribution=True):
        return self.rt.bind_evaluation(
            mutation_id,
            baseline_run_receipt=base or run_receipt(run_id="base", harness_version="v1"),
            candidate_run_receipt=cand or run_receipt(run_id="cand", harness_version="v2"),
            comparison_receipt=comp or comparison(fixed=["t1"]),
            calibration_report_receipt=report or calibration_report(),
            calibration_gate_receipt=gate or calibration_gate(),
            attribution_plausible=attribution,
        )

    def test_01_experiment_created(self):
        self.assertEqual(self.rt._experiment(self.exp)["candidate_version"], "v2")

    def test_02_same_version_rejected(self):
        with self.assertRaises(HarnessEvolutionError):
            self.rt.create_experiment(target_id="x", target_version="1", harness_id="h", baseline_version="v", candidate_version="v", suite_id="s", environment_id="e", evaluator_set_id="q", evaluator_version="1", model_id="m", model_config_hash=h("a"), budget_id="b", task_cohort_hash=h("b"), evidence_archetype="PROCESS", expected_task_count=1, calibrated_evaluator_id="j", calibrated_evaluator_version="1", calibrated_evaluator_config_hash=h("c"))

    def test_03_bad_hash_rejected(self):
        with self.assertRaises(HarnessEvolutionError):
            self.rt.register_component(self.exp, file_path="x", component_class="SKILL", baseline_hash="bad")

    def test_04_component_registered(self):
        row = self.rt.db.execute("SELECT component_class FROM components WHERE file_path='SKILL.md'").fetchone()
        self.assertEqual(row[0], "SKILL")

    def test_05_unsupported_component_rejected(self):
        with self.assertRaises(HarnessEvolutionError):
            self.rt.register_component(self.exp, file_path="x", component_class="MAGIC", baseline_hash=h("7"))

    def test_06_duplicate_component_rejected(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.rt.register_component(self.exp, file_path="SKILL.md", component_class="SKILL", baseline_hash=h("d"))

    def test_07_prediction_overlap_rejected(self):
        with self.assertRaises(HarnessEvolutionError):
            self.make_mutation(fixes=("t1",), regs=("t1",))

    def test_08_coupled_requires_reason_hash(self):
        with self.assertRaises(HarnessEvolutionError):
            self.rt.create_mutation(self.exp, root_cause_hash=h("1"), evidence_bundle_hash=h("2"), predicted_fix_ids=[], predicted_regression_ids=[], attribution_mode="COUPLED_SET")

    def test_09_stage_undeclared_path_rejected(self):
        self.make_mutation()
        with self.assertRaises(HarnessEvolutionError):
            self.rt.stage_change("m", file_path="unknown", before_hash=h("d"), after_hash=h("4"), rollback_hash=h("d"))

    def test_10_immutable_component_rejected(self):
        self.make_mutation()
        with self.assertRaises(HarnessEvolutionError):
            self.rt.stage_change("m", file_path="locked.md", before_hash=h("f"), after_hash=h("4"), rollback_hash=h("f"))

    def test_11_baseline_mismatch_rejected(self):
        self.make_mutation()
        with self.assertRaises(HarnessEvolutionError):
            self.rt.stage_change("m", file_path="SKILL.md", before_hash=h("9"), after_hash=h("4"), rollback_hash=h("9"))

    def test_12_rollback_hash_must_equal_before(self):
        self.make_mutation()
        with self.assertRaises(HarnessEvolutionError):
            self.rt.stage_change("m", file_path="SKILL.md", before_hash=h("d"), after_hash=h("4"), rollback_hash=h("5"))

    def test_13_noop_change_rejected(self):
        self.make_mutation()
        with self.assertRaises(HarnessEvolutionError):
            self.rt.stage_change("m", file_path="SKILL.md", before_hash=h("d"), after_hash=h("d"), rollback_hash=h("d"))

    def test_14_freeze_requires_change(self):
        self.make_mutation()
        with self.assertRaises(HarnessEvolutionError):
            self.rt.freeze_mutation("m")

    def test_15_cross_component_requires_coupled(self):
        self.make_mutation()
        self.rt.stage_change("m", file_path="SKILL.md", before_hash=h("d"), after_hash=h("4"), rollback_hash=h("d"))
        self.rt.stage_change("m", file_path="workflow.md", before_hash=h("e"), after_hash=h("5"), rollback_hash=h("e"))
        with self.assertRaises(HarnessEvolutionError):
            self.rt.freeze_mutation("m")

    def test_16_coupled_cross_component_succeeds(self):
        self.stage_and_freeze(mode="COUPLED_SET", two=True)
        self.assertEqual(self.rt._mutation("m")["state"], "STAGED")

    def test_17_single_component_freeze_succeeds(self):
        self.stage_and_freeze()
        self.assertEqual(self.rt.mutation_receipt("m")["state"], "STAGED")

    def test_18_single_step_isolation_valid(self):
        self.stage_and_freeze()
        iso = self.rt.record_isolation("m", mode="SINGLE_STEP", prior_shared_verifier_state=False, sanitized_before_agent=False, prior_tests_hidden=True, prior_reward_hidden=True, agent_owned_state_preserved=True, evidence_hash=h("6"))
        self.assertTrue(iso["isolation_valid"])

    def test_19_shared_unsanitized_invalid(self):
        self.stage_and_freeze()
        self.assertFalse(self.isolate(valid=False)["isolation_valid"])

    def test_20_shared_sanitized_valid(self):
        self.stage_and_freeze()
        self.assertTrue(self.isolate(valid=True)["isolation_valid"])

    def test_21_separate_mode_rejects_prior_shared_state(self):
        self.stage_and_freeze()
        with self.assertRaises(HarnessEvolutionError):
            self.rt.record_isolation("m", mode="SEPARATE_VERIFIER", prior_shared_verifier_state=True, sanitized_before_agent=False, prior_tests_hidden=True, prior_reward_hidden=True, agent_owned_state_preserved=True, evidence_hash=h("6"))

    def test_22_run_field_mismatch_rejected(self):
        self.stage_and_freeze(); self.isolate()
        bad = run_receipt(run_id="base", harness_version="v1", overrides={"environment_id": "other"})
        with self.assertRaises(HarnessEvolutionError): self.bind(base=bad)

    def test_23_unsealed_run_rejected(self):
        self.stage_and_freeze(); self.isolate()
        bad = run_receipt(run_id="base", harness_version="v1", overrides={"sealed": False})
        with self.assertRaises(HarnessEvolutionError): self.bind(base=bad)

    def test_24_incomplete_coverage_rejected(self):
        self.stage_and_freeze(); self.isolate()
        bad = run_receipt(run_id="base", harness_version="v1", overrides={"coverage_complete": False})
        with self.assertRaises(HarnessEvolutionError): self.bind(base=bad)

    def test_25_tampered_receipt_hash_rejected(self):
        self.stage_and_freeze(); self.isolate()
        bad = run_receipt(run_id="base", harness_version="v1")
        bad["budget_id"] = "tampered"
        with self.assertRaises(HarnessEvolutionError): self.bind(base=bad)

    def test_26_calibration_must_be_validation(self):
        self.stage_and_freeze(); self.isolate()
        bad = calibration_report({"phase": "CALIBRATION"})
        with self.assertRaises(HarnessEvolutionError): self.bind(report=bad)

    def test_27_calibrated_evaluator_mismatch_rejected(self):
        self.stage_and_freeze(); self.isolate()
        bad = calibration_report({"evaluator_id": "other"})
        with self.assertRaises(HarnessEvolutionError): self.bind(report=bad)

    def test_28_comparison_run_id_mismatch_rejected(self):
        self.stage_and_freeze(); self.isolate()
        with self.assertRaises(HarnessEvolutionError): self.bind(comp=comparison(fixed=["t1"], baseline="wrong"))

    def test_29_not_comparable_requires_reasons(self):
        self.stage_and_freeze(); self.isolate()
        with self.assertRaises(HarnessEvolutionError): self.bind(comp=comparison(state="NOT_COMPARABLE", reasons=[]))

    def test_30_valid_binding(self):
        self.stage_and_freeze(); self.isolate()
        out = self.bind()
        self.assertEqual(out["comparison_state"], "COMPARABLE")

    def test_31_keep_decision(self):
        self.stage_and_freeze(); self.isolate(); comp = comparison(fixed=["t1"]); gate = calibration_gate(); self.bind(comp=comp, gate=gate)
        d = self.rt.decision("m", comparison_receipt=comp, calibration_gate_receipt=gate)
        self.assertEqual(d["verdict"], "KEEP")
        chk.validate(d)

    def test_32_critical_regression_rolls_back(self):
        self.stage_and_freeze(); self.isolate(); comp = comparison(fixed=["t1"], regressed=["t2"], critical=["t2"]); gate = calibration_gate(); self.bind(comp=comp, gate=gate)
        d = self.rt.decision("m", comparison_receipt=comp, calibration_gate_receipt=gate)
        self.assertEqual(d["verdict"], "ROLLBACK")

    def test_33_more_regressions_roll_back(self):
        self.stage_and_freeze(); self.isolate(); comp = comparison(fixed=["t1"], regressed=["t2", "t3"]); gate = calibration_gate(); self.bind(comp=comp, gate=gate)
        self.assertEqual(self.rt.decision("m", comparison_receipt=comp, calibration_gate_receipt=gate)["verdict"], "ROLLBACK")

    def test_34_calibration_fail_inconclusive(self):
        self.stage_and_freeze(); self.isolate(); comp = comparison(fixed=["t1"]); gate = calibration_gate("FAIL"); self.bind(comp=comp, gate=gate)
        self.assertEqual(self.rt.decision("m", comparison_receipt=comp, calibration_gate_receipt=gate)["verdict"], "INCONCLUSIVE")

    def test_35_invalid_isolation_inconclusive(self):
        self.stage_and_freeze(); self.isolate(valid=False); comp = comparison(fixed=["t1"]); gate = calibration_gate(); self.bind(comp=comp, gate=gate)
        self.assertEqual(self.rt.decision("m", comparison_receipt=comp, calibration_gate_receipt=gate)["verdict"], "INCONCLUSIVE")

    def test_36_attribution_false_inconclusive(self):
        self.stage_and_freeze(); self.isolate(); comp = comparison(fixed=["t1"]); gate = calibration_gate(); self.bind(comp=comp, gate=gate, attribution=False)
        self.assertEqual(self.rt.decision("m", comparison_receipt=comp, calibration_gate_receipt=gate)["verdict"], "INCONCLUSIVE")

    def test_37_equal_fix_regression_inconclusive(self):
        self.stage_and_freeze(); self.isolate(); comp = comparison(fixed=["t1"], regressed=["t2"]); gate = calibration_gate(); self.bind(comp=comp, gate=gate)
        self.assertEqual(self.rt.decision("m", comparison_receipt=comp, calibration_gate_receipt=gate)["verdict"], "INCONCLUSIVE")

    def test_38_fix_precision(self):
        self.make_mutation(fixes=("t1", "t2"), regs=())
        self.rt.stage_change("m", file_path="SKILL.md", before_hash=h("d"), after_hash=h("4"), rollback_hash=h("d")); self.rt.freeze_mutation("m"); self.isolate()
        comp = comparison(fixed=["t1"]); gate = calibration_gate(); self.bind(comp=comp, gate=gate)
        d = self.rt.decision("m", comparison_receipt=comp, calibration_gate_receipt=gate)
        self.assertEqual(d["fix_precision"], 0.5)

    def test_39_regression_recall(self):
        self.make_mutation(fixes=("t1",), regs=("t2",))
        self.rt.stage_change("m", file_path="SKILL.md", before_hash=h("d"), after_hash=h("4"), rollback_hash=h("d")); self.rt.freeze_mutation("m"); self.isolate()
        comp = comparison(fixed=[], regressed=["t2", "t3"]); gate = calibration_gate(); self.bind(comp=comp, gate=gate)
        d = self.rt.decision("m", comparison_receipt=comp, calibration_gate_receipt=gate)
        self.assertEqual(d["regression_recall"], 0.5)

    def test_40_reconcile_kept_valid(self):
        self.stage_and_freeze(); self.isolate(); comp = comparison(fixed=["t1"]); gate = calibration_gate(); self.bind(comp=comp, gate=gate); self.rt.decision("m", comparison_receipt=comp, calibration_gate_receipt=gate)
        r = self.rt.reconcile("m", state="KEPT", observed_version="v2", observed_component_hashes={"SKILL.md": h("4")}, evidence_hash=h("7"))
        self.assertEqual(r["state"], "KEPT"); chk.validate(r)

    def test_41_reconcile_kept_wrong_version_rejected(self):
        self.stage_and_freeze(); self.isolate(); comp = comparison(fixed=["t1"]); gate = calibration_gate(); self.bind(comp=comp, gate=gate); self.rt.decision("m", comparison_receipt=comp, calibration_gate_receipt=gate)
        with self.assertRaises(HarnessEvolutionError): self.rt.reconcile("m", state="KEPT", observed_version="v1", observed_component_hashes={"SKILL.md": h("4")}, evidence_hash=h("7"))

    def test_42_reconcile_kept_hash_mismatch_rejected(self):
        self.stage_and_freeze(); self.isolate(); comp = comparison(fixed=["t1"]); gate = calibration_gate(); self.bind(comp=comp, gate=gate); self.rt.decision("m", comparison_receipt=comp, calibration_gate_receipt=gate)
        with self.assertRaises(HarnessEvolutionError): self.rt.reconcile("m", state="KEPT", observed_version="v2", observed_component_hashes={"SKILL.md": h("d")}, evidence_hash=h("7"))

    def test_43_reconcile_rollback_valid(self):
        self.stage_and_freeze(); self.isolate(); comp = comparison(regressed=["t2", "t3"]); gate = calibration_gate(); self.bind(comp=comp, gate=gate); self.rt.decision("m", comparison_receipt=comp, calibration_gate_receipt=gate)
        r = self.rt.reconcile("m", state="ROLLED_BACK", observed_version="v1", observed_component_hashes={"SKILL.md": h("d")}, evidence_hash=h("7"))
        self.assertEqual(r["state"], "ROLLED_BACK")

    def test_44_reconciliation_requires_exact_component_set(self):
        self.stage_and_freeze(); self.isolate(); comp = comparison(fixed=["t1"]); gate = calibration_gate(); self.bind(comp=comp, gate=gate); self.rt.decision("m", comparison_receipt=comp, calibration_gate_receipt=gate)
        with self.assertRaises(HarnessEvolutionError): self.rt.reconcile("m", state="KEPT", observed_version="v2", observed_component_hashes={}, evidence_hash=h("7"))

    def test_45_ledger_tamper_detected(self):
        self.stage_and_freeze()
        self.assertTrue(self.rt.verify_ledger())
        self.rt.db.execute("UPDATE ledger SET payload_json='{}' WHERE seq=1"); self.rt.db.commit()
        self.assertFalse(self.rt.verify_ledger())

    def test_46_cannot_stage_after_freeze(self):
        self.stage_and_freeze()
        with self.assertRaises(HarnessEvolutionError): self.rt.stage_change("m", file_path="workflow.md", before_hash=h("e"), after_hash=h("5"), rollback_hash=h("e"))

    def test_47_decision_before_evaluation_rejected(self):
        self.stage_and_freeze(); self.isolate()
        with self.assertRaises(HarnessEvolutionError): self.rt.decision("m", comparison_receipt=comparison(fixed=["t1"]), calibration_gate_receipt=calibration_gate())

    def test_48_contract_rejects_raw_content(self):
        d = {"schema": "amos.harness-evolution.decision.v1", "prompt": "secret"}
        with self.assertRaises(ContractError): chk.validate(d)

    def test_49_contract_rejects_authorize_verdict(self):
        body = {
            "schema": "amos.harness-evolution.decision.v1", "mutation_id": "m", "verdict": "AUTHORIZE", "reasons": [],
            "fixed_task_ids": [], "regressed_task_ids": [], "critical_regression_task_ids": [], "predicted_fix_ids": [],
            "predicted_regression_ids": [], "fix_precision": 0.0, "regression_recall": 1.0, "comparison_state": "COMPARABLE",
            "calibration_verdict": "PASS", "isolation_valid": True, "attribution_plausible": True,
            "authority_semantics": mod.AUTHORITY_SEMANTICS, "causal_semantics": mod.CAUSAL_SEMANTICS,
            "rollback_semantics": mod.ROLLBACK_SEMANTICS, "evaluator_semantics": mod.EVALUATOR_SEMANTICS,
        }
        body = receipt(body)
        with self.assertRaises(ContractError): chk.validate(body)

    def test_50_mutation_receipt_validates(self):
        self.stage_and_freeze()
        chk.validate(self.rt.mutation_receipt("m"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
