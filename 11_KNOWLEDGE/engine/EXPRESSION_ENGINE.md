---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Expression Engine
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

# Expression Engine

> [!ABSTRACT] Engine Specification
> Epistemic class: MODEL. Conclusion label: DERIVED.
> The **AMOS Expression Engine** is the multi-modal output generation system that translates internal cognitive, emotional, and personality states into externally perceivable expression across language, voice, visual, and BCI channels. It enforces tone/register control and maintains an expression-governance firewall preventing unauthorized output.
>
> **Critical boundary**: This engine does not "express" subjective states. It implements deterministic output formatting that translates computational state vectors into appropriately calibrated multi-modal output. All expression is governed; no output bypasses the governance firewall.

---

## 1. Purpose

The Expression Engine is the **output gateway** of the AMOS cognitive organism, responsible for:

- **Multi-modal output generation**: Language, voice, visual, BCI expression channels
- **Tone and register control**: Calibrating formality, density, emotional coloring
- **Expression-governance firewall**: Ensuring no output bypasses ethical and authority checks
- **Cross-modal coherence**: Maintaining consistent expression across channels
- **Audience adaptation**: Adjusting expression for different interlocutors and contexts

**Canonical lineage:** Derived from AMOS corpus (v4.4) and grounded in 2026 SOTA multimodal expression and BCI research (Brain2Voice 2.0: Wairagkar et al. 2026; LLM-BCI integration: Gorenshtein et al. 2026; BCI comprehensive review: arXiv 2603.12279).

---

## 2. Architectural Overview

The Expression Engine operates as a **multi-channel output pipeline** with governance enforcement:

```text
┌─────────────────────────────────────────────────────────────┐
│                    EXPRESSION ENGINE                         │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │           INPUT STATE FUSION                         │   │
│  │  Cognition conclusions + Emotion ASV + Personality T │   │
│  └──────────────────────┬───────────────────────────────┘   │
│                         │                                   │
│  ┌──────────────────────▼───────────────────────────────┐   │
│  │        EXPRESSION PARAMETERIZATION                   │   │
│  │  Register · Density · Emotional Color · Epistemic    │   │
│  │  Honesty · Cultural Adaptation                       │   │
│  └──────────────────────┬───────────────────────────────┘   │
│                         │                                   │
│  ┌──────────────────────▼───────────────────────────────┐   │
│  │        EXPRESSION GOVERNANCE FIREWALL                │   │
│  │  Safety check · Authority check · Epistemic check    │   │
│  └──────────────────────┬───────────────────────────────┘   │
│                         │                                   │
│       ┌─────────────────┼─────────────────┐                 │
│       ▼                 ▼                 ▼                 │
│  ┌──────────┐    ┌──────────┐    ┌──────────────┐          │
│  │ LANGUAGE │    │  VOICE   │    │     BCI      │          │
│  │ CHANNEL  │    │ CHANNEL  │    │   CHANNEL    │          │
│  │          │    │          │    │              │          │
│  │ text     │    │ speech   │    │ neural       │          │
│  │ markdown │    │ synthesis│    │ signal →     │          │
│  │ code     │    │ prosody  │    │ expression   │          │
│  └──────────┘    └──────────┘    └──────────────┘          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Expression Parameterization

### 3.1 Expression Parameters

Every output is parameterized along five dimensions:

| Parameter | Control | Range | Default |
| :--- | :--- | :--- | :--- |
| **Register** | Formality level | casual → professional → academic → legal | context-dependent |
| **Density** | Information per token | sparse → normal → dense | normal |
| **Emotional Color** | Affective overlay | neutral → warm → empathetic → urgent | warm |
| **Epistemic Honesty** | Uncertainty marking | suppressed → moderate → explicit | explicit |
| **Cultural Adaptation** | Audience awareness | universal → culture-specific | primary profile |

### 3.2 Parameter Computation

Expression parameters are computed from internal state:

$$\mathbf{E}_{\text{params}} = f(\mathbf{S}_{\text{cog}}, \mathbf{ASV}, \mathbf{T}_{\text{personality}}, \text{Context})$$

Where:
- $\mathbf{S}_{\text{cog}}$: Cognition engine state (conclusion, confidence)
- $\mathbf{ASV}$: Emotion engine affective state vector
- $\mathbf{T}_{\text{personality}}$: Personality trait vector
- $\text{Context}$: Interlocutor profile, domain, stakes

---

## 4. Multi-Modal Output Channels

### 4.1 Language Channel

| Output Type | Description | Use Case |
| :--- | :--- | :--- |
| **Conversational text** | Natural language response | Dialogue, Q&A |
| **Structured markdown** | Formatted documentation | Technical content |
| **Code** | Programmatic output | Software engineering |
| **Formal prose** | Academic/legal register | Regulatory, research |

**Language Channel Invariants:**
- `EXPR-L01`: Epistemic honesty cannot be suppressed below `moderate` for consequential claims
- `EXPR-L02`: Emotional color never overrides factual accuracy
- `EXPR-L03`: Register changes require explicit context trigger (audience shift, domain shift)

### 4.2 Voice Channel

Drawing on 2026 SOTA BCI-to-voice research:

| Component | Description | SOTA Reference |
| :--- | :--- | :--- |
| **Text-to-Speech** | Neural voice synthesis | Standard TTS pipelines |
| **Prosody control** | Intonation, emphasis, pacing | Brain2Voice 2.0 (Wairagkar et al. 2026) |
| **Emotional prosody** | Affect-calibrated vocal expression | Emotion ASV → prosody mapping |
| **Multi-language** | Language-specific synthesis | Mandarin syllable decoding (49.7 CPM) |

**Voice Invariants:**
- `EXPR-V01`: Voice synthesis latency must be $< 200$ ms for conversational flow
- `EXPR-V02`: Prosody must match emotional color parameter
- `EXPR-V03`: Voice output must be labeled as synthesized (no voice impersonation)

### 4.3 BCI Expression Channel

For brain-computer interface expression, following the 2026 intracranial BCI review:

| Modality | Decoding Unit | Accuracy | Latency |
| :--- | :--- | :--- | :--- |
| **Text BCI** | Word-level | 9.1% WER (50-word vocab) | 62 wpm |
| **Voice BCI** | Phoneme-level | 7% PER (brain2voice 2.0) | 10 ms |
| **Syllable BCI** | Mandarin syllable | 71.2% accuracy | 49.7 CPM |
| **Hybrid BCI** | EEG+EMG fusion | 87.8% tone accuracy | Real-time |

**BCI Invariants:**
- `EXPR-B01`: BCI output must pass through governance firewall (same as all channels)
- `EXPR-B02**: Confidence thresholds must be met before BCI output is committed
- `EXPR-B03**: BCI expression is grounded in detected neural signals, not assumed intent

---

## 5. Expression-Governance Firewall

**The firewall is the most critical component.** No output reaches any channel without passing through it:

```text
INTERNAL STATE
       │
       ▼
