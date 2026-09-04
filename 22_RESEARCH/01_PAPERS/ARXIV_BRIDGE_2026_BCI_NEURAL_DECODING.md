---
title: "ArXiv Bridge 2026 — BCI Neural Decoding & Brain Signal Processing"
type: arxiv_bridge
source: 22_RESEARCH/01_PAPERS/ARXIV_BRIDGE_2026_BCI_NEURAL_DECODING
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
epistemic_class: SOURCE_CLAIM
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: SOURCE_CLAIM
  provenance:
    - arxiv_2026_corpus
    - 11_KNOWLEDGE/_arxiv_md/_arxiv_md_MOC
    - 22_RESEARCH/02_ARXIV_BRIDGES
  scope: arxiv_bridge_2026_bci_neural_decoding
tags:
  - amos-os
  - 22_research
  - arxiv-bridge
  - bci
  - neural-decoding
  - eeg
  - fnirs
  - brain-computer-interface
  - sota-2026
---

# ArXiv Bridge 2026 — BCI Neural Decoding & Brain Signal Processing

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **Epistemic Class:** `SOURCE_CLAIM`
> **Bridge Date:** 2026-09-04
> **Source Corpus:** `/Users/mac/Documents/_arxiv_md_external/obsidian-arxiv-md/2026/`

---

## Purpose

This bridge connects 2026 arXiv pre-prints in brain-computer interfaces (BCI), neural decoding, EEG signal processing, and multimodal brain signal fusion to their corresponding AMOS planes. These papers represent the neural interface frontier critical to AMOS's interface and cognitive organism planes.

---

## 1. EEG Foundation Models & Universal BCI

### 1.1 DeeperBrain: Neuro-Grounded EEG Foundation Model

| Field | Value |
|-------|-------|
| **arXiv ID** | `2601.06134v2` |
| **Title** | DeeperBrain: A Neuro-Grounded EEG Foundation Model Towards Universal BCI |
| **Date** | 2026-01 |
| **Target Planes** | [[15_INTERFACES/15_INTERFACES_MOC\|15_INTERFACES]], [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC\|05_COGNITIVE_ORGANISM]], [[13_MODELS/13_MODELS_MOC\|13_MODELS]] |
| **Epistemic Class** | `EMPIRICAL` |
| **AMOS Relevance** | EEG foundation model for universal BCI — directly relevant to AMOS interfaces plane and cognitive organism. Foundation models for EEG enable transfer learning across BCI tasks, paralleling AMOS's multi-scale model deployment. Neuro-grounded pretraining ensures biological plausibility. |
| **Confidence Ceiling** | `EMPIRICAL` for EEG benchmarks; `SOURCE_CLAIM` for universal BCI claim. |

### 1.2 Bridging Scalp and Intracranial EEG via Pretrained Neural Representations

| Field | Value |
|-------|-------|
| **arXiv ID** | `2604.14202v1` |
| **Title** | Bridging scalp and intracranial EEG in BCI via pretrained neural representations |
| **Date** | 2026-04 |
| **Target Planes** | [[15_INTERFACES/15_INTERFACES_MOC\|15_INTERFACES]], [[13_MODELS/13_MODELS_MOC\|13_MODELS]], [[22_RESEARCH/22_RESEARCH_MOC\|22_RESEARCH]] |
| **Epistemic Class** | `EMPIRICAL` |
| **AMOS Relevance** | Bridging scalp and intracranial EEG — critical for AMOS interfaces plane. Non-invasive (scalp) to invasive (intracranial) transfer enables AMOS to leverage both BCI modalities. Pretrained neural representations enable cross-modal transfer learning. |
| **Confidence Ceiling** | `EMPIRICAL` for transfer learning; `SOURCE_CLAIM` for clinical deployment. |

---

## 2. EEG Signal Processing & Artifact Rejection

### 2.1 From EEG Cleaning to Decoding: Artifact Rejection in MI-BCIs

| Field | Value |
|-------|-------|
| **arXiv ID** | `2605.12408v2` |
| **Title** | From EEG Cleaning to Decoding: The Role of Artifact Rejection in MI-based BCIs |
| **Date** | 2026-05 |
| **Target Planes** | [[15_INTERFACES/15_INTERFACES_MOC\|15_INTERFACES]], [[17_OBSERVABILITY/17_OBSERVABILITY_MOC\|17_OBSERVABILITY]], [[04_RUNTIME/04_RUNTIME_MOC\|04_RUNTIME]] |
| **Epistemic Class** | `EMPIRICAL` |
| **AMOS Relevance** | EEG artifact rejection for motor imagery BCI — relevant to AMOS interfaces and observability planes. Artifact rejection is the signal quality gate for BCI systems, paralleling AMOS's provenance validation. Systematic study of cleaning → decoding pipeline informs AMOS's signal processing runtime. |
| **Confidence Ceiling** | `EMPIRICAL` for MI-BCI benchmarks; `SOURCE_CLAIM` for other BCI paradigms. |

