---
title: "Brain2Qwerty v2 — Non-Invasive MEG Brain-to-Text Decoding"
type: research_paper
source: arxiv
arxiv_id: "2608.18114"
url: "https://arxiv.org/abs/2608.18114"
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
epistemic_class: SOURCE_CLAIM
conclusion_class: DERIVED
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance:
    - arxiv:2608.18114
    - 22_RESEARCH/BCI_AI_QUANTUM_SOTA_2026-09-04
  scope: non_invasive_bci_decoding
tags:
  - research
  - arxiv
  - bci
  - meg
  - brain-to-text
  - non-invasive
  - meta
created: 2026-09-04
---

# Brain2Qwerty v2 — Non-Invasive MEG Brain-to-Text Decoding

> **arXiv:** [2608.18114](https://arxiv.org/abs/2608.18114) · Meta/ESPCI, Aug 2026
> **Code:** github.com/facebookresearch/brain2qwerty
> **Epistemic class:** `SOURCE_CLAIM` (peer-reviewed preprint)
> **AMOS bridge:** C04 Bio-Neuro, C05 Mind-Behavior

## Key result

Decodes natural sentences from real-time MEG recordings with **39% average WER**, best participant at 50% sentences with ≤1 word error. Trained on 22,000 sentences × 9 subjects (10 hours each).

Three AI contributions:
1. **Deep learning replaces hand-crafted pipelines** for event detection
2. **LLM finetuning** extracts semantic representations from neural signals
3. **AI agents** iteratively refine the decoding pipeline via automated code development

Critical finding: decoding accuracy **log-linearly improves with data volume**, suggesting the gap with invasive approaches could be partially bridged through data scaling.

## AMOS bridge analysis

### C04 Bio-Neuro: Non-invasive BCI bandwidth

The vault's SOTA ingestion previously listed "Non-invasive BCI bandwidth" as `UNKNOWN/GAP` — EEG/fNIRS bit-rate ceiling ~100 bits/min. Brain2Qwerty v2 demonstrates this gap is **partially bridgeable** through:
- MEG (higher SNR than EEG) + deep learning
- Data scaling (log-linear improvement)
- LLM semantic extraction (language priors constrain the decoding space)

This updates the gap from `UNKNOWN/GAP` to `COMPETING` — a path exists but requires MEG (not portable) and significant data collection.

### C05 Mind-Behavior: AI-agent-iterated pipeline

The use of AI agents to iteratively refine the decoding pipeline via automated code development is a direct instance of AMOS C05 cognitive process orchestration:
- Agent observes decoding performance
- Agent proposes code modifications
- Agent evaluates modified pipeline
- Loop continues until performance threshold

This maps to AMOS closed-loop learning: observe → hypothesize → modify → evaluate → admit/reject.

### RSCF: Data scaling claim

The log-linear improvement claim is `SOURCE_CLAIM` from the paper. AMOS should not promote this to `DERIVED` without independent verification of the scaling exponent across different MEG systems and subjects.

## Epistemic boundary

- Results are from 9 subjects at 2 institutions. Generalization is `COMPETING` until broader validation.
- MEG requires shielded rooms and cryogenic sensors — not wearable. The "non-invasive" advantage is partially offset by infrastructure requirements.
- AI-agent pipeline refinement introduces meta-level uncertainty: the pipeline itself is an artifact of agent exploration, not a human-designed architecture.

## Related

- [[22_RESEARCH/BCI_AI_QUANTUM_SOTA_2026-09-04|BCI/AI/Quantum SOTA 2026-09-04]]
- [[07_SKILLS/amos-c04-bio-neuro-master/SKILL|C04 Bio-Neuro Master]]
- [[07_SKILLS/amos-c05-mind-behavior-master/SKILL|C05 Mind-Behavior Master]]
- [[07_SKILLS/amos-closed-loop-learning-governor/SKILL|Closed-Loop Learning Governor]]
- [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
