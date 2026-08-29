#!/usr/bin/env python3
"""Canonicalize missing `rscf.state` in AMOS SKILL.md files.

Uses the existing frontmatter fields (`provenance`, `epistemic_class`, `rscf_state`,
`source`) to choose the weakest accurate RSCF state, then injects an `rscf:` block
or `state:` field.  Only modifies files where `rscf.state` is missing.
"""

from __future__ import annotations

import argparse
import re
import sys
import yaml
from pathlib import Path


ALLOWED_RSCF_STATES = (
    "SOURCE_CANON", "SOURCE_CLAIM", "OBSERVATION", "DERIVED",
    "AMOS_MODEL", "DOMAIN_EMPIRICAL", "VERIFIED", "CONDITIONAL",
    "COMPETING", "UNKNOWN/GAP",
)


def _infer_state(fm: dict, source_dir: str) -> str:
    """Infer the weakest accurate rscf.state from existing frontmatter."""
    # 1. Existing top-level legacy rscf_state
    legacy = str(fm.get("rscf_state", "")).strip()
    if legacy in ALLOWED_RSCF_STATES:
        return legacy

    # 2. Existing epistemic_class if it is a valid rscf state
    epistemic = str(fm.get("epistemic_class", "")).strip()
    if epistemic in ALLOWED_RSCF_STATES:
        return epistemic

    # 3. Provenance-driven
    provenance = str(fm.get("provenance", "")).lower()
    if "arxiv" in provenance or provenance.startswith(("arxiv", "http")):
        return "SOURCE_CLAIM"
    if "amos_canon" in provenance or "canon" in str(fm.get("source", "")).lower():
        return "AMOS_MODEL"
    if "amos_corpus" in provenance or "am.os" in provenance:
        return "DERIVED"

    # 4. Source path-driven
    source = str(fm.get("source", "")).lower()
    if source.startswith("01_canon"):
        return "AMOS_MODEL"
    if any(source.startswith(p) for p in ("02_kernel", "07_skills", "11_knowledge", "25_cognitive_matrix")):
        return "DERIVED"
    if "arxiv" in source:
        return "SOURCE_CLAIM"

    # 5. Default based on runtime tree
    if source_dir == ".devin/skills":
        name = str(fm.get("name", "")).lower()
        if name.startswith(("arxiv-", "amos-07")) or "arxiv" in name:
            return "SOURCE_CLAIM"
    return "DERIVED"


def _canonicalize_skill(skill_md: Path, dry_run: bool) -> tuple[bool, str]:
    txt = skill_md.read_text(encoding="utf-8", errors="replace")
    m = re.match(r"^(---\s*\n)(.*?\n)(---\s*\n)(.*)$", txt, re.DOTALL)
    if not m:
        return False, "no frontmatter"

    try:
        fm = yaml.safe_load(m.group(2)) or {}
    except yaml.YAMLError as e:
        return False, f"yaml_error: {e}"

    rscf = fm.get("rscf") or {}
    if rscf and rscf.get("state"):
        return False, "rscf.state present"

    state = _infer_state(fm, skill_md.parents[1].name if len(skill_md.parents) > 1 else "")
    claim_class = rscf.get("claim_class") if rscf else None
    provenance = rscf.get("provenance") if rscf else None
    scope = rscf.get("scope") if rscf else None

    # Fallback values
    if not claim_class:
        claim_class = state
    if not provenance:
        provenance = fm.get("provenance") or "AMOS_corpus"
    if not scope:
        scope = "AMOS_general"

    new_rscf = {
        "state": state,
        "claim_class": claim_class,
        "provenance": provenance,
        "scope": scope,
    }
    # Preserve any other existing rscf keys
    if rscf:
        for k, v in rscf.items():
            if k not in new_rscf:
                new_rscf[k] = v

    # Serialize rscf block manually to avoid full-frontmatter re-dump
    rscf_yaml = "rscf:\n" + "".join(f"  {k}: {v}\n" for k, v in new_rscf.items())

    if "rscf:" in m.group(2):
        # Replace the existing rscf: block, preserving the rest of the frontmatter
        fm_txt = m.group(2)
        # Regex: from rscf: to the next top-level key (no indent) or end of frontmatter
        pattern = re.compile(r"^(rscf:\s*\n(?:\s+.*?\n)*?)(?=\n\w|[\r\n]?$)", re.MULTILINE)
        new_fm = pattern.sub(rscf_yaml.rstrip() + "\n", fm_txt, count=1)
        if new_fm == fm_txt:  # fallback if regex fails
            new_fm = re.sub(r"rscf:.*?(?=\n\w|\n---)", rscf_yaml.rstrip() + "\n", fm_txt, count=1, flags=re.DOTALL)
        full = f"{m.group(1)}{new_fm}{m.group(3)}{m.group(4)}"
    else:
        # Insert rscf block just before the closing ---
        fm_txt = m.group(2)
        new_fm = fm_txt.rstrip() + "\n" + rscf_yaml
        full = f"{m.group(1)}{new_fm}{m.group(3)}{m.group(4)}"

    if not dry_run:
        skill_md.write_text(full, encoding="utf-8")
    return True, f"set rscf.state={state}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Canonicalize rscf.state in SKILL.md files")
    parser.add_argument("roots", nargs="+", type=Path, help="Skill roots (e.g. 07_SKILLS .devin/skills)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would change without writing")
    args = parser.parse_args(argv)

    changed: list[tuple[str, str, str]] = []
    for root in args.roots:
        if not root.exists():
            print(f"SKIP: {root} does not exist", file=sys.stderr)
            continue
        for skill_dir in root.iterdir():
            if not skill_dir.is_dir():
                continue
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue
            did, msg = _canonicalize_skill(skill_md, args.dry_run)
            if did:
                changed.append((str(root), skill_dir.name, msg))

    print(f"{'WOULD CHANGE' if args.dry_run else 'CHANGED'}: {len(changed)} files")
    for root, name, msg in changed:
        print(f"  {root}/{name} -> {msg}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
