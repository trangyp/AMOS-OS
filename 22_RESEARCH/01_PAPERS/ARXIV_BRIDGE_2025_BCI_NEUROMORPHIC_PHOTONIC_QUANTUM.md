---
title: "ArXiv Bridge 2025 — BCI / Neuromorphic / Photonic AI / Quantum Error Correction"
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
  provenance: arxiv_2025
  scope: AMOS_research
---

# ArXiv Bridge 2025 — BCI, Neuromorphic, Photonic AI & Quantum Error Correction

## Purpose

This note bridges **late-2025 arXiv preprints** in four high-impact areas into the AMOS OS knowledge and engineering planes. Each entry is summarized, mapped to AMOS domains/skills/artifacts, and tagged with RSCF `SOURCE_CLAIM` (the paper's own claims) versus `AMOS_MODEL` (AMOS-specific interpretation). `DOCUMENTED != IMPLEMENTED` for all downstream mappings.

---

## 1. Brain-Computer Interfaces (BCI) & Neural Decoding

### 1.1 MultiDiffNet — Multi-Objective Diffusion for Generalizable Brain Decoding
- **arXiv ID:** 2511.18294
- **What it does:** Diffusion-based latent-space decoder for EEG that generalizes across subjects and sessions without synthetic subject generation.
- **Key result:** Unified benchmark suite across SSVEP, motor imagery, P300, and imagined speech; strong cross-subject/cross-session generalization.
- **AMOS mapping:**
  - Domain: [[21_DOMAINS/23_UBI_BEI_BIOELECTROMAGNETIC/23_UBI_BEI_BIOELECTROMAGNETIC_MOC|UBI BEI / Bioelectromagnetic Intelligence]]
  - Plane: [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C07_PERCEPTION/C07_PERCEPTION_MOC|C07 Perception]], [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L01_SENSING_OBSERVATION/L01_SENSING_OBSERVATION_MOC|L01 Sensing/Observation]]
  - Skills: [[11_KNOWLEDGE/05_FRAMEWORKS/BEI_BIOELECTROMAGNETIC_INTELLIGENCE|BEI Bioelectromagnetic Intelligence]], [[07_SKILLS/MULTIMODAL_SENSOR_FUSION_EKF_LEDGER|MULTIMODAL_SENSOR_FUSION_EKF_LEDGER]]
  - RSCF axis: `generalization` — subject-disjoint evaluation aligns with AMOS `confidence_ceiling` and `UNKNOWN/GAP` when subject drift is unverified.

### 1.2 SPINT — Spatial Permutation-Invariant Transformer for Intracortical Motor Decoding
- **arXiv ID:** 2507.08402
- **What it does:** Set-based transformer for intracortical BCI that infers unit-specific identities dynamically, enabling zero-shot/few-shot cross-session decoding.
- **Key result:** Eliminates test-time alignment and fine-tuning; evaluated on FALCON Benchmark.
- **AMOS mapping:**
  - Plane: [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L03_PERCEPT_FORMATION/L03_PERCEPT_FORMATION_MOC|L03 Percept Formation]], [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L24_SELF_REGULATION/L24_SELF_REGULATION_MOC|L24 Self-Regulation]]
  - Skills: [[11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/UBI_NEUROBIOLOGICAL_INTELLIGENCE|UBI Neurobiological Intelligence]], [[07_SKILLS/amos-adaptive-stability-balancer/SKILL|amos-adaptive-stability-balancer]]
  - Mapping: permutation-invariance ↔ AMOS identity-continuity for neural-population drift.

### 1.3 EDAPT — Calibration-Free BCIs with Continual Online Adaptation
- **arXiv ID:** 2508.10474
- **What it does:** Population pretraining + online continual fine-tuning for EEG decoders; updates within 200 ms on consumer hardware.
- **Key result:** Accuracy scales with total data budget rather than subject/trial allocation.
- **AMOS mapping:**
  - Plane: [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L21_LEARNING/L21_LEARNING_MOC|L21 Learning]], [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L29_EVOLUTION/L29_EVOLUTION_MOC|L29 Evolution]]
  - Skills: [[11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/UBI_NEUROBIOLOGICAL_INTELLIGENCE|UBI Neurobiological Intelligence]], [[07_SKILLS/amos-closed-loop-learning-governor/SKILL|amos-closed-loop-learning-governor]]
  - Mapping: continual personalization ↔ AMOS `UBI_ENTROPY_CORRECTION` and `runtime_context_reuse`.

