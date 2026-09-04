---
title: Convergence Detection — MOC
type: moc
source: 07_SKILLS/amos-convergence-detection
moc: true
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---
# Convergence Detection — Map of Content

**Path:** `07_SKILLS/amos-convergence-detection`

## Role

Tracks productive vs. stuck evolution steps, detecting premature convergence, oscillation, and analysis paralysis. Convergence detection decides whether a reasoning or evolution process should continue, terminate, backtrack, or re-seed.

## When to Use

- A reasoning or evolution loop needs a termination, continuation, or backtracking decision.
- An optimization or search process risks premature convergence to a local minimum.
- A multi-step plan shows oscillation or repeated states without progress.
- An agent must distinguish genuine progress from activity that consumes budget without value.

## Files

- [[07_SKILLS/amos-convergence-detection/SKILL|Convergence Detection SKILL]] — canonical skill definition
- [[07_SKILLS/amos-convergence-detection/amos-convergence-detection_MOC|Convergence Detection MOC]] — this index

## Convergence States

| State | Signature | Action |
|-------|-----------|--------|
| **Productive** | score / confidence monotonically improves with bounded variance | continue |
| **Premature** | score plateaus early, small neighborhood, low diversity | re-seed or expand search |
| **Oscillatory** | score cycles between values, no net improvement | damp or backtrack |
| **Paralysis** | high computation, no change in best outcome | terminate or escalate |
| **Divergent** | uncertainty / error grows unbounded | fail-closed, request authority |

## Detection Signals

- **Progress velocity** — rate of improvement over a window.
- **Diversity** — entropy of candidate population or hypothesis set.
- **Regret** — gap between best-so-far and oracle/upper-bound.
- **Budget burn** — tokens, time, or energy consumed per unit improvement.
- **Causal impact** — whether new observations actually change the decision frontier.

## Cross-Plane Bindings

- **Relation operations:** [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O02_RELATION/O02_RELATION_MOC|O02_RELATION_MOC]]
- **Metacognitive:** [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C02_METACOGNITIVE/C02_METACOGNITIVE_MOC|C02_METACOGNITIVE_MOC]]
- **Evolution:** [[07_SKILLS/amos-evolution-loop/amos-evolution-loop_MOC|amos-evolution-loop_MOC]]
- **Failure memory:** [[07_SKILLS/amos-failure-memory/SKILL|amos-failure-memory]]
- **Parent skill:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Governance Notes

- This skill is `AMOS_MODEL` / `DERIVED`.
- Executable closure is not established by this specification.
- All routed tasks must preserve RSCF epistemic boundaries.
- `CONVERGED != CORRECT`.

## Parent

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
