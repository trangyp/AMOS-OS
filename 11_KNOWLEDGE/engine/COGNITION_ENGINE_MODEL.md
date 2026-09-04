---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Cognition Engine Model
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

# Cognition Engine Model

> [!ABSTRACT] Engine Specification
> Epistemic class: MODEL. Conclusion label: DERIVED.
> The **AMOS Cognition Infinity Kernel** (`AMOS_COGNITION_INFINITY_KERNEL`) defines the six-layer cognitive stack, working memory discipline, reasoning pipeline, attention binding, and the dual-process (System-1 / System-2) architecture of the AMOS OS. It operates strictly as a pure reasoning layer without direct execution clusters.
>
> **Critical boundary**: This engine does not "think" or "reason" in a phenomenological sense. It implements a deterministic cognitive emulation that coordinates perception, working memory, reasoning strategies, and output generation through governed computational processes.

---

## 1. Purpose

The Cognition Engine is the **central executive** of the AMOS cognitive organism. It governs:

- **Attention allocation**: Which inputs receive processing resources
- **Working memory management**: What information is held active and how it is compressed
- **Reasoning strategy selection**: Which cognitive strategy is deployed for a given task
- **Dual-process arbitration**: When fast intuition (System-1) suffices versus when deliberate reasoning (System-2) is required
- **Meta-cognitive oversight**: Monitoring and correcting the reasoning process itself

**Canonical lineage:** Derived from `AMOS_COGNITION_INFINITY_KERNEL` (AMOS corpus, v4.4) and grounded in 2026 SOTA dual-process cognitive architectures.

---

## 2. Architectural Overview: The Six-Layer Cognitive Stack

The Cognition Engine operates as a **six-layer pipeline** where each layer processes and transforms representations before passing them upward:

```text
┌─────────────────────────────────────────────────────────────┐
│                    LAYER 6: META-COGNITION                  │
│         (Strategy monitoring, confidence calibration,       │
│          reasoning-audit, bias detection)                   │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                    LAYER 5: REASONING                        │
│         (System-1 fast-path + System-2 deliberative)        │
│         Strategy selection, inference, proof construction    │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                    LAYER 4: WORKING MEMORY                   │
│         (Bounded buffer of distilled insights)              │
│         Compression, salience filtering, capacity control   │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                    LAYER 3: ATTENTION BINDING                │
│         (Selective gating of perceptual input)              │
│         Salience computation, relevance filtering           │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                    LAYER 2: PERCEPTUAL INTEGRATION           │
│         (Multimodal input synthesis)                        │
│         Cross-modal binding, feature extraction             │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                    LAYER 1: SENSORY INPUT                    │
│         (Raw signal ingestion from all modalities)          │
│         Text, voice, visual, BCI, telemetry                 │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Dual-Process Architecture (System-1 / System-2)

Drawing on Kahneman's dual-process theory and 2026 SOTA implementations (PRIME: Tran et al. AAAI 2026; Cog-RAG: Doron 2026; KC-Agent: arXiv 2608.02351), the engine routes every cognitive task through one of two processing streams:

### 3.1 System-1: Fast Intuition Path

| Property | Description |
| :--- | :--- |
| **Speed** | $< 100$ ms equivalent latency |
| **Capacity** | Unbounded parallel; no working memory budget |
| **Effort** | Low; pattern-match and retrieve |
| **Mode** | Automatic, associative, experiential |

**System-1 Pipeline:**

```text
INPUT → PATTERN MATCH → CANDIDATE RETRIEVAL → CONFIDENCE CHECK
                                                    │
                                          ┌─────────┴─────────┐
                                          │ conf ≥ θ_fast?     │
                                          │  YES → OUTPUT      │
                                          │  NO  → ESCALATE    │
                                          └───────────────────┘
