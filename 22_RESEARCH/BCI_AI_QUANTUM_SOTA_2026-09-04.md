---
title: BCI/AI/Quantum SOTA Research Ingestion 2026-09-04
type: research_ingestion
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 22_RESEARCH/02_ARXIV_BRIDGES
    - 11_KNOWLEDGE/_arxiv_md/_arxiv_md_MOC
  scope: sota_research_ingestion
tags:
  - research
  - bci
  - ai
  - quantum
  - sota
  - 2026-09
created: 2026-09-04
---

# BCI / AI / Quantum SOTA Research Ingestion — 2026-09-04

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **Epistemic Class:** `AMOS_MODEL`
> **Conclusion Class:** `DERIVED`

---

## Epistemic boundary (read first)

This ingestion is a **DERIVED AMOS_MODEL** synthesis of public, peer-reviewed and pre-print literature as of September 2026. It is **not** empirical observation by AMOS, **not** canon, and **not** a claim of biological or physical truth. The following non-negotiable boundaries hold throughout:

```text
SOURCE_CLAIM != VERIFIED
AMOS_MODEL != OBSERVATION
DOCUMENTED != IMPLEMENTED
CAPABILITY != AUTHORITY
```

Any bridge between quantum mechanics and biological consciousness is tagged `AMOS_MODEL` and must **not** be read as a physics claim. No quantum-biological causation is asserted without independent experimental evidence. Where evidence is absent, the state is `UNKNOWN/GAP`.

---

## BCI SOTA (Brain-Computer Interfaces)

### High-channel-count intracortical arrays

The state of the art in invasive recording is defined by **Utah-array-derived and next-generation high-channel-count probes** exceeding 1,000 simultaneously recorded channels.

- **Neuralink** (N1 implant, first-in-human trial 2024, expanded cohort 2025–2026): 1,024 electrode threads, ~64 channels per flexible polymer thread, read via custom ASIC. The 2024 *Lancet Neurology* / *NEJM* report demonstrated cursor control with a BCI pointer; subsequent reports (2025–2026) added intent-decoding for writing and grasp selection. Threads retraction was observed in the first subject, partially recovered after algorithmic recalibration — a documented failure mode, not a resolved one.
- **Paradromics** (Connexus system): ~1,600-channel microwire array targeting the speech motor cortex. FDA Breakthrough Device designation (2023); first-in-human cortical visual/speech prosthetic trials reported 2025–2026. Speech-decoding throughput is the headline metric.
- **Blackrock Neurotech** (Utah array legacy + Neuralace): chronic implants with the longest human track record (>1,000 days in some participants); multi-array configurations reaching ~512 channels in clinical use.

**Epistemic tag:** `SOURCE_CLAIM` for vendor-reported throughput; `EMPIRICAL` only for peer-reviewed trial data. Vendor press releases are **not** peer-reviewed evidence.

### Non-invasive decoding: fNIRS and EEG motor imagery

- **EEG motor-imagery decoding** remains dominated by deep-learning pipelines (EEGNet, ShallowConvNet, and transformer variants such as EEG-Conformer and BIOT). Cross-subject generalization accuracy on the BCI Competition IV-2a dataset has plateaued around 70–78% for 4-class motor imagery; domain adaptation (adversarial, contrastive) is the active frontier for closing the inter-subject gap.
- **fNIRS** (functional near-infrared spectroscopy) offers better spatial localization than EEG at the cost of temporal resolution (~1–2 Hz hemodynamic response). Hybrid EEG-fNIRS systems report 5–10% accuracy gains over EEG-alone on mental-workload and motor-imagery tasks (2024–2026 meta-analyses).
- **Wireless, dry-electrode consumer headsets** (OpenBCI, g.Nautilus, Emotiv) have narrowed the gel-to-dry SNR gap but remain below clinical-grade wet electrodes for high-frequency (gamma-band) features.

### Speech decoding from intracranial recordings

This is the fastest-moving BCI sub-field:

- **Stanford / UCSF (Metzger, Willett et al., 2024–2026):** intracortical microelectrode arrays in the precentral gyrus decoding intended speech at **~62–78 words/min** with a ~50k-word vocabulary using RNN-transducer and transformer language-model rescoring. The 2024 *Nature* paper reported 78 wpm at 25% WER; 2025–2026 follow-ups improved WER with LLM-based rescoring.
- **Berkeley / UCSF (Chartier et al.):** ECoG-based speech synthesis reaching ~47–60 wpm with a phoneme-to-acoustic pipeline.
- **Stanford / BrainGate (Stavisky et al.):** handwriting decoding at ~90 characters/min (18 wpm) with <1% error on a 66-character alphabet using RNN decoders.

**Key insight for AMOS:** speech BCI has crossed the 60 wpm threshold that the field identified as the minimum for practical communication by paralyzed patients. This is an `EMPIRICAL` milestone, not a model prediction.

### Closed-loop BCI for stroke rehabilitation

