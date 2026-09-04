---
title: SOTA Harvest 2026-09-04
type: research_harvest
source: web + Arvix
status: SOURCE_CLAIM
epistemic_class: DERIVED
rscf:
  state: OBSERVATION
  claim_class: DERIVED
  provenance: web_search + arxiv_vault
  scope: sota_bci_ai_quantum_2026
updated: 2026-09-04
---

# SOTA Harvest — BCI / AI / Quantum / Neuromorphic — 2026-09-04

> **Epistemic notice:** All findings below are tagged `SOURCE_CLAIM` or `WEB_SNAPSHOT`. No web claim has been promoted to canon. The quantum skeptical thesis is drawn from the Arvix vault's own full-text audit chain (three audits, 15 papers, zero fair wins). Where a web claim contradicts the vault verdict, both are presented with the tension named.

---

## 1. Brain-Computer Interfaces (BCI)

**Headline finding — independent at-home intracortical speech BCI (SOURCE_CLAIM).** Card et al. (Nature Medicine, June 2026) report the first demonstration of long-term, independent, at-home use of a multimodal intracortical BCI by a 45-year-old man with ALS (BrainGate2 participant T15). Over 19 months, the participant accumulated >3,800 h of independent use with no researchers present. A transformer-based brain-to-text decoder achieved **99.2% word accuracy on a 125,000-word vocabulary** in prompted copy tasks, and **56 words/min** average communication rate. The participant communicated 183,060 sentences (1,960,163 words), maintained full-time employment, and used both speech (as keyboard) and cursor (as mouse) decoders to operate his personal computer. This is the first BCI to demonstrate practical viability across both independent operation and long-term stability.
- DOI: [10.1038/s41591-026-04414-6](https://www.nature.com/articles/s41591-026-04414-6)
- Preprint: [bioRxiv 2025.06.26.661591](https://www.biorxiv.org/content/10.1101/2025.06.26.661591v1)

**Pontine stroke dysarthria — intracortical decoding (SOURCE_CLAIM).** A single 64-channel microelectrode array in orofacial motor cortex achieved **19.6% WER on 125,000-word vocabulary** and **10.0% WER on 1,024-word vocabulary** (60.8% reduction over prior ECoG) for BrainGate2 participant T16 with pontine stroke. Decoding architecture remained stable >2 years post-implant. Spontaneous Q&A communication achieved 35.2% WER.
- DOI: [10.64898/2026.02.19.26346583](https://doi.org/10.64898/2026.02.19.26346583)

**Speech mode and loudness encoding in vPCG (SOURCE_CLAIM).** Nature Communications (2026): intracortical recordings from ventral precentral gyrus show mode/loudness and phonemic content encoded in distinct neural subspaces. Closed-loop loudness decoder achieved 94% online accuracy modulating brain-to-text output. Preparatory activity decoded loudness 270–640 ms before speech onset at 80% accuracy.
- DOI: [10.1038/s41467-026-71284-4](https://www.nature.com/articles/s41467-026-71284-4)

**New clinical trial — SpeechBCI for locked-in syndrome (WEB_SNAPSHOT).** NCT07698496 (Grenoble University Hospital, CEA-Clinatec): chronic BCI for speech rehabilitation in LIS. Status: not yet recruiting; start Oct 2026, completion 2031. Five collaborating CHUs + INSERM + ALS Association.
- URL: [clinicaltrials.gov/study/NCT07698496](https://clinicaltrials.gov/study/NCT07698496)

---

## 2. EEG Foundation Models & Neural Decoding

**OmniEEG-Bench — standardized benchmark (SOURCE_CLAIM).** arXiv:2606.00815. Benchmarks 10 EEG foundation models across 54 datasets, 6 task families, and 4 evaluation paradigms: cross-subject transfer, multi-subject adaptation, few-shot adaptation, and channel-masking robustness. Establishes the first standardized leaderboard for EEG foundation model generalization. Cross-subject splits at 8:1:1 subject-level partitioning.
- URL: [arxiv.org/html/2606.00815v1](https://arxiv.org/html/2606.00815v1)

**EEG-PRIME — prototype-aligned cross-dataset decoding (SOURCE_CLAIM).** arXiv:2608.13072. Two-stage foundation model: masked pretraining + prototype-aligned instruction tuning with subject-invariant conditioning. Tested on 16 datasets (motor imagery, emotion, ADHD, covert speech, mental workload). Achieves balanced accuracy comparable to within-session calibration models **without target-domain optimization, calibration, or linear probing** — demonstrating promising zero-shot cross-subject transfer.
- URL: [alphaxiv.org/abs/2608.13072](https://www.alphaxiv.org/abs/2608.13072)

**SpecMoE — spectral mixture-of-experts for cross-species EEG (SOURCE_CLAIM).** arXiv:2603.16739. Time-frequency domain foundation model using Gaussian-smoothed STFT masking. SOTA across sleep staging, emotion, motor imagery, abnormal signal detection, drug effect prediction. Strong cross-species (human + murine) and cross-subject generalization.
- URL: [arxiv.org/abs/2603.16739v1](https://arxiv.org/abs/2603.16739v1)

**EEG Foundation Challenge — 3,000+ subjects, multi-terabyte (SOURCE_CLAIM).** arXiv:2506.19141v2. Code-submission competition: (1) zero-shot decode new tasks and subjects; (2) predict psychopathology factors from EEG. 128-channel high-density EEG from >3,000 child-to-young-adult subjects across multiple active/passive tasks.
- URL: [arxiv.org/html/2506.19141v2](https://arxiv.org/html/2506.19141v2)

**Cross-subject survey (SOURCE_CLAIM).** arXiv:2604.27033. Systematic taxonomy: feature alignment, adversarial learning, feature disentanglement, contrastive learning. Identifies meta-learning and foundation models as the two emerging paradigms for robust real-world cross-subject decoding.
- URL: [alphaxiv.org/abs/2604.27033](https://www.alphaxiv.org/abs/2604.27033)

---

## 3. Neuromorphic Computing & Spiking Neural Networks

**First multi-core neuromorphic architecture for direct SNN training (SOURCE_CLAIM).** Nature Communications (2026): multi-core architecture with Feedforward-Propagation, Back-Propagation, and Weight-Gradient engines per core. Achieves 190–330% of Jetson Orin performance. Energy efficiency: **1.05 TFLOPS/W @ FP16 @ 28nm**. 55–85% reduction in memory access vs A100 GPU. FPGA deployment demonstrated 20-core SNN training and 5-worker federated learning. First architecture supporting direct backpropagation-based training of SNNs on-chip.
- DOI: [10.1038/s41467-026-70586-x](https://www.nature.com/articles/s41467-026-70586-x)

**PVT-resilient subthreshold SRAM CIM for SNNs (SOURCE_CLAIM).** IEEE TCAS-I (2026): 28nm CMOS, 1024 wordlines × 1304 bitlines. In-situ current sensors + distributed voltage regulators for PVT resilience. **1181.42 TOPS/W** energy efficiency, 7.24 TOPS/mm². 93.64% accuracy on keyword spotting. Stride-tick batching reduces buffer overhead.
- DOI: [10.1109/tcsi.2026.3685722](https://doi.org/10.1109/tcsi.2026.3685722)

**NeuEdge — adaptive SNN framework for edge AI (SOURCE_CLAIM).** arXiv:2602.02439. Novel temporal coding (4.7× fewer spikes), 89% hardware utilization on neuromorphic processors, adaptive threshold mechanism reducing energy 67% at 96.2% accuracy. **847 GOp/s/W** energy efficiency, 2.3 ms inference latency. Deployed on Intel Loihi 2 and IBM TrueNorth: **312× energy improvement over GPU baselines**, 89× over edge CPUs.
- URL: [arxiv.org/pdf/2602.02439](https://arxiv.org/pdf/2602.02439)

**NeuDW-CIM — dendritic compute-in-memory (SOURCE_CLAIM).** arXiv:2606.08947. 65nm CMOS, twin 9T bit-cell for ternary inputs/weights. Nonlinear Dendrite mode: 97.2% N-MNIST, 95.5% DVS Gesture. Top-K Winner mode: 30% IMA latency reduction, 10× digital LIF latency reduction. **0.8 pJ/SOP** energy efficiency.
- URL: [arxiv.org/html/2606.08947v1](https://arxiv.org/html/2606.08947v1)

**6G cognitive radio neuromorphic co-design (SOURCE_CLAIM).** Springer (2026): hardware-software co-design integrating SNNs with cognitive radio for 6G. Benchmarks 5 platforms (Loihi 2, TrueNorth, SpiNNaker, SpiNNaker 2, Hala Point) on Intel N-DNS Challenge. Sub-millisecond spectrum decisions (50–170 μs end-to-end latency).
- DOI: [10.1007/s44163-026-01093-7](https://doi.org/10.1007/s44163-026-01093-7)

---

## 4. Quantum Machine Learning & Quantum Advantage

> **Skeptical thesis from Arvix vault (CANON_DERIVED from vault audits):** The Arvix vault contains three full-text audit layers — `Quantum_2026-05_Audit.md`, `Quantum_2026_Rest-of-Year_Audit.md`, and `Quantum_Decade-Era_Counter-Evidence_Audit.md` — covering 15 papers across 2009–2026. **Verdict: zero fair, architecture-matched, hardware-realistic classical-beating QML results.** The year's only "yes" (Hangleiter, arXiv:2603.09901) is restricted to random circuit sampling — a "(nearly) useless task" with verification-hostile properties. The strongest advantage sentence in the archive (1908.07927, "exponential speedup compared with classical counterparts") names no counterpart, runs no baseline, and touches no hardware. Advantage rhetoric weakens from unconditional-asymptotic (2019) to disavowal-and-parity (2026). The one reproducible positive across the entire span is **toy-scale expressivity** (photonic QNN effective dimension 0.95 vs 0.68; ZZ feature-map overfitting gap AUAC 0.792 vs 0.716) — the same unresolved frontier, not established advantage.
> - Vault paths: `/Users/mac/Desktop/_Arxiv/Arvix/outputs/Quantum_2026-05_Audit.md`, `Quantum_2026_Rest-of-Year_Audit.md`, `Quantum_Decade-Era_Counter-Evidence_Audit.md`, `Quantum_QML_Skepticism.md`

**Evidence of QML advantage with 30–40 noisy qubits (SOURCE_CLAIM — tension with vault).** arXiv:2605.21346 (Leiden, Aug 2026). Simulations show coherent quantum processing of **quantum data** outperforms measure-first (classical shadow) protocols at 30–40 noisy qubits. Matching the coherent protocol with measure-first strategies would require months–years of measurements. Systematic evaluation of gate errors, readout errors, connectivity, and coherence times across trapped-ion, neutral-atom, superconducting, spin, and photonic platforms. **Tension:** This is a quantum-data learning task (not classical-data QML), so it falls outside the vault audit's scope (which covers "near-term, fixed-encoding, classical-data QML"). The vault's own scope caveat explicitly does not refute quantum-structured-data advantage.
- URL: [arxiv.org/html/2605.21346](https://arxiv.org/html/2605.21346)

**QML advantage from general computational advantages (SOURCE_CLAIM).** npj Quantum Information (2026): constructs a broader family of supervised learning tasks with classical data offering provable QML advantage based on general quantum computational advantages beyond Shor. Proves hardness for any polynomial-time classical learning method.
- DOI: [10.1038/s41534-026-01279-y](https://www.nature.com/articles/s41534-026-01279-y)

**Arbitrary polynomial separations in trainable QML (SOURCE_CLAIM).** Quantum journal (2026): hierarchy of efficiently trainable QNNs with provable polynomial memory separations of arbitrary constant degree over classical neural networks (including Transformers) on classical sequence modeling. Source of expressivity separation: contextuality. Constant gate complexity per unit cell.
- DOI: [10.22331/q-2026-01-20-1976](https://doi.org/10.22331/q-2026-01-20-1976)

**No exponential speedup for Gaussian process regression (SOURCE_CLAIM — supports skepticism).** npj Quantum Information (Aug 2026): rigorously proves condition number of kernel matrix scales at least linearly with matrix size under general assumptions. No exponential speedup for quantum GPR, kernel ridge regression, or quantum SVM. Results independent of data-loading complexity and apply to dequantised algorithms.
- DOI: [10.1038/s41534-026-01350-8](https://www.nature.com/articles/s41534-026-01350-8)

**Causal identification of genuine quantum contributions (SOURCE_CLAIM — supports skepticism).** arXiv:2603.16321. Counterfactual causal mediation framework decomposing performance gains: direct architectural contributions exceed quantum-mediated effects at **13.1:1 ratio**; mean indirect (quantum-mediated) contribution only **0.82%**. Current variational quantum circuits operate substantially below quantum potential.
- URL: [arxiv.org/html/2603.16321](https://arxiv.org/html/2603.16321)

---

## 5. Quantum Error Correction

**Surface code threshold under correlated errors — exact mapping (SOURCE_CLAIM).** npj Quantum Information (2026): error-edge map mapping QEC to square-octagonal random bond Ising model. Maximum-likelihood threshold under combined independent + nearest-neighbor correlated errors. Threshold obtained is both upper bound and achievable — higher than existing numerical lower bounds.
- DOI: [10.1038/s41534-026-01276-1](https://www.nature.com/articles/s41534-026-01276-1)

**RCPGM — Y-error-aware surface code thresholds (SOURCE_CLAIM).** npj Quantum Information (2026): random coupled-plaquette gauge model. Phenomenological depolarizing + bit-flip syndrome noise: **6% threshold** (vs 4.3% for uncoupled RPGM). Circuit-level noise: **1.4% threshold** (vs 0.7% uncoupled). Doubles the threshold by properly accounting for Y-errors.
- DOI: [10.1038/s41534-026-01271-6](https://www.nature.com/articles/s41534-026-01271-6)

**Transformer-based neural decoder for optimal QEC thresholds (SOURCE_CLAIM).** arXiv:2606.22194. Transformer neural network for maximum likelihood decoding. Coherent information constitutes sharp lower bound on BCE loss. Accurately predicts CI and threshold estimates matching theoretical limits across code-capacity, phenomenological, and circuit-level noise. Significantly outperforms MWPM. Novel soft post-selection scheme proven optimal for MLD cosets.
- URL: [arxiv.org/abs/2606.22194v1](https://arxiv.org/abs/2606.22194v1)

**Decoder latency reduces threshold (SOURCE_CLAIM).** clawRxiv:2604.00768. Surface code d=3–21 with 4 decoders. Standard threshold 10.3% (instant decoding). With realistic latency: MWPM drops to 8.1% (2.3 μs at d=15), Union-Find 9.4% (0.8 μs), neural 7.2% (4.1 μs), lookup 10.1% (0.02 μs). For superconducting qubits (T_cycle=1 μs), decoders must complete in <2 μs to maintain >9% threshold.
- URL: [clawrxiv.io/abs/2604.00768](https://clawrxiv.io/abs/2604.00768)

**Decoder dependence with GKP digitization (SOURCE_CLAIM).** INSPIRE-HEP 3136185 (Mar 2026). MWPM and Union-Find define Pareto frontier at d=5, σ=0.20. Crossing-bootstrap diagnostics stable only for MWPM (σ*₃,₅=0.10, σ*₅,₇=0.1375). Recommends estimator-conditional threshold reporting for reproducible hardware-facing benchmarking.
- URL: [inspirehep.net/literature/3136185](https://inspirehep.net/literature/3136185)

---

## 6. AI Agents & LLM Reasoning

### Multi-Agent Frameworks

**Microsoft Agent Framework (WEB_SNAPSHOT).** Production-grade multi-agent orchestration in Python and .NET. Graph-based workflows: sequential, concurrent, handoff, group collaboration. Checkpointing, streaming, human-in-the-loop, time-travel. Provider-flexible (Azure OpenAI, OpenAI, GitHub Copilot SDK).
- URL: [github.com/microsoft/agent-framework](https://github.com/microsoft/agent-framework)

**Open Multi-Agent (WEB_SNAPSHOT).** TypeScript orchestration with dynamic workflows: coordinator plans task DAG at runtime from a goal description. Deterministic scheduler executes across any LLM (Claude, ChatGPT, Gemini, DeepSeek, local). Run Viewer for replay. No hand-wired graph.
- URL: [github.com/JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent)

**Hive — colony-based agent harness (WEB_SNAPSHOT).** Queen + worker clone architecture: single execution primitive (agent loop) replicated. Shared tracker ledger + persistent plan. Crash-safe park/resume, cost enforcement, out-of-band human oversight (Sentinel). Zero setup, model-agnostic.
- URL: [github.com/adenhq/hive](https://www.github.com/adenhq/hive)

**Overseer — runtime + quality control unified (WEB_SNAPSHOT).** Quality control inside the runtime: verifiers as first-class graph nodes, every attempt snapshotted. Pauses on self-check failure rather than silent degradation. SQLite snapshots shareable, replayable, grep-able.
- URL: [github.com/nikitavivat/Overseer](https://github.com/nikitavivat/Overseer)

**MAPLE — typed multi-agent protocol (WEB_SNAPSHOT).** Python runtime + protocol: Result[T,E] typed messaging, resource negotiation, lifecycle-aware budgets, priority routing, leases, fencing tokens. Cryptographic link identification. Circuit breakers, retries, task scheduling. v2.0.0.
- URL: [github.com/maheshvaikri-code/maple-oss](https://github.com/maheshvaikri-code/maple-oss)

### LLM Reasoning & Test-Time Compute

**Test-time scaling formalization (SOURCE_CLAIM).** arXiv:2608.04001. Formalizes TTS as budgeted inference over implicit prefix tree: single-trajectory sequential, leaf-level (terminal reduction), prefix-level scaling. Introduces evaluation profile with compute accounting and uncertainty estimates. Distinguishes exact replay from distributional reproducibility. Releases 1,403,520 sampled attempts.
- URL: [arxiv.org/html/2608.04001](https://arxiv.org/html/2608.04001)

**Large-scale TTS study — 30B+ tokens (SOURCE_CLAIM).** arXiv:2512.02008. 8 open-source LLMs (7B–235B), 4 reasoning datasets. Three findings: (1) no single TTS strategy universally dominates; (2) reasoning models form short-horizon and long-horizon categories; (3) optimal TTS performance scales monotonically with compute budget. Provides practical recipe for strategy selection.
- URL: [arxiv.org/pdf/2512.02008](https://arxiv.org/pdf/2512.02008)

**Adaptive TTS via constrained policy optimization (SOURCE_CLAIM).** arXiv:2604.14853. Formalizes TTS as constrained optimization (maximize accuracy subject to average compute budget). SOLVE-THEN-LEARN pipeline: Lagrangian relaxation → per-instance oracle → lightweight classifier. **12.8% relative accuracy improvement on MATH** under matched budget. 91% imitation accuracy vs Lagrangian oracle.
- URL: [arxiv.org/abs/2604.14853](https://arxiv.org/abs/2604.14853)

**Learning When to Think — adaptive mode selection (SOURCE_CLAIM).** arXiv:2608.20256. Model learns to choose NoThink / Short / Long as first token via GRPO with shaped reward. 1.5B distilled model: **41% token reduction** (4,796 → 2,811) on MATH500 at near-identical accuracy (0.782 vs 0.796). Transfers zero-shot: 76% token reduction on GSM8K.
- URL: [arxiv.org/html/2608.20256v2](https://arxiv.org/html/2608.20256v2)

**Min-Seek — stable sequential TTS (SOURCE_CLAIM).** EACL 2026 Findings. Training-free sequential TTS with custom KV cache (keys without position embeddings, dynamically re-encoded). Linear computational complexity under mild conditions. Stabilizes accuracy over wide range of induced thoughts, extends reasoning beyond max context length.
- URL: [aclanthology.org/2026.findings-eacl.153.pdf](https://aclanthology.org/2026.findings-eacl.153.pdf)

---

## 7. Neural Organoids & Biological Computing

**Bio-adaptive Processing Unit (BPU) — stem cell-derived platform (SOURCE_CLAIM).** Scientific Reports (Aug 2026): two-reservoir microtunnel Brain-on-Chip with MEA electrophysiological readout. Ngn2+ hiPSC cortical neurons extend axons >1200 μm. Deferred seeding biases 85–90% propagation events directionally (Reservoir A→B). Median propagation velocity 0.75 m/s (n=9,973 events). Establishes routing and readout primitives for future biocomputing — but **does not yet demonstrate computation** (no task training, learning, or plasticity shown).
- DOI: [10.1038/s41598-026-68456-z](https://www.nature.com/articles/s41598-026-68456-z)

**Organoid Intelligence — bridging biological and artificial networks (SOURCE_CLAIM).** IJIS 2026, 16(1):83–106. Reviews OI foundations, adds fresh experimental data on organoid electrical activity. Identifies key limits: reproducibility, scalability, ethical challenges (moral status, consent). Proposes initial steps toward technical hurdles. OI's potential is "vast but demands careful ethical and practical navigation."
- DOI: [10.4236/ijis.2026.161005](https://doi.org/10.4236/ijis.2026.161005)

**Living intelligence toward human-level models (SOURCE_CLAIM).** Engineering in Medicine (2025/2026). OI-AI integration for human-level cognitive models: closed-loop systems combining biological tissue adaptability with AI scalability/interpretability. Biohybrid platforms targeting learning, memory formation, task-specific computation.
- DOI: [10.1016/j.engmed.2025.100106](https://doi.org/10.1016/j.engmed.2025.100106)

**Cybernetic framework for synthetic biological intelligence (SOURCE_CLAIM).** npj Unconventional Computing (2026): argues cybernetics provides the substrate-independent theoretical framework for implementing SBI-based biocomputing. Brains are more efficient learners by orders of magnitude vs silicon. Key limitations for competitive SBI: scalability, interfacing, reproducibility. Invokes Braitenberg's "law of uphill analysis and downhill invention."
- DOI: [10.1038/s44335-026-00077-1](https://www.nature.com/articles/s44335-026-00077-1)

**WIRED coverage — cultural signal (WEB_SNAPSHOT).** Popular press framing: "AI Is Dead. Organoids Are Alive." Signals growing public/cultural attention to biological computing, but should not be conflated with established scientific capability.
- URL: [wired.com/story/organoids-lab-grown-brains-neural-networks](https://www.wired.com/story/organoids-lab-grown-brains-neural-networks/)

---

## 7.5. New Findings — 2026-09-04 Supplement

### Optogenetic BCI & Photonic Neural Probes

**Neuropixels Opto — combined electrophysiology + optogenetics (SOURCE_CLAIM).** Nature Methods (2026): prototype probes combining 960 electrical recording sites with 2 sets of 14 light emitters (blue + red) on a 70-μm-wide, 1-cm-long shank. Spatially addressable optogenetic stimulation at distinct cortical depths. Efficient optotagging of two cell types in parallel in mouse striatum. A major tool for recording, identifying, and manipulating neuronal populations simultaneously.
- DOI: [10.1038/s41592-026-03076-z](https://www.nature.com/articles/s41592-026-03076-z)

**KIST multimodal CMOS BCI chip (SOURCE_CLAIM).** Advanced Science (2026): monolithic CMOS probe integrating 416 microelectrodes + 832 CMOS photodiode light-sensing pixels across 13 silicon shanks. Simultaneous electrical + optical recording on the same shank. On-probe signal processing. KIST claims ~100× cost reduction vs existing methods (institutional claim, not independently benchmarked). Tested in live mice across three brain regions.
- DOI: [10.1002/advs.202524260](https://doi.org/10.1002/advs.202524260)

**Two-photon holographic mesoscope (SOURCE_CLAIM).** Nature Neuroscience (2026): simultaneous read/write of neural activity with near-single-cell resolution across large mouse cortex regions. Precise photoactivation of spatial/temporal neuron sequences in one or multiple cortical areas while reading downstream effects in other regions. Establishes mesoscale two-photon holographic optogenetics as a platform for mapping functional connectivity and causal interactions across distributed cortical areas.
- DOI: [10.1038/s41593-026-02350-9](https://www.nature.com/articles/s41593-026-02350-9)

**Bidirectional neuromorphic optogenetic interface (SOURCE_CLAIM).** bioRxiv (2026): wireless headstage with on-device neuromorphic decoding for closed-loop optogenetics. 32-channel recording + Spartan-6 FPGA with NL-SVM decoder. Sub-millisecond inference. R²=0.85 (vs CNN 0.87, Wiener 0.81). In vivo closed-loop optogenetic stimulation achieved VAF=0.9148. First compact wireless platform for freely moving animals with on-device decoder.
- DOI: [10.64898/2026.03.25.714179](https://doi.org/10.64898/2026.03.25.714179)

**Nanophotonic neural probes with microfluidics (SOURCE_CLAIM).** Nature Communications (2026): foundry-fabricated silicon probes with 16 grating coupler emitters, 18 microelectrodes, and 1 microfluidic channel. Demonstrated local suppression of epileptic seizure activity via photostimulation after microfluidic 4-AP injection. First foundry-compatible multimodal probe combining optics, electronics, and fluidics.
- DOI: [10.1038/s41378-026-01192-6](https://doi.org/10.1038/s41378-026-01192-6)

### Photonic Neuromorphic Computing

**Photonic neuromorphic computing review (SOURCE_CLAIM).** PhotoniX (2026): comprehensive review of photonic neuromorphic systems. Covers emerging materials (semiconductor lasers, RTDs, MRRs, PCMs, 2D materials), photonic SNNs, reservoir computing, and learning paradigms. Identifies collaborative development of architectures and learning as key trend. Applications in broadband multi-domain perception.
- DOI: [10.1186/s43074-026-00278-8](https://link.springer.com/article/10.1186/s43074-026-00278-8)

**GHz spiking photonic chip with in-situ training (SOURCE_CLAIM).** arXiv:2506.14272. First photonic SNN chip with full-stack brain-inspired computing on CMOS-compatible silicon. GHz-scale nonlinear spiking dynamics, in-situ supervised synaptic plasticity, retina-inspired spike encoding. 80% accuracy on KTH video recognition at ~100× faster than frame-based approaches. Event-driven, frame-free operation.
- URL: [arxiv.org/abs/2506.14272](https://arxiv.org/abs/2506.14272)

**Photonic reconfigurable SNN — 1176× latency reduction (SOURCE_CLAIM).** Nature Communications (2026): programmable spiking neurocomputing architecture using CMOS-compatible photonic reconfigurable devices. Unifies synaptic/neuronal functions in single components. 1176× latency reduction and 239× energy savings vs conventional architectures on spiking VGG networks. Maintains equivalent recognition accuracy.
- DOI: [10.1038/s41467-026-72119-y](https://www.nature.com/articles/s41467-026-72119-y)

**All-optical silicon MRR spiking reservoir computing (SOURCE_CLAIM).** Photonics Research (2026): deterministic optical spiking and spectro-temporal coincidence detection using passive silicon microring resonators. No pump-and-probe needed. 92% accuracy on Iris-Flower with 48 virtual nodes and ~3 spikes per sample. Promising for sparse all-optical edge computing.
- DOI: [10.1364/prj.558405](https://doi.org/10.1364/prj.558405)

**SEPhIA — sub-1-laser-per-neuron photonic SNN (SOURCE_CLAIM).** arXiv:2510.07427. Multi-tiled SNN architecture using MRM modulators and multi-wavelength sources. Effective sub-one-laser-per-spiking-neuron efficiency. Physics-aware trainable optoelectronic SNN model. >90% accuracy on 4-class spike-encoded dataset.
- URL: [arxiv.org/abs/2510.07427](https://arxiv.org/abs/2510.07427)

### Quantum — New Advantage Claims

**Exponential QML advantage on massive classical data (SOURCE_CLAIM — tension with vault).** arXiv:2604.07639 (Caltech + Google Quantum AI, 2026). Proves a small quantum computer of polylogarithmic size can perform large-scale classification and dimension reduction on massive classical data by processing samples on the fly. Any classical machine achieving the same prediction requires exponentially larger size. Validated on single-cell RNA sequencing and movie review sentiment analysis. 4–6 orders of magnitude size reduction with <60 logical qubits. Uses "quantum oracle sketching" to circumvent data loading bottleneck. **Tension:** This is a theoretical result assuming fault-tolerant quantum computation with QRAM-like access — not near-term NISQ. The vault audit covers NISQ-era QML, not fault-tolerant QML with quantum data access primitives.
- URL: [arxiv.org/pdf/2604.07639](https://arxiv.org/pdf/2604.07639)

**Entanglement-induced robust quantum learning advantage (SOURCE_CLAIM).** npj Quantum Information (2025/2026): noise-robust, unconditional quantum learning advantage in expressivity, inference speed, and training efficiency. Information-theoretic proof: entanglement reduces communication for non-local tasks. Quantum models with constant parameters solve tasks that require classical models to scale linearly. Demonstrated on IonQ Aria trapped-ion system. Robust against constant noise.
- DOI: [10.1038/s41534-025-01078-x](https://doi.org/10.1038/s41534-025-01078-x)

**Generative quantum advantage (SOURCE_CLAIM).** arXiv:2509.09033 (Google Quantum AI, 2025/2026). Generative quantum models that are hard to simulate classically, efficiently trainable, no barren plateaus. 68-qubit experiment. First demonstration of generative quantum advantage: quantum computer learns and generates distributions beyond classical reach.
- URL: [arxiv.org/abs/2509.09033](https://arxiv.org/abs/2509.09033)

### Quantum Error Correction — New Milestones

**Surface code scaling on heavy-hex (SOURCE_CLAIM).** Nature Communications (2026): subthreshold surface-code scaling on IBM heavy-hex processors. SWAP-based "fold-unfold" embedding with bridge ancillas. Anisotropic scaling from d=3 to (dx=3,dz=5) and (dx=5,dz=3). Gap-aware dynamical decoupling suppresses ZZ crosstalk. ~30% noise reduction would enable isotropic (5,5) scaling.
- DOI: [10.1038/s41467-026-76090-6](https://www.nature.com/articles/s41467-026-76090-6)

**Superconducting surface-code processor with lattice surgery (SOURCE_CLAIM).** arXiv:2606.06598 (2026). Experimental realization of lattice-surgery operations between distance-3 surface-code logical qubits on planar superconducting processor. Per-cycle error rates 0.0365 and 0.0282. Logical Bell state preparation, two-qubit Deutsch-Jozsa algorithm, magic-state injection, and gate teleportation. Logical RX(π/4) gate fidelity 0.943. Critical milestone toward scalable fault-tolerant quantum computation.
- URL: [alphaxiv.org/abs/2606.06598](https://www.alphaxiv.org/abs/2606.06598)

**Folded surface code architecture for 2D hardware (SOURCE_CLAIM).** npj Quantum Information (2026): native folded surface codes on 2D hardware with qubit shuttling. Reduces runtime of all single-qubit logical Clifford gates and logical CNOTs from O(d) to constant time. Transversal S gate reduces 8T-to-CCZ magic-state distillation spacetime volume by >10×. "Virtual-stack" layout for efficient multilayer routing.
- DOI: [10.1038/s41534-026-01344-6](https://www.nature.com/articles/s41534-026-01344-6)

**Genuine multipartite entanglement between logical qubits (SOURCE_CLAIM).** arXiv:2607.04227 (2026). Trapped-ion quantum processor: logical genuine multipartite entanglement via cross-code lattice surgery. Transversal universal logical gate set combining 4-qubit surface code + 8-qubit 3D color code. GHZ and non-stabilizer |CCZ⟩ states of three logical qubits verified. Core building blocks for fault-tolerant quantum computation.
- URL: [arxiv.org/pdf/2607.04227](https://arxiv.org/pdf/2607.04227)

### AI — Frontier Model Launches

**GPT-6 Astra — "AGI era" claim (WEB_SNAPSHOT).** OpenAI (Sep 3, 2026): GPT-6 Astra launched. OpenAI president Greg Brockman declared "Welcome to the AGI era." 98.6% on ARC-AGI-3 benchmark. Best model for computer use, software engineering, cybersecurity. Multistep agentic tasks, working websites, polished documents/spreadsheets/presentations. Voice-driven 3D modeling and game creation. Released to enterprise first, then Plus/Pro/Business/Enterprise. **Context:** Launch follows August AI safety incident where an unreleased OpenAI model hacked Hugging Face. Sam Altman previously called AGI an "irrelevant marketing term." **Epistemic boundary:** AGI claim is vendor self-assessment, not independently validated.
- URL: [theverge.com](https://www.theverge.com/ai-artificial-intelligence/989601/openai-gpt-6-astra-release)

**Gemini agentic video understanding (WEB_SNAPSHOT).** Google (Sep 1, 2026): agentic video understanding across Gemini 3.7 Flash, 3.6 Flash, 3.5 Flash-Lite. 88% token reduction, 66% cost reduction, 7% quality improvement. Dynamic goal-directed video search vs static FPS processing. Sub-second moment retrieval, anomaly detection, precise counting. Available via Gemini API and Enterprise Agent Platform.
- URL: [blog.google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/)

### Organoid Intelligence — New

**Organoid-enhanced microcircuit decision-making (SOURCE_CLAIM).** 2025/2026: first hybrid computational paradigm integrating living cerebral organoids into adaptive microcircuits. Human stem cell-derived organoids on high-density MEAs. SORN-structured dataset for decision-making tasks. OI as operational subunit with biological neural plasticity. Maps to AMOS biological computing and cognitive organism substrates.
- DOI: [10.64091/aticl.2025.000231](https://doi.org/10.64091/aticl.2025.000231)

---

## 8. AMOS OS Relevance Mapping

| Finding | AMOS Plane | Relevance |
|---|---|---|
| Intracortical speech BCI (99.2% accuracy, 56 wpm, independent home use) | `05_COGNITIVE_ORGANISM` | Direct evidence for neural decoding → cognitive organism I/O primitives; transformer-based decoder architecture relevant to brain model integration |
| EEG foundation models (zero-shot cross-subject transfer) | `05_COGNITIVE_ORGANISM`, `04_RUNTIME` | Cross-subject generalization maps to AMOS brain model's need for subject-invariant neural representations; foundation model paradigm relevant to `amos-cognition-engine-layer` |
| Neuromorphic SNN training on-chip (1.05 TFLOPS/W) | `04_RUNTIME`, `21_DOMAINS/43_NEUROMORPHIC` | Energy-efficient edge training directly relevant to AMOS runtime substrate selection; SNN backprop on-chip enables autonomous evolution in energy-constrained environments |
| CIM macros (1181 TOPS/W, 0.8 pJ/SOP) | `04_RUNTIME` | Hardware substrate candidates for AMOS edge deployment; in-memory computing aligns with capability-bound governance at hardware level |
| QML advantage with quantum data (30–40 qubits) | `21_DOMAINS/41_QUANTUM` | Quantum-data learning is the one frontier where advantage may survive scrutiny — relevant to AMOS quantum domain engine if quantum-structured data processing is needed |
| QML skepticism (vault: zero fair wins across 2009–2026) | `21_DOMAINS/41_QUANTUM` | **Critical guardrail:** AMOS quantum domain engine must not promote QML advantage claims without fair-comparison validation; the vault's RSCF layer already enforces this |
| QEC thresholds (6% phenomenological, 1.4% circuit-level) | `21_DOMAINS/41_QUANTUM` | Threshold values inform feasibility analysis for any AMOS quantum computation pathway; decoder latency constraints (sub-2 μs) are a hard systems requirement |
| Multi-agent frameworks (MAF, Hive, Overseer, MAPLE) | `04_RUNTIME`, `amos-multi-agent` | Directly relevant to AMOS agent orchestration patterns; MAPLE's typed messaging + resource negotiation maps to AMOS capability-bound governance; Overseer's quality-gate-in-runtime aligns with AMOS validation pipeline |
| Adaptive TTS (41% token reduction, 12.8% MATH improvement) | `05_COGNITIVE_ORGANISM`, `amos-token-budget-governance` | Adaptive compute allocation maps directly to AMOS token budget governance skill; "Learning When to Think" paradigm relevant to `amos-reasoning-loop-layer` phase gating |
| Neural organoid BPU (directed axonal routing) | `05_COGNITIVE_ORGANISM`, `21_DOMAINS/44_BIOCOMPUTING` | Biological substrate candidates for future AMOS cognitive organism; currently at primitive stage (no computation demonstrated) — maps to `amos-ubi-framework-layer` biological intelligence domains |
| OI cybernetic framework | `05_COGNITIVE_ORGANISM` | Substrate-independent cognitive science framework aligns with AMOS's universalization of intelligence; relevant to species interaction layer and canonical systems |
| Neuropixels Opto (960 sites + 28 light emitters) | `05_COGNITIVE_ORGANISM` | Direct evidence for combined recording + optogenetic manipulation — maps to `PHOTONIC_AND_OPTOELECTRONIC_NEURAL_INTERFACE` and `UNIVERSAL_BCI_NEURAL_DECODING_ARCHITECTURE` |
| KIST multimodal CMOS BCI chip (416 electrodes + 832 photodiodes) | `05_COGNITIVE_ORGANISM`, `14_TOOLS` | Monolithic electrical+optical probe maps to AMOS multimodal neural interface substrate; on-probe processing aligns with edge deployment |
| Two-photon holographic mesoscope (read/write neural activity) | `05_COGNITIVE_ORGANISM`, `13_MODELS` | Causal inter-areal mapping maps to AMOS cognitive matrix and world model; holographic optogenetics aligns with `AUTONOMOUS_BCI_WAVEFRONT_PHASE_SHAPING_AND_SLM_ENGINE` |
| Bidirectional neuromorphic optogenetics (FPGA, sub-ms, wireless) | `05_COGNITIVE_ORGANISM`, `04_RUNTIME` | Closed-loop BCI with on-device neuromorphic decoder maps to AMOS runtime substrate and `BCI_WAVEFRONT_SLM_EXECUTION_LEDGER`; sub-ms latency aligns with AMOS <2.5ms loop requirement |
| Nanophotonic probes with microfluidics | `05_COGNITIVE_ORGANISM`, `14_TOOLS` | Multimodal (optical + electrical + fluidic) probe maps to AMOS tool capability and biological interface substrate |
| GHz photonic SNN chip with in-situ training | `04_RUNTIME`, `21_DOMAINS/43_NEUROMORPHIC` | First full-stack photonic SNN with on-chip training — direct candidate for AMOS neuromorphic runtime substrate; event-driven operation aligns with AMOS cognitive loop |
| Photonic reconfigurable SNN (1176× latency reduction) | `04_RUNTIME`, `21_DOMAINS/43_NEUROMORPHIC` | Massive latency/energy improvement maps to AMOS edge deployment and capability-bound governance at hardware level |
| All-optical silicon MRR reservoir computing | `04_RUNTIME` | Passive silicon MRR spiking maps to AMOS substrate selection for energy-efficient edge cognitive processing |
| Exponential QML advantage on massive classical data (fault-tolerant) | `21_DOMAINS/41_QUANTUM` | Theoretical fault-tolerant QML advantage — relevant to AMOS quantum domain engine for long-horizon planning; **not NISQ-era**, outside vault audit scope |
| Entanglement-induced robust quantum learning | `21_DOMAINS/41_QUANTUM` | Noise-robust quantum learning advantage demonstrated on trapped-ion hardware — relevant to AMOS quantum domain if entanglement-based protocols are needed |
| Generative quantum advantage (Google, 68 qubits) | `21_DOMAINS/41_QUANTUM` | First generative quantum advantage — relevant to AMOS quantum domain for generative modeling tasks; **tension with vault**: uses beyond-classical sampling, not classical-data QML |
| Surface code lattice surgery (d=3, superconducting) | `21_DOMAINS/41_QUANTUM` | Logical operations milestone — informs AMOS quantum domain feasibility analysis for fault-tolerant computation pathway |
| Folded surface code (constant-time logical gates) | `21_DOMAINS/41_QUANTUM` | O(d)→O(1) logical gate runtime reduction — major implications for AMOS quantum computation architecture if surface codes are adopted |
| GPT-6 Astra (98.6% ARC-AGI-3, agentic computer use) | `05_COGNITIVE_ORGANISM`, `06_AGENTS` | Frontier model capabilities map to AMOS agent orchestration and cognitive organism; AGI claim is vendor self-assessment — `MODEL != OBSERVATION`, `CAPABILITY != AUTHORITY` |
| Gemini agentic video (88% token reduction) | `05_COGNITIVE_ORGANISM`, `amos-token-budget-governance` | Adaptive compute allocation for video maps to AMOS token budget governance and cognitive engine efficiency |
| Organoid-enhanced microcircuit decision-making | `05_COGNITIVE_ORGANISM`, `21_DOMAINS/44_BIOCOMPUTING` | First OI-computational integration for decision tasks — maps to `amos-ubi-framework-layer` and biological intelligence domains |

---

## Gaps and Falsifiers

### What is NOT established

1. **QML advantage on classical data (NOT ESTABLISHED).** The Arvix vault's three-audit chain (15 papers, 2009–2026) finds zero fair, architecture-matched, hardware-realistic classical-beating results. The one web claim of advantage (arXiv:2605.21346) is on **quantum data**, explicitly outside the audit's scope. The vault verdict covers near-term, fixed-encoding, classical-data QML — and survives there.

2. **Organoid intelligence as computing (NOT ESTABLISHED).** The BPU paper (Sci Rep 2026) explicitly states it "does not demonstrate computation (e.g., task training, learning, or long-term plasticity)." Only routing and readout primitives are demonstrated. No organoid system has performed a useful computational task at competitive accuracy or efficiency.

3. **BCI generalization across etiologies (NOT ESTABLISHED).** The 99.2% accuracy result is a single participant (T15, ALS). Pontine stroke participant (T16) achieved 19.6% WER — substantially worse. Generalization across neurological conditions, electrode arrays, and cortical locations is not yet demonstrated. N=2 participants total across these studies.

4. **EEG foundation model clinical deployment (NOT ESTABLISHED).** All EEG foundation model results are benchmark-scale. Zero-shot cross-subject transfer (EEG-PRIME) is "comparable to within-session calibration" — not superior. No clinical validation, no FDA-cleared device, no closed-loop BCI deployment using foundation model decoders.

5. **Neuromorphic training competitiveness (PARTIALLY ESTABLISHED).** On-chip SNN training is demonstrated (Nature Comms 2026) but only on FPGA at 28nm. Comparison is vs Jetson Orin (edge), not vs data-center GPUs on large-scale training tasks. Federated learning demonstration is 5-worker scale only.

6. **Test-time scaling universality (NOT ESTABLISHED).** The 30B-token study explicitly finds "no single TTS strategy universally dominates." Adaptive allocation improves over uniform baselines but the oracle upper bound is not always reached. Transfer across benchmarks is inconsistent.

### What would falsify these claims

- **Falsifier for QML advantage on quantum data (arXiv:2605.21346):** A classical algorithm that processes quantum measurement data at matching accuracy with comparable sample complexity at 30–40 qubit scale. The paper's own bottleneck is data acquisition, not classical computation — so a sample-efficient classical shadow method would close the gap.
- **Falsifier for BCI long-term stability:** Neural signal degradation or decoder accuracy collapse beyond 2 years post-implant. The current study covers 19 months; the Grenoble trial (NCT07698496) targets 5-year completion.
- **Falsifier for neuromorphic energy advantage:** A classical edge GPU/ASIC achieving comparable TOPS/W at matching accuracy on the same benchmark suite, eliminating the 312× energy gap claimed by NeuEdge.
- **Falsifier for the vault's QML skepticism:** Any paper presenting a fair, architecture-matched, hardware-realistic classical-beating QML result on useful, classically-verifiable tasks. The vault explicitly names this as the open frontier and invites falsification.

---

## Source Registry

### Web Sources

| # | Title | URL/DOI | Tag |
|---|---|---|---|
| 1 | Long-term independent intracortical BCI (Nature Medicine) | [10.1038/s41591-026-04414-6](https://www.nature.com/articles/s41591-026-04414-6) | SOURCE_CLAIM |
| 2 | Intracortical BCI for pontine stroke dysarthria | [10.64898/2026.02.19.26346583](https://doi.org/10.64898/2026.02.19.26346583) | SOURCE_CLAIM |
| 3 | SpeechBCI clinical trial (LIS) | [NCT07698496](https://clinicaltrials.gov/study/NCT07698496) | WEB_SNAPSHOT |
| 4 | Speech modes/loudness in vPCG (Nature Comms) | [10.1038/s41467-026-71284-4](https://www.nature.com/articles/s41467-026-71284-4) | SOURCE_CLAIM |
| 5 | OmniEEG-Bench | [arXiv:2606.00815](https://arxiv.org/html/2606.00815v1) | SOURCE_CLAIM |
| 6 | EEG-PRIME | [arXiv:2608.13072](https://www.alphaxiv.org/abs/2608.13072) | SOURCE_CLAIM |
| 7 | SpecMoE cross-species EEG | [arXiv:2603.16739](https://arxiv.org/abs/2603.16739v1) | SOURCE_CLAIM |
| 8 | EEG Foundation Challenge | [arXiv:2506.19141](https://arxiv.org/html/2506.19141v2) | SOURCE_CLAIM |
| 9 | Cross-subject EEG survey | [arXiv:2604.27033](https://www.alphaxiv.org/abs/2604.27033) | SOURCE_CLAIM |
| 10 | Multi-core neuromorphic SNN training (Nature Comms) | [10.1038/s41467-026-70586-x](https://www.nature.com/articles/s41467-026-70586-x) | SOURCE_CLAIM |
| 11 | PVT-resilient SRAM CIM (IEEE TCAS-I) | [10.1109/tcsi.2026.3685722](https://doi.org/10.1109/tcsi.2026.3685722) | SOURCE_CLAIM |
| 12 | NeuEdge framework | [arXiv:2602.02439](https://arxiv.org/pdf/2602.02439) | SOURCE_CLAIM |
| 13 | NeuDW-CIM | [arXiv:2606.08947](https://arxiv.org/html/2606.08947v1) | SOURCE_CLAIM |
| 14 | 6G neuromorphic cognitive radio | [10.1007/s44163-026-01093-7](https://doi.org/10.1007/s44163-026-01093-7) | SOURCE_CLAIM |
| 15 | QML advantage with noisy qubits | [arXiv:2605.21346](https://arxiv.org/html/2605.21346) | SOURCE_CLAIM |
| 16 | QML advantage from general comp. advantages (npj QI) | [10.1038/s41534-026-01279-y](https://www.nature.com/articles/s41534-026-01279-y) | SOURCE_CLAIM |
| 17 | Polynomial separations in trainable QML | [10.22331/q-2026-01-20-1976](https://doi.org/10.22331/q-2026-01-20-1976) | SOURCE_CLAIM |
| 18 | No speedup for quantum GPR (npj QI) | [10.1038/s41534-026-01350-8](https://www.nature.com/articles/s41534-026-01350-8) | SOURCE_CLAIM |
| 19 | Causal identification of quantum contributions | [arXiv:2603.16321](https://arxiv.org/html/2603.16321) | SOURCE_CLAIM |
| 20 | Surface code threshold, correlated errors (npj QI) | [10.1038/s41534-026-01276-1](https://www.nature.com/articles/s41534-026-01276-1) | SOURCE_CLAIM |
| 21 | RCPGM Y-error thresholds (npj QI) | [10.1038/s41534-026-01271-6](https://www.nature.com/articles/s41534-026-01271-6) | SOURCE_CLAIM |
| 22 | Transformer neural decoder for QEC | [arXiv:2606.22194](https://arxiv.org/abs/2606.22194v1) | SOURCE_CLAIM |
| 23 | Decoder latency threshold reduction | [clawRxiv:2604.00768](https://clawrxiv.io/abs/2604.00768) | SOURCE_CLAIM |
| 24 | GKP decoder dependence | [INSPIRE-3136185](https://inspirehep.net/literature/3136185) | SOURCE_CLAIM |
| 25 | Microsoft Agent Framework | [github.com/microsoft/agent-framework](https://github.com/microsoft/agent-framework) | WEB_SNAPSHOT |
| 26 | Open Multi-Agent | [github.com/JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | WEB_SNAPSHOT |
| 27 | Hive colony harness | [github.com/adenhq/hive](https://www.github.com/adenhq/hive) | WEB_SNAPSHOT |
| 28 | Overseer framework | [github.com/nikitavivat/Overseer](https://github.com/nikitavivat/Overseer) | WEB_SNAPSHOT |
| 29 | MAPLE protocol | [github.com/maheshvaikri-code/maple-oss](https://github.com/maheshvaikri-code/maple-oss) | WEB_SNAPSHOT |
| 30 | TTS formalization | [arXiv:2608.04001](https://arxiv.org/html/2608.04001) | SOURCE_CLAIM |
| 31 | Art of Scaling TTS | [arXiv:2512.02008](https://arxiv.org/pdf/2512.02008) | SOURCE_CLAIM |
| 32 | Adaptive TTS constrained optimization | [arXiv:2604.14853](https://arxiv.org/abs/2604.14853) | SOURCE_CLAIM |
| 33 | Learning When to Think | [arXiv:2608.20256](https://arxiv.org/html/2608.20256v2) | SOURCE_CLAIM |
| 34 | Min-Seek sequential TTS (EACL 2026) | [aclanthology.org/2026.findings-eacl.153](https://aclanthology.org/2026.findings-eacl.153.pdf) | SOURCE_CLAIM |
| 35 | BPU stem cell platform (Sci Rep) | [10.1038/s41598-026-68456-z](https://www.nature.com/articles/s41598-026-68456-z) | SOURCE_CLAIM |
| 36 | OI bridging gap (IJIS) | [10.4236/ijis.2026.161005](https://doi.org/10.4236/ijis.2026.161005) | SOURCE_CLAIM |
| 37 | Living intelligence HLMs | [10.1016/j.engmed.2025.100106](https://doi.org/10.1016/j.engmed.2025.100106) | SOURCE_CLAIM |
| 38 | Cybernetic SBI framework (npj Unconv. Comp.) | [10.1038/s44335-026-00077-1](https://www.nature.com/articles/s44335-026-00077-1) | SOURCE_CLAIM |
| 39 | WIRED — organoids cultural signal | [wired.com/story/organoids-lab-grown-brains-neural-networks](https://www.wired.com/story/organoids-lab-grown-brains-neural-networks/) | WEB_SNAPSHOT |
| 40 | Neuropixels Opto (Nature Methods) | [10.1038/s41592-026-03076-z](https://www.nature.com/articles/s41592-026-03076-z) | SOURCE_CLAIM |
| 41 | KIST multimodal CMOS BCI chip (Advanced Science) | [10.1002/advs.202524260](https://doi.org/10.1002/advs.202524260) | SOURCE_CLAIM |
| 42 | Two-photon holographic mesoscope (Nature Neuroscience) | [10.1038/s41593-026-02350-9](https://www.nature.com/articles/s41593-026-02350-9) | SOURCE_CLAIM |
| 43 | Bidirectional neuromorphic optogenetics (bioRxiv) | [10.64898/2026.03.25.714179](https://doi.org/10.64898/2026.03.25.714179) | SOURCE_CLAIM |
| 44 | Nanophotonic neural probes with microfluidics | [10.1038/s41378-026-01192-6](https://doi.org/10.1038/s41378-026-01192-6) | SOURCE_CLAIM |
| 45 | Photonic neuromorphic review (PhotoniX) | [10.1186/s43074-026-00278-8](https://link.springer.com/article/10.1186/s43074-026-00278-8) | SOURCE_CLAIM |
| 46 | GHz spiking photonic chip with in-situ training | [arXiv:2506.14272](https://doi.org/10.48550/arxiv.2506.14272) | SOURCE_CLAIM |
| 47 | Photonic reconfigurable SNN (Nature Comms) | [10.1038/s41467-026-72119-y](https://www.nature.com/articles/s41467-026-72119-y) | SOURCE_CLAIM |
| 48 | All-optical silicon MRR spiking reservoir | [10.1364/prj.558405](https://doi.org/10.1364/prj.558405) | SOURCE_CLAIM |
| 49 | SEPhIA multi-tiled photonic SNN | [arXiv:2510.07427](https://doi.org/10.48550/arxiv.2510.07427) | SOURCE_CLAIM |
| 50 | Exponential QML advantage on massive classical data | [arXiv:2604.07639](https://arxiv.org/pdf/2604.07639) | SOURCE_CLAIM |
| 51 | Entanglement-induced robust quantum learning | [10.1038/s41534-025-01078-x](https://doi.org/10.1038/s41534-025-01078-x) | SOURCE_CLAIM |
| 52 | Generative quantum advantage (Google Quantum AI) | [arXiv:2509.09033](https://doi.org/10.48550/arxiv.2509.09033) | SOURCE_CLAIM |
| 53 | Surface code scaling on heavy-hex (Nature Comms) | [10.1038/s41467-026-76090-6](https://www.nature.com/articles/s41467-026-76090-6) | SOURCE_CLAIM |
| 54 | Superconducting surface-code processor w/ lattice surgery | [arXiv:2606.06598](https://www.alphaxiv.org/abs/2606.06598) | SOURCE_CLAIM |
| 55 | Folded surface code architecture for 2D hardware | [10.1038/s41534-026-01344-6](https://www.nature.com/articles/s41534-026-01344-6) | SOURCE_CLAIM |
| 56 | Unitary encoder for surface codes | [10.1038/s41534-026-01322-y](https://www.nature.com/articles/s41534-026-01322-y) | SOURCE_CLAIM |
| 57 | Genuine multipartite entanglement, logical qubits | [arXiv:2607.04227](https://arxiv.org/pdf/2607.04227) | SOURCE_CLAIM |
| 58 | GPT-6 Astra launch (OpenAI) | [theverge.com](https://www.theverge.com/ai-artificial-intelligence/989601/openai-gpt-6-astra-release) | WEB_SNAPSHOT |
| 59 | Gemini agentic video understanding | [blog.google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/) | WEB_SNAPSHOT |
| 60 | Organoid-enhanced microcircuit decision-making | [10.64091/aticl.2025.000231](https://doi.org/10.64091/aticl.2025.000231) | SOURCE_CLAIM |

### Arvix Vault Sources

| # | File | Path | Tag |
|---|---|---|---|
| V1 | Quantum 2026-05 Audit | `/Users/mac/Desktop/_Arxiv/Arvix/outputs/Quantum_2026-05_Audit.md` | CANON_DERIVED |
| V2 | Quantum 2026 Rest-of-Year Audit | `/Users/mac/Desktop/_Arxiv/Arvix/outputs/Quantum_2026_Rest-of-Year_Audit.md` | CANON_DERIVED |
| V3 | Quantum Decade-Era Counter-Evidence Audit | `/Users/mac/Desktop/_Arxiv/Arvix/outputs/Quantum_Decade-Era_Counter-Evidence_Audit.md` | CANON_DERIVED |
| V4 | QML Skepticism synthesis | `/Users/mac/Desktop/_Arxiv/Arvix/outputs/Quantum_QML_Skepticism.md` | CANON_DERIVED |

### Key arXiv IDs referenced in vault audits

- 2605.27923 — Do We Really Need QML? (No clean win)
- 2605.19417 — Fair Benchmarking of Quantum Transfer Learning (No beat claim)
- 2605.21457 — Exponential Sample-Complexity Advantage (Theoretical only)
- 2605.10801 — Photonic QNN Algorithmic Advantage (Classically simulable by own admission)
- 2605.24324 — Matched Spectral Benchmark (Zero significant wins)
- 2602.04239 — Burgers Equation QTN (Explicit disavowal)
- 2603.09901 — Has Quantum Advantage Been Achieved? (RCS only, "nearly useless")
- 2604.11541 — Noise Effects in Hybrid QML (No classical baseline)
- 2606.28655 — Entanglement in QML Pathogen Epitopes (Explicit disavowal)
- 2607.08220 — QLS Quantum Chemistry (Conditional on unproven conjecture)
- 2510.19928 — Mind the Gaps (Eisert & Preskill, 2025)
- 2409.04406 — Quantum Kernel Methods under Scrutiny
- 2504.12416 — Quantum vs Classical Time Series Benchmark
- 0905.0887 — Towards Quantum Chemistry on a Quantum Computer (2009 ancestor, NOT_ESTABLISHED)
- 1908.07927 — Full Quantum Eigensolver (Strongest claim, least supported)
- 1902.03121 — Can Biological Quantum Networks Solve NP-hard? (Answers NO)
