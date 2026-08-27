---
title: SKILL
type: skill
name: amos-ethics-os-governor
description: Ethics Os Governor — organization, law and policy capability. Use when governance design, legal analysis, or policy reasoning. Use when amos-c09-org-law-policy-master routes to this specialized capability.
parent_skill: amos-c09-org-law-policy-master
domain: c09
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-ethics-os-governor]
---


# Ethics Os Governor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c09-org-law-policy-master`
- **Domain**: c09
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Governance, law and policy engine for Ethics Os Governor

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
**Links:** [[07_SKILLS_MOC]]
