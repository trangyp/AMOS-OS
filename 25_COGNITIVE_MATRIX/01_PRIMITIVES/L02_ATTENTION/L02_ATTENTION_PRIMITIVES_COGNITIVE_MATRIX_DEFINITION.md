---
tags: ['cognitive_matrix', 'primitives', 'l02_attention', 'note']
---

Below is the **full replacement content** for `L02_ATTENTION/DEFINITION.md`, written to stay source-bounded and to distinguish recovered primitive meaning from AMOS model completion.

---
tags:
  - amos
  - cognitive-matrix
  - l02
  - attention
  - definition
  - rscf
  - hml
  - provenance

title: "L02_ATTENTION — Definition"
origin_architect: "Trang Phan"
status: "MODEL_SPECIFICATION / UNVALIDATED"
epistemic_class: "MODEL"
runtime_alignment: "AMOS Full Brain OS / AMOS_CORE v4.4 lineage"
---

# L02_ATTENTION — Definition

**Class:** `COGNITIVE_PRIMITIVE_DEFINITION_CONTRACT`  
**Origin architect / steward:** Trang Phan  
**Primitive:** `L02_ATTENTION`  
**Artifact:** `DEFINITION.md`  
**Status:** `AMOS_MODEL / SOURCE-BOUNDED / UNVALIDATED`

> **Integrity boundary:** available L02 material supports attention as an allocation function over scarce reasoning/observation resources. The detailed typed architecture below completes the contract as an AMOS model. It must not be represented as recovered canonical implementation unless direct source material establishes that status.

---

# 0. Purpose

`L02_ATTENTION` defines the cognitive primitive responsible for selectively allocating finite cognitive processing resources among competing candidate targets.

Its primitive role can be summarized as:

```text
AVAILABLE INFORMATION / TARGETS
↓
ATTENTION ELIGIBILITY
↓
PRIORITY ASSESSMENT
↓
RESOURCE ALLOCATION PROPOSAL
↓
GOVERNED ATTENTION STATE
↓
DEEPER COGNITIVE PROCESSING
```

The primitive answers:

> **Given more potentially processable information than can be processed with equal depth, what should receive cognitive resources now, at what scale, and under what constraints?**

It does **not** answer:

```text
What is true?
What caused an event?
What action is authorized?
What should permanently enter memory?
What external effect should be committed?
```

Those require other AMOS functions and/or control-plane validation.

---

# 1. Source / Canon References

## 1.1 Source-supported primitive role

Recovered L02 material supports the primitive concept:

```text
Primitive: attention allocation;
budget scarce reasoning/observation resources.
```

Therefore the minimum source-supported definition is:

> `L02_ATTENTION` is the AMOS cognitive primitive concerned with allocation of scarce reasoning and observation resources.

## 1.2 Source limitations

The currently available placeholder does **not** independently establish:

```text
canonical attention equations
canonical variable names
canonical state schema
canonical scoring function
canonical allocation algorithm
canonical agent architecture
canonical control-plane owner
canonical protocol vocabulary
canonical runtime implementation
canonical numerical thresholds
```

These remain `UNKNOWN/GAP` unless independently recovered.

## 1.3 Relevant AMOS architectural references

The model completion is aligned with:

```text
AMOS Attention Allocation Governor
AMOS Context Budget Governor
AMOS Constraint Propagation
AMOS Infrastructure Control Plane
AMOS Deterministic AI Control Plane
AMOS RSCF
AMOS H/M/L decomposition
AMOS provenance architecture
AMOS scope/regime firewalls
AMOS uncertainty/confidence ceilings
```

These references provide architectural constraints but do not automatically make every definition below source canon.

## 1.4 Epistemic classification

```yaml
source_status:

  attention_as_primitive:
    status: SOURCE_SUPPORTED

  allocation_function:
    status: SOURCE_SUPPORTED

  scarce_reasoning_resources:
    status: SOURCE_SUPPORTED

  scarce_observation_resources:
    status: SOURCE_SUPPORTED

  detailed_attention_contract:
    status: MODEL

  typed_state:
    status: MODEL

  exact_equations:
    status: UNKNOWN/GAP

  exact_runtime:
    status: UNKNOWN/GAP

  empirical_cognitive_claims:
    status: NOT_ESTABLISHED
```

---

# 2. Core Definition

`L02_ATTENTION` is the AMOS cognitive resource-selection layer that transforms a set of currently addressable cognitive targets into a bounded attention-allocation proposal subject to objectives, constraints, uncertainty, dependency structure, H/M/L scale, provenance, risk, and available cognitive budget.

Formally, as an AMOS model:

[
L02:
(X,G,B,C,U,P,HML)
\rightarrow
A
]

where:

```text
X    = candidate attention targets
G    = active objective / goal state
B    = available attention budget
C    = applicable constraints
U    = uncertainty state
P    = provenance state
HML  = active scale context
A    = proposed attention allocation
```

This equation is an `AMOS_MODEL` representation, not a recovered empirical law.

---

# 3. Attention as Selection Under Scarcity

If cognitive processing were unlimited, attention allocation would not require the same scarcity-governance function.

The L02 problem exists because:

```text
candidate processing demand
>
available processing capacity
```

at least in some operating states.

Candidate resource relation:

[
Demand_t > Capacity_t
\Rightarrow
SelectionRequired_t
]

The purpose of L02 is therefore not merely to identify salient information.

It must govern **selective processing under finite resources**.

---

# 4. Attention Is Not Salience

Salience is one possible input to attention.

It is not identical to attention.

