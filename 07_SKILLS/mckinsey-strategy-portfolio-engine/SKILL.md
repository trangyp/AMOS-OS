---
title: SKILL — Mckinsey Strategy Portfolio Engine
type: skill
source: 07_SKILLS/mckinsey-strategy-portfolio-engine
name: mckinsey-strategy-portfolio-engine
description: Strategy Portfolio Engine — McKinsey strategic capability. Use when strategic
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
- mckinsey-strategy-portfolio-engine
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
---




# Mckinsey: strategy Portfolio Engine

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c08-strategy-game-master`
- **Domain**: mckinsey
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

McKinsey strategy framework for Mckinsey: strategy Portfolio Engine

## When to Use

- When mckinsey strategy framework for mckinsey: strategy portfolio engine is needed within the mckinsey domain
- When the parent skill (`amos-c08-strategy-game-master`) routes to this specialized capability
- When a query requires mckinsey-specific reasoning grounded in vault sources
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **strategy_portfolio.assess_commercial**: Assess commercial due diligence: market, competitive position, and growth
- **strategy_portfolio.evaluate_credit**: Evaluate credit and lending: risk scoring, portfolio, and concentration
- **strategy_portfolio.analyze_banking**: Analyze banking CRM: customer lifetime value, retention, and cross-sell
- **strategy_portfolio.transfer_architecture**: Transfer architecture references: best practices across organizational contexts
- **strategy_portfolio.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **strategy_portfolio.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **strategy_portfolio.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 88797eb19264cf47) for the full vault-sourced domain knowledge (4415 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_C08_STRATEGY_GAME_MASTER_KNOWLEDGE.md` (content_hash: 4b676ad6f9ca020f) (vault canon, SOURCE_CLAIM)

### McKinsey Strategy Portfolio Engine

From C08 Strategy & Game: Strategic portfolio management.

**Portfolio strategy model**:
- **BCG matrix**: stars, cash cows, question marks, dogs
- **GE-McKinsey matrix**: industry attractiveness vs competitive strength
- **Portfolio balance**: balance growth and cash flow across portfolio
- **Resource allocation**: allocate resources based on strategic priority

**Strategy laws**:
- `STRATEGY != PLAN`: a strategy is a direction; a plan is a sequence of actions
- `PORTFOLIO != COLLECTION`: a portfolio is a balanced set; a collection is an unstructured group
- `ALLOCATION != DISTRIBUTION`: allocation is strategic; distribution is mechanical

### Epistemic Boundary

The strategy portfolio engine is an analytical toolset. It does not prove optimal allocation, that portfolio balance is always achievable, or that strategic frameworks predict outcomes.

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

## Provenance

- **Skill**: `mckinsey-strategy-portfolio-engine`
- **Parent**: `amos-c08-strategy-game-master`
- **Domain**: mckinsey
- **Origin architect**: Trang Phan
- **Vault sources**:
- `architecture/DSc ScD Portfolio - Three Canon Architecture.md` — DSc/ScD Portfolio — Trang Phan (Independent Submission) (6148 chars, score: 10, content_hash: ad04085e8f89fc0a)
- `s

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[mckinsey-strategy-portfolio-engine_MOC]]

## Examples

- **Scenario**: When mckinsey strategy framework for mckinsey: strategy portfolio engine is needed within the mckinsey domain
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

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `[[mckinsey-strategy-portfolio-engine_MOC]]` — skill Map of Content
- `amos-c08-strategy-game-master` — parent skill
- `[[mckinsey-strategy-portfolio-engine-workflow]]` — corresponding workflow
- `mckinsey-strategy-portfolio-engine-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: mckinsey-strategy-portfolio-engine
node_type: skill
path: 07_SKILLS/mckinsey-strategy-portfolio-engine/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
