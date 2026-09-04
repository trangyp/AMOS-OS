---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Learning Adaptation Engine
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

# Learning Adaptation Engine — Cognition Organ

> **Status:** `ACTIVE_SPECIFICATION` · **AMOS Core target:** `v4.4`
> **Origin architect / steward:** Trang Phan
> **Segment:** `05_COGNITIVE_ORGANISM/04_COGNITION`
> **Conclusion class:** `AMOS_MODEL` · **Canonical status:** `SOURCE_GROUNDED_CANON_CANDIDATE`

______________________________________________________________________

## 1. Purpose

The **Learning Adaptation Engine** governs how AMOS acquires, retains, transfers, and meta-cognitively regulates knowledge across task encounters, domain shifts, and distribution changes. It implements online learning (single-pass adaptation from streaming data), meta-learning (learning how to learn), and transfer learning (cross-domain knowledge reuse) mechanisms within the cognitive organism.

```text
TASK EXPERIENCES + OBSERVATIONS + OUTCOME FEEDBACK
                        |
    ┌───────────────────┼───────────────────┐
    │    LEARNING ADAPTATION ENGINE          │
    │                                        │
    │  ┌──────────┐ ┌──────────┐ ┌────────┐│
    │  │ ONLINE   │ │ META-    │ │TRANSFER││
    │  │ LEARNING │ │ LEARNING │ │ LEARNING││
    │  └──────────┘ └──────────┘ └────────┘│
    │         ↕           ↕          ↕      │
    │    ┌──────────────────────────────┐   │
    │    │   STABILITY-PLASTICITY      │   │
    │    │   ARBITRATION               │   │
    │    └──────────────────────────────┘   │
    └───────────────────┼───────────────────┘
                        ↓
    UPDATED KNOWLEDGE BASE + META-LEARNING STATE (RSCF: DERIVED)
                        ↓
         MEMORY ENGINE / REASONING / ACTION SELECTION
```

______________________________________________________________________

## 2. Online Learning Subsystem

### 2.1 Stability-Plasticity Dilemma

The core challenge of online learning is balancing retention of previously learned knowledge (stability) against acquisition of new knowledge (plasticity). Drawing from MANGO (Meta-Adaptive Network Gradient Optimization, arXiv:2605.19080, 2026), AMOS implements gradient-gating and meta-learned regularization:

**Gradient-Gating:** Parameter updates are selectively scaled based on sensitivity:

$$\theta_i^{(t+1)} = \theta_i^{(t)} - \eta \cdot g_i(\theta) \cdot \nabla_{\theta_i} \mathcal{L}_t$$

Where $g_i(\theta) \in (0, 1]$ is the gate value:

$$g_i(\theta) = \frac{|\theta_i|}{|\theta_i| + \epsilon + \lambda_i \cdot |\nabla_{\theta_i} \mathcal{L}_{\text{replay}}|}$$

Parameters with high gradient impact on replay (past knowledge) receive smaller updates, protecting them from catastrophic forgetting.

**Meta-Leaned Regularization:** Layer-wise stability coefficients $\lambda_i$ are learned via bi-level meta-optimization:

$$\lambda_i^{*} = \arg\min_{\lambda_i} \mathcal{L}_{\text{replay}}(\theta^{(t)} - \eta \cdot g(\theta, \lambda) \cdot \nabla \mathcal{L}_t)$$

This directly measures the effect of each parameter update on past knowledge, with replay serving as both training signal and forgetting evaluator.

### 2.2 Continual Learning Protocol

```text
FUNCTION online_learn(new_data, replay_buffer):
    // Phase 1: Gradient-gated parameter update
    gradients ← compute_gradients(new_data)
    gated_gradients ← apply_gradient_gating(gradients, sensitivity_map)
    θ ← θ - η * gated_gradients
    
    // Phase 2: Meta-regularization feedback
    replay_loss_before ← compute_replay_loss(θ_old, replay_buffer)
    replay_loss_after ← compute_replay_loss(θ, replay_buffer)
    λ ← update_stability_coefficients(λ, replay_loss_before, replay_loss_after)
    
    // Phase 3: Buffer management
    update_replay_buffer(replay_buffer, new_data, reservoir_sampling)
    
    // Phase 4: Backward transfer check
    IF replay_loss_after < replay_loss_before:
        signal POSITIVE_BACKWARD_TRANSFER  // Rare: new knowledge improves old
    
    RETURN θ, λ, replay_buffer
```

