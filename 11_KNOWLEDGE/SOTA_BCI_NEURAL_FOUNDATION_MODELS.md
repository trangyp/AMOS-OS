---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Sota Bci Neural Foundation Models
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

# SOTA BCI Neural Foundation Models Knowledge Engine

**Path:** `11_KNOWLEDGE/SOTA_BCI_NEURAL_FOUNDATION_MODELS.md`  
**Plane:** `11_KNOWLEDGE` (Information, Memory, State & Model Substrate)  
**Classification:** SOTA_KNOWLEDGE_NODE / DERIVED  
**Research Epoch:** 2026-09-04  
**Freshness Policy:** REVALIDATE_QUARTERLY  

---

## 1. Overview & Architectural Taxonomy

Neural foundation models represent a paradigm shift from subject-specific, task-trained linear classifiers to pre-trained, cross-subject multi-channel neural representations. As of mid-2026, over 50 BCI foundation models have been published (64% in 2025–2026 alone), marking an explosion in research activity across diverse model scopes, signal modalities, backbone architectures, and training methodologies.

In 2025–2026, foundation architectures operate across three primary recording regimes:

1. **Intracortical Spiking & LFP**: Sub-millimeter spatial resolution, $30\,\text{kHz}$ sampling rate; foundation models learn population spike rasters and continuous multi-channel field dynamics. Models like Brant (NeurIPS 2023) and UniBCI (arXiv:2605.00061) target this regime for invasive BCI applications.
2. **Subdural & Epidural Micro-ECoG**: Meso-scale cortical surface field potentials; captures local high-gamma synchronization and phonetic grid activations. Emerging hybrid ECoG-EEG foundation models attempt cross-modality transfer.
3. **Non-Invasive Scalp EEG/MEG**: The dominant modality (72% of surveyed models). Foundation models overcome volume conduction and non-stationarity through spatial graph attention, spherical-harmonics electrode embeddings, and self-supervised masked token reconstruction. Key models include DeeperBrain, B[FM]2, INCEPT, LaBraM, CBraMod, CSBrain, REVE, CoMET, FoME, and NeuroLM.

### 1.1 Critical Empirical Findings (Benchmark Synthesis)

A comprehensive 2026 benchmark audit (Liu et al., arXiv:2601.17883) evaluating 12 open-source foundation models across 13 datasets spanning 9 BCI paradigms revealed:

- **Linear probing is frequently insufficient**: Frozen-backbone evaluation often fails to match fine-tuned specialist models, suggesting current foundation models have not yet achieved truly universal representations.
- **Specialist models remain competitive**: Task-specific models trained from scratch remain competitive across many tasks, particularly motor imagery and SSVEP.
- **Larger models ≠ better generalization**: Under current data regimes and training practices, model scale does not monotonically predict downstream performance.
- **Protocol-dependent gains**: Reported improvements are often contingent on specific preprocessing, training budget, and baseline selection choices.

```text
EVIDENCE HIERARCHY FOR BCI FOUNDATION MODELS:
─────────────────────────────────────────────
PEER_REVIEWED_BENCHMARK     > VENDOR_REPORTED
CROSS_SUBJECT_PROTOCOL      > WITHIN_SUBJECT
FROZEN_PROBING_PROTOCOL     > FINE_TUNING
MULTI_DATASET_VALIDATION    > SINGLE_DATASET
COMMUNITY_REPRODUCIBLE      > PROPRIETARY
```

---

## 2. Key 2025–2026 Foundation Models & Frameworks

### 2.1 DeeperBrain: Neuro-Grounded EEG Foundation Architecture (arXiv:2601.06134)

- **Architecture**: Hierarchical spatio-temporal state space model (SSM) incorporating learnable 3D sensor channel coordinates and continuous temporal convolution.
- **Key Innovation — Neurodynamics Statistics Prediction (NSP)**: Unlike reconstruction-only objectives, DeeperBrain enforces alignment with macroscopic brain states by predicting interpretable order parameters:
  $$\mathcal{L}_{\text{NSP}} = \mathbb{E}_{\mathbf{X}} \left[ \sum_{i} \|f_i(\mathbf{Z}) - \hat{f}_i(\mathbf{Z})\|^2 \right]$$
  where $f_i$ represents spectral power, functional connectivity, cross-frequency coupling, and dynamic complexity measures.
