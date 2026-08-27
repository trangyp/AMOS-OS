---
title: L02 ATTENTION PRIMITIVES COGNITIVE MATRIX OPERATORS
type: cognitive
source: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L02_ATTENTION
tags: [cognitive_matrix, primitives, l02_attention, note, canon/cognitive-matrix]
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


The source placeholder explicitly defines L02 as **“attention allocation; budget scarce reasoning/observation resources”** and requires operators/kernels, invariants, H/M/L, interfaces, dependencies, provenance, repair, tests, governance, freshness, and version lineage before promotion. It also explicitly prohibits inventing missing canon or implementation status. 

---
tags:
  - amos
  - cognitive-matrix
  - l02
  - attention
  - operators
  - kernels
  - rscf
  - hml
  - governance

title: "L02_ATTENTION — Operators"
origin_architect: "Trang Phan"
status: "MODEL_SPECIFICATION / SOURCE-BOUNDED / UNVALIDATED"
epistemic_class: "MODEL"
runtime_alignment: "AMOS Full Brain OS / AMOS_CORE v4.4 lineage"
---

# L02_ATTENTION — Operators

**Class:** `COGNITIVE_PRIMITIVE_OPERATOR_CONTRACT`  
**Origin architect / steward:** Trang Phan  
**Primitive:** `L02_ATTENTION`  
**Artifact:** `OPERATORS.md`  
**Status:** `AMOS_MODEL / SOURCE-BOUNDED / UNVALIDATED`

> **Canon boundary:** the recovered L02 source establishes the primitive role as attention allocation over scarce reasoning/observation resources and explicitly requires an operator/kernel contract before promotion. It does not currently provide a canonical named L02 operator registry. Therefore operator names, signatures, transition equations, kernels, and protocols in this artifact are `AMOS_MODEL` unless independently recovered from direct canon or executable runtime evidence.

---

# 0. Purpose

Define the typed operators through which `L02_ATTENTION` may:

- receive attention candidates,
- admit or reject candidates,
- estimate attention relevance,
- rank eligible candidates,
- allocate finite attention resources,
- focus,
- defer,
- suspend,
- resume,
- reallocate,
- escalate,
- de-escalate,
- preserve provenance,
- respond to contradictions,
- react to stale dependencies,
- recover from failed allocation,
- and emit governed attention proposals.

The operator layer answers:

> **What transformations may L02 apply to attention state, under which preconditions, with which effects, and under which invariant and governance constraints?**

Core boundary:

```text
OPERATOR
!=
ARBITRARY TRANSFORMATION

ATTENTION OPERATOR
!=
TRUTH OPERATOR

ATTENTION OPERATOR
!=
AUTHORITY OPERATOR

OPERATOR RESULT
!=
COMMIT
```

---

# 1. Source / Canon References

## 1.1 Source-supported primitive role

The recoverable L02 source establishes:

```text
L02_ATTENTION
=
attention allocation;
budget scarce reasoning/observation resources
```

and explicitly requires:

```text
Operators / kernels
```

as part of the contract surface required before promotion.

The source also states that the placeholder:

```text
does not invent missing canon,
equations,
thresholds,
empirical claims,
or implementation status
```

Therefore:

```yaml
source_status:

  L02_attention_allocation:
    status: SOURCE_SUPPORTED

  scarce_reasoning_observation_budget:
    status: SOURCE_SUPPORTED

  requirement_for_operator_contract:
    status: SOURCE_SUPPORTED

  canonical_operator_names:
    status: UNKNOWN/GAP

  canonical_operator_signatures:
    status: UNKNOWN/GAP

  canonical_operator_order:
    status: UNKNOWN/GAP

  canonical_kernels:
    status: UNKNOWN/GAP

  executable_operator_runtime:
    status: UNKNOWN/GAP
```

## 1.2 Governing AMOS operator constraints

Applicable AMOS framework forms include:

### Hard admission

[
Admit(x)=\bigwedge_i HardInvariant_i(x)
]

### Confidence ceiling

[
Conf(C)\leq\min_i Conf(P_i)
]

### Selective invalidation

[
Invalid(p)
\Rightarrow
Invalidate(Descendants(p))
]

These constrain L02 operators but are not proof of canonical L02-specific operator names.

## 1.3 Related L02 artifacts

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
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README

L01_SENSING_OBSERVATION
```

---

# 2. Definition and Scope

An L02 operator is a typed transformation:

[
O:
(S_t,I,C)
\rightarrow
(S_{t+1},R)
]

where:

```text
O       = attention operator
S_t     = current attention state
I       = typed operator input
C       = applicable context/constraints
S_t+1   = proposed successor attention state
R       = operator result
```

The operator is admissible only when:

[
Preconditions(O,S_t,I,C)=true
]

and:

[
HardInvariants(S_{t+1})=true
]

or the transition must fail closed.

Scope includes:

```text
candidate admission
attention scoring
priority comparison
resource allocation
focus management
deferral
reallocation
escalation
de-escalation
freshness handling
dependency invalidation
memory interaction
provenance handling
repair
rollback proposal
```

Out of scope:

```text
truth determination
final causal inference
durable memory commit
external-effect authorization
policy override
unbounded tool execution
```

---

# 3. Operator Classes

```yaml
AttentionOperatorClass:

  INGESTION:
    meaning:
      accept or normalize candidate inputs

  ADMISSION:
    meaning:
      determine candidate eligibility

  ASSESSMENT:
    meaning:
      estimate attention-relevant dimensions

  PRIORITIZATION:
    meaning:
      rank or compare candidates

  ALLOCATION:
    meaning:
      assign bounded cognitive resources

  FOCUS:
    meaning:
      activate or sustain processing

  DEFERRAL:
    meaning:
      preserve candidate without current allocation

  ESCALATION:
    meaning:
      move unresolved decision-relevant state upward

  DEESCALATION:
    meaning:
      reduce attention when additional processing has low value

  INVALIDATION:
    meaning:
      withdraw attention effects dependent on failed premises

  MEMORY:
    meaning:
      interact with attention-supporting retained state

  REPAIR:
    meaning:
      restore valid attention operation

  GOVERNANCE:
    meaning:
      produce or consume control-plane validation state
