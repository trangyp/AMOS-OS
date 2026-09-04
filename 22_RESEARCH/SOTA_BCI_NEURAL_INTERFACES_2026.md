---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Sota Bci Neural Interfaces 2026
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

# SOTA Brain-Computer Interfaces & Neural Interfaces 2026

> [!ABSTRACT] Research Synthesis
> Comprehensive State-of-the-Art review of Brain-Computer Interfaces (BCI) in 2026: invasive, endovascular, and non-invasive approaches; neural foundation models; bidirectional interfaces; standardization; market dynamics; and AMOS integration architecture. Extends [[22_RESEARCH/SOTA_BCI_FOUNDATION_MODELS_NEURAL_INTERFACES_2026|SOTA_BCI_FOUNDATION_MODELS_NEURAL_INTERFACES_2026]] with a full 2026 platform-based landscape update.

---

## 1. Executive Summary

The 2026 BCI landscape has crossed a **regulatory and commercial threshold**. Three structural shifts define the moment:

1. **The world's first commercially approved invasive BCI exists.** China's NMPA approved **Neuracle NEO** for commercial sale in **March 2026** — the first time any invasive BCI has moved from clinical research to sellable medical device. The US FDA has not yet approved any BCI for commercial use, but Synchron is targeting the first PMA filing after a 2026 pivotal trial, and multiple IDE trials are expanding.

2. **Patient scale is growing across invasive players.** Neuralink has **21+ enrolled patients** across the US and Canada in its PRIME study; Blackrock Neurotech maintains a **19+ year, 40+ patient** Utah Array track record; ONWARD Medical has **seven** ARC-BCI implants in spinal cord injury patients. Human implantation shifted from "a handful of pioneers" to "multiple programs recruiting at scale."

