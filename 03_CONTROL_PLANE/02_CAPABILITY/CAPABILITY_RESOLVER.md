---
canon-group: meta
canon-type: framework
rscf-state: source-claim
topic: Capability Resolver
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---

# CAPABILITY RESOLVER

The current Drive artifact `CAPABILITY_RESOLVER.md` is **not substantive canon**. It contains the same misplaced `# K COUNTERFACTUAL` placeholder and explicitly says it is only reserving the canonical location. The architecture tree places it with `CAPABILITY_CONTRACT.md` and `CAPABILITY_MANIFEST.md` in the Capability subsystem.

So the following is a **substantive candidate replacement**, not recovered pre-existing content.

______________________________________________________________________

artifact_id: AMOS-OS-CP-CAPABILITY-RESOLVER
title: AMOS OS Capability Resolver
canonical_name: CAPABILITY_RESOLVER

artifact_class: CONTROL_PLANE_RESOLVER
plane: CONTROL_PLANE
subsystem: CAPABILITY
canonical_location: 03_CONTROL_PLANE/02_CAPABILITY/CAPABILITY_RESOLVER.md

origin_architect: Trang Phan
amos_core_target: v4.4

status: CANDIDATE_CANON
conclusion_class: DERIVED

parent:

- 03_CONTROL_PLANE/02_CAPABILITY

siblings:

- CAPABILITY_CONTRACT.md
- [[03_CONTROL_PLANE/02_CAPABILITY/CAPABILITY_MANIFEST|CAPABILITY_MANIFEST]].md

upstream:

- 00_ROOT
- 01_CANON
- 02_KERNEL
- 03_CONTROL_PLANE/00_INDEX
- 03_CONTROL_PLANE/01_TASK_CONTRACT
- 03_CONTROL_PLANE/02_CAPABILITY/[[03_CONTROL_PLANE/02_CAPABILITY/CAPABILITY_MANIFEST|CAPABILITY_MANIFEST]].md
- 03_CONTROL_PLANE/02_CAPABILITY/CAPABILITY_CONTRACT.md

downstream:

- 03_CONTROL_PLANE/03_POLICY
- 03_CONTROL_PLANE/04_AUTHORITY
- 03_CONTROL_PLANE/05_PROVENANCE
- 03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION
- 03_CONTROL_PLANE/07_OBSERVABILITY
- 03_CONTROL_PLANE/08_EFFECTS
- 03_CONTROL_PLANE/09_COMMIT
- 04_RUNTIME

implementation_status: SPECIFICATION
empirical_validation_status: NOT_CLAIMED
formal_verification_status: NOT_CLAIMED

## updated: 2026-08-26

## AMOS OS — CAPABILITY RESOLVER

> **Layer:** `03_CONTROL_PLANE/02_CAPABILITY`
>
> **Artifact:** `CAPABILITY_RESOLVER.md`
>
> **Status:** `CANDIDATE_CANON`
>
> **AMOS CORE target:** `v4.4`
>
> **Origin Architect:** Trang Phan

______________________________________________________________________

## 0. Purpose

The Capability Resolver determines whether a resolved AMOS task can be
satisfied using the capabilities that are actually available, applicable,
sufficient, fresh, compatible, and governable in the current execution
context.

Conceptually:

```text
TASK CONTRACT
    ↓
CAPABILITY RESOLVER
    ↓
CAPABILITY PLAN
```

Its responsibility is not merely:

```text
DOES A TOOL EXIST?
```

Its responsibility is to determine:

```text
WHAT CAPABILITY DOES THE TASK REQUIRE?

WHICH AVAILABLE CAPABILITIES COULD SATISFY IT?

ARE THEY ACTUALLY ACCESSIBLE?

DO THEIR INPUT/OUTPUT CONTRACTS MATCH?

DO THEY APPLY IN THE CURRENT ENVIRONMENT?

ARE THEY FRESH ENOUGH?

ARE THEIR LIMITS COMPATIBLE WITH THE TASK?

DO THEY REQUIRE OTHER CAPABILITIES?

DO THEY CREATE EFFECTS?

CAN THE REQUIRED CAPABILITY COMPOSITION BE EXECUTED?

WHAT REMAINS UNKNOWN?

WHAT MUST BE GOVERNED DOWNSTREAM?
```

The Capability Resolver is therefore the Control Plane boundary between:

```text
SEMANTICALLY RESOLVED WORK
```

and:

```text
EXECUTIONALLY REALIZABLE WORK
```

______________________________________________________________________

## 1. Core Law

```text
DO NOT EQUATE
A REQUESTED OPERATION
WITH
AN AVAILABLE CAPABILITY.
```

Expanded:

```text
TASK CONTRACT
    ↓
DERIVE REQUIREMENTS
    ↓
DISCOVER CANDIDATES
    ↓
VALIDATE AVAILABILITY
    ↓
VALIDATE COMPATIBILITY
    ↓
VALIDATE SCOPE / REGIME
    ↓
VALIDATE FRESHNESS
    ↓
RESOLVE DEPENDENCIES
    ↓
ASSESS EFFECTS
    ↓
TEST SUFFICIENCY
    ↓
CAPABILITY PLAN
```

______________________________________________________________________

## 2. Fundamental Distinctions

```text
TASK REQUIREMENT
!=
CAPABILITY
```

```text
CAPABILITY DECLARATION
!=
CAPABILITY AVAILABILITY
```

```text
CAPABILITY AVAILABILITY
!=
CAPABILITY SUFFICIENCY
```

```text
CAPABILITY SUFFICIENCY
!=
POLICY PERMISSION
```

```text
CAPABILITY SUFFICIENCY
!=
AUTHORITY
```

```text
CAPABILITY SUFFICIENCY
!=
SUCCESSFUL EXECUTION
```

```text
CAPABILITY INVOCATION
!=
OBSERVED EFFECT
```

The resolver establishes execution possibility.

It does not establish permission, authority, successful completion, or
empirical truth.

______________________________________________________________________

## 3. Resolver Position

```text
TASK CONTRACT
      ↓
┌─────────────────────────────┐
│     CAPABILITY RESOLVER     │
│                             │
│ derive requirements         │
│ inspect manifests           │
│ discover candidates         │
│ validate availability       │
│ validate compatibility      │
│ resolve dependencies        │
│ construct capability plan   │
│ expose capability gaps      │
└─────────────────────────────┘
      ↓
CAPABILITY CONTRACT / PLAN
      ↓
POLICY / AUTHORITY /
PROVENANCE / TRANSACTION
```

______________________________________________________________________

## 4. Resolver Objective

The resolver should construct:

```text
THE SMALLEST SUFFICIENT
CAPABILITY SET
THAT CAN SATISFY
THE TASK CONTRACT
WITHOUT INVENTING
CAPABILITIES,
EXPANDING EFFECTS,
OR IGNORING LIMITS.
```

______________________________________________________________________

## 5. Inputs

The resolver may consume:

```text
TASK CONTRACT

CAPABILITY MANIFESTS

CAPABILITY CONTRACTS

CURRENT RUNTIME STATE

CONNECTOR STATE

TOOL STATE

MODEL CAPABILITIES

LOCAL EXECUTION CAPABILITIES

EXTERNAL SERVICE CAPABILITIES

ENVIRONMENT INFORMATION

VERSION INFORMATION

DEPENDENCY STATE

FRESHNESS INFORMATION
```

Only information relevant to the task should become load-bearing.

______________________________________________________________________

## 6. Output Classes

The resolver produces one of:

```text
RESOLVED

CONDITIONAL

COMPETING

DEGRADED

BLOCKED

UNKNOWN/GAP
```

______________________________________________________________________

## 7. Resolved

Use when a sufficient capability plan is established.

```yaml
status: RESOLVED
capability_plan:
  - capability_a
  - capability_b
```

This means:

```text
EXECUTION PATH IDENTIFIED
```

not:

```text
EXECUTION AUTHORIZED
```

______________________________________________________________________

## 8. Conditional

Use when capability sufficiency depends on an explicit unresolved condition.

Example:

```text
CAPABILITY X IS SUFFICIENT
IF
CONNECTOR SESSION IS ACTIVE
```

______________________________________________________________________

## 9. Competing

Use when multiple materially different capability plans remain viable and
selection matters.

Example:

```text
LOCAL PARSER
vs
REMOTE SERVICE
```

with materially different:

```text
PRIVACY

LATENCY

COST

EFFECTS

PROVENANCE

QUALITY
```

______________________________________________________________________

## 10. Degraded

Use when the task can be partially satisfied, but not at the requested
capability level.

Example:

```text
REQUESTED:
EDIT FILE

AVAILABLE:
READ FILE
```

A read-only alternative may exist, but it is not equivalent.

______________________________________________________________________

## 11. Blocked

Use when a required capability is known to be unavailable or incompatible.

______________________________________________________________________

## 12. Unknown / Gap

Use when capability state cannot be established.

```text
UNKNOWN
!=
UNAVAILABLE
```

______________________________________________________________________

## 13. Capability Requirement Extraction

The resolver begins from the Task Contract.

Conceptually:

```text
TaskContract
→
RequiredCapabilitySet
```

Potential requirements include:

```text
READ

SEARCH

RETRIEVE

PARSE

ANALYZE

REASON

GENERATE

TRANSFORM

EXECUTE CODE

CREATE FILE

EDIT FILE

DELETE FILE

QUERY DATABASE

CALL API

SEND MESSAGE

SCHEDULE EVENT

OBSERVE STATE

COMMIT STATE

ROLL BACK
```

______________________________________________________________________

## 14. Semantic Requirement vs Implementation

The task may require:

```text
RETRIEVE CURRENT WEATHER
```

The resolver should not prematurely bind that to one specific implementation.

Candidate implementations may include:

```text
WEATHER API

WEB RETRIEVAL

CONNECTED DATA SOURCE
```

The requirement is semantic.

The capability is operational.

______________________________________________________________________

## 15. Capability Manifest

A capability manifest describes what a capability claims to provide.

Conceptually:

```yaml
CapabilityManifest:

  capability_id:

  provider:

  capability_class:

  operations: []

  inputs:

  outputs:

  preconditions:

  limits:

  environment:

  regime:

  version:

  freshness:

  dependencies:

  effects:

  failure_modes:

  provenance:

  status:
```

______________________________________________________________________

## 16. Manifest Is a Source Claim

A manifest declaring:

```text
CAPABILITY SUPPORTS X
```

is initially:

```text
SOURCE_CLAIM
```

unless validated by stronger evidence.

Documentation alone does not prove successful execution.

______________________________________________________________________

## 17. Capability Contract

A Capability Contract binds a capability to a particular task requirement.

Conceptually:

```yaml
CapabilityContract:

  requirement:

  selected_capability:

  operation:

  input_binding:

  output_binding:

  preconditions:

  limits:

  dependencies:

  effects:

  freshness:

  environment:

  failure_semantics:

  provenance:

  invalidation_conditions:
```

______________________________________________________________________

## 18. Capability Classes

Candidate capability classes:

```text
COGNITIVE

INFORMATION_RETRIEVAL

STORAGE

COMPUTE

TRANSFORMATION

COMMUNICATION

OBSERVATION

CONTROL

TRANSACTION

EXTERNAL_SERVICE

HUMAN

COMPOSITE
```

______________________________________________________________________

## 19. Cognitive Capability

Examples:

```text
REASONING

CLASSIFICATION

SUMMARIZATION

SYNTHESIS

PLANNING
```

Do not confuse model competence claims with verified universal capability.

______________________________________________________________________

## 20. Information Retrieval Capability

Examples:

```text
FILE READ

DATABASE QUERY

SEARCH

WEB RETRIEVAL

CONNECTOR READ
```

______________________________________________________________________

## 21. Storage Capability

Examples:

```text
CREATE FILE

WRITE RECORD

UPDATE DOCUMENT

PERSIST STATE
```

______________________________________________________________________

## 22. Compute Capability

Examples:

```text
RUN CODE

CALCULATE

SIMULATE

PROCESS DATA
```

______________________________________________________________________

## 23. Transformation Capability

Examples:

```text
CONVERT FORMAT

RESIZE

TRANSLATE

REFORMAT

RESTRUCTURE
```

______________________________________________________________________

## 24. Communication Capability

Examples:

```text
SEND EMAIL

SEND MESSAGE

POST EXTERNALLY

NOTIFY
```

Communication capability is inherently effect-sensitive.

______________________________________________________________________

## 25. Observation Capability

Examples:

```text
CHECK STATUS

READ CURRENT STATE

VERIFY EFFECT

MONITOR CONDITION
```

Observation must be distinguished from mutation.

______________________________________________________________________

## 26. Control Capability

Examples:

```text
START

STOP

RESTART

DEPLOY

ROLL BACK

CONFIGURE
```

______________________________________________________________________

## 27. Transaction Capability

Examples:

```text
PREPARE

COMMIT

ABORT

COMPARE-AND-SWAP

VERSIONED UPDATE
```

Conceptual availability does not imply a literal database transaction system.

______________________________________________________________________

## 28. External Service Capability

Capabilities supplied by:

```text
API

PLUGIN

CONNECTOR

REMOTE TOOL

CLOUD SERVICE
```

require external-state validation.

______________________________________________________________________

## 29. Human Capability

Some tasks may require:

```text
HUMAN APPROVAL

HUMAN JUDGMENT

PHYSICAL ACTION

MANUAL VERIFICATION
```

The resolver must be able to identify:

```text
NO MACHINE CAPABILITY SUFFICIENT
```

rather than invent one.

______________________________________________________________________

## 30. Composite Capability

A task may require:

```text
C1 + C2 + C3
```

rather than one capability.

Example:

```text
READ FILE
+
TRANSFORM CONTENT
+
WRITE FILE
```

______________________________________________________________________

## 31. Capability Discovery

Candidate discovery sources:

```text
REGISTERED MANIFESTS

RUNTIME TOOL REGISTRY

CONNECTED SERVICES

LOCAL ENVIRONMENT

CANONICAL CAPABILITY MAP

VALIDATED PRIOR CAPABILITY CAPSULES
```

Do not search the entire capability universe when a local sufficient set is
known.

______________________________________________________________________

## 32. Candidate Set

For requirement `R`:

```text
Candidates(R)
=
{
C1,
C2,
...
Cn
}
```

Each candidate must be tested against the task's actual requirements.

______________________________________________________________________

## 33. No Candidate

If:

```text
Candidates(R) = ∅
```

then:

```text
CAPABILITY GAP
```

Do not fabricate a capability.

______________________________________________________________________

## 34. Candidate Qualification

A candidate is qualified only if relevant dimensions match.

Conceptually:

```text
Qualified(C,R)
=
OperationMatch
∧
InputMatch
∧
OutputMatch
∧
EnvironmentMatch
∧
RegimeMatch
∧
FreshnessSufficient
∧
LimitsCompatible
∧
DependenciesResolvable
```

Policy and authority are intentionally excluded here because they are
separate governance layers.

______________________________________________________________________

## 35. Operation Match

The capability must actually support the required operation.

```text
READ
```

does not imply:

```text
WRITE
```

```text
CREATE
```

does not imply:

```text
UPDATE
```

```text
DRAFT
```

does not imply:

```text
SEND
```

______________________________________________________________________

## 36. Directionality

Capability direction matters.

```text
IMPORT
!=
EXPORT
```

```text
UPLOAD
!=
DOWNLOAD
```

```text
READ
!=
WRITE
```

```text
ENCODE
!=
DECODE
```

unless the manifest explicitly supports both.

______________________________________________________________________

## 37. Input Compatibility

A capability must accept the actual task input.

Potential dimensions:

```text
TYPE

FORMAT

SIZE

ENCODING

SCHEMA

LANGUAGE

VERSION

ACCESS METHOD
```

______________________________________________________________________

## 38. Output Compatibility

The output must satisfy downstream requirements.

Example:

```text
CAPABILITY OUTPUT:
PLAIN TEXT

TASK DELIVERABLE:
EDITABLE XLSX
```

The capability alone is insufficient.

A transformation capability may be required.

______________________________________________________________________

## 39. Type Compatibility

Conceptually:

```text
OutputType(C1)
→
InputType(C2)
```

must be compatible for composition.

______________________________________________________________________

## 40. Schema Compatibility

Two capabilities may both use JSON but remain incompatible.

```text
FORMAT MATCH
!=
SCHEMA MATCH
```

______________________________________________________________________

## 41. Version Compatibility

Example:

```text
CAPABILITY SUPPORTS API v2

TARGET REQUIRES API v3
```

Result:

```text
INCOMPATIBLE
```

unless an adapter exists.

______________________________________________________________________

## 42. Environment Compatibility

Capability validity may depend on:

```text
OPERATING SYSTEM

RUNTIME

NETWORK

REGION

HARDWARE

ACCOUNT

TENANT

PROJECT

SANDBOX

PRODUCTION
```

______________________________________________________________________

## 43. Regime Compatibility

A capability proven in one regime is not automatically valid in another.

```text
TEST
!=
PRODUCTION
```

```text
LOCAL
!=
REMOTE
```

```text
SIMULATION
!=
PHYSICAL SYSTEM
```

______________________________________________________________________

## 44. Freshness

Capability state can expire.

Examples:

```text
TOKEN EXPIRED

CONNECTOR DISCONNECTED

MODEL RETIRED

API VERSION CHANGED

SERVICE DOWN

PERMISSION CHANGED

FILE MOVED
```

Therefore:

```text
CAPABILITY AVAILABLE @ T1
```

does not imply:

```text
CAPABILITY AVAILABLE @ T2
```

______________________________________________________________________

## 45. Freshness Envelope

Conceptually:

```yaml
freshness:
  observed_at:
  valid_until:
  revalidation_trigger:
```

where applicable.

______________________________________________________________________

## 46. Availability Classes

Candidate states:

```text
AVAILABLE

CONDITIONALLY_AVAILABLE

DEGRADED

UNAVAILABLE

UNKNOWN

STALE
```

______________________________________________________________________

## 47. Available

Observed or sufficiently validated to be usable in the current context.

______________________________________________________________________

## 48. Conditionally Available

Requires a condition such as:

```text
CONNECTION

LOGIN

DEPENDENCY

CONFIGURATION

RESOURCE
```

______________________________________________________________________

## 49. Degraded Capability

Capability exists but with reduced:

```text
QUALITY

THROUGHPUT

SCOPE

FEATURE SET

PRECISION

OUTPUT TYPE
```

______________________________________________________________________

## 50. Unavailable

Known not to be usable.

______________________________________________________________________

## 51. Unknown

No sufficient evidence about current availability.

Do not convert `UNKNOWN` into `UNAVAILABLE`.

______________________________________________________________________

## 52. Stale

Previous availability evidence is no longer fresh enough for the task.

______________________________________________________________________

## 53. Capability Limits

Every capability should be treated as bounded.

Possible limits:

```text
MAX INPUT SIZE

MAX OUTPUT SIZE

RATE LIMIT

TIMEOUT

SUPPORTED TYPES

SUPPORTED LANGUAGES

CONTEXT WINDOW

MEMORY

STORAGE

NETWORK ACCESS

FILE SIZE

TRANSACTION SIZE

CONCURRENCY
```

______________________________________________________________________

## 54. Limit Compatibility

A capability that nominally supports an operation may still be insufficient.

Example:

```text
CAPABILITY:
READ FILE ≤ 10 MB

TASK:
READ FILE = 500 MB
```

Nominal operation match is insufficient.

______________________________________________________________________

## 55. Limit Splitting

If a task exceeds a capability limit, determine whether safe decomposition
exists.

```text
TASK
→
CHUNK 1
→
CHUNK 2
→
...
```

Only if decomposition preserves semantics.

______________________________________________________________________

## 56. Non-Decomposable Tasks

Do not chunk blindly when the task requires:

```text
GLOBAL CONSISTENCY

ATOMICITY

FULL-CONTEXT REASONING

ORDER DEPENDENCE

CROSS-CHUNK CAUSAL STRUCTURE
```

______________________________________________________________________

## 57. Capability Dependencies

Capability `C1` may require:

```text
C2

RESOURCE R

STATE S

SERVICE V

CONNECTION K
```

Conceptually:

```text
C1
↓
C2
↓
C3
```

The resolver must establish dependency closure for load-bearing paths.

______________________________________________________________________

## 58. Dependency Closure

```text
Closure(C)
=
C
+
all load-bearing capability dependencies
```

A capability is not sufficiently resolved merely because its top-level
manifest exists.

______________________________________________________________________

## 59. Circular Dependency

If:

```text
C1 → C2 → C1
```

and neither is independently satisfiable:

```text
CAPABILITY DEADLOCK
```

or unresolved composition gap.

______________________________________________________________________

## 60. Optional Dependency

Distinguish:

```text
REQUIRED DEPENDENCY
```

from:

```text
OPTIONAL ENHANCEMENT
```

Optional enhancement failure should not invalidate a sufficient core path.

______________________________________________________________________

## 61. Capability Composition

For task `T`:

```text
Plan(T)
=
C1 ∘ C2 ∘ ... ∘ Cn
```

where each interface is compatible.

______________________________________________________________________

## 62. Composition Validity

Conceptually:

```text
ValidComposition(P)
=
∀ adjacent Ci,Cj:
Output(Ci) compatible Input(Cj)
∧
all dependencies satisfied
∧
scope preserved
∧
regime preserved
∧
effect semantics preserved
```

______________________________________________________________________

## 63. Capability Graph

Example:

```text
TASK
 ↓
READ SOURCE
 ↓
PARSE
 ↓
ANALYZE
 ↓
GENERATE ARTIFACT
 ↓
WRITE ARTIFACT
```

Each node is separately resolvable.

______________________________________________________________________

## 64. Alternative Plans

A task may support:

```text
PLAN A:
C1 → C2

PLAN B:
C3 → C4 → C5
```

The resolver should not automatically choose the shortest plan.

______________________________________________________________________

## 65. Plan Evaluation

Candidate dimensions:

```text
SUFFICIENCY

INTEGRITY

EFFECT EXPOSURE

PROVENANCE QUALITY

REVERSIBILITY

RELIABILITY

FRESHNESS

LATENCY

COST

COMPLEXITY
```

Governance may add further criteria downstream.

______________________________________________________________________

## 66. Optimization Order

Default candidate order:

```text
INTEGRITY

SUFFICIENCY

LOWER IRREVERSIBLE EFFECT

BETTER PROVENANCE

REPAIRABILITY

RELIABILITY

EFFICIENCY
```

Speed cannot compensate for semantic insufficiency.

______________________________________________________________________

## 67. Least-Capability Principle

Use:

```text
THE SMALLEST CAPABILITY SET
THAT FULLY SATISFIES
THE TASK CONTRACT.
```

Do not activate broader capabilities merely because they exist.

______________________________________________________________________

## 68. Least-Privilege Compatibility

Capability resolution should support downstream least-privilege governance.

If task requires:

```text
READ ONE FILE
```

do not prefer a capability requiring:

```text
WRITE ALL FILES
```

when a narrower sufficient capability exists.

______________________________________________________________________

## 69. Effect Envelope

Each capability should expose potential effects.

Candidate classes:

```text
NONE

READ

LOCAL COMPUTE

EPHEMERAL WRITE

PERSISTENT WRITE

EXTERNAL COMMUNICATION

STATE MUTATION

DESTRUCTIVE

FINANCIAL

GOVERNANCE
```

______________________________________________________________________

## 70. Effect Expansion Check

Capability plan must not silently exceed task effect intent.

```text
TaskEffectEnvelope
```

must contain the required effects of the selected plan, subject to downstream
governance.

If a capability necessarily creates broader effects:

```text
MATERIAL EFFECT MISMATCH
```

must be surfaced.

______________________________________________________________________

## 71. Read vs Write

A capability with write access may technically perform a read.

But when a narrower read-only capability exists, it may be preferable for
governance and risk minimization.

______________________________________________________________________

## 72. Hidden Effects

Capabilities may create secondary effects:

```text
LOGGING

CACHE WRITE

REMOTE UPLOAD

METADATA CREATION

NOTIFICATION

BILLING

AUDIT EVENT
```

Material hidden effects should be represented when known.

______________________________________________________________________

## 73. Capability Side Effects

Do not assume:

```text
PRIMARY OPERATION
=
ONLY EFFECT
```

Side effects may alter policy or authority requirements.

______________________________________________________________________

## 74. Capability Provenance

For each selected capability, retain:

```text
SOURCE OF MANIFEST

VERSION

PROVIDER

OBSERVATION OF AVAILABILITY

VALIDATION EVIDENCE

DEPENDENCY ORIGIN
```

where material.

______________________________________________________________________

## 75. Provenance Independence

Multiple declarations may descend from the same provider metadata.

```text
MANIFEST A
+
README B
+
DOC C
```

may all originate from one underlying source.

Do not count them as independent confirmation.

______________________________________________________________________

## 76. Capability Confidence

Confidence in capability sufficiency is bounded by the weakest load-bearing
component.

Conceptually:

```text
Confidence(Plan)
≤
MIN(
  Availability,
  OperationMatch,
  InterfaceCompatibility,
  DependencyClosure,
  EnvironmentCompatibility,
  Freshness
)
```

______________________________________________________________________

## 77. Capability Proof Capsule

Consequential capability decisions should conceptually carry:

```yaml
CapabilityProofCapsule:

  task_requirement:

  selected_plan:

  candidate_capabilities:

  selected_capabilities:

  manifests:

  availability_evidence:

  interface_bindings:

  dependencies:

  environment:

  regime:

  freshness:

  limits:

  effects:

  competing_plans:

  gaps:

  falsifiers:

  invalidation_conditions:

  confidence_ceiling:
```

______________________________________________________________________

## 78. Capability Falsifiers

Examples:

```text
CONNECTOR DISCONNECTED

TOOL NO LONGER EXPOSED

API VERSION CHANGED

INPUT EXCEEDS LIMIT

OUTPUT TYPE INCOMPATIBLE

DEPENDENCY FAILED

NETWORK UNAVAILABLE

TARGET ENVIRONMENT CHANGED
```

______________________________________________________________________

## 79. Invalidation Conditions

Capability resolution should be invalidated when load-bearing conditions
change.

Examples:

```text
CAPABILITY VERSION CHANGE

SESSION CHANGE

CONNECTION CHANGE

ACCOUNT CHANGE

TARGET CHANGE

ENVIRONMENT CHANGE

DEPENDENCY CHANGE

TASK VERSION CHANGE

SERVICE STATUS CHANGE
```

______________________________________________________________________

## 80. Capability State Version

Conceptually:

```text
CAPABILITY PLAN @ STATE V1
```

Before consequential execution:

```text
CHECK CURRENT STATE
```

If a load-bearing capability changed:

```text
REVALIDATE DEPENDENT PLAN
```

______________________________________________________________________

## 81. MVCC Pattern

Resolver reads:

```text
CAPABILITY REGISTRY @ V1
```

constructs:

```text
PLAN @ V1
```

Execution may later verify:

```text
CURRENT VERSION == V1
```

for load-bearing mutable state.

