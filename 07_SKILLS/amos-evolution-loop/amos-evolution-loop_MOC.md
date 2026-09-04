---
title: Evolution Loop — MOC
type: moc
source: 07_SKILLS/amos-evolution-loop
moc: true
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---
# Evolution Loop — Map of Content

**Path:** `07_SKILLS/amos-evolution-loop`

## Role

Continuous observe→integrate cycle with rollback, debt tracking, and bounded mutation. The evolution loop is the AMOS mechanism for safely improving skills, agents, and artifacts over time without violating trusted-core invariants.

## When to Use

- The runtime needs a governed, continuous improvement loop that preserves safety invariants.
- A skill, agent, or artifact requires versioned evolution under GMEF authorization.
- A candidate mutation must be integrated, evaluated, and either promoted or rolled back.
- A lineage must track `evolutionary_debt` and `failure_memory` across epochs.

## Files

- [[07_SKILLS/amos-evolution-loop/SKILL|Evolution Loop SKILL]] — canonical skill definition
- [[07_SKILLS/amos-evolution-loop/amos-evolution-loop_MOC|Evolution Loop MOC]] — this index

## Loop Phases

| Phase | Action | Gate |
|-------|--------|------|
| 1. Observe | Monitor runtime, telemetry, and external feedback | observation admission |
| 2. Propose | Generate candidate mutations within capability envelope | mutation class (M0–M5) |
| 3. Validate | Run validation pipeline on candidates | 10-stage validation |
| 4. Integrate | Merge accepted candidates to staging | GMEF authorization |
| 5. Evaluate | Observe behavior under load / test | convergence / divergence check |
| 6. Promote or Rollback | Commit or revert with effect receipt | promotion gates / rollback basins |

## Cross-Plane Bindings

- **Runtime master:** [[07_SKILLS/amos-os-runtime-master/amos-os-runtime-master_MOC|amos-os-runtime-master_MOC]]
- **Observation:** [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/O15_OBSERVATION_MOC|O15_OBSERVATION_MOC]]
- **Validation:** [[07_SKILLS/amos-validation-pipeline/amos-validation-pipeline_MOC|amos-validation-pipeline_MOC]]
- **GMEF / evolution:** [[01_CANON/04_INFRASTRUCTURE_CANON/GMEF_CANON|GMEF_CANON]] · [[07_SKILLS/amos-autonomous-evolution/SKILL|amos-autonomous-evolution]]
- **Failure memory:** [[07_SKILLS/amos-failure-memory/SKILL|amos-failure-memory]]
- **Evolutionary debt:** [[07_SKILLS/amos-evolutionary-debt/SKILL|amos-evolutionary-debt]]
- **Convergence detection:** [[07_SKILLS/amos-convergence-detection/SKILL|amos-convergence-detection]]
- **Parent skill:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Governance Notes

- This skill is `AMOS_MODEL` / `DERIVED`.
- Executable closure is not established by this specification.
- All routed tasks must preserve RSCF epistemic boundaries.
- `EVOLVED != CORRECT`; `TESTED != SAFE`.

## Parent

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
