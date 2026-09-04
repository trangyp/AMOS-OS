---
title: Quantum Parameterized Circuit State Tomography
type: quantum_domain_engine
plane: 21_DOMAINS/41_QUANTUM_SYSTEMS
amos_core_target: v4.4
origin_architect: Trang Phan
status: ACTIVE_PRODUCTION_SPEC
conclusion_class: DERIVED
rscf:
  state: DERIVED
  provenance: authoritative_AMOS_OS_structure
  scope: active__AMOS_OS
---

# Quantum Parameterized Circuit State Tomography Specification

## 1. Variational Quantum Circuit Foundations

Quantum State Tomography (QST) reconstructs the density matrix $\rho$ of an unknown quantum state using a finite number of projective measurements. The **AMOS Parameterized Quantum Circuit (PQC) State Tomography Engine** uses a variational ansatz to estimate multi-qubit states and evaluate quantum state fidelity:

$$F(\rho, \sigma) = \left(\text{Tr}\sqrt{\sqrt{\rho}\sigma\sqrt{\rho}}\right)^2$$

```
       +-------------------------------------------------------------+
       |         Unknown Target Quantum State Preparation |psi>      |
       +-------------------------------------------------------------+
                                      |
                                      v
       +-------------------------------------------------------------+
       |         Parameterized Hardware-Efficient Ansatz U(theta)    |
       |             R_y(theta_i) * R_z(phi_i) * CNOT Layers         |
       +-------------------------------------------------------------+
                                      |
                                      v
       +-------------------------------------------------------------+
       |         Multi-Basis Pauli Projections (sigma_X, Y, Z)       |
       +-------------------------------------------------------------+
                                      |
                                      v
       +-------------------------------------------------------------+
       |      Variational Gradient Descent / Quantum Natural Grad    |
       |       Loss(theta) = 1 - Tr(rho_target * rho(theta))         |
       +-------------------------------------------------------------+
```

## 2. Mathematical Dynamics
The trial state $|\psi(\boldsymbol{\theta})\rangle$ is parameterized by $L$ alternating rotation and entangling layers:
$$|\psi(\boldsymbol{\theta})\rangle = \prod_{l=1}^L \left( \prod_{j=1}^{n-1} \text{CNOT}_{j, j+1} \prod_{j=1}^n R_y(\theta_{l, j}) R_z(\phi_{l, j}) \right) |0\rangle^{\otimes n}$$

---
*Governed by Origin Architect Trang Phan | AMOS OS v4.4 Canonical Core*
