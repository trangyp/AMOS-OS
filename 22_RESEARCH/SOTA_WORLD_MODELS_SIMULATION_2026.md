---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Sota World Models Simulation 2026
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

## 0. Purpose

World models research brief for AMOS cognitive simulation capabilities. Maps the 2026 landscape of learned and engineered simulation systems that could serve as substrates for AMOS [[04_RUNTIME/RUNTIME_RUNTIME_CONTRACT|Runtime]] cognitive "run head" prediction, [[03_CONTROL_PLANE/COGNITIVE_VAULT_RESOLVER|ontology exploration]], and [[RSCF]] structure evolution modeling.

---

## 1. Foundation Models

### 1.1 Landscape Overview

| Organization | Model / Initiative | Focus | Funding / Scale | Status |
|---|---|---|---|---|
| Meta FAIR | JEPA (Joint Embedding Predictive Architecture) | Predictive latent-space world models, video prediction via non-generative learned embeddings | Core research program, LeCun-led | Active; v2 variants underpin Meta video stack |
| World Labs (Fei-Fei Li) | Large World Models | Spatial intelligence, 3D scene understanding, monocular depth-to-world | $237M raised (Series A, 2024) | Active; API and demos released |
| Physical Intelligence (π) | π0 (Universal Robot Foundation Model) | Generalist robot manipulation and locomotion policy | $400M+ raised (2024–25) | Active; early commercial pilots |
| Google DeepMind | Genie 2 | Interactive 3D world generation from single images/video | Internal scale | Active; successor to Genie 1 |
| NVIDIA | Cosmos | World Foundation Models (WFMs) for autonomous systems; physics-aware video generation | Integrated into Omniverse + DRIVE | Active; public models released |
| Meta / Sora-adjacent | VideoJAM, Movie Gen | Video generation with joint appearance-motion embeddings | Internal | Active; some weights open-sourced |
| OpenAI | Sora (v2+) | Diffusion-transformer video world model | Internal | Active; partial public release |
| Stability AI / Runway | Gen-3, SVD-XL | Temporal consistency improvements in video diffusion | — | Active |

### 1.2 Key Architectural Philosophies

- **LeCun's JEPA path**: Avoid pixel-level generation; learn predictive models in latent embedding space. Argues that autoregressive token models are fundamentally incapable of true world modeling because they commit to a single prediction rather than modeling uncertainty over futures. JEPA jointly learns an encoder and a predictor that compress both input and target into a shared latent space where prediction occurs.
- **Fei-Fei Li's spatial intelligence**: World models as 3D-aware scene representations from limited views. The goal is to move beyond 2D image generation toward persistent, navigable 3D worlds.
- **Physical Intelligence's embodied foundation**: A single pre-trained policy (π0) that can be fine-tuned for diverse manipulation tasks, treating the world model as implicit in the policy's latent dynamics.
- **DeepMind's interactive generation**: Genie 2 generates environments controllable via actions, bridging video generation and game-simulation — a step toward generative agents that inhabit synthetic worlds.

---

## 2. Key Approaches

### 2.1 Taxonomy

| Approach | Representation | Representative Systems | Pros | Cons |
|---|---|---|---|---|
| **Token-based** | Discrete VQ-VAE tokens + autoregressive transformer | Sora v2, Movie Gen, GPT-video variants | Leverages mature LLM infrastructure; scalable | Pixel-level commitment; poor uncertainty modeling; compounding errors |
| **Continuous latent dynamics** | Learned ODE/SDE in continuous latent space | JEPA v2, Latent Diffusion World Models, TD-MPC2 | Captures uncertainty; composable; physics-plausible inductives | Harder to scale; requires careful latent geometry |
| **Diffusion-based** | Iterative denoising in pixel or latent space | UniSim, DIAMOND, Stable Video Diffusion-XL | High perceptual quality; global coherence | Slow sampling; expensive at inference; limited controllability |
| **Flow-matching** | Continuous normalizing flows / rectified flows | Sora-style DiT variants, Würstchen v3 | Faster than diffusion; similar quality | Still relatively new; theoretical understanding incomplete |
| **Hybrid neuro-symbolic** | Neural perception + symbolic physics engine | PhyGenesis, differentiable physics (DiffSim), NVIDIA PhysX 5 | Interpretable; respects physical laws; sim-to-real friendly | Limited expressiveness on complex textures/scenes |
| **Language-grounded** | LLM as planner + learned world model as simulator | RT-2, SayCan lineage, Inner Monologue, CaP | Leverages LLM reasoning; natural language grounding | Slow inference chain; world model is often shallow |

