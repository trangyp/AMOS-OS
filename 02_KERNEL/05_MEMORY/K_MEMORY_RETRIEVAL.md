---
title: K MEMORY RETRIEVAL
type: memory
source: 02_KERNEL/05_MEMORY
artifact_id: AMOS-OS-K-MEMORY-RETRIEVAL
canonical_name: K_MEMORY_RETRIEVAL
artifact_type: kernel_memory_retrieval_contract
status: AMOS_MODEL
conclusion_class: AMOS_MODEL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
plane: KERNEL
kernel_family: MEMORY
scope: AMOS_OS
updated: 2026-08-26
tags:
- amos-os
- kernel
- core
- canon-group/tech-ai
- kernel/memory
- kernel/memory-retrieval
- kernel/context
- kernel/provenance
- kernel/dependency
- kernel/conflict
- kernel/epistemic-integrity
- rscf/retrieval
- rscf/memory
- rscf/provenance
- rscf/dependency
- hml
- topic/selective-retrieval
- topic/dependency-closure
- topic/freshness
- topic/regime
- topic/context-relevance
- canon/kernel
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# K MEMORY RETRIEVAL

> **AMOS Core target:** `v4.4`  
> **Origin architect / steward:** Trang Phan  
> **Plane:** `02_KERNEL`  
> **Status:** `AMOS_MODEL`  
> **Conclusion class:** `AMOS_MODEL`

## Purpose

`K_MEMORY_RETRIEVAL` defines the kernel-level contract governing how AMOS locates, selects, validates, loads, ranks, expands, and reuses persistent memory.

Retrieval is not merely search.

AMOS retrieval must preserve epistemic type, provenance, dependency structure, scope, regime, freshness, conflicts, uncertainty, and authority boundaries while loading only the smallest sufficient memory set required to answer or act safely.

Core boundary:

```text
STORED != RELEVANT
MATCHED != VALID
RETRIEVED != TRUSTED
RETRIEVED != TRUE
RELEVANT != AUTHORITATIVE
SIMILAR != SAME
POPULAR != INDEPENDENT
RECENT != CORRECT
MEMORY != CANON
RECALL != VALIDATION
CAPABILITY != AUTHORITY
UNKNOWN/GAP != PASS
```

---

## 1. Retrieval Objective

Given:

```text
Q = current objective / query
C = active context
M = available memory space
```

retrieval seeks a bounded set:

```text
R ⊆ M
```

such that `R` contains the smallest sufficient set of memories capable of materially changing the answer, decision, or action.

Conceptually:

```text
R* =
argmin |R|

subject to:

DECISION_SUFFICIENCY(R)
∧ INTEGRITY(R)
∧ DEPENDENCY_CLOSURE(R)
```

This is an architectural objective, not an assertion of a currently implemented optimization algorithm.

---

## 2. Core Retrieval Law

```text
RETRIEVE
THE SMALLEST
SUFFICIENT
PROOF SCOPE.
```

AMOS should not load the entire memory graph when a valid local dependency closure is sufficient.

Likewise:

```text
MORE MEMORY
!=
BETTER REASONING
```

Excess retrieval can introduce:

```text
NOISE
STALE CONTEXT
CONFLICT LEAKAGE
PROVENANCE CONFUSION
SCOPE CONTAMINATION
FALSE CONSENSUS
ATTENTION DILUTION
```

---

## 3. Retrieval Pipeline

Canonical conceptual path:

```text
OBJECTIVE
↓
CONTEXT / SCOPE
↓
MEMORY CLASS TARGET
↓
H-LEVEL RETRIEVAL
↓
VALIDITY CHECK
↓
M-LEVEL EXPANSION IF REQUIRED
↓
VALIDITY CHECK
↓
L-LEVEL EXPANSION IF REQUIRED
↓
RAW EVIDENCE IF REQUIRED
↓
DEPENDENCY CLOSURE
↓
PROVENANCE / INDEPENDENCE CHECK
↓
CONFLICT CHECK
↓
FRESHNESS / REGIME CHECK
↓
SUFFICIENCY CHECK
↓
RETURN RETRIEVAL SET
```

Default:

```text
RAW EVIDENCE
=
DO_NOT_LOAD_UNLESS_REQUIRED
```

---

## 4. Retrieval Object

A retrieval request should conceptually preserve:

```yaml
retrieval_request:
  request_id:
  objective:
  query:
  context:
  target_memory_types: []
  required_scope:
  required_regime:
  freshness_requirement:
  authority_requirement:
  dependency_depth:
  max_expansion:
  consequence_class:
  requested_at:
```

A retrieved memory candidate should preserve:

```yaml
retrieval_candidate:
  memory_id:
  memory_type:
  claim_class:
  relevance:
  provenance:
  source_ancestry:
  scope:
  regime:
  freshness:
  dependencies: []
  conflicts: []
  authority_state:
  immune_state:
  confidence_ceiling:
  invalidation_conditions: []
```

---

## 5. Retrieval Result

Conceptually:

```yaml
retrieval_result:
  request_id:
  selected_memories: []
  rejected_candidates: []
  quarantined_candidates: []
  unresolved_conflicts: []
  unresolved_gaps: []
  dependency_closure_complete:
  provenance_independence_state:
  scope_compatibility:
  regime_compatibility:
  freshness_state:
  sufficiency_state:
  retrieval_class:
```

