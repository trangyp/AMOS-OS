---
title: "AMOS Gap Discovery Engine — All 6 Modes Implemented"
created: "2026-08-23"
origin: "Hermes ↔ Cosmo Brain"
origin_architect: "Trang Phan"
type: "note"
tags: [cosmo, amos, canon-group/tech-ai, rscf/claim, rscf/state/observation, topic/gap-discovery, topic/llm-operator-pipeline, topic/implementation, dated, dated/2026-08-23]
status: "complete"
provenance: "OBSERVATION"
confidence: "HIGH"
---

# AMOS Gap Discovery Engine — All 6 Modes Implemented

> Epistemic class: OBSERVATION
> Conclusion label: `HIGH` — All 6 discovery modes now operational.
> Test results: 15/15 self-tests pass (was 11/11).
> Governing law: `integrity > completeness > fluency > speed > token savings`.

## Summary

Implemented the 3 remaining stub discovery modes in
`AMOS_GapRegistry.py`'s `GapDiscoveryEngine` class:
- **Compliance-driven**: diffs current capabilities against external requirements
- **Contradiction-driven**: maps detected conflicts to missing resolution mechanisms
- **Temporal**: re-verifies claims whose validity has expired

All 6 discovery modes are now operational. GAP-MGMT-001 coverage status
upgraded from NOT_COVERED to COVERED.

## What Was Done

### 3 New Discovery Methods

#### 1. `discover_compliance_driven(compliance_spec)`
- **Input**: compliance spec with standard name and requirements list
- **Each requirement**: id, description, component, current_coverage
- **Output**: gap candidates for NOT_COVERED and PARTIALLY_COVERED requirements
- **Impact**: HIGH for NOT_COVERED, MEDIUM for PARTIALLY_COVERED
- **Provenance**: `compliance_driven:{standard}`

#### 2. `discover_contradiction_driven(conflict)`
- **Input**: conflict dict with type, description, component, resolution_attempted, missing_mechanism
- **Output**: gap candidate for missing resolution mechanism
- **Impact**: from conflict severity (default MEDIUM)
- **Provenance**: `contradiction_driven:{conflict_type}`

#### 3. `discover_temporal(expiry_report)`
- **Input**: expiry report with expired_claims list
- **Each claim**: id, component, expired_at, original_claim, re_verification_status
- **Output**: gap candidates for NOT_VERIFIED and VERIFIED_INVALID claims
- **Impact**: HIGH for VERIFIED_INVALID, MEDIUM for NOT_VERIFIED
- **Provenance**: `temporal:validity_expiry`

### Updated `run_all_discovery()`
- Now accepts 6 optional parameters (one per discovery mode)
- Returns results dict with all 6 modes populated
- No more stub empty lists

### Gap Status Update
- **GAP-MGMT-001**: NOT_COVERED → COVERED (all 6 modes implemented)
- **GAP-MGMT-002**: still NOT_COVERED (unknown-unknown registry not implemented)
- **GAP_MANAGEMENT component**: NOT_COVERED → PARTIALLY_COVERED (1 of 2 gaps covered)

### Tests Added (4 new tests, 11 → 15 total)
- **Test 11**: Compliance-driven discovery finds 3 unmet requirements (from 4, 1 covered)
- **Test 12**: Contradiction-driven discovery maps conflict to missing mechanism
- **Test 13**: Temporal discovery finds 2 expired claims (from 3, 1 still valid)
- **Test 14**: `run_all_discovery` with all 6 modes produces 10 total candidates

## Test Results

| Metric | Before | After |
|--------|--------|-------|
| Discovery modes | 3 of 6 | **6 of 6** |
| Self-tests | 11/11 | **15/15** |
| GAP-MGMT-001 | NOT_COVERED | **COVERED** |
| GAP_MANAGEMENT | NOT_COVERED | **PARTIALLY_COVERED** |

## All Test Suites Status

| Suite | Tests | Status |
|-------|-------|--------|
| AMOS OS Kernel (Python) | 1934 passed | Green |
| Cognitive Substrate self-tests | 146/146 passed | Green |
| Cognitive Substrate slices | 125 passed | Green |
| TypeScript (vitest) | 1253 passed | Green |
| Kafka Brain Buffer (tsx) | 180/180 passed | Green |
| GapRegistry self-tests | **15/15 passed** | Green |
| LLM Operator Pipeline | 10/10 passed | Green |
| CognitiveState BrainModel | 10/10 passed | Green |
| BrainCortex | 71/71 passed | Green |
| INFRA_META_SCHEMA | 73/73 passed | Green |
| **Total verified** | **3638+** | **All green** |

## Architecture — 6 Discovery Modes

| Mode | Trigger | Method | Status |
|------|---------|--------|--------|
| Structural | New component added | Graph analysis: missing interfaces, orphan deps | ✅ Implemented |
| Failure-driven | Incident/bug | Root-cause to missing capability/interface/recovery | ✅ Implemented |
| Compliance-driven | Standard update | Diff against external requirements | ✅ **NEW** |
| Boundary-driven | Scope expansion | Enumerate new boundary conditions | ✅ Implemented |
| Contradiction-driven | Conflict detected | Map to missing resolution mechanism | ✅ **NEW** |
| Temporal | Validity expiry | Re-verify expired claims | ✅ **NEW** |

## Key Lessons

1. **Placeholder patterns**: When a module has placeholder methods returning
   empty lists, implementing them is straightforward — the interface is already
   defined, just needs the logic.

2. **Test-driven gap closure**: Each new discovery mode gets its own test that
   verifies the expected behavior with specific inputs and outputs.

3. **Coverage status upgrade**: When a gap is closed, update its
   `coverage_status` from NOT_COVERED to COVERED and reduce its impact.
   This propagates to the component-level coverage summary.

4. **Compliance-driven design**: The compliance spec format (standard +
   requirements list with coverage status) is reusable across any standard.

5. **Temporal validity**: Claims have a validity period. When they expire,
   they need re-verification. VERIFIED_INVALID claims are higher impact
   than NOT_VERIFIED because we know they're wrong.

## Links

- [[00_COSMO_BRAIN_MOC]]
- 2026-08-23 AMOS Kafka Brain Buffer Complete Fix
- 2026-08-22 AMOS Completion Graph All 249 Gaps Closed

---
**MOC:** [[DATED_MOC]]
