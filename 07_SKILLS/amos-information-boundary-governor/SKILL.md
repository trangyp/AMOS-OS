---
title: SKILL
type: skill
name: amos-information-boundary-governor
description: Information Boundary Governor — boundary and scope capability. Use when evaluating scope boundaries, context continuity, or capability bounds. Use when amos-boundary-scope-master routes to this specialized capability.
parent_skill: amos-boundary-scope-master
domain: boundary
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-information-boundary-governor]
---


# Information Boundary Governor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-boundary-scope-master`
- **Domain**: boundary
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Boundary and scope governance for Information Boundary Governor

## When to Use

- When boundary and scope governance for information boundary governor is needed within the boundary domain
- When the parent skill (`amos-boundary-scope-master`) routes to this specialized capability
- When a query requires boundary-specific reasoning grounded in vault sources
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **information_boundary.evaluate_scope**: Evaluate scope boundaries: what is in-scope, out-of-scope, and at the boundary
- **information_boundary.check_admission**: Check admission criteria: whether a query enters this capability legitimately
- **information_boundary.detect_drift**: Detect context drift, persona drift, or scope creep beyond authorized bounds
- **information_boundary.enforce_compaction**: Enforce context compaction and recoverability when budget is exceeded
- **information_boundary.audit_boundary**: Audit boundary crossings and log violations for governance review

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: d455529878c13257) for the full vault-sourced domain knowledge (8752 chars).
- **information_boundary.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **information_boundary.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Information Boundary Governance

The Cognitive Organism OS defines information boundaries to control what information enters, exits, and flows within the system.

**Boundary specification**: `B_i = <Inside, Outside, Ingress, Egress, Permissions, Permeability>`

**Information boundary laws**:
- `EXPOSURE != DISCLOSURE`: being exposed to information does not authorize disclosing it
- `OBSERVED != SHARED`: observing information does not authorize sharing it
- `INTERNAL != EXTERNAL`: internal state is not external state without explicit egress authorization

**Ingress gates**: What information may enter the system
- Source verification: information source must be verified
- Scope check: information must be within system's declared scope
- Freshness check: information must be within its validity window

**Egress gates**: What information may leave the system
- Authority check: egress requires explicit authority
- Redaction: sensitive information must be redacted before egress
- Provenance: egress records what left and why

### Epistemic Boundary

Information boundary governance is an architectural construct. It does not prove absolute information security, impossibility of leakage, or information-theoretic confidentiality.

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

- **Skill**: `amos-information-boundary-governor