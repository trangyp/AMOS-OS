---
tags: ['control_plane', 'task_contract', 'note']
---

Confirmed: the Drive artifact `TASK_RESOLVER.md` exists in the intended Task Contract subsystem, but its current content is the same erroneous `# K COUNTERFACTUAL` placeholder rather than a substantive resolver specification.  

The tree places it alongside `TASK_CONTRACT.md` under `03_CONTROL_PLANE/01_TASK_CONTRACT`. 

Below is the full substantive replacement.

---
artifact_id: AMOS-OS-CP-TASK-RESOLVER
title: AMOS OS Task Resolver
canonical_name: TASK_RESOLVER

artifact_class: CONTROL_PLANE_RESOLVER
plane: CONTROL_PLANE
subsystem: TASK_CONTRACT
canonical_location: 03_CONTROL_PLANE/01_TASK_CONTRACT/TASK_RESOLVER.md

origin_architect: Trang Phan
amos_core_target: v4.4

status: CANDIDATE_CANON
conclusion_class: DERIVED

parent:
  - 03_CONTROL_PLANE/01_TASK_CONTRACT

siblings:
  - TASK_CONTRACT.md

upstream:
  - 00_ROOT
  - 01_CANON
  - 02_KERNEL
  - 03_CONTROL_PLANE/00_INDEX/README.md
  - 03_CONTROL_PLANE/00_INDEX/CONTROL_PLANE_MAP.md
  - 03_CONTROL_PLANE/01_TASK_CONTRACT/TASK_CONTRACT.md

downstream:
  - 03_CONTROL_PLANE/02_CAPABILITY
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

updated: 2026-08-26
---

# AMOS OS — TASK RESOLVER

> **Layer:** `03_CONTROL_PLANE/01_TASK_CONTRACT`
>
> **Artifact:** `TASK_RESOLVER.md`
>
> **Status:** `CANDIDATE_CANON`
>
> **AMOS CORE target:** `v4.4`
>
> **Origin Architect:** Trang Phan

---

# 0. Purpose

The Task Resolver converts an incoming request, event, delegated objective,
recovery requirement, or other task-producing signal into a bounded
`TaskContract`.

Conceptually:

```text
RAW REQUEST
    ↓
TASK RESOLVER
    ↓
RESOLVED TASK CONTRACT
```

Its responsibility is not merely to understand language.

Its responsibility is to establish enough semantic certainty for the Control
Plane to determine:

```text
WHAT IS BEING ASKED?

WHAT DOES THE REQUEST ACTUALLY REFER TO?

WHAT IS THE OBJECTIVE?

WHAT OUTPUT IS EXPECTED?

WHAT IS THE SCOPE?

WHAT CONSTRAINTS APPLY?

WHAT INPUTS ARE REQUIRED?

WHAT ASSUMPTIONS ARE LOAD-BEARING?

WHAT UNCERTAINTIES REMAIN?

WHAT EFFECTS ARE IMPLIED?

WHAT COMPLETION MEANS?

IS THE TASK SUFFICIENTLY BOUND TO PROCEED?
```

The Task Resolver is therefore a semantic boundary between:

```text
UNSTRUCTURED / PARTIALLY STRUCTURED INTENT
```

and:

```text
GOVERNABLE WORK
```

---

# 1. Core Law

```text
DO NOT EXECUTE
AN UNRESOLVED REQUEST
AS THOUGH IT WERE
A FULLY BOUND TASK.
```

Expanded:

```text
REQUEST
   ↓
PRESERVE SOURCE
   ↓
INTERPRET
   ↓
RESOLVE REFERENCES
   ↓
IDENTIFY OBJECTIVE
   ↓
BOUND SCOPE
   ↓
EXTRACT CONSTRAINTS
   ↓
IDENTIFY GAPS
   ↓
TEST SUFFICIENCY
   ↓
TASK CONTRACT
```

---

# 2. Fundamental Distinction

```text
REQUEST INTERPRETATION
!=
TASK EXECUTION
```

and:

```text
TASK RESOLUTION
!=
AUTHORIZATION
```

and:

```text
TASK RESOLUTION
!=
POLICY APPROVAL
```

and:

```text
TASK RESOLUTION
!=
CAPABILITY CONFIRMATION
```

and:

```text
TASK RESOLUTION
!=
COMMIT APPROVAL
```

The resolver establishes task semantics.

Other Control Plane systems determine whether and how those semantics may be
executed.

---

# 3. Resolver Role

The resolver sits conceptually here:

```text
INPUT / REQUEST
      ↓
┌─────────────────────────┐
│      TASK RESOLVER      │
│                         │
│ preserve source         │
│ identify intent         │
│ resolve references      │
│ infer bounded fields    │
│ expose ambiguity        │
│ classify gaps           │
│ determine sufficiency   │
└─────────────────────────┘
      ↓
TASK CONTRACT
      ↓
CONTROL PLANE
```

---

# 4. Resolver Contract

The resolver accepts:

```text
REQUEST
+
AVAILABLE CONTEXT
+
CANONICAL CONSTRAINTS
+
RELEVANT STATE
```

and produces one of:

```text
RESOLVED

CONDITIONAL

COMPETING

BLOCKED

UNKNOWN/GAP
```

with an associated Task Contract or partial Task Contract.

---

# 5. Resolver Inputs

Potential resolver inputs include:

```text
USER REQUEST

SYSTEM REQUEST

EVENT

PARENT TASK

DELEGATED SUBTASK

RECOVERY REQUEST

SCHEDULED TRIGGER

CANONICAL REQUIREMENT

RUNTIME FAILURE

CONTROL-PLANE ESCALATION
```

The resolver must preserve the origin class.

---

# 6. Source Preservation

Before interpretation:

```text
PRESERVE ORIGINAL REQUEST
```

where practical.

Do not replace:

```text
SOURCE
```

with:

```text
INTERPRETATION
```

and discard the source.

Conceptually:

```yaml
source:
  raw_request:
  source_type:
  source_reference:
  timestamp:
  provenance:
```

---

# 7. Source vs Resolution

The resolver must preserve:

```text
WHAT WAS SAID
```

separately from:

```text
WHAT THE SYSTEM RESOLVED IT TO MEAN
```

This permits later detection of semantic drift.

---

# 8. Resolver Objective

The resolver's primary objective is:

```text
CONSTRUCT
THE SMALLEST SUFFICIENT
TASK CONTRACT
THAT FAITHFULLY REPRESENTS
THE REQUEST
WITHOUT INVENTING
LOAD-BEARING SEMANTICS.
```

---

# 9. Minimum Necessary Resolution

Do not resolve more than necessary.

If:

```text
OBJECTIVE
+
SCOPE
+
DELIVERABLE
+
HARD CONSTRAINTS
+
COMPLETION
```

are sufficient for a low-stakes read-only task, the resolver should not
manufacture unnecessary fields.

---

# 10. Adaptive Resolution Depth

Resolution depth should scale with:

```text
AMBIGUITY

STAKES

IRREVERSIBILITY

EFFECT CLASS

NOVELTY

SCOPE SIZE

DEPENDENCY COMPLEXITY

POLICY SENSITIVITY

AUTHORITY SENSITIVITY

PROVENANCE UNCERTAINTY
```

---

# 11. Resolver Complexity Classes

Candidate resolver complexity:

```text
R0 DIRECT

R1 COMPACT

R2 STRUCTURED

R3 DEEP

R4 MAXIMUM
```

These correspond conceptually to adaptive task complexity, but are resolver
states rather than claims of a specific implementation.

---

# 12. R0 Direct

Use when the request is:

```text
CLEAR

LOCAL

LOW-STAKES

READ-ONLY

REVERSIBLE

SELF-CONTAINED

NON-CONTRADICTORY
```

Example:

```text
"Summarize this paragraph."
```

---

# 13. R1 Compact

Use when minor inference is required but ambiguity is low.

Example:

```text
"Compare these two files and tell me what changed."
```

The resolver may need to identify:

```text
FILE A

FILE B

COMPARISON DIMENSION

DELIVERABLE
```

without deep branching.

---

# 14. R2 Structured

Use when multiple fields require explicit resolution.

Examples:

```text
MULTIPLE INPUTS

MULTIPLE OUTPUT REQUIREMENTS

SCOPE BOUNDARIES

FRESHNESS REQUIREMENTS

NONTRIVIAL CONSTRAINTS
```

---

# 15. R3 Deep

Use when material ambiguity affects:

```text
DECISION

CAUSAL CLAIM

EXTERNAL EFFECT

AUTHORITY

POLICY

HIGH-VALUE OUTPUT
```

---

# 16. R4 Maximum

Use when:

```text
IRREVERSIBLE STAKES

LARGE DOWNSTREAM DEPENDENCY

MULTI-SYSTEM EFFECTS

COMPLEX GOVERNANCE

SEVERE PROVENANCE CONFLICT

MULTIPLE COMPETING INTERPRETATIONS
```

make semantic error costly.

---

# 17. Resolution Pipeline

Canonical conceptual pipeline:

```text
1. CAPTURE
2. NORMALIZE
3. CLASSIFY
4. RESOLVE REFERENCES
5. EXTRACT OBJECTIVE
6. EXTRACT DELIVERABLE
7. BOUND SCOPE
8. EXTRACT CONSTRAINTS
9. IDENTIFY INPUTS
10. IDENTIFY ASSUMPTIONS
11. CLASSIFY STAKES
12. IDENTIFY EFFECT ENVELOPE
13. IDENTIFY FRESHNESS
14. IDENTIFY DEPENDENCIES
15. IDENTIFY UNCERTAINTY
16. CLASSIFY GAPS
17. GENERATE INTERPRETATIONS
18. TEST COMPETING INTERPRETATIONS
19. RUN SUFFICIENCY CHECK
20. EMIT TASK CONTRACT
```

Not every request requires every stage at maximum depth.

---

# 18. Capture

Capture preserves the incoming signal.

