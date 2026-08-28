---
title: K HML
type: note
source: 02_KERNEL/09_INTEGRATION
tags:
- kernel
- integration
- note
- canon/kernel
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# K HML — Full Canonical Reconstruction

**Status:** `AMOS_MODEL / CANON-CANDIDATE`
**Conclusion class:** `MODEL`
**AMOS Core target:** `v4.4`
**Origin architect / steward:** Trang Phan

I broadened the corpus search beyond the literal filename. The relevant AMOS corpus contains major architecture/state artifacts including **AMOS [[ARCHITECTURE]]**, **AMOS OS**, the max-detail Reality Architecture master, and the Trang Reality Architecture corpus.

There is still no independently identified artifact titled `K_HML`. Therefore the document below is the **full kernel reconstruction consistent with the supplied AMOS v4.4 H/M/L contract**, not falsely presented as a verbatim historical source file.

```yaml
---
artifact_id: AMOS-OS-K-HML
canonical_name: K_HML
artifact_type: fractal_abstraction_retrieval_kernel

status: CANON_CANDIDATE
conclusion_class: MODEL

amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan

canonical_location: 02_KERNEL/K_HML.md
plane: KERNEL
scope: AMOS_OS

updated: 2026-08-26
---
```

# K HML

> H/M/L is the AMOS fractal abstraction,
> retrieval, dependency-localization,
> and evidence-escalation architecture.

---

# 0. Epistemic Boundary

H/M/L MUST NOT be interpreted as:

- proof that every AMOS artifact is already indexed;
- proof that every H/M/L node has persistent runtime storage;
- empirical validation of AMOS models;
- permission to infer missing L-level evidence from H-level summaries;
- permission to treat compression as evidence;
- permission to treat hierarchy as causation.

Canonical distinction:

H/M/L STRUCTURE
!=
EMPIRICAL [[VALIDATION]]

H/M/L LOCATION
!=
TRUTH

H/M/L COMPRESSION
!=
PROOF

H/M/L PARENTAGE
!=
CAUSATION

---

# 1. Purpose

K_HML governs how AMOS moves between:

H = HIGH / DOMAIN / MACRO ABSTRACTION

M = MIDDLE / SUBSYSTEM / MECHANISM

L = LOW / DETAIL / EVIDENCE-PROXIMAL LAYER

The architecture exists to prevent two opposite failures:

1. loading the entire knowledge universe for every question;
2. answering from compressed abstractions when decisive evidence lies below them.

---

# 2. Fundamental Structure

Canonical topology:

ROOT
 ↓
H
 ↓
M
 ↓
L
 ↓
RAW EVIDENCE

Operationally:

BOOTSTRAP CAPSULE
 ↓
H DOMAIN
 ↓
M SUBSYSTEM
 ↓
L DETAIL
 ↓
RAW EVIDENCE
   only when required

Default:

RAW_EVIDENCE = DO_NOT_LOAD_UNLESS_REQUIRED

---

# 3. H Layer

H represents the broadest decision-useful semantic region below the root/bootstrap layer.

Examples:

H_KERNEL
H_MEMORY
H_GOVERNANCE
H_COGNITION
H_PROVENANCE
H_CAUSALITY
H_SECURITY
H_RUNTIME
H_AGENTS
H_KNOWLEDGE

H answers primarily:

WHAT DOMAIN
OF THE SYSTEM
MATTERS?

H should contain enough information to determine whether deeper traversal is necessary.

It should not pretend to contain all M/L evidence.

---

# 4. M Layer

M represents a subsystem, mechanism, model, bounded problem region, or intermediate dependency structure within H.

Example:

H_MEMORY
 ├── M_ADMISSION
 ├── M_RETRIEVAL
 ├── M_CONFLICT
 ├── M_IMMUNE
 └── M_COMPACTION

M answers:

WHICH MECHANISM
INSIDE THE DOMAIN
CAN CHANGE THE ANSWER?

M is the principal routing layer between broad abstraction and detailed evidence.

---

# 5. L Layer

L represents the narrow detailed layer needed to resolve a concrete dependency.

Possible L objects include:

RULE
CONSTRAINT
EQUATION
SCHEMA
STATE
TEST RESULT
VERSION
CLAIM
PROVENANCE EDGE
COUNTEREXAMPLE
FALSIFIER
MEASUREMENT
AUTHORITY TOKEN
POLICY CLAUSE
IMPLEMENTATION DETAIL

L answers:

WHICH SPECIFIC DETAIL
IS LOAD-BEARING?

---

# 6. Raw Evidence Layer

Raw evidence is below ordinary H/M/L traversal.

Examples:

SOURCE FILE
TEST OUTPUT
LOG
TRACE
DATABASE RECORD
EXPERIMENT RESULT
PRIMARY DOCUMENT
SIGNED RECORD
OBSERVATION
CODE IMPLEMENTATION

Raw evidence is loaded when abstraction is insufficient.

Rule:

DO NOT LOAD RAW EVIDENCE
MERELY BECAUSE IT EXISTS.

LOAD IT WHEN IT CAN
MATERIALLY ALTER
THE CONCLUSION.

---

# 7. H/M/L Is Fractal

H, M, and L are relative roles, not globally fixed physical depths.

A node that is L relative to one problem may become H relative to a narrower problem.

Example:

H_MEMORY
 ↓
M_RETRIEVAL
 ↓
L_SCORING

Zoom into scoring:

H_SCORING
 ↓
M_PROVENANCE_WEIGHT
 ↓
L_SOURCE_ANCESTRY

Therefore:

H/M/L = RELATIVE FRACTAL SCALE

not:

H/M/L = THREE ABSOLUTE DATABASE TABLES

---

# 8. Recursive Definition

For knowledge region K:

H(K) = high-level representation of K

M(K) = decision-relevant decomposition of H(K)

L(K) = detail sufficient to resolve M(K)

And any L node may recursively expose:

L
→ H'
→ M'
→ L'

when further zoom is required.

---

# 9. Resolution Operator

Define:

Resolve(q, n)

