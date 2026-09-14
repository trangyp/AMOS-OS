#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

HEX64 = re.compile(r"^[0-9a-f]{64}$")
ARCHETYPES = {"CONTRACT", "INTERVENTION", "PROCESS", "OUTCOME_PROPERTY"}
COMPARISON_STATES = {"COMPARABLE", "NOT_COMPARABLE"}
MUTATION_VERDICTS = {"KEEP", "ROLLBACK", "INCONCLUSIVE"}
FORBIDDEN = {
    "prompt", "completion", "raw_input", "raw_output", "input_value", "output_value",
    "tool_output", "chain_of_thought", "reasoning", "authorization", "api_key", "token", "password",
}


def _hash_ok(value: Any) -> bool:
    return bool(HEX64.fullmatch(str(value or "")))


def _forbidden_paths(value: Any, path: str = "$") -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if str(key).lower() in FORBIDDEN:
                found.append(child_path)
            found.extend(_forbidden_paths(child, child_path))
    elif isinstance(value, list):
        for i, child in enumerate(value):
            found.extend(_forbidden_paths(child, f"{path}[{i}]")
    return found


def _required(obj: dict[str, Any], names: tuple[str, ...], errors: list[str]) -> None:
    for name in names:
        if name not in obj:
            errors.append(f"missing {name}")


def validate_run_receipt(obj: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    _required(
        obj,
        (
            "run_id", "suite_id", "target_id", "target_version", "environment_id", "harness_id",
            "harness_version", "evaluator_set_id", "evaluator_version", "model_id", "model_config_hash",
            "budget_id", "task_cohort_hash", "evidence_archetype", "expected_task_count", "observed_task_count",
            "coverage_complete", "judgment_count", "review_count", "competing_judgment_sets", "sealed",
            "authority_semantics", "judge_semantics", "review_semantics", "receipt_hash",
        ),
        errors,
    )
    if obj.get("evidence_archetype") not in ARCHETYPES:
        errors.append("invalid evidence_archetype")
    if obj.get("authority_semantics") != "EVALUATION_DOES_NOT_GRANT_AUTHORITY":
        errors.append("evaluation receipt cannot grant authority")
    if obj.get("judge_semantics") != "JUDGE_OUTPUT_IS_EVIDENCE_NOT_GROUND_TRUTH":
        errors.append("judge output must remain evidence, not ground truth")
    if obj.get("review_semantics") != "REVIEW_DECISION_IS_NOT_RUNTIME_AUTHORITY":
        errors.append("review decision cannot become runtime authority")
    for name in ("model_config_hash", "task_cohort_hash", "receipt_hash"):
        if not _hash_ok(obj.get(name)):
            errors.append(f"{name} must be 64 lowercase hex chars")
    rr = obj.get("roundtrip_receipt_hash")
    if rr is not None and not _hash_ok(rr):
        errors.append("roundtrip_receipt_hash must be null or 64 lowercase hex chars")
    for name in ("expected_task_count", "observed_task_count", "judgment_count", "review_count"):
        if not isinstance(obj.get(name), int) or obj.get(name, -1) < 0:
            errors.append(f"{name} must be non-negative integer")
    if isinstance(obj.get("expected_task_count"), int) and isinstance(obj.get("observed_task_count"), int):
        expected = obj["expected_task_count"]
        observed = obj["observed_task_count"]
        if observed > expected:
            errors.append("observed_task_count cannot exceed expected_task_count")
        if obj.get("coverage_complete") is True and observed != expected:
            errors.append("coverage_complete requires observed == expected")
        if obj.get("coverage_complete") is False and observed == expected:
            errors.append("coverage_complete=false conflicts with complete count")
    if obj.get("sealed") is not True:
        errors.append("reliable run receipt must be sealed")
    if not isinstance(obj.get("competing_judgment_sets"), list):
        errors.append("competing_judgment_sets must be list")
    return errors


def validate_comparison_receipt(obj: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    _required(
        obj,
        (
            "comparison_id", "baseline_run_id", "candidate_run_id", "state", "reasons", "fixed_task_ids",
            "regressed_task_ids", "unchanged_task_ids", "critical_regression_task_ids", "causal_semantics",
            "authority_semantics", "receipt_hash",
        ),
        errors,
    )
    if obj.get("state") not in COMPARISON_STATES:
        errors.append("invalid comparison state")
    for name in ("reasons", "fixed_task_ids", "regressed_task_ids", "unchanged_task_ids", "critical_regression_task_ids"):
        if not isinstance(obj.get(name), list):
            errors.append(f"{name} must be list")
    if obj.get("state") == "COMPARABLE" and obj.get("reasons"):
        errors.append("COMPARABLE receipt cannot contain incompatibility reasons")
    if obj.get("state") == "NOT_COMPARABLE":
        if not obj.get("reasons"):
            errors.append("NOT_COMPARABLE requires reasons")
        for name in ("fixed_task_ids", "regressed_task_ids", "critical_regression_task_ids"):
            if obj.get(name):
                errors.append("NOT_COMPARABLE cannot carry performance deltas")
                break
    if obj.get("causal_semantics") != "SCORE_DELTA_DOES_NOT_PROVE_CAUSAL_ATTRIBUTION":
        errors.append("comparison cannot claim causal attribution")
    if obj.get("authority_semantics") != "EVALUATION_DOES_NOT_GRANT_AUTHORITY":
        errors.append("comparison cannot grant authority")
    if not _hash_ok(obj.get("receipt_hash")):
        errors.append("receipt_hash must be 64 lowercase hex chars")
    return errors


def validate_mutation_receipt(obj: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    _required(
        obj,
        (
            "comparison_id", "verdict", "predicted_fix_ids", "predicted_regression_ids", "observed_fixed_ids",
            "observed_regressed_ids", "critical_regression_ids", "fix_precision", "regression_recall",
            "attribution_plausible", "authority_semantics", "causal_semantics", "receipt_hash",
        ),
        errors,
    )
    if obj.get("verdict") not in MUTATION_VERDICTS:
        errors.append("invalid mutation verdict")
    for name in ("predicted_fix_ids", "predicted_regression_ids", "observed_fixed_ids", "observed_regressed_ids", "critical_regression_ids"):
        if not isinstance(obj.get(name), list):
            errors.append(f"{name} must be list")
    for name in ("fix_precision", "regression_recall"):
        value = obj.get(name)
        if not isinstance(value, (int, float)) or not 0 <= float(value) <= 1:
            errors.append(f"{name} must be in [0,1]")
    if obj.get("verdict") == "KEEP":
        if obj.get("attribution_plausible") is not True:
            errors.append("KEEP requires attribution_plausible=true")
        if obj.get("critical_regression_ids"):
            errors.append("KEEP cannot contain critical regressions")
        if not obj.get("observed_fixed_ids"):
            errors.append("KEEP requires at least one observed fix")
        if len(obj.get("observed_regressed_ids", [])) >= len(obj.get("observed_fixed_ids", [])):
            errors.append("KEEP requires more fixes than regressions")
    if obj.get("authority_semantics") != "EVALUATION_DOES_NOT_GRANT_AUTHORITY":
        errors.append("mutation verdict cannot grant authority")
    if obj.get("causal_semantics") != "SCORE_DELTA_DOES_NOT_PROVE_CAUSAL_ATTRIBUTION":
        errors.append("mutation verdict cannot claim causal proof")
    if not _hash_ok(obj.get("receipt_hash")):
        errors.append("receipt_hash must be 64 lowercase hex chars")
    return errors


def validate(obj: dict[str, Any]) -> list[str]:
    errors = [f"receipt contains forbidden persisted field: {p}" for p in _forbidden_paths(obj)]
    if "run_id" in obj and "expected_task_count" in obj:
        errors.extend(validate_run_receipt(obj))
    elif "state" in obj and "baseline_run_id" in obj:
        errors.extend(validate_comparison_receipt(obj))
    elif "verdict" in obj and "observed_fixed_ids" in obj:
        errors.extend(validate_mutation_receipt(obj))
    else:
        errors.append("unknown evaluation receipt type")
    return errors


def self_test() -> int:
    run = {
        "run_id": "r", "suite_id": "s", "target_id": "t", "target_version": "v", "environment_id": "e",
        "harness_id": "h", "harness_version": "1", "evaluator_set_id": "es", "evaluator_version": "1",
        "model_id": "m", "model_config_hash": "a" * 64, "budget_id": "b", "task_cohort_hash": "b" * 64,
        "evidence_archetype": "PROCESS", "trace_id": None, "roundtrip_receipt_hash": None,
        "expected_task_count": 2, "observed_task_count": 2, "coverage_complete": True, "judgment_count": 0,
        "review_count": 0, "competing_judgment_sets": [], "sealed": True,
        "authority_semantics": "EVALUATION_DOES_NOT_GRANT_AUTHORITY",
        "judge_semantics": "JUDGE_OUTPUT_IS_EVIDENCE_NOT_GROUND_TRUTH",
        "review_semantics": "REVIEW_DECISION_IS_NOT_RUNTIME_AUTHORITY", "receipt_hash": "c" * 64,
    }
    comparison = {
        "comparison_id": "c", "baseline_run_id": "b", "candidate_run_id": "n", "state": "COMPARABLE",
        "reasons": [], "fixed_task_ids": ["t1"], "regressed_task_ids": [], "unchanged_task_ids": ["t2"],
        "critical_regression_task_ids": [], "causal_semantics": "SCORE_DELTA_DOES_NOT_PROVE_CAUSAL_ATTRIBUTION",
        "authority_semantics": "EVALUATION_DOES_NOT_GRANT_AUTHORITY", "receipt_hash": "d" * 64,
    }
    mutation = {
        "comparison_id": "c", "verdict": "KEEP", "predicted_fix_ids": ["t1"], "predicted_regression_ids": [],
        "observed_fixed_ids": ["t1"], "observed_regressed_ids": [], "critical_regression_ids": [],
        "fix_precision": 1.0, "regression_recall": 1.0, "attribution_plausible": True,
        "authority_semantics": "EVALUATION_DOES_NOT_GRANT_AUTHORITY",
        "causal_semantics": "SCORE_DELTA_DOES_NOT_PROVE_CAUSAL_ATTRIBUTION", "receipt_hash": "e" * 64,
    }
    if validate(run) or validate(comparison) or validate(mutation):
        print("positive fixture failed", file=sys.stderr)
        return 1
    bad = dict(run); bad["prompt"] = "secret"
    if not validate(bad):
        print("raw-content negative fixture failed", file=sys.stderr)
        return 1
    bad2 = dict(mutation); bad2["attribution_plausible"] = False
    if not validate(bad2):
        print("authority/attribution negative fixture failed", file=sys.stderr)
        return 1
    print("SELF_TEST_PASS")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate AMOS interactive-evaluation receipts")
    ap.add_argument("path", nargs="?")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if not args.path:
        ap.error("receipt path required unless --self-test")
    try:
        obj = json.loads(Path(args.path).read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"invalid receipt JSON: {exc}", file=sys.stderr)
        return 2
    errors = validate(obj)
    for error in errors:
        print("ERROR", error)
    print(f"EVALUATION_CONTRACT errors={len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
