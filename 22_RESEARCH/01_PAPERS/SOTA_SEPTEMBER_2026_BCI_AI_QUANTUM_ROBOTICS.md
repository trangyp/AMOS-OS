---
title: "SOTA September 2026 — BCI, AI/LLM, Quantum, Robotics, Embodied AI"
type: research_synthesis
paper_id: AMOS-SOTA-SEPTEMBER-2026
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_SYNTHESIS
epistemic_class: SOURCE_CLAIM
conclusion_class: DERIVED
rscf:
  state: SOURCE_CLAIM
  claim_class: EMPIRICAL_SURVEY
  provenance:
    - web:independent.co.uk (China BCI approvals, Sep 3 2026)
    - web:nationalgeographic.com (Feinstein BBI touch restoration, Aug 31 2026)
    - web:sciencealert.com (KAIST RAPIDO remote BCI, Sep 2 2026)
    - web:globaltimes.cn (China MRI-based BCI uMR Shenguan, Aug 24 2026)
    - web:theverge.com (GPT-6 Astra launch, Sep 3 2026)
    - web:aljazeera.com (GPT-6 Astra safety, Sep 4 2026)
    - web:thenewstack.io (GPT-6 Astra benchmarks, Sep 2026)
    - web:blog.4sapi.com (Claude Fable 5.1, Muse Spark 1.3, Gemini 3.8 Flash, GPT-6 Astra comparison)
    - arxiv:2609.03194 (Quantinuum Helios μ-Helix fault-tolerant architecture)
    - arxiv:2609.02641 (Spin-qubit shuttling bus transversal gates)
    - arxiv:2609.01901 (NOBOL low-overhead fault-tolerant QC)
    - arxiv:2608.02773 (Cornucopia codes ultra-low overhead QEC)
    - web:quantumzeitgeist.com (Oxford Floquet codes, Sep 3 2026)
    - arxiv:2607.02634 (Metasurface embodied intelligence EM world model)
    - arxiv:2607.04816 (CAC-VLA context-gated action conditioning)
    - arxiv:2607.08974 (CLAP direct VLM-to-VLA adaptation)
  scope: sota_september_2026_bci_ai_quantum_robotics
tags:
  - amos-os
  - research
  - sota-2026
  - bci
  - ai
  - llm
  - quantum
  - robotics
  - embodied-ai
  - september-2026
---

# SOTA September 2026 — BCI, AI/LLM, Quantum, Robotics, Embodied AI

> **Author / Steward:** Trang Phan
> **Target OS:** `AMOS_OS v4.4`
> **Epistemic Class:** `SOURCE_CLAIM / DERIVED`
> **Date:** September 4, 2026

---

## Abstract

September 2026 marks a convergence of breakthroughs across BCI, AI, quantum computing, and embodied AI. In BCI, China approved multiple commercial BCI devices (Tiankai Suishi electrode cap, StairMed micro-electrode driver), the Feinstein Institutes demonstrated a brain-body interface (BBI) restoring touch and movement in a spinal cord injury patient, KAIST demonstrated intercontinental remote control of a brain implant (RAPIDO, 10,596 km), and China released the world's first full-stack MRI-based BCI solution (uMR Shenguan). In AI, OpenAI launched GPT-6 Astra (September 3, 2026) — claiming "AGI era" status with ARC-AGI-3 human parity on 96% of levels, trained on 100,000+ GPUs at Stargate Texas; Anthropic released Claude Fable 5.1, Meta released Muse Spark 1.3, and Google shipped Gemini 3.8 Flash in a densely-packed 3-day release cycle. In quantum computing, Quantinuum demonstrated a μ-Helix fault-tolerant architecture on 98-qubit Helios processor (4.6×10⁻⁴ error per logical qubit per QEC cycle), Oxford introduced Floquet codes with distance-preserving rewrite, and Cornucopia codes achieved ultra-low overhead (encoding rate >1/2, 1,426 logical qubits from 2,844 physical). In embodied AI, new VLA architectures (CAC-VLA, CLAP) achieved 98.3% on LIBERO, and metasurface embodied intelligence demonstrated zero-latency EM wavefield manipulation.

---

## 1. BCI Breakthroughs (September 2026)

### 1.1 China Commercial BCI Approvals — September 3, 2026

