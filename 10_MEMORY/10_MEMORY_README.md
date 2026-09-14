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

Memory retains experience — working memory, episodic memory, case memory, long-term memory, negative memory, and authority-sensitive memory. The Memory Plane is the **temporal persistence layer** of the AMOS Full Brain OS, governing how cognitive states survive across sessions, how past experiences inform future reasoning, and how forgetting is governed rather than arbitrary.

## 2. Memory Classes

| Class | Description | Retention | Stored epistemic class | Authority |
| :--- | :--- | :--- | :--- | :--- |
| Working | Active processing context | Session | OBSERVATION | Agent-local |
| Episodic | Event-based records | Long-term | OBSERVATION | Scoped |
| Case | Specific case records | Long-term | OBSERVATION or provenance-bound DERIVED content | Scoped |
| Long-term | Persistent remembered content | Governed | OBSERVATION / SOURCE_CLAIM | Controlled |
| Negative | Failed experiences | Long-term | OBSERVATION / UNKNOWN-GAP | Scoped |
| Authority-sensitive | Permission-gated content | Access-controlled | OBSERVATION / DECISION record | Authority-gated |
| Quarantined | Contradictory/unverified | Until resolved | COMPETING / OBSERVATION | Isolated |
| Expired | Historical inactive records | Lineage only | OBSERVATION | None |

A memory object never becomes validated knowledge merely by residing in a long-term tier. Any promotion to validated knowledge occurs outside the Memory Plane through the evidence/knowledge admission pipeline.

## 3. Hard Boundaries

```text
Memory != Knowledge
Memory != Current State
Memory != Canon
Retrieved != Current
Remembered != Authorized
```

A remembered claim is not automatically validated. Memory retrieval returns `OBSERVATION` — stored historical content that has not been independently revalidated by retrieval itself. Promotion to validated knowledge requires the [[11_KNOWLEDGE/KNOWLEDGE_CONTRACT|KNOWLEDGE_CONTRACT]] pipeline.

Memory is historical — it records what was stored or observed. State is current — it describes what is currently authoritative. Memory may inform state updates through governed reasoning; it does not directly modify authoritative state.

Memory is mutable through governed lifecycle operations. Canon is separately governed and cannot be silently changed by memory admission, retrieval, consolidation, or revision.

## 4. Memory Architecture Overview

### 4.1 Tiered Storage Model

The Memory Plane uses six logical storage classes. These classes define lifecycle and retrieval policy, not universal performance guarantees.

| Tier | Name | Purpose | Operational intent | Performance evidence |
| :--- | :--- | :--- | :--- | :--- |
| T1 | HOT | Active working context | Hot-path / highest-priority retrieval | NOT_BENCHMARKED |
| T2 | WARM | Recent episodes and traces | Interactive recent-memory retrieval | NOT_BENCHMARKED |
| T3 | COLD | Long-term persistent storage | Capacity-oriented durable retrieval | NOT_BENCHMARKED |
| T4 | QUARANTINED | Contradictory/isolated claims | Isolated from ordinary context assembly | NOT_BENCHMARKED |
| T5 | EXPIRED | Superseded/inactive lineage | Historical/forensic access only | NOT_BENCHMARKED |
| T6 | RAW_ARCHIVE | Compressed telemetry/raw evidence | Archive/reconstruction path | NOT_BENCHMARKED |

Concrete latency SLOs are `UNKNOWN/GAP` until an executed benchmark binds backend, hardware, dataset, concurrency, cache state, query type, and measurement environment. Tier labels must not be interpreted as millisecond guarantees.

**Detail:** [[10_MEMORY/TIERED_MEMORY_LIFECYCLE_ARCHITECTURE|TIERED_MEMORY_LIFECYCLE_ARCHITECTURE]]

### 4.2 Dual-Representation Substrate

AMOS may use complementary retrieval representations such as:

1. **Vector/embedding indexes** — approximate similarity-based candidate retrieval.
2. **Symbolic/graph indexes** — discrete relation and lineage traversal.

These are retrieval mechanisms, not validity mechanisms:

```text
Similarity != Validity
Graph Edge != Verified Fact
Retrieval Score != Confidence
```

**Detail:** [[10_MEMORY/SEMANTIC_ASSOCIATIVE_GRAPH_SUBSTRATE|SEMANTIC_ASSOCIATIVE_GRAPH_SUBSTRATE]]

### 4.3 Episodic Ledger

Memory lifecycle operations should preserve append-only audit lineage so admissions, revisions, quarantine, expiration, and tombstoning remain reconstructable.

**Detail:** [[10_MEMORY/EPISODIC_MEMORY_SUBSTRATE|EPISODIC_MEMORY_SUBSTRATE]]

### 4.4 Executable Local Lifecycle Reference

The active repository includes a bounded local reference implementation:

- Runtime: `10_MEMORY/memory_lifecycle_runtime.py`
- Regression suite: `19_TESTS/test_memory_lifecycle_runtime.py`
- Skill contract validator: `07_SKILLS/amos-agent-memory-dynamics-rscf-engine/scripts/memory_contract_check.py`

The executable scope covers local SQLite semantics for:

- provenance-bound admission;
- origin/version lineage;
- scoped retrieval;
- event-valid versus recorded time;
- quarantine, supersession, expiration, and tombstoning;
- context assembly that remains `OBSERVATION`;
- content-hash and ledger-integrity checks.

This local implementation does **not** establish distributed consistency, production durability, semantic retrieval quality, privacy/compliance sufficiency, or production performance.

## 5. Memory Operations

### 5.1 Write Operations

| Operation | Description | Authority | Memory-plane output class |
| :--- | :--- | :--- | :--- |
| `ADMIT` | Record new remembered observation | Operation-specific write authority | OBSERVATION |
| `REVISE` | Create a new version while preserving predecessor lineage | Operation-specific write authority | OBSERVATION |
| `QUARANTINE` | Isolate contradictory/suspicious memory | Memory governor/control plane | OBSERVATION / COMPETING state |
| `EXPIRE` | Remove stale memory from ordinary retrieval | Memory governor/control plane | OBSERVATION |
| `TOMBSTONE` | Terminate active use while preserving lineage | Memory governor/control plane | OBSERVATION |
| `CONSOLIDATE` | Derive a bounded summary/schema from multiple memories | Consolidation authority | DERIVED artifact, not automatic knowledge |
| `REVALIDATE` | Re-check remembered content against current evidence | Evidence/knowledge process | Result belongs to evidence/knowledge plane |

### 5.2 Read Operations

| Operation | Description | Output class |
| :--- | :--- | :--- |
| `EXACT_LOOKUP` | Retrieve by memory ID | OBSERVATION |
| `SIMILARITY` | Retrieve candidate memories by similarity | OBSERVATION |
| `SYMBOLIC_TRAVERSAL` | Follow graph relations | OBSERVATION |
| `HYBRID_QUERY` | Combine multiple retrieval mechanisms | OBSERVATION |
| `TEMPORAL_RANGE` | Query by valid/recorded time | OBSERVATION |
| `CAUSAL_CHAIN` | Follow provenance/lineage | OBSERVATION |
| `ASSEMBLE_CONTEXT` | Build bounded prompt/context material | OBSERVATION |

All read operations return stored observations. Retrieval does not independently verify truth, freshness, authority, or present applicability.

### 5.3 Retention and Eviction

A retention policy may be modeled by:

$$
\operatorname{Retain}(i,t)=
\bigl[A_i(t)\geq\theta_r\bigr]
\lor D_i(t),
$$

where:

- $A_i(t)$ is a defined activation/relevance measure for memory $i$ at time $t$;
- $\theta_r$ is the configured retention threshold;
- $D_i(t)$ indicates that a protected dependency still requires the memory.

This is an AMOS policy model, not an empirical law. A production implementation must define and validate the activation function, dependency predicate, retention cost, and legal/privacy retention constraints before automated eviction.

## 6. Key Invariants

| ID | Invariant | Rationale |
| :--- | :--- | :--- |
| `INV-MEM-01` | Memory ≠ Knowledge | Prevents false confidence from retrieval |
| `INV-MEM-02` | Historical lineage is append-preserving | Supports audit/reconstruction |
| `INV-MEM-03` | Forgetting/expiry is governed | Prevents arbitrary data loss |
| `INV-MEM-04` | Quarantined memory is isolated by default | Prevents contaminated context |
| `INV-MEM-05` | Memory access is authority-gated | Enforces scope/access control |
| `INV-MEM-06` | Ordinary reads return OBSERVATION | Retrieval never verifies |
| `INV-MEM-07` | Cross-tier/state movement is governed | Prevents silent promotion/eviction |
| `INV-MEM-08` | Revision creates a new version | Prevents destructive historical rewrite |
| `INV-MEM-09` | Recorded time ≠ event-valid time | Preserves point-in-time correctness |

## 7. Failure Modes

| Failure | Detection | Recovery | Severity |
| :--- | :--- | :--- | :--- |
| Memory corruption | Hash/ledger verification | Quarantine affected lineage; recover from trustworthy evidence if available | CRITICAL |
| Quarantine leakage | Retrieval eligibility check | Force isolation; invalidate affected context | HIGH |
| Authority violation | Scope/capability gate | Reject; audit; escalate | HIGH |
| In-place historical rewrite | Version/lineage audit | Reject mutation; restore prior version if possible | HIGH |
| Temporal collapse | Compare event-valid and recorded coordinates | Reconstruct point-in-time query; mark ambiguity | HIGH |
| Consolidation error | Source/derivation audit | Preserve sources; quarantine derived artifact | MEDIUM |
| Unsupported performance claim | Benchmark-forensics gate | Downgrade to UNKNOWN/GAP | MEDIUM |

## 8. Inter-Plane Connections

- **Cognitive Organism:** [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]] — consumes bounded memory context.
- **Knowledge:** [[11_KNOWLEDGE/KNOWLEDGE_CONTRACT|KNOWLEDGE_CONTRACT]] — separately validates/promotes claims.
- **Runtime:** [[04_RUNTIME/CAUSAL_CONCURRENCY_MVCC|CAUSAL_CONCURRENCY_MVCC]] — governs state/concurrency integration when implemented.
- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] — owns authority and consequential commit decisions.
- **Observability:** [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]] — records bounded memory operations and integrity signals.

______________________________________________________________________

**Parent:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
