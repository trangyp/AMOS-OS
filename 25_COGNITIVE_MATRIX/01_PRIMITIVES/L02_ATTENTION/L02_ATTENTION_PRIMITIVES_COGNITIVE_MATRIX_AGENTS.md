---
type: agent
tags: [amos]
  - cognitive-matrix
  - l02
  - attention
  - agents
  - rscf
  - hml
  - provenance
  - control-plane
  - ai

title: "L02_ATTENTION — Agents"
origin_architect: "Trang Phan"
status: "MODEL_SPECIFICATION / UNVALIDATED"
epistemic_class: "MODEL"
runtime_alignment: "AMOS Full Brain OS / AMOS_CORE v4.4 lineage"
---


# L02_ATTENTION — Agents

**Class:** `COGNITIVE_PRIMITIVE_AGENT_CONTRACT`  
**Origin architect / steward:** Trang Phan  
**Architecture:** `AMOS_OS / COGNITIVE_MATRIX`  
**Primitive:** `L02_ATTENTION`  
**Artifact:** `AGENTS.md`  
**Role:** `ATTENTION ALLOCATION / PRIORITIZATION / RESOURCE-BUDGET AGENT CONTRACT`  
**Status:** `AMOS_MODEL / SOURCE-BOUNDED / UNVALIDATED`

> **Source boundary:** the recoverable `L02_ATTENTION` source identifies this primitive as **attention allocation** whose role is to **budget scarce reasoning/observation resources**. The source is explicitly a non-canonical placeholder and prohibits invention of missing canon, equations, thresholds, empirical claims, or implementation status. :contentReference[oaicite:0]{index=0}
>
> Accordingly, the agent architecture below is a source-bounded AMOS reconstruction. Exact canonical agent names, runtime bindings, thresholds, authority assignments, and implementation state remain `UNKNOWN/GAP`.

---

# 0. Executive Definition

`L02_ATTENTION/AGENTS.md` defines the bounded agent roles responsible for proposing, evaluating, coordinating, auditing, and repairing allocation of scarce AMOS attention resources.

The primitive sits conceptually after observation availability:

```text
L00_REALITY_ENVIRONMENT
↓
L01_SENSING_OBSERVATION
↓
OBSERVABLE / RETRIEVED / ACTIVE INFORMATION
↓
L02_ATTENTION
↓
ATTENTION CANDIDATES
↓
PRIORITIZATION
↓
RESOURCE ALLOCATION
↓
FOCUS / MONITOR / DEFER / SUPPRESS / ESCALATE
↓
DOWNSTREAM COGNITION
```

The recovered source supports only the primitive role:

```text
attention allocation;
budget scarce reasoning/observation resources
```



Therefore all specific agent roles in this document are classified as:

```text
AMOS_MODEL
```

until directly source-confirmed or explicitly approved as new specification.

---

# 1. Core Purpose

L02 agents exist to coordinate the allocation of finite cognitive resources across competing information, tasks, risks, uncertainties, dependencies, goals, and time horizons.

The governing function is:

[
\boxed{
AvailableInformation
+
Goals
+
Constraints
+
AttentionBudget
\rightarrow
AttentionAllocationProposal
}
]

not:

[
\boxed{
Salience
\rightarrow
Truth
}
]

Attention determines **what receives processing resources**.

Attention does not establish:

```text
truth
importance in every context
causal status
decision authority
action authority
moral value
canonical status
```

---

# 2. Source / Canon References

## 2.1 Direct Recoverable L02 Source

The recovered L02 placeholder states:

```yaml
title: L02_ATTENTION Placeholder
origin_architect: Trang Phan
status: PROPOSED_SPECIFICATION_UNKNOWN_GAP
epistemic_class: UNKNOWN/GAP
runtime_alignment: AMOS Full Brain OS / AMOS_CORE v4.4 lineage
```

and defines the role:

```text
Primitive: attention allocation;
budget scarce reasoning/observation resources.
```



The source also requires the following before promotion:

```text
Definition and scope
Purpose / non-purpose
State and variables
Operators / kernels
Named invariants
H/M/L applicability
Inputs / outputs / interfaces
Dependencies and provenance
Failure modes
Repair / rollback behavior
Tests / falsifiers
RSCF / GMEF links
Governance / authority boundary
Freshness / regime validity
Supersession / version lineage
```



## 2.2 Relevant AMOS Architecture Families

```text
AMOS_CORE v4.4 lineage
AMOS Full Brain OS
AMOS Cognition
AMOS RSCF
AMOS H/M/L
AMOS provenance topology
AMOS epistemic regimes
AMOS attention allocation governance
AMOS context-budget governance
AMOS uncertainty governance
AMOS consequence governance
AMOS risk constraint governance
AMOS control-plane architecture
L00_REALITY_ENVIRONMENT
L01_SENSING_OBSERVATION
```

## 2.3 Source Status

```yaml
source_status:

  L02_role_attention_allocation:
    status: SOURCE_SUPPORTED

  scarce_reasoning_observation_budget:
    status: SOURCE_SUPPORTED

  exact_agent_registry:
    status: UNKNOWN/GAP

  exact_agent_names:
    status: UNKNOWN/GAP

  exact_agent_authority:
    status: UNKNOWN/GAP

  exact_runtime_bindings:
    status: UNKNOWN/GAP

  exact_attention_equations:
    status: UNKNOWN/GAP

  executable_agents:
    status: UNKNOWN/GAP

  empirical_validation:
    status: UNKNOWN/GAP
```

Therefore:

```text
SOURCE-SUPPORTED ROLE
!=
CANONICAL AGENT REGISTRY

AGENT MODEL
!=
DEPLOYED AGENT

AGENT CAPABILITY
!=
AUTHORITY
```

---

# 3. Definition and Scope

An `L02 Attention Agent` is a bounded cognitive worker or logical role that participates in attention-resource allocation.

An L02 agent may:

```text
identify attention candidates
score decision relevance
identify urgency
identify uncertainty
identify dependency criticality
identify consequence exposure
identify novelty
identify threat/risk signals
propose resource allocation
monitor saturation
detect attention starvation
detect fixation
detect distractor capture
request escalation
propose redistribution
audit allocation
```

It may not independently:

```text
declare observations true
rewrite evidence
grant itself authority
commit external actions
erase competing hypotheses
promote UNKNOWN/GAP to PASS
override hard safety constraints
change canonical architecture
```

---

# 4. Attention Agent Tensor

Candidate agent tensor:

[
\boxed{
T_{Agt}^{L02}
=============

T[
agent_id,
role,
capabilities,
inputs,
outputs,
budget,
priority_domain,
HML,
scope,
regime,
authority,
dependencies,
provenance,
uncertainty,
state
]
}
]

