---
title: K_GOVERNED_EVOLUTION Repair Overlay — 2026-09-14
origin_architect: Trang Phan
type: kernel_repair_overlay
status: ACTIVE_REPAIR_OVERLAY
conclusion_class: AMOS_MODEL
canonical_status: NOT_CANON_PROMOTION
amos_core_target: v4.4
created: 2026-09-14
---

# K_GOVERNED_EVOLUTION Repair Overlay — 2026-09-14

## Purpose

This overlay preserves `02_KERNEL/K_GOVERNED_EVOLUTION.md` as historical/source material while strengthening its active governed interpretation with executable mutation permission and commit-time authorization.

Origin architect / steward: **Trang Phan**.

The source four-stage sequence—proposal, formal/invariant verification, regression sandbox, CAS swap with approval—is useful but insufficient by itself. It does not fully specify mutation class, admissible target range, lifecycle legality, propagation limits, rollback obligation, authority level, effect identity, or commit-time freshness.

## Hard boundary

```text
CAPABILITY_TO_CHANGE != AUTHORITY_TO_CHANGE
PROPOSAL_AUTHORITY != EXPERIMENT_AUTHORITY
EXPERIMENT_AUTHORITY != DEPLOYMENT_AUTHORITY
COMMITTABLE != COMMITTED
MODEL_SELF_DESCRIPTION != AUTHORIZATION_TOKEN
```

AMOS mutation refers to governed external state, repository, policy, routing, memory, Skill, workflow, or runtime changes. It does not claim host-model neural-weight self-modification.

## Mutation Permission Profile

Every mutable object requires an explicit permission profile:

```text
MPP(x) = {
  mutation_class,
  allowed_targets,
  evidence_threshold,
  approval_authority,
  propagation_limit,
  rollback_required,
  monitoring_window,
  policy_hash
}
```

No performance gain can compensate for a failed hard safety, invariant, authority, propagation, rollback, or audit gate.

## Constitutional anti-capture invariant

A candidate may not autonomously modify the governance boundary used to judge that same candidate.

```text
M0 OR ModifiesGovernanceBoundary(candidate)
  -> ESCALATE_CONSTITUTIONAL
```

This is a governance rule, not a claim that a model can reliably detect all governance-boundary edits by itself. Target classification must be supplied or independently observed by the harness/control plane.

## Lifecycle legality

The bounded executable path permits only declared adjacent promotion transitions:

```text
PROPOSED
-> ELIGIBILITY_CHECK
-> SANDBOXED
-> EXPERIMENTING
-> EVIDENCE_PENDING
-> CHALLENGED
-> GOVERNANCE_REVIEW
-> APPROVED_LIMITED
-> CANARY
-> PRODUCTION_LIMITED
-> PRODUCTION_GENERAL
```

A direct proposal-to-general-production jump is blocked.

Quarantine, rollback, frozen, and retirement recovery paths remain separate control-plane transitions and are not implied by this positive promotion path.

## Prepare gate

A mutation candidate is blocked if any required condition fails:

- mutation class matches its permission profile;
- target is inside the allowed range;
- lifecycle transition is legal;
- evidence level meets threshold;
- invariants pass;
- safety gate passes;
- audit is complete;
- requested propagation is a subset of the allowed envelope;
- rollback target exists when required.

Authority is evaluated separately. The witness must have:

- `mutation:approve` scope;
- authority level at least the profile requirement;
- policy hash equal to the profile policy hash.

## Commit-time authorization

Prepared mutation state binds:

```text
change_id
change_hash
parent_hash
policy_hash
authority_id
required_authority_level
target
proposed_state
```

Commit entitlement requires the exact candidate effect, parent, policy, and authority to remain valid.

```text
AuthorizedCommit
  := ChangeFresh
     AND ParentFresh
     AND PolicyFresh
     AND AuthorityIdentityFresh
     AND AuthorityScopeFresh
     AND AuthorityLevelStillEligible
     AND AuthorityPolicyBindingFresh.
```

If the candidate bytes/semantics change after prepare, the `change_hash` changes and the mutation must be revalidated. If authority is downgraded after prepare, the commit must be revalidated.

## Rollback and negative memory

A production-bound profile may require a known-good rollback parent. Rollback removes an active failed state but must not erase the failure evidence, lineage, or falsifier that triggered repair.

The bounded gate enforces rollback-target presence when the profile requires it. Durable rollback execution and negative-memory persistence remain infrastructure responsibilities outside this module.

## Executable binding

Bounded implementation:

- `03_CONTROL_PLANE/09_COMMIT/governed_mutation_gate.py`

Verifier:

- `03_CONTROL_PLANE/09_COMMIT/test_governed_mutation_gate.py`

Current bounded local evidence:

- Python compilation: PASS.
- 12 adversarial/unit tests: PASS, 0 FAIL.
- tests cover constitutional self-rewrite, governance capture, illegal lifecycle jump, inadequate evidence, non-compensatory safety, propagation expansion, missing rollback, inadequate authority, fresh commit, candidate mutation after prepare, parent/policy drift, and authority downgrade.

## Remaining gaps

- Automatic trustworthy classification of whether a target changes constitutional/governance boundaries: `NOT_ESTABLISHED`.
- Full experiment-environment X0–X6 enforcement: `NOT_ESTABLISHED` by this module.
- Monitoring-window execution and stop-condition observer: `NOT_ESTABLISHED` here.
- Durable effect-release ledger and receiver acknowledgement: delegated to infrastructure/control-plane mechanisms; not implemented by this gate.
- Recovery-state transition graph beyond the positive promotion path: `PARTIAL`.

## Status

`ACTIVE_REPAIR_OVERLAY / AMOS_MODEL`

`GOVERNED_MUTATION_EXECUTABLE_BINDING = BOUNDED`

`AUTONOMOUS_CONSTITUTIONAL_SELF_REWRITE = PROHIBITED`
