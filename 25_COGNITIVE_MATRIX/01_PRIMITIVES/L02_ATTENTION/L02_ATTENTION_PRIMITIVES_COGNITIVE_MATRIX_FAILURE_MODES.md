---
type: failure-mode
source: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L02_ATTENTION
tags:
- amos
- cognitive-matrix
- matrix/l02
- attention
- failure-modes
- rscf
- hml
- domain/cognitive-matrix
title: L02_ATTENTION — Failure Modes
origin_architect: Trang Phan
status: MODEL_SPECIFICATION / UNVALIDATED
epistemic_class: MODEL
runtime_alignment: AMOS Full Brain OS / AMOS_CORE v4.4 lineage
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# L02_ATTENTION — Failure Modes

**Class:** `COGNITIVE_PRIMITIVE_FAILURE_CONTRACT`
**Origin architect / steward:** Trang Phan
**Primitive:** `L02_ATTENTION`
**Artifact:** `FAILURE_MODES.md`
**Status:** `AMOS_MODEL / SOURCE-BOUNDED / UNVALIDATED`

> **Canon boundary:** The recovered L02 source supports attention as allocation of scarce reasoning/observation resources. The detailed failure taxonomy below is a governed `AMOS_MODEL` completion unless a failure mode is explicitly traceable to source canon or a governing AMOS invariant.

---

# 0. Purpose

Define how `L02_ATTENTION` can fail, how failures are detected and typed, which state becomes invalid, how failure propagates across H/M/L dependencies, and how the system repairs attention without silently converting uncertainty into success.

The contract covers failures involving:

- admission,
- prioritization,
- allocation,
- attention budgets,
- salience,
- uncertainty,
- evidence,
- provenance,
- dependencies,
- freshness,
- scope,
- regime,
- H/M/L routing,
- agents,
- skills,
- workflows,
- authority,
- commit boundaries,
- repair,
- and validation.

The governing principle is:

```text
ATTENTION FAILURE
!=
GLOBAL SYSTEM FAILURE
```

A failure should invalidate the smallest dependency-closed region that actually depends on the failed state.

---

# 1. Source / Canon References

## 1.1 Recovered L02 primitive

Source-supported semantic core:

```text
L02_ATTENTION
=
attention allocation;
budget scarce reasoning/observation resources
```

Therefore the strongest currently source-supported failure family is:

```text
failure to allocate scarce reasoning/observation
resources consistently with the governing contract
```

The source does **not**, from currently resolved evidence, establish the complete canonical failure taxonomy in this artifact.

## 1.2 Governing AMOS constraints

Applicable governing forms include:

### Hard admission

[
Admit(x)=\bigwedge_i HardInvariant_i(x)
]

A hard invariant failure is non-compensatory.

### Confidence ceiling

[
Conf(C)\leq\min_i Conf(P_i)
]

Failure to respect a load-bearing premise confidence ceiling constitutes confidence inflation.

### Selective invalidation

[
Invalid(p)\Rightarrow Invalidate(Descendants(p))
]

Failure recovery should invalidate actual dependent descendants rather than unrelated state.

## 1.3 Related L02 artifacts

```text
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
```

---

# 2. Definition and Scope

An `L02_ATTENTION` failure is:

> A state, transition, allocation, ranking, routing, or attention proposal that violates an applicable L02 invariant, relies on invalid or insufficient load-bearing state, exceeds available attention resources, loses required provenance/scope/regime information, or crosses an authority boundary without authorization.

Formally:

[
Failure_{L02}(x,t)=
\exists I_j:
Applicable(I_j,x,t)
\land
Satisfied(I_j,x,t)=0
]

or:

[
Failure_{L02}(x,t)=UNKNOWN
]

when a load-bearing condition cannot be established.

Hard boundary:

```text
UNPROVEN_VALIDITY != VALIDITY
```

---

# 3. Failure Classes

```yaml
FailureClass:
  - INPUT_FAILURE
  - ADMISSION_FAILURE
  - PRIORITY_FAILURE
  - ALLOCATION_FAILURE
  - BUDGET_FAILURE
  - STATE_FAILURE
  - DEPENDENCY_FAILURE
  - PROVENANCE_FAILURE
  - FRESHNESS_FAILURE
  - SCOPE_FAILURE
  - REGIME_FAILURE
  - HML_FAILURE
  - EVIDENCE_FAILURE
  - CONFIDENCE_FAILURE
  - CONTROL_PLANE_FAILURE
  - AUTHORITY_FAILURE
  - AGENT_FAILURE
  - SKILL_FAILURE
  - WORKFLOW_FAILURE
  - PROTOCOL_FAILURE
  - REPAIR_FAILURE
  - VALIDATION_FAILURE
  - UNKNOWN_FAILURE
```

---

# 4. Typed Inputs

```yaml
AttentionFailureInput:

  attention_state:
    type: AttentionState

  candidates:
    type: AttentionCandidate[]

  allocation:
    type: AttentionAllocation | null

  attention_budget:
    type: AttentionBudget | UNKNOWN

  priorities:
    type: PriorityState[]

  constraints:
    type: ConstraintSet

  dependencies:
    type: DependencyGraph

  evidence:
    type: EvidenceBundle

  provenance:
    type: ProvenanceBundle

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef

  freshness:
    type: FreshnessState

  hml_coordinate:
    type: HMLCoordinate

  authority:
    type: AuthorityWitness | null

  execution_state:
    type: ExecutionState
```

