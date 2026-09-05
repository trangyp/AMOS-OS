---
title: "SOTA LLM Inference Optimization & Reasoning 2026"
type: sota_paper
created: 2026-09-05
updated: 2026-09-05
tags:
  - amos-os
  - sota
  - research
  - llm
  - inference
  - reasoning
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: arxiv_2026
  scope: AMOS_general
---

# SOTA LLM Inference Optimization & Reasoning (2026)

> **Epistemic status:** `SOURCE_CLAIM` · **Provenance:** arXiv 2026 preprints · **Confidence ceiling:** 0.95

## Scope

This paper synthesizes 8 state-of-the-art 2026 preprints covering:
- LLM inference acceleration (speculative decoding, KV-cache compression, sparse attention)
- Test-time compute scaling and reasoning regimes
- Latent-space optimization for reasoning LLMs
- Agentic world models and embodied foundation models

---

## Papers

### 1. CacheSpec — arXiv:2607.20507
- **Domain:** LLM inference acceleration via small-model speculative drafting
- **Key result:** Converts Program-of-Thought programs into reusable cache objects. Uses a small model for variable extraction and speculative drafting, yielding up to ~3.1x latency speedup and ~2.8x throughput improvement while maintaining output quality.
- **AMOS mapping:**
  - [[04_RUNTIME/06_EXECUTION/06_EXECUTION_MOC|06 Execution]] → inference execution pipeline
  - [[07_SKILLS/arxiv-kv-cache-quantization-rscf/SKILL|KV Cache Quantization]] → cache management
  - [[07_SKILLS/amos-budget-aware-optimizer-selection-rscf-engine/SKILL|Budget-Aware]] → small model routing
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

### 2. Long-Context Speculative Decoding with Compressed KV Cache — arXiv:2608.30252
- **Domain:** Speculative decoding for long-context LLM serving
- **Key result:** Adds a compressed, incrementally updated draft-side KV memory to speculative decoding. Preserves exact recent context and long-range dependencies. Speedups of 2.08x (8B model) and 3.33x (70B model) at up to 32K prefix length with no quality loss.
- **AMOS mapping:**
  - [[07_SKILLS/arxiv-long-context-rope-scaling-rscf/SKILL|Long Context RoPE]] → context length scaling
  - [[07_SKILLS/arxiv-kv-cache-quantization-rscf/SKILL|KV Cache]] → compressed KV memory
  - [[07_SKILLS/arxiv-flash-attention-io-rscf/SKILL|Flash Attention IO]] → attention optimization
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.95

### 3. Vegas: Self-Speculative Decoding with Verification-Guided Sparse Attention — arXiv:2602.07223
- **Domain:** Self-speculative decoding with sparse attention
- **Key result:** Identifies critical KV cache entries as a byproduct of verification, enabling sparse attention during drafting. Achieves 1.25x–2.81x throughput gains over vLLM baseline across multiple model sizes.
- **AMOS mapping:**
  - [[07_SKILLS/arxiv-sparse-attention-scaling-rscf/SKILL|Sparse Attention]] → sparse attention patterns
  - [[07_SKILLS/arxiv-streaming-attention-sinks-rscf/SKILL|Streaming Attention Sinks]] → KV cache management
  - [[04_RUNTIME/06_EXECUTION/06_EXECUTION_MOC|06 Execution]] → inference runtime
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

### 4. OasisKV: Scaling In-Decode KV Cache Beyond HBM — arXiv:2608.08097
- **Domain:** KV cache offloading with lookahead prefetching
- **Key result:** Uses lookahead tokens from speculative decoding to prefetch only important KV blocks from host/remote memory. Achieves ~2x throughput under prefill-decode disaggregation with <0.7% accuracy loss.
- **AMOS mapping:**
  - [[07_SKILLS/arxiv-kv-cache-quantization-rscf/SKILL|KV Cache]] → cache hierarchy management
  - [[07_SKILLS/arxiv-activation-checkpointing-rscf/SKILL|Activation Checkpointing]] → memory management
  - [[04_RUNTIME/04_RUNTIME_MOC|04 Runtime]] → memory-aware scheduling
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

### 5. Test-Time Scaling in Reasoning LLMs — arXiv:2608.04001
- **Domain:** Formalization of test-time compute scaling regimes
- **Key result:** Formalizes test-time scaling into three regimes: sequential (chain-of-thought), leaf (tree search), and prefix (draft-then-verify). Provides evaluation/reproducibility guidelines and releases a large trace dataset.
- **AMOS mapping:**
  - [[07_SKILLS/arxiv-test-time-compute-scaling-rscf/SKILL|Test-Time Compute]] → compute scaling framework
  - [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O07_INFERENCE/O07_INFERENCE_MOC|O07 Inference]] → inference lifecycle
  - [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O08_PREDICTION/O08_PREDICTION_MOC|O08 Prediction]] → prediction scaling
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.95

### 6. ∇-Reasoner: LLM Reasoning via Test-Time Gradient Descent — arXiv:2603.04948
- **Domain:** Latent-space optimization for reasoning
- **Key result:** Replaces discrete search with first-order textual optimization during decoding. Improves math-reasoning accuracy by >20% while reducing model calls by 10–40%. Treats reasoning as gradient descent in latent space.
- **AMOS mapping:**
  - [[07_SKILLS/arxiv-test-time-compute-scaling-rscf/SKILL|Test-Time Compute]] → compute-efficient reasoning
  - [[07_SKILLS/amos-mathematical-rigor-rscf-kernel/SKILL|Mathematical Rigor]] → formal reasoning
  - [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O07_INFERENCE/O07_INFERENCE_MOC|O07 Inference]] → inference optimization
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

