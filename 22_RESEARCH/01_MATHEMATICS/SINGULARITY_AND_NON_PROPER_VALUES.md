---
artifact_id: AMOS-SINGULARITY-NON-PROPER-VALUES
name: singularity-and-non-proper-values
title: "A Note on Singularity and Non-Proper Value Sets in AMOS Dynamical Systems"
document_version: "2.0.0"
schema_version: "2.0.0"
amos_core_target: "v4.4"
created: "2026-08-25"
updated: "2026-09-04"
origin_architect: "Trang Phan"
steward: "Trang Phan"
canon-group: science-math
canon-type: research-paper
rscf-state: source-claim
topic: singularity-math
status: active
conclusion_class: "AMOS_MODEL"
source_status: "SOURCE_CLAIM"
tags:
  - canon-group/science-math
  - canon/paper
  - rscf/claim
  - topic/singularity
  - jelonek-set
  - non-proper-values
---

# A Note on Singularity and Non-Proper Value Sets in AMOS Dynamical Systems

> **Origin Architect / Steward:** Trang Phan  
> **AMOS_CORE Target:** `v4.4`  
> **Conclusion Class:** `AMOS_MODEL`  
> **Status:** `ACTIVE_RESEARCH`

---

## 1. Abstract & Topological Context

In complex dynamical systems and polynomial mappings $F: \mathbb{C}^n \to \mathbb{C}^n$, non-proper value distributions and bifurcation sets represent boundaries where standard causal flow transitions into singular regimes.

In AMOS OS, these mathematical boundaries define the limits of predictable state progression and trigger automatic execution containment before catastrophic failure occurs.

---

## 2. Definitions & Mathematical Formulations

### 2.1 The Non-Proper Value Set $S_F$ (Jelonek Set)
Let $X, Y$ be affine varieties, and $f: X \to Y$ a polynomial map. The set of non-proper values $S_f \subset Y$ is defined as:

$$S_f = \{ y \in Y \mid \exists \{x_k\}_{k=1}^\infty \subset X \text{ s.t. } \|x_k\| \to \infty \text{ and } f(x_k) \to y \}$$

### 2.2 The Singularity Invariant
For a system mapping $F$, the critical variety is:

$$\Sigma = \{ x \in X \mid \text{rank}(dF_x) < \dim(Y) \}$$

The bifurcation set is:

$$\mathcal{B}(f) = f(\Sigma) \cup S_f$$

---

## 3. Operational Applications in AMOS OS

1. **State Space Partitioning:** Identifies unstable attractor basins in `12_STATE/CAUSAL_STATE_GRAPH.md`.
2. **Epistemic Phase Transitions:** Detects points where small changes in user prompts cause discontinuous jumps in model reasoning (`17_OBSERVABILITY/EPISTEMIC_DRIFT_MONITOR.md`).
3. **Rollback Triggering:** If an agent's execution trajectory approaches $\mathcal{B}(f)$, the transaction is halted and isolated.
