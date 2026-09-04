---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: L16 PLANNING PRIMITIVES COGNITIVE MATRIX DEPENDENCIES
type: note
source: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L16_PLANNING
tags:
  - note
  - matrix/l16-planning
  - domain/cognitive-matrix
  - trang-framework-recursive-ontology-dynamics
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# L16 — Dependencies

**Package:** `L16_PLANNING`
**Class:** `COGNITIVE_MATRIX_CONTRACT`
**Epistemic class:** `DERIVED / MODEL EXTENSION`
**Status:** `CONTRACT_FILLED / NOT_IMPLEMENTED / NOT_VALIDATED`
**Filled by:** governed generator `fill_matrix.py` · **Date:** `2026-08-26`

## Scope

Covers plan synthesis, feasibility gating, and contingency embedding.

## Upstream dependencies

- [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L15_GOAL_FORMATION/L15_GOAL_FORMATION_PRIMITIVES_COGNITIVE_MATRIX_README|L15_GOAL_FORMATION_PRIMITIVES_COGNITIVE_MATRIX_README]]
- [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L12_COUNTERFACTUAL_SIMULATION/L12_COUNTERFACTUAL_SIMULATION_PRIMITIVES_COGNITIVE_MATRIX_README|L12_COUNTERFACTUAL_SIMULATION_PRIMITIVES_COGNITIVE_MATRIX_README]]

## Downstream dependents

- [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L17_DECISION/L17_DECISION_PRIMITIVES_COGNITIVE_MATRIX_README|L17_DECISION_PRIMITIVES_COGNITIVE_MATRIX_README]]
- O12_PLAN

Dependency direction follows the primitive flow order; cycles are defects.

## Hard boundaries

```text
CONTRACT_FILLED != IMPLEMENTED
DOCUMENTED != EXECUTABLE
MODEL != VERIFIED
UNKNOWN/GAP != PASS
```

______________________________________________________________________

[[25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_MOC|COGNITIVE_MATRIX_MOC]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]|[[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

RSCF-NODE
node_id: l16_primitives_dependencies
node_type: note
path: 01_PRIMITIVES/L16_PLANNING/L16_PLANNING_PRIMITIVES_COGNITIVE_MATRIX_DEPENDENCIES.md
claim_class: DERIVED
node_path_note: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L16_PLANNING/L16_PLANNING_PRIMITIVES_COGNITIVE_MATRIX_DEPENDENCIES.md

______________________________________________________________________

**MOC:** [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L16_PLANNING/L16_PLANNING_MOC|L16_PLANNING_MOC]]

______________________________________________________________________

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
