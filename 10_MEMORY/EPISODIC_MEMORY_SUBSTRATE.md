---
title: 10_MEMORY — Episodic Memory Substrate
type: memory_substrate_specification
plane: 10_MEMORY
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - authoritative_AMOS_OS_structure
    - 00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE
    - 05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC
    - 10_MEMORY/10_MEMORY_MOC
    - 12_STATE/12_STATE_MOC
  scope: episodic_memory_governance
tags:
  - amos-os
  - memory
  - episodic-memory
  - ebbinghaus-curve
  - vector-search
  - hnsw
  - spatiotemporal-indexing
---

# Episodic Memory Substrate & Temporal Replay Engine

**Origin Architect & Steward:** Trang Phan
**Target AMOS Lineage:** v4.4
**Plane:** `10_MEMORY`
**Status:** `ACTIVE_SPECIFICATION`
**Epistemic Classification:** `AMOS_MODEL` / `DERIVED`

---

## 1. Executive Summary & 4-Tier Memory Strata

The **Episodic Memory Substrate** coordinates the persistent retention, consolidation, and associative recall of temporal agent experiences, causal decisions, environmental observations, and tool outcomes across the AMOS Full Brain OS.

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AMOS HIERARCHICAL MEMORY STRATA                          │
│                                                                             │
│  [Tier 0: Working Memory Buffer]                                            │
│  - Ring buffer in GPU/SRAM (< 32k tokens, access latency < 0.5 ms)          │
│                               │                                             │
│                               ▼                                             │
│  [Tier 1: Episodic Memory Substrate (This Plane)]                           │
│  - Causal event graphs, temporal traces, and multi-agent dialogue logs      │
│  - Ebbinghaus-Wiener decay & consolidation engine (latency < 2.5 ms)        │
│                               │                                             │
│                               ▼                                             │
│  [Tier 2: Semantic Knowledge Graph (11_KNOWLEDGE)]                          │
│  - Hyperbolic Lorentz embeddings, verified RSCF DAGs, ontology index        │
│                               │                                             │
│                               ▼                                             │
│  [Tier 3: Procedural Skill Archive (07_SKILLS)]                             │
│  - Compiled WASM binaries, proven workflows, and deterministic playbooks    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Nine-Part AMOS Control Contract

### 2.1 ROLE
Provides indexed, spatiotemporal episodic storage and associative replay for multi-agent reasoning traces, preventing amnesia while bounding memory volume through salience-driven decay.

### 2.2 INTERFACES
- `IEventLogger`: Streams atomic episodic frames into local append-only WAL buffers.
- `IRetrievalEngine`: Performs hybrid dense-sparse vector search across HNSW / DiskANN indexes.
- `IConsolidationScheduler`: Manages sleep-phase memory consolidation and hippocampal-neocortical replay.
- `IForgettingGovernor`: Prunes low-salience episodic frames according to the mathematical retention curve.

### 2.3 DEPENDENCIES
- `04_RUNTIME`: Session clocks and causal execution ticks.
- `05_COGNITIVE_ORGANISM`: Metacognitive attention and working memory controllers.
- `12_STATE`: Zero-copy Apache Arrow memory-mapped storage.
- `18_SECURITY`: AES-256-GCM / Post-Quantum encryption of private memory blocks.

### 2.4 INVARIANTS
1. **Append-Only Immutability**: Historical episodic logs are cryptographically sealed with BLAKE3 hash chains; past records cannot be edited in place.
2. **Epistemic Isolation**: Episodic memory stores *what occurred* (`OBSERVATION` / `EVENT`), which does not automatically confer *canonical truth* (`CANON` / `LAW`).
3. **Bounded Footprint**: Memory usage per agent is strictly bounded by active forgetting curves and compaction policies.

### 2.5 AUTHORITY
Governed by `AMOS_CORE v4.4`, origin architect **Trang Phan**.

### 2.6 PROVENANCE
Engineered from cognitive neurobiology (hippocampal replay), vector search architectures (HNSW / DiskANN), and Ebbinghaus memory dynamics.

### 2.7 TESTS
- Unit verification of Ebbinghaus-Wiener exponential decay calculations.
- Recall accuracy benchmarks under $10^6$ dense vector embeddings ($\text{Recall@10} \ge 98.2\%$).
- Disaster recovery and WAL replay integrity tests following simulated sudden power loss.

### 2.8 FAILURE MODES
- Storage quota saturation from high-frequency telemetry logging.
- Index fragmentation degrading retrieval latency.
- Corrupted embedding vector pointers.

### 2.9 RECOVERY
- Automated memory compaction: Spatiotemporal clustering merges similar low-salience episodes into summary nodes.
- Re-indexing of HNSW graphs in the background without blocking reads.