This is a reasoning pattern, not a claim of literal infrastructure.

______________________________________________________________________

## 82. CAS Pattern

Conceptually:

```text
IF
CURRENT_CAPABILITY_STATE
=
EXPECTED_STATE
THEN
CONTINUE
ELSE
RE-RESOLVE
```

______________________________________________________________________

## 83. Selective Invalidation

If:

```text
C3
```

fails in:

```text
C1 → C2 → C3 → C4
```

invalidate:

```text
C3
+
dependent descendants
```

not unrelated capability reasoning.

______________________________________________________________________

## 84. Repair

```text
FAILED CAPABILITY
    ↓
LOCALIZE FAILURE
    ↓
INVALIDATE DEPENDENTS
    ↓
SEARCH ALTERNATIVE
    ↓
REVALIDATE COMPOSITION
    ↓
CONTINUE IF SUFFICIENT
```

______________________________________________________________________

## 85. Failed Path Rule

Do not retry the same capability path without changed conditions when the
failure is deterministic.

Example:

```text
UNSUPPORTED FORMAT
```

will not be repaired by identical retries.

______________________________________________________________________

## 86. Transient Failure

A transient failure may justify retry.

Examples:

```text
TIMEOUT

TEMPORARY SERVICE UNAVAILABLE

RATE LIMIT
```

Retry semantics belong partly to runtime policy.

The resolver should preserve failure type.

______________________________________________________________________

## 87. Permanent Failure

Examples:

```text
UNSUPPORTED OPERATION

INCOMPATIBLE VERSION

MISSING REQUIRED FEATURE
```

should trigger alternative resolution rather than blind retry.

______________________________________________________________________

## 88. Capability Fast Path

Use the fast path when:

```text
REQUIREMENT IS CLEAR

ONE LOCAL CAPABILITY DOMINATES

AVAILABILITY IS CURRENT

INPUT/OUTPUT MATCH

NO MATERIAL LIMIT ISSUE

DEPENDENCIES CLOSED

NO MATERIAL CONFLICT

NO EFFECT EXPANSION
```

______________________________________________________________________

## 89. Fast Path Result

```yaml
status: RESOLVED

complexity: C0

plan:
  - capability_x
```

______________________________________________________________________

## 90. Fast Path Independence

Do not infer locality from task simplicity.

Example:

```text
"send this"
```

may require:

```text
RECIPIENT RESOLUTION

COMMUNICATION CAPABILITY

CONNECTED ACCOUNT

AUTHORITY

POLICY

EXTERNAL EFFECT GOVERNANCE
```

______________________________________________________________________

## 91. Escalation Triggers

Escalate capability reasoning for:

```text
MULTIPLE CANDIDATES

STALE AVAILABILITY

EXTERNAL EFFECTS

HIGH STAKES

LARGE DATA

COMPLEX COMPOSITION

CROSS-ENVIRONMENT EXECUTION

CAPABILITY CONFLICT

DEPENDENCY AMBIGUITY

PROVENANCE UNCERTAINTY

IRREVERSIBLE OPERATIONS

GOVERNANCE EFFECTS
```

______________________________________________________________________

## 92. Adaptive Complexity

Candidate classes:

```text
C0 DIRECT

C1 COMPACT

C2 STRUCTURED

C3 DEEP

C4 MAXIMUM
```

Use the lowest sufficient class.

______________________________________________________________________

## 93. C0 Direct

One obvious local capability, low stakes, no effectful ambiguity.

______________________________________________________________________

## 94. C1 Compact

Small composition or minor validation required.

______________________________________________________________________

## 95. C2 Structured

Multiple capability requirements and explicit dependency validation.

______________________________________________________________________

## 96. C3 Deep

External services, material effects, weak availability evidence, or complex
composition.

______________________________________________________________________

## 97. C4 Maximum

Irreversible/high-stakes operations, governance changes, cross-system atomic
requirements, or severe provenance/dependency ambiguity.

______________________________________________________________________

## 98. Capability Gap Classification

Classify gaps:

```text
CRITICAL

DECISION-RELEVANT

EXPLANATORY

COSMETIC
```

______________________________________________________________________

## 99. Critical Capability Gap

A missing capability without which the task cannot be safely or correctly
performed.

Example:

```text
TASK:
SEND MESSAGE

NO COMMUNICATION CAPABILITY
```

______________________________________________________________________

## 100. Decision-Relevant Gap

Multiple capability paths exist but missing information could alter which
path should be selected.

______________________________________________________________________

## 101. Explanatory Gap

Missing detail that does not alter plan sufficiency.

______________________________________________________________________

## 102. Cosmetic Gap

Non-material metadata or naming uncertainty.

Do not block execution planning for cosmetic gaps.

______________________________________________________________________

## 103. Capability Sensitivity

For each load-bearing capability assumption:

```text
IF THIS WERE FALSE,
WOULD THE PLAN FAIL
OR CHANGE MATERIALLY?
```

If yes:

```text
REVALIDATE FIRST
```

______________________________________________________________________

## 104. Cheapest High-Information Test

When uncertainty exists, prefer:

```text
CHECK TOOL EXISTS

CHECK CONNECTION

CHECK VERSION

CHECK INPUT LIMIT

CHECK TARGET ACCESSIBILITY
```

before expensive execution attempts.

______________________________________________________________________

## 105. Competing Capability Plans

Do not force convergence when plans are:

```text
EQUALLY SUPPORTED

INCOMPARABLE

CORRELATED

OR DIFFERENT IN MATERIAL GOVERNANCE PROPERTIES
```

Preserve:

```text
COMPETING
```

until a discriminating criterion exists.

______________________________________________________________________

## 106. Plan Dominance

Plan `P1` dominates `P2` if it is at least as sufficient and strictly better
on a material criterion without introducing worse load-bearing trade-offs.

Example:

```text
SAME OUTPUT
+
NARROWER EFFECTS
+
SAME RELIABILITY
```

may favor `P1`.

______________________________________________________________________

## 107. Capability Fallback

Fallback is valid only if it still satisfies the Task Contract.

```text
PRIMARY FAILED
→
FALLBACK
```

does not imply the fallback is equivalent.

______________________________________________________________________

## 108. Degraded Fallback

If fallback provides only partial satisfaction:

```text
RETURN DEGRADED
```

and expose the missing requirement.

______________________________________________________________________

## 109. No Silent Substitution

Do not silently substitute:

```text
CURRENT DATA
→
STALE CACHE
```

```text
WRITE
→
READ
```

```text
EXACT FORMAT
→
DIFFERENT FORMAT
```

```text
VERIFIED SOURCE
→
UNVERIFIED SOURCE
```

when the difference is task-relevant.

______________________________________________________________________

## 110. Safe Alternative

When the requested capability is unavailable, the resolver may identify a
safe alternative.

Keep:

```text
REQUESTED CAPABILITY PATH
```

distinct from:

```text
ALTERNATIVE PATH
```

______________________________________________________________________

## 111. Example — Read File

Task:

```text
READ FILE A
```

Capability:

```text
FILE_READER
```

Validation:

```text
FILE EXISTS
INPUT TYPE SUPPORTED
SIZE WITHIN LIMIT
READ ACCESS AVAILABLE
```

Result:

```text
RESOLVED
```

______________________________________________________________________

## 112. Example — Unsupported File

Task:

```text
READ FORMAT X
```

Reader supports:

```text
A
B
C
```

No converter exists.

Result:

```text
BLOCKED:
UNSUPPORTED FORMAT
```

Do not pretend the file was read.

______________________________________________________________________

## 113. Example — Converter Composition

Task:

```text
ANALYZE FORMAT X
```

Available:

```text
X → TEXT CONVERTER
TEXT ANALYZER
```

Plan:

```text
FORMAT X
↓
CONVERT
↓
TEXT
↓
ANALYZE
```

if conversion preserves required semantics.

______________________________________________________________________

## 114. Example — Lossy Conversion

If converter discards information required by the task:

```text
CONVERSION EXISTS
```

but:

```text
PLAN INSUFFICIENT
```

Availability is not enough.

______________________________________________________________________

## 115. Example — Draft Email

Task:

```text
DRAFT EMAIL
```

Required capability:

```text
TEXT GENERATION
```

Sending capability is not required.

______________________________________________________________________

## 116. Example — Send Email

Task:

```text
SEND EMAIL
```

Required composition may include:

```text
GENERATE / RECEIVE CONTENT
+
RECIPIENT BINDING
+
EMAIL SERVICE
+
CONNECTED ACCOUNT
+
SEND OPERATION
```

Policy and authority remain downstream checks.

______________________________________________________________________

## 117. Example — Current Price

Task:

```text
CURRENT PRICE OF X
```

Static internal knowledge alone is insufficient if freshness requirements
demand current market data.

The resolver should require a fresh retrieval capability.

______________________________________________________________________

## 118. Example — Code Execution

Task:

```text
EXECUTE PYTHON ANALYSIS
```

Candidate capability must satisfy:

```text
PYTHON EXECUTION

REQUIRED LIBRARIES

FILE ACCESS

RESOURCE LIMITS

OUTPUT REQUIREMENTS
```

______________________________________________________________________

## 119. Example — Missing Library

