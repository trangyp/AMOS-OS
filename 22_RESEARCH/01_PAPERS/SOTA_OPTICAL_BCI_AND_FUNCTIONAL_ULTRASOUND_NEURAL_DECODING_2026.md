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
    - Caltech bioRxiv 2026 (fUSI cranial window motor decoding)
    - Sensors 2026 (MGFNet EEG-fNIRS fusion)
    - J Neural Eng 2026 (BiGSTF-Net, DG-ADMM source localization)
    - Nature Biomed Eng 2026 (GBF eigenmode source imaging)
    - IEEE TNSRE 2025 (wearable HD-DOT)
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
---

# SOTA Synthesis: Optical BCI, Functional Ultrasound Neural Decoding & Cross-Modal EEG-fNIRS Fusion (2026)

> **Author / Steward:** Trang Phan
> **Target OS:** `AMOS_OS v4.4`
> **Epistemic Class:** `SOURCE_CLAIM / DERIVED`
> **Date:** September 2026

---

## Abstract

Non-invasive and minimally invasive neural decoding has entered a new era driven by three converging modalities: functional ultrasound imaging (fUSI) for sub-millimeter hemodynamic decoding, high-density diffuse optical tomography (HD-DOT) for portable cortical mapping, and cross-modal EEG-fNIRS fusion networks exploiting complementary temporal and spatial resolution. The 2026 SOTA includes: fUSI through acoustically transparent cranial windows enabling single-trial digit movement decoding; MGFNet achieving 99.40% accuracy on n-back tasks via coupling-guided sparse routing; geometric basis function (GBF) eigenmodes revolutionizing electrical source imaging (ESI); wearable HD-DOT achieving 95–98% cognitive state classification at ~1 cm³ resolution; and diffusion-based language models (DELTA, MultiDiffNet) enabling non-autoregressive EEG-to-text decoding. Together, these advances bridge invasive microelectrode arrays and non-invasive scalp recording, offering a multi-scale optical-acoustic-electrical continuum for next-generation BCI.

---

## Key Findings

### 1. Functional Ultrasound Imaging (fUSI) for Single-Trial Motor Decoding (2026)
- **Spatial resolution**: Sub-millimeter mapping of deep cortical tissue through acoustically transparent PEEK cranial windows.
- **Capability**: Single-trial decoding of multi-body-part and single-digit movement encoding; cross-session decoding demonstrated. Voxel analysis reveals differential encoding across Brodmann areas.
- **Future**: Real-time 3D/4D imaging, multimodal integration, adaptive online decoding for closed-loop non-invasive BCI.
- **Reference**: Lin et al., Caltech bioRxiv, doi:10.64898/2026.07.03.735688

### 2. MGFNet: Multi-Granularity Fusion for EEG-fNIRS Decoding (2026)
- **Accuracy**: 99.40% (n-back), 99.03% (word generation) under within-subject held-out evaluation.
- **Architecture**: Intra-modal encoders → cross-modal interaction with dilated convolutions → Coupling-Guided Sparse Component Routing (CGSCR) for adaptive discrete routing.
- **Robustness**: Under -10 dB AWGN EEG corruption, outperforms static-fusion by 9.23 pp (n-back) and 6.31 pp (WG).
- **Reference**: Sensors, doi:10.3390/s26113402

### 3. BiSTF-Net & BiGSTF-Net: Bidirectional Cross-Modal Fusion (2026)
- **BiSTF-Net**: Decoupled pipeline — Bi-CMG (early spatial enhancement), ATA (adaptive temporal alignment for fNIRS delays), SCAF (symmetric cross-attention fusion); 83.33% (MA), 82.09% (MI), 84.99% (WG) cross-session.
- **BiGSTF-Net**: Modal Residual Interaction Unit + Spatio-Temporal Gated Unit; consistently outperforms fusion baselines across cross-session evaluation.
- **Reference**: J Neural Eng, doi:10.1088/1741-2552/ae9595; Brain Sci, doi:10.3390/brainsci16020241

