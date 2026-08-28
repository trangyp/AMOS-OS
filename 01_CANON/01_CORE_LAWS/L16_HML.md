---
title: L16 HML
type: note
source: 01_CANON/01_CORE_LAWS
tags:
  - canon
  - core_laws
  - hml
  - three_speed_lens
  - governance
  - domain_policy
  - mechanical_checks
  - strictness_inheritance
  - level_assignment
  - no_level_skipping
  - epistemic_governance
  - canon/universe
rscf:
  state: SOURCE_CLAIM
  claim_class: CONDITIONAL
  provenance: AMOS_corpus
  scope: core_laws
  canonical_status: CONDITIONAL
  specification_status: PROPOSED_SPECIFICATION
  node_id: l16_hml
  node_type: note
---

# L16 H/M/L Lens Laws

**STATUS:** PROPOSED_SPECIFICATION  
**epistemic_class:** AMOS_MODEL  
**canonical_status:** CONDITIONAL  
**updated:** 2026-08-26

---

# 0. Status

L16 defines the proposed AMOS **H/M/L Three-Speed Lens** for assigning validation rigor to claims, artifacts, transformations, decisions, and execution paths.

It replaces the prior placeholder with a structured specification governing:

- High-level governance and constitutional reasoning,
- Medium-level domain policy,
- Low-level mechanical checks,
- explicit H/M/L assignment,
- strictness inheritance,
- prevention of level skipping,
- validation sufficiency,
- dependency-aware escalation,
- cross-level transformations,
- provenance preservation,
- claim confidence ceilings,
- scope and regime compatibility,
- local versus global validation,
- irreversible-action escalation,
- failure recovery,
- H/M/L interaction with RSCF,
- H/M/L interaction with proof capsules,
- H/M/L interaction with the AMOS Fractal Knowledge Network.

L16 remains:

```text
PROPOSED_SPECIFICATION
        │
        ▼
    AMOS_MODEL
        │
        ▼
    CONDITIONAL

until authoritative HML canon validates, modifies, supersedes, or rejects these semantics.

The four source laws are:

```text
HML-1 THREE-SPEED LENS
HML-2 STRICTNESS INHERITANCE
HML-3 NO LEVEL SKIPPING
HML-4 EXPLICIT ASSIGNMENT
```

The central invariant is:

```text
THE REQUIRED RIGOR OF AN OUTPUT
MUST NEVER BE LOWER
THAN THE STRICTEST LOAD-BEARING REQUIREMENT
OF ITS VALIDATION PATH.
```

---

# 1. Governing Objective

H/M/L exists to prevent a common reasoning failure:

```text
CHEAP CHECK
    ↓
LOCAL SUCCESS
    ↓
UNJUSTIFIED GLOBAL CLAIM
```

AMOS instead distinguishes three validation speeds:

```text
HIGH
governance / constitution
        │
        ▼
MEDIUM
domain policy
        │
        ▼
LOW
mechanical checks
```

These levels represent **rigor/applicability classes**, not literal processor speeds.

They determine:

* what must be validated,
* how much evidence is required,
* what dependencies must be traversed,
* what authority is necessary,
* what provenance must be preserved,
* what conflicts trigger escalation,
* what shortcuts are permitted,
* what conclusion classes are available.

---

# 2. Core H/M/L Laws

```text
HML-1
THREE-SPEED LENS

HML-2
STRICTNESS INHERITANCE

HML-3
NO LEVEL SKIPPING

HML-4
EXPLICIT ASSIGNMENT
```

Unified:

```text
ARTIFACT / CLAIM / DECISION
          ↓
DECLARE H/M/L
          ↓
DISCOVER DEPENDENCIES
          ↓
FIND STRICTEST APPLICABLE LEVEL
          ↓
RUN SUFFICIENT VALIDATION
          ↓
CHECK FOR LEVEL SKIPPING
          ↓
CLASSIFY RESULT
```

---

# 3. HML-1 — Three-Speed Lens

**Law**

High, Medium, and Low apply distinct rigor.

The source defines:

```text
H = governance / constitution
M = domain policy
L = mechanical checks
```

These descriptions establish the canonical semantic anchors of the proposed specification.

---

# 4. High Level — H

High is the governance/constitutional lens.

```yaml
H:
  semantic_anchor:
    - governance
    - constitution
```

H applies when a claim or artifact can determine or modify system-level authority, governing constraints, foundational invariants, or other constitution-like rules.

Typical conceptual examples include:

* core laws,
* authority hierarchy,
* governance rules,
* canonical invariants,
* epistemic constitutions,
* irreversible governance changes,
* cross-domain rules with broad downstream impact.

These examples are extensions of the source semantic anchor and remain `AMOS_MODEL` unless separately canonicalized.

---

# 5. H-Level Character

Conceptually:

```text
H
=
FOUNDATIONAL
+
GOVERNANCE-SENSITIVE
+
HIGH DOWNSTREAM DEPENDENCY
+
HIGH VALIDATION RIGOR
```

An H-level conclusion may influence many M- and L-level descendants.

Therefore errors at H can propagate broadly.

```text
H ERROR
  │
  ├── M1 ERROR
  │     ├── L1
  │     └── L2
  │
  ├── M2 ERROR
  └── M3 ERROR
```

This justifies stronger validation before H-level mutation or acceptance.

---

# 6. Medium Level — M

Medium is the domain-policy lens.

```yaml
M:
  semantic_anchor:
    - domain_policy
```

M applies to rules, policies, interpretations, models, or operational decisions whose authority is bounded to a defined domain.

Conceptually:

```text
H GOVERNANCE
     ↓
M DOMAIN POLICY
     ↓
L MECHANICAL EXECUTION
```

Examples may include:

* domain-specific validation rules,
* subsystem policies,
* application-specific constraints,
* domain operating procedures,
* bounded model-selection policies.

These examples remain extensions rather than recovered authoritative canon.

---

# 7. M-Level Character

Conceptually:

```text
M
=
DOMAIN-BOUNDED
+
POLICY-SENSITIVE
+
CONTEXTUAL
+
SUBORDINATE TO APPLICABLE H
```

M may specialize H but cannot silently override H.

```text
H CONSTRAINT
     ↓
M SPECIALIZATION
```

is allowed when compatible.

```text
H CONSTRAINT
     ↓
M CONTRADICTION
```

requires escalation rather than silent acceptance.

---

# 8. Low Level — L

Low is the mechanical-check lens.

```yaml
L:
  semantic_anchor:
    - mechanical_checks
```

L applies to deterministic, local, bounded checks whose result does not by itself establish broader governance or policy claims.

Examples may include:

* schema validation,
* hash equality,
* type checks,
* syntax checks,
* deterministic arithmetic,
* local constraint verification,
* exact-format validation,
* mechanical consistency checks.

These are representative extensions, not an exhaustive recovered L taxonomy.

---

# 9. L-Level Character

Conceptually:

```text
L
=
LOCAL
+
MECHANICAL
+
BOUNDED
+
CHEAP
+
REPEATABLE
```

where applicable.

However:

```text
L SUCCESS
```

does not imply:

```text
M POLICY VALIDITY
```

and does not imply:

```text
H GOVERNANCE VALIDITY
```

This is enforced by HML-3.

---

# 10. H/M/L Are Not Truth Classes

H, M, and L do not directly mean:

```text
TRUE
PROBABLY TRUE
FALSE
```

They describe validation applicability/rigor.

Thus:

```yaml
artifact:
  hml_level: H
  claim_class: CONDITIONAL
```

is valid.

Likewise:

```yaml
artifact:
  hml_level: L
  claim_class: VERIFIED
```

may be valid for a bounded deterministic check.

Therefore:

```text
H/M/L
≠
CLAIM CLASS
```

---

# 11. H/M/L Are Not Confidence Scores

Do not interpret:

```text
H > M > L
```

as:

```text
confidence(H) > confidence(M) > confidence(L)
```

An L mechanical check may have very high certainty within its narrow scope.

An H constitutional model may remain conditional.

The levels concern required rigor and applicability, not numerical confidence.

---

# 12. H/M/L Are Not Importance Labels

An L-level check can be operationally critical.

Example:

```text
HASH MATCH?
```

may be mechanically simple but decisive for artifact integrity.

Therefore:

```text
LOW LEVEL
≠
LOW IMPORTANCE
```

Likewise:

```text
HIGH LEVEL
≠
AUTOMATICALLY HIGHER TRUTH
```

---

# 13. H/M/L Are Not Organizational Rank

The levels should not automatically be interpreted as:

```text
EXECUTIVE
MANAGER
WORKER
```

or any human status hierarchy.

Their source semantics are:

```text
H → governance / constitution
M → domain policy
L → mechanical checks
```

No social hierarchy is implied.

---

# 14. HML-2 — Strictness Inheritance

**Law**

Outputs inherit the strictest applicable level of their inputs.

Suppose:

```text
INPUT A = L
INPUT B = M
INPUT C = H
```

and all three are load-bearing for output `O`.

Then:

```text
O
inherits
H
```

because H is the strictest applicable level.

---

# 15. Strictness Function

Conceptually define:

```text
strictness(L) < strictness(M) < strictness(H)
```

Then for load-bearing inputs:

```text
level(output)
=
max(
  level(input_1),
  level(input_2),
  ...
  level(input_n),
  level(contextual_requirement)
)
```

This is an AMOS conceptual model, not recovered source code.

---

# 16. Load-Bearing Qualification

Strictness inheritance applies to **applicable load-bearing inputs**, not every artifact merely present in context.

Suppose:

```text
A = H
B = L
```

but `A` is unrelated to conclusion `C`.

Then the mere presence of `A` should not force `C` to H.

The relevant structure is:

```text
DEPENDENCY EDGE
```

not proximity.

Conceptually:

```text
STRICTNESS(C)
=
MAX LEVEL
OVER LOAD-BEARING DEPENDENCY CLOSURE
```

---

# 17. Dependency-Aware Inheritance

```text
A(H) ───────┐
            │
