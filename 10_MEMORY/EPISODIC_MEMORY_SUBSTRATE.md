---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Episodic Memory Substrate
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

# Episodic Memory Substrate & Temporal Replay Engine

**Origin Architect / Steward:** Trang Phan
**AMOS_CORE Target:** `v4.4`
**Epistemic Class:** `AMOS_MODEL`

---

## 1. Cognitive Memory Architecture (4-Tier Strata)

The AMOS Memory Substrate coordinates multi-tiered storage spanning ultra-fast working contexts to permanent semantic/episodic graph embeddings:

| Tier | Name | Capacity | Latency | Persistence | Storage Medium |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tier 0** | Working Memory | $\le 32\text{k}$ tokens | $< 1\text{ ms}$ | Session-scoped | In-context ring buffer |
| **Tier 1** | Episodic Memory | Bounded by salience | $< 50\text{ ms}$ | Causal-epoch scoped | Structured event traces |
| **Tier 2** | Semantic Memory | Unbounded (graph) | $< 200\text{ ms}$ | Persistent | Vector graph (HNSW/DiskANN) |
| **Tier 3** | Procedural Memory | Unbounded (blueprints) | $< 100\text{ ms}$ | Persistent | Validated skill blueprints + WASM |

### 1.1 Tier 0: Working Memory

**Role**: Active cognitive context; what the system is "thinking about right now".

**Characteristics**:
- Ring buffer architecture; oldest entries evicted when capacity exceeded
- All active reasoning chains, current task context, and recent interactions
- No persistence across sessions (unless explicitly promoted to Tier 1)

**Eviction Policy**:
$$\text{Evict}(t) = \arg\min_{i \in \text{Buffer}} A_i(t)$$

Where $A_i(t)$ is the activation level from the tiered memory lifecycle model.

### 1.2 Tier 1: Episodic Memory

**Role**: Structured causal event traces with timestamps, agent decisions, and tool feedback.

**What gets stored**:
- Every significant interaction (task completion, decision, error, recovery)
- Agent reasoning chains (compressed)
- Tool invocation results
- Authority grants/revocations
- Knowledge promotion/retraction events

**Episode Structure**:

```yaml
episode:
  episode_id: "EP-2026-0904-001"
  timestamp_iso: "2026-09-04T10:30:00Z"
  causal_epoch: 4402
  episode_type: "task_completion"
  salience_score: 0.89
  
  participants:
    primary_agent: "AGT-RESEARCH-01"
    collaborating_agents: ["AGT-QFM-SPECIALIST-01"]
    tools_used: ["obsidian-read-tool", "web-search-tool"]
  
  state_delta:
    hypotheses_validated: ["H-OFI-01", "H-ROUGH-HESTON-02"]
    hypotheses_rejected: ["H-BLACK-SCHOLES-03"]
    epistemic_entropy_change: -0.42
    knowledge_promoted: ["KN-2026-09-04-001"]
    knowledge_retracted: []
  
  reasoning_trace:
    steps: 7
    inference_rules_used: ["modus_ponens", "bayesian_update"]
    proof_trails: ["PT-88412", "PT-88413"]
  
  tool_results:
    - tool: "web-search-tool"
      query: "rough heston model calibration 2026"
      results_count: 12
      relevance_score: 0.87
  
  authority_context:
    authority_token: "AUTH-GR-88912-EXP-20260904"
    scope: "22_RESEARCH/01_MATHEMATICS"
    expiry: "2026-09-04T11:00:00Z"
  
  vector_embedding_ref: "emb://hnsw/shard-04/idx-89410"
```

### 1.3 Tier 2: Semantic Memory

**Role**: Persistent knowledge graph; the long-term "understanding" of the system.

**Storage**: Dual representation (dense vectors + symbolic graph) as defined in `SEMANTIC_ASSOCIATIVE_GRAPH_SUBSTRATE`.

**Key difference from Tier 1**: Semantic memory stores **generalized knowledge** (concepts, relationships, rules), not specific events. An episodic trace of "calibrated Heston model on 2026-09-04" becomes semantic knowledge "Heston model calibration requires Rough process parameters."

### 1.4 Tier 3: Procedural Memory

**Role**: Validated skill execution blueprints and compiled routines.

**Contents**:
- Skill definitions (from `07_SKILLS`)
- Workflow templates (from `26_WORKFLOWS`)
- Compiled WASM routines for deterministic operations
- Optimized inference pipelines

---

## 2. Mathematical Forgetting & Retention Curve

Memory retention probability $R(t)$ for episode $e$ follows the generalized Ebbinghaus-Wiener decay function:

$$R(t) = \exp\left( -\frac{t}{S(e)} \right)$$

Where memory stability $S(e)$ is:

$$S(e) = S_0 \cdot (1 + \alpha \cdot \text{Salience}(e))^{\beta \cdot \text{Rehearsals}(e)}$$

| Parameter | Symbol | Description |
| :--- | :--- | :--- |
| Baseline stability | $S_0$ | Default retention half-life |
| Salience weight | $\alpha$ | How much epistemic importance boosts retention |
| Rehearsal multiplier | $\beta$ | How much each retrieval strengthens the memory |
| Salience | $\text{Salience}(e) \in [0, 1]$ | Epistemic entropy delta $\Delta H_{epistemic}$ |
| Rehearsals | $\text{Rehearsals}(e)$ | Number of successful cross-plane associative retrievals |

