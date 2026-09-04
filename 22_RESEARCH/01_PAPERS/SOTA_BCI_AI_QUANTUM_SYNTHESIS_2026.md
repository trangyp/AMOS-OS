---
title: "State of the Art Synthesis 2026: BCI, Neuromorphic AI, and Quantum Systems"
type: research_synthesis
plane: 22_RESEARCH
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_SYNTHESIS
updated: 2026-09-05
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 66,000+ ArXiv corpus synthesis
    - Master Drive Research Assets
    - Arvix Quantum 2026-05 and rest-of-year audit outputs
    - public web corpus snapshot 2026-09-04
  scope: state_of_the_art_research_2026
---

# State of the Art Synthesis 2026: BCI, Neuromorphic AI, and Quantum Systems

**Origin Architect / Steward:** Trang Phan
**AMOS_CORE Target:** `v4.4`
**Epistemic Class:** `AMOS_MODEL`
**Freshness:** `2026-09-04`

---

## 1. Cross-Disciplinary Convergence Matrix

This document unifies empirical breakthroughs from the ArXiv corpus (66,000+ preprints), the AMOS Drive research assets, and a public web snapshot into the AMOS v4.4 Full Brain Operating System across three pillars.

| Research Pillar | Key Breakthroughs Ingested | Primary AMOS Plane Integration | Impact on AMOS Full Brain OS |
| :--- | :--- | :--- | :--- |
| **Brain-Computer Interfaces (BCI)** | Long-term independent home use of intracortical speech + cursor BCI (Nature Medicine 2026); bimanual typing neuroprosthesis (Nature Neuroscience 2026); sensory-guided human-machine joint learning for EEG motor imagery (Nature Communications 2026); EEG foundation models (DeeperBrain, NeuroAtlas, EDAPT) | `05_COGNITIVE_ORGANISM`, `26_UBI_SI`, `01_CANON/03` | Real-time `< 10 ms` cognitive intent decoding, bidirectional neural symbiosis, and robust cross-subject/cross-paradigm generalization |
| **Neuromorphic & Bio-Computing** | Triplet STDP, asynchronous event fabrics, spiking neural networks (SNNs), Brain-Inspired BCIs (BI-BCIs), closed-loop optogenetics and tactile-encoded supernumerary control | `24_UBI_NBI`, `01_CANON/03`, `03_CONTROL_PLANE` | Energy-optimal neuromorphic substrate (`< 1 pJ/event`), closed-loop adaptation, and low-power event-driven inference |
| **Quantum Systems & Quantum-AI** | Fermionic unitary brick-wall circuits with tunable classical hardness, autotuning quantum compilation (TuniQ), exponential quantum advantage for massive classical data, transformer-based molecular ground-state circuit generation (ADAPT-GQE), Bernstein-Vazirani Networks (BVNs) | `21_DOMAINS/41_QUANTUM`, `22_RESEARCH/01`, `04_RUNTIME` | Fault-tolerant quantum compilation, quantum advantage domains, and cryptographic entropy grounding for AMOS control-plane primitives |

---

## 2. Invariant Epistemic Grounding

```text
EMPIRICAL_BREAKTHROUGH != PRODUCTION_COMMIT
THEORETICAL_MODEL != DEPLOYED_PHYSICAL_HARDWARE
SIMULATION_VALIDATED != SYSTEMIC_CLOSURE
ARXIV_INGESTION != CANON_PROMOTION
WEB_SNAPSHOT != PEER_REVIEWED_EVIDENCE
```

---

## 3. Brain-Computer Interfaces — 2026 State of the Art

### 3.1 Intracortical speech + cursor BCI

- **Source:** *Long-term independent use of an intracortical brain-computer interface for speech and cursor control* (Nature Medicine, 2026)
- **Scope:** A participant with ALS and severe dysarthria used a multimodal intracortical BCI at home, without researchers, for nearly 2 years and >3,800 hours.
- **Performance:** >99% word accuracy on a 125,000-word vocabulary; 56 words per minute average; >92% of 183,060 sentences self-rated at least mostly correct.
- **World effect:** Personal computer control (keyboard + mouse), texting, email, internet browsing, sustained full-time employment.
- **AMOS relevance:** Demonstrates a real-world `human → BCI → effector` loop with long-term independent operation. Maps onto AMOS `PERSONALITY`/`EXPRESSION_TRANSLATION` input field, `OMNI_KERNEL` routing, `BRAIN_CORE` decoding, and `INFRASTRUCTURE_CONTROL_PLANE` authorization before `HOST_DEPLOYMENT` and `WORLD_EFFECT`.

### 3.2 Bimanual typing neuroprosthesis

- **Source:** *Restoring rapid natural bimanual typing with a neuroprosthesis after paralysis* (Nature Neuroscience, 2026)
- **Scope:** iBCI typing using attempted finger movements on a QWERTY keyboard; as few as 30 calibration sentences.
- **Performance:** 110 characters per minute, 22 words per minute, 1.6% word error rate.
- **AMOS relevance:** High-throughput, familiar-effector human-machine interface. Reinforces the AMOS design principle that motor intent decoding should align with existing human skill rather than requiring entirely new control schemes.