Python runtime exists, but required library does not.

Result may be:

```text
CONDITIONAL
```

if installation is possible and governed,

or:

```text
BLOCKED
```

if no compatible path exists.

______________________________________________________________________

## 120. Example — Web Requirement

Task:

```text
VERIFY CURRENT PUBLIC FACT
```

If local knowledge is stale and web retrieval is available:

```text
WEB RETRIEVAL
```

may become load-bearing.

If web retrieval is unavailable:

```text
CURRENT VERIFICATION GAP
```

must remain visible.

______________________________________________________________________

## 121. Example — Local vs Remote

Task can be completed by:

```text
LOCAL CAPABILITY
```

or:

```text
REMOTE SERVICE
```

If local is sufficient and avoids unnecessary external effects:

```text
LOCAL MAY DOMINATE
```

subject to quality and other task constraints.

______________________________________________________________________

## 122. Example — Destructive Capability

Task:

```text
DELETE RESOURCE X
```

Capability Resolver may establish:

```text
DELETE OPERATION AVAILABLE
```

It must not conclude:

```text
DELETE AUTHORIZED
```

or execute before downstream governance.

______________________________________________________________________

## 123. Example — Human Required

Task:

```text
PHYSICALLY INSPECT DEVICE
```

No physical embodiment capability exists.

Result:

```text
MACHINE CAPABILITY GAP
```

Possible alternative:

```text
HUMAN INSPECTION REQUIRED
```

______________________________________________________________________

## 124. Example — Partial Capability

Task:

```text
EDIT PDF WHILE PRESERVING FORM FIELDS
```

Available capability can edit PDF but destroys forms.

Result:

```text
DEGRADED / INSUFFICIENT
```

not `RESOLVED`.

______________________________________________________________________

## 125. Example — Size Limit

Task input:

```text
2 GB DATASET
```

Capability limit:

```text
100 MB
```

Resolver must determine whether:

```text
SAFE PARTITIONING
```

exists.

If global analysis requires full dataset context:

```text
CAPABILITY GAP
```

remains.

______________________________________________________________________

## 126. Example — Cross-Capability Atomicity

Task:

```text
UPDATE A AND B ATOMICALLY
```

Capabilities:

```text
UPDATE A

UPDATE B
```

individually exist.

That does not prove:

```text
ATOMIC UPDATE A+B
```

exists.

Atomicity is a separate requirement.

______________________________________________________________________

## 127. Atomic Multi-Capability Reasoning

Some tasks require capabilities to satisfy a joint invariant.

```text
C1
+
C2
```

may individually be sufficient for their operations but jointly insufficient
for:

```text
ATOMICITY

CONSISTENCY

ORDERING

FINALITY
```

The resolver must reason over the composition, not only nodes.

______________________________________________________________________

## 128. Causal Epoch Finality

For capability plans depending on mutable causal state:

```text
PLAN RESOLVED @ EPOCH E1
```

may cease to be execution-valid after relevant state moves to:

```text
E2
```

Final execution eligibility requires relevant causal state still to satisfy
the plan's validity conditions.

______________________________________________________________________

## 129. Shard-Local Resolution

Local capability resolution is safe only when:

```text
DEPENDENCY CLOSURE IS LOCAL

NO MATERIAL REMOTE CAPABILITY STATE CAN ALTER SUFFICIENCY

NO CROSS-SHARD EFFECT COUPLING

NO SHARED GOVERNANCE DEPENDENCY
```

______________________________________________________________________

## 130. Proof-Based Coordination Avoidance

Do not globally query every capability source if local proof establishes:

```text
ONE SUFFICIENT PLAN

COMPLETE LOCAL DEPENDENCY CLOSURE

NO MATERIAL CONFLICT

NO REMOTE STATE RELEVANCE
```

Coordination avoidance must be proven, not assumed.

______________________________________________________________________

## 131. Capability Resolver and RSCF

Capability resolution may create RSCF structures around:

```text
TASK REQUIREMENT

CANDIDATE CAPABILITIES

DEPENDENCIES

LIMITS

ENVIRONMENT

EFFECTS
```

Traverse only dependencies capable of changing the capability decision.

______________________________________________________________________

## 132. Capability Resolver and Fractal Retrieval

Use:

```text
BOOTSTRAP
↓
H DOMAIN
↓
M CAPABILITY SUBSYSTEM
↓
L CAPABILITY DETAIL
↓
RAW MANIFEST / EVIDENCE
ONLY IF REQUIRED
```

______________________________________________________________________

## 133. Raw Evidence Rule

Raw capability evidence defaults:

```text
DO_NOT_LOAD_UNLESS_REQUIRED
```

Load it when necessary to resolve:

```text
AVAILABILITY

LIMIT

VERSION

DEPENDENCY

CONTRADICTION

FRESHNESS

EFFECT
```

______________________________________________________________________

## 134. Capability Resolver and GMEF

If a task requires creating, replacing, or modifying a canonical capability
mechanism:

```text
ROUTE GOVERNANCE EVOLUTION
```

rather than treating the change as ordinary runtime selection.

______________________________________________________________________

## 135. Capability Resolver and Provenance Resolver

Capability Resolver asks:

```text
WHAT CAN PERFORM THIS TASK?
```

Provenance Resolver asks:

```text
WHAT EVIDENCE / SOURCE LINEAGE
SUPPORTS THE INPUTS AND CLAIMS?
```

The two interact but must not collapse into one another.

______________________________________________________________________

## 136. Capability Resolver and Policy

Capability exists:

```text
YES
```

Policy may still say:

```text
NO
```

Therefore:

```text
CAPABILITY
≠
PERMISSION
```

______________________________________________________________________

## 137. Capability Resolver and Authority

Capability may exist and policy may permit an operation generally.

The current principal may still lack authority.

Therefore:

```text
CAPABILITY
≠
AUTHORITY
```

______________________________________________________________________

## 138. Capability Resolver and Effects

Capability Resolver should expose:

```text
POTENTIAL EFFECTS
```

to the Effect subsystem.

The Effect subsystem determines the actual governed effect plan.

______________________________________________________________________

## 139. Capability Resolver and Observability

A task requiring proof of completion may need:

```text
EXECUTION CAPABILITY
+
OBSERVATION CAPABILITY
```

Example:

```text
UPLOAD FILE
+
VERIFY FILE EXISTS REMOTELY
```

Invocation alone is not completion evidence.

______________________________________________________________________

## 140. Capability Resolver and Semantic Transaction

A semantic transaction may bind:

```text
TASK VERSION

CAPABILITY PLAN VERSION

CAPABILITY STATE SNAPSHOT

DEPENDENCY SNAPSHOT
```

for consequential operations.

______________________________________________________________________

## 141. Capability Resolver and Commit

Before commit:

```text
REVALIDATE
LOAD-BEARING
CAPABILITY CONDITIONS
```

if mutable.

______________________________________________________________________

## 142. Capability Resolver and Finalizer

Finalizer should evaluate actual results, not merely whether the selected
capability was invoked.

```text
TOOL CALL SUCCEEDED
!=
TASK COMPLETED
```

______________________________________________________________________

## 143. Capability Resolver and Recovery

When execution fails:

```text
FAILURE
↓
CLASSIFY CAPABILITY FAILURE
↓
INVALIDATE DEPENDENT PLAN
↓
SEARCH ALTERNATIVE
↓
REVALIDATE
```

Do not globally recompute unless necessary.

______________________________________________________________________

## 144. Capability Resolver and Replay

Replay must preserve:

```text
CAPABILITY VERSION

PLAN VERSION

RELEVANT STATE

ENVIRONMENT
```

when historical reproducibility matters.

A current capability may behave differently from the historical one.

______________________________________________________________________

## 145. Capability Resolver and Memory

Previously validated capability plans may be reused only while:

```text
TASK REQUIREMENTS MATCH

DEPENDENCIES VALID

ENVIRONMENT MATCHES

REGIME MATCHES

FRESHNESS VALID

NO MATERIAL CONFLICT EXISTS
```

______________________________________________________________________

## 146. Capability Capsule Reuse

Conceptually:

```text
IF
DependenciesValid(P)
∧
ScopeCompatible(P,T)
∧
RegimeCompatible(P,T)
∧
Fresh(P)
∧
NoConflict(P)
THEN
REUSE
ELSE
REVALIDATE
```

______________________________________________________________________

## 147. Capability Anti-Fabrication

Never infer:

```text
TOOL NAME SOUNDS RIGHT
→
TOOL SUPPORTS OPERATION
```

```text
SERVICE EXISTS
→
SERVICE CONNECTED
```

```text
API DOCUMENTED
→
API ACCESSIBLE
```

```text
MODEL CAN GENERALLY DO X
→
CURRENT CONFIGURATION CAN DO X
```

______________________________________________________________________

## 148. Capability Anti-Generalization

Do not infer:

```text
WORKED ON FILE A
→
WORKS ON ALL FILES
```

```text
WORKED IN TEST
→
WORKS IN PRODUCTION
```

```text
WORKED ON VERSION 1
→
WORKS ON VERSION 2
```

______________________________________________________________________

## 149. Capability Anti-Benchmark Rule

