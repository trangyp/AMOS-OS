---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Attention Selection Architecture
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

# Attention Selection Architecture — Cognition Organ

> **Status:** `ACTIVE_SPECIFICATION` · **AMOS Core target:** `v4.4`
> **Origin architect / steward:** Trang Phan
> **Segment:** `05_COGNITIVE_ORGANISM/04_COGNITION`
> **Conclusion class:** `AMOS_MODEL` · **Canonical status:** `SOURCE_GROUNDED_CANON_CANDIDATE`

______________________________________________________________________

## 1. Purpose

The **Attention Selection Architecture** defines the computational mechanisms by which AMOS directs, modulates, and selects among competing cognitive stimuli, internal representations, and task-relevant signals. It specifies how saliency maps are constructed, how competitive inhibition suppresses irrelevant activations, and how temporal attention windows gate the flow of information into working memory and downstream reasoning engines.

This architecture extends the higher-level [ATTENTION_ENGINE](../ATTENTION_ENGINE.md) contract with concrete algorithmic mechanisms grounded in 2026 neuroscience and machine learning research.

```text
MULTIMODAL SENSORY STREAMS + INTERNAL REPRESENTATIONS
                         |
    ┌────────────────────┼────────────────────┐
    │          ATTENTION SELECTION ARCHITECTURE│
    │                                          │
    │  ┌──────────────┐  ┌──────────────────┐ │
    │  │ SALIENCY MAP  │  │ COMPETITIVE      │ │
    │  │ CONSTRUCTION  │→ │ INHIBITION FIELD │ │
    │  └──────────────┘  └──────────────────┘ │
    │           |                |              │
    │  ┌──────────────────────────────────────┐│
    │  │     TEMPORAL ATTENTION WINDOW GATE   ││
    │  └──────────────────────────────────────┘│
    └────────────────────┬────────────────────┘
                         ↓
           FOCUSED ATTENTION VECTOR (RSCF: DERIVED)
                         ↓
              COGNITION / REASONING / MEMORY
```

______________________________________________________________________

## 2. Saliency Map Construction

### 2.1 Multi-Cue Saliency Integration

Following the biased competition framework (Desimone & Duncan, 1995) and validated by 2026 RIFT-EEG studies (Dynamic Competition in Early Visual Cortex, Nature Comms Biology 2026), saliency is computed as a weighted superposition of feature-specific conspicuity maps:

$$S(\mathbf{x}) = \sum_{f \in \mathcal{F}} w_f \cdot C_f(\mathbf{x}) + w_{\text{ctx}} \cdot \Gamma(\mathbf{x})$$

Where:
- $C_f(\mathbf{x})$: conspicuity at spatial location $\mathbf{x}$ for feature channel $f \in \{\text{color, orientation, motion, intensity, semantic}\}$
- $\Gamma(\mathbf{x})$: contextual modulation signal from higher cortical areas (top-down goal relevance)
- $w_f$: channel-specific weights modulated by active task envelope
- $\sum w_f = 1$ enforced by normalization

### 2.2 Inhibited Self-Attention (ISA) Mechanism

Drawing from the 2026 ISA framework (van der Wal et al., arXiv:2607.12881), AMOS implements competitive push-pull saliency computation:

$$\text{ISA}_{ij} = \alpha \cdot \text{softmax}(QK^T / \sqrt{d})_{ij} + \beta \cdot \text{softmin}(QK^T / \sqrt{d})_{ij}$$

Where $\alpha > 0$ is the excitatory weight and $\beta < 0$ is the inhibitory weight. Unlike standard attention which discards negative attention scores via softmax normalization, ISA retains and leverages negative attention scores to explicitly suppress irrelevant features and sharpen focus on objects of interest.

The attention-on-objects (AoO) metric quantifies focus quality:

$$\text{AoO} = \frac{\sum_{\mathbf{x} \in \Omega_{\text{obj}}} S(\mathbf{x})}{\sum_{\mathbf{x} \in \Omega_{\text{total}}} S(\mathbf{x})}$$

Where $\Omega_{\text{obj}}$ is the set of task-relevant object locations and $\Omega_{\text{total}}$ is the full spatial domain.

### 2.3 Bidirectional Recurrent Gating

Following Salehi et al. (Nature Communications, 2026), the saliency map is refined through bidirectional recurrent gating:

```text
         FEEDFORWARD PATHWAY (Feature Extraction)
              ┌───────────────────────┐
INPUT → [L1] → [L2] → [BOTTLENECK] → [L3] → [L4] → FEATURES
              └───────────────────────┘
                     ↕ (lateral connections)
              ┌───────────────────────┐
TOP-    → [A1] → [A2] → [A3] → [A4] → ATTENTION MAPS
DOWN            ↑
CONTEXT    DENSE RECURRENT LAYER (Working Memory)
```

Each iteration applies multiplicative gating:

$$\mathbf{f}^{(t+1)}_l = \mathbf{a}^{(t)}_l \odot g(\mathbf{f}^{(t)}_l, \mathbf{h}^{(t)}_l)$$

Where $\mathbf{a}^{(t)}_l$ is the attention map at layer $l$, $\mathbf{f}^{(t)}_l$ is the feature map, $g(\cdot)$ is the gating function, and $\odot$ denotes element-wise multiplication. This mechanism enables the system to learn inhibition of return (IOR), object binding, and top-down visual search without task-specific architectural modifications.

______________________________________________________________________

## 3. Competitive Inhibition Field

### 3.1 Lateral Inhibition Network

The competitive inhibition field implements winner-take-all (WTA) dynamics with soft normalization to prevent complete suppression of non-winning activations:

$$S_{\text{eff}}(\mathbf{x}_i) = \frac{S(\mathbf{x}_i)^\sigma}{\sum_{j \in \mathcal{N}(\mathbf{x}_i)} S(\mathbf{x}_j)^\sigma + \epsilon}$$

Where:
- $\sigma \geq 1$ controls inhibition sharpness (higher $\sigma$ → harder WTA)
- $\mathcal{N}(\mathbf{x}_i)$ is the local competitive neighborhood
- $\epsilon$ prevents division by zero and allows residual activation

### 3.2 Feedforward vs. Lateral Inhibition Balance

From SCRI (Salience by Competitive and Recurrent Interactions, Cox et al., 2022, validated in 2026), AMOS distinguishes two inhibition types:

```text
FEEDFORWARD INHIBITION:
  Signal at location i → inhibits neurons at location j (j ≠ i)
  Role: Suppresses initial distractor competition
  Governs: Initial saliency response dynamics

LATERAL INHIBITION:
  FEF neuron at location i ↔ FEF neuron at location j
  Role: Sustained competition during deliberation
  Governs: Resolution of ambiguous stimuli
```

The inhibition balance parameter $\phi \in [0, 1]$ determines the relative contribution:

$$I_{\text{total}} = \phi \cdot I_{\text{ff}} + (1 - \phi) \cdot I_{\text{lat}}$$

Higher $\phi$ values prioritize rapid initial filtering; lower values enable deeper competitive resolution for complex stimuli.

### 3.3 Distractor Suppression Dynamics

Per the 2026 RIFT study (Nature Comms Biology), competitive inhibition follows a three-phase temporal profile:

| Phase | Time Window | Mechanism | Effect |
|-------|------------|-----------|--------|
| P1: Bottom-Up Capture | 0–100ms | Salient distractor captures attentional resources | Target processing attenuated |
| P2: Active Competition | 100–250ms | Top-down control signals engage | Distractor representation declines |
| P3: Suppression | 250ms+ | Distractor suppressed below nontarget baseline | Target selection stabilized |

______________________________________________________________________

## 4. Temporal Attention Windows

### 4.1 Sliding Attention Window Model

Temporal attention is modeled as a set of overlapping windows at multiple timescales, each gated by a relevance signal:

$$W_{\text{temp}}(t; \tau) = \exp\left(-\frac{(t - t_{\text{focus}})^2}{2\tau^2}\right) \cdot R(t)$$

Where:
- $\tau$: window width (short $\tau$ = transient attention, long $\tau$ = sustained attention)
- $t_{\text{focus}}$: center of current attentional focus
- $R(t) \in [0, 1]$: relevance modulation from goal states

### 4.2 Multi-Timescale Attention Hierarchy

```text
LAYER        TIMESCALE      FUNCTION
───────────────────────────────────────────────
τ₁ (fast)    ~50ms          Transient onset response
τ₂ (medium)  ~200ms         Sustained feature selection
τ₃ (slow)    ~2s            Working memory maintenance
τ₄ (very slow) ~10s+        Task-level attentional set
```

