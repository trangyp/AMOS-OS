---
title: DEPRECATED TERMS
type: deprecated
source: 01_CANON/06_GLOSSARY
artifact_id: AMOS-OS-DEPRECATED-TERMS
canonical_name: DEPRECATED_TERMS
artifact_type: canonical_semantic_lifecycle_registry
registry_type: deprecated_term_registry
status: SOURCE_CLAIM
conclusion_class: AMOS_MODEL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
domain: canon
scope: AMOS_OS
authority_scope: terminology-deprecation-and-semantic-migration
created: 2026-08-25
updated: 2026-08-25
tags:
- amos-os
- canon
- universe
- canon-group/meta
- canon/semantics
- canon/terminology
- canon/deprecation
- canon/supersession
- canon/registry
- rscf/claim
- rscf/provenance
- rscf/state/source-claim
- topic/deprecated-terms
- topic/semantic-integrity
- topic/semantic-migration
- topic/lineage
- topic/provenance
aliases:
- AMOS Deprecated Terms - Deprecated Terminology Registry - AMOS Terminology Migration Registry
---

# AMOS OS Deprecated Terms
> **Origin architect / steward:** Trang Phan
> **AMOS Core target:** v4.4
> **Conclusion class:** `AMOS_MODEL`
## 1. Purpose
`DEPRECATED_TERMS.md` is the canonical lifecycle registry for terminology that should no longer be used as the preferred semantic identity in current AMOS OS artifacts.
Deprecation preserves lineage rather than erasing history.
```text
OLD TERM
→ DEPRECATION RECORD
→ REPLACEMENT / SPLIT / RETIREMENT
→ MIGRATION
→ PROVENANCE PRESERVED
```
A deprecated term may remain visible in historical artifacts, aliases, citations, provenance records, migration tables, archived code, and supersession chains.
It must not silently regain canonical status through repetition.
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# 2. Hard Laws

```text
DEPRECATED != DELETED
DEPRECATED != FALSE
DEPRECATED != INVALID_HISTORY
DEPRECATED != CURRENT_CANON

RENAMED != SEMANTICALLY_CHANGED
SEMANTICALLY_CHANGED != SIMPLE_RENAME

ALIAS != REPLACEMENT
REPLACEMENT != SUPERSESSION
SUPERSESSION != DELETION

HISTORICAL_USAGE != CURRENT_AUTHORITY
NEWER_NAME != AUTOMATICALLY_BETTER
FILENAME_CHANGE != CANON_CHANGE

UNKNOWN_REPLACEMENT != INVENTED_REPLACEMENT
```

Deprecation is a governed semantic operation.

---

# 3. Authority Boundary

This registry may establish that a term is:

```text
CURRENT
DISCOURAGED
DEPRECATED
SUPERSEDED
RETIRED
HISTORICAL_ONLY
AMBIGUOUS
UNKNOWN/GAP
```

It does **not** independently establish:

```text
runtime implementation
empirical truth
execution permission
commit authority
artifact validity
model validity
historical authorship
```

Term lifecycle and claim validity are separate dimensions.

---

# 4. Why Deprecated Terms Are Preserved

AMOS preserves deprecated terminology because deletion can destroy:

- provenance
- historical searchability
- version lineage
- old RSCF references
- archived dependency resolution
- migration understanding
- supersession evidence
- semantic-change history

Therefore:

```text
DEPRECATE
→ PRESERVE
→ REDIRECT
→ EXPLAIN
```

rather than:

```text
DEPRECATE
→ ERASE
```

---

# 5. Canonical Deprecation Record

Each mature entry SHOULD use a structure equivalent to:

```yaml
term: ""
canonical_id: ""
status: DEPRECATED

deprecated_from: ""
deprecated_at: ""

replacement:
  term: ""
  canonical_id: ""

change_type: ""

reason: ""

semantic_relation:
  - ""

scope: ""

historical_scope: ""

migration:
  automatic: false
  instructions: ""

provenance:
  source_artifacts: []
  supersession_record: ""
  approved_by: ""

notes: ""

conclusion_class: ""
```

Unknown fields remain:

```text
UNKNOWN/GAP
```

They must not be inferred merely to complete the record.

---

