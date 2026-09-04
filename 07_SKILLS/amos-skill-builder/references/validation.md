---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Validation
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# Skill Builder — Validation Reference

## Hard Gates (G1–G10)

Every AMOS skill MUST pass these gates before promotion to `production`.

### G1: Frontmatter Complete

- Required fields: `name`, `description`
- Allowed extra fields: `domain`, `epistemic_class`, `origin_architect`, `parent_skill`, `version`, `author`, `steward`, `redirect_target`
- `name` MUST match the skill directory name

### G2: Description Meaningful

- `description` MUST be ≥ 20 characters
- MUST NOT be a placeholder ("Placeholder SKILL.md for ...")
- MUST describe what the skill does and when to use it

### G3: No Placeholder Content

- SKILL.md MUST NOT contain "Placeholder SKILL.md" in the first 500 chars

### G4: Epistemic Class Labeling

- All claims MUST be labeled: SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL
- No claim beyond established evidence or explicitly labeled AMOS_MODEL

### G5: Provenance

- Source path recorded for every derived claim
- Vault references include the canonical vault file path

### G6: Anti-Overreach

- No claim beyond the skill's declared scope
- Scope declared in frontmatter or first section

### G7: 1:1:1 Binding

- Every skill binds to exactly one agent and one workflow
- Agent `depends_on_skills` includes this skill
- Workflow `Skill:` frontmatter references this skill

### G8: Failure Modes

- Known failure modes documented
- On validation failure: downgrade confidence, flag gap, escalate

### G9: Capability Naming

- Capabilities use `<domain>.<verb>` format (e.g., `skill.design`)
- No hyphens in capability names (use underscores)
- No `run_` prefix (use `design_` or domain-specific verb)

### G10: Content Hash

- Agent `content_hash` matches recomputed hash
- Promotion state is one of: draft, staging, production, deprecated

## Validation Commands

```bash
python3 scripts/skill_consolidation_inventory.py   # skill validation
python3 agent_sync_validator.py                     # agent validation
python3 scripts/workflow_audit.py                   # workflow validation
```

______________________________________________________________________

**MOC:** references_MOC

## Related

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-skill-builder-validation
node_type: reference
path: 07_SKILLS/amos-skill-builder/references/validation.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
