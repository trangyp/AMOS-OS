---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Intuition Engine
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

# Intuition Engine

> [!abstract] Engine Specification
> Defines the heuristic, pattern-recognition system for AMOS Full Brain OS — providing fast, frugal, recognition-primed decision-making that complements deliberative reasoning with experiential pattern matching.
> **Epistemic status:** AMOS_MODEL specification; not yet validated as empirical claim.

---

## 1. Purpose

The Intuition Engine implements **System-1-like processing** — fast, automatic, pattern-based cognitive shortcuts that provide rough-but-usable judgments without full deliberative analysis. In AMOS, intuition is not mystical; it is **statistical pattern recognition over accumulated experience**.

Key principle: **Intuitions are hypotheses, not conclusions.** They provide starting points for deliberation, not final answers.

---

## 2. Theoretical Foundation

### 2.1 Recognition-Primed Decision (RPD) Model

Based on Gary Klein's RPD model, the Intuition Engine operates in three modes:

```text
                    RECOGNITION-PRIMED DECISION FLOW
                    ════════════════════════════════════
                              │
                    ┌─────────┴─────────┐
                    │  PATTERN MATCH    │
                    │  (experience DB)  │
                    └─────────┬─────────┘
                              │
              ┌───────────────┼───────────────┐
              │               │               │
         NO MATCH       PARTIAL MATCH    STRONG MATCH
              │               │               │
              ↓               ↓               ↓
         DELIBERATE    ASK: "CAN I      PROCEED WITH
         (full         MAKE IT WORK?"    MATCHED
         reasoning)    (simulation)      PROCEDURE
              │               │               │
              ↓               ↓               ↓
         ┌────┴────┐    ┌────┴────┐    ┌────┴────┐
         │ UNPACK  │    │ TWEAK   │    │ EXECUTE │
         │ PROBLEM │    │ PROCEDURE│   │ DIRECTLY│
         └─────────┘    └─────────┘    └─────────┘
```

### 2.2 Heuristics Library

The engine maintains a library of **fast-and-frugal heuristics**:

| Heuristic | Strategy | Use Case | Accuracy |
| :--- | :--- | :--- | :--- |
| **Recognition** | If you recognize it, act on it | Familiar problems | High for experienced domains |
| **Take-the-Best** | Use first cue that discriminates | Multi-cue decisions | Good with limited time |
| **Recognition-Heuristic** | If one option is recognized and the other isn't, choose recognized | Paired comparisons | Surprisingly effective |
| **Fluency** | Prefer easily-processed options | Choice under uncertainty | Good for quality assessment |
| **Affect** | Use emotional tag as proxy for value | Risk assessment | Good for experienced risk |
| **1/N** | Equal allocation across options | Resource allocation | Robust against overfitting |

---

## 3. Pattern Recognition Architecture

### 3.1 Experience Database

The engine queries the episodic memory substrate for similar past situations:

$$\text{pattern\_match}(q, \mathcal{E}) = \arg\max_{e \in \mathcal{E}} \text{sim}(q, e)$$

Where:
- $q$: Current situation query vector
- $\mathcal{E}$: Experience database (episodic memory)
- $\text{sim}$: Similarity function (cosine, Jaccard, or domain-specific)

### 3.2 Confidence Estimation

Intuition confidence is based on experience density:

$$C_{\text{intuition}}(q) = \frac{|\{e \in \mathcal{E} : \text{sim}(q, e) > \theta_{\text{match}}\}|}{K}$$

Where $K$ is the normalization constant (expected experience density).

| Confidence Level | Threshold | Action |
| :--- | :--- | :--- |
| **HIGH** | $C > 0.8$ | Execute directly, monitor |
| **MEDIUM** | $0.5 < C \leq 0.8$ | Use as hypothesis, validate |
| **LOW** | $C \leq 0.5$ | Use as seed for deliberation only |

---

## 4. Intuition Modes

### 4.1 Hypothesis Generation Mode
- **Trigger:** Novel problem, no strong pattern match
- **Action:** Generate candidate solutions from partial matches
- **Output:** Ranked list of hypotheses for deliberative evaluation

### 4.2 Direct Execution Mode
- **Trigger:** Strong pattern match, high confidence
- **Action:** Execute matched procedure directly
- **Output:** Action execution + monitoring for anomalies

### 4.3 Simulation Mode
- **Trigger:** Partial match, medium confidence
- **Action:** Mentally simulate procedure in current context
- **Output:** Modified procedure or rejection

### 4.4 Blind Spot Detection Mode
- **Trigger:** Intuition contradicts deliberation
- **Action:** Flag for human review, preserve both interpretations
- **Output:** Competing hypotheses for resolution

