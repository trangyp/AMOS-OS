---
title: "FRACTAL_KNOWLEDGE_NETWORK Specification"
aliases:
  - "FRACTAL_KNOWLEDGE_NETWORK"
  - "Fractal Knowledge Network"
  - "FKN"
  - "H/M/L Knowledge Network"
type: core_law
source: 01_CANON/01_CORE_LAWS
tags:
  - core_law
  - fractal
  - knowledge_network
  - hml
  - hierarchical_resolution
  - traversal
  - retrieval
  - dependency
  - provenance
  - rscf
  - gmef
  - knowledge_graph
  - adaptive_resolution
  - selective_loading
  - context_efficiency
  - canon
  - canon/universe

rscf:
  state: SOURCE_CLAIM
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: core_laws
  node_id: fractal_knowledge_network
  node_type: core_law
---

# FRACTAL_KNOWLEDGE_NETWORK Specification

> [!abstract]
> Specifies scale-invariant knowledge graph traversal across
> **H / M / L resolutions**.
>
> The Fractal Knowledge Network provides a resolution-aware retrieval
> architecture in which reasoning begins from the smallest sufficient
> representation and descends into greater detail only when that detail
> can materially alter the result.

---

# 0. Status

```yaml
status:
  node_id: fractal_knowledge_network
  node_type: core_law
  state: SOURCE_CLAIM
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: core_laws

  canonical_statement:
    supplied: >
      Specifies scale-invariant knowledge graph traversal across
      H/M/L resolutions.

  governing_dimensions:
    - H
    - M
    - L

  architectural_functions:
    - fractal_traversal
    - resolution_selection
    - dependency_directed_retrieval
    - selective_detail_loading
    - provenance_preserving_navigation
````

The supplied node directly establishes:

```text
FRACTAL_KNOWLEDGE_NETWORK
=
scale-invariant knowledge graph traversal
across H / M / L resolutions
```

The detailed semantics below are an expanded AMOS architectural
reconstruction around that source spine.

Where exact mechanics are not supplied by authoritative source text,
they remain:

```text
DERIVED
MODEL
or
UNKNOWN/GAP
```

rather than invented canon.

---

# 1. Purpose

The Fractal Knowledge Network exists to prevent two symmetric
reasoning failures:

```text
UNDER-RETRIEVAL
```

where insufficient detail is loaded to support the conclusion,

and:

```text
OVER-RETRIEVAL
```

where large amounts of irrelevant detail are loaded even though they
cannot change the answer.

The governing objective is:

```text
retrieve the smallest sufficient knowledge structure
capable of supporting the decision
```

while preserving the ability to descend recursively when uncertainty,
contradiction, dependency, or stakes require greater resolution.

---

# 2. Core Law

For knowledge object \(K\), define three resolution projections:

$$
H(K),\quad M(K),\quad L(K)
$$

where the normalized interpretation is:

```text
H = high-level / domain resolution
M = middle / subsystem resolution
L = low-level / detail resolution
```

The source establishes the existence of H/M/L resolutions.

The exact formal semantics of each resolution are not defined in the
terse source and therefore the definitions above are normalized AMOS
model semantics.

---

# 3. Fractal Principle

A knowledge structure is fractal when the same navigation discipline
can recur at multiple scales.

Conceptually:

```text
H
|
+--> M1
|     |
|     +--> L1
|     +--> L2
|
+--> M2
      |
      +--> L3
      +--> L4
```

A node at one level may itself expose another H/M/L decomposition.

Therefore:

```text
H/M/L
```

is not necessarily one fixed three-layer global tree.

It may recur recursively.

---

# 4. Scale Invariance

The supplied phrase:

```text
scale-invariant knowledge graph traversal
```

means the traversal discipline is intended to remain structurally
usable across different resolutions.

Normalized principle:

$$
TraversalRule(H)
\approx
TraversalRule(M)
\approx
TraversalRule(L)
$$

with respect to navigation logic.

This does **not** imply that:

```text
H = M = L
```

or that each layer contains equal information.

Scale invariance concerns traversal structure, not semantic identity.

---

# 5. H — High Resolution Layer

Within this reconstruction, `H` represents the high-level orientation
surface.

Typical functions:

```text
domain identification
system orientation
major conceptual boundary
top-level dependencies
high-level applicability
primary governing law
```

H answers questions such as:

```text
What domain are we in?

What major knowledge structure governs this problem?

Which subsystem may contain the answer?

What are the major dependencies?
```

---

# 6. H Is Not the Final Answer by Default

H can sometimes be sufficient.

Example:

```text
Question:
Which law governs epistemic classification?

H:
EPISTEMIC_REGIMES
```

If that fully resolves the request:

```text
STOP
```

There is no integrity benefit from automatically loading every
subsystem and implementation detail.

Therefore:

```text
AVAILABLE DETAIL
!= REQUIRED DETAIL
```

---

# 7. M — Middle Resolution Layer

`M` represents subsystem or mechanism resolution.

Typical functions:

```text
subsystem selection
mechanism identification
dependency decomposition
competing branch identification
local governing structures
```

M answers:

```text
Which part of H matters?

Which mechanism changes the outcome?

Which branch contains the load-bearing dependency?
```

---

# 8. M as Selective Expansion

Conceptually:

```text
H: EPISTEMIC SYSTEM
        |
        +--> M1: classification
        +--> M2: provenance
        +--> M3: scope/regime
        +--> M4: gap handling
```

If the problem concerns provenance:

```text
expand M2
```

rather than automatically expanding:

```text
M1 + M2 + M3 + M4
```

Selective expansion is central to efficient fractal traversal.

---

# 9. L — Low Resolution Layer

`L` represents detailed resolution.

Typical contents may include:

```text
specific rule
equation
schema field
edge
premise
falsifier
exception
implementation constraint
raw evidence pointer
```

L answers:

```text
What exact detail resolves the remaining uncertainty?
```

---

# 10. L Is Not Raw Evidence

Critical boundary:

```text
L
!= RAW EVIDENCE
```

L is the detailed knowledge representation layer.

Raw evidence may sit beneath or behind L.

Conceptually:

```text
H
|
v
M
|
v
L
|
v
RAW EVIDENCE
```

Raw evidence should be loaded only when required.

---

# 11. Raw Evidence Boundary

Default:

```text
RAW EVIDENCE
=
DO_NOT_LOAD_UNLESS_REQUIRED
```

Reasons include:

```text
context cost
irrelevant detail
noise
provenance duplication
attention dilution
unnecessary computation
increased contradiction surface
```

This does not mean raw evidence is unimportant.

It means raw evidence is retrieved when it can materially alter
validation.

---

# 12. Bootstrap Capsule

A fractal traversal can begin from a compact bootstrap representation.

Conceptually:

```yaml
bootstrap_capsule:
  objective: "..."
  governing_domain: H
  candidate_subsystems:
    - M1
    - M2
  known_dependencies: []
  unresolved_uncertainty: []
  raw_evidence_required: false
```

The exact bootstrap schema is not supplied by the terse source.

It is an architectural model.

---

# 13. Canonical Retrieval Direction

Normalized traversal:

```text
BOOTSTRAP
   |
   v
   H
   |
   v
   M
   |
   v
   L
   |
   v
RAW EVIDENCE
```

but descent occurs only as needed.

Therefore the actual traversal may be:

```text
BOOTSTRAP -> H -> STOP
```

or:

```text
BOOTSTRAP -> H -> M -> STOP
```

or:

```text
BOOTSTRAP -> H -> M -> L -> STOP
```

or:

```text
BOOTSTRAP -> H -> M -> L -> RAW EVIDENCE
```

depending on decision sufficiency.

---

# 14. Smallest Sufficient Proof Scope

The Fractal Knowledge Network should seek:

$$
R^*
=
\arg\min_R Cost(R)
$$

subject to:

$$
Sufficiency(R)=TRUE
$$

where \(R\) is the retrieved knowledge region.

This is a normalized optimization model.

The source does not provide this equation.

The integrity constraint dominates the minimization:

```text
do not minimize retrieval
past the point of evidentiary sufficiency
```

---

# 15. Integrity Dominates Compression

The system must never interpret:

```text
smallest sufficient scope
```

as:

```text
smallest possible scope
```

Correct:

```text
MINIMIZE
subject to
INTEGRITY
```

Incorrect:

```text
MINIMIZE
even when required evidence disappears
```

Therefore:

$$
Integrity > RetrievalCompression
$$

---

# 16. Dependency-Directed Traversal

Traversal should follow dependencies capable of changing the answer.

Suppose:

```text
H
|
+--> M1
|     |
|     +--> L1
|
+--> M2
|     |
|     +--> L2
|
+--> M3
```

and only:

```text
M2 -> L2
```

can change the decision.

Then the preferred traversal is:

```text
H -> M2 -> L2
```

not exhaustive traversal of every branch.

---

# 17. Materiality Rule

A dependency is material when changing it could:

```text
flip the conclusion
change confidence materially
change scope
change regime
invalidate a premise
reveal contradiction
alter action
alter governance requirement
change safety or reversibility
```

If none apply, deeper traversal may have low decision value.

---

# 18. Branch Expansion Rule

Expand branch \(B\) when:

$$
EV_{information}(B) > Cost(B)
$$

conceptually.

This is not a source-defined numerical formula.

It represents the AMOS principle that retrieval effort should be spent
where uncertainty reduction has positive decision value.

---

# 19. Fractal Stop Rule

Stop descending when:

```text
CLAIM SUFFICIENCY
AND
DECISION SUFFICIENCY
AND
ACTION SUFFICIENCY
```

are achieved.

Do not continue retrieving merely because deeper nodes exist.

---

# 20. Claim Sufficiency

Claim sufficiency exists when the available knowledge is adequate to
state the conclusion at the correct epistemic class and confidence
ceiling.

It requires enough information to avoid:

```text
fabrication
scope leakage
regime leakage
unsupported causality
hidden contradiction
material provenance ambiguity
```

---

# 21. Decision Sufficiency

Decision sufficiency exists when unresolved uncertainty is unlikely to
change the decision.

This is stronger than:

```text
we have some relevant information
```

but weaker than:

```text
we know everything
```

---

# 22. Action Sufficiency

Action sufficiency exists when the evidence supports a safe next action
at the appropriate reversibility level.

A complete theory is not always necessary for a reversible action.

Conversely, an irreversible action may require deeper traversal.

---

# 23. Adaptive Depth

Traversal depth should scale with:

```text
stakes
irreversibility
novelty
weak evidence
staleness
contradiction
causal ambiguity
scope mismatch
regime mismatch
provenance correlation
governance impact
```

Higher risk can justify descent from:

```text
H -> M -> L -> evidence
```

even when H alone appears plausible.

---

# 24. C0–C4 Complexity Integration

Conceptual integration:

```text
C0 DIRECT
  -> H may suffice

