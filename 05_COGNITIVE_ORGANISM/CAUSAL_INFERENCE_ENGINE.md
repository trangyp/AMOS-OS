---
title: CAUSAL_INFERENCE_ENGINE
type: engine_specification
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_ENGINE
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: authoritative_AMOS_OS_structure
  scope: active__AMOS_OS
tags:
  - cognitive-organism
  - causal-inference
  - engine
  - pearl-hierarchy
---

# Causal Inference Engine (CIE)

## 1. Theoretical Foundation & Pearl Causal Hierarchy
The Causal Inference Engine provides structural causal modeling (SCM), do-calculus intervention analysis, and counterfactual simulation across all cognitive operations.

$$\mathcal{M} = \langle U, V, F, P(U) \rangle$$
where $U$ is exogenous noise, $V$ are endogenous variables, and $F = \{f_i\}$ represents structural causal equations $v_i = f_i(pa_i, u_i)$.

```mermaid
graph TD
    L1[Layer 1: Association - P(y|x)] --> L2[Layer 2: Intervention - P(y|do(x))]
    L2 --> L3[Layer 3: Counterfactual - P(y_x|x', y')]
    L3 --> CIE[Causal Inference Engine Output]
```

## 2. Structural Capabilities
1. **LiNGAM Causal Discovery**: Identifies Linear Non-Gaussian Acyclic Models from observational streaming telemetry.
2. **Do-Calculus Symbolic Prover**: Derives interventional distributions from non-experimental data where identifiable.
3. **Twin Network Counterfactual Engine**: Evaluates counterfactual queries $Y_{X=x}(u)$ under abducted exogenous variables.

## 3. Cross References
- [[00_ROOT/00_ROOT_MOC|Root Navigation MOC]]
- [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|Cognitive Organism MOC]]
- [[05_COGNITIVE_ORGANISM/INTUITION_ENGINE|Intuition Engine]]
- [[05_COGNITIVE_ORGANISM/METACOGNITIVE_ENGINE|Metacognitive Engine]]
- [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L11_CAUSAL_MODELING/L11_CAUSAL_MODELING_MOC|L11 Causal Modeling MOC]]

## Scope

`CAUSAL_INFERENCE_ENGINE` is part of the AMOS OS canonical corpus. Its role is defined by its containing plane and RSCF metadata.

## Invariants

| ID | Invariant |
|----|-----------|
| CAUSAL_INFERENCE_ENGINE_INV_01 | Content preserves RSCF epistemic classification. |
| CAUSAL_INFERENCE_ENGINE_INV_02 | Authority is checked before any state-altering claim. |
| CAUSAL_INFERENCE_ENGINE_INV_03 | Cross-links are valid within the vault graph. |

## Cross References
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- [[20_OPERATIONS/AMOS_OS_AUDIT_2026-09-03|Audit Ledger]]