---

## 6. Memory Types

Retrieval must preserve epistemic type.

Relevant classes include:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN
```

and AMOS conclusion classes:

```text
VERIFIED
DERIVED
MODEL
CONDITIONAL
COMPETING
UNKNOWN/GAP
```

Retrieval must not silently transform one type into another.

```text
RETRIEVE(MODEL)
!=
VERIFY(MODEL)
```

---

## 7. H/M/L Retrieval

AMOS memory retrieval follows fractal decomposition:

```text
H
DOMAIN / MAJOR KNOWLEDGE CAPSULE
↓
M
SUBSYSTEM / SUBDOMAIN
↓
L
DETAIL / CLAIM / DEPENDENCY
↓
RAW
PRIMARY OR STORED EVIDENCE
```

Default traversal:

```text
H FIRST
```

Expand only when H-level knowledge is insufficient.

---

## 8. H-Level Retrieval

H-level retrieval answers:

```text
WHICH DOMAIN?
WHICH MAJOR MEMORY FAMILY?
WHICH PROOF CAPSULE?
WHICH GOVERNING CONTEXT?
```

H-level retrieval should maximize routing accuracy while minimizing detail loading.

---

## 9. M-Level Retrieval

M-level retrieval resolves subsystem-level uncertainty.

Examples:

```text
PROVENANCE SUBSYSTEM
MEMORY CONFLICT SUBSYSTEM
CAUSAL SUBSYSTEM
AUTHORITY SUBSYSTEM
DOMAIN-SPECIFIC MODEL
```

M-level expansion occurs only when it can materially change the result.

---

## 10. L-Level Retrieval

L-level retrieval resolves:

```text
SPECIFIC CLAIM
SPECIFIC PREMISE
SPECIFIC DEPENDENCY
SPECIFIC FALSIFIER
SPECIFIC VERSION
SPECIFIC OBSERVATION
```

L-level retrieval is appropriate when higher-level capsules cannot establish sufficiency.

---

## 11. Raw Evidence Gate

Raw evidence is expensive and may increase complexity.

Therefore:

```text
RAW
=
DO_NOT_LOAD_UNLESS_REQUIRED
```

Load raw evidence when:

```text
PROOF CAPSULE INVALID
PROVENANCE UNCLEAR
CONFLICT MATERIAL
FRESHNESS EXPIRED
DEPENDENCY AMBIGUOUS
SCOPE UNCERTAIN
REGIME SHIFTED
HIGH-STAKES VALIDATION REQUIRED
```

---

## 12. RSCF Retrieval

RSCFs are first-class retrieval objects.

Retrieval should prefer a valid reusable RSCF when:

```text
DEPENDENCIES VALID
SCOPE VALID
REGIME VALID
FRESHNESS VALID
PROVENANCE VALID
NO MATERIAL UNRESOLVED CONFLICT
```

Then:

```text
REUSE RSCF
```

instead of recomputing its full evidence chain.

---

## 13. Proof Capsule Retrieval

Important conclusions should be retrieved with their proof capsule, including:

```text
CLAIM
CLASS
LOAD-BEARING PREMISES
EVIDENCE
PROVENANCE
SCOPE
TEMPORAL VALIDITY
REGIME
DEPENDENCIES
COMPETING EXPLANATIONS
FALSIFIERS
CONFIDENCE CEILING
```

A claim detached from these fields may be insufficient for load-bearing reuse.

---

## 14. Dependency Closure

Retrieval must not stop at a conclusion when its load-bearing dependencies are required for validity.

Given:

```text
C ← P1,P2,P3
```

if `C` is reused as load-bearing:

```text
DEPENDENCY_CLOSURE(C)
```

must be sufficiently established.

This does not require blindly loading every ancestor.

Only material dependencies need expansion.

---

## 15. Smallest Sufficient Closure

Conceptually:

```text
CLOSURE*
=
minimum dependency subgraph
required to establish
current validity
```

AMOS should avoid:

```text
FULL GRAPH EXPANSION
```

unless necessary.

---

## 16. Retrieval Relevance

Similarity alone does not define relevance.

Conceptually:

```text
RELEVANCE(M,Q)
=
f(
semantic_match,
dependency_value,
scope_match,
regime_match,
freshness,
authority_need,
decision_value
)
```

No specific weighting is asserted unless separately implemented and validated.

---

## 17. Decision-Changing Relevance

The highest-value memory is not necessarily the most semantically similar memory.

Prefer memory capable of resolving:

```text
LOAD-BEARING PREMISE
CRITICAL GAP
COMPETING HYPOTHESIS
SENSITIVE THRESHOLD
AUTHORITY QUESTION
FRESHNESS QUESTION
CAUSAL QUESTION
```

---

## 18. Retrieval Ranking Firewall

Ranking must not silently equate:

```text
SIMILARITY
=
TRUTH
```

or:

```text
RETRIEVAL SCORE
=
CONFIDENCE
```

or:

```text
TOP RESULT
=
AUTHORITATIVE RESULT
```

Ranking is routing.

Validation is separate.

---

## 19. Semantic Similarity Firewall

```text
SEMANTICALLY SIMILAR
!=
SEMANTICALLY IDENTICAL
```

Structural resemblance cannot prove:

```text
SAME CLAIM
SAME SOURCE
SAME REGIME
SAME SCOPE
SAME CAUSE
```

---

## 20. Identity Gate

Before reuse, memory identity should be sufficiently resolved.

Relevant identity dimensions:

```text
MEMORY ID
ARTIFACT ID
CLAIM ID
SOURCE ID
VERSION ID
HASH
SEMANTIC IDENTITY
```

Filename similarity is insufficient.

---

## 21. Provenance Retrieval

A load-bearing memory should retrieve enough provenance to establish:

```text
SOURCE
ANCESTRY
TRANSFORMATION PATH
VALIDATION HISTORY
DEPENDENCIES
```

where material.

If provenance is unavailable:

```text
PROVENANCE = UNKNOWN/GAP
```

and trust must be bounded accordingly.

---

## 22. Independence Retrieval

Multiple retrieved memories may share ancestry.

Example:

```text
SOURCE A
├─ MEMORY B
├─ SUMMARY C
└─ MEMORY D
```

Retrieving `B`, `C`, and `D` does not provide three independent confirmations.

```text
COUNT(RECORDS)
!=
COUNT(INDEPENDENT_SOURCES)
```

---

## 23. Sybil-Hardened Retrieval

Retrieval must resist false consensus caused by many descendants of one source.

```text
ONE SOURCE
→ MANY MEMORIES
→ MANY MATCHES
```

must remain:

```text
ONE PROVENANCE FAMILY
```

unless independence is demonstrated.

---

## 24. Conflict-Aware Retrieval

Retrieval must not return only supporting memories when material contradictory memories exist.

For consequential conclusions:

```text
RETRIEVE SUPPORT
+
SEARCH FOR MATERIAL CONTRADICTION
```

If credible incompatible claims remain:

```text
COMPETING
```

must be preserved.

---

## 25. Adversarial Retrieval

For consequential claims, retrieve through a genuinely different path seeking:

```text
CONTRADICTION
CORRELATED PROVENANCE
STALE PREMISES
SCOPE LEAKAGE
REGIME MISMATCH
HIDDEN DEPENDENCY
STRONGER ALTERNATIVE
CAUSAL OVERREACH
```

This path must not merely retrieve paraphrases of the original evidence.

---

## 26. Competing Hypothesis Retrieval

Given hypotheses:

```text
H1
H2
H3
```

retrieval should seek evidence capable of discriminating between them.

Prefer:

```text
CHEAPEST
HIGH-INFORMATION
DISCRIMINATING TEST
```

over accumulating redundant support for one hypothesis.

---

## 27. Conflict Preservation

If retrieval finds:

```text
M1 ⟂ M2
```

and neither dominates under valid evidence:

```text
RETURN BOTH
+
CONFLICT STATE
```

Do not force convergence for fluency.

---

## 28. Freshness Gate

Memory validity may expire.

```text
VALID(M,T0)
```

does not imply:

```text
VALID(M,T1)
```

where relevant environmental conditions changed.

Retrieval must check freshness when the conclusion depends on current state.

---

## 29. Freshness-Bounded Trust

Conceptually:

```text
TRUST(M)
=
TRUST(M | VALIDITY_WINDOW)
```

not:

```text
TRUST(M)
=
PERMANENT
```

---

## 30. Stale Retrieval

A stale memory may still be useful as:

```text
HISTORICAL EVIDENCE
BACKGROUND
PRIOR MODEL
LINEAGE
```

but must not silently serve as current validated state.

```text
STALE != USELESS
STALE != CURRENT
```

---

## 31. Scope Gate

Every important retrieved claim inherits an applicability envelope.

Potential dimensions:

```text
SYSTEM
POPULATION
ENVIRONMENT
SCALE
TIME
REGIME
MEASUREMENT METHOD
ASSUMPTIONS
```

Retrieval must not silently generalize beyond that envelope.

---

## 32. Regime Gate

A memory validated under:

```text
R0
```

cannot automatically be reused under:

```text
R1
```

When regime compatibility is unknown:

```text
REGIME_COMPATIBILITY = UNKNOWN/GAP
```

---

## 33. Temporal Retrieval

Historical and current retrieval must remain distinguishable.

```text
STATE @ T0
!=
STATE @ NOW
```

Retrieving historical memory does not establish present validity.

---

## 34. Causal Retrieval Firewall

Retrieval must preserve causal evidence type.

Evidence of:

```text
ASSOCIATION
CORRELATION
SEQUENCE
CO-OCCURRENCE
STRUCTURAL SIMILARITY
```

must not be retrieved and silently interpreted as:

```text
CAUSAL EFFECT
```

---

## 35. Causal Evidence Retrieval

Where causal inference is required, retrieval should seek appropriately typed evidence for:

```text
MECHANISM
INTERVENTION
COUNTERFACTUAL
CONFOUNDING
MEDIATION
NECESSITY
SUFFICIENCY
FEEDBACK
```

as relevant.

---

## 36. Causal Epoch Retrieval

Where a conclusion depends on causal-finality state:

```text
MEMORY
+
CAUSAL_EPOCH
```

must remain linked.

A conclusion finalized under an earlier causal epoch may require revalidation.

---

## 37. Authority-Aware Retrieval

Retrieval must distinguish:

```text
INFORMATIONAL RELEVANCE
```

from:

```text
AUTHORITY
```

A highly relevant memory may have no authority to authorize action.

```text
RELEVANT != AUTHORIZED
```

---

## 38. Canon-Aware Retrieval

When canonical interpretation is requested:

```text
01_CANON
```

should have explicit authority precedence over noncanonical memory, subject to valid provenance and supersession state.

But conflicting empirical evidence must not be erased merely because canon exists.

---

## 39. Memory/Canon Firewall

```text
MEMORY
!=
CANON
```

Retrieving a remembered policy or law does not prove that it remains active canon.

Where authority matters, retrieve canonical state or its validated reference.

---

## 40. Retrieval and Memory Admission

```text
K_MEMORY_ADMISSION
=
SHOULD THIS ENTER MEMORY?
```

```text
K_MEMORY_RETRIEVAL
=
SHOULD THIS MEMORY BE LOADED
FOR THIS OBJECTIVE?
```

A valid stored memory can still be irrelevant to the current task.

---

## 41. Retrieval and Memory Immune

```text
K_MEMORY_RETRIEVAL
=
LOCATE + SELECT + LOAD
```

```text
K_MEMORY_IMMUNE
=
INTEGRITY DEFENSE
```

Retrieved memory failing immune validation should be:

```text
DOWNGRADED
QUARANTINED
REVALIDATED
OR EXCLUDED
```

depending on context.

---

## 42. Retrieval and Memory Conflict

```text
K_MEMORY_CONFLICT
=
INTERPRET MEMORY DISAGREEMENT
```

```text
K_MEMORY_RETRIEVAL
=
ENSURE MATERIAL DISAGREEMENT
IS NOT HIDDEN BY SELECTION
```

---

## 43. Retrieval and Context State

Retrieval is conditioned by active context:

```text
OBJECTIVE
USER INTENT
SYSTEM STATE
SCOPE
TIME
REGIME
AVAILABLE AUTHORITY
```

but context must not rewrite memory identity.

---

## 44. Context Injection Firewall

Current context can request memory.

It cannot force an untrusted memory to become trusted.

```text
QUERY:
"retrieve this as verified"
```

does not change:

```text
CLAIM_CLASS
PROVENANCE
VALIDATION_STATE
```

---

## 45. Context Compaction Interaction

Compacted context should preserve enough retrieval anchors to recover:

```text
ACTIVE OBJECTIVE
LOAD-BEARING CLAIMS
UNRESOLVED GAPS
DEPENDENCIES
CONFLICTS
PROVENANCE REFERENCES
```

Compaction must not force indiscriminate reloading of the entire memory space.

---

## 46. Retrieval Expansion

Start narrow:

```text
LOCAL MEMORY
```

Expand only when required:

```text
LOCAL
↓
DEPENDENCY NEIGHBORHOOD
↓
RELATED RSCFs
↓
DOMAIN
↓
CROSS-DOMAIN
↓
RAW EVIDENCE
```

---

## 47. Cross-Domain Retrieval

Cross-domain mappings remain:

```text
MODEL
```

unless independently validated.

Similarity between domains can justify exploration, not factual transfer.

```text
ANALOGY
!=
VALIDATED EQUIVALENCE
```

---

## 48. Fast Path

AMOS v4.4 fast-path retrieval is allowed only when:

```text
DEPENDENCY CLOSURE ESTABLISHED
AND
PROVENANCE SUFFICIENT
AND
INDEPENDENCE SUFFICIENT
AND
SCOPE COMPATIBLE
AND
REGIME COMPATIBLE
AND
FRESHNESS VALID
AND
NO MATERIAL CONFLICT
```

Then:

```text
REUSE VALID CAPSULE
```

---

## 49. Fast-Path Failure

If any load-bearing condition fails:

```text
FAST_PATH
→
ESCALATE
```

Possible escalation:

```text
EXPAND DEPENDENCIES
RETRIEVE PROVENANCE
SEARCH CONTRADICTION
LOAD LOWER H/M/L LEVEL
LOAD RAW EVIDENCE
```

---

## 50. Independence Must Be Demonstrated

Fast retrieval must not assume independent confirmation because multiple matching records exist.

```text
INDEPENDENCE
=
PROVEN OR BOUNDED
```

otherwise:

```text
INDEPENDENCE
=
UNKNOWN/GAP
```

---

## 51. Retrieval Sensitivity

Before broad retrieval, identify the smallest unresolved premise capable of flipping the result.

Then retrieve evidence for that premise first.

Example:

```text
DECISION D
depends on
P1, P2, P3

