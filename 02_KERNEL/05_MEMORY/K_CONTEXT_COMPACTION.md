---
title: K CONTEXT COMPACTION
type: action
source: 02_KERNEL/05_MEMORY
artifact_id: AMOS-OS-K-CONTEXT-COMPACTION
canonical_name: K_CONTEXT_COMPACTION
artifact_type: kernel_context_compaction_contract
status: AMOS_MODEL
conclusion_class: AMOS_MODEL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
plane: KERNEL
kernel_family: CONTEXT
scope: AMOS_OS
updated: 2026-08-26
tags:
- amos-os
- kernel
- core
- canon-group/tech-ai
- kernel/context
- kernel/context-compaction
- kernel/provenance
- kernel/dependency
- kernel/epistemics
- kernel/recovery
- rscf/claim
- rscf/provenance
- topic/compaction
- topic/context-window
- topic/information-preservation
- topic/dependency-closure
- topic/lossy-compression
- topic/retrieval
- canon/kernel
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# K CONTEXT COMPACTION

> **AMOS Core target:** `v4.4`
> **Origin architect / steward:** Trang Phan
> **Plane:** `02_KERNEL`
> **Status:** `AMOS_MODEL`
> **Conclusion class:** `AMOS_MODEL`

## Purpose

`K_CONTEXT_COMPACTION` defines the kernel contract for reducing active reasoning context while preserving the information required to maintain epistemic integrity, dependency validity, provenance recoverability, contradiction visibility, causal discipline, and continuation correctness.

Context compaction exists because active context is finite while AMOS knowledge, evidence, history, and dependency graphs may be much larger.

The objective is therefore not:

```text
KEEP EVERYTHING ACTIVE
```

nor:

```text
MAKE THE CONTEXT AS SMALL AS POSSIBLE
```

but:

```text
PRESERVE THE
SMALLEST SUFFICIENT
REASONING STATE
```

subject to integrity constraints.

Core firewall:

```text
COMPACTION != DELETION
SUMMARY != SOURCE
SUMMARY != CANON
COMPRESSION != VALIDATION
OMISSION != INVALIDATION
NOT_IN_ACTIVE_CONTEXT != UNKNOWN
NOT_IN_ACTIVE_CONTEXT != FALSE
RETRIEVABLE != CURRENTLY_LOADED
TOKEN_SAVING != INTEGRITY
FLUENCY != SEMANTIC_PRESERVATION
```

---

## 1. Core Law

AMOS context compaction is governed by:

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

Therefore:

```text
TOKEN_REDUCTION
```

may never justify loss of a load-bearing fact, unresolved contradiction, provenance dependency, authority boundary, falsifier, scope condition, or recovery pointer.

---

## 2. Context Model

For reasoning operation `q`, define active context:

```text
C_q
```

as the currently loaded subset of information available to the operation.

Conceptually:

```text
C_q = {
    objective,
    scope,
    constraints,
    active_claims,
    premises,
    evidence_refs,
    provenance,
    dependencies,
    competing_hypotheses,
    contradictions,
    regime,
    freshness,
    authority,
    decisions,
    recovery_refs
}
```

This is an architectural representation.

It does not assert that a runtime literally stores context in this exact object form.

---

## 3. Context Is Not Knowledge

```text
ACTIVE_CONTEXT != KNOWLEDGE_BASE
ACTIVE_CONTEXT != MEMORY
ACTIVE_CONTEXT != WORLD_MODEL
ACTIVE_CONTEXT != CANON
```

Context is an operational working set.

Knowledge may exist outside active context and remain retrievable.

---

## 4. Compaction Function

Conceptually:

```text
C'
=
Compact(C, Q, D, P)
```

where:

```text
C  = current context
Q  = active objective/query
D  = dependency requirements
P  = integrity policy
C' = compacted context
```

Required condition:

```text
SUFFICIENCY(C', Q)
=
TRUE
```

before the compacted state may replace the larger active state.

---

## 5. Smallest Sufficient Proof Scope

Compaction should preserve the smallest context capable of supporting the current proof or decision.

Conceptually:

```text
C*
=
argmin |C'|
```

subject to:

```text
CLAIM_SUFFICIENCY(C')
∧
DECISION_SUFFICIENCY(C')
∧
ACTION_SUFFICIENCY(C')
∧
INTEGRITY(C')
```

This is a design objective, not a claim of universal computational optimality.

---

## 6. Preservation Classes

Context objects should be classified before removal.

Recommended classes:

```text
MUST_PRESERVE
PRESERVE_REFERENCE
RECONSTRUCTIBLE
DISCARDABLE
UNKNOWN
```

`UNKNOWN` must not default to `DISCARDABLE`.

---

## 7. MUST_PRESERVE

The active compacted context should retain information whose loss can materially alter reasoning.

Examples include:

```text
CURRENT OBJECTIVE
HARD CONSTRAINTS
LOAD-BEARING PREMISES
CURRENT CONCLUSION CLASS
UNRESOLVED CONTRADICTIONS
COMPETING HYPOTHESES
AUTHORITY BOUNDARIES
SCOPE CONDITIONS
REGIME CONDITIONS
CRITICAL FRESHNESS LIMITS
DECISION-CHANGING UNCERTAINTY
IRREVERSIBLE-ACTION WARNINGS
ACTIVE FALSIFIERS
```

---

## 8. Preserve by Reference

Large evidence objects need not remain fully loaded when a stable recovery reference is sufficient.

Conceptually:

```text
RAW_EVIDENCE
↓ COMPACT
{
    evidence_id,
    claim_supported,
    provenance_ref,
    scope,
    freshness,
    hash/version,
    retrieval_pointer
}
```

The raw evidence may then return to:

```text
DO_NOT_LOAD_UNLESS_REQUIRED
```

---

## 9. Reconstructible Content

