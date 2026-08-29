#!/usr/bin/env python3
"""Generate `## Operations` for AMOS workflow MD files that have `## Steps` but
no `## Operations`. Each top-level step becomes a numbered operation.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def _extract_steps_block(txt: str) -> list[str] | None:
    m = re.search(r"^## Steps\s*\n(.*?)(?=\n## |\Z)", txt, re.MULTILINE | re.DOTALL)
    if not m:
        return None
    block = m.group(1).strip()
    if not block:
        return None
    steps: list[str] = []
    current: list[str] = []
    for line in block.splitlines():
        if re.match(r"^\s*\d+\.\s+", line):
            if current:
                steps.append(" ".join(current).strip())
            current = [line]
        elif line.strip() and current and (line.startswith(" ") or line.startswith("\t")):
            current.append(line.strip())
    if current:
        steps.append(" ".join(current).strip())
    return steps


def _step_to_operation(idx: int, step: str) -> str:
    body = re.sub(r"^\s*\d+\.\s+", "", step)
    body = re.sub(r"\s+", " ", body)
    if len(body) > 240:
        body = body[:237].rstrip() + "..."
    return f"{idx}. {body}"


def _build_operations_txt(steps: list[str]) -> str:
    ops = ["## Operations", ""]
    for i, s in enumerate(steps, 1):
        ops.append(_step_to_operation(i, s))
    ops.append("")
    return "\n".join(ops)


def _canonicalize_operations(workflow_md: Path, dry_run: bool) -> tuple[bool, str]:
    txt = workflow_md.read_text(encoding="utf-8", errors="replace")
    if "## Operations" in txt:
        return False, "already_has_operations"
    steps = _extract_steps_block(txt)
    if not steps:
        return False, "no_steps_block"
    m = re.search(r"(^## Steps\s*\n.*?)(?=\n## |\Z)", txt, re.MULTILINE | re.DOTALL)
    if not m:
        return False, "parse_error"
    insert_pos = m.end()
    new_txt = txt[:insert_pos] + "\n" + _build_operations_txt(steps) + txt[insert_pos:]
    if dry_run:
        return True, f"would_insert_{len(steps)}_operations"
    workflow_md.write_text(new_txt, encoding="utf-8")
    return True, f"inserted_{len(steps)}_operations"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate ## Operations from ## Steps for workflows")
    parser.add_argument("root", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    changed = 0
    for f in args.root.rglob("*.md"):
        if not f.is_file():
            continue
        did, msg = _canonicalize_operations(f, args.dry_run)
        if did:
            changed += 1
            print(f"  {f.relative_to(args.root)} -> {msg}")

    print(f"{'WOULD CHANGE' if args.dry_run else 'CHANGED'}: {changed} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
