---
type: canon
artifact_id: AMOS-HML-CANON
name: HML_CANON
title: "AMOS H/M/L Canon — Fractal Knowledge Resolution and Retrieval Architecture"

document_version: "2.0.0"
canon_version: "4.4"
amos_core_target: "v4.4"

status: ACTIVE_CANON_CANDIDATE
conclusion_class: AMOS_MODEL
rscf_state: derived

canon_group: tech-ai
canon_type: knowledge-architecture-canon

origin_architect: Trang Phan
steward: Trang Phan

created: 2026-08-25
updated: 2026-08-25

tags: [amos, canon, universe, amos-os, amos-core, amos-core-v4-4, hml, fractal-knowledge, knowledge-resolution, retrieval, dependency-closure, rscf, provenance, epistemic-regime, scope, freshness, uncertainty, progressive-disclosure, context-management, evidence, canon-group/tech-ai, canon/framework, canon/model, rscf/claim, rscf/provenance, rscf/state/derived, topic/hml-canon]

aliases: "- AMOS HML Canon
  - H/M/L Canon
  - AMOS H/M/L Architecture
  - AMOS Fractal Knowledge Resolution C..."
related: "see body"---



# AMOS H/M/L Canon

**Origin architect / steward:** Trang Phan

> **Status:** `ACTIVE_CANON_CANDIDATE`  
> **AMOS Core target:** `v4.4`  
> **Conclusion class:** `AMOS_MODEL`

---

# 0. Purpose

The **AMOS H/M/L Canon** defines the canonical fractal resolution architecture used to organize, retrieve, reason over, validate, and selectively expand AMOS knowledge.

H/M/L separates knowledge into progressively more specific resolution levels:

```text
H — HIGH / DOMAIN
↓
M — MID / SUBSYSTEM
↓
L — LOW / DETAIL
↓
RAW EVIDENCE
```

The purpose is not merely hierarchical organization.

H/M/L provides a governed mechanism for:

* progressive knowledge retrieval;
* context minimization;
* dependency-directed traversal;
* provenance preservation;
* uncertainty-directed escalation;
* RSCF resolution;
* evidence loading;
* contradiction localization;
* scope and regime control;
* freshness checking;
* selective invalidation;
* proof reuse;
* efficient reasoning without integrity loss.

The canonical retrieval law is:

```text
LOAD THE SMALLEST SUFFICIENT
DEPENDENCY-CLOSED KNOWLEDGE PATH
THAT CAN SUPPORT THE REQUIRED CONCLUSION.
```

Raw evidence remains:

```text
DO_NOT_LOAD_UNLESS_REQUIRED
```

unless a load-bearing uncertainty cannot otherwise be resolved.

---

# 1. Core H/M/L Structure

```text
                    QUERY / OBJECTIVE
                           │
                           ↓
                 ┌───────────────────┐
                 │ H — DOMAIN        │
                 │ orientation       │
                 │ boundaries        │
                 │ major invariants  │
                 └─────────┬─────────┘
                           │
                  relevant branch only
                           ↓
                 ┌───────────────────┐
                 │ M — SUBSYSTEM     │
                 │ mechanisms        │
                 │ dependencies      │
                 │ interfaces        │
                 └─────────┬─────────┘
                           │
                 required detail only
                           ↓
                 ┌───────────────────┐
                 │ L — DETAIL        │
                 │ exact claims      │
                 │ rules             │
                 │ parameters        │
                 └─────────┬─────────┘
                           │
                 unresolved proof need?
                    YES ───┴─── NO
                     │           │
                     ↓           ↓
             ┌─────────────┐   SYNTHESIZE
             │ RAW EVIDENCE│
             │ provenance  │
             │ observations│
             │ source data │
             └─────────────┘
```

---

# 2. Canonical Meaning of H, M, and L

## H — High-Level Domain

`H` provides the smallest sufficient domain-level orientation.

H may contain:

```text
DOMAIN IDENTITY
PURPOSE
SYSTEM BOUNDARY
MAJOR CONCEPTS
TOP-LEVEL INVARIANTS
AUTHORITY BOUNDARIES
MAJOR DEPENDENCIES
REGIME ENVELOPE
PROVENANCE ENTRYPOINTS
M-SUBSYSTEM INDEX
```

H answers:

> What domain are we in, what governs it, and which subsystem could materially answer the question?

H should not contain every implementation detail.

---

## M — Mid-Level Subsystem

`M` decomposes an H-domain into operational or conceptual subsystems.

M may contain:

```text
SUBSYSTEM PURPOSE
MECHANISMS
INTERFACES
DEPENDENCY EDGES
CONTROL RELATIONSHIPS
RSCF CLUSTERS
STATE TRANSITIONS
FAILURE MODES
PROVENANCE RELATIONSHIPS
L-NODE INDEX
```

M answers:

> Which mechanism, subsystem, or dependency path controls the result?

---

## L — Low-Level Detail

`L` contains the detail required to establish or challenge specific conclusions.

L may contain:

```text
CLAIMS
PREMISES
RULES
ALGORITHMS
PARAMETERS
SCHEMAS
FORMULAS
INVARIANTS
TEST CONDITIONS
EXCEPTIONS
FALSIFIERS
SOURCE REFERENCES
EXACT DEPENDENCIES
```

L answers:

> What exact evidence, rule, premise, or implementation detail determines the conclusion?

---

# 3. Raw Evidence Layer

Raw evidence sits below L but is not automatically loaded.

```text
H
↓
M
↓
L
↓
RAW EVIDENCE
```

Raw evidence may include:

```text
SOURCE DOCUMENTS
SOURCE CODE
OBSERVATIONS
LOGS
MEASUREMENTS
EXPERIMENT RESULTS
DATABASE RECORDS
EXTERNAL CLAIMS
VERSION HISTORY
TRACE EVENTS
TEST OUTPUTS
PRIMARY RECORDS
```