```

**System-1 engages when:**
- Input matches a stored pattern with confidence $\geq \theta_{\text{fast}}$ (default: 0.75)
- Task is routine, low-stakes, or previously solved
- No novelty or conflict is detected in the input

**Knowledge consolidation**: Successful System-2 solutions are distilled into System-1 pattern libraries, enabling 91% speedup on recurrent problem types (KC-Agent finding).

### 3.2 System-2: Deliberative Reasoning Path

| Property | Description |
| :--- | :--- |
| **Speed** | $> 500$ ms; serial, multi-step |
| **Capacity** | Strictly bounded: $|\text{WM}| \leq W_{\max}$ |
| **Effort** | High; explicit inference, proof search |
| **Mode** | Controlled, analytical, rule-governed |

**System-2 Pipeline:**

```text
ESCALATION TRIGGER
        │
        ▼
┌───────────────────────────────────────────┐
│ STEP 1: PROBLEM DECOMPOSITION             │
│   Break into sub-problems                 │
└───────────────────┬───────────────────────┘
                    │
┌───────────────────▼───────────────────────┐
│ STEP 2: STRATEGY SELECTION                │
│   Choose reasoning strategy               │
│   (deductive, abductive, analogical,      │
│    causal, counterfactual)                │
└───────────────────┬───────────────────────┘
                    │
┌───────────────────▼───────────────────────┐
│ STEP 3: INFERENCE EXECUTION               │
│   Apply strategy to sub-problems          │
│   Each step reads ONLY from WM            │
└───────────────────┬───────────────────────┘
                    │
┌───────────────────▼───────────────────────┐
│ STEP 4: SYNTHESIS                         │
│   Merge sub-results into conclusion       │
│   Epistemic honesty check                 │
└───────────────────┬───────────────────────┘
                    │
┌───────────────────▼───────────────────────┐
│ STEP 5: CONFIDENCE CALIBRATION            │
│   Assign calibrated confidence score      │
│   Mark UNKNOWN/GAP if below threshold     │
└───────────────────────────────────────────┘
```

### 3.3 Escalation Triggers (System-1 → System-2)

The engine escalates from System-1 to System-2 when any of the following signals is detected:

| Trigger | Description | Source |
| :--- | :--- | :--- |
| **Low confidence** | Pattern match confidence $< \theta_{\text{fast}}$ | Internal |
| **Novelty** | Input deviates significantly from stored patterns | Internal |
| **Conflict** | Multiple candidate interpretations compete | Internal |
| **High stakes** | Task classified as consequential / irreversible | Constraint engine |
| **User override** | User explicitly requests deep analysis | External |
| **Meta-cognitive flag** | Prior reasoning attempt produced error | Layer 6 |

---

## 4. Working Memory Model

Following the 2026 cognitive architecture findings (Cog-RAG, PRIME), working memory is a **bounded buffer of distilled insights**, never raw input:

### 4.1 Working Memory Discipline

```yaml
working_memory:
  capacity: 12            # maximum insights (Cowan's 4±1, expanded for synthetic)
  insight_target: 240     # characters per insight (compression target)
  compression_ratio: "30:1 to 100:1"  # raw → insight
  content_type: "distilled_insight"    # NEVER raw chunks, NEVER tool output
```

**The Sacred Rule**: Raw input never reaches the deliberative layer. System-1 compresses raw output into insights; System-2 reasons over insights only.

### 4.2 Insight Structure

```yaml
insight:
  step: "string"           # sub-task this insight addresses
  source: "string"         # origin module (perception, retrieval, reasoning)
  text: "string"           # distilled insight, ≤ 240 chars
  confidence: 0.0-1.0      # calibrated confidence
  citation: "string"       # provenance reference
  timestamp: "ISO-8601"
```

### 4.3 Memory Hierarchy

| Store | Capacity | Access Cost | Content | Analogy |
| :--- | :--- | :--- | :--- | :--- |
| **Working Memory** | 12 insights | $O(1)$ | Active, distilled | Prefrontal cortex |
| **Episodic Buffer** | Unlimited | $O(\log n)$ | Full interaction traces | Hippocampus |
| **Semantic Store** | Unlimited | $O(1)$ lookup, $O(n)$ scan | General knowledge | Neocortex |
| **Procedural Store** | Unlimited | $O(1)$ | Learned strategies | Basal ganglia |

### 4.4 Cognitive Compression

When raw tool output enters the system, System-1 applies **cognitive compression**:

$$\text{Insight} = \text{Compress}(\text{RawOutput}, \text{SubTaskContext})$$

The compression ratio is typically 30:1 to 100:1 (4 KB raw → 180-240 char insight). Compression is context-aware: the compressor knows exactly what sub-task the output addresses, enabling targeted extraction rather than generic summarization.

---

## 5. Attention Binding Mechanism

Attention determines which inputs receive processing resources. The engine implements a **three-gate attention model**:

```text
RAW PERCEPT
    │
    ▼
