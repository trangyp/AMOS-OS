---
type: cognitive
tags: [amos]
  - cognitive-matrix
  - l02
  - attention
  - hml
  - rscf
  - governance

title: "L02_ATTENTION — HML"
origin_architect: "Trang Phan"
status: "MODEL_SPECIFICATION / SOURCE-BOUNDED / UNVALIDATED"
epistemic_class: "MODEL"
runtime_alignment: "AMOS Full Brain OS / AMOS_CORE v4.4 lineage"
---


# L02_ATTENTION — HML

**Class:** `COGNITIVE_PRIMITIVE_HML_CONTRACT`  
**Origin architect / steward:** Trang Phan  
**Primitive:** `L02_ATTENTION`  
**Artifact:** `HML.md`  
**Status:** `AMOS_MODEL / SOURCE-BOUNDED / UNVALIDATED`

> **Canon boundary:** available L02 material supports attention as allocation of scarce reasoning/observation resources. The detailed H/M/L decomposition below is an AMOS architectural model unless a direct L02 canon reference independently establishes the same mapping.

---

# 0. Purpose

Define the hierarchical/multiscale contract by which `L02_ATTENTION` operates across AMOS H/M/L reasoning levels without collapsing system-level priorities, subsystem allocation, and local attention events into one undifferentiated state.

The intended decomposition is:

```text
H — governing attention context
M — attention allocation subsystem
L — concrete attention target/event
```

Core rule:

```text
H != M != L

but

H ↔ M ↔ L
```

Cross-level influence is permitted only through typed, provenance-preserving transformations.

---

# 1. Source / Canon References

## 1.1 Source-supported L02 semantic core

Recovered primitive meaning:

```text
L02_ATTENTION
=
attention allocation;
budget scarce reasoning/observation resources
```

This directly supports:

* attention as an allocation function,
* scarcity of reasoning/observation resources,
* the need to determine what receives processing resources.

It does **not** independently establish the exact H/M/L decomposition in this artifact.

## 1.2 AMOS H/M/L framework lineage

Relevant AMOS framework concepts include:

```text
recursive RSCF / H-M-L decomposition
smallest sufficient proof scope
dependency-aware escalation
cross-scale reasoning
selective invalidation
confidence ceilings
scope/regime preservation
```

Framework constraint:

```text
local evidence
!=
automatic system-level truth
```

and:

```text
system-level objective
!=
automatic local evidence
```

## 1.3 Related artifacts

```text
L02_ATTENTION — README
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
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README

L01_SENSING_OBSERVATION
```

---

# 2. Definition and Scope

For L02, H/M/L represents three distinct resolutions of attention state.

[
A =
{A_H,A_M,A_L}
]

where:

* (A_H) = governing/system-level attention state,
* (A_M) = subsystem/task-level attention allocation,
* (A_L) = local candidate/event-level attention decision.

This is a **typed architectural decomposition**, not a claim that biological or artificial cognition universally contains exactly three attention levels.

Scope:

```yaml
scope:
  system: AMOS_OS
  subsystem: COGNITIVE_MATRIX
  primitive: L02_ATTENTION
  concern:
    - attention_resolution
    - allocation
    - cross_level_constraint
    - escalation
    - aggregation
    - provenance
    - confidence
```

---

# 3. H Level — Governing Attention Context

## 3.1 Definition

`H` represents the highest active reasoning scope governing which domains, objectives, risks, dependencies, and unresolved uncertainties deserve attention.

H does not normally select individual observations directly.

It constrains the attention environment in which M operates.

Conceptually:

[
H_t =
f(
Objective_t,
Constraints_t,
Risk_t,
Uncertainty_t,
Dependencies_t,
Resources_t
)
]

`f` is `AMOS_MODEL`, not a canonically validated empirical equation.

## 3.2 H concerns

```text
governing objective
scope
stakes
irreversibility
critical dependencies
critical gaps
global constraints
risk
resource envelope
regime
freshness requirements
proof sufficiency
authority boundaries
```

## 3.3 H question

```text
What deserves reasoning capacity at the governing scope?
```

## 3.4 Example

If AMOS is evaluating a consequential deployment:

```text
H:
objective = determine deployment safety

attention priority:
  safety invariants
  unresolved critical gaps
  authority
  irreversible consequences

low priority:
  cosmetic formatting
```

---