# 6. Deprecation Change Types

Canonical change classes:

```text
RENAMED
CLARIFIED
NARROWED
EXTENDED
SPLIT
MERGED
SUPERSEDED
RETIRED
COLLISION_RESOLVED
LEGACY_ALIAS
HISTORICAL_ONLY
UNKNOWN_CHANGE
```

## RENAMED

Semantic identity remains materially stable while the preferred label changes.

```text
OLD_NAME
≈ semantic identity
→ NEW_NAME
```

## CLARIFIED

The term remains but its definition becomes more precise.

## NARROWED

The replacement applies to a smaller scope than the historical term.

## EXTENDED

The replacement explicitly covers a broader scope.

## SPLIT

One historical term maps to multiple distinct current concepts.

```text
OLD
├→ NEW_A
└→ NEW_B
```

Automatic one-to-one replacement is unsafe.

## MERGED

Multiple historical terms resolve into one canonical concept.

## SUPERSEDED

A newer governed concept replaces the older concept.

## RETIRED

The concept should no longer participate in current architecture.

## COLLISION_RESOLVED

A historically overloaded term is replaced by explicitly scoped terminology.

## LEGACY_ALIAS

The old term survives only as an alias for discovery or compatibility.

## HISTORICAL_ONLY

The term is retained solely for provenance/history.

---

# 7. Deprecation State Machine

```text
CURRENT
   │
   ├──→ DISCOURAGED
   │       │
   │       └──→ DEPRECATED
   │
   └──→ DEPRECATED
             │
             ├──→ LEGACY_ALIAS
             ├──→ SUPERSEDED
             ├──→ HISTORICAL_ONLY
             └──→ RETIRED
```

A transition must be explicit.

Repository age alone does not establish lifecycle state.

---

# 8. Current AMOS Core Version Vocabulary

Current AMOS architecture targets:

```text
AMOS_CORE v4.4
```

The v3.0 → v4.4 evolution spine preserves concepts including:

```text
deterministic logic
recursive RSCF / H-M-L
governed evolution
causal lineage
epistemic regimes
competing hypotheses
provenance topology
Sybil hardening
persistent provenance
MVCC / CAS concepts
atomic multi-RSCF reasoning
causal epoch finality
hardened shard-local finalization
proof-based coordination avoidance
```

Earlier vocabulary must not be discarded simply because later vocabulary is more precise.

Historical terms should instead be mapped through lineage when evidence supports the mapping.

---

# 9. Deprecated Marketing / Magnitude Qualifiers

Historical AMOS artifacts may contain magnitude or promotional qualifiers such as:

```text
SUPER
SUPERSTACK
SUPREME
ULTRA
OMEGA
INFINITY
vINFINITY
vInfinity
FULL
EXPANDED
CANON
```

These tokens are **not automatically semantic identities**.

For canonical AMOS OS naming, such qualifiers SHOULD NOT be assumed to encode:

```text
authority
version
validation level
implementation completeness
architectural layer
epistemic status
```

unless a governing artifact explicitly assigns that meaning.

Preferred rule:

```text
PROMOTIONAL / MAGNITUDE QUALIFIER
!=
CANONICAL TYPE
```

### Migration

Do not globally strip these terms from historical evidence.

For new canonical filenames and identifiers, prefer semantic names based on actual role:

```text
AMOS_CORE
CONTROL_PLANE
COGNITIVE_ORGANISM
RSCF
PROVENANCE_REGISTRY
MEMORY
AGENT
SKILL
WORKFLOW
```

rather than magnitude claims.

### Status

```text
Historical usage: PRESERVE
New canonical naming: DISCOURAGED
Automatic historical rewrite: PROHIBITED
```

---

# 10. `vInfinity` / `INFINITY` as Version Identity

Using terms such as:

```text
vInfinity
vINFINITY
INFINITY
```

as substitutes for explicit version metadata is deprecated for canonical version resolution.

Use explicit version metadata:

```yaml
version: 4.4
```

or:

```yaml
amos_core_target: v4.4
```

where applicable.

Hard rule:

```text
INFINITY LABEL
!=
VERSION IDENTITY
```

Historical names remain historical evidence and must not be rewritten without provenance-aware migration.

