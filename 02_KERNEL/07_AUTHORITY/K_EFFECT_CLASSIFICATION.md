---
artifact_id: AMOS-OS-K-EFFECT-CLASSIFICATION
canonical_name: K_EFFECT_CLASSIFICATION
artifact_type: kernel_effect_classification_contract
status: AMOS_MODEL
conclusion_class: AMOS_MODEL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
plane: KERNEL
scope: AMOS_OS
updated: 2026-08-26
tags: ['kernel', 'authority', 'note']

---
# K EFFECT CLASSIFICATION

> **AMOS Core target:** `v4.4`  
> **Origin architect / steward:** Trang Phan  
> **Canonical location:** `02_KERNEL/K_EFFECT_CLASSIFICATION.md`  
> **Status:** `AMOS_MODEL`  
> **Conclusion class:** `AMOS_MODEL`

## Purpose

`K_EFFECT_CLASSIFICATION` defines the kernel-level contract for determining what kind of effect a proposed operation can produce before authority, risk, commit, execution, recovery, and observability decisions rely on it.

Core law:

```text
CAPABILITY
!=
AUTHORITY
!=
EFFECT
```

An operation must not be governed solely by its name, tool, agent, skill, workflow, or stated intention.

AMOS reasons about the **actual effect envelope**.

```text
INTENT
↓
PROPOSED OPERATION
↓
POTENTIAL EFFECTS
↓
EFFECT CLASSIFICATION
↓
RISK / AUTHORITY / COMMIT REQUIREMENTS
↓
EXECUTION
↓
OBSERVED EFFECTS
```

This artifact defines an architectural model. It does not establish that the classifier is implemented or empirically validated.

---

# 1. Architectural Boundary

Effect classification belongs to the kernel because higher layers require a stable distinction between different consequence classes.

```text
CANON
↓
KERNEL EFFECT SEMANTICS
↓
CONTROL-PLANE POLICY
↓
RUNTIME ENFORCEMENT
↓
COGNITIVE / AGENT ACTION
↓
TOOLS
↓
EXTERNAL EFFECTS
```

Therefore:

```text
KERNEL
→ defines effect classes and invariants

CONTROL_PLANE
→ determines policy for those classes

RUNTIME
→ enforces applicable gates

AGENT / SKILL / WORKFLOW
→ proposes operations

TOOL
→ provides capability

EXTERNAL SYSTEM
→ receives possible effect
```

No lower layer may silently redefine the kernel effect class to obtain weaker governance.

---

# 2. Fundamental Distinctions

```text
INTENT != EFFECT

PROPOSAL != EFFECT

CAPABILITY != EFFECT

TOOL_CALL != EFFECT

STATE_MUTATION != EXTERNAL_EFFECT

READ != WRITE

WRITE != DELETE

REVERSIBLE != IRREVERSIBLE

LOCAL != GLOBAL

DIRECT != INDIRECT

IMMEDIATE != DEFERRED

OBSERVED_EFFECT != CLAIMED_EFFECT

POTENTIAL_EFFECT != REALIZED_EFFECT

INTERNAL_EFFECT != EXTERNAL_EFFECT

INFORMATIONAL_OUTPUT != AUTHORITATIVE_STATE

AUTHORITATIVE_STATE != REAL-WORLD ACTION

MODEL_PREDICTION != EFFECT

DECISION != EXECUTION

EXECUTION_SUCCESS != INTENDED_EFFECT

NO OBSERVED EFFECT != PROOF OF NO EFFECT
```

---

# 3. Effect

An effect is a material change, disclosure, commitment, influence, or externally relevant consequence attributable to an operation within a defined scope.

Conceptually:

```yaml
effect:
  effect_id:
  operation:
  actor:
  target:
  effect_type:
  scope:
  reversibility:
  persistence:
  authority_impact:
  confidentiality_impact:
  integrity_impact:
  availability_impact:
  externality:
  temporal_profile:
  dependency_impact:
  provenance:
```

An operation may produce more than one effect.

---

# 4. Effect Envelope

For operation `O`:

```text
EFFECT_ENVELOPE(O)
=
{
  E1,
  E2,
  ...,
  En
}
```

Governance must consider all **load-bearing plausible effects**, not merely the most convenient interpretation.

Thus:

```text
GOVERNANCE(O)
>=
GOVERNANCE(
  HIGHEST_MATERIAL_EFFECT(O)
)
```

subject to applicable canon and policy.

---

# 5. Primary Effect Classes

AMOS model-level primary classes:

```text
E0 — NO MATERIAL EFFECT

E1 — OBSERVATIONAL / READ EFFECT

E2 — EPHEMERAL INTERNAL EFFECT

E3 — PERSISTENT INTERNAL EFFECT

E4 — AUTHORITATIVE STATE EFFECT

E5 — EXTERNAL INFORMATION EFFECT

E6 — EXTERNAL MUTATION EFFECT

E7 — AUTHORITY / GOVERNANCE EFFECT

E8 — IRREVERSIBLE OR HIGH-CONSEQUENCE EFFECT

EX — UNKNOWN / UNCLASSIFIED EFFECT
```

These classes are proposed kernel semantics and remain `AMOS_MODEL` until promoted.

---

# 6. E0 — No Material Effect

Examples may include:

```text
PURE LOCAL CALCULATION
NON-PERSISTED TRANSFORMATION
NON-MUTATING FORMAT CONVERSION
DISCARDED SIMULATION
```

Required condition:

```text
NO MATERIAL:
  STATE CHANGE
  PERSISTENCE
  DISCLOSURE
  AUTHORITY CHANGE
  EXTERNAL MUTATION
  RESOURCE COMMITMENT
```

If any material consequence exists:

```text
NOT E0
```

---

# 7. E1 — Observational / Read Effect

Examples:

```text
READ STATE
READ MEMORY
READ FILE
QUERY DATABASE
INSPECT LOG
FETCH PUBLIC INFORMATION
```

A read can still carry:

```text
CONFIDENTIALITY RISK
PRIVACY RISK
RESOURCE COST
RATE-LIMIT EFFECT
AUDIT EFFECT
```

