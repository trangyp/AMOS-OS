---
title: SKILL — Amos Fx Carry Differential Engine
type: skill
source: 07_SKILLS/amos-fx-carry-differential-engine
name: amos-fx-carry-differential-engine
description: Carry Differential Engine — forex and finance capability. Use when forex analysis, currency
  trading, or market dynamics. Use when amos-c07-econ-finance-master routes to this specialized capability.
parent_skill: amos-c07-econ-finance-master
domain: fx
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/econ-finance
- rscf/source_claim
- hml/m
- epistemic/source_claim
- amos_os
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
---








# Fx Carry Differential Engine

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

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-fx-carry-differential-engine_MOC]]

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


## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `[[amos-fx-carry-differential-engine_MOC]]` — skill Map of Content
- `amos-c07-econ-finance-master` — parent skill
- `[[amos-fx-carry-differential-engine-workflow]]` — corresponding workflow
- `amos-fx-carry-differential-engine-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-fx-carry-differential-engine
node_type: skill
path: 07_SKILLS/amos-fx-carry-differential-engine/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
