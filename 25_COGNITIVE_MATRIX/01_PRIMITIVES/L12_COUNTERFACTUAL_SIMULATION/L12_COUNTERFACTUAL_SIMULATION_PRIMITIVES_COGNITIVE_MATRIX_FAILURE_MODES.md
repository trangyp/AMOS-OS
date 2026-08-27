---
title: L12 COUNTERFACTUAL SIMULATION PRIMITIVES COGNITIVE MATRIX FAILURE MODES
type: note
tags: [note, l12-counterfactual-simulation]
---

# L12 — Failure Modes

**Package:** `L12_COUNTERFACTUAL_SIMULATION`  
**Class:** `COGNITIVE_MATRIX_CONTRACT`  
**Epistemic class:** `DERIVED / MODEL EXTENSION`  
**Status:** `CONTRACT_FILLED / NOT_IMPLEMENTED / NOT_VALIDATED`  
**Filled by:** governed generator `fill_matrix.py` · **Date:** `2026-08-26`

## Scope

Covers scenario construction, simulation honesty rules, and pessimism correction.

## Failure modes

- `FM-L12-01`: Best-case branch cherry-picked. → detection: branch-coverage audit
- `FM-L12-02`: Unmodeled coupling invalidates independence assumptions. → detection: coupling review

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
node_id: l12_primitives_failure_modes
node_type: note
path: 01_PRIMITIVES/L12_COUNTERFACTUAL_SIMULATION/L12_COUNTERFACTUAL_SIMULATION_PRIMITIVES_COGNITIVE_MATRIX_FAILURE_MODES.md
claim_class: DERIVED
node_path_note: /Users/mac/Documents/AMOS_OS/25_COGNITIVE_MATRIX/01_PRIMITIVES/L12_COUNTERFACTUAL_SIMULATION/L12_COUNTERFACTUAL_SIMULATION_PRIMITIVES_COGNITIVE_MATRIX_FAILURE_MODES.md

---
**MOC:** [[L12_COUNTERFACTUAL_SIMULATION_MOC]]
