---
title: L12 COUNTERFACTUAL SIMULATION PRIMITIVES COGNITIVE MATRIX INVARIANTS
type: note
tags: [note, l12-counterfactual-simulation]
---

# L12 — Invariants

**Package:** `L12_COUNTERFACTUAL_SIMULATION`  
**Class:** `COGNITIVE_MATRIX_CONTRACT`  
**Epistemic class:** `DERIVED / MODEL EXTENSION`  
**Status:** `CONTRACT_FILLED / NOT_IMPLEMENTED / NOT_VALIDATED`  
**Filled by:** governed generator `fill_matrix.py` · **Date:** `2026-08-26`

## Scope

Covers scenario construction, simulation honesty rules, and pessimism correction.

## Invariants

- `INV-L12-1`: Stable verdicts require ALL branches stable (simulation pessimism rule).
- `INV-L12-2`: Simulated outcomes are never reported as observed outcomes.

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
node_id: l12_primitives_invariants
node_type: note
path: 01_PRIMITIVES/L12_COUNTERFACTUAL_SIMULATION/L12_COUNTERFACTUAL_SIMULATION_PRIMITIVES_COGNITIVE_MATRIX_INVARIANTS.md
claim_class: DERIVED
node_path_note: /Users/mac/Documents/AMOS_OS/25_COGNITIVE_MATRIX/01_PRIMITIVES/L12_COUNTERFACTUAL_SIMULATION/L12_COUNTERFACTUAL_SIMULATION_PRIMITIVES_COGNITIVE_MATRIX_INVARIANTS.md

---
**MOC:** [[L12_COUNTERFACTUAL_SIMULATION_MOC]]
