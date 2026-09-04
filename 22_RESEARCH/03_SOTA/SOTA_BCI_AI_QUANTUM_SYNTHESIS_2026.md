---
title: SOTA BCI / AI / Quantum / Neuromorphic Synthesis 2026
type: research_synthesis
source: 22_RESEARCH
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_RESEARCH_SYNTHESIS
epistemic_class: SOURCE_CLAIM
conclusion_class: DERIVED
created: 2026-09-04
updated: 2026-09-04
rscf:
  state: DERIVED
  claim_class: SOURCE_CLAIM
  provenance:
    - Nature Medicine (s41591-026-04414-6)
    - Nature Medicine (s41591-026-04498-0)
    - Nature Neuroscience (s41593-026-02218-y)
    - Nature Electronics (s41928-025-01509-9)
    - Nature Communications (s41467-026-76090-6)
    - Nature Communications (s41467-026-71773-6)
    - Nature (s41586-026-10759-2)
    - Nature Communications (s41467-026-73331-6)
    - Nature Machine Intelligence (s42256-026-01255-3)
    - Nature Communications (s41467-026-70860-y)
    - npj Quantum Information (s41534-026-01350-8)
    - arxiv:2607.24396 (SpiNNaker2)
    - arxiv:2601.00245 (Modern Neuromorphic AI)
    - arxiv:2603.16321 (Quantum Causal Mediation)
    - arxiv:2608.18155 (QML Benchmark Audit)
    - arxiv:2608.11373 (Quantum Oncological ML)
    - arxiv:2608.24735 (Meta^n Recursive Self-Improvement)
    - arxiv:2609.02786 (SafeEvolve)
    - arxiv:2609.00829 (HarnessEvolve)
    - arxiv:2608.31111 (Aspire)
    - arxiv:2607.15524 (Recursive Harness Self-Improvement)
    - IBM/University of Chicago (2026-07-30 quantum advantage)
    - OpenAI (GPT-5.6 announcement)
    - Anthropic (Claude Opus 5 / Fable 5 / Mythos 5)
    - Google (Gemini 3.5)
    - IEEE ICEACE 2025 (Memristor BCI)
    - Nature Sensors (s44460-026-00067-7)
  scope: active__SOTA_research_synthesis_2026_Q3
tags:
  - amos
  - research
  - sota
  - bci
  - ai
  - quantum
  - neuromorphic
  - memristor
  - self-improving
  - 2026
---

# SOTA BCI / AI / Quantum / Neuromorphic Synthesis 2026

> **Harvest date:** 2026-09-04
> **Epistemic class:** SOURCE_CLAIM (peer-reviewed papers, official announcements) unless otherwise noted
> **Confidence ceiling:** 0.95 (SOURCE_CLAIM), 0.70 (AMOS_MODEL extrapolations)
> **Falsifier:** Any claim here is falsified by subsequent peer-reviewed refutation or failure to replicate

---

## 1. Brain-Computer Interfaces (BCI) — SOTA 2025-2026

### 1.1 Long-term independent at-home intracortical BCI

**Source:** Nature Medicine (s41591-026-04414-6) — SOURCE_CLAIM, peer-reviewed

An ALS participant used a multimodal intracortical BCI independently at home for **nearly 2 years**, accumulating **>3,800 hours** of use with no researchers present. Key metrics:

| Metric | Value |
|--------|-------|
| Total sentences decoded | 183,060 |
| Total words decoded | 1,960,163 |
| Average decoding rate | 56 words/min |
| User-rated accuracy (≥"mostly correct") | 92% |
| Formal word accuracy (125k vocabulary) | >99% |
| Employment sustained | Full-time |

**AMOS relevance:** Demonstrates that intracortical BCIs have crossed the threshold from lab demonstration to **independent assistive technology**. This is a phase transition from OBSERVATION (lab) to OBSERVATION (real-world deployment). The 99% word accuracy at 125k vocabulary is a 5-order-of-magnitude improvement over the first speech BCIs (~2019).

