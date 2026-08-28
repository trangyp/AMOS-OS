---
title: K_CORE_LAWS — Core Laws Dispatch Kernel
type: kernel
source: 02_KERNEL
artifact_id: AMOS-OS-K-CORE-LAWS
canonical_name: K_CORE_LAWS
artifact_type: kernel_law_contract
status: AMOS_MODEL
conclusion_class: AMOS_MODEL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
plane: 02_KERNEL
kernel_family: META_LOGIC
domain: core-laws-governance
scope: AMOS_OS
created: '2026-08-25'
updated: '2026-08-28'
tags:
- amos-os
- kernel
- core_laws
- dispatch
- law-hierarchy
- rule-of-2
- rule-of-4
- law-of-law
- signal-fidelity
- structural-integrity
- rscf/claim
- rscf/state/model
- 01-canon-moc
- 02-kernel-moc
- 00-home
- 00-root-moc
aliases:
- Core Laws Dispatch Kernel
- K_CORE_LAWS
- AMOS Core Laws Gate
---

# K_CORE_LAWS — Core Laws Dispatch Kernel

> **Origin Architect / Steward:** Trang Phan  
> **Plane:** `02_KERNEL`  
> **Status:** `AMOS_MODEL`  
> **Enforcement Gate:** L1 Meta Logic Hard Gate

---

## 1. Constitutional Law Hierarchy

`K_CORE_LAWS` enforces the non-negotiable legal stack of AMOS OS. All agent proposals, architectural mutations, and plan syntheses must pass strict formal verification against the 5 Constitutional Meta-Laws before execution admission.

```
+-------------------------------------------------------------------------+
|                      5 CONSTITUTIONAL META-LAWS                         |
|                                                                         |
|  1. LAW OF LAW: Superior systemic constraints override local goals     |
|  2. RULE OF 2: Dual-axis structural verification (Short/Long, In/Out)   |
|  3. RULE OF 4: Four-quadrant interaction matrix coverage               |
|  4. SIGNAL FIDELITY: Zero semantic distortion across transformations    |
|  5. STRUCTURAL INTEGRITY: No ungrounded synthetic drift                |
+-------------------------------------------------------------------------+
```

---

## 2. The Five Meta-Laws Formalized

### 2.1 Law of Law (Hierarchical Override)
If a local optimization $O_{\text{local}}$ conflicts with a global systemic constraint $C_{\text{global}}$, $C_{\text{global}}$ strictly dominates:

$$\forall P \in \text{Proposals}, \quad \text{Violates}(P, C_{\text{global}}) \implies \text{Admit}(P) = \text{FALSE}$$

### 2.2 Rule of 2 (Dual Structural Axes)
Every strategic proposal must be evaluated simultaneously along two orthogonal axes:
- **Axis 1 (Temporal):** Short-term utility vs Long-term sustainability ($U_{\text{short}} \times U_{\text{long}}$).
- **Axis 2 (Spatial/Scope):** Internal component stability vs External ecosystem impact ($I_{\text{internal}} \times I_{\text{external}}$).
- **Axis 3 (Decision):** Risk exposure vs Return velocity ($R_{\text{risk}} \times R_{\text{reward}}$).

### 2.3 Rule of 4 (Four-Quadrant Matrix)
Every architectural solution must be mapped onto a 4-quadrant interaction grid:

```
                  HUMAN (Skills, Cognition, Safety)
                                 |
        SYSTEM                   +                   ENVIRONMENT
  (Tools, Infra, Logic)          |             (Market, Physics, Regulation)
                                 |
                    TIME (Phasing, Horizon, TSS)
```

An option that fails in any quadrant is classified as `UNSTABLE / REJECTED`.

### 2.4 Signal Fidelity Law
Information passed through multi-agent pipelines must maintain mathematical entropy bounds and zero loss of truth conditions:

$$\Delta H_{\text{distortion}}(\mathcal{M}_{\text{out}}, \mathcal{M}_{\text{in}}) = 0$$

### 2.5 Structural Integrity Law
No proposition may be admitted without explicit causal ancestry grounded in native canon or verified observation.

---

## 3. The 21 Domain Core Laws Matrix

In addition to the 5 Meta-Laws, `K_CORE_LAWS` orchestrates the 21 domain-specific invariant laws spanning:
- **Cognitive & Biological (L0–L5):** 4 UBI Domain Invariants (NBI, NEI, SI, BEI), Homeostasis Floor.
- **Quantum & Fractal (L4):** QLS Coherence Floor, Superposition Dominance Collapse.
- **Governance & Economic (C06–C07):** TSS Overload Accumulation Law, Fragmentation Multiplier.
- **Computational & Systems (C04):** Deterministic Replay Invariant, Fail-Closed Trust Threshold.

---

## 4. Cross-Plane Bindings

- **Governing Canon:** [[LAW_HIERARCHY]] · [[K_LAW_HIERARCHY]] · [[K_CANON]]
- **Routing & Control:** [[K_CONTROL_PLANE]] · [[K_FAIL_CLOSED]] · [[AMOS_KERNEL_SUPER_VINFINITY]]
- **Proof & RSCF:** [[0_UNIVERSE_LOGIC_KERNEL_ULK_ULMK]] · [[K_ABSOLUTE_LOGIC]] · [[K_PROVENANCE]]
- **Navigation:** [[00_HOME]] · [[01_CANON_MOC]] · [[02_KERNEL_MOC]] · [[00_ROOT_MOC]]

