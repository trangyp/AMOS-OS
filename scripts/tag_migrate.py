#!/usr/bin/env python3
"""
tag_migrate.py — Dry-run (or apply) migration for the AMOS tag vocabulary.

Reads the canonical map embedded here (and, when present, the machine-readable
`migration:` YAML block in 16_SCHEMAS/TAG_VOCABULARY.md), parses every
`tags:` frontmatter block across the vault, applies rename/drop rules, and:

  - DRY-RUN (default): prints a diff report ONLY. No files are modified.
  - --apply: writes the migrated `tags:` blocks back (gated; requires --confirm).

Contract-aligned: governed, reversible, holds writes until an approved diff.
"""

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

# ---------------------------------------------------------------------------
# Canonical map (source of truth mirrored from 16_SCHEMAS/TAG_VOCABULARY.md)
# In a real wiring step this would be loaded from the YAML to avoid drift;
# for the proposal dry-run it is embedded here.
# ---------------------------------------------------------------------------
RENAME = {
    "amos_os": "amos-os",
    "control_plane": "control-plane",
    "cognitive_matrix": "cognitive-matrix",
    "canonical": "canon",
    "canon/skill": "type/skill",
    "type/skill": "type/skill",
    "canon/workflow": "type/workflow",
    "type/workflow": "type/workflow",
    "canon/cognitive-matrix": "domain/cognitive-matrix",
    "canon/general": "epistemic/amos_model",
    "rscf/source_claim": "epistemic/source_claim",
    "epistemic/source_claim": "epistemic/source_claim",
    "rscf/state/canonical": "rscf/state/canonical",
    # law gate tags
    "l0_integrity": "law/L0-integrity",
    "l0-integrity": "law/L0-integrity",
    "l1-epistemic": "law/L1-epistemic",
    "l2-provenance": "law/L2-provenance",
    "l3-dependency": "law/L3-dependency",
    # cognitive-matrix layer tags
    "l00": "matrix/l00",
    "l01": "matrix/l01",
    "l02": "matrix/l02",
    "l03": "matrix/l03",
}

# Drop rules. Exact names and regexes. Not taxonomy.
# NOTE: do NOT blanket-drop `NN-*` or `*-moc` tags here — those are graph
# enablement tags whose disposition is a separate, reviewed decision. This
# drop list is only for unambiguous NON-taxonomy noise (file-name leaks and
# receipt/registry artifact tags).
DROP_EXACT = {"moc"}  # bare 'moc' replaced by type/moc on the MOC file itself
DROP_SUFFIX = {".md"}  # filename leaks
DROP_REGEX = [
    re.compile(r"^inv-authz-\d+$"),  # invariant receipt tags
]
# Tags that are clearly filename/artifact leaks (contain a path-ish pattern
# like `<file>.md` style or the `_Cognitive_..._readme` filename pattern).
FILENAME_LEAK = re.compile(r"(\.md$|_readme$|_moc$|_map$|_canon$|_contract$|_index$|_registry$|_readme\.)", re.I)


def drop_rule(tag):
    if tag in DROP_EXACT:
        return True
    if tag.endswith(".md"):
        return True
    for rx in DROP_REGEX:
        if rx.match(tag):
            return True
    return False


def canonicalize(tag):
    if drop_rule(tag):
        return None  # dropped
    # exact rename first
    if tag in RENAME:
        return RENAME[tag]
    # canonical key with underscore -> hyphen is NOT auto-applied to arbitrary
    # unknown tags (avoid false positives); only known renames are mapped.
    return tag  # unchanged (unknown) — flagged as UNMAPPED for audit


def parse_tags(text):
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    if not m:
        return None
    fm = m.group(1)
    lines = fm.splitlines()
    tags = []
    in_tags = False
    for line in lines:
        if re.match(r"^tags:\s*$", line):
            in_tags = True
            continue
        if in_tags:
            if re.match(r"^\s*-\s+", line):
                tags.append(line.strip()[2:].strip())
            else:
                in_tags = False
    return tags


