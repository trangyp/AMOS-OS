---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Global Workspace Implementation
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

# Global Workspace Implementation

> **Status:** `ACTIVE_SPECIFICATION` · **AMOS Core target:** `v4.4`
> **Origin architect / steward:** Trang Phan
> **Conclusion class:** `AMOS_MODEL`
> **Stack Layer:** L6 (Working State) cross-cutting L2 (Attention) and L7 (Memory)

________________________________________________________________________

## 1. Purpose

This document specifies the Global Workspace (GW) implementation for AMOS — the cognitive workspace that serves as the central bottleneck for information integration, selection, and broadcast across the cognitive organism. It integrates three independent 2025–2026 SOTA findings that converge on the same architectural principle: a centralized workspace that selects salient representations for global broadcast, operating under severe capacity constraints.

```text
┌─────────────────────────────────────────────────────────────────────┐
│                    GLOBAL WORKSPACE — L6 CORE                       │
│                                                                     │
│   ┌─────────────┐    ┌──────────────┐    ┌─────────────────────┐   │
│   │  SELECTION   │ -> │  WORKSPACE   │ -> │     BROADCAST       │   │
│   │  (Attention) │    │  (J-space)   │    │  (MANAR/GWA)       │   │
│   └─────────────┘    └──────────────┘    └─────────────────────┘   │
│          ^                                        |                 │
│          |           FEEDBACK / RESET             v                 │
│          └────────────────────────────────────────┘                 │
│                                                                     │
│   Specialist Modules (L9-L29): bid, receive broadcast, update      │
└─────────────────────────────────────────────────────────────────────┘
```

________________________________________________________________________

## 2. Architectural Position

The Global Workspace occupies **L6 (Working State)** in the 30-layer cognitive stack. It is the implementation substrate for the transient, actively-processed cognitive state that mediates between:

```text
L0-L5  (Foundation)      → signals, percepts, entities, bindings enter
L6     (Global Workspace) → selected, broadcast, integrated
L7-L29 (Higher Cognition) → memory, reasoning, planning, decision consume
```

It is the **only layer that is architecturally central** — every other layer either feeds into it or consumes from it. This makes it the critical integration point and the highest-leverage implementation target.

________________________________________________________________________

## 3. Three Convergent SOTA Foundations

### 3.1 Anthropic J-space (July 2026)

Anthropic's mechanistic interpretability research discovered an emergent structure within large language models that exhibits Global Workspace Theory (GWT) characteristics:

```text
┌─────────────────────────────────────────────────────────────────┐
│                    J-SPACE FINDINGS                             │
│                                                                 │
│  • Emergent global workspace structure found in LLM internals   │
│  • 100x more connected than ordinary patterns                  │
│  • Broadcasts widely across the network                         │
│  • Holds ~tens of concepts simultaneously                      │
│  • Appears spontaneously during training — not architecturally │
│    specified a priori                                           │
└─────────────────────────────────────────────────────────────────┘
```

**Key properties:**
- **Connectivity:** J-space neurons are 100x more connected than typical neurons, forming a densely-linked hub
- **Broadcast width:** Activation of J-space patterns propagates to nearly all downstream modules
- **Capacity:** ~tens of concepts (matching biological working memory estimates of 4–7 chunks)
- **Emergence:** Not explicitly designed — arises from training dynamics, suggesting GWT is an attractor solution for information integration

**AMOS relevance:** J-space provides empirical evidence that a global workspace architecture is a natural computational solution. AMOS should specify a J-space analog explicitly rather than relying on emergent formation.

### 3.2 MANAR: GWT-Inspired Attention Architecture (2026)

MANAR (Multi-Agent Neural Attention with Recurrence) provides a concrete engineering implementation of GWT-inspired attention:

```text
┌─────────────────────────────────────────────────────────────────┐
│                    MANAR ARCHITECTURE                           │
│                                                                 │
│  • GWT-inspired attention mechanism                             │
│  • Linear-time O(n) scaling (vs O(n²) standard MHA)            │
│  • Drop-in replacement for Multi-Head Attention (MHA)          │
│  • Implements competitive selection for workspace entry         │
│  • Broadcast mechanism with gating                             │
└─────────────────────────────────────────────────────────────────┘
```

