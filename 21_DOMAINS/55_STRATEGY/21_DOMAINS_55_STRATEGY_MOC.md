---
title: 04 Strategy MOC — 04 Strategy — 21 Domains / 04 Strategy
type: moc
source: 21_DOMAINS/55_STRATEGY
tags:
- 04-strategy
- canon/domain
- directed-systemal-intelligence-domain
- seven-cycles-domain-model
- strategy-domains-domain-spec
- strategy-domains-interfaces
- strategy-domains-provenance
- tpe-domain-model
- tss-domain-model
moc: true
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
aliases:
- 55_STRATEGY_MOC
- 04 Strategy MOC
---

# 04 Strategy — Map of Content

**Path:** `21_DOMAINS/55_STRATEGY`
**Files:** 9 | **Subdirectories:** 1

## Purpose

This MOC indexes the Strategy domain — the governed specification of how
AMOS directs systemal intelligence, selects among competing courses of
action, and coordinates the seven-cycle governance rhythm. The strategy
domain bridges cognitive capability (what the system can reason about)
with governance and economic systems (how decisions become authoritative
and consequential). It defines domain models, interfaces, provenance, and
the contract binding strategy artifacts to the rest of the vault.

## MECE Domain

**E — Strategy, Governance & Economic Systems.**

In the MECE architecture the strategy domain occupies the
**governance/economic** slice of the domains layer. It is distinct from
cognitive capability domains (which define what can be reasoned) and from
infrastructure domains (which define how artifacts are stored and routed).
Strategy artifacts specify directed systemal intelligence, the Seven
Cycles domain model, TSS (governance), and TPE (economic outcome
prediction), ensuring that strategic reasoning has explicit models,
interfaces, and provenance rather than implicit assumptions.

## Files

- [[21_DOMAINS/55_STRATEGY/DIRECTED_SYSTEMAL_INTELLIGENCE_DOMAIN|DIRECTED_SYSTEMAL_INTELLIGENCE_DOMAIN]] — domain model for directed systemal intelligence
- [[21_DOMAINS/55_STRATEGY/DOMAINS_STRATEGY_CONTRACT|DOMAINS_STRATEGY_CONTRACT]] — contract binding strategy domain artifacts
- [[21_DOMAINS/55_STRATEGY/SEVEN_CYCLES_DOMAIN_MODEL|SEVEN_CYCLES_DOMAIN_MODEL]] — seven-cycle governance rhythm domain model
- [[21_DOMAINS/55_STRATEGY/STRATEGY_DOMAINS_DOMAIN_SPEC|STRATEGY_DOMAINS_DOMAIN_SPEC]] — specification of the strategy domain scope
- [[21_DOMAINS/55_STRATEGY/STRATEGY_DOMAINS_INTERFACES|STRATEGY_DOMAINS_INTERFACES]] — interfaces between strategy and other domains
- [[21_DOMAINS/55_STRATEGY/STRATEGY_DOMAINS_PROVENANCE|STRATEGY_DOMAINS_PROVENANCE]] — provenance chain for strategy domain artifacts
- [[21_DOMAINS/55_STRATEGY/STRATEGY_DOMAINS_README|STRATEGY_DOMAINS_README]] — README for the strategy domains subdomain
- [[21_DOMAINS/55_STRATEGY/TPE_DOMAIN_MODEL|TPE_DOMAIN_MODEL]] — TPE (economic outcome prediction) domain model
- [[21_DOMAINS/55_STRATEGY/TSS_DOMAIN_MODEL|TSS_DOMAIN_MODEL]] — TSS (governance) domain model

## Subdirectories

- [[01_CANON/00_INDEX/00_INDEX_MOC|00_INDEX_MOC]] — 00_INDEX

## Relationships

- **Parent domains:** [[21_DOMAINS/21_DOMAINS_MOC|21_DOMAINS_MOC]]
- **Strategy contract:** [[21_DOMAINS/55_STRATEGY/DOMAINS_STRATEGY_CONTRACT|DOMAINS_STRATEGY_CONTRACT]]
- **Seven Cycles model:** [[21_DOMAINS/55_STRATEGY/SEVEN_CYCLES_DOMAIN_MODEL|SEVEN_CYCLES_DOMAIN_MODEL]]
- **TSS governance:** [[21_DOMAINS/55_STRATEGY/TSS_DOMAIN_MODEL|TSS_DOMAIN_MODEL]]
- **TPE economics:** [[21_DOMAINS/55_STRATEGY/TPE_DOMAIN_MODEL|TPE_DOMAIN_MODEL]]
- **Root navigation:** [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]

## Epistemic Boundary

Strategy domain artifacts are **DERIVED** models from the AMOS corpus.
A domain model specifies how strategic reasoning is structured; it does
not prove that the model has been deployed or that governance cycles
have been executed. `MODEL != DEPLOYED_RUNTIME`. TSS/TPE predictions
remain hypotheses until discriminating evidence is produced.

______________________________________________________________________


## Domain Scope

The Strategy domain covers strategic planning, competitive analysis, game theory, and decision-making:

### Sub-domains
- **Strategic planning**: mission, vision, values; SWOT, PESTEL, Porter's 5 Forces; balanced scorecard
- **Competitive strategy**: cost leadership, differentiation, focus (Porter); blue ocean strategy
- **Game theory**: Nash equilibrium, dominant strategies, repeated games, evolutionary game theory
- **Decision analysis**: decision trees, expected value, real options, Monte Carlo, multi-criteria decision analysis

### SOTA Methods
- **Strategy frameworks**: OKR (objectives and key results), Hoshin Kanri, OGSM; V2MOM (Salesforce)
- **Competitive analysis**: Porter's 5 Forces, VRIO (Barney), resource-based view (RBV), dynamic capabilities (Teece)
- **Game theory**: mechanism design, auction theory, signaling, screening; algorithmic game theory
- **Decision science**: prospect theory (Kahneman-Tversky), nudge theory, behavioral economics; Bounded rationality

### AMOS Integration
- **C08 domain**: [[21_DOMAINS/18_C08_STRATEGY_GAME/18_C08_STRATEGY_GAME_MOC|C08 strategy-game domain]]
- **Strategy MOC**: [[00_ROOT/55_STRATEGY_MOC|55_STRATEGY_MOC]]
- **Investment engine**: [[11_KNOWLEDGE/engine/INVESTMENT_ENGINE|Investment Engine]]
- **Sector rotation engine**: [[11_KNOWLEDGE/engine/SECTOR_ROTATION_ENGINE|Sector Rotation Engine]]

### Invariants
1. `STRATEGY != EXECUTION` — strategy formulation is necessary but not sufficient
2. `MODEL != REALITY` — strategic models are approximations of complex markets
3. All strategic claims must cite provenance (framework, data, assumptions)
4. `PLAN != OUTCOME` — plans do not guarantee outcomes


**Parent:** [[21_DOMAINS/21_DOMAINS_MOC|21_DOMAINS_MOC]]
