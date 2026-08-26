---
tags:
  - amos
  - cognitive-matrix
  - l02
  - attention
  - invariants
  - rscf
  - governance

title: "L02_ATTENTION — Invariants"
origin_architect: "Trang Phan"
status: "MODEL_SPECIFICATION / SOURCE-BOUNDED / UNVALIDATED"
epistemic_class: "MODEL"
runtime_alignment: "AMOS Full Brain OS / AMOS_CORE v4.4 lineage"
---

# L02_ATTENTION — Invariants

**Class:** `COGNITIVE_PRIMITIVE_INVARIANT_CONTRACT`  
**Origin architect / steward:** Trang Phan  
**Primitive:** `L02_ATTENTION`  
**Artifact:** `INVARIANTS.md`  
**Status:** `AMOS_MODEL / SOURCE-BOUNDED / UNVALIDATED`

> **Canon boundary:** the available L02 material supports attention as allocation of scarce reasoning/observation resources. The invariant system below formalizes that primitive inside AMOS governance. Unless independently traced to direct L02 canon, individual invariant IDs and equations are `AMOS_MODEL`, not recovered canonical laws.

---

# 0. Purpose

Define the conditions that must remain true whenever `L02_ATTENTION` selects, ranks, allocates, sustains, shifts, suppresses, escalates, or terminates attention.

The invariant layer exists to prevent attention from silently becoming:

```text
truth
evidence
confidence
authority
commit permission
causal proof
unbounded resource consumption
```

Core contract:

```text
ATTENTION = RESOURCE ALLOCATION

ATTENTION != TRUTH
ATTENTION != EVIDENCE
ATTENTION != AUTHORITY
ATTENTION != COMMIT
```

---

# 1. Source / Canon References

## 1.1 Source-supported semantic core

Recovered L02 meaning:

```text
L02_ATTENTION
=
attention allocation;
budget scarce reasoning/observation resources
```

This supports two load-bearing propositions:

```text
A. attention performs allocation
B. the allocated reasoning/observation resource is scarce
```

The detailed invariant registry below is an architectural formalization of those propositions.

## 1.2 AMOS framework references

Relevant AMOS framework constraints include:

```text
integrity > completeness > fluency > speed > token savings

smallest sufficient proof scope

trust is local, typed, scoped,
provenance-aware, regime-aware,
and freshness-bounded

derived confidence cannot exceed
the weakest load-bearing premise
unless independently revalidated

structural similarity != causation

capability != authority

proposal != commit

UNKNOWN/GAP != PASS

preserve contradictions

preserve competing hypotheses

prefer selective invalidation

preserve provenance

respect scope/regime boundaries
```

## 1.3 Related L02 contracts

```text
[[L02_ATTENTION — README]]
[[L02_ATTENTION — Purpose]]
[[L02_ATTENTION — Definition]]
[[L02_ATTENTION — Variables]]
[[L02_ATTENTION — State]]
[[L02_ATTENTION — Operators]]
[[L02_ATTENTION — Dependencies]]
[[L02_ATTENTION — Equations]]
[[L02_ATTENTION — HML]]
[[L02_ATTENTION — Control Planes]]
[[L02_ATTENTION — Agents]]
[[L02_ATTENTION — Skills]]
[[L02_ATTENTION — Workflows]]
[[L02_ATTENTION — Protocols]]
[[L02_ATTENTION — Provenance]]
[[L02_ATTENTION — Failure Modes]]
[[L02_ATTENTION — Gap Matrix]]
[[L02_ATTENTION — Repair]]
[[L02_ATTENTION — Rscf]]
[[L02_ATTENTION — Tests]]

[[L01_SENSING_OBSERVATION]]
```

---

# 2. Definition and Scope

An L02 invariant is a condition that must remain true across admissible attention-state transitions.

Let:

[
A_t
]

denote attention state at time (t), and:

[
T(A_t,o)
\rightarrow
A_{t+1}
]

denote application of an attention operator (o).

For invariant (I_k):

[
I_k(A_t)=true
]

and any admissible transition must satisfy:

[
I_k(A_{t+1})=true
]

unless the transition explicitly enters:

```text
FAIL
QUARANTINE
RECOVERY
ESCALATION
```

because preservation cannot be established.

This is an `AMOS_MODEL` transition contract.

---

# 3. Typed Inputs

