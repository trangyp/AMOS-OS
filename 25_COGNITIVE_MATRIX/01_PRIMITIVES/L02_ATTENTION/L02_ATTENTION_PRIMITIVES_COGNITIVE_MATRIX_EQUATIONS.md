---
tags: ['cognitive_matrix', 'primitives', 'l02_attention', 'note']
---

Below is the **full replacement content** for `L02_ATTENTION/EQUATIONS.md`. The key safeguard is that only source-supported equations are marked `SOURCE_CANON`; the attention scoring/allocation equations are explicitly `AMOS_MODEL` until direct L02 canon is recovered.

---
tags:
  - amos
  - cognitive-matrix
  - l02
  - attention
  - equations
  - rscf
  - hml

title: "L02_ATTENTION — Equations"
origin_architect: "Trang Phan"
status: "MODEL_SPECIFICATION / UNVALIDATED"
epistemic_class: "MODEL"
runtime_alignment: "AMOS Full Brain OS / AMOS_CORE v4.4 lineage"
---

# L02_ATTENTION — Equations

**Class:** `COGNITIVE_PRIMITIVE_EQUATION_CONTRACT`  
**Origin architect / steward:** Trang Phan  
**Primitive:** `L02_ATTENTION`  
**Artifact:** `EQUATIONS.md`  
**Status:** `AMOS_MODEL / SOURCE-BOUNDED / UNVALIDATED`

> **Canon boundary:** Available L02 material establishes attention allocation over scarce reasoning/observation resources. It does not, from the currently resolved evidence, establish a canonical mathematical attention equation. Accordingly, equations introduced specifically to formalize L02 below are `AMOS_MODEL` unless explicitly marked otherwise.

---

# 0. Purpose

This artifact defines the mathematical contract for `L02_ATTENTION`.

It specifies formal relationships for:

- attention candidate admission,
- finite attention budgets,
- priority,
- allocation,
- uncertainty,
- dependency criticality,
- H/M/L distribution,
- provenance and freshness,
- hard constraints,
- confidence ceilings,
- invalidation,
- saturation,
- switching,
- repair,
- and governed attention proposals.

The equations are intended to make L02:

```text
typed
auditable
bounded
falsifiable
dependency-aware
provenance-aware
H/M/L-aware
control-plane compatible
```

They are not presented as established neuroscience or psychology.

---

# 1. Source / Canon References

## 1.1 Source-supported primitive

Recovered L02 definition:

```text
L02_ATTENTION
=
attention allocation;
budget scarce reasoning/observation resources
```

This supports the structural relationship:

[
\text{finite attention resources}
\rightarrow
\text{allocation problem}
]

but does not uniquely determine an allocation formula.

## 1.2 Governing AMOS equations

The AMOS Attention Allocation Governor supplies these governing forms:

### EQ-GOV-001 — Hard Admission

[
Admit(x)=\bigwedge_i HardInvariant_i(x)
]

**Type:** `SOURCE_FRAMEWORK_EQUATION`

Interpretation:

A target cannot enter governed attention allocation if an applicable non-compensatory hard invariant fails.

---

### EQ-GOV-002 — Confidence Ceiling

[
Conf(C)\leq\min_i Conf(P_i)
]

**Type:** `SOURCE_FRAMEWORK_EQUATION`

Interpretation:

A conclusion cannot exceed the weakest load-bearing premise unless that premise is independently revalidated or replaced.

---

### EQ-GOV-003 — Selective Invalidation

[
Invalid(p)
\Rightarrow
Invalidate(Descendants(p))
]

**Type:** `SOURCE_FRAMEWORK_EQUATION`

Interpretation:

Invalidation propagates through actual dependency descendants rather than automatically invalidating unrelated state.

These equations govern L02 but are not evidence that they originated as L02-specific canonical equations.

---

# 2. Equation Classes

Every equation in this artifact MUST carry an epistemic type.

```yaml
EquationClass:
  - SOURCE_CANON
  - SOURCE_FRAMEWORK_EQUATION
  - AMOS_MODEL
  - DERIVED
  - IMPLEMENTATION_CANDIDATE
  - EMPIRICALLY_VALIDATED
  - UNKNOWN
```

Hard invariant:

```text
AMOS_MODEL != SOURCE_CANON
```

and:

```text
FORMALIZED != EMPIRICALLY_VALIDATED
```

---

# 3. Typed Mathematical Domain

Let:

[
X={x_1,\ldots,x_n}
]

be the set of eligible attention candidates.

Each candidate may be represented as:

[
x_i =
(o_i,g_i,u_i,c_i,d_i,p_i,t_i,r_i,h_i)
]

where:

```text
o_i = observation/content state
g_i = goal relevance
u_i = uncertainty state
c_i = consequence/criticality
d_i = dependency state
p_i = provenance state
t_i = temporal state
r_i = regime compatibility
h_i = H/M/L coordinate
```

This tensorization is `AMOS_MODEL`.

---

# 4. Attention Budget

Define total available attention budget:

[
B_t \ge 0
]

and allocation:

[
a_i(t)\ge0
]

with:

### EQ-L02-001 — Budget Conservation

[
\sum_{i=1}^{n}a_i(t)\le B_t
]

**Type:** `AMOS_MODEL`
**Purpose:** prevent allocation beyond declared finite capacity.

Hard invariant:

```text
ALLOCATED_ATTENTION <= AVAILABLE_ATTENTION
```

