#!/usr/bin/env python3
"""
tag_migrate_suffix.py — Pass 5 candidate (DRAFT, NOT auto-executed): remove
redundant artifact-suffix tags (-readme, -map, -contract, -registry, -canon,
-index).

Evidence (2026-08-30) shows these are PURE REDUNDANCY, same class as the Pass-3
degenerate lNN mirrors:
  - artifact-kind is ALREADY in every filename (KIND: *_README/_MAP/_CONTRACT/
    _REGISTRY/_CANON/_INDEX) or parent dir: 8,639/8,639 instances.
  - plane is ALREADY in the path (TOP_LEVEL_PLANE/...).
  - no `.obsidian/graph.json` color-group references any suffix tag.
  - no dataview/MOC query references a suffix tag (the 11 `canon` hits are
    namespaced `canon/*` tags, NOT `-canon` suffixes).
  - 0 files (of 2,076) would be left tagless.

These tags do NOT overlap with `type:` values (a file keeps its one `type:`),
so removing them is pure noise elimination — NOT Option C (adding type:+plane:).
Option C is REJECTED: path + filename + type: already encode both axes; adding
properties would triple-redundant-encode.

Requires EXPLICIT sign-off to apply (large: ~8,639 tags / 2,076 files /
~30% of vault).
DRY-RUN by default. --apply --confirm --backup-dir <DIR> writes with rollback.
"""

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

SUFFIXES = ("-readme", "-map", "-contract", "-registry", "-canon", "-index")


def is_suffix_tag(t):
    return t.endswith(SUFFIXES)


def parse_frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    if not m:
        return None, None
    return m.group(1), m.group(0)


def strip_suffix_from_fm(fm):
    lines = fm.splitlines()
    out = []
    in_tags = False
    dropped = []
    for line in lines:
        if re.match(r"^tags:\s*$", line):
            in_tags = True
            out.append(line)
            continue
        if in_tags:
            if re.match(r"^\s*-\s+", line):
                t = line.strip()[2:].strip().lstrip("#")
                if is_suffix_tag(t):
                    dropped.append(t)
                    continue
                out.append(line)
            else:
                in_tags = False
                out.append(line)
            continue
        out.append(line)
    return "\n".join(out), dropped


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--confirm", action="store_true")
    ap.add_argument("--backup-dir", default=None)
    args = ap.parse_args()

    if args.apply and not args.confirm:
        print("Refusing to write without --confirm.", file=sys.stderr)
        sys.exit(2)
    if args.apply and not args.backup_dir:
        print("Warning: --apply without --backup-dir (no rollback basin).", file=sys.stderr)

    root = Path(args.root)
    changed = 0
    tag_drops = Counter()
    examples = []

    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        fm, block = parse_frontmatter(text)
        if fm is None:
            continue
        new_fm, dropped = strip_suffix_from_fm(fm)
        if not dropped:
            continue
        changed += 1
        for d in dropped:
            tag_drops[d] += 1
        if not args.apply:
            if len(examples) < 12:
                examples.append(f"{path}: -{len(dropped)}")
        else:
            text2 = text.replace(block, "---\n" + new_fm + "\n---", 1)
            if args.backup_dir:
                rel = str(path.relative_to(root)).replace("/", "__") + ".bak"
                bakp = Path(args.backup_dir) / rel
                bakp.parent.mkdir(parents=True, exist_ok=True)
                bakp.write_text(text, encoding="utf-8")
            path.write_text(text2, encoding="utf-8")

    print(f"files changed: {changed}")
    print(f"suffix tag instances removed: {sum(tag_drops.values())}")
    print("\nBy suffix:")
    by_suf = Counter()
    for t, c in tag_drops.items():
        for s in SUFFIXES:
            if t.endswith(s):
                by_suf[s] += c
                break
    for s in SUFFIXES:
        print(f"  {s:<12}{by_suf[s]:>6}")
    if examples:
        print("\nSample files (dry-run):")
        for e in examples:
            print("  " + e)
    print("APPLIED." if args.apply else "DRY-RUN only — no files written.")


if __name__ == "__main__":
    main()
