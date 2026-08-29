---
schema_version: 1.0
title: SKILL — Amos Forex Unified Os
type: skill
source: 07_SKILLS/amos-forex-unified-os
name: amos-forex-unified-os
description: Forex Unified Os — forex and finance capability. Use when forex analysis,
  currency trading, or market dynamics. Use when amos-c07-econ-finance-master routes
  to this specialized capability. Do not use for generic tasks outside fx domain.
parent_skill: amos-c07-econ-finance-master
domain: fx
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- type/skill
- domain/econ-finance
- epistemic/source_claim
- hml/m
- epistemic/source_claim
- amos-os
- 07-skills-moc
- amos-forex-unified-os-moc
- 00-home
- amos-rscf-nodes
- law-hierarchy
- references-moc
- trang-framework-recursive-ontology-dynamics
- skill
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
rscf_state: SOURCE_CLAIM
hml_level: M
gmef_gates:
- L0_integrity
- L1_epistemic
- L2_provenance
- L5_scope
- L6_uncertainty
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L4
- L5
- L6
- L16
- L17
license: MIT
steward: Trang Phan
---

# Forex Unified Os

## Identity

Origin architect: **Trang Phan**. Domain: fx. Parent: amos-c07-econ-finance-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.
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

## Operations

1. **forex_unified.calibrate_model**: Calibrate FX models: Bayesian neural SDEs, volatility surfaces, and term structures
2. **forex_unified.assess_risk**: Assess FX risk: currency exposure, correlation breakdown, and tail events
3. **forex_unified.backtest_strategy**: Backtest FX strategies: walk-forward, regime-aware, and stress-tested
4. **forex_unified.monitor_regime**: Monitor FX regime shifts: volatility, correlation, and liquidity transitions
5. **forex_unified.classify_regime**: Classify FX regime: stable, transitioning, volatile, stressed, crisis
6. **forex_unified.detect_drift**: Detect drift in FX models, regime classification, or risk metrics
7. **forex_unified.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
8. **forex_unified.validate_outputs**: Validate outputs against domain constraints and epistemic class.

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

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-forex-unified-os_MOC]]

## Examples

- **Scenario**: When calibrating FX models: Bayesian neural SDEs, volatility surfaces
  - **Input**: A query matching this skill's domain (fx)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When assessing FX risk: currency exposure, correlation, tail events
  - **Input**: A query matching this skill's domain (fx)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When backtesting FX strategies: walk-forward, regime-aware, stress-tested
  - **Input**: A query matching this skill's domain (fx)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the fx domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-c07-econ-finance-master` — routes to this skill when fx specialization is needed
- **Peers**: Other skills in the `fx` domain may be composed in sequence
- **Orchestrator**: The parent skill or `AMOS_HOME` orchestrates routing
- **Workflow**: Each skill has a corresponding workflow in `08_WORKFLOWS/`
- **Agent**: Each skill has a corresponding agent in `06_AGENTS/`


## Evaluation

### Success Criteria

- Output includes epistemic class label (SOURCE/DERIVED/AMOS_MODEL/EMPIRICAL)
- Output includes provenance reference to source evidence
- Output includes confidence ceiling (capped at 0.95 for DERIVED, 1.0 for SOURCE_CANON)
- Output includes gap flags for unresolved unknowns
- Output does not exceed declared scope

### Failure Modes

- **Overreach**: Output claims validity beyond its epistemic class
- **Scope creep**: Output addresses questions outside the declared domain
- **Provenance loss**: Output cannot trace back to source evidence
- **Confidence inflation**: Output confidence exceeds the weakest-premise ceiling


## Error Handling

- **On scope violation**: Reject the query and route back to parent skill
- **On missing evidence**: Flag as GAP and reduce confidence ceiling to 0.5
- **On contradiction**: Flag as CRITICAL_GAP and halt until resolved
- **On provenance loss**: Mark output as UNKNOWN and require human review
- **On drift**: Trigger drift alignment via `amos-ai-drift-alignment-governor`


## Do not use

- For generic financial analysis outside the forex/engine framework
- To claim empirical validation of market efficiency or pricing models
- As a substitute for domain-specific financial or economic evidence
- Outside forex/finance domain reasoning

## References

- `references/fractal_forex_enterprise.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `` — skill Map of Content
- `amos-c07-econ-finance-master` — parent skill
- `` — corresponding workflow
- `amos-forex-unified-os-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-forex-unified-os
node_type: skill
path: 07_SKILLS/amos-forex-unified-os/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
