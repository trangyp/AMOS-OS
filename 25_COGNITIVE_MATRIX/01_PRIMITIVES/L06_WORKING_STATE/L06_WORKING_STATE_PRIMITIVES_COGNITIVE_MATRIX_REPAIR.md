---
title: L06 WORKING STATE PRIMITIVES COGNITIVE MATRIX REPAIR
type: note
tags: [note, l06-working-state]
---


# L06 — Repair & Recovery

**Package:** `L06_WORKING_STATE`  
**Class:** `COGNITIVE_MATRIX_CONTRACT`  
**Epistemic class:** `DERIVED / MODEL EXTENSION`  
**Status:** `CONTRACT_FILLED / NOT_IMPLEMENTED / NOT_VALIDATED`  
**Filled by:** governed generator `fill_matrix.py` · **Date:** `2026-08-26`

## Scope

Covers working-set membership, decay, and context switches.

## Failure handling

- On `FM-L06-01`: Evict lowest-salience item; checkpoint evictees to L07.
- On `FM-L06-02`: Restore from last durable checkpoint; mark gap in continuity.

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

[[COGNITIVE_MATRIX_MOC]] · 00_ROOT_MOC|AMOS MOC

---
RSCF-NODE
node_id: l06_primitives_repair
node_type: note
path: 01_PRIMITIVES/L06_WORKING_STATE/L06_WORKING_STATE_PRIMITIVES_COGNITIVE_MATRIX_REPAIR.md
claim_class: DERIVED
node_path_note: /Users/mac/Documents/AMOS_OS/25_COGNITIVE_MATRIX/01_PRIMITIVES/L06_WORKING_STATE/L06_WORKING_STATE_PRIMITIVES_COGNITIVE_MATRIX_REPAIR.md

---
**MOC:** [[L06_WORKING_STATE_MOC]]
