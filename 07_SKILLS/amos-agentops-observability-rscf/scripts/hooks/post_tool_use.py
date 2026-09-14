#!/usr/bin/env python3
"""Validate structured trace artifacts emitted by an AgentOps observability run.

Non-trace outputs pass through. Compatible trace JSON is validated using the
Skill-local runtime. The hook does not score prose or infer semantic quality.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[2]
RUNTIME = SKILL_DIR / "scripts" / "agent_trace_runtime.py"


def load_runtime():
    spec = importlib.util.spec_from_file_location("amos_post_trace_runtime", RUNTIME)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def main() -> int:
    raw = sys.stdin.read() if not sys.stdin.isatty() else ""
    if not raw.strip():
        return 0
    try:
        obj = json.loads(raw)
    except json.JSONDecodeError:
        return 0
    if not isinstance(obj, dict) or "trace_id" not in obj or "spans" not in obj:
        return 0
    if not RUNTIME.exists():
        print("BLOCK: Skill-local agent_trace_runtime.py not found")
        return 1
    try:
        mod = load_runtime()
        env = mod.TraceEnvelope.from_dict(obj)
        env.validate()
    except Exception as exc:
        print(f"BLOCK: invalid structured trace artifact: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
