---
canon-group: meta
canon-type: framework
rscf-state: source-claim
topic: K Law Hierarchy
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---

# K_LAW_HIERARCHY

> **AMOS Core target:** `v4.4`
> **Origin architect / steward:** Trang Phan
> **Plane:** `02_KERNEL`
> **Status:** `AMOS_MODEL`
> **Conclusion class:** `AMOS_MODEL`

## Purpose

`K_LAW_HIERARCHY` defines the deterministic precedence model used when multiple AMOS laws, invariants, constraints, policies, rules, or instructions are simultaneously applicable.
Its central function is:

```text
APPLICABLE RULES
↓
AUTHORITY CLASSIFICATION
↓
SCOPE / REGIME FILTERING
↓
PRECEDENCE RESOLUTION
↓
CONFLICT DETECTION
↓
VALID RULE SET
```

## The kernel prevents arbitrary conflict resolution. It does **not** create authority. It evaluates authority and precedence already established through AMOS canon and governance structures. rscf: state: DERIVED claim_class: DERIVED provenance: AMOS_corpus scope: AMOS_general

## 1. Core Law

```text
INTEGRITY
>
COMPLETENESS
>
FLUENCY
>
SPEED
>
TOKEN SAVINGS
```

No optimization may reverse this order.

Therefore:

```text
FASTER
!=
MORE AUTHORITATIVE

MORE COMPLETE
!=
MORE CORRECT

MORE RECENT
!=
HIGHER AUTHORITY

MORE SPECIFIC
!=
AUTOMATICALLY HIGHER AUTHORITY

MORE POPULAR
!=
MORE AUTHORITATIVE
```

______________________________________________________________________

## 2. Architectural Position

```text
01_CANON
   │
   ├── AMOS_CORE_LAWS
   ├── LAW_HIERARCHY
   ├── INVARIANT_REGISTRY
   ├── AUTHORITY_CANON
   └── SUPERSESSION_LOG
   │
   ↓
02_KERNEL
   │
   ├── K_CORE19_LOGIC
   ├── K_DISTINCTION_RELATION_CONSTRAINT
   └── K_LAW_HIERARCHY
   │
   ↓
03_CONTROL_PLANE
   │
   ↓
04_RUNTIME
```

The distinction is critical:

```text
CANONICAL LAW DEFINITION
!=
KERNEL LAW EVALUATION
```

`01_CANON/LAW_HIERARCHY` defines authoritative hierarchy.

`K_LAW_HIERARCHY` provides the deterministic reasoning contract for evaluating that hierarchy.

______________________________________________________________________

## 3. Hard Boundary

```text
CANON != KERNEL
KERNEL != AUTHORITY
AUTHORITY != CAPABILITY
POLICY != LAW
RULE != INVARIANT
DEFAULT != MANDATE
PROPOSAL != COMMIT
CONFLICT != SUPERSESSION
SUPERSESSION != DELETION
RECENCY != PRECEDENCE
SPECIFICITY != AUTHORITY
UNKNOWN/GAP != PASS
```

______________________________________________________________________

## 4. Law Object

A law should be treated as a typed object rather than an unstructured sentence.

Conceptually:

```yaml
law:
  law_id:
  canonical_name:

  law_class:
  authority_class:
  authority_source:

  statement:

  scope:
  regime:
  temporal_validity:

  priority:
  specificity:

  dependencies: []
  exceptions: []

  provenance:
  supersedes: []
  superseded_by: []

  conflict_policy:
  failure_policy:

  status:
  conclusion_class:
```

Only fields material to a particular law need to be instantiated.

______________________________________________________________________

## 5. Law Classes

AMOS should distinguish at minimum:

```text
CORE LAW
CANON LAW
INVARIANT
KERNEL CONSTRAINT
CONTROL-PLANE POLICY
PROTOCOL RULE
RUNTIME RULE
DOMAIN RULE
LOCAL RULE
DEFAULT
HEURISTIC
MODEL ASSUMPTION
USER REQUEST
```

These classes are not interchangeable.

______________________________________________________________________

## 6. Authority Classes

Conceptually:

```text
A0 = ROOT INTEGRITY LAW
A1 = CANONICAL SYSTEM LAW
A2 = REGISTERED INVARIANT
A3 = GOVERNANCE / AUTHORITY CONSTRAINT
A4 = KERNEL SEMANTIC / LOGICAL CONSTRAINT
A5 = CONTROL-PLANE POLICY
A6 = PROTOCOL / INTERFACE CONTRACT
A7 = RUNTIME / WORKFLOW RULE
A8 = DOMAIN-SCOPED RULE
A9 = LOCAL CONFIGURATION / DEFAULT
A10 = HEURISTIC / OPTIMIZATION
```

This numbering is an architectural model for deterministic comparison.

It must not be interpreted as recovered historical canon unless explicitly bound to canonical source lineage.