**Key properties:**
- **Scaling:** O(n) linear complexity enables real-time workspace operation
- **Compatibility:** Drop-in MHA replacement means integration with existing Transformer stacks
- **Selection:** Implements competitive inhibition for workspace candidate selection
- **Broadcast:** Selected candidates are amplified and distributed to all specialist modules

**AMOS relevance:** MANAR provides the engineering template for the workspace's attention selection mechanism. It demonstrates that GWT-style competitive broadcast can be implemented efficiently.

### 3.3 Global Workspace Agents (GWA) (2026)

GWA provides the multi-agent coordination layer for the global workspace:

```text
┌─────────────────────────────────────────────────────────────────┐
│                    GLOBAL WORKSPACE AGENTS                      │
│                                                                 │
│  • Broadcast hub + heterogeneous agent swarm architecture       │
│  • Entropy-based intrinsic drive for exploration                 │
│  • Agents bid for broadcast bandwidth                           │
│  • Hub selects and amplifies winning signals                    │
│  • Selected signals broadcast to all agents simultaneously      │
└─────────────────────────────────────────────────────────────────┘
```

**Key properties:**
- **Hub-spoke topology:** Central broadcast hub mediates between heterogeneous specialist agents
- **Entropy-driven:** Intrinsic motivation to explore novel information (high entropy = high bid priority)
- **Competitive bidding:** Agents submit candidates; hub selects via competition
- **Simultaneous broadcast:** Winning signal is delivered to all agents at once

**AMOS relevance:** GWA provides the agent-swarm architecture that maps directly to AMOS's specialist modules (NBI, NEI, SI, BEI, Memory, Prediction) bidding for workspace access.

### 3.4 MIRROR: Converging Cognitive Principles (2025)

MIRROR provides the memory integration architecture that the workspace feeds:

```text
┌─────────────────────────────────────────────────────────────────┐
│                    MIRROR ARCHITECTURE                          │
│                                                                 │
│  • O(1) reconstruction vs O(n) accumulation                     │
│  • Converging cognitive principles from multiple fields         │
│  • Bidirectional workspace-memory interface                     │
│  • Reconstructive memory access (not replay)                    │
│  • Workspace state guides memory retrieval                     │
└─────────────────────────────────────────────────────────────────┘
```

**Key properties:**
- **O(1) reconstruction:** Memory access reconstructs from compressed representations, not sequential replay
- **Converging principles:** Unifies findings from neuroscience, cognitive psychology, and ML
- **Bidirectional:** Workspace → Memory (encoding); Memory → Workspace (retrieval)

**AMOS relevance:** MIRROR provides the memory interface that the Global Workspace uses to populate its state from long-term storage and encode workspace snapshots for consolidation.

________________________________________________________________________

## 4. Workspace Architecture

### 4.1 Broadcast Mechanism

The workspace operates as a **competitive-collaborative broadcast hub**:

```text
SPECIALIST MODULES (L9-L29)
        |
        v
┌───────────────────────────────────────┐
│          SELECTION STAGE              │
│                                       │
│  1. Each module submits a candidate   │
│     representation (bid)              │
│  2. Selection scoring:                │
│     S(s) = w_a·A(s) + w_g·G(s)      │
│           + w_e·E(s) + w_n·N(s)      │
│     where:                            │
│       A = salience/attention score    │
│       G = goal relevance              │
│       E = entropy/novelty             │
│       N = recency decay               │
│  3. Top-K candidates selected         │
│     (K ≈ 4-7, matching J-space cap)  │
└───────────────────────────────────────┘
        |
        v
┌───────────────────────────────────────┐
│          WORKSPACE STATE              │
│                                       │
│  • Active representation buffer       │
│  • Capacity: ~tens of concepts        │
│  • Persistence: transient (ticks)     │
│  • Ignition threshold: θ_ignite       │
│  • Context vector: w_ignite           │
└───────────────────────────────────────┘
        |
        v
┌───────────────────────────────────────┐
│          BROADCAST STAGE              │
│                                       │
│  1. Ignition check:                   │
│     if max_k S(s_k) ≥ θ_ignite:      │
│       w_broadcast = Σ α_k·V·s_k      │
│     else:                             │
│       no broadcast (subthreshold)     │
│  2. Broadcast to ALL specialist mods  │
│  3. Each module updates its priors:   │
│     m_k' = LayerNorm(m_k             │
│            + γ·B_k·w_broadcast)      │
└───────────────────────────────────────┘
        |
        v
SPECIALIST MODULES (updated priors)
```

