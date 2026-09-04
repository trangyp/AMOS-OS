---
title: "SOTA Embodied AI & Robot Foundation Models 2026"
type: specialist_knowledge
source: 11_KNOWLEDGE
domain: C10_TECH_ENGINEERING
primary_h_owner: H4_Physical_Interaction
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_RESEARCH_SYNTHESIS
conclusion_class: MIXED
research_epoch: 2026-09-04
freshness_policy: REVALIDATE_FOR_CURRENT_SOTA
epistemic_class: SOURCE_CLAIM
rscf:
  state: SOURCE_CLAIM
  claim_class: EMPIRICAL_SURVEY
  provenance:
    - 22_RESEARCH/01_PAPERS/SOTA_EMBODIED_ROBOT_FOUNDATION_MODELS_2026.md
    - arXiv:2608.15875 (GigaBrain-0.7)
    - arXiv:2607.11643 (Xiaomi-Robotics-U0)
    - arXiv:2606.11324 (Embodied-R1.5)
    - arXiv:2608.16885 (τ₀-VLA)
    - Tencent Hy-Embodied-VLM-1.0 (Jul 2026)
  scope: embodied_ai_robot_foundation_models_state_of_the_art_2026
tags:
  - amos-os
  - sota
  - embodied-ai
  - robotics
  - vla
  - foundation-models
  - world-models
  - 2026
---

# SOTA Embodied AI & Robot Foundation Models 2026

> **Epistemic boundary**
>
> This file is a freshness-bounded research synthesis. It separates peer-reviewed empirical
> findings, arXiv/source claims, engineering models, and forward research hypotheses. It does not
> claim that AMOS itself controls any physical robot or embodied system.

## 0. Why this subsystem exists

The C10 master owns `Tech & Engineering`, but embodied AI crosses several distinct mechanisms that
should not be collapsed into generic "AI models":

```text
perception (vision + language)
-> world understanding (VLM backbone)
-> task planning (high-level policy)
-> action prediction (continuous action expert)
-> physical execution (robot actuator)
-> observation feedback (closed loop)
-> self-correction (repair cycle)
```

The embodied AI subsystem is an M-level specialist extension under **H4 Physical Interaction**.
Perception depends on C04 (neuro); planning depends on C01 (logic); safety depends on C09 and
Control Plane; physical execution depends on C10.

## 1. SOTA Architecture Families (2026)

### 1.1 Vision-Language-Action (VLA) Foundation Models

| Model | Source | Scale | Key Result | AMOS Binding |
|:---|:---|:---|:---|:---|
| GigaBrain-0.7 | arXiv:2608.15875 | 37K+ hrs data | Three-system architecture (understanding + prediction + action); one-stage alignment training; outperforms π₀.₅ in zero-shot | `25_COGNITIVE_MATRIX/O07-O08-O14` |
| Xiaomi-Robotics-U0 | arXiv:2607.11643 | 38B params | World foundation model; unified image/video/embodied generation; #1 on World Arena; improves π₀.₅ OOD 36.9%→63.2% | `07_SKILLS/amos-k-world-model` |
| Embodied-R1.5 | arXiv:2606.11324 | 8B params | PGC closed-loop (Planner-Grounder-Corrector); SOTA on 16/24 benchmarks; +17% over Gemini-Robotics-ER-1.5 | `07_SKILLS/amos-audit-repair-master` |
| τ₀-VLA | arXiv:2608.16885 | 40K hrs data | World-model-guided test-time computation; beam search over predicted futures; long-horizon task improvement | `07_SKILLS/amos-test-time-compute-scaling` |
| Hy-Embodied-VLM-1.0 | Tencent, Jul 2026 | ~3B active / ~30B total | MoE VLM; latency-sensitive deployment; strong physical-world understanding | `07_SKILLS/amos-budget-aware-optimizer-selection` |

### 1.2 World Models for Embodied AI

The SOTA establishes that **world models are essential** for embodied AI:

- **Training data generation**: Embodied scene generation (Xiaomi-U0)
- **Action evaluation**: Predict terminal observations for candidate actions (τ₀-VLA)
- **Test-time search**: Beam search over predicted futures (τ₀-VLA)
- **OOD generalization**: World model pre-training improves out-of-distribution success