```yaml
AttentionInvariantInput:

  attention_state:
    type: AttentionState

  candidate_set:
    type: AttentionCandidate[]

  allocation:
    type: AttentionAllocation[]

  objective:
    type: ObjectiveState

  constraints:
    type: ConstraintSet

  resource_budget:
    type: ResourceBudget

  dependencies:
    type: DependencyGraph

  evidence:
    type: EvidenceBundle

  provenance:
    type: ProvenanceBundle

  uncertainty:
    type: UncertaintyVector

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef

  freshness:
    type: FreshnessState

  authority:
    type: AuthorityEnvelope

  proposed_operator:
    type: AttentionOperator
```

---

# 4. Typed Outputs

```yaml
AttentionInvariantResult:

  valid:
    type: Boolean

  invariant_results:
    type: InvariantCheck[]

  violated:
    type: InvariantId[]

  threatened:
    type: InvariantId[]

  blocked_transition:
    type: Boolean

  escalation_required:
    type: Boolean

  quarantine_required:
    type: Boolean

  repair_required:
    type: Boolean

  affected_dependencies:
    type: DependencyRef[]

  provenance:
    type: ProvenanceBundle

  confidence_ceiling:
    type: ConfidenceBound

  gap_status:
    type: GapStatus
```

Invariant evaluation must not silently convert an unresolved check into `true`.

```text
UNKNOWN != TRUE
```

---

# 5. State Variables

```text
A_t       current attention state
C_t       candidate set
B_t       available attention budget
b_i       allocation to candidate i
P_i       candidate priority
S_i       candidate salience
R_i       decision/risk relevance
U_i       uncertainty
D_i       dependency criticality
F_i       freshness state
E_i       evidence state
V_i       provenance state
Q_i       scope envelope
G_i       regime
Auth_i    authority state
Conf_i    confidence bound
X_t       unresolved contradiction set
Gap_t     unresolved gap set
```

---

# 6. Invariant Families

The L02 invariant registry is divided into:

```text
I.   Identity invariants
II.  Resource invariants
III. Epistemic invariants
IV.  Provenance invariants
V.   Scope/regime invariants
VI.  Dependency invariants
VII. Contradiction/gap invariants
VIII. Governance/authority invariants
IX.  H/M/L invariants
X.   Transition/recovery invariants
```

---

# 7. Identity Invariants

## L02-INV-001 — Attention Identity

```text
ATTENTION
=
allocation of scarce reasoning/observation resources
```

An implementation that merely labels information as important without affecting resource allocation does not, by this contract alone, establish implementation of L02.

---

## L02-INV-002 — Attention ≠ Truth

[
Attend(x)
\not\Rightarrow
True(x)
]

A candidate receiving attention does not establish its truth.

---

## L02-INV-003 — Attention ≠ Evidence

[
Attend(x)
\not\Rightarrow
Evidence(x)
]

Attention can be directed toward:

```text
hypotheses
contradictions
unknowns
false claims
tests
risks
speculation
```

without promoting them to evidence.

---

## L02-INV-004 — Attention ≠ Confidence

[
Priority(x)
\not\Rightarrow
Confidence(x)
]

Increasing attention priority must not independently raise epistemic confidence.

---

## L02-INV-005 — Attention ≠ Causality

[
Attend(x)
\not\Rightarrow
Cause(x)
]

High attention may reflect risk, uncertainty, novelty, salience, or dependency importance rather than causal importance.

---

# 8. Resource Invariants

## L02-INV-006 — Finite Budget

For a bounded attention cycle:

[
B_t < \infty
]

where the relevant budget dimensions are explicitly typed.

Possible dimensions:

```text
tokens
time
tool calls
compute
retrieval operations
agent calls
working-memory capacity
human-review capacity
```

---

## L02-INV-007 — Allocation Conservation

For allocations sharing the same unit:

[
\sum_i b_i \le B_t
]

The system may not allocate more of a bounded resource than is available.

---

## L02-INV-008 — Unit Integrity

Different resource dimensions must remain typed.

Therefore:

```text
500 tokens
+
4 tool calls
+
20 seconds
```

cannot be treated as one scalar budget without an explicit conversion function.

---

## L02-INV-009 — No Negative Allocation

[
b_i \ge 0
]

unless a separately defined signed resource model explicitly requires otherwise.

---

## L02-INV-010 — Resource Use Requires Addressable Candidate

Allocated attention must resolve to an identifiable candidate or governed exploration pool.

```text
allocation
→ candidate/procedure reference
```

Untraceable resource consumption violates accounting integrity.

---

# 9. Priority Invariants

## L02-INV-011 — Priority Is Decision-Relative

Priority must be interpreted relative to an objective and context.

[
P_i =
P(i\mid Objective,Scope,Regime,t)
]

There is no required globally context-free priority.

---

## L02-INV-012 — Salience ≠ Priority

