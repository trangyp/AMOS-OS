---
title: "SOTA Synthesis: Optical BCI, Functional Ultrasound Neural Decoding & Cross-Modal EEG-fNIRS Fusion (2026)"
type: research_synthesis
paper_id: AMOS-SOTA-OPTICAL-FUS-2026
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_SYNTHESIS
epistemic_class: SOURCE_CLAIM
conclusion_class: DERIVED
rscf:
  state: SOURCE_CLAIM
  claim_class: EMPIRICAL_SURVEY
  provenance:
    - Nature Comms 2026 (fUSI BCI review, SIAT)
    - Caltech bioRxiv 2026 (fUSI cranial window motor decoding)
    - Sensors 2026 (MGFNet EEG-fNIRS fusion)
    - J Neural Eng 2026 (BiGSTF-Net, DG-ADMM source localization)
    - Nature Biomed Eng 2026 (GBF eigenmode source imaging)
    - IEEE TNSRE 2025/2026 (wearable HD-DOT)
    - Nature Sci Reports 2025 (ultra-high-density DOT)
    - OpenReview 2026 (DELTA diffusion EEG-to-text)
    - PMLR 2026 (MultiDiffNet generalizable brain decoding)
    - Frontiers Neurosci 2026 (Brain-CLIPLM semantic compression)
  scope: optical_bci_functional_ultrasound_cross_modal_neural_decoding
tags:
  - amos-os
  - research
  - sota-2026
  - optical-bci
  - functional-ultrasound
  - diffuse-optical-tomography
  - eeg-fnirs-fusion
  - electrical-source-imaging
  - diffusion-language-models
  - neural-decoding
---

# SOTA Synthesis: Optical BCI, Functional Ultrasound Neural Decoding & Cross-Modal EEG-fNIRS Fusion (2026)

> **Author / Steward:** Trang Phan
> **Target OS:** `AMOS_OS v4.4`
> **Epistemic Class:** `SOURCE_CLAIM / DERIVED`
> **Date:** September 2026

---

## Abstract

Non-invasive and minimally invasive neural decoding has entered a new era driven by three converging modalities: functional ultrasound imaging (fUSI) for sub-millimeter hemodynamic decoding, high-density diffuse optical tomography (HD-DOT) for portable cortical mapping, and cross-modal EEG-fNIRS fusion networks that exploit the complementary temporal and spatial resolution of electrophysiology and hemodynamics. The 2026 SOTA landscape includes: (1) fUSI through acoustically transparent cranial windows enabling single-trial decoding of individual digit movements at sub-millimeter resolution; (2) MGFNet achieving 99.40% accuracy on n-back tasks via coupling-guided sparse routing for EEG-fNIRS fusion; (3) geometric basis function (GBF) eigenmodes from individual cortical surfaces revolutionizing electrical source imaging (ESI) by providing compact, biologically grounded priors for the EEG inverse problem; (4) wearable HD-DOT systems achieving 95–98% cognitive state classification with ~1 cm³ volumetric resolution; and (5) diffusion-based language models (DELTA, MultiDiffNet) enabling non-autoregressive EEG-to-text decoding with improved semantic alignment. Together, these advances bridge the gap between invasive microelectrode arrays and non-invasive scalp-level recording, offering a multi-scale optical-acoustic-electrical continuum for next-generation BCI.

---

## Key Findings

### 1. Functional Ultrasound Imaging (fUSI) for Single-Trial Motor Decoding (2026)
- **Spatial resolution**: Sub-millimeter mapping of deep cortical tissue through acoustically transparent PEEK cranial windows.
- **Decoding capability**: Single-trial decoding of multi-body-part and single-digit movement encoding within primary sensorimotor cortex; cross-session decoding demonstrated.
- **Voxel analysis**: Differential encoding of single-digit movement information across Brodmann areas, bridging invasive electrophysiology and non-invasive hemodynamic imaging.
- **Future directions**: Real-time 3D/4D imaging, multimodal integration, adaptive online decoding for closed-loop non-invasive BCI.
- **Reference**: Lin et al., Caltech bioRxiv, doi:10.64898/2026.07.03.735688; SIAT review, jcjs.siat.ac.cn