B(L) ───────┼──→ C
            │
D(M) ───────┘
```

If all are load-bearing:

```text
C = H
```

But:

```text
A(H)      B(L) → C
```

with no dependency edge from `A` to `C` means:

```text
A
```

does not affect C's level.

---

# 18. Strictness Inheritance Schema

```yaml
strictness_inheritance:

  output:
    artifact_id: string

  inputs:
    - artifact_id: A
      level: H
      load_bearing: true

    - artifact_id: B
      level: L
      load_bearing: true

  contextual_requirements:
    - level: M
      reason: string

  effective_level:
    H
```

---

# 19. Strictest Applicable Level

The word **applicable** is essential.

The rule is not:

```text
ALWAYS USE H
```

The rule is:

```text
USE THE STRICTEST LEVEL
THAT ACTUALLY APPLIES
TO THE LOAD-BEARING PATH
```

This preserves efficiency without weakening integrity.

---

# 20. No Downward Laundering

A high-rigor premise cannot be transformed into a lower-rigor output merely by passing through an L-level operation.

Invalid:

```text
H CLAIM
  ↓
L FORMATTER
  ↓
L CLAIM
```

Correct:

```text
H CLAIM
  ↓
L FORMATTER
  ↓
H-SCOPED OUTPUT
```

The formatter may itself be L, but it does not erase the H requirement of the content.

---

# 21. Transformation Invariance

If transformation `T` changes representation but not semantic authority:

```text
A(H)
  ↓ T(L)
A'\(H\)
```

The operation can be L while the artifact remains H-applicable.

Thus distinguish:

```yaml
transformation:
  operation_level: L

artifact:
  inherited_level: H
```

---

# 22. Mixed-Level Artifacts

An artifact may contain components with different H/M/L applicability.

Example:

```text
DOCUMENT
├── constitutional rule      H
├── domain implementation    M
└── checksum                  L
```

The document should not necessarily flatten all internal components to one level for every operation.

Instead:

```yaml
artifact:
  aggregate_level: H

  components:
    governance:
      level: H

    domain_policy:
      level: M

    checksum:
      level: L
```

The aggregate becomes H when an operation depends on the H component.

---

# 23. Atomic Multi-Level Reasoning

A conclusion may require simultaneous validation across multiple levels.

```text
H GOVERNANCE PREMISE
       +
M DOMAIN RULE
       +
L MECHANICAL RESULT
       ↓
CONCLUSION
```

The conclusion inherits H strictness.

But each premise remains typed at its native level.

This preserves diagnostic resolution.

---

# 24. HML-3 — No Level Skipping

**Law**

Low-speed shortcuts cannot validate High-speed claims.

The canonical prohibited pattern is:

```text
H CLAIM
   ↑
L CHECK
```

when the L check is treated as sufficient proof.

---

# 25. Level-Skipping Firewall

Invalid:

```text
L PASSES
   ↓
H VERIFIED
```

unless an independently established H-level rule explicitly proves that the L result is sufficient for the specific H conclusion.

Even then, the authority comes from the H-level bridge rule, not from L alone.

---

# 26. L → H Prohibition

Suppose an artifact:

```text
PASSES SCHEMA
```

This may establish:

```text
SCHEMA VALIDITY
```

It does not automatically establish:

```text
CANONICAL VALIDITY
```

Likewise:

```text
HASH MATCH
```

does not automatically establish:

```text
SEMANTIC CORRECTNESS
```

and:

```text
TESTS PASS
```

does not automatically establish:

```text
GOVERNANCE COMPLIANCE
```

unless the required higher-level proof is separately satisfied.

---

# 27. L → M Prohibition

An L check also cannot automatically validate M policy.

Example:

```text
CONFIGURATION PARSES
```

does not imply:

```text
CONFIGURATION SATISFIES DOMAIN POLICY
```

Thus:

```text
MECHANICAL VALIDITY
≠
POLICY VALIDITY
```

---

# 28. M → H Prohibition

Likewise:

```text
DOMAIN POLICY ACCEPTS X
```

does not imply:

```text
CONSTITUTIONAL GOVERNANCE ACCEPTS X
```

unless H-level compatibility is established.

Thus:

```text
M VALID
≠
H VALID
```

---

# 29. Upward Evidence vs Upward Validation

Lower-level evidence may contribute to a higher-level conclusion.

This is allowed.

```text
L EVIDENCE
   ↓
H REASONING
   ↓
H CONCLUSION
```

What is prohibited is:

```text
L EVIDENCE
   ↓
NO H VALIDATION
   ↓
H CONCLUSION
```

Therefore:

```text
LOW-LEVEL EVIDENCE
CAN SUPPORT
HIGH-LEVEL REASONING

BUT CANNOT REPLACE
HIGH-LEVEL VALIDATION
```

---

# 30. Downward Execution

Higher-level decisions may authorize lower-level execution.

```text
H DECISION
   ↓
M POLICY
   ↓
L ACTION
```

This is not level skipping because authority flows downward through compatible constraints.

However, the L action must remain within the authorized scope.

---

# 31. Downward Specialization

Valid:

```text
H:
Protect provenance.

M:
For domain D, require source hashes.

L:
Compare SHA values.
```

Here:

```text
L mechanical check
```

implements:

```text
M domain policy
```

which specializes:

```text
H governance
```

But success of the SHA comparison does not by itself prove every aspect of provenance governance.

---

# 32. Explicit Bridge Rule

Cross-level validation may occur only when a governed bridge establishes sufficiency.

Conceptually:

```yaml
hml_bridge:

  source_level: L

  target_level: H

  target_claim:
    string

  sufficiency_rule:
    string

  authority:
    level: H

  assumptions: []

  scope:
    string

  falsifiers: []
```

Without such a bridge:

```text
L → H
VALIDATION
=
BLOCKED
```

---

# 33. Bridge Strictness

A bridge that licenses a transition to H must itself satisfy H-level governance.

Thus:

```text
L EVIDENCE
     ↓
H-AUTHORIZED BRIDGE
     ↓
H CONCLUSION
```

not:

```text
L EVIDENCE
     ↓
L BRIDGE
     ↓
H CONCLUSION
```

---

# 34. HML-4 — Explicit Assignment

**Law**

Every load-bearing artifact declares its H/M/L applicability.

This prevents hidden assumptions about required rigor.

Conceptually:

```yaml
artifact:
  artifact_id: string

  hml:
    applicability:
      - H
```

or:

```yaml
artifact:
  hml:
    applicability:
      - M
```

or:

```yaml
artifact:
  hml:
    applicability:
      - L
```

---

# 35. Applicability vs Single Level

The source says:

> every load-bearing artifact declares its H/M/L applicability.

This can support richer declarations than a single scalar when needed.

Example:

```yaml
hml:
  applicability:
    H: true
    M: true
    L: false
```

or:

```yaml
hml:
  native_level: M
  applicable_levels:
    - M
    - H
```

The exact canonical schema is not supplied, so these remain AMOS_MODEL representations.

---

# 36. Explicit Assignment Record

```yaml
hml_assignment:

  artifact_id:
    string

  native_level:
    H | M | L

  applicability:
    - H
    - M
    - L

  reason:
    string

  scope:
    string|null

  assigned_by:
    string|null

  authority:
    string|null

  provenance:
    string|null

  epoch:
    string|null
```

---

# 37. Unknown Assignment

If the correct level cannot be established:

```yaml
hml:
  level: UNKNOWN
```

A consequential operation should not silently default to L.

Conceptually:

```text
UNKNOWN LEVEL
     ↓
CONSEQUENTIAL ACTION?
  ├── NO → bounded provisional handling
  └── YES → escalate / block
```

This follows the broader AMOS fail-closed principle for critical unknowns.

---

# 38. Ambiguous Assignment

An artifact may plausibly belong to multiple levels.

Example:

```text
HYPOTHESIS 1 → M
HYPOTHESIS 2 → H
```

If the distinction changes required validation, preserve:

```yaml
hml_assignment:
  status: COMPETING
  candidates:
    - M
    - H