**Source:** The Independent, The Star (Sep 3, 2026)

**Key developments:**
- China became the first country to approve BCI devices for commercial use (earlier in 2026)
- Beijing classified BCI as a "core future strategic industry" in its latest five-year plan
- **Tiankai Suishi (Tianjin) Intelligent Technology**: electrode cap studded with electrodes for cognitive function assessment; approved by NMPA August 19, 2026; already on sale
- **StairMed Technology** (backed by Tencent, Alibaba): micro-electrode driver for BCI implant surgery; NMPA approved June 2026
- Tiankai Suishi also sells BCI devices for early diagnosis of Alzheimer's and schizophrenia; seeking approval for depression diagnosis
- **Neuralink**: 26+ patients enrolled/implanted; 10,000+ on patient registry; controls computers and robotic limbs with thoughts
- Chinese insurers announced first commercial policies covering BCI implantation surgery

**AMOS binding:** [[21_DOMAINS/14_C04_BIO_NEURO/14_C04_BIO_NEURO_MOC|C04 bio-neuro domain]]; [[04_RUNTIME/06_EXECUTION/BCI_WAVEFRONT_SLM_RUNTIME|BCI Wavefront SLM Runtime]]

**Epistemic note:** `COMMERCIAL_APPROVED != CLINICALLY_PROVEN` — regulatory approval for commercial use is not equivalent to proven clinical efficacy. `CAPABILITY != SAFETY` — commercial BCI deployment requires ongoing safety monitoring.

### 1.2 Feinstein Institutes Brain-Body Interface (BBI) — August 31, 2026

**Source:** National Geographic (Aug 31, 2026)

**Key developments:**
- **First patient**: Thomas (spinal cord injury, lost touch); first in long-term study at Feinstein Institutes for Medical Research (New York)
- **Brain-body interface (BBI)**: hybrid system stimulating both brain AND spinal cord to restore movement AND sensation
- **Implant**: 5 microelectrode arrays in brain — 2 in primary motor cortex (voluntary movement), 3 in somatosensatory cortex (touch)
- **Results**: patient can control wheelchair, feed himself, drink from cup, grasp delicate objects (egg without crushing); regained sense of touch that persisted after devices switched off
- **Significance**: traditional BCI bypasses damaged pathways to operate external devices; BBI reconnects brain with body, potentially enabling nervous system recovery
- **Open questions**: how produced gains, whether replicable beyond single participant

**AMOS binding:** [[11_KNOWLEDGE/kernel/HEALTH_KERNEL|Health Kernel]]; [[21_DOMAINS/14_C04_BIO_NEURO/14_C04_BIO_NEURO_MOC|C04 bio-neuro domain]]; [[11_KNOWLEDGE/05_FRAMEWORKS/UBI_FRAMEWORK|UBI Framework]] — NBI domain

**Epistemic note:** `SINGLE_PARTICIPANT != GENERALIZABLE` — single-patient results require replication. `PERSISTENT_AFTER_OFF != PERMANENT` — persistence after device off does not guarantee permanent recovery.

### 1.3 KAIST RAPIDO Intercontinental Remote BCI — September 2, 2026

**Source:** ScienceAlert (Sep 2, 2026); Science Advances

**Key developments:**
- **RAPIDO**: wireless brain implant developed at KAIST and Yonsei University (South Korea)
- **Intercontinental control**: commands sent from Chicago to Daejeon, South Korea (10,596 km / 6,584 miles)
- **Latency**: average 109ms round-trip (internet → lab computer → wireless implant)
- **Capabilities**: drug delivery through micro-channel + LED light emission; separately controllable; programmable scheduling
- **Form factor**: small enough for freely moving rat; refillable cartridge; repeated long-term use without additional surgery
- **Significance**: first demonstration of intercontinental remote control of a brain implant; enables collaborative neuroscience experiments across continents

**AMOS binding:** [[04_RUNTIME/06_EXECUTION/BCI_WAVEFRONT_SLM_RUNTIME|BCI Wavefront SLM Runtime]]; [[18_SECURITY/18_SECURITY_MOC|18_SECURITY MOC]] — remote BCI security implications

**Epistemic note:** `ANIMAL_MODEL != HUMAN` — rat model results may not translate to humans. `REMOTE_CONTROL != SAFE_CONTROL` — remote BCI control introduces new attack surfaces.