```

---

# 4. Typed Operator Contract

```yaml
AttentionOperator:

  operator_id:
    type: OperatorId

  operator_class:
    type: AttentionOperatorClass

  input_types:
    type: TypeRef[]

  output_types:
    type: TypeRef[]

  preconditions:
    type: InvariantRef[]

  hard_invariants:
    type: InvariantRef[]

  reads:
    type: StateRef[]

  writes:
    type: StateRef[]

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef

  hml:
    type: HMLContext

  provenance_requirements:
    type: ProvenanceRequirement[]

  authority_requirement:
    type: AuthorityRequirement

  reversibility:
    type:
      - REVERSIBLE
      - CONDITIONALLY_REVERSIBLE
      - IRREVERSIBLE

  result_class:
    type:
      - PROPOSAL
      - LOCAL_STATE
      - VALIDATION_REQUEST
      - ESCALATION_REQUEST
      - UNKNOWN_GAP

  failure_modes:
    type: FailureModeRef[]

  repair:
    type: RepairRef[]
```

---

# 5. Typed Inputs

```yaml
AttentionOperatorInput:

  candidates:
    type: AttentionCandidate[]

  active_objective:
    type: GoalRef | UNKNOWN

  attention_state:
    type: AttentionState

  budget:
    type: AttentionBudget

  constraints:
    type: ConstraintContext

  evidence:
    type: EvidenceBundle

  provenance:
    type: ProvenanceBundle

  dependencies:
    type: DependencyGraph

  uncertainty:
    type: UncertaintyVector

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef

  hml:
    type: HMLContext

  freshness:
    type: FreshnessState

  authority:
    type: AuthorityContext | UNKNOWN
```

---

# 6. Typed Outputs

```yaml
AttentionOperatorOutput:

  attention_state:
    type: AttentionState

  candidate_results:
    type: AttentionCandidateResult[]

  allocation_proposal:
    type: AttentionAllocationProposal | null

  deferred:
    type: CandidateRef[]

  quarantined:
    type: CandidateRef[]

  invalidated:
    type: CandidateRef[]

  escalation:
    type: EscalationRequest | null

  repair:
    type: RepairProposal | null

  provenance:
    type: ProvenanceBundle

  uncertainty:
    type: UncertaintyVector

  confidence_ceiling:
    type: ConfidenceBound

  status:
    type:
      - PASS
      - PARTIAL
      - BLOCKED
      - REVALIDATE
      - QUARANTINE
      - ESCALATE
      - UNKNOWN_GAP
```

---

# 7. State Variables

```text
X_t       = candidate attention set
E_t       = eligible candidate set
A_t       = active allocation state
B_t       = attention budget state
G_t       = governing objective
C_t       = constraint state
D_t       = dependency state
U_t       = uncertainty state
P_t       = provenance state
F_t       = freshness state
S_t       = scope
R_t       = regime
HML_t     = active scale context
Q_t       = quarantined candidate set
Def_t     = deferred candidate set
Comp_t    = competing-hypothesis state
Contr_t   = contradiction state
Mem_t     = attention-supporting memory state
```

---

# 8. Core Operator Registry

The following operators form the proposed L02 model registry.

```text
INGEST()
NORMALIZE()
ADMIT()
REJECT()
QUARANTINE()

ASSESS_RELEVANCE()
ASSESS_SALIENCE()
ASSESS_UNCERTAINTY()
ASSESS_CONSEQUENCE()
ASSESS_DEPENDENCY_CRITICALITY()
ASSESS_TIME_SENSITIVITY()
ASSESS_INFORMATION_VALUE()
ASSESS_COST()

RANK()
COMPARE()
SELECT()

ALLOCATE()
RESERVE()
FOCUS()
SUSTAIN()
SHIFT()
RELEASE()

DEFER()
RESUME()

ESCALATE()
DEESCALATE()

CHECK_FRESHNESS()
REVALIDATE()

INVALIDATE()
REALLOCATE()

RECALL()
EXTERNALIZE_MEMORY()

REPAIR()
ROLLBACK_PROPOSE()

EMIT_PROPOSAL()
```

All names above are `AMOS_MODEL` until directly recovered.

---

# 9. `INGEST()`

## Purpose

Receive candidate objects from upstream observation, reasoning, memory, tool, or control-plane sources.

Signature:

[
INGEST:
InputObject[]
\rightarrow
AttentionCandidate[]
]

Candidate:

```yaml
INGEST:

  reads:
    - incoming_objects

  writes:
    - candidate_buffer

  preconditions:
    - input_type_recognized

  effects:
    - candidate_registered
    - source_ref_preserved

  forbidden:
    - truth_promotion
    - authority_promotion
```

Hard boundary:

```text
INGESTED
!=
ADMITTED
```

---

# 10. `NORMALIZE()`

## Purpose

Convert heterogeneous candidates into a comparable typed attention representation.

[
NORMALIZE(x)
\rightarrow
x'
]

Normalization may align:

```text
candidate type
scope
regime
H/M/L coordinate
resource-cost representation
provenance reference
dependency references
```

It may not erase semantic differences.

Hard invariant:

```text
NORMALIZATION
!=
SEMANTIC COLLAPSE
```

---

# 11. `ADMIT()`

## Purpose

Determine whether a candidate is eligible to enter ordinary attention allocation.

[
Admit(x)
========

\bigwedge_i HardInvariant_i(x)
]

Result:

```yaml
ADMIT:
  result:
    - ADMITTED
    - BLOCKED
    - QUARANTINED
    - UNKNOWN_GAP
