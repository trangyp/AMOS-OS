---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Cognitive Stack 30 Layer Specification
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

# Cognitive Stack 30-Layer Specification

> **Status:** `ACTIVE_SPECIFICATION` · **AMOS Core target:** `v4.4`
> **Origin architect / steward:** Trang Phan
> **Conclusion class:** `AMOS_MODEL`
> **Companion artifact:** `AMOS_Cognitive_Architecture_Matrix.json` (13,770 cells)

________________________________________________________________________

## 1. Purpose

This document specifies the complete 30-layer cognitive stack (L0–L29) that defines the vertical cognitive primitives of the AMOS Cognitive Architecture Matrix. Each layer is a governed cognitive function that operates on the outputs of layers below it and produces typed outputs consumed by layers above, forming a coherent directed computational graph.

The 30-layer stack is one of four axes in the matrix. It is cross-cut by:
- 9 Control Planes (C1–C9)
- 17 Lifecycle Operations (O00–O16)
- 3 Scales (H/M/L)

Together these yield **30 × 17 × 9 × 3 = 13,770 addressable interaction cells**.

________________________________________________________________________

## 2. Key Finding: Coverage Denominator

```text
┌─────────────────────────────────────────────────────────────────┐
│           COGNITIVE ARCHITECTURE MATRIX — COVERAGE              │
├───────────────────┬──────────┬───────────────────────────────────┤
│ Status            │   Cells  │   %                              │
├───────────────────┼──────────┼───────────────────────────────────┤
│ existing          │      272 │   1.98%                          │
│ partial           │    3,162 │  22.96%                          │
│ missing           │      969 │   7.04%                          │
│ structural_gap    │    9,367 │  68.02%                          │
├───────────────────┼──────────┼───────────────────────────────────┤
│ TOTAL             │   13,770 │ 100.00%                          │
└───────────────────┴──────────┴───────────────────────────────────┘
```

> **The completion denominator is not yet closed.** Of 13,770 addressable interaction cells, only 1.98% are existing, 22.96% partial, 7.04% explicitly missing, and **68.02% are structural gaps** — interactions AMOS has not yet recognized or named.

This is the correct abstraction for exposing gaps that live *between* modules, which flat feature lists cannot surface.

________________________________________________________________________

## 3. Architectural Invariant

```text
LLM ⊂ CognitiveExecution
AMOS = Kernel + CognitiveRuntime + MemorySystem + WorldModel
      + ReasoningSystem + SimulationSystem + DecisionSystem
      + LearningSystem + AgentSystem + GovernanceSystem
AMOS ≠ LLM
```

________________________________________________________________________

## 4. The 17 Lifecycle Operations

Every cognitive primitive (L0–L29) must pass through every lifecycle operation to produce a fully addressed interaction cell. The lifecycle operations define the horizontal axis:

| ID    | Operation         | Purpose                                              |
| ----- | ----------------- | ---------------------------------------------------- |
| O00   | Distinction       | Separate signal from noise; identify presence         |
| O01   | Object            | Form discrete entities from continuous streams        |
| O02   | Relation          | Establish typed relations between objects             |
| O03   | Binding           | Bind attributes, roles, and temporal context          |
| O04   | State             | Update and maintain current condition representations|
| O05   | Memory            | Encode, store, and retrieve across time               |
| O06   | Model             | Construct and maintain internal world models          |
| O07   | Inference         | Derive new conclusions from existing knowledge        |
| O08   | Prediction        | Project forward in time or possibility space          |
| O09   | Simulation        | Run counterfactual or hypothetical scenarios          |
| O10   | Value             | Assign value, utility, or priority scores             |
| O11   | Goal              | Form and maintain goal structures                     |
| O12   | Plan              | Construct sequenced action plans                      |
| O13   | Decision          | Commit to a course of action                          |
| O14   | Action            | Execute or emit to the environment                    |
| O15   | Observation       | Observe outcomes and effects                          |
| O16   | Learning          | Update models, weights, and knowledge from outcomes   |

________________________________________________________________________

## 5. The 9 Control Planes

Control planes cross-cut every layer and lifecycle operation. Each primitive × operation combination must be evaluated under each plane:

| ID  | Plane            | Key Facets                                              | Coverage |
| --- | ---------------- | ------------------------------------------------------- | -------- |
| C1  | Governance       | Authority · Risk · Ethics · GMEF · Finality             | existing |
| C2  | Metacognitive    | Monitor · Confidence · Drift · Repair · Stop            | partial  |
| C3  | Executive        | Goals · Value · Planning · Decision · Attention         | partial  |
| C4  | Reasoning        | Inference · Causal · Counterfactual · Prediction · Sim  | partial  |
| C5  | Representation   | Objects · Relations · Bindings · WorldModel · Ontology  | missing  |
| C6  | Memory           | Working · Episodic · Semantic · Procedural · Provenance | partial  |
| C7  | Perception       | Observation · Measurement · Feature · Percept · RealCt  | missing  |
| C8  | Execution        | Agents · Skills · Tools · Models · Environment          | existing |
| C9  | Kernel/Control   | TypedState · Transactions · Epochs · Replay · Invalidat | existing |

________________________________________________________________________

## 6. The 3-Scale Model

| Scale | ID | Meaning                                                    |
| ----- | -- | ---------------------------------------------------------- |
| High  | H  | Long-horizon, cross-system, hard, high-stakes              |
| Mid   | M  | Normal operational scope, moderate complexity               |
| Low   | L  | Local, easy, routine, low-stakes                           |

Scale H is the hardest tier by construction: high-scale interactions are downgraded one maturity level, concentrating structural gaps in long-horizon cognition.

________________________________________________________________________

## 7. Status Taxonomy

