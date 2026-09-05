---
title: "SOTA BCI Neural Decoding & Foundation Models 2026"
type: sota_paper
domain: [bci, neural_decoding, foundation_models, brain_computer_interfaces]
created: 2026-09-05
updated: 2026-09-05
tags:
  - amos-os
  - sota
  - research
  - bci
  - neural-decoding
  - foundation-models
  - brain-computer-interfaces
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: arxiv_2026
  scope: AMOS_general
confidence_ceiling: 0.93
---

# SOTA BCI Neural Decoding & Foundation Models 2026

> **Synthesis date:** 2026-09-05 · **Domain:** Brain-Computer Interfaces, Neural Decoding, Foundation Models for Neural Data · **Epistemic class:** SOURCE_CLAIM

## 1. Overview

The brain-computer interface (BCI) field has entered a **foundation-model era** in 2026. The frontier has shifted from task-specific decoders trained on individual subjects to generalizable neural representations that transfer across subjects, species, brain regions, and recording modalities. Eight key advances define the SOTA:

1. **Non-invasive sentence decoding** from MEG achieving near-competitive WER using LLM semantic representations (Brain2Qwerty v2)
2. **Intracortical speech BCIs** reaching sub-15% phoneme error rates with non-homologous sensor calibration (Contextual seq2seq)
3. **Open-vocabulary mutual information** as a modality-agnostic evaluation metric for speech BCIs (OVMI)
4. **Cross-species/cross-subject/cross-region foundation models** for invasive spike data (UniBCI)
5. **Subject-invariant EEG representations** via two-stage pretraining (EEG-PRIME)
6. **Compact implantable decoders** with integer-only inference via task-specific knowledge distillation (BrainDistill)
7. **Real-time motor-imagery state decoding** for rehabilitation exoskeletons (Dual-state EEG)
8. **Unified motor-imagery architectures** for consumer-grade EEG hardware (NeuroPath)

These advances directly inform AMOS OS's [[07_SKILLS/amos-agent-systems-master/SKILL|agent systems]] (neural-agent interfaces), [[10_MEMORY/10_MEMORY_MOC|memory plane]] (neural signal encoding), and [[04_RUNTIME/04_RUNTIME_README|runtime]] (real-time neural decoding pipelines).

## 2. Key Papers & Breakthroughs

### 2.1 Brain2Qwerty v2 — Non-Invasive MEG Sentence Decoding
- **arXiv ID:** arXiv:2608.18114
- **Domain:** Non-invasive BCI, MEG, language decoding
- **Key result:** Achieves ~39% word error rate (WER) for non-invasive sentence decoding from magnetoencephalography (MEG) signals, a significant advance over prior non-invasive approaches. The system leverages LLM-derived semantic representations as a prior, bridging neural activity to language structure through a learned mapping from MEG features to token embeddings. This demonstrates that non-invasive recording modalities can approach clinically relevant decoding accuracy when combined with foundation-model language priors.
- **AMOS mapping:** [[10_MEMORY/10_MEMORY_MOC|Memory plane]] (neural-to-symbolic encoding), [[07_SKILLS/amos-cognition-engine-layer/SKILL|cognition engine]] (language grounding from neural signals), [[04_RUNTIME/04_RUNTIME_README|Runtime]] (real-time MEG processing pipeline)
- **Epistemic class:** SOURCE_CLAIM
- **Confidence ceiling:** 0.90

### 2.2 Contextual seq2seq Intracortical Speech Decoding
- **arXiv ID:** arXiv:2603.20246
- **Domain:** Intracortical BCI, speech decoding, neural prosthesis
- **Key result:** Achieves 14.3% phoneme error rate for intracortical speech decoding using a contextual sequence-to-sequence architecture. Introduces a Non-Homologous Sensor (NHS) calibration module that enables rapid recalibration when sensor arrays change position or composition, addressing a critical clinical barrier for long-term implant viability. The contextual model leverages preceding sentence context to improve phoneme prediction, mirroring natural language processing.
- **AMOS mapping:** [[07_SKILLS/amos-adaptive-calibration/SKILL|adaptive calibration]], [[10_MEMORY/10_MEMORY_MOC|Memory plane]] (contextual state encoding), [[07_SKILLS/amos-evolution-loop/SKILL|evolution loop]] (sensor drift adaptation)
- **Epistemic class:** SOURCE_CLAIM
- **Confidence ceiling:** 0.91

