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

See: [[21_DOMAINS/14_C04_BIO_NEURO/14_C04_BIO_NEURO_MOC|C04 Bio Neuro]] · [[07_SKILLS/amos-c04-bio-neuro-master|C04 Master Skill]]

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
- [[07_SKILLS/amos-c04-bio-neuro-master|C04 Master Skill]] — bio-neuro domain skill.
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

**Origin Architect / Steward:** Trang Phan

---

[[00_ROOT/00_ROOT_MOC|AMOS MOC]] · [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