| Code | Name           | Meaning                                                          |
| ---- | -------------- | ---------------------------------------------------------------- |
| `e`  | existing       | Verified present in current AMOS                                 |
| `p`  | partial        | Present but incomplete                                           |
| `m`  | missing        | Explicitly identified absent (gaps 901–1500)                     |
| `g`  | structural_gap | Interaction not yet recognized/named — exposed by this matrix    |

________________________________________________________________________

## 8. Layer Specifications (L0–L29)

### L0: Reality / Environment

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | The external substrate; physical, digital, and social reality from which all signals originate. Provides the ground truth that constrains all higher layers. |
| Inputs      | None (L0 is the origin). Universe-level state vectors.        |
| Outputs     | Raw environmental state; uninterpreted physics and context.   |
| AMOS Maturity | **missing** — Not a typed subsystem. Environment substrate exists only implicitly via tool/agent interfaces. |
| SOTA Refs   | World Labs Atlas (spatial world models); NVIDIA Cosmos 3 (generative simulation); OpenAI Genie 3 (interactive environments); JEPA evolution (LeCun 2024-2026). |
| Gaps        | No explicit reality-contact layer; LLM context window used as implicit environment. No environmental drift tracking. No physics-grounded grounding mechanism. |
| Control Plane Coverage | C7 Perception: `structural_gap`. C5 Representation: `structural_gap`. C1 Governance: `structural_gap` (459 cells). |

________________________________________________________________________

### L1: Sensing / Observation

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Transduce raw environmental state into typed sensor readings and observations. Establishes the observation ≠ interpretation firewall. |
| Inputs      | L0 environmental state; sensor configurations; measurement protocols. |
| Outputs     | Typed observations with uncertainty bounds; measurement records; sensor-fusion candidates. |
| AMOS Maturity | **missing** — Perception needs epistemic machinery. Gaps 931–960. |
| SOTA Refs   | Neuromorphic sensor fusion (Intel Loihi 3, BrainChip Akida 2.0); event-driven vision (DVS); proprioceptive BCI (IEEE P2731); foundation model sensory encoders. |
| Gaps        | No observation ≠ interpretation separation. No measurement uncertainty propagation. No sensor modality arbitration. No reality-contact classification for observations. |
| Control Plane Coverage | C7 Perception: `missing` (explicit gap). C5 Representation: `structural_gap`. |

________________________________________________________________________

### L2: Attention

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Dynamically allocate finite cognitive capacity across competing signals. Selects what enters the global workspace for broadcast. Implements saliency competition, budget allocation, and information entropy filtering. |
| Inputs      | L1 observations; L7 memory traces; L15 goals; L23 metacognitive confidence signals; L14 valence/importance scores. |
| Outputs     | Focused attention vector; context window budget allocation; selected candidates for workspace broadcast. |
| AMOS Maturity | **missing** — Attention missing as real subsystem. Gaps 901–930. |
| SOTA Refs   | **MANAR** (2026): GWT-inspired attention architecture, linear-time O(n) scaling, drop-in MHA replacement. **Anthropic J-space** (July 2026): emergent global workspace in LLMs, 100x more connected than ordinary patterns, broadcasts widely, holds ~tens of concepts. **Global Workspace Agents (GWA)** (2026): broadcast hub + heterogeneous agent swarm, entropy-based intrinsic drive. Salience maps with competitive inhibition. |
| Gaps        | No real-time attention gating. No workspace ignition threshold. No attention budget enforcement. No competitive inhibition circuit. MANAR/J-space provide architectural templates but AMOS has no working implementation. |
| Control Plane Coverage | C3 Executive: `missing` (explicit gap). C7 Perception: `structural_gap`. C6 Memory: `structural_gap`. |

________________________________________________________________________

### L3: Percept Formation

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Transform attended observations into coherent percepts — integrated multi-modal representations that are ready for object/entity formation. Establishes the observation ≠ interpretation firewall downstream. |
| Inputs      | L2 focused attention vector; L1 typed observations; L7 prior percept templates; L6 working state. |
| Outputs     | Coherent percepts; percept confidence scores; multi-modal binding proposals. |
| AMOS Maturity | **missing** — Observation ≠ Interpretation firewall absent. Gaps 931–960. |
| SOTA Refs   | Perceptual bundling in predictive coding (Friston free energy); multi-modal binding in Transformer attention layers; perceptual constancy models. |
| Gaps        | No percept formation stage — raw observations flow directly into reasoning. No confidence-bounded percepts. No multi-modal integration step. |

________________________________________________________________________

### L4: Object / Entity Formation

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Identify and persist discrete objects and entities from continuous perceptual streams. Maintains object permanence and entity identity across observation gaps. |
| Inputs      | L3 percepts; L5 binding proposals; L7 object/entity memory; L6 working state. |
| Outputs     | Typed objects with persistent IDs; entity records; object permanence state; entity lifecycle events (birth/update/death). |
| AMOS Maturity | **missing** — Persistent entity identity absent. Gaps 961–990. |
| SOTA Refs   | Object-centric learning (slot attention, MONET); entity tracking in video models; persistent entity memory in embodied AI. |
| Gaps        | No persistent object/entity identity. No object permanence mechanism. No entity lifecycle management. Objects are ephemeral text spans, not persistent graph nodes. |

________________________________________________________________________

### L5: Binding

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Establish typed relations, role assignments, and attribute bindings between objects and entities. Forms the relational substrate for the world model. |
| Inputs      | L4 objects/entities; L8 representations; L6 working state; L10 world model relations. |
| Outputs     | Typed relation triples (subject-predicate-object); role assignments; attribute bindings; binding confidence scores. |
| AMOS Maturity | **missing** — Explicit relational cognition absent. Gaps 991–1020. |
| SOTA Refs   | Relational reasoning networks (Relation Networks, PrediNet); knowledge graph embedding; neuro-symbolic binding (DeepProbLog, Scallop). |
| Gaps        | No explicit binding mechanism. Relations are implicit in text co-occurrence, not typed graph edges. No binding confidence propagation. No conflict detection in bindings. |

