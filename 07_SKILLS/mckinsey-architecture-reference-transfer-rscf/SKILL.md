---
title: SKILL — Mckinsey Architecture Reference Transfer Rscf
type: skill
source: 07_SKILLS/mckinsey-architecture-reference-transfer-rscf
name: mckinsey-architecture-reference-transfer-rscf
description: Architecture Reference Transfer — McKinsey strategic capability. Use when strategic analysis,
  business consulting, or McKinsey-framework reasoning. Use when amos-c08-strategy-game-master routes
  to this specialized capability.
parent_skill: amos-c08-strategy-game-master
domain: mckinsey
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/strategy-game
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
---








# Mckinsey: architecture Reference Transfer Rscf

## Identity

Origin architect: **Trang Phan**. Domain: mckinsey. Parent: amos-c08-strategy-game-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.
## When to Use

- When mckinsey strategy framework for mckinsey: architecture reference transfer rscf is needed within the mckinsey domain
- When the parent skill (`amos-c08-strategy-game-master`) routes to this specialized capability
- When a query requires mckinsey-specific reasoning grounded in vault sources
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **architecture_reference.assess_commercial**: Assess commercial due diligence: market, competitive position, and growth
- **architecture_reference.evaluate_credit**: Evaluate credit and lending: risk scoring, portfolio, and concentration
- **architecture_reference.analyze_banking**: Analyze banking CRM: customer lifetime value, retention, and cross-sell
- **architecture_reference.transfer_architecture**: Transfer architecture references: best practices across organizational contexts
- **architecture_reference.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **architecture_reference.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **architecture_reference.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_C08_STRATEGY_GAME_MASTER_KNOWLEDGE.md` (content_hash: 4b676ad6f9ca020f) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C09_ORG_LAW_POLICY_MASTER_KNOWLEDGE.md` (content_hash: bead46b07fc02558) (vault canon, SOURCE_CLAIM)

### McKinsey Architecture Reference Transfer

From C08 Strategy & Game: Consulting frameworks and strategic architecture. From C09 Org & Law: Organizational architecture and governance.

**Reference transfer model**:
- **Architecture reference**: a documented architecture pattern from one domain
- **Transfer**: applying the architecture pattern to a new domain
- **Adaptation**: adapting the pattern to fit the new domain's constraints
- **Validation**: validating that the transferred architecture works in the new domain

**Transfer protocol**:
1. **Identify reference**: identify the source architecture pattern
2. **Analyze constraints**: analyze the target domain's constraints
3. **Map**: map the reference architecture to the target domain
4. **Adapt**: adapt the architecture to fit target constraints
5. **Validate**: validate the adapted architecture
6. **Document**: document the transfer with provenance

**Transfer laws**:
- `REFERENCE != SOLUTION`: a reference architecture is not a solution; it must be adapted
- `PATTERN != GUARANTEE`: a pattern that works in one domain does not guarantee success in another
- `TRANSFER != COPY`: transfer is adaptation, not copying

### Epistemic Boundary

Architecture reference transfer is an analytical methodology. It does not prove the transferred architecture is optimal, that all patterns transfer, or that adaptation is always successful.

## Instant Start

> **Reference**: See `references/mckinsey-architecture-reference-transfer-rscf_code.md` (content_hash: 39b5c8a5b4df8e2c) for the code implementation.

## Core Components

| Component | Import Path | Purpose |
|-----------|-------------|---------|
| `HierarchicalGenerator` | `.core` | Rule-based 7-level hierarchy |
| `GoalDrivenGenerator` | `.goal_core` | Natural language goal parsing |
| `UnifiedGenerator` | `.unified_generator` | Combines both approaches |
| `PatternLibrary` | `.patterns` | Code templates for 5 pattern types |
| `AMOSArchitectureBridge` | `.integration` | AMOS ecosystem integration |

## CLI Commands

```bash
# Main CLI
python -m hierarchical_ai_architecture_generator generate --limit 1000
python -m hierarchical_ai_architecture_generator query --layer safety_controller
python -m hierarchical_ai_architecture_generator demo

# Goal-driven CLI
python goal_driven_ai_architecture_generator_v2.py generate \
    --goal "Create retrieval system" --count 50
python goal_driven_ai_architecture_ge

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[mckinsey-architecture-reference-transfer-rscf_MOC]]
```

## Examples

- **Scenario**: When mckinsey strategy framework for mckinsey: architecture reference transfer rscf is needed within the mckinsey domain
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

- `references/mckinsey-architecture-reference-transfer-rscf_code.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `[[mckinsey-architecture-reference-transfer-rscf_MOC]]` — skill Map of Content
- `amos-c08-strategy-game-master` — parent skill
- `[[mckinsey-architecture-reference-transfer-rscf-workflow]]` — corresponding workflow
- `mckinsey-architecture-reference-transfer-rscf-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: mckinsey-architecture-reference-transfer-rscf
node_type: skill
path: 07_SKILLS/mckinsey-architecture-reference-transfer-rscf/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