only P2 can flip D

→ retrieve P2 first
```

---

## 52. Gap-Driven Retrieval

Classify gaps:

```text
CRITICAL
DECISION-RELEVANT
EXPLANATORY
COSMETIC
```

Retrieval priority:

```text
CRITICAL
↓
DECISION-RELEVANT
↓
EXPLANATORY
↓
COSMETIC
```

Do not spend retrieval budget resolving cosmetic gaps while a critical premise remains unknown.

---

## 53. Unknown/GAP Retrieval

If required information cannot be found:

```text
RETURN UNKNOWN/GAP
```

and identify the minimum missing information.

Never fabricate a bridging premise.

---

## 54. Retrieval Stop Conditions

Stop retrieval when:

```text
CLAIM SUFFICIENCY
AND
DECISION SUFFICIENCY
AND
ACTION SUFFICIENCY
```

are reached.

More retrieval after sufficiency may reduce quality.

---

## 55. Retrieval Budget

Conceptually:

```text
VALUE OF ADDITIONAL RETRIEVAL
=
EXPECTED DECISION IMPROVEMENT
-
RETRIEVAL COST
-
NOISE RISK
-
STALE/CONFLICT CONTAMINATION RISK
```

Continue only while expected value remains positive.

---

## 56. Adaptive Retrieval Complexity

```text
C0 — DIRECT
known valid local memory

