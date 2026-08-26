---
artifact_id: AMOS-OS-K-REPAIR-PRIORITY
canonical_name: K_REPAIR_PRIORITY
artifact_type: kernel_repair_priority_contract
status: AMOS_MODEL
conclusion_class: AMOS_MODEL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
plane: KERNEL
kernel_family: RECOVERY
scope: AMOS_OS
updated: 2026-08-26

tags:
  - amos-os
  - kernel
  - kernel/repair
  - kernel/priority
  - kernel/recovery
  - kernel/invariants
  - kernel/causal
  - kernel/provenance
  - kernel/homeostasis
  - kernel/repair-harm
  - rscf
  - topic/triage
  - topic/repair-order
  - topic/failure-containment
  - topic/reversibility
---

# K REPAIR PRIORITY

> **AMOS Core target:** `v4.4`  
> **Origin architect / steward:** Trang Phan  
> **Plane:** `02_KERNEL`  
> **Status:** `AMOS_MODEL`  
> **Conclusion class:** `AMOS_MODEL`

## Purpose

`K_REPAIR_PRIORITY` defines the kernel contract for deciding **what should be repaired first** when AMOS contains multiple faults, invalid premises, damaged dependencies, degraded subsystems, unresolved contradictions, or competing recovery actions.

The governing principle is:

```text
REPAIR ORDER
MUST FOLLOW
VALIDITY + DEPENDENCY + HARM,
NOT
VISIBILITY + CONVENIENCE.
```

Canonical flow:

```text
FAULT SET
→ CONTAINMENT
→ DEPENDENCY / CAUSAL ANALYSIS
→ PRIORITY CLASSIFICATION
→ REPAIR-HARM CHECK
→ MINIMUM SUFFICIENT REPAIR
→ REVALIDATION
→ NEXT PRIORITY
```

---

## 1. Hard Boundaries

```text
PRIORITY != SEVERITY
SEVERITY != URGENCY
URGENCY != IMPORTANCE
VISIBILITY != PRIORITY
RECENCY != PRIORITY
EASE != PRIORITY
COST != PRIORITY
ROOT CAUSE != ALWAYS FIRST ACTION
SYMPTOM != ROOT CAUSE
REPAIRABILITY != AUTHORITY
CAPABILITY != AUTHORITY
PROPOSAL != COMMIT
LOCAL FAILURE != LOCAL IMPACT
HIGH CONFIDENCE != HIGH PRIORITY
UNKNOWN/GAP != LOW PRIORITY
```

A highly visible fault may be downstream of a less visible load-bearing failure.

A severe fault may require containment before repair.

A root cause may be known while an immediately dangerous downstream effect must be contained first.

---

## 2. Core Priority Law

For fault set:

```text
F = {F1, F2, ... Fn}
```

AMOS should not simply select:

```text
argmax Severity(Fi)
```

or:

```text
argmax Visibility(Fi)
```

Instead, repair priority is a typed decision over materially relevant properties.

Conceptually:

```text
PRIORITY(Fi)
=
f(
  INTEGRITY_RISK,
  ACTIVE_HARM,
  DEPENDENCY_CRITICALITY,
  CAUSAL_POSITION,
  PROPAGATION_RISK,
  IRREVERSIBILITY,
  AUTHORITY,
  REPAIR_HARM,
  RECOVERABILITY,
  INFORMATION_VALUE,
  UNCERTAINTY
)
```

This is a decision model.

It does **not** assert that these dimensions can always be reduced to a universal scalar score.

---

## 3. Integrity-First Ordering

Default repair precedence:

```text
1. STOP ACTIVE IRREVERSIBLE HARM
2. PRESERVE SYSTEM / EVIDENCE / RECOVERY VIABILITY
3. RESTORE LOAD-BEARING INTEGRITY
4. REPAIR CAUSAL / DEPENDENCY ROOTS
5. RESTORE AUTHORITATIVE STATE
6. RESTORE REQUIRED FUNCTION
7. RESTORE PERFORMANCE / OPTIMIZATION
8. COSMETIC REPAIR
```

This ordering is conditional on scope, regime, authority, and repair-harm constraints.

No lower-order optimization may silently weaken higher-order integrity.

---

## 4. Gap Priority Integration

AMOS gap classes:

```text
CRITICAL
DECISION-RELEVANT
EXPLANATORY
COSMETIC
```

Default resolution order:

```text
CRITICAL
→ DECISION-RELEVANT
→ EXPLANATORY
→ COSMETIC
```

But classification must be based on decision effect, not file location or naming.

A missing cosmetic description does not outrank an uncertain rollback path.

---

## 5. Fault Object

Each repair candidate should conceptually reference a typed fault object:

```yaml
fault:
  fault_id:
  fault_type:
  observed_at:
  affected_scope:
  source:
  evidence:
  provenance:
  causal_epoch:
  regime:
  active_harm:
  severity:
  propagation_risk:
  dependency_position:
  authority_impact:
  recoverability_impact:
  reversibility:
  uncertainty:
  freshness:
```

Missing load-bearing fields remain:

```text
UNKNOWN/GAP
```

---

## 6. Repair Candidate Object

```yaml
repair_candidate:
  repair_id:
  fault_id:
  proposed_action:
  target_scope:
  expected_effect:
  dependencies: []
  prerequisites: []
  competing_repairs: []
  repair_harm:
  reversibility:
  rollback_path:
  authority_required:
  evidence:
  provenance:
  confidence_ceiling:
```

Priority belongs to the fault/action relationship, not merely to the fault in isolation.

---

## 7. Priority Classes

Canonical qualitative classes:

```text
RP0 — EMERGENCY CONTAINMENT
RP1 — CRITICAL INTEGRITY REPAIR
RP2 — LOAD-BEARING REPAIR
RP3 — DECISION-RELEVANT REPAIR
RP4 — FUNCTIONAL RECOVERY
RP5 — DEGRADATION / PERFORMANCE REPAIR
RP6 — EXPLANATORY / MAINTENANCE
RP7 — COSMETIC
RPX — UNKNOWN/GAP
```

These classes describe priority semantics.

They do not independently grant execution authority.

---

## 8. RP0 — Emergency Containment

Use when harm is actively expanding or irreversible loss is imminent.

