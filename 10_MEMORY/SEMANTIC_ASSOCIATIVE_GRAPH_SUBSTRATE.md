---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Semantic Associative Graph Substrate
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

# Semantic Associative Graph Substrate & Hybrid Retrieval

> [!ABSTRACT] Memory Architecture Specification
> Governs the persistent semantic associative knowledge graph of AMOS.
> Unifies dense vector embeddings with discrete symbolic relation closures under the **Reasoning State Claim Framework (RSCF)**.

---

## 1. Dual-Representation Substrate (Vector + Graph)

Every semantic concept node $v_i \in \mathcal{V}$ possesses a dual representation:

$$\mathcal{R}(v_i) = \langle \mathbf{e}_i, \mathcal{E}_{\text{rel}}(v_i), \mathcal{P}(v_i) \rangle$$

1. **Continuous Embedding ($\mathbf{e}_i \in \mathbb{R}^D$):** Dense vector capturing fuzzy semantic similarity, enabling nearest-neighbor semantic search:
   $$\text{Sim}_{\text{dense}}(v_i, v_j) = \frac{\mathbf{e}_i \cdot \mathbf{e}_j}{\|\mathbf{e}_i\| \|\mathbf{e}_j\|}$$
2. **Discrete Symbolic Graph ($\mathcal{E}_{\text{rel}}$):** Typed, directed relational edges enforcing structural constraints:
   - `INDEXED_BY`: Parent MOC or cluster boundary.
   - `GOVERNED_BY`: Axiomatic law or constitutional constraint in `01_CANON`.
   - `BOUND_TO`: Executable code, runtime kernel, or tool definition.
   - `FALSIFIED_BY`: Empirical falsifier condition or competing hypothesis.
   - `DERIVED_FROM`: Upstream source or evidence node.
   - `CONTRADICTS`: Epistemic conflict with another node.
   - `SUPERSEDES`: Version lineage or canon promotion.
3. **Epistemic Provenance Envelope ($\mathcal{P}(v_i)$):** Epistemic class (`OBSERVATION`, `SOURCE_CLAIM`, `DERIVED`, `AMOS_MODEL`), confidence ceiling, and source hash pointer.

---

## 2. Hybrid Retrieval Protocol (Beam-Search Traversal)

Query resolution executes in two coupled phases:

### 2.1 Phase 1 — Dense Retrieval
Identifies the top-$K$ seed nodes in embedding space:
$$\mathcal{V}_{\text{seed}} = \text{TopK}_{v \in \mathcal{V}} \left( \cos(\mathbf{e}_q, \mathbf{e}_v) \right)$$

**Configuration:**
- Default $K = 10$
- Minimum cosine similarity threshold: $0.65$
- Embedding model: 1536-dim (OpenAI Ada-002 compatible)

### 2.2 Phase 2 — Structural Closure Traversal
Expands $\mathcal{V}_{\text{seed}}$ along typed symbolic relations using constrained breadth-first search to find the **smallest sufficient dependency closure**:

$$\mathcal{G}_{\text{closure}} = \text{Traverse}(\mathcal{V}_{\text{seed}}, \text{Filter}(\text{Depth} \le 3, \text{Risk} \le \text{Threshold}))$$

**Traversal Rules:**
- Follow `DERIVED_FROM`, `GOVERNED_BY`, `BOUND_TO` edges (inbound and outbound)
- Follow `FALSIFIED_BY` edges only when explicitly requested for competition analysis
- Never follow `SUPERSEDES` edges backward (historical lineage only)
- Maximum traversal depth: 3 hops (configurable per query)
- Risk budget: total accumulated risk score must remain below threshold

### 2.3 Retrieval Safety

This prevents semantic hallucination by grounding continuous vector recall within verified logical dependencies. The dense retrieval phase identifies relevance; the structural closure phase verifies validity.

```text
RETRIEVAL INVARIANT:
────────────────────
Vector similarity identifies CANDIDATES.
Structural closure validates DEPENDENCIES.
Neither phase alone is sufficient.
```

---

## 3. Graph Maintenance Operations

### 3.1 Node Insertion
```text
INSERT_NODE(v_new):
    1. Compute embedding e_new = Encoder(content(v_new))
    2. Determine epistemic_class from source metadata
    3. Identify typed edges from content analysis
    4. Verify no duplicate node exists (cosine sim > 0.95 AND same epistemic class)
    5. If duplicate: merge provenance, do not create new node
    6. If unique: insert node, compute edge weights, update cluster assignments
```

### 3.2 Edge Promotion
When evidence accumulates, edges can be promoted:
```text
SOURCE_CLAIM --[corroboration_count >= 3]--> EVIDENCE
EVIDENCE     --[contradiction_check_pass]--> VALIDATED
VALIDATED    --[canon_review_pass]--> CANONICAL
```

### 3.3 Contradiction Detection
When a new node contradicts an existing node:
```text
CONTRADICTION_DETECTED(v_new, v_existing):
    1. Create CONTRADICTS edge (bidirectional)
    2. Flag both nodes for competition analysis
    3. Do NOT automatically demote either node
    4. Escalate to Knowledge governance for resolution
    5. Record competition metadata in both nodes
```

---

## 4. Invariants & Epistemic Boundaries

- `INV-SEM-01`: **Vector Proximity $\neq$ Logical Entailment.** High cosine similarity does not prove logical validity or causal relation.
- `INV-SEM-02`: **No Relation Without Provenance.** Every edge in $\mathcal{E}_{\text{rel}}$ must record its originating event ID or canonical citation.
- `INV-SEM-03`: **Fail-Closed on Broken Closure.** If an indispensable premise node is missing or unverified, the retrieval engine marks the result `UNKNOWN/GAP` and halts promotion.
- `INV-SEM-04`: **Memory $\neq$ Knowledge.** A retrieved node is not automatically validated. Semantic recall does not establish truth.
- `INV-SEM-05`: **No Silent Promotion.** Epistemic class transitions require explicit governance action.

---

## 5. Performance Characteristics

| Operation | Latency Target | Throughput Target |
| :--- | :--- | :--- |
| Dense retrieval (Top-10 from 1M nodes) | < 50ms | 100 queries/sec |
| Structural closure (3-hop, 10 seeds) | < 100ms | 50 queries/sec |
| Node insertion (with dedup check) | < 200ms | 1000 nodes/sec |
| Contradiction detection | < 150ms | 50 queries/sec |
| Graph rebuild (full reindex) | < 4 hours | — |

---

## 6. Cross-Vault References

- [[10_MEMORY/10_MEMORY_MOC|10_MEMORY_MOC]]
- [[10_MEMORY/EPISODIC_MEMORY_SUBSTRATE|EPISODIC_MEMORY_SUBSTRATE]]
- [[10_MEMORY/TIERED_MEMORY_LIFECYCLE_ARCHITECTURE|TIERED_MEMORY_LIFECYCLE_ARCHITECTURE]]
- [[11_KNOWLEDGE/11_KNOWLEDGE_MOC|11_KNOWLEDGE_MOC]]
- [[16_SCHEMAS/TENSOR_CONTRACTS|TENSOR_CONTRACTS]]