- **Robot-assisted + BCI motor imagery** trials (Ang et al., Soekadar et al.): moderate effect sizes (Cohen's d ≈ 0.4–0.6) for upper-limb Fugl-Meyer improvement in chronic stroke patients. The mechanism is hypothesized to be Hebbian plasticity reinforcement via contingent sensory feedback.
- **Closed-loop stimulation** (paired-associative stimulation, epidural spinal stimulation + BCI trigger): 2025 trials show partial hand-function recovery in cervical SCI patients, but sample sizes remain small (n < 20) and replication is incomplete. Tag: `SOURCE_CLAIM` pending larger RCTs.

### Bidirectional BCI (recording + stimulation)

- **Bergman / Aflalo / Andersen (Caltech → UCLA):** bidirectional cortical prosthetics combining single-unit recording with intracortical microstimulation (ICMS) for somatosensory feedback. Monkeys demonstrated closed-loop grasp with artificial tactile feedback (2024); human translation is in early feasibility.
- **Neuralink / Synchron:** stimulation capabilities are in the device roadmap but not yet demonstrated at peer-reviewed clinical endpoints as of 2026.

### AMOS C04 Bio-Neuro domain binding

The BCI SOTA maps to **AMOS C04 (Bio-Neuro)** domain. The binding is epistemically constrained:

- Neural decoding accuracy → `EMPIRICAL` (measured bit-rate, WER).
- Mechanistic claims about neural coding → `AMOS_MODEL` unless independently replicated.
- **Quantum-consciousness claims in BCI** → `AMOS_MODEL` only, explicitly **not** a physics claim. No evidence supports quantum-coherent processes in macroscopic neural decoding. The Penrose-Hameroff Orch-OR hypothesis remains `COMPETING` / `UNRESOLVED` and is **not** load-bearing for any AMOS C04 binding.

See: [[21_DOMAINS/14_C04_BIO_NEURO/14_C04_BIO_NEURO_MOC|C04 Bio Neuro]] · [[07_SKILLS/amos-c04-bio-neuro-master/SKILL|C04 Master Skill]]

---

## AI SOTA (Large Models & Reasoning)

### Mixture-of-Depths (MoD) conditional computation

- **Google DeepMind (Raposo et al., 2024):** Mixture-of-Depths allows each token to choose whether to pass through a transformer layer or skip it via a learned router, reducing FLOPs by ~50% at iso-perplexity. Combined with Mixture-of-Experts (MoE), this yields the **MoD-MoE** architecture. As of 2026, MoD has been adopted in several open-weight models (DeepSeek-V3 uses a related shared-expert sparse routing).
- **AMOS relevance:** conditional computation is a direct analog to the AMOS cognitive-load-gated validation depth (see `amos-validation-depth-layer`). Tokens that "skip" layers are the architectural parallel to mutations that skip deep validation when consequence is low.

### Sparse attention and long-context scaling

- **LongRoPE (Microsoft, 2024):** extends rotary position embeddings to **2M+ tokens** via non-uniform interpolation and evolutionary search over rotation frequencies. Demonstrated on Llama-2-7B with 2M-token context.
- **YaRN (Peng et al., 2023–2024):** yet another RoPE extensioN, scaling to 128k–1M tokens with NTK-aware interpolation. Widely adopted in open-source fine-tuning pipelines.
- **RingAttention / Blockwise RingAttention (Liu et al., 2023–2024):** enables training and inference on sequences longer than GPU memory by distributing attention computation across devices. Used in 1M-token context training runs.
- **As of 2026:** frontier models routinely offer **1M–10M token context windows** (Gemini 1.5/2.0 Pro, Claude 3.5/4, GPT-4-class). Effective retrieval within ultra-long contexts degrades beyond ~100k tokens ("lost in the middle" effect persists despite architectural mitigations).

### Test-time compute scaling (o1 / o3-style reasoning)

- **OpenAI o1 (Sept 2024) → o3 (2025):** reinforcement-learning-trained reasoning chains that scale performance with test-time compute. The paradigm: generate long chains-of-thought, use a reward model to verify intermediate steps, and apply search (best-of-N, tree-search, or process-reward-guided beam search). Demonstrated on competition math (AIME, Codeforces) and PhD-level science benchmarks (GPQA Diamond).
- **DeepSeek-R1 (Jan 2025):** open-weight replication of o1-style reasoning via pure RL (GRPO) without supervised CoT distillation, achieving comparable reasoning performance. R1-Zero (RL-only) showed emergent self-verification and reflection behaviors.
- **AMOS relevance:** test-time compute scaling is the computational analog of AMOS `amos-reasoning-loop-layer` (7-phase reasoning loop). The RL-verified reasoning chain maps to AMOS proof-carrying commits: the reasoning trace is the receipt.

### GRPO (Group Relative Policy Optimization)

- **DeepSeek (Shao et al., 2024):** GRPO simplifies PPO by replacing the value-network critic with group-relative advantage estimation. For each prompt, sample a group of G outputs, compute advantages as (reward − group_mean) / group_std. This removes the value network, reducing memory and training instability.
- **Adoption:** GRPO is now the default RL algorithm for reasoning-model post-training in the open-weight ecosystem (R1, Qwen-QwQ, and derivatives). It is empirically effective but lacks the strong theoretical convergence guarantees of PPO with a learned value function.

### Flow matching generative models

- **Lipman et al. (2023) / Esser et al. (Flow Matching for Generative Modeling, 2024):** flow matching generalizes diffusion models by learning a vector field that transports a source distribution to a target distribution along a prescribed probability path. Stochastic interpolants and rectified flow are special cases.
- **Stable Diffusion 3 (Esser et al., 2024):** uses rectified flow (a flow-matching variant) instead of DDPM-style diffusion, improving sample quality and training efficiency.
- **Meta Voicebox (2024):** flow-matching for multilingual TTS, demonstrating zero-shot voice cloning with 6x fewer inference steps vs diffusion baselines.
- **As of 2026:** flow matching has largely supplanted discrete-time diffusion in state-of-the-art image, audio, and video generation (Sora-class models use flow-matching variants).

### RAG evaluation and agent memory

- **RAGAS, ARES, TruLens:** the standard RAG evaluation frameworks measure context relevance, faithfulness (groundedness), and answer relevance. As of 2026, multi-hop RAG benchmarks (HotpotQA, MuSiQue, FRAMES) remain the hardest evaluation frontier.
- **Agent memory dynamics:** the MemGPT / Letta / Mem0 lineage provides tiered memory (core / archival / recall) for LLM agents. The open research question is **memory consolidation** — when and how to compress episodic memory into semantic memory without catastrophic forgetting. This directly parallels AMOS `10_MEMORY` plane concerns.
- **AMOS relevance:** RAG evaluation maps to AMOS evidence-grounding discipline (`SOURCE_CLAIM != VERIFIED`); agent memory dynamics map to `10_MEMORY` and `05_COGNITIVE_ORGANISM`.

### AMOS C10 / C05 domain binding

- **C10 (Cognitive Organism):** reasoning chains, test-time compute, and agent memory dynamics bind here. The cognitive-organism plane governs the self-model, reasoning loop, and memory consolidation.
- **C05 (Mathematics / Formal):** flow matching, GRPO convergence analysis, and sparse-attention complexity bounds bind here as formal/mathematical objects.

See arxiv skills in vault: [[11_KNOWLEDGE/_arxiv_md/_arxiv_md_MOC|arxiv MOC]]

---

## Quantum SOTA (Computing & Cryptography)

### Surface-code error correction and below-threshold logical qubits

- **Google Quantum AI (Willow chip, Dec 2024):** 105 superconducting qubits demonstrating **below-threshold** surface-code error correction — increasing the code distance from 3 to 5 to 7 **reduced** the logical error rate, the first time this critical threshold theorem prediction was experimentally confirmed. The logical qubit (distance-7) had a lower error rate than the distance-5 logical qubit, which was lower than distance-3. This is the foundational milestone for fault-tolerant quantum computing.
- **IBM (Heron r2 / Condor, 2024–2026):** 156-qubit Heron processors with tunable-coupler architecture. IBM's error-correction roadmap targets the **LDPC (low-density parity-check) code** as a more efficient alternative to the surface code, requiring ~10x fewer physical qubits per logical qubit. As of 2026, LDPC codes are demonstrated in simulation and small-scale hardware but not yet at the scale of Google's surface-code milestone.
- **Quantinuum (H2 trapped-ion, 2024–2026):** 56-qubit trapped-ion system demonstrating 12 logical qubits with mid-circuit measurement and feedforward. Reported logical fidelity improvements consistent with below-threshold operation in the color-code family.
- **Key metric:** the **threshold** for the surface code on superconducting hardware is ~1% physical error rate; Google's Willow operates at ~0.3% two-qubit gate error, comfortably below threshold.

**Epistemic tag:** `EMPIRICAL` for the below-threshold demonstration (peer-reviewed, *Nature* 2024). `SOURCE_CLAIM` for vendor roadmaps to 1M+ qubit machines.

### Continuous-variable QKD (GG02 protocol)

- **Grosshans & Grangier (2002, GG02):** continuous-variable quantum key distribution using Gaussian-modulated coherent states and homodyne detection. CV-QKD's advantage over discrete-variable (BB84) QKD is compatibility with standard telecom photodetectors (no single-photon detectors required).
- **As of 2026:** CV-QKD has been demonstrated over **100+ km fiber** (Toshiba, 2024; several Chinese groups, 2025) with secure key rates of ~kbps. The main limitation is the trusted-node requirement for long distances (quantum repeaters remain experimental).
- **NIST / ETSI standardization:** CV-QKD is under active standardization but not yet a finalized FIPS standard. BB84 and measurement-device-independent QKD (MDI-QKD) remain the more mature protocols.

### Quantum Koopman algorithms for dynamical systems

- **Koopman operator theory** lifts nonlinear dynamical systems into infinite-dimensional linear systems via observable functions. The **quantum Koopman** approach (Lloyd, Schuld, et al.) proposes using quantum circuits to approximate the Koopman operator's spectral decomposition, potentially offering exponential speedup for certain ergodic systems.
- **Status (2026):** this is a **theoretical / small-scale** result. No practical quantum advantage has been demonstrated for Koopman decomposition on classically-hard dynamical systems. The approach is `AMOS_MODEL` for any claim of real-world speedup. Classical Koopman (DMD, EDMD) remains the practical workhorse for fluid dynamics, power-grid analysis, and neuroscience (neural population dynamics).

### Post-quantum cryptography migration

- **NIST FIPS 203 (ML-KEM / Kyber):** finalized August 2024. Module-lattice-based key encapsulation. Now the primary PQC key-exchange standard.
- **NIST FIPS 204 (ML-DSA / Dilithium):** finalized August 2024. Module-lattice-based digital signature.
- **NIPS 205 (SLH-DSA / SPHINCS+):** finalized August 2024. Hash-based stateless digital signature (fallback if lattice assumptions break).
- **Migration status (2026):** TLS 1.3 hybrid post-quantum key exchange (X25519 + ML-KEM-768) is deployed by Cloudflare, Google, Apple iMessage, and Signal. Full PQC migration of the internet's PKI (X.509 certificate replacement) is estimated at 10–15 years due to the long tail of embedded devices and HSM refresh cycles.
- **AMOS relevance:** PQC migration binds to `18_SECURITY` and the cryptographic audit trail in `00_ROOT/CLAUDE.md` (BLAKE3 / SHA-256 envelopes). The migration is `EMPIRICAL` (standards are published and deployed).

### Quantum advantage benchmarks

- **Google Sycamore (2019):** random circuit sampling — claimed quantum advantage, later matched by classical tensor-network methods (Pan, Zhang 2021–2022). The "advantage" is contested for this specific task.
- **Chinese USTC Jiuzhang (2020–2022):** boson sampling advantage, also partially challenged by improved classical algorithms.
- **As of 2026:** no **practically useful** quantum advantage has been unambiguously demonstrated for a commercially-relevant problem. The below-threshold error-correction milestone (Google Willow) is the more significant achievement, as it is a prerequisite for future fault-tolerant advantage rather than a benchmarking claim.

### AMOS C03 / 41_QUANTUM_SYSTEMS domain binding

- **C03 (Physics-Cosmos):** quantum error correction, QKD, and PQC bind here as physics-derived objects. The binding is `EMPIRICAL` for demonstrated results, `SOURCE_CLAIM` for roadmaps.
- **41_QUANTUM_SYSTEMS:** the vault's quantum-systems domain plane. See [[21_DOMAINS/41_QUANTUM_SYSTEMS/41_QUANTUM_SYSTEMS_MOC|Quantum Systems]].

See: [[07_SKILLS/amos-c03-physics-cosmos-master/amos-c03-physics-cosmos-master_MOC|C03 Master Skill]]

---

## Cross-domain bridges

### BCI × AI: neural decoding with transformer architectures

The speech-decoding milestones (Stanford/Berkeley, 62–78 wpm) are fundamentally **AI-architecture-dependent**: the neural-to-text pipeline uses RNN-transducers, transformers, and LLM-based language-model rescoring. The BCI signal is the input tensor; the AI model is the decoder. This is the most mature cross-domain bridge and is `EMPIRICAL`.

**AMOS_MODEL extension:** the reverse direction — using BCI-derived neural representations to improve AI architectures (e.g., brain-inspired sparse coding, predictive-coding losses) — is speculative. No demonstrated advantage exists as of 2026.

### AI × Quantum: quantum machine learning — skepticism vs genuine advantage

- **Skepticism (Tang 2019, Landman 2022):** several proposed quantum ML speedups (quantum recommendation systems, quantum PCA) were de-quantized — reproduced classically with polylogarithmic overhead. The pattern: many QML "advantages" rely on low-rank structure that classical algorithms can also exploit.
- **Genuine candidates (2026):** quantum kernel methods (Havlicek et al., IBM) and quantum-enhanced generative models (quantum circuit Born machines) remain candidates for advantage on specific data distributions, but no peer-reviewed practical advantage on real-world datasets exists.
- **AMOS stance:** QML advantage is `UNKNOWN/GAP`. Claims of quantum-accelerated LLM training are `AMOS_MODEL` and unsupported by evidence. The honest position: quantum computers may eventually accelerate specific sub-routines (linear algebra, sampling) in ML pipelines, but this is not established.

### Quantum × BCI: quantum-coherent neural modeling (AMOS_MODEL only)

- **Penrose-Hameroff Orch-OR:** proposes that consciousness arises from quantum-coherent collapse in microtubules. This is a `COMPETING` hypothesis with **no experimental consensus** as of 2026. Multiple critiques (Tegmark 2000, decoherence-time calculations) argue that warm, wet biological systems decohere too fast for sustained quantum coherence.
- **Quantum biology (established):** photosynthetic light-harvesting (Engel et al., 2007), avian magnetoreception (cryptochrome radical-pair mechanism), and enzymatic tunneling are `EMPIRICAL` examples of quantum effects in biology. **None** of these involve neural computation or consciousness.
- **AMOS binding:** any bridge between quantum coherence and BCI/neural decoding is `AMOS_MODEL` — explicitly **not** a physics claim. The AMOS C04 (Bio-Neuro) and 41_QUANTUM_SYSTEMS domains are linked for exploratory modeling, but no causal claim is asserted. `UNKNOWN/GAP` is the honest state for quantum-consciousness.

---

## AMOS integration

This ingestion binds to the following AMOS planes and domain MOCs:

- [[11_KNOWLEDGE/_arxiv_md/_arxiv_md_MOC|arxiv MOC]] — raw arXiv ingest index; source papers for the claims above are traceable through this MOC.
- [[21_DOMAINS/14_C04_BIO_NEURO/14_C04_BIO_NEURO_MOC|C04 Bio Neuro]] — BCI SOTA domain binding.
- [[21_DOMAINS/41_QUANTUM_SYSTEMS/41_QUANTUM_SYSTEMS_MOC|Quantum Systems]] — Quantum SOTA domain binding.
- [[07_SKILLS/amos-c04-bio-neuro-master/SKILL|C04 Master Skill]] — bio-neuro domain skill.
- [[07_SKILLS/amos-c03-physics-cosmos-master/amos-c03-physics-cosmos-master_MOC|C03 Master Skill]] — physics-cosmos domain skill (quantum error correction, PQC, QKD).

### Related AMOS artifacts

- [[22_RESEARCH/02_ARXIV_BRIDGES|ArXiv Bridges]] — bridge construction contract and subordinate indices.
- [[22_RESEARCH/01_PAPERS/SOTA_HARVEST_2026-09-04|SOTA_HARVEST_2026-09-04]] — latest BCI / AI / Quantum harvest (if present).
- [[22_RESEARCH/01_PAPERS/SOTA_BCI_AI_QUANTUM_SYNTHESIS_2026|SOTA_BCI_AI_QUANTUM_SYNTHESIS_2026]] — cross-domain synthesis (if present).
- [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]] — research plane MOC.