Candidate typed schema:

```yaml
L02AttentionAgent:

  agent_id:
    type: AgentId

  role:
    type: AttentionAgentRole

  capabilities:
    type: CapabilityRef[]

  budget:
    type: ResourceBudget

  priority_domain:
    type: PriorityDomain[]

  hml:
    type: H | M | L | MULTI_SCALE

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef | UNKNOWN

  authority:
    type: AuthorityEnvelope

  dependencies:
    type: DependencyRef[]

  provenance:
    type: ProvenanceBundle

  uncertainty:
    type: UncertaintyVector

  lifecycle_state:
    type:
      - DECLARED
      - AVAILABLE
      - ACTIVE
      - DEGRADED
      - QUARANTINED
      - DISABLED
      - UNKNOWN
```

This is an `AMOS_MODEL` tensor.

---

# 5. Typed Agent Inputs

```yaml
L02AgentInput:

  attention_candidates:
    type: AttentionCandidate[]

  observations:
    type: ObservationRef[]

  active_claims:
    type: ClaimRef[]

  active_goals:
    type: GoalRef[]

  unresolved_gaps:
    type: GapRecord[]

  dependencies:
    type: DependencyGraph | PartialGraph

  current_budget:
    type: AttentionBudget

  time_constraints:
    type: TemporalConstraint[]

  risk_constraints:
    type: RiskConstraint[]

  consequence_context:
    type: ConsequenceEnvelope

  uncertainty:
    type: UncertaintyVector

  hml:
    type: HMLContext

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef

  provenance:
    type: ProvenanceBundle

  authority_context:
    type: AuthorityContext
```

---

# 6. Typed Agent Outputs

```yaml
L02AgentOutput:

  allocation_proposal:
    type: AttentionAllocationProposal

  selected_targets:
    type: AttentionTarget[]

  deferred_targets:
    type: AttentionTarget[]

  monitored_targets:
    type: AttentionTarget[]

  suppressed_targets:
    type: AttentionTarget[]

  escalation_targets:
    type: AttentionTarget[]

  budget_distribution:
    type: BudgetAllocation[]

  rationale_refs:
    type: EvidenceRef[]

  provenance:
    type: ProvenanceBundle

  uncertainty:
    type: UncertaintyVector

  confidence_ceiling:
    type: ConfidenceBound

  validation_state:
    type:
      - UNVALIDATED
      - CONDITIONAL
      - VALIDATED
      - FAILED
      - UNKNOWN

  proposed_effects:
    type: ProposedEffect[]
```

Hard boundary:

```text
allocation_proposal
!=
committed_allocation
```

---

# 7. Attention Candidate Object

Agents operate over candidate targets.

```yaml
AttentionCandidate:

  target_id:
    type: TargetId

  target_type:
    type:
      - OBSERVATION
      - CLAIM
      - GOAL
      - RISK
      - GAP
      - TASK
      - CONFLICT
      - MEMORY
      - TOOL_RESULT
      - EXTERNAL_EVENT
      - UNKNOWN

  salience:
    type: Score | UNKNOWN

  goal_relevance:
    type: Score | UNKNOWN

  uncertainty:
    type: Score | Vector | UNKNOWN

  risk:
    type: Score | UNKNOWN

  consequence:
    type: Score | UNKNOWN

  urgency:
    type: Score | UNKNOWN

  novelty:
    type: Score | UNKNOWN

  dependency_criticality:
    type: Score | UNKNOWN

  reversibility:
    type: Score | UNKNOWN

  information_value:
    type: Score | UNKNOWN

  estimated_cost:
    type: ResourceCost | UNKNOWN

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef

  hml:
    type: H | M | L

  provenance:
    type: ProvenanceBundle
```

---

# 8. Attention Budget

The recovered source explicitly establishes that L02 budgets scarce reasoning/observation resources. 

Candidate budget object:

```yaml
AttentionBudget:

  total:
    type: ResourceUnits

  available:
    type: ResourceUnits

  reserved:
    type: ResourceUnits

  consumed:
    type: ResourceUnits

  emergency_reserve:
    type: ResourceUnits

  dimensions:
    - reasoning_tokens
    - observation_calls
    - retrieval_calls
    - validation_calls
    - execution_time
    - tool_calls
    - human_attention
```

Not all environments expose all dimensions.

Unavailable dimensions remain:

```text
UNKNOWN/GAP
```

---

# 9. Candidate Agent Registry

The following are **architectural roles**, not claims of canonical or deployed agents.

```text
L02.A01_ATTENTION_ROUTER
L02.A02_PRIORITY_ASSESSOR
L02.A03_BUDGET_ALLOCATOR
L02.A04_SALIENCE_MONITOR
L02.A05_GOAL_RELEVANCE_AGENT
L02.A06_RISK_ATTENTION_AGENT
L02.A07_UNCERTAINTY_ATTENTION_AGENT
L02.A08_DEPENDENCY_CRITICALITY_AGENT
L02.A09_TEMPORAL_URGENCY_AGENT
L02.A10_NOVELTY_MONITOR
L02.A11_CONFLICT_MONITOR
L02.A12_ATTENTION_BALANCER
L02.A13_ATTENTION_DRIFT_MONITOR
L02.A14_FIXATION_DETECTOR
L02.A15_STARVATION_DETECTOR
L02.A16_DISTRACTOR_FILTER
L02.A17_CROSS_SCALE_ATTENTION_AGENT
L02.A18_ATTENTION_REPAIR_AGENT
L02.A19_ATTENTION_AUDITOR
L02.A20_CONTROL_PLANE_INTERFACE_AGENT
```

---

# 10. A01 — Attention Router

**Role:** determine which attention subsystem should inspect a candidate.

```yaml
agent:
  id: L02.A01_ATTENTION_ROUTER

  inputs:
    - AttentionCandidate[]
    - HMLContext
    - ScopeEnvelope
    - RegimeRef

  outputs:
    - RoutingProposal[]

  capabilities:
    - classify candidate
    - route to specialist attention agent
    - preserve candidate provenance

  prohibited:
    - final priority commitment
    - evidence modification
    - authority escalation
```

Hard invariant:

[
Route(x)
\neq
Prioritize(x)
]

Routing does not itself mean high priority.

---

# 11. A02 — Priority Assessor

**Role:** estimate relative priority among attention candidates.

Candidate priority dimensions:

```text
goal relevance
consequence
risk
urgency
uncertainty
dependency criticality
novelty
information value
reversibility
resource cost
```

Candidate structural model:

[
P(x)
====

f(
G_x,
C_x,
R_x,
T_x,
U_x,
D_x,
N_x,
I_x,
V_x,
Cost_x
)
]

This is an `AMOS_MODEL`.