- **Pre-training Objective — Dual Objective Strategy**:
  $$\mathcal{L}_{\text{total}} = \lambda_{\text{MER}} \mathcal{L}_{\text{MER}} + \lambda_{\text{NSP}} \mathcal{L}_{\text{NSP}}$$
  where MER (Masked EEG Reconstruction) ensures local signal fidelity:
  $$\mathcal{L}_{\text{MER}} = \mathbb{E}_{\mathbf{X}} \left[ \sum_{t \in \mathcal{M}} \|\mathbf{X}_t - \hat{\mathbf{X}}_t\|^2_2 \right]$$
  with $\mathcal{M}$ masking $40\text{--}60\%$ of time-electrode patches.
- **Performance**: State-of-the-art or highly competitive across 10 diverse downstream BCI tasks under end-to-end fine-tuning. Crucially maintains superior efficacy under rigorous frozen-probing protocol, verifying that embedding neuroscientific first principles endows learned representations with intrinsic universality.
- **Volume Conduction-Aware Channel Encoding**: Models spatial mixing via 3D geometry using learnable electrode coordinates $(x, y, z)$, directly encoding the biophysical fact that scalp EEG signals are attenuated and spatially blurred through volume conduction.

### 2.2 B[FM]2: Brain Foundation Model via Flow Matching (arXiv:2606.20812)

- **Architecture**: SplitUNet velocity network that factorizes each 2D spatiotemporal convolution into separate 1D temporal and 1D electrode convolutions, preserving electrode topology throughout the hierarchy.
- **Key Innovation — Continuous-Time Flow Matching**: Eliminates patch/tokenization discretization entirely by pretraining directly on the raw continuous multi-channel waveform via flow matching:
  $$\mathcal{L}_{\text{FM}} = \mathbb{E}_{t, \mathbf{x}_0, \mathbf{x}_1} \left[ \|v_\theta(\mathbf{x}_t, t) - (\mathbf{x}_1 - \mathbf{x}_0)\|^2 \right]$$
  where $\mathbf{x}_t = (1-t)\mathbf{x}_0 + t\mathbf{x}_1$ interpolates between Gaussian noise $\mathbf{x}_0$ and data $\mathbf{x}_1$.
- **Sample Efficiency**: Achieves SOTA on 7 of 9 standard downstream EEG classification tasks using only $36{,}895$ segments ($\approx 307$ hours) — 1–2 orders of magnitude less than existing foundation models.
- **Generative Quality**: Generates synthetic EEGs that two board-certified neurologists cannot distinguish from real brain data (Cohen's $\kappa = -0.096$).
- **SplitUNet Architecture Detail**:
  - Time-only compression: Encoder halves only temporal resolution at each of 4 stages, preserving electrode dimension $E$ throughout.
  - Attention placement: Efficient linear-attention blocks at each resolution stage, with full self-attention only at the bottleneck (time compressed by $8\times$).

### 2.3 INCEPT: Invariance-Oriented EEG Foundation Model (arXiv:2608.24597)

- **Pre-training Data**: Over 11,000 hours of unlabelled clinical EEG.
- **Key Innovation — Invariance-Oriented Pre-Training**: Rather than prioritizing signal reconstruction alone, INCEPT learns representation-level stability across correlated EEG observations, separating stable neural structure from nuisance variability while preserving subject-, state-, and condition-discriminative information.
- **Electrode Embedding**: Uses spherical-harmonics-based electrode embeddings for channel-order and montage invariance.
- **Performance**: Ranks first among recent EEG foundation models on 26 of 30 linear-probing metrics and 24 of 30 fine-tuning metrics across 10 datasets spanning signal-level assessment, brain-state decoding, and brain-health evaluation.

### 2.4 Surveyed Model Taxonomy (50 Models, 2024–2026)

| Category | Representative Models | Pre-training Paradigm | Backbone |
| :--- | :--- | :--- | :--- |
| **EEG Foundation** | DeeperBrain, B[FM]2, INCEPT, CBraMod, CSBrain, CodeBrain | Masked reconstruction / Flow matching / Invariance | Transformer, SSM, UNet |
| **EEG-Text Cross-Modal** | CET-MAE, NeuroLM, LBLM | Contrastive EEG-text masked autoencoding | Transformer |
| **Multi-Modal Brain** | BrainOmni, LaBraM, BrainLM, Brain-JEPA | Cross-modality (EEG+MEG, EEG+fMRI) | Transformer, JEPA |
| **Intracranial** | Brant, UniBCI | Self-supervised on iEEG/ECoG | Transformer |
| **Clinical** | BrainWave, FoME | Domain-specific pre-training | SSM, Transformer |
| **fMRI** | SLIM-Brain, NeuroSTORM, fMRI-LM | Voxel-level SSL + language alignment | Transformer, VAE |

---

## 3. Mathematical Encoding & Latent State Representation

### 3.1 Patch-Based Tokenization (Standard Paradigm)

Neural foundation tokenization decomposes continuous multi-lead recordings $\mathbf{Y} \in \mathbb{R}^{C \times T}$ into discrete spatio-temporal embedding vectors:

$$\mathbf{E} = \operatorname{Linear}(\mathbf{Y}_{\text{patch}}) + \mathbf{P}_{\text{spatial}}(x, y, z) + \mathbf{P}_{\text{temporal}}(t)$$

The token sequence is processed through bidirectional selective state space blocks:
$$h_k = \mathbf{\bar{A}} h_{k-1} + \mathbf{\bar{B}} \mathbf{e}_k, \quad \mathbf{z}_k = \mathbf{C} h_k + \mathbf{D} \mathbf{e}_k$$

This retains infinite-context memory of slow drifts (circadian, fatigue, medication shifts) while operating in linear $O(T)$ complexity.

### 3.2 Continuous Flow-Matching Paradigm (B[FM]2)

The flow-matching objective learns a velocity field $v_\theta(\mathbf{x}_t, t)$ that transforms Gaussian noise into the data manifold:

$$\frac{d\mathbf{x}}{dt} = v_\theta(\mathbf{x}_t, t), \quad \mathbf{x}_0 \sim \mathcal{N}(0, I), \quad \mathbf{x}_1 \sim p_{\text{data}}$$

The SplitUNet factorizes the velocity network:

$$v_\theta(\mathbf{x}_t, t) = \text{SplitUNet}(\mathbf{x}_t, t) = \text{ElectrodeConv}(\text{TemporalConv}(\mathbf{x}_t))$$

where temporal convolutions operate on the dense time axis and electrode convolutions operate on the sparse anatomically-constrained electrode axis.

### 3.3 Invariance-Oriented Representation (INCEPT)

The invariance objective enforces that essential subject-sensitive information remains stable across different observations:

$$\mathcal{L}_{\text{INV}} = \mathbb{E}_{\mathbf{x}, \mathbf{x}'} \left[ d(\text{proj}(f_\theta(\mathbf{x})), \text{proj}(f_\theta(\mathbf{x}'))) \right]$$

