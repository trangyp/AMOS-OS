---
title: L16 PLANNING PRIMITIVES COGNITIVE MATRIX REPAIR
type: note
tags: [note, l16-planning]
---

# L16 — Repair & Recovery

**Package:** `L16_PLANNING`  
**Class:** `COGNITIVE_MATRIX_CONTRACT`  
**Epistemic class:** `DERIVED / MODEL EXTENSION`  
**Status:** `CONTRACT_FILLED / NOT_IMPLEMENTED / NOT_VALIDATED`  
**Filled by:** governed generator `fill_matrix.py` · **Date:** `2026-08-26`

## Scope

Covers plan synthesis, feasibility gating, and contingency embedding.

## Failure handling

- On `FM-L16-01`: Reject; regenerate within full-precision constraints.
- On `FM-L16-02`: Halt execution; trigger replanning.

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
node_id: l16_primitives_repair
node_type: note
path: 01_PRIMITIVES/L16_PLANNING/L16_PLANNING_PRIMITIVES_COGNITIVE_MATRIX_REPAIR.md
claim_class: DERIVED
node_path_note: /Users/mac/Documents/AMOS_OS/25_COGNITIVE_MATRIX/01_PRIMITIVES/L16_PLANNING/L16_PLANNING_PRIMITIVES_COGNITIVE_MATRIX_REPAIR.md

---
**MOC:** [[L16_PLANNING_MOC]]
