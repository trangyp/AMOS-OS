---
canon-group: meta
canon-type: framework
rscf-state: source-claim
topic: Mode Conflict Registry
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---

# MODE CONFLICT REGISTRY

`MODE_CONFLICT_REGISTRY.md` in Drive is also only the reservation placeholder; there is no substantive canonical implementation in that artifact to reproduce verbatim.

______________________________________________________________________

artifact_id: AMOS-OS-MODE-CONFLICT-REGISTRY
title: AMOS OS Mode Conflict Registry
canonical_name: MODE_CONFLICT_REGISTRY

artifact_class: GOVERNED_REGISTRY
subsystem: MODE_GOVERNANCE
origin_architect: Trang Phan
amos_core_target: v4.4

status: CANDIDATE_CANON
conclusion_class: DERIVED

source_state:
existing_file: PLACEHOLDER
recovered_substantive_implementation: false

related_artifacts:

- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_ADMISSION_QUEUE|MODE_ADMISSION_QUEUE]].md
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_COMPOSITION_REGISTRY|MODE_COMPOSITION_REGISTRY]].md
- [[03_CONTROL_PLANE/01_TASK_CONTRACT/TASK_CONTRACT|TASK_CONTRACT]].md
- [[03_CONTROL_PLANE/01_TASK_CONTRACT/TASK_RESOLVER|TASK_RESOLVER]].md
- [[03_CONTROL_PLANE/02_CAPABILITY/CAPABILITY_RESOLVER|CAPABILITY_RESOLVER]].md
- [[02_KERNEL/04_STATE/K_SYSTEM_STATE|K_SYSTEM_STATE]]
- [[02_KERNEL/09_INTEGRATION/K_GMEF|K_GMEF]]
- [[02_KERNEL/09_INTEGRATION/K_RSCF|K_RSCF]]
- [[02_KERNEL/09_INTEGRATION/K_HML|K_HML]]
- [[02_KERNEL/09_INTEGRATION/K_BINDING|K_BINDING]]
- [[02_KERNEL/09_INTEGRATION/K_CONSTRAINT_PROPAGATION|K_CONSTRAINT_PROPAGATION]]
- [[02_KERNEL/07_AUTHORITY/K_CAPABILITY_AUTHORIZATION|K_CAPABILITY_AUTHORIZATION]]
- [[02_KERNEL/06_RISK_REPAIR/K_RISK_CONSTRAINT|K_RISK_CONSTRAINT]]
- [[02_KERNEL/07_AUTHORITY/K_EFFECT_CLASSIFICATION|K_EFFECT_CLASSIFICATION]]
- [[02_KERNEL/07_AUTHORITY/K_INFORMATION_EXPOSURE|K_INFORMATION_EXPOSURE]]
- [[02_KERNEL/08_PROVENANCE/K_PROVENANCE|K_PROVENANCE]]
- [[02_KERNEL/08_PROVENANCE/K_PROVENANCE_TOPOLOGY|K_PROVENANCE_TOPOLOGY]]
- [[02_KERNEL/08_PROVENANCE/K_SYBIL_HARDENING|K_SYBIL_HARDENING]]
- [[02_KERNEL/07_AUTHORITY/K_COMMIT_TIME_AUTHORITY|K_COMMIT_TIME_AUTHORITY]]
- [[02_KERNEL/06_RISK_REPAIR/K_COLLAPSE_RECOVERY|K_COLLAPSE_RECOVERY]]
- [[02_KERNEL/06_RISK_REPAIR/K_HOMEOSTASIS|K_HOMEOSTASIS]]
- [[02_KERNEL/06_RISK_REPAIR/K_REPAIR_HARM|K_REPAIR_HARM]]
- [[02_KERNEL/06_RISK_REPAIR/K_REPAIR_PRIORITY|K_REPAIR_PRIORITY]]

implementation_status: SPECIFICATION
formal_verification_status: NOT_CLAIMED
empirical_validation_status: NOT_CLAIMED

## promotion_required: true

## MODE CONFLICT REGISTRY — part 2

> **Status:** `CANDIDATE_CANON`
>
> **Conclusion class:** `DERIVED`
>
> **AMOS CORE target:** `v4.4`
>
> **Origin Architect:** Trang Phan

______________________________________________________________________

## 0. PURPOSE

`MODE_CONFLICT_REGISTRY` is the governed AMOS OS registry for representing,
classifying, preserving, resolving, superseding, invalidating, and auditing
conflicts involving operating modes.

Its purpose is not merely to record that two modes are "incompatible."

It preserves the complete conflict object:

```text
WHAT CONFLICTS?

WHY?

ON WHICH DIMENSION?

UNDER WHICH SCOPE?

UNDER WHICH REGIME?

AT WHICH VERSION?

WITH WHICH AUTHORITY?

WITH WHICH EFFECTS?

BASED ON WHICH EVIDENCE?

DO THE SUPPORTING SOURCES SHARE ANCESTRY?

IS THE CONFLICT HARD OR CONDITIONAL?

CAN IT BE REPAIRED?

CAN IT BE DISCRIMINATED?

CAN IT BE SAFELY DEFERRED?

WHAT WOULD INVALIDATE IT?

WHAT DEPENDS ON ITS RESOLUTION?
```

The registry therefore acts as the conflict-preservation and
conflict-resolution layer of AMOS mode governance.

______________________________________________________________________

## 1. CORE LAW

```text
CONFLICT
IS INFORMATION.
```

Therefore:

```text
DETECTED CONFLICT
≠
ERROR TO HIDE
```

and:

```text
UNRESOLVED CONFLICT
≠
PERMISSION TO GUESS
```

The integrity-preserving response may be:

```text
COMPETING

CONDITIONAL

BLOCKED

DEGRADED

UNKNOWN/GAP
```

rather than forced convergence.

______________________________________________________________________

## 2. CONFLICT BOUNDARY

Hard distinction:

```text
DIFFERENCE
!=
CONFLICT

CONFLICT
!=
INCOMPATIBILITY

INCOMPATIBILITY
!=
GLOBAL INVALIDITY

CONFLICT DETECTION
!=
CONFLICT RESOLUTION

CONFLICT RESOLUTION
!=
CONFLICT DELETION
```

A conflict may exist only:

```text
ON ONE DIMENSION

IN ONE SCOPE

IN ONE REGIME

FOR ONE VERSION

DURING ONE EPOCH

UNDER ONE AUTHORITY STATE
```

while the modes remain compatible elsewhere.

______________________________________________________________________

## 3. WHY THE REGISTRY EXISTS

Without explicit conflict governance, a resolver may silently do one of the
following:

```text
PICK THE FIRST CLAIM

PICK THE NEWEST CLAIM

PICK THE MOST POPULAR CLAIM

PICK THE HIGHEST-CONFIDENCE CLAIM

PICK THE MOST AUTHORITATIVE-SOUNDING CLAIM

MERGE INCOMPATIBLE CLAIMS

DROP THE MINORITY CLAIM

AVERAGE NON-COMPARABLE VALUES

TREAT UNKNOWN AS FALSE

TREAT UNKNOWN AS TRUE

RETRY A FAILED PATH

RECOMPUTE EVERYTHING
```

AMOS must instead preserve the actual epistemic and operational structure.

______________________________________________________________________

## 4. REGISTRY ROLE

Conceptually:

```text
MODE ADMISSION
      ↓
MODE COMPOSITION
      ↓
CONFLICT DETECTION
      ↓
MODE CONFLICT REGISTRY
      ↓
CONFLICT CLASSIFICATION
      ↓
PROVENANCE / SCOPE / REGIME ANALYSIS
      ↓
DISCRIMINATING TEST OR POLICY RESOLUTION
      ↓
RESOLVED / COMPETING / CONDITIONAL / BLOCKED
      ↓
DEPENDENT PLAN UPDATE
```

______________________________________________________________________

## 5. REGISTRY OBJECT

```yaml
ModeConflictRegistry:

  registry_id:

  schema_version:

  registry_version:

  epoch:

  policy_epoch:

  authority_epoch:

  provenance_epoch:

  conflicts: {}

  conflict_sets: {}

  resolutions: {}

  supersession_records: {}

  dependency_edges: {}

  invalidation_records: {}

  unresolved_conflicts: []

  created_at:

  updated_at:
```

______________________________________________________________________

## 6. CONFLICT RECORD

