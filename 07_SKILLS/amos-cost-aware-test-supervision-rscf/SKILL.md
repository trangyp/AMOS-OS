---
schema_version: 1.0
title: SKILL — Amos Cost Aware Test Supervision Rscf
type: skill
source: 07_SKILLS/amos-cost-aware-test-supervision-rscf
name: amos-cost-aware-test-supervision-rscf
description: Cost Aware Test Supervision — super engines capability. Use when super-engine reasoning, consciousness emulation, or mega-engine analysis. Use when amos-super-engines-master routes to this specialized capability. Do not use for generic tasks outside super domain.
parent_skill: amos-super-engines-master
domain: super
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/super-engines
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
license: MIT
steward: Trang Phan
---

# Cost Aware Test Supervision Rscf

## Identity

Origin architect: **Trang Phan**. Domain: super. Parent: amos-super-engines-master. Epistemic class: SOURCE_CLAIM. H/M/L: H.
## When to Use

- When supervising testing with cost-awareness: coverage vs cost
- When transforming distinction-relation structures across scales
- When orchestrating full brain OS: coordinating all cognitive engines
- When the parent skill (`amos-super-engines-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **cost_aware.supervise_test**: Supervise testing with cost-awareness: balance test coverage vs resource cost
- **cost_aware.transform_distinction**: Transform distinction-relation structures across scales and contexts
- **cost_aware.orchestrate_brain**: Orchestrate full brain OS: coordinate all cognitive engines as a unified system

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: b9dd24dc8d3f6a0d) for the full vault-sourced domain knowledge (8852 chars).
- **cost_aware.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **cost_aware.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **cost_aware.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### RSCF Epistemic Substrate

This RSCF engine operates on the AMOS RSCF (Reasoning, Scope, Claim, Falsifier) epistemic substrate.

**RSCF objects**: claim / class / premises / evidence / provenance / scope / regime / freshness / dependencies / competing hypotheses / falsifiers / confidence ceiling.

**RSCF state kinds**: OBSERVATION, SOURCE_CLAIM, DERIVED, MODEL, DECISION, UNKNOWN.

**RSCF laws**:
- `CLAIM != FACT`: a claim is not a fact; it must be labeled with epistemic class
- `CONFIDENCE <= EVIDENCE`: confidence cannot exceed evidence support
- `FALSIFIER_REQUIRED`: every claim must declare its falsifier
- `SCOPE_BOUND`: every claim is valid only within its declared scope and regime
- `PROVENANCE_REQUIRED`: every claim must have traceable provenance

**RSCF validation gates**:
- G1 (Law of Law): no unresolved contradictions
- G2 (Epistemic class): all claims labeled, no class promotion without evidence
- G3 (Provenance): source path recorded for every derived claim
- G4 (Anti-overreach): no claim beyond declared scope
- G5 (Equation firewall): equations carry status tags
- G6 (Failure mode): on failure, downgrade, flag, escalate

### Epistemic Boundary

This RSCF engine is an epistemic governance tool. It does not prove claims are true, that all falsifiers are known, or that the RSCF framework is complete.

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
- **G4 (Anti-overreach)**: No claim beyond the skill's declared scope and epistemic class.
- **G5 (Equation firewall)**: Equations carry status tags (ESTABLISHED_MATH / SOURCE_DERIVED / AMOS_MODEL / EMPIRICALLY_CALIBRATED / UNVERIFIED).
- **G6 (Failure mode)**: On validation failure, downgrade confidence, flag the gap, escalate — do not force-fit.

## Provenance

- **Skill**: `amos-cost-aware-test-supervision-rscf`
- **Parent**: `amos-super-engines-master`
- **Domain**: super
- **

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-cost-aware-test-supervision-rscf_MOC]]

## Examples

- **Scenario**: When supervising testing with cost-awareness: coverage vs cost
  - **Input**: A query matching this skill's domain (super)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When transforming distinction-relation structures across scales
  - **Input**: A query matching this skill's domain (super)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When orchestrating full brain OS: coordinating all cognitive engines
  - **Input**: A query matching this skill's domain (super)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the super domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-super-engines-master` — routes to this skill when super specialization is needed
- **Peers**: Other skills in the `super` domain may be composed in sequence
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

- For generic consciousness analysis outside the super-engine framework
- To claim empirical validation of consciousness or mega-engine theories
- As a substitute for domain-specific cognitive or consciousness evidence
- Outside super-engine domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `[[amos-cost-aware-test-supervision-rscf_MOC]]` — skill Map of Content
- `amos-super-engines-master` — parent skill
- `[[amos-cost-aware-test-supervision-rscf-workflow]]` — corresponding workflow
- `amos-cost-aware-test-supervision-rscf-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-cost-aware-test-supervision-rscf
node_type: skill
path: 07_SKILLS/amos-cost-aware-test-supervision-rscf/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
