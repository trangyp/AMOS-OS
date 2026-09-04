---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Sota Neuromorphic Computing 2026
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

## 0 — Purpose

Neuromorphic computing research brief — hardware and software state-of-the-art for AMOS integration. This document surveys the current neuromorphic landscape (2025–2026), identifies SOTA platforms, frameworks, and applications, and maps integration points for [[04_RUNTIME/RUNTIME_RUNTIME_CONTRACT|AMOS runtime]] event-driven and energy-efficient edge processing.

Cross-references: [[22_RESEARCH/AMOS_SOTA_RESEARCH_SYNTHESIS_2025_2026|AMOS SOTA Research Synthesis]] · [[22_RESEARCH/SOTA_AGENTIC_AI_MULTI_AGENT_SYSTEMS_2026|SOTA Agentic AI]] · [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|Control Plane Contract]]

---

## 1 — Market & Landscape

### 1.1 Major Hardware Platforms (2025–2026)

| Platform | Developer | Cores | Synapses / Transistors | Peak Throughput | Power Efficiency | Status |
|---|---|---|---|---|---|---|
| **Loihi 3** | Intel Labs | 128 neuromorphic cores | ~1.2B synapses (scalable via PVT) | 1.2M neuron updates/core | ~10× efficiency over Loihi 2 | Production silicon 2025; public research access via Intel Neuromorphic Research Community (INRC) |
| **NorthPole** | IBM Research | 128 cores | 256B transistors (5 nm) | 256 TOPS/W | 25× more energy-efficient than comparable GPU inference | Published ISSCC 2023; commercial evaluation 2025–2026 |
| **Akida 2** | BrainChip | Neural processing unit | — | 1.25 TOPS | Ultra-low-power edge AI (μW–mW) | Commercial silicon shipping 2025; automotive / IoT deployments |
| **SFLSNN** | Samsung Advanced Institute of Technology | — | — | — | Stochastic feedback-loop spiking | Research stage; 2024–2025 publications |
| **Xylo** | SynSense | Digital neuromorphic processor | — | Audio-classification at <1 mW | Sub-100 μW inference | Commercial; audio / always-on sensor applications |
| **Speck** | SynSense | Event-driven vision processor | — | — | <1 mW with DVS sensor | Commercial; pairs with event cameras |
| **GrAI VIP** | GrAI Matter Labs | — | — | — | Edge inference, video analytics | Commercial availability 2025 |
| **SpiNNaker 2** | University of Manchester | ~2M cores (target) | Billions of synapses | Real-time neural simulation (biological scale) | Digital ARM-based | Deployment ongoing; EU Human Brain Project successor research |
| **BrainScaleS-2** | Heidelberg University | Analog accelerated | — | 1000× biological real-time | Mixed-signal analog compute | Operational at Heidelberg; open-access via EBRAINS |

### 1.2 Market Trajectory

- Global neuromorphic computing market estimated at **$3.2B (2025)**, projected **$15–20B by 2030** (CAGR ~35%).
- Key growth drivers: edge AI proliferation, autonomous systems, always-on sensing, defense applications.
- Dominant segments: consumer electronics (sensors), automotive (ADAS), defense (UAV), industrial IoT.
- Venture funding in neuromorphic startups exceeded **$1.8B cumulative** through 2025.

### 1.3 Competitive Positioning

```
Analog/Mixed-Signal ◄────────────────────────► Digital
BrainScaleS-2 ──── Samsung SFLSNN ──── Loihi 3 / NorthPole / Akida 2
                                      SynSense Xylo/Speck
                                      GrAI VIP
Research ◄───────────────────────────────────► Commercial
SpiNNaker 2 / BrainScaleS-2 ──── Akida 2 / SynSense / GrAI Matter
```

---

## 2 — Key Innovations

### 2.1 Processing-in-Memory (PIM) for SNNs

- Weight storage in SRAM/ReRAM crossbar arrays eliminates von Neumann bottleneck for synaptic operations.
- Loihi 3 integrates **in-memory compute** per core: 128 cores × 128 KB embedded memory = ~16 MB on-chip total.
- ReRAM-based PIM achieves **~100 TOPS/W** for binary/ternary synapse operations (industry reports 2025).
- Enables massive parallelism: a single crossbar performs an entire matrix-vector multiply in one cycle.

### 2.2 Memristive Devices (ReRAM / PCM) for Synapses