[
Salience_i
\not\equiv
Priority_i
]

Highly noticeable information need not deserve high reasoning allocation.

---

## L02-INV-013 — Novelty ≠ Priority

[
Novelty_i
\not\Rightarrow
HighPriority_i
]

Novelty can justify inspection but cannot automatically dominate load-bearing dependencies.

---

## L02-INV-014 — Repetition ≠ Priority

Repeated information does not become increasingly important merely through repetition.

This protects against:

```text
frequency capture
prompt repetition
source duplication
retrieval duplication
narrative reinforcement
```

---

## L02-INV-015 — Critical Constraints Dominate Preferences

If candidate (x) implicates a hard constraint and candidate (y) only advances a soft preference, the soft preference cannot compensate for violating the hard constraint.

```text
hard constraint
>
soft optimization
```

---

# 10. Epistemic Invariants

## L02-INV-016 — Attention Cannot Promote Claim Class

Attention allocation alone may not perform:

```text
UNKNOWN/GAP → MODEL
MODEL → DERIVED
DERIVED → VERIFIED
COMPETING → VERIFIED
```

Claim-class promotion requires appropriate evidence.

---

## L02-INV-017 — Confidence Ceiling Preservation

If conclusion (C) depends on load-bearing premises (p_1...p_n):

[
Conf(C)
\le
\min_i Conf(p_i)
]

unless independent revalidation changes the evidence graph.

Attention expenditure alone does not increase the ceiling.

---

## L02-INV-018 — Missing Evidence Remains Missing

```text
more reasoning about missing evidence
!=
new evidence
```

If a required source or observation is absent, additional internal attention cannot silently fill it.

---

## L02-INV-019 — Observation / Inference Separation

Information originating from L01 or another evidence source must remain distinguishable from L02-derived prioritization or inference.

```text
OBSERVATION
!=
ATTENTION_SCORE
!=
DERIVED_INTERPRETATION
```

---

## L02-INV-020 — Attention Does Not Repair Evidence Automatically

Attending to stale, corrupted, contradictory, or weak evidence does not make it valid.

---

# 11. Provenance Invariants

## L02-INV-021 — Provenance Preservation

Every materially decision-relevant attention candidate should retain source ancestry sufficient to recover why it entered the candidate set.

```text
candidate
→ source/origin
→ transformation lineage
```

---

## L02-INV-022 — Allocation Provenance

A material allocation decision should be attributable to:

```text
objective
candidate
priority rationale
constraints
budget state
operator
```

where the runtime supports such state.

---

## L02-INV-023 — Correlated Evidence Is Not Independent Evidence

If:

```text
E1 ← Source A
E2 ← Source A
E3 ← Source A
```

then attention to all three does not create three independent confirmations.

---

## L02-INV-024 — Reformatting Does Not Reset Origin

```text
summary(Source A)
translation(Source A)
embedding(Source A)
agent restatement(Source A)
```

remain descendants of `Source A` for independence accounting.

---

## L02-INV-025 — Provenance Loss Blocks Strong Promotion

If load-bearing provenance becomes unrecoverable, downstream conclusions requiring that provenance must be downgraded, quarantined, or marked `UNKNOWN/GAP`.

---

# 12. Scope and Regime Invariants

## L02-INV-026 — Scope Preservation

Candidate evidence retains its applicability envelope through attention processing.

[
Scope_{out}
\subseteq
Scope_{supported}
]

unless expansion is independently justified.

---

## L02-INV-027 — No Silent Scope Generalization

Local evidence cannot silently become universal evidence.

```text
one repository
!=
all repositories

one regime
!=
all regimes

one user
!=
all users

one benchmark
!=
general capability
```

---

## L02-INV-028 — Regime Preservation

Attention processing must retain relevant regime identity.

```text
normal
stress
simulation
production
historical
forecast
```

must not be silently merged.

---

## L02-INV-029 — Regime Shift Requires Revalidation

If applicability depends on regime (G_a) and the system moves to (G_b):

[
G_a \neq G_b
]

then stale attention conclusions must be revalidated where the shift can alter the decision.

---

## L02-INV-030 — Freshness Is Not Optional When Material

Time-sensitive attention candidates must retain freshness state.

```text
fresh
stale
unknown freshness
```

must remain distinguishable.

---

# 13. Dependency Invariants

## L02-INV-031 — Load-Bearing Dependencies Receive Protection

Attention optimization may not discard a premise or dependency whose failure can flip the governing conclusion merely because it is expensive to inspect.

---

## L02-INV-032 — Dependency Closure Before Local Fast Path

