---
title: "SKILL — Amos Heritage Decision Intelligence"
type: skill
source: 07_SKILLS/amos-heritage-decision-intelligence
name: amos-heritage-decision-intelligence
description: Heritage Decision Intelligence — society and culture capability. Use when social analysis, cultural reasoning, or anthropological study. Use when amos-c06-society-culture-master routes to this specialized capability.
parent_skill: amos-c06-society-culture-master
domain: c06
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-heritage-decision-intelligence, canon/skill]
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: "1.1.0"
---


# Heritage Decision Intelligence

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c06-society-culture-master`
- **Domain**: c06
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Society-culture engine for Heritage Decision Intelligence

## When to Use

- When analyzing emergent social intelligence: norms, networks, culture
- When modeling heritage decision intelligence: tradition and adaptation
- When assessing long-term civilizational patterns and cyclical dynamics
- When evaluating historical pattern claims for statistical validity
- When the parent skill (`amos-c06-society-culture-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **heritage_decision.analyze_social**: Analyze emergent social intelligence: norms, networks, and cultural dynamics
- **heritage_decision.model_heritage**: Model heritage decision intelligence: tradition, continuity, and adaptation
- **heritage_decision.assess_language**: Assess language as equation: semantic structure, pragmatic force, and drift
- **heritage_decision.evaluate_pattern**: Evaluate heritage pattern claims: statistical validity, sample size, p-value
- **heritage_decision.detect_drift**: Detect drift in heritage patterns, cultural cycles, or evidence freshness
- **heritage_decision.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **heritage_decision.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Domain Knowledge

> **Source**: `_00_Cosmo brain/misc/H/HERITAGE INTELLIGENCE™.md` (content_hash: 290290a4d8df047c) (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/misc/H/HERITAGE_THE_PATTERNS_WE_FOUND.md` (content_hash: 55180e7dc81c0f9a) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C08_STRATEGY_GAME_MASTER_KNOWLEDGE.md` (content_hash: 4b676ad6f9ca020f) (vault canon, SOURCE_CLAIM)

### Heritage Decision Intelligence

From Cosmo Brain Heritage Intelligence: 32 layers + 10 signal classes for multi-layer decision intelligence. Covers thermodynamic constraints, information-theoretic limits, biological integrity, and decision governance from cosmic entropy to micro-market behavior.

**6 Foundational propositions**:
1. **Life**: life as the fundamental organizing principle
2. **Information Security**: information integrity as the basis of decision-making
3. **Brain**: cognitive architecture for decision intelligence
4. **Externalization**: externalizing decision intelligence into systems
5. **Integrity**: maintaining integrity through transformations
6. **Purpose**: purpose-driven decision-making

**32-layer architecture**: Multi-layer decision intelligence from cosmic entropy to micro-market behavior, covering thermodynamic constraints, information-theoretic limits, biological integrity, and decision governance across scales (H/M/L).

**10 Signal classes**: Different types of signals that inform decision-making, from weak signals to strong signals, from immediate to delayed, from direct to indirect.

### Heritage Patterns (9 discovered)

The Heritage framework identifies 9 cyclical patterns in human history:

| Pattern | Cycle | Description |
|---------|-------|-------------|
| H1 | 17 years | Cicada cycle in human conflict (1618-2026, p < 0.01) |
| H2 | 144 years | Technological revolutions (Gutenberg 1440 → Transformer AI 2016) |
| H3 | 37 years | Financial crises (South Sea Bubble 1720 onward) |
| H4 | 83 years | Empire collapse cycle |
| H5 | 1,360 years | Civilizational complexity (solar correlation) |
| H6 | 120 years | Language death/revival cycle |
| H7 | Golden ratio | Dynastic lengths |
| H8 | Prime numbers | Innovation cycles |
| H9 | Variable | "Shadow civilization" signal in radiocarbon data |

### Epistemic Boundary

Heritage patterns are SOURCE_CLAIM. Statistical significance claims (e.g., p < 0.01) require independent verification. Historical cycle detection is AMOS_MODEL — patterns in historical data do not constitute prediction or deterministic law. Do not present heritage patterns as established historical laws or forecasts.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-heritage-decision-intelligence_MOC]]

## Examples

- **Scenario**: When analyzing emergent social intelligence: norms, networks, culture
  - **Input**: A query matching this skill's domain (c06)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When modeling heritage decision intelligence: tradition and adaptation
  - **Input**: A query matching this skill's domain (c06)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When assessing long-term civilizational patterns and cyclical dynamics
  - **Input**: A query matching this skill's domain (c06)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the c06 domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-c06-society-culture-master` — routes to this skill when c06 specialization is needed
- **Peers**: Other skills in the `c06` domain may be composed in sequence
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
- `[[amos-heritage-decision-intelligence_MOC]]` — skill Map of Content
- `amos-c06-society-culture-master` — parent skill
- `[[amos-heritage-decision-intelligence-workflow]]` — corresponding workflow
- `amos-heritage-decision-intelligence-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-heritage-decision-intelligence
node_type: skill
path: 07_SKILLS/amos-heritage-decision-intelligence/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
