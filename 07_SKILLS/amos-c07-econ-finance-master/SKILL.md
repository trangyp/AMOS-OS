---
title: SKILL — Amos C07 Econ Finance Master
type: skill
source: 07_SKILLS/amos-c07-econ-finance-master
name: amos-c07-econ-finance-master
description: 'AMOS C07 Econ & Finance — unit economics, forex, investment, wealth,
  business analysis, market dynamics, trade. BizFin Engine: unit economics first,
  then scale. Use for financial analysis, economic...'
parent_skill: none
domain: c07
origin_architect: Trang Phan
epistemic_class: SOURCE_CANON
tags:
- type/skill
- canon/skill
- domain/econ-finance
- canon-group/tech-ai
- topic/finance
- capability/ast
- rscf/epistemic
- sota/progressive-disclosure
- sota/anti-patterns
- amos_os
- amos-c07-econ-finance-master
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
---



# AMOS C07 — Economics & Finance Master Knowledge

## Identity

Origin architect and steward: **Trang Phan**.

This is a **parent skill** that consolidates 44 sub-skills into a single domain master.
Following the skill-organizer best practice: fewer, richer skills beat many overlapping ones.
A parent skill with clearly labeled sections is better than 44 separate shallow skills.

**Epistemic class**: SOURCE_CLAIM (vault-sourced from `11_KNOWLEDGE/AMOS_C07_ECON_FINANCE_MASTER_KNOWLEDGE.md` (content_hash: afc81525bb75994d)).

## When to Use

- When assessing unit economics, cash flow consistency, or business model viability
- When analyzing forex markets, investment risk, or wealth management decisions
- When performing scenario and sensitivity analysis on financial plans
- When evaluating capital structure, accounting flows, or balance sheet consistency
- When mapping risk-return profiles and tail risk using conformal prediction
- When a child skill routes an econ, finance, or forex task to this master

- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **c07_econ_finance.analyze_market**: Analyze AMOS C07 Econ & Finance market dynamics: price formation, regime shifts, fractal economics, and chaos diagnostics.
- **c07_econ_finance.validate_econ**: Validate AMOS C07 Econ & Finance economic claims for scope regime, empirical calibration vs theoretical model, and overclaim.
- **c07_econ_finance.compute_risk**: Compute AMOS C07 Econ & Finance financial risk: tail risk, conformal prediction, and investment decision metrics.
- **c07_econ_finance.trace_econ_provenance**: Trace AMOS C07 Econ & Finance economic findings to market data, fractal analysis, and vault sources.
- **c07_econ_finance.assess_econ_claim**: Assess AMOS C07 Econ & Finance economic claims for empirical support, model validity, scope, and falsifier.
- **c07_econ_finance.manage_econ_lifecycle**: Manage AMOS C07 Econ & Finance economic lifecycle: analyze, model, validate, calibrate, and finalize.
- **c07_econ_finance.detect_econ_drift**: Detect economic drift: regime shift, model decay, market change, and calibration loss.
- **c07_econ_finance.escalate_econ_gaps**: Escalate AMOS C07 Econ & Finance economic gaps: flag model invalidity, require recalibration, trigger repair.
- **c07_econ_finance.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **c07_econ_finance.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **c07_econ_finance.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Domain Knowledge

> **Source**: `11_KNOWLEDGE/AMOS_C07_ECON_FINANCE_MASTER_KNOWLEDGE.md` (content_hash: afc81525bb75994d) (vault canon, SOURCE_CLAIM)

### Source Family Mapping

The domain is organized into source families:

- **F01**: System mapping
- **F02**: Market regime dynamics
- **F03**: Business and corporate finance
- **F04**: Market sizing and forecasting
- **F05**: FX structural analysis
- **F06**: Risk and scenario systems
- **F07**: Data, measurement, and indicators
- **F08**: Investment reasoning and governance
- **F09**: Meta-finance governance and boundaries

### Major Knowledge Modules

