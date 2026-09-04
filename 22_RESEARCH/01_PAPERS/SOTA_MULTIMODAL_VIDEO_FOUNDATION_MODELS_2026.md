---
title: "SOTA Multimodal Video Foundation Models 2026"
type: sota_synthesis
domain: [multimodal_ai, video_understanding, vision_language]
created: 2026-09-04
updated: 2026-09-04
tags:
  - sota
  - multimodal
  - video
  - vision-language
  - foundation-models
  - amos-research
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: arxiv_cvpr_2026
  scope: multimodal_video_models
confidence_ceiling: 0.95
---

# SOTA Multimodal Video Foundation Models 2026

> **Synthesis date:** 2026-09-04 · **Domain:** Multimodal AI, Video Understanding, Vision-Language Models · **Epistemic class:** SOURCE_CLAIM

## 1. Overview

Video-language foundation models have reached a new frontier in 2026, with unified architectures that jointly handle image, video, and audio understanding. The key advances are:

1. **Codec-stream tokenization** (LLaVA-OneVision-2) treating compressed video as continuous bit-cost streams
2. **Encoder-Predictor-Decoder (EPD) frameworks** (InternVideo-Next) with latent world models for video pretraining
3. **Holistic visual tokenizers** (HYDRA-X) unifying image and video tokenization in a single ViT
4. **Audiovisual correspondence learning** (PEAV) with 100M+ audio-video pair contrastive objectives
5. **Open-weight video grounding** (Molmo2) with point-driven grounding in images, multi-images, and video

These advances directly inform AMOS OS's [[15_INTERFACES/15_INTERFACES_README|interfaces plane]] and [[05_COGNITIVE_ORGANISM/04_COGNITION/04_COGNITION_MOC|cognition]] architecture.

## 2. Key Papers & Breakthroughs

### 2.1 LLaVA-OneVision-2 — Codec-Stream Video Tokenization
- **Paper:** arXiv:2605.25979 (2026)
- **Core innovation:** Codec-stream tokenization treats compressed video as a continuous bit-cost stream where bit-cost dynamics determine adaptive temporal groups and motion-residual cues select salient spatial evidence
- **Architecture:** Native OneVision-Encoder + Windowed Attention + shared 3D RoPE for unified spatiotemporal coordinates
- **Training:** ~8M re-captioned video samples for pretraining, 4M-sample spatial corpus for fine-tuning
- **Results:** JumpScore 74.9 mAP (vs Qwen3-VL-8B 30.1, +44.8 points); +4.3 avg on video tasks, +5.3 on spatial tasks, +15.6 J&F on tracking
- **AMOS alignment:** Codec-stream tokenization maps to AMOS [[10_MEMORY/10_MEMORY_MOC|memory plane]] — adaptive temporal grouping is a form of memory consolidation. The bit-cost dynamics model is analogous to AMOS [[07_SKILLS/amos-token-budget-governance/SKILL|token budget governance]].

### 2.2 InternVideo-Next — World-Understanding Video Models
- **Paper:** CVPR 2026
- **Core innovation:** Encoder-Predictor-Decoder (EPD) framework where the predictor acts as a latent world model. Two-stage pretraining: Stage 1 conditional diffusion decoder with semantic priors; Stage 2 predicts frozen Stage 1 targets
- **Key insight:** Pixel-level reconstruction conflicts with semantics; latent prediction encourages shortcut learning. EPD disentangles these by separating encoder, predictor, and decoder roles
- **Results:** SOTA across general video benchmarks with only public unlabeled videos
- **AMOS alignment:** The EPD framework maps directly to AMOS's [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O06_MODEL/O06_MODEL_MOC|O06 Model]] → [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O08_PREDICTION/O08_PREDICTION_MOC|O08 Prediction]] → [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O09_SIMULATION/O09_SIMULATION_MOC|O09 Simulation]] lifecycle. The latent world model is AMOS's [[07_SKILLS/amos-k-world-model/SKILL|K_WORLD_MODEL]].

### 2.3 HYDRA-X — Unified Image-Video Tokenization
- **Paper:** arXiv:2606.13289 (2026)
- **Core innovation:** First UMM that unifies image and video tokenization within a single ViT. Frame-level causal temporal attention suffices for reconstruction; hierarchical temporal compression outperforms single-step
- **Decompressor:** Lightweight module that upsamples temporally compressed features under joint image-video teacher supervision
- **Editing pipeline:** Source-target interaction at latent level inside tokenizer (not semantic level inside LLM) — improves consistency and convergence
- **AMOS alignment:** Unified tokenization maps to AMOS [[16_SCHEMAS/16_SCHEMAS_README|schemas plane]] — a single schema for multimodal representation. The decompressor is analogous to AMOS [[07_SKILLS/amos-hml-canon/SKILL|H/M/L canon]] (compressed H → expanded M/L).

### 2.4 PEAV — Audiovisual Perception via Contrastive Learning
- **Paper:** CVPR 2026
- **Core innovation:** Perception Encoder Audiovisual — 10 pairwise contrastive objectives across audio-video, audio-text, video-text modalities
- **Data engine:** O(100M) audio-video pairs with synthesized high-quality captions covering speech, music, and general sound effects
- **Results:** New SOTA across standard audio and video benchmarks; enables novel tasks like speech retrieval
- **AMOS alignment:** Maps to AMOS [[05_COGNITIVE_ORGANISM/04_COGNITION/04_COGNITION_MOC|cognition]] — multi-modal perception integration. The 10 pairwise objectives map to AMOS [[07_SKILLS/amos-multimodal-perception-layer/SKILL|multimodal perception layer]].

