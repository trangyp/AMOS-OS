---
date: 2026-09-04
epistemic_class: SOURCE_CLAIM
rscf:
  claim_class: SOURCE_CLAIM
  confidence_ceiling: 0.95
  freshness: 2026-09-04
  provenance: arxiv_web_search_2026-09-04
  scope: AMOS_research_knowledge
  state: DERIVED
tags:
- sota
- arxiv
- bci
- ai
- quantum
- photonic
- neuromorphic
- research
- rscf/digest
title: SOTA Digest — BCI / AI / Quantum / Photonic (2026-09-04)
type: research_digest
---
# SOTA Digest — BCI / AI / Quantum / Photonic (2026-09-04)

> **Epistemic status:** SOURCE_CLAIM compiled from public arXiv preprints and web search. These are third-party research claims, not AMOS canon. All technical numbers trace to the cited paper IDs. `DOCUMENTED != IMPLEMENTED` applies.

## Brain-Computer Interfaces & Neural Speech Decoding

| arXiv ID | Title | Key claim | AMOS relevance |
|---|---|---|---|
| [2605.24313](https://arxiv.org/abs/2605.24313) | End-to-End Intracortical Speech Decoding from Neural Activity | Conformer decoder reaches 23.80% CER on held-out ALS data *without* an external language model. | Validates `C04` neural decoding / `C05` cognition bridge; supports on-device decoder design that reduces memory/latency. |
| [2603.20246](https://arxiv.org/abs/2603.20246) | Decoding the decoder: Contextual sequence-to-sequence modeling for intracortical speech decoding | Seq2seq + Neural Hammer & Scalpel (NHS) calibration: 14.3% PER, 19.4% WER with rescoring on Willett dataset. | `05_COGNITIVE_ORGANISM` sensor-to-symbol pipeline; day-specific nonstationarity handling for runtime calibration. |
| [2604.16441](https://arxiv.org/abs/2604.16441) | iPhoneme: Brain-to-Text Communication for ALS Using ConformerXL Decoding | 192.9M-param ConformerXL + chorded gaze/silent-speech input; 92.14% phoneme accuracy, 73.39% word accuracy, 180 ms CPU latency. | Human-computer interaction / multimodal input fusion; `15_INTERFACES` accessibility pattern. |
| [2609.02887](https://arxiv.org/abs/2609.02887) | A Common Measure of Communication for Speech Brain-Computer Interfaces | Proposes open-vocabulary mutual information (OVMI) to compare heterogeneous speech BCI systems. | `11_KNOWLEDGE` metrics canon; replaces single-WER benchmarking with information-theoretic communication capacity. |
| [2603.13321](https://arxiv.org/abs/2603.13321) | BrainWhisperer: Leveraging Large-Scale ASR Models for Neural Speech Decoding | Fine-tunes Whisper on MEA recordings; uses pretrained ASR encoder for cross-participant neural speech decoding. | `06_AGENTS` / `13_MODELS` cross-subject transfer and foundation-model reuse. |

## Quantum Error Correction & Quantum Computing

| arXiv ID | Title | Key claim | AMOS relevance |
|---|---|---|---|
| [2607.05814](https://arxiv.org/abs/2607.05814) | Latency-Constrained Hardware-Aware QEC Co-Design with Adaptive Confidence-Gated Neural Decoding | Neural fast-path + MWPM refinement: 99.81% logical accuracy, 4.6×10⁵ samples/s on CPU, only 3.3–6.2% of syndromes escalated. | `02_KERNEL` deterministic decoding throughput; `18_SECURITY` confidence-gated escalation pattern. |
| [2608.27682](https://arxiv.org/abs/2608.27682) | Logical Neural Belief Propagation for Linear-Complexity Decoding of Surface Codes | L-NBP matches BP-OSD/MWPM with linear complexity; threshold 17.5% depolarizing noise. | `C03` quantum analog / `C02` compute complexity; scalable decoder for fault-tolerant OS error correction. |
| [2607.20060](https://arxiv.org/abs/2607.20060) | Physics-Informed Graph-Neural Decoding of the Surface Code | Discrete Poisson solver on syndrome graph; logical signal as exact topological pairing; closed-form scalar readout. | `C03` physics-cosmos / `C10` engineering; interpretable topological signal for QEC. |
| [2608.02030](https://arxiv.org/abs/2608.02030) | ZeroG: A Pre-Decoder-Aware Decoder for Quantum Error Correction | Stochastic approximate MWPM for sparse residual syndromes; 10× latency improvement, <350 ns worst-case at d≤15. | Real-time QEC under `04_RUNTIME` latency constraints; `10_MEMORY` sparse-error budget. |
| [2605.04892](https://arxiv.org/abs/2605.04892) | Real-time Surface-Code Error Correction Using an FPGA-based Neural-Network Decoder | FPGA NN decoder on superconducting processor: 550 ns closed-loop latency (124 ns NN), 1.25 µs QEC cycle. | `14_TOOLS` FPGA/hardware-software co-design; deterministic feedback for quantum control. |

## Multi-Agent AI & Agent Swarms

| arXiv ID | Title | Key claim | AMOS relevance |
|---|---|---|---|
| [2608.30661](https://arxiv.org/abs/2608.30661) | SwarmBench: Can Large Language Models Act as Agent Swarm Orchestrators? | Benchmark for LLM swarm orchestration; proposes SwarmExp (experience extraction + replay) to improve orchestration. | `06_AGENTS` / `07_SKILLS` swarm governance; `19_TESTS` benchmark design. |
| [2608.17282](https://arxiv.org/abs/2608.17282) | DeAR: Decentralized Agentic Reasoning via Capability Grounding and Collaborative Thought Navigation | Peer-to-peer agent reasoning with capability grounding, thought-map navigation, topology update; beats centralized baselines on 9 multimodal benchmarks. | `03_CONTROL_PLANE` decentralized routing; `25_COGNITIVE_MATRIX` capability-grounding contract. |
| [2608.26081](https://arxiv.org/abs/2608.26081) | SwarmWorld: Stigmergic technological evolution in societies of language-model agents | Homogeneous LLM agents self-organize into technological societies in a spatial simulator; stigmergic artifact construction. | `06_AGENTS` emergent social intelligence / `C06` culture; `05_COGNITIVE_ORGANISM` environment-cognition loop. |
| [2609.01870](https://arxiv.org/abs/2609.01870) | ArcticSwarm: Deferring Early Consensus in Long-Horizon Multi-Agent Research | Separates evidence gathering from integration; gated isolation prevents early consensus; 82.6% BrowseComp-Plus with Qwen 3.5-27B. | `11_KNOWLEDGE` research synthesis; `03_CONTROL_PLANE` consensus/commit boundary. |
| [2607.27942](https://arxiv.org/abs/2607.27942) | Scaling LLM-Driven Multi-Agent Systems: Design Principles and Architectural Scalability Analysis | Four design principles (simplicity, elastic feedback, sequential workflows with optional loops, summary-based communication); linear cost growth with intermediate-complexity peak. | `06_AGENTS` / `21_DOMAINS` MAS architectural MECE guidance; consistency and evaluation standardization gaps. |

## Photonic / Neuromorphic Computing

| arXiv ID | Title | Key claim | AMOS relevance |
|---|---|---|---|
| [2607.26016](https://arxiv.org/abs/2607.26016) | MDTransformer: Mode-Division Photonic Transformer Accelerator | Mode-division optical dataflow + inverse-designed coherent crossbar; 40.4% area reduction, 63.6% power saving vs. prior PTAs. | `C10` hardware-software co-design; `13_MODELS` efficient transformer inference. |
| [2604.02429](https://arxiv.org/abs/2604.02429) | Photonic convolutional neural network with pre-trained in situ training | All-optical CNN on silicon photonics; 94% MNIST accuracy; 100–242× better energy efficiency than GPUs. | `C10` photonic compute / `C02` efficient inference. |
| [2604.16228](https://arxiv.org/abs/2604.16228) | TRON: Trainable, architecture-reconfigurable random optical neural networks | Multi-scattering medium + DMD learnable matrix multiplier; in-situ NAS directly on optics. | `13_MODELS` reconfigurable optical hardware; `C10` fabrication flexibility. |
| [2605.23051](https://arxiv.org/abs/2605.23051) | General-Purpose Photonic Computing Primitive for Contemporary AI | DUET: dynamic universal encoding tensor core with VODICs; full-range signed operands; validated on classification, segmentation, Transformer generation. | `C10` general-purpose photonic AI accelerator; `13_MODELS`/ `16_SCHEMAS` tensor encoding. |
| [2603.07174](https://arxiv.org/abs/2603.07174) | Scalable optical neural network with nonlocally coupled coherent photonic processor | Multiport directional couplers + nonlocal coherent coupling; 3N phase shifters for N-dimensional unitary. | `C10` scalable optical MVM / `C02` matrix computation. |

## Cross-domain AMOS observations

- **BCI → AI bridge**: foundation ASR models (Whisper) are being repurposed as neural feature encoders, blurring the line between acoustic and neural representation spaces. This maps to `05_COGNITIVE_ORGANISM` multimodal perception and `15_INTERFACES` human-AI interaction.
- **AI → Quantum bridge**: LLM-based decoders and swarm orchestrators are entering real-time QEC loops. `03_CONTROL_PLANE` latency/commit boundaries and `18_SECURITY` confidence-gated escalation are directly applicable.
- **Photonic compute → AI efficiency**: optical accelerators are moving from narrow MNIST demos to Transformer-class workloads. `10_MEMORY`/ `16_SCHEMAS` must account for analog precision, sign representation, and hardware-aware training.
- **Measurement canon**: OVMI in speech BCI is an example of `11_KNOWLEDGE` metrics needing information-theoretic normalization before cross-system comparison — analogous to RSCF confidence ceilings.

## Gaps and next steps

- **EMPIRICAL**: None of the above has been independently reproduced by AMOS. Reproduction status = UNKNOWN/GAP.
- **IMPLEMENTATION**: Hardware-aware QEC and photonic accelerators require executable bindings to `04_RUNTIME` and `14_TOOLS` that are not yet present.
- **CANON**: These papers are SOURCE_CLAIM, not `01_CANON`. Any canon promotion requires governed ingestion through `amos-knowledge-research-master` / `arxiv-rscf-compiler`.

---

**MOC:** [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]] · [[22_RESEARCH/01_PAPERS/ARXIV_BRIDGE_2026_QUANTUM_COMPUTING_MEMORY_SENSING|Quantum Memory Sensing Bridge]] · [[22_RESEARCH/SOTA_QUANTUM_ERROR_CORRECTION_BREAKTHROUGHS_2026|SOTA QEC 2026]]