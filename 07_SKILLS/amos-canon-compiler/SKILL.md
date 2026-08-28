---
title: SKILL — Amos Canon Compiler
type: skill
source: 07_SKILLS/amos-canon-compiler
name: amos-canon-compiler
description: Canon Compiler — canon and universe capability. Use when canon reasoning, universe-level
  analysis, or invariant verification. Use when amos-canon-universe-master routes to this specialized
  capability.
parent_skill: amos-canon-universe-master
domain: canon
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/canon-universe
- rscf/source_claim
- hml/h
- epistemic/source_claim
- amos_os
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
---








# Canon Compiler

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

- **canon_compiler.compile_canon**: Compile canonical structure from sources into a consistent, navigable canon
- **canon_compiler.check_consistency**: Check canon consistency: no contradictions, no gaps, no orphan references
- **canon_compiler.enforce_invariant**: Enforce canon invariants: structural laws that must hold across all parts
- **canon_compiler.navigate_canon**: Navigate canon: locate the canonical part for any topic or query
- **canon_compiler.validate_substrate**: Validate canonical software substrate against canon requirements

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 0980a04439ab621f) for the full vault-sourced domain knowledge (9537 chars).
- **canon_compiler.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **canon_compiler.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **canon_compiler.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Cosmo Brain Vault Content

> **Source**: `_00_Cosmo brain/amos-general/A/Universe/AMOS_UNIVERSE_OS_FULL_BUNDLE.md` (content_hash: c3aef595e3657ad7, 3166758 bytes) (vault canon, SOURCE_CLAIM)

### Canon Compilation Process

The canon compiler transforms vault sources into a consistent, navigable canonical structure.

**10 canonical parts** (Universe Total Canon):
- P1_META: Meta-logic and universal laws
- P2_LOGIC: Logic kernel (ULK 8 ALUs, 7 UMLs, 6 UOPs)
- P3_PHYSICS: Physical constraints and cosmic behavior
- P4_INFORMATION: Information theory and flow
- P5_BIOLOGY: Biological logic and UBI
- P6_COGNITION: Cognitive architecture and inference
- P7_SOCIETY: Social dynamics and culture
- P8_GOVERNANCE: Governance and authority
- P9_REPAIR: Repair and recovery
- P10_CANON_INTEGRATION: Cross-layer integration

### Compilation Steps

1. **Extract**: Pull canonical content from vault sources
2. **Type**: Assign epistemic class to each canon entry
3. **Cross-reference**: Build wikilink graph and dependency closure
4. **Validate**: Check canon consistency (no contradictions, no gaps, no orphan references)
5. **Index**: Build navigation index (MOC, tags, backlinks)
6. **Package**: Produce compiled canon with provenance manifest

### Canon Inheritance Rules

- Child canon inherits parent canon's epistemic class unless explicitly overridden
- Override requires independent evidence and steward approval
- Canon versioning: each compilation produces a versioned snapshot
- Canon rollback: every compilation has a rollback target

### Epistemic Boundary

Canon compilation is an organizational process. It does not prove the canon is true, complete, or final. The canon is a structured knowledge base, not a source of truth.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the skill's scope.
- **G2 (Epistemic class)**: All claims labeled SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL — never claim beyond evidence.
- **G3 (Provenance)**: Source path recorded for every derived claim.
- **G4 (Anti-overreach)**: No claim beyond the skill's declar

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-canon-compiler_MOC]]

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


## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `[[amos-canon-compiler_MOC]]` — skill Map of Content
- `amos-canon-universe-master` — parent skill
- `[[amos-canon-compiler-workflow]]` — corresponding workflow
- `amos-canon-compiler-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-canon-compiler
node_type: skill
path: 07_SKILLS/amos-canon-compiler/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
