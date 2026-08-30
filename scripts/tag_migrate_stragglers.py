#!/usr/bin/env python3
"""
Pass 6b — Remediate remaining underscore-form canonical-tag stragglers.

Applies the declared "Hyphen, never underscore" rule to a small closed set of
known canonical tags that still appear in legacy underscore form (missed by
earlier passes because they weren't in the original rename map):
    amos_os -> amos-os
    control_plane -> control-plane
    cognitive_matrix -> cognitive-matrix
    master_canon -> master-canon
    total_canon_matrix -> total-canon-matrix
    cross_plane -> cross-plane
Fixes FRONTMATTER tags only. Pure format normalization, no semantic change.
Backs up each touched file.

Usage: python3 tag_migrate_stragglers.py --root . [--apply] [--backup-dir DIR]
Default: dry-run.
"""
import argparse, re, shutil, sys
from pathlib import Path

PAIRS = {
    'amos_os': 'amos-os',
    'control_plane': 'control-plane',
    'cognitive_matrix': 'cognitive-matrix',
    'master_canon': 'master-canon',
    'total_canon_matrix': 'total-canon-matrix',
    'cross_plane': 'cross-plane',
}

def transform(path, apply, basin):
    text = path.read_text(encoding='utf-8', errors='replace')
    m = re.match(r'^---\s*\n(.*?)\n---', text, re.S)
    if not m:
        return path, 0, 0
    head = m.group(1)
    out = []
    in_tags = False
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
        if tag in PAIRS:
            changed += 1
            out.append(f'{indent}- {PAIRS[tag]}\n')
        else:
            out.append(line)
    if changed == 0:
        return path, 0, 0
    new_head = ''.join(out)
    new_text = text[:m.start(1)] + new_head + text[m.end(1):]
    if apply:
        if basin is not None:
            bak = basin / (str(path).replace('/', '__') + '.bak')
            shutil.copy2(path, bak)
        path.write_text(new_text, encoding='utf-8')
    return path, changed, changed

def main():
    global args
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
        _, ch, _ = transform(p, args.apply, basin)
        if ch:
            touched += 1
            instances += ch
            print(f"   {str(p)}  ({ch})")
    print(f"[{'APPLIED' if args.apply else 'DRY-RUN'}] files: {touched}, instances: {instances}")
    return 0

if __name__ == '__main__':
    sys.exit(main())
