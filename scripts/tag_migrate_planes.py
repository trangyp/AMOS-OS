#!/usr/bin/env python3
"""
Pass 8 — Remove redundant TOP-LEVEL plane-mirror tags (folder-leak noise).

A tag like `21_domains`, `01_canon`, `11_knowledge` merely mirrors the top-level
numbered folder the file already lives in (21_DOMAINS/, 01_CANON/, ...). It is
the same folder-leak class already removed in Pass 2 (`00-home`, `index-*`,
`*-moc`) per TAG_VOCABULARY §4 ("Remove filename-leak tags").

REMOVAL RULE (location-aware, fail-closed):
  - Drop a top-level plane tag `NN_xxx` from a file's tags ONLY if the file is
    physically under the matching `NN_XXX/` folder (pure mirror, fully redundant
    with the path).
  - PRESERVE a plane tag when the file is NOT under its folder (cross-plane
    reference — carries real meaning, e.g. `13_models` on a knowledge-file
    cross-domain governor).
Rare plane-tags for sub-folder mirrors and the `*_modes` reasoning-mode scheme are
NOT in scope (separate decision).

Usage: python3 tag_migrate_planes.py --root . [--apply] [--backup-dir DIR]
Default: dry-run.
"""
import argparse, re, shutil, sys
from pathlib import Path

def top_plane_folders(root):
    return {d.name.lower(): d.name for d in Path(root).iterdir()
            if d.is_dir() and re.match(r'^\d{1,2}_[A-Z]', d.name)}

def transform(path, root, planemap, apply, basin):
    rel_parts = list(path.relative_to(root).parts)
    text = path.read_text(encoding='utf-8', errors='replace')
    m = re.match(r'^---\s*\n(.*?)\n---', text, re.S)
    if not m:
        return path, 0, []
    head = m.group(1)
    out = []
    in_tags = False
    changed = 0
    log = []
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
        # only handle exact top-level plane tags
        if tag.lower() in planemap:
            folder = planemap[tag.lower()]
            if folder in rel_parts:
                # file IS under the matching plane folder -> pure mirror, drop
                changed += 1
                log.append((tag, 'DROP(in ' + folder + ')'))
                continue
            else:
                out.append(line)  # cross-reference: preserve
                continue
        out.append(line)
    if changed == 0:
        return path, 0, []
    new_head = ''.join(out)
    new_text = text[:m.start(1)] + new_head + text[m.end(1):]
    if apply:
        if basin is not None:
            bak = basin / (str(path.relative_to(root)).replace('/', '__') + '.bak')
            shutil.copy2(path, bak)
        path.write_text(new_text, encoding='utf-8')
    return path, changed, log

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.')
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--dry-run', dest='apply', action='store_false')
    ap.add_argument('--backup-dir')
    args = ap.parse_args()
    root = Path(args.root)
    planemap = top_plane_folders(root)
    print('Top-level plane folders:', len(planemap))
    basin = Path(args.backup_dir) if args.backup_dir else None
    if args.apply and basin is not None:
        basin.mkdir(parents=True, exist_ok=True)
    touched = instances = preserved = 0
    preserved_log = []
    for p in root.rglob('*.md'):
        if '.git' in p.parts:
            continue
        _, ch, log = transform(p, root, planemap, args.apply, basin)
        if ch:
            touched += 1
            instances += ch
    # Count preserved cross-refs (scan dry-run)
    for p in root.rglob('*.md'):
        if '.git' in p.parts: continue
        m=re.match(r"^---\s*\n(.*?)\n---", p.read_text(encoding='utf-8',errors='replace'), re.S)
        if not m: continue
        pp=list(p.relative_to(root).parts); in_tags=False
        for line in m.group(1).splitlines():
            if re.match(r'^tags:\s*$',line): in_tags=True; continue
            if in_tags and re.match(r'^\s*-\s+',line):
                t=line.strip()[2:].strip()
                if t.lower() in planemap and planemap[t.lower()] not in pp:
                    preserved+=1; preserved_log.append((t,str(p)))
            elif in_tags and not re.match(r'^\s*-',line): in_tags=False
    mode='APPLIED' if args.apply else 'DRY-RUN'
    print(f'[{mode}] files: {touched}, instances removed: {instances}')
    print(f'Preserved cross-reference plane tags (files not under that folder): {preserved}')
    for t,f in preserved_log: print(f'   {t:<20} @{f}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
