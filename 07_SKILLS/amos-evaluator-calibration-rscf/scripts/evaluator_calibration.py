#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
import sqlite3
import statistics
import time
import uuid
from pathlib import Path
from typing import Any

PHASES = {"CALIBRATION", "VALIDATION"}
EVALUATOR_KINDS = {"DETERMINISTIC", "MODEL_JUDGE", "HUMAN", "EXTERNAL_RUNNER"}
REFERENCE_KINDS = {"HUMAN", "DETERMINISTIC", "MODEL", "CONSENSUS", "EXTERNAL_DATASET"}
INDEPENDENCE = {"INDEPENDENT", "RELATED", "UNKNOWN"}
SCORE_SEMANTICS = {"NONE", "PROBABILITY_PASS", "RANK_SCORE", "UNBOUNDED_SCORE"}
THRESHOLD_SOURCES = {"FIXED", "CALIBRATION_DERIVED", "NOT_APPLICABLE"}
REFERENCE_LABELS = {"PASS", "FAIL"}
EVALUATOR_LABELS = {"PASS", "FAIL", "ABSTAIN"}
GATE_STATES = {"PASS", "FAIL", "INCONCLUSIVE"}

AUTHORITY_SEMANTICS = "CALIBRATION_EVIDENCE_DOES_NOT_GRANT_AUTHORITY"
TRUTH_SEMANTICS = "REFERENCE_LABEL_IS_EVIDENCE_NOT_GROUND_TRUTH"
CALIBRATION_SEMANTICS = "CALIBRATED_ON_COHORT_DOES_NOT_IMPLY_GENERALIZATION"
AGREEMENT_SEMANTICS = "AGREEMENT_DOES_NOT_IMPLY_TRUTH"
PROBABILITY_SEMANTICS = "SCORE_IS_NOT_A_PROBABILITY_UNLESS_DECLARED_AND_VALIDATED"
CAUSAL_SEMANTICS = "EVALUATOR_DRIFT_DELTA_DOES_NOT_PROVE_CAUSAL_ATTRIBUTION"
DEPLOYMENT_SEMANTICS = "RELIABILITY_GATE_PASS_DOES_NOT_IMPLY_DEPLOYMENT_VALIDITY"

FORBIDDEN_DURABLE_KEYS = {
    "prompt", "completion", "raw_input", "raw_output", "input_value", "output_value",
    "tool_output", "chain_of_thought", "reasoning", "authorization", "api_key",
    "token", "password", "secret", "credential",
}


class CalibrationError(RuntimeError):
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
        raise CalibrationError(f"{name} must be a non-empty string")
    return value.strip()


def _hash64(name: str, value: str) -> str:
    if not isinstance(value, str) or len(value) != 64 or any(c not in "0123456789abcdef" for c in value):
        raise CalibrationError(f"{name} must be 64 lowercase hex chars")
    return value


def _reject_raw(value: Any, path: str = "$") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if str(key).lower() in FORBIDDEN_DURABLE_KEYS:
                raise CalibrationError(f"raw/sensitive durable field forbidden: {path}.{key}")
            _reject_raw(child, f"{path}.{key}")
    elif isinstance(value, list):
        for i, child in enumerate(value):
            _reject_raw(child, f"{path}[{i}]")


def _ledger_hash(prev_hash: str, event_type: str, payload_json: str, ts_ns: int) -> str:
    return _sha256_text(f"{prev_hash}|{event_type}|{payload_json}|{ts_ns}")


def _safe_ratio(num: int | float, den: int | float) -> float | None:
    return None if den == 0 else float(num) / float(den)


