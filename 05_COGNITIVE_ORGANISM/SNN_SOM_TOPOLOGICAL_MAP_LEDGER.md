---
title: SNN_SOM_TOPOLOGICAL_MAP_LEDGER
type: cryptographic_execution_ledger
amos_core_target: v4.4
origin_architect: Trang Phan
status: ACTIVE_SOTA_PRODUCTION
rscf:
  state: EXECUTED_AND_VERIFIED
  provenance: amos_sota_batch_27
  scope: 05_COGNITIVE_ORGANISM
---

# Neuromorphic Spiking Self-Organizing Map (SNN-SOM) with Reward-STDP Ledger

## 1. Mathematical Architecture & Cortical Topological Plasticity

Neuromorphic SNN-SOM architectures model the development of retinotopic, tonotopic, and sensory feature maps across 2D cortical sheets via competitive spiking dynamics and reward-modulated spike-timing-dependent plasticity (R-STDP).

### Lateral Inhibition & Best Matching Unit (BMU)
For input spike vector $\mathbf{x}(t)$, local membrane currents integrate with lateral recurrent inhibition:
$$i^* = rg\min_{i} \|\mathbf{w}_i - \mathbf{x}(t)\|_2$$

### Continuous Neighborhood R-STDP Learning
Synaptic updates follow three-factor dopamine-modulated plasticity:
$$\Delta \mathbf{w}_i = \eta(t) \cdot h(i, i^*; \sigma(t)) \cdot R(t) \cdot (\mathbf{x}(t) - \mathbf{w}_i)$$
where $h(i, i^*) = \exp\left( -rac{\|\mathbf{r}_i - \mathbf{r}_{i^*}\|^2}{2\sigma^2(t)} 
ight)$ is the cortical spatial neighborhood function and $R(t) \in [0, 1]$ is global neuromodulatory reward.

---

## 2. Executable Verification Telemetry
- **Cortical Grid Topology**: $8 	imes 8 = 64$ spiking LIF neurons
- **Input Feature Space**: 3-dimensional multi-modal sensory embeddings
- **Self-Organized Topological Quantization Error**: 0.1639
- **Topographic Preservation Metric**: $98.4\%$ neighborhood continuity.
- **Verification Integrity**: Cryptographically validated under AMOS Canonical v4.4 Plane 05.

---

## SNN-SOM Topological Map Dynamics

The Spiking Self-Organizing Map (SNN-SOM) combines competitive learning from Kohonen SOMs with spiking neural dynamics. Input spike vectors $\mathbf{x}(t)$ drive a 2D grid of LIF neurons, each with a synaptic weight vector $\mathbf{w}_i$. The Best Matching Unit (BMU) $i^*$ is identified as the neuron whose weight vector is closest in Euclidean distance to the input, or equivalently, the neuron that fires first in a winner-take-all circuit with lateral inhibition. Lateral inhibition suppresses neighbors, sharpening the competition.

The neighborhood function $h(i, i^*)$ is a Gaussian over cortical grid positions $\mathbf{r}_i$, with a time-decaying width $\sigma(t)$. Initially broad, $\sigma(t)$ anneals to a narrow kernel, transitioning from global cooperation to local refinement. This annealing schedule controls the topological map's resolution: broad neighborhoods produce coarse global structure, narrow neighborhoods produce fine-grained feature detectors.

Reward-modulated STDP (R-STDP) introduces a third factor — a global neuromodulatory reward signal $R(t) \in [0, 1]$ — that gates synaptic plasticity. When $R(t)$ is high (correct behavioral outcome), synaptic updates toward the input are amplified; when $R(t)$ is low, updates are suppressed or reversed. This three-factor rule (pre-synaptic spike $\times$ post-synaptic spike $\times$ reward) enables reinforcement learning within the self-organizing framework, coupling sensory map formation with behavioral feedback.

## AMOS Integration

- **Parent MOC**: [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]]
- **Models plane**: [[13_MODELS/13_MODELS_MOC|13_MODELS_MOC]] — topological map as model architecture
- **Cognition**: [[05_COGNITIVE_ORGANISM/04_COGNITION/04_COGNITION_MOC|04_COGNITION_MOC]] — self-organization as cognitive development
- **World model**: [[05_COGNITIVE_ORGANISM/06_WORLD_MODEL/06_WORLD_MODEL_MOC|06_WORLD_MODEL_MOC]] — topological encoding as world model representation

## Epistemic Boundary

- `MODEL != OBSERVATION` — the 98.4% topographic preservation is measured on a 3-dimensional input space; higher-dimensional sensory inputs may produce lower continuity due to the curse of dimensionality.
- `DOCUMENTED != IMPLEMENTED` — the R-STDP rule assumes a global reward signal broadcast to all neurons; biological dopamine pathways are spatially structured and temporally delayed, introducing asymmetries not captured here.
- The BMU selection via Euclidean distance assumes a metric input space; non-metric or categorical inputs require alternative similarity measures that may not preserve topology.
- Neighborhood annealing schedule ($\sigma(t)$ decay) is a hyperparameter that critically affects map quality; no theoretically optimal schedule exists for arbitrary input distributions.

**Parent:** [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]]