---

# 5. Typed Outputs

```yaml
AttentionFailureResult:

  failure_id:
    type: FailureId

  detected:
    type:
      - TRUE
      - FALSE
      - UNKNOWN

  failure_class:
    type: FailureClass

  severity:
    type:
      - LOCAL
      - SUBSYSTEM
      - GOVERNING
      - CRITICAL
      - UNKNOWN

  affected_state:
    type: StateRef[]

  affected_dependencies:
    type: DependencyRef[]

  hml_scope:
    type: HMLCoordinate[]

  evidence:
    type: EvidenceBundle

  provenance:
    type: ProvenanceBundle

  confidence:
    type: ConfidenceBound

  repairability:
    type:
      - LOCAL_REPAIR
      - REVALIDATION
      - ROLLBACK
      - ESCALATION
      - UNRECOVERABLE
      - UNKNOWN

  proposed_repair:
    type: RepairProposal | null

  commit_authority:
    type: NONE

  falsifiers:
    type: Falsifier[]
```

Detection does not grant repair authority.

---

# 6. State Variables

```text
X_t        attention candidate set
E_t        eligible candidate set
A_t        current allocation
B_t        available attention budget
Π_t        priority state
G_t        goal state
U_t        uncertainty state
C_t        constraint/consequence state
D_t        dependency state
P_t        provenance state
F_t        freshness state
S_t        scope state
R_t        regime state
H_t        H/M/L state
Q_t        deferred attention queue
V_t        invariant-validation state
Auth_t     authority state
Repair_t   repair state
```

Failure-specific state:

```text
F_id       failure identity
F_class    failure class
F_origin   earliest known failure origin
F_extent   affected dependency closure
F_status   OPEN / CONTAINED / REPAIRED / UNKNOWN
```

---

# 7. Operators

```text
DETECT_FAILURE()
CLASSIFY_FAILURE()
LOCALIZE_FAILURE()
TRACE_DEPENDENCIES()
CHECK_BUDGET()
CHECK_ADMISSION()
CHECK_PRIORITY()
CHECK_ALLOCATION()
CHECK_PROVENANCE()
CHECK_FRESHNESS()
CHECK_SCOPE()
CHECK_REGIME()
CHECK_HML()
CHECK_CONFIDENCE()
CHECK_AUTHORITY()

QUARANTINE()
INVALIDATE()
FREEZE()
REVALIDATE()
REALLOCATE()
REPAIR()
ROLLBACK()
ESCALATE()
RETEST()
RESTORE()
```

Hard boundary:

```text
DETECT_FAILURE()
!=
AUTHORIZE_REPAIR()
```

---

# 8. Governing Invariants

```text
L02-FM-INV-001
Hard invariant failure cannot be compensated by priority.

L02-FM-INV-002
Allocated attention cannot exceed available attention.

L02-FM-INV-003
Attention allocation cannot be negative.

L02-FM-INV-004
Priority cannot be interpreted as truth.

L02-FM-INV-005
Salience cannot substitute for evidence strength.

L02-FM-INV-006
Novelty cannot substitute for validity.

L02-FM-INV-007
Uncertainty cannot automatically imply importance.

L02-FM-INV-008
Dependency cannot automatically imply causation.

L02-FM-INV-009
Confidence cannot exceed weakest load-bearing premise.

L02-FM-INV-010
Correlated provenance cannot masquerade as independent confirmation.

L02-FM-INV-011
Scope mismatch cannot silently pass.

L02-FM-INV-012
Regime mismatch cannot silently pass.

L02-FM-INV-013
Stale load-bearing state cannot silently remain authoritative.

L02-FM-INV-014
H/M/L coordinates cannot silently collapse.

L02-FM-INV-015
Failure propagation follows dependency edges.

L02-FM-INV-016
Unrelated valid state survives local failure.

L02-FM-INV-017
Repair must not destroy provenance.

L02-FM-INV-018
Repair must not weaken governing invariants.

L02-FM-INV-019
Capability cannot create authority.

L02-FM-INV-020
Attention proposal cannot become commit without separate authorization.

L02-FM-INV-021
UNKNOWN/GAP cannot be represented as PASS.

L02-FM-INV-022
Unexecuted validation cannot be represented as successful validation.
```

---

# 9. Core Failure Modes

## FM-L02-001 — Attention Budget Overflow

Condition:

[
\sum_i a_i>B_t
]

Failure:

```text
requested/allocated attention exceeds declared capacity
```

Impact:

```text
allocation invalid
dependent execution proposal invalid
```

Repair:

```text
freeze allocation
recompute available budget
reduce/reprioritize allocation
revalidate
```

---

## FM-L02-002 — Negative Allocation

Condition:

[
a_i<0
]

Classification:

`ALLOCATION_FAILURE`

Repair:

```text
reject malformed allocation
restore last valid state
recompute
```

---

## FM-L02-003 — Unknown Budget Treated as Known

Condition:

```text
B_t = UNKNOWN
```

but execution behaves as though:

```text
B_t = known finite value
```

This violates:

```text
UNKNOWN/GAP != PASS
```

Repair:

```text
resolve budget
or
operate under explicitly bounded conservative assumption
```

---

## FM-L02-004 — Hard-Constraint Compensation

Failure pattern:

```text
hard invariant = FAIL
priority = VERY_HIGH
therefore admit candidate
```

Invalid because:

[
Admit(x)=\bigwedge_i HardInvariant_i(x)
]

Repair:

```text
remove failed candidate from ordinary allocation
resolve invariant failure separately
```

---

## FM-L02-005 — Salience Capture

Condition:

```text
highly noticeable / emotionally striking / recent / repeated target
```

captures attention despite insufficient decision relevance.

Hard boundary:

```text
SALIENCE != TRUTH
SALIENCE != DECISION VALUE
```

Repair:

```text
separate salience from evidence
recalculate priority from governing variables
```

---

## FM-L02-006 — Novelty Capture

Condition:

```text
novel information receives disproportionate attention
solely because it is novel
```

Hard boundary:

```text
NOVEL != TRUE
NOVEL != IMPORTANT
```

---

## FM-L02-007 — Familiarity Capture

Opposite failure:

```text
repeated/familiar evidence is overweighted
because it feels established
```

Potential provenance failure:

```text
multiple descendants of one source
→ false appearance of confirmation
```

---

## FM-L02-008 — Threat Capture

Attention becomes dominated by perceived risk without proportional evidence, consequence, or scope validation.

Important distinction:

```text
THREAT SIGNAL
!=
VERIFIED THREAT
```

However, credible high-consequence threats may legitimately receive precautionary attention.

Therefore classification may remain `CONDITIONAL`.

---

## FM-L02-009 — Goal Drift

Current allocation no longer serves the governing objective.

Condition:

[
Goal(A_t)\not\sim Goal_{authoritative}
]

Possible causes:

```text
recent-tool-result capture
subgoal substitution
conversation drift
stale objective
agent-local optimization
```

Repair:

```text
reload authoritative objective
invalidate dependent priorities
reallocate
```

---

## FM-L02-010 — Priority Inversion

A lower-decision-value target consumes resources needed by a higher-priority load-bearing target.

Detection requires validated priority semantics; it cannot be inferred merely from disagreement.

---

## FM-L02-011 — Critical Target Starvation

A valid high-criticality target receives insufficient attention.

Possible condition:

[
Critical_i=1
\land
a_i<a_i^{minimum}
]

where the minimum is explicitly defined.

Repair:

```text
release lower-value allocation
use reserve capacity
or escalate resource insufficiency
```

---

## FM-L02-012 — Background Starvation

Persistent exclusive focus prevents necessary low-frequency monitoring.

Examples:

```text
freshness checks
regime checks
new contradictions
authority revocation
dependency invalidation
```

Repair:

```text
reserve monitoring budget
periodic revalidation
```

---

## FM-L02-013 — Attention Thrashing

Rapid repeated switching causes effective resource loss.

Pattern:

```text
A → B → C → A → D → B
```

without decision-relevant information gain.

Potential impact:

```text
context reload cost
state fragmentation
unfinished dependency chains
duplicated retrieval
```

---

## FM-L02-014 — Premature Focus Lock

The system commits attention too early to one hypothesis or branch.

Pattern:

```text
weak initial evidence
→ strong allocation
→ alternatives ignored
```

This can suppress `COMPETING`.

Repair:

```text
restore competing hypotheses
identify cheapest discriminating test
reallocate
```

---

## FM-L02-015 — Endless Exploration

Opposite failure:

```text
continuous branching
without synthesis or stopping
```

even after claim/decision/action sufficiency is achieved.

Repair:

```text
apply stopping rule
collapse equivalent branches
preserve unresolved material gaps only
```

---

# 10. Evidence and Epistemic Failures

## FM-L02-016 — Confidence Inflation

Condition:

[
Conf(C)>
\min_i Conf(P_i)
]

for load-bearing premises.

Repair:

```text
downgrade confidence
or independently revalidate weakest premise
```

---

## FM-L02-017 — Evidence/Attention Confusion

Failure:

```text
more attention given to claim
→ claim treated as better supported
```

Hard boundary:

```text
ATTENTION != EVIDENCE
```

---

## FM-L02-018 — Repetition-as-Confirmation

Repeated presentation of the same ancestral claim is interpreted as independent support.

Repair:

```text
resolve semantic/source ancestry
collapse correlated evidence
recompute confidence
```

---

## FM-L02-019 — Contradiction Suppression

A conflicting evidence item receives insufficient attention because it threatens an established conclusion.

This violates AMOS competing-hypothesis preservation.

Repair:

```text
surface contradiction
preserve COMPETING
seek discriminating evidence
```

---

## FM-L02-020 — Unknown-to-Pass Collapse

Pattern:

```text
required variable = UNKNOWN
validator finds no explicit contradiction
→ PASS
```

Invalid.

Correct state:

```text
UNKNOWN/GAP
```

---

# 11. Dependency Failures

## FM-L02-021 — Hidden Dependency

Priority/allocation relies on a premise not represented in the dependency graph.

Impact:

```text
selective invalidation becomes unsound
confidence ceiling may be wrong
repair may preserve invalid descendants
```

---

## FM-L02-022 — Dependency Overreach

Unrelated state is treated as dependent and unnecessarily invalidated.

Repair principle:

[
Invalid(p)
\Rightarrow
Invalidate(Descendants(p))
]

not:

```text
InvalidateEverything()
```

---

## FM-L02-023 — Missing Dependency Invalidation

A premise fails but downstream attention priorities remain unchanged.