### 1.4 POSSM — Hybrid State-Space Models for Real-Time Neural Decoding
- **arXiv ID:** 2506.05320
- **What it does:** Spike-token cross-attention + recurrent SSM for causal online neural decoding; up to 9× faster than Transformers on GPU.
- **Key result:** Pretraining on monkey motor cortex transfers to human handwriting and speech decoding.
- **AMOS mapping:**
  - Plane: [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L13_PREDICTION/L13_PREDICTION_MOC|L13 Prediction]], [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L03_PERCEPT_FORMATION/L03_PERCEPT_FORMATION_MOC|L03 Percept Formation]]
  - Skills: [[11_KNOWLEDGE/05_FRAMEWORKS/BEI_BIOELECTROMAGNETIC_INTELLIGENCE|BEI Bioelectromagnetic Intelligence]], [[07_SKILLS/arxiv-selective-state-space-rscf/SKILL|arxiv-selective-state-space-rscf]]
  - Mapping: cross-species transfer ↔ AMOS `domain_bridge` and `provenance` tagging.

### 1.5 BrainOmni — Brain Foundation Model for Unified EEG & MEG
- **arXiv ID:** 2505.18185
- **What it does:** First unified brain foundation model across heterogeneous EEG/MEG recordings; introduces `BrainTokenizer` for spatiotemporal brain tokens.
- **Key result:** Sensor-encoder handles spatial layout, orientation, and modality for cross-device generalization.
- **AMOS mapping:**
  - Plane: [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L08_REPRESENTATION/L08_REPRESENTATION_MOC|L08 Representation]], [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C07_PERCEPTION/C07_PERCEPTION_MOC|C07 Perception]]
  - Skills: [[11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/UBI_NEUROBIOLOGICAL_INTELLIGENCE|UBI Neurobiological Intelligence]], [[07_SKILLS/amos-universal-coordinate-rscf-engine/SKILL|amos-universal-coordinate-rscf-engine]]
  - Mapping: unified tokenization ↔ AMOS `RSCF` structural-axis taxonomy and multi-modal sensor fusion.

---

## 2. Neuromorphic Computing

### 2.1 Fully Integrated Memristive SNN with Analog Neurons
- **arXiv ID:** 2509.04960
- **What it does:** 128×24 memristor array + analog neurons on CMOS; trains directly on spatiotemporal data via surrogate gradient; 93.06% on DVS128 Gesture at 101.05 TSOPS/W.
- **Key result:** Time-scaling property allows compact capacitors and 50,000× accelerated samples (30 µs).
- **AMOS mapping:**
  - Plane: [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C08_EXECUTION/C08_EXECUTION_MOC|C08 Execution]], [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L02_ATTENTION/L02_ATTENTION_MOC|L02 Attention]]
  - Skills: [[07_SKILLS/amos-neural-ode-dynamics-rscf-engine/SKILL|amos-neural-ode-dynamics-rscf-engine]], [[07_SKILLS/amos-entropy-lacunarity-governor/SKILL|amos-entropy-lacunarity-governor]]
  - Mapping: event-driven, energy-efficient inference ↔ AMOS `compute_energy_regulation` and `metabolism` contracts.

### 2.2 Unified Memcapacitor-Memristor Memory for RSNNs
- **arXiv ID:** 2506.22227
- **What it does:** Fabricated memory stack that unifies memristive and memcapacitive behavior to control spatial and temporal dynamics in recurrent SNNs.
- **Key result:** Single silicon-doped hafnium-oxide + Ti scavenging layer device can serve as synaptic weight and neuron time-constant.
- **AMOS mapping:**
  - Plane: [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L07_MEMORY/L07_MEMORY_MOC|L07 Memory]], [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L21_LEARNING/L21_LEARNING_MOC|L21 Learning]]
  - Skills: [[07_SKILLS/amos-memory-systems-master/SKILL|amos-memory-systems-master]], [[07_SKILLS/amos-distinct-working-memory-rscf/SKILL|amos-distinct-working-memory-rscf]]
  - Mapping: unified synapse/neuron memory ↔ AMOS `memory-admission` and `context-continuity` invariants.

---

## 3. Photonic AI

