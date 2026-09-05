---
title: "ArXiv 0710.5212 — A Note on Singularity and Non-Proper Value Sets in Real Polynomial Mappings"
type: mathematical_monograph
plane: 22_RESEARCH
subplane: 01_MATHEMATICS
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_MONOGRAPH
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - "Google Drive/0710.5212_A_note_on_singularity_and_non-proper_value_set.md"
    - "22_RESEARCH/01_MATHEMATICS"
  scope: singularity_theory_algebraic_topology
tags:
  - amos-os
  - research
  - mathematics
  - singularity-theory
  - jelonek-set
  - polynomial-mappings
---

# ArXiv 0710.5212 — Singularity & Non-Proper Value Sets in Real Polynomial Mappings

> **Origin Architect / Steward:** Trang Phan  
> **Target Core Lineage:** `v4.4`  
> **Plane:** `22_RESEARCH / 01_MATHEMATICS`  
> **Mathematical Foundations:** Real Algebraic Geometry, Differential Topology, Jelonek Set $S_f$, Asymptotic Critical Values

---

## 1. Executive Summary & Topological Context

In differential topology and algebraic geometry, a mapping $f: X \to Y$ between Riemannian manifolds is **proper** if the pre-image $f^{-1}(K)$ of every compact set $K \subset Y$ is compact in $X$. For polynomial mappings $f: \mathbb{R}^n \to \mathbb{R}^n$ (or $\mathbb{C}^n \to \mathbb{C}^n$), properness can fail at points in the target space where pre-images escape to infinity along unbounded paths.

The set of non-proper values $S_f \subset \mathbb{R}^n$ (the **Jelonek set**) characterizes the exact locus where fibration triviality fails. Understanding $S_f$ and its intersection with the critical value set $K_0(f) = f(\{x \in \mathbb{R}^n : \text{rank}(df_x) < n\})$ is essential for analyzing non-linear state-space singularities, phase-space bifurcations, and neural loss surface topology.

---

## 2. Mathematical Formalism

### 2.1 The Jelonek Set $S_f$ of Non-Proper Values

Let $f = (f_1, \dots, f_n): \mathbb{R}^n \to \mathbb{R}^n$ be a polynomial mapping of degree $d = \max \deg(f_i)$.

**Definition (Non-Proper Value Set):**
A point $y \in \mathbb{R}^n$ belongs to the set of non-proper values $S_f$ if and only if there exists a sequence $\{x_k\}_{k=1}^{\infty} \subset \mathbb{R}^n$ such that:

$$\lim_{k \to \infty} \|x_k\| = \infty \quad \text{and} \quad \lim_{k \to \infty} f(x_k) = y$$

**Jelonek’s Theorem on Affine Varieties:**
For a polynomial map $f: \mathbb{C}^n \to \mathbb{C}^n$, $S_f$ is an algebraic hypersurface of degree at most $\frac{d^n - 1}{d - 1}$. In the real case $f: \mathbb{R}^n \to \mathbb{R}^n$, $S_f$ is a semi-algebraic set of dimension at most $n-1$.

---

### 2.2 Asymptotic Critical Values (Rabier Condition)

Let $df_x^*$ be the adjoint derivative. The asymptotic critical value set $K_{\infty}(f)$ is the set of points $y \in \mathbb{R}^n$ for which there exists a sequence $\{x_k\} \subset \mathbb{R}^n$ with $\|x_k\| \to \infty$, $f(x_k) \to y$, and:

$$\lim_{k \to \infty} \|x_k\| \cdot \nu(df_{x_k}) = 0$$

Where $\nu(A) = \inf_{\|\xi\|=1} \|A^*(\xi)\|$ is the distance from $A$ to the singular linear maps.

**Generalized Fibration Theorem:**
The map $f: \mathbb{R}^n \setminus f^{-1}(K_0(f) \cup S_f) \to \mathbb{R}^n \setminus (K_0(f) \cup S_f)$ is a locally trivial $C^\infty$ smooth fibration. The bifurcation set is precisely $\mathcal{B}(f) = K_0(f) \cup S_f$.

---

## 3. Integration with AMOS 137 Math Registry & Dynamical Systems

| AMOS Plane | Component | Mathematical Application |
| :--- | :--- | :--- |
| [[22_RESEARCH/01_MATHEMATICS/AMOS_137_MATH_REGISTRY\|137 Math Registry]] | Registry Formulation M114 | Bifurcation analysis of non-linear control basins |
| [[04_RUNTIME/04_RUNTIME_MOC\|04_RUNTIME]] | Stability Boundary Observer | Detecting escape trajectories near non-proper value loci $S_f$ |
| [[25_COGNITIVE_MATRIX/AMOS_19X19_GO_BOARD_FORMAL_SYSTEM\|25_COGNITIVE_MATRIX]] | Singular Potential Trapping | Discrete lattice projection of continuous asymptotic critical points |

---

## 4. Cross References

- **Mathematics Hub:** [[22_RESEARCH/01_MATHEMATICS/22_MATHEMATICS_MOC|01_MATHEMATICS_MOC]]]]
- **Research Papers MOC:** [[22_RESEARCH/01_PAPERS/01_PAPERS_MOC|01_PAPERS_MOC]]
- **Root MOC:** [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