### 2. MGFNet: Multi-Granularity Fusion for EEG-fNIRS Decoding (2026)
- **Accuracy**: 99.40% on n-back task, 99.03% on word generation task (within-subject held-out evaluation).
- **Architecture**: Intra-modal encoders for EEG/HbO/HbR → cross-modal interaction encoders with dilated convolutions → Coupling-Guided Sparse Component Routing (CGSCR) for adaptive discrete routing.
- **Robustness**: Under EEG corruption at -10 dB AWGN, MGFNet outperforms static-fusion variant by 9.23 percentage points (n-back) and 6.31 percentage points (WG).
- **Reference**: Sensors, doi:10.3390/s26113402

### 3. BiGSTF-Net & BiSTF-Net: Bidirectional Cross-Modal EEG-fNIRS Fusion (2026)
- **BiGSTF-Net**: Modal Residual Interaction Unit for bidirectional inter-modal guidance + Spatio-Temporal Gated Unit for intra-modal integration; consistently outperforms fusion baselines across cross-session evaluation.
- **BiSTF-Net**: Decoupled pipeline with Bi-CMG (early spatial enhancement), ATA (adaptive temporal alignment for subject-specific fNIRS delays), and SCAF (symmetric cross-attention fusion); achieves 83.33% (MA), 82.09% (MI), 84.99% (WG) cross-session accuracy.
- **Reference**: J Neural Eng, doi:10.1088/1741-2552/ae9595; Brain Sci, doi:10.3390/brainsci16020241

### 4. Geometric Basis Function (GBF) Eigenmodes for EEG/MEG Source Imaging (2026)
- **Innovation**: Patient-specific geometric eigenmodes derived from individual cortical surfaces serve as anatomic constraints for the inverse problem.
- **Validation**: Meta-source benchmark, task-evoked data, resting-state networks, intracranial stimulation, and epilepsy data.
- **Result**: High localization accuracy; whole-brain activity described by hundreds of geometric modes — compact yet accurate representation.
- **Temporal extension**: Eigenmode transfer functions from neural field theory introduce temporal constraints into source imaging (arXiv:2609.00809).
- **Reference**: Nature Biomed Eng, doi:10.1038/s41551-026-01664-0; arXiv:2609.00809

### 5. Dynamic Graph-Laplacian EEG Source Localization (2026)
- **Framework**: DG-ADMM combines LCMV beamforming, ROI-level PCA, dynamic phase synchronization graphs, and graph-Laplacian regularization via ADMM optimization.
- **Result**: Spatially concentrated, physiologically plausible source patterns; improved source-space motor imagery decoding on PhysioNet.
- **Reference**: J Neural Eng, doi:10.1088/1741-2552/ae857e

### 6. Wearable HD-DOT for Cognitive State Assessment (2025–2026)
- **Mental fatigue/workload**: Random Forest classification achieving 95.14% (fatigue/non-fatigue) and 97.93% (four n-back tasks) using wearable HD-DOT.
- **Spatial resolution**: ~1/2 that of fMRI with inter-optode spacing ~13 mm; fMRI-HD-DOT correspondence as close as 4.4 ± 1 mm.
- **Ultra-high-density arrays**: Simulations show further improvement in image quality and decoding performance with denser grids.
- **Real-time platform**: DAE-based motion artifact correction processing ~750 channels in real-time with low latency.
- **Reference**: IEEE TNSRE, doi:10.1109/tnsre.2025.3551676; Nature Sci Reports, doi:10.1038/s41598-025-85858-7

### 7. DELTA: Diffusion-Based EEG-to-Text Decoding (2026)
- **Architecture**: RVQ EEG tokenizer → LLaDA masked language diffusion model for non-sequential denoising.
- **Result**: Improves semantic alignment by up to 5.37 points over autoregressive baselines; BLEU-1 21.9, ROUGE-1 F 17.2 on ZuCo.
- **Advantage**: Eliminates error accumulation of autoregressive decoding; robust to noisy EEG via hierarchical quantization.
- **Reference**: OpenReview, id:Hw3wWRyLs4

### 8. MultiDiffNet: Generalizable Diffusion Brain Decoding (2026)
- **Framework**: Diffusion-based compact latent space optimized for multiple objectives; bypasses generative augmentation.
- **Benchmark**: Unified suite spanning SSVEP, Motor Imagery, P300, and Imagined Speech with subject/session-disjoint evaluation.
- **Result**: State-of-the-art subject-agnostic generalization across four EEG decoding tasks.
- **Reference**: PMLR v308, AAAI 2026 NeuroAI Workshop

