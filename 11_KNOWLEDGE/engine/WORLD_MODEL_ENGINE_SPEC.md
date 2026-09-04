---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: World Model Engine Spec
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

# WORLD_MODEL_ENGINE_SPEC: AMOS World Model Implementation Specification

## 1. Purpose

This engine spec maps the 2026 SOTA world model research findings to AMOS-specific implementation patterns. It provides the computational architecture, data flow, and organ-level integration blueprint for building a world model within the AMOS Cognitive Organism framework.

**Canonical lineage:** Derived from `22_RESEARCH/SOTA_WORLD_MODELS_GENERATIVE_SIMULATION_2026.md` (OBSERVATION class, 2026-09-04).

---

## 2. Architectural Principle: The World Model as Cognitive Backbone

AMOS treats the world model not as an application-level feature but as the **substrate on which cognition operates**. This aligns with LeCun's thesis (AMI Labs, 2026): "The next real AI revolution will come from understanding the world, not just predicting the next word."

### 2.1 Four Functional Components

```
┌──────────────────────────────────────────────────────────┐
│                  AMOS WORLD MODEL ENGINE                  │
│                                                          │
│  ┌─────────┐  ┌───────────┐  ┌─────────┐  ┌─────────┐  │
│  │ RENDER  │  │ SIMULATE  │  │  PLAN   │  │ PREDICT │  │
│  │         │  │           │  │         │  │         │  │
│  │ Observa-│  │ Geometric │  │ Action  │  │ Latent  │  │
│  │ tions   │  │ +Physical │  │ selec-  │  │ next-   │  │
│  │ from    │  │ state     │  │ tion    │  │ state   │  │
│  │ world   │  │ from      │  │ given   │  │ in      │  │
│  │         │  │ world     │  │ goal    │  │ embed-  │  │
│  │         │  │           │  │         │  │ ding    │  │
│  └────┬────┘  └─────┬─────┘  └────┬────┘  └────┬────┘  │
│       │             │             │             │        │
│       └─────────────┴─────────────┴─────────────┘        │
│                          │                               │
│                ┌─────────▼──────────┐                    │
│                │   SPATIAL CONTEXT  │                    │
│                │   (Shared Repre-   │                    │
│                │    sentation)      │                    │
│                └─────────┬──────────┘                    │
│                          │                               │
└──────────────────────────┼──────────────────────────────┘
                           │
              ┌────────────▼────────────┐
              │   JEPA ENCODER LAYER    │
              │   (Joint Embedding      │
              │    Predictive)          │
              └────────────┬────────────┘
                           │
              ┌────────────▼────────────┐
              │   MULTIMODAL INPUTS     │
              │   text|image|video|3D   │
              └─────────────────────────┘
```

---

## 3. Component Specifications

### 3.1 JEPA Encoder Layer (Predictive Perception)

**Source:** LeJEPA (arXiv:2511.08544), EB-JEPA (arXiv:2602.03604), Rectified LpJEPA (arXiv:2602.01456)

**Purpose:** Transform raw multimodal inputs into collapse-free, task-relevant latent representations.

**Implementation pattern:**

```
Class AMOSJEPAEncoder:
    config:
        representation_dim: 768          # latent dimension
        target_distribution: "RGG"       # Rectified Generalized Gaussian
        sparsity_parameter: 0.3          # controllable ℓ0 via RDMReg
        predictor_depth: 6               # transformer layers in predictor
        ema_momentum: 0.996              # for target encoder update
    
    components:
        context_encoder: ViT(native_resolution)
        target_encoder: ViT(native_resolution)  # EMA copy
        predictor: Transformer(hidden_dim=768, depth=6)
        regularizer: RDMReg(target="RGG", p=2.0, sparsity=0.3)
    
    training:
        objective: JEPA_loss + λ · RDMReg
        collapse_prevention: "RDMReg replaces all ad-hoc regularizers"
        max_entropy: true under expected ℓp norm constraints
```

**Key design decisions:**
1. Use Rectified LpJEPA (not LeJEPA alone) for controllable sparsity
2. Target RGG distribution with explicit ℓ0 control
3. Single-GPU training feasible per EB-JEPA specs