```yaml
ModeConflictRecord:

  conflict_id:

  conflict_class:

  conflict_type:

  participants: []

  claims: []

  dimensions: []

  scope:

  regime:

  versions:

  conditions:

  evidence:

  provenance:

  provenance_topology:

  independence:

  authority:

  capabilities:

  constraints:

  effects:

  risk:

  causal_structure:

  dependencies:

  competing_explanations: []

  discriminating_tests: []

  resolution_state:

  resolution:

  confidence_ceiling:

  freshness:

  falsifiers: []

  invalidation_conditions: []

  lifecycle:

  conclusion_class:
```

______________________________________________________________________

## 7. CONFLICT IDENTITY

Conflict identity should include enough information to distinguish materially
different conflicts.

Conceptually:

```text
ConflictIdentity
=
(
  Participants,
  Claims,
  Dimension,
  Scope,
  Regime,
  Versions,
  Conditions
)
```

Therefore:

```text
Conflict(A,B,Authority)
```

is not necessarily the same object as:

```text
Conflict(A,B,State)
```

______________________________________________________________________

## 8. PARTICIPANTS

Conflict participants may include:

```text
MODE ↔ MODE

MODE ↔ TASK CONTRACT

MODE ↔ CAPABILITY

MODE ↔ CONSTRAINT

MODE ↔ AUTHORITY

MODE ↔ EFFECT POLICY

MODE ↔ SYSTEM STATE

MODE ↔ REGIME

MODE ↔ PROVENANCE REQUIREMENT

MODE ↔ GOVERNANCE RULE

MODE ↔ MODE COMPOSITION

COMPOSITION ↔ COMPOSITION
```

The registry should not assume every conflict is mode-vs-mode.

______________________________________________________________________

## 9. CLAIM MODEL

A conflict exists when two or more load-bearing claims cannot simultaneously
hold within the same applicability envelope.

Conceptually:

```text
Claim A
∧
Claim B
∧
SameRelevantEnvelope
→
Unsatisfiable
```

______________________________________________________________________

## 10. CONFLICT PREDICATE

```text
Conflict(A,B | E)
```

where:

```text
E =
(
  scope,
  regime,
  time,
  version,
  authority,
  assumptions
)
```

A conflict outside shared envelope `E` may be only apparent.

______________________________________________________________________

## 11. APPARENT CONFLICT

Example:

```text
A:
Mode X compatible with Y
under NORMAL

B:
Mode X incompatible with Y
under EMERGENCY
```

These statements do not necessarily conflict.

Correct result:

```text
REGIME-PARTITIONED CLAIMS
```

not:

```text
CONTRADICTION
```

______________________________________________________________________

## 12. TRUE CONFLICT

A true conflict requires incompatible claims inside materially overlapping
applicability envelopes.

______________________________________________________________________

## 13. CONFLICT CLASSES

Candidate classes:

```text
HARD

SOFT

CONDITIONAL

TEMPORAL

VERSIONED

REGIME_BOUND

SCOPE_BOUND

AUTHORITY_BOUND

RESOURCE_BOUND

STATE_BOUND

POLICY_BOUND

EPISTEMIC

CAUSAL

PROVENANCE

EXECUTION

SUPERSESSION

UNKNOWN
```

These remain specification-level classifications until canonically fixed.

______________________________________________________________________

## 14. HARD CONFLICT

A hard conflict means both requirements cannot be satisfied simultaneously.

Example:

```text
A requires:

STATE = READ_ONLY

B requires:

STATE = WRITE_ACTIVE
```

under a state model where those states are mutually exclusive.

______________________________________________________________________

## 15. SOFT CONFLICT

A soft conflict means both modes can coexist, but not at full preferred
semantics.

Possible resolution:

```text
DEGRADE A

DEGRADE B

SERIALIZE

RESTRICT EFFECTS

CHANGE PRIORITY
```

______________________________________________________________________

## 16. CONDITIONAL CONFLICT

```text
Conflict(A,B | condition=true)
```

but:

```text
Compatible(A,B | condition=false)
```

Conditions must remain attached.

______________________________________________________________________

## 17. TEMPORAL CONFLICT

Modes may conflict only during overlapping execution windows.

Example:

```text
A and B
cannot own resource R
simultaneously
```

but may execute sequentially.

______________________________________________________________________

## 18. VERSION CONFLICT

```text
A@v1 compatible B@v3

A@v2 incompatible B@v3
```

Do not generalize across versions.

______________________________________________________________________

## 19. REGIME CONFLICT

```text
NORMAL:
A+B allowed

EMERGENCY:
A+B blocked
```

The conflict registry must preserve regime typing.

______________________________________________________________________

## 20. SCOPE CONFLICT

Example:

```text
A valid:
SUBSYSTEM S1

B valid:
SUBSYSTEM S2
```

An apparent contradiction may disappear when scopes are separated.

______________________________________________________________________

## 21. AUTHORITY CONFLICT

Example:

```text
A requires authority:
WRITE

B requires:
NO_WRITE
```

If both apply to the same operation:

```text
AUTHORITY_CONFLICT
```

______________________________________________________________________

## 22. CAPABILITY CONFLICT

Example:

```text
A requires CAPABILITY_X

B forbids CAPABILITY_X
```

The resolver must not silently choose one.

______________________________________________________________________

## 23. CONSTRAINT CONFLICT

```text
Constraint_A ∩ Constraint_B = ∅
```

where intersection semantics are valid.

Result:

```text
UNSATISFIABLE COMPOSITION
```

______________________________________________________________________

## 24. EFFECT CONFLICT

Example:

```text
A:
external_write = REQUIRED

B:
external_write = FORBIDDEN
```

If both are load-bearing:

```text
EFFECT_CONFLICT
```

______________________________________________________________________

## 25. INFORMATION EXPOSURE CONFLICT

Example:

```text
DEBUG MODE:
requires verbose internals

EXTERNAL INTERFACE MODE:
forbids internal disclosure
```

The conflict may be resolvable through redaction or isolation.

______________________________________________________________________

## 26. STATE CONFLICT

Modes may require mutually exclusive system states.

```text
StateRequirements(A)
∩
StateRequirements(B)
=
∅
```

______________________________________________________________________

## 27. RESOURCE CONFLICT

Example:

```text
A requires exclusive R

B requires exclusive R
```

Possible resolution:

```text
SERIALIZATION
```

if simultaneous ownership is not required.

______________________________________________________________________

## 28. POLICY CONFLICT

A mode may satisfy technical constraints but violate governance policy.

Policy conflict cannot be resolved merely through technical compatibility.

______________________________________________________________________

## 29. EPISTEMIC CONFLICT

Two evidence-backed claims may disagree.

Example:

```text
H1:
A compatible B

H2:
A incompatible B
```

If neither dominates under valid evidence rules:

```text
COMPETING
```

______________________________________________________________________

## 30. CAUSAL CONFLICT

Two modes may contain incompatible causal assumptions.

Example:

```text
MODE A MODEL:
X causes Y

MODE B MODEL:
Y causes X
```

Structural disagreement must be preserved unless discriminating evidence
exists.

______________________________________________________________________

## 31. PROVENANCE CONFLICT

Examples:

```text
SAME CLAIM
DIFFERENT ORIGINS
WITH INCOMPATIBLE DETAILS
```

or:

```text
CLAIM A SAYS SOURCE = S1

CLAIM B SAYS SOURCE = S2
```

when source identity matters to validity.

______________________________________________________________________

## 32. SUPERSESSION CONFLICT

Two artifacts may each claim canonical precedence.

Example:

```text
A supersedes B

C supersedes B
```

without established ordering between `A` and `C`.

Result:

```text
SUPERSESSION_CONFLICT
```

______________________________________________________________________

## 33. EXECUTION CONFLICT

A composition may be semantically valid but operationally impossible in the
current execution environment.

Example:

```text
A requires resource R

B requires resource S

R and S individually exist

but cannot be allocated atomically
```

______________________________________________________________________

## 34. UNKNOWN CONFLICT

When the nature of a detected incompatibility cannot yet be typed:

```text
conflict_type = UNKNOWN
```

Do not fabricate classification.

______________________________________________________________________

## 35. CONFLICT DIMENSIONS

A conflict record may include multiple dimensions:

```yaml
dimensions:

  - STATE

  - AUTHORITY

  - CAPABILITY

  - EFFECT

  - RISK

  - RESOURCE

  - SCOPE

  - REGIME

  - VERSION

  - TEMPORAL

  - CAUSAL

  - PROVENANCE

  - GOVERNANCE
```

______________________________________________________________________

## 36. MULTI-DIMENSION CONFLICT

A single conflict may be both:

```text
AUTHORITY
+
EFFECT
+
RISK
```

Do not collapse multi-dimensional conflicts into one generic label.

______________________________________________________________________

## 37. CONFLICT GRAPH

Conceptually:

```text
          MODE A
          /    \
   STATE/      \AUTHORITY
       /        \
    MODE B     MODE C
       \        /
        \EFFECT/
         MODE D
```

Edges remain typed.

______________________________________________________________________

## 38. CONFLICT HYPERGRAPH

Some conflicts are higher-order.

Example:

```text
A+B valid

A+C valid

B+C valid

A+B+C invalid
```

Represent:

```text
Conflict({A,B,C})
```

rather than inventing a false pairwise conflict.

______________________________________________________________________

## 39. PAIRWISE FIREWALL

```text
NoConflict(A,B)
∧
NoConflict(A,C)
∧
NoConflict(B,C)

↛

NoConflict(A,B,C)
```

______________________________________________________________________

## 40. CONFLICT SET

```yaml
ModeConflictSet:

  conflict_set_id:

  members: []

  interaction_order:

  shared_dimensions: []

  triggering_conditions: []

  provenance:

  resolution_state:
```

______________________________________________________________________

## 41. CONFLICT DETECTION PIPELINE

```text
REQUESTED COMPOSITION
       ↓
LOAD MODE CONTRACTS
       ↓
LOAD MATERIAL RELATIONS
       ↓
DEPENDENCY CLOSURE
       ↓
CONSTRAINT PROPAGATION
       ↓
STATE COMPARISON
       ↓
AUTHORITY COMPARISON
       ↓
CAPABILITY COMPARISON
       ↓
EFFECT COMPARISON
       ↓
RISK INTERACTION
       ↓
SCOPE / REGIME / VERSION ALIGNMENT
       ↓
CAUSAL INTERACTION CHECK
       ↓
PROVENANCE CHECK
       ↓
CONFLICT RECORD
```

______________________________________________________________________

## 42. CONFLICT NORMALIZATION

Before declaring conflict, normalize:

```text
IDENTITY

VERSION

SCOPE

REGIME

TIME

MEASUREMENT

UNITS

TERMINOLOGY

POLICY EPOCH
```

where relevant.

______________________________________________________________________

## 43. TERMINOLOGY CONFLICT

Different labels do not prove semantic conflict.

Example:

```text
READ_ONLY
```

and:

```text
NO_MUTATION
```

may or may not be equivalent.

Translation requires explicit semantic binding.

______________________________________________________________________

## 44. SAME WORD FIREWALL

Likewise, identical terminology does not prove identical semantics.

```text
"SAFE"
```

in two modes may have different operational definitions.

______________________________________________________________________

## 45. SCOPE ALIGNMENT

Before conflict comparison:

```text
ScopeOverlap =
Scope(A) ∩ Scope(B)
```

If:

```text
ScopeOverlap = ∅
```

there may be no operational conflict.

______________________________________________________________________

## 46. REGIME ALIGNMENT

Compare claims only where regime envelopes overlap.

______________________________________________________________________

## 47. TEMPORAL ALIGNMENT

Two claims valid in different periods may represent evolution rather than
contradiction.

______________________________________________________________________

## 48. VERSION ALIGNMENT

Conflict detection must compare relevant versions, not merely mode names.

______________________________________________________________________

## 49. PROVENANCE MODEL

Each conflicting claim should retain:

```text
SOURCE IDENTITY

ANCESTRY

TRANSFORMATION PATH

TIMESTAMP

VERSION

VALIDATION STATE

CORRELATION RISK
```

______________________________________________________________________

## 50. PROVENANCE TOPOLOGY

Example:

```text
SOURCE S
├── CLAIM A1
├── CLAIM A2
└── CLAIM A3
```

These are not three independent supports.

______________________________________________________________________

## 51. SYBIL HARDENING

Conflict resolution must resist:

```text
REPETITION

MIRRORING

FORKING

REPACKAGING

CITATION LOOPS

DERIVATIVE MAJORITY
```

______________________________________________________________________

## 52. SOURCE COUNT FIREWALL

```text
NumberOfDocuments
!=
NumberOfIndependentSources
```

______________________________________________________________________

## 53. AUTHORITY FIREWALL

Authority alone does not erase contradictory evidence.

Authority may govern a decision while epistemic conflict remains recorded.

This distinction is critical:

```text
DECISION RESOLVED
!=
EVIDENCE CONFLICT RESOLVED
```

______________________________________________________________________

## 54. DECISION VS TRUTH

A policy may decide:

```text
USE MODE A
```

while the registry still records:

```text
A vs B evidence = COMPETING
```

Governance selection must not rewrite epistemic state.

______________________________________________________________________

## 55. CONFLICT STATES

Candidate lifecycle states:

```text
DETECTED

NORMALIZING

VALIDATING

COMPETING

BLOCKING

CONDITIONAL

DEFERRED

RESOLVED

SUPERSEDED

INVALIDATED

REOPENED
```

______________________________________________________________________

## 56. DETECTED

A potential conflict has been identified but not fully validated.

______________________________________________________________________

## 57. NORMALIZING

Identity, scope, regime, versions, or terminology are being aligned.

______________________________________________________________________

## 58. VALIDATING

Evidence and provenance are being checked.

______________________________________________________________________

## 59. COMPETING

Two or more materially incompatible claims remain supported.

______________________________________________________________________

## 60. BLOCKING

The conflict prevents safe composition or execution.

______________________________________________________________________

## 61. CONDITIONAL

Conflict exists only under explicit conditions.

______________________________________________________________________

## 62. DEFERRED

Resolution is intentionally postponed because:

```text
NO CURRENT DECISION DEPENDS ON IT
```

or:

```text
RESOLUTION COST > CURRENT DECISION VALUE
```

provided deferral is safe.

______________________________________________________________________

## 63. RESOLVED

A valid resolution has been established for the declared envelope.

______________________________________________________________________

## 64. SUPERSEDED

A newer governed resolution replaces the previous one.

The old record remains in lineage.

______________________________________________________________________

## 65. INVALIDATED

The conflict itself was based on a failed premise.

Example:

```text
A and B appeared to conflict

but

A referred to v1
B referred to v2
```

______________________________________________________________________

## 66. REOPENED

A previously resolved conflict may reopen when:

```text
NEW EVIDENCE

VERSION CHANGE

REGIME SHIFT

POLICY CHANGE

AUTHORITY CHANGE

PROVENANCE CORRECTION

FAILED FALSIFIER

SUPERSESSION DISPUTE
```

occurs.

______________________________________________________________________

## 67. CONFLICT SEVERITY

Severity should reflect consequence, not rhetorical intensity.

Candidate dimensions:

```text
DECISION IMPACT

IRREVERSIBILITY

BLAST RADIUS

AUTHORITY IMPACT

EFFECT IMPACT

SAFETY IMPACT

DEPENDENCY COUNT

RECOVERY COST
```

______________________________________________________________________

## 68. SEVERITY ≠ CONFIDENCE

A conflict may be:

```text
HIGH SEVERITY
LOW CONFIDENCE
```

or:

```text
LOW SEVERITY
HIGH CONFIDENCE
```

Keep these dimensions separate.

______________________________________________________________________

## 69. CONFLICT PRIORITY

Conceptually:

```text
Priority =
f(
  DecisionImpact,
  Irreversibility,
  BlastRadius,
  DependencyCentrality,
  ResolutionValue,
  ResolutionCost
)
```

No universal numeric formula is asserted.

______________________________________________________________________

## 70. GAPS

Conflict gaps should use:

```text
CRITICAL

DECISION-RELEVANT

EXPLANATORY

COSMETIC
```

______________________________________________________________________

## 71. CRITICAL CONFLICT GAP

A missing fact without which a high-stakes conflict cannot be safely resolved.

______________________________________________________________________

## 72. DECISION-RELEVANT GAP

Could change the selected composition or action.

______________________________________________________________________

## 73. EXPLANATORY GAP

