#!/usr/bin/env python3
"""
tag_migrate_lNN.py — Pass 3 (lNN family): remove degenerate path-mirror tags only.

The lNN prefix is overloaded across two MEANINGFUL systems that we keep:
  - cognitive-matrix layer tags   (l00_reality_environment ... l29_evolution)
                                   bound to 25_COGNITIVE_MATRIX/01_PRIMITIVES/LNN_*/
  - RSCF law-gate tags             (l4-causal, l10-failure-recovery, l18-gmef, ...)

THOSE ARE LEFT ALONE. This pass targets ONLY the third, degenerate sub-family:
tags whose body mirrors the file's OWN path, i.e. contain the literal
`primitives-cognitive-matrix-*` fragment (e.g. l17-decision-primitives-cognitive-
matrix-readme). They encode filename/path info, not independent meaning, and are
generation artifacts. Removed as pure noise.

Scope audit (2026-08-30): 153 distinct degenerate tags / 195 instances /
45 files, all inside 25_COGNITIVE_MATRIX/01_PRIMITIVES/LNN_*/.

DRY-RUN by default (prints stats, writes nothing).
--apply --confirm --backup-dir <DIR> writes, snapshotting originals for rollback.
"""

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

# A tag is degenerate if it starts with l+digits AND its body contains the
# literal 'primitives-cognitive-matrix' path mirror.
DEGENERATE = re.compile(r"^l\d+.*primitives[_-]cognitive[_-]matrix", re.I)


def parse_frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    if not m:
        return None, None
    return m.group(1), m.group(0)


def strip_degenerate_from_fm(fm):
    """Return (new_fm, dropped_list). Only removes DEGENERATE tags."""
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
                if DEGENERATE.match(t):
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
        new_fm, dropped = strip_degenerate_from_fm(fm)
        if not dropped:
            continue
        changed += 1
        for d in dropped:
            tag_drops[d] += 1
        if not args.apply:
            if len(examples) < 20:
                examples.append(f"{path}: -{len(dropped)} ({', '.join(dropped)})")
        else:
            text2 = text.replace(block, "---\n" + new_fm + "\n---", 1)
            if args.backup_dir:
                rel = str(path.relative_to(root)).replace("/", "__") + ".bak"
                bakp = Path(args.backup_dir) / rel
                bakp.parent.mkdir(parents=True, exist_ok=True)
                bakp.write_text(text, encoding="utf-8")
            path.write_text(text2, encoding="utf-8")

    print(f"files changed: {changed}")
    print(f"distinct degenerate tags removed: {len(tag_drops)}")
    print(f"degenerate tag instances removed: {sum(tag_drops.values())}")
    if tag_drops:
        print("\nTop removed tags:")
        for k, v in tag_drops.most_common(20):
            print(f"  DROP {v:>4}  {k}")
    if examples:
        print("\nSample files (dry-run):")
        for e in examples:
            print("  " + e)
    print("APPLIED." if args.apply else "DRY-RUN only — no files written.")


if __name__ == "__main__":
    main()