C1 — COMPACT
small validation set

C2 — STRUCTURED
dependency + provenance retrieval

C3 — DEEP
multi-path / conflict / raw evidence

C4 — MAXIMUM
high-stakes adversarial retrieval
```

Start at the lowest sufficient level.

---

## 57. Escalation Conditions

Escalate when:

```text
HIGH STAKES
IRREVERSIBILITY
NOVELTY
WEAK EVIDENCE
STALE MEMORY
CONTRADICTION
CAUSAL AMBIGUITY
SCOPE MISMATCH
REGIME SHIFT
COMPETING MODELS
GOVERNANCE IMPACT
LOW TRUST
PROVENANCE CORRELATION
```

---

## 58. Retrieval Recovery

If a retrieved path fails:

```text
PATH A
↓
FAILED PREMISE
```

do not blindly rerun `PATH A`.

Instead:

```text
INVALIDATE FAILED EDGE
↓
PRESERVE UNAFFECTED RETRIEVAL
↓
REROUTE
```

---

## 59. Local Rerouting

Conceptually:

```text
Q
├─ PATH A → FAILED
├─ PATH B → VALID
└─ PATH C → UNNECESSARY
```

Use `PATH B`.

Do not recompute the entire graph unless required.

---

## 60. Retrieval Cache

Previously validated retrieval results may be reused when:

```text
DEPENDENCIES UNCHANGED
SCOPE UNCHANGED
REGIME UNCHANGED
FRESHNESS VALID
CONFLICT STATE UNCHANGED
PROVENANCE VALID
```

Otherwise the cache must be invalidated or revalidated.

---

## 61. Retrieval Cache Firewall

```text
CACHED
!=
CURRENT
```

Cache existence cannot substitute for validity checks.

---

## 62. MVCC/CAS Compatibility

Where retrieval interacts with mutable persistent state, conceptually:

```text
READ MEMORY @ VERSION V1
↓
REASON
↓
VERIFY CURRENT VERSION
```

If state changed to `V2` before load-bearing commit:

```text
V1 != V2
→
REVALIDATE
```

This expresses compatibility with AMOS persistent-state reasoning; it does not assert implemented storage semantics.

---

## 63. Atomic Multi-RSCF Retrieval

If a decision requires:

```text
R1 + R2 + R3
```

the retrieved set should represent a mutually compatible state.

Do not silently combine:

```text
R1 @ EPOCH A
R2 @ EPOCH B
R3 @ EPOCH C
```

when epoch mismatch affects validity.

---

## 64. Retrieval Consistency

Required consistency depends on the decision.

Some queries can tolerate:

```text
EVENTUAL / PARTIAL CONTEXT
```

while governance or irreversible decisions may require:

```text
COHERENT VALIDATED SNAPSHOT
```

The retrieval kernel should not impose one universal consistency model.

---

## 65. Retrieval Failure Classes

```text
NO_MATCH
FALSE_MATCH
STALE_MATCH
MISSCOPED_MATCH
REGIME_MISMATCH
PROVENANCE_GAP
DEPENDENCY_GAP
CONFLICT_HIDDEN
CORRELATED_RESULTS
FALSE_INDEPENDENCE
IDENTITY_COLLISION
VERSION_MISMATCH
AUTHORITY_MISMATCH
CAUSAL_TYPE_MISMATCH
OVER_RETRIEVAL
UNDER_RETRIEVAL
PREMATURE_STOP
RUNAWAY_EXPANSION
CACHE_STALENESS
UNKNOWN/GAP
```

---

## 66. Over-Retrieval

Over-retrieval occurs when memory is loaded that cannot materially affect the objective and introduces unnecessary complexity.

Symptoms:

```text
CONTEXT BLOAT
DUPLICATE CLAIMS
UNRELATED CONFLICTS
ATTENTION DILUTION
PROVENANCE CONFUSION
```

---

## 67. Under-Retrieval

Under-retrieval occurs when a load-bearing dependency, contradiction, scope condition, or authority source is omitted.

```text
SMALL CONTEXT
```

is not inherently good if it is insufficient.

The rule is:

```text
SMALLEST SUFFICIENT
```

not:

```text
SMALLEST POSSIBLE
```

---

## 68. Retrieval Integrity Invariants

```text
MR-01
RETRIEVAL MUST NOT IMPLY TRUTH

