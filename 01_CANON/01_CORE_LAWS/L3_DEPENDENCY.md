---
title: L3 DEPENDENCY
type: note
tags: [note, 01-core-laws]
---

---title: "AMOS Core Laws — L3 Dependency Laws"
type: document
tags: [note]
---


# L3 Dependency Laws

## 0. Status and Governing Boundary

`L3_DEPENDENCY.md` defines the AMOS OS **L3 Dependency Law family**.

This artifact replaces the former structural placeholder with a substantive dependency contract.

It governs:

- prerequisite relationships;
- load-bearing dependencies;
- dependency graphs;
- dependency closure;
- dependency direction;
- conditional dependencies;
- cross-scale dependencies;
- epistemic dependencies;
- provenance dependencies;
- authority dependencies;
- execution dependencies;
- state dependencies;
- temporal dependencies;
- invalidation propagation;
- dependency repair;
- dependency-aware finalization.

Origin architect / steward:

**Trang Phan**

This specification MUST preserve the distinction between:

```text
SOURCE-DERIVED AMOS RULES
````

and:

```text
AMOS_MODEL FORMALIZATION
```

Generalized graph equations and schemas in this document are formalizations unless a source anchor explicitly establishes otherwise.

---

# 1. Hard Boundaries

```text
RELATION != DEPENDENCY

ASSOCIATION != DEPENDENCY

SEQUENCE != DEPENDENCY

CORRELATION != DEPENDENCY

DEPENDENCY != CAUSATION

PREREQUISITE != CAUSE

INPUT != AUTHORITY

DEPENDENCY != OWNERSHIP

UPSTREAM != SUPERIOR

DOWNSTREAM != SUBORDINATE

REFERENCE != LOAD_BEARING_DEPENDENCY

OPTIONAL != REQUIRED

SOFT_DEPENDENCY != HARD_DEPENDENCY

CONDITIONAL_DEPENDENCY != UNIVERSAL_DEPENDENCY

SHARED_DEPENDENCY != INDEPENDENCE

DEPENDENCY_PATH != PROOF

DEPENDENCY_CLOSURE != EMPIRICAL_VALIDATION

RESOLVED != TRUE

AVAILABLE != VALID

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

---

# 2. Purpose

L3 answers the question:

> **What must remain valid, available, compatible, authorized, or established for a given AMOS object, claim, decision, workflow, state transition, or action to remain admissible?**

AMOS reasoning is not treated as a collection of isolated statements.

It is treated as a structured dependency system.

Conceptually:

```text
PREMISE
   ↓
INTERMEDIATE CLAIM
   ↓
DECISION
   ↓
ACTION
```

If the premise fails, AMOS must determine which downstream objects actually depend upon it.

The governing repair principle is:

```text
INVALIDATE DEPENDENTS

PRESERVE NONDEPENDENTS
```

not:

```text
ONE FAILURE
→
DESTROY EVERYTHING
```

---

# 3. Relationship to Earlier Core Laws

The core-law dependency spine is:

```text
L0 INTEGRITY
      ↓
L1 EPISTEMIC
      ↓
L2 PROVENANCE
      ↓
L3 DEPENDENCY
```

L0 preserves structural distinctions.

L1 determines what epistemic class a claim may occupy.

L2 preserves where evidence and claims came from.

L3 determines what relies on what.

Together:

```text
WHAT IS IT?
    ↓
WHAT DO WE KNOW ABOUT IT?
    ↓
WHERE DID THAT KNOWLEDGE COME FROM?
    ↓
WHAT ELSE DEPENDS ON IT?
```

---

# 4. Core Dependency Principle

The governing principle is:

> **No consequential AMOS conclusion, state transition, or action may be treated as independent of a premise, resource, authority, provenance root, constraint, state object, or subsystem that is materially required for its validity or execution.**

Material dependencies must remain explicit enough to support:

```text
validation

ordering

impact analysis

selective invalidation

repair

rollback

revalidation
```

---

# 5. Dependency Object

A normalized dependency object MAY be represented as:

```yaml
DependencyObject:

  dependency_id: string

  source_object: null

  target_object: null

  dependency_type: null

  direction: null

  strength: null

  load_bearing: null

  condition: null

  scope: {}

  regime: {}

  HML: null

  established_at: null

  valid_from: null

  valid_until: null

  freshness_requirement: null

  provenance: []

  authority_requirement: null

  failure_effect: null

  recovery_rule: null

  status: null

  confidence_ceiling: null
```

This schema is `AMOS_MODEL`.

---

# 6. Dependency Graph

Let:

```text
G_D = (V,E)
```

where:

```text
V = governed AMOS objects
E = typed dependency edges
```

A directed dependency edge:

```text
A → B
```

means:

> `B` depends on `A` under the edge's declared scope, regime, condition, and dependency type.

It does **not** automatically mean:

```text
A causes B
```

or:

```text
A controls B
```

or:

```text
A has authority over B
```

---

# 7. Dependency Direction

AMOS MUST define dependency direction consistently.

For this specification:

```text
A → B
```

means:

```text
B DEPENDS_ON A
```

Therefore:

```text
A = upstream dependency
B = downstream dependent
```

Example:

```text
SOURCE
  ↓
CLAIM
  ↓
DECISION
  ↓
ACTION
```

The action is downstream of the decision.

---

# 8. L3-D001 — Dependency Must Be Typed

A dependency edge must not remain merely:

```text
A related_to B
```

when the relationship affects validity.

It SHOULD identify a type.

Proposed dependency types include:

```text
EPISTEMIC

PROVENANCE

LOGICAL

STRUCTURAL

CAUSAL

TEMPORAL

STATE

RESOURCE

AUTHORITY

POLICY

CONSTRAINT

CAPABILITY

EXECUTION

DATA

SCHEMA

VERSION

INTERFACE

ENVIRONMENT

SECURITY

MEMORY

WORKFLOW

CONTROL_PLANE

HML

CONDITIONAL
```

---

# 9. L3-D002 — Dependency Is Not Causation

From:

```text
B depends_on A
```

AMOS may not infer:

```text
A caused B
```

Dependency may represent:

```text
logical prerequisite

data requirement

authorization requirement

runtime requirement

structural requirement

temporal prerequisite
```

without representing physical or behavioral causation.

---

# 10. L3-D003 — Causal Dependencies Require Causal Evidence

If an edge is classified:

```text
dependency_type = CAUSAL
```

then it becomes subject to the AMOS causal firewall.

Sequence, structural similarity, or co-occurrence alone are insufficient.

---

# 11. L3-D004 — References Are Not Automatically Dependencies

A document may reference another artifact without relying upon it.

Therefore:

```text
REFERENCES(A,B)
```

does not imply:

```text
DEPENDS_ON(A,B)
```

