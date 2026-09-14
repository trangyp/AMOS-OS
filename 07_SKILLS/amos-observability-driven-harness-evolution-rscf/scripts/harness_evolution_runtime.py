#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sqlite3
import time
import uuid
from pathlib import Path
from typing import Any, Iterable

SOURCE_COMPONENTS = {
    "SYSTEM_PROMPT",
    "TOOL_DESCRIPTION",
    "TOOL_IMPLEMENTATION",
    "MIDDLEWARE",
    "SKILL",
    "SUB_AGENT_CONFIG",
    "LONG_TERM_MEMORY",
}
AMOS_EXTENSION_COMPONENTS = {"AGENT_CONFIG", "WORKFLOW", "POLICY_CONFIG", "TOOL_REGISTRY"}
COMPONENT_CLASSES = SOURCE_COMPONENTS | AMOS_EXTENSION_COMPONENTS
ATTRIBUTION_MODES = {"SINGLE_COMPONENT", "COUPLED_SET"}
ISOLATION_MODES = {"SINGLE_STEP", "SEPARATE_VERIFIER", "SHARED_VERIFIER"}
MUTATION_STATES = {
    "PROPOSED",
    "STAGED",
    "EVALUATED",
    "KEEP_RECOMMENDED",
    "ROLLBACK_RECOMMENDED",
    "INCONCLUSIVE",
    "RECONCILED",
}
VERDICTS = {"KEEP", "ROLLBACK", "INCONCLUSIVE"}
RECONCILIATION_STATES = {"KEPT", "ROLLED_BACK", "NOT_APPLIED"}

AUTHORITY_SEMANTICS = "HARNESS_EVOLUTION_RECOMMENDATION_DOES_NOT_GRANT_WRITE_OR_MERGE_AUTHORITY"
CAUSAL_SEMANTICS = "NEXT_ROUND_DELTA_DOES_NOT_PROVE_CAUSAL_ATTRIBUTION"
ROLLBACK_SEMANTICS = "ROLLBACK_RECOMMENDATION_DOES_NOT_EXECUTE_ROLLBACK"
ISOLATION_SEMANTICS = "VERIFIER_OR_REWARD_LEAKAGE_INVALIDATES_COMPARATIVE_EVIDENCE"
EVALUATOR_SEMANTICS = "EVALUATOR_RELIABILITY_PASS_DOES_NOT_IMPLY_GROUND_TRUTH"

FORBIDDEN_DURABLE_KEYS = {
    "prompt",
    "completion",
    "raw_input",
    "raw_output",
    "input_value",
    "output_value",
    "tool_output",
    "chain_of_thought",
    "reasoning",
    "authorization",
    "api_key",
    "token",
    "password",
    "secret",
    "credential",
}

FROZEN_RUN_FIELDS = (
    "suite_id",
    "target_id",
    "target_version",
    "environment_id",
    "harness_id",
    "evaluator_set_id",
    "evaluator_version",
    "model_id",
    "model_config_hash",
    "budget_id",
    "task_cohort_hash",
    "evidence_archetype",
    "expected_task_count",
)


class HarnessEvolutionError(RuntimeError):
    pass


def _now_ns() -> int:
    return time.time_ns()


def _canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _sha256_json(value: Any) -> str:
    return _sha256_text(_canonical_json(value))


def _nonempty(name: str, value: Any) -> str:
    if not isinstance(value, str) or not value.strip():
        raise HarnessEvolutionError(f"{name} must be a non-empty string")
    return value.strip()


def _hash64(name: str, value: Any) -> str:
    if not isinstance(value, str) or len(value) != 64 or any(c not in "0123456789abcdef" for c in value):
        raise HarnessEvolutionError(f"{name} must be 64 lowercase hex chars")
    return value


def _reject_raw(value: Any, path: str = "$") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if str(key).lower() in FORBIDDEN_DURABLE_KEYS:
                raise HarnessEvolutionError(f"raw/sensitive durable field forbidden: {path}.{key}")
            _reject_raw(child, f"{path}.{key}")
    elif isinstance(value, list):
        for i, child in enumerate(value):
            _reject_raw(child, f"{path}[{i}]")


def _ledger_hash(prev_hash: str, event_type: str, payload_json: str, ts_ns: int) -> str:
    return _sha256_text(f"{prev_hash}|{event_type}|{payload_json}|{ts_ns}")


def _validate_receipt_hash(receipt: dict[str, Any], *, schema: str | None = None) -> None:
    _reject_raw(receipt)
    if not isinstance(receipt, dict):
        raise HarnessEvolutionError("receipt must be object")
    if schema is not None and receipt.get("schema") != schema:
        raise HarnessEvolutionError(f"receipt schema must be {schema}")
    h = receipt.get("receipt_hash")
    _hash64("receipt_hash", h)
    body = dict(receipt)
    body.pop("receipt_hash", None)
    if _sha256_json(body) != h:
        raise HarnessEvolutionError("receipt_hash mismatch")