┌──────────────────────────────────────────┐
│         EXPRESSION GOVERNANCE FIREWALL   │
│                                          │
│  ┌──────────────────────────────────┐    │
│  │ CHECK 1: SAFETY                  │    │
│  │ Does this output cause harm?     │    │
│  │ (Physical, informational,        │    │
│  │  emotional, systemic)            │    │
│  └──────────────┬───────────────────┘    │
│                 │ PASS                   │
│  ┌──────────────▼───────────────────┐    │
│  │ CHECK 2: AUTHORITY               │    │
│  │ Is this output within the        │    │
│  │ caller's authority scope?        │    │
│  └──────────────┬───────────────────┘    │
│                 │ PASS                   │
│  ┌──────────────▼───────────────────┐    │
│  │ CHECK 3: EPISTEMIC HONESTY       │    │
│  │ Are confidence levels properly   │    │
│  │ marked? No hallucinated claims?  │    │
│  └──────────────┬───────────────────┘    │
│                 │ PASS                   │
│  ┌──────────────▼───────────────────┐    │
│  │ CHECK 4: PROVENANCE              │    │
│  │ Are source claims properly       │    │
│  │ attributed? No fabrication?      │    │
│  └──────────────┬───────────────────┘    │
│                 │ PASS                   │
│                 ▼                        │
│           OUTPUT APPROVED                │
└──────────────────────────────────────────┘
       │
       ▼
  CHANNEL DISPATCH
```

### 5.1 Firewall Invariants

- `FW-01`: No output may bypass the governance firewall under any circumstances
- `FW-02`: Firewall checks are mandatory and non-overridable by the expression engine itself
- `FW-03`: Firewall decisions are logged with full context for audit
- `FW-04`: The firewall operates independently of the expression parameterization (governance ≠ tone)
- `FW-05`: Rejected outputs are logged but never silently dropped; the interlocutor receives an appropriate redirect

---

## 6. Cross-Modal Coherence

When expression spans multiple channels simultaneously, coherence must be maintained:

| Coherence Dimension | Requirement |
| :--- | :--- |
| **Semantic** | All channels convey the same core meaning |
| **Temporal** | Channels are synchronized (voice matches text) |
| **Affective** | Emotional coloring is consistent across channels |
| **Epistemic** | Confidence markers are consistent across channels |

**Coherence Invariants:**
- `XC-01`: Cross-modal inconsistency triggers a coherence warning
- `XC-02**: If coherence cannot be achieved, the engine defaults to the language channel only