### 2.3 Positive Backward Transfer

A distinctive feature of MANGO is its ability to achieve positive backward transfer (BWT), where learning new domain knowledge improves performance on previously learned tasks. On the CLEAR-10 benchmark, MANGO achieves +15.12% BWT with buffer size 2000, indicating that meta-learned regularization enables learning of generalizable representations rather than mere task-specific memorization.

______________________________________________________________________

## 3. Meta-Learning Subsystem

### 3.1 Meta-Cognitive Memory Abstraction (MCMA)

From Liang et al. (ACL Findings, 2026), meta-learning is implemented as learning how to structure, abstract, and reuse memories. The MCMA framework decouples task execution from memory management:

```text
MEMORY COPILOT (Meta-Level)
    ├── Determines how memories are structured (tree, chain, NL)
    ├── Determines abstraction granularity (episodic → semantic)
    ├── Determines when memory is transferable
    └── Trained via Direct Preference Optimization (DPO)

TASK MODEL (Frozen)
    └── Executes actions using retrieved memories
```

**Abstraction Hierarchy:**

| Level | Content | Transferability |
|-------|---------|----------------|
| Level 1 (Episodic) | Concrete interaction trajectories | Low: domain-specific |
| Level 2 (Procedural) | Abstracted task procedures | Medium: similar tasks |
| Level 3 (Semantic) | Domain-general knowledge schemas | High: cross-domain |

When no stored memory is transferable to a novel domain, the memory copilot itself is transferred—preserving the learned abstraction capability rather than specific knowledge.

### 3.2 Automated Meta-Learning of Memory Designs (ALMA)

From Xiong et al. (arXiv:2602.07755, 2026), AMOS implements open-ended exploration of memory architectures:

```text
ALGORITHM: ALMA Meta-Agent Loop
1. Initialize archive with empty memory design template
2. REPEAT:
   a. Sample candidate designs from archive (proportional to success rate)
   b. Meta Agent reflects on performance outcomes
   c. Meta Agent proposes new memory design (as executable code)
   d. Evaluate design in sandbox environment
   e. If error: Meta Agent self-debugs (up to 3 retries)
   f. Add design + evaluation to archive
3. UNTIL budget exhausted
```

The search space includes database schemas, retrieval mechanisms, and update strategies expressed as executable code, enabling discovery of memory paradigms beyond human intuition.

### 3.3 Self-Evolving Meta-Memory (MetaMem)

From Xin et al. (ACL Findings, 2026), the meta-memory layer learns transferable knowledge utilization experiences:

$$\mathcal{E}_{t+1} = \mathcal{E}_t + \alpha \cdot \Delta\mathcal{E}(\text{SelfReflect}(r_t, y_t, \mathcal{E}_t))$$

Where:
- $\mathcal{E}$: accumulated meta-memory (set of knowledge utilization experience units)
- $r_t$: reasoning response at time $t$
- $y_t$: correctness-based reward signal
- $\Delta\mathcal{E}$: proposed update to meta-memory

Over training, the proportion of general (task-agnostic) experience units increases from ~65% to >80%, indicating convergence toward broadly applicable reasoning strategies.

### 3.4 Metacognitive Consolidation

From Zhuang et al. (ACL 2026), metacognitive experience from past reasoning episodes is consolidated into reusable meta-knowledge via hierarchical, multi-timescale update:

```text
INSTANCE-LEVEL TRACES
    │ (reasoning, monitoring, control roles)
    ↓
EPISODIC META-TRACES
    │ (attributed failure modes, effort patterns)
    ↓
HIERARCHICAL CONSOLIDATION
    │ (gradual formation of evolving meta-knowledge)
    ↓
REUSABLE META-KNOWLEDGE
    → Guides future reasoning strategy selection
```

______________________________________________________________________

## 4. Transfer Learning Subsystem

