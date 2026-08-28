---
title: L17 RSCF
type: rscf
source: 01_CANON/01_CORE_LAWS
tags:
  - canon
  - core_laws
  - rscf
  - claim_discipline
  - claim_taxonomy
  - proof_capsule
  - no_proof_no_claim
  - conditional_carry
  - dependency_propagation
  - confidence_ceiling
  - gaps
  - falsifiers
  - epistemic_governance
  - provenance
  - canon/universe
rscf:
  state: SOURCE_CLAIM
  claim_class: CONDITIONAL
  provenance: AMOS_corpus
  scope: core_laws
  canonical_status: CONDITIONAL
  specification_status: PROPOSED_SPECIFICATION
  node_id: l17_rscf
  node_type: note
---

# L17 RSCF Claim Discipline

**STATUS:** PROPOSED_SPECIFICATION
**epistemic_class:** AMOS_MODEL
**canonical_status:** CONDITIONAL
**updated:** 2026-08-26

---

# 0. Status

L17 defines the proposed AMOS **RSCF Claim Discipline**.

It replaces the prior placeholder with a structured specification governing:

- claim typing,
- separation of epistemic classes,
- proof capsules,
- established versus not-established content,
- explicit gaps,
- falsifiers,
- confidence ceilings,
- no-proof-no-claim discipline,
- conditional dependency propagation,
- provenance-aware derivation,
- contradiction preservation,
- competing claims,
- local invalidation,
- proof reuse,
- freshness and regime validity,
- RSCF graph composition,
- interaction with H/M/L rigor,
- interaction with causal reasoning,
- interaction with persistent knowledge,
- consequential claim finalization.

L17 remains:

```text
PROPOSED_SPECIFICATION
        │
        ▼
    AMOS_MODEL
        │
        ▼
    CONDITIONAL

until authoritative RSCF canon validates, modifies, supersedes, or rejects these semantics.

The four source laws are:

```text
RSCF-1 CLASS CONTRACT
RSCF-2 PROOF CAPSULE
RSCF-3 NO-PROOF-NO-CLAIM
RSCF-4 CONDITIONAL CARRY
```

The central invariant is:

```text
A CLAIM MAY NEVER
OUTRUN ITS PROOF,
ITS PREMISES,
OR ITS CONDITIONS.
```

---

# 1. Governing Objective

RSCF exists to prevent epistemic laundering.

The prohibited pattern is:

```text
SOURCE SAYS X
      ↓
MODEL EXTENDS X
      ↓
FLUENT SYNTHESIS
      ↓
X' PRESENTED AS ESTABLISHED
```

RSCF instead requires:

```text
CLAIM
  ↓
CLASS
  ↓
PROVENANCE
  ↓
PREMISES
  ↓
PROOF STATUS
  ↓
GAPS
  ↓
FALSIFIERS
  ↓
CONFIDENCE CEILING
```

The governing principle is:

```text
INTEGRITY OF CLAIM STATUS
>
COMPLETENESS OF NARRATIVE
```

Missing proof remains missing.

---

# 2. Core RSCF Laws

```text
RSCF-1
CLASS CONTRACT

RSCF-2
PROOF CAPSULE

RSCF-3
NO-PROOF-NO-CLAIM

RSCF-4
CONDITIONAL CARRY
```

Unified:

```text
PROPOSITION
    ↓
ASSIGN CLASS
    ↓
IDENTIFY LOAD-BEARING PREMISES
    ↓
BUILD PROOF CAPSULE
    ↓
SEPARATE ESTABLISHED
FROM NOT ESTABLISHED
    ↓
PRESERVE GAPS
    ↓
PROPAGATE CONDITIONS
    ↓
SET CONFIDENCE CEILING
    ↓
CLASSIFY CONCLUSION
```

---

# 3. RSCF-1 — Class Contract

**Law**

Every claim is:

```text
SOURCE
DERIVED
MODEL
UNKNOWN
```

and silently mixing classes is a violation.

The source terminology establishes a four-class contract:

```yaml
rscf_claim_classes:
  - SOURCE
  - DERIVED
  - MODEL
  - UNKNOWN
```

These are epistemic roles.

They answer:

> **What kind of epistemic object is this claim?**

They do not, by themselves, answer:

> **How confident should we be that it is true?**

---

# 4. SOURCE

A `SOURCE` claim records what a source asserts.

Conceptually:

```yaml
claim:
  class: SOURCE
  proposition: X
  provenance:
    source: S
```

The valid conclusion is:

```text
SOURCE S ASSERTS X
```

not automatically:

```text
X IS TRUE
```

Therefore:

```text
SOURCE
≠
VERIFIED FACT
```

---

# 5. SOURCE_CLAIM Compatibility

Existing AMOS metadata uses:

```text
SOURCE_CLAIM
```

while L17's source law says:

```text
SOURCE
```

The supplied L17 text does not define whether these are exact synonyms.

Therefore the safest representation is:

```yaml
taxonomy_mapping:
  SOURCE:
    existing_label: SOURCE_CLAIM
    relation: LIKELY_COMPATIBLE
    canonical_equivalence: NOT_ESTABLISHED
```

Until authoritative RSCF canon resolves the mapping:

```text
SOURCE
≈
SOURCE_CLAIM

but

SOURCE = SOURCE_CLAIM
```

is not asserted as canonical fact.

---

# 6. DERIVED

A `DERIVED` claim follows from identified premises through an explicit reasoning relation.

Conceptually:

```text
P1
+
P2
+
RULE R
↓
C
```

Then:

```yaml
claim:
  class: DERIVED
  proposition: C
  depends_on:
    - P1
    - P2
  derivation_rule: R
```

A derived claim cannot be stronger than its load-bearing premises unless independently revalidated.

---

# 7. Derived Confidence Ceiling

For:

```text
C = derive(P1, P2, ..., Pn)
```

conceptually:

```text
CONFIDENCE(C)
≤
MIN LOAD-BEARING SUPPORT
OF P1...Pn
```

unless C receives independent evidence.

Therefore:

```text
WEAK PREMISE
     ↓
DERIVED CLAIM
```

cannot become:

```text
STRONG CLAIM
```

merely because the derivation is fluent or logically elaborate.

---

# 8. MODEL

A `MODEL` claim is a proposed representation, interpretation, mechanism, abstraction, mapping, hypothesis, or explanatory structure.

Conceptually:

```yaml
claim:
  class: MODEL
  proposition:
    "Structure M explains or represents X"
```

A model may be:

* useful,
* coherent,
* predictive,
* elegant,
* operationally valuable,

without being empirically verified.

Thus:

```text
MODEL
≠
OBSERVED FACT
```

and:

```text
MODEL FIT
≠
CAUSAL PROOF
```

---

# 9. UNKNOWN

`UNKNOWN` records unresolved epistemic state.

It is not an error to be hidden.

It is a valid RSCF output.

```yaml
claim:
  class: UNKNOWN
  proposition: X
  reason:
    insufficient_evidence
```

Conceptually:

```text
NO SUFFICIENT PROOF
      ↓
UNKNOWN / GAP
```

not:

```text
NO SUFFICIENT PROOF
      ↓
PLAUSIBLE-SOUNDING COMPLETION
```

---

# 10. UNKNOWN Is Information

An explicit unknown communicates:

* what has not been established,
* where proof closure fails,
* which dependency is missing,
* what evidence could resolve it.

Therefore:

```text
UNKNOWN
>
FABRICATED COMPLETENESS
```

under the AMOS integrity ordering.

---

# 11. Class Orthogonality

Claim class is distinct from confidence/status.

For example:

```yaml
claim:
  epistemic_class: MODEL
  claim_class: CONDITIONAL
```

is coherent.

Likewise:

```yaml
claim:
  epistemic_class: DERIVED
  claim_class: VERIFIED
```

may be coherent if the derivation and premises are sufficiently established within scope.

Thus:

```text
SOURCE / DERIVED / MODEL / UNKNOWN
```

should not be silently collapsed into:

```text
VERIFIED / CONDITIONAL / COMPETING / GAP
```

These represent different dimensions.

---

# 12. Epistemic Type vs Conclusion Class

A useful conceptual separation is:

```text
EPISTEMIC TYPE
SOURCE
DERIVED
MODEL
UNKNOWN

        ×

CONCLUSION STATUS
VERIFIED
DERIVED
MODEL
CONDITIONAL
COMPETING
UNKNOWN/GAP
```

The exact canonical cross-product is not supplied.

Therefore this is a proposed representation rather than recovered authoritative taxonomy.

---

# 13. Class Contract Invariant

Every consequential proposition should permit the question:

```text
WHAT CLASS IS THIS CLAIM?
```

If the answer is hidden or ambiguous:

```text
RSCF CLASS CONTRACT
=
VIOLATED
```

for purposes of this proposed specification.

---

# 14. No Silent Class Mixing

Invalid:

```text
SOURCE:
"System X may produce Y."

SYNTHESIS:
"System X produces Y."
```

The modal uncertainty has disappeared.

Likewise invalid:

```text
MODEL:
"A could explain B."

SYNTHESIS:
"A caused B."
```

The epistemic class changed silently.

---

# 15. Explicit Class Transition

Class transitions may occur when justified.

Example:

```text
SOURCE
  ↓
INDEPENDENT VALIDATION
  ↓
ESTABLISHED OBSERVATION
```

or:

```text
MODEL
  ↓
DISCRIMINATING TESTS
  ↓
STRONGER SUPPORT
```

But the transition itself must be evidenced.

The rule is:

```text
CLASS CHANGE
REQUIRES
JUSTIFICATION
```

---

# 16. Claim Identity

A claim should be treated as a typed proposition rather than free-floating prose.

Conceptually:

```yaml
claim:
  claim_id: C17
  proposition: string
  epistemic_class: SOURCE | DERIVED | MODEL | UNKNOWN
