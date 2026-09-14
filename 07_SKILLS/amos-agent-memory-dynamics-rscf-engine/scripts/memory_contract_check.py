#!/usr/bin/env python3
import argparse
import json
import sys

ALLOWED = {"ACTIVE", "QUARANTINED", "SUPERSEDED", "EXPIRED", "TOMBSTONED"}


def audit(x):
    issues = []
    state = x.get("state")
    if state not in ALLOWED:
        issues.append("INVALID_STATE")
    if not x.get("memory_id"):
        issues.append("MISSING_MEMORY_ID")
    if not x.get("origin_id"):
        issues.append("MISSING_ORIGIN_ID")
    if not isinstance(x.get("version"), int) or x.get("version", 0) < 1:
        issues.append("INVALID_VERSION")
    if not x.get("scope"):
        issues.append("MISSING_SCOPE")
    if not x.get("provenance"):
        issues.append("MISSING_PROVENANCE")
    if x.get("epistemic_class") not in {None, "OBSERVATION"}:
        issues.append("MEMORY_PROMOTED_BEYOND_OBSERVATION")
    vf, vt = x.get("valid_from"), x.get("valid_to")
    if vf is not None and vt is not None and vt < vf:
        issues.append("INVALID_VALIDITY_INTERVAL")
    if state == "QUARANTINED" and x.get("context_eligible", False):
        issues.append("QUARANTINE_LEAK")
    if state in {"SUPERSEDED", "EXPIRED", "TOMBSTONED"} and x.get("context_eligible", False):
        issues.append("NONACTIVE_CONTEXT_LEAK")
    return {"status": "PASS" if not issues else "QUARANTINE", "issues": issues}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("path", nargs="?")
    p.add_argument("--self-test", action="store_true")
    a = p.parse_args()
    if a.self_test:
        ok = audit({"memory_id": "m", "origin_id": "o", "version": 1, "scope": "s", "provenance": "p", "state": "ACTIVE", "epistemic_class": "OBSERVATION", "context_eligible": True})
        bad = audit({"memory_id": "m", "origin_id": "o", "version": 1, "scope": "s", "provenance": "p", "state": "QUARANTINED", "epistemic_class": "OBSERVATION", "context_eligible": True})
        if ok["status"] != "PASS" or "QUARANTINE_LEAK" not in bad["issues"]:
            return 1
        print("PASS memory contract self-test")
        return 0
    if not a.path:
        p.error("path required unless --self-test")
    with open(a.path, encoding="utf-8") as f:
        data = json.load(f)
    result = audit(data)
    print(json.dumps(result, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
