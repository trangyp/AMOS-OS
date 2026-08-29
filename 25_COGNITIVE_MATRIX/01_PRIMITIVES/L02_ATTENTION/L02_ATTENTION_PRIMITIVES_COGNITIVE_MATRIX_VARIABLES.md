---
type: variable
source: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L02_ATTENTION
tags:
- amos
- cognitive-matrix
- matrix/l02
- attention
- variables
- typed-state
- rscf
- hml
- governance
- domain/cognitive-matrix
title: L02_ATTENTION — Variables
origin_architect: Trang Phan
status: MODEL_VARIABLE_CONTRACT / UNIMPLEMENTED / UNVALIDATED
epistemic_class: MODEL
runtime_alignment: AMOS Full Brain OS / AMOS_CORE v4.4 lineage
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# L02_ATTENTION — Variables

**Class:** `COGNITIVE_PRIMITIVE_VARIABLE_CONTRACT`
**Origin architect / steward:** Trang Phan
**Primitive:** `L02_ATTENTION`
**Artifact:** `VARIABLES.md`
**Status:** `AMOS_MODEL / UNIMPLEMENTED / UNVALIDATED`

> **Canon boundary:** available L02 source material supports attention allocation as the primitive role and identifies scarce reasoning/observation resources as its concern. The source also requires variables, dependencies, provenance, H/M/L, failure/repair, tests/falsifiers, and governance boundaries before promotion. A canonical L02 variable registry has not been recovered. Therefore variable identifiers, tensors, domains, update functions, thresholds, and equations introduced below are `AMOS_MODEL` unless separately source-bound.

---

# 0. Purpose

Define the typed variable contract required to represent `L02_ATTENTION` without collapsing:

```text
attention
priority
salience
evidence strength
confidence
resource availability
authority
execution
```

into a single quantity.

The variable layer provides the state vocabulary consumed by:

```text
L02 operators
L02 equations
L02 invariants
L02 workflows
L02 agents
L02 Skills
L02 tests
control-plane validation
RSCF reasoning
H/M/L propagation
repair/recovery
```

The central separation is:

```text
WHAT DESERVES ATTENTION
!=
WHAT IS TRUE

WHAT IS IMPORTANT
!=
WHAT IS AUTHORIZED

WHAT CAN BE PROCESSED
!=
WHAT MAY BE COMMITTED
```

---

# 1. Source / Canon References

## 1.1 Source-supported core

Recovered L02 material supports:

```text
L02_ATTENTION
=
attention allocation;
budget scarce reasoning/observation resources
```

and requires explicit treatment of:

```text
variables
state
operators
invariants
dependencies
H/M/L
control-plane requirements
memory
Skills
protocols
provenance
failure modes
repair / rollback
tests / falsifiers
RSCF / GMEF
authority boundaries
```

## 1.2 Evidence boundary

```yaml
source_status:

  primitive_identity:
    status: SOURCE_SUPPORTED

  attention_allocation_role:
    status: SOURCE_SUPPORTED

  scarce_resource_role:
    status: SOURCE_SUPPORTED

  requirement_for_variables:
    status: SOURCE_SUPPORTED

  canonical_variable_names:
    status: UNKNOWN_GAP

  canonical_variable_types:
    status: UNKNOWN_GAP

  canonical_domains:
    status: UNKNOWN_GAP

  canonical_thresholds:
    status: UNKNOWN_GAP

  canonical_update_equations:
    status: UNKNOWN_GAP

  executable_variable_schema:
    status: UNKNOWN_GAP
```

---

# 2. Definition and Scope

An L02 variable is a typed state element used to describe:

```text
candidate attention targets
available attention resources
allocation decisions
priority drivers
epistemic conditions
dependency state
scope/regime/freshness
provenance
authority
attention history
failure/recovery state
```

Formal model:

[
V^{L02}_t =
(C_t,B_t,A_t,P_t,E_t,U_t,D_t,S_t,R_t,F_t,\Pi_t,\Gamma_t,Auth_t,X_t)
]

where the tuple is an `AMOS_MODEL` representation rather than a recovered canonical equation.

L02 variables do **not** independently establish:

```text
truth
causality
authorization
execution
empirical validity
```

---

# 3. Variable Type System

```yaml
L02Variable:

  variable_id:
    type: VariableId

  semantic_type:
    type: VariableType

  value:
    type: Any

  domain:
    type: DomainSpec

  unit:
    type: Unit | null

  scale:
    type:
      - H
      - M
      - L
      - CROSS_SCALE

  epistemic_class:
    type:
      - SOURCE_CLAIM
      - OBSERVATION
      - DERIVED
      - MODEL
      - DECISION
      - UNKNOWN_GAP

  scope:
    type: ScopeRef

  regime:
    type: RegimeRef

  freshness:
    type: FreshnessState

  provenance:
    type: ProvenanceRef[]

  dependencies:
    type: VariableRef[]

  confidence:
    type: ConfidenceBound | null

  authority:
    type: AuthorityRef | null

  state_version:
    type: VersionRef

  validity:
    type:
      - VALID
      - CONDITIONAL
      - STALE
      - INVALID
      - UNKNOWN
```

---

# 4. Core Variable Families

The minimum proposed variable families are:

```text
1. Candidate variables
2. Resource variables
3. Allocation variables
4. Priority variables
5. Salience variables
6. Goal-relevance variables
7. Risk/consequence variables
8. Uncertainty variables
9. Evidence variables
10. Provenance variables
11. Dependency variables
12. Scope variables
13. Regime variables
14. Freshness variables
15. H/M/L variables
16. Memory variables
17. Authority variables
18. Execution/control variables
19. Switching variables
20. Repair/recovery variables
```

