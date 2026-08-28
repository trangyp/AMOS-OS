---
title: L11 CAUSAL MODELING PRIMITIVES COGNITIVE MATRIX INVARIANTS
type: note
source: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L11_CAUSAL_MODELING
tags:
- note
- l11-causal-modeling
- canon/cognitive-matrix
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# L11 — Invariants

**Package:** `L11_CAUSAL_MODELING`
**Class:** `COGNITIVE_MATRIX_CONTRACT`
**Epistemic class:** `DERIVED / MODEL EXTENSION`
**Status:** `CONTRACT_FILLED / NOT_IMPLEMENTED / NOT_VALIDATED`
**Filled by:** governed generator `fill_matrix.py` · **Date:** `2026-08-26`

## Scope

Covers causal graph maintenance, intervention semantics, and confounder handling.

## Invariants

- `INV-L11-1`: Causal edges require named evidence class (mechanism/intervention/RCT); observational-only edges stay correlational.
- `INV-L11-2`: Confounded relations are tagged, never silently promoted to causal.

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
node_id: l11_primitives_invariants
node_type: note
path: 01_PRIMITIVES/L11_CAUSAL_MODELING/L11_CAUSAL_MODELING_PRIMITIVES_COGNITIVE_MATRIX_INVARIANTS.md
claim_class: DERIVED
node_path_note: /Users/mac/Documents/AMOS_OS/25_COGNITIVE_MATRIX/01_PRIMITIVES/L11_CAUSAL_MODELING/L11_CAUSAL_MODELING_PRIMITIVES_COGNITIVE_MATRIX_INVARIANTS.md

---
**MOC:** [[L11_CAUSAL_MODELING_MOC]]

---
**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
