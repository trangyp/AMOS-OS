---
schema_version: 1.0
name: amos-flow-canon
title: SKILL — Amos Flow Canon
type: note
source: 07_SKILLS/amos-flow-canon
tags:
  - type/skill
  - type/skill
  - domain/canon-universe
  - epistemic/source_claim
  - hml/m
  - epistemic/source_claim
  - amos-os
  - references
  - readme
  - law-hierarchy
  - trang-framework-recursive-ontology-dynamics
  - skill
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
rscf_state: SOURCE_CLAIM
hml_level: M
gmef_gates:
  - L0_integrity
  - L1_epistemic
  - L2_provenance
  - L5_scope
  - L7_authority
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
  - L0
  - L1
  - L2
  - L4
  - L5
  - L7
  - L16
  - L17
  - L18
parent_skill: amos-canon-universe-master
domain: canon
description: AMOS Flow Canon — Part II (Flow) of the 7-Part Universe Canon. Constrained throughput, conversion under limits, bottleneck/leakage/queue dynamics. Use when analyzing how power/energy/capital/information moves through a system, when throughput needs structural characterization, or when identifying bottlenecks or leakage. Do not use for generic tasks outside canon/universe domain.
license: MIT
steward: Trang Phan
---

# AMOS Flow Canon

## Identity

Origin architect: **Trang Phan**. Domain: canon. Parent: amos-canon-universe-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.

## When to Use

- When analyzing how power moves through any system
- When a system's throughput, conversion, or transmission needs structural characterization
- When identifying bottlenecks, leakage, or queue dynamics in a claimed system
- When flow is asserted but not structurally characterized (the vault's genuine gap)

## Capabilities

- **canon_audit**: Audit structural completeness across the 7-Part Universe Canon
- **canon_validate**: Validate system against canon invariants
- **canon_map**: Map system elements to canon parts

## Operations

1. **canon_audit**: Audit structural completeness across the 7-Part Universe Canon
1. **canon_validate**: Validate system against canon invariants
1. **canon_map**: Map system elements to canon parts

## Source

Vault-generated from 7-Part Canon audit (2026-08-23) — identified Flow (Part II) as the only part absent from all 5 existing vault canon layers

## 7-Part Mapping

| Part              | Owned By                   | Gap Status                                    |
| ----------------- | -------------------------- | --------------------------------------------- |
| I — Constraint    | amos-flow-canon            | ✅ Filled                                     |
| II — Flow         | amos-flow-canon            | ✅ Filled                                     |
| III — Structure   | amos-flow-canon            | ✅ Filled (flow→structure dependency)         |
| IV — Enforcement  | amos-law-stack-enforcement | ✅ Filled (flows need enforcement to persist) |
| V — Time          | —                          | ⚪ Empty                                      |
| VI — Adaptation   | —                          | ⚪ Empty                                      |
| VII — Termination | —                          | ⚪ Empty                                      |

## Part Details

### Part II — Flow

- **Definition:** Constrained throughput across a system. Flow is not possession. Flow is conversion under limits.
- **Properties:** Input → transformation → output · Bottlenecks · Leakage · Queues
- **Properties:** Power exists only while it is moving. Flow without structure dissipates. Structure without flow decays.
- **Examples:** Energy through matter, blood through organs, supplies through armies, capital through economies
- **GENUINE GAP ORIGIN:** The vault has no first-class canon for Flow. This is the single most valuable addition the 7-Part Canon makes. All 5 existing vault canon layers (UTC, CIL, Codex, 7 Cycles, Trang ∅) have no first-class Flow characterization.

## Epistemic Boundary

This skill directly addresses the **genuine gap** identified in the 7-Part Canon re-audit: Flow (Part II) is the only part that is precisely characterized as a gap in ALL 5 existing vault canon layers. Adding this skill closes the gap — Flow becomes the first part with complete coverage across all canon layers.

## Law Stack Bridge

Flow (Part II) maps to the Law Stack's Rule of 2™ as the named binary attractor — dual-frame test with rejection rationale. Rubber-stamp fails. Flow persistence depends on enforcement mechanisms (Part IV) maintaining the dual-frame test passing.

## Do not use

- For generic tasks outside the declared AMOS domain
- As a substitute for domain-specific analysis
- For empirical claims without evidence
- Outside the AMOS canon law hierarchy

## References

- references — session-specific detail and authoritative sources
- references/README — references subdirectory readme

______________________________________________________________________

**MOC:** [[07_SKILLS/amos-flow-canon/amos-flow-canon_MOC|amos-flow-canon_MOC]]

## Examples

- **Scenario**: When analyzing how power moves through any system

  - **Input**: A query matching this skill's domain ()
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When a system's throughput, conversion, or transmission needs structural characterization

  - **Input**: A query matching this skill's domain ()
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When identifying bottlenecks, leakage, or queue dynamics in a claimed system

  - **Input**: A query matching this skill's domain ()
  - **Output**: Structured result with epistemic labels and provenance

## Validation Gates

- **L0 Integrity**: All 7 parts accounted for; no part silently dropped
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope; no scope creep
- **L7 Authority**: No autonomous action beyond authority boundary

## Anti-Patterns

- **Do not use** for tasks outside the domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval

## Composition

- **Peers**: Other skills in the \`\` domain may be composed in sequence
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

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-flow-canon
node_type: skill
path: 07_SKILLS/amos-flow-canon/SKILL.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
