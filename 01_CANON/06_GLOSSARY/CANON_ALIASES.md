---
title: CANON ALIASES
type: canon
source: 01_CANON/06_GLOSSARY
artifact_id: AMOS-OS-ALIASES
canonical_name: ALIASES
artifact_type: canonical_registry
registry_type: identity_alias_registry
status: SOURCE_CLAIM
conclusion_class: AMOS_MODEL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
domain: canon
scope: AMOS_OS
authority_scope: identity-resolution
version: 1.0.0
created: 2026-08-25
updated: 2026-08-25
tags: [amos-os, canon, universe, canon-group/meta, canon/registry, canon/identity, canon/aliases, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/identity-resolution, topic/naming, topic/provenance]
aliases: "- AMOS Alias Registry
  - AMOS Identity Alias Registry
  - Canonical Alias Registry
  - Alias Resolu..."---
# AMOS OS Alias Registry
> **Origin architect / steward:** Trang Phan  
> **AMOS Core target:** v4.4  
> **Conclusion class:** `AMOS_MODEL`  
> **Authority:** canonical identity-resolution registry
## 1. Purpose
The **AMOS OS Alias Registry** defines how alternate names, historical names, abbreviations, display labels, legacy identifiers, renamed artifacts, and compatibility identifiers resolve to canonical AMOS identities.
Its purpose is to preserve **identity continuity without collapsing distinct concepts**.
An alias may provide another route to an existing identity.
It does **not** automatically create a new identity.
```text
ALIAS
→ RESOLUTION
→ CANONICAL IDENTITY
```
The governing distinction is:
```text
NAME != IDENTITY
ALIAS != CANON
PATH != IDENTITY
FILENAME != IDENTITY
DISPLAY LABEL != IDENTITY
VERSION LABEL != IDENTITY
SEMANTIC SIMILARITY != IDENTITY
```
This registry exists because AMOS artifacts can evolve, move, be renamed, acquire abbreviations, or retain historical references while their canonical identity and provenance must remain recoverable.
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# 2. Canonical Identity Law

Every governed AMOS artifact SHOULD have one canonical identity.

That identity may have zero or more aliases.

Formally:

```text
CanonicalIdentity C
Aliases A(C) = {a₁, a₂, ..., aₙ}
```

Resolution is:

```text
R(aᵢ) → C
```

where:

- `aᵢ` is an alias,
- `C` is the canonical identity,
- `R` is the governed alias-resolution function.

The reverse relation is not identity equivalence:

```text
R(alias) = canonical
```

does **not** imply:

```text
alias == canonical
```

The alias is a reference edge.

The canonical artifact remains the authoritative identity.

---

# 3. Identity Firewall

AMOS maintains a strict separation between identity dimensions.

```text
CANONICAL_ID
≠
ARTIFACT_ID
≠
FILENAME
≠
PATH
≠
DISPLAY_NAME
≠
ALIAS
≠
VERSION
≠
CONTENT_HASH
≠
RSCF_NODE_ID
```

These fields may point to the same conceptual artifact but perform different functions.

Example:

```yaml
canonical_id: AMOS-OS-CONTROL-PLANE
artifact_id: AMOS-OS-CONTROL-PLANE
filename: CONTROL_PLANE_CANON.md
path: 01_CANON/CONTROL_PLANE_CANON.md
display_name: AMOS Control Plane Canon
aliases:
  - Control Plane Canon
  - CP Canon
version: 1.0.0
```

Changing:

```text
CONTROL_PLANE_CANON.md
```

to:

```text
CONTROL_PLANE.md
```

does not by itself create a new canonical identity.

---

# 4. Why Aliases Exist

Aliases are permitted when they preserve useful identity continuity.

Primary cases include:

| Alias class           | Purpose                                       |
| --------------------- | --------------------------------------------- |
| `SHORT_NAME`          | concise human-readable reference              |
| `ABBREVIATION`        | compact technical identifier                  |
| `HISTORICAL_NAME`     | preserve earlier terminology                  |
| `LEGACY_NAME`         | resolve deprecated identifiers                |
| `RENAMED_ARTIFACT`    | maintain links after rename                   |
| `DISPLAY_NAME`        | presentation-friendly label                   |
| `COMPATIBILITY_ALIAS` | maintain software/API compatibility           |
| `DOMAIN_ALIAS`        | domain-specific reference to canonical object |
| `LANGUAGE_ALIAS`      | translated/localized naming                   |
| `PATH_ALIAS`          | resolve previous repository location          |
| `SYMBOL_ALIAS`        | alternate notation for registered symbol      |
| `MIGRATION_ALIAS`     | temporary mapping during structural migration |

Aliases MUST be typed when the distinction affects resolution or governance.

---

# 5. Canonical Alias Record

Each governed alias SHOULD eventually resolve through a record of the form:

```yaml
alias_id: ALIAS-000001

alias: "AMOS Full Brain"

alias_type: SHORT_NAME

canonical_id: AMOS-FULL-BRAIN-OS

canonical_path: 01_CANON/FULL_BRAIN_OS_CANON.md

status: ACTIVE

scope:
  ecosystem: AMOS_OS
  domain: cognition
  locale: global

validity:
  valid_from: 2026-08-25
  valid_until: null

provenance:
  origin_architect: Trang Phan
  source: canonical-registry
  introduced_by: null
  supersedes: null

resolution:
  deterministic: true
  priority: canonical
  ambiguity: false
```

Fields unavailable from canonical evidence remain:

```text
UNKNOWN/GAP
```

They MUST NOT be inferred merely to complete the record.

---

# 6. Alias Resolution Contract

Alias resolution follows:

```text
INPUT NAME
   ↓
NORMALIZE
   ↓
EXACT CANONICAL MATCH?
   ├── YES → RETURN CANONICAL
   └── NO
        ↓
EXACT ALIAS MATCH?
   ├── YES → RESOLVE ALIAS
   └── NO
        ↓
SCOPED ALIAS MATCH?
   ├── ONE VALID TARGET → RESOLVE
   ├── MULTIPLE TARGETS → AMBIGUOUS
   └── NONE → UNKNOWN/GAP
```

AMOS MUST NOT silently use semantic similarity to manufacture an alias relationship.

```text
similar_name
≠
alias relationship
```

A fuzzy match may generate a proposal:

```text
PROPOSED_ALIAS
```

but cannot become authoritative without the required governance path.

---

# 7. Resolution States

Alias resolution uses explicit states.

```text
CANONICAL
ACTIVE_ALIAS
DEPRECATED_ALIAS
HISTORICAL_ALIAS
MIGRATION_ALIAS
AMBIGUOUS
CONFLICT
UNKNOWN/GAP
INVALID
```

### `CANONICAL`

Input directly names the canonical identity.

### `ACTIVE_ALIAS`

A governed active alias resolves deterministically.

### `DEPRECATED_ALIAS`

Alias remains resolvable for compatibility but SHOULD NOT be used for new references.

### `HISTORICAL_ALIAS`

Alias exists for provenance/history rather than current naming.

### `MIGRATION_ALIAS`

Temporary compatibility mapping during repository or schema migration.

### `AMBIGUOUS`

The alias legitimately maps to multiple possible targets under the supplied scope.

### `CONFLICT`

Registry evidence contains incompatible mappings.

### `UNKNOWN/GAP`

No governed resolution exists.

### `INVALID`

The alias violates registry constraints or refers to a known invalid identity.

---

# 8. Deterministic Resolution Priority

When resolving an identifier, precedence is:

```text
1. exact canonical ID
2. exact canonical registered name
3. exact active alias within explicit scope
4. exact compatibility alias
5. historical/deprecated alias
6. migration alias
7. unresolved
```

Fuzzy semantic matching is outside canonical resolution.

It MAY be used for discovery but MUST be labeled as inference.

