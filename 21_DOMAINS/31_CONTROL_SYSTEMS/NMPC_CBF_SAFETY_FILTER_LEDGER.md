---
title: Non-Linear MPC & Control Barrier Function (CBF) Safety Ledger
plane: 21_DOMAINS
subplane: 31_CONTROL_SYSTEMS
status: ACTIVE_SOTA_CONTROL_SURFACE
origin_architect: Trang Phan
governance: AMOS_v4.4_CANONICAL
hash_digest: 98a51ea55108915757c693381769a2a342d6c96ce7058280886790aa2b2d81de
rscf-state: source-claim
---

# Higher-Order Control Barrier Function (HOCBF) Safety Quadratic Program

## 1. Mathematical Formalism

Let the continuous-time control-affine dynamical system be given by:
$$\dot{x} = f(x) + g(x)u, \quad x \in \mathcal{X} \subset \mathbb{R}^n, \; u \in \mathcal{U} \subset \mathbb{R}^m$$

The safe operational set $\mathcal{C}$ is defined by the zero-superlevel set of a continuously differentiable barrier function $h(x): \mathbb{R}^n \to \mathbb{R}$:
$$\mathcal{C} = \{x \in \mathbb{R}^n : h(x) \ge 0\}$$

For a relative degree $r=2$ barrier function with respect to acceleration input $u$, the Higher-Order Control Barrier Function (HOCBF) defines a sequence of functions $\psi_0(x) = h(x)$, $\psi_1(x) = \dot{\psi}_0(x) + \alpha_1(\psi_0(x))$, leading to the constraint:
$$L_f^2 h(x) + L_g L_f h(x) u + \alpha_1(h(x))\dot{h}(x) + \alpha_2(\psi_1(x)) \ge 0$$

The safety filter solves a real-time convex Quadratic Program (QP):
$$\min_{u \in \mathcal{U}} \frac{1}{2} \|u - u_{nom}(x)\|^2 \quad \text{s.t.} \quad a_{cbf}(x)^\top u \ge b_{cbf}(x)$$

## 2. Telemetry Verification Results

```json
{
  "steps": 100,
  "dt": 0.05,
  "min_barrier_value": 2.591077226629842,
  "min_dist_to_obstacle": 2.0077542744643435,
  "safety_radius": 1.2,
  "safety_preserved": true,
  "final_target_error": 0.4602210847444972,
  "initial_state": [
    0.0,
    0.0,
    2.0,
    1.5
  ],
  "target_state": [
    8.0,
    6.0,
    0.0,
    0.0
  ]
}
```

## 3. Cryptographic Receipt
- **Safe Invariance**: Min obstacle distance = `2.0078m` (Safe radius = `1.2000m`).
- **Target Convergence**: Final positional error = `0.4602m`.


## SOTA Methods

### Nonlinear Model Predictive Control (NMPC)
- **NMPC**: receding horizon optimization; minimize cost over prediction horizon; constraints (state, input); real-time iteration
- **Solvers**: IPOPT, SNOPT, acados, FORCES Pro; real-time NMPC (1-10ms); multiple shooting vs single shooting
- **Robustness**: tube MPC, scenario MPC, min-max MPC; stochastic MPC; chance constraints; distributionally robust MPC

### Control Barrier Functions (CBF)
- **CBF**: safety-critical control; h(x) ≥ 0 defines safe set; ḣ(x) ≥ -α(h(x)) ensures forward invariance
- **CBF-QP**: quadratic program; min ||u - u_des||² s.t. CBF constraint + input bounds; real-time safety filter
- **High-order CBF**: HOCBF for higher relative degree; exponential CBF; robust CBF (measurement noise, model uncertainty)
- **CLF-CBF**: combine Control Lyapunov Function (stability) with CBF (safety); CLF-CBF-QP

### Applications
- **Autonomous vehicles**: collision avoidance, lane keeping, adaptive cruise control; speed control
- **Robotics**: manipulator safety, drone collision avoidance; human-robot collaboration; safe RL
- **Power systems**: grid stability, frequency regulation; voltage safety; economic dispatch with safety

### AMOS Integration
- **Control systems domain**: [[21_DOMAINS/31_CONTROL_SYSTEMS/31_CONTROL_SYSTEMS_MOC|31 Control Systems MOC]]
- **C10 domain**: [[21_DOMAINS/20_C10_TECH_ENGINEERING/20_C10_TECH_ENGINEERING_MOC|C10 tech-engineering domain]]
- **SOTA embodied AI**: [[22_RESEARCH/01_PAPERS/SOTA_EMBODIED_AI_AND_ROBOT_LEARNING_2026|SOTA Embodied AI 2026]]

### Invariants
1. `SAFE_SET != INVARIANT` — defining a safe set does not guarantee forward invariance
2. `MODEL != REALITY` — NMPC uses approximate models; robustness to model error is critical
3. All safety claims must cite provenance (model, CBF, solver, validation method)
4. `CONSTRAINT != GUARANTEE` — constraints in optimization do not guarantee physical safety

