---
title: "AMOS Longevity Reproducibility Archival"
created: "2026-08-22"
type: note
source: 11_KNOWLEDGE/dated
tags: [canon-group/human-system, canon/framework, rscf/claim, rscf/provenance, rscf/state/observation, topic/amos-longevity-reproducibility, dated, dated/2026-08-22]
status: "living"
provenance: "MODEL"
confidence: "VERIFIED"
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: temporal_log
---


# AMOS Longevity, Reproducibility & Archival (Gaps 291-300)

> Epistemic class: MODEL (code artifact + test verification).
> Related: 2026-08-22 AMOS Governance Architecture Decommissioning · 2026-08-22 AMOS Fairness Ethics Externalities · amos-completion-graph-workflow

## Summary

Closed gaps 291-300 by implementing the **Longevity, Reproducibility & Archival**
governance module (`amos/governance/longevity_reproducibility.py`).
This is the 23rd governance gate in `AmosKernel.run()`, evaluated post-execution.

The user pre-implemented the module, types, and store methods. I added:
- `has_high_energy()` method to `EnergyEnvironmentalManager` (gap 297)
- `has_no_doi()` method to `ResearchArtifactManager` (gap 298)
- Gates for gaps 297 and 298 in the governor (were missing)
- Kernel wiring, exports, tests, seeder update, and learning persistence

## 10 Subsystems

| Gap | Subsystem | Class | Purpose |
|-----|-----------|-------|---------|
| 291 | Archival format | `ArchivalFormatManager` | Archival format management |
| 292 | Historical reproducibility | `HistoricalReproducibilityManager` | Historical reproducibility |
| 293 | Provider disappearance | `ProviderDisappearanceManager` | Provider disappearance plan |
| 294 | Hardware abstraction | `HardwareAbstractionManager` | Hardware abstraction |
| 295 | Numerical reproducibility | `NumericalReproducibilityManager` | Numerical reproducibility |
| 296 | Performance portability | `PerformancePortabilityManager` | Performance portability |
| 297 | Energy/environmental | `EnergyEnvironmentalManager` | Energy/environmental accounting |
| 298 | Research artifacts | `ResearchArtifactManager` | Research artifact format |
| 299 | Negative experiments | `NegativeExperimentManager` | Negative experiment registry |
| 300 | External scientific closure | `ExternalScientificClosureManager` | External scientific closure |

## Gate Evaluation

`LongevityReproducibilityGovernor.evaluate_post()` returns 10 gate results:
- `longevity-291-obsolete-format` (CONDITIONAL/PASS)
- `longevity-292-non-reproducible` (CONDITIONAL/PASS)
- `longevity-293-provider-disappeared` (CONDITIONAL/PASS)
- `longevity-294-non-portable` (CONDITIONAL/PASS)
- `longevity-295-non-deterministic` (CONDITIONAL/PASS)
- `longevity-296-performance-non-portable` (CONDITIONAL/PASS)
- `longevity-297-high-energy` (CONDITIONAL/PASS) — added by me
- `longevity-298-no-doi` (CONDITIONAL/PASS) — added by me
- `longevity-299-unpublished-negative` (CONDITIONAL/PASS)
- `longevity-300-pending-closure` (CONDITIONAL/PASS)

## Key Semantics

1. **Archival format status**: STABLE, DEPRECATED, OBSOLETE, MIGRATING
2. **Reproducibility level**: FULLY_REPRODUCIBLE, MOSTLY_REPRODUCIBLE, PARTIALLY_REPRODUCIBLE, NON_REPRODUCIBLE
3. **Provider status**: ACTIVE, END_OF_LIFE, DISAPPEARED, REPLACED
4. **API pattern**: Some subsystems use `register()`, others use `record()`
5. **Governor attributes**: `archival`, `reproducibility`, `provider`, `hardware`, `numerical`, `portability`, `energy`, `artifacts`, `negative`, `closure`
6. **Kernel attribute**: `longevity_governor`
7. **Empty state**: All gates return PASS on empty state
8. **All gates are CONDITIONAL** (no FAIL) — longevity issues are advisory, not blocking

## Implementation Chain

- **Types**: `amos/core/types.py` — 10 dataclasses + 3 enums (user-created)
- **Schema**: `amos/state/store.py` — 10 tables + 10 put/list method pairs (user-created)
- **Module**: `amos/governance/longevity_reproducibility.py` — 10 subsystems + governor (user-created, I added 2 has_* methods + 2 gates)
- **Kernel**: `amos/kernel.py` — import, instantiation, gate evaluation (I added)
- **Exports**: `amos/__init__.py` — all types + `LongevityReproducibilityGovernor` (I added)
- **Tests**: `tests/test_longevity_reproducibility.py` — 31 tests (I created)
- **Seeder**: `amos/governance/seed_completion.py` — gaps 291-300 in CLOSED_CLUSTERS (I moved)

## Completion Graph Impact

- **Closed gaps**: 200 → 210 (gaps 291-300 = 10 gaps closed)
- **Open gaps**: 30 → 20 (but user also closed assurance_debt 301-320, so 230 closed, 0 open)
- **Total tests**: 1405 → 1505 (31 new tests for longevity + user's assurance_debt tests)
- **All 1505 tests pass**

## Lessons Learned

1. **User pre-implemented module**: The user created the module, types, and store methods before I started. I only needed to add missing gates, wire into kernel, add exports, write tests, and update seeder.
2. **Missing gates**: The user's governor was missing gates for gaps 297 (energy) and 298 (artifacts). I added `has_high_energy()` and `has_no_doi()` methods plus the corresponding gates.
3. **Mixed API**: Some subsystems use `register()` (archival, provider, hardware, artifacts, negative, closure), others use `record()` (reproducibility, numerical, portability, energy).
4. **All CONDITIONAL gates**: Unlike previous clusters, all longevity gates are CONDITIONAL (no FAIL). Longevity issues are advisory.
5. **Pre-existing assurance_debt bugs**: The user's assurance_debt module had SQL column count mismatches (8 `?` for 7-column tables) and a gate count mismatch (17 gates vs expected 15). I fixed both.
6. **All 230 gaps now closed**: With the user's assurance_debt implementation, all 230 meta-gaps (91-320) are now closed. The Completion Graph is complete.

---
**Links:** [[DATED_MOC]] | [[KNOWLEDGE_MOC]]
