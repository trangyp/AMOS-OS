---
title: "SKILL — Amos Emergent Social Intelligence Risk Rscf"
type: skill
source: 07_SKILLS/amos-emergent-social-intelligence-risk-rscf
name: amos-emergent-social-intelligence-risk-rscf
description: Emergent Social Intelligence Risk — society and culture capability. Use when social analysis, cultural reasoning, or anthropological study. Use when amos-c06-society-culture-master routes to this specialized capability.
parent_skill: amos-c06-society-culture-master
domain: c06
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-emergent-social-intelligence-risk-rscf, canon/skill]
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: "1.1.0"
---


# Emergent Social Intelligence Risk Rscf

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c06-society-culture-master`
- **Domain**: c06
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Society-culture engine for Emergent Social Intelligence Risk Rscf

## When to Use

- When analyzing emergent social intelligence: norms, networks, culture
- When modeling heritage decision intelligence: tradition and adaptation
- When assessing language as equation: semantic structure and drift
- When the parent skill (`amos-c06-society-culture-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **emergent_social.analyze_social**: Analyze emergent social intelligence: norms, networks, and cultural dynamics
- **emergent_social.model_heritage**: Model heritage decision intelligence: tradition, continuity, and adaptation
- **emergent_social.assess_language**: Assess language as equation: semantic structure, pragmatic force, and drift
- **emergent_social.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **emergent_social.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **emergent_social.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 275c3a3ed3327fdb) for the full vault-sourced domain knowledge (8170 chars).

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

- **Skill**: `amos-emergent-so

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-emergent-social-intelligence-risk-rscf_MOC]]

## Examples

- **Scenario**: When analyzing emergent social intelligence: norms, networks, culture
  - **Input**: A query matching this skill's domain (c06)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When modeling heritage decision intelligence: tradition and adaptation
  - **Input**: A query matching this skill's domain (c06)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When assessing language as equation: semantic structure and drift
  - **Input**: A query matching this skill's domain (c06)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the c06 domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-c06-society-culture-master` — routes to this skill when c06 specialization is needed
- **Peers**: Other skills in the `c06` domain may be composed in sequence
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
- `[[amos-emergent-social-intelligence-risk-rscf_MOC]]` — skill Map of Content
- `amos-c06-society-culture-master` — parent skill
- `[[amos-emergent-social-intelligence-risk-rscf-workflow]]` — corresponding workflow
- `amos-emergent-social-intelligence-risk-rscf-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-emergent-social-intelligence-risk-rscf
node_type: skill
path: 07_SKILLS/amos-emergent-social-intelligence-risk-rscf/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