```

This permits dependencies and invalidation to target claims precisely.

---

# 17. Claim Granularity

One paragraph may contain multiple claims with different classes.

Example:

```text
S1: Source A reports X.        SOURCE
D1: X implies Y under rule R. DERIVED
M1: Y may explain Z.          MODEL
U1: Whether Z causes Q.       UNKNOWN
```

Flattening the paragraph into one undifferentiated status loses epistemic structure.

---

# 18. Atomic Claim Discipline

Where consequential, decompose compound claims:

```text
A and B and C
```

into:

```text
C1 = A
C2 = B
C3 = C
```

when their proof states differ.

Otherwise one established clause can mask an unsupported clause.

---

# 19. Mixed-Class Artifact

An artifact may legitimately contain:

```yaml
artifact:
  claims:
    - id: C1
      class: SOURCE

    - id: C2
      class: DERIVED

    - id: C3
      class: MODEL

    - id: C4
      class: UNKNOWN
```

The artifact itself should not silently flatten all claims to the strongest status.

---

# 20. RSCF-2 — Proof Capsule

**Law**

Consequential claims carry a proof capsule containing:

```text
claim
established
not_established
gaps
falsifiers
ceiling
```

This is the minimum source-defined capsule.

---

# 21. Minimal Proof Capsule

```yaml
proof_capsule:

  claim:
    string

  established:
    []

  not_established:
    []

  gaps:
    []

  falsifiers:
    []

  ceiling:
    string
```

This is the closest direct structural rendering of RSCF-2.

---

# 22. Claim Field

The capsule's `claim` field identifies the proposition being evaluated.

```yaml
claim:
  text:
    "X"
```

A capsule without a precise claim risks proof leakage because evidence may support only part of an ambiguous proposition.

---

# 23. Established

`established` records what the available proof actually supports.

Example:

```yaml
established:
  - source_S_reports_X
  - artifact_hash_matches_reference
```

This should remain narrower than or equal to the evidence.

Never expand:

```text
ESTABLISHED:
SOURCE REPORTS X
```

into:

```text
ESTABLISHED:
X IS TRUE
```

without additional proof.

---

# 24. Not Established

`not_established` records propositions that the current proof does not support.

Example:

```yaml
not_established:
  - X_is_independently_verified
  - X_generalizes_to_regime_R2
  - X_causes_Y
```

This field is critical because it prevents readers from inferring unsupported extensions from an otherwise strong capsule.

---

# 25. Established / Not-Established Firewall

```text
ESTABLISHED
────────────
WHAT PROOF SUPPORTS

NOT ESTABLISHED
───────────────
WHAT MUST NOT BE INFERRED
```

The second field is not redundant.

It explicitly marks the epistemic boundary.

---

# 26. Gaps

`gaps` record missing information or unresolved proof requirements.

```yaml
gaps:
  - id: G1
    missing:
      independent_validation
```

A gap should identify the minimum missing element when possible.

---

# 27. Gap Severity

A proposed extension may classify gaps as:

```text
CRITICAL
DECISION-RELEVANT
EXPLANATORY
COSMETIC
```

This taxonomy is consistent with broader AMOS gap handling but is not explicitly supplied by the four L17 laws.

Therefore it remains an AMOS_MODEL extension.

---

# 28. Critical Gap

A critical gap blocks the target claim or action.

```text
CLAIM C
depends on
P

P = UNKNOWN
```

If P is indispensable:

```text
C
cannot exceed
UNKNOWN / CONDITIONAL
```

depending on the exact logical structure.

---

# 29. Decision-Relevant Gap

A decision-relevant gap can change the selected action but may not invalidate all descriptive claims.

Example:

```text
Option A cheaper?
ESTABLISHED

Option A legally permitted?
UNKNOWN
```

The first claim may survive.

The action may remain blocked.

---

# 30. Explanatory Gap

An explanatory gap affects understanding but not the current decision.

It should remain visible but should not force unnecessary retrieval if it cannot change the outcome.

---

# 31. Cosmetic Gap

A cosmetic gap affects presentation rather than substantive claim validity.

RSCF should not spend disproportionate validation effort resolving cosmetic gaps before critical ones.

---

# 32. Falsifiers

A proof capsule carries conditions or observations that would invalidate, weaken, or require reconsideration of the claim.

```yaml
falsifiers:
  - authoritative_source_contradicts_X
  - discriminating_test_fails
```

A falsifier makes the claim operationally challengeable.

---

# 33. Falsifier Scope

Falsifiers should target the actual claim.

A falsifier for:

```text
MODEL M explains X in regime R1
```

need not invalidate:

```text
MODEL M explains Y in regime R2
```

unless dependency and scope establish that connection.

---

# 34. Ceiling

The `ceiling` field limits the strongest conclusion justified by current support.

Example:

```yaml
ceiling:
  CONDITIONAL
```

means the claim must not be presented as VERIFIED under the current proof state.

---

# 35. Confidence Ceiling Principle

Conceptually:

```text
CLAIM STRENGTH
≤
PROOF CEILING
```

The ceiling may be constrained by:

* weak premises,
* unresolved gaps,
* source-only evidence,
* correlated provenance,
* stale evidence,
* scope mismatch,
* unresolved contradictions,
* model uncertainty,
* conditional dependencies.

---

# 36. Ceiling Is Not Average Confidence

Suppose:

```text
P1 = very strong
P2 = very strong
P3 = unresolved
```

and all three are load-bearing.

The conclusion does not receive the average:

```text
HIGH + HIGH + UNKNOWN
---------------------
      MEDIUM
```

Instead the unresolved load-bearing premise constrains the conclusion.

This is a structural ceiling, not an arithmetic mean.

---

# 37. Extended Proof Capsule

A richer AMOS representation may preserve:

```yaml
proof_capsule:

  claim:
    id: string
    text: string
    epistemic_class:
      SOURCE | DERIVED | MODEL | UNKNOWN

  established: []

  not_established: []

  gaps: []

  falsifiers: []

  ceiling:
    VERIFIED |
    DERIVED |
    MODEL |
    CONDITIONAL |
    COMPETING |
    UNKNOWN

  premises: []

  provenance:
    roots: []

  scope:
    string|null

  regime:
    string|null

  freshness:
    string|null

  dependencies: []

  competing_explanations: []
```

Only the six source fields are explicitly required by L17 as supplied.

The rest are proposed extensions.

---

# 38. Capsule Completeness

A proof capsule is not necessarily an exhaustive proof transcript.

It should contain the smallest sufficient structure needed to preserve:

* what is claimed,
* what is established,
* what remains unestablished,
* what is missing,
* what could falsify it,
* how strongly it may be stated.

Thus:

```text
PROOF CAPSULE
≠
HIDDEN CHAIN OF THOUGHT
```

It is a compact epistemic contract.

---

# 39. Capsule Reuse

A proof capsule may be reused only while its load-bearing validity conditions remain satisfied.

Conceptually:

```text
CAPSULE C @ EPOCH E1
       ↓
DEPENDENCIES STILL VALID?
SCOPE STILL MATCHES?
REGIME STILL MATCHES?
FRESHNESS STILL VALID?
       ↓
YES → REUSE
NO  → REVALIDATE
```

This is an AMOS_MODEL extension consistent with persistent provenance.

---

# 40. Capsule Identity

A reusable capsule should have stable identity.

```yaml
proof_capsule:
  capsule_id: PC_001
  claim_id: C_001
```

This allows dependent claims to reference the capsule without copying or silently altering it.

---

# 41. Capsule Versioning

Conceptually:

```yaml
proof_capsule:
  capsule_id: PC_001
  version: 3
  epoch: E17
```

A new version should preserve lineage to the prior capsule when the proof state changes.

---

# 42. Capsule Provenance

```yaml
proof_capsule:
  provenance:
    roots:
      - source_A
      - observation_B

    ancestry:
      - edge_1
      - edge_2
```

This prevents multiple descendants of one source from being mistaken for independent support.

---

# 43. Capsule Dependency Closure

A capsule need not load every known artifact.

It should preserve the dependencies capable of changing the claim.

```text
CLAIM
 ↓
LOAD-BEARING PREMISES
 ↓
LOAD-BEARING EVIDENCE
```

Non-material background can remain unloaded.

---

# 44. RSCF-3 — No-Proof-No-Claim

**Law**

Absence of proof is recorded as a gap, never filled by fluent inference.

This is the principal anti-fabrication firewall.

```text
NO PROOF
   ↓
GAP
```

not:

```text
NO PROOF
   ↓
PLAUSIBLE INFERENCE
   ↓
CLAIM
```

---

# 45. No-Proof-No-Claim Invariant

```text
IF
required proof for proposition P is absent

THEN
P is not established.
```

The system may still state:

```text
P is possible
P is a model
P is a hypothesis
P is unknown
```

when properly typed.

It may not silently state:

```text
P is established
```

---

# 46. Fluent Inference Firewall

Language fluency creates no epistemic entitlement.

```text
COHERENT SENTENCE
≠
SUPPORTED CLAIM
```

Likewise:

```text
PLAUSIBILITY
≠
PROOF
```

and:

```text
ABSENCE OF CONTRADICTION
≠
CONFIRMATION
```

---

# 47. Missing Bridge

Suppose:

```text
A established
B established
```

but the required rule:

```text
A + B ⇒ C
```

is not established.

Then:

```text
C
```

remains unsupported.

The missing logical bridge itself is a gap.

```yaml
gaps:
  - missing_derivation_rule_for_C
```

---

# 48. Missing Evidence

Suppose:

```text
MODEL M predicts X
```

but X has not been observed.

Then:

```text
M predicts X
```

may be established as a model consequence.

But:

```text
X occurred
```

is not established.

RSCF preserves the distinction.

---

# 49. Missing Source

If a claim is attributed to source S but S is unavailable:

```text
"Source S says X"
```

may itself remain unverified unless reliable provenance establishes the attribution.

Do not reconstruct the missing source from downstream summaries and present the reconstruction as original source content.

---

# 50. Missing Canon

If canonical detail is absent:

```text
CANON GAP
```

must remain visible.

Do not replace it with:

```text
LIKELY CANON
```

merely because a model extension fits the architecture.

This is especially important for proposed AMOS specifications.

---

# 51. Model Completion

Model completion is allowed only when labeled.

Example:

```text
SOURCE ESTABLISHES:
A, B