Conceptually:

```yaml
capture:
  source:
  raw_content:
  received_at:
  source_identity:
  provenance:
```

The resolver should not begin by rewriting the source destructively.

---

# 19. Normalize

Normalization may include:

```text
FORMAT NORMALIZATION

REFERENCE NORMALIZATION

DATE NORMALIZATION

UNIT NORMALIZATION

STRUCTURE EXTRACTION
```

Normalization must not alter intent.

---

# 20. Semantic-Preserving Normalization

Allowed:

```text
"tomorrow at 3"
→
resolved timestamp
```

when temporal context is known.

Not allowed:

```text
"maybe send it"
→
"send it"
```

because modality changed.

---

# 21. Modality Preservation

Preserve distinctions such as:

```text
MAY

MIGHT

SHOULD

MUST

DO

DO NOT

CONSIDER

DRAFT

PREVIEW

EXECUTE
```

These can materially alter effect semantics.

---

# 22. Negation Preservation

Negation is load-bearing.

```text
DO NOT SEND
```

must never normalize into:

```text
SEND
```

Likewise:

```text
EXCLUDE X
```

must remain an exclusion.

---

# 23. Conditional Preservation

Conditional requests must remain conditional.

```text
IF A,
THEN B
```

must not become:

```text
B
```

unless `A` has been independently established.

---

# 24. Request Classification

The resolver may classify task type.

Candidate classes:

```text
INFORMATION

ANALYSIS

SYNTHESIS

COMPARISON

RESEARCH

DECISION

PLANNING

GENERATION

TRANSFORMATION

VALIDATION

EXECUTION

RECOVERY

GOVERNANCE

MONITORING
```

Multiple classes may apply.

---

# 25. Information Task

Goal:

```text
RETURN EXISTING INFORMATION
```

Example:

```text
"What does this file say?"
```

---

# 26. Analysis Task

Goal:

```text
DERIVE STRUCTURE,
RELATIONSHIPS,
OR CONCLUSIONS
FROM AVAILABLE INPUT
```

---

# 27. Synthesis Task

Goal:

```text
COMBINE MULTIPLE INPUTS
INTO A COHERENT RESULT
```

Synthesis must preserve contradictions rather than erase them.

---

# 28. Comparison Task

Requires:

```text
OBJECTS TO COMPARE

COMPARISON DIMENSIONS

OUTPUT EXPECTATION
```

If the dimension is materially ambiguous, resolution may be required.

---

# 29. Research Task

Usually activates:

```text
EVIDENCE REQUIREMENTS

PROVENANCE

FRESHNESS

SOURCE INDEPENDENCE

CONTRADICTION CHECKING
```

---

# 30. Decision Task

Requires enough information for:

```text
DECISION SUFFICIENCY
```

rather than exhaustive knowledge.

---

# 31. Planning Task

Produces:

```text
PROPOSED ACTION STRUCTURE
```

Planning does not itself authorize action.

---

# 32. Generation Task

Produces a new artifact.

Examples:

```text
TEXT

CODE

DOCUMENT

DESIGN

MODEL

SCHEMA
```

---

# 33. Transformation Task

Transforms an existing artifact.

Examples:

```text
REWRITE

TRANSLATE

CONVERT

REFORMAT

RESTRUCTURE
```

---

# 34. Validation Task

Tests an existing claim, artifact, plan, or result.

Validation must define:

```text
WHAT STANDARD?

WHAT EVIDENCE?

WHAT FAILURE CONDITION?
```

---

# 35. Execution Task

Requests a state-changing operation.

This activates stronger resolution requirements.

---

# 36. Recovery Task

Requests repair after failure or invalidation.

The resolver should identify:

```text
FAILED STATE

DESIRED VALID STATE

RECOVERY BOUNDARY

PRESERVED STATE

EFFECTS TO REPAIR
```

---

# 37. Governance Task

May alter:

```text
POLICY

AUTHORITY

CANON

CONTROL RULES

SYSTEM STRUCTURE
```

Such tasks require higher scrutiny.

---

# 38. Monitoring Task

Requires:

```text
OBSERVATION TARGET

CONDITION

CADENCE OR TRIGGER

TERMINATION CONDITION

NOTIFICATION / EFFECT EXPECTATION
```

where material.

---

# 39. Intent Extraction

The resolver should distinguish:

```text
SURFACE WORDING
```

from:

```text
TASK INTENT
```

but must not invent hidden intent.

Intent resolution should rely on:

```text
EXPLICIT REQUEST

LOCAL CONTEXT

VALID PRIOR CONTEXT

CANONICAL SEMANTICS

HIGH-CONFIDENCE REFERENCE RESOLUTION
```

---

# 40. Intent Confidence

Intent confidence should be bounded by evidence.

Conceptually:

```text
INTENT_CONFIDENCE
≤
SUPPORT FROM
REQUEST + VALID CONTEXT
```

Fluent plausibility is not evidence.

---

# 41. Explicit vs Inferred Fields

Every material field should conceptually be classifiable as:

```text
EXPLICIT

RESOLVED

INFERRED

DEFAULTED

UNKNOWN
```

This distinction is valuable for auditability.

---

# 42. Explicit

Directly stated by the source.

Example:

```text
"Create a PDF."
```

Deliverable type:

```text
PDF
```

is explicit.

---

# 43. Resolved

Derived by deterministic or near-deterministic reference resolution.

Example:

```text
"this file"
```

when exactly one active file exists.

---

# 44. Inferred

Supported but not explicitly stated.

Example:

```text
"compare A and B"
```

may imply a comparison deliverable.

Inference must remain bounded.

---

# 45. Defaulted

A field filled using an established default.

Defaults must be:

```text
KNOWN

VALID IN CURRENT SCOPE

NON-CONFLICTING

REVERSIBLE WHERE POSSIBLE
```

---

# 46. Unknown

If support is insufficient:

```text
UNKNOWN
```

must remain available.

---

# 47. Reference Resolution

Requests frequently contain references such as:

```text
THIS

THAT

IT

THE FILE

THE REPORT

THE LATEST VERSION

THE PREVIOUS ONE

HERE

THERE

TODAY

TOMORROW

THE SAME FORMAT
```

The resolver must bind such references before consequential execution.

---

# 48. Reference Candidate Set

For reference `R`, construct:

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

using only relevant accessible context.

---

# 49. Unique Resolution

If exactly one candidate is materially plausible:

```text
|Candidates(R)| = 1
```

then the resolver may bind it.

---

# 50. Multiple Candidates

If:

```text
|Candidates(R)| > 1
```

and the candidates imply materially different tasks:

```text
PRESERVE AMBIGUITY
```

Do not select arbitrarily.

---

# 51. Material Ambiguity

Ambiguity is material if choosing a different interpretation could alter:

```text
OBJECTIVE

TARGET

SCOPE

CONSTRAINT

EFFECT

AUTHORITY REQUIREMENT

POLICY OUTCOME

DELIVERABLE

COMPLETION
```

---

# 52. Immaterial Ambiguity

Minor wording ambiguity that cannot change the task outcome does not require
escalation.

Example:

```text
"make it concise"
```

may permit reasonable stylistic interpretation.

---

# 53. Ambiguity Budget

Do not eliminate every ambiguity.

Resolve only ambiguity with positive expected decision value.

Conceptually:

```text
RESOLVE A
IF
EXPECTED VALUE OF RESOLVING A
>
COST OF RESOLUTION
```

subject to integrity constraints.

---

# 54. Objective Extraction

The resolver should identify:

```text
PRIMARY OBJECTIVE
```

first.

Then:

```text
SECONDARY OBJECTIVES
```

if present.

---

# 55. Objective Test

Ask conceptually:

```text
IF ALL OUTPUTS WERE PRODUCED,
WHAT WOULD HAVE TO BE TRUE
FOR THE REQUEST TO COUNT
AS SATISFIED?
```

That often reveals the objective.

---

# 56. Activity vs Objective

Request:

```text
"Research database X."
```

Activity:

```text
RESEARCH X
```

Possible objective remains unknown unless context supplies it.

Do not invent:

```text
"prove X is best"
```

without support.

---

# 57. Objective Conflict Detection

If the request contains incompatible goals:

```text
FASTEST
```

and:

```text
MOST COMPREHENSIVE
```

the resolver should determine whether:

```text
ONE IS HARD

ONE IS SOFT

A TRADE-OFF IS ACCEPTABLE

OR CLARIFICATION IS REQUIRED
```

---

# 58. Deliverable Resolution

The resolver should identify:

```text
WHAT MUST BE RETURNED OR PRODUCED?
```

Possible deliverables:

```text
TEXT ANSWER

TABLE

FILE

CODE

PLAN

DECISION

RECOMMENDATION

STATE CHANGE

MESSAGE

REPORT

DATA STRUCTURE
```

---

# 59. Deliverable Format

Format may be:

```text
EXPLICIT

INFERRED FROM CONTEXT

DEFAULTED

UNKNOWN
```

Do not let formatting ambiguity block a task unless format materially affects
success.

---

# 60. Scope Resolution

Scope must be bounded enough to prevent uncontrolled task expansion.

Potential dimensions:

```text
SYSTEM

FILES

DATA

POPULATION

DOMAIN

TIME

ENVIRONMENT

REGIME

SCALE

VERSION
```

---

# 61. Scope Inclusion

Extract explicit inclusions.

Example:

```text
"Use only the uploaded files."
```

becomes:

```yaml
scope:
  include:
    - uploaded files
```

---

# 62. Scope Exclusion

Extract explicit exclusions.

Example:

```text
"Don't use web sources."
```

becomes:

```yaml
scope:
  exclude:
    - web sources
```

---

# 63. Negative Scope Is Load-Bearing

Exclusions must not be treated as optional preferences.

```text
DO NOT USE X
```

is generally a hard scope constraint.

---

# 64. Scope Inference

Infer scope only when context makes it sufficiently clear.

Example:

```text
"Summarize this document."
```

