---
artifact_id: AMOS-SYMBOL-REGISTRY
name: SYMBOL_REGISTRY
title: "AMOS Symbol Registry — Canonical Symbols, Operators, Types, States, and Semantic Identity"

document_version: "1.0.0"
canon_version: "4.4"
amos_core_target: "v4.4"

status: ACTIVE_CANON_CANDIDATE
conclusion_class: AMOS_MODEL
rscf_state: derived

canon_group: meta
canon_type: registry

origin_architect: Trang Phan
steward: Trang Phan

created: 2026-08-25
updated: 2026-08-25

tags:
  - amos
  - amos-os
  - amos-core
  - amos-core-v4-4
  - canon
  - registry
  - symbol-registry
  - symbols
  - notation
  - operators
  - semantics
  - identity
  - types
  - states
  - rscf
  - gmef
  - hml
  - provenance
  - epistemic-regime
  - causal-lineage
  - mvcc
  - cas
  - finality
  - invariants
  - canon-group/meta
  - canon/registry
  - rscf/provenance
  - rscf/state/derived
  - topic/symbol-registry

aliases:
  - AMOS Symbol Registry
  - Symbol Registry
  - AMOS Notation Registry
  - AMOS Semantic Symbol Table
---

# AMOS Symbol Registry

**Origin architect / steward:** Trang Phan

> **Status:** `ACTIVE_CANON_CANDIDATE`  
> **AMOS Core target:** `v4.4`  
> **Conclusion class:** `AMOS_MODEL`

---

# 0. Purpose

The **AMOS Symbol Registry** provides the canonical location for registering symbols, abbreviations, operators, state labels, conclusion classes, structural identifiers, and formal notation used throughout AMOS OS.

Its primary purpose is semantic stability.

```text
ONE SYMBOL
→ ONE REGISTERED MEANING WITHIN A DECLARED SCOPE
```

The registry prevents silent semantic drift between:

```text
CANON
KERNEL
CONTROL PLANE
RUNTIME
COGNITION
AGENTS
SKILLS
WORKFLOWS
MEMORY
KNOWLEDGE
STATE
MODELS
RESEARCH
```

A symbol's appearance does not by itself establish its meaning.

```text
SYMBOL
!=
SEMANTICS
```

Meaning is determined by its registered definition, scope, type, version, and applicable canon.

---

# 1. Registry Boundary

The Symbol Registry records semantic identities.

It does not independently create implementation behavior.

```text
SYMBOL REGISTRATION
!=
IMPLEMENTATION
```

It also does not independently establish empirical truth.

```text
DEFINED SYMBOL
!=
VERIFIED CLAIM
```

And it does not create authority merely by naming something.

```text
SYMBOL
!=
AUTHORITY
```

---

# 2. Core Identity Law

AMOS distinguishes:

```text
DISPLAY NAME
!=
SYMBOL
!=
ARTIFACT ID
!=
REGISTRY ID
!=
SEMANTIC IDENTITY
!=
IMPLEMENTATION IDENTITY
!=
VERSION IDENTITY
```

These identities may reference one another.

They must not be silently collapsed.

---

# 3. Symbol Record

Every consequential registered symbol should eventually support:

```yaml
symbol:
  symbol_id:
  notation:
  canonical_name:
  symbol_type:
  definition:
  scope:
  namespace:
  semantic_identity:
  aliases: []
  dependencies: []
  conflicts: []
  provenance:
  introduced_in:
  supersedes:
  deprecated_by:
  status:
```

Unknown fields remain:

```text
UNKNOWN/GAP
```

They must not be inferred merely from notation.

---

# 4. Symbol Types

Canonical symbol classes may include:

```text
SYSTEM
SUBSYSTEM
STRUCTURE
TYPE
STATE
CONCLUSION_CLASS
OPERATOR
RELATION
VARIABLE
FUNCTION
SET
REGISTRY
PROTOCOL
IDENTIFIER
AUTHORITY_CLASS
EVIDENCE_CLASS
REGIME
LIFECYCLE_STATE
CONTROL_STATE
PROVENANCE_TYPE
TEMPORAL_TYPE
CAUSAL_TYPE
```

Additional classes require explicit registration.

---

# 5. AMOS Core Structural Symbols