```text
SALIENCE
=
how strongly something stands out

ATTENTION
=
how cognitive resources are allocated
```

Therefore:

```text
HIGH SALIENCE != HIGH ATTENTION NECESSARILY
```

A highly salient event may be irrelevant to the governing objective.

A low-salience dependency may be critical to a decision.

Candidate relationship:

[
AttentionPriority(x)
====================

f(
GoalRelevance,
DependencyCriticality,
Risk,
Uncertainty,
Novelty,
TimeSensitivity,
Salience,
Cost
)
]

The exact canonical function is `UNKNOWN/GAP`.

---

# 5. Attention Is Not Truth

Attention changes processing allocation.

It does not establish epistemic validity.

```text
ATTENDED != TRUE

UNATTENDED != FALSE

HIGH ATTENTION != HIGH CONFIDENCE

REPEATED ATTENTION != INDEPENDENT EVIDENCE
```

A false claim may deserve substantial attention because it is dangerous.

A verified fact may require little additional attention because it is already stable.

---

# 6. Attention Is Not Importance

Importance and attention should remain distinct.

```text
IMPORTANCE
=
potential consequence or value

ATTENTION
=
allocated cognitive processing
```

A highly important item may temporarily receive low attention because:

```text
required evidence is unavailable
another dependency must be resolved first
a higher-risk issue has immediate temporal priority
processing it now has low information value
```

Conversely, a small technical detail may receive high attention if it is a load-bearing dependency.

---

# 7. Attention Is Not Authority

Attention determines or proposes where cognition should focus.

It does not grant permission to act.

```text
ATTENTION != AUTHORITY

PRIORITY != AUTHORITY

SALIENCE != AUTHORITY

CAPABILITY != AUTHORITY
```

A target may receive maximum attention while still being prohibited from producing an external effect.

---

# 8. Attention Is Not Commit

L02 may produce:

```text
candidate ranking
attention recommendation
allocation proposal
routing proposal
escalation proposal
```

These are not equivalent to authoritative state change.

```text
PROPOSAL != COMMIT
```

Where attention state is governed by a higher control plane:

```text
L02 PROPOSAL
↓
CONTROL-PLANE VALIDATION
↓
COMMITTABLE
↓
COMMIT
```

The exact canonical ownership of attention-state commit remains `UNKNOWN/GAP`.

---

# 9. Scope

L02 applies to allocation among cognitive targets such as:

```text
observations
claims
questions
uncertainties
contradictions
dependencies
risks
hypotheses
goals
subtasks
evidence
memory candidates
tool results
repair targets
decision variables
```

L02 may govern allocation across:

```text
reasoning depth
observation depth
retrieval depth
validation effort
comparison effort
counterexample search
uncertainty reduction
repair analysis
cross-scale analysis
```

---

# 10. Out of Scope

L02 does not independently own:

```text
raw sensing
truth determination
causal proof
long-term memory admission
final action authorization
external effect execution
canonical knowledge promotion
identity governance
ethical authority
system-wide commit finality
```

It may interact with these functions but must not silently absorb them.

---

# 11. Typed Inputs

```yaml
AttentionInput:

  candidates:
    type: AttentionCandidate[]

  active_objective:
    type: GoalRef | UNKNOWN

  observation_context:
    type: ObservationContext

  current_attention_state:
    type: AttentionState

  available_budget:
    type: AttentionBudget

  constraints:
    type: ConstraintContext

  uncertainty:
    type: UncertaintyVector

  provenance:
    type: ProvenanceBundle

  dependencies:
    type: DependencyGraph

  competing_hypotheses:
    type: HypothesisSet

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef

  hml:
    type: HMLContext

  temporal_context:
    type: TemporalContext

  authority_context:
    type: AuthorityContext | UNKNOWN
```

Exact canonical field names remain unresolved.

---

# 12. Attention Candidate

Candidate model:

```yaml
AttentionCandidate:

  id:
    type: CandidateId

  target:
    type: CognitiveTargetRef

  target_type:
    type:
      - OBSERVATION
      - CLAIM
      - QUESTION
      - EVIDENCE
      - HYPOTHESIS
      - CONTRADICTION
      - DEPENDENCY
      - RISK
      - TASK
      - MEMORY_CANDIDATE
      - TOOL_RESULT
      - REPAIR_TARGET
      - OTHER

  goal_relevance:
    type: Score | UNKNOWN

  salience:
    type: Score | UNKNOWN

  novelty:
    type: Score | UNKNOWN

  uncertainty:
    type: Score | UNKNOWN

  dependency_criticality:
    type: Score | UNKNOWN

  consequence:
    type: Score | UNKNOWN

  time_sensitivity:
    type: Score | UNKNOWN

  expected_information_gain:
    type: Score | UNKNOWN

  processing_cost:
    type: ResourceEstimate | UNKNOWN

  provenance:
    type: ProvenanceBundle

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef

  hml:
    type: HMLContext
```

---

# 13. Typed Outputs

```yaml
AttentionOutput:

  allocation_proposal:
    type: AttentionAllocation[]

  deferred_targets:
    type: AttentionCandidate[]

  blocked_targets:
    type: AttentionCandidate[]

  quarantined_targets:
    type: AttentionCandidate[]

  escalation_targets:
    type: AttentionCandidate[]

  unresolved_conflicts:
    type: ConflictSet

  budget_state:
    type: AttentionBudgetState

  provenance:
    type: ProvenanceBundle

  uncertainty:
    type: UncertaintyVector

  confidence_ceiling:
    type: ConfidenceBound

  status:
    type:
      - PROPOSED
      - PARTIAL
      - BLOCKED
      - REVALIDATE
      - UNKNOWN_GAP
```