def wilson_interval(successes: int, n: int, confidence_level: float = 0.95) -> tuple[float, float] | None:
    """Wilson score interval for a binomial proportion.

    Established mathematics. Assumes Bernoulli observations and interprets the
    supplied sample as appropriate for the requested interval. It does not prove
    independence, representativeness, or external validity.
    """
    if not isinstance(successes, int) or not isinstance(n, int) or n < 0 or successes < 0 or successes > n:
        raise CalibrationError("invalid successes/n")
    if not (0.0 < confidence_level < 1.0):
        raise CalibrationError("confidence_level must lie in (0,1)")
    if n == 0:
        return None
    p = successes / n
    z = statistics.NormalDist().inv_cdf(0.5 + confidence_level / 2.0)
    z2 = z * z
    denom = 1.0 + z2 / n
    center = (p + z2 / (2.0 * n)) / denom
    half = z / denom * math.sqrt(p * (1.0 - p) / n + z2 / (4.0 * n * n))
    return max(0.0, center - half), min(1.0, center + half)


def brier_score(probabilities: list[float], labels: list[int]) -> float | None:
    """Mean squared probabilistic loss for binary outcomes."""
    if len(probabilities) != len(labels):
        raise CalibrationError("probabilities and labels length mismatch")
    if not probabilities:
        return None
    for q in probabilities:
        if not isinstance(q, (int, float)) or not (0.0 <= float(q) <= 1.0):
            raise CalibrationError("probabilities must lie in [0,1]")
    if any(y not in (0, 1) for y in labels):
        raise CalibrationError("binary labels must be 0 or 1")
    return sum((float(q) - y) ** 2 for q, y in zip(probabilities, labels)) / len(probabilities)


def expected_calibration_error(probabilities: list[float], labels: list[int], bins: int = 10) -> float | None:
    """Fixed-bin ECE for declared binary probabilities.

    This is a descriptive calibration statistic, not a proper scoring rule and
    not a correctness or deployment guarantee.
    """
    if len(probabilities) != len(labels):
        raise CalibrationError("probabilities and labels length mismatch")
    if not isinstance(bins, int) or bins < 2:
        raise CalibrationError("bins must be integer >=2")
    if not probabilities:
        return None
    groups: list[list[tuple[float, int]]] = [[] for _ in range(bins)]
    for q, y in zip(probabilities, labels):
        qf = float(q)
        if not (0.0 <= qf <= 1.0) or y not in (0, 1):
            raise CalibrationError("invalid probability/label")
        idx = min(bins - 1, int(qf * bins))
        groups[idx].append((qf, y))
    n = len(probabilities)
    ece = 0.0
    for group in groups:
        if not group:
            continue
        mean_q = sum(q for q, _ in group) / len(group)
        empirical = sum(y for _, y in group) / len(group)
        ece += len(group) / n * abs(mean_q - empirical)
    return ece