| Symbol      | Canonical meaning                                                                              |
| ----------- | ---------------------------------------------------------------------------------------------- |
| `AMOS`      | Architectural framework/system family governed by AMOS canon                                   |
| `AMOS OS`   | Integrated AMOS operating architecture                                                         |
| `AMOS Core` | Core deterministic reasoning and governance lineage                                            |
| `RSCF`      | Recursive Structured Cognitive Framework / registered AMOS structure as defined by bound canon |
| `GMEF`      | Registered AMOS GMEF structure; exact expansion must follow authoritative canon                |
| `H`         | High-level/domain layer in H/M/L decomposition                                                 |
| `M`         | Mid-level/subsystem layer in H/M/L decomposition                                               |
| `L`         | Low-level/detail layer in H/M/L decomposition                                                  |
| `H/M/L`     | Recursive hierarchical decomposition pattern                                                   |

## Integrity note

Where an acronym's exact canonical expansion is not bound to an authoritative source, this registry preserves the symbol without inventing an expansion.

```text
KNOWN SYMBOL
+
UNKNOWN EXPANSION
=
PRESERVE SYMBOL
+
MARK GAP
```

---

# 6. H/M/L Symbols

Canonical structural interpretation:

```text
H
=
DOMAIN / HIGH-LEVEL STRUCTURE

M
=
SUBSYSTEM / MID-LEVEL STRUCTURE

L
=
DETAIL / LOW-LEVEL STRUCTURE
```

Conceptually:

```text
H
↓
M
↓
L
```

The decomposition is recursive.

Therefore:

```text
H
├── M1
│   ├── L1
│   └── L2
└── M2
    └── L3
```

may itself contain further H/M/L decomposition where canon permits.

---

# 7. RSCF Symbols

The registry reserves:

```text
RSCF
RSCF_ID
RSCF_STATE
RSCF_DEPENDENCY
RSCF_PROVENANCE
RSCF_SCOPE
RSCF_REGIME
RSCF_CONFIDENCE
```

for RSCF-related semantic identities.

A registered RSCF reference should not be reduced to an untyped text label where its identity is load-bearing.

---

# 8. Evidence Classes

Canonical evidence/knowledge typing includes:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN
```

These labels are semantically distinct.

---

# 9. SOURCE_CLAIM

```text
SOURCE_CLAIM
```

means a claim attributed to a source.

It does not mean the claim is verified.

Canonical law:

```text
SOURCE_CLAIM
!=
VERIFIED
```

---

# 10. OBSERVATION

```text
OBSERVATION
```

represents an observed or measured state within a defined measurement and scope envelope.

Canonical law:

```text
OBSERVATION
!=
UNIVERSAL FACT
```

An observation inherits:

```text
TIME
ENVIRONMENT
METHOD
SCOPE
PROVENANCE
```

where material.

---

# 11. DERIVED

```text
DERIVED
```

represents a conclusion produced from other premises or evidence.

Canonical law:

```text
DERIVED CONFIDENCE
<=
WEAKEST LOAD-BEARING PREMISE
```

unless independent revalidation exists.

---

# 12. MODEL

```text
MODEL
```

represents an explanatory, structural, computational, conceptual, or predictive representation.

Canonical firewall:

```text
MODEL
!=
REALITY
```

and:

```text
MODEL
!=
AUTHORITY
```

---

# 13. DECISION

```text
DECISION
```

represents a governed selection or commitment.

Canonical firewall:

```text
DECISION
!=
EVIDENCE
```

A decision may depend on evidence but remains a different semantic type.

---

# 14. UNKNOWN

```text
UNKNOWN
```

means required information is not established.

It is not equivalent to:

```text
FALSE
```

or:

```text
ZERO
```

or:

```text
PASS
```

Canonical law:

```text
UNKNOWN/GAP != PASS
```

---

# 15. Conclusion Classes

AMOS conclusion classes include:

```text
VERIFIED
DERIVED
MODEL
CONDITIONAL
COMPETING
UNKNOWN/GAP
```

Use the weakest accurate class.

---

# 16. VERIFIED

```text
VERIFIED
```

means the claim satisfies the applicable verification standard within its declared scope, regime, provenance, and freshness envelope.

It does not imply universal truth.

```text
VERIFIED IN SCOPE S
!=
VERIFIED IN ALL SCOPES
```

---

# 17. CONDITIONAL

```text
CONDITIONAL
```

means the conclusion depends materially on one or more unresolved assumptions, thresholds, regimes, or premises.

Conceptually:

```text
IF P
→ C
```

where failure of `P` may invalidate `C`.

---

# 18. COMPETING

```text
COMPETING
```

means multiple incompatible hypotheses remain materially viable.

```text
H1
↔
H2
```

does not authorize forced convergence.

Canonical rule:

```text
INSUFFICIENT DISCRIMINATING EVIDENCE
→
PRESERVE COMPETING
```

---

# 19. UNKNOWN/GAP

```text
UNKNOWN/GAP
```

means the required evidence, definition, dependency, provenance, or validation is absent or insufficient.

Gap classes may include:

```text
CRITICAL
DECISION-RELEVANT
EXPLANATORY
COSMETIC
```

---

# 20. Core Logical Operators

The registry recognizes the following notation conventions.

| Symbol | Meaning                                                        |
| ------ | -------------------------------------------------------------- |
| `=`    | defined/equal within stated semantics                          |
| `!=`   | explicitly not equivalent                                      |
| `→`    | transition, implication, or directed flow according to context |
| `↓`    | ordered flow/decomposition                                     |
| `↑`    | increase or upward relation where declared                     |
| `<=`   | less than or equal / confidence ceiling relation               |
| `>=`   | greater than or equal                                          |
| `<`    | less than                                                      |
| `>`    | greater than                                                   |
| `∈`    | membership                                                     |
| `∉`    | non-membership                                                 |
| `∅`    | empty set                                                      |
| `∧`    | logical AND                                                    |
| `∨`    | logical OR                                                     |
| `¬`    | logical NOT                                                    |

Context must disambiguate overloaded mathematical notation.

---

# 21. Non-Equivalence Operator

AMOS uses:

```text
A != B
```

as a strong semantic firewall.

Examples:

```text
CANON != KERNEL

