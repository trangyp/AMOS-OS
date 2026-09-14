#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

HEX64 = re.compile(r"^[0-9a-f]{64}$")
TRANSPORT_STATES = {
    "QUEUED", "SENDING", "ACKED", "PARTIAL", "RETRYABLE",
    "PERMANENT_FAILURE", "PROTOCOL_ERROR", "IN_DOUBT", "RECONCILED_PRESENT",
}
ROUNDTRIP_STATES = {"VERIFIED_ROUNDTRIP", "NOT_VERIFIED"}
FORBIDDEN_KEYS = {
    "input_value", "output_value", "prompt", "completion", "raw_input", "raw_output",
    "input.value", "output.value", "authorization", "api_key", "token", "password",
}


def _forbidden_paths(value: Any, path: str = "$") -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            key_text = str(key).lower()
            child_path = f"{path}.{key}"
            if key_text in FORBIDDEN_KEYS:
                found.append(child_path)
            found.extend(_forbidden_paths(child, child_path))
    elif isinstance(value, list):
        for i, child in enumerate(value):
            found.extend(_forbidden_paths(child, f"{path}[{i}]"))
    return found


def _hash_ok(value: Any) -> bool:
    return bool(HEX64.fullmatch(str(value or "")))


def validate_transport(obj: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = (
        "export_id", "trace_id", "run_id", "build_id", "payload_hash", "state",
        "attempt_count", "transport_semantics", "authority_semantics", "receipt_hash",
    )
    for key in required:
        if key not in obj:
            errors.append(f"missing {key}")
    if obj.get("state") not in TRANSPORT_STATES:
        errors.append("invalid transport state")
    if not all(str(obj.get(k, "")).strip() for k in ("export_id", "trace_id", "run_id", "build_id")):
        errors.append("transport identity fields must be non-empty")
    if not isinstance(obj.get("attempt_count"), int) or obj.get("attempt_count", -1) < 0:
        errors.append("attempt_count must be non-negative integer")
    if obj.get("transport_semantics") != "HTTP_ACK_IS_NOT_BACKEND_READBACK_VERIFICATION":
        errors.append("transport receipt must preserve ACK/readback distinction")
    if obj.get("authority_semantics") != "TRANSPORT_DOES_NOT_GRANT_AUTHORITY":
        errors.append("transport receipt must not claim authority")
    if obj.get("state") == "ACKED" and obj.get("last_http_status") != 200:
        errors.append("ACKED requires observed HTTP 200")
    if obj.get("state") == "RECONCILED_PRESENT" and obj.get("last_http_status") == 200:
        errors.append("RECONCILED_PRESENT must not masquerade as HTTP ACKED")
    if obj.get("status") == "VERIFIED_ROUNDTRIP" or obj.get("roundtrip_verified") is True:
        errors.append("transport receipt cannot self-promote to round-trip verification")
    if not _hash_ok(obj.get("payload_hash")):
        errors.append("payload_hash must be 64 lowercase hex chars")
    if not _hash_ok(obj.get("receipt_hash")):
        errors.append("receipt_hash must be 64 lowercase hex chars")
    return errors


def validate_roundtrip(obj: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = (
        "trace_id", "run_id", "build_id", "status", "expected_span_count",
        "observed_span_count", "missing_span_ids", "extra_span_ids", "duplicate_span_ids",
        "mismatches", "contamination", "authority_semantics", "causal_semantics", "receipt_hash",
    )
    for key in required:
        if key not in obj:
            errors.append(f"missing {key}")
    if obj.get("status") not in ROUNDTRIP_STATES:
        errors.append("invalid round-trip status")
    if not all(str(obj.get(k, "")).strip() for k in ("trace_id", "run_id", "build_id")):
        errors.append("round-trip identity fields must be non-empty")
    for key in ("expected_span_count", "observed_span_count"):
        if not isinstance(obj.get(key), int) or obj.get(key, -1) < 0:
            errors.append(f"{key} must be non-negative integer")
    for key in ("missing_span_ids", "extra_span_ids", "duplicate_span_ids", "mismatches", "contamination"):
        if not isinstance(obj.get(key), list):
            errors.append(f"{key} must be list")
    if obj.get("authority_semantics") != "ROUNDTRIP_EVIDENCE_DOES_NOT_GRANT_AUTHORITY":
        errors.append("round-trip evidence must not claim authority")
    if obj.get("causal_semantics") != "READBACK_MATCH_DOES_NOT_PROVE_CAUSALITY":
        errors.append("read-back match must not claim causal proof")
    if obj.get("status") == "VERIFIED_ROUNDTRIP":
        if obj.get("expected_span_count") != obj.get("observed_span_count"):
            errors.append("verified round-trip requires equal expected/observed span counts")
        for key in ("missing_span_ids", "extra_span_ids", "duplicate_span_ids", "mismatches", "contamination"):
            if obj.get(key):
                errors.append(f"verified round-trip cannot contain {key}")
    if not _hash_ok(obj.get("receipt_hash")):
        errors.append("receipt_hash must be 64 lowercase hex chars")
    return errors


def validate(obj: dict[str, Any]) -> list[str]:
    errors = _forbidden_paths(obj)
    errors = [f"receipt contains forbidden persisted field: {p}" for p in errors]
    if "export_id" in obj:
        errors.extend(validate_transport(obj))
    elif "expected_span_count" in obj or obj.get("status") in ROUNDTRIP_STATES:
        errors.extend(validate_roundtrip(obj))
    else:
        errors.append("unknown receipt type")
    return errors


def self_test() -> int:
    good_transport = {
        "export_id": "e", "trace_id": "t", "run_id": "r", "build_id": "b",
        "payload_hash": "a" * 64, "state": "ACKED", "attempt_count": 1,
        "last_http_status": 200, "ack_hash": "b" * 64, "partial_rejected_spans": 0,
        "transport_semantics": "HTTP_ACK_IS_NOT_BACKEND_READBACK_VERIFICATION",
        "authority_semantics": "TRANSPORT_DOES_NOT_GRANT_AUTHORITY", "receipt_hash": "c" * 64,
    }
    good_roundtrip = {
        "trace_id": "t", "run_id": "r", "build_id": "b", "status": "VERIFIED_ROUNDTRIP",
        "expected_span_count": 2, "observed_span_count": 2, "missing_span_ids": [],
        "extra_span_ids": [], "duplicate_span_ids": [], "mismatches": [], "contamination": [],
        "authority_semantics": "ROUNDTRIP_EVIDENCE_DOES_NOT_GRANT_AUTHORITY",
        "causal_semantics": "READBACK_MATCH_DOES_NOT_PROVE_CAUSALITY", "receipt_hash": "d" * 64,
    }
    if validate(good_transport) or validate(good_roundtrip):
        print("positive fixture failed", file=sys.stderr)
        return 1
    bad = dict(good_transport)
    bad["status"] = "VERIFIED_ROUNDTRIP"
    bad["prompt"] = "secret"
    errs = validate(bad)
    if not any("self-promote" in e for e in errs) or not any("forbidden persisted" in e for e in errs):
        print("transport promotion negative fixture failed", file=sys.stderr)
        return 1
    bad_rt = dict(good_roundtrip)
    bad_rt["missing_span_ids"] = ["x"]
    if not validate(bad_rt):
        print("round-trip negative fixture failed", file=sys.stderr)
        return 1
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
        print("receipt path required", file=sys.stderr)
        return 2
    try:
        obj = json.loads(Path(args.path).read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"invalid receipt: {exc}", file=sys.stderr)
        return 2
    errors = validate(obj)
    for err in errors:
        print("ERROR", err)
    print(f"TRANSPORT_ROUNDTRIP_CONTRACT errors={len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