Examples:

```text
ACTIVE CORRUPTION
SECURITY BREACH PROPAGATION
DESTRUCTIVE EXTERNAL EFFECT
LOSS OF LAST RECOVERY STATE
UNBOUNDED CASCADE
ONGOING PROVENANCE DESTRUCTION
```

Preferred action:

```text
CONTAIN
→ PRESERVE EVIDENCE
→ STABILIZE
→ DIAGNOSE
```

Containment may precede root-cause repair.

---

## 9. RP1 — Critical Integrity Repair

Use when a load-bearing invariant is violated and continued operation cannot be trusted.

Examples:

```text
AUTHORITY INTEGRITY FAILURE
IDENTITY CORRUPTION
CANON / KERNEL CONTRADICTION
INVALID AUTHORITATIVE STATE
PROVENANCE INTEGRITY FAILURE
SECURITY TRUST-BOUNDARY FAILURE
```

Default behavior:

```text
FAIL CLOSED
OR
ENTER GOVERNED DEGRADED MODE
```

until integrity is restored.

---

## 10. RP2 — Load-Bearing Repair

A fault is load-bearing when dependent conclusions or operations rely upon it.

For:

```text
P
├── D1
├── D2
└── D3
```

if:

```text
Invalid(P)
```

then repairing downstream descendants individually may be wasteful or incorrect.

Prefer:

```text
REPAIR / REVALIDATE P
→ REVALIDATE DEPENDENTS
```

when `P` is genuinely causal or dependency-load-bearing.

---

## 11. RP3 — Decision-Relevant Repair

A repair is decision-relevant when its unresolved state can flip a consequential decision.

Conceptually:

```text
IF VALID(P)
→ DECISION A

IF INVALID(P)
→ DECISION B
```

Then `P` has high repair priority even if it is not globally severe.

This is the repair analogue of sensitivity-first reasoning.

---

## 12. RP4 — Functional Recovery

Functional failures are prioritized after higher-order integrity requirements unless the function itself is safety-critical.

Examples:

```text
ROUTER UNAVAILABLE
AGENT EXECUTION FAILURE
MEMORY RETRIEVAL DEGRADED
TOOL ADAPTER FAILURE
INTERFACE FAILURE
```

A function must not be restored by violating kernel, security, authority, or provenance invariants.

---

## 13. RP5 — Degradation Repair

Examples:

```text
LATENCY
THROUGHPUT
CACHE MISS RATE
REDUNDANT COMPUTATION
NONCRITICAL RESOURCE PRESSURE
```

Performance degradation does not outrank correctness or integrity.

```text
FAST + INVALID
<
SLOW + VALID
```

---

## 14. RP6 — Explanatory / Maintenance

Includes:

```text
DOCUMENTATION GAP
NONCRITICAL INDEX DRIFT
STALE NON-LOAD-BEARING DESCRIPTION
MAINTENANCE DEBT
NONCRITICAL REFACTORING
```

These should not displace unresolved decision-critical faults.

---

## 15. RP7 — Cosmetic

Examples:

```text
FORMATTING
NONSEMANTIC NAMING CLEANUP
PRESENTATION POLISH
GRAPH AESTHETICS
```

Cosmetic repair is last unless cosmetic structure itself carries semantic or operational meaning.

---

## 16. RPX — Unknown Priority

If priority cannot be safely determined because required evidence is missing:

```text
RPX = UNKNOWN/GAP
```

Do not silently map:

```text
UNKNOWN
→ LOW PRIORITY
```

Unknown blast radius can itself justify escalation.

---

## 17. Containment vs Repair

Critical distinction:

```text
CONTAINMENT
!=
REPAIR
```

Example:

```text
FAULT F
→ ACTIVE HARM H
```

The correct order may be:

```text
CONTAIN H
→ PRESERVE EVIDENCE
→ REPAIR F
```

rather than:

```text
REPAIR F
→ HOPE H STOPS
```

---

## 18. Root Cause vs First Action

Root cause has structural importance, but:

```text
ROOT CAUSE
!=
ALWAYS FIRST ACTION
```

If:

```text
ROOT CAUSE REPAIR = SLOW

AND

DOWNSTREAM HARM = ACTIVE + IRREVERSIBLE
```

then:

```text
CONTAIN DOWNSTREAM HARM FIRST
→ REPAIR ROOT CAUSE SECOND
```

The causal model and action order must remain distinct.

---

## 19. Ancestor-First Rule

For dependency chain:

```text
A
↓
B
↓
C
↓
D
```

where failure of `A` invalidates all descendants:

```text
Invalid(A)
→ Invalid(B,C,D)
```

default repair order is:

```text
A
→ B
→ C
→ D
```

provided no downstream containment requirement overrides this order.

---

## 20. Selective Invalidation Rule

If:

```text
P2 INVALID
```

in:

```text
P1 + P2 + P3 → C
```

repair should target:

```text
P2
+
DEPENDENTS(P2)
```

not automatically:

```text
P1 + P2 + P3 + ALL SYSTEM STATE
```

Priority should minimize unnecessary invalidation.

---

## 21. Shared-Dependency Priority

Suppose:

```text
      P
    / | \
   A  B  C
```

and all three descendants fail.

Repairing:

```text
A
B
C
```

independently is lower priority than checking `P` when `P` plausibly explains all failures.

However:

```text
SHARED STRUCTURE
!=
SHARED CAUSE
```

The parent hypothesis must be validated.

---

## 22. Causal Priority

A causal ancestor may deserve priority when evidence supports:

```text
CAUSE C
→ FAILURES F1,F2,F3
```

But:

```text
CORRELATED FAILURES
```

do not prove:

```text
COMMON CAUSE
```

Causal repair priority requires causally appropriate evidence.

---

## 23. Causal Epoch Priority

When a fault changes causal structure:

```text
CE17
→ FAULT
→ CE18
```

repair priority must account for conclusions derived under the obsolete epoch.

Affected conclusions may require:

```text
INVALIDATE
→ REPAIR
→ REVALIDATE
```

A stale causal conclusion can become more important than a visible runtime symptom.

---

## 24. Propagation Priority

Faults with high propagation potential receive elevated priority.

Conceptually:

```text
PROPAGATION_RISK(F)
=
POTENTIAL_TO_INVALIDATE
OR DAMAGE
ADDITIONAL VALID STATE
```

Examples:

```text
CORRUPT MEMORY ADMISSION
BAD AUTHORITY PROPAGATION
INVALID PROVENANCE MERGE
RECURSIVE FALSE PREMISE
UNBOUNDED RETRY CASCADE
```

---

## 25. Irreversibility Priority

When two faults have comparable impact:

```text
F1 → REVERSIBLE DAMAGE
F2 → IRREVERSIBLE DAMAGE
```

prefer containment/repair of:

```text
F2
```

when evidence supports the classification.

Irreversible loss reduces future option space.

---

## 26. Recovery-Option Priority

Protecting recovery capability is load-bearing.

High-priority risks include:

```text
LOSS OF LAST KNOWN-GOOD STATE
ROLLBACK CORRUPTION
PROVENANCE DESTRUCTION
BACKUP INVALIDATION
RECOVERY KEY LOSS
```

A repair that preserves current functionality while destroying all recovery paths may be unacceptable.

---

## 27. Authority Priority

Authority failures receive elevated priority because downstream valid execution may become untrustworthy.

Examples:

```text
UNAUTHORIZED COMMIT
POLICY BYPASS
AUTHORITY EPOCH MISMATCH
CAPABILITY / PERMISSION CONFUSION
```

Do not repair downstream effects while leaving an active authority violation capable of reproducing them.

---

## 28. Provenance Priority

If provenance loss would make future diagnosis impossible:

```text
PRESERVE PROVENANCE
```

may outrank immediate cleanup.

Canonical order where feasible:

```text
SNAPSHOT
→ HASH / IDENTIFY
→ PRESERVE TRACE
→ REPAIR
```

---

## 29. Evidence Preservation Priority

When repair can destroy diagnostic evidence:

```text
EVIDENCE PRESERVATION
```

should precede destructive repair unless doing so would allow greater immediate harm.

This is a governed tradeoff, not an absolute rule.

---

## 30. Security Priority

Security faults may elevate directly to:

```text
RP0
or
RP1
```

depending on active harm and integrity impact.

Functional availability does not justify silently preserving a compromised trust boundary.

---

## 31. Memory Priority

Memory faults should be ordered by their ability to contaminate future reasoning.

High priority:

```text
INVALID MEMORY BEING ACTIVELY RETRIEVED
CORRUPT MEMORY ADMISSION
PROVENANCE-LESS MEMORY PROMOTION
CONFLICT RESOLUTION FAILURE
```

Lower priority:

```text
UNUSED STALE NON-LOAD-BEARING MEMORY
```

provided it cannot reactivate unexpectedly.

---

## 32. Repair-Harm Integration

Priority cannot be determined independently of `K_REPAIR_HARM`.

Suppose:

```text
F1 = HIGH IMPACT
R1 = HIGH REPAIR HARM

F2 = MODERATE IMPACT
R2 = LOW REPAIR HARM
```

The correct order is not automatically `F1`.

Possible result:

```text
CONTAIN F1
→ REPAIR F2
→ GATHER EVIDENCE FOR SAFE R1
```

Repair priority is action-aware.

---

## 33. Reversibility Bias

When candidate repairs have comparable expected benefit:

```text
REVERSIBLE
>
IRREVERSIBLE
```

as a default preference.

This preference may be overridden by active irreversible harm.

---

## 34. Information-Value Priority

Sometimes the highest-priority action is not a repair.

It may be:

```text
TEST
MEASURE
ISOLATE
TRACE
COMPARE
REVALIDATE
```

If a cheap test can discriminate between materially different repair paths, run it first.

```text
HIGH-INFORMATION TEST
>
LOW-CONFIDENCE INTERVENTION
```

when expected decision value is positive.

---

## 35. Sensitivity-First Repair

Identify the smallest unresolved premise that can change repair ordering.

Example:

```text
IF P IS SHARED
→ REPAIR P FIRST

IF P IS INDEPENDENT
→ REPAIR LOCAL FAULTS
```

Then:

```text
VALIDATE P FIRST
```

may be the highest-value action.

---

## 36. Freshness Priority

A stale premise supporting a repair decision must be revalidated when current conditions could have changed materially.

```text
VALID @ T0
```

does not imply:

```text
VALID @ T1
```

Priority computed from stale topology, authority, or state can be invalid.

---

## 37. Regime Priority

Repair ordering is regime-dependent.

```text
PRIORITY(F | G1)
```

does not imply:

```text
PRIORITY(F | G2)
```

Examples of regime change:

```text
NORMAL → INCIDENT
READ-ONLY → WRITE
SIMULATION → PRODUCTION
ISOLATED → NETWORKED
SINGLE-SHARD → CROSS-SHARD
```

Priority must inherit the active applicability envelope.

---

## 38. Scope Firewall

A high-priority fault in one subsystem does not automatically become globally highest priority.

Track:

```text
SYSTEM
ENVIRONMENT
SCALE
TIME
REGIME
MEASUREMENT
ASSUMPTIONS
```

Priority is scoped.

---

## 39. Local Priority

Local repair is allowed when:

```text
DEPENDENCY CLOSURE ESTABLISHED
PROVENANCE INDEPENDENCE ESTABLISHED
NO MATERIAL CONFLICT
REGIME COMPATIBLE
FRESHNESS VALID
AUTHORITY VALID
REPAIR HARM ACCEPTABLE
```

Then:

```text
LOCAL REPAIR
```

may outrank expensive global recomputation.

---

## 40. Global Escalation

Escalate priority analysis when:

```text
DEPENDENCIES AMBIGUOUS
PROVENANCE SHARED
FAULTS CONFLICT
CAUSAL COUPLING EXISTS
REGIME SHIFT OCCURRED
AUTHORITY IS AFFECTED
REPAIR IS IRREVERSIBLE
BLAST RADIUS UNKNOWN
RECOVERY PATH UNCERTAIN
MULTIPLE RSCFs SHARE LOAD-BEARING PREMISES
```

---

## 41. Multi-RSCF Priority

For:

```text
RSCF-A ← P
RSCF-B ← P
RSCF-C ← Q
```

if:

```text
Invalid(P)
```