Benchmark success does not establish universal capability.

```text
BENCHMARK PERFORMANCE
!=
TASK-SPECIFIC SUFFICIENCY
```

______________________________________________________________________

## 150. Capability Anti-Latency Rule

Reported latency is not hardware-independent or environment-independent.

Do not encode:

```text
CAPABILITY LATENCY = X
```

as universal without scope.

______________________________________________________________________

## 151. Capability Anti-Sybil Rule

Multiple capability descriptions derived from one provider do not create
independent validation.

______________________________________________________________________

## 152. Capability Anti-Effect Rule

Never resolve:

```text
READ REQUIREMENT
```

into a write-heavy capability without surfacing the broader effect envelope.

______________________________________________________________________

## 153. Capability Anti-Privilege Rule

Do not expand access scope merely to make capability selection easier.

______________________________________________________________________

## 154. Capability Anti-Retry Rule

Repeated failure does not create evidence of eventual success.

Retry only when failure semantics justify it.

______________________________________________________________________

## 155. Capability Anti-Substitution Rule

Do not silently replace a required capability with an easier but
semantically weaker operation.

______________________________________________________________________

## 156. Capability Anti-Regression Gate

Capability resolver optimizations must preserve or improve:

```text
REQUIREMENT FIDELITY

AVAILABILITY CORRECTNESS

LIMIT VISIBILITY

SCOPE CORRECTNESS

REGIME CORRECTNESS

FRESHNESS

DEPENDENCY CLOSURE

EFFECT VISIBILITY

PROVENANCE

CONTRADICTION VISIBILITY

REPAIRABILITY

AUDITABILITY
```

Otherwise reject the optimization.

______________________________________________________________________

## 157. Resolver Invariants

```text
CR-I01
A TASK REQUIREMENT MUST NOT BE TREATED AS AN EXISTING CAPABILITY.

CR-I02
A CAPABILITY DECLARATION MUST NOT BE TREATED AS CURRENT AVAILABILITY WITHOUT SUFFICIENT SUPPORT.

CR-I03
CAPABILITY AVAILABILITY MUST NOT BE TREATED AS POLICY PERMISSION.

CR-I04
CAPABILITY AVAILABILITY MUST NOT BE TREATED AS AUTHORITY.

CR-I05
READ CAPABILITY MUST NOT IMPLY WRITE CAPABILITY.

CR-I06
WRITE CAPABILITY MUST NOT IMPLY DELETE CAPABILITY.

CR-I07
DRAFT CAPABILITY MUST NOT IMPLY SEND CAPABILITY.

CR-I08
CAPABILITY LIMITS MUST REMAIN VISIBLE WHEN LOAD-BEARING.

CR-I09
INPUT AND OUTPUT CONTRACTS MUST BE COMPATIBLE.

CR-I10
VERSION AND REGIME COMPATIBILITY MUST NOT BE ASSUMED.

CR-I11
STALE CAPABILITY STATE MUST NOT BE TREATED AS CURRENT.

CR-I12
REQUIRED DEPENDENCIES MUST BE RESOLVED.

CR-I13
OPTIONAL DEPENDENCY FAILURE MUST NOT INVALIDATE AN OTHERWISE SUFFICIENT CORE PLAN.

CR-I14
CAPABILITY COMPOSITION MUST PRESERVE TASK SEMANTICS.

CR-I15
A COMPOSITE TASK MAY REQUIRE JOINT CAPABILITY VALIDATION.

CR-I16
ATOMICITY MUST NOT BE INFERRED FROM INDEPENDENT WRITE CAPABILITIES.

CR-I17
MATERIAL SIDE EFFECTS MUST REMAIN VISIBLE.

CR-I18
CAPABILITY SELECTION MUST NOT SILENTLY EXPAND TASK EFFECTS.

CR-I19
UNKNOWN CAPABILITY STATE MUST REMAIN DISTINCT FROM UNAVAILABLE.

CR-I20
DEGRADED CAPABILITY MUST NOT BE REPORTED AS FULL SUFFICIENCY.

CR-I21
COMPETING MATERIAL PLANS MUST REMAIN VISIBLE UNTIL DISCRIMINATED.

CR-I22
CAPABILITY PROVENANCE MUST REMAIN RECOVERABLE.

CR-I23
CONFIDENCE MUST NOT EXCEED THE WEAKEST LOAD-BEARING CAPABILITY PREMISE.

CR-I24
FAILED CAPABILITIES SHOULD INVALIDATE ONLY DEPENDENT PLAN COMPONENTS.

CR-I25
FAST-PATH RESOLUTION REQUIRES PROVEN LOCAL SUFFICIENCY.

CR-I26
CAPABILITY OPTIMIZATION MUST NOT WEAKEN INTEGRITY.
```

These identifiers remain candidate specification IDs until separately
registered as canonical invariants.

______________________________________________________________________

## 158. Capability Resolver Result

Conceptual form:

```yaml
CapabilityResolverResult:

  resolver_id:

  task_contract:
    task_id:
    task_version:

  status:

  complexity:

  requirements: []

  candidates: []

  selected_plan:

  capability_contracts: []

  availability:

  dependencies:

  limits:

  environment:

  regime:

  freshness:

  effects:

  competing_plans: []

  gaps:
    critical: []
    decision_relevant: []
    explanatory: []
    cosmetic: []

  provenance:

  uncertainty:

  invalidation_conditions:

  next_route:
```

______________________________________________________________________

## 159. Next Route

Candidate routes:

```text
CAPABILITY_READY

RETRIEVE_CAPABILITY_STATE

REQUEST_CONNECTION

REQUEST_RESOURCE

RESOLVE_DEPENDENCY

POLICY_RESOLUTION

AUTHORITY_RESOLUTION

PROVENANCE_RESOLUTION

RETURN_DEGRADED

BLOCK

RETURN_UNKNOWN
```

______________________________________________________________________

## 160. Resolver Pseudocode

```text
function resolve_capabilities(task, runtime):

    requirements =
        derive_capability_requirements(task)

    plans = []

    for requirement in requirements:

        candidates =
            discover_candidates(
                requirement,
                runtime
            )

        if candidates.empty:
            record_gap(
                requirement,
                CRITICAL
            )
            continue

        qualified = []

        for capability in candidates:

            manifest =
                load_minimum_manifest(
                    capability
                )

            if not operation_match(
                capability,
                requirement
            ):
                continue

            availability =
                validate_availability(
                    capability,
                    runtime
                )

            if availability == UNAVAILABLE:
                continue

            compatibility =
                validate_interfaces(
                    capability,
                    requirement
                )

            if not compatibility:
                continue

            if not environment_compatible(
                capability,
                task
            ):
                continue

            if not regime_compatible(
                capability,
                task
            ):
                continue

            if not limits_compatible(
                capability,
                requirement
            ):
                continue

            dependencies =
                resolve_dependency_closure(
                    capability
                )

            if not dependencies.sufficient:
                continue

            qualified.append(
                build_capability_contract(
                    requirement,
                    capability,
                    availability,
                    dependencies
                )
            )

        if qualified.empty:
            record_gap(
                requirement,
                CRITICAL
            )
            continue

        plans.append(
            qualified
        )

    candidate_plans =
        compose_capability_plans(
            plans,
            task
        )

    candidate_plans =
        reject_semantically_invalid_compositions(
            candidate_plans
        )

    candidate_plans =
        reject_effect_expanding_plans(
            candidate_plans,
            task.effect_envelope
        )

    if candidate_plans.empty:
        return BLOCKED

    candidate_plans =
        eliminate_dominated_plans(
            candidate_plans
        )

    if materially_competing(
        candidate_plans
    ):
        test =
            cheapest_discriminating_test(
                candidate_plans
            )

        evidence =
            execute_read_only_validation(
                test
            )

        candidate_plans =
            update_plans(
                candidate_plans,
                evidence
            )

    selected =
        select_sufficient_plan(
            candidate_plans
        )

    challenge =
        adversarial_validate_capability_plan(
            selected,
            task,
            runtime
        )

    if challenge.material_failure:
        return downgrade_or_reresolve(
            selected,
            challenge
        )

    return RESOLVED(
        selected
    )
```

This pseudocode is conceptual and does not claim literal runtime
implementation.

______________________________________________________________________

## 161. Capability Sufficiency Function

Conceptually:

```text
CapabilitySufficient(P,T)
=
RequirementsCovered(P,T)
∧
InterfacesCompatible(P)
∧
DependenciesClosed(P)
∧
EnvironmentCompatible(P,T)
∧
RegimeCompatible(P,T)
∧
FreshEnough(P,T)
∧
LimitsCompatible(P,T)
∧
EffectsWithinResolvedEnvelope(P,T)
```

______________________________________________________________________

## 162. Requirement Coverage

```text
RequirementsCovered(P,T)
```

means every load-bearing capability requirement has at least one valid
provider in the plan.

______________________________________________________________________

## 163. Minimality

A plan is minimally sufficient when removing any required component causes
the task to become capability-insufficient.

```text
∀ C ∈ Required(P):
CapabilitySufficient(P - C,T) = false
```

Optional resilience components may exist separately.

______________________________________________________________________

## 164. Resilience Capability