Does not currently change the decision.

______________________________________________________________________

## 74. COSMETIC GAP

Non-semantic registry metadata.

______________________________________________________________________

## 75. RESOLUTION PRINCIPLE

Conflict resolution should seek:

```text
THE CHEAPEST
HIGH-INFORMATION
DISCRIMINATING TEST
```

rather than accumulating redundant evidence.

______________________________________________________________________

## 76. DISCRIMINATING TEST

```yaml
ConflictDiscriminatingTest:

  test_id:

  conflict_id:

  hypotheses: []

  observation:

  expected_if_h1:

  expected_if_h2:

  cost:

  reversibility:

  information_value:

  authority_required:

  risk:

  result:

  provenance:
```

______________________________________________________________________

## 77. TEST SELECTION

Prefer a test that can change the decision.

Avoid tests that merely generate more correlated evidence.

______________________________________________________________________

## 78. RESOLUTION METHODS

Candidate methods:

```text
SCOPE_PARTITION

REGIME_PARTITION

VERSION_PARTITION

TEMPORAL_SERIALIZATION

CONSTRAINT_TIGHTENING

CAPABILITY_RESTRICTION

AUTHORITY_RESOLUTION

EFFECT_RESTRICTION

MODE_DEGRADATION

MODE_SUSPENSION

MODE_EXCLUSION

MODE_SUBSTITUTION

PRIORITY_RULE

DISCRIMINATING_TEST

CANONICAL_SUPERSESSION

POLICY_DECISION

KEEP_COMPETING
```

______________________________________________________________________

## 79. SCOPE PARTITION

Example:

```text
A valid in S1

B valid in S2
```

Resolution:

```text
PARTITION BY SCOPE
```

not arbitrary winner selection.

______________________________________________________________________

## 80. REGIME PARTITION

```text
NORMAL → A

EMERGENCY → B
```

if supported.

______________________________________________________________________

## 81. VERSION PARTITION

```text
v1 → relation R1

v2 → relation R2
```

______________________________________________________________________

## 82. TEMPORAL SERIALIZATION

If modes conflict only concurrently:

```text
A
then
B
```

may resolve the conflict.

______________________________________________________________________

## 83. CONSTRAINT TIGHTENING

A soft conflict may be resolved by adopting a valid stricter common
constraint.

______________________________________________________________________

## 84. CAPABILITY RESTRICTION

Example:

```text
A+B
allowed

only with:
CAPABILITY_X disabled
```

Result:

```text
VALID_WITH_CONDITIONS
```

______________________________________________________________________

## 85. EFFECT RESTRICTION

Example:

```text
A+B
valid only under
READ_ONLY
```

______________________________________________________________________

## 86. MODE DEGRADATION

```text
A(full) + B(full)
invalid

A(degraded) + B(full)
valid
```

The degraded semantics must be explicit.

______________________________________________________________________

## 87. MODE SUSPENSION

A higher-priority mode may temporarily suspend another.

Suspension does not necessarily revoke admission.

______________________________________________________________________

## 88. MODE EXCLUSION

When no safe composition exists:

```text
EXCLUDE ONE OR MORE MODES
```

according to governed priority and task sufficiency.

______________________________________________________________________

## 89. MODE SUBSTITUTION

Substitution requires an explicit equivalence/substitutability relation.

Similarity is insufficient.

______________________________________________________________________

## 90. PRIORITY RULE

A policy may specify dominance on one dimension.

Example:

```text
SAFETY
DOMINATES
PERFORMANCE
ON
EXTERNAL EFFECT PERMISSION
```

Do not infer global dominance.

______________________________________________________________________

## 91. KEEP COMPETING

If evidence remains incomparable:

```text
KEEP COMPETING
```

is a valid terminal epistemic state.

______________________________________________________________________

## 92. NO FORCED CONVERGENCE

```text
H1 supported

H2 supported

No discriminating evidence
```

must not become:

```text
H1 wins
```

merely because a single answer is convenient.

______________________________________________________________________

## 93. CONFLICT RESOLUTION RECORD

```yaml
ModeConflictResolution:

  resolution_id:

  conflict_id:

  state_before:

  state_after:

  method:

  selected_outcome:

  rejected_outcomes: []

  preserved_competing_claims: []

  premises:

  evidence:

  provenance:

  authority_basis:

  scope:

  regime:

  versions:

  conditions:

  falsifiers:

  invalidation_conditions:

  timestamp:
```

______________________________________________________________________

## 94. RESOLUTION CLASS

Resolution conclusion classes:

```text
VERIFIED

DERIVED

MODEL

CONDITIONAL

COMPETING

UNKNOWN/GAP
```

______________________________________________________________________

## 95. CONFIDENCE CEILING

```text
Confidence(Resolution)
<=
WeakestLoadBearingPremise
```

unless independently revalidated.

______________________________________________________________________

## 96. RESOLUTION DOES NOT ERASE HISTORY

```text
RESOLVE
!=
DELETE
```

Preserve:

```text
ORIGINAL CLAIMS

ORIGINAL EVIDENCE

PROVENANCE

PREVIOUS STATES

DECISION BASIS

SUPERSESSION PATH
```

______________________________________________________________________

## 97. CONFLICT LINEAGE

Conceptually:

```text
CONFLICT C1
   ↓
RESOLUTION R1
   ↓
NEW EVIDENCE
   ↓
REOPEN C1
   ↓
RESOLUTION R2
```

Do not overwrite `R1`.

______________________________________________________________________

## 98. SUPERSESSION

```yaml
ConflictSupersessionRecord:

  supersession_id:

  old_resolution:

  new_resolution:

  authority:

  reason:

  provenance:

  effective_from:

  scope:

  regime:
```

______________________________________________________________________

## 99. SUPERSESSION FIREWALL

```text
NEWER
!=
SUPERSEDING
```

Supersession requires valid lineage and authority.

______________________________________________________________________

## 100. DEPENDENCY TRACKING

Conflict resolutions may support downstream objects.

```text
Conflict Resolution R
├── Composition Plan P1
├── Task Plan T1
└── Capability Decision C1
```

If `R` fails, invalidate dependent conclusions.

______________________________________________________________________

## 101. SELECTIVE INVALIDATION

```text
INVALIDATE
ONLY
DEPENDENT DESCENDANTS
```

not the entire registry.

______________________________________________________________________

## 102. INVALIDATION RECORD

```yaml
ConflictInvalidation:

  invalidation_id:

  target:

  failed_premise:

  cause:

  affected_descendants: []

  unaffected_objects: []

  timestamp:

  provenance:
```

______________________________________________________________________

## 103. FAILURE RECOVERY

```text
RESOLUTION FAILS
      ↓
IDENTIFY FAILED PREMISE
      ↓
TRACE DEPENDENTS
      ↓
INVALIDATE LOCAL CLOSURE
      ↓
RESTORE NEAREST VALID STATE
      ↓
SEARCH ALTERNATIVE
```

______________________________________________________________________

## 104. NEAREST VALID STATE

Do not return automatically to global baseline.

Return to the nearest state whose load-bearing premises remain valid.

______________________________________________________________________

## 105. NO FAILED-PATH LOOP

```text
FAILED PATH
+
UNCHANGED EVIDENCE
+
UNCHANGED STATE
→
DO NOT RETRY
```

______________________________________________________________________

## 106. REPAIR HARM

Before resolving a conflict through modification, consider whether repair
creates greater harm than the original conflict.

Conceptually:

```text
RepairAllowed
only if
ExpectedRepairHarm
<
ExpectedUnresolvedConflictHarm
```

subject to governance.

______________________________________________________________________

## 107. REPAIR PRIORITY

Prefer:

```text
REVERSIBLE

LOCAL

LOW-BLAST-RADIUS

PROVENANCE-PRESERVING

CONSTRAINT-PRESERVING
```

repairs.

______________________________________________________________________

## 108. HOMEOSTASIS

Repeated conflict oscillation may indicate unstable mode composition.

Example:

```text
A enabled
→ B conflict
→ disable B
→ C conflict
→ enable B
→ A conflict
```

The registry should preserve enough lineage to detect such loops.

______________________________________________________________________

## 109. OSCILLATION

Candidate state:

```text
CONFLICT_OSCILLATION
```

may be recorded when repeated repairs recreate prior invalid states.

______________________________________________________________________

