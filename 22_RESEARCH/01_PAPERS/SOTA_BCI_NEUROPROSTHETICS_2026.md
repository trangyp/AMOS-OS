---
title: SOTA BCI Neuroprosthetics 2026
type: research_synthesis
source: 22_RESEARCH/01_PAPERS
tags:
  - sota
  - bci
  - neuroprosthetics
  - research
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: web_search_2026-09-04
  scope: BCI_neuroprosthetics_2026
  freshness: 2026-09-04
  falsifier: "BCI performance claims are from published peer-reviewed studies but generalization to broader populations requires additional clinical trials"
---

# SOTA BCI Neuroprosthetics 2026

**Date:** 2026-09-04
**Epistemic class:** SOURCE_CLAIM (peer-reviewed publications)
**Confidence ceiling:** 0.95 (single-participant studies limit generalizability)

## 1. Long-Term Independent Home Use (Nature Medicine 2026)

- **Participants:** 1 (ALS with severe dysarthria)
- **Duration:** ~2 years, 3,800+ hours at home
- **Performance:** 56 wpm, 99% word accuracy (125k vocab), 1.96M words communicated
- **Independence:** No researchers present during use
- **Impact:** Sustained full-time employment despite paralysis
- **AMOS binding:** `15_INTERFACES` — demonstrates BCI viability as primary communication interface

## 2. Double Neural Bypass (Nature Medicine 2026)

- **System:** BCI + spinal cord stimulation + cortical microstimulation
- **Participant:** C4 sensory / C5 motor complete tetraplegia
- **Capabilities:** Self-feeding, delicate object manipulation
- **Recovery:** Persistent improvements in elbow flexion and wrist tactile sensation after system off
- **Technology:** Recurrent ANN + RL for fine grasp control
- **AMOS binding:** `04_RUNTIME` — closed-loop bio-digital system with bidirectional feedback

## 3. Bimanual Typing Neuroprosthesis (Nature Neuroscience 2026)

- **Participants:** 2 (ALS + SCI)
- **Performance:** 110 cpm, 22 wpm, 1.6% WER
- **Calibration:** 30 sentences
- **Approach:** QWERTY finger movement decoding + 5-gram language model
- **AMOS binding:** `15_INTERFACES` — near-able-bodied communication rates

## 4. Tactile-Encoded BCI for Supernumerary Limbs (Nature Communications 2026)

- **Participants:** 10 able-bodied
- **Approach:** Tactile P300 paradigm (sensory afferents, not motor)
- **Capabilities:** 4 DoF supernumerary control, concurrent with natural movement
- **Training:** 3 days for significant improvement
- **AMOS binding:** `13_MODELS` — movement augmentation without natural impairment

## 5. Sensory-Guided Human-Machine Joint Learning (Nature Communications 2026)

- **Participants:** 31 BCI-naive
- **Performance:** 86% (1D), 77.5% (2D) online accuracy
- **Approach:** Human motor learning + adaptive ML
- **AMOS binding:** `13_MODELS` — rapid BCI skill acquisition framework

## Falsifiers

- `F-BCI-1`: N=1 or N=2 studies — generalization NOT ESTABLISHED
- `F-BCI-2`: Long-term durability beyond study period NOT ESTABLISHED
- `F-BCI-3`: Supernumerary limb control in able-bodied users — applicability to motor-impaired NOT ESTABLISHED

**Parent:** [[22_RESEARCH/01_PAPERS/SOTA_BCI_AI_QUANTUM_SYNTHESIS_2026|SOTA_BCI_AI_QUANTUM_SYNTHESIS_2026]] · [[22_RESEARCH/22_RESEARCH_README|22_RESEARCH_README]]