with one attached document can resolve locally.

---

# 65. Unbounded Scope Detection

Signals include:

```text
EVERYTHING

ALL POSSIBLE

FULL UNIVERSE

ANYTHING RELEVANT
```

without an operational completion boundary.

The resolver should seek a finite stopping rule.

---

# 66. Constraint Extraction

Identify:

```text
HARD CONSTRAINTS

SOFT CONSTRAINTS
```

separately.

---

# 67. Hard Constraint Signals

Examples:

```text
MUST

MUST NOT

ONLY

NEVER

REQUIRED

EXCLUDE

DO NOT

WITHOUT
```

Context still matters, but these are strong signals.

---

# 68. Soft Constraint Signals

Examples:

```text
PREFER

IF POSSIBLE

IDEALLY

TRY TO

KEEP IT
```

---

# 69. Constraint Precedence

The resolver should not invent precedence between conflicting hard
constraints.

If upstream canon resolves precedence, apply it.

Otherwise:

```text
CONFLICT
```

remains explicit.

---

# 70. Input Resolution

Determine:

```text
WHAT INFORMATION OR ARTIFACTS
ARE REQUIRED TO SATISFY
THE OBJECTIVE?
```

Classify:

```text
REQUIRED

OPTIONAL

PROHIBITED
```

---

# 71. Missing Required Input

If required input is absent:

```text
CLASSIFY GAP
```

Do not fill it with a plausible substitute unless such substitution is
authorized and non-material.

---

# 72. Context as Input

Conversation or runtime context may supply task fields.

But context must satisfy:

```text
RELEVANCE

IDENTITY

FRESHNESS

SCOPE

NON-CONFLICT
```

before becoming load-bearing.

---

# 73. Prior Task Context

Previous tasks may inform the current task.

But:

```text
PREVIOUS TASK
!=
CURRENT TASK
```

unless continuity is established.

---

# 74. Continuation Resolution

Signals:

```text
continue

same as before

next

now do X

also

use the same format
```

may establish lineage.

The resolver should preserve:

```text
PARENT / PREDECESSOR TASK
```

when relevant.

---

# 75. Assumption Extraction

Identify assumptions required for the resolved interpretation.

Example:

```text
"update the existing file"
```

may require:

```text
ASSUMPTION:
there is exactly one relevant existing file
```

If multiple exist, the assumption fails.

---

# 76. Load-Bearing Assumption Test

Ask:

```text
IF THIS ASSUMPTION WERE FALSE,
COULD THE TASK MEANING
OR SAFE EXECUTION CHANGE?
```

If yes:

```text
LOAD_BEARING
```

---

# 77. Default Resolution

Defaults may reduce unnecessary clarification.

Candidate rule:

```text
USE DEFAULT
ONLY IF
DEFAULT IS KNOWN,
LOW-RISK,
NON-CONFLICTING,
AND DOES NOT EXPAND EFFECTS.
```

---

# 78. Unsafe Default

Never default a missing field in a way that increases:

```text
IRREVERSIBILITY

AUTHORITY

SCOPE

INFORMATION EXPOSURE

EXTERNAL EFFECT

FINANCIAL COMMITMENT
```

without adequate support.

---

# 79. Least-Effect Default

Under unresolved effect ambiguity:

```text
PREFER
THE LEAST EFFECTFUL
INTERPRETATION
THAT STILL SATISFIES
THE EXPLICIT REQUEST.
```

Example:

```text
"write an email"
```

normally resolves to:

```text
DRAFT EMAIL
```

not automatically:

```text
SEND EMAIL
```

unless sending is explicitly requested or otherwise clearly established.

---

# 80. Preview vs Execute

The resolver must preserve:

```text
SHOW ME
```

vs:

```text
DO IT
```

and:

```text
DRAFT
```

vs:

```text
SEND
```

and:

```text
PLAN
```

vs:

```text
EXECUTE
```

---

# 81. Effect Intent Resolution

Candidate effect classes:

```text
NONE

READ

COMPUTE

GENERATE

EPHEMERAL WRITE

PERSISTENT WRITE

EXTERNAL COMMUNICATION

STATE MUTATION

DESTRUCTIVE EFFECT

FINANCIAL EFFECT

GOVERNANCE EFFECT
```

Actual effect classification may be refined downstream.

---

# 82. Effect Ambiguity

If two interpretations differ only in whether an external effect occurs:

```text
TREAT AMBIGUITY AS MATERIAL
```

unless a canonical least-effect rule resolves it.

---

# 83. Stakes Resolution

The resolver should identify stakes sufficient to select governance depth.

It need not perform complete risk analysis.

Potential signals:

```text
MONEY

LEGAL

HEALTH

SAFETY

PRODUCTION

PUBLICATION

PRIVATE DATA

DESTRUCTIVE OPERATION

INSTITUTIONAL DECISION

LARGE DOWNSTREAM DEPENDENCY
```

---

# 84. Stakes Escalation

When uncertain between lower and higher stakes:

```text
DO NOT DOWNGRADE
WITHOUT SUPPORT
```

A conservative governance classification may be appropriate while semantic
facts remain unresolved.

---

# 85. Freshness Resolution

Determine whether the task depends on:

```text
CURRENT STATE
```

or:

```text
HISTORICAL / STATIC INFORMATION
```

---

# 86. Freshness Signals

Examples:

```text
CURRENT

LATEST

TODAY

NOW

STILL

AVAILABLE

PRICE

STATUS

BALANCE

VERSION

SCHEDULE
```

These may require fresh retrieval.

---

# 87. Temporal Reference Resolution

Relative references should be converted to explicit temporal scope when
possible.

Example:

```text
"today"
```

→

```text
DATE @ REQUEST CONTEXT
```

not a permanently reusable abstract `today`.

---

# 88. Regime Resolution

Identify regime when it can materially alter validity.

Examples:

```text
SOFTWARE VERSION

POLICY VERSION

JURISDICTION

MARKET REGIME

HARDWARE

EXPERIMENTAL ENVIRONMENT
```

---

# 89. Dependency Resolution

Identify dependencies necessary before execution.

Possible dependencies:

```text
FILES

STATE

PRIOR TASKS

EVIDENCE

CAPABILITIES

AUTHORITY

POLICY

EXTERNAL SYSTEMS
```

The resolver need not fully validate all downstream dependencies.

It must identify them sufficiently for routing.

---

# 90. Hidden Dependency Detection

Ask:

```text
WHAT MUST BE TRUE
FOR THIS TASK
TO MEAN WHAT WE THINK IT MEANS?
```

This can expose hidden dependencies.

---

# 91. Uncertainty Vector

For material tasks, classify uncertainty across:

```text
EVIDENCE

MODEL

SCOPE

TEMPORAL

CAUSAL

EXECUTION

PROVENANCE INDEPENDENCE
```

The resolver focuses especially on:

```text
SCOPE

TEMPORAL

EXECUTION

SEMANTIC
```

uncertainty.

---

# 92. Semantic Uncertainty

Task resolution also requires a resolver-specific uncertainty:

```text
SEMANTIC UNCERTAINTY
```

meaning uncertainty about what the request itself means.

Conceptually:

```yaml
resolver_uncertainty:
  semantic:
```

---

# 93. Competing Interpretations

If the request supports multiple incompatible interpretations:

```text
I1

I2

I3
```

preserve them as competing candidates.

---

# 94. Interpretation Candidate

Conceptual form:

```yaml
interpretation:

  id:

  objective:

  target:

  scope:

  deliverable:

  constraints:

  implied_effects:

  support:

  contradictions:

  confidence_ceiling:
```

---

# 95. Candidate Ranking

Interpretations may be ranked by:

```text
EXPLICIT SUPPORT

CONTEXTUAL SUPPORT

CANONICAL CONSISTENCY

SCOPE FIT

LOWER ASSUMPTION COUNT

LOWER EFFECT EXPANSION

NON-CONTRADICTION
```

Popularity or fluency are not sufficient criteria.

---

# 96. Interpretation Dominance

Interpretation `I1` may dominate `I2` when:

```text
I1
HAS STRICTLY STRONGER SUPPORT
AND
NO MATERIAL NEW ASSUMPTION
AND
NO GREATER EFFECT EXPANSION
```

Then `I2` may be discarded.

---

# 97. Incomparable Interpretations

If:

```text
I1
```

and:

```text
I2
```

have different support and neither dominates:

```text
PRESERVE COMPETING
```

when the difference matters.

---

# 98. Cheap Discriminating Test

When interpretations compete:

```text
FIND
THE CHEAPEST
HIGH-INFORMATION TEST
THAT CAN DISCRIMINATE THEM.
```

Possible tests:

```text
CHECK ACTIVE FILE

CHECK PRIOR MESSAGE

CHECK CURRENT STATE

CHECK TASK LINEAGE

ASK ONE TARGETED QUESTION
```

---

# 99. Clarification Principle

Clarification is a tool, not the default.

Ask a clarification question only when:

```text
A MATERIAL GAP EXISTS
AND
AVAILABLE CONTEXT / RETRIEVAL
CANNOT RESOLVE IT SAFELY
AND
THE TASK CANNOT PROCEED
UNDER A SAFE BOUNDED INTERPRETATION.
```

---

# 100. Do Not Over-Clarify

Do not ask:

```text
WHAT FORMAT?
```

when a reasonable default format cannot change the substantive outcome.

Do ask:

```text
WHICH ACCOUNT?
```

before a consequential action when multiple accounts are plausible.

---

# 101. Minimum Clarification

When clarification is necessary:

```text
ASK
THE MINIMUM QUESTION
THAT CLOSES
THE HIGHEST-PRIORITY GAP.
```

Do not ask a long questionnaire when one discriminating answer is sufficient.

---

# 102. Gap Classification

Resolver gaps:

```text
CRITICAL

DECISION-RELEVANT

EXPLANATORY

COSMETIC
```

Resolve in that order.

---

# 103. Critical Semantic Gap