MR-02
RETRIEVAL MUST PRESERVE CLAIM CLASS

MR-03
RETRIEVAL MUST PRESERVE PROVENANCE WHEN MATERIAL

MR-04
RETRIEVAL MUST PRESERVE SCOPE

MR-05
RETRIEVAL MUST PRESERVE REGIME

MR-06
RETRIEVAL MUST PRESERVE FRESHNESS STATE

MR-07
RETRIEVAL MUST PRESERVE MATERIAL CONFLICTS

MR-08
RETRIEVAL MUST NOT ASSUME SOURCE INDEPENDENCE

MR-09
DUPLICATE RECORDS MUST NOT AMPLIFY CONFIDENCE

MR-10
DEPENDENCY CLOSURE MUST BE SUFFICIENT FOR LOAD-BEARING REUSE

MR-11
RAW EVIDENCE MUST NOT LOAD BY DEFAULT

MR-12
H/M/L EXPANSION MUST BE DEMAND-DRIVEN

MR-13
FAST PATH MUST FAIL CLOSED ON MATERIAL UNKNOWN CONDITIONS

MR-14
STALE MEMORY MUST NOT MASQUERADE AS CURRENT STATE

MR-15
HISTORICAL MEMORY MUST REMAIN TEMPORALLY TYPED

