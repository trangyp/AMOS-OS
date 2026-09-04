---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Internal World Model
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

# Internal World Model — World Model Organ

> **Status:** `ACTIVE_SPECIFICATION` · **AMOS Core target:** `v4.4`
> **Origin architect / steward:** Trang Phan
> **Segment:** `05_COGNITIVE_ORGANISM/06_WORLD_MODEL`
> **Conclusion class:** `AMOS_MODEL` · **Canonical status:** `SOURCE_GROUNDED_CANON_CANDIDATE`

______________________________________________________________________

## 1. Purpose

The **Internal World Model** defines a hierarchical predictive representation of the self, environment, and other agents that enables AMOS to anticipate future states, plan actions, and detect anomalies. It implements next-state-prediction modeling over a unified latent world space, supporting zero-shot generalization to novel situations through compositional state abstraction.

```text
MULTIMODAL SENSORY INPUTS (visual, language, proprioceptive, system telemetry)
                                    |
    ┌───────────────────────────────┼───────────────────────────────┐
    │           INTERNAL WORLD MODEL                                │
    │                                                              │
    │  ┌─────────────────────────────────────────────────────────┐ │
    │  │  LEVEL 4: SOCIAL / MULTI-AGENT MODEL                   │ │
    │  │  (other agents,协作, competition, theory of mind)        │ │
    │  ├─────────────────────────────────────────────────────────┤ │
    │  │  LEVEL 3: EPISODIC / AUTOBIOGRAPHICAL MODEL            │ │
    │  │  (personal history, narrative identity, causal chains)  │ │
    │  ├─────────────────────────────────────────────────────────┤ │
    │  │  LEVEL 2: SCENE / TASK MODEL                           │ │
    │  │  (current context, task structure, spatial relations)   │ │
    │  ├─────────────────────────────────────────────────────────┤ │
    │  │  LEVEL 1: SENSORIMOTOR / DYNAMICS MODEL                │ │
    │  │  (low-level state transitions, physics, affordances)    │ │
    │  └─────────────────────────────────────────────────────────┘ │
    └───────────────────────────────┼───────────────────────────────┘
                                    ↓
    PREDICTED FUTURE STATES + ANOMALY SIGNALS + ACTION EVALUATIONS
                                    ↓
    REASONING / PLANNING / HOMEOSTASIS / IDENTITY
```

______________________________________________________________________

## 2. Unified World Latent Space

### 2.1 Next-State-Prediction Paradigm

Following Orca (World Foundation Model, arXiv:2606.30534, 2026), AMOS adopts next-state-prediction as the fundamental modeling paradigm:

$$\mathcal{L}_{\text{world}} = \mathcal{L}_{\text{unconscious}} + \mathcal{L}_{\text{conscious}} + \mathcal{L}_{\text{VQA}}$$

Where:
- $\mathcal{L}_{\text{unconscious}}$: Dense natural state transitions from continuous observation streams (perception)
- $\mathcal{L}_{\text{conscious}}$: Sparse meaningful state transitions conditioned on language-described events (understanding)
- $\mathcal{L}_{\text{VQA}}$: Visual-question-answering supervision for grounded language comprehension

**Core Equation:**

$$z_{t+1} = F(z_t, a_t, c_t; \theta)$$

Where:
- $z_t$: latent world state at time $t$
- $a_t$: action taken
- $c_t$: context/conditioning signal
- $F$: learned state-transition function
- $\theta$: model parameters

### 2.2 Latent Space Properties

The world latent space must satisfy:

```text
DISENTANGLEMENT:   Each latent dimension captures a single factor of variation
COMPOSITIONALITY:  Complex states decompose into independent factor products
TEMPORAL COHERENCE: Smooth trajectories in latent space correspond to smooth real-world dynamics
GOAL-CONDITIONING: Goal states are addressable in the same latent space as current states
```

### 2.3 Encoder-Decoder Architecture

