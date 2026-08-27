---
title: SKILL
type: skill
name: amos-trust-formation-governor
description: Trust Formation Governor — organization, law and policy capability. Use when governance design, legal analysis, or policy reasoning. Use when amos-c09-org-law-policy-master routes to this specialized capability.
parent_skill: amos-c09-org-law-policy-master
domain: c09
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-trust-formation-governor]
---


# Trust Formation Governor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c09-org-law-policy-master`
- **Domain**: c09
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Governance, law and policy engine for Trust Formation Governor

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