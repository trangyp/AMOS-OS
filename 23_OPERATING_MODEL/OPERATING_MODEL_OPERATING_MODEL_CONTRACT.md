---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Operating Model Operating Model Contract
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# Operating Model Contract

## 0. Status

- epistemic class: `AMOS_MODEL`
- canonical status: `CONDITIONAL`
- implementation status: `PARTIAL`

This contract specifies organizational governance semantics. Document existence does not establish
plane-wide enforcement or current human delegations.

## 1. Scope

`23_OPERATING_MODEL` governs:

```text
ROLES
DECISION RIGHTS
GOVERNANCE FORUMS
ESCALATION
SERVICE LEVELS
```

It does not replace infrastructure effect authority in the Control Plane.

## 2. Core separation

C09 distinguishes six organizational layers:

```text
LEGAL ENTITY
REPORTING STRUCTURE
OPERATING MODEL
DECISION RIGHTS
CONTROL SYSTEM
INCENTIVE / CULTURE
```

These layers interact but are not interchangeable.

```text
ORG CHART != LEGAL AUTHORITY
ROLE != DECISION RIGHT
DECISION RIGHT != TECHNICAL CAPABILITY
APPROVAL != COMMIT
FORUM MEMBERSHIP != AUTHORITY
SERVICE TARGET != SAFETY OVERRIDE
```

## 3. Shared integrity terms

- load-bearing artifacts are typed and versioned;
- scope, regime, jurisdiction, time and authority are explicit where material;
- authority may be delegated only within the delegator's own envelope;
- stale/revoked rights do not survive merely because work already started;
- consequence and reversibility thresholds determine escalation intensity;
- verifier independence must be demonstrated when load-bearing;
- unresolved contradictions remain visible;
- failure invalidates only actual dependents where computable;
- derived confidence does not exceed the weakest load-bearing premise without revalidation.

## 4. Plane-specific invariants

1. Every recurring decision area has one accountable decision owner.
2. Proposal, consultation, decision, execution and notification are separate roles.
3. Delegation thresholds are explicit by amount/risk/scope/reversibility where material.
4. High-impact actions may require separation of proposal, approval, execution and verification.
5. Crisis governance may shorten latency but may not erase provenance, scope or post-event review.
6. Governance forums coordinate/review; they do not automatically create effect authority.
7. Service levels express operating commitments; they do not authorize unsafe or invalid execution.
8. Organizational authorization must still pass applicable technical commit-time gates for durable
   system/world effects.

## 5. Required operating-model objects

### Role record
Identity, purpose, accountable outcomes, responsibilities, exclusions, required capability,
decision participation, authority source, escalation route, conflicts/separation-of-duty, lifecycle.

### Decision-right record
Decision class, proposer, decider, consulted, informed, executor, thresholds, veto/hold,
delegation source, evidence preconditions, expiry/revocation, audit receipt.

### Forum charter
Purpose, scope, decision classes, membership roles, chair, quorum if applicable, evidence pack,
decision/escalation rules, cadence/triggers, minutes/receipt, follow-up ownership.

### Escalation record
Trigger, origin owner, unresolved question, evidence/provenance, requested authority/expertise,
deadline, permitted interim action, containment state, resolution and return path.

### Service-level record
Service/objective, owner, consumer, target, measurement definition, window, exclusions, severity,
response/recovery objectives, dependency assumptions, breach/escalation rule, review cadence.

## 6. Decision classes

C09 provides four classes:

- **Strategic** — long-horizon direction, major allocation, entry/exit.
- **Tactical** — medium-horizon planning and budget/capacity within envelope.
- **Operational** — routine execution choices.
- **Crisis** — urgent decisions under degraded information.

Applying one governance latency to all four is a design error.

## 7. Delegation and blast-radius rule

Reversible, low-blast-radius decisions may be pushed downward within capability and policy limits.
Irreversible or high-blast-radius decisions require stronger authority/evidence and often
independent review.

```text
DELEGATION != ACCOUNTABILITY_ERASURE
CHILD_AUTHORITY <= PARENT_AUTHORITY
PLANNING_TIME_ALLOW != COMMIT_TIME_ALLOW
```

## 8. UNKNOWN/GAP semantics

An unresolved `UNKNOWN/GAP` blocks only the decision/effect whose integrity, legality, authorization,
or safety materially depends on it. Missing implementation or live delegation is never filled by
narrative inference.

## 9. Executed-evidence boundary

Receipts elsewhere in `_AMOS_OS` prove only the exact validator/version/input/environment/scope they
bind. They may inform this contract but do not prove enterprise-wide operating-model implementation.

## 10. Evaluation sequence

1. Resolve decision/service/role identity and current version.
2. Bind scope, regime, jurisdiction and temporal validity.
3. Resolve accountable owner and decision rights.
4. Check delegation/capability/authority if an effect is proposed.
5. Resolve evidence/provenance and material conflicts.
6. Apply consequence/reversibility thresholds.
7. Decide, hold, deny, or escalate using the weakest accurate conclusion class.
8. Record a receipt for consequential decisions/effects where required.
9. Revalidate mutable authority/policy/state at commit when technical mutation occurs.

## 11. Promotion checklist

- [ ] stable identity/version
- [ ] primary owner
- [ ] decision rights explicit
- [ ] scope/regime/jurisdiction explicit
- [ ] delegation source and limits explicit
- [ ] conflict/separation-of-duty handled
- [ ] service or response thresholds defined where applicable
- [ ] escalation/rollback/recovery path
- [ ] observability/audit evidence route
- [ ] unresolved critical gaps visible
- [ ] implementation claim backed by a specific receipt

## 12. Falsifiers

This contract must be revised if:
- admitted canon defines materially different semantics;
- a current higher-authority operating policy supersedes these partitions;
- executed validation contradicts an invariant inside the same applicability envelope;
- implementation silently collapses role/decision/authority boundaries.

## Related

- [[23_OPERATING_MODEL/23_OPERATING_MODEL_MOC|23_OPERATING_MODEL_MOC]]
- [[23_OPERATING_MODEL/01_ROLES/01_ROLES_MOC|Roles]]
- [[23_OPERATING_MODEL/02_DECISION_RIGHTS/02_DECISION_RIGHTS_MOC|Decision Rights]]
- [[23_OPERATING_MODEL/03_GOVERNANCE_FORUMS/03_GOVERNANCE_FORUMS_MOC|Governance Forums]]
- [[23_OPERATING_MODEL/04_ESCALATION/04_ESCALATION_MOC|Escalation]]
- [[23_OPERATING_MODEL/05_SERVICE_LEVELS/05_SERVICE_LEVELS_MOC|Service Levels]]
- [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|Control Plane]]
- [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|Observability]]
- [[20_OPERATIONS/20_OPERATIONS_MOC|Operations]]

---
RSCF-NODE
node_id: operating_model_operating_model_contract
node_type: contract
path: 23_OPERATING_MODEL/OPERATING_MODEL_OPERATING_MODEL_CONTRACT.md
claim_class: AMOS_MODEL
