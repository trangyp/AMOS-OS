---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Runtime Coordination Protocols
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

# RUNTIME_COORDINATION_PROTOCOLS — Production Runtime Coordination Protocol Suite

> [!ABSTRACT] Runtime Specification
> Defines the ten core coordination protocols that govern how AMOS OS agents submit, execute, commit, retry, fail, and recover work. Each protocol is specified with formal semantics, invariants, and failure modes. These protocols are the runtime discipline that converts concurrent agent intent into causally ordered, recoverable, auditable state transitions.
> Dependent on CAS_VERSION_VECTOR, MULTI_EPOCH_COORDINATION, and CAUSAL_CONCURRENCY_MVCC for foundational primitives.

---

## 1. CAS/Version Vector Protocol

### 1.1 Purpose

Compare-and-swap (CAS) with causal version vectors provides the fundamental atomicity primitive for AMOS runtime coordination. Every state mutation is validated against a version vector before commitment, ensuring that concurrent modifications are detected and deterministically resolved.

### 1.2 Formal Definition

A state location $L$ carries a version vector $VV(L) \in \mathbb{N}^n$ where $n$ is the number of known writers (agents, shards, or replicas).

$$
\text{CAS}(L, VV_{\text{expected}}, VV_{\text{new}}, \text{payload}):
\begin{cases}
\text{success} & \text{if } VV(L) = VV_{\text{expected}} \text{ and } VV_{\text{new}} \text{ is } VV_{\text{expected}}[+i] \\
\text{failure} & \text{otherwise}
\end{cases}
$$

### 1.3 Causal Ordering Properties

- **Monotonicity:** Version vector counters are non-decreasing. A writer increments its own component; the result always dominates the previous state.
- **Concurrent detection:** $VV_a \parallel VV_b$ when neither dominates the other. Concurrent writes are always detected as conflicts.
- **Join:** $VV_a \sqcup VV_b = (\max(a_i, b_i))$ for all components $i$. The join yields the causal frontier known to both writers.

### 1.4 AMOS Integration

CAS/version vector operations bind directly to:
- [[04_RUNTIME/CAS_VERSION_VECTOR|CAS_VERSION_VECTOR]] — the foundational primitive
- [[04_RUNTIME/CAUSAL_CONCURRENCY_MVCC|CAUSAL_CONCURRENCY_MVCC]] — transactional composition
- [[03_CONTROL_PLANE/09_COMMIT/CONTROL_PLANE_COMMIT_CONTRACT|CONTROL_PLANE_COMMIT_CONTRACT]] — commit gate enforcement

---

## 2. Multi-Epoch Coordination

### 2.1 Epoch Model

An epoch $E$ is a monotonic integer label attached to a coherent batch of state transitions. Multiple epochs can be in flight concurrently across different shards. The protocol bounds what may be committed at each epoch and detects when causally dependent updates cross epoch boundaries.

### 2.2 Finality Semantics

```
FINALIZE_EPOCH(E):
    for each shard s contributing to E:
        wait for s to finalize its E-local writes (vector-CAS)
    advance global frontier to E
    emit FINALIZED(E, frontier, receipts)
```

**Finality guarantee:** A state transition at epoch $E$ is not visible to any reader until all shards contributing to $E$ have finalized. This is a **strong consistency barrier** — not eventual consistency, not best-effort.

### 2.3 Rollback Semantics

Rollback operates at the epoch level:

```
ROLLBACK(target_epoch):
    1. Identify all epochs E where E > target_epoch
    2. For each such E, in reverse order:
        a. Read pre-state hash from WAL for each mutation in E
        b. Restore state to pre-state hash
        c. Emit ROLLBACK_RECEIPT(E, target_epoch, restored_hash)
    3. Advance global frontier to target_epoch
```

**Constraint:** Rollback is only possible if the WAL chain from `target_epoch` to `current_epoch` is intact. If the WAL chain is broken, rollback is impossible and the system enters DEGRADED mode (§10).

