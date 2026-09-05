---
canon-group: research
canon-type: synthesis
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: arxiv_web_2026-09
conclusion_class: ACTIVE_RESEARCH_SYNTHESIS
epistemic_class: SOURCE_CLAIM
topic: SOTA VLA Quantum BCI 2026 Synthesis
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - research/sota
  - research/vla
  - research/quantum
  - research/bci
created: 2026-09-05
---

# SOTA Vision-Language-Action, Quantum Computing, and BCI Research — 2026 Synthesis

> **Epistemic boundary:** `ACTIVE_RESEARCH_SYNTHESIS` — All claims below are `SOURCE_CLAIM` from cited papers. None of these methods are implemented in AMOS. AMOS bindings are `DERIVED` implications, not deployment claims.

## 1. Vision-Language-Action (VLA) Models

### 1.1 VLAct — Representation-Centric Continued Pre-training

**Source:** arXiv:2608.27550 (Aug 2026)

**Claim:** Scaling robot data for generalist VLA models is bottlenecked by representation quality, not just data volume. VLAct proposes VLM-prior preservation, multi-head continuous action co-supervision, and partially unified cross-embodiment action layouts.

**Key results:**
- 82.6% success on LIBERO-Plus (surpasses ABot-M0, LingBot-VLA)
- 92.5% on RoboTwin 2.0
- On RoboCasa-GR1 (unseen humanoid), VLAct with 20% of trajectories outperforms full-data GR00T-N1.6
- Trained on 16 GPUs with fully open-source data

**AMOS binding (`DERIVED`):** Relevant to `21_DOMAINS/54_ROBOTICS` and `13_MODELS/01_FOUNDATION`. The representation-centric pre-training approach aligns with AMOS's H/M/L retrieval architecture — representation quality under fixed data budgets mirrors AMOS's "smallest sufficient closure" principle.

### 1.2 Mantis — Disentangled Visual Foresight

**Source:** CVPR 2026 (Yang et al.)

**Claim:** Decouples visual foresight prediction from the VLA backbone using meta queries and a diffusion Transformer (DiT) head. Reduces backbone burden, preserves comprehension/reasoning through language supervision.

**Key results:**
- 96.7% success on LIBERO after fine-tuning
- Outperforms π0.5 in instruction-following, generalization, and reasoning
- Adaptive Temporal Ensemble (ATE) balances efficiency and motion stability

**AMOS binding (`DERIVED`):** The disentanglement pattern (separating foresight from action) maps to AMOS's separation of `PREDICTION` from `EXECUTION` in the runtime pipeline. Relevant to `04_RUNTIME/06_EXECUTION` and `05_COGNITIVE_ORGANISM/06_WORLD_MODEL`.

### 1.3 WLA — World-Language-Action Models

**Source:** arXiv:2606.05979 (2026)

**Claim:** Unifies world modeling, language reasoning, and action synthesis in a single autoregressive Transformer. Uses a World Expert for physical dynamics and an Action Expert for state-action correlation.

**Key results:**
- 2B active parameters, 40ms inference on RTX 5090
- 92.94% on RoboTwin2.0 Clean
- 56.5% on RMBench
- Can learn from cross-embodiment videos without action annotations

**AMOS binding (`DERIVED`):** The World Expert / Action Expert separation maps to AMOS's `K_WORLD_MODEL` and `K_EFFECT_CLASSIFICATION` kernel contracts. The autoregressive backbone aligns with `02_KERNEL/04_STATE` state transition models.

### 1.4 StreamPI — Streaming Multimodal Temporal Modeling

**Source:** arXiv:2608.26067 (Aug 2026)

**Claim:** Equips single-frame VLA with temporal reasoning without additional parameters. Uses instruction-anchored temporal modeling where each (visual, language) pair is an atomic temporal unit.

**Key results:**
- Outperforms π0.5 on memory-dependent and precise perception tasks
- Random-interval streaming training supports asynchronous deployment
- Seamlessly inherits pretrained single-frame weights

**AMOS binding (`DERIVED`):** The temporal streaming approach maps to AMOS's `10_MEMORY` context continuity patterns. The instruction-anchored design parallels AMOS's `03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION` — language as a persistent semantic anchor.

### 1.5 UniMem — Unified Multimodal Memory and Control

**Source:** arXiv:2608.22869 (2026)

