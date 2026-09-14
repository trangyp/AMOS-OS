#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


def load_runtime(repo: Path | None = None):
    local = Path(__file__).resolve().with_name("agent_trace_runtime.py")
    candidates = [local]
    if repo is not None:
        candidates.append(repo / "17_OBSERVABILITY" / "agent_trace_runtime.py")
    path = next((candidate for candidate in candidates if candidate.exists()), None)
    if path is None:
        raise RuntimeError("trace runtime not found in Skill bundle or repository observability plane")
    spec = importlib.util.spec_from_file_location("amos_trace_contract_runtime", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def validate_file(path: Path, repo: Path | None = None) -> str:
    mod = load_runtime(repo)
    data = json.loads(path.read_text(encoding="utf-8"))
    env = mod.TraceEnvelope.from_dict(data)
    env.validate()
    coverage = env.coverage_ratio()
    coverage_text = "UNKNOWN" if coverage is None else f"{coverage:.6f}"
    return (
        "TRACE_CONTRACT_PASS "
        f"receipt_sha256={env.receipt_sha256()} "
        f"missingness={env.missingness_state()} coverage={coverage_text}"
    )


def self_test(repo: Path | None = None) -> int:
    mod = load_runtime(repo)
    trace_id = "1" * 32
    root_id = "2" * 16
    tool_id = "3" * 16
    valid = {
        "trace_id": trace_id,
        "expected_span_count": 2,
        "spans": [
            {
                "trace_id": trace_id,
                "span_id": root_id,
                "parent_span_id": None,
                "name": "root",
                "kind": "WORKFLOW",
                "start_time_ns": 1,
                "end_time_ns": 10,
                "status": "OK",
                "attributes": {"amos.workflow.id": "wf-self-test"},
            },
            {
                "trace_id": trace_id,
                "span_id": tool_id,
                "parent_span_id": root_id,
                "name": "execute_tool fixture",
                "kind": "TOOL",
                "start_time_ns": 2,
                "end_time_ns": 5,
                "status": "OK",
                "attributes": {"gen_ai.operation.name": "execute_tool"},
            },
        ],
    }
    env = mod.TraceEnvelope.from_dict(valid)
    env.validate()
    if env.missingness_state() != "COMPLETE":
        print("SELF_TEST_FAIL: valid fixture missingness", file=sys.stderr)
        return 1

    invalid = json.loads(json.dumps(valid))
    invalid["spans"][1]["kind"] = "EFFECT"
    invalid["spans"][1]["effect_state"] = "COMMITTED"
    invalid["spans"][1]["effect_id"] = "effect-fixture"
    try:
        mod.TraceEnvelope.from_dict(invalid).validate()
    except mod.TraceContractError:
        pass
    else:
        print("SELF_TEST_FAIL: authority-less committed effect admitted", file=sys.stderr)
        return 1

    if not mod.entropy_delta_bits([0.5, 0.5], [0.9, 0.1]) < 0.0:
        print("SELF_TEST_FAIL: entropy delta sign assumption", file=sys.stderr)
        return 1

    print("SELF_TEST_PASS")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate an AMOS agent trace contract document")
    ap.add_argument("trace", nargs="?", help="trace JSON file")
    ap.add_argument("--repo", default=None, help="optional AMOS repository root")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    repo = Path(args.repo).resolve() if args.repo else None
    try:
        if args.self_test:
            return self_test(repo)
        if not args.trace:
            ap.error("trace path is required unless --self-test is used")
        print(validate_file(Path(args.trace).resolve(), repo))
        return 0
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"TRACE_CONTRACT_FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
