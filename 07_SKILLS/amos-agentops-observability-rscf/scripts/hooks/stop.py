#!/usr/bin/env python3
"""End-of-run structural check for the AMOS AgentOps Observability Skill."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[2]
VALIDATOR = SKILL_DIR / "scripts" / "trace_contract.py"


def main() -> int:
    if not VALIDATOR.exists():
        print("BLOCK: trace_contract.py not found")
        return 1
    result = subprocess.run(
        [sys.executable, str(VALIDATOR), "--self-test"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        print("BLOCK: observability trace contract self-test failed")
        if result.stdout:
            print(result.stdout.rstrip())
        if result.stderr:
            print(result.stderr.rstrip())
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