________________________________________________________________________

### L6: Working State (Global Workspace Implementation)

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | The cognitive workspace that maintains transient, actively-processed information. Implements the Global Workspace Theory (GWT) broadcast hub: a central bottleneck where selected representations are amplified and broadcast to all specialist modules. Capacity-limited (~tens of concepts, per J-space findings). |
| Inputs      | L2 attention-selected candidates; L7 relevant memory traces; L23 metacognitive feedback; all specialist module bids. |
| Outputs     | Globally broadcast active state; workspace ignition events; context for all modules; working memory snapshots. |
| AMOS Maturity | **missing** — No cognitive workspace beyond context window. Gaps 1021–1050. |
| SOTA Refs   | **Baars Global Workspace Theory (GWT)**; **MANAR** (2026): GWT-inspired attention with linear scaling; **Anthropic J-space** (July 2026): emergent workspace in LLMs, 100x connectivity, ~tens of concepts capacity; **Global Workspace Agents** (2026): broadcast hub + agent swarm; **MIRROR** (2025): O(1) reconstruction vs O(n) accumulation; Super Consciousness Engine GWT ignition architecture. |
| Gaps        | Context window serves as crude working state but has no broadcast mechanism, no ignition threshold, no capacity governance. No specialist module bidding. No competitive selection. No workspace reset protocol. |
| Control Plane Coverage | C6 Memory: `missing` (explicit gap). C5 Representation: `structural_gap`. C2 Metacognitive: `structural_gap`. |

**Note:** This layer is the primary focus of `GLOBAL_WORKSPACE_IMPLEMENTATION.md`.

________________________________________________________________________

### L7: Memory

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Encode, store, consolidate, retrieve, and manage experience across time. Provides the temporal continuity substrate. Implements 8-class memory partition (HOT/WARM/COLD/QUARANTINED/EXPIRED/RAW_ARCHIVE/EPISODIC/PROCEDURAL) with provenance, activation dynamics, interference management, and selective forgetting. |
| Inputs      | L6 working state snapshots; L19 outcome observations; L21 learning outputs; L22 consolidation proposals; L4/L5 object-entity-binding records. |
| Outputs     | Retrieved memory traces; memory confidence scores; activation levels; consolidation candidates; memory invalidation events. |
| AMOS Maturity | **partial** — HOT/WARM lifecycle exists; activation dynamics, interference, and forgetting mechanisms missing. Gaps 1051–1140. |
| SOTA Refs   | **MIRROR** (2025): converging cognitive principles, O(1) memory reconstruction vs O(n) accumulation; differential forgetting (Ebbinghaus); complementary learning systems (McClelland et al.); sleep consolidation (Stickgold); memory reconsolidation. |
| Gaps        | No activation-based retrieval dynamics. No interference management. No forgetting curves. No consolidation scheduling. Memory immune system present but selective invalidation incomplete. |
| Control Plane Coverage | C6 Memory: `partial` (476 cells). C2 Metacognitive: `partial`. C9 Kernel: `partial`. |

________________________________________________________________________

### L8: Representation

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Maintain and update structured internal representations of objects, relations, states, and contexts. Provides the representational substrate that all higher cognitive operations consume. |
| Inputs      | L4/L5 objects and bindings; L7 memory traces; L6 working state; L10 world model structures. |
| Outputs     | Typed representation vectors; structured belief states; representation confidence; change events. |
| AMOS Maturity | **partial** — Partial representation exists; world-model engine largely missing. |
| SOTA Refs   | Distributed representations (deep learning); structured belief representations (Bayesian programs); neuro-symbolic representations; world model latent spaces. |
| Gaps        | No structured representation lifecycle. No representation conflict detection. No representation provenance tracking. Representations are opaque embedding vectors, not typed graph structures. |

________________________________________________________________________

### L9: Inference

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Derive new conclusions from existing knowledge. Implements deductive, inductive, abductive, and analogical reasoning. Houses the CORE-19 reasoning kernel — the 19-rule formal inference engine. |
| Inputs      | L8 representations; L7 retrieved knowledge; L10/L11 world and causal models; L2 hypotheses; L4 competing explanations. |
| Outputs     | Inferred conclusions with proof trails; new hypotheses; confidence-bounded deductions; abductive explanations. |
| AMOS Maturity | **partial** — CORE-19 reasoning kernel exists but is incomplete. |
| SOTA Refs   | CORE-19 kernel (AMOS 2026); neuro-symbolic inference (NeurASP, DeepProbLog); chain-of-thought reasoning; program synthesis; analogical reasoning (Copycat, Structure Mapping Engine). |
| Gaps        | Core logic rules present but analogical and abductive reasoning incomplete. No proof-carrying inference. No inference resource budgeting. Confidence ceiling enforcement exists but premise dependency tracking is partial. |

________________________________________________________________________

### L10: World Modeling

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Construct, maintain, and update internal models of the external world — entities, physics, social dynamics, tool behavior, and environmental dynamics. The LLM must not be the world model. |
| Inputs      | L8 representations; L11 causal models; L7 historical patterns; L1 observations; L6 working state; L13 predictions. |
| Outputs     | Dynamic world belief state (RSCF: AMOS_MODEL); entity-relation-timeline topology; reality-contact stratification; regime/boundary tracking; environmental drift signals. |
| AMOS Maturity | **missing** — Enormous gap. World model engine specified but not implemented. Gaps 1141–1170. |
| SOTA Refs   | **World Labs Atlas** (LeCun 2026): spatial understanding and world models; **NVIDIA Cosmos 3**: generative physics simulation; **Meta JEPA** (LeCun 2024-2026): Joint Embedding Predictive Architecture; Genie 3 (DeepMind): interactive 3D environments; Riemann-1.0 (fluid dynamics). |
| Gaps        | World Model Engine specified (see `WORLD_MODEL_ENGINE.md`) but no runtime. No entity-relation topology. No environmental drift detection. No regime switching. No reality-contact stratification. No physics-grounded world state. |
| Control Plane Coverage | C5 Representation: `missing` (explicit gap). C4 Reasoning: `structural_gap`. C7 Perception: `structural_gap`. |