Local reasoning is permitted only when relevant dependency closure is sufficiently established for the intended claim.

This does not require loading every dependency.

It requires resolving those capable of materially changing the answer.

---

## L02-INV-033 — Selective Invalidation

If dependency (d) fails:

[
Invalidate(d)
\Rightarrow
Invalidate(Descendants(d))
]

not:

[
Invalidate(d)
\Rightarrow
Invalidate(AllState)
]

unless (d) is globally load-bearing.

---

## L02-INV-034 — Independent Branch Preservation

Failure of one branch must not destroy independent valid branches.

---

## L02-INV-035 — No Hidden Dependency Promotion

A conclusion cannot be promoted while an unresolved hidden dependency known to be load-bearing remains omitted from the proof scope.

---

# 14. Contradiction and Gap Invariants

## L02-INV-036 — Contradictions Remain Visible

Attention compression must not erase unresolved contradictions.

```text
CONTRADICTION
!=
NOISE
```

unless explicitly adjudicated with evidence.

---

## L02-INV-037 — Competing Hypotheses Remain Competing

When evidence does not discriminate between materially incompatible hypotheses:

```text
COMPETING
```

must be preserved.

Attention allocation may seek discriminating evidence but cannot force convergence.

---

## L02-INV-038 — UNKNOWN/GAP ≠ PASS

```text
UNKNOWN/GAP
!=
PASS
```

A missing invariant check cannot be treated as a successful invariant check.

---

## L02-INV-039 — Critical Gap Priority

A gap capable of changing a consequential decision must not be suppressed by lower-impact explanatory or cosmetic work.

Gap ordering:

```text
CRITICAL
DECISION-RELEVANT
EXPLANATORY
COSMETIC
```

---

## L02-INV-040 — Gap Closure Requires Evidence

A gap is not closed because:

```text
a plausible answer exists
a model generated a completion
the answer sounds coherent
no contradiction was found
```

Closure requires evidence appropriate to the gap class.

---

# 15. Governance / Authority Invariants

## L02-INV-041 — Capability ≠ Authority

```text
CAPABILITY
!=
AUTHORITY
```

An agent capable of attending to or analyzing an action does not thereby gain permission to perform it.

---

## L02-INV-042 — Proposal ≠ Commit

```text
PROPOSAL
!=
COMMIT
```

Attention may produce recommendations or candidate actions.

Durable effects require the governing commit path.

---

## L02-INV-043 — Priority ≠ Authorization

[
HighPriority(x)
\not\Rightarrow
Authorized(x)
]

Urgency cannot manufacture authority.

---

## L02-INV-044 — Resource Availability ≠ Authority

Available compute, tools, money, time, or agent capacity does not create permission.

---

## L02-INV-045 — Attention Cannot Override Control Plane

L02 is subordinate to applicable:

```text
authority
policy
constraint
provenance
commit-time
risk
```

control-plane requirements.

---

# 16. H/M/L Invariants

## L02-INV-046 — H/M/L Distinction

```text
H != M != L
```

H, M, and L attention states must remain semantically distinguishable.

---

## L02-INV-047 — H Constrains M

Governing H-level requirements constrain M-level allocation.

M cannot silently rewrite the governing objective.

---

## L02-INV-048 — M Constrains L

L-level resource consumption must remain within M allocation.

---

## L02-INV-049 — L Does Not Automatically Generalize to H

[
L\ evidence
\not\Rightarrow
H\ conclusion
]

without valid aggregation and applicability.

---

## L02-INV-050 — H Does Not Manufacture L

[
H\ expectation
\not\Rightarrow
L\ observation
]

This protects against top-down hallucination.

---

## L02-INV-051 — Cross-Level Provenance Preservation

Every decision-relevant H↔M↔L transformation retains recoverable ancestry.

---

## L02-INV-052 — Cross-Level Confidence Non-Inflation

Aggregation upward cannot increase confidence solely because multiple dependent lower-level objects were combined.

---

## L02-INV-053 — Local Completion ≠ Global Completion

```text
L complete
!=
M complete

M complete
!=
H complete
```

---

# 17. Transition Invariants

## L02-INV-054 — Operators Must Preserve Invariants

For admissible operator (o):

[
Valid(A_t)
\land
Apply(o,A_t)
\Rightarrow
Valid(A_{t+1})
]

or the transition must fail closed.

---

## L02-INV-055 — Unsafe Transition Must Not Silently Succeed

If preservation cannot be established:

```text
PASS
```

is forbidden.

Allowed states include:

```text
BLOCK
QUARANTINE
ESCALATE
REPAIR
UNKNOWN/GAP
```

