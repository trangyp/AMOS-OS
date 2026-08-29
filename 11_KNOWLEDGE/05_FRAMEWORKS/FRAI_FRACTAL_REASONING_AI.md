---
title: FRAI — Fractal Reasoning AI
type: fractal
source: 11_KNOWLEDGE/05_FRAMEWORKS
artifact: FRAI_FRACTAL_REASONING_AI.md
artifact_id: amos_11_knowledge_05_frameworks_frai_fractal_reasoning_ai
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 11_KNOWLEDGE
segment: 11_KNOWLEDGE/05_FRAMEWORKS
artifact_kind: REASONING
path: 11_KNOWLEDGE/05_FRAMEWORKS/FRAI_FRACTAL_REASONING_AI.md
tags:
- amos-os
- knowledge
- vault
- 11_knowledge
- 05_frameworks
- frai
- fractal_reasoning_ai
- self_similarity
- multi_scale_reasoning
- lmh_architecture
- recursive_decomposition
- rscf
- canon_candidate
- canon/knowledge
- ldai-logically-deterministic-ai
- trang-lmh-architecture
- trang-reality-architecture
- khung-trang
version: 1.0.0
updated: '2026-08-27'
status: ACTIVE_REFERENCE
epistemic_class: AMOS_MODEL
canonical_status: SOURCE_GROUNDED_CANON_CANDIDATE
implementation_status: CONCEPTUAL_SOURCE_DEFINED
validation_status: NOT_INDEPENDENTLY_ESTABLISHED
executable_binding: NOT_ESTABLISHED
ingestion_action: NATIVE_CANON_INGESTION
raw_source_policy: DO_NOT_LOAD_UNLESS_REQUIRED
rscf:
  state: SOURCE_CLAIM
  claim_class: AMOS_MODEL
  provenance:
  - TRANG_FRAI_FRACTAL_REASONING_AI
  - AMOS_FRACTAL_CONSCIOUSNESS_WHITEPAPER_FULL_FIXED
  - AMOS_CORPUS
  scope:
  - KNOWLEDGE_FRAMEWORKS
  - FRACTAL_REASONING
  - SOURCE_DEFINED_FRAI_MODEL
framework_binding:
  primary:
    name: Trang FRAI (Fractal Reasoning AI)
    acronym: FRAI
    role: MULTI_SCALE_FRACTAL_REASONING_ENGINE
  underlying_deterministic_engine:
    name: Trang LDAI (Logically Deterministic AI)
    acronym: LDAI
    artifact:
    - - LDAI_LOGICALLY_DETERMINISTIC_AI
  structural_grounding:
    name: Trang LMH Architecture
    artifact:
    - - TRANG_LMH_ARCHITECTURE
  cognitive_matrix_binding:
    artifact:
    - - 25_COGNITIVE_MATRIX_MOC
epistemic_boundary:
  source_presence: VERIFIED_SOURCE_PRESENCE
  framework_structure: VERIFIED_SOURCE_STRUCTURE
  fractal_logic: SOURCE_DEFINED_MODEL
  runtime_enforcement: NOT_ESTABLISHED
---

# FRAI — Fractal Reasoning AI™

`FRAI_FRACTAL_REASONING_AI.md` is the canonical Knowledge Plane reference artifact for **Trang FRAI (Fractal Reasoning AI)** within `11_KNOWLEDGE/05_FRAMEWORKS`.

FRAI models and operates over recursive, self-similar **[L, M, H]** structures across all scales of observation and abstraction.

---

# 1. Formal Definition

$$\text{FRAI} = \langle \mathcal{D}, \mathcal{S}, \mathcal{R}, \mathcal{I}, \mathcal{A}, \mathcal{T}_2 \rangle$$

Where:
* $\mathcal{D}$: **Fractal Decomposer** — recursively partitions inputs into $[L, M, H]$ layers:
  $$\mathcal{D}(X) = (L_X, M_X, H_X), \quad L_X = (L_{L_X}, M_{L_X}, H_{L_X}), \dots$$
* $\mathcal{S}$: **Self-Similarity Detector** — identifies invariant relational patterns repeating across macro, meso, and micro scales.
* $\mathcal{R}$: **Multi-Layer Reasoner** — applies specialized reasoning strategies per tier:
  * **Layer L (Foundation/Substrate):** High consistency, low entropy ($E_L < 0.1$), deterministic logic (LDAI).
  * **Layer M (Flow/Coordination):** Intermediate entropy ($0.1 \le E_M \le 0.2$), probabilistic routing and adaptive tuning.
  * **Layer H (Apex/Creative):** Flexible boundary exploration ($0.1 \le E_H \le 0.3$), hypothesis generation, fast decisions.
* $\mathcal{I}$: **Integrator** — synthesizes multi-tier evaluations into a unified action.
* $\mathcal{A}$: **Adaptive Tuner** — refines scaling parameters based on environmental feedback.
* $\mathcal{T}_2$: **Dual-Path Cross-Validation** — enforces two independent verification routes before state commit.

---

# 2. Inter-Plane & Vault Connections

- **Deterministic Base:** [[LDAI_LOGICALLY_DETERMINISTIC_AI]]
- **Tri-Layer Architecture:** [[TRANG_LMH_ARCHITECTURE]]
- **Ontology & Reality:** [[TRANG_REALITY_ARCHITECTURE]] and [[KHUNG_TRANG]]
- **Native Sources:** `11_KNOWLEDGE/fractal/TRANG_FRAI_FRACTAL_REASONING_AI`

---

# 3. RSCF Contract

```yaml
RSCF:
  node_id: amos_11_knowledge_05_frameworks_frai_fractal_reasoning_ai
  node_type: framework
  claim_class: AMOS_MODEL
  state: SOURCE_CLAIM
  H:
    identity: "Trang FRAI (Fractal Reasoning AI)"
    role: "Recursive self-similar multi-scale reasoning engine"
  M:
    primitives: [decomposer, self_similarity, multi_layer_reasoner, integrator, adaptive_tuner, t2_validator]
    tiers: [L_deterministic, M_probabilistic, H_generative]
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
```

---

**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[05_FRAMEWORKS_MOC]] · [[LDAI_LOGICALLY_DETERMINISTIC_AI]] · [[TRANG_LMH_ARCHITECTURE]] · [[TRANG_REALITY_ARCHITECTURE]]

---
**MOC:** [[05_FRAMEWORKS_MOC]]