---

# 5. Candidate Variables

## 5.1 Candidate set

[
C_t={c_1,c_2,\ldots,c_n}
]

Type:

```yaml
C_t:
  type: AttentionCandidateSet
  cardinality: finite
```

Each candidate represents something potentially deserving processing.

Candidate examples may include:

```text
observation
claim
contradiction
question
gap
hypothesis
risk
dependency
memory
Skill
tool result
decision
action proposal
repair target
```

---

## 5.2 Candidate identity

```text
cid_i = stable candidate identity
```

Invariant:

```text
candidate alias != new candidate
```

unless provenance establishes genuinely distinct semantic origin.

---

## 5.3 Candidate class

```yaml
class_i:
  type:
    - OBSERVATION
    - CLAIM
    - GAP
    - CONTRADICTION
    - HYPOTHESIS
    - DEPENDENCY
    - RISK
    - MEMORY
    - SKILL
    - TOOL_RESULT
    - DECISION
    - ACTION_PROPOSAL
    - REPAIR_TARGET
    - OTHER
```

This registry is `AMOS_MODEL`.

---

# 6. Resource Variables

## 6.1 Total attention budget

[
B_t
]

represents the available bounded processing budget.

It must be typed by resource class.

```yaml
B_t:

  reasoning_tokens:
    type: NonNegativeQuantity

  tool_calls:
    type: NonNegativeInteger

  wall_time:
    type: Duration

  retrieval_budget:
    type: NonNegativeQuantity

  execution_budget:
    type: NonNegativeQuantity

  human_attention:
    type: NonNegativeQuantity | UNKNOWN
```

Hard rule:

```text
unlike units cannot be silently summed
```

---

## 6.2 Available budget

[
B_t^{avail}
]

with:

[
0\le B_t^{avail}\le B_t
]

---

## 6.3 Reserved budget

[
B_t^{reserve}
]

Candidate interpretation:

resources retained for:

```text
critical contradictions
late-arriving evidence
recovery
authority checks
validation
unexpected failure
```

Constraint:

[
B_t^{ordinary}
\le
B_t-B_t^{reserve}
]

where a reserve policy exists.

---

# 7. Allocation Variables

## 7.1 Candidate allocation

[
a_{i,t}
]

represents attention allocated to candidate \(c_i\).

Domain:

[
a_{i,t}\ge0
]

Resource conservation:

[
\sum_i a_{i,t}\le B_t^{avail}
]

for each compatible resource dimension.

---

## 7.2 Allocation vector

[
\mathbf{A}*t =
[a*{1,t},a_{2,t},\ldots,a_{n,t}]
]

Type:

```yaml
A_t:
  axes:
    - candidate
    - resource_class
    - time
```

---

## 7.3 Allocation status

```yaml
allocation_state_i:
  type:
    - UNALLOCATED
    - QUEUED
    - ACTIVE
    - PAUSED
    - COMPLETED
    - BLOCKED
    - INVALIDATED
```

---

# 8. Priority Variables

Priority must remain distinct from truth.

## 8.1 Priority

[
p_{i,t}
]

Type:

```text
PriorityScore | PriorityClass
```

Possible ordinal representation:

```text
CRITICAL
HIGH
MEDIUM
LOW
DEFER
```

No canonical numeric range is asserted.

---

## 8.2 Priority driver vector

Proposed representation:

[
\mathbf{P}_{i,t}
================

[
g_i,
k_i,
u_i,
r_i,
\tau_i,
d_i,
n_i,
m_i
]
]

where:

```text
g_i = goal relevance
k_i = dependency criticality
u_i = uncertainty relevance
r_i = risk/consequence relevance
τ_i = time sensitivity
d_i = decision relevance
n_i = novelty
m_i = meaning/salience contribution
```

This is `AMOS_MODEL`.

No fixed weighting equation is canonical here.

---

# 9. Salience Variables

## 9.1 Salience

[
s_{i,t}
]

represents how strongly a candidate attracts processing attention.

Hard firewall:

[
s_{i,t}\not\Rightarrow Truth(c_i)
]

and:

[
s_{i,t}\not\Rightarrow Conf(c_i)
]

Salience may influence allocation but cannot independently change epistemic status.

---

## 9.2 Novelty

[
n_{i,t}
]

represents relative novelty.

Hard boundary:

```text
NOVEL != IMPORTANT
NOVEL != TRUE
```

---

## 9.3 Repetition/frequency

[
freq_{i,t}
]

represents observed repetition.

Hard boundary:

```text
REPETITION != INDEPENDENT CONFIRMATION
```

---

# 10. Goal-Relevance Variables

## 10.1 Active objective

[
G_t
]

Type:

```yaml
G_t:
  objective_id: ObjectiveId
  scope: ScopeRef
  success_conditions: Condition[]
  constraints: ConstraintRef[]
```

---

## 10.2 Candidate-goal relevance

[
g_{i,t}
]

represents candidate relevance to \(G_t\).

Important distinction:

```text
goal relevance
!=
epistemic support
```

A false hypothesis may be highly relevant because disproving it matters.

---

# 11. Consequence / Risk Variables

## 11.1 Consequence magnitude

[
q_{i,t}
]

represents estimated downstream consequence if the candidate is mishandled.

Possible dimensions:

```text
safety
financial
legal
institutional
privacy
reputation
system integrity
irreversibility
dependency fan-out
```

---

## 11.2 Irreversibility

[
irr_{i,t}
]

represents expected difficulty/cost of reversing downstream effects.

Hard boundary:

```text
HIGH IRREVERSIBILITY
=> stronger validation demand

HIGH IRREVERSIBILITY
!= automatic execution prohibition
```

unless a governing constraint specifies prohibition.

---

# 12. Uncertainty Variables

Use an uncertainty vector rather than one scalar where material.

[
\mathbf{U}_{i,t}
================

[
u^E,
u^M,
u^S,
u^T,
u^C,
u^X,
u^P
]
]

with:

```text
u^E = evidence uncertainty
u^M = model uncertainty
u^S = scope uncertainty
u^T = temporal uncertainty
u^C = causal uncertainty
u^X = execution uncertainty
u^P = provenance-independence uncertainty
```

Domain may be qualitative:

```text
LOW
MEDIUM
HIGH
MAXIMUM
UNKNOWN
```

unless a calibrated quantitative system exists.

---

# 13. Evidence Variables

## 13.1 Evidence set

[
E_i={e_1,\ldots,e_m}
]

Each evidence object must preserve:

```yaml
EvidenceVariable:

  evidence_id: EvidenceId

  evidence_class:
    - SOURCE_CLAIM
    - OBSERVATION
    - DERIVED
    - MODEL
    - DECISION
    - UNKNOWN_GAP

  source_ref: ProvenanceRef

  scope: ScopeRef

  regime: RegimeRef

  freshness: FreshnessState

  confidence: ConfidenceBound

  dependencies: EvidenceRef[]
```

Attention does not transform an evidence class by itself.

---

# 14. Confidence Variables

## 14.1 Confidence ceiling

[
Conf^{max}\(C\)
]

For load-bearing premises:

[
Conf(C)
\le
\min_j Conf(P_j)
]

unless independent revalidation changes the dependency structure.

This is aligned with the governing AMOS confidence rule.

---

## 14.2 Attention-confidence firewall

For an attention-only operation \(T_A\):

[
Conf(T_A(C))
\le Conf(C)
]

unless \(T_A\) also acquires genuinely new admissible evidence.

Thus:

```text
MORE ATTENTION
!=
MORE CONFIDENCE
```

---

# 15. Provenance Variables

## 15.1 Provenance identity

[
\pi_i
]

Minimum fields:

```yaml
pi_i:

  source_id: SourceId
  semantic_origin_id: OriginId
  parent_refs: []
  transformation_refs: []
  version: VersionRef | null
  timestamp: Timestamp | null
```

---

## 15.2 Independence group

[
ig_i
]

represents evidence ancestry grouping.

If:

```text
E2 derives from E1
E3 summarizes E2
```

then:

```text
ig(E1) = ig(E2) = ig(E3)
```

unless an independent source enters.

---

## 15.3 Provenance recoverability

[
\rho_i^{prov}
]

Type:

```text
RECOVERABLE
PARTIAL
LOST
UNKNOWN
```

Decision-relevant provenance loss should trigger quarantine or revalidation.

---

# 16. Dependency Variables

## 16.1 Dependency graph

[
D_t=(V_D,E_D)
]

where edges represent load-bearing dependency.

---

## 16.2 Dependency criticality

[
k_i
]

Candidate interpretation:

how strongly candidate \(c_i\) can alter downstream conclusions.

---

## 16.3 Fan-out

[
fanout_i = |Descendants(c_i)|
]

Fan-out may affect attention priority but does not itself prove importance.

---

## 16.4 Dependency validity

```yaml
dependency_state_i:
  type:
    - VALID
    - CONDITIONAL
    - STALE
    - INVALID
    - UNKNOWN
```

---

# 17. Scope Variables

[
S_i
]

Minimum structure:

```yaml
Scope:

  system: string | null
  population: string | null
  environment: string | null
  scale: H | M | L | CROSS_SCALE | null
  measurement_method: string | null
  assumptions: []
```

Hard invariant:

```text
scope expansion requires evidence
```

---

# 18. Regime Variables

[
R_i
]

Examples:

```text
development
test
production
historical
live
normal
stress
simulation
deployment-specific
```

Regime is typed metadata, not free-form justification.

---

## 18.1 Regime compatibility

[
Compat(R_e,R_q)
]

returns:

```text
COMPATIBLE
CONDITIONAL
INCOMPATIBLE
UNKNOWN
```

---

# 19. Freshness Variables

## 19.1 Observation time

[
t_i^{obs}
]

## 19.2 Valid-through time

[
t_i^{valid}
]

where defined.

## 19.3 Freshness state

```text
FRESH
AGING
STALE
EXPIRED
UNKNOWN
```

Hard rule:

```text
retrieval_time != observation_time
```

and:

```text
RECALL != REFRESH
```

---

# 20. H/M/L Variables

Each material variable must identify scale.

```yaml
ScaleRef:
  type:
    - H
    - M
    - L
    - CROSS_SCALE
```

Suggested interpretation:

```text
H = governing/system level
M = subsystem/coordination level
L = local candidate/detail level
```

---

## 20.1 Cross-scale dependency

[
D^{HML}_{x\rightarrow y}
]

records an explicit dependency across levels.

Hard boundary:

```text
L observation != H conclusion
```

without a valid aggregation/translation relation.

---

# 21. Memory Variables

## 21.1 Attention memory

[
M_t^A
]

