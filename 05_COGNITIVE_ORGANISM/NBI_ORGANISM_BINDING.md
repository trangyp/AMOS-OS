---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Nbi Organism Binding
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

# NBI Organism Binding

## 0. Executive Specification

The **NBI Organism Binding** formalizes **Neurobiological Intelligence (NBI)** within the AMOS Cognitive Organism plane (`05_COGNITIVE_ORGANISM`). NBI represents the neuromorphic, synaptically plastic, and spiking computation substrate of UBI, executing discrete-time and continuous spike-train transformations across cortical microcircuits.

```text
+---------------------------------------------------------------------------------------+
|                       NBI: NEUROBIOLOGICAL INTELLIGENCE ARCHITECTURE                  |
|                                                                                       |
|   ┌──────────────────────────┐     ┌───────────────────────────┐     ┌──────────────┐ |
|   │ SPIKING NEURAL DYNAMICS  │ <-> │ DENDRITIC MICROCOMPUTING  │ <-> │ STDP PLASTIC │ |
|   │ • Leaky Integrate & Fire │     │ • Multi-compartment Trees │     │ • Spike-Time │ |
|   │ • Event-Driven Telemetry │     │ • Non-linear NMDA Spikes  │     │ • Homeostatic│ |
|   │ • Refractory Boundaries  │     │ • Sub-linear Attenuation  │     │ • Metaplastic│ |
|   └──────────────────────────┘     └───────────────────────────┘     └──────────────┘ |
+---------------------------------------------------------------------------------------+
                                           │
                        ┌──────────────────┴──────────────────┐
                        ▼                                     ▼
      ┌──────────────────────────────────┐  ┌──────────────────────────────────┐
      │     CANONICAL MICROCIRCUITS      │  │     CROSS-MODAL UBI COUPLING     │
      │ • Layer 4: Sensory Input Thalamus│  │ • Coupled to NEI Emotional Drive │
      │ • Layer 2/3: Predictive Coding   │  │ • Regulated by SI Energy Budget  │
      │ • Layer 5: Motor Action / Output │  │ • Aligned with BEI Bioelectric   │
      │ • Layer 6: Corticothalamic Feed  │  │ • Bound to 04_RUNTIME Scheduler  │
      └──────────────────────────────────┘  └──────────────────────────────────┘
```

---

## 1. Spiking Neural Network (SNN) Dynamics