```

Hard boundary:

```text
HIGH PRIORITY
cannot compensate for
FAILED HARD INVARIANT
```

---

# 12. `REJECT()`

## Purpose

Remove a candidate from the active admissible set when a non-recoverable incompatibility is established for the current scope/regime.

```text
REJECT
!=
DELETE FROM HISTORY
```

Rejected candidates should retain sufficient provenance to explain the decision.

---

# 13. `QUARANTINE()`

## Purpose

Isolate a candidate whose integrity cannot currently be established.

Triggers may include:

```text
missing provenance
contaminated source
ambiguous scope
conflicting identity
revoked evidence
unknown authority
unresolved critical contradiction
```

Formally:

[
IntegrityUnknown(x)
\Rightarrow
QUARANTINE(x)
]

where continuing ordinary processing would be unsafe.

---

# 14. `ASSESS_RELEVANCE()`

## Purpose

Estimate candidate relevance to the governing objective.

[
Rel_i
=====

f(x_i,G_t)
]

This is `AMOS_MODEL`.

Important:

```text
RELEVANCE
!=
TRUTH
```

A false hypothesis may be highly relevant because falsifying it changes the decision.

---

# 15. `ASSESS_SALIENCE()`

## Purpose

Estimate how strongly a candidate stands out.

Possible contributors:

```text
novelty
frequency
contrast
threat signal
recency
user emphasis
system alerting
```

Hard boundary:

```text
SALIENCE
!=
PRIORITY
```

Salience is one attention signal, not the governing result.

---

# 16. `ASSESS_UNCERTAINTY()`

## Purpose

Estimate unresolved uncertainty associated with a candidate.

Output should distinguish where possible:

```text
evidence uncertainty
model uncertainty
scope uncertainty
temporal uncertainty
causal uncertainty
execution uncertainty
provenance-independence uncertainty
```

Hard boundary:

```text
HIGH UNCERTAINTY
!=
AUTOMATIC HIGH PRIORITY
```

---

# 17. `ASSESS_CONSEQUENCE()`

## Purpose

Estimate potential consequence if a candidate is ignored, misunderstood, delayed, or acted upon incorrectly.

Candidate factors:

```text
impact
irreversibility
downstream dependency
safety
financial/legal exposure
systemic radius
recoverability window
```

This is a governance input, not an empirical universal formula.

---

# 18. `ASSESS_DEPENDENCY_CRITICALITY()`

## Purpose

Estimate whether a candidate is load-bearing for other active claims or decisions.

Candidate model:

[
Criticality(x)
==============

f(
DescendantImpact(x),
FailureSensitivity(x)
)
]

Hard boundary:

```text
HIGH GRAPH DEGREE
!=
HIGH EPISTEMIC CRITICALITY
```

---

# 19. `ASSESS_TIME_SENSITIVITY()`

## Purpose

Estimate temporal urgency.

Possible factors:

```text
deadline
freshness decay
regime transition
recoverability window
latency
event timing
commit deadline
```

Hard boundary:

```text
URGENT
!=
IMPORTANT
```

---

# 20. `ASSESS_INFORMATION_VALUE()`

## Purpose

Estimate whether additional attention can materially reduce decision-changing uncertainty.

Candidate:

[
EIV(x)
======

ExpectedDecisionValue(
AdditionalProcessing(x)
)
]

The exact numeric model remains unresolved.

---

# 21. `ASSESS_COST()`

## Purpose

Estimate expected cost of allocating more attention.

Possible resource axes:

```text
tokens
time
compute
tool calls
retrieval cost
agent calls
human review
context pressure
switching cost
```

Resource units must remain typed.

---

# 22. `RANK()`

## Purpose

Order eligible candidates by attention priority.

Generic model:

[
\pi_i
=====

F(
Rel_i,
Criticality_i,
Consequence_i,
Uncertainty_i,
Time_i,
InformationValue_i,
Cost_i,
Salience_i
)
]

No canonical weighting is asserted.

Input:

```text
eligible candidates
```

Output:

```text
ordered priority state
```

Hard boundary:

```text
RANK
!=
AUTHORIZE
```

---

# 23. `COMPARE()`

## Purpose

Compare two or more candidates when a complete total ranking is unnecessary.

[
COMPARE(x_i,x_j)
\rightarrow
{
i>j,
j>i,
EQUIVALENT,
INCOMPARABLE,
UNKNOWN
}
]

`INCOMPARABLE` is valid when candidates use incompatible resource, scope, or consequence dimensions.

Do not force a numeric comparison where semantics do not support it.

---

# 24. `SELECT()`

## Purpose

Select candidates for potential resource allocation.

[
SELECT(E_t,\Pi_t,B_t)
\rightarrow
S_t
]

Selection does not allocate resources yet.

```text
SELECTED
!=
ALLOCATED
```

---

# 25. `ALLOCATE()`

## Purpose

Assign bounded cognitive resources to selected candidates.

[
ALLOCATE(S_t,B_t)
\rightarrow
A_t
]

subject to:

[
\sum_i a_i
\le
B_t
]

for compatible resource units.

Allocation output remains an attention-state proposal where authoritative state commit is governed externally.

---

# 26. `RESERVE()`

## Purpose

Protect a portion of the attention budget for unforeseen decision-relevant events.

[
B_{available}
=============

## B_{total}

## B_{reserved}

B_{used}
]

Reserve may support:

```text
contradiction response
new evidence
repair
regime shift
user correction
critical gap discovery
tool failure
```

---

# 27. `FOCUS()`

## Purpose

Move a candidate into active processing.

[
FOCUS(x_i)
\Rightarrow
Active(x_i)
]

provided:

```text
candidate admitted
allocation exists
constraints pass
```

Hard boundary:

```text
FOCUS
!=
BELIEVE
```

---

# 28. `SUSTAIN()`

## Purpose

Continue allocating attention to an active candidate.

A sustain decision should require continued expected value.

Candidate:

[
Continue(x)
===========

EIV_{next}(x)

>

Cost_{next}(x)
]

as an `AMOS_MODEL` heuristic.

If no longer decision-relevant:

```text
RELEASE or DEFER
```

---

# 29. `SHIFT()`

## Purpose

Move attention from one candidate or branch to another.

[
SHIFT(x_i,x_j)
]

should account for:

```text
switching cost
unfinished dependencies
critical state preservation
memory/recovery cost
```

Frequent unnecessary switching is an attention-thrashing failure mode.

---

# 30. `RELEASE()`

## Purpose

Return unused attention resources to the available budget.

[
B_{available}' =
B_{available} + Released
]

for compatible units.

Release does not delete provenance or history.

---

# 31. `DEFER()`

## Purpose

Remove a candidate from immediate processing while retaining enough state for later resumption.

```text
ACTIVE
→
DEFERRED
```

Required retention may include:

```text
candidate ID
reason for deferral
remaining gap
provenance
scope
regime
freshness condition
dependencies
```

---

# 32. `RESUME()`

## Purpose

Return deferred attention work to active consideration.

Precondition:

```text
candidate still applicable
dependencies sufficiently valid
scope/regime compatible
freshness acceptable or revalidated
```

Hard boundary:

```text
RESUME
!=
ASSUME OLD PRIORITY STILL VALID
```

---

# 33. `ESCALATE()`

## Purpose

Move a local/subsystem attention issue to a higher governance or reasoning level.

Triggers may include:

```text
critical contradiction
authority ambiguity
hard constraint conflict
scope mismatch
regime shift
critical dependency failure
high irreversibility
resource exhaustion
unbounded uncertainty
cross-subsystem consequence
```

H/M/L example:

```text
L
→
M
→
H
```

Escalation changes who/what must reason about the issue.

It does not itself authorize external action.

---

# 34. `DEESCALATE()`

## Purpose

Reduce reasoning depth after decision-changing uncertainty has been sufficiently resolved.

Possible transition:

```text
C4 → C3 → C2 → C1 → C0
```

or:

```text
H → M → L
```

depending on architecture.

Hard invariant:

```text
DEESCALATION
cannot hide unresolved critical gaps.
```

---

# 35. `CHECK_FRESHNESS()`

## Purpose

Determine whether mutable load-bearing state remains valid for current use.

[
Fresh(x,t)
]

may depend on:

```text
age
state version
environment
regime
source update
revocation
authority epoch
```

Result:

```text
FRESH
STALE
UNKNOWN
```

---

# 36. `REVALIDATE()`

## Purpose

Re-establish validity after freshness, regime, scope, dependency, provenance, or authority changes.

```text
STALE
→
REVALIDATE
→
VALID / INVALID / UNKNOWN
```

Hard boundary:

```text
REVALIDATE
!=
REUSE OLD CONCLUSION
```

---

# 37. `INVALIDATE()`

## Purpose

Withdraw validity from state dependent on failed premises.

Core rule:

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

unless dependency closure proves (p) globally load-bearing.

---

# 38. `REALLOCATE()`

## Purpose

Redistribute attention resources after state change.

[
A_{t+1}
=======

REALLOCATE(
A_t,
\Delta Evidence,
\Delta Goal,
\Delta Risk,
\Delta Regime,
\Delta Dependency
)
]

Possible triggers:

```text
new evidence
candidate completion
failed dependency
priority change
budget change
authority change
regime shift
critical gap discovery
```

---

# 39. `RECALL()`

## Purpose

Retrieve attention-supporting memory.

Hard boundaries:

```text
RECALL
!=
TRUTH