```text
DISCOVERY != RESOLUTION
```

---

# 9. Scope-Aware Aliases

Aliases are local and typed.

An alias does not necessarily have universal meaning.

An alias MAY be constrained by:

```text
ecosystem
domain
subsystem
repository
namespace
schema
protocol
runtime
language
time
version
environment
```

Therefore:

```text
alias + scope → canonical identity
```

is safer than:

```text
alias → universal identity
```

Example:

```yaml
alias: "CP"
scope: AMOS_OS
canonical_id: AMOS-CONTROL-PLANE
```

does not establish that `CP` means AMOS Control Plane outside that scope.

---

# 10. Ambiguity Firewall

If one alias maps to multiple canonical objects:

```text
A → C₁
A → C₂
```

the resolver MUST NOT arbitrarily select one.

Return:

```text
AMBIGUOUS
```

unless a valid scope discriminator resolves the collision.

Example:

```yaml
alias: "Kernel"

candidates:
  - AMOS-OS-KERNEL
  - AMOS-LEGAL-KERNEL
  - AMOS-SIMULATION-KERNEL

resolution_state: AMBIGUOUS
required_discriminator:
  - domain
  - canonical_id
```

This preserves competing interpretations instead of creating false certainty.

---

# 11. Alias Collision Rules

A collision occurs when:

```text
same alias
+
compatible scope
+
multiple canonical targets
```

Collision handling:

```text
DETECT
→ FREEZE AUTOMATIC RESOLUTION
→ IDENTIFY PROVENANCE
→ APPLY SCOPE
→ CHECK SUPERSESSION
→ RESOLVE OR PRESERVE AMBIGUITY
```

Never resolve a collision based solely on:

- popularity,
- file modification time,
- directory order,
- lexical similarity,
- number of inbound links,
- model confidence.

---

# 12. Rename Semantics

Renaming is not identity replacement.

```text
OLD_FILENAME
→ NEW_FILENAME
```

SHOULD preserve:

```text
canonical_id
artifact_id
provenance
lineage
supersession history
RSCF relations
```

The previous name MAY become:

```text
HISTORICAL_NAME
```

or:

```text
RENAMED_ARTIFACT
```

alias.

Correct:

```text
Old Name
    ↓ alias
Canonical Identity
    ↑
New canonical filename
```

Incorrect:

```text
rename
→ erase old identity
→ invent unrelated new artifact
```

---

# 13. Version Firewall

Alias resolution and version resolution are separate operations.

```text
ALIAS_RESOLUTION != VERSION_RESOLUTION
```

Example:

```text
AMOS Core
```

may resolve to the canonical AMOS Core identity.

It does not automatically mean:

```text
AMOS Core v4.4
```

unless the requesting context explicitly asks for the current target/version and the applicable version registry establishes that mapping.

The canonical filename policy remains:

```text
No version suffix required in canonical filenames.
```

Evolution is tracked through:

```text
version metadata
revision
hash
provenance
supersession
change record
migration record
```

not by silently embedding history into filenames.

---

# 14. Supersession

Alias and supersession are different relations.

```text
ALIAS_OF
```

means:

> alternate identifier for the same governed identity.

```text
SUPERSEDES
```

means:

> later artifact/version replaces an earlier governed artifact/version.

Therefore:

```text
ALIAS_OF != SUPERSEDES
```

Example:

```yaml
old_name: AMOS_SUPER_CORE
new_name: AMOS_CORE
relation: ALIAS_OF
```

may be appropriate after a naming cleanup if identity remained unchanged.

But:

```yaml
old_artifact: AMOS_CORE_LEGACY_MODEL
new_artifact: AMOS_CORE_REDESIGNED_MODEL
relation: SUPERSEDES
```

may represent actual architectural replacement.

These relations MUST NOT be conflated.

---

# 15. Provenance Requirements

Every authoritative alias SHOULD preserve enough provenance to answer:

```text
Who established this mapping?
What canonical identity does it resolve to?
When did the mapping become valid?
Why does the alias exist?
Was it renamed, migrated, translated, or deprecated?
What supersedes it?
What scope makes the mapping valid?
```

Minimum provenance:

```yaml
provenance:
  origin: SOURCE | MIGRATION | GOVERNANCE_DECISION | LEGACY_IMPORT
  source_artifact: ""
  introduced_at: ""
  introduced_by: ""
  evidence_ref: ""
```

Missing provenance is not silently repaired.

It remains:

```text
UNKNOWN/GAP
```

until evidence is bound.

---

# 16. Provenance Topology

Multiple alias records do not establish independent evidence if they descend from one source.

Example:

```text
SOURCE S
├── Alias Registry A
├── Migration Map B
└── Compatibility Table C
```

A, B, and C may all repeat the same mapping.

That remains one provenance ancestry:

```text
independent_confirmation_count = 1
```

AMOS therefore distinguishes:

```text
REPETITION != INDEPENDENT CONFIRMATION
```

This protects canonical identity resolution from provenance amplification.

---

# 17. RSCF Relation Types

Alias records may participate in RSCF topology using typed relations such as:

```text
ALIAS_OF
CANONICAL_NAME_OF
FORMERLY_NAMED
RENAMED_TO
SUPERSEDES
SUPERSEDED_BY
MIGRATED_TO
COMPATIBILITY_ALIAS_OF
TRANSLATION_OF
SYMBOL_ALIAS_OF
PATH_ALIAS_OF
DEPRECATED_ALIAS_OF
```

These relation types MUST retain distinct semantics.

Do not collapse them into a generic:

```text
RELATED_TO
```

when the actual relationship is known.

---

# 18. Canonical AMOS OS Root Aliases

The following mappings establish root-level naming conventions.

| Canonical plane         | Approved shorthand    |
| ----------------------- | --------------------- |
| `01_CANON`              | `CANON`               |
| `02_KERNEL`             | `KERNEL`              |
| `03_CONTROL_PLANE`      | `CONTROL_PLANE`, `CP` |
| `04_RUNTIME`            | `RUNTIME`, `RT`       |
| `05_COGNITIVE_ORGANISM` | `COGNITIVE_ORGANISM`  |
| `06_AGENTS`             | `AGENTS`              |
| `07_SKILLS`             | `SKILLS`              |
| `08_WORKFLOWS`          | `WORKFLOWS`           |
| `09_PROTOCOLS`          | `PROTOCOLS`           |
| `10_MEMORY`             | `MEMORY`              |
| `11_KNOWLEDGE`          | `KNOWLEDGE`           |
| `12_STATE`              | `STATE`               |
| `13_MODELS`             | `MODELS`              |
| `14_TOOLS`              | `TOOLS`               |
| `15_INTERFACES`         | `INTERFACES`          |
| `16_SCHEMAS`            | `SCHEMAS`             |
| `17_OBSERVABILITY`      | `OBSERVABILITY`       |
| `18_SECURITY`           | `SECURITY`            |
| `19_TESTS`              | `TESTS`               |
| `20_OPERATIONS`         | `OPERATIONS`          |
| `21_DOMAINS`            | `DOMAINS`             |
| `22_RESEARCH`           | `RESEARCH`            |
| `23_OPERATING_MODEL`    | `OPERATING_MODEL`     |
| `24_ARCHIVE`            | `ARCHIVE`             |
| `25_COGNITIVE_MATRIX`   | `COGNITIVE_MATRIX`    |

These are repository/navigation aliases.

They do not erase the distinction between a directory, conceptual plane, implementation, and canonical definition.

---

# 19. Prefix Registry

AMOS naming prefixes are aliases for artifact classes, not substitutes for full canonical identity.

| Prefix | Meaning       |
| ------ | ------------- |
| `K_`   | Kernel        |
| `CP_`  | Control Plane |
| `RT_`  | Runtime       |
| `A_`   | Agent         |
| `S_`   | Skill         |
| `WF_`  | Workflow      |
| `P_`   | Protocol      |
| `M_`   | Memory        |