**Claim:** Unifies high-level multimodal memory and low-level control under one backbone. Uses event classifier for memory updates, keyframe encoder for dense spatial memory.

**Key results:**
- Outperforms fixed-interval image conditioning across 5 simulation and 4 hardware tasks
- Single-model system eliminates memory bottleneck of multi-VLM approaches

**AMOS binding (`DERIVED`):** Directly relevant to `10_MEMORY` and `amos-memory-systems-master`. The event-classifier-driven memory updates map to AMOS's `K_MEMORY_ADMISSION` contract — gated memory entry rather than arbitrary frame sampling.

---

## 2. Quantum Computing Breakthroughs

### 2.1 IBM 70 Logical Qubits — Verifiable Quantum Advantage

**Source:** "Sampling hard circuits with verifiably high fidelity" (IBM + University of Chicago, Aug 2026)

**Claim:** 70 error-corrected logical qubits solved a classically intractable problem in ~15 minutes with statistical evidence of reliability. One of the largest logical quantum computing demonstrations.

**Key claims:**
- New error correction strategy preserves RCS computational hardness
- Structure allows error detection during computation
- Leading classical methods require impractical time for same task

**AMOS binding (`DERIVED`):** Relevant to `21_DOMAINS/41_QUANTUM_SYSTEMS` and `11_KNOWLEDGE/05_FRAMEWORKS/QLS_FRAMEWORK`. The verifiable fidelity approach maps to AMOS's `RSCF` provenance discipline — quantum results must carry evidence of reliability, not just claims.

### 2.2 Cornucopia Codes — Ultra-Low Overhead QEC

**Source:** arXiv:2608.02773 (2026)

**Claim:** Quantum LDPC codes achieving encoding rate >1/2 with pseudo-threshold >0.4% under circuit-level noise. A single [[2844,1426,18]] code block encodes 1,426 logical qubits with extrapolated logical error rate of 2.6×10⁻¹⁶ per cycle at 0.1% physical error.

**Key implications:**
- Bivariate bicycle codes would need 68,000+ physical qubits for same logical count
- 12 entangling layers for syndrome extraction, independent of code size
- Designed for reconfigurable neutral-atom arrays

**AMOS binding (`DERIVED`):** Relevant to `21_DOMAINS/41_QUANTUM_SYSTEMS/COHERENT_ISING_MACHINE_LEDGER`. The encoding efficiency maps to AMOS's `L23_MVCC_CAS` concurrency principles — more efficient state encoding reduces coordination overhead.

### 2.3 τ-Helix Architecture — Compact Fault-Tolerant Design

**Source:** arXiv:2609.03194 (Sep 2026, Quantinuum Helios)

**Claim:** Experimentally validated compact fault-tolerant architecture for trapped ions. 98-qubit processor demonstrates repeated QEC, full Clifford group on two logical qubits, and heterogeneous interface with distance-5 surface code.

**Key results:**
- Encoded implementations outperform unencoded physical baselines without postselection
- Fault-tolerant chain-map interface between τ-Helix and surface code
- Three-logical-qubit GHZ state with verified fidelity

**AMOS binding (`DERIVED`):** The heterogeneous code interface (τ-Helix ↔ surface code) maps to AMOS's `K_BINDING` contract — governed relationships between different encoding systems. Relevant to `02_KERNEL/09_INTEGRATION`.

### 2.4 NOBOL — Single Bell-Pair Logical CNOT

**Source:** arXiv:2609.01901 (Sep 2026)

**Claim:** Requires only one Bell pair to perform logical CNOT on distant qubits in arbitrary CSS codes. Operations only on logical X/Z operator subsets, which are smaller than full code.

**Key implications:**
- Depth-optimal circuit with logarithmic depth in logical operator size
- Code-agnostic and qubit-modality-agnostic
- Significant overhead reduction for distributed quantum computing

**AMOS binding (`DERIVED`):** Maps to AMOS's `L25_SHARD_LOCAL` and `L26_PROOF_COORDINATION` — reducing coordination overhead between distant logical units. The single-Bell-pair primitive parallels AMOS's "smallest sufficient closure" principle.

### 2.5 Cross-Code Lattice Surgery — Genuine Multipartite Entanglement

**Source:** arXiv:2607.04227 (Jul 2026)

**Claim:** Experimental generation and certification of logical genuine multipartite entanglement using cross-code lattice surgery. Combines 4-qubit surface code (Hadamard) with 8-qubit 3D color code (CCZ).

