---
title: CONFLICT REGISTRY
type: registry
artifact_id: AMOS-OS-CONFLICT-REGISTRY
canonical_name: CONFLICT_REGISTRY
artifact_type: canonical_conflict_registry
status: SOURCE_CLAIM
conclusion_class: AMOS_MODEL
amos_core_target: v4.4

origin_architect: Trang Phan
steward: Trang Phan

domain: canon
scope: AMOS_OS
authority_scope: conflict-identification-preservation-classification-resolution-and-invalidation

created: 2026-08-25
updated: 2026-08-25

tags: [amos-os, canon, universe, canon-group/meta, canon/framework, canon/registry, canon/conflict-registry, canon/provenance, canon/lineage, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/conflict-registry, topic/contradiction, topic/competing-hypotheses, topic/evidence-topology, topic/provenance-topology, topic/source-independence, topic/regime, topic/scope, topic/invalidation, topic/adversarial-validation]

aliases: "- AMOS Conflict Registry
  - AMOS OS Conflict Registry
  - Canon Conflict Registry..."---




# AMOS OS Conflict Registry

> **Origin architect / steward:** Trang Phan  
> **AMOS Core target:** `v4.4`  
> **Conclusion class:** `AMOS_MODEL`  
> **Status:** `SOURCE_CLAIM`

## 1. Purpose

`CONFLICT_REGISTRY.md` defines the canonical AMOS OS contract for identifying, recording, preserving, classifying, testing, resolving, superseding, and auditing material conflicts.

A conflict may exist between:

```text
CLAIMS
SOURCES
RSCFs
MODELS
CANON ARTIFACTS
RULES
INVARIANTS
VERSIONS
SCOPES
REGIMES
OBSERVATIONS
DECISIONS
AUTHORITY ASSERTIONS
PROVENANCE RECORDS
STATE RECORDS
TEST RESULTS
```

The registry exists so contradiction is never silently removed for fluency, convenience, majority agreement, or premature convergence.

---

# 2. Core Law

```text
CONFLICT DETECTED
!=
CONFLICT RESOLVED
```

and:

```text
ABSENCE OF RESOLUTION
!=
PERMISSION TO CHOOSE
```

When incompatible hypotheses remain equally supported, incomparable, correlated, or insufficiently evidenced:

```text
PRESERVE COMPETING
```

---

# 3. Integrity Priority

Conflict handling follows:

```text
INTEGRITY
>
COMPLETENESS
>
FLUENCY
>
SPEED
>
TOKEN SAVINGS
```

A clean-looking answer must never be produced by hiding a material contradiction.

---

# 4. Conflict Registry Boundary

The Conflict Registry is distinct from:

```text
CONFLICT_REGISTRY
!=
SOURCE_REGISTRY

CONFLICT_REGISTRY
!=
CLAIM_REGISTRY

CONFLICT_REGISTRY
!=
CANON

CONFLICT_REGISTRY
!=
PROVENANCE_LEDGER

CONFLICT_REGISTRY
!=
SOURCE_LINEAGE

CONFLICT_REGISTRY
!=
AUTHORITY_REGISTRY

CONFLICT_REGISTRY
!=
DECISION_LOG

CONFLICT_REGISTRY
!=
ERROR_LOG
```

Conceptually:

```text
SOURCE_REGISTRY
→ identifies evidence objects

SOURCE_LINEAGE
→ identifies ancestry

CLAIM / RSCF
→ represents propositions and dependencies

CONFLICT_REGISTRY
→ represents incompatibility requiring preservation,
   discrimination, qualification, or resolution
```

---

# 5. What Counts as a Conflict

A conflict exists when two or more relevant states cannot all be accepted under the same declared interpretation, scope, time, regime, assumptions, or authority context.

Examples:

```text
CLAIM A
vs
NOT CLAIM A

VALUE = 10
vs
VALUE = 20

RULE X REQUIRED
vs
RULE X PROHIBITED

SOURCE A SAYS X
vs
SOURCE B SAYS NOT-X

MODEL A PREDICTS X
vs
MODEL B PREDICTS Y

CANON REVISION A
vs
CANON REVISION B

OBSERVATION A
vs
EXPECTED INVARIANT

AUTHORITY A PERMITS ACTION
vs
AUTHORITY B DENIES ACTION
```

---

# 6. Apparent Conflict

Not every disagreement is a genuine contradiction.

Before classifying a hard conflict, test for:

```text
SCOPE DIFFERENCE
REGIME DIFFERENCE
TIME DIFFERENCE
VERSION DIFFERENCE
UNIT DIFFERENCE
DEFINITION DIFFERENCE
MEASUREMENT DIFFERENCE
ASSUMPTION DIFFERENCE
POPULATION DIFFERENCE
SCALE DIFFERENCE
SEMANTIC ALIASING
PROVENANCE DUPLICATION
```

Example:

```text
CLAIM A valid in R₁
CLAIM B valid in R₂
```

may represent:

```text
REGIME-SCOPED COMPATIBILITY
```

rather than contradiction.

---

# 7. Conflict Classes

Recommended top-level classes:

```text
DIRECT_CONTRADICTION
PARTIAL_CONTRADICTION
SCOPE_CONFLICT
REGIME_CONFLICT
TEMPORAL_CONFLICT
VERSION_CONFLICT
SEMANTIC_CONFLICT
UNIT_CONFLICT
MEASUREMENT_CONFLICT
PROVENANCE_CONFLICT
AUTHORITY_CONFLICT
INVARIANT_CONFLICT
MODEL_CONFLICT
OBSERVATION_CONFLICT
STATE_CONFLICT
DEPENDENCY_CONFLICT
IMPLEMENTATION_CONFLICT
UNKNOWN_CONFLICT
```

---

# 8. Direct Contradiction

```text
A
vs
NOT A
```