### 3.2 Spatial Context Module

**Source:** Atlas (World Labs, Sep 2026), SenseNova-SI (CVPR 2026), Qwen-3D (ECCV 2026)

**Purpose:** Ground all inputs in a unified 3D spatial representation.

**Implementation pattern:**

```
Class AMOSSpatialContext:
    config:
        spatial_resolution: "adaptive"     # multi-scale
        voxel_size: 0.05                   # ~5cm, per Qwen-3D
        positional_encoding: "3D_RoPE"     # (t, x, y, z) rotation embeddings
    
    components:
        image_to_3d: DepthEstimator()      # monocular depth → point cloud
        voxel_pool: VoxelGrid(voxel_size)
        spatial_pe: RotaryPositionalEmbedding(dim=3)
        cross_modal_attention: FullAttention()  # not causal for spatial
    
    data_flow:
        1. Each input image → depth map → 3D point cloud
        2. Points projected to world coordinates via camera pose
        3. Voxel pooling collapses redundant multi-view observations
        4. 3D RoPE enables attention in scene space (not frame space)
        5. Output: persistent scene tokens encoding full 3D structure
    
    output:
        scene_tokens: Tensor[B, N_voxels, D]   # persistent across time
        camera_poses: Tensor[B, N_views, 4, 4]
        depth_maps: Tensor[B, N_views, H, W]
```

### 3.3 Causal Dynamics Model

**Source:** Causal-JEPA (arXiv:2602.11389), CausalVAE plugin (arXiv:2604.07712), CAER (arXiv:2608.30897)

**Purpose:** Predict next state while maintaining intervention fidelity and causal structure.

**Implementation pattern:**

```
Class AMOSCausalDynamics:
    config:
        representation_type: "object_centric"  # C-JEPA style
        causal_structure: "learned_DAG"
        intervention_fidelity: true              # audited, not assumed
    
    components:
        object_encoder: ObjectCentricEncoder()  # from pretrained JEPA
        causal_branch: CausalVAEPlugin(
            dag_constraint: "differentiable_DAG",
            staged_training: true
        )
        action_conditioned_transition: Transformer(
            input: [object_tokens, action_embedding],
            output: next_object_tokens
        )
        action_reweighter: CAER()  # redistribute loss to causally affected tokens
    
    training:
        stage_1: "predictive dynamics only (freeze causal branch)"
        stage_2: "progressive activation of structural regularization"
        stage_3: "alignment-anchored weak supervision"
        
        intervention_training:
            method: "object_level_masking"  # C-JEPA style
            mask_ratio: 0.3
            rationale: "object masking induces latent interventions"
    
    audit:
        method: "capture-gated matched-intervention audit"
        frequency: "per_checkpoint"
        metric: "operator_error on task observables"
        alert_threshold: "operator_error > 0.5 × oracle_error"
```

**Critical requirement from 2026 research:** Intervention fidelity must be **directly audited** on the model's native interface, not inferred from reward fit. The "intervention gap" finding shows these are decorrelated.

### 3.4 Active Inference Planner

**Source:** Active Inference World Models (Zenodo, Jul 2026), Nuijten et al. (UAI 2026), Hashash et al. (arXiv:2606.22813), de Vries (arXiv:2603.20927)

**Purpose:** Select actions that minimize expected free energy, unifying goal-seeking and information-gathering.

**Implementation pattern:**

