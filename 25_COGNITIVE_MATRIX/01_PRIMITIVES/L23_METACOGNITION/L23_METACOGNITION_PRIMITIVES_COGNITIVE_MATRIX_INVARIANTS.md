---
title: L23 METACOGNITION PRIMITIVES COGNITIVE MATRIX INVARIANTS
type: note
tags: [note, l23-metacognition]
---

# L23 — Invariants

**Package:** `L23_METACOGNITION`  
**Class:** `COGNITIVE_MATRIX_CONTRACT`  
**Epistemic class:** `DERIVED / MODEL EXTENSION`  
**Status:** `CONTRACT_FILLED / NOT_IMPLEMENTED / NOT_VALIDATED`  
**Filled by:** governed generator `fill_matrix.py` · **Date:** `2026-08-26`

## Scope

Covers monitor taxonomy, interrupt thresholds, and uncertainty calibration of self-reports.

## Invariants

- `INV-L23-1`: Confidence ceilings are enforced, not advisory (cap 0.95).
- `INV-L23-2`: Monitor interrupts are fail-closed: unresolved anomaly halts escalation.

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
node_id: l23_primitives_invariants
node_type: note
path: 01_PRIMITIVES/L23_METACOGNITION/L23_METACOGNITION_PRIMITIVES_COGNITIVE_MATRIX_INVARIANTS.md
claim_class: DERIVED
node_path_note: /Users/mac/Documents/AMOS_OS/25_COGNITIVE_MATRIX/01_PRIMITIVES/L23_METACOGNITION/L23_METACOGNITION_PRIMITIVES_COGNITIVE_MATRIX_INVARIANTS.md

---
**MOC:** [[L23_METACOGNITION_MOC]]