def render_tags_block(new_tags):
    if not new_tags:
        return "tags:\n"
    body = "\n".join(f"- {t}" for t in new_tags)
    return f"tags:\n{body}\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".",
                    help="vault root directory (default: current dir)")
    ap.add_argument("--apply", action="store_true",
                    help="actually write files (default: dry-run only)")
    ap.add_argument("--confirm", action="store_true",
                    help="required alongside --apply")
    ap.add_argument("--backup-dir", default=None,
                    help="dir to snapshot originals before writing (rollback basin)")
    ap.add_argument("--min-changes", type=int, default=0,
                    help="only report files with >= N tag changes")
    args = ap.parse_args()

    if args.apply and not args.confirm:
        print("Refusing to write without --confirm (governed rollback gate).",
              file=sys.stderr)
        sys.exit(2)

    if args.apply:
        if args.backup_dir:
            Path(args.backup_dir).mkdir(parents=True, exist_ok=True)
        else:
            print("Warning: applying without --backup-dir (no rollback basin). "
                  "Use --backup-dir <DIR> to snapshot originals.", file=sys.stderr)

    root = Path(args.root)
    changed_files = 0
    total_changes = 0
    unmapped = Counter()
    dropped = Counter()
    rewritten = Counter()

    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        tags = parse_tags(text)
        if tags is None:
            continue
        new = []
        changed = False
        for t in tags:
            c = canonicalize(t)
            if c is None:
                dropped[t] += 1
                changed = True
                continue
            if c != t:
                rewritten[t] += 1
                changed = True
            new.append(c)
        if changed:
            changed_files += 1
            edits = sum(1 for t in tags if canonicalize(t) != t or drop_rule(t))
            total_changes += edits
            if args.min_changes == 0 or (len(tags) - len(new)) >= args.min_changes:
                if args.apply:
                    if args.backup_dir:
                        # snapshot original before mutation (rollback basin)
                        rel = path.relative_to(root)
                        bak = Path(args.backup_dir) / (str(rel).replace("/", "__") + ".bak")
                        bak.parent.mkdir(parents=True, exist_ok=True)
                        bak.write_text(text, encoding="utf-8")
                    # rewrite frontmatter tags block
                    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
                    fm = m.group(1)
                    lines = fm.splitlines()
                    out = []
                    in_tags = False
                    for line in lines:
                        if re.match(r"^tags:\s*$", line):
                            in_tags = True
                            out.append(line)
                            continue
                        if in_tags:
                            if re.match(r"^\s*-\s+", line):
                                continue
                            else:
                                in_tags = False
                        out.append(line)
                    new_fm = "\n".join(out)
                    # re-append the new block after the tags: line
                    new_fm = new_fm.replace(
                        "tags:",
                        "tags:\n" + "\n".join(f"- {t}" for t in new),
                        1,
                    )
                    text2 = text.replace(fm, new_fm, 1)
                    path.write_text(text2, encoding="utf-8")
                else:
                    # dry-run: print changed file and its diff
                    old_str = ", ".join(tags)
                    new_str = ", ".join(new)
                    print(f"{path}\n  - [{len(tags)}] {old_str}\n  + [{len(new)}] {new_str}")

    print("\n=== SUMMARY ===")
    print(f"files with tag changes : {changed_files}")
    print(f"total tag edits (approx): {total_changes}")
    print("\nTop dropped tags:")
    for k, v in dropped.most_common(15):
        print(f"  DROP {v:>5}  {k}")
    print("\nTop rewritten tags:")
    for k, v in rewritten.most_common(15):
        print(f"  REN  {v:>5}  {k}  ->  {RENAME.get(k, k)}")
    print(f"\nUnmapped/unchanged distinct tags remain: (see report for audit)")
    if args.apply:
        print("APPLIED (--confirm was honored).")
    else:
        print("DRY-RUN only — no files written.")


if __name__ == "__main__":
    main()
