---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 10 Memory Readme
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

# 10 Memory — README

## 1. Role

Memory retains experience — working memory, episodic memory, case memory, long-term memory, negative memory, and authority-sensitive memory. The Memory Plane is the **temporal persistence layer** of the AMOS Full Brain OS, governing how cognitive states survive across sessions, how past experiences inform future reasoning, and how forgetting is mathematically controlled rather than arbitrary.

## 2. Memory Classes

| Class | Description | Retention | Epistemic Class | Authority |
| :--- | :--- | :--- | :--- | :--- |
| Working | Active processing context | Session | OBSERVATION | Agent-local |
| Episodic | Event-based records | Long-term | OBSERVATION | Scoped |
| Case | Specific case records | Long-term | DERIVED | Scoped |
| Long-term | Persistent knowledge | Permanent | SOURCE_CLAIM → VALIDATED | Controlled |
| Negative | Failed experiences | Long-term | UNKNOWN/GAP | Scoped |
| Authority-sensitive | Permission-gated | Access-controlled | DECISION | Authority-gated |
| Quarantined | Contradictory/unverified | Until resolved | COMPETING | Isolated |
| Expired | Tombstone records | Lineage only | EXPIRED | None |

## 3. Hard Boundaries

```
Memory != Knowledge
```

A remembered claim is not automatically validated. Memory retrieval returns `OBSERVATION` — raw data that has been stored but not independently verified. Promotion to `VALIDATED` knowledge requires passing through the [[11_KNOWLEDGE/KNOWLEDGE_CONTRACT|KNOWLEDGE_CONTRACT]] promotion pipeline.

```
Memory != State
```

Memory is historical — it records what happened. State is current — it describes what is. Memory feeds state updates through the reasoning pipeline; it does not directly modify state.

```
Memory != Canon
```

Memory is mutable (subject to governed decay and consolidation). Canon is immutable (subject to governed amendment via [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]).

## 4. Memory Architecture Overview

### 4.1 Tiered Storage Model

The Memory Plane uses a 6-tier storage model that balances access speed against storage cost:

| Tier | Name | Purpose | Latency |
| :--- | :--- | :--- | :--- |
| T1 | HOT | Active working context | <5ms |
| T2 | WARM | Recent episodes and traces | <50ms |
| T3 | COLD | Long-term persistent storage | <200ms |
| T4 | QUARANTINED | Contradictory/isolated claims | <100ms |
| T5 | EXPIRED | Superseded tombstones | <50ms |
| T6 | RAW_ARCHIVE | Compressed telemetry | <500ms |

**Detail:** [[10_MEMORY/TIERED_MEMORY_LIFECYCLE_ARCHITECTURE|TIERED_MEMORY_LIFECYCLE_ARCHITECTURE]]

### 4.2 Dual-Representation Substrate

Memory is stored in two complementary representations:

1. **Vector embeddings** — Dense continuous representations for similarity-based retrieval
2. **Symbolic graph** — Discrete relations for logical traversal and constraint checking

**Detail:** [[10_MEMORY/SEMANTIC_ASSOCIATIVE_GRAPH_SUBSTRATE|SEMANTIC_ASSOCIATIVE_GRAPH_SUBSTRATE]]

### 4.3 Episodic Ledger

All memory operations are recorded in a monotonic append-only episodic ledger, providing complete audit trail and causal lineage.

**Detail:** [[10_MEMORY/EPISODIC_MEMORY_SUBSTRATE|EPISODIC_MEMORY_SUBSTRATE]]

## 5. Memory Operations

### 5.1 Write Operations

| Operation | Description | Authority | Epistemic Class |
| :--- | :--- | :--- | :--- |
| `ADMIT` | Record new observation | Agent-scoped | OBSERVATION |
| `CONSOLIDATE` | Compress episodes into schemas | Consolidation engine | DERIVED |
| `PROMOTE` | Move memory to higher tier | Memory governor | DERIVED |
| `DEMOTE` | Move memory to lower tier | Memory governor | DERIVED |
| `QUARANTINE` | Isolate contradictory claim | Memory governor | COMPETING |
| `REVALIDATE` | Refresh expired memory | Memory governor | SOURCE_CLAIM |
| `TOMBSTONE` | Mark superseded memory | Memory governor | EXPIRED |

### 5.2 Read Operations

| Operation | Description | Output Class |
| :--- | :--- | :--- |
| `EXACT_LOOKUP` | Retrieve by memory ID | OBSERVATION |
| `SIMILARITY` | Retrieve by vector similarity | OBSERVATION |
| `SYMBOLIC_TRAVERSAL` | Follow graph relations | OBSERVATION |
| `HYBRID_QUERY` | Combine similarity + symbolic | OBSERVATION |
| `TEMPORAL_RANGE` | Query by time window | OBSERVATION |
| `CAUSAL_CHAIN` | Follow causal lineage | OBSERVATION |

All read operations return `OBSERVATION` — the result is raw retrieved content, never independently verified.

### 5.3 Retention and Eviction

Retention is governed by the activation model:

$$\text{Retain}(i) \iff A_i(t) \geq \theta_{\text{retention}} \lor \text{has\_critical\_dependents}(i)$$

Where $A_i(t)$ is the activation of memory node $i$ at time $t$. Eviction (transition to EXPIRED) occurs only when activation falls below threshold and no critical dependents exist.

## 5. Key Invariants

| ID | Invariant | Rationale |
| :--- | :--- | :--- |
| `INV-MEM-01` | Memory ≠ Knowledge | Prevents false confidence from retrieval |
| `INV-MEM-02` | Episodic memory is append-only | Preserves causal lineage |
| `INV-MEM-03` | Forgetting is mathematically governed | Prevents arbitrary data loss |
| `INV-MEM-04` | Quarantined memory is isolated | Prevents contaminated reasoning |
| `INV-MEM-05` | Memory access is authority-gated | Enforces access control |
| `INV-MEM-06` | All reads return OBSERVATION | Retrieval never verifies |
| `INV-MEM-07` | Cross-tier movement is governed | No arbitrary promotion or eviction |

## 6. Failure Modes

| Failure | Detection | Recovery | Severity |
| :--- | :--- | :--- | :--- |
| **Memory corruption** | Hash verification | Restore from snapshot; quarantine | CRITICAL |
| **Activation overflow** | Activation bound check | Clamp to maximum; log | LOW |
| **Quarantine failure** | Isolation check | Force isolation; notify steward | HIGH |
| **Consolidation error** | Schema induction failure | Skip episode; log | MEDIUM |
| **Eviction of critical node** | Dependency check | Restore; prevent eviction | HIGH |
| **Authority violation** | Access check on read/write | Reject; log; escalate | HIGH |

## 7. Inter-Plane Connections

- **Cognitive Organism:** [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]] — Cognitive organism accesses memory
- **Knowledge:** [[11_KNOWLEDGE/KNOWLEDGE_CONTRACT|KNOWLEDGE_CONTRACT]] — Memory feeds knowledge validation
- **Runtime:** [[04_RUNTIME/CAUSAL_CONCURRENCY_MVCC|CAUSAL_CONCURRENCY_MVCC]] — Memory uses causal snapshots for reads
- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] — Memory access authority enforced
- **Observability:** [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]] — Memory operations produce observability data

______________________________________________________________________

**Parent:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