under the same:

```text
scope
time
regime
definitions
measurement basis
assumptions
```

is a direct contradiction.

Do not weaken it into vague language such as:

```text
different perspectives
```

when logical incompatibility is established.

---

# 9. Partial Contradiction

Two claims may overlap only partly.

Example:

```text
A:
X applies to all systems.

B:
X fails for system S.
```

B conflicts with the universal portion of A but may not invalidate all narrower instances.

Use targeted invalidation.

---

# 10. Scope Conflict

```text
A valid for population P₁
B valid for population P₂
```

is not automatically a contradiction.

Conflict exists only if an artifact incorrectly projects both into the same applicability envelope.

Canonical firewall:

```text
DIFFERENT SCOPE
!=
CONTRADICTION
```

---

# 11. Regime Conflict

A proposition may change validity across regimes.

```text
R₁ → A
R₂ → NOT A
```

This can be valid if:

```text
R₁ != R₂
```

The registry must preserve the regime boundary rather than forcing universal convergence.

---

# 12. Temporal Conflict

Example:

```text
T₁: POLICY = A
T₂: POLICY = B
```

This may represent evolution rather than contradiction.

Check:

```text
effective_from
effective_until
supersession
revision
```

before declaring unresolved conflict.

---

# 13. Version Conflict

Different revisions may legitimately disagree.

```text
v3.0 → RULE A
v4.4 → RULE B
```

Required question:

```text
IS B A GOVERNED SUCCESSOR,
AN ALTERNATIVE BRANCH,
OR AN UNRELATED CLAIM?
```

Filename version labels alone do not answer this.

---

# 14. Semantic Conflict

Different terms may refer to:

```text
same concept
different concepts
overlapping concepts
historically renamed concepts
```

Resolve terminology before treating textual disagreement as substantive contradiction.

Use:

```text
CANONICAL_GLOSSARY
ALIASES
DEPRECATED_TERMS
```

where available.

---

# 15. Unit Conflict

Example:

```text
10 ms
vs
10 s
```

may arise from unit mismatch rather than evidence disagreement.

Units must be resolved before epistemic conflict classification.

---

# 16. Measurement Conflict

Two observations may differ because of:

```text
different instruments
different calibration
different sampling
different normalization
different environments
different measurement windows
```

Measurement incompatibility must remain visible.

---

# 17. Provenance Conflict

A provenance conflict exists when source origin, ancestry, authorship, derivation, revision, or independence claims disagree.

Examples:

```text
SRC-A claims ROOT-X
SRC-B records ROOT-Y
```

or:

```text
SOURCE A marked independent
but lineage shows shared ancestor
```

This can materially alter evidence strength.

---

# 18. Authority Conflict

Authority conflicts occur when multiple authority-bearing artifacts issue incompatible directives inside overlapping authority scope.

Example:

```text
POLICY-A → ALLOW
POLICY-B → DENY
```

Resolution requires authority hierarchy, scope, time, and supersession analysis.

Popularity does not resolve authority conflicts.

---

# 19. Invariant Conflict

An invariant conflict occurs when:

```text
PROPOSED STATE
```

would violate:

```text
GOVERNING INVARIANT
```

Example:

```text
CAPABILITY → AUTHORITY
```

conflicts with:

```text
CAPABILITY != AUTHORITY
```

The invariant violation must be surfaced before execution.

---

# 20. Model Conflict

Models may produce incompatible explanations or predictions.

```text
MODEL H₁ → X
MODEL H₂ → Y
```

Do not collapse them unless discriminating evidence exists.

Use:

```text
COMPETING
```

where appropriate.

---

# 21. Observation Conflict

Observed states may conflict with:

```text
other observations
models
predictions
expected invariants
historical state
```

Observation conflict does not automatically identify which side is wrong.

---

# 22. State Conflict

Persistent or distributed state may disagree.

Conceptually:

```text
STATE-A = X
STATE-B = Y
```

Resolution may require:

```text
revision identity
causal ordering
authority
epoch
commit state
recovery semantics
```

Repository-level canon should define the contract without pretending that conceptual mechanisms prove implementation.

---

# 23. Dependency Conflict

A dependency conflict exists when a conclusion depends on premises that cannot simultaneously hold.

Example:

```text
CONCLUSION C
requires A
requires B

A contradicts B
```

Then:

```text
C MUST NOT PASS UNCONDITIONALLY
```

---

# 24. Minimum Conflict Record

Every consequential conflict SHOULD support a structure equivalent to:

```yaml
conflict:
  conflict_id:
  canonical_name:

  classification:
    conflict_type:
    severity:
    state:

  parties:
    - object_id:
      object_type:
      claim:
      source_refs: []

  compatibility:
    same_scope:
    same_regime:
    same_time:
    same_version:
    same_units:
    same_definitions:
    same_measurement_method:

  provenance:
    source_lineage_refs: []
    independence_state:
    correlation_risk:

  analysis:
    contradiction_statement:
    shared_premises: []
    differing_premises: []
    hidden_dependencies: []
    candidate_explanations: []

  discrimination:
    falsifiers: []
    discriminating_tests: []
    cheapest_high_information_test:

  lifecycle:
    detected_at:
    status:
    resolved_at:
    superseded_by:

  resolution:
    outcome:
    winning_claim:
    losing_claim:
    scoped_resolution:
    rationale_ref:

  impact:
    affected_claims: []
    affected_rscfs: []
    affected_models: []
    affected_decisions: []

  integrity:
    conclusion_class:
    unresolved_gaps: []
```

---

# 25. Conflict Identity

Each material conflict should receive a stable identity:

```text
conflict_id
```

Conceptual format:

```text
CNF::<namespace>::<stable-id>
```

Example:

```text
CNF::AMOS::CANON-001
```

This is a naming model, not proof of current implementation.

---