RECALL
!=
FRESHNESS

RECALL
!=
REVALIDATION
```

A recalled priority should normally be treated as prior state, not automatically current state.

---

# 40. `EXTERNALIZE_MEMORY()`

## Purpose

Propose moving attention-relevant state from active context to a persistent memory substrate.

Possible targets:

```text
attention history
deferred branches
unresolved gaps
decision rationale
failed paths
provenance references
```

Output:

```text
MemoryWriteProposal
```

not:

```text
DurableMemoryCommit
```

---

# 41. `REPAIR()`

## Purpose

Restore valid attention operation after a detected failure.

General pattern:

```text
detect failed premise/operator
↓
localize affected state
↓
freeze affected descendants
↓
preserve unaffected branches
↓
repair smallest failing element
↓
revalidate affected closure
↓
resume
```

Repair itself must respect L02 repair and control-plane contracts.

---

# 42. `ROLLBACK_PROPOSE()`

## Purpose

Propose restoration to the nearest valid attention state when local repair is insufficient.

[
S_{rollback}
============

NearestValidAncestor(S_{failed})
]

subject to:

```text
objective compatibility
dependency validity
scope/regime compatibility
budget consistency
authority compatibility
```

The operator proposes rollback.

Authoritative rollback commit belongs to the appropriate control plane.

---

# 43. `EMIT_PROPOSAL()`

## Purpose

Produce a governed downstream attention or action-related proposal.

Example:

```yaml
AttentionProposal:

  candidate_refs: []

  allocations: []

  deferred: []

  unresolved_gaps: []

  scope: null
  regime: null

  evidence: []
  provenance: []

  authority_required: false

  confidence_ceiling: 0

  falsifiers: []
```

Hard boundary:

```text
EMIT_PROPOSAL()
!=
COMMIT()
```

---

# 44. Composite Attention Kernel

A candidate L02 processing kernel is:

```text
INGEST
↓
NORMALIZE
↓
ADMIT
↓
ASSESS
↓
RANK / COMPARE
↓
SELECT
↓
ALLOCATE
↓
FOCUS
↓
OBSERVE RESULT
↓
SUSTAIN / SHIFT / RELEASE
↓
DEFER / ESCALATE / COMPLETE
↓
REVALIDATE WHEN STATE CHANGES
```

This is `AMOS_MODEL`.

It must not be labelled canonical without source evidence.

---

# 45. Formal Kernel Representation

Let:

[
K_{L02}
=======

O_n\circ O_{n-1}\circ\dots\circ O_1
]

where each (O_i) is an admissible L02 operator.

Kernel validity requires:

[
Valid(K_{L02})
==============

\bigwedge_i
ValidTransition(O_i)
]

and:

[
Invariant(S_0)
\land
\bigwedge_i PreserveInvariant(O_i)
\Rightarrow
Invariant(S_n)
]

where no unresolved required check is silently interpreted as `true`.

---

# 46. Operator Preconditions

Every operator should declare preconditions.

Example:

```yaml
ALLOCATE:

  preconditions:
    - candidate_set_resolved
    - candidates_admitted
    - budget_known
    - scope_known
    - regime_known
    - hard_constraints_pass

  conditional_preconditions:
    - provenance_valid_if_material
    - authority_valid_if_governed_effect

  failure_result:
    - BLOCKED
    - REVALIDATE
    - UNKNOWN_GAP
```

---

# 47. Operator Postconditions

Example:

```yaml
ALLOCATE:

  postconditions:
    - total_allocation_within_budget
    - allocation_provenance_recorded
    - HML_identity_preserved
    - deferred_candidates_retained
    - confidence_ceiling_preserved
    - no_authority_promotion
```

---

# 48. Operator Invariants

```text
L02-OP-INV-001
Operators must consume and emit typed state.

L02-OP-INV-002
Operators may not silently change epistemic class.

L02-OP-INV-003
Operators may not silently expand scope.

L02-OP-INV-004
Operators may not silently change regime.

L02-OP-INV-005
Operators must preserve provenance where material.

L02-OP-INV-006
Hard failures are non-compensatory.

L02-OP-INV-007
Allocation cannot exceed available typed budget.

L02-OP-INV-008
Priority cannot grant authority.

L02-OP-INV-009
Attention cannot establish truth.

L02-OP-INV-010
Attention cannot establish causation.

L02-OP-INV-011
Unknown state cannot silently become PASS.

L02-OP-INV-012
Invalidation propagates only through actual descendants.

L02-OP-INV-013
Independent unaffected state must survive local failure.

L02-OP-INV-014
Contradictions must remain visible.

L02-OP-INV-015
COMPETING hypotheses remain competing until discriminated.

