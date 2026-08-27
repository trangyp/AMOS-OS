---
aliases:
- NAMING_STANDARD

artifact_id: AMOS-OS-NAMING-STANDARD
name: AMOS_OS_NAMING_STANDARD
title: "AMOS OS Naming Standard — Canonical Identity, Namespace, Versioning, and Rename Governance"

document_version: "2.0.0"
naming_standard_version: "1.0.0"
namespace_contract_version: "1.0.0"
amos_core_target: "v4.4"

status: ACTIVE_STANDARD
conclusion_class: "AMOS_MODEL"
rscf_state: "derived"

canon_group: "tech-ai"
canon_type: "standard"

origin_architect: "Trang Phan"
steward: "Trang Phan"

created: "2026-08-25"
updated: "2026-08-25"

scope:
  - AMOS_OS
  - repository_namespaces
  - artifact_identity
  - filenames
  - folder_names
  - registry_names
  - schema_names
  - agent_names
  - skill_names
  - workflow_names
  - protocol_names
  - mode_names
  - model_names
  - version_identity
  - rename_governance

tags:
  - amos
  - amos-os
  - naming
  - naming-standard
  - namespace
  - identity
  - artifact-identity
  - versioning
  - semantic-versioning
  - repository
  - filesystem
  - registry
  - canon
  - kernel
  - agents
  - skills
  - workflows
  - protocols
  - modes
  - memory
  - knowledge
  - state
  - models
  - tools
  - schemas
  - provenance
  - rscf
  - migration
  - rename
  - compatibility
  - lineage
  - governance
  - canon-group/tech-ai
  - canon/standard
  - rscf/claim
  - rscf/provenance
  - rscf/state/derived
  - topic/amos-os
  - topic/naming-standard
  - topic/namespace-governance
  - topic/version-governance

aliases:
  - AMOS Naming Standard
  - AMOS OS Naming Standard
  - AMOS Namespace Standard
  - AMOS Identity Standard
  - AMOS Repository Naming Standard

related:
  - "[[00_ROOT/00-Home]]"
  - "MOC"
  - "[[00_ROOT/ARCHITECTURE]]"
  - "[[FULL_TREE]]"
  - "[[SYSTEM_MAP]]"
  - "[[AUTHORITATIVE_STATE]]"
  - "[[DEPENDENCY_MAP]]"
  - "[[PLACEMENT_RULES]]"
  - "[[ROADMAP]]"
  - "[[00_ROOT/RSCF_NODE_INDEX]]"
---

# AMOS OS Naming Standard

> **Status:** `ACTIVE_STANDARD`  
> **Standard version:** `1.0.0`  
> **AMOS_CORE target:** `v4.4`  
> **Origin architect / steward:** Trang Phan  
> **Conclusion class:** `AMOS_MODEL`

---

# 0. Purpose

The AMOS OS Naming Standard defines how AMOS artifacts are:

```text
IDENTIFIED
NAMED
VERSIONED
PLACED
REFERRED TO
RENAMED
MIGRATED
DEPRECATED
ARCHIVED
```

without collapsing filesystem representation into semantic identity.

Its primary objective is:

> **Stable identity under architectural evolution.**

The standard governs:

* root folders;
* subsystem folders;
* Markdown architecture artifacts;
* kernel contracts;
* agents;
* skills;
* workflows;
* protocols;
* modes;
* schemas;
* models;
* registries;
* ledgers;
* indexes;
* maps;
* runtime artifacts;
* tests;
* migration aliases;
* artifact IDs;
* version metadata.

The standard follows AMOS integrity rules: explicit uncertainty, provenance preservation, dependency-aware change, and no invented historical identity when source information is missing.

---

# 1. Core Identity Firewall

The following fields are distinct:

```text
FILENAME
FOLDER NAME
ARTIFACT ID
REGISTRY NAME
CLASS NAME
MODULE NAME
DISPLAY NAME
SEMANTIC IDENTITY
VERSION IDENTITY
PROVENANCE LINEAGE
```

Therefore:

```text
Filename
!=
ArtifactID
```

```text
ArtifactID
!=
RegistryName
```

```text
RegistryName
!=
ClassName
```

```text
Path
!=
SemanticIdentity
```

```text
Rename
!=
Reclassification
```

```text
Rename
!=
VersionPromotion
```

```text
VersionLabel
!=
HistoricalProof
```

This is the central naming invariant.

---

# 2. Naming Objectives

AMOS naming should optimize for:

```text
clarity
stability
machine readability
human readability
deterministic sorting
lineage preservation
cross-reference safety
searchability
minimal ambiguity
```

Naming should not optimize for decorative language.

Avoid namespace inflation such as:

```text
ULTIMATE
SUPREME
INFINITE
OMEGA
ULTRA
MAXIMUM
PERFECT
ABSOLUTE
```

unless the term is part of a real, source-defined semantic identity.

Hard rule:

```text
DecorativeIntensity
!=
ArchitecturalMeaning
```

---

# 3. Namespace Layers

AMOS uses multiple namespace layers.

```text
N0 — Repository
N1 — Root section
N2 — Subsystem
N3 — Artifact family
N4 — Artifact
N5 — Internal symbol
N6 — Version
N7 — Runtime instance
```

Example:

```text
AMOS_OS/
21_DOMAINS/
45_MODES/
06_REASONING_MODES/
MODE_FAMILY_REGISTRY.md
```

Each layer has its own identity.

---

# 4. Root Folder Convention

Top-level AMOS OS sections use:

```text
NN_UPPER_SNAKE_CASE
```

Examples:

```text
00_ROOT
01_CANON
02_KERNEL
03_CONTROL_PLANE
04_RUNTIME
05_COGNITIVE_ORGANISM
06_AGENTS
07_SKILLS
08_WORKFLOWS
09_PROTOCOLS
10_MEMORY
11_KNOWLEDGE
12_STATE
```

The numeric prefix defines deterministic order.

It is not part of the semantic name.

Therefore:

```text
01_CANON
```

has:

```yaml
ordinal: 1
semantic_name: CANON
```

---

# 5. Root Ordinal Rule

Root ordinals should:

* use two digits while the namespace remains below 100;
* be unique within the parent namespace;
* preserve intentional order;
* not be reused for a different semantic subsystem after retirement without explicit migration.

Example:

```text
07_SKILLS
```

must not later become:

```text
07_MODELS
```

without a breaking namespace migration.

---

# 6. Folder Naming

General folder form:

```text
UPPER_SNAKE_CASE
```

or when ordered:

```text
NN_UPPER_SNAKE_CASE
```