# 26. Conflict Identity Firewall

```text
CONFLICT_ID
!=
CLAIM_ID

CONFLICT_ID
!=
SOURCE_ID

CONFLICT_ID
!=
RSCF_ID

CONFLICT_ID
!=
INCIDENT_ID

CONFLICT_ID
!=
ERROR_ID
```

One conflict may involve many claims and sources.

One claim may participate in multiple conflicts.

---

# 27. Conflict State

Recommended states:

```text
DETECTED
UNDER_REVIEW
COMPETING
CONDITIONAL
RESOLVED
PARTIALLY_RESOLVED
SUPERSEDED
INVALIDATED
DORMANT
UNKNOWN/GAP
```

---

# 28. DETECTED

Use when incompatibility has been identified but not sufficiently analyzed.

```text
DETECTED
!=
CONFIRMED DIRECT CONTRADICTION
```

Classification may change after scope or regime analysis.

---

# 29. UNDER_REVIEW

Use when active discrimination is underway.

This state should preserve all material alternatives.

---

# 30. COMPETING

Use when incompatible hypotheses remain legitimately live.

Canonical rule:

```text
EQUAL SUPPORT
OR
INCOMPARABLE SUPPORT
OR
CORRELATED SUPPORT
OR
INSUFFICIENT DISCRIMINATION
→
COMPETING
```

---

# 31. CONDITIONAL

Use when apparent disagreement can be resolved through explicit conditions.

Example:

```text
IF R₁ → A
IF R₂ → B
```

The result is conditional, not universal.

---

# 32. RESOLVED

A conflict may be marked `RESOLVED` only when discriminating evidence or governing authority is sufficient for the declared scope.

Resolution must preserve:

```text
why
scope
time
regime
evidence
dependencies
invalidation conditions
```

---

# 33. PARTIALLY_RESOLVED

Use when only part of the conflict space has been resolved.

Example:

```text
A wins for R₁
B remains competing for R₂
```

Do not promote the whole conflict to resolved.

---

# 34. SUPERSEDED

Use when a later conflict record or governed resolution replaces an earlier treatment.

Historical conflict identity should remain recoverable.

---

# 35. UNKNOWN/GAP

Use when critical information is missing.

Examples:

```text
unknown source ancestry
unknown revision
unknown regime
unknown measurement method
unknown authority hierarchy
unknown scope
```

Canonical law:

```text
UNKNOWN/GAP
!=
PASS
```

---

# 36. Severity

Recommended decision-oriented severity classes:

```text
COSMETIC
EXPLANATORY
DECISION_RELEVANT
CRITICAL
```

Resolve in this order:

```text
CRITICAL
↓
DECISION_RELEVANT
↓
EXPLANATORY
↓
COSMETIC
```

---

# 37. Critical Conflict

A conflict is `CRITICAL` when unresolved contradiction prevents safe or valid continuation.

Examples:

```text
authority ambiguity before irreversible commit
contradictory safety constraints
broken canonical lineage
conflicting invariants
unresolved source identity for load-bearing evidence
```

---

# 38. Decision-Relevant Conflict

A conflict is decision-relevant if resolving it can change:

```text
choice
action
priority
resource allocation
confidence
governance path
```

These conflicts deserve evidence spending.

---

# 39. Explanatory Conflict

An explanatory conflict affects understanding but not the current decision.

It should remain visible without necessarily blocking execution.

---

# 40. Cosmetic Conflict

Formatting, naming, or presentation disagreement that does not alter semantics may be classified as cosmetic.

Do not spend deep reasoning budget on cosmetic conflicts while critical ones remain unresolved.

---

# 41. Conflict Detection

Conflict detection SHOULD test:

```text
LOGICAL INCOMPATIBILITY
SEMANTIC INCOMPATIBILITY
NUMERICAL INCOMPATIBILITY
SCOPE OVERLAP
REGIME OVERLAP
TEMPORAL OVERLAP
VERSION OVERLAP
AUTHORITY OVERLAP
DEPENDENCY INCOMPATIBILITY
PROVENANCE INCOMPATIBILITY
```

---

# 42. Conflict Normalization

Before comparing claims:

```text
NORMALIZE TERMINOLOGY
↓
NORMALIZE UNITS
↓
IDENTIFY VERSION
↓
IDENTIFY TIME
↓
IDENTIFY SCOPE
↓
IDENTIFY REGIME
↓
IDENTIFY ASSUMPTIONS
↓
COMPARE
```

This reduces false contradiction.

---

# 43. Evidence Topology

Conflict analysis must distinguish:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN
```

Different epistemic types cannot always be compared as peers.

Example:

```text
MODEL prediction
vs
OBSERVATION
```

is not equivalent to:

```text
OBSERVATION
vs
OBSERVATION
```

---

# 44. Provenance Independence

Suppose:

```text
H₁ supported by A, B, C
H₂ supported by D
```

If:

```text
A ← ROOT-X
B ← ROOT-X
C ← ROOT-X
```

then H₁ does not automatically have three independent confirmations.

Canonical rule:

```text
SOURCE COUNT
!=
INDEPENDENT EVIDENCE COUNT
```

---

# 45. Sybil Hardening

Conflict resolution must resist evidence multiplication.

```text
ROOT-A
├→ ARTICLE-1
├→ ARTICLE-2
├→ AGENT-SUMMARY
├→ REPORT
└→ DATABASE-COPY
```

may still constitute one evidence ancestry.

Repetition does not resolve conflict.

---

# 46. Authority Firewall

```text
MORE AUTHORITATIVE
```

may resolve:

```text
WHICH RULE GOVERNS?
```

but does not automatically resolve:

```text
WHICH EMPIRICAL CLAIM IS TRUE?
```

Keep governance and empirical resolution distinct.

---

# 47. Causal Firewall

Conflicts about causation require causal evidence.

Do not resolve:

```text
A CAUSES B
vs
A DOES NOT CAUSE B
```

using only:

```text
correlation
sequence
co-occurrence
analogy
structural similarity
```

Relevant distinctions include:

```text
association
correlation
mechanism
enabling condition
necessary condition
sufficient condition
mediation
confounding
feedback
causal effect
```

---

# 48. Scope Firewall

A conflict can disappear after scope partitioning.

Example:

```text
A true for P₁
B true for P₂
```

Correct resolution may be:

```text
CONDITIONAL BY POPULATION
```

not:

```text
A WINS
```

---

# 49. Regime Firewall

If system behavior changes across regimes:

```text
R₁ → H₁
R₂ → H₂
```

the registry should preserve both.

A regime transition may invalidate a formerly correct resolution.

---

# 50. Freshness Conflict

New evidence may conflict with older evidence because the environment changed.

Check:

```text
IS OLD EVIDENCE WRONG?
```

versus:

```text
DID THE SYSTEM CHANGE?
```

These are not equivalent.

---

# 51. Conflict and Supersession

A newer artifact does not automatically win.

Required checks:

```text
IS IT A LEGITIMATE SUCCESSOR?

