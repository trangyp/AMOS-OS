---
title: K CAUSAL EPOCH
artifact_id: AMOS-OS-K-CAUSAL-EPOCH
canonical_name: K_CAUSAL_EPOCH
artifact_type: kernel_causal_epoch_contract
status: AMOS_MODEL
conclusion_class: AMOS_MODEL
amos_core_target: v4.4

origin_architect: Trang Phan
steward: Trang Phan

plane: KERNEL
kernel_family: CAUSAL
domain: causal-epoch
scope: AMOS_OS

created: 2026-08-25
updated: 2026-08-25

tags:
  - amos-os
  - canon-group/tech-ai
  - canon/model
  - kernel
  - kernel/causal
  - kernel/causal-epoch
  - kernel/causal-finality
  - kernel/dependency
  - kernel/provenance
  - kernel/state
  - kernel/regime
  - kernel/freshness
  - kernel/concurrency
  - kernel/rscf
  - kernel/validation
  - kernel/recovery
  - causal/epoch
  - causal/lineage
  - causal/finality
  - causal/closure
  - provenance/topology
  - provenance/persistence
  - state/authoritative
  - rscf/state/model
  - topic/causal-epoch
  - topic/causal-finality
  - topic/epoch-boundary

aliases:
  - AMOS Causal Epoch Kernel
  - Causal Epoch Kernel
  - K Causal Epoch
  - K_CAUSAL_EPOCH
---


# K CAUSAL EPOCH

> **AMOS Core target:** `v4.4`  
> **Origin architect / steward:** Trang Phan  
> **Plane:** `02_KERNEL`  
> **Status:** `AMOS_MODEL`  
> **Conclusion class:** `AMOS_MODEL`

## Purpose

`K_CAUSAL_EPOCH` defines the AMOS kernel model for establishing, identifying, validating, finalizing, superseding, and recovering **bounded causal epochs**.

A causal epoch is a validity interval in which a defined causal state may be treated as internally coherent under an explicit set of:

```text
CAUSAL DEPENDENCIES
PROVENANCE
SCOPE
REGIME
STATE
POLICY / AUTHORITY CONDITIONS
TEMPORAL ASSUMPTIONS
VALIDATION CONDITIONS
```

The epoch provides a boundary around causal conclusions.

It does **not** make those conclusions universally or permanently true.

Core distinction:

```text
FINALIZED_FOR_EPOCH
!=
ETERNALLY TRUE
```

---

# 1. Core Law

For causal conclusion `C` evaluated within epoch `E`:

```text
VALID(C, E)
```

means only:

```text
C is valid
within the declared
scope,
regime,
dependency state,
provenance state,
and temporal conditions
of E.
```

It does not imply:

```text
∀E' VALID(C, E')
```

Therefore:

```text
EPOCH VALIDITY
!=
UNIVERSAL VALIDITY
```

---

# 2. Why Causal Epochs Exist

AMOS reasoning operates over systems that can change.

Changes may occur in:

```text
EVIDENCE
STATE
DEPENDENCIES
REGIME
POLICY
AUTHORITY
PROVENANCE
MODELS
MEASUREMENTS
ENVIRONMENT
CAUSAL STRUCTURE
```

Without epoch boundaries, a conclusion derived under an earlier state can silently leak into a later incompatible state.

The causal epoch prevents:

```text
OLD VALIDITY
→
UNCONTROLLED REUSE
→
NEW REGIME
```

Instead:

```text
EPOCH E0
↓
VALID CONCLUSIONS
↓
CHANGE EVENT
↓
BOUNDARY
↓
EPOCH E1
↓
REVALIDATE AFFECTED CONCLUSIONS
```

---

# 3. Hard Boundaries

```text
EPOCH
!=
TIMESTAMP

EPOCH
!=
VERSION LABEL

EPOCH
!=
GLOBAL TRUTH

EPOCH FINALITY
!=
IMMUTABILITY

FINALIZED
!=
UNFALSIFIABLE

NEWER
!=
AUTHORITATIVE

DIFFERENT EPOCH
!=
INVALID

SAME EPOCH
!=
AUTOMATICALLY COMPATIBLE

TEMPORAL ORDER
!=
CAUSAL ORDER

STATE CHANGE
!=
CAUSAL CHANGE

DEPENDENCY
!=
CAUSATION

PROPOSAL
!=
COMMIT

CAPABILITY
!=
AUTHORITY

UNKNOWN/GAP
!=
PASS
```

---

# 4. Causal Epoch Primitive

Conceptually:

```text
E_c = (
  id,
  parent,
  causal_state,
  dependency_state,
  provenance_state,
  scope,
  regime,
  temporal_bounds,
  validation_state,
  authority_state
)
```

A minimal representation:

```yaml
causal_epoch:
  epoch_id:
  parent_epoch:

  opened_at:
  finalized_at:

  causal_state:
  dependency_state:
  provenance_state:

  scope:
  regime:

  validation_state:
  authority_state:

  status:
```

---

# 5. Epoch Identity

Epoch identity must be explicit.

```text
EPOCH_ID
!=
FILENAME

EPOCH_ID
!=
CREATION TIME

EPOCH_ID
!=
DOCUMENT VERSION
```

Recommended conceptual identity:

```text
epoch_id =
stable identifier for
a bounded causal state
```

Examples:

```text
CE-000001
CE-000002
CE-000003
```

The exact encoding is an implementation concern.

---

# 6. Epoch Lineage

Epochs form lineage.

```text
E0
↓
E1
↓
E2
↓
E3
```

Each successor should preserve its parent relation.

Conceptually:

```yaml
epoch_lineage:
  epoch_id: CE-000003
  parent_epoch: CE-000002
  supersedes: CE-000002
```

But:

```text
SUPERSEDES
!=
ERASES
```

Previous epochs remain recoverable for provenance, replay, audit, and comparison.

---

# 7. Epoch Opening

