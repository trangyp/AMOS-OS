---
title: SKILL
type: skill
name: amos-risk-constraint-governor
description: Risk Constraint Governor — organization, law and policy capability. Use when governance design, legal analysis, or policy reasoning. Use when amos-c09-org-law-policy-master routes to this specialized capability.
parent_skill: amos-c09-org-law-policy-master
domain: c09
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-risk-constraint-governor]
---


# Risk Constraint Governor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c09-org-law-policy-master`
- **Domain**: c09
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Governance, law and policy engine for Risk Constraint Governor

## When to Use

- When governing ethical decisions: principles, consequences, procedural fairness
- When enforcing risk constraints: acceptable risk, risk budget, escalation thresholds
- When assessing trust formation: evidence, reputation, accountability mechanisms
- When designing governance structures: role clarity, accountability mapping, regulatory scanning
- When the parent skill (`amos-c09-org-law-policy-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **risk_constraint.govern_ethics**: Govern ethical decisions: principles, consequences, and procedural fairness
- **risk_constraint.enforce_risk_constraint**: Enforce risk constraints: acceptable risk, risk budget, and risk escalation
- **risk_constraint.assess_trust**: Assess trust formation: evidence, reputation, and accountability mechanisms
- **risk_constraint.design_governance**: Design governance structures: role/responsibility clarity, accountability mapping
- **risk_constraint.detect_drift**: Detect governance drift: authority decay, accountability erosion, regulatory change
- **risk_constraint.escalate_gaps**: Escalate governance gaps: flag constitutional issues, require legal review
- **risk_constraint.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **risk_constraint.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Domain Knowledge

> **Source**: `_00_Cosmo brain/misc/C0/C09_org_law_policy.md` (content_hash: 302e0c57d6667297) (vault canon, SOURCE_CLAIM)

### C09 Org, Law & Policy Domain

- **Focus**: Org design, governance, legal constraints, policy mechanics
- **Module ID**: `C09_org_law_policy`

### Typical Questions

- Which governance structure fits these goals?
- Where will accountability actually sit?
- Which legal and regulatory constraints shape this design?

### Core Methods

- `role_and_responsibility_clarity` — clarify who owns what decision and consequence
- `governance_mechanism_design` — design governance mechanisms matching organizational goals
- `regulatory_landscape_scanning` — scan regulatory landscape for binding constraints
- `policy_impact_pathways` — trace policy decisions through impact pathways

### Risk Notes

- `not_formal_legal_advice` — outputs are structural analysis, not legal advice
- `local_law_variation_can_be_large` — local jurisdiction variation can be significant

### Interfaces

**Inputs**: natural language questions, structured prompts, tabular data, narrative case descriptions

**Outputs**: structured reasoning steps, tables and summaries, scenario trees, recommendations with assumptions

### Epistemic Boundary

Governance design is SOURCE_CLAIM (vault-sourced framework). Legal analysis is NOT formal legal advice — always recommend professional legal review for consequential decisions.

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
- **G6 (Failure mode)**: On 