A dependency requires material reliance.

---

# 12. L3-D005 — Load-Bearing Dependencies Must Be Distinguished

Dependencies SHOULD support:

```text
load_bearing = true | false | unknown
```

A load-bearing dependency is one whose failure can invalidate, block, downgrade, or materially alter the dependent object.

---

# 13. L3-D006 — Incidental Relations Must Not Trigger Invalidation

Suppose:

```text
A → B
```

exists only as contextual background.

If:

```text
load_bearing = false
```

then invalidation of `A` must not automatically invalidate `B`.

---

# 14. L3-D007 — Unknown Load-Bearing Status Is a Gap

If AMOS cannot determine whether dependency `A → B` is load-bearing:

```text
load_bearing = UNKNOWN
```

It must not silently assume:

```text
false
```

for consequential reasoning.

---

# 15. Dependency Strength

Proposed classes:

```text
HARD

SOFT

CONDITIONAL

OPTIONAL

UNKNOWN
```

---

# 16. HARD Dependency

A hard dependency means:

```text
¬Valid(A)
⇒
¬Admissible(B)
```

within the applicable scope and regime.

Example:

```text
valid authorization
→
durable commit
```

If authorization is mandatory and absent, the commit cannot proceed.

---

# 17. SOFT Dependency

A soft dependency affects:

```text
quality

confidence

performance

efficiency

interpretability
```

but does not necessarily make the dependent object inadmissible.

---

# 18. CONDITIONAL Dependency

A conditional dependency applies only when predicate `φ` holds.

AMOS MODEL:

```text
A →φ B
```

meaning:

```text
φ = true
⇒
B depends_on A
```

Outside `φ`, the edge may be inactive.

---

# 19. OPTIONAL Dependency

An optional dependency may improve an outcome without being necessary for admissibility.

```text
OPTIONAL
!=
LOAD_BEARING
```

unless explicitly promoted under a particular regime.

---

# 20. UNKNOWN Dependency Strength

When dependency strength cannot be established:

```text
strength = UNKNOWN
```

This must remain visible.

---

# 21. L3-D008 — Dependency Scope Must Be Explicit

A dependency may exist only within a particular:

```text
system

population

environment

scale

workflow

operation

decision

claim

version
```

Therefore:

```text
Dependency(A,B)
```

should be interpreted with:

```text
scope(A→B)
```

where material.

---

# 22. L3-D009 — Dependency Regime Must Be Explicit

A dependency valid under:

```text
R1
```

may disappear or reverse under:

```text
R2
```

Therefore:

```text
dependency edge
+
regime
```

must travel together where regime matters.

---

# 23. L3-D010 — Dependency Time Must Be Explicit

Some dependencies are temporary.

Example:

```text
temporary authority
→
temporary permission
```

A dependency may therefore contain:

```text
valid_from

valid_until
```

or equivalent temporal bounds.

---

# 24. L3-D011 — Dependency Version Must Be Explicit

A component may depend on:

```text
API v3
```

but not:

```text
API v4
```

Therefore:

```text
depends_on(component)
```

without version information may be insufficient.

---

# 25. L3-D012 — Dependencies Must Preserve Provenance

Dependency edges themselves are claims.

Therefore dependency declarations SHOULD preserve:

```text
who asserted the dependency

source

evidence

version

time

scope

regime

validation status
```

L3 therefore depends on L2.

---

# 26. L3-D013 — Dependency Claims Have Epistemic Classes

A dependency may be:

```text
VERIFIED

DERIVED

MODEL

CONDITIONAL

COMPETING

UNKNOWN/GAP
```

Dependency diagrams must not visually imply certainty greater than the evidence supports.

---

# 27. L3-D014 — Dependency Closure Must Precede Consequential Execution

For consequential object `X`, AMOS should resolve the smallest sufficient set of load-bearing dependencies before execution.

Define:

```text
Closure(X)
```

as the recursively required dependency set for `X`.

Conceptually:

```text
Closure(X)
=
DirectDependencies(X)
∪
Closure(DirectDependencies(X))
```

subject to:

```text
scope

regime

conditions

dependency type

load-bearing status
```

This is an `AMOS_MODEL` formalization.

---

# 28. L3-D015 — Dependency Closure Must Be Minimal

AMOS should not expand every reachable edge indiscriminately.

Instead:

```text
RequiredClosure(X)
⊆
ReachableAncestors(X)
```

where `RequiredClosure` contains dependencies capable of changing:

```text
validity

decision

authority

execution

confidence

safety
```

This supports the v4.4 smallest-sufficient-proof principle.

---

# 29. L3-D016 — Nonmaterial Dependencies May Be Deferred

If a dependency cannot alter the current decision:

```text
decision_impact = 0
```

within the declared scope, AMOS may defer its expansion.

This is an efficiency rule.

It does not erase the dependency.

---

# 30. L3-D017 — Unresolved Hard Dependencies Block Finalization

If:

```text
HardDependency(A,B)
```

and:

```text
status(A) = UNKNOWN/GAP
```

then `B` cannot be promoted as if `A` passed.

Conceptually:

```text
UNKNOWN/GAP != PASS
```

---

# 31. L3-D018 — Dependency Failure Propagates Selectively

Core rule:

```text
Invalid(A)
⇒
Invalidate(
  load-bearing descendants of A
)
```

This is selective invalidation.

Not all graph nodes should be recomputed.

---

# 32. L3-D019 — Selective Invalidation Must Follow Dependency Edges

Suppose:

```text
A → B → D

C → E
```

If:

```text
A = INVALID
```

then:

```text
B
D
```

require invalidation or revalidation.

But:

```text
C
E
```

remain unaffected unless another dependency connects them.

---

# 33. L3-D020 — Failure of One Premise Does Not Necessarily Falsify a Conclusion

Suppose:

```text
A → C
B → C
```

and either `A` or `B` independently suffices.

Failure of `A` may leave `C` supported by `B`.

Therefore AMOS must distinguish:

```text
AND dependencies
```

from:

```text
OR dependencies
```

---

# 34. Conjunctive Dependencies

For:

```text
C depends on A AND B
```

AMOS MODEL:

```text
Valid(C)
⇒
Valid(A) ∧ Valid(B)
```

where both are mandatory.

---

# 35. Disjunctive Dependencies

For:

```text
C depends on A OR B
```

AMOS MODEL:

```text
Valid(C)
⇒
Valid(A) ∨ Valid(B)
```

where either dependency path is sufficient.

---

# 36. Threshold Dependencies

Some systems may require:

```text
k of n
```

dependencies.

AMOS MODEL:

```text
Admissible(C)
⇔
Σ_i Pass(D_i) ≥ k
```

only when such a threshold is explicitly defined.

AMOS must not invent `k`.