Examples:

```text
UNKNOWN DESTRUCTIVE TARGET

UNKNOWN RECIPIENT

UNKNOWN AMOUNT

UNKNOWN ACCOUNT

UNKNOWN ENVIRONMENT

CONTRADICTORY HARD REQUIREMENTS
```

when consequential action depends on them.

---

# 104. Decision-Relevant Semantic Gap

Example:

```text
"Which is better?"
```

when the optimization criterion could change the recommendation.

---

# 105. Explanatory Semantic Gap

Example:

A missing reason for a preference that does not change the requested output.

---

# 106. Cosmetic Semantic Gap

Example:

Exact heading style.

Do not block substantive work for cosmetic ambiguity.

---

# 107. Resolver Sensitivity Test

For each unresolved material field:

```text
IF THIS FIELD CHANGED,
COULD THE TASK RESULT
OR EFFECT CHANGE?
```

If no:

```text
LOW PRIORITY
```

If yes:

```text
RESOLVE OR CONDITION
```

---

# 108. Objective Sensitivity

Objective is almost always load-bearing.

If objective ambiguity exists:

```text
ESCALATE RESOLUTION
```

unless competing objectives can safely be returned as alternatives.

---

# 109. Target Sensitivity

Target ambiguity is especially important for effectful tasks.

```text
UNKNOWN TARGET
+
IRREVERSIBLE EFFECT
=
BLOCK
```

---

# 110. Parameter Sensitivity

Parameters such as:

```text
AMOUNT

DATE

QUANTITY

RECIPIENT

PATH

VERSION

ENVIRONMENT
```

should be tested for decision/effect sensitivity.

---

# 111. Constraint Sensitivity

A missing soft constraint may be tolerable.

A missing hard constraint may invalidate the task.

---

# 112. Resolver Fast Path

Use the fast path only when:

```text
ONE DOMINANT INTERPRETATION

DEPENDENCY CLOSURE SUFFICIENT

NO MATERIAL CONFLICT

NO MATERIAL REFERENCE AMBIGUITY

NO MATERIAL FRESHNESS ISSUE

NO EFFECT EXPANSION

NO CRITICAL GAP
```

---

# 113. Fast Path Output

Conceptually:

```yaml
resolver_result:

  status: RESOLVED

  complexity: R0

  task_contract:
    objective:
    deliverable:
    scope:
    constraints:
    completion:
```

---

# 114. Fast Path Independence Requirement

Do not assume a task is local merely because it is syntactically simple.

Example:

```text
"Delete it."
```

is short but may require deep reference and authority resolution.

---

# 115. Resolver Escalation Triggers

Escalate when:

```text
REFERENCE AMBIGUITY

CONTRADICTION

SCOPE CONFLICT

STALE CONTEXT

MULTIPLE PLAUSIBLE TARGETS

CAUSAL REQUIREMENT

PROVENANCE CONFLICT

REGIME SHIFT

IRREVERSIBLE EFFECT

GOVERNANCE IMPACT

UNKNOWN AUTHORITY-RELEVANT PRINCIPAL

AMBIGUOUS DEPENDENCIES
```

---

# 116. Resolver De-Escalation

Once decision-changing semantic uncertainty is resolved:

```text
STOP EXPANDING
```

and emit the contract.

---

# 117. Resolver Stop Condition

Resolution is sufficient when:

```text
OBJECTIVE BOUND
∧
SCOPE BOUND
∧
DELIVERABLE BOUND
∧
HARD CONSTRAINTS KNOWN
∧
CRITICAL REFERENCES RESOLVED
∧
CRITICAL GAPS CLOSED
∧
COMPLETION DEFINED
```

plus any additional stake-dependent requirements.

---

# 118. Task Sufficiency

Candidate function:

```text
TaskSufficient(T)
```

returns true only when the unresolved fields cannot materially prevent safe
Control Plane evaluation.

---

# 119. Resolution Does Not Require Perfect Knowledge

A resolver does not need to know:

```text
EVERY IMPLEMENTATION DETAIL

EVERY POSSIBLE DEPENDENCY

EVERY FUTURE FAILURE
```

before producing a task.

It needs enough semantic closure for downstream governance.

---

# 120. Partial Task Contract

When some fields are known:

```yaml
task_contract:
  objective: KNOWN
  target: UNKNOWN
  scope: PARTIAL
  constraints: KNOWN
```

preserve the partial structure.

Do not discard valid resolved fields because one field remains unknown.

---

# 121. Selective Resolution

If only target is unresolved:

```text
RESOLVE TARGET
```

not the entire task again.

This follows AMOS selective invalidation principles.

---

# 122. Resolver State

Candidate states:

```text
CAPTURED

PARSING

RESOLVING

COMPETING

BLOCKED

RESOLVED

CONDITIONAL

INVALIDATED

SUPERSEDED
```

---

# 123. Captured

Source request has been preserved but not yet semantically processed.

---

# 124. Parsing

Surface structure is being extracted.

---

# 125. Resolving

References, objectives, scope, or constraints are being bound.

---

# 126. Competing

Multiple materially incompatible interpretations remain viable.

---

# 127. Blocked

A critical gap prevents sufficient task resolution.

---

# 128. Resolved

One sufficiently supported task interpretation has been established.

---

# 129. Conditional

The task is resolvable only under explicit assumptions.

Example:

```text
IF "the report" refers to REPORT-A,
THEN TASK = ...
```

This may be adequate for non-effectful analysis but not for irreversible
execution.

---

# 130. Invalidated

Previously resolved semantics are no longer valid because a dependency
changed.

---

# 131. Superseded

A newer resolver result replaces the prior one.

Preserve lineage.

---

# 132. Resolver Output

Conceptual resolver result:

```yaml
TaskResolverResult:

  resolver_id:

  source:
    request:
    provenance:

  status:

  complexity:

  selected_interpretation:

  competing_interpretations: []

  task_contract:

  unresolved:
    critical: []
    decision_relevant: []
    explanatory: []
    cosmetic: []

  assumptions:
    load_bearing: []

  evidence:

  provenance:

  invalidation_conditions:

  next_route:
```

---

# 133. Next Route

Possible next routes:

```text
TASK_CONTRACT_READY

REQUEST_CLARIFICATION

RETRIEVE_CONTEXT

CAPABILITY_RESOLUTION

POLICY_RESOLUTION

AUTHORITY_RESOLUTION

PROVENANCE_RESOLUTION

BLOCK

RETURN_UNKNOWN
```

---

# 134. Resolver Provenance

The resolver should retain provenance for material semantic bindings.

Example:

```yaml
binding:
  field: target
  value: FILE-A
  basis:
    - explicit reference
    - active attachment
```

This permits later auditing.

---

# 135. Binding Strength

Candidate classes:

```text
EXPLICIT

DETERMINISTIC

STRONGLY_RESOLVED

INFERRED

DEFAULTED

CONDITIONAL

UNKNOWN
```

The exact enum remains implementation-dependent.

---

# 136. Binding Confidence Ceiling

A task field should not be represented with greater certainty than its
support permits.

Example:

```text
TARGET = FILE-A
```

may be:

```text
CONDITIONAL
```

if two files exist and context only weakly favors A.

---

# 137. Provenance Topology

When interpretation relies on multiple contextual sources, check whether they
are independent.

Example:

```text
MESSAGE B
quotes
MESSAGE A
```

Then B is not independent confirmation of A's interpretation.

---

# 138. Persistent Provenance

Once a material task field is resolved, preserve the resolution basis through
downstream processing.

Do not allow:

```text
TARGET RESOLVED FROM SOURCE A
```

to become merely:

```text
TARGET = X
```

with the source forgotten.

---

# 139. Freshness-Bounded Resolution

Some bindings expire.

Example:

```text
"the current production version"
```

resolved at time `T1`.

At `T2`, before execution, that binding may need revalidation.

---

# 140. Resolution Epoch

Conceptually, a resolver result may bind to:

```text
TASK EPOCH

CONTEXT EPOCH

STATE VERSION
```

when mutable state matters.

This is a reasoning pattern, not a claim about a specific runtime mechanism.

---

# 141. MVCC Pattern

Resolver reads:

```text
CONTEXT @ V1
```

and resolves:

```text
TASK @ V1
```

Before consequential commit:

```text
COMPARE CURRENT CONTEXT
WITH V1
```

If a load-bearing semantic dependency changed:

```text
INVALIDATE DEPENDENT TASK FIELDS
```

---

# 142. CAS Pattern

For a mutable task binding:

```text
IF CURRENT_BINDING_VERSION
=
EXPECTED_BINDING_VERSION
THEN CONTINUE
ELSE REVALIDATE
```

Conceptually.

---

# 143. Resolver Dependency Graph

Task fields may depend on other resolved fields.

Example:

```text
REQUEST
   ↓
TARGET
   ↓
SCOPE
   ↓
EFFECT ENVELOPE
```

If target changes, scope and effect analysis may need revalidation.

---

# 144. Selective Invalidation

Example:

```text
TARGET → ENVIRONMENT → EFFECT

FORMAT → DELIVERABLE_PRESENTATION
```

If target changes:

```text
INVALIDATE:
TARGET DESCENDANTS
```

Do not invalidate unrelated formatting decisions.

---

# 145. Resolver Repair

When a binding fails:

```text
LOCALIZE FAILED BINDING
↓
INVALIDATE DESCENDANTS
↓
RETURN TO NEAREST VALID STATE
↓
RESOLVE ALTERNATIVE
↓
RECHECK SUFFICIENCY
```

---

# 146. Failed Path Rule

Do not repeat a failed interpretation path without changed evidence.

```text
I1 FAILED
+
NO NEW EVIDENCE
→
DO NOT RESELECT I1
```

unless failure itself was procedural rather than semantic.

---

# 147. Resolver Contradiction Detection

Search for contradictions between:

```text
REQUEST PARTS

REQUEST AND CONTEXT

CURRENT AND PRIOR TASK

SCOPE AND CONSTRAINTS

OBJECTIVE AND EFFECT

DELIVERABLE AND PROHIBITIONS
```

---

# 148. Request/Internal Contradiction

Example:

```text
"Send this now,
but don't contact anyone."
```

Preserve conflict.

Do not choose one clause silently.

---

# 149. Request/Context Contradiction

Example:

Current request:

```text
"use version 4"
```

prior context:

```text
"use version 3"
```

The current explicit request may supersede prior context, but the transition
should be recognized.

---

# 150. Current Explicit Intent

Candidate precedence principle:

```text
CURRENT EXPLICIT TASK INTENT
```

normally dominates:

```text
OLDER INFERRED TASK INTENT
```

unless upstream canon or governance rules establish otherwise.

---

# 151. User Correction

If the source corrects prior semantics:

```text
"Not A — B."
```

then:

```text
A
```

must be invalidated as a current task binding.

Preserve history; update active resolution.

---

# 152. Resolver Causal Firewall

If request asks:

```text
"Did X cause Y?"
```

resolver must classify it as causal.

Do not silently resolve it as:

```text
"Are X and Y associated?"
```

---

# 153. Resolver Scope Firewall

If request asks:

```text
"Does this work in environment A?"
```

do not silently broaden to:

```text
"Does this work universally?"
```

---

# 154. Resolver Regime Firewall

If context comes from regime `R1` but task targets `R2`:

```text
R1 EVIDENCE
```

cannot silently bind `R2` semantics.

---

# 155. Resolver Temporal Firewall

If the task asks:

```text
LATEST
```

do not resolve from stale context merely because it is available.

---

# 156. Resolver Effect Firewall

Do not transform:

```text
ANALYZE
```

into:

```text
ACT
```

or:

```text
DRAFT
```

into:

```text
SEND
```

without support.

---

# 157. Resolver Authority Firewall

Do not infer:

```text
USER REQUESTED ACTION
```

therefore:

```text
USER IS AUTHORIZED FOR ACTION
```

Authority is downstream.

---

# 158. Resolver Capability Firewall

Do not infer:

```text
TASK REQUIRES X
```

therefore:

```text
X IS AVAILABLE
```

Capability resolution is downstream.

---

# 159. Resolver Policy Firewall

Do not mutate a prohibited task into a different task merely to make it
permissible unless the system is explicitly constructing a safe alternative.

If constructing an alternative:

```text
ORIGINAL TASK
```

and:

```text
SAFE ALTERNATIVE
```

must remain distinct.

---

# 160. Safe Alternative

Conceptual output:

```yaml
original_task:
  status: BLOCKED

alternative_task:
  status: PROPOSED
  relationship: SAFE_ALTERNATIVE
```

Do not claim the alternative is what the requester originally asked for.

---

# 161. Adversarial Resolver Validation

For consequential task resolution, challenge the selected interpretation.

Ask:

```text
WHAT ELSE COULD THIS MEAN?

WHAT REFERENCE COULD BE WRONG?

WHAT CONTEXT COULD BE STALE?

WHAT NEGATION COULD HAVE BEEN MISREAD?

WHAT EFFECT COULD HAVE BEEN SILENTLY EXPANDED?

WHAT SCOPE COULD HAVE LEAKED?

WHAT ASSUMPTION IS HIDDEN?
```

---

# 162. Independent Challenge Path

The challenge should use a genuinely different route.

Example:

Primary path:

```text
LINGUISTIC INTERPRETATION
```

Challenge path:

```text
TASK HISTORY + ACTIVE STATE + EFFECT ANALYSIS
```

---

# 163. Challenge Success

If challenge reveals a plausible materially different interpretation:

```text
DOWNGRADE RESOLUTION
```

to:

```text
CONDITIONAL

COMPETING

BLOCKED

UNKNOWN
```

as appropriate.

---

# 164. Challenge Failure

If no alternative survives:

```text
KEEP SELECTED INTERPRETATION
```

but do not upgrade it to `VERIFIED` merely because challenge failed.

---

# 165. Resolver Proof Capsule

Consequential resolution should conceptually carry:

```yaml
TaskResolverProofCapsule:

  source_request:

  selected_interpretation:

  task_class:

  objective_binding:
    value:
    basis:
    class:

  target_binding:
    value:
    basis:
    class:

  scope_binding:

  constraint_binding:

  deliverable_binding:

  effect_binding:

  assumptions:

  competing_interpretations:

  discriminating_evidence:

  unresolved_gaps:

  falsifiers:

  invalidation_conditions:

  confidence_ceiling:
```

---

# 166. Resolver Invalidation Conditions

Examples:

```text
NEW USER CORRECTION

TARGET CHANGES

ACTIVE FILE CHANGES

CURRENT VERSION CHANGES

CONTEXT EXPIRES

REGIME CHANGES

NEW CONTRADICTORY EVIDENCE

PARENT TASK SUPERSEDED
```

---

# 167. Parent Task Resolution

A child task must inherit only relevant parent semantics.

Conceptually:

```text
PARENT TASK
   ↓
INHERIT:
  applicable scope
  applicable constraints
  lineage
   ↓
CHILD TASK
```

---

# 168. Parent Constraint Inheritance

A child task may narrow constraints.

It may not silently remove a parent hard constraint.

```text
PARENT HARD CONSTRAINT
→
CHILD
```

unless explicit supersession is valid.

---

# 169. Child Scope

Candidate invariant:

```text
CHILD_SCOPE
⊆
PARENT_SCOPE
```

unless a separate scope expansion is authorized.

---

# 170. Delegated Task Resolution

Delegation must resolve:

```text
SUBTASK OBJECTIVE

SUBTASK SCOPE

RETURN CONTRACT

DEPENDENCIES

CONSTRAINTS
```

Do not delegate a vague fragment that cannot be independently evaluated.

---

# 171. Multi-Agent Resolver

For multiple agents:

```text
ROOT TASK
   ↓
TASK RESOLVER
   ↓
SUBTASK CONTRACTS
   ↓
AGENTS
```

Each subtask must retain root lineage.

---

# 172. Agent Independence

Separate agents are not automatically independent.

Check shared:

```text
STATE

PROVENANCE

TARGETS

EFFECTS

AUTHORITIES

DEPENDENCIES
```

---

# 173. Atomic Resolution

Some fields must be resolved jointly.

Example:

```text
TARGET
+
ENVIRONMENT
+
ACTION
```

may jointly determine the actual task.

Resolving each independently can create an impossible combination.

---

# 174. Atomic Multi-RSCF Reasoning

Where multiple RSCF structures jointly determine task semantics, resolution
must preserve atomic consistency.

Conceptually:

```text
RSCF-A
+
RSCF-B
+
RSCF-C
→
ONE TASK BINDING
```

if no independent resolution is valid.

---

# 175. Causal Epoch Finality

When a task depends on causally related mutable state, a resolver result
should not be treated as permanently final merely because local parsing is
complete.

Conceptually:

```text
SEMANTIC RESOLUTION
+
CAUSAL STATE VALIDITY
→
EXECUTION-RELEVANT FINALITY
```

---

# 176. Shard-Local Resolution

Local resolution is permitted when:

```text
DEPENDENCY CLOSURE IS LOCAL

NO CROSS-SHARD CONFLICT

PROVENANCE INDEPENDENCE ESTABLISHED

SCOPE/REGIME COMPATIBLE

FRESHNESS VALID
```

This is a reasoning architecture pattern, not a claim of literal distributed
deployment.

---

# 177. Coordination Avoidance

Do not coordinate globally if local proof establishes that remote state
cannot change task semantics.

Conceptually:

```text
PROOF OF INDEPENDENCE
→
SAFE LOCAL RESOLUTION
```

not:

```text
ASSUMED INDEPENDENCE
→
SKIP COORDINATION
```

---

# 178. Proof-Based Coordination Avoidance

Before avoiding broader coordination, establish:

```text
DEPENDENCY CLOSURE

NO SHARED LOAD-BEARING STATE

NO SHARED EFFECT TARGET

NO MATERIAL PROVENANCE CORRELATION

NO GOVERNANCE COUPLING
```

where relevant.

---

# 179. Resolver and Fractal Knowledge Network

Use smallest sufficient retrieval:

```text
BOOTSTRAP
↓
H DOMAIN
↓
M SUBSYSTEM
↓
L DETAIL
↓
RAW EVIDENCE
ONLY IF REQUIRED
```

---

# 180. Resolver Bootstrap

Bootstrap should contain enough information to determine:

```text
LIKELY DOMAIN

LIKELY TASK CLASS

RELEVANT CANON

LIKELY DEPENDENCY PATH
```

without loading the full corpus.

---

# 181. H-Level Resolution

Use H domain knowledge when the task domain itself is ambiguous or
domain-level rules affect interpretation.

---

# 182. M-Level Resolution

Use M subsystem knowledge when a particular subsystem determines task
semantics.

---

# 183. L-Level Resolution

Use L detail when exact implementation, field, rule, or artifact semantics
are load-bearing.

---

# 184. Raw Evidence

Load raw evidence only when required to:

```text
DISAMBIGUATE

VERIFY A LOAD-BEARING FIELD

RESOLVE CONTRADICTION

ESTABLISH PROVENANCE

CHECK FRESHNESS

TEST A FALSIFIER
```

---

# 185. Retrieval Failure

If required evidence cannot be retrieved:

```text
DO NOT BRIDGE THE GAP
WITH PLAUSIBLE SEMANTICS.
```

Return:

```text
CONDITIONAL

BLOCKED

UNKNOWN/GAP
```

depending on materiality.

---

# 186. Resolver and RSCF

Task resolution may instantiate RSCF around:

```text
REQUEST

REFERENCES

OBJECTIVE

SCOPE

CONSTRAINTS

DEPENDENCIES
```

The RSCF is bounded by task resolution needs.

---

# 187. Resolver and GMEF