### 2.4 Replay Semantics

Replay reconstructs state by re-executing mutations from the WAL:

```
REPLAY(start_epoch, end_epoch):
    state = SNAPSHOT(start_epoch)
    for each wal_entry in WAL[start_epoch+1 .. end_epoch]:
        if wal_entry.dsc_decision == ALLOW:
            APPLY(state, wal_entry.mutation)
            VERIFY(state, wal_entry.post_state_hash)
    return state
```

**Invariant:** Replay is deterministic — given the same WAL entries and the same start state, it always produces the same end state. This is guaranteed because the DSC is deterministic (see [[03_CONTROL_PLANE/AGENT_SAFETY_ARCHITECTURE_2026|AGENT_SAFETY_ARCHITECTURE_2026]] §2.3).

### 2.5 AMOS Integration

- [[04_RUNTIME/MULTI_EPOCH_COORDINATION|MULTI_EPOCH_COORDINATION]] — foundational epoch protocol
- [[03_CONTROL_PLANE/12_ROLLBACK/CONTROL_PLANE_ROLLBACK_CONTRACT|CONTROL_PLANE_ROLLBACK_CONTRACT]] — rollback governance
- [[03_CONTROL_PLANE/11_REPLAY/CONTROL_PLANE_REPLAY_CONTRACT|CONTROL_PLANE_REPLAY_CONTRACT]] — replay governance

---

## 3. Task State Machine

### 3.1 States

Every task in the AMOS runtime follows a strict state machine:

```
                    ┌──────────┐
                    │ SUBMITTED│
                    └────┬─────┘
                         │ admit
                         ▼
                    ┌──────────┐
               ┌────│ WORKING  │────┐
               │    └──────────┘    │
               │    /     |    \    │
               ▼   ▼      │     ▼  ▼
        ┌──────────┐  ┌────────┐  ┌──────────┐
        │ COMPLETED│  │FAILED  │  │ CANCELED │
        └──────────┘  └────────┘  └──────────┘
                         │
                         │ reject (pre-execution)
                         ▼
                    ┌──────────┐
                    │ REJECTED │
                    └──────────┘
```

### 3.2 State Definitions

| State | Description | Entry Condition | Exit Action |
|-------|-------------|----------------|-------------|
| **SUBMITTED** | Task registered, awaiting admission | Agent or user submits task | Validate schema, bind task lease |
| **WORKING** | Task admitted, execution in progress | Admission checks pass | Emit progress receipts |
| **COMPLETED** | Task finished successfully | Execution + validation pass | Commit state, emit completion receipt |
| **CANCELED** | Task terminated by user or system | Cancel request from authorized source | Release resources, emit cancel receipt |
| **REJECTED** | Task denied before execution | Admission check fails (schema, authority, policy) | Emit rejection receipt with reason |
| **FAILED** | Task terminated due to error | Execution error, timeout, or invariant violation | Rollback if mutations occurred, emit failure receipt |

### 3.3 Valid Transitions

```
SUBMITTED  → WORKING    (on successful admission)
SUBMITTED  → REJECTED   (on admission failure)
SUBMITTED  → CANCELED   (on cancel before start)
WORKING    → COMPLETED  (on successful finish)
WORKING    → FAILED     (on execution error)
WORKING    → CANCELED   (on cancel during execution)
FAILED     → WORKING    (on retry — subject to retry bounds, §5)
REJECTED   → SUBMITTED  (on resubmission after correction)
```

### 3.4 Transition Receipts

Every state transition emits a receipt:

```
TransitionReceipt {
    task_id:       TaskIdentifier,
    from_state:    TaskState,
    to_state:      TaskState,
    reason:        String,          // human-readable reason
    epoch:         Epoch,           // epoch at which transition occurred
    agent_id:      AgentIdentifier, // who triggered the transition
    signature:     PQCSignature,    // cryptographic proof
}
```