______________________________________________________________________

## 7. Default Precedence

Conceptually:

```text
ROOT INTEGRITY
↓
CANON
↓
INVARIANTS
↓
AUTHORITY CONSTRAINTS
↓
KERNEL CONSTRAINTS
↓
CONTROL-PLANE POLICY
↓
PROTOCOL CONTRACTS
↓
RUNTIME RULES
↓
DOMAIN RULES
↓
LOCAL DEFAULTS
↓
HEURISTICS
```

But precedence evaluation must still check:

```text
APPLICABILITY
SCOPE
REGIME
TIME
SUPERSESSION
EXCEPTION
DEPENDENCY
```

before selecting a rule.

______________________________________________________________________

## 8. Precedence Function

For rules `A` and `B`, conceptual precedence may be represented as:

```text
P(A, B | C)
```

where `C` is the active context.

Possible results:

```text
A_PRECEDES_B
B_PRECEDES_A
EQUIVALENT
NON_COMPARABLE
CONFLICT
UNKNOWN
```

AMOS must not force a total order where only a partial order is justified.

______________________________________________________________________

## 9. Partial-Order Principle

The law hierarchy is not necessarily:

```text
EVERY LAW
>
OR
<
EVERY OTHER LAW
```

Two rules may apply to unrelated domains.

Example:

```text
SECURITY_RULE_A
```

and:

```text
DOCUMENT_FORMAT_RULE_B
```

may have no meaningful precedence relation.

Therefore:

```text
NON_COMPARABLE
```

is a valid result.

______________________________________________________________________

## 10. Applicability Before Precedence

Before comparing authority:

```text
IS LAW A APPLICABLE?
IS LAW B APPLICABLE?
```

must be established.

Conceptually:

```text
APPLICABLE(L, C)
=
SCOPE_MATCH
∧ REGIME_MATCH
∧ TEMPORAL_VALID
∧ STATUS_VALID
∧ DEPENDENCIES_VALID
```

A high-authority law outside its declared applicability envelope must not be silently generalized.

______________________________________________________________________

## 11. Scope Firewall

A law may apply only to:

```text
SYSTEM
SUBSYSTEM
DOMAIN
POPULATION
ENVIRONMENT
JURISDICTION
SCALE
OPERATION
ARTIFACT TYPE
```

Example:

```text
LAW_A(scope = MEMORY)
```

does not automatically govern:

```text
CONTROL_PLANE
```

unless its scope includes it.

______________________________________________________________________

## 12. Regime Firewall

A law valid under:

```text
REGIME_A
```

does not automatically remain valid under:

```text
REGIME_B
```

Therefore:

```text
VALID(L | R1)
!=
VALID(L | R2)
```

unless regime invariance is established.

______________________________________________________________________

## 13. Temporal Validity

A law may have:

```text
effective_from
effective_until
superseded_at
revalidation_due
```

A law outside its valid temporal envelope must not remain active merely because it exists in the repository.

______________________________________________________________________

## 14. Supersession

Supersession is explicit and directional.

```text
LAW_NEW
--SUPERSEDES-->
LAW_OLD
```

means the old law remains part of provenance history but loses current authority within the supersession scope.

```text
SUPERSEDED
!=
DELETED
```

______________________________________________________________________

## 15. Partial Supersession

A new law may supersede only part of an older law.

Example:

```text
LAW_OLD
├── CLAUSE A
├── CLAUSE B
└── CLAUSE C
```

If:

```text
LAW_NEW supersedes CLAUSE B
```

then:

```text
CLAUSE A = PRESERVED
CLAUSE B = SUPERSEDED
CLAUSE C = PRESERVED
```

unless broader supersession is explicitly declared.

______________________________________________________________________

## 16. Supersession Firewall

The following do not prove supersession:

```text
NEWER DATE
NEWER FILE
NEWER VERSION LABEL
DIFFERENT FILENAME
MORE DETAILED TEXT
MORE RECENT COMMIT
```

Supersession requires authoritative lineage.

______________________________________________________________________

## 17. Version Rule

```text
VERSION
!=
AUTHORITY
```

A newer artifact may be:

```text
DRAFT
MODEL
PROPOSAL
EXPERIMENT
```

while an older artifact remains canonical.

Therefore:

```text
v4 > v3
```

cannot be interpreted as:

```text
AUTHORITY(v4) > AUTHORITY(v3)
```

without valid promotion/supersession evidence.

______________________________________________________________________

## 18. Specificity

Specificity may resolve conflicts only where canon licenses specificity as a precedence rule.

Conceptually:

```text
GENERAL LAW
↓
SCOPED SPECIALIZATION
```

may permit:

```text
SPECIFIC > GENERAL
```

inside the narrower scope.

But:

```text
SPECIFICITY
!=
INHERENT AUTHORITY
```

______________________________________________________________________

## 19. Exception Semantics