Preferred:

```text
COGNITIVE_ORGANISM
CONTROL_PLANE
REASONING_MODES
FRESHNESS_REVALIDATION_MODES
```

Avoid:

```text
Cognitive Organism
cognitive-organism
Cognitive_Organism
```

inside governed AMOS OS structural folders.

---

# 7. Root / Framework Markdown Files

Root or architecture contracts use:

```text
UPPER_SNAKE_CASE.md
```

Examples:

```text
ARCHITECTURE.md
AUTHORITATIVE_STATE.md
DEPENDENCY_MAP.md
FULL_TREE.md
MOC.md
NAMING_STANDARD.md
PLACEMENT_RULES.md
ROADMAP.md
SYSTEM_MAP.md
```

These names represent architectural roles.

---

# 8. Reserved Structural Suffixes

AMOS reserves the following suffixes.

## `_MAP.md`

Topology, relationship, or navigational mapping.

Examples:

```text
SYSTEM_MAP.md
DEPENDENCY_MAP.md
AUTHORITY_MAP.md
```

A map describes relations.

It is not necessarily an authoritative registry.

---

## `_REGISTRY.md`

Typed authoritative or semi-authoritative membership registry.

Examples:

```text
AGENT_REGISTRY.md
MODE_FAMILY_REGISTRY.md
MODEL_REGISTRY.md
```

A registry should answer:

```text
what entries exist
what identity each has
what version/state each has
```

---

## `_LEDGER.md`

Append-oriented historical or audit state.

Examples:

```text
EXECUTION_LEDGER.md
MIGRATION_LEDGER.md
PROVENANCE_LEDGER.md
```

Ledger semantics imply:

```text
historical continuity
append/replay
auditability
```

not mutable current-state truth.

---

## `_INDEX.md`

Search/navigation index.

Examples:

```text
RSCF_NODE_INDEX.md
MODE_INDEX.md
SKILL_INDEX.md
```

Index membership does not imply canon status.

---

## `_SPEC.md`

Formal specification.

Examples:

```text
MODE_SPEC.md
PROTOCOL_SPEC.md
AGENT_SPEC.md
```

---

## `_CONTRACT.md`

Boundary or interface agreement.

Examples:

```text
RUNTIME_CONTRACT.md
TOOL_CONTRACT.md
AUTHORITY_CONTRACT.md
```

---

## `_SCHEMA.md`

Human-readable schema specification.

Executable schemas may instead use:

```text
*.json
*.yaml
*.py
```

depending on implementation.

---

## `_CANON.md`

Use only when the artifact is explicitly canon-governed.

Do not add `_CANON` decoratively.

---

# 9. Kernel Naming

Kernel-level artifacts use:

```text
K_<NAME>
```

Examples:

```text
K_RSCF
K_PROVENANCE
K_ROUTING
K_VALIDATION
K_STATE_TRANSITION
```

Files may use:

```text
K_RSCF_CONTRACT.md
K_PROVENANCE_SCHEMA.md
K_ROUTING_SPEC.md
```

`K_` means:

```text
kernel-owned
```

not:

```text
universally true
```

---

# 10. Agent Naming

Agent contracts use:

```text
A_<NAME>
```

Canonical semantic names:

```text
A_ENVIRONMENT_SCAN
A_EXECUTOR
A_INVESTMENT
A_RESEARCH
A_VALIDATOR
A_ORCHESTRATOR
```

Python classes may retain conventional form:

```python
EnvironmentScan_Agent
Executor_Agent
Investment_Agent
```

The class name and artifact name are related but distinct.

Example:

```yaml
artifact_id: AMOS-AGENT-ENVIRONMENT-SCAN
registry_name: EnvironmentScan_Agent
contract_name: A_ENVIRONMENT_SCAN
```

---

# 11. Skill Naming

Skill directories should use lowercase kebab-case where the runtime/skill registry expects that convention.

Example:

```text
amos-phase-c-cognition-field
amos-7-part-universe-canon-full
amos-19x19-family-complete
```

Skill artifact metadata should include:

```yaml
name:
version:
domain:
source:
```

Do not derive version identity from the directory name unless the registry explicitly requires it.

---

# 12. Workflow Naming

Workflow names should be action/process oriented.

Preferred:

```text
amos-phase-c-cognition-field.md
amos-agent-validation.md
amos-repository-migration.md
```

Avoid vague names such as:

```text
workflow-final.md
new-process.md
best-workflow.md
```

---

# 13. Protocol Naming

Protocols should express interaction semantics.

Preferred:

```text
AGENT_HANDOFF_PROTOCOL.md
COMMIT_PROTOCOL.md
RSCF_VALIDATION_PROTOCOL.md
STATE_SYNC_PROTOCOL.md
```

Protocol identity should be independent of implementation language.

---

# 14. Mode Naming

Mode families use:

```text
NN_<SEMANTIC_NAME>_MODES
```

Examples:

```text
06_REASONING_MODES
10_EPISTEMIC_MODES
17_ATTENTION_MODES
41_DECISION_MODES
84_FRESHNESS_REVALIDATION_MODES
```

Mode family folder contents should typically include:

```text
MODE_FAMILY_SPEC.md
MODE_FAMILY_REGISTRY.md
```

Individual mode identifiers should be stable semantic names.

Example:

```text
EXPLORATORY_MAPPING
DIAGNOSTIC_ANALYSIS
DESIGN_AND_ARCHITECTURE
AUDIT_AND_CRITIQUE
```

Hard rule:

```text
Mode
!=
Agent
```

---

# 15. Model Naming

Formal models should declare their scope in identity.

Preferred:

```text
PORTFOLIO_RISK_MODEL
COGNITIVE_FIELD_MODEL
REGIME_MODEL
PROVENANCE_CORRELATION_MODEL
```

Avoid:

```text
PERFECT_MODEL
MASTER_MODEL
ULTIMATE_MODEL
```

unless those are preserved historical/source identities.

---

# 16. Schema Naming

Schemas should identify the object being typed.

Examples:

```text
AGENT_SCHEMA
EXECUTION_REQUEST_SCHEMA
MODE_STATE_SCHEMA
RSCF_NODE_SCHEMA
```

Executable schema version should appear in metadata:

```yaml
schema_name: AGENT_SCHEMA
schema_version: "2.0.0"
```

not be inferred from:

```text
AGENT_SCHEMA_FINAL_FINAL.json
```

---

# 17. Registry Naming

Typed registry artifacts:

```text
<DOMAIN>_REGISTRY.md
```

Examples:

```text
AGENT_REGISTRY.md
MODE_REGISTRY.md
SKILL_REGISTRY.md
MODEL_REGISTRY.md
TOOL_REGISTRY.md
```

Registry entries should minimally carry:

```yaml
id:
name:
version:
status:
owner:
path:
```

---

# 18. Artifact ID Convention

Artifact IDs are stable semantic identifiers.

Preferred form:

```text
AMOS-<DOMAIN>-<OBJECT>
```

Examples:

```text
AMOS-OS-NAMING-STANDARD
AMOS-OS-ROOT-ARCHITECTURE
AMOS-INVESTMENT-AGENT
AMOS-EXECUTOR-AGENT
AMOS-ENVIRONMENT-SCAN-AGENT
```

Artifact IDs should:

* use uppercase;
* use hyphens;
* avoid filesystem ordinals;
* avoid volatile directory paths;
* remain stable across safe renames.

---

# 19. Artifact ID Invariant

A path change does not normally change `artifact_id`.

Example:

```text
old path:
03_CONTROL_PLANE/OLD_FOLDER/AUTHORITY.md
```

to:

```text
new path:
03_CONTROL_PLANE/AUTHORITY/AUTHORITY.md
```

may retain:

```yaml
artifact_id: AMOS-CONTROL-PLANE-AUTHORITY
```

Therefore:

```text
Move
!=
NewArtifact
```

---

# 20. Semantic Identity

Semantic identity answers:

> What is this thing?

Examples:

```text
RSCF validator
Investment Agent
Reasoning Mode Registry
AMOS OS Root Architecture
```

Semantic identity is stronger than filename representation.

---

# 21. Display Name

Display names may be human-friendly.

Example:

```yaml
artifact_id: AMOS-OS-NAMING-STANDARD
name: AMOS_OS_NAMING_STANDARD
title: "AMOS OS Naming Standard — Canonical Identity and Namespace Governance"
```

These may coexist because they serve different roles.

---

# 22. Version Axes

AMOS does not assume one universal version number.

Possible axes:

```text
document_version
component_version
schema_version
protocol_version
runtime_version
model_version
dataset_version
canon_version
architecture_version
migration_contract_version
```

These are distinct.

Example:

```yaml
document_version: "2.0.0"
component_version: "1.4.0"
schema_version: "3.0.0"
amos_core_target: "v4.4"
```

---

# 23. Semantic Versioning

Default governed artifact version syntax:

```text
MAJOR.MINOR.PATCH
```

Example:

```text
2.3.1
```

Interpretation:

```text
MAJOR
=
breaking semantic/interface change

MINOR
=
backward-compatible capability or structure addition

PATCH
=
non-breaking correction
```

---

# 24. Major Version

Increment `MAJOR` when:

* required fields change incompatibly;
* authority semantics change;
* persisted state format becomes incompatible;
* interface semantics break;
* identity contract changes;
* lifecycle semantics materially change;
* prior consumers require migration.

---

# 25. Minor Version

Increment `MINOR` when:

* optional fields are added;
* backward-compatible capabilities are added;
* new registry entries are supported;
* new validators are added;
* new modes/features are introduced without contract break.

---

# 26. Patch Version

Increment `PATCH` for:

* typo fixes;
* wording clarification;
* metadata correction;
* non-semantic refactor;
* formatting;
* added examples that do not alter contract.

---

# 27. AMOS_CORE Target

`amos_core_target` is not the artifact's own version.

Example:

```yaml
document_version: "2.0.0"
amos_core_target: "v4.4"
```

means:

```text
this artifact = v2.0.0
designed against = AMOS_CORE v4.4
```

Do not write:

```text
version: v4.4
```

unless the artifact itself is actually version 4.4.

---

# 28. Historical Version Firewall

Missing historical version information remains:

```text
UNKNOWN/GAP
```

Do not infer:

```text
no version label
→ historical v0
```

unless a migration policy explicitly assigns a baseline.

If a baseline is assigned:

```yaml
source_version: UNKNOWN/GAP
assigned_version: "0.0.0"
assignment_reason: migration_baseline
```

This preserves epistemic integrity.

---

# 29. Filename Versioning

Default architecture preference:

```text
version metadata inside artifact
```

rather than:

```text
version embedded in filename
```

Preferred:

```text
ARCHITECTURE.md
```

with:

```yaml
document_version: "2.0.0"
```

instead of:

```text
ARCHITECTURE_v2.0.0.md
```

unless multiple parallel physical versions must coexist.

---

# 30. When Filename Versions Are Allowed

Filename versions are appropriate when:

* multiple versions intentionally coexist;
* runtime loader requires versioned modules;
* migration snapshot preservation requires immutable copies;
* external interface contract requires it;
* historical archive stores explicit versions.

Example:

```text
AGENT_SCHEMA_v1.json
AGENT_SCHEMA_v2.json
```

---

# 31. Mutable Canonical Pointer

When versioned files coexist, use an unversioned registry/pointer where useful.

Example:

```text
AGENT_SCHEMA_CURRENT.md
```

or registry metadata:

```yaml
canonical_version: "2.0.0"
path: AGENT_SCHEMA_v2.json
```

Avoid aliases such as:

```text
FINAL
LATEST_FINAL
REAL_FINAL
FINAL2
```

---

# 32. Prohibited Version Labels

Do not use as machine-significant versions:

```text
FINAL
LATEST
NEW
BEST
ULTIMATE
INFINITY
OMEGA
COMPLETE
PERFECT
```

These may survive as historical/source labels but must not substitute for structured version metadata.

---

# 33. Source Identity Preservation

If an imported source originally uses:

```text
AMOS_OMEGA_QUANTUM_STACK
```

do not silently rename its semantic identity merely because AMOS naming preferences now avoid decorative terms.

Preserve:

```yaml
source_name: AMOS_OMEGA_QUANTUM_STACK
canonical_alias:
```

until a governed migration decision exists.

Hard rule:

```text
Normalization
!=
HistoricalErasure
```

---

# 34. Source Name vs Canonical Name

A migrated artifact may carry:

```yaml
source_name: "AMOS_SUPER_MIND_OS"
canonical_name: "AMOS_MIND_OS"
```

only when the mapping is explicitly reviewed.

Until then:

```yaml
canonical_name: UNKNOWN/GAP
```

is preferable to invented normalization.

---

# 35. Rename Governance

Renaming requires classification.

Possible rename classes:

```text
R0 — cosmetic
R1 — filesystem-only
R2 — namespace migration
R3 — semantic identity migration
R4 — public/external contract migration
```

Validation requirements increase from R0 to R4.

---

# 36. Cosmetic Rename