MODEL EXTENSION:
C may follow if assumption Q holds.
```

This is compliant because the epistemic transition is explicit.

---

# 52. Inference as DERIVED

Inference may also be permitted as `DERIVED` when:

* premises are explicit,
* the derivation rule is explicit or sufficiently defined,
* the conclusion does not outrun those premises.

Thus RSCF-3 does not prohibit reasoning.

It prohibits **unmarked reasoning being laundered into proof**.

---

# 53. No-Proof-No-Claim and UNKNOWN

The preferred terminal state for an unresolved proposition is often:

```yaml
claim:
  class: UNKNOWN

gap:
  missing:
    discriminating_evidence
```

This preserves both the question and the reason it remains unresolved.

---

# 54. No-Proof-No-Claim and COMPETING

If evidence supports multiple incompatible explanations:

```text
H1
vs
H2
```

and neither dominates:

```text
COMPETING
```

is superior to inventing convergence.

The unresolved discriminator becomes a gap.

---

# 55. Proof Absence vs Evidence of Absence

RSCF must distinguish:

```text
NO EVIDENCE FOR X
```

from:

```text
EVIDENCE THAT X IS ABSENT
```

These are different claims.

The first normally creates a gap.

The second may support a negative proposition if the observation process is appropriate.

---

# 56. RSCF-4 — Conditional Carry

**Law**

`CONDITIONAL-ON` propagates through all dependents.

Suppose:

```text
P
is valid
CONDITIONAL-ON Q
```

and:

```text
C depends on P
```

Then:

```text
C
```

inherits dependence on Q unless C is independently revalidated without P.

---

# 57. Conditional Propagation

```text
Q
↓
P [CONDITIONAL-ON Q]
↓
C
↓
D
```

Then:

```text
P conditional on Q
C conditional on Q
D conditional on Q
```

for all descendants whose proof requires that path.

---

# 58. Conditional Carry Equation

For claim `C` with load-bearing parents:

```text
Parents(C) = {P1 ... Pn}
```

conceptually:

```text
Conditions(C)
=
⋃ Conditions(Pi)
+
Conditions introduced by C
```

for all load-bearing `Pi`.

This is a proposed formalization of RSCF-4.

---

# 59. Conditional Carry Is Dependency-Specific

Conditions propagate only along actual dependency edges.

```text
Q → P → C
```

does not make unrelated claim:

```text
X
```

conditional on Q.

Thus:

```text
CONDITIONAL PROPAGATION
=
GRAPH-LOCAL
```

not global contamination.

---

# 60. Conditional Carry Through Derivation

```text
P1 [conditional on A]
P2 [conditional on B]
        ↓
        C
```

If both are load-bearing:

```text
C
conditional on
A ∧ B
```

subject to the actual logical relationship.

A richer condition expression may be required where dependencies are disjunctive rather than conjunctive.

---

# 61. Conjunctive Conditions

If C requires both P1 and P2:

```text
C ← P1 ∧ P2
```

and:

```text
P1 conditional on A
P2 conditional on B
```

then conceptually:

```text
C conditional on A ∧ B
```

---

# 62. Disjunctive Conditions

If either independent path can establish C:

```text
C ← P1 ∨ P2
```

with:

```text
P1 conditional on A
P2 conditional on B
```

then the exact condition is not necessarily:

```text
A ∧ B
```

It may be:

```text
A ∨ B
```

depending on proof sufficiency.

Therefore conditional carry should preserve logical structure rather than blindly concatenate labels.

---

# 63. Alternative Independent Proof

Suppose:

```text
P1 [conditional on A]
     ↓
     C
```

but independently:

```text
P2 [verified]
     ↓
     C
```

If P2 independently establishes C within the same scope:

```text
C
```

need not remain conditional on A.

This is not dropping a condition silently.

It is independent revalidation.

---

# 64. Conditional Discharge

A condition may be discharged when its proposition becomes established.

```text
C conditional on Q
```

then later:

```text
Q VERIFIED
```

may permit:

```text
C
```

to be reclassified, provided no other unresolved conditions remain.

The dependent capsule should record the revalidation event.

---

# 65. Conditional Failure

If:

```text
C conditional on Q
```

and:

```text
Q FALSE
```

then C's dependent proof path fails.

This does not necessarily prove:

```text
NOT C
```

because C may have another independent proof path.

Correct action:

```text
INVALIDATE FAILED PATH
↓
SEARCH VALID ALTERNATIVE PATH IF MATERIAL
```

---

# 66. Conditional Unknown

If:

```text
Q UNKNOWN
```

then:

```text
C conditional on Q
```

cannot be upgraded merely because C otherwise appears plausible.

The unresolved condition remains load-bearing.

---

# 67. Nested Conditional Carry

```text
A conditional on X
B conditional on A
C conditional on B
```

Then C transitively depends on X.

Conceptually:

```text
X
↓
A
↓
B
↓
C
```

RSCF should preserve the transitive ancestry.

---

# 68. Condition Identity

Conditions should have stable identities where consequential.

```yaml
condition:
  condition_id: Q17
  proposition: string
```

Then dependents can reference:

```yaml
conditional_on:
  - Q17
```

rather than duplicating potentially divergent prose.

---

# 69. Conditional Carry Schema

```yaml
claim:

  claim_id:
    C1

  proposition:
    string

  conditional_on:
    - condition_id: Q1
      status:
        VERIFIED |
        FALSE |
        UNKNOWN |
        CONDITIONAL

  dependencies:
    - P1
    - P2
```

---

# 70. Conditional Closure

Conceptually:

```python
def conditional_closure(claim):
    conditions = own_conditions(claim)

    for premise in load_bearing_parents(claim):
        conditions |= conditional_closure(premise)

    return conditions
```

Semantic pseudocode only.

Real implementations must handle cycles and alternative proof paths.

---

# 71. RSCF Claim Graph

Claims form a provenance-aware dependency graph.

```text
S1 SOURCE
   │
   ▼
D1 DERIVED
   │
   ├────► M1 MODEL
   │
   ▼
D2 DERIVED
```

Each edge should answer:

```text
HOW DOES THE CHILD DEPEND ON THE PARENT?
```

not merely:

```text
THEY ARE RELATED
```

---

# 72. Dependency Edge Types

A proposed RSCF extension may distinguish:

```yaml
dependency_edges:
  - SUPPORTS
  - DERIVED_FROM
  - CONDITIONAL_ON
  - CONTRADICTS
  - FALSIFIES
  - SPECIALIZES
  - REVALIDATES
  - SUPERSEDES
```

The supplied L17 source does not define this edge taxonomy.

Therefore these remain model-level candidates.

---

# 73. Load-Bearing Edge

A load-bearing edge means:

```text
REMOVE OR INVALIDATE P
```

and the proof of:

```text
C
```

changes materially.

This distinguishes causal/proof dependency from mere citation or contextual relevance.

---

# 74. Non-Load-Bearing Context

A claim may cite contextual material that is not necessary for its proof.

Such context should not automatically constrain:

* confidence ceiling,
* conditional carry,
* invalidation,
* H/M/L inheritance.

Only actual load-bearing dependencies do.

---

# 75. RSCF and Provenance

Every important claim should preserve source ancestry when material.

```text
SOURCE S
   ↓
D1
   ↓
D2
```

D2 should not appear provenance-independent merely because it is two derivation steps away from S.

---

# 76. Provenance Independence

Suppose:

```text
S
├── D1
├── D2
└── D3
```

Then:

```text
D1 + D2 + D3
```

do not constitute three independent source roots.

They share ancestry:

```text
S
```

RSCF should preserve this topology.

---

# 77. Source Multiplicity Firewall

```text
NUMBER OF CLAIMS
≠
NUMBER OF INDEPENDENT SOURCES
```

and:

```text
NUMBER OF CITATIONS
≠
NUMBER OF INDEPENDENT PROOF ROOTS
```

Independence must be demonstrated.

---

# 78. RSCF and Sybil Hardening

A source claim repeated across:

* summaries,
* mirrors,
* derivative documents,
* downstream models,

must not gain artificial confidence through repetition.

Conceptually:

```text
ONE ROOT
→ MANY DESCENDANTS
```

remains one ancestral root unless independent evidence exists.

---

# 79. RSCF and Contradiction

If:

```text
C1: X
C2: NOT X
```

both have material support:

```text
DO NOT
silently average
or select by fluency
```

Instead preserve:

```yaml
status:
  COMPETING
```

until authority, scope, provenance, or discriminating evidence resolves the conflict.

---

# 80. Contradiction Is Not Always Global

Claims may differ by scope:

```text
C1:
X in regime R1

C2:
NOT X in regime R2
```

These are not necessarily contradictory.

RSCF contradiction analysis must compare applicability envelopes.

---

# 81. RSCF and Scope

A proof capsule should preserve the domain in which the claim is established.

Conceptually:

```yaml
scope:
  system: string|null
  population: string|null
  environment: string|null
  scale: string|null
  time: string|null
  regime: string|null
```

The exact schema is an AMOS_MODEL extension.

---

# 82. Scope Inheritance

A derived claim cannot silently broaden beyond its premises.

If:

```text
P established in SCOPE A
```

then:

```text
C derived from P
```

inherits that scope unless independent justification supports expansion.

Thus:

```text
LOCAL EVIDENCE
≠
UNIVERSAL CLAIM
```

---

# 83. Scope Intersection

If C depends jointly on:

```text
P1 valid in S1
P2 valid in S2
```

then C's direct validity is generally bounded by their compatible intersection:

```text
Scope(C)
⊆
S1 ∩ S2
```

unless another proof establishes a broader envelope.

This is a conceptual rule, not a recovered RSCF formula.

---

# 84. Regime Carry

Conditional carry should include regime conditions when load-bearing.

```text
P valid only in R1
↓
C derived from P
```

then:

```text
C valid only in R1
```

unless independently validated elsewhere.

---

# 85. Freshness Carry

If a claim depends on time-sensitive evidence:

```text
E valid until T
↓
C
```

then C cannot silently outlive E's validity horizon.

Thus:

```text
STALE PREMISE
→
DEPENDENT CLAIM REVALIDATION
```

---

# 86. RSCF and Causal Firewall

A source may establish:

```text
A correlates with B
```

A model may propose:

```text
A causes B
```

RSCF must preserve the class transition:

```text
SOURCE:
association

