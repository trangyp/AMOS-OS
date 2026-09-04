---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Tiered Memory Lifecycle Architecture
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

# Tiered Memory Lifecycle Architecture & Activation Dynamics

> [!ABSTRACT] Memory Substrate Specification
> Defines the 6-tier memory lifecycle (`HOT`, `WARM`, `COLD`, `QUARANTINED`, `EXPIRED`, `RAW_ARCHIVE`) and cognitive activation dynamics (spreading activation, interference, decay, consolidation) for AMOS Full Brain OS.
> Solves Gaps 1051–1140 identified in the [[25_COGNITIVE_MATRIX/AMOS_COGNITIVE_ARCHITECTURE_MATRIX|Cognitive Architecture Matrix]].

---

## 1. Six-Tier Memory Lifecycle State Machine

```
              ┌───────────────┐
              │  RAW_ARCHIVE  │ (Raw sensor & BCI telemetry streams)
              └───────┬───────┘
                      │ Admission Filter (Salience > θ_admit)
                      ▼
              ┌───────────────┐
              │      HOT      │ (Working state, cognitive registers, active context)
              └──┬─────────┬──┘
    Consolidate  │         │ Contradiction / Conflict
 (Decay < θ_hot) │         │
                 ▼         ▼
  ┌─────────────────┐   ┌─────────────────┐
  │      WARM       │   │   QUARANTINED   │ (Contradictory / Falsified / Unverified)
  └──┬───────────┬──┘   └─────────────────┘
     │           │
Deep │           │ TTL / Invalidation
Archive          ▼
     │   ┌─────────────────┐
     │   │     EXPIRED     │ (Pruned from active graph, tombstone retained)
     │   └─────────────────┘
     ▼
┌───────────────┐
│     COLD      │ (Long-term persistent semantic & episodic graph)
└───────────────┘
```

### Tier Specifications:
1. **HOT (Working Memory):** High-speed RAM/KV-cache. Capacity: bounded to active cognitive task context. Latency: $< 5\text{ ms}$.
2. **WARM (Episodic Buffer):** Local indexed vector/graph store. Retains recent episodes, intermediate reasoning traces. Latency: $< 50\text{ ms}$.
3. **COLD (Archival Knowledge Graph):** Permanent Obsidian vault notes, RSCF proof capsules, vector databases. Latency: $< 200\text{ ms}$.
4. **QUARANTINED (Contradiction Hold):** Isolated from inference traversal. Triggered when two verified claims contradict until human steward or SMT solver resolves.
5. **EXPIRED (Tombstone):** Nodes superseded by newer versions. Historical lineage preserved via hash pointer.
6. **RAW_ARCHIVE (Cold Telemetry):** Lossless compressed sensory/telemetry logs for forensic audit.

---

## 2. Activation Dynamics & Forgetting Formulation

Cognitive node activation $A_i(t)$ determines retrieval probability and working memory admission:

$$A_i(t) = B_i + \sum_{j \in \mathcal{C}(i)} W_{ji} S_{ji} - \delta \cdot \ln(1 + \Delta t_{i})$$

Where:
* $B_i = \ln \left( \sum_{k=1}^K t_k^{-d} \right)$: Base-level activation based on power-law frequency of use.
* $\sum_j W_{ji} S_{ji}$: Spreading activation from currently active context nodes $j$.
* $\delta \cdot \ln(1 + \Delta t_i)$: Time-dependent exponential decay (forgetting curve).

### Interference & Pruning Condition:
A node transitions from `WARM` to `EXPIRED` if its activation falls below the retention floor:
$$A_i(t) < \theta_{\text{retention}} \quad\land\quad \text{has\_critical\_dependents}(i) = \text{False}$$

---

## 3. Consolidation & Offline Dream Cycle

During idle cognitive epochs (system maintenance mode), the consolidation engine executes:
1. **Abstraction:** Compresses multiple episodic episode traces into unified procedural schemas.
2. **Topological Healing:** Resolves broken wikilinks, reconciles duplicate entities, updates MOC indices.
3. **Contradiction Resolution:** Runs SMT checks on newly admitted claims against existing axioms in `01_CANON`.

---

## 4. Tier Promotion Rules

### 4.1 Promotion Conditions