DOES IT SHARE THE SAME AUTHORITY SCOPE?

DOES IT EXPLICITLY SUPERSEDE?

IS LINEAGE VERIFIED?

IS THE NEW VERSION VALID FOR THIS REGIME?
```

---

# 52. Competing Hypothesis Structure

Recommended representation:

```yaml
hypotheses:

  H1:
    claim:
    supporting_sources: []
    contradicting_sources: []
    assumptions: []
    scope:
    regime:
    falsifiers: []

  H2:
    claim:
    supporting_sources: []
    contradicting_sources: []
    assumptions: []
    scope:
    regime:
    falsifiers: []
```

Do not force a winner prematurely.

---

# 53. Strongest Supported Conclusion

For consequential conflicts:

```text
BUILD THE STRONGEST SUPPORTED CONCLUSION
```

Then challenge it using a genuinely different path.

Challenge for:

```text
contradiction
correlated provenance
stale premises
scope leakage
hidden dependency
causal overreach
stronger alternative
```

---

# 54. Adversarial Challenge

Conceptual process:

```text
PROVISIONAL CONCLUSION
↓
SEARCH FOR STRONGEST CONTRADICTION
↓
CHECK SOURCE ANCESTRY
↓
CHECK SCOPE
↓
CHECK REGIME
↓
CHECK FRESHNESS
↓
CHECK CAUSAL TYPE
↓
CHECK DEPENDENCIES
↓
CHECK ALTERNATIVE MODEL
↓
RETAIN / DOWNGRADE / CONDITION / COMPETE / INVALIDATE
```

---

# 55. Discriminating Evidence

When multiple hypotheses remain live, prefer:

```text
CHEAPEST
HIGH-INFORMATION
DISCRIMINATING TEST
```

over accumulating redundant supporting material.

---

# 56. Discriminating Test

A discriminating test should have materially different expected outcomes under competing hypotheses.

Example:

```text
H₁ predicts X
H₂ predicts NOT-X

TEST T observes X or NOT-X
```

T has higher conflict-resolution value than another source repeating shared assumptions.

---

# 57. Sensitivity

Identify:

```text
THE SMALLEST PREMISE,
THRESHOLD,
ASSUMPTION,
OR OBSERVATION
CAPABLE OF FLIPPING THE RESULT
```

Test it first.

---

# 58. Fragile Resolution

If small plausible changes reverse the winner:

```text
CONDITIONAL
```

is preferable to an overconfident resolution.

---

# 59. Robust Resolution

A resolution is more robust when it survives plausible perturbations of noncritical assumptions.

Robustness does not imply universality beyond the tested envelope.

---

# 60. Resolution Classes

Possible resolution outcomes:

```text
CLAIM_A_SUPPORTED
CLAIM_B_SUPPORTED
BOTH_CONDITIONAL
BOTH_COMPETING
SCOPE_PARTITIONED
REGIME_PARTITIONED
TEMPORALLY_PARTITIONED
VERSION_SUPERSEDED
SEMANTICALLY_RECONCILED
UNIT_RECONCILED
MEASUREMENT_RECONCILED
AUTHORITY_RESOLVED
INSUFFICIENT_EVIDENCE
UNKNOWN/GAP
```

---

# 61. Resolution Proof Capsule

Important conflict resolutions should conceptually preserve:

```text
claim/class
load-bearing premises
evidence/provenance
scope
temporal validity
regime validity
dependencies
competing explanations
falsifiers
invalidation conditions
confidence ceiling
```

---

# 62. Resolution Confidence Ceiling

Resolution confidence cannot exceed the weakest load-bearing premise unless that premise is independently revalidated or removed.

```text
RESOLUTION CONFIDENCE
<=
WEAKEST LOAD-BEARING PREMISE
```

---

# 63. Local Resolution

AMOS v4.4 reasoning permits local resolution only when relevant closure is established:

```text
dependency closure
provenance independence
scope compatibility
regime compatibility
freshness
non-conflict with governing constraints
```

Independence must be demonstrated, not assumed.

---

# 64. Escalation Conditions

Escalate conflict handling when:

```text
evidence shares ancestry
sources materially conflict
evidence is stale
regimes differ
causal coupling exists
governance is affected
stakes are irreversible
dependencies are ambiguous
authority is unclear
critical invariants may fail
```

---

# 65. Conflict Resolution Workflow

```text
DETECT
↓
REGISTER
↓
CLASSIFY
↓
NORMALIZE
↓
CHECK SCOPE
↓
CHECK REGIME
↓
CHECK TIME
↓
CHECK VERSION
↓
CHECK PROVENANCE
↓
CHECK INDEPENDENCE
↓
IDENTIFY HYPOTHESES
↓
IDENTIFY LOAD-BEARING DIFFERENCE
↓
SELECT DISCRIMINATING TEST
↓
CHALLENGE PROVISIONAL WINNER
↓
RESOLVE / CONDITION / COMPETE / UNKNOWN
```

---

# 66. No Majority Rule

Canonical prohibition:

```text
MOST SOURCES AGREE
```

does not imply:

```text
CLAIM VERIFIED
```

until provenance topology is considered.

Ten descendants of one source may provide less independent confirmation than two truly independent observations.

---

# 67. No Authority-by-Repetition

```text
REPEATED CLAIM
!=
CANON
```

Canon requires governed promotion.

---

# 68. No Resolution-by-Fluency

A synthesized paragraph that blends incompatible claims is not a valid resolution.

Do not produce:

```text
A and NOT-A are both essentially true
```

unless a legitimate scope, regime, semantic, or conditional partition explains how.

---

# 69. No Silent Averaging

Conflicting numerical claims must not automatically be averaged.

Example:

```text
10
vs
100
```

does not license:

```text
55
```

without a model that justifies aggregation.

---

# 70. No Silent Scope Expansion

If evidence supports:

```text
SCOPE A
```

conflict resolution must not produce:

```text
UNIVERSAL CLAIM
```

without evidence for the expanded scope.

---

# 71. No Silent Causal Upgrade

Resolving an association conflict does not license a causal conclusion.

```text
ASSOCIATION RESOLVED
!=
CAUSATION VERIFIED
```

---

# 72. No Silent Historical Rewrite

When a newer canon supersedes an older canon:

```text
OLD CANON
```

must remain historically recoverable.

Do not rewrite lineage to make the newer rule appear timeless.

---

# 73. Invalidation

If conflict resolution shows a premise invalid:

```text
INVALIDATE THE PREMISE
AND DEPENDENT DESCENDANTS
```

not unrelated branches.

---

# 74. Selective Invalidation

Example:

```text
P1 → C1
P1 → C2