An epoch opens when AMOS begins operating under a causally relevant state that is distinguishable from its predecessor.

Conceptually:

```text
OPEN(E_n)
```

requires:

```text
IDENTITY
PARENT
SCOPE
REGIME
BASELINE DEPENDENCIES
PROVENANCE ANCHOR
```

to be known or explicitly marked `UNKNOWN/GAP`.

---

# 8. Epoch Boundary

A causal epoch boundary occurs when a change can materially invalidate the causal assumptions of the active epoch.

Examples include:

```text
REGIME SHIFT
CAUSAL EDGE CHANGE
LOAD-BEARING DEPENDENCY CHANGE
PROVENANCE ROOT INVALIDATION
AUTHORITATIVE STATE CHANGE
MEASUREMENT SEMANTICS CHANGE
POLICY EPOCH CHANGE
EXTERNAL ENVIRONMENT CHANGE
MATERIAL MODEL CHANGE
CONFLICT RESOLUTION
```

Not every event creates a new causal epoch.

---

# 9. Boundary Decision

For event `Δ`:

```text
BOUNDARY_REQUIRED(Δ)
```

when:

```text
Δ can materially change
one or more load-bearing
causal conclusions.
```

Conceptually:

```text
if affects_load_bearing_causal_state(Δ):
    open_new_epoch()
else:
    remain_in_epoch()
```

---

# 10. Non-Boundary Changes

Examples that may not require a new causal epoch:

```text
COSMETIC DOCUMENT EDIT
NON-SEMANTIC RENAME
UNRELATED OBSERVABILITY EVENT
NON-LOAD-BEARING METADATA UPDATE
COMMENT CHANGE
FORMATTING CHANGE
```

provided they do not alter semantic identity, provenance, authority, or causal interpretation.

---

# 11. Causal State Snapshot

Each finalized epoch should conceptually bind a causal state snapshot.

```yaml
causal_state:
  causal_claims: []
  causal_edges: []
  causal_closures: []
  competing_hypotheses: []
  unresolved_gaps: []
```

This need not duplicate every underlying artifact.

References or content-addressed bindings may be sufficient.

---

# 12. Dependency Snapshot

Epoch validity depends on load-bearing dependencies.

```yaml
dependency_state:
  dependencies: []
  dependency_hash_or_revision:
  unresolved_dependencies: []
```

The critical law:

```text
CHANGE IN NON-LOAD-BEARING DEPENDENCY
MAY NOT
INVALIDATE EPOCH
```

while:

```text
CHANGE IN LOAD-BEARING DEPENDENCY
MAY REQUIRE
REVALIDATION OR NEW EPOCH
```

---

# 13. Provenance Snapshot

A causal epoch should preserve provenance topology sufficient to reconstruct why its conclusions were accepted.

```yaml
provenance_state:
  source_roots: []
  ancestry_edges: []
  independence_state:
  source_revisions: []
  source_hashes: []
```

Where available.

---

# 14. Persistent Provenance

Epoch transitions must not destroy historical provenance.

```text
E0 provenance
↓
E1 provenance
↓
E2 provenance
```

must remain traceable.

Therefore:

```text
NEW EPOCH
!=
PROVENANCE RESET
```

---

# 15. Provenance Topology

The epoch should distinguish:

```text
SOURCE_A
├── CLAIM_B
├── CLAIM_C
└── CLAIM_D
```

from:

```text
SOURCE_A → CLAIM_B
SOURCE_X → CLAIM_C
SOURCE_Z → CLAIM_D
```

because evidence independence may affect causal confidence.

---

# 16. Sybil-Hardening Rule

Multiple descendants of one provenance root remain one correlated ancestry family.

```text
N REPORTS
FROM
ONE ROOT
!=
N INDEPENDENT SOURCES
```

This remains true across epoch boundaries unless independent provenance is actually established.

---

# 17. Scope Binding

Every causal epoch has a scope envelope.

Conceptually:

```yaml
scope:
  system:
  population:
  environment:
  scale:
  measurement_method:
  assumptions: []
```

Claims finalized in the epoch inherit compatible scope constraints.

---

# 18. Scope Firewall

If:

```text
C valid in E0
under scope S0
```

then:

```text
C valid in S1
```

does not follow unless:

```text
S1 ⊆ S0
```

or cross-scope transfer is independently validated.

---

# 19. Regime Binding

Each causal epoch should bind its operative regime.

```yaml
regime:
  regime_id:
  defining_conditions: []
  transition_conditions: []
```

The same causal relation may differ across regimes.

```text
R0:
X → Y

R1:
X ↛ Y
```

Therefore regime is potentially load-bearing.

---

# 20. Regime Shift

A detected regime shift is a primary causal-epoch boundary candidate.

```text
E0 / R0
↓
REGIME SHIFT
↓
E1 / R1
```

Conclusions dependent on `R0` must not silently propagate into `R1`.

---

# 21. Temporal Binding

A causal epoch may have:

```yaml
temporal_bounds:
  opened_at:
  effective_from:
  finalized_at:
  superseded_at:
```

But temporal boundaries alone do not define causal epochs.

```text
TIME PASSED
!=
CAUSAL EPOCH CHANGED
```

unless freshness or causal state changes make time material.

---

# 22. Freshness Binding

A causal premise may expire while the epoch otherwise remains stable.

Therefore:

```text
FRESHNESS
```

is evaluated independently.

If a load-bearing premise becomes stale:

```text
EPOCH VALIDITY
```

may require reopening or revalidation.

---

# 23. Causal Closure Integration

`K_CAUSAL_CLOSURE` determines the minimal load-bearing causal graph for a claim.

`K_CAUSAL_EPOCH` binds that graph to a state interval.

```text
CAUSAL CLOSURE
+
EPOCH
=
BOUNDED CAUSAL VALIDITY
```

Thus:

```text
CC(C, E)
```

