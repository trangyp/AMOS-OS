---
title: "ArXiv Bridge 2025 Q3/Q4 — BCI, AI, Neuromorphic, Photonic & Quantum Substrates"
type: research_bridge
source: 22_RESEARCH/01_PAPERS
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE
date: 2025-09-05
epistemic_class: SOURCE_CLAIM
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: arxiv_2025_q3_q4
  scope: AMOS_research
---

# ArXiv Bridge 2025 Q3/Q4 — BCI, AI, Neuromorphic, Photonic & Quantum Substrates

## Purpose

This note bridges **late-2025 arXiv preprints** in BCI/neural decoding, AI-driven neurofoundation models, photonic/neuromorphic substrates, and quantum optical/memristive computing into the AMOS OS knowledge and engineering planes. Each entry is summarized, mapped to AMOS domains/skills/artifacts, and tagged with RSCF `SOURCE_CLAIM` (the paper's own claims) versus `AMOS_MODEL` (AMOS-specific interpretation). `DOCUMENTED != IMPLEMENTED` for all downstream mappings.

---

## 1. Brain-Computer Interfaces (BCI) & Neural Decoding

### 1.1 BiND — Bimanual Neural Discriminator-Decoder for Intracortical BCIs
- **arXiv ID:** 2509.03521 | [arXiv:2509.03521](https://arxiv.org/abs/2509.03521)
- **What it does:** Two-stage model that first classifies motion type (unimanual left / unimanual right / bimanual) and then uses specialized GRU decoders with a trial-relative time index to predict continuous 2D hand velocities from intracortical recordings.
- **Key result:** Mean R² = 0.76 for unimanual and 0.69 for bimanual trajectory prediction on a 13-session tetraplegic dataset; +2% over next-best GRU and +4% in cross-session analyses.
- **AMOS mapping:**
  - Domain: [[21_DOMAINS/23_UBI_BEI_BIOELECTROMAGNETIC/23_UBI_BEI_BIOELECTROMAGNETIC_MOC|UBI BEI / Bioelectromagnetic Intelligence]]
  - Plane: [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L01_SENSING_OBSERVATION/L01_SENSING_OBSERVATION_MOC|L01 Sensing/Observation]], [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L21_LEARNING/L21_LEARNING_MOC|L21 Learning]]
  - Skills: [[11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/UBI_NEUROBIOLOGICAL_INTELLIGENCE|UBI Neurobiological Intelligence]], [[07_SKILLS/amos-c04-bio-neuro-master/SKILL|amos-c04-bio-neuro-master]]
  - RSCF axis: `cross-session_robustness` — aligns with AMOS identity-continuity and runtime-context-reuse for neural-population drift.

### 1.2 A Generalist Intracortical Motor Decoder (NeurIPS 2025)
- **Source:** NeurIPS 2025 preprint | [NDT3 GitHub](https://github.com/joel99/ndt3)
- **What it does:** Autoregressive Transformer pretrained on 2,000 hours of neural population spiking activity paired with motor covariates from >30 monkeys and humans; evaluated as a foundation model for motor decoding.
- **Key result:** Improves decoding on 8 downstream tasks and generalizes across neural distribution shifts; scaling autoregressive Transformers does **not** resolve sensor variability and output stereotypy.
- **AMOS mapping:**
  - Plane: [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L03_PERCEPT_FORMATION/L03_PERCEPT_FORMATION_MOC|L03 Percept Formation]], [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L24_SELF_REGULATION/L24_SELF_REGULATION_MOC|L24 Self-Regulation]]
  - Skills: [[07_SKILLS/amos-c04-bio-neuro-master/SKILL|amos-c04-bio-neuro-master]], [[07_SKILLS/arxiv-selective-state-space-rscf/SKILL|arxiv-selective-state-space-rscf]]
  - RSCF axis: `foundation_model_generalization` — pretraining ↔ AMOS `memory_consolidation`; `UNKNOWN/GAP` on sensor-variability closure.