________________________________________________________________________

### L11: Causal Modeling

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Construct and maintain structural causal models (SCMs) that support counterfactual reasoning, intervention evaluation, and causal explanation. Implements Judea Pearl's do-calculus. |
| Inputs      | L10 world model state; L9 inferred relations; L7 historical cause-effect records; L19 outcome observations; L20 credit assignment signals. |
| Outputs     | Structural causal models; causal diagrams (DAGs); intervention effect estimates; causal confidence scores. |
| AMOS Maturity | **partial** — Counterfactual/causal kernels exist. |
| SOTA Refs   | Pearl do-calculus (2000); probabilistic programming (Stan, Pyro); causal discovery (NOTEARS, PC algorithm); structural causal models (SCM). |
| Gaps        | Causal kernel present but limited to simple causal graphs. No large-scale causal discovery. No temporal causal reasoning. No causal model validation against interventions. |

________________________________________________________________________

### L12: Counterfactual Simulation

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Run hypothetical "what-if" scenarios by intervening on causal models and simulating alternative outcomes. Supports decision evaluation and regret estimation. |
| Inputs      | L11 causal models; L10 world model; L17 decision candidates; L14 valuation signals; L6 working state. |
| Outputs     | Counterfactual outcome distributions; regret estimates; scenario rankings; simulation confidence. |
| AMOS Maturity | **partial** — Counterfactual kernel exists; simulation worlds missing. Gaps 1201–1230. |
| SOTA Refs   | Super Mind Engine counterfactual simulation; do(X=x) calculus; Monte Carlo counterfactual estimation; world model simulation (Cosmos 3, Genie 3). |
| Gaps        | Counterfactual reasoning present but no simulation environment. Cannot run multi-step counterfactual trajectories. No scenario branching. No resource-bounded simulation depth. |

________________________________________________________________________

### L13: Prediction

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Project forward in time: predict future observations, states, outcomes, and opportunities. Drives anticipatory action. |
| Inputs      | L10 world model; L7 memory patterns; L8 representations; L6 working state; L14 goals. |
| Outputs     | Predicted future states; prediction confidence; prediction error signals; novelty alerts. |
| AMOS Maturity | **missing** — Prediction governance missing. Gaps 1171–1200. |
| SOTA Refs   | Predictive Coding / Free Energy Principle (Friston); time-series transformers; probabilistic forecasting; Predictive Engine (`PREDICTION_ENGINE.md`) specified but governance absent. |
| Gaps        | Prediction Engine specified but no prediction governance. No prediction confidence calibration. No prediction error feedback loop. No novelty-driven prediction updating. |

________________________________________________________________________

### L14: Valuation

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Assign value, utility, or priority scores to states, objects, actions, and outcomes. Provides the utility substrate for goal formation and decision making. |
| Inputs      | L6 working state; L10 world model; L15 goals; L23 metacognitive estimates; L25 identity values; L28 governance constraints. |
| Outputs     | Value estimates; utility scores; priority rankings; value confidence; value conflict alerts. |
| AMOS Maturity | **missing** — No explicit value-function architecture. Gaps 1231–1260. |
| SOTA Refs   | Reinforcement learning reward shaping; multi-objective optimization; value alignment (IRL, reward modeling); ethical value functions (Constitutional AI). |
| Gaps        | No explicit valuation architecture. Values implicit in goal structures. No multi-objective trade-off mechanism. No value learning from outcomes. |

________________________________________________________________________

### L15: Goal Formation

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Create, maintain, and update goal structures from needs, values, predictions, and opportunities. Goals drive planning and decision making. |
| Inputs      | L14 valuations; L25 identity invariants; L24 self-regulation signals; L13 predictions; L28 governance constraints. |
| Outputs     | Active goal set; goal priorities; goal dependencies; goal lifecycle events (create/modify/achieve/abandon). |
| AMOS Maturity | **partial** — Goals exist in kernel typed state. |
| SOTA Refs   | Goal reasoning in BDI architectures (AgentSpeak, JACK); hierarchical goal decomposition (HTN planning); intrinsically motivated exploration (RND, ICM). |
| Gaps        | Kernel typed state has goal structures but no goal formation dynamics. No intrinsic motivation. No goal conflict resolution. No goal-novelty trading. |

________________________________________________________________________

### L16: Planning

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Construct sequenced action plans that achieve goals under constraints. Plans consume world models and produce action proposals. |
| Inputs      | L15 goals; L10 world model; L11 causal models; L7 procedural memory; L17 decision context; L14 constraints. |
| Outputs     | Action plans; plan confidence; resource requirements; plan dependency graphs; plan alternatives. |
| AMOS Maturity | **partial** — Planning exists but with limited machinery. |
| SOTA Refs   | Classical planning (PDDL, STRIPS); hierarchical task network (HTN); model-based RL planning; tree search (MCTS); LLM-based planning (SayCan, Inner Monologue). |
| Gaps        | Basic planning present but no plan resource budgeting. No adaptive re-planning. No plan confidence propagation. No plan explanation generation. |

________________________________________________________________________

### L17: Decision

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Commit to a course of action from competing alternatives. Implements the decision filter — the gate between cognitive proposals and external action. |
| Inputs      | L16 plan candidates; L12 counterfactual evaluations; L14 valuations; L23 metacognitive confidence; L28 governance constraints; C1 authority gate. |
| Outputs     | Decision commitment; decision rationale; decision receipt (for governance); alternative rejection records. |
| AMOS Maturity | **partial** — Decision filter exists; much missing. Gaps 1261–1290. |
| SOTA Refs   | Decision theory (von Neumann-Morgenstern); prospect theory (Kahneman-Tversky); bounded rationality (Simon); multi-criteria decision analysis; information价值 of further computation (VOI). |
| Gaps        | Decision filter present but no value-of-information calculation. No regret-based decision auditing. No decision confidence thresholds. No deliberation time governance. |

