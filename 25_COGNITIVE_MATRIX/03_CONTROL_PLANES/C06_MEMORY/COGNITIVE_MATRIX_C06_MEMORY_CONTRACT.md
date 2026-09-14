---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: conditional
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: AMOS_MODEL
topic: Cognitive Matrix C06 Memory Contract
created: 2026-08-22
updated: 2026-09-14
---

# C06_MEMORY — Memory lifecycle control

## 0. Status

`EXECUTABLE_BOUNDED_LOCAL_REFERENCE / SQLITE / TESTED`

Origin architect / steward: **Trang Phan**.

C06 now has a subsystem-local executable reference. This does not promote memory to knowledge or establish distributed production correctness.

## 1. Scope

C06 governs bounded admission, versioned revision, retrieval, quarantine, expiration, tombstoning, provenance retention, bi-temporal validity, and local integrity checking.

## 2. Hard epistemic boundaries

```text
MEMORY != KNOWLEDGE
MEMORY != CURRENT_STATE
RETRIEVED != CURRENT
REMEMBERED != AUTHORIZED
CONTENT_HASH_EQUAL != MEMORY_IDENTITY_EQUAL
REVISION != IN_PLACE_REWRITE
QUARANTINED != DEFAULT_RETRIEVABLE
TOMBSTONED != DELETED_LINEAGE
SIMILARITY != VALIDITY
RECORDED_TIME != EVENT_VALID_TIME
CONTEXT_ASSEMBLY != EPISTEMIC_PROMOTION
```

All ordinary retrievals remain `OBSERVATION` objects.

## 3. Lifecycle

Bounded state transitions are:

`ACTIVE -> QUARANTINED | EXPIRED | TOMBSTONED`

A revision does not mutate historical content in place:

`ACTIVE(v) -> SUPERSEDED(v) + ACTIVE(v+1)`.

The predecessor remains addressable for explicitly authorized forensic/history access.

## 4. Bi-temporal contract

Each version records separately:

- `valid_from`, `valid_to`: represented-world applicability interval;
- `recorded_at`: time AMOS stored the version.

`recorded_at` is never substituted for event-valid time.

## 5. Authority

Read and write capabilities are operation-specific. A read scope does not imply any write scope.

Reference capability forms:

- `memory:admit:<scope>`
- `memory:revise:<scope>`
- `memory:quarantine:<scope>`
- `memory:expire:<scope>`
- `memory:tombstone:<scope>`
- `memory:read:<scope>`
- `memory:forensic:<scope>`

The witness must be fresh and state-version compatible.

## 6. Integrity model

The local runtime stores:

1. SHA-256 content identity for every memory version;
2. immutable origin identity and predecessor version lineage;
3. an append-only operation ledger whose events bind the previous event hash.

`verify_integrity()` checks stored content against its bound digest and recomputes the event chain.

Hash-chain validity is evidence of local record integrity only. It is not proof that remembered content is true.

## 7. Executable reference

Runtime:

`10_MEMORY/memory_lifecycle_runtime.py`

Adversarial tests:

`10_MEMORY/test_memory_lifecycle_runtime.py`

CI:

`.github/workflows/memory-runtime-tests.yml`

The initial Memory Runtime CI lane completed successfully on 2026-09-14.

Tests cover admission, default retrieval, versioned revision, stale-version rejection, quarantine isolation, expiration/tombstone lineage, bi-temporal validity, scoped authority, duplicate-content identity separation, and deliberate content/event-ledger tampering.

## 8. Remaining UNKNOWN/GAP

The local SQLite reference does **not** establish:

- distributed consistency or consensus;
- vector/embedding retrieval quality;
- graph-extraction correctness;
- truthfulness of stored content;
- production latency or throughput;
- cross-tenant authorization correctness;
- privacy/compliance sufficiency;
- automatic knowledge promotion;
- independent trust-root or hardware-backed persistence guarantees.

## 9. Promotion boundary

`TEST_PASS != TRUTH` and `MEMORY_RUNTIME_VALID != KNOWLEDGE_VALID`.

Any promotion beyond `AMOS_MODEL / bounded executable reference` requires independent evidence for the target claim and regime.

[[10_MEMORY/10_MEMORY_README|10_MEMORY_README]] · [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/COGNITIVE_MATRIX_CONTROL_PLANES_CONTRACT|CONTROL_PLANES_CONTRACT]]