where:

q = current question
n = current H/M/L node

Resolution stops when the node contains sufficient evidence to satisfy the decision contract.

Conceptually:

Resolve(q,n) =
  ANSWER(n)
  if Sufficiency(q,n)

otherwise:

  Resolve(
    q,
    RelevantChildren(q,n)
  )

---

# 10. Materiality Gate

A child should be traversed only if:

Material(child,q) = TRUE

Conceptually:

Material(c,q)
iff

Changing(c)
could change
Claim(q)
or
Decision(q)
or
Action(q)

Therefore:

IRRELEVANT DEPENDENCY
→ DO NOT LOAD

POTENTIALLY
DECISION-CHANGING
DEPENDENCY
→ LOAD / TEST

---

# 11. Smallest Sufficient Proof Scope

H/M/L implements:

SMALLEST
SUFFICIENT
PROOF SCOPE

Do not retrieve:

ALL H
ALL M
ALL L
ALL RAW EVIDENCE

when:

H_A
→ M_A2
→ L_A2.3

is sufficient.

---

# 12. Dependency-Directed Traversal

Traversal is not breadth-first by default.

Preferred:

QUESTION
 ↓
LOAD-BEARING H
 ↓
LOAD-BEARING M
 ↓
LOAD-BEARING L
 ↓
EVIDENCE IF REQUIRED

Not:

QUESTION
 ↓
EVERYTHING AMOS KNOWS

---

# 13. Bootstrap Capsule

Before H traversal, AMOS may use a compact bootstrap capsule containing the minimum routing state.

Conceptual fields:

bootstrap_capsule:
  objective
  scope
  stakes
  freshness_requirement
  active_regime
  relevant_domains
  authority_context
  known_constraints
  known_conflicts
  unresolved_gaps
  proof_capsule_refs

The bootstrap capsule is routing context.

It is not a substitute for evidence.

---

# 14. Retrieval Contract

Canonical retrieval:

BOOTSTRAP
→ H
→ M
→ L
→ RAW

but descent is conditional.

Allowed termination:

BOOTSTRAP → ANSWER

H → ANSWER

H → M → ANSWER

H → M → L → ANSWER

H → M → L → RAW → ANSWER

depending on sufficiency.

---

# 15. Downward Escalation Conditions

Descend H→M when:

H is ambiguous
OR
multiple M mechanisms could alter outcome
OR
H compression hides load-bearing uncertainty
OR
scope cannot be established
OR
conflict exists.

Descend M→L when:

specific rule/evidence is load-bearing
OR
mechanisms compete
OR
threshold sensitivity exists
OR
provenance independence is unresolved
OR
causal typing is unresolved.

Descend L→RAW when:

L is merely a derived summary
OR
primary evidence is required
OR
provenance must be verified
OR
freshness is material
OR
contradiction cannot otherwise be resolved
OR
stakes require direct validation.

---

# 16. Upward Compression

After lower-level resolution:

RAW
→ L
→ M
→ H
→ PROOF CAPSULE

But upward compression must preserve load-bearing distinctions.

Compression must not erase:

CONTRADICTIONS
FALSIFIERS
SCOPE
REGIME
PROVENANCE
DEPENDENCIES
UNCERTAINTY
AUTHORITY
FRESHNESS

---

# 17. Lossless-for-Decision Compression

H/M/L compression need not preserve every token.

It must preserve every fact capable of changing the supported decision.

Define:

DecisionLoss(C) = information removed by compression that could change the supported decision.

Required:

DecisionLoss(C) = 0

for the declared decision envelope.

This is a structural requirement, not a universal mathematical theorem.

---

# 18. Proof Capsule Coupling

An important H/M/L conclusion should be reusable through a proof capsule containing conceptually:

claim
class
premises
evidence
provenance
scope
regime
freshness
dependencies
competing explanations
falsifiers
confidence ceiling

H/M/L provides retrieval topology.

Proof capsules provide reusable validated conclusion topology.

---

# 19. RSCF Coupling

H/M/L and RSCF are related but not identical.

H/M/L:
WHERE / HOW DEEP
TO RETRIEVE

RSCF:
HOW REASONING
DEPENDENCIES ARE
STRUCTURED

Conceptually:

H
 ↓
M
 ↓
L

may contain:

RSCF
├── H
├── M
└── L

at any relevant scale.

Therefore H/M/L is recursively composable with RSCF.

---

# 20. GMEF Coupling

GMEF may use H/M/L to localize the scope of governed evolution.

Example:

H_RUNTIME
 ↓
M_ROUTING
 ↓
L_WEIGHT_VECTOR

A permitted L-level mutation does not imply permission to mutate:

M_ROUTING GOVERNANCE

or:

H_RUNTIME CONSTITUTION

Therefore:

LOWER-LEVEL
MUTATION AUTHORITY
!=
UPWARD AUTHORITY

---

# 21. Upward Authority Firewall

Permission at L does not imply permission at M.

Permission at M does not imply permission at H.

Formally:

Authority(L)
↛ Authority(M)

Authority(M)
↛ Authority(H)

unless explicit authority inheritance exists.

---

# 22. Downward Constraint Propagation

Valid H-level constraints propagate downward when applicable.

If:

Constraint C
applies to H

and M,L ∈ Scope(C)

then:

C(H)
→ C(M)
→ C(L)

But scope must be established.

A constraint cannot silently propagate outside its applicability envelope.

---

# 23. Upward Evidence Propagation

Evidence may propagate upward only through valid derivation.

RAW OBSERVATION
 ↓
L CLAIM
 ↓
M CONCLUSION
 ↓
H CONCLUSION

At every transition:

support must remain valid
scope must remain compatible
regime must remain compatible
provenance must remain traceable.

---

# 24. Weakest-Premise Ceiling

For derived H conclusion:

H* = f(M1,...,Mn)

and each M depends on L evidence.

Then:

Confidence(H*)
≤
weakest
load-bearing premise

unless that premise is independently revalidated or bypassed through another valid proof path.

---