---

# 11. Filename-Encoded Version Authority

The practice of inferring canonical version solely from filenames such as:

```text
*_v0
*_v1
*_v2
```

is deprecated as an authority mechanism.

Version authority belongs in explicit metadata, provenance, revision history, hashes, supersession records, or governed registries.

```text
FILENAME VERSION
!=
PROVEN VERSION
```

A filename may contain a version for compatibility or historical purposes, but it cannot independently establish lineage.

---

# 12. Automatic `_v0` Assignment

Automatically assigning:

```text
_v0
```

to artifacts lacking explicit version metadata is deprecated for canonical AMOS OS identity management.

Reason:

```text
MISSING VERSION
→ UNKNOWN/GAP
```

not:

```text
MISSING VERSION
→ ASSUME v0
```

This protects provenance from fabricated historical ordering.

---

# 13. Filename as Canonical Identity

Using the physical filename as the sole canonical identity is deprecated.

Current identity firewall:

```text
FILENAME
!=
ARTIFACT ID
!=
REGISTRY NAME
!=
SEMANTIC IDENTITY
!=
VERSION IDENTITY
```

Renaming a file must therefore not silently mutate semantic identity.

---

# 14. Path as Authority

Treating repository location alone as proof of authority is deprecated.

For example:

```text
artifact located in 01_CANON
```

does not by itself imply:

```text
artifact is validated current canon
```

Canonical placement is necessary for organization but insufficient for promotion.

Authority also depends on applicable governance and provenance.

---

# 15. `FULL` as Completeness Assertion

The term:

```text
FULL
```

must not be interpreted automatically as evidence that an artifact is exhaustive or implementation-complete.

Historical filenames containing `FULL` may remain unchanged for provenance.

For current semantics:

```text
FULL
!=
COMPLETE
!=
VALIDATED
!=
EXHAUSTIVE
```

Completeness requires explicit scope and evidence.

---

# 16. `CANON` as Validation Assertion

Historical use of `CANON` inside a filename or title does not independently establish current canonical authority.

```text
"CANON" IN NAME
!=
CANONICAL GOVERNANCE STATE
```

Current canonical status should be resolved through:

```text
artifact metadata
→ canon registry
→ provenance
→ supersession state
→ applicable governance
```

---

# 17. `Agent` as Universal Component Name

Using `Agent` for every active component is semantically deprecated.

AMOS OS distinguishes:

```text
ORGAN
AGENT
SKILL
WORKFLOW
PROTOCOL
TOOL
MODEL
RUNTIME SERVICE
CONTROL-PLANE COMPONENT
KERNEL OPERATOR
```

Therefore:

```text
EXECUTABLE COMPONENT
!=
AGENT
```

Only role-based workers satisfying the applicable agent contract should use `Agent` as their canonical type.

---

# 18. `Skill` and `Workflow` Interchangeability

Using:

```text
SKILL
```

and:

```text
WORKFLOW
```

as interchangeable terms is deprecated.

Canonical distinction:

```text
SKILL
= reusable procedure

WORKFLOW
= multi-step orchestration graph
```

Thus:

```text
SKILL != WORKFLOW
```

---

# 19. `Protocol` as Workflow

Historical usage that labels orchestration logic as a protocol should be migrated where the distinction is known.

Canonical rule:

```text
PROTOCOL
= interaction contract

WORKFLOW
= orchestration structure
```

Therefore:

```text
WORKFLOW != PROTOCOL
```

---

# 20. `Memory` as Canon

Treating stored memory as canonical truth is deprecated.

```text
MEMORY != CANON
```

Memory may contain:

```text
historical observations
preferences
summaries
derived claims
cached state
prior decisions
```

Each retains its own epistemic status.

---

# 21. `Knowledge` as Verified Fact

Using the term `knowledge` to imply automatic verification is deprecated.

Canonical distinction:

```text
KNOWLEDGE
= structured information available for reasoning

VERIFIED
= conclusion class supported to required standard
```

Therefore:

```text
KNOWLEDGE ENTRY != VERIFIED FACT
```

---

# 22. `Model` as Authority

Using a model's output as self-authorizing policy or truth is deprecated.

