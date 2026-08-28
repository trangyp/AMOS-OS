---
title: SKILL — Amos Formal Engines Master
type: skill
source: 07_SKILLS/amos-formal-engines-master
name: amos-formal-engines-master
description: AMOS Formal Engines — MURK 19x19, Go Board 19x19, tensor composition, formal specifications,
  proof systems. 6 typed tensors (T_R, T_F, T_E, T_C, T_G, T_M) with 5-check axis table. Use for formal
  re...
parent_skill: none
domain: formal
origin_architect: Trang Phan
epistemic_class: SOURCE_CANON
tags:
- type/skill
- canon/skill
- domain/formal-engines
- rscf/source_claim
- hml/h
- epistemic/source_canon
- amos_os
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
rscf_state: SOURCE_CLAIM
hml_level: H
gmef_gates:
- L0_integrity
- L1_epistemic
- L2_provenance
- L3_dependency
- L5_scope
- L7_authority
- L22_replayability
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L3
- L4
- L5
- L7
- L16
- L17
- L18
- L19
- L22
---

# L02_ATTENTION — Purpose

## Identity

Origin architect: **Trang Phan**. Domain: formal. Parent: none. Epistemic class: SOURCE_CANON. H/M/L: H.
## When to Use

- When performing formal verification, symbolic execution, proof checking, or mathematical reasoning
- When using MURK 19x19 interaction matrix for absolute logic reasoning
- When using Go Board 19x19 for compositional game-theoretic analysis
- When composing typed tensors (T_R, T_F, T_E, T_C, T_G, T_M) with axis compatibility gates
- When building formal specifications, proof systems, or constraint propagation
- When a child skill routes a formal verification or proof task to this master

- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **formal_engines.execute_formal**: Execute AMOS Formal Engines formal engines: MURK 19x19, Go Board, tensor composition, and RSCF proof systems.
- **formal_engines.validate_formal**: Validate AMOS Formal Engines proofs for completeness, soundness, tensor contract compliance, and axiom application.
- **formal_engines.analyze_tensor**: Analyze AMOS Formal Engines tensor structure: typed cells, axis compatibility, composition gates, and relation topology.
- **formal_engines.trace_formal_provenance**: Trace AMOS Formal Engines formal outputs to axioms, inference rules, tensor contracts, and proof graph.
- **formal_engines.assess_formal_claim**: Assess AMOS Formal Engines formal claims for proof status, tensor compatibility, gap registry, and invariant compliance.
- **formal_engines.manage_formal_lifecycle**: Manage AMOS Formal Engines formal lifecycle: axiomatize, derive, validate, cross-check, and finalize proof.
- **formal_engines.detect_formal_drift**: Detect formal drift: axiom erosion, tensor axis mismatch, proof graph degradation, and invariant violation.
- **formal_engines.escalate_formal_gaps**: Escalate AMOS Formal Engines formal gaps: flag unproven claims, tensor incompatibility, trigger gap registry repair.
- **formal_engines.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **formal_engines.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **formal_engines.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Domain Knowledge

> **Sources**: `_00_Cosmo brain/amos-general/A/forex/AMOS forex__packages__murk__primitives.md` (content_hash: b289395a883dab29), `_00_Cosmo brain/amos-general/A/amos/amos-go-board-19x19.md` (content_hash: 7d5f3bb30310282b) (vault canon, SOURCE_CLAIM)

### MURK 19 Primitive Definitions

The MURK (Absolute Logic) kernel defines 19 typed primitives represented as an Enum for strict type-checking:

| # | Primitive | Class |
|---|-----------|-------|
| 1 | Existence | ontological |
| 2 | NonExistence | ontological |
| 3 | Causality | causal |
| 4 | Temporal | temporal |
| 5 | Informational | informational |
| 6 | Topological | spatial |
| 7 | Identity | identity |
| 8 | Convergence | dynamic |
| 9 | Divergence | dynamic |
| 10 | Paradox | paradox |
| 11 | PositiveLogic | logic-valence |
| 12 | NegativeLogic | logic-valence |
| 13 | ZeroLogic | logic-valence |
| 14 | DualLogic | logic-valence |
| 15 | MultiLogic | logic-valence |
| 16 | MetaLogic | meta |
| 17 | SupraLogic | meta |
| 18 | AntiLogic | meta |
| 19 | NullLogic | meta |

The 19x19 interaction matrix (361 cells) provides 100% direct coverage of all primitive interactions. 5 resolution laws govern conflict resolution. The MURK reasoning engine is implemented at `cosmo-brain/AMOS_MURK_REASONING_ENGINE.py` with 231 total tests.

### Go Board 19x19 Formal System

The Go Board 19x19 is a formal system implementing 62+ sections from a 75-section formal spec (83%+). Key components:

- **Compositional engine**: `T = T_O∘T_G∘T_L∘T_E∘T_A∘T_K∘T_Φ∘T_Ω∘T_M`
- **Dependency cone**: CR (cone reach) / CD (cone depth)
- **Liberty independence graph**: eye topology (EyeQuality/PVR/Robustness)
- **Aji system**: DAG with half-life and latent threat tracking
- **Memory system**: decay, classes, prio
- [[AGENT_TEMPLATE]]

---
**MOC:** [[amos-formal-engines-master_MOC]]

## Examples

- **Scenario**: When performing formal verification, symbolic execution, proof checking, or mathematical reasoning
  - **Input**: A query matching this skill's domain (formal)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When using MURK 19x19 interaction matrix for absolute logic reasoning
  - **Input**: A query matching this skill's domain (formal)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When using Go Board 19x19 for compositional game-theoretic analysis
  - **Input**: A query matching this skill's domain (formal)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the formal domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `none` — routes to this skill when formal specialization is needed
- **Peers**: Other skills in the `formal` domain may be composed in sequence
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

- `references/11k_murk_audit.md` — loaded on demand
- `references/amatrix_dynamics.md` — loaded on demand
- `references/constraint_engine.md` — loaded on demand
- `references/equation_firewall.md` — loaded on demand
- `references/murk_engine_expansion.md` — loaded on demand
- `references/omega_advanced_tensor_analysis.md` — loaded on demand
- `references/qfm_adversarial_hardening.md` — loaded on demand
- `references/qfm_architecture_refinement.md` — loaded on demand
- `references/qfm_consolidation.md` — loaded on demand
- `references/qfm_five_layer_architecture.md` — loaded on demand
- `references/qfm_max_power_consolidation.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `references/tensor_composition_governance.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `[[amos-formal-engines-master_MOC]]` — skill Map of Content
- `none` — parent skill
- `[[amos-formal-engines-master-workflow]]` — corresponding workflow
- `amos-formal-engines-master-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-formal-engines-master
node_type: skill
path: 07_SKILLS/amos-formal-engines-master/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
