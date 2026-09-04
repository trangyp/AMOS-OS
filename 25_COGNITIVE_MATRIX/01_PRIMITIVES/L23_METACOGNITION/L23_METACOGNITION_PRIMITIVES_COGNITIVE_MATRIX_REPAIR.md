---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: L23 METACOGNITION PRIMITIVES COGNITIVE MATRIX REPAIR
type: note
source: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L23_METACOGNITION
tags:
  - note
  - matrix/l23-metacognition
  - domain/cognitive-matrix
  - trang-framework-recursive-ontology-dynamics
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# L23 — Repair & Recovery

**Package:** `L23_METACOGNITION`
**Class:** `COGNITIVE_MATRIX_CONTRACT`
**Epistemic class:** `DERIVED / MODEL EXTENSION`
**Status:** `CONTRACT_FILLED / NOT_IMPLEMENTED / NOT_VALIDATED`
**Filled by:** governed generator `fill_matrix.py` · **Date:** `2026-08-26`

## Scope

Covers monitor taxonomy, interrupt thresholds, and uncertainty calibration of self-reports.

## Failure handling

- On `FM-L23-01`: Add monitor for the gap; backfill missed events.
- On `FM-L23-02`: Tune thresholds; require distinct signal per alert.

## Recovery basin

Roll back to last validated state snapshot; re-run from upstream anchor.

## Hard boundaries

```text
CONTRACT_FILLED != IMPLEMENTED
DOCUMENTED != EXECUTABLE
MODEL != VERIFIED
UNKNOWN/GAP != PASS
```

______________________________________________________________________

[[25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_MOC|COGNITIVE_MATRIX_MOC]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]|[[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

RSCF-NODE
node_id: l23_primitives_repair
node_type: note
path: 01_PRIMITIVES/L23_METACOGNITION/L23_METACOGNITION_PRIMITIVES_COGNITIVE_MATRIX_REPAIR.md
claim_class: DERIVED
node_path_note: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L23_METACOGNITION/L23_METACOGNITION_PRIMITIVES_COGNITIVE_MATRIX_REPAIR.md

______________________________________________________________________

**MOC:** [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L23_METACOGNITION/L23_METACOGNITION_MOC|L23_METACOGNITION_MOC]]

______________________________________________________________________

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