# 25. No Confidence Inflation by Abstraction

Compression cannot increase epistemic strength.

Therefore:

L = CONDITIONAL
→ M cannot become VERIFIED
merely through summarization.

M = MODEL
→ H cannot become VERIFIED
merely through aggregation.

UNKNOWN/GAP
cannot disappear
because it was omitted
from a higher layer.

---

# 26. Provenance Preservation

Every material node should conceptually support:

node_id
layer
parent
children
source_refs
source_ancestry
claim_class
scope
regime
freshness
dependencies
conflicts
falsifiers
version

This permits upward conclusions to remain traceable.

---

# 27. Provenance Independence

Two L nodes are not independent merely because they are different nodes.

Example:

SOURCE S
 ├── L1
 ├── L2
 └── L3

does not establish three independent confirmations.

H/M/L must therefore interact with:

[[K_PROVENANCE]]
[[K_PROVENANCE_TOPOLOGY]]
[[K_SYBIL_HARDENING]]

---

# 28. Correlated Branches

If:

M_A ← Source S
M_B ← Source S

then:

Agreement(M_A,M_B)

has correlated provenance.

Do not count it as independent convergence.

---

# 29. Contradiction Preservation

Suppose:

L1 supports A
L2 supports ¬A

Then M must not silently compress them into A.

Allowed:

M:
  status = COMPETING
  branches = [A, ¬A]

Until discriminating evidence exists.

---

# 30. Competing Hypothesis Branching

At M:

M
├── HYPOTHESIS A
├── HYPOTHESIS B
└── HYPOTHESIS C

Each may descend through different L evidence.

Do not force convergence merely because the parent M expects one output.

---

# 31. Cheapest Discriminating Descent

When competing branches exist:

choose the cheapest L/raw test
with the highest expected ability
to distinguish them.

Not:

collect more redundant evidence
for every branch.

---

# 32. Causal Firewall

H/M/L hierarchy does not license causal inference.

H contains A
M contains B
L observes C

does not prove:

A → B → C

Hierarchical containment is structural.

Causal edges require appropriately typed evidence.

---

# 33. Structural vs Causal Edges

Allowed edge types should distinguish:

CONTAINS
DEPENDS_ON
DERIVED_FROM
CONSTRAINS
GOVERNS
OBSERVES
CAUSES
ENABLES
MEDIATES
CONFOUNDS
INVALIDATES

Never silently translate:

CONTAINS
→ CAUSES

or:

PRECEDES
→ CAUSES

---

# 34. Scope Envelope

Each material H/M/L node may carry:

scope:
  system
  population
  environment
  scale
  time
  regime
  measurement_method
  assumptions

A child conclusion cannot be generalized upward beyond its scope without separate justification.

---

# 35. Scope Intersection

If H conclusion depends on M1 and M2:

ValidScope(H)
⊆
Scope(M1)
∩
Scope(M2)

for load-bearing joint claims unless a valid transfer rule exists.

---

# 36. Regime Firewall

Evidence valid under regime R1:

L@R1

cannot automatically support:

M@R2

when the changed regime affects load-bearing assumptions.

Required:

REVALIDATE
or
DOWNGRADE
or
PRESERVE GAP

---

# 37. Freshness

Every reusable node may carry:

observed_at
validated_at
valid_until
freshness_policy

Freshness is dependency-specific.

A ten-year-old mathematical definition may remain valid.

A ten-minute-old runtime state may already be stale.

---

# 38. Freshness Propagation

If H depends load-bearingly on stale L:

Stale(L)
⇒
StaleDependent(H)

unless another valid path independently supports H.

Do not invalidate unrelated branches.

---

# 39. Selective Invalidation

Canonical:

Invalid(p)
⇒
invalidate only
dependent descendants(p)

Example:

H
├── M1
│   └── L1 ← invalid
└── M2
    └── L2 ← valid

Then:

invalidate M1-dependent conclusions.

Do not automatically destroy M2.

---

# 40. Dependency Closure

Before local reasoning terminates at a node, establish that all dependencies capable of changing the answer are either:

resolved,
validly encapsulated,
or explicitly marked GAP.

This is:

DEPENDENCY CLOSURE

---

# 41. Local Fast Path

Local H/M/L reasoning is permitted when:

dependency closure established
AND
provenance independence adequate
AND
scope compatible
AND
regime compatible
AND
freshness adequate
AND
no material conflict
AND
no hidden causal coupling
AND
authority sufficient.

Then:

LOCAL FINALIZATION
MAY PROCEED

---

# 42. Escalation Conditions

Escalate retrieval when:

shared ancestry discovered
conflict discovered
stale premise discovered
scope crossing occurs
regime shift occurs
causal ambiguity is material
governance is affected
irreversible stakes increase
dependency ambiguity remains
proof capsule invalidated.

---

# 43. Atomic Multi-H/M/L Reasoning

Some decisions span multiple branches:

H_A → M_A → L_A
H_B → M_B → L_B

If correctness depends jointly on both:

VALIDATE
{A,B}
ATOMically
AT DECISION BOUNDARY

Do not finalize one branch independently if the other can invalidate the joint decision.

---

# 44. Cross-H Coupling

Different H domains may interact.

Example:

H_MEMORY
↔
H_AUTHORITY

A memory mutation may be technically valid but unauthorized.

Therefore separate H branches are not automatically independent.

---

# 45. Cross-Layer Constraint Interaction

A low-level optimization may violate a higher-level invariant.

Example:

L_LATENCY
improves

but:

H_PRIVACY
constraint fails.

Result:

REJECT / CONDITION

Performance improvement cannot override a valid hard constraint.

---

# 46. Sensitivity

For a conclusion C, identify:

smallest premise
threshold
assumption
observation

whose change would flip C.

Then descend first into that H/M/L path.

This prevents spending retrieval budget on noncritical background.

---

# 47. Fragility

If small plausible changes in L produce a different H conclusion:

H conclusion = CONDITIONAL / FRAGILE

If H survives plausible noncritical perturbations:

H conclusion = ROBUST
within stated scope.