then repair of `P` may outrank isolated reconstruction of `RSCF-A` and `RSCF-B`.

`RSCF-C` should remain untouched if independent.

```text
INVALIDATE ONLY
DEPENDENT DESCENDANTS
```

---

## 42. Atomic Repair Priority

When multiple RSCFs form one atomic decision:

```text
R1 + R2 + R3 → D
```

priority should target the smallest invalid subset capable of restoring decision validity.

Do not independently commit partially repaired atomic reasoning when atomic validity is required.

---

## 43. MVCC / CAS Priority

A repair computed against version:

```text
V17
```

may become stale after:

```text
V18
```

Priority then becomes:

```text
REVALIDATE REPAIR ASSUMPTIONS
```

before:

```text
COMMIT STALE REPAIR
```

Stale repair execution is never prioritized merely because computation has already been spent.

---

## 44. Priority Stability

A repair queue is not immutable.

Priority may change when:

```text
NEW EVIDENCE ARRIVES
HARM BEGINS PROPAGATING
AUTHORITY CHANGES
REGIME CHANGES
DEPENDENCY TOPOLOGY CHANGES
REPAIR FAILS
ROLLBACK BECOMES UNAVAILABLE
CAUSAL EPOCH ADVANCES
```

Therefore:

```text
PRIORITY = STATE-DEPENDENT
```

---

## 45. Priority Inheritance

A descendant fault may inherit urgency from an ancestor but not necessarily identical priority.

Likewise, an ancestor may inherit priority from the number or importance of affected descendants.

This inheritance must be dependency-aware.

Simple counting is insufficient.

---

## 46. Priority Ceiling from Evidence

Confidence in repair ordering cannot exceed the weakest load-bearing premise.

```text
CONFIDENCE(PRIORITY ORDER)
≤
MIN(
  FAULT VALIDITY,
  DEPENDENCY VALIDITY,
  CAUSAL VALIDITY,
  SCOPE VALIDITY,
  FRESHNESS,
  PROVENANCE INDEPENDENCE,
  REPAIR-HARM ESTIMATE
)
```

If one load-bearing dimension is unknown:

```text
PRIORITY ORDER
→ CONDITIONAL
or
UNKNOWN/GAP
```

---

## 47. Competing Priorities

Do not force a total ordering when evidence supports incomparable repair priorities.

Example:

```text
F1 = HIGH SECURITY RISK
F2 = HIGH DATA-LOSS RISK
```

If harms cannot be validly compared:

```text
F1
vs
F2
=
COMPETING
```

Then seek a discriminating fact or parallel containment path.

---

## 48. Parallel Repair

Parallel repair is allowed only when independence is demonstrated.

Required properties may include:

```text
NO SHARED MUTABLE STATE
NO SHARED LOAD-BEARING PREMISE
NO CAUSAL COUPLING
NO AUTHORITY CONFLICT
NO COMMIT CONFLICT
NO REPAIR-HARM INTERACTION
```

Independence must not be assumed from separate filenames, agents, or modules.

---

## 49. Repair Queue

Conceptually:

```yaml
repair_queue:
  epoch:
  generated_at:
  regime:
  authoritative_state:
  items:
    - fault_id:
      repair_id:
      priority_class:
      priority_basis:
      blockers: []
      dependencies: []
      containment_required:
      repair_harm:
      reversibility:
      authority_required:
      confidence:
      freshness:
```

Queue order must be recomputable from evidence.

---

## 50. Priority Decision Gate

```text
FAULT CONFIRMED?
├── NO
│   └── DIAGNOSE / UNKNOWN/GAP
└── YES
    ↓
ACTIVE IRREVERSIBLE HARM?
├── YES
│   └── RP0 CONTAINMENT
└── NO
    ↓
INTEGRITY / AUTHORITY / SECURITY LOAD-BEARING?
├── YES
│   └── RP1
└── NO
    ↓
SHARED DEPENDENCY / CAUSAL ROOT?
├── YES
│   └── RP2
└── NO
    ↓
CAN IT FLIP A CONSEQUENTIAL DECISION?
├── YES
│   └── RP3
└── NO
    ↓
REQUIRED FUNCTION BROKEN?
├── YES
│   └── RP4
└── NO
    ↓
DEGRADATION?
├── YES
│   └── RP5
└── NO
    ↓
EXPLANATORY / MAINTENANCE?
├── YES
│   └── RP6
└── NO
    ↓
RP7 / RPX
```

Every branch remains subject to repair-harm and authority checks.

---

## 51. Priority vs Cost

Cheap repairs should not automatically precede expensive load-bearing repairs.

But cost matters when outcomes are equivalent.

If:

```text
R1
and
R2
```

produce equivalent validated outcomes with equivalent risk:

```text
LOWER COST / LOWER COMPLEXITY
```

may be preferred.

Optimization occurs only after integrity constraints are satisfied.

---

## 52. Priority vs Speed

Fast repair is valuable only when validity is preserved.

```text
FAST INVALID REPAIR
<
SLOWER VALID REPAIR
```

However:

```text
FAST SAFE CONTAINMENT
```

may outrank complete diagnosis during active harm.

---

## 53. Priority vs Completeness

Do not delay critical repair merely to obtain irrelevant completeness.

Use:

```text
SMALLEST SUFFICIENT PROOF SCOPE
```

Resolve only evidence capable of changing:

```text
WHAT TO CONTAIN
WHAT TO REPAIR
REPAIR ORDER
REPAIR SAFETY
AUTHORITY
```

---

## 54. Failed Repair Reprioritization

When repair `R1` fails:

```text
R1 FAILS
↓
PRESERVE TRACE
↓
INVALIDATE FAILED ASSUMPTIONS
↓
REASSESS FAULT / DEPENDENCY MODEL
↓
RECOMPUTE PRIORITY
```

Do not automatically keep `R1` at the top of the queue.

---

## 55. Repair Cascade Priority

If:

```text
REPAIR A
→ BREAK B
→ REPAIR B
→ BREAK C
```

then priority becomes:

```text
STOP CASCADE
→ REASSESS SHARED DEPENDENCY / CAUSAL MODEL
```

rather than continuing downstream patching.

---

## 56. Repair Thrashing Priority

Repeated oscillation:

```text
R1
→ ROLLBACK
→ R1
→ ROLLBACK
```

elevates:

```text
ROOT-CAUSE REASSESSMENT
```

above another identical retry.

---

## 57. Homeostasis Interaction

`K_HOMEOSTASIS` identifies deviations requiring regulation.

`K_REPAIR_PRIORITY` determines ordering among candidate corrections.

```text
K_HOMEOSTASIS
→ WHAT IS OUT OF BOUNDS?

K_REPAIR_PRIORITY
→ WHAT SHOULD BE ADDRESSED FIRST?

K_REPAIR_HARM
→ IS THE PROPOSED CORRECTION SAFE ENOUGH?
```

---

## 58. Collapse Recovery Interaction

When system validity collapses:

```text
K_COLLAPSE_RECOVERY
```

governs recovery structure.

`K_REPAIR_PRIORITY` orders recovery targets within that structure.

Canonical relationship:

```text
COLLAPSE
→ CONTAIN
→ IDENTIFY VALID SURVIVING STATE
→ PRIORITIZE LOAD-BEARING RESTORATION
→ REPAIR
→ REVALIDATE
```

---

## 59. Repair-Harm Interaction

```text
K_REPAIR_PRIORITY
=
WHAT SHOULD BE REPAIRED FIRST?

K_REPAIR_HARM
=
WHAT DAMAGE COULD THAT REPAIR CREATE?
```

Neither replaces the other.

A high-priority fault may require delayed repair if all known repair paths currently create greater unacceptable harm.

---

## 60. Authority Boundary

`K_REPAIR_PRIORITY` may determine:

```text
FAULT A SHOULD PRECEDE FAULT B
CONTAINMENT SHOULD PRECEDE REPAIR
REVALIDATION SHOULD PRECEDE COMMIT
FAULT REQUIRES ESCALATION
PRIORITY IS COMPETING
PRIORITY IS UNKNOWN/GAP
```

It does not independently grant:

```text
COMMIT AUTHORITY
POLICY EXCEPTION
CANON MODIFICATION
EXTERNAL SIDE-EFFECT PERMISSION
SECURITY EXCEPTION
```

---

## 61. Runtime Boundary

```text
K_REPAIR_PRIORITY
=
PRIORITY LOGIC
+
ORDERING CONSTRAINTS
+
ESCALATION CONDITIONS
```

while:

```text
RUNTIME
=
QUEUE EXECUTION
+
SCHEDULING
+
ROUTING
+
RETRY
+
ACTUATION
```

and:

```text
CONTROL_PLANE
=
AUTHORITY
+
POLICY
+
COMMIT
+
PROVENANCE GOVERNANCE
```

---

## 62. Priority Proof Capsule

Important priority decisions should conceptually preserve:

```yaml
repair_priority_proof:
  claim:
  conclusion_class:
  fault_set: []
  selected_fault:
  selected_repair:
  priority_class:
  load_bearing_premises: []
  evidence: []
  provenance: []
  dependency_scope:
  causal_scope:
  regime:
  freshness:
  active_harm:
  propagation_risk:
  irreversibility:
  repair_harm:
  competing_priorities: []
  falsifiers: []
  invalidation_conditions: []
  confidence_ceiling:
```

---

## 63. Adversarial Priority Validation

For consequential priority decision:

```text
REPAIR A BEFORE B
```

challenge using a genuinely different path.

Seek:

```text
HIDDEN ACTIVE HARM IN B
MISIDENTIFIED ROOT CAUSE
CORRELATED PROVENANCE
STALE TOPOLOGY
SCOPE LEAKAGE
REGIME SHIFT
CAUSAL OVERREACH
UNKNOWN BLAST RADIUS
AUTHORITY CONFLICT
REPAIR-HARM REVERSAL
LOSS OF RECOVERY OPTIONS
```

If challenge succeeds:

```text
REORDER
CONDITION
PRESERVE COMPETING
OR
UNKNOWN/GAP
```

---

## 64. Priority Invariants

```text
KRP-01
ACTIVE IRREVERSIBLE HARM MUST NOT BE IGNORED
FOR A MORE CONVENIENT REPAIR

KRP-02
VISIBILITY MUST NOT DETERMINE PRIORITY BY ITSELF

KRP-03
SEVERITY MUST NOT BE CONFUSED WITH PRIORITY

KRP-04
ROOT CAUSE MUST NOT BE CONFUSED WITH FIRST ACTION

KRP-05
CONTAINMENT MUST BE DISTINGUISHED FROM REPAIR

KRP-06
LOAD-BEARING DEPENDENCIES SHOULD BE RESTORED
BEFORE REDUNDANT DESCENDANT REPAIR WHEN VALIDATED

KRP-07
SHARED STRUCTURE MUST NOT BE TREATED AS PROOF
OF SHARED CAUSATION

KRP-08
REPAIR PRIORITY MUST INCLUDE REPAIR-HARM RISK

KRP-09
UNKNOWN/GAP MUST NOT BE SILENTLY ASSIGNED LOW PRIORITY

KRP-10
IRREVERSIBLE LOSS REQUIRES HEIGHTENED PRIORITY CONSIDERATION

KRP-11
RECOVERY CAPABILITY MUST BE PROTECTED

KRP-12
PROVENANCE REQUIRED FOR RECOVERY MUST NOT BE DESTROYED
FOR CLEANUP CONVENIENCE

KRP-13
AUTHORITY FAILURES MUST NOT BE BYPASSED
BY DOWNSTREAM REPAIR

KRP-14
SECURITY INTEGRITY MUST NOT BE TRADED
FOR FUNCTIONAL AVAILABILITY WITHOUT GOVERNED AUTHORITY

KRP-15
VALID UNAFFECTED STATE MUST NOT BE REPAIRED
MERELY BECAUSE RELATED STATE FAILED

KRP-16
PRIORITY MUST BE RECOMPUTED AFTER MATERIAL STATE CHANGE

KRP-17
STALE REPAIR PLANS REQUIRE REVALIDATION

KRP-18
PARALLEL REPAIR REQUIRES DEMONSTRATED INDEPENDENCE

KRP-19
FAILED REPAIR MUST CHANGE THE EVIDENCE STATE

KRP-20
REPEATED FAILED REPAIR MUST TRIGGER REASSESSMENT

KRP-21
REPAIR CASCADE MUST ELEVATE DEPENDENCY / CAUSAL REASSESSMENT

KRP-22
DECISION-FLIPPING UNCERTAINTY SHOULD BE RESOLVED
BEFORE NONCRITICAL BACKGROUND REPAIR

KRP-23
PRIORITY CONFIDENCE MUST NOT EXCEED
THE WEAKEST LOAD-BEARING PREMISE

KRP-24
INCOMPARABLE PRIORITIES MUST REMAIN COMPETING
UNTIL DISCRIMINATING EVIDENCE EXISTS

KRP-25
CAPABILITY MUST NOT BE CONFUSED WITH AUTHORITY

KRP-26
PRIORITY CLASSIFICATION MUST NOT ITSELF EXECUTE A REPAIR

KRP-27
PERFORMANCE REPAIR MUST NOT OUTRANK INTEGRITY REPAIR

KRP-28
COSMETIC REPAIR MUST NOT DISPLACE
UNRESOLVED DECISION-RELEVANT FAILURE

KRP-29
PRIORITY MUST RESPECT ACTIVE SCOPE AND REGIME

KRP-30
UNKNOWN/GAP MUST NOT PASS AS A VALID PRIORITY PROOF
```