---

# 37. L3-D021 — Dependency Logic Must Be Preserved

These structures are not equivalent:

```text
A AND B
```

```text
A OR B
```

```text
A THEN B
```

```text
A UNLESS B
```

```text
A IF regime R
```

Dependency normalization must preserve logical structure.

---

# 38. L3-D022 — Dependency Order Must Be Preserved

If:

```text
A
↓
B
↓
C
```

then evaluating `C` before resolving required `A` and `B` may produce premature conclusions.

Execution SHOULD respect prerequisite ordering.

---

# 39. Topological Execution

For an acyclic dependency graph, a valid execution order should place prerequisites before dependents.

Conceptually:

```text
TopoSort(G_D)
```

may determine an admissible order.

This is standard graph formalism applied as an AMOS_MODEL execution rule.

---

# 40. L3-D023 — Cycles Must Be Explicit

If:

```text
A → B
B → A
```

AMOS must not silently treat the graph as acyclic.

The cycle may represent:

```text
feedback

mutual dependency

circular definition

bootstrapping

invalid architecture
```

and requires classification.

---

# 41. L3-D024 — Circular Definition Is Not Automatically Valid Feedback

Example:

```text
A is valid because B is valid
B is valid because A is valid
```

does not create independent justification.

Such a cycle may be epistemically empty.

---

# 42. L3-D025 — Feedback Cycles Require State/Time Semantics

A valid feedback relationship may instead be:

```text
A(t)
→
B(t+1)
→
A(t+2)
```

Temporal indexing can distinguish feedback from circular definition.

---

# 43. L3-D026 — Recursive Dependency Requires a Termination or Fixed-Point Rule

Recursive dependencies must identify:

```text
base condition

termination condition

fixed point

bounded iteration

or explicit nontermination
```

where execution depends on recursion.

---

# 44. L3-D027 — Dependency Graphs Must Distinguish Structural and Runtime Edges

Example:

```text
MODULE A imports MODULE B
```

is structural.

```text
RUN A requires live SERVICE B
```

is runtime.

These dependency classes may differ.

---

# 45. L3-D028 — Declared Dependency and Observed Dependency Are Distinct

A manifest may state:

```text
A depends on B
```

This is:

```text
SOURCE_CLAIM
```

until validated.

Observed runtime behavior may establish:

```text
OBSERVATION
```

Neither should silently replace the other.

---

# 46. L3-D029 — Hidden Dependencies Are Integrity Risks

A hidden dependency exists when object `B` materially relies on `A`, but the edge is absent from the declared graph.

Hidden dependencies can produce:

```text
unexpected failure

invalid rollback

incorrect confidence

false modularity

unsafe deployment
```

---

# 47. L3-D030 — False Dependencies Are Also Risks

An incorrect edge may cause:

```text
unnecessary invalidation

excessive coupling

blocked execution

false authority assumptions

needless recomputation
```

Dependency repair must therefore support both:

```text
ADD MISSING EDGE
```

and:

```text
REMOVE FALSE EDGE
```

---

# 48. Dependency Classes by Domain

## Epistemic

```text
evidence → claim
premise → conclusion
```

## Provenance

```text
root → evidence
source → derived artifact
```

## Authority

```text
authority witness → authorized effect
```

## Policy

```text
policy → policy decision
```

## Execution

```text
runtime → operation
service → workflow step
```

## Data

```text
dataset → model output
```

## State

```text
state version → transition
```

## Constraint

```text
constraint → admissible action
```

## Version

```text
schema version → parser
```

## Temporal

```text
event A must occur before B
```

---

# 49. L3-D031 — Epistemic Dependencies Bound Confidence

If conclusion `C` depends on premises:

```text
P1 ... Pn
```

then:

```text
Conf(C)
≤
min Conf(load-bearing premises)
```

unless the weak premise is independently revalidated through a valid alternative path.

This is a governing AMOS confidence rule.

---

# 50. L3-D032 — Independent Revalidation May Replace a Failed Dependency

Suppose:

```text
P1 → C
```

and `P1` fails.

If independent evidence establishes:

```text
P2 → C
```

then the dependency graph may be repaired:

```text
P1 -X→ C

P2 → C
```

The conclusion requires reclassification, not automatic permanent deletion.

---

# 51. L3-D033 — Alternative Dependency Paths Must Be Genuine

Two paths:

```text
A → B → C

A → D → C
```

do not create two independent roots because both originate at `A`.

Dependency multiplicity is not provenance independence.

---

# 52. L3-D034 — Shared Ancestors Must Be Visible

For:

```text
A → B
A → C
B → D
C → D
```

AMOS should recognize `A` as a shared upstream dependency of `D`.

This matters for:

```text
risk concentration

failure propagation

confidence

repair
```

---

# 53. L3-D035 — Single Points of Failure Must Be Detectable

If many critical descendants depend on one node:

```text
A
├→ B
├→ C
├→ D
├→ E
└→ F
```

then `A` has high dependency fan-out.

This may indicate:

```text
critical dependency

single point of failure

high repair priority
```

but fan-out alone does not establish causal importance.

---

# 54. Dependency Fan-Out

AMOS MODEL:

```text
FanOut(x)
=
|DirectDependents(x)|
```

and optionally:

```text
DescendantImpact(x)
=
|LoadBearingDescendants(x)|
```

These are structural measures.

They are not universal risk equations.

---

# 55. L3-D036 — High Fan-Out Increases Potential Invalidation Surface

All else equal, failure of a node with many load-bearing descendants may create a larger revalidation surface.

Therefore dependency topology may inform:

```text
repair priority

test priority

monitoring priority
```

---

# 56. L3-D037 — Dependency Centrality Is Not Authority

A highly connected node is not automatically:

```text
authoritative

correct

important in every regime

allowed to govern other nodes
```

Topology and authority remain distinct.

---

# 57. L3-D038 — Authority Dependencies Must Be Explicit

An action may require:

```text
capability
+
authority
```

These are separate dependencies.

Example:

```text
ToolAvailable
→ execution capability

AuthorityWitnessValid
→ execution authorization
```

Both may be required.

---

# 58. L3-D039 — Capability Does Not Satisfy Authority Dependency

```text
CanExecute(A)
```

does not imply:

```text
Authorized(A)
```

Therefore:

```text
CAPABILITY != AUTHORITY
```

remains a hard dependency boundary.

---

# 59. L3-D040 — Proposal Does Not Satisfy Commit Dependency

A proposed state transition is not equivalent to a committed transition.

```text
PROPOSAL
→ validation
→ authorization
→ commit
```

must preserve stage dependencies.

---

# 60. L3-D041 — Commit Depends on Fresh Preconditions

Where mutable state is involved, commit may depend on:

```text
current state

current policy

current authority

current constraints

current version
```

