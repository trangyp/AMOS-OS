---
title: Cancer Evolutionary Therapy — Scientific Review and AMOS State-of-the-Art Framework
type: scientific_framework
source: 21_DOMAINS/03_HEALTH
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_FRAMEWORK
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - "Google Drive/Cancer Evolutionary Therapy — Scientific Review and AMOS s–o–a Framework.gdoc"
    - 21_DOMAINS/00_INDEX/DOMAIN_EXTENSION_PROTOCOL
  scope: oncology_evolutionary_therapy
tags:
  - amos-os
  - domains
  - health
  - oncology
  - evolutionary-therapy
---

# Cancer Evolutionary Therapy — Scientific Review and AMOS Framework

> **Origin Architect / Steward:** Trang Phan
> **Target Core Lineage:** `v4.4`
> **Domain Family:** `C03: HEALTH & BIOLOGY`

---

## 1. Executive Summary

Standard oncological paradigms focus on maximum tolerated dose (MTD) eradicate-at-all-costs strategies, which frequently select for treatment-resistant clonal subpopulations.

The **AMOS Cancer Evolutionary Therapy Framework** formulates tumor dynamics as non-linear evolutionary game systems, applying **Adaptive Therapy Stabilization** to maintain sensitive clones that competitively suppress resistant subpopulations.

```text
MODEL != OBSERVATION
DOCUMENTED != IMPLEMENTED
EVOLUTIONARY_STRATEGY != CLINICAL_PROTOCOL
```

---

## 2. Architectural Scope

This framework occupies the `C03: HEALTH & BIOLOGY` domain family within the AMOS domain extension system. It bridges evolutionary game theory, mathematical oncology, and adaptive control theory to produce a formal specification for treatment scheduling under clonal competition constraints.

The framework treats the tumor as a polymorphic clonal ecosystem rather than a homogeneous mass. Treatment decisions are framed as control inputs into a stochastic evolutionary dynamical system, where the objective function balances tumor burden reduction against the preservation of competitive suppression dynamics.

### 2.1 MECE Partition Mapping

| AMOS Plane | Role in Framework |
| :--- | :--- |
| `21_DOMAINS/07_HEALTHCARE` | Domain host, clinical translation, regulatory mapping |
| `22_RESEARCH/01_MATHEMATICS` | Formal game-theoretic models, ODE systems, stochastic analysis |
| `13_MODELS` | Population dynamics simulation, parameter inference, Bayesian update |
| `04_RUNTIME` | Treatment epoch scheduling, deterministic replay of clinical decisions |
| `18_SECURITY` | Patient data isolation, HIPAA/GDPR compliance envelope |
| `19_TESTS` | Model validation against clinical trial data, falsification harness |

---

## 3. Mathematical Dynamics & Lotka-Volterra Competition

Let $x_s$ be the population density of therapy-sensitive cancer cells, and $x_r$ the density of resistant cells:

$$\frac{dx_s}{dt} = r_s x_s \left(1 - \frac{x_s + \beta_{sr} x_r}{K}\right) - \delta_s(D(t))\, x_s$$

$$\frac{dx_r}{dt} = r_r x_r \left(1 - \frac{x_r + \beta_{rs} x_s}{K}\right) - \delta_r(D(t))\, x_r$$

Where:
- $\delta_s(D(t)) \gg \delta_r(D(t))$ is the drug-induced kill rate.
- $\beta_{rs}$ is the competitive inhibition exerted by sensitive cells on resistant clones.
- Adaptive dosing modulates $D(t)$ to preserve $x_s(t) \ge x_{\text{threshold}}$, bounding total tumor burden while preventing resistant outgrowth.

### 3.1 Adaptive Therapy Control Law

The dosing function $D(t)$ is governed by a bang-bang controller with hysteresis:

$$D(t) = \begin{cases} D_{\max} & \text{if } \frac{x_s + x_r}{K} \ge \theta_{\text{upper}} \\ 0 & \text{if } \frac{x_s + x_r}{K} \le \theta_{\text{lower}} \\ D(t-\Delta t) & \text{otherwise} \end{cases}$$

Where $\theta_{\text{upper}}$ and $\theta_{\text{lower}}$ define the treatment window bounds. The hysteresis gap prevents oscillatory dosing that would destabilize the competitive equilibrium.

### 3.2 Evolutionary Game-Theoretic Extension

Under the replicator dynamics formulation, the frequency of sensitive clones $p_s = x_s / (x_s + x_r)$ evolves as:

$$\frac{dp_s}{dt} = p_s (1 - p_s) \left[ f_s(\mathbf{x}, D) - f_r(\mathbf{x}, D) \right]$$

