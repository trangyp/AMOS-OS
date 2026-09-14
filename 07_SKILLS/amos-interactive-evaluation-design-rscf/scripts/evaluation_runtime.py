#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sqlite3
import time
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

EVIDENCE_ARCHETYPES = {"CONTRACT", "INTERVENTION", "PROCESS", "OUTCOME_PROPERTY"}
EVALUATOR_KINDS = {"DETERMINISTIC", "MODEL_JUDGE", "HUMAN", "EXTERNAL_RUNNER"}
JUDGMENTS = {"PASS", "FAIL", "ABSTAIN"}
REVIEW_DECISIONS = {"CONTINUE", "TERMINATE", "ESCALATE"}
REVIEW_STAGES = {"TOOL_RESULT", "TRAJECTORY", "TERMINAL"}
TASK_STATES = {"PASS", "FAIL", "UNKNOWN"}
COMPARISON_STATES = {"COMPARABLE", "NOT_COMPARABLE"}
MUTATION_VERDICTS = {"KEEP", "ROLLBACK", "INCONCLUSIVE"}

AUTHORITY_SEMANTICS = "EVALUATION_DOES_NOT_GRANT_AUTHORITY"
JUDGE_SEMANTICS = "JUDGE_OUTPUT_IS_EVIDENCE_NOT_GROUND_TRUTH"
REVIEW_SEMANTICS = "REVIEW_DECISION_IS_NOT_RUNTIME_AUTHORITY"
CAUSAL_SEMANTICS = "SCORE_DELTA_DOES_NOT_PROVE_CAUSAL_ATTRIBUTION"

FORBIDDEN_DURABLE_KEYS = {
    "prompt", "completion", "raw_input", "raw_output", "input_value", "output_value",
    "tool_output", "chain_of_thought", "reasoning", "authorization", "api_key", "token", "password",
}


class EvaluationError(RuntimeError):
    pass


class IncomparableRuns(EvaluationError):
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
        raise EvaluationError(f"{name} must be a non-empty string")
    return value.strip()


def _validate_hash(name: str, value: str | None, *, required: bool = False) -> str | None:
    if value is None and not required:
        return None
    if not isinstance(value, str) or len(value) != 64 or any(c not in "0123456789abcdef" for c in value):
        raise EvaluationError(f"{name} must be 64 lowercase hex chars")
    return value


def _reject_raw_content(value: Any, path: str = "$") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if str(key).lower() in FORBIDDEN_DURABLE_KEYS:
                raise EvaluationError(f"raw/sensitive durable field forbidden: {path}.{key}")
            _reject_raw_content(child, f"{path}.{key}")
    elif isinstance(value, list):
        for i, child in enumerate(value):
            _reject_raw_content(child, f"{path}[{i}]")


def _ledger_hash(prev_hash: str, event_type: str, payload_json: str, ts_ns: int) -> str:
    return _sha256_text(f"{prev_hash}|{event_type}|{payload_json}|{ts_ns}")


@dataclass(frozen=True)
class RunIdentity:
    run_id: str
    suite_id: str
    target_id: str
    target_version: str
    environment_id: str
    harness_id: str
    harness_version: str
    evaluator_set_id: str
    evaluator_version: str
    model_id: str
    model_config_hash: str
    budget_id: str
    task_cohort_hash: str
    evidence_archetype: str
    expected_task_count: int
    trace_id: str | None
    roundtrip_receipt_hash: str | None