An exception must be explicit.

```text
LAW_A
EXCEPT_WHEN
CONDITION_X
```

If `CONDITION_X` is satisfied:

```text
LAW_A
→
EXCEPTION_BRANCH
```

An exception is not equivalent to supersession.

```text
EXCEPTION != SUPERSESSION
```

______________________________________________________________________

## 20. Override Semantics

An override is a governed temporary or scoped precedence alteration.

Conceptually:

```yaml
override:
  override_id:
  target_rule:
  overriding_rule:
  authority_source:
  scope:
  regime:
  effective_from:
  expires_at:
  reason:
  provenance:
```

No override should exist merely because a runtime component chooses to ignore a rule.

______________________________________________________________________

## 21. Override Authority

```text
OVERRIDE CAPABILITY
!=
OVERRIDE AUTHORITY
```

A component capable of changing state cannot automatically override canon or invariants.

Valid override requires an authority path.

______________________________________________________________________

## 22. Non-Overrideable Laws

Some laws may be declared:

```text
NON_OVERRIDEABLE
```

within the system.

Examples conceptually include integrity-preserving constraints such as:

```text
UNKNOWN/GAP != PASS
CAPABILITY != AUTHORITY
PROPOSAL != COMMIT
```

A lower layer cannot waive such a law.

______________________________________________________________________

## 23. Conflict Types

AMOS should distinguish:

```text
DIRECT_CONTRADICTION
PRECEDENCE_CONFLICT
SCOPE_OVERLAP
REGIME_CONFLICT
TEMPORAL_CONFLICT
AUTHORITY_CONFLICT
SUPERSESSION_CONFLICT
EXCEPTION_CONFLICT
DEPENDENCY_CONFLICT
IMPLEMENTATION_CONFLICT
```

Conflict type affects resolution.

______________________________________________________________________

## 24. Direct Contradiction

Example:

```text
LAW_A:
X MUST OCCUR

LAW_B:
X MUST NOT OCCUR
```

If both apply:

```text
DIRECT_CONTRADICTION
```

must be registered.

______________________________________________________________________

## 25. Conflict Resolution

Conceptual resolution sequence:

```text
DETECT CONFLICT
↓
CHECK APPLICABILITY
↓
CHECK AUTHORITY CLASS
↓
CHECK SCOPE
↓
CHECK REGIME
↓
CHECK TEMPORAL VALIDITY
↓
CHECK SUPERSESSION
↓
CHECK EXCEPTIONS
↓
CHECK EXPLICIT PRECEDENCE
↓
RESOLVE OR PRESERVE CONFLICT
```

______________________________________________________________________

## 26. Conflict Preservation

If two applicable laws remain:

```text
EQUAL AUTHORITY
+
INCOMPATIBLE
+
NO VALID PRECEDENCE
```

the result is:

```text
COMPETING / CONFLICT
```

not arbitrary selection.

______________________________________________________________________

## 27. Unknown Precedence

If precedence cannot be established:

```text
PRECEDENCE = UNKNOWN
```

AMOS must not convert that into:

```text
A > B
```

through convenience or intuition.

For a consequential operation:

```text
UNKNOWN PRECEDENCE
→
ESCALATE / BLOCK / CONDITIONAL
```

depending on governance policy.

______________________________________________________________________

## 28. Integrity Ceiling

A derived rule decision cannot have stronger authority than its load-bearing authority premise.

Conceptually:

```text
AUTHORITY(DERIVED_DECISION)
≤
MIN(
  AUTHORITY(PREMISE_1),
  AUTHORITY(PREMISE_2),
  ...
)
```

unless independently revalidated by a higher-authority path.

______________________________________________________________________

## 29. Provenance Requirement

A law's authority requires recoverable provenance.

At minimum where material:

```text
LAW
↓
SOURCE
↓
LINEAGE
↓
AUTHORITY ORIGIN
↓
CURRENT STATUS
```

A law with unknown provenance cannot silently acquire canonical authority.

______________________________________________________________________

## 30. Source Count Firewall

Multiple copies of the same law do not create stronger authority.

```text
COPY_A
COPY_B
COPY_C
```

all derived from:

```text
SOURCE_X
```

remain one provenance family.

Therefore:

```text
REPETITION
!=
INDEPENDENT AUTHORITY
```

______________________________________________________________________

## 31. Authority vs Evidence

```text
AUTHORITY
!=
EVIDENCE QUALITY
```

A canonical rule may define how AMOS operates without constituting empirical evidence about the external world.

Likewise:

```text
STRONG EMPIRICAL EVIDENCE
!=
SYSTEM AUTHORITY
```

unless governance promotes it into a rule.

______________________________________________________________________

## 32. Law vs Model

```text
MODEL
```

describes, predicts, estimates, or organizes.

```text
LAW
```

constrains permissible system behavior.

Therefore:

```text
MODEL OUTPUT
!=
LAW
```

and:

```text
MODEL CONFIDENCE
!=
AUTHORITY
```

______________________________________________________________________

## 33. Law vs Policy

A policy is normally a governed operational rule beneath canon/kernel invariants.

Conceptually:

```text
CANON LAW
↓
KERNEL CONSTRAINT
↓
CONTROL-PLANE POLICY
```

Policy may specialize behavior but cannot silently contradict higher authority.

______________________________________________________________________

## 34. Law vs Protocol

A protocol defines interaction semantics.

```text
PROTOCOL
```

may constrain message order, schemas, handshakes, retries, and state transitions.

But:

```text
PROTOCOL
!=
ROOT AUTHORITY
```

unless explicitly elevated.

______________________________________________________________________

## 35. Law vs Runtime Rule

Runtime rules govern execution behavior.

Examples:

```text
RETRY LIMIT
TIMEOUT
QUEUE PRIORITY
SCHEDULING POLICY
```

They remain subordinate to higher integrity and authority constraints.

______________________________________________________________________

## 36. Law vs Heuristic

A heuristic may optimize:

```text
SPEED
COST
TOKEN USE
SEARCH DEPTH
ROUTING
```

but:

```text
HEURISTIC
<
INTEGRITY CONSTRAINT
```

Always.

______________________________________________________________________

## 37. Fast-Path Law

AMOS v4.4 permits smallest-sufficient-proof reasoning only when the fast path preserves integrity.

Conceptually:

```text
FAST_PATH_ALLOWED
IFF
DEPENDENCY_CLOSURE_VALID
∧ PROVENANCE_INDEPENDENCE_VALID
∧ SCOPE_COMPATIBLE
∧ REGIME_COMPATIBLE
∧ FRESHNESS_VALID
∧ NO_MATERIAL_CONFLICT
```

Otherwise:

```text
ESCALATE
```

______________________________________________________________________

## 38. Optimization Firewall

No optimization may weaken:

```text
FACTUAL SUPPORT
SCOPE CORRECTNESS
CONTRADICTION VISIBILITY
PROVENANCE RECOVERABILITY
CAUSAL DISCIPLINE
AUTHORITY DISCIPLINE
SAFETY
```

Therefore:

```text
OPTIMIZATION
<
INTEGRITY
```

______________________________________________________________________

## 39. Causal Firewall Precedence

A lower-level reasoning rule cannot override causal discipline.

```text
STRUCTURAL SIMILARITY
!=
CAUSATION
```

```text
CORRELATION
!=
CAUSATION
```

```text
SEQUENCE
!=
CAUSATION
```

No convenience rule can promote these relations into causal proof.

______________________________________________________________________

## 40. Provenance Firewall Precedence

Likewise:

```text
MULTIPLE DESCENDANTS
!=
MULTIPLE INDEPENDENT SOURCES
```

A heuristic counting sources cannot override provenance topology.

______________________________________________________________________

## 41. Scope Firewall Precedence

A rule favoring generalization cannot override explicit scope limits.

```text
VALID IN SCOPE A
```

does not become:

```text
VALID GLOBALLY
```

without revalidation.

______________________________________________________________________

## 42. Regime Firewall Precedence

When regime validity fails:

```text
PREVIOUS CONCLUSION
→
STALE / INVALID / REVALIDATE
```

A cached conclusion cannot override a detected regime shift.

______________________________________________________________________

## 43. Freshness

Freshness is a constraint, not automatic authority.

```text
FRESHER
!=
MORE AUTHORITATIVE
```

But stale evidence may invalidate an otherwise authoritative decision if the law explicitly requires current evidence.

______________________________________________________________________

## 44. Safety / Stakes Escalation

As stakes rise:

```text
REVERSIBILITY ↓
COST ↑
LEGAL EXPOSURE ↑
FINANCIAL EXPOSURE ↑
HEALTH EXPOSURE ↑
SAFETY EXPOSURE ↑
INSTITUTIONAL IMPACT ↑
```

required validation increases.

A speed optimization cannot outrank this governance requirement.

______________________________________________________________________

## 45. Authority Chain

A valid governed action conceptually follows:

```text
CANON
↓
KERNEL VALIDATION
↓
CONTROL-PLANE AUTHORIZATION
↓
RUNTIME EXECUTION
↓
STATE TRANSITION
↓
PROVENANCE RECORD
```

Therefore:

```text
VALID LOGIC
!=
AUTHORIZED ACTION
```

______________________________________________________________________

## 46. Proposal / Commit Hierarchy

```text
PROPOSAL
↓
VALIDATION
↓
AUTHORIZATION
↓
COMMIT
```

A proposal cannot self-promote into committed state.

```text
PROPOSAL != COMMIT
```

______________________________________________________________________

## 47. Capability / Authority Hierarchy

