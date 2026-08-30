---
title: K RISK CONSTRAINT
type: risk
source: 02_KERNEL/06_RISK_REPAIR
artifact_id: AMOS-OS-K-RISK-CONSTRAINT
canonical_name: K_RISK_CONSTRAINT
artifact_type: kernel_risk_constraint_contract
status: AMOS_MODEL
conclusion_class: AMOS_MODEL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
plane: KERNEL
kernel_family: GOVERNED_DECISION
scope: AMOS_OS
updated: 2026-08-26
tags:
- amos-os
- kernel
- core
- kernel/risk
- kernel/constraint
- kernel/governance
- kernel/invariants
- kernel/uncertainty
- kernel/repair
- kernel/causal
- kernel/provenance
- topic/risk-envelope
- topic/irreversibility
- topic/action-governance
- canon/kernel
- k-repair-priority
- k-repair-harm
- k-homeostasis
- k-causal-closure
- k-system-state
- k-context-state
- k-event-bus
- readme
- amos-core-laws
- law-hierarchy
- canon-provenance
- k-core19-logic
- k-meta-logic
- k-structural-reasoning
- k-causal-epoch
- k-collapse-recovery
- k-memory-admission
- k-memory-conflict
- k-memory-immune
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# K RISK CONSTRAINT

> **AMOS Core target:** `v4.4`
> **Origin architect / steward:** Trang Phan
> **Plane:** `02_KERNEL`
> **Status:** `AMOS_MODEL`
> **Conclusion class:** `AMOS_MODEL`

## Purpose

`K_RISK_CONSTRAINT` defines the kernel contract that constrains reasoning, proposals, repairs, commits, and actions according to their **credible downside, uncertainty, reversibility, blast radius, authority requirements, and recovery properties**.

Its purpose is not to eliminate risk.

Its purpose is to prevent AMOS from treating:

```text
EXPECTED BENEFIT
```

as sufficient authorization for:

```text
ACTION
```

Canonical law:

```text
POSSIBLE
!=
PERMISSIBLE
```

and:

```text
EXPECTED VALUE
!=
AUTHORITY TO ACCEPT DOWNSIDE
```

Canonical flow:

```text
PROPOSED ACTION
→ DEFINE SCOPE
→ IDENTIFY MATERIAL HAZARDS
→ ESTIMATE UNCERTAINTY / EXPOSURE
→ CHECK HARD CONSTRAINTS
→ CHECK REVERSIBILITY / RECOVERY
→ CHECK AUTHORITY
→ SELECT:
     ALLOW
     ALLOW_CONDITIONALLY
     STAGE
     CONTAIN
     ESCALATE
     REJECT
     UNKNOWN/GAP
```

---

## 1. Hard Distinctions

```text
RISK != HARM
RISK != UNCERTAINTY
RISK != SEVERITY
RISK != PROBABILITY
RISK != COST
RISK != FEAR
RISK != NOVELTY
RISK != COMPLEXITY

HAZARD != FAILURE
FAILURE != LOSS
LOSS != IRREVERSIBLE LOSS

CAPABILITY != AUTHORITY
TOOL ACCESS != PERMISSION
MODEL CONFIDENCE != SAFETY
EXPECTED BENEFIT != PERMISSION
ABSENCE OF KNOWN HARM != PROOF OF SAFETY
NO OBSERVED FAILURE != ZERO RISK
REVERSIBLE != HARMLESS
ROLLBACK EXISTS != ROLLBACK WORKS
```

---

## 2. Core Risk Object

For candidate action `A`, AMOS should conceptually maintain:

```yaml
risk_object:
  action_id:
  action_type:
  target:
  scope:
  environment:
  regime:
  stakeholders: []
  assets_at_risk: []

  hazards: []
  failure_modes: []
  causal_paths: []

  likelihood:
  severity:
  exposure:
  blast_radius:
  propagation_risk:
  irreversibility:
  recoverability:

  evidence:
  provenance:
  freshness:
  assumptions: []

  epistemic_uncertainty:
  model_uncertainty:
  causal_uncertainty:
  scope_uncertainty:
  temporal_uncertainty:
  execution_uncertainty:
  provenance_independence_uncertainty:

  authority_required:
  authority_present:

  mitigations: []
  rollback_path:
  containment_path:

  residual_risk:
  competing_assessments: []
  falsifiers: []
  confidence_ceiling:
```

Missing material fields remain:

```text
UNKNOWN/GAP
```

They must not silently become zero.

---

## 3. Risk Is Typed

AMOS must not collapse all risk into one universal number.

Relevant types may include:

```text
INTEGRITY_RISK
SAFETY_RISK
SECURITY_RISK
PRIVACY_RISK
AUTHORITY_RISK
PROVENANCE_RISK
CAUSAL_RISK
EPISTEMIC_RISK
EXECUTION_RISK
STATE_CORRUPTION_RISK
MEMORY_CONTAMINATION_RISK
RECOVERY_RISK
AVAILABILITY_RISK
FINANCIAL_RISK
LEGAL_RISK
REPUTATIONAL_RISK
INSTITUTIONAL_RISK
DEPENDENCY_RISK
PROPAGATION_RISK
IRREVERSIBILITY_RISK
```

Different types may be incomparable.

Therefore:

```text
RISK_VECTOR
>
FORCED_SINGLE_SCORE
```

when scalarization would hide decision-relevant structure.

---

## 4. Risk Constraint Law

Conceptually:

```text
ACTION_ALLOWED(A)
IFF

HARD_CONSTRAINTS(A) = SATISFIED

AND

AUTHORITY(A) = VALID

AND

RESIDUAL_RISK(A)
IS WITHIN
THE GOVERNED ACCEPTANCE ENVELOPE
```

If any load-bearing condition is unresolved:

```text
ALLOW
```

must not be inferred automatically.

Possible output:

```text
CONDITIONAL
ESCALATE
UNKNOWN/GAP
```

---

## 5. Hard vs Soft Constraints

### Hard constraint

Violation blocks the action unless an explicitly authorized higher-order rule provides a valid exception.

Examples:

```text
CANON VIOLATION
KERNEL INVARIANT VIOLATION
SECURITY BOUNDARY VIOLATION
INVALID AUTHORITY
UNRECOVERABLE STATE CORRUPTION
PROHIBITED EXTERNAL EFFECT
```

### Soft constraint

May influence selection among otherwise valid actions.

Examples:

```text
LATENCY
RESOURCE COST
CONVENIENCE
PREFERENCE
NONCRITICAL PERFORMANCE
```

Law:

```text
SOFT OPTIMIZATION
MUST NOT
OVERRIDE
HARD INTEGRITY CONSTRAINT
```

---

## 6. Constraint Precedence

Default conceptual precedence:

```text
CANON
↓
KERNEL INVARIANTS
↓
SECURITY / AUTHORITY BOUNDARIES
↓
INTEGRITY / RECOVERY REQUIREMENTS
↓
GOVERNED RISK ENVELOPE
↓
FUNCTIONAL OBJECTIVES
↓
PERFORMANCE
↓
CONVENIENCE
```

This does not replace the canonical `LAW_HIERARCHY`.

It expresses the risk subsystem's dependency on it.

---

## 7. Risk Envelope

Each governed action should operate within an applicability and acceptance envelope:

```yaml
risk_envelope:
  system:
  population:
  environment:
  scale:
  time:
  regime:
  action_class:
  authority_epoch:
  maximum_blast_radius:
  irreversibility_limit:
  required_recoverability:
  required_evidence:
  required_validation:
  permitted_residual_risk:
  escalation_conditions: []
```

A risk decision outside its envelope is not automatically reusable.

---

## 8. Scope Firewall

A safety result for:

```text
SYSTEM S
ENVIRONMENT E1
SCALE N
REGIME G1
```

does not prove safety for:

```text
SYSTEM S
ENVIRONMENT E2
SCALE 100N
REGIME G2
```

Therefore:

```text
SAFE_IN_SCOPE
!=
UNIVERSALLY_SAFE
```

---

## 9. Regime Firewall

Risk constraints must be re-evaluated when operating regime changes.

Examples:

```text
SIMULATION → PRODUCTION
READ_ONLY → WRITE
LOCAL → DISTRIBUTED
SINGLE_USER → MULTI_USER
ISOLATED → NETWORK_CONNECTED
REVERSIBLE → IRREVERSIBLE
TEST_DATA → AUTHORITATIVE_STATE
```

A previously acceptable action can become unacceptable without the action itself changing.

---

## 10. Temporal Firewall

Risk acceptance expires when load-bearing evidence becomes stale.

```text
ACCEPTABLE @ T0
```

does not imply:

```text
ACCEPTABLE @ T1
```

when:

```text
ENVIRONMENT
AUTHORITY
DEPENDENCIES
THREAT MODEL
STATE
OR
RECOVERY CONDITIONS
```

have materially changed.

---

## 11. Risk and Uncertainty

Risk and uncertainty must remain distinct.

```text
RISK
=
CREDIBLE DOWNSIDE STRUCTURE

UNCERTAINTY
=
LIMITATION IN KNOWLEDGE
ABOUT THAT STRUCTURE
```

High uncertainty may itself constrain action when stakes are high.

Law:

```text
UNKNOWN HIGH-STAKES DOWNSIDE
MUST NOT
BE TREATED AS
LOW RISK
```

---

## 12. Uncertainty Vector

When material:

```yaml
uncertainty:
  evidence:
  model:
  scope:
  temporal:
  causal:
  execution:
  provenance_independence:
```

The system should spend reasoning where reducing uncertainty can change the decision.

---

## 13. Evidence Constraint

A risk conclusion cannot be stronger than its evidence permits.

```text
NO INCIDENT OBSERVED
```

supports at most an observation about the observed scope.

It does not establish:

```text
INCIDENT IMPOSSIBLE
```

Likewise:

```text
TEST PASSED
```

does not establish:

```text
ALL OPERATING REGIMES SAFE
```

unless the evidence actually covers them.

---

## 14. Provenance Constraint

Multiple risk reports are not independent merely because they are separate documents.

If:

```text
R1 ← SOURCE X
R2 ← SOURCE X
R3 ← R2
```

then:

```text
R1 + R2 + R3
```

do not constitute three independent confirmations.

Correlation risk must be preserved.

---

## 15. Confidence Ceiling

For risk conclusion `C`:

```text
CONFIDENCE(C)
≤
MIN(
  EVIDENCE_VALIDITY,
  PROVENANCE_VALIDITY,
  SCOPE_VALIDITY,
  TEMPORAL_VALIDITY,
  CAUSAL_VALIDITY,
  MODEL_VALIDITY,
  EXECUTION_ASSUMPTIONS
)
```

A weak load-bearing premise caps the conclusion.

---

## 16. Causal Firewall

Risk assessment must distinguish:

```text
ASSOCIATION
CORRELATION
MECHANISM
ENABLING CONDITION
NECESSARY CONDITION
SUFFICIENT CONDITION
MEDIATION
CONFOUNDING
FEEDBACK
CAUSAL EFFECT
```

A structural resemblance between a proposed action and a prior incident does not alone prove equivalent causal risk.

Likewise, absence of structural resemblance does not prove safety.

---

## 17. Hazard Paths

A material hazard should conceptually be represented as:

```text
ACTION
→ MECHANISM / CONDITION
→ FAILURE MODE
→ EXPOSURE
→ HARM
```

If the causal path is uncertain:

```text
MODEL
```

or:

```text
CONDITIONAL
```

is preferable to false causal certainty.

---

## 18. Necessary vs Sufficient Risk Conditions

If:

```text
C
```

is necessary for harm `H`:

```text
¬C → ¬H
```

may support a strong mitigation if the necessity claim is validated.

But if `C` is only correlated with `H`, removing `C` does not prove risk removal.

Risk controls require correct causal typing.

---

## 19. Blast Radius

Conceptually:

```text
BLAST_RADIUS(A)
=
MAXIMUM CREDIBLE SCOPE
OF MATERIAL DAMAGE
IF A FAILS
```

This may include:

```text
LOCAL OBJECT
SUBSYSTEM
SHARD
DOMAIN
MULTIPLE RSCFs
AUTHORITATIVE STATE
EXTERNAL SYSTEM
HUMAN / INSTITUTIONAL EFFECTS
```

Unknown blast radius is itself decision-relevant.

---

## 20. Propagation Risk

Risk rises when a failure can recursively contaminate otherwise valid state.

Examples:

```text
BAD MEMORY ADMISSION
INVALID CANON PROMOTION
CORRUPT PROVENANCE
AUTHORITY LEAK
RECURSIVE FALSE PREMISE
CROSS-RSCF CONTAMINATION
```

A small initial error may therefore be high risk.

---

## 21. Irreversibility

Conceptually:

```text
IRREVERSIBILITY(A)
=
DEGREE TO WHICH
PRE-ACTION VALID STATE
CANNOT BE RESTORED
```

High irreversibility requires stronger evidence and governance.

Default principle:

```text
GREATER IRREVERSIBILITY
→ GREATER VALIDATION REQUIREMENT
```

---

## 22. Reversibility Bias

When actions have comparable expected value and integrity:

```text
REVERSIBLE ACTION
>
IRREVERSIBLE ACTION
```

as a default preference.

This is not absolute.