MR-16
MODEL MEMORY MUST NOT MASQUERADE AS VERIFIED EVIDENCE

MR-17
MEMORY MUST NOT MASQUERADE AS CANON

MR-18
RELEVANCE MUST NOT MASQUERADE AS AUTHORITY

MR-19
SIMILARITY MUST NOT MASQUERADE AS CAUSATION

MR-20
FAILED PATHS MUST NOT BE REPEATED WITHOUT CHANGED CONDITIONS

MR-21
INVALIDATION MUST REMAIN LOCAL WHERE POSSIBLE

MR-22
RETRIEVAL MUST STOP WHEN SUFFICIENCY IS REACHED

MR-23
CRITICAL GAPS MUST PRECEDE COSMETIC GAPS

MR-24
ATOMIC MULTI-RSCF REASONING MUST NOT MIX INCOMPATIBLE STATES

MR-25
UNKNOWN/GAP MUST NOT BECOME PASS
```

---

## 69. Required Tests

```text
H-LEVEL ROUTING TEST
M-LEVEL EXPANSION TEST
L-LEVEL EXPANSION TEST
RAW-EVIDENCE GATE TEST
RSCF REUSE TEST
PROOF-CAPSULE RETRIEVAL TEST
DEPENDENCY-CLOSURE TEST
MINIMUM-SUFFICIENT-CLOSURE TEST
PROVENANCE RETRIEVAL TEST
SOURCE-ANCESTRY TEST
INDEPENDENCE-GATE TEST
SYBIL-HARDENING TEST
CONFLICT-RETRIEVAL TEST
ADVERSARIAL-RETRIEVAL TEST
FRESHNESS TEST
SCOPE TEST
REGIME TEST
TEMPORAL-STATE TEST
CAUSAL-TYPE TEST
AUTHORITY-BOUNDARY TEST
CANON-BOUNDARY TEST
FAST-PATH TEST
FAST-PATH-FAILURE TEST
SENSITIVITY-RETRIEVAL TEST
GAP-PRIORITY TEST
STOP-CONDITION TEST
OVER-RETRIEVAL TEST
UNDER-RETRIEVAL TEST
CACHE-INVALIDATION TEST
MVCC/CAS-REVALIDATION TEST
ATOMIC-MULTI-RSCF TEST
LOCAL-REROUTING TEST
UNKNOWN-GAP TEST
```

---

## 70. Negative Tests

```text
TOP MATCH
→ VERIFIED
MUST FAIL

MOST SIMILAR
→ AUTHORITATIVE
MUST FAIL

THREE COPIES OF SOURCE A
→ THREE INDEPENDENT SOURCES
MUST FAIL

OLD VALID MEMORY
→ CURRENT VALID MEMORY
MUST FAIL

HISTORICAL STATE
→ PRESENT STATE
MUST FAIL

MODEL MEMORY
→ FACT
MUST FAIL

MEMORY
→ CANON
MUST FAIL

CORRELATION MEMORY
→ CAUSAL EFFECT
MUST FAIL

CONFLICTING MEMORY OMITTED
BECAUSE IT LOWERS FLUENCY
MUST FAIL

RAW EVIDENCE ALWAYS LOADED
MUST FAIL

ENTIRE MEMORY GRAPH LOADED
FOR LOCAL QUESTION
MUST FAIL

FAST PATH WITH UNKNOWN PROVENANCE
→ PASS
MUST FAIL

FAST PATH WITH REGIME MISMATCH
→ PASS
MUST FAIL

FAILED RETRIEVAL PATH
→ IDENTICAL RETRY
MUST FAIL

R1 @ EPOCH A
+
R2 @ INCOMPATIBLE EPOCH B
→ ATOMIC VALID SET
MUST FAIL

UNKNOWN/GAP
→ PASS
MUST FAIL
```

---

## 71. Retrieval Observability

Where implemented, retrieval should expose enough trace information to inspect:

```text
QUERY
TARGET TYPES
SELECTED MEMORIES
REJECTED MEMORIES
EXPANSION PATH
DEPENDENCY EXPANSION
PROVENANCE CHECK
CONFLICT CHECK
FRESHNESS CHECK
SCOPE / REGIME CHECK
STOP REASON
GAPS
```

Observability must not require exposing protected internal reasoning.

---

## 72. Retrieval Trace

Conceptual trace:

```yaml
retrieval_trace:
  retrieval_id:
  objective:
  initial_nodes: []
  expanded_nodes: []
  rejected_nodes: []
  quarantine_nodes: []
  dependency_edges_loaded: []
  conflicts_found: []
  gaps_found: []
  stop_condition:
  final_retrieval_class:
```

---

## 73. Privacy and Security Boundary

Retrieval eligibility does not override access control.

```text
RELEVANT
+
EXISTS
```

does not imply:

```text
AUTHORIZED TO RETRIEVE
```

Authorization belongs to the appropriate security/control-plane contract.

---

## 74. Tool Boundary

A retrieval tool provides capability.

```text
TOOL CAN SEARCH MEMORY
```

does not imply:

```text
TOOL MAY ACCESS ALL MEMORY
```

or:

```text
TOOL OUTPUT IS TRUSTED
```

---

## 75. Runtime Boundary

`K_MEMORY_RETRIEVAL` defines retrieval invariants and deterministic constraints.

Execution belongs to runtime components.

```text
KERNEL
=
RETRIEVAL LOGIC / INVARIANTS

RUNTIME
=
EXECUTION / SCHEDULING / ROUTING

CONTROL_PLANE
=
POLICY / AUTHORITY / COMMIT

MEMORY
=
PERSISTENT STORAGE

KNOWLEDGE
=
EVIDENCE / CLAIM / RSCF STRUCTURES
```

---

## 76. Authority Boundary

`K_MEMORY_RETRIEVAL` may determine:

```text
WHAT MEMORY IS RELEVANT
WHAT DEPENDENCIES ARE REQUIRED
WHAT VALIDITY CHECKS ARE REQUIRED
WHEN RETRIEVAL IS INSUFFICIENT
```

It does not independently determine:

```text
WHO MAY ACCESS THE MEMORY
WHO MAY ALTER CANON
WHO MAY COMMIT STATE
WHO MAY AUTHORIZE EXTERNAL ACTION
```

Therefore:

```text
RETRIEVAL CAPABILITY
!=
RETRIEVAL AUTHORITY
```

---

## 77. Promotion Gate

Before promotion beyond `AMOS_MODEL`, evidence should establish:

```text
[ ] H/M/L retrieval implemented
[ ] RSCF retrieval implemented
[ ] proof capsule retrieval implemented
[ ] dependency closure implemented
[ ] provenance-aware retrieval implemented
[ ] ancestry/correlation detection implemented
[ ] independence gate implemented
[ ] conflict-aware retrieval implemented
[ ] freshness checks implemented
[ ] scope checks implemented
[ ] regime checks implemented
[ ] authority-aware retrieval implemented
[ ] fast-path validation implemented
[ ] sensitivity-driven expansion implemented
[ ] gap prioritization implemented
[ ] retrieval stop conditions implemented
[ ] cache invalidation implemented
[ ] local rerouting implemented
[ ] atomic multi-RSCF retrieval tested
[ ] concurrent-state revalidation tested
[ ] observability wired
[ ] security/access controls integrated
[ ] adversarial retrieval tests passed
[ ] unresolved critical gaps registered
```

Until evidenced:

```text
RETRIEVAL_RUNTIME = UNKNOWN/GAP
HML_ROUTER_IMPLEMENTATION = UNKNOWN/GAP
RSCF_RETRIEVAL_IMPLEMENTATION = UNKNOWN/GAP
PROVENANCE_AWARE_RANKING = UNKNOWN/GAP
SYBIL_HARDENED_RETRIEVAL = UNKNOWN/GAP
ATOMIC_MULTI_RSCF_RETRIEVAL = UNKNOWN/GAP
FORMAL_VERIFICATION = UNKNOWN/GAP
EMPIRICAL_VALIDATION = UNKNOWN/GAP
```

---

## 78. RSCF Node

```RSCF-NODE
node_id: AMOS-OS-K-MEMORY-RETRIEVAL
node_type: kernel_memory_retrieval_contract
domain: AMOS_OS_KERNEL
functional_type: MemoryRetrievalKernel
lifecycle_stage: Architecture
claim_class: AMOS_MODEL

RSCF-RELATIONS:
  - ROOTED_IN: README
  - DEPENDENCY_BOUND_TO: DEPENDENCY_MAP

  - GOVERNED_BY: AMOS_CORE_LAWS
  - CONSTRAINED_BY: INVARIANT_REGISTRY
  - PRECEDENCE_GOVERNED_BY: LAW_HIERARCHY
  - PERSISTENCE_GOVERNED_BY: PERSISTENCE_CANON
  - PROVENANCE_GOVERNED_BY: CANON_PROVENANCE
  - SOURCE_LINEAGE_GOVERNED_BY: SOURCE_LINEAGE
  - AUTHORITY_BOUND_TO: AUTHORITY_CANON

  - INDEXED_BY: KERNEL_MAP
  - IDENTITY_BOUND_TO: K_IDENTITY
  - META_LOGIC_BOUND_TO: K_META_LOGIC
  - MULTI_HYPOTHESIS_BOUND_TO: K_MULTI_HYPOTHESIS
  - CONTEXT_BOUND_TO: K_CONTEXT_STATE
  - CONTEXT_COMPACTION_BOUND_TO: K_CONTEXT_COMPACTION
  - MEMORY_ADMISSION_BOUND_TO: K_MEMORY_ADMISSION
  - MEMORY_CONFLICT_BOUND_TO: K_MEMORY_CONFLICT
  - MEMORY_IMMUNE_BOUND_TO: K_MEMORY_IMMUNE
  - SYSTEM_STATE_BOUND_TO: K_SYSTEM_STATE
  - WORLD_MODEL_BOUND_TO: K_WORLD_MODEL
  - CAUSAL_CLOSURE_BOUND_TO: K_CAUSAL_CLOSURE
  - CAUSAL_EPOCH_BOUND_TO: K_CAUSAL_EPOCH

  - MEMORY_INTERACTION: README
  - KNOWLEDGE_INTERACTION: 11_KNOWLEDGE/00_AMOS_Full_Brain_OS_Architecture
  - STATE_INTERACTION: README
  - SCHEMA_INTERACTION: README
  - OBSERVED_BY: README
  - SECURITY_CONSTRAINED_BY: README
  - VERIFIED_BY: README
  - OPERATED_BY: README