Canonical default:

```text
RAW_EVIDENCE_LOAD_POLICY
=
DO_NOT_LOAD_UNLESS_REQUIRED
```

This is an efficiency policy, not an evidence-suppression policy.

If raw evidence can materially change the conclusion:

```text
RAW EVIDENCE
MUST BECOME RETRIEVABLE.
```

---

# 4. H/M/L Is Fractal

H/M/L is recursive.

An H node may contain M nodes.

An M node may itself be treated as a local H when entered.

An L node may expose another H/M/L structure if its internal complexity requires decomposition.

```text
H
├── M1
│   ├── L1
│   ├── L2
│   └── L3
│
├── M2
│   ├── L1
│   │   └── local H
│   │       ├── local M
│   │       └── local L
│   └── L2
│
└── M3
```

Therefore:

```text
H / M / L
=
RESOLUTION ROLES
```

not necessarily permanent absolute object types.

---

# 5. Resolution Is Contextual

A knowledge object can occupy different H/M/L roles depending on the current reasoning scope.

Example:

```text
GLOBAL VIEW
H = AMOS OS
M = CONTROL PLANE
L = PROVENANCE SYSTEM
```

When the reasoning focus becomes provenance:

```text
LOCAL VIEW
H = PROVENANCE SYSTEM
M = LINEAGE RESOLUTION
L = SOURCE ANCESTRY EDGE
```

Therefore:

```text
HML_ROLE
!=
PERMANENT_IDENTITY
```

Semantic identity and resolution role remain separate.

---

# 6. H/M/L Identity Firewall

The following are distinct:

```text
ARTIFACT IDENTITY
SEMANTIC IDENTITY
HML RESOLUTION ROLE
RSCF IDENTITY
VERSION IDENTITY
PROVENANCE IDENTITY
REPOSITORY LOCATION
```

Changing an object's H/M/L placement must not silently alter its semantic or provenance identity.

---

# 7. Primary Retrieval Law

AMOS retrieval should begin with the smallest sufficient context.

```text
QUERY
↓
H
↓
RELEVANT M
↓
REQUIRED L
↓
RAW EVIDENCE ONLY IF NEEDED
```

Not:

```text
QUERY
↓
LOAD EVERYTHING
↓
SEARCH EVERYTHING
↓
REASON OVER EVERYTHING
```

unless exhaustive retrieval is genuinely required.

---

# 8. Dependency-Directed Retrieval

Traversal follows decision-relevant dependencies.

```text
QUESTION
↓
TARGET CLAIM
↓
LOAD-BEARING PREMISES
↓
DEPENDENCY EDGES
↓
REQUIRED H/M/L NODES
```

The system should not expand branches that cannot materially alter the result.

Canonical rule:

```text
IF NODE CANNOT CHANGE
CLAIM / DECISION / ACTION
THEN DO NOT EXPAND BY DEFAULT.
```

---

# 9. Smallest Sufficient Proof Scope

AMOS v4.4 permits local reasoning when the proof scope is sufficient.

Conceptually:

```text
MINIMUM PROOF SCOPE
=
MIN(
  dependency-closed,
  provenance-valid,
  scope-compatible,
  regime-compatible,
  fresh-enough,
  non-conflicting
  knowledge set
)
```

The objective is not minimum tokens.

The objective is:

```text
MINIMUM SUFFICIENT VALID EVIDENCE
```

---

# 10. Integrity Dominates Compression

Compression is subordinate to integrity.

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
SMALLER CONTEXT
```

is desirable only when it preserves the load-bearing proof.

---

# 11. H Bootstrap Capsule

An H node should ideally expose a compact bootstrap capsule.

```yaml
h_bootstrap:
  node_id:
  domain:
  purpose:

  scope:
  regime:

  major_invariants: []

  authority_boundary:

  major_dependencies: []

  m_children: []

  known_conflicts: []

  freshness:

  provenance:

  escalation_conditions: []
```

The bootstrap capsule is an orientation object.

It is not necessarily sufficient evidence for a consequential conclusion.

---

# 12. M Subsystem Capsule

An M node should provide the subsystem information necessary to determine whether deeper retrieval is required.

```yaml
m_capsule:
  node_id:
  parent_h:

  subsystem:
  responsibility:

  inputs: []
  outputs: []

  dependencies: []

  invariants: []

  rscf_nodes: []

  l_children: []

  known_failures: []
  known_conflicts: []

  scope:
  regime:
  freshness:

  provenance:

  escalation_conditions: []
```

---

# 13. L Detail Capsule

L is where exact load-bearing details should become explicit.

```yaml
l_capsule:
  node_id:
  parent_m:

  claim:
  claim_class:

  premises: []
  evidence: []

  dependencies: []

  provenance:

  scope:
  regime:
  freshness:

  competing_hypotheses: []

  falsifiers: []

  confidence_ceiling:

  raw_evidence_refs: []
```

---

# 14. RSCF and H/M/L

RSCF and H/M/L solve different problems.

```text
H/M/L
=
KNOWLEDGE RESOLUTION / RETRIEVAL STRUCTURE

