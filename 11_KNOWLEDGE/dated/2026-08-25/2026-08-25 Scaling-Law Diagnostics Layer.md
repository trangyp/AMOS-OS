---
title: 2026-08-25 Scaling-Law Diagnostics Layer
type: daily-learning
date: 2026-08-25
epistemic: SOURCE/DERIVED
tags: [math, fractal, statistics, power-law, zipf, dated, dated/2026-08-25]
---

# 2026-08-25 — Scaling-Law Diagnostics (FR012–FR014 Deep)

## Gap found

The corpus names power laws, Zipf rankings, and fBm everywhere (FR012–FR014 in the 25-family map) and even specifies validation methods ("tail fit + KS test", "rank-size plot linearity", "Hurst estimation") — but **no skill, agent, or workflow enforced the fitting discipline**. Power-law claims are the most over-claimed pattern class in any large corpus; "everything is a power law" is the fractal version of "correlation is causation". Meanwhile the RG bridge needs audited exponents to feed universality matching — unaudited fits would poison B1's strictest gate.

## Closure (4 channels)

| Channel | Artifact |
|---|---|
| Skill | `amos/amos-scaling-law-diagnostics` — MLE α estimation with CI, x_min declaration rule, alternative-model duel (log-normal/stretch-exponential via likelihood ratio/Vuong), KS reporting, mechanism tagging, Benford companion check |
| Agent | `.devin/agents/amos-scaling-fit-auditor-agent.json` — 6 capabilities incl. exponent gate for RG |
| Workflow | `scaling-law-audit-pipeline-workflow.md` — 9-step pipeline ending at the exponent gate |
| Memory + vault note | recorded |

## Key rules now enforced

1. **Log-log regression alone is rejected** as evidence for α (systematic bias); MLE with CI required
2. **No x_min → incomplete claim** — scaling rarely holds across full range
3. **Alternative-model duel licenses the claim**: lose to log-normal → downgrade to "heavy-tailed", never "power law"
4. **Mechanism tag separates DERIVED-explanatory from curve-fitting**: preferential attachment / multiplicative growth / self-organization
5. **Benford audit** (P(d)=log₁₀(1+1/d): d=1→30.1% … d=9→4.6%) available for order-of-magnitude datasets — fabrication/regime-mixture detector
6. **Exponent gate**: only fully-audited fits feed the RG universality matcher

## Integration payoff
A-matrix cascade magnitudes, UCP historical-collapse frequencies, vault file-size distributions, and agent-count claims all become auditable under one pipeline — and the RG bridge's exponent tables now have a quality floor.

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
