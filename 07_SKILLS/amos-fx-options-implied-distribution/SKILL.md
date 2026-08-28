---
title: SKILL — Amos Fx Options Implied Distribution
type: skill
source: 07_SKILLS/amos-fx-options-implied-distribution
name: amos-fx-options-implied-distribution
description: Options Implied Distribution — forex and finance capability. Use when forex analysis, currency trading, or market dynamics. Use when amos-c07-econ-finance-master routes to this specialized capability. Do not use for generic tasks outside fx domain.
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

# Fx Options Implied Distribution

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

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-fx-options-implied-distribution_MOC]]

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
- `[[amos-fx-options-implied-distribution_MOC]]` — skill Map of Content
- `amos-c07-econ-finance-master` — parent skill
- `[[amos-fx-options-implied-distribution-workflow]]` — corresponding workflow
- `amos-fx-options-implied-distribution-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-fx-options-implied-distribution
node_type: skill
path: 07_SKILLS/amos-fx-options-implied-distribution/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
