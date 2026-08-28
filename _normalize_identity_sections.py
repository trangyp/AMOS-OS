#!/usr/bin/env python3
"""
Normalize ## Identity sections to user's compact format and sync from .agents/skills/.

User's new format (from .agents/skills/):
  ## Identity

  Origin architect: **Trang Phan**. Domain: canon. Parent: amos-canon-universe-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.

This script:
1. Reads frontmatter (origin_architect, domain, parent_skill, epistemic_class, hml_level)
2. Replaces/inserts ## Identity with the compact format
3. Syncs 10 user-edited skills from .agents/skills/ to 07_SKILLS/
"""

import re
import yaml
from pathlib import Path

VAULT = Path("/Users/mac/Documents/AMOS_OS")
SKILLS_DIR = VAULT / "07_SKILLS"
AGENTS_SKILLS_DIR = VAULT / ".agents/skills"


def generate_identity_line(fm: dict) -> str:
    """Generate the compact Identity line from frontmatter."""
    origin = fm.get("origin_architect", "Trang Phan")
    domain = fm.get("domain", "unknown")
    parent = fm.get("parent_skill", "none")
    epistemic = fm.get("epistemic_class", "SOURCE_CLAIM")
    hml = fm.get("hml_level", "M")

    return (f"Origin architect: **{origin}**. Domain: {domain}. "
            f"Parent: {parent}. Epistemic class: {epistemic}. H/M/L: {hml}.")


def normalize_identity_section(text: str, fm: dict) -> str:
    """Replace or insert ## Identity section with compact format."""
    identity_line = generate_identity_line(fm)
    new_section = f"## Identity\n\n{identity_line}\n"

    # Check if ## Identity exists
    identity_pattern = re.compile(r'## Identity\s*\n.*?(?=\n## |\Z)', re.DOTALL)

    if identity_pattern.search(text):
        # Replace existing
        text = identity_pattern.sub(new_section.rstrip(), text)
    else:
        # Insert after first # heading (before ## When to Use if it exists)
        when_to_use_pattern = re.compile(r'(## When to Use\s*\n)')
        if when_to_use_pattern.search(text):
            text = when_to_use_pattern.sub(new_section + r'\1', text, count=1)
        else:
            # Insert after the first # heading
            heading_pattern = re.compile(r'^(# .+)$', re.MULTILINE)
            m = heading_pattern.search(text)
            if m:
                insert_pos = m.end()
                text = text[:insert_pos] + "\n\n" + new_section + text[insert_pos:]

    return text


def sync_from_agents_skills():
    """Sync ## Identity and ## When to Use from .agents/skills/ to 07_SKILLS/."""
    synced = 0
    for sd in AGENTS_SKILLS_DIR.iterdir():
        if not sd.is_dir() or not (sd / "SKILL.md").exists():
            continue
        agents_text = (sd / "SKILL.md").read_text(encoding="utf-8")

        # Extract ## Identity and ## When to Use from .agents/skills/
        agents_identity = re.search(r'## Identity\s*\n(.*?)(?=\n## |\Z)', agents_text, re.DOTALL)
        agents_when = re.search(r'## When to Use\s*\n(.*?)(?=\n## |\Z)', agents_text, re.DOTALL)

        if not agents_identity:
            continue

        # Sync to 07_SKILLS/
        skill_path = SKILLS_DIR / sd.name / "SKILL.md"
        if not skill_path.exists():
            continue

        skill_text = skill_path.read_text(encoding="utf-8")
        original = skill_text

        # Replace ## Identity
        identity_pattern = re.compile(r'## Identity\s*\n.*?(?=\n## |\Z)', re.DOTALL)
        if identity_pattern.search(skill_text):
            skill_text = identity_pattern.sub(agents_identity.group(0).rstrip(), skill_text)
        else:
            # Insert before ## When to Use
            when_pattern = re.compile(r'(## When to Use\s*\n)')
            if when_pattern.search(skill_text):
                skill_text = when_pattern.sub(agents_identity.group(0).rstrip() + "\n\n" + r'\1', skill_text, count=1)

        # Replace ## When to Use if user has a better version
        if agents_when:
            when_pattern = re.compile(r'## When to Use\s*\n.*?(?=\n## |\Z)', re.DOTALL)
            if when_pattern.search(skill_text):
                skill_text = when_pattern.sub(agents_when.group(0).rstrip(), skill_text)

        if skill_text != original:
            skill_path.write_text(skill_text, encoding="utf-8")
            synced += 1

    return synced


def normalize_all_skills():
    """Normalize ## Identity in all 07_SKILLS/."""
    normalized = 0
    for sd in SKILLS_DIR.iterdir():
        if not sd.is_dir() or not (sd / "SKILL.md").exists():
            continue
        skill_path = sd / "SKILL.md"
        text = skill_path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        try:
            fm = yaml.safe_load(parts[1])
            if not isinstance(fm, dict):
                continue
        except yaml.YAMLError:
            continue

        body = parts[2]
        new_body = normalize_identity_section(body, fm)

        if new_body != body:
            new_text = f"---{parts[1]}---{new_body}"
            skill_path.write_text(new_text, encoding="utf-8")
            normalized += 1

    return normalized


if __name__ == "__main__":
    print("Step 1: Syncing user-edited skills from .agents/skills/ to 07_SKILLS/...")
    synced = sync_from_agents_skills()
    print(f"  Synced: {synced}")

    print("\nStep 2: Normalizing ## Identity sections in all remaining skills...")
    normalized = normalize_all_skills()
    print(f"  Normalized: {normalized}")

    print(f"\nTotal: {synced + normalized} skills updated")