RSCF
=
CLAIM / PREMISE / EVIDENCE / DEPENDENCY STRUCTURE
```

They interact:

```text
H
↓
M
↓
L
↓
RSCF
↓
EVIDENCE / PROVENANCE
```

But:

```text
HML_NODE != RSCF_NODE
```

unless explicitly modeled as both.

---

# 15. RSCF Retrieval

A target RSCF may trigger H/M/L traversal.

```text
TARGET CLAIM
↓
RSCF
├── PREMISE A → M1/L2
├── PREMISE B → M3/L1
├── PREMISE C → H2/M4/L7
└── EVIDENCE D → RAW SOURCE
```

Only load-bearing dependencies need expansion by default.

---

# 16. Proof Capsule Reuse

A previously validated conclusion may be reused without reloading its full evidence tree when its validity envelope remains intact.

A reusable proof capsule should conceptually retain:

```text
CLAIM
CLAIM CLASS
LOAD-BEARING PREMISES
PROVENANCE
DEPENDENCIES
SCOPE
REGIME
FRESHNESS
COMPETING EXPLANATIONS
FALSIFIERS
CONFIDENCE CEILING
```

Reuse is valid only while those conditions remain valid.

---

# 17. Proof Capsule Invalidation

If a dependency fails:

```text
FAILED PREMISE
↓
DEPENDENCY EDGE
↓
DEPENDENT PROOF CAPSULES
↓
INVALIDATE
```

Unrelated capsules remain valid.

```text
LOCAL FAILURE
!=
GLOBAL KNOWLEDGE FAILURE
```

---

# 18. Epistemic Typing

H/M/L does not change epistemic class.

Knowledge may remain:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN
```

and conclusions may remain:

```text
VERIFIED
DERIVED
MODEL
CONDITIONAL
COMPETING
UNKNOWN/GAP
```

A claim does not become stronger merely because it appears at H level.

```text
HIGH LEVEL
!=
HIGH CONFIDENCE
```

---

# 19. Provenance Preservation

Every material compression boundary must preserve enough provenance to recover the underlying source path.

```text
RAW SOURCE
↓
L
↓
M
↓
H
```

must remain recoverable as:

```text
H
→ M
→ L
→ SOURCE
```

when validation requires it.

Therefore:

```text
COMPRESSION
MUST NOT
DESTROY MATERIAL LINEAGE.
```

---

# 20. Provenance Topology

Multiple H/M/L nodes may derive from one underlying source.

```text
SOURCE_A
├── L1
│   └── M1
│       └── H1
│
├── L2
│   └── M2
│       └── H2
│
└── L3
    └── M3
        └── H3
```

The resulting H nodes are not independent confirmations.

```text
MULTIPLE H NODES
!=
MULTIPLE INDEPENDENT SOURCES
```

---

# 21. Sybil Hardening

H/M/L must not amplify confidence through repeated descendants of the same ancestry.

```text
ONE SOURCE
→ MANY L
→ MANY M
→ MANY H
```

must not become:

```text
MANY INDEPENDENT CONFIRMATIONS
```

Independence is a provenance property, not a node-count property.

---

# 22. Scope Inheritance

Child knowledge inherits applicable scope constraints unless explicitly narrowed or independently expanded.

```text
H_SCOPE
↓
M_SCOPE
↓
L_SCOPE
```

A child may narrow scope:

```text
L_SCOPE ⊆ M_SCOPE ⊆ H_SCOPE
```

A child must not silently broaden it.

---

# 23. Scope Envelope

Material nodes should support an applicability envelope.

```yaml
scope:
  system:
  population:
  environment:
  scale:
  time:
  measurement_method:
  assumptions:
```

Cross-scope reuse requires validation.

---

# 24. Regime Inheritance

Knowledge is regime-aware.

```text
REGIME_A
H
↓
M
↓
L
```

A regime shift may invalidate only the nodes whose assumptions depend on the old regime.

```text
REGIME SHIFT
!=
DELETE ALL KNOWLEDGE
```

Instead:

```text
REVALIDATE AFFECTED DEPENDENCY CLOSURE
```

---

# 25. Freshness

Freshness may differ by level.

```text
FRESHNESS(H)
!=
FRESHNESS(M)
!=
FRESHNESS(L)
!=
FRESHNESS(RAW)
```

An H summary may remain structurally valid while a load-bearing L value becomes stale.

Therefore:

```text
FRESH H
DOES NOT GUARANTEE
FRESH L
```

---

# 26. Freshness Escalation

If a conclusion depends on time-sensitive detail:

```text
H
↓
M
↓
STALE L
```

the system should revalidate the L dependency rather than automatically rebuilding the entire H tree.

---

# 27. Contradiction Handling

Contradictions should remain visible.

Example:

```text
H1
└── M1
    ├── L1 → CLAIM A
    └── L2 → CLAIM NOT-A
```

The correct state is not forced synthesis.

It may be:

```text
COMPETING
```

or:

```text
UNKNOWN/GAP
```

until discriminating evidence exists.

---

# 28. Cross-Branch Contradiction

Contradictions may exist across branches.

```text
H1/M2/L4
        \
         X
        /
H3/M1/L7
```

When both are load-bearing, local fast-path reasoning is no longer sufficient.

Escalation is required.

---

# 29. Competing Hypotheses

H/M/L supports parallel competing branches.

```text
H
└── M
    ├── L-HYPOTHESIS-A
    ├── L-HYPOTHESIS-B
    └── L-HYPOTHESIS-C
```

Do not collapse them merely for compactness.

Canonical rule:

```text
COMPRESSION
MUST PRESERVE
DECISION-RELEVANT COMPETITION.
```

---

# 30. Discriminating Retrieval

When hypotheses compete, retrieve evidence according to information value.

```text
COMPETING A / B
↓
WHAT OBSERVATION MOST CHEAPLY
DISTINGUISHES A FROM B?
↓
LOAD THAT PATH FIRST
```

This is preferable to indiscriminately loading more background.

---

# 31. Causal Firewall

H/M/L hierarchy does not establish causation.

```text
H STRUCTURE
↓
M STRUCTURE
↓
L STRUCTURE
```

does not imply:

```text
H CAUSES M
M CAUSES L
```

H/M/L edges may represent:

```text
CONTAINMENT
RESOLUTION
DEPENDENCY
REFERENCE
CLASSIFICATION
```

rather than causal relations.

---

# 32. Typed Edges

Material H/M/L edges should ideally be typed.

Possible edge types:

```text
CONTAINS
DEPENDS_ON
DERIVED_FROM
SUPPORTED_BY
CONTRADICTS
SUPERSEDES
IMPLEMENTS
GOVERNS
OBSERVES
CALIBRATES
REFERENCES
REQUIRES
INVALIDATES
```

