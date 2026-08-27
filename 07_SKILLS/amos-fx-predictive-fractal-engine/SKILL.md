---
title: SKILL
type: skill
name: amos-fx-predictive-fractal-engine
description: Predictive Fractal Engine — forex and finance capability. Use when forex analysis, currency trading, or market dynamics. Use when amos-c07-econ-finance-master routes to this specialized capability.
parent_skill: amos-c07-econ-finance-master
domain: fx
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-fx-predictive-fractal-engine]
---


# Fx Predictive Fractal Engine

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c07-econ-finance-master`
- **Domain**: fx
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

FX market analysis engine for Fx Predictive Fractal Engine

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

- **predictive_fractal.calibrate_model**: Calibrate FX models: Bayesian neural SDEs, volatility surfaces, and term structures
- **predictive_fractal.assess_risk**: Assess FX risk: currency exposure, correlation breakdown, and tail events
- **predictive_fractal.backtest_strategy**: Backtest FX strategies: walk-forward, regime-aware, and stress-tested
- **predictive_fractal.monitor_regime**: Monitor FX regime shifts: volatility, correlation, and liquidity transitions

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: ca2a844eb70a525c) for the full vault-sourced domain knowledge (9433 chars).
- **predictive_fractal.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **predictive_fractal.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **predictive_fractal.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_C07_ECON_FINANCE_MASTER_KNOWLEDGE.md` (content_hash: afc81525bb75994d) (vault canon, SOURCE_CLAIM)

### FX Predictive Fractal Engine

From C07 H5: Structural levels via fractal recurrence. All outputs MODEL; never trading advice.

**Fractal recurrence model**:
- **Multi-timeframe recurrence**: structural levels identified through recurrence match across timeframes
- **Level confirmation**: a level counts only when confirmed across timeframes; single-timeframe levels are observations, not structure
- **Validity decay**: levels are conditional reference points whose validity decays with regime change

**Epistemic status**: Fractal recurrence is a pattern-description device (MODEL), not a proven physical law of markets.

**Prediction protocol**:
1. Identify structural levels via multi-timeframe recurrence
2. Tag with regime (trend/range/crisis) using posterior weights
3. Map entangled pairs (correlated currency pairs)
4. Apply risk tags (LOW/MEDIUM/HIGH/UNKNOWN)
5. Tag all outputs as MODEL with assumption registers

**Law**: `PATTERN != PREDICTION`. A fractal pattern is a structural observation, not a prediction.

### Epistemic Boundary

FX predictive fractal engine is an analytical model. It does not prove fractal patterns predict FX movements, that levels are permanent, or that predictions are trading advice.

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

##