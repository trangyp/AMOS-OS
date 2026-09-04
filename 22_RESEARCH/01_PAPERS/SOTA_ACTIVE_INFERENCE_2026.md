---
title: SOTA Active Inference 2026
type: research_synthesis
source: 22_RESEARCH/01_PAPERS
tags:
  - sota
  - active-inference
  - free-energy-principle
  - predictive-processing
  - generative-models
  - research
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: web_search_2026-09-04
  scope: active_inference_2026
  freshness: 2026-09-04
  falsifier: "Active inference scaling to real-world robotic control and large-scale models NOT ESTABLISHED"
---

# SOTA Active Inference 2026

**Date:** 2026-09-04
**Epistemic class:** SOURCE_CLAIM (UAI/PMLR, Minds and Machines, arXiv)
**Confidence ceiling:** 0.90

## 1. What Type of Inference is Active Inference? (UAI 2026 / PMLR 337)

- **Result:** AIF = variational inference with specific entropy corrections to VFE
- **Mapping:** Different planning-as-inference methods = different entropy corrections
- **Implementation:** Message-passing via channel reparameterization → standard Bethe free energy
- **Robustness:** Full AIF objective robust across all uncertainty regimes (decisive + suggestive observations)
- **AMOS binding:** `13_MODELS` · `04_RUNTIME` — formal VI framework for cognitive models

## 2. Structure Learning in Active Inference (Minds and Machines 2026)

- **Framework:** AIF provides unified mechanistic account of structure learning
- **Method:** Bayesian model selection within AIF
- **Levels:** 3 types of information processing (inference, associative learning, structure learning)
- **AMOS binding:** `11_KNOWLEDGE` · `13_MODELS` — autonomous model restructuring

## 3. Scale-Free Active Inference — Renormalizing Generative Models (PMC 2026)

- **Innovation:** Discrete state-space with paths as latent variables
- **Hierarchy:** Renormalization group for multi-scale compositionality
- **Applications:** Image classification, movie/music compression+generation, Atari game learning
- **AMOS binding:** `25_COGNITIVE_MATRIX` — hierarchical multi-scale reasoning matrix

## 4. RGM Foundations — Derivations & Verification (arXiv:2608.09512)

- **Contribution:** Self-contained derivation of RGMs; open verified implementation
- **Details:** Hierarchy construction, belief/action updates, inter-level information passing
- **Transparency:** Separates theory from implementation; auditable and reproducible
- **AMOS binding:** `13_MODELS` — verified generative model framework

## 5. Expected Free Energy as Information Constraint (arXiv:2608.17167)

- **Formulation:** Bethe free energy with information constraint for epistemic drive
- **KKT:** Specific multiplier value recovers EFE solution
- **Benefit:** Fully supports inference by message passing (no KL structure issue)
- **AMOS binding:** `03_CONTROL_PLANE` — principled exploration-exploitation in commit decisions

## AMOS Architecture Mapping

| AIF Component | AMOS Plane | Mapping |
|---------------|-----------|---------|
| Variational inference + entropy corrections | `13_MODELS` | Formal cognitive model framework |
| Message-passing scheme | `04_RUNTIME` | Efficient runtime computation |
| Structure learning (Bayesian model selection) | `11_KNOWLEDGE` | Autonomous knowledge restructuring |
| Renormalizing generative models | `25_COGNITIVE_MATRIX` | Multi-scale 19×19 matrix hierarchy |
| Bethe free energy + information constraint | `03_CONTROL_PLANE` | Epistemic drive in commit decisions |
| Scale-free compositionality | `05_COGNITIVE_ORGANISM` | Multi-scale cognitive organism |
| Path latent variables | `12_STATE` | State trajectory representation |

## Falsifiers

- `F-AIF-1`: AIF message-passing efficiency is theoretical — large-scale model performance NOT ESTABLISHED
- `F-AIF-2`: RGM scale-free inference demonstrated on images/music/Atari — real-world robotic control NOT ESTABLISHED
- `F-AIF-3`: Structure learning in AIF is conceptual — computational tractability for complex environments NOT ESTABLISHED
- `F-AIF-4`: Bethe free energy formulation recovers EFE at specific KKT multiplier — sensitivity to multiplier choice NOT FULLY CHARACTERIZED

**Parent:** [[22_RESEARCH/01_PAPERS/SOTA_BCI_AI_QUANTUM_SYNTHESIS_2026|SOTA_BCI_AI_QUANTUM_SYNTHESIS_2026]] · [[22_RESEARCH/22_RESEARCH_README|22_RESEARCH_README]]
