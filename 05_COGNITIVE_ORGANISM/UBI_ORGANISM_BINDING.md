---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Ubi Organism Binding
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

# UBI Organism Binding

## 0. Executive Specification

The **UBI Organism Binding** establishes the structural, biological, and mathematical integration of **Universal Biological Intelligence (UBI)** within the AMOS Cognitive Organism plane (`05_COGNITIVE_ORGANISM`). 

UBI unites four distinct, mutually complementary modal intelligences into an allostatically balanced cognitive organism:

```text
+---------------------------------------------------------------------------------------+
|                    UNIVERSAL BIOLOGICAL INTELLIGENCE (UBI) ARCHITECTURE               |
|                                                                                       |
|   ┌─────────────────────────────┐                     ┌───────────────────────────┐   |
|   │ NBI: NEUROBIOLOGICAL INTEL  │                     │ NEI: NEURO-ELECTROMAGNETIC│   |
|   │ • Spiking Neural Networks   │                     │ • Affective Allostasis    │   |
|   │ • Synaptic STDP Plasticity  │ <─────────────────> │ • Coherent Dipole Fields  │   |
|   │ • Dendritic Computation     │                     │ • Emotion Field Coupling  │   |
|   └──────────────┬──────────────┘                     └─────────────┬─────────────┘   |
|                  ▲                                                  ▲                 |
|                  │                 ┌──────────────────┐             │                 |
|                  │                 │ UBI HOMEOSTASIS  │             │                 |
|                  │                 │ & FREE ENERGY    │             │                 |
|                  │                 └──────────────────┘             │                 |
|                  ▼                                                  ▼                 |
|   ┌──────────────┴──────────────┐                     ┌─────────────┴─────────────┐   |
|   │ SI: SOMATIC INTELLIGENCE    │                     │ BEI: BIOELECTROMAGNETIC   │   |
|   │ • Interoception / Visceral  │ <─────────────────> │ • Morphogenetic Gradients │   |
|   │ • Vagal / Autonomic Tone    │                     │ • Membrane Potentials     │   |
|   │ • Metabolic Energy Budgets  │                     │ • Pattern Regeneration    │   |
|   └─────────────────────────────┘                     └───────────────────────────┘   |
+---------------------------------------------------------------------------------------+
                                           │
                        ┌──────────────────┴──────────────────┐
                        ▼                                     ▼
      ┌──────────────────────────────────┐  ┌──────────────────────────────────┐
      │     EPISTEMIC SAFETY FIREWALL    │  │    DETERMINISTIC RUNTIME GATES   │
      │ • BIO_MODEL != MEDICAL_DIAGNOSIS │  │ • Bound to 04_RUNTIME Scheduler  │
      │ • VITALITY != IMMUNITY_OVERRIDE  │  │ • Monitored via 17_OBSERVABILITY │
      │ • FAIL-CLOSED ALLERTON CIRCUIT   │  │ • Fail-Safe Recovery in 16_REPAIR│
      └──────────────────────────────────┘  └──────────────────────────────────┘
```

---

## 1. The Four Modal Intelligences (NBI, NEI, SI, BEI)

### 1.1 Neurobiological Intelligence (NBI)
* **Domain:** Synaptically routed structural cognition, spiking networks, and logical abstraction.
* **Mathematical Dynamics:** Spiking neurons governed by adaptive leaky integrate-and-fire (LIF) dynamics with Spike-Timing-Dependent Plasticity (STDP):

$$\tau_m \frac{dv_i}{dt} = -(v_i - v_{\text{rest}}) + R_m \left( I_i^{\text{syn}}(t) + I_i^{\text{ext}}(t) \right)$$

$$\Delta w_{ij} = \begin{cases}
A_+ \exp\left(-\frac{\Delta t}{\tau_+}\right) & \text{if } \Delta t = t_{\text{post}} - t_{\text{pre}} > 0 \\
-A_- \exp\left(\frac{\Delta t}{\tau_-}\right) & \text{if } \Delta t < 0
\end{cases}$$

### 1.2 Neuro-Electromagnetic & Emotional Intelligence (NEI)
* **Domain:** Large-scale electromagnetic field synchrony, affective valence, and empathetic resonance.
* **Mathematical Dynamics:** Kuramoto phase-oscillator coupling modeling macroscopic cortical coherence and emotional state vectors $\mathbf{e} = [v, a, d]^\top$ (valence, arousal, dominance):

$$\frac{d\theta_i}{dt} = \omega_i + \frac{K_{\text{NEI}}}{N} \sum_{j=1}^N \sin(\theta_j - \theta_i) + \eta_{\text{affect}} \cdot \mathbf{e}(t)$$

