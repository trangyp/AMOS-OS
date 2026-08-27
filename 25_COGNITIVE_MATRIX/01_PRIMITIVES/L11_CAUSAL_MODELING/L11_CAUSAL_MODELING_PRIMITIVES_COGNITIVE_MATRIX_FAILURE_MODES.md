---
title: L11 CAUSAL MODELING PRIMITIVES COGNITIVE MATRIX FAILURE MODES
type: note
tags: [note, l11-causal-modeling]
---


# L11 — Failure Modes

**Package:** `L11_CAUSAL_MODELING`  
**Class:** `COGNITIVE_MATRIX_CONTRACT`  
**Epistemic class:** `DERIVED / MODEL EXTENSION`  
**Status:** `CONTRACT_FILLED / NOT_IMPLEMENTED / NOT_VALIDATED`  
**Filled by:** governed generator `fill_matrix.py` · **Date:** `2026-08-26`

## Scope

Covers causal graph maintenance, intervention semantics, and confounder handling.

## Failure modes

- `FM-L11-01`: Correlation promoted to causation. → detection: evidence-class gate
- `FM-L11-02`: Collider conditioning induces spurious links. → detection: graph-structure check

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
node_id: l11_primitives_failure_modes
node_type: note
path: 01_PRIMITIVES/L11_CAUSAL_MODELING/L11_CAUSAL_MODELING_PRIMITIVES_COGNITIVE_MATRIX_FAILURE_MODES.md
claim_class: DERIVED
node_path_note: /Users/mac/Documents/AMOS_OS/25_COGNITIVE_MATRIX/01_PRIMITIVES/L11_CAUSAL_MODELING/L11_CAUSAL_MODELING_PRIMITIVES_COGNITIVE_MATRIX_FAILURE_MODES.md

---
**MOC:** [[L11_CAUSAL_MODELING_MOC]]