---

# 48. Gap Classification

Missing H/M/L content should be classified:

CRITICAL
DECISION_RELEVANT
EXPLANATORY
COSMETIC

Resolve in that order.

A cosmetic missing L detail must not block a decision when all load-bearing dependencies are already resolved.

A critical gap must.

---

# 49. Unknown Propagation

If a load-bearing L node is UNKNOWN:

L = UNKNOWN

then M must not fabricate resolution.

Allowed:

M = UNKNOWN/GAP

or:

M = CONDITIONAL
on explicit assumption A.

The assumption must remain visible.

---

# 50. Retrieval Budget

Reasoning cost should be spent where:

ExpectedDecisionValue(
  uncertainty reduction
)
> retrieval cost

This is a decision heuristic, not an empirical law.

---

# 51. Adaptive Complexity

H/M/L maps naturally to AMOS adaptive complexity.

C0:
direct answer from valid capsule/bootstrap

C1:
H-level check

C2:
H→M structured reasoning

C3:
H→M→L deep validation

C4:
H→M→L→RAW
plus adversarial validation,
competing hypotheses,
provenance topology,
causal/scope analysis.

---

# 52. Complexity Escalation

Escalate complexity for:

stakes
irreversibility
novelty
weak evidence
stale evidence
contradiction
causal ambiguity
scope mismatch
competing models
governance impact
low trust
explicit deep-analysis request.

---

# 53. Complexity De-escalation

Once outcome-changing uncertainty is resolved:

STOP DESCENDING.

Do not continue retrieval merely to maximize apparent completeness.

---

# 54. Stop Conditions

H/M/L retrieval may stop when:

Claim Sufficiency
AND
Decision Sufficiency
AND
Action Sufficiency

are satisfied.

Or when:

further retrieval
has negligible expected
decision value.

---

# 55. Claim Sufficiency

Claim sufficiency exists when the requested conclusion is supported to the required epistemic class.

Do not retrieve implementation details if the user only requires a supported architectural definition.

---

# 56. Decision Sufficiency

Decision sufficiency exists when unresolved uncertainty cannot reasonably change the decision inside the stated scope.

---

# 57. Action Sufficiency

Action sufficiency exists when there is enough validated information to select a safe next action.

The entire ontology need not be resolved first.

---

# 58. Failure Recovery

When a path fails:

do not restart from ROOT
unless necessary.

Instead:

identify failed premise
invalidate dependent path
return to nearest valid node
select alternate branch
reuse unaffected proof capsules.

---

# 59. No Failed-Path Repetition

A failed retrieval/reasoning path should not be repeated unless something changed:

NEW EVIDENCE
NEW SCOPE
NEW ASSUMPTION
NEW REGIME
NEW METHOD
NEW AUTHORITY
NEW PROVENANCE PATH

---

# 60. H/M/L Memory Admission

Not every traversed node belongs in persistent memory.

Persistence should depend on:

future utility
provenance quality
stability
scope clarity
conflict state
sensitivity
revalidation cost
governance requirements.

---

# 61. Context Compaction

Resolved H/M/L paths may be compacted into proof capsules.

Instead of retaining:

all raw evidence tokens

retain:

claim
premises
references
scope
regime
freshness
dependencies
falsifiers
confidence ceiling

provided reconstruction remains possible when needed.

---

# 62. Compaction Invalidation

If a proof capsule dependency changes:

do not trust the capsule merely because its text remains available.

Check:

dependency versions
scope
regime
freshness
provenance
conflicts.

---

# 63. Version Binding

Material H/M/L nodes should be version-bindable.

Conceptually:

NodeRef =
(
  node_id,
  version,
  epoch
)

A conclusion derived from:

L@v3

must not silently be represented as derived from:

L@v4

without revalidation.

---

# 64. MVCC Concept

For mutable H/M/L state:

READ
Node@V

↓

REASON

↓

COMMIT / ACT

↓

CURRENT_VERSION == V ?

If no:

revalidate affected dependency closure.

This is an architectural concept, not a claim that every H/M/L corpus store implements MVCC.

---

# 65. CAS Concept

Where state mutation is relevant:

CAS(
 expected_version = V,
 new_state = V'
)

Failure:

RELOAD
REVALIDATE
DO NOT BLIND WRITE

Again, conceptual unless runtime implementation evidence exists.

---

# 66. Causal Epoch Binding

A conclusion whose load-bearing path depends on causal model epoch E should carry:

causal_epoch = E

If causal model changes materially:

invalidate only dependent conclusions.

---

# 67. Governance Epoch Binding

Likewise:

governance_epoch = G

A previously allowed L-level action may become unauthorized after G changes.

Epistemic validity and authorization validity are separate.

---

# 68. Identity Binding

H/M/L retrieval involving actors, resources, tools, memories, or targets should bind to stable identity where material.

NAME MATCH
!=
IDENTITY PROOF

---

# 69. Authority Binding

A correct conclusion does not itself authorize action.

Therefore:

KNOW(C)
!=
AUTHORIZED(ACT(C))

H/M/L reasoning must pass action requests to applicable authority/governance kernels.

---

# 70. Effect Classification

Before executing an action derived from H/M/L reasoning, classify its effects.

Possible dimensions:

READ_ONLY
REVERSIBLE
STATE_MUTATING
EXTERNAL
IRREVERSIBLE
HIGH_CONSEQUENCE
INFORMATION_EXPOSING

Required validation increases with consequence.

---

# 71. Information Exposure

Retrieval depth itself may expose sensitive information.

Therefore:

NEED TO REASON
does not imply
NEED TO DISPLAY

H/M/L retrieval and output disclosure are distinct operations.

---

# 72. Raw Evidence Firewall

Raw evidence may be necessary internally while inappropriate to reproduce fully.

Return:

smallest sufficient supported result

while preserving provenance references where permitted.

---

# 73. Cross-Domain Mapping

Structural similarity between:

H_A/M_A/L_A

and:

H_B/M_B/L_B

may generate a MODEL or hypothesis.

