#!/usr/bin/env python3
"""
Propagate vault metadata fields from .agents/skills/ pattern to all skills, agents, workflows.

The user added these fields to 10 skills in .agents/skills/:
  parent_skill, domain, origin_architect, epistemic_class, version,
  rscf_state, hml_level, gmef_gates, collapse_class, qfm_gate_set, law_compliance

This script:
1. Reads the pattern from .agents/skills/
2. Infers domain-specific values for each skill based on parent_skill/domain
3. Adds these fields to all 07_SKILLS/, 06_AGENTS/, 08_WORKFLOWS/
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

# ─── Default field values from user's pattern ───
DEFAULT_FIELDS = {
    "origin_architect": "Trang Phan",
    "epistemic_class": "SOURCE_CLAIM",
    "version": "1.1.0",
    "rscf_state": "SOURCE_CLAIM",
    "hml_level": "M",
    "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope", "L7_authority"],
    "collapse_class": "reversible",
    "qfm_gate_set": "QFM_v43",
    "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L7", "L16", "L17", "L18"],
}

# ─── Domain-specific overrides ───
DOMAIN_OVERRIDES = {
    # Canon domain — higher rigor
    "canon": {
        "epistemic_class": "SOURCE_CLAIM",
        "hml_level": "H",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L3_dependency", "L5_scope", "L7_authority"],
        "law_compliance": ["L0", "L1", "L2", "L3", "L4", "L5", "L7", "L16", "L17", "L18", "L19"],
    },
    # Formal verification — highest rigor
    "formal": {
        "epistemic_class": "SOURCE_CLAIM",
        "hml_level": "H",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L3_dependency", "L5_scope", "L7_authority", "L22_replayability"],
        "law_compliance": ["L0", "L1", "L2", "L3", "L4", "L5", "L7", "L16", "L17", "L18", "L19", "L22"],
    },
    # Runtime/OS — execution-critical
    "runtime": {
        "epistemic_class": "SOURCE_CLAIM",
        "hml_level": "M",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope", "L7_authority", "L8_execution"],
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L7", "L8", "L16", "L17", "L18"],
    },
    # Security — boundary-critical
    "security": {
        "epistemic_class": "SOURCE_CLAIM",
        "hml_level": "H",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope", "L7_authority", "L23_mvcc_cas"],
        "collapse_class": "fail_closed",
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L7", "L16", "L17", "L18", "L23"],
    },
    # Audit/repair — recovery-focused
    "audit": {
        "epistemic_class": "DERIVED",
        "hml_level": "M",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope", "L7_authority", "L22_replayability"],
        "collapse_class": "reversible",
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L7", "L16", "L17", "L18", "L22"],
    },
    # Knowledge/research — evidence-focused
    "knowledge": {
        "epistemic_class": "SOURCE_CLAIM",
        "hml_level": "M",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope"],
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L16", "L17"],
    },
    # Arxiv research — evidence
    "arxiv": {
        "epistemic_class": "SOURCE_CLAIM",
        "hml_level": "M",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope"],
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L16", "L17"],
    },
    # Econ/finance — state+entropy
    "econ": {
        "epistemic_class": "AMOS_MODEL",
        "hml_level": "M",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope", "L6_uncertainty"],
        "collapse_class": "reversible",
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L6", "L16", "L17"],
    },
    "fx": {
        "epistemic_class": "AMOS_MODEL",
        "hml_level": "M",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope", "L6_uncertainty"],
        "collapse_class": "reversible",
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L6", "L16", "L17"],
    },
    # Strategy — topology+relation
    "c08": {
        "epistemic_class": "AMOS_MODEL",
        "hml_level": "M",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope", "L7_authority"],
        "collapse_class": "reversible",
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L7", "L16", "L17", "L18"],
    },
    # Mind/behavior
    "c05": {
        "epistemic_class": "AMOS_MODEL",
        "hml_level": "M",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope"],
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L16", "L17"],
    },
    "mind_behavior": {
        "epistemic_class": "AMOS_MODEL",
        "hml_level": "M",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope"],
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L16", "L17"],
    },
    # Bio/neuro
    "c04": {
        "epistemic_class": "SOURCE_CLAIM",
        "hml_level": "M",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope", "L7_authority"],
        "collapse_class": "reversible",
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L7", "L16", "L17", "L18"],
    },
    # Society/culture
    "c06": {
        "epistemic_class": "SOURCE_CLAIM",
        "hml_level": "M",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope", "L7_authority"],
        "collapse_class": "reversible",
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L7", "L16", "L17", "L18"],
    },
    # Org/law/policy
    "c09": {
        "epistemic_class": "SOURCE_CLAIM",
        "hml_level": "H",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope", "L7_authority"],
        "collapse_class": "fail_closed",
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L7", "L16", "L17", "L18"],
    },
    # Tech/engineering
    "c10": {
        "epistemic_class": "SOURCE_CLAIM",
        "hml_level": "M",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope", "L7_authority", "L8_execution"],
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L7", "L8", "L16", "L17", "L18"],
    },
    # Trang framework
    "trang": {
        "epistemic_class": "SOURCE_CLAIM",
        "hml_level": "H",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope", "L7_authority"],
        "collapse_class": "reversible",
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L7", "L16", "L17", "L18"],
    },
    # Fractal
    "fractal": {
        "epistemic_class": "AMOS_MODEL",
        "hml_level": "M",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope"],
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L16", "L17"],
    },
    # RSCF epistemic
    "rscf": {
        "epistemic_class": "SOURCE_CLAIM",
        "hml_level": "H",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope", "L7_authority"],
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L7", "L16", "L17", "L18", "L19"],
    },
    # Causal
    "causal": {
        "epistemic_class": "SOURCE_CLAIM",
        "hml_level": "H",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope", "L24_causal_epoch"],
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L7", "L16", "L17", "L18", "L24"],
    },
    # Memory
    "memory": {
        "epistemic_class": "SOURCE_CLAIM",
        "hml_level": "M",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope"],
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L16", "L17"],
    },
    # Boundary
    "boundary": {
        "epistemic_class": "SOURCE_CLAIM",
        "hml_level": "H",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope", "L7_authority"],
        "collapse_class": "fail_closed",
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L7", "L16", "L17", "L18"],
    },
    # Info
    "info": {
        "epistemic_class": "AMOS_MODEL",
        "hml_level": "M",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope"],
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L16", "L17"],
    },
    "information": {
        "epistemic_class": "AMOS_MODEL",
        "hml_level": "M",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope"],
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L16", "L17"],
    },
    # Agent
    "agent": {
        "epistemic_class": "SOURCE_CLAIM",
        "hml_level": "M",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope", "L7_authority"],
        "collapse_class": "reversible",
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L7", "L16", "L17", "L18"],
    },
    # Super engines
    "super": {
        "epistemic_class": "AMOS_MODEL",
        "hml_level": "H",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope", "L7_authority"],
        "collapse_class": "reversible",
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L7", "L16", "L17", "L18"],
    },
    # McKinsey
    "mckinsey": {
        "epistemic_class": "AMOS_MODEL",
        "hml_level": "M",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope"],
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L16", "L17"],
    },
    # Skill (meta)
    "skill": {
        "epistemic_class": "SOURCE_CLAIM",
        "hml_level": "M",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope"],
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L16", "L17"],
    },
    # Workflow
    "workflow": {
        "epistemic_class": "SOURCE_CLAIM",
        "hml_level": "M",
        "gmef_gates": ["L0_integrity", "L1_epistemic", "L2_provenance", "L5_scope", "L7_authority", "L8_execution"],
        "collapse_class": "reversible",
        "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L7", "L8", "L16", "L17", "L18"],
    },
}

# C01-C12 domain mappings
C_DOMAIN_OVERRIDES = {
    "c01": {"epistemic_class": "SOURCE_CLAIM", "hml_level": "H", "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L7", "L16", "L17", "L18", "L19"]},
    "c02": {"epistemic_class": "SOURCE_CLAIM", "hml_level": "H", "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L7", "L16", "L17", "L18"]},
    "c03": {"epistemic_class": "SOURCE_CLAIM", "hml_level": "H", "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L16", "L17"]},
    "c11": {"epistemic_class": "SOURCE_CLAIM", "hml_level": "M", "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L16", "L17"]},
    "c12": {"epistemic_class": "SOURCE_CLAIM", "hml_level": "M", "law_compliance": ["L0", "L1", "L2", "L4", "L5", "L16", "L17"]},
}


def get_fields_for_domain(domain: str) -> dict:
    """Get field values for a given domain."""
    fields = dict(DEFAULT_FIELDS)
    domain_lower = domain.lower() if domain else ""

    # Check domain overrides
    if domain_lower in DOMAIN_OVERRIDES:
        fields.update(DOMAIN_OVERRIDES[domain_lower])
    elif domain_lower in C_DOMAIN_OVERRIDES:
        fields.update(C_DOMAIN_OVERRIDES[domain_lower])
    elif "cross-domain" in domain_lower:
        # Cross-domain uses defaults
        pass

    return fields


def add_vault_metadata_to_skills():
    """Add vault metadata fields to all skills in 07_SKILLS/."""
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

        # Skip if already has rscf_state (already enhanced)
        if "rscf_state" in fm:
            continue

        domain = fm.get("domain", "")
        fields = get_fields_for_domain(domain)

        # Add fields
        for k, v in fields.items():
            if k not in fm:
                fm[k] = v

        new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
        new_text = f"---\n{new_fm}---\n{parts[2]}"
        skill_path.write_text(new_text, encoding="utf-8")
        enhanced += 1

    return enhanced


def add_vault_metadata_to_agents():
    """Add vault metadata fields to all agents in 06_AGENTS/."""
    enhanced = 0
    for af in AGENTS_DIR.glob("*.json"):
        try:
            agent = json.loads(af.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue

        # Skip if already has rscf_state
        if "rscf_state" in agent:
            continue

        # Infer domain from agent's domain field or tags
        domain = agent.get("domain", "")
        if not domain:
            # Infer from tags
            tags = agent.get("tags", [])
            if isinstance(tags, list):
                for t in tags:
                    if isinstance(t, str) and t.startswith("domain/"):
                        domain = t.replace("domain/", "")
                        break

        fields = get_fields_for_domain(domain)

        # Add fields
        for k, v in fields.items():
            if k not in agent:
                agent[k] = v

        af.write_text(json.dumps(agent, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        enhanced += 1

    return enhanced


def add_vault_metadata_to_workflows():
    """Add vault metadata fields to all workflows in 08_WORKFLOWS/."""
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

        # Skip if already has rscf_state
        if "rscf_state" in fm:
            continue

        domain = fm.get("domain", "")
        if not domain:
            # Infer from tags
            tags = fm.get("tags", [])
            if isinstance(tags, list):
                for t in tags:
                    if isinstance(t, str) and t.startswith("domain/"):
                        domain = t.replace("domain/", "")
                        break
            if not domain:
                domain = "workflow"

        fields = get_fields_for_domain(domain)

        # Add fields
        for k, v in fields.items():
            if k not in fm:
                fm[k] = v

        new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
        new_text = f"---\n{new_fm}---\n{parts[2]}"
        wf.write_text(new_text, encoding="utf-8")
        enhanced += 1

    return enhanced


if __name__ == "__main__":
    print("Adding vault metadata fields to all skills, agents, workflows...")
    print(f"  Fields: {list(DEFAULT_FIELDS.keys())}")
    print()

    skills = add_vault_metadata_to_skills()
    print(f"Skills enhanced: {skills}")

    agents = add_vault_metadata_to_agents()
    print(f"Agents enhanced: {agents}")

    workflows = add_vault_metadata_to_workflows()
    print(f"Workflows enhanced: {workflows}")

    total = skills + agents + workflows
    print(f"\nTotal files enhanced: {total}")