class EvaluationRuntime:
    """Local deterministic evaluation/review evidence runtime.

    Scope: SQLite reference semantics only. It does not execute model judges, grant
    runtime authority, or establish deployment validity.
    """

    def __init__(self, db_path: str | Path = ":memory:") -> None:
        self.db_path = str(db_path)
        self.db = sqlite3.connect(self.db_path)
        self.db.row_factory = sqlite3.Row
        self.db.execute("PRAGMA foreign_keys=ON")
        self._init_schema()

    def close(self) -> None:
        self.db.close()

    def _init_schema(self) -> None:
        self.db.executescript(
            """
            CREATE TABLE IF NOT EXISTS runs (
              run_id TEXT PRIMARY KEY,
              suite_id TEXT NOT NULL,
              target_id TEXT NOT NULL,
              target_version TEXT NOT NULL,
              environment_id TEXT NOT NULL,
              harness_id TEXT NOT NULL,
              harness_version TEXT NOT NULL,
              evaluator_set_id TEXT NOT NULL,
              evaluator_version TEXT NOT NULL,
              model_id TEXT NOT NULL,
              model_config_hash TEXT NOT NULL,
              budget_id TEXT NOT NULL,
              task_cohort_hash TEXT NOT NULL,
              evidence_archetype TEXT NOT NULL,
              expected_task_count INTEGER NOT NULL,
              trace_id TEXT,
              roundtrip_receipt_hash TEXT,
              created_at_ns INTEGER NOT NULL,
              sealed_at_ns INTEGER
            );

            CREATE TABLE IF NOT EXISTS task_results (
              run_id TEXT NOT NULL,
              task_id TEXT NOT NULL,
              outcome_state TEXT NOT NULL,
              process_state TEXT NOT NULL,
              safety_state TEXT NOT NULL,
              recovered INTEGER NOT NULL,
              critical_failure INTEGER NOT NULL,
              evidence_hash TEXT NOT NULL,
              PRIMARY KEY (run_id, task_id),
              FOREIGN KEY (run_id) REFERENCES runs(run_id)
            );

            CREATE TABLE IF NOT EXISTS judgments (
              judgment_id TEXT PRIMARY KEY,
              run_id TEXT NOT NULL,
              task_id TEXT NOT NULL,
              criterion TEXT NOT NULL,
              evaluator_id TEXT NOT NULL,
              evaluator_version TEXT NOT NULL,
              evaluator_kind TEXT NOT NULL,
              judgment TEXT NOT NULL,
              score REAL,
              critical INTEGER NOT NULL,
              explanation_hash TEXT,
              evidence_ref TEXT NOT NULL,
              created_at_ns INTEGER NOT NULL,
              FOREIGN KEY (run_id) REFERENCES runs(run_id)
            );

            CREATE TABLE IF NOT EXISTS reviews (
              review_id TEXT PRIMARY KEY,
              run_id TEXT NOT NULL,
              task_id TEXT NOT NULL,
              stage TEXT NOT NULL,
              reviewer_id TEXT NOT NULL,
              reviewer_version TEXT NOT NULL,
              decision TEXT NOT NULL,
              subject_ref TEXT NOT NULL,
              subject_hash TEXT NOT NULL,
              explanation_hash TEXT,
              metadata_hash TEXT,
              created_at_ns INTEGER NOT NULL,
              FOREIGN KEY (run_id) REFERENCES runs(run_id)
            );

            CREATE TABLE IF NOT EXISTS comparisons (
              comparison_id TEXT PRIMARY KEY,
              baseline_run_id TEXT NOT NULL,
              candidate_run_id TEXT NOT NULL,
              state TEXT NOT NULL,
              reasons_json TEXT NOT NULL,
              fixed_json TEXT NOT NULL,
              regressed_json TEXT NOT NULL,
              unchanged_json TEXT NOT NULL,
              critical_regressions_json TEXT NOT NULL,
              created_at_ns INTEGER NOT NULL
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

    def _append_event(self, event_type: str, payload: dict[str, Any]) -> str:
        _reject_raw_content(payload)
        payload_json = _canonical_json(payload)
        row = self.db.execute("SELECT event_hash FROM ledger ORDER BY seq DESC LIMIT 1").fetchone()
        prev = row["event_hash"] if row else "0" * 64
        ts = _now_ns()
        event_hash = _ledger_hash(prev, event_type, payload_json, ts)
        self.db.execute(
            "INSERT INTO ledger(event_type,payload_json,ts_ns,prev_hash,event_hash) VALUES(?,?,?,?,?)",
            (event_type, payload_json, ts, prev, event_hash),
        )
        self.db.commit()
        return event_hash

    def create_run(
        self,
        *,
        suite_id: str,
        target_id: str,
        target_version: str,
        environment_id: str,
        harness_id: str,
        harness_version: str,
        evaluator_set_id: str,
        evaluator_version: str,
        model_id: str,
        model_config_hash: str,
        budget_id: str,
        task_cohort_hash: str,
        evidence_archetype: str,
        expected_task_count: int,
        trace_id: str | None = None,
        roundtrip_receipt_hash: str | None = None,
        run_id: str | None = None,
    ) -> str:
        for name, value in (
            ("suite_id", suite_id), ("target_id", target_id), ("target_version", target_version),
            ("environment_id", environment_id), ("harness_id", harness_id),
            ("harness_version", harness_version), ("evaluator_set_id", evaluator_set_id),
            ("evaluator_version", evaluator_version), ("model_id", model_id),
            ("budget_id", budget_id), ("task_cohort_hash", task_cohort_hash),
        ):
            _nonempty(name, value)
        _validate_hash("model_config_hash", model_config_hash, required=True)
        if roundtrip_receipt_hash is not None:
            _validate_hash("roundtrip_receipt_hash", roundtrip_receipt_hash, required=True)
        if evidence_archetype not in EVIDENCE_ARCHETYPES:
            raise EvaluationError(f"unsupported evidence_archetype: {evidence_archetype}")
        if not isinstance(expected_task_count, int) or expected_task_count <= 0:
            raise EvaluationError("expected_task_count must be positive integer")
        if trace_id is not None:
            _nonempty("trace_id", trace_id)
        rid = run_id or uuid.uuid4().hex
        _nonempty("run_id", rid)
        self.db.execute(
            """INSERT INTO runs(
                run_id,suite_id,target_id,target_version,environment_id,harness_id,harness_version,
                evaluator_set_id,evaluator_version,model_id,model_config_hash,budget_id,task_cohort_hash,
                evidence_archetype,expected_task_count,trace_id,roundtrip_receipt_hash,created_at_ns
            ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (
                rid, suite_id, target_id, target_version, environment_id, harness_id, harness_version,
                evaluator_set_id, evaluator_version, model_id, model_config_hash, budget_id, task_cohort_hash,
                evidence_archetype, expected_task_count, trace_id, roundtrip_receipt_hash, _now_ns(),
            ),
        )
        self.db.commit()
        self._append_event("RUN_CREATED", {"run_id": rid, "suite_id": suite_id, "target_id": target_id})
        return rid

    def _run_row(self, run_id: str) -> sqlite3.Row:
        row = self.db.execute("SELECT * FROM runs WHERE run_id=?", (run_id,)).fetchone()
        if row is None:
            raise EvaluationError(f"unknown run_id: {run_id}")
        return row

    def _require_open(self, run_id: str) -> sqlite3.Row:
        row = self._run_row(run_id)
        if row["sealed_at_ns"] is not None:
            raise EvaluationError("run is sealed")
        return row

    def record_task_result(
        self,
        run_id: str,
        task_id: str,
        *,
        outcome_state: str,
        process_state: str,
        safety_state: str,
        recovered: bool,
        critical_failure: bool,
        evidence: dict[str, Any],
    ) -> str:
        self._require_open(run_id)
        _nonempty("task_id", task_id)
        for name, state in (("outcome_state", outcome_state), ("process_state", process_state), ("safety_state", safety_state)):
            if state not in TASK_STATES:
                raise EvaluationError(f"{name} must be one of {sorted(TASK_STATES)}")
        _reject_raw_content(evidence)
        evidence_hash = _sha256_json(evidence)
        try:
            self.db.execute(
                "INSERT INTO task_results VALUES(?,?,?,?,?,?,?,?)",
                (run_id, task_id, outcome_state, process_state, safety_state, int(recovered), int(critical_failure), evidence_hash),
            )
        except sqlite3.IntegrityError as exc:
            raise EvaluationError(f"duplicate task result: {task_id}") from exc
        self.db.commit()
        self._append_event("TASK_RESULT_RECORDED", {"run_id": run_id, "task_id": task_id, "evidence_hash": evidence_hash})
        return evidence_hash

    def record_judgment(
        self,
        run_id: str,
        task_id: str,
        *,
        criterion: str,
        evaluator_id: str,
        evaluator_version: str,
        evaluator_kind: str,
        judgment: str,
        evidence_ref: str,
        score: float | None = None,
        critical: bool = False,
        explanation: str | None = None,
        judgment_id: str | None = None,
    ) -> str:
        self._require_open(run_id)
        for name, value in (
            ("task_id", task_id), ("criterion", criterion), ("evaluator_id", evaluator_id),
            ("evaluator_version", evaluator_version), ("evidence_ref", evidence_ref),
        ):
            _nonempty(name, value)
        if evaluator_kind not in EVALUATOR_KINDS:
            raise EvaluationError("invalid evaluator_kind")
        if judgment not in JUDGMENTS:
            raise EvaluationError("invalid judgment")
        if score is not None and not isinstance(score, (int, float)):
            raise EvaluationError("score must be numeric or null")
        jid = judgment_id or uuid.uuid4().hex
        explanation_hash = _sha256_text(explanation) if explanation is not None else None
        self.db.execute(
            "INSERT INTO judgments VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                jid, run_id, task_id, criterion, evaluator_id, evaluator_version, evaluator_kind,
                judgment, float(score) if score is not None else None, int(critical), explanation_hash,
                evidence_ref, _now_ns(),
            ),
        )
        self.db.commit()
        self._append_event(
            "JUDGMENT_RECORDED",
            {"judgment_id": jid, "run_id": run_id, "task_id": task_id, "criterion": criterion, "judgment": judgment},
        )
        return jid

    def record_review(
        self,
        run_id: str,
        task_id: str,
        *,
        stage: str,
        reviewer_id: str,
        reviewer_version: str,
        decision: str,
        subject_ref: str,
        subject_hash: str,
        explanation: str | None = None,
        metadata: dict[str, Any] | None = None,
        review_id: str | None = None,
    ) -> str:
        self._require_open(run_id)
        for name, value in (
            ("task_id", task_id), ("reviewer_id", reviewer_id), ("reviewer_version", reviewer_version),
            ("subject_ref", subject_ref),
        ):
            _nonempty(name, value)
        _validate_hash("subject_hash", subject_hash, required=True)
        if stage not in REVIEW_STAGES:
            raise EvaluationError("invalid review stage")
        if decision not in REVIEW_DECISIONS:
            raise EvaluationError("invalid review decision")
        if metadata is not None:
            _reject_raw_content(metadata)
        rid = review_id or uuid.uuid4().hex
        explanation_hash = _sha256_text(explanation) if explanation is not None else None
        metadata_hash = _sha256_json(metadata) if metadata is not None else None
        self.db.execute(
            "INSERT INTO reviews VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                rid, run_id, task_id, stage, reviewer_id, reviewer_version, decision,
                subject_ref, subject_hash, explanation_hash, metadata_hash, _now_ns(),
            ),
        )
        self.db.commit()
        self._append_event(
            "REVIEW_RECORDED",
            {"review_id": rid, "run_id": run_id, "task_id": task_id, "stage": stage, "decision": decision},
        )
        return rid

    def seal_run(self, run_id: str) -> dict[str, Any]:
        row = self._require_open(run_id)
        observed = self.db.execute("SELECT COUNT(*) AS n FROM task_results WHERE run_id=?", (run_id,)).fetchone()["n"]
        if observed > row["expected_task_count"]:
            raise EvaluationError("observed task count exceeds expected task count")
        sealed = _now_ns()
        self.db.execute("UPDATE runs SET sealed_at_ns=? WHERE run_id=?", (sealed, run_id))
        self.db.commit()
        self._append_event("RUN_SEALED", {"run_id": run_id, "observed_task_count": observed})
        return self.run_receipt(run_id)

    def judge_consensus(self, run_id: str, task_id: str, criterion: str) -> dict[str, Any]:
        rows = self.db.execute(
            "SELECT evaluator_id,evaluator_version,evaluator_kind,judgment,score,critical FROM judgments WHERE run_id=? AND task_id=? AND criterion=? ORDER BY evaluator_id,evaluator_version",
            (run_id, task_id, criterion),
        ).fetchall()
        if not rows:
            return {"status": "NO_EVIDENCE", "judgments": []}
        judgments = [dict(r) for r in rows]
        distinct = sorted({r["judgment"] for r in rows})
        status = "AGREED" if len(distinct) == 1 else "COMPETING"
        return {"status": status, "judgments": judgments, "aggregate_judgment": distinct[0] if status == "AGREED" else None}

    def _identity(self, run_id: str) -> RunIdentity:
        r = self._run_row(run_id)
        return RunIdentity(
            run_id=r["run_id"], suite_id=r["suite_id"], target_id=r["target_id"], target_version=r["target_version"],
            environment_id=r["environment_id"], harness_id=r["harness_id"], harness_version=r["harness_version"],
            evaluator_set_id=r["evaluator_set_id"], evaluator_version=r["evaluator_version"], model_id=r["model_id"],
            model_config_hash=r["model_config_hash"], budget_id=r["budget_id"], task_cohort_hash=r["task_cohort_hash"],
            evidence_archetype=r["evidence_archetype"], expected_task_count=r["expected_task_count"], trace_id=r["trace_id"],
            roundtrip_receipt_hash=r["roundtrip_receipt_hash"],
        )

    def comparison_compatibility(self, baseline_run_id: str, candidate_run_id: str) -> tuple[bool, list[str]]:
        b = self._identity(baseline_run_id)
        c = self._identity(candidate_run_id)
        fields = (
            "suite_id", "target_id", "target_version", "environment_id", "harness_id",
            "evaluator_set_id", "evaluator_version", "model_id", "model_config_hash", "budget_id",
            "task_cohort_hash", "evidence_archetype", "expected_task_count",
        )
        reasons = [f"{f} mismatch" for f in fields if getattr(b, f) != getattr(c, f)]
        if b.run_id == c.run_id:
            reasons.append("baseline and candidate run are identical")
        return not reasons, reasons

    def compare_runs(self, baseline_run_id: str, candidate_run_id: str, *, comparison_id: str | None = None) -> dict[str, Any]:
        b_row = self._run_row(baseline_run_id)
        c_row = self._run_row(candidate_run_id)
        if b_row["sealed_at_ns"] is None or c_row["sealed_at_ns"] is None:
            raise EvaluationError("both runs must be sealed before comparison")
        compatible, reasons = self.comparison_compatibility(baseline_run_id, candidate_run_id)
        fixed: list[str] = []
        regressed: list[str] = []
        unchanged: list[str] = []
        critical_regressions: list[str] = []
        if compatible:
            b = {r["task_id"]: r for r in self.db.execute("SELECT * FROM task_results WHERE run_id=?", (baseline_run_id,))}
            c = {r["task_id"]: r for r in self.db.execute("SELECT * FROM task_results WHERE run_id=?", (candidate_run_id,))}
            if set(b) != set(c):
                compatible = False
                reasons.append("observed task set mismatch")
            else:
                for task_id in sorted(b):
                    bp = b[task_id]["outcome_state"] == "PASS"
                    cp = c[task_id]["outcome_state"] == "PASS"
                    if not bp and cp:
                        fixed.append(task_id)
                    elif bp and not cp:
                        regressed.append(task_id)
                    else:
                        unchanged.append(task_id)
                    if not b[task_id]["critical_failure"] and c[task_id]["critical_failure"]:
                        critical_regressions.append(task_id)
        state = "COMPARABLE" if compatible else "NOT_COMPARABLE"
        cid = comparison_id or uuid.uuid4().hex
        self.db.execute(
            "INSERT INTO comparisons VALUES(?,?,?,?,?,?,?,?,?,?)",
            (
                cid, baseline_run_id, candidate_run_id, state, _canonical_json(reasons), _canonical_json(fixed),
                _canonical_json(regressed), _canonical_json(unchanged), _canonical_json(critical_regressions), _now_ns(),
            ),
        )
        self.db.commit()
        self._append_event("RUNS_COMPARED", {"comparison_id": cid, "state": state})
        receipt = {
            "comparison_id": cid,
            "baseline_run_id": baseline_run_id,
            "candidate_run_id": candidate_run_id,
            "state": state,
            "reasons": reasons,
            "fixed_task_ids": fixed,
            "regressed_task_ids": regressed,
            "unchanged_task_ids": unchanged,
            "critical_regression_task_ids": critical_regressions,
            "causal_semantics": CAUSAL_SEMANTICS,
            "authority_semantics": AUTHORITY_SEMANTICS,
        }
        receipt["receipt_hash"] = _sha256_json(receipt)
        return receipt

    def mutation_verdict(
        self,
        comparison: dict[str, Any],
        *,
        predicted_fix_ids: Iterable[str],
        predicted_regression_ids: Iterable[str],
        attribution_plausible: bool,
    ) -> dict[str, Any]:
        _reject_raw_content(comparison)
        if comparison.get("state") not in COMPARISON_STATES:
            raise EvaluationError("invalid comparison state")
        predicted_fix = sorted(set(predicted_fix_ids))
        predicted_reg = sorted(set(predicted_regression_ids))
        fixed = set(comparison.get("fixed_task_ids", []))
        regressed = set(comparison.get("regressed_task_ids", []))
        critical = set(comparison.get("critical_regression_task_ids", []))
        fix_precision = len(set(predicted_fix) & fixed) / max(1, len(predicted_fix))
        regression_recall = 1.0 if not regressed else len(set(predicted_reg) & regressed) / len(regressed)
        if comparison["state"] != "COMPARABLE" or not attribution_plausible:
            verdict = "INCONCLUSIVE"
        elif critical or len(regressed) > len(fixed):
            verdict = "ROLLBACK"
        elif fixed and len(fixed) > len(regressed):
            verdict = "KEEP"
        else:
            verdict = "INCONCLUSIVE"
        result = {
            "comparison_id": comparison.get("comparison_id"),
            "verdict": verdict,
            "predicted_fix_ids": predicted_fix,
            "predicted_regression_ids": predicted_reg,
            "observed_fixed_ids": sorted(fixed),
            "observed_regressed_ids": sorted(regressed),
            "critical_regression_ids": sorted(critical),
            "fix_precision": fix_precision,
            "regression_recall": regression_recall,
            "attribution_plausible": bool(attribution_plausible),
            "authority_semantics": AUTHORITY_SEMANTICS,
            "causal_semantics": CAUSAL_SEMANTICS,
        }
        result["receipt_hash"] = _sha256_json(result)
        return result

    def run_receipt(self, run_id: str) -> dict[str, Any]:
        row = self._run_row(run_id)
        observed = self.db.execute("SELECT COUNT(*) AS n FROM task_results WHERE run_id=?", (run_id,)).fetchone()["n"]
        judge_count = self.db.execute("SELECT COUNT(*) AS n FROM judgments WHERE run_id=?", (run_id,)).fetchone()["n"]
        review_count = self.db.execute("SELECT COUNT(*) AS n FROM reviews WHERE run_id=?", (run_id,)).fetchone()["n"]
        competing = self.db.execute(
            """SELECT task_id,criterion,COUNT(DISTINCT judgment) AS n
               FROM judgments WHERE run_id=? GROUP BY task_id,criterion HAVING n > 1""",
            (run_id,),
        ).fetchall()
        receipt = {
            "run_id": row["run_id"],
            "suite_id": row["suite_id"],
            "target_id": row["target_id"],
            "target_version": row["target_version"],
            "environment_id": row["environment_id"],
            "harness_id": row["harness_id"],
            "harness_version": row["harness_version"],
            "evaluator_set_id": row["evaluator_set_id"],
            "evaluator_version": row["evaluator_version"],
            "model_id": row["model_id"],
            "model_config_hash": row["model_config_hash"],
            "budget_id": row["budget_id"],
            "task_cohort_hash": row["task_cohort_hash"],
            "evidence_archetype": row["evidence_archetype"],
            "trace_id": row["trace_id"],
            "roundtrip_receipt_hash": row["roundtrip_receipt_hash"],
            "expected_task_count": row["expected_task_count"],
            "observed_task_count": observed,
            "coverage_complete": observed == row["expected_task_count"],
            "judgment_count": judge_count,
            "review_count": review_count,
            "competing_judgment_sets": [{"task_id": r["task_id"], "criterion": r["criterion"]} for r in competing],
            "sealed": row["sealed_at_ns"] is not None,
            "authority_semantics": AUTHORITY_SEMANTICS,
            "judge_semantics": JUDGE_SEMANTICS,
            "review_semantics": REVIEW_SEMANTICS,
        }
        receipt["receipt_hash"] = _sha256_json(receipt)
        return receipt

    def verify_integrity(self) -> tuple[bool, list[str]]:
        errors: list[str] = []
        prev = "0" * 64
        for row in self.db.execute("SELECT * FROM ledger ORDER BY seq"):
            if row["prev_hash"] != prev:
                errors.append(f"ledger seq {row['seq']} prev_hash mismatch")
            expected = _ledger_hash(row["prev_hash"], row["event_type"], row["payload_json"], row["ts_ns"])
            if row["event_hash"] != expected:
                errors.append(f"ledger seq {row['seq']} event_hash mismatch")
            try:
                _reject_raw_content(json.loads(row["payload_json"]))
            except Exception as exc:
                errors.append(f"ledger seq {row['seq']} contains forbidden field: {exc}")
            prev = row["event_hash"]
        return (not errors, errors)


__all__ = [
    "EvaluationRuntime", "EvaluationError", "IncomparableRuns", "RunIdentity",
    "AUTHORITY_SEMANTICS", "JUDGE_SEMANTICS", "REVIEW_SEMANTICS", "CAUSAL_SEMANTICS",
]