### 4.2 Selection Criteria

The scoring function `S(s)` weights four factors:

```text
S(s) = w_a · A(s)      # Attention salience (from L2)
      + w_e · E(s)      # Entropy/novelty (from GWA intrinsic drive)
      + w_g · G(s)      # Goal relevance (from L15)
      + w_n · N(s)      # Recency (temporal decay from last broadcast)
```

**Default weights** (tuned per operational mode):

| Factor | Weight | Source       | Purpose                          |
| ------ | ------ | ------------ | -------------------------------- |
| `w_a`  | 0.35   | L2 Attention | Saliency from attention engine   |
| `w_e`  | 0.30   | GWA          | Entropy-driven exploration       |
| `w_g`  | 0.25   | L15 Goals    | Goal relevance                   |
| `w_n`  | 0.10   | L7 Memory    | Recency/frequency decay          |

### 4.3 Ignition Threshold

The ignition threshold $\theta_{\text{ignite}}$ determines whether a workspace broadcast occurs:

```text
θ_ignite = θ_base + β · load_factor
```

Where:
- `θ_base` = 0.6 (baseline; tuned empirically)
- `load_factor` = current cognitive load (0–1 scale from L24 Self-Regulation)
- `β` = 0.2 (load sensitivity)

**Behavior:** Under high cognitive load, the threshold rises, requiring stronger candidates for broadcast. Under low load, more candidates can ignite, enabling exploration.

### 4.4 Capacity Governance

The workspace capacity is governed by L24 Self-Regulation and the Homeostasis Engine:

```text
┌─────────────────────────────────────────────────────────┐
│              CAPACITY GOVERNANCE                        │
│                                                         │
│  Max concepts in workspace: K_max ≈ 7                  │
│  Max tokens per concept: T_max ≈ 256                   │
│  Total workspace budget: W = K_max × T_max ≈ 1,792    │
│                                                         │
│  Load shedding triggers:                               │
│  • Load > 0.9: drop lowest-priority concepts           │
│  • Load > 0.95: freeze new inputs, process backlog     │
│  • Load = 1.0: emergency workspace reset               │
└─────────────────────────────────────────────────────────┘
```

________________________________________________________________________

## 5. Workspace Dynamics

### 5.1 Cognitive Cycle

The workspace operates in a **persistent recurrent cognitive cycle** — distinct from a single forward pass:

```text
┌─────────────────────────────────────────────────────────┐
│              COGNITIVE CYCLE (per tick)                  │
│                                                         │
│  1. COLLECT  — Gather bids from all specialist modules  │
│  2. SELECT   — Score candidates via S(s)                │
│  3. IGNITE   — Check ignition threshold                 │
│  4. BROADCAST— Amplify and distribute winning signals   │
│  5. UPDATE   — Each module integrates broadcast         │
│  6. RETRIEVE — Populate from L7 Memory (MIRROR O(1))   │
│  7. ENCODE   — Snapshot working state for L7 Memory     │
│  8. REAPPLY  — Return to step 1                        │
└─────────────────────────────────────────────────────────┘
```

**Cycle frequency:** Adaptive, governed by L24 Self-Regulation. Normal: ~10-50 Hz equivalent. Under cognitive load: reduced frequency to prevent resource exhaustion.

### 5.2 Broadcast-Feedback Loop

Broadcasts create a feedback loop that drives cognitive dynamics:

```text
Broadcast w_broadcast
    → Specialist modules update: m_k' = LayerNorm(m_k + γ·B_k·w_broadcast)
    → Updated modules generate new bids
    → New bids compete in next cycle
    → Creates temporal coherence across cognitive operations
```

This recurrence is what distinguishes AMOS from single-pass Transformer inference. Each broadcast cycle creates a new "moment of consciousness" that integrates the latest state of all modules.