**Key results:**
- Stabilizer (GHZ) and non-stabilizer (|CCZ⟩) states of three logical qubits
- Verified genuine multipartite entanglement — beyond bipartite mixtures
- Universal logical gate set via lattice surgery

**AMOS binding (`DERIVED`):** Relevant to `09_PROTOCOLS/ZK_MERKLE_GOSSIP_CONSENSUS_LEDGER` — multipartite entanglement as a substrate for consensus protocols. The cross-code surgery maps to AMOS's `K_CIL` (Canon Integration Layer) — joining complementary code structures.

---

## 3. Brain-Computer Interface Advances

### 3.1 Independent At-Home BCI — 3,800+ Hours, 56 WPM

**Source:** Nature Medicine, s41591-026-04414-6 (2026)

**Claim:** First demonstration of independent at-home intracortical BCI use. ALS participant used multimodal BCI for 3,800+ hours over ~2 years with no researchers present.

**Key results:**
- 1,960,163 words communicated at 56 WPM average
- 99%+ word accuracy on 125,000-word vocabulary (formal testing)
- 92% of sentences labeled "mostly correct" by participant
- Sustained full-time employment despite paralysis
- Speech BCI as keyboard + cursor BCI as mouse for full computer control

**AMOS binding (`DERIVED`):** Directly relevant to `21_DOMAINS/51_HEALTH`, `05_COGNITIVE_ORGANISM/01_SENSING_OBSERVATION`, and `15_INTERFACES`. The long-term stability maps to AMOS's `K_IDENTITY` continuity contract — neural decoder identity must persist across years.

### 3.2 Generalizable Multi-User Speech BCI Decoder

**Source:** bioRxiv 2026.07.23.739430 (2026)

**Claim:** Transformer-based decoder trained jointly across six intracortical speech BCI participants. Multi-user model outperforms single-user models by >50% relative WER reduction.

**Key results:**
- Fine-tunable on <200 sentences from held-out user to achieve <7% WER
- Generalizes across sex, disease etiology, and speaking strategy
- Enables rapid deployment (days vs. weeks of training data)

**AMOS binding (`DERIVED`):** The multi-user generalization maps to AMOS's `K_SYBIL_HARDENING` — pooling data across sources while preserving individual identity. The transfer learning approach aligns with `amos-transfer-learning` skill concepts.

### 3.3 Speech Mode and Loudness Decoding from vPCG

**Source:** Nature Communications, s41467-026-71284-4 (2026)

**Claim:** Neuronal firing rates in ventral precentral gyrus (vPCG) encode speech mode (mimed/whispered/normal/loud) and loudness in distinct neural subspaces from phonemic content.

**Key results:**
- 94% and 89% mode/loudness decoding accuracy for two participants
- Preparatory activity at 270-640ms before speech onset enables 80% decoding
- Closed-loop loudness decoder achieves 94% online accuracy

**AMOS binding (`DERIVED`):** The subspace separation (mode/loudness vs. phonemes) maps to AMOS's `K_EFFECT_CLASSIFICATION` — different effect types encoded in distinct representational spaces. Relevant to `05_COGNITIVE_ORGANISM/04_COGNITION/ATTENTION_SELECTION_ARCHITECTURE`.

### 3.4 Pontine Stroke Speech Restoration

**Source:** 2026.02.19.26346583 (BrainGate2, participant T16)

**Claim:** Intracortical BCI from single 64-channel microelectrode array in orofacial motor cortex achieves 19.6% WER on 125,000-word vocabulary for pontine stroke dysarthria.

**Key results:**
- 60.8% WER reduction over prior ECoG studies
- Stable >2 years post-implantation
- Generalizes to spontaneous Q&A communication (35.2% WER)

**AMOS binding (`DERIVED`):** The single-array performance maps to AMOS's "smallest sufficient closure" — minimal sensor footprint achieving functional communication. Relevant to `15_INTERFACES` and `21_DOMAINS/51_HEALTH`.

### 3.5 Neural Hammer & Scalpel — Day-to-Day Calibration

**Source:** arXiv:2603.20246 (2026)

**Claim:** Multitask Transformer sequence-to-sequence model for intracortical speech decoding. NHS calibration module addresses day-to-day nonstationarity via global alignment + feature-wise modulation.

**Key results:**
- Joint phoneme, word, and acoustic feature prediction
- Analyzed held-out-day generalization and attention patterns
- Interpretability through encoder/decoder attention analysis