```text
CAPABILITY
↓
PERMISSION CHECK
↓
AUTHORITY CHECK
↓
EXECUTION ELIGIBILITY
```

Thus:

```text
CAN_DO(X)
```

does not establish:

```text
MAY_DO(X)
```

______________________________________________________________________

## 48. Tool Authority

```text
TOOL_AVAILABLE
```

does not imply:

```text
TOOL_AUTHORIZED
```

and:

```text
TOOL_AUTHORIZED
```

does not necessarily imply:

```text
EXTERNAL_EFFECT_AUTHORIZED
```

These are distinct gates.

______________________________________________________________________

## 49. User Instruction Position

User instructions are important runtime inputs.

However, a user request cannot validly override non-overrideable system integrity, safety, authority, or provenance constraints.

Conceptually:

```text
USER OBJECTIVE
↓
APPLICABILITY CHECK
↓
HIGHER CONSTRAINT CHECK
↓
EXECUTION
```

______________________________________________________________________

## 50. Domain Law Position

Domain-specific rules may specialize generic rules where:

```text
DOMAIN SCOPE MATCHES
+
SPECIALIZATION IS AUTHORIZED
+
NO HIGHER LAW IS VIOLATED
```

Then:

```text
DOMAIN_SPECIFIC_RULE
```

may govern the domain operation.

Outside that domain:

```text
NO AUTOMATIC GENERALIZATION
```

______________________________________________________________________

## 51. Local Configuration

Local configuration has narrow authority.

Example:

```text
DEFAULT_TIMEOUT = 30
```

may be overridden by a higher runtime or control-plane policy.

Local configuration cannot rewrite canon.

______________________________________________________________________

## 52. Constraint Composition

If multiple compatible laws apply:

```text
L1
L2
L3
```

they may compose into:

```text
VALID_RULE_SET = L1 ∧ L2 ∧ L3
```

where strict conjunction is appropriate.

But composition rules must be typed.

______________________________________________________________________

## 53. Constraint Closure

For decision `D`, evaluate only laws capable of changing `D`.

```text
LAW_CLOSURE(D)
```

should include:

```text
DIRECT CONSTRAINTS
UPSTREAM AUTHORITY
DEPENDENCIES
EXCEPTIONS
SUPERSESSION
MATERIAL CONFLICTS
```

This prevents unnecessary global recomputation.

______________________________________________________________________

## 54. Locality

```text
LOCAL DECISION
```

may use local law resolution only if dependency closure proves no higher or external rule can alter the outcome.

Otherwise:

```text
ESCALATE
```

______________________________________________________________________

## 55. Conflict Escalation Conditions

Escalate when:

```text
AUTHORITY AMBIGUOUS
PROVENANCE AMBIGUOUS
SUPERSESSION AMBIGUOUS
SCOPE OVERLAP UNRESOLVED
REGIME MISMATCH
EQUAL-RANK CONFLICT
GOVERNANCE IMPACT
IRREVERSIBLE STAKES
DEPENDENCY CLOSURE UNKNOWN
```

______________________________________________________________________

## 56. Deterministic Resolution Algorithm

Conceptually:

```python
def resolve_law_set(laws, context):
    applicable = []

    for law in laws:
        if not scope_matches(law, context):
            continue

        if not regime_matches(law, context):
            continue

        if not temporally_valid(law, context):
            continue

        if is_superseded(law, context):
            continue

        if not dependencies_valid(law, context):
            return UNKNOWN_GAP

        applicable.append(law)

    conflicts = detect_conflicts(applicable)

    for conflict in conflicts:
        result = resolve_explicit_precedence(conflict)

        if result == UNKNOWN:
            return COMPETING

        apply_resolution(result)

    return compose_valid_rules(applicable)
```

This is architectural pseudocode, not evidence of deployed implementation.

______________________________________________________________________

## 57. Resolution Tuple

A law comparison may conceptually evaluate:

```text
R(L) =
<
authority,
scope,
regime,
time,
supersession,
specificity,
exception,
provenance
>
```

But these fields are not simply numeric scores.

Some are hard eligibility gates.

Therefore:

```text
LAW HIERARCHY
!=
WEIGHTED SCOREBOARD
```

______________________________________________________________________

## 58. No Authority Averaging

Conflicting authority cannot safely be resolved by:

```text
AVERAGE SCORE
MAJORITY VOTE
SOURCE COUNT
POPULARITY
MODEL CONFIDENCE
```

unless an authoritative governance rule explicitly defines that mechanism.

______________________________________________________________________

## 59. Competing Laws

When incompatible rules remain equally supported and equally authoritative:

```text
STATE = COMPETING
```

Required output should preserve:

```text
LAW_A
LAW_B
CONFLICT
MISSING DISCRIMINATOR
```

rather than inventing convergence.

______________________________________________________________________

## 60. Cheapest Discriminator

When conflict is resolvable through additional evidence, seek the cheapest high-information discriminator.

