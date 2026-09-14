# Memory Lifecycle Contract

## Purpose

Bind AMOS memory concepts to a small executable reference without confusing memory storage with knowledge validation, authorization, or production deployment.

## Hard invariants

1. Memory retrieval returns an observation, not a fact.
2. A memory revision never destroys its predecessor.
3. Every memory object carries provenance and access scope.
4. Stale revision writes fail closed.
5. Quarantine removes a memory from normal retrieval without erasing lineage.
6. Tombstone blocks normal retrieval and is terminal in the local reference.
7. Explicit conflicts preserve both competing memories; the runtime does not choose truth.
8. Context snapshots bind exact memory revision identities and hashes.
9. Snapshot replay cannot bypass a later quarantine or tombstone.
10. Search score is relevance evidence only.

## Temporal model

Each revision has:

- `valid_from`: beginning of source/effective validity;
- `valid_to`: end of source/effective validity when superseded;
- `recorded_at`: local transaction/observation time;
- `expires_at`: retrieval-policy expiry.

The pair of effective validity and recorded time is sufficient for bounded historical queries in this local reference. It is not a claim of complete bitemporal database semantics.

## External mechanism provenance

External sources are mechanism references, not authority.

### Letta Code

Pinned source: `letta-ai/letta-code@85cb7ed50a69cdc6ae7084abc9e9ec271d43b215`.

Relevant source mechanisms:

- `src/agent/prompts/letta_local_memfs.md`: agent context is Git-tracked so prior changes can be inspected or reverted.
- `src/skills/builtin/managing-shared-memory/SKILL.md`: shared memory is distinct from in-context memory.
- current concurrency/recovery code separates observer-safe sync from owner-only resumption of interrupted work.

AMOS adaptation: preserve version history and separate stored memory from current context and execution authority. Do not inherit the claim that self-modifying memory is inherently safe.

### Mem0

Pinned source: `mem0ai/mem0@c7ee362aff94a369af70f13f2b4f853f6793ff4c`.

Relevant source mechanisms:

- memory CRUD/search interfaces;
- V3 additive ingestion documentation states that new memories accumulate rather than overwriting prior memories;
- expired memories remain stored and are hidden from normal retrieval by default.

AMOS adaptation: use append/version/tombstone semantics and retrieval-time expiry. Do not treat LLM extraction or vector similarity as truth or authority.

### Graphiti

Pinned source: `getzep/graphiti@c035afb7990b6077331a81e98b04efcfd9bf8184`.

Relevant source mechanisms:

- temporal validity windows (`valid_at`, `invalid_at`);
- episode/source provenance for derived graph facts;
- old facts are invalidated rather than erased;
- temporal filters support historical retrieval.

AMOS adaptation: preserve temporal validity and provenance while keeping memory objects distinct from validated knowledge graph facts.

## Context snapshot contract

A context snapshot stores only the deterministic selection coordinates needed for replay:

```text
namespace
query
as_of
max_chars
ordered(memory_id, revision, content_hash, relevance_score)
```

The snapshot digest excludes wall-clock creation time so identical selection state yields the same digest. Replaying an old revision is allowed only while the owning memory object remains ACTIVE and the caller still has the required scope. A replayed old revision is marked stale when it is no longer latest.

## Authority boundary

The local store checks a supplied scope token against a required scope string. This is an executable contract check, not a production authorization system. Real deployments must bind principal identity, policy version, revocation/freshness, tenant isolation, and commit-time authority outside the memory store.

## Unknown / gap

The local reference does not establish:

- distributed multi-writer consistency;
- encryption or secure deletion;
- privacy-law compliance;
- tenant isolation against a malicious database operator;
- semantic contradiction detection without external evidence;
- calibrated retrieval quality;
- vector/graph backend equivalence;
- production backup/restore behavior;
- production latency, scale, or availability.