3. **AI-native decoding became the dominant technical trend.** Transformer and state-space foundation models trained on neural corpora (Stable EEG foundation models like DeeperBrain/ST-EEGFormer, Synchron's **Chiral** cognitive AI brain foundation model) are moving BCI decoding from per-user supervised retraining toward **cross-person self-supervised generalization**.

**Market context:** The BCI market was valued at **~$2.8B (2025)** and **~$3.2B (2026)**, projected to reach **$6–12B by 2030**, a 15–18% CAGR (sources: Grand View Research, MarketsandMarkets, Global Market Insights). Total disclosed BCI funding tracked at $7.5B+ across 16 companies / 34 rounds.

**AMOS Boundary (RSCF discipline):** Per [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] and AGENTS.md invariants — `LATEST != AUTHORITATIVE`, `DOCUMENTED != IMPLEMENTED`, `MODEL != DEPLOYED_RUNTIME`, `CAPABILITY != AUTHORITY`. Company announcements are `OBSERVATION` of intent/progress; regulatory approvals are verified only against primary agency records; AMOS integration pathways herein are `PROPOSAL` class until tied to committed implementation evidence.

---

## 2. Invasive BCI

Invasive (intracortical / subdural) BCIs achieve the highest signal fidelity by placing electrodes in or on brain tissue, at the cost of surgical risk and long-term biocompatibility. In 2026 the invasive frontier is defined by **electrode-count scaling** and **path to approval**.

### 2.1 Neuralink

| Attribute | Detail |
| :--- | :--- |
| **Implant** | N1 — 1,024 electrodes across 64 flexible threads (~one-tenth hair width) |
| **Study** | PRIME (Precise Robotically Implanted Brain-Computer Interface) |
| **Patients** | 21+ enrolled (US & Canada), early 2026 |
| **Demo milestone** | Noland Arbaugh (first patient, Jan 2024) achieved mind-controlled cursor |
| **Funding** | Series E **$650M** (June 2025; ARK Invest, Founders Fund, Sequoia, Thrive), ~**$9B pre-money** valuation; >$1.2B total raised |
| **Next-gen** | ~**3,000-electrode** device in development; high-volume production expansion (South SF + Austin, 144k sq ft) |
| **Blindsight** | Visual prosthesis; FDA **Breakthrough Device Designation** (Sept 2024), trials expected within 6–12 months |
| **Other** | Hearing/auditory program announced; nearly fully automated surgical threading (Rev 10 / Optimus robots) |

**Technical notes.**
- Thread retraction occurred in early patients (Arbaugh), since mitigated via thread-count refinement and surgical depth technique — evidence that long-term implant stability remains the dominant failure mode.
- Neuralink's stated goal: **two orders of magnitude more channels than clinically approved devices** (~102,400 electrodes eventual target).

### 2.2 Blackrock Neurotech

| Attribute | Detail |
| :--- | :--- |
| **Platform** | Utah Array (rigid silicon microelectrode array) |
| **Track record** | **19+ years** of human use, **40+ patients** |
| **Next-gen** | **Neuralace** — flexible lace-structured array at **10,000+ channels** |
| **Funding** | **$200M** from Tether (April 2024) for commercialization; DARPA partnership (Jan 2026) for defense applications |
| **Programs** | MoveAgain (motor restoration); BrainGate academic lineage |

**Technical notes.**
- The Utah Array, originally used in the BrainGate consortium, is the most-studied invasive array ever deployed, with a multi-decade safety signal.
- **Neuralace** shifts from rigid silicon to a flexible, lace-structured substrate to improve long-term biocompatibility and scale channel count by ~100× (96 → 10,000+). Not yet in human trials as of 2026.
- Regulatory: research/510(k)-cleared (NeuroPort 96-electrode); no commercial BCI approval yet.

### 2.3 Paradromics

| Attribute | Detail |
| :--- | :--- |
| **Device** | **Connexus Direct Data Interface** (Connexus DDI) |
| **Electrodes** | **1,684** (up to 4 cortical modules × 421 microwire electrodes, ~1.55mm, <40µm dia, Pt-Ir tips) |
| **Data rate** | **200+ bits/sec** information transfer in preclinical models; 100 Mbit/s wireless infrared link; ~56ms latency |
| **Regulatory** | **First FDA IDE for speech restoration** with a fully implantable BCI (Nov 2025) |
| **Clinical** | First human implant **June 17, 2026** at University of Michigan (Dr. Matthew Willsey); sites at UC Davis, MGH |
| **Application** | Speech restoration + computer control for severe motor impairment |

**Technical notes.**
- Connexus is a fully implantable high-data-rate platform: subclavicular internal transceiver, continuous inductive power, on-chip low-noise amplifiers/digitizers with edge processing.
- First fully implantable BCI purpose-built and FDA-cleared-for-trial for **speech restoration**, a differentiated indication versus motor-control focus of Neuralink/Synchron.

### 2.4 Precision Neuroscience

| Attribute | Detail |
| :--- | :--- |
| **Device** | **Layer 7** cortical interface |
| **Electrodes** | **1,024** electrodes in an ultra-thin film (~1/5th hair thickness) that conforms to brain surface |
| **Regulatory** | **FDA 510(k) cleared** (April 2025) for temporary recording/monitoring/stimulation |
| **Clinical** | 30-day extended brain monitoring achieved (2025); pre-IDE long-term studies |
| **Partnership** | **Medtronic** (Jan 12, 2026) — integrate Layer 7 with Medtronic StealthStation surgical navigation; co-development for real-time structural + functional intraoperative info |
| **Approach** | Minimally invasive — placed via burr hole or open procedures |

**Technical notes.**
- Layer 7 is a **minimally invasive cortical (non-penetrating) film array** — lower risk than intracortical threads, traded against slightly lower single-neuron fidelity.
- The **Medtronic partnership** is strategically significant: it embeds Precision's technology into the surgical navigation platform already used ubiquitously by neurosurgeons, accelerating clinical adoption and giving Medtronic access to functional neural data for product development.

### 2.5 China: Neuracle NEO

| Attribute | Detail |
| :--- | :--- |
| **Device** | **NEO** — semi-invasive **extradural** BCI |
| **Electrodes** | ~8 electrodes, placed over the dura (no cortical penetration) |
| **Regulatory** | **NMPA commercial approval — March 2026**, world's first commercially approved invasive BCI |
| **Clinical history** | 32 clinical cases prior to approval |
| **Significance** | China's regulatory-first-mover position in BCI commercialization |

**Technical notes.**
- Neuracle NEO's approval is a **landmark**: it is the first time any invasive BCI has received commercial (sellable medical device) approval anywhere. Its **extradural** placement balances fidelity against reduced surgical risk.
- Geopolitical framing: China has designated BCI a **core strategic industry** in its 15th Five-Year Plan (2026+); NeuCyber (mesh electrode, 7 implanted) and Beinao-1 programs are expanding in parallel. The US FDA has not yet approved a BCI for commercial sale, creating a **regulatory leadership gap** with strategic implications.

---

## 3. Endovascular BCI

### 3.1 Synchron — Stentrode

| Attribute | Detail |
| :--- | :--- |
| **Device** | **Stentrode** — stent-based electrode array delivered via catheter through jugular vein; **no craniotomy** |
| **Electrodes** | **16** on a self-expanding stent, placed in a cerebral vein |
| **Study** | **COMMAND** (NCT05035823) — first IDE trial of a permanently implanted BCI in the US; Breakthrough Device Designation (Aug 2020) |
| **COMMAND result** | All **6 patients** met primary safety endpoint (12 months, no device-related SAEs) — Sept 30, 2024 |
| **Expanded** | Dec 2025 FDA approval expansion for ALS patients |
| **2026 pivot** | **Pivotal trial** toward **first PMA filing** for an implantable BCI; potential approval 2028–2029 |
| **Funding** | **$200M Series D** (Nov 6, 2025; Double Point, ARCH, Khosla, Bezos Expeditions, Qatar Investment Authority, Protocol Labs, IQT) |
| **Apple integration** | First BCI maker with native **Apple BCI HID** integration (May 2025) — Stentrode registers with iOS as its own input device class, driving iPhone/iPad/Vision Pro without per-app hacks; demonstrated by ALS patient Mark Jackson (Aug 2025) |
| **AI** | **Chiral** — "world's first cognitive AI brain foundation model" (GTC 2025, with NVIDIA Holoscan/Cosmos); self-supervised learning on 20 patient-years of neural data |
| **Next-gen** | Transcatheter **"high-channel whole-brain interface"** in development (San Diego hub) |

**Technical notes (endovascular value proposition).**
- The endovascular route **eliminates craniotomy** and reduces infection risk, using a delivery paradigm (catheterization) familiar to interventional neuroradiology — expanding the addressable patient population versus intracortical surgery and de-risking the FDA pathway (Class III vascular device classification rather than novel neurosurgical category).
- Trade-off: **16 electrodes yield lower spatial resolution** than intracortical arrays (~1.2 bits/sec, 92–94% decode accuracy in reported figures). This is the "fidelity gap" the next-gen high-channel implant targets.
- **Chiral** embodies the endovascular **data-scale advantage**: because Stentrode deployment is as routine as a stent procedure, Synchron argues it can reach population-level neural data collection needed to train a brain foundation model — a moat competitors with complex surgery cannot match.

---

## 4. Non-Invasive BCI

Consumer-grade non-invasive BCI (primarily EEG) improved resolution through denser dry-electrode headsets, better artifact rejection, and smartphone-native integration.

| Platform | Approach | Notes (2025–2026) |
| :--- | :--- | :--- |
| **OpenBCI** | Open-source EEG/ECoG bio-amplification | Cyton/Ganglion boards; de-facto research standard; now includes 3D-printable dry electrodes |
| **Emotiv** | Consumer EEG headsets (EPOC+/Insight) | Cognitive workload, emotion, facial-expression decoding; software SDK for app developers |
| **Muse** | Consumer EEG meditation/focus | 4-ch dry electrode; strong consumer adoption for wellness |
| **NextMind (Snap)** | Visual-parietal non-invasive BCI | Steady-state visual evoked potential (SSVEP) attention decoding; headband; commercial dev kit (acquired by Snap, 2022) |
| **Neurable** | EEG-integrated headphones | Smart brain-computer headphones with embedded EEG (2025–26); **consumer BCI exceeding clinical EEG resolution** claim |

**Technical notes.**
- Non-invasive consumer BCI is entering a phase where **integrated wearables** (headphones/bands) embed EEG. Signal fidelity is lower than clinical EEG and far below invasive, giving it a lower AMOS confidence ceiling (INV-BCI-05).
- Emerging non-invasive alternatives beyond EEG: **ultrasound-based** approaches (Merge Labs — Sam Altman, Nudge, Gestala) represent a growing category for modulating/reading neural tissue without scalp electrodes or surgery.

---

## 5. Foundation Models for Neural Decoding

This is the intellectual epicenter of 2026 BCI. Full technical detail is in [[22_RESEARCH/SOTA_BCI_FOUNDATION_MODELS_NEURAL_INTERFACES_2026|SOTA_BCI_FOUNDATION_MODELS_NEURAL_INTERFACES_2026]]; summary here.

### 5.1 LLM-Integrated Neural Decoding

- **Speech neuroprosthetics** (UC Berkeley/UCSF RNN-T, Nature Neuroscience, Mar 2025): **<5% word error rate**, 80-ms decoding increments — near-real-time neural-to-speech.
- **UCSF Chang Lab**: 78-words/minute text decoding + personalized speech audio.
- **Text-to-Speech / multimodal communication**: Dreamécran-style decoding expanded beyond sensorimotor cortex (prefrontal, temporal, parietal) by Maastricht, broadening the eligible patient population.
- **BrainGate2** (Nature Neuroscience, Mar 2026): motor-cortex-to-finger-movement typing approaching able-bodied speed with rapid calibration.

### 5.2 Cross-Person Generalization

- **ICLR 2026 EEG foundation benchmark** (ST-EEGFormer vs DeeperBrain vs EEGNet vs CSP+SVM): foundation models excel at **zero-shot cross-subject transfer**; smaller gains within-subject where supervised classical decoders remain competitive.
- **DeeperBrain**: hierarchical spatio-temporal SSM with learnable 3D electrode coordinates; MARS (masked auto-encoding) pretraining; $O(T)$ complexity; infinite-context memory of slow drifts.
- Implication for AMOS: cross-person foundation decoders can bootstrap new users with minimal calibration, but must not be conflated with identity transfer (INV-BCI-04).

### 5.3 Self-Supervised Learning on Neural Data

- **Synchron Chiral**: generative pretraining directly on neural activity (NVIDIA Holoscan edge decoding → Cosmos context awareness → Chiral foundation model); moving from supervised to self-supervised intent-to-action.
- The generative-pretraining-of-brain-data paradigm ("a GPT-like moment for the brain") is the defining technical bet of the 2026 cohort, and central to the AMOS cognitive-input-substrate thesis.

---

## 6. Bidirectional BCI

Bidirectional systems record neural signals **and** deliver stimulation, enabling closed-loop sensory feedback and full duplex brain-computer communication.

### 6.1 Visual Prostheses

| Program | Approach | Status (2026) |
| :--- | :--- | :--- |
| **Neuralink Blindsight** | Cortical visual prosthesis; N1 electrodes deliver phosphene-generating stimulation to primary visual cortex, bypassing eyes/optic nerve | FDA **Breakthrough Device Designation**; image streamed from camera, wireless to implant; target > natural-vision resolution long-term |
| **Cortica/Elektra (Intelligent Implants)** | ~30-ch fully implantable visual cortical array | Human-feasibility phase; 30-min low-resolution room/task awareness demonstrated |

**Technical notes.**
- Visual prostheses stimulate the **visual cortex** directly, producing phosphene percepts. Resolution scales with electrode count — motivating Neuralink's high-density approach.
- Safety concerns: long-term seizure risk, tissue trauma from cortical stimulation; experts caution efficacy/vision gains require multi-year validation per [[22_RESEARCH/01_PAPERS/SOTA_BCI_AND_NEUROTECHNOLOGY_SYNTHESIS_2026|SOTA_BCI_AND_NEUROTECHNOLOGY_SYNTHESIS_2026]].

### 6.2 Sensory Feedback / Motor Restoration Stimulation

- **ONWARD Medical ARC-BCI** (DigitalBridge): pairs a **motor-cortex BCI implant (WIMAGINE, CEA-Clinatec)** with an **implantable spinal cord stimulator (ARC-IM)**. AI decodes movement intent → wirelessly commands spinal stimulation → thought-driven limb movement below the injury. **Seven human implants** (Jan 2026), 10 FDA Breakthrough Device Designations, FDA Total Product Life Cycle Advisory (TAP) Program participant. Derives from the Grégoire Courtine/Jocelyne Bloch *Nature* 2023 work.
- **BCI-FES**: stroke rehabilitation combining motor decoding with functional electrical stimulation.
- **Sensory feedback direction** (touch/proprioception restoration): research-stage closed-loop stimulation returning sensation from prostheses.

### 6.3 Bidirectional Brain-Computer Communication

- The convergence of recording + stimulation into a single platform enables **input and output over one neural interface** — the foundation for two-way human-AI dialogue.
- **Apple BCI HID** is architecturally significant: it establishes bidirectional, OS-level recognition where neural input is treated natively (a thought becomes a system input like a keystroke), enabling true bidirectional device control.
- **Implication for AMOS**: bidirectional BCI is the hardware substrate for the **human-in-the-loop cognitive architecture** (Section 9.3).

---

## 7. Standardization & Regulation

### 7.1 IEEE P2731

- **P2731 — Standard for a Unified Terminology for Brain-Computer Interfaces** (IEEE EMBS, PAR approved 2018, active): establishes a unified BCI glossary for users, neurologists, and engineers; a common functional model of BCIs; and data-sharing/file-format fundamentals.
- Companion: **IEEE P2794 — Reporting Standard for in vivo Neural Interface Research (RSNIR)** — framework for standardizing reporting across publications, grants, and regulatory submissions.
- IEEE Brain Initiative vehicle: drives interoperability across the growing BCI ecosystem — directly relevant to AMOS multi-device sensor fusion (Section 9.1).

### 7.2 ISO / IEC

- **ISO/IEC JTC 1/SC 43** — Brain-computer interfaces (administratively supported by IEC): standardization of BCI for IT-enablement of brain-computer communication/interaction.
- **ISO/IEC TS 27571:2026** (Edition 1, published 2026-04): *Data format for noninvasive brain information collection* — defines basic data elements, metadata, extensible modular data structure, and naming conventions for EEG/MEG/fNIRS/fMRI.
- **ISO/TC 150** (implants for surgery) and **ISO/TC 299** (robotics — exoskeletons/wearable robotics, incl. neural-interface aspects; related to personal care robots) provide adjacent standards for implant safety and robot integration.

### 7.3 FDA Regulatory Pathways

| Pathway | Entity / Status |
| :--- | :--- |
| **Breakthrough Device Designation** | Neuralink Blindsight (2024), Synchron Stentrode (2020), ONWARD ARC-BCI (2024, +9 others), Cortec (2026) |
| **IDE (Investigational Device Exemption)** | Synchron COMMAND (first permanent BCI IDE); Paradromics Connect-One (first speech-restoration BCI IDE, Nov 2025); Neuralink PRIME |
| **510(k)** | Precision Layer 7 (cleared April 2025); ONWARD ARC-EX commercial |
| **PMA** | None yet for invasive BCI; Synchron targets **first PMA filing** post-2026 pivotal; potential approval 2028–2029 |
| **TAP (Total Product Life Cycle Advisory)** | ONWARD Medical among first neurotechnology invitees |

**Key regulatory insight:** The US has **no commercially approved BCI** as of 2026, while China's NMPA approved Neuracle NEO in March 2026. The convergence is on **data-quality and long-term safety evidence** — FDA is requiring efficacy-at-scale (pivotal) data that feasibility studies do not provide, setting the commercial gate at ~2028–2030.

---

## 8. Market Data

| Metric | Value |
| :--- | :--- |
| **Market size 2025** | ~$2.8B |
| **Market size 2026** | **~$3.2B** |
| **Projected 2030** | **$6–12B** (Grand View, MarketsandMarkets, Global Market Insights); bciintel narrower $5.5–7B |
| **CAGR 2025–2030** | 15–18% |
| **Medical implantable segment CAGR** | 20–25% (fastest-growing) |
| **Disclosed funding** | $7.5B+ across 16 companies / 34 rounds |
| **2024→2025 funding growth** | $406M → $1.0B (total BCI funding more than doubled) |
| **Longer-term** | $14–18B (2035, bciintel); >$50B potential TAM by 2040 |

**Drivers:** first commercial BCI approvals (China; US pending ~2028–2030), expanding DBS indications, non-invasive consumer neurotechnology into mainstream computing, defense procurement (DARPA) beyond research, aging population, VC investment.

---

## 9. AMOS Integration Architecture

Maps the 2026 BCI landscape onto the AMOS_OS cognitive architecture (per [[21_DOMAINS/14_C04_BIO_NEURO/C04_NEURAL_DECODING_AND_BCI_ARCHITECTURE|C04_NEURAL_DECODING_AND_BCI_ARCHITECTURE]] and [[15_INTERFACES/BCI_EXPRESSION_GATEWAY_ADAPTER|BCI_EXPRESSION_GATEWAY_ADAPTER]]).

### 9.1 Sensor Fusion Layer (Multi-Device Integration)

```
INVASIVE (N1 / Utah / Connexus / Layer 7)
ENDOVASCULAR (Stentrode)
NON-INVASIVE (EEG, fNIRS, ultrasound)
        │  heterogeneous sampling, latency, fidelity
        ▼
┌──────────────────────────────────────────┐
│ AMOS SENSOR FUSION LAYER                 │
│  · IEEE P2731-compatible unified vocab    │
│  · ISO/IEC TS 27571-compatible data fmt   │
│  · time-alignment + confidence weighting  │
└─────────────────┬────────────────────────┘
                  ▼
        EPISTEMIC CLASSIFICATION (OBSERVATION)
```

- Different device classes carry different confidence ceilings (INV-BCI-05). Fusion must preserve per-source `confidence_ceiling` and not collapse multi-modal signals into a single higher-confidence claim.

### 9.2 Neural Foundation Models as Cognitive Input Substrate

- Cross-person decoders (DeeperBrain, ST-EEGFormer, Chiral) provide a **parametric prior** for new users, reducing calibration to near-zero.
- In AMOS terms: foundation-model outputs are `DERIVED` (INV-BCI-02); decoded intentions are `PROPOSAL` requiring commit-time authority (INV-BCI-03).
- Decoder confidence must be propagated as an epistemic signal, not silently fused into ground truth.

### 9.3 Bidirectional Cognitive Architecture (Human-in-the-Loop)

```
        ┌────────── RECORD ──────────┐
        ▼                            │
   ┌─────────┐      intent      ┌──────────┐
   │  HUMAN   │ ──────────────► │  AMOS    │
   │  BRAIN   │ ◄────────────── │  COG.    │
   └─────────┘   stimulation    └──────────┘
        ▲        / feedback            │
        └────────── RECORD ────────────┘
```

- Bidirectional BCI (recording + stimulation, e.g., ARC-BCI DigitalBridge, Blindsight) makes AMOS a **full-duplex partner**: receive neural intent, return synthesized feedback/sensation.
- Apple BCI HID establishes native OS-level bidirectional input — an architectural pattern AMOS can mirror for first-class neural I/O channels.

### 9.4 Bandwidth Gap Analysis

| Layer | Scale |
| :--- | :--- |
| **Human brain neurons** | ~**86 billion** |
| **State-of-art implant** (Neuralink N1 / Connexus) | **1,024–1,684 electrodes** (~102,400 aspirational) |
| **Coverage** | 1,024 / 8.6×10¹⁰ ≈ **0.0000012%** of neurons (user-cited figure: ~**0.001%** by a looser definition of sampled circuitry) |

**AMOS reading:** The electrode-to-neuron **bandwidth gap is the binding constraint** on all BCI-mediated cognition. Three compensating vectors:
1. **Sample density, not count** — 1 electrode samples a local population, not one neuron.
2. **Generative decoding** — foundation models infer unobserved cognitive state from sparse observations (compression/vicarious coverage).
3. **Task-selective readout** — decode the *intent-relevant* manifold rather than whole-brain state, drastically lowering effective bandwidth needs.
- AMOS treats BCI as a **sparse cognitive I/O channel** with explicit bandwidth/coverage accounting, not as a full brain-state stream.

---

## 10. Critical Gaps & AMOS Opportunities

### 10.1 Critical Gaps

1. **Long-term implant stability** — thread retraction (Neuralink), gliosis (Utah Array) limit multi-year signal fidelity; NO device has multi-year durability data at high channel density.
2. **No US commercial approval** — China leads (Neuracle NEO); US PMA gate at ~2028–2030 creates a commercialization vacuum.
3. **Calibration burden** — per-user supervised decoding remains heavy absent robust cross-person foundation transfer.
4. **Non-invasive fidelity ceiling** — consumer EEG is far below clinical; ultrasound non-invasive is promising but unproven at scale.
5. **Data standards fragmentation** — despite IEEE P2731 / ISO TS 27571, cross-corpus and cross-device interoperability is incomplete.
6. **Safety evidence depth** — Breakthrough Designation ≠ approval; none of the visual/speech stimulation systems have efficacy-at-scale data.
7. **Ethics/privacy/identity** — neural data is sensitive biometric+internal-state data; no mature governance (China's strategic-industry designation raises dual-use concerns).

### 10.2 AMOS Opportunities

1. **Multi-device sensor fusion runtime** — implement the fusion layer (Section 9.1) as an AMOS adapter, treating heterogeneous BCI channels with per-source epistemic classification.
2. **Cognitive-input substrate** — integrate a neural foundation decoder (DeeperBrain-style SSM) as a `DERIVED` cognitive input, complementing language/vision inputs.
3. **Bidirectional control plane** — model the human-in-the-loop loop as a first-class AMOS runtime partner (stimulation return path).
4. **Bandwidth-aware cognition** — design AMOS reasoning to operate under sparse-channel bounds rather than assuming full neural state.
5. **Governance/standards leadership** — position AMOS's RSCF/authority concepts as a template for BCI data provenance and epistemic classification, aligning with IEEE P2731/P2794.
6. **Non-invasive pilot** — consumer EEG (OpenBCI/Neurable) as an accessible, low-risk testbed for AMOS neural-input experiments before committing to invasive high-fidelity channels.

---

## 11. References & Provenance

- Neuralink PRIME study, Series E (Jun 2025), Blindsight Breakthrough Designation (Sep 2024), next-gen device (2026): Neuralink/JUST RIGHT News/TechCrunch; neuralink.com/trials.
- Orban Convergence / ColombiaOne / Multiple 2026 sources for patient-count and Blindsight timeline.
- Blackrock Neuralace, Tether $200M (Apr 2024), DARPA (Jan 2026): bciintel Device DB, Tesorb BCI comparison (Apr 2026).
- Paradromics Connexus, IDE (Nov 2025), first implant (Jun 2026): paradromics.com; bciintel Device DB.
- Precision Layer 7, 510(k) (Apr 2025), Medtronic partnership (Jan 12, 2026): GlobeNewswire; Bloomberg; MedTech Dive; MassDevice.
- Synchron COMMAND (Sep 2024 results), Apple BCI HID (May 2025), Chiral (Mar 2025), $200M Series D (Nov 2025): businesswire.com; techtimes; clinicaltrials.gov NCT05035823.
- ONWARD ARC-BCI 7 implants (Jan 2026): globenewswire.com; ONWARD Q1 2026 results (May 26, 2026).
- IEEE P2731 / P2794; ISO/IEC TS 27571:2026; ISO/IEC JTC 1/SC 43; ISO/TC 299: standards.ieee.org; iso.org; IEEE SA BMI standards roadmap.
- Market data: bciintel State of BCI 2026 (Mar 2026); Business Research Company; Market Data Forecast; MarketsandMarkets; Grand View Research.

---

## 12. Cross-Vault References

- [[22_RESEARCH/SOTA_BCI_FOUNDATION_MODELS_NEURAL_INTERFACES_2026|SOTA_BCI_FOUNDATION_MODELS_NEURAL_INTERFACES_2026]]
- [[15_INTERFACES/BCI_EXPRESSION_GATEWAY_ADAPTER|BCI_EXPRESSION_GATEWAY_ADAPTER]]
- [[21_DOMAINS/14_C04_BIO_NEURO/C04_NEURAL_DECODING_AND_BCI_ARCHITECTURE|C04_NEURAL_DECODING_AND_BCI_ARCHITECTURE]]
- [[22_RESEARCH/01_PAPERS/SOTA_BCI_AND_NEUROTECHNOLOGY_SYNTHESIS_2026|SOTA_BCI_AND_NEUROTECHNOLOGY_SYNTHESIS_2026]]
- [[22_RESEARCH/RSCF_BCI_SHI_TRANSDURAL_TELEMETRY_2026|RSCF_BCI_SHI_TRANSDURAL_TELEMETRY_2026]]
- [[21_DOMAINS/01_DOMAIN_ARCHITECTURE/C04_BCI_LIFECYCLE_GOVERNANCE_CONTRACT|C04_BCI_LIFECYCLE_GOVERNANCE_CONTRACT]]
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]

---

## RSCF Block

```RSCF-NODE
node_id: sota_bci_neural_interfaces_2026
node_type: research_synthesis
domain: C04_BIO_NEURO
claim_class: DERIVED
state: DERIVED
confidence_ceiling: HIGH_FOR_PLATFORM_PROGRESS; MEDIUM_FOR_REGULATORY_STATUS; LOW_FOR_ARRIVED_CAPABILITY
provenance:
  - company_press_releases_2024_2026
  - regulatory_agency_records_partial
  - market_research_reports_2026
  - bciintel_state_of_bci_2026
  - clinicaltrials_gov_COMMAND_NCT05035823
relations:
  extends: sota_bci_foundation_models_2026
  upstream: c04_neural_decoding_and_bci_architecture
  adapter: bci_expression_gateway_adapter
  payload: rscf_bci_shi_event_based_transdural_telemetry_2026
  governance_contract: c04_bci_lifecycle_governance_contract
falsifiers:
  - A US-invasive BCI receives commercial approval before 2028, invalidating the regulatory-gap thesis
  - Automated fully-implantable speech BCI fails to reach the 2026-2028 recruitment scale
  - Cross-person neural foundation models fail to generalize beyond lab cohorts in deployed clinical settings
  - Non-invasive ultrasound BCI reaches invasive-level motor fidelity, collapsing the invasive premium
  - Neuralink/Connexus thread arrays demonstrate multi-year signal instability at high density
hard_rules:
  - BREAKTHROUGH_DESIGNATION != COMMERCIAL_APPROVAL
  - COMPANY_ANNOUNCEMENT == OBSERVATION_OF_PROGRESS, NOT VERIFIED_CAPABILITY
  - IDE == PERMISSION_TO_TEST, NOT EVIDENCE_OF_EFFECTIVENESS
  - NEWEST_DEVICE_CLAIM != LATEST_AUTHORITATIVE_RESULT (per AGENTS.md LATEST != AUTHORITATIVE)
  - ELECTRODE_COUNT == SAMPLED_SITES, NOT NEURON_COVERAGE (bandwidth-gap discipline)
```