| From | To | Condition | Gate Function |
| :--- | :--- | :--- | :--- |
| RAW_ARCHIVE | HOT | Salience > θ_admit | Admission filter |
| HOT | WARM | Activation < θ_hot | Decay-based demotion |
| WARM | COLD | Deep archive consolidation | Idle consolidation cycle |
| WARM | EXPIRED | TTL expired OR activation < θ_retention | Freshness check |
| Any | QUARANTINED | Contradiction detected | Contradiction gate |
| QUARANTINED | Any | Resolution by steward or SMT solver | Resolution gate |
| EXPIRED | WARM | Explicit revalidation | Revalidation gate |

### 4.2 Promotion Gate Functions

**Admission Gate (RAW → HOT):**

$$\text{Admit}(x) \iff \text{Salience}(x) > \theta_{\text{admit}}$$

Where salience is computed as:

$$\text{Salience}(x) = \alpha_r \cdot \text{Recency}(x) + \alpha_f \cdot \text{Frequency}(x) + \alpha_{\text{rel}} \cdot \text{Relevance}(x) + \alpha_a \cdot \text{Authority}(x) + \alpha_n \cdot \text{Novelty}(x)$$

With constraint: $\sum \alpha_i = 1$

**Consolidation Gate (HOT → WARM):**

$$\text{Consolidate}(x) \iff A_i(t) < \theta_{\text{hot}} \land \text{has\_critical\_dependents}(x) = \text{False}$$

**Pruning Gate (WARM → EXPIRED):**

$$\text{Prune}(x) \iff A_i(t) < \theta_{\text{retention}} \land \text{TTL}(x) \text{ expired} \land \text{has\_critical\_dependents}(x) = \text{False}$$

**Quarantine Gate (Any → QUARANTINED):**

$$\text{Quarantine}(x) \iff \exists\, y \in \text{KnowledgeGraph}: \text{Contradicts}(x, y) \land \text{Confidence}(y) > \text{Confidence}(x)$$

---

## 5. Spreading Activation Mathematics

### 5.1 Activation Function

Cognitive node activation $A_i(t)$ determines retrieval probability and working memory admission:

$$A_i(t) = B_i + \sum_{j \in \mathcal{C}(i)} W_{ji} S_{ji} - \delta \cdot \ln(1 + \Delta t_{i})$$

Where:
* $B_i = \ln \left( \sum_{k=1}^K t_k^{-d} \right)$: Base-level activation based on power-law frequency of use.
* $\sum_j W_{ji} S_{ji}$: Spreading activation from currently active context nodes $j$.
* $\delta \cdot \ln(1 + \Delta t_i)$: Time-dependent exponential decay (forgetting curve).

### 5.2 Spreading Activation Parameters

```yaml
spreading_activation:
  base_level:
    formula: "B_i = ln(sum(t_k^-d for k in 1..K))"
    d: 0.5  # Power-law decay exponent
    K: 10   # Number of recent access events considered
  
  context_activation:
    formula: "sum(W_ji * S_ji for j in neighbors)"
    W_ji: "Edge weight from node j to node i"
    S_ji: "Semantic similarity between node j and node i"
    max_neighbors: 20  # Bounded spreading to prevent explosion
  
  decay:
    formula: "delta * ln(1 + delta_t)"
    delta: 0.5  # Decay rate parameter
    min_activation: 0.01  # Below this = eligible for pruning
```

### 5.3 Activation Propagation

```yaml
activation_propagation:
  method: "Parallel bounded spreading"
  max_hops: 3  # Maximum path length for activation spread
  decay_per_hop: 0.5  # Activation halved per hop
  threshold: 0.1  # Stop spreading if activation < threshold
  
  convergence:
    max_iterations: 10
    convergence_threshold: 0.001  # Stop if change < threshold
    method: "Jacobi iteration"
```

---

## 6. Time-Decay Forgetting Curves

### 6.1 Forgetting Function

The probability of retaining a memory at time $t$ after encoding:

$$P(\text{retain}, t) = e^{-\lambda \cdot t} \cdot (1 + \alpha \cdot \text{rehearsal\_count}(t))$$