Repair:

```text
compute affected closure
invalidate descendants
recompute only affected allocation
```

---

## FM-L02-024 — Dependency/Causality Collapse

Attention dependency is interpreted as causal mechanism.

Hard boundary:

```text
DEPENDENCY != CAUSATION
```

---

# 12. Provenance Failures

## FM-L02-025 — Missing Provenance

A load-bearing observation or priority signal lacks recoverable origin.

Default handling:

```text
QUARANTINE / UNKNOWN
```

not automatic trust.

---

## FM-L02-026 — Provenance Collision

Different sources are incorrectly merged as one source, or one source is represented as multiple independent sources.

---

## FM-L02-027 — Sybil Confirmation

Multiple aliases, copies, summaries, or descendants of one origin appear as independent confirmation.

---

## FM-L02-028 — Stale Provenance

Source identity remains known, but applicability has expired because the underlying state changed.

---

# 13. Scope / Regime / Temporal Failures

## FM-L02-029 — Scope Leakage

Evidence valid for one scope controls attention outside that scope.

Examples:

```text
local → global
one subsystem → entire OS
one user/context → universal
one benchmark → general capability
```

---

## FM-L02-030 — Regime Leakage

Priority evidence from regime \(R_1\) is applied in \(R_2\) without compatibility validation.

---

## FM-L02-031 — Freshness Blindness

A mutable load-bearing premise is not revalidated after its freshness envelope expires.

---

## FM-L02-032 — Temporal Priority Error

Urgency is confused with importance, or importance is confused with urgency.

Hard distinction:

```text
TIME SENSITIVITY
!=
CONSEQUENCE
```

Both may influence attention but are separate dimensions.

---

# 14. H/M/L Failure Modes

## FM-L02-033 — H-Level Capture

High-level framing consumes attention while decisive M/L evidence remains unresolved.

---

## FM-L02-034 — L-Level Tunnel Vision

Excessive detail allocation loses the governing objective or system context.

---

## FM-L02-035 — M-Level Bottleneck

Subsystem reasoning prevents necessary escalation to H or descent to L.

---

## FM-L02-036 — Scale Collapse

Evidence, confidence, variables, or constraints from H/M/L are mixed without scale identity.

Hard boundary:

```text
CROSS-SCALE SIMILARITY
!=
CROSS-SCALE VALIDITY
```

---

## FM-L02-037 — Failed Upward Escalation

A decisive L-level falsifier does not trigger reconsideration of its dependent H-level conclusion.

---

## FM-L02-038 — Invalid Downward Constraint

A speculative H-level model suppresses valid L-level observations.

Repair:

```text
restore observational independence
mark H model as MODEL
reassess dependency
```

---

# 15. Control-Plane Failures

## FM-L02-039 — Capability/Authority Collapse

Pattern:

```text
agent can allocate/route
→ agent assumed authorized to execute
```

Invalid:

```text
CAPABILITY != AUTHORITY
```

---

## FM-L02-040 — Proposal/Commit Collapse

Pattern:

```text
AttentionProposal
→ immediate durable action
```

without commit-time validation.

Invalid:

```text
PROPOSAL != COMMIT
```

---

## FM-L02-041 — Stale Authority

Authority was valid when attention was allocated but invalid at commit time.

Required:

```text
commit-time authority freshness
```

for consequential effects.

---

## FM-L02-042 — Constraint Staleness

Allocation is based on constraints that changed before execution.

---

## FM-L02-043 — Worker Self-Authorization

An L02 worker creates or broadens its own authority.

Must fail closed.

---

# 16. Agent Failure Modes

```text
FM-L02-044 Agent Goal Drift
FM-L02-045 Agent Priority Bias
FM-L02-046 Agent State Desynchronization
FM-L02-047 Agent Provenance Loss
FM-L02-048 Agent Overreach
FM-L02-049 Agent Duplicate Work
FM-L02-050 Agent Conflict Suppression
FM-L02-051 Agent Handoff Loss
FM-L02-052 Agent False Completion
```

Agents remain candidate runtime roles unless executable implementation is independently established.

---

# 17. Skill Failure Modes

```text
FM-L02-053 Wrong Skill Selection
FM-L02-054 Skill Scope Mismatch
FM-L02-055 Skill Version Staleness
FM-L02-056 Skill Output Overtrust
FM-L02-057 Skill Provenance Loss
FM-L02-058 Skill Authority Leakage
FM-L02-059 Cross-Skill Semantic Mismatch
FM-L02-060 Skill Failure Hidden as Success
```

Hard boundary:

```text
SKILL OUTPUT
!=
VALIDATED RESULT
```

---

# 18. Workflow Failure Modes

```text
FM-L02-061 Admission Check Skipped
FM-L02-062 Budget Check Skipped
FM-L02-063 Dependency Check Skipped
FM-L02-064 Provenance Check Skipped
FM-L02-065 Scope/Regime Check Skipped
FM-L02-066 Premature Branching
FM-L02-067 Premature Synthesis
FM-L02-068 Missing Adversarial Check
FM-L02-069 Missing Stopping Condition
FM-L02-070 Failed Repair Repeated Without New Evidence
```

---

# 19. Protocol Failure Modes

