---
title: SKILL
type: skill
name: amos-counterfactual-reasoning-governor
description: Counterfactual Reasoning Governor — causal reasoning capability. Use when causal analysis, counterfactual reasoning, or intervention design. Use when amos-causal-reasoning-master routes to this specialized capability.
parent_skill: amos-causal-reasoning-master
domain: causal
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-counterfactual-reasoning-governor]
---


# Counterfactual Reasoning Governor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-causal-reasoning-master`
- **Domain**: causal
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Causal reasoning engine for Counterfactual Reasoning Governor

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

- **counterfactual_reasoning.validate_abstraction**: Validate causal abstraction: does the higher-level model preserve causal structure?
- **counterfactual_reasoning.enforce_closure**: Enforce causal closure: every effect must have a sufficient cause within the system
- **counterfactual_reasoning.govern_hierarchy**: Govern causal hierarchy: direct, distributed, delayed, and cascading causes
- **counterfactual_reasoning.reason_counterfactual**: Reason counterfactually: what would happen under alternative interventions

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: ef41fd5a1688a1f8) for the full vault-sourced domain knowledge (9239 chars).
- **counterfactual_reasoning.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **counterfactual_reasoning.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **counterfactual_reasoning.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/kernel/A/AMOS_Counterfactual_Reasoning_Kernel_v0_Meta_Cognition4_2.md` (content_hash: 8809484d7b9a31de) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Counterfactual Reasoning

From Cosmo Brain Counterfactual Reasoning Kernel v0: What-if analysis, alternative scenario reasoning, and causal inference through comparison of actual vs hypothetical states.

**4 Counterfactual types**:
- **Past counterfactual**: What would have happened if something in the past had been different? (e.g., "If we had launched earlier...")
- **Future counterfactual**: What would happen if something changes in the future? (e.g., "If we increase price by 10%...")
- **Structural counterfactual**: What does the structure imply would happen under different conditions? (e.g., "Given this system design, if load doubles...")
- **Causal counterfactual**: What can we infer about causation by comparing what happened with what would have happened without the cause?

**5 Valid counterfactual criteria**:
1. **Plausible initial state**: the counterfactual starting point must be plausible or clearly flagged as implausible
2. **Minimal change principle**: change only what's necessary; don't silently change other things
3. **Causal chain conservation**: respect the causal structure (A->B->C, changing A propagates through B to C)
4. **Uncertainty proportionate**: the further from actuality, the larger the uncertainty
5. **Assumption transparency**: all assumptions about how the world would differ must be explicit

**4 Rules**:
1. `counterfactual_needs_causal_model`: valid counterfactual reasoning requires a causal model; without it, you're guessing
2. `uncertainty_grows_with_distance`: the more different the counterfactual world is from actuality, the larger the uncertainty
3. `minimal_intervention`: change only what's specified; don't silently assume other things stay the same
4. `counterfactual_is_not_prediction`: a counterfactual is a reasoned exploration of alternatives, not a prediction

**5 Safety constraints**:
- Never present counterfactual as fact
- Never ignore uncertainty in far counterfactuals
- Always state assumptions explicitly
- Always label counterfactual as counterfactual
- Never use counterfactual to over-determine outcomes

**3 Functions**: `construct_counterfactual`, `compare_actual_vs_counterfactual`, `scenario_analysis`

### Epistemic Boundary

---
**Links:** [[07_SKILLS_MOC]]