means causal closure for claim `C` under epoch `E`.

---

# 24. Epoch-Specific Closure

It is possible that:

```text
CC(C, E0)
!=
CC(C, E1)
```

because a new epoch may introduce:

```text
NEW CONFOUNDER
NEW PATH
NEW REGIME
NEW DEPENDENCY
NEW MECHANISM
NEW PROVENANCE
```

Therefore causal closure must not be assumed invariant across epochs.

---

# 25. Causal Epoch Finality

A finalized epoch asserts:

```text
WITHIN DECLARED CONDITIONS,
THE EPOCH STATE IS SUFFICIENTLY CLOSED
FOR ITS AUTHORIZED PURPOSE.
```

It does not assert universal causal completeness.

Recommended state:

```text
FINALIZED_FOR_SCOPE
```

rather than:

```text
ABSOLUTELY_FINAL
```

---

# 26. Finality Preconditions

Conceptually:

```text
FINALIZE(E)
```

requires:

```text
DEPENDENCY CLOSURE SUFFICIENT
CAUSAL CLOSURE SUFFICIENT
PROVENANCE BOUND
SCOPE EXPLICIT
REGIME EXPLICIT
FRESHNESS ACCEPTABLE
CONFLICTS RESOLVED OR PRESERVED
CRITICAL GAPS CLOSED
AUTHORITY VALID
```

where required for the intended action.

---

# 27. Unresolved Competing Hypotheses

An epoch may be finalized while retaining competing hypotheses if convergence is not required.

Example:

```text
EPOCH E4

H1 = ACTIVE
H2 = ACTIVE
STATE = COMPETING
```

This is valid when:

```text
THE DECISION DOES NOT REQUIRE
FALSE CONVERGENCE.
```

---

# 28. Finality Does Not Erase COMPETING

```text
FINALIZED EPOCH
+
COMPETING HYPOTHESES
```

is allowed.

Finality means the state of knowledge is fixed for the epoch, not that every uncertainty disappeared.

---

# 29. Finality Does Not Erase UNKNOWN

Likewise:

```text
UNKNOWN/GAP
```

may remain in a finalized epoch when explicitly bounded and noncritical.

Critical gaps that affect the authorized conclusion block finalization.

---

# 30. Gap Classes

Use:

```text
CRITICAL
DECISION-RELEVANT
EXPLANATORY
COSMETIC
```

Finality rule:

```text
UNRESOLVED CRITICAL GAP
→
NO FINALIZATION
```

unless the final state itself is explicitly:

```text
UNKNOWN/GAP
```

---

# 31. Epoch Commit

A proposed epoch state is not committed merely because computation completed.

```text
COMPUTED
!=
COMMITTED
```

Conceptual sequence:

```text
PROPOSE
↓
VALIDATE
↓
CHECK AUTHORITY
↓
COMMIT
↓
FINALIZE
```

---

# 32. Authority Firewall

The kernel may determine:

```text
EPOCH IS LOGICALLY ELIGIBLE FOR FINALIZATION
```

but:

```text
KERNEL
!=
CONTROL PLANE
```

Actual authority to commit or promote state belongs to the appropriate control-plane contract.

---

# 33. Proposal vs Commit

```text
PROPOSED_EPOCH
```

may contain a candidate successor state.

Only authorized commit converts it to:

```text
COMMITTED_EPOCH
```

Therefore:

```text
PROPOSAL != COMMIT
```

---

# 34. MVCC Analogy

AMOS causal epoch handling may use MVCC-like concepts.

Conceptually:

```text
READER A → EPOCH E4
READER B → EPOCH E4

WRITER → PROPOSE E5

READERS REMAIN CONSISTENT ON E4
UNTIL E5 IS COMMITTED
```

This is an architectural reasoning pattern, not a claim that every AMOS runtime literally implements database MVCC.

---

# 35. Snapshot Isolation Concept

Reasoning started against epoch `E_n` should know whether its load-bearing state changed before commit.

```text
READ E_n
↓
REASON
↓
VALIDATE
↓
COMPARE CURRENT EPOCH
```

If current epoch is now:

```text
E_n+1
```

revalidation may be required.

---

# 36. CAS Concept

Conceptually:

```text
COMMIT
ONLY IF
CURRENT_EPOCH == EXPECTED_EPOCH
```

Equivalent reasoning pattern:

```python
if current_epoch == expected_epoch:
    commit(candidate)
else:
    conflict()
```

This prevents stale reasoning from silently overwriting newer authoritative state.

---

# 37. CAS Failure

A CAS-style failure is not necessarily a logical failure.

It means:

```text
THE BASE STATE CHANGED.
```

Correct response:

```text
REVALIDATE AFFECTED DEPENDENCIES
```

not:

```text
BLINDLY RETRY EVERYTHING
```

---

# 38. Atomic Multi-RSCF Epoch Reasoning

A causal epoch may depend on multiple RSCFs that must be evaluated consistently.

Example:

```text
RSCF_A
RSCF_B
RSCF_C
↓
EPOCH E
```

If their joint consistency is load-bearing:

```text
PARTIAL COMMIT
```

must not create a falsely coherent causal state.

---

# 39. Atomicity Principle

For a logically atomic causal transition:

```text
ALL REQUIRED RSCF UPDATES COMMIT
```

or:

```text
NONE BECOME AUTHORITATIVE
```

when partial state would violate invariants.

---

# 40. Causal Order

Epoch ordering must distinguish:

```text
WALL-CLOCK ORDER
```

from:

```text
CAUSAL ORDER
```

If:

```text
A → B
```

then the system must preserve the dependency relation even when timestamps are close, delayed, or distributed.

---

# 41. Causal Lineage

For state transitions:

```text
S0
→
S1
→
S2
```

epoch lineage should preserve which state transitions depend on which earlier states.

This enables selective invalidation.

---

# 42. Epoch DAG

Not all causal lineage must be a simple chain.

