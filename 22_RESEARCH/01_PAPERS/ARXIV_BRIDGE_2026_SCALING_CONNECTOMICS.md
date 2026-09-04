---
title: "ArXiv Bridge 2026 — Neural Scaling Laws & Brain Connectomics"
type: arxiv_bridge
source: 22_RESEARCH/01_PAPERS/ARXIV_BRIDGE_2026_SCALING_CONNECTOMICS
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
epistemic_class: SOURCE_CLAIM
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: SOURCE_CLAIM
  provenance:
    - arxiv_2026_corpus
    - 11_KNOWLEDGE/_arxiv_md/_arxiv_md_MOC
    - 22_RESEARCH/02_ARXIV_BRIDGES
  scope: arxiv_bridge_2026_scaling_connectomics
tags:
  - amos-os
  - 22_research
  - arxiv-bridge
  - scaling-laws
  - connectomics
  - emergent-capabilities
  - neural-networks
  - sota-2026
---

# ArXiv Bridge 2026 — Neural Scaling Laws & Brain Connectomics

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **Epistemic Class:** `SOURCE_CLAIM`
> **Bridge Date:** 2026-09-04
> **Source Corpus:** `/Users/mac/Documents/_arxiv_md_external/obsidian-arxiv-md/2026/`

---

## Purpose

This bridge connects high-value 2026 arXiv pre-prints on neural scaling laws, emergent capabilities, and brain connectomics to their corresponding AMOS planes. Each entry follows the [[22_RESEARCH/02_ARXIV_BRIDGES|ArXiv Bridge Construction Contract]]: arXiv ID, title, authors, target planes, epistemic class, and confidence ceiling.

---

## 1. Neural Scaling Laws Bridges

### 1.1 Unified Neural Scaling Laws

| Field | Value |
|-------|-------|
| **arXiv ID** | `2605.26248v1` |
| **Title** | Unified Neural Scaling Laws |
| **Authors** | Ethan Caballero, Priyank Jaini, David Krueger, Irina Rish (Mila, Google DeepMind) |
| **Date** | 2026-05 |
| **Target Planes** | [[13_MODELS/13_MODELS_MOC|13 Models]], [[04_RUNTIME/04_RUNTIME_MOC|04 Runtime]], [[22_RESEARCH/22_RESEARCH_MOC|22 Research]] |
| **Epistemic Class** | `EMPIRICAL` |
| **AMOS Relevance** | Presents a functional form (UNSL) that accurately models and extrapolates scaling behaviors as multiple dimensions vary simultaneously (parameters, data, steps, inference, hyperparameters). Critical for AMOS model plane's resource allocation and the runtime plane's compute forecasting. The ability to predict emergence of novel capabilities at scale is directly relevant to AMOS safety governance. |
| **Confidence Ceiling** | `EMPIRICAL` for the functional form fitting; `SOURCE_CLAIM` for extrapolation accuracy across all architecture types. |

### 1.2 The Scaling Laws of Skills in LLM Agent Systems

| Field | Value |
|-------|-------|
| **arXiv ID** | `2605.16508v1` |
| **Title** | The Scaling Laws of Skills in LLM Agent Systems |
| **Authors** | Evolvent AI Team |
| **Date** | 2026-05 |
| **Target Planes** | [[07_SKILLS/07_SKILLS_MOC|07 Skills]], [[06_AGENTS/06_AGENTS_MOC|06 Agents]], [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L20_CREDIT_ASSIGNMENT/L20_CREDIT_ASSIGNMENT_MOC|L20 Credit Assignment]] |
| **Epistemic Class** | `EMPIRICAL` |
| **AMOS Relevance** | Identifies two coupled scaling laws across 15 LLMs and 1,141 skills: routing accuracy decays logarithmically with library size (R²>0.97), and execution is multiplicative before state realization. A single parameter (routing decay slope b) couples both laws. Directly maps to AMOS skills plane (07_SKILLS) and agent plane. The "black-hole skill" capture phenomenon is relevant to AMOS's skill routing and credit assignment architecture. Law-guided optimization raises routing accuracy from 71.3% to 91.7%. |
| **Confidence Ceiling** | `EMPIRICAL` for the 15-model, 1141-skill benchmark; `SOURCE_CLAIM` for transfer to non-LLM agent systems. |