It does not establish empirical equivalence or causation.

---

# 74. Analogy Firewall

A pattern observed in one H domain:

PATTERN_A

mapped to another:

PATTERN_B

remains:

MODEL

until independently validated in B.

---

# 75. H/M/L Node Schema

Conceptually:

hml_node:
  node_id:
  layer: H | M | L

  title:
  semantic_type:

  parent_refs: []
  child_refs: []

  claim_class:
  claims: []

  dependencies: []
  constraints: []

  source_refs: []
  provenance_ancestry: []

  scope:
  regime:
  freshness:

  conflicts: []
  competing_hypotheses: []
  falsifiers: []

  authority_context:
  governance_epoch:
  causal_epoch:

  version:
  valid_from:
  valid_until:

  raw_evidence_refs: []

  load_policy:
  invalidation_policy:
  compaction_policy:

---

# 76. H Node Schema

h_node:
  domain_id:
  domain_definition:
  domain_boundary:

  principal_subsystems: []

  constitutional_constraints: []

  active_conflicts: []

  high_level_proof_capsules: []

  routing_map: []

  escalation_conditions: []

---

# 77. M Node Schema

m_node:
  subsystem_id:
  parent_h:

  mechanism:
  state:

  competing_models: []

  relevant_constraints: []

  l_dependencies: []

  discriminating_tests: []

  local_proof_capsules: []

---

# 78. L Node Schema

l_node:
  detail_id:
  parent_m:

  claim:
  claim_class:

  evidence_refs: []
  source_ancestry: []

  assumptions: []
  falsifiers: []

  scope:
  regime:
  freshness:

  implementation_refs: []
  test_refs: []

---

# 79. H/M/L Edge Schema

hml_edge:
  edge_id:

  from:
  to:

  edge_type:
    CONTAINS |
    DEPENDS_ON |
    DERIVED_FROM |
    CONSTRAINS |
    GOVERNS |
    OBSERVES |
    CAUSES |
    ENABLES |
    MEDIATES |
    CONFOUNDS |
    INVALIDATES

  load_bearing:
  scope:
  regime:

  provenance:
  version:

---

# 80. Retrieval Request Schema

hml_retrieval_request:
  objective:
  requested_output:

  scope:
  stakes:
  freshness_requirement:

  starting_capsule:

  candidate_h_domains: []

  decision_changing_uncertainty: []

  maximum_depth:

  raw_evidence_policy:
    DO_NOT_LOAD_UNLESS_REQUIRED

---

# 81. Retrieval Result Schema

hml_retrieval_result:
  conclusion:
  conclusion_class:

  traversed_path: []

  load_bearing_nodes: []

  evidence_refs: []

  unresolved_gaps: []

  competing_hypotheses: []

  scope:
  regime:
  freshness:

  falsifiers: []

  confidence_ceiling:

  invalidation_conditions: []

---

# 82. Canonical Traversal Algorithm

INPUT:
question q

1. Parse:
   objective
   scope
   stakes
   freshness
   deliverable

2. Identify:
   decision-changing uncertainty

3. Load:
   bootstrap capsule

4. Select:
   smallest relevant H set

5. For each load-bearing H:
   inspect proof capsule / routing state

6. Descend to M only if H insufficient.

7. Descend to L only if M insufficient.

8. Load raw evidence only if L cannot establish required support.

9. Check:
   provenance
   conflicts
   scope
   regime
   freshness
   causal type
   authority where relevant

10. Challenge consequential conclusions through an independent path where available.

11. Preserve COMPETING when discrimination fails.

12. Synthesize early.

13. Stop when:
   Claim Sufficiency
   Decision Sufficiency
   Action Sufficiency

14. Emit:
   conclusion
   class
   decisive evidence
   material uncertainty
   invalidation conditions.

---

# 83. Adversarial H/M/L Validation

For consequential conclusion C:

PATH A:
construct strongest supported C.

PATH B:
seek failure through a genuinely different route.

Challenge for:

contradiction
correlated provenance
stale premises
scope leakage
hidden dependency
causal overreach
stronger alternative
authority mismatch
regime shift.

If challenge succeeds:

DOWNGRADE
or
CONDITION
or
COMPETING
or
UNKNOWN/GAP.

---

# 84. Independence Requirement

A second traversal is useful only if materially independent.

Rephrasing the same M node through another agent does not establish independence.

Independence should consider:

source ancestry
data lineage
model lineage
shared assumptions
shared preprocessing
shared authority
shared causal model.

---

# 85. Proof-Based Coordination Avoidance

A local H/M/L branch may finalize without global coordination when proof establishes:

all decision-changing mutable dependencies are inside closure
OR
external mutable dependencies cannot affect the result.

Absence of observed conflict is insufficient.

---

# 86. Shard-Local Finalization

If an H/M/L region is sharded:

Shard S may finalize locally only when:

dependency closure is local
AND
cross-shard dependencies are immutable or proven irrelevant
AND
authority is local and sufficient
AND
causal/governance epochs are compatible.

This is a v4.4 reasoning concept, not evidence that every AMOS store has distributed shard implementation.

---

# 87. Anti-Sybil Rule

N descendant summaries from one source are one ancestry family.

Evidence weight must account for topology.

Therefore:

COUNT(NODES)
!=
COUNT(INDEPENDENT SOURCES)

---

# 88. Anti-Fluency Rule

A smooth H summary cannot repair missing L evidence.

If:

L = GAP

then H must expose the gap when load-bearing.

Never bridge:

UNKNOWN
→ fluent prose
→ apparent certainty.

---

# 89. Anti-Completeness Rule

H/M/L prioritizes:

INTEGRITY
>
COMPLETENESS
>
FLUENCY
>
SPEED
>
TOKEN SAVINGS

Therefore incomplete but valid output dominates complete fabrication.

---

# 90. Anti-Overretrieval Rule

More context can reduce integrity through:

noise
contradiction masking
stale evidence
provenance confusion
attention dilution
scope mixing.

Therefore retrieval volume is not monotonic with answer quality.

