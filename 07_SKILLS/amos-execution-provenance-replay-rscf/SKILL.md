---
title: SKILL
type: skill
name: amos-execution-provenance-replay-rscf
description: Execution Provenance Replay — security and safety capability. Use when security analysis, safety verification, or adversarial defense. Use when amos-security-safety-master routes to this specialized capability.
parent_skill: amos-security-safety-master
domain: security
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-execution-provenance-replay-rscf]
---


# Execution Provenance Replay Rscf

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-security-safety-master`
- **Domain**: security
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Security and trust engine for Execution Provenance Replay Rscf

## When to Use

- When detecting adversarial activity: attacks, probes, manipulation
- When quantifying adversarial entropy and attack surface
- When governing principal-trust relationships: delegation, revocation
- When monitoring distributed attack composition: multi-stage threats
- When the parent skill (`amos-security-safety-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **execution_provenance.detect_adversary**: Detect adversarial activity: attacks, probes, and manipulation attempts
- **execution_provenance.quantify_entropy**: Quantify adversarial entropy: uncertainty, information leakage, and attack surface
- **execution_provenance.govern_trust**: Govern principal-trust relationships: delegation, revocation, and audit
- **execution_provenance.monitor_attack**: Monitor distributed attack composition: multi-stage, multi-vector threats
- **execution_provenance.replay_provenance**: Replay execution provenance: trace and verify every action for integrity
- **execution_provenance.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **execution_provenance.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **execution_provenance.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Content

### Source 1: v3.9 — Persistent Incremental Provenance Runtime

> Path: `misc/V/V3_9_PERSISTENT_PROVENANCE.md` | Size: 1469 chars | Match score: 12 | content_hash: 34abc31c30da52b7

# v3.9 — Persistent Incremental Provenance Runtime

## Focus
- persistent live graph
- localized cycle checks
- dependency-aware invalidation
- versioned hashes
- copy-on-write updates

## Markdown brain adaptation
Use persistent graph + dependency-aware selective invalidation.

## Historical gap
Concurrent overlapping writes remained execution-order dependent; no MVCC/CAS snapshot semantics.

## Benchmark boundary
> **Reference**: See `references/execution_provenance_spec.md` (content_hash: c29702f9eab920ac) for the JSON specification.

Benchmark results are preserved only within their tested operationalization and are not universal guarantees.

---

---

### Source 2: AMOS Server CLI IO Replay Test Expansion

> Path: `dated/2026-08-23/2026-08-23 AMOS Server CLI IO Replay Test Expansion.md` | Size: 5307 chars | Match score: 10 | content_hash: ae8cdcb9b053b9cc

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
- `test_hash_empty_dict` — SHA-256 hex digest of empty dict (64 chars)
- `test_hash_nested_dict` — deterministic hash of nested structures
- `test_hash_string_value` — deterministic hash of string values

- `test_record_with_different_status` — accepts DERIVED/VERIFIED/COMPETING/UNKNOWN/CONDITIONAL
- `test_record_input_output_hash_differ` — different inputs/outputs → different hashes
- `test_record_same_input_output_same_hash` — same input/output → same hash
- `test_record_environment_has_python` — environment includes Python version
- `test_record_environment_has_platform` — environment includes platform string
- `test_record_unique_ids` — 10 records → 10 unique IDs
- `test_record_ended_at_gte_started_at` — ended_at >= started_at
- `test_emit_persists_to_store` — emit() persists to Store
- `test_multiple_emits_persist` — 5 emits → 5 persisted events
- `test_multiple_handlers_called` — 2 handlers for same type both called
- `test_handler_only_called_for_matching_type` — non-matching type → no call
- `test_e