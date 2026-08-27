---
title: SKILL
type: skill
name: amos-forex-unified-os
description: Forex Unified Os — forex and finance capability. Use when forex analysis, currency trading, or market dynamics. Use when amos-c07-econ-finance-master routes to this specialized capability.
parent_skill: amos-c07-econ-finance-master
domain: fx
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-forex-unified-os]
---


# Forex Unified Os

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c07-econ-finance-master`
- **Domain**: fx
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

FX market analysis engine for Forex Unified Os

## When to Use

- When calibrating FX models: Bayesian neural SDEs, volatility surfaces
- When assessing FX risk: currency exposure, correlation, tail events
- When backtesting FX strategies: walk-forward, regime-aware, stress-tested
- When monitoring FX regime shifts: volatility, correlation, liquidity
- When classifying FX regimes: stable, transitioning, volatile, stressed, crisis
- When the parent skill (`amos-c07-econ-finance-master`) routes to this specialized capability

## Capabilities

- **forex_unified.calibrate_model**: Calibrate FX models: Bayesian neural SDEs, volatility surfaces, and term structures
- **forex_unified.assess_risk**: Assess FX risk: currency exposure, correlation breakdown, and tail events
- **forex_unified.backtest_strategy**: Backtest FX strategies: walk-forward, regime-aware, and stress-tested
- **forex_unified.monitor_regime**: Monitor FX regime shifts: volatility, correlation, and liquidity transitions
- **forex_unified.classify_regime**: Classify FX regime: stable, transitioning, volatile, stressed, crisis
- **forex_unified.detect_drift**: Detect drift in FX models, regime classification, or risk metrics
- **forex_unified.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **forex_unified.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Domain Knowledge

> **Source**: `_00_Cosmo brain/engine/A/amos_omega_fx_engine.md` (content_hash: 39bf5e55cc49ed6c) (vault canon, SOURCE_CLAIM)

### FX Regime Classification

The Omega FX Engine classifies markets into 5 regime types:

| Regime | Description |
|--------|-------------|
| STABLE | Low volatility, tight spreads, high liquidity |
| TRANSITIONING | Shifting volatility, widening spreads |
| VOLATILE | High volatility, normal liquidity |
| STRESSED | Very high volatility, reduced liquidity |
| CRISIS | Extreme volatility, liquidity collapse, spread blowout |

### Shock Types

- **LIQUIDITY**: liquidity squeeze, funding stress
- **VOLATILITY**: volatility spike, regime break
- **POLICY**: central bank policy shift
- **CONTAGION**: cross-market spillover
- **EXTERNAL**: external macro shock

### Core FX Structural Metrics

- `price`: current price level
- `volatility`: realized volatility measure
- `volume`: trading volume
- `spread`: bid-ask spread
- `liquidity_score`: composite liquidity metric [0, 1]
- `momentum`: directional momentum
- `mean_reversion_score`: mean reversion tendency
- `correlation_index`: cross-currency correlation

### Epistemic Boundary

The Omega FX Engine is **structural (NOT predictive)** FX analysis. It provides regime classification, fragility gradients, and coupling heatmaps — NOT price predictions or trading signals. All FX analysis is AMOS_MODEL. `not_investment_advice` — outputs are structural analysis, not investment recommendations.

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


> **Reference**: See `references/fractal_forex_enterprise.md` (content_hash: 5ca9b48c2e447325) for the Fractal Forex Enterprise (fractal FX analysis, enterprise-scale forex, multi-timeframe fractal pattern