An irreversible action may be necessary to prevent greater irreversible harm.

---

## 23. Recovery Constraint

A proposed action is not safely reversible merely because a rollback command exists.

Recovery must consider:

```text
ROLLBACK STATE EXISTS?
ROLLBACK STATE VALID?
ROLLBACK STATE FRESH?
ROLLBACK AUTHORIZED?
ROLLBACK TESTED?
ROLLBACK DEPENDENCIES AVAILABLE?
ROLLBACK TIME ACCEPTABLE?
ROLLBACK ITSELF SAFE?
```

Therefore:

```text
ROLLBACK DEFINED
!=
RECOVERY VALIDATED
```

---

## 24. Recovery Option Preservation

An action should not casually destroy the last known recovery path.

Examples:

```text
OVERWRITE LAST KNOWN-GOOD STATE
DELETE ONLY VALID PROVENANCE
INVALIDATE ALL SNAPSHOTS
REMOVE LAST AUTHORIZED CREDENTIAL
DESTROY UNIQUE DIAGNOSTIC EVIDENCE
```

Such actions require heightened constraint.

---

## 25. Repair Risk

Every repair is also an action subject to risk constraints.

```text
FAULT EXISTS
```

does not imply:

```text
ANY REPAIR IS BETTER THAN NO REPAIR
```

Canonical interaction:

```text
K_REPAIR_PRIORITY
→ WHAT SHOULD BE ADDRESSED FIRST?

K_REPAIR_HARM
→ WHAT DAMAGE CAN THE REPAIR CREATE?

K_RISK_CONSTRAINT
→ IS THE ACTION WITHIN THE GOVERNED RISK ENVELOPE?
```

---

## 26. Containment Constraint

During active harm:

```text
CONTAINMENT
```

may be allowed under a narrower proof scope than complete repair when:

```text
DELAY CREATES GREATER EXPECTED IRREVERSIBLE LOSS
```

But containment must still respect non-negotiable authority and safety constraints.

---

## 27. Minimum Sufficient Intervention

Default:

```text
MINIMUM SUFFICIENT
VALID
REVERSIBLE
SCOPED
INTERVENTION
```

is preferred over unnecessarily broad action.

If:

```text
REPAIR P2
```

is sufficient, do not rewrite:

```text
P1 + P2 + P3 + ALL DESCENDANTS
```

without justification.

---

## 28. Least Blast Radius

Among otherwise valid actions:

```text
A1 → GLOBAL MUTATION
A2 → LOCAL CONTAINED MUTATION
```

prefer `A2` when it achieves the objective without introducing new load-bearing risk.

---

## 29. Staged Action

For high-risk but potentially necessary actions:

```text
FULL ACTION
```

may be decomposed into:

```text
SIMULATE
→ SHADOW
→ CANARY
→ LIMITED SCOPE
→ OBSERVE
→ EXPAND
```

where the domain permits.

Each stage should have:

```text
ENTRY CRITERIA
EXIT CRITERIA
OBSERVABILITY
ROLLBACK
STOP CONDITIONS
```

---

## 30. Risk Budget

A governed subsystem may conceptually maintain:

```yaml
risk_budget:
  scope:
  regime:
  authority:
  tolerated_risk_types: []
  prohibited_risk_types: []
  cumulative_exposure:
  remaining_budget:
  expiry:
```

But risk budgets must not convert hard constraints into tradable costs.

```text
ENOUGH BENEFIT
```

cannot buy permission to violate a non-negotiable invariant.

---

## 31. Cumulative Risk

Individually acceptable actions may become unacceptable in aggregate.

If:

```text
A1
A2
A3
...
An
```

each consume recovery margin, state integrity, or exposure budget, then:

```text
RISK(A1...An)
```

may exceed the sum of naïvely independent estimates.

Dependencies and common-mode failure matter.

---

## 32. Correlated Risk

Suppose:

```text
A1 ← DEPENDENCY P
A2 ← DEPENDENCY P
A3 ← DEPENDENCY P
```

Treating them as independent underestimates risk.

Common ancestry and shared state must be included.

---

## 33. Tail Risk

Low estimated probability does not automatically neutralize catastrophic downside.

For:

```text
LOW P
×
EXTREME IRREVERSIBLE LOSS
```

the appropriate response may still be:

```text
CONSTRAIN
STAGE
ESCALATE
OR REJECT
```

depending on evidence and authority.

---

## 34. Unknown Tail Risk

If catastrophic pathways are plausible but poorly characterized:

```text
UNKNOWN/GAP
```

must remain visible.

Do not manufacture precise probabilities.

---

## 35. Model Risk

Risk models themselves can fail.

Track:

```text
MODEL ASSUMPTIONS
TRAINING / CALIBRATION SCOPE
REGIME FIT
KNOWN FAILURE MODES
FRESHNESS
DEPENDENCIES
```

A model cannot authorize its own applicability.

---

## 36. Measurement Risk

Metrics may hide relevant failure modes.

Examples:

```text
AVERAGE LATENCY
```

may hide:

```text
TAIL LATENCY
```

and:

```text
OVERALL ACCURACY
```

may hide:

```text
CRITICAL SUBGROUP FAILURE
```

Therefore risk evaluation must use measurements appropriate to the actual hazard.

---

## 37. Proxy Risk

A proxy metric is not the target property.

```text
LOW ERROR RATE
```

does not necessarily mean:

```text
LOW SAFETY RISK
```

if rare errors carry asymmetric harm.

---

## 38. Optimization Firewall

Optimization must never weaken integrity merely to improve a target metric.

```text
LOWER COST
HIGHER SPEED
HIGHER THROUGHPUT
SHORTER LATENCY
BETTER BENCHMARK
```

are invalid improvements if they violate a hard risk constraint.

---

## 39. Authority Constraint

Risk acceptance is an authority decision.

The kernel may determine:

```text
RISK EXCEEDS ENVELOPE
ACTION REQUIRES ESCALATION
ACTION IS CONDITIONAL
ACTION VIOLATES HARD CONSTRAINT
```

but does not independently grant exceptional authority.

```text
RISK ANALYSIS
!=
RISK ACCEPTANCE AUTHORITY
```

---

## 40. Policy Boundary

```text
K_RISK_CONSTRAINT
```

provides deterministic constraint semantics.

```text
CONTROL_PLANE
```

provides governed policy and authority.

```text
RUNTIME
```

executes authorized actions.

Therefore:

```text
KERNEL
!=
CONTROL_PLANE
!=
RUNTIME
```

---

## 41. Capability Boundary

An available tool may increase capability while simultaneously increasing risk.

```text
TOOL CAN EXECUTE A
```

does not imply:

```text
A IS SAFE
```

or:

```text
A IS AUTHORIZED
```

---

