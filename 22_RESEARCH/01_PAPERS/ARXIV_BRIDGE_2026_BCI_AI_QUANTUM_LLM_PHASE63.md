---
title: "arXiv Bridge 2026 — BCI/AI/Quantum/LLM SOTA Phase 63"
type: arxiv_bridge
created: 2026-09-05
updated: 2026-09-05
tags:
  - amos-os
  - arxiv
  - bridge
  - sota
  - bci
  - ai-agents
  - quantum
  - llm
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: arxiv_2026
  scope: AMOS_general
---

# arXiv Bridge 2026 — BCI/AI/Quantum/LLM SOTA (Phase 63)

> **Epistemic status:** `SOURCE_CLAIM` · **Provenance:** arXiv 2026 preprints · **Confidence ceiling:** 0.95
> **Papers bridged:** 32 across 4 domains

## Purpose

This bridge file links 32 arXiv 2026 preprints to their corresponding AMOS OS SOTA synthesis papers, AMOS skill mappings, and canonical domain references. It serves as the provenance chain for the September 2026 SOTA integration.

---

## BCI / Neural Decoding (8 papers)

### 1. Brain2Qwerty v2 — arXiv:2608.18114
- **Domain:** Non-invasive MEG sentence decoding
- **Key result:** ~39% WER, LLM semantic representations, iterative AI-agent pipeline
- **AMOS mapping:** [[15_INTERFACES/15_INTERFACES_README|Interfaces]] · [[22_RESEARCH/01_PAPERS/SOTA_BCI_NEURAL_DECODING_FOUNDATION_MODELS_2026|SOTA BCI]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

### 2. Contextual seq2seq Speech Decoding — arXiv:2603.20246
- **Domain:** Intracortical speech decoding
- **Key result:** 14.3% phoneme error, 19.4% WER with rescoring, NHS calibration
- **AMOS mapping:** [[15_INTERFACES/15_INTERFACES_README|Interfaces]] · [[21_DOMAINS/14_C04_BIO_NEURO/14_C04_BIO_NEURO_MOC|C04 Bio Neuro]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

### 3. OVMI for Speech BCIs — arXiv:2609.02887
- **Domain:** Information-theoretic BCI benchmarking
- **Key result:** Open-vocabulary mutual information, 16.3% accuracy improvement
- **AMOS mapping:** [[07_SKILLS/amos-information-theory-master/SKILL|Information Theory]] · [[17_OBSERVABILITY/17_OBSERVABILITY_README|Observability]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.95

### 4. UniBCI — arXiv:2605.00061
- **Domain:** Foundation model for invasive BCI
- **Key result:** Cross-species/subject/region, context-conditioned tokenization
- **AMOS mapping:** [[13_MODELS/13_MODELS_README|Models]] · [[15_INTERFACES/15_INTERFACES_README|Interfaces]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

### 5. EEG-PRIME — arXiv:2608.13072
- **Domain:** EEG foundation model
- **Key result:** Subject-invariant, instruction-aware representations
- **AMOS mapping:** [[13_MODELS/13_MODELS_README|Models]] · [[15_INTERFACES/15_INTERFACES_README|Interfaces]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

### 6. BrainDistill — arXiv:2601.17625
- **Domain:** Compact implantable neural decoder
- **Key result:** Task-specific knowledge distillation, integer-only inference
- **AMOS mapping:** [[07_SKILLS/amos-budget-aware-optimizer-selection-rscf-engine/SKILL|Budget-Aware]] · [[15_INTERFACES/15_INTERFACES_README|Interfaces]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.85

### 7. Real-Time Movement Onset/Offset — arXiv:2603.16825
- **Domain:** Closed-loop motor BCI
- **Key result:** Dual-state EEG, rehabilitation exoskeleton control
- **AMOS mapping:** [[21_DOMAINS/54_ROBOTICS/54_ROBOTICS_MOC|54 Robotics]] · [[15_INTERFACES/15_INTERFACES_README|Interfaces]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.85

### 8. NeuroPath — arXiv:2604.09654
- **Domain:** Motor-imagery EEG decoding
- **Key result:** Unified architecture, consumer-grade EEG, cross-montage
- **AMOS mapping:** [[15_INTERFACES/15_INTERFACES_README|Interfaces]] · [[13_MODELS/13_MODELS_README|Models]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.85

---

## AI Agents / Memory / Tools (8 papers)

### 9. ToolAtlas — arXiv:2607.11126
- **Domain:** Tool-side memory graph
- **Key result:** 21.6% pass@1 improvement, cross-agent transfer
- **AMOS mapping:** [[07_SKILLS/amos-agent-systems-master/SKILL|Agent Systems]] · [[14_TOOLS/14_TOOLS_README|Tools]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

### 10. AutoAgent — arXiv:2603.09716
- **Domain:** Self-evolving multi-agent framework
- **Key result:** Elastic memory compression, closed-loop skill updating
- **AMOS mapping:** [[07_SKILLS/amos-autonomous-evolution/SKILL|Autonomous Evolution]] · [[06_AGENTS/06_AGENTS_README|Agents]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

### 11. MAP-Graph — arXiv:2608.10509
- **Domain:** Provenance-aware shared memory
- **Key result:** 94.96% task success, typed execution graph
- **AMOS mapping:** [[10_MEMORY/10_MEMORY_MOC|Memory]] · [[07_SKILLS/amos-memory-systems-master/SKILL|Memory Systems]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

### 12. LatticeMind — arXiv:2608.08236
- **Domain:** Conflict-aware memory primitive
- **Key result:** 0.97 conflict detection accuracy
- **AMOS mapping:** [[07_SKILLS/amos-memory-conflict-governor/SKILL|Memory Conflict]] · [[10_MEMORY/10_MEMORY_MOC|Memory]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

### 13. HarnessEvolve — arXiv:2609.00829
- **Domain:** Agent self-evolution with reference trajectories
- **Key result:** Prevents catastrophic forgetting, gates updates
- **AMOS mapping:** [[07_SKILLS/amos-autonomous-evolution/SKILL|Autonomous Evolution]] · [[07_SKILLS/amos-evolution-loop/SKILL|Evolution Loop]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.85

### 14. GSE — arXiv:2608.06153
- **Domain:** Globally reusable coding skills
- **Key result:** 61.4% F1 improvement, Skill Relation Graph
- **AMOS mapping:** [[07_SKILLS/07_SKILLS_MOC|Skills]] · [[07_SKILLS/amos-c10-tech-engineering-master/SKILL|C10 Tech]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

### 15. Ouroboros — arXiv:2608.08311
- **Domain:** Self-developing coding agent
- **Key result:** SOTA Terminal-Bench 2.1, reviewed core evolution
- **AMOS mapping:** [[07_SKILLS/amos-autonomous-evolution/SKILL|Autonomous Evolution]] · [[07_SKILLS/amos-code-agent-harness-rscf/SKILL|Code Agent Harness]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

### 16. FlowEvo — arXiv:2607.21596
- **Domain:** Workflow-skill co-evolution
- **Key result:** 85.6% ALFWorld, ~1/3 token usage
- **AMOS mapping:** [[08_WORKFLOWS/08_WORKFLOWS_MOC|Workflows]] · [[07_SKILLS/amos-workflow-builder/SKILL|Workflow Builder]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

---

## Quantum Sensing / QEC / Networking (8 papers)

### 17. Fault-Tolerant Heisenberg-Limited Sensing — arXiv:2608.00171
- **Domain:** Quantum sensing with fault tolerance
- **Key result:** Heisenberg scaling restoration under noise
- **AMOS mapping:** [[21_DOMAINS/41_QUANTUM_SYSTEMS/41_QUANTUM_SYSTEMS_MOC|41 Quantum]] · [[22_RESEARCH/01_PAPERS/SOTA_QUANTUM_SENSING_METROLOGY_2026|SOTA Quantum Sensing]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.95

### 18. Noise-Symmetry QEC Metrology — arXiv:2608.21842
- **Domain:** QEC encoding optimization
- **Key result:** Symmetry freedom in QEC, SQL to Heisenberg scaling
- **AMOS mapping:** [[21_DOMAINS/41_QUANTUM_SYSTEMS/41_QUANTUM_SYSTEMS_MOC|41 Quantum]] · [[07_SKILLs/amos-mathematical-rigor-rscf-kernel/SKILL|Mathematical Rigor]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.95

### 19. ML QEC Thresholds — arXiv:2606.22194
- **Domain:** Neural QEC decoders
- **Key result:** Transformer decoders, coherent information to BCE, outperforms MWPM
- **AMOS mapping:** [[13_MODELS/13_MODELS_README|Models]] · [[21_DOMAINS/41_QUANTUM_SYSTEMS/41_QUANTUM_SYSTEMS_MOC|41 Quantum]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

### 20. Scalable Neural Decoders — arXiv:2604.08358
- **Domain:** CNN decoder for quantum LDPC
- **Key result:** 10^-10 logical error rate, 3-5 orders higher throughput
- **AMOS mapping:** [[04_RUNTIME/04_RUNTIME_MOC|Runtime]] · [[21_DOMAINS/41_QUANTUM_SYSTEMS/41_QUANTUM_SYSTEMS_MOC|41 Quantum]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.95

### 21. SatQNet — arXiv:2604.09306
- **Domain:** Satellite quantum network routing
- **Key result:** RL entanglement router, directed line graph GNN
- **AMOS mapping:** [[09_PROTOCOLS/09_PROTOCOLS_MOC|Protocols]] · [[21_DOMAINS/60_SPACE_EXPLORATION/60_SPACE_EXPLORATION_MOC|60 Space]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

### 22. Dynamic Entanglement Distribution — arXiv:2607.15262
- **Domain:** Metropolitan quantum network
- **Key result:** q-ROADM, 6 users, 150+ hours, multi-protocol
- **AMOS mapping:** [[09_PROTOCOLS/09_PROTOCOLS_MOC|Protocols]] · [[18_SECURITY/18_SECURITY_README|Security]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

### 23. Finite-Noise Quantum ML — arXiv:2608.24229
- **Domain:** Quantum ML theory
- **Key result:** Statistical learning theory, finite-noise optimum
- **AMOS mapping:** [[07_SKILLS/amos-rscf-epistemic-master/SKILL|RSCF Epistemic]] · [[13_MODELS/13_MODELS_README|Models]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

### 24. Hybrid Quantum Neural Networks — arXiv:2608.01194
- **Domain:** Hybrid QNN review
- **Key result:** Architecture survey, implementation challenges
- **AMOS mapping:** [[13_MODELS/13_MODELS_README|Models]] · [[21_DOMAINS/41_QUANTUM_SYSTEMS/41_QUANTUM_SYSTEMS_MOC|41 Quantum]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.85

---

## LLM Inference / Reasoning (8 papers)

### 25. CacheSpec — arXiv:2607.20507
- **Domain:** Small-model speculative drafting
- **Key result:** 3.1x latency speedup, 2.8x throughput
- **AMOS mapping:** [[04_RUNTIME/06_EXECUTION/06_EXECUTION_MOC|06 Execution]] · [[07_SKILLS/arxiv-kv-cache-quantization-rscf/SKILL|KV Cache]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

### 26. Long-Context Speculative Decoding — arXiv:2608.30252
- **Domain:** Compressed KV for speculative decoding
- **Key result:** 2.08x (8B), 3.33x (70B) at 32K prefix
- **AMOS mapping:** [[07_SKILLS/arxiv-long-context-rope-scaling-rscf/SKILL|Long Context]] · [[04_RUNTIME/04_RUNTIME_MOC|Runtime]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.95

### 27. Vegas — arXiv:2602.07223
- **Domain:** Self-speculative sparse attention
- **Key result:** 1.25x-2.81x throughput over vLLM
- **AMOS mapping:** [[07_SKILLS/arxiv-sparse-attention-scaling-rscf/SKILL|Sparse Attention]] · [[04_RUNTIME/04_RUNTIME_MOC|Runtime]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

### 28. OasisKV — arXiv:2608.08097
- **Domain:** KV cache beyond HBM
- **Key result:** ~2x throughput, <0.7% accuracy loss
- **AMOS mapping:** [[07_SKILLS/arxiv-kv-cache-quantization-rscf/SKILL|KV Cache]] · [[04_RUNTIME/04_RUNTIME_MOC|Runtime]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

### 29. Test-Time Scaling Regimes — arXiv:2608.04001
- **Domain:** Reasoning LLM evaluation framework
- **Key result:** Sequential/leaf/prefix regimes, reproducibility guidelines
- **AMOS mapping:** [[07_SKILLS/arxiv-test-time-compute-scaling-rscf/SKILL|Test-Time Compute]] · [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O07_INFERENCE/O07_INFERENCE_MOC|O07 Inference]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.95

### 30. ∇-Reasoner — arXiv:2603.04948
- **Domain:** Latent-space gradient descent reasoning
- **Key result:** >20% math accuracy, 10-40% fewer model calls
- **AMOS mapping:** [[07_SKILLS/arxiv-test-time-compute-scaling-rscf/SKILL|Test-Time Compute]] · [[07_SKILLS/amos-mathematical-rigor-rscf-kernel/SKILL|Mathematical Rigor]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

### 31. Belief-Calibrated Optimization — arXiv:2609.01861
- **Domain:** Agentic world model optimization
- **Key result:** Persistent in-context world model, improved held-out performance
- **AMOS mapping:** [[07_SKILLS/amos-k-world-model/SKILL|K World Model]] · [[05_COGNITIVE_ORGANISM/06_WORLD_MODEL/06_WORLD_MODEL_MOC|06 World Model]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

### 32. GigaBrain-0.7 — arXiv:2608.15875
- **Domain:** Embodied VLA foundation model
- **Key result:** 37K+ hours, three-system architecture, zero-shot cross-embodiment
- **AMOS mapping:** [[21_DOMAINS/54_ROBOTICS/54_ROBOTICS_MOC|54 Robotics]] · [[22_RESEARCH/01_PAPERS/SOTA_EMBODIED_ROBOT_FOUNDATION_MODELS_2026|SOTA Embodied]]
- **Epistemic class:** SOURCE_CLAIM · **Confidence ceiling:** 0.90

---

## SOTA Synthesis Papers Linked

| SOTA Paper | Papers | Domain |
|-----------|--------|--------|
| [[22_RESEARCH/01_PAPERS/SOTA_BCI_NEURAL_DECODING_FOUNDATION_MODELS_2026\|SOTA BCI Neural Decoding]] | 8 | BCI |
| [[22_RESEARCH/01_PAPERS/SOTA_AI_AGENTS_MEMORY_TOOLS_EVOLUTION_2026\|SOTA AI Agents Memory & Tools]] | 8 | AI Agents |
| [[22_RESEARCH/01_PAPERS/SOTA_QUANTUM_SENSING_ERROR_CORRECTION_NETWORKING_2026\|SOTA Quantum Sensing & QEC]] | 8 | Quantum |
| [[22_RESEARCH/01_PAPERS/SOTA_LLM_INFERENCE_OPTIMIZATION_REASONING_2026\|SOTA LLM Inference & Reasoning]] | 8 | LLM |

---

## Cross-References

- [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
- [[22_RESEARCH/01_PAPERS/01_PAPERS_MOC|01_PAPERS_MOC]]
- [[20_OPERATIONS/AMOS_OS_AUDIT_FIX_EXPANSION_2026-09-04|Audit Fix Expansion]]
- [[20_OPERATIONS/AMOS_OS_MECE_AUDIT_2026-09-04|MECE Audit]]
- [[20_OPERATIONS/AMOS_MECE_FIX_LOG_2026-09-05|MECE Fix Log]]