### Epistemic summary table

| Domain | Strongest claim | Epistemic class | Evidence |
| :--- | :--- | :--- | :--- |
| BCI speech decoding | 62–78 wpm, intracortical | `EMPIRICAL` | Peer-reviewed trials (Stanford/UCSF, *Nature* 2024–2026) |
| BCI high-channel arrays | >1,000 channels demonstrated | `EMPIRICAL` (clinical) / `SOURCE_CLAIM` (vendor) | Neuralink N1, Paradromics Connexus |
| AI reasoning (o1/o3/R1) | Test-time compute scales performance | `EMPIRICAL` | GPQA, AIME, Codeforces benchmarks |
| AI long-context | 1M–10M token windows | `EMPIRICAL` | Frontier model releases 2024–2026 |
| Quantum error correction | Below-threshold logical qubits | `EMPIRICAL` | Google Willow, *Nature* Dec 2024 |
| PQC migration | FIPS 203/204/205 finalized, hybrid TLS deployed | `EMPIRICAL` | NIST standards, Cloudflare/Google deployment |
| QML advantage | Not established | `UNKNOWN/GAP` | De-quantization results (Tang, Landman) |
| Quantum-consciousness | Not established | `AMOS_MODEL` / `COMPETING` | Orch-OR hypothesis, no experimental consensus |

