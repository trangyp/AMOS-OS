#!/usr/bin/env python3
"""Portable structural preflight for the AMOS AgentOps Observability Skill.

This hook validates only Skill packaging/discovery structure. It does not grant tool,
telemetry-capture, or effect authority.
"""
from __future__ import annotations

import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[2]
SKILL_MD = SKILL_DIR / "SKILL.md"


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing YAML frontmatter opening delimiter")
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration as exc:
        raise ValueError("missing YAML frontmatter closing delimiter") from exc
    data: dict[str, str] = {}
    for raw in lines[1:end]:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw[:1].isspace() or ":" not in raw:
            raise ValueError(f"unsupported frontmatter syntax: {raw!r}")
        key, value = raw.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def main() -> int:
    if not SKILL_MD.exists():
        print("BLOCK: SKILL.md not found")
        return 1
    try:
        text = SKILL_MD.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(text)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"BLOCK: invalid SKILL.md: {exc}")
        return 1

    if set(frontmatter) != {"name", "description"}:
        print("BLOCK: portable Skill frontmatter must contain only name and description")
        return 1
    if frontmatter.get("name") != "amos-agentops-observability-rscf":
        print("BLOCK: Skill name does not match directory identity")
        return 1
    if not frontmatter.get("description"):
        print("BLOCK: Skill description is required")
        return 1
    if len(text.splitlines()) > 500:
        print("WARN: SKILL.md exceeds 500 lines; use progressive references")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
