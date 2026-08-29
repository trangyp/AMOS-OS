---
title: L18 ACTION PRIMITIVES COGNITIVE MATRIX FAILURE MODES
type: note
source: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L18_ACTION
tags:
- note
- l18-action
- domain/cognitive-matrix
- cognitive-matrix-moc
- 00-root-moc
- amos-moc
- l18-action-moc
- trang-framework-recursive-ontology-dynamics
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# L18 — Failure Modes

**Package:** `L18_ACTION`
**Class:** `COGNITIVE_MATRIX_CONTRACT`
**Epistemic class:** `DERIVED / MODEL EXTENSION`
**Status:** `CONTRACT_FILLED / NOT_IMPLEMENTED / NOT_VALIDATED`
**Filled by:** governed generator `fill_matrix.py` · **Date:** `2026-08-26`

## Scope

Covers action dispatch, capability gating, and execution receipts.

## Failure modes

- `FM-L18-01`: Effect lands outside declared scope. → detection: scope assertion post-check
- `FM-L18-02`: Tool failure mid-action leaves partial state. → detection: transactional wrapper

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
node_id: l18_primitives_failure_modes
node_type: note
path: 01_PRIMITIVES/L18_ACTION/L18_ACTION_PRIMITIVES_COGNITIVE_MATRIX_FAILURE_MODES.md
claim_class: DERIVED
node_path_note: /Users/mac/Documents/AMOS_OS/25_COGNITIVE_MATRIX/01_PRIMITIVES/L18_ACTION/L18_ACTION_PRIMITIVES_COGNITIVE_MATRIX_FAILURE_MODES.md

---
**MOC:** [[L18_ACTION_MOC]]

---
**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
