---
title: SKILL — Mckinsey Wealth Management Rscf
type: skill
source: 07_SKILLS/mckinsey-wealth-management-rscf
name: mckinsey-wealth-management-rscf
description: Wealth Management — McKinsey strategic capability. Use when strategic
  analysis, business consulting, or McKinsey-framework reasoning. Use when amos-c08-strategy-game-master
  routes to this specialized capability.
parent_skill: amos-c08-strategy-game-master
domain: mckinsey
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/strategy-game
- canon-group/human-system
- topic/strategy
- capability/mckinsey-strategy
- topic/consulting
- rscf/epistemic
- rscf/T-topology
- rscf/G-relation
- rscf/S-state
- rscf/C-constraint
- rscf/type-model
- sota/progressive-disclosure
- sota/anti-patterns
- amos_os
- mckinsey-wealth-management-rscf
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
---




# Mckinsey: wealth Management Rscf

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c08-strategy-game-master`
- **Domain**: mckinsey
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

McKinsey strategy framework for Mckinsey: wealth Management Rscf

## When to Use

- When mckinsey strategy framework for mckinsey: wealth management rscf is needed within the mckinsey domain
- When the parent skill (`amos-c08-strategy-game-master`) routes to this specialized capability
- When a query requires mckinsey-specific reasoning grounded in vault sources
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **wealth_management.assess_commercial**: Assess commercial due diligence: market, competitive position, and growth
- **wealth_management.evaluate_credit**: Evaluate credit and lending: risk scoring, portfolio, and concentration
- **wealth_management.analyze_banking**: Analyze banking CRM: customer lifetime value, retention, and cross-sell
- **wealth_management.transfer_architecture**: Transfer architecture references: best practices across organizational contexts
- **wealth_management.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **wealth_management.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **wealth_management.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_C07_ECON_FINANCE_MASTER_KNOWLEDGE.md` (content_hash: afc81525bb75994d) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C08_STRATEGY_GAME_MASTER_KNOWLEDGE.md` (content_hash: 4b676ad6f9ca020f) (vault canon, SOURCE_CLAIM)

### Wealth Management

From C07 Econ & Finance: Investment management and portfolio theory. From C08 Strategy & Game: Strategic portfolio management.

**Wealth management model**:
- **Asset allocation**: strategic allocation across asset classes (equity, fixed income, alternatives)
- **Risk management**: risk budgeting, VaR, stress testing
- **Portfolio optimization**: mean-variance optimization, factor models
- **Wealth preservation**: capital preservation, downside protection, generational transfer

**Wealth management laws**:
- `RETURN != ALPHA`: returns may be from beta (market) not alpha (skill)
- `PAST != FUTURE`: past performance does not guarantee future results
- `DIVERSIFICATION != GUARANTEE`: diversification reduces risk but does not eliminate it

**RSCF integration**:
- Wealth management claims are MODEL (conditional on assumptions)
- Confidence ceiling: return predictions <= evidence support
- Falsifier: underperformance vs benchmark over declared period
- Scope: claims valid only within declared market regime

**McKinsey framework integration**:
- Portfolio analysis using BCG matrix (stars, cash cows, question marks, dogs)
- Strategic allocation using GE-McKinsey matrix (attractiveness vs strength)
- Risk-adjusted returns using Sharpe, Sortino, Calmar ratios

### Epistemic Boundary

Wealth management is an analytical framework. It does not prove positive returns, that models predict markets, or that risk management eliminates all risk.

## Summary

Implemented `UnknownUnknownRegistry` class in `AMOS_GapRegistry.py` to track
areas where we don't know what we don't know. This closes GAP-MGMT-002 and
upgrades GAP-OMNIVERSE-003 to COVERED. The GAP_MANAGEMENT component is now
fully COVERED.

## What Was Implemented

### `UnknownUnknownEntry` dataclass
- `entry_id`: unique identifier (e.g., "UU-001")
- `surface_area`: what domain/area was surveyed
- `survey_method`: how we looked for unknowns (architectural_review, fuzzing, etc.)
- `estimated_count`: how many unknown-unknowns we think exist
- `confidence`: 0.0-1.0 confidence in the estimate
- `surveyed`: has this area been surveyed at all?
- `last_surveyed`: ISO timestamp of last survey
- `notes`: additional context

### `UnknownUnknownRegistry` class
- **5 pre-populated surface areas**:
  - UU-001: BRAIN_CORE_ubi_integration (surveyed, est=5, conf=0.3)
  - UU-002: OMNI_KERNEL_runtime_integration (surveyed, est=3, conf=0.4)
  - UU-003: OMNIVERSE_BRAIN_world_model (surveyed, est=8, conf=0.2)
  - UU-004: EXPRESSION_TRANSLATION_edge_cases (unsurveyed)
  - UU

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[mckinsey-wealth-management-rscf_MOC]]

## Examples

- **Scenario**: When mckinsey strategy framework for mckinsey: wealth management rscf is needed within the mckinsey domain
  - **Input**: A query matching this skill's domain (mckinsey)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When the parent skill (`amos-c08-strategy-game-master`) routes to this specialized capability
  - **Input**: A query matching this skill's domain (mckinsey)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When a query requires mckinsey-specific reasoning grounded in vault sources
  - **Input**: A query matching this skill's domain (mckinsey)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the mckinsey domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-c08-strategy-game-master` — routes to this skill when mckinsey specialization is needed
- **Peers**: Other skills in the `mckinsey` domain may be composed in sequence
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

- `references/money_regimes_for_wealth.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `[[mckinsey-wealth-management-rscf_MOC]]` — skill Map of Content
- `amos-c08-strategy-game-master` — parent skill
- `[[mckinsey-wealth-management-rscf-workflow]]` — corresponding workflow
- `mckinsey-wealth-management-rscf-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: mckinsey-wealth-management-rscf
node_type: skill
path: 07_SKILLS/mckinsey-wealth-management-rscf/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
