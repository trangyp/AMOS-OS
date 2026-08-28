---
title: SKILL — Amos Execution Provenance Replay Rscf
type: skill
source: 07_SKILLS/amos-execution-provenance-replay-rscf
name: amos-execution-provenance-replay-rscf
description: Execution Provenance Replay — security and safety capability. Use when security analysis, safety verification, or adversarial defense. Use when amos-security-safety-master routes to this specialized capability. Do not use for generic tasks outside security domain.
parent_skill: amos-security-safety-master
domain: security
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/security-safety
- rscf/source_claim
- hml/h
- epistemic/source_claim
- amos_os
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
rscf_state: SOURCE_CLAIM
hml_level: H
gmef_gates:
- L0_integrity
- L1_epistemic
- L2_provenance
- L5_scope
- L7_authority
- L23_mvcc_cas
collapse_class: fail_closed
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L4
- L5
- L7
- L16
- L17
- L18
- L23
---

# Execution Provenance Replay Rscf

## Identity

Origin architect: **Trang Phan**. Domain: security. Parent: amos-security-safety-master. Epistemic class: SOURCE_CLAIM. H/M/L: H.
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

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-execution-provenance-replay-rscf_MOC]]

## Examples

- **Scenario**: When detecting adversarial activity: attacks, probes, manipulation
  - **Input**: A query matching this skill's domain (security)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When quantifying adversarial entropy and attack surface
  - **Input**: A query matching this skill's domain (security)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When governing principal-trust relationships: delegation, revocation
  - **Input**: A query matching this skill's domain (security)
  - **Output**: Structured result with epistemic labels and provenance


## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

## Anti-Patterns

- **Do not use** for tasks outside the security domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-security-safety-master` — routes to this skill when security specialization is needed
- **Peers**: Other skills in the `security` domain may be composed in sequence
- **Orchestrator**: The parent skill or `AMOS_HOME` orchestrates routing
- **Workflow**: Each skill has a corresponding workflow in `08_WORKFLOWS/`
- **Agent**: Each skill has a corresponding agent in `06_AGENTS/`


## Evaluation

### Success Criteria

- Output includes epistemic class label (SOURCE/DERIVED/AMOS_MODEL/EMPIRICAL)
- Output includes provenance reference to source evidence
- Output includes confidence ceiling (capped at 0.95 for DERIVED, 1.0 for SOURCE_CANON)
- Output includes gap flags for unresolved unknowns
- Output does not exceed declared scope

### Failure Modes

- **Overreach**: Output claims validity beyond its epistemic class
- **Scope creep**: Output addresses questions outside the declared domain
- **Provenance loss**: Output cannot trace back to source evidence
- **Confidence inflation**: Output confidence exceeds the weakest-premise ceiling


## Error Handling

- **On scope violation**: Reject the query and route back to parent skill
- **On missing evidence**: Flag as GAP and reduce confidence ceiling to 0.5
- **On contradiction**: Flag as CRITICAL_GAP and halt until resolved
- **On provenance loss**: Mark output as UNKNOWN and require human review
- **On drift**: Trigger drift alignment via `amos-ai-drift-alignment-governor`


## Do not use

- For generic security analysis outside the AMOS security framework
- To claim empirical validation of adversarial defense theories
- As a substitute for domain-specific security or safety evidence
- Outside security/safety domain reasoning

## References

- `references/execution_provenance_spec.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `[[amos-execution-provenance-replay-rscf_MOC]]` — skill Map of Content
- `amos-security-safety-master` — parent skill
- `[[amos-execution-provenance-replay-rscf-workflow]]` — corresponding workflow
- `amos-execution-provenance-replay-rscf-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-execution-provenance-replay-rscf
node_type: skill
path: 07_SKILLS/amos-execution-provenance-replay-rscf/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