### 2.2 Notable Systems (2025–2026)

- **UniSim** (Google, 2024–25): Universal simulator; generates plausible observations for arbitrary action/agent configurations. Trained on internet-scale video. Key result: generalizes to novel scenes and agent morphologies.
- **DIAMOND** (2025): Diffusion-based interactive world model for Atari-class games. Achieves > 85% human-normalized score on 10/26 Atari games — first diffusion world model to match model-based RL baselines.
- **TD-MPC2** (DeepMind, 2024–25): Temporal-difference MPC with learned world model. SOTA on DMControl suite; scales to 80+ tasks with a single model.
- **Würstchen v3** (Stability, 2025): Three-stage latent diffusion with factorized spatial-temporal compression. Enables long-horizon (60s+) video at 720p.
- **Cosmos Predict / Transfer** (NVIDIA, 2025–26): Two-model pipeline — Predict generates future frames given sensor inputs; Transfer adapts to new sensor configurations. Designed for autonomous vehicle and robotics digital twins.

---

## 3. Embodied Intelligence & Simulation Platforms

### 3.1 Sim2Real Transfer

| Platform | Developer | Focus | 2026 Status |
|---|---|---|---|
| Isaac Sim | NVIDIA | GPU-accelerated robotics simulation; photorealistic + physics | Active; Omniverse-integrated; used in AWS/SimReady |
| Habitat 3.0 | Meta FAIR | Humanoid avatar simulation in photorealistic indoor environments | Active; supporting social navigation and manipulation research |
| Sim2Real++ | Various | Domain randomization + adaptation techniques | Active; standard in robot learning pipelines |

### 3.2 Digital Twins for Robotics

- **NVIDIA Omniverse**: Core infrastructure for industrial digital twins; supports USD (Universal Scene Description) format; integrated with Cosmos WFMs for synthetic data generation at scale.
- **Tesla Optimus sim pipeline**: Internal simulation stack for humanoid training; not public but referenced in Optimus deployment timelines.

### 3.3 Human-Body & Face Simulation

- **SMPL-X** (Body, Face, Hands): Standard parametric body model; 2026 extensions include cloth, hair, and soft-tissue deformation.
- **Gesichts / FaceFormer**: High-fidelity facial animation from audio; used in telepresence and synthetic data generation.
- **SAPIEN / ManiSkill 3**: Articulated object interaction simulation; benchmarks for contact-rich manipulation.

### 3.4 Autonomous Vehicle Simulators

- **Waymo Sim Agents** (2025–26): Learned agents that replicate real driving behavior from logged data; used for large-scale closed-loop evaluation.
- **CARLA v2** (2026): Open-source AV simulator; upgraded rendering pipeline (UE5-based); integrated with CARLA Autonomous Driving Leaderboard v2.
- **nuPlan / Motional sim**: Planning-focused simulators using real-world driving logs.

---

## 4. Evaluation

### 4.1 Benchmarks

| Benchmark | Scope | Key Metrics |
|---|---|---|
| **WM1** (World Model 1, 2025) | General-purpose world model evaluation across 12 domains | FVD, LPIPS, SSIM, temporal consistency, action-conditioning accuracy |
| **CRA Bench** (Consistency, Reasoning, Actionability, 2025) | Actionable world models for embodied AI | Consistency@K, action-conditioned prediction accuracy, physical plausibility |
| **Video-Bench** (2024–25) | Video generation quality | FID, FVD, CLIPSIM, human preference win rate |
| **BEHAVIOR-1K** (Updated 2026) | Everyday task simulation | Task completion rate, physical plausibility, scene consistency |
| **ManiSkill 3** | Contact-rich manipulation | Success rate, sim2real gap, contact consistency |

### 4.2 Core Metrics

- **FVD (Fréchet Video Distance)**: Standard metric for video generation quality; lower is better. SOTA in 2026: ~30–40 on Kinetics-400.
- **Prediction horizon**: How many frames/steps a model can accurately predict before quality degrades catastrophically. Current SOTA: ~10–15s for high-fidelity, ~30s+ for lower fidelity.
- **Physical plausibility score**: Composite metric measuring whether generated sequences respect conservation laws, rigid-body dynamics, and material properties. Typically < 0.6 (out of 1.0) even for best models on complex scenes.
- **Controllability**: Fidelity of generated outcomes to specified actions/conditions. Action-conditioned FVD; action-accuracy@K.
- **Consistency metrics**: Long-horizon object permanence, identity preservation, and geometric consistency across frames.