**Invariant:** State transitions are **total** (every task is always in exactly one state) and **deterministic** (given the same trigger and state, the next state is always the same).

---

## 4. Lease and Fencing

### 4.1 Purpose

When a task is reassigned (e.g., after a worker failure), the original worker may still be executing. Lease and fencing mechanisms protect against stale-worker mutations.

### 4.2 Lease Protocol

```
ACQUIRE_LEASE(task, worker, duration):
    lease = Lease{
        task_id:   task.id,
        worker_id: worker.id,
        epoch:     current_epoch,
        expires:   now + duration,
        fence:     next_fence_token(),
    }
    CAS(lease_location[task.id], null, lease)
    if success: return lease.fence
    else: return FAILURE  // another worker holds the lease
```

### 4.3 Fencing Token

A fencing token is a monotonically increasing integer issued with each lease. Every mutation must include its fencing token; the commit layer rejects mutations with stale tokens:

```
COMMIT_WITH_FENCE(mutation, fence_token):
    current_fence = READ(lease_location[mutation.task_id])
    if fence_token < current_fence.fence:
        REJECT("stale fence — worker lost lease")
        EMIT STALE_WORKER_REJECTION(mutation, fence_token, current_fence)
    else:
        PROCEED_WITH_COMMIT(mutation)
```

### 4.4 Stale Worker Protection

```
WORKER_FAILURE_DETECTED(worker):
    1. Revoke all leases held by worker
    2. Increment fence tokens for affected tasks
    3. Reassign tasks to new workers with new leases
    4. Any late-arriving mutations from the old worker are rejected by fence check
    5. Emit WORKER_RECOVERY_RECEIPT(worker, affected_tasks, new_fences)
```

**Invariant:** A worker that has lost its lease can never successfully commit a mutation for that task. The fence token guarantees this regardless of timing.

---

## 5. Retry Semantics

### 5.1 Classification by Effect Type

AMOS classifies mutations by their idempotency characteristics to determine safe retry behavior:

| Effect Type | Retry Safe? | Mechanism | Example |
|-------------|------------|-----------|---------|
| **Read-only** | Always | Direct retry | Query state, observe metric |
| **Idempotent effect** | Yes | Retry with same idempotency key | Write to a set, increment a counter with CAS |
| **Non-idempotent effect** | Conditional | IN_DOUBT protocol (§5.2) | Send external message, charge payment |
| **Destructive effect** | No | Fail closed, escalate to human | Delete archive, revoke permanent credential |

### 5.2 IN_DOUBT Protocol

When a non-idempotent effect's outcome is uncertain (e.g., network timeout after the effect may or may not have occurred):

```
NON_IDEMPOTENT_EXECUTION(effect):
    result = EXECUTE(effect)
    if result == SUCCESS:
        RECORD_EFFECT(effect, COMMITTED)
        return COMMITTED
    elif result == TIMEOUT:
        // Effect may have occurred — we don't know
        RECORD_EFFECT(effect, IN_DOUBT)
        ESCALATE_TO_HUMAN(effect, IN_DOUBT, evidence=timeout_details)
        return IN_DOUBT
    elif result == FAILURE:
        RECORD_EFFECT(effect, FAILED)
        return FAILED
```

**Invariant:** IN_DOUBT is a terminal state for automatic processing. A human (or human-delegated agent) must resolve it. The system never retries IN_DOUBT effects automatically.

### 5.3 Retry Budget

```
RETRY_TASK(task, max_attempts=3, backoff=EXPONENTIAL):
    attempts = 0
    while attempts < max_attempts:
        result = EXECUTE(task)
        if result.status == COMPLETED:
            return result
        elif task.effect_type == NON_IDEMPOTENT and result.status == TIMEOUT:
            return IN_DOUBT  // do not retry
        else:
            attempts += 1
            WAIT(backoff(attempts))
    ESCALATE(task, max_attempts_exceeded)
```