```text
MODEL != AUTHORITY
```

A model may:

```text
estimate
predict
simulate
classify
recommend
generate hypotheses
```

but authority must originate from the appropriate governance boundary.

---

# 23. `Tool` as Permission

Language implying that possession of a tool establishes authorization is deprecated.

```text
TOOL != PERMISSION
```

The canonical sequence is:

```text
CAPABILITY
+
IDENTITY
+
POLICY
+
AUTHORITY
+
CONTEXT
→ PERMITTED ACTION
```

as applicable.

---

# 24. Capability as Authority

Any terminology or implementation assumption equating capability with authority is deprecated.

Hard boundary:

```text
CAPABILITY != AUTHORITY
```

An agent capable of mutation does not thereby possess commit authority.

---

# 25. Proposal as Commit

Terminology treating proposed state as committed state is deprecated.

```text
PROPOSAL != COMMIT
```

Preferred distinction:

```text
PROPOSE
→ VALIDATE
→ AUTHORIZE
→ COMMIT
```

subject to the governing workflow.

---

# 26. `Unknown` as Failure

Treating:

```text
UNKNOWN/GAP
```

as synonymous with failure, falsehood, or zero is deprecated.

Canonical interpretation:

```text
UNKNOWN/GAP
= insufficient established information
```

Hard boundary:

```text
UNKNOWN/GAP != PASS
UNKNOWN/GAP != FALSE
UNKNOWN/GAP != ZERO
```

---

# 27. `No Contradiction` as Proof

Language implying:

```text
no contradiction found
→ verified
```

is deprecated.

Absence of detected contradiction may increase support in a defined validation process, but:

```text
ABSENCE_OF_CONTRADICTION != PROOF
```

---

# 28. Multiple Sources Without Provenance Independence

Calling several descendant artifacts:

```text
independent sources
```

without checking ancestry is deprecated.

Example:

```text
SOURCE A
├→ REPORT B
├→ ARTICLE C
└→ SUMMARY D
```

does not establish three independent confirmations.

Preferred terms:

```text
multiple reports
shared provenance
correlated evidence
independence UNKNOWN/GAP
```

until independence is demonstrated.

---

# 29. Structural Similarity as Equivalence

Language asserting identity because two systems share:

```text
dimensions
topology
equations
hierarchy
graph structure
```

is deprecated unless equivalence is independently established.

```text
STRUCTURAL_SIMILARITY
!=
SEMANTIC_IDENTITY
```

---

# 30. Structural Similarity as Causation

Any terminology promoting structural resemblance directly into causal claims is deprecated.

```text
STRUCTURAL_SIMILARITY
!=
CAUSATION
```

Such relationships should normally remain:

```text
MODEL
HYPOTHESIS
ANALOGY
STRUCTURAL_MAPPING
```

until causally validated.

---

# 31. Correlation as Causation

Terminology collapsing correlation into causal effect is deprecated.

```text
CORRELATION != CAUSATION
```

Use the appropriate typed relation:

```text
ASSOCIATED_WITH
CORRELATED_WITH
ENABLES
MEDIATES
CONFOUNDS
CAUSES
```

only when the evidence licenses that type.

---

# 32. Global Trust

The notion of a source, model, agent, or artifact being simply:

```text
TRUSTED
```

without scope is discouraged.

Preferred vocabulary:

```text
trusted_for: <claim/type>
scope: <domain>
regime: <environment>
fresh_until: <condition/time>
provenance: <source>
```

Canonical principle:

```text
TRUST IS LOCAL
```

---

# 33. Universal Confidence

Single confidence values that obscure distinct uncertainty dimensions are discouraged for consequential reasoning.

Prefer explicit uncertainty where material:

```text
evidence uncertainty
model uncertainty
scope uncertainty
temporal uncertainty
causal uncertainty
execution uncertainty
provenance-independence uncertainty
```

A scalar confidence score may still be used where its semantics are explicitly defined.

---

# 34. Global Recompute as Default Recovery

Treating every invalidated premise as requiring total recomputation is deprecated as the default recovery model.

Preferred principle:

```text
FAILURE
→ LOCAL INVALIDATION
→ DEPENDENT DESCENDANTS
→ PRESERVE UNAFFECTED WORK
→ REROUTE
```

