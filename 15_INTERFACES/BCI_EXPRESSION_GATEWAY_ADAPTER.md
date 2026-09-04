---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Bci Expression Gateway Adapter
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

# BCI Expression Gateway Adapter

> [!ABSTRACT] Neural Interface Adapter Specification
> Binds raw and decoded electrophysiological BCI telemetry (spikes, ECoG, EEG from `21_DOMAINS/14_C04_BIO_NEURO`) into the **AMOS Full Brain OS Expression Gateway (`T_expression`)**.
> Updated with 2026 foundation model architectures and commercial BCI specifications.

---

## 1. Expression Translation Integration

The full BCI-to-expression pipeline:

```text
BCI TELEMETRY (raw neural signals)
    │
    │  Spikes, LFP, ECoG, EEG, fNIRS
    │  1,000–10,000+ channels (invasive)
    │  32–256 channels (non-invasive)
    │
    ▼
┌─────────────────────────────────┐
│ FOUNDATION MODEL DECODER        │
│ DeeperBrain / ST-EEGFormer      │
│ Cross-subject transfer          │
│ Linear O(T) complexity          │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│ EXPRESSION_CLASSIFY             │
│ Intent type classification      │
│ (speech, motor, cognitive,      │
│  emotional, attentional)        │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│ INTENT_EXTRACTION               │
│ Decode specific intended content│
│ (words, movements, commands)    │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│ MEANING_CORE                    │
│ Semantic interpretation of      │
│ decoded intent                  │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│ STRUCTURAL_LOGIC_MAP            │
│ Map to AMOS cognitive structures│
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│ EMOTION_TO_SIGNAL               │
│ Affective state from neural     │
│ patterns (valence, arousal)     │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│ NORMALISE                       │
│ Epistemic classification        │
│ OBSERVATION → PROPOSAL          │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│ LOGIC-READY INPUT               │
│ Committed to AMOS reasoning     │
│ pipeline (with authority gate)  │
└─────────────────────────────────┘
```

---

## 2. 2026 BCI Modality Specifications

### 2.1 Invasive (Intracortical)

| Parameter | 2020 Baseline | 2026 State-of-the-Art |
| :--- | :--- | :--- |
| Channel count | 100–200 | 1,000–10,000+ |
| Signal type | Spikes + LFP | Spikes + LFP + ECoG high-gamma |
| Sampling rate | 30 kHz | 30 kHz (unchanged) |
| Wireless | Experimental | Standard clinical deployment |
| AI decoder accuracy (speech) | 30–50% WER | <5% WER |
| Latency | ~200 ms | <80 ms (RNN-T transducer) |

### 2.2 Non-Invasive (EEG/fNIRS)

| Parameter | 2020 Baseline | 2026 State-of-the-Art |
| :--- | :--- | :--- |
| Resolution | Clinical only | Consumer exceeds clinical EEG |
| Foundation model | None | DeeperBrain, ST-EEGFormer |
| Cross-subject | Per-session calibration | Zero-shot transfer |
| Form factor | Lab headset | Wearable, AR/VR integrated |
| Closed-loop latency | ~500 ms | <12.5 ms (Dareplane) |

### 2.3 Hybrid Modalities

- **EEG + fNIRS**: Combined electrical + hemodynamic signals for richer representation
- **ECoG + Intracortical**: Meso-scale + micro-scale for high-resolution + wide coverage
- **BCI + EMG**: Neural + muscular signals for robust motor decoding

---

## 3. Structural Logic Map Fields

| Field | Source | AMOS Type |
| :--- | :--- | :--- |
| **Actors** | Decoded intent target | Agent ID / Entity reference |
| **Systems** | Decoded system invocation | `K_omni`, `C04_bio_neuro`, `C03_quantum`, `L7_memory` |
| **Variables** | Continuous neural trajectories | Motor/attentional continuous values |
| **Constraints** | Safety/authority bounds | Timeout, precision tolerance, risk tier |
| **Time** | Causal epoch + urgency | Epoch vector + urgency classification |
| **Direction** | Action polarity | read, write, simulate, query, abort, commit |

---

## 4. Invariants & Safety Rules