```
Class AMOSActiveInferencePlanner:
    config:
        planning_horizon: 20              # timesteps
        policy_space: "discrete"          # for initial implementation
        epistemic_weight: 1.0             # balance exploration/exploitation
        precision_prior: 1.0              # prior confidence in observations
    
    components:
        generative_model:
            transition_model: CausalDynamics()  # from 3.3
            observation_model: Decoder()        # latent → predicted observation
            preference_distribution: C(s)       # log-prior over preferred states
        
        inference_engine:
            vfe_minimizer: VariationalFreeEnergy()
            efe_minimizer: ExpectedFreeEnergy()
            message_passing: ReactiveMessagePassing(
                factor_graph: True,
                event_driven: True,
                local_computations: True
            )
        
        policy_selector:
            method: "Boltzmann_over_EFE"
            temperature: 1.0
            posterior_policy: "softmax(-EFE[π] / τ)"
    
    planning_loop:
        1. PERCEIVE: minimize VFE → q*(s_current)
        2. SIMULATE: for each candidate policy π:
              imagine trajectory using causal dynamics model
              compute EFE[π] = pragmatic_value + information_gain
        3. SELECT: π* ← argmax p(π|EFE)
        4. ACT: execute first action of π*
        5. UPDATE: observe outcome, update beliefs
        6. META: if prediction_error > threshold ε → engage deliberative reasoning
    
    test_time_scaling:
        mechanism: "reasoning reduces prediction errors at test time"
        biological_analogy: "basal_ganglia + prefrontal_cortex engagement"
        efficiency_gain: ">36% vs model-free Q-learning (per Hashash et al.)"
```

### 3.5 Cross-Embodiment Action Interface

**Source:** CLAP (arXiv:2608.27406), Riemann-1.0 (arXiv:2608.27033), AnyWorld (arXiv:2608.29242)

**Purpose:** Map planned actions to concrete motor commands across different interfaces.

```
Class AMOSCrossEmbodimentAction:
    config:
        action_representations:
            - end_effector_pose
            - language_instruction
            - latent_action         # CLAP-style
    
    components:
        action_encoder: ActionEncoder(action_rep="mixed")
        embodiment_adapter: EmbodimentAdapter()  # maps latent → specific output
        video_action_predictor: VideoActionPredictor()  # predicts visual outcome
    
    supported_embodiments:
        - "screen_output"     # GUI/CLI interactions
        - "text_generation"   # LLM-style outputs
        - "robot_actuation"   # future: robot control
        - "api_execution"     # tool use
    
    training:
        progressive_pretraining:
            stage_1: "human egocentric videos (action structure)"
            stage_2: "mixed-embodiment fine-tuning"
            stage_3: "target embodiment specialization"
```

---

## 4. Data Flow: The AMOS Cognitive Loop

```
┌─────────────────────────────────────────────────────────────┐
│                    THE AMOS COGNITIVE LOOP                   │
│                     (Active Inference Cycle)                 │
│                                                             │
│  ① SENSE        ② ENCODE       ③ PREDICT      ④ PLAN      │
│  ┌─────────┐   ┌──────────┐   ┌──────────┐   ┌─────────┐  │
│  │ Raw     │──▶│ JEPA     │──▶│ Causal   │──▶│ EFE     │  │
│  │ multi-  │   │ Encoder  │   │ Dynamics │   │ Planner │  │
│  │ modal   │   │ + Spatial│   │ Model    │   │         │  │
│  │ input   │   │ Context  │   │          │   │         │  │
│  └─────────┘   └──────────┘   └──────────┘   └────┬────┘  │
│                                                      │      │
│  ⑧ LEARN        ⑦ EVALUATE     ⑥ UPDATE      ⑤ ACT │      │
│  ┌─────────┐   ┌──────────┐   ┌──────────┐   ┌─────▼────┐│
│  │ Update  │◀──│ Compare  │◀──│ Belief   │◀──│ Execute  ││
│  │ weights │   │ predicted│   │ update   │   │ action   ││
│  │ (+ meta)│   │ vs       │   │ via VFE  │   │ + observe││
│  │         │   │ observed │   │ minimiz. │   │ outcome  ││
│  └─────────┘   └──────────┘   └──────────┘   └──────────┘│
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Mapping to AMOS organ architecture:**

| AMOS Organ | Cognitive Function | World Model Component |
|------------|-------------------|----------------------|
| **Nervous System (C1)** | Signal routing, reactive message passing | Factor graph + RMP |
| **Immune System (C2)** | Anomaly detection, prediction error monitoring | VFE / surprise thresholding |
| **Endocrine System (C3)** | Precision weighting, neuromodulation | Attention gain control |
| **Musculoskeletal System (C4)** | Action execution | Cross-embodiment action interface |
| **Digestive System (C5)** | Data ingestion, preprocessing | Multimodal tokenizer + encoder |
| **Respiratory System (C6)** | Memory consolidation, forgetting | Episodic buffer + replay |
| **Integumentary System (C7)** | Boundary, interface with environment | I/O interface + perception |

---

## 5. Training Protocol

### 5.1 Progressive Training Schedule

```
Phase 1 (Months 1-3): Self-Supervised Foundation
    ├── Train JEPA encoder on multimodal corpus
    ├── Apply LeJEPA SIGReg / RDMReg for collapse prevention
    ├── Build spatial context module (3D RoPE, voxel pooling)
    └── Eval: probe representations on downstream tasks