# 4. M Level — Attention Allocation Subsystem

## 4.1 Definition

`M` converts H-level governing requirements into bounded allocations among competing tasks, evidence paths, hypotheses, modules, agents, or workflows.

Conceptually:

[
M_t =
Allocate(
Candidates_t,
Budget_t,
H_t
)
]

M is where competition for scarce attention is explicitly resolved.

## 4.2 M concerns

```text
candidate generation
candidate ranking
attention budget
task priority
branch allocation
evidence retrieval priority
agent/skill routing
uncertainty reduction
dependency resolution
escalation
de-escalation
stopping
```

## 4.3 M question

```text
Given the governing objective and finite resources,
which reasoning path should receive how much attention?
```

## 4.4 Example

```text
H:
verify deployment safety

M candidates:
  inspect provenance
  inspect authority
  inspect runtime tests
  inspect cosmetic documentation

M allocation:
  provenance = HIGH
  authority = HIGH
  runtime tests = HIGH
  cosmetic documentation = LOW
```

---

# 5. L Level — Concrete Attention Event

## 5.1 Definition

`L` represents a specific attention-bearing candidate, observation, claim, evidence item, dependency, contradiction, test, or action proposal.

Conceptually:

[
L_i =
Candidate(
content_i,
source_i,
scope_i,
salience_i,
uncertainty_i,
cost_i
)
]

An L-level candidate may be admitted, deferred, suppressed, escalated, revisited, or rejected.

## 5.2 L concerns

```text
specific observation
specific claim
specific contradiction
specific source
specific evidence item
specific variable
specific test
specific tool result
specific dependency
specific gap
specific action proposal
```

## 5.3 L question

```text
Should this specific item receive attention now,
and if so, how much?
```

---

# 6. Typed H/M/L State

```yaml
AttentionHMLState:

  H:
    objective:
      type: ObjectiveState

    scope:
      type: ScopeEnvelope

    regime:
      type: RegimeRef

    constraints:
      type: ConstraintSet

    risk:
      type: RiskState

    uncertainty:
      type: UncertaintyVector

    resource_envelope:
      type: ResourceBudget

    authority:
      type: AuthorityEnvelope

  M:
    candidates:
      type: AttentionCandidate[]

    allocation:
      type: AttentionAllocation[]

    active_branches:
      type: BranchRef[]

    resource_state:
      type: ResourceState

    dependency_frontier:
      type: DependencyRef[]

    escalation_state:
      type: EscalationState

  L:
    candidate_id:
      type: CandidateId

    content_ref:
      type: EvidenceOrTaskRef

    source:
      type: SourceRef

    provenance:
      type: ProvenanceRef

    scope:
      type: ScopeEnvelope

    regime:
      type: RegimeRef

    priority:
      type: PriorityScore

    confidence:
      type: ConfidenceBound

    cost:
      type: ResourceCost

    disposition:
      type:
        - ATTEND
        - DEFER
        - ESCALATE
        - QUARANTINE
        - REJECT
        - COMPLETE
```

---

# 7. Typed Inputs

```yaml
HMLAttentionInput:

  observations:
    type: Observation[]

  objective:
    type: ObjectiveState

  constraints:
    type: ConstraintSet

  candidate_tasks:
    type: AttentionCandidate[]

  dependencies:
    type: DependencyGraph

  uncertainty:
    type: UncertaintyVector

  provenance:
    type: ProvenanceBundle

  risk:
    type: RiskState

  resource_budget:
    type: ResourceBudget

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef

  freshness:
    type: FreshnessState

  authority:
    type: AuthorityEnvelope
```

---

# 8. Typed Outputs

```yaml
HMLAttentionOutput:

  H_state:
    type: HAttentionState

  M_state:
    type: MAttentionState

  L_allocations:
    type: LAttentionDecision[]

  escalation_requests:
    type: EscalationRequest[]

  deferred_items:
    type: CandidateRef[]

  quarantined_items:
    type: CandidateRef[]

  completed_items:
    type: CandidateRef[]

  unresolved_gaps:
    type: GapRef[]

  provenance:
    type: ProvenanceBundle

  confidence_ceiling:
    type: ConfidenceBound
```

---

# 9. State Variables

