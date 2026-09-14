---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 12 State Moc
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

# 12 State — Map of Content

## 0. Status

State-plane MOC. `AMOS_MODEL · CONDITIONAL · BOUNDED_PARTIAL`.

A bounded executable single-process MVCC/CAS state substrate is now established for exact-version CAS, snapshots, optimistic read/write-set validation, epoch-vector matching, atomic in-memory multi-write preflight, idempotent transaction replay, and explicit refusal of external-effect transactions. This does **not** establish durable persistence, multi-process isolation, distributed consensus, external-effect exactly-once semantics, or production deployment validity.

Current executable owner:

- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/versioned_state_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_versioned_state_runtime.py`

Full reference-runtime CI passed for the state executor/test pair in GitHub Actions run `34856708741` at commit `753fee9e1957f2fb0e9afe7046c384bd6a118e40`.

## 1. Purpose

The **State plane** governs authoritative state records and state-versioned artifacts — the explicitly represented condition of an AMOS object, subsystem, transaction, artifact, or governed process at a declared version, time, scope, and regime.

Normalized representation (semantic, not an asserted universal physical schema):

```text
STATE = IDENTITY + VALUE/CONDITION + VERSION + SCOPE + REGIME
        + TEMPORAL_CONTEXT + PROVENANCE + AUTHORITY_STATUS
        + DEPENDENCIES + VALIDITY_STATUS