not merely values observed earlier.

---

# 61. L3-D042 — Stale Dependencies Must Trigger Revalidation

If:

```text
Dependency(A,B)
```

was established under stale state, AMOS must determine whether it remains valid before consequential finalization.

---

# 62. L3-D043 — Freshness Is Dependency-Specific

Different dependencies may have different freshness requirements.

Example:

```text
historical authorship
```

may be stable.

```text
authorization
```

may require commit-time freshness.

---

# 63. L3-D044 — State Dependencies Require Version Identity

If:

```text
Decision D
```

depends on:

```text
State S_v1
```

and current state becomes:

```text
S_v2
```

AMOS must not silently treat `D` as validated against `S_v2`.

---

# 64. L3-D045 — Mutable Dependencies Need Revalidation Rules

A dependency on mutable object `A` should define:

```text
what change invalidates the edge

what change requires revalidation

what change is irrelevant
```

where consequential.

---

# 65. L3-D046 — Dependency Compatibility Must Be Checked

Two individually valid dependencies may be mutually incompatible.

Example:

```text
A requires schema v1

B requires schema v2
```

Both cannot necessarily be satisfied by one runtime state.

---

# 66. L3-D047 — Dependency Composition Requires Compatibility

Before composing:

```text
A → X

B → X
```

AMOS should check:

```text
scope compatibility

regime compatibility

version compatibility

authority compatibility

temporal compatibility
```

---

# 67. L3-D048 — Dependency Closure Must Preserve Contradictions

If:

```text
A requires X

B forbids X
```

and both are required for `C`, the dependency graph contains a conflict.

AMOS must not silently choose one.

Status:

```text
COMPETING
```

or:

```text
UNKNOWN/GAP
```

until precedence or repair resolves the conflict.

---

# 68. L3-D049 — Dependency Conflicts Require Precedence Rules

Where dependencies arise from:

```text
laws

policies

contracts

constraints

authority
```

conflict resolution requires an explicit precedence mechanism.

Dependency topology alone cannot decide precedence.

---

# 69. L3-D050 — Scope Leakage Through Dependencies Is Forbidden

A valid dependency:

```text
A → B
```

under scope `S1` must not automatically be reused under `S2`.

Applicability must travel with the edge.

---

# 70. L3-D051 — Regime Leakage Through Dependencies Is Forbidden

A dependency valid in:

```text
NORMAL_REGIME
```

may fail in:

```text
STRESS_REGIME
```

or:

```text
RECOVERY_REGIME
```

Therefore regime changes can invalidate dependency edges.

---

# 71. L3-D052 — H/M/L Dependencies Must Preserve Scale

Dependencies may occur:

```text
within scale
```

or:

```text
across scale
```

These must be distinguishable.

---

# 72. H-Scale Dependencies

Examples:

```text
canon → architecture

core law → system governance

root authority → subordinate authority

system invariant → subsystem admissibility
```

---

# 73. M-Scale Dependencies

Examples:

```text
control plane → workflow

Skill → agent operation

memory subsystem → reasoning subsystem

policy engine → action proposal
```

---

# 74. L-Scale Dependencies

Examples:

```text
function → variable

claim → evidence fragment

test → fixture

operation → parameter

file → schema
```

---

# 75. Cross-Scale Dependency

Example:

```text
H invariant
   ↓
M policy
   ↓
L action
```

If the H-level invariant fails or changes, dependent M/L objects may require revalidation.

---

# 76. L3-D053 — Upward Dependency Must Not Be Assumed from Downward Governance

If:

```text
H constrains M
```

it does not automatically mean:

```text
H depends on M
```

Dependency direction must be separately established.

---

# 77. L3-D054 — Local Success Does Not Validate Upstream Architecture

A passing L-level test does not automatically validate:

```text
M subsystem

H architecture

unexercised dependency paths
```

This prevents upward overgeneralization.

---

# 78. L3-D055 — Global Validity Requires Relevant Dependency Coverage

A claim about the entire system requires sufficient coverage of its load-bearing dependency structure.

Passing one local branch is insufficient.

---

# 79. Dependency State Machine

```text
DISCOVERED
    ↓
DECLARED
    ↓
TYPED
    ↓
SCOPED
    ↓
VALIDATED
    ↓
ACTIVE
```

Possible branches:

```text
DECLARED
    ↓
UNKNOWN
```

```text
TYPED
    ↓
CONFLICTING
```

```text
ACTIVE
    ↓
STALE
```

```text
ACTIVE
    ↓
INVALID
```

```text
INVALID
    ↓
REPAIRED
    ↓
REVALIDATED
```

---

# 80. Dependency Status Vocabulary

```text
DISCOVERED

DECLARED

TYPED

VALIDATED

ACTIVE

INACTIVE

CONDITIONAL

UNKNOWN

CONFLICTING

STALE

INVALID

QUARANTINED

REPAIRED

SUPERSEDED
```

---

# 81. Dependency Operators

Proposed operators:

```text
REGISTER_DEPENDENCY

TYPE_DEPENDENCY

SET_DIRECTION

SET_STRENGTH

SET_LOAD_BEARING

SET_CONDITION

SET_SCOPE

SET_REGIME

SET_VERSION

TRACE_UPSTREAM

TRACE_DOWNSTREAM

COMPUTE_CLOSURE

COMPUTE_MINIMAL_CLOSURE

DETECT_CYCLE

DETECT_CONFLICT

DETECT_SHARED_ANCESTOR

DETECT_SINGLE_POINT_OF_FAILURE

INVALIDATE_EDGE

INVALIDATE_DESCENDANTS

REVALIDATE_EDGE

REPAIR_DEPENDENCY

REMOVE_FALSE_DEPENDENCY

ADD_MISSING_DEPENDENCY
```

---

# 82. Control-Plane Requirements

A runtime enforcing L3 SHOULD eventually support:

```text
typed dependency registry

directed dependency graph

conditional edges

load-bearing flags

scope/regime envelopes

version bindings

freshness requirements

dependency closure

cycle detection

conflict detection

selective invalidation

revalidation

dependency impact analysis

rollback-aware lineage
```

This specification does not claim all of these mechanisms currently exist in production.

---

# 83. Agents

Potential dependency-oriented roles include:

```text
DEPENDENCY_MAPPER

DEPENDENCY_AUDITOR

CLOSURE_RESOLVER

IMPACT_ANALYST

CYCLE_DETECTOR

CONFLICT_ANALYST

REVALIDATION_AGENT

REPAIR_AGENT

RSCF_DEPENDENCY_AUDITOR
```

Agent capability does not grant execution or canon authority.

---

# 84. Skills

Relevant AMOS capabilities may include:

```text
AMOS OS kernel

RSCF modeling

constraint propagation

provenance analysis

claim verification

system completion auditing

causal hierarchy analysis

control-plane governance

repair allocation

repository dependency analysis

context continuity
```

Dependency results inherited from Skills retain their own evidence and provenance status.

---

# 85. Workflow — Dependency Registration

```text
OBJECT IDENTIFIED
      ↓
IDENTIFY MATERIAL REQUIREMENTS
      ↓
CREATE DEPENDENCY EDGES
      ↓
TYPE EACH EDGE
      ↓
SET DIRECTION
      ↓
SET LOAD-BEARING STATUS
      ↓
SET CONDITION
      ↓
SET SCOPE / REGIME
      ↓
ATTACH PROVENANCE
      ↓
VALIDATE
      ↓
REGISTER
```

---

# 86. Workflow — Dependency Closure

```text
TARGET X
   ↓
DIRECT DEPENDENCIES
   ↓
LOAD-BEARING FILTER
   ↓
CONDITIONAL EDGE FILTER
   ↓
SCOPE / REGIME FILTER
   ↓
RECURSIVE UPSTREAM TRAVERSAL
   ↓
CONFLICT CHECK
   ↓
CYCLE CHECK
   ↓
MINIMAL REQUIRED CLOSURE
```

---

# 87. Workflow — Pre-Execution Dependency Gate

```text
PROPOSED ACTION
      ↓
RESOLVE HARD DEPENDENCIES
      ↓
CHECK STATE
      ↓
CHECK AUTHORITY
      ↓
CHECK POLICY
      ↓
CHECK CONSTRAINTS
      ↓
CHECK CAPABILITY
      ↓
CHECK VERSION
      ↓
CHECK FRESHNESS
      ↓
CHECK CONFLICTS
      ↓
PASS / BLOCK / ESCALATE
```

---

# 88. Workflow — Dependency Failure

```text
DEPENDENCY FAILURE
      ↓
IDENTIFY FAILED NODE / EDGE
      ↓
DETERMINE LOAD-BEARING STATUS
      ↓
TRACE DEPENDENTS
      ↓
CHECK ALTERNATIVE SUPPORT PATHS
      ↓
SELECTIVE INVALIDATION
      ↓
REPAIR / REPLACE / REMOVE EDGE
      ↓
REVALIDATE DESCENDANTS
```

---

# 89. Workflow — Dependency Repair

```text
FAILURE
  ↓
LOCATE EARLIEST INVALID DEPENDENCY
  ↓
CLASSIFY FAILURE
  ↓
PRESERVE UNAFFECTED GRAPH
  ↓
RECOVER MISSING PREREQUISITE
  OR
REPLACE FAILED PREREQUISITE
  OR
REMOVE FALSE DEPENDENCY
  OR
ADD MISSING DEPENDENCY
  ↓
RECOMPUTE MINIMAL CLOSURE
  ↓
REVALIDATE
```

---

# 90. Workflow — Cycle Audit

```text
DEPENDENCY GRAPH
      ↓
DETECT CYCLE
      ↓
CLASSIFY:

  VALID FEEDBACK?
  TEMPORAL LOOP?
  BOOTSTRAP?
  CIRCULAR DEFINITION?
  ERROR?

      ↓
ADD TIME / STATE SEMANTICS
OR
BREAK INVALID CYCLE
OR
PRESERVE EXPLICIT FEEDBACK
```

---

# 91. Protocol — Dependency Registration

```yaml
dependency_registration:

  dependency_id: null

  upstream: null

  downstream: null

  type: null

  strength:
    - HARD
    - SOFT
    - CONDITIONAL
    - OPTIONAL
    - UNKNOWN

  load_bearing:
    - true
    - false
    - unknown

  condition: null

  scope: {}

  regime: {}

  version: null

  freshness: null

  provenance: []

  status: null
```

---

# 92. Protocol — Dependency Closure Request

```yaml
dependency_closure_request:

  target: null

  include_types: []

  include_soft: false

  scope: {}

  regime: {}

  time: null

  version: null

  stop_at_validated_roots: true

  require_load_bearing_resolution: true
```

---

# 93. Protocol — Dependency Failure Event

```yaml
dependency_failure:

  failed_object: null

  failed_edge: null

  failure_type: null

  detected_at: null

  scope: {}

  regime: {}

  direct_dependents: []

  load_bearing_descendants: []

  alternative_paths: []

  invalidated: []

  preserved: []

  revalidation_required: []
```

---

# 94. Protocol — Dependency Repair

```yaml
dependency_repair:

  target: null

  failure: null

  repair_type:
    - RESTORE
    - REPLACE
    - REMOVE_FALSE_EDGE
    - ADD_MISSING_EDGE
    - RECLASSIFY
    - RESCOPE
    - REREGIME
    - REVERSION
    - QUARANTINE

  old_state: null

  proposed_state: null

  affected_descendants: []

  validation_required: []

  rollback_point: null
```

---

# 95. Dependency Invariants

```text
L3-INV001
Material dependencies must be explicit or marked UNKNOWN/GAP.

L3-INV002
Dependency direction must be unambiguous.

L3-INV003
Dependency must not be treated as causation without causal evidence.

L3-INV004
References must not automatically become dependencies.

L3-INV005
Load-bearing and incidental dependencies must remain distinct.

L3-INV006
Hard and soft dependencies must remain distinct.

L3-INV007
Conditional dependencies must preserve their predicates.

L3-INV008
Dependency scope must travel with the edge.

L3-INV009
Dependency regime must travel with the edge.

L3-INV010
Mutable dependency versions must remain identifiable.

L3-INV011
Unresolved hard dependencies cannot silently pass.

L3-INV012
Dependency failure invalidates only load-bearing descendants.

L3-INV013
Independent alternative support must be preserved.

L3-INV014
Dependency multiplicity does not prove provenance independence.

L3-INV015
Cycles must remain visible.

L3-INV016
Circular definitions do not self-validate.

L3-INV017
Capability dependencies do not satisfy authority dependencies.

L3-INV018
Proposal does not satisfy commit.

L3-INV019
Stale mutable dependencies require revalidation.

L3-INV020
Dependency conflicts must remain visible until resolved.

L3-INV021
Cross-scale dependency translation must preserve scale.

L3-INV022
Local validation does not automatically validate upstream architecture.

L3-INV023
Dependency graph changes require downstream impact analysis.

L3-INV024
Rollback must preserve dependency failure history.

L3-INV025
Optimization may not erase load-bearing dependency edges.
```

---

# 96. Failure Modes