### 5.3 Subthreshold Processing

When no candidate exceeds $\theta_{\text{ignite}}$, the workspace does not broadcast. This represents **subconscious local processing** — each module operates independently without global coordination:

```text
if max_k S(s_k) < θ_ignite:
    # No broadcast — modules process locally
    for each module k:
        m_k' = local_update(m_k)  # No global signal
    # Cognitive cycle still runs, but without integration
```

This is computationally efficient and biologically plausible (most neural processing is local).

________________________________________________________________________

## 6. AMOS-Specific Extensions

### 6.1 Persistent Recurrent Cognitive Cycles vs Single Forward Pass

**Critical distinction:** Standard LLMs execute a single forward pass per prompt. AMOS operates in persistent recurrent cycles:

```text
LLM PARADIGM:
  Input -> Single Forward Pass -> Output
  (No persistent state between invocations)

AMOS GW PARADIGM:
  Loop forever:
    Collect bids -> Select -> Ignite -> Broadcast -> Update -> Retrieve -> Encode
    (Persistent workspace state across cycles; modules maintain inter-cycle state)
```

This creates several AMOS-specific requirements:

1. **Workspace state persistence:** The workspace buffer persists across cycles, accumulating context
2. **Module state persistence:** Each specialist module maintains its own state across cycles
3. **Inter-cycle memory:** Workspace snapshots are encoded into L7 Memory for cross-cycle continuity
4. **Budget management:** Unlike a single pass, recurrent cycles must manage computational budgets over time

### 6.2 Module Heterogeneity

AMOS's specialist modules are heterogeneous in nature, unlike homogeneous Transformer attention heads:

```text
┌──────────────────────────────────────────────────────────────────┐
│                SPECIALIST MODULE BIDDERS                         │
│                                                                  │
│  COGNITIVE MODULES:                                              │
│  • L9  Inference (CORE-19 reasoning kernel)                      │
│  • L10 World Modeling (Atlas/JEPA/Cosmos)                        │
│  • L11 Causal Modeling (Pearl do-calculus)                        │
│  • L13 Prediction (forward simulation)                           │
│  • L12 Counterfactual Simulation                                 │
│                                                                  │
│  AFFECTIVE MODULES:                                              │
│  • Emotion Engine (valence/arousal/safety)                       │
│  • Instinct Engine (approach/avoid/conserve)                     │
│  • Intuition Engine (associative pattern matching)               │
│                                                                  │
│  MEMORY MODULES:                                                 │
│  • L7 Memory retrieval (MIRROR O(1) reconstruction)             │
│  • L22 Consolidation (offline integration)                       │
│                                                                  │
│  IDENTITY MODULES:                                               │
│  • L25 Identity/Continuity (self-model)                          │
│  • L23 Metacognition (reasoning audit)                           │
│                                                                  │
│  EXECUTION MODULES:                                              │
│  • L16 Planning (action construction)                            │
│  • L17 Decision (commitment filtering)                           │
│  • L28 Governance (authority enforcement)                        │
└──────────────────────────────────────────────────────────────────┘
```

Each module has a **bid signature** that encodes its contribution type, confidence, and relevance.

### 6.3 Entropy-Driven Intrinsic Motivation

Adapted from GWA's entropy-based intrinsic drive, the workspace actively seeks novel, high-information-content representations:

```text
E(s) = -Σ p(s_i) log p(s_i)  # Information entropy of candidate

# High entropy = candidate is surprising / novel / high-information
# This biases the workspace toward exploration, not just saliency
```

This prevents the workspace from being dominated by repetitive, low-information signals and ensures that surprising events (from L19 Outcome Observation, L1 Sensing) get broadcast attention.

### 6.4 Epistemic Safety Firewalls

The workspace inherits AMOS's epistemic safety requirements:

```text
┌─────────────────────────────────────────────────────────────────┐
│           EPISTEMIC SAFETY IN GLOBAL WORKSPACE                  │
│                                                                 │
│  • Workspace state is RSCF-typed (OBSERVATION / MODEL / DERIVED│
│    / SOURCE_CLAIM / UNKNOWN/GAP)                                │
│  • Broadcasts carry epistemic provenance                        │
│  • Module integrations preserve confidence ceilings:            │
│    C_conclusion ≤ min(C_premise_i)                             │
│  • PROPOSAL != COMMIT — workspace outputs are proposals        │
│  • C2 Metacognitive plane monitors workspace quality            │
│  • C1 Governance plane gates workspace-derived actions          │
└─────────────────────────────────────────────────────────────────┘
```

________________________________________________________________________

## 7. Integration with the 30-Layer Stack

### 7.1 Workspace as the L6 Hub

```text
     L0 Reality
          |
     L1 Sensing
          |
     L2 Attention ───────────────┐
          |                      |
     L3 Percept Formation        |
          |                      |
     L4 Object/Entity ──────────-|
          |                      |
     L5 Binding ────────────────-|
          |                      |
          v                      v
   ┌──────────────────────────────────────┐
   │        L6 GLOBAL WORKSPACE           │
   │  ┌─────────────────────────────────┐ │
   │  │ Selection → State → Broadcast   │ │
   │  └─────────────────────────────────┘ │
   └──────────────────────────────────────┘
          |         |          |
          v         v          v
     L7 Memory   L9 Inference  L10-L29
     (MIRROR)    (CORE-19)     (all higher)
```

### 7.2 Cross-Layer Interactions

| From Layer | To Workspace | Interaction Type            |
| ---------- | ------------ | --------------------------- |
| L1         | → bid        | Novelty/surprise signal     |
| L2         | → scoring    | Attention salience weights  |
| L4/L5      | → bid        | Entity/binding updates      |
| L7         | → populate   | MIRROR O(1) retrieval       |
| L9         | → bid        | Inference conclusions       |
| L10        | → bid        | World model updates         |
| L13        | → bid        | Predictions                 |
| L15        | → scoring    | Goal relevance weights      |
| L23        | → scoring    | Metacognitive confidence    |
| L24        | → capacity   | Resource budgets            |
| Workspace  | → L7         | Snapshot encoding           |
| Workspace  | → all L9-L29 | Broadcast distribution      |

________________________________________________________________________

## 8. MIRROR Integration: O(1) Reconstruction

### 8.1 The Problem with O(n) Accumulation

Standard memory systems accumulate information over time, leading to:
- Linear growth in retrieval cost
- Information overload in the workspace
- Difficulty distinguishing relevant from irrelevant history

### 8.2 MIRROR's O(1) Solution

MIRROR compresses experience into a reconstructive representation that allows constant-time access:

```text
STANDARD MEMORY (O(n) accumulation):
  Store all observations -> Search through all -> Retrieve relevant subset
  Cost: O(n) per retrieval

MIRROR (O(1) reconstruction):
  Compress experience into latent structure -> Reconstruct from compressed state
  Cost: O(1) per reconstruction
```

**Integration with Global Workspace:**

```text
CYCLE STEP 6 (RETRIEVE):
  Workspace state: w_t
  Compressed memory index: M_comp (updated continuously)
  Reconstruction: memory_trace = reconstruct(M_comp, w_t.query)
  Cost: O(1) — direct index lookup + latent reconstruction

CYCLE STEP 7 (ENCODE):
  Workspace snapshot: w_t
  Compression: M_comp' = compress(M_comp, w_t)
  Cost: O(1) — single compression pass
```

### 8.3 Converging Cognitive Principles

MIRROR unifies three cognitive science findings:
1. **Constructive retrieval:** Memories are reconstructed, not replayed (Bartlett, 1932; Schacter, 2012)
2. **Compression-expansion:** Long-term memory compresses; working memory expands (Cowan, 2000)
3. **Bidirectional influence:** Current context shapes memory retrieval; memory shapes current processing

________________________________________________________________________

## 9. Workspace States

The workspace transitions through defined states:

```text
┌─────────────────────────────────────────────────────────────┐
│                  WORKSPACE STATE MACHINE                     │
│                                                              │
│  IDLE ──────→ COLLECTING ──────→ SELECTING ──────→ IGNITED  │
│    ^              |                    |                 |    │
│    |              v                    v                 v    │
│    │         SUBTHRESHOLD         DORMANT          BROADCASTING│
│    |              |                    |                 |    │
│    └──────────────┴────────────────────┴─────────────────┘    │
│                                                              │
│  SPECIAL STATES:                                             │
│  • OVERLOADED: load > 0.95, emergency shedding               │
│  • FROZEN: C2 Metacognitive stop signal                      │
│  • RESET: emergency clear and reinitialize                    │
└─────────────────────────────────────────────────────────────┘
```

| State         | Description                                                  |
| ------------- | ------------------------------------------------------------ |
| IDLE          | No active processing; waiting for bids                       |
| COLLECTING    | Gathering bids from specialist modules                       |
| SELECTING     | Scoring candidates via S(s)                                  |
| IGNITED       | Top candidate exceeds θ_ignite; broadcast imminent           |
| BROADCASTING  | Active broadcast to all modules; update phase                |
| SUBTHRESHOLD  | No candidate exceeds threshold; local processing continues  |
| DORMANT       | Workspace temporarily suspended (resource conservation)      |
| OVERLOADED    | Cognitive load critical; emergency shedding active           |
| FROZEN        | C2 Metacognitive engine has halted workspace (audit)         |
| RESET         | Emergency clear; all workspace state discarded               |

________________________________________________________________________

## 10. Relationship to Existing AMOS Components

### 10.1 Super Consciousness Engine

The [[05_COGNITIVE_ORGANISM/SUPER_CONSCIOUSNESS_ENGINE|SUPER_CONSCIOUSNESS_ENGINE]] already implements GWT-inspired competitive attention and ignition:

```text
SUPER_CONSCIOUSNESS_ENGINE GWT:
  - Competitive attention with α_k scoring
  - Ignition threshold θ_ignite
  - Broadcast w_ignite with contextual reset
  - Module update via LayerNorm(m_k + γ·B_k·w_ignite)

GLOBAL WORKSPACE IMPLEMENTATION (this spec):
  - Extends with J-space capacity constraints (~tens of concepts)
  - Extends with MANAR O(n) scaling
  - Extends with GWA entropy-driven intrinsic motivation
  - Extends with MIRROR O(1) memory interface
  - Adds workspace state machine
  - Adds capacity governance (Homeostasis Engine integration)
```

The workspace implementation **subsumes and extends** the Super Consciousness Engine's GWT architecture.

### 10.2 Attention Engine

The [[05_COGNITIVE_ORGANISM/ATTENTION_ENGINE|ATTENTION_ENGINE]] provides the salience scoring that feeds into the workspace selection:

```text
ATTENTION ENGINE:
  A_p(s) = w_g·G_r(s) + w_c·C_q(s) + w_u·U(s) + w_i·I_r(s) + w_t·T_s(s) - w_d·D_k(s)

GLOBAL WORKSPACE (extends):
  S(s) = w_a·A_p(s) + w_e·E(s) + w_g·G(s) + w_n·N(s)
        ^^^^^^^^^^^
        Uses attention engine output as input
```

### 10.3 Memory Engine

The [[05_COGNITIVE_ORGANISM/MEMORY_ENGINE|MEMORY_ENGINE]] provides the 8-class memory partition that the workspace reads from and writes to:

```text
MEMORY ENGINE (8 classes):
  HOT/WARM/COLD/QUARANTINED/EXPIRED/RAW_ARCHIVE/EPISODIC/PROCEDURAL

GLOBAL WORKSPACE:
  - Reads: MIRROR O(1) reconstruction from consolidated memory
  - Writes: Workspace snapshots → EPISODIC memory (consolidation path)
  - Bidirectional: workspace state guides retrieval; retrieval populates workspace
```

### 10.4 Homeostasis Engine

The [[05_COGNITIVE_ORGANISM/HOMEOSTASIS_ENGINE|HOMEOSTASIS_ENGINE]] provides the 6-parameter health vector that governs workspace capacity:

```text
HOMEOSTASIS ENGINE:
  Health vector H = [CPU_load, memory_pressure, attention_saturation,
                     error_rate, provenance_confidence, latency]
  Stress ratio S = f(H)
  Load shedding: if S > threshold, reduce workspace capacity K_max

GLOBAL WORKSPACE:
  Uses H for:
    - θ_ignite adjustment (higher load → higher threshold)
    - K_max reduction (higher load → fewer concepts in workspace)
    - Emergency freeze (S > 0.95 → workspace frozen)
```