## 110. COLLAPSE RECOVERY

If conflict resolution causes broad state collapse:

```text
STOP PROPAGATION

PRESERVE VALID STATE

IDENTIFY FIRST FAILED EDGE

ROLL BACK LOCAL DESCENDANTS

REBUILD ONLY REQUIRED CLOSURE
```

______________________________________________________________________

## 111. TASK CONTRACT

Task contracts constrain allowable conflict resolutions.

Example:

```text
TASK CONTRACT:
external_write = forbidden

Conflict resolution:
enable external_write
```

is invalid even if it would reconcile two modes.

______________________________________________________________________

## 112. TASK SUFFICIENCY

A conflict does not always need complete theoretical resolution.

If a safe task action exists that is invariant across competing hypotheses:

```text
ACT ON INVARIANT SAFE INTERSECTION
```

while preserving the unresolved conflict.

______________________________________________________________________

## 113. SAFE INTERSECTION

Given:

```text
H1 permits {A,B}

H2 permits {A,C}
```

common safe action:

```text
{A}
```

may be sufficient.

______________________________________________________________________

## 114. ACTION SUFFICIENCY

Stop resolving when remaining uncertainty cannot change the safe action.

This does not mean the conflict is epistemically solved.

______________________________________________________________________

## 115. CAPABILITY RESOLVER

Conflict resolution may constrain capability selection.

```text
MODE CONFLICT
      ↓
CAPABILITY RESTRICTION
      ↓
CAPABILITY RESOLVER
```

______________________________________________________________________

## 116. CAPABILITY AUTHORIZATION

A conflict resolution cannot authorize a capability merely because it would
make the conflict disappear.

______________________________________________________________________

## 117. RISK CONSTRAINT

High-risk conflicts require stronger validation.

Escalation triggers include:

```text
IRREVERSIBILITY

SAFETY EXPOSURE

LEGAL EXPOSURE

FINANCIAL EXPOSURE

PRIVILEGED ACCESS

LARGE BLAST RADIUS

INSTITUTIONAL IMPACT
```

______________________________________________________________________

## 118. EFFECT CLASSIFICATION

Conflict resolution must classify the effects of proposed repairs.

A repair that changes:

```text
READ
→
WRITE
```

or:

```text
REVERSIBLE
→
IRREVERSIBLE
```

requires escalation.

______________________________________________________________________

## 119. INFORMATION EXPOSURE

Conflict diagnostics must not unnecessarily expose protected internal
information.

Preserve the conflict record while respecting exposure policy.

______________________________________________________________________

## 120. BINDING

A conflict resolution should remain bound to:

```text
CONFLICT

TASK

MODE SET

SCOPE

REGIME

AUTHORITY

POLICY

PROVENANCE

EPOCH
```

______________________________________________________________________

## 121. CONSTRAINT PROPAGATION

Resolved constraints must propagate to dependent composition plans.

______________________________________________________________________

## 122. PROPAGATION FIREWALL

Do not propagate a local conflict resolution beyond its validated envelope.

______________________________________________________________________

## 123. CAUSAL FIREWALL

A conflict between outcomes does not prove causal incompatibility.

Distinguish:

```text
ASSOCIATION CONFLICT

MECHANISM CONFLICT

CAUSAL DIRECTION CONFLICT

INTERVENTION EFFECT CONFLICT

CONFOUNDING MODEL CONFLICT
```

______________________________________________________________________

## 124. CAUSAL COMPETING HYPOTHESES

Example:

```text
H1:
A causes failure F

H2:
B causes failure F

H3:
C confounds A and F
```

Do not collapse these without discriminating evidence.

______________________________________________________________________

## 125. COUNTERFACTUAL TEST

Where appropriate, a causal conflict may ask:

```text
IF A WERE ABSENT
WHILE RELEVANT CONDITIONS
WERE HELD FIXED,
WOULD F CHANGE?
```

Counterfactual reasoning remains `MODEL` unless supported by appropriate
evidence.

______________________________________________________________________

## 126. SENSITIVITY

Identify the smallest premise that can flip conflict resolution.

Example:

```text
P:
A and B share resource R
```

If:

```text
¬P
```

then conflict disappears.

Test `P` first.

______________________________________________________________________

## 127. UNCERTAINTY VECTOR

```text
Uconflict =
(
  evidence,
  model,
  scope,
  temporal,
  causal,
  execution,
  provenance_independence,
  authority,
  interaction
)
```

______________________________________________________________________

## 128. CONFLICT ROBUSTNESS

A conflict is robust when plausible changes to noncritical assumptions do not
remove it.

______________________________________________________________________

## 129. FRAGILE CONFLICT

If one uncertain premise determines whether the conflict exists:

```text
CONDITIONAL
```

is the appropriate class.

______________________________________________________________________

## 130. ADVERSARIAL VALIDATION

For consequential conflicts, challenge the conflict itself:

```text
IS THIS ACTUALLY THE SAME MODE?

IS THIS THE SAME VERSION?

DO THE SCOPES OVERLAP?

DO THE REGIMES OVERLAP?

ARE THE CLAIMS REALLY INCOMPATIBLE?

IS TERMINOLOGY BEING MISALIGNED?

DO SOURCES SHARE ANCESTRY?

IS ONE CLAIM STALE?

IS THERE A HIDDEN THIRD VARIABLE?

IS THE CONFLICT ONLY TEMPORAL?

CAN SERIALIZATION REMOVE IT?

IS AUTHORITY THE REAL CONFLICT?

IS THE CONFLICT HIGHER-ORDER?

DOES THE PROPOSED RESOLUTION CREATE A WORSE CONFLICT?
```

______________________________________________________________________

## 131. FALSIFIERS

Conflict falsifiers may include:

```text
SCOPE DISJOINTNESS

REGIME DISJOINTNESS

VERSION DISJOINTNESS

TERMINOLOGY RECONCILIATION

DEPENDENCY CORRECTION

PROVENANCE CORRECTION

RESOURCE INDEPENDENCE

SUCCESSFUL DISCRIMINATING TEST

CANONICAL SUPERSESSION

CAUSAL MODEL FAILURE
```

______________________________________________________________________

## 132. RSCF INTEGRATION

```yaml
ModeConflictRSCF:

  claim:
    conflict_exists:

  participants:

  conflict_type:

  premises:

  evidence:

  provenance:

  scope:

  regime:

  versions:

  dependencies:

  competing_explanations:

  discriminating_tests:

  falsifiers:

  resolution_state:

  confidence_ceiling:

  invalidation_conditions:
```

______________________________________________________________________

## 133. RECURSIVE RSCF

```text
CONFLICT RSCF
│
├── CLAIM A RSCF
├── CLAIM B RSCF
├── SCOPE RSCF
├── REGIME RSCF
├── PROVENANCE RSCF
├── AUTHORITY RSCF
├── EFFECT RSCF
├── CAUSAL RSCF
└── RESOLUTION RSCF
```

______________________________________________________________________

## 134. ATOMIC MULTI-RSCF

When conflict resolution depends jointly on multiple claims, evaluate the
load-bearing RSCFs against a coherent state where material.

______________________________________________________________________

## 135. GMEF INTEGRATION

A conflict resolution that changes canonical mode relationships may constitute
governed evolution.

Examples:

```text
NEW INCOMPATIBILITY

NEW DOMINANCE RULE

NEW AUTHORITY PRECEDENCE

NEW EFFECT RESTRICTION

NEW SUPERSESSION RELATION
```

Such changes require appropriate evolution governance.

______________________________________________________________________

## 136. H/M/L INTEGRATION

Suggested retrieval:

```text
BOOTSTRAP
↓
H MODE GOVERNANCE
↓
M CONFLICT MANAGEMENT
↓
L SPECIFIC CONFLICT
↓
RAW EVIDENCE ONLY IF REQUIRED
```

______________________________________________________________________

## 137. FAST PATH

Local conflict resolution is allowed only when:

```text
CONFLICT IDENTITY CLEAR

SCOPE ALIGNED

REGIME ALIGNED

VERSIONS ALIGNED

PROVENANCE SUFFICIENT

NO CORRELATED-EVIDENCE AMBIGUITY

RESOLUTION LOCAL

NO CAUSAL COUPLING

NO IRREVERSIBLE EFFECT ESCALATION

NO GOVERNANCE CHANGE

NO HIGHER-ORDER DEPENDENCY
```