Examples:

```text
duplicate underscore cleanup
case normalization
obvious typo
```

Still requires collision check.

---

# 37. Filesystem Rename

Changes physical path/name while preserving semantic identity.

Must preserve:

```text
artifact_id
provenance
registry identity
version lineage
```

unless explicitly changed separately.

---

# 38. Namespace Migration

Changes a governed internal namespace.

Requires:

```text
dependency graph
reference audit
alias map
migration manifest
post-validation
```

---

# 39. Semantic Identity Migration

Changes what the artifact is called conceptually.

Requires:

```text
source justification
canon review
dependency review
registry migration
provenance link
deprecation alias
```

---

# 40. Rename Manifest

Every material rename migration should support:

```yaml
RenameManifest:
  migration_id:
  version:

  mappings:
    - old_path:
      new_path:
      artifact_id:
      semantic_identity_changed:
      reason:

  collisions: []

  references_updated: []

  unresolved_gaps: []

  validation:

  rollback:
```

---

# 41. Alias Rule

Aliases are allowed for navigation and compatibility.

Example:

```yaml
aliases:
  - AMOS Naming Standard
  - AMOS Namespace Standard
```

Aliases must not silently become separate artifacts.

---

# 42. Deprecated Names

When a semantic name is replaced:

```yaml
previous_names:
  - OLD_NAME

deprecated_names:
  - OLD_NAME

canonical_name:
  NEW_NAME
```

Preserve old names long enough to resolve historical references.

---

# 43. Rename Collision Rule

A rename is blocked when:

```text
OldA != OldB
```

but:

```text
Normalize(OldA)
=
Normalize(OldB)
```

unless a separate merge decision exists.

Status:

```text
COLLISION
```

not:

```text
PASS
```

---

# 44. Case-Fold Collision

Check case-insensitive equivalence.

Example:

```text
Agent.md
AGENT.md
```

may be distinct on one filesystem and identical on another.

Cross-platform AMOS repositories should treat such collisions as material.

---

# 45. Unicode Normalization

Where cross-platform portability matters, names should use normalized Unicode.

Preferred structural namespace:

```text
ASCII
```

for core paths and machine-consumed identifiers.

Human-facing titles may use Unicode.

---

# 46. Character Rules

Machine structural names should generally use:

```text
A-Z
0-9
_
-
.
```

according to namespace.

Avoid in filesystem contracts:

```text
/
\
:
*
?
"
<
>
|
```

and control characters.

---

# 47. Spaces

Core governed filesystem names should avoid spaces.

Preferred:

```text
COGNITIVE_MATRIX
```

not:

```text
Cognitive Matrix
```

Display titles may use spaces.

---

# 48. Hyphens vs Underscores

Use:

```text
UPPER_SNAKE_CASE
```

for AMOS OS structural filesystem names.

Use:

```text
lowercase-kebab-case
```

where external runtime conventions require it, especially skill names.

Use:

```text
UPPER-HYPHENATED
```

for stable artifact IDs.

Example:

```yaml
folder: COGNITIVE_ORGANISM
skill: amos-phase-c-cognition-field
artifact_id: AMOS-PHASE-C-COGNITION-FIELD
```

---

# 49. Python Names

Python modules:

```text
snake_case.py
```

unless preserving existing AMOS compatibility conventions.

Python classes:

```text
PascalCase
```

or established legacy style where required.

Legacy names such as:

```python
Investment_Agent
```

may be preserved for compatibility.

Do not mechanically rename executable symbols based only on documentation naming rules.

---

# 50. TypeScript Names

Recommended:

```text
kebab-case.ts
```

or existing package convention.

Exported types/classes:

```text
PascalCase
```

Constants:

```text
UPPER_SNAKE_CASE
```

The repository-local convention takes precedence when consistency is load-bearing.

---

# 51. JSON Names

JSON artifact filenames should describe the semantic object.

Examples:

```text
agent_schema.json
runtime_contract.json
mode_registry.json
```

Legacy AMOS source names should preserve provenance even when they are not canonical new-file conventions.

---

# 52. Markdown Wiki Links

Wiki-link references should use stable canonical note names where possible.

Example:

```text
ARCHITECTURE
DEPENDENCY_MAP
NAMING_STANDARD
```

After rename, links must be audited.

Hard rule:

```text
FileMoved
!=
ReferencesUpdated
```

---

# 53. RSCF Naming

RSCF node IDs must remain stable where they identify persistent reasoning/provenance entities.

Preferred:

```text
AMOS_OS_NAMING_STANDARD
```

or deterministic system-generated IDs where that subsystem requires them.

Do not change node IDs merely because filenames move.

---

# 54. RSCF Identity Firewall

```text
RSCFNodeID
!=
FilePath
```

```text
ClaimID
!=
SectionHeading
```

```text
ProvenanceID
!=
SourceFilename
```

Stable logical IDs prevent path migration from destroying reasoning lineage.

---

# 55. Ledger Entry IDs

Append-oriented ledgers should use stable entry identifiers.

Possible form:

```text
<LEDGER>-<DATE>-<SEQUENCE>
```

Example:

```text
MIG-20260825-0001
```

or UUID/hash-based identity where appropriate.

The method must be defined by the ledger contract.

---

# 56. Runtime Instance IDs

Runtime instances require transient identity distinct from artifact identity.

Example:

```yaml
component:
  artifact_id: AMOS-INVESTMENT-AGENT
  version: "1.0.0"

runtime:
  instance_id: "run_..."
```

Hard rule:

```text
Artifact
!=
Instance
```

---

# 57. Environment Names

Standard environment values should be bounded enums when possible.

Example:

```text
DEV
TEST
STAGING
PRODUCTION
SIMULATION
```

Avoid:

```text
REAL
LIVE_REAL
FINAL_PROD
PROD2
```

---

# 58. Lifecycle Names

Preferred lifecycle vocabulary:

```text
PLACEHOLDER
DRAFT
SOURCE_BOUND
MODEL
IMPLEMENTED
TESTED
VALIDATED_FOR_SCOPE
ACTIVE
DEPRECATED
ARCHIVED
QUARANTINED
```

Lifecycle terms should remain distinct from epistemic conclusion classes.

---

# 59. Epistemic Names

