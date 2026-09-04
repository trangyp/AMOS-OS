---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
Type: Workflow
Skill: amos-law-stack-enforcement
Agent: amos-law-stack-enforcement-agent
Trigger: When validating whether system rules hold across scale, checking law adherence to LoL/R2/R4 hierarchy, or when a draft law short-circuits canonical order. Use whenever the user mentions law stack, enforcement, invariants, rule hierarchy, LoL, R2, R4, or scale-transition validation.
Version: 1.1.0
title: AMOS Law Stack Enforcement
tags:
  - type/workflow
  - domain/canon-enforcement
  - amos-os
type: workflow
source: 08_WORKFLOWS
rscf:
  state: AMOS_MODEL
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: workflow_process
---

# AMOS Law Stack Enforcement

## Preconditions

- Skill `amos-law-stack-enforcement` is loaded and available.
- Input falls within the declared domain scope.
- User request matches the trigger conditions above.

## Steps

1. **Load law hierarchy** — Load the Law of Law (LoL), Rule of 2 (R2), and Rule of 4 (R4) canonical definitions.
1. **Validate LoL** — Check that the draft law satisfies the Law of Law meta-hierarchy (no law can supersede its own meta-law).
1. **Validate R2** — Run the Rule of 2 dual-frame rejection test: can the law be rejected from two independent frames?
1. **Validate R4** — Check Rule of 4 quadrant completeness: UBI, TSS, PSI, QLS.
1. **Scale transition check** — Verify invariant enforcement across H (constitutional), M (domain), L (mechanical) scale transitions.
1. **UBI integrity audit** — Audit UBI Score and ledger integrity against structural output.
1. **Detect short-circuit** — Identify if the draft law bypasses canonical order (e.g., L-level check used for H-level decision).
1. **Finalize** — Emit law stack validation report with LoL->R2->R4 ordering confirmation.

## Operations

1. **Load law hierarchy** — Load the Law of Law (LoL), Rule of 2 (R2), and Rule of 4 (R4) canonical definitions.
1. **Validate LoL** — Check that the draft law satisfies the Law of Law meta-hierarchy (no law can supersede its own meta-law).
1. **Validate R2** — Run the Rule of 2 dual-frame rejection test: can the law be rejected from two independent frames?
1. **Validate R4** — Check Rule of 4 quadrant completeness: UBI, TSS, PSI, QLS.
1. **Scale transition check** — Verify invariant enforcement across H (constitutional), M (domain), L (mechanical) scale transitions.
1. **UBI integrity audit** — Audit UBI Score and ledger integrity against structural output.
1. **Detect short-circuit** — Identify if the draft law bypasses canonical order (e.g., L-level check used for H-level decision).
1. **Finalize** — Emit law stack validation report with LoL->R2->R4 ordering confirmation.

## Validation Gates

- [ ] LoL meta-hierarchy satisfied (law does not supersede its own meta-law)
- [ ] R2 dual-frame rejection test passed
- [ ] R4 quadrant completeness verified (UBI/TSS/PSI/QLS)
- [ ] Scale transition invariants hold (H/M/L)
- [ ] UBI Score/ledger integrity verified
- [ ] No canonical order short-circuit detected
- [ ] Epistemic class labeled
- [ ] Provenance recorded
- [ ] Confidence ceiling enforced

## Error Handling

- **Scope violation**: Reject and route to parent skill.
- **Contradiction**: Flag CRITICAL_GAP and halt; do not fabricate canon.
- **Provenance loss**: Mark output as UNKNOWN and request human review.
- **Drift**: Trigger drift alignment governor before re-execution.

## Composition

- Can be invoked by parent master skill for domain-specific audits.
- Can delegate to `amos-audit-repair-master` for gap escalation.
- No delegation to non-AMOS skills.

## Provenance

- **Origin architect**: Trang Phan
- **Steward**: Trang Phan
- **Epistemic class**: AMOS_MODEL
- **RSCF state**: SOURCE_CLAIM