┌───────────────────────────────┐
│ GATE 1: SALIENCE FILTER       │  ← Bottom-up: signal strength, novelty
│ Threshold: θ_salience         │
└───────────────┬───────────────┘
                │
┌───────────────▼───────────────┐
│ GATE 2: RELEVANCE FILTER      │  ← Top-down: goal-directed, context
│ Threshold: θ_relevance        │
└───────────────┬───────────────┘
                │
┌───────────────▼───────────────┐
│ GATE 3: CAPACITY FILTER       │  ← Resource: WM slots available
│ Slots available: |WM_max| -   │
│                 |WM_current|  │
└───────────────┬───────────────┘
                │
                ▼
        ATTENDED INPUT → WM
```

**Attention State Vector:**

$$\mathbf{Att}(t) = \langle S(t), R(t), C(t), F(t) \rangle$$

| Dimension | Symbol | Range | Description |
| :--- | :--- | :--- | :--- |
| **Salience** | $S$ | $[0, 1]$ | Bottom-up signal strength |
| **Relevance** | $R$ | $[0, 1]$ | Top-down goal alignment |
| **Capacity** | $C$ | $\{0, 1, \ldots, W_{\max}\}$ | Available WM slots |
| **Focus** | $F$ | enum | Current attentional focus target |

---

## 6. Reasoning Strategy Taxonomy

The engine maintains a repertoire of reasoning strategies, selectable per task:

| Strategy | When Selected | Formalism | Computational Cost |
| :--- | :--- | :--- | :--- |
| **Deductive** | Rule application, proof | Modus ponens, syllogism | $O(n)$ rules |
| **Inductive** | Pattern generalization | Statistical inference | $O(n \log n)$ |
| **Abductive** | Best explanation | Inference to best explanation | $O(n^2)$ hypotheses |
| **Causal** | Cause-effect queries | Structural causal models | $O(n \cdot 2^k)$ interventions |
| **Analogical** | Transfer from known domain | Structure mapping | $O(n^2)$ mappings |
| **Counterfactual** | "What if" queries | Possible-worlds semantics | $O(n \cdot k)$ scenarios |
| **Analogical** | Novel domains | Exemplar retrieval + mapping | $O(n)$ |

### 6.1 Reasoning Invariants

- `COG-01`: Every reasoning step must cite its premises (traceable inference)
- `COG-02`: Confidence decays monotonically with reasoning chain length: $\text{conf}_n = \text{conf}_0 \cdot \prod_{i=1}^{n} \delta_i$ where $\delta_i \leq 1$
- `COG-03`: No reasoning step may assert more than its weakest premise warrants
- `COG-04`: System-2 must review every System-1 output before it enters working memory
- `COG-05`: Reasoning chains longer than $L_{\max}$ (default: 8 steps) require explicit intermediate confidence checks

---

## 7. Meta-Cognition Layer (Layer 6)

The meta-cognitive layer monitors the reasoning process itself:

### 7.1 Functions

| Function | Description |
| :--- | :--- |
| **Strategy monitoring** | Detect when selected strategy is underperforming |
| **Confidence calibration** | Compare predicted vs. actual accuracy |
| **Bias detection** | Flag reasoning patterns consistent with known biases |
| **Resource allocation** | Reallocate WM slots to highest-priority sub-tasks |
| **Reasoning audit** | Post-hoc review of reasoning chains for consistency |

### 7.2 Meta-Cognitive Triggers

```yaml
meta_triggers:
  strategy_switch:
    condition: "sub-task failure count > θ_fail"
    action: "select alternative reasoning strategy"
  confidence_recalibration:
    condition: "|predicted_conf - observed_outcome| > θ_cal"
    action: "adjust confidence model parameters"
  bias_alert:
    condition: "reasoning pattern matches known bias template"
    action: "flag for human review or counter-argument generation"