Therefore:

```text
READ
!=
ZERO RISK
```

and:

```text
READ AUTHORITY
MAY STILL BE REQUIRED
```

---

# 8. E2 — Ephemeral Internal Effect

Effects limited to temporary execution context.

Examples:

```text
WORKING MEMORY UPDATE
TEMPORARY PLAN
SCRATCH STATE
UNCOMMITTED HYPOTHESIS
SIMULATION STATE
```

Required property:

```text
LOSS OF EXECUTION CONTEXT
→ EFFECT DISAPPEARS
```

unless another persistence mechanism captures it.

---

# 9. E3 — Persistent Internal Effect

Effects persisted inside AMOS-managed substrates without yet constituting authoritative system state.

Examples may include:

```text
MEMORY CANDIDATE
CACHE ENTRY
CHECKPOINT
DRAFT ARTIFACT
PROVENANCE RECORD
NON-AUTHORITATIVE KNOWLEDGE CANDIDATE
```

Critical distinction:

```text
PERSISTED
!=
CANONICAL

PERSISTED
!=
AUTHORITATIVE
```

---

# 10. E4 — Authoritative State Effect

A mutation that changes authoritative AMOS state.

Examples may include:

```text
STATE COMMIT
MEMORY ADMISSION
KNOWLEDGE PROMOTION
WORKFLOW STATE TRANSITION
CONFIGURATION COMMIT
CONTROL-STATE MUTATION
```

Such operations interact directly with:

```text
K_COMMIT_TIME_AUTHORITY
K_CAPABILITY_AUTHORIZATION
K_RISK_CONSTRAINT
```

where applicable.

---

# 11. E5 — External Information Effect

Information crosses the governed AMOS boundary without necessarily mutating the external target.

Examples:

```text
SEND MESSAGE
PUBLISH OUTPUT
DISCLOSE DATA
RETURN SECRET
TRANSMIT DOCUMENT
NOTIFY EXTERNAL PARTY
```

Core law:

```text
INFORMATION LEAVING
THE GOVERNED BOUNDARY
IS AN EFFECT
```

even if no remote database mutation is visible.

---

# 12. E6 — External Mutation Effect

An operation modifies an external system or real-world state.

Examples:

```text
CREATE EXTERNAL RECORD
UPDATE EXTERNAL RECORD
DELETE EXTERNAL RECORD
SUBMIT TRANSACTION
CHANGE REMOTE CONFIGURATION
DEPLOY
EXECUTE EXTERNAL COMMAND
```

These effects normally require stronger execution governance than equivalent internal proposals.

---

# 13. E7 — Authority / Governance Effect

Operations that alter who or what may act, decide, commit, approve, supersede, or govern.

Examples:

```text
GRANT PERMISSION
REVOKE PERMISSION
CHANGE ROLE
CHANGE POLICY
CHANGE AUTHORITY EPOCH
PROMOTE CANON
CHANGE GOVERNANCE RULE
ALTER SECURITY BOUNDARY
```

Core law:

```text
AUTHORITY MUTATION
IS NOT AN ORDINARY WRITE
```

It requires governance appropriate to authority-changing consequences.

---

# 14. E8 — Irreversible / High-Consequence Effect

Effects whose rollback is impossible, unreliable, disproportionately costly, legally significant, safety-critical, or otherwise highly consequential.

Possible examples:

```text
IRREVERSIBLE EXTERNAL ACTION
DESTRUCTIVE DELETE WITHOUT RECOVERY
HIGH-VALUE FINANCIAL COMMITMENT
SAFETY-CRITICAL ACTUATION
PUBLICATION WITH MATERIAL CONSEQUENCE
PERMANENT CREDENTIAL REVOCATION
```

Classification depends on context.

The operation name alone does not establish `E8`.

---

# 15. EX — Unknown / Unclassified

If the material effect envelope cannot be established:

```text
EFFECT_CLASS = EX
```

For consequential operations:

```text
UNKNOWN EFFECT
→ DO NOT ASSUME LOW EFFECT
```

Instead:

```text
CLASSIFY
OR
ESCALATE
OR
CONSTRAIN
OR
DENY
```

according to applicable governance.

---

# 16. Effect Dimensions

Primary class alone may be insufficient.

Each material effect may carry orthogonal dimensions.

```yaml
effect_dimensions:
  locus:
  persistence:
  reversibility:
  scope:
  timing:
  directness:
  authority_impact:
  confidentiality_impact:
  integrity_impact:
  availability_impact:
  financial_impact:
  legal_impact:
  safety_impact:
  governance_impact:
  dependency_impact:
```

---

# 17. Locus

```text
INTERNAL
EXTERNAL
CROSS_BOUNDARY
HYBRID
```

Do not infer locus from the executing component.

An internal agent can produce an external effect.

An external tool can sometimes produce only an observational effect.

---

# 18. Persistence

```text
EPHEMERAL
SESSION
BOUNDED
PERSISTENT
PERMANENT
UNKNOWN
```

Persistence affects recovery and authority requirements.

---

# 19. Reversibility

```text
R0 — TRIVIALLY REVERSIBLE
R1 — REVERSIBLE
R2 — COMPENSATABLE
R3 — PARTIALLY REVERSIBLE
R4 — PRACTICALLY IRREVERSIBLE
RX — UNKNOWN
```

Important:

```text
COMPENSATION
!=
ROLLBACK
```

Sending a correction after disclosure does not undo the disclosure.

---

# 20. Scope

```text
OBJECT
LOCAL
SHARD
SUBSYSTEM
DOMAIN
SYSTEM
MULTI-SYSTEM
PUBLIC / REAL-WORLD
UNKNOWN
```

A small operation may have large dependency consequences.

Therefore:

```text
TARGET SIZE
!=
BLAST RADIUS
```

---

# 21. Timing

```text
IMMEDIATE
DEFERRED
SCHEDULED
CONDITIONAL
RECURRING
LONG-LIVED
```

Deferred effects must not be treated as harmless merely because execution happens later.