---

## 6. MVCC Pattern — Multi-Version Concurrency Control

### 6.1 Purpose

MVCC allows concurrent reads and writes without blocking, by maintaining multiple versions of each state variable. Readers see a consistent snapshot at their read-epoch; writers create new versions without disturbing readers.

### 6.2 Snapshot Isolation

```
READ(var, reader_epoch):
    // Return the version of var that was committed at or before reader_epoch
    for version in var.history (newest to oldest):
        if version.epoch <= reader_epoch:
            return version.value
    return var.initial_value
```

Readers are **never blocked** by writers. Writers are **never blocked** by readers. Conflicts are detected only at commit time via CAS.

### 6.3 Transaction Structure

Every transaction $T_k$ follows:

$$
T_k = \langle E_{\text{read}}, \mathcal{R}(T_k), \mathcal{W}(T_k), \Delta\mathcal{S}_k, \Pi_k \rangle
$$

Where:
- $E_{\text{read}}$: the epoch at which the read-set was captured.
- $\mathcal{R}(T_k)$: the observed read set (variable, epoch) pairs.
- $\mathcal{W}(T_k)$: the proposed write set (variable, new value) pairs.
- $\Delta\mathcal{S}_k$: the proposed state mutation.
- $\Pi_k$: the proof capsule and validation receipts.

At commit time:

$$
\text{ValidateCAS}(T_k) = \bigwedge_{(v_i, e_i) \in \mathcal{R}(T_k)} \left( \text{CurrentEpoch}(v_i) = e_i \right)
$$

If validation fails, the transaction **aborts immediately** and triggers localized replay against the latest epoch.

### 6.4 AMOS Integration

- [[04_RUNTIME/CAUSAL_CONCURRENCY_MVCC|CAUSAL_CONCURRENCY_MVCC]] — the foundational MVCC specification
- [[02_KERNEL/MVCC_CAS|MVCC_CAS]] — kernel-level MVCC implementation
- [[04_RUNTIME/CAS_VERSION_VECTOR|CAS_VERSION_VECTOR]] — version vector primitives

---

## 7. Event Sourcing

### 7.1 Principle

The AMOS runtime does not store only the current state. It stores the **complete sequence of events** that produced the current state. The current state is derived by replaying events from a known good snapshot.

### 7.2 Event Store

```
EventStore {
    events: AppendOnlyLog<Event>,
    snapshots: Map<Epoch, StateSnapshot>,
    
    APPEND(event):
        event.timestamp = NOW()
        event.hash = HASH(event || last_event_hash)
        events.append(event)
    
    REPLAY(from_epoch, to_epoch):
        state = LOAD_SNAPSHOT(nearest_snapshot_before(from_epoch))
        for event in events[from_epoch .. to_epoch]:
            APPLY(state, event)
        return state
}
```

### 7.3 Event Types

| Event Type | Description | Example |
|------------|-------------|---------|
| `TASK_SUBMITTED` | A new task entered the system | Task creation with schema |
| `TASK_STATE_CHANGED` | A task transitioned between states | SUBMITTED → WORKING |
| `CAPABILITY_GRANTED` | An agent received a capability token | Token issuance with PQC sig |
| `CAPABILITY_REVOKED` | A capability token was revoked | Revocation with reason |
| `STATE_MUTATED` | A state variable was updated | CAS write with version |
| `EFFECT_EXECUTED` | An external effect was committed | WAL entry with receipt |
| `GUARDIAN_ACTION` | Guardian rejected/reworked/quarantined | Guardian receipt |
| `FAILURE_DETECTED` | A failure was observed | Error receipt with context |
| `RECOVERY_INITIATED` | Recovery process started | Recovery receipt |
| `EPOCH_FINALIZED` | An epoch completed finalization | Finalization receipt |

### 7.4 Audit Trail Properties