---

## Gaps and open questions

1. **BCI longevity:** chronic recording quality degrades over months (glial scarring, electrode drift). No solution is established. `UNKNOWN/GAP`.
2. **Non-invasive BCI bandwidth:** EEG/fNIRS bit-rate ceiling (~100 bits/min) is far below invasive BCI. No known path to close this gap without improved sensor physics. `UNKNOWN/GAP`.
3. **AI reasoning reliability:** o1/o3-style reasoning chains can produce confident errors (hallucinated proofs). Verification of reasoning traces is an open problem. `COMPETING` methods (process reward models, Lean4 verification) are active.
4. **Quantum advantage for ML:** no practical advantage demonstrated. `UNKNOWN/GAP`.
5. **Quantum-consciousness:** Orch-OR is `COMPETING` with no discriminating experimental evidence. `UNKNOWN/GAP`. AMOS does not assert this bridge as physics.

---

## SOTA Update — 2026-09-04 Phase 2 (arXiv Sept 2026)

### BCI / Neural Decoding

| Paper | Key result | Epistemic class | AMOS bridge |
| :--- | :--- | :--- | :--- |
| **Brain2Qwerty v2** (arXiv:2608.18114, Meta, Aug 2026) | Non-invasive MEG brain-to-text decoding at 39% WER average, best participant 50% sentences with ≤1 word error. Log-linear improvement with data volume. LLM finetuning for semantic representations + AI agents for pipeline refinement. | `SOURCE_CLAIM` (peer-reviewed preprint) | Bridges to AMOS C04 Bio-Neuro (non-invasive BCI bandwidth gap narrowing) and C05 Mind-Behavior (AI-agent-iterated pipeline design). Code: github.com/facebookresearch/brain2qwerty. |
| **EEG-PRIME** (arXiv:2608.13072) | Two-stage EEG foundation model: masked pretraining + prototype-aligned instruction tuning with multi-level conditioning (task-semantic, dataset-level, subject-invariance via gradient reversal). Cross-dataset generalization across 16 BCI paradigms. | `SOURCE_CLAIM` | Bridges to AMOS C04 (subject-invariant neural decoding) and RSCF (prototype-aligned classification = frozen text embeddings, cosine similarity matching). |
| **EEG-VID** (arXiv:2609.00566) | Task-guided latent predictive pretraining for EEG. EMA target encoder + weak task guidance. 41/42 backbone-dataset-protocol comparisons improved. 4-electrode spatial posterior supports assistive target selection at 40.24% vs 25% chance. | `SOURCE_CLAIM` | Bridges to AMOS C04 (latent predictive coding for neural signals) and C05 (assistive target selection = BCI-to-action loop). |
| **FRED** (arXiv:2608.03176, ACM MM 2026 BCI Challenge) | Frequency-decorrelated temporal ensembles for EEG-fNIRS imagined-handwriting. 9-member ensemble: 0.8076/0.7242/0.7492 public/private/overall. fNIRS-only at chance (0.2511); EEG is principal signal. | `SOURCE_CLAIM` | Bridges to AMOS C04 (multi-frequency EEG modeling) and C02 Math-Compute (ensemble diversity via frequency decorrelation). |
| **UniBCI** (arXiv:2605.00061) | Unified pretrained model for invasive BCIs. Spatio-temporal tokenization + interval-area attention + self-supervised masked reconstruction. Multi-species neural decoding, motor decoding, classification, regression. | `SOURCE_CLAIM` | Bridges to AMOS C04 (invasive BCI foundation model) and C02 (spatio-temporal tokenization for neural spike data). |