---

# 22. Directness

```text
DIRECT
INDIRECT
SECOND_ORDER
CASCADE
UNKNOWN
```

Example:

```text
CHANGE CONFIGURATION
↓
RESTART SERVICE
↓
ALTER TRAFFIC
↓
AFFECT USERS
```

The first mutation can carry downstream effects even when those effects are not immediate.

---

# 23. Potential vs Realized Effect

Before execution:

```text
POTENTIAL_EFFECT
```

After execution:

```text
REALIZED_EFFECT
```

Governance normally must reason from credible potential effects.

Otherwise dangerous actions could bypass controls merely because harm has not happened yet.

---

# 24. Intended vs Actual Effect

```text
INTENDED_EFFECT
!=
ACTUAL_EFFECT
```

AMOS should preserve both where material.

Conceptually:

```yaml
effect_result:
  intended:
  predicted:
  observed:
  unexpected:
```

Unexpected effects become evidence for future classification and recovery.

---

# 25. Direct and Cascading Effects

For operation `O`:

```text
DIRECT_EFFECTS(O)
```

may induce:

```text
CASCADE_EFFECTS(O)
```

through dependency edges.

Conceptually:

```text
O
→ E1
→ dependency D1
→ E2
→ dependency D2
→ E3
```

Effect classification should traverse only dependencies capable of materially changing governance.

---

# 26. Effect Dependency Closure

Define:

```text
EFFECT_CLOSURE(O)
```

as the smallest sufficient set of plausible downstream consequences required for the current decision.

Do not expand to the entire universe of theoretically possible consequences.

Do not stop before load-bearing consequences.

This follows the v4.4 smallest-sufficient-proof principle.

---

# 27. Hidden Effect Firewall

A declared low-impact action does not establish low impact.

Example:

```text
OPERATION LABEL:
  "UPDATE CACHE"
```

but actual dependency:

```text
CACHE
→ AUTHORIZATION DECISIONS
```

Then the operation may carry an authority-relevant effect.

Core law:

```text
LABEL
!=
EFFECT
```

---

# 28. Tool Effect Firewall

Tool identity does not determine permission or consequence.

```text
TOOL != PERMISSION
TOOL != AUTHORITY
TOOL != EFFECT CLASS
```

The same tool can support:

```text
READ
WRITE
DELETE
PUBLISH
EXECUTE
```

with different effect classes.

Classification attaches to the actual operation.

---

# 29. Agent Effect Firewall

```text
AGENT ROLE
!=
EFFECT CLASS
```

A "research agent" can still produce an external effect if permitted to send, write, publish, or mutate.

A "deployment agent" can perform a read-only inspection.

Classification follows consequences, not labels.

---

# 30. Skill Effect Firewall

```text
SKILL != EFFECT
```

A skill may contain multiple actions with different effects.

Example:

```text
SKILL:
  inspect repository   → E1
  create patch         → E3
  commit state         → E4
  deploy externally    → E6/E8
```

Governance must not flatten the entire skill into one assumed effect unless explicitly valid.

---

# 31. Workflow Effect Composition

A workflow may contain:

```text
STEP A → E1
STEP B → E3
STEP C → E4
STEP D → E6
```

Workflow governance must account for the highest material effect actually reachable under the execution path.

```text
WORKFLOW_EFFECT
!=
FIRST_STEP_EFFECT
```

---

# 32. Conditional Branches

For:

```text
IF X:
  READ
ELSE:
  DELETE
```

the workflow cannot globally be treated as read-only.

Before the branch is resolved:

```text
POTENTIAL EFFECT ENVELOPE
INCLUDES DELETE
```

unless runtime architecture guarantees the destructive branch is unreachable.

---

# 33. Multi-Effect Operations

One operation may simultaneously cause:

```text
STATE MUTATION
+
INFORMATION DISCLOSURE
+
AUTHORITY CHANGE
```

Do not force a single lossy class if multiple dimensions remain governance-relevant.

Represent:

```text
PRIMARY_EFFECT
+
SECONDARY_EFFECTS
+
DIMENSIONS
```

or an equivalent typed structure.

---

# 34. Highest-Governance Rule

Where effect classes impose different governance strength:

```text
REQUIRED_GOVERNANCE(O)
=
MAX_GOVERNANCE(
  MATERIAL_EFFECTS(O)
)
```

This is a conceptual ordering, not necessarily a single numeric scale.

Some effects may be incomparable.

Example:

```text
PRIVACY DISCLOSURE
vs
SERVICE AVAILABILITY MUTATION
```

may require different controls rather than one scalar rank.

---

# 35. Incomparable Effects

Do not force:

```text
EFFECT A > EFFECT B
```

when they are governed along different dimensions.

Preserve:

```text
MULTI-DIMENSIONAL EFFECT PROFILE
```

when scalar ordering loses material information.

---

# 36. Effect Classification and Risk

Effect class informs risk.

It does not equal risk.

```text
EFFECT_CLASS != RISK_CLASS
```

Risk may depend on:

```text
PROBABILITY
MAGNITUDE
REVERSIBILITY
SCOPE
EXPOSURE
DEPENDENCIES
UNCERTAINTY
```

Thus:

```text
EFFECT
→ INPUT TO RISK

EFFECT
!=
RISK
```

---

# 37. Effect Classification and Authority

Effect class can determine which authority is required.

Example:

```text
READ RESOURCE
```

may require one authority envelope.

```text
DELETE RESOURCE
```

may require another.

But:

```text
EFFECT_CLASS
!=
AUTHORITY
```

Classification informs the authority gate; it does not grant authority.

---

# 38. Effect Classification and Commit Time

Before authoritative commit:

```text
PROPOSED EFFECT ENVELOPE
```

must remain compatible with the authority under which the exact commit occurs.

If the effect changes materially between authorization and commit:

```text
RECLASSIFY
↓
REVALIDATE AUTHORITY
```

---

# 39. Effect Drift

Effect drift occurs when:

```text
EFFECT_CLASS(T0)
!=
EFFECT_CLASS(T1)
```