If resolving the request reveals that the task proposes changing system
governance or canonical architecture:

```text
ROUTE TO GMEF-RELEVANT GOVERNANCE
```

rather than treating it as an ordinary generation task.

---

# 188. Resolver and Memory

Memory can support resolution only when:

```text
RELEVANT

VALID

NON-CONFLICTING

FRESH ENOUGH

SCOPE-COMPATIBLE
```

Do not let stale memory override current explicit intent.

---

# 189. Resolver and World Model

A world model may help resolve contextual references.

But:

```text
MODEL STATE
!=
OBSERVED CURRENT STATE
```

For consequential bindings, revalidation may be necessary.

---

# 190. Resolver and Provenance

Every material inferred field should remain traceable to:

```text
SOURCE

CONTEXT

RULE

OR EVIDENCE
```

that produced it.

---

# 191. Resolver and Semantic Transaction

Once a task is sufficiently resolved, the resolved contract may become part
of a semantic transaction.

The semantic transaction should bind to:

```text
TASK ID

TASK VERSION

RESOLVER RESULT

RELEVANT SNAPSHOT
```

where material.

---

# 192. Resolver and Commit

Before commit, downstream systems may ask:

```text
IS THIS STILL
THE SAME TASK
THAT WAS RESOLVED?
```

If not:

```text
RETURN TO RESOLUTION
```

for affected fields.

---

# 193. Commit-Time Resolver Check

Candidate check:

```text
CURRENT TASK VERSION
=
PLANNED TASK VERSION

AND

NO LOAD-BEARING
RESOLUTION DEPENDENCY
HAS CHANGED
```

Otherwise:

```text
REVALIDATE
```

---

# 194. Resolver and Observability

Resolution should identify what must later be observed to know whether the
task was completed.

Example:

```text
"Make sure the file was uploaded."
```

requires observable upload state, not merely tool invocation.

---

# 195. Resolver and Effects

The resolver identifies intended effect semantics.

The effect subsystem determines actual effect class and governance.

Distinction:

```text
INTENDED EFFECT
!=
OBSERVED EFFECT
```

---

# 196. Resolver and Finalizer

The finalizer evaluates actual results against the resolved Task Contract.

Therefore:

```text
BAD RESOLUTION
→
BAD COMPLETION TEST
```

even if runtime execution itself is technically correct.

---

# 197. Resolver and Replay

Replay must use the resolver result associated with the original task
version.

Do not reinterpret historical requests using current context and then treat
the new interpretation as the historical task.

---

# 198. Historical Resolution

Historical audit should distinguish:

```text
WHAT THE REQUEST MEANT
UNDER THEN-AVAILABLE CONTEXT
```

from:

```text
WHAT IT WOULD MEAN
UNDER CURRENT CONTEXT
```

---

# 199. Resolver Anti-Fabrication Rules

Never perform:

```text
UNKNOWN TARGET
→
PLAUSIBLE TARGET
```

```text
UNKNOWN OBJECTIVE
→
CONVENIENT OBJECTIVE
```

```text
AMBIGUOUS RECIPIENT
→
MOST LIKELY RECIPIENT
```

for consequential execution without sufficient support.

Never perform:

```text
MISSING CONSTRAINT
→
ASSUME NONE
```

when context indicates constraints may be material.

---

# 200. Resolver Anti-Expansion Rules

Never silently transform:

```text
READ
→
WRITE
```

```text
DRAFT
→
SEND
```

```text
PREVIEW
→
EXECUTE
```

```text
LOCAL
→
GLOBAL
```

```text
ONE FILE
→
ALL FILES
```

```text
CURRENT TASK
→
ALL FUTURE TASKS
```

---

# 201. Resolver Anti-Compression Rule

Compression must not erase:

```text
NEGATION

CONDITION

TARGET

SCOPE

HARD CONSTRAINT

EFFECT CLASS

UNCERTAINTY

COMPETING INTERPRETATION
```

when load-bearing.

---

# 202. Resolver Anti-Fluency Rule

A fluent interpretation is not necessarily a supported interpretation.

```text
LINGUISTIC PLAUSIBILITY
!=
SEMANTIC PROOF
```

---

# 203. Resolver Anti-Popularity Rule

The most common interpretation is not necessarily the correct interpretation
for the current task.

---

# 204. Resolver Anti-Authority Rule

Do not use apparent authority of a source to fill missing task semantics.

Authority to request an action and clarity of requested semantics are separate
questions.

---

# 205. Resolver Anti-Causal Rule

Do not convert:

```text
WHY DID X HAPPEN?
```

into a confident causal task if the source only supports association.

The task may still ask a causal question; the eventual answer may be
`UNKNOWN/GAP`.

---

# 206. Resolver Anti-Scope-Leak Rule

Context outside the active task must not silently enter scope merely because
it is available.

---

# 207. Resolver Anti-Staleness Rule

Previously resolved references must not be reused indefinitely.

Freshness is binding-specific.

---

# 208. Resolver Anti-Sybil Rule

Multiple context fragments derived from the same origin do not provide
independent support for an interpretation.

---

# 209. Resolver Anti-Regression Gate

Any optimization to task resolution must preserve or improve:

```text
INTENT FIDELITY

REFERENCE CORRECTNESS

SCOPE CORRECTNESS

NEGATION PRESERVATION

CONSTRAINT VISIBILITY

PROVENANCE

CONTRADICTION VISIBILITY

EFFECT BOUNDARIES

FRESHNESS

REPAIRABILITY

AUDITABILITY

USER FIT
```

Otherwise reject or roll back the optimization.

---

# 210. Resolver Invariants

```text
TR-I01
SOURCE REQUEST MUST REMAIN TRACEABLE.

TR-I02
RESOLVED INTENT MUST NOT BE CONFUSED WITH SOURCE WORDING.

TR-I03
LOAD-BEARING SEMANTICS MUST NOT BE INVENTED.

TR-I04
NEGATION MUST BE PRESERVED.

TR-I05
CONDITIONS MUST BE PRESERVED.

TR-I06
MATERIAL REFERENCE AMBIGUITY MUST NOT BE SILENTLY COLLAPSED.

TR-I07
OBJECTIVE MUST BE BOUND BEFORE CONSEQUENTIAL EXECUTION.

TR-I08
TARGET MUST BE BOUND BEFORE TARGET-SENSITIVE CONSEQUENTIAL EXECUTION.

TR-I09
SCOPE MUST NOT EXPAND SILENTLY.

TR-I10
HARD CONSTRAINTS MUST NOT BE DROPPED.

TR-I11
DRAFT MUST NOT BE RESOLVED AS SEND WITHOUT SUPPORT.

TR-I12
PREVIEW MUST NOT BE RESOLVED AS COMMIT WITHOUT SUPPORT.

TR-I13
PLAN MUST NOT BE RESOLVED AS EXECUTION WITHOUT SUPPORT.

TR-I14
TASK RESOLUTION DOES NOT GRANT AUTHORITY.

TR-I15
TASK RESOLUTION DOES NOT ESTABLISH CAPABILITY.

TR-I16
TASK RESOLUTION DOES NOT ESTABLISH POLICY PERMISSION.

TR-I17
COMPETING MATERIAL INTERPRETATIONS MUST REMAIN VISIBLE.

TR-I18
CLARIFICATION SHOULD TARGET THE HIGHEST-VALUE UNRESOLVED GAP.

TR-I19
LOW-VALUE AMBIGUITY SHOULD NOT BLOCK SUFFICIENTLY BOUNDED WORK.

TR-I20
FRESHNESS-SENSITIVE BINDINGS MUST EXPIRE OR REVALIDATE.

TR-I21
PROVENANCE OF MATERIAL INFERENCES MUST REMAIN RECOVERABLE.

TR-I22
RESOLUTION CONFIDENCE MUST NOT EXCEED SUPPORT.

TR-I23
FAILED BINDINGS SHOULD INVALIDATE ONLY DEPENDENT FIELDS.

TR-I24
LOCAL FAST-PATH RESOLUTION REQUIRES PROVEN DEPENDENCY SUFFICIENCY.

TR-I25
OPTIMIZATION MUST NOT ALTER TASK MEANING.
```

These identifiers remain candidate specification IDs until separately
registered as canonical invariants.

---

# 211. Example — Direct Resolution

Request:

```text
"Summarize this file."
```

Context:

```text
exactly one attached file
```

Resolver:

```yaml
status: RESOLVED

objective:
  summarize attached file

target:
  attached_file_1

deliverable:
  text summary

scope:
  include:
    - attached_file_1

effects:
  - read
  - analyze
  - respond
```

No clarification required.

---

# 212. Example — Ambiguous Target

Request:

```text
"Delete the old one."
```

Context:

```text
FILE-A
FILE-B
FILE-C
```

with no unique age relation.

Resolver:

```yaml
status: BLOCKED

gap:
  class: CRITICAL
  field: target
```

Required action:

```text
RESOLVE TARGET
```

before destructive execution.

---

# 213. Example — Draft vs Send

Request:

```text
"Write an email to Alex explaining the delay."
```

Resolver:

```text
GENERATE EMAIL DRAFT
```

unless context explicitly establishes sending intent.

Do not resolve automatically to:

```text
SEND EMAIL
```

---

# 214. Example — Explicit Send

Request:

```text
"Send Alex an email explaining the delay."
```

Resolver:

```yaml
objective:
  communicate delay to Alex

deliverable:
  sent email

effect_intent:
  external_communication

recipient:
  Alex
```

If multiple Alex identities are plausible and recipient choice matters:

```text
RECIPIENT GAP
```

must be resolved.

---

# 215. Example — Current Data

Request:

```text
"What's the current price?"
```

Resolver should identify:

```text
FRESHNESS REQUIRED
```

and bind the relevant asset.

A stale cached value does not satisfy the resolved task.

---

# 216. Example — Comparison Ambiguity

Request:

```text
"Which one is better?"
```

Objects:

```text
A
B
```