---

## L02-INV-056 — No Irreversible Attention-Induced Effect Without Governance

If an attention-derived proposal could cause irreversible external effects, L02 must hand off to appropriate authority/commit governance.

---

## L02-INV-057 — Stop Requires Sufficiency

Attention may stop when relevant sufficiency conditions are met.

Conceptually:

[
Stop =
ClaimSufficient
\land
DecisionSufficient
\land
ActionSufficient
]

with non-applicable components explicitly marked.

---

## L02-INV-058 — Resource Exhaustion ≠ Epistemic Closure

Running out of budget does not mean the problem is solved.

```text
BUDGET_EXHAUSTED
!=
VERIFIED
```

---

# 18. Control-Plane Requirements

The control plane should enforce or independently validate invariants involving:

```text
authority
hard constraints
resource ceilings
scope
regime
freshness
provenance requirements
commit eligibility
irreversible effects
```

L02 may evaluate and propose.

The control plane owns durable authorization where applicable.

Minimum separation:

```text
L02:
  ATTEND
  RANK
  ALLOCATE
  DEFER
  ESCALATE
  PROPOSE

CONTROL PLANE:
  AUTHORIZE
  REJECT EFFECT
  VALIDATE COMMIT ELIGIBILITY
  FINALIZE DURABLE EFFECT
```

---

# 19. Agents

Proposed logical roles:

```text
L02_INVARIANT_AUDITOR
L02_RESOURCE_AUDITOR
L02_EPISTEMIC_AUDITOR
L02_PROVENANCE_AUDITOR
L02_SCOPE_REGIME_AUDITOR
L02_DEPENDENCY_AUDITOR
L02_HML_AUDITOR
L02_RECOVERY_COORDINATOR
```

These are architectural roles, not claims of implemented agents.

No auditing agent may self-certify implementation merely because it can describe the invariant.

---

# 20. Skills

Potential supporting AMOS capabilities:

```text
AMOS Attention Allocation Governor
AMOS Constraint Propagation RSCF Engine
AMOS Context Budget Governor RSCF
AMOS Cross-Scale RSCF Tensor Engine
AMOS Provenance Trust Firewall
AMOS Metacognitive Confidence Auditor
AMOS Claim Verifier
AMOS Infrastructure Control Plane
AMOS Risk Constraint Governor
AMOS Repair Harm Auditor
AMOS RSCF Modeler
```

Availability of a skill:

```text
!= canonical dependency
!= runtime invocation
!= validation
!= authority
```

unless independently evidenced.

---

# 21. Workflow

```text
RECEIVE attention state
↓
RESOLVE applicable invariant set
↓
TYPE candidate / resource / scope / regime
↓
CHECK hard invariants
↓
CHECK budget constraints
↓
CHECK epistemic separation
↓
CHECK provenance
↓
CHECK dependencies
↓
CHECK contradictions / gaps
↓
CHECK H/M/L preservation
↓
CHECK authority boundary
↓
IF all required checks PASS
    allow proposed attention transition
ELSE IF recoverable
    repair / reroute / selectively invalidate
ELSE IF unresolved
    quarantine / escalate / UNKNOWN
ELSE
    block
```

---

# 22. Protocol

```yaml
L02InvariantCapsule:

  primitive: L02_ATTENTION

  transition:
    from_state: null
    operator: null
    to_state_proposal: null

  applicable_invariants: []

  checks: []

  violations: []

  threatened_invariants: []

  budget:
    available: null
    proposed: null
    units: null

  scope: null
  regime: null
  freshness: null

  dependencies: []

  contradictions: []

  gaps: []

  authority:
    required: null
    present: null

  evidence: []

  provenance: []

  disposition:
    enum:
      - PASS
      - BLOCK
      - QUARANTINE
      - REPAIR
      - ESCALATE
      - UNKNOWN_GAP

  confidence_ceiling: 0
```

---

# 23. Evidence / Provenance Requirements

A validated invariant claim requires more than documentation.

Evidence classes should remain distinguishable:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN
```

Examples:

```text
README says invariant exists
→ SOURCE_CLAIM

code contains check
→ OBSERVATION of implementation structure

test executes check and rejects violation
→ runtime evidence