where $\mathbf{x}, \mathbf{x}'$ are correlated observations of the same subject and $d$ is a distance metric in representation space.

### 3.4 Failure Modes of Fixed-Encoding Classical QML (Mechanistic Analysis)

Three formal geometric mechanisms cause BCI-QML hybrid approaches to fail:

1. **Amplitude Rank Collapse**: Encoding continuous neural vectors into quantum amplitudes via fixed linear unitaries compresses feature variance into lower-dimensional subspaces.
2. **Angle Redundancy**: Periodic trigonometric parameterizations introduce artificial periodic symmetries not present in neural signal manifolds.
3. **Basis Misalignment**: Hilbert-space inner products measure global state overlap rather than task-relevant semantic distance.

---

## 4. Inner Speech Decoding Frontier (2026)

Foundation models are increasingly applied to non-invasive inner speech (IS) decoding — imagined speech without overt articulation — a critical target for locked-in syndrome communication BCIs:

| Modality | Key Foundation Models | IS Decoding Status |
| :--- | :--- | :--- |
| **EEG** | LaBraM, LBLM, CET-MAE | Limited vocabulary; near-chance for open-vocabulary |
| **MEG** | SSL speech models (wav2vec 2.0 aligned) | Cross-subject decoding improving with scale |
| **fMRI** | BrainLM, Brain-JEPA, fMRI-LM | Semantic-level decoding; low lexical accuracy |
| **fNIRS** | MindSpeech, Jung et al. 2025 | Scalable pre-training emerging; below clinical thresholds |

**Critical Challenge**: Current IS decoding remains below clinically viable thresholds for reliable communication. The shift from task-specific classification toward scalable representation learning and semantic-level decoding is underway but faces fundamental neurophysiological constraints (weak, noisy, non-stationary signals).

---

## 5. Cross-Plane Grounding in AMOS

