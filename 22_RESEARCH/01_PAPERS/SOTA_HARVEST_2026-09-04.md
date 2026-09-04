---
title: SOTA Harvest 2026-09-04 — BCI / AI / Quantum
type: research_note
source: 22_RESEARCH
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_HARVEST
updated: 2026-09-05
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

## 4. 2026-09-05 public web / arXiv snapshot additions

> **Source:** Web search of arXiv 2026 preprints and public pages; epistemic class `SOURCE_CLAIM` / `WEB_SNAPSHOT`; no independent replication or canon promotion performed.

### 4.1 Brain-Computer Interfaces

- **UniBCI** — `arXiv:2605.00061` — unified pretrained model for invasive BCIs (context-conditioned spatio-temporal tokenization, Interval-Area Attention, masked-signal reconstruction). Suggests foundation-model path for `05_COGNITIVE_ORGANISM` invasive-decoder engines.
- **Brain2Qwerty v2** — `arXiv:2608.18114` — non-invasive MEG sentence decoding at 39% WER on 22,000 sentences, best participant <1 word error for half of sentences; data-scaling log-linear improvement.
- **BrainDistill** — `arXiv:2601.17625` — task-specific knowledge distillation for implantable motor decoders with quantization-aware training, targeting power-constrained implants.
- **EEG-VID** — `arXiv:2609.00566` — task-guided latent predictive pretraining; improves cross-day/subject EEG decoding with weak task guidance.
- **EEG-PRIME** — `arXiv:2608.13072` — prototype-aligned instruction-tuned EEG foundation model with multi-level conditioning for cross-dataset BCI decoding.

### 4.2 Neuromorphic & Brain-Inspired AI

- **AIGOR** — `arXiv:2607.03191` — modular event-driven SNN inference architecture, packet-switched spike routing, FPGA-validated on AMD Versal VPK180.
- **SpiNNaker2 chip** — `arXiv:2607.24396` — 152-PE ARM M4F neuromorphic chip; 4.5 TOPS / 2.7 TOPS/W, >150k neurons, >1.8B synaptic events/s at 1ms timestep.
- **HiAER-Spike** — `arXiv:2602.18072` — 160M neuron / 40B synapse event-driven platform at UC San Diego, mouse-brain scale at faster than real time.
- **Reconfigurable hybrid CNN-FC neuromorphic core** — `arXiv:2609.03174` — FPGA SCNN for biomedical edge inference, 88.26% hypoxia classification at 1.455W.
- **Mixed-signal SNN design-space framework** — `arXiv:2607.06456` — PyTorch-compatible mixed-signal SNN exploration with ReRAM/floating-gate synapse models.

### 4.3 Quantum Computing & Quantum-AI

- **Helix trapped-ion fault-tolerant architecture** — `arXiv:2609.03194` — Quantinuum Helios 98-qubit experimental validation; error ~4.6×10⁻⁴ per logical qubit per QEC cycle, Clifford group benchmarked on two logical qubits.
- **NOBOL** — `arXiv:2609.01901` — one Bell-pair logical CNOT for arbitrary CSS codes with logarithmic-depth circuit.
- **Cornucopia codes** — `arXiv:2608.02773` — LDPC family with rate > 1/2 and pseudo-threshold > 0.4%; `[[2844,1426,18]]` block, 12 entangling layers.
- **High-rank encoding for approximate QEC** — `arXiv:2609.00778` — mixed code states can improve entanglement fidelity vs rank-one encoders.
- **Spin-qubit shuttling bus** — `arXiv:2609.02641` — transversal two-qubit logical gates via spin shuttling, ancilla sharing, 15-to-1 magic-state distillation mapping.

## 5. Arvix vault check

- `11_KNOWLEDGE/_arxiv_md/` contains only `2007/` and `2008/` cohorts (legacy AMOS mirror).
- External 66,000-paper corpus resides at `/Users/mac/Desktop/_Arxiv/Arvix` (cohorts 2007–2023, with 2024/2025 only 1 file each); the specific 2026 arXiv IDs above are not yet present in that corpus and are recorded as `WEB_SNAPSHOT`.

## 6. Ingestion status

| Item | Field | State |
|------|-------|-------|
| BCI harvest | 10 items | SOURCE_CLAIM |
| Neuromorphic harvest | 5 items | SOURCE_CLAIM |
| AI harvest | 2 items | SOURCE_CLAIM |
| Quantum harvest | 9 items | SOURCE_CLAIM |
| Independent replication | Not performed | UNKNOWN/GAP |
| AMOS canon promotion | Not performed | UNKNOWN/GAP |

______________________________________________________________________

**Related:** [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]] · [[22_RESEARCH/SOTA_AGENT_TOOLING_REPOS|SOTA_AGENT_TOOLING_REPOS]] · [[11_KNOWLEDGE/_arxiv_md/_arxiv_md_MOC|_arxiv_md_MOC]]

**MOC:** [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