C1 COMPACT
  -> H + selected M

C2 STRUCTURED
  -> H + M + selected L

C3 DEEP
  -> dependency closure across H/M/L

C4 MAXIMUM
  -> full material dependency/provenance challenge
     and raw evidence where required
```

The FKN determines **where to traverse**.

Adaptive complexity determines **how deeply to reason**.

---

# 25. Resolution Is Not Confidence

Critical firewall:

```text
H
!= LOW CONFIDENCE

M
!= MEDIUM CONFIDENCE

L
!= HIGH CONFIDENCE
```

H/M/L encode resolution.

They do not encode epistemic strength.

An H-level canonical fact may be stronger than an L-level speculative
detail.

---

# 26. Resolution Is Not Epistemic Class

Likewise:

```text
H/M/L
```

must not be conflated with:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
```

These dimensions are orthogonal.

Example:

```yaml
node:
  resolution: L
  epistemic_class: SOURCE_CLAIM
```

is valid.

So is:

```yaml
node:
  resolution: H
  epistemic_class: DERIVED
```

---

# 27. Resolution Is Not Scope

```text
H
```

does not automatically mean broad scope.

```text
L
```

does not automatically mean narrow applicability.

Resolution concerns detail.

Scope concerns where the claim applies.

---

# 28. Resolution Is Not Regime

```text
H/M/L
```

does not define whether knowledge is:

```text
canonical
empirical
simulation
speculative
```

A traversal must preserve regime independently.

---

# 29. Resolution Is Not Provenance

A high-level summary can preserve strong provenance.

A low-level detail can have weak provenance.

Therefore:

```text
DEPTH
!= PROVENANCE QUALITY
```

---

# 30. Resolution Is Not Truth

Deep retrieval can still retrieve false information.

Therefore:

```text
MORE DETAIL
!= MORE TRUTH
```

The purpose of fractal traversal is relevant resolution, not automatic
truth generation.

---

# 31. Recursive Structure

A subsystem can itself become an H-level object relative to its
children.

Example:

```text
GLOBAL H
  |
  v
GLOBAL M = PROVENANCE
             |
             v
        LOCAL H
        /     \
       v       v
 LOCAL M1   LOCAL M2
                |
                v
              LOCAL L
```

This is the primary meaning of fractal recursion in this architecture.

---

# 32. Relative Resolution

Therefore:

```text
H
M
L
```

are best understood as relative resolution roles.

A node may be:

```text
M relative to its parent
```

and simultaneously:

```text
H relative to its descendants
```

unless authoritative canon defines globally fixed levels.

---

# 33. Fractal Address

Illustrative addressing:

```text
H.epistemic
  /M.provenance
    /L.source_ancestry
```

or:

```text
H.recovery
  /M.multi_epoch
    /L.rewind_boundary
```

The exact path syntax is not source-defined.

---

# 34. Fractal Node

Illustrative node:

```yaml
fractal_node:
  node_id: provenance_independence

  resolution:
    role: M

  parent:
    node_id: epistemic_integrity

  children:
    - source_ancestry
    - correlation_risk
    - independence_test

  epistemic_class: MODEL

  dependencies: []

  raw_evidence:
    load_policy: DO_NOT_LOAD_UNLESS_REQUIRED
```

---

# 35. Parent Summary Contract

A parent should summarize children without erasing material
distinctions.

Conceptually:

$$
H = Compress(M_1,M_2,\ldots,M_n)
$$

subject to:

$$
Preserve(MaterialDifferences)=TRUE
$$

Compression that hides an outcome-changing contradiction is invalid.

---

# 36. Child Expansion Contract

A child expands information represented at the parent level.

Valid expansion:

```text
H:
State transition integrity
```

to:

```text
M:
Snapshot isolation
CAS
monotonic commit
```

to:

```text
L:
expected state mismatch -> abort
```

The child should add resolution rather than silently redefine the
parent.

---

# 37. Parent-Child Consistency

For parent \(P\) and child set \(C\):

```text
child detail
must not silently contradict
parent summary
```

If contradiction exists:

```text
CONFLICT
```

must be surfaced.

Do not automatically prefer the parent or child.

---

# 38. Lossy Compression Boundary

H-level compression is inherently capable of losing detail.

Loss is acceptable only when the omitted information cannot materially
alter the current use.

Therefore:

```text
LOSSY
can be acceptable

OUTCOME-CHANGING LOSS
is not acceptable
```

---

# 39. Expansion Trigger — Ambiguity

Descend when H is ambiguous.

Example:

```text
H:
"Use provenance-aware evidence."
```

Question:

```text
What counts as independent provenance?
```

requires M/L expansion.

---

# 40. Expansion Trigger — Contradiction

If two H summaries conflict:

```text
H1 -> X
H2 -> NOT X
```

descend into the load-bearing M/L nodes to determine:

```text
scope
regime
source ancestry
freshness
dependency
```

Do not resolve by summary preference.

---

# 41. Expansion Trigger — Weak Provenance

If an H conclusion rests on:

```text
SOURCE_CLAIM
```

and the decision requires stronger validation, descend toward:

```text
underlying source
observation
independent evidence
raw artifact
```

as required.

---

# 42. Expansion Trigger — Staleness

If the H capsule is stale:

```text
H@t0
```

and the answer depends on current state:

```text
t1
```

descend or refresh the affected branch.

Do not invalidate unrelated branches automatically.

---

# 43. Expansion Trigger — Scope Leakage

If H appears to generalize beyond its supporting scope:

```text
H:
universal conclusion
```

but M reveals:

```text
population = P1 only
```

then H must be narrowed or revalidated.

---

# 44. Expansion Trigger — Regime Crossing

If H combines:

```text
simulation result
```

with:

```text
empirical conclusion
```

descend into the regime boundary.

Cross-regime conclusions require an explicit bridge.

---

# 45. Expansion Trigger — Causal Claim

Causal conclusions generally justify deeper inspection of:

```text
mechanism
confounding
temporal ordering
intervention evidence
mediation
feedback
alternative explanations
```

Structural resemblance at H is insufficient.

---

# 46. Expansion Trigger — Irreversibility

If action is irreversible:

```text
expand proof scope
```

before commitment.

Examples include material:

```text
financial
legal
health
safety
institutional
governance
state mutation
```

effects.

---

# 47. Expansion Trigger — Governance

A local knowledge branch may appear sufficient for factual reasoning
while still requiring governance-level expansion before action.

Therefore:

```text
KNOWLEDGE SUFFICIENCY
!= AUTHORITY TO MUTATE
```

---

# 48. De-Escalation

Once outcome-changing uncertainty is resolved:

```text
STOP EXPANDING
```

Do not continue to deeper resolution solely because it is available.

This prevents exhaustive retrieval from becoming the default.

---

# 49. Horizontal Traversal

FKN is not limited to vertical descent.

Traversal may move horizontally:

```text
M1 <--> M2
```

when sibling subsystems interact.

Example:

```text
provenance
<-->
freshness
```

if stale provenance changes evidence validity.

---

# 50. Cross-Branch Traversal

Suppose:

```text
H
|
+--> M1
|     |
|     +--> L1
|
+--> M2
      |
      +--> L2
```

and:

```text
L1 depends on L2
```

then dependency traversal may cross branches.

Fractal hierarchy must not hide graph edges.

---

# 51. Tree vs Graph Boundary

The network is a knowledge **graph**.

Therefore it must not be reduced conceptually to a pure tree.

```text
hierarchy
+
cross-links
+
dependencies
+
provenance edges
=
knowledge graph
```

A node can have multiple meaningful relations.

---

# 52. Graph Relation Types

Possible relation classes include:

```text
PARENT_OF
CHILD_OF
DEPENDS_ON
SUPPORTS
CONTRADICTS
SUPERSEDES
DERIVED_FROM
OBSERVED_BY
MODEL_OF
INDEXED_BY
RELATED_TO
FALSIFIED_BY
```

Only relation types established by the governing schema should be
treated as canonical enumerations.

This list is an integration model.

---

# 53. Dependency Closure

Local reasoning is safe only when the load-bearing dependency closure
is known sufficiently.

Conceptually:

$$
Closure(C)
=
C
\cup Dependencies(C)
\cup Dependencies(Dependencies(C))
\ldots
$$

but traversal should stop at dependencies that cannot materially change
the conclusion.

---

# 54. Minimal Dependency Closure

Do not interpret dependency closure as:

```text
load the entire universe graph
```

Instead:

```text
load the transitive material dependency closure
```

This is a central FKN efficiency principle.

---

# 55. Hidden Dependency Hazard

Suppose:

```text
H -> M1 -> L1
```

appears independent.

But L1 secretly depends on:

```text
M2
```

which was not loaded.

Then the apparent local proof is incomplete.

Therefore:

```text
LOCAL REASONING
requires
DEPENDENCY CLOSURE
```

not merely local coherence.

---

# 56. Dependency Materiality

A dependency may be ignored only if changing it cannot materially alter:

```text
claim
confidence
scope
regime
action
governance
safety
```

This should be demonstrated where stakes justify it.

---

# 57. RSCF Integration