KERNEL != CONTROL_PLANE

CONTROL_PLANE != RUNTIME

RUNTIME != COGNITION

ORGAN != AGENT

AGENT != SKILL

SKILL != WORKFLOW

WORKFLOW != PROTOCOL

MEMORY != CANON

MODEL != AUTHORITY

TOOL != PERMISSION

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT
```

`!=` must not be interpreted merely as numeric inequality in these contexts.

It expresses architectural non-equivalence.

---

# 22. Direction Operator

```text
A → B
```

may represent:

```text
TRANSITION

DEPENDENCY DIRECTION

INFERENCE

CONTROL FLOW

CAUSAL CLAIM
```

depending on explicit typing.

Therefore:

```text
A → B
```

alone does not prove causality.

---

# 23. Causal Firewall

A causal edge must be distinguished from:

```text
ASSOCIATION

CORRELATION

SEQUENCE

DEPENDENCY

ENABLEMENT

MEDIATION

CONFOUNDING

FEEDBACK
```

Canonical law:

```text
STRUCTURAL EDGE
!=
CAUSAL EDGE
```

---

# 24. Dependency Symbols

Conceptual dependency notation:

```text
A
↓
B
```

may mean:

```text
A DEPENDS ON B
```

only where the relationship is explicitly defined that way.

A richer representation should eventually use:

```yaml
dependency:
  from:
  to:
  dependency_type:
  load_bearing:
  scope:
  regime:
  freshness:
```

---

# 25. Provenance Symbols

Reserved provenance concepts include:

```text
PROVENANCE
SOURCE_ID
SOURCE_ANCESTRY
PARENT_SOURCE
DERIVED_FROM
SUPERSEDES
SUPERSEDED_BY
HASH
REVISION
VERSION
EPOCH
```

Canonical law:

```text
MULTIPLE DESCENDANTS
!=
MULTIPLE INDEPENDENT SOURCES
```

---

# 26. Independence Symbol

Where useful:

```text
A ⫫ B
```

may represent an asserted independence relationship.

However:

```text
A ⫫ B
```

must not be assigned merely because A and B have different names.

Independence requires evidence.

---

# 27. Correlated Provenance

Conceptually:

```text
SOURCE S
├── CLAIM A
├── CLAIM B
└── CLAIM C
```

means:

```text
A
B
C
```

share ancestry.

Therefore:

```text
COUNT(A,B,C) = 3
```

does not imply:

```text
INDEPENDENT_CONFIRMATIONS = 3
```

---

# 28. Confidence Symbols

Where numerical confidence is used, reserve:

```text
C
```

or explicitly namespaced alternatives such as:

```text
CONFIDENCE
C_claim
C_evidence
```

A bare numerical confidence value must not hide its meaning.

Canonical law:

```text
C_derived
<=
MIN(C_load_bearing_premises)
```

unless independently revalidated.

---

# 29. Uncertainty Symbols

AMOS uncertainty may be represented as a vector:

```text
U
=
[
U_evidence,
U_model,
U_scope,
U_temporal,
U_causal,
U_execution,
U_provenance
]
```

where:

```text
U_evidence
```

represents evidence uncertainty;

```text
U_model
```

model uncertainty;

```text
U_scope
```

scope uncertainty;

```text
U_temporal
```

freshness/time uncertainty;

```text
U_causal
```

causal uncertainty;

```text
U_execution
```

execution uncertainty;

and:

```text
U_provenance
```

provenance-independence uncertainty.

---

# 30. Scope Symbol

Reserve:

```text
S
```

for scope only where explicitly declared.

A scope envelope may include:

```text
SYSTEM / POPULATION
ENVIRONMENT
SCALE
TIME
REGIME
MEASUREMENT METHOD
ASSUMPTIONS
```

Canonical law:

```text
VALID(S1)
!=
VALID(S2)
```

unless scope transfer is established.

---

# 31. Regime Symbol

Reserve:

```text
R
```

or:

```text
REGIME
```

for epistemic/operational regime where explicitly declared.

Example:

```text
R_normal
R_degraded
R_recovery
```

Conclusions inherit regime validity.

---

# 32. Temporal Symbols

Canonical temporal notation may include:

```text
t
t0
t1
t2
Δt
```

where:

```text
t
```

represents time within a defined clock/reference system.

Canonical firewall:

```text
VALID AT t1
!=
VALID AT t2
```

when freshness conditions may have changed.

---

# 33. Freshness

Reserve:

```text
FRESHNESS
TTL
VALID_UNTIL
REVALIDATE_AT
```

as semantic concepts.

A freshness-bound claim should eventually carry:

```yaml
temporal_validity:
  observed_at:
  valid_from:
  valid_until:
  ttl:
  revalidate_at:
```

where applicable.

---

# 34. Version Symbols

Version identity must be explicitly typed.

Preferred forms:

```text
CANON_VERSION
DOCUMENT_VERSION
SCHEMA_VERSION
STATE_VERSION
RUNTIME_VERSION
MODEL_VERSION
ARTIFACT_VERSION
```

Canonical firewall:

```text
CANON_VERSION
!=
DOCUMENT_VERSION
!=
STATE_VERSION
!=
RUNTIME_VERSION
```

---

# 35. AMOS Core Version

```text
v4.4
```

in this registry refers to the targeted AMOS Core lineage version where explicitly identified as:

```text
AMOS_CORE_VERSION
```

A filename containing `v4.4` does not independently establish canonical version identity.

---

# 36. State Version

Reserve:

```text
V
V0
V1
Vn
```

for state-version notation only when context explicitly establishes it.

Example:

```text
V42
→
V43
```

represents a state transition.

It does not necessarily represent a software release.

---

# 37. MVCC

```text
MVCC
```

is reserved for:

```text
MULTI-VERSION CONCURRENCY CONTROL
```

when used in its standard concurrency-control meaning.

Within AMOS reasoning architecture it denotes the associated version-aware concurrency concept, not proof that a specific database implementation exists.

---

# 38. CAS

```text
CAS
```

is reserved for:

```text
COMPARE-AND-SWAP
```

when used in the AMOS concurrency/state context.

Conceptually:

```text
EXPECTED_VERSION
=
CURRENT_VERSION
→
COMMIT MAY PROCEED
```

otherwise:

```text
EXPECTED_VERSION
!=
CURRENT_VERSION
→
CONFLICT
```

---

# 39. Conflict

Reserve:

```text
CONFLICT
```

for an incompatible state, claim, write, authority, or dependency condition requiring resolution or preservation.

Conflict must not silently become:

```text
PASS
```

---

# 40. Epoch

Reserve:

```text
E
EPOCH
CAUSAL_EPOCH
```

for explicitly typed epoch identity.

Conceptually:

```text
E1
→
E2
```

indicates an epoch transition.

It does not by itself indicate causality or finality.

---

# 41. Causal Epoch

```text
CAUSAL_EPOCH
```

represents the applicable causal/dependency epoch defined by AMOS Core semantics.

A conclusion valid in:

```text
E1
```

may require revalidation in:

```text
E2
```

when load-bearing conditions changed.

---

# 42. Finality

Reserve:

```text
FINAL
FINALIZED
FINALITY
```

for explicit finalization states only.

Canonical firewall:

```text
COMMITTED
!=
GLOBALLY FINAL
```

and:

```text
LOCAL FINALITY
!=
GLOBAL FINALITY
```

unless the applicable proof establishes equivalence.

---

# 43. Shard Symbols

Where shard notation is required:

```text
S0
S1
S2
...
Sn
```

may identify shards only when namespace context makes the meaning unambiguous.

Preferred explicit form:

```text
SHARD_0
SHARD_1
```

where collision with scope notation `S` is possible.

---

# 44. Atomicity

Reserve:

```text
ATOMIC
ATOMICITY
```

for a transaction or reasoning boundary whose all-or-none semantics are explicitly scoped.

Canonical law:

```text
ATOMIC(SCOPE_A)
!=
ATOMIC(SCOPE_B)
```

unless equivalence is established.

---

# 45. Multi-RSCF Atomicity

Conceptually:

```text
ATOMIC(
  RSCF_A,
  RSCF_B,
  RSCF_C
)
```

means those RSCFs participate in one declared atomic reasoning/finalization boundary.

This notation does not itself prove implementation-level atomicity.

---

# 46. Authority Symbols

Reserved authority concepts:

```text
AUTHORITY
AUTHORITY_SCOPE
AUTHORITY_ID
AUTHORITY_CLASS
PERMISSION
CAPABILITY
PROPOSAL
COMMIT
```

Canonical firewalls:

```text
CAPABILITY != AUTHORITY