**AMOS alignment**: `K_WORLD_MODEL` at the embodied level — same model, different resolution (H/M/L).

### 1.3 Closed-Loop Self-Correction

Two independent SOTA papers establish that **closed-loop self-correction** is essential for
long-horizon tasks:

- **Embodied-R1.5 PGC loop**: Planner → Grounder → Corrector → re-plan if needed
- **τ₀-VLA beam search**: Propose → Predict → Evaluate → select best candidate

**AMOS alignment**: Both map to AMOS `amos-audit-repair-master` — real-time correction during
execution, not just post-hoc analysis.

## 2. Key Technical Details

### 2.1 GigaBrain-0.7 three-system architecture

```text
System 1: Understanding (VLM backbone)
    ↓ shared representations
System 2: Prediction (latent world model)
    ↓ predicted futures
System 3: Action (continuous action expert)
    ↓ motor commands
```

One-stage alignment training jointly optimizes all three systems, eliminating multi-stage
optimization fragmentation.

**AMOS mapping**: System 1 → O07 Inference; System 2 → O08 Prediction; System 3 → O14 Action.

### 2.2 τ₀-VLA test-time computation

```text
High-level subtask generator
    ↓ candidate subtasks
World model → predict terminal observations
    ↓ predicted futures
Value model → score candidates
    ↓ ranked candidates
Beam search → expand best
    ↓ selected action
```

Additional test-time computation substantially improves next-subtask prediction accuracy and
closed-loop success on long-horizon tasks.

**AMOS mapping**: Propose-Predict-Evaluate loop = `amos-self-regulated-simulative-planning-rscf`.

### 2.3 Embodied-R1.5 PGC loop

```text
Planner: decompose task into steps
    ↓
Grounder: ground steps in current observation
    ↓
Corrector: detect errors and re-plan
    ↓ (loop if correction needed)
```

**AMOS mapping**: O12 Plan → O14 Action → O15 Observation → repair cycle.

### 2.4 Hy-Embodied-VLM-1.0 MoE efficiency

~3B active parameters per token out of ~30B total. Only domain-relevant experts activate per task.

**AMOS mapping**: `amos-budget-aware-optimizer-selection-rscf-engine` — activate only necessary
parameters for the task.

## 3. AMOS Integration

### 3.1 VLA as unified cognitive architecture

The SOTA converges on VLA models that unify perception, reasoning, and action. AMOS's
`25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS` should be implementable as a VLA pipeline:

| AMOS Operation | VLA Component |
|:---|:---|
| O07 Inference (understanding) | VLM backbone |
| O08 Prediction (world model) | Latent predictor |
| O09 Simulation | World model rollout |
| O12 Plan | High-level policy with test-time computation |
| O13 Decision | Value model scoring |
| O14 Action (execution) | Continuous action expert |
| O15 Observation | Sensor feedback |
| Repair | PGC corrector loop |

### 3.2 World models for embodied simulation

AMOS `O09 Simulation` should integrate world model prediction as a first-class capability:

- Generate training data (embodied scene generation)
- Evaluate candidate actions (predict terminal observations)
- Enable test-time search (beam search over predicted futures)
- Validate safety envelopes (simulate before acting)

### 3.3 Closed-loop self-correction

AMOS `amos-audit-repair-master` should:

- Support **real-time correction** during execution (not just post-hoc)
- Use **world model predictions** to evaluate correction candidates
- Maintain **execution memory** for context-aware corrections
- Implement **PGC-style loops** for long-horizon tasks

### 3.4 Efficiency via MoE

AMOS `amos-budget-aware-optimizer-selection-rscf-engine` should apply MoE principles to embodied AI:

- Activate only domain-relevant skills/agents per task
- Route to lightweight models for simple subtasks
- Reserve full parameter activation for complex reasoning
- Use ~3B active params for latency-sensitive deployment

## 4. Cross-Domain Connections