---

# 91. Anti-Underretrieval Rule

Conversely:

FAST ANSWER
cannot justify
stopping above
a decision-changing uncertainty.

If L/raw evidence can flip a consequential conclusion:

DESCEND.

---

# 92. Canonical H/M/L Laws

KHML-001
H/M/L MUST BE
TREATED AS A
FRACTAL ABSTRACTION
AND RETRIEVAL SYSTEM.

KHML-002
H REPRESENTS
THE RELEVANT
HIGH-LEVEL DOMAIN.

KHML-003
M REPRESENTS
THE RELEVANT
SUBSYSTEM OR MECHANISM.

KHML-004
L REPRESENTS
THE RELEVANT
DETAIL OR
EVIDENCE-PROXIMAL NODE.

KHML-005
RAW EVIDENCE MUST
DEFAULT TO
DO_NOT_LOAD_UNLESS_REQUIRED.

KHML-006
TRAVERSAL MUST FOLLOW
DECISION-RELEVANT
DEPENDENCIES.

KHML-007
IRRELEVANT BRANCHES
SHOULD NOT BE LOADED.

KHML-008
H/M/L DEPTH MUST BE
RELATIVE AND FRACTAL,
NOT ASSUMED ABSOLUTE.

KHML-009
AN L NODE MAY BECOME
AN H NODE UNDER
FURTHER ZOOM.

KHML-010
COMPRESSION MUST NOT
ERASE LOAD-BEARING
CONTRADICTIONS.

KHML-011
COMPRESSION MUST NOT
INCREASE CLAIM CLASS.

KHML-012
UNKNOWN MUST NOT
DISAPPEAR THROUGH
SUMMARIZATION.

KHML-013
DERIVED CONFIDENCE
MUST NOT EXCEED THE
WEAKEST LOAD-BEARING
PREMISE WITHOUT
REVALIDATION.

KHML-014
NODE MULTIPLICITY
MUST NOT BE TREATED
AS PROVENANCE
INDEPENDENCE.

KHML-015
STRUCTURAL HIERARCHY
MUST NOT BE TREATED
AS CAUSAL HIERARCHY.

KHML-016
SCOPE MUST PROPAGATE
THROUGH LOAD-BEARING
DERIVATIONS.

KHML-017
REGIME CHANGES MUST
INVALIDATE STALE
DEPENDENT CONCLUSIONS.

KHML-018
FRESHNESS MUST BE
DEPENDENCY-SPECIFIC.

KHML-019
INVALIDATION MUST BE
SELECTIVE.

KHML-020
LOCAL FINALIZATION
REQUIRES DEPENDENCY
CLOSURE.

KHML-021
CONFLICT MUST TRIGGER
BRANCHING OR
ESCALATION WHEN
MATERIAL.

KHML-022
GENUINE COMPETING
HYPOTHESES MUST
REMAIN COMPETING
UNTIL DISCRIMINATED.

KHML-023
THE CHEAPEST
HIGH-INFORMATION
DISCRIMINATING TEST
SHOULD BE PREFERRED.

KHML-024
CROSS-DOMAIN ANALOGY
MUST REMAIN MODEL
UNTIL VALIDATED.

KHML-025
PERMISSION AT L
MUST NOT IMPLY
PERMISSION AT M OR H.

KHML-026
HIGHER-LEVEL VALID
CONSTRAINTS MUST
PROPAGATE DOWNWARD
ONLY WITHIN SCOPE.

KHML-027
EVIDENCE MAY PROPAGATE
UPWARD ONLY THROUGH
VALID DERIVATION.

KHML-028
RAW EVIDENCE
RETRIEVAL MUST NOT
IMPLY RAW EVIDENCE
DISCLOSURE.

KHML-029
PROOF CAPSULE REUSE
REQUIRES VALID
DEPENDENCIES,
SCOPE,
REGIME,
FRESHNESS,
AND PROVENANCE.

KHML-030
FAILED PATHS MUST
NOT BE REPEATED
WITHOUT CHANGED
EVIDENCE OR METHOD.

KHML-031
REASONING SHOULD
ROLL BACK TO THE
NEAREST VALID NODE.

KHML-032
MULTI-H BRANCHES
MUST BE ATOMIC
WHEN JOINT STATE IS
LOAD-BEARING.

KHML-033
CROSS-H COUPLING
MUST NOT BE
ASSUMED ABSENT.

KHML-034
SENSITIVITY SHOULD
DIRECT RETRIEVAL
TOWARD THE PREMISE
MOST ABLE TO FLIP
THE RESULT.

KHML-035
CRITICAL GAPS MUST
DOMINATE COSMETIC
GAPS.

KHML-036
RETRIEVAL SHOULD STOP
WHEN CLAIM,
DECISION,
AND ACTION
SUFFICIENCY ARE MET.

KHML-037
MORE RETRIEVAL MUST
NOT BE EQUATED WITH
MORE TRUTH.

KHML-038
LESS RETRIEVAL MUST
NOT BE EQUATED WITH
MORE EFFICIENCY IF
DECISION-CHANGING
UNCERTAINTY REMAINS.

KHML-039
H/M/L NODE STATE
SHOULD REMAIN
VERSION-BINDABLE
WHEN MUTABLE.

KHML-040
STALE VERSION
ASSUMPTIONS MUST BE
REVALIDATED AT
COMMIT WHEN
LOAD-BEARING.

KHML-041
CAUSAL EPOCHS MUST
BE PRESERVED WHEN
CAUSAL DEPENDENCIES
ARE LOAD-BEARING.

KHML-042
GOVERNANCE EPOCHS
MUST BE PRESERVED
WHEN AUTHORITY IS
LOAD-BEARING.

KHML-043
KNOWLEDGE VALIDITY
MUST REMAIN DISTINCT
FROM ACTION AUTHORITY.

KHML-044
IDENTITY SIMILARITY
MUST NOT REPLACE
IDENTITY BINDING.

KHML-045
OUTPUT DISCLOSURE
MUST REMAIN DISTINCT
FROM INTERNAL
RETRIEVAL NEED.