Conceptually:

```text
      E1
     /  \
   E2    E3
     \  /
      E4
```

may occur where branches represent distinct hypotheses, environments, or state paths.

Therefore:

```text
EPOCH LINEAGE
MAY BE
DAG-LIKE
```

when the architecture permits branching.

---

# 43. Branching Epochs

Branching may be appropriate for:

```text
COMPETING HYPOTHESES
SIMULATION BRANCHES
SHADOW STATE
RECOVERY STATE
COUNTERFACTUAL STATE
```

These branches must not automatically become authoritative.

---

# 44. Authoritative Epoch

At any authority scope, the system should be able to identify the currently accepted epoch.

Conceptually:

```yaml
authoritative_epoch:
  scope:
  epoch_id:
  committed_at:
  authority_record:
```

If this cannot be established:

```text
AUTHORITATIVE EPOCH
=
UNKNOWN/GAP
```

---

# 45. Shadow Epoch

A shadow epoch may be used for evaluation without authority.

```text
AUTHORITATIVE E4
↓
SHADOW E5
↓
TEST
↓
PROMOTE OR DISCARD
```

This supports reversible evolution.

---

# 46. Recovery Epoch

A recovery path may establish:

```text
E_RECOVERY
```

derived from the nearest known valid ancestor.

```text
E4
↓
E5 INVALID
↓
ROLL BACK
↓
E4
↓
REPAIR
↓
E6
```

History should preserve the failed `E5` rather than erase it.

---

# 47. Selective Invalidation

If premise `P` fails:

```text
INVALID(P)
```

then invalidate only epoch conclusions transitively dependent on `P`.

```text
P → C1 → C2

P ↛ C3
```

Therefore:

```text
INVALID(P)
→
INVALIDATE C1, C2
PRESERVE C3
```

---

# 48. Epoch-Wide Invalidation

An entire epoch should be invalidated only when failure is sufficiently global.

Examples:

```text
FOUNDATIONAL PROVENANCE FAILURE
GLOBAL REGIME MISIDENTIFICATION
CORRUPTED AUTHORITATIVE SNAPSHOT
INVALID EPOCH ROOT
SYSTEM-WIDE LOAD-BEARING INVARIANT FAILURE
```

Global invalidation is last resort.

---

# 49. Recovery Law

```text
INVALIDATE MINIMALLY
ROLL BACK LOCALLY
REVALIDATE LOCALLY
PRESERVE UNAFFECTED STATE
```

Preferred over:

```text
DELETE EVERYTHING
RECOMPUTE EVERYTHING
```

---

# 50. Nearest Valid State

Recovery should locate:

```text
NEAREST VALID ANCESTOR
```

rather than automatically reverting to genesis.

Conceptually:

```text
E0 → E1 → E2 → E3 → E4
                    ↑
                 FAILURE
```

If `E2` remains valid:

```text
RECOVERY BASE = E2
```

unless evidence requires an earlier boundary.

---

# 51. Causal Epoch Freshness

Each finalized conclusion should retain freshness semantics.

```yaml
freshness:
  evaluated_at:
  valid_until:
  refresh_trigger:
```

where applicable.

A causal epoch can remain historically valid while becoming unsuitable for present reuse.

---

# 52. Historical Validity vs Current Validity

```text
VALID_AT(E0)
```

and:

```text
VALID_NOW
```

are different predicates.

Historical preservation must not imply current applicability.

---

# 53. Epoch Reuse Gate

Reuse conclusion `C` from epoch `E0` only when:

```text
DEPENDENCIES STILL VALID
SCOPE COMPATIBLE
REGIME COMPATIBLE
FRESHNESS VALID
PROVENANCE VALID
NO MATERIAL CONFLICT
```

Otherwise reopen or revalidate.

---

# 54. Fast Path

Epoch-local reasoning is eligible when:

```text
DEPENDENCY CLOSURE IS LOCAL
PROVENANCE INDEPENDENCE IS ESTABLISHED
SCOPE IS COMPATIBLE
REGIME IS STABLE
FRESHNESS IS VALID
NO CONFLICT EXISTS
NO CROSS-EPOCH LOAD-BEARING CHANGE EXISTS
```

Then global coordination may be unnecessary.

---

# 55. Proof-Based Coordination Avoidance

Conceptually:

```text
PROVEN LOCAL CLOSURE
+
PROVEN INDEPENDENCE
+
NO CROSS-BOUNDARY CAUSAL COUPLING
+
VALID EPOCH BASE
→
LOCAL FINALIZATION ELIGIBILITY
```

This is a coordination-avoidance reasoning principle.

It is not a claim that AMOS has universally solved distributed consensus.

---

# 56. Cross-Shard Epoch Coupling

Suppose:

```text
SHARD A / E_A
SHARD B / E_B
```

If a conclusion depends on both:

```text
A → B
```

then independent local finalization may be insufficient.

The cross-shard causal dependency becomes load-bearing.

---

# 57. Shard-Local Finalization

Shard-local finalization is safe only when independence is demonstrated.

Required conceptually:

```text
LOCAL DEPENDENCY CLOSURE
LOCAL CAUSAL CLOSURE
NO UNRESOLVED CROSS-SHARD DEPENDENCY
PROVENANCE SUFFICIENT
REGIME COMPATIBLE
```

Independence must not be assumed from physical separation.

---

# 58. Epoch Conflict

An epoch conflict exists when concurrent candidate transitions cannot both be accepted under the same authority scope.

Example:

```text
E4
├── candidate E5-A
└── candidate E5-B
```

If mutually incompatible:

```text
CONFLICT
```

must remain visible until resolved.

---

# 59. Conflict Firewall

Do not silently select:

```text
LATEST
LONGEST
MOST CONFIDENT
MOST POPULAR
```

as the winner.

Conflict resolution requires an explicit rule, evidence, or authority decision.

---

# 60. Competing Epochs