P2 → C3
```

If P1 fails:

```text
INVALIDATE C1
INVALIDATE C2
PRESERVE C3
```

This is dependency-local recovery.

---

# 75. Rollback

When a resolution fails:

```text
ROLL BACK
TO
NEAREST VALID STATE
```

Preserve unaffected work.

Do not globally recompute unless necessary.

---

# 76. Failed Resolution Path

A failed path should not simply be repeated.

Canonical rule:

```text
DO NOT REPEAT FAILED PATH
WITHOUT CHANGED EVIDENCE
```

---

# 77. Conflict Reopening

A resolved conflict may reopen when:

```text
new evidence appears
source provenance changes
source independence fails
regime changes
scope changes
governing authority changes
freshness expires
dependency changes
falsifier is triggered
```

---

# 78. Resolution Validity Envelope

Every consequential resolution SHOULD specify:

```text
system/population
environment
scale
time
regime
measurement method
assumptions
```

Resolution outside this envelope remains unproven.

---

# 79. Conflict Lifecycle

```text
DETECTED
↓
UNDER_REVIEW
↓
COMPETING / CONDITIONAL
↓
RESOLVED / PARTIALLY_RESOLVED
↓
MONITORED
↓
REOPENED if invalidation condition fires
```

---

# 80. Conflict Dependency Graph

Conceptually:

```text
SOURCE
↓
CLAIM
↓
CONFLICT
↓
RESOLUTION
↓
RSCF
↓
MODEL / DECISION / ACTION
```

The registry should support reverse traversal to determine downstream impact.

---

# 81. Conflict Propagation

A conflict does not automatically propagate everywhere.

Propagation occurs only along relevant dependency edges.

```text
CONFLICT
→ DEPENDENT CLAIM
→ DEPENDENT RSCF
→ DEPENDENT DECISION
```

---

# 82. Canon Conflict

A conflict involving canon requires elevated governance.

Potential cases:

```text
two active canonical definitions
conflicting invariant declarations
unclear supersession
broken version lineage
authority overlap
semantic identity collision
```

No agent should silently choose a canon branch.

---

# 83. Kernel Conflict

Kernel conflicts concern deterministic operators or invariants.

Examples:

```text
operator definitions disagree
same input produces incompatible expected outputs
invariants cannot simultaneously hold
```

Resolution requires canonical dependency review.

---

# 84. Control Plane Conflict

Control-plane conflicts may involve:

```text
authority
commit rights
policy
finalization
provenance
state transitions
```

These are governance-relevant and should generally escalate.

---

# 85. Runtime Conflict

Runtime conflicts may involve:

```text
scheduler decisions
router decisions
worker state
execution results
retries
commit observations
```

Runtime observations must not silently redefine canon.

---

# 86. Agent Conflict

Agents may disagree.

```text
AGENT-A → H₁
AGENT-B → H₂
```

Agent count is not evidence count.

Check whether agents used:

```text
same sources
same model
same prompt lineage
same tools
same assumptions
```

before treating disagreement as independent analysis.

---

# 87. Model Conflict

Multiple models may disagree because of:

```text
architecture
training
assumptions
inputs
calibration
regime
randomness
```

Model disagreement is evidence about model uncertainty, not automatically about ground truth.

---

# 88. Tool Conflict

Two tools may return different values.

Before choosing:

```text
CHECK DATA SOURCE
CHECK QUERY
CHECK TIME
CHECK VERSION
CHECK UNITS
CHECK CACHE
CHECK TRANSFORMATION
```

Tool identity is not source authority.

---

# 89. Memory Conflict

Persistent memory may conflict with newer evidence.

Canonical principle:

```text
MEMORY
!=
CANON
```

Memory should be revalidated when it becomes load-bearing and conflicts with fresher authoritative evidence.

---

# 90. Knowledge Conflict

Knowledge artifacts may legitimately preserve competing models.

Do not force the knowledge layer into a single narrative where discriminating evidence is absent.

---

# 91. Research Conflict

External papers may disagree.

Required checks include:

```text
study population
method
sample
measurement
date
environment
replication
shared datasets
shared authorship/source lineage
```

Paper count alone does not resolve the conflict.

---

# 92. Conflict Query Model

The registry SHOULD conceptually support:

```text
GET CONFLICT BY ID

