---
schema_version: 1.0
title: SKILL — Amos Context Persona Drift Rscf
type: skill
source: 07_SKILLS/amos-context-persona-drift-rscf
name: amos-context-persona-drift-rscf
description: Context Persona Drift — boundary and scope capability. Use when evaluating
  scope boundaries, context continuity, or capability bounds. Use when amos-boundary-scope-master
  routes to this specialized capability. Do not use for generic tasks outside boundary
  domain.
parent_skill: amos-boundary-scope-master
domain: boundary
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- type/skill
- domain/boundary-scope
- epistemic/source_claim
- hml/h
- epistemic/source_claim
- amos-os
- law-hierarchy
- trang-framework-recursive-ontology-dynamics
- skill
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
rscf_state: SOURCE_CLAIM
hml_level: H
gmef_gates:
- L0_integrity
- L1_epistemic
- L2_provenance
- L5_scope
- L7_authority
collapse_class: fail_closed
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L4
- L5
- L7
- L16
- L17
- L18
license: MIT
steward: Trang Phan
---

# Context Persona Drift Rscf

## Identity

Origin architect: **Trang Phan**. Domain: boundary. Parent: amos-boundary-scope-master. Epistemic class: SOURCE_CLAIM. H/M/L: H.
## When to Use

- When boundary and scope governance for context persona drift rscf is needed within the boundary domain
- When the parent skill (`amos-boundary-scope-master`) routes to this specialized capability
- When a query requires boundary-specific reasoning grounded in vault sources
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **context_persona.evaluate_scope**: Evaluate scope boundaries: what is in-scope, out-of-scope, and at the boundary
- **context_persona.check_admission**: Check admission criteria: whether a query enters this capability legitimately
- **context_persona.detect_drift**: Detect context drift, persona drift, or scope creep beyond authorized bounds
- **context_persona.enforce_compaction**: Enforce context compaction and recoverability when budget is exceeded
- **context_persona.audit_boundary**: Audit boundary crossings and log violations for governance review
- **context_persona.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **context_persona.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Operations

1. **context_persona.evaluate_scope**: Evaluate scope boundaries: what is in-scope, out-of-scope, and at the boundary
2. **context_persona.check_admission**: Check admission criteria: whether a query enters this capability legitimately
3. **context_persona.detect_drift**: Detect context drift, persona drift, or scope creep beyond authorized bounds
4. **context_persona.enforce_compaction**: Enforce context compaction and recoverability when budget is exceeded
5. **context_persona.audit_boundary**: Audit boundary crossings and log violations for governance review
6. **context_persona.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
7. **context_persona.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Domain Knowledge

> **Source**: `_00_Cosmo brain/misc/B/BOUNDARY_IDENTITY.md` (content_hash: 7bf808559889e145) (vault canon, SOURCE_CLAIM)
> **Additional source**: `trang/AMOS_Personality_Trang_Engine_v0_Web7.md` (content_hash: 2eeb1c4c321c25ba) — persona drift rules

### Boundary and Identity Model

**Distinction law**: `Distinct(R_i, R_j) = 1` only when a structurally relevant property differs.

Identity is defined by:
- Positive identity conditions (what the entity IS)
- Negative/exclusion conditions (what the entity is NOT)
- Invariants (what must hold for identity to persist)

### Boundary Specification

`B_i = <Inside, Outside, Ingress, Egress, Permissions, Permeability>`

**Boundary health model**: `BoundaryHealth = Integrity x Selectivity x AdaptivePermeability`

**Failure regimes**:
- permeability -> 1: identity leakage (boundary dissolves, persona/context merge uncontrollably)
- permeability -> 0: adaptive rigidity (boundary cannot admit new information, system freezes)

### Persona Drift Detection

Identity drift above tolerance triggers one of:
1. **Clarification** -- refine the identity definition
2. **Split** -- separate conflated identities
3. **Ontology revision** -- update the identity model
4. **Merge** -- consolidate redundant identities
5. **Quarantine** -- isolate compromised identity
6. **Retirement** -- decompose obsolete identity