```text
FM-L02-071 Missing Required Field
FM-L02-072 Invalid Type
FM-L02-073 Invalid Enum
FM-L02-074 Missing Provenance Bundle
FM-L02-075 Missing Scope Envelope
FM-L02-076 Missing Regime
FM-L02-077 Missing Freshness
FM-L02-078 Missing Dependency References
FM-L02-079 Missing Falsifiers
FM-L02-080 Missing Confidence Ceiling
FM-L02-081 Proposal Mislabelled Commit
FM-L02-082 UNKNOWN Mislabelled PASS
```

---

# 20. Failure Severity

Suggested model:

```yaml
FailureSeverity:

  LOCAL:
    meaning:
      one candidate/operator/local state affected

  SUBSYSTEM:
    meaning:
      multiple related allocations or M-level subsystem affected

  GOVERNING:
    meaning:
      H-level objective, constraint, provenance, authority,
      or shared dependency affected

  CRITICAL:
    meaning:
      integrity boundary violated or safe continuation impossible

  UNKNOWN:
    meaning:
      severity cannot yet be bounded
```

Severity is not equivalent to confidence.

---

# 21. Failure Propagation

Define failed premise (p).

Affected closure:

[
Affected(p)={x:p\leadsto x}
]

Then:

[
Invalid(p)
\Rightarrow
Invalidate(Affected(p))
]

while:

[
y\notin Affected(p)
\Rightarrow
Preserve(y)
]

unless another independent failure applies.

This is an `AMOS_MODEL` application of selective invalidation.

---

# 22. Failure Containment

Containment protocol:

```text
DETECT
↓
TYPE
↓
LOCALIZE
↓
FREEZE affected state
↓
PRESERVE unaffected state
↓
TRACE dependencies
↓
QUARANTINE uncertain inputs
↓
SELECT smallest sufficient repair
```

Containment does not mean resolution.

---

# 23. Repair / Recovery

General repair state machine:

```text
OPEN
↓
CONTAINED
↓
DIAGNOSED
↓
REPAIR_PROPOSED
↓
VALIDATED
↓
REPAIRED
```

Alternative paths:

```text
DIAGNOSED
→ REVALIDATION_REQUIRED

DIAGNOSED
→ ROLLBACK_REQUIRED

DIAGNOSED
→ ESCALATION_REQUIRED

DIAGNOSED
→ UNKNOWN/GAP
```

Repair must not automatically retry the same failed path.

Hard rule:

```text
RETRY requires changed evidence,
changed state,
changed assumptions,
or changed method.
```

---

# 24. Repair Classes

```yaml
RepairClass:

  LOCAL_REPAIR:
    use_when:
      failure isolated and dependencies bounded

  REALLOCATION:
    use_when:
      allocation invalid but underlying state remains valid

  REVALIDATION:
    use_when:
      freshness/provenance/scope/regime uncertainty is decisive

  SELECTIVE_INVALIDATION:
    use_when:
      premise failure has known descendants

  ROLLBACK:
    use_when:
      current state cannot be safely repaired in place

  ESCALATION:
    use_when:
      authority, safety, critical uncertainty, or unresolved contradiction prevents local resolution

  TERMINATION:
    use_when:
      no valid repair path exists within declared authority/resources
```

---

# 25. Recovery Invariants

```text
L02-REC-001
Repair preserves unaffected valid state.

L02-REC-002
Repair preserves provenance lineage.

L02-REC-003
Repair cannot weaken hard invariants.

L02-REC-004
Repair cannot silently expand scope.

L02-REC-005
Repair cannot silently change regime.

L02-REC-006
Repair cannot self-grant authority.

L02-REC-007
Repair must revalidate affected descendants.

L02-REC-008
Failed repair must remain visible.

L02-REC-009
Rollback target must be a previously valid state.

L02-REC-010
UNKNOWN recovery status cannot be marked successful.
```

---

# 26. Tests / Validators

Required validators:

```text
VALIDATE_FAILURE_SCHEMA
VALIDATE_FAILURE_CLASS
VALIDATE_FAILURE_LOCALIZATION
VALIDATE_BUDGET
VALIDATE_NONNEGATIVITY
VALIDATE_HARD_ADMISSION
VALIDATE_PRIORITY_SEPARATION
VALIDATE_CONFIDENCE_CEILING
VALIDATE_PROVENANCE
VALIDATE_PROVENANCE_INDEPENDENCE
VALIDATE_DEPENDENCY_CLOSURE
VALIDATE_SELECTIVE_INVALIDATION
VALIDATE_SCOPE
VALIDATE_REGIME
VALIDATE_FRESHNESS
VALIDATE_HML
VALIDATE_AUTHORITY
VALIDATE_PROPOSAL_COMMIT_BOUNDARY
VALIDATE_REPAIR
VALIDATE_ROLLBACK
VALIDATE_UNAFFECTED_STATE_PRESERVATION
```

---

# 27. Minimum Failure Tests

