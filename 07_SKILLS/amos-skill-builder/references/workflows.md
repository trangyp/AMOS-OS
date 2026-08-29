---
title: Workflows — Amos Skill Builder
type: reference
source: 07_SKILLS/amos-skill-builder/references
tags:
- reference
- amos-skill-builder
- type/skill
- skill
- law-hierarchy
- trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# Skill Builder — Workflow Reference

## Skill Creation/Update Workflow

### Phase 1: ORIENT
- Load the skill-builder skill
- Classify the request: new skill, update existing, fill placeholder, merge
- Confirm domain, scope, and parent skill (if any)

### Phase 2: GAP
- Identify the capability gap
- Check if a placeholder exists that can be filled
- Check if an existing skill can be extended
- Assess severity and urgency

### Phase 3: SOURCE
- Gather source material from vault, existing skills, and references
- Label all sources with epistemic class
- Record provenance for every source

### Phase 4: ARCHITECT
- Design skill structure: frontmatter, description, capabilities, validation gates
- Define 1:1:1 binding (skill → agent → workflow)
- Specify failure paths and fail-closed conditions
- Apply G1–G10 hard gates

### Phase 5: BUILD
- Generate SKILL.md with meaningful content
- Create reference files if needed
- Validate against frontmatter, binding, and content rules
- Package with provenance and confidence ceiling

### Phase 6: VALIDATE
- Run `skill_consolidation_inventory.py` — must pass
- Run `agent_sync_validator.py` — must pass
- Run `workflow_audit.py` — must pass
- Fix any issues and re-validate

### Phase 7: PACKAGE
- Ensure all files are in place
- Verify content hash matches
- Confirm promotion state is `production`
- Present results with epistemic labels

## Failure Paths

- If validation fails: downgrade confidence, flag the gap, escalate
- If source material is insufficient: mark as UNKNOWN/GAP, fail closed
- If 1:1:1 binding is broken: flag routing mismatch, block skill creation
- If placeholder cannot be filled: leave as placeholder, document why

---
**MOC:** references_MOC

## Related

- [[07_SKILLS_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-skill-builder-workflows
node_type: reference
path: 07_SKILLS/amos-skill-builder/references/workflows.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
