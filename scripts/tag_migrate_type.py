#!/usr/bin/env python3
"""
tag_migrate_type.py — Pass 4 (Option B): collapse near-duplicate `type:` values.

`type:` is a 164-value enum with separator/case drift. This collapses the known
collision families to a single canonical owner (same discipline as Pass-1 tag
renames):

  cognitive_matrix / cognitive-matrix / cognition  -> cognitive
  canon_specification                              -> canon
  core_law                                         -> law
  superseded                                       -> supersession
  source-summary                                   -> index

Only the `type:` VALUE is rewritten; NO other frontmatter is touched. Tags are
untouched by this pass.

Scope (2026-08-30): 49 files across 6 rename pairs.

DRY-RUN by default. --apply --confirm --backup-dir <DIR> writes with rollback.
"""

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

RENAME = {
    "cognitive_matrix": "cognitive",
    "cognitive-matrix": "cognitive",
    "cognition": "cognitive",
    "canon_specification": "canon",
    "core_law": "law",
    "superseded": "supersession",
    "source-summary": "index",
}

# only recognize these exact values (case-sensitive)
VALID = set(RENAME.keys())


def rewrite_type(fm):
    """Rewrite the type: VALUE in frontmatter per RENAME. Returns (new_fm, old, new)."""
    lines = fm.splitlines()
    out = []
    changed = None
    for line in lines:
        m = re.match(r"^(type:\s*)(\S+)(\s*)$", line)
        if m and m.group(2) in VALID:
            old = m.group(2)
            new = RENAME[old]
            line = m.group(1) + new + m.group(3)
            changed = (old, new)
        out.append(line)
    return "\n".join(out), changed


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
    changed_files = 0
    renames = Counter()
    examples = []

    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
        if not m:
            continue
        fm, block = m.group(1), m.group(0)
        new_fm, ch = rewrite_type(fm)
        if not ch:
            continue
        changed_files += 1
        renames[ch] += 1
        if not args.apply:
            if len(examples) < 25:
                examples.append(f"{path}: type:{ch[0]} -> {ch[1]}")
        else:
            text2 = text.replace(block, "---\n" + new_fm + "\n---", 1)
            if args.backup_dir:
                rel = str(path.relative_to(root)).replace("/", "__") + ".bak"
                bakp = Path(args.backup_dir) / rel
                bakp.parent.mkdir(parents=True, exist_ok=True)
                bakp.write_text(text, encoding="utf-8")
            path.write_text(text2, encoding="utf-8")

    print(f"files changed: {changed_files}")
    print("type: renames applied:")
    for (old, new), v in renames.most_common():
        print(f"  {old:<22} -> {new:<14} {v:>4} files")
    if examples:
        print("\nSample (dry-run):")
        for e in examples:
            print("  " + e)
    print("APPLIED." if args.apply else "DRY-RUN only — no files written.")


if __name__ == "__main__":
    main()