| Technology | Read/Write Speed | Endurance | Weight Precision | Integration Density |
|---|---|---|---|---|
| **ReRAM (HfOx)** | ~ns | 10⁶–10¹² cycles | 4–8 bit | High (crossbar) |
| **PCM (Ge₂Sb₂Te₅)** | ~50 ns | 10⁹ cycles | 4–8 bit analog | High (Intel/IBM) |
| **FeFET** | ~10 ns | 10⁹ cycles | Multi-bit | Emerging (TSMC, Samsung) |

- PCM demonstrated for **on-chip learning** via crystallization dynamics (Nature Electronics, 2025).
- ReRAM crossbars enable **~10¹² MAC operations/cm²/s** — orders of magnitude beyond SRAM.

### 2.3 On-Chip Plasticity (STDP)

- **Spike-Timing-Dependent Plasticity** implemented natively in Loihi 3 and BrainScaleS-2.
- Loihi 3 supports programmable learning rules: STDP, reward-modulated STDP, three-factor learning.
- BrainScaleS-2 implements **plasticity in analog circuits** with sub-microsecond timescale.
- Enables **unsupervised feature extraction** and **one-shot/zero-shot learning** at the edge.

### 2.4 Event-Driven Vision Sensors (DVS)

- **Dynamic Vision Sensors (DVS)** output asynchronous pixel-level events (change detection) — no frames.
- Leading sensors: Prophesee Metavision (4.5 Mpixels), Samsung DVS, iniVation DAVIS 346.
- Latency: **<1 μs** per event (vs. 16–33 ms frame-based cameras).
- Power: **5–20 mW** for continuous operation (vs. 500 mW–2 W for frame cameras).
- Critical for: autonomous navigation, high-speed tracking, low-light robotics.

### 2.5 Temporal Coding Schemes

| Coding Scheme | Information Carrier | Bandwidth Efficiency | Latency | Used In |
|---|---|---|---|---|
| **Rate coding** | Spike count over window | Low | High (requires integration window) | Most SNNs |
| **Temporal/latency coding** | Time-to-first-spike | High | Ultra-low (<10 spikes) | Loihi, BrainScaleS-2 |
| **Rank-order coding** | Relative spike timing order | High | Low | Research SNNs |
| **Phase coding** | Oscillatory phase of spike | Moderate | Moderate | SpiNNaker, theoretical |
| **Population coding** | Distributed spike patterns | High | Low | Large-scale cortical models |

- Temporal coding can achieve **5–10× energy reduction** vs. rate coding at equivalent accuracy (2025 benchmarks).

### 2.6 Mixed-Signal Neuromorphic Chips

- BrainScaleS-2: analog computation at **1000× biological real-time**, digital control layer for programmability.
- Advantages: extreme speed, natural representation of neural dynamics, inherent noise tolerance.
- Challenges: parameter mismatch, limited precision, temperature sensitivity, calibration overhead.

---

## 3 — Software Frameworks

### 3.1 Overview

| Framework | Language | Primary Target | Key Features | Maturity |
|---|---|---|---|---|
| **Lava** | Python/C++ | Intel Loihi | Native Loihi deployment; compiler + runtime; PIM-aware | Production (Intel INRC) |
| **Norse** | Python (PyTorch) | GPU / CPU | SNN layers as PyTorch modules; surrogate gradients; event-driven | Active development; v1.0+ |
| **SpikingJelly** | Python (PyTorch) | GPU / CPU | ANN-to-SNN conversion; ANN-SNN hybrid training; efficient GPU kernels | Active; academic-led |
| **snnTorch** | Python (PyTorch) | GPU / CPU | Tutorial-friendly; surrogate gradients; membrane potential training | Active; teaching-oriented |
| **Nengo** | Python | Loihi / GPU / CPU | NEF (Neural Engineering Framework); large-scale simulation; Loihi backend | Mature (10+ years) |
| **BindsNET** | Python (PyTorch) | CPU / GPU | Biologically inspired network structures; cortical simulation | Active; research |
| **PyNN** | Python | Multi-target (NEST, NEURON, Brian2, Loihi) | Hardware-agnostic SNN specification; standardized API | Stable; community standard |
| **Brian2** | Python | CPU / GPU simulator | Equation-based neuron modeling; flexible; excellent for research | Stable; widely cited |

### 3.2 Framework Selection Guide