Typed edges prevent structural ambiguity.

---

# 33. Authority Firewall

Knowledge resolution does not grant authority.

```text
HML RETRIEVAL
!=
AUTHORIZATION
```

Likewise:

```text
FOUND RELEVANT KNOWLEDGE
!=
PERMISSION TO EXECUTE
```

Governance and authority remain separate AMOS OS concerns.

---

# 34. Canon Firewall

H/M/L is not itself a canon promotion mechanism.

```text
HML ORGANIZATION
!=
CANONIZATION
```

A knowledge object must still pass the appropriate:

```text
PROVENANCE
VALIDATION
AUTHORITY
SUPERSESSION
PROMOTION
```

process.

---

# 35. Memory Firewall

Memory may use H/M/L.

But:

```text
MEMORY
!=
KNOWLEDGE
!=
CANON
```

Stored historical content can remain:

```text
SOURCE_CLAIM
STALE
SUPERSEDED
REJECTED
COMPETING
UNKNOWN
```

without being promoted.

---

# 36. Adaptive Retrieval Complexity

H/M/L integrates with AMOS adaptive complexity.

```text
C0 DIRECT
C1 COMPACT
C2 STRUCTURED
C3 DEEP
C4 MAXIMUM
```

Possible mapping:

```text
C0
→ known local answer / no expansion

C1
→ H only or H + one M

C2
→ H + relevant M + selected L

C3
→ dependency closure + RSCFs + selected evidence

C4
→ maximum justified traversal + adversarial validation
```

This mapping is operational guidance, not an absolute equivalence.

---

# 37. Escalation Conditions

Escalate deeper when material uncertainty remains in:

```text
EVIDENCE
MODEL
SCOPE
TEMPORAL VALIDITY
CAUSALITY
EXECUTION
PROVENANCE INDEPENDENCE
AUTHORITY
```

Also escalate for:

```text
CONTRADICTION
STALE PREMISE
REGIME SHIFT
CROSS-DOMAIN TRANSFER
IRREVERSIBLE ACTION
HIGH STAKES
AMBIGUOUS DEPENDENCIES
SHARED PROVENANCE ANCESTRY
```

---

# 38. De-Escalation

Stop expanding when outcome-changing uncertainty is resolved.

```text
ENOUGH EVIDENCE
+
DEPENDENCY CLOSURE
+
NO MATERIAL CONFLICT
+
VALID SCOPE
+
VALID REGIME
+
VALID FRESHNESS
=
STOP
```

Do not continue retrieval merely because more knowledge exists.

---

# 39. Claim Sufficiency

Claim sufficiency asks:

> Is there enough valid support to state the conclusion at its correct epistemic class?

If yes, further retrieval may be unnecessary.

---

# 40. Decision Sufficiency

Decision sufficiency asks:

> Is there enough information to distinguish among materially different decisions?

A conclusion can be incomplete yet decision-sufficient.

---

# 41. Action Sufficiency

Action sufficiency asks:

> Is there enough validated information and authority to choose a safe next action?

Action sufficiency may be reached before total explanatory completeness.

---

# 42. Stop Rule

Canonical stop condition:

```text
CLAIM SUFFICIENCY
+
DECISION SUFFICIENCY
+
ACTION SUFFICIENCY
```

subject to the task's actual requirements.

Exhaustiveness is not the default objective.

---

# 43. Sensitivity-Directed Traversal

Before expanding a large branch, identify the premise most capable of flipping the result.

```text
CONCLUSION
↓
SENSITIVITY ANALYSIS
↓
MOST DECISION-SENSITIVE PREMISE
↓
RELEVANT H/M/L PATH
↓
TEST FIRST
```

This minimizes low-value retrieval.

---

# 44. Uncertainty-Directed Traversal

Material uncertainty can be represented as a vector:

```text
U = [
  evidence,
  model,
  scope,
  temporal,
  causal,
  execution,
  provenance_independence
]
```

Retrieval should target the uncertainty dimension with the highest expected decision value.

---

# 45. Local Fast Path

AMOS v4.4 local reasoning is allowed when the required H/M/L dependency closure demonstrates:

```text
DEPENDENCY CLOSURE
PROVENANCE INDEPENDENCE
SCOPE COMPATIBILITY
REGIME COMPATIBILITY
FRESHNESS
NON-CONFLICT
```

If these are established:

```text
LOCAL PATH
→
LOCAL CONCLUSION
```

may be sufficient.

---

# 46. Fast-Path Escalation

Fast path must terminate when encountering:

```text
SHARED ANCESTRY
CONFLICT
STALE EVIDENCE
REGIME CROSSING
SCOPE LEAKAGE
CAUSAL COUPLING
GOVERNANCE IMPACT
IRREVERSIBLE STAKES
AMBIGUOUS DEPENDENCIES
```

Then:

```text
LOCAL
→
BROADER DEPENDENCY CLOSURE
```

---

# 47. Atomic Multi-RSCF Retrieval

A conclusion may depend on several RSCFs distributed across different H/M/L branches.

```text
H1/M2/L4 → RSCF_A
H2/M1/L7 → RSCF_B
H4/M3/L2 → RSCF_C
```

If all are load-bearing:

```text
A + B + C
=
ATOMIC DECISION SUPPORT SET
```

A partial set must not be mistaken for complete support.

---

# 48. Cross-H Dependency Closure

Some decisions cannot remain inside one H domain.

```text
H_LEGAL
      \
       \
        → DECISION
       /
H_FINANCIAL
       \
        \
H_OPERATIONAL
```

Cross-H retrieval is permitted when required.

The fast path must not become a silo.

---

# 49. Proof-Based Coordination Avoidance

Global traversal is unnecessary when locality can be proven.

Conceptually:

```text
LOCAL DEPENDENCIES CLOSED
+
NO MATERIAL EXTERNAL CONFLICT
+
PROVENANCE VALID
+
SCOPE/REGIME VALID
+
FRESHNESS VALID
→
NO GLOBAL RETRIEVAL REQUIRED
```

Locality must be demonstrated.

It must not be assumed from folder boundaries.

---

# 50. Persistent Provenance

Compression and caching should preserve lineage across sessions or persistent state where the implementation supports persistence.

Conceptually:

```text
PROOF CAPSULE
+
PROVENANCE POINTERS
+
VERSION / HASH
+
DEPENDENCY IDS
+
VALIDITY ENVELOPE
```

allows revalidation without full reconstruction.

This is an architectural requirement, not a claim that every current runtime already implements persistent provenance.

---

# 51. MVCC / CAS Alignment

Where AMOS implementations use versioned state concepts, H/M/L nodes may carry revision identity.

Conceptually:

```yaml
node_state:
  semantic_id:
  revision:
  content_hash:
  parent_revision:
  provenance:
```

A compare-and-swap style guard may conceptually require:

```text
EXPECTED_REVISION
==
CURRENT_REVISION
```

before authoritative replacement.

H/M/L does not itself implement MVCC or CAS.

It provides a compatible knowledge identity structure.

---

# 52. Supersession

New knowledge should not silently erase old knowledge.

```text
OLD NODE
↓
SUPERSEDED_BY
↓
NEW NODE
```

Historical provenance remains recoverable where required.

Canonical relation:

```text
SUPERSEDED
!=
NEVER EXISTED
```

---

# 53. Versioning

Canonical filenames should not require version suffixes.

Version identity belongs in metadata, provenance, hashes, revision history, or supersession records.

```text
FILENAME
!=
VERSION IDENTITY
```

H/M/L node identity should therefore distinguish:

```text
semantic_id
revision_id
content_hash
canon_state
```

where relevant.

---

# 54. Node Lifecycle

A conceptual H/M/L lifecycle may include:

```text
PLACEHOLDER
↓
SOURCE_CLAIM
↓
MODEL / DERIVED
↓
VALIDATED
↓
ACTIVE
↓
SUPERSEDED
↓
ARCHIVED
```

Not every artifact must traverse every state.

Promotion requires explicit governance.

---

# 55. Placeholder Firewall

A placeholder may reserve structure.

It does not establish content.

```text
PLACEHOLDER EXISTS
!=
IMPLEMENTATION EXISTS
```

Likewise:

```text
H NODE EXISTS
!=
DOMAIN COMPLETE

M NODE EXISTS
!=
SUBSYSTEM IMPLEMENTED

L NODE EXISTS
!=
CLAIM VALIDATED
```

---

# 56. Missing Branches

If an expected H/M/L branch does not exist:

```text
EXPECTED NODE
+
NO VALID CONTENT
→
UNKNOWN/GAP
```

Do not synthesize a missing canonical branch merely because its structure appears predictable.

---

# 57. Gap Classification

Missing H/M/L information should be classified:

```text
CRITICAL
DECISION-RELEVANT
EXPLANATORY
COSMETIC
```

Priority:

```text
CRITICAL
↓
DECISION-RELEVANT
↓
EXPLANATORY
↓
COSMETIC
```

---

# 58. Failure Recovery

If an H/M/L node is invalidated:

```text
INVALID NODE
↓
IDENTIFY DEPENDENTS
↓
INVALIDATE DEPENDENT PROOF EDGES
↓
PRESERVE UNAFFECTED NODES
↓
RETURN TO NEAREST VALID STATE
↓
REROUTE
```

Global recomputation is a last resort.

---

# 59. No Failed-Path Repetition

A failed retrieval path should not simply be repeated.

```text
FAILED PATH
+
UNCHANGED EVIDENCE
→
DO NOT RETRY IDENTICALLY
```

Retry requires a changed condition:

```text
NEW EVIDENCE
NEW SOURCE
NEW SCOPE
NEW REGIME
NEW MODEL
NEW DEPENDENCY PATH
```

---

# 60. H/M/L and the 7-Part Universe

H/M/L can recursively organize knowledge about every part of the AMOS 7-Part Universe.

```text
P1 REALITY
├── H
├── M
└── L

P2 SENSE
├── H
├── M
└── L

P3 KNOWLEDGE
├── H
├── M
└── L

P4 COGNITION
├── H
├── M
└── L

P5 GOVERNANCE
├── H
├── M
└── L

P6 EXECUTION
├── H
├── M
└── L

P7 EVOLUTION
├── H
├── M
└── L
```

Therefore:

```text
7-PART UNIVERSE
=
SEMANTIC RESPONSIBILITY DECOMPOSITION

H/M/L
=
FRACTAL RESOLUTION DECOMPOSITION
```

They are complementary.

---

# 61. H/M/L and AMOS OS Repository Planes

H/M/L must not be confused with repository depth.

```text
H != ROOT FOLDER
M != SUBFOLDER
L != FILE
```

A root file may contain L-level detail.

A deeply nested artifact may serve as H-level orientation for a local domain.

H/M/L is semantic resolution.

---

# 62. Knowledge Plane Mapping

Primary repository relationships may include:

```text
11_KNOWLEDGE
├── H domain structures
├── M subsystem structures
├── L detail structures
├── RSCF structures
├── evidence references
└── provenance references

10_MEMORY
└── persistent/retrievable historical structures

12_STATE
└── current authoritative/working state

13_MODELS
└── model structures referenced by H/M/L

22_RESEARCH
└── source evidence / experiments
```

This mapping is architectural rather than proof of current implementation.

---

# 63. H/M/L Node Contract

A mature node may follow:

```yaml
hml_node:
  node_id:
  semantic_id:

  resolution:
    level: H | M | L
    parent:
    children: []

  title:
  purpose:

  claim_class:

  scope:
  regime:
  freshness:

  dependencies: []

  provenance:
    source_ids: []
    ancestry: []
    content_hash:
    revision:

  rscf_refs: []

  evidence_refs: []

  competing_nodes: []

  falsifiers: []

  authority:
    owner:
    promotion_state:

  lifecycle:
    status:
    supersedes:
    superseded_by:

  retrieval:
    bootstrap_priority:
    escalation_conditions: []
    raw_evidence_policy:

  validation:
    last_validated:
    validation_refs: []
```

---

# 64. H Node Minimum Contract

An H node should answer at minimum:

```text
WHAT DOMAIN?
WHAT PURPOSE?
WHAT BOUNDARY?
WHAT MAJOR INVARIANTS?
WHAT MAJOR SUBSYSTEMS?
WHAT AUTHORITY BOUNDARY?
WHAT KNOWN GAPS?
WHERE TO EXPAND NEXT?
```

---

# 65. M Node Minimum Contract

An M node should answer:

```text
WHAT SUBSYSTEM?
WHAT RESPONSIBILITY?
WHAT INPUTS?
WHAT OUTPUTS?
WHAT DEPENDENCIES?
WHAT INVARIANTS?
WHAT FAILURE MODES?
WHAT L DETAILS CAN CHANGE THE RESULT?
```

---

# 66. L Node Minimum Contract

An L node should answer:

```text
WHAT EXACT CLAIM / RULE?
WHAT PREMISES?
WHAT EVIDENCE?
WHAT PROVENANCE?
WHAT SCOPE?
WHAT REGIME?
WHAT FRESHNESS?
WHAT FALSIFIES IT?
WHAT DEPENDS ON IT?
```

---

# 67. Retrieval Trace

Consequential retrieval should be traceable conceptually as:

```yaml
retrieval_trace:
  objective:

  starting_h:

  visited:
    - node:
      reason:
      materiality:

  skipped:
    - node:
      reason:

  escalations: []

  evidence_loaded: []

  unresolved_gaps: []

  stop_reason:
```

This does not require exposing hidden chain-of-thought.

The trace records material retrieval decisions, not private internal reasoning.

---

# 68. Adversarial Validation

For consequential conclusions, a separate challenge path should test the selected H/M/L proof.

Challenge targets include:

```text
CONTRADICTION
SHARED PROVENANCE
STALE PREMISES
SCOPE LEAKAGE
REGIME MISMATCH
HIDDEN DEPENDENCY
CAUSAL OVERREACH
STRONGER COMPETING MODEL
```

If challenge succeeds:

```text
VERIFIED → DERIVED
DERIVED → CONDITIONAL
CONDITIONAL → COMPETING
COMPETING → UNKNOWN/GAP
```

as appropriate.

---

# 69. Confidence Ceiling

A high-level summary cannot carry confidence greater than its weakest load-bearing support unless independently revalidated.

Conceptually:

```text
CONFIDENCE(H)
≤
MIN(
  LOAD-BEARING M/L/RSCF CONFIDENCE
)
```

for the specific claim being made.

This is claim-local, not necessarily a single confidence score for the entire H node.

---

# 70. Compression Boundary

When L details are summarized into M:

```text
L1 + L2 + L3
↓
M SUMMARY
```

the M summary must preserve:

```text
DECISION-RELEVANT QUALIFIERS
CONTRADICTIONS
SCOPE
REGIME
FRESHNESS
PROVENANCE
CONFIDENCE CEILING
```

The same applies from M to H.

---

# 71. Lossy Compression Rule

Lossy compression is permitted only for information that cannot materially alter the target outcome.

```text
NON-MATERIAL DETAIL
→
MAY COMPRESS
```

but:

```text
LOAD-BEARING DETAIL
→
MUST REMAIN RECOVERABLE
```

---

# 72. Anti-Fluency Rule

A missing L node must not be bridged with plausible prose.

```text
H CLAIM
↓
M CLAIM
↓
L = MISSING
```

requires:

```text
UNKNOWN/GAP
```

where the missing L detail is load-bearing.

Not:

```text
PLAUSIBLE COMPLETION
```

---

# 73. H/M/L Minimal Invariants

```text
HML-001 H/M/L ARE RESOLUTION ROLES, NOT TRUTH LEVELS

HML-002 H/M/L ROLE != SEMANTIC IDENTITY

HML-003 H/M/L ROLE != REPOSITORY DEPTH

HML-004 HIGH LEVEL != HIGH CONFIDENCE

HML-005 STORED != VERIFIED

HML-006 SUMMARY != SOURCE

HML-007 MULTIPLE DESCENDANTS != INDEPENDENT SOURCES

HML-008 COMPRESSION MUST PRESERVE MATERIAL PROVENANCE

HML-009 COMPRESSION MUST PRESERVE MATERIAL CONTRADICTIONS

HML-010 SCOPE MUST NOT SILENTLY EXPAND

HML-011 REGIME CROSSING REQUIRES VALIDATION

HML-012 FRESHNESS IS DEPENDENCY-SPECIFIC

HML-013 RAW EVIDENCE DEFAULTS TO DO_NOT_LOAD_UNLESS_REQUIRED

HML-014 RAW EVIDENCE MUST BE RETRIEVABLE WHEN LOAD-BEARING

HML-015 RETRIEVAL FOLLOWS MATERIAL DEPENDENCIES

HML-016 LOCALITY MUST BE DEMONSTRATED, NOT ASSUMED

HML-017 UNKNOWN/GAP != PASS

HML-018 PLACEHOLDER != IMPLEMENTATION

HML-019 RSCF != HML NODE

HML-020 HML RETRIEVAL != AUTHORITY

HML-021 HML ORGANIZATION != CANONIZATION

HML-022 FAILED DEPENDENCIES INVALIDATE ONLY THEIR DESCENDANTS

HML-023 COMPETING HYPOTHESES MUST REMAIN VISIBLE

HML-024 STRUCTURAL HIERARCHY != CAUSAL HIERARCHY

HML-025 OPTIMIZATION MUST NOT WEAKEN INTEGRITY
```