### 3.3 Sensory-guided human-machine joint learning

- **Source:** *Sensory-guided human-machine joint learning accelerates the acquisition of motor imagery BCI control* (Nature Communications, 2026)
- **Scope:** EEG motor imagery in 31 BCI-naïve users.
- **Performance:** 86.0% (1D) and 77.5% (2D) online discrete accuracies; 77.5% continuous control (1D), 66.9% (2D).
- **AMOS relevance:** Provides empirical grounding for **adaptive complexity** and **human-machine co-learning** in the AMOS Runtime. The decoder and the user learn simultaneously, aligning with the AMOS `RSCF` competing-hypotheses / repair loop.

### 3.4 Non-invasive EEG foundation models

- **Representative ArXiv corpus entries (2026):**
  - `2601.06134v2_DeeperBrain__A_Neuro-Grounded_EEG_Foundation_Model_Towards_Universal_BCI`
  - `2605.14698v1_NeuroAtlas__Benchmarking_Foundation_Models_for_Clinical_EEG_and_Brain-Computer_I`
  - `2608.10474v1_EDAPT__Towards_Calibration-Free_BCIs_with_Continual_Online_Adaptation`
  - `2604.14202v1_Bridging_scalp_and_intracranial_EEG_in_BCI_via_pretrained_neural_representations`
- **AMOS relevance:** Foundation models for EEG move the field from per-subject calibration toward universal, transfer-learnable neural representations. They are candidate `BRAIN_CORE` engines under the UBI stack and `OMNI_KERNEL` adaptive routing.

---

## 4. Neuromorphic & Brain-Inspired AI — 2026 State of the Art

- **Source:** *Towards neuromorphic neurotechnologies: integrating brain-inspired computing with brain-computer interfaces* (npj Biomedical Innovations, 2026)
- **Key idea:** Brain-Inspired Brain-Computer Interfaces (BI-BCIs) — unifying low-power, closed-loop, miniaturized neuromorphic neurotechnologies.
- **Techniques:** Spiking neural networks (SNNs), asynchronous event-based representation (AER), triplet STDP, closed-loop PWM optogenetics, tactile-encoded supernumerary control.
- **AMOS relevance:** Directly maps to the `BRAIN_CORE` engine ecosystem (UBI_NBI, neuroemotional, somatic) and `OMNI_KERNEL` minimum-activation routing. Provides empirical support for event-driven, energy-bound cognitive loops inside AMOS Runtime.

---

## 5. Quantum Systems & Quantum-AI — 2026 State of the Art

### 5.1 Scalable quantum machine learning

- **Source:** *Scalable Quantum Machine Learning: Trainability, Expressivity and Efficiency* (arXiv 2607.24014)
- **Key idea:** Unitary brick-wall circuit with tunable fermionic particle number `k`; tunable classical hardness; parallel parameter-shift rule reducing gradient evaluations by a factor `3n/(8k)`.
- **AMOS relevance:** Candidate quantum engine for the `04_RUNTIME` probabilistic / optimization family and `21_DOMAINS/41_QUANTUM`.

### 5.2 Autotuning quantum compilation

- **Source:** *TuniQ: Autotuning Compilation Passes for Quantum Workloads at Scale* (ACM, 2026)
- **Key idea:** RL-based compiler pass selection per pipeline stage, adaptive to circuit, backend, and noise profile.
- **AMOS relevance:** Maps onto `SUPER_CODE` / fabrication engines and `INFRASTRUCTURE_CONTROL_PLANE` optimization. Reinforces that compilation/effect pipelines require runtime adaptation, not static heuristics.

### 5.3 Exponential quantum advantage for classical data

- **Source:** *Exponential quantum advantage in processing massive classical data* (Google Quantum AI / Caltech, arXiv 2604.07639)
- **Claim:** A small quantum computer of polylogarithmic size can classify and dimensionally reduce massive classical data with exponentially smaller classical resource requirements; validated on single-cell RNA sequencing and sentiment analysis (4–6 orders of magnitude resource reduction, <60 logical qubits).
- **AMOS relevance:** Provides a bounded, empirically reported quantum advantage domain. Treated as `SOURCE_CLAIM` pending independent reproduction and scope validation; not treated as universal AMOS capability.

### 5.4 AI-generated quantum chemistry circuits

- **Source:** *Learning to Prepare Molecular Ground States with Transformer Models* (arXiv 2607.22468)
- **Key idea:** ADAPT-GQE — transformer/LM trained to generate ground-state preparation circuits; executed on Quantinuum Helios-1.
- **AMOS relevance:** Demonstrates `C02_math_compute` / `C10_tech_engineering` cross-domain fabrication. A concrete case where a `BRAIN_CORE` model produces a deployable quantum artifact.

