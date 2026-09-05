---
title: SE(3) Lie Group Kinematics & Exponential Map Manifold Integrator Ledger
plane: 21_DOMAINS
subplane: 28_ENGINEERING_MATH
status: ACTIVE_SOTA_MATHEMATICAL_SURFACE
origin_architect: Trang Phan
governance: AMOS_v4.4_CANONICAL
hash_digest: eed2e69e5e6501a2500c2ebeb0ea9aa2da00d6e83b3b3e5f63804e49eceb2728
rscf-state: source-claim
---

# Differential Geometry of SE(3) Rigid Body Kinematics & Lie Group Integration

## 1. Mathematical Formalism

The Special Euclidean group $SE(3) = SO(3) \ltimes \mathbb{R}^3$ represents rigid body configurations in 3D space:
$$T = \begin{bmatrix} R & p \\ 0 & 1 \end{bmatrix} \in SE(3), \quad R \in SO(3), \; p \in \mathbb{R}^3$$

The Lie algebra $\mathfrak{se}(3)$ consists of spatial twists $\xi = (v, \omega)^\top \in \mathbb{R}^6$ under the wedge operator $\wedge: \mathbb{R}^6 \to \mathfrak{se}(3)$:
$$\xi^\wedge = \begin{bmatrix} [\omega]_\times & v \\ 0 & 0 \end{bmatrix} \in \mathbb{R}^{4 \times 4}$$

The closed-form exponential map $\exp: \mathfrak{se}(3) \to SE(3)$ is evaluated via Rodrigues formula and left-Jacobian $V(\omega)$:
$$\exp(\xi^\wedge) = \begin{bmatrix} \exp([\omega]_\times) & V(\omega) v \\ 0 & 1 \end{bmatrix}$$
where $\theta = \|\omega\|$, and:
$$V(\omega) = I_3 + \frac{1 - \cos\theta}{\theta^2}[\omega]_\times + \frac{\theta - \sin\theta}{\theta^3}[\omega]_\times^2$$

Manifold integration preserves the metric structure $R^\top R = I_3$ and $\det(R) = +1$ without Euler angle singularities or drift.

## 2. Telemetry Verification Results

```json
{
  "steps": 200,
  "dt": 0.01,
  "max_orthogonality_error": 3.809796810731578e-15,
  "max_determinant_error": 1.6653345369377348e-15,
  "final_position": [
    1.4345650628196702,
    1.4663292428263106,
    -0.6149849015168382
  ],
  "final_orientation_trace": 1.6485176298420068,
  "manifold_invariance_maintained": true
}
```

## 3. Cryptographic Receipt
- **Max Orthogonality Drift**: `3.81e-15`
- **Max Determinant Drift**: `1.67e-15`
- **Manifold Invariance**: `PRESERVED`


## SOTA Methods

### SE(3) Lie group kinematics
- **SE(3)**: Special Euclidean group in 3D; rigid body transformations; 6-DOF (3 translation + 3 rotation)
- **Lie algebra se(3)**: 6-dimensional tangent space; twist coordinates ξ = [v, ω]; exponential map exp(ξ∧) ∈ SE(3)
- **Adjoint representation**: Ad_g for coordinate transforms; adjoint algebra ad_ξ for Lie bracket; Jacobian computation
- **Logarithmic map**: log(T) ∈ se(3); pose difference; geodesic distance on SE(3)

### Rigid body dynamics
- **Newton-Euler**: F = ma, τ = Iα + ω×(Iω); recursive Newton-Euler algorithm (RNEA)
- **Lagrangian**: L = T - V; Euler-Lagrange equations; generalized coordinates; manipulator equation
- **Hamiltonian**: H = T + V; symplectic integrators; variational integrators; structure-preserving integration
- **Spatial algebra**: Featherstone's spatial vector algebra; 6D spatial vectors; articulated body algorithm (ABA)

### AMOS Integration
- **Engineering math domain**: [[21_DOMAINS/28_ENGINEERING_MATH/28_ENGINEERING_MATH_MOC|28 Engineering Math MOC]]
- **C10 domain**: [[21_DOMAINS/20_C10_TECH_ENGINEERING/20_C10_TECH_ENGINEERING_MOC|C10 tech-engineering domain]]
- **Mechanical structural engine**: [[11_KNOWLEDGE/engine/AMOS_MECHANICAL_STRUCTURAL_ENGINE_LAYER|Mechanical Structural Engine]]
- **Event neuromorphic SLAM**: [[21_DOMAINS/54_ROBOTICS/EVENT_NEUROMORPHIC_SLAM_LEDGER|Event Neuromorphic SLAM Ledger]]
- **SOTA embodied AI**: [[22_RESEARCH/01_PAPERS/SOTA_EMBODIED_AI_AND_ROBOT_LEARNING_2026|SOTA Embodied AI 2026]]

### Invariants
1. `KINEMATICS != DYNAMICS` — motion (kinematics) ≠ forces (dynamics)
2. `IDEALIZATION != REALITY` — rigid body assumption ignores deformation, friction, compliance
3. All kinematic claims must cite provenance (frame, convention, units, uncertainty)
4. `MODEL != PHYSICS` — Lie group models are mathematical abstractions of physical motion