**Falsifier:** Failure to replicate in additional participants; degradation of electrode performance beyond 2 years.

### 1.2 Double neural bypass — restoring movement AND sensation

**Source:** Nature Medicine (s41591-026-04498-0) — SOURCE_CLAIM, peer-reviewed

A **bidirectional** intracortical BCI (double neural bypass, DNB) restored both hand movement and sensation in a participant with complete C4/C5 tetraplegia. The system integrates:

- Intracortical BCI for movement intention decoding
- Deep reinforcement learning for fine grasp control
- Patterned spinal cord stimulation
- Activity-informed intracortical microstimulation ("cortical mirroring")

**Key result:** Recovery of self-feeding and delicate object manipulation, with **persistent improvements** even when the system is turned off — demonstrating neuroplasticity driven by the bidirectional loop.

**AMOS relevance:** This is the first demonstration of a **bidirectional BCI** producing lasting therapeutic effects beyond assistive use. The "cortical mirroring" concept maps to AMOS's bidirectional cognitive-feedback architecture in `05_COGNITIVE_ORGANISM`.

### 1.3 Bimanual typing neuroprosthesis — 110 char/min

**Source:** Nature Neuroscience (s41593-026-02218-y) — SOURCE_CLAIM

An iBCI typing neuroprosthesis decoded attempted finger movements for bimanual QWERTY typing:

| Metric | Value |
|--------|-------|
| Typing speed | 110 char/min (22 wpm) |
| Word error rate | 1.6% |
| Calibration sentences needed | 30 |
| Participants | 2 (ALS + SCI) |

**AMOS relevance:** Approaches able-bodied typing accuracy. The RNN decoder with 5-gram language model maps to AMOS's `13_MODELS` probabilistic language layer.

### 1.4 Wireless subdural BCI — 65,536 electrodes

**Source:** Nature Electronics (s41928-025-01509-9) — SOURCE_CLAIM

A 50-μm-thick flexible micro-ECoG BCI integrating **65,536 recording electrodes** on a single CMOS substrate with 1,024 active channels, wireless powering, and telemetry. This represents a **1000× scale-up** over previous ECoG devices.

**AMOS relevance:** Minimally invasive (subdural, not intracortical) + high channel count = practical BCI scaling path. Maps to `09_PROTOCOLS` (wireless telemetry) and `14_TOOLS` (hardware capability).

### 1.5 BCI for pontine stroke dysarthria

**Source:** bioRxiv (2026.02.19.26346583) — SOURCE_CLAIM (preprint)

Intracortical BCI from a single 64-channel microelectrode array in orofacial motor cortex achieved:
- 19.6% WER on 125,000-word vocabulary (vs. 25.5% WER for ECoG on 1,024 words)
- 10.0% WER on 1,024-word vocabulary (60.8% reduction over prior ECoG)
- Stable >2 years post-implantation
- Spontaneous Q&A communication at 35.2% WER

**AMOS relevance:** Extends BCI speech restoration beyond ALS to stroke populations. The stability over 2+ years is critical evidence for long-term deployment.

---

## 2. Neuromorphic Computing — SOTA 2025-2026

### 2.1 SpiNNaker2 chip

**Source:** arxiv:2607.24396 — SOURCE_CLAIM

| Specification | Value |
|--------------|-------|
| Processing elements | 152 (ARM M4F + accelerators) |
| Deep network performance | 4.5 TOPS (high-performance) |
| Energy efficiency | 2.7 TOPS/W (INT8, high-efficiency) |
| SNN capacity | >150,000 neurons, >1.8B synaptic events/s |
| Baseline power | <250 mW |
| Time step | 1 ms |

**AMOS relevance:** SpiNNaker2 bridges neuromorphic and deep network computing. The event-based routing fabric maps to AMOS's `03_CONTROL_PLANE` event-driven coordination. The 250 mW baseline power is critical for embodied AI integration.