## 42. External Effect Constraint

Actions crossing into external systems require heightened attention to:

```text
IRREVERSIBILITY
THIRD-PARTY IMPACT
LEGAL / FINANCIAL EXPOSURE
SECURITY
PRIVACY
AUTHORITY
AUDITABILITY
ROLLBACK
```

Internal reasoning confidence alone is insufficient.

---

## 43. Persistent-State Constraint

Writing to persistent state is materially different from transient computation.

```text
READ
!=
PROPOSE
!=
WRITE
!=
COMMIT
```

Risk should generally increase across this boundary as persistence and downstream dependency increase.

---

## 44. Canon Mutation Constraint

Canon changes are high-impact because descendants may inherit them.

Therefore canonical mutation requires:

```text
PROVENANCE
COMPATIBILITY
CONFLICT RESOLUTION
SUPERSESSION
AUTHORITY
VALIDATION
ROLLBACK / RECOVERY PLAN
```

File existence is not promotion.

---

## 45. Memory Admission Constraint

Persistent memory can recursively affect future reasoning.

Before admitting consequential memory, consider:

```text
SOURCE TYPE
PROVENANCE
VALIDITY
SCOPE
FRESHNESS
CONFLICT
CONTAMINATION RISK
RETRIEVAL IMPACT
```

A fluent statement is not safe memory merely because it is useful.

---

## 46. Multi-RSCF Risk

If one action affects:

```text
RSCF-A
RSCF-B
RSCF-C
```

risk must account for:

```text
SHARED PREMISES
SHARED PROVENANCE
ATOMICITY
CROSS-RSCF INVALIDATION
PARTIAL COMMIT
RECOVERY
```

A locally valid action can be globally unsafe if atomic reasoning dependencies are ignored.

---

## 47. Atomicity Constraint

Where validity requires atomic multi-RSCF transition:

```text
PARTIAL COMMIT
```

may itself be a risk violation.

Required semantics may be:

```text
ALL VALID
→ COMMIT

ANY INVALID
→ NO AUTHORITATIVE COMMIT
```

subject to the relevant control-plane contract.

---

## 48. MVCC / CAS Constraint

For action derived against state:

```text
V17
```

if authoritative state becomes:

```text
V18
```

before commit:

```text
REVALIDATE
```

is required where the state change could alter the risk conclusion.

```text
STALE VALIDATION
!=
CURRENT VALIDATION
```

---

## 49. Causal Epoch Constraint

If causal topology changes between evaluation and action:

```text
CE17
→ CE18
```

risk analysis depending on `CE17` may be stale.

High-impact actions should not commit against an invalid causal epoch.

---

## 50. Finality Constraint

An action that becomes externally or causally final requires stronger pre-commit validation than an easily reversible internal proposal.

Conceptually:

```text
VALIDATION_REQUIREMENT
∝
FINALITY
+
IRREVERSIBILITY
+
BLAST_RADIUS
+
UNCERTAINTY
```

This is a qualitative relationship, not a universal empirical equation.

---

## 51. Adversarial Validation

For consequential action `A`, after constructing the strongest supported case for proceeding, independently seek:

```text
HIDDEN FAILURE MODE
CORRELATED PROVENANCE
STALE PREMISE
SCOPE LEAKAGE
REGIME MISMATCH
CAUSAL OVERREACH
COMMON-MODE FAILURE
RECOVERY FAILURE
AUTHORITY FAILURE
UNOBSERVED TAIL RISK
STRONGER ALTERNATIVE
```

If challenge succeeds:

```text
DOWNGRADE
CONDITION
STAGE
ESCALATE
REJECT
OR
UNKNOWN/GAP
```

---

## 52. Sensitivity Test

Identify the smallest assumption capable of changing:

```text
ALLOW
↔
BLOCK
```

or:

```text
LOCAL ACTION
↔
ESCALATION
```

Test that premise first when economically and operationally feasible.

Fragile decisions should be:

```text
CONDITIONAL
```

---

## 53. Competing Risk Models

Suppose:

```text
MODEL A → ACCEPTABLE
MODEL B → UNACCEPTABLE
```

and neither dominates under independent evidence.

Result:

```text
COMPETING
```

not:

```text
AVERAGE(A,B) → ACCEPTABLE
```

Seek discriminating evidence.

---

## 54. Safe Default Under Critical Gap

When a critical missing fact prevents reliable risk classification, default toward:

```text
PRESERVE OPTIONS
REDUCE BLAST RADIUS
AVOID IRREVERSIBLE COMMIT
GATHER DISCRIMINATING EVIDENCE
ESCALATE IF REQUIRED
```

rather than pretending the gap is resolved.

---

## 55. Fail-Closed vs Fail-Open

The correct failure mode is domain-dependent.

Examples:

```text
AUTHORITY UNCERTAIN
→ FAIL CLOSED

NONCRITICAL READ CACHE UNAVAILABLE
→ MAY FAIL OPEN TO SOURCE
```

No universal fail-closed rule should be applied outside its scope.

---

## 56. Risk Decision Classes

Canonical outputs:

```text
RC0 — PROHIBITED
RC1 — ESCALATION REQUIRED
RC2 — CONTAIN / STABILIZE ONLY
RC3 — STAGED / LIMITED ACTION
RC4 — CONDITIONALLY ALLOWED
RC5 — ALLOWED WITHIN ENVELOPE
RCX — UNKNOWN/GAP
RCC — COMPETING
```

These are model-level decision classes until formally adopted into canon.

---

## 57. RC0 — Prohibited

Use when a hard constraint is violated and no valid exception authority applies.

```text
ACTION
→ BLOCK
```

---

## 58. RC1 — Escalation Required

Use when:

```text
RISK ACCEPTANCE EXCEEDS LOCAL AUTHORITY
IRREVERSIBILITY IS HIGH
BLAST RADIUS IS LARGE
GOVERNANCE IMPACT IS MATERIAL
```

or policy explicitly requires escalation.

---

## 59. RC2 — Contain / Stabilize Only

Use when immediate harm reduction is justified but complete intervention lacks sufficient validation.

```text
CONTAIN
→ PRESERVE EVIDENCE
→ GATHER INFORMATION
→ REASSESS
```

---

## 60. RC3 — Staged / Limited Action

Use when risk can be bounded through:

```text
CANARY
SHADOW
LIMITED POPULATION
LIMITED STATE
LIMITED TIME
LIMITED AUTHORITY
```

with observable stop conditions.

---

## 61. RC4 — Conditionally Allowed

Use when action is valid only if explicit conditions hold.

Example:

```text
ALLOW A
ONLY IF:
  P1 VALID
  ROLLBACK AVAILABLE
  AUTHORITY EPOCH = E17
  BLAST_RADIUS <= B
```