```text
H_t        governing attention state
M_t        subsystem allocation state
L_t        local attention state

B_H        H-level resource envelope
B_M        M-level allocation budget
b_i        local candidate allocation

P_H        governing priority field
P_M        subsystem priority vector
p_i        local candidate priority

U_H        governing uncertainty
U_M        subsystem uncertainty
u_i        local uncertainty

R_H        governing risk
R_M        subsystem risk
r_i        local risk

D_H        governing dependency set
D_M        active dependency frontier
d_i        local dependencies

C_H        governing confidence ceiling
C_M        subsystem confidence ceiling
c_i        local confidence
```

---

# 10. Budget Relation

A minimal conservation constraint is:

[
\sum_i b_i \le B_M
]

and:

[
B_M \le B_H
]

where budget may represent:

```text
tokens
time
tool calls
retrieval operations
agent calls
human-review capacity
compute
working-context capacity
```

The units must not be silently mixed.

Therefore:

```text
token budget + seconds + tool calls
```

cannot be numerically summed without an explicit conversion model.

---

# 11. H→M Operator

```text
PROJECT_H_TO_M(H_t)
```

Purpose:

Translate governing objectives and constraints into subsystem priorities.

Conceptually:

[
M^{prior}*t =
\Pi*{H\rightarrow M}(H_t)
]

Required preservation:

```text
objective
hard constraints
critical gaps
scope
regime
authority restrictions
risk requirements
```

H→M projection may compress information but may not erase load-bearing constraints.

---

# 12. M→L Operator

```text
ALLOCATE_M_TO_L(M_t, L_1...L_n)
```

Conceptually:

[
b_i =
Allocate(L_i\mid M_t)
]

Candidate allocation may depend on:

```text
goal relevance
dependency criticality
risk
uncertainty
novelty
freshness
contradiction
cost
expected information gain
irreversibility
```

No single canonical weighting formula is established here.

---

# 13. L→M Operator

```text
AGGREGATE_L_TO_M()
```

Local results update subsystem state.

[
M_{t+1}
=======

Update_M(M_t,\Delta L)
]

Examples:

```text
new contradiction
test failure
source confirmation
dependency resolution
gap closure
runtime failure
unexpected evidence
```

Important:

```text
L result
!=
automatic M conclusion
```

Aggregation must respect applicability and provenance.

---

# 14. M→H Operator

```text
ESCALATE_M_TO_H()
```

M-level evidence should reach H when it can materially alter the governing objective or decision.

Candidate triggers:

```text
critical invariant failure
authority failure
critical gap
regime change
scope invalidation
high-impact contradiction
irreversible-risk discovery
resource exhaustion
dependency collapse
confidence collapse
```

Conceptually:

[
Escalate(M\rightarrow H)
========================

1
]

when an M-state change is decision-relevant at H.

---

# 15. Cross-Level Attention Cycle

```text
H objective / constraints
        ↓
PROJECT
        ↓
M candidate allocation
        ↓
ALLOCATE
        ↓
L attention events
        ↓
OBSERVE / TEST / REASON
        ↓
L results
        ↓
AGGREGATE
        ↓
M updated state
        ↓
ESCALATE if governing consequence
        ↓
H updated state
```

This may repeat until sufficiency or termination criteria are met.

---

# 16. Invariants

```text
L02-HML-INV-001
H, M, and L remain typed and distinguishable.

L02-HML-INV-002
H-level objectives constrain M allocation.

L02-HML-INV-003
M allocation cannot silently override H hard constraints.

L02-HML-INV-004
L evidence cannot automatically become H truth.

L02-HML-INV-005
H intent cannot manufacture L evidence.

L02-HML-INV-006
Cross-level transformations retain provenance.

L02-HML-INV-007
Scope must survive H↔M↔L translation.

L02-HML-INV-008
Regime must survive cross-level translation.

L02-HML-INV-009
Confidence cannot increase merely because information is aggregated upward.

L02-HML-INV-010
Critical contradictions must not be compressed away.

L02-HML-INV-011
Hard constraints are non-compensatory across levels.

L02-HML-INV-012
Budget allocation cannot exceed the governing resource envelope.

L02-HML-INV-013
Local completion does not imply subsystem completion.

L02-HML-INV-014
Subsystem completion does not imply governing-objective completion.

L02-HML-INV-015
Global uncertainty does not require exhaustive processing of every local item.

L02-HML-INV-016
Only decision-relevant local dependencies need escalation.

L02-HML-INV-017
Invalidation propagates only through actual dependency edges.

L02-HML-INV-018
UNKNOWN/GAP remains visible through aggregation.

L02-HML-INV-019
Attention priority does not establish truth.

L02-HML-INV-020
Salience does not establish evidential importance.
```