---

## 65. Required Tests

```text
ACTIVE-HARM PRIORITY TEST
IRREVERSIBILITY PRIORITY TEST
CONTAINMENT-BEFORE-REPAIR TEST
ROOT-CAUSE ORDERING TEST
ANCESTOR-FIRST TEST
SELECTIVE-INVALIDATION TEST
SHARED-DEPENDENCY TEST
CAUSAL-PRIORITY TEST
CAUSAL-EPOCH TEST
PROPAGATION-RISK TEST
RECOVERY-OPTION TEST
AUTHORITY-PRIORITY TEST
PROVENANCE-PRESERVATION TEST
SECURITY-PRIORITY TEST
MEMORY-CONTAMINATION TEST
REPAIR-HARM INTEGRATION TEST
REVERSIBILITY TEST
INFORMATION-VALUE TEST
SENSITIVITY-FIRST TEST
FRESHNESS TEST
REGIME-SHIFT TEST
SCOPE-FIREWALL TEST
LOCAL-PRIORITY TEST
GLOBAL-ESCALATION TEST
MULTI-RSCF TEST
ATOMIC-REPAIR TEST
MVCC/CAS STALENESS TEST
COMPETING-PRIORITY TEST
PARALLEL-INDEPENDENCE TEST
FAILED-REPAIR REPRIORITIZATION TEST
REPAIR-CASCADE TEST
REPAIR-THRASHING TEST
UNKNOWN-GAP TEST
```

---

## 66. Negative Tests

```text
MOST VISIBLE FAULT
→ HIGHEST PRIORITY
MUST FAIL

MOST SEVERE FAULT
→ ALWAYS FIRST REPAIR
MUST FAIL

ROOT CAUSE KNOWN
→ ROOT CAUSE ALWAYS FIRST ACTION
MUST FAIL

FAULT LOCAL
→ REPAIR LOCAL FIRST
MUST FAIL

THREE CHILDREN FAIL
→ SHARED PARENT CAUSED THEM
MUST FAIL

NEWEST FAULT
→ HIGHEST PRIORITY
MUST FAIL

CHEAPEST REPAIR
→ FIRST REPAIR
MUST FAIL

FASTEST REPAIR
→ FIRST REPAIR
MUST FAIL

MODEL SAYS HIGH PRIORITY
→ AUTHORIZED EXECUTION
MUST FAIL

TOOL CAN FIX
→ TOOL MAY FIX
MUST FAIL

FAULT HAS HIGH CONFIDENCE
→ HIGHEST PRIORITY
MUST FAIL

UNKNOWN BLAST RADIUS
→ LOW PRIORITY
MUST FAIL

DOWNSTREAM SYMPTOM FIXED
→ ROOT FAULT REPAIRED
MUST FAIL

SEPARATE MODULES
→ INDEPENDENT PARALLEL REPAIR
MUST FAIL

OLD PRIORITY QUEUE
→ STILL VALID AFTER REGIME CHANGE
MUST FAIL

REPAIR FAILED
→ RETRY SAME REPAIR FOREVER
MUST FAIL

PERFORMANCE DEGRADED
→ OUTRANK INTEGRITY FAILURE
MUST FAIL

COSMETIC GAP EASY
→ REPAIR BEFORE CRITICAL GAP
MUST FAIL

UNKNOWN/GAP
→ PASS
MUST FAIL
```

---

## 67. Failure Modes

```text
VISIBILITY BIAS
SEVERITY-ONLY PRIORITIZATION
RECENCY BIAS
CONVENIENCE BIAS
COST BIAS
ROOT-CAUSE DOGMATISM
SYMPTOM CHASING
DOWNSTREAM PATCH CASCADE
REPAIR THRASHING
GLOBAL RECOMPUTATION BIAS
LOCALITY ASSUMPTION
FALSE INDEPENDENCE
STALE PRIORITY QUEUE
REGIME-STALE PRIORITY
PROVENANCE LOSS
RECOVERY-OPTION LOSS
AUTHORITY BYPASS
SECURITY REGRESSION
REPAIR-HARM BLINDNESS
IRREVERSIBILITY BLINDNESS
CAUSAL OVERREACH
SHARED-ANCESTRY CONFUSION
UNKNOWN-AS-LOW-PRIORITY
PREMATURE TOTAL ORDERING
```

---

## 68. Recovery Semantics

When priority ordering is discovered to be wrong:

```text
DETECT PRIORITY FAILURE
↓
STOP NONESSENTIAL REPAIR EXECUTION
↓
PRESERVE TRACE
↓
CONTAIN ACTIVE HARM
↓
INVALIDATE FAILED PRIORITY PREMISES
↓
PRESERVE UNAFFECTED VALID REPAIRS
↓
RECONSTRUCT MINIMUM DEPENDENCY / CAUSAL SCOPE
↓
RECOMPUTE PRIORITY
↓
RESUME THROUGH AUTHORIZED PATH
```