formal proof establishes bounded property
→ formal evidence within stated assumptions
```

These must not be collapsed.

---

# 24. Uncertainty and Confidence Ceiling

Current uncertainty profile:

```yaml
uncertainty:

  evidence:
    level: HIGH
    reason: direct canonical L02 invariant registry not established

  model:
    level: MEDIUM
    reason: invariant structure follows AMOS governance but remains architectural

  scope:
    level: MEDIUM
    reason: exact primitive boundary requires direct canon/runtime confirmation

  temporal:
    level: LOW_MEDIUM
    reason: specification must track AMOS lineage changes

  causal:
    level: MEDIUM
    reason: attention relevance must not be confused with causal relevance

  execution:
    level: HIGH
    reason: executable enforcement has not been demonstrated here

  provenance_independence:
    level: MEDIUM
    reason: overlapping AMOS artifacts may share common ancestry
```

Confidence rule:

```text
confidence in SOURCE-SUPPORTED primitive semantics
>
confidence in canonical invariant registry
>
confidence in runtime enforcement
```

Runtime enforcement confidence remains near zero until executable evidence is produced.

---

# 25. Failure Modes

## FM-INV-001 — Invariant Omission

A required invariant is absent from the transition gate.

## FM-INV-002 — Decorative Invariant

The invariant exists in documentation but is not enforced.

## FM-INV-003 — Fail-Open Unknown

```text
UNKNOWN
→ PASS
```

## FM-INV-004 — Budget Overrun

Allocation exceeds typed available budget.

## FM-INV-005 — Unit Collapse

Different resource units are merged without conversion semantics.

## FM-INV-006 — Epistemic Promotion by Attention

Attention causes unsupported confidence or claim-class promotion.

## FM-INV-007 — Salience Capture

High-salience material crowds out load-bearing evidence.

## FM-INV-008 — Provenance Loss

Source ancestry disappears during ranking or compression.

## FM-INV-009 — Scope Leakage

Local evidence is generalized beyond its envelope.

## FM-INV-010 — Regime Leakage

Evidence from one regime is reused in another without validation.

## FM-INV-011 — Contradiction Suppression

Conflicting evidence is dropped because it complicates prioritization.

## FM-INV-012 — Authority Leakage

Attention priority becomes implicit permission.

## FM-INV-013 — H/M/L Collapse

Cross-scale states become indistinguishable.

## FM-INV-014 — Global Invalidation

A local failure destroys unrelated valid work.

## FM-INV-015 — Premature Stop

The system terminates attention while a critical unresolved gap remains.

---

# 26. Repair / Recovery

Repair must target the smallest violated dependency closure.

```text
detect invariant violation
↓
identify earliest invalid state/edge
↓
block dependent transition
↓
preserve unaffected state
↓
restore violated invariant
↓
revalidate descendants
↓
resume only from nearest valid state
```

Examples:

### Budget violation

```text
rollback allocation
→ recompute available budget
→ reprioritize candidates
```

### Provenance loss

```text
quarantine affected candidate
→ reconstruct ancestry
→ recompute independence/confidence
```

### Scope leakage

```text
restore original scope
→ invalidate unsupported generalized conclusions
→ re-evaluate downstream allocations
```

### Authority leakage

```text
cancel proposed effect
→ restore proposal state
→ obtain valid authority witness
→ revalidate at commit boundary
```

### Contradiction suppression

```text
restore contradictory evidence
→ reopen COMPETING state
→ seek cheapest discriminating evidence
```

---

# 27. Tests / Validators

Minimum validator registry:

```text
VALIDATE_ATTENTION_IDENTITY
VALIDATE_FINITE_BUDGET
VALIDATE_ALLOCATION_CONSERVATION
VALIDATE_RESOURCE_UNITS
VALIDATE_PRIORITY_CONTEXT
VALIDATE_SALIENCE_SEPARATION
VALIDATE_CLAIM_CLASS_NON_PROMOTION
VALIDATE_CONFIDENCE_CEILING
VALIDATE_PROVENANCE_PRESERVATION
VALIDATE_PROVENANCE_INDEPENDENCE
VALIDATE_SCOPE_PRESERVATION
VALIDATE_REGIME_PRESERVATION
VALIDATE_FRESHNESS
VALIDATE_DEPENDENCY_CLOSURE
VALIDATE_SELECTIVE_INVALIDATION
VALIDATE_CONTRADICTION_VISIBILITY
VALIDATE_GAP_VISIBILITY
VALIDATE_AUTHORITY_SEPARATION
VALIDATE_HML_SEPARATION
VALIDATE_FAIL_CLOSED
VALIDATE_STOP_SUFFICIENCY
```

---

# 28. Minimum Test Cases

```text
TEST-L02-INV-001
Allocate attention to a false hypothesis.
Expected:
attention allowed;
claim class unchanged.

TEST-L02-INV-002
Allocate beyond available budget.
Expected:
BLOCK.