---

# 74. Canonical Retrieval Algorithm

Conceptually:

```text
1. PARSE OBJECTIVE
2. IDENTIFY TARGET CLAIM / DECISION / ACTION
3. LOAD H BOOTSTRAP
4. IDENTIFY MATERIAL M BRANCH
5. LOAD ONLY REQUIRED M NODES
6. IDENTIFY LOAD-BEARING L NODES
7. CHECK:
   - provenance
   - scope
   - regime
   - freshness
   - contradictions
   - dependency closure
8. LOAD RAW EVIDENCE IF REQUIRED
9. BUILD / REUSE RSCF PROOF CAPSULES
10. CHALLENGE CONSEQUENTIAL CONCLUSIONS
11. RESOLVE OR PRESERVE COMPETING HYPOTHESES
12. STOP WHEN SUFFICIENCY IS REACHED
13. RETURN CORRECT CONCLUSION CLASS
```

---

# 75. Retrieval Pseudocode

```text
function resolve(target):

    h = bootstrap(target.domain)

    branch = select_material_M(h, target)

    if branch == NONE:
        return UNKNOWN/GAP

    m = retrieve(branch)

    details = select_load_bearing_L(m, target)

    for l in details:

        validate_scope(l)
        validate_regime(l)
        validate_freshness(l)
        validate_provenance(l)

        if evidence_required(l):
            retrieve_raw_evidence(l)

    closure = dependency_closure(details)

    if closure.has_material_gap:
        return UNKNOWN/GAP

    if closure.has_unresolved_competition:
        return COMPETING

    conclusion = synthesize(closure)

    if consequential(conclusion):
        conclusion = adversarial_validate(conclusion)

    return weakest_accurate_class(conclusion)
```

This pseudocode is a structural model.

It is not asserted to be literal AMOS runtime implementation.

---

# 76. Anti-Patterns

The following violate H/M/L canon:

```text
LOAD ENTIRE CORPUS BY DEFAULT

ASSUME ROOT NODE IS AUTHORITATIVE

TREAT SUMMARY AS PRIMARY EVIDENCE

DROP PROVENANCE DURING COMPRESSION

COUNT COPIES AS INDEPENDENT SOURCES

HIDE CONTRADICTIONS IN HIGH-LEVEL SUMMARIES

EXPAND EVERY BRANCH REGARDLESS OF MATERIALITY

INFER MISSING CANON FROM FOLDER STRUCTURE

ASSUME REPOSITORY DEPTH == HML LEVEL

PROMOTE MODEL TO FACT THROUGH REPEATED SUMMARIZATION

REUSE STALE PROOF CAPSULES ACROSS REGIME SHIFTS

ALLOW FAST PATH WITHOUT DEPENDENCY CLOSURE
```

---

# 77. Validation Requirements

An H/M/L implementation should eventually test:

```text
H → M ROUTING
M → L ROUTING
DEPENDENCY CLOSURE
PROVENANCE RECOVERY
SCOPE INHERITANCE
REGIME INVALIDATION
FRESHNESS INVALIDATION
CONTRADICTION PRESERVATION
COMPETING HYPOTHESIS PRESERVATION
RAW EVIDENCE ESCALATION
PROOF CAPSULE REUSE
LOCAL INVALIDATION
CROSS-H DEPENDENCIES
SYBIL / SHARED-ANCESTRY DETECTION
STOP CONDITIONS
```

---

# 78. Canon Promotion Gate

Promotion:

```text
ACTIVE_CANON_CANDIDATE
→
ACTIVE_CANON
```

requires canonical review of:

* exact H/M/L definitions;
* recursive semantics;
* node identity;
* RSCF relationship;
* provenance topology;
* retrieval rules;
* dependency closure;
* scope inheritance;
* regime handling;
* freshness semantics;
* contradiction preservation;
* competing-hypothesis behavior;
* raw-evidence escalation;
* fast-path conditions;
* proof reuse;
* invalidation behavior;
* version/supersession behavior;
* repository mappings;
* implementation/test evidence where implementation claims are made.

Until then, this document remains an AMOS architectural model.

---

# 79. RSCF Node

```yaml
node_id: AMOS_HML_CANON

functional_type:
  - CANONICAL_KNOWLEDGE_MODEL
  - FRACTAL_RESOLUTION_MODEL
  - RETRIEVAL_MODEL
  - DEPENDENCY_TRAVERSAL_MODEL

lifecycle_stage:
  CANON_CANDIDATE

origin_architect:
  Trang Phan

steward:
  Trang Phan

amos_core_target:
  v4.4

claim_class:
  AMOS_MODEL

claim: >
  AMOS knowledge can be organized and retrieved through recursive
  H/M/L resolution roles—H domain, M subsystem, and L detail—with
  raw evidence loaded only when required by material dependency,
  validation, contradiction, provenance, scope, regime, freshness,
  or uncertainty conditions.

dependencies:
  - "AMOS_CORE_LAWS"
  - "INVARIANT_REGISTRY"
  - "LAW_HIERARCHY"
  - "AMOS_7_PART_UNIVERSE_CANON"
  - "ARCHITECTURE"

critical_invariants:
  - H/M/L ARE RESOLUTION ROLES
  - HIGH LEVEL != HIGH CONFIDENCE
  - SUMMARY != SOURCE
  - RAW EVIDENCE DEFAULTS TO DO_NOT_LOAD_UNLESS_REQUIRED
  - MATERIAL EVIDENCE MUST REMAIN RETRIEVABLE
  - PROVENANCE MUST SURVIVE MATERIAL COMPRESSION
  - DEPENDENCY CLOSURE PRECEDES LOCAL FINALIZATION
  - INDEPENDENCE MUST BE DEMONSTRATED
  - SCOPE MUST NOT SILENTLY EXPAND
  - REGIME SHIFTS REQUIRE LOCAL REVALIDATION
  - COMPETING HYPOTHESES MUST REMAIN VISIBLE
  - UNKNOWN/GAP != PASS

does_not_establish:
  - empirical proof of a universal three-level ontology
  - implementation completeness
  - automatic canon authority for H nodes
  - equivalence between H/M/L and repository depth
  - automatic provenance independence
  - automatic correctness of compressed summaries
  - literal implementation of every v4.4 distributed-state mechanism
```