### 2.2 Intel Loihi 2 + Hala Point

**Source:** Neuromorphic Hardware Landscape 2026 (wagenbach.com) — SOURCE_CLAIM

| Specification | Value |
|--------------|-------|
| Process node | Intel 4nm EUV |
| Neurons per chip | 1 million programmable |
| Synapses per chip | 120 million |
| Die area | 31 mm² |
| Transistors | 2.3 billion |
| Spike processing speed | 10× over Loihi 1 |
| Hala Point system | 1.15 billion neurons, 128B synapses |
| Hala Point power | 2,600 W at max load |
| Loihi 3 target | 100× better energy efficiency than GPU (2026) |

**Key architectural advance:** Programmable microcode neuron model — Leaky Integrate-and-Fire, Izhikevich, and custom variants all run on the same hardware. Graded spikes (amplitude carries information) supported natively. Three-factor learning rules enable biologically realistic plasticity.

**AMOS relevance:** The programmable neuron model maps to AMOS's `02_KERNEL/02_COGNITION` — different cognitive primitives can be configured without hardware changes. Three-factor learning maps to the UBI (Universal Biological Intelligence) framework.

### 2.3 Dual memory pathway neuromorphic co-design

**Source:** Nature Machine Intelligence (s42256-026-01255-3) — SOURCE_CLAIM

Algorithm-hardware co-design with explicit slow memory pathway (inspired by cortical fast-slow organization):
- 40-60% fewer parameters than equivalent SNNs
- 4× throughput improvement
- 5× energy efficiency improvement
- Competitive accuracy on long-sequence benchmarks

**AMOS relevance:** The dual memory pathway (fast-slow) directly maps to AMOS's `10_MEMORY` temporal memory architecture and `02_KERNEL` cognitive primitives. The co-design approach validates AMOS's algorithm-hardware co-design philosophy.

### 2.4 Memristor BCI for robotic arm control

**Source:** IEEE ICEACE 2025 — SOURCE_CLAIM

A memristor-based compute-in-memory architecture for multimodal BCI:
- 30-channel EEG + 36-channel fNIRS fusion
- <10 ms response time
- 7-DOF robotic arm control
- FPGA cerebellar loop reference validation
- Analog parallel computing eliminates von Neumann bottleneck

**AMOS relevance:** Memristor + BCI convergence is a direct hardware implementation of AMOS's cognitive organism concept. The cerebellar loop reference maps to `05_COGNITIVE_ORGANISM` organ coordination.

### 2.5 Self-powered analogue neuromorphic system

**Source:** Nature Sensors (s44460-026-00067-7) — SOURCE_CLAIM

A fully analogue, self-powered neuromorphic system using drift and diffusive memristors:
- Multimodal sensing + spike encoding + unsupervised learning
- No digital circuitry or external power
- Homo-synaptic and hetero-synaptic plasticity
- Sensing, computation, memory, and learning on single PCB

**AMOS relevance:** Self-powered neuromorphic processing is the hardware substrate for AMOS's autonomous cognitive organism. The hetero-synaptic plasticity maps to the UBI framework's cross-domain learning.

### 2.6 Synthetic hippocampus for robotic cognition

**Source:** BioNanoScience 2025 — SOURCE_CLAIM

A synthetic hippocampal architecture using SNNs and neuromorphic substrates:
- Segregates online sensorimotor interaction from offline consolidation
- Bidirectional memory traversal
- Goal-prioritised plasticity updates
- Energy-efficient policy synthesis
- Dual-state system bridging real-time control with autonomous learning

**AMOS relevance:** Directly maps to AMOS's `10_MEMORY` dual-mode architecture (online/offline) and `05_COGNITIVE_ORGANISM` cognitive loop.

---

## 3. Quantum Computing & Quantum ML — SOTA 2025-2026

### 3.1 IBM/University of Chicago quantum advantage demonstration