may contain:

```text
prior candidates
prior allocations
prior failures
prior discriminating tests
prior priorities
invalidated paths
repair history
```

---

## 21.2 Memory validity

```yaml
memory_state:
  type:
    - ACTIVE
    - CONDITIONAL
    - STALE
    - INVALIDATED
    - QUARANTINED
```

---

## 21.3 Reuse eligibility

[
Reuse(m,q)
]

requires compatibility across:

```text
scope
regime
freshness
dependencies
provenance
objective
```

---

# 22. Contradiction Variables

## 22.1 Contradiction set

[
K_t
]

contains unresolved incompatible claims.

---

## 22.2 Contradiction status

```text
OPEN
RESOLVED
CONDITIONAL
QUARANTINED
UNKNOWN
```

Hard rule:

```text
attention compression must not erase OPEN contradiction state
```

---

# 23. COMPETING Variables

## 23.1 Hypothesis set

[
HYP_t={h_1,\ldots,h_n}
]

Each hypothesis carries:

```text
support
counterevidence
scope
regime
provenance
independence
falsifiers
confidence ceiling
```

---

## 23.2 Competition status

```text
ACTIVE_COMPETING
DISCRIMINATED
INVALIDATED
UNRESOLVED
```

L02 may allocate attention toward discriminating evidence.

It must not fabricate convergence.

---

# 24. Decision-Value Variables

Candidate model:

[
DV_i
]

represents expected value of resolving candidate \(c_i\) for the governing decision.

Potential factors:

```text
probability result changes decision
consequence magnitude
uncertainty reduction
cost of resolution
time sensitivity
reversibility
```

No canonical scoring formula is asserted.

---

# 25. Information-Gain Variables

Candidate:

[
IG_i
]

represents expected discriminating information gained from processing a candidate.

Hard boundary:

```text
EXPECTED INFORMATION GAIN
!=
GUARANTEED TRUTH
```

---

# 26. Cost Variables

[
Cost_i
]

may be a typed vector:

[
Cost_i =
[
tokens,
time,
toolCalls,
money,
humanEffort,
risk
]
]

No scalar aggregation is permitted without an explicit conversion or policy model.

---

# 27. Switching Variables

## 27.1 Current focus

[
f_t
]

Type:

```text
CandidateId | null
```

---

## 27.2 Switching cost

[
SC_{i\rightarrow j}
]

may capture:

```text
context reload
tool setup
lost working state
cognitive/context fragmentation
execution overhead
```

---

## 27.3 Switch count

[
N^{switch}_t
]

Useful for detecting attention thrashing.

---

# 28. Persistence Variables

## 28.1 Attention age

[
age_i
]

## 28.2 Consecutive allocation

[
dur_i
]

## 28.3 Starvation duration

[
starve_i
]

These variables can support starvation/thrashing detection but do not independently define canonical thresholds.

---

# 29. Authority Variables

## 29.1 Capability

[
Cap_i
]

represents whether a component can technically perform an operation.

---

## 29.2 Authority

[
Auth_i
]

represents whether that operation is permitted.

Hard invariant:

[
Cap_i \not\Rightarrow Auth_i
]

---

## 29.3 Authority witness

```yaml
AuthorityWitness:

  principal: PrincipalRef
  permitted_effects: []
  scope: ScopeRef
  constraints: []
  valid_from: Timestamp | null
  valid_until: Timestamp | null
  version: VersionRef
```

---

# 30. Proposal / Commit Variables

## 30.1 Proposal

[
Prop_t
]

Type:

```yaml
AttentionAllocationProposal:
  allocations: []
  rationale_refs: []
  evidence_refs: []
  state_version: VersionRef
```

---

## 30.2 Commit status

```text
NOT_PROPOSED
PROPOSED
VALIDATING
COMMITTED
REJECTED
STALE
ROLLED_BACK
```

Hard boundary:

[
PROPOSED \neq COMMITTED
]

---

# 31. State-Version Variables

## 31.1 Read version

[
v^{read}
]

## 31.2 Current authoritative version

[
v^{current}
]

## 31.3 Commit version

[
v^{commit}
]

Candidate freshness gate:

[
v^{read}=v^{current}
]

or explicit revalidation is required before authoritative mutation.

This is an AMOS control-plane model, not proof of a currently implemented MVCC runtime.

---

# 32. Failure Variables

```yaml
FailureState:

  failure_id: FailureId

  failure_class:
    - TYPE_ERROR
    - BUDGET_VIOLATION
    - STARVATION
    - THRASHING
    - SALIENCE_CAPTURE
    - PROVENANCE_LOSS
    - STALE_STATE
    - SCOPE_MISMATCH
    - REGIME_MISMATCH
    - AUTHORITY_FAILURE
    - DEPENDENCY_FAILURE
    - CONTRADICTION_SUPPRESSION
    - UNKNOWN_AS_PASS
    - OTHER

  affected_variables: []

  first_detected_at: Timestamp

  recoverability:
    - LOCAL
    - SUBSYSTEM
    - GLOBAL
    - UNKNOWN

  status:
    - OPEN
    - REPAIRING
    - REPAIRED
    - ESCALATED
    - UNRECOVERABLE
```

---

# 33. Repair Variables

## 33.1 Repair target

[
RT_t
]

## 33.2 Last valid state

[
V^{valid}_{t-k}
]

## 33.3 Repair attempt count

[
N^{repair}
]

## 33.4 Changed evidence flag

[
\Delta E
]

Rule:

```text
failed repair + ΔE = 0
=> do not blindly repeat same repair path
```

---

# 34. Output Variables

L02 should output typed proposals rather than untyped priority prose.

```yaml
AttentionAllocationOutput:

  candidate_states: []

  allocations: []

  deferred_candidates: []

  blocked_candidates: []

  unresolved_gaps: []

  contradictions: []

  competing_hypotheses: []

  resource_state: {}

  scope: {}

  regime: {}

  provenance: []

  confidence_ceiling: null

  authority_state: null

  state_version: null

  proposal_status: PROPOSED
```

---

# 35. Input Variables

Candidate input contract:

```yaml
AttentionAllocationInput:

  objective:
    type: ObjectiveState

  candidates:
    type: AttentionCandidate[]

  resource_budget:
    type: ResourceBudget

  constraints:
    type: Constraint[]

  evidence_state:
    type: EvidenceState

  dependency_graph:
    type: DependencyGraph

  scope:
    type: ScopeRef

  regime:
    type: RegimeRef

  freshness:
    type: FreshnessContext

  memory:
    type: AttentionMemory | null

  authority_context:
    type: AuthorityContext

  state_version:
    type: VersionRef
```

---

# 36. Variable Invariants

```text
L02-VAR-INV-001
Every decision-relevant variable has a type.

L02-VAR-INV-002
Unlike units cannot be silently combined.

L02-VAR-INV-003
Priority != confidence.

L02-VAR-INV-004
Salience != evidence.

L02-VAR-INV-005
Novelty != truth.

L02-VAR-INV-006
Frequency != provenance independence.

L02-VAR-INV-007
Capability != authority.

L02-VAR-INV-008
Proposal state != committed state.

L02-VAR-INV-009
Unknown variable state cannot be converted to PASS.

L02-VAR-INV-010
Scope must travel with decision-relevant variables.

L02-VAR-INV-011
Regime must travel with regime-sensitive variables.

L02-VAR-INV-012
Freshness cannot be refreshed merely by recall.

L02-VAR-INV-013
Confidence cannot exceed weakest load-bearing premise without revalidation.

L02-VAR-INV-014
Variable provenance must remain recoverable where decision-relevant.

L02-VAR-INV-015
Invalidated variables cannot silently re-enter active state.

L02-VAR-INV-016
Cross-H/M/L translation requires an explicit mapping.

L02-VAR-INV-017
Attention allocation cannot exceed the applicable resource budget.

L02-VAR-INV-018
A variable marked MODEL cannot silently become OBSERVATION.

L02-VAR-INV-019
A source-derived variable cannot lose source identity during transformation.

L02-VAR-INV-020
State mutation must preserve version/freshness information where authoritative effects depend on it.
```

---

# 37. Dependencies

Variable semantics depend on the broader L02 contract:

```text
L02_ATTENTION/README
L02_ATTENTION/PURPOSE
L02_ATTENTION/DEFINITION
L02_ATTENTION/STATE
L02_ATTENTION/OPERATORS
L02_ATTENTION/INVARIANTS
L02_ATTENTION/DEPENDENCIES
L02_ATTENTION/EQUATIONS
L02_ATTENTION/HML
L02_ATTENTION/CONTROL_PLANES
L02_ATTENTION/MEMORY
L02_ATTENTION/PROTOCOLS
L02_ATTENTION/PROVENANCE
L02_ATTENTION/FAILURE_MODES
L02_ATTENTION/REPAIR
L02_ATTENTION/TESTS
L02_ATTENTION/RSCF
```

Likely external dependencies include:

```text
L01_SENSING_OBSERVATION
RSCF
constraint propagation
provenance governance
memory governance
authority/control plane
Skill routing
context-budget governance
```

Exact canonical dependency edges remain `UNKNOWN/GAP`.

---

# 38. H/M/L Applicability

## H — Governing variables

Examples:

```text
G_t
B_t
system-level consequence
global constraints
authority envelope
critical unresolved gaps
global contradiction state
```

## M — Coordination variables

Examples:

```text
subsystem budgets
Skill priorities
dependency clusters
hypothesis groups
resource partitions
repair queues
```

## L — Candidate variables

Examples:

```text
c_i
p_i
s_i
g_i
u_i
a_i
scope_i
regime_i
freshness_i
provenance_i
```

Cross-scale rule:

```text
L variable
→ explicit aggregation/translation
→ M variable
→ explicit aggregation/translation
→ H variable
```

Never:

```text
one L observation
→ unexplained H conclusion
```

---

# 39. Control-Plane Requirements

The authoritative control plane should own or validate, where applicable:

```text
resource ceilings
authority state
state versions
commit eligibility
freshness gates
scope/regime compatibility
cross-worker resource conflicts
rollback authorization
durable mutation
```

L02 may calculate or propose:

```text
candidate priorities
candidate allocations
defer/escalate recommendations
discriminating-test targets
```

but:

```text
L02 proposal
!=
authoritative commit
```

unless explicit authority is delegated.

---

# 40. Agents

Candidate logical roles:

```text
ATTENTION_ALLOCATOR
ATTENTION_STATE_AUDITOR
ATTENTION_PROVENANCE_AUDITOR
ATTENTION_RESOURCE_MONITOR
ATTENTION_ADVERSARIAL_VALIDATOR
ATTENTION_REPAIR_AGENT
```

These are architectural roles, not proof of deployed autonomous agents.

---

# 41. Skills

Potential capability families relevant to the variable contract include:

```text
AMOS Attention Allocation Governor
AMOS Context Budget Governor RSCF
AMOS Constraint Propagation RSCF
AMOS Provenance Trust Firewall
AMOS Metacognitive Confidence Auditor
AMOS Memory Conflict Governor
AMOS Repair Priority Governor
AMOS Action Memory Firewall
RSCF Modeler
```

Skill availability remains distinct from runtime invocation and authority.

---

# 42. Workflow

```text
RECEIVE INPUT VARIABLES
↓
VALIDATE TYPES
↓
VALIDATE UNITS
↓
RESOLVE OBJECTIVE
↓
RESOLVE CANDIDATE IDENTITIES
↓
RESOLVE PROVENANCE
↓
RESOLVE SCOPE / REGIME / FRESHNESS
↓
LOAD DEPENDENCY STATE
↓
LOAD RESOURCE STATE
↓
LOAD AUTHORITY CONTEXT
↓
COMPUTE / CLASSIFY PRIORITY VARIABLES
↓
ALLOCATE WITHIN BUDGET
↓
CHECK INVARIANTS
↓
GENERATE PROPOSAL
↓
CONTROL-PLANE VALIDATION
↓
COMMIT / REJECT / REVALIDATE
```

---

# 43. Protocols

Candidate variable-oriented protocols:

```text
L02_VARIABLE_DECLARE
L02_VARIABLE_VALIDATE
L02_VARIABLE_UPDATE
L02_VARIABLE_INVALIDATE
L02_VARIABLE_REVALIDATE
L02_VARIABLE_TRANSLATE_HML
L02_VARIABLE_PROVENANCE_BIND
L02_VARIABLE_SCOPE_BIND
L02_VARIABLE_REGIME_BIND
L02_VARIABLE_COMMIT_PROPOSE
```

Canonical protocol names remain `UNKNOWN/GAP`.

---

# 44. Evidence / Provenance

Every decision-relevant variable should answer:

```text
Where did this value come from?
What transformed it?
Which version produced it?
What does it depend on?
For what scope is it valid?
Under which regime?
How fresh is it?
What could invalidate it?
```

Minimum provenance:

```yaml
VariableProvenance:

  variable_id: null
  source_refs: []
  semantic_origin_refs: []
  transformation_refs: []
  dependency_refs: []
  version: null
  timestamp: null
  scope: null
  regime: null
  freshness: UNKNOWN
```

---

# 45. Failure Modes

```text
FM-L02-VAR-001
Untyped variable.

FM-L02-VAR-002
Unit mismatch.

FM-L02-VAR-003
Priority/confidence collapse.

FM-L02-VAR-004
Salience/evidence collapse.

FM-L02-VAR-005
Frequency/independence collapse.

FM-L02-VAR-006
Scope metadata lost.

FM-L02-VAR-007
Regime metadata lost.

FM-L02-VAR-008
Stale value reused as fresh.

FM-L02-VAR-009
Provenance stripped.

FM-L02-VAR-010
Variable alias treated as independent evidence.

FM-L02-VAR-011
Invalid variable remains active.

FM-L02-VAR-012
Cross-scale variable silently generalized.

FM-L02-VAR-013
Resource units incorrectly aggregated.

FM-L02-VAR-014
Allocation exceeds budget.

FM-L02-VAR-015
Capability treated as authority.

FM-L02-VAR-016
Proposal state treated as committed.

FM-L02-VAR-017
MODEL variable treated as observation.

FM-L02-VAR-018
UNKNOWN value treated as zero or PASS.

FM-L02-VAR-019
Concurrent update overwrites newer state.

FM-L02-VAR-020
Repair changes variable semantics without provenance.
```

---

# 46. Repair / Recovery

```text
DETECT INVALID VARIABLE
↓
FREEZE AFFECTED DERIVATIONS
↓
CLASSIFY FAILURE
↓
IDENTIFY SOURCE VARIABLE / EDGE
↓
INVALIDATE DEPENDENT DESCENDANTS
↓
PRESERVE UNAFFECTED STATE
↓
RESTORE LAST VALID VALUE
    OR
RECOMPUTE FROM VALID PREMISES
    OR
RETRIEVE NEW EVIDENCE
↓
REVALIDATE TYPE / SCOPE / REGIME / FRESHNESS / PROVENANCE
↓
RERUN DEPENDENT TESTS
↓
PROPOSE UPDATED STATE
```

Hard recovery rule:

[
Invalid(p)
\Rightarrow
Invalidate(Descendants(p))
]

not:

```text
invalidate everything
```

unless dependency analysis proves global impact.

---

# 47. Tests / Validators

Minimum validators:

```text
VALIDATE_VARIABLE_SCHEMA
VALIDATE_VARIABLE_TYPE
VALIDATE_UNIT_COMPATIBILITY
VALIDATE_RESOURCE_CONSERVATION

VALIDATE_PRIORITY_CONFIDENCE_SEPARATION
VALIDATE_SALIENCE_EVIDENCE_SEPARATION
VALIDATE_FREQUENCY_INDEPENDENCE_SEPARATION

VALIDATE_SCOPE_BINDING
VALIDATE_REGIME_BINDING
VALIDATE_FRESHNESS

VALIDATE_PROVENANCE
VALIDATE_DEPENDENCY_CLOSURE

VALIDATE_HML_MAPPING

VALIDATE_AUTHORITY
VALIDATE_PROPOSAL_COMMIT

VALIDATE_VERSION_FRESHNESS
VALIDATE_SELECTIVE_INVALIDATION

VALIDATE_UNKNOWN_NOT_PASS
```