```

Until discriminated, use the strictest decision-relevant interpretation for consequential execution.

---

# 39. Assignment Is Falsifiable

An H/M/L assignment is itself a claim.

Therefore it should have:

* provenance,
* scope,
* assumptions,
* falsifiers,
* epoch/freshness where relevant.

```yaml
assignment_claim:
  artifact: A
  proposition: "A requires M-level validation"
  claim_class: CONDITIONAL
```

It is not automatically authoritative merely because metadata contains `level: M`.

---

# 40. Assignment Provenance

```yaml
hml_assignment_provenance:

  artifact_id:
    string

  level:
    H | M | L

  source:
    string

  source_type:
    SOURCE_CLAIM |
    OBSERVATION |
    DERIVED |
    MODEL |
    DECISION

  authority:
    string|null

  ancestry:
    []

  timestamp:
    string|null

  falsifiers:
    []
```

---

# 41. H-Level Validation Profile

A proposed H-level validation profile may require checking:

```text
AUTHORITY
+
CORE LAW COMPATIBILITY
+
PROVENANCE
+
DEPENDENCY CLOSURE
+
CONTRADICTIONS
+
SCOPE
+
REGIME
+
IRREVERSIBILITY
+
DOWNSTREAM IMPACT
```

The exact checklist is not supplied by the source and therefore remains an AMOS_MODEL extension.

---

# 42. M-Level Validation Profile

A proposed M-level profile may require:

```text
DOMAIN AUTHORITY
+
APPLICABLE H CONSTRAINTS
+
DOMAIN EVIDENCE
+
SCOPE
+
POLICY CONSISTENCY
+
CONFLICT CHECK
+
PROVENANCE
```

M-level validation must remain compatible with governing H-level constraints.

---

# 43. L-Level Validation Profile

A proposed L-level profile may focus on:

```text
LOCAL INPUTS
+
DETERMINISTIC RULE
+
EXPECTED OUTPUT
+
MECHANICAL CONSISTENCY
```

Examples:

```text
TYPE VALID?
HASH MATCH?
SCHEMA VALID?
ARITHMETIC CORRECT?
FORMAT VALID?
```

L may use fast-path validation when dependency closure is genuinely local.

---

# 44. Three-Speed Comparison

| Property                                        | H                         | M                | L                 |
| ----------------------------------------------- | ------------------------- | ---------------- | ----------------- |
| Source semantic anchor                          | governance / constitution | domain policy    | mechanical checks |
| Scope                                           | broad/foundational        | domain-bounded   | local/mechanical  |
| Typical downstream impact                       | potentially high          | bounded/domain   | local             |
| Shortcut tolerance                              | lowest                    | conditional      | highest when safe |
| Cross-domain authority                          | possible if governed      | normally bounded | none by itself    |
| Can validate H alone?                           | potentially               | no               | no                |
| Can implement higher-level rule?                | yes                       | yes              | yes               |
| Explicit assignment required when load-bearing? | yes                       | yes              | yes               |

Rows beyond the source semantic anchors are proposed model extensions.

---

# 45. H/M/L Dependency Graph

```text
           H1
          /  \
        M1    M2
       / \     \
     L1  L2    L3
```

This does not mean every system must have exactly this tree.

Dependencies may be graphs:

```text
H1 ─────┐
        ├── M3 ─── L4
H2 ─────┘      \
                L5
```

Strictness follows actual dependency closure.

---

# 46. H/M/L and RSCF

RSCF nodes may carry H/M/L applicability.

```yaml
rscf:
  state: SOURCE_CLAIM
  claim_class: CONDITIONAL

  hml:
    native_level: H
    applicability:
      - H
```

H/M/L complements rather than replaces:

```text
RSCF STATE
CLAIM CLASS
PROVENANCE
SCOPE
```

---

# 47. Orthogonality of Typing

A node can simultaneously have:

```yaml
node:
  epistemic_type: MODEL
  claim_class: CONDITIONAL
  hml_level: H
  provenance: AMOS_corpus
  scope: core_laws
```

These dimensions answer different questions:

```text
EPISTEMIC TYPE
→ what kind of thing is this?

CLAIM CLASS
→ how strongly is it supported?

H/M/L
→ what validation rigor applies?

PROVENANCE
→ where did it come from?

SCOPE
→ where does it apply?
```

---

# 48. H/M/L and Proof Capsules

An important conclusion's proof capsule should preserve the effective H/M/L level.

```yaml
proof_capsule:

  claim:
    text: string
    class: CONDITIONAL

  hml:
    native_level: M
    effective_level: H

  premises:
    - id: P1
      level: H

    - id: P2
      level: M

    - id: P3
      level: L

  confidence_ceiling:
    CONDITIONAL
```

The effective level is H because of P1.

---

# 49. H/M/L and Confidence Ceiling

Strictness level and confidence ceiling are distinct but interact.

Suppose:

```text
H CLAIM
depends on
UNKNOWN H PREMISE
```

Then more L checks cannot raise the conclusion above that unresolved premise.

Conceptually:

```text
CONFIDENCE(C)
≤
WEAKEST LOAD-BEARING PREMISE
```

while:

```text
RIGOR(C)
≥
STRICTEST APPLICABLE LEVEL
```

These are different axes.

---

# 50. Dual Constraint

Conceptually:

```text
OUTPUT
must satisfy:

RIGOR FLOOR
=
strictest applicable H/M/L level

AND

CONFIDENCE CEILING
=
weakest load-bearing premise
```

Thus AMOS must avoid both:

```text
UNDER-VALIDATION
```

and:

```text
OVER-CLAIMING
```

---

# 51. H/M/L and Provenance

A mechanical check does not repair weak provenance.

Example:

```text
SOURCE UNKNOWN
      ↓
FILE HASH VERIFIED
```

The hash may be L-verified, but source authority remains unknown.

Therefore:

```text
L INTEGRITY CHECK
≠
H/M PROVENANCE VALIDATION
```

---

# 52. H/M/L and Source Ancestry

Suppose multiple M-level domain reports depend on one H-level source claim.

```text
H SOURCE S
  │
  ├── M1
  ├── M2
  └── M3
```

The three M descendants do not create independent H confirmation.

H/M/L does not override provenance topology.

---

# 53. H/M/L and Competing Hypotheses

If two H-level interpretations remain viable:

```text
H1
vs
H2
```

many L-level checks that are compatible with both do not resolve the competition.

The preferred test is one that discriminates:

```text
T(H1) ≠ T(H2)
```

not merely one that both predict.

---

# 54. H/M/L and Causal Claims

A mechanical correlation check may be L-level.

A causal interpretation may require M- or H-level validation depending on scope and consequence.

Thus:

```text
L CORRELATION CHECK PASSES
```

does not imply:

```text
HIGHER-LEVEL CAUSAL CLAIM VERIFIED
```

HML-3 blocks the level skip.

---

# 55. H/M/L and Scope

Level assignment does not erase scope.

Example:

```yaml
artifact:
  level: M
  scope:
    domain: finance
```

does not authorize use as:

```text
M POLICY FOR ALL DOMAINS
```

The applicability envelope remains load-bearing.

---

# 56. H/M/L and Regime

A domain policy may be M-level in regime `R1` but invalid in `R2`.

```text
M POLICY @ R1
≠
M POLICY @ R2
```

unless compatibility is established.

Likewise an H-level constitutional rule may have declared regime boundaries.

Level alone does not guarantee regime invariance.

---

# 57. H/M/L and Freshness

An H assignment may become stale if governance changes.

An M assignment may become stale if domain policy changes.

An L check may become stale if:

* schema changes,
* algorithm changes,
* expected values change,
* artifact version changes.

Thus:

```yaml
hml:
  level: M
  epoch: E17
  freshness: VALID
```

may later become:

```yaml
freshness: STALE
```

requiring revalidation.

---

# 58. Epoch-Bound Assignment

Conceptually:

```text
LEVEL(A) @ E1
```

need not equal:

```text
LEVEL(A) @ E2
```

if governing semantics changed.

Therefore reusable proof capsules should preserve assignment epoch where material.

---

# 59. H/M/L and Fractal Retrieval

Within the AMOS Fractal Knowledge Network:

```text
H
↓
M
↓
L
```

can also represent retrieval granularity.

However, L16 specifically anchors H/M/L to:

```text
H governance/constitution
M domain policy
L mechanical checks
```

Therefore retrieval depth and rigor level must not be silently conflated unless authoritative canon defines them as identical.

---

# 60. Retrieval-Level Firewall

Possible AMOS architecture may use:

```text
H domain
M subsystem
L detail
```

for knowledge retrieval.

L16 uses:

```text
H governance
M policy
L mechanical checks
```

These may interact, but their exact equivalence is not established by the supplied L16 source.

Therefore:

```yaml
hml_semantic_relation:
  retrieval_HML_vs_rigor_HML:
    status: GAP_UNLESS_CANONICALLY_MAPPED
```

This is an important anti-fabrication boundary.

---

# 61. Recursive H/M/L

H/M/L may recur inside domains.

Conceptually:

```text
GLOBAL H
  ↓
