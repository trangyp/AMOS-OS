---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Metacognitive Engine
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

# Metacognitive Engine

> [!abstract] Engine Specification
> Defines the self-monitoring, self-evaluating, and self-regulating layer for AMOS Full Brain OS — enabling the system to observe its own cognitive processes, assess confidence, detect errors, and adapt strategies.
> **Epistemic status:** AMOS_MODEL specification; not yet validated as empirical claim.

---

## 1. Purpose

The Metacognitive Engine implements **cognition about cognition** — the system's ability to monitor, evaluate, and regulate its own thinking processes. This is what enables AMOS to:

- **Know what it knows** (and doesn't know)
- **Detect when it's confused** or uncertain
- **Adapt its processing strategy** based on task demands
- **Learn from its own errors** and adjust

Metacognition is not a luxury — it is essential for bounded intelligence operating in open-world domains.

---

## 2. Metacognitive Architecture

```text
                    METACOGNITIVE ARCHITECTURE
                    ════════════════════════════
                              │
         ┌────────────────────┼────────────────────┐
         │                    │                    │
    KNOWLEDGE              MONITORING           CONTROL
    MONITORING             SUBSYSTEM            SUBSYSTEM
         │                    │                    │
    ┌────┴────┐          ┌────┴────┐          ┌────┴────┐
    │ What    │          │ How     │          │ When to │
    │ do I    │          │ well am  │          │ change  │
    │ know?   │          │ I doing? │          │ strategy│
    └─────────┘          └─────────┘          └─────────┘
```

### 2.1 Knowledge Monitoring (Knowing What You Know)

Tracks the system's **epistemic state** across all knowledge domains:

| Dimension | Metric | Range |
| :--- | :--- | :--- |
| **Coverage** | Fraction of domain covered by knowledge base | [0, 1] |
| **Confidence** | Average confidence of knowledge claims | [0, 1] |
| **Freshness** | Recency of knowledge updates | [0, 1] |
| **Consistency** | Fraction of non-contradictory claims | [0, 1] |
| **Source Quality** | Fraction of claims with verified provenance | [0, 1] |

**Knowledge State Vector:**

$$\mathbf{K}_d = [C_d, \text{Conf}_d, F_d, \text{Cons}_d, Q_d]$$

For domain $d$.

### 2.2 Performance Monitoring (Knowing How Well You're Doing)

Real-time tracking of cognitive process quality:

| Metric | Computation | Use |
| :--- | :--- | :--- |
| **Accuracy** | Correct outputs / total outputs | Overall quality |
| **Efficiency** | Useful work / total compute | Resource optimization |
| **Consistency** | Same input → same output rate | Reliability |
| **Latency** | Response time vs. target | SLA compliance |
| **Error Rate** | Errors / total operations | Quality trend |

### 2.3 Strategy Control (Knowing When to Change)

Based on monitoring signals, the engine triggers strategy transitions:

```text
PERFORMANCE DEGRADATION DETECTED
    ↓
┌─────────────────────────────────────┐
│ 1. DIAGNOSE: What went wrong?       │
│ 2. PRESCRIBE: What should change?   │
│ 3. IMPLEMENT: Apply new strategy    │
│ 4. MONITOR: Did it help?            │
└─────────────────────────────────────┘
```

---

## 3. Confidence Calibration

### 3.1 Expected Calibration Error (ECE)

The engine monitors its own calibration using Expected Calibration Error:

$$\text{ECE} = \sum_{b=1}^{B} \frac{|n_b|}{n} \cdot |\text{acc}(b) - \text{conf}(b)|$$

Where:
- $B$: Number of confidence bins
- $n_b$: Number of samples in bin $b$
- $\text{acc}(b)$: Accuracy in bin $b$
- $\text{conf}(b)$: Average confidence in bin $b$

Target: $\text{ECE} < 0.05$ (well-calibrated).

### 3.2 Calibration Actions

| ECE Level | Action |
| :--- | :--- |
| $\text{ECE} < 0.03$ | Excellent — no adjustment |
| $0.03 \leq \text{ECE} < 0.08$ | Good — monitor closely |
| $0.08 \leq \text{ECE} < 0.15$ | Fair — apply Platt scaling |
| $\text{ECE} \geq 0.15$ | Poor — recalibrate + reduce confidence |

---

## 4. Error Detection Patterns

### 4.1 Internal Consistency Checks

```yaml
consistency_checks:
  - name: "Self-contradiction"
    pattern: "Claim A and Claim ¬A both asserted"
    response: "Flag for resolution, quarantine"
    
  - name: "Circular reasoning"
    pattern: "Claim A supports Claim B which supports Claim A"
    response: "Flag as potential circularity"
    
  - name: "Stale reference"
    pattern: "Referenced entity no longer exists"
    response: "Update or remove reference"
    
  - name: "Scope violation"
    pattern: "Claim extends beyond evidence domain"
    response: "Add scope limitation annotation"
```

### 4.2 Process Monitoring Signals

| Signal | Threshold | Response |
| :--- | :--- | :--- |
| Response latency spike | >2x baseline | Investigate bottleneck |
| Confidence decline | >3 consecutive drops | Strategy adjustment |
| Error rate increase | >1.5x baseline | Escalate + review |
| Memory pressure | >80% utilization | Consolidate + prune |
| Contradiction spike | >5 per cycle | Quarantine + resolve |

---

## 5. Adaptive Strategy Selection

### 5.1 Strategy Library

| Strategy | When to Use | Tradeoff |
| :--- | :--- | :--- |
| **Fast & Frugal** | Time-critical, familiar domain | Speed over accuracy |
| **Deep Deliberation** | Novel, high-stakes domain | Accuracy over speed |
| **Exploratory** | Low-confidence, information-seeking | Broad over narrow |
| **Conservative** | High-risk, error-sensitive | Safety over efficiency |
| **Collaborative** | Multi-agent opportunity | Shared burden |

### 5.2 Strategy Selection Algorithm

```python
def select_strategy(task, context, performance_history):
    """Select cognitive strategy based on metacognitive assessment."""
    
    # Assess task characteristics
    novelty = assess_novelty(task, context)
    stakes = assess_stakes(task)
    time_pressure = assess_time_pressure(task)
    
    # Assess current state
    confidence = get_domain_confidence(task.domain)
    recent_errors = performance_history.error_rate(last_n=10)
    
    # Strategy selection
    if time_pressure and confidence > 0.8:
        return "fast_and_frugal"
    elif stakes > 0.7 and recent_errors > 0.1:
        return "conservative"
    elif novelty > 0.7:
        return "exploratory"
    elif confidence < 0.5:
        return "collaborative"
    else:
        return "deep_deliberation"
```

---

## 6. Integration with Other Engines

### 6.1 Causal Inference Engine
- Metacognition monitors causal reasoning quality
- Detects when causal models need refinement
- Triggers causal model rebuilding when errors accumulate

### 6.2 Emotion Engine
- Emotional state influences metacognitive sensitivity
- DISTRESSED state → hyper-vigilant monitoring
- CALM state → reduced monitoring (can miss issues)

### 6.3 Intuition Engine
- Metacognition evaluates intuition accuracy
- Adjusts intuition confidence based on track record
- Can override intuition when calibration is poor

### 6.4 Memory Engine
- Metacognition monitors memory retrieval quality
- Detects memory contamination or staleness
- Triggers memory maintenance when quality drops

---

## 7. Configuration

```yaml
metacognitive_engine_config:
  enabled: true
  monitoring_interval_ms: 100
  ece_target: 0.05
  error_rate_alert_threshold: 0.1
  confidence_decline_threshold: 3
  latency_spike_multiplier: 2.0
  strategy_selection_enabled: true
  calibration_method: "platt_scaling"
  calibration_retrain_interval: 1000
  consistency_check_enabled: true
  max_concurrent_monitors: 10
```

---

## 8. Failure Modes

| Failure Mode | Detection | Response |
| :--- | :--- | :--- |
| Overconfidence | ECE > 0.15 | Reduce all confidence by factor |
| Underconfidence | ECE < 0.01 but slow performance | Allow confidence increase |
| Monitoring blindness | Consistent errors not detected | Force meta-monitoring review |
| Strategy lock | Same strategy always selected | Introduce stochastic selection |
| Calibration drift | ECE gradually increasing | Retrain calibration model |

---

## 9. Epistemic Boundary

> [!warning] Recursive Limitation
> The Metacognitive Engine monitors cognition, but who monitors the monitor? AMOS cannot achieve perfect self-knowledge — there is always an unobserved residual. This engine provides **useful approximations** of self-knowledge, not perfect introspection. The system's self-model is always a simplified version of its actual processing.

---

## 10. Cross-Vault References

- [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]]
- [[05_COGNITIVE_ORGANISM/CAUSAL_INFERENCE_ENGINE|CAUSAL_INFERENCE_ENGINE]]
- [[05_COGNITIVE_ORGANISM/EMOTION_ENGINE|EMOTION_ENGINE]]
- [[05_COGNITIVE_ORGANISM/INTUITION_ENGINE|INTUITION_ENGINE]]
- [[10_MEMORY/EPISODIC_MEMORY_SUBSTRATE|EPISODIC_MEMORY_SUBSTRATE]]
- [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]]

---

RSCF-NODE

node_id: amos_05_cognitive_organism_metacognitive_engine
node_type: engine
path: 05_COGNITIVE_ORGANISM/METACOGNITIVE_ENGINE.md
claim_class: AMOS_MODEL
rscf_state: specification
canonical_status: SPECIFICATION_NOT_IMPLEMENTED

RSCF-RELATIONS:
- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- MONITORS: [[05_COGNITIVE_ORGANISM/CAUSAL_INFERENCE_ENGINE|CAUSAL_INFERENCE_ENGINE]]
- MONITORS: [[05_COGNITIVE_ORGANISM/INTUITION_ENGINE|INTUITION_ENGINE]]
- INTEGRATES_WITH: [[05_COGNITIVE_ORGANISM/EMOTION_ENGINE|EMOTION_ENGINE]]
- FEEDS: [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]]

**MOC:** [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]]