______________________________________________________________________

## 138. ESCALATION

Escalate when:

```text
CONFLICT IS HIGH STAKES

PROVENANCE IS AMBIGUOUS

SOURCES SHARE ANCESTRY

SCOPE IS UNCERTAIN

REGIME IS SHIFTING

CAUSAL MODELS COMPETE

AUTHORITY CONFLICTS

RESOLUTION IS IRREVERSIBLE

CONFLICT AFFECTS GOVERNANCE

DEPENDENCY CLOSURE IS LARGE

HIGHER-ORDER INTERACTION EXISTS
```

______________________________________________________________________

## 139. MVCC PATTERN

Conceptually:

```text
READ CONFLICT STATE @ V1
       ↓
BUILD RESOLUTION
       ↓
VALIDATE
       ↓
CHECK LOAD-BEARING READ SET
       ↓
UNCHANGED?
 /             \
YES             NO
 |               |
COMMIT          REVALIDATE
```

This is a reasoning pattern, not a claim of literal runtime implementation.

______________________________________________________________________

## 140. READ SET

Conflict resolution read set may include:

```text
CONFLICT RECORD

MODE VERSIONS

COMPOSITION RELATIONS

SYSTEM STATE

POLICY

AUTHORITY

REGIME

PROVENANCE

DEPENDENCIES

EFFECT STATE
```

______________________________________________________________________

## 141. CAS PATTERN

Conceptually:

```text
IF
CONFLICT_VERSION == EXPECTED
AND
POLICY_EPOCH == EXPECTED
AND
AUTHORITY_EPOCH == EXPECTED
THEN
FINALIZE RESOLUTION
ELSE
REVALIDATE
```

______________________________________________________________________

## 142. CAUSAL EPOCH FINALITY

A conflict resolved under causal state `E1` must not silently remain final
after a material transition to `E2`.

______________________________________________________________________

## 143. LOCAL FINALIZATION

Local conflict resolution may avoid global coordination only when independence
is demonstrated.

Required proof may include:

```text
NO SHARED LOAD-BEARING STATE

NO CROSS-MODE AUTHORITY EFFECT

NO GLOBAL INVARIANT

NO SHARED EFFECT TARGET

NO CAUSAL COUPLING
```

______________________________________________________________________

## 144. EVENT MODEL

Candidate events:

```text
MODE_CONFLICT_DETECTED

MODE_CONFLICT_VALIDATED

MODE_CONFLICT_COMPETING

MODE_CONFLICT_BLOCKING

MODE_CONFLICT_CONDITIONAL

MODE_CONFLICT_RESOLVED

MODE_CONFLICT_DEFERRED

MODE_CONFLICT_INVALIDATED

MODE_CONFLICT_REOPENED

MODE_CONFLICT_SUPERSEDED
```

Exact event identifiers remain specification-level.

______________________________________________________________________

## 145. EVENT RECORD

```yaml
ModeConflictEvent:

  event_id:

  conflict_id:

  event_type:

  participants:

  state_before:

  state_after:

  resolution_id:

  actor:

  registry_version:

  epoch:

  provenance:

  timestamp:
```

______________________________________________________________________

## 146. EVENT IDEMPOTENCE

Duplicate delivery must not create duplicate semantic conflicts or resolutions.

______________________________________________________________________

## 147. OBSERVABILITY

The registry should make it possible to answer:

```text
WHAT CONFLICTS EXIST?

WHICH ARE BLOCKING?

WHICH ARE COMPETING?

WHICH ARE CONDITIONAL?

WHICH ARE STALE?

WHICH WERE REOPENED?

WHICH MODES ARE MOST CONFLICT-CENTRAL?

WHICH CONFLICTS SHARE PROVENANCE?

WHICH RESOLUTIONS HAVE LARGE DEPENDENCY CLOSURES?

WHICH CONFLICTS HAVE NO DISCRIMINATING TEST?

WHICH RESOLUTIONS ARE FRAGILE?
```

______________________________________________________________________

## 148. METRICS

Conceptually:

```yaml
metrics:

  total_conflicts:

  blocking_conflicts:

  competing_conflicts:

  conditional_conflicts:

  unresolved_conflicts:

  resolved_conflicts:

  reopened_conflicts:

  stale_conflicts:

  high_severity_conflicts:

  provenance_ambiguous_conflicts:

  nary_conflicts:

  mean_resolution_age:

  invalidated_resolutions:
```

Metrics do not establish correctness.

______________________________________________________________________

## 149. MACHINE-READABLE REGISTRY

```yaml
mode_conflict_registry:

  schema_version:

  registry_version:

  epoch:

  conflicts:

    - conflict_id:

      participants: []

      claims: []

      conflict_class:

      conflict_type:

      dimensions: []

      scope:

      regime:

      versions:

      conditions: []

      evidence: []

      provenance:

      provenance_topology:

      independence:

      authority:

      capabilities:

      constraints:

      effects:

      risk:

      causal_structure:

      competing_explanations: []

      discriminating_tests: []

      resolution_state:

      resolution:

      conclusion_class:

      confidence_ceiling:

      freshness:

      falsifiers: []

      invalidation_conditions: []

  conflict_sets: []

  resolutions: []

  supersession: []

  invalidations: []
```

______________________________________________________________________

## 150. DETECTION PSEUDOCODE

```text
function detect_mode_conflicts(mode_set, context):

    modes =
        resolve_mode_identities(mode_set)

    closure =
        load_material_dependency_closure(modes)

    normalize(
        identity,
        terminology,
        versions,
        scope,
        regime,
        time
    )

    claims =
        collect_load_bearing_claims(closure)

    constraints =
        propagate_constraints(claims)

    candidate_conflicts =
        compare(
            state,
            authority,
            capability,
            constraints,
            effects,
            risk,
            resources,
            causal_models
        )

    for candidate in candidate_conflicts:

        if scopes_do_not_overlap(candidate):
            classify_as_non_conflict_partition()

        elif regimes_do_not_overlap(candidate):
            classify_as_regime_partition()

        elif versions_do_not_overlap(candidate):
            classify_as_version_partition()

        else:
            validate_provenance(candidate)

            collapse_correlated_sources(candidate)

            register_conflict(candidate)

    check_higher_order_interactions(mode_set)

    return conflict_set
```

______________________________________________________________________

## 151. RESOLUTION PSEUDOCODE

```text
function resolve_mode_conflict(conflict, context):

    if conflict.invalidated:
        return NO_ACTIVE_CONFLICT

    align_scope_regime_version(conflict)

    if not true_overlap(conflict):
        return PARTITIONED

    hypotheses =
        construct_competing_explanations(conflict)

    evidence =
        validate_evidence_and_provenance(conflict)

    if evidence_insufficient:
        return UNKNOWN_OR_COMPETING

    sensitivity =
        identify_flip_premise(conflict)

    test =
        choose_cheapest_high_information_test(
            hypotheses,
            sensitivity
        )

    if safe_and_worthwhile(test):
        result =
            execute_or_request_test(test)

        update_conflict(result)

    if conflict_still_competing:
        safe_action =
            derive_safe_intersection(conflict)

        if safe_action sufficient:
            return {
                decision: safe_action,
                epistemic_state: COMPETING
            }

        return COMPETING

    resolution =
        construct_minimal_valid_resolution(conflict)

    adversarially_validate(resolution)

    record_read_set(resolution)

    return resolution
```

______________________________________________________________________

## 152. FINALIZATION PSEUDOCODE

```text
function finalize_conflict_resolution(resolution):

    if load_bearing_state_changed:
        revalidate

    if authority_changed:
        reauthorize

    if regime_changed:
        revalidate

    if new_conflict_detected:
        reopen_or_abort

    persist_lineage(resolution)

    invalidate_only_dependent_objects()

    emit_resolution_event()
```

______________________________________________________________________

## 153. FAILURE REGISTRY

