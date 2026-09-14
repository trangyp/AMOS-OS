---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_executable_binding
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Effect Release State
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/derived
  - control-plane
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
canonical_status: CONDITIONAL
---

# EFFECT RELEASE STATE

## 0. Status

Control-plane effect-release artifact. `AMOS_MODEL · CONDITIONAL · implementation BOUNDED_LOCAL`.

Origin architect / steward: **Trang Phan**.

```text
EFFECT_INTENT != AUTHORIZATION
AUTHORIZATION != RELEASE
PREPARED != COMMITTED
COMMITTABLE != COMMITTED
IDEMPOTENCY != AUTHORIZATION
DISPATCHING != COMMITTED
EXTERNALIZED_UNKNOWN != COMMITTED
LOCAL_TRANSACTION != DISTRIBUTED_CONSENSUS
```

## 1. Purpose

`EFFECT_RELEASE_STATE` defines the typed local release-state lifecycle for consequential effects after upstream capability, policy, authority, provenance, semantic-transaction, and commit-time freshness checks.

The active bounded local persistence binding is:

- `release_ledger_store_v44.py`
- `test_release_ledger_store_v44.py`
- [[03_CONTROL_PLANE/08_EFFECTS/EFFECT_RELEASE_LEDGER_VALIDATION_RECEIPT_2026-09-14|Effect Release Ledger Validation Receipt — 2026-09-14]]

## 2. Local release states

The local reference store recognizes:

```text
PREPARED
DISPATCHING
COMMITTED
EXTERNALIZED_UNKNOWN
ABORTED
```

Current legal edges are:

```text
PREPARED -> DISPATCHING
PREPARED -> ABORTED
DISPATCHING -> COMMITTED
DISPATCHING -> EXTERNALIZED_UNKNOWN
EXTERNALIZED_UNKNOWN -> COMMITTED
EXTERNALIZED_UNKNOWN -> ABORTED
```

`PREPARED -> COMMITTED` is intentionally illegal: an effect must enter the dispatch boundary before a committed receipt can close the local release state.

## 3. Release identity and lineage

The local reference binds each record to:

```text
ledger_id
ledger_generation
ledger_version
record_version
idempotency_key
effect_digest
transaction_id
authority_id
principal
state
committed_receipt
```

The store enforces:

- same key + different digest => block idempotency;
- same digest + different key => block idempotency;
- same key+digest but different transaction/authority/principal => block lineage;
- same key+digest with committed receipt => already committed;
- same key+digest in `DISPATCHING` or `EXTERNALIZED_UNKNOWN` => reconcile, never blind redispatch;
- recreated ledger generation => revalidation;
- an old-generation record cannot transition under a new generation even if the caller supplies the current ledger identity.

## 4. Persistence and atomicity

The bounded implementation uses SQLite/WAL with:

- `synchronous=FULL`;
- `BEGIN IMMEDIATE` write transactions;
- monotonic ledger version inside a generation;
- per-record version;
- compare-and-swap checks for generation/version and record version/state;
- generation-scoped unique idempotency key and effect digest constraints;
- preserved historical records across ledger generations.

The current `ledger_hash` is an identity/version hash derived from ledger ID, generation, and version. It is **not** a cryptographic digest of all persisted ledger contents and must not be presented as full tamper-evident history proof.

## 5. Authority boundary

The ledger is not an authorization engine.

`authority_id` and `principal` are lineage-bound fields. Their presence does not prove that authority is current or sufficient. Upstream infrastructure/control-plane gates must establish authority and policy freshness before effect release.

`recreate_generation()` is an administrative local reference operation. Production use must be authority-gated by the caller; this store does not create that authority.

## 6. Receipts and uncertain externalization

A local transition to `COMMITTED` requires a non-empty receipt string. This store does not verify receipt signatures or semantic correctness.

`DISPATCHING` and `EXTERNALIZED_UNKNOWN` are uncertainty-preserving states. The store returns `RECONCILE_EFFECT` for duplicate attempts in these states. It does not itself contact or reconcile with the external sink.

## 7. Current bounded validation

Executed locally on 2026-09-14:

- Python compile: PASS.
- 13 persistence/idempotency/lineage/CAS/reconciliation tests: PASS.
- `ResourceWarning` treated as an error: PASS after explicit connection-lifecycle repair.
- history preservation across ledger generations: PASS.
- stale old-generation record attack using current ledger identity: BLOCKED / revalidation required.

No GitHub Actions run is claimed for this evidence.

## 8. Remaining gaps

- Distributed consensus / multi-node finality: `NOT_ESTABLISHED`.
- External sink acknowledgement and automated reconciliation: `NOT_ESTABLISHED`.
- Signed/typed receipt verification: `NOT_ESTABLISHED`.
- Full-content hash chain or Merkle integrity: `NOT_ESTABLISHED`.
- Durable integration with every effect-producing domain Skill: `PARTIAL`.
- Empirical production validation: `NOT_ESTABLISHED`.

## 9. Falsifiers

F1: an executable test permits key/digest ambiguity or lineage transfer.  
F2: a stale generation or record version can mutate current state without revalidation.  
F3: uncertain externalization is silently treated as committed.  
F4: ledger recreation erases historical release evidence.  
F5: the local reference is presented as distributed consensus or authorization authority.

## 10. Cross-plane bindings

- Governed by canon — [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- Authority — [[03_CONTROL_PLANE/04_AUTHORITY/04_AUTHORITY_MOC|04_AUTHORITY_MOC]]
- Commit — [[03_CONTROL_PLANE/09_COMMIT/09_COMMIT_MOC|09_COMMIT_MOC]]
- Observability — [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]]; observation never substitutes for authority
- Recovery — [[20_OPERATIONS/OPERATIONS_README|OPERATIONS_README]]

RSCF-NODE
node_id: cp_03_control_plane_08_effects_effect_release_state_md
node_type: CONTRACT
path: 03_CONTROL_PLANE/08_EFFECTS/EFFECT_RELEASE_STATE.md
claim_class: AMOS_MODEL
rscf_state: DERIVED
canonical_status: CONDITIONAL

RSCF-RELATIONS:
- IMPLEMENTED_BOUNDED_BY: `release_ledger_store_v44.py`
- VERIFIED_BOUNDED_BY: `test_release_ledger_store_v44.py`
- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

**MOC:** [[03_CONTROL_PLANE/08_EFFECTS/08_EFFECTS_MOC|08_EFFECTS_MOC]]
