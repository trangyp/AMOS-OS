---
type: research_synthesis
source: 22_RESEARCH/01_PAPERS
aliases:
  - SOTA_NEURAL_SCALING_LAWS_AND_EMERGENT_ABILITIES_2026
  - 22_RESEARCH/01_PAPERS/SOTA_NEURAL_SCALING_LAWS_AND_EMERGENT_ABILITIES_2026
amos_core_target: v4.4
artifact_id: AMOS-PAPER-SCALING-LAWS-EMERGENT-2026
conclusion_class: DERIVED
epistemic_class: SOURCE_CLAIM
created: 2026-09-04
origin_architect: Trang Phan
status: ACTIVE_SPECIFICATION
tags:
  - amos
  - research
  - scaling-laws
  - emergent-abilities
  - phase-transitions
  - grokking
  - representation-geometry
  - model-calibration
title: "Neural Scaling Laws and Emergent Abilities: 2026 State of the Art in Phase-Transitional Learning Dynamics"
rscf:
  state: SOURCE_CLAIM
  provenance: arxiv_corpus_2026
  scope: active__AMOS_OS
---

# Neural Scaling Laws and Emergent Abilities: 2026 State of the Art

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **Epistemic Class:** `SOURCE_CLAIM`
> **Status:** `ACTIVE_RESEARCH`

---

## Abstract

Neural scaling laws — the empirical regularities governing how model performance improves with parameters, data, and compute — have evolved from simple power-law descriptions to sophisticated frameworks incorporating phase transitions, representation geometry, and universal critical phenomena. This synthesis reviews the 2026 state of the art, covering: (1) Phase-Transitional Scaling (PTS), which treats emergent abilities as sigmoidal phase transitions with universal curve collapse; (2) the geometric anatomy of capability acquisition, revealing collapse-recovery-behavior sequences; (3) layer-wise discrete emergence as a universal architectural property; (4) grokking as a dimensional phase transition with self-organized criticality; and (5) Unified Neural Scaling Laws (UNSL) for multi-dimensional extrapolation. These advances directly inform AMOS model calibration, cognitive scale selection, and the prediction of capability emergence across the cognitive matrix scales.

---

## Key Findings (2026)

### 1. Phase-Transitional Scaling (PTS)
The PTS framework (OpenReview 2026) provides a **falsifiable, quantitative** account of emergent abilities as phase transitions:
- Each capability $K$ is characterized by a **sigmoidal response** with threshold $T_K$ and sharpness $\gamma_K$
- Connected to three theoretical perspectives: **finite-size mean-field theory**, **percolation on representational graphs**, and **noise-activated barrier crossing** in training dynamics
- Validated across **12 diverse capabilities**: sigmoid form confirmed in 47/48 comparisons
- $T_K$ is controlled by **data complexity** ($R^2 = 0.89$); $\gamma_K$ is controlled by **training dynamics** ($R^2 = 0.76$)
- **Universal curve collapse** across different architectures (94% variance explained)
- Outperforms power-law baselines by **4× in out-of-sample prediction accuracy**

### 2. Geometric Anatomy of Capability Acquisition
Systematic tracking across six transformer sizes (405K–151M parameters), eight algorithmic tasks, and three Pythia models (arXiv:2602.15997) reveals:
- Representations first **collapse to a low-dimensional state**, then **recover**, and only then does **behavioral performance improve**
- Linear probes show task-relevant information exists in hidden states **before** the model can act on it
- The **collapse floor** is task-specific; collapse propagates **top-down** through the network
- Only **RankMe** reliably precedes capability acquisition for hard tasks
- For hard tasks: geometry changes first, behavior follows (precursor gap ~49K training steps on Pythia-2.8B logical deduction)
- For easy tasks: both happen simultaneously — no precursor detectable

### 3. Universal Discrete Layer-Wise Emergence
Layer-by-layer probing across seven architecturally diverse models spanning three orders of magnitude (2026):
- Nearly all model-task combinations exhibit **abrupt accuracy transitions at specific network depths** — not gradual improvement
- Post-emergence performance converges to **remarkably consistent levels** — suggesting binary competence states
- Robust **task-dependent emergence ordering**: linguistic capabilities crystallize in shallower layers; abstract reasoning requires deeper computation
- Hierarchy is **consistent across all tested architectures** — universal organizing principles independent of model family
- Size-dependent effects are **complex and non-monotonic** — architectural details modulate pure scaling effects

### 4. Grokking as Dimensional Phase Transition
Finite-size scaling of gradient avalanche dynamics across eight model scales (arXiv:2604.04655):
- Grokking is a **dimensional phase transition**: effective dimensionality $D$ crosses from sub-diffusive ($D < 1$) to super-diffusive ($D > 1$) at generalization onset
- Exhibits **self-organized criticality (SOC)**
- $D$ reflects **gradient field geometry**, not network architecture: synthetic i.i.d. Gaussian gradients maintain $D \approx 1$ regardless of topology
- Real training exhibits **dimensional excess** from backpropagation correlations
- The $D(t)$ crossing is **robust across topologies** — offers new insight into trainability of overparameterized networks

### 5. Unified Neural Scaling Laws (UNSL)
UNSL (arXiv:2605.26248) provides a functional form that accurately models scaling as **multiple dimensions vary simultaneously**:
- Models how evaluation metric varies with parameters, dataset size, training steps, inference steps, and hyperparameters
- Yields **considerably more accurate extrapolations** than prior functional forms
- Validated across various architectures and diverse upstream/downstream tasks

---

## Technical Details

### Phase-Transitional Scaling Form

The PTS sigmoidal response for capability $K$:

$$\text{Acc}_K(N) = \frac{1}{1 + \exp\left[-\gamma_K (N - T_K)\right]}$$

where $N$ is a composite resource variable (parameters × data × compute), $T_K$ is the transition threshold, and $\gamma_K$ is the sharpness. Universal curve collapse is achieved via:

$$\tilde{N} = \gamma_K (N - T_K), \quad \tilde{\text{Acc}} = \text{Acc}_K(N)$$

### Representation Geometry Stages

| Stage | Description | Indicator |
|:---|:---|:---|
| Collapse | Hidden states compress to low-dimensional manifold | RankMe ↓ |
| Recovery | Dimensionality increases as task-relevant features emerge | RankMe ↑ |
| Compression | Final compact representation for efficient computation | RankMe stabilizes |
| Behavioral | Task performance improves | Accuracy ↑ |

### Grokking Dimensional Transition

The effective dimensionality $D(t)$ is computed via finite-size scaling of gradient norms:

$$D(t) = \frac{d \ln \langle \|\nabla L\|^2 \rangle}{d \ln t}$$

- Sub-diffusive regime: $D < 1$ (memorization, gradient correlations weak)
- Super-diffusive regime: $D > 1$ (generalization, gradient correlations strong)
- Critical crossing: $D(t_c) = 1$ marks generalization onset

### UNSL Multi-Dimensional Form

UNSL models loss as a function of multiple scaling dimensions:

$$L(N, D, S, T_{\text{inf}}, \theta) = f\left(\frac{N^\alpha}{D^\beta}, \frac{S^\sigma}{N^\alpha}, g(T_{\text{inf}}, \theta)\right)$$

where $N$ = parameters, $D$ = data, $S$ = training steps, $T_{\text{inf}}$ = inference steps, $\theta$ = hyperparameters, and $\alpha, \beta, \sigma$ are task-dependent exponents.

---

## AMOS Integration

### Cognitive Scale Selection
- [[25_COGNITIVE_MATRIX/04_SCALES/04_SCALES_MOC|Cognitive Matrix Scales]] — PTS thresholds $T_K$ map to AMOS scale transitions (L→M→H)
- [[25_COGNITIVE_MATRIX/04_SCALES/H_HIGH_SCALE/H_HIGH_SCALE_MOC|High Scale]] — emergent capabilities at large parameter counts
- [[25_COGNITIVE_MATRIX/04_SCALES/L_LOW_SCALE/L_LOW_SCALE_MOC|Low Scale]] — base capabilities below emergence thresholds

### Model Calibration
- [[13_MODELS/13_MODELS_MOC|Models Plane]] — UNSL for multi-dimensional model performance forecasting
- [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L21_LEARNING/L21_LEARNING_MOC|L21 Learning]] — grokking dynamics inform learning rate and regularization schedules

### Cognitive Organism
- [[05_COGNITIVE_ORGANISM/04_COGNITION/04_COGNITION_MOC|Cognition]] — representation geometry stages map to cognitive matrix layer transitions
- [[05_COGNITIVE_ORGANISM/18_LIFECYCLE/18_LIFECYCLE_MOC|Lifecycle]] — capability emergence ordering informs developmental staging

### Related SOTA Papers
- [[22_RESEARCH/01_PAPERS/SOTA_MECHANISTIC_INTERPRETABILITY_AND_CIRCUIT_ANALYSIS_2026|Mechanistic Interpretability]] — circuit formation during grokking
- [[22_RESEARCH/01_PAPERS/SOTA_AI_REASONING_AND_WORLD_MODELS_2026|AI Reasoning & World Models]] — emergent reasoning capabilities
- [[22_RESEARCH/01_PAPERS/SOTA_FRACTAL_COGNITIVE_ARCHITECTURES_AND_ENTROPY_BOUNDS_2026|Fractal Cognitive Architectures]] — scale-invariant cognitive structures

### Domain Bindings
- [[21_DOMAINS/12_C02_MATH_COMPUTE/12_C02_MATH_COMPUTE_MOC|Math-Compute Domain]] — computational resource scaling
- [[21_DOMAINS/15_C05_MIND_BEHAVIOR/15_C05_MIND_BEHAVIOR_MOC|Mind-Behavior Domain]] — cognitive development parallels

---

## References

1. **Phase-Transitional Scaling** — OpenReview 2026, github.com/KalChe/Phase-Transitional-Scaling
2. **The Geometric Anatomy of Capability Acquisition in Transformers** — arXiv:2602.15997 (2026)
3. **Layer-Wise Analysis Reveals Universal Discrete Emergence Across LLM Architectures** — doi:10.21203/rs.3.rs-8178590/v1 (2026)
4. **Grokking as Dimensional Phase Transition in Neural Networks** — arXiv:2604.04655 (2026)
5. **Unified Neural Scaling Laws** — arXiv:2605.26248 (2026)
6. Kaplan, J. et al. — Scaling Laws for Neural Language Models, arXiv:2001.08361 (2020)
7. Hoffmann, J. et al. — Training Compute-Optimal Large Language Models (Chinchilla), arXiv:2203.15556 (2022)
8. Wei, J. et al. — Emergent Abilities of Large Language Models, arXiv:2206.07682 (2022)
9. Power, A. et al. — Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets, arXiv:2201.09799 (2022)

---

> **Epistemic Boundary:** PTS sigmoidal form is validated on 12 capabilities but may not hold for all emergent abilities. The geometric precursor gap is detectable only when task difficulty is high relative to model capacity. Layer-wise discrete emergence is probed on specific tasks and may not generalize to all capability types. UNSL extrapolation accuracy is validated on specific architecture families. `SOURCE_CLAIM != VERIFIED` for universal applicability.
