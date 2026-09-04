---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 05 Cognitive Organism Readme
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

# 05 Cognitive Organism — Full Brain MECE Architecture Specification

> [!ABSTRACT] Role in AMOS Full Brain OS
> **Plane:** `05_COGNITIVE_ORGANISM` (Group C: Cognitive Capability & Orchestration).
> **Structural Role:** Assembles and coordinates the multi-layer cognitive organism above raw kernels (`02_KERNEL`) and below autonomous task agents (`06_AGENTS`).
> Instantiates the **Five Full-Brain Peers** (`B_core`, `K_omni`, `B_omniverse`, `P_personality`, `T_expression`) and unifies the **30 Cognitive Primitives (L00–L29)** into an integrated, closed-loop reasoning organism.

---

## 1. Five-Peer MECE Full Brain Architecture

In strict adherence to the Full Brain OS Master Canon, organismic cognition is partitioned across five peers with disjoint responsibilities:

```
                      ┌────────────────────────────┐
                      │    G_gap (Cross-Cutting)   │
                      │   Zero-Gap Management Bus  │
                      └─────────────┬──────────────┘
                                    │
    ┌───────────────────────────────┼──────────────────────────────┐
    ▼                               ▼                              ▼
┌───────────────┐           ┌───────────────┐              ┌───────────────┐
│    B_core     │           │    K_omni     │              │  B_omniverse  │
│ Core Cognitive│ ◄───────► │ Substrate     │ ◄──────────► │ World & System│
│ Processing    │           │ Knowledge/QEC │              │ Possibility   │
└───────┬───────┘           └───────────────┘              └───────┬───────┘
        │                           ▲                              │
        ▼                           │                              ▼
┌───────────────┐                   │                      ┌───────────────┐
│ P_personality │ ──────────────────┴────────────────────► │ T_expression  │
│ Affective &   │                                          │ BCI, Language │
│ Homeostatic   │                                          │ & Multimodal  │
└───────────────┘                                          └───────────────┘
```

| Full-Brain Peer | Architectural Identity | Primary Functional Ownership | Explicit Non-Ownership (Firewalls) |
| :--- | :--- | :--- | :--- |
| **`B_core`** | Brain Core | Working memory, hypothesis generation, deduction, active inference, decision orchestration. | Physical tool execution, deployment authority, external effects. |
| **`K_omni`** | Omni-Kernel Substrate | Reusable reasoning, formal epistemic access, quantum-classical algebras, invariant verification. | Dynamic runtime session state, arbitrary external policy changes. |
| **`B_omniverse`** | Omniverse Brain | Multi-scale world modeling, counterfactual simulation, cross-domain possibility exploration. | Empirical truth assertions without external sensor grounding. |
| **`P_personality`** | Persona & Homeostasis | Affective conditioning, somatic state tracking, ethical heuristics, homeostatic drive balance. | Root system authority, biological claim inflation. |
| **`T_expression`** | Expression & Translation | Bidirectional BCI neural signal decoding, natural language generation, structural API translation. | Domain reasoning ownership, unverified claim emission. |
| **`G_gap`** | Gap Governor | Cross-cutting detection of missing dependencies, uncalibrated models, and unresolved references. | Not a sixth peer; acts as a non-authoritarian inspection firewall. |

---

## 2. The 30 Cognitive Primitives (L00–L29) Mapping

