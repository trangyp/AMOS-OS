---
title: L06 WORKING STATE PRIMITIVES COGNITIVE MATRIX FAILURE MODES
type: note
source: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L06_WORKING_STATE
tags: [note, l06-working-state, canon/cognitive-matrix]
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# L06 — Failure Modes

**Package:** `L06_WORKING_STATE`  
**Class:** `COGNITIVE_MATRIX_CONTRACT`  
**Epistemic class:** `DERIVED / MODEL EXTENSION`  
**Status:** `CONTRACT_FILLED / NOT_IMPLEMENTED / NOT_VALIDATED`  
**Filled by:** governed generator `fill_matrix.py` · **Date:** `2026-08-26`

## Scope

Covers working-set membership, decay, and context switches.

## Failure modes

- `FM-L06-01`: Working-set overflow drops critical context. → detection: capacity monitor
- `FM-L06-02`: Checkpoint loss on interruption. → detection: checkpoint persistence test

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
node_id: l06_primitives_failure_modes
node_type: note
path: 01_PRIMITIVES/L06_WORKING_STATE/L06_WORKING_STATE_PRIMITIVES_COGNITIVE_MATRIX_FAILURE_MODES.md
claim_class: DERIVED
node_path_note: /Users/mac/Documents/AMOS_OS/25_COGNITIVE_MATRIX/01_PRIMITIVES/L06_WORKING_STATE/L06_WORKING_STATE_PRIMITIVES_COGNITIVE_MATRIX_FAILURE_MODES.md

---
**MOC:** [[L06_WORKING_STATE_MOC]]

---
**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