PERMISSION != CAPABILITY

PROPOSAL != COMMIT

EXECUTION != AUTHORIZATION
```

---

# 47. Canon Symbols

Reserved:

```text
CANON
CANON_ID
CANON_VERSION
CANON_STATE
CANON_SOURCE
CANON_PROVENANCE
```

A file under `01_CANON` is not automatically final canon merely because of placement.

```text
CANON LOCATION
!=
CANON VALIDATION
```

---

# 48. Lifecycle States

Common lifecycle labels may include:

```text
PLACEHOLDER
DRAFT
CANDIDATE
ACTIVE
DEPRECATED
SUPERSEDED
ARCHIVED
RETIRED
```

Exact permitted transitions should be defined by the relevant lifecycle canon or registry.

---

# 49. PLACEHOLDER

```text
PLACEHOLDER
```

means the artifact location or structural role exists but substantive canonical content is incomplete.

Canonical law:

```text
PLACEHOLDER
!=
IMPLEMENTED
```

and:

```text
PLACEHOLDER
!=
VALIDATED
```

---

# 50. ACTIVE_CANON_CANDIDATE

```text
ACTIVE_CANON_CANDIDATE
```

denotes a developed candidate intended for canonical review/binding.

It does not equal:

```text
ACTIVE_CANON
```

---

# 51. Supersession

Reserved relationships:

```text
SUPERSEDES
SUPERSEDED_BY
REPLACES
DEPRECATED_BY
```

Supersession must preserve lineage.

Conceptually:

```text
ARTIFACT A
↓ superseded by
ARTIFACT B
```

does not permit erasing A's provenance.

---

# 52. Status and Conclusion Class

These fields are distinct.

```text
STATUS
!=
CONCLUSION_CLASS
```

Example:

```yaml
status: ACTIVE_CANON_CANDIDATE
conclusion_class: AMOS_MODEL
```

The first describes artifact lifecycle/governance state.

The second describes epistemic classification.

---

# 53. Registry Naming

Registry artifacts use:

```text
*_REGISTRY.md
```

Examples:

```text
SYMBOL_REGISTRY.md
INVARIANT_REGISTRY.md
AGENT_REGISTRY.md
SKILL_REGISTRY.md
MODEL_REGISTRY.md
```

Naming convention does not itself grant registry authority.

---

# 54. Prefix Registry

Current architectural prefixes include:

| Prefix | Meaning                |
| ------ | ---------------------- |
| `K_`   | Kernel artifact        |
| `CP_`  | Control-plane artifact |
| `RT_`  | Runtime artifact       |
| `A_`   | Agent artifact         |
| `S_`   | Skill artifact         |
| `WF_`  | Workflow artifact      |
| `P_`   | Protocol artifact      |
| `M_`   | Memory artifact        |

Prefix meaning is contextual to artifact naming and must not silently override mathematical notation.

---

# 55. Namespace Firewall

The same visible symbol may exist in separate namespaces.

Example:

```text
M_
```

as an artifact prefix may mean:

```text
MEMORY
```

while:

```text
M
```

inside H/M/L means:

```text
MID-LEVEL / SUBSYSTEM
```

Therefore:

```text
VISIBLE SIMILARITY
!=
SEMANTIC IDENTITY
```

---

# 56. Collision Handling

When two meanings compete for the same symbol:

```text
SYMBOL COLLISION
↓
IDENTIFY NAMESPACES
↓
PRESERVE EXISTING CANON
↓
QUALIFY AMBIGUOUS SYMBOL
↓
REGISTER ALIAS OR REPLACEMENT
```

Do not silently redefine the older symbol.

---

# 57. Qualified Symbols

Preferred qualification patterns include:

```text
RSCF.STATE
RSCF.PROVENANCE
CANON.VERSION
STATE.VERSION
MODEL.VERSION
AUTHORITY.SCOPE
```

or implementation-compatible equivalents.

Qualification should be introduced when it materially reduces ambiguity.

---

# 58. Alias Rules

Aliases may improve discoverability.

They must not create separate semantic identities accidentally.

```text
ALIAS
→
CANONICAL SYMBOL
```

not:

```text
ALIAS
→
NEW UNTRACKED DEFINITION
```

---

# 59. Deprecated Symbols

A deprecated symbol should preserve:

```yaml
deprecated_symbol:
  symbol:
  former_definition:
  deprecated_at:
  replacement:
  reason:
  provenance:
```

Deprecated symbols should remain resolvable for historical interpretation.

---

# 60. Symbol Evolution

Symbol evolution should follow:

```text
REGISTER
↓
USE
↓
REVIEW
↓
REFINE
↓
SUPERSEDE IF NECESSARY
↓
PRESERVE LINEAGE
```

Do not mutate historical semantics silently.

---

# 61. Semantic Immutability

Once a symbol has been used in canonical historical material, changing its meaning is a provenance event.

Canonical law:

```text
SAME SPELLING
+
NEW MEANING
!=
SAME SEMANTIC IDENTITY
```

A new semantic identity should be versioned, namespaced, or explicitly superseded.

---

# 62. Mathematical Symbols

Mathematical notation used in AMOS equations should be locally declared where ambiguity exists.

Examples:

```text
x
y
z
n
N
P
C
R
S
E
F
```

This registry must not assign universal AMOS meanings to conventional mathematical variables without canonical evidence.

---

# 63. Local Definitions

A document may introduce a local symbol:

```text
Let x = ...
```

provided:

```text
LOCAL SYMBOL
```

does not conflict with a canonical reserved symbol within the same semantic scope.

Local definitions should not automatically enter this global registry.

---

# 64. Symbol Promotion

A local symbol should be promoted into the Symbol Registry when it becomes:

```text
CROSS-DOCUMENT

LOAD-BEARING

CANONICAL

REPEATED

ARCHITECTURALLY SIGNIFICANT

REQUIRED FOR INTEROPERABILITY
```

---

# 65. Machine-Readable Registry Contract

A future machine-readable registry may use:

```yaml
symbols:
  - symbol_id: AMOS-SYM-RSCF
    notation: RSCF
    canonical_name: RSCF
    symbol_type: STRUCTURE
    namespace: AMOS_CORE
    definition_ref: UNKNOWN/GAP
    status: ACTIVE
    provenance_ref: UNKNOWN/GAP

  - symbol_id: AMOS-SYM-H
    notation: H
    canonical_name: High-Level Domain
    symbol_type: STRUCTURAL_LEVEL
    namespace: HML
    status: ACTIVE

  - symbol_id: AMOS-SYM-M
    notation: M
    canonical_name: Mid-Level Subsystem
    symbol_type: STRUCTURAL_LEVEL
    namespace: HML
    status: ACTIVE

  - symbol_id: AMOS-SYM-L
    notation: L
    canonical_name: Low-Level Detail
    symbol_type: STRUCTURAL_LEVEL
    namespace: HML
    status: ACTIVE
```

Exact schema remains subject to `16_SCHEMAS`.

---

# 66. Minimum Registry Invariants

```text
SYM-001  SYMBOL != SEMANTICS

SYM-002  SYMBOL != AUTHORITY

SYM-003  DEFINED != VERIFIED

SYM-004  DISPLAY NAME != SEMANTIC IDENTITY

SYM-005  VERSION TYPES MUST NOT BE SILENTLY COLLAPSED

SYM-006  ALIAS != NEW SEMANTIC IDENTITY

SYM-007  SYMBOL COLLISIONS MUST REMAIN VISIBLE

SYM-008  HISTORICAL SEMANTICS MUST PRESERVE PROVENANCE

SYM-009  UNKNOWN EXPANSION MUST NOT BE INVENTED

SYM-010  LOCAL SYMBOL != GLOBAL CANONICAL SYMBOL

SYM-011  SAME SPELLING != SAME MEANING ACROSS NAMESPACES

SYM-012  STRUCTURAL EDGE != CAUSAL EDGE