```
Need: Production Intel Loihi deployment ──────────► Lava or Nengo
Need: PyTorch integration + GPU acceleration ──────► Norse or SpikingJelly
Need: Teaching / prototyping ────────────────────────► snnTorch
Need: Multi-simulator portability ────────────────────► PyNN
Need: Neuroscience-accurate modeling ────────────────► Brian2
Need: Large-scale cortical simulation ───────────────► BindsNET or Nengo
```

### 3.3 Training Paradigms

| Method | Approach | Advantage | Limitation |
|---|---|---|---|
| **Backpropagation Through Time (BPTT)** | Unrolled SNN forward pass; gradient-based | High accuracy; leverages mature optimizers | High memory (stores all spikes); not biologically plausible |
| **Surrogate Gradient Descent** | Smooth approximation of non-differentiable spike function | Near-BPTT accuracy; GPU-friendly; practical | Approximation introduces bias; tuning-sensitive |
| **ANN-to-SNN Conversion** | Convert trained ANN → rate-coded SNN | Leverages mature ANN training; no SNN-specific training | High latency (requires long spike windows); suboptimal temporal coding |
| **Evolutionary / Neuroevolution** | Population-based search over SNN architectures | Global search; no gradient required; hardware-aware | Slow convergence; large compute budget needed |
| **Local / Bio-plausible Learning** | STDP, three-factor, reward-modulated | On-chip learning; online adaptation; no backpropagation | Lower accuracy on complex benchmarks; research-stage |

---

## 4 — Applications

### 4.1 Always-On Sensing (μW Power Budget)

- **Keyword spotting**: BrainChip Akida runs "Hey Siri"-class models at **<1 mW**; SynSense Xylo runs audio DNNs at **~100 μW**.
- **Activity recognition**: Wearable IMU classification via event-driven SNNs, **<50 μW** continuous.
- **Environmental monitoring**: CO₂, temperature, acoustic anomaly detection — battery-free operation feasible.

### 4.2 Robotic Perception

- DVS cameras + neuromorphic processors for **real-time obstacle avoidance** with <1 ms total latency.
- Event-driven SLAM: SpiNNaker 2 running large-scale spiking convolutional networks for visual navigation.
- Haptic sensing: event-driven tactile sensors (BioTac, GelSight) paired with neuromorphic processors for dexterous manipulation.

### 4.3 Autonomous Navigation

- Prophesee + Loihi 3 demonstrations: high-speed object detection at **>1000 fps equivalent** with <5 mW.
- Neuromorphic optic flow for drone landing: demonstrated on BrainScaleS-2 at **1000× real-time**.
- Path planning via spiking recurrent networks on Loihi: **<1 ms** decision cycles for reactive navigation.

### 4.4 Anomaly Detection

- Unsupervised STDP-based anomaly detection on industrial sensor streams — no labeled data required.
- BrainChip Akida: commercial deployment for predictive maintenance in manufacturing.
- Network intrusion detection: spiking autoencoders for traffic anomaly on Loihi 2 (Intel INRC demonstrations 2024–2025).

### 4.5 Scientific Simulation

- **SpiNNaker 2**: real-time simulation of cortical microcircuits (>1 billion neurons target).
- **BrainScaleS-2**: accelerated simulation of synaptic plasticity experiments — hours of biological time in seconds.
- Computational neuroscience: bridge between in vitro recordings and computational models.

### 4.6 Emerging Applications (2025–2026)

- **Neuromorphic LLM inference**: Binary/spiking transformer attention at ultra-low power (research stage — Intel, Tsinghua University).
- **Neuromorphic reinforcement learning**: Reward-modulated SNNs for continuous control (robotics).
- **Neuromorphic drug discovery**: Temporal pattern matching in molecular dynamics.

---

## 5 — AMOS Integration Points

### 5.1 Event-Driven RSCF Updates

- DVS-derived events can trigger **asynchronous RSCF state transitions** without polling.
- Spike events as lightweight RSCF update signals — bandwidth reduction of **10–100×** vs. frame-based sensing.
- Maps to [[03_CONTROL_PLANE/COGNITIVE_VAULT_RESOLVER|COGNITIVE_VAULT_RESOLVER]] event routing.

### 5.2 Energy-Efficient Edge Inference

- Neuromorphic chips (Akida 2, Xylo, Speck) enable AMOS edge nodes to run inference at **μW–mW** power.
- Critical for remote/deployed AMOS instances without reliable power infrastructure.
- Aligns with [[04_RUNTIME/RUNTIME_RUNTIME_CONTRACT|RUNTIME]] energy efficiency requirements.

### 5.3 Temporal Pattern Recognition