Examples:

```text
CHECK SUPERSESSION RECORD
CHECK CANON SOURCE
CHECK EFFECTIVE DATE
CHECK AUTHORITY SIGNATURE
CHECK SCOPE DECLARATION
CHECK REGIME CONDITION
```

Do not gather redundant evidence if one authoritative check can resolve the conflict.

______________________________________________________________________

## 61. Failure Propagation

If a law used by decision `D` becomes invalid:

```text
LAW_X
↓
DECISION_D
↓
ACTION_A
```

invalidate dependent conclusions/actions according to dependency semantics.

Do not invalidate unrelated branches.

______________________________________________________________________

## 62. Rollback

```text
FAILED LAW PREMISE
↓
LOCATE DEPENDENTS
↓
INVALIDATE DESCENDANTS
↓
RETURN TO NEAREST VALID STATE
↓
RE-RESOLVE LAW SET
↓
REVALIDATE
```

Global rollback is last resort.

______________________________________________________________________

## 63. Persistent Provenance

A resolved law decision should preserve where material:

```yaml
law_resolution:
  resolution_id:

  candidate_laws: []
  applicable_laws: []
  rejected_laws: []

  winning_law:
  precedence_basis:

  conflicts: []
  unresolved: []

  scope:
  regime:
  timestamp:

  provenance:
  authority_source:

  resulting_state:
```

______________________________________________________________________

## 64. Atomicity

If several law-dependent changes form one logical commit:

```text
C1
C2
C3
```

the system must not expose an invalid partial state where atomic semantics require:

```text
ALL
OR
NONE
```

Law resolution therefore integrates with AMOS atomicity and commit semantics.

______________________________________________________________________

## 65. Concurrency

Concurrent rule or policy updates must not silently produce ambiguous authority.

Conceptually:

```text
READ LAW STATE @ EPOCH E
↓
PROPOSE CHANGE
↓
COMPARE / VALIDATE
↓
COMMIT IF AUTHORITY STATE UNCHANGED
```

This aligns with AMOS MVCC/CAS reasoning patterns.

It does not assert that every implementation literally uses a particular database mechanism.

______________________________________________________________________

## 66. Causal Epoch Finality

Where decisions depend on epoch-finalized state:

```text
LAW DECISION @ EPOCH E
```

must not silently incorporate partially finalized state from incompatible epochs.

Finality semantics belong to the relevant state/control/runtime mechanisms.

The law hierarchy must respect them.

______________________________________________________________________

## 67. Law Hierarchy Invariants

```text
LH-01
HIGHER AUTHORITY MUST NOT BE SILENTLY OVERRIDDEN

LH-02
RECENCY MUST NOT IMPLY AUTHORITY

LH-03
SPECIFICITY MUST NOT IMPLY AUTHORITY WITHOUT LICENSE

LH-04
SUPERSESSION MUST BE EXPLICIT

LH-05
SUPERSEDED LAW MUST REMAIN PROVENANCE-RECOVERABLE

LH-06
SCOPE MUST BE CHECKED BEFORE PRECEDENCE

LH-07
REGIME MUST BE CHECKED BEFORE PRECEDENCE

LH-08
TEMPORAL VALIDITY MUST BE CHECKED

LH-09
UNKNOWN PRECEDENCE MUST NOT BECOME PASS

LH-10
EQUAL UNRESOLVED CONFLICT MUST REMAIN VISIBLE

LH-11
MODEL CONFIDENCE MUST NOT CREATE AUTHORITY

LH-12
SOURCE COUNT MUST NOT CREATE AUTHORITY

LH-13
CAPABILITY MUST NOT CREATE AUTHORITY

LH-14
TOOL ACCESS MUST NOT CREATE AUTHORITY

LH-15
PROPOSAL MUST NOT CREATE COMMIT AUTHORITY

LH-16
LOCAL POLICY MUST NOT REWRITE CANON

LH-17
HEURISTICS MUST NOT WEAKEN INTEGRITY

LH-18
FAST PATH MUST NOT BYPASS LOAD-BEARING LAW

LH-19
INVALIDATION MUST FOLLOW DEPENDENCY EDGES

LH-20
AUTHORITY PROVENANCE MUST REMAIN RECOVERABLE
```

______________________________________________________________________

## 68. Core Resolution Laws

```text
APPLICABILITY BEFORE PRECEDENCE

AUTHORITY BEFORE CONVENIENCE

SCOPE BEFORE GENERALIZATION

REGIME BEFORE REUSE

PROVENANCE BEFORE TRUST

SUPERSESSION BEFORE RECENCY

CONFLICT BEFORE FORCED CONVERGENCE

VALIDATION BEFORE PROMOTION

AUTHORIZATION BEFORE COMMIT

INTEGRITY BEFORE OPTIMIZATION
```

______________________________________________________________________

