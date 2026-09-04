---
title: SOTA Harvest 2026-09-04 — BCI / AI / Quantum
type: research_note
source: 22_RESEARCH
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_HARVEST
updated: 2026-09-04
rscf:
  state: SOURCE_CLAIM
  claim_class: AMOS_MODEL
  provenance:
    - web_search
    - arxiv.org
    - nature.com
    - mit.edu
  scope: active__AMOS_OS
tags:
  - sota
  - bci
  - ai
  - quantum
  - 22_research
---

# SOTA Harvest — BCI / AI / Quantum (2026-09-04)

> **Epistemic boundary:** This note records externally sourced claims and paper metadata. Each item is a `SOURCE_CLAIM`, not independently verified, canonical, or empirically confirmed.

______________________________________________________________________

## 1. Brain-Computer Interfaces

### 1.1 Tactile-encoded BCI for supernumerary limb control
- **Source:** `https://www.nature.com/articles/s41467-026-75213-3`
- **Title:** Concurrent control of natural and robotic limbs through a tactile-encoded brain-computer interface
- **Key claim:** A tactile-evoked P300 BCI enables concurrent control of four supernumerary DOFs while natural movement remains unimpaired.
- **AMOS relevance:** Demonstrates multi-effector neuromotor binding; relevant to `15_INTERFACES` and `05_COGNITIVE_ORGANISM` sensorimotor integration contracts.

### 1.2 Synchron endovascular BCI — COMMAND trial results
- **Source:** `https://doi.org/10.1227/neu.0000000000003360_47238`
- **Title:** Results of the Command Trial: An Early Feasibility Study of the Synchron Endovascular Brain-Computer Interface
- **Key claim:** Fully implanted endovascular BCI shows early safety and feasibility signals in six subjects with chronic severe upper-limb paralysis.
- **AMOS relevance:** Regulatory/safety evidence class; relevant to `18_SECURITY` and `19_TESTS` medical-device governance boundaries.

### 1.3 Speech BCI common metric — OVMI
- **Source:** `https://arxiv.org/abs/2609.02887`
- **Title:** A Common Measure of Communication for Speech Brain-Computer Interfaces
- **Key claim:** Open-vocabulary mutual information (OVMI) provides a principled, information-theoretic comparison of heterogeneous speech BCIs.
- **AMOS relevance:** Evaluation metric for `19_TESTS` and `04_VALIDATION`; addresses comparability of different neural-decoder systems.

### 1.4 Bidirectional BCI for walking exoskeleton
- **Source:** `https://www.vis.caltech.edu/documents/34543/Brain_Stimulation_2026.pdf`
- **Title:** Real-time brain-computer interface control of walking exoskeleton with bilateral sensory feedback
- **Key claim:** ECoG-based bidirectional BCI actuates a robotic gait exoskeleton while delivering sensory feedback, achieving high decode correlation (ρ ≈ 0.92).
- **AMOS relevance:** Closed-loop sensorimotor control; bridges `15_INTERFACES` and `04_RUNTIME` real-time control contracts.

### 1.5 Volitional DBS for Parkinson’s disease
- **Source:** `https://www.medrxiv.org/content/10.64898/2026.08.12.26350419v1.full.pdf`
- **Title:** Volitional deep brain stimulation following brain-computer interface training for Parkinson’s disease
- **Key claim:** Patients can self-regulate cortical beta signals via BCI training to govern closed-loop DBS.
- **AMOS relevance:** Human-in-the-loop therapeutic control; relevant to `UBI`, `CONSENTX`, and `03_CONTROL_PLANE` authority gates.

______________________________________________________________________

## 2. Artificial Intelligence