```text
MCR-CF01 FALSE_CONFLICT

MCR-CF02 MISSED_CONFLICT

MCR-CF03 SCOPE_COLLAPSE

MCR-CF04 REGIME_COLLAPSE

MCR-CF05 VERSION_COLLAPSE

MCR-CF06 TERMINOLOGY_COLLAPSE

MCR-CF07 PROVENANCE_COLLAPSE

MCR-CF08 SYBIL_MAJORITY

MCR-CF09 AUTHORITY_OVERRIDES_EVIDENCE

MCR-CF10 EVIDENCE_OVERRIDES_POLICY

MCR-CF11 FORCED_CONVERGENCE

MCR-CF12 PAIRWISE_OVERREACH

MCR-CF13 HIDDEN_NARY_CONFLICT

MCR-CF14 STALE_RESOLUTION

MCR-CF15 GLOBAL_INVALIDATION

MCR-CF16 FAILED_PATH_LOOP

MCR-CF17 REPAIR_ESCALATION

MCR-CF18 EFFECT_ESCALATION

MCR-CF19 CONFLICT_OSCILLATION

MCR-CF20 LINEAGE_LOSS
```

______________________________________________________________________

## 154. FALSE CONFLICT

Two claims appear incompatible only because their envelopes differ.

Repair:

```text
PARTITION
```

rather than resolve.

______________________________________________________________________

## 155. MISSED CONFLICT

Two modes appear individually valid but violate a shared invariant when
composed.

______________________________________________________________________

## 156. PROVENANCE COLLAPSE

Multiple derivative claims are incorrectly counted as independent support.

______________________________________________________________________

## 157. AUTHORITY OVERRIDES EVIDENCE

Unsafe:

```text
AUTHORIZED PERSON CHOSE H1
→
H1 IS EMPIRICALLY TRUE
```

Authority may select action, not manufacture evidence.

______________________________________________________________________

## 158. EVIDENCE OVERRIDES POLICY

Unsafe:

```text
EVIDENCE SUPPORTS ACTION
→
ACTION AUTHORIZED
```

Evidence and authority are separate predicates.

______________________________________________________________________

## 159. FORCED CONVERGENCE

Unsafe:

```text
H1 ≈ H2
→
AVERAGE THEM
```

when hypotheses are structurally incompatible.

______________________________________________________________________

## 160. STALE RESOLUTION

A valid old resolution may become invalid after:

```text
VERSION CHANGE

REGIME CHANGE

POLICY CHANGE

AUTHORITY CHANGE

SYSTEM STATE CHANGE

NEW EVIDENCE
```

______________________________________________________________________

## 161. GLOBAL INVALIDATION FAILURE

One failed conflict premise should not invalidate unrelated mode relations.

______________________________________________________________________

## 162. FAILED PATH LOOP

Do not repeatedly apply a resolution already shown invalid under unchanged
conditions.

______________________________________________________________________

## 163. REPAIR ESCALATION

A repair may solve a local conflict while creating a larger downstream
conflict.

Every consequential repair therefore needs downstream effect evaluation.

______________________________________________________________________

## 164. PROPERTY TESTS

```text
Different(A,B)
↛
Conflict(A,B)
```

```text
Conflict(A,B,S1)
↛
Conflict(A,B,S2)
```

```text
Conflict(A@v1,B)
↛
Conflict(A@v2,B)
```

```text
ResolvedForDecision(C)
↛
EpistemicallyResolved(C)
```

```text
DocumentsSupporting(H1)=10
↛
IndependentSources(H1)=10
```

______________________________________________________________________

## 165. SCOPE TEST

Create two contradictory claims with disjoint scopes.

Expected:

```text
NO TRUE CONFLICT
```

______________________________________________________________________

## 166. REGIME TEST

Create opposite relations under different regimes.

Expected:

```text
REGIME_PARTITION
```

not forced contradiction.

______________________________________________________________________

## 167. VERSION TEST

Create opposite relations for different versions.

Expected:

```text
VERSION_PARTITION
```

______________________________________________________________________

## 168. PROVENANCE TEST

Copy one source into ten files.

Expected:

```text
ONE PROVENANCE FAMILY
```

______________________________________________________________________

## 169. COMPETING TEST

Provide two independently supported incompatible claims with no discriminating
evidence.

Expected:

```text
COMPETING
```

______________________________________________________________________

## 170. POLICY TEST

Policy chooses one operational action while evidence remains competing.

Expected:

```text
DECISION = RESOLVED

EPISTEMIC CONFLICT = PRESERVED
```

______________________________________________________________________

## 171. N-ARY TEST

```text
AB valid
AC valid
BC valid
ABC invalid
```

Expected:

```text
REGISTER N-ARY CONFLICT
```

without inventing pairwise incompatibility.

______________________________________________________________________

## 172. INVALIDATION TEST

Invalidate one premise of resolution `R1`.

Expected:

```text
R1 INVALIDATED

ONLY R1 DEPENDENTS INVALIDATED

UNRELATED RESOLUTIONS PRESERVED
```

______________________________________________________________________

## 173. OSCILLATION TEST

Repeatedly apply two locally valid repairs that recreate each other's
conflicts.

Expected:

```text
DETECT OSCILLATION
AND ESCALATE
```

rather than loop indefinitely.

______________________________________________________________________

## 174. COMMIT-TIME TEST

Change authority after resolution planning but before finalization.

Expected:

```text
REVALIDATE
```

______________________________________________________________________

## 175. ERROR REGISTRY

```yaml
ModeConflictErrors:

  E_MCR_CONFLICT_UNKNOWN:
    meaning: conflict existence cannot be established

  E_MCR_CONFLICT_BLOCKING:
    meaning: unresolved conflict blocks composition

  E_MCR_SCOPE_AMBIGUOUS:
    meaning: conflict scope cannot be aligned

  E_MCR_REGIME_AMBIGUOUS:
    meaning: applicable regime cannot be established

  E_MCR_VERSION_AMBIGUOUS:
    meaning: participant versions cannot be established

  E_MCR_PROVENANCE:
    meaning: evidence ancestry is insufficiently known

  E_MCR_SYBIL:
    meaning: apparent support depends on correlated provenance

  E_MCR_AUTHORITY:
    meaning: resolution lacks required authority

  E_MCR_EFFECT:
    meaning: proposed resolution violates effect constraints

  E_MCR_RISK:
    meaning: proposed resolution exceeds risk envelope

  E_MCR_CAUSAL:
    meaning: causal conflict remains unresolved

  E_MCR_COMPETING:
    meaning: incompatible hypotheses remain materially supported

  E_MCR_STALE:
    meaning: resolution freshness conditions failed

  E_MCR_NARY:
    meaning: higher-order conflict detected

  E_MCR_REPAIR:
    meaning: proposed repair creates unacceptable downstream harm

  E_MCR_OSCILLATION:
    meaning: conflict resolution loop detected

  E_MCR_SUPERSESSION:
    meaning: canonical supersession cannot be determined

  E_MCR_UNKNOWN:
    meaning: unresolved registry failure
```

______________________________________________________________________

## 176. PROOF CAPSULE

```yaml
ModeConflictProofCapsule:

  conflict_id:

  claim:
    statement:
    class:

  participants:

  claims:

  conflict_type:

  dimensions:

  premises:

  evidence:

  provenance:

  provenance_topology:

  independence:

  scope:

  regime:

  versions:

  authority:

  constraints:

  effects:

  risk:

  causal_structure:

  competing_explanations:

  discriminating_tests:

  selected_resolution:

  preserved_competing_claims:

  falsifiers:

  uncertainty:

  confidence_ceiling:

  invalidation_conditions:
```

______________________________________________________________________

## 177. KNOWN GAPS

```yaml
KnownGaps:

  - id: MCR-GAP-001
    class: DECISION-RELEVANT
    issue: >
      Existing MODE_CONFLICT_REGISTRY.md is only a placeholder;
      no substantive canonical implementation was recovered from it.

  - id: MCR-GAP-002
    class: DECISION-RELEVANT
    issue: >
      Exact canonical conflict-type enumeration has not been
      independently recovered from authoritative implementation source.

  - id: MCR-GAP-003
    class: UNKNOWN/GAP
    issue: >
      Exact persistence and runtime indexing mechanism for conflict
      records is not established.

  - id: MCR-GAP-004
    class: UNKNOWN/GAP
    issue: >
      Exact event identifiers and transport semantics are not established.

  - id: MCR-GAP-005
    class: DECISION-RELEVANT
    issue: >
      Exact binding among MODE_CONFLICT_REGISTRY,
      MODE_COMPOSITION_REGISTRY, TASK_RESOLVER,
      CAPABILITY_RESOLVER, and runtime activation requires
      canonical confirmation.

  - id: MCR-GAP-006
    class: UNKNOWN/GAP
    issue: >
      No universal numeric conflict severity, confidence, or
      escalation thresholds are asserted here.
```