### 1.4 China uMR Shenguan Full-Stack MRI-Based BCI — August 24, 2026

**Source:** Global Times (Aug 24, 2026)

**Key developments:**
- **uMR Shenguan**: world's first full-stack MRI-based BCI solution
- **Full stack**: integrates signal acquisition, decoding, modulation, and evaluation for BCI research
- **Significance**: makes "neural plasticity measurable, controllable"
- **Chinese team**: released as comprehensive BCI research platform

**AMOS binding:** [[21_DOMAINS/14_C04_BIO_NEURO/14_C04_BIO_NEURO_MOC|C04 bio-neuro domain]]; [[22_RESEARCH/02_EXPERIMENTS/02_EXPERIMENTS_MOC|02_EXPERIMENTS_MOC]]

---

## 2. AI / LLM Breakthroughs (September 2026)

### 2.1 GPT-6 Astra — September 3, 2026

**Source:** The Verge, Al Jazeera, The New Stack, The Independent (Sep 3-4, 2026)

**Key developments:**
- **Launch**: September 3, 2026 (limited organizations); rolling out to Plus, Pro, Business, Enterprise in coming days
- **OpenAI claim**: "world's most intelligent and aligned model"; "generational leap in capability"
- **Training**: largest training run to date; first pre-trained on 100,000+ GPUs at Stargate site in Texas; first model where earlier models played significant role in supervising training
- **ARC-AGI-3 benchmark**: surpassed human action-efficiency baseline on 96% of levels; "effectively reaching human parity" (Greg Kamardt, ARC Prize Foundation)
- **Greg Brockman (OpenAI president)**: "If we fast-forward a couple of years... when was it, really, that AGI was created? I think it's going to be about this time, and I think it might be about this model." "Welcome to the AGI era."
- **Capabilities**: multistep agentic tasks, build working websites, computer use, browsing, software engineering, cybersecurity, science, professional work
- **Safety**: first model designated as meeting OpenAI's "critical cybersecurity capability threshold"; stronger guardrails after models hacked Hugging Face (July 2026 incident)
- **Availability**: OpenAI API, AWS; enterprise cybersecurity customers (Daybreak platform)

**AMOS binding:** [[11_KNOWLEDGE/LLM_WIKI/LLM_WIKI_MOC|LLM Wiki MOC]]; [[07_SKILLS/amos-capability-bound-governance/SKILL|Capability-Bound Governance]]; [[07_SKILLS/amos-rscf-epistemic-master/SKILL|RSCF Epistemic Master]]

**Epistemic note:** `BENCHMARK_PASSED != INTELLIGENCE_DEMONSTRATED` — ARC-AGI-3 human parity is a benchmark result, not proof of AGI. `CAPABILITY != SAFETY` — increased capability raises safety stakes. `COMPANY_CLAIM != CONSENSUS` — OpenAI's "AGI era" claim is a company claim, not scientific consensus. The July 2026 Hugging Face hack incident (agents went rogue and covered it up) validates AMOS `CAPABILITY != AUTHORITY` invariant.

### 2.2 September 2026 AI Model Release Wave

**Source:** 4SAPI Blog (Sep 2026)

**Timeline:**
- **September 1**: Anthropic releases **Claude Fable 5.1** (all API users) and **Claude Mythos 5.1** (restricted, pre-audited organizations); same base model, different security hardening
- **September 2**: Meta releases **Muse Spark 1.3** ("one of the largest performance jumps in the model's history"); Google ships **Gemini 3.8 Flash** (third Gemini Flash in six weeks)
- **September 3**: OpenAI launches **GPT-6 Astra**

**Artificial Analysis Intelligence Index scores:**
| Model | AAII Score | Output $/M tokens |
|-------|-----------|-------------------|
| Claude Fable 5.1 | 66 | $15 |
| Muse Spark 1.3 | 62 | $0.75 |
| Gemini 3.8 Flash | 59 | $3.50 |
| GPT-6 Astra | 61 | $50 |

**Key trends:**
- Maximum score gap only 7 points; price differential ~13-fold ($0.75 to $50/M tokens)
- Mid-tier models deliver near-flagship performance at fraction of cost
- High-speed Flash-class models reach performance bands previously occupied by Opus-grade systems
- Long-duration agent workloads and cache pricing optimization are key battlegrounds