### 2.5 Molmo2 — Open-Weight Video Grounding
- **Paper:** CVPR 2026
- **Core innovation:** 7 new video datasets + 2 multi-image datasets; point-driven grounding in single image, multi-image, and video tasks
- **Key contribution:** Open weights AND open data — addresses the gap where strongest VLMs remain proprietary
- **Results:** SOTA among open-source models; exceptional point-driven grounding capabilities that even proprietary models lack
- **AMOS alignment:** Open-weight grounding maps to AMOS [[14_TOOLS/14_TOOLS_README|tools plane]] — open, auditable tools for perception. Point-driven grounding is a form of [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/O15_OBSERVATION_MOC|O15 Observation]] with spatial precision.

## 3. Architectural Implications for AMOS OS

### 3.1 Unified Multimodal Representation
The SOTA converges on unified tokenizers (HYDRA-X) and unified coordinate systems (LLaVA-OV-2's 3D RoPE). AMOS's [[16_SCHEMAS/16_SCHEMAS_README|schemas plane]] should define:
- A unified multimodal schema that handles image, video, and audio in a single representation space
- Temporal compression hierarchies aligned with H/M/L (compressed → expanded)
- Codec-stream dynamics as a memory consolidation mechanism

### 3.2 World Models as Video Pretraining
InternVideo-Next's EPD framework establishes that video pretraining is fundamentally about learning world models. AMOS's [[07_SKILLS/amos-k-world-model/SKILL|K_WORLD_MODEL]] should:
- Separate the world model (predictor) from the encoder and decoder
- Use conditional diffusion for bridging pixel fidelity with semantic abstraction
- Predict frozen Stage 1 targets to mitigate shortcut learning

### 3.3 Grounding as Observation
Molmo2's point-driven grounding establishes that precise spatial observation is a first-class capability. AMOS's [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/O15_OBSERVATION_MOC|O15 Observation]] should:
- Support point-level spatial precision, not just region-level
- Extend grounding to temporal sequences (video)
- Maintain open-weight, open-data provenance for auditability

## 4. Cross-Domain Connections

| AMOS Domain | SOTA Connection | Mapping |
|-------------|----------------|---------|
| [[15_INTERFACES/15_INTERFACES_README|Interfaces]] | All 5 papers | Multimodal perception interfaces |
| [[05_COGNITIVE_ORGANISM/04_COGNITION/04_COGNITION_MOC|Cognition]] | InternVideo-Next EPD | World model as cognition architecture |
| [[10_MEMORY/10_MEMORY_MOC|Memory]] | LLaVA-OV-2 codec streams | Adaptive temporal grouping as memory |
| [[16_SCHEMAS/16_SCHEMAS_README|Schemas]] | HYDRA-X unified tokenizer | Unified multimodal schema |
| [[14_TOOLS/14_TOOLS_README|Tools]] | Molmo2 open weights | Open auditable perception tools |
| [[07_SKILLS/amos-k-world-model/SKILL|K_WORLD_MODEL]] | InternVideo-Next | Latent world model predictor |
| [[07_SKILLS/amos-multimodal-perception-layer/SKILL|Multimodal Perception]] | PEAV 10 pairwise objectives | Cross-modal alignment |

## 5. Open Questions & Gaps

1. **Unified tokenizer efficiency:** HYDRA-X's 7B dense model is large. Can AMOS achieve unified tokenization with smaller models via [[07_SKILLS/amos-hml-canon/SKILL|H/M/L]] tiering?
2. **World model transfer:** InternVideo-Next's world model is trained on video. Can it transfer to AMOS's [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O09_SIMULATION/O09_SIMULATION_MOC|O09 Simulation]] for non-video domains?
3. **Audiovisual grounding:** No SOTA paper addresses joint audio-visual grounding (point + sound). AMOS [[15_INTERFACES/15_INTERFACES_README|interfaces]] needs this for BCI applications.
4. **Provenance for synthetic data:** PEAV uses O(100M) synthetic captions. AMOS [[07_SKILLS/amos-provenance-trust-firewall/SKILL|provenance trust firewall]] needs synthetic data provenance chains.

## 6. References

- arXiv:2605.25979 — LLaVA-OneVision-2: Towards Next-Generation Perceptual Intelligence
- CVPR 2026 — InternVideo-Next: Towards World-Understanding Video Models
- arXiv:2606.13289 — HYDRA-X: Native Unified Multimodal Models with Holistic Visual Tokenizers
- CVPR 2026 — PEAV: Pushing the Frontier of Audiovisual Perception with Large-Scale Multimodal Correspondence Learning
- CVPR 2026 — Molmo2: Open Weights and Data for Vision-Language Models with Video Understanding and Grounding

---

**Related:** [[22_RESEARCH/01_PAPERS/SOTA_TRANSFORMER_ARCHITECTURE_INNOVATIONS_2026|Transformer Innovations]] · [[22_RESEARCH/01_PAPERS/SOTA_NEURAL_SCALING_LAWS_AND_EMERGENT_ABILITIES_2026|Neural Scaling Laws]] · [[22_RESEARCH/01_PAPERS/SOTA_WORLD_MODELS_PHYSICAL_AI_2026|World Models]] · [[22_RESEARCH/01_PAPERS/SOTA_EMBODIED_AI_AND_ROBOT_LEARNING_2026|Embodied AI]]

**MOC:** [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]] · [[22_RESEARCH/01_PAPERS/01_PAPERS_MOC|01_PAPERS_MOC]]