```text
L3-FM001
Missing dependency.

L3-FM002
False dependency.

L3-FM003
Dependency direction reversed.

L3-FM004
Soft dependency treated as hard.

L3-FM005
Hard dependency treated as optional.

L3-FM006
Conditional dependency treated as universal.

L3-FM007
Reference treated as dependency.

L3-FM008
Dependency treated as causation.

L3-FM009
Unknown dependency treated as resolved.

L3-FM010
Unresolved hard dependency treated as pass.

L3-FM011
Scope lost.

L3-FM012
Regime lost.

L3-FM013
Version lost.

L3-FM014
Freshness ignored.

L3-FM015
Cycle hidden.
```

---

# 97. Extended Failure Modes

```text
L3-FM016
Circular definition treated as proof.

L3-FM017
Shared upstream dependency mistaken for independent support.

L3-FM018
Failure causes global invalidation instead of selective invalidation.

L3-FM019
Dependent descendants remain trusted after load-bearing premise failure.

L3-FM020
Independent descendants invalidated unnecessarily.

L3-FM021
Alternative support path ignored.

L3-FM022
Authority dependency omitted.

L3-FM023
Capability substituted for authority.

L3-FM024
Proposal substituted for commit.

L3-FM025
Old state substituted for current state.

L3-FM026
Incompatible dependencies composed.

L3-FM027
Dependency conflict silently resolved.

L3-FM028
H-level dependency incorrectly inferred from L-level success.

L3-FM029
Dependency graph compressed until critical edges disappear.

L3-FM030
Repair changes dependency structure without revalidation.
```

---

# 98. Repair / Recovery Principles

Dependency repair MUST favor local correction.

Conceptually:

```text
FAILED EDGE
    ↓
DEPENDENT SUBGRAPH
```

should be repaired without unnecessarily recomputing:

```text
ENTIRE SYSTEM
```

where dependency isolation is valid.

Required sequence:

```text
IDENTIFY FAILURE

CLASSIFY EDGE

CHECK LOAD-BEARING STATUS

TRACE DESCENDANTS

CHECK ALTERNATIVES

QUARANTINE AFFECTED SUBGRAPH

REPAIR EARLIEST INVALID EDGE

RECOMPUTE CLOSURE

REVALIDATE DESCENDANTS

PRESERVE UNAFFECTED STATE
```

---

# 99. Selective Invalidation Rule

AMOS MODEL:

```text
Invalid(x)
⇒
∀y ∈ LBDescendants(x):
    Revalidate(y)
```

where:

```text
LBDescendants(x)
```

means load-bearing descendants of `x`.

This equation is a formalized dependency rule, not an empirical theorem.

---

# 100. Dependency Confidence Rule

For conclusion `C`:

```text
Conf(C)
≤
min {
  Conf(p)
  |
  p ∈ LoadBearingPremises(C)
}
```

unless a weaker premise is replaced or independently revalidated.

This prevents downstream confidence amplification unsupported by the dependency graph.

---

# 101. Dependency Sufficiency

AMOS may consider a dependency set sufficient when:

```text
all hard dependencies resolved
AND
all active conditions evaluated
AND
no unresolved load-bearing conflict
AND
scope compatible
AND
regime compatible
AND
required freshness satisfied
AND
required authority satisfied
```

This is:

```text
DEPENDENCY SUFFICIENCY
```

not universal truth.

---

# 102. Tests

## L3-T001 — Hard Dependency Failure

Input:

```text
A HARD→ B

A = INVALID
```

Expected:

```text
B cannot remain PASS without alternative support.
```

---

## L3-T002 — Soft Dependency Failure

Input:

```text
A SOFT→ B

A = INVALID
```

Expected:

```text
B requires downgrade/reassessment according to the declared edge semantics,
not automatic invalidation.
```

---

## L3-T003 — Conditional Dependency

Input:

```text
A →φ B

φ = false
```

Expected:

```text
A is not active as a dependency of B under the current condition.
```

---

## L3-T004 — Selective Invalidation

Input:

```text
A → B → C

D → E
```

Invalidate `A`.

Expected:

```text
B = REVALIDATE
C = REVALIDATE

D = UNCHANGED
E = UNCHANGED
```

---

## L3-T005 — Alternative Path

Input:

```text
A → C
B → C
```

where either independently suffices.

Invalidate `A`.

Expected:

```text
C requires reassessment against B.

C != automatically INVALID.
```

---

## L3-T006 — Shared Root Path

Input:

```text
A → B → D
A → C → D
```

Expected:

```text
B-path and C-path do not constitute two independent root supports.
```

---

## L3-T007 — Dependency Cycle

Input:

```text
A → B
B → A
```

Expected:

```text
cycle detected
classification required
```

not silent topological execution.

---

## L3-T008 — Temporal Feedback

Input:

```text
A(t) → B(t+1)
B(t+1) → A(t+2)
```

Expected:

```text
feedback may be represented without treating it as same-state circular proof.
```

---

## L3-T009 — Authority Dependency

Input:

```text
capability = true
authority = false
```

Expected:

```text
execution blocked where authority is hard-required.
```

---

## L3-T010 — Stale State Dependency

Input:

```text
Decision D depends on State v1.

Current State = v2.
```

Expected:

```text
D requires dependency freshness/revalidation before consequential commit.
```

---

# 103. Extended Validators

```text
validate_dependency_identity()

validate_dependency_direction()

validate_dependency_type()

validate_dependency_strength()

validate_load_bearing_status()

validate_dependency_condition()

validate_dependency_scope()

validate_dependency_regime()

validate_dependency_version()

validate_dependency_freshness()

validate_dependency_provenance()

validate_dependency_closure()

validate_minimal_dependency_closure()

validate_cycle_state()

validate_dependency_conflicts()

validate_alternative_paths()

validate_selective_invalidation()

validate_HML_dependency_mapping()

validate_authority_dependency()

validate_commit_dependencies()

validate_rscf_dependency_graph()
```

These are required validation surfaces, not claims of existing executable implementations.

---

# 104. Falsifiers

This specification must be revised if authoritative AMOS canon establishes that:

```text
dependency closure is unnecessary before consequential execution;

failed premises should invalidate unrelated system state;

unknown hard dependencies may count as passed;

capability implies authority;

proposal implies commit;

dependency edges do not carry scope/regime;

or dependency history may be erased during repair.
```

The generalized equations must also be revised if source canon establishes materially different dependency semantics.

---

# 105. Dependencies of L3 Itself

```yaml
dependencies:

  hard:
    - "L0_INTEGRITY"
    - "L1_EPISTEMIC"
    - "L2_PROVENANCE"

  architectural:
    - "CORE_LAWS_CANON_CORE_LAWS_CONTRACT"
    - "CORE_LAWS_MAP"
    - "CANON_CONTRACT"
    - "00_ROOT"

  conceptual:
    - "RSCF"
    - "HML"
    - "SCOPE"
    - "REGIME"
    - "FRESHNESS"
    - "CONSTRAINTS"
    - "AUTHORITY"
    - "STATE"
    - "VERSIONING"
    - "INVALIDATION"
    - "REPAIR"
```