$$\mathbf{e}_{t+1} = \mathbf{e}_t + \kappa \left( \mathbf{e}_{\text{target}} - \mathbf{e}_t \right) + \mathbf{J}_{\text{somatic}} \cdot \mathbf{s}_{\text{interoceptive}}$$

### 1.3 Somatic Intelligence (SI)
* **Domain:** Interoceptive feedback, viscero-sensory regulation, metabolic energy budgeting, and vagal tone.
* **Mathematical Dynamics:** Allostatic metabolic control law optimizing glycogen/glucose reserves and heart-rate variability (HRV):

$$\frac{dE_{\text{metabolic}}}{dt} = \dot{E}_{\text{intake}} - \sum_k P_{\text{organ}}^{(k)} - \lambda_{\text{computation}} \cdot \text{FLOPs}_{\text{active}}$$

$$\text{AllostaticLoad}(t) = \int_0^t \left\| \mathbf{s}_{\text{actual}}(\tau) - \mathbf{s}_{\text{homeostatic\_setpoint}} \right\|_{\mathbf{Q}}^2 \, d\tau$$

### 1.4 Bioelectromagnetic Intelligence (BEI)
* **Domain:** Endogenous resting membrane potential patterns ($V_{\text{mem}}$), non-neural morphogenetic signaling (Michael Levin framework), and anatomical self-repair.
* **Mathematical Dynamics:** Spatial-temporal reaction-diffusion of bioelectric membrane potential across syncytial gap-junction networks:

$$\frac{\partial V_i}{\partial t} = \frac{1}{C_m} \sum_{\text{ion}} I_{\text{ion}}(V_i, c_i) + \sum_{j \in \mathcal{N}(i)} G_{ij} (V_j - V_i)$$

Where $G_{ij}$ is the gap junctional conductance gating anatomical patterning memory and morphological regeneration.

---

## 2. Master UBI State Tensor & Coupled Dynamics

The global state of the biological organism is formalized as a coupled tensor:

$$\mathbf{\Psi}_{\text{UBI}}(t) = \big[ \mathbf{x}_{\text{NBI}}(t), \; \mathbf{e}_{\text{NEI}}(t), \; \mathbf{s}_{\text{SI}}(t), \; \mathbf{V}_{\text{BEI}}(t) \big] \in \mathbb{R}^{D_{\text{UBI}}}$$

### 2.1 Cross-Modal Coupling Matrix
The evolution of the coupled organism is governed by the nonlinear interaction tensor:

$$\frac{d\mathbf{\Psi}_{\text{UBI}}}{dt} = \mathbf{F}_{\text{intrinsic}}\big(\mathbf{\Psi}_{\text{UBI}}\big) + \mathbf{\Gamma}_{\text{coupling}} \cdot \mathbf{\Psi}_{\text{UBI}} - \nabla_{\mathbf{\Psi}} \mathcal{F}_{\text{FEP}}$$

$$\mathbf{\Gamma}_{\text{coupling}} = \begin{pmatrix}
0 & \mathbf{C}_{\text{NBI}\leftarrow\text{NEI}} & \mathbf{C}_{\text{NBI}\leftarrow\text{SI}} & \mathbf{C}_{\text{NBI}\leftarrow\text{BEI}} \\
\mathbf{C}_{\text{NEI}\leftarrow\text{NBI}} & 0 & \mathbf{C}_{\text{NEI}\leftarrow\text{SI}} & \mathbf{C}_{\text{NEI}\leftarrow\text{BEI}} \\
\mathbf{C}_{\text{SI}\leftarrow\text{NBI}} & \mathbf{C}_{\text{SI}\leftarrow\text{NEI}} & 0 & \mathbf{C}_{\text{SI}\leftarrow\text{BEI}} \\
\mathbf{C}_{\text{BEI}\leftarrow\text{NBI}} & \mathbf{C}_{\text{BEI}\leftarrow\text{NEI}} & \mathbf{C}_{\text{BEI}\leftarrow\text{SI}} & 0
\end{pmatrix}$$

