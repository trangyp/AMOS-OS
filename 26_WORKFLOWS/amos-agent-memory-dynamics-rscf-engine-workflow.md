---
title: amos-agent-memory-dynamics-rscf-engine-workflow
type: workflow
Skill: amos-agent-memory-dynamics-rscf-engine
Agent: amos-agent-memory-dynamics-rscf-engine-agent
Version: 2.0.0
domain: memory
origin_architect: Trang Phan
epistemic_class: AMOS_MODEL
---

# Workflow: AMOS Agent Memory Lifecycle

## Objective

Preserve persistent memory as governed historical evidence, not truth, current state, or authority.

## State machine

`INTAKE -> AUTHORITY_RESOLVED -> INTEGRITY_CHECKED -> ELIGIBILITY_RESOLVED -> EXECUTED -> RECORDED -> COMPLETE`

Failure exits: `REJECTED | QUARANTINED | UNKNOWN_GAP`.

Persistent memory states: `ACTIVE | QUARANTINED | SUPERSEDED | EXPIRED | TOMBSTONED`.

## Execution

1. Resolve operation, memory scope, provenance, temporal coordinates, and explicit capabilities.
2. Reject unauthorized reads/writes; read authority never implies mutation authority.
3. Verify stored content hashes and ledger continuity before consequential reuse.
4. Apply lifecycle eligibility plus event-valid and recorded-time constraints.
5. Execute exactly one bounded operation:
   - `ADMIT`: new provenance-bound `OBSERVATION`.
   - `REVISE`: new version + predecessor `SUPERSEDED`.
   - `QUARANTINE`: isolate conflict/contamination.
   - `EXPIRE`: stop normal retrieval while keeping lineage.
   - `TOMBSTONE`: terminate active use while keeping lineage.
   - `READ/HISTORY`: retrieve only.
   - `ASSEMBLE_CONTEXT`: construct bounded `OBSERVATION` context only.
6. Append a lifecycle event and preserve origin/version/predecessor lineage.
7. Return scope, provenance, state, temporal bounds, context eligibility, and unresolved gaps.

## Hard firewalls

- `MEMORY != KNOWLEDGE`
- `MEMORY != CURRENT_STATE`
- `RETRIEVED != CURRENT`
- `REMEMBERED != AUTHORIZED`
- `CONTENT_HASH_EQUAL != MEMORY_IDENTITY_EQUAL`
- `REVISION != IN_PLACE_REWRITE`
- `QUARANTINED != RETRIEVABLE_BY_DEFAULT`
- `TOMBSTONED != DELETED_LINEAGE`
- `SIMILARITY != VALIDITY`
- `RECORDED_TIME != EVENT_VALID_TIME`
- `CONTEXT_ASSEMBLY != EPISTEMIC_PROMOTION`

## Executable surfaces

- Runtime: `10_MEMORY/memory_lifecycle_runtime.py`
- Tests: `19_TESTS/test_memory_lifecycle_runtime.py`
- Skill validator: `07_SKILLS/amos-agent-memory-dynamics-rscf-engine/scripts/memory_contract_check.py`

## Evidence boundary

Validated target: local SQLite lifecycle semantics and deterministic contract tests.

Still `UNKNOWN/GAP`: distributed memory consistency, semantic extraction accuracy, embedding/graph retrieval quality, privacy/compliance sufficiency, production performance, and automated promotion into validated knowledge.