Where $f_s$ and $f_r$ are the fitness functions of sensitive and resistant phenotypes respectively. The adaptive therapy objective is to maintain $p_s$ above the critical frequency $p_s^* = \beta_{rs} / (\beta_{sr} + \beta_{rs})$ at which resistant clones lose their selective advantage.

---

## 4. Methodology & Framework Architecture

### 4.1 Treatment Strategy Hierarchy

1. **Adaptive Dosing Stabilization (ADS):** Maintain a stable polymorphic equilibrium where sensitive clones competitively suppress resistant clones. Drug holidays are triggered when tumor burden falls below the lower threshold.
2. **Extinction-First Induction:** Short-duration MTD induction to reduce initial tumor volume before transitioning to adaptive maintenance.
3. **Competitive Release Prevention:** Explicitly avoid treatment intensification that eliminates the sensitive population, which would remove competitive suppression on resistant clones.

### 4.2 Parameter Inference Pipeline

- **Input:** Longitudinal tumor volume measurements, circulating tumor DNA (ctDNA) fractions, imaging biomarkers.
- **Inference:** Bayesian hierarchical model estimating $r_s, r_r, \beta_{sr}, \beta_{rs}, K, \delta_s, \delta_r$ with posterior credible intervals.
- **Validation:** Posterior predictive checks against held-out clinical data; model comparison via WAIC and leave-one-out cross-validation.

### 4.3 Stochastic Extension

The deterministic ODE system is augmented with demographic stochasticity for small-population regimes:

$$dx_s = \left[ r_s x_s \left(1 - \frac{x_s + \beta_{sr} x_r}{K}\right) - \delta_s x_s \right] dt + \sqrt{x_s}\, dW_s$$

$$dx_r = \left[ r_r x_r \left(1 - \frac{x_r + \beta_{rs} x_s}{K}\right) - \delta_r x_r \right] dt + \sqrt{x_r}\, dW_r$$

Where $dW_s, dW_r$ are independent Wiener processes. This captures extinction dynamics in small resistant populations that deterministic models miss.

---

## 5. Safety Invariants

- `INV-ONCO-001` (**Competitive Suppression Preservation**): Treatment schedule must not drive $x_s \to 0$ before $x_r$ is controlled, as this triggers competitive release.
- `INV-ONCO-002` (**Tumor Burden Ceiling**): Total burden $x_s + x_r$ must remain below the symptomatic threshold $K_{\text{sympt}}$ at all times.
- `INV-ONCO-003` (**Parameter Identifiability**): Inference pipeline must report posterior credible intervals; decisions under non-identifiable parameters must escalate to human oncologist.
- `INV-ONCO-004` (**Model != Patient**): Framework outputs are decision support, not autonomous clinical decisions. All treatment modifications require licensed oncologist sign-off.

---

## 6. Navigation & Bindings

- **Domain Hub:** [[21_DOMAINS/21_DOMAINS_MOC|21_DOMAINS_MOC]]
- **137 Math Coupling:** [[22_RESEARCH/01_MATHEMATICS/AMOS_137_MATH_REGISTRY|AMOS_137_MATH_REGISTRY]]
- **Model Simulation Plane:** [[13_MODELS/13_MODELS_MOC|13_MODELS_MOC]]
- **Runtime Epoch Scheduling:** [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME_MOC]]
- **Security & Privacy Envelope:** [[18_SECURITY/18_SECURITY_MOC|18_SECURITY_MOC]]
- **Validation & Falsification:** [[19_TESTS/19_TESTS_MOC|19_TESTS_MOC]]
- **Domain Extension Protocol:** [[21_DOMAINS/00_INDEX/DOMAIN_EXTENSION_PROTOCOL|DOMAIN_EXTENSION_PROTOCOL]]

---

## 7. Known Gaps

- **Clinical Trial Validation:** The Lotka-Volterra competition model has been validated against retrospective prostate cancer data (Zhang et al.) but has not been prospectively validated across diverse tumor types (breast, lung, melanoma).
- **Spatial Heterogeneity:** The current ODE model assumes well-mixed populations. Spatial tumor heterogeneity and microenvironmental gradients are not captured. Partial differential equation extensions remain `UNKNOWN/GAP`.
- **Multi-Drug Resistance:** The two-clone model does not account for multi-drug resistance mechanisms (MDR1, ALK mutations). Extension to $n$-clone systems is specified but not implemented.
- **Immune System Coupling:** Tumor-immune dynamics (tumor-infiltrating lymphocytes, checkpoint inhibitor interactions) are not integrated into the current framework.
- **Epistemic Boundary:** `MODEL != OBSERVATION` — mathematical predictions require clinical correlation before treatment modification. This framework is a decision support specification, not an autonomous therapy execution system.