Global recomputation remains available when dependency closure cannot safely isolate the failure.

---

# 35. Global Coordination as Default Correctness Mechanism

Treating global coordination as mandatory for every operation is not the current AMOS v4.4 preferred model.

Where independence can be demonstrated:

```text
PROOF OF SAFE LOCALITY
→ COORDINATION MAY BE AVOIDED
```

However, the opposite shortcut is also prohibited:

```text
COORDINATION IS EXPENSIVE
→ SKIP IT
```

The v4.4 concept is:

```text
PROOF-BASED COORDINATION AVOIDANCE
```

not unconditional coordination avoidance.

---

# 36. Local Finality as Global Finality

Terminology collapsing shard-local or bounded finality into system-wide finality is deprecated.

```text
SHARD-LOCAL FINALITY
!=
GLOBAL FINALITY
```

Finality must declare scope.

---

# 37. Conversational Runtime as Literal Distributed Implementation

Language claiming that a conversational AMOS adaptation literally implements all source-code distributed mechanisms is deprecated unless implementation evidence establishes it.

Concepts such as:

```text
MVCC
CAS
atomic multi-RSCF reasoning
causal epochs
shard-local finalization
proof-based coordination avoidance
```

may function as reasoning and architecture models.

Their conceptual use does not prove literal infrastructure implementation.

---

# 38. Canonical Naming Migration

For new AMOS OS artifacts, prefer semantic names tied to architectural role.

Examples:

```text
K_*     kernel contracts
CP_*    control-plane components
RT_*    runtime components
A_*     agents
S_*     skills
WF_*    workflows
P_*     protocols
M_*     memory components
*_MAP   topology/index maps
*_REGISTRY
*_LEDGER
```

Avoid adding adjectives merely to imply superiority or completeness.

Example:

```text
AMOS_SUPER_OMEGA_FULL_AGENT
```

should not be generated when the semantic identity is simply:

```text
A_ENVIRONMENT_SCAN
```

unless the historical name itself must be preserved.

---

# 39. Historical Artifact Firewall

Historical artifacts are evidence of historical state.

Do not perform uncontrolled global replacements.

```text
CURRENT TERMINOLOGY CHANGE
≠
REWRITE ALL HISTORY
```

Historical artifacts SHOULD retain original language where needed for:

```text
provenance
citation
hash integrity
revision reconstruction
archival fidelity
historical interpretation
```

Use mappings instead.

---

# 40. Migration Mapping

Preferred migration representation:

| Historical term         | Current term     | Relation        | Migration                          |
| ----------------------- | ---------------- | --------------- | ---------------------------------- |
| old label               | new label        | `RENAMED`       | safe substitution if scope matches |
| overloaded label        | A / B            | `SPLIT`         | inspect context                    |
| legacy alias            | canonical term   | `ALIAS_OF`      | resolve                            |
| old architecture        | new architecture | `SUPERSEDED_BY` | preserve lineage                   |
| obsolete concept        | —                | `RETIRED`       | no current replacement             |
| unclear historical term | `UNKNOWN/GAP`    | unresolved      | investigate                        |

No replacement should be invented to make the table complete.

---

# 41. Safe Automatic Migration

Automatic migration is allowed only when:

```text
identity equivalence established
AND
scope compatible
AND
no semantic split
AND
no provenance damage
AND
no version ambiguity
AND
no conflicting canon
```

Otherwise:

```text
MANUAL REVIEW
```

or:

```text
UNKNOWN/GAP
```

---

# 42. Unsafe Automatic Migration

Automatic replacement MUST NOT occur when:

```text
one old term maps to multiple new terms
replacement changes scope
replacement changes authority
replacement changes causal meaning
replacement changes epistemic class
historical quotation must remain exact
artifact hash/provenance must remain stable
term identity is uncertain
```

---

# 43. Deprecation and Aliases

Deprecated terms may be retained in `ALIASES.md`.

Example:

```yaml
alias: LegacyTerm
canonical_target: CurrentTerm
status: DEPRECATED_ALIAS
```

But:

```text
DEPRECATED_ALIAS
!=
CURRENT PREFERRED TERM
```