Required boundary tests include:

```text
negative allocation
budget overflow
unit mismatch
null critical scope
stale evidence
lost provenance
duplicate semantic origin
cross-regime reuse
cross-HML generalization
confidence inflation from attention
unauthorized commit
stale state version
invalidated memory reuse
```

Execution status:

```text
NOT_RUN
```

unless separate runtime evidence exists.

---

# 48. Falsifiers

This variable specification must be revised if canonical evidence establishes:

```text
different canonical L02 variable identities;

different variable domains;

attention is not resource bounded;

priority and confidence are canonically identical;

L02 owns authoritative commits;

H/M/L mappings differ materially;

provenance/freshness/scope are not part of the intended L02 state;

a different canonical resource model supersedes this representation.
```

Implementation claims are falsified by reproducible cases where:

```text
allocation exceeds declared budget;

priority raises confidence without evidence;

stale evidence becomes fresh through recall alone;

source aliases create false independence;

scope/regime metadata disappears;

UNKNOWN is treated as PASS;

capability produces unauthorized commit;

invalidated variables silently return to active state.
```

---

# 49. Gap Matrix

```yaml
gap_status:

  source_role:
    status: SOURCE_SUPPORTED

  variable_requirement:
    status: SOURCE_SUPPORTED

  variable_type_system:
    status: MODEL_DEFINED

  candidate_variables:
    status: MODEL_DEFINED

  resource_variables:
    status: MODEL_DEFINED

  allocation_variables:
    status: MODEL_DEFINED

  priority_variables:
    status: MODEL_DEFINED

  salience_variables:
    status: MODEL_DEFINED

  uncertainty_variables:
    status: MODEL_DEFINED

  provenance_variables:
    status: MODEL_DEFINED

  dependency_variables:
    status: MODEL_DEFINED

  scope_regime_freshness:
    status: MODEL_DEFINED

  HML_variables:
    status: MODEL_DEFINED

  memory_variables:
    status: MODEL_DEFINED

  authority_variables:
    status: MODEL_DEFINED

  repair_variables:
    status: MODEL_DEFINED

  canonical_variable_registry:
    status: UNKNOWN_GAP

  canonical_domains:
    status: UNKNOWN_GAP

  canonical_units:
    status: UNKNOWN_GAP

  canonical_thresholds:
    status: UNKNOWN_GAP

  canonical_priority_equation:
    status: UNKNOWN_GAP

  canonical_resource_conversion:
    status: UNKNOWN_GAP

  executable_schema:
    status: UNKNOWN_GAP

  runtime_state_store:
    status: UNKNOWN_GAP

  runtime_validation:
    status: UNKNOWN_GAP
```

---

# 50. Uncertainty and Confidence Ceiling

```yaml
uncertainty:

  evidence:
    level: HIGH
    reason: canonical L02 variable registry not recovered

  model:
    level: MEDIUM
    reason: variable architecture follows established AMOS governance constraints

  scope:
    level: MEDIUM
    reason: exact L02 versus control-plane ownership remains unresolved

  temporal:
    level: MEDIUM
    reason: runtime schemas may evolve

  causal:
    level: LOW
    reason: variables describe architecture rather than establish causal effects

  execution:
    level: MAXIMUM
    reason: executable variable implementation not established

  provenance_independence:
    level: MEDIUM
    reason: available L02 material may descend from shared AMOS architecture
```

Confidence ceiling:

```text
variable architecture:
MODEL

canonical variable identity:
UNKNOWN/GAP

runtime implementation:
UNKNOWN/GAP

runtime correctness:
UNKNOWN/GAP
```

---

# 51. RSCF Completion State

```yaml
rscf:

  id: L02_ATTENTION_VARIABLES

  claim:
    L02_ATTENTION requires typed variables separating candidate identity,
    resource budget, allocation, priority, salience, epistemic confidence,
    uncertainty, provenance, dependencies, scope, regime, freshness,
    H/M/L scale, memory, authority, proposal state, and repair state so
    attention allocation cannot silently become truth, authority, or commit.

  claim_class: MODEL

  evidence:
    - L02_ATTENTION/PLACEHOLDER.md
    - source-supported L02 attention-allocation role
    - source-supported scarce-resource role

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    subsystem: COGNITIVE_MATRIX
    primitive: L02_ATTENTION
    artifact: VARIABLES.md
    derivation: SOURCE_BOUNDED_AMOS_MODEL

  scope:
    system: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    primitive: L02_ATTENTION
    concern: typed_variable_contract

  regime:
    governed architecture specification

  freshness:
    revalidate_when:
      - canonical VARIABLES source is recovered
      - L02 equations change
      - L02 state semantics change
      - H/M/L mappings change
      - control-plane ownership changes
      - executable runtime schema appears

  dependencies:
    - L02_ATTENTION_DEFINITION
    - L02_ATTENTION_STATE
    - L02_ATTENTION_OPERATORS
    - L02_ATTENTION_INVARIANTS
    - L02_ATTENTION_DEPENDENCIES
    - L02_ATTENTION_EQUATIONS
    - L02_ATTENTION_HML
    - L02_ATTENTION_CONTROL_PLANES
    - L02_ATTENTION_MEMORY
    - L02_ATTENTION_PROVENANCE
    - L02_ATTENTION_FAILURE_MODES
    - L02_ATTENTION_REPAIR
    - L02_ATTENTION_TESTS
    - AMOS_CORE_V4_4_LINEAGE

  competing:
    - minimal local attention-state model
    - centralized control-plane attention state
    - distributed attention-state model
    - hybrid local proposal plus authoritative global state

  falsifiers:
    - incompatible canonical variable registry
    - incompatible canonical state semantics
    - incompatible resource model
    - runtime evidence invalidating modeled invariants

  uncertainty:
    evidence: HIGH
    model: MEDIUM
    scope: MEDIUM
    temporal: MEDIUM
    causal: LOW
    execution: MAXIMUM
    provenance_independence: MEDIUM

  confidence_ceiling:
    MODEL only; variable names and equations must not be represented
    as canonical or implemented until source/runtime evidence establishes them

  gap_status:
    canonical_variable_registry: CRITICAL
    executable_schema: CRITICAL
    runtime_state_store: CRITICAL
    runtime_validation: CRITICAL

  cheapest_discriminating_test:
    recover canonical VARIABLES/STATE/EQUATIONS artifacts if they exist;
    otherwise implement the smallest typed L02 state schema and test
    budget conservation, epistemic separation, provenance preservation,
    scope/regime/freshness handling, and proposal/commit separation
```