MODEL:
causal interpretation
```

until causal evidence licenses stronger classification.

---

# 87. Structural Similarity Firewall

```text
SYSTEM A
resembles
SYSTEM B
```

may support:

```text
MODEL:
possible analogous mechanism
```

It does not by itself support:

```text
DERIVED:
same causal mechanism
```

unless a valid bridge exists.

---

# 88. Sequence Firewall

```text
A happened
then
B happened
```

is not sufficient proof that:

```text
A caused B
```

RSCF records the causal bridge as missing if no appropriate evidence exists.

---

# 89. RSCF and H/M/L

RSCF claim discipline and H/M/L rigor are orthogonal.

Example:

```yaml
claim:
  epistemic_class: MODEL
  claim_class: CONDITIONAL

  hml:
    effective_level: H
```

This means:

```text
THE CLAIM IS A MODEL

AND

THE CLAIM REQUIRES H-LEVEL
GOVERNANCE RIGOR
```

No contradiction exists.

---

# 90. RSCF/HML Composition

Conceptually:

```text
RSCF
answers:
WHAT IS THE EPISTEMIC STATUS?

H/M/L
answers:
WHAT VALIDATION RIGOR APPLIES?
```

Together:

```text
CLAIM
 ↓
RSCF CLASS
 ↓
H/M/L LEVEL
 ↓
PROOF CAPSULE
 ↓
CONCLUSION
```

---

# 91. Strictness and Ceiling

H/M/L provides a validation floor.

RSCF provides an epistemic ceiling.

Conceptually:

```text
H/M/L:
HOW MUCH RIGOR IS REQUIRED?

RSCF:
HOW STRONGLY MAY THE RESULT BE CLAIMED?
```

Thus:

```text
VALIDATION FLOOR
+
CONFIDENCE CEILING
```

jointly constrain output.

---

# 92. RSCF and Competing Hypotheses

Suppose:

```text
M1 explains X
M2 explains X
```

Both are MODEL.

If evidence cannot discriminate:

```yaml
conclusion:
  class: COMPETING
  candidates:
    - M1
    - M2
```

Do not force one model into DERIVED or VERIFIED merely because it is more fluent.

---

# 93. Cheapest Discriminating Test

When competing claims matter, seek evidence E such that:

```text
Prediction(M1, E)
≠
Prediction(M2, E)
```

This has greater decision value than evidence both models predict.

This is an AMOS_MODEL operational extension.

---

# 94. RSCF and Adversarial Validation

For consequential claims:

```text
BUILD STRONGEST SUPPORTED CLAIM
          ↓
CHALLENGE IT
```

Challenge for:

* contradictory evidence,
* correlated provenance,
* hidden conditions,
* stale premises,
* scope leakage,
* regime mismatch,
* causal overreach,
* stronger competing models,
* missing proof bridges.

If challenge succeeds:

```text
DOWNGRADE
CONDITION
PRESERVE COMPETING
or
RETURN UNKNOWN
```

---

# 95. RSCF and Sensitivity

Identify the smallest load-bearing premise that can flip the conclusion.

Example:

```text
C depends on P1, P2, P3

P1 strong
P2 strong
P3 uncertain
```

If C changes when P3 changes:

```text
P3
```

is a sensitivity pivot.

Validation effort should prioritize P3 before collecting redundant evidence for P1.

---

# 96. RSCF and Uncertainty Vector

A consequential proof capsule may distinguish:

```yaml
uncertainty:
  evidence: string
  model: string
  scope: string
  temporal: string
  causal: string
  execution: string
  provenance_independence: string
```

This prevents one generic "confidence" number from hiding the actual uncertainty source.

---

# 97. RSCF and Failure Recovery

If premise P fails:

```text
P ✕
│
├── C1
│   └── C2
│
└── C3
```

invalidate:

```text
P
C1
C2
C3
```

only where dependency edges are load-bearing.

Independent claims remain intact.

---

# 98. Local Invalidation

Suppose:

```text
P1 → C1
P2 → C2
```

If P1 fails:

```text
C1 revalidate
```

but:

```text
C2 preserved
```

unless another edge links it to P1.

Thus:

```text
FAILURE
≠
GLOBAL RECOMPUTATION
```

---

# 99. Alternative Proof Recovery

Suppose:

```text
P1 → C
P2 → C
```

where each path independently suffices.

If P1 fails:

```text
P1 PATH INVALID
```

but C may remain established through P2.

Therefore invalidation must operate on proof paths, not only claim labels.

---

# 100. Proof Path Schema

```yaml
proof_path:

  path_id:
    PP1

  target_claim:
    C

  premises:
    - P1
    - P2

  sufficiency:
    independent |
    joint |
    partial

  conditions: []

  status:
    VALID |
    INVALID |
    CONDITIONAL |
    UNKNOWN
```

This is a proposed extension.

---

# 101. RSCF and Persistent Knowledge

A claim promoted to persistent knowledge should preserve:

```yaml
persistent_claim:

  claim_id:
    string

  proposition:
    string

  epistemic_class:
    SOURCE |
    DERIVED |
    MODEL |
    UNKNOWN

  proof_capsule_id:
    string

  provenance:
    roots: []

  dependencies: []

  scope:
    string|null

  regime:
    string|null

  freshness:
    string|null

  falsifiers: []

  revalidation_conditions: []
```

Persistent storage does not convert a claim into fact.

---

# 102. Memory Is Not Proof

```text
CLAIM STORED
≠
CLAIM VERIFIED
```

Likewise:

```text
CLAIM RETRIEVED
≠
CLAIM FRESH
```

RSCF metadata must survive persistence and retrieval.

---

# 103. Knowledge Harvest

Conceptually:

```text
EPHEMERAL OUTPUT
      ↓
PERSISTENT EVIDENCE
      ↓
VALIDATED CLAIM
      ↓
DURABLE KNOWLEDGE
```

At every transition preserve:

* provenance,
* class,
* dependencies,
* conditions,
* gaps,
* falsifiers,
* scope,
* freshness.

---

# 104. Promotion Firewall

Invalid:

```text
MODEL
 ↓
SAVE TO KNOWLEDGE BASE
 ↓
VERIFIED
```

Persistence is not validation.

Correct:

```text
MODEL
 ↓
SAVE WITH MODEL CLASS
 ↓
REVALIDATE IF NEEDED
```

---

# 105. RSCF and Versioning

A claim may change over time.

```yaml
claim:
  claim_id: C1
  version: 4
  supersedes:
    - C1_v3
```

Do not overwrite prior epistemic state when lineage matters.

---

# 106. RSCF and Epochs

Conceptually:

```text
CLAIM C @ E1
```

may have a different proof state from:

```text
CLAIM C @ E2
```

if:

* sources changed,
* governance changed,
* regime changed,
* evidence became stale,
* contradictions emerged.

Proof capsules should therefore preserve temporal validity where material.

---

# 107. RSCF and MVCC/CAS Concepts

Where AMOS uses versioned persistent state conceptually, RSCF should avoid silently finalizing a claim against stale premises.

Conceptually:

```text
READ PREMISES @ VERSION V
      ↓
DERIVE C
      ↓
PREMISES STILL @ V?
```

If no:

```text
REVALIDATE
```

This is a reasoning pattern, not a claim that the conversational system literally implements MVCC/CAS.

---

# 108. Compare-And-Validate Pattern

Semantic pseudocode:

```python
def finalize_claim(claim, snapshot):

    proof = build_capsule(claim, snapshot)

    if premises_changed(snapshot):
        return REVALIDATE

    if proof.has_critical_gap:
        return CONDITIONAL_OR_UNKNOWN

    return classify(proof)
```

---

# 109. RSCF and Atomic Multi-Claim Reasoning

A decision may require:

```text
C1
+
C2
+
C3
```

jointly.

If:

```text
C1 VERIFIED
C2 CONDITIONAL
C3 VERIFIED
```

and all are load-bearing:

```text
DECISION
```

inherits the unresolved condition from C2.

Successful claims do not erase a weak load-bearing claim.

---

# 110. Atomic Finalization

Conceptually:

```text
ALL LOAD-BEARING CLAIMS
must satisfy
THE REQUIRED PROOF CONTRACT
```

before a consequential composite conclusion finalizes.

Partial proof should remain partial.

---

# 111. RSCF and Decision Objects

Separate:

```text
CLAIM
```

from:

```text
DECISION
```

A decision may be rational under uncertainty even when underlying claims remain conditional.

Example:

```yaml
decision:
  action:
    choose_reversible_test

  basis:
    - C1: CONDITIONAL
    - C2: COMPETING

  rationale:
    highest_information_gain_with_low_irreversible_cost
```

The decision does not upgrade C1 or C2.

---

# 112. RSCF and Action Sufficiency

A proof capsule can be sufficient for one action but insufficient for another.

```text
EVIDENCE E
```

may justify:

```text
RUN REVERSIBLE TEST
```

but not:

```text
MAKE IRREVERSIBLE COMMITMENT
```

Thus action sufficiency depends on stakes as well as descriptive confidence.

---

# 113. Consequential Claim

RSCF-2 explicitly requires proof capsules for **consequential claims**.

The supplied source does not define a formal threshold for "consequential."

A proposed interpretation includes claims whose failure could materially affect:

* governance,
* irreversible action,
* safety,
* legal/financial exposure,
* large downstream dependency,
* canonical knowledge,
* major institutional decisions.

This remains an AMOS_MODEL extension.

---

# 114. Non-Consequential Claims

RSCF need not impose maximal capsule overhead on every trivial statement.

A lightweight internal capsule may suffice where:

* stakes are low,
* claim is local,
* proof is direct,
* dependencies are simple,
* no material uncertainty exists.

The source law requires consequential claims to carry capsules; it does not state that every sentence needs a maximal serialized structure.

---

# 115. Adaptive RSCF Depth

Conceptually:

```text
LOW STAKES
DIRECT PROOF
→ COMPACT RSCF