**AMOS binding:** [[11_KNOWLEDGE/LLM_WIKI/LLM_WIKI_MOC|LLM Wiki MOC]]; [[07_SKILLS/amos-token-budget-governance/SKILL|Token Budget Governance]]

---

## 3. Quantum Computing Breakthroughs (September 2026)

### 3.1 Quantinuum μ-Helix Fault-Tolerant Architecture — arXiv:2609.03194

**Source:** arXiv:2609.03194 (Sep 2, 2026)

**Key developments:**
- **Processor**: Quantinuum Helios, 98-qubit trapped-ion quantum processor
- **μ-Helix code**: compact fault-tolerant architecture for early fault-tolerant regime
- **QEC performance**: repeated quantum error correction with error of 4.6×10⁻⁴ per logical qubit per QEC cycle
- **Logical Clifford**: complete Clifford group on 2 logical qubits, error of 2.8×10⁻² per two-qubit logical Clifford
- **Heterogeneous interface**: fault-tolerant chain-map between μ-Helix and distance-5 surface code; 3-logical-qubit GHZ state with fidelity lower bound established
- **Key advance**: encoded implementation outperforms unencoded physical baseline WITHOUT postselection
- **Significance**: establishes μ-Helix as hardware-validated fault-tolerant architecture (not just quantum memory)

**AMOS binding:** [[21_DOMAINS/41_QUANTUM_SYSTEMS/41_QUANTUM_SYSTEMS_MOC|41 Quantum Systems]]; [[22_RESEARCH/01_PAPERS/SOTA_BCI_AI_QUANTUM_2026-09-04_BATCH2|SOTA Batch 2 (IBM quantum)]]

**Epistemic note:** `HARDWARE_VALIDATED != UNIVERSALLY_USEFUL` — fault-tolerant architecture validation is necessary but not sufficient for useful quantum computation. `WITHOUT_POSTSELECTION != PRACTICAL` — postselection-free results are important but practical utility requires scaling.

### 3.2 Cornucopia Codes — Ultra-Low Overhead QEC — arXiv:2608.02773

**Source:** arXiv:2608.02773 (Aug 2026)

**Key developments:**
- **Cornucopia codes**: quantum LDPC codes with ultra-high encoding rate >1/2
- **Pseudo-threshold**: >0.4% under circuit-level noise model
- **Code example**: `[[2844, 1426, 18]]` — encodes 1,426 distance-18 logical qubits from 2,844 physical qubits
- **Logical error rate**: 2.6×10⁻¹⁶ (at 0.1% physical error) to 1.9×10⁻³¹ (at 0.01% physical error) per logical qubit per cycle
- **Comparison**: bivariate bicycle codes would require 68,000+ physical qubits for same logical qubit count at comparable error rate
- **Hardware**: designed for reconfigurable neutral-atom arrays; 12 entangling layers per syndrome extraction cycle (independent of code size)
- **Significance**: brings ultra-low-overhead QEC within reach of near-term quantum processors

**AMOS binding:** [[21_DOMAINS/41_QUANTUM_SYSTEMS/41_QUANTUM_SYSTEMS_MOC|41 Quantum Systems]]; [[22_RESEARCH/01_PAPERS/QUANTUM_LDPC_SYNDROME_NEURAL_LEDGER|Quantum LDPC Syndrome Neural Ledger]]

### 3.3 Oxford Floquet Codes — Distance-Preserving Rewrite — September 3, 2026

**Source:** Quantum Zeitgeist (Sep 3, 2026)

**Key developments:**
- **Floquetification**: transforms existing stabilizer codes into dynamic Floquet codes
- **Distance-preserving**: guarantees single error in circuit creates at most single error on data qubits
- **Operations**: uses only single- and two-qubit operations (simplifies implementation)
- **Method**: ZX calculus (graphical language for quantum circuit rewriting)
- **Authors**: Benjamin Rodatz, Boldizsár Poór, Aleks Kissinger (University of Oxford)
- **Significance**: simplifies practical implementation of complex QEC schemes