Example:

```text
A_EvidenceAgent
```

communicates artifact class:

```text
Agent
```

It does not itself establish:

```text
authority
implementation status
canonicality
validation state
runtime permission
```

---

# 20. Canonical Concept Aliases

Within the current AMOS OS architecture, the following conceptual short forms may be used when scope is clear:

```yaml
AMOS:
  canonical: AMOS
  aliases:
    - AMOS OS
    - AMOS Universe

RSCF:
  canonical: Recursive Structured Cognitive Framework
  aliases:
    - RSCF

HML:
  canonical: H/M/L
  aliases:
    - HML
    - Hierarchical Fractal Decomposition

CP:
  canonical: CONTROL_PLANE
  aliases:
    - Control Plane

RT:
  canonical: RUNTIME
  aliases:
    - Runtime
```

Where a long-form expansion is not explicitly established by bound canon, retain the abbreviation rather than inventing an expansion.

---

# 21. Canon Identity Protection

Alias handling MUST preserve AMOS architectural firewalls.

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

An alias MUST NOT create equivalence across these boundaries.

For example:

```text
"Brain" → Cognitive Organism
```

cannot be assumed if the term could also refer to:

```text
Full Brain OS model
knowledge corpus
runtime cognition
cognitive matrix
```

Resolution must remain scoped or ambiguous.

---

# 22. Semantic Similarity Firewall

AMOS explicitly rejects:

```text
same dimensions
→ same semantics
```

and:

```text
same name
→ same object
```

and:

```text
similar structure
→ alias
```

This is especially important for structures such as the AMOS 19×19 family.

A shared 19×19 address space does not make:

```text
MURK
Semantic Matrix
Go Board
A-Matrix
```

aliases of one another.

Their relationship may be structural or model-level.

Their semantic identities remain distinct.

```text
ADDRESS-SPACE KINSHIP != IDENTITY
```

---

# 23. Cross-Language Aliases

Translated labels MAY point to one canonical identity when explicitly governed.

Example:

```yaml
canonical_id: AMOS-OS-KERNEL

aliases:
  - value: Kernel
    language: en
    type: DISPLAY_NAME

  - value: Nhân Hệ Thống
    language: vi
    type: LANGUAGE_ALIAS
```

Translation must preserve conceptual scope.

A translated term with materially different meaning must not be registered as an alias merely because it appears linguistically similar.

---

# 24. Runtime Contract

A runtime alias resolver SHOULD expose a deterministic interface such as:

```text
resolve_alias(
    identifier,
    namespace=None,
    domain=None,
    version=None,
    locale=None,
    timestamp=None
)
```

Result:

```yaml
input: ""
normalized_input: ""
resolution_state: ACTIVE_ALIAS
canonical_id: ""
canonical_name: ""
canonical_path: ""
alias_type: ""
scope: {}
confidence: 1.0
provenance: []
warnings: []
```

For deterministic registry matches:

```text
confidence = 1.0
```

only means the resolver is certain about the registry result.

It does **not** mean the underlying canonical claim has been empirically validated.

---

# 25. Unknown Handling

If no mapping exists:

```yaml
resolution_state: UNKNOWN/GAP
canonical_id: null
```

Do not:

```text
guess nearest artifact
invent canonical ID
infer alias from spelling
silently redirect
```

A suggested candidate MAY be returned separately:

```yaml
suggested_candidates:
  - canonical_id: ...
    relation: MODEL
```

but the canonical resolution remains:

```text
UNKNOWN/GAP
```

---

# 26. Alias Mutation Governance

Alias mutation is governed because aliases affect repository-wide identity resolution.

Mutation lifecycle:

```text
PROPOSAL
→ COLLISION CHECK
→ CANONICAL TARGET CHECK
→ PROVENANCE CHECK
→ SCOPE CHECK
→ DEPENDENCY CHECK
→ APPROVAL
→ COMMIT
→ INDEX UPDATE
→ LINK VALIDATION
```

