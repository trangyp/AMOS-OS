---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Cas Version Vector
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

# CAS_VERSION_VECTOR — CAS Version Vector Protocol

## 1. Role

The CAS Version Vector protocol generalizes single-location Compare-And-Swap (CAS) into a **causal, multi-replica version-tracking primitive** for the AMOS_OS runtime. Where K_CAS provides an atomic single-slot swap, the version vector extends the same discipline to distributed state: each shard/node/replica tracks a vector of per-source counters, and CAS-like operations validate against the full vector rather than a single epoch number.

Version vectors are the mechanism that lets AMOS uphold causal consistency, shard-local finalization, and coordination-free execution (Tier 1) without a global lock, while preserving the lock-free, linearizable character of CAS for commit.

## 2. Data Structure

### 2.1 Version Vector Definition

Let there be $n$ sources (shards, nodes, or writers). A version vector is an $n$-tuple of monotonically increasing counters:

$$
VV = (c_1, c_2, \dots, c_n), \quad c_i \in \mathbb{N}
$$

Incrementing source $i$ yields:

$$
VV^{[+i]} = (c_1, \dots, c_i + 1, \dots, c_n)
$$

### 2.2 Partial Order (Causal Order)

$VV_a \le VV_b$ iff for all $i$, $a.c_i \le b.c_i$. Two vectors are **concurrent** if neither $\le$ the other:
`a ∥ b ⟺ not(a<=b) and not(b<=a)`. This directly encodes causal concurrency: concurrent updates are not ordered; causally dependent updates are.

## 3. Mathematical Foundations

### 3.1 Join (Merge)

The join (least upper bound) of two vectors is the element-wise max:

$$
VV_a \sqcup VV_b = \big(\max(a.c_1, b.c_1), \dots, \max(a.c_n, b.c_n)\big)
$$

The join represents the "latest state known to both" — the causal frontier of a merged replica.

### 3.2 CAS on a Vector

A vector-CAS atomically validates and, if valid, updates a vector:

```
CAS_VECTOR(loc, expected_VV, new_VV):
    if *loc is_at_least expected_VV   # no conflicting concurrent write
        and *loc not_newer_in_any (per policy)
    : write new_VV to loc; return SUCCESS
    else: return FAILURE
```

The atomicity is provided by a single compare-and-swap on the vector word(s) (or a version-stamped aggregate), giving the same lock-free, linearizable guarantee as scalar CAS but with causal semantics.

### 3.3 Conflict Detection

Two committed writes at source basis $i$ and $j$ ($i \ne j$) conflict exactly when their vector components for each other's source are concurrent:

```
CONFLICT(w_i, w_j) ⟺ (w_i ∥ w_j)
```

This is precisely the check a multi-source commit performs before finalization.

## 4. Runtime Protocol

### 4.1 Write Path (Shard-Local + Causal)

```
WRITE(state, source_i):
    my_VV = READ_VV(state)
    new_VV = my_VV[+i]              # increment own counter
    ok = CAS_VECTOR(state.VV, my_VV, new_VV)
    if ok: return COMMITTED(new_VV)
    else:  # concurrent write detected; read and re-resolve
           # CRDT / merge or conflict-resolution policy applies
           return CONFLICT
```

### 4.2 Finalization / Epoch Cross-Check

At epoch close, a shard finalizes its local records and propagates its vector component so downstream shards can build a consistent global picture via join. Shard-local finalization does not require global coordination — it only requires that each shard's vector component be causally consistent with what it has published.

### 4.3 Conflict Resolution Tiers

| Tier | Basis | Coordination | Mechanism |
|------|-------|--------------|-----------|
| 1 | disjoint namespaces | none | version vectors never overlap; no conflict |
| 2 | same shard | local | vector-CAS enforces total order locally |
| 3 | cross-shard, deterministic epoch | epoch ordering | vector-CAS at epoch boundary resolves deterministically |