| AMOS Domain | SOTA Connection | Mapping |
|:---|:---|:---|
| `21_DOMAINS/04_ROBOTICS` | All 5 papers | VLA foundation models |
| `04_RUNTIME` | GigaBrain-0.7 one-stage | Unified runtime pipeline |
| `07_SKILLS/amos-k-world-model` | Xiaomi-U0, τ₀-VLA | World model for embodied AI |
| `25_COGNITIVE_MATRIX/O09_SIMULATION` | τ₀-VLA beam search | World-model-guided simulation |
| `07_SKILLS/amos-audit-repair-master` | Embodied-R1.5 PGC loop | Closed-loop self-correction |
| `07_SKILLS/amos-test-time-compute-scaling` | τ₀-VLA | Compute-scalable inference |
| `07_SKILLS/amos-budget-aware-optimizer-selection` | Hy-Embodied MoE | Efficient parameter activation |
| `05_COGNITIVE_ORGANISM` | GigaBrain-0.7 three-system | Cognitive organism architecture |

## 5. Open Questions & Gaps

1. **Multi-embodiment generalization**: GigaBrain-0.7 demonstrates multi-embodiment training but
   doesn't prove zero-shot transfer to truly novel embodiments. AMOS needs embodiment-agnostic
   action representations.
2. **World model accuracy**: τ₀-VLA's world model predicts terminal observations but doesn't
   report prediction accuracy. AMOS `amos-prediction-governance` needs world model validation
   protocols.
3. **Long-horizon safety**: No SOTA paper addresses safety guarantees for 100+ step horizons.
   AMOS `amos-operational-modes` needs long-horizon safety envelopes.
4. **Data efficiency**: 37,000-40,115 hours of training data is enormous. AMOS `amos-few-shot`
   capabilities need to reduce this.
5. **Sim-to-real transfer**: All papers train on real-world data or simulation but don't
   formally characterize the sim-to-real gap. AMOS needs sim-to-real validation protocols.

## 6. Falsifiers

- `F-2026-09-04-EMB-1`: If GigaBrain-0.7's three-system architecture is shown to not outperform
  a single-system VLA at equal scale, AMOS must not adopt three-system decomposition as canonical.
- `F-2026-09-04-EMB-2`: If τ₀-VLA's test-time computation is shown to not improve success on
  tasks beyond 50 steps, AMOS must limit test-time search to short-horizon tasks.
- `F-2026-09-04-EMB-3`: If Embodied-R1.5's PGC loop is shown to increase latency beyond
  real-time thresholds (>100ms correction cycle), AMOS must use post-hoc correction for
  time-critical operations.
- `F-2026-09-04-EMB-4`: If Hy-Embodied-VLM-1.0's 3B active params cause >10% quality loss vs
  full 30B activation, AMOS must not use MoE for H-level embodied reasoning.

## 7. References

- arXiv:2608.15875 — GigaBrain-0.7: Scaling Embodied Foundation Models with Three-System Architecture. Aug 2026.
- arXiv:2607.11643 — Xiaomi-Robotics-U0: Unified Embodied Synthesis with World Foundation Model. Jul 2026.
- arXiv:2606.11324 — Embodied-R1.5: Evolving Physical Intelligence via Embodied Foundation Models. Jun 2026.
- arXiv:2608.16885 — τ₀-VLA: Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation. Aug 2026.
- Tencent. Hy-Embodied-VLM-1.0: Efficient MoE for Embodied Agents. Jul 2026.

---

**Related:** [[22_RESEARCH/01_PAPERS/SOTA_EMBODIED_ROBOT_FOUNDATION_MODELS_2026|Embodied Robot Foundation Models]] · [[22_RESEARCH/01_PAPERS/SOTA_EMBODIED_AI_AND_ROBOT_LEARNING_2026|Embodied AI & Robot Learning]] · [[22_RESEARCH/01_PAPERS/SOTA_WORLD_MODELS_PHYSICAL_AI_2026|World Models]] · [[22_RESEARCH/01_PAPERS/SOTA_FOUNDATION_AGENTS_AND_COGNITIVE_ARCHITECTURES_2026|Foundation Agents]]

**MOC:** [[11_KNOWLEDGE/11_KNOWLEDGE_MOC|11_KNOWLEDGE_MOC]] · [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
