from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ALLOWED_RUN = {"RUNNING", "CONTINUED_AS_NEW", "COMPLETED", "BLOCKED"}
ALLOWED_STEP = {"STARTED", "COMPLETED", "RETRYABLE", "AMBIGUOUS"}
ALLOWED_KIND = {"PURE", "EFFECT"}


def audit(snapshot: dict[str, Any]) -> dict[str, Any]:
    issues: list[str] = []
    for key in [
        "workflow_id",
        "run_id",
        "code_version",
        "status",
        "explicit_state_hash",
        "steps",
        "event_head",
    ]:
        if key not in snapshot:
            issues.append(f"MISSING:{key}")
    if issues:
        return {"status": "QUARANTINE", "issues": issues}

    if not snapshot["workflow_id"]:
        issues.append("WORKFLOW_ID_EMPTY")
    if not isinstance(snapshot["run_id"], int) or snapshot["run_id"] <= 0:
        issues.append("RUN_ID_INVALID")
    if not snapshot["code_version"]:
        issues.append("CODE_VERSION_EMPTY")
    if snapshot["status"] not in ALLOWED_RUN:
        issues.append("RUN_STATUS_INVALID")
    if not snapshot["explicit_state_hash"]:
        issues.append("STATE_HASH_EMPTY")
    if not snapshot["event_head"]:
        issues.append("EVENT_HEAD_EMPTY")
    if not isinstance(snapshot["steps"], list):
        issues.append("STEPS_NOT_LIST")
        return {"status": "QUARANTINE", "issues": issues}

    unresolved_effects = []
    seen = set()
    for step in snapshot["steps"]:
        sid = step.get("step_id")
        if not sid:
            issues.append("STEP_ID_EMPTY")
            continue
        if sid in seen:
            issues.append(f"STEP_ID_DUPLICATE:{sid}")
        seen.add(sid)
        kind = step.get("kind")
        status = step.get("status")
        if kind not in ALLOWED_KIND:
            issues.append(f"STEP_KIND_INVALID:{sid}")
        if status not in ALLOWED_STEP:
            issues.append(f"STEP_STATUS_INVALID:{sid}")
        if status == "COMPLETED" and not step.get("output_hash"):
            issues.append(f"COMPLETED_WITHOUT_RECEIPT:{sid}")
        if kind == "EFFECT":
            if not step.get("effect_key"):
                issues.append(f"EFFECT_KEY_MISSING:{sid}")
            if status in {"STARTED", "AMBIGUOUS"}:
                unresolved_effects.append(sid)

    if unresolved_effects:
        issues.append("UNRESOLVED_EFFECTS:" + ",".join(sorted(unresolved_effects)))

    return {
        "status": "PASS" if not issues else "QUARANTINE",
        "issues": issues,
    }


def self_test() -> None:
    good = {
        "workflow_id": "wf",
        "run_id": 1,
        "code_version": "v1",
        "status": "RUNNING",
        "explicit_state_hash": "abc",
        "event_head": "def",
        "steps": [
            {
                "step_id": "s1",
                "kind": "PURE",
                "status": "COMPLETED",
                "output_hash": "x",
                "effect_key": None,
            },
            {
                "step_id": "e1",
                "kind": "EFFECT",
                "status": "COMPLETED",
                "output_hash": "y",
                "effect_key": "op-1",
            },
        ],
    }
    assert audit(good)["status"] == "PASS"
    bad = json.loads(json.dumps(good))
    bad["steps"][1]["status"] = "AMBIGUOUS"
    assert audit(bad)["status"] == "QUARANTINE"
    assert any(
        x.startswith("UNRESOLVED_EFFECTS") for x in audit(bad)["issues"]
    )
    print("durable_contract_check self-test PASS")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if args.path:
        data = json.loads(Path(args.path).read_text(encoding="utf-8"))
    else:
        data = json.load(sys.stdin)
    result = audit(data)
    print(json.dumps(result, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