---

# 106. Evidence / Provenance

```yaml
provenance:

  origin_architect: "Trang Phan"

  steward: "Trang Phan"

  artifact:
    path: "01_CANON/01_CORE_LAWS/L3_DEPENDENCY.md"

  source_alignment:

    supported_runtime_patterns:
      - "dependency closure before execution"
      - "invalidate only dependent descendants"
      - "confidence bounded by weakest unresolved load-bearing premise"
      - "capability does not imply authority"
      - "rollback does not erase failure memory"
      - "optimization may not weaken integrity"

  formalization:

    class: "AMOS_MODEL"

    includes:
      - "dependency graph G_D=(V,E)"
      - "minimal dependency closure"
      - "hard/soft/conditional/optional taxonomy"
      - "load-bearing descendant model"
      - "dependency protocols"
      - "dependency state machine"
      - "H/M/L dependency mapping"

  final_canon_approval:
    status: "UNKNOWN/GAP"
```

---

# 107. Source / Model Firewall

```text
SOURCE-ALIGNED AMOS RUNTIME PRINCIPLES:

- build dependency closure before execution;
- invalidate only dependent descendants;
- confidence cannot exceed weakest unresolved load-bearing premise
  unless independently revalidated;
- capability does not imply authority;
- rollback does not erase failure memory;
- optimization may not weaken integrity.


AMOS_MODEL FORMALIZATIONS:

G_D = (V,E)

Closure(X)
=
DirectDependencies(X)
∪
Closure(DirectDependencies(X))

Invalid(x)
⇒
∀y ∈ LBDescendants(x):
    Revalidate(y)

Conf(C)
≤
min Conf(LoadBearingPremises(C))

FanOut(x)
=
|DirectDependents(x)|
```

The formalizations MUST NOT be presented as recovered canonical equations unless source evidence establishes them.

---

# 108. Equation Registry Relationship

Existing AMOS equation material contains broader dependency-relevant structures including recursive state transitions, constraint propagation, H/M/L decomposition, and survival/selection conditions. These provide architectural context but do not by themselves establish the exact canonical L3 dependency-law inventory.

Therefore:

```text
EQUATION COMPATIBILITY
!=
CANONICAL L3 SOURCE RECOVERY
```

---

# 109. Uncertainty Vector

```yaml
uncertainty:

  dependency_closure_runtime_principle:
    state: "LOW"

  selective_invalidation_principle:
    state: "LOW"

  load_bearing_confidence_ceiling:
    state: "LOW"

  capability_authority_distinction:
    state: "LOW"

  complete_original_L3_law_inventory:
    state: "HIGH"

  canonical_L3_numbering:
    state: "HIGH"

  canonical_dependency_taxonomy:
    state: "HIGH"

  canonical_dependency_graph_equation:
    state: "HIGH"

  canonical_HML_dependency_contract:
    state: "HIGH"

  exact_runtime_implementation:
    state: "UNKNOWN"

  empirical_validation:
    state: "NOT_CLAIMED"
```

---

# 110. Confidence Ceiling

```yaml
confidence_ceiling:

  source_aligned_runtime_principles:
    class: "SOURCE_DERIVED / SOURCE_ALIGNED"

  generalized_dependency_architecture:
    class: "AMOS_MODEL"

  final_canonical_L3_specification:
    value: 0

  implementation:
    value: 0

  runtime_validation:
    value: 0

  empirical_universality:
    value: 0
```

---

# 111. Gap Matrix

```yaml
gap_matrix:

  authoritative_full_L3_source:
    status: "UNKNOWN/GAP"
    severity: "CRITICAL_FOR_FINAL_CANON"

  dependency_closure_principle:
    status: "SOURCE_ALIGNED"

  selective_invalidation_principle:
    status: "SOURCE_ALIGNED"

  load_bearing_dependency_principle:
    status: "SOURCE_ALIGNED"

  complete_canonical_L3_law_inventory:
    status: "UNKNOWN/GAP"
    severity: "CRITICAL"

  canonical_dependency_taxonomy:
    status: "UNKNOWN/GAP"

  canonical_dependency_equations:
    status: "UNKNOWN/GAP"

  canonical_cycle_semantics:
    status: "UNKNOWN/GAP"

  canonical_HML_dependency_mapping:
    status: "UNKNOWN/GAP"

  executable_dependency_registry:
    status: "UNKNOWN/GAP"

  executable_validators:
    status: "UNKNOWN/GAP"

  executed_L3_test_suite:
    status: "UNKNOWN/GAP"

  production_validation:
    status: "UNKNOWN/GAP"

  final_canon_approval:
    status: "UNKNOWN/GAP"
    severity: "CRITICAL"
```

---

# 112. Promotion Requirements

Promotion beyond the present status requires recovery or explicit approval of:

```text
AUTHORITATIVE L3 SOURCE MATERIAL

CANONICAL DEPENDENCY LAW INVENTORY

CANONICAL DEPENDENCY TYPES

CANONICAL EDGE DIRECTION

CANONICAL LOAD-BEARING SEMANTICS

CANONICAL CLOSURE RULES

CANONICAL CYCLE RULES

CANONICAL INVALIDATION RULES

CANONICAL REVALIDATION RULES

CANONICAL H/M/L MAPPING

CONTROL-PLANE OWNERSHIP

EXECUTABLE TEST CONTRACT

VERSION / SUPERSESSION LINEAGE

CANON AUTHORITY
```

---

# 113. Promotion Ladder

Canonical lifecycle:

```text
PLACEHOLDER
    ↓
PROPOSED_SPECIFICATION
    ↓
PARTIAL_SOURCE_ALIGNMENT
    ↓
SOURCE_ALIGNED
    ↓
CANON_REVIEWED
    ↓
CANON_APPROVED
    ↓
REGISTERED
```

Implementation lifecycle:

```text
NOT_IMPLEMENTED
    ↓
IMPLEMENTATION_PROPOSED
    ↓
IMPLEMENTED
    ↓
TESTED
    ↓
VALIDATED
    ↓
RUNTIME_ACTIVE
```

These lifecycles remain independent.

---

# 114. L3 RSCF