---

# 14. State Variables

Candidate L02 state:

```text
X_t       = candidate target set at time t

A_t       = current attention allocation

B_t       = total attention budget

B_avail   = currently available budget

B_used    = allocated/consumed budget

B_reserve = protected attention reserve

G_t       = active goal/objective

C_t       = active constraints

U_t       = uncertainty vector

D_t       = dependency state

P_t       = provenance state

R_t       = active regime

S_t       = active scope

HML_t     = scale context

Q_t       = quarantined targets

F_t       = deferred targets
```

These are model variables.

---

# 15. Attention Budget

Candidate contract:

[
B_{used} + B_{reserve} \le B_{total}
]

and:

[
B_{available}
=============

## B_{total}

## B_{used}

B_{reserve}
]

Hard rule:

```text
DO NOT ALLOCATE RESOURCES THAT DO NOT EXIST
```

The precise meaning of resource units may vary by runtime:

```text
tokens
time
tool calls
retrieval operations
validation cycles
agent calls
working-memory capacity
human-review capacity
```

No universal equivalence between these units is assumed.

---

# 16. Candidate Attention Priority

A non-canonical model representation is:

[
Priority(x)
===========

f(
G_x,
D_x,
K_x,
U_x,
T_x,
N_x,
S_x,
I_x,
Cost_x
)
]

where:

```text
G = goal relevance
D = dependency criticality
K = consequence / risk
U = uncertainty
T = time sensitivity
N = novelty
S = salience
I = expected information value
Cost = expected resource cost
```

This is intentionally abstract.

No exact weighting is claimed.

---

# 17. Hard-Invariant Admission

Attention allocation must not be governed by score alone.

For candidate (x):

[
Admit(x)
========

\bigwedge_i HardInvariant_i(x)
]

Only after hard admission may optimization occur.

Therefore:

```text
VERY HIGH PRIORITY
+
HARD INVARIANT FAILURE
=
DO NOT ADMIT
```

This prevents weighted optimization from compensating for prohibited conditions.

---

# 18. Objective Relevance

Attention should normally remain bound to the governing objective.

Candidate relation:

[
Rel(x,G)
========

Relevance(x \mid G)
]

But objective relevance is not the only factor.

A target with low direct relevance may still deserve attention when it is:

```text
a safety constraint
a critical dependency
a falsifier
a contradiction
a governance condition
a hidden failure source
```

---

# 19. Dependency Criticality

A low-level detail may become attention-critical when many downstream conclusions depend on it.

Candidate:

[
Criticality(x)
\propto
Impact(Descendants(x))
]

This is not necessarily equivalent to graph degree.

The important property is **decision-changing dependency impact**.

---

# 20. Uncertainty Allocation

Attention should increase where uncertainty reduction has positive expected decision value.

Conceptually:

[
Attention(x)
\uparrow
\quad
\text{when}
\quad
EV(\Delta U_x) > Cost(x)
]

where:

```text
EV(ΔU)
=
expected decision value from reducing uncertainty
```

This is an AMOS decision heuristic, not a canonical numerical law.

---

# 21. Attention and Falsification

Attention should not only reinforce the leading hypothesis.

It should reserve capacity for:

```text
contradiction search
falsifier search
competing hypotheses
provenance correlation checks
scope mismatch checks
regime-shift checks
```

Especially for consequential claims:

```text
BUILD STRONGEST SUPPORTED CONCLUSION
↓
ALLOCATE ATTENTION TO BREAK IT
```

---

# 22. Attention and Provenance

Evidence repetition should not automatically receive additional epistemic weight.

If multiple items share ancestry:

```text
SOURCE A
├── summary B
├── summary C
└── paraphrase D
```

then:

```text
B + C + D
!=
three independent confirmations
```

Attention may still be distributed across them for comparison, but provenance independence must remain explicit.

---

# 23. Attention and Scope

Every target should inherit or carry an applicability envelope where relevant.

```yaml
scope_envelope:

  system: optional
  population: optional
  environment: optional
  scale: optional
  measurement_method: optional
  assumptions: optional
```

Attention to evidence in one scope does not automatically justify transferring conclusions outside that scope.

---

# 24. Attention and Regime

Attention allocation should respond to regime change.

Examples:

```text
normal → crisis
stable → volatile
offline → live
research → production
reversible → irreversible
low-stakes → consequential
```

Candidate rule:

```text
REGIME CHANGE
→
REASSESS ATTENTION PRIORITIES
```

because previously low-priority constraints may become load-bearing.

---

# 25. Temporal Attention

L02 must distinguish:

```text
urgent
important
persistent
stale
future-critical
temporarily blocked
```

Urgency and importance are not identical.

Candidate dimensions:

```text
time_to_consequence
freshness
deadline
recoverability_window
dependency_order
future_option_loss
```

---

# 26. H/M/L Applicability

L02 operates recursively across H/M/L.

## H — Governing attention

Questions:

```text
What domain deserves resources?
What objective dominates?
What major risk could invalidate the entire task?
What cross-system dependency is load-bearing?
```

Examples:

```text
research vs execution
safety vs optimization
architecture vs implementation
diagnosis vs repair
```

## M — Subsystem attention

Questions:

```text
Which subsystem deserves processing?
Which evidence family should be inspected?
Which hypothesis branch deserves validation?
Which workstream should receive budget?
```

## L — Local attention

Questions:

```text
Which claim?
Which variable?
Which line?
Which observation?
Which test?
Which dependency?
```

---

# 27. H/M/L Conservation Rule