### Quantum Error Correction / Fault-Tolerant Computing

| Paper | Key result | Epistemic class | AMOS bridge |
| :--- | :--- | :--- | :--- |
| **τ-Helix compact FT architecture** (arXiv:2609.03194, Quantinuum, Sep 2026) | Experimental validation on 98-qubit trapped-ion Helios. Repeated QEC with error per logical qubit per cycle. Complete Clifford group on 2 logical qubits under active correction. Heterogeneous τ-Helix ↔ surface code GHZ state. Encoded outperforms unencoded without postselection. | `SOURCE_CLAIM` (experimental) | Bridges to AMOS C03 Physics-Cosmos (fault-tolerant architecture validation) and L23 MVCC-CAS (logical operation correctness under concurrent error correction). |
| **Cornucopia codes** (arXiv:2608.02773) | qLDPC codes with ultra-high encoding rate >1/2, pseudo-threshold >0.4%. `` block encodes 1426 logical qubits, extrapolated logical error 2.6×10⁻¹⁶ at 0.1% physical error. 12 entangling layers per syndrome cycle, independent of code size. Neutral-atom array compatible. | `SOURCE_CLAIM` | Bridges to AMOS C03 (quantum error correction at ultra-low overhead) and C02 (encoding efficiency optimization). |
| **NOBOL** (arXiv:2609.01901) | Single Bell-pair logical CNOT for distant qubits in arbitrary CSS codes. Depth-optimal circuit with logarithmic depth. Hardware-agnostic, effective for monolithic and distributed architectures. | `SOURCE_CLAIM` | Bridges to AMOS C03 (low-overhead fault-tolerant gate operations) and C09 (distributed quantum computing resource allocation). |
| **Spin-qubit shuttling bus** (arXiv:2609.02641) | Multi-qubit shuttling bus for transversal gates + magic state distillation. All-to-all logical connectivity via coherent spin shuttling. 2D grid reduces inter-qubit distance. 15-to-1 magic state distillation optimized via Quantum Reverse Mapping. | `SOURCE_CLAIM` | Bridges to AMOS C03 (spin-qubit architecture co-design) and C10 Tech-Engineering (hardware-software co-design methodology). |
| **High-rank encoding** (arXiv:2609.00778) | Intrinsic encoding randomness (mixed code states from pure inputs) can improve optimal entanglement fidelity. Rank-one encoder loss bounded quadratic near perfect recovery. | `SOURCE_CLAIM` | Bridges to AMOS C03 (approximate QEC theory) and C02 (optimization over encoder rank). |

### AI Reasoning / Test-Time Compute Scaling

| Paper | Key result | Epistemic class | AMOS bridge |
| :--- | :--- | :--- | :--- |
| **Test-Time Scaling survey** (arXiv:2608.04001) | Systematic account: 3 structural regimes (single-trajectory, leaf-level, prefix-level). Evaluation principles separating system performance from candidate-bank diagnostics. 2B+ reasoning traces released. | `SOURCE_CLAIM` (survey) | Bridges to AMOS C05 (cognitive compute allocation) and RSCF (evaluation protocol = epistemic regime classification). |
| **Adaptive TTC via Constrained Policy Optimization** (arXiv:2604.14853) | Constrained optimization: maximize accuracy subject to average compute budget. Lagrangian relaxation → per-instance oracle. SOLVE-THEN-LEARN pipeline. 12.8% relative improvement on MATH. | `SOURCE_CLAIM` | Bridges to AMOS C02 (constrained optimization) and C05 (adaptive reasoning effort allocation). |
| **Learning When to Think** (arXiv:2608.20256) | 3-mode routing (NoThink/Short/Long) learned inside GRPO. 41% token reduction at matched accuracy. Router sorts by difficulty. Transfers to unseen benchmarks. | `SOURCE_CLAIM` | Bridges to AMOS C05 (metacognitive reasoning mode selection) and L16 HML (H/M/L speed lens = NoThink/Short/Long). |
| **AERA** (arXiv:2608.27964) | Adaptive Evidence Residual Allocation: sequential controller learns whether additional computation will recover better answer. 92.61% accuracy vs 93.01% with 128 responses, 95.99% token reduction. Non-monotonic checkpoint correctness. | `SOURCE_CLAIM` | Bridges to AMOS C05 (evidence-residual reasoning) and RSCF (confidence ≠ correctness — present evidence may weaken before recovery). |
| **Divergent-Convergent Reasoning (DCR)** (arXiv:2608.15303) | Two-phase: exploration + reconciliation. Single reconciliation amplifies correct minority reports. Recursive DCR: 93.3% AIME 2024, 92.0% AIME 2025, 27% less compute. Dispersion metric predicts test-time gains. | `SOURCE_CLAIM` | Bridges to AMOS C05 (divergent-convergent cognitive primitive) and C08 (minority report amplification = game-theoretic reasoning). |

### Neuromorphic Computing

| Paper | Key result | Epistemic class | AMOS bridge |
| :--- | :--- | :--- | :--- |
| **SpiNNaker2** (arXiv:2607.24396) | 152-PE neuromorphic chip: ARM M4F + accelerators. 4.5 TOPS INT8, 2.7 TOPS/W efficiency. >150K neurons, >1.8B synaptic events/s. <250mW baseline. Bridges deep networks + SNNs. | `SOURCE_CLAIM` (hardware validated) | Bridges to AMOS C04 (neuromorphic substrate for neural computation) and C10 (hardware-software co-design). |
| **AIGOR** (arXiv:2607.03191) | Modular event-driven neuromorphic architecture. Configurable neuron model, precision, folding, partitioning. Declarative specification → generated cores. Validated on AMD Versal VPK180. | `SOURCE_CLAIM` | Bridges to AMOS C10 (reconfigurable hardware architecture) and C04 (configurable SNN inference). |
| **HiAER-Spike** (arXiv:2602.18072) | 160M neurons, 40B synapses (2× mouse brain) at faster-than-real-time. Hierarchical address event routing. Python interface, web portal. CIFAR-10, DVS gesture, MNIST, Pong. | `SOURCE_CLAIM` | Bridges to AMOS C04 (scale of neuromorphic computation) and C02 (massively parallel event-driven processing). |
| **NGN** (arXiv:2608.17394) | Noisy group neurons with synchronous resetting. Population-level reset + neural stochasticity. 87.35% CIFAR10-DVS in 10 time steps. | `SOURCE_CLAIM` | Bridges to AMOS C04 (bio-inspired neuronal dynamics) and C02 (stochastic regularization via population reset). |