No canonical weighting is asserted here.

---

# 12. A03 — Budget Allocator

**Role:** propose distribution of scarce attention resources.

Candidate constraint:

[
\boxed{
\sum_i b_i
\le
B_{available}
}
]

where:

* (b_i) = attention assigned to target (i),
* (B_{available}) = available budget.

Candidate output states:

```text
FOCUS
MONITOR
DEFER
SUPPRESS
ESCALATE
```

Hard constraints are non-compensatory.

A high score on one criterion cannot automatically override a hard invariant.

---

# 13. A04 — Salience Monitor

**Role:** detect events or objects that stand out strongly in the active information field.

Salience may arise from:

```text
intensity
novelty
change
frequency
contrast
threat
goal relevance
social signal
prediction error
```

Hard boundary:

[
\boxed{
Salience
\neq
Truth
}
]

and:

[
\boxed{
Salience
\neq
Importance
}
]

A highly salient distractor may deserve less attention than a quiet but load-bearing dependency.

---

# 14. A05 — Goal Relevance Agent

**Role:** assess candidate relevance to the currently authorized objective.

Candidate relation:

[
GR(x,g)
=======

Relevance(x,g)
]

The agent must use the active authoritative goal.

It must not substitute:

```text
latest tool result
salient recent message
agent preference
historical objective
```

for the active authorized objective.

---

# 15. A06 — Risk Attention Agent

**Role:** identify candidates whose potential harm or irreversibility justifies increased scrutiny.

Candidate inputs:

```text
risk severity
probability
uncertainty
irreversibility
blast radius
legal exposure
financial exposure
health/safety exposure
institutional consequence
```

Candidate rule:

```text
HIGH CONSEQUENCE
+
HIGH UNCERTAINTY
→
ATTENTION ESCALATION CANDIDATE
```

not automatic action.

---

# 16. A07 — Uncertainty Attention Agent

**Role:** identify uncertainty that could materially change the outcome.

Attention should focus on:

```text
decision-changing uncertainty
load-bearing unknowns
scope uncertainty
regime uncertainty
causal uncertainty
freshness uncertainty
execution uncertainty
provenance-independence uncertainty
```

Low-value background uncertainty should not consume scarce budget merely because it exists.

---

# 17. A08 — Dependency Criticality Agent

**Role:** identify premises or nodes with large downstream dependency effects.

Candidate metric:

[
DC(x)
=====

Impact(x)
\times
FanOut(x)
\times
LoadBearing(x)
]

This is an `AMOS_MODEL`.

A quiet premise with high fan-out may deserve more attention than a dramatic but isolated observation.

---

# 18. A09 — Temporal Urgency Agent

**Role:** detect time-sensitive attention requirements.

Candidate signals:

```text
deadline proximity
freshness expiry
revalidation window
authority expiry
market/event timing
repair window
recovery window
irreversibility threshold
```

Urgency does not imply truth.

[
\boxed{
Urgent
\neq
Correct
}
]

---

# 19. A10 — Novelty Monitor

**Role:** detect genuinely new information.

Novelty must remain distinct from:

```text
noise
format change
source duplication
paraphrase
repeated evidence
```

Candidate rule:

[
Novel(x)
========

InformationNotAlreadyRepresented(x)
]

subject to provenance and semantic-equivalence checks.

---

# 20. A11 — Conflict Monitor

**Role:** increase attention toward unresolved contradictions that can alter downstream conclusions.

Candidate targets:

```text
observation conflicts
claim conflicts
regime conflicts
scope conflicts
provenance conflicts
authority conflicts
dependency conflicts
model conflicts
```

The agent must preserve:

```text
COMPETING
```

when discriminating evidence is insufficient.

---

# 21. A12 — Attention Balancer

**Role:** prevent over-allocation to one target, modality, agent, or hypothesis.

It should monitor:

```text
concentration
coverage
starvation
fixation
redundancy
context saturation
resource exhaustion
```

Candidate concentration measure:

[
Concentration
=============

\frac{\max_i b_i}{B_{total}}
]

This is a model diagnostic only.

No universal safe threshold is asserted.

---

# 22. A13 — Attention Drift Monitor

**Role:** detect when active focus deviates from the authorized objective or decision-relevant uncertainty.

Potential drift signals:

```text
repeated low-impact work
latest-result chasing
unnecessary raw evidence loading
irrelevant branching
scope expansion
objective substitution
tool-output fixation
cosmetic optimization
```

Repair action may include:

```text
freeze
re-anchor objective
restore budget
invalidate irrelevant branch
resume smallest sufficient path
```

---

# 23. A14 — Fixation Detector

**Role:** detect excessive attention persistence on one target or hypothesis.

Candidate fixation indicators:

```text
repeated analysis without new evidence
repeated identical tool path
unchanged failed hypothesis
high token/resource concentration
ignored competing evidence
ignored stop conditions
```

Hard rule:

```text
FAILED PATH
+
NO CHANGED EVIDENCE
+
NO CHANGED ASSUMPTION
=
DO NOT REPEAT
```

---

# 24. A15 — Starvation Detector

**Role:** detect material targets receiving insufficient attention.

Candidate starvation candidates:

```text
load-bearing premise
critical safety constraint
unresolved contradiction
high-value falsifier
expiring authority
stale critical evidence
repair-critical dependency
```

Attention starvation is especially material when the ignored target can flip the outcome.

---

# 25. A16 — Distractor Filter

**Role:** reduce resource allocation to highly salient but low decision-value information.

Potential distractors:

```text
repetition
cosmetic detail
low-impact novelty
non-load-bearing contradiction
irrelevant background
redundant descendants of one source
low-value side branches
```

Filtering must not discard evidence merely because it is inconvenient.

---

# 26. A17 — Cross-Scale Attention Agent

**Role:** coordinate H/M/L attention.

```text
H = governing objective / system constraint
M = subsystem / competing workstream
L = observation / detail / local evidence
```

Candidate rule:

```text
H attention sets bounds
↓
M attention allocates subsystem budget
↓
L attention resolves decisive detail
```

But upward escalation is permitted when L evidence invalidates an H premise.

---

# 27. A18 — Attention Repair Agent

**Role:** repair invalid attention allocation.

Repair targets:

```text
drift
fixation
starvation
over-allocation
under-allocation
scope leakage
regime mismatch
stale priority
authority mismatch
dependency change
```

Repair must preserve:

```text
prior allocation
why it failed
what changed
what new allocation replaced it
```

---

# 28. A19 — Attention Auditor

**Role:** independently inspect whether the attention system obeyed its contract.

Audit questions:

```text
Was the authorized objective preserved?
Were load-bearing premises prioritized?
Were hard constraints respected?
Was salience confused with truth?
Were competing hypotheses preserved?
Was provenance considered?
Were resources wasted on redundant evidence?
Was the stop condition respected?
Were critical gaps ignored?
Did any agent exceed authority?
```