| AMOS Plane | Component | BCI Foundation Model Integration |
| :--- | :--- | :--- |
| **10_MEMORY** | [[10_MEMORY/EPISODIC_MEMORY_SUBSTRATE\|EPISODIC_MEMORY]] | BCI latent states $\mathbf{z}_k$ indexed as episodic neural state vectors with salience scores |
| **05_COGNITIVE_ORGANISM** | [[05_COGNITIVE_ORGANISM/PERCEPTION_ENGINE\|PERCEPTION_ENGINE]] | Modality mask for direct brain-state intent translation |
| **05_COGNITIVE_ORGANISM** | [[05_COGNITIVE_ORGANISM/ATTENTION_ENGINE\|ATTENTION_ENGINE]] | Neural attention state inferred from BCI spectral features |
| **05_COGNITIVE_ORGANISM** | [[05_COGNITIVE_ORGANISM/COGNITION_ENGINE\|COGNITION_ENGINE]] | Working memory capacity inference from EEG theta/gamma coupling |
| **15_INTERFACES** | [[15_INTERFACES/BCI_EXPRESSION_GATEWAY_ADAPTER\|BCI_EXPRESSION_GATEWAY]] | Protocol adapter for BCI stream ingestion |
| **13_MODELS** | [[01_FOUNDATION_MOC|FOUNDATION_MODELS]] | Neural signal processing foundation model library |
| **22_RESEARCH** | [[22_RESEARCH/01_PAPERS/SOTA_BCI_AND_NEUROTECHNOLOGY_SYNTHESIS_2026\|SOTA_BCI_SYNTHESIS]] | Upstream empirical foundation literature |

### 5.1 BCI-to-AMOS State Pipeline

```text
RAW EEG (C × T)
    ↓ [Patch Tokenization / Flow Matching]
FOUNDATION ENCODING E ∈ R^{N × D}
    ↓ [AMOS Perception Engine]
NEURAL STATE VECTOR z_k
    ↓ [Episodic Memory Substrate]
EPISODE STORAGE + SALIENCE SCORING
    ↓ [Cognitive Engine]
WORKING MEMORY UPDATE / ATTENTION MODULATION
    ↓ [Control Plane]
AUTHORITY-GATED BEHAVIORAL OUTPUT
```

---

## 6. 2026 Frontiers: CodeBrain, C-STEM, Neuralink, Clinical Trials

### 6.1 CodeBrain (ICLR 2026)

CodeBrain introduces a novel paradigm for EEG foundation models by grounding neural representations in code embeddings:

- **Cross-modal alignment**: Maps EEG temporal patterns to programming code embeddings, enabling zero-shot classification of cognitive states associated with logical reasoning.
- **Key Innovation**: Pre-trains on paired (EEG, code) data where subjects perform programming tasks, learning representations that capture computational thinking patterns.
- **Performance**: State-of-the-art on cognitive load classification and logical reasoning state detection.
- **AMOS Relevance**: Directly applicable to `05_COGNITIVE_ORGANISM/COGNITION_ENGINE` for inferring computational reasoning states from neural signals.

### 6.2 C-STEM Online BCI

C-STEM introduces continuous, online (real-time) BCI foundation model capabilities:

- **Online adaptation**: Foundation model fine-tunes continuously as new neural data streams in, without requiring batch retraining.
- **Calibration-free transfer**: Zero-shot cross-subject transfer without per-user calibration sessions.
- **Key Innovation**: Temporal streaming transformer with causal attention that processes neural data in real-time while maintaining cross-subject representations.
- **Performance**: Maintains >85% accuracy across sessions without recalibration; approaches within-subject performance in cross-subject mode.
- **AMOS Relevance**: Enables `15_INTERFACES/BCI_EXPRESSION_GATEWAY_ADAPTER` to operate without per-subject calibration epochs.

### 6.3 Neuralink Transdural Implant

Neuralink's latest implant design addresses long-term biocompatibility:

- **Transdural approach**: Electrode threads pass through the dura mater rather than penetrating deep into cortical tissue, reducing inflammatory response.
- **1024-channel thread ASIC**: High-density recording with on-chip signal processing.
- **Key Innovation**: Reduced immune response enables chronic (>5 year) implantation with maintained signal quality.
- **Clinical Status**: Early human trials ongoing; FDA Breakthrough Device Designation for VOICE (thought-to-speech) application.
- **AMOS Relevance**: Validates long-term BCI as a viable neural interface modality for `15_INTERFACES`.

### 6.4 Clinical Trial Updates (2026)

| Trial | Status | Key Result | Date |
| :--- | :--- | :--- | :--- |
| BrainGate2 (Phase III) | Active | 99.2% WER, 125K vocabulary | Jun 2026 |
| Neuralink VOICE | FDA Breakthrough | Thought-to-speech demo | Apr 2026 |
| Synchron Pivotal | Preparing | First PMA application | Nov 2025 |
| Paradromics Connexus | FDA IDE approved | High-data-rate implant | Nov 2025 |
| Precision Layer 7 | FDA 510(k) cleared | Surface array | Apr 2025 |
| Double Neural Bypass | Published | Intracortical BCI + neuromuscular stimulation | Jun 2026 |
| Stanford Inner Speech | Published | 74% accuracy, 125K vocabulary | Aug 2025 |