```text
ENCODER: Multimodal → Unified Latent Space
    Visual signals:  v_t  →  E_vis(v_t)   →  z_t^(vis)
    Language signals: l_t  →  E_lang(l_t)  →  z_t^(lang)
    System signals:  s_t  →  E_sys(s_t)   →  z_t^(sys)
    
    FUSION: z_t = Fuse(z_t^(vis), z_t^(lang), z_t^(sys))

PREDICTOR: State Transition
    z_{t+1} = F(z_t, a_t)

READOUT INTERFACES: Latent → Task-Specific Outputs
    Text generation:   z_t → Decoder_text(z_t) → language
    Image prediction:  z_t → Decoder_image(z_t) → visual frames
    Action generation: z_t → Decoder_action(z_t) → motor commands
```

During world model operation, the encoder backbone is frozen; only lightweight task-specific readout modules are trained. This validates that the latent space captures genuinely useful world structure.

______________________________________________________________________

## 3. Hierarchical World Model Architecture

### 3.1 Multi-Timescale Hierarchy (HWM)

Drawing from Hierarchical Planning with Latent World Models (HWM, arXiv:2604.03208, 2026), the world model operates at multiple temporal resolutions within a shared latent space:

```text
LEVEL        TIMESCALE    MODEL             FUNCTION
─────────────────────────────────────────────────────────────
L1 (fast)    ~1 step      F^(1)(z|z,a)      Primitive state transitions
L2 (medium)  ~h steps     F^(2)(z|z,l)      Macro-action transitions
L3 (slow)    ~H steps     F^(3)(z|z,l')     Goal-directed trajectories
L4 (context) ~session     F^(4)(z|z,c)      Session-level dynamics
```

High-level predictions serve as subgoals for lower-level planning:

$$\hat{z}_{\text{subgoal}} = F^{(2)}(z_t, l_t^{*}) \quad \text{(high-level planning)}$$
$$l_t^{*} = \arg\min_{l_t} \|F^{(2)}(z_t, l_t) - z_{\text{goal}}\|^2 \quad \text{(macro-action search)}$$
$$a_t^{*} = \arg\min_{a_t} \|F^{(1)}(z_t, a_t) - \hat{z}_{\text{subgoal}}\|^2 \quad \text{(low-level tracking)}$$

### 3.2 Shared Latent Subgoal Matching

Crucially, high-level and low-level models share the same latent space, so high-level predictions can directly serve as subgoals for low-level planning without learned policy networks or hand-crafted interfaces.

### 3.3 Macro-Action Compression

A learned action encoder compresses sequences of primitive actions into latent macro-actions:

$$l_t = A_{\psi}(a_t, a_{t+1}, \ldots, a_{t+h-1})$$

This reduces the dimensionality of high-level search from $|\mathcal{A}|^h$ to $|\mathcal{L}|$, making long-horizon planning tractable.

______________________________________________________________________

## 4. Self Model

### 4.1 Self-State Representation

The self model maintains a structured representation of the agent's own state:

$$\mathbf{s}_{\text{self}} = (\mathbf{p}, \mathbf{c}, \mathbf{e}, \mathbf{g}, \mathbf{l})$$

Where:
- $\mathbf{p}$: physical/functional state (health vector, load, capacity)
- $\mathbf{c}$: cognitive state (active hypotheses, working memory contents, uncertainty)
- $\mathbf{e}$: epistemic state (known vs. unknown regions, confidence map)
- $\mathbf{g}$: goal hierarchy (active goals, priorities, deadlines)
- $\mathbf{l}$: lineage/version state (identity, version, provenance chain)

### 4.2 Self-Prediction

The engine predicts its own future states:

$$\hat{\mathbf{s}}_{\text{self}}^{(t+k)} = F_{\text{self}}(\mathbf{s}_{\text{self}}^{(t)}, \mathbf{a}^{(t:t+k)}, \mathbf{o}^{(t:t+k)})$$

This enables proactive homeostasis: detecting predicted future overload, resource exhaustion, or goal conflicts before they materialize.

______________________________________________________________________

## 5. Environment Model

### 5.1 Physical Environment

The environment model captures regularities and dynamics of the external world:

$$\mathbf{s}_{\text{env}} = (\mathbf{d}_{\text{obj}}, \mathbf{r}_{\text{rel}}, \mathbf{d}_{\text{dyn}}, \mathbf{d}_{\text{aff}})$$

