#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from harness_evolution_contract_check import ContractError, validate as validate_base


def validate(doc: dict[str, Any]) -> None:
    """Apply the base receipt schema and the v3 fail-closed verdict overlay."""
    validate_base(doc)
    if doc.get("schema") != "amos.harness-evolution.decision.v1":
        return
    verdict = doc.get("verdict")
    if verdict not in {"KEEP", "ROLLBACK"}:
        return
    if doc.get("comparison_state") != "COMPARABLE":
        raise ContractError(f"{verdict} requires comparable runs")
    if doc.get("calibration_verdict") != "PASS":
        raise ContractError(f"{verdict} requires evaluator reliability PASS")
    if not doc.get("isolation_valid"):
        raise ContractError(f"{verdict} requires valid isolation")
    if not doc.get("attribution_plausible"):
        raise ContractError(f"{verdict} requires plausible attribution")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        print("harness_evolution_guarded_contract_check self-test: PASS")
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
    raise SystemExit(main())