**Source:** IBM Newsroom (2026-07-30) — SOURCE_CLAIM (corporate announcement)

IBM and University of Chicago demonstrated quantum advantage using:
- **70 logical qubits** with novel error correction
- Computation completed in **~15 minutes**
- Classically intractable sampling problem
- Verifiable high fidelity (trusted quantum computation)
- Released on Quantum Advantage Tracker

**AMOS relevance:** First credible quantum advantage with trust verification. The "trusted quantum computation" concept maps to AMOS's `18_SECURITY` trust-boundary enforcement and `03_CONTROL_PLANE` commit-time validation.

**Falsifier:** Classical algorithm improvement that matches the quantum result; failure to scale beyond 70 logical qubits.

### 3.2 Surface code scaling on heavy-hex

**Source:** Nature Communications (s41467-026-76090-6) — SOURCE_CLAIM

IBM demonstrated subthreshold scaling of surface codes on heavy-hex lattice:
- Distance scaling from (3,3) to (3,5) and (5,3)
- Dynamical decoupling suppresses coherent ZZ crosstalk
- ~30% noise reduction would enable (5,5) scaling
- Basis-dependent scaling (not isotropic)

**AMOS relevance:** The basis-dependent scaling is a MECE-style partition insight — X and Z errors scale differently, requiring asymmetric protection. Maps to `01_CANON/04_INFRASTRUCTURE_CANON` error correction canon.

### 3.3 Reinforcement learning control of quantum error correction

**Source:** Nature (s41586-026-10759-2) — SOURCE_CLAIM

Google's Willow processor used RL to continuously steer QEC control parameters:
- 3.5× improvement in logical stability against injected drift
- Record surface code performance: 7.72×10⁻⁴ logical error per cycle
- Record colour code performance: 8.19×10⁻³ logical error per cycle
- RL optimization speed independent of system size (scalable)
- "A quantum computer that learns from its errors and never stops computing"

**AMOS relevance:** The RL-driven QEC directly maps to AMOS's `02_KERNEL/06_RISK_REPAIR` — the system repairs itself during execution, not by stopping. The "never stops computing" paradigm is the AMOS `04_RUNTIME` continuous-operation invariant.

### 3.4 Real-time low-latency QEC with FPGA decoder

**Source:** Nature Communications (s41467-026-73331-6) — SOURCE_CLAIM

- 8-qubit stability experiment with 25 decoding rounds
- Sub-microsecond mean decoding time per round
- Scalable FPGA decoder integrated into control system
- Logical error suppression with increasing rounds
- Evidence that backlog problem is avoidable

**AMOS relevance:** Sub-microsecond decoding maps to AMOS's `04_RUNTIME` bounded execution lifecycle and `17_OBSERVABILITY` real-time telemetry.

### 3.5 Quantum ML — skeptical analysis

**Source:** arxiv:2603.16321, arxiv:2608.18155, arxiv:2608.11373, npj Quantum Information (s41534-026-01350-8) — SOURCE_CLAIM

**Key findings (sobering):**

1. **Causal mediation analysis** (arxiv:2603.16321): Direct architectural contributions exceed quantum-mediated effects by 13.1:1. Mean indirect quantum contribution: only 0.82%. Current variational quantum circuits operate substantially below their quantum potential.

2. **QML-IDS benchmark** (arxiv:2608.18155): Tuned classical models (Random Forest, XGBoost) match or exceed quantum models on every NIDS dataset. Apparent quantum gains attributed to classical preprocessing and regularisation, not quantum effects. Only two advantages survive FDR correction.

3. **Gaussian process regression** (npj QI): No exponential speedup in a wide range of scenarios. Condition number of kernel matrix scales at least linearly with matrix size.

4. **Oncological data benchmark** (arxiv:2608.11373): No evidence of quantum advantage in ML on oncological data. Field should prioritize higher-dimensional, biologically realistic datasets.