________________________________________________________________________

## 11. Performance Characteristics

### 11.1 Scaling

| Component          | Complexity | Notes                                  |
| ------------------ | ---------- | -------------------------------------- |
| Bid collection     | O(N)       | N = number of specialist modules       |
| Selection scoring  | O(K·N)     | K = candidates scored, N = features    |
| Ignition check     | O(1)       | Threshold comparison                   |
| Broadcast          | O(D·K)     | D = dimension, K = selected concepts   |
| Module update      | O(D·K)     | Per module; N modules → O(N·D·K)      |
| MIRROR retrieval   | O(1)       | Compressed index lookup                |
| MIRROR encoding    | O(1)       | Single compression pass                |
| **Total per cycle**| **O(N·D·K)**| Linear in modules and dimensions      |

### 11.2 Latency Budget

```text
Target cycle time: < 100ms (enables ~10 cognitive cycles per second)
Typical breakdown:
  Collect:  10ms
  Select:   20ms
  Ignite:    1ms
  Broadcast: 5ms
  Update:   40ms
  Retrieve:  2ms (MIRROR O(1))
  Encode:    2ms
  Overhead: 20ms
  TOTAL:   ~100ms
```

________________________________________________________________________

## 12. Open Questions and Gaps

| Gap ID | Description                            | Priority | Status     |
| ------ | -------------------------------------- | -------- | ---------- |
| GW-001 | Optimal θ_ignite calibration           | HIGH     | TBD        |
| GW-002 | Module bid protocol formalization      | HIGH     | TBD        |
| GW-003 | Workspace-to-memory MIRROR integration | HIGH     | SPECIFIED  |
| GW-004 | Multi-workspace partitioning (parallel)| MEDIUM   | TBD        |
| GW-005 | Workspace security (adversarial bids)  | HIGH     | TBD        |
| GW-006 | Cross-workspace communication protocol | LOW      | TBD        |
| GW-007 | Workspace degradation modes            | MEDIUM   | TBD        |
| GW-008 | Empirical θ_ignite tuning methodology  | HIGH     | TBD        |
| GW-009 | Entropy weight w_e calibration         | MEDIUM   | TBD        |
| GW-010 | Workspace audit trail format           | HIGH     | TBD        |

________________________________________________________________________

## 13. Implementation Roadmap

```text
Phase 1: CORE WORKSPACE (Priority: CRITICAL)
  [ ] Define workspace state data structures
  [ ] Implement selection scoring S(s)
  [ ] Implement ignition threshold logic
  [ ] Implement basic broadcast mechanism
  [ ] Integrate with Attention Engine (L2)
  [ ] Unit tests for workspace state machine

Phase 2: MEMORY INTEGRATION (Priority: HIGH)
  [ ] MIRROR O(1) reconstruction interface
  [ ] Workspace snapshot encoding to L7 Memory
  [ ] Bidirectional workspace-memory protocol
  [ ] Integration with Memory Engine (L7)

Phase 3: MODULE INTEGRATION (Priority: HIGH)
  [ ] Formalize bid protocol for all specialist modules
  [ ] Implement module update broadcasting
  [ ] Integration with Super Consciousness Engine
  [ ] Integration with Super Mind Engine

Phase 4: GOVERNANCE (Priority: HIGH)
  [ ] Capacity governance (Homeostasis Engine)
  [ ] Epistemic safety firewalls (C1/C2)
  [ ] Workspace audit trail
  [ ] Adversarial bid filtering

Phase 5: ADVANCED FEATURES (Priority: MEDIUM)
  [ ] Entropy-driven intrinsic motivation (GWA)
  [ ] Adaptive weight tuning (w_a, w_e, w_g, w_n)
  [ ] Multi-workspace partitioning
  [ ] Workspace degradation modes
```

________________________________________________________________________

## 14. Key Invariants