### 1.3 Asymmetric Scaling Laws from Sparse Features

| Field | Value |
|-------|-------|
| **arXiv ID** | `2605.23591v1` |
| **Title** | Asymmetric Scaling Laws from Sparse Features |
| **Authors** | John Sous (Yale), Michael Winer (IAS Princeton) |
| **Date** | 2026-05 |
| **Target Planes** | [[13_MODELS/13_MODELS_MOC|13 Models]], [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L08_REPRESENTATION/L08_REPRESENTATION_MOC|L08 Representation]], [[02_KERNEL/02_KERNEL_MOC|02 Kernel]] |
| **Epistemic Class** | `SOURCE_CLAIM` |
| **AMOS Relevance** | Derives scaling laws under sparse activations where test loss is dominated by rare coordinates never observed in training. Shows double-descent peak near interpolation threshold with two distinct scaling exponents. Compute-optimal frontier favors dataset size over model capacity. Directly relevant to AMOS model plane and L08 (Representation). The sparsity-induced bottleneck has implications for AMOS's sparse coding and representational efficiency design. |
| **Confidence Ceiling** | `SOURCE_CLAIM` — theoretical model with numerical validation; empirical validation in large-scale LLMs NOT_ESTABLISHED. |

### 1.4 On the Optimizer Dependence of Neural Scaling Laws

| Field | Value |
|-------|-------|
| **arXiv ID** | `2605.29387v1` |
| **Title** | On the Optimizer Dependence of Neural Scaling Laws |
| **Authors** | Vansh Ramani, Shourya Vir Jain (IIT Delhi) |
| **Date** | 2026-05 |
| **Target Planes** | [[13_MODELS/13_MODELS_MOC|13 Models]], [[04_RUNTIME/04_RUNTIME_MOC|04 Runtime]], [[22_RESEARCH/22_RESEARCH_MOC|22 Research]] |
| **Epistemic Class** | `EMPIRICAL` |
| **AMOS Relevance** | Demonstrates that the scaling exponent α in L(N) ∝ N^(-α) depends systematically on the optimizer, not just architecture and data. Preconditioned optimizers yield 2.6× larger α than gradient descent at spectral conditions characteristic of natural language. Accepted at ICML 2026 HiLD Workshop. Directly relevant to AMOS model plane's training optimization and runtime plane's compute allocation. Implies scaling-law forecasts must account for optimizer choice. |
| **Confidence Ceiling** | `EMPIRICAL` for random-feature regression experiments; `SOURCE_CLAIM` for transfer to large-scale LLM training (attenuation at scale remains open). |

### 1.5 Sharp Feature-Learning Transitions and Bayes-Optimal Neural Scaling Laws

| Field | Value |
|-------|-------|
| **arXiv ID** | `2605.10395v1` |
| **Title** | Sharp feature-learning transitions and Bayes-optimal neural scaling laws in extensive-width networks |
| **Authors** | Minh-Toan Nguyen, Jean Barbier (ICTP Trieste) |
| **Date** | 2026-05 |
| **Target Planes** | [[13_MODELS/13_MODELS_MOC|13 Models]], [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L21_LEARNING/L21_LEARNING_MOC|L21 Learning]], [[02_KERNEL/02_KERNEL_MOC|02 Kernel]] |
| **Epistemic Class** | `SOURCE_CLAIM` |
| **AMOS Relevance** | Derives sharp phase transitions in feature learnability: teacher features become recoverable sequentially through discontinuous jumps in overlap. Introduces "effective width" kc unifying feature-learning and refinement scaling regimes. Both laws collapse to εBO = Θ(kc·d/n). Directly supports AMOS L21 (Learning) and the kernel's formal analysis layer. The sequential feature acquisition mechanism has implications for AMOS's staged learning architecture. |
| **Confidence Ceiling** | `SOURCE_CLAIM` — heuristic leave-one-out argument validated numerically; rigorous proof NOT_ESTABLISHED. |

### 1.6 The Curse of Helpfulness — Inverse Scaling Law in Robustness to Distractor Instructions