### 2.3 Common Measure for Speech BCIs (OVMI)
- **arXiv ID:** arXiv:2609.02887
- **Domain:** BCI evaluation, open-vocabulary decoding, mutual information
- **Key result:** Introduces Open-Vocabulary Mutual Information (OVMI) as a modality-agnostic evaluation metric for speech BCIs, enabling fair comparison across invasive and non-invasive systems. Demonstrates a 16.3% accuracy improvement when OVMI-guided optimization is applied to decoder training, suggesting that traditional word-error metrics underrepresent decoder capacity. OVMI provides a principled information-theoretic foundation for benchmarking open-vocabulary neural speech decoders.
- **AMOS mapping:** [[19_TESTS/19_TESTS_README|Test plane]] (modality-agnostic evaluation), [[07_SKILLS/amos-validation-pipeline/SKILL|validation pipeline]] (information-theoretic validation), [[07_SKILLS/amos-multi-objective-optimization/SKILL|multi-objective optimization]] (Pareto-optimal decoder metrics)
- **Epistemic class:** SOURCE_CLAIM
- **Confidence ceiling:** 0.88

### 2.4 UniBCI — Foundation Model for Invasive Spike Data
- **arXiv ID:** arXiv:2605.00061
- **Domain:** Neural foundation models, invasive recording, cross-species transfer
- **Key result:** Presents the first foundation model for invasive spike data that generalizes across species, subjects, and brain regions without per-subject retraining. UniBCI is pretrained on large-scale multi-electrode spike corpora and fine-tuned with minimal data for downstream decoding tasks. Cross-region transfer (motor cortex → auditory cortex) and cross-species transfer (rodent → primate) demonstrate that shared neural coding principles can be extracted at the spike level, establishing a new paradigm for invasive BCI generalization.
- **AMOS mapping:** [[07_SKILLS/amos-transfer-learning/SKILL|transfer learning]], [[10_MEMORY/10_MEMORY_MOC|Memory plane]] (cross-domain neural representations), [[07_SKILLS/amos-foundation-model-integration/SKILL|foundation model integration]]
- **Epistemic class:** SOURCE_CLAIM
- **Confidence ceiling:** 0.89

### 2.5 EEG-PRIME — Two-Stage EEG Foundation Model
- **arXiv ID:** arXiv:2608.13072
- **Domain:** EEG foundation models, subject-invariant representations
- **Key result:** Introduces a two-stage EEG foundation model that produces subject-invariant representations through contrastive pretraining followed by task-specific adaptation. The first stage learns modality-generic EEG features across thousands of subjects; the second stage adapts to downstream tasks (motor imagery, emotion recognition, seizure detection) with minimal labeled data. Subject-invariant representations reduce inter-subject variance by a significant margin, enabling zero-shot deployment to new users without calibration sessions.
- **AMOS mapping:** [[07_SKILLS/amos-foundation-model-integration/SKILL|foundation model integration]], [[10_MEMORY/10_MEMORY_MOC|Memory plane]] (subject-invariant encoding), [[07_SKILLS/amos-adaptive-calibration/SKILL|adaptive calibration]] (zero-shot calibration reduction)
- **Epistemic class:** SOURCE_CLAIM
- **Confidence ceiling:** 0.87

### 2.6 BrainDistill — Compact Implantable Decoder
- **arXiv ID:** arXiv:2601.17625
- **Domain:** Neural decoder compression, knowledge distillation, implantable BCI
- **Key result:** Demonstrates task-specific knowledge distillation that compresses large neural decoders into compact models suitable for implantable hardware with integer-only inference. BrainDistill achieves near-teacher accuracy while reducing model size by an order of magnitude and enabling fully integer-quantized execution on resource-constrained neural implants. This bridges the gap between foundation-model-scale decoders and the severe power/area constraints of clinical implantable devices.
- **AMOS mapping:** [[04_RUNTIME/04_RUNTIME_README|Runtime]] (constrained-device inference), [[07_SKILLS/amos-token-budget-governance/SKILL|token budget governance]] (resource-constrained execution), [[07_SKILLS/amos-model-compression/SKILL|model compression]]
- **Epistemic class:** SOURCE_CLAIM
- **Confidence ceiling:** 0.86

