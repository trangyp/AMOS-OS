---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: K Cas
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

# K_CAS — Compare-And-Swap Epoch ALU

## 1. Role

The Compare-And-Swap (CAS) kernel provides the fundamental lock-free atomic primitive for AMOS OS state transitions. CAS enables concurrent state updates without global locks by allowing a thread to atomically verify that a memory location holds an expected value before writing a new value.

CAS is the building block for all higher-level concurrency primitives in AMOS: MVCC snapshots, epoch management, shard-local finalization, and coordination-free execution.

## 2. CAS Operation

The CAS operation is defined as:

```
CAS(location, expected_value, new_value) → {
    if *location == expected_value:
        *location = new_value
        return SUCCESS  // (old_value = expected_value)
    else:
        return FAILURE  // (old_value ≠ expected_value, location was modified by another thread)
}
```

**Properties:**
- Atomic: CAS executes as a single uninterruptible operation
- Lock-free: No mutual exclusion required between concurrent CAS operations
- Linearizable: Concurrent CAS operations appear to execute in some sequential order

## 3. AMOS CAS Semantics

### 3.1 State Transition via CAS

A state transition in AMOS follows the CAS loop pattern:

```
1. READ current state → S_current
2. COMPUTE desired new state → S_new = f(S_current)
3. CAS(state_location, S_current, S_new)
4. If CAS fails (another thread modified state):
   a. Re-read current state → S_current'
   b. Re-compute → S_new' = f(S_current')
   c. Retry CAS
5. If CAS succeeds → transition complete, emit receipt
```

### 3.2 Epoch Tag CAS

CAS is used to atomically advance epoch tags:

```
CAS(epoch_location, expected_epoch, new_epoch)
```

Where `new_epoch = expected_epoch + 1` and the CAS ensures no other thread has advanced the epoch between read and write.

### 3.3 Optimistic Concurrency Control

CAS enables optimistic execution:
1. Execute operation speculatively without locks
2. At commit time, CAS the result against the expected pre-condition
3. If CAS fails, discard speculative work and retry

This pattern is used throughout AMOS for:
- Shard-local finalization (CAS finalization record against expected epoch)
- RSCF observation logging (CAS observation against expected state)
- Knowledge promotion (CAS claim class against expected class)

## 4. CAS Failure Analysis

| Failure Type | Cause | Recovery |
|-------------|-------|----------|
| **Spurious failure** | Another thread performed a valid concurrent CAS | Retry with updated state |
| **ABA problem** | Value changed from A to B and back to A between read and CAS | Use versioned CAS (epoch tags prevent ABA) |
| **Livelock** | Repeated CAS failures due to high contention | Exponential backoff or escalate to shard coordination |
| **Starvation** | One thread's CAS always fails due to another thread's priority | Fairness ordering via shard-ID tie-breaking |

### 4.1 ABA Prevention

AMOS prevents ABA through epoch tagging:
- Each state version carries a monotonically increasing epoch number
- CAS compares both value AND epoch number
- A value that returns to its previous state but with a different epoch is detected

```
CAS_with_epoch(location, expected_value, expected_epoch, new_value, new_epoch)
→ requires: value == expected_value AND epoch == expected_epoch
```

## 5. CAS Performance Characteristics

| Metric | Value | Description |
|--------|-------|-------------|
| Best case | O(1) | Single CAS succeeds |
| Average case | O(1 + contention) | Expected retries proportional to contention |
| Worst case | Unbounded | Livelock under extreme contention (mitigated by backoff) |
| Throughput | High under low contention | Degrades with high contention |
| Memory overhead | Zero | No lock structures allocated |

## 6. Invariants

- **CAS-01:** CAS is atomic — no other thread observes a partial write
- **CAS-02:** CAS is linearizable — concurrent CAS operations have a total order
- **CAS-03:** CAS failure implies the location was modified — no spurious failures
- **CAS-04:** Every CAS failure triggers a retry with updated state — no stale writes
- **CAS-05:** CAS with epoch tags prevents ABA — version monotonicity preserved

## 7. Inter-Plane Connections

- **MVCC:** [[02_KERNEL/K_MVCC|K_MVCC]] — CAS provides the atomic primitive for MVCC snapshot operations
- **MVCC-CAS Integration:** [[02_KERNEL/MVCC_CAS|MVCC_CAS]] — Combined MVCC/CAS transaction protocol
- **Coordination Avoidance:** [[09_PROTOCOLS/COORDINATION_AVOIDANCE_PROTOCOL|COORDINATION_AVOIDANCE_PROTOCOL]] — CAS enables coordination-free execution
- **Failure Recovery:** [[02_KERNEL/K_FAILURE_RECOVERY|K_FAILURE_RECOVERY]] — CAS rollback uses CAS to atomically restore state
- **Runtime:** [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME_MOC]] — CAS underlies all runtime state transitions

______________________________________________________________________

**MOC:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]] · [[00_ROOT/00_HOME|00_HOME]]

**Related:** [[02_KERNEL/K_MVCC|K_MVCC]] · [[02_KERNEL/MVCC_CAS|MVCC_CAS]] · [[02_KERNEL/K_CAS|K_CAS]]