---

# 17. Dependency Structure

Primary upstream dependency:

```text
L01_SENSING_OBSERVATION
```

provides candidate observations.

L02 H/M/L then determines which observations or reasoning objects receive scarce processing capacity.

Conceptual flow:

```text
L01
SENSE / OBSERVE
      ↓
candidate observation field
      ↓
L02-H
governing relevance constraints
      ↓
L02-M
allocation / prioritization
      ↓
L02-L
specific attention event
```

Potential downstream primitives must be established from canon before being asserted as canonical dependencies.

---

# 18. H/M/L Applicability Matrix

| Concern             |                  H |                 M |                  L |
| ------------------- | -----------------: | ----------------: | -----------------: |
| Governing objective |            Primary |         Inherited |       Context only |
| Attention budget    |           Envelope |        Allocation |        Consumption |
| Priority            |          Governing |            Ranked | Candidate-specific |
| Scope               |          Governing |         Preserved |           Attached |
| Regime              |          Governing |         Preserved |           Attached |
| Risk                |             System |         Subsystem |              Event |
| Uncertainty         |          Aggregate | Decision-relevant |  Evidence-specific |
| Provenance          |             Policy |       Composition |    Source-specific |
| Dependencies        |    Global critical |   Active frontier |          Immediate |
| Constraints         |          Governing |          Enforced |            Checked |
| Evidence            |        Sufficiency |       Composition |        Direct item |
| Contradictions      | Global consequence |    Reconciliation |          Detection |
| Authority           |           Boundary |       Enforcement |    Action-specific |
| Validation          |       System claim |          Workflow |    Specific result |
| Repair              |           Strategy |      Coordination |   Local correction |

---

# 19. Attention Priority Across H/M/L

A generic, non-canonical prioritization model may be represented as:

[
Priority_i =
F(
Goal_i,
Dependency_i,
Risk_i,
Uncertainty_i,
Freshness_i,
Contradiction_i,
InformationGain_i,
Cost_i
)
]

This is intentionally function-valued rather than assigning unsupported canonical weights.

Constraint:

[
Priority_i
\not\Rightarrow
Truth_i
]

Attention answers:

```text
what to inspect
```

not:

```text
what is true
```

---

# 20. Adaptive Complexity Mapping

L02 may map AMOS adaptive complexity onto H/M/L attention:

```yaml
C0:
  H: minimal
  M: minimal
  L: direct target

C1:
  H: compact objective
  M: small candidate set
  L: bounded reasoning

C2:
  H: explicit constraints
  M: structured allocation
  L: dependency-aware analysis

C3:
  H: consequential objective
  M: competing branches
  L: deeper evidence traversal

C4:
  H: maximum governance
  M: multi-branch / adversarial allocation
  L: raw evidence where required
```

Escalation should occur because decision-changing uncertainty warrants it, not merely because more analysis is possible.

---

# 21. Control-Plane Requirements

The control plane must own or validate:

```text
objective identity
scope
regime
hard constraints
resource envelope
authority
freshness
provenance
dependency state
commit eligibility
```

L02 may propose allocation.

It must not infer durable authority from attention priority.

```text
ATTEND(x)
!=
AUTHORIZE(x)
```

and:

```text
HIGH_PRIORITY(x)
!=
COMMIT(x)
```

Commit-time authority remains a control-plane concern.

---

# 22. Agents

Candidate logical roles:

```text
L02_H_ATTENTION_GOVERNOR
L02_M_ALLOCATION_COORDINATOR
L02_L_ATTENTION_WORKER
L02_ESCALATION_AUDITOR
L02_BUDGET_AUDITOR
L02_CROSS_SCALE_PROVENANCE_AUDITOR
```

These are architectural role proposals unless separately implemented and validated.

Role separation:

```text
H governor:
  determines governing attention requirements

M coordinator:
  distributes bounded attention

L worker:
  examines specific candidate

auditor:
  checks cross-level integrity
```

---

# 23. Skills

Potential AMOS capability mappings include:

```text
AMOS Attention Allocation Governor
AMOS Context Budget Governor RSCF
AMOS Constraint Propagation RSCF Engine
AMOS Cross-Scale RSCF Tensor Engine
AMOS Metacognitive Confidence Auditor
AMOS RSCF Modeler
AMOS Infrastructure Control Plane
AMOS Context Continuity Governor
AMOS Provenance Trust Firewall
```

Skill availability does not establish canonical L02 membership.

---

# 24. Workflow

```text
RECEIVE observations from L01
↓
RESOLVE governing objective at H
↓
IDENTIFY hard constraints / risk / gaps
↓
PROJECT H requirements into M
↓
GENERATE candidate attention targets
↓
RANK / ALLOCATE within budget
↓
PROCESS selected L candidates
↓
CAPTURE evidence + provenance
↓
AGGREGATE relevant L results
↓
UPDATE M state
↓
ESCALATE decision-changing changes to H
↓
CHECK claim/action sufficiency
↓
CONTINUE / DE-ESCALATE / STOP
```

---

# 25. Protocol

```yaml
AttentionHMLCapsule:

  primitive:
    value: L02_ATTENTION

  h_state:
    objective: null
    scope: null
    regime: null
    constraints: []
    risk: null
    uncertainty: null
    budget: null
    authority: null

  m_state:
    candidates: []
    allocation: []
    active_dependencies: []
    active_branches: []
    unresolved_conflicts: []

  l_state:
    active_candidate: null
    source: null
    provenance: null
    priority: null
    allocation: null
    result: null

  escalation:
    required: false
    reason: null

  evidence: []

  provenance: []

  confidence_ceiling: 0

  gap_status: UNKNOWN/GAP
```

---

# 26. Evidence / Provenance

Every cross-level transformation should preserve:

```text
source identity
semantic origin
parent state
transformation/operator
scope
regime
freshness
dependencies
confidence
timestamp/epoch where available
```

Conceptually:

[
Prov(L)
\rightarrow
Prov(M)
\rightarrow
Prov(H)
]

must retain ancestry.

Aggregation must not transform several descendants of one source into false independent confirmation.

---

# 27. Provenance Independence

Suppose:

```text
L1 ← Source A
L2 ← Source A
L3 ← Source A
```

Then upward aggregation must not treat:

```text
L1 + L2 + L3
```

as three independent confirmations.

Independence is a provenance property, not a count property.

This applies at all H/M/L transitions.

---

# 28. Confidence Ceiling

For an M-level conclusion derived from L-level premises:

[
Conf(M)
\le
\min_i Conf(L_i)
]

for load-bearing premises unless independently revalidated.

Likewise:

[
Conf(H)
\le
\min_j Conf(M_j)
]

for load-bearing subsystem conclusions.

Aggregation alone cannot increase epistemic confidence.

Independent validation may alter the evidence graph and therefore the ceiling.

---

# 29. Uncertainty Vector

```yaml
uncertainty:

  evidence:
    concern:
      whether attended observations actually support the claim

  model:
    concern:
      whether the H/M/L allocation model is appropriate

  scope:
    concern:
      whether local evidence applies at higher levels

  temporal:
    concern:
      whether attention state or evidence has become stale

  causal:
    concern:
      whether relevance or priority is being mistaken for causal importance

  execution:
    concern:
      whether proposed allocations were actually executed

  provenance_independence:
    concern:
      whether aggregated evidence is genuinely independent
```

---

# 30. Failure Modes

## FM-HML-001 — Level Collapse

```text
H = M = L
```

Different reasoning scales become indistinguishable.

## FM-HML-002 — Upward Overgeneralization

One local observation becomes a global conclusion.

```text
L observation
→ H truth
```

without sufficient aggregation.

## FM-HML-003 — Downward Hallucination

H-level expectation causes unsupported L-level observation.

```text
H expectation
→ invented L evidence
```

## FM-HML-004 — Budget Leakage

Local work consumes resources beyond M/H allocation.

## FM-HML-005 — Priority Inversion

Low-impact local items consume attention while critical dependencies remain unresolved.

## FM-HML-006 — Constraint Loss

H hard constraints disappear during H→M projection.

## FM-HML-007 — Provenance Collapse

Source ancestry disappears during upward aggregation.

## FM-HML-008 — Confidence Inflation

Multiple correlated L items produce unjustified higher H confidence.

## FM-HML-009 — Escalation Failure

