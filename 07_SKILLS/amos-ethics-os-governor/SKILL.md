---
schema_version: 1.0
title: SKILL — Amos Ethics Os Governor
type: skill
source: 07_SKILLS/amos-ethics-os-governor
name: amos-ethics-os-governor
description: Ethics Os Governor — organization, law and policy capability. Use when
  governance design, legal analysis, or policy reasoning. Use when amos-c09-org-law-policy-master
  routes to this specialized capability. Do not use for generic tasks outside c09
  domain.
parent_skill: amos-c09-org-law-policy-master
domain: c09
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- type/skill
- domain/org-law-policy
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

# Ethics Os Governor

## Identity

Origin architect: **Trang Phan**. Domain: c09. Parent: amos-c09-org-law-policy-master. Epistemic class: SOURCE_CLAIM. H/M/L: H.
## When to Use

- When governing ethical decisions: principles, consequences, procedural fairness
- When enforcing risk constraints: acceptable risk, budget, escalation
- When assessing trust formation: evidence, reputation, accountability
- When evaluating actions against 6 ethical integrity axes
- When determining ALLOW/CONDITIONAL/BLOCK decisions for proposed actions
- When the parent skill (`amos-c09-org-law-policy-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **ethics.govern_ethics**: Govern ethical decisions: principles, consequences, and procedural fairness
- **ethics.enforce_risk_constraint**: Enforce risk constraints: acceptable risk, risk budget, and risk escalation
- **ethics.assess_trust**: Assess trust formation: evidence, reputation, and accountability mechanisms
- **ethics.evaluate_action**: Evaluate action impact across 6 ethical integrity axes
- **ethics.classify_decision**: Classify ethical decisions: ALLOW, CONDITIONAL, or BLOCK
- **ethics.detect_drift**: Detect drift in ethical policy, axis weights, or threshold calibration
- **ethics.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **ethics.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Operations

1. **ethics.govern_ethics**: Govern ethical decisions: principles, consequences, and procedural fairness
2. **ethics.enforce_risk_constraint**: Enforce risk constraints: acceptable risk, risk budget, and risk escalation
3. **ethics.assess_trust**: Assess trust formation: evidence, reputation, and accountability mechanisms
4. **ethics.evaluate_action**: Evaluate action impact across 6 ethical integrity axes
5. **ethics.classify_decision**: Classify ethical decisions: ALLOW, CONDITIONAL, or BLOCK
6. **ethics.detect_drift**: Detect drift in ethical policy, axis weights, or threshold calibration
7. **ethics.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
8. **ethics.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Domain Knowledge

> **Source**: `_00_Cosmo brain/amos-general/A/CORE/AMOS_CORE - FULL.md` (content_hash: 70a3efa841e64e65) (vault canon, SOURCE_CLAIM)

### Universal Ethical Alignment Engine (UEAE)

The UEAE evaluates actions across 6 ethical integrity axes:

| Axis | Focus |
|------|-------|
| BIOLOGICAL_INTEGRITY | Impact on biological systems and health |
| SYSTEMIC_INTEGRITY | Impact on system structure and stability |
| TEMPORAL_INTEGRITY | Impact across time horizons |
| INFORMATIONAL_INTEGRITY | Impact on information quality and access |
| PLANETARY_INTEGRITY | Impact on planetary-scale systems |
| RELATIONAL_INTEGRITY | Impact on relationships and trust |

### Ethical Decision Types

- **ALLOW**: Action passes all axis thresholds and uncertainty penalties
- **CONDITIONAL**: Action passes with conditions or mitigations required
- **BLOCK**: Action fails one or more hard breach thresholds

### Action Impact Model

Each action is evaluated with:
- `axis_impacts`: per-axis impact scores
- `scope`: scope of impact (local, systemic, planetary)
- `reversibility`: how reversible the action is
- `uncertainty`: uncertainty penalty applied to scores

### Ethical Policy Parameters

- `min_axis_score`: minimum acceptable score per axis
- `axis_weights`: relative importance of each axis
- `allow_threshold`: threshold for ALLOW decision
- `block_threshold`: threshold for BLOCK decision
- `hard_breach_detection`: minimum integrity requirements that cannot be compensated

### Epistemic Boundary

Ethical alignment is AMOS_MODEL. The UEAE is a structural ethics governance framework, NOT a moral philosophy claim or legal compliance system. Always recommend professional legal and ethical review for consequential decisions.

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
- **G5 (Equation fire

---
**Links:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Related

- [[07_SKILLS/amos-ethics-os-governor/amos-ethics-os-governor_MOC|amos-ethics-os-governor_MOC]]

## Examples

- **Scenario**: When governing ethical decisions: principles, consequences, procedural fairness
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
- `` — skill Map of Content
- `amos-c09-org-law-policy-master` — parent skill
- `` — corresponding workflow
- `amos-ethics-os-governor-agent` — corresponding agent
---

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-ethics-os-governor
node_type: skill
path: 07_SKILLS/amos-ethics-os-governor/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