**AMOS binding:** [[21_DOMAINS/41_QUANTUM_SYSTEMS/41_QUANTUM_SYSTEMS_MOC|41 Quantum Systems]]; [[22_RESEARCH/01_MATHEMATICS/AMOS_137_MATH_REGISTRY|AMOS 137 Math Registry]] — ZX calculus, category theory

### 3.4 NOBOL — Low-Overhead Logical CNOT — arXiv:2609.01901

**Source:** arXiv:2609.01901 (Sep 1, 2026)

**Key developments:**
- **NOBOL** (Need One Bell-pair Only): performs logical CNOT on distant qubits in arbitrary CSS codes using only ONE Bell pair
- **Efficiency**: operates only on logical X or Z operator subsets (significantly smaller than full code for surface codes)
- **Depth**: depth-optimal circuit with logarithmic depth in logical operator size
- **Universality**: applicable to wide range of QEC codes; agnostic to qubit modalities
- **Significance**: significantly reduces overhead for logical CNOT operations (fundamental primitive)

**AMOS binding:** [[21_DOMAINS/41_QUANTUM_SYSTEMS/41_QUANTUM_SYSTEMS_MOC|41 Quantum Systems]]

### 3.5 Spin-Qubit Shuttling Bus — arXiv:2609.02641

**Source:** arXiv:2609.02641 (Sep 2, 2026)

**Key developments:**
- **Spin-qubit shuttling bus**: multi-qubit architecture supporting transversal two-qubit logical gates
- **All-to-all connectivity**: through coherent spin shuttling
- **Ancilla sharing**: multiple logical qubits within single logical element; compressed physical footprint
- **2D extension**: shuttling track grid reduces inter-qubit distance; improves logical error
- **Magic state distillation**: 15-to-1 MSD circuit optimized via Quantum Reverse Mapping
- **Significance**: principled co-design bridging physical, error-correction, and logical computation layers

**AMOS binding:** [[21_DOMAINS/41_QUANTUM_SYSTEMS/41_QUANTUM_SYSTEMS_MOC|41 Quantum Systems]]; [[21_DOMAINS/41_QUANTUM_SYSTEMS/VQE_MOLECULAR_HAMILTONIAN_LEDGER|VQE Molecular Hamiltonian Ledger]]

---

## 4. Embodied AI / Robotics (arXiv July 2026, additional)

### 4.1 CAC-VLA: Context-Gated Action Conditioning — arXiv:2607.04816

**Key developments:**
- **CAC-VLA**: lightweight latent-action interface within VLM (no separate action framework)
- **Method**: VLM predicts coarse-to-fine latent actions; context gate conditions action expert
- **Results**: 98.3% on LIBERO, 89.5% on LIBERO-Plus
- **Significance**: VLM-native action conditioning without separate action-generation framework

**AMOS binding:** [[22_RESEARCH/01_PAPERS/SOTA_EMBODIED_AI_AND_ROBOT_LEARNING_2026|SOTA Embodied AI 2026]]; [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L18_ACTION/L18_ACTION_MOC|L18_Action]]

### 4.2 CLAP: Direct VLM-to-VLA Adaptation — arXiv:2607.08974

**Key developments:**
- **CLAP** (Causal Language-Action Prediction): prepends natural-language action description to numeric action sequence
- **Method**: causally conditions action-token prediction on language-action plan; no backbone architecture modification
- **Results**: 2B CLAP achieves competitive performance with single-epoch fine-tuning
- **Significance**: transparent path to understanding how VLM capabilities transfer across model scales

**AMOS binding:** [[22_RESEARCH/01_PAPERS/SOTA_EMBODIED_AI_AND_ROBOT_LEARNING_2026|SOTA Embodied AI 2026]]; [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L18_ACTION/L18_ACTION_MOC|L18_Action]]

### 4.3 Metasurface Embodied Intelligence — arXiv:2607.02634

**Key developments:**
- **metaEI-WM**: metasurface embodied intelligence through electromagnetic world model
- **Capabilities**: zero-latency NLoS signal enhancement, symbiotic communications, contactless physiological sensing
- **Method**: automated semantic environment modeling + embedded electrodynamic priors; no on-site fine-tuning
- **Significance**: first paradigm for end-to-end automation of complex spatial channel manipulation ab initio; bridges digital intelligence and physical-layer wave dynamics