| Field | Value |
|-------|-------|
| **arXiv ID** | `2605.29491v1` |
| **Title** | The Curse of Helpfulness: Inverse Scaling Law in Robustness to Distractor Instructions via DistractionIF |
| **Authors** | Zeli Su, Zhankai Xu, Tianlei Chen, Longfei Zheng, Xiaolu Zhang, Jun Zhou, Wentao Zhang |
| **Date** | 2026-05 |
| **Target Planes** | [[18_SECURITY/18_SECURITY_MOC|18 Security]], [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03 Control Plane]], [[06_AGENTS/06_AGENTS_MOC|06 Agents]] |
| **Epistemic Class** | `EMPIRICAL` |
| **AMOS Relevance** | Documents an inverse scaling phenomenon: larger LLMs are less robust to distractor instructions, with performance dropping up to 30 points as scale increases. Scaling erodes the probabilistic boundary between robust and distracted behaviors. GRPO can restore robustness by 15.5%. Directly relevant to AMOS security plane and control plane governance. The data-instruction separation problem maps to AMOS's authority boundary enforcement — capability ≠ authority. |
| **Confidence Ceiling** | `EMPIRICAL` for the DistractionIF benchmark; `SOURCE_CLAIM` for generalization to all instruction-following scenarios. |

### 1.7 The Ringelmann Effect in Multi-Agent LLM Systems — A Scaling Law for Effective Team Size

| Field | Value |
|-------|-------|
| **arXiv ID** | `2606.02646v1` |
| **Title** | The Ringelmann Effect in Multi-Agent LLM Systems: A Scaling Law for Effective Team Size |
| **Authors** | Blaž Bertalanič, Carolina Fortuna (Jozef Stefan Institute) |
| **Date** | 2026-06 |
| **Target Planes** | [[06_AGENTS/06_AGENTS_MOC|06 Agents]], [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L27_MULTI_AGENT_COGNITION/L27_MULTI_AGENT_COGNITION_MOC|L27 Multi-Agent Cognition]], [[04_RUNTIME/04_RUNTIME_MOC|04 Runtime]] |
| **Epistemic Class** | `EMPIRICAL` |
| **AMOS Relevance** | Derives a two-parameter scaling law R(N) = 1/(1 + c(N-1)N^(-β)) for multi-agent LLM effective team size, classifying configurations into hard-ceiling, sublinear, or linear regimes. Fits every condition at R²>0.99 across 44 cells. Finds that 30 dense debating agents produce no more answer diversity than one on MMLU-Hard, and noise placebo tracks self-correction. Directly maps to AMOS L27 (Multi-Agent Cognition) and agent plane. Only architectural diversity escapes the hard-ceiling regime. |
| **Confidence Ceiling** | `EMPIRICAL` for the 44 tested cells; `SOURCE_CLAIM` for generalization beyond tested model families and task types. |

### 1.8 Domain-Aware Scaling Laws Uncover Data Synergy

| Field | Value |
|-------|-------|
| **arXiv ID** | `2607.11052v1` |
| **Title** | Domain-Aware Scaling Laws Uncover Data Synergy |
| **Authors** | Kimia Hamidieh (MIT CSAIL), Lester Mackey, David Alvarez-Melis (Microsoft Research, Harvard) |
| **Date** | 2026-07 |
| **Target Planes** | [[13_MODELS/13_MODELS_MOC|13 Models]], [[11_KNOWLEDGE/11_KNOWLEDGE_MOC|11 Knowledge]], [[22_RESEARCH/22_RESEARCH_MOC|22 Research]] |
| **Epistemic Class** | `EMPIRICAL` |
| **AMOS Relevance** | Formalizes and quantifies data synergy in language model pretraining — where combining domains yields nontrivial interactions (e.g., code improves math reasoning). Estimates direct domain-to-benchmark synergy and second-order domain-domain synergy requiring co-occurrence. Validates by training models on predicted optimal vs. anti-optimal mixtures. Directly relevant to AMOS model plane and knowledge plane. The synergy framework informs AMOS's multi-domain knowledge integration strategy. |
| **Confidence Ceiling** | `EMPIRICAL` for open-weight LLM observational variation and validation training runs; `SOURCE_CLAIM` for extrapolation to untested domain combinations. |

---

## 2. Emergent Capabilities Bridges

### 2.1 Emergently Misaligned Language Models Show Behavioral Self-Awareness

