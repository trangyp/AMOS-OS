---
schema_version: 1.0
title: SKILL — Amos Fx Macro Differential Mapper
type: skill
source: 07_SKILLS/amos-fx-macro-differential-mapper
name: amos-fx-macro-differential-mapper
description: Macro Differential Mapper — forex and finance capability. Use when forex
  analysis, currency trading, or market dynamics. Use when amos-c07-econ-finance-master
  routes to this specialized capability. Do not use for generic tasks outside fx domain.
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
- amos-fx-macro-differential-mapper-moc
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

# Fx Macro Differential Mapper

## Identity

Origin architect: **Trang Phan**. Domain: fx. Parent: amos-c07-econ-finance-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.
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

- **macro_differential.calibrate_model**: Calibrate FX models: Bayesian neural SDEs, volatility surfaces, and term structures
- **macro_differential.assess_risk**: Assess FX risk: currency exposure, correlation breakdown, and tail events
- **macro_differential.backtest_strategy**: Backtest FX strategies: walk-forward, regime-aware, and stress-tested
- **macro_differential.monitor_regime**: Monitor FX regime shifts: volatility, correlation, and liquidity transitions
- **macro_differential.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **macro_differential.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **macro_differential.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: bcc29e4e925cdc95) for the full vault-sourced domain knowledge (7449 chars).

## Operations

1. **macro_differential.calibrate_model**: Calibrate FX models: Bayesian neural SDEs, volatility surfaces, and term structures
2. **macro_differential.assess_risk**: Assess FX risk: currency exposure, correlation breakdown, and tail events
3. **macro_differential.backtest_strategy**: Backtest FX strategies: walk-forward, regime-aware, and stress-tested
4. **macro_differential.monitor_regime**: Monitor FX regime shifts: volatility, correlation, and liquidity transitions
5. **macro_differential.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
6. **macro_differential.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
7. **macro_differential.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/misc/G/Game.md` (content_hash: f116a25acc488148) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C07_ECON_FINANCE_MASTER_KNOWLEDGE.md` (content_hash: afc81525bb75994d) (vault canon, SOURCE_CLAIM)

### FX Macro Differential Mapper

From Cosmo Brain Game: FX macro in trading strategy context. Market architecture, trading power equations, Soros/Druckenmiller macro break trades, policy contradiction trades. From C07 Econ & Finance: FX macro analysis.

**FX macro differential model**:
- **Macro break trades**: Soros/Druckenmiller style -- identify macroeconomic breaks and trade the differential
- **Policy contradiction trades**: identify when policy contradicts economic reality and trade the differential
- **Board-flipping concepts**: identify when the market "board" flips from one state to another

**Differential mapping**:
- **Interest rate differential**: the differential between central bank rates
- **Inflation differential**: the differential between inflation rates
- **Growth differential**: the differential between growth rates
- **Policy differential**: the differential between policy stances
- **Sentiment differential**: the differential between market sentiment measures

**Mapping protocol**:
1. **Identify macro state**: identify the current macroeconomic state
2. **Identify differentials**: identify the key differentials
3. **Identify breaks**: identify potential macro breaks
4. **Identify contradictions**: identify policy contradictions
5. **Map**: map the differential structure
6. **Record**: record with provenance

**Mapping laws**:
- `DIFFERENTIAL != SPREAD`: a differential is a macroeconomic difference; a spread is a market price difference
- `MACRO != MICRO**: macro is economy-wide; micro is firm-specific
- `BREAK != TREND**: a break is a regime change; a trend is a continuation

**Risk warning**: FX macro trading carries significant risk. This is an AMOS_MODEL, not financial advice.

### Epistemic Boundary

FX macro differential mapping is an AMOS_MODEL. It does not prove macro breaks are predictable, that differentials predict exchange rates, or that the mapping is always correct.

## Failure Modes
- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail,

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-fx-macro-differential-mapper_MOC]]

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


## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

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

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `` — skill Map of Content
- `amos-c07-econ-finance-master` — parent skill
- `` — corresponding workflow
- `amos-fx-macro-differential-mapper-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-fx-macro-differential-mapper
node_type: skill
path: 07_SKILLS/amos-fx-macro-differential-mapper/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