Use:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN/GAP
```

Conclusion classes:

```text
VERIFIED
DERIVED
MODEL
CONDITIONAL
COMPETING
UNKNOWN/GAP
```

Do not invent decorative confidence labels.

---

# 60. State Naming

State names should describe actual state.

Preferred:

```text
REGISTERED_STUB
READ_ONLY_PROTOTYPE
LIVE_SCANNER
VALIDATED_EXECUTOR
IN_DOUBT
QUARANTINED
```

Avoid:

```text
DONE
GOOD
READYISH
WORKING
COMPLETE
```

unless formally defined.

---

# 61. Boolean Names

Boolean fields should be clear predicates.

Preferred:

```yaml
provenance_required: true
authority_validated: false
rollback_supported: true
```

Avoid:

```yaml
provenance: true
authority: true
rollback: true
```

when those fields could ambiguously mean presence rather than state.

---

# 62. Time Field Naming

Use explicit temporal semantics.

Preferred:

```text
created_at
updated_at
observed_at
effective_at
committed_at
expires_at
validated_at
```

Avoid generic:

```text
date
timestamp
time
```

when more than one temporal meaning exists.

---

# 63. Hash Field Naming

Use explicit hash semantics.

Examples:

```text
content_hash
plan_hash
schema_hash
source_hash
state_hash
```

Do not call all hashes simply:

```text
hash
```

when multiple hashes coexist.

---

# 64. Provenance Field Naming

Preferred:

```yaml
provenance:
  source_id:
  source_version:
  parent_ids:
  transformation:
  observed_at:
```

Avoid overwriting source lineage with only the current filename.

---

# 65. Dependency Names

Dependencies should use stable semantic/artifact identity when possible.

Preferred:

```yaml
dependencies:
  - AMOS-OS-ROOT-ARCHITECTURE
  - AMOS-OS-DEPENDENCY-MAP
```

Paths may be stored as additional resolution metadata.

---

# 66. Canon Naming

The term `CANON` is reserved for governed canonical status.

Do not name a draft:

```text
NEW_CANON.md
```

unless it has actually passed canon admission.

Candidate artifacts should use:

```text
CANDIDATE
PROPOSAL
DRAFT
RESEARCH
```

as appropriate.

---

# 67. Placeholder Naming

Placeholder files should use their eventual canonical filename.

Example:

```text
DEPENDENCY_MAP.md
```

with:

```yaml
status: PROPOSED_SPECIFICATION
```

not:

```text
DEPENDENCY_MAP_PLACEHOLDER.md
```

This minimizes rename churn when content is promoted.

---

# 68. Placeholder Promotion

Promotion should update metadata:

```yaml
status: ACTIVE
```

or appropriate lifecycle state.

It should not require renaming the file unless semantics changed.

---

# 69. Archive Naming

Archive structures may include date/version for historical disambiguation.

Examples:

```text
2026-08-25/
v1/
migration_20260825/
```

Archive names should preserve original identities where feasible.

---

# 70. Backup Naming

Backups are operational artifacts, not canonical versions.

Preferred:

```text
backup_20260825T103000Z
```

Do not treat:

```text
backup
```

as a semantic version.

---

# 71. Migration Naming

Migration IDs should be unique and traceable.

Example:

```text
MIGRATION_20260825_NAMESPACE_V1
```

Migration records should retain:

```text
old identity
new identity
mapping
reason
version
validation
rollback
```

---

# 72. Test Naming

Tests should identify the behavior under test.

Preferred Python:

```text
test_agent_registration
test_mode_registry_integrity
test_dependency_cycle_detection
```

Avoid:

```text
test1
test_final
test_everything
```

---

# 73. Fixture Naming

Fixtures should describe semantic purpose.

Example:

```text
valid_agent_context
stale_authority_context
conflicting_provenance_graph
```

---

# 74. Error Code Naming

Error codes should be stable and machine-readable.

Example:

```text
NAMING-E001
NAMING-E002
```

Possible registry:

```text
NAMING-E001 INVALID_STRUCTURAL_NAME
NAMING-E002 COLLISION
NAMING-E003 UNKNOWN_VERSION_IDENTITY
NAMING-E004 SEMANTIC_IDENTITY_COLLISION
NAMING-E005 UNRESOLVED_REFERENCE
```

---

# 75. Failure State Naming

Use explicit failure classes.

Preferred:

```text
COLLISION
REFERENCE_BREAK
VERSION_AMBIGUITY
IDENTITY_COLLAPSE
PATH_ESCAPE
STALE_ALIAS
```

Do not reduce all failures to:

```text
ERROR
```

where classification is decision-relevant.

---

# 76. Naming Validation Pipeline

```text
INPUT NAME
↓
DETERMINE NAMESPACE
↓
VALIDATE CHARACTERS
↓
VALIDATE FORMAT
↓
VALIDATE RESERVED TERMS
↓
CHECK COLLISION
↓
CHECK ARTIFACT ID
↓
CHECK VERSION
↓
CHECK REFERENCES
↓
PASS / BLOCK
```

---

# 77. Rename Validation Pipeline

```text
SOURCE OBJECT
↓
IDENTIFY ARTIFACT
↓
IDENTIFY REFERENCES
↓
CLASSIFY RENAME
↓
GENERATE TARGET NAME
↓
CHECK COLLISION
↓
CHECK SEMANTIC CHANGE
↓
GENERATE ALIAS / MANIFEST
↓
REVIEW
↓
COMMIT
↓
VERIFY
```

---

# 78. Rename Commit Rule

A rename may commit only when:

```text
IdentityKnown
∧ TargetValid
∧ CollisionFree
∧ ReferencesHandled
∧ ProvenancePreserved
∧ RollbackKnown
```

For high-impact canonical artifacts:

```text
∧ CanonReviewPassed
```

---

# 79. Unknown Identity Rule

If the semantic meaning of a token is unknown:

```text
UNKNOWN/GAP
```

Do not automatically strip it.

Example:

```text
OMEGA
CANON
FULL
EXPANDED
```

may be decorative in one context and load-bearing in another.

Therefore:

```text
SameToken
!=
SameMeaningAcrossArtifacts
```

---

# 80. Case Preservation

Structural namespaces use canonical casing.

Examples:

```text
CONTROL_PLANE
AUTHORITATIVE_STATE.md
```

Human-readable titles may use:

```text
Control Plane
Authoritative State
```

---

# 81. Acronyms

Stable acronyms may remain uppercase.

Examples:

```text
AMOS
RSCF
GMEF
API
OS
HML
```

Avoid introducing unexplained acronyms when a clear semantic name exists.

---

# 82. H/M/L Naming

H/M/L artifacts should explicitly identify level only when the level is semantically necessary.

Examples:

```text
H_DOMAIN_REGISTRY
M_SUBSYSTEM_MAP
L_COMPONENT_INDEX
```

Do not encode H/M/L into every filename without need.

---

# 83. Scope Naming

Names should encode scope only when it prevents ambiguity.

Preferred:

```text
PORTFOLIO_RISK_MODEL
```

over:

```text
RISK_MODEL
```

if multiple risk domains exist.

But avoid excessively long names that duplicate full paths.

---

# 84. Parent Context Rule

Filesystem hierarchy already provides context.

Example:

```text
21_DOMAINS/
45_MODES/
17_ATTENTION_MODES/
MODE_FAMILY_SPEC.md
```

is preferable to:

```text
AMOS_OS_DOMAINS_MODES_ATTENTION_MODE_FAMILY_SPEC.md
```

inside that folder.

---

# 85. MECE Naming

Sibling names should be mutually distinguishable.

Bad:

```text
MEMORY
LONG_MEMORY
PERSISTENT_MEMORY
```

without defined boundaries.

Better:

```text
WORKING_MEMORY
EPISODIC_MEMORY
CASE_MEMORY
VALIDATED_LONG_TERM_MEMORY
```

if those categories are actually canon-defined.

---

# 86. Overlap Firewall

Two artifacts must not use near-identical names for materially different roles without explicit distinction.

Example:

```text
MODE_REGISTRY
MODE_FAMILY_REGISTRY
```

is acceptable because the scope difference is typed.

---

# 87. Singular vs Plural

Folder collections generally use plural semantic groups where appropriate:

```text
AGENTS
SKILLS
WORKFLOWS
PROTOCOLS
MODELS
TOOLS
```

A singular concrete artifact uses singular identity:

```text
Investment_Agent
Executor_Agent
```

Consistency is more important than dogmatic grammar.

---

# 88. Action vs Object Naming

Processes/workflows should favor verbs or process nouns:

```text
VALIDATE_AGENT
REBUILD_INDEX
MIGRATION_WORKFLOW
```

Persistent objects should favor nouns:

```text
AGENT_REGISTRY
DEPENDENCY_MAP
AUTHORITY_LEDGER
```

---

# 89. Command Naming

Commands should be explicit actions.

Examples:

```text
validate
register
promote
archive
rollback
reindex
```

Avoid generic commands:

```text
run
do
process
handle
```

when multiple behaviors could apply.

---

# 90. API Field Compatibility

Once an external field name becomes part of a stable interface, renaming it is a compatibility change.

Example:

```yaml
artifact_id:
```

to:

```yaml
id:
```

may be a breaking change even if semantically equivalent.

Version accordingly.

---

# 91. Registry Compatibility

Registry keys should not be reused for unrelated artifacts.

If an entry is retired:

```yaml
status: RETIRED
```

retain enough history to prevent semantic reuse ambiguity.

---

# 92. Name Reuse Rule

Do not reuse a retired canonical identity for a new unrelated component.

Preferred:

```text
old identity remains retired
new component receives new identity
```

This preserves lineage.

---

# 93. Canonical Link Rule

Documentation should prefer canonical artifact identity over transient filenames when both are available.

Example:

```yaml
dependency:
  artifact_id: AMOS-OS-NAMING-STANDARD
  path: 00_ROOT/00_ROOT_NAMING_STANDARD.md
