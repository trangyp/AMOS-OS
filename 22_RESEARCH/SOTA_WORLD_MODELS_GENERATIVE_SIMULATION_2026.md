---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Sota World Models Generative Simulation 2026
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

# SOTA Research Synthesis: World Models and Generative World Simulation (2026)

## 1. Executive Summary

The world model paradigm reached an inflection point between late 2025 and mid-2026. Three thresholds were crossed simultaneously: **real-time interactivity** (Genie 3, Aug 2025), **persistent 3D artifacts** (World Labs Marble, Nov 2025), and **open physical-AI foundation models** (NVIDIA Cosmos 3, 2026). In parallel, Yann LeCun departed Meta (Nov 2025) to found AMI Labs with a $1.03B seed round (Mar 2026), explicitly betting that world models—not LLMs—are the path to general intelligence.

The field now spans four functionally distinct camps (per World Labs' June 2026 taxonomy):

| Camp | Function | Key Systems |
|------|----------|-------------|
| **Renderers** | Generate photorealistic observations | Sora (discontinued Apr 2026), Veo 3.1, Kling 3.0 |
| **Simulators** | Produce geometrically/physically faithful state | NVIDIA Cosmos, World Labs Marble/Atlas |
| **Planners** | Output actions given observations + goals | DreamerV3, TD-MPC2, Cosmos Policy, Riemann-1.0 |
| **Predictive abstractions** | Learn latent dynamics for planning | JEPA family, V-JEPA 2, Causal-JEPA |

The convergence thesis—that a single architecture will eventually serve all four functions—is now the dominant research vector. World Labs' Atlas (Sep 2026), a multimodal autoregressive diffusion transformer operating natively on text, images, video, and 3D, represents the most aggressive push toward this unified model.

---

## 2. Key Systems and Architectures

### 2.1 World Labs Atlas (Sep 2026)

Atlas is an omni world model pretrained from scratch on multimodal data. Architecture: **multimodal autoregressive diffusion transformer** where all inputs are combined into a shared spatial context grounded at 3D positions.

**Capabilities:**
- Camera-controlled video generation (up to 1 minute at 1440p)
- Spatial reconstruction from 1–dozens of input images (outperforms specialized 3D reconstruction models)
- Space-time simulation (Real-to-Sim for robotics)
- Native 3D output as point clouds and Gaussian splats

**Scale evidence:** Performance improves with training compute; scaling trend expected to hold.

> "The same bet the field has been making since the late 1980s—that a sufficiently rich model of the world is all that any agent needs to see worlds, build them, and act in them—is the bet now driving an entire generation of research." — World Labs, Jun 2026

### 2.2 NVIDIA Cosmos (2025–2026)

Cosmos is a platform of world foundation models (WFMs) purpose-built for physical AI. Key components:

- **Cosmos-Predict**: Text/image-to-video generation
- **Cosmos-Transfer**: Sim-to-real translation
- **Cosmos-Reason**: Reasoning about future states
- **Cosmos 3 (2026)**: Open omnimodel (mixture-of-transformers) generating text, image, video, ambient sound, and actions; downloadable from Hugging Face

By Jan 2026: >2M downloads. Designed to plug into NVIDIA Isaac Sim and feed training data to GR00T humanoid robots.

### 2.3 Google DeepMind Genie 3 (Aug 2025)

First real-time interactive general-purpose world model:
- **720p at 20–24 fps** real-time generation
- Consistency maintained for several minutes (memory extends ~1 minute back)
- Promptable world events (text-driven environmental changes)
- Tested with SIMA agent for goal-directed exploration

**Limitations acknowledged:** Limited agent action space, imperfect multi-agent simulation, no geographic accuracy, limited continuous interaction duration.

### 2.4 OpenAI Sora → Sora 2 (2024–2026)

Sora pioneered video-generation-as-world-simulation. Sora 2 improved physics compliance (rigid-body, fluid dynamics, object permanence).

**Critical status change:** OpenAI discontinued the Sora consumer app (Apr 26, 2026) and announced API shutdown (Sep 24, 2026). Sora survives only as a rate-limited ChatGPT feature. This marks a significant market signal about the commercial viability of pure generative video models.

### 2.5 Google Veo 3.1 (2025–2026)

Veo 3.1 (Google DeepMind) is now the dominant active video generation model:
- Native 4K at 60fps output
- Native audio/dialogue with lip-sync (8 languages)
- First-last-frame control, 60-second scene extension
- Ingredients-to-video (3-image multi-reference for consistency)
- Integrated into Gemini ecosystem

### 2.6 Riemann-1.0 (Aug 2026)

A fully causal autoregressive **World Action Model** for embodied intelligence:
- Jointly models multi-view visual observations, robot states, and actions
- Functions as both executable robot policy AND multi-embodiment visual world simulator
- Progressive embodied pretraining from egocentric human videos, gripper demonstrations, and robot trajectories
- 200K+ hours of interaction data
- SOTA: 94.3% RoboTwin2.0, 99.0% LIBERO, 85.0% real-world manipulation SR

### 2.7 Other Notable Systems

| System | Lab | Focus | Index |
|--------|-----|-------|-------|
| V-JEPA 2 | Meta FAIR | Self-supervised video world model | 87/100 |
| UniSim | DeepMind | Action-conditioned video simulator | 72/100 |
| DIAMOND | MSFT/Unige | Model-based RL | 64/100 |
| Decart Oasis | Decart | Minecraft-style playable model | — |
| Wayve GAIA-2 | Wayve | Driving simulator | — |
| BWM | Open-source | Low-cost high-fidelity robot simulator | #1 WorldArena Track 1 (open) |

---

## 3. JEPA Framework Evolution

### 3.1 Architecture Lineage

The JEPA (Joint-Embedding Predictive Architecture) family represents the **predictive abstraction** camp—models that predict in learned representation space rather than pixel space.

**Key papers (2025–2026):**

1. **LeJEPA** (Balestriero & LeCun, Nov 2025): Provable, scalable self-supervised learning via Sketched Isotropic Gaussian Regularization (SIGReg). Eliminates ad-hoc heuristics. [arXiv:2511.08544]

2. **EB-JEPA** (Meta FAIR, Feb 2026): Open-source library for energy-based JEPAs. Self-contained implementations for image representation learning, video prediction, and action-conditioned world models. Achieves 97% planning success on Two Rooms task. [arXiv:2602.03604]

3. **Rectified LpJEPA** (Kuang, Dagade, Rudner, Balestriero, LeCun, Feb 2026): Introduces Rectified Distribution Matching Regularization (RDMReg) targeting Rectified Generalized Gaussian distributions. Enables controllable sparsity and non-negativity in representations. [arXiv:2602.01456]

4. **LLM-JEPA** (Huang, LeCun, Balestriero, Sep 2025): First JEPA-style training objective for LLMs. Combines generative loss with embedding-space prediction across paired views (e.g., text ↔ code). Outperforms standard training across Llama3, Gemma2, OpenELM, Olmo families. [arXiv:2509.14252]

5. **VL-JEPA** (Chen et al., Dec 2025): Vision-language JEPA predicting continuous text embeddings. 50% fewer trainable parameters than standard VLMs while outperforming CLIP, SigLIP2, and Perception Encoder on video classification/retrieval. [arXiv:2512.10942]

6. **Var-JEPA** (Gögl & Yau, Mar 2026): Variational formulation bridging JEPA and generative modeling. Shows standard JEPA is a deterministic specialization of coupled VAE. Provides ELBO objective that naturally prevents collapse. [arXiv:2603.20111]

7. **Causal-JEPA (C-JEPA)** (Nam, Le Lidec, Maes, LeCun, Balestriero, Feb 2026): Object-level masking induces causal inductive bias via latent interventions. +20% absolute gain on counterfactual reasoning. Uses only 1.02% of patch-based token count for 8× faster planning. [arXiv:2602.11389]

### 3.2 The JEPA ↔ Generative Debate

The core architectural fork in 2026:

- **Pixel-space prediction** (Sora-lineage): Reconstructs pixels. Renders beautifully, expensive to serve.
- **Latent-space prediction** (JEPA-lineage): Predicts in learned latent space. Never renders. Cheap. LeCun argues correct substrate for planning: "a planner does not care what the frame looks like, only what state it implies."

LeCun's departure from Meta and founding of AMI Labs represents the institutional commitment to this thesis.

---

## 4. Mathematical Foundations

### 4.1 Predictive Coding and Free Energy Principle

The **Free Energy Principle** (Friston, 2005–present) provides the deepest theoretical foundation for world models:

- Systems maintaining structural/functional integrity can be described as minimizing **Variational Free Energy (VFE)**
- Perception, action, planning, and learning are unified under a single computational objective
- VFE = complexity − accuracy (KL divergence from prior + negative log-likelihood)

**2026 developments:**

- **Active Inference World Models** (Zenodo, Jul 2026): Extends reactive sensorimotor coordination toward structured belief systems. Agents use semantic priors, update beliefs through evidence, and balance pragmatic goal fulfillment against epistemic uncertainty reduction.

- **Active Inference as Test-Time Scaling Law** (Hashash et al., Jun 2026): Derives a scaling law for physical AI agents where reasoning reduces prediction errors at test time. Policy updates modeled as soft Bayesian inference. Outperforms model-free Q-learning and model-based BRL in autonomous driving tasks. Inference efficiency improved by >36%.

- **Active Inference for Physical AI** (de Vries, Mar 2026): Engineering perspective showing VFE minimization realized via reactive message passing on factor graphs. Event-driven, interruptible, locally adaptable—well matched to physical operation constraints.

- **Phenotyping Agency in AI** (Wilson, Friston et al., Apr 2026): Formalizes intentionality, rationality, and explainability in active inference agents using POMDPs. Expected Free Energy unifies goal-seeking and information-gathering.

### 4.2 Formal Frameworks

**Core equations:**

```
VFE[q] = KL[q(θ) || p(θ)] − 𝔼_q[log p(D|θ)]    (Variational Free Energy)

EFE[π] = 𝔼_{q(s,o|π)} [D_KL[q(s,o|π) || p(o|s,C)q(s|π)]    (Expected Free Energy)

G(π) = Pragmatic value + Information gain
```

Where pragmatic value drives goal-directed behavior and information gain drives epistemic exploration.

### 4.3 JEPA Formal Foundations

**LeJEPA** establishes that isotropic Gaussian embeddings are minimax-optimal for downstream prediction via SIGReg (Sketched Isotropic Gaussian Regularization).

**Rectified LpJEPA** generalizes this to Rectified Generalized Gaussian distributions:

```
RGG(x; μ, σ, p) ∝ max(0, |x − μ|)^p · exp(−(|x − μ|/σ)^p)    (RGG density)

Objective: Align representations to RGG via sliced two-sample distribution matching
```

This enables controllable sparsity while preserving maximum entropy under expected ℓp norm constraints.

**Var-JEPA** establishes the equivalence:

```
Standard JEPA ≡ Deterministic specialization of coupled VAE with learned conditional prior
```

This bridges predictive and generative self-supervision under a single ELBO objective.

---

## 5. Spatial Intelligence and 3D Understanding

### 5.1 SenseNova-SI (CVPR 2026)

Cai et al. establish a **data-centric scaling law** for spatial intelligence using 8M samples (SenseNova-SI-8M) across five domains:

1. Metric Measurement (MM)
2. Spatial Relations (SR)
3. Mental Reconstruction (MR)
4. Perspective-taking (PT)
5. Comprehensive Reasoning (CR)

**Key findings:**
- Scaling law governs spatial intelligence progression
- Emergent generalization: spatial task training transfers to unrelated tasks
- Spatial chain-of-thought may NOT be effective—text CoT fails to improve spatial reasoning
- Models retain general multimodal capabilities after spatial training

### 5.2 SpatialTree (CVPR 2026)

Four-level capability hierarchy:
- **L1**: Low-level perception
- **L2**: Mental mapping
- **L3**: Simulation
- **L4**: Spatial agent (action execution)

Critical finding: extensive reasoning is indispensable for complex tasks but **detrimental to intuitive perception** (over-thinking degrades precision). Proposes auto-think strategy: suppress reasoning for perception, encourage it for planning.

### 5.3 SSR (Feb 2026)

7B-parameter spatial intelligence model with LocalCogMap (local cognitive map)—a 10×10 grid-based scene graph representation. Achieves 73.9 on VSI-Bench, outperforming models 35× larger.

### 5.4 Qwen-3D (ECCV 2026)

Geometry-aware LMM that:
- Applies 3D Rotary Positional Embeddings (attention in scene space, not frame space)
- Compresses multi-view observations into persistent scene tokens via voxel pooling (~5cm)
- Shared mask decoder for grounding and segmentation
- Only ~50M new trainable parameters via LoRA + mask decoder

### 5.5 SpatialEvo (Apr 2026)

Self-evolving framework exploiting a key insight: **ground truth for 3D spatial reasoning is deterministic**—computable from point clouds and camera poses without model involvement. The Deterministic Geometric Environment (DGE) formalizes 16 spatial task categories as verifiable oracles, enabling noise-free RL without human annotation.

---

## 6. Embodied AI and Sim-to-Real Transfer

### 6.1 World-Action Models

**Riemann-1.0** (Aug 2026) and **CLAP** (Aug 2026) represent the frontier of unified world-action models:

- **Riemann-1.0**: Causal autoregressive model jointly predicting observations, states, and actions. Progressive pretraining from human videos → gripper demos → robot trajectories.
- **CLAP**: Cross-embodiment framework reconciling disparate action spaces via end-effector poses, language instructions, and latent actions. Curriculum-based learning: foundational physics priors → grounded end-effector actions → zero-shot deployment.
- **AnyWorld** (Aug 2026): Factorizes interaction into action + camera + embodiment factors, enabling independent recomposition.

### 6.2 Sim-to-Real Transfer Breakthroughs

**SimDist** (Levy et al., Mar 2026):
- Distills structural priors from physics simulators into world models
- Pretrains encoder, reward model, and value function in simulation
- Real-world adaptation: only updates latent dynamics model (frozen encoder/reward/value)
- Outperforms prior RL finetuning methods that often collapse

**Cosmos Policy Sim-to-Real** (Schmeckpeper, Jun 2026):
- First successful zero-shot sim-to-real transfer of a world-action model
- 35% success rate from purely synthetic priors (800 synthetic demos per task)
- Outperforms Diffusion Policy trained on 50 real-world demonstrations

**WoVR** (Jiang et al., Feb 2026):
- Hallucination-aware world-model RL for VLA post-training
- Keyframe-Initialized Rollouts (KIR) reduce effective error depth
- PACE: Policy-Aligned Co-Evolution prevents distribution drift
- Real-robot success: 91.7% (vs 61.7% base VLA policy)

### 6.3 The Planner Problem

World Labs identifies the planner as "the most intriguing and most nascent" component. Their assessment (Jun 2026):

> "Almost all [robotic demos] have been confined to heavily constrained laboratory setups, with narrow object sets and short task horizons. None have been validated at the complexity, variability, or duration that real-world deployment demands. The gap between a compelling demo reel and a robot that reliably works in a kitchen, a warehouse, or an operating room remains vast."

---

## 7. Causal World Models and Intervention-Based Learning

### 7.1 The Intervention Gap

**"The Intervention Gap in Latent World Models"** (Aug 2026): Key empirical finding—planning-time intervention fidelity is a **distinct, measurable property** separate from reward fit. Across TD-MPC2 checkpoints, episode return falls as operator-error grows while reward-prediction error stays small. A self-supervised world model preserves intervention fidelity substantially better than task-anchored models.

### 7.2 Causal Architectures

**Causal-JEPA** (Feb 2026): Object-level masking as latent intervention during training. Makes interaction reasoning functionally necessary. +20% on counterfactual reasoning, 8× faster planning.

**CausalVAE as World Model Plugin** (Apr 2026): Structural causal disentanglement module attached to encoder-transition backbones. Maintains factual prediction while improving counterfactual retrieval (+102.5% CF-H@1 on Physics benchmark).

**CAER** (Aug 2026): Causal Action Effect Reweighting—redistributes supervision toward tokens whose predicted future is causally affected by the action. Online signal, no external annotations.

**Causal Process Models** (2026): Reframes dynamic causal graph discovery as multi-agent RL. Agents sequentially decide which objects are causally connected at each timestep. Sparse, time-varying interaction graphs outperform dense message-passing baselines.

**Unifying Perspective on Causal WMs** (Aug 2026): Formalizes Causal World Models (CWMs) as structured decision models linking observations → representations → causal structure → interventions. Establishes component-wise identifiability requirements.

### 7.3 Self-Evolving Cognitive Framework (Jun 2026)

Proposes transition from **predictive intelligence** to **epistemic intelligence**:
- Causal world modeling + intervention-driven reasoning + continual cognitive refinement
- Embodied interaction as epistemic process: hypothesis generation → experimentation → knowledge acquisition
- Agents as autonomous causal learners in a scientific-like epistemic loop

---

## 8. Implications for AMOS_OS: Integration into the Cognitive Organism Layer

### 8.1 World Models as Cognitive Substrate

The 2026 landscape maps directly onto the AMOS cognitive architecture:

| AMOS Layer | World Model Component | Source Systems |
|------------|----------------------|----------------|
| **Perception** | Sensory encoding (pixels → latent) | JEPA encoders, V-JEPA 2 |
| **Internal Model** | Predictive world model | C-JEPA, DreamerV3, TD-MPC2 |
| **Causal Reasoning** | Intervention-aware dynamics | Causal-JEPA, CausalVAE, CWMs |
| **Planning** | Action selection via imagined rollouts | EFE minimization, Riemann-1.0 |
| **Spatial Understanding** | 3D scene representation | Atlas, Qwen-3D, SenseNova-SI |
| **Action Execution** | Motor policy output | World Action Models, Cosmos Policy |

### 8.2 Free Energy Principle as Unifying Objective

Active inference provides the mathematical framework for integrating world models into AMOS:

```
AMOS Cognitive Loop ≡ Active Inference Cycle:

1. Perception:    q(s) ← minimize VFE[observations]
2. Planning:      π* ← minimize EFE[future trajectories]
3. Action:        a ← sample from π* acting on world
4. Learning:      θ  ← gradient descent on F[θ, q]
5. Meta-learning: Update generative model structure
```

This maps to AMOS's existing organ architecture:
- **Nervous System** (C1神经系统): Reactive message passing on factor graph
- **Immune System** (C2免疫系统): Anomaly detection via surprise/prediction error
- **Endocrine System** (C3内分泌系统): Neuromodulation via precision-weighting
- **Musculoskeletal System** (C4运动系统): Action execution conditioned on planned policy

---

## 9. Integration Pathway: World Model Components → AMOS Organ Architecture

### 9.1 Phase 1: Predictive Perception (0–3 months)

**Objective:** Implement JEPA-based predictive encoding within AMOS cognitive layer.

**Components:**
- Adapt EB-JEPA library for AMOS-specific sensory streams
- Implement LeJEPA's SIGReg for collapse-free representation learning
- Build spatial context grounding inspired by Atlas's 3D-positioned input encoding

**Architecture:**
```
Input (text/image/video/3D) → JEPA Encoder → Spatial Context → Predictive Head
                                                              ↓
                                              Next-state latent prediction
```

### 9.2 Phase 2: Causal World Model (3–6 months)

**Objective:** Add intervention-aware dynamics model.

**Components:**
- Causal-JEPA for object-level interaction reasoning
- CausalVAE plugin for structured latent causal graphs
- CAER training for action-effect-aware supervision

**Key design decision:** Use object-centric representations (C-JEPA) over patch-based for 100× token efficiency and native causal interpretability.

### 9.3 Phase 3: Active Inference Planning (6–9 months)

**Objective:** Implement EFE-based planning within world model.

**Components:**
- VFE minimization for perception (reactive message passing on factor graph)
- EFE minimization for policy selection
- Epistemic exploration bonus for curiosity-driven learning
- Precision-weighting for attentional modulation

### 9.4 Phase 4: Cross-Embodiment Action (9–12 months)

**Objective:** Unified action model across AMOS interfaces.

**Components:**
- CLAP-style cross-embodiment action conditioning
- Riemann-1.0-style unified policy-simulator architecture
- Sim-to-real transfer via SimDist framework
- Cosmos-3-style multimodal output (text + image + video + sound + actions)

---

## 10. Open Problems and Research Frontiers

### 10.1 Long-Horizon Consistency
Current world models (including Genie 3) maintain consistency for minutes, not hours. AMOS requires persistent world models operating across sessions. The memory bottleneck remains unsolved.

### 10.2 Action Grounding
Video models can imagine but not act. World Action Models (Riemann-1.0, CLAP) bridge this gap, but deployment on physical hardware remains limited to constrained lab settings.

### 10.3 Intervention Fidelity
The "intervention gap" (Aug 2026 finding) shows that models can predict well but intervene poorly. Task-anchored training degrades intervention fidelity while reward prediction stays accurate—a dangerous dissociation for AMOS planning.

### 10.4 Evaluation Taxonomy
No consensus on how to evaluate world models across the four functional categories. VBench-physics sub-scores improved from ~30% to ~55% (2023–2026) but measure only perceptual plausibility, not causal correctness.

### 10.5 Data Asymmetry
Renderers are awash in internet video; simulators and planners face acute shortages of 3D assets and robot demonstrations. CLAP's cross-embodiment approach (leveraging human videos for robot training) partially addresses this.

### 10.6 The Unified Architecture Problem
> "Reconciling visual beauty, physical precision, and action planning inside a single architecture is the defining open problem in world model research today." — World Labs, Jun 2026

Whether a single model can simultaneously render photorealistic views, produce physically accurate structure, and plan action sequences remains the grand challenge.

### 10.7 Epistemic vs. Predictive Intelligence
The self-evolving cognitive framework (Jun 2026) argues for a paradigm shift from prediction to **epistemic intelligence**—agents that construct, revise, and refine causal world models through interaction. This aligns with AMOS's vision of the Cognitive Organism as a self-evolving system.

---

## 11. References

### Primary Sources

1. World Labs Team. "Atlas: A World Model for Spatial Intelligence." World Labs Blog, Sep 1, 2026.
2. World Labs Team. "A Functional Taxonomy of World Models." World Labs Blog, Jun 3, 2026.
3. Parker-Holder, J. & Fruchter, S. "Genie 3: A New Frontier for World Models." Google DeepMind Blog, Aug 5, 2025.
4. OpenAI. "Video Generation Models as World Simulators." Feb 15, 2024.
5. Google DeepMind. "Veo 3.1." deepmind.google/models/veo, 2025–2026.
6. NVIDIA. "Cosmos World Foundation Models." 2025–2026.

### JEPA and Representation Learning

7. Balestriero, R. & LeCun, Y. "LeJEPA: Provable and Scalable Self-Supervised Learning Without the Heuristics." arXiv:2511.08544, Nov 2025.
8. Terver, B. et al. "EB-JEPA: A Lightweight Library for Energy-Based Joint-Embedding Predictive Architectures." arXiv:2602.03604, Feb 2026.
9. Kuang, Y. et al. "Rectified LpJEPA: Joint-Embedding Predictive Architectures with Sparse and Maximum-Entropy Representations." arXiv:2602.01456, Feb 2026.
10. Huang, H., LeCun, Y. & Balestriero, R. "LLM-JEPA: Large Language Models Meet Joint Embedding Predictive Architectures." arXiv:2509.14252, Sep 2025.
11. Chen, D. et al. "VL-JEPA: Joint Embedding Predictive Architecture for Vision-language." arXiv:2512.10942, Dec 2025.
12. Gögl, M. & Yau, C. "Var-JEPA: A Variational Formulation of the Joint-Embedding Predictive Architecture." arXiv:2603.20111, Mar 2026.
13. Nam, H. et al. "Causal-JEPA: Learning World Models through Object-Level Latent Interventions." arXiv:2602.11389, Feb 2026.

### Spatial Intelligence

14. Cai, Z. et al. "Scaling Spatial Intelligence with Multimodal Foundation Models." CVPR 2026.
15. Xiao, Y. et al. "SpatialTree: How Spatial Intelligence Branches Out in MLLMs." CVPR 2026.
16. Zhang, Y. et al. "SSR: Structured Scene Reasoning." arXiv:2603.00409, Feb 2026.
17. Lin, L. et al. "Qwen-3D: A Generalist 3D Vision-Language Model for Spatial Understanding." ECCV 2026.
18. Li, D. et al. "SpatialEvo: Self-Evolving Spatial Intelligence via Deterministic Geometric Environments." arXiv:2604.14144, Apr 2026.

### Embodied AI and Sim-to-Real

19. Riemann-1.0. "An Embodied World Action Model for Physical AI." arXiv:2608.27033, Aug 2026.
20. "CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators." arXiv:2608.27406, Aug 2026.
21. "AnyWorld: Factorized Egocentric World Models for Cross-Embodiment Generalization." arXiv:2608.29242, Aug 2026.
22. Schmeckpeper, K. "Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors." arXiv:2606.31101, Jun 2026.
23. Levy, J. et al. "SimDist: Simulation Distillation for Efficient Sim-to-Real Transfer." arXiv:2603.15759, Mar 2026.
24. Jiang, Z. et al. "WoVR: Reliable World-Model-Based Reinforcement Learning for VLA Post-Training." arXiv:2602.13977, Feb 2026.

### Causal World Models

25. "The Intervention Gap in Latent World Models." arXiv:2608.29998, Aug 2026.
26. Ding, Z. et al. "CausalVAE as a Plug-in for World Models." arXiv:2604.07712, Apr 2026.
27. "CAER: Causal Action Effect Reweighting for World Model Training." arXiv:2608.30897, Aug 2026.
28. "Causal Process Models: Reframing Dynamic Causal Graph Discovery as RL." 2026.
29. "A Unifying Perspective on Causal World Models." arXiv:2608.13456, Aug 2026.
30. "Self-Evolving Cognitive Framework via Causal World Modeling." arXiv:2606.22449, Jun 2026.

### Free Energy Principle and Active Inference

31. "Active Inference World Models: From Embodied Control to General-Purpose Adaptive Intelligence." Zenodo, Jul 2026.
32. Nuijten, W. et al. "What Type of Inference is Active Inference?" UAI 2026, PMLR 337.
33. de Vries, B. "Active Inference for Physical AI Agents — An Engineering Perspective." arXiv:2603.20927, Mar 2026.
34. Hashash, O. et al. "Active Inference as the Test-Time Scaling Law for Physical AI Agents." arXiv:2606.22813, Jun 2026.
35. Wilson, P. et al. "Active Inference: A Method for Phenotyping Agency in AI Systems?" arXiv:2604.23278, Apr 2026.

### AMI Labs and Industry

36. "Former Meta A.I. Chief's Start-Up Is Valued at $3.5 Billion." New York Times, Mar 10, 2026.
37. "Yann LeCun just raised $1bn to prove the AI industry has got it wrong." The Next Web, Aug 25, 2026.
38. "A four-year-old has seen more of the world than ChatGPT." The Next Web, Aug 25, 2026.
39. "Yann LeCun's Startup Challenges the Logic Behind AI." Observer, Jun 22, 2026.

### Surveys and Guides

40. "Video World Models: Sora, Genie, Cosmos, V-JEPA Explained." world-models.io, 2026.
41. "World Models: The Ultimate Guide (2026 Edition)." Prompt20, May 23, 2026.
42. "World Models Explained: What They Are in 2026." DataLLM Lab, Jul 10, 2026.
43. "World Models Race 2026." Introl Blog, Jan 3, 2026.
