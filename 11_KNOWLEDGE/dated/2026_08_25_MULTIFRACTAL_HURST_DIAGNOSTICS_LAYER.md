---
title: 2026-08-25 Multifractal-Hurst Diagnostics Layer
type: daily-learning
date: 2026-08-25
epistemic: SOURCE/DERIVED
tags: [math, fractal, multifractal, hurst, diagnostics, dated, dated/2026-08-25]
---


# 2026-08-25 — Multifractal & Hurst Diagnostics (FR014–FR016 Deep)

## Gap found

FR014 (fBm/Hurst), FR015 (Weierstrass), FR016 (multifractal) are the **subtlest and easiest-to-fake** fractal families. The map names their validation methods (Hurst estimation, nowhere-differentiable check, Legendre transform) but nothing enforced them. The classic error is specific: running multifractal machinery on a monofractal produces a spurious τ(q) spectrum width, and people call it "multifractal". Single-method Hurst estimates biased by short-range dependence are nearly as common.

## Closure (4 channels)

| Channel | Artifact |
|---|---|
| Skill | `amos/amos-multifractal-hurst-diagnostics` — three-track contract with evidence tables, 6-step procedure, guard set |
| Agent | `.devin/agents/amos-multifractal-audit-agent.json` — 6 capabilities incl. monofractal null test and finance time-basis check |
| Workflow | `multifractal-hurst-audit-pipeline-workflow.md` — three-track pipeline |
| Memory + vault note | recorded |

## The classic error now gated

**Linear τ(q) = monofractal.** If the spectrum is a single slope (R²≈1 for one D), the correct claim is monofractal — multifractal machinery applied anyway manufactures spurious f(α) width. The monofractal null test is mandatory before any multifractal claim.

## Other enforced rules

- Multi-method H (R/S + DFA + wavelet variance agreeing within CI); single-method R/S rejected (short-range-dependence bias)
- AR/ARMA baseline before long-memory claims — apparent long memory often vanishes under control
- Δα width must exceed surrogate estimation error
- Weierstrass roughness claims need stated parameters with ab>1
- Financial fBm requires trading-time vs clock-time declaration

## Audit-family status: 11 layers

The fit-gate-label skeleton is now reused across scaling laws, networks, information measures, chaos, and multifractals. Each new layer costs less and shares more infrastructure.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[DATED_MOC]]
