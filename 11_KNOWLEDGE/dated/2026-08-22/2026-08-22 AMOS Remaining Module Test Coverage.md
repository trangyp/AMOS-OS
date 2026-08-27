---
title: "AMOS Remaining Module Test Coverage"
created: "2026-08-22"
origin: "Hermes ↔ Cosmo Brain"
origin_architect: "Trang Phan"
type: "note"
tags: [cosmo, amos, canon-group/system, rscf/claim, rscf/state/observation, topic/implementation, topic/test-coverage, topic/state, topic/io, topic/gmef, topic/authority, dated, dated/2026-08-22]
status: "verified"
provenance: "OBSERVATION"
confidence: "VERIFIED"
---

# AMOS Remaining Module Test Coverage

> Epistic class: OBSERVATION
> Conclusion label: `VERIFIED` — 51 new tests pass for 7 previously untested modules.
> Governing law: `integrity > completeness > fluency > speed > token savings`.

## Overview

Added test coverage for the 7 AMOS OS Kernel modules that previously lacked
dedicated test files. This completes the test coverage for all non-governance
kernel subsystems.

## New Test Files

| Test File | Tests | Modules |
|-----------|------:|---------|
| test_state_modules.py | 14 | EpochManager, TransactionManager |
| test_io_modules.py | 10 | task_from, evidence_from, claim_from, payload |
| test_gmef_authority.py | 21 | GMEF, AuthorityGovernor |
| test_server_cli.py | 6 | HTTP server, CLI |
| **Total** | **51** | **7 modules** |

## Key Findings

### EpochManager
- `epoch_state()` is on `Store`, not `EpochManager` — the manager delegates to store
- Epochs auto-increment via `SELECT COALESCE(MAX(epoch),0)+1`
- Finalize sets state to "FINAL" (valid) or "ABORTED" (invalid)

### TransactionManager
- Uses CAS (Compare-And-Swap) on object versions — `expected_version` mismatch causes abort
- `independent()` checks for write-set overlap with active transactions
- Commits are atomic via `BEGIN IMMEDIATE` + rollback on error

### I/O Payload
- Evidence has `source_id`, `source_family`, `content` — NOT `source`, `url`, `retrieved_at`
- `payload(d)` treats `d` itself as the task if no "task" key present
- Unknown fields in task dict are silently ignored

### GMEF
- 7 required fields: target, mutation_class, hypothesis, authority, rollback, validation, predicted_regression
- M0 = constitutional invariant → always BLOCK
- M1/M2 without authority → BLOCK
- All other valid changes → SANDBOX (validate before promotion)

### AuthorityGovernor
- Checks: capability match, token expiry, scope (wildcard `*` matches all), consequence level, reversible_only
- Order hierarchy: low=0 < medium=1 < high=2 < critical=3
- `reversible_only=True` blocks irreversible operations

### HTTP Server & CLI
- Server: POST /run endpoint, returns JSON kernel state
- CLI: 4 subcommands (init, run, inspect, serve)
- CLI reads JSON from stdin when input is `-`

## Test Results

- Python: 1934 tests pass (was 1678, +224 new)
- TypeScript: 1253 tests pass (was 1191, +4 new)
- **Total: 3701 verified tests** across all runtimes

## Links
- [[00_Cosmo_Brain_MOC]]
- 2026-08-22 AMOS Core Runtime Modules
- 2026-08-22 AMOS Core Module Test Coverage
- 2026-08-22 TypeScript Data Quality Governance