HIGH STAKES
WEAK EVIDENCE
CONTRADICTION
CAUSAL CLAIM
GOVERNANCE IMPACT
→ DEEP RSCF
```

Claim discipline remains constant while representation depth adapts.

---

# 116. Minimal RSCF Runtime

```text
CLAIM
 ↓
CLASS?
 ↓
PROOF?
 ↓
CONDITIONS?
 ↓
GAPS?
 ↓
CEILING?
 ↓
OUTPUT
```

If these questions are resolved, deeper expansion may not be necessary.

---

# 117. Escalation Triggers

Escalate RSCF depth when:

```text
CLAIM CLASS AMBIGUOUS
PROVENANCE CORRELATED
SOURCE AUTHORITY UNKNOWN
LOAD-BEARING GAP
CONTRADICTION
CONDITIONAL DEPENDENCY
CAUSAL OVERREACH RISK
SCOPE MISMATCH
REGIME SHIFT
STALE EVIDENCE
IRREVERSIBLE ACTION
GOVERNANCE IMPACT
```

---

# 118. De-Escalation

Once decision-changing uncertainty is resolved:

```text
STOP
```

Do not continue proof expansion merely because more background could be collected.

This preserves smallest-sufficient-proof behavior.

---

# 119. RSCF Claim Lifecycle

```text
PROPOSITION
   ↓
CLASSIFY
   ↓
ATTACH PROVENANCE
   ↓
IDENTIFY PREMISES
   ↓
BUILD CAPSULE
   ↓
CHECK CONDITIONS
   ↓
CHECK GAPS
   ↓
CHECK FALSIFIERS
   ↓
SET CEILING
   ↓
FINALIZE
   ↓
PERSIST IF WARRANTED
   ↓
REVALIDATE WHEN INVALIDATED
```

---

# 120. SOURCE Lifecycle

```text
SOURCE MATERIAL
   ↓
EXTRACT ASSERTION
   ↓
LABEL SOURCE
   ↓
PRESERVE ATTRIBUTION
   ↓
DO NOT UPGRADE
WITHOUT VALIDATION
```

---

# 121. DERIVED Lifecycle

```text
PREMISES
   ↓
DERIVATION RULE
   ↓
CONCLUSION
   ↓
INHERIT CONDITIONS
   ↓
INHERIT SCOPE
   ↓
SET CEILING
```

---

# 122. MODEL Lifecycle

```text
OBSERVATIONS / CLAIMS
       ↓
MODEL CONSTRUCTION
       ↓
PREDICTIONS
       ↓
DISCRIMINATING TEST
       ↓
RETAIN / REVISE / REJECT
```

Model evaluation does not erase the distinction between model and observation.

---

# 123. UNKNOWN Lifecycle

```text
QUESTION
  ↓
PROOF INSUFFICIENT
  ↓
UNKNOWN
  ↓
IDENTIFY GAP
  ↓
SEEK HIGH-VALUE DISCRIMINATOR
  ↓
RECLASSIFY ONLY IF WARRANTED
```

---

# 124. RSCF Claim Validation Algorithm

```python
def validate_claim(claim):

    cls = classify_epistemic_type(claim)

    if cls is None:
        return UNKNOWN("claim class missing")

    capsule = build_proof_capsule(claim)

    if missing_required_proof(capsule):
        capsule.gaps.append(
            identify_missing_proof(capsule)
        )

    capsule.conditions = conditional_closure(claim)

    capsule.ceiling = compute_ceiling(capsule)

    return capsule
```

Semantic pseudocode only.

---

# 125. No-Proof-No-Claim Algorithm

```python
def establish(proposition, proof):

    if proof is None:
        return {
            "class": "UNKNOWN",
            "gap": "required proof absent"
        }

    if not proof_supports(proposition):
        return {
            "class": "UNKNOWN",
            "gap": "proof does not establish proposition"
        }

    return classify_supported_claim(
        proposition,
        proof
    )
```

---

# 126. Class-Mixing Detector

```python
def detect_class_laundering(source_claim, output_claim):

    if source_claim.class == "SOURCE":
        if output_claim.asserts_source_content_as_fact_without_validation:
            return VIOLATION

    if source_claim.class == "MODEL":
        if output_claim.asserts_model_as_observation_without_validation:
            return VIOLATION

    return PASS
```

---

# 127. Conditional-Carry Algorithm

```python
def propagate_conditions(claim):

    conditions = set(claim.own_conditions)

    for parent in claim.load_bearing_parents:
        conditions.update(
            propagate_conditions(parent)
        )

    return conditions
```

A production implementation would need proof-path semantics for alternatives and cycles.

---

# 128. Confidence Ceiling Algorithm

```python
def confidence_ceiling(claim):

    ceilings = [
        premise.ceiling
        for premise in claim.load_bearing_premises
    ]

    ceilings += gap_constraints(claim)
    ceilings += provenance_constraints(claim)
    ceilings += scope_constraints(claim)
    ceilings += freshness_constraints(claim)

    return weakest_applicable_ceiling(
        ceilings
    )
```

Conceptual only.

---

# 129. Proof Capsule Validation Algorithm

```python
REQUIRED_FIELDS = {
    "claim",
    "established",
    "not_established",
    "gaps",
    "falsifiers",
    "ceiling"
}

def validate_capsule(capsule):

    missing = REQUIRED_FIELDS - capsule.keys()

    if missing:
        return {
            "status": "INVALID",
            "missing": missing
        }

    return {
        "status": "STRUCTURALLY_VALID"
    }
```

Structural validity does not establish semantic correctness.

---

# 130. Proof Capsule Integrity Invariants

```yaml
rscf_capsule_invariants:

  PCI_1_CLAIM:
    requirement:
      target_claim_is_explicit

  PCI_2_ESTABLISHED:
    requirement:
      established_contains_only_supported_content

  PCI_3_NOT_ESTABLISHED:
    requirement:
      unsupported_material_extensions_are_explicit

  PCI_4_GAPS:
    requirement:
      missing_load_bearing_proof_is_recorded

  PCI_5_FALSIFIERS:
    requirement:
      material_invalidation_conditions_are_preserved

  PCI_6_CEILING:
    requirement:
      conclusion_does_not_exceed_support

  PCI_7_CONDITIONS:
    requirement:
      inherited_conditions_are_not_dropped

  PCI_8_PROVENANCE:
    requirement:
      source_ancestry_is_preserved_when_material

  PCI_9_SCOPE:
    requirement:
      proof_scope_is_not_silently_broadened

  PCI_10_FRESHNESS:
    requirement:
      stale_load_bearing_evidence_triggers_revalidation
```

Only the first six are directly anchored to the source capsule law; the remainder are extensions.

---

# 131. RSCF Integrity Invariants

```yaml
rscf_integrity_invariants:

  RSCFI_1_CLASS:
    requirement:
      every_claim_has_explicit_epistemic_class

  RSCFI_2_NO_MIX:
    requirement:
      claim_classes_are_not_silently_mixed

  RSCFI_3_CAPSULE:
    requirement:
      consequential_claims_have_proof_capsules

  RSCFI_4_NO_PROOF:
    requirement:
      absence_of_proof_is_recorded_as_gap

  RSCFI_5_NO_FLUENT_FILL:
    requirement:
      fluent_inference_does_not_replace_missing_proof

  RSCFI_6_CONDITIONAL_CARRY:
    requirement:
      conditional_on_propagates_through_load_bearing_dependents

  RSCFI_7_CEILING:
    requirement:
      derived_claim_does_not_exceed_load_bearing_support_without_independent_revalidation

  RSCFI_8_PROVENANCE:
    requirement:
      descendants_do_not_gain_false_independence

  RSCFI_9_SCOPE:
    requirement:
      derived_claims_do_not_silently_expand_scope

  RSCFI_10_LOCAL_INVALIDATION:
    requirement:
      failed_premises_invalidate_only_dependent_proof_paths

  RSCFI_11_CONTRADICTION:
    requirement:
      genuine_competing_claims_remain_visible

  RSCFI_12_PERSISTENCE:
    requirement:
      storage_does_not_upgrade_epistemic_class
```

---

# 132. RSCF Anti-Patterns

## RSCF-A1 — Source-to-Fact Laundering

```text
SOURCE S CLAIMS X
→
X IS VERIFIED
```

without validation.

Rejected.

---

## RSCF-A2 — Model-to-Fact Laundering

```text
MODEL M EXPLAINS X
→
M IS THE ACTUAL MECHANISM
```

Rejected.

---

## RSCF-A3 — Gap Filling by Fluency

```text
EVIDENCE ENDS HERE
        ↓
PLAUSIBLE PROSE CONTINUES
        ↓
CLAIM PRESENTED AS ESTABLISHED
```

Rejected.

---

## RSCF-A4 — Dropped Condition

```text
P conditional on Q
P → C
→
C unconditional
```

Rejected.

---

## RSCF-A5 — Hidden Unknown

```text
UNKNOWN
→
OMITTED FROM SUMMARY
→
APPARENT CERTAINTY
```

Rejected.

---

## RSCF-A6 — Proof-by-Repetition

```text
ONE SOURCE
→ 20 DERIVATIVES
→ "20 SOURCES AGREE"
```

Rejected.

---

## RSCF-A7 — Average-Away Weak Premise

```text
9 STRONG PREMISES
+
1 CRITICAL UNKNOWN
→
"OVERALL HIGH CONFIDENCE"
```

Rejected when the unknown is load-bearing.

---

## RSCF-A8 — Persistence Upgrade

```text
MODEL
→ STORED
→ CANON
```

Rejected.

---

## RSCF-A9 — Scope Laundering

```text
VALID IN A
→
VALID EVERYWHERE
```

Rejected.

---

## RSCF-A10 — Temporal Laundering

```text
VALID @ E1
→
VALID FOREVER
```

Rejected.

---

## RSCF-A11 — Contradiction Erasure

```text
C1: X
C2: NOT X
→
SYNTHESIS: "probably X"
```

without discriminating evidence.

Rejected.

---

## RSCF-A12 — Circular Validation

```text
MODEL M
uses
MODEL M
to prove
MODEL M
```

Rejected as independent validation.

---

# 133. Proof vs Explanation

An explanation may improve comprehension without increasing proof strength.

```text
BETTER EXPLANATION
≠
STRONGER EVIDENCE
```

Therefore prose quality must not influence claim classification.

---

# 134. Proof vs Computation

A deterministic calculation can establish the result of that calculation given its inputs.

It does not establish that the inputs themselves are true.

```text
INPUT CLAIMS
   ↓
