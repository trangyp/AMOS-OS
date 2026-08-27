---
title: SKILL
type: skill
name: amos-context-orientation-cache-rscf
description: Context Orientation Cache — boundary and scope capability. Use when evaluating scope boundaries, context continuity, or capability bounds. Use when amos-boundary-scope-master routes to this specialized capability.
parent_skill: amos-boundary-scope-master
domain: boundary
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-context-orientation-cache-rscf]
---


# Context Orientation Cache Rscf

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-boundary-scope-master`
- **Domain**: boundary
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Boundary and scope governance for Context Orientation Cache Rscf

## When to Use

- When boundary and scope governance for context orientation cache rscf is needed within the boundary domain
- When the parent skill (`amos-boundary-scope-master`) routes to this specialized capability
- When a query requires boundary-specific reasoning grounded in vault sources
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **context_orientation.evaluate_scope**: Evaluate scope boundaries: what is in-scope, out-of-scope, and at the boundary
- **context_orientation.check_admission**: Check admission criteria: whether a query enters this capability legitimately
- **context_orientation.detect_drift**: Detect context drift, persona drift, or scope creep beyond authorized bounds
- **context_orientation.enforce_compaction**: Enforce context compaction and recoverability when budget is exceeded
- **context_orientation.audit_boundary**: Audit boundary crossings and log violations for governance review
- **context_orientation.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **context_orientation.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 97f65efe940db593) for the full vault-sourced domain knowledge (4512 chars).

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
- **G6 (Failure mode)**: On validation failure, downgrade confidence, flag the gap, escalate

---
**Links:** [[07_SKILLS_MOC]]