### 1.3 BaRISTA — Brain Scale Informed Spatiotemporal Representation
- **arXiv ID:** 2512.12135 | [arXiv:2512.12135](https://arxiv.org/abs/2512.12135)
- **What it does:** Spatiotemporal transformer for multiregional intracranial recordings with a self-supervised masked latent-reconstruction objective; supports variable spatial scales from single channels to brain regions.
- **Key result:** Learns brain network patterns and enhances downstream decoding; tokenization is scale-aware.
- **AMOS mapping:**
  - Plane: [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L08_REPRESENTATION/L08_REPRESENTATION_MOC|L08 Representation]], [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C07_PERCEPTION/C07_PERCEPTION_MOC|C07 Perception]]
  - Skills: [[11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/UBI_NEUROBIOLOGICAL_INTELLIGENCE|UBI Neurobiological Intelligence]], [[07_SKILLS/MULTIMODAL_SENSOR_FUSION_EKF_LEDGER|MULTIMODAL_SENSOR_FUSION_EKF_LEDGER]]
  - RSCF axis: `multiscale_tokenization` — aligns with AMOS RSCF structural-axis taxonomy and H/M/L fractal resolution.

---

## 2. Neuromorphic & Photonic AI Substrates

### 2.1 Nonlinear Photonic Neuromorphic Chips for Spiking RL
- **arXiv ID:** 2508.06962 | [arXiv:2508.06962](https://arxiv.org/abs/2508.06962)
- **What it does:** 16-channel programmable incoherent photonic neuromorphic chip co-designing a simplified MZI mesh with DFB-SA lasers; implements both linear and nonlinear spike computations in the optical domain.
- **Key result:** Photonic spiking RL with 1.39 TOPS/W (linear) / 987.65 GOPS/W (nonlinear) and 320 ps latency; CartPole and Pendulum benchmarks converge to standard PPO reward.
- **AMOS mapping:**
  - Plane: [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C08_EXECUTION/C08_EXECUTION_MOC|C08 Execution]], [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L21_LEARNING/L21_LEARNING_MOC|L21 Learning]]
  - Skills: [[07_SKILLS/amos-c10-tech-engineering-master/SKILL|amos-c10-tech-engineering-master]], [[02_KERNEL/QUANTUM_NEUROMORPHIC_PHOTONIC_EXECUTION_MODEL|Quantum-Neuromorphic-Photonic Execution Model]]
  - RSCF axis: `energy_efficiency` — orders-of-magnitude sparse-workload advantage ↔ AMOS `runtime-benchmarking` and `capability_bound_governance`.

### 2.2 Emergent Learning — Neuromorphic Photonic Computing with Accelerated Training
- **arXiv ID:** 2512.13372 | [arXiv:2512.13372](https://arxiv.org/abs/2512.13372)
- **What it does:** Transforms a disordered optical medium (DMD + scattering + camera) into a photonic device that stores, recognizes, and classifies arbitrary memory patterns via an optical-synaptic matrix.
- **Key result:** Hardware co-localization of memory and optical operator; capacity ~10⁶⁰⁵⁵⁷ tailored memories; shifts training burden into the optical domain.
- **AMOS mapping:**
  - Plane: [[10_MEMORY/10_MEMORY_MOC|10_MEMORY]], [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L05_BINDING/L05_BINDING_MOC|L05 Binding]]
  - Skills: [[07_SKILLS/amos-memory-systems-master/SKILL|amos-memory-systems-master]], [[02_KERNEL/QUANTUM_NEUROMORPHIC_PHOTONIC_EXECUTION_MODEL|Quantum-Neuromorphic-Photonic Execution Model]]
  - RSCF axis: `memory_compute_cotenant` — aligns with AMOS `memory_substrate` and `action-memory_firewall` for optical memory admission.

---

## 3. Quantum AI & Hybrid Substrates

### 3.1 Quantum Optical Neural Networks with Atom-Cavity Nonlinearity
- **arXiv ID:** 2511.06167 | [arXiv:2511.06167](https://arxiv.org/abs/2511.06167)
- **What it does:** Quantum optical neural network (QONN) using atom-cavity neurons with controllable photon absorption/emission to replace electronic nonlinear-activation components in optical neural networks.
- **Key result:** MNIST and SAT-6 satellite image classification with low power and compact hardware; convolutional QONN demonstrated.
- **AMOS mapping:**
  - Plane: [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L08_REPRESENTATION/L08_REPRESENTATION_MOC|L08 Representation]], [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C08_EXECUTION/C08_EXECUTION_MOC|C08 Execution]]
  - Skills: [[01_CANON/02_UNIVERSE_CANON/OMEGA_QUANTUM_STACK_CANON|Omega Quantum Stack Canon]], [[07_SKILLS/amos-c03-physics-cosmos-master/SKILL|amos-c03-physics-cosmos-master]]
  - RSCF axis: `quantum_optical_activation` — `AMOS_MODEL` mapping only; physical quantum advantage for AMOS perception is `UNKNOWN/GAP`.