5. **QML state of the field** (postquantum.com): "Quantum machine learning now has a demonstrated advantage on quantum data and no accepted advantage on ordinary business data."

**AMOS relevance:** These skeptical findings are critical for AMOS's epistemic discipline. They validate `L1_EPISTEMIC.02` (Source Claim ≠ Verification) and `L4_CAUSAL` (Causal Firewall). The 0.82% quantum-mediated contribution is a COMPETING hypothesis against quantum advantage claims. AMOS must not promote QML from CONDITIONAL to ESTABLISHED without discriminating evidence.

---

## 4. AI / LLM Frontier — SOTA 2025-2026

### 4.1 GPT-5.6 — frontier intelligence + efficiency

**Source:** OpenAI announcement — SOURCE_CLAIM (corporate)

| Model | Position | Key claim |
|-------|----------|-----------|
| GPT-5.6 Sol | Flagship | Outperforms Claude Fable 5 on coding agent index at <½ cost |
| GPT-5.6 Terra | Mid-tier | Matches GPT-5.5 intelligence at ½ price |
| GPT-5.6 Luna | Fastest | 80% cheaper than Sol |

**Key architectural advance:** Training optimised for both task success AND efficiency — "more work per token." Inference optimisations include load balancing, speculative decoding, caching, and kernel optimisation. Agentic harness improvements for context bloat, tool usage, and repeated work.

**AMOS relevance:** The "more work per token" training objective maps to AMOS's `02_KERNEL` efficiency invariant (INTEGRITY > COMPLETENESS > FLUENCY > SPEED > TOKEN_SAVINGS). The agentic harness optimisation maps to `08_WORKFLOWS` process orchestration.

### 4.2 Claude Opus 5 / Fable 5 / Mythos 5

**Source:** Anthropic announcements — SOURCE_CLAIM (corporate)

| Model | Configuration | Key metric |
|-------|--------------|------------|
| Claude Mythos 5 | Trusted partners only | Most capable Anthropic model; safeguards lifted for vetted partners |
| Claude Fable 5 | General access | Same weights as Mythos 5; safeguards for bio/cybersecurity |
| Claude Opus 5 | Default for Max/Pro | 2× Opus 4.8 performance on Frontier-Bench at lower cost |
| Claude Sonnet 5 | Default for Free/Pro | Close to Opus 4.8 performance at lower prices |

**Key results:**
- ARC-AGI 3: Opus 5 scores 3× the next-best model
- Zapier AutomationBench: Opus 5 pass rate 1.5× next-best at same cost
- OSWorld 2.0: Opus 5 surpasses Fable 5 at ⅓ the cost
- Best-ever prompt injection resistance (Gray Swan benchmark)

**AMOS relevance:** The Mythos/Fable split (same weights, different safeguards) maps to AMOS's `18_SECURITY` authority boundary — capability is not authorization. The "verifying its work and iterating" behavior maps to AMOS's `19_TESTS` validation gate.

### 4.3 Gemini 3.5 — frontier intelligence with action

**Source:** Google blog announcement — SOURCE_CLAIM (corporate)

| Metric | Value |
|--------|-------|
| Terminal-Bench 2.1 | 76.2% |
| GDPval-AA | 1656 Elo |
| MCP Atlas | 83.6% |
| CharXiv Reasoning | 84.2% |
| Speed vs. frontier | 4× faster |

**Key advance:** Antigravity harness deploys collaborative subagents for multi-step workflows. Builder + player agent architecture for complex task execution.

**AMOS relevance:** The builder/player agent split maps to AMOS's `06_AGENTS` worker/orchestrator separation. The Antigravity harness maps to `08_WORKFLOWS` orchestration.

---

## 5. Self-Improving & Agentic AI — SOTA 2025-2026

### 5.1 Meta^n — Recursive self-improvement through emergent depth

**Source:** arxiv:2608.24735 — SOURCE_CLAIM

