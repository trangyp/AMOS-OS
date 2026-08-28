---
title: validation — References — Amos Workflow Builder
type: reference
source: 07_SKILLS/amos-workflow-builder/references
tags:
- reference
- amos-workflow-builder
- canon/skill
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Workflow Builder Validation Gates

## Hard Gates (G1-G10)

### G1 (Frontmatter)
- Type field present and equals "Workflow"
- Skill field present and matches bound skill name
- Agent field present and matches bound agent name
- Trigger field present and non-empty
- Version field present

**Pass**: All fields present and correct.
**Fail**: Any field missing or incorrect.

### G2 (Binding)
- Workflow binds to exactly one agent
- Workflow binds to exactly one skill
- Agent exists in `.devin/agents/`
- Skill exists in `.devin/skills/`
- Agent's `depends_on_skills` includes the bound skill
- No orphan workflow (not referenced by any agent)

**Pass**: All bindings correct and 1:1:1.
**Fail**: Any binding broken or not 1:1.

### G3 (Steps)
- At least one step present
- Every step has a number
- Every step has an action
- Every step has a gate
- Steps are sequentially numbered

**Pass**: All steps well-formed.
**Fail**: Any step missing action or gate.

### G4 (Gates)
- Every step's gate has a name
- Validation Gates section present
- Every gate has pass/fail criteria
- Gates are uniquely named (G1, G2, ...)

**Pass**: All gates well-formed.
**Fail**: Any gate missing criteria.

### G5 (Failure Paths)
- Failure Paths section present
- Every failure path is explicit
- Every failure path fails closed (no force-fit)
- Failure paths cover: validation failure, insufficient content, scope violation

**Pass**: All failure paths explicit and fail-closed.
**Fail**: Any failure path missing or not fail-closed.

### G6 (Provenance)
- Source skill path recorded
- Source agent path recorded
- Epistemic class labels present where applicable
- Content hash present in agent binding

**Pass**: Provenance complete.
**Fail**: Any provenance field missing.

### G7 (Epistemic)
- Epistemic class labels present for derived claims
- No claim promoted beyond its evidence
- AMOS_MODEL labeled explicitly
- SOURCE_CANON not promoted to DOMAIN_EMPIRICAL

**Pass**: All epistemic labels correct.
**Fail**: Any label missing or over-promoted.

### G8 (Scope)
- No step claims beyond the workflow's declared scope
- No step claims empirical truth for AMOS_MODEL constructs
- Trigger condition matches declared scope

**Pass**: All steps within scope.
**Fail**: Any step out of scope.

### G9 (Contradiction)
- No unresolved contradictions between steps
- No step contradicts another step
- No gate contradicts another gate

**Pass**: No contradictions.
**Fail**: Any contradiction found.

### G10 (Package)
- Workflow file is valid markdown
- Workflow file is in `.devin/workflows/`
- Workflow file name matches `{skill-name}-workflow.md` pattern
- Workflow is installable (no broken references)

**Pass**: Package complete and installable.
**Fail**: Any package issue.

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[references_MOC]] · [[07_SKILLS_MOC]]

**MOC:** [[references_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-workflow-builder-validation
node_type: reference
path: 07_SKILLS/amos-workflow-builder/references/validation.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