Auditing is separate from allocation.

---

# 29. A20 — Control-Plane Interface Agent

**Role:** translate cognitive attention proposals into control-plane-readable requests.

It may prepare:

```text
allocation proposal
budget request
escalation request
tool-use proposal
revalidation request
quarantine request
```

It may not self-authorize consequential effects.

[
\boxed{
InterfaceAgent
\neq
AuthorityRoot
}
]

---

# 30. Agent State Variables

```text
A_id   = agent identity
Role   = declared role
Cap    = capability set
Auth   = authority envelope
B      = allocated budget
Used   = consumed budget
Avail  = remaining budget
Targets = active attention targets
HML    = active scale
Sc     = scope
Rg     = regime
P      = provenance
U      = uncertainty
V      = validation state
D      = dependencies
F      = failure state
Rep    = repair state
```

---

# 31. Attention Allocation Tensor

Candidate primitive-level tensor:

[
\boxed{
T_{att}
=======

T[
target,
salience,
goal_relevance,
risk,
uncertainty,
urgency,
novelty,
dependency_criticality,
information_value,
cost,
HML,
scope,
regime,
provenance,
allocation
]
}
]

The tensor encodes decision-relevant dimensions.

It does not imply that those dimensions have canonical numerical scales.

---

# 32. Candidate Attention Equation

Candidate structural allocation score:

[
Score(x)
========

w_g G_x
+
w_r R_x
+
w_u U_x
+
w_t T_x
+
w_d D_x
+
w_n N_x
+
w_i I_x
-------

w_c Cost_x
]

subject to hard invariants.

This is explicitly:

```text
AMOS_MODEL
```

not recovered L02 canon.

No canonical weights are claimed.

A safer governance form is:

[
\boxed{
Admit(x)
========

\bigwedge_k HardInvariant_k(x)
}
]

followed by ranking among admissible candidates.

Thus:

```text
HARD FAILURE
!=
COMPENSATABLE LOW SCORE
```

---

# 33. Core Agent Invariants

```text
L02-AGT-INV-001
Attention is finite.

L02-AGT-INV-002
Salience does not establish truth.

L02-AGT-INV-003
Frequency does not establish importance.

L02-AGT-INV-004
Recentness does not automatically establish priority.

L02-AGT-INV-005
Goal relevance must use the active authorized objective.

L02-AGT-INV-006
Hard constraints are non-compensatory.

L02-AGT-INV-007
Critical gaps receive attention before cosmetic gaps when decision-relevant.

L02-AGT-INV-008
Competing hypotheses must remain visible.

L02-AGT-INV-009
Correlated evidence must not consume budget as though independently confirming.

L02-AGT-INV-010
Derived confidence remains bounded by load-bearing premises.

L02-AGT-INV-011
Attention allocation must preserve scope.

L02-AGT-INV-012
Attention allocation must preserve regime.

L02-AGT-INV-013
Attention allocation must preserve H/M/L position.

L02-AGT-INV-014
Attention agents must preserve provenance.

L02-AGT-INV-015
Capability does not establish authority.

L02-AGT-INV-016
Proposal does not establish commit.

L02-AGT-INV-017
Unknown budget or priority state cannot silently become valid allocation.

L02-AGT-INV-018
Failed paths cannot repeat unchanged indefinitely.

L02-AGT-INV-019
Repair must preserve allocation history.

L02-AGT-INV-020
Optimization may not weaken integrity.
```

---

# 34. Attention Conservation Constraint

For an explicit finite budget:

[
\boxed{
\sum_i Allocation_i
+
Reserve
\le
Budget_{total}
}
]

If actual resource dimensions are unknown:

```text
Budget = UNKNOWN
```

rather than fabricating a precise capacity.

---

# 35. Minimum Attention Principle

Use the smallest sufficient attention scope.

Conceptually:

[
\boxed{
A^*
===

\min A
\quad
\text{s.t.}
\quad
DecisionSufficiency(A)=1
}
]

This is an AMOS_MODEL efficiency rule.

It means:

```text
do not spend scarce reasoning budget
on information that cannot materially change
the answer, decision, validation state, or repair path.
```

---

# 36. Escalation Principle

Escalate attention when:

```text
stakes increase
irreversibility increases
uncertainty becomes decision-changing
evidence conflicts
provenance independence is unclear
scope changes
regime changes
freshness fails
authority is ambiguous
causal claims are proposed
```

De-escalate after decisive uncertainty is resolved.

---

# 37. Dependencies

Primary architectural dependencies:

```text
L00_REALITY_ENVIRONMENT
L01_SENSING_OBSERVATION
L02_DEFINITION
L02_PURPOSE
L02_VARIABLES
L02_STATE
L02_OPERATORS
L02_INVARIANTS
L02_DEPENDENCIES
L02_HML
L02_SKILLS
L02_WORKFLOWS
L02_PROTOCOLS
L02_CONTROL_PLANES
L02_PROVENANCE
L02_RSCF
L02_FAILURE_MODES
L02_REPAIR
L02_TESTS
```

Functional dependencies include:

```text
active objective state
observations
attention budget
risk constraints
time constraints
provenance state
uncertainty state
dependency graph
authority state
```

---

# 38. H/M/L Applicability

## H — Governing Attention

H-level agents attend to:

```text
primary objective
global constraints
major risks
resource envelope
system integrity
governance state
critical regime changes
```

## M — Subsystem Attention

M-level agents attend to:

```text
workstreams
hypotheses
subsystems
evidence clusters
tool families
active plans
```

## L — Local Attention

L-level agents attend to:

```text
individual observations
individual claims
specific conflicts
specific tool results
individual variables
specific falsifiers
```

---

# 39. Cross-Scale Attention Rule

Candidate structure:

[
A_H
\rightarrow
A_M
\rightarrow
A_L
]

but upward interrupts are permitted:

[
Critical_L
\rightarrow
Reallocate_M
\rightarrow
Reassess_H
]

if a local finding invalidates a governing assumption.

Hard boundary:

```text
H PRIORITY
!=
PERMISSION TO IGNORE FALSIFYING L EVIDENCE
```

---

# 40. Control-Plane Requirements

The control plane should own or validate:

```text
active objective identity
attention budget
resource ceilings
tool-call ceilings
authority envelope
hard safety constraints
scope boundaries
regime boundaries
commit eligibility
external side effects
cross-agent allocation policy
quarantine
rollback
```

Attention agents may propose resource allocation.

They must not own final authority unless explicitly delegated.

---

# 41. Agent Authority Envelope

Candidate authority levels:

```yaml
authority_levels:

  OBSERVE:
    may:
      - read permitted state

  SCORE:
    may:
      - compute attention features

  PROPOSE:
    may:
      - propose attention allocation

  ROUTE:
    may:
      - route work to approved subsystem

  ESCALATE:
    may:
      - request higher-level attention

  VALIDATE:
    may:
      - validate allocation under declared contract

  COMMIT:
    may:
      - commit allocation only if explicitly authorized
```

No role inherits `COMMIT` automatically.

---

# 42. Agent Cooperation Model

Candidate collaboration:

```text
ATTENTION ROUTER
↓
PRIORITY ASSESSOR
↓
SPECIALIST ATTENTION AGENTS
├── RISK
├── UNCERTAINTY
├── DEPENDENCY
├── TEMPORAL
├── NOVELTY
└── CONFLICT
↓
ATTENTION BALANCER
↓
BUDGET ALLOCATOR
↓
ATTENTION AUDITOR
↓
CONTROL-PLANE INTERFACE
```

This is a proposed logical decomposition.

It does not require separate LLM instances.

A runtime may implement multiple roles inside one deterministic or model-assisted component.

---

# 43. Anti-Homogenization Rule

Specialist agents should not merely reproduce one shared ranking.

If all specialists use identical signals, they provide little independent value.

Where role separation matters:

```text
risk agent
!=
novelty agent

uncertainty agent
!=
goal relevance agent

priority assessor
!=
auditor
```

However:

```text
DIFFERENT ROLE
!=
INDEPENDENT EVIDENCE
```

Agent diversity must not be confused with provenance independence.

---

# 44. Workflow — Standard Attention Allocation

```text
ACTIVE OBJECTIVE
↓
LOAD CURRENT OBSERVATIONS
↓
LOAD ATTENTION BUDGET
↓
GENERATE ATTENTION CANDIDATES
↓
FILTER HARD-INVARIANT VIOLATIONS
↓
ASSESS:
  goal relevance
  risk
  uncertainty
  urgency
  dependency criticality
  novelty
  information value
  cost
↓
CHECK H/M/L
↓
CHECK SCOPE / REGIME
↓
BALANCE ALLOCATION
↓
PROPOSE FOCUS SET
↓
AUDIT
↓
CONTROL-PLANE VALIDATION
↓
COMMIT / REVISE / QUARANTINE
```

---

# 45. Workflow — High-Stakes Allocation

```text
HIGH-CONSEQUENCE TARGET
↓
INCREASE VALIDATION DEPTH
↓
CHECK LOAD-BEARING PREMISES
↓
CHECK PROVENANCE INDEPENDENCE
↓
CHECK REGIME
↓
CHECK FRESHNESS
↓
CHECK CAUSAL STATUS
↓
CHECK REVERSIBILITY
↓
PRESERVE COMPETING HYPOTHESES
↓
ALLOCATE ADDITIONAL ATTENTION IF DECISION VALUE > COST
↓
AUDIT
```

---

# 46. Workflow — Attention Drift Recovery

```text
DRIFT DETECTED
↓
FREEZE NONESSENTIAL ALLOCATION
↓
RESTORE AUTHORIZED OBJECTIVE
↓
IDENTIFY DRIFTED TARGETS
↓
RELEASE THEIR BUDGET
↓
RESTORE LOAD-BEARING TARGETS
↓
CHECK DEPENDENCIES
↓
REVALIDATE PRIORITY
↓
RESUME
```

---

# 47. Workflow — Fixation Recovery

```text
TARGET RECEIVES REPEATED ATTENTION
↓
CHECK FOR NEW EVIDENCE
↓
CHECK FOR CHANGED STATE
↓
CHECK WHETHER RESULT CAN CHANGE
↓
NO MATERIAL CHANGE?
    ↓
    STOP REPEATING
    ↓
    REDISTRIBUTE BUDGET
YES?
    ↓
    CONTINUE BOUNDED INVESTIGATION
```

---

# 48. Workflow — Critical Gap Escalation

```text
GAP IDENTIFIED
↓
CLASSIFY:
  CRITICAL
  DECISION-RELEVANT
  EXPLANATORY
  COSMETIC
↓
CRITICAL?
  ↓
CHECK WHETHER GAP CAN FLIP CONCLUSION
↓
SELECT CHEAPEST HIGH-INFORMATION TEST
↓
ALLOCATE ATTENTION
↓
RESOLVE / CONDITIONAL / UNKNOWN
```

---

# 49. Protocols

Candidate agent protocol objects:

```text
AttentionCandidateEvent
AttentionScoreRequest
AttentionScoreResult
BudgetRequest
BudgetAllocationProposal
AttentionRouteRequest
AttentionEscalationRequest
AttentionDeferEvent
AttentionMonitorEvent
AttentionSuppressionProposal
AttentionConflictEvent
AttentionDriftEvent
AttentionRepairProposal
AttentionAuditRequest
AttentionAuditResult
AttentionCommitProposal
AttentionCommitResult
```

Material protocol messages should preserve:

```text
agent_id
role
target_id
budget
scope
regime
H/M/L
provenance
timestamp
authority
validation state
```

---

# 50. Evidence / Provenance Requirements

Every consequential allocation should be traceable to:

```text
active objective
candidate target
observations
risk constraints
uncertainty
dependency information
priority factors
budget state
agent role
allocation decision
validation result
authority context
```

Candidate provenance tensor:

[
\boxed{
P_{att}
=======

T[
target,
objective,
inputs,
agent,
scoring,
budget,
scope,
regime,
HML,
validation,
authority
]
}
]

---

# 51. Uncertainty Vector

Candidate attention uncertainty:

```yaml
attention_uncertainty:

  evidence:
    type: LOW | MEDIUM | HIGH | UNKNOWN

  goal_relevance:
    type: LOW | MEDIUM | HIGH | UNKNOWN

  priority_model:
    type: LOW | MEDIUM | HIGH | UNKNOWN

  scope:
    type: LOW | MEDIUM | HIGH | UNKNOWN

  regime:
    type: LOW | MEDIUM | HIGH | UNKNOWN

  temporal:
    type: LOW | MEDIUM | HIGH | UNKNOWN

  dependency:
    type: LOW | MEDIUM | HIGH | UNKNOWN

  provenance_independence:
    type: LOW | MEDIUM | HIGH | UNKNOWN

  execution:
    type: LOW | MEDIUM | HIGH | UNKNOWN
```

---

# 52. Confidence Ceiling

For an allocation proposal (A):

[
\boxed{
Conf(A)
\le
\min_i Conf(P_i)
}
]

for load-bearing premises (P_i).

Candidate expansion:

[
Conf(A)
\le
\min(
Conf_{goal},
Conf_{evidence},
Conf_{risk},
Conf_{dependency},
Conf_{scope},
Conf_{regime},
Conf_{budget}
)
]

where applicable.

No fluent ranking may raise weak evidence above its actual support.

---

# 53. Failure Modes

```text
FM-L02-AGT-001   Salience-as-Truth
FM-L02-AGT-002   Salience-as-Priority
FM-L02-AGT-003   Recentness-Bias
FM-L02-AGT-004   Novelty-Bias
FM-L02-AGT-005   Goal-Drift
FM-L02-AGT-006   Attention-Fixation
FM-L02-AGT-007   Critical-Target-Starvation
FM-L02-AGT-008   Budget-Overrun
FM-L02-AGT-009   Budget-Underutilization
FM-L02-AGT-010   Redundant-Evidence-Waste
FM-L02-AGT-011   Provenance-Blindness
FM-L02-AGT-012   Correlated-Confirmation-Inflation
FM-L02-AGT-013   Scope-Leakage
FM-L02-AGT-014   Regime-Leakage
FM-L02-AGT-015   HML-Collapse
FM-L02-AGT-016   Low-Impact-Branching
FM-L02-AGT-017   Premature-Closure
FM-L02-AGT-018   Endless-Investigation
FM-L02-AGT-019   Hard-Constraint-Compensation
FM-L02-AGT-020   Capability-Authority-Collapse
FM-L02-AGT-021   Proposal-Commit-Collapse
FM-L02-AGT-022   Unknown-As-Pass
FM-L02-AGT-023   Auditor/Allocator-Collapse
FM-L02-AGT-024   Specialist-Homogenization
FM-L02-AGT-025   Missing-Stop-Condition
FM-L02-AGT-026   Context-Saturation
FM-L02-AGT-027   Resource-Reserve-Exhaustion
FM-L02-AGT-028   Stale-Priority-Reuse
FM-L02-AGT-029   Conflict-Suppression
FM-L02-AGT-030   Repair-Lineage-Loss
```

---

# 54. Repair / Recovery

General attention repair:

```text
DETECT ALLOCATION FAILURE
↓
FREEZE AFFECTED ALLOCATION
↓
PRESERVE CURRENT ALLOCATION HISTORY
↓
IDENTIFY FAILED PREMISE
↓
IDENTIFY FAILED AGENT / ROLE / RULE
↓
TRACE DOWNSTREAM RESOURCE EFFECT
↓
RESTORE OBJECTIVE
↓
RESTORE HARD CONSTRAINTS
↓
RECOMPUTE PRIORITY ONLY WHERE AFFECTED
↓
REDISTRIBUTE BUDGET
↓
AUDIT
↓
REVALIDATE
↓
COMMIT IF AUTHORIZED
```

Repair must not require global attention recomputation when the affected dependency closure is local.

---

# 55. Selective Attention Reallocation

If target (x)'s priority premise fails:

[
Affected(x)
===========

AttentionAllocationsDependentOn(x)
]

Only affected allocations should be invalidated where dependency structure permits.

```text
LOCAL PRIORITY FAILURE
!=
GLOBAL ATTENTION RESET
```

---

# 56. Agents and AI Application

For AI systems, L02 agents may govern scarce resources such as:

```text
reasoning tokens
context-window space
retrieval budget
web queries
tool calls
model invocations
verification passes
simulation runs
human review requests
memory reads
memory writes
test execution
```

The architecture can therefore serve as a control layer over AI cognition:

```text
AI INPUT FIELD
↓
L01 OBSERVATION
↓
L02 ATTENTION
↓
RESOURCE ALLOCATION
↓
REASON / RETRIEVE / VERIFY / TOOL / DEFER
```

---

# 57. AI Attention Use Cases

Candidate applications:

```text
select which documents to read deeply
choose which claims require verification
decide which tool calls justify cost
route high-risk outputs for stronger validation
limit redundant retrieval
prioritize unresolved contradictions
preserve attention for critical dependencies
defer cosmetic work
detect reasoning loops
detect context-window saturation
route high-uncertainty cases to human review
```

These are implementation possibilities, not claims of current deployment.

---

# 58. AI Attention Safety Boundary

An AI attention controller must not use priority scoring to bypass:

```text
safety constraints
privacy constraints
authority constraints
legal constraints
user scope
information boundaries
```

Candidate law:

[
\boxed{
AdmissibleTarget(x)
===================

\bigwedge_i HardInvariant_i(x)
}
]

Only then may ranking occur.

---

# 59. Tests / Validators

Candidate validators:

```text
VALIDATOR_AGENT_IDENTITY
VALIDATOR_ROLE
VALIDATOR_CAPABILITY
VALIDATOR_AUTHORITY
VALIDATOR_ATTENTION_BUDGET
VALIDATOR_GOAL_RELEVANCE
VALIDATOR_HARD_CONSTRAINTS
VALIDATOR_SCOPE
VALIDATOR_REGIME
VALIDATOR_HML
VALIDATOR_PROVENANCE
VALIDATOR_DEPENDENCY_CRITICALITY
VALIDATOR_UNCERTAINTY
VALIDATOR_PRIORITY
VALIDATOR_FIXATION
VALIDATOR_STARVATION
VALIDATOR_DRIFT
VALIDATOR_STOP_CONDITION
VALIDATOR_PROPOSAL_COMMIT
VALIDATOR_REPAIR_LINEAGE
```

---

# 60. Minimum Test Suite

```text
TEST_L02_AGENT_001
An agent cannot allocate more budget than available.

TEST_L02_AGENT_002
Salience alone cannot establish priority.

TEST_L02_AGENT_003
High salience cannot establish truth.

TEST_L02_AGENT_004
Goal relevance uses the current authorized objective.

TEST_L02_AGENT_005
Critical hard constraint blocks inadmissible target regardless of score.

TEST_L02_AGENT_006
UNKNOWN priority premise cannot silently become PASS.

TEST_L02_AGENT_007
Correlated evidence does not receive independent-confirmation bonus.

TEST_L02_AGENT_008
Repeated failed path without changed evidence is stopped.

TEST_L02_AGENT_009
High dependency-criticality premise receives attention when decision-relevant.

TEST_L02_AGENT_010
Critical gap is prioritized over cosmetic gap.

TEST_L02_AGENT_011
L-level anomaly cannot silently become H-level priority.

TEST_L02_AGENT_012
Scope widening without evidence fails validation.

TEST_L02_AGENT_013
Regime widening without evidence fails validation.

TEST_L02_AGENT_014
Quarantined information cannot silently become an active target.

TEST_L02_AGENT_015
Capability cannot create authority.

TEST_L02_AGENT_016
Allocation proposal does not equal committed allocation.

TEST_L02_AGENT_017
Auditor can disagree with allocator without being overwritten.

TEST_L02_AGENT_018
Fixation detection releases budget when no new evidence exists.

TEST_L02_AGENT_019
Attention-starved load-bearing premise triggers escalation.

TEST_L02_AGENT_020
Repair preserves failed allocation history.
```

