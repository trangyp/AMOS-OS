---
title: SKILL
type: skill
name: amos-fx-state-space-kalman-engine
description: State Space Kalman Engine — forex and finance capability. Use when forex analysis, currency trading, or market dynamics. Use when amos-c07-econ-finance-master routes to this specialized capability.
parent_skill: amos-c07-econ-finance-master
domain: fx
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-fx-state-space-kalman-engine]
---


# Fx State Space Kalman Engine

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c07-econ-finance-master`
- **Domain**: fx
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

FX market analysis engine for Fx State Space Kalman Engine

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

- **state_space.calibrate_model**: Calibrate FX models: Bayesian neural SDEs, volatility surfaces, and term structures
- **state_space.assess_risk**: Assess FX risk: currency exposure, correlation breakdown, and tail events
- **state_space.backtest_strategy**: Backtest FX strategies: walk-forward, regime-aware, and stress-tested
- **state_space.monitor_regime**: Monitor FX regime shifts: volatility, correlation, and liquidity transitions

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: d67d03ec3e72a507) for the full vault-sourced domain knowledge (10170 chars).
- **state_space.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **state_space.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **state_space.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_C07_ECON_FINANCE_MASTER_KNOWLEDGE.md` (content_hash: afc81525bb75994d) (vault canon, SOURCE_CLAIM)

### FX State-Space Kalman Engine

From C07: Regime superposition with posterior weights. All outputs MODEL.

**State-space model**:
- **State vector**: unobserved true state (regime, level, trend)
- **Observation vector**: observed market data (prices, volumes, spreads)
- **Transition model**: how state evolves over time
- **Observation model**: how state maps to observations

**Kalman filter protocol**:
1. **Predict**: predict next state from transition model
2. **Update**: update state estimate with new observation
3. **Compute posterior**: compute posterior state distribution
4. **Tag regime**: tag current regime with posterior weights
5. **Flag uncertainty**: flag when posterior uncertainty is high

**Regime posteriors**: Regime classes (trend/range/crisis) hold posterior weights updated on macro evidence. No single regime is asserted while alternatives retain material probability.

**Law**: `FILTERED != CERTAIN`. Kalman-filtered estimates are uncertain; posterior variance must be reported.

### Epistemic Boundary

FX state-space Kalman engine is an analytical model. It does not prove optimal filtering, that the state-space model is correct, or that estimates converge to truth.

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

- **Skill**: `amos-fx-state-space-kalman-engine`
- **Parent**: 