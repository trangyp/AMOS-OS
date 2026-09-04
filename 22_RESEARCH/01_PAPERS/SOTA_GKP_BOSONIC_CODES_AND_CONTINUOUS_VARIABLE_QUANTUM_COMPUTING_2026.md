---
type: research_paper
source: 22_RESEARCH/01_PAPERS
aliases:
  - SOTA_GKP_BOSONIC_CODES_AND_CONTINUOUS_VARIABLE_QUANTUM_COMPUTING_2026
  - GKP Bosonic Codes & CV Quantum Computing
amos_core_target: v4.4
artifact_id: AMOS-RESEARCH-GKP-BOSONIC-2026
conclusion_class: OBSERVATION / SOTA_SYNTHESIS
created: 2026-09-04
origin_architect: Trang Phan
status: ACTIVE_RESEARCH
tags:
  - amos
  - research
  - quantum
  - gkp-codes
  - bosonic-qubits
  - continuous-variable
  - quantum-error-correction
title: Gottesman-Kitaev-Preskill (GKP) Bosonic Codes and Optical Continuous-Variable Quantum Computing (2026)
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: active__AMOS_OS
---

# Gottesman-Kitaev-Preskill (GKP) Bosonic Codes and Optical Continuous-Variable Quantum Computing (2026)

## Abstract
We present a comprehensive formulation of finite-energy Gottesman-Kitaev-Preskill (GKP) bosonic quantum error-correcting codes synthesized in 3D superconducting microwave cavities and optical continuous-variable (CV) cluster states. GKP grid states provide hardware-efficient protection against photon loss, phase noise, and continuous Gaussian displacements, reducing physical qubit overhead by $>90\%$ when concatenated with discrete topological surface codes.

---

## 1. Ideal and Finite-Energy GKP Code Stabilizers

In continuous phase space $(q, p)$ governed by the canonical commutation relation $[\hat{q}, \hat{p}] = i\hbar$ (with $\hbar = 1$), the ideal square-lattice GKP code space is defined as the joint $+1$ eigenspace of two commuting displacement stabilizer operators:

$$\hat{S}_q = \exp\left( -i 2\sqrt{\pi} \hat{p} ight), \quad \hat{S}_p = \exp\left( i 2\sqrt{\pi} \hat{q} ight)$$

Logical basis states are infinite superpositions of position eigenstates:

$$|0_Langle \propto \sum_{n=-\infty}^\infty |2n\sqrt{\pi}angle_q, \quad |1_Langle \propto \sum_{n=-\infty}^\infty |(2n+1)\sqrt{\pi}angle_q$$

### Finite-Energy Gaussian Envelopes
Physical realizations enforce finite photon number via a Gaussian envelope operator $\hat{E}_\Delta = \exp(-\Delta^2 \hat{a}^\dagger \hat{a})$:

$$|0_{L,\Delta}angle = rac{1}{\mathcal{N}_0} \exp\left(-\Delta^2 \hat{a}^\dagger \hat{a}ight) \sum_{n=-\infty}^\infty |2n\sqrt{\pi}angle_q$$

$$|1_{L,\Delta}angle = rac{1}{\mathcal{N}_1} \exp\left(-\Delta^2 \hat{a}^\dagger \hat{a}ight) \sum_{n=-\infty}^\infty |(2n+1)\sqrt{\pi}angle_q$$

where $\Delta pprox 0.28$ corresponds to $\sim 11.0	ext{ dB}$ of quantum squeezing, yielding logical error rates $P_L < 10^{-5}$ per stabilizer measurement cycle.

---

## 2. Wigner Function Phase-Space Tomography

The Wigner quasi-probability distribution $W(q, p)$ of a finite-energy GKP qubit exhibits sharp hexagonal/square interference peaks with deep negative regions:

$$W_{|\psiangle}(q, p) = rac{1}{\pi} \int_{-\infty}^\infty \langle q + y | \psi angle \langle \psi | q - y angle e^{-2i p y} \, dy$$

```
   p-quadrature
       ▲
       │      +       -       +       -       +
       │     ( )     ( )     ( )     ( )     ( )
       │      -       +       -       +       -
 0 ────┼─────( )─────(●)─────( )─────(●)─────( )─────► q-quadrature
       │      -       +       -       +       -
       │     ( )     ( )     ( )     ( )     ( )
       │      +       -       +       -       +
```

---

## 3. Autonomous Syndrome Extraction & Homodyne Feedback Loop

Continuous drift $(u, v) \in \mathbb{R}^2$ is tracked and corrected via non-destructive ancillary transmon coupling or phase-sensitive optical homodyne detection:

```mermaid
flowchart LR
    A[Cavity Bosonic Mode GKP State] --> B[Phase-Sensitive Homodyne Detection]
    B --> C[Extract Modular Displacement: u mod sqrt(pi)]
    C --> D{Displacement u < sqrt(pi)/2?}
    D -->|Yes: Correctable Drift| E[Apply Displacement D(-u_mod)]
    D -->|No: Logical Phase Flip| F[Record Pauli Syndrome to Surface Code]
    E --> G[Stabilized GKP Grid State]
    F --> G
```

---

## 4. Concatenated GKP-Surface Code Fault Tolerance

By utilizing GKP states as the physical qubits of a planar rotated Surface Code, single-photon loss errors are converted into biased Gaussian noise, increasing the surface code fault-tolerance threshold from $p_{	ext{th}} pprox 1\%$ to $p_{	ext{th}} > 6.8\%$.

$$\Lambda_{	ext{eff}} = rac{P_{	ext{logical}}}{P_{	ext{physical}}} \propto \exp\left( -d \cdot rac{\sqrt{\pi}}{2\Delta} ight)$$

---

## 5. Integration with AMOS Quantum Subsystems

- **Quantum Systems Domain**: [[21_DOMAINS/41_QUANTUM_SYSTEMS/41_QUANTUM_SYSTEMS_MOC|41_QUANTUM_SYSTEMS_MOC]]
- **QKD & Cryptography**: [[18_SECURITY/CONTINUOUS_VARIABLE_QUANTUM_KEY_DISTRIBUTION_ENGINE|CONTINUOUS_VARIABLE_QUANTUM_KEY_DISTRIBUTION_ENGINE]]
- **Kernel Scheduling**: [[16_SCHEMAS/HETEROGENEOUS_XPU_SCHEDULER_SCHEMA|HETEROGENEOUS_XPU_SCHEDULER_SCHEMA]]
- **Research Papers MOC**: [[22_RESEARCH/01_PAPERS/01_PAPERS_MOC|01_PAPERS_MOC]]