---

## 3. Multimodal BCI & Cross-Modal Fusion

### 3.1 Synchronous EEG-fNIRS BCI with Multimodal Avalanche Analysis

| Field | Value |
|-------|-------|
| **arXiv ID** | `2603.23358v1` |
| **Title** | A Synchronous EEG-fNIRS BCI: A Proof-of-Concept for Multimodal Avalanche Analysis |
| **Date** | 2026-03 |
| **Target Planes** | [[15_INTERFACES/15_INTERFACES_MOC\|15_INTERFACES]], [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC\|05_COGNITIVE_ORGANISM]], [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L02_ATTENTION/L02_ATTENTION_MOC\|L02 Attention]] |
| **Epistemic Class** | `SOURCE_CLAIM` |
| **AMOS Relevance** | Synchronous EEG-fNIRS fusion with avalanche analysis — directly relevant to AMOS cross-modal interface ledgers. Neural avalanche analysis connects to AMOS's criticality-based cognitive state transitions. Multimodal fusion (electrical + hemodynamic) provides complementary temporal and spatial resolution. |
| **Confidence Ceiling** | `SOURCE_CLAIM` — proof-of-concept; clinical validation pending. |

---

## 4. Brain-to-Text & Speech Decoding

### 4.1 Unified Brain-to-Text Decoding (from earlier bridge)

See [[22_RESEARCH/01_PAPERS/ARXIV_BRIDGE_2026_QUANTUM_HARDWARE_SENSING|ArXiv Bridge — Quantum Hardware/Sensing]] §5.1 for the brain-to-text decoding paper (arXiv:2603.12628). This paper bridges speech production and perception decoding, directly relevant to AMOS's BCI interface and cognitive representation planes.

---

## Bridge Summary

| Domain | Papers Bridged | Primary AMOS Planes |
|--------|---------------|---------------------|
| EEG Foundation Models | 2 | 15_INTERFACES, 05_COGNITIVE_ORGANISM, 13_MODELS |
| EEG Signal Processing | 1 | 15_INTERFACES, 17_OBSERVABILITY, 04_RUNTIME |
| Multimodal BCI Fusion | 1 | 15_INTERFACES, 05_COGNITIVE_ORGANISM, 25_COGNITIVE_MATRIX |
| Brain-to-Text Decoding | 1 (cross-ref) | 15_INTERFACES, 25_COGNITIVE_MATRIX |
| **Total** | **5** (4 new + 1 cross-ref) | |

---

## Epistemic Boundary

All bridges carry `SOURCE_CLAIM` or `EMPIRICAL` epistemic class. EEG foundation model results (§1.1) are `EMPIRICAL` on benchmarks but `SOURCE_CLAIM` for universal BCI claims. Cross-modal fusion results (§3.1) are `SOURCE_CLAIM` — proof-of-concept only. Artifact rejection findings (§2.1) are `EMPIRICAL` for MI-BCI but may not generalize to all BCI paradigms.

`EMPIRICAL != UNIVERSAL`
`SOURCE_CLAIM != VERIFIED`
`PROOF_OF_CONCEPT != CLINICAL_DEPLOYMENT`

---

## Navigation

- [[22_RESEARCH/02_ARXIV_BRIDGES|ArXiv Bridges MOC]]
- [[22_RESEARCH/01_PAPERS/ARXIV_BRIDGE_2026_BCI_AI_QUANTUM|ArXiv Bridge — BCI/AI/Quantum]]
- [[22_RESEARCH/01_PAPERS/ARXIV_BRIDGE_2026_CAUSAL_PREDICTIVE|ArXiv Bridge — Causal/Predictive]]
- [[22_RESEARCH/01_PAPERS/ARXIV_BRIDGE_2026_SCALING_CONNECTOMICS|ArXiv Bridge — Scaling/Connectomics]]
- [[22_RESEARCH/01_PAPERS/ARXIV_BRIDGE_2026_DIFFUSION_FEDERATED_EMBODIED|ArXiv Bridge — Diffusion/Federated/Embodied]]
- [[22_RESEARCH/01_PAPERS/ARXIV_BRIDGE_2026_QUANTUM_HARDWARE_SENSING|ArXiv Bridge — Quantum Hardware/Sensing]]
- [[22_RESEARCH/01_PAPERS/ARXIV_BRIDGE_2026_NEUROMORPHIC_TRANSFORMER|ArXiv Bridge — Neuromorphic/Transformer]]
- [[22_RESEARCH/01_PAPERS/ARXIV_BRIDGE_2026_ALIGNMENT_RAG_AGENTS|ArXiv Bridge — Alignment/RAG/Agents]]
- [[22_RESEARCH/01_PAPERS/01_PAPERS_MOC|Papers MOC]]
- [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
