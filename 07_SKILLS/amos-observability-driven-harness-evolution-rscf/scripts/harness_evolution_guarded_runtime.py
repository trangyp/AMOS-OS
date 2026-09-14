#!/usr/bin/env python3
from __future__ import annotations

import json
from typing import Any

from harness_evolution_runtime import (
    AUTHORITY_SEMANTICS,
    CAUSAL_SEMANTICS,
    EVALUATOR_SEMANTICS,
    ROLLBACK_SEMANTICS,
    HarnessEvolutionError,
    HarnessEvolutionRuntime,
    _canonical_json,
    _sha256_json,
    _validate_receipt_hash,
)


class GuardedHarnessEvolutionRuntime(HarnessEvolutionRuntime):
    """Fail-closed verdict overlay for the v3 harness-evolution evidence store.

    The base runtime owns identity, inventory, mutation, isolation, evidence binding,
    reconciliation, and ledger state. This overlay owns verdict admission. It exists
    so KEEP and ROLLBACK are both unavailable when comparison, calibration,
    isolation, or attribution evidence is unusable.
    """

    def decision(
        self,
        mutation_id: str,
        *,
        comparison_receipt: dict[str, Any],
        calibration_gate_receipt: dict[str, Any],
    ) -> dict[str, Any]:
        mutation = self._require_state(mutation_id, "EVALUATED")
        _validate_receipt_hash(comparison_receipt)
        _validate_receipt_hash(
            calibration_gate_receipt,
            schema="amos.evaluator-calibration.gate.v1",
        )
        binding = self.db.execute(
            "SELECT * FROM evaluation_bindings WHERE mutation_id=?",
            (mutation_id,),
        ).fetchone()
        if binding is None:
            raise HarnessEvolutionError("evaluation binding missing")
        if comparison_receipt["receipt_hash"] != binding["comparison_hash"]:
            raise HarnessEvolutionError("comparison receipt differs from bound evidence")
        if calibration_gate_receipt["receipt_hash"] != binding["calibration_gate_hash"]:
            raise HarnessEvolutionError("calibration gate differs from bound evidence")

        isolation = self.isolation_receipt(mutation_id)
        evidence_reasons: list[str] = []
        if binding["comparison_state"] != "COMPARABLE":
            evidence_reasons.append("evaluation runs are not comparable")
        if binding["calibration_verdict"] != "PASS":
            evidence_reasons.append("evaluator reliability gate is not PASS")
        if not isolation["isolation_valid"]:
            evidence_reasons.append("evaluation isolation evidence is invalid")
        if not binding["attribution_plausible"]:
            evidence_reasons.append("attribution not plausible under frozen-axis evidence")

        # For usable evidence the base runtime's KEEP/ROLLBACK arithmetic is valid.
        if not evidence_reasons:
            return super().decision(
                mutation_id,
                comparison_receipt=comparison_receipt,
                calibration_gate_receipt=calibration_gate_receipt,
            )

        # Fail closed before the base method can convert a critical regression from
        # contaminated/incomparable/unreliable evidence into ROLLBACK_RECOMMENDED.
        fixed = sorted(set(comparison_receipt.get("fixed_task_ids", [])))
        regressed = sorted(set(comparison_receipt.get("regressed_task_ids", [])))
        critical = sorted(set(comparison_receipt.get("critical_regression_task_ids", [])))
        predicted_fix = set(json.loads(mutation["predicted_fix_json"]))
        predicted_reg = set(json.loads(mutation["predicted_regression_json"]))
        fixed_set = set(fixed)
        regressed_set = set(regressed)
        fix_precision = len(predicted_fix & fixed_set) / max(1, len(predicted_fix))
        regression_recall = (
            1.0
            if not regressed_set
            else len(predicted_reg & regressed_set) / len(regressed_set)
        )
        result = {
            "schema": "amos.harness-evolution.decision.v1",
            "mutation_id": mutation_id,
            "verdict": "INCONCLUSIVE",
            "reasons": evidence_reasons,
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
                mutation_id,
                "INCONCLUSIVE",
                _canonical_json(evidence_reasons),
                _canonical_json(fixed),
                _canonical_json(regressed),
                _canonical_json(critical),
                fix_precision,
                regression_recall,
                result["receipt_hash"],
            ),
        )
        self.db.execute(
            "UPDATE mutations SET state='INCONCLUSIVE' WHERE mutation_id=?",
            (mutation_id,),
        )
        self.db.commit()
        self._event(
            "DECISION_RECORDED",
            {"mutation_id": mutation_id, "verdict": "INCONCLUSIVE"},
        )
        return result