When two candidate epoch states have incomparable support:

```text
E5-A
vs
E5-B
```

preserve:

```text
COMPETING
```

until discriminating evidence exists.

---

# 61. Discriminating Test

Prefer:

```text
CHEAPEST
HIGH-INFORMATION
TEST
```

that distinguishes competing epoch states.

Do not accumulate redundant evidence if it cannot change the decision.

---

# 62. Epoch Sensitivity

Identify the smallest condition capable of forcing a new epoch.

Examples:

```text
ONE LOAD-BEARING SOURCE INVALIDATED
ONE REGIME THRESHOLD CROSSED
ONE AUTHORITY POLICY CHANGED
ONE CAUSAL EDGE REVERSED
ONE DEPENDENCY BECAME CROSS-SHARD
```

These are high-sensitivity epoch conditions.

---

# 63. Epoch Stability

An epoch is comparatively stable when plausible perturbations of noncritical assumptions do not require:

```text
NEW EPOCH
REOPENING
DOWNGRADE
```

Stability does not imply truth.

---

# 64. Epoch State Machine

Recommended conceptual states:

```text
PROPOSED
OPEN
VALIDATING
COMPETING
ELIGIBLE
COMMITTED
FINALIZED_FOR_SCOPE
STALE
SUPERSEDED
INVALIDATED
RECOVERY
UNKNOWN/GAP
```

---

# 65. PROPOSED

```text
PROPOSED
```

means a candidate epoch exists but carries no authoritative status.

---

# 66. OPEN

```text
OPEN
```

means the epoch is active but causal closure or validation remains incomplete.

---

# 67. VALIDATING

```text
VALIDATING
```

means required causal, provenance, dependency, scope, and regime checks are underway.

---

# 68. ELIGIBLE

```text
ELIGIBLE
```

means kernel-level conditions for commit appear satisfied.

It does not itself grant commit authority.

---

# 69. COMMITTED

```text
COMMITTED
```

means the authorized control path accepted the epoch state.

---

# 70. FINALIZED_FOR_SCOPE

```text
FINALIZED_FOR_SCOPE
```

means the committed epoch is closed for its declared applicability envelope.

It does not imply universal finality.

---

# 71. STALE

```text
STALE
```

means historical integrity remains, but present reuse requires revalidation.

---

# 72. SUPERSEDED

```text
SUPERSEDED
```

means a later governed epoch replaced the epoch for current authoritative use.

Superseded does not mean erroneous.

---

# 73. INVALIDATED

```text
INVALIDATED
```

means a load-bearing failure undermined the epoch or relevant portion of its state.

---

# 74. RECOVERY

```text
RECOVERY
```

means the system is rebuilding from a valid causal ancestor or unaffected state.

---

# 75. UNKNOWN/GAP

```text
UNKNOWN/GAP
```

means sufficient information to determine epoch state is absent.

Never convert this to `PASS`.

---

# 76. Epoch Record

Recommended conceptual schema:

```yaml
causal_epoch_record:
  epoch_id:
  parent_epoch:
  lineage_branch:

  status:
  conclusion_class:

  opened_at:
  committed_at:
  finalized_at:
  superseded_at:

  scope:
  regime:

  causal_closures: []
  causal_claims: []
  competing_hypotheses: []

  dependency_roots: []
  provenance_roots: []

  source_revisions: []
  hashes: []

  policy_epoch:
  authority_record:

  freshness:
  unresolved_gaps: []
  conflicts: []

  invalidation_conditions: []
  recovery_parent:
```

---

# 77. Epoch Proof Capsule

Important finalized epoch conclusions should conceptually preserve:

```yaml
epoch_proof_capsule:
  claim:
  claim_class:

  epoch_id:

  load_bearing_premises: []
  evidence: []
  provenance: []

  scope:
  regime:
  temporal_validity:

  causal_dependencies: []
  competing_explanations: []

  falsifiers: []
  invalidation_conditions: []

  confidence_ceiling:
```

---

# 78. Proof Capsule Reuse

Reuse only while:

```text
DEPENDENCIES VALID
SCOPE VALID
REGIME VALID
FRESHNESS VALID
PROVENANCE VALID
EPOCH COMPATIBLE
```

If not:

```text
REVALIDATE
```

or:

```text
REOPEN
```

---

# 79. Epoch Invariants

```text
CE-01
EVERY CAUSAL EPOCH MUST HAVE STABLE IDENTITY

CE-02
EPOCH IDENTITY MUST BE DISTINCT FROM FILENAME AND VERSION LABEL

CE-03
EPOCH LINEAGE MUST REMAIN RECOVERABLE

CE-04
NEW EPOCH MUST NOT ERASE OLD PROVENANCE

CE-05
FINALIZED_FOR_EPOCH MUST NOT BECOME ETERNAL TRUTH

CE-06
SCOPE MUST REMAIN EXPLICIT

CE-07
REGIME MUST REMAIN EXPLICIT WHEN LOAD-BEARING

CE-08
FRESHNESS MUST BE CHECKED BEFORE REUSE

CE-09
CAUSAL CLOSURE MAY CHANGE ACROSS EPOCHS

CE-10
LOAD-BEARING DEPENDENCY CHANGE MUST TRIGGER REVALIDATION

CE-11
NON-LOAD-BEARING CHANGE MUST NOT FORCE GLOBAL INVALIDATION

CE-12
PROPOSAL MUST NOT BECOME COMMIT WITHOUT AUTHORITY

CE-13
KERNEL ELIGIBILITY MUST NOT BE EQUATED WITH CONTROL-PLANE AUTHORITY

CE-14
STALE REASONING MUST NOT SILENTLY OVERWRITE NEWER AUTHORITATIVE STATE

CE-15
MULTI-RSCF ATOMICITY MUST BE PRESERVED WHERE PARTIAL COMMIT BREAKS INVARIANTS

CE-16
PROVENANCE INDEPENDENCE MUST BE DEMONSTRATED, NOT ASSUMED

CE-17
SHARD SEPARATION MUST NOT BE EQUATED WITH CAUSAL INDEPENDENCE

CE-18
COMPETING EPOCHS MUST REMAIN COMPETING UNTIL RESOLVED

CE-19
SELECTIVE INVALIDATION MUST BE PREFERRED OVER GLOBAL INVALIDATION

CE-20
RECOVERY MUST BEGIN FROM THE NEAREST VALID STATE WHEN POSSIBLE

CE-21
SUPERSESSION MUST PRESERVE HISTORY

CE-22
HISTORICAL VALIDITY MUST NOT BE EQUATED WITH CURRENT VALIDITY

CE-23
TIME ORDER MUST NOT BE EQUATED WITH CAUSAL ORDER

CE-24
UNKNOWN/GAP MUST NOT BECOME PASS
```