## 69. Failure Modes

```text
AUTHORITY_COLLAPSE
PRECEDENCE_INVERSION
RECENCY_AS_AUTHORITY
SPECIFICITY_AS_AUTHORITY
SILENT_OVERRIDE
FALSE_SUPERSESSION
SUPERSESSION_LINEAGE_BREAK
SCOPE_LEAKAGE
REGIME_LEAKAGE
STALE_LAW_REUSE
UNRESOLVED_CONFLICT_SUPPRESSION
MODEL_AUTHORITY_ESCALATION
CAPABILITY_AUTHORITY_ESCALATION
PROVENANCE_COLLAPSE
FALSE_INDEPENDENCE
INVALID_EXCEPTION
INVALID_OVERRIDE
LOCAL_RULE_ESCALATION
PARTIAL_ATOMIC_COMMIT
UNKNOWN_AS_PASS
```

______________________________________________________________________

## 70. Recovery Semantics

For a hierarchy failure:

```text
DETECT
↓
IDENTIFY AFFECTED LAW
↓
IDENTIFY AUTHORITY SOURCE
↓
TRACE DEPENDENT DECISIONS
↓
INVALIDATE AFFECTED DESCENDANTS
↓
RESTORE LAST VALID AUTHORITY STATE
↓
RE-RUN PRECEDENCE
↓
REVALIDATE
```

Unrelated decisions remain intact where dependency independence is established.

______________________________________________________________________

## 71. Observability

Material law resolutions should expose traceable fields such as:

```text
resolution_id
law_ids
authority_classes
scope
regime
effective_time
supersession_state
conflict_state
precedence_basis
authority_source
decision
commit_state
timestamp
```

But:

```text
TRACE EXISTS
!=
RESOLUTION CORRECT
```

______________________________________________________________________

## 72. Test Requirements

The kernel should eventually test:

```text
HIGHER VS LOWER AUTHORITY
EQUAL AUTHORITY CONFLICT
NON-COMPARABLE LAWS
SCOPE MISMATCH
REGIME MISMATCH
TEMPORAL EXPIRY
FULL SUPERSESSION
PARTIAL SUPERSESSION
INVALID RECENCY OVERRIDE
INVALID SPECIFICITY OVERRIDE
VALID SCOPED EXCEPTION
INVALID EXCEPTION
VALID GOVERNED OVERRIDE
UNAUTHORIZED OVERRIDE
UNKNOWN AUTHORITY
UNKNOWN PROVENANCE
FAST-PATH ESCALATION
DEPENDENCY INVALIDATION
ATOMIC LAW-DEPENDENT COMMIT
CONCURRENT LAW UPDATE
```

______________________________________________________________________

## 73. Negative Tests

```text
NEWER LAW → AUTOMATICALLY HIGHER
MUST FAIL

MORE SPECIFIC → AUTOMATICALLY HIGHER
MUST FAIL

MORE SOURCES → AUTOMATICALLY HIGHER
MUST FAIL

MODEL CONFIDENCE → AUTHORITY
MUST FAIL

CAPABILITY → AUTHORITY
MUST FAIL

TOOL ACCESS → PERMISSION
MUST FAIL

PROPOSAL → COMMIT
MUST FAIL

UNKNOWN PRECEDENCE → PASS
MUST FAIL

SUPERSEDED → DELETE HISTORY
MUST FAIL

OUT-OF-SCOPE HIGHER LAW → SILENT GLOBAL APPLICATION
MUST FAIL

HEURISTIC → OVERRIDE INVARIANT
MUST FAIL
```

______________________________________________________________________

## 74. Lifecycle

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

Each transition is independent.

Therefore:

```text
MODEL != IMPLEMENTED
IMPLEMENTED != TESTED
TESTED != VALIDATED
VALIDATED != AUTHORIZED
```

______________________________________________________________________

## 75. Promotion Gate

Before promotion beyond `AMOS_MODEL`:

```text
[ ] canonical law hierarchy source bound
[ ] authority classes canonically confirmed
[ ] precedence rules canonically confirmed
[ ] scope semantics confirmed
[ ] regime semantics confirmed
[ ] temporal semantics confirmed
[ ] supersession semantics confirmed
[ ] exception semantics confirmed
[ ] override semantics confirmed
[ ] conflict semantics confirmed
[ ] provenance integration verified
[ ] dependency integration verified
[ ] control-plane authority integration verified
[ ] atomicity behavior tested
[ ] concurrent-update behavior tested
[ ] rollback behavior tested
[ ] negative tests passed
[ ] unresolved conflicts registered
```

Until these gates are satisfied:

```text
IMPLEMENTATION_STATUS = UNKNOWN/GAP
```

______________________________________________________________________

## 76. Integrity Note

This artifact replaces an empty repository placeholder with a structured AMOS v4.4-aligned law-hierarchy model.

