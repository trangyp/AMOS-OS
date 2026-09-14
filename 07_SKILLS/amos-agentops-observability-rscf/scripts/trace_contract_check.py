#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HEX64 = re.compile(r"^[0-9a-f]{64}$")
ALLOWED_STATUS = {"OBSERVED", "INCOMPLETE", "IN_DOUBT"}
FORBIDDEN_CONTENT_KEYS = {"input_value", "output_value", "prompt", "completion", "raw_input", "raw_output"}


def validate(obj: dict) -> list[str]:
    errors = []
    for key in ("trace_id", "span_count", "coverage_complete", "effect_states", "status", "authority_semantics", "causal_semantics", "receipt_hash"):
        if key not in obj:
            errors.append(f"missing {key}")
    if obj.get("status") not in ALLOWED_STATUS:
        errors.append("invalid status")
    if obj.get("authority_semantics") != "OBSERVED_REFERENCE_ONLY":
        errors.append("telemetry must not claim authority")
    if obj.get("causal_semantics") != "TRACE_EDGE_IS_NOT_CAUSAL_PROOF":
        errors.append("trace must not claim causal proof")
    if not isinstance(obj.get("coverage_complete"), bool):
        errors.append("coverage_complete must be boolean")
    if not isinstance(obj.get("span_count"), int) or obj.get("span_count", 0) < 1:
        errors.append("span_count must be positive integer")
    if not isinstance(obj.get("effect_states"), list):
        errors.append("effect_states must be list")
    if obj.get("status") == "IN_DOUBT" and "IN_DOUBT" not in obj.get("effect_states", []):
        errors.append("IN_DOUBT receipt requires IN_DOUBT effect state")
    if not HEX64.fullmatch(str(obj.get("receipt_hash", ""))):
        errors.append("receipt_hash must be 64 lowercase hex chars")
    forbidden = sorted(FORBIDDEN_CONTENT_KEYS.intersection(obj.keys()))
    if forbidden:
        errors.append("receipt contains raw content fields: " + ",".join(forbidden))
    return errors


def self_test() -> int:
    good = {
        "trace_id":"t", "span_count":1, "coverage_complete":True,
        "effect_states":[], "status":"OBSERVED",
        "authority_semantics":"OBSERVED_REFERENCE_ONLY",
        "causal_semantics":"TRACE_EDGE_IS_NOT_CAUSAL_PROOF",
        "receipt_hash":"a"*64,
    }
    if validate(good):
        print("positive fixture failed", file=sys.stderr); return 1
    bad = dict(good); bad["authority_semantics"] = "AUTHORIZED"; bad["prompt"] = "secret"
    e = validate(bad)
    if not any("authority" in x for x in e) or not any("raw content" in x for x in e):
        print("negative fixture failed", file=sys.stderr); return 1
    print("SELF_TEST_PASS")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if not args.path:
        print("receipt path required", file=sys.stderr); return 2
    try:
        obj = json.loads(Path(args.path).read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"invalid receipt: {exc}", file=sys.stderr); return 2
    errors = validate(obj)
    for e in errors: print("ERROR", e)
    print(f"TRACE_CONTRACT errors={len(errors)}")
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