The governing law is:

```text
PROPOSAL != COMMIT
```

No agent, skill, model, or tool gains authority to modify canonical aliases merely because it can generate a candidate mapping.

---

# 27. Safe Rename Procedure

Before a governed rename:

```text
1. identify canonical ID
2. identify current canonical path
3. collect inbound references
4. inspect existing aliases
5. detect collisions
6. classify rename vs supersession
7. create compatibility alias if needed
8. perform rename
9. update registry
10. validate links
11. preserve provenance
12. record change
```

Rollback MUST be possible while identity lineage remains recoverable.

---

# 28. Deletion Rule

Aliases SHOULD NOT simply disappear when they have historical or compatibility value.

Prefer:

```text
ACTIVE
→ DEPRECATED
→ HISTORICAL
```

where appropriate.

Permanent removal is appropriate only when the alias is:

```text
invalid
erroneous
security-sensitive
never committed
or explicitly removed through governance
```

Deletion must not erase provenance required to interpret historical references.

---

# 29. Integrity Invariants

The alias registry SHALL preserve these invariants:

### A1 — Canonical uniqueness

Within a governed namespace:

```text
canonical_id → one canonical identity
```

### A2 — Deterministic active resolution

```text
active alias + valid scope → ≤ 1 canonical target
```

### A3 — No silent ambiguity

```text
multiple valid targets → AMBIGUOUS
```

### A4 — No inferred canon

```text
missing mapping → UNKNOWN/GAP
```

### A5 — Provenance preservation

Alias changes retain recoverable lineage.

### A6 — Version separation

```text
alias identity != version identity
```

### A7 — Authority separation

```text
alias resolution != authority grant
```

### A8 — Semantic firewall

Structural similarity cannot create alias equivalence.

### A9 — Reversibility

Governed rename/migration operations SHOULD retain a rollback route.

### A10 — Local trust

Alias validity is bounded by its namespace, scope, provenance, and applicable temporal regime.

---

# 30. Validation Tests

A production alias registry SHOULD test at least:

```text
canonical ID resolves to itself
active alias resolves correctly
deprecated alias remains traceable
historical alias resolves with warning
unknown alias returns UNKNOWN/GAP
ambiguous alias never auto-selects
scope disambiguates valid collision
cross-domain collision remains separated
rename preserves canonical ID
path change preserves canonical identity
version does not leak into alias identity
supersession is not treated as aliasing
symbol aliases preserve symbol identity
language aliases preserve scope
provenance survives migration
alias chains do not form cycles
deleted canonical targets are detected
duplicate aliases are detected
case-normalization is deterministic
whitespace normalization is deterministic
fuzzy similarity does not become canon
authority is never inherited from alias resolution
```

---

# 31. Forbidden States

The following are invalid:

```text
alias → alias → alias → ... → canonical
```

when chains can be flattened safely.

Prefer:

```text
alias₁ ─┐
alias₂ ─┼→ canonical
alias₃ ─┘
```

Also forbidden:

```text
A → B
B → A
```

Alias cycles are integrity failures.

Likewise:

```text
same active alias
same scope
different canonical target
```

must produce conflict/ambiguity rather than silent resolution.

---

# 32. Alias Chain Compression

Historical imports may temporarily contain:

```text
A → B
B → C
C → canonical
```

Canonicalization SHOULD flatten this to:

```text
A → canonical
B → canonical
C → canonical
```

while preserving historical lineage separately.

This improves deterministic lookup without destroying provenance.

---

# 33. Relationship to Naming Standard

`NAMING_STANDARD.md` governs:

```text
how artifacts should be named
```

`ALIASES.md` governs:

```text
how alternate identifiers resolve
```

Therefore:

```text
NAMING_STANDARD
        ↓
canonical naming rules

ALIASES
        ↓
identity compatibility / resolution
```

Neither replaces the other.

---

# 34. Relationship to Symbol Registry