Meta^n keeps the meta-operation fixed and recurses on its input. Each layer reads traces of the solver stack below + code that produced them, then writes the next layer as a strategic pre-process + callable helpers.

**Key results:**
- Outperforms prior self-improving agents on all 8 benchmark families
- Only agent scoring above zero on ARC-AGI-2 (built to resist skill memorization)
- Depth set by convergence, not fixed in advance
- Distinct layer roles emerge with depth (no prompt prescribes them)

**AMOS relevance:** The fixed meta-operation + growing input is the AMOS `02_KERNEL/01_META_LOGIC` pattern — the reasoning kernel is immutable while the knowledge substrate grows. The emergent layer roles validate AMOS's `25_COGNITIVE_MATRIX` fractal decomposition.

### 5.2 SafeEvolve — Harness-policy co-evolution for safety

**Source:** arxiv:2609.02786 — SOURCE_CLAIM

Experience-driven self-evolving framework for agent safety alignment:
- Harness side: trajectory-level safety evidence → bounded, component-level updates (auditable, reversible)
- Policy side: SFT-RL paradigm with verifier-decomposed rewards
- 3× ASR reduction on AgentDojo while improving utility from 59.79% to 61.86%
- Harm score reduced from 56.45 to 12.27 on AgentHarm

**AMOS relevance:** The "auditable and reversible" harness updates map to AMOS's `04_RUNTIME` rollback/recovery and `17_OBSERVABILITY` audit trail. The verifier-decomposed rewards map to `19_TESTS` validation gates.

### 5.3 HarnessEvolve — Learning from reference trajectories

**Source:** arxiv:2609.00829 — SOURCE_CLAIM

Addresses three challenges in agent self-evolution:
1. **Credit assignment failure** → reference trajectories + error signal clustering
2. **Shortcut learning** → quality gate filters data leakage and prompt bloat
3. **Catastrophic forgetting** → performance gate + epoch-end validation on held-out set

**AMOS relevance:** All three challenges map directly to AMOS's `02_KERNEL/06_RISK_REPAIR` (biological integrity, entropy correction). The quality + performance gates map to `03_CONTROL_PLANE/09_COMMIT` commit-time revalidation.

### 5.4 Aspire — Self-evolution from vague goals

**Source:** arxiv:2608.31111 — SOURCE_CLAIM

ASPIRE benchmark for vague-goal-driven self-evolution:
- Agent must operationalize natural-language capability goals
- Hidden evaluation tasks (520 items, 6 goals)
- Supports both model-weight and agent-harness evolution
- Finding: "vague goals redirect search effort toward goal interpretation"
- Finding: "weight-level gains remain sparse and unstable"
- Finding: "strongest evolved harness remains below engineered reference"

**AMOS relevance:** The gap between self-evolved and engineered harnesses validates AMOS's `L7_AUTHORITY` — autonomous evolution does not exceed governed authority. The instability of weight-level gains maps to `L0.02` (No Fabricated Closure) — cannot claim improvement without discriminating evidence.

### 5.5 OPT-BENCH — Scaling law of self-improvement

**Source:** ACL 2026 Findings — SOURCE_CLAIM

Benchmark with 20 ML tasks + 10 NP-hard problems across 19 LLMs:
- **Scaling Law of Self-Improvement:** stronger base models are significantly more effective at leveraging historical feedback
- **Critical cognitive divergence:** historical context helps in continuous ML domains but is constrained in discrete NP tasks
- Frontier models "frequently resetting solutions rather than repairing them" in combinatorial spaces

**AMOS relevance:** The divergence between continuous and discrete optimization validates AMOS's `L5_SCOPE_REGIME` — claims valid only within declared scope. The "resetting vs. repairing" finding maps to `02_KERNEL/06_RISK_REPAIR` — repair is harder than restart.

---

## 6. Convergence Trends

### 6.1 BCI + AI convergence

The memristor BCI (IEEE ICEACE 2025) and the double neural bypass (Nature Medicine 2026) demonstrate that BCI + AI is no longer theoretical — it is producing clinical results. The key convergence vectors:

