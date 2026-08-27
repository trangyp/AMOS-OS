---
title: "data_quality cluster closed (gaps 239-249)"
created: "2026-08-22"
origin: "Hermes ↔ Cosmo Brain"
origin_architect: "Trang Phan"
type: note
source: 11_KNOWLEDGE/dated
tags: [cosmo, amos, canon-group/system, rscf/claim, rscf/state/observation, topic/implementation, topic/completion-graph, dated, dated/2026-08-22, canon/knowledge]
status: "verified"
provenance: "OBSERVATION"
confidence: "VERIFIED"
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: temporal_log
---


# data_quality cluster closed — gaps 239-249

> Epistic class: OBSERVATION
> Conclusion label: `VERIFIED` — implementation, tests, and seed counts all green.
> Governing law: `integrity > completeness > fluency > speed > token savings`.

## What was implemented

The `data_quality` cluster (gaps 239-249) was implemented in the AMOS OS Kernel:

```
cosmo-brain/AMOS_OS_KERNEL/
├── amos/state/store.py                      (added put/list methods for 11 tables)
├── amos/governance/data_quality.py          (11 subsystems + governor)
├── tests/test_data_quality.py               (11 gap-level test classes)
├── amos/kernel.py                           (DataQualityGovernor wired)
├── amos/governance/seed_completion.py       (moved to CLOSED_CLUSTERS)
└── tests/test_completion.py                 (seed counts updated)
```

### Subsystems

| Gap | Subsystem | Responsibility |
| ---: | --- | --- |
| 239 | `RetentionPolicyManager` | Data retention policies by data_type and action |
| 240 | `DataQualityGate` | Data quality level (excellent/good/fair/poor/unusable) and score |
| 241 | `UnitRegistry` | Unit registry with name, symbol, dimension, conversion factor |
| 242 | `CoordinateSystemRegistry` | Coordinate system registry (WGS84, Cartesian, etc.) |
| 243 | `SchemaEvolutionTracker` | Schema migrations: additive, breaking, deprecation |
| 244 | `MissingDataManager` | Missing data pattern (MCAR/MAR/MNAR), fraction, imputation |
| 245 | `SensorReliabilityTracker` | Sensor reliability score, failure rate, calibration |
| 246 | `MeasurementUncertaintyTracker` | Value, uncertainty, confidence interval, source |
| 247 | `ConstructValidityTracker` | Construct validity score, type, threats |
| 248 | `GoodhartMonitor` | Goodhart's law status, gaming evidence, original goal |
| 249 | `MetricVersionTracker` | Metric versions, deprecation, supersession |

### Kernel gate order

`DataQualityGovernor.evaluate_post()` now runs in `AmosKernel.run()` after `ResourceGovernanceGovernor`, returning 11 gate results:

- `data-quality-239-retention-unbounded`
- `data-quality-240-quality-unusable`
- `data-quality-241-unit-unregistered`
- `data-quality-242-coordinate-unregistered`
- `data-quality-243-schema-breaking-change`
- `data-quality-244-missing-data-unchecked`
- `data-quality-245-sensor-unreliable`
- `data-quality-246-measurement-uncertain`
- `data-quality-247-construct-invalid`
- `data-quality-248-goodhart-gaming`
- `data-quality-249-metric-deprecated`

## Verification

```bash
cd cosmo-brain/AMOS_OS_KERNEL
python3 -m pytest tests/ -q
```

Result: **1049 passed in 14.10s, 0 failures**.

The `test_completion.py` seed counts updated to:
- `closed_gaps_seeded`: 159
- `open_gaps_seeded`: 71
- `total_gaps`: 230

`test_seeded_closed_chains_are_complete` now checks gap 249 in addition to previous closed anchors.

## Why this matters for the completion jump

`data_quality` is the second rung in Phase 1 of the roadmap. Without data-quality gates, the AMOS OS Kernel cannot distinguish usable evidence from unusable evidence, track metric versions, or detect Goodhart gaming. Closing this cluster makes the persistent state model evidence-grade.

## Learned

- The data-quality cluster had types and schema already in `core/types.py` and `state/store.py`, but the `Store` class was missing the `put_*` / `list_*` methods. Adding those was the critical missing piece; the module and tests could then follow the established pattern.
- The `Store` method naming convention uses plural `list_*_records` and singular `put_*_record`; keeping this consistent made the governor module straightforward.
- Kernel wiring now runs: Principal → Autonomy → AIBOM → Semantic → AgentOps → Eval → Scientific → Ontology → Completion → Trust → Canon → Consensus → Adversarial → Uncertainty → Decision → Resource → **Data Quality**.

## Anti-fabrication

- Source: `python3 -m pytest tests/ -q` run 2026-08-22.
- Verification: 1049 passed, 0 failed.
- No new conceptual framework was invented. All 11 records map directly to pre-defined `DataQuality*` dataclasses in `amos/core/types.py`.

## Links
- [[00_COSMO_BRAIN_MOC]]
- 2026-08-22 AMOS System Completion Baseline
- 2026-08-22 AMOS System Completion Audit
- 2026-08-22 AMOS System Completion Roadmap
- 2026-08-22 resource_governance cluster closed

---
**MOC:** [[DATED_MOC]]