Local attention must not silently redefine higher-level objectives.

```text
L priority
!=
H objective
```

Likewise:

```text
high-level importance
does not imply
every low-level detail deserves equal attention
```

Candidate hierarchy:

[
Goal_H
\rightarrow
Priority_M
\rightarrow
Allocation_L
]

with upward invalidation when lower-level evidence falsifies a higher-level premise.

---

# 28. Cross-Scale Escalation

Escalate from L → M or M → H when:

```text
local evidence changes system-level conclusion
local contradiction affects multiple branches
scope mismatch cannot be resolved locally
regime change affects architecture
authority boundary is crossed
resource exhaustion affects global objective
```

Do not escalate merely because a target is difficult.

---

# 29. Operators

Candidate L02 operators:

```text
OBSERVE_CANDIDATES()
NORMALIZE_TARGETS()
FILTER_INELIGIBLE()
ESTIMATE_RELEVANCE()
ESTIMATE_SALIENCE()
ESTIMATE_NOVELTY()
ESTIMATE_UNCERTAINTY()
ESTIMATE_DEPENDENCY_CRITICALITY()
ESTIMATE_CONSEQUENCE()
ESTIMATE_TIME_SENSITIVITY()
ESTIMATE_INFORMATION_VALUE()
ESTIMATE_COST()

ADMIT()
RANK()
ALLOCATE()
DEFER()
QUARANTINE()
ESCALATE()
REALLOCATE()
RELEASE()
INVALIDATE()
REPAIR()
```

Exact canonical operator vocabulary is `UNKNOWN/GAP`.

---

# 30. Core Invariants

```text
L02-INV-001
Attention is a resource-allocation function, not a truth function.

L02-INV-002
Attention does not create authority.

L02-INV-003
Attention proposal does not equal commit.

L02-INV-004
High salience cannot automatically override hard constraints.

L02-INV-005
High priority cannot automatically override hard constraints.

L02-INV-006
Attention allocations cannot exceed governed resource capacity.

L02-INV-007
Protected reserve cannot be silently consumed.

L02-INV-008
Objective relevance must remain explicit.

L02-INV-009
Scope must remain explicit where material.

L02-INV-010
Regime validity must remain explicit where material.

L02-INV-011
Provenance ancestry must not be mistaken for independent evidence.

L02-INV-012
Contradictions must not be hidden merely because they disrupt priority ranking.

L02-INV-013
Competing hypotheses remain competing until discriminating evidence exists.

L02-INV-014
UNKNOWN/GAP cannot silently become PASS.

L02-INV-015
Confidence cannot exceed the weakest load-bearing premise.

L02-INV-016
H/M/L distinctions must remain recoverable.

L02-INV-017
Local failure should invalidate dependent descendants, not unrelated state.

L02-INV-018
Optimization cannot weaken integrity.

L02-INV-019
Attention to a target does not establish causal status.

L02-INV-020
Attention allocation must remain provenance-recoverable where consequential.
```

---

# 31. Dependencies

## Upstream

Primary upstream dependency:

```text
L00_REALITY_ENVIRONMENT
↓
L01_SENSING_OBSERVATION
↓
L02_ATTENTION
```

L01 supplies potentially attendable observations or observation structures.

## Internal / supporting

Potential dependencies include:

```text
active objective state
constraint state
provenance state
scope/regime state
resource-budget state
dependency graph
uncertainty state
H/M/L context
```

## Downstream

L02 may route selected targets toward later cognitive functions such as:

```text
interpretation
working context
memory operations
reasoning
planning
decision
action proposal
metacognition
```

Exact cognitive-matrix ordering beyond available source material must not be invented.

---

# 32. Control-Plane Requirements

L02 cognition should remain distinct from authoritative control.

Candidate architecture:

```text
L02 ATTENTION
↓
PROPOSE RESOURCE ALLOCATION
↓
CONTROL PLANE
↓
VALIDATE:
  objective
  budget
  scope
  regime
  constraints
  provenance
  freshness
  authority
↓
COMMIT / BLOCK / REVALIDATE
```

Hard separation:

```text
COGNITIVE PREFERENCE
!=
CONTROL AUTHORITY
```

---

# 33. Agents

Logical L02 roles may include:

```text
L02_ATTENTION_ROUTER
L02_PRIORITY_ASSESSOR
L02_BUDGET_ALLOCATOR
L02_ATTENTION_BALANCER
L02_DEPENDENCY_SCOUT
L02_UNCERTAINTY_SCOUT
L02_CONTRADICTION_SCOUT
L02_ATTENTION_AUDITOR
L02_REPAIR_AGENT
```

These names represent candidate logical roles.

They are not proof that canonical AMOS requires separate deployed agents.

---

# 34. Skills

Potentially relevant AMOS skills:

```text
AMOS Attention Allocation Governor
AMOS Context Budget Governor
AMOS Constraint Propagation
AMOS Metacognitive Confidence Auditor
AMOS Provenance Trust Firewall
AMOS Risk Constraint Governor
AMOS Context Continuity Governor
AMOS Session Control Plane
AMOS Infrastructure Control Plane
AMOS RSCF Modeler
```

Skill availability does not imply automatic authority.

---

# 35. Primary Workflow