A local discovery capable of changing the governing decision remains trapped at L/M.

## FM-HML-010 — Escalation Flood

Every local change is escalated to H, destroying locality and efficiency.

## FM-HML-011 — Scope Leakage

L evidence from one applicability envelope is generalized beyond it.

## FM-HML-012 — Regime Leakage

Evidence from one regime is propagated into another without revalidation.

## FM-HML-013 — Salience Capture

Highly noticeable information consumes resources despite low decision relevance.

## FM-HML-014 — Global Recompute Pathology

Any local change forces unnecessary full H/M/L recomputation.

---

# 31. Repair / Recovery

## Level collapse

```text
retype H/M/L objects
→ restore scale boundaries
→ reconstruct dependency edges
```

## Upward overgeneralization

```text
rollback H claim
→ recover originating L evidence
→ test aggregation sufficiency
→ re-promote only if warranted
```

## Constraint loss

```text
restore H constraint
→ invalidate affected M allocation
→ selectively invalidate dependent L work
→ reroute
```

## Provenance collapse

```text
quarantine aggregate
→ recover source ancestry
→ recompute independence
→ recalculate confidence
```

## Priority inversion

```text
recompute decision relevance
→ restore critical dependency priority
→ defer non-load-bearing items
```

## Escalation failure

```text
identify decision-changing L/M result
→ escalate with provenance
→ recompute H state
```

---

# 32. Selective Invalidation

If local premise (L_k) fails:

[
Invalid(L_k)
\Rightarrow
Invalidate(Descendants(L_k))
]

not:

[
Invalid(L_k)
\Rightarrow
Invalidate(All)
]

If the failed local result supports only one M branch:

```text
invalidate that branch
preserve independent M branches
preserve unaffected H state
```

This is central to scalable H/M/L reasoning.

---

# 33. Escalation Criteria

Escalation from L→M or M→H is appropriate when the new information:

```text
changes a hard constraint
changes a critical dependency
changes the governing decision
changes authority eligibility
changes scope
changes regime
invalidates a load-bearing premise
reveals a critical contradiction
changes irreversibility/risk
exhausts resource assumptions
changes confidence beyond a decision threshold
```

Otherwise local handling is preferred.

---

# 34. De-escalation Criteria

Attention may move downward or terminate when:

```text
critical uncertainty is resolved
remaining gaps are explanatory/cosmetic
additional evidence has low expected decision value
candidate branches become equivalent
proof/action sufficiency is reached
resource cost exceeds expected information value
```

De-escalation must not hide unresolved critical gaps.

---

# 35. Stop Condition

A generic H/M/L stop condition is:

[
Stop =
ClaimSufficient
\land
DecisionSufficient
\land
ActionSufficient
]

where applicable.

For explanation-only tasks:

```text
DecisionSufficient
and ActionSufficient
```

may be `NOT_APPLICABLE`.

Stopping is not equivalent to universal certainty.

---

# 36. Tests / Validators

```text
VALIDATE_HML_TYPES
VALIDATE_HML_SEPARATION
VALIDATE_H_TO_M_PROJECTION
VALIDATE_M_TO_L_ALLOCATION
VALIDATE_L_TO_M_AGGREGATION
VALIDATE_M_TO_H_ESCALATION
VALIDATE_BUDGET_CONSERVATION
VALIDATE_SCOPE_PRESERVATION
VALIDATE_REGIME_PRESERVATION
VALIDATE_PROVENANCE_PRESERVATION
VALIDATE_CONFIDENCE_CEILING
VALIDATE_DEPENDENCY_PROPAGATION
VALIDATE_SELECTIVE_INVALIDATION
VALIDATE_CRITICAL_GAP_VISIBILITY
VALIDATE_AUTHORITY_SEPARATION
VALIDATE_STOP_CONDITION
```

---

# 37. Minimum Tests