RSCF can serve as a compact knowledge capsule at any resolution.

Conceptually:

```text
H-RSCF
  |
  v
M-RSCF
  |
  v
L-RSCF
```

Each capsule can preserve:

```text
claim
class
premises
provenance
scope
regime
freshness
dependencies
competing explanations
falsifiers
confidence ceiling
```

---

# 58. RSCF as Fractal Node

Illustrative:

```yaml
rscf:
  node_id: K

  resolution: M

  claim:
    text: "..."

  epistemic_class: DERIVED

  premises:
    - P1

  dependencies:
    - L.detail_1

  provenance:
    - S1

  scope: S

  regime: R

  falsifiers:
    - F1
```

The exact schema remains governed by RSCF canon.

---

# 59. GMEF Integration

GMEF can represent a structured mapping of relevant environment,
mechanism, or governing context around an RSCF node where applicable.

Conceptually:

```text
RSCF = claim-centered capsule
GMEF = surrounding structured context
FKN  = traversal topology
```

This relationship is architectural unless a dedicated canonical GMEF
specification defines stronger semantics.

---

# 60. Proof Capsule Integration

A proof capsule can be retrieved at H first.

Example:

```yaml
proof_capsule:
  claim: C
  class: DERIVED
  load_bearing_premises:
    - P1
    - P2
  dependencies:
    - M1
  confidence_ceiling: CONDITIONAL
```

If the user only needs the conclusion and P1/P2 are valid:

```text
STOP
```

If P2 is uncertain:

```text
DESCEND P2
```

---

# 61. Proof-Guided Traversal

Traversal priority:

```text
LOAD-BEARING PREMISES
>
BACKGROUND CONTEXT
```

A premise that can flip the conclusion should be inspected before
noncritical explanatory material.

---

# 62. Weakest-Premise Traversal

If:

```text
P1 confidence = strong
P2 confidence = weak
P3 confidence = strong
```

and all are load-bearing:

```text
inspect P2 first
```

because P2 controls the confidence ceiling.

This is sensitivity-directed fractal retrieval.

---

# 63. Contradiction-Guided Traversal

When contradiction exists:

```text
C
vs
NOT C
```

retrieve the smallest nodes capable of discriminating between them.

Do not expand unrelated graph regions.

---

# 64. Competing-Hypothesis Traversal

Suppose:

```text
H1
H2
H3
```

remain viable.

Identify:

```text
lowest-cost discriminating evidence
```

and traverse toward that evidence.

Avoid collecting more evidence that all hypotheses predict equally.

---

# 65. Provenance-Guided Traversal

If three nodes support C:

```text
N1
N2
N3
```

before treating them as independent:

```text
trace ancestry
```

If:

```text
N1 <- S
N2 <- S
N3 <- S
```

then support is correlated.

The FKN must preserve provenance topology across resolution levels.

---

# 66. Provenance Compression

H may summarize:

```text
3 supporting sources
```

but if M/L reveal:

```text
all descend from one source
```

the H summary is misleading.

Therefore H-level provenance summaries should preserve material
correlation information.

---

# 67. Sybil Resistance

Fractal traversal must resist evidence inflation through duplicated
descendants.

```text
SOURCE S
 / | | \
v  v v  v
A  B C  D
```

does not automatically mean:

```text
4 independent sources
```

The graph must allow traversal upstream to common ancestry.

---

# 68. Freshness-Guided Traversal

If only one branch is stale:

```text
H
|
+--> M1 FRESH
+--> M2 STALE
+--> M3 FRESH
```

refresh:

```text
M2
```

and dependent descendants.

Do not recompute M1/M3 unless dependency edges require it.

---

# 69. Selective Invalidation

If node \(N\) fails:

```text
invalidate N
+
dependent descendants
```

not:

```text
invalidate entire FKN
```

unless N is globally load-bearing.

This enables local repair.

---

# 70. Local Repair

Conceptual process:

```text
FAILED NODE
    |
    v
identify affected edges
    |
    v
invalidate descendants
    |
    v
retrieve alternate path
    |
    v
revalidate local capsule
```

Global recomputation is last resort.

---

# 71. Failed-Path Rule

Do not repeat a failed traversal path unless something material changed.

Changed conditions may include:

```text
new evidence
new source
new regime
new version
new assumption
new dependency
new retrieval method
```

Otherwise repeated traversal is unlikely to add value.

---

# 72. Cycle Detection

Because FKN is a graph, cycles may exist as relations.

However, proof dependency cycles require special care.

Example:

```text
A depends on B
B depends on A
```

cannot independently establish either proposition.

Therefore:

```text
RECURSIVE STRUCTURE
!= CIRCULAR PROOF
```

---

# 73. Fractal Recursion vs Circular Reasoning

Valid fractal recursion:

```text
same traversal pattern
reused at another scale
```

Invalid circular reasoning:

```text
A is true because B
B is true because A
```

These must remain distinct.

---

# 74. Scale-Invariant Traversal Rule

Normalized generic traversal:

```text
1. inspect current node
2. identify decision-relevant uncertainty
3. identify children/dependencies capable of resolving it
4. traverse only those branches
5. validate returned evidence
6. update current capsule
7. stop if sufficient
8. otherwise recurse
```

The same pattern can operate at H, M, or L.

---

# 75. Traversal Pseudocode

```python
def traverse(node, objective):
    capsule = inspect(node)

    if sufficient(capsule, objective):
        return capsule

    uncertainty = decision_changing_uncertainty(capsule, objective)

    branches = material_dependencies(
        node=node,
        uncertainty=uncertainty,
    )

    for branch in prioritize(branches):
        result = traverse(branch, objective)
        capsule = integrate(capsule, result)

        if sufficient(capsule, objective):
            break

    return capsule
```

Illustrative only.

No literal executable implementation is established by the terse
source.

---

# 76. Raw Evidence Escalation

```python
def maybe_load_raw_evidence(node):
    if node.validation_is_sufficient:
        return DO_NOT_LOAD

    if raw_evidence_can_change_outcome(node):
        return LOAD

    return DO_NOT_LOAD
```

The governing principle:

```text
RAW EVIDENCE
IS ESCALATION,
NOT DEFAULT
```

---

# 77. Traversal Priority Function

Illustrative:

$$
Priority(B)
=
\frac{
DecisionImpact(B)
\times
UncertaintyReduction(B)
}{
RetrievalCost(B)
}
$$

subject to:

```text
integrity constraints
```

This equation is not source canon.

It formalizes the preference for cheap, high-information checks.

---

# 78. Sensitivity-First Traversal

Given assumptions:

```text
A1
A2
A3
```

identify:

```text
the smallest assumption capable of flipping the result
```

and inspect that branch first.

This can dramatically reduce unnecessary traversal.

---

# 79. Fractal Retrieval Under Uncertainty

Track uncertainty dimensions separately where material:

```text
evidence
model
scope
temporal
causal
execution
provenance independence
```

Then traverse the branch corresponding to the uncertainty that can
actually change the decision.

---

# 80. Evidence Uncertainty

If uncertainty is:

```text
Did source S really say X?
```

traverse:

```text
provenance/source branch
```

not unrelated model details.

---

# 81. Model Uncertainty

If uncertainty is:

```text
Which model best explains O?
```

traverse:

```text
competing models
predictions
discriminating observations
```

---

# 82. Scope Uncertainty

If uncertainty is:

```text
Does this result apply to population P2?
```

traverse:

```text
scope envelope
population
environment
measurement conditions
```

---

# 83. Temporal Uncertainty

If uncertainty is:

```text
Is this still current?
```

traverse:

```text
freshness
version
timestamp
supersession
```

---

# 84. Causal Uncertainty

If uncertainty is:

```text
Did A cause B?
```

traverse:

```text
mechanism
confounding
intervention
temporal ordering
alternative causes
```

rather than collecting more structural analogies.

---

# 85. Provenance-Independence Uncertainty

If uncertainty is:

```text
Are these confirmations independent?
```

traverse upward:

```text
source ancestry
dataset ancestry
model ancestry
pipeline ancestry
```

This is an example where optimal traversal may move **upstream**, not
deeper into content.

---

# 86. Bidirectional Traversal

FKN therefore supports conceptual movement:

```text
DOWN:
more detail

UP:
broader context / ancestry

SIDEWAYS:
related subsystem

BACK:
dependency source

FORWARD:
dependent consequence
```

Fractal traversal is graph navigation, not merely top-down expansion.

---

# 87. Query-Relative Traversal

The same network may produce different paths for different questions.

Question A:

```text
What is L23?
```

Path:

```text
H -> answer
```

Question B:

```text
Does L23 prove full serializability?
```

Path:

```text
H
-> M snapshot isolation
-> L explicit equations
-> boundary analysis
```

Question C:

```text
Does the deployed runtime literally implement CPU CAS?
```

Path may require:

```text
raw implementation evidence
```

if available.

---

# 88. Context Budget

FKN should treat reasoning context as finite.

Therefore:

```text
context should contain
the highest-value material
for the current objective
```

rather than every retrievable node.

This is a resource discipline, not permission to omit load-bearing
evidence.

---

# 89. Context Pollution

Overloading context with unrelated nodes can create:

```text
attention dilution
false associations
contradiction noise
stale premise leakage
provenance confusion
higher synthesis cost
```

Fractal selective retrieval mitigates this.

---

# 90. Compression Integrity

A compressed H capsule must preserve at minimum any feature capable of
changing downstream reasoning.

Potentially material fields include:

```text
claim class
scope
regime
freshness
critical dependencies
contradictions
confidence ceiling
falsifiers
provenance independence
```

when relevant.

---

# 91. H Capsule

Illustrative:

```yaml
H:
  domain: epistemic_integrity

  governing_claim:
    text: >
      Knowledge claims require typed epistemic classification.

  major_dependencies:
    - epistemic_regimes
    - provenance
    - scope_regime

  unresolved:
    - none

  descend_if:
    - classification_disputed
    - provenance_uncertain
    - scope_crossing
```

---

