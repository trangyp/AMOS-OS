---
title: SKILL
type: skill
name: amos-scientific-closure-governor-rscf
description: Scientific Closure Governor — causal reasoning capability. Use when causal analysis, counterfactual reasoning, or intervention design. Use when amos-causal-reasoning-master routes to this specialized capability.
parent_skill: amos-causal-reasoning-master
domain: causal
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-scientific-closure-governor-rscf]
---


# Scientific Closure Governor Rscf

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-causal-reasoning-master`
- **Domain**: causal
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Causal reasoning engine for Scientific Closure Governor Rscf

## When to Use

- When validating causal abstraction across model levels
- When enforcing causal closure: every effect has a sufficient cause
- When governing causal hierarchy: direct, distributed, delayed, cascading
- When reasoning counterfactually about alternative interventions
- When the parent skill (`amos-causal-reasoning-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **scientific_closure.validate_abstraction**: Validate causal abstraction: does the higher-level model preserve causal structure?
- **scientific_closure.enforce_closure**: Enforce causal closure: every effect must have a sufficient cause within the system
- **scientific_closure.govern_hierarchy**: Govern causal hierarchy: direct, distributed, delayed, and cascading causes
- **scientific_closure.reason_counterfactual**: Reason counterfactually: what would happen under alternative interventions
- **scientific_closure.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **scientific_closure.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **scientific_closure.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: bdd4d2cb285a670d) for the full vault-sourced domain knowledge (7917 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Scientific Closure

Scientific closure governs when a scientific question is sufficiently answered to be considered "closed" within the AMOS framework.

**Closure criteria**:
1. **Hypothesis tested**: the hypothesis has been tested with declared falsifiers
2. **Evidence sufficient**: evidence meets the minimum for the claim class
3. **Contradictions resolved**: no unresolved contradictions remain
4. **Provenance complete**: full provenance chain is traceable
5. **Replication**: results have been independently replicated (for VERIFIED class)
6. **Peer review**: results have been reviewed (for VERIFIED class)

**Closure levels**:
- **CLOSED_VERIFIED**: all criteria met, independently verified
- **CLOSED_SOURCE**: source claims verified, not independently replicated
- **CLOSED_MODEL**: model-based closure, not empirically verified
- **OPEN**: still under investigation
- **BLOCKED**: cannot close due to insufficient evidence

**Law**: `Closure != Truth`. A closed question is sufficiently answered within the framework, not proven true in an absolute sense.

### Epistemic Boundary

Scientific closure is an epistemic governance construct. It does not prove absolute truth, finality, or that the answer will never be revised. Closure is operational, not metaphysical.

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

---
**Links:** [[07_SKILLS_MOC]]