SYM-013  SOURCE_CLAIM != VERIFIED

SYM-014  MODEL != AUTHORITY

SYM-015  UNKNOWN/GAP != PASS

SYM-016  PLACEHOLDER != IMPLEMENTED

SYM-017  PROPOSAL != COMMIT

SYM-018  CAPABILITY != AUTHORITY

SYM-019  LOCAL FINALITY != GLOBAL FINALITY

SYM-020  SYMBOL EVOLUTION MUST PRESERVE LINEAGE
```

---

# 67. Validation Rules

Before registering a new canonical symbol, determine:

```text
1. DOES THE CONCEPT ALREADY HAVE A SYMBOL?

2. IS THE EXISTING SYMBOL SEMANTICALLY IDENTICAL?

3. DOES THE NEW SYMBOL COLLIDE WITH ANOTHER NAMESPACE?

4. IS THE DEFINITION AUTHORITATIVE OR ONLY A MODEL?

5. WHAT IS THE PROVENANCE?

6. WHAT SCOPE DOES THE SYMBOL APPLY TO?

7. WHAT VERSION INTRODUCED IT?

8. DOES IT SUPERSEDE AN EARLIER SYMBOL?

9. WILL EXISTING CANON CHANGE MEANING?

10. CAN THE SYMBOL BE MACHINE-RESOLVED?
```

If these cannot be resolved and are load-bearing:

```text
UNKNOWN/GAP
```

must remain visible.

---

# 68. Anti-Fabrication Rule

The registry must never create plausible acronym expansions merely to make the registry appear complete.

Example:

```text
KNOWN:
GMEF is a canonical AMOS symbol.

UNKNOWN:
Exact authoritative expansion.
```

Correct registry behavior:

```text
GMEF
→ REGISTER SYMBOL
→ BIND KNOWN REFERENCES
→ MARK EXPANSION UNKNOWN/GAP
```

Incorrect behavior:

```text
GMEF
→ INVENT PLAUSIBLE EXPANSION
```

---

# 69. Registry Resolution

Conceptual resolution:

```text
INPUT SYMBOL
↓
NAMESPACE
↓
SYMBOL RECORD
↓
VERSION
↓
SCOPE
↓
SEMANTIC DEFINITION
↓
PROVENANCE
```

If multiple valid records remain:

```text
COMPETING / AMBIGUOUS
```

must be returned rather than selecting arbitrarily.

---

# 70. Symbol Dependency

Some symbols depend on other registered semantics.

Example:

```text
CAUSAL_EPOCH
↓
EPOCH
↓
CAUSAL / DEPENDENCY SEMANTICS
```

A dependent symbol should not silently remain valid if its load-bearing definition is superseded incompatibly.

---

# 71. Symbol Provenance

Consequential symbols should eventually preserve:

```text
ORIGIN

INTRODUCED VERSION

SOURCE ARTIFACT

REVISION

SUPERSESSION HISTORY

SEMANTIC CHANGES

CURRENT STATUS
```

This allows historical AMOS artifacts to be interpreted according to the semantics active when they were produced.

---

# 72. RSCF Registry Node

```yaml
node_id: AMOS_SYMBOL_REGISTRY

functional_type:
  - SEMANTIC_REGISTRY
  - SYMBOL_REGISTRY
  - NOTATION_REGISTRY
  - IDENTITY_REGISTRY

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
  AMOS OS requires a provenance-aware symbol registry that
  distinguishes notation from semantic identity and preserves
  namespace, scope, version, lifecycle, and supersession
  boundaries for load-bearing architectural symbols.

critical_invariants:
  - SYMBOL != SEMANTICS
  - SYMBOL != AUTHORITY
  - DEFINED != VERIFIED
  - SAME SPELLING != SAME SEMANTIC IDENTITY
  - ALIAS != NEW SEMANTIC IDENTITY
  - UNKNOWN EXPANSION MUST NOT BE INVENTED
  - SYMBOL EVOLUTION MUST PRESERVE LINEAGE
  - STRUCTURAL EDGE != CAUSAL EDGE
  - UNKNOWN/GAP != PASS

dependencies:
  - AMOS_CORE_LAWS
  - INVARIANT_REGISTRY
  - LAW_HIERARCHY
  - HML_CANON
  - PERSISTENCE_CANON
  - AUTHORITY_CANON
  - CONTROL_PLANE_CANON
  - SCHEMA_REGISTRY
  - PROVENANCE

