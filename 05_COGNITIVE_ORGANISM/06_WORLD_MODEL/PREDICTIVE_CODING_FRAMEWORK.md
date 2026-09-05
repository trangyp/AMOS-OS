---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Predictive Coding Framework
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

# Predictive Coding Framework — World Model Organ

> **Status:** `ACTIVE_SPECIFICATION` · **AMOS Core target:** `v4.4`
> **Origin architect / steward:** Trang Phan
> **Segment:** `05_COGNITIVE_ORGANISM/06_WORLD_MODEL`
> **Conclusion class:** `AMOS_MODEL` · **Canonical status:** `SOURCE_GROUNDED_CANON_CANDIDATE`

______________________________________________________________________

## 1. Purpose

The **Predictive Coding Framework** implements the computational substrate for prediction-error minimization within AMOS, grounding perception, learning, and action in the Free Energy Principle (FEP). It defines how the cognitive organism generates top-down predictions, computes bottom-up prediction errors, and minimizes variational free energy through both perceptual inference (model updating) and active inference (action selection).

```text
TOP-DOWN PREDICTIONS          BOTTOM-UP PREDICTION ERRORS
(from generative model)        (from sensory input)
        ↓                              ↑
┌──────────────────────────────────────────────────┐
│              PREDICTIVE CODING LAYER             │
│                                                  │
│  GENERATIVE MODEL: p(o|z) · p(z)                │
│         ↕                                        │
│  PREDICTION ERROR: ε = o - ŷ(z)                 │
│         ↕                                        │
│  FREE ENERGY: F = D_KL[q(z)||p(z)] - E_q[ln p(o|z)] │
│         ↕                                        │
│  UPDATE RULE: minimize F via {q*, θ*, a}         │
│                                                  │
│  ┌────────────┐ ┌────────────┐ ┌──────────────┐ │
│  │ PERCEPTION │ │  LEARNING  │ │ACTION (Active│ │
│  │ (q update) │ │ (θ update) │ │ Inference)   │ │
│  └────────────┘ └────────────┘ └──────────────┘ │
└──────────────────────────────────────────────────┘
        ↓
    UPDATED WORLD MODEL + SELECTED ACTIONS
```

______________________________________________________________________

## 2. Free Energy Principle Foundation

### 2.1 Variational Free Energy

Following Friston (2010) and extended by Bhattacharya et al. (Bayesian Reflex, arXiv:2608.00492, 2026), the variational free energy functional is:

$$F[q] = D_{\text{KL}}[q(\mathbf{z}) \| p(\mathbf{z})] - \mathbb{E}_{q(\mathbf{z})}[\ln p(\mathbf{o} | \mathbf{z})]$$

Where:
- $q(\mathbf{z})$: approximate posterior over hidden states (recognition model)
- $p(\mathbf{z})$: prior over hidden states (generative model)
- $p(\mathbf{o} | \mathbf{z})$: likelihood of observations given hidden states