`SYMBOL_REGISTRY.md` governs canonical mathematical/logical symbols.

This registry governs alternate names.

When an alias refers specifically to notation:

```text
ALIASES
→ SYMBOL_ALIAS_OF
→ SYMBOL_REGISTRY
```

Symbol equivalence must be explicitly established.

Visual resemblance is insufficient.

---

# 35. Relationship to Universal Variable Registry

Variables require stable identity independently of their display notation.

```text
UNIVERSAL_VARIABLE_REGISTRY
→ variable identity

SYMBOL_REGISTRY
→ notation identity

ALIASES
→ alternate naming identity
```

Thus:

```text
same symbol != same variable
same variable may have scoped notation aliases
```

---

# 36. Relationship to Provenance

Every consequential alias mapping SHOULD be recoverable through provenance.

Conceptually:

```text
Alias
  ↓
Canonical Identity
  ↓
Source / Canon
  ↓
Provenance
  ↓
Revision / Supersession History
```

An alias registry without provenance is a convenience index.

It is not sufficient as an authoritative identity system.

---

# 37. Relationship to Runtime

Runtime systems MAY consume aliases.

They MUST NOT redefine canonical identity.

```text
CANON
  ↓
ALIAS REGISTRY
  ↓
CONTROLLED RESOLUTION
  ↓
RUNTIME CONSUMER
```

Therefore:

```text
runtime usage != canonical authority
```

A runtime-discovered name MAY become an alias proposal but requires governance before canonical registration.

---

# 38. Relationship to Memory and Knowledge

Memory may contain historical or informal names.

Knowledge may contain competing terminology.

Neither automatically modifies this registry.

```text
MEMORY
KNOWLEDGE
   ↓
candidate terminology
   ↓
alias proposal
   ↓
governance
   ↓
ALIASES
```

This protects canon from accidental semantic drift.

---

# 39. Security Considerations

Alias systems can become an attack surface when identifiers are intentionally made confusing.

Relevant risks include:

```text
name collision
namespace spoofing
look-alike identifiers
Unicode confusables
path substitution
deprecated-name hijacking
canonical-target replacement
alias-cycle injection
provenance stripping
unauthorized registry mutation
```

Security-sensitive implementations SHOULD normalize and validate identifiers before resolution.

Canonical identity must be checked after resolution and before authority decisions.

Most importantly:

```text
ALIAS RESOLUTION != AUTHORIZATION
```

---

# 40. Authority Boundary

This registry has authority over:

```text
identity alias resolution
```

It does not independently determine:

```text
runtime permissions
agent permissions
tool permissions
commit authority
security authorization
canonical truth
empirical validity
```

The hard boundary is:

```text
IDENTITY != AUTHORITY
```

Resolving:

```text
"CP" → CONTROL_PLANE
```

does not grant the caller Control Plane authority.

---

# 41. Failure Modes

Primary failure modes:

| Failure                     | Required behavior                  |
| --------------------------- | ---------------------------------- |
| Unknown alias               | `UNKNOWN/GAP`                      |
| Multiple targets            | `AMBIGUOUS`                        |
| Conflicting records         | `CONFLICT`                         |
| Missing canonical target    | fail closed                        |
| Alias cycle                 | reject                             |
| Stale migration mapping     | require revalidation               |
| Missing provenance          | downgrade trust                    |
| Scope mismatch              | do not resolve                     |
| Version ambiguity           | request/retain version gap         |
| Unauthorized mutation       | reject                             |
| Canonical target superseded | follow governed supersession rules |
| Corrupted registry          | restore last validated state       |

---

# 42. Recovery Semantics

When alias integrity fails:

```text
DETECT
→ ISOLATE FAILED RECORD
→ INVALIDATE DEPENDENT RESOLUTIONS
→ PRESERVE UNAFFECTED REGISTRY
→ RESTORE LAST VALID MAPPING
→ REPLAY VALID CHANGES
→ REVALIDATE DEPENDENCIES
```