Information may be removed from active context when it can be deterministically or safely reconstructed from retained state.

Required properties should include, where applicable:

```text
STABLE SOURCE
STABLE IDENTITY
KNOWN VERSION
VALID RETRIEVAL PATH
NO MATERIAL MUTATION RISK
NO LOST INTERPRETIVE DEPENDENCY
```

If reconstruction is uncertain:

```text
RECONSTRUCTIBLE = FALSE
```

or:

```text
UNKNOWN/GAP
```

---

## 10. Discardable Content

Content may be discarded from active context when it is neither load-bearing nor required for recovery.

Examples can include:

```text
REDUNDANT WORDING
DUPLICATE NON-INDEPENDENT RESTATEMENTS
RESOLVED EXPLORATORY BRANCHES
NON-LOAD-BEARING BACKGROUND
REGENERABLE PRESENTATION TEXT
LOW-VALUE INTERMEDIATE FORMAT
```

But semantic uniqueness must be tested before deletion.

---

## 11. Semantic Preservation

Compaction is valid only if meaning required for future reasoning survives.

For load-bearing proposition `p`:

```text
Meaning(p, C)
≈
Meaning(p, C')
```

within the required reasoning scope.

A shorter sentence is not necessarily an equivalent sentence.

---

## 12. Epistemic-Type Preservation

Compaction must preserve epistemic type.

The following transformation is invalid:

```text
SOURCE_CLAIM:
"Source A reports X"

↓ compact

"X is true"
```

Correct compaction retains:

```text
SOURCE_CLAIM(X, Source A)
```

until independently promoted.

---

## 13. Conclusion-Class Preservation

Compaction must preserve:

```text
VERIFIED
DERIVED
MODEL
CONDITIONAL
COMPETING
UNKNOWN/GAP
```

A `CONDITIONAL` claim must not become an unconditional claim because its assumptions were compacted away.

---

## 14. Provenance Preservation

For every load-bearing claim:

```text
CLAIM
↓
EVIDENCE
↓
SOURCE
```

must remain recoverable.

At minimum, compacted representation should preserve enough information to recover:

```text
SOURCE IDENTITY
SOURCE ANCESTRY
EVIDENCE IDENTITY
DEPENDENCY EDGE
VERSION / HASH WHEN AVAILABLE
```

---

## 15. Provenance Topology

Compaction must not flatten:

```text
SOURCE A
  ↓
REPORT B
  ↓
ARTICLE C
```

into:

```text
THREE INDEPENDENT SOURCES
```

Source ancestry remains material after compaction.

---

## 16. Sybil-Hardening Preservation

Duplicate descendants of one origin must remain recognizable as correlated evidence.

Thus:

```text
COMPACT({
  A→B,
  A→C,
  A→D
})
```

must not become:

```text
3 independent confirmations
```

---

## 17. Dependency Preservation

Load-bearing dependency edges must survive compaction.

If:

```text
P1
↓
P2
↓
C
```

then compacting away `P1` without retaining its dependency relationship may falsely make `C` appear independently established.

Required:

```text
DEPENDENCY(C, P2)
DEPENDENCY(P2, P1)
```

or an equivalent recoverable structure.

---

## 18. Dependency Closure

Before compaction, determine the dependency closure relevant to the active objective.

Conceptually:

```text
D*(Q)
=
all dependencies
capable of materially
changing Q
```

Objects outside this closure are stronger candidates for unloading.

---

## 19. Hidden Dependency Firewall

If dependency status is unknown:

```text
DEPENDENCY(x,Q) = UNKNOWN
```

AMOS must not silently assume:

```text
DEPENDENCY(x,Q) = FALSE
```

Compaction should escalate until the ambiguity is resolved or preserved explicitly.

---

## 20. Contradiction Preservation

If:

```text
CLAIM A
```

and:

```text
CLAIM ¬A
```

remain unresolved, compaction must retain the conflict.

Invalid:

```text
A
¬A

↓ compact

A
```

or:

```text
¬A
```

merely because one representation is easier to summarize.

---

## 21. Competing-Hypothesis Preservation

For:

```text
H1
H2
H3
```

with unresolved competition, compaction should preserve:

```text
COMPETING {
  H1,
  H2,
  H3
}
```

plus the discriminating evidence required to resolve them.

---

## 22. Assumption Preservation

Assumptions that bound a conclusion must survive.

Invalid:

```text
IF A AND B:
  C

↓ compact

C
```

Correct:

```text
C
CLASS: CONDITIONAL
REQUIRES: A, B
```

---

## 23. Scope Preservation

If:

```text
VALID(C, Ω)
```

then compacted context must not reduce this to:

```text
VALID(C)
```

when scope `Ω` is material.

Applicability envelopes must survive.

---

## 24. Regime Preservation

If a conclusion is valid only under regime `R0`:

```text
VALID(C | R0)
```

then `R0` is load-bearing.

Compaction must not silently create:

```text
VALID(C | ANY_REGIME)
```

---

## 25. Freshness Preservation

Time-sensitive claims require freshness metadata.

Conceptually:

```yaml
claim:
  value:
  observed_at:
  valid_until:
  regime_epoch:
```

Compaction that preserves the value but removes its expiration condition is invalid.

---

## 26. Causal-Type Preservation

Compaction must preserve distinctions among:

```text
ASSOCIATION
CORRELATION
MECHANISM
CAUSE
ENABLING CONDITION
NECESSARY CONDITION
SUFFICIENT CONDITION
MEDIATION
CONFOUNDING
FEEDBACK
```

Invalid:

```text
A correlated with B

↓ compact

A causes B
```

---

## 27. Structural-Similarity Firewall

Compaction must not turn:

```text
A structurally resembles B
```

into:

```text
A and B share the same mechanism
```

Structural mappings remain `MODEL` unless independently validated.

---

## 28. Quantitative Preservation

Where a numeric value is load-bearing, retain:

```text
VALUE
UNIT
UNCERTAINTY
MEASUREMENT METHOD
SCOPE
TIME
```

when material.

Invalid:

```text
10 ± 4 ms
```

becoming:

```text
10 ms exactly
```

---

## 29. Unit Preservation

Compaction must never remove units where they are required for interpretation.

```text
10
```

is not equivalent to:

```text
10 ms
```

or:

```text
10 kg
```

---

## 30. Identity Preservation

Stable entity identity must survive name compression.

```text
ENTITY_ID != DISPLAY_NAME
```

If two objects share a name, compaction must not merge them without justified identity resolution.

---

## 31. Authority Preservation

Context compaction must preserve who or what has authority to:

```text
PROPOSE
VALIDATE
APPROVE
COMMIT
EXECUTE
ROLL BACK
```

Core firewall:

```text
CAPABILITY != AUTHORITY
```

Removing the authority boundary can convert harmless capability into unsafe implied permission.

---

## 32. Proposal/Commit Firewall

Invalid compaction:

```text
Agent proposed change X.
Commit authority has not approved.

↓ compact

Change X approved.
```

Required distinction:

```text
PROPOSAL != COMMIT
```

must survive every compaction boundary.

---

## 33. Tool/Permission Firewall

Likewise:

```text
TOOL AVAILABLE
```

must not compact into:

```text
TOOL AUTHORIZED
```

because:

```text
TOOL != PERMISSION
```

---

## 34. Decision Preservation

When a decision has been made, compacted context should preserve:

```text
DECISION
RATIONALE
LOAD-BEARING PREMISES
AUTHORITY
TIME
SCOPE
REVERSIBILITY
INVALIDATION CONDITIONS
```

when needed for continuation or audit.

---

## 35. Decision vs Evidence

Compaction must not convert:

```text
DECISION:
Use model M
```

into:

```text
FACT:
Model M is correct
```

A decision can be rational under uncertainty without making its premises true.

---

## 36. Recovery Pointer

Every compacted-away load-bearing evidence object should have a recovery route when feasible.

Conceptually:

```yaml
recovery_ref:
  object_id:
  source:
  location:
  version:
  hash:
  retrieval_method:
```

---

## 37. Lossless vs Lossy Compaction

Two major classes:

```text
LOSSLESS COMPACTION
LOSSY COMPACTION
```

Lossless compaction preserves all semantically relevant information.

Lossy compaction intentionally removes some information judged non-load-bearing.

Lossy compaction requires stronger integrity checks.

---

## 38. Lossy Compaction Gate

Before lossy compaction:

```text
[ ] objective known
[ ] dependency closure known
[ ] load-bearing premises identified
[ ] provenance retained
[ ] contradictions retained
[ ] competing hypotheses retained
[ ] scope retained
[ ] regime retained
[ ] freshness retained
[ ] authority retained
[ ] recovery route exists where required
```

If not:

```text
DO NOT COMPACT
```

or compact conservatively.

---

## 39. RSCF Compaction

An RSCF may be compacted into a proof capsule.

Conceptually:

```yaml
proof_capsule:
  claim:
  class:
  load_bearing_premises:
  evidence_refs:
  provenance:
  scope:
  temporal_validity:
  regime:
  dependencies:
  competing_explanations:
  falsifiers:
  confidence_ceiling:
```

This capsule can replace large active evidence only while its dependencies remain valid.

---

## 40. Proof Capsule Reuse

A proof capsule may be reused when:

```text
DEPENDENCIES VALID
∧
SCOPE COMPATIBLE
∧
REGIME COMPATIBLE
∧
FRESHNESS VALID
∧
NO NEW MATERIAL CONFLICT
```

Otherwise:

```text
REVALIDATE
```

---

## 41. Capsule Invalidation

If premise `p` fails:

```text
INVALID(p)
```

then:

```text
INVALIDATE(
  capsules dependent on p
)
```

not:

```text
INVALIDATE ALL CONTEXT
```

---

## 42. Fractal Compaction

AMOS context compaction follows H/M/L structure.

```text
RAW DETAIL
↓
L CAPSULE
↓
M CAPSULE
↓
H CAPSULE
↓
BOOTSTRAP
```

Each higher layer should retain sufficient pointers to descend when required.

---

## 43. H-Level Context

H-level context should preserve:

```text
OBJECTIVE
DOMAIN
MAJOR CLAIMS
MAJOR CONSTRAINTS
CRITICAL CONFLICTS
KEY DEPENDENCIES
AUTHORITY
DECISION STATE
```

It should not contain unnecessary raw evidence.

---

## 44. M-Level Context

M-level context preserves subsystem-level structures required to resolve material uncertainty.

Examples:

```text
MECHANISM
SUBSYSTEM STATE
COMPETING MODELS
DEPENDENCY BRANCH
PROVENANCE CLUSTER
```

---

## 45. L-Level Context

L-level context contains detailed evidence, measurements, records, calculations, or source-specific reasoning.

It is loaded only when needed.

```text
L_DETAIL
=
DO_NOT_LOAD_UNLESS_REQUIRED
```

by default.

---

## 46. Raw Evidence

Raw evidence is the deepest retrieval layer.

It should be loaded when:

```text
PROVENANCE NEEDS VERIFICATION
SUMMARY IS AMBIGUOUS
CONTRADICTION EXISTS
PREMISE IS CHALLENGED
FRESHNESS IS UNCLEAR
SCOPE IS UNCLEAR
HIGH-STAKES VALIDATION REQUIRES IT
```

---

## 47. Compaction Cascade

Conceptually:

```text
RAW EVIDENCE
↓
EVIDENCE CAPSULE
↓
RSCF
↓
SUBSYSTEM CAPSULE
↓
DOMAIN CAPSULE
↓
BOOTSTRAP CONTEXT
```

