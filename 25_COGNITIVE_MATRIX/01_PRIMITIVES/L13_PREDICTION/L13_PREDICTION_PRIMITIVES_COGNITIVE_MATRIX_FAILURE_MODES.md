---
title: L13 PREDICTION PRIMITIVES COGNITIVE MATRIX FAILURE MODES
type: note
tags: [note, l13-prediction]
---

# L13 — Failure Modes

**Package:** `L13_PREDICTION`  
**Class:** `COGNITIVE_MATRIX_CONTRACT`  
**Epistemic class:** `DERIVED / MODEL EXTENSION`  
**Status:** `CONTRACT_FILLED / NOT_IMPLEMENTED / NOT_VALIDATED`  
**Filled by:** governed generator `fill_matrix.py` · **Date:** `2026-08-26`

## Scope

Covers forecast emission, calibration scoring, and horizon discipline.

## Failure modes

- `FM-L13-01`: Overconfident narrow bands. → detection: calibration curve audit
- `FM-L13-02`: Horizon confusion (short-term skill sold as long-term). → detection: horizon stratification

## Hard boundaries

```text
CONTRACT_FILLED != IMPLEMENTED
DOCUMENTED != EXECUTABLE
MODEL != VERIFIED
UNKNOWN/GAP != PASS
```

---

[[COGNITIVE_MATRIX_MOC]] · [[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: l13_primitives_failure_modes
node_type: note
path: 01_PRIMITIVES/L13_PREDICTION/L13_PREDICTION_PRIMITIVES_COGNITIVE_MATRIX_FAILURE_MODES.md
claim_class: DERIVED
node_path_note: /Users/mac/Documents/AMOS_OS/25_COGNITIVE_MATRIX/01_PRIMITIVES/L13_PREDICTION/L13_PREDICTION_PRIMITIVES_COGNITIVE_MATRIX_FAILURE_MODES.md

---
**MOC:** [[L13_PREDICTION_MOC]]