The alias registry resolves identity.

This registry governs lifecycle status.

---

# 44. Deprecation and the Canonical Glossary

`CANONICAL_GLOSSARY.md` defines current canonical meanings.

`DEPRECATED_TERMS.md` defines historical and deprecated semantic identities.

Relationship:

```text
CANONICAL_GLOSSARY
       ↑
       │ replacement / current meaning
       │
DEPRECATED_TERMS
       ↓
       │ historical identity
       │
ALIASES / ARCHIVE / PROVENANCE
```

---

# 45. Deprecation and Supersession

Deprecation and supersession are related but distinct.

```text
DEPRECATION
= term should no longer be preferred

SUPERSESSION
= another governed artifact/concept replaces it
```

Therefore:

```text
DEPRECATED
```

does not automatically imply a replacement exists.

Possible state:

```text
term: X
status: DEPRECATED
replacement: UNKNOWN/GAP
```

This is valid.

---

# 46. Deprecation and Deletion

Deletion should not be used merely to clean terminology.

Deletion may destroy provenance.

Preferred sequence:

```text
IDENTIFY
→ CLASSIFY
→ DEPRECATE
→ MAP
→ MIGRATE CURRENT DEPENDENCIES
→ ARCHIVE WHERE APPROPRIATE
→ RETAIN LINEAGE
```

Physical deletion is a separate lifecycle decision.

---

# 47. Semantic Collision Resolution

When one historical term refers to multiple concepts:

```text
TERM X
├→ CONCEPT A
└→ CONCEPT B
```

do not select one replacement globally.

Mark:

```text
change_type: SPLIT
automatic_migration: false
```

Then discriminate using:

```text
artifact context
version
domain
dependencies
definition
provenance
```

---

# 48. Deprecation Review Triggers

Review a term when:

- its meaning changes across versions
- it collides with another canonical identity
- it encodes misleading authority
- it implies unsupported completeness
- it obscures architectural boundaries
- it conflates epistemic classes
- it causes causal overreach
- it breaks provenance
- it becomes redundant after a governed merge
- its domain-specific meaning leaks into root canon
- a newer term more precisely preserves the intended semantics

---

# 49. Non-Reasons for Deprecation

A term should **not** be deprecated solely because:

```text
it is old
it is uncommon
a newer synonym sounds better
an agent prefers another term
a file was renamed
a directory was reorganized
a model generated an alternative
```

Semantic governance requires a material reason.

---

# 50. Required Deprecation Evidence

Consequential deprecation SHOULD identify:

```text
current definition
historical definition
difference
scope
affected artifacts
replacement if any
migration risk
provenance
authority for change
```

If this evidence is incomplete:

```text
DEPRECATION PROPOSAL
```

should remain distinct from:

```text
COMMITTED DEPRECATION
```

---

# 51. Dependency Handling

When term `T` is deprecated:

```text
T
├→ artifact A
├→ schema B
├→ agent C
├→ workflow D
└→ knowledge E
```

only dependencies whose semantics are materially affected should be migrated.

Do not globally invalidate unrelated descendants.

---

# 52. Deprecation Proof Capsule

A consequential deprecation can be represented conceptually as:

```yaml
claim:
  term: ""
  state: DEPRECATED

load_bearing_premises:
  - ""

evidence:
  - ""

provenance:
  - ""

scope: ""

replacement: ""

competing_explanations:
  - ""

falsifiers:
  - ""

migration_dependencies:
  - ""

confidence_ceiling: ""
```

If a load-bearing premise fails, dependent migration decisions should be invalidated locally.

---

# 53. Reversal

Deprecation may be reversed if new canonical evidence establishes that the decision was incorrect.

Reversal must preserve the prior lifecycle record.

```text
CURRENT
→ DEPRECATED
→ REINSTATED
```

does not erase the intermediate state.

This protects causal and governance lineage.

---

# 54. Registry Integrity Invariants

### DT-1 — No invented replacement

```text
UNKNOWN REPLACEMENT
→ UNKNOWN/GAP
```

### DT-2 — Historical language remains recoverable

Deprecation must not destroy provenance.

### DT-3 — Current canon wins within current scope

Historical popularity cannot override governed current semantics.