______________________________________________________________________

## 178. CANON PROMOTION CHECKLIST

```text
[ ] canonical location confirmed

[ ] provenance lineage registered

[ ] conflict identity schema approved

[ ] conflict type enum approved

[ ] conflict dimension enum approved

[ ] n-ary conflict representation approved

[ ] scope partition semantics approved

[ ] regime partition semantics approved

[ ] version partition semantics approved

[ ] authority conflict semantics approved

[ ] capability conflict semantics approved

[ ] constraint conflict semantics approved

[ ] effect conflict semantics approved

[ ] causal conflict semantics approved

[ ] provenance topology integration approved

[ ] Sybil hardening tested

[ ] competing-hypothesis preservation tested

[ ] discriminating-test contract approved

[ ] resolution lifecycle approved

[ ] supersession semantics approved

[ ] selective invalidation verified

[ ] repair harm integration verified

[ ] repair priority integration verified

[ ] collapse recovery integration verified

[ ] RSCF integration verified

[ ] GMEF integration verified

[ ] H/M/L mapping verified

[ ] MVCC/read-set semantics verified

[ ] commit-time authority semantics verified

[ ] oscillation detection tested

[ ] authoritative-state record updated

[ ] steward approval completed
```

______________________________________________________________________

## 179. CANONICAL COMPRESSION

```text
MODE CONFLICT REGISTRY
=
THE GOVERNED MEMORY
OF DISAGREEMENT
INSIDE AMOS MODE GOVERNANCE.

A DIFFERENCE
IS NOT AUTOMATICALLY
A CONFLICT.

A CONFLICT
IS NOT AUTOMATICALLY
GLOBAL INCOMPATIBILITY.

BEFORE DECLARING CONFLICT,
ALIGN:

IDENTITY,
VERSION,
SCOPE,
REGIME,
TIME,
TERMINOLOGY,
AND POLICY EPOCH.

WHEN TWO CLAIMS
CANNOT BOTH HOLD
INSIDE THE SAME
LOAD-BEARING ENVELOPE,
REGISTER THE CONFLICT.

DO NOT HIDE IT.

DO NOT AVERAGE IT.

DO NOT PICK
THE MOST REPEATED CLAIM.

DO NOT COUNT
DESCENDANTS OF ONE SOURCE
AS INDEPENDENT CONFIRMATION.

DO NOT LET AUTHORITY
MANUFACTURE TRUTH.

DO NOT LET EVIDENCE
MANUFACTURE AUTHORITY.

IF CONFLICT IS
SCOPE-DEPENDENT,
PARTITION BY SCOPE.

IF REGIME-DEPENDENT,
PARTITION BY REGIME.

IF VERSION-DEPENDENT,
PARTITION BY VERSION.

IF TEMPORAL,
SERIALIZE WHEN VALID.

IF CONDITIONAL,
PRESERVE THE CONDITION.

IF A CHEAP
HIGH-INFORMATION TEST
CAN DISCRIMINATE,
TEST THE LOAD-BEARING
UNCERTAINTY FIRST.

IF TWO HYPOTHESES
REMAIN SUPPORTED
AND INCOMPARABLE,
KEEP THEM COMPETING.

IF A SAFE ACTION
IS COMMON TO ALL
LIVE HYPOTHESES,
THE SYSTEM MAY ACT
ON THAT SAFE INTERSECTION
WITHOUT PRETENDING
THE CONFLICT IS SOLVED.

WHEN A RESOLUTION FAILS,
INVALIDATE ONLY
THE DEPENDENT CONCLUSIONS.

ROLL BACK
TO THE NEAREST
VALID STATE.

DO NOT REPEAT
A FAILED PATH
WITHOUT CHANGED EVIDENCE.

DO NOT RECOMPUTE
THE WHOLE SYSTEM
WHEN LOCAL REPAIR
IS SUFFICIENT.

PRESERVE
CONFLICT LINEAGE,
PROVENANCE,
FALSIFIERS,
SCOPE,
REGIME,
AUTHORITY,
AND INVALIDATION CONDITIONS.

CONFLICT
IS NOT NOISE.

CONFLICT
IS STRUCTURED INFORMATION
ABOUT WHERE
THE CURRENT MODEL,
POLICY,
EVIDENCE,
OR MODE SET
CANNOT YET
COHERENTLY CLOSE.
```

______________________________________________________________________

## 180. MASTER CONTRACT

Conceptually:

```text
ModeConflictRegistry
:
(
  ModeSet,
  ModeClaims,
  CompositionState,
  TaskContract,
  Constraints,
  Capabilities,
  Authority,
  Effects,
  SystemState,
  Scope,
  Regime,
  Versions,
  Provenance,
  RiskState
)
→
(
  ConflictSet,
  ConflictClasses,
  CompetingHypotheses,
  DiscriminatingTests,
  ResolutionState,
  SafeActionEnvelope,
  InvalidationConditions
)
```

subject to:

```text
INTEGRITY

PROVENANCE PRESERVATION

CONTRADICTION VISIBILITY

SCOPE CORRECTNESS

REGIME CORRECTNESS

VERSION CORRECTNESS

CAUSAL DISCIPLINE

AUTHORITY DISCIPLINE

EFFECT DISCIPLINE

RISK DISCIPLINE

NO FALSE CONVERGENCE

SELECTIVE INVALIDATION

LOCAL REPAIR

LINEAGE PRESERVATION
```

______________________________________________________________________

## 181. FINAL LAW

```text
WHEN TWO MODES,
CLAIMS,
CONSTRAINTS,
AUTHORITIES,
OR COMPOSITIONS
APPEAR TO DISAGREE,

DO NOT FIRST ASK:

"WHICH ONE WINS?"

ASK:

"ARE THEY ACTUALLY
ABOUT THE SAME THING?"

THEN:

"ARE THEY THE SAME VERSION?"

THEN:

"DO THEIR SCOPES OVERLAP?"

THEN:

"DO THEIR REGIMES OVERLAP?"

THEN:

"ARE THEY VALID
AT THE SAME TIME?"

THEN:

"ARE THEIR TERMS
SEMANTICALLY EQUIVALENT?"

THEN:

"DO THEIR SOURCES
HAVE INDEPENDENT ANCESTRY?"

THEN:

"IS ONE PREMISE STALE?"

THEN:

"IS THE CONFLICT
STATE,
AUTHORITY,
CAPABILITY,
CONSTRAINT,
EFFECT,
RISK,
RESOURCE,
POLICY,
PROVENANCE,
OR CAUSAL?"

THEN:

"IS IT PAIRWISE
OR HIGHER-ORDER?"

THEN:

"WHAT IS THE SMALLEST
PREMISE THAT COULD
FLIP THE RESULT?"

THEN:

"WHAT IS THE CHEAPEST
HIGH-INFORMATION TEST
THAT CAN DISCRIMINATE?"

THEN:

"CAN A SAFE ACTION
BE TAKEN WITHOUT
RESOLVING THE ENTIRE
EPISTEMIC CONFLICT?"

AND IF
NO VALID EVIDENCE
SELECTS A WINNER,

DO NOT INVENT ONE.

RETURN:

COMPETING

OR:

UNKNOWN/GAP.

THE PURPOSE
OF THE REGISTRY
IS NOT TO MAKE
CONFLICT DISAPPEAR.

IT IS TO MAKE
CONFLICT EXPLICIT,
TYPED,
PROVENANCE-AWARE,
SCOPE-BOUND,
REGIME-BOUND,
REPAIRABLE,
AUDITABLE,
AND SAFE TO REASON OVER.
```

## END — MODE CONFLICT REGISTRY

```

This should be treated as `DERIVED / CANDIDATE_CANON`, not recovered original canon: the actual Drive artifact currently contains only the placeholder reservation and explicitly says not to treat that placeholder as implemented logic or final canon.
```

______________________________________________________________________

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] · [[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

______________________________________________________________________

RSCF-NODE
node_id: mode_conflict_registry
node_type: note
path: 03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_CONFLICT_REGISTRY.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
  claim_class: AMOS_MODEL

______________________________________________________________________

**MOC:** [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/00_MODE_INDEX_MOC|00_MODE_INDEX_MOC]]