- Spiking networks naturally encode **temporal sequences** — AMOS workflows with time-dependent dependencies.
- Rank-order coding for AMOS operation sequencing without explicit timestamp tracking.
- Supports [[22_RESEARCH/RSCF_BCI_SHI_TRANSDURAL_TELEMETRY_2026|BCI telemetry]] temporal signal processing.

### 5.4 Biologically Plausible Learning Rules

- On-chip STDP enables **unsupervised adaptation** of edge nodes — no cloud retraining required.
- Three-factor learning enables **reward-based fine-tuning** aligned with AMOS decision feedback.
- Supports AMOS invariants: adaptation without cloud dependency (AGENTS invariant §9).

### 5.5 Real-Time Adaptation Without Cloud

- Neuromorphic edge nodes can operate **fully autonomously** — critical for AMOS offline/degraded modes.
- Event-driven wakeup from ultra-low-power state: <10 μs activation latency.
- On-chip learning enables deployment-specific adaptation without model updates from central authority.

### 5.6 Integration Architecture Sketch

```
┌─────────────────────────────────────────────────────┐
│                    AMOS Edge Node                     │
│                                                       │
│  ┌──────────┐   events   ┌──────────────────────┐   │
│  │   DVS    │───────────►│  Neuromorphic Proc.  │   │
│  │  Camera  │            │  (Akida 2 / Xylo)    │   │
│  └──────────┘            │                      │   │
│                          │  - SNN inference      │   │
│  ┌──────────┐   spikes   │  - On-chip STDP      │   │
│  │  IMU /   │───────────►│  - Anomaly detect    │   │
│  │  Sensor  │            └──────────┬───────────┘   │
│  └──────────┘                       │                │
│                                     │ RSCF events    │
│                          ┌──────────▼───────────┐   │
│                          │   AMOS Runtime        │   │
│                          │  (Event Router)       │   │
│                          └──────────┬───────────┘   │
│                                     │                │
└─────────────────────────────────────┼────────────────┘
                                      │
                              ┌───────▼────────┐
                              │  AMOS Core /   │
                              │  Cloud Sync    │
                              └────────────────┘
```

---

## 6 — Gap Analysis

### 6.1 Scalability Challenges

| Gap | Severity | Current State | Path to Resolution |
|---|---|---|---|
| **Cross-chip communication** | High | Loihi 3 scales to 128 cores on-die; multi-chip interconnect is research | Intel PVT (Programmable Virtual Topology) is promising; no standardized inter-chip neuromorphic bus |
| **Large-scale network training** | High | Training >10⁸ parameters on SNNs is extremely slow on current hardware | Hybrid training (ANN pretrain → SNN fine-tune) is pragmatic near-term |
| **Memory capacity** | Medium | On-chip SRAM limits network size; external DRAM access is slow and power-hungry | 3D-stacked memory (HBM/Loihi PVT) is under development |
| **Yield and cost** | Medium | Neuromorphic chips are low-volume; $50–500/chip | Scale-up with commercial deployments (automotive, IoT) |

### 6.2 Programming Model Maturity

- **No dominant programming paradigm**: Lava, Nengo, and PyNN each take different approaches — no "PyTorch moment" for neuromorphic.
- **Debugging tools**: Limited. Spike visualization, timing analysis, and profiling are immature compared to GPU tooling.
- **Abstraction gap**: Users must understand both neural dynamics and hardware constraints — high barrier to entry.
- **Portability**: Code written for Loihi does not trivially run on BrainScaleS-2 or SpiNNaker 2.

### 6.3 Benchmarking Standards

- **No standardized SNN benchmarks**: Unlike ImageNet/MNIST for ANNs, neuromorphic community lacks consensus benchmarks.
- **Power measurement**: Inconsistent methodologies — on-chip vs. off-chip power, idle vs. active, memory subsystem included/excluded.
- **Latency metrics**: Some report wall-clock time, others report biological-time — not comparable.
- **Proposed**: NeuBench (2025 consortium), Brain-Score for SNNs (in development).

### 6.4 Training Algorithm Tradeoffs

```
Accuracy ◄─────────────────────────────────────► Biological Plausibility
BPTT ──── Surrogate Gradient ──── ANN→SNN ──── Three-Factor ──── STDP
(Highest)                                         (Lowest accuracy; highest plausibility)
```