### AI Agent Memory / Multi-Agent Systems

| Paper | Key result | Epistemic class | AMOS bridge |
| :--- | :--- | :--- | :--- |
| **CAMA** (arXiv:2608.19701) | Correlation-Aware Memory Arbitration: decouples retrieved memories, recovers missing independent evidence. Prevents "Memory Correlation Bias" (false majority from shared upstream sources). | `SOURCE_CLAIM` | **Direct bridge to AMOS K-Sybil-Hardening**: apparent multiplicity ≠ independent evidence. CAMA's dependency inference = AMOS provenance sybil hardening for agent memory. |
| **Mesh Memory Protocol (MMP)** (arXiv:2604.19540) | Semantic infrastructure for cross-session agent-to-agent collaboration. CAT7 7-field schema, SVAF field-level evaluation, inter-agent lineage (content-hash), remix (role-evaluated understanding). Production-deployed. | `SOURCE_CLAIM` | **Direct bridge to AMOS Memory Systems**: CAT7 schema = AMOS typed memory atoms. Inter-agent lineage = AMOS provenance chain. Remix = AMOS action-memory firewall (receiver stores own understanding, not raw peer signal). |
| **Prism** (arXiv:2604.19795) | Evolutionary memory substrate: entropy-gated stratification (skills/notes/attempts), causal memory graph with interventional edges, Value-of-Information retrieval, heartbeat-driven consolidation, replicator-decay dynamics. 88.1 LLM-as-Judge on LOCOMO. | `SOURCE_CLAIM` | Bridges to AMOS Memory Systems (stratified memory = AMOS 3-type memory), Causal Reasoning (interventional edges = do-calculus), and GMEF (evolutionary stable memory set = convergence detection). |
| **BMAM** (arXiv:2026.findings-acl.1973) | Brain-inspired multi-agent memory: episodic, semantic, salience-aware, control-oriented subsystems. 6-phase lifecycle. 78.45% LoCoMo. Soul Portability Test: 87.5% identity-integrity across export/clear/restore. | `SOURCE_CLAIM` | **Direct bridge to AMOS Identity Canon**: Soul Portability Test = AMOS identity continuity across memory export/restore. Brain-inspired decomposition = AMOS UBI 4-domain mapping to memory subsystems. |
| **MemMA** (arXiv:2603.18718) | Multi-agent memory cycle coordination: Meta-Thinker → Memory Manager + Query Reasoner. In-situ self-evolving construction (probe QA, verify, repair). Forward + backward path coordination. | `SOURCE_CLAIM` | Bridges to AMOS Memory Systems (construction-retrieval-utilization cycle = AMOS encode-consolidate-retrieve) and Audit-Repair (failure → memory repair action). |

### Key AMOS-relevant patterns across all findings

1. **Subject-invariance via adversarial training** (EEG-PRIME gradient reversal) mirrors AMOS K-Sybil-Hardening (suppress source-specific variation → independent evidence).
2. **Non-monotonic checkpoint correctness** (AERA) challenges the assumption that present confidence predicts future correctness — directly relevant to AMOS RSCF confidence ceiling semantics.
3. **Memory Correlation Bias** (CAMA) is the multi-agent generalization of AMOS Sybil hardening: correlated memories from shared upstream sources create false majorities.
4. **Soul Portability Test** (BMAM) provides an empirical protocol for AMOS Identity Continuity Canon: export → clear → restore → measure identity-integrity.
5. **Cornucopia codes** encoding rate >1/2 with 1426 logical qubits per block represents a step-change in QEC efficiency — the gap between physical and logical qubit overhead is narrowing faster than projected.
6. **Brain2Qwerty v2** demonstrates that non-invasive BCI is approaching invasive BCI performance through data scaling + LLM semantic extraction — the "non-invasive bandwidth ceiling" gap (listed as UNKNOWN/GAP above) may be partially bridgeable.

---

## SOTA Update — 2026-09-04 Phase 3 (arXiv late August / September 2026)

### Multi-Agent Memory & Collaboration (continued)

| Paper | Key result | Epistemic class | AMOS bridge |
| :--- | :--- | :--- | :--- |
| **Gated-Memory Routing** (arXiv:2609.00237, EMNLP 2026) | Memory Write Gate commits only non-redundant reasoning steps; Retrieval Gate supplies compact relevant subset; Adaptive Halting Controller stops when sufficient evidence. Best average accuracy + 31.9% HumanEval cost reduction. | `SOURCE_CLAIM` (peer-reviewed) | **Direct bridge to AMOS Memory Systems**: Write Gate = K_Memory_Admission (non-redundant admission); Retrieval Gate = K_Memory_Retrieval (compact relevant subset); Adaptive Halting = AMOS convergence detection (sufficient evidence → stop). |
| **PlanFence** (arXiv:2609.03340) | Dependency-scoped action-validation for distributed LLM agents. Plans cite exact public records; executor validates only records that can affect pending action. Stale-plan execution eliminated in 30/30 controlled workflows. | `SOURCE_CLAIM` | **Direct bridge to AMOS Causal Epoch + Action-Memory Firewall**: PlanFence's dependency-scoped validation = AMOS causal epoch finality (plan validity tied to source epoch). "Fresh memory ≠ valid plan" = AMOS "Memory ≠ Knowledge" boundary. |
| **MAP-Graph** (arXiv:2608.10509) | Provenance-aware memory layer: typed execution graph, ancestry tracing, permission-ineligible exclusion, multiplicative path trust reranking, risk-sensitive action gate. 94.96% task success, 72.70% exact decision accuracy. | `SOURCE_CLAIM` | **Direct bridge to AMOS Provenance Trust Firewall + K-Binding**: MAP-Graph's permission filtering = AMOS K-Binding validation; path trust = AMOS provenance chain trust; risk-sensitive gate = AMOS commit-time gating. Provenance as operational control signal, not just audit metadata. |
| **SRMA / Bilevel Coordinated Reflection** (arXiv:2609.02750) | Game-theoretic orchestrator-worker model. Bilevel coordination game with approximate potential game equilibrium. SRMA accepts memory only after grounded evaluation risk decreases. 72.2% SWE-bench. Information-theoretic impossibility: no transcript-only gate can improve uniformly. | `SOURCE_CLAIM` | **Direct bridge to AMOS C08 Strategy Game + Memory Conflict Governor**: Bilevel game = AMOS C08 game-theoretic reasoning. SRMA's "accept only when risk decreases" = AMOS fail-closed memory admission. Impossibility result = AMOS RSCF boundary (transcript-only evidence is insufficient). |