class CalibrationRuntime:
    """Deterministic local evaluator calibration evidence runtime.

    It records bounded calibration/validation evidence. It does not execute model
    judges, declare reference labels to be truth, or grant deployment authority.
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
            CREATE TABLE IF NOT EXISTS sessions (
              session_id TEXT PRIMARY KEY,
              phase TEXT NOT NULL,
              evaluator_id TEXT NOT NULL,
              evaluator_version TEXT NOT NULL,
              evaluator_kind TEXT NOT NULL,
              evaluator_config_hash TEXT NOT NULL,
              cohort_hash TEXT NOT NULL,
              expected_count INTEGER NOT NULL,
              reference_source_id TEXT NOT NULL,
              reference_source_version TEXT NOT NULL,
              reference_kind TEXT NOT NULL,
              reference_independence TEXT NOT NULL,
              score_semantics TEXT NOT NULL,
              threshold_value REAL,
              threshold_source TEXT NOT NULL,
              parent_calibration_id TEXT,
              created_at_ns INTEGER NOT NULL,
              sealed_at_ns INTEGER,
              FOREIGN KEY(parent_calibration_id) REFERENCES sessions(session_id)
            );
            CREATE TABLE IF NOT EXISTS observations (
              session_id TEXT NOT NULL,
              task_id TEXT NOT NULL,
              reference_label TEXT NOT NULL,
              evaluator_label TEXT NOT NULL,
              score REAL,
              evidence_ref TEXT NOT NULL,
              metadata_hash TEXT,
              PRIMARY KEY(session_id,task_id),
              FOREIGN KEY(session_id) REFERENCES sessions(session_id)
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
        self.db.execute("INSERT INTO ledger(event_type,payload_json,ts_ns,prev_hash,event_hash) VALUES(?,?,?,?,?)", (event_type, p, ts, prev, h))
        self.db.commit()
        return h

    def _session(self, session_id: str) -> sqlite3.Row:
        row = self.db.execute("SELECT * FROM sessions WHERE session_id=?", (session_id,)).fetchone()
        if row is None:
            raise CalibrationError(f"unknown session_id: {session_id}")
        return row

    def _open(self, session_id: str) -> sqlite3.Row:
        row = self._session(session_id)
        if row["sealed_at_ns"] is not None:
            raise CalibrationError("session is sealed")
        return row

    def create_session(
        self,
        *,
        phase: str,
        evaluator_id: str,
        evaluator_version: str,
        evaluator_kind: str,
        evaluator_config_hash: str,
        cohort_hash: str,
        expected_count: int,
        reference_source_id: str,
        reference_source_version: str,
        reference_kind: str,
        reference_independence: str,
        score_semantics: str,
        threshold_value: float | None,
        threshold_source: str,
        parent_calibration_id: str | None = None,
        session_id: str | None = None,
    ) -> str:
        if phase not in PHASES:
            raise CalibrationError("invalid phase")
        for name, value in (
            ("evaluator_id", evaluator_id), ("evaluator_version", evaluator_version),
            ("reference_source_id", reference_source_id), ("reference_source_version", reference_source_version),
        ):
            _nonempty(name, value)
        if evaluator_kind not in EVALUATOR_KINDS:
            raise CalibrationError("invalid evaluator_kind")
        if reference_kind not in REFERENCE_KINDS:
            raise CalibrationError("invalid reference_kind")
        if reference_independence not in INDEPENDENCE:
            raise CalibrationError("invalid reference_independence")
        if score_semantics not in SCORE_SEMANTICS:
            raise CalibrationError("invalid score_semantics")
        if threshold_source not in THRESHOLD_SOURCES:
            raise CalibrationError("invalid threshold_source")
        _hash64("evaluator_config_hash", evaluator_config_hash)
        _hash64("cohort_hash", cohort_hash)
        if not isinstance(expected_count, int) or expected_count <= 0:
            raise CalibrationError("expected_count must be positive integer")
        if threshold_value is not None and not isinstance(threshold_value, (int, float)):
            raise CalibrationError("threshold_value must be numeric or null")
        if threshold_source == "NOT_APPLICABLE" and threshold_value is not None:
            raise CalibrationError("NOT_APPLICABLE threshold_source requires null threshold")
        if phase == "CALIBRATION":
            if parent_calibration_id is not None:
                raise CalibrationError("CALIBRATION session cannot have parent_calibration_id")
        else:
            if parent_calibration_id is None:
                raise CalibrationError("VALIDATION session requires parent_calibration_id")
            parent = self._session(parent_calibration_id)
            if parent["phase"] != "CALIBRATION" or parent["sealed_at_ns"] is None:
                raise CalibrationError("parent must be a sealed CALIBRATION session")
            same_fields = (
                "evaluator_id", "evaluator_version", "evaluator_kind", "evaluator_config_hash",
                "reference_source_id", "reference_source_version", "reference_kind",
                "reference_independence", "score_semantics", "threshold_source",
            )
            candidate = {
                "evaluator_id": evaluator_id, "evaluator_version": evaluator_version,
                "evaluator_kind": evaluator_kind, "evaluator_config_hash": evaluator_config_hash,
                "reference_source_id": reference_source_id, "reference_source_version": reference_source_version,
                "reference_kind": reference_kind, "reference_independence": reference_independence,
                "score_semantics": score_semantics, "threshold_source": threshold_source,
            }
            mismatches = [f for f in same_fields if parent[f] != candidate[f]]
            if mismatches:
                raise CalibrationError("validation identity differs from calibration: " + ",".join(mismatches))
            if parent["cohort_hash"] == cohort_hash:
                raise CalibrationError("validation cohort must differ from calibration cohort")
            parent_threshold = parent["threshold_value"]
            if (parent_threshold is None) != (threshold_value is None) or (
                parent_threshold is not None and float(parent_threshold) != float(threshold_value)
            ):
                raise CalibrationError("validation threshold must be frozen from calibration")
        sid = session_id or uuid.uuid4().hex
        _nonempty("session_id", sid)
        self.db.execute(
            """INSERT INTO sessions VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (
                sid, phase, evaluator_id, evaluator_version, evaluator_kind, evaluator_config_hash,
                cohort_hash, expected_count, reference_source_id, reference_source_version,
                reference_kind, reference_independence, score_semantics,
                float(threshold_value) if threshold_value is not None else None, threshold_source,
                parent_calibration_id, _now_ns(), None,
            ),
        )
        self.db.commit()
        self._event("SESSION_CREATED", {"session_id": sid, "phase": phase, "evaluator_id": evaluator_id})
        return sid

    def record_observation(
        self,
        session_id: str,
        task_id: str,
        *,
        reference_label: str,
        evaluator_label: str,
        score: float | None,
        evidence_ref: str,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        session = self._open(session_id)
        _nonempty("task_id", task_id)
        _nonempty("evidence_ref", evidence_ref)
        if reference_label not in REFERENCE_LABELS:
            raise CalibrationError("reference_label must be PASS or FAIL")
        if evaluator_label not in EVALUATOR_LABELS:
            raise CalibrationError("invalid evaluator_label")
        if score is not None and not isinstance(score, (int, float)):
            raise CalibrationError("score must be numeric or null")
        if session["score_semantics"] == "NONE" and score is not None:
            raise CalibrationError("score forbidden when score_semantics=NONE")
        if session["score_semantics"] == "PROBABILITY_PASS" and score is not None and not (0.0 <= float(score) <= 1.0):
            raise CalibrationError("PROBABILITY_PASS score must lie in [0,1]")
        if metadata is not None:
            _reject_raw(metadata)
        metadata_hash = _sha256_json(metadata) if metadata is not None else None
        try:
            self.db.execute(
                "INSERT INTO observations VALUES(?,?,?,?,?,?,?)",
                (session_id, task_id, reference_label, evaluator_label, float(score) if score is not None else None, evidence_ref, metadata_hash),
            )
        except sqlite3.IntegrityError as exc:
            raise CalibrationError(f"duplicate observation: {task_id}") from exc
        self.db.commit()
        self._event("OBSERVATION_RECORDED", {"session_id": session_id, "task_id": task_id, "evaluator_label": evaluator_label})

    def seal_session(self, session_id: str) -> dict[str, Any]:
        session = self._open(session_id)
        n = self.db.execute("SELECT COUNT(*) n FROM observations WHERE session_id=?", (session_id,)).fetchone()["n"]
        if n > session["expected_count"]:
            raise CalibrationError("observed count exceeds expected_count")
        ts = _now_ns()
        self.db.execute("UPDATE sessions SET sealed_at_ns=? WHERE session_id=?", (ts, session_id))
        self.db.commit()
        self._event("SESSION_SEALED", {"session_id": session_id, "observed_count": n})
        return self.report(session_id)

    def report(self, session_id: str, *, confidence_level: float = 0.95, ece_bins: int = 10) -> dict[str, Any]:
        s = self._session(session_id)
        rows = list(self.db.execute("SELECT * FROM observations WHERE session_id=? ORDER BY task_id", (session_id,)))
        n = len(rows)
        answered = [r for r in rows if r["evaluator_label"] != "ABSTAIN"]
        tp = sum(r["reference_label"] == "PASS" and r["evaluator_label"] == "PASS" for r in answered)
        tn = sum(r["reference_label"] == "FAIL" and r["evaluator_label"] == "FAIL" for r in answered)
        fp = sum(r["reference_label"] == "FAIL" and r["evaluator_label"] == "PASS" for r in answered)
        fn = sum(r["reference_label"] == "PASS" and r["evaluator_label"] == "FAIL" for r in answered)
        correct = tp + tn
        answered_n = len(answered)
        acc = _safe_ratio(correct, answered_n)
        ci = wilson_interval(correct, answered_n, confidence_level) if answered_n else None
        tpr = _safe_ratio(tp, tp + fn)
        tnr = _safe_ratio(tn, tn + fp)
        precision = _safe_ratio(tp, tp + fp)
        balanced = None if tpr is None or tnr is None else (tpr + tnr) / 2.0
        prob_rows = [r for r in rows if r["score"] is not None]
        probability_count = len(prob_rows)
        probability_coverage = _safe_ratio(probability_count, n) if n else None
        bs = None
        ece = None
        if s["score_semantics"] == "PROBABILITY_PASS" and prob_rows:
            qs = [float(r["score"]) for r in prob_rows]
            ys = [1 if r["reference_label"] == "PASS" else 0 for r in prob_rows]
            bs = brier_score(qs, ys)
            ece = expected_calibration_error(qs, ys, ece_bins)
        receipt = {
            "schema": "amos.evaluator-calibration.report.v1",
            "session_id": session_id,
            "phase": s["phase"],
            "evaluator_id": s["evaluator_id"],
            "evaluator_version": s["evaluator_version"],
            "evaluator_kind": s["evaluator_kind"],
            "evaluator_config_hash": s["evaluator_config_hash"],
            "cohort_hash": s["cohort_hash"],
            "expected_count": s["expected_count"],
            "observed_count": n,
            "observed_coverage": n / s["expected_count"],
            "classification_count": answered_n,
            "classification_coverage": _safe_ratio(answered_n, n) if n else None,
            "abstention_rate": _safe_ratio(n - answered_n, n) if n else None,
            "confusion": {"tp": tp, "tn": tn, "fp": fp, "fn": fn},
            "selective_accuracy": acc,
            "accuracy_wilson_interval": None if ci is None else {"lower": ci[0], "upper": ci[1], "confidence_level": confidence_level},
            "sensitivity": tpr,
            "specificity": tnr,
            "precision": precision,
            "balanced_accuracy": balanced,
            "score_semantics": s["score_semantics"],
            "probability_count": probability_count,
            "probability_coverage": probability_coverage,
            "probability_complete": bool(n > 0 and probability_count == n),
            "brier_score": bs,
            "ece": ece,
            "ece_bins": ece_bins if s["score_semantics"] == "PROBABILITY_PASS" else None,
            "threshold_value": s["threshold_value"],
            "threshold_source": s["threshold_source"],
            "reference_source_id": s["reference_source_id"],
            "reference_source_version": s["reference_source_version"],
            "reference_kind": s["reference_kind"],
            "reference_independence": s["reference_independence"],
            "parent_calibration_id": s["parent_calibration_id"],
            "sealed": s["sealed_at_ns"] is not None,
            "reference_semantics": TRUTH_SEMANTICS,
            "calibration_semantics": CALIBRATION_SEMANTICS,
            "agreement_semantics": AGREEMENT_SEMANTICS,
            "probability_semantics": PROBABILITY_SEMANTICS,
            "authority_semantics": AUTHORITY_SEMANTICS,
            "deployment_semantics": DEPLOYMENT_SEMANTICS,
        }
        receipt["receipt_hash"] = _sha256_json(receipt)
        return receipt

    def reliability_gate(self, session_id: str, policy: dict[str, Any]) -> dict[str, Any]:
        _reject_raw(policy)
        s = self._session(session_id)
        report = self.report(session_id)
        allowed = {
            "min_observed_coverage", "min_classification_coverage", "min_selective_accuracy",
            "min_accuracy_ci_lower", "max_abstention_rate", "max_brier_score", "max_ece",
            "require_probability_complete", "require_independent_reference",
        }
        unknown = sorted(set(policy) - allowed)
        if unknown:
            raise CalibrationError("unsupported policy fields: " + ",".join(unknown))
        if s["phase"] != "VALIDATION" or s["sealed_at_ns"] is None:
            checks = [{"name": "held_out_validation", "state": "UNKNOWN", "reason": "sealed VALIDATION session required"}]
            verdict = "INCONCLUSIVE"
        else:
            checks: list[dict[str, Any]] = []
            def threshold_check(name: str, metric: float | None, bound: float, op: str) -> None:
                if not isinstance(bound, (int, float)) or not (0.0 <= float(bound) <= 1.0):
                    raise CalibrationError(f"{name} policy threshold must lie in [0,1]")
                if metric is None:
                    checks.append({"name": name, "state": "UNKNOWN", "observed": None, "required": bound})
                else:
                    ok = metric >= bound if op == ">=" else metric <= bound
                    checks.append({"name": name, "state": "PASS" if ok else "FAIL", "observed": metric, "required": bound})
            if "min_observed_coverage" in policy:
                threshold_check("min_observed_coverage", report["observed_coverage"], policy["min_observed_coverage"], ">=")
            if "min_classification_coverage" in policy:
                threshold_check("min_classification_coverage", report["classification_coverage"], policy["min_classification_coverage"], ">=")
            if "min_selective_accuracy" in policy:
                threshold_check("min_selective_accuracy", report["selective_accuracy"], policy["min_selective_accuracy"], ">=")
            if "min_accuracy_ci_lower" in policy:
                lower = None if report["accuracy_wilson_interval"] is None else report["accuracy_wilson_interval"]["lower"]
                threshold_check("min_accuracy_ci_lower", lower, policy["min_accuracy_ci_lower"], ">=")
            if "max_abstention_rate" in policy:
                threshold_check("max_abstention_rate", report["abstention_rate"], policy["max_abstention_rate"], "<=")
            if "max_brier_score" in policy:
                threshold_check("max_brier_score", report["brier_score"], policy["max_brier_score"], "<=")
            if "max_ece" in policy:
                threshold_check("max_ece", report["ece"], policy["max_ece"], "<=")
            if policy.get("require_probability_complete"):
                checks.append({"name": "require_probability_complete", "state": "PASS" if report["probability_complete"] else "FAIL", "observed": report["probability_complete"], "required": True})
            if policy.get("require_independent_reference"):
                checks.append({"name": "require_independent_reference", "state": "PASS" if report["reference_independence"] == "INDEPENDENT" else "FAIL", "observed": report["reference_independence"], "required": "INDEPENDENT"})
            states = {c["state"] for c in checks}
            verdict = "FAIL" if "FAIL" in states else ("INCONCLUSIVE" if "UNKNOWN" in states else "PASS")
        result = {
            "schema": "amos.evaluator-calibration.gate.v1",
            "session_id": session_id,
            "verdict": verdict,
            "checks": checks,
            "policy_hash": _sha256_json(policy),
            "reference_semantics": TRUTH_SEMANTICS,
            "calibration_semantics": CALIBRATION_SEMANTICS,
            "authority_semantics": AUTHORITY_SEMANTICS,
            "deployment_semantics": DEPLOYMENT_SEMANTICS,
        }
        result["receipt_hash"] = _sha256_json(result)
        return result

    def compare_drift(self, baseline_session_id: str, candidate_session_id: str) -> dict[str, Any]:
        b = self._session(baseline_session_id)
        c = self._session(candidate_session_id)
        reasons: list[str] = []
        for f in (
            "phase", "evaluator_id", "cohort_hash", "expected_count", "reference_source_id",
            "reference_source_version", "reference_kind", "reference_independence", "score_semantics",
            "threshold_value", "threshold_source",
        ):
            if b[f] != c[f]:
                reasons.append(f"{f} mismatch")
        if b["phase"] != "VALIDATION" or c["phase"] != "VALIDATION":
            reasons.append("both sessions must be VALIDATION")
        if b["sealed_at_ns"] is None or c["sealed_at_ns"] is None:
            reasons.append("both sessions must be sealed")
        b_rows = {r["task_id"]: r for r in self.db.execute("SELECT * FROM observations WHERE session_id=?", (baseline_session_id,))}
        c_rows = {r["task_id"]: r for r in self.db.execute("SELECT * FROM observations WHERE session_id=?", (candidate_session_id,))}
        if set(b_rows) != set(c_rows):
            reasons.append("observed task set mismatch")
        state = "NOT_COMPARABLE" if reasons else "COMPARABLE"
        rb = self.report(baseline_session_id)
        rc = self.report(candidate_session_id)
        def delta(key: str) -> float | None:
            x, y = rb.get(key), rc.get(key)
            return None if x is None or y is None else float(y) - float(x)
        changes = []
        if state == "COMPARABLE":
            changes = sorted(t for t in b_rows if b_rows[t]["evaluator_label"] != c_rows[t]["evaluator_label"])
        result = {
            "schema": "amos.evaluator-calibration.drift.v1",
            "baseline_session_id": baseline_session_id,
            "candidate_session_id": candidate_session_id,
            "state": state,
            "reasons": reasons,
            "baseline_evaluator_version": b["evaluator_version"],
            "candidate_evaluator_version": c["evaluator_version"],
            "baseline_config_hash": b["evaluator_config_hash"],
            "candidate_config_hash": c["evaluator_config_hash"],
            "delta_selective_accuracy": delta("selective_accuracy") if state == "COMPARABLE" else None,
            "delta_classification_coverage": delta("classification_coverage") if state == "COMPARABLE" else None,
            "delta_abstention_rate": delta("abstention_rate") if state == "COMPARABLE" else None,
            "delta_brier_score": delta("brier_score") if state == "COMPARABLE" else None,
            "delta_ece": delta("ece") if state == "COMPARABLE" else None,
            "prediction_change_task_ids": changes,
            "causal_semantics": CAUSAL_SEMANTICS,
            "agreement_semantics": AGREEMENT_SEMANTICS,
            "authority_semantics": AUTHORITY_SEMANTICS,
        }
        result["receipt_hash"] = _sha256_json(result)
        return result

    def verify_ledger(self) -> bool:
        prev = "0" * 64
        for row in self.db.execute("SELECT * FROM ledger ORDER BY seq"):
            expected = _ledger_hash(prev, row["event_type"], row["payload_json"], row["ts_ns"])
            if row["prev_hash"] != prev or row["event_hash"] != expected:
                return False
            prev = row["event_hash"]
        return True


def _self_test() -> None:
    rt = CalibrationRuntime()
    cfg = "a" * 64
    cal = rt.create_session(
        phase="CALIBRATION", evaluator_id="judge", evaluator_version="1", evaluator_kind="MODEL_JUDGE",
        evaluator_config_hash=cfg, cohort_hash="b" * 64, expected_count=2,
        reference_source_id="human-panel", reference_source_version="1", reference_kind="HUMAN",
        reference_independence="INDEPENDENT", score_semantics="PROBABILITY_PASS",
        threshold_value=0.5, threshold_source="CALIBRATION_DERIVED",
    )
    rt.record_observation(cal, "a", reference_label="PASS", evaluator_label="PASS", score=0.9, evidence_ref="e:a")
    rt.record_observation(cal, "b", reference_label="FAIL", evaluator_label="FAIL", score=0.1, evidence_ref="e:b")
    rt.seal_session(cal)
    val = rt.create_session(
        phase="VALIDATION", evaluator_id="judge", evaluator_version="1", evaluator_kind="MODEL_JUDGE",
        evaluator_config_hash=cfg, cohort_hash="c" * 64, expected_count=2,
        reference_source_id="human-panel", reference_source_version="1", reference_kind="HUMAN",
        reference_independence="INDEPENDENT", score_semantics="PROBABILITY_PASS",
        threshold_value=0.5, threshold_source="CALIBRATION_DERIVED", parent_calibration_id=cal,
    )
    rt.record_observation(val, "c", reference_label="PASS", evaluator_label="PASS", score=0.8, evidence_ref="e:c")
    rt.record_observation(val, "d", reference_label="FAIL", evaluator_label="FAIL", score=0.2, evidence_ref="e:d")
    rt.seal_session(val)
    gate = rt.reliability_gate(val, {"min_observed_coverage": 1.0, "min_selective_accuracy": 0.5, "require_independent_reference": True})
    assert gate["verdict"] == "PASS"
    assert rt.verify_ledger()
    print("evaluator_calibration self-test: PASS")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        _self_test()