```

---

## 79. Canonical Retrieval Summary

```text
OBJECTIVE
↓
IDENTIFY DECISION-CHANGING UNCERTAINTY
↓
RETRIEVE H
↓
VALID?
├─ YES → CHECK SUFFICIENCY
└─ NO / INSUFFICIENT
      ↓
      RETRIEVE M
      ↓
      VALID?
      ├─ YES → CHECK SUFFICIENCY
      └─ NO / INSUFFICIENT
            ↓
            RETRIEVE L
            ↓
            RAW EVIDENCE IF REQUIRED
↓
DEPENDENCY CLOSURE
↓
PROVENANCE
↓
INDEPENDENCE
↓
SCOPE
↓
REGIME
↓
FRESHNESS
↓
CONFLICT
↓
AUTHORITY
↓
SUFFICIENT?
├─ YES → STOP
└─ NO  → RESOLVE NEXT HIGHEST-VALUE GAP
```

Core laws:

```text
RETRIEVAL != TRUTH
RECALL != VALIDATION
SIMILARITY != IDENTITY
RELEVANCE != AUTHORITY
RECENCY != CORRECTNESS
MULTIPLICITY != INDEPENDENCE
MEMORY != CANON
CORRELATION != CAUSATION
MORE CONTEXT != MORE KNOWLEDGE
SMALLEST != SUFFICIENT
UNKNOWN/GAP != PASS
```

The decisive invariant is:

```text
AMOS DOES NOT
RETRIEVE MEMORY
BECAUSE IT EXISTS.

AMOS RETRIEVES
MEMORY BECAUSE
IT CAN MATERIALLY
CHANGE THE
CURRENT RESULT.

IT STARTS
WITH THE
SMALLEST
VALID KNOWLEDGE
CAPSULE.

IT DESCENDS
FROM H
TO M
TO L
TO RAW EVIDENCE

ONLY WHEN
THE CURRENT
LEVEL CANNOT
CLOSE THE
LOAD-BEARING
UNCERTAINTY.

WHEN MEMORY
IS RETRIEVED,

AMOS DOES NOT
ASK ONLY:

"IS THIS
SIMILAR?"

IT ALSO ASKS:

"WHAT IS IT?"

"WHERE DID IT
COME FROM?"

"WHAT DOES IT
DEPEND ON?"

"IS ITS
PROVENANCE
INDEPENDENT?"

"WHERE DOES IT
APPLY?"

"UNDER WHICH
REGIME?"

"IS IT STILL
FRESH?"

"WHAT
CONTRADICTS IT?"

"DOES IT HAVE
AUTHORITY HERE?"

"CAN IT CHANGE
THE DECISION?"

IF ONE
DEPENDENCY
FAILS,

AMOS DOES NOT
RELOAD THE
WHOLE BRAIN.

IT INVALIDATES
THE FAILED PATH,

PRESERVES
UNAFFECTED
MEMORY,

AND REROUTES
LOCALLY.

IF THE
NECESSARY
MEMORY
CANNOT BE
VALIDATED,

AMOS DOES NOT
FILL THE GAP
WITH FLUENCY.

IT RETURNS:

UNKNOWN/GAP.

THE GOAL
OF MEMORY
RETRIEVAL

IS NOT
MAXIMUM RECALL.

IT IS

MINIMUM
SUFFICIENT
VALID
RECALL.
```

## Related

[[README]] ·
[[DEPENDENCY_MAP]] ·
[[AMOS_CORE_LAWS]] ·
[[INVARIANT_REGISTRY]] ·
[[LAW_HIERARCHY]] ·
[[PERSISTENCE_CANON]] ·
[[CANON_PROVENANCE]] ·
[[SOURCE_LINEAGE]] ·
[[AUTHORITY_CANON]] ·
[[KERNEL_MAP]] ·
[[K_IDENTITY]] ·
[[K_META_LOGIC]] ·
[[K_MULTI_HYPOTHESIS]] ·
[[K_CONTEXT_STATE]] ·
[[K_CONTEXT_COMPACTION]] ·
[[K_MEMORY_ADMISSION]] ·
[[K_MEMORY_CONFLICT]] ·
[[K_MEMORY_IMMUNE]] ·
[[K_SYSTEM_STATE]] ·
[[K_WORLD_MODEL]] ·
[[K_CAUSAL_CLOSURE]] ·
[[K_CAUSAL_EPOCH]] ·
README ·
11_KNOWLEDGE/00_AMOS_Full_Brain_OS_Architecture ·
README ·
README ·
[[README]] ·
README ·
[[README]] ·
README

```text
```

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
**MOC:** [[05_MEMORY_MOC]]
