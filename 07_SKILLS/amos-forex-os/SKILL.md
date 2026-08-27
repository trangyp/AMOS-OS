---
title: SKILL
type: skill
source: 07_SKILLS/amos-forex-os
name: amos-forex-os
description: Forex Os — forex and finance capability. Use when forex analysis, currency trading, or market dynamics. Use when amos-c07-econ-finance-master routes to this specialized capability.
parent_skill: amos-c07-econ-finance-master
domain: fx
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-forex-os, canon/skill]
rscf:
  state: DERIVED
  claim_class: EMPIRICAL
  provenance: AMOS_corpus
  scope: AMOS_general
version: "1.1.0"
---


# Forex Os

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c07-econ-finance-master`
- **Domain**: fx
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

FX market analysis engine for Forex Os

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

- **forex.calibrate_model**: Calibrate FX models: Bayesian neural SDEs, volatility surfaces, and term structures
- **forex.assess_risk**: Assess FX risk: currency exposure, correlation breakdown, and tail events
- **forex.backtest_strategy**: Backtest FX strategies: walk-forward, regime-aware, and stress-tested
- **forex.monitor_regime**: Monitor FX regime shifts: volatility, correlation, and liquidity transitions
- **forex.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **forex.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **forex.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: e0b215017a070122) for the full vault-sourced domain knowledge (7541 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/amos-general/A/Infrastructure/AMOS_Infrastructure_Deep_Report_v23.md` (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/misc/H/HERITAGE_THE_PATTERNS_WE_FOUND.md` (content_hash: 55180e7dc81c0f9a) (vault canon, SOURCE_CLAIM)

### Forex OS

From Cosmo Brain Infrastructure Deep Report: Forex belongs beneath a larger infrastructure that already owns global structure, integrity limits, capability limits, cross-domain routing, and interface/expression behavior. From Heritage Patterns: Full Forex System Stress test.

**Architectural positioning**: Forex OS is NOT the AMOS root. Forex belongs beneath a larger infrastructure that owns:
- Global structure
- Integrity limits
- Capability limits
- Cross-domain routing
- Interface/expression behavior

**Full Forex System Stress test** (TEST 10, 10,000 simulations):
- Trade 28 pairs simultaneously
- All 7 regimes active
- All 14 central banks active
- 10 economic data releases per day
- Liquidity ranging from normal to vacuum
- Leverage 10:1
- 1ms latency
- 5% data loss
- 25% adversarial spoofing
- 50% novelty events

**Forex OS laws**:
- `FOREX_OS != AMOS_ROOT`: Forex OS is a subsystem; it is not the root OS
- `FOREX != MARKET**: Forex is the foreign exchange system; it is not the entire market
- `STRESS_TEST != PRODUCTION**: stress test validates under extreme conditions; production has different requirements

### Epistemic Boundary

Forex OS is a domain-specific subsystem. It does not prove Forex is the most important market, that the stress test covers all scenarios, or that Forex OS can operate independently.

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
- **G6 (Failure mode)**: On validation f

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-forex-os_MOC]]

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

- **Parent**: `[[amos-c07-econ-finance-master]]` — routes to this skill when fx specialization is needed
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
- `[[amos-forex-os_MOC]]` — skill Map of Content
- `[[amos-c07-econ-finance-master]]` — parent skill
- `[[amos-forex-os-workflow]]` — corresponding workflow
- `[[amos-forex-os-agent]]` — corresponding agent