Do not globally undo successful independent repairs unless their validity depends on the failed priority premise.

---

## 69. Promotion Gate

Before promotion beyond `AMOS_MODEL`, evidence should establish:

```text
[ ] fault schema implemented
[ ] repair candidate schema implemented
[ ] priority classes implemented
[ ] active-harm detection integrated
[ ] dependency criticality implemented
[ ] selective invalidation implemented
[ ] causal-priority checks implemented
[ ] propagation-risk handling implemented
[ ] repair-harm integration implemented
[ ] reversibility handling implemented
[ ] provenance preservation tested
[ ] recovery-option preservation tested
[ ] authority boundary enforced
[ ] security-priority tests passed
[ ] regime/freshness invalidation implemented
[ ] competing-priority representation implemented
[ ] parallel independence proof implemented
[ ] multi-RSCF repair ordering tested
[ ] MVCC/CAS stale-plan handling tested
[ ] failed-repair reprioritization tested
[ ] cascade/thrashing escalation tested
[ ] observability wired
[ ] unresolved critical gaps registered
```

Until evidenced:

```text
REPAIR_PRIORITY_RUNTIME = UNKNOWN/GAP
AUTOMATED_PRIORITY_QUEUE = UNKNOWN/GAP
AUTOMATED_CAUSAL_PRIORITY = UNKNOWN/GAP
AUTOMATED_DEPENDENCY_CRITICALITY = UNKNOWN/GAP
AUTOMATED_PROPAGATION_RISK = UNKNOWN/GAP
AUTOMATED_REPAIR_HARM_PRIORITY = UNKNOWN/GAP
PARALLEL_REPAIR_INDEPENDENCE_PROOF = UNKNOWN/GAP
MULTI_RSCF_PRIORITY_RUNTIME = UNKNOWN/GAP
CAUSAL_EPOCH_PRIORITY_RUNTIME = UNKNOWN/GAP
FORMAL_PRIORITY_OPTIMALITY_PROOF = UNKNOWN/GAP
EMPIRICAL_VALIDATION = UNKNOWN/GAP
```

---

## 70. RSCF Node

```RSCF-NODE
node_id: AMOS-OS-K-REPAIR-PRIORITY
node_type: kernel_repair_priority_contract
domain: AMOS_OS_KERNEL
functional_type: RepairPriorityKernel
lifecycle_stage: Architecture
claim_class: AMOS_MODEL

RSCF-RELATIONS:
  - ROOTED_IN: [[00_ROOT/README]]
  - DEPENDENCY_BOUND_TO: [[00_ROOT/DEPENDENCY_MAP]]

  - GOVERNED_BY: [[01_CANON/AMOS_CORE_LAWS]]
  - CONSTRAINED_BY: [[01_CANON/INVARIANT_REGISTRY]]
  - PRECEDENCE_GOVERNED_BY: [[01_CANON/LAW_HIERARCHY]]
  - PROVENANCE_GOVERNED_BY: [[01_CANON/CANON_PROVENANCE]]
  - AUTHORITY_BOUND_TO: [[01_CANON/AUTHORITY_CANON]]

  - INDEXED_BY: [[02_KERNEL/00_INDEX/KERNEL_MAP]]
  - LOGIC_BOUND_TO: [[02_KERNEL/K_CORE19_LOGIC]]
  - META_LOGIC_BOUND_TO: [[02_KERNEL/K_META_LOGIC]]
  - STRUCTURAL_REASONING_BOUND_TO: [[02_KERNEL/K_STRUCTURAL_REASONING]]
  - CAUSAL_CLOSURE_BOUND_TO: [[02_KERNEL/K_CAUSAL_CLOSURE]]
  - CAUSAL_EPOCH_BOUND_TO: [[02_KERNEL/K_CAUSAL_EPOCH]]
  - SYSTEM_STATE_BOUND_TO: [[02_KERNEL/K_SYSTEM_STATE]]

  - HOMEOSTASIS_BOUND_TO: [[02_KERNEL/K_HOMEOSTASIS]]
  - REPAIR_HARM_BOUND_TO: [[02_KERNEL/K_REPAIR_HARM]]
  - RECOVERY_BOUND_TO: [[02_KERNEL/K_COLLAPSE_RECOVERY]]

  - MEMORY_ADMISSION_BOUND_TO: [[02_KERNEL/K_MEMORY_ADMISSION]]
  - MEMORY_CONFLICT_BOUND_TO: [[02_KERNEL/K_MEMORY_CONFLICT]]
  - MEMORY_IMMUNE_BOUND_TO: [[02_KERNEL/K_MEMORY_IMMUNE]]
  - MEMORY_RETRIEVAL_BOUND_TO: [[02_KERNEL/K_MEMORY_RETRIEVAL]]

  - STATE_INTERACTION: [[12_STATE/00_INDEX/README]]
  - OBSERVED_BY: [[17_OBSERVABILITY/00_INDEX/README]]
  - SECURITY_CONSTRAINED_BY: [[18_SECURITY/00_INDEX/README]]
  - VERIFIED_BY: [[19_TESTS/00_INDEX/README]]
  - OPERATED_BY: [[20_OPERATIONS/00_INDEX/README]]
```

---

## 71. Canonical Repair-Priority Summary

```text
MULTIPLE FAULTS EXIST
↓
IS ACTIVE IRREVERSIBLE HARM OCCURRING?
├── YES
│   ↓
│   CONTAIN FIRST
└── NO
    ↓
PRESERVE:
  EVIDENCE
  PROVENANCE
  RECOVERY OPTIONS
↓
IDENTIFY:
  LOAD-BEARING DEPENDENCIES
  CAUSAL ROOTS
  SHARED STATE
  AUTHORITY IMPACT
  SECURITY IMPACT
  PROPAGATION RISK
↓
IS A LOAD-BEARING ANCESTOR INVALID?
├── YES
│   ↓
│   PRIORITIZE ANCESTOR
│   UNLESS DOWNSTREAM CONTAINMENT IS URGENT
└── NO
    ↓
CAN AN UNCERTAINTY FLIP THE REPAIR ORDER?
├── YES
│   ↓
│   RUN CHEAPEST HIGH-INFORMATION TEST
└── NO
    ↓
EVALUATE CANDIDATE REPAIR HARM
↓
PRIORITIES COMPARABLE?
├── NO
│   ↓
│   PRESERVE COMPETING
│   OR PARALLEL CONTAINMENT IF INDEPENDENT
└── YES
    ↓
SELECT HIGHEST VALID PRIORITY
↓
AUTHORITY VALID?
├── NO
│   ↓
│   ESCALATE / DO NOT COMMIT
└── YES
    ↓
EXECUTE MINIMUM SUFFICIENT REPAIR
↓
REVALIDATE
↓
RECOMPUTE QUEUE
```

