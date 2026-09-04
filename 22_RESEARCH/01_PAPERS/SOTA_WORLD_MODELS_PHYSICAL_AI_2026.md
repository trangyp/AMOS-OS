---
title: SOTA World Models Physical AI 2026
type: research_synthesis
source: 22_RESEARCH/01_PAPERS
tags:
  - sota
  - world-models
  - physical-ai
  - robotics
  - embodied-ai
  - research
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: web_search_2026-09-04
  scope: world_models_physical_ai_2026
  freshness: 2026-09-04
  falsifier: "World model performance validated in simulation — real-world generalization to unstructured environments NOT ESTABLISHED"
---

# SOTA World Models & Physical AI 2026

**Date:** 2026-09-04
**Epistemic class:** SOURCE_CLAIM (arXiv preprints)
**Confidence ceiling:** 0.85

## 1. CLAP — Cross-Embodiment Video World Models (arXiv:2608.27406)

- **Innovation:** Cross-embodiment action-conditioned video generation from internet-scale data
- **Action spaces:** End-effector poses, language instructions, latent actions
- **Curriculum:** Latent actions first (unlabeled video) → end-effector grounding (zero-shot deployment)
- **Performance:** Approaches/surpasses single-embodiment SOTA on DROID
- **AMOS binding:** `13_MODELS` — substrate-independent world model

## 2. Riemann-1.0 — Embodied World Action Model (arXiv:2608.27033)

- **Architecture:** Fully causal autoregressive; unified policy + simulator
- **Data:** 200K+ hours interaction data; egocentric human + handheld-gripper + robot trajectories
- **Performance:** 94.3% RoboTwin2.0, 99.0% LIBERO, 62.6% RoboCasa-365, 85.0% real-world long-horizon
- **AMOS binding:** `05_COGNITIVE_ORGANISM` — unified acting + simulating cognitive organism

## 3. DreamX-Phi 1.0 — Geometry-Aware Video WM (arXiv:2608.13489)

- **Geometry:** SE(3) transformations via PRoPE attention; rigid-motion structure preservation
- **Consistency:** SAM3 masks + frozen V-JEPA teacher for object persistence
- **Efficiency:** Distribution-matching distillation for few-step deployment
- **Ranking:** 1st Track 1, 2nd Track 2 WorldArena 2.0 Challenge
- **AMOS binding:** `13_MODELS` — physics-respecting world simulation

## 4. GeniWorld — Generalizable Interactive WM (arXiv:2608.06332)

- **Actions:** URDF-based visual action representations
- **Decoupling:** Embodiment kinematics separated from environmental dynamics
- **Control:** Autoregressive video prediction + high-frequency kinematic control
- **Generalization:** Zero-shot to highly randomized unseen environments
- **AMOS binding:** `19_TESTS` — scalable policy evaluator under perturbation

## 5. Xiaomi-Robotics-U0 — Unified Embodied Synthesis (arXiv:2607.11643)

- **Scale:** 38B parameter multimodal autoregressive
- **Tasks:** Text-to-image, image editing, embodied scene/transfer/video generation
- **Innovation:** First multi-view scene generation across multiple robot embodiments
- **AMOS binding:** `13_MODELS` — foundation world model for embodied AI

## AMOS Architecture Mapping

| WM Component | AMOS Plane | Mapping |
|--------------|-----------|---------|
| Cross-embodiment learning | `13_MODELS` | Substrate-independent model |
| Causal state transitions | `04_RUNTIME` | Causal runtime execution |
| Unified policy + simulator | `05_COGNITIVE_ORGANISM` | Dual-role cognitive organism |
| SE(3) geometric encoding | `16_SCHEMAS` | Spatial schema enforcement |
| Object consistency (SAM3) | `17_OBSERVABILITY` | Persistent object tracking |
| Policy evaluation under perturbation | `19_TESTS` | Bounded testing framework |
| Progressive embodied pretraining | `23_OPERATING_MODEL` | Staged learning operating model |

## Falsifiers

- `F-WM-1`: CLAP cross-embodiment zero-shot is in simulation — real-world transfer NOT ESTABLISHED
- `F-WM-2`: Riemann-1.0 85% real-world success on specific tasks — unstructured environment generalization NOT ESTABLISHED
- `F-WM-3`: DreamX-Phi SE(3) encoding preserves rigid motion — deformable object handling NOT ESTABLISHED
- `F-WM-4`: GeniWorld zero-shot OOD generalization with fixed-scene training — multi-scene training scalability NOT ESTABLISHED
- `F-WM-5`: Xiaomi-U0 38B model — inference latency and deployment feasibility on edge devices NOT ESTABLISHED

**Parent:** [[22_RESEARCH/01_PAPERS/SOTA_BCI_AI_QUANTUM_SYNTHESIS_2026|SOTA_BCI_AI_QUANTUM_SYNTHESIS_2026]] · [[22_RESEARCH/22_RESEARCH_README|22_RESEARCH_README]]