### DT-4 — Scope must be preserved

A local deprecation cannot silently become universal.

### DT-5 — Semantic splits require contextual migration

```text
1 OLD → N NEW
```

prohibits blind replacement.

### DT-6 — Authority changes require explicit review

A rename cannot silently increase or decrease authority.

### DT-7 — Epistemic class must survive migration

```text
SOURCE_CLAIM
```

cannot become:

```text
VERIFIED
```

because terminology changed.

### DT-8 — Causal type must survive migration

```text
CORRELATED_WITH
```

cannot become:

```text
CAUSES
```

through lexical substitution.

### DT-9 — Identity remains separate from filename

Renaming files does not automatically migrate semantic identity.

### DT-10 — Contradictions remain visible

Conflicting migration records must remain `COMPETING` until resolved.

---

# 55. Initial Canonical Deprecation Rules

The following are current semantic deprecation rules for AMOS OS:

| Deprecated interpretation                    | Preferred interpretation                                          |
| -------------------------------------------- | ----------------------------------------------------------------- |
| filename = identity                          | explicit artifact/semantic identity                               |
| filename suffix = proven version             | explicit version/provenance metadata                              |
| missing version = v0                         | `UNKNOWN/GAP`                                                     |
| `FULL` = exhaustive                          | explicit completeness evidence                                    |
| `CANON` in filename = authority              | governed canon state                                              |
| `OMEGA/ULTRA/SUPREME` = higher authority     | no authority inference                                            |
| every active component = agent               | typed component classification                                    |
| skill = workflow                             | separate procedure/orchestration types                            |
| workflow = protocol                          | separate orchestration/interface types                            |
| memory = canon                               | separate persistence/authority layers                             |
| knowledge = verified truth                   | typed epistemic state                                             |
| model = authority                            | model remains advisory/representational unless governed otherwise |
| tool = permission                            | explicit authorization required                                   |
| capability = authority                       | explicit authority required                                       |
| proposal = commit                            | governed commit required                                          |
| unknown = pass                               | preserve `UNKNOWN/GAP`                                            |
| no contradiction = proof                     | additional validation required                                    |
| repeated source = independent evidence       | provenance independence required                                  |
| structural similarity = identity             | semantic validation required                                      |
| structural similarity = causation            | causal evidence required                                          |
| correlation = causation                      | causal evidence required                                          |
| local finality = global finality             | explicit finality scope                                           |
| conceptual MVCC/CAS = literal implementation | implementation evidence required                                  |

---

# 56. Terms Not Yet Proven Deprecated

This registry must not fabricate a comprehensive deprecated-term inventory.

Additional historical AMOS terminology may exist across:

```text
legacy repositories
archived files
AMOS Core versions
Full Brain OS artifacts
Cognition artifacts
Universe frameworks
research notes
generated architecture
historical agent definitions
```

Until corpus-level lineage review establishes their status:

```text
status: UNKNOWN/GAP
```

rather than:

```text
status: DEPRECATED
```

This distinction is mandatory.

---

# 57. Validation Work Required

Before this registry can be promoted beyond its current source-claim/model status:

```text
[ ] scan canonical AMOS Core lineage
[ ] bind v3.0 → v4.4 terminology changes
[ ] scan historical root artifacts
[ ] scan canonical glossary collisions
[ ] scan alias registry
[ ] scan symbol registry
[ ] scan universal variable registry
[ ] scan archived terminology
[ ] identify semantic splits
[ ] identify true renames
[ ] identify retired concepts
[ ] identify historical-only labels
[ ] establish supersession edges
[ ] establish migration dependencies
[ ] preserve unresolved contradictions
[ ] mark uncertain mappings UNKNOWN/GAP
```

---

# 58. Migration Algorithm

```text
INPUT: historical term T

1. Resolve exact historical identity.
2. Determine artifact/version/domain context.
3. Search current canonical glossary.
4. Search alias registry.
5. Search supersession lineage.
6. Compare definitions.
7. Compare scope.
8. Compare authority semantics.
9. Compare epistemic semantics.
10. Compare causal semantics.

IF exact semantic continuity:
    classify RENAMED / LEGACY_ALIAS

ELSE IF one historical concept became multiple:
    classify SPLIT
    require contextual migration

ELSE IF multiple concepts became one:
    classify MERGED

ELSE IF current concept explicitly replaces old:
    classify SUPERSEDED

ELSE IF concept no longer applies:
    classify RETIRED

ELSE:
    UNKNOWN/GAP
```