---

## 3. Mathematical Forgetting & Salience Retention Model

Memory retention probability $R(t)$ for an episodic frame $e$ at elapsed time $t$ follows the generalized Ebbinghaus-Wiener decay function:

$$R(t) = \exp\left( -\frac{t}{S(e)} \right)$$

where stability $S(e)$ is dynamically modulated by epistemic salience and cross-plane retrieval frequency:

$$S(e) = S_0 \cdot \left( 1 + \alpha \cdot \text{Salience}(e) \right)^{\beta \cdot \text{Rehearsals}(e)}$$

### Parameter Definitions:
- $S_0$: Baseline stability constant ($S_0 = 86,400\text{ seconds} \approx 24\text{ hours}$).
- $\text{Salience}(e) \in [0.0, 1.0]$: Epistemic entropy delta and task impact factor:
  $$\text{Salience}(e) = w_1 |\Delta \mathcal{H}_{\text{epistemic}}| + w_2 \cdot \text{Surprise}(e) + w_3 \cdot \text{RewardDelta}(e)$$
- $\text{Rehearsals}(e) \in \mathbb{N}$: Cumulative count of associative queries referencing episode $e$.
- $\alpha, \beta$: Hyperparameters calibrated to human memory consolidation benchmarks ($\alpha = 2.4$, $\beta = 1.15$).

---

## 4. Storage Schema & Serialization

### Episodic Frame JSON Schema:
```json
{
  "$schema": "https://amos-os.org/schemas/v4.4/episodic_trace.json",
  "episode_id": "EP-2026-0904-00128",
  "timestamp_iso": "2026-09-04T14:10:00Z",
  "causal_epoch": 4410,
  "salience_score": 0.94,
  "agent_id": "amos-epistemic-verifier-01",
  "trigger_event": "LEAN4_PROOF_VERIFICATION_PASS",
  "state_delta": {
    "hypotheses_validated": ["H-GKP-BOSONIC-01", "H-LORENTZ-02"],
    "epistemic_entropy_change": -0.48,
    "rscf_class_promoted": "DERIVED"
  },
  "context_snapshot": {
    "working_memory_hash": "a1b2c3d4e5f67890",
    "active_tools_invoked": ["lean4_check", "blake3_sign"]
  },
  "vector_embedding_ref": "emb://hnsw/shard-02/idx-94812",
  "blake3_receipt_hash": "7f8e9d0c1b2a34567890abcdef1234567890abcdef1234567890abcdef1234"
}
```

---

## 5. AMOS OS MECE Plane Integration

| AMOS Plane | Role & Responsibilities |
| :--- | :--- |
| **[[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME]]** | Provides execution timestamps and causal epoch clocks. |
| **[[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM]]** | Directs sleep-phase consolidation and working memory retrieval queries. |
| **[[10_MEMORY/10_MEMORY_MOC|10_MEMORY]]** | Core host plane managing physical vector databases, WAL logs, and decay timers. |
| **[[11_KNOWLEDGE/11_KNOWLEDGE_MOC|11_KNOWLEDGE]]** | Absorbs consolidated semantic claims into permanent knowledge graphs. |
| **[[12_STATE/12_STATE_MOC|12_STATE]]** | Zero-copy shared memory registers for fast episodic retrieval caching. |
| **[[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY]]** | Logs retrieval hit-rates, memory saturation, and consolidation metrics. |

---

## 6. Structural Invariants & Governance

1. **Deterministic Recall**: Identical query embeddings and filter predicates return identical candidate sets on a static snapshot.
2. **Privacy & Sandboxing**: Private agent thoughts are encrypted with shard-specific keys; cross-agent recall requires explicit capability delegation.
3. **No Unchecked Accumulation**: Total episodic storage volume is constrained to configured disk quotas; unreferenced episodes decay gracefully.
4. **Lineage**: Governed under AMOS v4.4; origin steward **Trang Phan**.

---

## 7. Cross-Plane References

- Memory MOC: [[10_MEMORY/10_MEMORY_MOC|10_MEMORY MOC]]
- Memory Contract: [[10_MEMORY/MEMORY_MEMORY_CONTRACT|MEMORY_MEMORY_CONTRACT]]
- Fractal Learning Engine: [[10_MEMORY/FRACTAL_LEARNING_AND_MEMORY_REDUCTION_ENGINE|Fractal Learning Engine]]
- Spintronic Synapse Monograph: [[10_MEMORY/SPINTRONIC_DOMAIN_WALL_AND_NEUROMORPHIC_CROSSBAR_MONOGRAPH|Spintronic Synapses]]
- Knowledge MOC: [[11_KNOWLEDGE/11_KNOWLEDGE_MOC|11_KNOWLEDGE MOC]]
