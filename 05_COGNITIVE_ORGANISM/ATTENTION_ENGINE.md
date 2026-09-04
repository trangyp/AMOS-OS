---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Attention Engine
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

# Attention Engine — Cognitive Organism

> **Status:** `ACTIVE_SPECIFICATION` · **AMOS Core target:** `v4.4`  
> **Origin architect / steward:** Trang Phan  
> **Functional Group:** `A. INPUT / REPRESENTATION` (MECE Partition)  
> **Conclusion class:** `AMOS_MODEL`

---

## 1. Architectural Purpose & Role

The **Attention Engine** governs the dynamic allocation of finite cognitive capacity, context window budget, and computational priority across competing perceptual signals, retrieved evidence, and active hypotheses within `05_COGNITIVE_ORGANISM`.

Operating directly downstream from the [Perception Engine](file:///Users/mac/Documents/AMOS_OS/05_COGNITIVE_ORGANISM/PERCEPTION_ENGINE.md) and upstream from the [Cognition Engine](file:///Users/mac/Documents/AMOS_OS/05_COGNITIVE_ORGANISM/COGNITION_ENGINE.md), its role is to prevent cognitive saturation by filtering, weighting, and routing only decision-critical tokens into working memory.

```text
PERCEPTUAL INPUTS & SIGNALS
            ↓
┌───────────────────────────────────────┐
│           ATTENTION ENGINE            │
│  - Salience Scoring                   │
│  - Context Budgeting & Compaction     │
│  - Information Entropy Filtering      │
└───────────────────────────────────────┘
            ↓
FOCUSED ATTENTION VECTOR / BUDGET
            ↓
COGNITION & REASONING ENGINES
```

---

## 2. Mathematical & Algorithmic Formulation

### 2.1 Attention Priority Equation
The attention priority metric $A_p(s)$ for any candidate token, fact, or signal $s$ is computed as:

$$A_p(s) = w_g \cdot G_r(s) + w_c \cdot C_q(s) + w_u \cdot U(s) + w_i \cdot I_r(s) + w_t \cdot T_s(s) - w_d \cdot D_k(s)$$

Where:
* $G_r(s) \in [0, 1]$: Goal relevance given active task envelope.
* $C_q(s) \in [0, 1]$: Consequence severity if $s$ is omitted or false.
* $U(s) \in [0, 1]$: Epistemic uncertainty associated with $s$.
* $I_r(s) \in [0, 1]$: Irreversibility factor of actions conditioned on $s$.
* $T_s(s) \in [0, 1]$: Time-decay sensitivity and urgency.
* $D_k(s) \in [0, 1]$: Redundancy / duplicate knowledge penalty (Sybil discount).
* $\sum w_i = 1$: Governed weighting parameters set by active control-plane regime.

### 2.2 Context Budget Allocation & Retention Ranking
When context budget capacity $B_{max}$ is approached, attention executes strict priority compaction following the canonical retention hierarchy:

$$\text{Hard Constraints} \succ \text{Critical Falsifiers} \succ \text{Active Contradictions} \succ \text{Current Decisions} \succ \text{Provenance Roots} \succ \text{Narrative Detail}$$

---

## 3. Hard Architectural Invariants

```text
SALIENCE != TRUTH
THREAT_SIGNAL != FACT
NOVELTY != RELEVANCE
HIGH_WEIGHT != HIGH_AUTHORITY
ATTENTION_FOCUS != COMMITMENT
```

1. **Anti-Hallucination Gate:** An emotionally intense or salient signal must never be promoted from hypothesis to observation merely due to high attention weighting.
2. **Deterministic Pruning:** Compaction must preserve causal lineage and provenance roots. Pruned tokens are archived, never destroyed silently.
3. **Fail-Closed on Saturation:** If $A_p(s)$ cannot be resolved under resource constraints, the engine signals `LOAD_SHEDDING` to [Homeostasis Engine](file:///Users/mac/Documents/AMOS_OS/05_COGNITIVE_ORGANISM/HOMEOSTASIS_ENGINE.md).

---

## 4. Grounding in Arvix Research Corpus

The Attention Engine is grounded in foundational and empirical literature cataloged in the [Arvix Research Corpus](file:///Users/mac/Desktop/_Arxiv/Arvix):

1. **Sublinear Approximation & Sparsification:**
   * Grounded in [[2602.00874v1_Sublinear_Time_Quantum_Algorithm_for_Attention_Approximation]]: Quantum and randomized sublinear algorithms for sparse attention matrices, enabling $O(d \log n)$ attention scaling over massive corpora without token loss.
2. **Cortical Information Integration & Gating:**
   * Grounded in [[1012.5649v1_Network_algorithmics_and_the_emergence_of_information_integration_in_cortical_mo]]: Explores network algorithmics and information integration in cortical modules, defining how hierarchical loops prevent runaway feedback while preserving local receptive field sensitivity.
3. **Cross-Year Cognitive Synthesis:**
   * Grounded in [[outputs/Consciousness_Early_Thread_2007-2010]]: Synthesizes the state-vs-integration split across early cognitive papers, establishing that selective attention is the prerequisite for coherent information integration.

---

## 5. Input / Output Contracts & Typed Interfaces

### 5.1 Input Contract
```yaml
attention_request:
  candidate_signals:
    - signal_id: string
      modality: "TEXT | METRIC | GRAPH_EDGE | TEMPORAL_DELTA"
      raw_payload: any
      source_provenance: string
      initial_uncertainty: float
  active_goal_envelope:
    goal_id: string
    hard_constraints: list[string]
    temporal_deadline: timestamp
  available_budget:
    max_tokens: int
    compute_cycles: int
```

### 5.2 Output Contract
```yaml
attention_output:
  attended_vector:
    - signal_id: string
      attention_score: float
      assigned_layer: "WORKING_MEMORY | HYPOTHESIS_SPACE | SNOOZED"
      justification: string
  suppressed_signals: list[string]
  compaction_receipt:
    tokens_allocated: int
    tokens_shed: int
    integrity_verified: bool
```

---

## 6. Cross-Plane & Upstream / Downstream Bindings

* **Governing Canon:** [[01_CANON/03_COGNITION_CANON/COGNITIVE_ORGANISM_CANON|COGNITIVE_ORGANISM_CANON]]
* **Upstream Feeder:** [[05_COGNITIVE_ORGANISM/PERCEPTION_ENGINE|PERCEPTION_ENGINE]]
* **Downstream Consumers:** [[05_COGNITIVE_ORGANISM/COGNITION_ENGINE|COGNITION_ENGINE]] · [[05_COGNITIVE_ORGANISM/MEMORY_ENGINE|MEMORY_ENGINE]]
* **Regulatory Monitor:** [[05_COGNITIVE_ORGANISM/HOMEOSTASIS_ENGINE|HOMEOSTASIS_ENGINE]] (receives context load telemetry)
* **Master Index:** [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]] · [[00_ROOT/00_HOME|00_HOME]]

---
RSCF-NODE
node_id: amos_05_cognitive_organism_attention_engine
node_type: engine
path: 05_COGNITIVE_ORGANISM/ATTENTION_ENGINE.md
claim_class: AMOS_MODEL
RSCF-RELATIONS:
  - GOVERNED_BY: [[01_CANON/03_COGNITION_CANON/COGNITIVE_ORGANISM_CANON]]
  - INDEXED_BY: [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC]]
  - INDEXED_BY: [[00_ROOT/00_HOME]]
  - FEEDS: [[05_COGNITIVE_ORGANISM/COGNITION_ENGINE]]
  - MONITORED_BY: [[05_COGNITIVE_ORGANISM/HOMEOSTASIS_ENGINE]]