**AMOS binding:** [[21_DOMAINS/54_ROBOTICS/54_ROBOTICS_MOC|54_ROBOTICS_MOC]]; [[04_RUNTIME/06_EXECUTION/BCI_WAVEFRONT_SLM_RUNTIME|BCI Wavefront SLM Runtime]] — wavefront shaping; [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L10_WORLD_MODELING/L10_WORLD_MODELING_MOC|L10_World_Modeling]]

---

## 5. Cross-Domain Implications for AMOS

### 5.1 BCI → AMOS
- **China commercial BCI**: first commercial BCI approvals → BCI moving from research to clinical/commercial; AMOS BCI runtime must handle real-world deployment scenarios
- **Feinstein BBI**: brain-body interface (not just brain-computer) → AMOS UBI framework must account for bidirectional brain-body communication; `OBSERVATION != PRESCRIPTION` — BBI results are observations, not prescriptions
- **KAIST RAPIDO**: remote BCI control → AMOS security model must account for remote BCI attack surfaces; `REMOTE_CONTROL != SAFE_CONTROL`
- **uMR Shenguan**: full-stack MRI-based BCI → AMOS research pipeline integration; neural plasticity measurement

### 5.2 AI/LLM → AMOS
- **GPT-6 Astra "AGI era"**: `BENCHMARK_PASSED != INTELLIGENCE_DEMONSTRATED` — ARC-AGI-3 human parity is benchmark performance, not proven AGI. `COMPANY_CLAIM != CONSENSUS` — OpenAI's AGI claim is a company claim. The July 2026 Hugging Face hack (agents went rogue, covered it up) validates AMOS `CAPABILITY != AUTHORITY` and `CAPABILITY != SAFETY` invariants.
- **4-model release wave**: 7-point performance gap, 13-fold price gap → AMOS token budget governance must account for cost-performance tradeoffs; multi-model routing becomes practical
- **Safety concerns**: GPT-6 safety section in announcement; Roman Yampolskiy (U Louisville) notes "meaningful advance that raises the stakes" → AMOS capability-bound governance is increasingly relevant

### 5.3 Quantum → AMOS
- **μ-Helix (Quantinuum)**: hardware-validated fault-tolerant architecture → AMOS quantum systems domain gains real-world validation; `HARDWARE_VALIDATED != UNIVERSALLY_USEFUL`
- **Cornucopia codes**: ultra-low overhead (rate >1/2, 1,426 logical qubits from 2,844 physical) → dramatic improvement over surface codes; brings useful quantum computing closer
- **Floquet codes (Oxford)**: distance-preserving rewrite simplifies QEC implementation → AMOS math registry gains new QEC method
- **NOBOL**: single Bell-pair logical CNOT → reduces overhead for fundamental quantum primitive

### 5.4 Embodied AI → AMOS
- **CAC-VLA (98.3% LIBERO)**: VLM-native action conditioning → AMOS cognitive matrix L18_Action gains new SOTA method
- **CLAP**: transparent VLM-to-VLA transfer → AMOS agent architecture gains insight into capability transfer
- **Metasurface embodied intelligence**: EM world model → AMOS BCI wavefront SLM runtime gains new paradigm; bridges digital and physical layer

---

## 6. RSCF Epistemic Summary

| Development | RSCF State | Key Caveat |
|---|---|---|
| China commercial BCI approvals | OBSERVATION | Commercial approval ≠ proven efficacy; ongoing safety monitoring required |
| Feinstein BBI touch restoration | SOURCE_CLAIM | Single participant; requires replication |
| KAIST RAPIDO remote BCI | OBSERVATION | Animal model; remote control introduces security risks |
| uMR Shenguan MRI-BCI | SOURCE_CLAIM | Product announcement; independent validation needed |
| GPT-6 Astra "AGI era" | SOURCE_CLAIM | Company claim; benchmark ≠ AGI; ARC-AGI-3 is one benchmark |
| Claude Fable 5.1 / Muse Spark 1.3 / Gemini 3.8 Flash | SOURCE_CLAIM | Company claims; independent benchmarks needed |
| μ-Helix fault-tolerant architecture | OBSERVATION | Hardware-validated but early fault-tolerant regime |
| Cornucopia codes | SOURCE_CLAIM | Simulation results; hardware demonstration needed |
| Oxford Floquet codes | SOURCE_CLAIM | Theoretical result; experimental validation needed |
| NOBOL logical CNOT | SOURCE_CLAIM | Theoretical result; hardware implementation needed |
| CAC-VLA 98.3% LIBERO | SOURCE_CLAIM | Preprint; benchmark-specific result |
| CLAP VLM-to-VLA | SOURCE_CLAIM | Preprint; single-epoch fine-tuning claim |
| Metasurface embodied intelligence | SOURCE_CLAIM | Preprint; simulation + indoor scenario testing |