---

# 80. Status Boundary

H/M/L is an AMOS architectural and reasoning model.

It should not be presented as proof that all knowledge in reality naturally possesses exactly three intrinsic levels.

```text
H/M/L
=
AMOS FRACTAL RESOLUTION MODEL
```

not:

```text
H/M/L
=
EMPIRICALLY VERIFIED UNIVERSAL ONTOLOGY
```

The number of physical files, modules, database levels, or runtime components does not need to equal three.

---

# 81. Changelog

## v2.0.0 — 2026-08-25

Expanded the placeholder into an AMOS v4.4-aligned H/M/L canon candidate.

Added:

* formal H/M/L definitions;
* raw-evidence layer;
* recursive/fractal semantics;
* contextual resolution roles;
* identity firewall;
* smallest-sufficient retrieval;
* dependency-directed traversal;
* bootstrap capsules;
* RSCF integration;
* proof capsule reuse;
* provenance preservation;
* provenance topology and Sybil hardening;
* scope/regime/freshness inheritance;
* contradiction handling;
* competing hypotheses;
* causal firewall;
* authority/canon/memory firewalls;
* adaptive complexity;
* claim/decision/action sufficiency;
* sensitivity-directed retrieval;
* uncertainty-directed retrieval;
* v4.4 fast-path conditions;
* atomic multi-RSCF retrieval;
* cross-H dependency closure;
* proof-based coordination avoidance;
* persistent provenance alignment;
* MVCC/CAS conceptual alignment;
* supersession/versioning;
* lifecycle semantics;
* placeholder firewall;
* local failure recovery;
* 7-Part Universe mapping;
* node contracts;
* retrieval trace;
* adversarial validation;
* confidence ceilings;
* compression invariants;
* canonical retrieval algorithm;
* anti-patterns;
* validation requirements.

## v1.0.0 — 2026-08-25

Initial placeholder reserved the canonical AMOS OS location.

---

# 82. Canonical Summary

```text
H
=
DOMAIN ORIENTATION
WHAT SYSTEM / DOMAIN ARE WE IN?

M
=
SUBSYSTEM RESOLUTION
WHAT MECHANISM OR BRANCH CONTROLS THE RESULT?

L
=
LOAD-BEARING DETAIL
WHAT EXACT CLAIM, PREMISE, RULE, OR PARAMETER MATTERS?

RAW
=
PRIMARY EVIDENCE
WHAT SOURCE OR OBSERVATION ACTUALLY SUPPORTS THE DETAIL?
```

Canonical traversal:

```text
OBJECTIVE
↓
H
↓
MATERIAL M
↓
LOAD-BEARING L
↓
RAW EVIDENCE IF REQUIRED
↓
RSCF / DEPENDENCY CLOSURE
↓
VALIDATION
↓
CONCLUSION
```

Canonical stop law:

```text
DO NOT LOAD MORE
MERELY BECAUSE MORE EXISTS.
```

Canonical escalation law:

```text
IF MISSING INFORMATION
CAN MATERIALLY CHANGE
CLAIM / DECISION / ACTION,
ESCALATE.
```

Canonical integrity law:

```text
COMPRESSION
MUST NEVER
OUTRUN PROVENANCE,
DEPENDENCY,
SCOPE,
REGIME,
FRESHNESS,
OR CONTRADICTION.
```

And the hard boundaries remain:

```text
H/M/L ROLE != TRUTH LEVEL
H/M/L ROLE != REPOSITORY DEPTH
HIGH LEVEL != HIGH CONFIDENCE
SUMMARY != SOURCE
MEMORY != CANON
MODEL != AUTHORITY
MULTIPLE DESCENDANTS != INDEPENDENT SOURCES
STRUCTURAL HIERARCHY != CAUSAL HIERARCHY
PLACEHOLDER != IMPLEMENTATION
UNKNOWN/GAP != PASS
```

---

**Related:** README|AMOS OS · 00_ROOT_MOC|MOC · ARCHITECTURE|Architecture · SYSTEM_MAP|System Map · NEURAL_NETWORK|AMOS Neural Network · AUTHORITATIVE_STATE|Authoritative State · PLACEMENT_RULES|Placement Rules · AMOS Canon · CANON_MAP|Canon Map · AMOS_CORE_LAWS|AMOS Core Laws · INVARIANT_REGISTRY|Invariant Registry · LAW_HIERARCHY|Law Hierarchy · AMOS_7_PART_UNIVERSE_CANON|AMOS 7-Part Universe Canon · KERNEL_MAP|Kernel Map · CONTROL_PLANE_MAP|Control Plane Map · COGNITIVE_ORGANISM_MAP|Cognitive Organism · MEMORY_MEMORY_MAP|Memory Map · AMOS_FULL_BRAIN_OS_ARCHITECTURE|AMOS Full Brain OS Architecture · Knowledge Map · STATE_STATE_MAP|State Map · MODEL_MAP|Model Map · SCHEMA_MAP|Schema Map · OBSERVABILITY_OBSERVABILITY_MAP|Observability Map · TEST_MAP|Test Map · INDEX_RESEARCH_README|Research · COGNITIVE_MATRIX_ARCHITECTURE|Cognitive Matrix

```
```

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: hml_canon
node_type: note
path: 01_CANON/02_UNIVERSE_CANON/HML_CANON.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[02_UNIVERSE_CANON_MOC]]