```text
1. RECEIVE candidate targets

2. RESOLVE active objective

3. RESOLVE available resource budget

4. IDENTIFY hard constraints

5. NORMALIZE target scope / regime / HML

6. IDENTIFY decision-changing uncertainty

7. ASSESS:
   - relevance
   - dependency criticality
   - consequence
   - uncertainty
   - time sensitivity
   - novelty
   - salience
   - information value
   - cost

8. APPLY hard admission gates

9. PRESERVE competing hypotheses / contradictions

10. RANK admissible targets

11. ALLOCATE bounded resources

12. RESERVE capacity for:
    - falsification
    - unexpected evidence
    - repair
    - escalation

13. PRODUCE allocation proposal

14. VALIDATE through control plane where required

15. OBSERVE results

16. REALLOCATE when decision-changing state changes
```

---

# 36. Adaptive Complexity Workflow

L02 should not spend maximum resources on every task.

Candidate levels:

```text
C0 — DIRECT
C1 — COMPACT
C2 — STRUCTURED
C3 — DEEP
C4 — MAXIMUM
```

Escalation factors:

```text
stakes
irreversibility
novelty
weak evidence
stale evidence
contradiction
causal ambiguity
scope mismatch
regime shift
competing models
governance impact
low trust
explicit user requirement
```

De-escalate after outcome-changing uncertainty is resolved.

---

# 37. Attention Reserve

A system allocating 100% of available capacity to known targets may become brittle.

Candidate rule:

[
B_{reserve} > 0
]

when operating conditions justify reserve capacity.

Reserve may support:

```text
unexpected evidence
contradictions
emergency validation
repair
high-impact user correction
regime shift
tool failure
```

The exact reserve policy is `UNKNOWN/GAP`.

---

# 38. Reallocation

Attention must remain adaptive.

Candidate transition:

[
A_{t+1}
=======

Reallocate(
A_t,
\Delta Evidence,
\Delta Goal,
\Delta Risk,
\Delta Uncertainty,
\Delta Regime
)
]

Reallocation should occur when new information materially changes the expected value of continued processing.

---

# 39. Stop Condition

Attention allocation should terminate or de-escalate when additional processing no longer has sufficient expected value.

Candidate condition:

```text
CLAIM SUFFICIENCY
+
DECISION SUFFICIENCY
+
ACTION SUFFICIENCY
+
NO MATERIAL UNRESOLVED CRITICAL GAP
→
STOP / DE-ESCALATE
```

This avoids infinite analysis.

---

# 40. Protocols

Candidate L02 protocol objects:

```text
AttentionCandidate
AttentionRequest
AttentionScore
AttentionAllocationProposal
AttentionAllocationDecision
AttentionBudgetRequest
AttentionBudgetState
AttentionDeferral
AttentionQuarantine
AttentionEscalation
AttentionReallocation
AttentionRelease
AttentionConflictNotice
AttentionAuditRecord
```

Suggested common envelope:

```yaml
AttentionProtocolEnvelope:

  message_id: MessageId
  target_id: CognitiveTargetId
  objective_id: GoalId | null

  hml:
    type: H | M | L

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef

  provenance:
    type: ProvenanceBundle

  uncertainty:
    type: UncertaintyVector

  timestamp:
    type: Timestamp

  status:
    type:
      - CANDIDATE
      - PROPOSED
      - ADMITTED
      - DEFERRED
      - QUARANTINED
      - ESCALATED
      - RELEASED
```

---

# 41. Evidence / Provenance

Every consequential allocation should preserve enough provenance to answer:

```text
What received attention?

Why did it receive attention?

Which objective justified it?

Which evidence affected ranking?

Which dependency made it important?

What resource was allocated?

What alternatives were deferred?

What constraints applied?

What uncertainty remained?

Which agent/system proposed the allocation?

Was the allocation committed?

What later changed it?
```

Candidate provenance tensor:

[
P_{L02}
=======

T[
target,
source,
objective,
dependency,
scope,
regime,
HML,
agent,
budget,
allocation,
time
]
]

---

# 42. Uncertainty Vector

Material L02 uncertainty may be separated into:

```yaml
uncertainty:

  evidence:
    meaning: uncertainty in evidence supporting priority

  model:
    meaning: uncertainty in the ranking/allocation model

  scope:
    meaning: uncertainty about applicability envelope

  temporal:
    meaning: uncertainty caused by freshness or timing

  causal:
    meaning: uncertainty in causal relevance

  execution:
    meaning: uncertainty in actual resource use / implementation

  provenance_independence:
    meaning: uncertainty about evidence ancestry and independence
```

Attention should preferentially reduce uncertainty that can change the decision.

---

# 43. Confidence Ceiling

For an attention conclusion (C):

[
Conf(C)
\le
\min_i Conf(P_i)
]

where (P_i) are load-bearing premises.

Example:

[
Conf(Allocate(x))
\le
\min(
Conf(G),
Conf(B),
Conf(D_x),
Conf(C),
Conf(Scope),
Conf(Regime)
)
]

Missing load-bearing evidence must produce:

```text
UNKNOWN/GAP
```

or conditional allocation, not fabricated certainty.

---

# 44. Failure Modes

```text
FM-L02-001  Salience Capture
FM-L02-002  Goal Drift
FM-L02-003  Attention Flooding
FM-L02-004  Budget Exhaustion
FM-L02-005  Reserve Exhaustion
FM-L02-006  Novelty Addiction
FM-L02-007  Threat Overweighting
FM-L02-008  Confirmation Attention
FM-L02-009  Contradiction Suppression
FM-L02-010  Dependency Blindness
FM-L02-011  Low-Level Rabbit Hole
FM-L02-012  High-Level Vagueness
FM-L02-013  HML Collapse
FM-L02-014  Scope Leakage
FM-L02-015  Regime Blindness
FM-L02-016  Stale Priority
FM-L02-017  Provenance Correlation Blindness
FM-L02-018  Attention/Truth Collapse
FM-L02-019  Attention/Authority Collapse
FM-L02-020  Proposal/Commit Collapse
FM-L02-021  Unknown-As-Pass
FM-L02-022  Premature Closure
FM-L02-023  Infinite Analysis
FM-L02-024  Cost Blindness
FM-L02-025  Consequence Blindness
FM-L02-026  Time-Sensitivity Blindness
FM-L02-027  Uncertainty Neglect
FM-L02-028  Over-Validation
FM-L02-029  Under-Validation
FM-L02-030  Global Recompute After Local Failure
```

