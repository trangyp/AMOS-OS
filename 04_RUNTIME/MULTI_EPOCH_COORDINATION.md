---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Multi Epoch Coordination
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# MULTI_EPOCH_COORDINATION — Multi-Epoch Coordination Protocol

## 1. Role

The Multi-Epoch Coordination protocol governs how the AMOS_OS runtime orders, bounds, and finalizes state changes across **multiple concurrently advancing epochs** and across **disparate time domains** — including the continuous-time, analog outputs of 2026 neuromorphic/photonic substrates. It is the runtime discipline that converts raw, unsynchronized change into causally ordered, CAS-addressable, finalizable state.

Epochs give AMOS a discrete, deterministic ordering frame over which causal consistency, MVCC snapshot isolation, and shard-local finalization can be defined — even when the underlying evidence (spikes, photonic pulse trains, sensor streams) is continuous in time.

## 2. Epoch Model

### 2.1 Epoch Definition

An epoch $E$ is a monotonic integer label attached to a coherent batch of state transitions across one or more shards. Epochs are globally comparable:

$$
E_i < E_j \iff i < j
$$

Every committed transition carries the epoch at which it was finalized. This yields a total causal frame even when individual shards advance at different rates.

### 2.2 Multi-Epoch Structure

Multiple epochs can be **in flight concurrently**: different shards may be executing epochs $E_5, E_6, E_7$ simultaneously. The protocol's job is to:
1. Bound what may be committed at each epoch.
2. Detect when causally dependent updates cross epoch boundaries.
3. Finalize shard-local state in a way that yields a consistent global view at each epoch frontier.

## 3. Mathematical Foundations

### 3.1 Causal Cross-Epoch Ordering

An update $u$ at epoch $E_a$ and issue $i$ (per version vector component $VV$) is causally ordered relative to update $v$ at epoch $E_b$ and issue $j$ if:

$$
u \to v \iff (E_a < E_b) \land (VV_u \le VV_v)
$$

If neither orders the other ($u \parallel v$), they are concurrent and must be merged or deterministically resolved at the epoch boundary.

### 3.2 Epoch Frontier

For a set of shards $S$, the epoch frontier at time $t$ is the vector of the most recently **finalized** epoch per shard:

$$
\mathcal{F}(t) = (e_1, e_2, \dots, e_{|S|}), \quad e_s = \text{last finalized epoch of shard } s
$$

A read at snapshot frontier $\mathcal{F}$ sees exactly the committed state consistent with that frontier — the runtime's snapshot-isolation guarantee.

### 3.3 Consistency Bound

The protocol maintains the invariant that no transition referencing epoch $E$ is visible until **all shards** contributing to $E$ have finalized. For a global epoch, this is a barrier:

```
FINALIZE_EPOCH(E):
    for each shard s contributing to E:
        wait for s to finalize its E-local writes (vector-CAS)
    advance global frontier to E
```

For shard-local (partial) epochs, finalization only waits on the participating shards, enabling coordination-free advancement (Tier 1/2).

## 4. Protocol Operations

### 4.1 Epoch Open / Close

```
OPEN_EPOCH(E):     # start a new causal scope
    record E as open for the initiating shard set

CLOSE_EPOCH(E):
    apply all buffered E-state transitions via CAS/vector-CAS
    emit FINALIZED(E, frontier(receipts))
    advance this shard's frontier component to E
```

### 4.2 Cross-Epoch Conflict

A transition that references an earlier epoch but arrives at a later epoch (out-of-order causality) is held until the missing epoch finalizes, preventing forward-reachability of partial state:

```
RECEIVE(transition, E_target):
    if E_target == current_open: apply
    elif E_target < current_open and finalized: apply (historical, ordered)
    else: buffer until ordering satisfied
```

### 4.3 Epoch-Bounding Continuous-Time Inputs

For continuous-time substrates (analog BrainScaleS-2, photonic streams, spike trains), the protocol defines an **epoch-bounding function** that cuts the continuous signal into observables attributable to a discrete epoch:

```
BOUND_TO_EPOCH(signal_window, E):
    accumulate OBSERVATION over the window [t_start(E), t_end(E)]
    tag the aggregate with E and a version-vector component (source)
    → the aggregate is now CAS-addressable within E
```

This bridges the discrete-epoch runtime with the continuous-time physical substrate — the key 2026 integration point (see SOTA synthesis).

## 5. Finalization & Determinism

### 5.1 Shard-Local Finalization

Each shard finalizes its own epoch-local writes independently (coordination-free), then publishes its vector component. Downstream shards build the global view by **join** of published components (per Version Vector semantics).

### 5.2 Deterministic Global Finalize

For epochs requiring a global barrier, finalize resolves any concurrent cross-shard conflicts by a deterministic tie-break (epoch order, then shard-ID), so every observer derives the same global state.

### 5.3 Receipts

Each finalization emits a receipt: `(epoch, shard_set, vector_frontier, provenance)` — sufficient for audit and rollback (K_FAILURE_RECOVERY).

## 6. AMOS-Specific Constraints

- **Causal prior to finalize**: no state is finalized without causal ordering established (via version vectors).
- **Freshness interaction**: the scheduler (SOFT_REALTIME_SCHEDULER) guarantees epoch-close and commit a minimum budget so frontiers advance within a bounded window, even under perceptual (neural) overload.
- **Fail closed**: an epoch that cannot finalize within its allowed freshness bound fails closed and escalates, rather than committing partial/causally-unsound state.
- **Continuous-time bridging**: analog/photonic inputs must be epoch-bounded before entering the CAS/commit path — raw continuous output is `OBSERVATION`, never a committed `DECISION`.

## 7. Invariants

- **ME-01:** Epochs are globally monotonic and comparable.
- **ME-02:** State is not visible until its epoch finalizes (isolation).
- **ME-03:** Concurrent cross-epoch updates are detected and deterministically resolved.
- **ME-04:** Shard-local finalization is coordination-free.
- **ME-05:** Continuous-time inputs are epoch-bounded before commit.
- **ME-06:** Every finalization produces a provenance receipt.
- **ME-07:** Epoch-close cannot be starved by perceptual load.

## 8. Inter-Plane Connections

- **Causal concurrency:** [[04_RUNTIME/CAUSAL_CONCURRENCY_MVCC|CAUSAL_CONCURRENCY_MVCC]] — causal MVCC frame
- **Version vectors:** [[04_RUNTIME/CAS_VERSION_VECTOR|CAS_VERSION_VECTOR]] — causal ordering primitive
- **Shard finalization:** [[09_FINALIZATION_MOC|09_FINALIZATION_MOC]] — finalize mechanics
- **MVCC/CAS:** [[02_KERNEL/MVCC_CAS|MVCC_CAS]] — transactional snapshot isolation
- **Scheduler:** [[02_KERNEL/SOFT_REALTIME_SCHEDULER|SOFT_REALTIME_SCHEDULER]] — epoch budget guarantee
- **Neural-symbolic:** [[02_KERNEL/NEURAL_SYMBOLIC_HYBRID|NEURAL_SYMBOLIC_HYBRID]] — continuous-time observation bridging
- **SOTA substrate:** [[22_RESEARCH/SOTA_NEUROMORPHIC_PHOTONIC_COMPUTING_2026|SOTA_NEUROMORPHIC_PHOTONIC_COMPUTING_2026]]

______________________________________________________________________

**MOC:** [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME_MOC]] · [[00_ROOT/00_HOME|00_HOME]]

**Related:** [[04_RUNTIME/CAS_VERSION_VECTOR|CAS_VERSION_VECTOR]] · [[04_RUNTIME/CAUSAL_CONCURRENCY_MVCC|CAUSAL_CONCURRENCY_MVCC]] · [[02_KERNEL/MVCC_CAS|MVCC_CAS]]