- **Append-only** — events are never modified or deleted.
- **Hash-chained** — each event includes the hash of the previous event, creating a tamper-evident chain.
- **PQC-signed** — critical events carry post-quantum signatures for long-term auditability.
- **Queryable** — events can be filtered by agent, task, epoch, type, or time range.
- **Replayable** — the complete state at any point in history can be reconstructed by replaying events.

---

## 8. Distributed Consensus

### 8.1 Consensus Model

AMOS does not require global consensus for most operations. The coordination-avoidance principle applies: use version vectors to prove disjointness (Tier 1) or deterministic order (Tier 3), avoiding central coordination.

When consensus IS required (epoch barriers, cross-shard conflicts, authority changes), AMOS uses a **partition-tolerant, deterministic** protocol:

### 8.2 Consensus Tiers

| Tier | Condition | Coordination Required | Mechanism |
|------|-----------|----------------------|-----------|
| **1 — Disjoint** | Agents operate on disjoint namespaces | None | Version vectors never overlap; no conflict possible |
| **2 — Shard-local** | All writes within one shard | Local CAS only | Vector-CAS enforces total order locally |
| **3 — Cross-shard, deterministic** | Writes span shards with known order | Epoch ordering | Vector-CAS at epoch boundary; deterministic tie-break |
| **4 — True consensus** | Concurrent, cross-shard, unordered writes | Majority quorum | Raft-derived protocol with epoch ballot |

### 8.3 Tier 4 Protocol

For the rare cases where true consensus is needed:

```
CONSENSUS_ROUND(proposal):
    ballot = (current_epoch, node_id)
    PROPOSE(ballot, proposal)
    wait for MAJORITY acknowledgment
    if majority_acks >= quorum:
        COMMIT(proposal, ballot)
        emit CONSENSUS_RECEIPT(proposal, ballot, ack_set)
    else:
        ABORT(ballot)
        RETRY with incremented epoch
```

**Invariant:** Consensus rounds are bounded in time. If a round cannot achieve quorum within the epoch budget, it fails closed and escalates.

### 8.4 Model Lineage Diversity in Consensus

Consensus participants must include agents from **at least two different model lineages** to prevent correlated decision failures:

```
CONSENSUS_DIVERSITY: |{model_lineage(p) : p ∈ participants}| ≥ 2
```

---

## 9. Failure Isolation

### 9.1 Principle

Failures are contained at the smallest possible scope. Local repair is preferred over global recomputation. The system is designed so that a failure in one shard, agent, or task does not cascade to others.

### 9.2 Failure Classification

| Failure Class | Scope | Response | Cascades? |
|---------------|-------|----------|-----------|
| **Agent crash** | Single agent | Restart with WAL replay | No |
| **Shard failure** | One shard | Local recovery from WAL + snapshot | No |
| **Epoch failure** | One epoch | Rollback to previous epoch | No |
| **Cross-shard conflict** | Multiple shards | Deterministic resolution at epoch boundary | No |
| **Partition** | Network split | Each partition operates independently; reconcile on heal | No |
| **Correlated failure** | Multiple agents, same model lineage | Activate oversight agents from different lineage | No (by design) |
| **Catastrophic** | System-wide | Halt, preserve WAL, escalate to human | Yes (controlled) |

### 9.3 Local Repair

```
LOCAL_REPAIR(failed_task):
    1. Capture failure context (error, state, epoch)
    2. Identify smallest sufficient scope for repair
    3. Acquire lease for failed_task with new fence token
    4. Replay WAL from last successful snapshot to failure point
    5. Re-execute from failure point with updated context
    6. If repair succeeds: emit REPAIR_RECEIPT and continue
    7. If repair fails: escalate to global recomputation
```

### 9.4 Global Recomputation

Global recomputation is the **last resort** — used only when local repair fails or the failure scope exceeds a single shard:

```
GLOBAL_RECOMPUTE(failed_scope):
    1. Snapshot current state at failure boundary
    2. Quarantine affected tasks
    3. Recompute from the last known-good global snapshot
    4. Validate recomputed state against snapshot hash
    5. If valid: swap in recomputed state, release quarantine
    6. If invalid: HALT and escalate to human
```

**Invariant:** Global recomputation is bounded in scope and time. It never touches state outside the declared `failed_scope`.

---

## 10. Recovery Semantics

### 10.1 Recovery State Machine

After a failure is detected, the system follows a structured recovery process:

```
          ┌──────────┐
          │ DEGRADED │
          └────┬─────┘
               │ initiate recovery
               ▼
          ┌───────────┐
          │RECOVERING │
          └────┬──────┘
               │ recovery complete, begin validation
               ▼
          ┌──────────────┐
          │REVALIDATING  │
          └────┬─────────┘
               │ all invariants verified
               ▼
          ┌──────────┐
          │ RESTORED │
          └──────────┘
```

### 10.2 State Definitions

| State | Description | Actions Allowed | Actions Blocked |
|-------|-------------|-----------------|-----------------|
| **DEGRADED** | System operating with reduced capacity; failure detected but not yet addressed | Read-only operations, WAL append | New task admission, external effects |
| **RECOVERING** | Active repair in progress; WAL replay, local repair, or global recomputation | WAL replay, state restoration | All writes except recovery writes |
| **REVALIDATING** | Recovery complete; invariant checks running | Read operations for validation | All mutations |
| **RESTORED** | All invariants verified; full operation resumed | All operations | None |

### 10.3 Recovery Transitions

```
DEGRADED → RECOVERING:
    trigger: RECOVERY_INITIATED event emitted
    condition: failure scope identified, repair plan formulated

RECOVERING → REVALIDATING:
    trigger: repair operation completes
    condition: state hash matches expected post-repair hash

REVALIDATING → RESTORED:
    trigger: all invariant checks pass
    condition: GMEF validation, RSCF validation, law-of-law check

REVALIDATING → DEGRADED:
    trigger: invariant check fails
    condition: repair did not fully resolve the failure
    action: re-enter recovery with expanded scope

DEGRADED → HALT:
    trigger: recovery cannot proceed (WAL chain broken, unrecoverable state)
    condition: maximum recovery attempts exhausted
    action: preserve state, escalate to human, await external intervention
```

### 10.4 Receipt Emission

Each recovery state transition emits a receipt:

```
RecoveryReceipt {
    receipt_type:     RecoveryTransition,
    failed_scope:     ScopeDescription,
    recovery_method:  LocalRepair | GlobalRecompute,
    start_epoch:      Epoch,
    end_epoch:        Epoch,
    state_hash_before: Hash,
    state_hash_after:  Hash,
    invariant_results: Vec<InvariantCheckResult>,
    timestamp:        EpochTimestamp,
    signature:        PQCSignature,
}
```

---

## 11. Invariants

- **COORD-01:** CAS operations are atomic and linearizable.
- **COORD-02:** Version vectors are monotonically increasing (no ABA).
- **COORD-03:** Epochs are globally monotonic and comparable.
- **COORD-04:** State is not visible until its epoch finalizes.
- **COORD-05:** Every task is in exactly one state at any time.
- **COORD-06:** Lease fencing prevents stale-worker mutations.
- **COORD-07:** Non-idempotent effects are never automatically retried.
- **COORD-08:** MVCC reads are never blocked by writes.
- **COORD-09:** Event store is append-only and hash-chained.
- **COORD-10:** Consensus participants span at least two model lineages.
- **COORD-11:** Failures are isolated to the smallest sufficient scope.
- **COORD-12:** Recovery state machine always terminates (DEGRADED → RECOVERING → REVALIDATING → RESTORED or HALT).
- **COORD-13:** Rollback is only possible with an intact WAL chain.
- **COORD-14:** Every state transition emits a cryptographically signed receipt.