### 4.1 Domain Similarity Assessment

Before transferring knowledge across domains, the engine quantifies domain similarity using the Representation-Transferability metric:

$$\rho_{\text{transfer}}(\mathcal{D}_{\text{source}}, \mathcal{D}_{\text{target}}) = 1 - \text{MMD}^2(\phi(\mathcal{D}_{\text{source}}), \phi(\mathcal{D}_{\text{target}}))$$

Where MMD is the Maximum Mean Discrepancy in a shared representation space $\phi$.

### 4.2 Transfer Protocol

```text
FUNCTION transfer_knowledge(source_domain, target_domain):
    // Step 1: Assess transferability
    ρ ← compute_transferability(source_domain, target_domain)
    
    IF ρ > τ_high:
        // Direct transfer: reuse source representations
        RETURN direct_transfer(source_domain.representations, target_domain)
    ELIF ρ > τ_low:
        // Adapted transfer: fine-tune with target data
        RETURN adapted_transfer(source_domain.representations, target_domain.data)
    ELSE:
        // Copilot transfer: transfer the abstraction ability itself
        RETURN copilot_transfer(source_domain.meta_copilot, target_domain)
```

### 4.3 Negative Transfer Detection

The engine actively monitors for negative transfer—cases where transferred knowledge degrades target domain performance:

$$\text{NegativeTransfer} \iff \text{Acc}_{\text{with\_transfer}} < \text{Acc}_{\text{without\_transfer}} - \epsilon_{\text{margin}}$$

When detected, the system automatically reverts to target-only learning and logs the failure mode for future transfer governance.

______________________________________________________________________

## 5. Stability-Plasticity Arbitration

### 5.1 Adaptive Balance Parameter

The global stability-plasticity balance is governed by a meta-parameter $\Psi \in [0, 1]$:

$$\Psi = \sigma\left(\beta_0 + \beta_1 \cdot \text{TaskNovelty} + \beta_2 \cdot \text{DistributionShift} - \beta_3 \cdot \text{ForgettingRate}\right)$$

Where $\sigma$ is the sigmoid function:
- High $\Psi$ → high plasticity (novel environment, novel tasks)
- Low $\Psi$ → high stability (known environment, critical tasks)

### 5.2 Forgetting Rate Monitoring

The engine maintains a running estimate of catastrophic forgetting:

$$\text{FR}_t = \frac{1}{K} \sum_{k=1}^{K} \max(0, \text{Acc}_k^{\text{peak}} - \text{Acc}_k^{\text{current}})$$

Where $K$ is the number of previously learned tasks. When $\text{FR}_t$ exceeds threshold $\tau_{\text{FR}}$, the engine triggers stability mode, increasing regularization and reducing learning rate.

______________________________________________________________________

## 6. Implementation Specification

```text
FUNCTION learning_adaptation_step(experience, system_state):
    // Determine learning mode
    mode ← select_mode(system_state.task_novelty, system_state.dist_shift)
    
    SWITCH mode:
        CASE ONLINE:
            θ, λ, buffer ← online_learn(experience, replay_buffer)
        CASE META:
            meta_knowledge ← metacognitive_consolidation(experience, meta_traces)
            strategy ← select_reasoning_strategy(meta_knowledge)
        CASE TRANSFER:
            domain_sim ← assess_domain_similarity(current_domain, experience.domain)
            IF domain_sim > τ_high:
                apply_direct_transfer(...)
            ELIF domain_sim > τ_low:
                apply_adapted_transfer(...)
            ELSE:
                apply_copilot_transfer(...)
    
    // Update stability-plasticity balance
    Ψ ← compute_balance(task_novelty, dist_shift, forgetting_rate)
    apply_balance_regulation(Ψ)
    
    // Monitor for negative transfer
    IF negative_transfer_detected():
        revert_and_log(...)
    
    RETURN updated_knowledge_base, meta_state
```

______________________________________________________________________

## 7. Invariants