---

# 59. Current-Artifact Rule

New AMOS OS artifacts SHOULD:

```text
use current canonical terminology
retain explicit semantic identity
retain explicit version metadata where applicable
retain provenance
link deprecated aliases when useful
avoid unsupported magnitude qualifiers
```

Historical artifacts SHOULD:

```text
preserve historically accurate terminology
```

unless a governed migration specifically requires modification.

---

# 60. Canonical Summary

AMOS terminology evolves without destroying its history.

The lifecycle is:

```text
TERM
→ DEFINITION
→ USE
→ EVOLUTION
→ DEPRECATION
→ MIGRATION
→ PROVENANCE PRESERVATION
```

The core law is:

```text
SEMANTIC EVOLUTION
WITHOUT
HISTORICAL ERASURE
```

Therefore:

```text
DEPRECATED != DELETED
OLD != WRONG
NEW != VERIFIED
RENAMED != REDEFINED
ALIAS != IDENTITY
FILENAME != CANON
HISTORICAL_USAGE != CURRENT_AUTHORITY
UNKNOWN_REPLACEMENT != INVENTED_REPLACEMENT
```

When the lineage cannot yet be established:

```text
UNKNOWN/GAP
```

is the correct canonical state.

---

## RSCF Node

```RSCF-NODE
node_id: AMOS-OS-DEPRECATED-TERMS
node_type: canonical_semantic_lifecycle_registry
domain: AMOS_OS_CANON
functional_type: Registry
lifecycle_stage: SemanticGovernance
claim_class: AMOS_MODEL

RSCF-RELATIONS:
  - INDEXED_BY: 00_ROOT_MOC|AMOS MOC
  - INDEXED_BY: CANON_MAP
  - GOVERNED_BY: AMOS_CORE_LAWS
  - GOVERNED_BY: LAW_HIERARCHY
  - CONSTRAINED_BY: INVARIANT_REGISTRY
  - DEFINITIONS_FROM: CANONICAL_GLOSSARY
  - RESOLVES_WITH: ALIASES
  - RESOLVES_WITH: SYMBOL_REGISTRY
  - RESOLVES_WITH: UNIVERSAL_VARIABLE_REGISTRY
  - PRESERVES: README
  - RELATED_TO: NAMING_STANDARD
  - RELATED_TO: ARCHITECTURE
  - RELATED_TO: SYSTEM_MAP
  - RELATED_TO: AUTHORITY_CANON
  - RELATED_TO: CONTROL_PLANE_CANON
  - RELATED_TO: HML_CANON
  - RELATED_TO: COGNITION_CANON
  - RELATED_TO: COGNITIVE_ORGANISM_CANON
  - RELATED_TO: FULL_BRAIN_OS_CANON
```

## Related

[[README]] ·
[[00_ROOT_MOC]]|[[AMOS MOC]] ·
[[ARCHITECTURE]] ·
[[SYSTEM_MAP]] ·
NAMING_STANDARD ·
[[NEURAL_NETWORK]] ·
[[CANON_MAP]] ·
[[AMOS_CORE_LAWS]] ·
[[INVARIANT_REGISTRY]] ·
[[LAW_HIERARCHY]] ·
[[CANONICAL_GLOSSARY]] ·
ALIASES ·
[[SYMBOL_REGISTRY]] ·
[[UNIT_REGISTRY]] ·
[[UNIVERSAL_VARIABLE_REGISTRY]] ·
[[HML_CANON]] ·
[[COGNITION_CANON]] ·
[[COGNITIVE_ORGANISM_CANON]] ·
[[FULL_BRAIN_OS_CANON]] ·
[[AUTHORITY_CANON]] ·
[[CONTROL_PLANE_CANON]] ·
[[README]]

```text
```

---

[[00_ROOT_MOC]]|[[AMOS MOC]]

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
**MOC:** [[06_GLOSSARY_MOC]]
