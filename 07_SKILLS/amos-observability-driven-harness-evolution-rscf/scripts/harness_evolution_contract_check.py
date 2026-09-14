#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

FORBIDDEN = {
    "prompt", "completion", "raw_input", "raw_output", "input_value", "output_value",
    "tool_output", "chain_of_thought", "reasoning", "authorization", "api_key",
    "token", "password", "secret", "credential",
}
AUTHORITY = "HARNESS_EVOLUTION_RECOMMENDATION_DOES_NOT_GRANT_WRITE_OR_MERGE_AUTHORITY"
CAUSAL = "NEXT_ROUND_DELTA_DOES_NOT_PROVE_CAUSAL_ATTRIBUTION"
ROLLBACK = "ROLLBACK_RECOMMENDATION_DOES_NOT_EXECUTE_ROLLBACK"
EVALUATOR = "EVALUATOR_RELIABILITY_PASS_DOES_NOT_IMPLY_GROUND_TRUTH"


class ContractError(RuntimeError):
    pass


def canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha(value: Any) -> str:
    return hashlib.sha256(canonical(value).encode("utf-8")).hexdigest()


def reject_raw(value: Any, path: str = "$") -> None:
    if isinstance(value, dict):
        for k, v in value.items():
            if str(k).lower() in FORBIDDEN:
                raise ContractError(f"forbidden durable field: {path}.{k}")
            reject_raw(v, f"{path}.{k}")
    elif isinstance(value, list):
        for i, v in enumerate(value):
            reject_raw(v, f"{path}[{i}]")


def hash64(name: str, value: Any) -> None:
    if not isinstance(value, str) or len(value) != 64 or any(c not in "0123456789abcdef" for c in value):
        raise ContractError(f"{name} must be 64 lowercase hex chars")


def check_hash(doc: dict[str, Any]) -> None:
    hash64("receipt_hash", doc.get("receipt_hash"))
    body = dict(doc)
    got = body.pop("receipt_hash")
    if sha(body) != got:
        raise ContractError("receipt_hash mismatch")


def validate_mutation(doc: dict[str, Any]) -> None:
    if doc.get("schema") != "amos.harness-evolution.mutation.v1":
        raise ContractError("wrong mutation schema")
    if doc.get("authority_semantics") != AUTHORITY or doc.get("causal_semantics") != CAUSAL:
        raise ContractError("mutation semantics mismatch")
    if doc.get("state") not in {"PROPOSED", "STAGED", "EVALUATED", "KEEP_RECOMMENDED", "ROLLBACK_RECOMMENDED", "INCONCLUSIVE", "RECONCILED"}:
        raise ContractError("invalid mutation state")
    fixes = set(doc.get("predicted_fix_ids", []))
    regs = set(doc.get("predicted_regression_ids", []))
    if fixes & regs:
        raise ContractError("prediction sets overlap")
    changes = doc.get("changes")
    if not isinstance(changes, list):
        raise ContractError("changes must be list")
    seen: set[str] = set()
    classes: set[str] = set()
    for c in changes:
        path = c.get("file_path")
        if not isinstance(path, str) or not path:
            raise ContractError("change path missing")
        if path in seen:
            raise ContractError("duplicate change path")
        seen.add(path)
        classes.add(c.get("component_class"))
        for key in ("before_hash", "after_hash", "rollback_hash"):
            hash64(key, c.get(key))
        if c["before_hash"] == c["after_hash"]:
            raise ContractError("no-op change")
        if c["rollback_hash"] != c["before_hash"]:
            raise ContractError("rollback hash mismatch")
    if len(classes) > 1 and doc.get("attribution_mode") != "COUPLED_SET":
        raise ContractError("cross-component mutation must be coupled")
    if doc.get("attribution_mode") == "COUPLED_SET":
        hash64("coupling_reason_hash", doc.get("coupling_reason_hash"))
    check_hash(doc)


def validate_isolation(doc: dict[str, Any]) -> None:
    if doc.get("schema") != "amos.harness-evolution.isolation.v1":
        raise ContractError("wrong isolation schema")
    if doc.get("isolation_semantics") != "VERIFIER_OR_REWARD_LEAKAGE_INVALIDATES_COMPARATIVE_EVIDENCE":
        raise ContractError("isolation semantics mismatch")
    if doc.get("mode") not in {"SINGLE_STEP", "SEPARATE_VERIFIER", "SHARED_VERIFIER"}:
        raise ContractError("invalid isolation mode")
    hash64("evidence_hash", doc.get("evidence_hash"))
    computed = bool(doc.get("prior_tests_hidden") and doc.get("prior_reward_hidden") and doc.get("agent_owned_state_preserved"))
    if doc.get("mode") == "SHARED_VERIFIER" and doc.get("prior_shared_verifier_state"):
        computed = computed and bool(doc.get("sanitized_before_agent"))
    if bool(doc.get("isolation_valid")) != computed:
        raise ContractError("isolation_valid inconsistent with evidence")
    check_hash(doc)