The cognitive organism operationalizes the complete MECE primitive spectrum defined in [25_COGNITIVE_MATRIX/AMOS_COGNITIVE_ARCHITECTURE_MATRIX.md](file:///Users/mac/Documents/AMOS_OS/25_COGNITIVE_MATRIX/AMOS_COGNITIVE_ARCHITECTURE_MATRIX.md):

| Layer Range | Functional Cluster | Cognitive Primitives Included | Primary Managing Engine / Node |
| :--- | :--- | :--- | :--- |
| **L00 – L03** | **Sensory & Working State** | L00 Ground Truth, L01 Perception, L02 Attention, L03 Working Memory | [[05_COGNITIVE_ORGANISM/PERCEPTION_ENGINE|PERCEPTION_ENGINE]] & [[05_COGNITIVE_ORGANISM/ATTENTION_ENGINE|ATTENTION_ENGINE]] |
| **L04 – L06** | **Memory Triad** | L04 Episodic Memory, L05 Semantic Memory, L06 Procedural Memory | [[05_COGNITIVE_ORGANISM/MEMORY_ENGINE|MEMORY_ENGINE]] (Sparse Distributed Memory & Dense Attractors) |
| **L07 – L12** | **Core Reasoning & Action** | L07 Abstraction, L08 Concept Formation, L09 Reasoning, L10 Inference, L11 Planning, L12 Decision Making | [[05_COGNITIVE_ORGANISM/COGNITION_ENGINE|COGNITION_ENGINE]] & [[05_COGNITIVE_ORGANISM/PREDICTION_ENGINE|PREDICTION_ENGINE]] |
| **L13 – L16** | **Metacognitive Executive** | L13 Metacognition, L14 Uncertainty, L15 Self-Correction, L16 Goal Alignment | [[05_COGNITIVE_ORGANISM/METACOGNITIVE_ENGINE|METACOGNITIVE_ENGINE]] & [[05_COGNITIVE_ORGANISM/REPAIR_ENGINE|REPAIR_ENGINE]] |
| **L17 – L19** | **Affective & Homeostatic Drive** | L17 Emotion Regulation, L18 Somatic Integration, L19 Homeostasis | [[05_COGNITIVE_ORGANISM/EMOTION_ENGINE|EMOTION_ENGINE]] & [[05_COGNITIVE_ORGANISM/HOMEOSTASIS_ENGINE|HOMEOSTASIS_ENGINE]] |
| **L20 – L21** | **Transduction & Expression** | L20 Language Translation, L21 Multimodal / BCI Expression | [[15_INTERFACES/BCI_EXPRESSION_GATEWAY_ADAPTER|BCI Gateway]] & [[21_DOMAINS/14_C04_BIO_NEURO/C04_NEURAL_DECODING_AND_BCI_ARCHITECTURE|C04 BCI]] |
| **L22 – L24** | **Social & Moral Intelligence** | L22 Social Cognition, L23 Theory of Mind, L24 Moral Reasoning | [[05_COGNITIVE_ORGANISM/SUPER_MIND_ENGINE|SUPER_MIND_ENGINE]] & [[21_DOMAINS/16_C06_SOCIETY_CULTURE/16_C06_SOCIETY_CULTURE_MOC|C06 Society]] |
| **L25 – L27** | **Generative World Simulation** | L25 Creative Synthesis, L26 Intuitive Heuristics, L27 Counterfactual Simulation | [[05_COGNITIVE_ORGANISM/WORLD_MODEL_ENGINE|WORLD_MODEL_ENGINE]] & [[05_COGNITIVE_ORGANISM/INTUITION_ENGINE|INTUITION_ENGINE]] |
| **L28 – L29** | **Epistemic Invariants & Selfhood** | L28 Epistemic Humility, L29 Selfhood Continuity | [[05_COGNITIVE_ORGANISM/IDENTITY_ENGINE|IDENTITY_ENGINE]] & [[05_COGNITIVE_ORGANISM/SUPER_CONSCIOUSNESS_ENGINE|SUPER_CONSCIOUSNESS_ENGINE]] |

---

## 3. Real-Time Call Lifecycle & Runtime Binding

When an external signal or internal goal enters the cognitive organism, it transitions through a formal 12-stage lifecycle governed by [05_COGNITIVE_ORGANISM/FULL_BRAIN_OS_RUNTIME_BINDING.md](file:///Users/mac/Documents/AMOS_OS/05_COGNITIVE_ORGANISM/FULL_BRAIN_OS_RUNTIME_BINDING.md):

```text
1. SIGNAL INGESTION (Sensory / BCI / Message)
   └── Type-checked at T_expression / BCI Gateway
2. PEER ROUTING & ATTENTION ALLOCATION
   └── B_core activates relevant primitives (L01-L03) via Attention Engine
3. MEMORY & PRIOR RETRIEVAL
   └── K_omni / Memory Engine extracts episodic and semantic attractors (L04-L06)
4. GENERATIVE SIMULATION & INFERENCE
   └── B_omniverse simulates counterfactual branches (L25-L27)
5. REASONING & PROPOSAL FORMATION
   └── B_core synthesizes candidate action / claim (L07-L12)
6. AFFECTIVE & HOMEOSTATIC FILTER
   └── P_personality evaluates risk, ethics, and homeostasis constraints (L17-L19)
7. METACOGNITIVE UNCERTAINTY ATTACHMENT
   └── Metacognitive Engine attaches confidence ceiling and falsifiers (L13-L15)
8. G_GAP INTEGRITY AUDIT
   └── Verifies absence of load-bearing UNKNOWN/GAP states
9. RUNTIME ADMISSION GATE
   └── Evaluated by 03_CONTROL_PLANE policy and authority contracts
10. TOOL / EFFECTOR EXECUTION
    └── Executed strictly through 14_TOOLS if authorized
11. SENSORY FEEDBACK OBSERVATION
    └── Compares observed result with predictive priors (Free Energy calculation)
12. MEMORY COMMIT & POST-ACTION REPAIR
    └── Updates state in 10_MEMORY and 12_STATE; engages Repair Engine upon surprise
```

---

## 4. Hard Cognitive Invariants

1. **`BRAIN != RUNTIME != CONTROL`**: The cognitive organism reasons, simulates, and proposes; it cannot directly commit external effects without passing through the Control Plane and Runtime security gates.
2. **`CAPABILITY != AUTHORITY`**: Demonstrating high decoding accuracy or sophisticated reasoning capacity does not confer administrative authority to bypass user confirmation.
3. **`MODEL != OBSERVATION`**: Predicted states generated by internal world models remain hypotheses (`AMOS_MODEL`) until confirmed by external sensor feedback (`OBSERVATION`).
4. **`HOMEOSTATIC_FAIL_SAFE`**: If energy expenditure or surprise metric $S = -\ln p(o)$ exceeds critical bounds, the organism downregulates exploratory degrees of freedom into safe conservative operation.

---

## 5. Navigation & Architectural Cross-References

* **Authoritative Specification:** [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]]
* **Subsystem Contracts:** [[05_COGNITIVE_ORGANISM/COGNITIVE_ORGANISM_COGNITIVE_ORGANISM_CONTRACT|COGNITIVE_ORGANISM_CONTRACT]]
* **Runtime Handshake:** [[05_COGNITIVE_ORGANISM/FULL_BRAIN_OS_RUNTIME_BINDING|FULL_BRAIN_OS_RUNTIME_BINDING]]
* **Neural Substrate:** [[21_DOMAINS/14_C04_BIO_NEURO/C04_NEURAL_DECODING_AND_BCI_ARCHITECTURE|C04 BCI Architecture]]
* **Matrix Crosswalk:** [[25_COGNITIVE_MATRIX/AMOS_COGNITIVE_ARCHITECTURE_MATRIX|AMOS Cognitive Architecture Matrix]]

---
RSCF-NODE
node_id: 05_cognitive_organism_readme
node_type: plane_readme
domain: 05_COGNITIVE_ORGANISM
path: 05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_README.md
RSCF-RELATIONS:
  - IMPLEMENTS: [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE]]
  - INDEXED_BY: [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC]]
  - BOUND_TO: [[05_COGNITIVE_ORGANISM/FULL_BRAIN_OS_RUNTIME_BINDING]]
claim_class: AMOS_MODEL