### 4. GBF Eigenmodes for EEG/MEG Source Imaging (2026)
- **Innovation**: Patient-specific cortical surface eigenmodes as anatomic constraints for the inverse problem; whole-brain activity described by hundreds of geometric modes.
- **Validation**: Meta-source benchmark, task-evoked data, resting-state networks, intracranial stimulation, epilepsy data.
- **Temporal extension**: Eigenmode transfer functions from neural field theory introduce temporal constraints (arXiv:2609.00809).
- **DG-ADMM**: Dynamic graph-Laplacian priors with LCMV beamforming and ADMM optimization for improved MI source-space decoding.
- **Reference**: Nature Biomed Eng, doi:10.1038/s41551-026-01664-0; J Neural Eng, doi:10.1088/1741-2552/ae857e

### 5. Wearable HD-DOT for Cognitive State Assessment (2025–2026)
- **Classification**: 95.14% (fatigue/non-fatigue), 97.93% (four n-back tasks) via Random Forest with wearable HD-DOT.
- **Resolution**: ~1/2 fMRI spatial resolution; fMRI-HD-DOT correspondence 4.4 ± 1 mm; inter-optode spacing ~13 mm.
- **Real-time**: DAE-based motion artifact correction processing ~750 channels with low latency.
- **Reference**: IEEE TNSRE, doi:10.1109/tnsre.2025.3551676; Nature Sci Reports, doi:10.1038/s41598-025-85858-7

### 6. DELTA & MultiDiffNet: Diffusion-Based Neural Decoding (2026)
- **DELTA**: RVQ EEG tokenizer + LLaDA masked language diffusion; improves semantic alignment by 5.37 points over autoregressive baselines; BLEU-1 21.9 on ZuCo. Eliminates error accumulation via non-sequential denoising.
- **MultiDiffNet**: Diffusion-based compact latent space for subject-agnostic generalization across SSVEP, MI, P300, imagined speech; releases unified benchmark suite.
- **Brain-CLIPLM**: Semantic compression hypothesis — EEG preserves semantic anchors not full lexical form; 67.6% Top-5, 85.0% Top-25 sentence retrieval on ZuCo.
- **Reference**: OpenReview id:Hw3wWRyLs4; PMLR v308 (AAAI 2026); Frontiers Neurosci, doi:10.3389/fnins.2026.1899770

---

## Technical Details

### fUSI Neurovascular Coupling

Functional ultrasound measures cerebral blood volume changes via ultrafast Doppler: ΔCBV(t) ∝ ∫|S(f,t)|² df. Single-trial decoding exploits the hemodynamic lag (~3–5 s) relative to neural onset, with sub-millimeter voxel resolution enabling somatotopic mapping of individual digits.

### Cross-Modal EEG-fNIRS Fusion

```
[EEG] → Intra-modal Encoder ─┐
                              ├→ Cross-Modal Interaction (dilated conv, ATA)
[HbO/HbR] → Intra-modal Encoder ─┘
                              │
                 CGSCR (coupling-guided sparse routing)
                              │
                    [Classification Head]
```

Key challenge: fNIRS hemodynamic response peaks 3–5 s after neural onset, requiring adaptive temporal alignment (ATA) to synchronize with millisecond-level EEG.

### GBF Eigenmode Source Imaging

Neural sources expressed as linear combinations of cortical surface eigenmodes: Ĵ(t) = Σ αₖ(t)·φₖ, reducing the inverse problem from ~10,000 sources to ~hundreds of modes.

### Diffusion-Based EEG-to-Text

DELTA formulates decoding as iterative denoising: p_θ(x₀|x_t,t) = LLaDA(x_t, t, RVQ-EEG), where RVQ discretizes EEG into multi-layer tokens and the diffusion model reconstructs sentences via non-sequential masked prediction.

---

## AMOS Integration

