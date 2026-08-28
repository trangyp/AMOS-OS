---
title: AMOS TypeScript Data Quality Governance
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
- topic/governance
- topic/data-quality
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


# TypeScript Data Quality Governance

> Epistic class: OBSERVATION
> Conclusion label: `VERIFIED` — 49 TypeScript tests pass for the data quality governance module.
> Governing law: `integrity > completeness > fluency > speed > token savings`.

## Module

Implemented TypeScript Data Quality Governance module for the Cosmo Brain,
mirroring the Python AMOS OS Kernel `data_quality.py` (gaps 239-249).

**Location**: `cosmo-brain/governance/data-quality/index.ts`
**Tests**: `cosmo-brain/tests/unit/governance-data-quality.test.ts` (49 tests)

## 11 Subsystems

| Gap | Subsystem | Description |
|-----|-----------|-------------|
| 239 | Retention Policy Manager | Data retention policies with expiry |
| 240 | Data Quality Gate | Quality level tracking (high/medium/low/unusable) |
| 241 | Unit Registry | Canonical measurement units with conversion |
| 242 | Coordinate System Registry | Spatial reference frames |
| 243 | Schema Evolution Tracker | Breaking/compatible/additive change tracking |
| 244 | Missing Data Manager | MCAR/MAR/MNAR pattern detection |
| 245 | Sensor Reliability Tracker | Sensor degradation detection |
| 246 | Measurement Uncertainty | Type A/B uncertainty tracking |
| 247 | Construct Validity | Content/construct/criterion validity scores |
| 248 | Goodhart Monitor | Metric gaming detection |
| 249 | Metric Version Tracker | Metric lineage and supersession |

## Gate Semantics

- **FAIL**: CRITICAL_MISSING_DATA, BREAKING_SCHEMA_CHANGE
- **CONDITIONAL**: LOW_QUALITY_DATA, DEGRADED_SENSORS, HIGH_UNCERTAINTY, LOW_CONSTRUCT_VALIDITY, GOODHART_GAMING

## Cross-Runtime Parity

This TypeScript module mirrors the Python `amos/governance/data_quality.py`.
Both runtimes now have data quality governance coverage.

## Test Results

- TypeScript: 1191 tests pass (was 1142, +49 new)
- Python: 1934 tests pass (all modules with full test coverage)
- **Total: 3701 verified tests** across all runtimes

## Links
- [[00_COSMO_BRAIN_MOC]]
- 2026-08-22 AMOS All 249 Gaps Closed
- Python equivalent: `AMOS_OS_KERNEL/amos/governance/data_quality.py`

---
**MOC:** [[DATED_MOC]]