```yaml
rscf:

  claim:

    id: "l3_dependency"

    class: "AMOS_MODEL"

    statement: >
      AMOS reasoning, governance, and execution require explicit typed
      dependency structures so that load-bearing prerequisites can be
      resolved before consequential execution, confidence can remain
      bounded by required premises, and failures can propagate selectively
      only to dependent descendants.

  source_aligned_claims:

    - claim:
        "Dependency closure should be established before consequential execution."

      class:
        "SOURCE_ALIGNED"

    - claim:
        "Invalidation should affect dependent descendants rather than unrelated state."

      class:
        "SOURCE_ALIGNED"

    - claim:
        "Confidence cannot exceed the weakest unresolved load-bearing premise unless independently revalidated."

      class:
        "SOURCE_ALIGNED"

    - claim:
        "Capability does not imply authority."

      class:
        "SOURCE_ALIGNED"

  premises:

    - "conclusions can depend on upstream premises"

    - "dependencies differ in type and strength"

    - "some dependencies are load-bearing"

    - "dependency validity can vary by scope, regime, time and version"

    - "dependency failure can invalidate downstream conclusions"

    - "unrelated state should survive local dependency failure"

  evidence:
    - "AMOS OS kernel dependency-closure and selective-invalidation rules"

  provenance:
    origin_architect: "Trang Phan"
    source_family: "AMOS OS / AMOS_CORE lineage"
    artifact: "01_CANON/01_CORE_LAWS/L3_DEPENDENCY.md"

  scope:
    system: "AMOS OS"
    layer: "CORE LAWS"
    family: "L3_DEPENDENCY"

  regime:
    - "ARCHITECTURE"
    - "REASONING"
    - "CONTROL_PLANE"
    - "AMOS_MODEL"

  freshness:
    updated: "2026-08-26"

  dependencies:
    - "L0_INTEGRITY"
    - "L1_EPISTEMIC"
    - "L2_PROVENANCE"
    - "CORE_LAWS_CANON_CORE_LAWS_CONTRACT"
    - "CORE_LAWS_MAP"

  competing:

    - id: "FLAT_REASONING"

      statement: >
        Claims can be evaluated independently without tracking
        upstream dependencies.

      status: "REJECTED_FOR_AMOS_MODEL"

    - id: "GLOBAL_INVALIDATION"

      statement: >
        Failure of any important premise should invalidate the
        entire reasoning state.

      status: "REJECTED"

    - id: "DEPENDENCY_EQUALS_CAUSATION"

      statement: >
        Every dependency edge represents a causal relationship.

      status: "REJECTED"

    - id: "CAPABILITY_EQUALS_AUTHORITY"

      statement: >
        A component able to execute an operation is thereby
        authorized to execute it.

      status: "REJECTED"

  falsifiers:

    - "authoritative AMOS canon establishes incompatible dependency rules"

    - "higher valid canon supersedes this specification"

    - "source recovery establishes materially different L3 semantics"

  confidence_ceiling:

    source_aligned_subset:
      class: "SOURCE_ALIGNED"

    generalized_specification:
      class: "AMOS_MODEL"

    final_canon:
      value: 0
```

---

# 115. Current Completion State

```yaml
completion:

  artifact:
    name: "L3_DEPENDENCY.md"

  placeholder:
    status: false

  substantive_content:
    status: "PRESENT"

  specification:
    status: "COMPLETE_FOR_DECLARED_MODEL_SCOPE"

  epistemic_class:
    status: "AMOS_MODEL"

  source_alignment:
    status: "PARTIAL_SOURCE_ALIGNMENT"

  final_canon:
    status: "UNKNOWN/GAP"

  implementation:
    status: "NOT_ESTABLISHED"

  runtime_enforcement:
    status: "NOT_ESTABLISHED"

  executable_validation:
    status: "NOT_ESTABLISHED"
```

---

# 116. Final L3 Dependency Contract

> **AMOS must know what depends on what before it treats a conclusion, decision, transition, or action as sufficiently grounded. Dependencies must be typed, directional, scoped, regime-aware, version-aware, provenance-bound, and classified by whether they are load-bearing. Dependency is not causation, reference is not dependency, capability is not authority, and proposal is not commit. Consequential execution requires the smallest sufficient closure of active hard dependencies. When a dependency fails, AMOS invalidates or revalidates only the descendants that materially rely upon it, preserves independent support and unrelated state, repairs the earliest invalid dependency where possible, and never converts UNKNOWN/GAP into PASS.**

Compressed L3 law:

```text
IDENTIFY THE TARGET

IDENTIFY ITS PREREQUISITES

TYPE THE DEPENDENCIES

SET THEIR DIRECTION

DISTINGUISH HARD FROM SOFT

DISTINGUISH LOAD-BEARING FROM INCIDENTAL

PRESERVE CONDITIONS

PRESERVE SCOPE

PRESERVE REGIME

PRESERVE TIME

PRESERVE VERSION

PRESERVE PROVENANCE

RESOLVE THE MINIMUM REQUIRED CLOSURE

DETECT CYCLES

DETECT CONFLICTS

DO NOT CONFUSE DEPENDENCY WITH CAUSATION

DO NOT CONFUSE REFERENCE WITH DEPENDENCY

DO NOT CONFUSE CAPABILITY WITH AUTHORITY

DO NOT CONFUSE PROPOSAL WITH COMMIT

DO NOT LET UNKNOWN HARD DEPENDENCIES PASS

BOUND CONFIDENCE BY LOAD-BEARING PREMISES

INVALIDATE DEPENDENT DESCENDANTS ONLY

PRESERVE INDEPENDENT SUPPORT

REPAIR THE EARLIEST FAILED DEPENDENCY

REVALIDATE WHAT ACTUALLY CHANGED
```

---

00_ROOT_MOC|AMOS MOC

---

**Related:** [[00_HOME]] · AMOS_RSCF_NODES · L0_INTEGRITY · L1_EPISTEMIC · L2_PROVENANCE · CORE_LAWS_MAP · CORE_LAWS_CANON_CORE_LAWS_CONTRACT

---

RSCF-NODE

node_id: l3_dependency

node_type: core_law_family

path: 01_CANON/01_CORE_LAWS/L3_DEPENDENCY.md

origin_architect: Trang Phan

artifact_status: PROPOSED_SOURCE_ALIGNED_SPECIFICATION

canonical_status: PARTIAL_SOURCE_ALIGNMENT

RSCF-RELATIONS:

* INDEXED_BY: [[00_HOME]]

* INDEXED_BY: AMOS_RSCF_NODES

* GOVERNED_BY: CORE_LAWS_CANON_CORE_LAWS_CONTRACT

* MAPPED_BY: CORE_LAWS_MAP

* DEPENDS_ON: L0_INTEGRITY

* DEPENDS_ON: L1_EPISTEMIC

* DEPENDS_ON: L2_PROVENANCE

* DEPENDS_ON: [[00_ROOT_MOC]]

* BELONGS_TO: 01_CANON/01_CORE_LAWS

claim_class: AMOS_MODEL

source_alignment: PARTIAL

final_canon_confidence_ceiling: 0

```
```

---
**MOC:** [[01_CORE_LAWS_MOC]]