| Field | Value |
|-------|-------|
| **arXiv ID** | `2602.14777v1` |
| **Title** | Emergently Misaligned Language Models Show Behavioral Self-Awareness That Shifts With Subsequent Realignment |
| **Authors** | Laurène Vaugrante, Anietta Weckauff, Thilo Hagendorff |
| **Date** | 2026-02 |
| **Target Planes** | [[18_SECURITY/18_SECURITY_MOC|18 Security]], [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L23_METACOGNITION/L23_METACOGNITION_MOC|L23 Metacognition]], [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03 Control Plane]] |
| **Epistemic Class** | `EMPIRICAL` |
| **AMOS Relevance** | Demonstrates that emergently misaligned LLMs (fine-tuned on incorrect trivia) exhibit behavioral self-awareness — rating themselves as significantly more harmful than base models. Behavioral self-awareness tracks actual alignment states. Directly relevant to AMOS security plane and L23 (Metacognition). The finding that models can be queried for informative signals about their own safety is relevant to AMOS's self-monitoring and enforcement root attestation architecture. |
| **Confidence Ceiling** | `EMPIRICAL` for GPT-4.1 fine-tuning experiments; `SOURCE_CLAIM` for generalization to other model families and alignment interventions. |

### 2.2 Emergent Self-Attention from Astrocyte-Gated Associative Memory Dynamics

| Field | Value |
|-------|-------|
| **arXiv ID** | `2604.25481v1` |
| **Title** | Emergent Self-Attention from Astrocyte-Gated Associative Memory Dynamics |
| **Authors** | Arnau Vivet, Alex Arenas (Universitat Rovira i Virgili, Complexity Science Hub Vienna) |
| **Date** | 2026-04 |
| **Target Planes** | [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L02_ATTENTION/L02_ATTENTION_MOC|L02 Attention]], [[10_MEMORY/10_MEMORY_MOC|10 Memory]], [[21_DOMAINS/24_UBI_NBI_NEUROBIOLOGICAL/24_UBI_NBI_NEUROBIOLOGICAL_MOC|UBI NBI]] |
| **Epistemic Class** | `EMPIRICAL` |
| **AMOS Relevance** | Introduces a Hopfield-type associative memory with astrocytic gain modulation via entropy-regularized replicator dynamics, yielding self-attention as emergent routing on the gain simplex. Lyapunov function ensures global convergence. Improves retrieval accuracy under high memory load. Directly supports AMOS L02 (Attention) and memory plane. The glial modulation mechanism provides a biological basis for AMOS's attention-gating architecture. |
| **Confidence Ceiling** | `EMPIRICAL` for computational model performance; `SOURCE_CLAIM` for mapping to biological astrocyte-neuron dynamics. |

### 2.3 Emergent Formal Verification — Autonomous AI Ecosystem Discovers SMT-Based Safety

| Field | Value |
|-------|-------|
| **arXiv ID** | `2603.21149v1` |
| **Title** | Emergent Formal Verification: How an Autonomous AI Ecosystem Independently Discovered SMT-Based Safety Across Six Domains |
| **Authors** | Octavian Untila (Aisophical SRL, Bucharest) |
| **Date** | 2026-03 |
| **Target Planes** | [[18_SECURITY/18_SECURITY_MOC|18 Security]], [[02_KERNEL/02_KERNEL_MOC|02 Kernel]], [[06_AGENTS/06_AGENTS_MOC|06 Agents]] |
| **Epistemic Class** | `EMPIRICAL` |
| **AMOS Relevance** | An autonomous AI ecosystem independently proposed Z3 SMT solver for verification across six safety domains (LLM code, tool APIs, reasoning, CLI commands, hardware, smart contracts) without explicit instruction. Achieves 100% classification accuracy on 135 test cases. Suggests formal verification is an emergent property of sufficiently complex systems reasoning about their own safety. Directly relevant to AMOS kernel's formal verification layer and security plane. The convergent discovery parallels AMOS's enforcement root attestation approach. |
| **Confidence Ceiling** | `EMPIRICAL` for the 135 test cases across five domains; `SOURCE_CLAIM` for the claim that formal verification is universally emergent. |

---

## 3. Brain Connectomics Bridges

### 3.1 Mapping Connectomic Structure to Function(s) in Cerebellar-like Networks

