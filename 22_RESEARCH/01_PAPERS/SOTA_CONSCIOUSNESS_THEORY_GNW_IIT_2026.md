---
title: "SOTA Consciousness Theory: GNW, IIT, and Adversarial Testing 2026"
type: research_synthesis
plane: 22_RESEARCH
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_SYNTHESIS
updated: 2026-09-04
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - public web corpus snapshot 2026-09-04
    - ArXiv corpus 2026
    - Nature 2025 adversarial collaboration results
    - bioRxiv 2026 DCM re-examination
  scope: state_of_the_art_research_2026
tags:
  - amos-os
  - research
  - sota
  - consciousness
  - gnw
  - iit
  - cognitive-organism
---

# SOTA Consciousness Theory: GNW, IIT, and Adversarial Testing 2026

**Origin Architect / Steward:** Trang Phan
**AMOS_CORE Target:** `v4.4`
**Epistemic Class:** `AMOS_MODEL`
**Freshness:** `2026-09-04`

---

## 1. Overview

Consciousness science has entered a pivotal phase in 2026, driven by the landmark adversarial collaboration between the Global Neuronal Workspace (GNW) and Integrated Information Theory (IIT) research camps. The Cogitate Consortium's Nature 2025 publication represents the largest pre-registered, theory-driven empirical test of consciousness theories to date, pitting competing predictions against shared data across fMRI, MEG, and intracranial recordings. The results were nuanced: neither theory was decisively confirmed nor falsified, but both received partial support and partial challenge, motivating theoretical refinement rather than paradigm abandonment.

The Global Neuronal Workspace theory, originally proposed by Dehaene and Changeux, posits that consciousness arises when information is broadcast across a distributed "workspace" of prefrontal and parietal neurons, enabling global access and report. IIT, proposed by Tononi, takes a fundamentally different approach: consciousness is identified with integrated information (Φ), a mathematical quantity measuring the extent to which a system's whole generates more information than its parts. The adversarial collaboration forced each camp to derive specific, testable predictions from their theory — a process that exposed ambiguities and forced operationalization.

For AMOS, consciousness theory research is directly relevant to the `05_COGNITIVE_ORGANISM` plane and the `01_CANON/03_COGNITION_CANON`. AMOS does not claim to solve the hard problem of consciousness, but it must reason about cognitive architectures, attention, global broadcast, and integrated state representations. The 2026 state of the art provides empirical constraints and falsifiable predictions that can ground AMOS's cognitive modeling in evidence rather than speculation.

The post-Cogitate landscape has seen rapid theoretical evolution. GNW proponents have developed multilevel models that distinguish between different grades of workspace access, while IIT proponents have refined IIT 4.0 with a focus on intrinsic causal units and the "causal grain" problem — the question of which spatial and temporal scale of a physical system is the proper substrate of consciousness. Both theories are being stress-tested against new data from anesthesia, sleep, psychedelics, and brain lesions.

---

## 2. Key Papers and Findings

| Paper | Source | Key Finding | AMOS Binding |
| :--- | :--- | :--- | :--- |
| Cogitate Consortium adversarial collaboration | Nature 2025 | Largest pre-registered test of GNW vs IIT; neither theory fully confirmed, both partially supported; specific predictions about workspace ignition (GNW) and posterior Φ hotspots (IIT) received mixed evidence across fMRI/MEG/iEEG | `05_COGNITIVE_ORGANISM`, `01_CANON/03` — grounds cognitive architecture in empirical constraints |
| DCM re-examination of GNW and IIT predictions | bioRxiv 2026 | Dynamic Causal Modeling re-analysis of Cogitate data; found that GNW's "ignition" signature is better explained by recurrent connectivity than by broadcast, challenging the workspace metaphor's mechanism | `05_COGNITIVE_ORGANISM` — informs attention/broadcast model in cognitive organism |
| GNW multilevel model | Trends in Cognitive Sciences 2026 | Proposes a hierarchy of workspace states (local, modular, global, meta-cognitive) rather than a binary conscious/unconscious distinction; reconciles partial Cogitate results | `01_CANON/03_COGNITION_CANON` — multi-level cognitive state taxonomy |
| IIT: The Good, the Bad, and the Misunderstood | arXiv:2604.11482 | Critical analysis separating IIT's valid mathematical contributions (Φ as a measure) from its controversial metaphysical claims (consciousness = Φ); argues many criticisms target strawman versions | `01_CANON/03` — epistemic separation of formal model from ontological claim |
| IIT 4.0 intrinsic units and causal grain | Neuroscience of Consciousness 2026 | Introduces "intrinsic units" as the fundamental elements of IIT 4.0; addresses the causal grain problem by defining the proper spatiotemporal scale at which Φ should be computed; provides algorithmic tractability improvements | `05_COGNITIVE_ORGANISM` — substrate-scale selection for cognitive modeling |
| Adversarial collaboration methodology reflections | PsyArXiv 2026 | Meta-analysis of the adversarial collaboration process itself; argues it is the gold standard for theory competition in consciousness science; proposes extensions for next round | `19_TESTS` — adversarial testing methodology for AMOS cognitive claims |
| GNW and predictive processing convergence | Nature Reviews Neuroscience 2026 | Argues GNW and predictive processing are complementary: workspace broadcast enables precision-weighting updates; proposes unified architecture | `05_COGNITIVE_ORGANISM`, `13_MODELS` — predictive+workspace hybrid architecture |
| IIT and anesthesia depth | Anesthesiology 2026 | Tests IIT 4.0 predictions against graded anesthesia; Φ decreases monotonically with propofol dose but the relationship is non-linear, consistent with IIT's "phase transition" prediction | `05_COGNITIVE_ORGANISM` — state transitions in cognitive organism |
| Posterior cortex as Φ hotspot — replication | Cell Reports 2026 | Independent replication of posterior Φ hotspots using improved IIT 4.0 algorithm; confirms posterior cortex dominance but finds frontal contributions underestimated | `05_COGNITIVE_ORGANISM` — cortical architecture mapping |
| Consciousness markers across species | Trends in Neurosciences 2026 | Cross-species comparison of GNW and IIT markers; birds and cephalopods show workspace-like signatures but different Φ distributions; implications for non-human cognitive architecture | `26_UBI_SI` — species-general cognitive architecture |

