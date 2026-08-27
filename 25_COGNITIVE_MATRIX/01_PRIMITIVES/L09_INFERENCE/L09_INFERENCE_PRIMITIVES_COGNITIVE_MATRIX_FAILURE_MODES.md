---
title: L09 INFERENCE PRIMITIVES COGNITIVE MATRIX FAILURE MODES
type: note
tags: [note, l09-inference]
---

# L09 — Failure Modes

**Package:** `L09_INFERENCE`  
**Class:** `COGNITIVE_MATRIX_CONTRACT`  
**Epistemic class:** `DERIVED / MODEL EXTENSION`  
**Status:** `CONTRACT_FILLED / NOT_IMPLEMENTED / NOT_VALIDATED`  
**Filled by:** governed generator `fill_matrix.py` · **Date:** `2026-08-26`

## Scope

Covers rule-gated deduction, abductive candidacy, and derivation-lineage tracking.

## Failure modes

- `FM-L09-01`: Rule applied outside its validity regime. → detection: regime-condition check
- `FM-L09-02`: Conjecture slippage: conditional result used unconditionally. → detection: CONDITIONAL-ON audit

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
node_id: l09_primitives_failure_modes
node_type: note
path: 01_PRIMITIVES/L09_INFERENCE/L09_INFERENCE_PRIMITIVES_COGNITIVE_MATRIX_FAILURE_MODES.md
claim_class: DERIVED
node_path_note: /Users/mac/Documents/AMOS_OS/25_COGNITIVE_MATRIX/01_PRIMITIVES/L09_INFERENCE/L09_INFERENCE_PRIMITIVES_COGNITIVE_MATRIX_FAILURE_MODES.md

---
**MOC:** [[L09_INFERENCE_MOC]]
