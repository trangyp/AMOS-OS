---
title: L20 CREDIT ASSIGNMENT PRIMITIVES COGNITIVE MATRIX REPAIR
type: note
tags: [note, l20-credit-assignment]
---

# L20 — Repair & Recovery

**Package:** `L20_CREDIT_ASSIGNMENT`  
**Class:** `COGNITIVE_MATRIX_CONTRACT`  
**Epistemic class:** `DERIVED / MODEL EXTENSION`  
**Status:** `CONTRACT_FILLED / NOT_IMPLEMENTED / NOT_VALIDATED`  
**Filled by:** governed generator `fill_matrix.py` · **Date:** `2026-08-26`

## Scope

Covers temporal credit decay, counterfactual attribution, and blame-symmetry rules.

## Failure handling

- On `FM-L20-01`: Recompute with decay model; log correction.
- On `FM-L20-02`: Deduplicate by failure-mode independence before scoring.

## Recovery basin

Roll back to last validated state snapshot; re-run from upstream anchor.

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
node_id: l20_primitives_repair
node_type: note
path: 01_PRIMITIVES/L20_CREDIT_ASSIGNMENT/L20_CREDIT_ASSIGNMENT_PRIMITIVES_COGNITIVE_MATRIX_REPAIR.md
claim_class: DERIVED
node_path_note: /Users/mac/Documents/AMOS_OS/25_COGNITIVE_MATRIX/01_PRIMITIVES/L20_CREDIT_ASSIGNMENT/L20_CREDIT_ASSIGNMENT_PRIMITIVES_COGNITIVE_MATRIX_REPAIR.md

---
**MOC:** [[L20_CREDIT_ASSIGNMENT_MOC]]