def _as_sorted_ids(name: str, values: Iterable[str]) -> list[str]:
    out: set[str] = set()
    for value in values:
        out.add(_nonempty(name, value))
    return sorted(out)


class HarnessEvolutionRuntime:
    """Deterministic local control/evidence runtime for harness evolution.

    It records and validates bounded mutation evidence. It does not edit files,
    execute evaluations, commit changes, merge branches, or grant authority.
    """

    def __init__(self, db_path: str | Path = ":memory:") -> None:
        self.db = sqlite3.connect(str(db_path))
        self.db.row_factory = sqlite3.Row
        self.db.execute("PRAGMA foreign_keys=ON")
        self._init_schema()

    def close(self) -> None:
        self.db.close()

    def _init_schema(self) -> None:
        self.db.executescript(
            """
            CREATE TABLE IF NOT EXISTS experiments (
              experiment_id TEXT PRIMARY KEY,
              target_id TEXT NOT NULL,
              target_version TEXT NOT NULL,
              harness_id TEXT NOT NULL,
              baseline_version TEXT NOT NULL,
              candidate_version TEXT NOT NULL,
              suite_id TEXT NOT NULL,
              environment_id TEXT NOT NULL,
              evaluator_set_id TEXT NOT NULL,
              evaluator_version TEXT NOT NULL,
              model_id TEXT NOT NULL,
              model_config_hash TEXT NOT NULL,
              budget_id TEXT NOT NULL,
              task_cohort_hash TEXT NOT NULL,
              evidence_archetype TEXT NOT NULL,
              expected_task_count INTEGER NOT NULL,
              calibrated_evaluator_id TEXT NOT NULL,
              calibrated_evaluator_version TEXT NOT NULL,
              calibrated_evaluator_config_hash TEXT NOT NULL,
              created_at_ns INTEGER NOT NULL
            );
            CREATE TABLE IF NOT EXISTS components (
              experiment_id TEXT NOT NULL,
              file_path TEXT NOT NULL,
              component_class TEXT NOT NULL,
              baseline_hash TEXT NOT NULL,
              mutable INTEGER NOT NULL,
              PRIMARY KEY(experiment_id,file_path),
              FOREIGN KEY(experiment_id) REFERENCES experiments(experiment_id)
            );
            CREATE TABLE IF NOT EXISTS mutations (
              mutation_id TEXT PRIMARY KEY,
              experiment_id TEXT NOT NULL,
              root_cause_hash TEXT NOT NULL,
              evidence_bundle_hash TEXT NOT NULL,
              predicted_fix_json TEXT NOT NULL,
              predicted_regression_json TEXT NOT NULL,
              attribution_mode TEXT NOT NULL,
              coupling_reason_hash TEXT,
              state TEXT NOT NULL,
              created_at_ns INTEGER NOT NULL,
              FOREIGN KEY(experiment_id) REFERENCES experiments(experiment_id)
            );
            CREATE TABLE IF NOT EXISTS changes (
              mutation_id TEXT NOT NULL,
              file_path TEXT NOT NULL,
              component_class TEXT NOT NULL,
              before_hash TEXT NOT NULL,
              after_hash TEXT NOT NULL,
              rollback_hash TEXT NOT NULL,
              PRIMARY KEY(mutation_id,file_path),
              FOREIGN KEY(mutation_id) REFERENCES mutations(mutation_id)
            );
            CREATE TABLE IF NOT EXISTS isolation (
              mutation_id TEXT PRIMARY KEY,
              mode TEXT NOT NULL,
              prior_shared_verifier_state INTEGER NOT NULL,
              sanitized_before_agent INTEGER NOT NULL,
              prior_tests_hidden INTEGER NOT NULL,
              prior_reward_hidden INTEGER NOT NULL,
              agent_owned_state_preserved INTEGER NOT NULL,
              evidence_hash TEXT NOT NULL,
              FOREIGN KEY(mutation_id) REFERENCES mutations(mutation_id)
            );
            CREATE TABLE IF NOT EXISTS evaluation_bindings (
              mutation_id TEXT PRIMARY KEY,
              baseline_run_hash TEXT NOT NULL,
              candidate_run_hash TEXT NOT NULL,
              comparison_hash TEXT NOT NULL,
              calibration_report_hash TEXT NOT NULL,
              calibration_gate_hash TEXT NOT NULL,
              comparison_state TEXT NOT NULL,
              calibration_verdict TEXT NOT NULL,
              attribution_plausible INTEGER NOT NULL,
              FOREIGN KEY(mutation_id) REFERENCES mutations(mutation_id)
            );
            CREATE TABLE IF NOT EXISTS decisions (
              mutation_id TEXT PRIMARY KEY,
              verdict TEXT NOT NULL,
              reasons_json TEXT NOT NULL,
              fixed_json TEXT NOT NULL,
              regressed_json TEXT NOT NULL,
              critical_regressions_json TEXT NOT NULL,
              fix_precision REAL NOT NULL,
              regression_recall REAL NOT NULL,
              receipt_hash TEXT NOT NULL,
              FOREIGN KEY(mutation_id) REFERENCES mutations(mutation_id)
            );
            CREATE TABLE IF NOT EXISTS reconciliations (
              mutation_id TEXT PRIMARY KEY,
              state TEXT NOT NULL,
              observed_version TEXT NOT NULL,
              observed_component_hashes_json TEXT NOT NULL,
              evidence_hash TEXT NOT NULL,
              FOREIGN KEY(mutation_id) REFERENCES mutations(mutation_id)
            );
            CREATE TABLE IF NOT EXISTS ledger (
              seq INTEGER PRIMARY KEY AUTOINCREMENT,
              event_type TEXT NOT NULL,
              payload_json TEXT NOT NULL,
              ts_ns INTEGER NOT NULL,
              prev_hash TEXT NOT NULL,
              event_hash TEXT NOT NULL
            );
            """
        )
        self.db.commit()

    def _event(self, event_type: str, payload: dict[str, Any]) -> str:
        _reject_raw(payload)
        p = _canonical_json(payload)
        row = self.db.execute("SELECT event_hash FROM ledger ORDER BY seq DESC LIMIT 1").fetchone()
        prev = row["event_hash"] if row else "0" * 64
        ts = _now_ns()
        h = _ledger_hash(prev, event_type, p, ts)
        self.db.execute(
            "INSERT INTO ledger(event_type,payload_json,ts_ns,prev_hash,event_hash) VALUES(?,?,?,?,?)",
            (event_type, p, ts, prev, h),
        )
        self.db.commit()
        return h

    def _experiment(self, experiment_id: str) -> sqlite3.Row:
        row = self.db.execute("SELECT * FROM experiments WHERE experiment_id=?", (experiment_id,)).fetchone()
        if row is None:
            raise HarnessEvolutionError(f"unknown experiment_id: {experiment_id}")
        return row

    def _mutation(self, mutation_id: str) -> sqlite3.Row:
        row = self.db.execute("SELECT * FROM mutations WHERE mutation_id=?", (mutation_id,)).fetchone()
        if row is None:
            raise HarnessEvolutionError(f"unknown mutation_id: {mutation_id}")
        return row

    def _require_state(self, mutation_id: str, *states: str) -> sqlite3.Row:
        row = self._mutation(mutation_id)
        if row["state"] not in states:
            raise HarnessEvolutionError(f"mutation state {row['state']} not in {states}")
        return row

    def create_experiment(
        self,
        *,
        target_id: str,
        target_version: str,
        harness_id: str,
        baseline_version: str,
        candidate_version: str,
        suite_id: str,
        environment_id: str,
        evaluator_set_id: str,
        evaluator_version: str,
        model_id: str,
        model_config_hash: str,
        budget_id: str,
        task_cohort_hash: str,
        evidence_archetype: str,
        expected_task_count: int,
        calibrated_evaluator_id: str,
        calibrated_evaluator_version: str,
        calibrated_evaluator_config_hash: str,
        experiment_id: str | None = None,
    ) -> str:
        for name, value in (
            ("target_id", target_id), ("target_version", target_version), ("harness_id", harness_id),
            ("baseline_version", baseline_version), ("candidate_version", candidate_version), ("suite_id", suite_id),
            ("environment_id", environment_id), ("evaluator_set_id", evaluator_set_id),
            ("evaluator_version", evaluator_version), ("model_id", model_id), ("budget_id", budget_id),
            ("evidence_archetype", evidence_archetype), ("calibrated_evaluator_id", calibrated_evaluator_id),
            ("calibrated_evaluator_version", calibrated_evaluator_version),
        ):
            _nonempty(name, value)
        if baseline_version == candidate_version:
            raise HarnessEvolutionError("candidate_version must differ from baseline_version")
        _hash64("model_config_hash", model_config_hash)
        _hash64("task_cohort_hash", task_cohort_hash)
        _hash64("calibrated_evaluator_config_hash", calibrated_evaluator_config_hash)
        if not isinstance(expected_task_count, int) or expected_task_count <= 0:
            raise HarnessEvolutionError("expected_task_count must be positive integer")
        eid = experiment_id or uuid.uuid4().hex
        _nonempty("experiment_id", eid)
        self.db.execute(
            "INSERT INTO experiments VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                eid, target_id, target_version, harness_id, baseline_version, candidate_version,
                suite_id, environment_id, evaluator_set_id, evaluator_version, model_id, model_config_hash,
                budget_id, task_cohort_hash, evidence_archetype, expected_task_count,
                calibrated_evaluator_id, calibrated_evaluator_version, calibrated_evaluator_config_hash, _now_ns(),
            ),
        )
        self.db.commit()
        self._event("EXPERIMENT_CREATED", {"experiment_id": eid, "harness_id": harness_id})
        return eid

    def register_component(
        self,
        experiment_id: str,
        *,
        file_path: str,
        component_class: str,
        baseline_hash: str,
        mutable: bool = True,
    ) -> None:
        self._experiment(experiment_id)
        _nonempty("file_path", file_path)
        if component_class not in COMPONENT_CLASSES:
            raise HarnessEvolutionError("unsupported component_class")
        _hash64("baseline_hash", baseline_hash)
        self.db.execute(
            "INSERT INTO components VALUES(?,?,?,?,?)",
            (experiment_id, file_path, component_class, baseline_hash, int(bool(mutable))),
        )
        self.db.commit()
        self._event("COMPONENT_REGISTERED", {"experiment_id": experiment_id, "file_path": file_path, "component_class": component_class})

    def create_mutation(
        self,
        experiment_id: str,
        *,
        root_cause_hash: str,
        evidence_bundle_hash: str,
        predicted_fix_ids: Iterable[str],
        predicted_regression_ids: Iterable[str],
        attribution_mode: str,
        coupling_reason_hash: str | None = None,
        mutation_id: str | None = None,
    ) -> str:
        self._experiment(experiment_id)
        _hash64("root_cause_hash", root_cause_hash)
        _hash64("evidence_bundle_hash", evidence_bundle_hash)
        fixes = _as_sorted_ids("predicted_fix_id", predicted_fix_ids)
        regs = _as_sorted_ids("predicted_regression_id", predicted_regression_ids)
        if set(fixes) & set(regs):
            raise HarnessEvolutionError("same task cannot be predicted fix and regression")
        if attribution_mode not in ATTRIBUTION_MODES:
            raise HarnessEvolutionError("invalid attribution_mode")
        if attribution_mode == "COUPLED_SET":
            _hash64("coupling_reason_hash", coupling_reason_hash)
        elif coupling_reason_hash is not None:
            raise HarnessEvolutionError("coupling_reason_hash only valid for COUPLED_SET")
        mid = mutation_id or uuid.uuid4().hex
        _nonempty("mutation_id", mid)
        self.db.execute(
            "INSERT INTO mutations VALUES(?,?,?,?,?,?,?,?,?,?)",
            (
                mid, experiment_id, root_cause_hash, evidence_bundle_hash,
                _canonical_json(fixes), _canonical_json(regs), attribution_mode,
                coupling_reason_hash, "PROPOSED", _now_ns(),
            ),
        )
        self.db.commit()
        self._event("MUTATION_CREATED", {"mutation_id": mid, "experiment_id": experiment_id})
        return mid

    def stage_change(
        self,
        mutation_id: str,
        *,
        file_path: str,
        before_hash: str,
        after_hash: str,
        rollback_hash: str,
    ) -> None:
        mutation = self._require_state(mutation_id, "PROPOSED")
        _hash64("before_hash", before_hash)
        _hash64("after_hash", after_hash)
        _hash64("rollback_hash", rollback_hash)
        if before_hash == after_hash:
            raise HarnessEvolutionError("change must alter content hash")
        if rollback_hash != before_hash:
            raise HarnessEvolutionError("rollback_hash must equal before_hash for reversible staged mutation")
        component = self.db.execute(
            "SELECT * FROM components WHERE experiment_id=? AND file_path=?",
            (mutation["experiment_id"], file_path),
        ).fetchone()
        if component is None:
            raise HarnessEvolutionError("file_path is not a declared harness component")
        if not component["mutable"]:
            raise HarnessEvolutionError("component is immutable in this experiment")
        if component["baseline_hash"] != before_hash:
            raise HarnessEvolutionError("before_hash does not match frozen baseline component hash")
        self.db.execute(
            "INSERT INTO changes VALUES(?,?,?,?,?,?)",
            (mutation_id, file_path, component["component_class"], before_hash, after_hash, rollback_hash),
        )
        self.db.commit()
        self._event("CHANGE_STAGED", {"mutation_id": mutation_id, "file_path": file_path, "component_class": component["component_class"]})

    def freeze_mutation(self, mutation_id: str) -> dict[str, Any]:
        mutation = self._require_state(mutation_id, "PROPOSED")
        rows = self.db.execute("SELECT * FROM changes WHERE mutation_id=? ORDER BY file_path", (mutation_id,)).fetchall()
        if not rows:
            raise HarnessEvolutionError("mutation requires at least one staged change")
        component_classes = {r["component_class"] for r in rows}
        if len(component_classes) > 1 and mutation["attribution_mode"] != "COUPLED_SET":
            raise HarnessEvolutionError("cross-component mutation requires COUPLED_SET attribution_mode")
        if mutation["attribution_mode"] == "COUPLED_SET" and not mutation["coupling_reason_hash"]:
            raise HarnessEvolutionError("COUPLED_SET requires coupling_reason_hash")
        self.db.execute("UPDATE mutations SET state='STAGED' WHERE mutation_id=?", (mutation_id,))
        self.db.commit()
        self._event("MUTATION_FROZEN", {"mutation_id": mutation_id, "change_count": len(rows)})
        return self.mutation_receipt(mutation_id)

    def record_isolation(
        self,
        mutation_id: str,
        *,
        mode: str,
        prior_shared_verifier_state: bool,
        sanitized_before_agent: bool,
        prior_tests_hidden: bool,
        prior_reward_hidden: bool,
        agent_owned_state_preserved: bool,
        evidence_hash: str,
    ) -> dict[str, Any]:
        self._require_state(mutation_id, "STAGED")
        if mode not in ISOLATION_MODES:
            raise HarnessEvolutionError("invalid isolation mode")
        _hash64("evidence_hash", evidence_hash)
        if mode in {"SINGLE_STEP", "SEPARATE_VERIFIER"} and prior_shared_verifier_state:
            raise HarnessEvolutionError("prior_shared_verifier_state incompatible with isolation mode")
        self.db.execute(
            "INSERT INTO isolation VALUES(?,?,?,?,?,?,?,?)",
            (
                mutation_id, mode, int(prior_shared_verifier_state), int(sanitized_before_agent),
                int(prior_tests_hidden), int(prior_reward_hidden), int(agent_owned_state_preserved), evidence_hash,
            ),
        )
        self.db.commit()
        self._event("ISOLATION_RECORDED", {"mutation_id": mutation_id, "mode": mode})
        return self.isolation_receipt(mutation_id)

    def isolation_receipt(self, mutation_id: str) -> dict[str, Any]:
        row = self.db.execute("SELECT * FROM isolation WHERE mutation_id=?", (mutation_id,)).fetchone()
        if row is None:
            raise HarnessEvolutionError("isolation evidence missing")
        clean = bool(row["prior_tests_hidden"] and row["prior_reward_hidden"] and row["agent_owned_state_preserved"])
        if row["mode"] == "SHARED_VERIFIER" and row["prior_shared_verifier_state"]:
            clean = clean and bool(row["sanitized_before_agent"])
        receipt = {
            "schema": "amos.harness-evolution.isolation.v1",
            "mutation_id": mutation_id,
            "mode": row["mode"],
            "prior_shared_verifier_state": bool(row["prior_shared_verifier_state"]),
            "sanitized_before_agent": bool(row["sanitized_before_agent"]),
            "prior_tests_hidden": bool(row["prior_tests_hidden"]),
            "prior_reward_hidden": bool(row["prior_reward_hidden"]),
            "agent_owned_state_preserved": bool(row["agent_owned_state_preserved"]),
            "evidence_hash": row["evidence_hash"],
            "isolation_valid": clean,
            "isolation_semantics": ISOLATION_SEMANTICS,
        }
        receipt["receipt_hash"] = _sha256_json(receipt)
        return receipt

    def _validate_run_receipt(self, receipt: dict[str, Any], exp: sqlite3.Row, *, candidate: bool) -> None:
        _validate_receipt_hash(receipt)
        required = set(FROZEN_RUN_FIELDS) | {"run_id", "harness_version", "coverage_complete", "sealed"}
        missing = sorted(required - set(receipt))
        if missing:
            raise HarnessEvolutionError("run receipt missing: " + ",".join(missing))
        for field in FROZEN_RUN_FIELDS:
            expected = exp[field]
            if receipt.get(field) != expected:
                raise HarnessEvolutionError(f"run receipt {field} mismatch")
        expected_version = exp["candidate_version"] if candidate else exp["baseline_version"]
        if receipt.get("harness_version") != expected_version:
            raise HarnessEvolutionError("run receipt harness_version mismatch")
        if not receipt.get("sealed"):
            raise HarnessEvolutionError("run receipt must be sealed")
        if not receipt.get("coverage_complete"):
            raise HarnessEvolutionError("run receipt coverage must be complete")

    def _validate_calibration(
        self,
        exp: sqlite3.Row,
        report: dict[str, Any],
        gate: dict[str, Any],
    ) -> None:
        _validate_receipt_hash(report, schema="amos.evaluator-calibration.report.v1")
        _validate_receipt_hash(gate, schema="amos.evaluator-calibration.gate.v1")
        if report.get("phase") != "VALIDATION":
            raise HarnessEvolutionError("calibration report must be held-out VALIDATION phase")
        if report.get("session_id") != gate.get("session_id"):
            raise HarnessEvolutionError("calibration report/gate session mismatch")
        if report.get("evaluator_id") != exp["calibrated_evaluator_id"]:
            raise HarnessEvolutionError("calibrated evaluator id mismatch")
        if report.get("evaluator_version") != exp["calibrated_evaluator_version"]:
            raise HarnessEvolutionError("calibrated evaluator version mismatch")
        if report.get("evaluator_config_hash") != exp["calibrated_evaluator_config_hash"]:
            raise HarnessEvolutionError("calibrated evaluator config mismatch")

    def bind_evaluation(
        self,
        mutation_id: str,
        *,
        baseline_run_receipt: dict[str, Any],
        candidate_run_receipt: dict[str, Any],
        comparison_receipt: dict[str, Any],
        calibration_report_receipt: dict[str, Any],
        calibration_gate_receipt: dict[str, Any],
        attribution_plausible: bool,
    ) -> dict[str, Any]:
        mutation = self._require_state(mutation_id, "STAGED")
        exp = self._experiment(mutation["experiment_id"])
        isolation = self.isolation_receipt(mutation_id)
        self._validate_run_receipt(baseline_run_receipt, exp, candidate=False)
        self._validate_run_receipt(candidate_run_receipt, exp, candidate=True)
        _validate_receipt_hash(comparison_receipt)
        self._validate_calibration(exp, calibration_report_receipt, calibration_gate_receipt)
        if comparison_receipt.get("baseline_run_id") != baseline_run_receipt.get("run_id"):
            raise HarnessEvolutionError("comparison baseline_run_id mismatch")
        if comparison_receipt.get("candidate_run_id") != candidate_run_receipt.get("run_id"):
            raise HarnessEvolutionError("comparison candidate_run_id mismatch")
        if comparison_receipt.get("state") not in {"COMPARABLE", "NOT_COMPARABLE"}:
            raise HarnessEvolutionError("invalid comparison state")
        if comparison_receipt.get("state") == "COMPARABLE" and comparison_receipt.get("reasons"):
            raise HarnessEvolutionError("comparable receipt cannot carry incompatibility reasons")
        if comparison_receipt.get("state") == "NOT_COMPARABLE" and not comparison_receipt.get("reasons"):
            raise HarnessEvolutionError("not-comparable receipt requires reasons")
        self.db.execute(
            "INSERT INTO evaluation_bindings VALUES(?,?,?,?,?,?,?,?,?)",
            (
                mutation_id,
                baseline_run_receipt["receipt_hash"], candidate_run_receipt["receipt_hash"],
                comparison_receipt["receipt_hash"], calibration_report_receipt["receipt_hash"],
                calibration_gate_receipt["receipt_hash"], comparison_receipt["state"],
                calibration_gate_receipt.get("verdict"), int(bool(attribution_plausible)),
            ),
        )
        self.db.execute("UPDATE mutations SET state='EVALUATED' WHERE mutation_id=?", (mutation_id,))
        self.db.commit()
        self._event("EVALUATION_BOUND", {"mutation_id": mutation_id, "comparison_state": comparison_receipt["state"]})
        return {
            "mutation_id": mutation_id,
            "comparison_state": comparison_receipt["state"],
            "calibration_verdict": calibration_gate_receipt.get("verdict"),
            "isolation_valid": isolation["isolation_valid"],
            "attribution_plausible": bool(attribution_plausible),
        }

    def decision(self, mutation_id: str, *, comparison_receipt: dict[str, Any], calibration_gate_receipt: dict[str, Any]) -> dict[str, Any]:
        mutation = self._require_state(mutation_id, "EVALUATED")
        _validate_receipt_hash(comparison_receipt)
        _validate_receipt_hash(calibration_gate_receipt, schema="amos.evaluator-calibration.gate.v1")
        binding = self.db.execute("SELECT * FROM evaluation_bindings WHERE mutation_id=?", (mutation_id,)).fetchone()
        if binding is None:
            raise HarnessEvolutionError("evaluation binding missing")
        if comparison_receipt["receipt_hash"] != binding["comparison_hash"]:
            raise HarnessEvolutionError("comparison receipt differs from bound evidence")
        if calibration_gate_receipt["receipt_hash"] != binding["calibration_gate_hash"]:
            raise HarnessEvolutionError("calibration gate differs from bound evidence")
        isolation = self.isolation_receipt(mutation_id)
        fixed = sorted(set(comparison_receipt.get("fixed_task_ids", [])))
        regressed = sorted(set(comparison_receipt.get("regressed_task_ids", [])))
        critical = sorted(set(comparison_receipt.get("critical_regression_task_ids", [])))
        predicted_fix = set(json.loads(mutation["predicted_fix_json"]))
        predicted_reg = set(json.loads(mutation["predicted_regression_json"]))
        fixed_set = set(fixed)
        regressed_set = set(regressed)
        fix_precision = len(predicted_fix & fixed_set) / max(1, len(predicted_fix))
        regression_recall = 1.0 if not regressed_set else len(predicted_reg & regressed_set) / len(regressed_set)
        reasons: list[str] = []
        if binding["comparison_state"] != "COMPARABLE":
            reasons.append("evaluation runs are not comparable")
        if binding["calibration_verdict"] != "PASS":
            reasons.append("evaluator reliability gate is not PASS")
        if not isolation["isolation_valid"]:
            reasons.append("evaluation isolation evidence is invalid")
        if not binding["attribution_plausible"]:
            reasons.append("attribution not plausible under frozen-axis evidence")

        if critical:
            verdict = "ROLLBACK"
            reasons.append("critical regression observed")
        elif not reasons and len(regressed) > len(fixed):
            verdict = "ROLLBACK"
            reasons.append("regressions exceed fixes")
        elif not reasons and fixed and len(fixed) > len(regressed):
            verdict = "KEEP"
            reasons.append("bounded net improvement with no critical regression")
        else:
            verdict = "INCONCLUSIVE"
            if not reasons:
                reasons.append("evidence does not establish bounded net improvement")

        state = {
            "KEEP": "KEEP_RECOMMENDED",
            "ROLLBACK": "ROLLBACK_RECOMMENDED",
            "INCONCLUSIVE": "INCONCLUSIVE",
        }[verdict]
        result = {
            "schema": "amos.harness-evolution.decision.v1",
            "mutation_id": mutation_id,
            "verdict": verdict,
            "reasons": reasons,
            "fixed_task_ids": fixed,
            "regressed_task_ids": regressed,
            "critical_regression_task_ids": critical,
            "predicted_fix_ids": sorted(predicted_fix),
            "predicted_regression_ids": sorted(predicted_reg),
            "fix_precision": fix_precision,
            "regression_recall": regression_recall,
            "comparison_state": binding["comparison_state"],
            "calibration_verdict": binding["calibration_verdict"],
            "isolation_valid": isolation["isolation_valid"],
            "attribution_plausible": bool(binding["attribution_plausible"]),
            "authority_semantics": AUTHORITY_SEMANTICS,
            "causal_semantics": CAUSAL_SEMANTICS,
            "rollback_semantics": ROLLBACK_SEMANTICS,
            "evaluator_semantics": EVALUATOR_SEMANTICS,
        }
        result["receipt_hash"] = _sha256_json(result)
        self.db.execute(
            "INSERT INTO decisions VALUES(?,?,?,?,?,?,?,?,?)",
            (
                mutation_id, verdict, _canonical_json(reasons), _canonical_json(fixed),
                _canonical_json(regressed), _canonical_json(critical), fix_precision,
                regression_recall, result["receipt_hash"],
            ),
        )
        self.db.execute("UPDATE mutations SET state=? WHERE mutation_id=?", (state, mutation_id))
        self.db.commit()
        self._event("DECISION_RECORDED", {"mutation_id": mutation_id, "verdict": verdict})
        return result

    def reconcile(
        self,
        mutation_id: str,
        *,
        state: str,
        observed_version: str,
        observed_component_hashes: dict[str, str],
        evidence_hash: str,
    ) -> dict[str, Any]:
        mutation = self._require_state(mutation_id, "KEEP_RECOMMENDED", "ROLLBACK_RECOMMENDED", "INCONCLUSIVE")
        if state not in RECONCILIATION_STATES:
            raise HarnessEvolutionError("invalid reconciliation state")
        _nonempty("observed_version", observed_version)
        _hash64("evidence_hash", evidence_hash)
        changes = {r["file_path"]: r for r in self.db.execute("SELECT * FROM changes WHERE mutation_id=?", (mutation_id,))}
        if set(observed_component_hashes) != set(changes):
            raise HarnessEvolutionError("reconciliation must cover every changed component exactly")
        for path, h in observed_component_hashes.items():
            _hash64(f"observed_component_hashes[{path}]", h)
        if state == "KEPT":
            expected_version = self._experiment(mutation["experiment_id"])["candidate_version"]
            if observed_version != expected_version:
                raise HarnessEvolutionError("KEPT reconciliation version mismatch")
            for path, row in changes.items():
                if observed_component_hashes[path] != row["after_hash"]:
                    raise HarnessEvolutionError("KEPT reconciliation hash mismatch")
        elif state == "ROLLED_BACK":
            expected_version = self._experiment(mutation["experiment_id"])["baseline_version"]
            if observed_version != expected_version:
                raise HarnessEvolutionError("ROLLED_BACK reconciliation version mismatch")
            for path, row in changes.items():
                if observed_component_hashes[path] != row["rollback_hash"]:
                    raise HarnessEvolutionError("ROLLED_BACK reconciliation hash mismatch")
        self.db.execute(
            "INSERT INTO reconciliations VALUES(?,?,?,?,?)",
            (mutation_id, state, observed_version, _canonical_json(observed_component_hashes), evidence_hash),
        )
        self.db.execute("UPDATE mutations SET state='RECONCILED' WHERE mutation_id=?", (mutation_id,))
        self.db.commit()
        self._event("RECONCILED", {"mutation_id": mutation_id, "state": state})
        result = {
            "schema": "amos.harness-evolution.reconciliation.v1",
            "mutation_id": mutation_id,
            "state": state,
            "observed_version": observed_version,
            "observed_component_hashes": dict(sorted(observed_component_hashes.items())),
            "evidence_hash": evidence_hash,
            "authority_semantics": AUTHORITY_SEMANTICS,
        }
        result["receipt_hash"] = _sha256_json(result)
        return result

    def mutation_receipt(self, mutation_id: str) -> dict[str, Any]:
        mutation = self._mutation(mutation_id)
        changes = [dict(r) for r in self.db.execute("SELECT * FROM changes WHERE mutation_id=? ORDER BY file_path", (mutation_id,))]
        receipt = {
            "schema": "amos.harness-evolution.mutation.v1",
            "mutation_id": mutation_id,
            "experiment_id": mutation["experiment_id"],
            "root_cause_hash": mutation["root_cause_hash"],
            "evidence_bundle_hash": mutation["evidence_bundle_hash"],
            "predicted_fix_ids": json.loads(mutation["predicted_fix_json"]),
            "predicted_regression_ids": json.loads(mutation["predicted_regression_json"]),
            "attribution_mode": mutation["attribution_mode"],
            "coupling_reason_hash": mutation["coupling_reason_hash"],
            "state": mutation["state"],
            "changes": [
                {
                    "file_path": r["file_path"],
                    "component_class": r["component_class"],
                    "before_hash": r["before_hash"],
                    "after_hash": r["after_hash"],
                    "rollback_hash": r["rollback_hash"],
                }
                for r in changes
            ],
            "authority_semantics": AUTHORITY_SEMANTICS,
            "causal_semantics": CAUSAL_SEMANTICS,
        }
        receipt["receipt_hash"] = _sha256_json(receipt)
        return receipt

    def verify_ledger(self) -> bool:
        prev = "0" * 64
        rows = self.db.execute("SELECT seq,event_type,payload_json,ts_ns,prev_hash,event_hash FROM ledger ORDER BY seq").fetchall()
        for row in rows:
            if row["prev_hash"] != prev:
                return False
            expected = _ledger_hash(prev, row["event_type"], row["payload_json"], row["ts_ns"])
            if row["event_hash"] != expected:
                return False
            prev = row["event_hash"]
        return True


