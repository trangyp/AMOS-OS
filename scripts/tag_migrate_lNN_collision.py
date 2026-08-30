#!/usr/bin/env python3
"""
Pass 7 — Resolve the `lNN` three-way collision by namespacing (TAG_VOCABULARY §4
lines 87-90). APPLY-READY per repeated explicit "keep fixing" mandate.

The bare `lNN-<kind>` prefix is shared by THREE distinct schemes:
  1. COGNITIVE-MATRIX layers (01_CANON vs 25_COGNITIVE_MATRIX stack): -> matrix/lNN-kind
  2. CORE-LAW / law-stack gates:                                          -> law/LN-kind
  3. Unified-Canon third scheme (l1_reality/l2_cognition/l3_governance):   -> DROP

DISAMBIGUATION is by KIND-NAME membership against the two authoritative name sets
built from the actual stack folders. The two stacks share NO common name (verified),
so kind-name is a perfect collision-free classifier regardless of file location.

Authoritative name sets:
  LAW_NAMES    from 01_CANON/01_CORE_LAWS/   (L0-L33)
  MATRIX_NAMES from 25_COGNITIVE_MATRIX/01_PRIMITIVES/  (L00-L29)

Rules:
  - tag == 3rd-scheme literal            -> DROP
  - kind in MATRIX_NAMES                 -> matrix/l<num>-<kind>
  - kind in LAW_NAMES                    -> law/L<num>-<kind>   (uppercase L)
  - otherwise (unknown kind)             -> LEFT UNTOUCHED (fail closed I-RPOL-007)
The matrix <num> is zero-padded to 2 digits (l05 -> matrix/l05-...). The law
<num> uses the actual law number with uppercase L (law/L4-causal etc.).

Usage: python3 tag_migrate_lNN_collision.py --root . [--apply] [--backup-dir DIR]
Default: dry-run (prints a full classification report). Pass --apply to write.
"""
import argparse, re, shutil, sys
from pathlib import Path

THIRD = {'l1_reality', 'l2_cognition', 'l3_governance'}

def stack_pairs(d):
    """Return {(num, kind)} from a L<num>_NAME folder/file set (kind hyphenated, lowercase)."""
    pairs = set()
    for f in Path(d).iterdir():
        if not f.name.upper().startswith('L'):
            continue
        base = f.name[:-4] if f.name.lower().endswith('.md') else f.name
        mm = re.match(r'^L(\d+)[-_](.+)$', base, re.I)
        if mm and mm.group(1).isdigit():
            pairs.add((int(mm.group(1)), mm.group(2).lower().replace('_', '-')))
    return pairs

LAW_PAIRS = stack_pairs('01_CANON/01_CORE_LAWS')
MATRIX_PAIRS = stack_pairs('25_COGNITIVE_MATRIX/01_PRIMITIVES')
# manual correction for known scrape truncation (verified names from vocab doc)
LAW_PAIRS |= {p for p in {
    (4,'causal'),(5,'scope-regime'),(6,'uncertainty'),(7,'authority'),
    (8,'execution'),(9,'evolution'),(10,'failure-recovery'),
    (11,'knowledge-memory'),(15,'fractal-knowledge'),(16,'hml'),(17,'rscf'),
    (18,'gmef'),(19,'proof-capsule'),(20,'adversarial'),
    (21,'epistemic-regime'),(22,'atomic-reasoning'),(23,'mvcc-cas'),
    (24,'causal-epoch'),(25,'shard-local'),(26,'proof-coordination'),
    (27,'gap'),(28,'critical-gap'),(29,'decision-value'),
    (30,'authority-boundary'),(31,'amos-plane'),(32,'canon'),(33,'kernel'),
    (22,'replayability'),  # L22_REPLAYABILITY.md is type:law (Deterministic Replayability Law)
}}
MATRIX_PAIRS |= {(0,'reality-validation-receipt')}  # 25_COGNITIVE_MATRIX/11_VALIDATION/L00_REALITY_VALIDATION_RECEIPT.md
# also include any law/matrix LNN tags already present in namespaced form where a bare form exists

def classify(tag):
    if tag in THIRD:
        return 'DROP'
    m = re.match(r'^l(\d+)[-_]([a-z][a-z0-9-]*)$', tag)
    if not m:
        return None
    num, kind = int(m.group(1)), m.group(2)
    if (num, kind) in MATRIX_PAIRS:
        return f'matrix/l{num:02d}-{kind}'
    if (num, kind) in LAW_PAIRS:
        return f'law/L{num}-{kind}'
    return None  # fail closed: unknown (number,kind) left untouched

def transform(path, apply, basin):
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
        new = classify(tag)
        if new is None:
            out.append(line)
            continue
        if new == 'DROP':
            changed += 1
            log.append((tag, 'DROP'))
            continue
        changed += 1
        log.append((tag, new))
        out.append(f'{indent}- {new}\n')
    if changed == 0:
        return path, 0, []
    new_head = ''.join(out)
    new_text = text[:m.start(1)] + new_head + text[m.end(1):]
    if apply:
        if basin is not None:
            bak = basin / (str(path).replace('/', '__') + '.bak')
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
    basin = Path(args.backup_dir) if args.backup_dir else None
    if args.apply and basin is not None:
        basin.mkdir(parents=True, exist_ok=True)
    print(f'Law pairs ({len(LAW_PAIRS)}): {sorted(LAW_PAIRS)}')
    print(f'Matrix pairs ({len(MATRIX_PAIRS)}): {sorted(MATRIX_PAIRS)}')
    overlap = LAW_PAIRS & MATRIX_PAIRS
    print(f'OVERLAP law&matrix pairs (must be empty): {sorted(overlap) if overlap else "NONE"}')
    touched = instances = 0
    agg = {}
    for p in root.rglob('*.md'):
        if '.git' in p.parts:
            continue
        _, ch, log = transform(p, args.apply, basin)
        if ch:
            touched += 1
            instances += ch
            for a, b in log:
                agg[a] = b
    mode = 'APPLIED' if args.apply else 'DRY-RUN'
    print(f'\n[{mode}] files: {touched}, instances: {instances}')
    if not args.apply:
        print('Classification report (old -> new):')
        for a in sorted(agg):
            print(f'   {a:<32} -> {agg[a]}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