DOMAIN M
      │
      ├── local governance-like policy
      ├── subsystem rules
      └── mechanical checks
```

But recursive reuse does not erase the absolute governance relation.

A local "high" within a subsystem must not automatically be treated as global H.

---

# 62. Relative vs Absolute Level

To avoid ambiguity, a future canonical schema may distinguish:

```yaml
hml:
  absolute_level: M
  local_role: H
```

For example, a subsystem's highest policy might be locally high while globally M.

The supplied source does not define this distinction, so this remains a proposed extension.

---

# 63. Strictness Across Recursion

Suppose:

```text
GLOBAL H
   ↓
DOMAIN M
   ↓
SUBSYSTEM LOCAL-H
```

If `LOCAL-H` remains subordinate to global M/H governance, its effective strictness cannot supersede its actual authority.

Therefore local naming must not manufacture constitutional authority.

---

# 64. H/M/L Fast Path

AMOS may use the smallest sufficient proof scope when:

* dependency closure is known,
* no higher-level dependency is load-bearing,
* provenance is adequate,
* scope/regime are compatible,
* evidence is fresh,
* no unresolved conflict exists.

Then:

```text
L TASK
→ L VALIDATION
→ STOP
```

may be sufficient.

No escalation is required merely because H exists somewhere in the system.

---

# 65. Fast-Path Safety Condition

Conceptually:

```python
def local_fast_path_allowed(task):
    return (
        dependency_closure_known(task)
        and highest_applicable_level(task) == L
        and provenance_valid(task)
        and scope_compatible(task)
        and freshness_valid(task)
        and not conflict_detected(task)
    )
```

Semantic pseudocode only.

---

# 66. Escalation Conditions

Escalate from L toward M/H when:

```text
HIGHER-LEVEL DEPENDENCY FOUND
OR
POLICY INTERPRETATION REQUIRED
OR
GOVERNANCE IMPACT EXISTS
OR
PROVENANCE IS AMBIGUOUS
OR
SCOPE LEAKAGE EXISTS
OR
REGIME SHIFT DETECTED
OR
CONFLICT EXISTS
OR
IRREVERSIBLE STAKES INCREASE
OR
AUTHORITY IS UNKNOWN
```

The exact escalation matrix is not supplied by the source.

---

# 67. L → M Escalation

```text
L CHECK
   ↓
POLICY QUESTION DISCOVERED
   ↓
ESCALATE TO M
```

Example:

```text
schema valid?
```

may be L.

But:

```text
is this field permitted under domain policy?
```

may require M.

---

# 68. M → H Escalation

```text
M POLICY ANALYSIS
   ↓
GOVERNANCE CONFLICT DISCOVERED
   ↓
ESCALATE TO H
```

Example:

```text
domain policy permits X
```

but:

```text
core governance appears to prohibit X
```

requires H resolution.

---

# 69. Direct L → H Escalation

Escalation does not always need to pass through M sequentially.

If an L operation discovers a direct constitutional issue:

```text
L
↓
H CONFLICT
↓
ESCALATE H
```

The "no level skipping" law prohibits **validation shortcuts**, not efficient escalation.

---

# 70. De-Escalation

Once higher-level uncertainty is resolved, execution may return to lower levels.

```text
H RESOLUTION
   ↓
M POLICY FIXED
   ↓
L EXECUTION
```

This is valid.

De-escalation means the remaining task is lower-level, not that prior H constraints disappear.

---

# 71. H/M/L Validation State Machine

```text
ARTIFACT
   ↓
LEVEL DECLARED?
 ├── NO
 │    ↓
 │ UNKNOWN
 │    ↓
 │ ESCALATE IF CONSEQUENTIAL
 │
 └── YES
      ↓
DEPENDENCIES DISCOVERED
      ↓
STRICTEST LEVEL COMPUTED
      ↓
VALIDATION SUFFICIENT?
 ├── NO → ESCALATE
 └── YES
      ↓
LEVEL SKIP?
 ├── YES → REJECT / REVALIDATE
 └── NO
      ↓
CLASSIFY
```

---

# 72. H-Level State Machine

```text
H CLAIM
  ↓
AUTHORITY KNOWN?
  ├── NO → UNKNOWN / BLOCK
  └── YES
       ↓
CORE-LAW COMPATIBLE?
  ├── NO → CONFLICT
  └── YES
       ↓
PROVENANCE VALID?
  ├── NO → CONDITIONAL / BLOCK
  └── YES
       ↓
DEPENDENCY + SCOPE + REGIME CHECK
       ↓
ADVERSARIAL VALIDATION
       ↓
CLAIM CLASS
```

This is proposed operational semantics, not recovered source code.

---

# 73. M-Level State Machine

```text
M CLAIM
  ↓
DOMAIN IDENTIFIED?
  ├── NO → UNKNOWN
  └── YES
       ↓
APPLICABLE H CONSTRAINTS KNOWN?
  ├── NO → ESCALATE
  └── YES
       ↓
DOMAIN POLICY VALID?
  ├── NO → REJECT
  └── YES
       ↓
SCOPE / PROVENANCE / CONFLICT CHECK
       ↓
CLAIM CLASS
```

---

# 74. L-Level State Machine

```text
L TASK
  ↓
INPUTS VALID?
  ├── NO → FAIL
  └── YES
       ↓
MECHANICAL RULE DEFINED?
  ├── NO → ESCALATE / UNKNOWN
  └── YES
       ↓
EXECUTE CHECK
       ↓
PASS / FAIL
       ↓
DO NOT GENERALIZE ABOVE L
```

---

# 75. H/M/L Assignment Algorithm

```python
def assign_hml(artifact):

    if affects_governance_or_constitution(artifact):
        return H

    if defines_or_interprets_domain_policy(artifact):
        return M

    if purely_mechanical_and_local(artifact):
        return L

    return UNKNOWN
```

This is semantic pseudocode.

Real assignment may require contextual dependencies and authoritative taxonomy.

---

# 76. Effective-Level Algorithm

```python
def effective_level(output, inputs, context):

    levels = []

    for item in inputs:
        if is_load_bearing(item, output):
            levels.append(item.hml_level)

    for requirement in context.requirements:
        if applies(requirement, output):
            levels.append(requirement.hml_level)

    if not levels:
        return UNKNOWN

    return strictest(levels)
```

---

# 77. Level-Skip Detector

```python
def detect_level_skip(
    target_claim,
    evidence_path
):

    target = target_claim.hml_level

    highest_validated = highest_validated_level(
        evidence_path
    )

    if strictness(highest_validated) < strictness(target):
        return True

    return False
```

This simplified model assumes no separately governed bridge.

---

# 78. Bridge-Aware Level-Skip Detector

```python
def validate_cross_level_path(
    source_level,
    target_level,
    bridge
):

    if strictness(source_level) >= strictness(target_level):
        return PASS

    if bridge is None:
        return FAIL

    if bridge.authority_level != target_level:
        return FAIL

    if not bridge.valid_for_scope:
        return FAIL

    return PASS
```

---

# 79. Strictness Inheritance Algorithm

```python
LEVEL_ORDER = {
    "L": 1,
    "M": 2,
    "H": 3
}

def inherit_strictness(load_bearing_inputs):

    if not load_bearing_inputs:
        return "UNKNOWN"

    return max(
        (
            item.hml_level
            for item in load_bearing_inputs
        ),
        key=lambda level: LEVEL_ORDER[level]
    )
```

Semantic pseudocode only.

---

# 80. H/M/L Proof Sufficiency

For a claim `C`:

```text
CLAIM SUFFICIENCY(C)
```

requires at minimum:

```text
CORRECT LEVEL ASSIGNMENT
+
SUFFICIENT VALIDATION AT THAT LEVEL
+
LOAD-BEARING DEPENDENCY CLOSURE
+
NO UNGOVERNED LEVEL SKIP
```

This does not mean every claim needs H-level analysis.

---

# 81. Action Sufficiency

A conclusion may be epistemically adequate but still insufficient for action if action stakes demand higher governance.

Conceptually:

```text
CLAIM LEVEL = M
ACTION IMPACT = H
```

Then:

```text
ACTION VALIDATION
→ H
```

even if the underlying descriptive claim remains M.

This distinction is a proposed extension consistent with AMOS action governance.

---

# 82. Irreversibility Escalation

When an action has:

* irreversible cost,
* broad institutional impact,
* legal exposure,
* safety impact,
* major downstream dependency,

the required validation may escalate.

Conceptually:

```text
BASE TASK = M
+
IRREVERSIBLE GOVERNANCE IMPACT
=
EFFECTIVE H
```

This is an AMOS_MODEL extension rather than an explicit L16 source law.

---

# 83. Reversible Action Preference

Under uncertainty:

```text
H UNKNOWN
```

does not necessarily require total inactivity if a reversible lower-risk action exists.

Preferred:

```text
REVERSIBLE
+
BOUNDED
+
INFORMATION-GAINING
```

action while preserving the unresolved H question.

But no reversible action may violate known H constraints.

---

# 84. H/M/L and Failure Recovery

When a validation premise fails, invalidate only dependent conclusions.

Example:

```text
H1
├── M1
│   ├── L1
│   └── L2
└── M2
```

If:

```text
M1 FAILS
```

then invalidate:

```text
M1
L1
L2
```

but preserve:

```text
H1
M2
```

unless they depend on M1 through another edge.

---

# 85. H-Level Failure

If an H premise fails:

```text
H1 INVALID
```

all descendants that require H1 must be reconsidered.

```text
H1 ✕
│
├── M1 → INVALIDATE
├── M2 → INVALIDATE
└── M3
    └── L1 → INVALIDATE