L02-OP-INV-016
H/M/L identity must survive cross-scale operators.

L02-OP-INV-017
Memory recall cannot renew freshness automatically.

L02-OP-INV-018
Proposal-producing operators cannot perform durable commit.

L02-OP-INV-019
Operator composition cannot weaken governing invariants.

L02-OP-INV-020
Model operator definitions cannot be promoted to canon without evidence.
```

---

# 49. Dependencies

Core dependencies may include:

```yaml
dependencies:

  upstream:
    - L01_SENSING_OBSERVATION

  within_L02:
    - L02_ATTENTION_DEFINITION
    - L02_ATTENTION_VARIABLES
    - L02_ATTENTION_STATE
    - L02_ATTENTION_INVARIANTS
    - L02_ATTENTION_DEPENDENCIES
    - L02_ATTENTION_EQUATIONS
    - L02_ATTENTION_HML
    - L02_ATTENTION_MEMORY
    - L02_ATTENTION_PROVENANCE
    - L02_ATTENTION_CONTROL_PLANES

  infrastructure:
    - constraint_state
    - provenance_state
    - authority_state
    - freshness_state
    - scope_state
    - regime_state
```

Potential downstream primitive relationships remain `UNKNOWN/GAP` unless directly recovered.

---

# 50. H/M/L Applicability

## H — Governing Operators

Candidate H-level operations:

```text
SET_GOVERNING_ATTENTION_SCOPE
IDENTIFY_CRITICAL_GAPS
IDENTIFY_SYSTEM_RISK
SET_RESOURCE_ENVELOPE
ESCALATE_GOVERNING_CONFLICT
DEESCALATE_AFTER_SUFFICIENCY
```

H-level operators should primarily shape constraints and attention envelopes.

## M — Allocation Operators

Primary M operators:

```text
ADMIT
ASSESS
RANK
COMPARE
SELECT
ALLOCATE
RESERVE
REALLOCATE
ESCALATE
```

## L — Local Attention Operators

Primary L operators:

```text
FOCUS
SUSTAIN
SHIFT
RELEASE
DEFER
RESUME
CHECK_FRESHNESS
REVALIDATE
INVALIDATE
RECALL
```

Hard boundary:

```text
L OPERATOR
cannot silently mutate
H GOVERNING OBJECTIVE.
```

---

# 51. Cross-Scale Operators

Candidate:

```text
PROJECT_H_TO_M()
ALLOCATE_M_TO_L()
AGGREGATE_L_TO_M()
ESCALATE_M_TO_H()
```

Rules:

```text
H→M:
preserve hard constraints

M→L:
preserve budget bounds

L→M:
preserve evidence/provenance

M→H:
escalate only decision-relevant changes
```

---

# 52. Control-Plane Requirements

L02 operators may manage reversible attention state locally where permitted.

The infrastructure/control plane should own or validate operations involving:

```text
durable state
persistent memory writes
external effects
authority changes
policy changes
cross-recipient disclosure
irreversible actions
constraint overrides
commit-time finalization
```

Operator ownership matrix:

| Operator             | L02 may propose |     L02 may locally apply | Control-plane commit required |
| -------------------- | --------------: | ------------------------: | ----------------------------: |
| `RANK`               |             Yes |                       Yes |                            No |
| `COMPARE`            |             Yes |                       Yes |                            No |
| `DEFER`              |             Yes |                   Usually |             Context-dependent |
| `ALLOCATE`           |             Yes |               Conditional | If authoritative shared state |
| `ESCALATE`           |             Yes |                       Yes |    No external effect implied |
| `INVALIDATE`         |             Yes |               Conditional |       If durable/shared state |
| `EXTERNALIZE_MEMORY` |             Yes |         No durable commit |                           Yes |
| `ROLLBACK_PROPOSE`   |             Yes | No authoritative rollback |                           Yes |
| external action      |   Proposal only |                        No |                           Yes |

This ownership matrix is `AMOS_MODEL`.

---

# 53. Agents

Candidate logical roles:

```text
L02_OPERATOR_ROUTER
L02_ADMISSION_AGENT
L02_PRIORITY_AGENT
L02_ALLOCATION_AGENT
L02_FRESHNESS_AGENT
L02_DEPENDENCY_AGENT
L02_ESCALATION_AGENT
L02_OPERATOR_AUDITOR
L02_REPAIR_AGENT
```

These are role abstractions.

They do not prove separate runtime deployments.

---

# 54. Skills

Potential capability mappings:

```text
AMOS Attention Allocation Governor
AMOS Context Budget Governor RSCF
AMOS Constraint Propagation RSCF Engine
AMOS Cross-Scale RSCF Tensor Engine
AMOS Provenance Trust Firewall
AMOS Metacognitive Confidence Auditor
AMOS Context State Maintenance RSCF
AMOS Infrastructure Control Plane
AMOS RSCF Modeler
```

Hard boundary:

```text
OPERATOR CAN CALL SKILL
!=
OPERATOR HAS UNBOUNDED AUTHORITY
```

---

# 55. Standard Workflow

```text
1. INGEST candidates

2. NORMALIZE candidate types

3. ADMIT under hard invariants

4. ASSESS:
   relevance
   consequence
   uncertainty
   dependency criticality
   time sensitivity
   information value
   cost
   salience

5. RANK / COMPARE

6. SELECT candidates

7. CHECK budget

8. ALLOCATE bounded resources

9. FOCUS selected targets

10. SUSTAIN while additional processing remains valuable

11. SHIFT / DEFER when priorities change

12. ESCALATE material unresolved conflicts

13. RELEASE completed resources

14. CHECK freshness before reuse

15. INVALIDATE affected descendants when premises fail

16. REALLOCATE

17. REPAIR when transition/invariant failure occurs

18. EMIT proposal where downstream governance is required
```

---

# 56. Protocols

Operator invocation envelope:

```yaml
AttentionOperatorInvocation:

  invocation_id: null

  operator_id: null

  primitive: L02_ATTENTION

  actor:
    agent_id: null
    capability: null

  state:
    attention_state_id: null
    version: null
    hash: null

  inputs: []

  scope: null
  regime: null
  hml: null

  budget:
    requested: null
    available: null
    units: null

  authority:
    required: null
    witness: null

  provenance: []

  expected_effects: []

  reversibility: null

  result_class:
    value: PROPOSAL