### 2.1 OpenAI GPT-6 Astra
- **Source:** `https://www.theverge.com/ai-artificial-intelligence/989601/openai-gpt-6-astra-release`
- **Title:** OpenAI’s next big AI model has ‘entered the AGI era’
- **Key claim:** GPT-6 Astra is described as a generational leap in cybersecurity, coding, and agentic multi-step workflows, with >100,000 GPU pre-training.
- **AMOS relevance:** Agentic capability escalation; relevant to `06_AGENTS`, `07_SKILLS`, and `03_CONTROL_PLANE` capability-envelope governance.

### 2.2 Frontier model release wave
- **Source:** `https://blog.4sapi.com/blog/gpt-6-astra-claude-gemini-model-comparison`
- **Title:** GPT-6 Astra vs Claude vs Gemini: AI Model War
- **Key claim:** Anthropic Claude Fable 5.1, Meta Muse Spark 1.3, Google Gemini 3.8 Flash, and OpenAI GPT-6 Astra released within 48 hours; pricing spreads >13×.
- **AMOS relevance:** Multi-agent ecosystem economics; relevant to `21_DOMAINS/07_ECON_FINANCE` and `06_AGENTS` market governance.

______________________________________________________________________

## 3. Quantum Computing

### 3.1 MIT dual-purpose qubit
- **Source:** `https://news.mit.edu/2026/new-qubit-architecture-enables-faster-more-accurate-operations-0903`
- **Title:** New qubit architecture enables faster, more accurate operations
- **Key claim:** A dual-purpose qubit with separate data and interaction components may improve speed and error rates for scalable quantum computers.
- **AMOS relevance:** Quantum error-correction substrate; relevant to `02_KERNEL/01_META_LOGIC` and `01_CANON/02_UNIVERSE_CANON/OMEGA_QUANTUM_STACK`.

### 3.2 Dynamic quantum circuits on superconducting qubit–cavity processor
- **Source:** `https://arxiv.org/html/2608.04780`
- **Title:** Demonstrating advantages of dynamic quantum circuits on a hybrid superconducting qubit–cavity processor
- **Key claim:** First dynamic-circuit Shor’s algorithm implementation on superconducting platform; 10-bit Bernstein–Vazirani with 82% average success.
- **AMOS relevance:** Concrete DQC benchmark; relevant to `02_KERNEL` formal verification and `13_MODELS` quantum simulation registries.

### 3.3 Spin-to-polarization mapping in quantum dot-cavity receiver
- **Source:** `https://arxiv.org/abs/2609.03910`
- **Title:** Spin-to-polarization mapping with a coherent quantum dot-cavity receiver
- **Key claim:** Experimental signature of one-to-one mapping between spin state and scattered-photon polarization for deterministic optical gates.
- **AMOS relevance:** Photon-spin interface for quantum communication; relevant to `15_INTERFACES` quantum protocol contracts.

### 3.4 Ultra-precise quantum projective designs in constant depth
- **Source:** `https://arxiv.org/abs/2609.03925`
- **Title:** Ultra-Precise Quantum Projective Designs in Constant Depth
- **Key claim:** Sparse commuting circuit ensemble reproduces low-order Haar moments in relative error with asymptotically optimal logarithmic interaction degree.
- **AMOS relevance:** Random quantum resource construction; relevant to `02_KERNEL` quantum-logic and `22_RESEARCH/01_MATHEMATICS` design theory.

______________________________________________________________________

## 4. Ingestion status

| Item | Field | State |
|------|-------|-------|
| BCI harvest | 5 items | SOURCE_CLAIM |
| AI harvest | 2 items | SOURCE_CLAIM |
| Quantum harvest | 4 items | SOURCE_CLAIM |
| Independent replication | Not performed | UNKNOWN/GAP |
| AMOS canon promotion | Not performed | UNKNOWN/GAP |

______________________________________________________________________

**Related:** [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]] · [[22_RESEARCH/SOTA_AGENT_TOOLING_REPOS|SOTA_AGENT_TOOLING_REPOS]] · [[11_KNOWLEDGE/_arxiv_md/_arxiv_md_MOC|_arxiv_md_MOC]]

**MOC:** [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