### 3.1 Integrated Photonic DNN with End-to-End On-Chip Backpropagation
- **arXiv ID:** 2506.14575
- **What it does:** First fully on-chip photonic DNN training by backpropagation on a single photonic chip, robust to fabrication variations.
- **Key result:** Linear and nonlinear computations performed photonically; matches ideal digital accuracy.
- **AMOS mapping:**
  - Plane: [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C08_EXECUTION/C08_EXECUTION_MOC|C08 Execution]], [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L21_LEARNING/L21_LEARNING_MOC|L21 Learning]]
  - Skills: [[02_KERNEL/QUANTUM_NEUROMORPHIC_PHOTONIC_EXECUTION_MODEL|Quantum-Neuromorphic-Photonic Execution Model]] (gap: [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L28_GOVERNANCE/L28_GOVERNANCE_MOC|L28 Governance]])
  - Mapping: on-chip training ↔ AMOS `runtime-benchmarking` and `capability_bound_governance`.

### 3.2 Versatile Silicon Integrated Photonic Processor for AI Clusters
- **arXiv ID:** 2504.01463
- **What it does:** 40 programmable unit cells, 160+ components; supports computing acceleration, signal processing, photonic switching, and secure encryption.
- **Key result:** Reconfigurable optoelectronic system for AI clusters.
- **AMOS mapping:**
  - Plane: [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C08_EXECUTION/C08_EXECUTION_MOC|C08 Execution]], [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L16_PLANNING/L16_PLANNING_MOC|L16 Planning]]
  - Skills: [[07_SKILLS/amos-infrastructure-control-plane/SKILL|amos-infrastructure-control-plane]], [[07_SKILLS/amos-observability-driven-harness-evolution-rscf/SKILL|amos-observability-driven-harness-evolution-rscf]]
  - Mapping: reconfigurable photonic interconnect ↔ AMOS `routing-policy` and `event-bus`.

### 3.3 Fully Analog End-to-End Online Training on Photonic Platform
- **arXiv ID:** 2506.18041
- **What it does:** Foundry silicon photonic chip with microring weight bank and on-chip photodetectors; real-time MGD online training at GBaud rates.
- **Key result:** >90% linear and >80% nonlinear classification accuracy; self-learning parameter adjustment.
- **AMOS mapping:**
  - Plane: [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L21_LEARNING/L21_LEARNING_MOC|L21 Learning]], [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L22_CONSOLIDATION/L22_CONSOLIDATION_MOC|L22 Consolidation]]
  - Skills: [[07_SKILLS/amos-calibrated-feedback-control-rscf/SKILL|amos-calibrated-feedback-control-rscf]], [[07_SKILLS/amos-ai-drift-alignment-governor/SKILL|amos-ai-drift-alignment-governor]]
  - Mapping: online adaptive photonic training ↔ AMOS `drift-alignment` and `calibrated-feedback`.

---

## 4. Quantum Error Correction

### 4.1 Robust Phase of Continuous Transversal Gates in Stabilizer Codes
- **arXiv ID:** 2510.01319
- **What it does:** Surface-code phase of continuously tunable logical unitaries via transversal operations; infidelity exponentially suppressed in code distance.
- **Key result:** Lowers overhead for continuous-angle logical rotations in quantum simulation.
- **AMOS mapping:**
  - Plane: [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L12_COUNTERFACTUAL_SIMULATION/L12_COUNTERFACTUAL_SIMULATION_MOC|L12 Counterfactual Simulation]], [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L13_PREDICTION/L13_PREDICTION_MOC|L13 Prediction]]
  - Skills: [[11_KNOWLEDGE/05_FRAMEWORKS/QLS_FRAMEWORK|QLS Framework]], [[01_CANON/02_UNIVERSE_CANON/OMEGA_QUANTUM_STACK_CANON|Omega Quantum Stack Canon]]
      - Quantum: [[21_DOMAINS/41_QUANTUM_SYSTEMS/41_QUANTUM_SYSTEMS_MOC|41_QUANTUM_SYSTEMS]]
  - Mapping: transversal logical gates ↔ AMOS `law-stack-enforcement` and `fail-closed` invariants.

### 4.2 Lattice Surgery with Bell Measurements for Modular QEC
- **arXiv ID:** 2510.13541
- **What it does:** Surface-code lattice surgery using only Bell measurements; halves module-crossing gates and saves ~40% entanglement.
- **Key result:** Stronger logical error suppression for given entanglement rate across link noise regimes.
- **AMOS mapping:**
  - Plane: [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L05_BINDING/L05_BINDING_MOC|L05 Binding]], [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C09_KERNEL_CONTROL/C09_KERNEL_CONTROL_MOC|C09 Kernel Control]]
  - Skills: [[01_CANON/02_UNIVERSE_CANON/OMEGA_QUANTUM_STACK_CANON|Omega Quantum Stack Canon]], [[01_CANON/02_UNIVERSE_CANON/OMEGA_QUANTUM_STACK|Omega Quantum Stack]]
  - Mapping: modular entanglement ↔ AMOS `k-binding` and `distributed-causal-evolution` contracts.