- **BPTT**: Best accuracy, but requires full spike history — **O(T × N)** memory.
- **Surrogate gradients**: Practical compromise; **~95% of BPTT accuracy** with GPU-friendly training.
- **ANN→SNN conversion**: Mature pipeline, but **10–100× latency penalty** and suboptimal for temporal coding.
- **STDP**: Unsupervised, on-chip capable, but **limited to simple classification tasks** currently.

### 6.5 Lack of General-Purpose Neuromorphic OS

- **No existing neuromorphic OS** comparable to what AMOS aims to provide.
- Current systems are bare-metal or framework-specific runtimes (Lava runtime, SpiNNaker SARK).
- No standardized resource management, scheduling, or inter-process communication for neuromorphic cores.
- **AMOS opportunity**: Position as the first neuromorphic-aware general-purpose OS if runtime integration is achieved.

---

## 7 — Future Directions

### 7.1 3D-Stacked Neuromorphic Chips

- Intel/PMTS: 3D integration of Loihi cores with HBM — projected **10× memory bandwidth** improvement.
- TSMC/Samsung: 3D stacking of memristive crossbars with CMOS logic — **10⁴ synapses/μm²** projected.
- Enables **brain-scale** on-chip networks (100B synapses) without off-chip memory.

### 7.2 Photonic Neuromorphic Computing

- **Light-based** neuron/synapse operations at **speed of light**, with massive WDM parallelism.
- MIT, Stanford, AIM Photonics: silicon photonic neurons demonstrated with **>100 GHz** bandwidth.
- Challenges: loss, noise, reconfigurability, footprint — 5–10 years from practical deployment.
- Potential: **10⁴–10⁶× energy efficiency** vs. electronic for specific matrix operations.

### 7.3 Quantum-Neuromorphic Hybrid Systems

- Quantum annealing (D-Wave) + neuromorphic readout for combinatorial optimization.
- Quantum-enhanced SNN training: variational quantum circuits as surrogate gradient approximators.
- Research stage (2025–2026): proof-of-concept demonstrations at <50 qubit scale.
- Long-term: quantum superposition for massive parallel exploration of SNN weight space.

### 7.4 Self-Organizing Neural Architectures

- **Neural Architecture Search (NAS) for SNNs**: automated discovery of efficient spiking topologies.
- **Growth-based approaches**: networks that structurally adapt during operation (adding/pruning neurons/synapses).
- **Neuromodulation-inspired**: global chemical/signal modulation for dynamic reconfiguration of network function.
- Aligns with AMOS invariants for real-time adaptation (AGENTS invariant §9).

### 7.5 Convergence with Other Frontiers

| Frontier | Convergence Point | Timeline |
|---|---|---|
| **Edge AI / TinyML** | Neuromorphic chips as TinyML accelerators | Now (2025–2026) |
| **Autonomous vehicles** | DVS + neuromorphic processors for real-time perception | 2026–2028 |
| **BCI / Neuroprosthetics** | SpiNNaker/BrainScaleS for neural interface decoding | 2027–2030 |
| **Federated learning** | On-chip neuromorphic adaptation + federated aggregation | 2026–2028 |
| **Scientific computing** | Brain-scale simulation for computational neuroscience | 2028–2032 |
| **AGI research** | Brain-inspired architectures as substrate for general intelligence | Speculative (>2030) |

---

## Appendix — Key References & Resources

- Intel Loihi 2/3 research: [Intel INRC](https://www.intel.com/neuromorphic) — 128-core, 1.2B synapses
- IBM NorthPole: IBM Research, ISSCC 2023, Nature 2023 — 128-core, 256 TOPS/W
- BrainChip Akida: commercial Edge AI neuromorphic processor — <1 mW inference
- SpiNNaker 2: University of Manchester, EU Human Brain Project — 2M cores target
- BrainScaleS-2: Heidelberg University, EBRAINS — analog accelerated, 1000× biological time
- Prophesee Metavision: leading DVS event camera — 4.5 Mpixels
- Lava framework: Intel's neuromorphic software stack — [Lava GitHub](https://github.com/lava-nc/lava)
- Norse: PyTorch SNN framework — [Norse GitHub](https://github.com/norse/norse)
- snnTorch: Teaching-friendly SNN framework — [snnTorch GitHub](https://github.com/Jespy96/snnTorch)

See also: [[22_RESEARCH/FRONTIER_TECH_RESEARCH_MOC|Frontier Tech Research MOC]] · [[22_RESEARCH/22_RESEARCH_MOC|Research MOC]] · [[00_ROOT/00_ROOT_MOC|Root MOC]]
