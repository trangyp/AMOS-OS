---
title: AMOS Gap Registry Test Suite
created: '2026-08-23'
origin: Hermes ↔ Cosmo Brain
origin_architect: Trang Phan
type: note
source: 11_KNOWLEDGE/dated
tags:
- cosmo
- amos
- canon-group/tech-ai
- rscf/claim
- rscf/state/observation
- topic/gap-registry
- topic/testing
- topic/python
- dated
- dated/2026-08-23
- canon/knowledge
status: complete
provenance: OBSERVATION
confidence: HIGH
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: temporal_log
---


# AMOS Gap Registry Test Suite

> Epistemic class: OBSERVATION
> Conclusion label: `HIGH` — 81 pytest tests + 29 self-tests = 110 total, all passing.
> Governing law: `integrity > completeness > fluency > speed > token savings`.

## Overview

Comprehensive pytest test suite for `AMOS_GapRegistry.py` (914 lines) — Gap Discovery Engine & Unknown-Unknown Registry. 63 tests across 8 test classes, covering all enums, dataclasses, registry operations, and 6 discovery modes.

## Source

- **Module**: `cosmo-brain/AMOS_GapRegistry.py` (914 lines, 15 self-tests)
- **Test file**: `cosmo-brain/AMOS_OS_KERNEL/tests/test_gap_registry.py` (552 lines, 63 pytest tests)
- **Total**: 78 tests (63 pytest + 15 self-tests)

## Test Classes

| Class | Tests | Description |
|-------|-------|-------------|
| `TestUncertaintyClass` | 4 | Enum values, member count |
| `TestImpactLevel` | 3 | Enum values, ordering |
| `TestInvestigationStatus` | 3 | Enum values, member count |
| `TestDiscoveryMode` | 3 | 6 discovery modes, values |
| `TestCompletenessLevel` | 4 | L0-L5 levels, ordering |
| `TestCompletenessClaim` | 7 | 10-link chain, serialization, is_complete_for_scope |
| `TestGapEntry` | 5 | Construction, defaults, serialization, custom values |
| `TestGapRegistry` | 17 | Pre-population (11 gaps), filtering, summary, JSON, add |
| `TestGapDiscoveryEngine` | 17 | All 6 discovery modes, run_all_discovery, edge cases |

## Key Test Coverage

### Enums (17 tests)
- All 5 enums: `UncertaintyClass` (3), `ImpactLevel` (4), `InvestigationStatus` (4), `DiscoveryMode` (6), `CompletenessLevel` (6)
- Value verification, member count, ordering

### CompletenessClaim (7 tests)
- Default construction with L0_UNVERIFIED
- Full construction with all 10 links
- `is_complete_for_scope()` true only at L5
- `to_dict()` with 14 fields, level as int

### GapEntry (5 tests)
- Default construction with KNOWN_GAP, NOT_STARTED
- `to_dict()` with 12 fields, enum values as strings
- Custom values with UNKNOWN_UNKNOWN, IN_PROGRESS

### GapRegistry (17 tests)
- Pre-populated with 11 gaps (3 BRAIN_CORE, 3 OMNI_KERNEL, 3 OMNIVERSE_BRAIN, 2 GAP_MANAGEMENT)
- Unique gap IDs
- 3 CRITICAL gaps (GAP-BRAIN-001, GAP-OMNI-001, GAP-OMNIVERSE-001)
- 1 PARTIALLY_COVERED gap (GAP-OMNIVERSE-003)
- Coverage summary with 6 components, totals, discovery mode counts
- JSON serialization with all gaps and summary
- Add gap and completeness claim

### GapDiscoveryEngine (17 tests)
- **Structural**: Finds unconsumed interfaces, no candidates when all consumed
- **Failure-driven**: Maps root cause with "missing" keyword, no candidates without
- **Boundary-driven**: Scope expansion triggers gap, same scope doesn't
- **Compliance-driven**: NOT_COVERED→HIGH, PARTIALLY_COVERED→MEDIUM, COVERED excluded
- **Contradiction-driven**: Missing mechanism triggers gap, no info doesn't
- **Temporal**: VERIFIED_INVALID→HIGH, NOT_VERIFIED→MEDIUM, VERIFIED_STILL_VALID excluded
- **run_all_discovery**: All 6 modes, partial modes, empty input
- **new_candidates**: Cleared on each call

## Running

```bash
cd cosmo-brain/AMOS_OS_KERNEL
python -m pytest tests/test_gap_registry.py -v
# Expected: 63 passed

cd cosmo-brain
python AMOS_GapRegistry.py
# Expected: 15/15 self-tests passed
```

## Module Architecture

```
AMOS_GapRegistry.py (914 lines)
├── Enums
│   ├── UncertaintyClass (KNOWN_GAP, UNKNOWN_UNKNOWN, UNKNOWABLE)
│   ├── ImpactLevel (CRITICAL, HIGH, MEDIUM, LOW)
│   ├── InvestigationStatus (NOT_STARTED, IN_PROGRESS, BLOCKED, RESOLVED)
│   ├── DiscoveryMode (STRUCTURAL, FAILURE_DRIVEN, COMPLIANCE_DRIVEN, BOUNDARY_DRIVEN, CONTRADICTION_DRIVEN, TEMPORAL)
│   └── CompletenessLevel (L0-L5)
├── CompletenessClaim (10-link chain: Requirement→...→GovernanceOwner)
├── GapEntry (12 fields: gap_id, component, description, coverage_status, impact, ...)
├── GapDiscoveryEngine (6 discovery modes + run_all_discovery)
├── GapRegistry (11 pre-populated gaps, filtering, summary, JSON)
└── _self_test() (15 self-tests)
```

## Pre-populated Gaps (11)

| ID | Component | Impact | Description |
|----|-----------|--------|-------------|
| GAP-BRAIN-001 | BRAIN_CORE | CRITICAL | No UBI domain engines |
| GAP-BRAIN-002 | BRAIN_CORE | HIGH | No C01-C12 domain cognition engines |
| GAP-BRAIN-003 | BRAIN_CORE | HIGH | No automation/code/factory engines |
| GAP-OMNI-001 | OMNI_KERNEL | CRITICAL | No omni kernel with 33 meta-kernels |
| GAP-OMNI-002 | OMNI_KERNEL | HIGH | No dynamic governance routing |
| GAP-OMNI-003 | OMNI_KERNEL | MEDIUM | No typed graph integration matrix |
| GAP-OMNIVERSE-001 | OMNIVERSE_BRAIN | CRITICAL | No world model |
| GAP-OMNIVERSE-002 | OMNIVERSE_BRAIN | HIGH | No agent fabrication layer |
| GAP-OMNIVERSE-003 | OMNIVERSE_BRAIN | HIGH | No knowledge ceiling & gap engine (PARTIALLY_COVERED) |
| GAP-MGMT-001 | GAP_MANAGEMENT | MEDIUM | No formal gap discovery engine |
| GAP-MGMT-002 | GAP_MANAGEMENT | MEDIUM | No unknown-unknown registry |

## Test Count Impact

- **Python kernel**: 1934 → 1997 (+63)
- **Total verified**: 3638 → 3701
- **Grand total**: 3997 → 4060

## Links

- [[00_COSMO_BRAIN_MOC]]
- 2026-08-23 AMOS Kafka Brain Buffer Test Suite
- 2026-08-23 AMOS TypeScript Type-Guards Safety-Filter Meta-Logic Tests

---
**MOC:** [[DATED_MOC]]