**AMOS binding (`DERIVED`):** The day-to-day calibration problem maps directly to AMOS's `K_MEMORY_RETRIEVAL` freshness contract — neural signal representations drift and require calibration to maintain validity. The NHS module parallels AMOS's `amos-adaptive-calibration` concepts.

---

## 4. Cross-Cutting Themes

### 4.1 Representation Quality Over Data Quantity
Both VLAct (VLA) and Cornucopia codes (quantum) demonstrate that representation architecture matters more than raw data/scale. This aligns with AMOS's H/M/L retrieval — the right representation reduces the search space.

### 4.2 Disentanglement for Efficiency
Mantis (visual foresight), WLA (world/action experts), and vPCG subspace separation all show that disentangling concerns improves performance. This maps to AMOS's MECE decomposition principle.

### 4.3 Verifiable Reliability
IBM's quantum advantage with verifiable fidelity and the BCI's 92% user-labeled accuracy both emphasize evidence over claims. This maps to AMOS's core RSCF discipline: `DOCUMENTED != IMPLEMENTED`, `TEST_SPECIFIED != TEST_EXECUTED`.

### 4.4 Long-Term Stability
The 3,800-hour BCI and >2-year decoder stability demonstrate that real-world systems must maintain identity and performance across regime changes. This maps to AMOS's `K_IDENTITY` continuity and `L10_FAILURE_RECOVERY` contracts.

---

## 5. Open Gaps (`UNKNOWN/GAP`)

| Gap | Description |
|-----|-------------|
| GAP-VLA-01 | No VLA model has demonstrated AMOS-level governance (authority, provenance, commit-time freshness) over action decisions. |
| GAP-Q-01 | Quantum error correction at scale remains experimental — no production deployment of logical qubit systems. |
| GAP-BCI-01 | BCI long-term stability is demonstrated for speech but not for complex cognitive tasks (reasoning, planning). |
| GAP-CROSS-01 | No work bridges VLA, quantum, and BCI in a unified architecture — this synthesis identifies the gap but does not claim closure. |
| GAP-AMOS-01 | AMOS bindings in this document are `DERIVED` implications — none are implemented or validated in AMOS runtime. |

---

## 6. Provenance

| Paper | Source | Date | Class |
|-------|--------|------|-------|
| VLAct | arXiv:2608.27550 | Aug 2026 | SOURCE_CLAIM |
| Mantis | CVPR 2026 | 2026 | SOURCE_CLAIM |
| WLA | arXiv:2606.05979 | 2026 | SOURCE_CLAIM |
| StreamPI | arXiv:2608.26067 | Aug 2026 | SOURCE_CLAIM |
| UniMem | arXiv:2608.22869 | 2026 | SOURCE_CLAIM |
| IBM 70Q | IBM+UChicago | Aug 2026 | SOURCE_CLAIM |
| Cornucopia | arXiv:2608.02773 | 2026 | SOURCE_CLAIM |
| τ-Helix | arXiv:2609.03194 | Sep 2026 | SOURCE_CLAIM |
| NOBOL | arXiv:2609.01901 | Sep 2026 | SOURCE_CLAIM |
| Cross-Code | arXiv:2607.04227 | Jul 2026 | SOURCE_CLAIM |
| BCI Home | Nature Medicine | 2026 | SOURCE_CLAIM |
| Multi-User BCI | bioRxiv | 2026 | SOURCE_CLAIM |
| vPCG Modes | Nature Comms | 2026 | SOURCE_CLAIM |
| Pontine BCI | BrainGate2 | 2026 | SOURCE_CLAIM |
| NHS Decoder | arXiv:2603.20246 | 2026 | SOURCE_CLAIM |

---

**Related:** [[22_RESEARCH/01_PAPERS/SOTA_AI_SAFETY_MATERIALS_ROBOTICS_EDGE_2026|SOTA AI Safety/Materials/Robotics/Edge]] · [[22_RESEARCH/01_PAPERS/SOTA_BCI_NEURAL_DECODING_FOUNDATION_MODELS_2026|SOTA BCI Neural Decoding]] · [[22_RESEARCH/01_PAPERS/SOTA_QUANTUM_SENSING_ERROR_CORRECTION_NETWORKING_2026|SOTA Quantum Sensing]] · [[22_RESEARCH/22_RESEARCH_MOC|Research MOC]]