CORRECT CALCULATION
   ↓
CORRECT CONDITIONAL RESULT
```

The result remains conditional on input validity.

---

# 135. Proof vs Simulation

A simulation can establish:

```text
MODEL M
produces outcome X
under parameters P
```

It does not by itself establish:

```text
REAL SYSTEM
will produce X
```

The model-to-reality bridge remains separately load-bearing.

---

# 136. Proof vs Benchmark

A benchmark may establish performance:

```text
UNDER BENCHMARK B
```

It does not automatically establish:

```text
UNIVERSAL PERFORMANCE
```

Scope must carry through the proof capsule.

---

# 137. Proof vs Formal Proof

If an artifact reports:

```text
"formally proven"
```

that remains a SOURCE claim until the proof or trusted validation establishes the assertion.

Documentation language does not automatically become proof status.

---

# 138. RSCF and Canonical Documents

A canonical document may be authoritative regarding what AMOS canon declares.

That does not automatically make every empirical proposition inside it externally verified.

Therefore distinguish:

```text
CANONICALLY VERIFIED:
AMOS canon states X

EMPIRICALLY VERIFIED:
X corresponds to external reality
```

These are different claims.

---

# 139. Corpus Model vs Empirical Claim

For AMOS corpus material:

```text
AMOS_MODEL
```

should remain distinct from:

```text
VERIFIED_EMPIRICAL_CLAIM
```

unless external validation exists.

This prevents architectural canon from being misrepresented as empirical science.

---

# 140. RSCF and Canon Authority

A canonical source may raise confidence about:

```text
WHAT THE CANON DEFINES
```

but not necessarily about:

```text
WHETHER THE DEFINED MODEL IS TRUE OF REALITY
```

RSCF must preserve that boundary.

---

# 141. RSCF and Recursive Reasoning

A derived claim may itself become a premise:

```text
SOURCE S
   ↓
D1
   ↓
D2
   ↓
D3
```

At every step preserve:

* class,
* conditions,
* provenance,
* scope,
* ceiling.

Recursive depth does not wash away ancestry.

---

# 142. Recursive Confidence

Conceptually:

```text
D3
cannot exceed
the weakest unresolved
load-bearing dependency
in its proof ancestry
```

unless an independent proof path revalidates D3.

---

# 143. Recursive Conditional Carry

```text
Q
↓
D1
↓
D2
↓
D3
```

If Q is load-bearing throughout:

```text
D1 conditional on Q
D2 conditional on Q
D3 conditional on Q
```

The condition must survive arbitrary derivation depth.

---

# 144. Recursive Provenance

```text
D3
```

must still permit reconstruction to:

```text
SOURCE ROOTS
```

when provenance is material.

A long derivation chain does not create independent evidence.

---

# 145. RSCF and Fractal Retrieval

The smallest sufficient proof should retrieve:

```text
BOOTSTRAP
 ↓
RELEVANT DOMAIN
 ↓
RELEVANT SUBSYSTEM
 ↓
RELEVANT DETAIL
 ↓
RAW EVIDENCE ONLY IF REQUIRED
```

RSCF determines when lower-level evidence is necessary to close a proof gap.

Raw evidence should not be loaded merely for completeness.

---

# 146. Proof-Driven Retrieval

```text
CLAIM C
 ↓
WHAT PREMISE CAN FLIP C?
 ↓
WHAT EVIDENCE RESOLVES THAT PREMISE?
 ↓
RETRIEVE ONLY THAT PATH
```

This minimizes irrelevant context while preserving integrity.

---

# 147. RSCF Stop Rule

Stop retrieval when:

```text
CLAIM SUFFICIENCY
+
DECISION SUFFICIENCY
+
ACTION SUFFICIENCY
```

are achieved.

Do not seek exhaustive proof when additional evidence cannot change the conclusion or action.

---

# 148. RSCF and Governance

Higher-stakes claims require stronger proof discipline.

Consequentiality may increase when claims affect:

* core laws,
* persistent canon,
* irreversible action,
* institutional decisions,
* legal/financial exposure,
* safety,
* large dependency graphs.

This affects proof depth, not the fundamental class contract.

---

# 149. RSCF Governance Mutation

Before changing a high-impact canonical claim:

```text
TARGET CLAIM
 ↓
CURRENT CAPSULE
 ↓
DEPENDENT CLAIMS
 ↓
PROPOSED CHANGE
 ↓
CONTRADICTION CHECK
 ↓
IMPACT SET
 ↓
VALIDATE
 ↓
COMMIT OR REJECT
```

This is a proposed operational extension.

---

# 150. Dependent Revalidation

When a canonical claim changes:

```text
C_old
↓
C_new
```

all descendants that materially depend on the changed proposition should be marked for revalidation.

Independent descendants remain intact.

---

# 151. RSCF Transactional Finalization

Conceptually:

```text
READ CLAIM GRAPH
      ↓
BUILD CAPSULE
      ↓
VALIDATE
      ↓
CHECK DEPENDENCIES UNCHANGED
      ↓
FINALIZE
```

If load-bearing state changes before finalization:

```text
ABORT STALE FINALIZATION
→
REVALIDATE
```

Again, this is a reasoning pattern, not a literal claim about runtime implementation.

---

# 152. RSCF Proof-Path Independence

Two proof paths:

```text
S1 → D1 → C
S2 → D2 → C
```

are independent only if relevant provenance ancestry is sufficiently independent.

If:

```text
S1 ← ROOT R → S2
```

then apparent independence may be false.

Therefore independence is a claim requiring proof.

---

# 153. Independent Revalidation

A conditional or weak claim can escape its inherited ceiling only through a proof path that does not depend on the weak premise.

```text
P weak
 ↓
C weak
```

plus:

```text
E independent
 ↓
C strongly supported
```

may permit C to be upgraded.

But E must be genuinely independent and applicable to the same claim/scope.

---

# 154. RSCF Proof Topology

```text
         S1
        /  \
      D1    D2
       \    /
         C
```

This is one ancestral source topology.

Contrast:

```text
S1 → D1 ─┐
         ├→ C
S2 → D2 ─┘
```

where S1 and S2 may be independent.

RSCF confidence should respond to topology, not raw edge count.

---

# 155. RSCF and Negative Claims

A negative claim:

```text
X does not exist
```

requires evidence capable of supporting absence within a defined search scope.

Failure to find X is not automatically proof of universal nonexistence.

Proof capsules should state the search envelope.

---

# 156. RSCF and Universal Claims

Universal claims have demanding scope.

```text
FOR ALL X
P(X)
```

cannot generally be established from:

```text
P(a)
P(b)
P(c)
```

without a valid generalization rule.

The missing bridge must remain explicit.

---

# 157. RSCF and Existential Claims

An existential claim:

```text
THERE EXISTS X SUCH THAT P(X)
```

may be established by one valid witness.

But the witness must itself be established and within the intended scope.

---

# 158. RSCF and Quantitative Claims

A quantitative claim should preserve:

* units,
* measurement method,
* uncertainty,
* sample,
* time,
* environment,

where load-bearing.

A bare number without its applicability envelope risks false precision.

---

# 159. RSCF and Threshold Decisions

Suppose action A occurs if:

```text
X > T
```

Then the highest-value validation target may be whether X is near threshold T.

If:

```text
X ≫ T
```

minor uncertainty may not matter.

If:

```text
X ≈ T
```

small uncertainty can flip the action.

RSCF sensitivity should prioritize threshold-adjacent uncertainty.

---

# 160. RSCF and Falsification

A strong proof capsule should make clear:

```text
WHAT WOULD CHANGE THIS CONCLUSION?
```

If no possible evidence could alter a model claim, the claim may be unfalsifiable within its stated formulation.

RSCF should mark that limitation rather than treating resistance to falsification as strength.

---

# 161. Falsifier Status

```yaml
falsifier:
  id: F1
  condition: string
  status:
    NOT_TESTED |
    NOT_OBSERVED |
    OBSERVED |
    INAPPLICABLE
```

If observed:

```text
CLAIM
→ REVALIDATE
```

not necessarily:

```text
CLAIM
→ FALSE
```

unless the falsifier is logically decisive.

---

# 162. Not-Established Registry

A consequential system may maintain:

```yaml
not_established_registry:

  claim_id:
    C1

  propositions:
    - P1
    - P2

  reasons:
    - missing_evidence
    - scope_not_validated
```

This prevents later summaries from forgetting proof boundaries.

---

# 163. Gap Registry

```yaml
gap_registry:

  - gap_id: G1
    claim_id: C1
    severity: CRITICAL
    missing: string
    cheapest_discriminator: string|null
    status:
      OPEN |
      RESOLVED |
      SUPERSEDED
```

This is a proposed extension.

---

# 164. Condition Registry

```yaml
condition_registry:

  - condition_id: Q1
    proposition: string
    status:
      VERIFIED |
      FALSE |
      UNKNOWN |
      CONDITIONAL

    dependents:
      - C1
      - C2
```

This supports selective invalidation and discharge.

---

# 165. Claim Registry

```yaml
claim_registry:

  - claim_id: C1

    proposition:
      string

    epistemic_class:
      SOURCE |
      DERIVED |
      MODEL |
      UNKNOWN

    claim_status:
      VERIFIED |
      CONDITIONAL |
      COMPETING |
      UNKNOWN

    proof_capsule:
      PC1

    dependencies: []

    conditional_on: []

    provenance:
      roots: []

    scope:
      string|null

    epoch:
      string|null