### 4.3 Optimal Spin-Qubit Shuttling Bus for Surface Code
- **arXiv ID:** 2510.17689
- **What it does:** Mixed-integer optimization of 1D shuttling bus architecture for rotated surface code using spin-qubit shuttling.
- **Key result:** Logical error rates down to 2×10⁻¹⁰ per round at code distance 21 under realistic noise.
- **AMOS mapping:**
  - Plane: [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L16_PLANNING/L16_PLANNING_MOC|L16 Planning]], [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C09_KERNEL_CONTROL/C09_KERNEL_CONTROL_MOC|C09 Kernel Control]]
  - Skills: [[01_CANON/02_UNIVERSE_CANON/OMEGA_QUANTUM_STACK|Omega Quantum Stack]], [[02_KERNEL/01_META_LOGIC/K_QCLA|K_QCLA]]
  - Mapping: shuttling-bus layout optimization ↔ AMOS `subsystem-constraint-layer` and `evolution-budget`.

### 4.4 Superconducting Three-Qubit Gates for Surface Code
- **arXiv ID:** 2506.09028
- **What it does:** 3-qubit CZZ gate for transmon qubits (35 ns, 99.96% fidelity); improves surface-code threshold by ~50% to ~1.2%.
- **Key result:** Reduces logical error by up to one order of magnitude vs standard CZ readout.
- **AMOS mapping:**
  - Plane: [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C08_EXECUTION/C08_EXECUTION_MOC|C08 Execution]], [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L18_ACTION/L18_ACTION_MOC|L18 Action]]
  - Skills: [[01_CANON/02_UNIVERSE_CANON/OMEGA_QUANTUM_STACK_CANON|Omega Quantum Stack Canon]], [[01_CANON/02_UNIVERSE_CANON/OMEGA_QUANTUM_STACK|Omega Quantum Stack]]
  - Mapping: high-fidelity multi-qubit gates ↔ AMOS `enforcement-root-attestation` and `commit-time-authorization`.

### 4.5 Logical Error Rates Under Trapped-Ion Inspired Noise
- **arXiv ID:** 2508.14227
- **What it does:** Surface-code logical channels under mixed coherent/stochastic circuit-level noise for trapped-ion QCCD architectures.
- **Key result:** Coherent dephasing during idling/transport is quantified for near-term trapped-ion QEC.
- **AMOS mapping:**
  - Plane: [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L13_PREDICTION/L13_PREDICTION_MOC|L13 Prediction]], [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L11_CAUSAL_MODELING/L11_CAUSAL_MODELING_MOC|L11 Causal Modeling]]
  - Skills: [[01_CANON/02_UNIVERSE_CANON/OMEGA_QUANTUM_STACK|Omega Quantum Stack]], [[07_SKILLS/amos-adversarial-entropy-accountant/SKILL|amos-adversarial-entropy-accountant]]
  - Mapping: coherent error modeling ↔ AMOS `entropy-lacunarity` and `failure-memory`.

---

## Synthesis & Open Gaps

| Theme | AMOS relevance | Gaps to close |
| :---- | :------------- | :------------ |
| BCI generalization | C07 Perception, C05 Representation, BEI/UBI domains | Calibration-free transfer; cross-subject `confidence_ceiling` |
| Neuromorphic hardware | C08 Execution, L07 Memory, metabolism | Device-to-runtime `enforcement-trust` boundary |
| Photonic AI | C08 Execution, L21 Learning | On-chip training `provenance` and `drift-alignment` |
| Quantum error correction | C09 Kernel Control, L16 Planning, 41_QUANTUM_SYSTEMS | Logical gate `authority` and `commit-time` receipts |

## Epistemic boundary

- All arXiv IDs are `SOURCE_CLAIM` from the preprints.
- AMOS mappings are `DERIVED` / `AMOS_MODEL` and must not be read as endorsements or runtime implementations.
- `DOCUMENTED != IMPLEMENTED`; `PAPER != DEPLOYED_SYSTEM`.

______________________________________________________________________

**MOC:** [[22_RESEARCH/01_PAPERS/01_PAPERS_MOC|01_PAPERS_MOC]] · [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]] · [[22_RESEARCH/01_PAPERS/ARXIV_BRIDGE_2026_CODING_MULTIMODAL_EMBODIED_QUANTUM_SENSING|ArXiv Bridge 2026]]

**Parent:** [[22_RESEARCH/22_RESEARCH_README|22_RESEARCH_README]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
