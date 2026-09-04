---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: murk engine expansion
type: reference
source: 07_SKILLS/amos-formal-engines-master/references
tags:
  - reference
  - amos-formal-engines-master
  - type/skill
  - law-hierarchy
  - trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# MURK Engine Expansion

> Source: `_00_Cosmo brain/engine/M/murk-engine-expansion.md`
> Epistemic class: SOURCE_DERIVED

______________________________________________________________________

## type: doc title: MURK Engine — 19-Primitive Absolute Logic Kernel and Brain Integration created: 2026-08-22 tags: [canon-group/tech-ai, canon/framework, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/murk-engine-expansion, engine]

## MURK Engine — 19-Primitive Absolute Logic Kernel

MURK is the **19-primitive Absolute Logic kernel** that forms the structured reasoning layer of the AMOS cognitive architecture. It provides a 19x19 interaction matrix (361 cells, 100% direct coverage) that ensures every primitive interacts with every other, leaving no gaps in the reasoning kernel. MURK operates within the 7-Part Universe Canon scaffold as the STRUCTURED REASONING component (Part III).

## 19 Typed Primitives

The MURK primitives are represented by a typed Enum for strict type-checking:

| #   | Primitive     | Description                           |
| --- | ------------- | ------------------------------------- |
| 1   | Existence     | Foundational being/presence predicate |
| 2   | NonExistence  | Absence/negation of being             |
| 3   | Causality     | Cause-effect linkage across time      |
| 4   | Temporal      | Time-ordering and temporal relations  |
| 5   | Informational | Information state and content         |
| 6   | Topological   | Spatial and structural relations      |
| 7   | Identity      | Sameness and persistence of entities  |
| 8   | Convergence   | Coming together of trajectories       |
| 9   | Divergence    | Separation of trajectories            |
| 10  | Paradox       | Self-referential contradiction        |
| 11  | PositiveLogic | Affirmative logical operator          |
| 12  | NegativeLogic | Negation logical operator             |
| 13  | ZeroLogic     | Null/zero-valued logic                |
| 14  | DualLogic     | Both-true-and-false logic             |
| 15  | MultiLogic    | Many-valued logic                     |
| 16  | MetaLogic     | Logic about logic                     |
| 17  | SupraLogic    | Beyond-level logic                    |
| 18  | AntiLogic     | Oppositional logic                    |
| 19  | NullLogic     | Empty/void logic                      |

## 19x19 Interaction Matrix

The full interaction matrix contains 361 cells with 100% direct coverage. Every primitive interacts with every other primitive, ensuring no reasoning gap exists in the kernel. This structural completeness is a key differentiator from standard logic systems that only define a subset of possible interactions.

## 5 Core Algorithms

1. **structural_input** — Parses and structures incoming reasoning input
1. **kernel_transform** — Applies the 19x19 transformation matrix to input primitives
1. **system_alignment** — Aligns MURK output with the broader cognitive system
1. **entropy_reduction** — Reduces reasoning entropy through deterministic compression
1. **detect_collapse** — Identifies when reasoning collapses under paradox or contradiction

## 5 Resolution Laws and Meta-Logic Overrides

MURK includes 5 resolution laws plus meta-logic overrides that govern how primitive interactions resolve. These laws determine which primitive takes precedence when interactions produce conflicting results, and how meta-logic operators (MetaLogic, SupraLogic, AntiLogic, NullLogic) override standard resolution.

## Collapse Detection

MURK detects three types of reasoning collapse:

- **Dissolution** — Reasoning dissolves into incoherence
- **Driftless** — Reasoning stalls without productive drift
- **TerminalQuiet** — Reasoning reaches a terminal state with no further output

When collapse is detected, MURK overrides the absolute_collapse_risk field in the brain model's CognitiveState and adds flags to the state's flag set.

## Brain Integration

MURK is wired into the ExecutableBrainModel via `AMOS_MURK_BRAIN_INTEGRATION.py` (738 lines). It adds the following fields to CognitiveState:

- `murk_primitives` — Active primitive set
- `murk_transformations` — Applied transformations
- `murk_compressed_result` — Compressed reasoning output
- `murk_collapse_state` — Detected collapse type (if any)
- `murk_session_id` — Session identifier
- `murk_aligned` — Alignment status with broader system
- `murk_alignment_issues` — Detected alignment problems
- `murk_timestamp` — Processing timestamp
- `murk_causal_driver` — Identified causal driver of transformation

## Reasoning Flow

1. User input arrives as `state.input_text`
1. MURK layer reads input, runs full pipeline (5 algorithms)
1. MURK writes results to state fields (primitives, transformations, compressed result, collapse state)
1. Brain model's other 60+ layers process the MURK-augmented state
1. Control/integrity layer gates the output
1. Output produced with provenance trail

## What MURK Adds Beyond the Brain Model

- **Causal driver analysis**: MURK identifies what CAUSES a transformation, not just what the transformation is
- **Collapse detection**: MURK detects when reasoning collapses (paradox, anti-logic, null) and flags it
- **19x19 structural coverage**: Every primitive interacts with every other — no gaps in the reasoning kernel
- **Deterministic**: Same input produces same output every time (no randomness)

## Formal Specification Foundation

MURK is grounded in the AMOS CORE-19 formal specification (Lean-style), which defines foundational types and predicates:

- **Sorts**: Entity, Time, Region, Information
- **Predicates**: Existence, Causality, Spatial Location, Information State
- **Meta-logical operators**: PositiveLogic, NegativeLogic, ContradictionLogic, ExistenceLogic, ModalLogic

This formal spec underpins the Core-19 reasoning kernel used across all AMOS engines, providing the type-theoretic foundation for the 19x19 semantic matrix, the MURK absolute logic DB, and all domain engine reasoning chains.

## Related Vault Sources

- `_00_Cosmo brain/engine/M/murk-engine-expansion.md` — Bridge note (original source)
- `_00_Cosmo brain/amos-general/A/forex/AMOS forex__packages__murk__primitives.md` — 19 primitive Enum definitions
- `_00_Cosmo brain/quantum/Quantum_Omega_Cognitive_Architecture_Overview.md` — MURK reasoning layer architecture
- `_00_Cosmo brain/amos-general/A/CORE/AMOS Core-19 Formal Spec Lean.md` — Lean-style formal specification
- `_00_Cosmo brain/engine/M/mental_state_engine.md` — Mental state engine (companion in engine/M/)

______________________________________________________________________

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
  **MOC:** references_MOC

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-formal-engines-master-murk-engine-expansion
node_type: reference
path: 07_SKILLS/amos-formal-engines-master/references/murk_engine_expansion.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
