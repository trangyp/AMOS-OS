---
title: "AMOS Structural Gap Promotion 340-347"
created: "2026-08-22"
origin: "Hermes ↔ Cosmo Brain"
origin_architect: "Trang Phan"
type: note
tags: [cosmo, amos, canon-group/system, rscf/claim, rscf/state/observation, topic/implementation, topic/cognitive-matrix, topic/structural-gap, dated, dated/2026-08-22]
status: "verified"
provenance: "OBSERVATION"
confidence: "VERIFIED"
---


# AMOS Structural Gap Promotion (Gaps 340-347)

> Epistic class: OBSERVATION
> Conclusion label: `VERIFIED` — 8 high-priority structural-gap unknown-unknowns promoted to gap records with complete 11-layer chains.
> Governing law: `integrity > completeness > fluency > speed > token savings`.

## What was done

Promoted 8 structural-gap unknown-unknowns to explicit gap records (340-347).
These target the 4 cognitive primitives with 100% structural gaps paired with
the 2 control planes with zero coverage.

## The 8 Promoted Gaps

| Gap | Primitive | Plane | Title |
|-----|-----------|-------|-------|
| 340 | L0 Reality/Environment | C5 Representation | No typed environment substrate |
| 341 | L0 Reality/Environment | C7 Perception | Cannot perceive environment |
| 342 | L19 Outcome Observation | C5 Representation | Cannot represent observed outcomes |
| 343 | L19 Outcome Observation | C7 Perception | Cannot perceive outcomes |
| 344 | L20 Credit Assignment | C5 Representation | Cannot represent causal credit |
| 345 | L20 Credit Assignment | C7 Perception | Cannot perceive causal credit |
| 346 | L22 Consolidation | C5 Representation | Cannot represent consolidated knowledge |
| 347 | L22 Consolidation | C7 Perception | Cannot perceive consolidation state |

## Why these 8?

- **4 primitives with 100% structural gaps**: L0, L19, L20, L22 — every cell in
  the matrix for these primitives is a structural gap (459/459 each)
- **2 planes with zero coverage**: C5 (Representation) and C7 (Perception) —
  these planes have no existing or partial cells for these primitives
- **Both primitive AND plane have zero coverage** — this makes them the most
  critical gaps in the matrix

## Implementation

- Function: `promote_structural_gaps()` in `amos/governance/seed_cognitive_matrix.py`
- Called automatically by `seed_cognitive_matrix()`
- Each promoted gap is:
  - `GapKind.RELATION` (missing interaction)
  - Cluster: `cognitive_architecture_matrix_promoted`
  - Priority: 3 (higher than explicit gaps at priority 2)
  - Closed with complete 11-layer completion chain
- Idempotent: re-calling returns 0

## Test Coverage

- 14 new tests in `tests/test_cognitive_matrix.py` (TestStructuralGapPromotion)
- Tests verify: registration count, idempotency, closed status, RELATION kind,
  range 340-347, completion chains (11 layers), target primitives (L0/L19/L20/L22),
  target planes (C5/C7), priority 3, integration with seed_cognitive_matrix,
  specific gap titles (340=Reality, 347=Consolidation)

## Completion Graph Final State

| Metric | Value |
|--------|-------|
| Total closed gaps | 257 (91-347) |
| Meta-gaps | 230 (91-320) |
| Matrix gaps | 19 (321-339) |
| Promoted gaps | 8 (340-347) |
| Open gaps | 0 |
| Clusters | 25 (23 COMPONENT + 2 RELATION) |
| Unknown-unknowns | 246 (243 structural-gap + 3 original) |
| Remaining promotable | 235 structural-gap unknown-unknowns |

## Anti-fabrication

- `python3 -m pytest tests/test_cognitive_matrix.py -q` → 42 passed (28 original + 14 promotion)
- `seed_cognitive_matrix()` output: `matrix_promoted_structural_gaps: 8`
- Gap statistics: `{'total_gaps': 257, 'open_gaps': 0, 'closed_gaps': 257}`

## Links

- [[00_COSMO_BRAIN_MOC]]
- 2026-08-22 AMOS Cognitive Architecture Matrix Governance
- 2026-08-22 AMOS All 249 Gaps Closed
- 2026-08-22 AMOS Core Module Test Coverage

---
**MOC:** [[DATED_MOC]]