```

---

# 94. Path Rule

Paths are resolution metadata.

They may change.

Therefore:

```text
Path
=
Location
```

not:

```text
Identity
```

---

# 95. Naming Provenance

Material naming changes should preserve:

```yaml
naming_provenance:
  source_name:
  previous_names: []
  current_name:
  changed_by:
  changed_at:
  migration_id:
  reason:
```

---

# 96. Naming Ledger

A mature AMOS OS may maintain:

```text
NAMING_LEDGER.md
```

or equivalent structured registry.

Purpose:

```text
track identity changes
preserve aliases
prevent name reuse
reconstruct migrations
```

---

# 97. Naming Registry

A central registry may eventually expose:

```yaml
ArtifactRegistryEntry:
  artifact_id:
  canonical_name:
  display_name:
  current_path:
  version:
  lifecycle:
  aliases:
  previous_names:
  owner:
```

This is a recommended architecture pattern, not a claim that such registry is currently implemented.

---

# 98. Deterministic Sorting

Names should permit deterministic ordering.

Ordered folders:

```text
00_
01_
02_
...
```

Registries should sort by a defined key such as:

```text
ordinal
artifact_id
name
```

Do not rely on filesystem return order.

---

# 99. Searchability

Names should use semantically meaningful tokens.

Preferred:

```text
FRESHNESS_REVALIDATION_MODES
```

over:

```text
FR_MODES
```

unless acronym use is already canonical and widely defined.

---

# 100. Naming Length

Names should be long enough to disambiguate but short enough to remain usable.

Optimization objective:

```text
minimum length
subject to
semantic uniqueness
```

not simply:

```text
shortest possible name
```

---

# 101. RSCF Naming Contract

```yaml
RSCFNaming:
  node_id:
  claim_id:
  artifact_id:
  path:
  semantic_name:
```

All five may refer to related objects while remaining distinct.

---

# 102. Name Resolution Order

When resolving a reference:

```text
artifact_id
↓
canonical registry identity
↓
canonical name
↓
approved alias
↓
historical alias
↓
path
```

Exact runtime order may differ by implementation, but semantic identity should outrank volatile path where possible.

---

# 103. Ambiguous Name Resolution

If one alias resolves to multiple live artifacts:

```text
AMBIGUOUS
```

Do not choose by convenience.

Resolve using:

```text
scope
parent namespace
version
artifact_id
```

---

# 104. Name Conflict States

```text
NO_CONFLICT
CASE_CONFLICT
PATH_CONFLICT
ALIAS_CONFLICT
REGISTRY_CONFLICT
SEMANTIC_CONFLICT
VERSION_CONFLICT
UNKNOWN
```

`UNKNOWN` is not `NO_CONFLICT`.

---

# 105. Naming Authority

Not every component may redefine canonical names.

Conceptually:

```text
Local worker
→ may propose rename