### 5.5 Bernstein-Vazirani Networks

- **Source:** *Bernstein–Vazirani Networks: Quantum Machine Learning by Interference* (arXiv 2608.19043)
- **Key idea:** Non-variational quantum ML using Fourier-basis interference; gradient-free; vision and representation learning tasks.
- **AMOS relevance:** Adds to the QML engine registry; useful as a `COMPETING_MODEL` entry under AMOS canon until independently benchmarked.

---

## 6. ArXiv Vault Cross-Reference

The separate ArXiv vault (`/Users/mac/Desktop/_Arxiv/Arvix`) contains 66,000+ preprints organized by year and month. Representative holdings directly relevant to AMOS planes:

| Domain | Sample vault paths | AMOS plane |
| :--- | :--- | :--- |
| BCI / EEG / neural interfaces | `.../2026/2026-07/C/2607.07185v3_Clinical_Translation_of_Brain-Computer_Interface_in_China*` | `05_COGNITIVE_ORGANISM` |
| EEG foundation models | `.../2026/2026-01/D/2601.06134v2_DeeperBrain*` | `01_CANON/03`, `BRAIN_CORE` |
| Quantum ML / QML | `.../2026/2026-07/2607.24014v1_Scalable_Quantum_Machine_Learning*` | `21_DOMAINS/41_QUANTUM` |
| Quantum chemistry + AI | `.../2026/2026-07/2607.22468_Learning_to_Prepare_Molecular_Ground_States*` | `C02`, `C10` |
| Quantum advantage | `.../2026/2026-04/2604.07639_Exponential_quantum_advantage_in_processing_massive_classical_data*` | `22_RESEARCH` |
| Neuromorphic / SNN | titles spanning 2025–2026 with `spiking`, `neuromorphic`, `SNN` | `BRAIN_CORE`, `OMNI_KERNEL` |

> **Canonical status:** These ArXiv files are external `SOURCE_CLAIM` / `COMPETING_MODEL` sources. They are not promoted to `01_CANON` without ingestion, RSCF framing, and explicit authority/promotion record.

---

## 7. AMOS Full Brain OS Integration Implications

1. **Input field:** BCI speech, typing, and motor-imagery signals are concrete `HUMAN / ENVIRONMENT → EXPRESSION_TRANSLATION` channels.
2. **Omni Kernel:** Adaptive routing (minimum sufficient region) is directly supported by EEG foundation models and user-decoder co-learning.
3. **Brain Core:** Neuromorphic computing and SNNs are candidate `BRAIN_CORE` engines; intracortical decoding is candidate `UBI_SI` / `UBI_NBI` capability.
4. **Omniverse Brain:** Quantum and BCI breakthroughs update the `Layer 4 Biological & Consciousness` and `Layer 2 Physical & Quantum` models.
5. **Runtime:** TuniQ and adaptive BCI training align with AMOS `REPAIR`, `REPLAY`, and `AUDIT` loops.
6. **Control Plane:** Long-term independent BCI use demonstrates real-world `authority → effect` governance under patient control — a human-in-the-loop authority model.
7. **Deployment:** Foundation models and neuromorphic chips are host-layer artifacts, not AMOS ontology definitions.

---

## 8. 2026 ArXiv Vault Representative Catalog

The external ArXiv vault (`/Users/mac/Desktop/_Arxiv/Arvix`) holds 66,000+ preprints. A 2026 keyword scan yields the following coverage counts and representative paths. These files are `SOURCE_CLAIM` candidates for future ingestion; they are not promoted to `01_CANON` without explicit authority/promotion record.

