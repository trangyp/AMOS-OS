---
title: SKILL
type: skill
name: amos-fx-options-implied-distribution
description: Options Implied Distribution — forex and finance capability. Use when forex analysis, currency trading, or market dynamics. Use when amos-c07-econ-finance-master routes to this specialized capability.
parent_skill: amos-c07-econ-finance-master
domain: fx
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-fx-options-implied-distribution]
---


# Fx Options Implied Distribution

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c07-econ-finance-master`
- **Domain**: fx
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

FX market analysis engine for Fx Options Implied Distribution

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

- **options_implied.calibrate_model**: Calibrate FX models: Bayesian neural SDEs, volatility surfaces, and term structures
- **options_implied.assess_risk**: Assess FX risk: currency exposure, correlation breakdown, and tail events
- **options_implied.backtest_strategy**: Backtest FX strategies: walk-forward, regime-aware, and stress-tested
- **options_implied.monitor_regime**: Monitor FX regime shifts: volatility, correlation, and liquidity transitions

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: d9e23c4a2786a5a4) for the full vault-sourced domain knowledge (9510 chars).
- **options_implied.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **options_implied.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **options_implied.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_C07_ECON_FINANCE_MASTER_KNOWLEDGE.md` (content_hash: afc81525bb75994d) (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/amos-general/A/Infrastructure/AMOS_Infrastructure_Deep_Report_v23.md` (vault canon, SOURCE_CLAIM)

### FX Options Implied Distribution

From C07 H5: FX Structural Analysis with options-implied distributions. From Infrastructure Deep Report: FX-specific domain analysis with options-implied distributions.

**Options-implied distribution model**:
- **Implied volatility surface**: the surface of implied volatilities across strikes and maturities
- **Risk-neutral density**: the probability distribution implied by option prices
- **Tail extraction**: extracting tail risk from the implied distribution
- **Smile/skew analysis**: analyzing the volatility smile/skew for market sentiment

**FX-specific factors**:
- **Release/vintage timing**: economic release timing affects FX options
- **Volatility regime**: current volatility regime affects option pricing
- **Regime candidates**: multiple regime candidates with posterior weights
- **Conditional distributions**: distributions conditioned on regime
- **Options-implied distributions**: distributions implied by FX option prices
- **Tail risk**: tail risk extracted from implied distributions
- **Costs and liquidity**: transaction costs and liquidity affect option pricing
- **Portfolio exposure**: portfolio exposure affects option strategy
- **Backtests**: backtests validate option strategies
- **FX-specific competing hypotheses**: multiple hypotheses for FX option behavior

**Law**: `IMPLIED != ACTUAL`. The implied distribution is the market's risk-neutral expectation; it is not the actual distribution. `OPTION_PRICE != FORECAST`: option prices imply distributions; they do not forecast future exchange rates.

### Epistemic Boundary

FX options implied distribution is an analytical framework. It does not prove the implied distribution is correct, that option prices reflect all information, or that the distribution predicts future rates.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceed