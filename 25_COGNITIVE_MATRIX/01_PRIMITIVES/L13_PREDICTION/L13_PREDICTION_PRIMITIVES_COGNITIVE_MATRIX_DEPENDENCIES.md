---
title: L13 PREDICTION PRIMITIVES COGNITIVE MATRIX DEPENDENCIES
type: note
tags: [note, l13-prediction]
---


# L13 — Dependencies

**Package:** `L13_PREDICTION`  
**Class:** `COGNITIVE_MATRIX_CONTRACT`  
**Epistemic class:** `DERIVED / MODEL EXTENSION`  
**Status:** `CONTRACT_FILLED / NOT_IMPLEMENTED / NOT_VALIDATED`  
**Filled by:** governed generator `fill_matrix.py` · **Date:** `2026-08-26`

## Scope

Covers forecast emission, calibration scoring, and horizon discipline.

## Upstream dependencies

- [[L09_INFERENCE_PRIMITIVES_COGNITIVE_MATRIX_README]]
- [[L10_WORLD_MODELING_PRIMITIVES_COGNITIVE_MATRIX_README]]

## Downstream dependents

- [[L19_OUTCOME_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]]
- [[L20_CREDIT_ASSIGNMENT_PRIMITIVES_COGNITIVE_MATRIX_README]]

Dependency direction follows the primitive flow order; cycles are defects.

## Hard boundaries

```text
CONTRACT_FILLED != IMPLEMENTED
DOCUMENTED != EXECUTABLE
MODEL != VERIFIED
UNKNOWN/GAP != PASS
```

---

[[COGNITIVE_MATRIX_MOC]] · 00_ROOT_MOC|AMOS MOC

---
RSCF-NODE
node_id: l13_primitives_dependencies
node_type: note
path: 01_PRIMITIVES/L13_PREDICTION/L13_PREDICTION_PRIMITIVES_COGNITIVE_MATRIX_DEPENDENCIES.md
claim_class: DERIVED
node_path_note: /Users/mac/Documents/AMOS_OS/25_COGNITIVE_MATRIX/01_PRIMITIVES/L13_PREDICTION/L13_PREDICTION_PRIMITIVES_COGNITIVE_MATRIX_DEPENDENCIES.md

---
**MOC:** [[L13_PREDICTION_MOC]]
