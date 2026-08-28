#!/usr/bin/env python3
"""
Normalize frontmatter across all skills, agents, workflows.

User's pattern (from .agents/skills/ and 07_SKILLS/amos-c05-mind-behavior-master):
1. Remove blank lines within YAML frontmatter
2. Remove duplicate metadata fields from rscf: nested block
   (hml_level, gmef_gates, collapse_class, qfm_gate_set, law_compliance
   should only appear at top level, not inside rscf:)
3. Unquote string values where safe (title, version, description)
4. Ensure blank line after frontmatter closing ---
"""

import json
import re
import yaml
from pathlib import Path

VAULT = Path("/Users/mac/Documents/AMOS_OS")
SKILLS_DIR = VAULT / "07_SKILLS"
AGENTS_DIR = VAULT / "06_AGENTS"
WORKFLOWS_DIR = VAULT / "08_WORKFLOWS"

# Fields that should NOT be duplicated inside rscf: block
TOP_LEVEL_ONLY_FIELDS = {
    "hml_level", "gmef_gates", "collapse_class", "qfm_gate_set", "law_compliance",
    "origin_architect", "epistemic_class", "version", "rscf_state",
    "parent_skill", "domain",
}


def clean_frontmatter_blanks(text: str) -> str:
    """Remove blank lines within YAML frontmatter."""
    if not text.startswith("---"):
        return text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return text

    fm_text = parts[1]
    # Remove blank lines from frontmatter
    fm_lines = fm_text.split("\n")
    fm_lines = [line for line in fm_lines if line.strip() != ""]
    fm_text = "\n".join(fm_lines)
    if not fm_text.endswith("\n"):
        fm_text += "\n"

    # Ensure blank line after closing ---
    body = parts[2]
    if body.startswith("\n"):
        body = body.lstrip("\n")
        body = "\n" + body

    return f"---\n{fm_text}---\n{body}"


def remove_duplicate_fields_from_rscf(fm: dict) -> bool:
    """Remove top-level fields that are duplicated inside rscf: block."""
    if not isinstance(fm, dict):
        return False
    rscf = fm.get("rscf")
    if not isinstance(rscf, dict):
        return False

    changed = False
    for field in TOP_LEVEL_ONLY_FIELDS:
        if field in rscf:
            del rscf[field]
            changed = True

    # If rscf is now empty, remove it
    if not rscf:
        del fm["rscf"]
        changed = True

    return changed


def normalize_skills():
    """Normalize frontmatter in all skills."""
    normalized = 0
    for sd in SKILLS_DIR.iterdir():
        if not sd.is_dir() or not (sd / "SKILL.md").exists():
            continue
        skill_path = sd / "SKILL.md"
        text = skill_path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue

        original = text

        # Step 1: Parse and clean rscf block
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        try:
            fm = yaml.safe_load(parts[1])
            if not isinstance(fm, dict):
                continue
        except yaml.YAMLError:
            continue

        rscf_changed = remove_duplicate_fields_from_rscf(fm)

        if rscf_changed:
            new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False, width=100)
            text = f"---\n{new_fm}---\n{parts[2]}"

        # Step 2: Remove blank lines in frontmatter
        text = clean_frontmatter_blanks(text)

        if text != original:
            skill_path.write_text(text, encoding="utf-8")
            normalized += 1

    return normalized


def normalize_workflows():
    """Normalize frontmatter in all workflows."""
    normalized = 0
    for wf in WORKFLOWS_DIR.glob("*.md"):
        if "MOC" in wf.stem or "README" in wf.stem or "CONTRACT" in wf.stem:
            continue
        text = wf.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue

        original = text

        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        try:
            fm = yaml.safe_load(parts[1])
            if not isinstance(fm, dict):
                continue
        except yaml.YAMLError:
            continue

        rscf_changed = remove_duplicate_fields_from_rscf(fm)

        if rscf_changed:
            new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False, width=100)
            text = f"---\n{new_fm}---\n{parts[2]}"

        text = clean_frontmatter_blanks(text)

        if text != original:
            wf.write_text(text, encoding="utf-8")
            normalized += 1

    return normalized


def normalize_agents():
    """Normalize agents — they're JSON, so just ensure no duplicate fields."""
    # Agents are JSON, no frontmatter blank line issues
    # But check for duplicate fields in nested objects
    normalized = 0
    for af in AGENTS_DIR.glob("*.json"):
        try:
            agent = json.loads(af.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue

        changed = remove_duplicate_fields_from_rscf(agent)

        if changed:
            af.write_text(json.dumps(agent, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            normalized += 1

    return normalized


if __name__ == "__main__":
    print("Normalizing frontmatter across all artifacts...")
    print("  - Remove blank lines within frontmatter")
    print("  - Remove duplicate fields from rscf: blocks")
    print("  - Ensure blank line after closing ---")
    print()

    skills = normalize_skills()
    print(f"Skills normalized: {skills}")

    workflows = normalize_workflows()
    print(f"Workflows normalized: {workflows}")

    agents = normalize_agents()
    print(f"Agents normalized: {agents}")

    total = skills + workflows + agents
    print(f"\nTotal files normalized: {total}")