### 2.1 Retention Conditions

A memory transitions through lifecycle states based on $R(t)$:

| Condition | Lifecycle Transition |
| :--- | :--- |
| $R(t) > \theta_{\text{hot}}$ | Remains in current tier |
| $\theta_{\text{cold}} < R(t) \le \theta_{\text{hot}}$ | HOT → WARM → COLD promotion |
| $R(t) \le \theta_{\text{cold}}$ | COLD → EXPIRED (tombstone retained) |
| Contradiction detected | Any tier → QUARANTINED |
| TTL expired | Any tier → EXPIRED |

---

## 3. Temporal Replay Engine

During idle cognitive epochs (system maintenance mode), the temporal replay engine executes:

### 3.1 Episode Compression

```text
MULTIPLE EPISODES
    │
    ▼
┌─────────────────────────┐
│ PATTERN DETECTION       │  ← Identify recurring structures
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ ABSTRACTION             │  ← Compress episodes into schemas
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ SCHEMA PROMOTION        │  ← Promote to semantic memory (Tier 2)
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ EPISODE ARCHIVAL        │  ← Original episodes compressed/archived
└─────────────────────────┘
```

### 3.2 Topological Healing

- Resolves broken wikilinks across the knowledge graph
- Reconciles duplicate entities (same concept, different names)
- Updates MOC indices to reflect current state
- Repairs inconsistent cross-references

### 3.3 Contradiction Resolution

- Runs SMT checks on newly admitted claims against existing axioms in `01_CANON`
- Identifies dormant contradictions (claims that contradicted but were never detected)
- Quarantines affected claims; triggers re-evaluation

---

## 4. Storage Schema & Serialization

```json
{
  "$schema": "https://amos-os.org/schemas/v4.4/episodic_trace.json",
  "episode_id": "EP-2026-0904-001",
  "timestamp_iso": "2026-09-04T10:30:00Z",
  "causal_epoch": 4402,
  "salience_score": 0.89,
  "agent_id": "AGT-RESEARCH-01",
  "episode_type": "task_completion",
  "state_delta": {
    "hypotheses_validated": ["H-OFI-01", "H-ROUGH-HESTON-02"],
    "epistemic_entropy_change": -0.42,
    "knowledge_promoted": ["KN-2026-09-04-001"]
  },
  "reasoning_trace": {
    "steps": 7,
    "inference_rules": ["modus_ponens", "bayesian_update"],
    "proof_trails": ["PT-88412"]
  },
  "retention_metadata": {
    "stability": 0.82,
    "rehearsals": 3,
    "last_accessed": "2026-09-04T10:30:00Z",
    "access_count": 5
  },
  "vector_embedding_ref": "emb://hnsw/shard-04/idx-89410",
  "compression_state": "UNCOMPRESSED",
  "linked_episodes": ["EP-2026-0903-042", "EP-2026-0904-002"]
}
```

---

## 5. Integration Points

| Interface | Direction | Contract |
| :--- | :--- | :--- |
| **04_RUNTIME** | Write | Session events → episodic traces |
| **02_KERNEL** | Read | Proof trails; reasoning chains |
| **11_KNOWLEDGE** | Read/Write | Semantic memory promotion; knowledge graph updates |
| **12_STATE** | Read/Write | Runtime state snapshots; epoch context |
| **05_COGNITIVE_ORGANISM** | Read | Consciousness engine state; emotion engine traces |
| **15_INTERFACES** | Write | BCI neural state vectors |
| **17_OBSERVABILITY** | Write | Memory health; retention statistics |

---

## 6. Failure Modes

| Failure | Detection | Recovery |
| :--- | :--- | :--- |
| **Working memory overflow** | Buffer capacity exceeded | Evict lowest-activation entries; log eviction |
| **Episodic trace corruption** | Hash verification failure | Reconstruct from backup; quarantine corrupted trace |
| **Forgetting curve miscalibration** | Retention statistics deviate from expected | Recalibrate $S_0$, $\alpha$, $\beta$ parameters |
| **Replay engine stall** | Maintenance epoch timeout | Skip current replay cycle; log incomplete replay |
| **Cross-tier inconsistency** | Semantic-episodic contradiction detection | Quarantine both; trigger re-evaluation |

---

## 7. Cross-Vault References

- [[10_MEMORY/10_MEMORY_MOC|10_MEMORY_MOC]]
- [[10_MEMORY/TIERED_MEMORY_LIFECYCLE_ARCHITECTURE|TIERED_MEMORY_LIFECYCLE_ARCHITECTURE]]
- [[10_MEMORY/SEMANTIC_ASSOCIATIVE_GRAPH_SUBSTRATE|SEMANTIC_ASSOCIATIVE_GRAPH_SUBSTRATE]]
- [[04_RUNTIME/CAUSAL_CONCURRENCY_MVCC|CAUSAL_CONCURRENCY_MVCC]]
- [[12_STATE/12_STATE_MOC|12_STATE_MOC]]

---

```RSCF-NODE
node_id: episodic_memory_substrate
node_type: memory_specification
domain: 10_MEMORY
claim_class: AMOS_MODEL
confidence_ceiling:
  architecture_design: high
  forgetting_curve_model: medium
  consolidation_engine: medium
falsifiers:
  - Retention curve fails to predict actual recall accuracy
  - Temporal replay introduces inconsistencies into semantic memory
  - Working memory eviction removes critical active context
```
