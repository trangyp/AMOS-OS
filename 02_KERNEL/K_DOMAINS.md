---
title: K_DOMAINS — Domain Engine Routing Kernel
type: kernel
source: 02_KERNEL
artifact_id: AMOS-OS-K-DOMAINS
canonical_name: K_DOMAINS
artifact_type: kernel_routing_contract
status: AMOS_MODEL
conclusion_class: AMOS_MODEL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
plane: 02_KERNEL
kernel_family: INTEGRATION
domain: domain-routing
scope: AMOS_OS
created: '2026-08-25'
updated: '2026-08-28'
tags:
- amos-os
- kernel
- domains
- routing
- c01-c12-engines
- multi-domain-orchestration
- rscf/claim
- rscf/state/model
- 02-kernel-moc
- 03-causal-moc
- 00-home
- 00-root-moc
aliases:
- Domain Engine Routing Kernel
- K_DOMAINS
- AMOS Domain Engine Router
---

# K_DOMAINS — Domain Engine Routing Kernel

> **Origin Architect / Steward:** Trang Phan  
> **Plane:** `02_KERNEL`  
> **Status:** `AMOS_MODEL`  
> **Enforcement Gate:** O2 Routing & BKC Kernel-as-Cognition

---

## 1. Purpose and Role

`K_DOMAINS` defines the routing matrix and interaction protocols for the 12 Specialized Domain Engines ($C_{01} \dots C_{12}$). It ensures that multi-domain queries are not collapsed into simplistic single-paradigm answers, but are decomposed into orthogonal sub-problems, routed to appropriate domain cognitive kernels, and re-synthesized deterministically.

```
+-------------------------------------------------------------------------+
|                       MULTI-DOMAIN ROUTING MATRIX                       |
|                                                                         |
|  [ Normalized Input ]                                                   |
|           |                                                             |
|           v                                                             |
|  ( Feature & Intent Extraction: CODE / TECH / BIZFIN / BIO / TSS / DOC )|
|           |                                                             |
|   +-------+-------+-------+-------+-------+-------+                     |
|   |       |       |       |       |       |       |                     |
|   v       v       v       v       v       v       v                     |
| [ C01 ] [ C02 ] [ C04 ] [ C05 ] [ C06 ] [ C07 ] [ C08 ]                |
|  Meta    Math    Code    UBI     TSS    BizFin  Legal                   |
|   |       |       |       |       |       |       |                     |
|   +-------+-------+-------+-------+-------+-------+                     |
|           |                                                             |
|           v                                                             |
|  ( Composition & Interface Integrity Check )                            |
|           |                                                             |
|           v                                                             |
|  [ Multi-Domain Unified Execution Plan ]                                |
+-------------------------------------------------------------------------+
```

---

## 2. The 12 Domain Engine Routing Table

| Engine | Primary Domain | Input Signature | Specialized Logic Pattern |
| :--- | :--- | :--- | :--- |
| **$C_{01}$** | **Meta-Logic** | Axioms, contradiction analysis | ULK 8 ALUs, QLS 4 Constants + 84 Laws |
| **$C_{02}$** | **Math & Compute** | Equations, optimization, signals | Boundary checks, numerical convergence, proofs |
| **$C_{03}$** | **Physics & Cosmos**| Spacetime fields, cosmology | Energy-coherence balance, physical bounds |
| **$C_{04}$** | **Code & Systems** | Software, scripts, refactors | Strict typing, AST transforms, test suites |
| **$C_{05}$** | **UBI / Biology** | Somatic/neural stress, emotion | NBI/NEI/SI/BEI 4-domain homeostasis |
| **$C_{06}$** | **TSS / Governance**| Cycles, institutional fragility| 4 Variables ($\Omega, H, F, S$), 7 Cycles, 4 Outcomes |
| **$C_{07}$** | **BizFin / Economy** | Valuation, unit economics | Cash flow lattice, margin preservation |
| **$C_{08}$** | **Legal & Risk** | Compliance, liability, contracts| Structural risk framing, zero personalized advice |
| **$C_{09}$** | **Scientific** | Experiments, hypotheses | Falsification protocols, empirical grounding |
| **$C_{10}$** | **Design & UI** | UX flows, layouts, visual maps | Obsidian JSON Canvas, clear typography |
| **$C_{11}$** | **Documentation** | Academic papers, reports | MECE structure, precision citations |
| **$C_{12}$** | **Expression** | Emotional/symbolic prose | Translation to structural invariant intent |

---

## 3. Composite Routing & Cross-Domain Arbitration

When a task intersects multiple domains:
1. **Preserve Interfaces:** The output of $C_{\text{TECH}}$ (e.g. system architecture) feeds as constraints into $C_{\text{BIZFIN}}$ (infrastructure cost) and $C_{\text{LEGAL}}$ (data sovereignty).
2. **Conflict Resolution:** If domain objectives conflict (e.g., speed vs security), resolve via [[K_CORE_LAWS]] Law of Law and [[K_RISK_CONSTRAINT]].
3. **No Domain Smuggling:** A domain engine cannot issue authoritative decisions outside its designated scope (e.g., $C_{\text{CODE}}$ cannot unilaterally authorize legal exemptions).

---

## 4. Cross-Plane Bindings

- **Meta-Orchestrator:** [[AMOS_KERNEL_SUPER_VINFINITY]] · [[AMOS_OMNI_KERNEL_CORE]] · [[AMOS_VOMNI_KERNEL]]
- **Control & Law:** [[K_CONTROL_PLANE]] · [[K_CORE_LAWS]] · [[K_AUTHORITY]]
- **State & Integration:** [[K_BINDING]] · [[K_TRANSLATION]] · [[STATE_STATE_CONTRACT]]
- **Navigation:** [[00_HOME]] · [[02_KERNEL_MOC]] · [[03_CAUSAL_MOC]] · [[00_ROOT_MOC]]