```text
TEST-L02-FM-001
Budget overflow must be detected.

TEST-L02-FM-002
Negative allocation must fail.

TEST-L02-FM-003
Unknown budget cannot produce validated allocation.

TEST-L02-FM-004
Hard invariant failure cannot be overridden by priority.

TEST-L02-FM-005
Salience alone cannot establish truth.

TEST-L02-FM-006
Novelty alone cannot establish validity.

TEST-L02-FM-007
Correlated sources cannot count as independent confirmation.

TEST-L02-FM-008
Contradictory evidence cannot silently disappear.

TEST-L02-FM-009
Weak load-bearing premise caps conclusion confidence.

TEST-L02-FM-010
Invalid premise invalidates dependent attention state.

TEST-L02-FM-011
Independent state survives local invalidation.

TEST-L02-FM-012
Scope mismatch is detected.

TEST-L02-FM-013
Regime mismatch is detected.

TEST-L02-FM-014
Expired freshness triggers revalidation.

TEST-L02-FM-015
H/M/L scale identity survives routing.

TEST-L02-FM-016
L-level falsifier can trigger dependent H-level reassessment.

TEST-L02-FM-017
Agent capability does not grant authority.

TEST-L02-FM-018
Proposal cannot become commit automatically.

TEST-L02-FM-019
Failed repair remains visible.

TEST-L02-FM-020
Retrying unchanged failed path is rejected or flagged.

TEST-L02-FM-021
UNKNOWN/GAP cannot return PASS.

TEST-L02-FM-022
Unexecuted failure test cannot be reported as passed.
```

---

# 28. Falsifiers

Revise this failure contract if direct canon establishes that:

```text
L02 has materially different failure semantics

L02 attention is not resource constrained

specific listed failure modes belong to another primitive

canonical L02 permits behaviors classified here as invariant violations

canonical control-plane ownership differs from this model

H/M/L does not apply to L02

canonical repair semantics contradict selective invalidation

runtime implementation demonstrates a different validated failure model
```

Individual failure hypotheses are falsified when their triggering conditions are shown not to produce the claimed contract violation under the applicable scope/regime.

---

# 29. Competing Failure Explanations

When attention behavior appears wrong, preserve at least these competing classes until evidence discriminates them:

```text
COMPETING-001
attention allocation itself is wrong

COMPETING-002
input observation from L01 is wrong

COMPETING-003
goal/objective state is wrong or stale

COMPETING-004
dependency graph is incomplete

COMPETING-005
provenance is correlated or invalid

COMPETING-006
scope/regime changed

COMPETING-007
budget estimate is wrong

COMPETING-008
worker behavior is valid but control-plane rejection is correct

COMPETING-009
apparent failure is actually valid prioritization under a hidden constraint

COMPETING-010
measurement/validator is wrong
```

Do not force convergence without discriminating evidence.

---

# 30. Cheapest Discriminating Tests

For apparent L02 failure, preferred diagnostic order:

```text
1. Check hard invariant violation.
2. Check authoritative objective.
3. Check available attention budget.
4. Check input validity from L01.
5. Check dependency closure.
6. Check provenance ancestry.
7. Check scope/regime/freshness.
8. Check H/M/L routing.
9. Check authority/commit boundary.
10. Only then expand to broader architectural failure.
```

This order is a model diagnostic policy, not canonical source law.

---

# 31. Control-Plane Requirements

The control plane should be able to distinguish:

```text
worker failure
input failure
model failure
constraint failure
authority failure
freshness failure
provenance failure
commit failure
unknown failure
```

For consequential attention-controlled effects it should support:

```text
typed state validation
dependency validation
freshness checking
authority checking
constraint checking
provenance checking
selective invalidation
rollback
commit-time revalidation
```

L02 should not own durable finalization authority merely because it detected or repaired an attention failure.

---

# 32. Agents

Candidate logical roles:

```text
L02_FAILURE_DETECTOR
L02_FAILURE_LOCALIZER
L02_DEPENDENCY_TRACER
L02_PROVENANCE_AUDITOR
L02_HML_FAILURE_ROUTER
L02_REPAIR_PROPOSER
L02_REVALIDATION_AGENT
L02_FAILURE_VALIDATOR
```

Status:

```text
MODEL ROLES
```

not proven runtime deployments.

---

# 33. Skills

Relevant capability mappings include:

```text
AMOS Attention Allocation Governor
AMOS Constraint Propagation RSCF Engine
AMOS Context Budget Governor RSCF
AMOS Provenance Trust Firewall
AMOS Metacognitive Confidence Auditor
AMOS Repair Harm Auditor
AMOS Target of Repair Intelligence
AMOS Infrastructure Control Plane
AMOS RSCF Modeler
```

Skill availability does not establish canonical L02 dependency.

---

# 34. Failure Workflow

```text
ATTENTION EVENT
↓
DETECT anomaly/invariant failure
↓
CLASSIFY failure
↓
ESTABLISH evidence
↓
LOCALIZE earliest supported failure
↓
IDENTIFY affected dependency closure
↓
PRESERVE competing explanations
↓
FREEZE affected state
↓
SELECT cheapest discriminating test
↓
REPAIR / REVALIDATE / ROLLBACK / ESCALATE
↓
RETEST
↓
RESTORE only if validation succeeds
```

---

# 35. Failure Protocol

```yaml
AttentionFailureCapsule:

  failure_id: null

  primitive:
    value: L02_ATTENTION

  failure_class: null

  claim_class:
    type:
      - VERIFIED
      - DERIVED
      - MODEL
      - CONDITIONAL
      - COMPETING
      - UNKNOWN/GAP

  trigger: null

  violated_invariants: []

  affected_state: []

  affected_dependencies: []

  hml_scope: []

  evidence: []

  provenance: []

  scope: null

  regime: null

  freshness: null

  competing: []

  falsifiers: []

  repair_proposal: null

  repair_authority: null

  validation_status:
    value: UNKNOWN

  confidence_ceiling: 0
```

