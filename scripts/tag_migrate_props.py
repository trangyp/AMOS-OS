#!/usr/bin/env python3
"""
tag_migrate_props.py — Pass 2: move graph-enablement tags to properties (Option A).

Strips CONTENT tags that are pure graph-federation / filename-mirror noise and
expresses the information as frontmatter properties or existing wikilinks:

  - `*-moc`            -> remove from content tags; add `moc: true` property on
                         files that are genuine MOCs (type: moc), else drop.
  - `00-*`             -> remove (roots are expressed by [[00_HOME]] links / type:)
  - `index-*`          -> remove (fold into type: listed per-file)
  - `amos-rscf-nodes`  -> remove (RSCF relations live in the RSCF-NODE block)

Does NOT touch the explicit OUT-of-scope families (-readme/-map/-contract/
-registry/-canon and lNN law-gate keep/drop) — those need separate sign-off.

DRY-RUN by default (prints stats, writes nothing).
--apply --confirm --backup-dir <DIR> writes, snapshotting originals for rollback.
"""

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

# Families to strip from content tags (Pass 2 / Option A)
DROP_NAMESPACE_PREFIX = ("00-", "index-")
DROP_EXACT = {"amos-rscf-nodes"}
DROP_SUFFIX = ("-moc",)


def is_drop_tag(t):
    if t in DROP_EXACT:
        return True
    if t.startswith(DROP_NAMESPACE_PREFIX):
        return True
    if t.endswith(DROP_SUFFIX):
        return True
    return False


def is_genuine_moc(text, path=None):
    """A file is a genuine MOC if its frontmatter declares type: moc, OR its
    filename follows the MOC convention (_MOC / MOC). Calibrated across the vault:
    type-only=1021, filename-only adds ~43, combined=1064 genuine MOCs."""
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    if m and re.search(r"^type:\s*moc\b", m.group(1), re.M):
        return True
    if path is not None:
        stem = Path(path).stem.upper()
        if "_MOC" in stem or stem == "MOC":
            return True
    return False


def parse_frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    if not m:
        return None, None
    return m.group(1), m.group(0)


def strip_tags_from_fm(fm, is_moc):
    """Return (new_fm_without_graph_tags, dropped_list, should_add_moc_prop)."""
    lines = fm.splitlines()
    out = []
    in_tags = False
    dropped = []
    found_tags = False
    for line in lines:
        if re.match(r"^tags:\s*$", line):
            in_tags = True
            found_tags = True
            out.append(line)
            continue
        if in_tags:
            if re.match(r"^\s*-\s+", line):
                t = line.strip()[2:].strip()
                if is_drop_tag(t):
                    dropped.append(t)
                    continue
                else:
                    out.append(line)
            else:
                in_tags = False
                out.append(line)
            continue
        out.append(line)

    new_fm = "\n".join(out)
    # If every tag was dropped, the tags: block may be left empty -> normalize to
    # "tags:" header only (valid YAML empty list). Actually preserve as-is; an empty
    # mulitline list "tags:\n" parses as None, which is fine for Obsidian.
    add_moc = is_moc and "moc: true" not in fm and "moc: true" not in new_fm
    return new_fm, dropped, add_moc


def add_property(fm, key, val):
    if re.search(rf"^{re.escape(key)}:", fm, re.M):
        return fm
    lines = fm.splitlines()
    # insert after the opening keys, before rscf: block if present, else end
    idx = 0
    for i, l in enumerate(lines):
        if re.match(r"^[a-z_][a-z0-9_]*:\s*$", l) or re.match(r"^[a-z_][a-z0-9_]*:", l):
            if re.match(r"^rscf:", l):
                idx = i
                break
            idx = i + 1
    lines.insert(idx, f"{key}: {val}")
    return "\n".join(lines)


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
    moc_props_added = 0
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

        is_moc = is_genuine_moc(text, path=path)
        new_fm, dropped, add_moc = strip_tags_from_fm(fm, is_moc)
        if add_moc:
            new_fm = add_property(new_fm, "moc", "true")

        if new_fm != fm:
            changed += 1
            for d in dropped:
                tag_drops[d] += 1
            if add_moc:
                moc_props_added += 1
            if not args.apply:
                if len(examples) < 25:
                    examples.append(f"{path}: -{len(dropped)} tags" +
                                    (f" +moc:true" if add_moc else ""))
            else:
                text2 = text.replace(block, "---\n" + new_fm + "\n---", 1)
                if args.backup_dir:
                    rel = str(path.relative_to(root)).replace("/", "__") + ".bak"
                    bakp = Path(args.backup_dir) / rel
                    bakp.parent.mkdir(parents=True, exist_ok=True)
                    bakp.write_text(text, encoding="utf-8")
                path.write_text(text2, encoding="utf-8")

    print(f"files changed: {changed}")
    print(f"moc:true properties added: {moc_props_added}")
    print("\nTop dropped tags:")
    for k, v in tag_drops.most_common(25):
        print(f"  DROP {v:>6}  {k}")
    if examples:
        print("\nSample changed files (dry-run):")
        for e in examples:
            print("  " + e)
    if args.apply:
        print("APPLIED (--confirm honored).")
    else:
        print("DRY-RUN only — no files written.")


if __name__ == "__main__":
    main()