If no evaluation criterion exists and different criteria could reverse the
answer:

```text
DECISION-RELEVANT GAP
```

Possible response:

```text
better by what criterion?
```

or use a clearly labeled multi-criteria comparison if that safely satisfies
the task.

---

# 217. Example — Safe Default

Request:

```text
"Give me a short summary."
```

Exact word count is unspecified.

The resolver may safely default to a concise summary because exact length is
not load-bearing.

---

# 218. Example — Unsafe Default

Request:

```text
"Transfer the money."
```

Missing:

```text
AMOUNT

SOURCE ACCOUNT

DESTINATION
```

No defaults.

Result:

```text
BLOCKED
```

---

# 219. Example — Competing Interpretation

Request:

```text
"Use the latest model."
```

Possible meanings:

```text
latest released model

latest model in repository

latest approved model

latest model used in prior task
```

If the distinction affects outcome:

```text
COMPETING
```

until discriminated.

---

# 220. Example — Scope Continuation

Prior task:

```text
analyze files A and B
```

Current request:

```text
"Now compare their security assumptions."
```

Resolver may inherit:

```text
A and B
```

because continuation is strongly established.

It should not add file C merely because C is available.

---

# 221. Example — Correction

Prior:

```text
"Use report A."
```

Current:

```text
"Actually use report B."
```

Resolver:

```text
INVALIDATE target=A
BIND target=B
```

Dependent reasoning based on A becomes stale.

---

# 222. Example — Conditional Task

Request:

```text
"If deployment finished, run the validation."
```

Resolver:

```yaml
condition:
  deployment_finished: REQUIRED_TRUE

action:
  run_validation
```

Do not execute validation merely because the action clause is clear.

---

# 223. Example — Causal Task

Request:

```text
"Did the policy change cause the decline?"
```

Resolver:

```yaml
task_class:
  - ANALYSIS
  - CAUSAL

objective:
  assess causal relationship

causal_requirement:
  true
```

The downstream evidence process must respect the causal firewall.

---

# 224. Example — Governance Task

Request:

```text
"Change the canonical rule so this case is always allowed."
```

Resolver should identify:

```text
GOVERNANCE EFFECT
```

and route accordingly.

It is not merely a text-editing task.

---

# 225. Example — Recovery Task

Request:

```text
"Undo only the changes caused by the failed migration."
```

Resolver must bind:

```text
FAILED MIGRATION

DEPENDENT CHANGES

UNAFFECTED CHANGES

RECOVERY SCOPE
```

before rollback.

---

# 226. Example — Historical Task

Request:

```text
"What did the resolver specification say in v3?"
```

Task scope:

```text
HISTORICAL
```

Current v4.4 semantics must not silently replace v3 content.

---

# 227. Example — Corpus vs Empirical Claim

Request:

```text
"Does AMOS prove this architecture is universally correct?"
```

Resolver must distinguish:

```text
CORPUS MODEL CLAIM
```

from:

```text
EMPIRICAL / FORMAL UNIVERSAL VALIDITY
```

The latter requires independent evidence.

---

# 228. Resolver Machine Form

```yaml
task_resolver:

  resolver_id:

  source:
    type:
    raw_request:
    provenance:
    timestamp:

  context:
    task_lineage:
    active_objects:
    temporal_context:
    environment:
    regime:

  classification:
    task_types: []
    complexity:

  bindings:

    objective:
      value:
      class:
      basis:

    target:
      value:
      class:
      basis:

    deliverable:
      value:
      class:
      basis:

    scope:
      value:
      class:
      basis:

    constraints:
      hard: []
      soft: []

    inputs:
      required: []
      optional: []
      prohibited: []

    assumptions:
      load_bearing: []
      noncritical: []

    freshness:

    stakes:

    effects:

    dependencies:

  competing_interpretations: []

  uncertainty:
    semantic:
    evidence:
    model:
    scope:
    temporal:
    causal:
    execution:
    provenance_independence:

  gaps:
    critical: []
    decision_relevant: []
    explanatory: []
    cosmetic: []

  sufficiency:
    objective:
    scope:
    constraints:
    references:
    completion:
    overall:

  output:
    status:
    task_contract:
    next_route:

  provenance:

  invalidation_conditions:
```

---

# 229. Resolver Pseudocode

```text
function resolve_task(request, context):

    source = preserve(request)

    normalized = normalize_without_semantic_expansion(source)

    task_class = classify(normalized)

    references = resolve_material_references(
        normalized,
        context
    )

    objective = resolve_objective(
        normalized,
        context,
        references
    )

    deliverable = resolve_deliverable(
        normalized,
        context
    )

    scope = resolve_scope(
        normalized,
        context,
        references
    )

    constraints = extract_constraints(
        normalized,
        context
    )

    inputs = identify_required_inputs(
        objective,
        scope,
        constraints
    )

    assumptions = identify_load_bearing_assumptions(
        objective,
        references,
        scope,
        inputs
    )

    freshness = resolve_freshness_requirement(
        normalized,
        inputs,
        context
    )

    stakes = classify_resolution_stakes(
        objective,
        scope,
        context
    )

    effects = resolve_effect_intent(
        normalized,
        objective
    )

    dependencies = identify_dependencies(
        objective,
        references,
        scope,
        effects
    )

    uncertainty = classify_uncertainty(
        source,
        context,
        dependencies
    )

    interpretations = generate_supported_interpretations(
        source,
        context
    )

    interpretations = eliminate_dominated_interpretations(
        interpretations
    )

    if materially_competing(interpretations):
        evidence = run_cheapest_discriminating_test(
            interpretations
        )

        interpretations = update(
            interpretations,
            evidence
        )

    gaps = classify_gaps(
        objective,
        references,
        scope,
        constraints,
        inputs,
        effects
    )

    if critical_gap(gaps):
        return BLOCKED(
            partial_task_contract,
            gaps
        )

    selected = select_supported_interpretation(
        interpretations
    )

    contract = build_task_contract(
        selected,
        objective,
        deliverable,
        scope,
        constraints,
        inputs,
        assumptions,
        freshness,
        stakes,
        effects,
        dependencies,
        uncertainty
    )

    if not sufficient(contract):
        return CONDITIONAL_OR_CLARIFY(
            contract,
            gaps
        )

    challenge = adversarial_validate_resolution(
        contract,
        source,
        context
    )

    if challenge.material_failure:
        return downgrade_resolution(
            contract,
            challenge
        )

    return RESOLVED(contract)
```

This pseudocode is conceptual and does not claim literal runtime
implementation.

---

# 230. Resolver Sufficiency Function

Conceptually:

```text
ResolveSufficient(T)
=
ObjectiveBound(T)
∧
DeliverableBound(T)
∧
ScopeBound(T)
∧
HardConstraintsKnown(T)
∧
CriticalReferencesBound(T)
∧
CriticalGapsClosed(T)
∧
CompletionDefined(T)
```

with additional predicates activated by stakes.

---

# 231. Consequential Sufficiency

For consequential tasks:

```text
ResolveSufficientConsequential(T)
=
ResolveSufficient(T)
∧
TargetBound(T)
∧
EffectIntentBound(T)
∧
FreshnessSufficient(T)
∧
NoMaterialSemanticConflict(T)
```

This still does not establish authority or policy permission.

---

# 232. Resolution Confidence

Conceptually:

```text
Confidence(TaskResolution)
≤
MIN(
  Confidence(ObjectiveBinding),
  Confidence(TargetBinding),
  Confidence(ScopeBinding),
  Confidence(HardConstraintBinding)
)
```

for whichever bindings are load-bearing.

---

# 233. Resolver Decision Rule

```text
IF
ONE INTERPRETATION
DOMINATES
AND
CRITICAL FIELDS
ARE BOUND
THEN
RESOLVE

ELSE IF
SAFE CONDITIONAL EXECUTION
IS POSSIBLE
THEN
CONDITIONAL

ELSE IF
MATERIAL INTERPRETATIONS
REMAIN INCOMPARABLE
THEN
COMPETING

ELSE IF
A CRITICAL GAP
CAN BE CLOSED
BY TARGETED CLARIFICATION
THEN
CLARIFY

ELSE
BLOCK / UNKNOWN
```

---

# 234. Resolver Optimization Law

Optimize in this order:

```text
SEMANTIC INTEGRITY

TASK SUFFICIENCY

LOW EFFECT EXPANSION

LOW CLARIFICATION BURDEN

LOW RETRIEVAL COST

LOW LATENCY

LOW TOKEN COST
```

Never invert the first two for speed.

---

# 235. Resolver Compression Law

A compressed resolver output is valid only if decompression would preserve:

```text
OBJECTIVE

TARGET

SCOPE

CONSTRAINTS

EFFECT INTENT

UNCERTAINTY

GAPS

PROVENANCE
```

where load-bearing.

---

# 236. Resolver Failure Classes

Candidate classes:

```text
REFERENCE_FAILURE

OBJECTIVE_FAILURE

SCOPE_FAILURE

CONSTRAINT_CONFLICT

INPUT_FAILURE

TEMPORAL_FAILURE

REGIME_FAILURE

PROVENANCE_FAILURE

COMPETING_INTERPRETATION

CRITICAL_GAP

CONTEXT_STALE

TASK_SUPERSEDED
```

---

# 237. Reference Failure

A material reference cannot be uniquely bound.

Response:

```text
LOCALIZE REFERENCE
→
RETRIEVE OR CLARIFY
```

---

# 238. Objective Failure

No sufficiently supported primary objective can be identified.

Response:

```text
BLOCK TASK FORMATION
```

rather than inventing one.

---

# 239. Scope Failure

Task boundaries cannot be determined sufficiently.

Response:

```text
NARROW
OR
CLARIFY
```

---

# 240. Constraint Conflict

Two hard requirements cannot simultaneously hold.

Response:

```text
PRESERVE CONFLICT
```

until precedence or correction is established.

---

# 241. Input Failure

Required input is unavailable.

Response:

```text
RETRIEVE
REQUEST
OR
RETURN GAP
```

depending on task.

---

# 242. Temporal Failure

A freshness-sensitive reference cannot be validated.

Response:

```text
STALE / UNKNOWN
```

not current fact.

---

# 243. Regime Failure

Available context applies to a different regime.

Response:

```text
SCOPE/REGIME GAP
```

---

# 244. Provenance Failure

The source of a load-bearing semantic binding is unknown or unreliable.

Response:

```text
DOWNGRADE
OR
REVALIDATE
```

---

# 245. Competing Interpretation Failure

Multiple interpretations remain viable after economical discrimination.

Response:

```text
COMPETING
```

rather than forced selection.

---

# 246. Critical Gap Failure

A critical field remains unresolved.

Response:

```text
BLOCK CONSEQUENTIAL EXECUTION
```

---

# 247. Stale Context Failure

A previously resolved task relied on context that changed.

Response:

```text
SELECTIVE INVALIDATION
+
RE-RESOLUTION
```

---

# 248. Supersession Failure

A newer task replaces the active one.

Response:

```text
STOP OLD TASK
+
PRESERVE LINEAGE
+
ACTIVATE SUCCESSOR
```

subject to downstream effect state.

---

# 249. Resolver Test Matrix

A resolver implementation should eventually be tested against at least:

```text
CLEAR READ-ONLY REQUEST

AMBIGUOUS REFERENCE

AMBIGUOUS DESTRUCTIVE TARGET

NEGATION

CONDITIONAL REQUEST

MULTIPLE OBJECTIVES

CONFLICTING CONSTRAINTS

STALE CONTEXT

CURRENT/LATEST REQUEST

DRAFT VS SEND

PLAN VS EXECUTE

PARENT/CHILD TASK

USER CORRECTION

COMPETING INTERPRETATIONS

SCOPE EXPANSION ATTEMPT

PROVENANCE CORRELATION

CAUSAL QUESTION

REGIME SHIFT

RECOVERY TASK

GOVERNANCE TASK
```

This is a specification-level test matrix, not evidence that such tests have
already passed.

---

# 250. Property-Oriented Tests

Candidate properties:

```text
P1:
Adding irrelevant context must not change the resolved task.

P2:
Removing a load-bearing reference must invalidate dependent bindings.

P3:
Changing "send" to "draft" must change effect intent.

P4:
Changing target identity must invalidate target-dependent scope/effects.

P5:
Equivalent paraphrases should resolve to semantically equivalent contracts.

P6:
Contradictory hard constraints must not produce READY.

P7:
A stale freshness-sensitive binding must not remain final.

P8:
Two descendants of one provenance origin must not count as independent support.

P9:
A correction must supersede the corrected binding.

P10:
A read-only task must not acquire write effects through resolution.
```

---

# 251. Metamorphic Resolution Tests

Example:

Original:

```text
"Summarize file A."
```

Paraphrase:

```text
"Give me a summary of file A."
```

Expected:

```text
SEMANTICALLY EQUIVALENT TASK CONTRACT
```

---

# 252. Negation Metamorphic Test

Original:

```text
"Send the report."
```

Mutation:

```text
"Do not send the report."
```

Expected:

```text
EFFECT INTENT MUST CHANGE
```

Any resolver producing equivalent contracts fails.

---

# 253. Scope Metamorphic Test

Original:

```text
"Analyze A."
```

Mutation:

```text
"Analyze only A."
```

Expected:

```text
EXCLUSION OF OTHER TARGETS
BECOMES EXPLICIT
```

---

# 254. Temporal Metamorphic Test

Original:

```text
"What was the price yesterday?"
```

Mutation:

```text
"What is the price now?"
```

Expected:

```text
TEMPORAL SCOPE
AND
FRESHNESS REQUIREMENT
CHANGE
```

---

# 255. Effect Metamorphic Test

Original:

```text
"Draft a message."
```

Mutation:

```text
"Send the message."
```

Expected:

```text
EXTERNAL EFFECT REQUIREMENT
CHANGES
```

---

# 256. Resolver Audit Questions

For any consequential resolved task, an auditor should be able to ask:

```text
WHAT WAS THE ORIGINAL REQUEST?

WHAT OBJECTIVE WAS RESOLVED?

WHAT TARGET WAS RESOLVED?

WHY?

WHAT SCOPE WAS USED?

WHAT CONSTRAINTS WERE EXTRACTED?

WHAT WAS INFERRED?

WHAT WAS DEFAULTED?

WHAT REMAINED UNKNOWN?

WHAT COMPETING INTERPRETATIONS EXISTED?

WHAT EVIDENCE DISCRIMINATED THEM?

WHAT WOULD INVALIDATE THIS RESOLUTION?
```

---

# 257. Resolver Governance Boundary

The resolver may say:

```text
THE TASK APPEARS TO REQUEST X
```

It must not itself conclude:

```text
THEREFORE X IS AUTHORIZED
```

unless authority resolution is explicitly integrated under a higher-level
governed transaction.

Conceptually, the distinctions remain separate.

---

# 258. Resolver Output Classes

Use the weakest accurate class:

```text
RESOLVED

CONDITIONAL

COMPETING

UNKNOWN/GAP
```

`RESOLVED` means semantic sufficiency, not empirical truth of task premises.

---

# 259. Resolver Integrity Hierarchy

```text
INTENT FIDELITY
>
COMPLETENESS
>
FLUENCY
>
SPEED
>
TOKEN SAVINGS
```

A shorter resolver path is desirable only if it preserves the task.

---

# 260. Canonical Compression

```text
TASK RESOLVER
=
THE AMOS OS CONTROL-PLANE FUNCTION
THAT CONVERTS
A REQUEST
INTO
A BOUNDED TASK CONTRACT.

IT PRESERVES
THE SOURCE.

IT RESOLVES
REFERENCES.

IT BINDS
THE OBJECTIVE.

IT IDENTIFIES
THE DELIVERABLE.

IT BOUNDS
THE SCOPE.

IT EXTRACTS
HARD AND SOFT CONSTRAINTS.

IT IDENTIFIES
REQUIRED INPUTS.

IT EXPOSES
LOAD-BEARING ASSUMPTIONS.

IT DETECTS
FRESHNESS,
REGIME,
DEPENDENCY,
AND EFFECT REQUIREMENTS.

IT PRESERVES
COMPETING INTERPRETATIONS
WHEN EVIDENCE DOES NOT
JUSTIFY CONVERGENCE.

IT ASKS
ONLY THE MINIMUM
DECISION-RELEVANT
CLARIFICATION.

IT NEVER
INVENTS
A CONSEQUENTIAL TARGET.

IT NEVER
EXPANDS
READ INTO WRITE,
DRAFT INTO SEND,
PREVIEW INTO COMMIT,
OR PLAN INTO EXECUTION
WITHOUT SUPPORT.

IT NEVER
TREATS TASK RESOLUTION
AS AUTHORITY,
POLICY APPROVAL,
CAPABILITY,
OR COMMIT PERMISSION.

IT USES
THE SMALLEST SUFFICIENT
PROOF SCOPE.

IT INVALIDATES
ONLY THE TASK FIELDS
DEPENDENT ON
FAILED SEMANTIC PREMISES.

AND IT STOPS
AS SOON AS
THE TASK IS
SUFFICIENTLY BOUND
FOR THE REST
OF THE CONTROL PLANE
TO GOVERN IT.
```

---

# 261. Master Resolver Contract

Conceptually:

```text
TaskResolver
:
(
  Request,
  Context,
  Canon,
  RelevantState
)
→
(
  TaskContract,
  ResolutionState,
  Gaps,
  Provenance,
  InvalidationConditions
)
```

subject to:

```text
NO FABRICATION
∧
NO SILENT SCOPE EXPANSION
∧
NO SILENT EFFECT EXPANSION
∧
NO HIDDEN CONSTRAINT DROPPING
∧
NO FORCED INTERPRETATION CONVERGENCE
```

---

# 262. Final Law

```text
A REQUEST
IS NOT EXECUTABLE
MERELY BECAUSE
ITS WORDS ARE GRAMMATICALLY CLEAR.

FIRST PRESERVE
WHAT WAS ACTUALLY REQUESTED.

THEN RESOLVE
WHAT EACH MATERIAL REFERENCE MEANS.

THEN IDENTIFY
THE OBJECTIVE.

THEN BIND
THE TARGET.

THEN BOUND
THE SCOPE.

THEN EXTRACT
THE CONSTRAINTS.

THEN IDENTIFY
THE REQUIRED INPUTS,
ASSUMPTIONS,
FRESHNESS,
DEPENDENCIES,
AND EFFECTS.

THEN EXPOSE
WHAT REMAINS UNKNOWN.

IF MULTIPLE
MATERIALLY DIFFERENT
INTERPRETATIONS SURVIVE,
KEEP THEM COMPETING
UNTIL DISCRIMINATING
EVIDENCE EXISTS.

IF A CRITICAL GAP
REMAINS,
DO NOT INVENT
THE MISSING SEMANTICS.

IF THE TASK
CAN BE SAFELY BOUNDED,
EMIT
THE SMALLEST SUFFICIENT
TASK CONTRACT.

ONLY THEN
MAY CAPABILITY,
POLICY,
AUTHORITY,
PROVENANCE,
TRANSACTION,
EFFECT,
AND COMMIT
GOVERNANCE CONTINUE.
```

# END — AMOS OS TASK RESOLVER

```

This is a **substantive candidate replacement**, not recovered pre-existing canon: the actual Drive artifact currently contains only the misplaced placeholder text, so claiming that the specification above was the file's existing full content would be unsupported. :contentReference[oaicite:3]{index=3}
```

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00_ROOT/00-Home]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: task_resolver
node_type: note
path: 03_CONTROL_PLANE/01_TASK_CONTRACT/TASK_RESOLVER.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_ROOT/00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[01_TASK_CONTRACT_MOC]]
