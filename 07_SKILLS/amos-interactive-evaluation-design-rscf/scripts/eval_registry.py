#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import tempfile
from pathlib import Path
from typing import Any

SCHEMA = "amos.eval-evidence-registry.v1"
EVIDENCE_CLASSES = {"CONCEPTUAL_DESIGN", "SYNTHETIC_SCENARIO", "EXECUTED_MODEL", "EXECUTED_RUNTIME", "UNKNOWN"}
VERDICTS = {"VERIFIED_TESTED_SCOPE", "PARTIAL", "INVALIDATED_EVIDENCE", "CONCEPTUAL_ONLY", "NON_REPRODUCIBLE", "UNKNOWN"}
VERIFIED_CLASSES = {"EXECUTED_MODEL", "EXECUTED_RUNTIME"}


def git_blob_sha(path: Path) -> str:
    payload = path.read_bytes()
    return hashlib.sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


def is_sha40(v: Any) -> bool:
    return isinstance(v, str) and len(v) == 40 and all(c in "0123456789abcdef" for c in v)


def req_str(obj: dict[str, Any], key: str, errors: list[str], prefix: str) -> None:
    if not isinstance(obj.get(key), str) or not obj[key].strip():
        errors.append(f"{prefix}.{key} must be a non-empty string")


def validate_entry(entry: Any, repo: Path | None, i: int) -> list[str]:
    p = f"entries[{i}]"
    if not isinstance(entry, dict):
        return [f"{p} must be object"]
    e: list[str] = []
    for k in ("suite_id", "target", "scope"):
        req_str(entry, k, e, p)
    ec, verdict = entry.get("evidence_class"), entry.get("verdict")
    if ec not in EVIDENCE_CLASSES:
        e.append(f"{p}.evidence_class invalid")
    if verdict not in VERDICTS:
        e.append(f"{p}.verdict invalid")
    if not isinstance(entry.get("not_proven"), list) or not all(isinstance(x, str) and x.strip() for x in entry.get("not_proven", [])):
        e.append(f"{p}.not_proven must be list of non-empty strings")
    hp, rp = entry.get("harness_path"), entry.get("receipt_path")
    hs, rs = entry.get("harness_blob_sha"), entry.get("receipt_blob_sha")
    if verdict == "VERIFIED_TESTED_SCOPE":
        if ec not in VERIFIED_CLASSES:
            e.append(f"{p}: verified verdict requires executed evidence class")
        for k, v in (("harness_path", hp), ("receipt_path", rp)):
            if not isinstance(v, str) or not v.strip():
                e.append(f"{p}.{k} required for verified verdict")
        for k, v in (("harness_blob_sha", hs), ("receipt_blob_sha", rs)):
            if not is_sha40(v):
                e.append(f"{p}.{k} must be exact Git blob SHA")
        result = entry.get("result")
        if not isinstance(result, dict):
            e.append(f"{p}.result required")
        else:
            vals = [result.get(k) for k in ("total", "passed", "failed", "exit_code")]
            if not all(isinstance(x, int) for x in vals):
                e.append(f"{p}.result counts/exit_code must be integers")
            elif min(vals[:3]) < 0 or vals[1] + vals[2] > vals[0]:
                e.append(f"{p}.result counts invalid")
        if not isinstance(entry.get("environment"), dict) or not entry["environment"]:
            e.append(f"{p}.environment required for verified verdict")
    if verdict == "CONCEPTUAL_ONLY" and ec != "CONCEPTUAL_DESIGN":
        e.append(f"{p}: conceptual verdict requires conceptual evidence")
    if verdict == "NON_REPRODUCIBLE":
        if not isinstance(rp, str) or not rp.strip():
            e.append(f"{p}.receipt_path required for non-reproducible verdict")
        if ec in VERIFIED_CLASSES:
            e.append(f"{p}: non-reproducible evidence cannot be promoted as executed")
    if verdict in {"PARTIAL", "INVALIDATED_EVIDENCE", "UNKNOWN"} and ec in VERIFIED_CLASSES and not isinstance(hp, str):
        e.append(f"{p}: executed partial evidence requires harness_path")
    if repo:
        for path_value, sha_value, label in ((hp, hs, "harness"), (rp, rs, "receipt")):
            if isinstance(path_value, str) and path_value.strip():
                f = repo / path_value
                if not f.is_file():
                    e.append(f"{p}.{label}_path missing: {path_value}")
                elif is_sha40(sha_value) and git_blob_sha(f) != sha_value:
                    e.append(f"{p}.{label}_blob_sha mismatch")
    return e


def validate(data: Any, repo: Path | None = None) -> list[str]:
    if not isinstance(data, dict):
        return ["registry root must be object"]
    e: list[str] = []
    if data.get("schema") != SCHEMA:
        e.append(f"schema must equal {SCHEMA}")
    if not isinstance(data.get("generated_from"), str) or not data["generated_from"].strip():
        e.append("generated_from must be non-empty string")
    entries = data.get("entries")
    if not isinstance(entries, list) or not entries:
        return e + ["entries must be non-empty list"]
    seen: set[str] = set()
    for i, entry in enumerate(entries):
        e.extend(validate_entry(entry, repo, i))
        if isinstance(entry, dict) and isinstance(entry.get("suite_id"), str):
            sid = entry["suite_id"]
            if sid in seen:
                e.append(f"entries[{i}].suite_id duplicates {sid}")
            seen.add(sid)
    return e


def self_test() -> int:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "h.py").write_text("print('ok')\n", encoding="utf-8")
        (root / "r.md").write_text("receipt\n", encoding="utf-8")
        good = {
            "schema": SCHEMA,
            "generated_from": "self-test",
            "entries": [{
                "suite_id": "T-1", "target": "fixture", "scope": "bounded",
                "evidence_class": "EXECUTED_MODEL", "verdict": "VERIFIED_TESTED_SCOPE",
                "harness_path": "h.py", "receipt_path": "r.md",
                "harness_blob_sha": git_blob_sha(root / "h.py"), "receipt_blob_sha": git_blob_sha(root / "r.md"),
                "result": {"total": 1, "passed": 1, "failed": 0, "exit_code": 0},
                "environment": {"runtime": "python"}, "not_proven": ["production runtime"],
            }],
        }
        if validate(good, root):
            return 1
        bad = json.loads(json.dumps(good)); bad["entries"][0]["harness_blob_sha"] = "0" * 40
        if not validate(bad, root):
            return 1
        bad2 = json.loads(json.dumps(good)); bad2["entries"][0]["evidence_class"] = "CONCEPTUAL_DESIGN"
        if not validate(bad2, root):
            return 1
    print("SELF_TEST_PASS")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("registry", nargs="?")
    ap.add_argument("--repo", default=".")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if not a.registry:
        ap.error("registry is required unless --self-test")
    try:
        data = json.loads(Path(a.registry).read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"ERROR invalid registry JSON: {exc}", file=sys.stderr)
        return 2
    errors = validate(data, Path(a.repo).resolve())
    for error in errors:
        print("ERROR", error)
    print("EVAL_REGISTRY_PASS" if not errors else f"EVAL_REGISTRY_FAIL errors={len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