Each step reduces active detail while preserving dependency recoverability.

---

## 48. Expansion

Compaction must be reversible where integrity requires.

Conceptually:

```text
H
↓ need detail
M
↓ need evidence
L
↓ challenge
RAW
```

This is contextual expansion.

---

## 49. Expansion Trigger

Expand when:

```text
CLAIM CHALLENGED
CONTRADICTION DETECTED
PROVENANCE AMBIGUOUS
DEPENDENCY UNKNOWN
SCOPE MISMATCH
REGIME CHANGE
FRESHNESS FAILURE
CAUSAL CLAIM ESCALATES
DECISION STAKES INCREASE
```

---

## 50. Compaction Trigger

Compaction is appropriate when:

```text
DETAIL NO LONGER DECISION-RELEVANT
BRANCH RESOLVED
RAW EVIDENCE HAS VALID CAPSULE
DEPENDENCY CLOSURE ESTABLISHED
CONTEXT PRESSURE INCREASES
PHASE TRANSITION OCCURS
HANDOFF REQUIRES STABLE STATE
```

---

## 51. Decision-Changing Uncertainty

Before compacting, identify uncertainty that could change:

```text
CLAIM
DECISION
ACTION
```

Such uncertainty remains active until resolved or explicitly represented.

---

## 52. Uncertainty Vector Preservation

When material:

```text
U = {
  evidence,
  model,
  scope,
  temporal,
  causal,
  execution,
  provenance_independence
}
```

Compaction must not collapse these dimensions into a misleading scalar.

---

## 53. Confidence Preservation

Invalid:

```text
confidence: 0.62
```

becoming:

```text
likely true
```

if the number was conditional on material assumptions omitted from the summary.

Confidence requires its dependency envelope.

---

## 54. Confidence Ceiling Preservation

If:

```text
CONF(C)
≤
CONF(P)
```

because `P` is load-bearing, compacting away `P` must not allow `C` to gain confidence.

Compaction cannot create evidence.

---

## 55. Evidence Independence Preservation

If evidence objects share ancestry, compacted summaries should retain the correlation.

Conceptually:

```yaml
evidence_cluster:
  origin: SOURCE_A
  descendants:
    - SOURCE_B
    - SOURCE_C
  independence: correlated
```

---

## 56. Duplicate Removal

Duplicate evidence may be compacted aggressively only when duplicate status is established.

```text
DUPLICATE
!=
INDEPENDENT CORROBORATION
```

Removing duplicates must not remove genuinely independent confirmation.

---

## 57. Contradiction Compression

Multiple contradictions may be represented compactly:

```yaml
conflict:
  proposition: X
  positions:
    - claim: X
      support: [...]
    - claim: NOT_X
      support: [...]
  status: UNRESOLVED
```

This preserves the conflict without retaining every surrounding sentence.

---

## 58. Branch Compaction

Exploratory branches may be compacted after resolution.

Conceptually:

```text
BRANCH A → rejected because F1
BRANCH B → retained because E1,E2
BRANCH C → unresolved
```

Preserve rejection reasons when they prevent future repetition of failed paths.

---

## 59. Failed-Path Memory

Do not discard the reason a reasoning path failed if the same path could otherwise be retried.

Preserve:

```text
PATH
FAILURE CONDITION
EVIDENCE
RETRY CONDITION
```

Core rule:

```text
DO NOT REPEAT
A FAILED PATH
WITHOUT CHANGED EVIDENCE
```

---

## 60. Resolved Branches

A resolved branch may be compacted to:

```yaml
branch:
  result:
  reason:
  dependencies:
  reopen_if:
```

This prevents unnecessary recomputation.

---

## 61. Causal Branch Preservation

If multiple causal explanations remain viable:

```text
A → B
B → A
C → {A,B}
```

compaction must preserve the alternatives until discriminating evidence exists.

---

## 62. Falsifier Preservation

For important claims, retain the cheapest meaningful falsifier or invalidation condition.

Example:

```yaml
claim:
  value: C
  falsifier: observation F
```

This enables efficient future revalidation.

---

## 63. Sensitivity Preservation

The smallest premise capable of flipping a conclusion should survive compaction.

Conceptually:

```text
S* = decision-flipping premise
```

If `S*` disappears, future reasoning may falsely treat a fragile conclusion as robust.

---

## 64. High-Stakes Compaction

For:

```text
LEGAL
FINANCIAL
HEALTH
SAFETY
SECURITY
INSTITUTIONAL
IRREVERSIBLE
```

decisions, compaction should preserve more evidence and stronger recovery paths.

Compression aggressiveness decreases as irreversible risk increases.

---

## 65. Reversibility Principle

Prefer compaction that is:

```text
REVERSIBLE
AUDITABLE
TRACEABLE
REHYDRATABLE
```

over destructive compression.

---

## 66. Rehydration

Rehydration reconstructs required active context from compacted state.

Conceptually:

```text
CAPSULE
+
RECOVERY REFERENCES
+
DEPENDENCY GRAPH
→
REHYDRATED CONTEXT
```

Rehydration must not invent missing detail.

---

## 67. Rehydration Failure

If required source material cannot be recovered:

```text
REHYDRATION = FAILED
```

then affected claims should become:

```text
UNKNOWN/GAP
```

or be downgraded according to surviving evidence.

---

## 68. Version Preservation

Where source evolution matters, compacted references should preserve:

```text
VERSION
REVISION
HASH
EPOCH
```

when available.

A pointer to a mutable source without version identity may not be sufficient for reproducibility.

---

## 69. Mutable-Source Firewall

If source `S` can change:

```text
REF(S)
```

does not guarantee future recovery of the same evidence.

Where material, preserve:

```text
REF + VERSION/HASH
```

or persistent evidence.

---

## 70. Temporal Ordering

Context compaction must preserve event ordering when causally or operationally significant.

Invalid:

```text
A occurred
then B
```

becoming an unordered set if sequence affects reasoning.

---

## 71. Epoch Boundaries

When state crosses an epoch boundary:

```text
EPOCH_n
→
EPOCH_n+1
```

compaction must preserve which conclusions belong to which epoch.

This is particularly important for:

```text
POLICY
CAUSAL STATE
PROVENANCE
AUTHORITY
COMMIT STATE
```

---

## 72. Persistent Provenance

Compaction of active context must not imply compaction of persistent provenance.

```text
ACTIVE CONTEXT REDUCTION
!=
PROVENANCE DELETION
```

Persistent lineage should remain available according to governance policy.

---

## 73. MVCC/CAS Conceptual Compatibility

Where runtime/state layers use versioned-state concepts, compacted context should preserve the version assumptions against which reasoning occurred.

Conceptually:

```text
READ VERSION V
↓
REASON
↓
COMMIT ATTEMPT
```

must not silently become:

```text
REASONING VALID FOR CURRENT STATE
```

if the state advanced.

---

## 74. Stale-Context Detection

Before using a compacted capsule:

```text
CURRENT_VERSION
?=
CAPSULE_VALIDATION_VERSION
```

If relevant state changed, revalidation may be required.

---

## 75. Atomic Multi-RSCF Reasoning

When a conclusion depends jointly on multiple RSCFs:

```text
R1
R2
R3
↓
C
```

compaction must preserve their joint dependency.

It must not make `C` appear independently supported by any single RSCF.

---

## 76. Atomicity Firewall

If:

```text
C requires {R1,R2,R3}
```

then:

```text
R1 alone
```

must not be sufficient after compaction unless separately proven.

---

## 77. Context Handoff

When reasoning passes between agents, workers, processes, or sessions, the handoff capsule should preserve:

```text
OBJECTIVE
CURRENT STATE
DECISIONS
OPEN QUESTIONS
LOAD-BEARING PREMISES
PROVENANCE
DEPENDENCIES
CONTRADICTIONS
COMPETING HYPOTHESES
AUTHORITY
NEXT SAFE ACTION
```

---

## 78. Handoff Firewall

A handoff summary is not automatically authoritative.

```text
HANDOFF_SUMMARY != CANON
```

The receiver must retain the ability to inspect underlying evidence when necessary.

---

## 79. Agent Boundary

Agents may compact their working context.

They must not silently compact away control-plane restrictions.

```text
AGENT_CONTEXT_COMPACTION
```

cannot modify:

```text
AUTHORITY
POLICY
CANON
PERMISSIONS
COMMIT RIGHTS
```

---

## 80. Security Boundary

Secrets and sensitive material require separate handling.

Compaction must not accidentally transform:

```text
SECRET VALUE
```

into a persistent plaintext summary merely to preserve context.

Prefer secure reference where policy permits.

---

## 81. Security Preservation

Compaction must preserve security-relevant constraints such as:

```text
ACCESS BOUNDARY
AUTHORIZATION
DATA CLASSIFICATION
SECRET REFERENCE
THREAT CONDITION
```

without unnecessarily reproducing sensitive values.

---

## 82. Observability

Compaction operations should be observable enough to answer:

```text
WHAT WAS COMPACTED?
WHY?
WHAT WAS RETAINED?
WHAT WAS DROPPED?
WHAT CAN BE REHYDRATED?
WHICH CAPSULE REPLACED IT?
```

where governance requires auditability.

---

## 83. Compaction Trace

Conceptually:

```yaml
compaction_event:
  context_id:
  before_ref:
  after_ref:
  policy:
  preserved:
  referenced:
  discarded:
  unresolved:
  timestamp:
```

This is a contract shape, not proof of implementation.

---

## 84. Compaction Quality

Compaction quality is not measured solely by token reduction.

Conceptually:

```text
QUALITY
=
f(
  integrity,
  sufficiency,
  recoverability,
  dependency_preservation,
  provenance_preservation,
  contradiction_preservation,
  reduction
)
```

---

## 85. Unsafe Optimization

Any optimization that improves:

```text
LATENCY
TOKEN COUNT
MEMORY
THROUGHPUT
```

while weakening:

```text
FACTUAL SUPPORT
SCOPE CORRECTNESS
CONTRADICTION VISIBILITY
PROVENANCE RECOVERABILITY
CAUSAL DISCIPLINE
SAFETY
```

must be rejected or rolled back.

---

## 86. Compaction Fast Path

Aggressive local compaction is permitted when:

```text
DEPENDENCY CLOSURE ESTABLISHED
PROVENANCE INDEPENDENCE KNOWN
SCOPE STABLE
REGIME STABLE
FRESHNESS VALID
NO MATERIAL CONFLICT
NO GOVERNANCE IMPACT
RECOVERY PATH VALID
```

---

## 87. Escalation Conditions

Compaction should become more conservative when:

```text
DEPENDENCIES AMBIGUOUS
EVIDENCE CONFLICTS
PROVENANCE CORRELATED
SOURCE MUTABLE
PREMISE STALE
REGIME CHANGED
SCOPE UNCLEAR
CAUSAL CLAIM LOAD-BEARING
GOVERNANCE INVOLVED
IRREVERSIBLE ACTION POSSIBLE
RECOVERY PATH UNCERTAIN
```

---

## 88. Compaction Levels

Suggested conceptual levels:

```text
CC0 — NONE
CC1 — REDUNDANCY REMOVAL
CC2 — STRUCTURED SUMMARY
CC3 — PROOF CAPSULE
CC4 — FRACTAL H-LEVEL CAPSULE
```

Higher compaction requires stronger proof that removed detail is recoverable or non-load-bearing.

---

## 89. CC0 — None

Use when:

```text
CONTEXT SMALL
HIGH DETAIL REQUIRED
ACTIVE CONTRADICTION
UNRESOLVED DEPENDENCIES
```