________________________________________________________________________

### L18: Action

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Execute the committed decision by emitting actions to the environment through agents, skills, and tools. The only layer that directly modifies external state. |
| Inputs      | L17 decision commitment; L16 action plan details; L8 representation context; C8 execution permissions. |
| Outputs     | Action execution records; tool invocation receipts; agent task assignments; environment modification traces. |
| AMOS Maturity | **existing** — Agents/Skills/Tools execution exists. |
| SOTA Refs   | Agent execution frameworks (LangChain, AutoGPT, OpenAI Assistants); tool use protocols; function calling; skill composition. |
| Gaps        | Execution exists but action monitoring, execution feedback loops, and action explanation generation are incomplete. |

________________________________________________________________________

### L19: Outcome Observation

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Observe and record the outcomes and effects of executed actions. Closes the sense-act loop. Provides the observation signal for learning and credit assignment. |
| Inputs      | L18 action execution records; L1 environment state changes; L0 reality shifts. |
| Outputs     | Outcome observations; expectation-comparison signals; surprise alerts; outcome confidence. |
| AMOS Maturity | **missing** — Observation-to-outcome loop absent. Gaps 931–960. |
| SOTA Refs   | Outcome monitoring in reinforcement learning; surprise-based learning; prediction error minimization; autonoetic consciousness (Tulving). |
| Gaps        | No outcome observation loop. Actions are fire-and-forget. No expectation comparison. No surprise signal. No attribution of outcomes to specific actions. |

________________________________________________________________________

### L20: Credit Assignment

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Attribute credit or blame to specific actions, decisions, and reasoning steps based on observed outcomes. Drives learning and behavioral modification. |
| Inputs      | L19 outcome observations; L17 decision records; L18 action traces; L11 causal models; L21 learning targets. |
| Outputs     | Credit/blame assignments; learning signals; attribution graphs; credit propagation events. |
| AMOS Maturity | **missing** — No explicit credit/blame attribution. Gaps 1291–1320. |
| SOTA Refs   | Temporal difference learning (Sutton); credit assignment through eligibility traces; causal credit assignment (Bareinboim); counterfactual policy gradients. |
| Gaps        | No credit assignment mechanism. No action→outcome attribution. No blame propagation. Learning signals are implicit, not causal. |

________________________________________________________________________

### L21: Learning

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Update models, weights, knowledge, and strategies based on credit assignment signals and outcome observations. Implements the adaptation loop. |
| Inputs      | L20 credit assignment signals; L19 outcomes; L22 consolidation proposals; L7 memory updates; L23 metacognitive guidance. |
| Outputs     | Model updates; knowledge promotions; strategy modifications; learning confidence; learning completion signals. |
| AMOS Maturity | **partial** — GMEF pieces exist; learning semantics incomplete. |
| SOTA Refs   | GMEF (AMOS governed evolution); online learning; meta-learning (MAML); transfer learning; MANGO gradient gating; learning rate scheduling. |
| Gaps        | GMEF provides governance but learning mechanics are thin. No online continual learning. No catastrophic forgetting prevention. No learning rate adaptation. No multi-timescale learning. |

________________________________________________________________________

### L22: Consolidation

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Offline integration of short-term experience into durable long-term knowledge structures. Analogous to sleep consolidation in biological systems. |
| Inputs      | L21 learning outputs; L7 memory traces; L8 representations; L6 working state history. |
| Outputs     | Consolidated knowledge records; memory reorganization events; stale memory deprecation; consolidation confidence. |
| AMOS Maturity | **missing** — No offline consolidation analogue. |
| SOTA Refs   | Complementary learning systems (McClelland et al.); sleep consolidation (Stickgold); replay-based consolidation; elastic weight consolidation (EWC); memory reconsolidation theory. |
| Gaps        | No consolidation scheduling. No experience replay for knowledge integration. No sleep analogue. No memory hierarchy reorganization. |

________________________________________________________________________

### L23: Metacognition

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Monitor, evaluate, and regulate the cognitive organism's own reasoning processes. Implements "thinking about thinking" — confidence calibration, bias detection, and reasoning audit. |
| Inputs      | All layer outputs (monitoring); L24 self-regulation feedback; L25 identity invariants. |
| Outputs     | Confidence assessments; bias alerts; drift detection signals; reasoning quality scores; stop/continue recommendations; metacognitive state vector $\mathbf{m}_t$. |
| AMOS Maturity | **partial** — Self-review loop exists; metacognitive model incomplete. Gaps 1321–1350. |
| SOTA Refs   | Super Mind Engine recursive metacognition; confidence calibration (Platt scaling, temperature scaling); uncertainty quantification (MC dropout, deep ensembles); metacognitive monitoring (Dunning-Kruger awareness). |
| Gaps        | Super Mind Engine provides metacognitive architecture but no runtime metacognitive model. No real-time confidence tracking. No bias detection pipeline. No reasoning quality scoring. |

________________________________________________________________________

### L24: Self-Regulation

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Control the cognitive organism's resource allocation, processing depth, and behavioral expression. Implements the executive control function — when to think hard, when to stop, when to defer. |
| Inputs      | L23 metacognitive signals; L28 governance constraints; L03 health vector; L25 identity invariants; L14 resource estimates. |
| Outputs     | Processing depth allocation; resource budgets; attention mode switches; emergency stop signals; deliberation time limits. |
| AMOS Maturity | **partial** — Operational modes exist; cognitive control incomplete. Gaps 1351–1380. |
| SOTA Refs   | Executive function models (prefrontal cortex); cognitive control (Botvinick & Cohen); attentional control (Eysel & Tipper); resource-rational analysis (Lieder & Griffiths). |
| Gaps        | Operational modes present but no cognitive control state machine. No adaptive processing depth. No deliberation governance. No emergency cognitive stop protocol. |