```

Independent branches remain intact.

---

# 86. M-Level Failure

```text
H1
│
├── M1 ✕
│   ├── L1
│   └── L2
│
└── M2 ✓
```

Recovery:

```text
INVALIDATE:
M1
L1
L2

PRESERVE:
H1
M2
```

---

# 87. L-Level Failure

An L failure normally invalidates only the mechanical result and conclusions dependent on it.

```text
L1 ✕
```

does not automatically invalidate:

```text
M POLICY
```

unless that policy conclusion depended on L1.

Again, dependency edges govern recovery.

---

# 88. H/M/L and Atomic Reasoning

A decision may require:

```text
H AUTHORITY
+
M POLICY
+
L CHECK
```

The system should not finalize the decision from partial validation such as:

```text
H ✓
M ?
L ✓
```

if M is load-bearing.

Conceptually:

```text
ATOMIC FINALIZATION
=
ALL LOAD-BEARING LEVELS VALID
```

within the relevant proof scope.

---

# 89. Partial Success

If:

```text
L ✓
M ✓
H UNKNOWN
```

and H is load-bearing:

```text
FINAL H-SENSITIVE CLAIM
=
UNKNOWN / CONDITIONAL
```

not verified.

The successful lower-level work should be preserved for reuse after H resolution.

---

# 90. H/M/L and Contradiction

Suppose:

```text
H RULE → NOT X
M POLICY → X
```

This is not resolved by taking the more specific M policy automatically.

Instead:

```text
CONFLICT
→ ESCALATE
→ PRESERVE CONTRADICTION
```

until authority and scope resolve it.

---

# 91. Apparent Contradiction Across Scope

Not every H/M conflict is real.

Example:

```text
H:
X prohibited globally except governed exception E

M:
X permitted inside E
```

This may be compatible.

Therefore contradiction analysis must preserve scope and exception semantics.

---

# 92. H/M/L and Authority

Conceptually:

```text
H authority
may constrain
M authority

M authority
may constrain
L execution
```

But H/M/L itself does not establish who or what possesses authority.

Authority provenance must be separately known.

---

# 93. Authority Firewall

Do not infer:

```text
ARTIFACT MARKED H
```

therefore:

```text
ARTIFACT IS AUTHORITATIVE
```

The H label indicates applicability/rigor, not authenticity or canonical authority.

Authority still requires provenance.

---

# 94. Self-Declared H

An artifact cannot manufacture authority merely by declaring:

```yaml
hml:
  level: H
```

The declaration is a source claim until validated.

Thus:

```text
SELF-LABEL
≠
GOVERNANCE AUTHORITY
```

---

# 95. H/M/L and Canonical Status

A proposed specification can be H-level while remaining conditional.

Example:

```yaml
canonical_status: CONDITIONAL
hml:
  level: H
```

This means:

```text
THE CLAIM CONCERNS GOVERNANCE
BUT IS NOT YET AUTHORITATIVE CANON
```

This distinction is especially important for L16 itself.

---

# 96. L16 Self-Application

L16 defines a governance-like rule system for H/M/L.

Therefore under its own proposed semantics, L16 is plausibly H-applicable.

However, because authoritative HML canon has not been recovered:

```yaml
L16:
  hml_assignment:
    proposed_level: H
    claim_class: CONDITIONAL
```

This is a derived model interpretation, not an authoritative self-certification.

---

# 97. No Circular Self-Validation

L16 cannot prove itself valid by applying L16.

Invalid:

```text
L16 says HML works
     ↓
HML validates L16
     ↓
therefore L16 is canon
```

This is circular.

Authoritative validation must come from independent canonical authority or evidence.

---

# 98. H/M/L and Canon Hierarchy

Conceptually:

```text
CANONICAL H LAW
      ↓
DOMAIN M POLICY
      ↓
LOCAL L CHECK
```

But the exact mapping between `LAW_HIERARCHY` and H/M/L is not supplied.

Therefore:

```yaml
law_hierarchy_hml_mapping:
  status: GAP
```

until authoritative canon defines it.

---

# 99. H/M/L Artifact Schema

```yaml
hml_artifact:

  artifact_id:
    string

  artifact_type:
    string

  hml:
    native_level:
      H | M | L | UNKNOWN

    effective_level:
      H | M | L | UNKNOWN

    applicability:
      - H
      - M
      - L

    assignment_status:
      SOURCE_CLAIM |
      DERIVED |
      VERIFIED |
      CONDITIONAL |
      COMPETING |
      UNKNOWN

  scope:
    system: string|null
    domain: string|null
    environment: string|null
    regime: string|null

  provenance:
    source: string|null
    ancestry: []

  dependencies: []

  falsifiers: []

  freshness:
    epoch: string|null
    state: string|null
```

---

# 100. H/M/L Decision Schema

```yaml
hml_decision:

  decision_id:
    string

  proposed_action:
    string

  base_level:
    H | M | L

  effective_level:
    H | M | L

  load_bearing_inputs:
    - artifact_id: string
      level: H | M | L

  governance_impact:
    none |
    bounded |
    high

  reversibility:
    reversible |
    partially_reversible |
    irreversible

  validation:
    status:
      PASS |
      FAIL |
      CONDITIONAL |
      UNKNOWN

  unresolved_conflicts: []

  falsifiers: []
```

---

# 101. H/M/L Proof Capsule

```yaml
hml_proof_capsule:

  claim:
    text: string

    class:
      VERIFIED |
      DERIVED |
      MODEL |
      CONDITIONAL |
      COMPETING |
      UNKNOWN

  hml:
    declared_level:
      H | M | L

    effective_level:
      H | M | L

    assignment_basis:
      string

  load_bearing_premises:
    - premise_id: string
      level: H | M | L
      claim_class: string

  provenance:
    roots: []

  scope:
    string|null

  regime:
    string|null

  dependencies: []

  competing_explanations: []

  falsifiers: []

  level_skip_check:
    PASS |
    FAIL |
    UNKNOWN

  confidence_ceiling:
    string
```

---

# 102. H-Level Proof Capsule

```yaml
H_proof_capsule:

  target:
    governance_or_constitutional_claim

  authority:
    source: string|null
    status: string

  governing_laws: []

  provenance:
    roots: []

  dependencies: []

  contradictions: []

  scope:
    string|null

  regime:
    string|null

  irreversible_impact:
    string|null

  adversarial_validation:
    status: string

  conclusion:
    class: string
```

---

# 103. M-Level Proof Capsule

```yaml
M_proof_capsule:

  target:
    domain_policy_claim

  domain:
    string

  governing_H_constraints: []

  policy_sources: []

  evidence: []

  scope:
    string

  contradictions: []

  provenance:
    roots: []

  conclusion:
    class: string
```

---

# 104. L-Level Proof Capsule

```yaml
L_proof_capsule:

  target:
    mechanical_check

  inputs: []

  rule:
    string

  deterministic:
    true|false

  execution_result:
    PASS |
    FAIL |
    UNKNOWN

  scope:
    string

  provenance:
    roots: []
```

---

# 105. H/M/L Validation Contract

```yaml
hml_validation_contract:

  artifact:
    id: string

  assignment:
    native_level:
      H | M | L

    effective_level:
      H | M | L

  dependency_closure:
    known: true|false

  strictness_inheritance:
    checked: true|false

  level_skip:
    detected: true|false

  provenance:
    validated: true|false

  scope:
    validated: true|false

  regime:
    validated: true|false

  conflicts:
    unresolved: []

  validation_result:
    PASS |
    FAIL |
    CONDITIONAL |
    UNKNOWN
```

---

# 106. H/M/L Integrity Invariants

```yaml
hml_integrity_invariants:

  HMLI_1_EXPLICIT:
    requirement:
      every_load_bearing_artifact_declares_hml_applicability

  HMLI_2_STRICTEST:
    requirement:
      output_inherits_strictest_applicable_load_bearing_level

  HMLI_3_NO_SKIP:
    requirement:
      lower_level_validation_cannot_alone_validate_higher_level_claim

  HMLI_4_PROVENANCE:
    requirement:
      level_labels_do_not_replace_authority_or_provenance

  HMLI_5_SCOPE:
    requirement:
      hml_level_does_not_override_scope

  HMLI_6_REGIME:
    requirement:
      hml_level_does_not_override_regime_validity

  HMLI_7_CONFIDENCE:
    requirement:
      strictness_level_does_not_override_confidence_ceiling

  HMLI_8_DEPENDENCY:
    requirement:
      inheritance_uses_actual_load_bearing_dependency_edges

  HMLI_9_CONFLICT:
    requirement:
      cross_level_conflicts_are_not_silently_resolved

  HMLI_10_BRIDGE:
    requirement:
      upward_cross_level_validation_requires_governed_sufficiency

  HMLI_11_RECOVERY:
    requirement:
      failure_invalidates_only_dependent_artifacts

  HMLI_12_NO_AUTHORITY_LAUNDERING:
    requirement:
      self_declared_H_does_not_create_canonical_authority