$F$ is an upper bound on negative log model evidence: $F \geq -\ln p(\mathbf{o})$. Minimizing $F$ is equivalent to maximizing model evidence (Occam's razor).

### 2.2 Expected Free Energy for Action Selection

For planning under uncertainty, the Expected Free Energy (EFE) guides action selection:

$$G(\mathbf{a}) = \underbrace{\mathbb{E}_{q(\mathbf{z}|\mathbf{a})}[H[p(\mathbf{o}|\mathbf{z})]]}_{\text{pragmatic value (expected ambiguity)}} + \underbrace{D_{\text{KL}}[q(\mathbf{z}|\mathbf{a}) \| p(\mathbf{z})]}_{\text{information gain (epistemic value)}}$$

Actions that minimize $G$ simultaneously:
- **Reduce ambiguity** about hidden states (pragmatic exploitation)
- **Reduce uncertainty** about the generative model (epistemic exploration)

### 2.3 Perception-Action Unification

The FEP provides a single objective for both perception and action:

$$\text{Perception:} \quad q^* = \arg\min_q F[q] \quad \text{(update beliefs to match observations)}$$
$$\text{Action:} \quad \mathbf{a}^* = \arg\min_{\mathbf{a}} G(\mathbf{a}) \quad \text{(select actions that minimize expected surprise)}$$

This unification means that perception and action are two routes to the same objective: minimizing surprise (free energy) about sensory observations.

______________________________________________________________________

## 3. Hierarchical Predictive Coding Architecture

### 3.1 Cortical Hierarchy Implementation

Following the Active Predictive Coding (APC) framework (Duan et al., AAAI 2026, PMLR 308), AMOS implements a canonical sensory-motor processing circuit replicated across cortical areas:

```text
HIGHEST LEVEL (Abstract Goals / Intentions)
    │ prediction向下
    │ error向上
    ↓
MID-HIGH LEVEL (Scene / Context)
    │ prediction向下
    │ error向上
    ↓
MID-LOW LEVEL (Object / Feature)
    │ prediction向下
    │ error向上
    ↓
LOWEST LEVEL (Pixel / Signal)
```

At each level $l$:

$$\hat{\mathbf{o}}^{(l)} = g^{(l)}(\mathbf{z}^{(l+1)}) \quad \text{(top-down prediction)}$$
$$\boldsymbol{\epsilon}^{(l)} = \mathbf{o}^{(l)} - \hat{\mathbf{o}}^{(l)} \quad \text{(prediction error)}$$
$$\mathbf{z}^{(l)} = \mathbf{z}^{(l)} + \eta \cdot \boldsymbol{\epsilon}^{(l)} \cdot \frac{\partial \mathbf{z}^{(l)}}{\partial \boldsymbol{\epsilon}^{(l)}} \quad \text{(state update)}$$

### 3.2 State-Transition Dynamics

In APC, complex state transition dynamics are decomposed into hierarchical sequences of simpler dynamics:

$$\mathbf{z}^{(l)}_{t+1} = f^{(l)}(\mathbf{z}^{(l)}_t, \mathbf{z}^{(l+1)}_t) \quad \text{(higher-level modulates lower-level dynamics)}$$

Complex policies are similarly decomposed:

$$\pi^{(l)} = \pi^{(l+1)} \circ \pi^{(l)}_{\text{sub}} \quad \text{(policy composition)}$$

With the lowest level comprising sequences of primitive actions.

### 3.3 Multiplicative Top-Down Modulation

Following the bidirectional recurrent gating model (Salehi et al., 2026), top-down predictions modulate lower-level processing via multiplicative gating:

$$\mathbf{z}^{(l)}_{t+1} = \mathbf{a}^{(l+1)}_t \odot g(\mathbf{z}^{(l)}_t)$$

Where $\mathbf{a}^{(l+1)}_t$ is the attentional gating signal from level $l+1$, and $\odot$ is element-wise multiplication. This implements "what is relevant" at higher levels controlling "what is processed" at lower levels.

______________________________________________________________________

## 4. Bayesian Reflex: Scalable Implementation

### 4.1 Three Pillars

From Bhattacharya et al. (2026), the Bayesian Reflex provides the algorithmic ingredients for scalable predictive coding:

**Pillar 1: Belief Maintenance**
$$q_t(\mathbf{z}) = \text{Gaussian Process / Particle Filter / Variational Density}$$

Gaussian processes provide non-parametric Bayesian flexibility; particle filters handle multi-modal posteriors; variational densities trade exactness for scalability.

**Pillar 2: Sequential Bayesian Updating**
$$q_t(\mathbf{z}) \propto p(\mathbf{o}_t | \mathbf{z}) \cdot q_{t-1}(\mathbf{z})$$

Recursive application of Bayes' theorem enables online, single-pass learning without re-processing entire histories.

**Pillar 3: Uncertainty-Driven Action**
$$\mathbf{a}^* = \arg\min_{\mathbf{a}} G(\mathbf{a}) \approx \arg\min_{\mathbf{a}} \mathbb{E}_{\tilde{\boldsymbol{\theta}} \sim q_t}[F(\mathbf{a}; \tilde{\boldsymbol{\theta}})]$$

Where $\tilde{\boldsymbol{\theta}}$ is sampled from the posterior using the ellipsoidal decomposition framework for near-exact i.i.d. sampling.

### 4.2 Ellipsoidal Decomposition for Exact Sampling

The ellipsoidal decomposition provides the first practical method for exact i.i.d. sampling from arbitrary posteriors, solving the inference problem that has long plagued Bayesian brain models:

$$\tilde{\boldsymbol{\theta}} \sim q_t(\boldsymbol{\theta}) \quad \text{(exact i.i.d. draws via ellipsoidal decomposition)}$$

This eliminates MCMC mixing issues that would otherwise compromise theoretical guarantees of Thompson sampling and active inference.

### 4.3 Recursive Gaussian Processes for Deep Hierarchy

For deep hierarchical generative models, Recursive Gaussian Processes (RGPs) provide:

$$q^{(l)}(\mathbf{z}^{(l)}) = \text{GP}(\mu^{(l)}, k^{(l)}) \quad \text{conditioned on } q^{(l+1)}(\mathbf{z}^{(l+1)})$$

RGPs preserve flexibility through layer-specific GP activations, variable selection mechanisms, and a look-up table approximation that makes inference both exact (conditional on the table) and scalable.

______________________________________________________________________

## 5. Prediction Error Minimization Dynamics

### 5.1 Prediction Error Decomposition

Total prediction error is decomposed along multiple axes:

$$\mathcal{E}_{\text{total}} = \underbrace{\mathcal{E}_{\text{sensory}}}_{\text{observation mismatch}} + \underbrace{\mathcal{E}_{\text{prior}}}_{\text{prior violation}} + \underbrace{\mathcal{E}_{\text{causal}}}_{\text{causal structure}} + \underbrace{\mathcal{E}_{\text{temporal}}}_{\text{temporal dynamics}}$$

### 5.2 Precision-Weighted Prediction Errors

Each prediction error is weighted by its estimated precision (inverse variance):

$$\tilde{\epsilon}^{(l)} = \Pi^{(l)} \cdot \epsilon^{(l)}$$

Where $\Pi^{(l)} = \text{diag}(\sigma^{(l)^{-2}})$ is the precision matrix. High-precision (reliable) prediction errors have greater influence on model updates; low-precision (noisy) errors are down-weighted.

### 5.3 Attention as Precision Optimization

Precision optimization implements attention: the system allocates attentional resources by adjusting the gain on prediction error units:

$$\text{High precision} \implies \text{High attention} \implies \text{Strong model update}$$
$$\text{Low precision} \implies \text{Low attention} \implies \text{Weak model update}$$

This bridges the Predictive Coding Framework with the Attention Selection Architecture.

______________________________________________________________________

## 6. Energy-Based Formulation

### 6.1 Hierarchical Energy-Based Model (IM-LEPP)

Drawing from IM-LEPP (Integrated Multimodal Latent Energy-based Predictive Processing, arXiv:2608.12398, 2026), AMOS models cognition as latent states flowing through learned energy landscapes:

$$E(\mathbf{z}; \mathbf{o}) = -\ln p(\mathbf{o}, \mathbf{z}) = -\ln p(\mathbf{o} | \mathbf{z}) - \ln p(\mathbf{z})$$

Cognition as diffusion: the system performs Langevin dynamics on the energy surface:

$$\mathbf{z}_{t+1} = \mathbf{z}_t - \frac{\epsilon}{2} \nabla_{\mathbf{z}} E(\mathbf{z}_t; \mathbf{o}) + \sqrt{\epsilon} \cdot \boldsymbol{\xi}_t$$

Where $\boldsymbol{\xi}_t \sim \mathcal{N}(0, I)$ is the diffusion noise.

### 6.2 Hub-and-Spoke Architecture

The IM-LEPP hub-and-spoke model grounds AMOS's multimodal integration:

```text
VISUAL PIPELINE  ──────→ ┌──────────┐ ←────── LANGUAGE PIPELINE
SCENE PIPELINE   ──────→ │ AMODAL   │ ←────── AUDITORY PIPELINE
PROPRIOCEPTIVE   ──────→ │   HUB    │ ←────── SYSTEM TELEMETRY
                          └──────────┘
                               ↓
                     CONDITIONED PREDICTIONS
                     (each pipeline's prediction
                      is conditioned by hub state,
                      preserving pipeline identity
                      while reflecting multimodal context)
```

Each pipeline's prediction is **conditioned by** rather than overwritten by the current hub state:

$$\hat{\mathbf{o}}_{\text{vis}} = f_{\text{vis}}(\mathbf{z}_{\text{vis}}, \mathbf{z}_{\text{hub}}) \neq g(\mathbf{z}_{\text{hub}})$$

This preserves pipeline-specific identity while letting every prediction reflect the full multimodal context.

______________________________________________________________________

## 7. JEPA and Active Inference Correspondence

### 7.1 SIGReg as Optimal Regularizer

From "The SIGReg Objective as Variational Free Energy" (arXiv:2607.13612, 2026), the choice of anti-collapse regularizer determines whether a Joint-Embedding Predictive Architecture (JEPA) training objective is a valid variational free energy:

| Regularizer | Entropy Estimate | AIF Surprise Bound |
|-------------|-----------------|-------------------|
| VICReg | Upper bound (unsafe) | May be violated |
| LogDet | Upper bound (unsafe) | May be violated |
| PairDist | Lower bound (safe) | Preserved |
| **SIGReg** | **Gap eliminated** | **Preserved** |

Under SIGReg enforcement (isotropic-Gaussian embeddings), the JEPA objective becomes an exact information bottleneck, and the surprise bound is preserved, making latent goal costs an exact proxy for Active Inference pragmatic value.

### 7.2 Missing Component: State-Epistemic Value

The analysis identifies that no current JEPA world model computes the **state-epistemic value**—a future-state coverage signal that encourages exploration of unvisited parts of state space. This is a critical gap for fully realizing active inference in learned world models.

______________________________________________________________________

## 8. Implementation Specification

### 8.1 Predictive Coding Step

```text
FUNCTION predictive_coding_step(observation, model):
    // Forward pass: generate predictions
    predictions ← []
    FOR EACH level l from top to bottom:
        ŷ^(l) ← generative_model(z^(l+1))
        ε^(l) ← observation^(l) - ŷ^(l)
        ε_weighted^(l) ← precision^(l) * ε^(l)
        predictions.append(ŷ^(l))
    
    // Backward pass: update states
    FOR EACH level l from bottom to top:
        Δz^(l) ← learning_rate * ε_weighted^(l) * ∂z/∂ε
        z^(l) ← z^(l) + Δz^(l)
    
    // Compute total free energy
    F ← compute_free_energy(predictions, observations, prior)
    
    // Update precisions (attention)
    FOR EACH level l:
        precision^(l) ← precision^(l) + η_p * (ε^(l)^2 - precision^(l)^(-1))
    
    RETURN z_states, predictions, F, precisions
```

### 8.2 Active Inference Step

```text
FUNCTION active_inference_step(z_current, model):
    // Sample parameters from posterior
    θ_tilde ← ellipsoidal_decompose(posterior)
    
    // Evaluate EFE for candidate actions
    candidate_actions ← generate_action_candidates(z_current)
    G_values ← []
    FOR EACH a in candidate_actions:
        z_predicted ← model.predict(z_current, a, θ_tilde)
        G ← pragmatic_value(z_predicted) + epistemic_value(z_predicted, posterior)
        G_values.append(G)
    
    // Select action that minimizes EFE
    a_optimal ← candidate_actions[argmin(G_values)]
    
    RETURN a_optimal, min(G_values)
```

______________________________________________________________________

## 9. Invariants

```text
PREDICTION_ERROR     ≠ EVIDENCE_OF_FAILURE
FREE_ENERGY          ≠ THERMODYNAMIC_ENERGY
PRECISION            ≠ CONFIDENCE
ACTIVE_INFERENCE     ≠ IMPULSIVE_ACTION
GENERATIVE_MODEL     ≠ REALITY
VARIATIONAL_FAMILY   ≠ TRUE_POSTERIOR
ELBO                 ≠ LOG_LIKELIHOOD
```

1. **Anti-Conflation:** Free energy minimization is a mathematical optimization, not a claim about thermodynamic or biological energy.
2. **Precision ≠ Truth:** High precision indicates the system's estimate of reliability, not objective truth.
3. **Active Inference ≠ Unconstrained Action:** EFE-minimizing actions are proposals subject to control-plane authorization.
4. **Fail-Closed on Model Degradation:** When free energy exceeds sustained threshold, the system enters reduced-capability mode.

______________________________________________________________________

## 10. 2026 Research Citations

| Citation | Contribution |
|----------|-------------|
| Bhattacharya et al., Bayesian Reflex (arXiv:2608.00492, 2026) | Scalable predictive coding via ellipsoidal decomposition, recursive Gaussian processes, and derivative-aware Bayesian optimization |
| Duan et al., Active Predictive Coding (AAAI 2026, PMLR 308) | Unified multi-modal intelligence via hierarchical APC for vision, navigation, language, and action |
| IM-LEPP (arXiv:2608.12398, 2026) | Hierarchical energy-based model of multimodal cognition with hub-and-spoke architecture |
| SIGReg as Variational Free Energy (arXiv:2607.13612, 2026) | Formal correspondence between JEPA training objectives and Active Inference free energy |
| Higher-Level Cognition Under PP (Springer, 2026) | Structural representations and grounded cognition extending predictive processing to abstract reasoning |

______________________________________________________________________

## 11. RSCF Contract and Gaps

```yaml
RSCF:
  node_id: amos_05_cognitive_organism_06_world_model_predictive_coding_framework
  node_type: framework
  claim_class: AMOS_MODEL
  state: DERIVED
  H:
    identity: "Predictive Coding Framework"
    role: "Prediction-error minimization and free energy principle for perception, learning, and action"
  M:
    pillars: [belief_maintenance, sequential_updating, uncertainty_driven_action]
    mechanisms: [precision_weighting, hierarchical_prediction_error, active_inference, energy_based_diffusion]
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
    independent_validation: NOT_ESTABLISHED
  executable_binding: NOT_ESTABLISHED
```

**Gaps / promotion conditions:**

- [ ] typed schema bound and validated for runtime ingestion
- [ ] free energy computation benchmarked on controlled environments
- [ ] precision estimation validated against known-noise conditions
- [ ] active inference tested on navigation and manipulation tasks
- [ ] JEPA correspondence verified empirically
- [ ] validation receipt: [[25_COGNITIVE_MATRIX/11_VALIDATION/ROUTING_POLICY_VALIDATION_RECEIPT|ROUTING_POLICY_VALIDATION_RECEIPT]]

______________________________________________________________________

## 12. Cross-Plane Bindings

- **Governing canon:** [[01_CANON/03_COGNITION_CANON/COGNITIVE_ORGANISM_CANON|COGNITIVE_ORGANISM_CANON]]
- **Parent model:** [[05_COGNITIVE_ORGANISM/06_WORLD_MODEL/INTERNAL_WORLD_MODEL|INTERNAL_WORLD_MODEL]]
- **Prediction engine:** [[05_COGNITIVE_ORGANISM/PREDICTION_ENGINE|PREDICTION_ENGINE]]
- **Attention coupling:** [[05_COGNITIVE_ORGANISM/ATTENTION_ENGINE|ATTENTION_ENGINE]] (precision = attention gain)
- **Homeostasis link:** [[05_COGNITIVE_ORGANISM/HOMEOSTASIS_ENGINE|HOMEOSTASIS_ENGINE]] (free energy as health metric)
- **Metacognitive audit:** [[05_COGNITIVE_ORGANISM/METACOGNITIVE_ENGINE|METACOGNITIVE_ENGINE]]
- **Kernel anchors:** [[02_KERNEL/01_META_LOGIC/K_META_LOGIC|K_META_LOGIC]]]]

______________________________________________________________________

**MOC:** [[05_COGNITIVE_ORGANISM/06_WORLD_MODEL/06_WORLD_MODEL_MOC|06_WORLD_MODEL_MOC]] · [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