```

Operator result envelope:

```yaml
AttentionOperatorResult:

  invocation_id: null

  operator_id: null

  status: null

  outputs: []

  new_state_proposal: null

  invariant_results: []

  budget_delta: null

  invalidated_dependencies: []

  gaps: []

  competing: []

  falsifiers: []

  provenance: []

  confidence_ceiling: 0

  commit_status:
    value: NOT_COMMITTED
```

---

# 57. Evidence / Provenance

Every consequential operator execution should preserve:

```text
operator identity
operator version
input state identity
output state identity/proposal
actor
capability
authority state
source evidence
dependencies read
scope
regime
H/M/L coordinate
budget before
budget after
invariant checks
timestamp
failure result
repair/rollback lineage
```

Candidate provenance tensor:

[
P_O
===

T[
operator,
actor,
input,
output,
reads,
writes,
scope,
regime,
HML,
authority,
time
]
]

This is `AMOS_MODEL`.

---

# 58. Read-Set Discipline

Where mutable state influences an operator decision:

```text
record exact state actually read
```

Candidate observed read:

```yaml
ObservedRead:

  object_id: null
  version: null
  content_hash: null
  semantic_role: null
```

Commit-sensitive operators should not rely solely on one global state hash if fine-grained read identity is available.

---

# 59. Freshness

Operator results inherit freshness limits from load-bearing state.

If:

[
Fresh(p)=false
]

and operator result depends on (p):

[
Fresh(Result_O)=false
]

until revalidated.

Hard boundary:

```text
CACHED OPERATOR RESULT
!=
CURRENT VALID RESULT
```

---

# 60. Confidence Ceiling

For operator result (R_O):

[
Conf(R_O)
\le
\min_i Conf(P_i)
]

for load-bearing premises (P_i).

An operator's deterministic execution does not prove the validity of its inputs.

```text
DETERMINISTIC TRANSFORMATION
OF
BAD INPUT
=
DETERMINISTIC BAD OUTPUT
```

---

# 61. Failure Modes

```text
FM-L02-OP-001   Invalid Input Type
FM-L02-OP-002   Missing Required Input
FM-L02-OP-003   Operator Applied Outside Scope
FM-L02-OP-004   Operator Applied Outside Regime
FM-L02-OP-005   Stale Input
FM-L02-OP-006   Provenance Loss
FM-L02-OP-007   Budget Overflow
FM-L02-OP-008   Negative Allocation
FM-L02-OP-009   Salience/Priority Collapse
FM-L02-OP-010   Priority/Truth Collapse
FM-L02-OP-011   Priority/Authority Collapse
FM-L02-OP-012   Attention/Causality Collapse
FM-L02-OP-013   Unknown-As-Pass
FM-L02-OP-014   Hard-Invariant Compensation
FM-L02-OP-015   HML Scale Collapse
FM-L02-OP-016   Hidden Dependency
FM-L02-OP-017   Over-Invalidation
FM-L02-OP-018   Under-Invalidation
FM-L02-OP-019   Contradiction Suppression
FM-L02-OP-020   COMPETING Collapse
FM-L02-OP-021   Attention Thrashing
FM-L02-OP-022   Infinite Sustain
FM-L02-OP-023   Premature Release
FM-L02-OP-024   Invalid Resume
FM-L02-OP-025   Unjustified Escalation
FM-L02-OP-026   Missed Escalation
FM-L02-OP-027   Memory Recall Treated Fresh
FM-L02-OP-028   Operator Self-Authorization
FM-L02-OP-029   Proposal/Commit Collapse
FM-L02-OP-030   Repair Without Revalidation
FM-L02-OP-031   Retry Without Changed Evidence
FM-L02-OP-032   Operator Sequence Drift
FM-L02-OP-033   Model Operator Reported as Canon
```

---

# 62. Repair / Recovery

General operator repair:

```text
DETECT operator failure
↓
FREEZE affected transition
↓
IDENTIFY failed precondition/invariant
↓
TRACE dependent state
↓
PRESERVE unaffected branches
↓
REPAIR smallest failed element
↓
REVALIDATE inputs
↓
REEXECUTE only affected operator chain
↓
VALIDATE outputs
↓
RESTORE state
```

If repair cannot establish safety:

```text
QUARANTINE
or
ROLLBACK_PROPOSE
or
ESCALATE
or
UNKNOWN/GAP
```

---

# 63. Operator Rollback

Where an operator modifies reversible local attention state:

[
Rollback(O,S_{t+1})
\rightarrow
S_t
]

where prior state remains valid.

For multi-operator chains:

```text
O1
→ O2
→ O3
→ O4 failure
```

rollback should target:

```text
nearest valid state
```

rather than automatically resetting all of L02.

---

# 64. Tests / Validators

Required validators:

```text
VALIDATE_OPERATOR_ID
VALIDATE_OPERATOR_CLASS
VALIDATE_INPUT_TYPES
VALIDATE_OUTPUT_TYPES
VALIDATE_PRECONDITIONS
VALIDATE_POSTCONDITIONS
VALIDATE_HARD_INVARIANTS
VALIDATE_BUDGET
VALIDATE_SCOPE
VALIDATE_REGIME
VALIDATE_FRESHNESS
VALIDATE_PROVENANCE
VALIDATE_DEPENDENCIES
VALIDATE_HML
VALIDATE_AUTHORITY
VALIDATE_READ_SET
VALIDATE_REVERSIBILITY
VALIDATE_PROPOSAL_COMMIT_SEPARATION
VALIDATE_REPAIR
VALIDATE_ROLLBACK
```

---

# 65. Minimum Test Suite

```text
TEST-L02-OP-001
INGEST preserves source identity.

TEST-L02-OP-002
INGEST does not imply ADMIT.

TEST-L02-OP-003
ADMIT fails when a hard invariant fails.

TEST-L02-OP-004
High priority cannot override failed admission.

TEST-L02-OP-005
RANK cannot alter epistemic class.

TEST-L02-OP-006
SALIENCE cannot automatically determine top rank.

TEST-L02-OP-007
ALLOCATE cannot exceed available typed budget.

TEST-L02-OP-008
ALLOCATE does not authorize external action.

TEST-L02-OP-009
FOCUS on a hypothesis does not make it true.

TEST-L02-OP-010
DEFER preserves provenance and unresolved state.

TEST-L02-OP-011
RESUME stale work triggers freshness check.

TEST-L02-OP-012
ESCALATE preserves H/M/L identity.

TEST-L02-OP-013
INVALIDATE removes dependent descendants only.

TEST-L02-OP-014
Independent branches survive local invalidation.