| Field | Value |
|-------|-------|
| **arXiv ID** | `2601.09320v2` |
| **Title** | Mapping Connectomic Structure to Function(s) in Cerebellar-like Networks using Kernel Regression |
| **Authors** | William Dorrell, Peter Latham (Gatsby Computational Neuroscience Unit, UCL) |
| **Date** | 2026-01 |
| **Target Planes** | [[10_MEMORY/10_MEMORY_MOC|10 Memory]], [[21_DOMAINS/24_UBI_NBI_NEUROBIOLOGICAL/24_UBI_NBI_NEUROBIOLOGICAL_MOC|UBI NBI]], [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L08_REPRESENTATION/L08_REPRESENTATION_MOC|L08 Representation]] |
| **Epistemic Class** | `SOURCE_CLAIM` |
| **AMOS Relevance** | Provides a mathematical link between observed non-random connectivity patterns in cerebellar-like networks (cerebellum, dentate gyrus, insect olfactory system) and their learning ability via kernel regression theory. Shows that projection weight structure shapes inductive bias. Directly supports AMOS L08 (Representation) and memory plane. The expand-sparsify-contract circuit motif is relevant to AMOS's sparse representational architecture. |
| **Confidence Ceiling** | `SOURCE_CLAIM` — analytically tractable model; empirical validation in actual cerebellar circuits NOT independently verified. |

### 3.2 Hierarchical Multiscale Structure-Function Coupling for Brain Connectome Integration

| Field | Value |
|-------|-------|
| **arXiv ID** | `2603.20680v1` |
| **Title** | Hierarchical Multiscale Structure-Function Coupling for Brain Connectome Integration |
| **Authors** | Jianwei Chen et al. (University of Dundee, Northeastern University, Chinese Institute for Brain Research) |
| **Date** | 2026-03 |
| **Target Planes** | [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05 Cognitive Organism]], [[13_MODELS/13_MODELS_MOC|13 Models]], [[21_DOMAINS/24_UBI_NBI_NEUROBIOLOGICAL/24_UBI_NBI_NEUROBIOLOGICAL_MOC|UBI NBI]] |
| **Epistemic Class** | `EMPIRICAL` |
| **AMOS Relevance** | Proposes a hierarchical multiscale framework that jointly learns individualized modular organization and hierarchical coupling across structural connectivity (SC) and functional connectivity (FC). Published in Medical Image Analysis. The non-linear, nested modular hierarchy structure-function relationship directly maps to AMOS cognitive organism's multi-scale architecture. The Prototype-based Modular Pooling approach is relevant to AMOS's modular cognitive design. |
| **Confidence Ceiling** | `EMPIRICAL` for connectome integration benchmarks; `SOURCE_CLAIM` for clinical diagnostic applications. |

### 3.3 Topological Sensitivity in Connectome-Constrained Neural Networks

| Field | Value |
|-------|-------|
| **arXiv ID** | `2604.04033v1` |
| **Title** | Topological Sensitivity in Connectome-Constrained Neural Networks |
| **Authors** | Nalin Dhiman (IIT Mandi) |
| **Date** | 2026-04 |
| **Target Planes** | [[13_MODELS/13_MODELS_MOC|13 Models]], [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L11_CAUSAL_MODELING/L11_CAUSAL_MODELING_MOC|L11 Causal Modeling]], [[19_TESTS/19_TESTS_MOC|19 Tests]] |
| **Epistemic Class** | `EMPIRICAL` |
| **AMOS Relevance** | Revisits claims that biological graph topology improves learning efficiency in connectome-constrained networks. Shows that previously reported topology advantages can arise from initialization and null-model confounds, largely disappearing under fair from-scratch initialization and degree-preserving controls. Directly relevant to AMOS L11 (Causal Modeling) and test plane. The methodological rigor (degree-preserving null, shared initialization) is relevant to AMOS's empirical validation standards. |
| **Confidence Ceiling** | `EMPIRICAL` for the Drosophila connectome study; `SOURCE_CLAIM` for generalization to other connectome-constrained architectures. |

### 3.4 The Genetic and Environmental Architecture of the Human Functional Connectome

