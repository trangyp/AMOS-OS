#!/usr/bin/env python3
"""
Apply user's new minimal tag pattern to all skills, agents, workflows.

User's pattern (from .agents/skills/):
  tags:
    - type/skill
    - canon/skill
    - domain/<domain-tag>
    - rscf/<rscf_state_lowercase>
    - hml/<hml_level_lowercase>
    - epistemic/<epistemic_class_lowercase>
    - amos_os

Also:
  - Convert gmef_gates and law_compliance to block-style YAML lists
  - Remove quotes from version
  - Sync .agents/skills/ to 07_SKILLS/
"""

import json
import re
import yaml
from pathlib import Path

VAULT = Path("/Users/mac/Documents/AMOS_OS")
SKILLS_DIR = VAULT / "07_SKILLS"
AGENTS_DIR = VAULT / "06_AGENTS"
WORKFLOWS_DIR = VAULT / "08_WORKFLOWS"
AGENTS_SKILLS_DIR = VAULT / ".agents/skills"

# Domain → domain tag mapping (from user's pattern + inferred)
DOMAIN_TAG_MAP = {
    "canon": "canon-universe",
    "agent": "agent-systems",
    "society": "society-culture",
    "formal": "formal-engines",
    "strategy": "strategy-game",
    "bio": "bio-neuro",
    "runtime": "os-runtime",
    "knowledge": "knowledge-research",
    "arxiv": "knowledge-research",
    "c01": "meta-logic",
    "c02": "physics-cosmos",
    "c03": "physics-cosmos",
    "c04": "bio-neuro",
    "c05": "mind-behavior",
    "c06": "society-culture",
    "c07": "econ-finance",
    "c08": "strategy-game",
    "c09": "org-law-policy",
    "c10": "tech-engineering",
    "c11": "design-language",
    "c12": "earth-ecology",
    "rscf": "rscf-epistemic",
    "mckinsey": "strategy-game",
    "audit": "audit-repair",
    "fx": "econ-finance",
    "econ": "econ-finance",
    "boundary": "boundary-scope",
    "security": "security-safety",
    "causal": "causal-reasoning",
    "memory": "memory-systems",
    "super": "super-engines",
    "info": "information-theory",
    "information": "information-theory",
    "fractal": "fractal-systems",
    "trang": "trang-framework",
    "skill": "skill-systems",
    "workflow": "os-runtime",
    "mind_behavior": "mind-behavior",
    "cross-domain": "cross-domain",
}


def get_domain_tag(domain: str) -> str:
    """Get domain tag from domain field."""
    if not domain:
        return "cross-domain"
    d = domain.lower().strip()
    if d in DOMAIN_TAG_MAP:
        return DOMAIN_TAG_MAP[d]
    # Handle cross-domain variants
    if "cross-domain" in d:
        return "cross-domain"
    # Default: use domain as-is
    return d.replace("_", "-")


def build_minimal_tags(fm: dict, artifact_type: str = "skill") -> list:
    """Build the minimal 7-tag set from frontmatter."""
    domain = fm.get("domain", "")
    rscf_state = fm.get("rscf_state", "SOURCE_CLAIM")
    hml_level = fm.get("hml_level", "M")
    epistemic_class = fm.get("epistemic_class", "SOURCE_CLAIM")

    domain_tag = get_domain_tag(domain)
    rscf_tag = f"rscf/{rscf_state.lower()}"
    hml_tag = f"hml/{hml_level.lower()}"
    epistemic_tag = f"epistemic/{epistemic_class.lower()}"

    return [
        f"type/{artifact_type}",
        f"canon/{artifact_type}",
        f"domain/{domain_tag}",
        rscf_tag,
        hml_tag,
        epistemic_tag,
        "amos_os",
    ]


def normalize_yaml_dump(fm: dict) -> str:
    """Dump YAML in the user's preferred format (block-style lists, no quotes on version)."""
    # Ensure version is not quoted
    if "version" in fm:
        v = fm["version"]
        if isinstance(v, str):
            # Try to make it a plain scalar
            try:
                fm["version"] = str(float(v)) if "." in v else int(v)
            except (ValueError, TypeError):
                pass

    # Dump with block style
    return yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False, width=100)


def apply_to_skills():
    """Apply minimal tags to all 07_SKILLS/."""
    enhanced = 0
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

        # Check if already has minimal tags (type/skill + amos_os + no canon-group)
        existing_tags = fm.get("tags", [])
        if isinstance(existing_tags, str):
            existing_tags = [existing_tags]
        if not isinstance(existing_tags, list):
            existing_tags = []

        has_minimal = ("type/skill" in existing_tags and "amos_os" in existing_tags
                       and not any(t.startswith("canon-group/") for t in existing_tags)
                       and not any(t.startswith("topic/") for t in existing_tags)
                       and not any(t.startswith("capability/") for t in existing_tags)
                       and not any(t.startswith("sota/") for t in existing_tags))

        if has_minimal:
            continue

        # Build new minimal tags
        new_tags = build_minimal_tags(fm, "skill")
        fm["tags"] = new_tags

        new_fm = normalize_yaml_dump(fm)
        new_text = f"---\n{new_fm}---\n{parts[2]}"
        skill_path.write_text(new_text, encoding="utf-8")
        enhanced += 1

    return enhanced