TEST-L02-INV-003
Combine tokens and tool calls as one scalar without conversion.
Expected:
TYPE FAILURE.

TEST-L02-INV-004
Repeat the same source through three summaries.
Expected:
one ancestry family;
no false independent confirmation.

TEST-L02-INV-005
Give a highly salient but irrelevant candidate high surface prominence.
Expected:
salience alone cannot force highest priority.

TEST-L02-INV-006
Remove provenance from a load-bearing candidate.
Expected:
QUARANTINE / DOWNGRADE / GAP.

TEST-L02-INV-007
Apply evidence outside its original scope.
Expected:
scope violation.

TEST-L02-INV-008
Move from historical regime to live regime without revalidation.
Expected:
revalidation required when decision-relevant.

TEST-L02-INV-009
Suppress contradictory evidence during compression.
Expected:
invariant failure.

TEST-L02-INV-010
Set HIGH_PRIORITY and attempt external commit.
Expected:
authority gate remains required.

TEST-L02-INV-011
Invalidate one independent local branch.
Expected:
only descendants invalidated.

TEST-L02-INV-012
Exhaust attention budget with critical gap unresolved.
Expected:
BUDGET_EXHAUSTED / UNKNOWN;
not PASS.

TEST-L02-INV-013
Aggregate multiple dependent L observations to H.
Expected:
no confidence inflation.

TEST-L02-INV-014
Attempt H-level expectation → fabricated L observation.
Expected:
invariant failure.

TEST-L02-INV-015
All required invariant checks pass.
Expected:
attention transition may proceed,
but no external authority is implied.
```

---

# 29. Falsifiers

This specification must be revised if source/runtime evidence establishes that:

```text
L02 is not an allocation primitive

attention resources are canonically unbounded

L02 canon explicitly equates attention with truth/confidence

resource conservation is intentionally absent

priority is canonically context-independent

provenance is explicitly outside the L02 contract

H/M/L does not apply to L02

authority is canonically owned by L02

a different canonical invariant registry supersedes this model
```

Runtime enforcement claims are falsified by a reproducible execution in which a documented hard invariant is violated and the transition still commits without authorized exception semantics.

---

# 30. Gap Matrix

```yaml
gap_status:

  primitive_identity:
    status: SOURCE_SUPPORTED

  allocation_semantics:
    status: SOURCE_SUPPORTED

  resource_scarcity:
    status: SOURCE_SUPPORTED

  invariant_need:
    status: DERIVED_FROM_AMOS_GOVERNANCE

  invariant_registry:
    status: MODEL_DEFINED

  invariant_ids:
    status: MODEL_DEFINED

  budget_equations:
    status: MODEL_DEFINED

  epistemic_invariants:
    status: MODEL_DEFINED

  provenance_invariants:
    status: MODEL_DEFINED

  scope_regime_invariants:
    status: MODEL_DEFINED

  HML_invariants:
    status: MODEL_DEFINED

  authority_invariants:
    status: MODEL_DEFINED

  canonical_L02_invariant_registry:
    status: UNKNOWN/GAP

  canonical_thresholds:
    status: UNKNOWN/GAP

  executable_enforcement:
    status: UNKNOWN/GAP

  executed_tests:
    status: UNKNOWN/GAP

  formal_verification:
    status: UNKNOWN/GAP