Where:
- $\lambda$ = decay rate (configurable per memory class)
- $\alpha$ = rehearsal benefit factor
- $\text{rehearsal\_count}(t)$ = number of rehearsals before time $t$

### 6.2 Decay Rates by Memory Class

| Memory Class | λ (decay rate) | Half-life | Rationale |
| :--- | :--- | :--- | :--- |
| Working | 0.1 | ~7 hours | Session-bound; naturally cleared |
| Episodic (recent) | 0.01 | ~3 days | Recent episodes retained longer |
| Episodic (old) | 0.001 | ~30 days | Older episodes fade gradually |
| Case | 0.0005 | ~60 days | Case records persistent |
| Negative | 0.002 | ~15 days | Failures retained but deprioritized |
| Authority-sensitive | 0.0001 | ~200 days | Permission-gated; long retention |

### 6.3 Rehearsal Effects

Each rehearsal (retrieval or active processing) boosts retention:

$$\text{rehearsal\_benefit}(n) = \alpha \cdot \log(1 + n)$$

Where $n$ = number of prior rehearsals. This models the **spacing effect** — each additional rehearsal provides diminishing but positive returns.

---

## 7. Interference & Pruning

### 7.1 Interference Detection

When two memories compete for the same retrieval slot:

$$\text{Interference}(i, j) = \text{Similarity}(i, j) \cdot |\text{Activation}(i) - \text{Activation}(j)|^{-1}$$

High similarity and similar activation levels cause interference. The system resolves interference by:
1. Retaining the memory with higher activation
2. Marking the lower-activation memory for potential pruning
3. Recording the interference event in the episodic ledger

### 7.2 Pruning Conditions

A node transitions from `WARM` to `EXPIRED` if:

$$A_i(t) < \theta_{\text{retention}} \quad\land\quad \text{has\_critical\_dependents}(i) = \text{False}$$

**Critical dependent check:** Before pruning, the system verifies that no other memory node has a hard dependency on the node being pruned. If critical dependents exist, the node is retained at WARM tier regardless of activation.

---

## 8. Consolidation & Offline Dream Cycle

During idle cognitive epochs (system maintenance mode), the consolidation engine executes:

### 8.1 Abstraction Phase

```yaml
abstraction:
  input: "Multiple episodic traces in HOT/WARM"
  method: "Schema induction from repeated patterns"
  output: "Unified procedural schemas in COLD"
  example: "10 episodes of 'writing test → running test → fixing bug' → schema: 'test-driven-development'"
```

### 8.2 Topological Healing Phase

```yaml
topological_healing:
  actions:
    - "Resolve broken wikilinks → update or remove"
    - "Reconcile duplicate entities → merge with provenance preservation"
    - "Update MOC indices → add new nodes, remove stale references"
    - "Validate graph connectivity → ensure no orphaned nodes"
```

### 8.3 Contradiction Resolution Phase

```yaml
contradiction_resolution:
  method: "SMT check on newly admitted claims against existing axioms"
  source: "01_CANON axioms + existing VALIDATED knowledge"
  on_contradiction:
    - "Move both claims to QUARANTINED"
    - "Record contradiction in provenance graph"
    - "Notify human steward for resolution"
  on_no_contradiction:
    - "Claims remain in current tier"
    - "Record validation receipt"
```

---

## 9. Cross-Vault References

- [[10_MEMORY/10_MEMORY_MOC|10_MEMORY_MOC]]
- [[10_MEMORY/EPISODIC_MEMORY_SUBSTRATE|EPISODIC_MEMORY_SUBSTRATE]]
- [[10_MEMORY/SEMANTIC_ASSOCIATIVE_GRAPH_SUBSTRATE|SEMANTIC_ASSOCIATIVE_GRAPH_SUBSTRATE]]
- [[10_MEMORY/MEMORY_MEMORY_CONTRACT|MEMORY_MEMORY_CONTRACT]]
- [[04_RUNTIME/CAUSAL_CONCURRENCY_MVCC|CAUSAL_CONCURRENCY_MVCC]]
- [[25_COGNITIVE_MATRIX/AMOS_COGNITIVE_ARCHITECTURE_MATRIX|Cognitive Architecture Matrix]] (L7 Memory × C6 Memory Plane)
- [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] — Forgetting follows governed rules, not arbitrary deletion