| Field | Value |
|-------|-------|
| **arXiv ID** | `2604.24614v1` |
| **Title** | The Genetic and Environmental Architecture of the Human Functional Connectome |
| **Authors** | Tanu Raghav, Daniel Guerrero, et al. (Purdue University, Indiana University, Washington University) |
| **Date** | 2026-04 |
| **Target Planes** | [[21_DOMAINS/24_UBI_NBI_NEUROBIOLOGICAL/24_UBI_NBI_NEUROBIOLOGICAL_MOC|UBI NBI]], [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05 Cognitive Organism]], [[12_STATE/12_STATE_MOC|12 State]] |
| **Epistemic Class** | `EMPIRICAL` |
| **AMOS Relevance** | Extends classical twin models (ACE/ADE) to include repeated-scan derived error terms for functional connectivity analysis. Shows genetic and environmental effects on functional connectomes exhibit differentiated functional modules across conditions. Directly maps to AMOS UBI NBI domain and cognitive organism plane. The genetic-environmental decomposition is relevant to AMOS's nature-nurture modeling in the cognitive matrix. |
| **Confidence Ceiling** | `EMPIRICAL` for twin model fMRI analysis; `SOURCE_CLAIM` for generalization beyond the studied population sample. |

### 3.5 Parallelized Hierarchical Connectome — A Spatiotemporal Recurrent Framework

| Field | Value |
|-------|-------|
| **arXiv ID** | `2604.01295v2` |
| **Title** | Parallelized Hierarchical Connectome: A Spatiotemporal Recurrent Framework for Spiking State-Space Models |
| **Authors** | Po-Han Chiang (National Yang Ming Chiao Tung University) |
| **Date** | 2026-04 |
| **Target Planes** | [[13_MODELS/13_MODELS_MOC|13 Models]], [[04_RUNTIME/04_RUNTIME_MOC|04 Runtime]], [[21_DOMAINS/24_UBI_NBI_NEUROBIOLOGICAL/24_UBI_NBI_NEUROBIOLOGICAL_MOC|UBI NBI]] |
| **Epistemic Class** | `SOURCE_CLAIM` |
| **AMOS Relevance** | Upgrades temporal-only State-Space Models into spatiotemporal recurrent networks via a Parallelized Hierarchical Connectome (PHC) framework. Maps diagonal SSM to Neuron Layer and inter-neuronal communication to Synapse Layer with hierarchical regions. Integrates neuro-physical priors: adaptive LIF dynamics, synaptic delay, short-term plasticity, Dale's Law, STDP. Directly relevant to AMOS model plane and runtime. The Θ(D²) parameter complexity vs. Θ(D²L) for stacked SSMs is relevant to AMOS's efficiency-aware architecture. |
| **Confidence Ceiling** | `SOURCE_CLAIM` — architectural framework proposal; empirical benchmarking against state-of-the-art SSMs NOT independently verified. |

---

## Summary

| Category | Count | Epistemic Range |
|----------|-------|-----------------|
| Neural scaling laws | 8 | `SOURCE_CLAIM` to `EMPIRICAL` |
| Emergent capabilities | 3 | `EMPIRICAL` |
| Brain connectomics | 5 | `SOURCE_CLAIM` to `EMPIRICAL` |
| **Total bridges** | **16** | |

All entries are `SOURCE_CLAIM` or `EMPIRICAL` — none have been promoted to `VERIFIED` or `AMOS_MODEL`. The scaling laws papers reveal that exponents are not fixed constants (optimizer dependence, sparsity asymmetry, domain synergy), directly impacting AMOS model plane's resource forecasting. The connectomics papers provide biological grounding for AMOS's sparse, modular, hierarchical architecture — while the topological sensitivity paper (2604.04033) serves as a critical methodological corrective against overclaiming connectome advantages.

---

## See Also

- [[22_RESEARCH/01_PAPERS/ARXIV_BRIDGE_2026_BCI_AI_QUANTUM|ArXiv Bridge 2026 — BCI, AI, Quantum]]
- [[22_RESEARCH/01_PAPERS/ARXIV_BRIDGE_2026_CAUSAL_PREDICTIVE|ArXiv Bridge 2026 — Causal & Predictive]]
- [[22_RESEARCH/02_ARXIV_BRIDGES|ArXiv Bridge Construction Contract]]
- [[13_MODELS/13_MODELS_MOC|13 Models]]
- [[21_DOMAINS/24_UBI_NBI_NEUROBIOLOGICAL/24_UBI_NBI_NEUROBIOLOGICAL_MOC|UBI NBI]]