Core laws:

```text
REPAIR PRIORITY != VISIBILITY
REPAIR PRIORITY != SEVERITY ALONE
ROOT CAUSE != ALWAYS FIRST ACTION
CONTAINMENT != REPAIR
ACTIVE IRREVERSIBLE HARM COMES FIRST
LOAD-BEARING VALIDITY PRECEDES CONVENIENCE
DEPENDENCY ROOTS PRECEDE REDUNDANT DESCENDANT PATCHING
REPAIR HARM CAN CHANGE REPAIR ORDER
INFORMATION CAN OUTRANK INTERVENTION
VALID UNAFFECTED STATE SHOULD SURVIVE
PRIORITY IS SCOPE + REGIME + STATE DEPENDENT
PRIORITY MUST BE RECOMPUTED AFTER MATERIAL CHANGE
INDEPENDENCE MUST BE DEMONSTRATED
INCOMPARABLE PRIORITIES REMAIN COMPETING
CAPABILITY != AUTHORITY
UNKNOWN/GAP != LOW PRIORITY
UNKNOWN/GAP != PASS
```

The decisive invariant is:

```text
AMOS DOES NOT
REPAIR SOMETHING
FIRST

MERELY BECAUSE
IT IS THE
LARGEST,
NEWEST,
LOUDEST,
EASIEST,
OR MOST
VISIBLE
PROBLEM.

AMOS FIRST ASKS:

IS HARM
STILL SPREADING?

CAN SOMETHING
IRREVERSIBLE
BE LOST?

WHAT VALID STATE
MUST BE
PRESERVED?

WHAT DOES
THE FAILURE
DEPEND ON?

WHAT DEPENDS
ON THE
FAILURE?

IS THERE
A SHARED
LOAD-BEARING
PREMISE?

IS THE
VISIBLE ERROR
ONLY A
DESCENDANT?

IS THE
ROOT CAUSE
KNOWN,
OR ONLY
ASSUMED?

DOES A
CHEAP TEST
CHANGE THE
REPAIR ORDER?

WHAT HARM
CAN THE
REPAIR ITSELF
CREATE?

IS THE
REPAIR
REVERSIBLE?

IS IT
AUTHORIZED?

IF ACTIVE
IRREVERSIBLE
HARM EXISTS,

AMOS
CONTAINS IT
FIRST.

IF A
LOAD-BEARING
PREMISE FAILS,

AMOS REPAIRS
THE MINIMUM
VALID ROOT
AND ITS
DEPENDENT
DESCENDANTS.

IT PRESERVES
INDEPENDENT
VALID STATE.

IT DOES NOT
PATCH EVERY
SYMPTOM
WHEN ONE
VALIDATED
ANCESTOR
EXPLAINS THEM.

IT DOES NOT
ASSUME
A COMMON
CAUSE
FROM COMMON
STRUCTURE.

IT DOES NOT
FORCE
INCOMPARABLE
RISKS INTO
A FALSE
TOTAL ORDER.

IT DOES NOT
PRIORITIZE
PERFORMANCE
OVER
INTEGRITY.

IT DOES NOT
PRIORITIZE
COSMETIC
COMPLETENESS
OVER
DECISION-
RELEVANT
VALIDITY.

WHEN THE
EVIDENCE
CHANGES,

THE PRIORITY
CAN CHANGE.

WHEN A
REPAIR FAILS,

THE FAILURE
BECOMES
NEW EVIDENCE.

WHEN THE
ORDER CANNOT
BE VALIDLY
DETERMINED,

AMOS DOES
NOT GUESS.

IT RETURNS:

COMPETING

OR

UNKNOWN/GAP.
```

## Related

[[00_ROOT/README]] ·
[[00_ROOT/DEPENDENCY_MAP]] ·
[[01_CANON/AMOS_CORE_LAWS]] ·
[[01_CANON/INVARIANT_REGISTRY]] ·
[[01_CANON/LAW_HIERARCHY]] ·
[[01_CANON/CANON_PROVENANCE]] ·
[[01_CANON/AUTHORITY_CANON]] ·
[[02_KERNEL/00_INDEX/KERNEL_MAP]] ·
[[02_KERNEL/K_CORE19_LOGIC]] ·
[[02_KERNEL/K_META_LOGIC]] ·
[[02_KERNEL/K_STRUCTURAL_REASONING]] ·
[[02_KERNEL/K_CAUSAL_CLOSURE]] ·
[[02_KERNEL/K_CAUSAL_EPOCH]] ·
[[02_KERNEL/K_SYSTEM_STATE]] ·
[[02_KERNEL/K_HOMEOSTASIS]] ·
[[02_KERNEL/K_REPAIR_HARM]] ·
[[02_KERNEL/K_COLLAPSE_RECOVERY]] ·
[[02_KERNEL/K_MEMORY_ADMISSION]] ·
[[02_KERNEL/K_MEMORY_CONFLICT]] ·
[[02_KERNEL/K_MEMORY_IMMUNE]] ·
[[02_KERNEL/K_MEMORY_RETRIEVAL]] ·
[[12_STATE/00_INDEX/README]] ·
[[17_OBSERVABILITY/00_INDEX/README]] ·
[[18_SECURITY/00_INDEX/README]] ·
[[19_TESTS/00_INDEX/README]] ·
[[20_OPERATIONS/00_INDEX/README]]

```text

**Classification note:** this replaces the placeholder with a substantive **AMOS_MODEL** kernel contract; it does not establish that `K_REPAIR_PRIORITY` is implemented, empirically validated, formally proven, or promoted into final canon. Those remain `UNKNOWN/GAP` until the stated promotion evidence exists.
```

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]