This is a modeling conservation constraint, not a physical law.

---

# 5. Residual Budget

### EQ-L02-002

[
B_t^{remaining}
===============

B_t-\sum_i a_i(t)
]

with:

[
B_t^{remaining}\ge0
]

**Type:** `DERIVED_FROM_MODEL`

If:

[
B_t^{remaining}<0
]

then:

```text
BUDGET_INVARIANT = FAIL
```

---

# 6. Candidate Admission

Before ranking:

### EQ-L02-003

[
E_t
===

{x_i\in X:
Admit(x_i)=1}
]

where:

[
Admit(x_i)
==========

\bigwedge_j HardInvariant_j(x_i)
]

**Type:** `AMOS_MODEL + SOURCE_FRAMEWORK_OPERATOR`

This separates:

```text
admissibility
```

from:

```text
priority
```

A candidate may be important but inadmissible.

---

# 7. Priority State

Define a candidate priority vector:

[
z_i =
[
G_i,
C_i,
U_i,
T_i,
D_i,
N_i,
R_i,
P_i
]
]

where, for example:

```text
G_i = goal relevance
C_i = consequence/criticality
U_i = decision-relevant uncertainty
T_i = time sensitivity
D_i = dependency criticality
N_i = novelty/information gain
R_i = regime relevance
P_i = provenance/evidence relevance
```

Exact canonical dimensions remain `UNKNOWN/GAP`.

---

# 8. Generic Priority Function

### EQ-L02-004

[
\pi_i
=====

F(z_i \mid S_t)
]

where:

```text
π_i = priority of candidate i
S_t = governing state/context
F = attention-priority function
```

**Type:** `AMOS_MODEL`

This intentionally leaves (F) unspecified.

Why:

> Current source evidence does not justify claiming one canonical linear or nonlinear scoring equation.

---

# 9. Linear Priority Candidate

A simple implementation candidate is:

### EQ-L02-005

[
\pi_i
=====

w_GG_i+
w_CC_i+
w_UU_i+
w_TT_i+
w_DD_i+
w_NN_i
]

subject to:

[
w_k\ge0
]

**Type:** `IMPLEMENTATION_CANDIDATE`

This is **not canonical**.

It should not be promoted without validation because attention factors may interact nonlinearly or non-compensatorily.

---

# 10. Non-Compensatory Priority

Hard constraints must sit outside additive scoring.

### EQ-L02-006

[
PriorityEligible_i
==================

Admit(x_i)\cdot \pi_i
]

where:

[
Admit(x_i)\in{0,1}
]

Thus:

[
Admit(x_i)=0
\Rightarrow
PriorityEligible_i=0
]

for ordinary allocation.

**Type:** `AMOS_MODEL`

This prevents:

```text
very high utility
+
hard safety failure
=
accepted target
```

---

# 11. Allocation Function

### EQ-L02-007

[
A_t
===

Allocate(E_t,\Pi_t,B_t,C_t)
]

where:

```text
E_t = eligible candidates
Π_t = priority vector
B_t = budget
C_t = constraints
A_t = allocation proposal
```

**Type:** `AMOS_MODEL`

Output:

[
A_t=[a_1,\ldots,a_n]
]

subject to EQ-L02-001.

---

# 12. Normalized Proportional Allocation

One candidate implementation:

### EQ-L02-008

[
a_i
===

B_t
\frac{\pi_i}
{\sum_{j\in E_t}\pi_j}
]

for:

[
\sum_j\pi_j>0
]

**Type:** `IMPLEMENTATION_CANDIDATE`

This should not be treated as canonical because it permits broad proportional allocation and may be inappropriate where selective focus is required.

---

# 13. Top-K Allocation

Alternative candidate:

### EQ-L02-009

[
A_t
===

TopK(\Pi_t,k)
]

subject to:

[
k\le |E_t|
]

**Type:** `IMPLEMENTATION_CANDIDATE`

This represents sparse attention.

It competes with proportional allocation.

---

# 14. Threshold Allocation

Alternative:

### EQ-L02-010

[
Attend(x_i)=
\begin{cases}
1,&\pi_i\ge\tau\
0,&\pi_i<\tau
\end{cases}
]

**Type:** `IMPLEMENTATION_CANDIDATE`

where (\tau) is a context-dependent threshold.

---

# 15. Competing Allocation Models

Current model must preserve:

```text
COMPETING_001 = proportional allocation
COMPETING_002 = top-k allocation
COMPETING_003 = threshold allocation
COMPETING_004 = hierarchical H/M/L allocation
COMPETING_005 = expected-decision-value allocation
```

No source-supported evidence currently licenses selecting one as canonical.

---

# 16. Expected Decision Value

Attention should preferentially reduce uncertainty when doing so can alter a decision.

Candidate:

### EQ-L02-011

[
EDV(x_i)
========

P(ChangeDecision\mid ObserveMore_i)
\times
Impact(ChangeDecision_i)
]

**Type:** `AMOS_MODEL`

This formalizes decision-relevant information value.

It is not a calibrated probability equation unless its terms are empirically estimated.

---

# 17. Uncertainty-Reduction Value

### EQ-L02-012

[
V_U(x_i)
========

EDV(x_i)\cdot
\Delta U_i
]

where:

[
\Delta U_i
==========

U_{before}-E[U_{after}\mid Attend(x_i)]
]

**Type:** `AMOS_MODEL`

Hard boundary:

```text
UNCERTAINTY != PRIORITY
```