### 7. Belief-Calibrated Optimization: Explicit World Model for Agentic Optimization — arXiv:2609.01861
- **Domain:** Agentic optimization with persistent world models
- **Key result:** Writes the optimizer's beliefs about environment edits into a persistent in-context world model. Improves both train and held-out performance across memory, tool, and code-as-action tasks.
- **AMOS mapping:**
  - [[07_SKILLS/amos-k-world-model/SKILL|K World Model]] → world model construction
  - [[05_COGNITIVE_ORGANISM/06_WORLD_MODEL/06_WORLD_MODEL_MOC|06 World Model]] → cognitive world model
  - [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O06_MODEL/O06_MODEL_MOC|O06 Model]] → model lifecycle
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

### 8. GigaBrain-0.7: Scaling Embodied Foundation Models — arXiv:2608.15875
- **Domain:** Embodied vision-language-action foundation models
- **Key result:** A 37,000+ hour pre-trained VLA model with one-stage alignment and a three-system architecture (perception, planning, action). Strong zero-shot cross-embodiment generalization and competitive home/industrial robot performance.
- **AMOS mapping:**
  - [[22_RESEARCH/01_PAPERS/SOTA_EMBODIED_ROBOT_FOUNDATION_MODELS_2026|SOTA Embodied Robots]] → embodied AI models
  - [[21_DOMAINS/54_ROBOTICS/54_ROBOTICS_MOC|54 Robotics]] → robotics domain
  - [[15_INTERFACES/15_INTERFACES_README|15 Interfaces]] → embodied interfaces
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

---

## Cross-Domain Themes

### Inference Acceleration
The 2026 SOTA in LLM inference converges on **speculative decoding + KV-cache compression** as the dominant paradigm. CacheSpec, Long-Context Speculative Decoding, Vegas, and OasisKV all exploit the draft-verify pattern with different KV management strategies. The AMOS runtime plane (`04_RUNTIME`) should integrate these as composable inference optimization passes.

### Test-Time Compute Scaling
The formalization of sequential/leaf/prefix regimes (arXiv:2608.04001) provides a framework for AMOS to standardize reasoning-agent inference. The ∇-Reasoner shows that gradient-like optimization in latent space can replace discrete search, reducing model calls by 10-40%.

### World Models for Agents
Belief-Calibrated Optimization demonstrates that persistent in-context world models improve agentic performance. This directly supports the AMOS `K_WORLD_MODEL` kernel contract and the `06_WORLD_MODEL` cognitive organism subsystem.

### Embodied AI Convergence
GigaBrain-0.7 shows that VLA foundation models with 37K+ hours of training can achieve zero-shot cross-embodiment generalization. This bridges the AMOS `15_INTERFACES` and `54_ROBOTICS` domains.

---

## AMOS Integration Plan

| Paper | AMOS Plane | AMOS Skill | Integration Priority |
|-------|-----------|------------|---------------------|
| CacheSpec | 04_RUNTIME | arxiv-kv-cache-quantization-rscf | HIGH |
| Long-Context Spec Decoding | 04_RUNTIME | arxiv-long-context-rope-scaling-rscf | HIGH |
| Vegas | 04_RUNTIME | arxiv-sparse-attention-scaling-rscf | MEDIUM |
| OasisKV | 04_RUNTIME | arxiv-kv-cache-quantization-rscf | MEDIUM |
| Test-Time Scaling | 25_COGNITIVE_MATRIX | arxiv-test-time-compute-scaling-rscf | HIGH |
| ∇-Reasoner | 25_COGNITIVE_MATRIX | arxiv-test-time-compute-scaling-rscf | MEDIUM |
| Belief-Calibrated | 02_KERNEL | amos-k-world-model | HIGH |
| GigaBrain-0.7 | 21_DOMAINS/54_ROBOTICS | — | MEDIUM |

---

## Cross-References

- [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
- [[22_RESEARCH/01_PAPERS/01_PAPERS_MOC|01_PAPERS_MOC]]
- [[22_RESEARCH/01_PAPERS/SOTA_AI_CODING_AGENTS_SELF_EVOLVING_HARNESSES_2026|SOTA AI Coding Agents 2026]]
- [[22_RESEARCH/01_PAPERS/SOTA_BCI_NEURAL_DECODING_FOUNDATION_MODELS_2026|SOTA BCI Neural Decoding 2026]]
- [[22_RESEARCH/01_PAPERS/SOTA_AI_AGENTS_MEMORY_TOOLS_EVOLUTION_2026|SOTA AI Agents Memory & Tools 2026]]
- [[22_RESEARCH/01_PAPERS/SOTA_QUANTUM_SENSING_ERROR_CORRECTION_NETWORKING_2026|SOTA Quantum Sensing & QEC 2026]]
- [[04_RUNTIME/04_RUNTIME_MOC|04 Runtime MOC]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O07_INFERENCE/O07_INFERENCE_MOC|O07 Inference MOC]]
