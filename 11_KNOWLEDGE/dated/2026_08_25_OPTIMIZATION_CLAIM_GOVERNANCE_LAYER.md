---
title: 2026-08-25 Optimization-Claim Governance Layer
type: daily-learning
date: 2026-08-25
epistemic: SOURCE/DERIVED
tags: [math, optimization, governance, dated, dated/2026-08-25]
---

# 2026-08-25 — Optimization-Claim Governance (Optimization-Kernel Deep)

## Gap found

Optimizer output is the **most confidently-wrong evidence class in applied math**: local optima reported as global, budget exhaustion reported as convergence, in-sample objectives reported as real-world optimality, and slightly-infeasible solutions accepted silently. The corpus has an entire Optimization kernel plus intervention-design workflows (A-matrix Phase 7, UCP stabilization) whose outputs are optimization results — none gated.

## Closure (4 channels)

| Channel | Artifact |
|---|---|
| Skill | `amos/amos-optimization-claim-governance` — claim-hierarchy table (what each license requires), six failure gates |
| Agent | `.devin/agents/amos-optimizer-certificate-auditor-agent.json` — 6 capabilities incl. method-class identification and G3 escalation |
| Workflow | `optimization-claim-audit-pipeline-workflow.md` — 8-step pipeline |
| Memory + vault note | recorded |

## The claim hierarchy (core content)

| Claim | License requires |
|---|---|
| Local optimum | first-order/KKT conditions + feasibility |
| Global optimum | proven convexity or bound certificate — **heuristics can NEVER certify this** |
| Converged | stopping criterion satisfied in history, not budget exhaustion |
| Near-optimal | optimality gap with bound provenance |
| Robust optimal | pre-declared sensitivity ranges |

## Key rules

1. **Heuristic "global" = Signal Fidelity violation** escalated into law-stack G3
2. **Feasibility at full precision** — numerical solvers return slightly-infeasible points routinely
3. **Pareto fronts as fronts** with declared scalarization weights; single-point multi-objective answers blocked
4. **In-sample vs out-of-sample objective provenance** declared

## Audit-family tally: 15 layers
Optimization claims were the last major uncaptured evidence class; the family now spans fits, point hypotheses, constructions, transforms, and solver outputs.

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[DATED_MOC]]