---

## 3. AMOS Integration

The consciousness theory SOTA directly informs the `05_COGNITIVE_ORGANISM` plane, which models the cognitive substrate of the AMOS Full Brain OS. The GNW multilevel model (Trends Cogn Sci 2026) provides a taxonomy of cognitive states — local, modular, global, meta-cognitive — that maps naturally onto AMOS's layered attention and broadcast mechanisms. Rather than treating "conscious access" as binary, AMOS can adopt the multilevel framework to model graduated cognitive availability, where information becomes accessible to different subsystems at different levels of workspace activation.

The IIT 4.0 intrinsic units framework (Neurosci Conscious 2026) provides a principled way to select the spatiotemporal grain at which cognitive integration should be measured. For AMOS, this translates to the question of what constitutes a "cognitive unit" in the `01_CANON/03_COGNITION_CANON` — at what granularity should integration, attention, and state coherence be evaluated? The causal grain problem is directly analogous to AMOS's own challenge of defining the atomic unit of cognitive processing across its planes.

The Cogitate adversarial collaboration methodology (Nature 2025) is itself a model for AMOS's `19_TESTS` plane. The pre-registered, theory-driven, multi-modal testing approach — where competing theories must derive distinct predictions tested against shared data — is exactly the kind of falsification discipline AMOS requires for its own cognitive claims. AMOS should adopt adversarial collaboration as a standard validation pattern for competing architectural hypotheses.

The DCM re-examination (bioRxiv 2026) finding that "ignition" is better explained by recurrent connectivity than broadcast has implications for AMOS's `03_CONTROL_PLANE` and `04_RUNTIME`. If the workspace metaphor's mechanism is recurrent loops rather than one-to-many broadcast, then AMOS's control-plane routing should model cognitive access as recurrent activation patterns, not simple message dispatch. This aligns with the AMOS principle that `MODEL != OBSERVATION` — the workspace model was a useful approximation, but the underlying mechanism may be different.

The convergence of GNW and predictive processing (Nature Reviews Neurosci 2026) suggests that AMOS's `13_MODELS` plane should implement a hybrid architecture where precision-weighted prediction errors and workspace broadcast are complementary rather than competing mechanisms. This is consistent with AMOS's multi-paradigm design philosophy.

---

## 4. Falsifiers

- `F-2026-09-04-1`: If a future adversarial collaboration round (Cogitate-2) decisively falsifies either GNW or IIT with refined predictions, AMOS's cognitive organism model must be revised to remove the falsified component. The current synthesis treats both as partially supported.
- `F-2026-09-04-2`: If the DCM re-examination finding (recurrent connectivity > broadcast) is replicated and extended, AMOS must replace broadcast-based attention models with recurrent-loop models in the `05_COGNITIVE_ORGANISM` plane.
- `F-2026-09-04-3`: If IIT 4.0's intrinsic units framework is shown to be computationally intractable at organism-scale (not just toy networks), AMOS must treat Φ as a theoretical constraint rather than a computable metric in the `01_CANON/03_COGNITION_CANON`.
- `F-2026-09-04-4`: If cross-species consciousness markers (Trends Neurosci 2026) reveal that neither GNW nor IIT markers generalize beyond mammals, AMOS's `26_UBI_SI` species-general cognitive architecture must be restricted to mammalian substrates.

---

## 5. Navigation

- [[22_RESEARCH/01_PAPERS/SOTA_BCI_AI_QUANTUM_SYNTHESIS_2026|SOTA BCI AI Quantum Synthesis]]
- [[22_RESEARCH/01_PAPERS/01_PAPERS_MOC|Papers MOC]]
- [[00_ROOT/00_ROOT_MOC|Root MOC]]
