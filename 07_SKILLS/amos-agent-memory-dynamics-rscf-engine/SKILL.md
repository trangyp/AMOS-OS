---
name: amos-agent-memory-dynamics-rscf-engine
description: Govern and execute AMOS agent-memory lifecycle operations including admission, versioned revision, scoped retrieval, context assembly, quarantine, expiration, tombstoning, temporal validity, provenance, authority checks, and integrity verification. Use when AMOS must persist or retrieve agent memory, resolve stale/conflicting memory, build context from stored memory, or audit whether memory state is safe to reuse. Preserve Memory != Knowledge, Retrieved != Current, and Remembered != Authorized.
---

# AMOS Agent Memory Dynamics RSCF Engine

Apply `integrity > authority > provenance > temporal validity > retrieval utility`.

## Runtime sequence

1. Resolve memory scope and required authority.
2. Admit new content only as `OBSERVATION` with provenance.
3. Preserve immutable origin identity and version lineage.
4. On correction, create a new version; never silently rewrite historical content.
5. Quarantine contradictory or suspicious memory before retrieval.
6. Apply both event-valid time and recorded time when time matters.
7. Retrieve only from the authorized scope.
8. Assemble context from eligible memory without promoting it to knowledge or action authority.
9. Expire or tombstone stale/superseded records while preserving lineage.
10. Verify content hashes and append-only ledger integrity before consequential reuse.

## Hard invariants

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

## Deterministic checks

Use `scripts/memory_contract_check.py` to validate memory snapshots and lifecycle transitions.

Use the repository runtime `10_MEMORY/memory_lifecycle_runtime.py` for executable local reference semantics when available.

Read `references/memory-lifecycle.md` for the lifecycle model, external mechanism provenance, and scope boundaries.

## Retrieval policy

Return `OBSERVATION` objects by default. Exclude `QUARANTINED`, `SUPERSEDED`, `EXPIRED`, and `TOMBSTONED` records unless the caller explicitly requests forensic/history access and has read authority.

Never treat lexical/vector/graph relevance as truth. Revalidation belongs to the knowledge/evidence plane.

## Write policy

Require explicit write capabilities per operation. A read capability never implies admission, revision, quarantine, expiration, or tombstoning authority.

If provenance is missing, scope is unresolved, or authority is ambiguous, fail closed.

## Output contract

Return the smallest sufficient result containing:
- memory identity and origin/version lineage;
- lifecycle state;
- scope;
- temporal validity when material;
- provenance;
- epistemic class (`OBSERVATION` for retrieval);
- unresolved gaps or conflicts;
- whether the result is eligible for context assembly.

Do not expose hidden chain-of-thought or private model state.