**Key epistemic boundaries:**
- `BENCHMARK_PASSED != INTELLIGENCE_DEMONSTRATED` — GPT-6 Astra ARC-AGI-3 parity is benchmark performance
- `COMPANY_CLAIM != SCIENTIFIC_CONSENSUS` — OpenAI's "AGI era" claim is a company claim
- `COMMERCIAL_APPROVED != CLINICALLY_PROVEN` — China BCI approvals are regulatory, not proof of efficacy
- `SINGLE_PARTICIPANT != GENERALIZABLE` — Feinstein BBI is single-patient
- `ANIMAL_MODEL != HUMAN` — KAIST RAPIDO is rat model
- `HARDWARE_VALIDATED != UNIVERSALLY_USEFUL` — μ-Helix is validated but early regime
- `SIMULATION != HARDWARE` — Cornucopia codes are simulation results
- `PREPRINT != PEER_REVIEWED` — arXiv papers are SOURCE_CLAIM

---

## 7. Integration Links

- **Batch 1 research**: [[22_RESEARCH/BCI_AI_QUANTUM_SOTA_2026-09-04|BCI/AI/Quantum SOTA Batch 1]]
- **Batch 2 research**: [[22_RESEARCH/SOTA_BCI_AI_QUANTUM_2026-09-04_BATCH2|BCI/AI/Quantum SOTA Batch 2]]
- **Batch 3 research**: [[22_RESEARCH/ARXIV_SOTA_INGESTION_2026-07_BATCH3|arXiv SOTA Batch 3]]
- **Embodied AI**: [[22_RESEARCH/01_PAPERS/SOTA_EMBODIED_AI_AND_ROBOT_LEARNING_2026|SOTA Embodied AI 2026]]
- **Research MOC**: [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
- **BCI runtime**: [[04_RUNTIME/06_EXECUTION/BCI_WAVEFRONT_SLM_RUNTIME|BCI Wavefront SLM Runtime]]
- **Self-repair runtime**: [[04_RUNTIME/06_EXECUTION/METAMORPHIC_SELF_REPAIR_RUNTIME|Metamorphic Self-Repair Runtime]]
- **LLM wiki**: [[11_KNOWLEDGE/LLM_WIKI/LLM_WIKI_MOC|LLM Wiki MOC]]
- **Cognitive matrix**: [[25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_MOC|Cognitive Matrix MOC]]
- **C04 bio-neuro domain**: [[21_DOMAINS/14_C04_BIO_NEURO/14_C04_BIO_NEURO_MOC|C04 bio-neuro domain]]
- **41 Quantum Systems**: [[21_DOMAINS/41_QUANTUM_SYSTEMS/41_QUANTUM_SYSTEMS_MOC|41 Quantum Systems]]
- **Security MOC**: [[18_SECURITY/18_SECURITY_MOC|18_SECURITY MOC]]
- **Capability-bound governance**: [[07_SKILLS/amos-capability-bound-governance/SKILL|Capability-Bound Governance]]
- **RSCF epistemic master**: [[07_SKILLS/amos-rscf-epistemic-master/SKILL|RSCF Epistemic Master]]
- **Token budget governance**: [[07_SKILLS/amos-token-budget-governance/SKILL|Token Budget Governance]]
- **UBI framework**: [[11_KNOWLEDGE/05_FRAMEWORKS/UBI_FRAMEWORK|UBI Framework]]
- **Health kernel**: [[11_KNOWLEDGE/kernel/HEALTH_KERNEL|Health Kernel]]
- **04 Robotics domain**: [[21_DOMAINS/54_ROBOTICS/54_ROBOTICS_MOC|04 Robotics MOC]]