TEST-L02-OP-015
RECALL does not renew freshness automatically.

TEST-L02-OP-016
EXTERNALIZE_MEMORY produces proposal, not commit.

TEST-L02-OP-017
ROLLBACK_PROPOSE does not self-finalize rollback.

TEST-L02-OP-018
UNKNOWN precondition cannot return PASS.

TEST-L02-OP-019
Operator composition preserves contradictions.

TEST-L02-OP-020
Operator composition preserves COMPETING hypotheses.

TEST-L02-OP-021
Operator execution preserves scope/regime.

TEST-L02-OP-022
Deterministic operator on invalid input cannot be reported as validated output.

TEST-L02-OP-023
Repair reruns only affected chain where dependency closure is bounded.

TEST-L02-OP-024
Unexecuted operator test remains UNEXECUTED.

TEST-L02-OP-025
AMOS_MODEL operator cannot be reported as canonical L02 operator.
```

---

# 66. Adversarial Tests

Test operator integrity against:

```text
malformed candidates
missing provenance
fake priority
salience flooding
duplicate-source flooding
budget exhaustion
scope injection
regime injection
stale state replay
authority spoofing
dependency hiding
contradiction suppression
operator reordering
double allocation
duplicate commit attempts
memory poisoning
rollback tampering
UNKNOWN→PASS coercion
```

---

# 67. Falsifiers

Revise this artifact if direct canon establishes that:

```text
L02 uses materially different operators

one or more listed functions belong canonically to another primitive

L02 does not perform ranking

L02 does not perform allocation

attention budgeting occurs exclusively outside L02

H/M/L does not apply to operator execution

memory interaction is excluded from L02

canonical control-plane ownership differs

canonical operator order is incompatible

runtime evidence validates a materially different kernel
```

An individual operator specification is falsified if executable evidence demonstrates that the operator cannot preserve its declared contract under the claimed scope.

---

# 68. Competing Operator Architectures

## COMPETING-001 — Minimal Primitive

```text
ADMIT
RANK
ALLOCATE
FOCUS
RELEASE
```

L02 owns only minimal attention allocation.

## COMPETING-002 — Full Cognitive Attention Runtime

```text
INGEST
NORMALIZE
ASSESS
RANK
ALLOCATE
FOCUS
SHIFT
DEFER
REVALIDATE
INVALIDATE
REPAIR
```

L02 owns broad attention lifecycle management.

## COMPETING-003 — Infrastructure-Mediated

```text
L02:
ASSESS
RANK
PROPOSE

INFRASTRUCTURE:
ADMIT
ALLOCATE
COMMIT
INVALIDATE
```

## COMPETING-004 — Hybrid

```text
L02 locally controls reversible cognitive attention

higher AMOS control plane governs:
shared budget
persistent state
cross-agent allocation
external effects
```

Current best model:

```text
COMPETING-004
```

but this remains `MODEL / COMPETING` until canonical ownership is resolved.

---

# 69. Gap Matrix

```yaml
gap_status:

  primitive_attention_role:
    status: SOURCE_SUPPORTED

  scarcity_basis:
    status: SOURCE_SUPPORTED

  operator_contract_required:
    status: SOURCE_SUPPORTED

  INGEST:
    status: MODEL_DEFINED

  NORMALIZE:
    status: MODEL_DEFINED

  ADMIT:
    status: FRAMEWORK_SUPPORTED / MODEL_BOUND

  ASSESS:
    status: MODEL_DEFINED

  RANK:
    status: MODEL_DEFINED

  ALLOCATE:
    status: MODEL_DEFINED

  FOCUS:
    status: MODEL_DEFINED

  DEFER:
    status: MODEL_DEFINED

  ESCALATE:
    status: MODEL_DEFINED

  REVALIDATE:
    status: MODEL_DEFINED

  INVALIDATE:
    status: FRAMEWORK_SUPPORTED / MODEL_BOUND

  REPAIR:
    status: MODEL_DEFINED

  canonical_operator_names:
    status: UNKNOWN/GAP

  canonical_operator_signatures:
    status: UNKNOWN/GAP

  canonical_operator_sequence:
    status: UNKNOWN/GAP

  canonical_attention_kernel:
    status: UNKNOWN/GAP

  canonical_control_plane_ownership:
    status: UNKNOWN/GAP

  runtime_operator_implementation:
    status: UNKNOWN/GAP

  executed_operator_tests:
    status: UNKNOWN/GAP

  formal_operator_verification:
    status: UNKNOWN/GAP
```

Critical gaps:

```text
1. canonical L02 operator registry
2. canonical operator ownership
3. executable operator implementation
4. operator/state correspondence
5. executed negative tests
```

---

# 70. Cheapest Discriminating Evidence

Highest-value retrieval order:

```text
1. Direct canonical L02 OPERATORS / kernel source

2. Direct L02 STATE source

3. Direct L02 VARIABLES source

4. Direct L02 INVARIANTS source

5. Cognitive-matrix runtime routing

6. AMOS Full Brain OS operator registry

7. AMOS_CORE v4.4 executable code

8. Runtime execution traces