---

## 5. Intuition-Deliberation Interface

```text
┌─────────────────────────────────────────────────────────┐
│                INTEGRATION PROTOCOL                      │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  INTUITION ──────→ "Here's my best guess" ──────→ DELIBERATION
│                                                         │
│  DELIBERATION ───→ "Check this pattern" ────────→ INTUITION
│                                                         │
│  CONFLICT ───────→ "Competing hypotheses" ─────→ HUMAN  │
│                                                         │
│  VALIDATION ─────→ "Confirm or update" ─────────→ MEMORY │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 5.1 When Intuition Leads
- Time-critical decisions (latency budget exceeded)
- Highly experienced domains (>100 similar past cases)
- Simple pattern matches (recognition threshold exceeded)

### 5.2 When Deliberation Leads
- Novel situations (no pattern match)
- High-stakes decisions (consequence severity > threshold)
- Conflicting intuitions (multiple strong matches)

---

## 6. Integration with Other Engines

### 6.1 Emotion Engine
- Positive valence → broader pattern acceptance (risk tolerance)
- Negative valence → narrower pattern matching (conservative)
- High arousal → faster pattern matching, lower confidence threshold

### 6.2 Instinct Engine
- Intuition can override instinct when context indicates false alarm
- Instincts can suppress intuition when survival is at stake
- Priority resolution: survival > efficiency > intuition

### 6.3 Causal Inference Engine
- Intuition provides candidate causal hypotheses
- Causal engine validates or rejects intuition's causal claims
- Reciprocal learning: validated intuitions become causal model priors

---

## 7. Configuration

```yaml
intuition_engine_config:
  enabled: true
  pattern_match_threshold: 0.7
  confidence_thresholds:
    high: 0.8
    medium: 0.5
    low: 0.3
  max_pattern_results: 10
  simulation_depth: 3
  conflict_detection: true
  blind_spot_detection: true
  learning_rate: 0.05
  experience_decay_rate: 0.01
  max_heuristics: 50
```

---

## 8. Failure Modes

| Failure Mode | Detection | Response |
| :--- | :--- | :--- |
| False pattern match | Deliberation rejects intuition | Record miss, tune similarity |
| Intuition fixation | Same pattern applied to novel contexts | Force deliberation override |
| Confidence inflation | High confidence but wrong answers | Recalibrate confidence function |
| Heuristic rigidity | Same heuristic always selected | Introduce stochastic selection |
| Experience contamination | Corrupted memories bias patterns | Memory quality filtering |

---

## 9. Epistemic Boundary

> [!warning] Heuristic Limitations
> The Intuition Engine provides **heuristic approximations**, not optimal solutions. It is subject to all known cognitive biases: availability bias, representativeness bias, anchoring, and confirmation bias. These are features (speed) and bugs (accuracy tradeoffs). Intuitions should always be validated for high-stakes decisions.

---

## 10. Cross-Vault References

- [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]]
- [[05_COGNITIVE_ORGANISM/EMOTION_ENGINE|EMOTION_ENGINE]]
- [[05_COGNITIVE_ORGANISM/INSTINCT_ENGINE|INSTINCT_ENGINE]]
- [[05_COGNITIVE_ORGANISM/CAUSAL_INFERENCE_ENGINE|CAUSAL_INFERENCE_ENGINE]]
- [[10_MEMORY/EPISODIC_MEMORY_SUBSTRATE|EPISODIC_MEMORY_SUBSTRATE]]
- [[10_MEMORY/SEMANTIC_ASSOCIATIVE_GRAPH_SUBSTRATE|SEMANTIC_ASSOCIATIVE_GRAPH_SUBSTRATE]]

---

RSCF-NODE

node_id: amos_05_cognitive_organism_intuition_engine
node_type: engine
path: 05_COGNITIVE_ORGANISM/INTUITION_ENGINE.md
claim_class: AMOS_MODEL
rscf_state: specification
canonical_status: SPECIFICATION_NOT_IMPLEMENTED

RSCF-RELATIONS:
- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- QUERIES: [[10_MEMORY/EPISODIC_MEMORY_SUBSTRATE|EPISODIC_MEMORY_SUBSTRATE]]
- INTEGRATES_WITH: [[05_COGNITIVE_ORGANISM/EMOTION_ENGINE|EMOTION_ENGINE]]
- INTEGRATES_WITH: [[05_COGNITIVE_ORGANISM/INSTINCT_ENGINE|INSTINCT_ENGINE]]
- INTEGRATES_WITH: [[05_COGNITIVE_ORGANISM/CAUSAL_INFERENCE_ENGINE|CAUSAL_INFERENCE_ENGINE]]

**MOC:** [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]]