---

# 52. Completion State

```yaml
completion_state:

  source_canon_references:
    status: PARTIAL_SOURCE_BOUND

  definition_scope:
    status: MODEL_COMPLETE

  typed_inputs_outputs:
    status: MODEL_COMPLETE

  state_variables:
    status: MODEL_COMPLETE

  operators:
    status: MODEL_COMPLETE_REFERENCE_BOUND

  invariants:
    status: MODEL_COMPLETE

  dependencies:
    status: MODEL_COMPLETE_WITH_GAPS

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
    status: MODEL_COMPLETE_SOURCE_PARTIAL

  uncertainty_confidence:
    status: MODEL_COMPLETE

  failure_modes:
    status: MODEL_COMPLETE

  repair_recovery:
    status: MODEL_COMPLETE

  tests_validators:
    status: MODEL_COMPLETE_UNEXECUTED

  falsifiers:
    status: MODEL_COMPLETE

  gap_status:
    status: EXPLICIT_CRITICAL_GAPS_OPEN

  canonical_variable_registry:
    status: UNKNOWN_GAP

  executable_schema:
    status: UNKNOWN_GAP

  runtime_validation:
    status: UNKNOWN_GAP

  overall:
    status: COMPLETE_FOR_VARIABLE_CONTRACT_SCOPE

  conclusion_class:
    MODEL
```

---

# 53. Hard Boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

Variable-specific boundaries:

```text
PRIORITY != TRUTH

PRIORITY != CONFIDENCE

SALIENCE != EVIDENCE

NOVELTY != IMPORTANCE

REPETITION != INDEPENDENCE

ATTENTION != BELIEF

RESOURCE != AUTHORITY

AVAILABLE != ALLOCATED

ALLOCATED != EXECUTED

EXECUTED != VALIDATED

RECALLED != FRESH

LOCAL != GLOBAL

L != M != H

MODEL VARIABLE != CANONICAL VARIABLE

VARIABLE DEFINED != VARIABLE IMPLEMENTED

TYPE-CORRECT != SEMANTICALLY VALID

STATE UPDATE != AUTHORITATIVE COMMIT
```

---

# 54. Governing Variable Contract

> **`L02_ATTENTION` must represent attention as typed, provenance-bound, scope/regime/freshness-aware allocation state over scarce resources. Variables that describe salience, priority, uncertainty, evidence, confidence, capability, authority, and commit state must remain structurally distinct. No attention variable may acquire epistemic, causal, or governance meaning merely because it receives a high score or large allocation. Unknown canonical variable definitions remain `UNKNOWN/GAP`, and modeled variables remain `MODEL` until independently source-bound or implemented and validated.**

---

# 55. Canon Boundary

```text
SOURCE-SUPPORTED:

L02_ATTENTION is an attention-allocation primitive.

It concerns budgeting scarce reasoning/observation resources.

Its placeholder requires explicit variables and associated
state/invariant/dependency/provenance/test/governance treatment.


AMOS_MODEL:

candidate variables
resource tensors
allocation vectors
priority variables
salience variables
goal relevance
risk/consequence variables
uncertainty vector
evidence variables
confidence variables
provenance variables
dependency variables
scope variables
regime variables
freshness variables
H/M/L variables
memory variables
contradiction variables
COMPETING variables
decision-value variables
information-gain variables
cost variables
switching variables
authority variables
proposal/commit variables
state-version variables
failure variables
repair variables


UNKNOWN/GAP:

canonical L02 variable names
canonical variable registry
canonical domains
canonical units
canonical numeric scales
canonical thresholds
canonical weighting functions
canonical resource conversion rules
canonical state schema
executable implementation
runtime validation
```

Therefore:

```text
CONCLUSION CLASS:
MODEL

NOT:
CANONICAL VARIABLE REGISTRY

NOT:
IMPLEMENTED L02 STATE

NOT:
VALIDATED ATTENTION RUNTIME

NOT:
EMPIRICAL ATTENTION THEORY

NOT:
AUTHORITY TO COMMIT
```

```text
```

---

[[00_ROOT_MOC]]|[[AMOS MOC]]

---
**Related:** [[00_HOME]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: l02_attention_primitives_cognitive_matrix_variables
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L02_ATTENTION/L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_VARIABLES.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[L02_ATTENTION_MOC]]