Governance / repository authority
→ approves canonical migration
```

Hard boundary:

```text
RenameCapability
!=
NamingAuthority
```

---

# 106. Naming Change Classes

| Class                | Example                  | Governance          |
| -------------------- | ------------------------ | ------------------- |
| Cosmetic             | typo                     | low                 |
| Structural           | folder normalization     | moderate            |
| Dependency-impacting | module rename            | high                |
| Canon identity       | canonical concept rename | very high           |
| External API         | public field rename      | breaking governance |

---

# 107. Cross-Domain Names

Cross-domain artifacts should avoid claiming universal scope without evidence.

Preferred:

```text
FINANCIAL_RISK_MODEL
```

over:

```text
UNIVERSAL_RISK_MODEL
```

unless the latter is explicitly an AMOS model name and appropriately classed.

---

# 108. Model-Language Firewall

Terms such as:

```text
quantum
consciousness
universal
absolute
infinite
```

may exist in AMOS source terminology.

Their presence in a name does not automatically establish external scientific validity.

Names preserve source identity; they do not prove claims.

---

# 109. Source Preservation Rule

Imported historical source artifacts may retain nonstandard names.

Example:

```text
AMOS_FULL_BRAIN_OS.json
```

This is acceptable as preserved source identity.

New governed artifacts should follow current standard unless compatibility requires otherwise.

---

# 110. Legacy Names

Legacy names should be classified:

```text
ACTIVE_COMPATIBILITY
DEPRECATED
HISTORICAL
UNKNOWN
```

Do not delete old identity information merely because a cleaner canonical name now exists.

---

# 111. Naming Migration State Machine

```text
PROPOSED
↓
ANALYZED
↓
COLLISION_CHECKED
↓
DEPENDENCY_CHECKED
↓
APPROVED
↓
APPLIED
↓
VERIFIED
```

Failure branches:

```text
BLOCKED
PARTIAL
ROLLED_BACK
IN_DOUBT
```

---

# 112. Rename Recovery

If rename validation fails:

```text
STOP
↓
PRESERVE CURRENT STATE
↓
IDENTIFY APPLIED OPERATIONS
↓
ROLL BACK SAFE CHANGES
↓
REPAIR REFERENCES
↓
REVALIDATE
```

Do not continue blindly through a partial namespace migration.

---

# 113. Naming Test Suite

Minimum validation should eventually include:

```text
T01 root folder grammar
T02 duplicate ordinal detection
T03 duplicate artifact ID detection
T04 invalid character detection
T05 case-fold collision detection
T06 alias collision detection
T07 version grammar
T08 missing version metadata
T09 path/artifact identity separation
T10 registry/path consistency
T11 broken wiki-link detection
T12 broken dependency reference detection
T13 illegal CANON naming
T14 placeholder lifecycle validation
T15 deprecated-name resolution
T16 artifact ID persistence after move
T17 source-name preservation
T18 migration manifest validity
T19 rollback mapping
T20 unknown identity remains UNKNOWN/GAP
```

---

# 114. Naming Validation Result

```yaml
NamingValidationResult:
  artifact_id:
  path:

  grammar:
    PASS
    FAIL

  identity:
    PASS
    FAIL
    UNKNOWN

  version:
    PASS
    FAIL
    UNKNOWN

  collision:
    PASS
    FAIL
    UNKNOWN

  references:
    PASS
    FAIL
    UNKNOWN

  overall:
    PASS
    CONDITIONAL
    FAIL
    UNKNOWN/GAP

  issues: []
```

Hard rule:

```text
UNKNOWN
cannot be promoted to
PASS
```

---

# 115. Naming Failure Registry

```text
N001 INVALID_CASE
N002 INVALID_SEPARATOR
N003 INVALID_ORDINAL
N004 DUPLICATE_ORDINAL
N005 DUPLICATE_ARTIFACT_ID
N006 PATH_COLLISION
N007 CASEFOLD_COLLISION
N008 ALIAS_COLLISION
N009 REGISTRY_COLLISION
N010 VERSION_AMBIGUITY
N011 UNKNOWN_HISTORICAL_VERSION
N012 SEMANTIC_IDENTITY_COLLAPSE
N013 BROKEN_REFERENCE
N014 BROKEN_DEPENDENCY
N015 CANON_STATUS_MISUSE
N016 PATH_AS_IDENTITY
N017 SOURCE_NAME_LOSS
N018 PARTIAL_RENAME
N019 UNRESOLVED_LEGACY_ALIAS
N020 UNAUTHORIZED_CANONICAL_RENAME
```

---

# 116. Naming Invariants

```text
NS01 Filename != ArtifactID
NS02 Path != SemanticIdentity
NS03 RegistryName != ClassName
NS04 Rename != Reclassification
NS05 Rename != VersionPromotion
NS06 MissingVersion != v0
NS07 AssignedVersion != HistoricalVersion
NS08 SourceNameMustRemainRecoverable
NS09 CanonNamesRequireCanonStatus
NS10 ArtifactIDsAreStableAcrossSafeMoves
NS11 OrdinalsDefineOrderNotIdentity
NS12 AliasesDoNotCreateNewArtifacts
NS13 DeprecatedNamesRemainResolvableWhereRequired
NS14 UnknownIdentity != ValidatedIdentity
NS15 Collision != PASS
NS16 FileMove != ReferenceRepair
NS17 CosmeticNormalizationCannotDestroyMeaning
NS18 VersionAxesRemainDistinct
NS19 RuntimeInstanceID != ArtifactID
NS20 ModelNameDoesNotEstablishEmpiricalValidity
NS21 WorkerRenameCapability != NamingAuthority
NS22 ExternalContractRenameRequiresCompatibilityReview
NS23 HistoricalLineageMustSurviveMigration
NS24 PlaceholderUsesFutureCanonicalFilename
NS25 RepositoryConsistencyCannotOverrideProvenance
```

---

# 117. Standard Examples

## Root contract

```yaml
artifact_id: AMOS-OS-ROOT-ARCHITECTURE
name: AMOS_OS_ARCHITECTURE
document_version: "2.0.0"
path: 00_ROOT/ARCHITECTURE.md
```

---

## Agent

```yaml
artifact_id: AMOS-INVESTMENT-AGENT
registry_name: Investment_Agent
component_version: "1.0.0"
path: 06_AGENTS/INVESTMENT/
```

---

## Skill

```yaml
artifact_id: AMOS-SKILL-PHASE-C-COGNITION-FIELD
name: amos-phase-c-cognition-field
version: "1.0.0"
```

---

## Mode family

```yaml
artifact_id: AMOS-MODE-FAMILY-REASONING
name: REASONING_MODES
ordinal: 6
path: 21_DOMAINS/45_MODES/06_REASONING_MODES
```

---

# 118. Anti-Patterns

Do not create names such as:

```text
FINAL_FINAL.md
FINAL_v2_REAL.md
NEWEST_VERSION.md
MASTER_FINAL_FINAL.json
PERFECT_AGENT.py
ULTIMATE_MODE.md
COPY_OF_ARCHITECTURE.md
ARCHITECTURE_NEW.md
ARCHITECTURE_FIXED.md
```

Use version metadata and lifecycle state instead.

---

# 119. Preferred Replacements

Instead of:

```text
ARCHITECTURE_FINAL.md
```

use:

```text
ARCHITECTURE.md
```

with:

```yaml
document_version: "2.0.0"
status: ACTIVE
```

Instead of:

```text
OLD_ARCHITECTURE.md
```

use archive lineage:

```text
24_ARCHIVE/ARCHITECTURE/v1/
```

or a formal migration record.

---

# 120. Naming Standard Promotion Gate

This standard may be treated as active at the architectural/model level because it now defines:

```text
folder naming
file naming
artifact identity
registry identity
version semantics
aliasing
mode naming
agent naming
skill naming
schema naming
rename governance
migration
provenance
tests
failure
recovery
```

Implementation enforcement remains separately auditable.

Therefore:

```text
NamingStandardSpecified
!=
RepositoryFullyCompliant
```

---

# 121. Current Implementation Boundary

This document does not establish that:

```text
all existing AMOS files comply
all old names are migrated
all artifact IDs exist
all aliases are registered
all version metadata is valid
all cross-links resolve
all rename migrations are reversible
```

Those remain repository-audit tasks.

Conclusion:

```text
STANDARD = DEFINED