Phase 2 (Months 4-6): Causal Dynamics
    ├── Object-centric extraction from JEPA features
    ├── Causal-JEPA training with object-level masking
    ├── CausalVAE plugin for DAG structure
    ├── CAER for action-effect reweighting
    └── Eval: intervention fidelity audit (must pass threshold)

Phase 3 (Months 7-9): Active Inference Integration
    ├── Connect dynamics model to EFE planner
    ├── Implement reactive message passing on factor graph
    ├── Train preference distribution for target domains
    ├── Test-time scaling integration
    └── Eval: planning success on robotic/control benchmarks

Phase 4 (Months 10-12): Cross-Embodiment Deployment
    ├── CLAP-style action conditioning across output modalities
    ├── Riemann-style progressive pretraining from diverse data
    ├── SimDist-style sim-to-real transfer (if applicable)
    └── Eval: end-to-end task completion in target environments
```

### 5.2 Key Training Hyperparameters

```yaml
# JEPA Encoder
jepa:
  learning_rate: 1e-4
  batch_size: 256
  patch_size: 16
  representation_dim: 768
  predictor_depth: 6
  ema_momentum: 0.996
  regularizer: "RDMReg"
  target_distribution: "RGG"
  sparsity: 0.3

# Spatial Context
spatial:
  voxel_size: 0.05
  max_scene_tokens: 2048
  positional_encoding: "3D_RoPE"
  
# Causal Dynamics
dynamics:
  object_slots: 32
  causal_masking_ratio: 0.3
  dag_constraint_weight: 0.1
  staged_warmup_epochs: [8, 40, 48]  # per CausalVAE recipe

# Active Inference
planning:
  horizon: 20
  efe_temperature: 1.0
  epistemic_weight: 1.0
  vfe_tolerance: 0.1
  reasoning_threshold_epsilon: 0.5
```

---

## 6. Evaluation Framework

### 6.1 Component-Level Evaluation

| Component | Metric | Target | Source |
|-----------|--------|--------|--------|
| JEPA Encoder | Linear probe accuracy | >91% CIFAR-10 | EB-JEPA benchmark |
| Spatial Context | VSI-Bench score | >74 | SenseNova-SI |
| Causal Dynamics | CF-H@1 (counterfactual) | >30 Physics | CausalVAE benchmark |
| Intervention fidelity | Operator error ratio | <0.5 × oracle | Intervention Gap paper |
| Planning | Two Rooms success | >97% | EB-JEPA benchmark |
| Active Inference | Inference efficiency | >36% gain vs Q-learning | Hashash et al. |

### 6.2 System-Level Evaluation

| Test | Metric | Target |
|------|--------|--------|
| Cognitive loop end-to-end | Task completion rate | >80% on target tasks |
| Long-horizon consistency | State drift after N steps | <5% at N=50 |
| Generalization | OOD performance retention | >70% of in-distribution |
| Real-time capability | Loop frequency | >10 Hz (100ms per cycle) |
| Memory efficiency | VRAM usage | <16GB for inference |

---

## 7. Risk Register

| Risk | Severity | Mitigation | Status |
|------|----------|------------|--------|
| Representation collapse | HIGH | RDMReg with RGG target | MITIGATED (LeJEPA) |
| Intervention gap | HIGH | Direct audit at every checkpoint | PROCEDURE DEFINED |
| Causal structure hallucination | MEDIUM | DAG constraint + alignment-anchored supervision | IN DESIGN |
| Long-horizon error accumulation | HIGH | KIR + PACE co-evolution (per WoVR) | TO IMPLEMENT |
| Sim-to-real gap | MEDIUM | SimDist framework + domain randomization | TO IMPLEMENT |
| Compute requirements | MEDIUM | EB-JEPA single-GPU feasibility confirmed | VALIDATED |
| Evaluation gap | HIGH | Multi-level eval (component + system) | FRAMEWORK DEFINED |

---

## 8. Dependency Map

```
External Dependencies:
├── EB-JEPA (Meta FAIR) → JEPA encoder implementation
├── LeJEPA → SIGReg regularizer
├── CausalVAE → Structural causal disentanglement
├── RMP (Reactive Message Passing) framework → Active inference engine
├── NVIDIA Cosmos → Reference for physical-AI world models
├── DreamerV3 / TD-MPC2 → Latent-space planning baselines
└── WorldArena benchmark → Evaluation protocol