### AI Reasoning / Test-Time Compute (continued)

| Paper | Key result | Epistemic class | AMOS bridge |
| :--- | :--- | :--- | :--- |
| **Budget-Difficulty Confounds** (arXiv:2609.03436) | Restart-controlled truncation probe: only 1/178 cells show prefix-limited value. Problem-difficulty baseline reaches AUROC 0.873 on 192K traces — within published probe range. Early-window "breakthrough" signals are difficulty proxies, not within-attempt information. | `SOURCE_CLAIM` | **Direct bridge to AMOS RSCF**: Confounds problem-difficulty with trajectory information. AMOS RSCF must distinguish "the problem was hard" from "the reasoning path was wrong" — this paper shows that's harder than expected. |
| **TTS in the Wild** (arXiv:2608.18931) | Exploitation, not exploration, is the bottleneck. Oracle quality improves with compute, but reward models correlate at ρ̂_v ≈ 0.12 with true quality — selection near-random. Only Fusion (synthesis across candidates) consistently improves. | `SOURCE_CLAIM` | Bridges to AMOS C05 (cognitive exploitation vs exploration) and RSCF (verifier reliability is `UNKNOWN/GAP` for open-ended tasks). |
| **Thinking Hard, Not Smart** (arXiv:2608.07968) | Models fail to ration test-time compute across questions. Greedy sequential solvers, front-load effort, insensitive to value. Planning prompts don't fix it. | `SOURCE_CLAIM` | Bridges to AMOS C05 (metacognitive resource allocation) and C08 (strategic prioritization). Models lack AMOS-style value-aware prioritization. |

### Quantum Error Correction (continued)

| Paper | Key result | Epistemic class | AMOS bridge |
| :--- | :--- | :--- | :--- |
| **L-NBP** (arXiv:2608.27682) | Logical Neural Belief Propagation: redirects decoding from physical to logical level. 17.5% threshold under depolarizing noise. Distance-9 surface code: matches BP-OSD at 0.2% of complexity. | `SOURCE_CLAIM` | Bridges to AMOS C03 (QEC decoding efficiency) and C02 (linear-complexity neural decoding). |
| **SpiderLS** (arXiv:2608.30228) | Full ZX reduction for lattice surgery compilation. Derives execution order, multi-target operations, Pauli-product measurements. Reduces spacetime cost. | `SOURCE_CLAIM` | Bridges to AMOS C03 (fault-tolerant gate compilation) and C02 (compiler optimization). |
| **Superconducting surface-code processor** (arXiv:2606.06598) | Experimental lattice surgery on distance-3 surface codes. Per-cycle error 0.0365/0.0282. Logical Bell state, Deutsch-Jozsa, magic-state injection. RX(π/4) fidelity 0.943. | `SOURCE_CLAIM` (experimental) | Bridges to AMOS C03 (experimental QEC validation) — first lattice surgery on superconducting hardware. |

### BCI / Neural Decoding (continued)

| Paper | Key result | Epistemic class | AMOS bridge |
| :--- | :--- | :--- | :--- |
| **EEG-AS** (arXiv:2609.00653) | Instance-level algorithm selection for EEG foundation models. Learns to reconstruct unavailable model behaviors from privileged prediction tokens. Narrows SBS-to-oracle gap. | `SOURCE_CLAIM` | Bridges to AMOS C04 (adaptive model selection for neural decoding) and C02 (algorithm selection as optimization). |
| **cBCI Decision Correctness** (arXiv:2609.02436) | Pre-emptive EEG signal of decision correctness available within response window. Team voting weighted by neural signal: 57%→88% on contested trials under high workload. Detrimental under low workload. | `SOURCE_CLAIM` | Bridges to AMOS C05 (pre-emptive cognitive state detection) and C08 (team decision augmentation). Workload-conditional — not general-purpose. |

### Neuromorphic Computing (continued)

| Paper | Key result | Epistemic class | AMOS bridge |
| :--- | :--- | :--- | :--- |
| **Lonic** (arXiv:2608.12500, ICCAD 2026) | INT4 fully local online SNN training. Algorithm-hardware co-design. 66.28x energy improvement vs Nvidia V100. 15.95x vs ASIC TPU. | `SOURCE_CLAIM` (peer-reviewed) | Bridges to AMOS C04 (neuromorphic training efficiency) and C10 (algorithm-hardware co-design). |
| **M-HySMap** (arXiv:2608.26223) | Activity-weighted multicast hypergraph mapping for SNNs on mesh NoCs. 10.6-19.6% routed multicast hop reduction. Incremental updates 4.7-12.7x faster. | `SOURCE_CLAIM` | Bridges to AMOS C04 (neuromorphic hardware mapping) and C02 (hypergraph partitioning optimization). |
| **Biomedical neuromorphic edge** (arXiv:2609.03174) | FPGA SCNN for hypoxia classification. 88.26% accuracy, 1.455W. Hardware-software co-design flow. | `SOURCE_CLAIM` | Bridges to AMOS C04 (edge neuromorphic inference) and C10 (biomedical application). |

### Key AMOS-relevant patterns from Phase 3

1. **PlanFence's stale-plan execution** is the distributed-agent generalization of AMOS causal epoch finality: fresh memory does not establish plan validity. The plan's dependency closure must be validated, not just the latest state.
2. **MAP-Graph's provenance as operational control** directly validates AMOS Provenance Trust Firewall design: provenance is not just audit metadata but an active control signal that gates actions.
3. **Gated-Memory Routing** provides a concrete architecture for AMOS K_Memory_Admission: the Write Gate is the admission filter, the Retrieval Gate is the compaction-aware retrieval, and Adaptive Halting is convergence detection.
4. **SRMA's impossibility result** (no transcript-only gate can improve uniformly) validates AMOS RSCF's requirement for environment-grounded evidence — transcript-only reasoning is structurally insufficient.
5. **Budget-Difficulty Confounds** shows that early-window "breakthrough" signals in reasoning traces are problem-difficulty proxies, not within-attempt information. AMOS RSCF must control for difficulty when evaluating reasoning quality.
6. **TTS exploitation bottleneck** (ρ̂_v ≈ 0.12 reward model correlation) means that for open-ended tasks, the verifier is the weak link. AMOS must not assume verifier reliability for non-verifiable tasks.