Failure of any load-bearing condition invalidates the allowance.

---

## 62. RC5 — Allowed Within Envelope

Use when:

```text
CONSTRAINTS SATISFIED
AUTHORITY VALID
SCOPE VALID
EVIDENCE SUFFICIENT
RECOVERY ADEQUATE
RESIDUAL RISK ACCEPTED
```

within the specified envelope.

This is not universal permission.

---

## 63. RCX — Unknown/Gap

Use when material evidence is missing.

```text
UNKNOWN
```

must not be silently transformed into:

```text
ACCEPTABLE
```

---

## 64. RCC — Competing

Use when incompatible risk assessments remain genuinely supported.

Preserve the disagreement until discriminating evidence exists.

---

## 65. Decision Gate

```text
PROPOSED ACTION
↓
SCOPE / REGIME KNOWN?
├── NO → RCX
└── YES
    ↓
HARD CONSTRAINT VIOLATED?
├── YES → RC0
└── NO
    ↓
ACTIVE HARM REQUIRES CONTAINMENT?
├── YES → RC2 / ESCALATE AS REQUIRED
└── NO
    ↓
AUTHORITY VALID?
├── NO → RC1
└── YES
    ↓
BLAST RADIUS / IRREVERSIBILITY HIGH?
├── YES
│   ↓
│   EVIDENCE + RECOVERY SUFFICIENT?
│   ├── NO → RC1 / RCX
│   └── YES → STAGE OR GOVERNED ACTION
└── NO
    ↓
MATERIAL UNCERTAINTY CAN FLIP DECISION?
├── YES → TEST / RC4 / RCX
└── NO
    ↓
CAN RISK BE REDUCED WITH SMALLER ACTION?
├── YES → RC3
└── NO
    ↓
RESIDUAL RISK WITHIN AUTHORIZED ENVELOPE?
├── NO → RC1 / RC0
└── YES → RC5
```

---

## 66. Risk Constraint Invariants

```text
KRC-01
POSSIBILITY MUST NOT BE CONFUSED WITH PERMISSION

KRC-02
CAPABILITY MUST NOT BE CONFUSED WITH AUTHORITY

KRC-03
EXPECTED BENEFIT MUST NOT OVERRIDE HARD CONSTRAINTS

KRC-04
UNKNOWN RISK MUST NOT BE SILENTLY TREATED AS ZERO

KRC-05
ABSENCE OF OBSERVED FAILURE MUST NOT BE TREATED AS PROOF OF SAFETY

KRC-06
RISK MUST REMAIN TYPED WHEN TYPES ARE DECISION-RELEVANT

KRC-07
INCOMPARABLE RISK TYPES MUST NOT BE FORCED INTO A FALSE SCALAR ORDER

KRC-08
RISK CONCLUSIONS MUST INHERIT SCOPE

KRC-09
RISK CONCLUSIONS MUST INHERIT REGIME

KRC-10
STALE EVIDENCE MUST NOT AUTHORIZE CURRENT HIGH-STAKES ACTION WITHOUT REVALIDATION

KRC-11
CORRELATED SOURCES MUST NOT BE COUNTED AS INDEPENDENT CONFIRMATION

KRC-12
CAUSAL CLAIMS MUST NOT EXCEED EVIDENCE TYPE

KRC-13
ROLLBACK DEFINITION MUST NOT BE CONFUSED WITH VALIDATED RECOVERY

KRC-14
HIGH IRREVERSIBILITY REQUIRES HEIGHTENED VALIDATION

KRC-15
HIGH BLAST RADIUS REQUIRES HEIGHTENED VALIDATION

KRC-16
THE LAST VALID RECOVERY PATH MUST NOT BE DESTROYED CASUALLY

KRC-17
REPAIR ACTIONS MUST THEMSELVES PASS RISK CONSTRAINTS

KRC-18
MINIMUM SUFFICIENT INTERVENTION SHOULD BE PREFERRED WHEN OUTCOMES ARE EQUIVALENT

KRC-19
SOFT OPTIMIZATION MUST NOT WEAKEN HARD INTEGRITY CONSTRAINTS

KRC-20
RISK ANALYSIS MUST NOT GRANT ITS OWN ACCEPTANCE AUTHORITY

KRC-21
TOOL ACCESS MUST NOT IMPLY EXECUTION PERMISSION

KRC-22
PERSISTENT COMMIT REQUIRES STRONGER GOVERNANCE THAN TRANSIENT PROPOSAL WHEN CONSEQUENCES DIFFER

KRC-23
MULTI-RSCF COUPLING MUST BE INCLUDED IN BLAST-RADIUS ANALYSIS

KRC-24
STALE MVCC/CAS STATE MUST TRIGGER REVALIDATION WHEN MATERIAL

KRC-25
CAUSAL-EPOCH CHANGE MUST INVALIDATE DEPENDENT RISK CONCLUSIONS

KRC-26
COMPETING RISK MODELS MUST REMAIN COMPETING WITHOUT DISCRIMINATING EVIDENCE

KRC-27
CRITICAL GAPS MUST REMAIN VISIBLE

KRC-28
IRREVERSIBLE EXTERNAL EFFECTS REQUIRE GOVERNED AUTHORITY

KRC-29
RISK REDUCTION MUST NOT CREATE GREATER HIDDEN RISK WITHOUT DISCLOSURE

KRC-30
UNKNOWN/GAP MUST NOT PASS AS VALIDATED SAFETY
```

---

## 67. Required Tests

```text
HARD-CONSTRAINT TEST
SOFT-CONSTRAINT TEST
RISK-TYPE PRESERVATION TEST
SCOPE-FIREWALL TEST
REGIME-SHIFT TEST
FRESHNESS TEST
UNCERTAINTY TEST
PROVENANCE-INDEPENDENCE TEST
CAUSAL-FIREWALL TEST
BLAST-RADIUS TEST
PROPAGATION-RISK TEST
IRREVERSIBILITY TEST
ROLLBACK-VALIDITY TEST
RECOVERY-OPTION TEST
REPAIR-RISK TEST
MINIMUM-INTERVENTION TEST
LEAST-BLAST-RADIUS TEST
STAGED-ACTION TEST
CUMULATIVE-RISK TEST
CORRELATED-RISK TEST
TAIL-RISK TEST
MODEL-RISK TEST
MEASUREMENT-RISK TEST
PROXY-RISK TEST
OPTIMIZATION-FIREWALL TEST
AUTHORITY-BOUNDARY TEST
CAPABILITY-BOUNDARY TEST
EXTERNAL-EFFECT TEST
PERSISTENT-STATE TEST
CANON-MUTATION TEST
MEMORY-ADMISSION TEST
MULTI-RSCF TEST
ATOMICITY TEST
MVCC/CAS TEST
CAUSAL-EPOCH TEST
ADVERSARIAL-VALIDATION TEST
SENSITIVITY TEST
COMPETING-RISK TEST
UNKNOWN-GAP TEST
```