```

---

# 107. Anti-Patterns

## HML-A1 — L Validates H

```text
L CHECK PASSED
→ H CLAIM VERIFIED
```

Rejected.

---

## HML-A2 — M Overrides H

```text
M POLICY SAYS X
→ IGNORE H CONSTRAINT
```

Rejected unless authoritative scope/exception semantics establish compatibility.

---

## HML-A3 — Hidden Level

A load-bearing artifact has no H/M/L assignment.

```text
LEVEL = IMPLICIT
```

Rejected for consequential reasoning.

---

## HML-A4 — Lowest-Level Wins

```text
H + M + L
→ use L because it is fastest
```

Rejected.

Correct:

```text
H + M + L
→ effective rigor H
```

when all are load-bearing.

---

## HML-A5 — Highest-Level Everywhere

```text
EVERY TASK
→ H
```

also rejected.

This destroys the purpose of adaptive rigor.

Use the strictest **applicable** level.

---

## HML-A6 — H Label Equals Truth

```text
LEVEL = H
→ VERIFIED
```

Rejected.

---

## HML-A7 — L Label Equals Unimportant

```text
LEVEL = L
→ LOW CONSEQUENCE
```

Rejected.

---

## HML-A8 — Formatting Downgrade

```text
H CONTENT
→ L TRANSFORMATION
→ L CONTENT
```

Rejected when semantic authority is preserved.

---

## HML-A9 — Context Contamination

An unrelated H artifact exists in context, therefore every output becomes H.

Rejected.

Inheritance follows dependency edges.

---

## HML-A10 — Retrieval/Rigor Conflation

```text
H RETRIEVAL DOMAIN
=
H GOVERNANCE LEVEL
```

without canonical mapping.

Rejected.

---

## HML-A11 — Circular Self-Validation

```text
HML validates HML
→ HML canonical
```

Rejected.

---

## HML-A12 — Authority Laundering

```text
artifact declares level H
→ artifact is constitutional authority
```

Rejected.

---

# 108. Adversarial Validation

For consequential H/M/L assignment, challenge:

```text
IS THIS REALLY THE CORRECT LEVEL?

IS A HIGHER-LEVEL DEPENDENCY HIDDEN?

IS THE APPARENT H DEPENDENCY ACTUALLY LOAD-BEARING?

IS A LOW-LEVEL CHECK BEING USED TO PROVE A HIGHER CLAIM?

IS DOMAIN POLICY BEING MISTAKEN FOR CONSTITUTIONAL AUTHORITY?

IS RETRIEVAL GRANULARITY BEING CONFUSED WITH RIGOR LEVEL?

IS THE LEVEL LABEL SELF-DECLARED WITHOUT AUTHORITY?

HAS SCOPE CHANGED?

HAS THE GOVERNANCE EPOCH CHANGED?

IS THERE A CONFLICT WITH A STRICTER APPLICABLE RULE?
```

If challenge succeeds:

```text
REASSIGN
ESCALATE
DOWNGRADE
PRESERVE COMPETING
or
RETURN UNKNOWN
```

as appropriate.

---

# 109. Sensitivity

For consequential decisions, identify the smallest change that would alter effective H/M/L.

Example:

```text
CURRENT:
all load-bearing dependencies = L

NEW FACT:
one dependency is governance-sensitive H
```

Then:

```text
effective level:
L → H
```

That hidden dependency is the sensitivity pivot.

---

# 110. H/M/L Uncertainty Vector

```yaml
hml_uncertainty:

  assignment:
    question:
      Is the artifact assigned to the correct level?

  dependency:
    question:
      Are all load-bearing dependencies known?

  authority:
    question:
      Is the level assignment supported by valid authority?

  scope:
    question:
      Does the assignment apply in this scope?

  regime:
    question:
      Does it remain valid in the current regime?

  temporal:
    question:
      Is the assignment fresh?

  execution:
    question:
      Can the required validation actually be performed?

  provenance:
    question:
      Is the assignment ancestry trustworthy?
```

---

# 111. H/M/L and Knowledge Memory

Durable H/M/L knowledge should preserve:

```yaml
hml_memory:

  artifact_id:
    string

  native_level:
    H | M | L

  effective_level:
    H | M | L

  assignment_basis:
    string

  authority:
    string|null

  scope:
    string|null

  regime:
    string|null

  epoch:
    string|null

  provenance:
    roots: []

  falsifiers: []

  revalidation_conditions: []
```

A remembered level assignment should not be silently treated as permanently valid.

---

# 112. H/M/L Knowledge Harvest

```text
ARTIFACT
   ↓
PROPOSE LEVEL
   ↓
VALIDATE ASSIGNMENT
   ↓
RECORD PROVENANCE
   ↓
RECORD SCOPE / REGIME
   ↓
PERSIST
   ↓
REVALIDATE WHEN GOVERNANCE CHANGES
```

Do not persist:

```text
UNVALIDATED LEVEL GUESS
```

as authoritative H/M/L knowledge.

---

# 113. H/M/L Retrieval Strategy

When answering a question:

```text
OBJECTIVE
   ↓
IDENTIFY LOAD-BEARING ARTIFACTS
   ↓
READ DECLARED H/M/L
   ↓
TRACE ONLY MATERIAL DEPENDENCIES
   ↓
COMPUTE STRICTEST APPLICABLE LEVEL
   ↓
VALIDATE AT THAT LEVEL
```

This supports the AMOS smallest-sufficient-proof principle.

---

# 114. H/M/L and Adaptive Complexity

A possible alignment is:

```text
L TASK
→ lower reasoning complexity often sufficient

M TASK
→ structured domain reasoning

H TASK
→ deeper governance validation
```

But:

```text
H/M/L
≠
C0/C1/C2/C3/C4
```

unless authoritative canon explicitly maps them.

H/M/L concerns validation applicability; adaptive complexity concerns reasoning effort.

---

# 115. Complexity Firewall

An H claim may sometimes be simple.

An L task may sometimes be computationally expensive.

Therefore:

```text
H
≠
COMPUTATIONALLY EXPENSIVE

L
≠
COMPUTATIONALLY CHEAP
```

The "three-speed" metaphor refers to rigor classes in this specification, not guaranteed runtime cost.

---

# 116. H/M/L and Action Governance

Conceptually:

```text
ACTION
  ↓
WHAT LEVEL DOES THE CLAIM REQUIRE?
  ↓
WHAT LEVEL DOES THE ACTION IMPACT REQUIRE?
  ↓
TAKE STRICTER
```

Thus:

```text
effective_action_level
=
max(
  claim_required_level,
  action_governance_level
)
```

This is a proposed AMOS model.

---

# 117. H/M/L and Reversibility

A reversible L action may proceed under lower validation when:

* no H/M rule is violated,
* uncertainty is bounded,
* rollback exists,
* no hidden higher-level dependency is known.

An irreversible action may require escalation.

Therefore H/M/L can govern not only belief formation but execution rigor.

---

# 118. H/M/L and Failure Recovery Basins

Before consequential mutation, recovery targets should match effective level.

Conceptually:

```text
H MUTATION
→ governance rollback / authoritative snapshot

M MUTATION
→ domain-policy rollback

L MUTATION
→ local transaction / file / state rollback
```

Exact recovery mechanisms are subsystem-specific.

---

# 119. Strictness Monotonicity

For a fixed dependency set:

```text
ADDING A STRICTER LOAD-BEARING PREMISE
```

must not lower required rigor.

Conceptually:

```text
R(S ∪ {x})
≥
R(S)
```

where `R` is required H/M/L strictness and `x` is load-bearing.

This is a derived invariant of HML-2.

---

# 120. Irrelevant-Premise Stability

Adding a non-load-bearing artifact should not alter effective level.

```text
x ∉ dependency_closure(C)
```

then conceptually:

```text
R(C | S ∪ {x})
=
R(C | S)
```

This prevents needless H escalation from irrelevant context.

---

# 121. Representation Stability

Changing representation should not change effective level unless semantics or dependencies change.

```text
MARKDOWN H CLAIM
   ↓
JSON CONVERSION
   ↓