known_gaps:
  - Exact authoritative expansion of every historical AMOS acronym is not established here.
  - Full symbol inventory requires corpus-level extraction.
  - Historical introduction version for each symbol requires provenance reconstruction.
  - Machine-readable registry schema requires schema binding.
  - Collision analysis across the complete AMOS corpus remains incomplete.

does_not_establish:
  - implementation completeness
  - empirical validation
  - mathematical proof
  - authority merely through registration
  - complete historical symbol inventory
```

---

# 73. Promotion Gate

Promotion:

```text
ACTIVE_CANON_CANDIDATE
→
ACTIVE_CANON
```

requires at minimum:

```text
CORPUS SYMBOL EXTRACTION
↓
DUPLICATE DETECTION
↓
NAMESPACE ANALYSIS
↓
COLLISION ANALYSIS
↓
CANON SOURCE BINDING
↓
VERSION / LINEAGE RECONSTRUCTION
↓
SCHEMA VALIDATION
↓
REGISTRY REVIEW
```

No symbol should be assigned a fabricated history to satisfy this gate.

---

# 74. Canonical Summary

```text
AMOS SYMBOL
↓
NAMESPACE
↓
TYPE
↓
SEMANTIC IDENTITY
↓
DEFINITION
↓
SCOPE
↓
VERSION
↓
PROVENANCE
↓
LIFECYCLE
```

Core laws:

```text
SYMBOL != SEMANTICS

SYMBOL != AUTHORITY

DEFINED != VERIFIED

DISPLAY NAME != SEMANTIC IDENTITY

SAME SPELLING != SAME MEANING

ALIAS != NEW IDENTITY

SOURCE_CLAIM != VERIFIED

MODEL != AUTHORITY

UNKNOWN/GAP != PASS

PLACEHOLDER != IMPLEMENTED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

STRUCTURAL EDGE != CAUSAL EDGE

LOCAL FINALITY != GLOBAL FINALITY

SYMBOL EVOLUTION MUST PRESERVE LINEAGE
```

Canonical objective:

```text
NAME PRECISELY.

TYPE EXPLICITLY.

NAMESPACE AMBIGUITY.

PRESERVE SEMANTIC IDENTITY.

PRESERVE VERSION IDENTITY.

PRESERVE PROVENANCE.

PRESERVE SUPERSESSION.

DO NOT TURN NOTATION INTO AUTHORITY.

DO NOT TURN DEFINITION INTO VERIFICATION.

DO NOT TURN REPETITION INTO CANON.

DO NOT INVENT MISSING EXPANSIONS.

WHEN SEMANTICS ARE UNKNOWN,
REGISTER THE GAP RATHER THAN FABRICATE THE MEANING.
```

---

**Related:** [[00_ROOT/README.md|AMOS OS]] · [[00_ROOT/ARCHITECTURE.md|Architecture]] · [[00_ROOT/NAMING_STANDARD.md|Naming Standard]] · [[00_ROOT/PLACEMENT_RULES.md|Placement Rules]] · [[01_CANON/00_INDEX/CANON_MAP.md|Canon Map]] · [[01_CANON/AMOS_CORE_LAWS.md|AMOS Core Laws]] · [[01_CANON/INVARIANT_REGISTRY.md|Invariant Registry]] · [[01_CANON/LAW_HIERARCHY.md|Law Hierarchy]] · [[01_CANON/HML_CANON.md|HML Canon]] · [[01_CANON/PERSISTENCE_CANON.md|Persistence Canon]] · [[01_CANON/AUTHORITY_CANON.md|Authority Canon]] · [[01_CANON/CONTROL_PLANE_CANON.md|Control Plane Canon]] · [[01_CANON/INFRASTRUCTURE_CANON.md|Infrastructure Canon]] · [[02_KERNEL/00_INDEX/KERNEL_MAP.md|Kernel Map]] · [[03_CONTROL_PLANE/00_INDEX/CONTROL_PLANE_MAP.md|Control Plane Map]] · [[11_KNOWLEDGE/00_AMOS_Full_Brain_OS_Architecture.md|AMOS Full Brain OS Architecture]] · [[16_SCHEMAS/00_INDEX/SCHEMA_MAP.md|Schema Map]] · [[16_SCHEMAS/REGISTRIES/README.md|Registry Schemas]] · [[17_OBSERVABILITY/00_INDEX/OBSERVABILITY_MAP.md|Observability Map]] · [[23_OPERATING_MODEL/00_INDEX/OPERATING_MODEL.md|Operating Model]]

```text
```

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: symbol_registry
node_type: note
path: 01_CANON/05_VARIABLE_REGISTRY/SYMBOL_REGISTRY.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