This mirrors the coordination-avoidance protocol: rely on version vectors to prove disjointness (Tier 1) or deterministic order (Tier 3), avoiding central coordination.

## 5. ABA Prevention

A scalar CAS is vulnerable to the ABA problem (value cycles A→B→A). Version vectors are constructed to be **monotonic** — counters only increment — so a vector never returns to a prior value. Thus vector-CAS inherently prevents ABA at the source counter level:

```
ABA-PREVENTION: counter monotonicity ⟹ VV never revisits a prior exact value
⟹ CAS_VECTOR validates against ever-increasing causal state
```

## 6. Implementation Details

- **Compactness**: store the vector as a bitfield or packed counter array; use a digest (hash) of the vector as the CAS word where the full vector exceeds one atomic word, with the digest compared at swap.
- **Synchronization**: `CAS_VECTOR` executes as a single uninterruptible write on the packed vector (or on the digest + monotonic epoch tag).
- **GC / Pruning**: components for permanently inactive sources can be bounded/compacted after a retention window, with receipts retained for provenance.
- **Backend abstraction**: identical to the 2026 substrate abstraction in SOFT_REALTIME_SCHEDULER — whether the state lives on a CPU shard, a memristor CIM array, or a photonic node, the vector protocol and its CAS discipline are uniform above the substrate.

## 7. AMOS-Specific Constraints

- **Causal consistency over throughput**: version vectors guarantee that any later-observed state is causally consistent, aligning with AMOS's causal epoch model.
- **Commit-time freshness**: a commit validates against the current vector; stale snapshots fail closed (per MVCC_CAS), ensuring no dirty writes.
- **Deterministic tie-break**: cross-vector conflicts resolve by epoch/shard-ID tie-break so conflicting finalizations are deterministic.
- **Provenance**: each vector update references the initiating RSCF/provenance record, preserving auditability.
- **Photonic/wide-fabric scaling**: when photonic interconnect makes cross-shard transport cheap, vector component propagation is no longer bandwidth-bound — but the logical vector discipline (causal, lock-free) is retained regardless of transport cost.

## 8. Invariants

- **VV-01:** Version vectors are monotonically increasing (no ABA).
- **VV-02:** `VV_a <= VV_b` iff $a$ is causally before $b$.
- **VV-03:** Two concurrent commits are always detected as a conflict.
- **VV-04:** Join yields the causal frontier (max over sources).
- **VV-05:** CAS_VECTOR is atomic and linearizable.
- **VV-06:** No dirty writes — commit validates against current vector.
- **VV-07:** Cross-shard conflicts resolve deterministically.

## 9. Inter-Plane Connections

- **CAS kernel:** [[02_KERNEL/K_CAS|K_CAS]] — scalar primitive generalized here
- **MVCC/CAS:** [[02_KERNEL/MVCC_CAS|MVCC_CAS]] — transactional composition
- **Causal concurrency:** [[04_RUNTIME/CAUSAL_CONCURRENCY_MVCC|CAUSAL_CONCURRENCY_MVCC]] — causal epoch model
- **Epoch coordination:** [[04_RUNTIME/MULTI_EPOCH_COORDINATION|MULTI_EPOCH_COORDINATION]] — finalization interaction
- **Shard finalization:** [[09_FINALIZATION_MOC|09_FINALIZATION_MOC]]
- **Scheduler:** [[02_KERNEL/SOFT_REALTIME_SCHEDULER|SOFT_REALTIME_SCHEDULER]] — commit fast-lane

______________________________________________________________________

**MOC:** [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME_MOC]] · [[00_ROOT/00_HOME|00_HOME]]

**Related:** [[02_KERNEL/K_CAS|K_CAS]] · [[04_RUNTIME/CAUSAL_CONCURRENCY_MVCC|CAUSAL_CONCURRENCY_MVCC]] · [[04_RUNTIME/MULTI_EPOCH_COORDINATION|MULTI_EPOCH_COORDINATION]]