```

Guided by [[12_STATE/STATE_README|STATE_README]] and [[12_STATE/STATE_STATE_CONTRACT|STATE_STATE_CONTRACT]]. Where older contract sections still say a local MVCC/CAS executor is not established, this MOC records the newer bounded runtime evidence; stronger durability/distributed/effect claims remain open.

## 2. State Architecture — Hard Boundaries

```text
Memory != Knowledge != State
```

- **Memory** — persistent/historical representation; informs but does not authorize.
- **Knowledge** — structured claims/relations/understanding.
- **State** — versioned current condition used by governed commits.

Protected firewalls:

```text
OBSERVED != AUTHORITATIVE
PROPOSED != COMMITTED
CACHED != CURRENT
DERIVED != AUTHORITATIVE
PREDICTED != ACTUAL
CAPABLE != AUTHORIZED
NAME != IDENTITY
PATH != VERSION
TIMESTAMP != AUTHORITATIVE_REVISION
SNAPSHOT_READ != CURRENT_STATE
INTERNAL_STATE_COMMIT != EXTERNAL_EFFECT_AUTHORIZATION
LOCAL_ATOMICITY != DISTRIBUTED_CONSENSUS
TEST_PASS != PRODUCTION_DURABILITY
```

## 3. State Families

| Family | Concern |
|---|---|
| Runtime state | Current runtime/system condition |
| Session state | Objective lock, current step, assumptions, decisions, unresolved gaps, rollback pointer |
| Agent state | Agent identity/lifecycle/configured state |
| Mode state | Regime/operating mode (`simulation != production`) |
| Task state | In-flight task condition, success/failure criteria, dependency closure |
| Authority state | Grant/revocation, principal/action/resource/epoch validity |
| Model state | Simulation/model condition (`MODEL STATE != OBSERVED STATE`) |
| Commit state | Proposal vs commit, receipts, rollback/recovery boundary |
| Lifecycle state | Object/subsystem lifecycle transitions |

Each family is versioned, scope-bound, and authority-aware. Existence or recency does not make a state artifact authoritative.

## 4. Runtime Snapshots

Runtime snapshots live in `12_STATE/01_RUNTIME_SNAPSHOTS/`. Snapshot slots record declared state/version/epoch/provenance context; a snapshot is not current merely because it exists.

Current bounded state runtime provides an in-memory `StateSnapshot` containing versioned values plus an explicit `EpochVector`. After a mutation, the prior snapshot remains historical and is not silently treated as current.

## 5. Epoch / Version Separation

```text
state_version != causal_epoch != policy_epoch != provenance_epoch
```

unless an explicit mapping licenses equivalence.

The current reference executor represents these as separate fields and advances `state_epoch` on successful local state commit without implicitly advancing causal, policy, or provenance epochs.

## 6. MVCC / CAS Bounded Runtime

The current reference implementation establishes the following **local** semantics:

```text
CAS_OK <=> EXPECTED_VERSION == CURRENT_VERSION
```

for the bounded in-memory store.

A transaction carries:

```text
transaction_id
read_versions
write_intents
expected_epoch_vector
external_effects flag
```

Commit behavior:

1. exact transaction-id replay returns the prior receipt;
2. transaction-id reuse with a different payload is rejected;
3. external-effect transactions are refused by the state-only runtime;
4. epoch vector is checked;
5. read/write versions are checked;
6. all checks complete before any write is applied;
7. successful internal multi-write commit advances the state epoch once.

This is a deterministic single-process reference model, not a distributed storage guarantee.

## 7. Selective Invalidation Boundary

Selective invalidation is **conditional**, not an unconditional law.

Narrow descendant-only invalidation requires:

```text
typed dependency edges
+
current dependency state
+
decision-relevant dependency completeness
+
computed affected closure
```

If dependency completeness is unknown, broaden quarantine/revalidation or return `UNKNOWN/GAP`; do not assume unrelated state is safe merely because no edge was observed.

## 8. Current Gaps — UNKNOWN/GAP

> [!WARNING] Stronger state mechanisms remain open
> - Durable WAL/storage and crash recovery — `UNKNOWN/GAP`
> - Multi-process transaction isolation/serializability — `UNKNOWN/GAP`
> - Distributed consensus/replication — `UNKNOWN/GAP`
> - Durable version-vector multi-replica protocol — `UNKNOWN/GAP`
> - Atomic multi-RSCF distributed finality — `UNKNOWN/GAP`
> - Causal-epoch finalization across processes/nodes — `UNKNOWN/GAP`
> - Shard-local finalization proof under concurrency — `UNKNOWN/GAP`
> - Durable outbox/inbox and ambiguous external-effect reconciliation — `UNKNOWN/GAP`
> - Production rollback basin demonstrated under crash/effect faults — `UNKNOWN/GAP`
> - Commit-time external authority/effect binding end-to-end — `UNKNOWN/GAP`

These gaps are not invalidated by the local reference implementation.

## 9. Evidence Status

Established bounded evidence:

- executor exists for local MVCC/CAS state transitions;
- adversarial tests cover version mismatch, stale snapshots/read sets, epoch mismatch, atomic conflict behavior, replay identity, and external-effect refusal;
- full reference-runtime CI passed at the cited state-test revision.

Not established:

- universal state correctness;
- full State-plane implementation;
- production persistence/durability;
- distributed linearizability/consensus;
- external-effect authority/finality.

## 10. Failure Modes Guarded

```text
STALE_READ
SCOPE_LEAK
REGIME_DRIFT
AUTHORITY_ESCALATION
PROVENANCE_LOSS
SILENT_PARTIAL_COMMIT
UNKNOWN_AS_VALID
VERSION_EPOCH_COLLAPSE
PROPOSAL_AS_COMMIT
TRANSACTION_ID_REUSE_WITH_DIFFERENT_PAYLOAD
LOCAL_ATOMICITY_AS_DISTRIBUTED_CONSENSUS
```

## 11. Promotion Gate

- [x] bounded local versioned-value schema exists
- [x] exact CAS behavior implemented
- [x] explicit epoch-vector separation implemented
- [x] stale read/version conflict handling implemented
- [x] atomic local multi-write preflight implemented
- [x] idempotent transaction replay implemented
- [x] external-effect refusal boundary implemented
- [x] adversarial regression tests executed
- [ ] durable persistence/crash recovery
- [ ] multi-process isolation proof
- [ ] distributed consensus/replication
- [ ] durable effect reconciliation
- [ ] commit-time external authority/effect integration

## 12. Cross-Plane Bindings

- Contract — [[12_STATE/STATE_STATE_CONTRACT|STATE_STATE_CONTRACT]]
- State orientation — [[12_STATE/STATE_README|STATE_README]]
- Kernel state — [[02_KERNEL/04_STATE/KERNEL_STATE_CONTRACT|KERNEL_STATE_CONTRACT]]
- Control plane — [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- Runtime — [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME_MOC]]
- Memory — [[10_MEMORY/10_MEMORY_MOC|10_MEMORY_MOC]]
- Observability — [[17_OBSERVABILITY/17_OBSERVABILITY_README|17_OBSERVABILITY_README]]
- Operations/recovery — [[20_OPERATIONS/20_OPERATIONS_README|20_OPERATIONS_README]]

## 13. Falsifiers

- F1: canonical source contradicts declared state semantics.
- F2: CAS succeeds on version mismatch.
- F3: a conflicting transaction partially mutates state.
- F4: state mutation silently changes causal/policy/provenance epochs.
- F5: transaction-id reuse changes the committed proposal.
- F6: external-effect transaction commits inside the local state-only runtime.
- F7: local regression success is represented as production durability or distributed consensus.

______________________________________________________________________

**Parent:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