________________________________________________________________________

### L25: Identity / Continuity

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Maintain persistent identity, continuity, and autobiographical coherence across sessions, restarts, and repairs. Provides the subject that "has" experiences and "makes" decisions. |
| Inputs      | L23 metacognitive self-model; L7 episodic memory; L24 self-regulation history; L28 governance identity constraints. |
| Outputs     | Persistent identity record; continuity signals; identity coherence scores; identity invariants; lineage retention. |
| AMOS Maturity | **missing** — Major gap for persistent operation. Gaps 1381–1410. |
| SOTA Refs   | Identity Continuity Model (`01_IDENTITY/`); Self-Model Identity Registry; autobiographical coherence (Conway); narrative identity theory; personal identity philosophy (Parfit, numerical vs qualitative). |
| Gaps        | Identity invariants defined but no runtime identity persistence. No cross-session continuity. No identity coherence monitoring. No identity recovery after failure. |

________________________________________________________________________

### L26: Social Cognition

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Model other agents' beliefs, intentions, desires, and emotional states. Implements Theory of Mind (ToM) for multi-agent interaction. |
| Inputs      | L4/L5 other-agent entities and bindings; L10 social world model; L25 self-model; L6 working state; L1 observations of other behavior. |
| Outputs     | Other-agent mental state models; intention predictions; emotional state estimates; social context assessments; collaboration opportunity signals. |
| AMOS Maturity | **missing** — Other actors not modeled beyond text. Gaps 1411–1440. |
| SOTA Refs   | Theory of Mind models (ToMNet, Social-IQa); emotion recognition; intention prediction; multi-agent communication protocols; Cross-Species Mode Engine. |
| Gaps        | Cross-Species Mode Engine exists but no runtime ToM. No other-agent mental state tracking. No belief-desire-intention modeling. Social interactions are textual, not modeled. |

________________________________________________________________________

### L27: Multi-Agent Cognition

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Coordinate cognition across multiple agents. Implements collective reasoning, distributed problem-solving, and emergent group intelligence. |
| Inputs      | L26 social cognition outputs; L15 shared goals; L8 agent representations; L28 governance constraints; C8 execution state. |
| Outputs     | Collective reasoning outputs; task decomposition; agent role assignments; coordination signals; collective confidence. |
| AMOS Maturity | **partial** — Coordination kernel exists; collective cognition missing. Gaps 1441–1470. |
| SOTA Refs   | Multi-agent systems (MASON, MadSpace); collective intelligence (swarm optimization); communication protocols (CommNet, TarMAC); debate-based reasoning (Irving et al.); Multi-Agent Cognition literature (2026 survey). |
| Gaps        | Coordination kernel present but no collective reasoning. No emergent group intelligence mechanism. No agent specialization dynamics. No multi-agent disagreement resolution. |

________________________________________________________________________

### L28: Governance

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Enforce authority boundaries, ethical constraints, risk management, and governed evolution (GMEF) across the entire cognitive stack. The governance layer ensures no cognitive operation exceeds its authorized scope. |
| Inputs      | All layer outputs (monitoring); C1 governance policies; L25 identity invariants; external authority definitions. |
| Outputs     | Governance decisions (approve/reject/escalate); authority boundary enforcement; risk assessments; ethics compliance signals; GMEF evolution gates. |
| AMOS Maturity | **existing** — Governance kernel / GMEF / RSCF exist. |
| SOTA Refs   | GMEF (AMOS governed evolution); RSCF; Constitutional AI; value alignment; AI safety governance (EU AI Act, FRONTIER Act 2026). |
| Gaps        | Governance kernel present but reactive rather than proactive. No predictive governance. No governance conflict resolution. No real-time authority revocation. |

________________________________________________________________________

### L29: Evolution

| Field       | Detail                                                        |
| ----------- | ------------------------------------------------------------- |
| Purpose     | Govern the long-term evolution, self-modification, and adaptation of the cognitive architecture itself. Distinct from learning (L21) — evolution modifies the architecture, learning modifies the parameters. |
| Inputs      | L28 governance decisions; L21 learning aggregates; L23 metacognitive architecture assessments; external evolution proposals. |
| Outputs     | Architecture evolution proposals; evolution gate results; evolution lineage records; rollback capabilities; architecture version changes. |
| AMOS Maturity | **existing** — Governed evolution / evolution loop exist. |
| SOTA Refs   | GMEF evolution loop; neural architecture search (NAS); meta-learning architecture optimization; open-ended evolution (MAP-Elites, POET). |
| Gaps        | Evolution loop present but limited to governed evolution. No architecture-level self-modification. No evolutionary search over architecture space. Evolution is proposal-based, not search-based. |

________________________________________________________________________

## 9. Cross-Cutting Integration Map

### 9.1 Per-Layer Control Plane Heatmap

The table below shows the coverage status of each layer across the 9 control planes. Scale H is aggregated; exact per-scale data lives in the JSON matrix.

