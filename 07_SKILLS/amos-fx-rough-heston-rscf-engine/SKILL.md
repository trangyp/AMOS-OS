---
title: SKILL
type: skill
name: amos-fx-rough-heston-rscf-engine
description: Rough Heston — forex and finance capability. Use when forex analysis, currency trading, or market dynamics. Use when amos-c07-econ-finance-master routes to this specialized capability.
parent_skill: amos-c07-econ-finance-master
domain: fx
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-fx-rough-heston-rscf-engine]
---


# Fx Rough Heston Rscf Engine

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c07-econ-finance-master`
- **Domain**: fx
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

FX market analysis engine for Fx Rough Heston Rscf Engine

## When to Use

- When calibrating FX models: Bayesian neural SDEs, volatility surfaces
- When assessing FX risk: currency exposure, correlation, tail events
- When backtesting FX strategies: walk-forward, regime-aware, stress-tested
- When monitoring FX regime shifts: volatility, correlation, liquidity
- When the parent skill (`amos-c07-econ-finance-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **rough_heston.calibrate_model**: Calibrate FX models: Bayesian neural SDEs, volatility surfaces, and term structures
- **rough_heston.assess_risk**: Assess FX risk: currency exposure, correlation breakdown, and tail events
- **rough_heston.backtest_strategy**: Backtest FX strategies: walk-forward, regime-aware, and stress-tested
- **rough_heston.monitor_regime**: Monitor FX regime shifts: volatility, correlation, and liquidity transitions

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: ddd9730b950f702f) for the full vault-sourced domain knowledge (9482 chars).
- **rough_heston.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **rough_heston.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **rough_heston.validate_outputs**: Validate outputs against domain constraints and epistemic class.

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
- **G6 (Failure mode)**: On validation failure, downgrade confidence, flag th

---
**Links:** [[07_SKILLS_MOC]]