FULL COMPLIANCE = UNKNOWN/GAP
```

---

# 122. Recommended Compliance Audit

```text
SCAN TREE
↓
CLASSIFY NAMES
↓
CHECK ROOT ORDINALS
↓
CHECK FILE GRAMMAR
↓
CHECK ARTIFACT IDs
↓
CHECK VERSION METADATA
↓
CHECK DUPLICATES
↓
CHECK ALIASES
↓
CHECK REFERENCES
↓
CHECK LEGACY NAMES
↓
GENERATE VIOLATION REGISTRY
↓
PROPOSE MIGRATION
```

No rename should be automatically executed merely because it violates a preferred naming style.

---

# 123. RSCF Node

```yaml
node_id: AMOS_OS_NAMING_STANDARD

node_type: naming_standard

domain: AMOS_OS

functional_type:
  IDENTITY_GOVERNANCE
  NAMESPACE_GOVERNANCE

lifecycle_stage:
  ACTIVE_STANDARD

origin_architect:
  Trang Phan

claim_class:
  AMOS_MODEL

claim: >
  AMOS OS naming should preserve stable semantic and provenance identity
  while using deterministic namespace conventions for folders, files,
  registries, components, modes, schemas, and versions.

premises:
  - filesystem paths can change independently of semantic identity
  - versions require explicit metadata
  - historical identity must remain recoverable
  - rename operations can break dependencies and provenance
  - machine-readable conventions improve deterministic governance

dependencies:
  - "ARCHITECTURE"
  - "FULL_TREE"
  - "PLACEMENT_RULES"
  - "DEPENDENCY_MAP"
  - "AUTHORITATIVE_STATE"

invariants:
  - Filename != ArtifactID
  - Path != SemanticIdentity
  - Rename != Reclassification
  - MissingVersion != HistoricalV0
  - Collision != PASS
  - SourceNameMustRemainRecoverable

does_not_establish:
  - full repository compliance
  - historical correctness of existing version labels
  - semantic equivalence of renamed legacy artifacts

falsifiers:
  - authoritative architecture adopts an incompatible namespace contract
  - runtime requires materially different naming semantics
  - canonical registry defines superseding identity rules

confidence_ceiling:
  naming_architecture: high
  repository_compliance: unknown
  historical_version_accuracy: source_dependent
```

---

# 124. Changelog

## v2.0.0 — 2026-08-25

Major expansion from placeholder into governed naming standard.

Added:

* explicit document, naming-standard, and namespace-contract versions;
* full naming taxonomy;
* identity firewall;
* folder conventions;
* root ordinal rules;
* root Markdown conventions;
* reserved suffix semantics;
* kernel naming;
* agent naming;
* skill naming;
* workflow naming;
* protocol naming;
* mode-family naming;
* model naming;
* schema naming;
* registry naming;
* artifact ID convention;
* semantic/display identity separation;
* independent version axes;
* semantic versioning;
* AMOS_CORE target semantics;
* historical-version firewall;
* filename-version rules;
* canonical pointer pattern;
* prohibited decorative versions;
* source identity preservation;
* rename classification;
* alias and deprecation rules;
* collision governance;
* case-fold and Unicode considerations;
* Python, TypeScript, JSON, Markdown naming guidance;
* RSCF naming;
* runtime-instance identity;
* lifecycle/epistemic naming;
* timestamp/hash/provenance naming;
* canon naming restrictions;
* placeholder naming;
* archive/backup/migration conventions;
* test and error-code naming;
* rename validation pipeline;
* naming authority;
* legacy compatibility;
* naming migration lifecycle;
* recovery semantics;
* 20 naming validation tests;
* naming failure registry;
* 25 hard naming invariants;
* compliance audit;
* RSCF node.

## v1.0.0 — 2026-08-25

Initial placeholder defined:

```text
NN_SECTION
UPPER_SNAKE_CASE.md
K_*
A_*
S_*
*_MAP.md
*_REGISTRY.md
*_LEDGER.md
```

and the initial identity/version firewall.

---

# 125. Final Naming Law

The naming standard compresses to:

```text
IDENTITY FIRST
↓
NAME SECOND
↓
PATH THIRD
↓
VERSION EXPLICIT
↓
PROVENANCE PRESERVED
↓
RENAMES GOVERNED
```

The primary invariant is:

> **An AMOS artifact remains the same artifact because its semantic identity and provenance remain continuous—not merely because its filename remains unchanged.**

The second invariant is:

> **A filename is a locator and representation, not the ultimate identity of an AMOS object.**

The third invariant is:

> **Missing historical version information remains `UNKNOWN/GAP`; version labels may be assigned prospectively, but must never be retroactively invented as historical fact.**

The fourth invariant is:

> **Naming normalization is permitted only when it preserves semantic distinctions, dependencies, provenance, and recoverability.**

---

**Related:** [[00_ROOT/00-Home]] · MOC · [[00_ROOT/ARCHITECTURE]] · [[FULL_TREE]] · [[SYSTEM_MAP]] · [[AUTHORITATIVE_STATE]] · [[DEPENDENCY_MAP]] · [[PLACEMENT_RULES]] · [[ROADMAP]] · [[00_ROOT/RSCF_NODE_INDEX]]

```text
```

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00_ROOT/00-Home]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: 00_root_naming_standard
node_type: note
path: 00_ROOT/00_ROOT_NAMING_STANDARD.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_ROOT/00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