# 92. M Capsule

```yaml
M:
  subsystem: provenance

  governing_claim:
    text: >
      Independent confirmation requires provenance independence.

  dependencies:
    - source_identity
    - ancestry
    - correlation_risk

  unresolved:
    - ancestry_of_source_B

  descend_to:
    - L.source_B_ancestry
```

---

# 93. L Capsule

```yaml
L:
  detail: source_B_ancestry

  claim:
    text: >
      Source B descends from Source A.

  epistemic_class: OBSERVATION

  provenance:
    source: metadata_record

  implication:
    text: >
      A and B cannot automatically be counted as independent
      confirmations.

  raw_evidence_required: false
```

Illustrative only.

---

# 94. Raw Evidence Pointer

```yaml
raw_evidence:
  id: artifact_001

  load_policy:
    default: DO_NOT_LOAD_UNLESS_REQUIRED

  pointer:
    source: "..."

  required_when:
    - provenance_disputed
    - source_claim_requires_verification
    - exact_text_material
```

FKN should prefer pointers over unnecessary raw duplication.

---

# 95. Pointer Integrity

A pointer must remain resolvable enough to support later retrieval.

A summary without recoverable provenance creates:

```text
orphan knowledge
```

which weakens future validation.

Therefore:

```text
COMPRESSION
must preserve
RECOVERABILITY
```

---

# 96. Persistent Provenance

When knowledge is compressed from L to M or H:

```text
source ancestry
```

should remain recoverable.

Example:

```text
H summary
  |
  v
M capsule
  |
  v
L evidence node
  |
  v
source
```

A future validator should be able to descend back toward the source.

---

# 97. Evidence Topology Preservation

The FKN should preserve whether support is:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
```

and whether multiple supports are:

```text
independent
correlated
unknown
```

Compression must not flatten these distinctions.

---

# 98. Regime Preservation

Suppose L says:

```text
simulation observation
```

M must not summarize it as:

```text
observed system behavior
```

without preserving:

```text
regime = simulation
```

Likewise H must not erase the regime boundary.

---

# 99. Scope Preservation

Suppose:

```text
L:
population = P1
```

Then M/H must not silently generalize:

```text
all populations
```

unless a validated generalization exists.

---

# 100. Freshness Preservation

If a load-bearing L node expires:

```text
L -> STALE
```

its M/H summaries may also become stale if they depend on it.

Selective invalidation should follow dependency edges upward and
downstream as required.

---

# 101. Confidence Preservation

If H is derived from:

```text
M1 confidence = high
M2 confidence = conditional
```

and M2 is load-bearing:

```text
H confidence ceiling
<= M2
```

unless independently revalidated.

Compression must not inflate confidence.

---

# 102. Contradiction Preservation

If:

```text
L1 -> X
L2 -> NOT X
```

M must not summarize:

```text
X
```

without preserving the contradiction.

Correct:

```text
COMPETING
```

or a scoped resolution if evidence distinguishes them.

---

# 103. Competing Hypothesis Preservation

Suppose:

```text
M1 model A
M2 model B
```

both explain the available observations.

H should preserve:

```text
COMPETING
```

rather than manufacturing one unified answer.

---

# 104. Falsifier Preservation

If L contains a critical falsifier:

```text
F
```

that could invalidate H, then H should retain at least a pointer to F.

A summary that hides its own invalidation condition is epistemically
fragile.

---

# 105. H/M/L Update Propagation

When L changes:

```text
L_old -> L_new
```

recompute only affected ancestors and dependents.

Conceptually:

```text
L2 changed
 |
 v
M1 affected
 |
 v
H1 affected
```

Unrelated:

```text
M2
M3
H2
```

remain valid if dependency closure proves independence.

---

# 106. Incremental Revalidation

Preferred:

```text
local change
-> local dependency analysis
-> local invalidation
-> local revalidation
```

rather than:

```text
local change
-> rebuild entire knowledge universe
```

unless global dependency exists.

---

# 107. Cache Boundary

A previously generated H/M/L capsule may be reused only while:

```text
dependencies valid
scope compatible
regime compatible
freshness valid
provenance unchanged materially
no unresolved conflict invalidates it
```

Otherwise:

```text
REVALIDATE
```

---

# 108. Cached Summary Hazard

A cached H summary can become stale while underlying L nodes change.

Therefore:

```text
CACHE HIT
!= VALID KNOWLEDGE
```

Cache reuse requires validity checks.

---

# 109. Version Binding

Conceptually:

```yaml
capsule:
  node_id: K
  version: v17

  dependencies:
    - node: P1
      version: v4
    - node: P2
      version: v9
```

If P2 changes:

```text
validate K
```

before reuse.

Exact version mechanics are not supplied by this source.

---

# 110. Epoch Binding

Where causal epochs are used, a knowledge capsule may also carry an
epoch binding.

Conceptually:

```yaml
capsule:
  epoch: e_k