| Category | 2026 Files | Representative Vault Paths |
| --- | --- | --- |
| **BCI & Neural Interfaces** | 110 | `2026/2026-01/D/2601.06134v2_DeeperBrain__A_Neuro-Grounded_EEG_Foundation_Model_Towards_Universal_BCI.md` <br> `2026/2026-02/B/2602.23410v3_Brain-OF__An_Omnifunctional_Foundation_Model_for_fMRI__EEG_and_MEG.md` <br> `2026/2026-03/N/2603.16880v2_NeuroNarrator__A_Generalist_EEG-to-Text_Foundation_Model_for_Clinical_Interpreta.md` <br> `2026/2026-04/B/2604.14202v1_Bridging_scalp_and_intracranial_EEG_in_BCI_via_pretrained_neural_representations.md` <br> `2026/2026-04/U/2604.00349v1_Ultrasonic_Brain_Computer_Interfaces_for_Enhancing_Human-Machine_Cognition.md` |
| **Neuromorphic & SNN** | 87 | `2026/2026-01/S/2601.02401v1_Spiking_Heterogeneous_Graph_Attention_Networks.md` <br> `2026/2026-02/U/2602.11206v1_UltraLIF__Fully_Differentiable_Spiking_Neural_Networks_via_Ultradiscretization_a.md` <br> `2026/2026-04/B/2604.11665v5_Beyond_LLMs__Sparse_Distributed_Memory__and_Neuromorphics__A_Hyper-Dimensional_S.md` <br> `2026/2026-04/E/2604.27004v1_EdgeSpike__Spiking_Neural_Networks_for_Low-Power_Autonomous_Sensing_in_Edge_IoT_.md` <br> `2026/2026-05/C/2605.28387v1_CLANE__Continual_Learning_of_Actions_on_Neuromorphic_Hardware_from_Event_Cameras.md` |
| **Quantum Computing & QML** | 1454 | `2026/2026-01/S/2601.01263v1_Simulating_Wigner_Localisation_with_the_IBM_Heron_2_Quantum_Processor__A_Proof-o.md` <br> `2026/2026-01/S/2601.10964v3_Stabilizer_Code-Generic_Universal_Fault-Tolerant_Quantum_Computation.md` <br> `2026/2026-02/C/2602.14827v1_Constrained_Portfolio_Optimization_via_Quantum_Approximate_Optimization_Algorith.md` <br> `2026/2026-04/A/2604.07639_Exponential_quantum_advantage_in_processing_massive_classical_data*` <br> `2026/2026-07/2607.24014v1_Scalable_Quantum_Machine_Learning*` |
| **AI Agents & LLMs** | 4528 | `2026/2026-01/A/2601.08815v3_Agent_Contracts__A_Formal_Framework_for_Resource-Bounded_Autonomous_AI_Systems.md` <br> `2026/2026-01/A/2601.12560v1_Agentic_Artificial_Intelligence__AI___Architectures__Taxonomies__and_Evaluation_.md` <br> `2026/2026-01/A/2601.15311v3_Aeon__High-Performance_Neuro-Symbolic_Memory_Management_for_Long-Horizon_LLM_Age.md` <br> `2026/2026-01/I/2601.14209v1_InT__Self-Proposed_Interventions_Enable_Credit_Assignment_in_LLM_Reasoning.md` <br> `2026/2026-01/M/2601.00360v3_Mapping_Human_Anti-collusion_Mechanisms_to_Multi-agent_AI_Systems.md` |

> **Canonical status:** These ArXiv paths are external `SOURCE_CLAIM` references. Their presence in the Drive catalog does not imply ingestion, validation, or promotion into AMOS canon.

## 9. Quantum QML Skepticism — 2026 Rest-of-Year Audit Verdict

The Arvix vault contains dedicated audit outputs (`outputs/Quantum_2026-05_Audit.md` and `outputs/Quantum_2026_Rest-of-Year_Audit.md`) that test the QML skeptical thesis against the most on-point 2026 papers. The audited verdict is `MODEL / SOURCE_CLAIM`: it reports what those papers *claim and qualify*, not a universal truth about QML.

| Month | arXiv | Claim tested | Fair-classical-beating? |
| --- | --- | --- | --- |
| Feb | 2602.04239 | QTN / HSE / PINN vs classical on 1D Burgers | No — explicit disavowal; quantum-native blocked by O(N) readout. |
| Mar | 2603.09901 | Has quantum advantage been achieved? (Hangleiter) | "Yes" only for random circuit sampling, a "(nearly) useless task" with verification-hostile XEB. Not a useful, matched, verified win. |
| Apr | 2604.11541 | Noise effects in hybrid VQC | No beat claim — no classical baseline. |
| Jun | 2606.28655 | Entanglement effect on QML of pathogen epitope binding | Explicit disavowal: "These results do not establish a general QML advantage." |
| Jul | 2607.08220 | QLS-icMRLCC quantum chemistry; "prospects of exponential quantum advantage" | Conditional / theoretical only; κ scaling verified at ≤4-atom toy scale; one diagnostic rests on an adapted, unproven conjecture. |
| May | 2605.27923 | QSVM/QCNN multidimensional MNIST | No clean win — partial, cost-prohibitive, parity-converging at scale. |
| May | 2605.10801 | Photonic gate-based QNN vs matched ANN | Toy, classically simulable by authors' admission; only effective-dimension expressivity gap. |
| May | 2605.24324 | Matched spectral benchmark of quantum-inspired feature maps | Zero significant wins across 30 comparisons; 27 significantly worse. |

**AMOS relevance:** These audits instantiate the RSCF `COMPETING_MODEL` discipline. The strongest reproducible positive is **toy-scale expressivity** (effective dimension, ZZ feature-map overfitting gap) — a promising design target, not a deployed advantage. Any AMOS quantum engine must route to this boundary rather than treating "quantum advantage" as a default capability.

---

## 10. Public Web Snapshot — BCI, Neuromorphic, Quantum (2026-09-04)

The following public-web sources were surfaced on `2026-09-04` to cross-check the ArXiv corpus. They are `WEB_SNAPSHOT / SOURCE_CLAIM`; peer-review and independent reproduction should be verified before canonical use.