```text
TEST-L02-HML-001
H, M, and L states are distinguishable.

TEST-L02-HML-002
H hard constraints survive projection to M.

TEST-L02-HML-003
M cannot allocate more resource than H permits.

TEST-L02-HML-004
Sum of L allocations cannot exceed M budget.

TEST-L02-HML-005
A local observation cannot automatically become a global conclusion.

TEST-L02-HML-006
A governing expectation cannot manufacture local evidence.

TEST-L02-HML-007
Cross-level provenance remains recoverable.

TEST-L02-HML-008
Scope survives H→M→L transformations.

TEST-L02-HML-009
Regime survives H→M→L transformations.

TEST-L02-HML-010
Correlated local evidence does not create false independent confirmation.

TEST-L02-HML-011
Critical local contradictions escalate.

TEST-L02-HML-012
Non-decision-relevant local changes need not escalate.

TEST-L02-HML-013
Local failure invalidates only dependent branches.

TEST-L02-HML-014
UNKNOWN/GAP survives upward aggregation.

TEST-L02-HML-015
Attention priority does not alter claim class by itself.

TEST-L02-HML-016
Stopping cannot occur while unresolved critical gaps block sufficiency.
```

---

# 38. Falsifiers

Revise this contract if direct AMOS canon establishes:

```text
L02 does not use H/M/L decomposition

H/M/L meanings differ materially from this mapping

attention allocation occurs at different canonical scales

canonical equations replace the modeled allocation forms

cross-level operators differ materially

L02 is not downstream of sensing/observation

another control plane exclusively owns the modeled functions
```

Runtime claims are falsified if executable evidence shows that the implemented system does not perform the documented cross-level behavior.

---

# 39. Competing Models

Preserve at least these alternatives:

```text
COMPETING-001:
H/M/L are reasoning-resolution levels.

COMPETING-002:
H/M/L represent domain hierarchy rather than attention resolution.

COMPETING-003:
L02 uses a flat priority system and H/M/L is only an external AMOS overlay.

COMPETING-004:
L02 uses more than three effective attention scales.

COMPETING-005:
attention hierarchy is dynamically generated rather than fixed.

COMPETING-006:
some allocation functions belong to the infrastructure control plane rather than L02.
```

No forced convergence is warranted without discriminating source/runtime evidence.

---

# 40. Gap Status

```yaml
gap_status:

  primitive_identity:
    status: SOURCE_SUPPORTED

  attention_allocation_semantics:
    status: SOURCE_SUPPORTED

  scarcity_semantics:
    status: SOURCE_SUPPORTED

  H_level_definition:
    status: MODEL_DEFINED

  M_level_definition:
    status: MODEL_DEFINED

  L_level_definition:
    status: MODEL_DEFINED

  H_to_M_operator:
    status: MODEL_DEFINED

  M_to_L_operator:
    status: MODEL_DEFINED

  L_to_M_operator:
    status: MODEL_DEFINED

  M_to_H_operator:
    status: MODEL_DEFINED

  canonical_HML_mapping:
    status: UNKNOWN/GAP

  canonical_HML_equations:
    status: UNKNOWN/GAP

  canonical_cross_level_invariants:
    status: UNKNOWN/GAP

  executable_HML_runtime:
    status: UNKNOWN/GAP

  executed_HML_validation:
    status: UNKNOWN/GAP

  L01_to_L02_HML_interface:
    status: PARTIAL / MODEL_DEFINED
```

Critical unresolved question:

```text
Does direct L02 canon explicitly assign H/M/L semantics,
or is this decomposition an AMOS architectural overlay?
```

Until resolved:

```text
H/M/L mapping = MODEL
```

---

# 41. RSCF Completion State