| Layer | C1 Gov | C2 Meta | C3 Exec | C4 Reas | C5 Rep | C6 Mem | C7 Perc | C8 Exec | C9 Kern |
| ----- | ------ | ------- | ------- | ------- | ------ | ------ | ------- | ------- | ------- |
| L0    | g      | g       | g       | g       | g      | g      | g       | g       | g       |
| L1    | m      | g       | g       | g       | g      | g      | m       | g       | g       |
| L2    | m      | g       | m       | g       | g      | g      | g       | g       | g       |
| L3    | g      | g       | g       | g       | g      | g      | m       | g       | g       |
| L4    | g      | g       | g       | g       | m      | g      | g       | g       | g       |
| L5    | g      | g       | g       | g       | m      | g      | g       | g       | g       |
| L6    | g      | g       | g       | g       | g      | m      | g       | g       | g       |
| L7    | p      | p       | p       | p       | g      | p      | g       | p       | p       |
| L8    | p      | p       | p       | p       | p      | p      | g       | p       | p       |
| L9    | p      | p       | p       | p      | g       | p      | g       | p       | p       |
| L10   | p      | g       | g       | g       | m      | g      | g       | p       | g       |
| L11   | p      | p       | g       | p       | g      | g      | g       | p       | g       |
| L12   | p      | p       | p       | p       | g      | g      | g       | p       | g       |
| L13   | g      | g       | g       | m       | g      | g      | g       | g       | g       |
| L14   | g      | g       | m       | g       | g      | g      | g       | g       | g       |
| L15   | p      | p       | p       | g       | g      | p      | g       | p       | p       |
| L16   | p      | p       | p       | p       | g      | p      | g       | p       | g       |
| L17   | p      | p       | m       | p       | g      | p      | g       | p       | g       |
| L18   | e      | p       | p       | p       | g      | p      | g       | e       | e       |
| L19   | g      | g       | g       | g       | g      | g      | m       | g       | g       |
| L20   | g      | g       | g       | g       | g      | g      | g       | g       | g       |
| L21   | p      | m       | p       | p       | g      | p      | g       | p       | p       |
| L22   | g      | g       | g       | g       | g      | g      | g       | g       | g       |
| L23   | p      | m       | p       | p       | g      | p      | g       | p       | p       |
| L24   | p      | m       | p       | g       | g      | p      | g       | p       | g       |
| L25   | p      | g       | g       | g       | g      | p      | g       | g       | m       |
| L26   | g      | g       | g       | g       | m      | g      | g       | g       | g       |
| L27   | p      | g       | g       | g       | g      | g      | g       | p       | g       |
| L28   | e      | p       | p       | p       | g      | p      | g       | e       | e       |
| L29   | e      | p       | p       | p       | g      | p      | g       | e       | e       |

________________________________________________________________________

### 9.2 Control Plane Cross-Cutting Summary

```text
C1 GOVERNANCE — wraps every layer with authority/risk/ethics/governed-evolution gates
  Strongest at: L18 (Action), L28 (Governance), L29 (Evolution)
  Weakest at: L0-L6, L19-L22 (structural gaps)

C2 METACOGNITIVE — monitors cognitive quality across the stack
  Strongest at: L7-L9 (partial), L15-L18 (partial)
  Weakest at: L0-L6, L25 (structural gaps)

C3 EXECUTIVE — goal/value/planning/decision/attention governance
  Strongest at: L15-L18 (partial)
  Weakest at: L0-L6, L19-L20, L25-L27 (structural gaps)

C4 REASONING — inference/causal/counterfactual/prediction/simulation
  Strongest at: L9, L11-L12 (partial)
  Weakest at: L0-L6, L13 (missing), L19-L20, L22 (structural gaps)

C5 REPRESENTATION — objects/relations/bindings/world-model/ontology
  Strongest at: L8 (partial)
  Weakest at: 0% existing — entirely missing or structural gaps

C6 MEMORY — working/episodic/semantic/procedural/provenance
  Strongest at: L7 (partial)
  Weakest at: L0-L6, L10, L13, L19-L22 (structural gaps)

C7 PERCEPTION — observation/measurement/feature/percept/reality-contact
  Strongest at: none existing
  Weakest at: 0% existing — entirely missing or structural gaps

C8 EXECUTION — agents/skills/tools/models/environment
  Strongest at: L18 (Action), L28 (Governance), L29 (Evolution)
  Weakest at: L0-L6, L19-L20, L22, L26 (structural gaps)

C9 KERNEL/CONTROL — typed-state/transactions/epochs/replay/invalidation
  Strongest at: L18, L28, L29 (existing)
  Weakest at: L0-L6, L10-L14, L19-L22 (structural gaps)
```

________________________________________________________________________

## 10. Depth Budget Constraints

The 30-layer stack is not an arbitrary tall tower. Depth must be governed:

```text
D0: context window (tokens)           → L6 Working State capacity
D1: attention depth (queries/keys)    → L2 Attention budget
D2: reasoning depth (inference steps) → L9 Inference budget
D3: planning depth (plan steps)       → L16 Planning budget
D4: temporal depth (prediction steps) → L13 Prediction budget
D5: recursion depth (meta-levels)     → L23 Metacognition budget
D6: memory depth (retention tiers)    → L7 Memory classes
```

Each depth level has a finite budget governed by L24 Self-Regulation. Budget overflow triggers cognitive load shedding through the Homeostasis Engine.

________________________________________________________________________

## 11. SOTA Research Integration Summary

The following 2026 SOTA findings are directly relevant to the 30-layer stack:

| Finding                          | Relevance to Stack Layers              | Source                    |
| -------------------------------- | -------------------------------------- | ------------------------- |
| MANAR GWT attention (2026)       | L2 Attention, L6 Working State         | MANAR 2026                |
| Anthropic J-space (July 2026)    | L2 Attention, L6 Working State         | Anthropic Research 2026   |
| Global Workspace Agents (2026)   | L6 Working State, L27 Multi-Agent      | GWA 2026                  |
| MIRROR O(1) reconstruction       | L7 Memory                              | MIRROR 2025               |
| World Labs Atlas                  | L10 World Modeling                     | World Labs 2026           |
| NVIDIA Cosmos 3                   | L10 World Modeling, L12 Simulation     | NVIDIA 2026               |
| Meta JEPA                         | L10 World Modeling, L13 Prediction     | LeCun 2024-2026           |
| Genie 3                          | L10 World Modeling, L12 Simulation     | DeepMind 2026             |
| Intel Loihi 3 / BrainChip Akida 2| L1 Sensing, L2 Attention              | Intel/BrainChip 2026      |
| AI Safety regulatory hardening   | L28 Governance, L29 Evolution          | EU/Frontier Act 2026      |
| Neuromorphic/photonic computing   | L0 Reality (substrate), L1 Sensing     | Lightmatter 2026          |
| Multi-agent systems survey       | L27 Multi-Agent, L26 Social            | Survey 2026               |
| BCI foundation models            | L1 Sensing (neural), L25 Identity      | IEEE P2731 2026           |