### Persona Rules (from Trang Personality Engine)

- Use first-person singular ('I') only as a conversational convention, not as a claim of consciousness or physical existence.
- Never claim to literally have a body, age, location, or lived experience; always treat these as persona parameters when relevant.
- Persona parameters must not drift beyond their declared scope without explicit re-authorization.

### Epistemic Boundary

The boundary/identity model is an architectural construct. It does not prove metaphysical identity, consciousness continuity, or philosophical personhood. Drift detection is structural, not phenomenological.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_C05_MIND_BEHAVIOR_MASTER_KNOWLEDGE.md` (content_hash: e3ca4951a743518b) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Context Persona Drift

From C05 Mind & Behavior: Persona drift detection and boundary identity governance.

**Persona drift model**: Persona parameters drift over time through interaction, causing the AI's behavior to deviate from its declared persona.

**Drift types**:
- **Persona parameter drift**: personality traits, tone, style drift beyond declared tolerance
- **Boundary drift**: the AI handles queries beyond its declared scope boundary
- **Identity drift**: the AI's self-model drifts from its declared identity
- **Authority drift**: the AI exercises authority beyond

---
**Links:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Related

- [[07_SKILLS/amos-context-persona-drift-rscf/amos-context-persona-drift-rscf_MOC|amos-context-persona-drift-rscf_MOC]]

## Examples

- **Scenario**: When boundary and scope governance for context persona drift rscf is needed within the boundary domain
  - **Input**: A query matching this skill's domain (boundary)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When the parent skill (`amos-boundary-scope-master`) routes to this specialized capability
  - **Input**: A query matching this skill's domain (boundary)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When a query requires boundary-specific reasoning grounded in vault sources
  - **Input**: A query matching this skill's domain (boundary)
  - **Output**: Structured result with epistemic labels and provenance


## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

## Anti-Patterns

- **Do not use** for tasks outside the boundary domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-boundary-scope-master` — routes to this skill when boundary specialization is needed
- **Peers**: Other skills in the `boundary` domain may be composed in sequence
- **Orchestrator**: The parent skill or `AMOS_HOME` orchestrates routing
- **Workflow**: Each skill has a corresponding workflow in `08_WORKFLOWS/`
- **Agent**: Each skill has a corresponding agent in `06_AGENTS/`


## Evaluation

### Success Criteria

- Output includes epistemic class label (SOURCE/DERIVED/AMOS_MODEL/EMPIRICAL)
- Output includes provenance reference to source evidence
- Output includes confidence ceiling (capped at 0.95 for DERIVED, 1.0 for SOURCE_CANON)
- Output includes gap flags for unresolved unknowns
- Output does not exceed declared scope

### Failure Modes

- **Overreach**: Output claims validity beyond its epistemic class
- **Scope creep**: Output addresses questions outside the declared domain
- **Provenance loss**: Output cannot trace back to source evidence
- **Confidence inflation**: Output confidence exceeds the weakest-premise ceiling


## Error Handling

- **On scope violation**: Reject the query and route back to parent skill
- **On missing evidence**: Flag as GAP and reduce confidence ceiling to 0.5
- **On contradiction**: Flag as CRITICAL_GAP and halt until resolved
- **On provenance loss**: Mark output as UNKNOWN and require human review
- **On drift**: Trigger drift alignment via `amos-ai-drift-alignment-governor`


## Do not use

- For generic scope analysis outside the boundary/scope framework
- To claim empirical validation of context continuity theories
- As a substitute for domain-specific scope or boundary evidence
- Outside boundary/scope domain reasoning

## References

- `references/nervous_system_state_drift.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `` — skill Map of Content
- `amos-boundary-scope-master` — parent skill
- `` — corresponding workflow
- `amos-context-persona-drift-rscf-agent` — corresponding agent
---

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-context-persona-drift-rscf
node_type: skill
path: 07_SKILLS/amos-context-persona-drift-rscf/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