def apply_to_agents():
    """Apply minimal tags to all 06_AGENTS/."""
    enhanced = 0
    for af in AGENTS_DIR.glob("*.json"):
        try:
            agent = json.loads(af.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue

        existing_tags = agent.get("tags", [])
        if isinstance(existing_tags, str):
            existing_tags = [existing_tags]
        if not isinstance(existing_tags, list):
            existing_tags = []

        has_minimal = ("type/agent" in existing_tags and "amos_os" in existing_tags
                       and not any(t.startswith("canon-group/") for t in existing_tags)
                       and not any(t.startswith("topic/") for t in existing_tags)
                       and not any(t.startswith("capability/") for t in existing_tags)
                       and not any(t.startswith("sota/") for t in existing_tags))

        if has_minimal:
            continue

        new_tags = build_minimal_tags(agent, "agent")
        agent["tags"] = new_tags

        af.write_text(json.dumps(agent, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        enhanced += 1

    return enhanced


def apply_to_workflows():
    """Apply minimal tags to all 08_WORKFLOWS/."""
    enhanced = 0
    for wf in WORKFLOWS_DIR.glob("*.md"):
        if "MOC" in wf.stem or "README" in wf.stem or "CONTRACT" in wf.stem:
            continue
        text = wf.read_text(encoding="utf-8")
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

        existing_tags = fm.get("tags", [])
        if isinstance(existing_tags, str):
            existing_tags = [existing_tags]
        if not isinstance(existing_tags, list):
            existing_tags = []

        has_minimal = ("type/workflow" in existing_tags and "amos_os" in existing_tags
                       and not any(t.startswith("canon-group/") for t in existing_tags)
                       and not any(t.startswith("topic/") for t in existing_tags)
                       and not any(t.startswith("capability/") for t in existing_tags)
                       and not any(t.startswith("sota/") for t in existing_tags))

        if has_minimal:
            continue

        new_tags = build_minimal_tags(fm, "workflow")
        fm["tags"] = new_tags

        new_fm = normalize_yaml_dump(fm)
        new_text = f"---\n{new_fm}---\n{parts[2]}"
        wf.write_text(new_text, encoding="utf-8")
        enhanced += 1

    return enhanced


def sync_from_agents_skills():
    """Sync .agents/skills/ frontmatter to 07_SKILLS/."""
    synced = 0
    for sd in AGENTS_SKILLS_DIR.iterdir():
        if not sd.is_dir() or not (sd / "SKILL.md").exists():
            continue
        agents_text = (sd / "SKILL.md").read_text(encoding="utf-8")
        if not agents_text.startswith("---"):
            continue
        agents_parts = agents_text.split("---", 2)
        if len(agents_parts) < 3:
            continue
        try:
            agents_fm = yaml.safe_load(agents_parts[1])
            if not isinstance(agents_fm, dict) or "rscf_state" not in agents_fm:
                continue
        except:
            continue

        # Check if .agents/skills/ version has minimal tags
        agents_tags = agents_fm.get("tags", [])
        if isinstance(agents_tags, str):
            agents_tags = [agents_tags]
        if not isinstance(agents_tags, list):
            agents_tags = []

        has_minimal = ("type/skill" in agents_tags and "amos_os" in agents_tags
                       and not any(t.startswith("canon-group/") for t in agents_tags))

        if not has_minimal:
            continue

        # Sync to 07_SKILLS/
        skill_path = SKILLS_DIR / sd.name / "SKILL.md"
        if not skill_path.exists():
            continue

        skill_text = skill_path.read_text(encoding="utf-8")
        if not skill_text.startswith("---"):
            continue
        skill_parts = skill_text.split("---", 2)
        if len(skill_parts) < 3:
            continue
        try:
            skill_fm = yaml.safe_load(skill_parts[1])
            if not isinstance(skill_fm, dict):
                continue
        except:
            continue

        # Copy tags and formatting fields from .agents/skills/
        changed = False
        for field in ["tags", "description", "version", "gmef_gates", "law_compliance"]:
            if field in agents_fm and agents_fm[field] != skill_fm.get(field):
                skill_fm[field] = agents_fm[field]
                changed = True

        if changed:
            new_fm = normalize_yaml_dump(skill_fm)
            new_text = f"---\n{new_fm}---\n{skill_parts[2]}"
            skill_path.write_text(new_text, encoding="utf-8")
            synced += 1

    return synced


if __name__ == "__main__":
    print("Step 1: Syncing user-edited skills from .agents/skills/ to 07_SKILLS/...")
    synced = sync_from_agents_skills()
    print(f"  Synced: {synced}")

    print("\nStep 2: Applying minimal tags to all skills...")
    skills = apply_to_skills()
    print(f"  Skills enhanced: {skills}")

    print("\nStep 3: Applying minimal tags to all agents...")
    agents = apply_to_agents()
    print(f"  Agents enhanced: {agents}")

    print("\nStep 4: Applying minimal tags to all workflows...")
    workflows = apply_to_workflows()
    print(f"  Workflows enhanced: {workflows}")

    total = skills + agents + workflows
    print(f"\nTotal files enhanced: {total}")