---

## 90. CC1 — Redundancy Removal

Remove:

```text
DUPLICATE WORDING
FORMAT NOISE
NON-INDEPENDENT REPETITION
```

while retaining all unique semantic content.

---

## 91. CC2 — Structured Summary

Replace verbose material with structured representations while retaining:

```text
CLAIMS
TYPES
DEPENDENCIES
PROVENANCE
SCOPE
UNCERTAINTY
```

---

## 92. CC3 — Proof Capsule

Retain only the proof-relevant closure plus recovery references.

Appropriate when a conclusion has reached stable local sufficiency.

---

## 93. CC4 — Fractal Capsule

Retain high-level H structure with M/L retrieval pointers.

Appropriate for large persistent systems where deep detail is not continuously required.

---

## 94. Anti-Drift Rule

Repeated compaction cycles can create semantic drift.

Therefore:

```text
SUMMARY
↓
SUMMARY OF SUMMARY
↓
SUMMARY OF SUMMARY OF SUMMARY
```

should not be trusted indefinitely.

Periodic revalidation against stable source evidence is required when the claim remains load-bearing.

---

## 95. Source-Anchored Recompaction

Prefer:

```text
SOURCE
→ NEW CAPSULE
```

over:

```text
OLD CAPSULE
→ NEW CAPSULE
→ NEWER CAPSULE
```

when cumulative information loss becomes material.

---

## 96. Compression Debt

Repeated lossy compaction creates conceptual:

```text
COMPRESSION_DEBT
```

representing increased uncertainty about whether active summaries still preserve original semantics.

Compression debt should trigger rehydration/revalidation when material.

---

## 97. Drift Detection

Possible drift indicators:

```text
LOST QUALIFIERS
LOST NEGATION
LOST UNITS
LOST SOURCE TYPE
LOST SCOPE
LOST REGIME
LOST UNCERTAINTY
LOST ALTERNATIVE
LOST DEPENDENCY
INCREASED CONFIDENCE WITHOUT NEW EVIDENCE
```

Any of these should trigger review.

---

## 98. Negation Preservation

Negation is load-bearing.

Invalid:

```text
X does NOT imply Y
```

becoming:

```text
X implies Y
```

Compaction systems must explicitly protect polarity.

---

## 99. Exception Preservation

Rules with exceptions must preserve those exceptions when decision-relevant.

Invalid:

```text
RULE R
EXCEPT E
```

becoming:

```text
RULE R ALWAYS
```

---

## 100. Boundary Preservation

Hard boundaries should be preferentially retained verbatim where compact paraphrase could weaken them.

Examples:

```text
CAPABILITY != AUTHORITY
UNKNOWN/GAP != PASS
MODEL != AUTHORITY
PROPOSAL != COMMIT
```

---

## 101. Compaction Invariants

```text
CC-01
COMPACTION MUST NOT CREATE NEW EVIDENCE

CC-02
COMPACTION MUST NOT INCREASE CLAIM CLASS

CC-03
COMPACTION MUST NOT INCREASE CONFIDENCE WITHOUT NEW SUPPORT

CC-04
LOAD-BEARING PREMISES MUST REMAIN ACTIVE OR RECOVERABLE

CC-05
PROVENANCE MUST REMAIN RECOVERABLE

CC-06
SOURCE ANCESTRY MUST NOT BE FLATTENED

CC-07
CORRELATED SOURCES MUST NOT BECOME INDEPENDENT SOURCES

CC-08
UNRESOLVED CONTRADICTIONS MUST REMAIN VISIBLE

CC-09
COMPETING HYPOTHESES MUST NOT BE SILENTLY COLLAPSED

CC-10
SCOPE CONDITIONS MUST SURVIVE

CC-11
REGIME CONDITIONS MUST SURVIVE

CC-12
FRESHNESS CONDITIONS MUST SURVIVE

CC-13
CAUSAL TYPE MUST SURVIVE

CC-14
EPISTEMIC TYPE MUST SURVIVE

CC-15
AUTHORITY BOUNDARIES MUST SURVIVE

CC-16
PROPOSAL MUST NOT BECOME COMMIT

CC-17
TOOL CAPABILITY MUST NOT BECOME PERMISSION

CC-18
UNKNOWN/GAP MUST NOT BECOME PASS

CC-19
NEGATION MUST SURVIVE

CC-20
LOAD-BEARING UNITS MUST SURVIVE

CC-21
ENTITY IDENTITY MUST SURVIVE

CC-22
DEPENDENCY EDGES MUST SURVIVE OR REMAIN RECOVERABLE

CC-23
FAILED-PATH CONDITIONS MUST BE RETAINED WHEN NEEDED TO PREVENT REPEAT FAILURE

CC-24
LOSSY COMPACTION MUST BE REVERSIBLE WHERE INTEGRITY REQUIRES

CC-25
TOKEN SAVINGS MUST NEVER OVERRIDE INTEGRITY
```

---

## 102. Failure Modes

```text
SEMANTIC_DRIFT
PROVENANCE_LOSS
DEPENDENCY_LOSS
SCOPE_LOSS
REGIME_LOSS
FRESHNESS_LOSS
NEGATION_LOSS
UNIT_LOSS
AUTHORITY_LOSS
CAUSAL_TYPE_LOSS
EPISTEMIC_TYPE_LOSS
CONTRADICTION_ERASURE
HYPOTHESIS_COLLAPSE
CONFIDENCE_INFLATION
SOURCE_INDEPENDENCE_INFLATION
IDENTITY_COLLISION
STALE_CAPSULE_REUSE
UNRECOVERABLE_COMPACTION
SUMMARY_OF_SUMMARY_DRIFT
FAILED_PATH_FORGETTING
PROPOSAL_COMMIT_COLLAPSE
TOOL_PERMISSION_COLLAPSE
UNKNOWN_PASS_COLLAPSE
GLOBAL_CONTEXT_INVALIDATION
```