```

---

# 166. RSCF Serialization Contract

A compact serialization may be:

```yaml
rscf:

  claim:
    id: C1
    text: string

  class:
    SOURCE |
    DERIVED |
    MODEL |
    UNKNOWN

  established: []

  not_established: []

  gaps: []

  falsifiers: []

  ceiling:
    string

  conditional_on: []

  dependencies: []

  provenance:
    roots: []

  scope:
    string|null
```

Only the class contract and six proof-capsule fields are source-required in the supplied L17 text.

---

# 167. RSCF Minimal Serialization

```yaml
rscf:
  class: MODEL

  capsule:
    claim:
      string

    established: []

    not_established: []

    gaps: []

    falsifiers: []

    ceiling:
      CONDITIONAL
```

This satisfies the conceptual minimum more directly.

---

# 168. RSCF Validation Contract

```yaml
rscf_validation_contract:

  claim_class:
    explicit: true|false

  class_mixing:
    detected: true|false

  proof_capsule:
    required: true|false
    present: true|false

  missing_proof:
    recorded_as_gap: true|false

  conditional_carry:
    complete: true|false

  ceiling:
    respected: true|false

  result:
    PASS |
    FAIL |
    CONDITIONAL |
    UNKNOWN
```

---

# 169. RSCF Compliance Matrix

| Requirement                 | Source Law    | Failure                      |
| --------------------------- | ------------- | ---------------------------- |
| Explicit claim class        | RSCF-1        | class ambiguity              |
| No silent class mixing      | RSCF-1        | epistemic laundering         |
| Consequential claim capsule | RSCF-2        | proof boundary lost          |
| `claim` field               | RSCF-2        | target ambiguity             |
| `established` field         | RSCF-2        | support unclear              |
| `not_established` field     | RSCF-2        | unsupported implication risk |
| `gaps` field                | RSCF-2/RSCF-3 | missing evidence hidden      |
| `falsifiers` field          | RSCF-2        | claim difficult to challenge |
| `ceiling` field             | RSCF-2        | overclaim risk               |
| Missing proof remains gap   | RSCF-3        | fabrication                  |
| Conditions propagate        | RSCF-4        | false unconditionality       |

---

# 170. RSCF Self-Application

L17 itself is:

```yaml
L17:
  epistemic_class: AMOS_MODEL
  canonical_status: CONDITIONAL
  specification_status: PROPOSED_SPECIFICATION
```

Therefore this expanded L17 must not represent its proposed extensions as recovered authoritative canon.

Its own proof capsule must distinguish:

```text
ESTABLISHED FROM PROVIDED SOURCE
```

from:

```text
MODEL EXTENSION
```

---

# 171. L17 Source-Established Content

From the supplied L17 source, the following are directly established as corpus claims:

```text
1. L17 is a proposed specification.
2. Its epistemic class is AMOS_MODEL.
3. Its canonical status is CONDITIONAL.
4. RSCF-1 defines SOURCE / DERIVED / MODEL / UNKNOWN.
5. Silent class mixing is a violation.
6. Consequential claims carry a capsule containing:
   claim,
   established,
   not_established,
   gaps,
   falsifiers,
   ceiling.
7. Absence of proof is recorded as a gap.
8. Fluent inference must not fill missing proof.
9. CONDITIONAL-ON propagates through dependents.
10. Authoritative RSCF suite v6+ with materially different taxonomy falsifies this proposal.
```

These are `SOURCE` claims about the supplied AMOS corpus note.

---

# 172. L17 Not Established by Source

The supplied source does **not** itself establish:

* exact semantics of SOURCE versus SOURCE_CLAIM,
* complete RSCF v6+ taxonomy,
* formal proof-path algorithms,
* exact confidence ordering,
* exact gap severity taxonomy,
* exact provenance edge taxonomy,
* exact condition algebra,
* exact scope schema,
* exact persistence schema,
* exact concurrency implementation,
* exact MVCC/CAS implementation,
* exact mapping to H/M/L,
* exact canonical threshold for "consequential,"
* exact canonical claim-status cross-product.

Those remain model extensions or gaps.

---

# 173. L17 Self-Proof Capsule

```yaml
proof_capsule:

  claim:
    >
      L17 proposes an RSCF claim discipline based on explicit
      SOURCE/DERIVED/MODEL/UNKNOWN typing, proof capsules for
      consequential claims, no-proof-no-claim discipline, and
      transitive conditional carry.

  established:
    - source_note_explicitly_states_RSCF_1
    - source_note_explicitly_states_RSCF_2
    - source_note_explicitly_states_RSCF_3
    - source_note_explicitly_states_RSCF_4
    - source_note_marks_specification_as_PROPOSED
    - source_note_marks_epistemic_class_as_AMOS_MODEL
    - source_note_marks_canonical_status_as_CONDITIONAL

  not_established:
    - complete_authoritative_RSCF_v6_plus_semantics
    - exact_SOURCE_to_SOURCE_CLAIM_mapping
    - exact_formal_dependency_algebra
    - exact_condition_algebra
    - exact_gap_taxonomy
    - exact_runtime_implementation

  gaps:
    - authoritative_RSCF_v6_plus_suite_not_supplied
    - formal_claim_taxonomy_beyond_four_source_classes_not_supplied
    - canonical_proof_capsule_extension_fields_not_supplied

  falsifiers:
    - authoritative_RSCF_suite_v6_plus_defines_materially_different_claim_taxonomy

  ceiling:
    CONDITIONAL
```

---

# 174. No Circular Self-Validation

L17 cannot become authoritative by applying its own RSCF discipline to itself.

Invalid:

```text
L17 DEFINES RSCF
      ↓
RSCF CAPSULE SAYS L17 IS VALID
      ↓
L17 IS CANON
```

Correct:

```text
L17 DEFINES PROPOSED RSCF
      ↓
RSCF EXPOSES ITS SUPPORT + GAPS
      ↓
L17 REMAINS CONDITIONAL
UNTIL EXTERNAL CANONICAL AUTHORITY RESOLVES IT
```

---

# 175. Falsifier F1

Original falsifier:

> **authoritative RSCF suite v6+ defines materially different claim taxonomy.**

Operationally:

```text
RECOVER AUTHORITATIVE
RSCF v6+
      ↓
COMPARE TAXONOMY
      ↓
MATERIAL DIFFERENCE?
 ├── NO
 │    ↓
 │ preserve L17
 │
 └── YES
      ↓
invalidate affected rules
      ↓
reclassify dependent claims
      ↓
rebuild affected capsules
```

---

# 176. Material Taxonomy Difference

A material difference may include authoritative canon establishing that:

* SOURCE / DERIVED / MODEL / UNKNOWN are not the governing classes,
* one or more classes have materially different semantics,
* class mixing is governed differently,
* additional mandatory classes change the four-class contract,
* UNKNOWN is represented differently in a way that alters propagation,
* DERIVED or MODEL have different proof semantics.

The precise threshold for "materially different" is itself not defined by the source.

---

# 177. Additional Invalidation Conditions

The expanded model should also be reconsidered if authoritative canon defines materially different:

* proof capsule fields,
* conditional propagation semantics,
* confidence ceilings,
* provenance independence rules,
* scope inheritance,
* proof-path invalidation,
* persistent knowledge semantics,
* H/M/L integration.

These are derived invalidation conditions for the expansion, not additional source falsifiers.

---

# 178. Known Gaps

```yaml
gaps:

  G1:
    severity: CRITICAL
    description:
      >
        Authoritative RSCF suite v6+ is not supplied, so the
        proposed four-class taxonomy cannot be treated as final canon.

  G2:
    severity: DECISION_RELEVANT
    description:
      >
        Exact relationship between SOURCE and existing
        SOURCE_CLAIM terminology is not established.

  G3:
    severity: DECISION_RELEVANT
    description:
      >
        Exact canonical semantics of confidence ceiling are not supplied.

  G4:
    severity: DECISION_RELEVANT
    description:
      >
        Exact logic for CONDITIONAL-ON propagation across alternative
        proof paths is not supplied.

  G5:
    severity: DECISION_RELEVANT
    description:
      >
        Exact canonical definition of a consequential claim is absent.

  G6:
    severity: EXPLANATORY
    description:
      >
        Exact provenance-edge taxonomy is not supplied.

  G7:
    severity: EXPLANATORY
    description:
      >
        Exact scope and regime serialization for RSCF capsules is not supplied.

  G8:
    severity: EXPLANATORY
    description:
      >
        Exact mapping between RSCF claim classes and broader AMOS
        conclusion classes is not supplied.

  G9:
    severity: EXPLANATORY
    description:
      >
        Exact persistent storage/versioning representation is not supplied.

  G10:
    severity: EXPLANATORY
    description:
      >
        Exact relationship between RSCF and H/M/L canonical semantics
        is not defined by this source.
```

---

# 179. RSCF Claim Graph for L17

```yaml
claim_graph:

  RSCF_C001:
    class: SOURCE
    claim:
      Every claim is SOURCE, DERIVED, MODEL, or UNKNOWN.

  RSCF_C002:
    class: SOURCE
    claim:
      Silently mixing those classes is a violation.

  RSCF_C003:
    class: SOURCE
    claim:
      Consequential claims carry proof capsules.

  RSCF_C004:
    class: SOURCE
    claim:
      >
        The source-defined capsule contains claim, established,
        not_established, gaps, falsifiers, and ceiling.

  RSCF_C005:
    class: SOURCE
    claim:
      Absence of proof is recorded as a gap.

  RSCF_C006:
    class: SOURCE
    claim:
      Missing proof must not be filled by fluent inference.

  RSCF_C007:
    class: SOURCE
    claim:
      CONDITIONAL-ON propagates through dependents.

  RSCF_C008:
    class: DERIVED
    claim:
      >
        A derived claim cannot silently drop a load-bearing condition
        inherited from a premise.

  RSCF_C009:
    class: DERIVED
    claim:
      >
        A missing load-bearing logical bridge must itself be represented
        as a proof gap.

  RSCF_C010:
    class: MODEL
    claim:
      >
        Proof capsules can be represented as reusable provenance-aware
        graph objects.

  RSCF_C011:
    class: MODEL
    claim:
      >
        Conditional carry should preserve logical structure across
        conjunctive and alternative proof paths.

  RSCF_C012:
    class: MODEL
    claim:
      >
        Persistent RSCF claims should preserve version, scope,
        provenance, dependencies, and revalidation conditions.

  RSCF_C013:
    class: UNKNOWN
    claim:
      >
        Whether authoritative RSCF v6+ uses the exact four-class
        taxonomy supplied here.
