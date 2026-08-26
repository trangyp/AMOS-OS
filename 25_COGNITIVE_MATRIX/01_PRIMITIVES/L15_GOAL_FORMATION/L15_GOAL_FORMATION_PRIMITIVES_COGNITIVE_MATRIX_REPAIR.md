# L15 — Repair & Recovery

**Package:** `L15_GOAL_FORMATION`  
**Class:** `COGNITIVE_MATRIX_CONTRACT`  
**Epistemic class:** `DERIVED / MODEL EXTENSION`  
**Status:** `CONTRACT_FILLED / NOT_IMPLEMENTED / NOT_VALIDATED`  
**Filled by:** governed generator `fill_matrix.py` · **Date:** `2026-08-26`

## Scope

Covers goal decomposition, priority ordering, and goal-conflict detection.

## Failure handling

- On `FM-L15-01`: Reject goal until criteria are measurable.
- On `FM-L15-02`: Prune drifting subgoals; log drift distance.

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
node_id: l15_primitives_repair
node_type: note
path: 01_PRIMITIVES/L15_GOAL_FORMATION/L15_GOAL_FORMATION_PRIMITIVES_COGNITIVE_MATRIX_REPAIR.md
claim_class: DERIVED
node_path_note: /Users/mac/Documents/AMOS_OS/25_COGNITIVE_MATRIX/01_PRIMITIVES/L15_GOAL_FORMATION/L15_GOAL_FORMATION_PRIMITIVES_COGNITIVE_MATRIX_REPAIR.md
