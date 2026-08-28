---
schema_version: 1.0
title: SKILL — Amos Aibom Lifecycle Assurance Rscf
type: skill
source: 07_SKILLS/amos-aibom-lifecycle-assurance-rscf
name: amos-aibom-lifecycle-assurance-rscf
description: AIBOM Lifecycle Assurance — RSCF epistemic capability. Use when classifying
  claims by epistemic state, validating outputs against epistemic and scope constraints,
  or analyzing evidence structure. Use when amos-rscf-epistemic-master routes to this
  . Do not use for generic tasks outside rscf domain.
parent_skill: amos-rscf-epistemic-master
domain: rscf
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/rscf-epistemic
- rscf/source_claim
- hml/h
- epistemic/source_claim
- amos_os
- 07-skills-moc
- amos-aibom-lifecycle-assurance-rscf-moc
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
- L5_scope
- L7_authority
collapse_class: reversible
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
- L19
license: MIT
steward: Trang Phan
---

# Aibom Lifecycle Assurance Rscf

## Identity

Origin architect: **Trang Phan**. Domain: rscf. Parent: amos-rscf-epistemic-master. Epistemic class: SOURCE_CLAIM. H/M/L: H.
## When to Use

- When classifying AIBOM lifecycle claims by epistemic state and binding them to evidence
- When validating evidence chains for provenance, freshness, scope, and regime validity
- When tracing AIBOM output provenance to vault sources and content hashes
- When assessing confidence ceilings based on epistemic class and evidence strength
- When detecting falsifiers and downgrading confidence as counter-evidence emerges
- When managing AIBOM lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating AIBOM outputs against domain constraints and epistemic class
- When the parent skill (`amos-rscf-epistemic-master`) routes to this specialized capability

## Capabilities

- **aibom_lifecycle.classify_claim**: Classify claims by epistemic state (VERIFIED, DERIVED, MODEL, UNKNOWN/GAP) and bind to evidence
- **aibom_lifecycle.validate_evidence**: Validate evidence chains: provenance, freshness, scope, and regime validity
- **aibom_lifecycle.trace_provenance**: Trace output provenance to vault sources and tag with content_hash
- **aibom_lifecycle.assess_confidence**: Assess confidence ceiling based on epistemic class and evidence strength
- **aibom_lifecycle.detect_falsifier**: Detect falsifiers and downgrade confidence when counter-evidence emerges
- **aibom_lifecycle.manage_lifecycle**: Manage AIBOM lifecycle: classify, validate, trace, assess, detect
- **aibom_lifecycle.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration
- **aibom_lifecycle.validate_outputs**: Validate AIBOM outputs against domain constraints and epistemic class

## Vault-Sourced Content

### Source 1: Assurance, Debt Registers & Maturity Governance

> Path: `dated/2026-08-22/2026-08-22 Assurance Debt Governance.md` | Size: 3711 chars | Match score: 5 | content_hash: a774828e5c7e1e7d

# Assurance, Debt Registers & Maturity Governance


## Overview

The Assurance, Debt Registers & Maturity Governance module provides the final
layer of the AMOS OS Kernel's governance stack. It ensures that assurance
cases are properly reviewed, debt is tracked and managed, components reach
appropriate maturity levels before promotion, evidence/benchmarks/policies
are kept current, obsolete architecture is detected, and simplification
opportunities are pursued.

## Subsystems

### 301 — Independent Falsifier Manager
Tracks independent falsifier access for scientific claims.
Gate: CONDITIONAL if pending falsifier access.

### 302 — Red-Team Independence Manager
Ensures red teams are independent from the development team.
Gate: FAIL if non-independent red teams detected.

### 303 — Assurance Case Manager
Manages assurance cases (draft/under_review/approved/rejected/expired).
Gate: CONDITIONAL if unapproved or expired cases.

### 304 — Certification Profile Manager
Tracks certifications (standard/level/certifier/valid_until).
Gate: CONDITIONAL if expired certifications.

### 305 — Residual Risk Acceptance Manager
Tracks residual risk acceptance by designated authority.
Gate: CONDITIONAL if unaccepted residual risks.

### 306 — Known Gap Disclosure Manager
Ensures known gaps are disclosed to appropriate audiences.
Gate: FAIL if undisclosed known gaps.

### 307-310 — Debt Register Manager
Tracks four types of debt: epistemic, governance, security, architecture.
Gate: FAIL if debt amount > 0.75 threshold.

### 311 — Debt Interaction Manager
Analyzes interactions between different types of debt.
Gate: CONDITIONAL if high-severity interactions (> 0.5).

### 312 — Maturity State Manager
Tracks component maturity (experimental/prototype/beta/production/legacy/deprecated).
Gate: CONDITIONAL if immature components in use.

### 313 — Promotion Evidence Manager
Manages promotion evidence standards (pending/promoted/demoted/quarantined/rejected).
Gate: CONDITIONAL if pending promotions.

### 314 — Demotion/Quarantine Manager
Manages demotion and quarantine rules with authority tracking.
Gate: FAIL if quarantined without authority; CONDITIONAL if quarantined with authority.

### 315 — Continuous Re

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-aibom-lifecycle-assurance-rscf_MOC]]

## Examples

- **Scenario**: When classifying AIBOM lifecycle claims by epistemic state and binding them to evidence
  - **Input**: A query matching this skill's domain (rscf)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When validating evidence chains for provenance, freshness, scope, and regime validity
  - **Input**: A query matching this skill's domain (rscf)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When tracing AIBOM output provenance to vault sources and content hashes
  - **Input**: A query matching this skill's domain (rscf)
  - **Output**: Structured result with epistemic labels and provenance


## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

## Anti-Patterns

- **Do not use** for tasks outside the rscf domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-rscf-epistemic-master` — routes to this skill when rscf specialization is needed
- **Peers**: Other skills in the `rscf` domain may be composed in sequence
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

- For generic epistemic analysis outside the RSCF framework
- To claim empirical validation of epistemic classification theories
- As a substitute for domain-specific evidence or provenance validation
- Outside RSCF epistemic domain reasoning

## References

- `references/aibom_subsystems.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `` — skill Map of Content
- `amos-rscf-epistemic-master` — parent skill
- `` — corresponding workflow
- `amos-aibom-lifecycle-assurance-rscf-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-aibom-lifecycle-assurance-rscf
node_type: skill
path: 07_SKILLS/amos-aibom-lifecycle-assurance-rscf/[[SKILL]].md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
