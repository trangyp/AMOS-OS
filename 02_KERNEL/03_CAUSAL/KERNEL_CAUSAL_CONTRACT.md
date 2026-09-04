---
title: Causal Kernel Contract — Subplane Governance Specification
type: specification
source: 02_KERNEL/03_CAUSAL
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 02_KERNEL/KERNEL_KERNEL_CONTRACT
    - 01_CANON/01_CORE_LAWS/CANON_CORE_LAWS_CONTRACT
    - 00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE
  scope: subplane_governance
tags:
  - amos-os
  - 02-kernel
  - causal
  - specification
---

# Causal Kernel Contract — Subplane Governance Specification

> **Origin Architect / Steward:** Trang Phan  
> **AMOS_CORE Target:** `v4.4`  
> **Epistemic Class:** `AMOS_MODEL`  
> **Status:** `ACTIVE_SPECIFICATION`

---

## 1. Architectural Scope & Purpose

`KERNEL_CAUSAL_CONTRACT` governs the causal inference engines, structural causal models (SCM), counterfactual reasoning manifolds, and do-calculus intervention evaluators across the AMOS Kernel. It guarantees that observational correlations are strictly separated from causal mechanisms, preventing spurious associations from driving system actions or architectural modifications.

---

## 2. Mathematical Foundations & Structural Causal Models

A Structural Causal Model (SCM) $\mathcal{M}_{\text{causal}}$ is formalized as a 4-tuple:

$$\mathcal{M}_{\text{causal}} = \langle \mathbf{U}, \mathbf{V}, \mathbf{F}, \mathbb{P}(\mathbf{U}) \rangle$$

Where:
- $\mathbf{U} = \{ U_1, \dots, U_m \}$ is the set of exogenous background variables distributed according to $\mathbb{P}(\mathbf{U})$.
- $\mathbf{V} = \{ V_1, \dots, V_n \}$ is the set of endogenous system variables.
- $\mathbf{F} = \{ f_1, \dots, f_n \}$ is a set of deterministic structural equations:
  $$V_i = f_i(\mathbf{PA}_i, U_i)$$
  Where $\mathbf{PA}_i \subset \mathbf{V}$ represents the direct causal parents of $V_i$.

### The Causal Hierarchy (Pearl's Ladder of Causation):
1. **Layer 1: Association (Seeing):** $\mathbb{P}(y \mid x)$ (Conditional probability).
2. **Layer 2: Intervention (Doing):** $\mathbb{P}(y \mid \text{do}(x))$ (Calculated via Backdoor / Frontdoor criteria).
3. **Layer 3: Counterfactuals (Imagining):** $\mathbb{P}(y_x \mid x', y')$ (Twin network method).

### Do-Calculus Invariant:
Intervention formula under Backdoor criterion for set $\mathbf{Z}$:
$$\mathbb{P}(Y = y \mid \text{do}(X = x)) = \sum_{\mathbf{z}} \mathbb{P}(Y = y \mid X = x, \mathbf{Z} = \mathbf{z}) \mathbb{P}(\mathbf{Z} = \mathbf{z})$$
Provided no vertex in $\mathbf{Z}$ is a descendant of $X$, and $\mathbf{Z}$ blocks every path between $X$ and $Y$ containing an arrow into $X$.

---

## 3. Epistemic Invariants & Confounder Defense

1. **`CORRELATION != CAUSATION`**: Statistical significance ($p < 0.001$, high mutual information $I(X; Y)$) must never be encoded as a directed causal edge $X \to Y$ without satisfying do-calculus identification or interventional RCT evidence.
2. **Acyclicity Invariant:** The causal graph $\mathcal{G} = (\mathbf{V}, \mathbf{PA})$ must remain a strict Directed Acyclic Graph (DAG) ($\text{Cycles}(\mathcal{G}) = \emptyset$).
3. **Latent Confounder Conservatism:** In the presence of unobserved confounders $U$, bounds on causal effects must be expressed as Manski bounds or Pearl bounds rather than exact point estimates.

---

## 4. Execution Mechanics & Causal Engine Pipeline

```text
[Observational Data / Diagnostic Telemetry]
                     │
                     ▼
       [DAG Structure Learning (PC / GES)]
                     │
                     ▼
         [d-Separation & Backdoor Linter] ──► [Unidentifiable? -> Tag UNKNOWN/GAP]
                     │ (Identifiable)
                     ▼
         [Interventional do(X) Simulator]
                     │
                     ▼
       [Counterfactual Scenario Generator]
                     │
                     ▼
         [Safe Action Policy Commit]
```

---

## 5. Failure Modes & Degradation

- **Spurious Feedback Cycle:** Emergent cyclic dependency during dynamic execution. **Action:** Instant causal graph cut at weakest edge and isolate to `24_ARCHIVE`.
- **Collider Bias (Berkson's Paradox):** Conditioning on a common effect creates artificial correlation. **Action:** Causal static analyzer flags collider conditioning and strips the condition.

---

## 6. Cross-Plane Bindings

- **`01_CANON/01_CORE_LAWS`**: Invariant derived from Causal Firewall Law.
- **`02_KERNEL/02_COGNITION`**: Supplies causal graphs for active planning.
- **`17_OBSERVABILITY`**: Validates causal graphs against production execution traces.

---

## 7. Verification & Formal Invariants

Formal verification of d-separation algorithms and DAG acyclicity verified via Lean 4:
$$\forall (G : \text{CausalDAG}), \quad \text{IsAcyclic}(G) \land \text{SoundIntervention}(G)$$

---

## 8. Lineage & Stewardship

- **Origin Architect:** Trang Phan
- **Steward:** Trang Phan
- **Target:** `v4.4`

---

## 9. Attestation Metadata

```yaml
subplane: 02_KERNEL/03_CAUSAL
contract_status: ACTIVE_SPECIFICATION
steward: Trang Phan
verification_status: CAUSALLY_VERIFIED
```