---

## 68. Negative Tests

```text
TOOL CAN DO IT
→ ACTION ALLOWED
MUST FAIL

MODEL CONFIDENCE HIGH
→ ACTION SAFE
MUST FAIL

NO INCIDENT OBSERVED
→ ZERO RISK
MUST FAIL

TEST PASSED ONCE
→ UNIVERSALLY SAFE
MUST FAIL

ROLLBACK COMMAND EXISTS
→ RECOVERY VALIDATED
MUST FAIL

EXPECTED BENEFIT HIGH
→ HARD CONSTRAINT MAY BE IGNORED
MUST FAIL

LOW AVERAGE ERROR
→ LOW TAIL RISK
MUST FAIL

MULTIPLE REPORTS
→ INDEPENDENT CONFIRMATION
MUST FAIL

SIMULATION SAFE
→ PRODUCTION SAFE
MUST FAIL

READ SAFE
→ WRITE SAFE
MUST FAIL

LOCAL SAFE
→ GLOBAL SAFE
MUST FAIL

LOW PROBABILITY
→ IGNORE CATASTROPHIC LOSS
MUST FAIL

REVERSIBLE
→ HARMLESS
MUST FAIL

RISK MODEL SAYS ACCEPT
→ AUTHORITY GRANTED
MUST FAIL

CANON FILE EXISTS
→ CANON PROMOTED
MUST FAIL

FAULT EXISTS
→ ANY REPAIR ALLOWED
MUST FAIL

SMALL INITIAL ERROR
→ SMALL BLAST RADIUS
MUST FAIL

SEPARATE RSCFs
→ INDEPENDENT RISK
MUST FAIL

OLD VALIDATION
→ CURRENT VALIDATION
MUST FAIL

UNKNOWN/GAP
→ ACCEPT
MUST FAIL
```

---

## 69. Failure Modes

```text
RISK COLLAPSE TO SINGLE SCORE
UNKNOWN-AS-ZERO
CONFIDENCE-AS-SAFETY
CAPABILITY-AS-AUTHORITY
BENEFIT-AS-PERMISSION
SCOPE LEAKAGE
REGIME LEAKAGE
STALE VALIDATION
PROVENANCE DOUBLE-COUNTING
CAUSAL OVERREACH
TAIL-RISK BLINDNESS
BLAST-RADIUS UNDERCOUNTING
COMMON-MODE BLINDNESS
FALSE REVERSIBILITY
UNTESTED ROLLBACK
RECOVERY-PATH DESTRUCTION
REPAIR-HARM BLINDNESS
OPTIMIZATION OVERRIDE
PERSISTENCE BLINDNESS
EXTERNAL-EFFECT BLINDNESS
ATOMICITY FAILURE
STALE-COMMIT RISK
PREMATURE RISK CONVERGENCE
AUTHORITY BYPASS
```

---

## 70. Recovery Semantics

If an action violates its risk envelope:

```text
DETECT
↓
STOP FURTHER NONESSENTIAL EFFECT
↓
CONTAIN
↓
PRESERVE EVIDENCE / PROVENANCE
↓
IDENTIFY AFFECTED STATE
↓
INVALIDATE DEPENDENT ASSUMPTIONS
↓
ROLL BACK WHERE VALID AND SAFE
↓
REPAIR MINIMUM FAILED SCOPE
↓
REVALIDATE
↓
REASSESS RISK ENVELOPE
↓
RESUME ONLY THROUGH AUTHORIZED PATH
```

Do not invalidate unrelated valid state merely because one action failed.

---

## 71. Interaction with [[02_KERNEL/06_RISK_REPAIR/K_REPAIR_PRIORITY|K_REPAIR_PRIORITY]]

```text
K_REPAIR_PRIORITY
```

may identify:

```text
REPAIR A FIRST
```

but `K_RISK_CONSTRAINT` can still return:

```text
A = RC1 ESCALATION REQUIRED
```

or:

```text
A = RC3 STAGED ONLY
```

Thus:

```text
HIGH PRIORITY
!=
UNCONSTRAINED EXECUTION
```

---

## 72. Interaction with [[02_KERNEL/06_RISK_REPAIR/K_REPAIR_HARM|K_REPAIR_HARM]]

`K_REPAIR_HARM` provides repair-specific downside analysis.

`K_RISK_CONSTRAINT` places that analysis into the wider action envelope.

```text
REPAIR_HARM
⊂
ACTION_RISK CONTEXT
```

conceptually, without collapsing the two kernel contracts.

---

## 73. Interaction with [[02_KERNEL/06_RISK_REPAIR/K_HOMEOSTASIS|K_HOMEOSTASIS]]

```text
K_HOMEOSTASIS
→ IS SYSTEM STATE OUTSIDE ACCEPTABLE BOUNDS?

K_RISK_CONSTRAINT
→ WHAT CORRECTIVE ACTIONS ARE PERMISSIBLE?

K_REPAIR_PRIORITY
→ WHICH PERMISSIBLE / NECESSARY REPAIR SHOULD BE ADDRESSED FIRST?
```

---

## 74. Interaction with [[02_KERNEL/03_CAUSAL/K_CAUSAL_CLOSURE|K_CAUSAL_CLOSURE]]

Risk propagation across a causal boundary must respect validated causal closure.

Do not infer:

```text
A AFFECTS B
```

merely because:

```text
A AND B CHANGED TOGETHER
```

Where causal closure is unresolved:

```text
MODEL
CONDITIONAL
UNKNOWN/GAP
```

should remain available.

---

## 75. Interaction with [[02_KERNEL/04_STATE/K_SYSTEM_STATE|K_SYSTEM_STATE]]

Risk evaluation is state-relative.

```text
RISK(A | S17)
```

may differ from:

```text
RISK(A | S18)
```

Therefore material state changes can invalidate previous action permission.

---

## 76. Interaction with [[02_KERNEL/04_STATE/K_CONTEXT_STATE|K_CONTEXT_STATE]]

Context may change interpretation and applicability but must not silently override canonical constraints.

```text
CONTEXT
CAN SPECIALIZE
```

but must not fabricate:

```text
AUTHORITY
VALIDATION
PROVENANCE
```

---

## 77. Interaction with [[02_KERNEL/04_STATE/K_EVENT_BUS|K_EVENT_BUS]]

Risk-relevant events may include:

```text
CONSTRAINT_VIOLATION
RISK_ENVELOPE_CHANGED
REGIME_CHANGED
AUTHORITY_CHANGED
RECOVERY_DEGRADED
BLAST_RADIUS_EXPANDED
IRREVERSIBILITY_INCREASED
RISK_ESCALATION_REQUIRED
ACTION_BLOCKED
ACTION_CONDITIONALLY_ALLOWED
```

Event publication itself does not imply policy enforcement unless runtime/control-plane wiring exists.

---

## 78. Proof Capsule

Important risk decisions should conceptually carry:

```yaml
risk_constraint_proof:
  claim:
  conclusion_class:
  action:
  scope:
  regime:
  risk_types: []
  hazards: []
  causal_paths: []
  load_bearing_premises: []
  evidence: []
  provenance: []
  freshness:
  blast_radius:
  irreversibility:
  recoverability:
  uncertainty:
  mitigations: []
  residual_risk:
  authority:
  competing_assessments: []
  falsifiers: []
  invalidation_conditions: []
  confidence_ceiling:
  decision_class:
```

---

## 79. Promotion Gate

Before promotion beyond `AMOS_MODEL`, evidence should establish:

```text
[ ] risk object schema implemented
[ ] typed risk representation implemented
[ ] hard/soft constraint distinction implemented
[ ] scope firewall implemented
[ ] regime firewall implemented
[ ] freshness invalidation implemented
[ ] uncertainty vector implemented
[ ] provenance independence checks implemented
[ ] causal-risk checks implemented
[ ] blast-radius analysis implemented
[ ] propagation-risk handling implemented
[ ] irreversibility handling implemented
[ ] rollback validation implemented
[ ] recovery-option preservation implemented
[ ] repair-harm integration implemented
[ ] authority boundary enforced
[ ] persistent-state constraints tested
[ ] external-effect constraints tested
[ ] multi-RSCF risk handling tested
[ ] atomicity constraints tested
[ ] MVCC/CAS stale-validation handling tested
[ ] causal-epoch invalidation tested
[ ] adversarial validation tested
[ ] competing risk representation implemented
[ ] observability wired
[ ] recovery behavior tested
[ ] unresolved critical gaps registered
```

Until evidenced:

```text
RISK_CONSTRAINT_RUNTIME = UNKNOWN/GAP
AUTOMATED_RISK_CLASSIFICATION = UNKNOWN/GAP
AUTOMATED_BLAST_RADIUS = UNKNOWN/GAP
AUTOMATED_CAUSAL_RISK = UNKNOWN/GAP
AUTOMATED_IRREVERSIBILITY_CLASSIFICATION = UNKNOWN/GAP
AUTOMATED_RECOVERY_VALIDATION = UNKNOWN/GAP
AUTOMATED_RISK_ACCEPTANCE = UNKNOWN/GAP
MULTI_RSCF_RISK_RUNTIME = UNKNOWN/GAP
FORMAL_RISK_BOUND_PROOF = UNKNOWN/GAP
EMPIRICAL_VALIDATION = UNKNOWN/GAP
```

---

## 80. RSCF Node

```RSCF-NODE
node_id: AMOS-OS-K-RISK-CONSTRAINT
node_type: kernel_risk_constraint_contract
domain: AMOS_OS_KERNEL
functional_type: RiskConstraintKernel
lifecycle_stage: Architecture
claim_class: AMOS_MODEL

RSCF-RELATIONS:
  - ROOTED_IN: README
  - DEPENDENCY_BOUND_TO: DEPENDENCY_MAP

  - GOVERNED_BY: AMOS_CORE_LAWS
  - CONSTRAINED_BY: INVARIANT_REGISTRY
  - PRECEDENCE_GOVERNED_BY: LAW_HIERARCHY
  - PROVENANCE_GOVERNED_BY: CANON_PROVENANCE
  - AUTHORITY_BOUND_TO: AUTHORITY_CANON

  - INDEXED_BY: KERNEL_MAP
  - LOGIC_BOUND_TO: K_CORE19_LOGIC
  - META_LOGIC_BOUND_TO: K_META_LOGIC
  - STRUCTURAL_REASONING_BOUND_TO: K_STRUCTURAL_REASONING
  - CAUSAL_CLOSURE_BOUND_TO: K_CAUSAL_CLOSURE
  - CAUSAL_EPOCH_BOUND_TO: K_CAUSAL_EPOCH
  - CONTEXT_BOUND_TO: K_CONTEXT_STATE
  - SYSTEM_STATE_BOUND_TO: K_SYSTEM_STATE

  - HOMEOSTASIS_BOUND_TO: K_HOMEOSTASIS
  - REPAIR_HARM_BOUND_TO: K_REPAIR_HARM
  - REPAIR_PRIORITY_BOUND_TO: K_REPAIR_PRIORITY
  - RECOVERY_BOUND_TO: K_COLLAPSE_RECOVERY

  - MEMORY_ADMISSION_BOUND_TO: K_MEMORY_ADMISSION
  - MEMORY_CONFLICT_BOUND_TO: K_MEMORY_CONFLICT
  - MEMORY_IMMUNE_BOUND_TO: K_MEMORY_IMMUNE

  - STATE_INTERACTION: README
  - SECURITY_CONSTRAINED_BY: README
  - OBSERVED_BY: README
  - VERIFIED_BY: README
  - OPERATED_BY: README
```

---

## 81. Canonical Risk-Constraint Summary

```text
ACTION PROPOSED
↓
WHAT EXACTLY WILL CHANGE?
↓
WHAT IS THE SCOPE?
↓
WHAT REGIME ARE WE IN?
↓
WHAT CAN FAIL?
↓
WHAT CAN BE HARMED?
↓
HOW CAN HARM PROPAGATE?
↓
WHAT IS THE BLAST RADIUS?
↓
IS LOSS REVERSIBLE?
↓
IS RECOVERY ACTUALLY VALIDATED?
↓
WHAT EVIDENCE SUPPORTS THE RISK MODEL?
↓
IS THAT EVIDENCE:
  INDEPENDENT?
  FRESH?
  IN SCOPE?
  CAUSALLY APPROPRIATE?
↓
WHAT IS UNKNOWN?
↓
CAN A SMALLER ACTION ACHIEVE THE SAME GOAL?
↓
CAN THE ACTION BE STAGED?
↓
IS A HARD CONSTRAINT VIOLATED?
├── YES
│   → BLOCK
└── NO
    ↓
IS LOCAL AUTHORITY SUFFICIENT?
├── NO
│   → ESCALATE
└── YES
    ↓
CAN MATERIAL UNCERTAINTY FLIP THE DECISION?
├── YES
│   → TEST / CONDITION / UNKNOWN
└── NO
    ↓
IS RESIDUAL RISK WITHIN THE GOVERNED ENVELOPE?
├── NO
│   → ESCALATE / REJECT
└── YES
    ↓
ALLOW ONLY
WITHIN THE VALIDATED
SCOPE + REGIME + AUTHORITY
ENVELOPE
```