| Source | Title / Type | Key claim | AMOS relevance |
| --- | --- | --- | --- |
| https://www.nature.com/articles/s41591-026-04414-6 | Long-term independent use of an intracortical BCI (Nature Medicine, 2026) | >99% word accuracy, 56 wpm, >3,800 h independent home use | Confirms `HUMAN → BCI → EFFECTOR` loop under patient authority; `05_COGNITIVE_ORGANISM`, `03_CONTROL_PLANE` |
| https://www.biorxiv.org/content/10.64898/2026.07.23.739430v1 | A generalizable speech neuroprosthesis (bioRxiv, 2026) | Transformer decoder trained across 6 participants; multi-user model finetuned on <200 sentences to <7% WER | Supports cross-subject `BRAIN_CORE` decoding and `OMNI_KERNEL` adaptive routing |
| https://arxiv.org/pdf/2603.12279 | Toward Robust Intracranial Language BCIs (arXiv review, 2026) | Cross-subject/multilingual gaps, long-term non-stationarity, weak cross-subject transfer, heterogeneous evaluation | Defines falsifiers and `UNKNOWN/GAP` boundaries for BCI generalization claims |
| https://www.nature.com/articles/s41467-026-75455-1 | Shared latent representations for cross-patient speech decoding (Nature Communications, 2026) | Invasive ECoG cross-patient latent representations improve speech decoding | Maps to `PERSONALITY`/`EXPRESSION_TRANSLATION` generalization and `RSCF` competing hypotheses |
| https://www.nature.com/articles/s44287-026-00321-7 | Figures of merit for neuromorphic devices (Nature Reviews Electrical Engineering, 2026) | Unified bioplausibility / energy / scalability metrics for neuromorphic architectures | `24_UBI_NBI`, `OMNI_KERNEL` substrate selection |
| https://www.nature.com/articles/s42256-026-01255-3 | Dual memory pathway algorithm–hardware co-design (Nature Machine Intelligence, 2026) | SNN with cortical fast–slow memory; 40–60% fewer parameters; >4× throughput, >5× energy efficiency | Direct `BRAIN_CORE` / `OMNI_KERNEL` event-driven memory architecture candidate |
| https://arxiv.org/html/2607.24396 | SpiNNaker2 chip for brain-inspired computing (arXiv, 2026) | 152 ARM M4F PEs; up to 4.5 TOPS / 2.7 TOPS/W INT8; >150k neurons, >1.8 G synaptic events/s | `HOST_DEPLOYMENT` neuromorphic hardware baseline |
| https://www.nature.com/articles/s41534-026-01279-y | Advantage of QML from general computational advantages (npj Quantum Information, 2026) | Broader family of classical-data supervised learning tasks with provable QML advantage beyond Shor | `21_DOMAINS/41_QUANTUM`, `C02_math_compute` — candidate formal advantage domain |
| https://arxiv.org/pdf/2603.06644 | Quantum Deep Learning: A Comprehensive Review (arXiv, 2026) | Taxonomy: hybrid QNN, quantum DNN, quantum algorithms for DL primitives, quantum-inspired classical algorithms | `21_DOMAINS/41_QUANTUM` registry reference |

---

## 11. Gaps and Falsifiers

- **G1:** Public web snapshots are not peer-reviewed; they require ArXiv / DOI cross-check before canonical use.
- **G2:** 66,000+ ArXiv files are not individually ingested; the vault has not been parsed into RSCF objects.
- **G3:** Quantum advantage claims require independent reproduction and scope-specific validation.
- **G4:** Long-term BCI results are case-study scale; broad population validity is not established.
- **G5:** The 2026 ArXiv catalog is keyword-surfaced only; titles and abstracts have not been reviewed for relevance or quality.
- **G6:** The Arvix quantum audits are summary verdicts; individual paper bodies are not yet ingested as per-paper RSCF objects.
- **G7:** Public web sources are not the primary evidence layer; DOI / ArXiv cross-check and independent reproduction are required before canonical use.

**Falsifiers:**

F1: A peer-reviewed retraction or failed reproduction of a cited 2026 result.
F2: AMOS code treats any of these results as `CANON` without explicit promotion record.
F3: A deployment artifact (skill, model, tool) is confused with an AMOS architectural definition.
F4: An ArXiv catalog entry is promoted to a source claim without reading and RSCF framing.
F5: A 2026 QML audit paper is later retracted or reproduced with contradictory results.
F6: A public web source is contradicted by its own peer-reviewed publication or withdrawn preprint.

---

