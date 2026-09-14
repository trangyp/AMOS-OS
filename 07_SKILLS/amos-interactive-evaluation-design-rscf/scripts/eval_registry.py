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
EVIDENCE_CLASSES = {
    "CONCEPTUAL_DESIGN",
    "SYNTHETIC_SCENARIO",
    "EXECUTED_MODEL",
    "EXECUTED_RUNTIME",
    "UNKNOWN",
}
VERDICTS = {
    "VERIFIED_TESTED_SCOPE",
    "PARTIAL",
    "INVALIDATED_EVIDENCE",
    "CONCEPTUAL_ONLY",
    "NON_REPRODUCIBLE",
    "UNKNOWN",
}
VERIFIED_CLASSES = {"EXECUTED_MODEL", "EXECUTED_RUNTIME"}
HEX40 = set("0123456789abcdef")


def nonempty_string(obj: dict[str, Any], key: str, errors: list[str], prefix: str) -> str | None:
    value = obj.get(key)
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{prefix}.{key} must be a non-empty string")
        return None
    return value.strip()


def valid_sha(value: Any) -> bool:
    return isinstance(value, str) and len(value) == 40 and set(value.lower()) <= HEX40


def git_blob_sha(path: Path) -> str:
    payload = path.read_bytes()
    header = f"blob {len(payload)}\0".encode("ascii")
    return hashlib.sha1(header + payload).hexdigest()


def validate_entry(entry: Any, repo: Path | None, index: int) -> list[str]:
    p = f"entries[{index}]"
    errors: list[str] = []
    if not isinstance(entry, dict):
        return [f"{p} must be an object"]

    nonempty_string(entry, "suite_id", errors, p)
    nonempty_string(entry, "target", errors, p)
    nonempty_string(entry, "scope", errors, p)

    evidence_class = entry.get("evidence_class")
    verdict = entry.get("verdict")
    if evidence_class not in EVIDENCE_CLASSES:
        errors.append(f"{p}.evidence_class must be one of {sorted(EVIDENCE_CLASSES)}")
    if verdict not in VERDICTS:
        errors.append(f"{p}.verdict must be one of {sorted(VERDICTS)}")

    not_proven = entry.get("not_proven")
    if not isinstance(not_proven, list) or not all(isinstance(x, str) and x.strip() for x in not_proven):
        errors.append(f"{p}.not_proven must be a list of non-empty strings")

    harness_path = entry.get("harness_path")
    receipt_path = entry.get("receipt_path")
    harness_sha = entry.get("harness_blob_sha")
    receipt_sha = entry.get("receipt_blob_sha")
    result = entry.get("result")

    if verdict == "VERIFIED_TESTED_SCOPE":
        if evidence_class not in VERIFIED_CLASSES:
            errors.append(f"{p}: VERIFIED_TESTED_SCOPE requires EXECUTED_MODEL or EXECUTED_RUNTIME")
        for key, value in (("harness_path", harness_path), ("receipt_path", receipt_path)):
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{p}.{key} is required for VERIFIED_TESTED_SCOPE")
        for key, value in (("harness_blob_sha", harness_sha), ("receipt_blob_sha", receipt_sha)):
            if not valid_sha(value):
                errors.append(f"{p}.{key} must be an exact 40-char Git blob SHA for VERIFIED_TESTED_SCOPE")
        if not isinstance(result, dict):
            errors.append(f"{p}.result is required for VERIFIED_TESTED_SCOPE")
        else:
            for key in ("total", "passed", "failed", "exit_code"):
                if not isinstance(result.get(key), int):
                    errors.append(f"{p}.result.{key} must be an integer")
            if all(isinstance(result.get(k), int) for k in ("total", "passed", "failed")):
                if result["total"] < 0 or result["passed"] < 0 or result["failed"] < 0:
                    errors.append(f"{p}.result counts must be non-negative")
                if result["passed"] + result["failed"] > result["total"]:
                    errors.append(f"{p}.result passed+failed cannot exceed total")
        env = entry.get("environment")
        if not isinstance(env, dict) or not env:
            errors.append(f"{p}.environment must be a non-empty object for VERIFIED_TESTED_SCOPE")

    if verdict == "CONCEPTUAL_ONLY" and evidence_class != "CONCEPTUAL_DESIGN":
        errors.append(f"{p}: CONCEPTUAL_ONLY requires CONCEPTUAL_DESIGN evidence_class")

    if verdict == "NON_REPRODUCIBLE":
        if not isinstance(receipt_path, str) or not receipt_path.strip():
            errors.append(f"{p}.receipt_path is required for NON_REPRODUCIBLE")
        if evidence_class in VERIFIED_CLASSES:
            errors.append(f"{p}: NON_REPRODUCIBLE cannot be promoted as {evidence_class}")

    if verdict in {"PARTIAL", "INVALIDATED_EVIDENCE", "UNKNOWN"} and evidence_class in VERIFIED_CLASSES:
        if not isinstance(harness_path, str) or not harness_path.strip():
            errors.append(f"{p}: executed partial evidence requires harness_path")

    if repo is not None:
        for key, value, sha_key, declared_sha in (
            ("harness_path", harness_path, "harness_blob_sha", harness_sha),
            ("receipt_path", receipt_path, "receipt_blob_sha", receipt_sha),
        ):
            if isinstance(value, str) and value.strip():
                target = repo / value
                if not target.is_file():
                    errors.append(f"{p}.{key} does not exist in repository: {value}")
                elif valid_sha(declared_sha):
                    actual_sha = git_blob_sha(target)
                    if actual_sha != declared_sha:
                        errors.append(f"{p}.{sha_key} mismatch: declared {declared_sha}, actual {actual_sha}")

    return errors