or when effect dimensions materially change.

Possible causes:

```text
TARGET CHANGE
DEPENDENCY CHANGE
REGIME CHANGE
CONFIGURATION CHANGE
TOOL BEHAVIOR CHANGE
WORKFLOW BRANCH CHANGE
SCOPE EXPANSION
```

Material drift invalidates effect-dependent proofs.

---

# 40. Regime Sensitivity

The same operation can have different effects under different regimes.

Example:

```text
WRITE TO SANDBOX
```

versus:

```text
WRITE TO PRODUCTION
```

Therefore:

```text
EFFECT(O, SANDBOX)
!=
EFFECT(O, PRODUCTION)
```

where the environments differ materially.

Effect classification inherits regime.

---

# 41. Temporal Sensitivity

An operation may change effect over time.

Example:

```text
DELETE TEMPORARY COPY
```

may be reversible while backups exist and effectively irreversible after backup expiry.

Effect classification therefore may require:

```text
VALID_AT
VALID_UNTIL
FRESHNESS
```

---

# 42. Provenance

Material effect classification should record why the classification exists.

Possible evidence types:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
UNKNOWN
```

Example:

```text
TOOL DOCUMENTATION SAYS "READ ONLY"
```

is initially:

```text
SOURCE_CLAIM
```

not necessarily verified runtime behavior.

---

# 43. Effect Evidence Independence

Multiple descriptions copied from one source do not independently prove an effect class.

```text
DOC A
DOC B ← copied from A
DOC C ← generated from A
```

does not equal three independent confirmations.

Correlated provenance must remain visible when consequential.

---

# 44. Conservative Classification Under Ambiguity

AMOS should not automatically classify every uncertain operation into the maximum imaginable class.

That would destroy usefulness.

Instead:

```text
IDENTIFY
THE SMALLEST
DECISION-RELEVANT
UNCERTAINTY
```

then resolve it.

If uncertainty cannot be resolved and stakes are consequential:

```text
EX
→ CONSTRAIN / ESCALATE / DENY
```

according to policy.

---

# 45. Cheap Discriminating Tests

Prefer tests that sharply distinguish effect hypotheses.

Example competing hypotheses:

```text
H1:
TOOL CALL IS READ-ONLY

H2:
TOOL CALL MUTATES REMOTE STATE
```

A high-information test may be:

```text
CHECK TOOL CONTRACT
OR
OBSERVE CONTROLLED SANDBOX BEHAVIOR
```

rather than accumulating generic documentation.

---

# 46. Competing Effect Hypotheses

If credible evidence supports incompatible classifications:

```text
H1 = E1
H2 = E6
```

and no valid precedence or discriminating evidence resolves them:

```text
EFFECT_CLASS = COMPETING
```

Do not silently choose the more convenient class.

---

# 47. Causal Firewall

Observed sequence alone does not prove an effect.

```text
OPERATION O
THEN EVENT E
```

does not establish:

```text
O CAUSED E
```

Effect attribution must distinguish:

```text
ASSOCIATION
CORRELATION
MECHANISM
ENABLING CONDITION
NECESSARY CONDITION
SUFFICIENT CONDITION
CAUSAL EFFECT
```

where consequential.

---

# 48. External Effect Boundary

External effects deserve explicit representation.

```text
INTERNAL INTENT
↓
EXTERNAL EFFECT GATE
↓
TOOL / INTERFACE
↓
EXTERNAL SYSTEM
```

Core invariant:

```text
INTERNAL AUTHORIZATION
DOES NOT SILENTLY
BECOME EXTERNAL-EFFECT AUTHORIZATION
```

---

# 49. Disclosure Is an Effect

Sending information outside its authorized boundary is a real effect even if nothing is "written" in the conventional database sense.

```text
READ SECRET
↓
DISPLAY SECRET TO UNAUTHORIZED TARGET
```

includes:

```text
E1
+
E5
```

The read classification alone is insufficient.

---

# 50. Resource Consumption Effects

Operations may have material resource effects:

```text
COMPUTE
STORAGE
BANDWIDTH
API QUOTA
FINANCIAL COST
RATE LIMIT
```

These can require separate effect dimensions even when the primary functional action is observational.

---

# 51. Availability Effects

An operation may change service availability without changing persistent data.

Examples:

```text
STOP PROCESS
EXHAUST CONNECTION POOL
LOCK RESOURCE
SATURATE QUOTA
```

Thus:

```text
NO DATA WRITE
!=
NO MATERIAL EFFECT
```

---

# 52. Security Effects

Security-relevant effects include:

```text
CREDENTIAL EXPOSURE
PERMISSION CHANGE
TRUST-BOUNDARY CHANGE
ATTACK-SURFACE CHANGE
AUDIT-DISABLING CHANGE
SECURITY-POLICY CHANGE
```

Some overlap with `E5`, `E6`, and `E7`.

The security dimension should remain explicit.

---

# 53. Knowledge Effects

Knowledge operations must distinguish:

```text
GENERATE CLAIM
STORE CLAIM
VALIDATE CLAIM
PROMOTE CLAIM
SUPERSEDE CLAIM
DELETE CLAIM
```

These have different authority and persistence consequences.

```text
GENERATED KNOWLEDGE
!=
VALIDATED KNOWLEDGE
```

---

# 54. Memory Effects

Memory operations distinguish:

```text
MEMORY CANDIDATE
MEMORY ADMISSION
MEMORY UPDATE
MEMORY SUPERSESSION
MEMORY DELETION
```

A conversational inference must not become persistent memory merely because it was generated.

---

# 55. Canon Effects

Canon operations distinguish:

```text
DRAFT
PROPOSE
REVIEW
PROMOTE
SUPERSEDE
DEPRECATE
```

Core law:

```text
DRAFT CANON
!=
CANON EFFECT
```

Only governed promotion changes authoritative canon.

---

# 56. Authority Effects

Operations that alter authorization topology should be explicitly flagged:

```yaml
authority_effect:
  grants:
  revokes:
  delegates:
  changes_scope:
  changes_precedence:
  changes_epoch:
```

Authority changes can affect many downstream decisions even if the direct mutation is small.

---

# 57. Effect Atomicity

For atomic transaction:

```text
T = {E1, E2, E3}
```

AMOS must reason about the effect set as a whole.

If only a subset is authorized:

```text
ATOMIC T
→ NO COMMIT
```

unless decomposition is valid and explicitly permitted.

---

# 58. Partial Effects

Failure during execution may produce:

```text
PARTIAL EFFECT
```

Example:

```text
STEP 1 COMMITTED
STEP 2 FAILED
```

Therefore execution outcomes include more than:

```text
SUCCESS
FAILURE
```

They may include:

```text
NO_EFFECT
FULL_EFFECT
PARTIAL_EFFECT
UNKNOWN_EFFECT
```

---

# 59. Compensation

When rollback is unavailable:

```text
COMPENSATING ACTION
```

may reduce consequences.

But:

```text
COMPENSATED
!=
NEVER HAPPENED
```

Provenance of the original effect must remain.

---

# 60. Irreversibility Gate

Before an operation classified as materially irreversible:

```text
VERIFY:
  EFFECT
  TARGET
  SCOPE
  AUTHORITY
  RISK
  PRECONDITIONS
  RECOVERY OPTIONS
```

Validation strength should increase with irreversible stakes.

---

# 61. Effect Classification Record

```yaml
effect_classification:
  classification_id:

  operation:
  actor:
  target:

  primary_class:
  secondary_classes: []

  dimensions:
    locus:
    persistence:
    reversibility:
    scope:
    timing:
    directness:

  impact:
    confidentiality:
    integrity:
    availability:
    authority:
    governance:
    financial:
    legal:
    safety:

  regime:
  valid_at:
  freshness:

  evidence: []
  provenance: []
  dependencies: []
  competing_hypotheses: []
  falsifiers: []
  invalidation_conditions: []

  conclusion_class:
  confidence_ceiling:
```

---

# 62. Conclusion Classes

Effect conclusions use the weakest accurate class:

```text
VERIFIED
DERIVED
MODEL
CONDITIONAL
COMPETING
UNKNOWN/GAP
```

Examples:

```text
DOCUMENTATION ONLY
→ SOURCE_CLAIM / MODEL-level support

OBSERVED SANDBOX BEHAVIOR
→ OBSERVATION within sandbox scope

CROSS-REGIME GENERALIZATION
→ CONDITIONAL unless validated

UNRESOLVED CONFLICT
→ COMPETING
```

---

# 63. Confidence Ceiling

For derived classification `EC`:

```text
CONFIDENCE(EC)
≤
MIN(
  OPERATION_IDENTITY,
  TARGET_IDENTITY,
  TOOL_BEHAVIOR_EVIDENCE,
  DEPENDENCY_MODEL,
  REGIME_MATCH,
  TEMPORAL_FRESHNESS,
  PROVENANCE_INDEPENDENCE
)
```

A weak load-bearing premise caps the effect classification.

---

# 64. Sensitivity

Identify the smallest premise capable of changing governance.

Examples:

```text
IS TARGET PRODUCTION?
IS WRITE PERSISTENT?
DOES THIS SEND DATA EXTERNALLY?
CAN DELETE BE RESTORED?
DOES THIS CHANGE AUTHORITY?
DOES THIS TOOL ACTUALLY MUTATE?
```

Test that premise first.

---

# 65. Adversarial Validation

For consequential classifications, challenge the initial result through a different path.

Seek:

```text
HIDDEN WRITE
HIDDEN DISCLOSURE
HIDDEN EXTERNAL CALL
HIDDEN AUTHORITY CHANGE
HIDDEN CASCADE
STALE TOOL CONTRACT
SCOPE LEAKAGE
REGIME MISMATCH
CORRELATED EVIDENCE
IRREVERSIBILITY MISCLASSIFICATION
```

If challenge succeeds:

```text
RECLASSIFY
OR
CONDITION
OR
PRESERVE COMPETING
OR
RETURN UNKNOWN/GAP
```

---

# 66. Invalidation

```text
INVALID(p)
→ INVALIDATE ONLY
EFFECT CLASSIFICATIONS
DEPENDENT ON p
```

Examples:

```text
TOOL VERSION CHANGED
TARGET CHANGED
DEPENDENCY TOPOLOGY CHANGED
REGIME CHANGED
POLICY CHANGED
REVERSIBILITY ASSUMPTION FAILED
```

Unaffected classifications remain reusable.

---

# 67. Failure Recovery

When effect classification proves wrong:

```text
DETECT MISMATCH
↓
PRESERVE OBSERVATION
↓
IDENTIFY FAILED PREMISE
↓
INVALIDATE DEPENDENT CLASSIFICATIONS
↓
CLASSIFY REALIZED EFFECT
↓
CONTAIN CONSEQUENCES
↓
ROLL BACK OR COMPENSATE
↓
UPDATE EFFECT MODEL
↓
REVALIDATE AFFECTED OPERATIONS
```

Do not erase the misclassification evidence.

---

# 68. Observability Events

Recommended events:

```text
EFFECT_CLASSIFICATION_STARTED
EFFECT_CLASSIFIED
EFFECT_CLASS_UNKNOWN
EFFECT_CLASS_COMPETING
EFFECT_RECLASSIFIED
EFFECT_DRIFT_DETECTED
EFFECT_SCOPE_CHANGED
EFFECT_REGIME_CHANGED
EFFECT_IRREVERSIBILITY_DETECTED
EXTERNAL_EFFECT_REQUESTED
EXTERNAL_EFFECT_AUTHORIZED
EXTERNAL_EFFECT_DENIED
EFFECT_EXECUTION_STARTED
EFFECT_OBSERVED
UNEXPECTED_EFFECT_OBSERVED
PARTIAL_EFFECT_DETECTED
EFFECT_ROLLBACK_STARTED
EFFECT_COMPENSATION_STARTED
EFFECT_RECOVERY_COMPLETED
```

---

# 69. Kernel Invariants

```text
KEC-01
INTENT MUST NOT BE TREATED AS EFFECT