H CLAIM
```

The conversion operation may be L.

The claim's applicability remains H.

---

# 122. Copy Stability

Copying an H artifact does not downgrade it.

```text
A(H)
→ copy
→ A'\(H\)
```

However, provenance should record the ancestry:

```text
A → A'
```

A copied artifact does not become an independent authority source.

---

# 123. Aggregation Rule

Suppose a report aggregates:

```text
A(L)
B(M)
C(M)
```

If all are load-bearing:

```text
REPORT = M
```

If an H premise is added:

```text
A(L)
B(M)
C(M)
D(H)
```

then:

```text
REPORT = H
```

for conclusions dependent on D.

---

# 124. Decomposition Rule

An H artifact may be decomposed into local L operations without downgrading the H semantic claim.

```text
H ARTIFACT
   ↓
parse      L
hash       L
format     L
serialize  L
```

These operations establish local properties only.

The overall governance meaning remains H-sensitive.

---

# 125. Verification Composition

Suppose:

```text
L1 PASS
L2 PASS
L3 PASS
```

Composition gives:

```text
ALL THREE L CONDITIONS PASS
```

It does not automatically produce:

```text
M PASS
```

or:

```text
H PASS
```

unless a higher-level rule explicitly defines those L conditions as jointly sufficient.

---

# 126. Higher-Level Sufficiency Rule

A legitimate composition may be:

```text
H RULE:
If L1, L2, L3 all pass,
then H-condition Q is satisfied.
```

Then:

```text
L1 ✓
L2 ✓
L3 ✓
+
H SUFFICIENCY RULE
→ Q
```

The proof remains H-governed because the sufficiency relation itself is H.

---

# 127. H/M/L Finalization

A consequential conclusion may finalize only when:

```text
LEVEL ASSIGNMENT
✓

STRICTNESS INHERITANCE
✓

REQUIRED VALIDATION
✓

NO UNGOVERNED LEVEL SKIP
✓

PROVENANCE
✓

SCOPE / REGIME
✓

LOAD-BEARING CONFLICTS
RESOLVED OR EXPLICIT
```

If any critical requirement remains unknown:

```text
FINALIZATION
=
BLOCKED / CONDITIONAL
```

depending on stakes.

---

# 128. H/M/L Concurrency

Different independent branches may be validated at different levels simultaneously.

```text
BRANCH A → H
BRANCH B → L
BRANCH C → M
```

No need to promote all branches to H merely because one branch is H.

Only merged conclusions inherit the strictest applicable branch.

---

# 129. Merge Rule

```text
A(H) ──┐
       ├──→ C
B(L) ──┘
```

If both load-bearing:

```text
C = H
```

But:

```text
A(H) → C1

B(L) → C2
```

keeps:

```text
C1 = H
C2 = L
```

until a later merge requires inheritance.

---

# 130. Atomic Merge

When a conclusion depends jointly on multiple levels:

```text
C = f(H1, M1, L1)
```

finalization requires all load-bearing components to be valid.

```text
H1 ✓
M1 ✓
L1 ✕
```

means:

```text
C NOT FINAL
```

even though L is the least strict level.

Strictness does not mean lower-level premises are optional.

---

# 131. H/M/L Provenance Topology

```text
H SOURCE
   │
   ├── M POLICY A
   │      └── L CHECK A
   │
   └── M POLICY B
          └── L CHECK B
```

If the H source invalidates:

```text
ALL DEPENDENT BRANCHES
→ REVALIDATE
```

If only L Check A fails:

```text
L CHECK B
```

and unrelated branches remain valid.

---

# 132. H/M/L Sybil Hardening

Ten M policies copied from one H authority do not constitute ten independent H confirmations.

Likewise ten L tests derived from one flawed M policy do not independently validate that policy.

```text
DESCENDANT MULTIPLICITY
≠
ANCESTRAL INDEPENDENCE
```

---

# 133. H/M/L Governance Mutation

Changing an H-level law may alter:

* M policies,
* L validators,
* stored proof capsules,
* effective-level assignments,
* action permissions.

Therefore H mutation should expose its dependency graph before finalization where consequential.

Conceptually:

```text
H MUTATION
   ↓
DEPENDENT M NODES
   ↓
DEPENDENT L NODES
   ↓
IMPACT SET
```

---

# 134. M Policy Mutation

Changing M policy requires revalidation of:

```text
DEPENDENT L EXECUTION
```

but not necessarily unrelated H governance.

```text
H remains
M changes
L descendants revalidate
```

---

# 135. L Mechanism Mutation

Changing an L mechanism may require revalidation of mechanical results.

It does not automatically alter M/H semantics unless those higher conclusions depend on the changed mechanism.

---

# 136. H/M/L Versioning

A useful representation:

```yaml
hml_version:

  level:
    H | M | L

  semantic_version:
    string|null

  authority_version:
    string|null

  epoch:
    string|null

  hash:
    string|null
```

This supports freshness and revalidation.

Exact version semantics are not supplied by the source.

---

# 137. H/M/L Revalidation Triggers

Possible triggers:

```text
AUTHORITY CHANGE
POLICY CHANGE
SCHEMA CHANGE
DEPENDENCY CHANGE
SCOPE CHANGE
REGIME CHANGE
PROVENANCE FAILURE
CONTRADICTION DISCOVERED
LEVEL REASSIGNMENT
NEW HIGHER-LEVEL CONSTRAINT
```

Only dependent conclusions need revalidation.

---

# 138. H/M/L Stop Condition

Reasoning may stop when:

```text
CLAIM SUFFICIENCY
+
DECISION SUFFICIENCY
+
ACTION SUFFICIENCY
```

are achieved at the strictest applicable level.

Do not continue escalating merely for completeness when no unresolved uncertainty can change the outcome.

---

# 139. H/M/L Minimal Proof Scope

```text
TASK
 ↓
LOAD-BEARING CLOSURE
 ↓
STRICTEST LEVEL
 ↓
MINIMUM VALIDATOR SET
 ↓
RESULT
```

This preserves:

```text
INTEGRITY
>
UNNECESSARY COMPLEXITY
```

without weakening HML-2 or HML-3.

---

# 140. H/M/L Canonical Safety Boundary

L16 does **not** establish:

* that H always requires maximal reasoning complexity,
* that L always means trivial,
* that H artifacts are automatically true,
* that M artifacts are less important than H artifacts,
* that L checks are optional,
* that every H claim requires every available source,
* that H/M/L equals H/M/L retrieval depth,
* that H/M/L equals organizational rank,
* that H/M/L equals confidence,
* that H/M/L equals epistemic class,
* that an artifact can self-certify its authority by declaring H,
* that every domain policy is M under all scopes,
* that every mechanical operation is L under all contexts,
* that lower-level evidence is irrelevant to higher-level reasoning.

These remain unsupported unless separately established.

---

# 141. Falsifiers

## F1 — Authoritative HML Canon Defines Different Level Semantics

Original falsifier:

> **authoritative HML canon defines different level semantics.**

If recovered canon defines:

```text
H ≠ governance / constitution
M ≠ domain policy
L ≠ mechanical checks
```

or materially changes their relation, L16 must be revised.

Process:

```text
RECOVER AUTHORITATIVE HML CANON
             ↓
COMPARE SEMANTICS
             ↓
CONFLICT?
  ├── NO → preserve
  └── YES
        ↓
invalidate affected L16 rules
        ↓
recompute dependent H/M/L assignments
```

---

# 142. Additional Invalidation Conditions

Proposed extensions should also be reconsidered if authoritative canon defines:

* a different strictness order,
* non-monotonic inheritance,
* permitted level skipping,
* a mandatory single-level assignment schema,
* explicit equivalence between retrieval H/M/L and rigor H/M/L,
* a different bridge model,
* different cross-level authority semantics.

These are not additional source falsifiers; they are derived invalidation conditions for the expanded specification.

---

# 143. Known Gaps

```yaml
gaps:

  G1:
    severity: CRITICAL
    description:
      Authoritative HML canon has not been supplied beyond the four proposed laws.

  G2:
    severity: DECISION_RELEVANT
    description:
      Exact formal criteria for assigning artifacts to H, M, or L are not defined.

  G3:
    severity: DECISION_RELEVANT
    description:
      Exact H-level validation checklist is not defined.

  G4:
    severity: DECISION_RELEVANT
    description:
      Exact M-level validation checklist is not defined.

  G5:
    severity: DECISION_RELEVANT
    description:
      Exact L-level validator taxonomy is not defined.

  G6:
    severity: DECISION_RELEVANT
    description:
      Canonical semantics for cross-level sufficiency bridges are not defined.

  G7:
    severity: DECISION_RELEVANT
    description:
      Relationship between HML rigor semantics and H/M/L fractal retrieval semantics is not established.

  G8:
    severity: EXPLANATORY
    description:
      Relative versus absolute H/M/L semantics for recursive subsystems are not defined.

  G9:
    severity: EXPLANATORY
    description:
      Exact mapping between LAW_HIERARCHY and H/M/L is not supplied.

  G10:
    severity: EXPLANATORY
    description:
      Exact relationship between H/M/L and adaptive complexity C0-C4 is not supplied.
