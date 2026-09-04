---
title: Autonomous Evolution — MOC
type: moc
source: 07_SKILLS/amos-autonomous-evolution
moc: true
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---
# Autonomous Evolution — Map of Content

**Path:** `07_SKILLS/amos-autonomous-evolution`

## Role

Self-improvement loop with trusted-core preservation. Improves system capabilities while keeping an immutable trusted core intact. Autonomous evolution is the top-level AMOS capability for safe, bounded self-modification.

## When to Use

- `amos-os-runtime-master` routes a self-improvement or capability-evolution task.
- A trusted-core boundary must be preserved while the outer system evolves.
- A rollback basin, failure memory, and governance approval are all available.
- A candidate mutation is M3–M5 and requires high-authority authorization.

## Files

- [[07_SKILLS/amos-autonomous-evolution/SKILL|Autonomous Evolution SKILL]] — canonical skill definition
- [[07_SKILLS/amos-autonomous-evolution/amos-autonomous-evolution_MOC|Autonomous Evolution MOC]] — this index

## Evolution Architecture

```text
[Trusted Core] — immutable, verified, source-of-truth invariants
      ↓
[Evolution Engine] — proposes, validates, and stages candidate mutations
      ↓
[Staging / Shadow Runtime] — tests candidates without authority
      ↓
[Governance Commit] — promoted only with receipt and causal epoch
      ↓
[Updated System] — new validated capability; rollback basin preserved
```

## Safety Conditions

| Condition | Requirement |
|-----------|-------------|
| Trusted-core preservation | Core invariants cannot be modified by the evolution process. |
| Rollback basin | A verified prior state must be recoverable. |
| Failure memory | All failed mutations are retained and learnable. |
| Convergence detection | Evolution must not runaway or oscillate. |
| Authority ceiling | M0–M2 mutations escalate; M3–M5 require governance. |
| Validation pipeline | Every candidate passes the 10-stage validation. |

## Cross-Plane Bindings

- **Runtime master:** [[07_SKILLS/amos-os-runtime-master/amos-os-runtime-master_MOC|amos-os-runtime-master_MOC]]
- **Governance:** [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C01_GOVERNANCE/C01_GOVERNANCE_MOC|C01_GOVERNANCE_MOC]]
- **Learning lifecycle:** [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O16_LEARNING/O16_LEARNING_MOC|O16_LEARNING_MOC]]
- **Evolution loop:** [[07_SKILLS/amos-evolution-loop/amos-evolution-loop_MOC|amos-evolution-loop_MOC]]
- **Failure memory:** [[07_SKILLS/amos-failure-memory/SKILL|amos-failure-memory]]
- **Convergence detection:** [[07_SKILLS/amos-convergence-detection/amos-convergence-detection_MOC|amos-convergence-detection_MOC]]
- **Validation:** [[07_SKILLS/amos-validation-pipeline/amos-validation-pipeline_MOC|amos-validation-pipeline_MOC]]
- **Parent skill:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Governance Notes

- This skill is `AMOS_MODEL` / `DERIVED`.
- Executable closure is not established by this specification.
- All routed tasks must preserve RSCF epistemic boundaries.
- `EVOLUTION != IMPROVEMENT`; every evolved capability must be independently validated.

## Parent

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