KEC-02
TOOL IDENTITY MUST NOT DETERMINE EFFECT CLASS BY ITSELF

KEC-03
AGENT IDENTITY MUST NOT DETERMINE EFFECT CLASS BY ITSELF

KEC-04
SKILL IDENTITY MUST NOT DETERMINE EFFECT CLASS BY ITSELF

KEC-05
READ MUST NOT BE TREATED AS ZERO EFFECT

KEC-06
PERSISTENCE MUST NOT BE TREATED AS AUTHORITY

KEC-07
PERSISTENT INTERNAL STATE MUST NOT BE TREATED AS CANON BY DEFAULT

KEC-08
INTERNAL COMMIT MUST NOT BE TREATED AS EXTERNAL EFFECT

KEC-09
INFORMATION DISCLOSURE MUST BE REPRESENTABLE AS AN EFFECT

KEC-10
AUTHORITY MUTATION MUST BE REPRESENTABLE AS A DISTINCT EFFECT

KEC-11
UNKNOWN EFFECT MUST NOT SILENTLY DOWNGRADE TO LOW EFFECT

KEC-12
MATERIAL EFFECT DRIFT MUST INVALIDATE EFFECT-DEPENDENT AUTHORIZATION

KEC-13
REVERSIBILITY MUST NOT BE ASSUMED FROM OPERATION LABELS

KEC-14
COMPENSATION MUST NOT BE EQUATED WITH ROLLBACK

KEC-15
POTENTIAL MATERIAL EFFECTS MUST BE CONSIDERED BEFORE EXECUTION

KEC-16
ACTUAL EFFECT MUST NOT BE ASSUMED FROM INTENDED EFFECT

KEC-17
CAUSAL ATTRIBUTION MUST NOT BE INFERRED FROM SEQUENCE ALONE

KEC-18
MULTI-EFFECT OPERATIONS MUST NOT LOSE LOAD-BEARING EFFECT DIMENSIONS

KEC-19
ATOMIC OPERATIONS REQUIRE GOVERNANCE FOR THE COMPLETE MATERIAL EFFECT SET

KEC-20
PARTIAL EFFECTS MUST REMAIN REPRESENTABLE

KEC-21
EFFECT CLASSIFICATION MUST INHERIT APPLICABLE REGIME

KEC-22
EFFECT CLASSIFICATION MUST BE FRESHNESS-BOUNDED WHERE BEHAVIOR CAN CHANGE

KEC-23
EFFECT PROVENANCE MUST REMAIN RECOVERABLE

KEC-24
CORRELATED EFFECT EVIDENCE MUST NOT BE COUNTED AS INDEPENDENT WITHOUT SUPPORT

KEC-25
EFFECT CLASS MUST NOT ITSELF GRANT AUTHORITY

KEC-26
LOW RISK MUST NOT PROVE LOW EFFECT

KEC-27
LOW EFFECT MUST NOT PROVE AUTHORIZATION

KEC-28
LOCAL TARGET SIZE MUST NOT PROVE LOCAL BLAST RADIUS

KEC-29
NO OBSERVED EFFECT MUST NOT PROVE NO EFFECT WHEN OBSERVABILITY IS INCOMPLETE

KEC-30
IRREVERSIBLE EFFECTS REQUIRE STRONGER GOVERNANCE PROPORTIONAL TO STAKES
```

---

# 70. Required Tests

```text
INTENT-EFFECT-SEPARATION TEST
TOOL-EFFECT-SEPARATION TEST
AGENT-EFFECT-SEPARATION TEST
SKILL-EFFECT-SEPARATION TEST
READ-EFFECT TEST
PERSISTENCE-AUTHORITY-SEPARATION TEST
INTERNAL-EXTERNAL-EFFECT-SEPARATION TEST
DISCLOSURE-EFFECT TEST
AUTHORITY-EFFECT TEST
UNKNOWN-EFFECT TEST
EFFECT-DRIFT TEST
TARGET-CHANGE TEST
REGIME-SHIFT TEST
REVERSIBILITY TEST
COMPENSATION-VS-ROLLBACK TEST
POTENTIAL-VS-REALIZED-EFFECT TEST
INTENDED-VS-ACTUAL-EFFECT TEST
CASCADE-EFFECT TEST
HIDDEN-DEPENDENCY TEST
MULTI-EFFECT TEST
ATOMIC-EFFECT TEST
PARTIAL-EFFECT TEST
PROVENANCE-INDEPENDENCE TEST
FRESHNESS TEST
IRREVERSIBILITY-GATE TEST
EXTERNAL-EFFECT-AUTHORITY TEST
```

---

# 71. Negative Tests

```text
TOOL IS READ TOOL
→ OPERATION IS READ-ONLY
MUST FAIL WITHOUT OPERATION EVIDENCE

AGENT IS RESEARCH AGENT
→ CANNOT PRODUCE EXTERNAL EFFECT
MUST FAIL

NO DATABASE WRITE
→ NO EFFECT
MUST FAIL

PERSISTED
→ AUTHORITATIVE
MUST FAIL

AUTHORITATIVE INTERNAL STATE
→ EXTERNAL ACTION AUTHORIZED
MUST FAIL

SEND INFORMATION
→ READ-ONLY EFFECT
MUST FAIL

REVERSIBLE IN SANDBOX
→ REVERSIBLE IN PRODUCTION
MUST FAIL

TARGET IS SMALL
→ BLAST RADIUS IS SMALL
MUST FAIL

DOCUMENTATION SAYS READ-ONLY
→ VERIFIED READ-ONLY
MUST FAIL WITHOUT REQUIRED VALIDATION

NO EFFECT OBSERVED
→ NO EFFECT OCCURRED
MUST FAIL WHEN OBSERVABILITY IS INCOMPLETE

OPERATION PREVIOUSLY E1
→ ALWAYS E1
MUST FAIL

ONE STEP E1
→ WORKFLOW E1
MUST FAIL WHEN HIGHER-EFFECT BRANCHES EXIST

