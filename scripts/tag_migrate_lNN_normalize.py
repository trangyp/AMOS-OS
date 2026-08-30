#!/usr/bin/env python3
"""
Pass 6a — Normalize the cognitive-matrix layer tag family to the canonical
`lNN-kind` hyphen form (applies the declared "Hyphen, never underscore" rule,
TAG_VOCABULARY §4 line 80, to the matrix-layer family).

SCOPE (safe, within-scheme, dedup-into-existing-sibling):
  Only 2-DIGIT bare lNN tags (matrix layers). The 1-DIGIT tags l1_reality /
  l2_cognition / l3_governance belong to a DIFFERENT scheme (Unified-Canon
  reality->cognition->governance) and are NEVER touched here.

  l05_binding                -> l05-binding     (dedup into existing hyphen sibling)
  l17_decision               -> l17-decision
  l00_reality_environment    -> l00-reality-environment

The larger `matrix/` vs `law/` namespacing split (the deferred naming decision
per §4 lines 87-90) is intentionally NOT performed here; it is a separate,
semantically-laden restructuring requiring explicit sign-off.

Usage: python3 tag_migrate_lNN_normalize.py --root . [--apply] [--backup-dir DIR]
Default: dry-run.
"""
import argparse, re, shutil, sys
from pathlib import Path

def canonical(tag):
    # only 2-digit underscore-form matrix layer: l<2digit>_<name...>
    # name may contain multiple words (internal underscores) -> all to hyphen
    m = re.match(r'^l(\d{2})_([a-z0-9][a-z0-9_]*)$', tag)
    if not m:
        return None
    name = m.group(2).replace('_', '-')
    return f'l{m.group(1)}-{name}'

def transform(path, apply, basin):
    text = path.read_text(encoding='utf-8', errors='replace')
    m = re.match(r'^---\s*\n(.*?)\n---', text, re.S)
    if not m:
        return path, 0
    head = m.group(1)
    out = []
    in_tags = False
    seen = []
    changed = 0
    for line in head.splitlines(keepends=True):
        s = line.rstrip('\n')
        if re.match(r'^tags:\s*$', s):
            in_tags = True
            out.append(line)
            continue
        if not in_tags:
            out.append(line)
            continue
        lm = re.match(r'^(\s*)-\s+(\S+)\s*$', s)
        if not lm:
            in_tags = False
            out.append(line)
            continue
        indent, tag = lm.group(1), lm.group(2)
        new = canonical(tag)
        if new and new in seen:
            changed += 1
            continue  # target already emitted: drop legacy duplicate
        if new:
            changed += 1
            seen.append(new)
            out.append(f'{indent}- {new}\n')
            continue
        seen.append(tag)
        out.append(line)
    if changed == 0:
        return path, 0
    new_head = ''.join(out)
    new_text = text[:m.start(1)] + new_head + text[m.end(1):]
    if apply:
        if basin is not None:
            bak = basin / (str(path).replace('/', '__') + '.bak')
            shutil.copy2(path, bak)
        path.write_text(new_text, encoding='utf-8')
    return path, changed

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.')
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--dry-run', dest='apply', action='store_false')
    ap.add_argument('--backup-dir')
    args = ap.parse_args()
    root = Path(args.root)
    basin = Path(args.backup_dir) if args.backup_dir else None
    if args.apply and basin is not None:
        basin.mkdir(parents=True, exist_ok=True)
    touched = instances = 0
    for p in root.rglob('*.md'):
        if '.git' in p.parts:
            continue
        _, ch = transform(p, args.apply, basin)
        if ch:
            touched += 1
            instances += ch
    print(f"[{'APPLIED' if args.apply else 'DRY-RUN'}] files: {touched}, instances: {instances}")
    return 0

if __name__ == '__main__':
    sys.exit(main())
