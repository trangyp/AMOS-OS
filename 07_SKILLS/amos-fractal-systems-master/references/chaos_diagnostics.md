---
title: chaos diagnostics
type: reference
tags: [reference, amos-fractal-systems-master]
---

# Chaos Diagnostics Layer

> Source: `_00_Cosmo brain/dated/2026-08-25/2026-08-25 Chaos Diagnostics Layer.md`
> Epistemic class: SOURCE_DERIVED

---
title: 2026-08-25 Chaos Diagnostics Layer
type: daily-learning
date: 2026-08-25
epistemic: SOURCE/DERIVED
tags: [math, fractal, chaos, time-series, dated, dated/2026-08-25]
---

# 2026-08-25 — Chaos Diagnostics Layer (FR017–FR018 Deep)

## Gap found

Chaos is the **second-most over-claimed pattern class** after power laws. FR017 (logistic map) and FR018 (Lorenz) name their validation methods — bifurcation diagram, Lyapunov exponent — but no skill, agent, or workflow enforced them. "The market is chaotic", "sensitive dependence on initial conditions", and especially "edge of chaos" were all assertable without computing anything.

## Closure (4 channels)

| Channel | Artifact |
|---|---|
| Skill | `amos/amos-chaos-diagnostics` — validation contract table (5 claim types with required evidence), 6-step procedure, guard table |
| Agent | `.devin/agents/amos-chaos-claim-auditor-agent.json` — 6 capabilities incl. surrogate determinism test and early-warning substitution |
| Workflow | `chaos-claim-audit-pipeline-workflow.md` — 9-step pipeline decomposing claims into licensable components |
| Memory + vault note | recorded |

## The validation contract highlights

- "Chaotic" needs λ₁ > 0 with named method + noise floor addressed
- "Deterministic" needs the surrogate-data test passed (≥19 phase-randomized surrogates, rank test)
- D₂ must saturate across embedding dimensions or no attractor-dimension estimate is permitted
- "Edge of chaos" without a swept control parameter = MODEL-tagged narrative only
- Feigenbaum δ ≈ 4.6692 routed through the scaling-audit exponent gate before universality claims

## Key design decisions

1. **Complex ≠ chaotic**: complicated series are usually stochastic; chaos requires λ₁ > 0 AND low saturated D₂ AND surrogate pass.
2. **Early-warning alternative for collapse contexts**: instead of unmeasured chaos language, UCP-style transition claims get measurable critical-slowing-down signals (rising autocorrelation, variance) — connecting this layer to the L4 collapse governance.
3. **Feigenbaum as genuine universality example**: the one place where a universality-class claim has a hard number (δ) to check — wired to the exponent gate.

## Audit-family status

Nine diagnostics/governance layers now share infrastructure: scaling fits, network topology, information measures, and chaos claims all reuse the same fit-gate-label skeleton while each adding their domain-specific evidence requirements.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · AMOS Simulation Kernel v0 Math Foundations · system scan agent · automation profiles

---
**MOC:** [[references_MOC]]