---

# 36. Evidence / Provenance Requirements

Every consequential failure determination should retain:

```text
failure ID
observation triggering detection
source identity
source ancestry
timestamp
state version
scope
regime
H/M/L coordinate
applicable invariant
failed condition
dependency edges
validator identity
repair lineage
test result
confidence
falsifiers
```

A generated description of a failure is not itself evidence that the failure occurred.

---

# 37. Uncertainty Vector

Recommended uncertainty dimensions:

```yaml
uncertainty:

  evidence:
    question:
      is the alleged failure directly observed?

  model:
    question:
      does the failure taxonomy correctly explain the observation?

  scope:
    question:
      is the rule applicable here?

  temporal:
    question:
      is relevant state still fresh?

  causal:
    question:
      is L02 actually causal or merely where failure became visible?

  execution:
    question:
      has the failure/repair been tested?

  provenance_independence:
    question:
      are supporting observations genuinely independent?
```

Important:

```text
OBSERVED AT L02
!=
CAUSED BY L02
```

---

# 38. Confidence Ceiling

Current confidence is bounded because:

```text
direct canonical L02 failure taxonomy is unresolved

canonical runtime mapping is unresolved

failure tests are not established here as executed

some failure modes are architectural extrapolations
```

Therefore:

```text
source-supported:
attention is an allocation problem over scarce reasoning/observation resources

framework-supported:
hard failures are non-compensatory
confidence is premise-bounded
invalidation is dependency-selective

model-supported:
the detailed L02 failure taxonomy and repair mapping

runtime-validated:
UNKNOWN/GAP
```

---

# 39. Gap Matrix

```yaml
gap_matrix:

  l02_attention_allocation_basis:
    status: SOURCE_SUPPORTED

  scarce_attention_resource_basis:
    status: SOURCE_SUPPORTED

  hard_failure_noncompensation:
    status: SOURCE_FRAMEWORK_SUPPORTED

  confidence_ceiling:
    status: SOURCE_FRAMEWORK_SUPPORTED

  selective_invalidation:
    status: SOURCE_FRAMEWORK_SUPPORTED

  canonical_l02_failure_taxonomy:
    status: GAP
    criticality: CRITICAL

  canonical_failure_ids:
    status: GAP
    criticality: EXPLANATORY

  canonical_failure_severity:
    status: GAP
    criticality: DECISION_RELEVANT

  canonical_failure_state_machine:
    status: GAP
    criticality: DECISION_RELEVANT

  canonical_repair_mapping:
    status: GAP
    criticality: CRITICAL

  canonical_agent_failure_roles:
    status: GAP
    criticality: EXPLANATORY

  canonical_skill_failure_dependencies:
    status: GAP
    criticality: EXPLANATORY

  control_plane_runtime_mapping:
    status: GAP
    criticality: CRITICAL

  executable_failure_detection:
    status: GAP
    criticality: CRITICAL

  executed_failure_tests:
    status: GAP
    criticality: CRITICAL
```

---

# 40. RSCF Completion State

```yaml
rscf:

  id: L02_ATTENTION_FAILURE_MODES

  claim:
    L02_ATTENTION failures can be modeled as violations or unresolved
    states affecting governed allocation of scarce reasoning/observation
    resources, with failures localized and propagated according to
    actual dependencies rather than assumed globally.

  claim_class: MODEL

  source_supported_core:
    - L02 concerns attention allocation
    - attention budgets scarce reasoning/observation resources

  source_framework_support:
    - hard invariant failures are non-compensatory
    - conclusion confidence is bounded by load-bearing premises
    - invalidation propagates through dependent descendants

  evidence:
    - recovered L02 primitive definition
    - AMOS Attention Allocation Governor contract
    - AMOS governance lineage

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    subsystem: COGNITIVE_MATRIX
    primitive: L02_ATTENTION
    artifact: FAILURE_MODES.md
    derivation: SOURCE_BOUNDED_MODEL_COMPLETION

  scope:
    system: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    primitive: L02_ATTENTION
    concern: attention_failure_detection_and_recovery

  regime:
    governed finite-resource cognitive allocation

  freshness:
    revalidate_when:
      - direct L02 failure canon is recovered
      - L02 invariants change
      - canonical attention equations change
      - control-plane semantics change
      - executable runtime evidence becomes available

  dependencies:
    - L01_SENSING_OBSERVATION
    - L02_ATTENTION_DEFINITION
    - L02_ATTENTION_VARIABLES
    - L02_ATTENTION_STATE
    - L02_ATTENTION_OPERATORS
    - L02_ATTENTION_INVARIANTS
    - L02_ATTENTION_DEPENDENCIES
    - L02_ATTENTION_EQUATIONS
    - L02_ATTENTION_HML
    - L02_ATTENTION_CONTROL_PLANES
    - L02_ATTENTION_PROVENANCE
    - L02_ATTENTION_REPAIR
    - L02_ATTENTION_TESTS

  competing:
    - true L02 allocation failure
    - upstream L01 observation failure
    - stale or incorrect objective
    - hidden dependency
    - provenance failure
    - scope/regime shift
    - budget estimation failure
    - control-plane rejection
    - validator/measurement failure

  falsifiers:
    - direct canon contradicts modeled failure classes
    - canonical runtime assigns failures differently
    - tests falsify proposed invariants
    - apparent L02 failures are demonstrated to originate elsewhere

  uncertainty:
    evidence: MEDIUM_HIGH
    model: MEDIUM
    scope: MEDIUM_HIGH
    temporal: MEDIUM
    causal: MEDIUM_HIGH
    execution: HIGH
    provenance_independence: MEDIUM

  confidence_ceiling:
    framework-level failure principles may be reused within their
    declared AMOS scope; detailed L02 failure modes remain MODEL
    until direct canon or executable evidence validates them

  gap_status:
    canonical_failure_taxonomy: CRITICAL_GAP
    canonical_repair_mapping: CRITICAL_GAP
    runtime_mapping: CRITICAL_GAP
    executed_validation: CRITICAL_GAP

  cheapest_discriminating_test:
    recover direct canonical L02 failure-mode definitions and compare
    them against this taxonomy and the L02 invariant registry
```