GET OPEN CONFLICTS

GET CRITICAL CONFLICTS

GET CONFLICTS FOR CLAIM

GET CONFLICTS FOR SOURCE

GET CONFLICTS FOR RSCF

GET CONFLICTS FOR CANON ARTIFACT

GET CONFLICTS BY TYPE

GET CONFLICTS BY REGIME

GET CONFLICTS BY SCOPE

GET COMPETING HYPOTHESES

GET UNRESOLVED AUTHORITY CONFLICTS

GET CONFLICTS WITH UNKNOWN PROVENANCE

GET RESOLVED CONFLICTS

GET REOPENED CONFLICTS

GET DOWNSTREAM IMPACT
```

---

# 93. Logical Indexes

Potential indexes:

```text
BY_CONFLICT_ID
BY_STATE
BY_SEVERITY
BY_TYPE
BY_OBJECT
BY_SOURCE
BY_CLAIM
BY_RSCF
BY_SCOPE
BY_REGIME
BY_VERSION
BY_AUTHORITY
BY_PROVENANCE
BY_RESOLUTION
BY_DEPENDENT
```

These describe architectural requirements, not current implementation proof.

---

# 94. Conflict Registry Invariants

```text
CNF-001
CONFLICT DETECTED != CONFLICT RESOLVED

CNF-002
DISAGREEMENT != DIRECT CONTRADICTION

CNF-003
DIFFERENT SCOPE != CONTRADICTION

CNF-004
DIFFERENT REGIME != CONTRADICTION

CNF-005
DIFFERENT TIME != CONTRADICTION

CNF-006
DIFFERENT VERSION != CONTRADICTION

CNF-007
SOURCE COUNT != INDEPENDENT EVIDENCE COUNT

CNF-008
REPETITION != CONFIRMATION

CNF-009
AUTHORITY != EMPIRICAL TRUTH

CNF-010
POPULARITY != AUTHORITY

CNF-011
MODEL AGREEMENT != VERIFICATION

CNF-012
AGENT AGREEMENT != INDEPENDENT CONFIRMATION

CNF-013
ABSENCE OF CONTRADICTION != PROOF

CNF-014
STRUCTURAL SIMILARITY != CAUSATION

CNF-015
CORRELATION != CAUSATION

CNF-016
NEWER != AUTOMATICALLY AUTHORITATIVE

CNF-017
SUPERSESSION != HISTORICAL ERASURE

CNF-018
UNKNOWN/GAP != PASS

CNF-019
COMPETING MUST REMAIN COMPETING UNTIL DISCRIMINATED

CNF-020
INVALIDATION PROPAGATES ONLY THROUGH DEPENDENCIES

CNF-021
RESOLUTION MUST BE SCOPE-BOUNDED

CNF-022
RESOLUTION MUST BE REGIME-AWARE

CNF-023
RESOLUTION CONFIDENCE CANNOT EXCEED ITS LOAD-BEARING PREMISES

CNF-024
FAILED RESOLUTION PATH MUST NOT REPEAT WITHOUT CHANGED EVIDENCE

CNF-025
MATERIAL CONTRADICTION MUST REMAIN VISIBLE
```

---

# 95. Integrity Gate

Before resolving a consequential conflict:

```text
[ ] conflict identity established
[ ] parties explicitly represented
[ ] semantic normalization checked
[ ] units checked
[ ] scope overlap checked
[ ] regime overlap checked
[ ] temporal overlap checked
[ ] versions checked
[ ] provenance checked
[ ] source ancestry checked
[ ] independence checked
[ ] correlation risk checked
[ ] authority scope checked
[ ] load-bearing premises identified
[ ] competing explanations preserved
[ ] falsifiers identified
[ ] discriminating evidence sought
[ ] sensitivity checked
[ ] downstream impact identified
[ ] invalidation conditions recorded
[ ] unresolved gaps exposed
```

---

# 96. High-Stakes Gate

Increase validation when conflict resolution affects:

```text
LEGAL
FINANCIAL
HEALTH
SAFETY
SECURITY
INSTITUTIONAL GOVERNANCE
IRREVERSIBLE COST
LARGE DOWNSTREAM DEPENDENCY
CANON PROMOTION
AUTHORITY ASSIGNMENT
```

Prefer staged and reversible action until the decision-changing conflict is resolved.

---

# 97. Conflict Resolution Template

```yaml
conflict_record:

  conflict_id:
  canonical_name:

  classification:
    type:
    severity:
    state:

  parties:
    - id:
      type:
      proposition:
      conclusion_class:
      source_refs: []

  envelope:
    scope:
    regime:
    time:
    version:
    units:
    definitions:
    measurement_method:

  provenance:
    lineage_refs: []
    independence_state:
    correlation_risk:

  contradiction:
    normalized_statement:
    shared_premises: []
    differing_premises: []
    hidden_dependencies: []

  hypotheses:
    - hypothesis_id:
      proposition:
      evidence_for: []
      evidence_against: []
      assumptions: []
      falsifiers: []

  discrimination:
    candidate_tests: []
    cheapest_high_information_test:
    result:

  resolution:
    state:
    conclusion_class:
    outcome:
    scope:
    regime:
    valid_from:
    valid_until:
    load_bearing_premises: []
    invalidation_conditions: []

  impact:
    affected_claims: []
    affected_rscfs: []
    affected_models: []
    affected_decisions: []

  governance:
    proposed_by:
    reviewed_by:
    committed_by:
    committed_at:

  gaps: []