```

Crossing to:

```text
e_{k+1}
```

does not automatically invalidate every capsule.

Only validity conditions and dependencies determine whether
revalidation is needed.

---

# 111. MVCC/CAS Integration Boundary

FKN knowledge capsules can conceptually participate in snapshot-based
reasoning.

Example:

```text
reason against
knowledge snapshot S_k
```

and commit a state change only if expected state remains valid.

However:

```text
FKN
!= MVCC
```

and:

```text
FKN
!= CAS
```

FKN defines knowledge traversal.

Concurrency control belongs to its own governing law.

---

# 112. Replayability Integration

A traversal can be made replayable if the relevant:

```text
root inputs
retrieval decisions
versions
dependencies
receipts
```

are sufficiently captured.

But:

```text
FKN
!= DETERMINISTIC REPLAYABILITY LAW
```

and this terse source does not define bit-for-bit replay mechanics.

Those belong to [[L22_REPLAYABILITY]] where applicable.

---

# 113. Causal Epoch Integration

FKN can traverse causal lineage:

```text
cause
-> consequence
-> epoch transition
```

but:

```text
graph edge
!= causal proof
```

Only appropriately typed causal evidence licenses causal conclusions.

---

# 114. Recovery Integration

When a knowledge node becomes invalid:

```text
identify failed node
trace dependents
invalidate affected capsules
retrieve alternate evidence
repair locally
```

This supports selective recovery.

It does not itself define the complete recovery protocol.

---

# 115. DMER Integration Boundary

A D/M/E/R recovery architecture may use FKN to locate:

```text
affected distinctions
mutations
entropy propagation
repair dependencies
```

across resolution levels.

However:

```text
FKN traversal
!= DMER recovery semantics
```

The relationship is complementary.

---

# 116. Local Reasoning Fast Path

Local reasoning can remain local when all of the following are
sufficiently established:

```text
dependency closure
provenance independence where material
scope compatibility
regime compatibility
freshness
non-conflict
```

If these hold:

```text
do not expand globally
```

This is the FKN fast path.

---

# 117. Escalation Conditions

Escalate traversal when:

```text
shared provenance ancestry
contradiction
stale evidence
cross-regime inference
causal coupling
governance impact
irreversible stakes
ambiguous dependency
scope mismatch
weak load-bearing premise
```

Escalation may mean deeper, broader, upstream, or cross-branch
navigation.

---

# 118. Fast Path Is Not Shortcutting Integrity

Incorrect:

```text
FAST PATH
=
skip validation
```

Correct:

```text
FAST PATH
=
validation establishes
that broader traversal cannot materially alter the answer
```

Efficiency follows proof of locality.

It is not assumed.

---

# 119. Independence Requirement

Suppose:

```text
branch A
branch B
```

appear unrelated.

Do not assume independence because they are stored separately.

Check whether they share:

```text
source
dataset
model
assumption
runtime
author
pipeline
causal dependency
```

if independence matters.

---

# 120. Cross-Domain Traversal

A structural pattern found in domain A may suggest a model for domain B.

Correct:

```text
MODEL TRANSFER
```

until independently validated.

Incorrect:

```text
same structure
therefore same causal law
```

FKN can traverse cross-domain analogies without converting analogy into
fact.

---

# 121. Cross-Scale Mapping

Likewise:

```text
micro-scale pattern
```

may resemble:

```text
macro-scale pattern
```

but scale-invariant **traversal** does not imply scale-invariant
**causation**.

Critical firewall:

```text
SCALE-INVARIANT NAVIGATION
!=
SCALE-INVARIANT PHYSICAL LAW
```

---

# 122. Fractal Architecture vs Universal Fractality

The name:

```text
FRACTAL_KNOWLEDGE_NETWORK
```

establishes an AMOS knowledge architecture.

It does **not** establish that:

```text
reality itself is universally fractal
```

or:

```text
all knowledge domains possess literal mathematical fractal geometry
```

unless separately supported.

---

# 123. Mathematical Fractal Boundary

The word `fractal` here should not automatically be interpreted as a
claim of:

```text
non-integer Hausdorff dimension
self-similar geometric object
Mandelbrot-style mathematical fractal
```

The supplied source establishes:

```text
scale-invariant knowledge graph traversal
```

not a formal fractal-dimension theorem.

---

# 124. H/M/L Completeness Boundary

The source establishes traversal across H/M/L resolutions.

It does not prove:

```text
all possible knowledge
can be losslessly represented
in exactly three levels
```

Recursive H/M/L decomposition can provide additional resolution, but
formal universal completeness is not established.

---

# 125. Fixed-Level Boundary

The terse source does not establish whether:

```text
H/M/L are globally fixed layers
```

or:

```text
relative recursive roles
```

The relative recursive interpretation used here is an AMOS-consistent
MODEL elaboration based on the term `fractal`.

This distinction remains falsifiable by authoritative canon.

---

# 126. Granularity Boundary

No exact threshold is supplied for deciding:

```text
H vs M
M vs L
```

Therefore classification of a particular node's resolution may require
domain-specific convention.

Do not invent universal numeric thresholds.

---

# 127. Traversal Cost Boundary

The source does not define:

```text
token budgets
latency targets
node limits
maximum depth
maximum breadth
```

Any such limits are implementation parameters, not established canon.

---

# 128. Retrieval Engine Boundary

The specification does not establish a particular:

```text
vector database
graph database
search engine
embedding model
filesystem
index
SQL store
distributed database
```

as the literal FKN implementation.

FKN is an architectural reasoning/retrieval specification unless
implementation evidence establishes otherwise.

---

# 129. Runtime Boundary

The existence of this canonical architecture does not prove that the
underlying ChatGPT runtime literally implements:

```text
FKN nodes
H/M/L database shards
RSCF storage
graph transactions
distributed CAS
```

These remain reasoning architecture concepts unless independently
verified.

---

# 130. Hidden Chain-of-Thought Boundary

Fractal knowledge retrieval does not require disclosure of private
chain-of-thought.

A sufficient trace can expose:

```text
claim
premises
sources
dependencies
scope
regime
falsifiers
classification
```

without exposing hidden reasoning tokens.

---

# 131. Failure Mode — Flat Retrieval

```text
FM-FKN-001
```

Condition:

```text
retrieve all knowledge at one undifferentiated resolution
```

Effect:

```text
poor context efficiency
loss of hierarchy
higher noise
```

Repair:

```text
restore H/M/L decomposition
```

---

# 132. Failure Mode — Premature Descent

```text
FM-FKN-002
```

Condition:

```text
load L/raw evidence
before identifying the decision-relevant branch
```

Effect:

```text
context pollution
wasted retrieval
attention dilution
```

Repair:

```text
return to H/M orientation
```

---

# 133. Failure Mode — Insufficient Descent

```text
FM-FKN-003
```

Condition:

```text
stop at H
despite unresolved load-bearing uncertainty
```

Effect:

```text
unsupported conclusion
```

Repair:

```text
descend into material dependency
```

---

# 134. Failure Mode — Exhaustive Traversal

```text
FM-FKN-004
```

Condition:

```text
visit every node
regardless of materiality
```

Effect:

```text
high cost
noise
slower synthesis
greater contradiction surface
```

Repair:

```text
dependency-directed traversal
```

---

# 135. Failure Mode — Hidden Dependency

```text
FM-FKN-005
```

Condition:

```text
local branch treated as independent
while relying on unloaded external premise
```

Effect:

```text
false proof closure
```

Repair:

```text
dependency closure analysis
```

---

# 136. Failure Mode — Provenance Collapse

```text
FM-FKN-006
```

Condition:

```text
H summary removes source ancestry
```

Effect:

```text
correlated evidence appears independent
```

Repair:

```text
restore provenance pointers/topology
```

---

# 137. Failure Mode — Scope Collapse

```text
FM-FKN-007
```

Condition:

```text
L-level scoped evidence
compressed into universal H claim
```

Repair:

```text
restore applicability envelope
```

---

# 138. Failure Mode — Regime Collapse

```text
FM-FKN-008
```

Condition:

```text
simulation/canonical/model evidence
compressed into empirical claim
```

Repair:

```text
restore regime label and bridge requirement
```

---

# 139. Failure Mode — Confidence Inflation

```text
FM-FKN-009
```

Condition:

```text
H confidence exceeds weakest
load-bearing child
```

Repair:

```text
restore dependency-aware confidence ceiling
```

---

# 140. Failure Mode — Fractal Reification

```text
FM-FKN-010
```

Condition:

```text
knowledge traversal architecture
used as proof that reality itself is fractal
```

Repair:

```text
restore MODEL boundary
```

---

# 141. Failure Mode — Recursive Loop

```text
FM-FKN-011
```

Condition:

```text
A -> B -> C -> A
```

used as evidentiary support.

Repair:

```text
detect circular dependency
require external grounding
```

---

# 142. Failure Mode — Stale Parent

```text
FM-FKN-012
```

Condition:

```text
L changes
but H cached summary remains unchanged
```

Repair:

```text
dependency-driven invalidation
```

---

# 143. Failure Mode — Raw Evidence Default

```text
FM-FKN-013
```

Condition:

```text
all raw artifacts loaded for every query
```

Repair:

```text
restore DO_NOT_LOAD_UNLESS_REQUIRED policy
```

---

# 144. Failure Mode — False Independence

```text
FM-FKN-014
```

Condition:

```text
separate branches assumed independent
because graph paths differ
```

Repair:

```text
trace provenance and causal ancestry
```

---

# 145. Failure Mode — Search Popularity Substitution

```text
FM-FKN-015
```

Condition:

```text
most frequently retrieved node
treated as most correct node
```

Repair:

```text
evaluate evidence class,
scope,
provenance,
freshness,
and dependency
```

---

# 146. Anti-Pattern Register

```yaml
anti_patterns:

  - id: FKN-AP01
    name: LOAD_EVERYTHING

  - id: FKN-AP02
    name: STOP_AT_SUMMARY_DESPITE_CRITICAL_GAP

  - id: FKN-AP03
    name: RAW_EVIDENCE_BY_DEFAULT

  - id: FKN-AP04
    name: HML_AS_CONFIDENCE_LEVELS

  - id: FKN-AP05
    name: HML_AS_EPISTEMIC_CLASSES

  - id: FKN-AP06
    name: TREE_ONLY_ASSUMPTION

  - id: FKN-AP07
    name: HIDDEN_CROSS_BRANCH_DEPENDENCY

  - id: FKN-AP08
    name: SUMMARY_ERASES_PROVENANCE

  - id: FKN-AP09
    name: SUMMARY_ERASES_SCOPE

  - id: FKN-AP10
    name: SUMMARY_ERASES_REGIME

  - id: FKN-AP11
    name: SUMMARY_ERASES_CONTRADICTION

  - id: FKN-AP12
    name: SUMMARY_INFLATES_CONFIDENCE

  - id: FKN-AP13
    name: REPEAT_FAILED_PATH_WITHOUT_NEW_EVIDENCE

  - id: FKN-AP14
    name: RECURSION_AS_CIRCULAR_PROOF

  - id: FKN-AP15
    name: FRACTAL_ARCHITECTURE_AS_UNIVERSAL_CAUSAL_LAW
```

---

# 147. Traversal Decision Matrix

| Condition                                | Preferred Traversal              |
| ---------------------------------------- | -------------------------------- |
| H fully resolves low-stakes question     | Stop at H                        |
| H identifies subsystem but not answer    | H → M                            |
| M leaves exact rule unresolved           | H → M → L                        |
| Source claim requires direct validation  | descend to raw/source evidence   |
| Contradiction exists                     | traverse discriminating branches |
| Evidence may share ancestry              | traverse upstream provenance     |
| Scope uncertain                          | traverse scope branch            |
| Regime uncertain                         | traverse regime branch           |
| Freshness uncertain                      | traverse version/time branch     |
| Causal claim consequential               | expand mechanism/confounders     |
| Irreversible action                      | expand proof scope               |
| Branch proven independent and irrelevant | do not load                      |
| Cached capsule dependencies unchanged    | reuse                            |
| Load-bearing dependency changed          | selectively invalidate/recompute |

---

# 148. Traversal State Machine

```text
START
  |
  v
BOOTSTRAP
  |
  v
LOAD H
  |
  v
SUFFICIENT?
 /       \
YES       NO
 |         |
STOP       v
         SELECT M
           |
           v
       SUFFICIENT?
        /      \
      YES       NO
       |         |
      STOP       v
              SELECT L
                 |
                 v
             SUFFICIENT?
              /      \
            YES       NO
             |         |
            STOP       v
                 RAW EVIDENCE?
                    /   \
                  NO     YES
                  |       |
                 GAP     LOAD
                           |
                           v
                       VALIDATE
                           |
                           v
                         STOP
```

---

# 149. Contradiction State Machine

```text
CLAIM C
   |
   +--> support path A
   |
   +--> contradiction path B
             |
             v
        COMPETING
             |
             v
identify discriminating dependency
             |
             v
traverse smallest sufficient branch
             |
       +-----+-----+
       |           |
       v           v
   RESOLVED     UNRESOLVED
       |           |
       v           v
   CONDITION     COMPETING
```

---

# 150. Local Repair State Machine

```text
VALID CAPSULE
     |
     v
DEPENDENCY CHANGES
     |
     v
CAPSULE INVALIDATED
     |
     v
IDENTIFY AFFECTED SUBGRAPH
     |
     v
RETRIEVE NEW MATERIAL
     |
     v
REVALIDATE
   /      \
PASS      FAIL
 |          |
 v          v
REUSE      ESCALATE
```

---

# 151. FKN Query Contract

Illustrative:

```yaml
fkn_query:
  objective: "..."

  starting_resolution:
    preferred: H

  constraints:
    scope: null
    regime: null
    freshness: null

  stakes:
    level: null
    irreversible: false

  traversal:
    raw_evidence_default: DO_NOT_LOAD_UNLESS_REQUIRED

  stop_conditions:
    - claim_sufficiency
    - decision_sufficiency
    - action_sufficiency
```

---

# 152. FKN Traversal Receipt

Illustrative:

```yaml
fkn_receipt:

  query_id: FKN-Q001

  objective:
    text: "..."

  start:
    node: H.root

  visited:
    - H.root
    - M.provenance
    - L.source_ancestry

  skipped:
    - M.performance
    - M.execution

  skip_reason:
    - not_material_to_decision

  raw_evidence:
    loaded: false

  stop_reason:
    claim_sufficiency: true
    decision_sufficiency: true
    action_sufficiency: true

  unresolved_gaps: []
```

The exact receipt schema is not source-established.

---

# 153. Minimal Node Schema

```yaml
fkn_node:

  node_id: K

  resolution:
    role: H

  summary:
    text: "..."

  children: []

  dependencies: []

  provenance: []

  epistemic_class: null

  scope: null

  regime: null

  freshness: null