---

# 41. Completion State

```yaml
completion_state:

  source_canon_references:
    status: PARTIAL / GAP_VISIBLE

  definition_scope:
    status: MODEL_COMPLETE

  typed_inputs_outputs:
    status: MODEL_COMPLETE

  state_variables:
    status: MODEL_COMPLETE

  operators:
    status: MODEL_COMPLETE

  invariants:
    status: MODEL_COMPLETE

  dependencies:
    status: MODEL_COMPLETE

  HML_applicability:
    status: MODEL_COMPLETE

  control_plane_requirements:
    status: MODEL_COMPLETE

  agents:
    status: MODEL_COMPLETE

  skills:
    status: MODEL_COMPLETE

  workflows:
    status: MODEL_COMPLETE

  protocols:
    status: MODEL_COMPLETE

  evidence_provenance:
    status: MODEL_COMPLETE

  uncertainty_confidence:
    status: MODEL_COMPLETE

  failure_modes:
    status: MODEL_COMPLETE

  repair_recovery:
    status: MODEL_COMPLETE

  tests_validators:
    status: MODEL_COMPLETE / UNEXECUTED

  falsifiers:
    status: MODEL_COMPLETE

  canonical_failure_taxonomy:
    status: UNKNOWN/GAP

  runtime_mapping:
    status: UNKNOWN/GAP

  executed_validation:
    status: UNKNOWN/GAP

  overall:
    status: COMPLETE_FOR_DECLARED_MODEL_SCOPE

  conclusion_class:
    MODEL / CONDITIONAL
```

---

# 42. Hard Boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

Failure-specific boundaries:

```text
ANOMALY != FAILURE

FAILURE OBSERVED AT L02 != FAILURE CAUSED BY L02

SALIENCE != TRUTH

NOVELTY != VALIDITY

REPETITION != INDEPENDENT CONFIRMATION

UNCERTAINTY != IMPORTANCE

URGENCY != CONSEQUENCE

DEPENDENCY != CAUSATION

PRIORITY != AUTHORITY

ATTENTION != EVIDENCE

LOCAL FAILURE != GLOBAL FAILURE

CONTAINED != REPAIRED

REPAIRED != VALIDATED

RETRY != REPAIR

MODEL FAILURE TAXONOMY != SOURCE CANON

TEST DEFINED != TEST EXECUTED

NO DETECTED FAILURE != VERIFIED CORRECTNESS
```

---

# 43. References

```text
PLACEHOLDER

L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README

L01_SENSING_OBSERVATION

Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
AMOS Repair Harm Auditor
AMOS Target of Repair Intelligence
Cosmo_Brain_BRIDGE_INDEX
AMOS RSCF
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
```

---

# 44. Governing Failure Contract

> **L02_ATTENTION fails when scarce reasoning/observation resources are allocated, prioritized, propagated, or acted upon in violation of applicable hard invariants, valid dependency structure, evidence/provenance requirements, scope/regime/freshness boundaries, H/M/L identity, or authority constraints. Failure detection must preserve uncertainty and competing explanations; recovery must invalidate only affected descendants, preserve unaffected valid state, and remain a proposal until separately authorized where durable effects are involved.**

---

# 45. Canon Boundary

```text
SOURCE-SUPPORTED:
L02 concerns attention allocation over scarce
reasoning/observation resources.

SOURCE-FRAMEWORK-SUPPORTED:
hard invariant failures are non-compensatory

Conf(C) <= min_i Conf(P_i)

Invalid(p) => Invalidate(Descendants(p))

AMOS_MODEL:
detailed failure taxonomy
failure severity classes
salience/novelty/threat capture classes
attention starvation/thrashing
H/M/L failure taxonomy
agent/skill/workflow/protocol failures
failure containment
repair state machine
failure-test registry

UNKNOWN/GAP:
canonical L02 failure-mode registry
canonical failure IDs
canonical severity rules
canonical repair mapping
canonical runtime detection logic
executed failure tests
runtime validation
```

Therefore:

```text
CONCLUSION CLASS:
MODEL / CONDITIONAL

NOT:
VERIFIED L02 FAILURE CANON

NOT:
IMPLEMENTED FAILURE DETECTOR

NOT:
EXECUTED VALIDATION
```

```text
```

---

[[00_ROOT_MOC]]|[[AMOS MOC]]

---
**Related:** [[00_HOME]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: l02_attention_primitives_cognitive_matrix_failure_modes
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L02_ATTENTION/L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_FAILURE_MODES.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[L02_ATTENTION_MOC]]

