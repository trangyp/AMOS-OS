---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Kernel State Contract
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
updated: 2026-09-14
---
---
---

# KERNEL STATE CONTRACT

## 0. Status

Kernel-plane contract for **STATE CONTRACT**. AMOS_MODEL; canonical status CONDITIONAL; implementation BOUNDED_PARTIAL. A deterministic single-process MVCC/CAS reference substrate exists for versioned internal state. It is not a durable database, distributed consensus protocol, or external-effect authority.

## 1. Scope

Governs bounded versioned state identity, snapshots, optimistic read/write sets, compare-and-swap, transaction preflight, internal atomic commit, explicit epoch vectors, and idempotent transaction replay. External effects and their authority remain outside this state kernel.

## 2. Contract terms

- **Versioned state** — each stored key carries an explicit version.
- **CAS** — success iff the caller's expected version matches the current version under the bounded local store contract.
- **Snapshot** — a snapshot records values/versions plus epoch vector; `SNAPSHOT_READ != CURRENT_STATE` after later mutation.
- **MVCC-style transaction** — read set, write intents, and expected epochs are validated before any write is applied.
- **Atomic local preflight** — a detected conflict produces no partial writes in the single-process reference implementation.
- **Epoch separation** — `state_epoch`, `causal_epoch`, `policy_epoch`, and `provenance_epoch` remain distinct; no equality mapping is inferred.
- **Replay identity** — repeated use of the same transaction id with the exact same proposal returns the prior receipt; reuse with a different payload is rejected.
- **Effect boundary** — transactions marked with external effects are refused here and routed to a separate authority/effect commit runtime.

## 3. Hard invariants

- `PROPOSAL != COMMIT`.
- `CAS_OK <=> EXPECTED_VERSION == CURRENT_VERSION` within the bounded local store.
- `SNAPSHOT_READ != CURRENT_STATE` after mutation.
- `INTERNAL_STATE_COMMIT != EXTERNAL_EFFECT_AUTHORIZATION`.
- `LOCAL_ATOMICITY != DISTRIBUTED_CONSENSUS`.
- `TEST_PASS != PRODUCTION_DURABILITY`.
- State version changes do not implicitly advance causal, policy, or provenance epochs.
- Non-state epochs do not move backward in the bounded reference runtime.
- Stale read sets or stale epoch vectors block commit rather than being silently rebased.

## 4. Executed reference

Bounded executor and regression owners:

- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/versioned_state_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_versioned_state_runtime.py`

The reference implements:

- exact-version compare-and-swap;
- snapshot capture;
- stale read-set conflict detection;
- multi-write transaction preflight before mutation;
- explicit state/causal/policy/provenance epoch vectors;
- idempotent replay by transaction identity;
- fail-closed rejection of external-effect transactions.

Current tests are local executable evidence only. They do not establish crash durability, multi-process serializability, distributed linearizability, consensus, or real external-effect exactly-once semantics.

## 5. Gaps

OPEN (`UNKNOWN/GAP` where required): durable WAL/storage; process crash recovery; multi-process synchronization; distributed consensus; snapshot isolation/serializability proof under concurrency; garbage collection/version retention; transaction dependency graph; durable outbox/inbox; external-effect reconciliation; policy/authority witness binding; recovery after ambiguous external dispatch.

## 6. Falsifiers

F1: canonical source defines different semantics. F2: CAS succeeds on version mismatch. F3: a conflicting transaction partially mutates state. F4: state mutation silently advances policy/causal/provenance epochs. F5: transaction-id reuse changes the committed payload. F6: external-effect transaction commits inside this state-only runtime. F7: local tests are described as distributed consensus or production durability.

## Worked semantics

1. **Read snapshot** — capture values/versions and explicit epoch vector.
2. **Propose** — construct read versions and unique write intents; proposal is non-authoritative.
3. **Preflight epochs** — expected epoch vector must equal the current vector for this bounded transaction.
4. **Preflight versions** — every read/write expected version must still match.
5. **Reject effectful transactions** — route them to authority/effect governance.
6. **Commit internal state atomically** — only after all checks pass; advance state epoch once.
7. **Emit receipt** — cache by transaction id for idempotent replay.
8. **Revalidate downstream state** separately where dependencies require it.

## Promotion-gate checklist

- [x] typed versioned value schema
- [x] exact CAS semantics
- [x] explicit epoch-vector separation
- [x] stale read/epoch conflict handling
- [x] atomic multi-write preflight in single-process reference
- [x] idempotent transaction replay
- [x] external-effect refusal boundary
- [ ] durable persistence and crash recovery
- [ ] concurrent serializability/isolation proof
- [ ] distributed consensus/replication
- [ ] authority/effect transaction integration

## Cross-plane bindings

- Parent Kernel — [[02_KERNEL/02_KERNEL_CONTRACT|02_KERNEL_CONTRACT]]
- Control plane — [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- Runtime — [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME_MOC]]
- System state — [[12_STATE/12_STATE_MOC|12_STATE_MOC]]
- Observability — [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]]

______________________________________________________________________

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] · [[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

RSCF-NODE
node_id: amos_02_kernel_04_state_kernel_state_contract_md
node_type: note
path: 02_KERNEL/04_STATE/KERNEL_STATE_CONTRACT.md
claim_class: AMOS_MODEL

______________________________________________________________________

**MOC:** [[02_KERNEL/04_STATE/04_STATE_MOC|04_STATE_MOC]]

______________________________________________________________________

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