```

Illustrative.

---

# 154. Full Node Schema

```yaml
fkn_node:

  identity:
    node_id: K
    node_type: knowledge_node
    version: null

  resolution:
    role: H
    parent_resolution: null
    recursive: true

  content:
    claim: "..."
    summary: "..."

  epistemic:
    class: null
    confidence_ceiling: null

  provenance:
    direct_sources: []
    ancestry: []
    independence_status: UNKNOWN

  graph:
    parents: []
    children: []
    dependencies: []
    dependents: []
    supports: []
    contradicts: []
    supersedes: []

  applicability:
    scope: null
    regime: null

  freshness:
    status: null

  proof:
    premises: []
    falsifiers: []
    competing: []

  retrieval:
    raw_evidence_policy: DO_NOT_LOAD_UNLESS_REQUIRED
    raw_evidence_pointers: []

  validation:
    status: null
    last_validated: null
```

Model-level schema only.

---

# 155. Fractal Index

A compact index can map H nodes:

```yaml
H_INDEX:

  epistemic:
    children:
      - classification
      - provenance
      - scope_regime
      - gaps

  reasoning:
    children:
      - RSCF
      - GMEF
      - atomic_reasoning
      - proof_capsules

  execution:
    children:
      - transactions
      - concurrency
      - epochs

  recovery:
    children:
      - rollback
      - repair
      - multi_epoch
```

This is illustrative and does not replace authoritative AMOS maps.

---

# 156. Navigation by Objective

Instead of retrieving by keyword alone:

```text
query text
```

FKN should orient around:

```text
objective
decision
uncertainty
dependency
```

Two semantically similar queries may require different graph paths
because their decision stakes differ.

---

# 157. Search vs Traversal

Search asks:

```text
Which nodes appear relevant?
```

Traversal asks:

```text
Which dependencies must be followed
to establish the answer?
```

Therefore:

```text
SEARCH
!= PROOF
```

Search can locate candidate nodes.

Dependency-aware traversal establishes support.

---

# 158. Retrieval vs Validation

Likewise:

```text
RETRIEVED
!= VALIDATED
```

A retrieved node may be:

```text
stale
contradicted
out of scope
wrong regime
correlated
source-only
```

Validation remains necessary where material.

---

# 159. Retrieval vs Authority

A node's presence in the network does not itself grant authority.

```text
INDEXED
!= CANONICAL

CANONICAL
!= EMPIRICALLY VERIFIED

RETRIEVED
!= TRUE
```

Each property must remain typed.

---

# 160. Traversal and Canon Priority

When multiple nodes conflict, canonical authority may matter within
canon-governed questions.

But authority should still be explicit.

Example:

```text
older MODEL node
vs
newer CANON_LAW
```

may be resolved by supersession if authoritative lineage establishes
it.

Do not infer supersession from recency alone.

---

# 161. Temporal Lineage

Knowledge evolution should preserve:

```text
v1
 |
 v
v2
 |
 v
v3
```

with explicit:

```text
supersedes
extends
contradicts
deprecated_by
```

relationships where known.

The latest node should not silently erase historical lineage.

---

# 162. Version Search

If a current node appears incomplete:

```text
inspect lineage
```

when historical versions could materially recover:

```text
missing definitions
supersession records
changed equations
removed boundaries
```

Do not load all historical versions by default.

---

# 163. Historical Evidence Boundary

Older canon can explain:

```text
how a concept evolved
```

but it should not automatically override newer authoritative canon.

Correct:

```text
historical context
```

not:

```text
silent rollback of canon
```

---

# 164. Knowledge Harvest Integration

FKN can support:

```text
Ephemeral Code
      |
      v
Persistent Evidence
      |
      v
Validated Knowledge
```

by placing each artifact at the appropriate resolution and preserving
provenance.

However, harvesting does not automatically validate source claims.

---

# 165. Source Claim Harvest

Documentation statement:

```text
"system passes 21 tests"
```

enters as:

```text
SOURCE_CLAIM
```

not observation.

If test artifacts are executed:

```text
OBSERVATION
```

can be added as a separate node.

The FKN preserves both.

---

# 166. Observation Harvest

Directly inspected evidence can enter an L node:

```yaml
resolution: L
epistemic_class: OBSERVATION
```

and later support M/H summaries.

The summary must preserve the observation's scope.

---

# 167. Derived Knowledge Harvest

A stable inference can be stored as:

```text
DERIVED
```

with:

```text
premises
dependency edges
scope
regime
falsifiers
confidence ceiling
```

so future traversal can reuse it without rebuilding everything.

---

# 168. Model Harvest

Architectural mappings can be stored as:

```text
MODEL
```

without being silently promoted to empirical truth.

This is especially important for cross-domain and cross-scale
structures.

---

# 169. Reuse Rule

Reuse a stored capsule only while:

```text
dependencies valid
scope valid
regime valid
freshness valid
provenance assumptions valid
no defeating contradiction
```

Otherwise descend and revalidate.

---

# 170. Revalidation Trigger

Trigger revalidation when:

```text
dependency version changes
source changes
scope changes
regime changes
environment changes
model changes
contradiction appears
falsifier fires
freshness expires
```

---

# 171. FKN and Causal Firewall

A graph naturally contains edges.

But:

```text
EDGE
!= CAUSE
```

A relation such as:

```text
RELATED_TO
```

must never be interpreted as:

```text
CAUSES
```

unless causal evidence licenses it.

---

# 172. FKN and Scope Firewall

A child can be narrower than its parent.

A sibling can operate under a different environment.

Therefore graph adjacency does not license scope transfer.

```text
CONNECTED
!= SAME SCOPE
```

---

# 173. FKN and Regime Firewall

Likewise:

```text
CONNECTED
!= SAME REGIME
```

A simulation node and empirical node may be adjacent while remaining
epistemically separated.

---

# 174. FKN and Provenance Firewall

```text
CONNECTED
!= INDEPENDENT
```

and:

```text
SEPARATE NODE
!= SEPARATE SOURCE
```

Provenance ancestry must remain explicit.

---

# 175. FKN and Freshness Firewall

```text
PARENT FRESH
```

does not automatically prove:

```text
ALL CHILDREN FRESH
```

and vice versa.

Freshness propagation depends on actual dependencies.

---

# 176. FKN and Causal Epochs

An epoch transition may alter the validity of selected nodes.

Conceptually:

```text
e_k
 |
 +--> H1
 +--> M1
 +--> L1

e_{k+1}
 |
 +--> L1 superseded
```

Only dependent summaries need revalidation unless broader coupling
exists.

---

# 177. FKN and No Time Travel

When a node is superseded:

```text
old node remains historical
```

and:

```text
new node becomes current
```

Do not silently rewrite the historical graph.

This preserves causal lineage.

---

# 178. FKN and Multi-Epoch Recovery

During recovery, FKN can identify:

```text
fault origin
affected dependency subgraph
cross-epoch descendants
repair candidates
```

This can support coordinated recovery.

The exact rollback algorithm remains governed elsewhere.

---

# 179. Fractal Recovery

A recovery problem itself can be traversed fractally:

```text
H:
Which subsystem failed?

M:
Which dependency path propagated corruption?

L:
Which exact mutation introduced the fault?

RAW:
What artifact proves it?
```

The same traversal discipline therefore applies to diagnosis.

---

# 180. Fractal Governance

Governance can also use H/M/L:

```text
H:
Is this action governed?

M:
Which authority/constraint applies?

L:
What exact permission or prohibition controls it?
```

This demonstrates scale-invariant traversal without claiming identical
content across scales.

---

# 181. Fractal Epistemics

```text
H:
What is the conclusion class?

M:
What evidence topology supports it?

L:
What exact source/observation/premise supports the topology?
```

Again:

```text
same traversal grammar
different semantic content
```

---

# 182. Fractal Causality

```text
H:
Is causal inference required?

M:
Which causal relation is claimed?

L:
What mechanism/confounder/intervention evidence licenses it?
```

This protects against causal overreach.

---

# 183. Fractal Scope Analysis

```text
H:
What is the applicability envelope?

M:
Which dimension may limit it?

L:
What exact population/environment/time constraint applies?
```

---

# 184. Fractal Provenance Analysis

```text
H:
Is support independently corroborated?

M:
Which sources support it?

L:
What ancestry does each source have?

RAW:
What original artifact anchors the lineage?
```

---

# 185. Fractal Contradiction Analysis

```text
H:
Contradiction exists.

M:
Which claims conflict?

L:
Which premises create the conflict?

RAW:
Which evidence can discriminate?
```

---

# 186. Fractal Sensitivity Analysis

```text
H:
Conclusion C

M:
Load-bearing premises P1/P2/P3

L:
Threshold or assumption capable of flipping C
```

This supports efficient decision-focused validation.

---

# 187. Fractal Action Analysis

```text
H:
What action class is appropriate?

M:
What uncertainty controls action choice?

L:
What evidence would permit escalation?
```

This supports reversible action under uncertainty.

---

# 188. Promotion Gate for Knowledge Capsules

Before promoting a detailed node into a reusable higher-resolution
capsule, check:

```text
provenance preserved
scope preserved
regime preserved
dependencies preserved
contradictions visible
falsifiers retained
confidence ceiling valid
freshness known
```

If material information is lost:

```text
DO NOT PROMOTE
```

---

# 189. Compression Gate

Conceptually:

```python
def safe_to_compress(node):
    return all([
        provenance_preserved(node),
        scope_preserved(node),
        regime_preserved(node),
        critical_dependencies_preserved(node),
        contradictions_preserved(node),
        confidence_not_inflated(node),
        falsifiers_recoverable(node),
    ])
```

Illustrative only.

---

# 190. Expansion Gate

```python
def should_expand(node, decision):
    return any([
        unresolved_load_bearing_uncertainty(node),
        contradiction_can_change_decision(node),
        provenance_is_ambiguous(node),
        evidence_is_stale(node),
        scope_is_uncertain(node),
        regime_is_uncertain(node),
        causal_claim_needs_support(node),
        stakes_require_more_validation(decision),
    ])
