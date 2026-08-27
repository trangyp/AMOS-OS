---
title: 2026-08-25 RG-Fractal Bridge Deep Verification
type: daily-learning
date: 2026-08-25
epistemic: DERIVED/MODEL
tags: [quantum, fractal, math, rg, bridge-b1, dated, dated/2026-08-25]
---

# 2026-08-25 — RG ↔ Fractal Bridge (B1) Deep Layer

## Gap found

B1 ("RG fixed points ↔ scale-invariant geometry — both are what survives zooming") was the most-used analogy in the stack and the most casually abused. The quantum library holds the real machinery (AM-QFT-005 Wilsonian RG/EFT, 006 Polchinski flow equation, 007 running coupling/beta functions — 14 RG/gauge entries total) and FR025 encodes renormalization as a fractal-family iteration, but nothing connected them with discipline. "Renormalizing X" could be said about anything.

## Closure (4 channels)

| Channel | Artifact |
|---|---|
| Skill | `amos/amos-rg-fractal-bridge` — precise shared-structure table (fixed points↔scale invariance, critical exponents↔scaling dimensions, relevant operators↔stable directions, universality classes↔same-D-different-Λ) + 4-item guard set |
| Agent | `.devin/agents/amos-rg-scaling-audit-agent.json` — 6 capabilities incl. exponent-match enforcement and RG-language-borrow blocking |
| Workflow | `rg-fractal-bridge-verification-workflow.md` — 7-step pipeline from map declaration to labels |
| Memory + vault note | recorded |

## The precise bridge (DERIVED, checkable)

Shared mathematics: fixed points = objects invariant under zoom map; critical exponents = scaling dimensions; relevant/irrelevant operators = linearization eigenvalues around the fixed point; universality classes = microscopic detail washes out while macroscopic exponents survive (the same-D-different-Λ lesson generalized).

Guard set: no beta function without declared flow + couplings · no universality without exponent match · no casual 2D-CFT export · mass gap stays MODEL inside QFT-mapping skill.

## Key rule now enforced

**"Renormalizing emotions" and similar borrowings are blocked by default** — allowed only with full φ-map + flow equation + couplings, which casual uses never have. This is the correct asymmetry: the burden is on the borrower, not the auditor.

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[DATED_MOC]]
