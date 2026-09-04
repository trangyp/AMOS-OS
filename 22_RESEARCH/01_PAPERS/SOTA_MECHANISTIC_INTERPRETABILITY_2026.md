---
title: SOTA Mechanistic Interpretability 2026
type: research_synthesis
source: 22_RESEARCH/01_PAPERS
tags:
  - sota
  - mechanistic-interpretability
  - sparse-autoencoders
  - circuit-analysis
  - research
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: web_search_2026-09-04
  scope: mechanistic_interpretability_2026
  freshness: 2026-09-04
  falsifier: "Interpretability methods validated on small models — scaling to 100B+ parameters NOT ESTABLISHED"
---

# SOTA Mechanistic Interpretability 2026

**Date:** 2026-09-04
**Epistemic class:** SOURCE_CLAIM (arXiv + ACL peer-reviewed)
**Confidence ceiling:** 0.90

## 1. CircuitLasso — Scalable Circuit Learning (arXiv:2606.16939)

- **Method:** Sparse linear regression for SAE feature circuits
- **Performance:** Matches intervention-based accuracy at fraction of cost
- **Capability:** Uncovers how SAE features propagate through model layers
- **AMOS binding:** `17_OBSERVABILITY` — scalable model monitoring

## 2. Subspace-Aware SAEs (SASA) (arXiv:2606.06333)

- **Problem:** Single-direction SAE decoders cause exponential feature splitting (exp(d_i) atoms for d_i-dimensional features)
- **Solution:** Learned decoder subspaces with block sparsity + nuclear-norm regularizer
- **Result:** Polynomial sample complexity O(poly(d_i)) vs exponential; validated on GPT-2 + Mistral-7B
- **AMOS binding:** `13_MODELS` — scalable interpretability for large models

## 3. Causal Semantic Modules via SAE Coactivation (ACL 2026)

- **Method:** SAE feature coactivation from handful of prompts
- **Capability:** Identify concept + relation components; ablation changes outputs predictably
- **Composition:** Concept × relation components yield compound counterfactuals
- **Architecture:** Concept components in early layers; relation components in later layers
- **AMOS binding:** `03_CONTROL_PLANE` — model steering via component manipulation

## 4. Neuron Basis Circuits (arXiv:2601.22594)

- **Finding:** MLP neurons are as sparse a feature basis as SAEs
- **Circuit size:** ~10² MLP neurons control subject-verb agreement behavior
- **Multi-hop:** Small neuron sets encode reasoning steps (city→state→capital)
- **Steering:** Neuron steering changes model output predictably
- **AMOS binding:** `17_OBSERVABILITY` — direct neuron monitoring without SAE overhead

## 5. AdaptiveK SAE — Complexity-Driven (ACL Findings 2026)

- **Innovation:** Dynamic sparsity based on input semantic complexity
- **Signal:** Context complexity linearly encoded in LLM representations (via linear probes)
- **Result:** Outperforms fixed sparsity on reconstruction, explained variance, cosine similarity, interpretability
- **AMOS binding:** `13_MODELS` — adaptive interpretability based on task complexity

## AMOS Architecture Mapping

| MI Component | AMOS Plane | Mapping |
|--------------|-----------|---------|
| Circuit tracing | `17_OBSERVABILITY` | Monitor causal circuits in production |
| SAE feature subspaces | `13_MODELS` | Multi-dimensional model features |
| Causal semantic modules | `03_CONTROL_PLANE` | Steer model behavior via component control |
| Neuron basis circuits | `17_OBSERVABILITY` | Direct monitoring without SAE training |
| Adaptive sparsity | `13_MODELS` | Complexity-aware interpretability |
| Feature propagation | `04_RUNTIME` | Trace information flow through runtime |

## Falsifiers

- `F-MI-1`: CircuitLasso validated on benchmarks — production-scale (100B+) NOT ESTABLISHED
- `F-MI-2`: SASA polynomial complexity is theoretical — empirical beyond Mistral-7B NOT ESTABLISHED
- `F-MI-3`: Causal semantic modules from few prompts — robustness with adversarial inputs NOT ESTABLISHED
- `F-MI-4`: Neuron basis sparsity found in specific architectures — universality across model families NOT ESTABLISHED

**Parent:** [[22_RESEARCH/01_PAPERS/SOTA_BCI_AI_QUANTUM_SYNTHESIS_2026|SOTA_BCI_AI_QUANTUM_SYNTHESIS_2026]] · [[22_RESEARCH/22_RESEARCH_README|22_RESEARCH_README]]