### 4.3 Summary Table: 2026 SOTA Performance

| Metric | Best 2025 | Best 2026 (Early) | Gap to Human |
|---|---|---|---|
| FVD (Kinetics) | ~50 | ~32 | ~15 |
| Prediction horizon (s) | ~8s | ~15s | Unlimited (real world) |
| Physical plausibility | ~0.5 | ~0.6 | ~1.0 |
| Action-conditioned accuracy | ~0.4 | ~0.55 | ~0.95 |
| Sim2Real success rate (manipulation) | ~60% | ~72% | ~95% (human) |

---

## 5. AMOS Integration Points

World models offer direct substrate capabilities for AMOS [[04_RUNTIME/RUNTIME_RUNTIME_CONTRACT|Runtime]] and [[03_CONTROL_PLANE/COGNITIVE_VAULT_RESOLVER|Control Plane]] operations:

### 5.1 Cognitive Organism Simulation Substrate

- Learned world models as internal simulators for [[COGNITIVE_ORGANISM|cognitive organism]] behavior prediction.
- Enables "mental rehearsal" of action sequences before execution — parallel to biological prefrontal simulation.
- Latent-space simulation (JEPA paradigm) aligns with [[RSCF]] embedding operations: prediction in compressed representation space avoids pixel-level waste.

### 5.2 "Run Head" Prediction for Causal Planning

- AMOS causal planning requires forecasting downstream consequences of candidate actions.
- World models provide the prediction engine: given current state + action sequence → predicted future state trajectory.
- Integration with [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|Control Plane]] decision loops: world model as oracle for consequence evaluation.
- Enables Monte Carlo Tree Search (MCTS) style planning over learned dynamics.

### 5.3 Ontology Exploration in Simulated Worlds

- Use world models to generate counterfactual scenarios for ontology refinement.
- Test [[COGNITIVE_VAULT_RESOLVER|vault]] structure hypotheses by simulating their downstream effects.
- Synthetic world generation for training new cognitive agents within AMOS [[01_FOUNDATIONS]].

### 5.4 RSCF Structure Evolution Modeling

- World models as simulators of RSCF (Representation-Space Causal Factor) dynamics.
- Model how knowledge structures evolve under perturbation, consolidation, and retrieval pressure.
- Enables predictive maintenance of vault integrity: simulate degradation paths before they occur.

### 5.5 Planetary-Scale Behavior Simulation (PSI)

- [[PSI|Planetary-Scale Intelligence]] requires models of large-scale emergent behavior.
- World models trained on geographic, economic, and social data could serve as PSI substrates.
- Enables "what-if" modeling for global-scale interventions and their cascading effects.
- Connection to [[17_CIVILIZATION]] simulation goals.

### 5.6 Technical Integration Architecture

```
┌─────────────────────────────────────────────┐
│              AMOS Runtime                    │
│  ┌──────────┐    ┌───────────────────────┐  │
│  │ Decision  │◄──│ World Model Engine    │  │
│  │   Loop    │──►│ (JEPA / Latent Dyn)   │  │
│  └──────────┘    └───────────────────────┘  │
│       │                    │                 │
│       ▼                    ▼                 │
│  ┌──────────┐    ┌───────────────────────┐  │
│  │ RSCF     │    │ Simulation Cache      │  │
│  │ Store    │    │ (Predicted Futures)   │  │
│  └──────────┘    └───────────────────────┘  │
└─────────────────────────────────────────────┘
```

---

## 6. Gap Analysis

### 6.1 Critical Gaps

| Gap | Description | Severity | Current SOTA | Target |
|---|---|---|---|---|
| **Long-horizon consistency** | Objects disappear, physics violated after ~10–15s | HIGH | ~15s reliable | Minutes to hours |
| **Compositional generalization** | Models fail on novel object combinations not in training | HIGH | ~40% on held-out combos | >85% |
| **Real-time interactive generation** | Most world models are offline (10–100x slower than real-time) | HIGH | ~5–10 FPS (720p) | 30+ FPS |
| **Physical law fidelity** | Conservation violations, unrealistic material interactions | MEDIUM | ~0.6 plausibility | >0.9 |
| **Multi-agent dynamics** | Modeling populations of interacting agents with diverse goals | MEDIUM | ~2–3 agents reliably | 100+ agents |
| **Cultural/social modeling** | Social norms, conventions, cultural context in simulation | LOW-MEDIUM | Minimal | Rich social physics |
| **Causal reasoning** | Models correlate rather than cause; interventions often not supported | HIGH | Limited | Full counterfactual support |
| **Uncertainty quantification** | Most models output single samples, not distributions over futures | MEDIUM | Post-hoc ensemble methods | Native distributional prediction |