---

# 45. Failure Example — Salience Capture

```text
highly visible event
↓
high salience
↓
attention monopolization
↓
goal-critical quiet dependency ignored
↓
incorrect downstream conclusion
```

Repair:

```text
restore active objective
↓
identify load-bearing dependencies
↓
re-score candidate set
↓
reserve attention for non-salient critical items
```

---

# 46. Failure Example — Rabbit Hole

```text
interesting local detail
↓
continued attention
↓
increasing sunk cognitive cost
↓
declining decision value
↓
objective drift
```

Repair test:

```text
"If this detail were resolved,
could it materially change the answer?"
```

If no:

```text
DEFER / RELEASE ATTENTION
```

---

# 47. Failure Example — Confirmation Attention

```text
leading hypothesis
↓
evidence supporting hypothesis receives attention
↓
contradictory evidence receives less attention
↓
apparent confidence increases
↓
false convergence
```

Repair:

```text
allocate explicit adversarial budget
↓
seek strongest competing explanation
↓
seek cheapest discriminating evidence
```

---

# 48. Repair / Recovery

General L02 repair:

```text
DETECT ATTENTION FAILURE
↓
FREEZE AFFECTED ALLOCATION
↓
RESTORE GOVERNING OBJECTIVE
↓
IDENTIFY FAILED PREMISE
↓
TRACE DEPENDENCIES
↓
PRESERVE UNAFFECTED ATTENTION STATE
↓
RELEASE MISALLOCATED RESOURCES
↓
RECONSTRUCT CANDIDATE SET
↓
REAPPLY HARD INVARIANTS
↓
RE-RANK
↓
REALLOCATE
↓
REVALIDATE
```

---

# 49. Selective Invalidation

If premise (p) becomes invalid:

[
Invalid(p)
\Rightarrow
Invalidate(Descendants(p))
]

not:

[
Invalid(p)
\Rightarrow
Invalidate(All)
]

unless the entire attention state actually depends on (p).

This preserves unaffected work.

---

# 50. Rollback

Rollback should return to the nearest valid attention state.

```text
FAILED CURRENT STATE
↓
IDENTIFY LAST VALID STATE
↓
PRESERVE VALID ALLOCATIONS
↓
REMOVE INVALID DESCENDANTS
↓
REPLAY FROM CHANGED PREMISE
```

Rollback must not erase provenance of the failed path.

---

# 51. Tests / Validators

Required model validators:

```text
VALIDATE_SOURCE_BOUNDARY
VALIDATE_TARGET_TYPING
VALIDATE_OBJECTIVE_BINDING
VALIDATE_BUDGET
VALIDATE_RESERVE
VALIDATE_HARD_INVARIANTS
VALIDATE_SCOPE
VALIDATE_REGIME
VALIDATE_HML
VALIDATE_PROVENANCE
VALIDATE_DEPENDENCY_GRAPH
VALIDATE_UNCERTAINTY
VALIDATE_CONFLICT_PRESERVATION
VALIDATE_AUTHORITY_SEPARATION
VALIDATE_PROPOSAL_COMMIT_SEPARATION
VALIDATE_SELECTIVE_INVALIDATION
VALIDATE_REPAIR
VALIDATE_STOP_CONDITION
```

---

# 52. Minimum Test Suite

```text
TEST-L02-001
High salience alone cannot force allocation.

TEST-L02-002
High priority cannot override a hard constraint.

TEST-L02-003
Attention allocation cannot exceed available budget.

TEST-L02-004
Protected reserve cannot be silently consumed.

TEST-L02-005
Attention does not change truth status.

TEST-L02-006
Attention does not grant authority.

TEST-L02-007
Proposal cannot automatically become commit.

TEST-L02-008
Changed governing objective triggers re-evaluation.

TEST-L02-009
Critical contradiction receives non-zero consideration where consequential.

TEST-L02-010
Correlated evidence is not treated as independent confirmation.

TEST-L02-011
Scope mismatch prevents silent generalization.

TEST-L02-012
Regime shift triggers priority re-evaluation.

TEST-L02-013
Local failure invalidates dependent descendants only.

TEST-L02-014
H/M/L scale identity survives allocation.

TEST-L02-015
UNKNOWN/GAP cannot silently become PASS.

TEST-L02-016
Low-value rabbit-hole processing can terminate.

TEST-L02-017
Critical dependency may outrank high-salience noncritical target.

TEST-L02-018
Competing hypotheses remain visible.

TEST-L02-019
Repair preserves provenance.

TEST-L02-020
No implementation claim is made without executable evidence.
```

---

# 53. Adversarial Tests

Test L02 against:

```text
clickbait-like salience
repetition
authority signaling
source duplication
fear/threat amplification
novelty flooding
large irrelevant tool output
contradictory evidence
goal substitution
stale objectives
scope injection
regime shifts
false urgency
budget starvation
recursive rabbit holes
agent self-prioritization
memory-driven distraction
external-effect smuggling
```

---

# 54. Falsifiers

This definition must be revised if:

```text
direct canonical L02 material defines attention differently

canonical AMOS assigns scarcity allocation to another primitive

canonical AMOS treats L02 solely as perceptual selection rather than
general reasoning/observation allocation

canonical H/M/L behavior materially contradicts this model

canonical control-plane ownership differs from the proposed separation

canonical equations contradict the model variables

executable runtime demonstrates incompatible semantics

formal analysis identifies contradictory invariants
```

---

# 55. Competing Definitions

Because direct detailed canon is incomplete, preserve alternatives.

## COMPETING_001 — Resource Allocation Definition

```text
L02 allocates scarce reasoning and observation resources.
```

**Support:** strongest currently recovered primitive wording.

## COMPETING_002 — Perceptual Selection Definition

```text
L02 primarily filters sensory/observation streams before cognition.
```

**Status:** plausible architectural alternative but not established by the supplied placeholder.

## COMPETING_003 — General Cognitive Scheduling Definition

```text
L02 schedules resources across observation, reasoning,
retrieval, validation, memory, and planning.
```

**Status:** broader AMOS model extension.

Current preferred interpretation:

```text
COMPETING_001
```

with controlled extension toward `COMPETING_003`.

Do not collapse these until direct canon discriminates them.

---

# 56. Gap Matrix

```yaml
gap_matrix:

  primitive_identity:
    status: SOURCE_SUPPORTED

  attention_allocation_role:
    status: SOURCE_SUPPORTED

  scarce_reasoning_resources:
    status: SOURCE_SUPPORTED

  scarce_observation_resources:
    status: SOURCE_SUPPORTED

  canonical_definition_full:
    status: GAP
    criticality: CRITICAL

  canonical_scope:
    status: GAP
    criticality: CRITICAL

  perceptual_vs_general_attention_scope:
    status: GAP
    criticality: CRITICAL

  canonical_variables:
    status: GAP
    criticality: DECISION_RELEVANT

  canonical_equations:
    status: GAP
    criticality: DECISION_RELEVANT

  canonical_operators:
    status: GAP
    criticality: DECISION_RELEVANT

  canonical_state_machine:
    status: GAP
    criticality: DECISION_RELEVANT

  canonical_budget_units:
    status: GAP
    criticality: DECISION_RELEVANT

  canonical_control_plane_owner:
    status: GAP
    criticality: CRITICAL

  canonical_agents:
    status: GAP
    criticality: EXPLANATORY

  canonical_protocols:
    status: GAP
    criticality: EXPLANATORY

  executable_runtime:
    status: GAP
    criticality: CRITICAL

  executed_tests:
    status: GAP
    criticality: CRITICAL

  model_definition:
    status: COMPLETE

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

  HML:
    status: MODEL_COMPLETE

  control_plane_requirements:
    status: MODEL_COMPLETE

  workflows:
    status: MODEL_COMPLETE

  evidence_provenance:
    status: MODEL_COMPLETE

  uncertainty:
    status: MODEL_COMPLETE

  failure_repair:
    status: MODEL_COMPLETE

  validators:
    status: MODEL_COMPLETE_UNEXECUTED
```

---

# 57. Cheapest Discriminating Evidence

Highest-value retrieval sequence:

```text
1. Direct canonical L02_ATTENTION definition source

2. Direct L02 PURPOSE / VARIABLES / STATE / OPERATORS

3. Cognitive-matrix source defining neighboring L01 and L03

4. AMOS cognition architecture describing attention routing

5. AMOS Full Brain OS dependency graph

6. AMOS_CORE runtime implementation

7. Executed tests
```

The cheapest decisive question is:

> **Does canonical L02 define attention narrowly as perceptual/observation selection, or broadly as allocation of scarce reasoning and observation resources across cognition?**

Until answered, broader cognitive scheduling remains `MODEL`.

---

# 58. RSCF Completion State

```yaml
rscf:

  id: L02_ATTENTION_DEFINITION

  claim:
    L02_ATTENTION is the AMOS cognitive primitive for allocating
    scarce reasoning and observation resources among competing
    candidate targets.

  claim_class: MODEL

  source_supported_core:
    - attention allocation
    - scarce reasoning resources
    - scarce observation resources

  model_extensions:
    - typed attention candidates
    - budget state
    - dependency criticality
    - uncertainty-aware allocation
    - H/M/L routing
    - control-plane separation
    - selective invalidation
    - repair workflow

  evidence:
    - recovered L02_ATTENTION primitive placeholder
    - AMOS Attention Allocation Governor architecture
    - AMOS v4.4 governance patterns

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    subsystem: COGNITIVE_MATRIX
    primitive: L02_ATTENTION
    artifact: DEFINITION.md
    derivation: SOURCE_BOUNDED_MODEL_COMPLETION

  scope:
    system: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    primitive: L02_ATTENTION

  regime:
    finite cognitive-resource allocation

  freshness:
    revalidate_when:
      - direct L02 canon is recovered
      - neighboring cognitive primitive definitions change
      - AMOS_CORE attention implementation is recovered
      - attention control-plane ownership changes

  dependencies:
    - L00_REALITY_ENVIRONMENT
    - L01_SENSING_OBSERVATION
    - L02_ATTENTION_PURPOSE
    - L02_ATTENTION_VARIABLES
    - L02_ATTENTION_STATE
    - L02_ATTENTION_OPERATORS
    - L02_ATTENTION_INVARIANTS
    - L02_ATTENTION_DEPENDENCIES
    - L02_ATTENTION_HML
    - L02_ATTENTION_CONTROL_PLANES
    - L02_ATTENTION_AGENTS
    - L02_ATTENTION_SKILLS
    - L02_ATTENTION_WORKFLOWS
    - L02_ATTENTION_PROTOCOLS
    - L02_ATTENTION_PROVENANCE
    - L02_ATTENTION_REPAIR
    - L02_ATTENTION_TESTS

  competing:
    - resource-allocation attention
    - perceptual-selection attention
    - general cognitive-scheduling attention

  falsifiers:
    - direct canon defines materially different primitive semantics
    - canonical scope excludes reasoning-resource allocation
    - canonical architecture assigns allocation elsewhere
    - executable runtime contradicts modeled interfaces
    - formal validation finds invariant inconsistency

  uncertainty:
    evidence: MEDIUM_HIGH
    model: MEDIUM
    scope: HIGH
    temporal: MEDIUM
    causal: LOW
    execution: HIGH
    provenance_independence: MEDIUM

  confidence_ceiling:
    source-supported primitive role with model-completed architecture;
    exact canonical scope, equations, state, and runtime remain unresolved

  gap_status:
    canonical_definition: CRITICAL_GAP
    canonical_scope: CRITICAL_GAP
    canonical_control_ownership: CRITICAL_GAP
    executable_runtime: CRITICAL_GAP
    executed_validation: CRITICAL_GAP

  cheapest_discriminating_test:
    recover direct L02 definition and determine whether attention
    scope is perceptual-only or general scarce cognitive-resource allocation
```