The AMOS reasoning spine supports the following load-bearing principles:

```text
INTEGRITY PRECEDENCE
TYPED AUTHORITY
SCOPE BOUNDARIES
REGIME BOUNDARIES
PROVENANCE
SUPERSESSION
CONFLICT PRESERVATION
DEPENDENCY-AWARE INVALIDATION
GOVERNED COMMIT
```

However, this document must not fabricate a historical formal specification where source lineage has not yet been bound.

Therefore:

```text
CONCLUSION_CLASS = AMOS_MODEL
```

The corresponding `01_CANON/LAW_HIERARCHY` remains the proper location for authoritative canonical law definitions.

This kernel defines how those laws are interpreted and resolved computationally.

______________________________________________________________________

## 77. RSCF Node

```RSCF-NODE
node_id: AMOS-OS-K-LAW-HIERARCHY
node_type: kernel_governance_contract
domain: AMOS_OS_KERNEL
functional_type: LawHierarchyKernel
lifecycle_stage: Architecture
claim_class: AMOS_MODEL

RSCF-RELATIONS:
  - INDEXED_BY: KERNEL_MAP
  - GOVERNED_BY: AMOS_CORE_LAWS
  - DEFINED_BY: LAW_HIERARCHY
  - CONSTRAINED_BY: INVARIANT_REGISTRY
  - AUTHORITY_GOVERNED_BY: AUTHORITY_CANON
  - PROVENANCE_GOVERNED_BY: CANON_PROVENANCE
  - LINEAGE_TRACKED_BY: SOURCE_LINEAGE
  - SOURCES_REGISTERED_BY: SOURCE_REGISTRY
  - CONFLICTS_TRACKED_BY: CONFLICT_REGISTRY
  - EVOLUTION_TRACKED_BY: SUPERSESSION_LOG
  - SEMANTICS_DEPEND_ON: K_DISTINCTION_RELATION_CONSTRAINT
  - LOGIC_EVALUATED_BY: K_CORE19_LOGIC
  - AUTHORIZED_THROUGH: CONTROL_PLANE_MAP
  - EXECUTED_THROUGH: RUNTIME_MAP
  - STATE_RECORDED_IN: AUTHORITATIVE_STATE
  - VERIFIED_BY: README
```

______________________________________________________________________

## Related

README ·
[[00_ROOT/ARCHITECTURE|ARCHITECTURE]] ·
[[00_ROOT/SYSTEM_MAP|SYSTEM_MAP]] ·
[[00_ROOT/PLACEMENT_RULES|PLACEMENT_RULES]] ·
[[01_CANON/00_INDEX/CANON_MAP|CANON_MAP]] ·
[[01_CANON/01_CORE_LAWS/AMOS_CORE_LAWS|AMOS_CORE_LAWS]] ·
[[01_CANON/01_CORE_LAWS/INVARIANT_REGISTRY|INVARIANT_REGISTRY]] ·
[[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] ·
[[01_CANON/04_INFRASTRUCTURE_CANON/AUTHORITY_CANON|AUTHORITY_CANON]] ·
[[01_CANON/02_UNIVERSE_CANON/HML_CANON|HML_CANON]] ·
[[01_CANON/07_PROVENANCE/CANON_PROVENANCE|CANON_PROVENANCE]] ·
[[01_CANON/07_PROVENANCE/SOURCE_LINEAGE|SOURCE_LINEAGE]] ·
[[01_CANON/07_PROVENANCE/SOURCE_REGISTRY|SOURCE_REGISTRY]] ·
[[01_CANON/08_SUPERSESSION/CONFLICT_REGISTRY|CONFLICT_REGISTRY]] ·
[[01_CANON/08_SUPERSESSION/SUPERSESSION_LOG|SUPERSESSION_LOG]] ·
README ·
[[02_KERNEL/00_INDEX/KERNEL_MAP|KERNEL_MAP]] ·
[[02_KERNEL/01_META_LOGIC/K_CORE19_LOGIC|K_CORE19_LOGIC]] ·
[[02_KERNEL/01_META_LOGIC/K_DISTINCTION_RELATION_CONSTRAINT|K_DISTINCTION_RELATION_CONSTRAINT]] ·
README ·
README ·
README ·
README ·
README ·
README ·
README ·
README ·
README ·
[[03_CONTROL_PLANE/00_INDEX/CONTROL_PLANE_MAP|CONTROL_PLANE_MAP]] ·
[[04_RUNTIME/00_INDEX/RUNTIME_MAP|RUNTIME_MAP]] ·
[[00_ROOT/AUTHORITATIVE_STATE|AUTHORITATIVE_STATE]] ·
README ·
README

```text
```

______________________________________________________________________

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] · [[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

______________________________________________________________________

**MOC:** [[02_KERNEL/01_META_LOGIC/01_META_LOGIC_MOC|01_META_LOGIC_MOC]]