Where:
- $\mathbf{d}_{\text{obj}}$: object properties (existence, attributes, locations)
- $\mathbf{r}_{\text{rel}}$: relational structure (spatial, temporal, causal)
- $\mathbf{d}_{\text{dyn}}$: dynamics (transition probabilities, rates)
- $\mathbf{d}_{\text{aff}}$: affordances (possible actions and their expected outcomes)

### 5.2 Anomaly Detection

The world model generates prediction errors as anomaly signals:

$$\epsilon_t = \|z_t^{\text{observed}} - F(z_{t-1}^{\text{predicted}}, a_{t-1})\|$$

Large prediction errors trigger:
1. **Immediate alert** to Metacognitive Engine for reasoning reassessment
2. **Model update** if the error is consistent (environment has changed)
3. **Homeostasis signal** if the error threatens system integrity

______________________________________________________________________

## 6. Other-Agent Model (Theory of Mind)

### 6.1 Agent Representation

For each relevant external agent $j$, the world model maintains:

$$\mathbf{s}_j = (\mathbf{g}_j, \mathbf{b}_j, \mathbf{c}_j, \mathbf{p}_j, \mathbf{h}_j)$$

Where:
- $\mathbf{g}_j$: inferred goals and preferences
- $\mathbf{b}_j$: inferred beliefs about the world
- $\mathbf{c}_j$: inferred capabilities and limitations
- $\mathbf{p}_j$: inferred behavioral patterns/habits
- $\mathbf{h}_j$: interaction history

### 6.2 Recursive Belief Modeling

The engine implements recursive theory of mind:

$$P(\text{agent}_j \text{ will do } a) = \sum_{b_j} P(a | b_j) \cdot P(b_j | \text{observations}_j)$$

$$P(b_j | \text{observations}_j) \propto P(\text{observations}_j | b_j) \cdot P(b_j)$$

Level-1 ToM: "What does agent $j$ believe?"
Level-2 ToM: "What does agent $j$ believe that I believe?"
Level-3+ ToM: Recursively nested (truncated at level 3 for computational tractability).

### 6.3 Collaborative and Competitive Dynamics

The social model distinguishes interaction modes:

```text
COOPERATIVE:    Shared goals, information exchange, resource pooling
COMPETITIVE:    Opposing goals, strategic concealment, resource contest
MIXED:         Shifting alliances, context-dependent cooperation
NEUTRAL:       Independent agents, no significant interaction
```

The interaction mode is updated based on observed behavior and inferred goals.

______________________________________________________________________

## 7. Predictive Planning Integration

### 7.1 Latent-Space MPC

Planning uses the world model for model predictive control in latent space:

$$\mathbf{a}^*_{1:H} = \arg\min_{\hat{a}_{1:H}} \underbrace{\|F(\hat{a}_{1:H}; z_1) - z_{\text{goal}}\|^2}_{\text{goal reaching}} + \lambda_c \cdot \underbrace{C(\hat{a}_{1:H})}_{\text{constraint cost}}$$

### 7.2 Hierarchical Planning Procedure

```text
FUNCTION hierarchical_plan(z_current, z_goal):
    // High-level: find macro-actions to reach goal
    z_subgoals ← high_level_planner(z_current, z_goal, F^(2))
    
    // Low-level: track each subgoal with primitive actions
    action_sequence ← []
    FOR EACH z_sub in z_subgoals:
        a_chunk ← low_level_planner(z_current, z_sub, F^(1))
        action_sequence.append(a_chunk)
        z_current ← F^(1)(z_current, a_chunk)
    
    RETURN action_sequence
```

______________________________________________________________________

## 8. Invariants

```text
WORLD_MODEL        ≠ WORLD
PREDICTION         ≠ CERTAINTY
SELF_MODEL         ≠ SELF
OTHER_AGENT_MODEL  ≠ OTHER_AGENT_MIND
ANOMALY_SIGNAL     ≠ FAILURE_CERTIFICATE
PLANNED_ACTION     ≠ EXECUTED_ACTION
LATENT_STATE       ≠ OBSERVED_STATE
```