Higher layers gate lower layers: the attentional set at $\tau_4$ modulates which transients at $\tau_1$ are propagated versus suppressed.

### 4.3 Temporal Binding Window

For cross-modal binding (e.g., associating a visual stimulus with a concurrent auditory signal), the temporal binding window is:

$$P_{\text{bind}}(v, a) = \exp\left(-\frac{|t_v - t_a|^2}{2\tau_{\text{bind}}^2}\right) \cdot \kappa(v, a)$$

Where $t_v, t_a$ are the onset times and $\kappa(v, a)$ is the cross-modal congruence score. The binding window width $\tau_{\text{bind}}$ is modulated by arousal and attentional load.

______________________________________________________________________

## 5. Mathematical Formalization

### 5.1 Joint Attention Optimization

The full attention selection problem is formalized as a constrained optimization:

$$\max_{\mathbf{a}} \quad U(\mathbf{a}, \mathbf{s}, \mathbf{g}) \quad \text{s.t.} \quad \|\mathbf{a}\|_1 \leq B, \quad a_i \geq 0 \;\forall i$$

Where:
- $\mathbf{a}$: attention allocation vector over stimuli $\mathbf{s}$
- $\mathbf{g}$: current goal state
- $U$: utility function combining saliency, goal relevance, and uncertainty
- $B$: total attention budget (bounded cognitive capacity)

The utility decomposes as:

$$U(\mathbf{a}, \mathbf{s}, \mathbf{g}) = \underbrace{\sum_i a_i \cdot S(\mathbf{x}_i)}_{\text{saliency}} + \underbrace{\lambda_g \sum_i a_i \cdot G(\mathbf{x}_i, \mathbf{g})}_{\text{goal relevance}} + \underbrace{\lambda_u \sum_i a_i \cdot H(\mathbf{x}_i)}_{\text{uncertainty}} - \underbrace{\lambda_r \sum_{i \neq j} a_i \cdot a_j \cdot \rho(i,j)}_{\text{redundancy penalty}}$$

### 5.2 Competitive Dynamics as Reaction-Diffusion

The spatial dynamics of the saliency field follow a discretized reaction-diffusion system:

$$\frac{\partial S(\mathbf{x}, t)}{\partial t} = D \nabla^2 S + f(S, \mathbf{I}) - g(S)$$

Where $D$ is the diffusion coefficient, $f(S, \mathbf{I})$ is the stimulus-driven excitation, and $g(S)$ is the local inhibition function. This formulation guarantees that the attention field converges to a stable focus under mild regularity conditions.

______________________________________________________________________

## 6. Implementation Specification

### 6.1 Algorithmic Pipeline

```text
FUNCTION attention_selection(candidates, goals, budget):
    // Phase 1: Feature-specific saliency computation
    saliency_maps ← []
    FOR EACH channel f in {color, orientation, motion, semantic}:
        C_f ← compute_conspicuity(candidates, channel=f)
        saliency_maps.append(C_f)
    
    // Phase 2: Integrated saliency map
    S ← weighted_sum(saliency_maps, weights=current_task_weights)
    
    // Phase 3: ISA-enhanced competitive inhibition
    S_inhibited ← apply_inhibited_self_attention(S, alpha=0.7, beta=-0.3)
    
    // Phase 4: Temporal window gating
    S_temporal ← apply_temporal_windows(S_inhibited, tau=multi_scale_taus)
    
    // Phase 5: Budget-constrained allocation
    a ← solve_constrained_optimization(S_temporal, goals, budget)
    
    // Phase 6: Distractor suppression
    a ← apply_lateral_inhibition(a, sigma=1.5)
    
    RETURN attention_vector: a
```

### 6.2 Performance Envelope

| Metric | Target | Rationale |
|--------|--------|-----------|
| Saliency computation latency | < 10ms per frame | Real-time perception loop |
| Inhibition convergence | < 5 iterations | Competitive dynamics settling |
| Budget compliance | Hard guarantee | No cognitive overflow |
| AoO ratio (object-relevant) | > 0.75 | ISA benchmark target |
| IOR latency | 150–300ms | Human-matched |

______________________________________________________________________

## 7. Invariants