### 9. Brain-CLIPLM: Semantic Compression for EEG-to-Text (2026)
- **Hypothesis**: Non-invasive EEG preserves recoverable semantic anchors, not full lexical-syntactic form.
- **Result**: 67.6% Top-5, 85.0% Top-25 sentence retrieval on ZuCo; EEG-derived anchors carry sentence-specific information beyond LLM priors.
- **Reference**: Frontiers Neurosci, doi:10.3389/fnins.2026.1899770

---

## Technical Details

### fUSI Neurovascular Coupling Model

Functional ultrasound imaging captures cerebral blood volume changes via ultrafast Doppler:

$$\Delta \text{CBV}(t) \propto \int_{f_{\text{Doppler}}} |S(f, t)|^2 \, df$$

Single-trial decoding exploits the hemodynamic response lag (~3–5 s) relative to neural onset. Sub-millimeter voxel resolution enables somatotopic mapping of individual digit representations, with cross-session stability enabling practical BCI deployment.

### HD-DOT Image Reconstruction

Diffuse optical tomography reconstructs 3D hemodynamic images from near-infrared measurements at multiple source-detector separations (13–40 mm). The modified Beer-Lambert law converts attenuation changes to HbO/HbR concentration changes:

$$\Delta A = \epsilon \cdot \Delta c \cdot d \cdot \text{DPF} + G$$

where DPF is the differential path length factor and G accounts for scattering geometry. Pre-calculated inverse Jacobian matrices enable real-time 3D reconstruction with DAE-based motion artifact correction.

### Cross-Modal EEG-fNIRS Fusion Architecture

```
[EEG Stream] → Intra-modal Encoder (spatiotemporal) ─┐
                                                       ├→ Cross-Modal Interaction (dilated conv, temporal alignment)
[HbO/HbR Stream] → Intra-modal Encoder (hemodynamic) ─┘
                                                       │
                                          CGSCR (coupling-guided sparse routing)
                                                       │
                                              [Adaptive Discrete Routing]
                                                       │
                                              [Classification Head]
```

Key challenge: fNIRS hemodynamic response peaks 3–5 s after neural onset, requiring adaptive temporal alignment (ATA) to synchronize with millisecond-level EEG.

### GBF Eigenmode Source Imaging

The EEG inverse problem is constrained by expressing neural sources as linear combinations of geometric basis functions derived from cortical surface eigenmodes:

$$\hat{\mathbf{J}}(t) = \sum_{k=1}^{K} \alpha_k(t) \cdot \boldsymbol{\phi}_k$$

where φ_k are the geometric eigenmodes and α_k(t) are time-varying coefficients. This reduces the inverse problem dimensionality from ~10,000 cortical sources to ~hundreds of modes, improving stability and localization accuracy.

### Diffusion-Based Neural Decoding

DELTA formulates EEG-to-text as iterative denoising in token space:

$$p_\theta(\mathbf{x}_0 | \mathbf{x}_t, t) = \text{LLaDA}(\mathbf{x}_t, t, \text{RVQ-EEG})$$

where RVQ discretizes continuous EEG into multi-layer tokens, and the diffusion model reconstructs sentences via non-sequential masked prediction, avoiding autoregressive error accumulation.

---

## AMOS Integration

