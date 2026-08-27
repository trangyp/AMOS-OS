---
title: SKILL
type: skill
name: amos-economic-model
description: Economic Model — econ capability. Use when executing the core capability within this domain. Use when amos-c07-econ-finance-master routes to this specialized capability.
parent_skill: amos-c07-econ-finance-master
domain: econ
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-economic-model]
---


# Economic Model

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c07-econ-finance-master`
- **Domain**: econ
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Economic model engine for Economic Model

## When to Use

- When governing agent economy: constitutional rules, monetary policy
- When modeling economic dynamics: supply, demand, price formation
- When assessing future debt and option value: intertemporal tradeoffs
- When the parent skill (`amos-c07-econ-finance-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **economic_model.govern_economy**: Govern agent economy: constitutional rules, monetary policy, and allocation
- **economic_model.model_economic**: Model economic dynamics: supply, demand, price formation, and equilibrium
- **economic_model.assess_debt**: Assess future debt and option value: intertemporal tradeoffs and commitments
- **economic_model.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **economic_model.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **economic_model.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: d865f64cecd4214a) for the full vault-sourced domain knowledge (6420 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/economy/Econ_Finance_Model.md` (content_hash: c5bb82643b0856ff) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C07_ECON_FINANCE_MASTER_KNOWLEDGE.md` (content_hash: afc81525bb75994d) (vault canon, SOURCE_CLAIM)

### Economic Model

From Cosmo Brain AMOS Economics & Finance Engine (vInfinity.1.0.0): Models firm behavior, macroeconomic cycles, public finance policy, and financial market risk.

**4 Core Sub-Kernels**:
1. **Microeconomics Kernel**: models preferences, constraints, technology, and market equilibria for firms and households
2. **Macroeconomics Kernel**: models the output gap, policy rates, expectations, and exogenous shocks affecting growth and inflation
3. **Public Finance Kernel**: tracks revenue, transfers, deficits, and intergenerational burdens for taxes and welfare
4. **Financial System Kernel**: models assets, liabilities, leverage, liquidity, and default risk in banks and capital markets

**3 Applied Engines**:
- **Sector Modelling Engine**: maps demand/supply profiles and shock propagation across sectors, connecting micro to macro impacts
- **Financial Risk Scenario Engine**: generates loss distributions and stress test results, highlighting tail risks
- **Policy Tradeoff Engine**: frames policy decisions as optimizations, extracting the Pareto frontier and mapping stakeholder impact

**3 Constraints**:
1. Never provide personalized investment advice
2. Flag high uncertainty for long-horizon economic forecasts
3. Avoid recommending illegal financial behaviour or market manipulation

**Economic model laws**:
- `MODEL != REALITY`: the economic model is an approximation; it is not the real economy
- `FORECAST != PREDICTION**: a forecast is a scenario projection; a prediction is a definite claim
- `EQUILIBRIUM != STABILITY**: equilibrium is a balance of forces; stability is resistance to perturbation

### Epistemic Boundary

Economic model is an AMOS_MODEL. It does not prove economic predictions are accurate, that the 4 sub-kernels are exhaustive, or that the model captures all economic dynamics.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the skill's scope.
- **G2 (Epistemic class)**: All claims labeled SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL — never claim beyond evid