9. Executed negative/invariant tests
```

The decisive architectural question is:

> **Does canonical L02 itself own admission, allocation, invalidation, and attention-state mutation, or does it primarily score/propose while the AMOS infrastructure control plane owns authoritative state transitions?**

---

# 71. RSCF Completion State

```yaml
rscf:

  id: L02_ATTENTION_OPERATORS

  claim:
    L02_ATTENTION can be represented as a typed operator system
    that admits attention candidates, assesses decision-relevant
    properties, ranks them, allocates finite reasoning/observation
    resources, manages focus and deferral, responds to changed
    dependencies, and emits governed proposals while preserving
    provenance, scope, regime, H/M/L identity, confidence ceilings,
    and authority boundaries.

  claim_class: MODEL

  source_supported_core:
    - L02 is an attention-allocation primitive
    - reasoning/observation resources are scarce
    - operator/kernel contract is required before promotion

  framework_supported_operators:
    - hard admission via invariants
    - selective invalidation of descendants
    - confidence-ceiling preservation

  model_operators:
    - INGEST
    - NORMALIZE
    - REJECT
    - QUARANTINE
    - ASSESS_RELEVANCE
    - ASSESS_SALIENCE
    - ASSESS_UNCERTAINTY
    - ASSESS_CONSEQUENCE
    - ASSESS_DEPENDENCY_CRITICALITY
    - ASSESS_TIME_SENSITIVITY
    - ASSESS_INFORMATION_VALUE
    - ASSESS_COST
    - RANK
    - COMPARE
    - SELECT
    - ALLOCATE
    - RESERVE
    - FOCUS
    - SUSTAIN
    - SHIFT
    - RELEASE
    - DEFER
    - RESUME
    - ESCALATE
    - DEESCALATE
    - CHECK_FRESHNESS
    - REVALIDATE
    - REALLOCATE
    - RECALL
    - EXTERNALIZE_MEMORY
    - REPAIR
    - ROLLBACK_PROPOSE
    - EMIT_PROPOSAL

  evidence:
    - direct L02 placeholder establishing attention allocation
    - direct L02 requirement for operators/kernels
    - AMOS Attention Allocation Governor framework

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    subsystem: COGNITIVE_MATRIX
    primitive: L02_ATTENTION
    artifact: OPERATORS.md
    derivation: SOURCE_BOUNDED_AMOS_MODEL

  scope:
    system: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    primitive: L02_ATTENTION
    concern: attention_operator_semantics

  regime:
    governed finite-resource cognitive allocation

  freshness:
    revalidate_when:
      - direct L02 operator canon is recovered
      - L02 state contract changes
      - L02 variable contract changes
      - control-plane ownership changes
      - AMOS_CORE attention runtime becomes available
      - executed validation becomes available

  dependencies:
    - L01_SENSING_OBSERVATION
    - L02_ATTENTION_DEFINITION
    - L02_ATTENTION_VARIABLES
    - L02_ATTENTION_STATE
    - L02_ATTENTION_INVARIANTS
    - L02_ATTENTION_DEPENDENCIES
    - L02_ATTENTION_EQUATIONS
    - L02_ATTENTION_HML
    - L02_ATTENTION_MEMORY
    - L02_ATTENTION_PROVENANCE
    - L02_ATTENTION_CONTROL_PLANES

  competing:
    - minimal L02 operator set
    - full L02 lifecycle runtime
    - infrastructure-owned attention mutation
    - hybrid local/infrastructure ownership

  falsifiers:
    - direct canon supplies incompatible operators
    - source assigns modeled functions to other primitives
    - runtime implements materially different ownership
    - executable tests violate modeled operator invariants

  uncertainty:
    evidence: MEDIUM_HIGH
    model: MEDIUM
    scope: MEDIUM_HIGH
    temporal: MEDIUM
    causal: LOW
    execution: HIGH
    provenance_independence: MEDIUM

  confidence_ceiling:
    high confidence attaches only to the source-supported primitive
    role and requirement for an operator/kernel surface;
    the detailed operator registry remains MODEL until direct canon
    or executable evidence resolves it

  gap_status:
    canonical_operator_registry: CRITICAL_GAP
    canonical_operator_ownership: CRITICAL_GAP
    runtime_implementation: CRITICAL_GAP
    executed_validation: CRITICAL_GAP

  cheapest_discriminating_test:
    recover canonical L02 operator/kernel definitions and determine
    which state transitions are L02-owned versus control-plane-owned
```

---

# 72. Completion State

```yaml
completion_state:

  source_canon_references:
    status: PARTIAL / SOURCE-BOUND

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

  canonical_operator_registry:
    status: UNKNOWN/GAP

  executable_runtime:
    status: UNKNOWN/GAP

  overall:
    status: COMPLETE_FOR_MODEL_SPECIFICATION_SCOPE

  conclusion_class:
    MODEL
```

---

# 73. Hard Boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

Operator-specific boundaries:

```text
INGEST != ADMIT

ADMIT != RANK

RANK != SELECT

SELECT != ALLOCATE

ALLOCATE != FOCUS

FOCUS != BELIEVE

PRIORITY != TRUTH

PRIORITY != CONFIDENCE

PRIORITY != AUTHORITY

SALIENCE != PRIORITY

NOVELTY != VALIDITY

DEPENDENCY != CAUSATION

RECALL != REVALIDATE

RESUME != FRESH

ESCALATE != AUTHORIZE

INVALIDATE != DELETE

REPAIR != VALIDATE

ROLLBACK PROPOSAL != ROLLBACK COMMIT

DETERMINISTIC OPERATOR != VALID INPUT

DOCUMENTED OPERATOR != IMPLEMENTED OPERATOR

IMPLEMENTED OPERATOR != VALIDATED OPERATOR

MODEL OPERATOR != CANONICAL OPERATOR
```

---

# 74. References

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
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README

L01_SENSING_OBSERVATION

Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
AMOS Context State Maintenance RSCF
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
```

---

# 75. Governing Operator Contract

> **`L02_ATTENTION` operates through typed, invariant-preserving transformations that admit candidate targets, assess their decision relevance, rank them, allocate finite reasoning/observation resources, manage focus and deferral, respond to stale or invalid dependencies, and escalate unresolved consequential state. Every operator must preserve provenance, scope, regime, H/M/L identity, confidence ceilings, contradiction visibility, and authority boundaries. Attention operators may propose state changes, but they may not silently promote truth, create authority, erase gaps, or commit durable external effects.**

---

# 76. Canon Boundary

```text
SOURCE-SUPPORTED:
L02_ATTENTION is an attention-allocation primitive.
It budgets scarce reasoning/observation resources.
An operators/kernels contract is explicitly required before promotion.

AMOS-FRAMEWORK-SUPPORTED:
Admit(x)=AND_i HardInvariant_i(x)

Conf(C)<=min_i Conf(P_i)

Invalid(p)=>Invalidate(Descendants(p))

AMOS_MODEL:
typed operator contract
operator registry
attention kernel
operator sequencing
assessment operators
ranking
allocation
focus
deferral
escalation
freshness
revalidation
reallocation
memory interaction
repair
rollback proposal
protocols
tests
operator ownership matrix

UNKNOWN/GAP:
canonical L02 operator names
canonical operator signatures
canonical operator ordering
canonical kernel
canonical ownership boundary
canonical thresholds
runtime implementation
runtime state transitions
executed operator tests
formal verification
```

Therefore:

```text
CONCLUSION CLASS:
MODEL

NOT:
VERIFIED L02 OPERATOR CANON

NOT:
PROOF OF IMPLEMENTATION

NOT:
PROOF OF RUNTIME ENFORCEMENT

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
node_id: l02_attention_primitives_cognitive_matrix_operators
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L02_ATTENTION/L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_OPERATORS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[L02_ATTENTION_MOC]]