1. **Neural decoding** → RNN/RL decoders achieving >99% word accuracy
2. **Neuromorphic hardware** → memristor arrays for <10ms BCI response
3. **Bidirectional BCI** → closed-loop cortical mirroring for neuroplasticity
4. **Minimally invasive** → 65k electrode subdural arrays

**AMOS_MODEL:** By 2027, BCI + AI will likely demonstrate:
- Non-invasive BCI achieving >90% word accuracy on >10k vocabulary (CONDITIONAL, confidence 0.6)
- Bidirectional BCI in chronic stroke rehabilitation trials (CONDITIONAL, confidence 0.7)
- Memristor-based BCI chips in human clinical trials (UNKNOWN/GAP, confidence 0.4)

### 6.2 Quantum + AI convergence

The IBM 70-logical-qubit quantum advantage and the RL-driven QEC (Google Willow) show quantum hardware maturing. However, QML on classical data has no accepted advantage (Section 3.5).

**AMOS_MODEL:** The convergence path is:
1. **Quantum for QEC** (OBSERVATION — already demonstrated)
2. **Quantum for quantum data** (OBSERVATION — bosonic displacement learning)
3. **Quantum for classical ML** (COMPETING — no broad acceptance)
4. **Quantum-classical hybrid** (CONDITIONAL — strongest practical path)

**Falsifier for quantum-classical hybrid advantage:** Classical algorithm improvements that match hybrid performance on the same tasks.

### 6.3 Neuromorphic + quantum convergence

**Status:** UNKNOWN/GAP — no credible demonstration of neuromorphic-quantum hybrid computing as of 2026-09-04.

**AMOS_MODEL:** The theoretical path would involve:
- Quantum neurons (qubit-based neuron models)
- Quantum-enhanced synaptic plasticity
- Quantum state space for SNN dynamics

**Confidence:** 0.3 (CONDITIONAL, no empirical evidence yet)

### 6.4 Embodied AI + robotics

The synthetic hippocampus (BioNanoScience 2025) and multi-network neuromorphic robotic control (IOP 2026) show embodied AI advancing on neuromorphic substrates:

- Spiking neural state machines for process orchestration on Loihi 2
- Milliwatt-regime operation with millisecond latencies
- Dual-state memory (online/offline) for adaptive generalization

**AMOS relevance:** Embodied AI on neuromorphic hardware is the physical implementation of AMOS's `05_COGNITIVE_ORGANISM` + `14_TOOLS` integration. The milliwatt power budget validates AMOS's efficiency-first invariant.

---

## 7. AMOS Architectural Implications

### 7.1 Validated architectural decisions

| AMOS component | SOTA validation | Source |
|----------------|----------------|--------|
| `02_KERNEL/06_RISK_REPAIR` | RL-driven QEC "never stops computing" | Nature s41586-026-10759-2 |
| `03_CONTROL_PLANE/09_COMMIT` | SafeEvolve auditable/reversible updates | arxiv:2609.02786 |
| `05_COGNITIVE_ORGANISM` | Bidirectional BCI cortical mirroring | Nature Medicine s41591-026-04498-0 |
| `10_MEMORY` dual-mode | Synthetic hippocampus online/offline | BioNanoScience 2025 |
| `13_MODELS` probabilistic | RNN + language model BCI decoding | Nature Neuroscience s41593-026-02218-y |
| `17_OBSERVABILITY` | Sub-μs QEC decoder telemetry | Nature Comms s41467-026-73331-6 |
| `18_SECURITY` authority ≠ capability | Mythos/Fable same weights, different safeguards | Anthropic 2026 |
| `19_TESTS` validation gates | HarnessEvolve quality + performance gates | arxiv:2609.00829 |
| `L0_INTEGRITY` > speed | GPT-5.6 "more work per token" | OpenAI 2026 |
| `L1_EPISTEMIC.02` source ≠ verified | QML 0.82% quantum contribution | arxiv:2603.16321 |
| `L4_CAUSAL` firewall | QML causal mediation framework | arxiv:2603.16321 |
| `L5_SCOPE_REGIME` | OPT-BENCH continuous vs. discrete divergence | ACL 2026 |
| `L7_AUTHORITY` | Aspire: self-evolved < engineered reference | arxiv:2608.31111 |

