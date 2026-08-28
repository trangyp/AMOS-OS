---
schema_version: 1.0
title: SKILL — Amos Trust Formation Governor
type: skill
source: 07_SKILLS/amos-trust-formation-governor
name: amos-trust-formation-governor
description: Trust Formation Governor — organization, law and policy capability. Use when governance design, legal analysis, or policy reasoning. Use when amos-c09-org-law-policy-master routes to this specialized capability. Do not use for generic tasks outside c09 domain.
parent_skill: amos-c09-org-law-policy-master
domain: c09
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/org-law-policy
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

# Trust Formation Governor

## Identity

Origin architect: **Trang Phan**. Domain: c09. Parent: amos-c09-org-law-policy-master. Epistemic class: SOURCE_CLAIM. H/M/L: H.
## When to Use

- When governing ethical decisions: principles, consequences, fairness
- When enforcing risk constraints: acceptable risk, budget, escalation
- When assessing trust formation: evidence, reputation, accountability
- When the parent skill (`amos-c09-org-law-policy-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **trust_formation.govern_ethics**: Govern ethical decisions: principles, consequences, and procedural fairness
- **trust_formation.enforce_risk_constraint**: Enforce risk constraints: acceptable risk, risk budget, and risk escalation
- **trust_formation.assess_trust**: Assess trust formation: evidence, reputation, and accountability mechanisms
- **trust_formation.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **trust_formation.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **trust_formation.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 56746d44e9bd524d) for the full vault-sourced domain knowledge (4646 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/amos-general/A/Universe/AMOS_UNIVERSE_CORE.md` (content_hash: 15f6a73982ed5a30) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C06_SOCIETY_CULTURE_MASTER_KNOWLEDGE.md` (content_hash: 6277c28f48ab4433) (vault canon, SOURCE_CLAIM)

### Trust Formation Governor

From Cosmo Brain Universe Core: Trust formation in global market and customer behavior patterns. From C06 Society & Culture: Trust dynamics in social systems.

**Trust formation model** (from Universe Core, Module 5):
- **Income-based behavior**: trust formation varies by income level
- **Life-stage behavior**: trust formation varies by life stage
- **Digital adoption curves**: trust formation varies with digital adoption
- **Price sensitivity**: trust formation is affected by price sensitivity
- **Time sensitivity**: trust formation is affected by time sensitivity
- **Brand adhesion**: trust formation is affected by brand adhesion
- **Churn triggers**: trust breakdown triggers
- **Loyalty triggers**: trust strengthening triggers
- **Economic stress reactions**: trust formation under economic stress

**Governor model**:
- **Trust baseline**: the baseline trust level
- **Trust formation rate**: the rate at which trust forms
- **Trust breakdown rate**: the rate at which trust breaks down
- **Trust ceiling**: the maximum trust level
- **Trust floor**: the minimum trust level

**Governor laws**:
- `TRUST != TRUSTWORTHINESS`: trust is the trustor's belief; trustworthiness is the trustee's property
- `FORMATION != EARNING**: trust formation is a process; earning trust is an action
- `TRUST != COMPLIANCE**: trust is a belief; compliance is a behavior

### Epistemic Boundary

Trust formation governance is a social model. It does not prove trust is always well-formed, that the formation model is complete, or that trust implies trustworthiness.

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
- **G4 (Anti-overreach)**: No cla

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-trust-formation-governor_MOC]]

## Examples

- **Scenario**: When governing ethical decisions: principles, consequences, fairness
  - **Input**: A query matching this skill's domain (c09)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When enforcing risk constraints: acceptable risk, budget, escalation
  - **Input**: A query matching this skill's domain (c09)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When assessing trust formation: evidence, reputation, accountability
  - **Input**: A query matching this skill's domain (c09)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the c09 domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-c09-org-law-policy-master` — routes to this skill when c09 specialization is needed
- **Peers**: Other skills in the `c09` domain may be composed in sequence
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

- For generic governance analysis outside the org/law/policy framework
- To claim empirical validation of governance or legal theories
- As a substitute for domain-specific legal or compliance evidence
- Outside org/law/policy domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `[[amos-trust-formation-governor_MOC]]` — skill Map of Content
- `amos-c09-org-law-policy-master` — parent skill
- `[[amos-trust-formation-governor-workflow]]` — corresponding workflow
- `amos-trust-formation-governor-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-trust-formation-governor
node_type: skill
path: 07_SKILLS/amos-trust-formation-governor/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