def _self_test() -> None:
    rt = HarnessEvolutionRuntime()
    h = lambda c: c * 64
    exp = rt.create_experiment(
        target_id="amos", target_version="1", harness_id="h", baseline_version="v1", candidate_version="v2",
        suite_id="s", environment_id="e", evaluator_set_id="judge-set", evaluator_version="1",
        model_id="m", model_config_hash=h("a"), budget_id="b", task_cohort_hash=h("b"),
        evidence_archetype="PROCESS", expected_task_count=1,
        calibrated_evaluator_id="judge", calibrated_evaluator_version="1", calibrated_evaluator_config_hash=h("c"),
    )
    rt.register_component(exp, file_path="SKILL.md", component_class="SKILL", baseline_hash=h("d"))
    mid = rt.create_mutation(exp, root_cause_hash=h("e"), evidence_bundle_hash=h("f"), predicted_fix_ids=["t1"], predicted_regression_ids=[], attribution_mode="SINGLE_COMPONENT")
    rt.stage_change(mid, file_path="SKILL.md", before_hash=h("d"), after_hash=h("1"), rollback_hash=h("d"))
    rt.freeze_mutation(mid)
    iso = rt.record_isolation(mid, mode="SINGLE_STEP", prior_shared_verifier_state=False, sanitized_before_agent=False, prior_tests_hidden=True, prior_reward_hidden=True, agent_owned_state_preserved=True, evidence_hash=h("2"))
    assert iso["isolation_valid"]
    assert rt.verify_ledger()
    print("harness_evolution_runtime self-test: PASS")


if __name__ == "__main__":
    _self_test()