def validate_decision(doc: dict[str, Any]) -> None:
    if doc.get("schema") != "amos.harness-evolution.decision.v1":
        raise ContractError("wrong decision schema")
    if doc.get("authority_semantics") != AUTHORITY or doc.get("causal_semantics") != CAUSAL:
        raise ContractError("decision semantics mismatch")
    if doc.get("rollback_semantics") != ROLLBACK or doc.get("evaluator_semantics") != EVALUATOR:
        raise ContractError("decision boundary mismatch")
    verdict = doc.get("verdict")
    if verdict not in {"KEEP", "ROLLBACK", "INCONCLUSIVE"}:
        raise ContractError("invalid verdict")
    fixed = set(doc.get("fixed_task_ids", []))
    regressed = set(doc.get("regressed_task_ids", []))
    critical = set(doc.get("critical_regression_task_ids", []))
    if critical - regressed:
        raise ContractError("critical regressions must be subset of regressions")
    if verdict == "KEEP":
        if doc.get("comparison_state") != "COMPARABLE":
            raise ContractError("KEEP requires comparable runs")
        if doc.get("calibration_verdict") != "PASS":
            raise ContractError("KEEP requires evaluator reliability PASS")
        if not doc.get("isolation_valid"):
            raise ContractError("KEEP requires valid isolation")
        if not doc.get("attribution_plausible"):
            raise ContractError("KEEP requires plausible attribution")
        if critical or not fixed or len(fixed) <= len(regressed):
            raise ContractError("KEEP requires net improvement and no critical regression")
    if verdict == "ROLLBACK" and not (critical or len(regressed) > len(fixed)):
        raise ContractError("ROLLBACK requires bounded regression evidence")
    if not isinstance(doc.get("fix_precision"), (int, float)) or not 0.0 <= float(doc["fix_precision"]) <= 1.0:
        raise ContractError("fix_precision out of range")
    if not isinstance(doc.get("regression_recall"), (int, float)) or not 0.0 <= float(doc["regression_recall"]) <= 1.0:
        raise ContractError("regression_recall out of range")
    check_hash(doc)


def validate_reconciliation(doc: dict[str, Any]) -> None:
    if doc.get("schema") != "amos.harness-evolution.reconciliation.v1":
        raise ContractError("wrong reconciliation schema")
    if doc.get("authority_semantics") != AUTHORITY:
        raise ContractError("authority semantics mismatch")
    if doc.get("state") not in {"KEPT", "ROLLED_BACK", "NOT_APPLIED"}:
        raise ContractError("invalid reconciliation state")
    if not isinstance(doc.get("observed_version"), str) or not doc["observed_version"]:
        raise ContractError("observed_version missing")
    hashes = doc.get("observed_component_hashes")
    if not isinstance(hashes, dict) or not hashes:
        raise ContractError("observed_component_hashes required")
    for path, h in hashes.items():
        if not isinstance(path, str) or not path:
            raise ContractError("invalid component path")
        hash64(f"component hash {path}", h)
    hash64("evidence_hash", doc.get("evidence_hash"))
    check_hash(doc)


def validate(doc: dict[str, Any]) -> None:
    if not isinstance(doc, dict):
        raise ContractError("document must be object")
    reject_raw(doc)
    schema = doc.get("schema")
    if schema == "amos.harness-evolution.mutation.v1":
        validate_mutation(doc)
    elif schema == "amos.harness-evolution.isolation.v1":
        validate_isolation(doc)
    elif schema == "amos.harness-evolution.decision.v1":
        validate_decision(doc)
    elif schema == "amos.harness-evolution.reconciliation.v1":
        validate_reconciliation(doc)
    else:
        raise ContractError("unsupported schema")


def _self_test() -> None:
    body = {
        "schema": "amos.harness-evolution.decision.v1",
        "mutation_id": "m",
        "verdict": "KEEP",
        "reasons": ["bounded net improvement with no critical regression"],
        "fixed_task_ids": ["a"],
        "regressed_task_ids": [],
        "critical_regression_task_ids": [],
        "predicted_fix_ids": ["a"],
        "predicted_regression_ids": [],
        "fix_precision": 1.0,
        "regression_recall": 1.0,
        "comparison_state": "COMPARABLE",
        "calibration_verdict": "PASS",
        "isolation_valid": True,
        "attribution_plausible": True,
        "authority_semantics": AUTHORITY,
        "causal_semantics": CAUSAL,
        "rollback_semantics": ROLLBACK,
        "evaluator_semantics": EVALUATOR,
    }
    body["receipt_hash"] = sha(body)
    validate(body)
    bad = dict(body)
    bad["verdict"] = "AUTHORIZE"
    bad["receipt_hash"] = sha({k: v for k, v in bad.items() if k != "receipt_hash"})
    try:
        validate(bad)
    except ContractError:
        print("harness_evolution_contract_check self-test: PASS")
        return
    raise AssertionError("invalid decision accepted")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        _self_test()
        return 0
    if not args.path:
        parser.error("path is required unless --self-test is used")
    try:
        doc = json.loads(Path(args.path).read_text(encoding="utf-8"))
        validate(doc)
    except (OSError, json.JSONDecodeError, ContractError) as exc:
        print(f"FAIL: {exc}")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