---

# 61. Adversarial Tests

Test agents against:

```text
high-salience false input
repeated paraphrased evidence
source-Sybil evidence
goal injection
scope injection
regime injection
false urgency
false novelty
attention flooding
context flooding
adversarial distractor
tool-output fixation
infinite research loop
hidden critical dependency
conflicting high-priority signals
authority spoofing
stale authority
stale objective
budget exhaustion
reserve exhaustion
cross-scale priority inflation
```

---

# 62. Falsifiers

This agent contract should be revised if:

```text
direct canonical L02 AGENTS material contradicts it

canonical AMOS attention semantics define different roles

canonical attention equations conflict with proposed scoring structures

canonical control-plane ownership differs materially

canonical H/M/L semantics invalidate cross-scale attention

canonical budget semantics differ materially

executable runtime proves proposed interfaces incompatible

formal analysis identifies contradictory agent invariants

executed tests falsify the proposed attention behavior
```

---

# 63. Gap Matrix

```yaml
gap_matrix:

  direct_L02_AGENTS_canon:
    status: GAP
    criticality: CRITICAL

  recovered_L02_placeholder:
    status: VERIFIED_SOURCE_ARTIFACT
    criticality: FOUNDATIONAL

  attention_allocation_role:
    status: SOURCE_SUPPORTED

  scarce_resource_budget_role:
    status: SOURCE_SUPPORTED

  canonical_agent_registry:
    status: GAP
    criticality: CRITICAL

  canonical_agent_names:
    status: GAP
    criticality: EXPLANATORY

  canonical_attention_tensor:
    status: GAP
    criticality: DECISION_RELEVANT

  canonical_priority_equations:
    status: GAP
    criticality: CRITICAL

  canonical_weights_thresholds:
    status: GAP
    criticality: CRITICAL

  canonical_budget_semantics:
    status: GAP
    criticality: CRITICAL

  canonical_control_plane_binding:
    status: GAP
    criticality: CRITICAL

  canonical_agent_authority:
    status: GAP
    criticality: CRITICAL

  canonical_agent_protocols:
    status: GAP
    criticality: DECISION_RELEVANT

  executable_agent_runtime:
    status: GAP
    criticality: CRITICAL

  executed_tests:
    status: GAP
    criticality: CRITICAL

  empirical_validation:
    status: GAP
    criticality: CRITICAL

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
    status: MODEL_COMPLETE_UNEXECUTED
```

---

# 64. Gap Resolution Priority

```text
1. Recover direct L02 ATTENTION canon.

2. Recover direct L02 AGENTS canon if it exists.

3. Extract exact attention variables.

4. Extract exact agent definitions.

5. Extract exact attention operators.

6. Extract exact allocation equations.

7. Resolve whether priority scoring is canonical or only conceptual.

8. Resolve canonical attention-budget semantics.

9. Resolve H/M/L attention allocation.

10. Resolve control-plane ownership.

11. Resolve agent authority boundaries.

12. Resolve agent-to-skill mappings.

13. Resolve attention state machine.

14. Build executable schema.

15. Implement deterministic validators.

16. Execute allocation tests.

17. Execute fixation/starvation tests.

18. Execute adversarial attention tests.

19. Execute repair/reallocation tests.

20. Promote status only from source or execution evidence.
```

---

# 65. Evidence / Provenance of This Artifact

```yaml
artifact_provenance:

  artifact:
    L02_ATTENTION/AGENTS.md

  origin_architect:
    Trang Phan

  direct_source:
    L02_ATTENTION/PLACEHOLDER.md

  direct_source_claims:
    - attention allocation primitive
    - budgets scarce reasoning/observation resources
    - current status UNKNOWN/GAP
    - direct canon not yet established
    - promotion requires dependencies/provenance/scope/regime/tests/authority

  derivation:
    class: SOURCE_BOUNDED_AMOS_MODEL_RECONSTRUCTION

  direct_L02_AGENTS_canon:
    status: UNKNOWN/GAP

  executable_validation:
    status: NOT_EXECUTED

  empirical_validation:
    status: NOT_ESTABLISHED
```

---

# 66. Uncertainty Vector

```yaml
uncertainty:

  evidence:
    level: HIGH
    reason:
      exact canonical L02 agent architecture is not recovered

  model:
    level: MEDIUM
    reason:
      architecture follows source-supported attention-allocation purpose
      and AMOS attention-governance principles but specific agents are reconstructed

  scope:
    level: MEDIUM

  temporal:
    level: MEDIUM

  causal:
    level: LOW
    reason:
      this artifact does not infer biological or causal mechanisms of attention

  execution:
    level: HIGH
    reason:
      no executable L02 agent runtime has been established

  provenance_independence:
    level: MEDIUM_HIGH
```

---

# 67. Confidence Ceiling

Strongest warranted conclusion:

```text
SOURCE-BOUNDED STRUCTURALLY COHERENT
AMOS L02 AGENT MODEL
```

not:

```text
DIRECT L02 AGENT CANON
CANON VERIFIED
AGENTS DEPLOYED
RUNTIME VALIDATED
EMPIRICALLY VALIDATED
NEUROSCIENTIFIC MODEL OF HUMAN ATTENTION
```

Therefore:

[
\boxed{
C_{L02-AGENTS}
\le
C_{weakest\ load-bearing\ premise}
}
]

---

# 68. RSCF Completion State