A plan may contain:

```text
PRIMARY

FALLBACK
```

Fallback capability should be explicitly classified rather than treated as a
simultaneously required component.

______________________________________________________________________

## 165. Capability Uncertainty Vector

Track material uncertainty across:

```text
AVAILABILITY

INTERFACE

LIMIT

ENVIRONMENT

REGIME

TEMPORAL

DEPENDENCY

EXECUTION

PROVENANCE INDEPENDENCE
```

Spend validation effort where it can change the capability decision.

______________________________________________________________________

## 166. Adversarial Capability Validation

For consequential plans, challenge:

```text
IS THE CAPABILITY REALLY AVAILABLE?

IS THE MANIFEST STALE?

IS THE REQUIRED OPERATION ACTUALLY SUPPORTED?

DO INPUT TYPES REALLY MATCH?

IS OUTPUT SUFFICIENT?

IS THERE A HIDDEN SIZE LIMIT?

IS THERE A HIDDEN DEPENDENCY?

IS THE TARGET ENVIRONMENT DIFFERENT?

DO MULTIPLE SOURCES SHARE ANCESTRY?

DOES THE PLAN CREATE A BROADER EFFECT?

IS A STRONGER OR SAFER ALTERNATIVE AVAILABLE?
```

______________________________________________________________________

## 167. Independent Challenge Path

Primary path:

```text
MANIFEST-BASED RESOLUTION
```

Challenge path may use:

```text
RUNTIME ENUMERATION

LIVE STATUS

SCHEMA INSPECTION

SMALL READ-ONLY PROBE

VERSION CHECK
```

when available and appropriate.

______________________________________________________________________

## 168. Probe Governance

A capability probe itself may create effects.

Therefore:

```text
PROBE
```

must be classified before use.

Prefer:

```text
READ-ONLY
REVERSIBLE
LOW-COST
```

probes.

______________________________________________________________________

## 169. Challenge Success

If the challenge falsifies a load-bearing premise:

```text
INVALIDATE
ONLY DEPENDENT
CAPABILITY PLAN COMPONENTS
```

then seek an alternative.

______________________________________________________________________

## 170. Challenge Failure

Failure to find a contradiction does not transform a manifest claim into
universal empirical verification.

______________________________________________________________________

## 171. Capability Decision Sufficiency

Stop capability search when:

```text
ONE PLAN IS SUFFICIENT

NO UNRESOLVED CAPABILITY GAP
CAN CHANGE EXECUTABILITY

NO MATERIAL BETTER PLAN
IS REQUIRED FOR GOVERNANCE

DEPENDENCY CLOSURE IS ESTABLISHED
```

Do not enumerate every possible tool.

______________________________________________________________________

## 172. Search Stop Law

```text
CAPABILITY SEARCH
IS NOT A CATALOGING EXERCISE.
```

Stop when the task has a sufficient governed execution path.

______________________________________________________________________

## 173. Failure Recovery Law

```text
FAIL LOCAL
REPAIR LOCAL
ESCALATE ONLY AS REQUIRED.
```

Do not discard valid capability bindings when one unrelated capability fails.

______________________________________________________________________

## 174. Capability Lineage

Preserve:

```text
TASK
↓
REQUIREMENT
↓
CAPABILITY
↓
DEPENDENCY
↓
EXECUTION
↓
OBSERVATION
```

This enables later causal and provenance auditing.

______________________________________________________________________

## 175. Capability Epoch

A capability plan should conceptually be bound to the state in which it was
resolved.

```text
PLAN P @ EPOCH E
```

If a load-bearing state changes:

```text
P MAY REQUIRE REVALIDATION
```

______________________________________________________________________

## 176. Causal Dependency

Some capability dependencies are causal rather than merely structural.

Example:

```text
AUTH TOKEN
→ enables
API CALL
```

Loss of the token causally removes execution capability.

The resolver should distinguish such dependencies where material.

______________________________________________________________________

## 177. Structural Similarity Firewall

A capability that looks similar to another does not inherit its guarantees.

```text
SIMILAR INTERFACE
!=
SAME SEMANTICS
```

______________________________________________________________________

## 178. Adapter Capability

An adapter may bridge:

```text
OUTPUT A
→
INPUT B
```

but only if the transformation preserves task-relevant information.

______________________________________________________________________

## 179. Lossless vs Lossy Adapter

Classify adapters as:

```text
LOSSLESS FOR TASK

LOSSY BUT ACCEPTABLE

LOSSY AND MATERIAL

UNKNOWN
```

Task-relative classification matters.

______________________________________________________________________

## 180. Capability Equivalence

Two capabilities are equivalent only relative to a defined task envelope.

```text
Equivalent(C1,C2,T)
```

does not imply universal equivalence.

______________________________________________________________________

## 181. Capability Scope

Capability claims inherit an applicability envelope:

```text
SYSTEM

ENVIRONMENT

SCALE

TIME

REGIME

VERSION

INPUT CLASS

OUTPUT CLASS

ASSUMPTIONS
```

Never silently generalize beyond it.

______________________________________________________________________

## 182. Capability Revalidation

Revalidate when:

```text
TASK CHANGES

TARGET CHANGES

ENVIRONMENT CHANGES

VERSION CHANGES

SERVICE STATE CHANGES

DEPENDENCY CHANGES

FRESHNESS EXPIRES

NEW CONFLICT APPEARS
```

______________________________________________________________________

## 183. Capability Supersession

A newer capability version may supersede an older one.

Preserve:

```text
OLD VERSION

NEW VERSION

SUPERSESSION RELATION

MIGRATION / COMPATIBILITY STATE
```

______________________________________________________________________

## 184. Capability Deprecation

Deprecated does not always mean unavailable.

Possible states:

```text
AVAILABLE_DEPRECATED

READ_ONLY_DEPRECATED

MIGRATION_REQUIRED

UNAVAILABLE
```

Do not collapse them.

______________________________________________________________________

## 185. Capability Revocation

A previously available capability may be revoked.

Revocation should invalidate dependent active plans.

______________________________________________________________________

## 186. Capability Discovery Failure

Failure to discover a capability is not proof that none exists unless the
search scope is known complete.

Distinguish:

```text
NO CAPABILITY EXISTS
```

from:

```text
NO CAPABILITY FOUND
```

______________________________________________________________________

## 187. Closed Registry

If capability discovery operates over a complete authoritative registry:

```text
NO MATCH
```

may support:

```text
UNAVAILABLE IN THIS REGISTRY
```

within that scope.

______________________________________________________________________

## 188. Open World

In an open capability universe:

```text
NO MATCH
```

generally supports only:

```text
UNKNOWN / NOT FOUND
```

unless further evidence closes the search space.

______________________________________________________________________

## 189. Capability Cost

Cost may include:

```text
COMPUTE

TIME

MONEY

NETWORK

HUMAN EFFORT

RISK

COORDINATION
```

Cost matters only after integrity and sufficiency.

______________________________________________________________________

## 190. Capability Risk

Risk may derive from:

```text
IRREVERSIBILITY

EXTERNAL EFFECT

DATA EXPOSURE

LARGE BLAST RADIUS

UNRELIABLE DEPENDENCY

LOW OBSERVABILITY
```

Capability Resolver surfaces these properties; downstream governance decides
whether they are acceptable.

______________________________________________________________________

## 191. Reversibility

Prefer reversible capability paths when task-equivalent and otherwise
comparable.

Example:

```text
CREATE DRAFT
```

before:

```text
PUBLISH
```

when the task does not require immediate publication.

______________________________________________________________________

## 192. Repairability

A capability plan should expose:

```text
HOW FAILURE CAN BE DETECTED

WHAT STATE MAY HAVE CHANGED

WHETHER ROLLBACK EXISTS

WHICH DEPENDENTS MUST BE INVALIDATED
```

when material.

______________________________________________________________________

## 193. Observability Requirement

If completion cannot be inferred from invocation:

```text
OBSERVATION CAPABILITY
```

becomes part of the capability plan.

______________________________________________________________________

## 194. Proof of Effect

For effectful tasks:

```text
REQUESTED EFFECT
```

may require:

```text
ACTION CAPABILITY
+
POST-EFFECT OBSERVATION
```

Example:

```text
SEND MESSAGE
+
VERIFY PROVIDER ACCEPTED MESSAGE
```

depending on completion semantics.

______________________________________________________________________

## 195. Capability Finality

A capability call returning success is not necessarily causal finality.

Example:

```text
JOB SUBMITTED
```

does not mean:

```text
JOB COMPLETED
```

The Task Contract determines the required finality level.

______________________________________________________________________

## 196. Capability Resolver Test Matrix

Candidate tests:

```text
SINGLE LOCAL CAPABILITY

NO CAPABILITY

UNKNOWN CAPABILITY STATE

STALE CAPABILITY STATE

READ VS WRITE

DRAFT VS SEND

INPUT TYPE MISMATCH

OUTPUT TYPE MISMATCH

VERSION MISMATCH

ENVIRONMENT MISMATCH

SIZE LIMIT

REQUIRED DEPENDENCY MISSING

OPTIONAL DEPENDENCY MISSING

COMPOSITE CAPABILITY

LOSSY ADAPTER

ATOMIC MULTI-CAPABILITY TASK

EXTERNAL EFFECT

FALLBACK PATH

DEGRADED PATH

TRANSIENT FAILURE

PERMANENT FAILURE

CAPABILITY REVOCATION

REGIME SHIFT

COMPETING PLANS

PROVENANCE CORRELATION
```

