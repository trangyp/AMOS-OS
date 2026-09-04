---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: K Mvcc
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

# K_MVCC — Multiversion Concurrency Snapshot Buffer

## 1. Role

The MVCC kernel provides snapshot-based concurrency control for AMOS OS. MVCC maintains multiple versions of state objects, allowing concurrent readers to access consistent snapshots without blocking writers. This is the primary mechanism for non-blocking reads in AMOS runtime.

## 2. MVCC Core Concepts

### 2.1 Version Chain

Each state object maintains a chain of versions:

```
State_Object {
    versions: [
        {epoch: 1, value: V1, timestamp: T1, writer: W1},
        {epoch: 2, value: V2, timestamp: T2, writer: W2},
        {epoch: 3, value: V3, timestamp: T3, writer: W3},  ← current
    ]
}
```

### 2.2 Snapshot Read

A snapshot read at epoch $E$ sees:
- The version with the largest epoch $\leq E$
- Consistent across all objects in the snapshot
- No interference from concurrent writers

```
READ_SNAPSHOT(epoch_E):
    for each object:
        find version with max(epoch) where epoch ≤ E
    return consistent snapshot
```

### 2.3 Write

A write creates a new version:
1. Read current version (epoch $E_{current}$)
2. Create new version with epoch $E_{new} = E_{current} + 1$
3. CAS the object's current pointer to the new version
4. Old versions are retained for snapshot reads

## 3. AMOS MVCC Semantics

### 3.1 Transaction Isolation Levels

| Isolation Level | Description | AMOS Usage |
|----------------|-------------|------------|
| **Read Uncommitted** | Read any version | Working memory exploration (fastest) |
| **Read Committed** | Read latest committed version | Normal agent operations |
| **Repeatable Read** | Read consistent snapshot for transaction duration | RSCF proof construction |
| **Serializable** | Transactions appear serial | Control plane commit (via epoch ordering) |

### 3.2 Snapshot Consistency

AMOS guarantees that a snapshot read at epoch $E$ is causally consistent:
- All writes with epoch $\leq E$ are visible
- All writes with epoch $> E$ are invisible
- Cross-object dependencies are preserved within the snapshot

### 3.3 Version Garbage Collection

Old versions are retained until:
- No active reader may reference them (all reader epochs advance past the version)
- Garbage collection runs after global epoch advance
- At least one version is always retained (current version)

```
GC_CONDITION(version_V):
    version_V.epoch < min(active_reader_epochs) - safety_margin
```

## 4. MVCC Integration with CAS

MVCC uses CAS for atomic version creation:

```
WRITE_MVCC(object, new_value):
    loop:
        current = object.current_version
        new_version = {epoch: current.epoch + 1, value: new_value}
        if CAS(object.versions_head, current, new_version):
            return SUCCESS
        else:
            retry  // another writer created a version
```

## 5. MVCC Invariants

- **MVCC-01:** Snapshots are consistent — all objects in a snapshot reflect the same epoch
- **MVCC-02:** Version chains are append-only — no mutation of existing versions
- **MVCC-03:** Epoch ordering is monotonic — versions are created in increasing epoch order
- **MVCC-04:** No version is garbage-collected while any reader may reference it
- **MVCC-05:** Current version is never garbage-collected
- **MVCC-06:** Write conflicts are resolved by CAS failure → retry with latest version

## 6. Performance Characteristics

| Operation | Latency | Blocking |
|-----------|---------|----------|
| Snapshot read | O(1) | None |
| Write (no contention) | O(1) | None |
| Write (with contention) | O(retries) | None (lock-free) |
| GC | O(versions_per_object) | None (background) |

MVCC enables:
- **Non-blocking reads:** Readers never block writers
- **Consistent snapshots:** Readers see a consistent view without locks
- **Time-travel:** Read state at any past epoch (for debugging, recovery)

## 7. Inter-Plane Connections

- **CAS:** [[02_KERNEL/K_CAS|K_CAS]] — CAS provides the atomic primitive for version creation
- **MVCC-CAS Integration:** [[02_KERNEL/MVCC_CAS|MVCC_CAS]] — Combined transaction protocol
- **Coordination Avoidance:** [[09_PROTOCOLS/COORDINATION_AVOIDANCE_PROTOCOL|COORDINATION_AVOIDANCE_PROTOCOL]] — MVCC enables coordination-free reads
- **Causal Concurrency:** [[04_RUNTIME/CAUSAL_CONCURRENCY_MVCC|CAUSAL_CONCURRENCY_MVCC]] — Causal ordering of MVCC snapshots
- **Runtime:** [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME_MOC]] — MVCC underlies runtime state access

______________________________________________________________________

**MOC:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]] · [[00_ROOT/00_HOME|00_HOME]]

**Related:** [[02_KERNEL/K_CAS|K_CAS]] · [[02_KERNEL/MVCC_CAS|MVCC_CAS]] · [[04_RUNTIME/CAUSAL_CONCURRENCY_MVCC|CAUSAL_CONCURRENCY_MVCC]]