---

# 80. Failure Modes

```text
EPOCH_ID_COLLISION
EPOCH_ALIAS_CONFUSION
SILENT_EPOCH_TRANSITION
FALSE_FINALITY
GLOBAL_FINALITY_OVERREACH
REGIME_LEAKAGE
SCOPE_LEAKAGE
STALE_EPOCH_REUSE
PROVENANCE_RESET
PROVENANCE_COLLAPSE
FALSE_SOURCE_INDEPENDENCE
STALE_WRITE
PARTIAL_ATOMIC_COMMIT
UNAUTHORIZED_COMMIT
LATEST_WINS_WITHOUT_RULE
SILENT_CONFLICT_RESOLUTION
CROSS_SHARD_CAUSAL_LEAK
FALSE_SHARD_INDEPENDENCE
BLIND_RETRY
GLOBAL_INVALIDATION
HISTORY_ERASURE
SUPERSESSION_WITHOUT_LINEAGE
RECOVERY_FROM_INVALID_BASE
UNKNOWN_AS_PASS
```

---

# 81. Conceptual Epoch Boundary Algorithm

```python
def requires_new_causal_epoch(event, active_epoch):
    affected = trace_load_bearing_dependencies(event, active_epoch)

    if not affected:
        return False

    if changes_regime(event):
        return True

    if changes_load_bearing_causal_structure(event):
        return True

    if invalidates_provenance_root(event):
        return True

    if changes_authoritative_state(event):
        return True

    if changes_load_bearing_scope(event):
        return True

    return requires_revalidation(affected)
```

This is architectural pseudocode, not evidence of deployed implementation.

---

# 82. Conceptual Finalization Algorithm

```python
def finalize_epoch(epoch, authority):
    require_dependency_closure(epoch)
    require_causal_closure(epoch)

    validate_scope(epoch)
    validate_regime(epoch)
    validate_freshness(epoch)
    validate_provenance(epoch)

    preserve_competing_hypotheses(epoch)
    reject_unresolved_critical_gaps(epoch)

    if not authority.can_commit(epoch):
        return "NOT_AUTHORIZED"

    epoch.status = "FINALIZED_FOR_SCOPE"
    return epoch
```

---

# 83. Conceptual CAS Commit

```python
def commit_epoch(expected_epoch, candidate_epoch):
    current = authoritative_epoch()

    if current.id != expected_epoch.id:
        return "EPOCH_CONFLICT"

    validate(candidate_epoch)
    commit(candidate_epoch)

    return "COMMITTED"
```

Again, this expresses the v4.4 reasoning pattern rather than asserting a particular deployed storage mechanism.

---

# 84. Conceptual Selective Recovery

```python
def recover_from_failure(failed_premise, epoch):
    affected = descendants_of(failed_premise)

    invalidate(affected)
    preserve(epoch.state - affected)

    base = nearest_valid_state(epoch, failed_premise)

    return rebuild_only_affected_closure(base)
```

---

# 85. Relationship to K_CAUSAL_CLOSURE

```text
K_CAUSAL_CLOSURE
=
WHAT CAUSAL STRUCTURE
IS LOAD-BEARING?

K_CAUSAL_EPOCH
=
UNDER WHICH BOUNDED STATE
IS THAT STRUCTURE VALID?
```

Together:

```text
CAUSAL STRUCTURE
+
CAUSAL VALIDITY INTERVAL
=
EPOCH-BOUNDED CAUSAL CLAIM
```

---

# 86. Relationship to K_COUNTERFACTUAL

Counterfactual branches should normally preserve their source epoch.

```text
AUTHORITATIVE E4
↓
COUNTERFACTUAL BRANCH CF-E4-A
```

The counterfactual branch must not silently replace authoritative epoch state.

---

# 87. Relationship to K_MULTI_HYPOTHESIS

Competing hypotheses may produce competing causal epoch candidates.

```text
H1 → E5-A
H2 → E5-B
```

Preserve both until discriminating evidence or governed authority resolves the conflict.

---

# 88. Relationship to K_METACOGNITION

`K_METACOGNITION` should challenge epoch validity for:

```text
STALE PREMISES
REGIME DRIFT
SCOPE DRIFT
HIDDEN DEPENDENCY
PROVENANCE CORRELATION
FALSE FINALITY
STALE WRITE
UNAUTHORIZED COMMIT
```

---

# 89. Relationship to K_STRUCTURAL_REASONING

`K_STRUCTURAL_REASONING` identifies system structure.

`K_CAUSAL_CLOSURE` identifies the causally load-bearing subset.

`K_CAUSAL_EPOCH` binds that subset to a governed validity interval.

```text
STRUCTURE
↓
CAUSAL CLOSURE
↓
CAUSAL EPOCH
```

---

# 90. Relationship to State

The state plane stores:

```text
AUTHORITATIVE
WORKING
SHADOW
RECOVERY
```

state.

The causal epoch kernel supplies semantics for when causal conclusions attached to those states remain valid.