def validate(data: Any, repo: Path | None = None) -> list[str]:
    if not isinstance(data, dict):
        return ["registry root must be an object"]
    errors: list[str] = []
    if data.get("schema") != SCHEMA:
        errors.append(f"schema must equal {SCHEMA}")
    if not isinstance(data.get("generated_from"), str) or not data["generated_from"].strip():
        errors.append("generated_from must be a non-empty string")
    entries = data.get("entries")
    if not isinstance(entries, list) or not entries:
        errors.append("entries must be a non-empty list")
        return errors
    seen: set[str] = set()
    for i, entry in enumerate(entries):
        errors.extend(validate_entry(entry, repo, i))
        if isinstance(entry, dict) and isinstance(entry.get("suite_id"), str):
            sid = entry["suite_id"]
            if sid in seen:
                errors.append(f"entries[{i}].suite_id duplicates {sid}")
            seen.add(sid)
    return errors


def self_test() -> int:
    good = {
        "schema": SCHEMA,
        "generated_from": "self-test",
        "entries": [{
            "suite_id": "T-1",
            "target": "fixture",
            "scope": "bounded",
            "evidence_class": "EXECUTED_MODEL",
            "verdict": "VERIFIED_TESTED_SCOPE",
            "harness_path": "h.py",
            "receipt_path": "r.md",
            "harness_blob_sha": "a" * 40,
            "receipt_blob_sha": "b" * 40,
            "result": {"total": 1, "passed": 1, "failed": 0, "exit_code": 0},
            "environment": {"runtime": "python"},
            "not_proven": ["production runtime"],
        }],
    }
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "h.py").write_text("print('ok')\n", encoding="utf-8")
        (root / "r.md").write_text("receipt\n", encoding="utf-8")
        good["entries"][0]["harness_blob_sha"] = git_blob_sha(root / "h.py")
        good["entries"][0]["receipt_blob_sha"] = git_blob_sha(root / "r.md")
        if validate(good, root):
            print("SELF_TEST positive fixture failed", file=sys.stderr)
            return 1
        bad = json.loads(json.dumps(good))
        del bad["entries"][0]["harness_path"]
        if not validate(bad, root):
            print("SELF_TEST expected missing harness rejection", file=sys.stderr)
            return 1
        bad2 = json.loads(json.dumps(good))
        bad2["entries"][0]["evidence_class"] = "CONCEPTUAL_DESIGN"
        if not validate(bad2, root):
            print("SELF_TEST expected conceptual-as-verified rejection", file=sys.stderr)
            return 1
    print("SELF_TEST_PASS")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate AMOS evaluation evidence registry")
    ap.add_argument("registry", nargs="?")
    ap.add_argument("--repo", default=".")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if not args.registry:
        ap.error("registry is required unless --self-test is used")
    repo = Path(args.repo).resolve()
    try:
        data = json.loads(Path(args.registry).read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"ERROR invalid registry JSON: {exc}", file=sys.stderr)
        return 2
    errors = validate(data, repo)
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        print(f"EVAL_REGISTRY_FAIL errors={len(errors)}")
        return 1
    print("EVAL_REGISTRY_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