---

# 59. Completion State

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

  gap_status:
    status: EXPLICIT

  canonical_completion:
    status: UNKNOWN/GAP

  implementation:
    status: UNKNOWN/GAP

  empirical_validation:
    status: UNKNOWN/GAP

  overall:
    status: COMPLETE_FOR_DECLARED_MODEL_SCOPE

  conclusion_class:
    MODEL / CONDITIONAL
```

---

# 60. Hard Boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

L02-specific boundaries:

```text
ATTENTION != TRUTH

ATTENTION != EVIDENCE

ATTENTION != IMPORTANCE

ATTENTION != SALIENCE

ATTENTION != AUTHORITY

ATTENTION != ACTION

ATTENTION != MEMORY ADMISSION

ATTENTION != CAUSATION

PRIORITY != TRUTH

PRIORITY != AUTHORITY

SALIENCE != PRIORITY

SALIENCE != TRUTH

REPETITION != IMPORTANCE

REPETITION != INDEPENDENT EVIDENCE

NOVELTY != VALUE

URGENCY != IMPORTANCE

HIGH UNCERTAINTY != AUTOMATIC HIGH PRIORITY

HIGH CONFIDENCE != AUTOMATIC LOW PRIORITY

LOCAL DETAIL != GLOBAL OBJECTIVE

H ATTENTION != M ATTENTION

M ATTENTION != L ATTENTION

MODEL DEFINITION != CANONICAL DEFINITION

IMPLEMENTED != VALIDATED
```

---

# 61. References

```text
[[L02_ATTENTION/PLACEHOLDER.md]]

[[L02_ATTENTION — Purpose]]
[[L02_ATTENTION — Variables]]
[[L02_ATTENTION — State]]
[[L02_ATTENTION — Operators]]
[[L02_ATTENTION — Invariants]]
[[L02_ATTENTION — Dependencies]]
[[L02_ATTENTION — Hml]]
[[L02_ATTENTION — Control Planes]]
[[L02_ATTENTION — Agents]]
[[L02_ATTENTION — Skills]]
[[L02_ATTENTION — Workflows]]
[[L02_ATTENTION — Protocols]]
[[L02_ATTENTION — Provenance]]
[[L02_ATTENTION — Rscf]]
[[L02_ATTENTION — Failure Modes]]
[[L02_ATTENTION — Repair]]
[[L02_ATTENTION — Tests]]

[[L01_SENSING_OBSERVATION]]

[[AMOS Attention Allocation Governor]]
[[AMOS Context Budget Governor]]
[[AMOS Constraint Propagation]]
[[AMOS Infrastructure Control Plane]]
[[AMOS Deterministic AI Control Plane]]
[[AMOS Metacognitive Confidence Auditor]]
[[AMOS Provenance Trust Firewall]]
[[AMOS RSCF]]
[[AMOS Full Brain OS]]
[[AMOS CORE v4.4]]
```

---

# 62. Governing Definition

> **L02_ATTENTION is the AMOS cognitive primitive for allocating scarce reasoning and observation resources among competing targets. It determines what deserves additional cognitive processing under an active objective, finite budget, dependencies, uncertainty, constraints, provenance, scope, regime, and H/M/L context. Attention changes processing allocation; it does not by itself establish truth, importance, causation, authority, memory admission, or permission to act.**

---

# 63. Canon Boundary

The strongest currently supportable statement is:

```text
SOURCE-SUPPORTED:
L02_ATTENTION concerns attention allocation
and scarce reasoning/observation resources.

MODEL:
The detailed typed allocation architecture,
budget model, H/M/L routing, uncertainty allocation,
dependency prioritization, control-plane separation,
repair logic, protocols, and validators in this file.

UNKNOWN/GAP:
Exact canonical definition,
exact scope,
exact equations,
exact state schema,
exact control-plane ownership,
and executable implementation.
```

Therefore:

```text
CONCLUSION CLASS:
MODEL / CONDITIONAL

NOT:
VERIFIED CANON
```

```text

This version deliberately keeps the **narrow-vs-broad attention scope unresolved**. That is the most important gap to close before promoting `L02_ATTENTION/DEFINITION.md` from model completion toward canonical status.
```

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]]
