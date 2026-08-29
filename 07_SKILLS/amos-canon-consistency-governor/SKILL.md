---
schema_version: 1.0
title: SKILL — Amos Canon Consistency Governor
type: skill
source: 07_SKILLS/amos-canon-consistency-governor
name: amos-canon-consistency-governor
description: Canon Consistency Governor — canon and universe capability. Use when
  canon reasoning, universe-level analysis, or invariant verification. Use when amos-canon-universe-master
  routes to this specialized capability. Do not use for generic tasks outside canon
  domain.
parent_skill: amos-canon-universe-master
domain: canon
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- type/skill
- domain/canon-universe
- epistemic/source_claim
- hml/h
- epistemic/source_claim
- amos-os
- 07-skills-moc
- amos-canon-consistency-governor-moc
- 00-home
- amos-rscf-nodes
- law-hierarchy
- references-moc
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
- L3_dependency
- L5_scope
- L7_authority
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L3
- L4
- L5
- L7
- L16
- L17
- L18
- L19
license: MIT
steward: Trang Phan
---

# Canon Consistency Governor

## Identity

Origin architect: **Trang Phan**. Domain: canon. Parent: amos-canon-universe-master. Epistemic class: SOURCE_CLAIM. H/M/L: H.
## When to Use

- When compiling canonical structure from vault sources
- When checking canon consistency for contradictions and gaps
- When enforcing canon invariants across all parts
- When navigating canon to locate parts for any topic
- When the parent skill (`amos-canon-universe-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **canon_consistency.compile_canon**: Compile canonical structure from sources into a consistent, navigable canon
- **canon_consistency.check_consistency**: Check canon consistency: no contradictions, no gaps, no orphan references
- **canon_consistency.enforce_invariant**: Enforce canon invariants: structural laws that must hold across all parts
- **canon_consistency.navigate_canon**: Navigate canon: locate the canonical part for any topic or query
- **canon_consistency.validate_substrate**: Validate canonical software substrate against canon requirements

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 653b78f7dec7566f) for the full vault-sourced domain knowledge (9537 chars).
- **canon_consistency.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **canon_consistency.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **canon_consistency.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Operations

1. **canon_consistency.compile_canon**: Compile canonical structure from sources into a consistent, navigable canon
2. **canon_consistency.check_consistency**: Check canon consistency: no contradictions, no gaps, no orphan references
3. **canon_consistency.enforce_invariant**: Enforce canon invariants: structural laws that must hold across all parts
4. **canon_consistency.navigate_canon**: Navigate canon: locate the canonical part for any topic or query
5. **canon_consistency.validate_substrate**: Validate canonical software substrate against canon requirements
6. **canon_consistency.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
7. **canon_consistency.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
8. **canon_consistency.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Cosmo Brain Vault Content

> **Source**: `_00_Cosmo brain/amos-general/0/00_AMOS_Full_Brain_OS_Architecture.md` (content_hash: b7acbb430dff829e) (vault canon, SOURCE_CLAIM)

### Canon Consistency Rules

**Law of Law**: No unresolved contradictions within the canon. Every contradiction must be either resolved, flagged as UNKNOWN/GAP, or explicitly tolerated with justification.

**Consistency checks**:
1. **Contradiction detection**: no two canon entries make contradictory claims within the same scope and regime
2. **Gap detection**: no canon entry references a missing dependency
3. **Orphan detection**: no canon entry has zero incoming references (except root entries)
4. **Scope consistency**: no canon entry claims beyond its declared scope
5. **Epistemic consistency**: no canon entry promotes its epistemic class without evidence
6. **Provenance consistency**: every canon entry has a traceable provenance chain

### RSCF Epistemic Substrate

Objects: claim / class / premises / evidence / provenance / scope / regime / freshness / dependencies / competing hypotheses / falsifiers / confidence ceiling.

State kinds: OBSERVATION, SOURCE_CLAIM, DERIVED, MODEL, DECISION, UNKNOWN.

### Contradiction Resolution Protocol

1. **Detect**: identify the contradiction (automated scan)
2. **Classify**: scope conflict, regime conflict, evidence conflict, or epistemic conflict
4. **Resolve**: resolve via evidence weight, scope intersection, or steward decision
5. **Flag**: if unresolvable, flag as UNKNOWN/GAP and fail closed
6. **Record**: record the contradiction and resolution in the canon audit trail

### Epistemic Boundary

Canon consistency is a structural property. It does not prove the canon is true, only that it is internally consistent. A consistent canon can still be wrong.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the skill's scope.
- **G2 (Epistemic class)**: All claims labeled SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL — never claim beyo

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-canon-consistency-governor_MOC]]

## Examples

- **Scenario**: When compiling canonical structure from vault sources
  - **Input**: A query matching this skill's domain (canon)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When checking canon consistency for contradictions and gaps
  - **Input**: A query matching this skill's domain (canon)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When enforcing canon invariants across all parts
  - **Input**: A query matching this skill's domain (canon)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the canon domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-canon-universe-master` — routes to this skill when canon specialization is needed
- **Peers**: Other skills in the `canon` domain may be composed in sequence
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

- For generic structural analysis outside the canon framework
- To claim empirical validation of consciousness or civilization theories
- As a substitute for domain-specific historical or scientific evidence
- Outside canon/universe domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `` — skill Map of Content
- `amos-canon-universe-master` — parent skill
- `` — corresponding workflow
- `amos-canon-consistency-governor-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-canon-consistency-governor
node_type: skill
path: 07_SKILLS/amos-canon-consistency-governor/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