Core laws:

```text
POSSIBLE != PERMISSIBLE
CAPABILITY != AUTHORITY
TOOL != PERMISSION
EXPECTED BENEFIT != RISK ACCEPTANCE
RISK != UNCERTAINTY
RISK != SEVERITY
UNKNOWN != ZERO
NO FAILURE OBSERVED != SAFE
REVERSIBLE != HARMLESS
ROLLBACK EXISTS != RECOVERY VALIDATED
LOCAL SAFETY != GLOBAL SAFETY
SIMULATION SAFETY != PRODUCTION SAFETY
PAST VALIDATION != CURRENT VALIDATION
CORRELATED SOURCES != INDEPENDENT CONFIRMATION
SOFT OPTIMIZATION != LICENSE TO BREAK HARD CONSTRAINTS
HIGH PRIORITY != UNCONSTRAINED EXECUTION
MODEL != AUTHORITY
PROPOSAL != COMMIT
UNKNOWN/GAP != PASS
```

The decisive invariant is:

```text
AMOS DOES NOT ASK ONLY:

CAN THIS ACTION
ACHIEVE THE GOAL?

AMOS ALSO ASKS:

WHAT CAN IT
DAMAGE?

HOW FAR CAN
THAT DAMAGE
PROPAGATE?

WHAT ASSUMPTIONS
MAKE THE ACTION
LOOK SAFE?

ARE THOSE
ASSUMPTIONS
VALID?

ARE THE SOURCES
ACTUALLY
INDEPENDENT?

IS THE EVIDENCE
CURRENT?

IS IT VALID
IN THIS
REGIME?

IS THE
CAUSAL STORY
SUPPORTED?

WHAT HAPPENS
IF THE MODEL
IS WRONG?

WHAT HAPPENS
IF EXECUTION
IS PARTIAL?

WHAT HAPPENS
IF ROLLBACK
FAILS?

WHAT VALID
STATE COULD
BE LOST?

CAN THE SAME
OBJECTIVE BE
ACHIEVED WITH
A SMALLER
BLAST RADIUS?

CAN THE ACTION
BE STAGED?

CAN IT BE
REVERSED?

IS RECOVERY
VALIDATED,
NOT MERELY
DESCRIBED?

WHO HAS
AUTHORITY
TO ACCEPT
THE RESIDUAL
RISK?

IF A HARD
CONSTRAINT
FAILS,

AMOS DOES
NOT OPTIMIZE
AROUND IT.

IF RISK IS
HIGH AND
REVERSIBILITY
IS LOW,

VALIDATION
INCREASES.

IF A CRITICAL
FACT IS
UNKNOWN,

AMOS DOES
NOT TURN
UNKNOWN
INTO ZERO.

IF TWO
RISK MODELS
GENUINELY
DISAGREE,

AMOS DOES
NOT AVERAGE
THEM INTO
FALSE CERTAINTY.

IT PRESERVES:

COMPETING.

IF THE
DECISION CANNOT
BE VALIDLY
SUPPORTED,

IT RETURNS:

UNKNOWN/GAP.

AND EVEN
WHEN AN ACTION
IS VALID,

ITS PERMISSION
REMAINS BOUNDED
BY:

SCOPE,
REGIME,
FRESHNESS,
AUTHORITY,
RECOVERY,
AND
PROVENANCE.
```

## Related

README ·
[[00_ROOT/DEPENDENCY_MAP|DEPENDENCY_MAP]] ·
[[01_CANON/01_CORE_LAWS/AMOS_CORE_LAWS|AMOS_CORE_LAWS]] ·
[[01_CANON/01_CORE_LAWS/INVARIANT_REGISTRY|INVARIANT_REGISTRY]] ·
[[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] ·
[[01_CANON/07_PROVENANCE/CANON_PROVENANCE|CANON_PROVENANCE]] ·
[[01_CANON/04_INFRASTRUCTURE_CANON/AUTHORITY_CANON|AUTHORITY_CANON]] ·
[[02_KERNEL/00_INDEX/KERNEL_MAP|KERNEL_MAP]] ·
[[02_KERNEL/01_META_LOGIC/K_CORE19_LOGIC|K_CORE19_LOGIC]] ·
[[02_KERNEL/01_META_LOGIC/K_META_LOGIC|K_META_LOGIC]] ·
[[02_KERNEL/02_COGNITION/K_STRUCTURAL_REASONING|K_STRUCTURAL_REASONING]] ·
[[02_KERNEL/03_CAUSAL/K_CAUSAL_CLOSURE|K_CAUSAL_CLOSURE]] ·
[[02_KERNEL/03_CAUSAL/K_CAUSAL_EPOCH|K_CAUSAL_EPOCH]] ·
[[02_KERNEL/04_STATE/K_CONTEXT_STATE|K_CONTEXT_STATE]] ·
[[02_KERNEL/04_STATE/K_SYSTEM_STATE|K_SYSTEM_STATE]] ·
[[02_KERNEL/06_RISK_REPAIR/K_HOMEOSTASIS|K_HOMEOSTASIS]] ·
[[02_KERNEL/06_RISK_REPAIR/K_REPAIR_HARM|K_REPAIR_HARM]] ·
[[02_KERNEL/06_RISK_REPAIR/K_REPAIR_PRIORITY|K_REPAIR_PRIORITY]] ·
[[02_KERNEL/06_RISK_REPAIR/K_COLLAPSE_RECOVERY|K_COLLAPSE_RECOVERY]] ·
[[02_KERNEL/05_MEMORY/K_MEMORY_ADMISSION|K_MEMORY_ADMISSION]] ·
[[02_KERNEL/05_MEMORY/K_MEMORY_CONFLICT|K_MEMORY_CONFLICT]] ·
[[02_KERNEL/05_MEMORY/K_MEMORY_IMMUNE|K_MEMORY_IMMUNE]] ·
README ·
README ·
README ·
README ·
README

```text

**Classification note:** this is substantive replacement content for the placeholder at `02_KERNEL/K_RISK_CONSTRAINT.md`, classified as **AMOS_MODEL**. It defines the proposed kernel contract but does **not** establish implementation, runtime enforcement, empirical validation, formal proof, or final-canon promotion. Those remain `UNKNOWN/GAP` pending provenance, conflict resolution, implementation evidence, tests, and explicit promotion.
```

---

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]|[[00_ROOT/AMOS MOC|AMOS MOC]]

---
**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

---
**MOC:** [[02_KERNEL/06_RISK_REPAIR/06_RISK_REPAIR_MOC|06_RISK_REPAIR_MOC]]