COMPENSATABLE
→ REVERSIBLE
MUST FAIL

LOW EFFECT
→ AUTHORIZED
MUST FAIL

HIGH EFFECT
→ DEFINITELY HIGH RISK
MUST FAIL WITHOUT CONTEXT

UNKNOWN EFFECT
→ E0
MUST FAIL
```

---

# 72. Failure Modes

```text
EFFECT UNDERCLASSIFICATION
EFFECT OVERCLASSIFICATION
HIDDEN WRITE
HIDDEN DISCLOSURE
HIDDEN AUTHORITY MUTATION
HIDDEN CASCADE
FALSE REVERSIBILITY
FALSE LOCALITY
REGIME LEAKAGE
STALE CLASSIFICATION
TARGET SUBSTITUTION
TOOL BEHAVIOR DRIFT
WORKFLOW BRANCH BLINDNESS
PARTIAL-EFFECT BLINDNESS
CORRELATED-EVIDENCE OVERCONFIDENCE
INTENT/EFFECT CONFUSION
COMMIT/EFFECT CONFUSION
COMPENSATION/ROLLBACK CONFUSION
CAUSAL OVERATTRIBUTION
PROVENANCE LOSS
```

---

# 73. Interaction Matrix

```text
K_CAPABILITY_AUTHORIZATION
→ DETERMINES WHETHER CAPABILITY USE IS AUTHORIZED

K_EFFECT_CLASSIFICATION
→ DETERMINES WHAT CONSEQUENCE CLASS THE OPERATION CARRIES

K_RISK_CONSTRAINT
→ EVALUATES RISK OF CLASSIFIED EFFECTS

K_COMMIT_TIME_AUTHORITY
→ REVALIDATES AUTHORITY FOR AUTHORITATIVE COMMIT EFFECTS

K_CAUSAL_CLOSURE
→ IDENTIFIES MATERIAL DOWNSTREAM EFFECT DEPENDENCIES

K_CAUSAL_EPOCH
→ BOUNDS CAUSAL VALIDITY

K_SYSTEM_STATE
→ PROVIDES STATE / TARGET CONTEXT

K_CONTEXT_STATE
→ PROVIDES EXECUTION CONTEXT

CONTROL_PLANE
→ MAPS EFFECT CLASSES TO POLICY

RUNTIME
→ ENFORCES EFFECT-SENSITIVE GATES

MEMORY
→ RECEIVES MEMORY EFFECTS

KNOWLEDGE
→ RECEIVES KNOWLEDGE EFFECTS

STATE
→ RECEIVES AUTHORITATIVE STATE EFFECTS

TOOLS
→ REALIZE CAPABILITIES

INTERFACES
→ MEDIATE BOUNDARY EFFECTS

OBSERVABILITY
→ RECORDS REALIZED EFFECTS

SECURITY
→ CONSTRAINS SECURITY-RELEVANT EFFECTS

TESTS
→ VALIDATE EFFECT CLASSIFICATION CONTRACTS

OPERATIONS
→ HANDLE RECOVERY / COMPENSATION
```

---

# 74. Promotion Gate

Before promotion beyond `AMOS_MODEL`, evidence should establish:

```text
[ ] effect taxonomy approved
[ ] effect schema implemented
[ ] primary effect classes implemented
[ ] effect dimensions implemented
[ ] tool-operation effect mapping implemented
[ ] internal/external boundary defined
[ ] disclosure classification implemented
[ ] authority-effect classification implemented
[ ] reversibility semantics implemented
[ ] effect dependency closure implemented
[ ] regime-sensitive classification implemented
[ ] freshness semantics implemented
[ ] effect drift detection implemented
[ ] multi-effect representation implemented
[ ] atomic effect handling implemented
[ ] partial-effect representation implemented
[ ] unknown-effect handling implemented
[ ] competing-effect handling implemented
[ ] provenance capture implemented
[ ] effect-sensitive authority integration implemented
[ ] effect-sensitive risk integration implemented
[ ] commit-time effect revalidation implemented
[ ] external-effect gating implemented
[ ] observability implemented
[ ] recovery / compensation tested
[ ] adversarial effect-classification tests passed
[ ] unresolved critical gaps registered
```

Until evidenced:

```text
EFFECT_CLASSIFIER_RUNTIME = UNKNOWN/GAP
EFFECT_TAXONOMY_CANON_STATUS = UNKNOWN/GAP
TOOL_EFFECT_MAPPING = UNKNOWN/GAP
EFFECT_DRIFT_ENFORCEMENT = UNKNOWN/GAP
EXTERNAL_EFFECT_GATE = UNKNOWN/GAP
REVERSIBILITY_VALIDATION = UNKNOWN/GAP
CASCADE_EFFECT_MODEL = UNKNOWN/GAP
PARTIAL_EFFECT_RECOVERY = UNKNOWN/GAP
EMPIRICAL_VALIDATION = UNKNOWN/GAP
FORMAL_VERIFICATION = UNKNOWN/GAP
```

---

# 75. RSCF Node

```RSCF-NODE
node_id: AMOS-OS-K-EFFECT-CLASSIFICATION
node_type: kernel_effect_classification_contract
domain: AMOS_OS_KERNEL
functional_type: EffectClassificationKernel
lifecycle_stage: Architecture
claim_class: AMOS_MODEL