```yaml
rscf:

  id: L02_ATTENTION_HML

  claim:
    L02_ATTENTION can be represented within AMOS as a three-resolution
    attention architecture in which H carries governing attention
    requirements, M allocates finite resources among competing reasoning
    paths, and L represents concrete attention events.

  claim_class: MODEL

  evidence:
    - source-supported L02 attention-allocation primitive
    - source-supported scarcity of reasoning/observation resources
    - AMOS recursive H/M/L reasoning architecture

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    subsystem: COGNITIVE_MATRIX
    primitive: L02_ATTENTION
    artifact: HML.md
    derivation: SOURCE_BOUNDED_AMOS_MODEL

  scope:
    system: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    primitive: L02_ATTENTION
    concern: hierarchical_attention_allocation

  regime:
    governed cognitive architecture specification

  freshness:
    revalidate_when:
      - direct L02 HML canon is recovered
      - AMOS_CORE HML semantics change
      - L02 runtime is identified
      - cross-level tests are executed
      - L01/L02 interface changes

  dependencies:
    - L01_SENSING_OBSERVATION
    - L02_ATTENTION_DEFINITION
    - L02_ATTENTION_VARIABLES
    - L02_ATTENTION_STATE
    - L02_ATTENTION_OPERATORS
    - L02_ATTENTION_INVARIANTS
    - L02_ATTENTION_DEPENDENCIES
    - L02_ATTENTION_EQUATIONS
    - L02_ATTENTION_CONTROL_PLANES
    - L02_ATTENTION_PROVENANCE

  competing:
    - HML as reasoning-resolution hierarchy
    - HML as domain hierarchy
    - flat attention architecture
    - dynamic multi-scale attention hierarchy
    - control-plane-owned allocation

  falsifiers:
    - direct canon defines incompatible H/M/L semantics
    - runtime implements materially different hierarchy
    - source evidence places allocation outside L02
    - AMOS H/M/L framework is not applicable to this primitive

  uncertainty:
    evidence: MEDIUM_HIGH
    model: MEDIUM
    scope: MEDIUM
    temporal: LOW_MEDIUM
    causal: MEDIUM
    execution: HIGH
    provenance_independence: MEDIUM

  confidence_ceiling:
    high confidence applies to the source-supported attention-allocation
    primitive; the specific H/M/L decomposition remains MODEL until
    direct L02 canon or executable evidence validates it

  gap_status:
    canonical_HML_contract: CRITICAL_GAP
    runtime_implementation: CRITICAL_GAP
    executed_validation: CRITICAL_GAP

  cheapest_discriminating_test:
    locate direct L02 canon defining H/M/L or attention hierarchy and
    compare it against the H/M/L decomposition specified here
```

---

# 42. Completion State

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
    status: MODEL_COMPLETE / CANON_UNRESOLVED

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

# 43. Hard Boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

H/M/L-specific boundaries:

```text
H != M != L

ATTENTION != TRUTH

SALIENCE != EVIDENCE

PRIORITY != CONFIDENCE

LOCAL RESULT != GLOBAL CONCLUSION

GLOBAL OBJECTIVE != LOCAL OBSERVATION

AGGREGATION != INDEPENDENT CONFIRMATION

ESCALATION != VALIDATION

ALLOCATION != AUTHORIZATION

RESOURCE AVAILABILITY != AUTHORITY

H COMPLETENESS != L VALIDATION

L VALIDATION != H COMPLETENESS

MODEL HML != CANONICAL HML

DOCUMENTED HML != IMPLEMENTED HML
```

---

# 44. References

```text
PLACEHOLDER

L02_ATTENTION — README
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
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README

L01_SENSING_OBSERVATION

Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
```

---

# 45. Governing H/M/L Contract

> **`L02_ATTENTION` may be represented in AMOS as a provenance-preserving H/M/L allocation hierarchy: H determines governing attention requirements and resource envelopes; M converts those requirements into bounded allocations among competing reasoning paths; L applies attention to concrete observations, claims, evidence, dependencies, tests, or actions. Information may move upward only through scope-, regime-, dependency-, and provenance-aware aggregation, while governing constraints may move downward without manufacturing evidence. Attention priority never establishes truth, confidence, authority, or commit eligibility.**

---

# 46. Canon Boundary

```text
SOURCE-SUPPORTED:
L02_ATTENTION concerns attention allocation.
Reasoning/observation resources are scarce.

AMOS-FRAMEWORK-SUPPORTED:
recursive H/M/L reasoning
dependency-aware escalation
confidence ceilings
selective invalidation
scope/regime preservation
provenance preservation
smallest sufficient proof scope

AMOS_MODEL:
H = governing attention context
M = attention allocation subsystem
L = concrete attention event
H→M projection
M→L allocation
L→M aggregation
M→H escalation
budget equations
cross-level attention cycle
H/M/L applicability matrix
agent roles
protocol schemas
test suite

UNKNOWN/GAP:
direct canonical L02 H/M/L definition
canonical H/M/L variables
canonical cross-level equations
canonical escalation thresholds
canonical budget semantics
canonical runtime implementation
executed H/M/L validation
validated L01→L02 cross-level interface
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
PROOF OF COGNITIVE UNIVERSALITY

NOT:
AUTHORIZATION TO COMMIT
```

```text
```

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: l02_attention_primitives_cognitive_matrix_hml
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L02_ATTENTION/L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_HML.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[L02_ATTENTION_MOC]]