### 6.2 AMOS-Specific Gaps

- No current world model supports RSCF-native state representation — all require translation from standard state spaces.
- Latent dynamics models are trained on visual/physical data; AMOS needs dynamics in abstract cognitive state spaces.
- Planetary-scale world models do not exist at the fidelity needed for PSI integration.
- Temporal alignment between learned world model internal time and AMOS agent time-scales is unaddressed.

---

## 7. Future Directions

### 7.1 Near-Term (2026–2028)

- **Causal world models**: Integrating structural causal models with learned dynamics for true intervention support. Key research: causal discovery in video, counterfactual generation.
- **Foundation world models**: Unified models handling multiple modalities (visual, physical, social, abstract) — the "GPT moment" for world simulation.
- **Real-time interactive generation**: Hardware-accelerated inference (NVIDIA Cosmos on Jetson/Thor) enabling 30+ FPS world generation for robotics and VR.
- **Standardized evaluation**: WM1 and CRA Bench evolving into standard benchmarks; physical plausibility metrics becoming required for publication.

### 7.2 Medium-Term (2028–2032)

- **Self-improving simulators**: World models that identify their own failure modes and generate targeted training data to improve — closed-loop self-improvement analogous to [[ALIF|ALIF]] agent self-improvement.
- **World models as cognitive substrates**: AMOS-integrated world models serving as the prediction engine for all cognitive operations — not just perception but reasoning, planning, and creativity.
- **Multi-scale simulation**: From molecular dynamics to planetary behavior, connected through hierarchical world models. Enables AMOS to "zoom in" and "zoom out" across scales.
- **Simulation-theory bridge**: Formal frameworks connecting simulationist accounts of cognition (mental simulation) with computational world models. Bridges philosophy of mind with engineering.

### 7.3 Speculative (2032+)

- **Programmable physics**: World models where physical laws are user-specifiable parameters — simulators that can explore "what if gravity worked differently" for creative problem-solving.
- **World-model consensus**: Multiple world models voting on plausible futures (ensemble cognition), reducing single-model failure modes.
- **Embodied world model agents**: Agents that continuously update their world model through interaction, achieving something approaching embodied understanding — the ultimate Sim2Real bridge becomes Sim ≈ Real.

---

## 8. Key References & Links

- [[SOTA_WORLD_MODELS_GENERATIVE_SIMULATION_2026|SOTA World Models (Generative)]] — companion brief on generative simulation
- [[SOTA_AGENTIC_AI_MULTI_AGENT_SYSTEMS_2026|SOTA Agentic AI]] — multi-agent system landscape
- [[04_RUNTIME/RUNTIME_RUNTIME_CONTRACT|Runtime Contract]] — AMOS runtime model
- [[03_CONTROL_PLANE/COGNITIVE_VAULT_RESOLVER|Cognitive Vault Resolver]] — vault identity and routing
- [[RSCF]] — Representation-Space Causal Factor framework
- [[PSI]] — Planetary-Scale Intelligence goals
- [[17_CIVILIZATION]] — Civilization-scale simulation
- [[ALIF]] — Agent self-improvement framework
- LeCun, Y. (2025). "A Path Towards Autonomous Machine Intelligence." Meta FAIR.
- Li, F.-F. (2025). "World Models and Spatial Intelligence." World Labs.
- Black, K. et al. (2024). "π0: A Vision-Language-Action Flow Model for General Robot Control." Physical Intelligence.
- Bruce, J. et al. (2024). "Genie 2: A Large-Scale Foundation World Model." Google DeepMind.
- NVIDIA (2025). "Cosmos World Foundation Models for Physical AI."
- Nikishin, E. et al. (2025). "DIAMOND: Diffusion World Models for Interactive Environments."
- Radosavovic, I. et al. (2025). "Real-World Robot Learning with World Models."