- **Interfaces Plane**: Directly informs [[15_INTERFACES/FUNCTIONAL_ULTRASOUND_NEURODECODER_LEDGER|FUNCTIONAL_ULTRASOUND_NEURODECODER_LEDGER]] for fUSI decoding pipelines; [[15_INTERFACES/CROSS_MODAL_EEG_FNIRS_FUSION_LEDGER|CROSS_MODAL_EEG_FNIRS_FUSION_LEDGER]] for multi-modal fusion architectures; [[15_INTERFACES/HD_DIFFUSE_OPTICAL_TOMOGRAPHY_LEDGER|HD_DIFFUSE_OPTICAL_TOMOGRAPHY_LEDGER]] for optical tomography; [[15_INTERFACES/EEG_ELECTRICAL_SOURCE_IMAGING_LEDGER|EEG_ELECTRICAL_SOURCE_IMAGING_LEDGER]] for source localization; [[15_INTERFACES/BCI_DIFFUSION_LANGUAGE_MODEL_LEDGER|BCI_DIFFUSION_LANGUAGE_MODEL_LEDGER]] for diffusion-based neural decoding.
- **Cognitive Organism Plane**: Feeds into [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]] as sensory acquisition modalities for the cognitive organism's perception loop.
- **Domains Plane**: Relevant to [[21_DOMAINS/21_DOMAIN_MOC|21_DOMAINS]] for healthcare BCI applications and cognitive monitoring systems.
- **Research Master Map**: [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
- **Related SOTA**: [[22_RESEARCH/01_PAPERS/SOTA_NEURAL_DUST_AND_ULTRASOUND_BCI_2026|SOTA_NEURAL_DUST_AND_ULTRASOUND_BCI_2026]] — companion paper on ultrasonic neural dust; [[22_RESEARCH/01_PAPERS/SOTA_BCI_AND_NEUROTECHNOLOGY_SYNTHESIS_2026|SOTA_BCI_AND_NEUROTECHNOLOGY_SYNTHESIS_2026]] — broader BCI synthesis; [[22_RESEARCH/01_PAPERS/SOTA_HOLOGRAPHIC_BCI_BRAIN_MACHINE_CO_ADAPTATION_2026|SOTA_HOLOGRAPHIC_BCI_BRAIN_MACHINE_CO_ADAPTATION_2026]] — holographic BCI co-adaptation.

---

## References

1. Lin et al. Functional ultrasound imaging through a human cranial window for mesoscopic mapping of motor effector encoding. Caltech bioRxiv, 2026. doi:10.64898/2026.07.03.735688
2. Functional Ultrasound Imaging-Based BCI Technologies and Applications. SIAT, 2026. jcjs.siat.ac.cn/en/article/cstr/32239.14.j.issn.2095-3135.20260629001
3. MGFNet: A Multi-Granularity Fusion Network with Coupling-Guided Sparse Routing for Hybrid EEG-fNIRS Decoding. Sensors, 2026. doi:10.3390/s26113402
4. BiGSTF-Net: inter-modal mutual guidance and intra-modal spatio-temporal fusion for EEG-fNIRS cognitive classification. J Neural Eng, 2026. doi:10.1088/1741-2552/ae9595
5. BiSTF-Net: Decoupled Bidirectional Spatio-Temporal Fusion Network for Hybrid EEG-fNIRS Cognitive Task Classification. Brain Sci, 2026. doi:10.3390/brainsci16020241
6. Liu et al. A geometry aware framework enhances noninvasive mapping of whole human brain dynamics. Nature Biomed Eng, 2026. doi:10.1038/s41551-026-01664-0
7. Temporally constraining source imaging estimates with eigenmodes of cortical geometry. arXiv:2609.00809, 2026.
8. Fei et al. Dynamic functional graph-Laplacian priors integrated with optimization for EEG source localization. J Neural Eng, 2026. doi:10.1088/1741-2552/ae857e
9. Simultaneous Mental Fatigue and Mental Workload Assessment With Wearable HD-DOT. IEEE TNSRE, 2025. doi:10.1109/tnsre.2025.3551676
10. Ultra high density imaging arrays in diffuse optical tomography for human brain mapping. Nature Sci Reports, 2025. doi:10.1038/s41598-025-85858-7
11. DELTA: Language Diffusion-based EEG-to-Text Architecture. OpenReview, 2026. id:Hw3wWRyLs4
12. MultiDiffNet: A Multi-Objective Diffusion Framework for Generalizable Brain Decoding. PMLR v308, AAAI 2026 NeuroAI Workshop.
13. Brain-CLIPLM: semantic compression for EEG-to-text decoding. Frontiers Neurosci, 2026. doi:10.3389/fnins.2026.1899770
14. H2Syner: Hierarchical Multimodal Hypergraph Learning Network for EEG-fNIRS Emotion Recognition. ICASSP, 2026. doi:10.1109/icassp55912.2026.11463478
15. A deep-learning empowered, real-time processing platform of fNIRS/DOT for BCI and neurofeedback. UCL Discovery, 2026. id:10219919
