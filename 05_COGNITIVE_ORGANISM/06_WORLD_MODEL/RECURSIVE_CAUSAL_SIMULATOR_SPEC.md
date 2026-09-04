---
title: RECURSIVE_CAUSAL_SIMULATOR_SPEC
type: organism_subsystem_specification
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_SPECIFICATION
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: authoritative_AMOS_OS_structure
  scope: active__05_COGNITIVE_ORGANISM
tags:
  - cognitive-organism
  - world-model
  - causal-simulator
  - pearl-hierarchy
  - do-calculus
  - active-inference
---

# Recursive Causal Simulator Specification (RCSS)

> **MECE note (2026-09-04):** This artifact was relocated from the duplicate `04_WORLD_MODEL/` folder into the canonical `06_WORLD_MODEL/` folder to resolve a MECE numbering collision with `04_COGNITION/`. The stale `04_WORLD_MODEL/` folder has been removed.

## 1. Subsystem Architecture
The **Recursive Causal Simulator** (RCSS) is the forward-generative and counterfactual evaluation engine of Plane 05 (`05_COGNITIVE_ORGANISM`). It operates on Structural Causal Models (SCMs) and Active Inference generative processes to forecast state trajectories across arbitrary planning horizons $H$.

```mermaid
graph TD
    Obs[Streaming Multi-Sensory Observation $o_t$] --> SCM[Structural Causal Model $\mathcal{M}$]
    SCM --> Abduction[1. Abduction: Compute $P(U | o_t)$]
    Abduction --> ActionPlan[Intervention Candidate $\text{do}(A = a)$]
    ActionPlan --> ActionIntervention[2. Action: Modify Graph to $\mathcal{M}_a$]
    ActionIntervention --> PredictionRollout[3. Prediction: Rollout Trajectory $\hat{s}_{t+1:t+H}$]
    PredictionRollout --> FreeEnergyVal{Expected Free Energy $\mathcal{G}$}
    FreeEnergyVal -->|Minimize $\mathcal{G}$| Commit[Select Optimal Policy $\pi^*$]
    FreeEnergyVal -->|Epistemic Risk High| ActiveExploration[Trigger Epistemic Probe]
```

## 2. Mathematical Formalization

### 2.1 Structural Causal Abduction & Prediction
Given endogenous variables $V = \{V_1, \dots, V_N\}$, exogenous background variables $U = \{U_1, \dots, U_M\}$, and structural equations $F = \{f_i\}$:

$$V_i = f_i(\text{Pa}(V_i), U_i), \quad U_i \sim P(U_i)$$

For an interventional query with hypothetical action policy $\pi$:

$$P(Y_{\text{do}(X = x)} = y) = \sum_{z} P(Y = y | X = x, Z = z) P(Z = z)$$

satisfying the backdoor criterion relative to $(X, Y)$.

### 2.2 Expected Free Energy Minimization
Policy selection $\pi^*$ over the simulated rollout tree minimizes the expected free energy $\mathcal{G}(\pi)$:

$$\mathcal{G}(\pi) = \sum_{\tau = t+1}^{t+H} \underbrace{-\mathbb{E}_{Q(o_\tau | \pi)} \left[ \ln P(o_\tau) \right]}_{\text{Pragmatic Value (Goal Realization)}} + \underbrace{\mathbb{E}_{Q(s_\tau | \pi)} \left[ D_{KL}\left( Q(s_\tau | o_\tau, \pi) \parallel Q(s_\tau | \pi) \right) \right]}_{\text{Epistemic Value (Information Gain)}}$$

### 2.3 Recursive Depth & Branching Factor
The simulator supports recursive self-simulation (the organism simulates itself simulating the world) up to a bounded recursion depth $D_{\max}$. At each depth level $d$, the branching factor $b_d$ is constrained by the cognitive budget $B_d$:

$$b_d \le \left\lfloor \frac{B_d}{c_{\text{rollout}}(H_d)} \right\rfloor, \quad H_d = H_0 \cdot \rho^{-d}, \quad \rho \in [0.5, 0.8]$$

where $c_{\text{rollout}}(H)$ is the per-branch compute cost and $\rho$ is the horizon decay factor. This produces a geometrically shrinking planning cone that respects bounded rationality.

### 2.4 Counterfactual Regret & Causal Credit Assignment
After executing policy $\pi^*$ and observing outcome $o_{t+1:t+H}$, the simulator computes counterfactual regret for each candidate action $a' \neq a^*$:

$$\text{Regret}(a') = \mathcal{G}(\pi_{a'}) - \mathcal{G}(\pi^*) - \lambda \cdot \text{Var}_{U}\left[\mathcal{G}(\pi_{a'})\right]$$

The variance term penalizes high-uncertainty counterfactuals (epistemic humility). Credit assignment propagates regret backward through the causal graph via the back-door adjusted estimator.

## 3. Pearl Causal Hierarchy Mapping

| Level | AMOS Operation | RCSS Capability |
|-------|---------------|-----------------|
| L1 — Association $P(y\|x)$ | Observation | Passive trajectory prediction from observational data |
| L2 — Intervention $P(y\|\text{do}(x))$ | Action | Forward simulation under structural-equation modification |
| L3 — Counterfactual $P(y_{x'}\|x,y)$ | Reflection | Retrospective re-simulation with held-fixed $U$ from abduction |

The simulator must never collapse L3 into L2 or L2 into L1. Each query type requires a distinct computational path and produces a distinct epistemic claim class.

## 4. Execution Contracts & Invariants
1. **Bounded Horizon Execution**: Simulation depth is capped at $H \le 16$ to prevent infinite state space explosion.
2. **Causal Non-Interference**: Interventions are evaluated in ephemeral shadow memory buffers without mutating live vault state.
3. **Receipt Emission**: Every counterfactual evaluation emits a cryptographic verification hash to `[[17_OBSERVABILITY/17_OBSERVABILITY_MOC]]`.
4. **Shadow-World Isolation**: Simulated trajectories are tagged with a `SIMULATED` provenance class and cannot be admitted to memory as `OBSERVED` without an explicit admission gate (`K_MEMORY_ADMISSION`).
5. **Causal Sufficiency Disclosure**: Every simulation declares its assumed causal graph $\mathcal{M}$ and the set of unobserved confounders $U_{\text{unobs}}$. If $U_{\text{unobs}} \neq \emptyset$, the output is downgraded to `CONDITIONAL` epistemic state.
6. **Recursion Termination**: Recursive self-simulation terminates when (a) depth $> D_{\max}$, (b) free-energy gradient $< \epsilon$, or (c) cognitive budget exhausted. A `RECURSION_TERMINATED` receipt records which condition fired.

## 5. Integration with AMOS Cognitive Stack

- **Perception → RCSS**: Streaming observations $o_t$ from `PERCEPTION_ENGINE` seed abduction.
- **RCSS → Planning**: Candidate policies $\{\pi_i\}$ from `PLANNING_ENGINE` are evaluated; $\pi^*$ is returned with expected free energy $\mathcal{G}^*$.
- **RCSS → World Model**: The structural causal model $\mathcal{M}$ is maintained by `INTERNAL_WORLD_MODEL`; RCSS reads but does not write it during simulation.
- **RCSS → Memory**: Counterfactual outcomes with high regret are encoded as `COUNTERFACTUAL_EVIDENCE` for future learning.
- **RCSS → Causal Reasoning Master**: L3 counterfactual queries route through `amos-causal-reasoning-master` for governance; RCSS provides the computational substrate.

## 6. Failure Modes & Guards

| Failure Mode | Symptom | Guard |
|-------------|---------|-------|
| Confounder omission | Spurious causal claim | Causal sufficiency disclosure (invariant 5) |
| Shadow-world leakage | Simulated state mutates live memory | Shadow-world isolation tag + admission gate (invariant 4) |
| Runaway recursion | Depth explosion / budget exhaustion | Recursion termination (invariant 6) |
| Level collapse | L3 query answered with L1 estimator | Pearl hierarchy mapping (§3) + epistemic class tagging |
| Free-energy gaming | Policy selected to minimize $\mathcal{G}$ by exploiting model error | Variance penalty (§2.4) + epistemic probe trigger |

## 7. Cross References
- [[00_ROOT/00_ROOT_MOC|Root Navigation MOC]]
- [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|Cognitive Organism MOC]]
- [[05_COGNITIVE_ORGANISM/06_WORLD_MODEL/INTERNAL_WORLD_MODEL|Internal World Model]]
- [[05_COGNITIVE_ORGANISM/06_WORLD_MODEL/PREDICTIVE_CODING_FRAMEWORK|Predictive Coding Framework]]
- [[05_COGNITIVE_ORGANISM/WORLD_MODEL_ENGINE|World Model Engine]]
- [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L10_WORLD_MODELING/L10_WORLD_MODELING_MOC|L10 World Modeling MOC]]
- [[11_KNOWLEDGE/GRAPH_FAMILY_SPECIFICATION|Graph Family Specification]] (Causal Graph family)