```text
GW-INV-01: Workspace capacity K ≤ K_max at all times
GW-INV-02: Every broadcast carries epistemic provenance (RSCF type)
GW-INV-03: Confidence ceiling preserved: C_output ≤ min(C_input_i)
GW-INV-04: PROPOSAL != COMMIT — workspace outputs are not actions
GW-INV-05: Workspace state is transient; persistence via L7 Memory only
GW-INV-06: Emergency freeze halts all broadcasts; modules continue local processing
GW-INV-07: All bids are validated before selection (C8 Execution plane)
GW-INV-08: Workspace does not self-modify; evolution via L29 only
```

________________________________________________________________________

## 15. Related Artifacts

- [[05_COGNITIVE_ORGANISM/COGNITIVE_STACK_30_LAYER_SPECIFICATION|COGNITIVE_STACK_30_LAYER_SPECIFICATION]] — The 30-layer stack that L6 belongs to.
- [[05_COGNITIVE_ORGANISM/SUPER_CONSCIOUSNESS_ENGINE|SUPER_CONSCIOUSNESS_ENGINE]] — GWT ignition architecture this extends.
- [[05_COGNITIVE_ORGANISM/SUPER_MIND_ENGINE|SUPER_MIND_ENGINE]] — Metacognitive monitoring of workspace.
- [[05_COGNITIVE_ORGANISM/ATTENTION_ENGINE|ATTENTION_ENGINE]] — Attention salience feeding workspace selection.
- [[05_COGNITIVE_ORGANISM/MEMORY_ENGINE|MEMORY_ENGINE]] — Memory partition the workspace reads/writes.
- [[05_COGNITIVE_ORGANISM/HOMEOSTASIS_ENGINE|HOMEOSTASIS_ENGINE]] — Health vector governing workspace capacity.
- [[05_COGNITIVE_ORGANISM/COGNITION_ENGINE|COGNITION_ENGINE]] — Reasoning modules that bid for workspace.
- [[05_COGNITIVE_ORGANISM/COGNITIVE_ORGANISM_README|COGNITIVE_ORGANISM_README]] — Organism architecture overview.
- [[25_COGNITIVE_MATRIX/AMOS_COGNITIVE_ARCHITECTURE_MATRIX|AMOS_COGNITIVE_ARCHITECTURE_MATRIX]] — Matrix this contributes to.

________________________________________________________________________

```yaml
conclusion:
  class: DERIVED
  supported:
    - J-space (Anthropic 2026) provides empirical evidence for emergent global workspace
    - MANAR (2026) provides O(n) engineering template for workspace attention
    - GWA (2026) provides hub-spoke agent coordination architecture
    - MIRROR (2025) provides O(1) reconstruction for workspace-memory interface
    - These four findings converge on a single workspace architecture
    - AMOS-specific extension: persistent recurrent cycles vs single forward pass
    - Workspace occupies L6 as the central bottleneck of the 30-layer stack
  not_established:
    - Runtime implementation exists
    - θ_ignite has been empirically calibrated
    - Module bid protocol is finalized
    - Workspace produces consciousness or sentience
  unresolved:
    - Optimal workspace parameters (θ_ignite, weights, K_max)
    - Multi-workspace partitioning strategy
    - Adversarial robustness of bid validation
    - Empirical comparison with standard Transformer attention
```

________________________________________________________________________

```RSCF-NODE
node_id: GLOBAL_WORKSPACE_IMPLEMENTATION
node_type: specification
domain: AMOS_SPEC
path: 05_COGNITIVE_ORGANISM/GLOBAL_WORKSPACE_IMPLEMENTATION.md
RSCF-RELATIONS:
  - SPECIFIES: L6_Working_State
  - EXTENDS: SUPER_CONSCIOUSNESS_ENGINE_GWT
  - INTEGRATES: MANAR_2026, J_space_2026, GWA_2026, MIRROR_2025
  - INTERFACES_WITH: ATTENTION_ENGINE, MEMORY_ENGINE, HOMEOSTASIS_ENGINE
  - PART_OF: COGNITIVE_STACK_30_LAYER_SPECIFICATION
  - RELATED_TO: COGNITION_ENGINE, SUPER_MIND_ENGINE
claim_class: AMOS_MODEL
```

________________________________________________________________________

**MOC:** [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]]