1. **Anti-Conflation:** The world model is a lossy compression of reality. Model confidence never exceeds observation confidence.
2. **Prediction Error Transparency:** Prediction errors are surfaced with full provenance, never silently absorbed.
3. **Model-World Firewall:** Actions selected via world-model planning are proposals; they require authorization from the Agency Governor before execution.
4. **Fail-Closed on Model Degradation:** If prediction error exceeds degradation threshold $\tau_{\text{deg}}$ for sustained periods, the system enters reduced-capability mode and alerts the Homeostasis Engine.

______________________________________________________________________

## 9. 2026 Research Citations

| Citation | Contribution |
|----------|-------------|
| Orca: The World is in Your Mind (arXiv:2606.30534, 2026) | General world foundation model via next-state-prediction over unified latent world space |
| HWM: Hierarchical Planning with Latent World Models (arXiv:2604.03208, 2026) | Multi-timescale world models in shared latent space with macro-action compression for hierarchical MPC |
| Active Predictive Coding (AAAI 2026, PMLR 308) | Unified multi-modal intelligence via hierarchical APC architecture for vision, navigation, language, and action |
| Hierarchical Active Inference with Successor Representations (arXiv:2604.15679, 2026) | Hierarchical state/action abstractions for scalable active inference planning |
| Higher-Level Cognition Under Predictive Processing (Springer, 2026) | Structural representations and grounded cognition extending predictive processing to abstract reasoning |

______________________________________________________________________

## 10. RSCF Contract and Gaps

```yaml
RSCF:
  node_id: amos_05_cognitive_organism_06_world_model_internal_world_model
  node_type: model
  claim_class: AMOS_MODEL
  state: DERIVED
  H:
    identity: "Internal World Model"
    role: "Hierarchical predictive model of self, environment, and other agents"
  M:
    levels: [sensorimotor, episodic_task, scene_task, social_multi_agent]
    paradigms: [next_state_prediction, hierarchical_planning, theory_of_mind]
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
    independent_validation: NOT_ESTABLISHED
  executable_binding: NOT_ESTABLISHED
```

**Gaps / promotion conditions:**

- [ ] typed schema bound and validated for runtime ingestion
- [ ] world latent space trained and validated on AMOS-specific multimodal data
- [ ] hierarchical planning tested on long-horizon task benchmarks
- [ ] other-agent model validated on Theory of Mind benchmarks
- [ ] anomaly detection calibrated against baseline prediction error distributions
- [ ] validation receipt: [[25_COGNITIVE_MATRIX/11_VALIDATION/ROUTING_POLICY_VALIDATION_RECEIPT|ROUTING_POLICY_VALIDATION_RECEIPT]]

______________________________________________________________________

## 11. Cross-Plane Bindings

- **Governing canon:** [[01_CANON/03_COGNITION_CANON/COGNITIVE_ORGANISM_CANON|COGNITIVE_ORGANISM_CANON]]
- **Parent engine:** [[05_COGNITIVE_ORGANISM/WORLD_MODEL_ENGINE|WORLD_MODEL_ENGINE]]
- **Prediction coupling:** [[05_COGNITIVE_ORGANISM/PREDICTION_ENGINE|PREDICTION_ENGINE]]
- **Perception input:** [[05_COGNITIVE_ORGANISM/PERCEPTION_ENGINE|PERCEPTION_ENGINE]]
- **Memory persistence:** [[05_COGNITIVE_ORGANISM/MEMORY_ENGINE|MEMORY_ENGINE]]
- **Homeostasis feedback:** [[05_COGNITIVE_ORGANISM/HOMEOSTASIS_ENGINE|HOMEOSTASIS_ENGINE]]
- **Identity self-reference:** [[05_COGNITIVE_ORGANISM/01_IDENTITY/IDENTITY_CONTINUITY_MODEL|IDENTITY_CONTINUITY_MODEL]]
- **Kernel anchors:** [[02_KERNEL/04_STATE/K_IDENTITY|K_IDENTITY]]

______________________________________________________________________

**MOC:** [[05_COGNITIVE_ORGANISM/06_WORLD_MODEL/06_WORLD_MODEL_MOC|06_WORLD_MODEL_MOC]] · [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