```

---

# 180. RSCF Dependency Graph

```yaml
dependency_graph:

  RSCF_1:
    depends_on:
      - claim_identity
      - epistemic_class_assignment

  RSCF_2:
    depends_on:
      - consequentiality
      - target_claim
      - proof_state

  RSCF_3:
    depends_on:
      - required_proof_definition
      - available_evidence
      - gap_representation

  RSCF_4:
    depends_on:
      - dependency_edges
      - condition_identity
      - load_bearing_status
```

---

# 181. Unified RSCF Architecture

```text
                    CLAIM
                      │
                      ▼
             ┌────────────────┐
             │ CLASS CONTRACT │
             └───────┬────────┘
                     ↓
       SOURCE / DERIVED / MODEL / UNKNOWN
                     ↓
             LOAD-BEARING PREMISES
                     ↓
             ┌────────────────┐
             │ PROOF CAPSULE  │
             └───────┬────────┘
                     ↓
        ┌────────────┼────────────┐
        ↓            ↓            ↓
  ESTABLISHED   NOT ESTABLISHED   GAPS
        │            │            │
        └────────────┼────────────┘
                     ↓
                 FALSIFIERS
                     ↓
             CONDITIONAL CARRY
                     ↓
                  CEILING
                     ↓
              CLAIM FINALIZATION
```

---

# 182. Four-Class Operational Contract

```yaml
four_class_contract:

  SOURCE:
    establishes:
      what_a_source_asserts

    does_not_automatically_establish:
      truth_of_the_assertion

  DERIVED:
    establishes:
      what_follows_from_identified_premises_and_valid_derivation

    inherits:
      - conditions
      - scope_constraints
      - confidence_constraints

  MODEL:
    establishes:
      a_proposed_representation_or_explanation

    does_not_automatically_establish:
      empirical_truth_or_causality

  UNKNOWN:
    establishes:
      that_required_support_is_currently_insufficient_or_unresolved

    must_not_be_replaced_by:
      fluent_completion
```

Only the four class names and prohibition on silent mixing are directly source-defined; these operational descriptions are proposed elaborations.

---

# 183. Proof Capsule Operational Contract

```yaml
proof_capsule_contract:

  claim:
    purpose:
      identify_target_proposition

  established:
    purpose:
      record_what_current_proof_supports

  not_established:
    purpose:
      mark_unsupported_extensions

  gaps:
    purpose:
      record_missing_proof

  falsifiers:
    purpose:
      identify_invalidation_conditions

  ceiling:
    purpose:
      bound_maximum_claim_strength
```

---

# 184. RSCF Canonical Compression

```text
EVERY CLAIM
HAS A CLASS:

SOURCE
DERIVED
MODEL
UNKNOWN
```

Then:

```text
CONSEQUENTIAL CLAIM
→
PROOF CAPSULE
```

containing:

```text
CLAIM
ESTABLISHED
NOT ESTABLISHED
GAPS
FALSIFIERS
CEILING
```

And:

```text
NO PROOF
→
GAP
```

never:

```text
NO PROOF
→
FLUENT COMPLETION
```

Finally:

```text
CONDITIONAL-ON Q
PROPAGATES
THROUGH EVERY
LOAD-BEARING DEPENDENT
```

until Q is discharged or the dependent is independently revalidated.

---

# 185. Canonical One-Line Law

> **AMOS RSCF requires every claim to preserve its epistemic class, every consequential claim to carry an explicit proof capsule, every missing proof to remain an explicit gap rather than being filled by fluent inference, and every load-bearing condition to propagate through dependent claims until independently discharged.**

---

# 186. Canonical Equations

Class contract:

```text
Class(C)
∈
{
SOURCE,
DERIVED,
MODEL,
UNKNOWN
}
```

No-proof-no-claim:

```text
RequiredProof(C) = ∅
or
RequiredProof(C) insufficient

⇒

Established(C) = FALSE
```

and:

```text
MissingProof(C)
⇒
Gap(C)
```

Conditional carry:

```text
P → C
and
P CONDITIONAL-ON Q

⇒

C CONDITIONAL-ON Q
```

when P is load-bearing and no independent proof discharges Q.

Confidence ceiling:

```text
STRENGTH(C)
≤
CEILING(C)
```

and conceptually:

```text
CEILING(C)
≤
WEAKEST UNRESOLVED
LOAD-BEARING PREMISE
```

unless independently revalidated.

---

# 187. RSCF Final Proof Capsule

```yaml
proof_capsule:

  claim:
    class: CONDITIONAL
    text:
      >
        AMOS L17 proposes RSCF as a claim-discipline system in
        which claims are explicitly typed SOURCE, DERIVED, MODEL,
        or UNKNOWN; consequential claims carry proof capsules;
        missing proof remains an explicit gap; and CONDITIONAL-ON
        dependencies propagate through load-bearing descendants.

  established:
    - four_source_claim_classes_are_explicitly_listed
    - silent_class_mixing_is_explicitly_prohibited
    - consequential_claim_capsule_is_explicitly_required
    - six_capsule_fields_are_explicitly_listed
    - no_proof_no_claim_rule_is_explicit
    - conditional_carry_rule_is_explicit

  not_established:
    - authoritative_RSCF_v6_plus_taxonomy
    - exact_SOURCE_SOURCE_CLAIM_equivalence
    - exact_condition_algebra
    - exact_proof_path_runtime
    - exact_confidence_ceiling_algorithm
    - exact_persistent_storage_schema
    - exact_HML_RSCF_mapping

  gaps:
    - authoritative_RSCF_v6_plus_suite
    - formal_taxonomy_specification
    - formal_conditional_propagation_specification
    - canonical_consequentiality_threshold

  falsifiers:
    - authoritative_RSCF_suite_v6_plus_defines_materially_different_claim_taxonomy

  ceiling:
    CONDITIONAL

  epistemic_class:
    AMOS_MODEL

  canonical_status:
    CONDITIONAL

  specification_status:
    PROPOSED_SPECIFICATION
```

---

# 188. RSCF Node

```yaml
RSCF-NODE:

  node_id:
    l17_rscf

  node_type:
    note

  path:
    01_CANON/01_CORE_LAWS/L17_RSCF.md

  epistemic_class:
    AMOS_MODEL

  claim_class:
    CONDITIONAL

  canonical_status:
    CONDITIONAL

  specification_status:
    PROPOSED_SPECIFICATION

RSCF-RELATIONS:

  - INDEXED_BY: [[00_HOME]]

  - INDEXED_BY: [[AMOS_RSCF_NODES]]

  - CHILD_OF: [[LAW_HIERARCHY]]

  - MEMBER_OF: [[01_CORE_LAWS_MOC]]

  - RELATED_TO: [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

  - RELATED_TO: [[AMOS_CORE_ALL_VERSIONS_FRACTAL_KNOWLEDGE_NETWORK]]

  - RELATED_TO: [[L16_HML]]

  - RELATED_TO: [[GMEF]]

  - RELATED_TO: [[PROVENANCE_TOPOLOGY]]

  - RELATED_TO: [[COMPETING_HYPOTHESES]]

  - RELATED_TO: [[SCOPE_REGIME_FIREWALL]]

  - RELATED_TO: [[CAUSAL_FIREWALL]]

  - RELATED_TO: [[L10_FAILURE_RECOVERY]]

  - RELATED_TO: [[L11_KNOWLEDGE_MEMORY]]

  - RELATED_TO: [[L15_FRACTAL_KNOWLEDGE]]
```

---

**00_ROOT_MOC:** [[AMOS MOC]]

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]]

**MOC:** [[01_CORE_LAWS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---

# 189. L17 Final Invariant

```text
EVERY CLAIM
DECLARES ITS CLASS

       ↓

SOURCE
DERIVED
MODEL
UNKNOWN

       ↓

CONSEQUENTIAL?
       │
       └── YES
            ↓
       PROOF CAPSULE

       ↓

SEPARATE
ESTABLISHED
FROM
NOT ESTABLISHED

       ↓

MISSING PROOF
BECOMES GAP

       ↓

NEVER FILL GAP
WITH FLUENCY

       ↓

PROPAGATE
CONDITIONAL-ON

       ↓

RESPECT
CONFIDENCE CEILING

       ↓

CLASSIFY
WITHOUT LAUNDERING
```

The compact operational law is:

```text
CLASS
→ PROVE
→ BOUND
→ CARRY CONDITIONS
→ PRESERVE GAPS
→ CLASSIFY
```

with the hard firewalls:

```text
SOURCE CLAIM
≠
TRUTH

DERIVED
≠
INDEPENDENT EVIDENCE

MODEL
≠
OBSERVATION

UNKNOWN
≠
PERMISSION TO GUESS

PLAUSIBILITY
≠
PROOF

FLUENCY
≠
EVIDENCE

REPETITION
≠
INDEPENDENT CONFIRMATION

STORAGE
≠
VALIDATION

SCOPE-SPECIFIC PROOF
≠
UNIVERSAL PROOF

CORRELATION
≠
CAUSATION

CONDITIONAL PREMISE
≠
UNCONDITIONAL DESCENDANT

FAILED PROOF PATH
≠
GLOBAL INVALIDATION

CANONICAL MODEL
≠
VERIFIED EMPIRICAL REALITY
```

**Conclusion class: CONDITIONAL / AMOS_MODEL.**

```