RSCF-NODE
node_id: sota_bci_ai_quantum_synthesis_2026
node_type: research_synthesis
path: 22_RESEARCH/01_PAPERS/SOTA_BCI_AI_QUANTUM_SYNTHESIS_2026.md
RSCF-RELATIONS:
- INDEXED_BY: [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
- INDEXED_BY: [[22_RESEARCH/01_PAPERS/01_PAPERS_MOC|01_PAPERS_MOC]]
- RELATED_TO: [[01_CANON/03_COGNITION_CANON/AMOS_FULL_BRAIN_OS_MASTER_CANON|AMOS Full Brain OS Master Canon]]
- RELATED_TO: [[21_DOMAINS/21_DOMAINS_MOC|21_DOMAINS_MOC]]
- RELATED_TO: [[22_RESEARCH/01_PAPERS/SOTA_HARVEST_2026-09-04|SOTA Harvest 2026-09-04]]

---

## 11. SOTA Update — 2026-09-05 Harvest

### 11.1 BCI — Cross-Subject Neural Speech Decoding

| Paper | Source | Key Finding | AMOS Binding |
|-------|--------|-------------|--------------|
| Boccato et al. 2026 — Cross-subject decoding for speech BCI | J. Neural Eng. 23(4):046018 | First neural-to-phoneme decoder trained jointly on two largest intracortical speech datasets; hierarchical GRU with CTC + feedback; cross-subject pretraining feasible without performance degradation; adapts to unseen subjects via linear transform | `05_COGNITIVE_ORGANISM/UNIVERSAL_BCI_NEURAL_DECODING_ARCHITECTURE` |
| Brain2Qwerty v2 — Non-invasive MEG brain-to-text | arXiv:2608.18114 (Meta/PSL) | 39% WER from real-time MEG; 22k sentences × 9 subjects × 10h; log-linear improvement with data volume; AI agents for iterative pipeline refinement | `05_COGNITIVE_ORGANISM` |
| BrainWhisperer — ASR-pretrained neural speech decoder | arXiv:2603.13321 | Whisper encoder + neural features; windowed self-attention; hierarchical low-rank projections; sub-100ms inference; cross-dataset generalization without fine-tuning | `05_COGNITIVE_ORGANISM` |
| Khanday et al. 2026 — End-to-end Conformer intracortical decoder | Odyssey 2026 | CER 23.80% without external LM; inter-session degradation drives variability; word boundary segmentation is dominant error source | `05_COGNITIVE_ORGANISM` |
| CMU adaptive AI + human motor learning BCI | Nature Communications 2026 | Non-invasive BCI with co-adaptive AI + human learning reduces training time and improves performance | `05_COGNITIVE_ORGANISM` |

**AMOS Integration:** Cross-subject pretraining directly supports the `UNIVERSAL_BCI_NEURAL_DECODING_ARCHITECTURE` goal of subject-independent neural decoding. The hierarchical GRU+CTC architecture maps to the AMOS cognition engine's 6-layer architecture. Brain2Qwerty's AI-agent-driven pipeline refinement validates the AMOS automation engine's iterative improvement loop.

### 11.2 Quantum — Surface Code Error Correction

| Paper | Source | Key Finding | AMOS Binding |
|-------|--------|-------------|--------------|
| IBM heavy-hex surface code scaling | Nature Communications 2026 | Subthreshold scaling on heavy-hex; fold-unfold embedding with bridge ancillas; gap-aware dynamical decoupling; anisotropic (dx,dz) scaling; 30% noise reduction would enable (5,5) | `21_DOMAINS/41_QUANTUM_SYSTEMS` |
| RL control of quantum error correction | Nature 2026 | RL agent manages 1000+ control parameters; 3.5× logical stability improvement; record surface code error 7.72×10⁻⁴/cycle; color code 8.19×10⁻³/cycle; never-stop-computing paradigm | `21_DOMAINS/41_QUANTUM_SYSTEMS/SURFACE_CODE_SYNDROME_DECODER_LEDGER` |
| L-NBP — Logical Neural Belief Propagation | arXiv:2608.27682 | Linear-complexity neural decoder; redirects to logical-level decoding; 17.5% threshold under depolarizing noise; 0.2× complexity of BP-OSD at distance-9 | `21_DOMAINS/41_QUANTUM_SYSTEMS` |
| FPGA NN decoder for real-time surface code | arXiv:2605.04892 | 550ns closed-loop latency; 124ns NN decoding; 1.25μs QEC cycle; mid-circuit feedback in non-Clifford circuits | `21_DOMAINS/41_QUANTUM_SYSTEMS` |
| Lattice surgery surface-code processor | arXiv:2606.06598 | Distance-3 logical qubits; per-cycle error 3.65% and 2.82%; logical Bell state; Deutsch-Jozsa at logical level; magic-state injection; R_X(π/4) fidelity 94.3% | `21_DOMAINS/41_QUANTUM_SYSTEMS` |

**AMOS Integration:** The RL-controlled QEC paradigm maps directly to the AMOS adaptive stability balancer — the quantum computer "learns from its errors and never stops computing," mirroring AMOS's continuous evolution loop with rollback. The FPGA NN decoder's 550ns latency sets the real-time constraint for the `SURFACE_CODE_SYNDROME_DECODER_LEDGER`. Lattice surgery establishes the fault-tolerant logical operation framework for AMOS quantum domain modeling.

### 11.3 AI — Multi-Agent Autonomous Reasoning

| Paper | Source | Key Finding | AMOS Binding |
|-------|--------|-------------|--------------|
| DeAR — Decentralized Agentic Reasoning | arXiv:2608.17282 | P2P collaboration replacing central control; capability grounding; thought map navigation; topology update for error correction; outperforms centralized baselines on 9 benchmarks | `03_CONTROL_PLANE` |
| Station — Autonomous Mathematical Discovery | arXiv:2608.23691 | Open-world multi-agent math discovery; no central coordinator; 5 novel results including Kakeya sets and kissing configurations; agents build shared scientific literature | `22_RESEARCH` |
| Codebook Agent — Topology design for LLM MAS | arXiv:2609.02264 | VQ-autoencoder compresses topologies to 16-entry codebook; 2.4ms topology emission; 21.9-33.2% fewer tokens; 84.6 avg accuracy | `03_CONTROL_PLANE` |
| ArcticSwarm — Long-horizon multi-agent research | arXiv:2609.01870 | Gated isolation prevents early consensus; 82.6% on BrowseComp-Plus; shared bulletin board; structured review at 3 commitment boundaries | `03_CONTROL_PLANE` |
| Leibniz — Theory-of-Mind neuro-symbolic reasoning | ACL 2026 | Bidirectional reasoning (Evolution + Reduction agents); shared belief state space; neuro-symbolic integration; outperforms SOTA in reasoning accuracy | `25_COGNITIVE_MATRIX` |
| SwarmWorld — Stigmergic technological evolution | arXiv:2608.26081 | LLM agent societies with stigmergic coordination; technological evolution emerges from agent interactions | `05_COGNITIVE_ORGANISM` |

**AMOS Integration:** DeAR's decentralized capability grounding maps to the AMOS control plane's authority gate — agents self-organize based on capability rather than central routing. ArcticSwarm's gated isolation principle directly supports the AMOS competing-hypothesis invariant (preserve competing hypotheses until discriminating evidence exists). Leibniz's bidirectional reasoning mirrors the MURK 19×19 interaction matrix's forward/reverse reasoning paths. Codebook Agent's topology compression validates the AMOS cognitive matrix's 19×19 coordinate routing approach.

### 11.4 Photonic Neural Networks

| Paper | Source | Key Finding | AMOS Binding |
|-------|--------|-------------|--------------|
| Inverse-designed nanophotonic NN accelerator | Nature Communications 2026 | 400M params/mm²; subwavelength voxel training; 89% MNIST / 90% MedNIST on 20×20μm² chip | `05_COGNITIVE_ORGANISM/PHOTONIC_AND_OPTOELECTRONIC_NEURAL_INTERFACE` |
| Photonic Mixture-of-Experts (PMoE) | Nature Communications 2026 | Width-scaling via parallel photonic cores; 97.1% multi-domain accuracy; 67% parameter overhead reduction; 0.067mm² core footprint | `05_COGNITIVE_ORGANISM` |
| On-chip backpropagation training | Nature 2026 | End-to-end on-chip gradient descent; >90% accuracy matching digital models; scalable despite fabrication variations | `05_COGNITIVE_ORGANISM` |
| Photonic tensor processor (PTP) | Nature Communications 2026 | All-optical crossbar; 98.1% MNIST / 72.0% CIFAR-10; rack-mounted with PyTorch integration; microcomb multi-wavelength carriers | `05_COGNITIVE_ORGANISM` |
| NARCA — Non-volatile all-optical ResNet accelerator | Light: Sci. Appl. 2026 | PCM-based residual convolution; 9.8μW weight update energy; matches ResNet deep feature extraction | `05_COGNITIVE_ORGANISM` |

**AMOS Integration:** The PMoE architecture's width-scaling approach directly maps to the AMOS cognitive matrix's parallel cell coordination — expanding width (parallel experts) rather than depth (serial layers) mirrors the matrix's 19×19 parallel coordinate routing. On-chip backpropagation enables the AMOS cognition engine to perform local learning without external compute, supporting the self-contained organism architecture. The 400M params/mm² density establishes the substrate feasibility for the `PHOTONIC_AND_OPTOELECTRONIC_NEURAL_INTERFACE` specification.

### 11.5 Updated Falsifiers

- `F7-2026-09-05`: Cross-subject BCI pretraining claims require validation on datasets beyond speech motor cortex (current evidence limited to motor/speech domains).
- `F8-2026-09-05`: RL-controlled QEC scalability claims require demonstration beyond distance-7 surface codes; the "never-stop-computing" paradigm assumes drift models that may not hold for all noise types.
- `F9-2026-09-05`: Photonic NN backpropagation training results are demonstrated on small-scale tasks (MNIST, MedNIST); scalability to transformer-class models remains `UNKNOWN/GAP`.

### 11.6 Brain Organoid Intelligence (OI)

| Paper | Source | Key Finding | AMOS Binding |
|-------|--------|-------------|--------------|
| Monsó et al. 2026 — Bio-adaptive Processing Unit (BPU) | Sci Rep 2026 | Two-reservoir microtunnel Brain-on-Chip; hiPSC-derived cortical neurons; 1200μm axonal extension; directed propagation A→B (85-90%); 0.75 m/s median velocity; MEA-interfaced biocomputing platform | `05_COGNITIVE_ORGANISM/NEURAL_ORGANOID_WORLD_MODEL_ARCHITECTURE` |
| Cortical Labs CL-1 — "Neurons as a Service" | WIRED 2026 | Toaster-sized device; 1M neurons × 6 months survival; trained on Pong and Doom; "Nvidia of neural computing"; self-repair, adaptability, energy efficiency | `05_COGNITIVE_ORGANISM` |
| Organoid cartpole balancing — Reinforcement learning | Singularity Hub 2026 | Brain organoids rewired networks to balance pole; electrical feedback as reinforcement; predictable learning in 3D organoid structures | `05_COGNITIVE_ORGANISM` |
| OI-enhanced microcircuit integration | Aticl 2025.000231 | Hybrid computational paradigm; organoids on high-density MEAs; SORN-1 dataset; OI-augmented DRL agent; revolutionary leap in learning rate and novel stimulus adaptation | `05_COGNITIVE_ORGANISM/ORGANISM_OS_SYNTHESIS` |
| NIH $87M organoid standardization center | 2025-2026 | NIH ended animal-only testing grants; $87M investment in standardized organoid modeling; artificial blood vessel research for >5mm organoids | `05_COGNITIVE_ORGANISM` |

**AMOS Integration:** The BPU's two-reservoir microtunnel architecture directly maps to the `NEURAL_ORGANOID_WORLD_MODEL_ARCHITECTURE` — directed axonal propagation enables the organoid's world model to have structured information flow rather than random connectivity. Cortical Labs' CL-1 "neurons as a service" model establishes the substrate for the `ORGANISM_OS_SYNTHESIS` — a living cognitive substrate with self-repair and adaptation that silicon cannot match. The organoid cartpole result validates that biological neural networks can perform reinforcement learning, supporting the AMOS cognitive organism's learning loop. The 5mm vascularization barrier is a hard constraint on current organoid scale — AMOS must account for this in its biological state vector (Bio component).

### 11.7 KV Cache Quantization for LLM Inference

| Paper | Source | Key Finding | AMOS Binding |
|-------|--------|-------------|--------------|
| SemKV — Semantic mixed-precision KV quantization | arXiv:2608.28911 | Quality cliff at 2.0-2.322 bits; 6.0× storage reduction with no detectable quality loss; TurboQuant-MSE raises to 7.9×; cliff-measure-then-interpolate recipe | `11_KNOWLEDGE/LLM_WIKI` |
| InnerQ — Hardware-aware KV quantization | arXiv:2602.23200 | Inner-dimension grouping; 22% speedup over prior work; 88% over FP16; hybrid symmetric/asymmetric; high-precision windows for recent + sink tokens | `11_KNOWLEDGE/LLM_WIKI` |
| NOVA-KV — Attention-preserving vector quantization | arXiv:2608.04074 | Transform coding with attention-aware distortion; non-orthogonal key transform; equal-volume partition codebooks; effective on GPT-OSS-20B MoE | `11_KNOWLEDGE/LLM_WIKI` |
| KVarN — Variance-normalized KV quantization | arXiv:2606.03458 | Hadamard rotation + dual-scaling variance normalization; fixes token-scale outliers; SOTA on MATH500, AIME24, HumanEval at 2-bit; vLLM implementation | `11_KNOWLEDGE/LLM_WIKI` |
| MixKVQ — Query-aware mixed-precision KV | ACL 2026 | Query-aware critical channel identification; per-token value quantization; comparable to full-precision at reduced memory | `11_KNOWLEDGE/LLM_WIKI` |

**AMOS Integration:** The "quality cliff" phenomenon (SemKV) is a critical finding for the AMOS cognition engine — it demonstrates that KV cache quantization has a non-graceful degradation threshold, meaning the system must operate above the cliff or fail closed. This maps to the AMOS adaptive stability balancer's collapse probability invariant. KVarN's error accumulation finding is directly relevant to the AMOS reasoning loop — long-horizon reasoning tasks accumulate quantization errors across timesteps, requiring the AMOS validation pipeline to account for this. The attention-preserving transform approach (NOVA-KV) aligns with the AMOS cognitive matrix's attention-based routing mechanism.

### 11.8 Updated Falsifiers (Additional)

- `F10-2026-09-05`: Brain organoid intelligence claims require demonstration of computation (not just signal propagation); current BPU results show routing primitives but not task training, learning, or long-term plasticity.
- `F11-2026-09-05`: Organoid vascularization beyond 5mm remains unsolved; scaling claims beyond current organoid sizes are `UNKNOWN/GAP`.
- `F12-2026-09-05`: KV cache quality cliff thresholds are model-specific (demonstrated on Llama-3.1-8B and Mistral-7B); generalization to other architectures requires per-deployment measurement.
