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

Operate persistent agent memory without conflating memory with knowledge, current state, or authority.

## States

`INTAKE -> AUTHORITY_RESOLVED -> INTEGRITY_CHECKED -> ELIGIBILITY_RESOLVED -> EXECUTED -> RECORDED -> COMPLETE`

Failure states:

`REJECTED | QUARANTINED | UNKNOWN_GAP`

Memory lifecycle states:

`ACTIVE | QUARANTINED | SUPERSEDED | EXPIRED | TOMBSTONED`

## Inputs

- operation: `READ | ASSEMBLE_CONTEXT | ADMIT | REVISE | QUARANTINE | EXPIRE | TOMBSTONE | HISTORY | VERIFY`
- memory scope
- provenance for writes
- memory identity/origin where applicable
- event-valid time and/or recorded-time cutoff when applicable
- explicit capability set

## Transition contract

1. **INTAKE -> AUTHORITY_RESOLVED**
   - Resolve exact memory scope.
   - Require `memory.read` for reads/history/context.
   - Require the operation-specific write capability for mutation.
   - Missing authority -> `REJECTED`.

2. **AUTHORITY_RESOLVED -> INTEGRITY_CHECKED**
   - Verify content hashes and append-only ledger before consequential reuse.
   - Integrity failure -> `QUARANTINED` and block downstream reuse.

3. **INTEGRITY_CHECKED -> ELIGIBILITY_RESOLVED**
   - Apply lifecycle state.
   - Apply `valid_from` / `valid_to` if event-valid time matters.
   - Apply `recorded_at` cutoff for point-in-time reconstruction.
   - Exclude non-active memory from ordinary retrieval.

4. **ELIGIBILITY_RESOLVED -> EXECUTED**
   - `ADMIT`: create `OBSERVATION`, version 1, origin identity, provenance.
   - `REVISE`: create a new version; mark predecessor `SUPERSEDED`.
   - `QUARANTINE`: isolate without erasing lineage.
   - `EXPIRE`: remove from active retrieval while retaining history.
   - `TOMBSTONE`: terminate active use while preserving lineage.
   - `READ/HISTORY`: return memory records only.
   - `ASSEMBLE_CONTEXT`: return bounded `OBSERVATION` context; never promote epistemic class.

5. **EXECUTED -> RECORDED**
   - Append lifecycle event to the hash-chained ledger.
   - Preserve source provenance and predecessor/successor linkage.

6. **RECORDED -> COMPLETE**
   - Return result, lifecycle state, scope, provenance, temporal bounds, and unresolved gaps.

## Hard invariants

- `MEMORY != KNOWLEDGE`
- `MEMORY != CURRENT_STATE`
- `RETRIEVED != CURRENT`
- `REMEMBERED != AUTHORIZED`
- `REVISION != IN_PLACE_REWRITE`
- `QUARANTINED != RETRIEVABLE_BY_DEFAULT`
- `RECORDED_TIME != EVENT_VALID_TIME`
- `CONTEXT_ASSEMBLY != EPISTEMIC_PROMOTION`

## Executable binding

Reference runtime: `10_MEMORY/memory_lifecycle_runtime.py`

Regression suite: `19_TESTS/test_memory_lifecycle_runtime.py`

Skill validator: `07_SKILLS/amos-agent-memory-dynamics-rscf-engine/scripts/memory_contract_check.py`

## Scope boundary

The runtime validates local SQLite reference semantics only. Distributed consistency, embedding quality, graph extraction quality, privacy/compliance sufficiency, production latency, and automatic knowledge promotion remain `UNKNOWN/GAP`.