Do not invalidate the entire alias registry because one mapping fails unless dependency closure demonstrates global contamination.

This follows the AMOS recovery principle:

```text
invalidate only failed premises,
edges,
and dependent conclusions
```

---

# 43. Promotion Gate

This artifact can be promoted only when its concrete alias entries are bound to canonical sources and reviewed.

Required gates:

```text
[ ] canonical identities indexed
[ ] alias types validated
[ ] collisions scanned
[ ] namespace rules established
[ ] provenance attached
[ ] rename history imported
[ ] deprecated aliases classified
[ ] supersession relations separated
[ ] symbol aliases checked
[ ] variable aliases checked
[ ] runtime resolver tested
[ ] cycle detection tested
[ ] unknown handling tested
[ ] authority firewall tested
[ ] recovery path tested
```

Until individual mappings have evidence, their status must remain appropriately typed.

---

# 44. Conclusion Classes

Alias-related statements use the weakest accurate class.

```text
VERIFIED
DERIVED
MODEL
CONDITIONAL
COMPETING
UNKNOWN/GAP
```

Examples:

```text
Registry explicitly maps A → B
→ VERIFIED within registry scope

Migration evidence implies old name A refers to B
→ DERIVED

Semantic similarity suggests A may refer to B
→ MODEL

A resolves to B only in subsystem X
→ CONDITIONAL

A validly refers to B or C
→ COMPETING / AMBIGUOUS

No evidence identifies A
→ UNKNOWN/GAP
```

---

# 45. Canonical Summary

The AMOS Alias Registry obeys one central rule:

```text
Aliases preserve access to identity.
They do not manufacture identity.
```

Expanded:

```text
NAME != IDENTITY
PATH != IDENTITY
VERSION != IDENTITY
SIMILARITY != IDENTITY
ALIAS != AUTHORITY
ALIAS != SUPERSESSION
ALIAS != CANON

ALIAS
→ typed resolution
→ scoped canonical identity
→ provenance
→ governed continuity
```

When deterministic resolution is impossible:

```text
PRESERVE AMBIGUITY
OR
RETURN UNKNOWN/GAP
```

Never invent the missing mapping.

---

## RSCF Node

```RSCF-NODE
node_id: AMOS-OS-ALIASES
node_type: canonical_registry
domain: AMOS_OS_IDENTITY
functional_type: Registry
lifecycle_stage: Canonicalization
claim_class: AMOS_MODEL

RSCF-RELATIONS:
  - INDEXED_BY: 00_ROOT_MOC|AMOS MOC
  - GOVERNED_BY: NAMING_STANDARD
  - RELATED_TO: CANON_MAP
  - RELATED_TO: SYMBOL_REGISTRY
  - RELATED_TO: UNIT_REGISTRY
  - RELATED_TO: UNIVERSAL_VARIABLE_REGISTRY
  - RELATED_TO: SYSTEM_MAP
  - RELATED_TO: ARCHITECTURE
  - RELATED_TO: NEURAL_NETWORK
  - CONSUMED_BY: CONTROL_PLANE_MAP
  - CONSUMED_BY: 04_RUNTIME
```

## Related

[[README]] ·
00_ROOT_MOC|AMOS MOC ·
[[ARCHITECTURE]] ·
[[SYSTEM_MAP]] ·
[[NEURAL_NETWORK]] ·
NAMING_STANDARD ·
[[CANON_MAP]] ·
[[AMOS_CORE_LAWS]] ·
[[INVARIANT_REGISTRY]] ·
[[LAW_HIERARCHY]] ·
[[SYMBOL_REGISTRY]] ·
[[UNIT_REGISTRY]] ·
[[UNIVERSAL_VARIABLE_REGISTRY]] ·
[[CONTROL_PLANE_MAP]] ·
11_KNOWLEDGE/00_AMOS_Full_Brain_OS_Architecture

```text
```

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
**MOC:** [[06_GLOSSARY_MOC]]