```text
SALIENCE != TRUTH
ATTENTION_ALLOC != COMMITMENT
COMPETITIVE_WINNER != CORRECT_HYPOTHESIS
TEMPORAL_FOCUS != EPISTEMIC_PRIORITY
INHIBITION_SUPPRESSION != EVIDENCE_ABSENCE
NOVELTY != RELEVANCE
HIGH_AOo != CORRECT_DECISION
```

1. **Anti-Hallucination Gate:** High saliency or AoO must never elevate a hypothesis to observation status.
2. **Deterministic Pruning:** Attention budget overflow triggers archival of pruned signals with full provenance; signals are never silently destroyed.
3. **Inhibition-Action Firewall:** Competitive inhibition suppresses information flow but does not by itself authorize action.
4. **Fail-Closed on Saturation:** If the constrained optimization is infeasible under current resource constraints, the system signals `LOAD_SHEDDING` to [HOMEOSTASIS_ENGINE](../HOMEOSTASIS_ENGINE.md).

______________________________________________________________________

## 8. 2026 Research Citations

| Citation | Contribution |
|----------|-------------|
| van der Wal et al., arXiv:2607.12881 (2026) | Inhibited Self-Attention (ISA) mechanism using negative attention scores for sharpened focus in Vision Transformers |
| Salehi et al., Nature Communications (2026) | Bidirectional recurrent gating model unifying spatial, feature, and object-based attention; inhibition of return; emergent-attention hypothesis |
| Dynamic Competition in Early Visual Cortex, Nature Comms Biology (2026) | RIFT-EEG evidence for three-phase bottom-up/top-down attentional competition timeline in visual cortex |
| Cox et al., SCRI (2022, validated 2026) | Salience by Competitive and Recurrent Interactions model of FEF visual neuron spiking during target selection |
| Desimone & Duncan (1995), biased competition framework | Foundational computational model for competitive attentional selection |

______________________________________________________________________

## 9. RSCF Contract and Gaps

```yaml
RSCF:
  node_id: amos_05_cognitive_organism_04_cognition_attention_selection_architecture
  node_type: architecture
  claim_class: AMOS_MODEL
  state: DERIVED
  H:
    identity: "Attention Selection Architecture"
    role: "Computational mechanisms for saliency, competitive inhibition, and temporal attention gating"
  M:
    components: [saliency_map, competitive_inhibition, temporal_attention_windows]
    algorithms: [isa, bidirectional_recurrent_gating, constrained_optimization, reaction_diffusion]
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
    independent_validation: NOT_ESTABLISHED
  executable_binding: NOT_ESTABLISHED
```

**Gaps / promotion conditions:**

- [ ] typed schema bound and validated for runtime ingestion
- [ ] ISA mechanism implemented and benchmarked against standard attention
- [ ] competitive inhibition dynamics verified in multi-stimulus scenarios
- [ ] temporal attention windows calibrated against human data
- [ ] validation receipt: [[25_COGNITIVE_MATRIX/11_VALIDATION/ROUTING_POLICY_VALIDATION_RECEIPT|ROUTING_POLICY_VALIDATION_RECEIPT]]

______________________________________________________________________

## 10. Cross-Plane Bindings

- **Governing canon:** [[01_CANON/03_COGNITION_CANON/COGNITIVE_ORGANISM_CANON|COGNITIVE_ORGANISM_CANON]]
- **Parent engine:** [[05_COGNITIVE_ORGANISM/ATTENTION_ENGINE|ATTENTION_ENGINE]]
- **Upstream input:** [[05_COGNITIVE_ORGANISM/PERCEPTION_ENGINE|PERCEPTION_ENGINE]]
- **Downstream consumers:** [[05_COGNITIVE_ORGANISM/COGNITION_ENGINE|COGNITION_ENGINE]] · [[05_COGNITIVE_ORGANISM/MEMORY_ENGINE|MEMORY_ENGINE]]
- **Regulatory monitor:** [[05_COGNITIVE_ORGANISM/HOMEOSTASIS_ENGINE|HOMEOSTASIS_ENGINE]]
- **Kernel anchors:** [[02_KERNEL/K_META_LOGIC|K_META_LOGIC]]

______________________________________________________________________

**MOC:** [[05_COGNITIVE_ORGANISM/04_COGNITION/04_COGNITION_MOC|04_COGNITION_MOC]] · [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