KHML-046
ADVERSARIAL
[[VALIDATION]] SHOULD
USE A GENUINELY
DIFFERENT PATH.

KHML-047
CORRELATED CHALLENGE
PATHS MUST NOT
MASQUERADE AS
INDEPENDENT
[[VALIDATION]].

KHML-048
LOCAL COORDINATION
AVOIDANCE MUST BE
PROOF-BASED.

KHML-049
SHARD-LOCAL
FINALIZATION MUST
REQUIRE PROVEN
LOCAL CLOSURE.

KHML-050
INTEGRITY MUST
DOMINATE RETRIEVAL
SPEED.

---

# 93. Negative Tests

H SUMMARY
→ VERIFIED
WITHOUT EVIDENCE
MUST FAIL

THREE L NODES
FROM SAME SOURCE
→ THREE INDEPENDENT
CONFIRMATIONS
MUST FAIL

H CONTAINS M
→ H CAUSES M
MUST FAIL

M VALID IN R1
→ M VALID IN R2
MUST FAIL WHEN
REGIME IS MATERIAL

L AUTHORITY
→ H AUTHORITY
MUST FAIL

LOCAL SUCCESS
→ GLOBAL VALIDITY
MUST FAIL

COMPRESSED CAPSULE
WITH STALE DEPENDENCY
→ REUSE
MUST FAIL

NO CONTRADICTION
OBSERVED
→ INDEPENDENCE PROVEN
MUST FAIL

RAW EVIDENCE EXISTS
→ LOAD ALL
MUST FAIL

RAW EVIDENCE LOADED
→ DISPLAY ALL
MUST FAIL

UNKNOWN L
→ CERTAIN H
MUST FAIL

ANALOGOUS STRUCTURE
→ SAME CAUSE
MUST FAIL

MORE SOURCES
WITH SAME ANCESTRY
→ HIGHER INDEPENDENT
CONFIDENCE
MUST FAIL

OLD VERSION VALID
→ CURRENT VERSION VALID
MUST FAIL WHEN
LOAD-BEARING STATE
CHANGED

CORRECT ANSWER
→ AUTHORIZED ACTION
MUST FAIL

SEPARATE H BRANCHES
→ INDEPENDENT
MUST FAIL WITHOUT
DEPENDENCY PROOF

NO CROSS-SHARD
CONFLICT OBSERVED
→ LOCAL FINALITY
MUST FAIL

FAILED PATH
→ RETRY IDENTICALLY
MUST FAIL WITHOUT
CHANGED CONDITIONS

---

# 94. Required Test Families

H-ROUTING TEST

M-ROUTING TEST

L-DETAIL TEST

RAW-EVIDENCE-GATE TEST

FRACTAL-RECURSION TEST

SMALLEST-PROOF-SCOPE TEST

DEPENDENCY-CLOSURE TEST

UPWARD-COMPRESSION TEST

DECISION-LOSS TEST

PROOF-CAPSULE TEST

RSCF-[[INTEGRATION]] TEST

GMEF-[[INTEGRATION]] TEST

AUTHORITY-FIREWALL TEST

CONSTRAINT-PROPAGATION TEST

EVIDENCE-PROPAGATION TEST

WEAKEST-PREMISE TEST

PROVENANCE-PRESERVATION TEST

PROVENANCE-INDEPENDENCE TEST

CORRELATED-BRANCH TEST

CONTRADICTION-PRESERVATION TEST

COMPETING-HYPOTHESIS TEST

DISCRIMINATING-TEST TEST

CAUSAL-FIREWALL TEST

SCOPE-INTERSECTION TEST

REGIME-SHIFT TEST

FRESHNESS TEST

SELECTIVE-INVALIDATION TEST

FAST-PATH TEST

ESCALATION TEST

MULTI-H-ATOMICITY TEST

CROSS-H-COUPLING TEST

SENSITIVITY TEST

GAP-PRIORITY TEST

UNKNOWN-PROPAGATION TEST

ADAPTIVE-COMPLEXITY TEST

STOP-CONDITION TEST

FAILURE-RECOVERY TEST

CONTEXT-COMPACTION TEST

VERSION-BINDING TEST

COMMIT-REVALIDATION TEST

CAUSAL-EPOCH TEST

GOVERNANCE-EPOCH TEST

IDENTITY-BINDING TEST

EFFECT-CLASSIFICATION TEST

INFORMATION-EXPOSURE TEST

ANTI-SYBIL TEST

ANTI-FLUENCY TEST

ANTI-OVERRETRIEVAL TEST

ANTI-UNDERRETRIEVAL TEST

PROOF-BASED-COORDINATION TEST

SHARD-LOCAL-FINALIZATION TEST

---

# 95. RSCF Node