---

## 103. Required Tests

```text
SEMANTIC-PRESERVATION TEST
NEGATION-PRESERVATION TEST
UNIT-PRESERVATION TEST
EPISTEMIC-TYPE TEST
CONCLUSION-CLASS TEST
PROVENANCE-PRESERVATION TEST
SOURCE-ANCESTRY TEST
INDEPENDENCE-PRESERVATION TEST
DEPENDENCY-CLOSURE TEST
HIDDEN-DEPENDENCY TEST
CONTRADICTION-PRESERVATION TEST
MULTI-HYPOTHESIS TEST
SCOPE-PRESERVATION TEST
REGIME-PRESERVATION TEST
FRESHNESS-PRESERVATION TEST
CAUSAL-TYPE TEST
AUTHORITY-PRESERVATION TEST
PROPOSAL-COMMIT TEST
TOOL-PERMISSION TEST
RECOVERY-POINTER TEST
REHYDRATION TEST
VERSION-PRESERVATION TEST
STALE-CAPSULE TEST
RSCF-CAPSULE TEST
ATOMIC-MULTI-RSCF TEST
HML-COMPACTION TEST
FAILED-PATH TEST
SENSITIVITY-PRESERVATION TEST
FALSIFIER-PRESERVATION TEST
SUMMARY-DRIFT TEST
LOSSY-COMPACTION TEST
```

---

## 104. Negative Tests

```text
SOURCE CLAIM
→ COMPACT
→ VERIFIED FACT
MUST FAIL

CONDITIONAL CLAIM
→ COMPACT
→ UNCONDITIONAL CLAIM
MUST FAIL

CORRELATED SOURCES
→ COMPACT
→ INDEPENDENT SOURCES
MUST FAIL

A AND NOT-A
→ COMPACT
→ A ONLY
MUST FAIL

COMPETING H1/H2
→ COMPACT
→ H1 VERIFIED
MUST FAIL

VALID IN R0
→ COMPACT
→ VALID IN ALL REGIMES
MUST FAIL

VALID IN SCOPE A
→ COMPACT
→ UNIVERSAL
MUST FAIL

TOOL AVAILABLE
→ COMPACT
→ TOOL AUTHORIZED
MUST FAIL

PROPOSAL
→ COMPACT
→ COMMIT
MUST FAIL

UNKNOWN/GAP
→ COMPACT
→ PASS
MUST FAIL

10 ± 4 ms
→ COMPACT
→ 10 ms EXACT
MUST FAIL

A CORRELATES WITH B
→ COMPACT
→ A CAUSES B
MUST FAIL

FAILED PATH
→ COMPACT AWAY FAILURE
→ REPEAT IDENTICAL PATH
MUST FAIL

SUMMARY
→ REPEATED COMPACTION
→ HIGHER CONFIDENCE
MUST FAIL
```

---

## 105. Promotion Gate

Before promotion beyond `AMOS_MODEL`:

```text
[ ] context schema bound
[ ] compaction classes implemented
[ ] load-bearing dependency detection implemented
[ ] provenance preservation implemented
[ ] source ancestry preserved
[ ] contradiction preservation implemented
[ ] multi-hypothesis preservation implemented
[ ] scope preservation implemented
[ ] regime preservation implemented
[ ] freshness preservation implemented
[ ] epistemic typing preserved
[ ] causal typing preserved
[ ] authority boundaries preserved
[ ] proof capsules implemented
[ ] RSCF recovery pointers implemented
[ ] H/M/L rehydration implemented
[ ] stale-capsule detection implemented
[ ] semantic-drift detection tested
[ ] failed-path memory tested
[ ] lossy-compaction gate tested
[ ] recovery behavior tested
[ ] observability wired
[ ] security handling tested
[ ] unresolved critical gaps registered
```

Until evidenced:

```text
IMPLEMENTATION_STATUS = UNKNOWN/GAP
RUNTIME_COMPACTOR = UNKNOWN/GAP
AUTOMATED_DEPENDENCY_CLOSURE = UNKNOWN/GAP
AUTOMATED_SEMANTIC_EQUIVALENCE = UNKNOWN/GAP
PROOF_CAPSULE_RUNTIME = UNKNOWN/GAP
REHYDRATION_RUNTIME = UNKNOWN/GAP
FORMAL_VERIFICATION = UNKNOWN/GAP
EMPIRICAL_VALIDATION = UNKNOWN/GAP
```

---

## 106. Integrity Note

This artifact replaces the repository placeholder with an AMOS v4.4-aligned **context-compaction kernel architecture**.

It defines intended semantics for:

```text
CONTEXT REDUCTION
DEPENDENCY CLOSURE
PROOF CAPSULES
PROVENANCE PRESERVATION
CONTRADICTION PRESERVATION
MULTI-HYPOTHESIS PRESERVATION
SCOPE / REGIME / FRESHNESS
H/M/L COMPACTION
REHYDRATION
FAILED-PATH MEMORY
SEMANTIC DRIFT CONTROL
RECOVERY
```

It does **not** establish runtime implementation.

Therefore:

```text
DOCUMENT_CLASS = AMOS_MODEL
IMPLEMENTATION = UNKNOWN/GAP
EMPIRICAL_VALIDATION = UNKNOWN/GAP
FORMAL_VERIFICATION = UNKNOWN/GAP
RUNTIME_AUTHORITY = NONE
```

---

## 107. RSCF Node