### 2.7 Real-Time Movement Onset/Offset Decoding
- **arXiv ID:** arXiv:2603.16825
- **Domain:** Motor-imagery BCI, rehabilitation, real-time state decoding
- **Key result:** Presents a dual-state motor-imagery EEG decoder that detects movement onset and offset in real time for rehabilitation exoskeleton control. The system operates on consumer-grade EEG hardware with low-latency inference, enabling closed-loop exoskeleton assistance during stroke rehabilitation. Dual-state decoding (movement vs. rest) achieves high temporal precision, reducing false triggers that could cause patient discomfort or injury during rehabilitation sessions.
- **AMOS mapping:** [[04_RUNTIME/04_RUNTIME_README|Runtime]] (real-time low-latency inference), [[07_SKILLS/amos-operational-modes/SKILL|operational modes]] (safety-critical closed-loop control), [[07_SKILLS/amos-convergence-detection/SKILL|convergence detection]] (state transition detection)
- **Epistemic class:** SOURCE_CLAIM
- **Confidence ceiling:** 0.85

### 2.8 NeuroPath — Unified Motor-Imagery Architecture
- **arXiv ID:** arXiv:2604.09654
- **Domain:** Motor-imagery BCI, consumer-grade EEG, unified architecture
- **Key result:** Introduces a unified motor-imagery decoding architecture designed for consumer-grade EEG headsets, eliminating the need for per-task architecture redesign. NeuroPath handles multiple motor-imagery paradigms (left/right hand, feet, tongue) within a single model, using a shared backbone with task-specific readout heads. The architecture is optimized for the lower signal quality and fewer channels of consumer hardware, making BCI accessible outside clinical settings.
- **AMOS mapping:** [[07_SKILLS/amos-foundation-model-integration/SKILL|foundation model integration]] (unified multi-task architecture), [[04_RUNTIME/04_RUNTIME_README|Runtime]] (consumer hardware deployment), [[07_SKILLS/amos-multi-objective-optimization/SKILL|multi-objective optimization]] (shared backbone, task-specific heads)
- **Epistemic class:** SOURCE_CLAIM
- **Confidence ceiling:** 0.84

## 3. Architectural Implications for AMOS OS

### 3.1 Neural Foundation Models as Memory Primitives
UniBCI and EEG-PRIME establish that neural data can be encoded into generalizable foundation representations. AMOS's [[10_MEMORY/10_MEMORY_MOC|memory plane]] can treat these as first-class encoding primitives:
- **Subject-invariant representations** map to AMOS's need for agent-identity-independent memory encoding
- **Cross-species/cross-region transfer** suggests that AMOS memory encoding should be modality-agnostic at the foundation level
- **Two-stage pretraining** (generic → task-specific) mirrors AMOS's [[07_SKILLS/amos-evolution-loop/SKILL|evolution loop]] observe→integrate cycle

### 3.2 Real-Time Safety-Critical Neural Decoding
The dual-state movement decoder and BrainDistill highlight that neural decoding pipelines must operate under strict latency and safety constraints:
- **Integer-only inference** on implantable hardware maps to AMOS [[04_RUNTIME/04_RUNTIME_README|runtime]] constrained-device execution
- **Closed-loop exoskeleton control** requires AMOS [[07_SKILLS/amos-operational-modes/SKILL|operational modes]] safety envelopes (SAFE_INTROSPECTION_ONLY for calibration, EXTERNAL_WRITE_LOW_RISK for actuation)
- **False-trigger reduction** maps to AMOS [[07_SKILLS/amos-capability-bound-governance/SKILL|capability-bound governance]] — neural decode → actuation must pass authority gates

### 3.3 Evaluation & Benchmarking
OVMI's information-theoretic evaluation framework has direct implications for AMOS [[19_TESTS/19_TESTS_README|test plane]]:
- **Modality-agnostic metrics** enable fair comparison across different neural decoding pipelines
- **Open-vocabulary evaluation** aligns with AMOS's need for open-world agent evaluation
- **Mutual information as a benchmark** suggests AMOS should adopt information-theoretic validation alongside behavioral metrics

## 4. Cross-Domain Connections

| AMOS Domain | SOTA Connection | Mapping |
|-------------|----------------|---------|
| [[10_MEMORY/10_MEMORY_MOC|Memory]] | UniBCI, EEG-PRIME, Brain2Qwerty | Neural representations as memory primitives |
| [[04_RUNTIME/04_RUNTIME_README|Runtime]] | BrainDistill, Dual-state decoder | Constrained-device real-time inference |
| [[19_TESTS/19_TESTS_README|Tests]] | OVMI | Information-theoretic evaluation metrics |
| [[07_SKILLS/amos-adaptive-calibration/SKILL|Adaptive Calibration]] | Contextual seq2seq NHS | Sensor drift adaptation |
| [[07_SKILLS/amos-operational-modes/SKILL|Operational Modes]] | Dual-state decoder | Safety-critical closed-loop control |
| [[07_SKILLS/amos-foundation-model-integration/SKILL|Foundation Model Integration]] | UniBCI, EEG-PRIME, NeuroPath | Cross-domain neural foundation models |
| [[07_SKILLS/amos-capability-bound-governance/SKILL|Capability-Bound Governance]] | Dual-state decoder | Neural decode → actuation authority gates |