```text
STATE STORAGE
!=
CAUSAL VALIDITY
```

---

# 91. Relationship to Control Plane

The control plane governs:

```text
AUTHORITY
POLICY
COMMIT
PROMOTION
PROVENANCE CONTROL
```

The kernel evaluates logical eligibility.

Therefore:

```text
K_CAUSAL_EPOCH
→
ELIGIBILITY

CONTROL_PLANE
→
AUTHORIZATION / COMMIT
```

---

# 92. Relationship to Runtime

The runtime may operationalize:

```text
EPOCH READ
EPOCH SNAPSHOT
CANDIDATE TRANSITION
CONFLICT DETECTION
RETRY / REVALIDATION
```

but runtime mechanics must not redefine kernel semantics.

```text
RUNTIME
IMPLEMENTS

KERNEL
DEFINES
```

---

# 93. Required Tests

Future implementation verification should include:

```text
EPOCH-IDENTITY TEST
PARENT-LINEAGE TEST
BOUNDARY-DETECTION TEST
NON-BOUNDARY CHANGE TEST
REGIME-SHIFT TEST
SCOPE-CHANGE TEST
FRESHNESS-EXPIRY TEST
PROVENANCE-INVALIDATION TEST
CAUSAL-CLOSURE-CHANGE TEST
FINALITY-BOUNDARY TEST
COMPETING-EPOCH TEST
UNKNOWN-PRESERVATION TEST
CAS-CONFLICT TEST
STALE-WRITE TEST
ATOMIC-MULTI-RSCF TEST
SELECTIVE-INVALIDATION TEST
NEAREST-VALID-RECOVERY TEST
SHARD-LOCAL-FINALIZATION TEST
CROSS-SHARD-COUPLING TEST
SUPERSESSION-LINEAGE TEST
HISTORICAL-REPLAY TEST
```

---

# 94. Negative Tests

```text
NEWER FILE
→
NEW AUTHORITATIVE EPOCH
MUST FAIL

TIMESTAMP CHANGE
→
CAUSAL EPOCH CHANGE
MUST FAIL

FINALIZED_FOR_SCOPE
→
UNIVERSAL TRUTH
MUST FAIL

SUPERSEDED
→
DELETE HISTORY
MUST FAIL

SHARD SEPARATION
→
CAUSAL INDEPENDENCE
MUST FAIL

MULTIPLE DESCENDANT SOURCES
→
INDEPENDENT CONFIRMATION
MUST FAIL

KERNEL ELIGIBILITY
→
COMMIT AUTHORITY
MUST FAIL

PROPOSAL
→
COMMIT
MUST FAIL

STALE BASE
→
SILENT WRITE
MUST FAIL

ONE FAILED PREMISE
→
GLOBAL INVALIDATION
MUST FAIL

COUNTERFACTUAL BRANCH
→
AUTHORITATIVE EPOCH
MUST FAIL

HISTORICALLY VALID
→
CURRENTLY VALID
MUST FAIL

UNKNOWN/GAP
→
PASS
MUST FAIL
```

---

# 95. Lifecycle

```text
PLACEHOLDER
↓
AMOS_MODEL
↓
SOURCE_BOUND
↓
IMPLEMENTED
↓
TESTED
↓
VALIDATED
↓
AUTHORIZED
```

These states remain distinct.

```text
MODEL != IMPLEMENTATION
IMPLEMENTATION != VALIDATION
VALIDATION != AUTHORITY
```

---

# 96. Promotion Gate

Before promotion beyond `AMOS_MODEL`:

```text
[ ] canonical causal-epoch lineage bound
[ ] epoch identity semantics confirmed
[ ] epoch boundary semantics confirmed
[ ] causal closure integration confirmed
[ ] regime transition semantics confirmed
[ ] scope transition semantics confirmed
[ ] freshness semantics confirmed
[ ] provenance persistence confirmed
[ ] provenance topology behavior confirmed
[ ] authoritative-state integration confirmed
[ ] MVCC-like semantics specified
[ ] CAS-like conflict semantics specified
[ ] multi-RSCF atomicity specified
[ ] commit authority boundary confirmed
[ ] competing epoch behavior confirmed
[ ] selective invalidation tested
[ ] nearest-valid recovery tested
[ ] shard-local finalization conditions tested
[ ] cross-shard coupling tested
[ ] supersession lineage tested
[ ] historical replay tested
[ ] negative tests implemented
[ ] unresolved conflicts registered
```

Until evidenced:

```text
IMPLEMENTATION_STATUS = UNKNOWN/GAP
```

---

# 97. Integrity Note

This artifact replaces a repository placeholder with a structured AMOS v4.4-aligned causal-epoch model.

It reflects the AMOS lineage concepts of:

```text
CAUSAL LINEAGE
CAUSAL EPOCH FINALITY
PERSISTENT PROVENANCE
PROVENANCE TOPOLOGY
MVCC / CAS CONCEPTS
ATOMIC MULTI-RSCF REASONING
SELECTIVE INVALIDATION
HARDENED SHARD-LOCAL FINALIZATION
PROOF-BASED COORDINATION AVOIDANCE
```

These are architectural reasoning patterns.

This document does **not** establish that the corresponding distributed mechanisms are implemented, deployed, formally verified, or empirically validated.

Therefore:

```text
DOCUMENT_CLASS = AMOS_MODEL
IMPLEMENTATION = UNKNOWN/GAP
EMPIRICAL_VALIDATION = UNKNOWN/GAP
FORMAL_VERIFICATION = UNKNOWN/GAP
RUNTIME_AUTHORITY = NONE
```

---

# 98. RSCF Node

