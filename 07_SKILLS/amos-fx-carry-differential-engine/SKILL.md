---
title: SKILL
type: skill
name: amos-fx-carry-differential-engine
description: Carry Differential Engine — forex and finance capability. Use when forex analysis, currency trading, or market dynamics. Use when amos-c07-econ-finance-master routes to this specialized capability.
parent_skill: amos-c07-econ-finance-master
domain: fx
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-fx-carry-differential-engine]
---


# Fx Carry Differential Engine

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c07-econ-finance-master`
- **Domain**: fx
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

FX market analysis engine for Fx Carry Differential Engine

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

- **carry_differential.calibrate_model**: Calibrate FX models: Bayesian neural SDEs, volatility surfaces, and term structures
- **carry_differential.assess_risk**: Assess FX risk: currency exposure, correlation breakdown, and tail events
- **carry_differential.backtest_strategy**: Backtest FX strategies: walk-forward, regime-aware, and stress-tested
- **carry_differential.monitor_regime**: Monitor FX regime shifts: volatility, correlation, and liquidity transitions

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 609d26ed187f95a8) for the full vault-sourced domain knowledge (9510 chars).
- **carry_differential.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **carry_differential.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **carry_differential.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/misc/F/FOREX LOOPHOLES.md` (content_hash: 46b37b527f6fcbac) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C07_ECON_FINANCE_MASTER_KNOWLEDGE.md` (content_hash: afc81525bb75994d) (vault canon, SOURCE_CLAIM)

### FX Carry Differential Engine

From Cosmo Brain FOREX LOOPHOLES: Carry trade flip strategy, swap arbitrage, and swap on holiday. From C07 Econ & Finance: FX carry trade analysis.

**Carry trade model**:
- **Carry trade**: trade pairs with largest positive swap (e.g., long AUD/JPY)
- **Price may go flat or decline slightly** but swap compensates
- **Profit**: 5-15%/year (stable)

**Swap arbitrage**:
- Long pairs with positive swap at broker A
- Short same pair at broker B
- Swap differential is daily profit

**Swap on holiday**:
- Hold positions through holidays
- Holiday swap is 2-5x higher
- If positive swap = large profit

**Spread profit equation** (SOURCE_DERIVED):
```
Spread_Profit = (Ask_max - Bid_min) × Contraction_Coefficient
```

**Carry differential laws**:
- `CARRY != ARBITRAGE`: carry trade earns swap; arbitrage exploits price differences
- `SWAP != INTEREST**: swap is the FX equivalent of interest; it is not the same as interest rates
- `HOLIDAY_SWAP != DAILY_SWAP**: holiday swap is 2-5x higher than daily swap

**Risk warning**: Carry trades can lose money if the currency pair moves against the position. The swap income may not compensate for the price loss. This is an AMOS_MODEL, not financial advice.

### Epistemic Boundary

FX carry differential engine is an AMOS_MODEL. It does not prove carry trades are always profitable, that swap differentials persist, or that the strategy is risk-free.

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
- **G4 (Anti-overreac