```

---

# 98. Adversarial Test Suite

A mature conflict system SHOULD survive:

```text
100 COPIES SUPPORT A
1 INDEPENDENT SOURCE SUPPORTS B
→ DO NOT TREAT AS 100:1 INDEPENDENT EVIDENCE

A VALID IN R₁
B VALID IN R₂
→ CONDITIONAL, NOT CONTRADICTORY

OLD CANON A
NEW GOVERNED CANON B
→ SUPERSESSION WITH HISTORY PRESERVED

NEW FILE NAMED v4.4
OLD FILE NAMED v3.0
NO VERIFIED LINEAGE
→ VERSION RELATION UNKNOWN/GAP

TWO AGENTS AGREE
SAME ROOT SOURCE
→ NOT INDEPENDENT CONFIRMATION

TWO PAPERS DISAGREE
SAME DATASET
→ CORRELATION RISK VISIBLE

MODEL PREDICTS X
OBSERVATION SHOWS Y
→ MODEL/OBSERVATION CONFLICT PRESERVED

AUTHORITY SAYS X
EMPIRICAL DATA SAYS Y
→ GOVERNANCE AND EMPIRICAL QUESTIONS SEPARATED

CLAIM A CORRELATES X WITH Y
CLAIM B DENIES CAUSATION
→ MAY NOT BE A CONFLICT

SOURCE A STALE
SOURCE B CURRENT
ENVIRONMENT CHANGED
→ CHECK REGIME SHIFT BEFORE INVALIDATING HISTORY

CONFLICT RESOLVED UNDER SCOPE S
QUERY MOVES OUTSIDE S
→ RESOLUTION NOT REUSED AUTOMATICALLY

LOAD-BEARING SOURCE INVALIDATED
→ ONLY DEPENDENT CONCLUSIONS INVALIDATED

NO DISCRIMINATING EVIDENCE
→ COMPETING / UNKNOWN, NOT FORCED WINNER
```

---

# 99. Conflict Metrics

Potential observability metrics:

```text
open_conflict_count
critical_conflict_count
decision_relevant_conflict_count
competing_hypothesis_count
authority_conflict_count
canon_conflict_count
provenance_conflict_count
scope_conflict_count
regime_conflict_count
stale_evidence_conflict_count
reopened_conflict_count
average_resolution_age
conflicts_with_unknown_independence
conflicts_without_discriminating_test
```

Metrics do not themselves establish correctness.

---

# 100. Conflict and RSCF

A conflict may bind directly to RSCF structures.

Conceptually:

```text
RSCF-A
↘
 CONFLICT
↗
RSCF-B
```

The conflict record should preserve:

```text
claims
premises
evidence
dependencies
scope
regime
falsifiers
```

without duplicating entire RSCFs unnecessarily.

---

# 101. Proof Capsule Reuse

A resolved conflict may be reused only while:

```text
dependencies remain valid
scope remains compatible
regime remains compatible
freshness remains valid
provenance assumptions remain valid
no material contradiction has appeared
```

Otherwise reopen or revalidate.

---

# 102. Conflict and Persistent Provenance

Conflict history must survive resolution.

```text
CONFLICT
→ RESOLUTION
```

must not become:

```text
ONLY RESOLUTION EXISTS
```

Historical disagreement is part of provenance.

---

# 103. Conflict and Canon Provenance

Canon provenance should be able to answer:

```text
WHICH CONFLICT CAUSED THIS CHANGE?

WHICH PRIOR CANON WAS CHALLENGED?

WHAT EVIDENCE DISCRIMINATED?

WHAT WAS SUPERSEDED?

WHAT REMAINS VALID?
```

---

# 104. Conflict and Source Registry

Relationship:

```text
SOURCE_REGISTRY
↓
SOURCE IDENTITIES

SOURCE_LINEAGE
↓
ANCESTRY

CONFLICT_REGISTRY
↓
INCOMPATIBILITIES

RSCF / CLAIM LAYER
↓
EPISTEMIC CONCLUSIONS
```

---

# 105. Conflict and Authority

Where conflict concerns authority:

```text
AUTHORITY_CANON
LAW_HIERARCHY
CONTROL_PLANE_CANON
```

should govern resolution.

Agents and runtime components may detect or propose resolution but must not silently manufacture authority.

---

# 106. Conflict and Runtime

Runtime MAY:

```text
detect
route
queue
surface
block
request review
```

conflicts according to policy.

Runtime must not erase unresolved canonical conflicts for execution convenience.

---

# 107. Conflict and Agents

Agents MAY:

```text
detect conflicts
construct hypotheses
find evidence
propose discriminating tests
propose resolutions
```

But:

```text
AGENT PROPOSAL
!=
CANON COMMIT
```

---

# 108. Conflict and Human Governance

Some conflicts cannot be resolved purely epistemically.

Examples:

```text
policy preference
institutional authority allocation
risk tolerance
ethical trade-off
resource priority
```

The registry should distinguish:

```text
EVIDENCE QUESTION
```

from:

```text
GOVERNANCE DECISION
```

---

# 109. Current Canonical Gaps

The following remain `UNKNOWN/GAP` until separately populated and validated:

```text
complete AMOS conflict inventory
complete conflict IDs
complete historical contradiction graph
complete canon supersession conflict history
complete provenance conflict inventory
complete authority conflict inventory
complete RSCF conflict bindings
complete model competition registry
complete conflict severity assignments
complete discriminating-test inventory
complete resolution proof capsules
complete conflict reopening policy implementation
complete runtime conflict routing implementation
complete observability implementation
complete automated contradiction detection
```

This artifact must not invent those records.

---

# 110. Promotion Gate

This file defines the canonical conflict-management contract.

Actual conflict entries should be promoted through:

```text
DETECTION
→ REGISTRATION
→ CLASSIFICATION
→ NORMALIZATION
→ PROVENANCE
→ SCOPE
→ REGIME
→ INDEPENDENCE
→ HYPOTHESIS CONSTRUCTION
→ DISCRIMINATION
→ ADVERSARIAL CHALLENGE
→ RESOLUTION / COMPETING / UNKNOWN
→ GOVERNED COMMIT
```

No unresolved critical gap should be hidden merely to achieve apparent completion.

---

# 111. RSCF Node

```RSCF-NODE
node_id: AMOS-OS-CONFLICT-REGISTRY
node_type: canonical_conflict_registry
domain: AMOS_OS_CANON
functional_type: ConflictRegistry
lifecycle_stage: CanonGovernance
claim_class: AMOS_MODEL