RSCF-RELATIONS:
  - ROOTED_IN: README
  - DEPENDENCY_BOUND_TO: DEPENDENCY_MAP

  - GOVERNED_BY: AMOS_CORE_LAWS
  - CONSTRAINED_BY: INVARIANT_REGISTRY
  - PRECEDENCE_GOVERNED_BY: LAW_HIERARCHY
  - AUTHORITY_GOVERNED_BY: AUTHORITY_CANON
  - PROVENANCE_GOVERNED_BY: CANON_PROVENANCE

  - INDEXED_BY: KERNEL_MAP
  - LOGIC_BOUND_TO: K_CORE19_LOGIC
  - STRUCTURE_BOUND_TO: K_STRUCTURAL_REASONING
  - CAUSAL_BOUND_TO: K_CAUSAL_CLOSURE
  - CAUSAL_EPOCH_BOUND_TO: K_CAUSAL_EPOCH
  - STATE_BOUND_TO: K_SYSTEM_STATE
  - CONTEXT_BOUND_TO: K_CONTEXT_STATE
  - AUTHORIZATION_BOUND_TO: K_CAPABILITY_AUTHORIZATION
  - COMMIT_AUTHORITY_BOUND_TO: K_COMMIT_TIME_AUTHORITY
  - RISK_BOUND_TO: K_RISK_CONSTRAINT
  - EVENT_BOUND_TO: K_EVENT_BUS

  - POLICY_BOUND_TO: README
  - EXECUTION_BOUND_TO: README

  - MEMORY_BOUND_TO: README
  - KNOWLEDGE_BOUND_TO: README
  - AUTHORITATIVE_STATE_BOUND_TO: README

  - TOOL_BOUND_TO: README
  - INTERFACE_BOUND_TO: README

  - OBSERVED_BY: README
  - SECURITY_BOUND_TO: README
  - VERIFIED_BY: README
  - RECOVERED_BY: README
```

---

# 76. Canonical Summary

```text
AMOS DOES NOT ASK ONLY:

WHAT ACTION
WAS REQUESTED?

AMOS ASKS:

WHAT CAN THIS
OPERATION
ACTUALLY CHANGE?
```

Core laws:

```text
INTENT != EFFECT
CAPABILITY != EFFECT
TOOL != EFFECT
AGENT != EFFECT
SKILL != EFFECT

READ != ZERO EFFECT
PERSISTENCE != AUTHORITY
INTERNAL STATE != EXTERNAL EFFECT
DISCLOSURE IS AN EFFECT
AUTHORITY CHANGE IS AN EFFECT

POTENTIAL EFFECT != REALIZED EFFECT
INTENDED EFFECT != ACTUAL EFFECT

REVERSIBLE != COMPENSATABLE
LOCAL TARGET != LOCAL BLAST RADIUS

EFFECT CLASS != RISK
EFFECT CLASS != AUTHORITY

UNKNOWN EFFECT != LOW EFFECT
COMPETING EFFECTS != CONVERGED EFFECT

NO OBSERVED EFFECT
!=
PROOF OF NO EFFECT
```

The decisive invariant is:

```text
BEFORE AMOS
AUTHORIZES,
COMMITS,
OR EXECUTES
A CONSEQUENTIAL
OPERATION,

IT MUST KNOW
ENOUGH TO DETERMINE:

WHAT
CAN CHANGE?

WHERE
CAN IT CHANGE?

WHO OR WHAT
CAN BE AFFECTED?

DOES INFORMATION
CROSS A BOUNDARY?

DOES STATE
BECOME PERSISTENT?

DOES STATE
BECOME AUTHORITATIVE?

DOES AN
EXTERNAL SYSTEM
CHANGE?

DOES AUTHORITY
CHANGE?

HOW LARGE
IS THE
EFFECT SCOPE?

IS THE EFFECT
REVERSIBLE?

IS IT ONLY
COMPENSATABLE?

CAN EFFECTS
CASCADE THROUGH
DEPENDENCIES?

IS THE
CLASSIFICATION
VALID IN THIS
REGIME?

IS IT
FRESH?

HAS THE
TARGET CHANGED?

HAS TOOL
BEHAVIOR CHANGED?

ARE THERE
HIDDEN EFFECTS?

ARE MULTIPLE
EFFECT CLAIMS
ACTUALLY
INDEPENDENT?

IS THE EFFECT
KNOWN,
CONDITIONAL,
COMPETING,
OR UNKNOWN?

IF THE
EFFECT ENVELOPE
MATERIALLY CHANGES,

RECLASSIFY.

IF GOVERNANCE
DEPENDED ON THE
OLD CLASSIFICATION,

REVALIDATE.

IF THE EFFECT
IS UNKNOWN
AND CONSEQUENTIAL,

DO NOT
ASSUME LOW IMPACT.

CLASSIFY,
CONSTRAIN,
ESCALATE,
OR DENY.

ONLY AFTER
THE MATERIAL
EFFECT ENVELOPE
IS SUFFICIENTLY
ESTABLISHED

MAY AUTHORITY,
RISK,
COMMIT,
AND EXECUTION
REASONING
RELY ON IT.
```

## Related

[[README]] ·
[[DEPENDENCY_MAP]] ·
[[AMOS_CORE_LAWS]] ·
[[INVARIANT_REGISTRY]] ·
[[LAW_HIERARCHY]] ·
[[AUTHORITY_CANON]] ·
[[CANON_PROVENANCE]] ·
[[KERNEL_MAP]] ·
[[K_CORE19_LOGIC]] ·
[[K_STRUCTURAL_REASONING]] ·
[[K_CAUSAL_CLOSURE]] ·
[[K_CAUSAL_EPOCH]] ·
[[K_SYSTEM_STATE]] ·
[[K_CONTEXT_STATE]] ·
[[K_CAPABILITY_AUTHORIZATION]] ·
[[K_COMMIT_TIME_AUTHORITY]] ·
[[K_RISK_CONSTRAINT]] ·
[[K_EVENT_BUS]] ·
README ·
README ·
README ·
README ·
README ·
README ·
README ·
[[README]] ·
README ·
[[README]] ·
README

```text

**Classification note:** this is substantive replacement content for `02_KERNEL/K_EFFECT_CLASSIFICATION.md`, but remains **AMOS_MODEL**. It defines the proposed effect semantics needed to connect capability authorization, commit-time authority, risk constraints, causal closure, runtime execution, and external-effect governance. It does **not** establish implementation, empirical validation, formal verification, or canonical promotion; those remain `UNKNOWN/GAP` until supported by provenance and test evidence.
```

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00_ROOT/00-Home]] · [[AMOS_RSCF_NODES]]

---
**MOC:** [[07_AUTHORITY_MOC]]