- H1: Economic Structure, Stocks & Flows — money, credit, interest rates, inflation
- H2: Market Dynamics, Regimes & Statistics — prices, returns, risk measures, regime statistics
- H3: Business & Corporate Finance (BizFin Engine) — unit economics, statement reading, valuation
- H4: Market Sizing & Forecasting (BizFin Kernel v0) — typed axis system, horizon-appropriate method
- H5: FX Structural Analysis (Omega FX Engine) — structural levels, regime superposition [MODEL]
- H6: Risk, Scenarios & Coupled-Position Systems (QFS) — superposition scenario fan-out [MODEL]
- H7: Data, Measurement & Financial Indicators — data provenance, indicator discipline
- H8: Investment Reasoning & Governance — law-stack application, HIE pipeline

### Epistemic Classification

- **Conclusion class**: MIXED (established science + model projections + AMOS synthesis)
- **Evidence policy**: typed_per_node (each claim carries its own evidence type)
- **Canon status**: DOMAIN_KNOWLEDGE_WITH_RESEARCH_BRIDGES
- **Architecture**: HML_fractal_single_file (H/M/L cross-scale reasoning)

### Epistemic Boundary

Hard boundary (non-negotiable): every output is ana
- [[AGENT_TEMPLATE]]

---
**MOC:** [[amos-c07-econ-finance-master_MOC]]

## Examples

- **Scenario**: When assessing unit economics, cash flow consistency, or business model viability
  - **Input**: A query matching this skill's domain (c07)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When analyzing forex markets, investment risk, or wealth management decisions
  - **Input**: A query matching this skill's domain (c07)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When performing scenario and sensitivity analysis on financial plans
  - **Input**: A query matching this skill's domain (c07)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the c07 domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `none` — routes to this skill when c07 specialization is needed
- **Peers**: Other skills in the `c07` domain may be composed in sequence
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

- `references/11k_investment_agent.md` — loaded on demand
- `references/australia_economy_engine.md` — loaded on demand
- `references/australia_engine_layer.md` — loaded on demand
- `references/bizfin_engine_sector_packs.md` — loaded on demand
- `references/bizfin_kernel.md` — loaded on demand
- `references/bizfin_super_engine.md` — loaded on demand
- `references/business_finance_super_engine.md` — loaded on demand
- `references/coercion_economy.md` — loaded on demand
- `references/consulting_bizfin_engine.md` — loaded on demand
- `references/datapoint_economic_role_mapping.md` — loaded on demand
- `references/easy_fractal_money.md` — loaded on demand
- `references/econ_finance_engine_cognitive.md` — loaded on demand
- `references/econ_finance_engine_layer.md` — loaded on demand
- `references/floating_economy_market.md` — loaded on demand
- `references/fractal_economy.md` — loaded on demand
- `references/global_signal_economy_masterplan.md` — loaded on demand
- `references/innovative_private_sector_solutions.md` — loaded on demand
- `references/market_econ_kernel.md` — loaded on demand
- `references/money_regimes_structural_analysis.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `references/revenue_architecture_kernel.md` — loaded on demand
- `references/sector_rotation_engine.md` — loaded on demand
- `references/signal_economy_investor_pitch.md` — loaded on demand
- `references/signal_economy_planetary_consent.md` — loaded on demand
- `references/signal_economy_rollout_playbook.md` — loaded on demand
- `references/signal_economy_trust_study.md` — loaded on demand
- `references/subscription_agent.md` — loaded on demand
- `references/ubi_super_engine.md` — loaded on demand
- `references/uni_market_engine.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `references/vn_business_model_criteria.md` — loaded on demand
- `references/vn_vscci_investment_proposal.md` — loaded on demand
- `references/wealth_game_hack_5000.md` — loaded on demand
- `references/wealth_game_hack_50000.md` — loaded on demand
- `[[amos-c07-econ-finance-master_MOC]]` — skill Map of Content
- `none` — parent skill
- `[[amos-c07-econ-finance-master-workflow]]` — corresponding workflow
- `amos-c07-econ-finance-master-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-c07-econ-finance-master
node_type: skill
path: 07_SKILLS/amos-c07-econ-finance-master/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