- **Interfaces Plane**: [[15_INTERFACES/FUNCTIONAL_ULTRASOUND_NEURODECODER_LEDGER|FUNCTIONAL_ULTRASOUND_NEURODECODER_LEDGER]] — fUSI decoding pipelines; [[15_INTERFACES/CROSS_MODAL_EEG_FNIRS_FUSION_LEDGER|CROSS_MODAL_EEG_FNIRS_FUSION_LEDGER]] — multi-modal fusion; [[15_INTERFACES/HD_DIFFUSE_OPTICAL_TOMOGRAPHY_LEDGER|HD_DIFFUSE_OPTICAL_TOMOGRAPHY_LEDGER]] — optical tomography; [[15_INTERFACES/EEG_ELECTRICAL_SOURCE_IMAGING_LEDGER|EEG_ELECTRICAL_SOURCE_IMAGING_LEDGER]] — source localization; [[15_INTERFACES/BCI_DIFFUSION_LANGUAGE_MODEL_LEDGER|BCI_DIFFUSION_LANGUAGE_MODEL_LEDGER]] — diffusion neural decoding.
- **Cognitive Organism**: [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]] — sensory acquisition modalities for the cognitive organism's perception loop.
- **Domains**: [[21_DOMAINS/21_DOMAIN_MOC|21_DOMAINS]] — healthcare BCI applications and cognitive monitoring.
- **Research Map**: [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
- **Related SOTA**: [[22_RESEARCH/01_PAPERS/SOTA_NEURAL_DUST_AND_ULTRASOUND_BCI_2026|SOTA_NEURAL_DUST_AND_ULTRASOUND_BCI_2026]]; [[22_RESEARCH/01_PAPERS/SOTA_BCI_AND_NEUROTECHNOLOGY_SYNTHESIS_2026|SOTA_BCI_AND_NEUROTECHNOLOGY_SYNTHESIS_2026]]; [[22_RESEARCH/01_PAPERS/SOTA_HOLOGRAPHIC_BCI_BRAIN_MACHINE_CO_ADAPTATION_2026|SOTA_HOLOGRAPHIC_BCI_BRAIN_MACHINE_CO_ADAPTATION_2026]].

---

## References

1. Lin et al. fUSI through a human cranial window for mesoscopic mapping of motor effector encoding. Caltech bioRxiv, 2026. doi:10.64898/2026.07.03.735688
2. MGFNet: Multi-Granularity Fusion Network for Hybrid EEG-fNIRS Decoding. Sensors, 2026. doi:10.3390/s26113402
3. BiGSTF-Net: inter-modal mutual guidance for EEG-fNIRS cognitive classification. J Neural Eng, 2026. doi:10.1088/1741-2552/ae9595
4. BiSTF-Net: Decoupled Bidirectional Spatio-Temporal Fusion for EEG-fNIRS. Brain Sci, 2026. doi:10.3390/brainsci16020241
5. Liu et al. Geometry aware framework for noninvasive whole-brain dynamics. Nature Biomed Eng, 2026. doi:10.1038/s41551-026-01664-0
6. Temporally constraining source imaging with cortical eigenmodes. arXiv:2609.00809, 2026.
7. Fei et al. Dynamic graph-Laplacian priors for EEG source localization. J Neural Eng, 2026. doi:10.1088/1741-2552/ae857e
8. Wearable HD-DOT for mental fatigue and workload assessment. IEEE TNSRE, 2025. doi:10.1109/tnsre.2025.3551676
9. Ultra high density imaging arrays in DOT for human brain mapping. Nature Sci Reports, 2025. doi:10.1038/s41598-025-85858-7
10. DELTA: Language Diffusion-based EEG-to-Text Architecture. OpenReview, 2026. id:Hw3wWRyLs4
11. MultiDiffNet: Multi-Objective Diffusion Framework for Generalizable Brain Decoding. PMLR v308, AAAI 2026.
12. Brain-CLIPLM: semantic compression for EEG-to-text decoding. Frontiers Neurosci, 2026. doi:10.3389/fnins.2026.1899770
13. H2Syner: Hierarchical Multimodal Hypergraph for EEG-fNIRS Emotion Recognition. ICASSP, 2026. doi:10.1109/icassp55912.2026.11463478
14. Deep-learning real-time processing platform for fNIRS/DOT BCI. UCL Discovery, 2026. id:10219919
