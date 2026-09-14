# Executable Memory Lifecycle Contract

## Status

`AMOS_MODEL + EXECUTED_TESTED_SCOPE` for the local SQLite reference only.

Canonical executable owner:

`07_SKILLS/amos-agent-memory-dynamics-rscf-engine/scripts/memory_lifecycle.py`

Regression evidence:

`19_TESTS/test_memory_lifecycle.py`

## State model

```text
ADMIT -> ACTIVE
ACTIVE -> REVISE -> ACTIVE
ACTIVE -> QUARANTINE -> QUARANTINED
QUARANTINED -> RESTORE -> ACTIVE
ACTIVE|QUARANTINED -> TOMBSTONE -> TOMBSTONED
```

Expiry does not delete memory. It hides a revision from normal retrieval after `expires_at` while retaining lineage.

## Data model

The reference persists:

- memory object identity, namespace, required scope, current status, latest revision;
- immutable historical revisions with content hashes, provenance, source class, temporal validity, expiry, and metadata;
- hash-chained lifecycle events;
- explicit conflict records;
- deterministic context snapshot selections and hashes.

## Core firewalls

```text
MEMORY != KNOWLEDGE
RETRIEVAL != VERIFICATION
RELEVANCE != TRUTH
REVISION != OVERWRITE
CONFLICT != WINNER
TOMBSTONE != PHYSICAL_DELETE
CONTEXT_SNAPSHOT != CURRENT_STATE
LOCAL_SCOPE_CHECK != PRODUCTION_AUTHORIZATION
TEST_PASS != PRODUCTION_VALIDITY
```

## Concurrency

Revision and status writes require `expected_revision`. A stale writer is rejected rather than silently merged. This is optimistic local concurrency, not distributed consensus.

## Conflict handling

The runtime only records a conflict declared by an upstream evidence process. Declaring a conflict quarantines both memories and preserves both provenance chains. Resolution authority remains outside this runtime.

## Context assembly

Normal context assembly:

1. filters to ACTIVE, unexpired, in-scope memories;
2. resolves the revision valid at the requested `as_of` time;
3. scores lexical relevance only;
4. deduplicates exact content hashes;
5. respects a hard character budget;
6. stores exact selected revision identities and hashes.

Snapshot replay marks prior revisions stale and fails closed when a selected object has since been quarantined or tombstoned.

## Production boundary

Still `UNKNOWN/GAP`:

- distributed coordination and fencing;
- cryptographic tenant isolation;
- secure deletion/erasure semantics;
- privacy/legal retention policy;
- vector and graph retrieval calibration;
- production database migration, backup, restore, and disaster recovery;
- deployment authority.
