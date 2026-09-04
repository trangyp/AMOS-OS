---
title: Continuous-Variable Quantum Key Distribution (CV-QKD) Protocol & Simulator Specification
type: domain_specification
plane: 21_DOMAINS/41_QUANTUM_SYSTEMS
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 21_DOMAINS/41_QUANTUM_SYSTEMS/41_QUANTUM_SYSTEMS_MOC
    - 21_DOMAINS/41_QUANTUM_SYSTEMS/CONTINUOUS_VARIABLE_QUANTUM_ROUTING
    - 22_RESEARCH/01_MATHEMATICS/AMOS_137_MATH_REGISTRY
    - 18_SECURITY/18_SECURITY_MOC
  scope: cv_qkd_simulation
tags:
  - amos-os
  - quantum-systems
  - cv-qkd
  - gaussian-modulation
  - gg02
  - reverse-reconciliation
  - holevo-bound
  - secret-key-rate
---

# Continuous-Variable Quantum Key Distribution (CV-QKD) Protocol & Simulator Specification

## 1. Executive Summary & Epistemic Scope

The **Continuous-Variable Quantum Key Distribution (CV-QKD) Engine** (`21_DOMAINS/41_QUANTUM_SYSTEMS`) implements the **GG02 Gaussian-Modulated Coherent State (GMCS)** protocol, providing unconditionally secure cryptographic key establishment over optical fiber infrastructure without single-photon avalanche detectors.

By utilizing homodyne detection and multi-dimensional reverse reconciliation, the system extracts secret key material resilient to collective Gaussian eavesdropping attacks (Holevo bound $\chi_E$).

```
+----------------------------------------------------------------------------------------------------+
|                         GG02 CONTINUOUS-VARIABLE QKD PROTOCOL PIPELINE                             |
|                                                                                                    |
|    [ Alice: Gaussian Coherent State Preparation $|\alpha\rangle = |x_A + i p_A\rangle$ ($V_A N_0$) ]|
|                                            ||                                                      |
|                                            \/                                                      |
|    [ Untrusted Fiber Channel: Transmittance $T = 10^{-\alpha L/10}$, Excess Noise $\xi$ ]           |
|                                            ||                                                      |
|                                            \/                                                      |
|    [ Bob: Shot-Noise-Limited Balanced Homodyne Detection ($\eta \approx 0.70, v_{\text{el}} = 0.05$) ]|
|                                            ||                                                      |
|                                            \/                                                      |
|    [ Reverse Reconciliation ($\beta \ge 0.95$) + Privacy Amplification via Toeplitz Hashing ]      |
|                                            ||                                                      |
|                                            \/                                                      |
|    [ Asymptotic Secret Key Rate $K = \beta I(A; B) - \chi_E$ -> 18_SECURITY Key Ring ]             |
+----------------------------------------------------------------------------------------------------+
```

---

## 2. Mathematical Formalism & Asymptotic Key Rate

### 2.1 Mutual Information $I(A; B)$
For modulation variance $V_A$ and total variance $V = V_A + 1$:

$$I(A; B) = \frac{1}{2} \log_2 \left( \frac{V + \chi_{\text{tot}}}{1 + \chi_{\text{tot}}} \right)$$

where total channel noise referred to channel input is:

$$\chi_{\text{tot}} = \chi_{\text{line}} + \frac{\chi_{\text{hom}}}{T} = \left(\frac{1-T}{T} + \xi\right) + \frac{1-\eta + v_{\text{el}}}{\eta T}$$

### 2.2 Eve's Holevo Bound $\chi_E$ under Collective Attacks
Under Gaussian optimality theorems, Eve's accessible information is bounded by the von Neumann entropy:

$$\chi_E = S(\rho_{AB}) - S(\rho_{A|B}) = G\left(\frac{\lambda_1 - 1}{2}\right) + G\left(\frac{\lambda_2 - 1}{2}\right) - G\left(\frac{\lambda_3 - 1}{2}\right)$$

where $G(x) = (x+1)\log_2(x+1) - x\log_2(x)$, and $\lambda_{1,2,3}$ are the symplectic eigenvalues of the covariance matrices $\gamma_{AB}$ and $\gamma_{A}^{x_B}$.

### 2.3 Asymptotic Secret Key Rate
$$K = \max\left(0, \; \beta I(A; B) - \chi_E\right) \quad [\text{bits/pulse}]$$

---

## 3. Operational Invariants & Security Thresholds

- `INV-QKD-001` (**Positive Key Rate Floor**): Fiber transmission is terminated if $K \le 10^{-5}\text{ bits/pulse}$.
- `INV-QKD-002` (**Excess Noise Quarantine**): Channel enters immediate security quarantine if excess noise $\xi > 0.05 N_0$.
- `INV-QKD-003` (**Reconciliation Efficiency SLA**): Multi-edge LDPC reverse reconciliation efficiency must satisfy $\beta \ge 0.95$.

---

## 4. Master Navigation & Bindings

- **Quantum Systems MOC:** [[21_DOMAINS/41_QUANTUM_SYSTEMS/41_QUANTUM_SYSTEMS_MOC|41_QUANTUM_SYSTEMS_MOC]]
- **Simulation Ledger:** [[21_DOMAINS/41_QUANTUM_SYSTEMS/CV_QKD_SIMULATION_LEDGER|CV_QKD_SIMULATION_LEDGER]]
- **Security Plane:** [[18_SECURITY/18_SECURITY_MOC|18_SECURITY_MOC]]
- **Quantum Routing:** [[21_DOMAINS/41_QUANTUM_SYSTEMS/CONTINUOUS_VARIABLE_QUANTUM_ROUTING|CONTINUOUS_VARIABLE_QUANTUM_ROUTING]]