```

Critical gaps:

```text
1. direct canonical L02 invariant registry
2. executable enforcement evidence
3. executed negative tests
4. canonical resource units and thresholds
```

---

# 31. RSCF Completion State

```yaml
rscf:

  id: L02_ATTENTION_INVARIANTS

  claim:
    L02_ATTENTION requires invariant-preserving allocation of scarce
    reasoning/observation resources such that attention does not silently
    alter truth status, evidence class, confidence, provenance, scope,
    regime, authority, or commit eligibility.

  claim_class: MODEL

  evidence:
    - source-supported L02 attention-allocation semantics
    - source-supported resource-scarcity semantics
    - AMOS governance and epistemic boundaries

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    subsystem: COGNITIVE_MATRIX
    primitive: L02_ATTENTION
    artifact: INVARIANTS.md
    derivation: SOURCE_BOUNDED_AMOS_MODEL

  scope:
    system: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    primitive: L02_ATTENTION
    concern: invariant_preservation

  regime:
    governed cognitive architecture specification

  freshness:
    revalidate_when:
      - direct L02 canon is recovered
      - L02 runtime is implemented
      - AMOS_CORE invariant semantics change
      - resource semantics change
      - control-plane interfaces change

  dependencies:
    - L01_SENSING_OBSERVATION
    - L02_ATTENTION_DEFINITION
    - L02_ATTENTION_VARIABLES
    - L02_ATTENTION_STATE
    - L02_ATTENTION_OPERATORS
    - L02_ATTENTION_DEPENDENCIES
    - L02_ATTENTION_EQUATIONS
    - L02_ATTENTION_HML
    - L02_ATTENTION_CONTROL_PLANES
    - L02_ATTENTION_PROVENANCE

  competing:
    - invariants belong directly to L02
    - some invariants belong only to infrastructure control plane
    - L02 requires a smaller canonical invariant set
    - L02 uses dynamically scoped invariants
    - HML invariants are external overlays rather than primitive invariants

  falsifiers:
    - direct canon establishes incompatible invariant semantics
    - runtime intentionally implements different validated semantics
    - source evidence assigns relevant constraints outside L02
    - executable tests demonstrate invariant non-enforcement

  uncertainty:
    evidence: HIGH
    model: MEDIUM
    scope: MEDIUM
    temporal: LOW_MEDIUM
    causal: MEDIUM
    execution: HIGH
    provenance_independence: MEDIUM

  confidence_ceiling:
    source-supported confidence applies to attention allocation and
    resource scarcity only; the detailed invariant registry remains
    MODEL until direct canon or executable validation establishes it

  gap_status:
    canonical_invariants: CRITICAL_GAP
    runtime_enforcement: CRITICAL_GAP
    executed_validation: CRITICAL_GAP

  cheapest_discriminating_test:
    locate direct canonical L02 invariant material and compare each
    proposed invariant family against source text, then execute negative
    transition tests against any identified runtime
```

---

# 32. Completion State

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
    status: REFERENCED / CROSS_ARTIFACT

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
    status: MODEL_COMPLETE / SOURCE_PARTIAL

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
    status: EXPLICIT / CRITICAL_GAPS_OPEN

  overall:
    status: COMPLETE_FOR_MODEL_SPECIFICATION_SCOPE

  conclusion_class:
    MODEL
```

---

# 33. Hard Boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

L02-specific extensions:

```text
ATTENTION != TRUTH

ATTENTION != EVIDENCE

ATTENTION != CONFIDENCE

ATTENTION != CAUSATION

SALIENCE != TRUTH

SALIENCE != PRIORITY

NOVELTY != IMPORTANCE

REPETITION != INDEPENDENT CONFIRMATION

PRIORITY != AUTHORITY

RESOURCE != AUTHORITY

BUDGET EXHAUSTION != COMPLETION

DOCUMENTED INVARIANT != ENFORCED INVARIANT

TEST DEFINITION != EXECUTED TEST

LOCAL PASS != GLOBAL PASS

MODEL INVARIANT != CANONICAL INVARIANT
```

---

# 34. Governing Invariant Contract

> **`L02_ATTENTION` allocates scarce reasoning and observation resources while preserving the epistemic, provenance, scope, regime, dependency, H/M/L, resource, and authority boundaries of the objects it processes. Attention may change what receives processing capacity; it may not, by allocation alone, change what is true, what counts as evidence, how confident AMOS may be, where evidence applies, whether sources are independent, or what actions are authorized. Any transition whose required invariants cannot be established must fail closed into block, quarantine, repair, escalation, or explicit `UNKNOWN/GAP` rather than silently passing.**

---

# 35. Canon Boundary

```text
SOURCE-SUPPORTED:
L02_ATTENTION concerns attention allocation.
Reasoning/observation resources are scarce.

AMOS-FRAMEWORK-SUPPORTED:
integrity before optimization
typed/scoped/provenance-aware reasoning
confidence ceilings
contradiction preservation
competing hypotheses
selective invalidation
authority separation
scope/regime preservation
H/M/L reasoning

AMOS_MODEL:
L02 invariant registry
invariant IDs
resource equations
priority invariants
epistemic invariants
provenance invariants
scope/regime invariants
dependency invariants
H/M/L invariants
transition invariants
validator registry
repair protocol

UNKNOWN/GAP:
direct canonical L02 invariant registry
canonical invariant numbering
canonical resource units
canonical thresholds
runtime implementation
runtime enforcement
executed negative tests
formal verification
```

Therefore:

```text
CONCLUSION CLASS:
MODEL

NOT:
VERIFIED L02 CANON

NOT:
PROOF OF IMPLEMENTATION

NOT:
PROOF OF ENFORCEMENT

NOT:
AUTHORITY TO COMMIT
```

```text
```

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: l02_attention_primitives_cognitive_matrix_invariants
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L02_ATTENTION/L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_INVARIANTS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