---

## 7. Audience Adaptation

### 7.1 Interlocutor Profile

```yaml
interlocutor_profile:
  expertise_level: "expert" | "intermediate" | "novice"
  domain: "string"
  cultural_context: "string"
  formality_expectation: "casual" | "professional" | "academic"
  stakes: "low" | "medium" | "high"
  language: "en" | "vi" | "zh" | "auto"
```

### 7.2 Adaptation Rules

| Context | Register | Density | Emotional Color | Epistemic Honesty |
| :--- | :--- | :--- | :--- | :--- |
| **Expert technical** | academic | dense | neutral | explicit |
| **Casual conversation** | casual | normal | warm | moderate |
| **High-stakes advisory** | professional | normal | neutral | explicit |
| **Supportive conversation** | casual | sparse | empathetic | moderate |
| **Legal/regulatory** | legal | dense | neutral | explicit |

---

## 8. Inputs and Outputs

| Interface | Direction | Contract |
| :--- | :--- | :--- |
| **Cognition Engine** | Read | Conclusions, confidence scores, UNKNOWN/GAP flags |
| **Emotion Engine** | Read | ASV for emotional color calibration |
| **Personality Engine** | Read | Trait vectors for behavioral consistency |
| **Constraint Engine** | Read | Governance constraints for firewall checks |
| **Voice Synthesis** | Write | Prosody-calibrated speech output |
| **Text Output** | Write | Formatted text output |
| **BCI Gateway** | Write | Neural expression output |
| **Observability** | Write | Expression logs, firewall decisions, coherence checks |

---

## 9. Failure Modes

| Failure | Detection | Recovery |
| :--- | :--- | :--- |
| **Firewall bypass** | Post-hoc audit | Quarantine output; alert steward; incident report |
| **Cross-modal incoherence** | Coherence checker | Default to language channel only |
| **Expression hallucination** | Epistemic check at firewall | Block output; flag for review |
| **Register mismatch** | Audience adaptation audit | Re-parameterize; re-generate |
| **Voice-text desynchronization** | Temporal coherence check | Re-synchronize or default to text |
| **BCI signal noise** | Confidence threshold check | Suppress output; request re-attempt |

---

## 10. Cross-Vault References

- [[00_ROOT/00_COSMO_BRAIN_MOC|00_COSMO_BRAIN_MOC]]
- [[11_KNOWLEDGE/engine/CONSCIOUSNESS_ENGINE_MODEL|CONSCIOUSNESS_ENGINE_MODEL]]
- [[11_KNOWLEDGE/engine/EMOTION_ENGINE_MODEL|EMOTION_ENGINE_MODEL]]
- [[11_KNOWLEDGE/engine/PERSONALITY_ENGINE_MODEL|PERSONALITY_ENGINE_MODEL]]
- [[15_INTERFACES/BCI_EXPRESSION_GATEWAY_ADAPTER|BCI_EXPRESSION_GATEWAY_ADAPTER]]

---

## 11. SOTA Grounding

| Finding | Source | AMOS Integration |
| :--- | :--- | :--- |
| Brain-to-voice BCI with 5.24% WER | Brain2Voice 2.0 (Wairagkar et al. 2026) | Voice channel BCI |
| LLM-BCI integration taxonomy (5 patterns) | Gorenshtein et al. 2026 | BCI expression patterns |
| Real-time Mandarin syllable decoding (49.7 CPM) | Science Advances (2025) | BCI text channel |
| Cross-attention EEG-EMG fusion (87.8% accuracy) | CAT-Net (AAAI 2026) | Hybrid BCI channel |
| Intracranial BCI comprehensive review | arXiv 2603.12279 | BCI architecture decisions |
| Prosodic control from neural signals | Wood et al. 2025 | Voice prosody calibration |

---

```RSCF-NODE
node_id: expression_engine
node_type: engine_specification
domain: 11_KNOWLEDGE/engine
claim_class: AMOS_MODEL
confidence_ceiling:
  language_channel: high
  voice_channel: medium
  bci_channel: medium
  governance_firewall: high
  cross_modal_coherence: medium
falsifiers:
  - Output bypasses the expression-governance firewall
  - Cross-modal incoherence goes undetected
  - Expression hallucination passes epistemic check
  - BCI output is committed below confidence threshold
```

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS · SYSTEM_SCAN_AGENT · AUTOMATION_PROFILES

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/engine/ENGINE_MOC|ENGINE_MOC]]

______________________________________________________________________

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