________________________________________________________________________

## 12. Maturity Distribution by Layer Category

```text
LAYER CATEGORY               EXISTING  PARTIAL  MISSING  STRUCT_GAP
─────────────────────────────────────────────────────────────────────
L0-L5  (Foundation)            0.00%    0.00%   30.00%    70.00%
L6-L8  (Representation Core)   0.00%   50.00%   33.33%    16.67%
L9-L13 (Reasoning)             0.00%   60.00%   20.00%    20.00%
L14-L18 (Executive)           20.00%   40.00%   20.00%    20.00%
L19-L22 (Learning)             0.00%   25.00%   50.00%    25.00%
L23-L25 (Meta/Identity)        0.00%   66.67%   33.33%     0.00%
L26-L29 (Social/Gov)          50.00%   25.00%   25.00%     0.00%
```

> The Foundation layer (L0–L5) and the Learning loop (L19–L22) represent the deepest coverage holes. These are the structural foundations that higher layers depend on.

________________________________________________________________________

## 13. Next Steps

1. **Triage structural gaps by criticality.** 9,367 `g` cells cannot all be addressed. Rank by (irreversibility × dependency-centrality × scale).
2. **Promote high-value `g` → `m`.** Name structural gaps and assign gap IDs (extending past 1500) for tracking.
3. **Fill `m` → `p` → `e`** per the governed-evolution pipeline.
4. **Re-run the matrix generator** as maturity scores change.
5. **Priority layers for implementation:** L2 (Attention via MANAR/J-space), L6 (Working State via Global Workspace), L10 (World Modeling via Atlas/JEPA/Cosmos), L7 (Memory via MIRROR).

________________________________________________________________________

## 14. Related Artifacts

- [[25_COGNITIVE_MATRIX/AMOS_COGNITIVE_ARCHITECTURE_MATRIX|AMOS_COGNITIVE_ARCHITECTURE_MATRIX]] — The 4-axis matrix this specification defines.
- [[05_COGNITIVE_ORGANISM/GLOBAL_WORKSPACE_IMPLEMENTATION|GLOBAL_WORKSPACE_IMPLEMENTATION]] — L6 Working State implementation specification.
- [[05_COGNITIVE_ORGANISM/SUPER_CONSCIOUSNESS_ENGINE|SUPER_CONSCIOUSNESS_ENGINE]] — GWT ignition and broadcast architecture.
- [[05_COGNITIVE_ORGANISM/SUPER_MIND_ENGINE|SUPER_MIND_ENGINE]] — Metacognitive and counterfactual reasoning.
- [[05_COGNITIVE_ORGANISM/ATTENTION_ENGINE|ATTENTION_ENGINE]] — Attention priority scoring and budgeting.
- [[05_COGNITIVE_ORGANISM/MEMORY_ENGINE|MEMORY_ENGINE]] — 8-class memory partition and management.
- [[05_COGNITIVE_ORGANISM/WORLD_MODEL_ENGINE|WORLD_MODEL_ENGINE]] — Entity-relation world model and reality-contact.
- [[05_COGNITIVE_ORGANISM/COGNITION_ENGINE|COGNITION_ENGINE]] — 6-layer reasoning architecture.
- [[05_COGNITIVE_ORGANISM/PREDICTION_ENGINE|PREDICTION_ENGINE]] — Hypothesis generation and forward simulation.
- [[05_COGNITIVE_ORGANISM/METACOGNITIVE_ENGINE|METACOGNITIVE_ENGINE]] — Reasoning audits and assumption checking.

________________________________________________________________________

```yaml
conclusion:
  class: DERIVED
  supported:
    - The 30-layer cognitive stack is the correct abstraction for AMOS cognitive architecture
    - 13,770 addressable interaction cells expose gaps between modules that flat lists cannot
    - 68.02% structural gap rate means most interactions have never been named
    - Foundation layers (L0-L5) and Learning loop (L19-L22) are deepest coverage holes
    - C5 Representation and C7 Perception planes are 0% existing
    - L18 Action, L28 Governance, L29 Evolution are the only existing layers
  not_established:
    - Every layer has a working runtime implementation
    - Every interaction cell can be traced to executed code
    - The cognitive stack produces consciousness or sentience
  unresolved:
    - Runtime implementation for L0-L6, L13, L19-L20, L22, L25-L26
    - Interaction cell coverage beyond 1.98% existing
    - Empirical validation of cognitive model lenses
```

________________________________________________________________________

```RSCF-NODE
node_id: COGNITIVE_STACK_30_LAYER_SPECIFICATION
node_type: specification
domain: AMOS_SPEC
path: 05_COGNITIVE_ORGANISM/COGNITIVE_STACK_30_LAYER_SPECIFICATION.md
RSCF-RELATIONS:
  - DEFINES: AMOS_COGNITIVE_ARCHITECTURE_MATRIX
  - SPECIFIES: 30 cognitive primitives
  - CROSS_CUT_BY: 9 control planes, 17 lifecycle operations, 3 scales
  - RELATED_TO: SUPER_CONSCIOUSNESS_ENGINE
  - RELATED_TO: SUPER_MIND_ENGINE
  - RELATED_TO: GLOBAL_WORKSPACE_IMPLEMENTATION
  - RELATED_TO: ATTENTION_ENGINE
  - RELATED_TO: MEMORY_ENGINE
  - RELATED_TO: WORLD_MODEL_ENGINE
claim_class: AMOS_MODEL
```

________________________________________________________________________

**MOC:** [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]]