```RSCF-NODE
node_id: AMOS-OS-K-CAUSAL-EPOCH
node_type: kernel_causal_epoch_contract
domain: AMOS_OS_KERNEL
functional_type: CausalEpochKernel
lifecycle_stage: Architecture
claim_class: AMOS_MODEL

RSCF-RELATIONS:
  - ROOTED_IN: README
  - DEPENDENCY_BOUND_TO: DEPENDENCY_MAP
  - STATE_BOUND_TO: AUTHORITATIVE_STATE

  - GOVERNED_BY: AMOS_CORE_LAWS
  - CONSTRAINED_BY: INVARIANT_REGISTRY
  - PRECEDENCE_GOVERNED_BY: LAW_HIERARCHY
  - PERSISTENCE_GOVERNED_BY: PERSISTENCE_CANON
  - AUTHORITY_GOVERNED_BY: AUTHORITY_CANON

  - PROVENANCE_GOVERNED_BY: CANON_PROVENANCE
  - LINEAGE_TRACKED_BY: SOURCE_LINEAGE
  - CONFLICTS_TRACKED_BY: CONFLICT_REGISTRY
  - SUPERSESSION_TRACKED_BY: SUPERSESSION_LOG

  - INDEXED_BY: KERNEL_MAP

  - LOGIC_DEPENDS_ON: K_CORE19_LOGIC
  - META_LOGIC_DEPENDS_ON: K_META_LOGIC
  - STRUCTURE_DEPENDS_ON: K_STRUCTURAL_REASONING
  - CAUSAL_CLOSURE_DEPENDS_ON: K_CAUSAL_CLOSURE

  - COUNTERFACTUAL_INTERACTS_WITH: K_COUNTERFACTUAL
  - METACOGNITION_INTERACTS_WITH: K_METACOGNITION
  - HYPOTHESIS_INTERACTS_WITH: K_MULTI_HYPOTHESIS

  - PROVENANCE_DEPENDS_ON: README
  - CAUSAL_DEPENDS_ON: README
  - DEPENDENCY_DEPENDS_ON: README
  - VALIDATED_BY: README
  - RECOVERY_INTERACTS_WITH: README

  - AUTHORIZED_THROUGH: CONTROL_PLANE_MAP
  - EXECUTED_THROUGH: RUNTIME_MAP

  - STATE_RECORDED_IN: AUTHORITATIVE_STATE
  - OBSERVED_BY: README
  - VERIFIED_BY: README
```

---

# 99. Canonical Summary

```text
ACTIVE CAUSAL EPOCH
↓
REASON AGAINST BOUNDED STATE
↓
TRACK LOAD-BEARING CAUSAL CLOSURE
↓
TRACK DEPENDENCIES
↓
TRACK PROVENANCE
↓
TRACK SCOPE
↓
TRACK REGIME
↓
TRACK FRESHNESS
↓
DETECT MATERIAL CHANGE
↓
NO MATERIAL CHANGE
    → REMAIN IN EPOCH

MATERIAL CHANGE
    → OPEN CANDIDATE SUCCESSOR
↓
VALIDATE AFFECTED CLOSURE
↓
PRESERVE COMPETING STATES
↓
CHECK AUTHORITY
↓
COMMIT
↓
FINALIZE FOR SCOPE
↓
PRESERVE PRIOR EPOCH + LINEAGE
```

Core laws:

```text
EPOCH != TIMESTAMP

EPOCH != VERSION LABEL

NEWER != AUTHORITATIVE

PROPOSAL != COMMIT

KERNEL ELIGIBILITY != CONTROL-PLANE AUTHORITY

FINALIZED_FOR_EPOCH != ETERNALLY TRUE

HISTORICAL VALIDITY != CURRENT VALIDITY

SHARD SEPARATION != CAUSAL INDEPENDENCE

MULTIPLE DESCENDANTS != INDEPENDENT PROVENANCE

SUPERSESSION != ERASURE

INVALIDATION SHOULD FOLLOW DEPENDENCY

UNKNOWN/GAP != PASS
```

The decisive invariant is:

```text
A CAUSAL CONCLUSION
MAY BE FINALIZED

ONLY WITHIN
AN EXPLICITLY BOUNDED EPOCH

WHOSE LOAD-BEARING
CAUSAL DEPENDENCIES,
PROVENANCE,
SCOPE,
REGIME,
FRESHNESS,
AND AUTHORITY CONDITIONS

ARE SUFFICIENTLY VALID
FOR THE DECLARED PURPOSE.

WHEN THOSE CONDITIONS CHANGE,

REVALIDATE ONLY
THE AFFECTED CLOSURE,

PRESERVE
UNAFFECTED STATE,

AND CREATE
GOVERNED LINEAGE

RATHER THAN
SILENTLY MUTATING HISTORY.
```

## Related

[[README]] ·
00_ROOT_MOC|AMOS MOC ·
[[ARCHITECTURE]] ·
[[AUTHORITATIVE_STATE]] ·
[[DEPENDENCY_MAP]] ·
[[CANON_MAP]] ·
[[AMOS_CORE_LAWS]] ·
[[INVARIANT_REGISTRY]] ·
[[LAW_HIERARCHY]] ·
[[PERSISTENCE_CANON]] ·
[[AUTHORITY_CANON]] ·
[[CANON_PROVENANCE]] ·
[[SOURCE_LINEAGE]] ·
[[CONFLICT_REGISTRY]] ·
[[SUPERSESSION_LOG]] ·
[[KERNEL_MAP]] ·
[[K_CORE19_LOGIC]] ·
[[K_META_LOGIC]] ·
[[K_STRUCTURAL_REASONING]] ·
[[K_CAUSAL_CLOSURE]] ·
[[K_COUNTERFACTUAL]] ·
[[K_METACOGNITION]] ·
[[K_MULTI_HYPOTHESIS]] ·
README ·
README ·
README ·
README ·
README ·
[[CONTROL_PLANE_MAP]] ·
[[RUNTIME_MAP]] ·
[[AUTHORITATIVE_STATE]] ·
[[README]] ·
[[README]]

```text
```

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
**MOC:** [[03_CAUSAL_MOC]]