```

Illustrative only.

---

# 191. Raw-Evidence Gate

```python
def should_load_raw(node):
    return (
        current_representation_is_insufficient(node)
        and raw_evidence_can_materially_change_validation(node)
    )
```

This prevents both evidence starvation and evidence flooding.

---

# 192. Traversal Invariants

```text
FKN-I1
START AT THE SMALLEST SUFFICIENT RESOLUTION.

FKN-I2
DESCEND ONLY WHEN MATERIAL UNCERTAINTY REQUIRES IT.

FKN-I3
RAW EVIDENCE IS NOT THE DEFAULT LOAD TARGET.

FKN-I4
H/M/L REPRESENT RESOLUTION, NOT CONFIDENCE.

FKN-I5
H/M/L REPRESENT RESOLUTION, NOT EPISTEMIC CLASS.

FKN-I6
GRAPH CONNECTION DOES NOT ESTABLISH CAUSATION.

FKN-I7
SEPARATE NODES DO NOT ESTABLISH PROVENANCE INDEPENDENCE.

FKN-I8
COMPRESSION MUST PRESERVE MATERIAL CONTRADICTIONS.

FKN-I9
COMPRESSION MUST PRESERVE MATERIAL SCOPE AND REGIME.

FKN-I10
COMPRESSION MUST NOT INFLATE CONFIDENCE.

FKN-I11
DEPENDENCY CLOSURE MUST BE SUFFICIENT FOR LOCAL REASONING.

FKN-I12
FAILED NODES INVALIDATE ONLY AFFECTED DEPENDENTS WHERE COMPUTABLE.

FKN-I13
RECURSION MUST NOT BECOME CIRCULAR PROOF.

FKN-I14
SCALE-INVARIANT TRAVERSAL DOES NOT PROVE SCALE-INVARIANT REALITY.

FKN-I15
STOP WHEN CLAIM, DECISION, AND ACTION SUFFICIENCY ARE ACHIEVED.
```

---

# 193. Source-Established Claims

The supplied node directly establishes:

```yaml
source_established:

  title:
    value: FRACTAL_KNOWLEDGE_NETWORK Specification

  type:
    value: core_law

  source:
    value: 01_CANON/01_CORE_LAWS

  tags:
    - core_law
    - fractal
    - knowledge_network

  governing_statement:
    value: >
      Specifies scale-invariant knowledge graph traversal across
      H/M/L resolutions.

  node:
    node_id: fractal_knowledge_network
    node_type: core_law

  path:
    value: >
      01_CANON/01_CORE_LAWS/FRACTAL_KNOWLEDGE_NETWORK.md

  relations:
    indexed_by:
      - 00_HOME
      - AMOS_RSCF_NODES

    child_of:
      - LAW_HIERARCHY

  related:
    - 00_HOME
    - AMOS_RSCF_NODES
    - LAW_HIERARCHY

  moc:
    - 01_CORE_LAWS_MOC

  trang_framework:
    - TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS
```

---

# 194. Corpus Corroboration Boundary

A Drive corpus search shows `FRACTAL_KNOWLEDGE_NETWORK` also appears in
AMOS reasoning/infrastructure materials alongside structures such as:

```text
RSCF
GMEF
HML
PROOF_CAPSULE
COMPETING_HYPOTHESES
UNCERTAINTY_VECTOR
```

This supports its placement in the broader AMOS reasoning architecture.

However:

```text
CORPUS CO-OCCURRENCE
!=
FULL SEMANTIC DEFINITION
```

and:

```text
INDEX PRESENCE
!=
INDEPENDENT EMPIRICAL VALIDATION
```

The terse source node remains the direct basis for the canonical
statement.

---

# 195. Not Established by This Node

The supplied terse source does **not** independently establish:

```yaml
not_established:

  - exact formal definitions of H, M, and L

  - whether H/M/L are globally fixed layers or recursive relative roles

  - exact number of children allowed per node

  - exact graph database implementation

  - exact traversal algorithm

  - exact ranking function

  - exact retrieval-cost function

  - exact token budget

  - exact maximum traversal depth

  - exact maximum traversal breadth

  - exact raw-evidence schema

  - exact RSCF/FKN serialization contract

  - exact GMEF/FKN coupling

  - exact proof-capsule/FKN coupling

  - exact cache implementation

  - exact invalidation algorithm

  - exact distributed consistency mechanism

  - exact concurrency protocol

  - exact persistence layer

  - exact hashing or signing mechanism

  - exact replay receipt format

  - literal implementation inside ChatGPT

  - universal mathematical fractality of knowledge

  - universal fractality of reality

  - universal causal invariance across scales

  - formal proof that H/M/L is an exhaustive ontology of knowledge
```

These remain implementation/model questions unless separately
established.

---

# 196. Gap Register

```yaml
gaps:

  - id: FKN-G001
    class: CRITICAL
    issue: >
      Authoritative exact definitions of H, M, and L are not contained
      in the supplied terse node.
    status: OPEN

  - id: FKN-G002
    class: DECISION_RELEVANT
    issue: >
      Whether H/M/L are globally fixed levels or recursively relative
      resolution roles is not explicitly established here.
    status: OPEN

  - id: FKN-G003
    class: DECISION_RELEVANT
    issue: >
      Exact materiality test governing branch expansion is not supplied.
    status: OPEN

  - id: FKN-G004
    class: DECISION_RELEVANT
    issue: >
      Exact dependency-closure algorithm is not supplied.
    status: OPEN

  - id: FKN-G005
    class: DECISION_RELEVANT
    issue: >
      Exact raw-evidence escalation criteria are not supplied.
    status: OPEN

  - id: FKN-G006
    class: EXPLANATORY
    issue: >
      Exact graph relation type registry is not supplied.
    status: OPEN

  - id: FKN-G007
    class: EXPLANATORY
    issue: >
      Exact persistence and versioning schema is not supplied.
    status: OPEN

  - id: FKN-G008
    class: EXPLANATORY
    issue: >
      Exact H/M/L compression algorithm is not supplied.
    status: OPEN

  - id: FKN-G009
    class: DECISION_RELEVANT
    issue: >
      Exact interaction between FKN and RSCF/GMEF requires their
      authoritative contracts.
    status: OPEN

  - id: FKN-G010
    class: DECISION_RELEVANT
    issue: >
      Exact local-fast-path proof requirements are not defined by this
      terse node.
    status: OPEN
```

---

# 197. Falsifiers

```yaml
falsifiers:

  - id: FKN-F001
    condition: >
      Authoritative FKN canon defines a resolution structure other than
      H/M/L.

  - id: FKN-F002
    condition: >
      Authoritative canon explicitly defines H/M/L as non-recursive
      globally fixed layers, falsifying the relative recursive model
      used in this expansion.

  - id: FKN-F003
    condition: >
      Authoritative canon defines fractal traversal in materially
      different terms from selective scale-invariant graph navigation.

  - id: FKN-F004
    condition: >
      A later canonical node explicitly supersedes this specification.

  - id: FKN-F005
    condition: >
      Authoritative canon mandates exhaustive raw-evidence loading,
      contradicting the selective retrieval model.

  - id: FKN-F006
    condition: >
      Authoritative HML canon establishes materially different semantics
      for H, M, or L.
```

---

# 198. Proof Capsule

```yaml
proof_capsule:

  claim:
    text: >
      FRACTAL_KNOWLEDGE_NETWORK specifies scale-invariant knowledge
      graph traversal across H/M/L resolutions.
    class: SOURCE_CLAIM

  source_basis:
    - supplied_core_law_node

  load_bearing_premises:

    - id: P1
      statement: >
        The supplied node is titled FRACTAL_KNOWLEDGE_NETWORK
        Specification.
      class: SOURCE_CLAIM

    - id: P2
      statement: >
        Its governing sentence explicitly specifies scale-invariant
        knowledge graph traversal.
      class: SOURCE_CLAIM

    - id: P3
      statement: >
        The traversal operates across H/M/L resolutions.
      class: SOURCE_CLAIM

  derived_architecture:
    statement: >
      A resolution-aware traversal system can begin at a compact
      representation and selectively descend into more detailed
      dependencies when required.
    class: MODEL

  scope:
    - AMOS
    - core_laws
    - knowledge_graph_traversal

  competing:
    - >
      Exact H/M/L semantics may differ if authoritative HML canon
      defines them more specifically.

  falsifiers:
    - FKN-F001
    - FKN-F002
    - FKN-F003
    - FKN-F004
    - FKN-F005
    - FKN-F006

  confidence_ceiling:
    source_statement: SOURCE_SUPPORTED
    expanded_mechanics: MODEL_DERIVED
```

---

# 199. Dependency Graph

```text
                         [[00_HOME]]
                              |
                              v
                    [[AMOS_RSCF_NODES]]
                              |
                              v
                       [[LAW_HIERARCHY]]
                              |
                              v
              [[FRACTAL_KNOWLEDGE_NETWORK]]
                     /        |         \
                    /         |          \
                   v          v           v
                 H            M            L
                   \          |           /
                    \         |          /
                     +--------+---------+
                              |
                              v
                     dependency traversal
                              |
                              v
                       raw evidence
                    only when required
```

Only the supplied index/parent relations are directly source-defined.

The internal dependency architecture is model-level expansion.

---

# 200. Extended Architecture

```text
                     OBJECTIVE
                         |
                         v
                 BOOTSTRAP CAPSULE
                         |
                         v
                         H
                +--------+--------+
                |                 |
                v                 v
               M1                M2
                |                 |
           +----+----+            |
           |         |            |
           v         v            v
          L1        L2           L3
           |                      |
           v                      v
      RAW SOURCE             RAW SOURCE
      if required            if required

