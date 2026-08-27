---
title: SKILL
type: skill
name: amos-counterfactual-selfhood-mapper
description: Counterfactual Selfhood Mapper — causal reasoning capability. Use when causal analysis, counterfactual reasoning, or intervention design. Use when amos-causal-reasoning-master routes to this specialized capability.
parent_skill: amos-causal-reasoning-master
domain: causal
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-counterfactual-selfhood-mapper]
---


# Counterfactual Selfhood Mapper

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-causal-reasoning-master`
- **Domain**: causal
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Causal reasoning engine for Counterfactual Selfhood Mapper

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

- **counterfactual_selfhood.validate_abstraction**: Validate causal abstraction: does the higher-level model preserve causal structure?
- **counterfactual_selfhood.enforce_closure**: Enforce causal closure: every effect must have a sufficient cause within the system
- **counterfactual_selfhood.govern_hierarchy**: Govern causal hierarchy: direct, distributed, delayed, and cascading causes
- **counterfactual_selfhood.reason_counterfactual**: Reason counterfactually: what would happen under alternative interventions

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: df869b1e6ab5a677) for the full vault-sourced domain knowledge (9620 chars).
- **counterfactual_selfhood.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **counterfactual_selfhood.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **counterfactual_selfhood.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Counterfactual Selfhood Mapping

The Cognitive Organism OS defines counterfactual selfhood as the exploration of "what would the self be like under different conditions."

**Counterfactual selfhood model**: `SelfModel(conditions) = f(Identity, Continuity, Boundary, Self-awareness)`

**Counterfactual dimensions**:
- **Identity counterfactual**: what if the system had different identity parameters?
- **Continuity counterfactual**: what if the system's continuity was interrupted?
- **Boundary counterfactual**: what if the system's boundaries were different?
- **Self-awareness counterfactual**: what if the system's self-awareness level changed?

**Mapping protocol**:
1. **Declare current self-model**: identity, continuity, boundary, self-awareness
2. **Construct counterfactual**: vary one dimension while holding others constant
3. **Map the counterfactual self**: what would the self-model look like?
4. **Compare**: how does the counterfactual self differ from the actual self?
5. **Classify**: STRUCTURAL (same structure, different parameters), FUNCTIONAL (different structure, same function), INCOMMENSURABLE (no comparison possible)

**Law**: `SELF_MODEL != SUBJECTIVE_SELF`. The counterfactual self is a model exploration, not a phenomenological claim.

### Epistemic Boundary

Counterfactual selfhood mapping is an analytical model. It does not prove the system has a self, that counterfactual selves are real, or that selfhood is mappable in all dimensions.

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
- **G4 (Anti-overreach)**: No claim be

---
**Links:** [[07_SKILLS_MOC]]