```text
LEARNING       ≠ UNDERSTANDING
TRANSFER       ≠ GUARANTEE
PLASTICITY     ≠ INSTABILITY
STABILITY      ≠ RIGIDITY
META_LEARNING  ≠ OBJECT_LEARNING
FORGETTING     ≠ INTENTIONAL_DELETION
ACCUMULATION   ≠ QUALITY
```

1. **Anti-Memorization Gate:** The engine must not merely accumulate experiences without abstraction; raw trajectory storage without structured representation is prohibited.
2. **Forgetting Audit:** Every online learning step must report its estimated forgetting rate. Unmonitored forgetting is a system fault.
3. **Transfer Provenance:** Every transferred knowledge unit carries source domain provenance and transfer confidence.
4. **Fail-Closed on Novelty:** When domain similarity cannot be computed (insufficient data), the engine defaults to no-transfer mode.

______________________________________________________________________

## 8. 2026 Research Citations

| Citation | Contribution |
|----------|-------------|
| MANGO (arXiv:2605.19080, 2026) | Meta-adaptive gradient-gating and meta-learned regularization for online continual learning; positive backward transfer |
| MCMA (ACL Findings, 2026) | Meta-cognitive memory abstraction treating memory management as a learnable skill; DPO-trained memory copilot |
| ALMA (arXiv:2602.07755, 2026) | Automated meta-learning of memory designs via open-ended code search by a Meta Agent |
| MetaMem (ACL Findings, 2026) | Self-evolving meta-memory for transferable knowledge utilization experiences |
| Metacognitive Consolidation (ACL 2026) | Hierarchical multi-timescale consolidation of meta-reasoning experience into reusable meta-knowledge |

______________________________________________________________________

## 9. RSCF Contract and Gaps

```yaml
RSCF:
  node_id: amos_05_cognitive_organism_04_cognition_learning_adaptation_engine
  node_type: engine
  claim_class: AMOS_MODEL
  state: DERIVED
  H:
    identity: "Learning Adaptation Engine"
    role: "Online learning, meta-learning, and transfer learning mechanisms for continuous adaptation"
  M:
    subsystems: [online_learning, meta_learning, transfer_learning]
    key_mechanisms: [gradient_gating, meta_regularization, memory_abstraction, copilot_transfer]
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
    independent_validation: NOT_ESTABLISHED
  executable_binding: NOT_ESTABLISHED
```

**Gaps / promotion conditions:**

- [ ] typed schema bound and validated for runtime ingestion
- [ ] online learning tested on AMOS-specific streaming data distributions
- [ ] meta-learning copilot trained and validated on multi-task benchmarks
- [ ] transfer learning domain similarity metrics calibrated
- [ ] negative transfer detection and recovery verified
- [ ] validation receipt: [[25_COGNITIVE_MATRIX/11_VALIDATION/ROUTING_POLICY_VALIDATION_RECEIPT|ROUTING_POLICY_VALIDATION_RECEIPT]]

______________________________________________________________________

## 10. Cross-Plane Bindings

- **Governing canon:** [[01_CANON/03_COGNITION_CANON/COGNITIVE_ORGANISM_CANON|COGNITIVE_ORGANISM_CANON]]
- **Parent engine:** [[05_COGNITIVE_ORGANISM/COGNITION_ENGINE|COGNITION_ENGINE]]
- **Memory integration:** [[05_COGNITIVE_ORGANISM/MEMORY_ENGINE|MEMORY_ENGINE]]
- **Metacognitive coupling:** [[05_COGNITIVE_ORGANISM/METACOGNITIVE_ENGINE|METACOGNITIVE_ENGINE]]
- **Reasoning feedback:** [[05_COGNITIVE_ORGANISM/04_COGNITION/REASONING_INFERENCE_ENGINE|REASONING_INFERENCE_ENGINE]]
- **Homeostasis interface:** [[05_COGNITIVE_ORGANISM/HOMEOSTASIS_ENGINE|HOMEOSTASIS_ENGINE]]
- **Control-plane gate:** [[03_CONTROL_PLANE/CONTROL_PLANE_README|CONTROL_PLANE_README]]

______________________________________________________________________

**MOC:** [[05_COGNITIVE_ORGANISM/04_COGNITION/04_COGNITION_MOC|04_COGNITION_MOC]] · [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