### 7.2 Identified gaps

| Gap | SOTA evidence | AMOS action |
|-----|---------------|-------------|
| Quantum-ML advantage on classical data | No broad acceptance | Keep QML as CONDITIONAL in `13_MODELS` |
| Self-improving AI stability | Weight-level gains "sparse and unstable" | Strengthen `02_KERNEL/06_RISK_REPAIR` |
| Agent credit assignment | Reference trajectory alignment needed | Add to `08_WORKFLOWS` orchestration |
| Neuromorphic-quantum convergence | No empirical evidence | Mark as UNKNOWN/GAP in `22_RESEARCH` |

### 7.3 Recommended vault updates

1. **`02_KERNEL/02_COGNITION/`** — Add BCI bidirectional loop as validated cognitive architecture pattern
2. **`02_KERNEL/06_RISK_REPAIR/`** — Add RL-driven QEC as self-repair paradigm
3. **`05_COGNITIVE_ORGANISM/`** — Add cortical mirroring as organ coordination pattern
4. **`10_MEMORY/`** — Add synthetic hippocampus as dual-mode memory reference
5. **`13_MODELS/`** — Add quantum ML as CONDITIONAL model class (not ESTABLISHED)
6. **`18_SECURITY/`** — Add Mythos/Fable safeguard split as authority-capability separation example
7. **`22_RESEARCH/`** — This document as SOTA reference

---

## 8. Epistemic Summary

| Domain | Strongest evidence | Epistemic class | Confidence ceiling |
|--------|-------------------|-----------------|-------------------|
| BCI speech decoding | >99% word accuracy, 125k vocab, 2-year independent use | OBSERVATION | 0.95 |
| BCI motor restoration | Self-feeding, persistent recovery | OBSERVATION | 0.90 |
| Neuromorphic chips | Loihi 2, SpiNNaker2, Hala Point deployed | OBSERVATION | 0.95 |
| Memristor BCI | <10ms response, 7-DOF arm (simulation) | SOURCE_CLAIM | 0.80 |
| Quantum advantage (sampling) | 70 logical qubits, trusted verification | SOURCE_CLAIM | 0.85 |
| Quantum ML on classical data | No accepted advantage | SOURCE_CLAIM | 0.90 |
| RL-driven QEC | 3.5× stability improvement, record error rates | OBSERVATION | 0.95 |
| Frontier LLM capability | GPT-5.6, Claude 5, Gemini 3.5 benchmarks | SOURCE_CLAIM | 0.80 |
| Self-improving AI | Meta^n on ARC-AGI-2, but narrow | SOURCE_CLAIM | 0.75 |
| Agent safety alignment | SafeEvolve 3× ASR reduction | SOURCE_CLAIM | 0.80 |

---

**Related:** [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] · [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]] · [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]] · [[01_CANON/01_CORE_LAWS/AMOS_CORE_LAWS|AMOS_CORE_LAWS]]

**MOC:** [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]

---
RSCF-NODE
node_id: SOTA_BCI_AI_QUANTUM_SYNTHESIS_2026
node_type: research_synthesis
path: 22_RESEARCH/03_SOTA/SOTA_BCI_AI_QUANTUM_SYNTHESIS_2026.md
RSCF-RELATIONS:
- INDEXED_BY: [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
- CHILD_OF: [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
- REFERENCES: [[01_CANON/01_CORE_LAWS/AMOS_CORE_LAWS|AMOS_CORE_LAWS]]
- REFERENCES: [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]]