NBI models neuronal ensembles using generalized Leaky Integrate-and-Fire (LIF) dynamics with dynamic threshold adaptation, grounded in neuromorphic BCI decoding (grounded in [arXiv:2410.03533v1](file:///Users/mac/Desktop/_Arxiv/Arvix/2024/2024-10/2410.03533v1_Multiscale_fusion_enhanced_spiking_neural_network_for_invasive_BCI_neural_signal.md)):

### 1.1 Membrane Potential Evolution
$$\tau_m \frac{dv_i(t)}{dt} = -\big(v_i(t) - v_{\text{rest}}\big) + R_m \sum_j w_{ij} \sum_{t_j^k} \alpha\big(t - t_j^k\big) + I_i^{\text{ext}}(t)$$

Where:
* $v_i(t)$ is the membrane potential of neuron $i$.
* $\alpha(t) = \frac{t}{\tau_s} \exp\left(1 - \frac{t}{\tau_s}\right) \Theta(t)$ is the post-synaptic current alpha-kernel.
* $t_j^k$ is the arrival time of the $k$-th spike from presynaptic neuron $j$.

### 1.2 Spike Generation & Refractory State
A spike $S_i(t) = 1$ is emitted when $v_i(t)$ crosses dynamic threshold $\vartheta_i(t)$:

$$S_i(t) = \Theta\big(v_i(t) - \vartheta_i(t)\big)$$

$$v_i(t^+) = v_{\text{reset}} \quad \text{for } t \in [t_{\text{spike}}, t_{\text{spike}} + \tau_{\text{ref}}]$$

$$\tau_\vartheta \frac{d\vartheta_i}{dt} = -(\vartheta_i - \vartheta_0) + \beta_\vartheta S_i(t)$$

Dynamic thresholding implements intrinsic adaptation, preventing runaway excitation during sensory surges.

---

## 2. Multi-Compartment Dendritic Computing

Rather than treating neurons as point processors, NBI implements active dendritic trees capable of solving linearly non-separable operations (e.g., XOR) within single neurons:

### 2.1 Dendritic Branch Dynamics
For dendritic compartment $d$ on neuron $i$:

$$C_d \frac{dV_d}{dt} = -G_L^d (V_d - E_L) + G_{a}^{d \to \text{soma}} (V_{\text{soma}} - V_d) + \sum_{k \in \text{syn}(d)} g_k(t)(E_k - V_d) + I_{\text{NMDA}}(V_d)$$

Where NMDA receptor-mediated voltage-dependent non-linear amplification is modeled as:

$$I_{\text{NMDA}}(V_d) = g_{\text{NMDA}}(t) \frac{V_d - E_{\text{NMDA}}}{1 + \frac{[\text{Mg}^{2+}]_o}{3.57} \exp(-0.062 V_d)}$$

This non-linearity enables localized branch-specific coincidence detection and logical gating prior to somatic integration.

---

## 3. Synaptic Plasticity & Homeostatic Scaling

### 3.1 Spike-Timing-Dependent Plasticity (STDP)
Synaptic weights evolve based on millisecond-level spike timing:

$$\frac{dw_{ij}}{dt} = \eta_{\text{STDP}} \left[ A_+ \exp\left(-\frac{\Delta t}{\tau_+}\right) \Theta(\Delta t) - A_- \exp\left(\frac{\Delta t}{\tau_-}\right) \Theta(-\Delta t) \right] + \xi_{\text{homeo}}$$

Where $\Delta t = t_i^{\text{post}} - t_j^{\text{pre}}$.

### 3.2 Synaptic Scaling & Metaplasticity
To maintain long-term stability and prevent saturation:

$$\xi_{\text{homeo}} = \gamma_{\text{scale}} w_{ij} \left( r_{\text{target}} - \bar{r}_i \right)$$

Where $\bar{r}_i$ is the low-pass filtered firing rate of postsynaptic neuron $i$ over an extended temporal window ($10\text{ s} \le \tau_{\text{scale}} \le 100\text{ s}$).

---

## 4. Canonical Cortical Microcircuit Architecture

NBI organizes neuronal populations into modular canonical microcircuits mimicking mammalian neocortex:

```text
Thalamic Sensory Afferents
          │
          ▼
   [ LAYER 4: GRANULAR INPUT ] (Spike-filtering & sensory de-noising)
          │
          ▼
   [ LAYER 2/3: SUPRAGRANULAR ] (Associative feature binding & prediction residuals)
          │
          ├───────────────────────────────┐
          ▼                               ▼
   [ LAYER 5: INFRAGRANULAR ]    [ CORTICO-CORTICAL INTER-COLUMN ]
   (Action command emission)     (Lateral contextual modulation)
          │
          ▼
   [ LAYER 6: CORTICOTHALAMIC ] (Top-down feedback gain control)
```

---

## 5. Epistemic Safety & Fail-Closed Bounds

```text
NBI_SPIKE_BURST != FACTUAL_VERIFICATION
SYNAPTIC_WEIGHT != ETHICAL_AUTHORITY
HOMEOSTATIC_DRIFT -> REVERT_TO_SAFE_KERNEL
```

1. **Deterministic Containment:** NBI computations provide high-speed pattern recognition and temporal prediction. They cannot authorize state transitions in `12_STATE` or `03_CONTROL_PLANE`.
2. **Epileptiform Quenching:** If average firing rate across any microcircuit exceeds $r_{\text{critical}} = 80\text{ Hz}$ for more than $50\text{ ms}$, the engine injects GABAergic inhibitory clamping current, logging an `NBI_EPILEPTIFORM_HALT` receipt to `17_OBSERVABILITY`.

---

## 6. Cross-Plane Bindings

- **Governed by Canon:** [[01_CANON/03_COGNITION_CANON/AMOS_FULL_BRAIN_OS_CANON|FULL_BRAIN_OS_CANON]].
- **UBI Framework:** [[05_COGNITIVE_ORGANISM/UBI_ORGANISM_BINDING|UBI_ORGANISM_BINDING]].
- **Runtime Binding:** [[05_COGNITIVE_ORGANISM/FULL_BRAIN_OS_RUNTIME_BINDING|FULL_BRAIN_OS_RUNTIME_BINDING]].
- **Active Inference:** [[05_COGNITIVE_ORGANISM/PREDICTION_ENGINE|PREDICTION_ENGINE]].
- **Grounded Evidence:** [[00_ROOT/ARXIV_RSCF_KNOWLEDGE_NODE|ARXIV_RSCF_KNOWLEDGE_NODE]].

---

RSCF-NODE
node_id: amos_05_cognitive_organism_nbi_organism_binding
node_type: binding
domain: COGNITION
path: 05_COGNITIVE_ORGANISM/NBI_ORGANISM_BINDING.md
claim_class: AMOS_MODEL
rscf_state: active_specification
canonical_status: CANONICAL_BINDING
RSCF-RELATIONS:
  - INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
  - INDEXED_BY: [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]]
  - GOVERNED_BY: [[01_CANON/03_COGNITION_CANON/AMOS_FULL_BRAIN_OS_CANON|FULL_BRAIN_OS_CANON]]
  - BOUND_TO: [[05_COGNITIVE_ORGANISM/UBI_ORGANISM_BINDING|UBI_ORGANISM_BINDING]]
  - BOUND_TO: [[05_COGNITIVE_ORGANISM/FULL_BRAIN_OS_RUNTIME_BINDING|FULL_BRAIN_OS_RUNTIME_BINDING]]