Only decision-relevant reducible uncertainty should increase attention pressure.

---

# 18. Consequence Weighting

Candidate consequence term:

### EQ-L02-013

[
C_i
===

Impact_i
\times
Irreversibility_i
]

**Type:** `AMOS_MODEL`

Possible extension:

[
C_i
===

Impact_i
\times
Irreversibility_i
\times
Exposure_i
]

This is a governance heuristic, not an empirical universal law.

---

# 19. Dependency Criticality

### EQ-L02-014

[
D_i
===

Impact(Descendants_i)
\times
FailureSensitivity_i
]

**Type:** `AMOS_MODEL`

Interpretation:

A premise with many consequential dependent conclusions may deserve more attention.

Hard boundary:

```text
DEPENDENCY DEGREE != CAUSAL IMPORTANCE
```

---

# 20. Temporal Urgency

Candidate:

### EQ-L02-015

[
T_i
===

f(
deadline_i,
decay_i,
recoverability_i,
latency_i
)
]

**Type:** `AMOS_MODEL`

No canonical functional form is claimed.

---

# 21. Freshness

Let evidence age be:

[
Age_i=t_{now}-t_{validated,i}
]

Candidate freshness:

### EQ-L02-016

[
Fresh_i
=======

f(Age_i,Volatility_i,RegimeChange_i)
]

**Type:** `AMOS_MODEL`

Do not assume exponential decay universally.

---

# 22. Freshness Gate

For a load-bearing mutable premise:

### EQ-L02-017

[
ValidFresh_i
============

Valid_i
\land
Fresh_i
]

If:

[
Fresh_i=0
]

then dependent attention proposals requiring that premise must be revalidated.

---

# 23. Scope Compatibility

Define:

### EQ-L02-018

[
ScopeOK(x_i,S)
==============

\mathbf{1}[Scope(x_i)\supseteq RequiredScope(S)]
]

**Type:** `AMOS_MODEL`

The actual scope relation may require partial overlap rather than strict set inclusion.

Therefore exact relation remains conditional.

---

# 24. Regime Compatibility

### EQ-L02-019

[
RegimeOK(x_i,R_t)
=================

\mathbf{1}[R_i\sim R_t]
]

where (\sim) denotes validated compatibility.

**Type:** `AMOS_MODEL`

Hard boundary:

```text
SAME DOMAIN != SAME REGIME
```

---

# 25. Provenance Independence

Let source ancestry sets be:

[
Anc(e_i)
]

and:

[
Anc(e_j)
]

Candidate independence check:

### EQ-L02-020

[
Independent(e_i,e_j)
====================

\mathbf{1}
[
Anc(e_i)\cap Anc(e_j)=\varnothing
]
]

**Type:** `AMOS_MODEL`

This is deliberately conservative.

Real independence may require more than ancestry disjointness.

---

# 26. Provenance Correlation Penalty

Candidate:

### EQ-L02-021

[
P^{effective}
=============

## P^{nominal}

CorrelationRisk
]

**Type:** `AMOS_MODEL`

No numerical form is canonical.

The invariant is qualitative:

```text
REPETITION FROM COMMON ANCESTRY
MUST NOT
INCREASE CONFIDENCE AS IF INDEPENDENT
```

---

# 27. Confidence Ceiling

### EQ-L02-022

[
Conf(C)
\le
\min_i Conf(P_i)
]

**Type:** `SOURCE_FRAMEWORK_EQUATION`

Application to attention:

An attention ranking derived from uncertain load-bearing state cannot claim greater epistemic confidence than that state permits.

---

# 28. Confidence of Attention Proposal

Candidate:

### EQ-L02-023

[
Conf(A_t)
\le
\min
{
Conf(B_t),
Conf(G_t),
Conf(D_t),
Conf(C_t),
Conf(P_t)
}
]

over whichever terms are actually load-bearing.

**Type:** `DERIVED AMOS_MODEL`

Do not include irrelevant terms merely to lower confidence mechanically.

---

# 29. Selective Invalidation

### EQ-L02-024

[
Invalid(p)
\Rightarrow
Invalidate(Descendants(p))
]

**Type:** `SOURCE_FRAMEWORK_EQUATION`

For L02:

[
Invalid(p)
\Rightarrow
RecomputeAttention(
AffectedClosure(p)
)
]

rather than recomputing all cognitive state.

---

# 30. Affected Closure

### EQ-L02-025

[
AffectedClosure(p)
==================

{x:
p\leadsto x}
]

where (\leadsto) denotes dependency reachability.

**Type:** `AMOS_MODEL`

---

# 31. Attention Reallocation

If candidate (x_k) becomes invalid:

### EQ-L02-026

[
a_k'=0
]

and freed budget:

[
\Delta B=a_k
]

may be reallocated:

[
\sum_{i\neq k}(a_i'-a_i)
\le
\Delta B
]

**Type:** `AMOS_MODEL`

unless budget is intentionally reserved rather than reallocated.

---

# 32. Reserved Attention

Candidate:

### EQ-L02-027

[
B_t
===

B_H+B_M+B_L+B_R
]

where:

```text
B_H = high-level attention budget
B_M = subsystem attention budget
B_L = local/detail attention budget
B_R = reserve budget
```

**Type:** `AMOS_MODEL`

with:

[
B_R\ge0
]

Reserve capacity protects against unexpected high-priority events.

---

# 33. H/M/L Budget Constraint

### EQ-L02-028

[
\sum_{s\in{H,M,L,R}}B_s
\le
B_t
]

**Type:** `AMOS_MODEL`

The actual H/M/L budget partition is not canonical.

---

# 34. Hierarchical Attention

Candidate hierarchical model:

### EQ-L02-029

[
A_H
===

Allocate(X_H,B_H)
]

[
A_M
===

Allocate(X_M\mid A_H,B_M)
]

[
A_L
===

Allocate(X_L\mid A_H,A_M,B_L)
]

**Type:** `AMOS_MODEL`

This implements progressive disclosure:

```text
H domain
→
M subsystem
→
L detail
→
raw evidence when required
```

---

# 35. H→M Constraint Propagation

### EQ-L02-030

[
Eligible_M
==========

Eligible_M
\cap
Constraints(A_H)
]

**Type:** `AMOS_MODEL`

High-level decisions may constrain subsystem search without predetermining unsupported conclusions.

---

# 36. L→H Escalation

A low-level observation may force high-level reassessment.

### EQ-L02-031

[
Critical_L=1
\land
Invalidates(P_H)
\Rightarrow
Revalidate(H)
]

**Type:** `AMOS_MODEL`

This prevents hierarchy from suppressing decisive counterevidence.

---

# 37. Salience vs Evidence

Candidate separation:

[
Salience_i
\neq
EvidenceStrength_i
]

This is an invariant, not a numerical equation.

Possible priority model:

### EQ-L02-032

[
\pi_i
=====

F(
Salience_i,
EvidenceStrength_i,
DecisionRelevance_i,
...
)
]

with distinct variables.

**Type:** `AMOS_MODEL`

---

# 38. Novelty

Candidate novelty measure:

### EQ-L02-033

[
N_i
===

Distance(x_i,M_{known})
]

**Type:** `AMOS_MODEL`

where the metric must be explicitly defined.

Hard boundary:

```text
NOVEL != TRUE
```

---

# 39. Attention Saturation

To prevent unlimited allocation to one target:

### EQ-L02-034

[
a_i\le a_i^{max}
]

**Type:** `AMOS_MODEL`

unless exclusive-focus mode explicitly permits:

[
a_i=B_t
]

---

# 40. Minimum Attention

Critical targets may require minimum allocation:

### EQ-L02-035

[
Critical_i=1
\Rightarrow
a_i\ge a_i^{min}
]

provided:

```text
candidate is admissible
and
budget exists
```

**Type:** `AMOS_MODEL`

---

# 41. Starvation

Define starvation:

### EQ-L02-036

[
Starved_i
=========

\mathbf{1}
[
Eligible_i
\land
Need_i>0
\land
a_i=0
\land
Duration_i>\tau_s
]
]

**Type:** `AMOS_MODEL`

Not all starvation is erroneous; low-priority items may legitimately remain unattended.

---

# 42. Switching Cost

Attention shifts may incur cost.

### EQ-L02-037

[
Cost_{switch}
=============

f(
Distance(Context_t,Context_{t+1}),
StateReload,
ToolTransition,
DependencyReload
)
]

**Type:** `AMOS_MODEL`

This formalizes why constant switching may reduce effective capacity.

---

# 43. Effective Budget

Candidate:

### EQ-L02-038

[
B_t^{effective}
===============

## B_t

## Cost_{switch}

## Cost_{governance}

Cost_{repair}
]

subject to:

[
B_t^{effective}\ge0
]

**Type:** `AMOS_MODEL`

These terms are abstract resource quantities unless units are concretely defined.

---

# 44. Attention Debt

Unresolved deferred items may accumulate attention debt.

### EQ-L02-039

[
Debt_{t+1}
==========

Debt_t
+
DeferredCritical_t
------------------

ResolvedDeferred_t
]

**Type:** `AMOS_MODEL`

This is a bookkeeping model, not a psychological law.

---

# 45. Escalation Threshold

Candidate:

### EQ-L02-040

[
Escalate(x_i)=1
]

if:

[
Risk_i\ge\tau_R
\lor
AuthorityAmbiguous_i
\lor
CriticalDependencyMissing_i
\lor
Contradiction_i
]

**Type:** `AMOS_MODEL`

Hard conditions should preferably be Boolean rather than compensatory scores.

---

# 46. Repair Priority

Candidate repair attention:

### EQ-L02-041

[
RepairPriority_i
================

Impact_i
\times
RecoverabilityWindow_i^{-1}
\times
DependencyFanout_i
]

**Type:** `AMOS_MODEL`

This equation is heuristic and must not override hard safety/authority constraints.

---

# 47. Repair Success

### EQ-L02-042

[
RepairValid_i
=============

FunctionalRecovery_i
\land
InvariantPreservation_i
\land
ProvenancePreservation_i
\land
NoCriticalRegression_i
]

**Type:** `AMOS_MODEL`

---

# 48. Attention Proposal

Final L02 output is a proposal:

### EQ-L02-043

[
Proposal_t
==========

(
A_t,
E_t,
U_t,
P_t,
F_t
)
]

where:

```text
A_t = allocation
E_t = evidence/provenance bundle
U_t = uncertainty
P_t = dependencies/premises
F_t = falsifiers
```

**Type:** `AMOS_MODEL`

Hard boundary:

[
Proposal_t\neq Commit_t
]

---

# 49. Commit Eligibility

If an attention proposal causes governed durable effects:

### EQ-L02-044

[
CommitEligible
==============

ProposalValid
\land
AuthorityValid
\land
ConstraintsFresh
\land
DependenciesFresh
\land
ScopeValid
\land
RegimeValid
]

**Type:** `AMOS_MODEL / CONTROL-PLANE CONTRACT`

L02 itself does not gain commit authority from this equation.

---

# 50. State Variables

```text
X_t       candidate set
E_t       eligible candidate set
B_t       total attention budget
B_R       reserve attention
A_t       allocation vector
Π_t       priority vector
G_t       goal state
U_t       uncertainty state
C_t       consequence/constraint state
D_t       dependency state
P_t       provenance state
R_t       regime state
S_t       scope state
H_t       H/M/L state
F_t       freshness state
Q_t       queue/deferred state
Debt_t    attention debt
```

All are `AMOS_MODEL` variable names unless separately canonical.

---

# 51. Operators

```text
OBSERVE()
ADMIT()
FILTER()
SCORE()
RANK()
ALLOCATE()
RESERVE()
FOCUS()
DEFOCUS()
SWITCH()
ESCALATE()
DEFER()

CHECK_BUDGET()
CHECK_CONSTRAINTS()
CHECK_SCOPE()
CHECK_REGIME()
CHECK_FRESHNESS()
CHECK_PROVENANCE()
CHECK_DEPENDENCIES()
CHECK_AUTHORITY()

INVALIDATE()
REALLOCATE()
REVALIDATE()
REPAIR()
ROLLBACK()
```

---

# 52. Invariants

```text
L02-EQ-INV-001
Σ allocation <= available budget.

L02-EQ-INV-002
Allocation cannot be negative.

L02-EQ-INV-003
Hard invariant failure cannot be compensated by priority.

L02-EQ-INV-004
Priority does not equal truth.

L02-EQ-INV-005
Salience does not equal evidence strength.

L02-EQ-INV-006
Novelty does not equal validity.

L02-EQ-INV-007
Uncertainty alone does not imply priority.

L02-EQ-INV-008
Dependency does not imply causation.

L02-EQ-INV-009
Confidence cannot exceed weakest load-bearing premise.

L02-EQ-INV-010
Invalidation propagates only through actual dependencies.

L02-EQ-INV-011
H/M/L scale identity must remain explicit.

L02-EQ-INV-012
Scope incompatibility cannot silently pass.

L02-EQ-INV-013
Regime incompatibility cannot silently pass.

L02-EQ-INV-014
Stale load-bearing state requires revalidation.

L02-EQ-INV-015
Correlated provenance cannot masquerade as independence.

L02-EQ-INV-016
Attention allocation cannot grant authority.

L02-EQ-INV-017
Proposal cannot become commit without control-plane validation.

L02-EQ-INV-018
UNKNOWN/GAP cannot numerically collapse into PASS.

L02-EQ-INV-019
Model equations cannot be relabeled canonical without source evidence.

L02-EQ-INV-020
Equation optimization cannot weaken integrity invariants.
```

---

# 53. Dependencies

Equation execution may depend on:

```text
L01_SENSING_OBSERVATION
L02_ATTENTION_DEFINITION
L02_ATTENTION_VARIABLES
L02_ATTENTION_STATE
L02_ATTENTION_OPERATORS
L02_ATTENTION_INVARIANTS
L02_ATTENTION_DEPENDENCIES
L02_ATTENTION_HML
L02_ATTENTION_CONTROL_PLANES
L02_ATTENTION_PROVENANCE
L02_ATTENTION_REPAIR
L02_ATTENTION_TESTS
```

Governance dependencies may include:

```text
AMOS Attention Allocation Governor
AMOS Constraint Propagation
AMOS Context Budget Governor
AMOS Provenance topology
AMOS Infrastructure Control Plane
AMOS RSCF
```

---

# 54. H/M/L Applicability

## H — Governing allocation

Equations address:

```text
global budget
goal alignment
system-critical risks
global constraints
reserve capacity
```

## M — Subsystem allocation

Equations address:

```text
workstreams
hypothesis families
agent groups
retrieval branches
tool workflows
```

## L — Local allocation

Equations address:

```text
observations
claims
variables
files
tool results
tests
individual evidence items
```

Cross-scale allocation must not silently mix units.

---

# 55. Control-Plane Requirements

The control plane should validate at minimum:

```text
equation identity
equation epistemic class
input types
units/domains
budget feasibility
hard invariants
scope
regime
freshness
provenance
dependency validity
authority
proposal/commit separation
```

Model flow:

```text
L02 worker
↓
compute candidate allocation
↓
emit AttentionProposal
↓
control-plane validation
↓
VALID / REJECT / REVALIDATE / ESCALATE
↓
authorized downstream handling
```

---

# 56. Agents

Candidate logical roles:

```text
L02_EQUATION_EVALUATOR
L02_BUDGET_ALLOCATOR
L02_PRIORITY_ESTIMATOR
L02_INVARIANT_AUDITOR
L02_PROVENANCE_AUDITOR
L02_DEPENDENCY_AUDITOR
L02_HML_ROUTER
L02_REPAIR_AGENT
```

These are model roles, not proof of deployed agents.

---

# 57. Skills

Relevant capabilities:

```text
AMOS Attention Allocation Governor
AMOS Mathematical Rigor RSCF Kernel
AMOS Constraint Propagation
AMOS Context Budget Governor
AMOS Provenance Trust Firewall
AMOS Metacognitive Confidence Auditor
AMOS RSCF Modeler
AMOS Infrastructure Control Plane
```

Hard boundary:

```text
SKILL EXISTS
!=
L02 CANONICALLY DEPENDS ON SKILL
```

---

# 58. Workflow

```text
1. RECEIVE candidate targets

2. TYPE variables

3. RESOLVE scope/regime

4. CHECK dependency state

5. APPLY hard admission equation

6. DETERMINE available budget

7. COMPUTE decision-relevant variables

8. SELECT explicitly declared allocation model

9. COMPUTE priority

10. ALLOCATE under budget constraint

11. CHECK H/M/L consistency

12. CHECK confidence ceiling

13. CHECK provenance independence

14. CHECK freshness

15. GENERATE allocation proposal

16. VALIDATE through control plane where required

17. COMMIT only under separate authority

18. PRESERVE gaps and falsifiers
```

---

# 59. Protocol

Suggested equation result envelope:

```yaml
AttentionEquationResult:

  equation_id:
    type: EquationId

  equation_class:
    type:
      - SOURCE_CANON
      - SOURCE_FRAMEWORK_EQUATION
      - AMOS_MODEL
      - DERIVED
      - IMPLEMENTATION_CANDIDATE

  inputs:
    type: TypedVariable[]

  outputs:
    type: TypedVariable[]

  assumptions:
    type: Assumption[]

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef

  provenance:
    type: ProvenanceBundle

  invariant_status:
    type:
      - PASS
      - FAIL
      - UNKNOWN

  confidence:
    type: ConfidenceBound

  falsifiers:
    type: Falsifier[]

  execution_status:
    type:
      - NOT_EXECUTED
      - EXECUTED
      - VALIDATED
      - FAILED
```

---

# 60. Evidence / Provenance

Each equation should retain:

```text
equation ID
equation text
equation class
source reference
derivation lineage
variables
variable types
units where applicable
assumptions
scope
regime
dependencies
validator
test status
falsifiers
version
```

No equation should gain canonical status through repetition across generated artifacts.

---

# 61. Failure Modes

```text
FM-L02-EQ-001  Budget Overflow
FM-L02-EQ-002  Negative Allocation
FM-L02-EQ-003  Unit Mismatch
FM-L02-EQ-004  Undefined Variable
FM-L02-EQ-005  Hidden Assumption
FM-L02-EQ-006  Additive Hard-Constraint Compensation
FM-L02-EQ-007  Salience/Truth Collapse
FM-L02-EQ-008  Uncertainty/Priority Collapse
FM-L02-EQ-009  Dependency/Causality Collapse
FM-L02-EQ-010  Scope Leakage
FM-L02-EQ-011  Regime Leakage
FM-L02-EQ-012  Freshness Blindness
FM-L02-EQ-013  Provenance Double Counting
FM-L02-EQ-014  Confidence Inflation
FM-L02-EQ-015  H/M/L Unit Collapse
FM-L02-EQ-016  Starvation
FM-L02-EQ-017  Attention Thrashing
FM-L02-EQ-018  Reserve Exhaustion
FM-L02-EQ-019  Priority Saturation
FM-L02-EQ-020  Proposal/Commit Collapse
FM-L02-EQ-021  Authority Leakage
FM-L02-EQ-022  Model-As-Canon Promotion
FM-L02-EQ-023  Equation-As-Empirical-Law Promotion
FM-L02-EQ-024  Invalid Global Recompute
FM-L02-EQ-025  Repair Regression
```

---

# 62. Repair / Recovery

```text
DETECT equation failure
↓
IDENTIFY affected equation
↓
IDENTIFY load-bearing variables
↓
FREEZE affected descendants
↓
PRESERVE unaffected state
↓
CLASSIFY:
  type error
  unit error
  assumption error
  stale input
  scope mismatch
  regime mismatch
  provenance failure
  model failure
↓
REPAIR smallest failed component
↓
RECOMPUTE affected closure
↓
REVALIDATE invariants
↓
RESTORE allocation if valid
```

If repair fails:

```text
ROLL BACK
to nearest valid equation/input state
```

---

# 63. Tests / Validators

Required validators:

```text
VALIDATE_EQUATION_CLASS
VALIDATE_VARIABLE_TYPES
VALIDATE_VARIABLE_DOMAINS
VALIDATE_UNITS
VALIDATE_BUDGET
VALIDATE_NONNEGATIVITY
VALIDATE_HARD_ADMISSION
VALIDATE_CONFIDENCE_CEILING
VALIDATE_DEPENDENCY_CLOSURE
VALIDATE_SCOPE
VALIDATE_REGIME
VALIDATE_FRESHNESS
VALIDATE_PROVENANCE
VALIDATE_HML
VALIDATE_AUTHORITY_BOUNDARY
VALIDATE_SELECTIVE_INVALIDATION
VALIDATE_REPAIR
VALIDATE_ROLLBACK
```

---

# 64. Minimum Tests

```text
TEST-L02-EQ-001
Allocation exceeding B_t must fail.

TEST-L02-EQ-002
Negative allocation must fail.

TEST-L02-EQ-003
Hard invariant failure cannot be overcome by large π_i.

TEST-L02-EQ-004
Zero total priority does not permit divide-by-zero proportional allocation.

TEST-L02-EQ-005
Unknown budget prevents false executable allocation.

TEST-L02-EQ-006
Stale load-bearing state triggers revalidation.

TEST-L02-EQ-007
Scope mismatch cannot silently enter ranking.

TEST-L02-EQ-008
Regime mismatch cannot silently enter ranking.

TEST-L02-EQ-009
Common-ancestry evidence cannot be counted as independent.

TEST-L02-EQ-010
Confidence respects weakest load-bearing premise.

TEST-L02-EQ-011
Invalid premise selectively invalidates dependent allocations.

TEST-L02-EQ-012
Unaffected allocation branches remain intact.

TEST-L02-EQ-013
H/M/L budgets cannot exceed global budget.

TEST-L02-EQ-014
Critical L-level falsifier can trigger H-level reassessment.

TEST-L02-EQ-015
Priority does not grant authority.

TEST-L02-EQ-016
Valid attention proposal does not automatically commit.

TEST-L02-EQ-017
AMOS_MODEL equation cannot be reported as SOURCE_CANON.

TEST-L02-EQ-018
Unexecuted equation cannot be reported as runtime validated.

TEST-L02-EQ-019
UNKNOWN/GAP cannot be converted to numeric PASS.

TEST-L02-EQ-020
Repair preserves unaffected state and provenance.
```

---

# 65. Falsifiers

Revise this artifact if:

```text
direct L02 canon supplies materially different equations

canonical L02 explicitly rejects finite-budget allocation

canonical variables differ materially from the model tensor

canonical attention uses no priority/ranking mechanism

runtime implementation contradicts budget conservation semantics

formal verification falsifies proposed invariants

empirical/runtime tests show a proposed allocation model systematically violates declared requirements
```

---

# 66. Gap Matrix

```yaml
gap_matrix:

  l02_attention_allocation_identity:
    status: SOURCE_SUPPORTED

  scarce_resource_basis:
    status: SOURCE_SUPPORTED

  hard_admission_equation:
    status: SOURCE_FRAMEWORK_SUPPORTED

  confidence_ceiling:
    status: SOURCE_FRAMEWORK_SUPPORTED

  selective_invalidation:
    status: SOURCE_FRAMEWORK_SUPPORTED

  canonical_l02_attention_equation:
    status: GAP
    criticality: CRITICAL

  canonical_priority_function:
    status: GAP
    criticality: CRITICAL

  canonical_budget_equation:
    status: GAP
    criticality: DECISION_RELEVANT

  canonical_attention_variables:
    status: GAP
    criticality: CRITICAL

  canonical_weights:
    status: GAP
    criticality: DECISION_RELEVANT

  canonical_thresholds:
    status: GAP
    criticality: DECISION_RELEVANT

  canonical_hml_equations:
    status: GAP
    criticality: DECISION_RELEVANT

  canonical_switching_model:
    status: GAP
    criticality: EXPLANATORY

  canonical_control_plane_equations:
    status: GAP
    criticality: CRITICAL

  executable_runtime_mapping:
    status: GAP
    criticality: CRITICAL

  empirical_validation:
    status: GAP
    criticality: CRITICAL
```

---

# 67. Cheapest Discriminating Evidence

Highest-value retrieval order:

```text
1. Direct L02_ATTENTION canonical equation definitions
2. L02 variable registry
3. L02 state schema
4. L02 operator definitions
5. AMOS cognition mathematical registry
6. AMOS Full Brain OS attention implementation
7. AMOS_CORE v4.4 attention/routing code
8. Executed tests and runtime traces
```

Cheapest decisive test:

> Recover any direct canonical equation explicitly bound to `L02_ATTENTION` and compare its variables, operators, constraints, and semantics against EQ-L02-001 through EQ-L02-044.

---

# 68. RSCF Completion State

```yaml
rscf:

  id: L02_ATTENTION_EQUATIONS

  claim:
    L02_ATTENTION can be represented as a governed finite-resource
    allocation problem in which admissible attention targets compete
    for bounded processing resources under hard constraints,
    dependency, provenance, scope, regime, uncertainty, temporal,
    H/M/L, and authority boundaries.

  claim_class: MODEL

  source_supported_core:
    - L02 concerns attention allocation
    - attention budgets scarce reasoning/observation resources

  source_framework_equations:
    - Admit(x)=AND_i HardInvariant_i(x)
    - Conf(C)<=min_i Conf(P_i)
    - Invalid(p)=>invalidate(descendants(p))

  model_equations:
    - finite budget conservation
    - residual budget
    - candidate admission
    - priority function
    - allocation function
    - uncertainty reduction
    - consequence weighting
    - dependency criticality
    - freshness
    - scope compatibility
    - regime compatibility
    - provenance independence
    - H/M/L allocation
    - switching cost
    - repair priority
    - commit eligibility

  competing:
    - proportional allocation
    - top-k allocation
    - threshold allocation
    - hierarchical H/M/L allocation
    - expected-decision-value allocation

  evidence:
    - recovered L02 primitive definition
    - AMOS Attention Allocation Governor contract
    - AMOS v4.4 governance lineage

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    subsystem: COGNITIVE_MATRIX
    primitive: L02_ATTENTION
    artifact: EQUATIONS.md
    derivation: SOURCE_BOUNDED_MODEL_COMPLETION

  scope:
    system: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    primitive: L02_ATTENTION
    concern: mathematical_attention_contract

  regime:
    governed finite-resource cognitive allocation

  freshness:
    revalidate_when:
      - direct L02 equation canon is recovered
      - canonical variables change
      - canonical attention operators change
      - AMOS_CORE runtime mapping is recovered
      - equation validation evidence changes

  dependencies:
    - L01_SENSING_OBSERVATION
    - L02_ATTENTION_DEFINITION
    - L02_ATTENTION_VARIABLES
    - L02_ATTENTION_STATE
    - L02_ATTENTION_OPERATORS
    - L02_ATTENTION_INVARIANTS
    - L02_ATTENTION_DEPENDENCIES
    - L02_ATTENTION_HML
    - L02_ATTENTION_CONTROL_PLANES
    - L02_ATTENTION_PROVENANCE
    - L02_ATTENTION_REPAIR
    - L02_ATTENTION_TESTS

  falsifiers:
    - direct canon contradicts modeled equations
    - runtime implementation contradicts modeled invariants
    - formal analysis identifies inconsistent equations
    - validation shows modeled allocation fails declared L02 contract

  uncertainty:
    evidence: MEDIUM_HIGH
    model: MEDIUM
    scope: MEDIUM_HIGH
    temporal: MEDIUM
    causal: LOW
    execution: HIGH
    provenance_independence: MEDIUM

  confidence_ceiling:
    source-supported governing equations may be reused within
    their declared AMOS framework scope; L02-specific mathematical
    equations remain MODEL until direct canon or executable evidence
    validates them

  gap_status:
    canonical_l02_equations: CRITICAL_GAP
    canonical_variables: CRITICAL_GAP
    runtime_mapping: CRITICAL_GAP
    executed_validation: CRITICAL_GAP

  cheapest_discriminating_test:
    recover direct canonical L02 equation definitions and compare
    them against the proposed equation registry
```

---

# 69. Completion State

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

  canonical_equations:
    status: UNKNOWN/GAP

  runtime_equation_mapping:
    status: UNKNOWN/GAP

  empirical_validation:
    status: UNKNOWN/GAP

  overall:
    status: COMPLETE_FOR_DECLARED_MODEL_SCOPE

  conclusion_class:
    MODEL / CONDITIONAL
```

---

# 70. Hard Boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

Equation-specific boundaries:

```text
EQUATION != EMPIRICAL LAW

FORMALIZATION != VALIDATION

MODEL EQUATION != CANONICAL EQUATION

SOURCE FRAMEWORK EQUATION != L02-SPECIFIC CANON

PRIORITY != TRUTH

SALIENCE != EVIDENCE

NOVELTY != VALIDITY

UNCERTAINTY != IMPORTANCE

DEPENDENCY != CAUSATION

SCORE != ADMISSIBILITY

HIGH SCORE != HARD-CONSTRAINT OVERRIDE

BUDGET != AUTHORITY

ALLOCATION != EXECUTION

ATTENTION PROPOSAL != COMMIT

CORRELATED EVIDENCE != INDEPENDENT EVIDENCE

H/M/L ANALOGY != CROSS-SCALE CAUSATION

UNKNOWN VARIABLE != ZERO

MISSING EVIDENCE != NEGATIVE EVIDENCE

UNEXECUTED TEST != PASS
```

---

# 71. References

```text
[[L02_ATTENTION/PLACEHOLDER.md]]

[[L02_ATTENTION — Definition]]
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
[[AMOS Mathematical Rigor RSCF Kernel]]
[[AMOS Constraint Propagation]]
[[AMOS Context Budget Governor]]
[[AMOS Provenance Trust Firewall]]
[[AMOS Infrastructure Control Plane]]
[[AMOS RSCF]]
[[AMOS Full Brain OS]]
[[AMOS CORE v4.4]]
```

---

# 72. Governing Equation Contract

> **L02_ATTENTION is modeled as constrained allocation of finite reasoning/observation resources across admissible targets. Hard invariants govern admission before scoring; allocation cannot exceed available budget; priority remains distinct from truth, authority, and evidence strength; confidence cannot exceed load-bearing premises; invalid state selectively invalidates dependent allocations; and any consequential allocation remains a proposal until separately authorized.**

---

# 73. Canon Boundary

```text
SOURCE-SUPPORTED:
L02 concerns attention allocation over scarce
reasoning/observation resources.

SOURCE-FRAMEWORK-SUPPORTED:
Admit(x)=AND_i HardInvariant_i(x)

Conf(C)<=min_i Conf(P_i)

Invalid(p)=>invalidate(descendants(p))

AMOS_MODEL:
budget conservation,
priority tensors,
allocation functions,
uncertainty reduction,
dependency criticality,
scope/regime gates,
provenance independence,
H/M/L allocation,
switching costs,
repair equations,
commit eligibility.

UNKNOWN/GAP:
canonical L02 equation set,
canonical variable names,
canonical units,
canonical coefficients,
canonical thresholds,
canonical allocation algorithm,
canonical H/M/L equations,
runtime equation mapping,
executed validation.
```

Therefore:

```text
CONCLUSION CLASS:
MODEL / CONDITIONAL

NOT:
VERIFIED L02 CANON

NOT:
IMPLEMENTED RUNTIME

NOT:
EMPIRICALLY VALIDATED
```

```text

The highest-value unresolved gap is the **canonical L02 equation registry**. Until that is recovered, the budget and allocation equations above should remain a coherent AMOS mathematical specification rather than being promoted into Trang Phan’s source canon.
```

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: l02_attention_primitives_cognitive_matrix_equations
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L02_ATTENTION/L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_EQUATIONS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