| ID | Invariant | Rationale |
| :--- | :--- | :--- |
| `INV-EXPR-01` | Raw neural signals are `OBSERVATION` | Neural data is raw measurement, not verified claim |
| `INV-EXPR-02` | Emotion modulates priority weighting, not authorization grants | Affective state influences processing priority but never grants authority (M12) |
| `INV-EXPR-03` | Transient motor preparations (<250 ms) without sustained frontal coherence are dropped | Prevents false activation from neural noise |
| `INV-EXPR-04` | Decoded neural outputs are proposals (`PROPOSAL`); commit requires commit-time authority | No neural signal can directly cause system state change |
| `INV-EXPR-05` | Foundation model confidence must exceed threshold $\theta_{\text{decode}}$ for proposal generation | Low-confidence decosals are rejected |
| `INV-EXPR-06` | Cross-subject model outputs have reduced confidence ceiling vs. personalized models | Generalization comes at calibration cost |
| `INV-EXPR-07` | Consumer-grade signals capped at lower confidence ceiling than clinical-grade | Hardware quality bounds epistemic trust |
| `INV-EXPR-08` | Closed-loop stimulation requires separate safety authority | Bidirectional BCI adds harm potential |

---

## 5. Foundation Model Integration (2026)

### 5.1 Decoder Selection

| Scenario | Recommended Decoder | Rationale |
| :--- | :--- | :--- |
| **Clinical speech BCI** | RNN-T (80ms latency) | Lowest latency for real-time speech |
| **Cross-subject EEG** | DeeperBrain (SSM) | Zero-shot transfer; linear complexity |
| **Within-subject motor** | ST-EEGFormer (ViT) | High accuracy; pre-trained representations |
| **Consumer wearable** | Lightweight SSM variant | Low power; edge deployment |

### 5.2 Adaptive Personalization

```yaml
adaptive_personalization:
  initial_model: "foundation_model_v2"
  personalization_data:
    min_sessions: 5
    signal_quality_threshold: 0.7
  adaptation_rate: "online_reinforcement_learning"
  drift_compensation:
    method: "exponential_moving_average"
    window: "24_hours"
  recalibration_trigger:
    - "signal_quality_drop > 20%"
    - "decoder_accuracy_drop > 15%"
    - "hardware_change_detected"
```

---

## 6. Integration Points

| Interface | Direction | Contract |
| :--- | :--- | :--- |
| **21_DOMAINS/C04_BIO_NEURO** | Read | Raw neural telemetry; signal preprocessing |
| **05_COGNITIVE_ORGANISM/PERCEPTION_ENGINE** | Write | Perceptual input stream |
| **05_COGNITIVE_ORGANISM/EMOTION_ENGINE** | Write | Affective state from neural patterns |
| **11_KNOWLEDGE/SOTA_BCI_NEURAL_FOUNDATION_MODELS** | Read | Foundation model specifications |
| **18_SECURITY** | Read | Neural data privacy constraints; authorization bounds |
| **10_MEMORY** | Write | BCI neural state vectors indexed as episodic traces |

---

## 7. Cross-Vault References

- [[15_INTERFACES/15_INTERFACES_MOC|15_INTERFACES_MOC]]
- [[21_DOMAINS/14_C04_BIO_NEURO/C04_NEURAL_DECODING_AND_BCI_ARCHITECTURE|C04_NEURAL_DECODING_AND_BCI_ARCHITECTURE]]
- [[11_KNOWLEDGE/SOTA_BCI_NEURAL_FOUNDATION_MODELS|SOTA_BCI_NEURAL_FOUNDATION_MODELS]]
- [[22_RESEARCH/SOTA_BCI_FOUNDATION_MODELS_NEURAL_INTERFACES_2026|SOTA_BCI_FOUNDATION_MODELS_2026]]
- [[11_KNOWLEDGE/AMOS_FULL_BRAIN_OS_ARCHITECTURE|AMOS Full Brain OS Architecture]]

---

```RSCF-NODE
node_id: bci_expression_gateway_adapter
node_type: interface_specification
domain: 15_INTERFACES
claim_class: AMOS_MODEL
confidence_ceiling:
  pipeline_architecture: high
  foundation_model_integration: high
  safety_invariants: high
falsifiers:
  - Foundation model decoder fails cross-subject generalization
  - Closed-loop latency exceeds physiological response window
  - Safety invariant violated by neural signal bypass
```