### 3.2 Experimental Neuromorphic Computing Based on Quantum Memristor
- **arXiv ID:** 2504.18694 | [arXiv:2504.18694](https://arxiv.org/abs/2504.18694)
- **What it does:** First neuromorphic architecture built on a photonic quantum memristor; memristive feedback loop enhances nonlinearity without entangling gates.
- **Key result:** Benchmarked on a nonlinear function and three time-series prediction tasks; quantum memristive element is shown as a building block for larger networks.
- **AMOS mapping:**
  - Plane: [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L12_COUNTERFACTUAL_SIMULATION/L12_COUNTERFACTUAL_SIMULATION_MOC|L12 Counterfactual Simulation]], [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L13_PREDICTION/L13_PREDICTION_MOC|L13 Prediction]]
  - Skills: [[11_KNOWLEDGE/05_FRAMEWORKS/QLS_FRAMEWORK|QLS Framework]], [[07_SKILLS/amos-c03-physics-cosmos-master/SKILL|amos-c03-physics-cosmos-master]]
  - RSCF axis: `quantum_bio_bridge` — maps to AMOS `biology-quantum-bridge-governor` anti-overclaim firewall; all quantum-biological mappings are `MODEL` / `METAPHOR`.

---

## 4. Synthesis: AMOS Substrate Architecture Convergence

| Strand | 2025 Q3/Q4 Frontier | AMOS Binding |
|---|---|---|
| BCI decoding | Permutation-invariant, generalist, multiscale spatiotemporal models | L01/L03/L07/L08 + UBI NBI + 05_COGNITIVE_ORGANISM/01_SENSING_OBSERVATION |
| Photonic compute | MZI/nonlinear spike, disordered-medium emergent learning | C08 Execution + 10_MEMORY + 02_KERNEL/QUANTUM_NEUROMORPHIC_PHOTONIC_EXECUTION_MODEL |
| Quantum activation | Atom-cavity QONN, photonic quantum memristor | C08/C12 + 01_CANON/OMEGA_QUANTUM_STACK* + QLS |
| Cross-cutting | Energy/throughput/scale-aware substrate selection | 04_RUNTIME/HARDWARE_AWARE_RUNTIME_INTEGRATION + 04_RUNTIME/06_EXECUTION |

These advances converge on the **hardware-aware runtime problem** AMOS is formalizing in `04_RUNTIME/HARDWARE_AWARE_RUNTIME_INTEGRATION` and `02_KERNEL/QUANTUM_NEUROMORPHIC_PHOTONIC_EXECUTION_MODEL`: a workload contract → capability registry → substrate selector → kernel driver → verification → receipt pipeline.

---

## Cross-References

- Sibling bridge: [[22_RESEARCH/01_PAPERS/ARXIV_BRIDGE_2025_BCI_NEUROMORPHIC_PHOTONIC_QUANTUM|ARXIV_BRIDGE_2025_BCI_NEUROMORPHIC_PHOTONIC_QUANTUM]]
- Domain: [[21_DOMAINS/14_C04_BIO_NEURO/14_C04_BIO_NEURO_MOC|14_C04_BIO_NEURO_MOC]] · [[21_DOMAINS/23_UBI_BEI_BIOELECTROMAGNETIC/23_UBI_BEI_BIOELECTROMAGNETIC_MOC|23_UBI_BEI_BIOELECTROMAGNETIC_MOC]]
- Runtime: [[04_RUNTIME/HARDWARE_AWARE_RUNTIME_INTEGRATION|HARDWARE_AWARE_RUNTIME_INTEGRATION]] · [[02_KERNEL/QUANTUM_NEUROMORPHIC_PHOTONIC_EXECUTION_MODEL|QUANTUM_NEUROMORPHIC_PHOTONIC_EXECUTION_MODEL]]
- Memory: [[10_MEMORY/MEMORY_DYNAMICS_AND_SUBSTRATE_INTEGRATION|MEMORY_DYNAMICS_AND_SUBSTRATE_INTEGRATION]] · [[10_MEMORY/10_MEMORY_MOC|10_MEMORY_MOC]]

## Epistemic Boundary

All paper summaries are `SOURCE_CLAIM` (arXiv preprint / conference preprint) with `NOT_INDEPENDENTLY_ESTABLISHED` experimental validation status. AMOS cross-plane mappings are `AMOS_MODEL` / `DERIVED`. No claim is made that AMOS implements these substrates or that the quantum-biological analogies are physically causal. `UNKNOWN/GAP` is preserved for runtime executable closure.