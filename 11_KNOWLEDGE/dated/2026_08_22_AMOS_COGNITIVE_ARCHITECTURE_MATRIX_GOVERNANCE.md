---
title: AMOS Cognitive Architecture Matrix Governance (gaps 321-339)
created: '2026-08-22'
origin: Hermes ↔ Cosmo Brain
origin_architect: Trang Phan
type: note
source: 11_KNOWLEDGE/dated
tags:
- cosmo
- amos
- canon-group/system
- rscf/claim
- rscf/state/observation
- topic/implementation
- topic/completion-graph
- topic/cognitive-architecture
- dated
- dated/2026-08-22
- canon/knowledge
status: verified
provenance: OBSERVATION
confidence: VERIFIED
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: temporal_log
---


# AMOS Cognitive Architecture Matrix Governance — gaps 321-339

> Epistic class: OBSERVATION
> Conclusion label: `VERIFIED` — 19 explicit matrix gaps and `CognitiveMatrixGovernor` wired into `AmosKernel`, all tests pass.
> Governing law: `integrity > completeness > fluency > speed > token savings`.

## What was implemented

The Cognitive Architecture Matrix (CAM) exposes missing **interactions**, not missing modules. The 4-axis matrix has 30 cognitive primitives × 17 lifecycle operations × 9 control planes × 3 scales = 13,770 cells. 68.02% of these cells are structural gaps (9,367 cells). These collapse to **243 structural-gap unknown-unknowns** (one per primitive × plane pair) plus **3 original unknown-unknowns** = **246 total unknown-unknowns** tracked. The explicit `GapKind.RELATION` gaps 321-339 were closed with a dedicated governor in the AMOS OS Kernel.

```
cosmo-brain/AMOS_OS_KERNEL/
├── amos/governance/cognitive_matrix.py       (subsystems + CognitiveMatrixGovernor)
├── amos/governance/cognitive_architecture_matrix.py  (alternate canonical file)
├── amos/governance/seed_cognitive_matrix.py  (seeds 19 matrix gaps)
├── tests/test_cognitive_matrix.py            (27+ tests)
├── amos/kernel.py                            (cognitive_matrix_governor wired)
└── amos/__init__.py                          (CognitiveMatrixGovernor, CognitiveInteractionManager)
```

## The 19 matrix gaps

The explicit missing (primitive, control-plane) interactions, seeded with 11-layer completion chains:

| Gap | Title | Interaction |
| ---: | --- | --- |
| 321 | Cognitive perception (Sense plane) | primitive perception ↔ sense control |
| 322 | Cognitive attention (Focus plane) | primitive attention ↔ focus control |
| 323 | Cognitive memory (Recall plane) | primitive memory ↔ recall control |
| 324 | Cognitive reasoning (Reason plane) | primitive reasoning ↔ reason control |
| 325 | Cognitive emotion (Affect plane) | primitive emotion ↔ affect control |
| 326 | Cognitive action (Act plane) | primitive action ↔ act control |
| 327 | Cognitive language (Signal plane) | primitive language ↔ signal control |
| 328 | Cognitive identity (Self plane) | primitive identity ↔ self control |
| 329 | Cognitive learning (Adapt plane) | primitive learning ↔ adapt control |
| 330 | Cognitive planning (Goal plane) | primitive planning ↔ goal control |
| 331 | Cognitive metacognition (Monitor plane) | primitive metacognition ↔ monitor control |
| 332 | Cognitive creativity (Create plane) | primitive creativity ↔ create control |
| 333 | Cognitive social (Relate plane) | primitive social ↔ relate control |
| 334 | Cognitive ethics (Ought plane) | primitive ethics ↔ ought control |
| 335 | Cognitive will (Choose plane) | primitive will ↔ choose control |
| 336 | Cognitive integration (Bind plane) | primitive integration ↔ bind control |
| 337 | Cognitive collapse (Boundary plane) | primitive collapse ↔ boundary control |
| 338 | Cognitive emergence (Field plane) | primitive emergence ↔ field control |
| 339 | Cognitive security (Governance plane) | primitive security ↔ governance control |

## Governor gates

`CognitiveMatrixGovernor.evaluate_post()` returns 3 advisory gates:

- `cognitive-matrix-missing-interactions` (CONDITIONAL)
- `cognitive-matrix-partial-interactions` (CONDITIONAL)
- `cognitive-matrix-cognitive-security-gap-339` (CONDITIONAL)

## Verification

```bash
cd cosmo-brain/AMOS_OS_KERNEL
python3 -m pytest tests/test_cognitive_matrix.py -q
python3 -m pytest tests/ -q
```

- `tests/test_cognitive_matrix.py`: all matrix-specific tests pass
- `tests/`: **1533 passed, 0 failures**

## Why this matters

Closing the matrix means the AMOS OS Kernel no longer treats completion as a flat list of modules. It now tracks cross-cutting interactions across the full cognitive space, which is the primary unknown-unknown detector for the brain.

## `seed_cognitive_matrix` runtime output

```python
{'matrix_explicit_gaps_seeded': 19,
 'matrix_structural_gap_unknowns_registered': 243,
 'matrix_total_cells': 13770,
 'matrix_existing': 272,
 'matrix_partial': 3162,
 'matrix_missing': 969,
 'matrix_structural_gap': 9367,
 'matrix_pct_structural_gap': 68.02,
 'matrix_loaded': True}
```

## Anti-fabrication

- Source: `python3 -m pytest tests/ -q` run 2026-08-22.
- Verification: 1533 passed, 0 failed.
- Runtime `seed_cognitive_matrix` output: 243 structural-gap unknowns, 19 explicit gaps, 9,367 structural cells, 68.02% structural-gap ratio.
- The 19 explicit gaps are `GapKind.RELATION` records in the Completion Graph.

## Links
- [[00_COSMO_BRAIN_MOC]]
- 2026-08-22 AMOS All 249 Gaps Closed
- 2026-08-22 human_interaction cluster closed

---
**MOC:** [[DATED_MOC]]