---

## SOTA Update — 2026-09-04 Phase 4 (AI Safety / Interpretability + Quantum Hardware)

### AI Safety & Mechanistic Interpretability

| Paper | Key result | Epistemic class | AMOS bridge |
| :--- | :--- | :--- | :--- |
| **Circuit-Guided Weight Scaling** (arXiv:2609.00051, EMNLP 2026 Findings) | Three-stage safety circuit: Harmful Detection Heads → Safety Neurons → Refusal Heads. Circuit-guided scaling improves safety rates by 26.5% under attacks with only 1.7% accuracy drop. Causal evidence via targeted interventions. Recurs across architectures. | `SOURCE_CLAIM` (peer-reviewed) | **Direct bridge to AMOS C05 + Security**: Safety circuit decomposition maps to AMOS layered enforcement (detection → mediation → refusal). Weight scaling = AMOS capability attenuation without architecture change. |
| **ObserverBench** (arXiv:2609.03026) | Benchmark for testing whether internal estimators are adequate for intervention/control/safety tasks. Estimation accuracy ≠ action quality. AUROC can rank monitors differently from deployment loss. Sparse SAE readouts trail dense controls. | `SOURCE_CLAIM` | **Direct bridge to AMOS RSCF + Observability**: ObserverBench's "accurate on average ≠ chooses good action" = AMOS RSCF "confidence ≠ correctness". Separates estimation quality from intervention quality — AMOS observability must do the same. |
| **Representational Alignment** (arXiv:2609.04022) | Prototype-based moral categorization is weakly preserved in LLMs. Representational similarity optimization aligns latent representations with human moral judgement structure. Improves adversarial robustness across scales. Behavioral alignment leaves categorization structure unchanged. | `SOURCE_CLAIM` | Bridges to AMOS C05 (moral cognition) and K_UBI (biological intelligence domains). Prototype-based categorization = AMOS UBI social domain. Representational alignment > behavioral alignment for robustness. |
| **SafeRI** (arXiv:2609.03544) | On-demand safety intervention for VLMs: streaming recognizer estimates token-level safety, gates LoRA module. Safety as on-demand intervention, not permanent modification. | `SOURCE_CLAIM` | **Direct bridge to AMOS Action-Memory Firewall**: SafeRI's on-demand intervention = AMOS action-memory firewall (safety gate activates only when needed, not always-on). Always-on intervention degrades general capability. |
| **Legibility ≠ Interpretability** (arXiv:2609.04194) | LLM judges can identify high-advantage reasoning steps but fall well short of noise ceiling. Step importance only partially recoverable from reasoning trace text. Fine-tuning helps for incorrect responses but not correct ones. | `SOURCE_CLAIM` | **Direct bridge to AMOS RSCF**: "Legibility ≠ Interpretability" = AMOS "DOCUMENTED != IMPLEMENTED". Reasoning trace text does not encode functional role reliably. AMOS must not treat reasoning traces as transparent windows. |

### Quantum Hardware & Architecture

| Paper | Key result | Epistemic class | AMOS bridge |
| :--- | :--- | :--- | :--- |
| **Neutral atom toric code** (arXiv:2606.04079) | Repeated QEC in toric code on neutral atom array. Mid-circuit measurement, qubit replacement, reservoir reloading for indefinite operation. Up to 90 cycles. Larger distance = lower absolute logical error. | `SOURCE_CLAIM` (experimental) | Bridges to AMOS C03 (experimental QEC with indefinite operation via reservoir reloading). |
| **Static atomic buses** (arXiv:2607.02804) | Neutral-atom architecture with auxiliary mediator atoms for long-range entanglement without transport. 99.9% bus-mediated CZ gate fidelity. >10x logical error improvement vs shuttling. QEC cycle ~1ms for d<12. | `SOURCE_CLAIM` | Bridges to AMOS C03 (hardware architecture for fault-tolerant QEC) and C10 (hardware-software co-design). |
| **Parity Twine Networks** (arXiv:2609.03583) | Hardware-aware optimization for neutral-atom parity architecture. CZ/CZSWAP/iSWAP variants. 30-qubit QFT: 3 orders of magnitude higher fidelity than competing compilation. | `SOURCE_CLAIM` | Bridges to AMOS C02 (compiler optimization) and C03 (quantum circuit compilation). |
| **Neutral atom computing review** (arXiv:2608.30783) | Comprehensive review of neutral atom quantum computing: physics, current capabilities, outlook. | `SOURCE_CLAIM` (survey) | Bridges to AMOS C03 (quantum hardware landscape). |
| **Infleqtion Sqale** (arXiv:2509.13247) | 114 neutral atom qubits. Motion + in-place entanglement. Logical Shor's Algorithm with better-than-physical performance. CNOT ladder depth independent of N and d. `` many-hypercube QEC code initialization. | `SOURCE_CLAIM` (experimental) | Bridges to AMOS C03 (logical algorithm execution on neutral atom hardware). |

### Key AMOS-relevant patterns from Phase 4

1. **Safety circuit decomposition** (Detection → Mediation → Refusal) mirrors AMOS layered enforcement: detect harmful intent → mediate via safety neurons → refuse at output. This is a three-layer enforcement chain, exactly like AMOS enforcement trust contract.
2. **ObserverBench's estimation ≠ action quality** is a generalization of AMOS RSCF: an observer that is accurate on average can still choose poor actions. AMOS must evaluate observability by action quality, not just estimation accuracy.
3. **SafeRI's on-demand intervention** validates AMOS action-memory firewall design: always-on safety intervention degrades general capability. Safety should be gated, not permanent.
4. **Legibility ≠ Interpretability** is the reasoning-trace version of AMOS "DOCUMENTED != IMPLEMENTED": the text of a reasoning step does not reliably encode its functional role. AMOS must not treat reasoning traces as transparent.
5. **Representational alignment > behavioral alignment** for adversarial robustness: aligning latent representations with human moral structure is more robust than aligning only observable responses. This suggests AMOS UBI alignment should operate at the representation level, not just the behavior level.
6. **Neutral atom QEC reaching indefinite operation** (reservoir reloading + mid-circuit measurement) is a hardware milestone: the gap between experimental QEC and practical fault-tolerant computing is narrowing.

---

**Origin Architect / Steward:** Trang Phan

---

[[00_ROOT/00_ROOT_MOC|AMOS MOC]] · [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