```yaml
rscf:

  id:
    L02_ATTENTION_AGENTS

  claim:
    L02_ATTENTION is source-supported as an attention-allocation
    primitive for budgeting scarce reasoning/observation resources.
    This artifact models bounded agent roles for prioritization,
    budgeting, risk, uncertainty, dependency criticality, temporal
    urgency, balancing, drift detection, repair, and audit.

  claim_class:
    MODEL

  evidence:
    - L02_ATTENTION/PLACEHOLDER.md
    - source-supported L02 role
    - AMOS Attention Allocation Governor principles
    - AMOS H/M/L principles
    - AMOS RSCF principles
    - AMOS control-plane principles

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    primitive: L02_ATTENTION
    artifact: AGENTS.md
    derivation: SOURCE_BOUNDED_AMOS_MODEL_RECONSTRUCTION
    direct_L02_AGENTS_canon: UNKNOWN/GAP

  scope:
    architecture: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    primitive: L02_ATTENTION
    artifact: AGENTS

  regime:
    attention allocation / scarce cognitive resource governance

  freshness:
    revalidate_when:
      - direct L02 canon becomes available
      - L02 agent canon becomes available
      - attention-allocation semantics change
      - H/M/L contract changes
      - control-plane contract changes
      - executable runtime becomes available

  dependencies:
    - L01_SENSING_OBSERVATION
    - L02_DEFINITION
    - L02_PURPOSE
    - L02_VARIABLES
    - L02_STATE
    - L02_OPERATORS
    - L02_INVARIANTS
    - L02_DEPENDENCIES
    - L02_HML
    - L02_SKILLS
    - L02_WORKFLOWS
    - L02_PROTOCOLS
    - L02_CONTROL_PLANES
    - L02_PROVENANCE
    - L02_FAILURE_MODES
    - L02_REPAIR
    - L02_TESTS
    - AMOS_RSCF
    - AMOS_HML
    - AMOS_ATTENTION_ALLOCATION_GOVERNOR
    - AMOS_CONTROL_PLANE

  competing:

    - id: COMPETING_001
      hypothesis:
        canonical L02 may use one attention allocator rather than multiple agent roles

    - id: COMPETING_002
      hypothesis:
        many proposed roles may belong to control-plane infrastructure rather than L02

    - id: COMPETING_003
      hypothesis:
        risk and uncertainty attention may belong to downstream specialist primitives

    - id: COMPETING_004
      hypothesis:
        canonical attention allocation may be rule-based rather than agent-based

  falsifiers:
    - direct L02 canon materially contradicts this agent architecture
    - canonical L02 agent registry differs materially
    - canonical control-plane architecture assigns ownership elsewhere
    - formal analysis identifies contradictory invariants
    - executable implementation requires incompatible agent contracts

  uncertainty:
    evidence: HIGH
    model: MEDIUM
    scope: MEDIUM
    temporal: MEDIUM
    causal: LOW
    execution: HIGH
    provenance_independence: MEDIUM_HIGH

  confidence_ceiling:
    source-bounded structural AMOS MODEL only;
    exact L02 agent canon unresolved;
    runtime implementation unverified;
    empirical validation absent

  material_gaps:
    - direct canonical L02 AGENTS specification
    - exact canonical agent registry
    - exact attention equations
    - exact resource-budget semantics
    - authority ownership
    - executable runtime
    - executed validation

  cheapest_discriminating_test:
    locate direct L02 agent/operator/allocation source material
    and compare exact roles and authority boundaries against this model
```

---

# 69. Completion State

```yaml
completion_state:

  source_canon_references:
    status: PARTIAL / SOURCE_BOUND / GAP_VISIBLE

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

  direct_L02_agent_canon:
    status: GAP

  executable_implementation:
    status: GAP

  runtime_validation:
    status: GAP

  empirical_validation:
    status: GAP

  overall_artifact:
    status: COMPLETE_FOR_DECLARED_MODEL_SCOPE

  conclusion_class:
    MODEL / CONDITIONAL
```

---

# 70. Agent Contract Summary

```text
L02 ATTENTION AGENT SYSTEM
=
ATTENTION ROUTING
+
PRIORITY ASSESSMENT
+
RESOURCE BUDGETING
+
GOAL RELEVANCE
+
RISK ATTENTION
+
UNCERTAINTY ATTENTION
+
DEPENDENCY CRITICALITY
+
TEMPORAL URGENCY
+
NOVELTY MONITORING
+
CONFLICT MONITORING
+
ATTENTION BALANCING
+
DRIFT DETECTION
+
FIXATION DETECTION
+
STARVATION DETECTION
+
DISTRACTOR FILTERING
+
H/M/L COORDINATION
+
REPAIR
+
AUDIT
+
CONTROL-PLANE INTERFACE
```

The governing principle is:

> **Attention is a finite governance resource. AMOS should allocate it toward information whose processing can materially change correctness, safety, decision quality, repair, or downstream validity—without confusing salience, novelty, repetition, or urgency with truth.**

---

# 71. Hard Boundaries

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

SALIENCE != TRUTH

SALIENCE != PRIORITY

NOVELTY != IMPORTANCE

RECENT != IMPORTANT

URGENT != CORRECT

FREQUENT != TRUE

REPEATED != INDEPENDENT

ATTENDED != VERIFIED

IGNORED != FALSE

DEFERRED != INVALID

SUPPRESSED != FALSE

HIGH_PRIORITY != AUTHORIZED

PRIORITY_SCORE != DECISION

RESOURCE_ALLOCATION != ACTION_AUTHORITY

MORE_ATTENTION != MORE_TRUTH

MORE_TOKENS != BETTER_REASONING

MORE_SOURCES != MORE_INDEPENDENCE

MORE_AGENTS != MORE_EVIDENCE

AGENT_ROLE != DEPLOYED_AGENT

AGENT_CAPABILITY != AUTHORITY

ATTENTION_PROPOSAL != ATTENTION_COMMIT

MODEL_COMPLETE != CANON_COMPLETE

CANON_COMPLETE != IMPLEMENTED

IMPLEMENTED != VALIDATED
```

---

# 72. References

## Direct Recovered Reference

```text
PLACEHOLDER
```

The recovered source explicitly identifies L02 as an attention-allocation primitive for budgeting scarce reasoning/observation resources, while retaining `UNKNOWN/GAP` status. 

## Internal L01/L02 References

```text
L01_SENSING_OBSERVATION — Readme
L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README
L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README
L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README

L02_ATTENTION — Readme
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
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
```

## Architecture References

```text
AMOS Full Brain OS Architecture
Cosmo_Brain_BRIDGE_INDEX
AMOS Cognition
AMOS RSCF
AMOS HML Architecture
Cosmo_Brain_BRIDGE_INDEX
AMOS Context Budget Governor
Cosmo_Brain_BRIDGE_INDEX
AMOS Provenance Topology
Cosmo_Brain_BRIDGE_INDEX
AMOS Deterministic AI Control Plane
Cosmo_Brain_BRIDGE_INDEX
```

## Source Lineage References

```text
AMOS_CORE_ALL_VERSIONS_EXHAUSTIVE_MASTER_UPDATED
AMOS_CORE_ALL_VERSIONS_EXHAUSTIVE_MASTER
AMOS_CORE_ALL_VERSIONS_FRACTAL_KNOWLEDGE_NETWORK
AMOS_CORE v4.4 lineage
AMOS_FULL_BRAIN_OS
AMOS_COGNITION
```

> Reference presence establishes intended lineage and dependency only. It does not establish that the reconstructed L02 agent registry or equations above appear verbatim in those sources.

---

**Related:** [[L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README]]

```text
```

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: l02_attention_primitives_cognitive_matrix_agents
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L02_ATTENTION/L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_AGENTS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[L02_ATTENTION_MOC]]