---

## 12. Falsifiers

- **F1:** A CAS operation succeeds despite a concurrent conflicting write.
- **F2:** A stale worker successfully commits a mutation after losing its lease.
- **F3:** A non-idempotent effect is automatically retried without human intervention.
- **F4:** An event is modified or deleted from the event store.
- **F5:** A consensus round completes without model lineage diversity.
- **F6:** A failure in one shard cascades to a non-adjacent shard without explicit cross-shard dependency.
- **F7:** The recovery state machine enters a cycle (never terminates).
- **F8:** State becomes visible before its epoch finalizes.
- **F9:** A replay produces a different state than the original execution.
- **F10:** Rollback succeeds with a broken WAL chain.

---

## 13. Promotion-Gate Checklist

- [ ] Typed schema bound to all protocol data structures
- [ ] Identity + versioning implemented for tasks, leases, epochs, and receipts
- [ ] Negative cases covered (stale · conflicting · unauthorized · timeout · partition input)
- [ ] Provenance edges persisted and validated for all state transitions
- [ ] Rollback basin demonstrated for all consequential effects
- [ ] Executed validation receipt specific to these protocols
- [ ] Unresolved critical gaps registered as UNKNOWN/GAP (visible)

---

## 14. Cross-Vault References

- CAS version vector — [[04_RUNTIME/CAS_VERSION_VECTOR|CAS_VERSION_VECTOR]]
- Multi-epoch coordination — [[04_RUNTIME/MULTI_EPOCH_COORDINATION|MULTI_EPOCH_COORDINATION]]
- MVCC causal concurrency — [[04_RUNTIME/CAUSAL_CONCURRENCY_MVCC|CAUSAL_CONCURRENCY_MVCC]]
- Runtime contract — [[04_RUNTIME/RUNTIME_RUNTIME_CONTRACT|RUNTIME_RUNTIME_CONTRACT]]
- Runtime MOC — [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME_MOC]]
- Agent safety architecture — [[03_CONTROL_PLANE/AGENT_SAFETY_ARCHITECTURE_2026|AGENT_SAFETY_ARCHITECTURE_2026]]
- Control plane contract — [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|CONTROL_PLANE_CONTROL_PLANE_CONTRACT]]
- Task contract — [[03_CONTROL_PLANE/01_TASK_CONTRACT/TASK_CONTRACT|TASK_CONTRACT]]
- Capability contract — [[03_CONTROL_PLANE/02_CAPABILITY/CAPABILITY_CONTRACT|CAPABILITY_CONTRACT]]
- Commit contract — [[03_CONTROL_PLANE/09_COMMIT/CONTROL_PLANE_COMMIT_CONTRACT|CONTROL_PLANE_COMMIT_CONTRACT]]
- Rollback contract — [[03_CONTROL_PLANE/12_ROLLBACK/CONTROL_PLANE_ROLLBACK_CONTRACT|CONTROL_PLANE_ROLLBACK_CONTRACT]]
- Replay contract — [[03_CONTROL_PLANE/11_REPLAY/CONTROL_PLANE_REPLAY_CONTRACT|CONTROL_PLANE_REPLAY_CONTRACT]]
- Observability — [[03_CONTROL_PLANE/07_OBSERVABILITY/CONTROL_PLANE_OBSERVABILITY_CONTRACT|CONTROL_PLANE_OBSERVABILITY_CONTRACT]]
- MVCC kernel — [[02_KERNEL/MVCC_CAS|MVCC_CAS]]
- AMOS core laws — [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- Trang Framework — [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] · [[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

______________________________________________________________________

RSCF-NODE
node_id: rt_04_runtime_coordination_protocols_md
node_type: specification
path: 04_RUNTIME/RUNTIME_COORDINATION_PROTOCOLS.md
claim_class: AMOS_MODEL

______________________________________________________________________

**MOC:** [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME_MOC]]