```

These gaps must remain explicit rather than being silently filled.

---

# 144. RSCF Claim Graph

```yaml
claim_graph:

  HML_C001:
    class: AMOS_MODEL
    claim:
      H, M, and L represent distinct rigor/applicability lenses.

  HML_C002:
    class: CONDITIONAL
    claim:
      H is anchored to governance and constitutional reasoning.

  HML_C003:
    class: CONDITIONAL
    claim:
      M is anchored to domain policy.

  HML_C004:
    class: CONDITIONAL
    claim:
      L is anchored to mechanical checks.

  HML_C005:
    class: AMOS_MODEL
    claim:
      Outputs inherit the strictest applicable level of load-bearing inputs.

  HML_C006:
    class: DERIVED
    claim:
      An unrelated H artifact should not force an independent L conclusion to H.

  HML_C007:
    class: AMOS_MODEL
    claim:
      L-level shortcuts cannot independently validate H-level claims.

  HML_C008:
    class: DERIVED
    claim:
      M-level validation cannot independently establish H-level validity.

  HML_C009:
    class: AMOS_MODEL
    claim:
      Every load-bearing artifact must explicitly declare H/M/L applicability.

  HML_C010:
    class: DERIVED
    claim:
      H/M/L assignment does not replace provenance, scope, regime, or claim class.

  HML_C011:
    class: CONDITIONAL
    claim:
      Retrieval H/M/L and rigor H/M/L must remain distinct unless authoritative canon maps them.

  HML_C012:
    class: DERIVED
    claim:
      Representation-only transformations do not downgrade inherited rigor.

  HML_C013:
    class: DERIVED
    claim:
      Cross-level validation requires a governed sufficiency relation.

  HML_C014:
    class: CONDITIONAL
    claim:
      L16 itself is plausibly H-applicable but cannot self-certify canonical authority.
```

---

# 145. Dependency Graph

```yaml
dependency_graph:

  HML_1:
    depends_on:
      - H_semantics
      - M_semantics
      - L_semantics

  HML_2:
    depends_on:
      - level_order
      - applicability
      - dependency_edges
      - load_bearing_status

  HML_3:
    depends_on:
      - target_claim_level
      - evidence_level
      - sufficiency_bridge_if_any
      - authority

  HML_4:
    depends_on:
      - artifact_identity
      - assignment_schema
      - assignment_provenance
      - scope
```

---

# 146. Unified H/M/L Architecture

```text
                    ARTIFACT
                       │
                       ▼
             ┌──────────────────┐
             │ EXPLICIT H/M/L   │
             │ ASSIGNMENT       │
             └────────┬─────────┘
                      ↓
              DEPENDENCY CLOSURE
                      ↓
          ┌───────────┼───────────┐
          ↓           ↓           ↓
          H           M           L
    governance     domain      mechanical
   constitution    policy       checks
          │           │           │
          └───────────┼───────────┘
                      ↓
             STRICTEST APPLICABLE
                      ↓
               VALIDATION PATH
                      ↓
              LEVEL-SKIP CHECK
                      ↓
             PROVENANCE / SCOPE
                      ↓
              CONFLICT CHECK
                      ↓
                CLAIM CLASS
```

---

# 147. Three-Speed Operational Contract

```yaml
three_speed_contract:

  H:
    purpose:
      governance_and_constitution

    validation:
      rigor:
        highest_of_three

    shortcuts:
      permitted_only_if:
        higher_level_sufficiency_is_established

  M:
    purpose:
      domain_policy

    validation:
      must_respect:
        - applicable_H_constraints

  L:
    purpose:
      mechanical_checks

    validation:
      optimized_for:
        local_bounded_deterministic_checks

    cannot_alone_validate:
      - M_policy_claims
      - H_governance_claims
```

"Highest of three" refers to the strictness ordering proposed by HML-2 semantics, not truth value.

---

# 148. Canonical Compression

```text
H
GOVERNANCE / CONSTITUTION

M
DOMAIN POLICY

L
MECHANICAL CHECKS
```

Then:

```text
STRICTEST APPLICABLE LEVEL WINS.
```

But:

```text
STRICTEST APPLICABLE
≠
H EVERYWHERE
```

And:

```text
LOWER-LEVEL SUCCESS
≠
HIGHER-LEVEL VALIDATION
```

Finally:

```text
EVERY LOAD-BEARING ARTIFACT
DECLARES ITS H/M/L APPLICABILITY.
```

---

# 149. Canonical One-Line Law

> **AMOS H/M/L assigns distinct rigor to governance, domain policy, and mechanical validation; every load-bearing artifact declares its applicability, every output inherits the strictest applicable load-bearing level, and no lower-level shortcut may independently validate a higher-level claim.**

---

# 150. Canonical Equations

Conceptual AMOS model:

```text
L < M < H
```

for validation strictness.

For conclusion `C` with load-bearing dependency set `D(C)`:

```text
RIGOR(C)
=
MAX {
  HML(x)
  |
  x ∈ D(C)
  and x is applicable
}
```

No-level-skipping invariant:

```text
VALIDATION_LEVEL
<
TARGET_REQUIRED_LEVEL

⇒

TARGET NOT VALIDATED
```

unless a separately governed target-level sufficiency bridge exists.

Confidence remains independently bounded:

```text
CONFIDENCE(C)
≤
WEAKEST LOAD-BEARING PREMISE
```

Therefore:

```text
HML STRICTNESS
determines
VALIDATION FLOOR

EPISTEMIC SUPPORT
determines
CONFIDENCE CEILING
```

---

# 151. Final Proof Capsule

```yaml
proof_capsule:

  claim:
    class: CONDITIONAL
    text:
      >
        AMOS L16 models H/M/L as a three-speed rigor lens:
        H for governance/constitutional reasoning, M for domain
        policy, and L for mechanical checks. Outputs inherit the
        strictest applicable level among their load-bearing inputs.
        Lower-level shortcuts cannot independently validate
        higher-level claims, and every load-bearing artifact must
        explicitly declare its H/M/L applicability.

  source:
    provenance:
      AMOS_corpus

    scope:
      core_laws

  load_bearing_premises:
    - H_semantic_anchor_is_governance_constitution
    - M_semantic_anchor_is_domain_policy
    - L_semantic_anchor_is_mechanical_checks
    - strictness_inheritance_applies_to_outputs
    - level_skipping_is_prohibited
    - load_bearing_artifacts_require_explicit_assignment

  dependencies:
    - RSCF
    - LAW_HIERARCHY
    - provenance_topology
    - scope_regime_firewall
    - competing_hypotheses
    - failure_recovery
    - knowledge_memory

  competing_explanations:
    - HML_may_have_more_specific_authoritative_semantics_not_yet_recovered
    - HML_retrieval_levels_may_or_may_not_map_directly_to_HML_rigor_levels
    - recursive_subsystems_may_require_relative_level_semantics
    - authoritative_canon_may_define_cross_level_bridges_differently

  falsifiers:
    - authoritative_HML_canon_defines_different_level_semantics

  gaps:
    - exact_assignment_criteria_not_supplied
    - exact_level_validation_profiles_not_supplied
    - exact_cross_level_bridge_semantics_not_supplied
    - retrieval_HML_to_rigor_HML_mapping_not_supplied
    - relative_vs_absolute_HML_semantics_not_supplied

  confidence_ceiling:
    CONDITIONAL

  canonical_status:
    CONDITIONAL

  specification_status:
    PROPOSED_SPECIFICATION
```

---

# 152. RSCF Node

```yaml
RSCF-NODE:

  node_id:
    l16_hml

  node_type:
    note

  path:
    01_CANON/01_CORE_LAWS/L16_HML.md

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

  - RELATED_TO: [[RSCF]]

  - RELATED_TO: [[GMEF]]

  - RELATED_TO: [[PROVENANCE_TOPOLOGY]]

  - RELATED_TO: [[COMPETING_HYPOTHESES]]

  - RELATED_TO: [[SCOPE_REGIME_FIREWALL]]

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

# 153. L16 Final Invariant

```text
EVERY LOAD-BEARING ARTIFACT
DECLARES
H / M / L

          ↓

TRACE ACTUAL
DEPENDENCIES

          ↓

TAKE THE
STRICTEST APPLICABLE LEVEL

          ↓

VALIDATE AT
THAT LEVEL

          ↓

NEVER USE
LOWER-LEVEL SUCCESS
AS UNGOVERNED PROOF
OF A HIGHER-LEVEL CLAIM
```

The compact operational law is:

```text
DECLARE
→ TRACE
→ INHERIT
→ VALIDATE
→ CHECK LEVEL SKIP
→ CLASSIFY
```

with the hard firewalls:

```text
L VALID
≠
M VALID

M VALID
≠
H VALID

H LABEL
≠
H AUTHORITY

H LEVEL
≠
VERIFIED

L LEVEL
≠
UNIMPORTANT

REPRESENTATION CHANGE
≠
RIGOR DOWNGRADE

UNRELATED H CONTEXT
≠
AUTOMATIC H ESCALATION

RETRIEVAL H/M/L
≠
RIGOR H/M/L
UNLESS CANONICALLY MAPPED
```

**Conclusion class: CONDITIONAL / AMOS_MODEL.**

```
