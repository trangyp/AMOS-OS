---
title: L18 ACTION PRIMITIVES COGNITIVE MATRIX INVARIANTS
type: note
source: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L18_ACTION
tags:
- note
- matrix/l18-action
- domain/cognitive-matrix
- trang-framework-recursive-ontology-dynamics
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# L18 — Invariants

**Package:** `L18_ACTION`
**Class:** `COGNITIVE_MATRIX_CONTRACT`
**Epistemic class:** `DERIVED / MODEL EXTENSION`
**Status:** `CONTRACT_FILLED / NOT_IMPLEMENTED / NOT_VALIDATED`
**Filled by:** governed generator `fill_matrix.py` · **Date:** `2026-08-26`

## Scope

Covers action dispatch, capability gating, and execution receipts.

## Invariants

- `INV-L18-1`: No effect executes without a per-task authority grant; denial reasons are always stated.
- `INV-L18-2`: External writes are gated by can_write/can_delete checks.

## Hard boundaries

```text
CONTRACT_FILLED != IMPLEMENTED
DOCUMENTED != EXECUTABLE
MODEL != VERIFIED
UNKNOWN/GAP != PASS
```

---

[[COGNITIVE_MATRIX_MOC]] · [[00_ROOT_MOC]]|[[AMOS MOC]]

---
RSCF-NODE
node_id: l18_primitives_invariants
node_type: note
path: 01_PRIMITIVES/L18_ACTION/L18_ACTION_PRIMITIVES_COGNITIVE_MATRIX_INVARIANTS.md
claim_class: DERIVED
node_path_note: /Users/mac/Documents/AMOS_OS/25_COGNITIVE_MATRIX/01_PRIMITIVES/L18_ACTION/L18_ACTION_PRIMITIVES_COGNITIVE_MATRIX_INVARIANTS.md

---
**MOC:** [[L18_ACTION_MOC]]

---
**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

