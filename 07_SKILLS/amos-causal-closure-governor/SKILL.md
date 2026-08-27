---
title: SKILL
type: skill
name: amos-causal-closure-governor
description: Causal Closure Governor — causal reasoning capability. Use when causal analysis, counterfactual reasoning, or intervention design. Use when amos-causal-reasoning-master routes to this specialized capability.
parent_skill: amos-causal-reasoning-master
domain: causal
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-causal-closure-governor]
---


# Causal Closure Governor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-causal-reasoning-master`
- **Domain**: causal
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Causal reasoning engine for Causal Closure Governor

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

- **causal_closure.validate_abstraction**: Validate causal abstraction: does the higher-level model preserve causal structure?
- **causal_closure.enforce_closure**: Enforce causal closure: every effect must have a sufficient cause within the system
- **causal_closure.govern_hierarchy**: Govern causal hierarchy: direct, distributed, delayed, and cascading causes
- **causal_closure.reason_counterfactual**: Reason counterfactually: what would happen under alternative interventions
- **causal_closure.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **causal_closure.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **causal_closure.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: fe5db79e174e18cc) for the full vault-sourced domain knowledge (5270 chars).

## Cosmo Brain Vault Content

> **Source**: `_00_Cosmo brain/trang/trang_amos_reality_architecture_master_max_detail.md` (vault canon, SOURCE_CLAIM)

### Causal Closure Principle

Causal closure states that every physical effect has a sufficient physical cause. Applied to AMOS:

**Causal closure law**: Every system state change must trace to a sufficient causal chain within the system's declared boundary.

**Closure requirements**:
- Every effect has a cause within the system boundary
- No "spooky action" -- uncaused state changes are flagged as UNKNOWN/GAP
- Causal chains must be traceable through the provenance graph
- External inputs are causes at the boundary, not violations of closure

### 6 Causal Modes

| Mode | Description | Example |
|------|-------------|---------|
| C0 Direct | A causes B directly | Function call returns value |
| C1 Distributed | Multiple causes converge | Multiple evidence sources support a claim |
| C2 Delayed | Cause precedes effect in time | Memory encoding enables later retrieval |
| C3 Cascading | Cause triggers chain | Gap detection triggers repair triggers validation |
| C4 Feedback | Effect feeds back to cause | Learning loop updates inference |
| C5 Counterfactual | What would happen without cause | Falsifier testing |

### Anti-Faking Mechanism

Causal closure governance includes anti-faking mechanisms that penalize:
- Narrative drift: claims that drift from their causal origin
- Deception gaps: missing causal links presented as complete
- Unsupported speculation: claims without causal backing

### Epistemic Boundary

Causal closure is an architectural principle, not a metaphysical claim. It does not prove determinism, physicalism, or the impossibility of emergent causation. It is a governance constraint, not a physics theorem.

## Failure Modes
- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the skill's scope.
- **G2 (Epistemic class)**: All claims labeled SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL — never claim beyond evidence.
- **G3 (Provenance)**: Source path recorded 