Cross-links:
L1 -------- DEPENDS_ON --------> L3
M1 -------- CONTRADICTS -------> M2
L2 -------- DERIVED_FROM ------> SOURCE
```

The architecture is a graph despite its hierarchical resolution
surface.

---

# 201. Operational Contract

```yaml
operational_contract:

  objective:
    - retrieve_smallest_sufficient_knowledge_structure
    - preserve_integrity_under_compression
    - enable_recursive_expansion

  default_start:
    resolution: H

  traversal:
    strategy:
      - identify_decision_changing_uncertainty
      - identify_material_dependencies
      - traverse_only_material_branches
      - validate_returned_nodes
      - recurse_when_required

  raw_evidence:
    default: DO_NOT_LOAD_UNLESS_REQUIRED

  preserve:
    - epistemic_class
    - provenance
    - provenance_ancestry
    - dependencies
    - scope
    - regime
    - freshness
    - contradictions
    - competing_hypotheses
    - falsifiers
    - confidence_ceiling

  stop_when:
    - claim_sufficiency
    - decision_sufficiency
    - action_sufficiency

  escalate_when:
    - contradiction
    - weak_evidence
    - stale_evidence
    - scope_mismatch
    - regime_crossing
    - causal_ambiguity
    - provenance_correlation
    - ambiguous_dependency
    - irreversible_stakes
    - governance_impact
```

---

# 202. Compact Canon Contract

```text
FRACTAL_KNOWLEDGE_NETWORK
SPECIFIES SCALE-INVARIANT
KNOWLEDGE GRAPH TRAVERSAL
ACROSS H / M / L RESOLUTIONS.

H ORIENTS.

M DECOMPOSES.

L RESOLVES DETAIL.

RAW EVIDENCE
IS LOADED ONLY WHEN REQUIRED.

H/M/L
ARE RESOLUTION ROLES,
NOT CONFIDENCE LEVELS.

H/M/L
ARE NOT EPISTEMIC CLASSES.

THE NETWORK IS A GRAPH,
NOT MERELY A TREE.

TRAVERSE DEPENDENCIES
THAT CAN MATERIALLY ALTER
THE ANSWER.

DO NOT LOAD
IRRELEVANT BRANCHES.

DO NOT STOP
BEFORE LOAD-BEARING
UNCERTAINTY IS RESOLVED.

COMPRESSION MUST PRESERVE
PROVENANCE,
SCOPE,
REGIME,
FRESHNESS,
DEPENDENCIES,
CONTRADICTIONS,
FALSIFIERS,
AND CONFIDENCE CEILINGS
WHEN MATERIAL.

SEPARATE NODES
DO NOT PROVE
INDEPENDENT PROVENANCE.

GRAPH CONNECTION
DOES NOT PROVE CAUSATION.

SCALE-INVARIANT TRAVERSAL
DOES NOT PROVE
SCALE-INVARIANT REALITY.

LOCAL REASONING
IS VALID ONLY WHEN
MATERIAL DEPENDENCY CLOSURE
IS ESTABLISHED.

WHEN A PREMISE FAILS,
INVALIDATE ONLY
DEPENDENT KNOWLEDGE
WHERE COMPUTABLE.

STOP WHEN
CLAIM SUFFICIENCY,
DECISION SUFFICIENCY,
AND ACTION SUFFICIENCY
ARE ACHIEVED.
```

---

# 203. RSCF Contract

```yaml
RSCF-CONTRACT:

  node_id: fractal_knowledge_network

  node_type: core_law

  H:
    name: FRACTAL_KNOWLEDGE_NETWORK Specification

    governing_statement: >
      Specifies scale-invariant knowledge graph traversal across
      H/M/L resolutions.

  M:
    major_subsystems:
      - H_resolution
      - M_resolution
      - L_resolution
      - dependency_directed_traversal
      - selective_expansion
      - selective_invalidation
      - raw_evidence_escalation

  L:
    mechanics:
      - start_at_smallest_sufficient_resolution
      - identify_decision_changing_uncertainty
      - follow_material_dependencies
      - preserve_provenance
      - preserve_scope
      - preserve_regime
      - preserve_freshness
      - preserve_conflicts
      - stop_at_sufficiency
      - load_raw_evidence_only_when_required

  state: SOURCE_CLAIM

  claim_class: AMOS_MODEL

  provenance: AMOS_corpus

  scope:
    - core_laws
    - knowledge_network
    - fractal_traversal

  confidence_ceiling:
    source_statement: SOURCE_SUPPORTED
    expanded_architecture: MODEL_DERIVED
```

---

# 204. RSCF-NODE

```yaml
RSCF-NODE:

  node_id: fractal_knowledge_network

  node_type: core_law

  title:
    FRACTAL_KNOWLEDGE_NETWORK Specification

  path:
    01_CANON/01_CORE_LAWS/FRACTAL_KNOWLEDGE_NETWORK.md

  state:
    SOURCE_CLAIM

  claim_class:
    AMOS_MODEL

  provenance:
    AMOS_corpus

  scope:
    - core_laws

  governs:
    - scale_invariant_knowledge_graph_traversal
    - H_resolution
    - M_resolution
    - L_resolution
```

---

# 205. RSCF-RELATIONS

```yaml
RSCF-RELATIONS:

  - INDEXED_BY: [[00_HOME]]

  - INDEXED_BY: [[AMOS_RSCF_NODES]]

  - CHILD_OF: [[LAW_HIERARCHY]]

  - INDEXED_BY: [[01_CORE_LAWS_MOC]]

  - FRAMEWORK_CONTEXT:
      [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
```

---

# 206. Canon Preservation Rule

The exact supplied source spine must remain recoverable:

```markdown
---
title: FRACTAL_KNOWLEDGE_NETWORK Specification
type: core_law
source: 01_CANON/01_CORE_LAWS
tags:
- core_law
- fractal
- knowledge_network
---

# FRACTAL_KNOWLEDGE_NETWORK Specification

Specifies scale-invariant knowledge graph traversal across H/M/L resolutions.
```

Expansion must not silently rewrite that source statement into a
stronger empirical claim.

---

# 207. Canon Boundary

> [!important] Canon Boundary
>
> The supplied source directly establishes:
>
> **FRACTAL_KNOWLEDGE_NETWORK specifies scale-invariant knowledge graph
> traversal across H/M/L resolutions.**
>
> It also establishes the node's canonical path, basic tags, related
> index nodes, MOC, Trang Framework relation, and RSCF index/parent
> relations.
>
> It does **not**, by itself, define the exact semantics of H, M, and L;
> a literal graph-database implementation; exact retrieval algorithms;
> raw-evidence schemas; cache mechanics; formal mathematical fractal
> properties; or universal scale invariance in reality.
>
> Those additions in this expanded specification are architectural
> `MODEL` / `DERIVED` elaborations unless separately supported by
> authoritative AMOS canon.

---

# 208. Final Integrity Rule

```text
FRACTAL_KNOWLEDGE_NETWORK
IS THE AMOS
SCALE-INVARIANT
KNOWLEDGE GRAPH
TRAVERSAL SPECIFICATION
ACROSS H / M / L
RESOLUTIONS.

BEGIN WITH
THE SMALLEST SUFFICIENT
KNOWLEDGE CAPSULE.

ORIENT AT H.

DESCEND TO M
WHEN THE RELEVANT
SUBSYSTEM MUST BE RESOLVED.

DESCEND TO L
WHEN EXACT DETAIL
CAN CHANGE THE RESULT.

LOAD RAW EVIDENCE
ONLY WHEN THE
CURRENT KNOWLEDGE LAYER
CANNOT SAFELY RESOLVE
A MATERIAL QUESTION.

DO NOT CONFUSE
RESOLUTION
WITH CONFIDENCE.

DO NOT CONFUSE
RESOLUTION
WITH EPISTEMIC CLASS.

DO NOT CONFUSE
GRAPH CONNECTION
WITH CAUSATION.

DO NOT CONFUSE
NODE MULTIPLICITY
WITH PROVENANCE
INDEPENDENCE.

DO NOT CONFUSE
SCALE-INVARIANT
TRAVERSAL
WITH A CLAIM THAT
REALITY ITSELF
IS UNIVERSALLY FRACTAL.

PRESERVE
PROVENANCE.

PRESERVE
DEPENDENCIES.

PRESERVE
SCOPE.

PRESERVE
REGIME.

PRESERVE
FRESHNESS.

PRESERVE
CONTRADICTIONS.

PRESERVE
COMPETING HYPOTHESES.

PRESERVE
FALSIFIERS.

PRESERVE
CONFIDENCE CEILINGS.

WHEN A LOAD-BEARING
NODE FAILS,
INVALIDATE ITS
DEPENDENT KNOWLEDGE,
NOT THE ENTIRE NETWORK,
UNLESS GLOBAL DEPENDENCY
IS ESTABLISHED.

WHEN LOCALITY,
DEPENDENCY CLOSURE,
PROVENANCE INDEPENDENCE,
SCOPE,
REGIME,
FRESHNESS,
AND NON-CONFLICT
ARE SUFFICIENTLY ESTABLISHED:

REASON LOCALLY.

WHEN THEY ARE NOT:

ESCALATE THROUGH
THE FRACTAL NETWORK.

TRAVERSE ONLY
WHAT CAN MATERIALLY
CHANGE THE ANSWER.

STOP WHEN
CLAIM,
DECISION,
AND ACTION
SUFFICIENCY
ARE ACHIEVED.

IF THE REQUIRED
CANON OR EVIDENCE
DOES NOT EXIST:

DO NOT INVENT IT.

EXPOSE THE GAP.

INTEGRITY
>
COMPLETENESS
>
FLUENCY
>
SPEED.
```

---

## Related

[[00_HOME]] ·
[[AMOS_RSCF_NODES]] ·
[[LAW_HIERARCHY]]

---

**MOC:** [[01_CORE_LAWS_MOC]]

---

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---

RSCF-NODE
node_id: fractal_knowledge_network
node_type: core_law
path: 01_CANON/01_CORE_LAWS/FRACTAL_KNOWLEDGE_NETWORK.md

RSCF-RELATIONS:

* INDEXED_BY: [[00_HOME]]
* INDEXED_BY: [[AMOS_RSCF_NODES]]
* CHILD_OF: [[LAW_HIERARCHY]]

---

[[00_ROOT_MOC|AMOS MOC]]