## 5. Open Questions & Gaps

1. **Long-term implant stability:** Contextual seq2seq's NHS module addresses sensor recalibration, but no SOTA paper provides evidence of >2-year implant stability with consistent decoding accuracy. AMOS treats long-term neural interface stability as UNKNOWN/GAP per [[01_CANON/01_CORE_LAWS/L10_FAILURE_RECOVERY|L10 failure recovery]].
2. **Closed-loop safety proofs:** The dual-state decoder demonstrates low false-trigger rates empirically, but no formal safety guarantee is provided for closed-loop neural decode → actuation. AMOS [[07_SKILLS/amos-capability-bound-governance/SKILL|capability-bound governance]] requires formal authority proofs for safety-critical actuation.
3. **Cross-modal transfer bounds:** UniBCI demonstrates cross-species/cross-region transfer, but the theoretical bounds on transfer degradation are not characterized. AMOS [[07_SKILLS/amos-transfer-learning/SKILL|transfer learning]] needs formal transfer bounds.
4. **Implantable power budgets:** BrainDistill achieves integer-only inference but does not report end-to-end power consumption including telemetry. AMOS [[07_SKILLS/amos-token-budget-governance/SKILL|token budget governance]] needs power-aware execution models for implantable devices.

## 6. References

- arXiv:2608.18114 — Brain2Qwerty v2: Non-Invasive MEG Sentence Decoding with LLM Semantic Representations
- arXiv:2603.20246 — Contextual seq2seq Intracortical Speech Decoding with NHS Calibration
- arXiv:2609.02887 — A Common Measure for Speech BCIs: Open-Vocabulary Mutual Information
- arXiv:2605.00061 — UniBCI: A Foundation Model for Invasive Spike Data
- arXiv:2608.13072 — EEG-PRIME: Two-Stage EEG Foundation Model for Subject-Invariant Representations
- arXiv:2601.17625 — BrainDistill: Compact Implantable Neural Decoders via Task-Specific Knowledge Distillation
- arXiv:2603.16825 — Real-Time Movement Onset/Offset Decoding for Rehabilitation Exoskeletons
- arXiv:2604.09654 — NeuroPath: Unified Motor-Imagery Architecture for Consumer-Grade EEG

---

## Cross-References

- [[22_RESEARCH/01_PAPERS/SOTA_AI_CODING_AGENTS_SELF_EVOLVING_HARNESSES_2026|SOTA AI Coding Agents & Self-Evolving Harnesses]] — neural-agent interface implications
- [[22_RESEARCH/01_PAPERS/SOTA_AI_AGENTS_MEMORY_TOOLS_EVOLUTION_2026|SOTA AI Agents Memory & Tools Evolution]] — memory encoding parallels
- [[22_RESEARCH/01_PAPERS/SOTA_LLM_INFERENCE_OPTIMIZATION_REASONING_2026|SOTA LLM Inference Optimization & Reasoning]] — foundation model inference parallels
- [[10_MEMORY/10_MEMORY_MOC|Memory Plane]] — neural representation encoding
- [[04_RUNTIME/04_RUNTIME_README|Runtime Plane]] — real-time neural decoding pipelines
- [[19_TESTS/19_TESTS_README|Test Plane]] — OVMI evaluation framework
- [[22_RESEARCH/AMOS_FRONTIER_RESEARCH_BRIDGE_2026-09-04|Frontier Research Bridge]] — cross-domain synthesis

**arXiv bridge note:** All 8 papers are 2026 arXiv preprints (Jan–Sep 2026). Epistemic class is SOURCE_CLAIM for all entries — these are reported results from preprints that have not yet undergone full peer review. Confidence ceilings reflect this. Specific numerical results (WER, phoneme error rates, accuracy improvements) should be treated as author-reported claims pending independent replication.

**MOC:** [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]] · [[22_RESEARCH/01_PAPERS/01_PAPERS_MOC|01_PAPERS_MOC]]