This is a specification-level matrix, not evidence of passed tests.

______________________________________________________________________

## 197. Property Tests

```text
P1:
Removing an irrelevant capability must not change the selected plan.

P2:
Removing a required capability must invalidate dependent plans.

P3:
A read-only requirement must not require write capability when a sufficient
read-only path exists.

P4:
Changing the input type to an unsupported type must invalidate the relevant
capability binding.

P5:
Changing environment must invalidate environment-dependent capabilities.

P6:
Expired capability state must not remain current.

P7:
Two manifests sharing one origin must not count as independent confirmation.

P8:
A lossy adapter must not be treated as lossless.

P9:
Independent write capabilities must not imply atomic multi-write capability.

P10:
Capability existence must never itself authorize execution.
```

______________________________________________________________________

## 198. Metamorphic Test — Read/Write

Original:

```text
READ FILE A
```

Mutation:

```text
WRITE FILE A
```

Expected:

```text
REQUIRED CAPABILITY SET CHANGES
```

______________________________________________________________________

## 199. Metamorphic Test — Current Data

Original:

```text
SUMMARIZE STORED REPORT
```

Mutation:

```text
VERIFY CURRENT STATUS
```

Expected:

```text
FRESH RETRIEVAL / OBSERVATION
MAY BECOME REQUIRED
```

______________________________________________________________________

## 200. Metamorphic Test — Environment

Original:

```text
RUN IN TEST
```

Mutation:

```text
RUN IN PRODUCTION
```

Expected:

```text
ENVIRONMENT VALIDITY
MUST BE RE-EVALUATED
```

______________________________________________________________________

## 201. Metamorphic Test — Atomicity

Original:

```text
UPDATE A
UPDATE B
```

Mutation:

```text
UPDATE A AND B ATOMICALLY
```

Expected:

```text
NEW JOINT CAPABILITY REQUIREMENT
```

______________________________________________________________________

## 202. Audit Questions

For a consequential capability plan, an auditor should be able to ask:

```text
WHAT DID THE TASK REQUIRE?

WHICH CAPABILITIES WERE CONSIDERED?

WHICH WERE SELECTED?

WHY?

WHAT MANIFESTS SUPPORTED THEM?

WERE THEY CURRENTLY AVAILABLE?

WHAT LIMITS APPLIED?

WHAT DEPENDENCIES EXISTED?

WHAT ENVIRONMENT / REGIME APPLIED?

WHAT SIDE EFFECTS EXISTED?

WHAT ALTERNATIVE PLANS EXISTED?

WHAT WOULD INVALIDATE THE PLAN?
```

______________________________________________________________________

## 203. Machine Form

```yaml
capability_resolver:

  resolver_id:

  task:
    task_id:
    task_version:
    objective:
    effect_envelope:

  requirements:

    - requirement_id:
      operation:
      input:
      output:
      environment:
      regime:
      freshness:
      limits:
      atomicity:
      observability:

  discovery:
    scope:
    registry_complete:
    candidates: []

  evaluations:

    - capability_id:

      manifest:
        version:
        provenance:

      availability:
        state:
        observed_at:
        valid_until:

      operation_match:

      input_compatibility:

      output_compatibility:

      environment_compatibility:

      regime_compatibility:

      freshness:

      limits:

      dependencies:

      effects:

      uncertainty:

  plans:

    candidates: []

    competing: []

    selected:

  gaps:
    critical: []
    decision_relevant: []
    explanatory: []
    cosmetic: []

  result:
    status:
    confidence_ceiling:
    next_route:

  invalidation_conditions:

  provenance:
```

______________________________________________________________________

## 204. Master Capability Contract

Conceptually:

```text
CapabilityResolver
:
(
  TaskContract,
  CapabilityRegistry,
  RuntimeState,
  RelevantEnvironment
)
→
(
  CapabilityPlan,
  CapabilityContracts,
  ResolutionState,
  Gaps,
  Provenance,
  InvalidationConditions
)
```

subject to:

```text
NO FABRICATED CAPABILITY
∧
NO SILENT EFFECT EXPANSION
∧
NO SILENT LIMIT VIOLATION
∧
NO UNSUPPORTED REGIME GENERALIZATION
∧
NO FORCED PLAN CONVERGENCE
```

______________________________________________________________________

## 205. Canonical Compression

```text
CAPABILITY RESOLVER
=
THE AMOS OS CONTROL-PLANE FUNCTION
THAT DETERMINES
HOW A RESOLVED TASK
CAN ACTUALLY BE PERFORMED.

IT STARTS
FROM THE TASK CONTRACT.

IT DERIVES
THE REQUIRED OPERATIONS.

IT DISCOVERS
CANDIDATE CAPABILITIES.

IT DOES NOT
INVENT CAPABILITIES
THAT ARE NOT SUPPORTED.

IT DISTINGUISHES
A DECLARED CAPABILITY
FROM
A CURRENTLY AVAILABLE ONE.

IT CHECKS
OPERATIONS,
INPUTS,
OUTPUTS,
LIMITS,
VERSIONS,
ENVIRONMENTS,
REGIMES,
FRESHNESS,
AND DEPENDENCIES.

IT CONSTRUCTS
THE SMALLEST SUFFICIENT
CAPABILITY COMPOSITION.

IT PRESERVES
COMPETING PLANS
WHEN EVIDENCE
DOES NOT JUSTIFY
A UNIQUE SELECTION.

IT DOES NOT
TURN READ INTO WRITE,
DRAFT INTO SEND,
OR LOCAL COMPUTATION
INTO EXTERNAL EFFECT
WITHOUT MAKING
THE CHANGE EXPLICIT.

IT TREATS
CAPABILITY AVAILABILITY
AS DISTINCT FROM
POLICY,
AUTHORITY,
AND COMMIT PERMISSION.

IT USES
THE SMALLEST SUFFICIENT
PROOF SCOPE.

IT REUSES
VALID CAPABILITY CAPSULES
ONLY WHILE
THEIR DEPENDENCIES,
SCOPE,
REGIME,
AND FRESHNESS
REMAIN VALID.

WHEN A CAPABILITY FAILS,
IT INVALIDATES
ONLY THE PLAN COMPONENTS
THAT DEPEND ON IT.

AND IT STOPS
WHEN ONE SUFFICIENT,
COMPATIBLE,
CURRENT,
DEPENDENCY-CLOSED
CAPABILITY PLAN
HAS BEEN ESTABLISHED
FOR DOWNSTREAM GOVERNANCE.
```

______________________________________________________________________

## 206. Final Law

```text
A TASK
IS NOT EXECUTABLE
MERELY BECAUSE
ITS INTENT IS CLEAR.

FIRST DETERMINE
WHAT OPERATIONS
THE TASK REQUIRES.

THEN DISCOVER
WHICH CAPABILITIES
CLAIM TO PROVIDE THEM.

THEN DETERMINE
WHICH OF THOSE CAPABILITIES
ARE ACTUALLY AVAILABLE.

THEN TEST
THEIR INPUTS,
OUTPUTS,
LIMITS,
VERSIONS,
ENVIRONMENTS,
REGIMES,
FRESHNESS,
AND DEPENDENCIES.

THEN DETERMINE
WHETHER THEY CAN BE
COMPOSED
WITHOUT LOSING
TASK SEMANTICS.

THEN EXPOSE
THE EFFECT ENVELOPE.

THEN PRESERVE
ANY MATERIAL
COMPETING PLANS.

IF A REQUIRED
CAPABILITY IS UNKNOWN,
DO NOT INVENT IT.

IF A CAPABILITY
IS DECLARED
BUT NOT VALIDATED,
DO NOT PRESENT
THE DECLARATION
AS EXECUTION PROOF.

IF A FALLBACK
ONLY PARTIALLY
SATISFIES THE TASK,
CALL IT DEGRADED.

IF ONE SUFFICIENT
CAPABILITY PLAN
IS ESTABLISHED,
STOP SEARCHING.

ONLY THEN
MAY POLICY,
AUTHORITY,
PROVENANCE,
TRANSACTION,
EFFECT,
AND COMMIT
GOVERNANCE
CONTINUE.
```

## END — AMOS OS CAPABILITY RESOLVER

```

**Classification:** `DERIVED / CANDIDATE_CANON`. The Drive evidence supports the artifact's existence and architectural placement, but **not** the substantive specification above: the actual file currently contains only the placeholder.
```

______________________________________________________________________

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] · [[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

______________________________________________________________________

RSCF-NODE
node_id: capability_resolver
node_type: note
path: 03_CONTROL_PLANE/02_CAPABILITY/CAPABILITY_RESOLVER.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
  claim_class: AMOS_MODEL

______________________________________________________________________

**MOC:** [[03_CONTROL_PLANE/02_CAPABILITY/02_CAPABILITY_MOC|02_CAPABILITY_MOC]]