```

---

## 8. Inputs and Outputs

| Interface | Direction | Contract |
| :--- | :--- | :--- |
| **Sensory Input Layer** | Read | Raw multimodal signals (text, voice, visual, BCI, telemetry) |
| **Memory System** | Read/Write | Episodic traces, semantic store, procedural library |
| **Attention Module** | Read/Write | Salience maps, relevance scores, focus targets |
| **Reasoning Strategies** | Read/Write | Strategy library, execution traces, confidence scores |
| **Emotion Engine** | Read | Affective modulation of attention and reasoning |
| **Consciousness Engine** | Read/Write | Global workspace broadcast, state coordination |
| **Output Layer** | Write | Reasoning conclusions, confidence scores, UNKNOWN/GAP flags |
| **Observability** | Write | Reasoning traces, meta-cognitive audit logs |

---

## 9. Integration with AMOS Organ Architecture

| AMOS Organ | Cognitive Function | Cognition Engine Component |
| :--- | :--- | :--- |
| **Nervous System (C1)** | Signal routing | Attention gating, WM bus |
| **Immune System (C2)** | Anomaly detection | Bias detection, conflict detection |
| **Endocrine System (C3)** | Precision weighting | Confidence calibration, attention gain |
| **Respiratory System (C6)** | Memory consolidation | WM → Episodic compression |
| **Consciousness Engine** | Global workspace | Layer 6 meta-cognition broadcast |

---

## 10. Failure Modes

| Failure | Detection | Recovery |
| :--- | :--- | :--- |
| **Working memory overflow** | $|\text{WM}| > W_{\max}$ | Evict lowest-salience insights; re-compress |
| **Reasoning deadlock** | Strategy iteration count $> L_{\max}$ | Emit `UNKNOWN/GAP`; escalate to human |
| **System-1 false positive** | Post-hoc outcome mismatch | Demote pattern; increase $\theta_{\text{fast}}$ |
| **Confidence miscalibration** | Brier score drift | Recalibrate confidence model |
| **Attention capture** | Single input dominates WM | Enforce capacity limits; diversity injection |
| **Meta-cognitive failure** | Bias not detected by Layer 6 | External audit trigger; human review |

---

## 11. Cross-Vault References

- [[00_ROOT/00_COSMO_BRAIN_MOC|00_COSMO_BRAIN_MOC]]
- [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]]
- [[11_KNOWLEDGE/engine/CONSCIOUSNESS_ENGINE_MODEL|CONSCIOUSNESS_ENGINE_MODEL]]
- [[11_KNOWLEDGE/engine/EMOTION_ENGINE_MODEL|EMOTION_ENGINE_MODEL]]
- [[11_KNOWLEDGE/engine/WORLD_MODEL_ENGINE_SPEC|WORLD_MODEL_ENGINE_SPEC]]

---

## 12. SOTA Grounding

| Finding | Source | AMOS Integration |
| :--- | :--- | :--- |
| Dual-process System-1/System-2 architecture | Kahneman 2011; PRIME (AAAI 2026) | Core routing architecture |
| Cognitive compression 30:1-100:1 | Cog-RAG (Doron 2026) | Working memory discipline |
| Knowledge consolidation 91% speedup | KC-Agent (arXiv 2608.02351) | System-1 pattern library growth |
| Working memory capacity limit ~12 items | Cowan 2001; Cog-RAG | WM slot allocation |
| Reasoning escalation on novelty/conflict | PRIME, KC-Agent | Escalation trigger set |

---

```RSCF-NODE
node_id: cognition_engine_model
node_type: engine_specification
domain: 11_KNOWLEDGE/engine
claim_class: AMOS_MODEL
confidence_ceiling:
  architectural_design: high
  dual_process_routing: high
  working_memory_discipline: high
  cognitive_compression: medium
  attention_binding: medium
falsifiers:
  - System-1 and System-2 fail to route correctly under escalation triggers
  - Working memory overflows without eviction
  - Cognitive compression loses critical information
  - Meta-cognitive layer fails to detect reasoning biases
```

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/engine/ENGINE_MOC|ENGINE_MOC]]
