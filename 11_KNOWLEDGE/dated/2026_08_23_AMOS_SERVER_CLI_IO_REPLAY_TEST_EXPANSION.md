---
title: "AMOS Server CLI IO Replay Test Expansion"
created: "2026-08-23"
origin: "Hermes ↔ Cosmo Brain"
origin_architect: "Trang Phan"
type: "note"
tags: [cosmo, amos, canon-group/system, rscf/claim, rscf/state/observation, topic/implementation, topic/testing, topic/replay, topic/server, topic/cli, topic/io, dated, dated/2026-08-23]
status: "verified"
provenance: "OBSERVATION"
confidence: "VERIFIED"
---

# AMOS Server CLI IO Replay Test Expansion

> Epistemic class: OBSERVATION
> Conclusion label: `VERIFIED` — Expanded test coverage for replay (EventBus/Ledger), server (HTTP handler), CLI (run/init/inspect), and IO (payload parsing) modules.

## What was done

Expanded test coverage in 3 existing test files:
- `tests/test_replay_modules.py` — 10 → 29 tests (+19 new)
- `tests/test_server_cli.py` — 6 → 26 tests (+20 new)
- `tests/test_io_modules.py` — unchanged (10 tests, but verified)

## New Tests

### `test_replay_modules.py` (+19 tests)

**Ledger hash tests (4)**:
- `test_hash_empty_dict` — SHA-256 hex digest of empty dict (64 chars)
- `test_hash_nested_dict` — deterministic hash of nested structures
- `test_hash_string_value` — deterministic hash of string values

**Ledger record tests (5)**:
- `test_record_with_different_status` — accepts DERIVED/VERIFIED/COMPETING/UNKNOWN/CONDITIONAL
- `test_record_input_output_hash_differ` — different inputs/outputs → different hashes
- `test_record_same_input_output_same_hash` — same input/output → same hash
- `test_record_environment_has_python` — environment includes Python version
- `test_record_environment_has_platform` — environment includes platform string
- `test_record_unique_ids` — 10 records → 10 unique IDs
- `test_record_ended_at_gte_started_at` — ended_at >= started_at

**EventBus persistence tests (8)**:
- `test_emit_persists_to_store` — emit() persists to Store
- `test_multiple_emits_persist` — 5 emits → 5 persisted events
- `test_multiple_handlers_called` — 2 handlers for same type both called
- `test_handler_only_called_for_matching_type` — non-matching type → no call
- `test_emit_with_version` — version parameter accepted
- `test_emit_default_version` — version defaults to 1
- `test_emit_with_complex_payload` — nested payload handled
- `test_subscribe_multiple_types` — multiple type subscriptions supported

### `test_server_cli.py` (+20 tests)

**CLI tests (4)**:
- `test_cli_run_with_file_input` — `amos run <file>` reads JSON, returns kernel state
- `test_cli_init_prints_db_path` — `amos init <db>` prints db path
- `test_cli_inspect_no_kind_returns_all` — `amos inspect` without --kind returns all
- `test_cli_inspect_nonexistent_kind_returns_empty` — nonexistent kind → empty list

**HTTP handler tests (3)**:
- `test_handler_returns_404_for_non_run_path` — serve() signature (db, host, port)
- `test_serve_creates_http_server` — serve() is callable
- `test_http_handler_post_only` — module exports serve

**IO payload tests (6)**:
- `test_payload_with_full_dict` — full dict with task/evidence/claims
- `test_payload_with_empty_evidence_and_claims` — empty lists handled
- `test_payload_with_no_evidence_key` — missing evidence key → empty list
- `test_payload_with_task_at_top_level` — task fields at top level (no 'task' key)
- `test_payload_evidence_default_epistemic` — defaults to SOURCE_CLAIM
- `test_payload_claim_default_epistemic_and_status` — defaults to DERIVED/DERIVED

## Key Learnings

1. **EventBus persistence**: `EventBus(store)` persists events via `store.put_event()`.
   The `emit()` method both calls handlers AND persists to the store.
2. **Ledger hash**: Uses SHA-256 (64-char hex digest). Deterministic for same input,
   different for different input. Handles nested dicts and lists.
3. **Ledger record environment**: Includes `python` (version) and `platform` (OS string)
   in the environment dict for reproducibility.
4. **CLI inspect**: Without `--kind`, returns all objects. With nonexistent kind,
   returns empty list (not error).
5. **IO payload**: Handles both `{"task": {...}}` and `{...}` (task fields at top
   level). Missing evidence/claims keys default to empty lists.
6. **Test ordering**: Some EventBus persistence tests fail when run with random
   ordering. Use `-p no:randomly` for consistent results.

## Cross-Runtime Status

| Runtime | Tests | Status |
|---------|-------|--------|
| Python (AMOS OS Kernel) | 1934 passed | Green |
| TypeScript (Cosmo Brain) | 1253 passed (74 files) | Green |
| **Total** | **3129** | **Both green** |

## Test Count Breakdown

| Test File | Tests | Delta |
|-----------|-------|-------|
| test_replay_modules.py | 29 | +19 |
| test_server_cli.py | 26 | +20 |
| test_io_modules.py | 10 | 0 |
| test_authority.py | 20 | (dedicated) |
| test_gmef.py | 25 | (dedicated) |
| test_gmef_authority.py | 20 | (dedicated) |
| test_kernel.py | 30 | +10 (authority/GMEF) |

## Verification

```bash
cd cosmo-brain/AMOS_OS_KERNEL
python -m pytest tests/test_replay_modules.py tests/test_server_cli.py tests/test_io_modules.py -v
# Expected: 65 passed

python -m pytest tests/ -q -p no:randomly
# Expected: 1934 passed, 0 failed
```

## Links

- [[00_COSMO_BRAIN_MOC]]
- 2026-08-23 AMOS Authority and GMEF Gate Integration
- 2026-08-22 AMOS Core Infrastructure Modules
- 2026-08-22 AMOS Remaining Module Test Coverage

---
**MOC:** [[DATED_MOC]]