Internal AMOS Dependencies:
├── C1_NERVOUS_SYSTEM → Factor graph routing
├── C2_IMMUNE_SYSTEM → Prediction error monitoring
├── C3_ENDOCRINE_SYSTEM → Precision weighting
├── C4_MUSCULOSKELETAL → Action execution
├── C5_DIGESTIVE → Data ingestion pipeline
├── C7_INTEGUMENTARY → I/O interface
└── AMOS_CONSCIOUSNESS_ENGINE → Meta-cognitive oversight
```

---

## 9. Open Design Questions

1. **Object slot count:** How many object-centric slots should the causal model maintain? Riemann-1.0 uses scene-level tokens; C-JEPA uses entity-level. AMOS needs a dynamic slot allocation mechanism.

2. **Preference distribution source:** EFE requires p(o|C)—preferred observations. Where do AMOS's preferences come from? Options: (a) user-specified goals, (b) learned from demonstration, (c) homeostatic setpoints (biological analogy).

3. **Causal graph persistence:** Should the learned DAG structure persist across sessions or be re-learned? CausalVAE suggests persistent structure with progressive refinement.

4. **Multi-scale temporal modeling:** Atlas handles 1-minute video; Genie 3 handles minutes of interaction; AMOS needs hours-to-days persistence. The memory architecture remains an open problem.

5. **Intervention fidelity vs. prediction accuracy trade-off:** The intervention gap paper shows these can be decorrelated. AMOS should prioritize intervention fidelity for planning reliability.

---

## 10. Version History

| Version | Date | Change | Class |
|---------|------|--------|-------|
| v0.1 | 2026-09-04 | Initial spec derived from SOTA synthesis | DERIVED |

---

## 11. References

- Balestriero & LeCun. "LeJEPA." arXiv:2511.08544, Nov 2025.
- Terver et al. "EB-JEPA." arXiv:2602.03604, Feb 2026.
- Kuang et al. "Rectified LpJEPA." arXiv:2602.01456, Feb 2026.
- Nam et al. "Causal-JEPA." arXiv:2602.11389, Feb 2026.
- World Labs. "Atlas: A World Model for Spatial Intelligence." Sep 2026.
- World Labs. "A Functional Taxonomy of World Models." Jun 2026.
- Hashash et al. "Active Inference as Test-Time Scaling Law." arXiv:2606.22813, Jun 2026.
- de Vries. "Active Inference for Physical AI." arXiv:2603.20927, Mar 2026.
- Nuijten et al. "What Type of Inference is Active Inference?" UAI 2026.
- "The Intervention Gap in Latent World Models." arXiv:2608.29998, Aug 2026.
- Ding et al. "CausalVAE as a Plugin for World Models." arXiv:2604.07712, Apr 2026.
- Riemann-1.0. arXiv:2608.27033, Aug 2026.
- CLAP. arXiv:2608.27406, Aug 2026.
- Levy et al. "SimDist." arXiv:2603.15759, Mar 2026.
- Jiang et al. "WoVR." arXiv:2602.13977, Feb 2026.