RSCF-RELATIONS:
  - INDEXED_BY: 00_ROOT_MOC|AMOS MOC
  - INDEXED_BY: CANON_MAP
  - GOVERNED_BY: AMOS_CORE_LAWS
  - CONSTRAINED_BY: INVARIANT_REGISTRY
  - CONSTRAINED_BY: LAW_HIERARCHY
  - PROVENANCE_GOVERNED_BY: CANON_PROVENANCE
  - SOURCE_IDENTITY_FROM: SOURCE_REGISTRY
  - LINEAGE_FROM: SOURCE_LINEAGE
  - TERMINOLOGY_FROM: CANONICAL_GLOSSARY
  - AUTHORITY_GOVERNED_BY: AUTHORITY_CANON
  - CONTROLLED_BY: CONTROL_PLANE_CANON
  - SUPPORTS: HML_CANON
  - SUPPORTS: PERSISTENCE_CANON
  - PRESERVES_HISTORY_WITH: README
```

---

# 112. Canonical Summary

```text
DETECT
↓
PRESERVE
↓
CLASSIFY
↓
NORMALIZE
↓
CHECK SCOPE
↓
CHECK REGIME
↓
CHECK TIME
↓
CHECK VERSION
↓
CHECK PROVENANCE
↓
CHECK INDEPENDENCE
↓
BUILD COMPETING HYPOTHESES
↓
IDENTIFY LOAD-BEARING DIFFERENCE
↓
TEST CHEAPEST HIGH-INFORMATION DISCRIMINATOR
↓
ADVERSARIALLY CHALLENGE
↓
RESOLVE
OR
CONDITION
OR
PRESERVE COMPETING
OR
UNKNOWN/GAP
↓
TRACK DEPENDENCIES
↓
REOPEN WHEN INVALIDATED
```

Core laws:

```text
CONFLICT DETECTED != CONFLICT RESOLVED

DISAGREEMENT != CONTRADICTION

DIFFERENT SCOPE != CONTRADICTION

DIFFERENT REGIME != CONTRADICTION

SOURCE COUNT != INDEPENDENT EVIDENCE COUNT

REPETITION != CONFIRMATION

AUTHORITY != EMPIRICAL TRUTH

POPULARITY != AUTHORITY

MODEL AGREEMENT != VERIFICATION

AGENT AGREEMENT != INDEPENDENT CONFIRMATION

ABSENCE OF CONTRADICTION != PROOF

CORRELATION != CAUSATION

STRUCTURAL SIMILARITY != CAUSATION

NEWER != AUTOMATICALLY AUTHORITATIVE

SUPERSESSION != HISTORICAL ERASURE

COMPETING != FAILURE

UNKNOWN/GAP != PASS

PROPOSAL != COMMIT
```

Canonical objective:

```text
NEVER HIDE A MATERIAL CONTRADICTION.

NEVER COUNT COPIES AS INDEPENDENT SUPPORT.

NEVER FORCE CONVERGENCE WITHOUT
DISCRIMINATING EVIDENCE.

FIRST ASK WHETHER THE APPARENT CONFLICT
IS REALLY A DIFFERENCE IN:

SCOPE,
REGIME,
TIME,
VERSION,
DEFINITION,
UNIT,
MEASUREMENT,
OR PROVENANCE.

IF A REAL CONFLICT REMAINS,
PRESERVE EVERY MATERIAL HYPOTHESIS.

TEST THE PREMISE MOST LIKELY
TO FLIP THE RESULT.

RESOLVE ONLY TO THE SCOPE
SUPPORTED BY THE EVIDENCE.

INVALIDATE ONLY DEPENDENT DESCENDANTS.

PRESERVE HISTORICAL CONFLICT
AS PROVENANCE.

WHEN THE EVIDENCE CANNOT DISCRIMINATE:

COMPETING.

WHEN CRITICAL INFORMATION IS MISSING:

UNKNOWN/GAP.
```

## Related

[[README]] ·
00_ROOT_MOC|AMOS MOC ·
[[ARCHITECTURE]] ·
[[SYSTEM_MAP]] ·
[[NEURAL_NETWORK]] ·
[[CANON_MAP]] ·
[[AMOS_CORE_LAWS]] ·
[[INVARIANT_REGISTRY]] ·
[[LAW_HIERARCHY]] ·
[[CANON_PROVENANCE]] ·
[[SOURCE_REGISTRY]] ·
[[SOURCE_LINEAGE]] ·
[[CANONICAL_GLOSSARY]] ·
ALIASES ·
[[DEPRECATED_TERMS]] ·
[[AUTHORITY_CANON]] ·
[[CONTROL_PLANE_CANON]] ·
[[HML_CANON]] ·
[[PERSISTENCE_CANON]] ·
11_KNOWLEDGE/00_AMOS_Full_Brain_OS_Architecture ·
[[AUTHORITATIVE_STATE]] ·
README ·
README

```text
```

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
**MOC:** [[08_SUPERSESSION_MOC]]
