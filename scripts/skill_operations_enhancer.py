#!/usr/bin/env python3
"""Generate a minimal but valid `## Operations` section for AMOS `SKILL.md`
files that have `## Capabilities` but no `## Operations`.

Each capability is converted into a numbered operation.  Complex multi-line
capability bullets are summarized by their first line.  The section is inserted
immediately after the `## Capabilities` block.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def _extract_capabilities_block(txt: str) -> list[str] | None:
    """Return the bullet lines under `## Capabilities` (or `## Capabilities\n`)."""
    m = re.search(r"^## Capabilities\s*\n(.*?)(?=\n## |\Z)", txt, re.MULTILINE | re.DOTALL)
    if not m:
        return None
    block = m.group(1).strip()
    if not block:
        return None
    # Split into top-level bullets (lines starting with '-' or '*')
    bullets: list[str] = []
    current: list[str] = []
    for line in block.splitlines():
        if re.match(r"^\s*[-*]\s+", line):
            if current:
                bullets.append(" ".join(current).strip())
            current = [line]
        elif line.strip() and current and (line.startswith(" ") or line.startswith("\t")):
            current.append(line.strip())
    if current:
        bullets.append(" ".join(current).strip())
    return bullets


def _bullet_to_operation(idx: int, bullet: str) -> str:
    # strip leading '- ' or '* '
    body = re.sub(r"^\s*[-*]\s+", "", bullet)
    # remove backtick/asterisk markup? keep bold for readability
    body = re.sub(r"\s+", " ", body)
    # Keep a concise one-line description
    if len(body) > 240:
        body = body[:237].rstrip() + "..."
    return f"{idx}. {body}"


def _build_operations_txt(bullets: list[str]) -> str:
    ops = ["## Operations", ""]
    for i, b in enumerate(bullets, 1):
        ops.append(_bullet_to_operation(i, b))
    # leave a trailing blank before the next section
    ops.append("")
    return "\n".join(ops)


def _canonicalize_operations(skill_md: Path, dry_run: bool) -> tuple[bool, str]:
    txt = skill_md.read_text(encoding="utf-8", errors="replace")
    if "## Operations" in txt:
        return False, "already_has_operations"
    bullets = _extract_capabilities_block(txt)
    if not bullets:
        return False, "no_capabilities_block"
    m = re.search(r"(^## Capabilities\s*\n.*?)(?=\n## |\Z)", txt, re.MULTILINE | re.DOTALL)
    if not m:
        return False, "parse_error"
    insert_pos = m.end()
    new_txt = txt[:insert_pos] + "\n" + _build_operations_txt(bullets) + txt[insert_pos:]
    if dry_run:
        return True, f"would_insert_{len(bullets)}_operations"
    skill_md.write_text(new_txt, encoding="utf-8")
    return True, f"inserted_{len(bullets)}_operations"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate ## Operations from ## Capabilities")
    parser.add_argument("roots", nargs="+", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    changed: list[tuple[str, str, str]] = []
    for root in args.roots:
        if not root.exists():
            continue
        for d in root.iterdir():
            if not d.is_dir():
                continue
            skill_md = d / "SKILL.md"
            if not skill_md.exists():
                continue
            did, msg = _canonicalize_operations(skill_md, args.dry_run)
            if did:
                changed.append((str(root), d.name, msg))

    print(f"{'WOULD CHANGE' if args.dry_run else 'CHANGED'}: {len(changed)} files")
    for root, name, msg in changed:
        print(f"  {root}/{name} -> {msg}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
