---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Mvcc Cas
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

# MVCC_CAS — MVCC/CAS Transaction Integration

## 1. Role

The MVCC/CAS integration kernel defines how MVCC snapshot reads and CAS atomic writes compose into a coherent transactional protocol for AMOS OS. This is the runtime transaction engine that combines:
- **MVCC** for consistent, non-blocking reads
- **CAS** for atomic, lock-free writes
- **Epoch ordering** for causal consistency

## 2. Transaction Model

### 2.1 Transaction Structure

```
Transaction {
    tx_id: UUID
    epoch: INTEGER  // creation epoch
    read_snapshot: SNAPSHOT  // MVCC snapshot at creation
    write_set: SET<WriteOperation>  // pending writes
    status: PENDING | COMMITTED | ABORTED
}
```

### 2.2 Transaction Lifecycle

```
BEGIN_TRANSACTION
    ↓
    capture MVCC snapshot at current epoch
    ↓
EXECUTE (read from snapshot, accumulate writes in write_set)
    ↓
COMMIT
    ↓
    for each write in write_set:
        CAS(current_version, expected, new_version)
        if CAS fails → ABORT entire transaction
    ↓
    if all CAS succeed → COMMITTED
    if any CAS fails → ABORTED, discard write_set
```

### 2.3 Snapshot Isolation

Transactions execute under snapshot isolation:
- Reads see a consistent snapshot captured at transaction start
- Writes are buffered until commit
- At commit, writes are validated against the current state
- If the current state has changed since snapshot capture, the transaction aborts

## 3. AMOS Transaction Protocol

### 3.1 Read Phase

```
READ(tx, object):
    if object has version in tx.read_snapshot:
        return snapshot version  // no lock needed
    else:
        return latest_committed_version  // fallback
```

### 3.2 Write Phase (Buffered)

```
WRITE(tx, object, new_value):
    add to tx.write_set:
        {object: object, expected_version: current_version, new_value: new_value}
    // actual write deferred to commit
```

### 3.3 Commit Phase

```
COMMIT(tx):
    1. VALIDATE: check no write conflicts since snapshot
        for each write in tx.write_set:
            if object.current_version.epoch > tx.epoch:
                ABORT  // concurrent write detected
    2. APPLY: execute all writes atomically
        for each write in tx.write_set:
            CAS(object.versions_head, write.expected_version, new_version)
            if CAS fails → ABORT all remaining writes
    3. FINALIZE: emit commit receipt with epoch tag
```

### 3.4 Abort Protocol

```
ABORT(tx):
    1. Discard all buffered writes
    2. Release snapshot reference
    3. Emit abort receipt (no state change)
    4. Optionally retry transaction with fresh snapshot
```

## 4. Conflict Resolution

### 4.1 Write-Write Conflict

Two transactions writing the same object:
- First to commit wins (CAS succeeds)
- Second to commit detects conflict (CAS fails, current version has higher epoch)
- Second transaction aborts and retries

### 4.2 Read-Write Conflict

Transaction reads object $O$ at snapshot epoch $E_s$, another transaction writes $O$ at epoch $E_w > E_s$:
- At commit time, validator detects the version has advanced
- Transaction aborts (snapshot is stale)

### 4.3 Conflict Avoidance

AMOS minimizes conflicts through:
- Shard-local transactions (most transactions don't cross shard boundaries)
- Coordination-free execution for disjoint namespaces (Tier 1)
- Epoch ordering for deterministic conflict resolution (Tier 3)

## 5. Invariants

- **TX-01:** Transactions are atomic — all writes commit or none do
- **TX-02:** Snapshot isolation — readers see consistent snapshots, never partial writes
- **TX-03:** Causal ordering — transactions commit in causal epoch order
- **TX-04:** No dirty reads — uncommitted writes are never visible to other transactions
- **TX-05:** No dirty writes — a transaction never writes an uncommitted version
- **TX-06:** Deterministic abort — conflicting transactions always abort in consistent order

## 6. Performance Characteristics

| Operation | Latency | Throughput |
|-----------|---------|------------|
| Begin (snapshot capture) | O(1) | Unlimited |
| Read from snapshot | O(1) | Unlimited |
| Buffer write | O(1) | Unlimited |
| Commit (no conflict) | O(writes × CAS) | High |
| Commit (with conflict) | O(1) | N/A (abort) |

## 7. Inter-Plane Connections

- **CAS:** [[02_KERNEL/K_CAS|K_CAS]] — Atomic primitive for version creation
- **MVCC:** [[02_KERNEL/K_MVCC|K_MVCC]] — Snapshot management and version chains
- **Coordination Avoidance:** [[09_PROTOCOLS/COORDINATION_AVOIDANCE_PROTOCOL|COORDINATION_AVOIDANCE_PROTOCOL]] — Transaction tiers
- **Causal Concurrency:** [[04_RUNTIME/CAUSAL_CONCURRENCY_MVCC|CAUSAL_CONCURRENCY_MVCC]] — Causal epoch management
- **Failure Recovery:** [[02_KERNEL/K_FAILURE_RECOVERY|K_FAILURE_RECOVERY]] — Transaction rollback
- **Control Plane:** [[03_CONTROL_PLANE/09_COMMIT/09_COMMIT_MOC|09_COMMIT_MOC]] — Commit authority gating

______________________________________________________________________

**MOC:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]] · [[00_ROOT/00_HOME|00_HOME]]

**Related:** [[02_KERNEL/K_CAS|K_CAS]] · [[02_KERNEL/K_MVCC|K_MVCC]] · [[04_RUNTIME/CAUSAL_CONCURRENCY_MVCC|CAUSAL_CONCURRENCY_MVCC]]