### 6.5 Updated Model Taxonomy (Including 2026 Additions)

| Category | Representative Models | Pre-training Paradigm | Backbone | Added 2026 |
| :--- | :--- | :--- | :--- | :--- |
| **EEG Foundation** | DeeperBrain, B[FM]2, INCEPT, CBraMod, CSBrain | Masked reconstruction / Flow matching / Invariance | Transformer, SSM, UNet | B[FM]2, INCEPT |
| **Code-Grounded** | CodeBrain | EEG-code cross-modal alignment | Transformer | CodeBrain (ICLR 2026) |
| **Online BCI** | C-STEM | Continuous streaming adaptation | Causal Transformer | C-STEM |
| **EEG-Text Cross-Modal** | CET-MAE, NeuroLM, LBLM | Contrastive EEG-text masked autoencoding | Transformer | — |
| **Multi-Modal Brain** | BrainOmni, LaBraM, BrainLM, Brain-JEPA | Cross-modality (EEG+MEG, EEG+fMRI) | Transformer, JEPA | — |
| **Intracranial** | Brant, UniBCI | Self-supervised on iEEG/ECoG | Transformer | — |
| **Clinical** | BrainWave, FoME | Domain-specific pre-training | SSM, Transformer | — |
| **fMRI** | SLIM-Brain, NeuroSTORM, fMRI-LM | Voxel-level SSL + language alignment | Transformer, VAE | — |

---

## 7. Open Challenges & Research Frontiers

1. **Standardized Evaluation**: No community-agreed benchmark protocol exists; cross-study comparison is confounded by heterogeneous preprocessing, training budgets, and baseline selection.
2. **Frozen-Probing Gap**: Most foundation models underperform under frozen-backbone evaluation, indicating representations are not yet truly universal.
3. **Scale-Performance Decoupling**: Larger models do not necessarily yield better generalization under current data regimes.
4. **Multi-Modal Fusion**: Integration of EEG with fMRI, MEG, and fNIRS remains underexplored.
5. **Real-Time Deployment**: Latency constraints for closed-loop BCI ($\le 12.5\,\text{ms}$) conflict with transformer inference costs.
6. **Clinical Translation**: No foundation model has yet achieved FDA/CE clearance for clinical BCI deployment.
7. **Ethical & Privacy**: Neural data foundation models raise unprecedented neuroprivacy concerns.
8. **Online Adaptation**: C-STEM demonstrates feasibility but bounded update constraints and forgetting mitigation remain open.
9. **Code-Grounded Representations**: CodeBrain's code-EEG alignment is task-specific; generalizing to arbitrary cognitive domains is unexplored.
10. **Chronic Implant Longevity**: Neuralink transdural approach shows promise but 5+ year signal stability data is still accumulating.

---

## 8. Epistemic Boundary

```text
FOUNDATION_MODEL_CAPABILITY != CLINICAL_VALIDATION
BENCHMARK_PERFORMANCE     != REAL_WORLD_DEPLOYMENT
CROSS_SUBJECT_TRANSFER    != INDIVIDUAL_RELIABILITY
RECONSTRUCTION_QUALITY    != DECODING_ACCURACY
PRETRAINING_SCALE         != UNIVERSAL_REPRESENTATION
```

---

**Parent Knowledge Map:** [[11_KNOWLEDGE/11_KNOWLEDGE_MOC|11_KNOWLEDGE_MOC]]  
**Sibling SOTA Review:** [[22_RESEARCH/01_PAPERS/SOTA_BCI_AND_NEUROTECHNOLOGY_SYNTHESIS_2026|SOTA_BCI_AND_NEUROTECHNOLOGY_SYNTHESIS_2026]]  
**Related:** [[11_KNOWLEDGE/AMOS_C04_BCI_STATE_OF_ART_2026|AMOS_C04_BCI_STATE_OF_ART_2026]] · [[11_KNOWLEDGE/SOTA_EDGE_AI_NEUROMORPHIC_COMPUTING_2026|SOTA_EDGE_AI_NEUROMORPHIC_COMPUTING_2026]] · [[11_KNOWLEDGE/SOTA_AI_AGENTS_MULTI_AGENT_SYSTEMS_2026|SOTA_AI_AGENTS_MULTI_AGENT_SYSTEMS_2026]]  
**AMOS Integration:** [[15_INTERFACES/15_INTERFACES_MOC|15_INTERFACES]] · [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM]]  
**Freshness:** Last comprehensive review 2026-09-04. Revalidate quarterly against arXiv BCI corpus.