```yaml
RSCF-NODE:
  node_id: AMOS-OS-K-HML
  node_type: fractal_abstraction_retrieval_kernel
  domain: AMOS_OS_KERNEL
  claim_class: MODEL

  relations:

    ROOTED_IN:
      - 00_ROOT/README
      - 00_ROOT/DEPENDENCY_MAP

    GOVERNED_BY:
      - 01_CANON/AMOS_CORE_LAWS
      - 01_CANON/LAW_HIERARCHY
      - 01_CANON/AUTHORITY_CANON

    PROVENANCE_BOUND_TO:
      - 01_CANON/CANON_PROVENANCE
      - 01_CANON/SOURCE_LINEAGE
      - 01_CANON/SOURCE_REGISTRY
      - 01_CANON/CONFLICT_REGISTRY
      - 01_CANON/SUPERSESSION_LOG

    LOGIC_BOUND_TO:
      - 02_KERNEL/K_CORE19_LOGIC
      - 02_KERNEL/K_META_LOGIC

    STRUCTURE_BOUND_TO:
      - 02_KERNEL/K_STRUCTURAL_REASONING
      - 02_KERNEL/K_BINDING
      - 02_KERNEL/K_CONSTRAINT_PROPAGATION

    HYPOTHESIS_BOUND_TO:
      - 02_KERNEL/K_MULTI_HYPOTHESIS
      - 02_KERNEL/K_COUNTERFACTUAL

    PROVENANCE_TOPOLOGY_BOUND_TO:
      - 02_KERNEL/K_PROVENANCE
      - 02_KERNEL/K_PROVENANCE_TOPOLOGY
      - 02_KERNEL/K_SYBIL_HARDENING

    CAUSAL_BOUND_TO:
      - 02_KERNEL/K_CAUSAL_CLOSURE
      - 02_KERNEL/K_CAUSAL_EPOCH
      - 02_KERNEL/K_CAUSAL_HIERARCHY

    CONTEXT_BOUND_TO:
      - 02_KERNEL/K_CONTEXT_STATE
      - 02_KERNEL/K_CONTEXT_COMPACTION

    MEMORY_BOUND_TO:
      - 02_KERNEL/K_MEMORY_ADMISSION
      - 02_KERNEL/K_MEMORY_RETRIEVAL
      - 02_KERNEL/K_MEMORY_CONFLICT
      - 02_KERNEL/K_MEMORY_IMMUNE

    GOVERNANCE_BOUND_TO:
      - 02_KERNEL/K_GMEF
      - 02_KERNEL/K_CAPABILITY_AUTHORIZATION
      - 02_KERNEL/K_COMMIT_TIME_AUTHORITY

    STATE_BOUND_TO:
      - 02_KERNEL/K_SYSTEM_STATE
      - 02_KERNEL/K_WORLD_MODEL
      - 02_KERNEL/K_IDENTITY

    RECOVERY_BOUND_TO:
      - 02_KERNEL/K_COLLAPSE_RECOVERY
      - 02_KERNEL/K_HOMEOSTASIS
      - 02_KERNEL/K_REPAIR_HARM
      - 02_KERNEL/K_REPAIR_PRIORITY

    RISK_BOUND_TO:
      - 02_KERNEL/K_RISK_CONSTRAINT
      - 02_KERNEL/K_EFFECT_CLASSIFICATION
      - 02_KERNEL/K_INFORMATION_EXPOSURE

```

---

# 96. Promotion Gate

K_HML must not be promoted from CANON_CANDIDATE to implemented canon solely because this specification is coherent.

Required evidence:

[ ] exact historical H/M/L source lineage identified
[ ] terminology conflict review completed
[ ] source registry updated
[ ] supersession status established
[ ] H routing implementation verified
[ ] M routing implementation verified
[ ] L routing implementation verified
[ ] raw evidence gating verified
[ ] proof capsule integration verified
[ ] RSCF integration verified
[ ] provenance topology verified
[ ] scope/regime propagation verified
[ ] freshness invalidation verified
[ ] competing hypothesis handling verified
[ ] selective invalidation verified
[ ] context compaction verified
[ ] version binding verified
[ ] commit-time revalidation verified
[ ] multi-RSCF atomicity verified
[ ] causal epoch handling verified
[ ] shard-local finalization verified if claimed
[ ] proof-based coordination avoidance verified if claimed
[ ] adversarial tests passed

Until then:

HML [[ARCHITECTURE]] = AMOS MODEL

HML RETRIEVAL CONTRACT = AMOS v4.4 [[CANON]]-COMPATIBLE MODEL

FULL HISTORICAL K_HML SOURCE = UNKNOWN/GAP

FULL RUNTIME IMPLEMENTATION = UNKNOWN/GAP

DISTRIBUTED SHARD FINALITY = UNKNOWN/GAP

FORMAL VERIFICATION = UNKNOWN/GAP

EMPIRICAL UNIVERSALITY = UNKNOWN/GAP

---

# 97. Canonical Compression

H/M/L
IS NOT
A THREE-LEVEL
FOLDER TREE.

IT IS A
FRACTAL
REASONING AND
RETRIEVAL CONTRACT.

START WITH
THE SMALLEST
VALID CONTEXT.

FIND THE H
THAT CAN CHANGE
THE ANSWER.

FIND THE M
THAT CARRIES
THE MECHANISM.

FIND THE L
THAT CARRIES
THE LOAD-BEARING
DETAIL.

LOAD RAW EVIDENCE
ONLY WHEN REQUIRED.

DO NOT CONFUSE
COMPRESSION
WITH PROOF.

DO NOT CONFUSE
STRUCTURE
WITH CAUSATION.

DO NOT CONFUSE
MULTIPLE DESCENDANTS
WITH INDEPENDENT
SOURCES.

DO NOT ERASE
CONTRADICTIONS
WHILE MOVING UPWARD.

DO NOT EXPAND
LOCAL VALIDITY
BEYOND ITS
SCOPE OR REGIME.

DO NOT LET
A STALE L
SUPPORT A
FRESH H.

DO NOT INVALIDATE
THE WHOLE TREE
WHEN ONE BRANCH
FAILS.

DESCEND ONLY
AS FAR AS
THE DECISION
REQUIRES.

ESCALATE WHEN
INTEGRITY
REQUIRES IT.

STOP WHEN
CLAIM,
DECISION,
AND ACTION
SUFFICIENCY
ARE ACHIEVED.

INTEGRITY
>
COMPLETENESS
>
FLUENCY
>
SPEED
>
TOKEN SAVINGS.

The provenance boundary is important: the Drive corpus clearly contains very large AMOS architecture sources—the main `AMOS ARCHITECTURE.md` is ~841 KB, `AMOS OS.md` ~751 KB, and the max-detail Reality Architecture master ~2.16 MB.    The corpus also contains later Core branches such as v4.7, v4.8, v5.3, and v5.8; I have **not** silently imported those later-version semantics into the v4.4 target above.

So this is suitable as the **full `K_HML` canon-candidate specification**, but the honest class remains `MODEL` until the exact historical H/M/L source and runtime evidence are bound through the source registry and supersession process.

---

[[00_ROOT_MOC]]|[[AMOS MOC]]

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
**MOC:** [[09_INTEGRATION_MOC]]