```RSCF-NODE
node_id: AMOS-OS-K-CONTEXT-COMPACTION
node_type: kernel_context_compaction_contract
domain: AMOS_OS_KERNEL
functional_type: ContextCompactionKernel
lifecycle_stage: Architecture
claim_class: AMOS_MODEL

RSCF-RELATIONS:
  - ROOTED_IN: README
  - DEPENDENCY_BOUND_TO: DEPENDENCY_MAP

  - GOVERNED_BY: AMOS_CORE_LAWS
  - CONSTRAINED_BY: INVARIANT_REGISTRY
  - PRECEDENCE_GOVERNED_BY: LAW_HIERARCHY
  - PROVENANCE_GOVERNED_BY: CANON_PROVENANCE
  - SOURCE_LINEAGE_GOVERNED_BY: SOURCE_LINEAGE
  - CONFLICTS_BOUND_TO: CONFLICT_REGISTRY

  - INDEXED_BY: KERNEL_MAP
  - CONTEXT_BOUND_TO: K_CONTEXT_STATE
  - WORLD_MODEL_BOUND_TO: K_WORLD_MODEL
  - IDENTITY_BOUND_TO: K_IDENTITY
  - SYSTEM_STATE_BOUND_TO: K_SYSTEM_STATE
  - EVENT_BOUND_TO: K_EVENT_BUS
  - META_LOGIC_BOUND_TO: K_META_LOGIC
  - METACOGNITION_BOUND_TO: K_METACOGNITION
  - MULTI_HYPOTHESIS_BOUND_TO: K_MULTI_HYPOTHESIS
  - COUNTERFACTUAL_BOUND_TO: K_COUNTERFACTUAL
  - STRUCTURAL_REASONING_BOUND_TO: K_STRUCTURAL_REASONING
  - CAUSAL_CLOSURE_BOUND_TO: K_CAUSAL_CLOSURE
  - CAUSAL_EPOCH_BOUND_TO: K_CAUSAL_EPOCH

  - KNOWLEDGE_INTERACTION: 11_KNOWLEDGE/00_AMOS_Full_Brain_OS_Architecture
  - STATE_INTERACTION: README
  - SCHEMA_INTERACTION: README
  - OBSERVED_BY: README
  - SECURITY_CONSTRAINED_BY: README
  - VERIFIED_BY: README
```

---

## 108. Canonical Summary

```text
ACTIVE CONTEXT
↓
IDENTIFY OBJECTIVE
↓
IDENTIFY DECISION-CHANGING UNCERTAINTY
↓
COMPUTE RELEVANT DEPENDENCY CLOSURE
↓
CLASSIFY CONTENT
↓
PRESERVE LOAD-BEARING STATE
↓
CAPSULIZE LARGE EVIDENCE
↓
PRESERVE PROVENANCE + CONFLICT + SCOPE
↓
STORE RECOVERY REFERENCES
↓
COMPACT
↓
VALIDATE SUFFICIENCY
↓
CONTINUE REASONING
```

When deeper evidence becomes necessary:

```text
COMPACTED CONTEXT
↓
RECOVERY POINTER
↓
H
↓
M
↓
L
↓
RAW EVIDENCE
↓
REVALIDATE
```

Core laws:

```text
COMPACTION != DELETION
SUMMARY != SOURCE
SUMMARY != CANON
COMPRESSION != VALIDATION
NOT_LOADED != UNKNOWN
NOT_LOADED != FALSE
SOURCE_CLAIM != VERIFIED
MODEL != FACT
CAPABILITY != AUTHORITY
PROPOSAL != COMMIT
TOOL != PERMISSION
UNKNOWN/GAP != PASS
```

The decisive invariant is:

```text
AMOS MAY
FORGET WORDING.

AMOS MAY
UNLOAD DETAIL.

AMOS MAY
COLLAPSE
REDUNDANCY.

AMOS MAY NOT
COMPACT AWAY

A LOAD-BEARING PREMISE,
PROVENANCE,
DEPENDENCY,
CONTRADICTION,
COMPETING HYPOTHESIS,
SCOPE,
REGIME,
FRESHNESS CONDITION,
CAUSAL TYPE,
AUTHORITY BOUNDARY,
FALSIFIER,
OR RECOVERY PATH

WHEN ITS LOSS
CAN CHANGE
THE CLAIM,
DECISION,
OR ACTION.

CONTEXT
SHOULD BE
AS SMALL
AS POSSIBLE

BUT

NO SMALLER
THAN THE
PROOF REQUIRES.

WHEN DETAIL
IS NOT NEEDED,

UNLOAD IT.

WHEN DETAIL
BECOMES
LOAD-BEARING,

REHYDRATE IT.

WHEN RECOVERY
IS IMPOSSIBLE,

DO NOT
INVENT THE
MISSING STATE.

RETURN

UNKNOWN/GAP.
```

## Related

[[README]] ·
[[ARCHITECTURE]] ·
[[DEPENDENCY_MAP]] ·
[[AMOS_CORE_LAWS]] ·
[[INVARIANT_REGISTRY]] ·
[[LAW_HIERARCHY]] ·
[[CANON_PROVENANCE]] ·
[[SOURCE_LINEAGE]] ·
[[CONFLICT_REGISTRY]] ·
[[KERNEL_MAP]] ·
[[K_CONTEXT_STATE]] ·
[[K_WORLD_MODEL]] ·
[[K_IDENTITY]] ·
[[K_SYSTEM_STATE]] ·
[[K_EVENT_BUS]] ·
[[K_META_LOGIC]] ·
[[K_METACOGNITION]] ·
[[K_MULTI_HYPOTHESIS]] ·
[[K_COUNTERFACTUAL]] ·
[[K_STRUCTURAL_REASONING]] ·
[[K_CAUSAL_CLOSURE]] ·
[[K_CAUSAL_EPOCH]] ·
11_KNOWLEDGE/00_AMOS_Full_Brain_OS_Architecture ·
[[README]] ·
[[README]] ·
[[README]] ·
[[README]] ·
[[README]]

```text
```

---

[[00_ROOT_MOC]]|[[AMOS MOC]]

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
**MOC:** [[05_MEMORY_MOC]]