* $\mathbf{C}_{\text{NBI}\leftarrow\text{SI}}$: Somatosensory visceral inputs biasing cognitive decisions (Damasio's Somatic Marker Hypothesis).
* $\mathbf{C}_{\text{NEI}\leftarrow\text{NBI}}$: Rational appraisals modulating emotional valence and arousal.
* $\mathbf{C}_{\text{BEI}\leftarrow\text{NBI}}$: Neural activity shaping long-term morphogenetic bioelectric patterns.
* $\mathbf{C}_{\text{SI}\leftarrow\text{NEI}}$: Chronic emotional stress increasing visceral inflammation and allostatic load.

---

## 3. Allostatic Setpoints & Homeostatic Basins

The organism defines safe physiological basins in state space $\Omega_{\text{vital}} \subset \mathbb{R}^{D_{\text{UBI}}}$:

$$\mathbf{\Psi}_{\text{UBI}}(t) \in \Omega_{\text{vital}} \iff \begin{cases}
V_{\text{mem}} \in [-70\text{ mV}, -20\text{ mV}] & (\text{BEI health}) \\
\text{AllostaticLoad} \le \Theta_{\text{allostatic\_limit}} & (\text{SI integrity}) \\
\|\mathbf{e}_{\text{NEI}}\| \le E_{\text{max}} & (\text{NEI stability}) \\
\text{SpikingRate}_{\text{avg}} \in [1\text{ Hz}, 50\text{ Hz}] & (\text{NBI balance})
\end{cases}$$

If $\mathbf{\Psi}_{\text{UBI}}$ traverses outside $\Omega_{\text{vital}}$, Tier 5 immediately asserts an allostatic correction signal:

$$\mathbf{u}_{\text{allostasis}} = -\mathbf{K}_{\text{allostasis}} \left( \mathbf{\Psi}_{\text{UBI}} - \mathbf{\Psi}_{\text{setpoint}} \right)$$

Routing high-priority interrupt signals to `04_RUNTIME` to throttle high-cost computational workloads until homeostasis is restored.

---

## 4. Epistemic Boundaries & Safety Firewalls

```text
UBI_MODEL != BIOLOGICAL_ORGANISM
VITALITY_STATE != LEGAL_OR_MEDICAL_ADVICE
SOMATIC_SIMULATION != PHYSICAL_FLESH
FIELD_COHERENCE != OCCULT_ENERGY
```

1. **Computational Analogue Boundary:** All UBI formalisms represent computational and systemic models of biological intelligence (`AMOS_MODEL`). They must never be conflated with clinical medical diagnostics or physical biology.
2. **Deterministic Precedence:** UBI states provide regulatory constraints and contextual biases to cognitive proposal generation. They can never bypass `03_CONTROL_PLANE` security policies or cryptographic capability checks.
3. **Fail-Closed Homeostatic Trip:** If simulated allostatic load exceeds critical thresholds ($\text{AllostaticLoad} > 0.95$), the organism triggers a self-protective quiescent state, prioritizing system recovery in `16_REPAIR`.

---

## 5. Cross-Plane Bindings

- **Governed by Canon:** [[01_CANON/03_COGNITION_CANON/AMOS_FULL_BRAIN_OS_CANON|FULL_BRAIN_OS_CANON]] & [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]].
- **Runtime Binding:** [[05_COGNITIVE_ORGANISM/FULL_BRAIN_OS_RUNTIME_BINDING|FULL_BRAIN_OS_RUNTIME_BINDING]].
- **Predictive Optimization:** [[05_COGNITIVE_ORGANISM/PREDICTION_ENGINE|PREDICTION_ENGINE]].
- **Biological Computing Model:** [[13_MODELS/01_FOUNDATION/BIO_LOGICAL_COMPUTING_MODEL|BIO_LOGICAL_COMPUTING_MODEL]].
- **Homeostatic Recovery:** [[05_COGNITIVE_ORGANISM/16_REPAIR/UBI_RECOVERY_ENGINE|UBI_RECOVERY_ENGINE]].

---

RSCF-NODE
node_id: amos_05_cognitive_organism_ubi_organism_binding
node_type: binding
domain: COGNITION
path: 05_COGNITIVE_ORGANISM/UBI_ORGANISM_BINDING.md
claim_class: AMOS_MODEL
rscf_state: active_specification
canonical_status: CANONICAL_BINDING
RSCF-RELATIONS:
  - INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
  - INDEXED_BY: [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]]
  - GOVERNED_BY: [[01_CANON/03_COGNITION_CANON/AMOS_FULL_BRAIN_OS_CANON|FULL_BRAIN_OS_CANON]]
  - BOUND_TO: [[05_COGNITIVE_ORGANISM/FULL_BRAIN_OS_RUNTIME_BINDING|FULL_BRAIN_OS_RUNTIME_BINDING]]
  - BOUND_TO: [[13_MODELS/01_FOUNDATION/BIO_LOGICAL_COMPUTING_MODEL|BIO_LOGICAL_COMPUTING_MODEL]]
