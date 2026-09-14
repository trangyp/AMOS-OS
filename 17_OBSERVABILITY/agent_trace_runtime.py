#!/usr/bin/env python3
"""Compatibility adapter to the canonical Skill-local AgentOps trace runtime.

The implementation is owned by
`07_SKILLS/amos-agentops-observability-rscf/scripts/agent_trace_runtime.py`
so the portable Skill and AMOS observability plane execute one code path.
"""
from __future__ import annotations

from pathlib import Path

_IMPL = (
    Path(__file__).resolve().parents[1]
    / "07_SKILLS"
    / "amos-agentops-observability-rscf"
    / "scripts"
    / "agent_trace_runtime.py"
)

if not _IMPL.exists():
    raise RuntimeError(f"canonical AgentOps trace runtime not found: {_IMPL}")

exec(compile(_IMPL.read_text(encoding="utf-8"), str(_IMPL), "exec"), globals(), globals())
