---
schema_version: 1.0
title: SKILL — Mckinsey Framework Navigator
type: skill
source: 07_SKILLS/mckinsey-framework-navigator
name: mckinsey-framework-navigator
description: Framework Navigator — McKinsey strategic capability. Use when strategic
  analysis, business consulting, or McKinsey-framework reasoning. Use when amos-c08-strategy-game-master
  routes to this specialized capability. Do not use for generic tasks outside mckinsey
  domain.
parent_skill: amos-c08-strategy-game-master
domain: mckinsey
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- type/skill
- domain/strategy-game
- epistemic/source_claim
- hml/m
- epistemic/source_claim
- amos-os
- law-hierarchy
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
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L4
- L5
- L16
- L17
license: MIT
steward: Trang Phan
---

# Mckinsey: framework Navigator

## Identity

Origin architect: **Trang Phan**. Domain: mckinsey. Parent: amos-c08-strategy-game-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.
## When to Use

- When mckinsey strategy framework for mckinsey: framework navigator is needed within the mckinsey domain
- When the parent skill (`amos-c08-strategy-game-master`) routes to this specialized capability
- When a query requires mckinsey-specific reasoning grounded in vault sources
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **framework_navigator.assess_commercial**: Assess commercial due diligence: market, competitive position, and growth
- **framework_navigator.evaluate_credit**: Evaluate credit and lending: risk scoring, portfolio, and concentration
- **framework_navigator.analyze_banking**: Analyze banking CRM: customer lifetime value, retention, and cross-sell
- **framework_navigator.transfer_architecture**: Transfer architecture references: best practices across organizational contexts

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: f7a6a345557a1f97) for the full vault-sourced domain knowledge (9619 chars).
- **framework_navigator.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **framework_navigator.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **framework_navigator.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Operations

1. **framework_navigator.assess_commercial**: Assess commercial due diligence: market, competitive position, and growth
2. **framework_navigator.evaluate_credit**: Evaluate credit and lending: risk scoring, portfolio, and concentration
3. **framework_navigator.analyze_banking**: Analyze banking CRM: customer lifetime value, retention, and cross-sell
4. **framework_navigator.transfer_architecture**: Transfer architecture references: best practices across organizational contexts
5. **framework_navigator.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
6. **framework_navigator.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
7. **framework_navigator.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_C08_STRATEGY_GAME_MASTER_KNOWLEDGE.md` (content_hash: 4b676ad6f9ca020f) (vault canon, SOURCE_CLAIM)

### McKinsey Framework Navigation

From C08 Strategy & Game: Consulting discipline and McKinsey frameworks.

**McKinsey frameworks**:
- **MECE decomposition**: Mutually Exclusive, Collectively Exhaustive problem decomposition
- **Hypothesis-first investigation**: form hypothesis, then test with data
- **Issue trees**: break problems into sub-issues systematically
- **Pyramid principle**: top-down communication, conclusion first
- **SWOT analysis**: Strengths, Weaknesses, Opportunities, Threats
- **Porter's five forces**: competitive analysis framework
- **BCG matrix**: growth-share matrix for portfolio analysis

**Framework navigation law**: `FRAMEWORK != ANSWER`. A framework structures thinking; it does not produce answers. The answer comes from applying the framework to evidence.

### Epistemic Boundary

McKinsey framework navigation is an analytical toolset. It does not prove frameworks are universally applicable, that structured thinking always produces correct answers, or that consulting frameworks are optimal.

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

- **Skill**: `mckinsey-framework-navigator`
- **Parent**: `amos-c08-strategy-game-master`
- **Domain**: mckinsey
- **Origin architect**: Trang Phan
- **Vault sources**:
- `misc/E/Enhanced Master Relationship Pack - Legal & Commercial Framework.md` — Enh

---
**Links:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Related

- [[07_SKILLS/mckinsey-framework-navigator/mckinsey-framework-navigator_MOC|mckinsey-framework-navigator_MOC]]

## Examples

- **Scenario**: When mckinsey strategy framework for mckinsey: framework navigator is needed within the mckinsey domain
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


## Do not use

- For generic business analysis outside the McKinsey framework
- To claim empirical validation of consulting methodologies
- As a substitute for domain-specific industry or market evidence
- Outside McKinsey/strategy domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `` — skill Map of Content
- `amos-c08-strategy-game-master` — parent skill
- `` — corresponding workflow
- `mckinsey-framework-navigator-agent` — corresponding agent
---

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: mckinsey-framework-navigator
node_type: skill
path: 07_SKILLS/mckinsey-framework-navigator/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
