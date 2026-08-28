---
title: COGNITIVE MATRIX NAMING STANDARD
type: naming
source: 25_COGNITIVE_MATRIX/00_INDEX
tags:
- cognitive_matrix
- index
- note
- canon/cognitive-matrix
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: index_navigation
---


# 00_INDEX — AMOS Cognitive Matrix Naming Standard

**Origin architect / steward:** Trang Phan
**Architecture:** AMOS OS
**Subsystem:** `25_COGNITIVE_MATRIX`
**Artifact:** `00_INDEX/NAMING_STANDARD.md`
**Class:** `MATRIX_NAMING_AND_IDENTITY_CONTRACT`
**Role:** `IDENTITY / ADDRESSING / DISCOVERY / INTEROPERABILITY / COLLISION_PREVENTION`
**Status:** `ACTIVE STRUCTURAL CONTRACT`
**Epistemic class:** `AMOS_MODEL + SOURCE_CANON_BINDING`

---

# 0. Purpose

`NAMING_STANDARD.md` defines the canonical naming, identifier, path, namespace, alias, reference, and collision-prevention rules for the AMOS Cognitive Matrix.

Its purpose is to ensure that every Matrix object can be:

```text
IDENTIFIED
ADDRESSED
RESOLVED
REFERENCED
VALIDATED
TRACED
DEPENDENCY-MAPPED
ROUTED
INVALIDATED
REPAIRED
```

without depending on ambiguous natural-language names.

The standard governs names for:

```text
Matrix artifacts
primitives
lifecycle operations
control planes
scales
cells
states
variables
operators
invariants
equations
dependencies
bindings
agents
skills
workflows
protocols
gaps
evidence
RSCFs
validators
tests
failures
repairs
provenance objects
authority objects
```

The governing distinction is:

```text
NAME
!=
IDENTITY

IDENTITY
!=
SEMANTICS

SEMANTICS
!=
IMPLEMENTATION

IMPLEMENTATION
!=
VALIDATION

VALIDATION
!=
AUTHORITY
```

A name makes an object addressable.

It does not prove that the object exists operationally, is implemented correctly, has been validated, or possesses authority.

---

# 1. Source and Canon References

Primary AMOS source lineage for this contract includes the AMOS/Trang corpus governed by Trang Phan as origin architect and steward.

Relevant architectural sources include:

```text
AMOS_FULL_BRAIN_OS
AMOS_CORE lineage
AMOS Cognitive Matrix
AMOS Canon
AMOS Infrastructure Control Plane
AMOS Cognitive Organism
AMOS Agent architecture
AMOS Skill architecture
AMOS Workflow architecture
AMOS Protocol architecture
AMOS Memory architecture
AMOS Knowledge architecture
RSCF
H/M/L
GMEF
```

This naming standard is an AMOS structural contract.

It must not be represented as an externally established universal naming standard.

Where source canon explicitly defines an identifier or term:

```text
SOURCE_CANON
>
DERIVED NAMING CONVENTION
```

Where canon is silent:

```text
derived convention
=
AMOS_MODEL
```

and must remain distinguishable from source-defined canon.

---

# 2. Scope

This contract governs:

```text
25_COGNITIVE_MATRIX/**
```

and any external AMOS object referenced from the Matrix.

It does not independently rename authoritative objects belonging to another AMOS subsystem.

For external objects:

```text
PRESERVE EXTERNAL CANONICAL ID
```

and create a Matrix binding/reference instead.

Example:

```text
AMOS_OS_KERNEL
```

must not be silently renamed:

```text
MATRIX_KERNEL
```

merely because the Matrix references it.

---

# 3. Naming Architecture

AMOS Matrix naming has six distinct layers:

```text
LAYER 1 — HUMAN LABEL

LAYER 2 — CANONICAL SYMBOL

LAYER 3 — CANONICAL IDENTIFIER

LAYER 4 — CANONICAL PATH

LAYER 5 — MACHINE REFERENCE

LAYER 6 — SEMANTIC ORIGIN
```

Example:

```yaml
human_label: World Modeling

symbol: L10

canonical_id: L10_WORLD_MODELING

canonical_path:
  01_PRIMITIVES/L10_WORLD_MODELING/

machine_reference:
  matrix://primitive/L10

semantic_origin:
  AMOS_COGNITIVE_MATRIX
```

These layers must not be silently collapsed.

---

# 4. Canonical Character Set

Canonical filesystem identifiers use:

```text
A-Z
0-9
_
-
.
```

with additional syntax permitted only where explicitly defined.

Default canonical component names use:

```text
UPPER_SNAKE_CASE
```

Examples:

```text
WORLD_MODELING

DEPENDENCY_GRAPH

CELL_CONTRACT

STRUCTURAL_GAP

COMMIT_AUTHORITY
```

Human-facing prose may use natural capitalization.

---

# 5. Forbidden Canonical Naming Patterns

Avoid canonical identifiers containing:

```text
spaces

uncontrolled punctuation

emoji

ambiguous Unicode lookalikes

unstable timestamps

random prose

unscoped abbreviations

personal shorthand

meaningless sequential numbers

temporary conversational references
```

Examples of invalid canonical names:

```text
world model thing

Final Final Matrix

new-cell-2

JohnsFix

thing_that_works

prediction???

Matrix 👍

latest_good_version
```

---

# 6. Case Rule

Canonical IDs:

```text
UPPER_SNAKE_CASE
```

Canonical Markdown filenames:

```text
UPPER_SNAKE_CASE.md
```

Canonical JSON filenames:

```text
UPPER_SNAKE_CASE.json
```

Canonical Python executable files:

```text
lower_snake_case.py
```

Examples:

```text
MATRIX_CONTRACT.md

PRIMITIVE_REGISTRY.md

AMOS_COGNITIVE_CELL_REGISTRY.json

build_amos_cognitive_cells.py
```

---

# 7. Directory Naming Rule

Architecture directories use:

```text
NN_NAME
```

where:

```text
NN
=
ordering/address prefix

NAME
=
canonical semantic label
```

Examples:

```text
00_INDEX

01_PRIMITIVES

02_LIFECYCLE_OPERATIONS

03_CONTROL_PLANES

04_SCALES

05_CELL_REGISTRY

06_CELL_CONTRACTS

07_COVERAGE

08_STRUCTURAL_GAPS

09_DEPENDENCY_GRAPH

10_ROUTING

11_VALIDATION

12_GENERATORS
```

Ordering numbers provide deterministic navigation.

They do not establish semantic priority unless explicitly declared.

---

# 8. Root Namespace

Canonical Matrix namespace:

```text
AMOS_COGNITIVE_MATRIX
```

Short contextual namespace:

```text
MATRIX
```

URI-style machine namespace:

```text
matrix://
```

The short form may be used only where Matrix context is already established.

---

# 9. Primitive Identifier Standard

Primitive symbols:

```text
L00
...
L29
```

Canonical primitive identifier:

```text
L{NN}_{PRIMITIVE_NAME}
```

Examples:

```text
L00_REALITY_ENVIRONMENT
L01_SENSING_OBSERVATION
L02_ATTENTION
L07_MEMORY
L10_WORLD_MODELING
L13_PREDICTION
L17_DECISION
L18_ACTION
L23_METACOGNITION
L28_GOVERNANCE
L29_EVOLUTION
```

Machine reference:

```text
matrix://primitive/L10
```

or:

```text
matrix://primitive/L10_WORLD_MODELING
```

---

# 10. Primitive Naming Invariant

Each primitive must have exactly one canonical identifier within a Matrix namespace.

Formally:

[
P_i \neq P_j
\Rightarrow
ID(P_i) \neq ID(P_j)
]

Canonical-name uniqueness is mandatory.

Semantic similarity does not permit identifier collision.

---

# 11. Lifecycle Operation Identifier Standard

Lifecycle operation symbols:

```text
O00
...
O16
```

Canonical identifier:

```text
O{NN}_{OPERATION_NAME}
```

Examples:

```text
O00_DISTINCTION
O01_OBJECT
O02_RELATION
O03_BINDING
O04_STATE
O05_MEMORY
O06_MODEL
O07_INFERENCE
O08_PREDICTION
O09_SIMULATION
O10_VALUE
O11_GOAL
O12_PLAN
O13_DECISION
O14_ACTION
O15_OBSERVATION
O16_LEARNING
```

Machine reference:

```text
matrix://operation/O08
```

---

# 12. Control-Plane Identifier Standard

Matrix cognitive control-plane symbols:

```text
C01
...
C09
```

Canonical identifiers:

```text
C01_GOVERNANCE
C02_METACOGNITIVE
C03_EXECUTIVE
C04_REASONING
C05_REPRESENTATION
C06_MEMORY
C07_PERCEPTION
C08_EXECUTION
C09_KERNEL_CONTROL
```

Machine reference:

```text
matrix://control-plane/C04
```

---

# 13. Control-Plane Namespace Firewall

Matrix control planes must not be confused with the AMOS Infrastructure Control Plane.

Therefore:

```text
MATRIX:C01_GOVERNANCE
```

is distinct from:

```text
AMOS_INFRASTRUCTURE_CONTROL_PLANE
```

Likewise:

```text
MATRIX:C09_KERNEL_CONTROL
```

does not automatically mean:

```text
AMOS_OS_KERNEL
```

Names must preserve architectural layer.

---

# 14. Scale Identifier Standard

Canonical scale symbols:

```text
H
M
L
```

Canonical names:

```text
H_HIGH_SCALE
M_MID_SCALE
L_LOW_SCALE
```

Machine references:

```text
matrix://scale/H
matrix://scale/M
matrix://scale/L
```

---

# 15. H/M/L Naming Semantics

Default Matrix interpretation:

```text
H
=
high/system/governing/long-horizon

M
=
mid/subsystem/workflow/intermediate

L
=
low/local/atomic/immediate
```

A domain-specific H/M/L interpretation must declare its translation.

Do not assume that identical H/M/L symbols across domains imply identical semantic scales.

---

# 16. Cell Identifier Standard

Canonical cell identity is derived from:

[
Cell = P \times O \times C \times S
]

Canonical CellID:

```text
CELL_{P}_{O}_{C}_{S}
```

Example:

```text
CELL_L10_O08_C04_H
```

meaning:

```text
Primitive:
L10_WORLD_MODELING

Lifecycle operation:
O08_PREDICTION

Control plane:
C04_REASONING

Scale:
H_HIGH_SCALE
```

---

# 17. CellID Determinism

For a coordinate:

[
(P,O,C,S)
]

the identifier function must satisfy:

[
ID(P,O,C,S)
===========

CELL_P_O_C_S
]

and:

[
(P_1,O_1,C_1,S_1)
=================

(P_2,O_2,C_2,S_2)
\Rightarrow
ID_1=ID_2
]

Likewise:

[
ID_1=ID_2
\Rightarrow
Coordinate_1=Coordinate_2
]

within the same Matrix namespace.

---

# 18. CellID Examples

```text
CELL_L02_O15_C07_L
```

Attention × Observation × Perception × Low scale.

```text
CELL_L07_O05_C06_M
```

Memory × Memory × Memory Control × Mid scale.

```text
CELL_L13_O08_C04_H
```

Prediction × Prediction × Reasoning × High scale.

```text
CELL_L18_O14_C08_L
```

Action × Action × Execution × Low scale.

```text
CELL_L28_O13_C01_H
```

Governance × Decision × Governance Control × High scale.

---

# 19. Cell Machine Reference

Canonical machine URI:

```text
matrix://cell/CELL_L10_O08_C04_H
```

Compact machine reference may be:

```text
matrix://cell/L10/O08/C04/H
```

The canonical registry must resolve both to the same CellID.

---

# 20. Matrix Object Identifier Grammar

General grammar:

```text
{OBJECT_CLASS}_{SEMANTIC_ID}
```

Examples:

```text
CELL_L10_O08_C04_H

GAP_L10_O08_C04_H_001

TEST_CELL_L10_O08_C04_H_001

VAL_CELL_L10_O08_C04_H_001

DEP_CELL_L10_O08_C04_H_001

BIND_CELL_L10_O08_C04_H_001
```

---

# 21. State Identifier Standard

State identifiers use:

```text
STATE_{SCOPE}_{NAME}
```

Examples:

```text
STATE_MATRIX_ACTIVE

STATE_CELL_VALIDATION

STATE_MEMORY_RETRIEVAL

STATE_ROUTER_SELECTION
```

For cell-specific state:

```text
STATE_{CELLID}_{NAME}
```

Example:

```text
STATE_CELL_L13_O08_C04_H_FORECAST_CONTEXT
```

---

# 22. Variable Identifier Standard

Variables should be semantically explicit.

Preferred:

```text
{scope}_{quantity}
```

Examples:

```text
cell_status

binding_confidence

evidence_count

dependency_depth

authority_freshness

validation_level
```

Formal mathematical symbols may be shorter:

```text
P
O
C
S
X
E
D
```

but every symbol must have a typed definition.

---

# 23. Variable Qualification

If a symbol is overloaded across documents, qualify it.

Example:

```text
C_matrix
```

versus:

```text
C_confidence
```

Do not permit silent symbol collision.

---

# 24. Operator Identifier Standard

Operators use verb-oriented identifiers:

```text
OP_{VERB}_{OBJECT}
```

Examples:

```text
OP_RESOLVE_CELL

OP_VALIDATE_BINDING

OP_INVALIDATE_DEPENDENCY

OP_PROMOTE_GAP

OP_ROUTE_CAPABILITY

OP_CHECK_AUTHORITY

OP_COMMIT_EFFECT
```

Operators must describe transformations rather than vague concepts.

---

# 25. Invariant Identifier Standard

Canonical invariant identifiers:

```text
INV_{DOMAIN}_{NNN}
```

Examples:

```text
INV_NAMING_001

INV_CELL_004

INV_DEPENDENCY_007

INV_AUTHORITY_003
```

Each invariant should additionally carry a human-readable name.

Example:

```yaml
id: INV_NAMING_001
name: CANONICAL_ID_UNIQUENESS
```

---

# 26. Equation Identifier Standard

Equation identifiers:

```text
EQ_{DOMAIN}_{NNN}
```

Example:

```text
EQ_MATRIX_001
```

Human label:

```text
CELL_CARDINALITY
```

Example:

[
N_{cells}
=========

N_P N_O N_C N_S
]

Every equation must identify whether it is:

```text
SOURCE_EQUATION
DERIVED_EQUATION
AMOS_MODEL
EMPIRICAL
EXTERNAL_THEOREM
IMPLEMENTATION_FORMULA
```

---

# 27. Dependency Identifier Standard

Dependency objects:

```text
DEP_{SOURCE}_{TARGET}_{NNN}
```

or, where excessively long:

```text
DEP_{SCOPE}_{NNN}
```

with source/target stored as typed fields.

Preferred machine representation:

```yaml
dependency_id: DEP_CELL_000123
source: CELL_L13_O08_C04_H
target: CELL_L10_O06_C04_H
type: REQUIRES
```

Avoid encoding every semantic property into filenames.

---

# 28. Dependency Edge Type Names

Canonical dependency relation vocabulary:

```text
REQUIRES

PRODUCES

TRANSFORMS

VALIDATES

GOVERNS

OBSERVES

AUTHORIZES

INVALIDATES

RECOVERS

SUPERSEDES
```

Relations should remain uppercase machine tokens.

---

# 29. Binding Identifier Standard

Binding IDs:

```text
BIND_{TARGET_CLASS}_{NNN}
```

Examples:

```text
BIND_CELL_000001

BIND_PRIMITIVE_000042

BIND_WORKFLOW_000008
```

Binding records contain:

```yaml
binding_id:
target:
binding_type:
bound_object:
status:
evidence:
validation:
```

---

# 30. Binding Type Vocabulary

Canonical binding types include:

```text
KERNEL

AGENT

SKILL

WORKFLOW

PROTOCOL

MEMORY

KNOWLEDGE

MODEL

TOOL

VALIDATOR

STATE

RUNTIME
```

---

# 31. Agent Identifier Standard

Matrix references to AMOS agents use:

```text
AGENT_{ROLE_NAME}
```

Examples:

```text
AGENT_PLANNER

AGENT_ANALYST

AGENT_AUDITOR

AGENT_RESEARCHER

AGENT_SIMULATOR

AGENT_CRITIC
```

If an agent already has a canonical external AMOS identifier, preserve that identifier instead of creating a competing Matrix identity.

---

# 32. Agent Instance Identifier

Where runtime instances must be distinguished:

```text
AGENT_INSTANCE_{CANONICAL_AGENT_ID}_{INSTANCE_ID}
```

Instance identity must not be confused with role identity.

```text
AGENT_PLANNER
!=
AGENT_INSTANCE_PLANNER_X
```

---

# 33. Skill Identifier Standard

Canonical Skill reference:

```text
SKILL_{CANONICAL_SKILL_NAME}
```

Example conceptual form:

```text
SKILL_AMOS_CLAIM_VERIFIER
```

When referencing an installed Skill whose canonical slug already exists, preserve that slug in metadata.

Example:

```yaml
skill_id: SKILL_AMOS_CLAIM_VERIFIER
canonical_slug: amos-claim-verifier
```

---

# 34. Skill Boundary

```text
SKILL_NAME
!=
SKILL_CAPABILITY_PROOF
```

A Skill appearing in a binding registry does not prove that it:

```text
exists in every runtime
is enabled
has required tools
is validated
has authority
```

---

# 35. Workflow Identifier Standard

Workflow IDs:

```text
WF_{WORKFLOW_NAME}
```

Examples:

```text
WF_CELL_RESOLUTION

WF_MATRIX_VALIDATION

WF_GAP_REPAIR

WF_DEPENDENCY_INVALIDATION

WF_GOVERNED_ACTION
```

Workflow instance:

```text
WF_INSTANCE_{WORKFLOW_ID}_{INSTANCE_ID}
```

---

# 36. Protocol Identifier Standard

Protocol IDs:

```text
PROTO_{PROTOCOL_NAME}
```

Examples:

```text
PROTO_AGENT_HANDOFF

PROTO_CELL_BINDING

PROTO_EVIDENCE_TRANSFER

PROTO_AUTHORITY_REQUEST

PROTO_COMMIT_FINALIZATION
```

---

# 37. Kernel Identifier Standard

Kernel references:

```text
KERNEL_{KERNEL_NAME}
```

Examples:

```text
KERNEL_LOGIC

KERNEL_CONSTRAINT

KERNEL_PROVENANCE

KERNEL_AUTHORITY
```

If canonical AMOS Kernel naming differs, external canonical identity prevails.

---

# 38. Memory Identifier Standard

Memory architecture object:

```text
MEM_{MEMORY_NAME}
```

Examples:

```text
MEM_WORKING_STATE

MEM_EPISODIC

MEM_SEMANTIC

MEM_PROVENANCE

MEM_NEGATIVE
```

Memory instance:

```text
MEM_INSTANCE_{MEMORY_CLASS}_{ID}
```

---

# 39. Knowledge Identifier Standard

Knowledge object:

```text
KNOW_{DOMAIN}_{ID}
```

Examples:

```text
KNOW_MATRIX_001

KNOW_CANON_004

KNOW_FOREX_102
```

Knowledge claims should additionally carry epistemic class.

---

# 40. Evidence Identifier Standard

Evidence IDs:

```text
EVID_{SOURCE_CLASS}_{NNN}
```

Examples:

```text
EVID_SOURCE_001

EVID_TEST_004

EVID_RUNTIME_019

EVID_EXTERNAL_005
```

Evidence identity must preserve source lineage.

---

# 41. Provenance Identifier Standard

Provenance objects:

```text
PROV_{SOURCE_FAMILY}_{NNN}
```

Example:

```text
PROV_AMOS_CANON_001
```

A transformed copy receives a distinct artifact identity while preserving ancestry.

Example:

```yaml
artifact_id: EVID_DERIVED_014
origin_provenance: PROV_AMOS_CANON_001
```

---

# 42. RSCF Identifier Standard

RSCF capsules:

```text
RSCF_{SCOPE}_{NNN}
```

Examples:

```text
RSCF_CELL_000001

RSCF_PRIMITIVE_000013

RSCF_NAMING_001
```

Where useful:

```text
RSCF_{OBJECT_ID}
```

Example:

```text
RSCF_CELL_L13_O08_C04_H
```

---

# 43. Gap Identifier Standard

Gap IDs:

```text
GAP_{SCOPE}_{NNN}
```

Examples:

```text
GAP_MATRIX_001

GAP_L13_003

GAP_CELL_L13_O08_C04_H_001
```

Gap ID remains stable through its lifecycle.

Do not rename a gap to imply resolution.

Instead change:

```text
gap_status
```

---

# 44. Gap Status Vocabulary

```text
DETECTED

CLASSIFIED

MAPPED

RESEARCHING

DESIGNED

IMPLEMENTED

VALIDATING

CLOSED_FOR_SCOPE

REOPENED

QUARANTINED
```

---

# 45. Failure Identifier Standard

Failure classes:

```text
FAIL_{DOMAIN}_{NAME}
```

Examples:

```text
FAIL_NAMING_COLLISION

FAIL_ORPHAN_CELL

FAIL_BROKEN_BINDING

FAIL_STALE_AUTHORITY

FAIL_PROVENANCE_AMBIGUITY
```

Failure instances:

```text
FAIL_INSTANCE_{FAILURE_CLASS}_{ID}
```

---

# 46. Repair Identifier Standard

Repair definitions:

```text
REPAIR_{DOMAIN}_{NAME}
```

Examples:

```text
REPAIR_NAMING_COLLISION

REPAIR_BROKEN_PATH

REPAIR_STALE_BINDING

REPAIR_DEPENDENCY_GRAPH
```

Repair execution instances must be distinguishable from repair definitions.

---

# 47. Test Identifier Standard

Tests:

```text
TEST_{DOMAIN}_{NNN}
```

Examples:

```text
TEST_NAMING_001

TEST_CELL_004

TEST_ROUTING_007
```

Optional semantic label:

```yaml
test_id: TEST_NAMING_001
name: CANONICAL_ID_UNIQUENESS
```

---

# 48. Validator Identifier Standard

Validators:

```text
VALIDATOR_{DOMAIN}_{NAME}
```

Examples:

```text
VALIDATOR_NAMING_SCHEMA

VALIDATOR_CELL_REGISTRY

VALIDATOR_DEPENDENCY_GRAPH

VALIDATOR_BINDING_COMPATIBILITY
```

Validation result:

```text
VAL_{TARGET}_{NNN}
```

---

# 49. Authority Identifier Standard

Authority objects must remain distinct from capability objects.

Authority ID:

```text
AUTH_{SCOPE}_{NNN}
```

Authority witness:

```text
AUTH_WITNESS_{SCOPE}_{NNN}
```

Example:

```text
AUTH_WITNESS_TOOL_WRITE_001
```

Never encode authority merely by naming something:

```text
AUTHORIZED_AGENT
```

unless an actual authority record exists.

---

# 50. Proposal Identifier Standard

Proposal:

```text
PROP_{DOMAIN}_{NNN}
```

Commit:

```text
COMMIT_{DOMAIN}_{NNN}
```

These identities must remain separate.

```text
PROP_X
!=
COMMIT_X
```

---

# 51. Canon Identifier Standard

Source canon objects should preserve source-defined names wherever available.

Matrix-local references may use:

```text
CANON_REF_{NNN}
```

but the reference must contain the original canonical identity.

Example:

```yaml
canon_ref: CANON_REF_001
source_id: AMOS_CORE
source_object: ...
```

---

# 52. Alias Standard

Aliases are discovery aids.

They are not canonical identifiers.

Alias record:

```yaml
alias: forecasting
canonical_target: L13_PREDICTION
status: ACTIVE
```

Aliases may be:

```text
natural-language synonyms
historical names
abbreviations
legacy identifiers
domain-specific terminology
```

---

# 53. Alias Resolution Invariant

Every active alias must resolve to:

```text
exactly one canonical target
```

unless explicitly classified:

```text
AMBIGUOUS_ALIAS
```

If ambiguous:

```text
DO NOT AUTO-RESOLVE
```

---

# 54. Synonym Boundary

Example:

```text
forecast
forecasting
prediction
predictive reasoning
```

may all point toward prediction-related objects.

They must not automatically collapse:

```text
L13_PREDICTION
O08_PREDICTION
predictive model
prediction workflow
```

into one identity.

---

# 55. Semantic-Origin Requirement

Every important canonical object should be capable of declaring:

```yaml
semantic_origin:
  architecture:
  subsystem:
  source:
  scope:
```

Example:

```yaml
semantic_origin:
  architecture: AMOS_OS
  subsystem: COGNITIVE_MATRIX
  source: PRIMITIVE_REGISTRY
  scope: MATRIX
```

---

# 56. Cross-Architecture Names

When two AMOS architectures contain similarly named objects:

```text
QUALIFY THE NAMESPACE
```

Example:

```text
MATRIX:C01_GOVERNANCE

INFRA:GOVERNANCE

CANON:GOVERNANCE

AGENT:GOVERNANCE
```

Never infer equivalence from lexical similarity.

---

# 57. Fully Qualified Identifier

Where collision risk exists, use:

```text
{ARCHITECTURE}:{SUBSYSTEM}:{OBJECT_CLASS}:{OBJECT_ID}
```

Example:

```text
AMOS:MATRIX:PRIMITIVE:L13
```

or:

```text
AMOS:MATRIX:CELL:CELL_L13_O08_C04_H
```

---

# 58. Machine URI Standard

Preferred conceptual URI grammar:

```text
amos://{subsystem}/{object-class}/{object-id}
```

Examples:

```text
amos://matrix/primitive/L13

amos://matrix/cell/CELL_L13_O08_C04_H

amos://matrix/gap/GAP_MATRIX_001

amos://agent/AGENT_PLANNER

amos://skill/amos-claim-verifier
```

These URIs are architectural identifiers.

They do not imply a network-accessible protocol unless implemented.

---

# 59. Filesystem Path Standard

Paths should encode architectural containment, not epistemic claims.

Example:

```text
25_COGNITIVE_MATRIX/
01_PRIMITIVES/
L13_PREDICTION/
INVARIANTS.md
```

Do not create paths such as:

```text
VALIDATED/
```

merely because a file currently has validation evidence unless that directory is explicitly a status registry.

---

# 60. Filename Standard

General Markdown filenames describe artifact function:

```text
README.md

DEFINITION.md

PURPOSE.md

STATE.md

VARIABLES.md

OPERATORS.md

INVARIANTS.md

EQUATIONS.md

MEMORY.md

CONTROL_PLANES.md

HML.md

AGENTS.md

SKILLS.md

WORKFLOWS.md

PROTOCOLS.md

DEPENDENCIES.md

FAILURE_MODES.md

REPAIR.md

TESTS.md

RSCF.md

GAP_MATRIX.md

PROVENANCE.md
```

Use consistent names across primitive packages.

---

# 61. Filename Semantics

Do not create:

```text
INFO.md

NOTES.md

MISC.md

OTHER.md

STUFF.md
```

for canonical architecture content.

Artifact names should reveal contract type.

---

# 62. [[README]] Boundary

`README.md` is orientation.

It is not automatically canonical authority.

Where a specialized contract exists:

```text
SPECIALIZED_CONTRACT
>
README DESCRIPTION
```

for that contract's domain.

---

# 63. Index Naming

Index files use explicit semantic names:

```text
MOC.md

CELL_INDEX.md

GAP_REGISTRY.md

STATUS_LEGEND.md
```

Avoid generic:

```text
INDEX2.md

MASTER_INDEX_NEW.md
```

---

# 64. Registry Naming

Canonical registries use:

```text
{DOMAIN}_REGISTRY
```

Examples:

```text
PRIMITIVE_REGISTRY

CONTROL_PLANE_REGISTRY

CELL_REGISTRY

GAP_REGISTRY

BINDING_REGISTRY
```

Registry identity must be singular within its authority scope.

---

# 65. Contract Naming

Contracts use:

```text
{DOMAIN}_CONTRACT
```

Examples:

```text
MATRIX_CONTRACT

CELL_CONTRACT

GENERATOR_CONTRACT

AUTHORITY_CONTRACT
```

---

# 66. Policy Naming

Policies use:

```text
{DOMAIN}_POLICY
```

Examples:

```text
ROUTING_POLICY

RETENTION_POLICY

PROMOTION_POLICY

INVALIDATION_POLICY
```

---

# 67. Protocol Naming

Protocols describe component interaction.

Policies describe governing constraints.

Contracts define structural obligations.

Therefore:

```text
PROTOCOL
!=
POLICY

POLICY
!=
CONTRACT
```

Naming must preserve this distinction.

---

# 68. Status Naming

Status values must describe one dimension only.

Bad:

```text
COMPLETE
```

Preferred:

```text
STRUCTURALLY_COMPLETE

IMPLEMENTED

UNIT_TESTED

AUTHORIZED
```

These answer different questions.

---

# 69. Status Dimensions

Canonical status dimensions should include:

```text
definition_status

structural_status

implementation_status

validation_status

operational_status

governance_status

freshness_status

gap_status
```

---

# 70. Placeholder Naming

Placeholder files may retain canonical final filenames.

Their internal status must state:

```text
PLACEHOLDER
```

Example:

```text
INVARIANTS.md
```

may exist while:

```yaml
artifact_status: PROPOSED_SPECIFICATION
```

This is preferable to:

```text
INVARIANTS_PLACEHOLDER.md
```

if the placeholder is intended to become the canonical artifact.

---

# 71. Placeholder Boundary

```text
CANONICAL_FILENAME
+
PLACEHOLDER_CONTENT
```

does not imply:

```text
CANONICAL_COMPLETION
```

Status lives in metadata, not filename inference.

---

# 72. Temporary Artifact Naming

Temporary working artifacts must be visibly noncanonical.

Recommended prefix:

```text
_TMP_
```

Examples:

```text
_TMP_CELL_AUDIT.md

_TMP_BINDING_ANALYSIS.json
```

Temporary artifacts must not be referenced as durable canonical dependencies.

---

# 73. Draft Artifact Naming

Where explicit drafts are required:

```text
_DRAFT_
```

may be used outside canonical artifact paths.

Example:

```text
_DRAFT_MATRIX_EXTENSION.md
```

Once promoted, create/update the canonical artifact rather than treating the draft name as canonical.

---

# 74. Archive Naming

Historical artifacts should use an explicit archival namespace rather than ambiguous suffixes.

Preferred:

```text
ARCHIVE/
```

Avoid:

```text
FINAL

FINAL2

FINAL_REAL

LATEST

OLD

OLD2
```

The architecture requested here does not depend on filename version numbering as the primary identity mechanism.

Lineage belongs in provenance metadata and repository/Drive history.

---

# 75. No Filename Versioning Rule

Canonical architecture filenames remain stable.

Prefer:

```text
MATRIX_CONTRACT.md
```

not:

```text
MATRIX_CONTRACT_V1.md
MATRIX_CONTRACT_V2.md
MATRIX_CONTRACT_FINAL.md
```

Changes should preserve:

```text
artifact identity
provenance
revision lineage
dependency impact
```

through the storage/version-control layer.

---

# 76. Collision Types

Naming collision classes:

```text
EXACT_ID_COLLISION

SEMANTIC_COLLISION

ALIAS_COLLISION

NAMESPACE_COLLISION

PATH_COLLISION

SYMBOL_COLLISION

ABBREVIATION_COLLISION

LEGACY_COLLISION

CROSS_ARCHITECTURE_COLLISION
```

---

# 77. Exact Collision

Example:

```text
L13_PREDICTION
```

assigned to two different primitive definitions.

This is invalid.

---

# 78. Semantic Collision

Two different IDs may still accidentally define the same concept.

Example:

```text
L13_PREDICTION

L30_FORECASTING
```

If they have the same intended semantics, ontology duplication may exist.

Do not accept merely because identifiers differ.

---

# 79. Legitimate Lexical Duplication

Lexically identical concepts may legitimately appear on different axes.

Example:

```text
L13_PREDICTION

O08_PREDICTION
```

This is not automatically a collision.

Their typed roles differ.

---

# 80. Namespace Collision

Example:

```text
C01_GOVERNANCE
```

versus:

```text
AMOS_INFRASTRUCTURE_GOVERNANCE
```

The same word does not establish the same object.

Namespace qualification resolves this.

---

# 81. Symbol Collision

Single-letter mathematical symbols require local definitions.

Example:

```text
C
```

could mean:

```text
ControlPlane
Confidence
Constraint
Context
```

Formal documents must type the symbol.

---

# 82. Naming Resolution Operator

Define:

[
ResolveName(x, context)
\rightarrow
CanonicalObject \cup Ambiguous \cup Unknown
]

The resolver must not force a match.

Valid outcomes:

```text
RESOLVED

AMBIGUOUS

UNKNOWN
```

---

# 83. Canonicalization Operator

[
Canonicalize(alias)
\rightarrow
canonical_id
]

only if:

```text
alias mapping exists
+
mapping is unambiguous
+
mapping is active
+
scope matches
```

Otherwise:

```text
UNKNOWN/GAP
```

or:

```text
AMBIGUOUS
```

---

# 84. Qualification Operator

[
Qualify(ID, namespace)
\rightarrow
FQID
]

Example:

```text
L13
```

becomes:

```text
AMOS:MATRIX:PRIMITIVE:L13
```

when cross-system ambiguity exists.

---

# 85. Parse CellID Operator

[
ParseCellID(ID)
\rightarrow
(P,O,C,S)
]

Example:

```text
CELL_L13_O08_C04_H
```

returns:

```yaml
primitive: L13
operation: O08
control_plane: C04
scale: H
```

Malformed IDs must fail closed.

---

# 86. Construct CellID Operator

[
ConstructCellID(P,O,C,S)
\rightarrow
CELL_P_O_C_S
]

only if all axis members exist in authoritative registries.

Thus:

```text
VALID SYNTAX
!=
VALID CELL
```

---

# 87. Typed Inputs

Naming operations accept typed inputs such as:

```yaml
NamingInput:
  object_class:
  proposed_name:
  namespace:
  scope:
  semantic_definition:
  source_origin:
  parent:
  aliases:
  requested_path:
```

---

# 88. Typed Outputs

```yaml
NamingResult:
  canonical_id:
  canonical_name:
  fully_qualified_id:
  canonical_path:
  machine_reference:
  aliases:
  collision_status:
  provenance:
  validation_status:
  gap_status:
```

---

# 89. Naming State Variables

Relevant state includes:

```text
canonical_registry

namespace_registry

alias_registry

path_registry

collision_registry

deprecated_name_registry

provenance_registry

dependency_graph

validation_state
```

---

# 90. Naming State Transition

A proposed name progresses:

```text
PROPOSED
 ↓
PARSED
 ↓
NORMALIZED
 ↓
COLLISION_CHECKED
 ↓
SEMANTICALLY_CHECKED
 ↓
REGISTERED
 ↓
ACTIVE
```

If conflict exists:

```text
COLLISION_CHECKED
 ↓
QUARANTINED
```

---

# 91. Naming Registration Preconditions

Before registration:

```text
object class known

namespace known

semantic definition exists

canonical pattern valid

exact collision absent

semantic collision assessed

parent scope valid

provenance present
```

---

# 92. Naming Registration Postconditions

After registration:

```text
canonical ID unique

registry updated

path resolvable

aliases mapped

provenance attached

dependency references valid
```

---

# 93. Naming Invariants

```text
INV_NAMING_001
CANONICAL_ID_UNIQUENESS

INV_NAMING_002
ONE_OBJECT_ONE_CANONICAL_ID_PER_NAMESPACE

INV_NAMING_003
ALIASES_DO_NOT_CREATE_IDENTITY

INV_NAMING_004
PATH_DOES_NOT_CREATE_AUTHORITY

INV_NAMING_005
NAME_DOES_NOT_CREATE_IMPLEMENTATION

INV_NAMING_006
ADDRESSABILITY_DOES_NOT_CREATE_VALIDATION

INV_NAMING_007
CAPABILITY_NAME_DOES_NOT_CREATE_AUTHORITY

INV_NAMING_008
PROPOSAL_NAME_DOES_NOT_CREATE_COMMIT

INV_NAMING_009
UNKNOWN_DOES_NOT_AUTO_RESOLVE

INV_NAMING_010
CROSS_ARCHITECTURE_NAMES_REQUIRE_NAMESPACE_SAFETY

INV_NAMING_011
CANONICAL_CELL_IDS_ARE_DETERMINISTIC

INV_NAMING_012
SOURCE_DEFINED_NAMES_PRESERVE_LINEAGE

INV_NAMING_013
RENAMING_REQUIRES_DEPENDENCY_IMPACT_ANALYSIS

INV_NAMING_014
DUPLICATE_SOURCE_COPIES_DO_NOT_CREATE_INDEPENDENT_PROVENANCE

INV_NAMING_015
STATUS_MUST_NOT_BE_INFERRED_FROM NAME
```

---

# 94. Hard Boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

Additional naming boundaries:

```text
NAME != OBJECT

LABEL != SEMANTICS

ALIAS != CANONICAL_ID

PATH != AUTHORITY

REGISTRY_ENTRY != IMPLEMENTATION

REFERENCE != DEPENDENCY_VALIDATION

DUPLICATE_NAME != DUPLICATE_OBJECT

SIMILAR_NAME != SAME_OBJECT

DIFFERENT_NAME != DIFFERENT_OBJECT
```

---

# 95. H/M/L Applicability

Naming operates across all H/M/L scales.

### H — High

Govern:

```text
architecture namespaces
canonical registries
cross-system naming
ontology identity
authority domains
```

### M — Mid

Govern:

```text
subsystems
workflows
agents
skills
protocols
dependency groups
```

### L — Low

Govern:

```text
cells
variables
operators
tests
evidence objects
runtime instances
```

---

# 96. Cross-Scale Naming Rule

Names may be reused across scale only when explicitly qualified.

Example:

```text
STATE_H_SYSTEM_RISK

STATE_M_WORKFLOW_RISK

STATE_L_ACTION_RISK
```

Avoid ambiguous:

```text
STATE_RISK
```

when scale changes semantics.

---

# 97. Control-Plane Requirements

Naming changes may affect:

```text
governance

metacognition

executive routing

reasoning

representation

memory

perception

execution

kernel control
```

The strongest control requirement applies when naming changes alter canonical identity.

---

# 98. Governance Requirement

Canonical rename is not cosmetic when dependencies reference the ID.

Therefore:

```text
RENAME
=
STRUCTURAL CHANGE
```

if the canonical ID changes.

Such changes require impact analysis.

---

# 99. Representation Requirement

The representation layer must preserve:

```text
canonical ID

display label

aliases

namespace

semantic origin
```

as distinct fields.

---

# 100. Memory Requirement

Persistent memory must store canonical identifiers where possible rather than unstable labels.

Preferred:

```yaml
primitive_id: L13
```

rather than:

```yaml
primitive: prediction thing
```

---

# 101. Agent Requirement

Agents interacting with Matrix objects should:

```text
resolve aliases

prefer canonical IDs

preserve namespaces

reject unresolved ambiguity

avoid inventing IDs

report missing registry entries
```

---

# 102. Skill Requirement

Skills that create or modify Matrix artifacts must validate naming against this contract before commit.

Relevant capability classes include:

```text
ontology compilation

registry management

matrix generation

dependency analysis

canon consistency

claim verification

system completion auditing
```

---

# 103. Workflow — New Object Naming

```text
Need new object
 ↓
identify object class
 ↓
identify namespace
 ↓
define semantics
 ↓
search canonical registry
 ↓
search aliases
 ↓
test semantic duplication
 ↓
construct candidate ID
 ↓
validate syntax
 ↓
validate collision
 ↓
attach provenance
 ↓
register
```

---

# 104. Workflow — Rename Existing Object

```text
Rename proposal
 ↓
resolve canonical object
 ↓
determine whether label or ID changes
 ↓
dependency impact analysis
 ↓
alias migration plan
 ↓
path impact analysis
 ↓
validation
 ↓
governance approval if required
 ↓
atomic update
 ↓
post-update validation
```

---

# 105. Label Change vs Identity Change

Changing:

```text
human_label
```

may be cosmetic.

Changing:

```text
canonical_id
```

is structural.

Never treat them equivalently.

---

# 106. Rename Compatibility

Where possible, old canonical identifiers should become explicit legacy aliases after a governed rename.

Example:

```yaml
old_id: L13_FORECAST
new_id: L13_PREDICTION
legacy_resolution: L13_PREDICTION
```

Only do this when semantics are actually preserved.

---

# 107. Semantic Change Boundary

If semantics change materially, do not disguise it as a rename.

```text
SEMANTIC CHANGE
!=
RENAME
```

A new object, supersession relation, or explicit migration may be required.

---

# 108. Protocol — Name Resolution

```text
REQUEST:
  raw_name
  namespace
  expected_object_class
  context

RESPONSE:
  status
  canonical_id
  confidence
  ambiguity
  alternatives
```

Resolution status:

```text
EXACT

ALIAS

CONTEXTUAL

AMBIGUOUS

UNKNOWN
```

---

# 109. Protocol — Canonical Registration

Registration request should contain:

```yaml
object_class:
canonical_name:
namespace:
definition:
scope:
parent:
source:
provenance:
aliases:
dependencies:
```

Registration must fail closed on unresolved identity collision.

---

# 110. Protocol — Cross-System Reference

External reference:

```yaml
external_reference:
  architecture:
  subsystem:
  canonical_id:
  canonical_name:
  source:
  local_binding_id:
```

Do not duplicate the external object's canonical identity into a new Matrix-local object unless the Matrix truly defines a distinct object.

---

# 111. Provenance Requirements

Every canonical naming decision should preserve:

```text
origin

source

semantic ancestry

registration event

rename history

supersession

alias history

scope
```

---

# 112. Provenance Independence

Two names derived from the same source do not constitute independent evidence that the underlying concept is valid.

```text
NAME_A
+
NAME_B
```

with common ancestry remains one provenance family.

---

# 113. Naming Confidence

Naming confidence concerns:

```text
identity resolution
```

not truth of the object's claims.

Example:

```yaml
name_resolution_confidence: 1.0
empirical_validity: UNKNOWN
```

is logically possible.

---

# 114. Confidence Ceiling

Naming confidence is bounded by the weakest load-bearing identity premise.

Conceptually:

[
C_{name}
\le
\min(
C_{namespace},
C_{semantic_definition},
C_{registry},
C_{provenance}
)
]

This is an AMOS MODEL constraint, not an externally established statistical law.

---

# 115. Uncertainty Vector

Naming uncertainty may be represented as:

```yaml
uncertainty:
  semantic:
  namespace:
  provenance:
  alias:
  collision:
  scope:
  freshness:
```

Do not compress materially different uncertainties into one vague score.

---

# 116. Failure Modes

Canonical naming failure modes include:

```text
FAIL_NAMING_COLLISION

FAIL_ALIAS_COLLISION

FAIL_SEMANTIC_DUPLICATION

FAIL_NAMESPACE_LEAKAGE

FAIL_PATH_IDENTITY_CONFUSION

FAIL_STALE_ALIAS

FAIL_ORPHAN_IDENTIFIER

FAIL_BROKEN_REFERENCE

FAIL_SYMBOL_OVERLOAD

FAIL_UNQUALIFIED_CROSS_ARCHITECTURE_NAME

FAIL_RENAME_WITHOUT_MIGRATION

FAIL_SOURCE_NAME_DRIFT

FAIL_STATUS_IN_NAME

FAIL_CANONICAL_ID_MUTATION

FAIL_CASE_DRIFT

FAIL_ILLEGAL_CHARACTER

FAIL_NONDETERMINISTIC_CELL_ID

FAIL_UNREGISTERED_OBJECT
```

---

# 117. Failure — Orphan Identifier

An identifier is orphaned when:

```text
ID exists
```

but no authoritative registry or semantic definition resolves it.

Repair:

```text
locate origin
 ↓
recover semantic definition
 ↓
resolve canonical registry
 ↓
register or quarantine
```

---

# 118. Failure — Semantic Duplication

Two canonical objects may accidentally represent the same concept.

Repair requires:

```text
compare definitions
 ↓
compare scope
 ↓
compare provenance
 ↓
compare dependencies
 ↓
determine SAME / DISTINCT / COMPETING
```

Do not merge based solely on lexical similarity.

---

# 119. Failure — Alias Collision

Example:

```text
"memory"
```

could refer to:

```text
L07_MEMORY

O05_MEMORY

C06_MEMORY

AMOS Memory subsystem
```

Resolution must use object class and namespace.

Without sufficient context:

```text
AMBIGUOUS
```

is the correct result.

---

# 120. Failure — Cross-Layer Leakage

Example:

```text
GOVERNANCE
```

incorrectly resolved to infrastructure authority when the request concerns the cognitive governance primitive.

Repair:

```text
restore namespace
+
object class
+
scope
```

---

# 121. Repair Principle

Naming repair must preserve semantic identity whenever possible.

Do not repair a naming problem by changing the underlying architecture unless the architecture itself is incorrect.

---

# 122. Repair Workflow

```text
detect failure
 ↓
identify affected identifiers
 ↓
resolve semantic origin
 ↓
map dependency fan-out
 ↓
select canonical identity
 ↓
prepare alias/migration mapping
 ↓
apply bounded repair
 ↓
validate references
 ↓
validate dependency graph
 ↓
validate provenance
```

---

# 123. Recovery After Bad Rename

If a rename causes failure:

```text
stop propagation
 ↓
restore last valid canonical mapping
 ↓
preserve attempted rename as provenance
 ↓
repair affected references
 ↓
re-run naming validators
```

---

# 124. Naming Validators

Required validators include:

```text
VALIDATOR_NAMING_SCHEMA

VALIDATOR_CANONICAL_ID_UNIQUENESS

VALIDATOR_ALIAS_RESOLUTION

VALIDATOR_NAMESPACE_COLLISION

VALIDATOR_PATH_CONSISTENCY

VALIDATOR_CELL_ID_DETERMINISM

VALIDATOR_REFERENCE_INTEGRITY

VALIDATOR_PROVENANCE_BINDING

VALIDATOR_LEGACY_ALIAS

VALIDATOR_CROSS_ARCHITECTURE_QUALIFICATION
```

---

# 125. Minimum Naming Tests

```text
TEST_NAMING_001
CANONICAL_IDS_UNIQUE

TEST_NAMING_002
PRIMITIVE_IDS_VALID

TEST_NAMING_003
OPERATION_IDS_VALID

TEST_NAMING_004
CONTROL_PLANE_IDS_VALID

TEST_NAMING_005
SCALE_IDS_VALID

TEST_NAMING_006
CELL_IDS_DETERMINISTIC

TEST_NAMING_007
CELL_IDS_REVERSIBLE

TEST_NAMING_008
ALIASES_RESOLVE

TEST_NAMING_009
AMBIGUOUS_ALIASES_FAIL_CLOSED

TEST_NAMING_010
NO_BROKEN_CANONICAL_REFERENCES

TEST_NAMING_011
NO_DUPLICATE_REGISTRY_IDENTITIES

TEST_NAMING_012
CROSS_ARCHITECTURE_NAMES_QUALIFIED

TEST_NAMING_013
PLACEHOLDER_STATUS_NOT_INFERRED

TEST_NAMING_014
RENAMES_PRESERVE_LINEAGE

TEST_NAMING_015
PROVENANCE_PRESENT
```

---

# 126. CellID Round-Trip Test

For every cell:

```text
coordinate
→ construct CellID
→ parse CellID
→ coordinate
```

must return the original coordinate.

Formally:

[
Parse(Construct(P,O,C,S))
=========================

(P,O,C,S)
]

---

# 127. Cardinality Test

Given:

```text
30 primitives
17 operations
9 control planes
3 scales
```

expected addressable cells:

[
30 \times 17 \times 9 \times 3
==============================

13,770
]

The naming generator must produce:

```text
13,770 unique CellIDs
```

if all combinations are intentionally addressable.

This establishes identifier coverage only.

It does not establish implementation or validation coverage.

---

# 128. Collision Test

For generated set:

[
IDs = {ID_1,\ldots,ID_n}
]

require:

[
|IDs|
=====

|Unique(IDs)|
]

Any violation is:

```text
FAIL_NAMING_COLLISION
```

---

# 129. Reference Integrity Test

Every canonical reference must resolve to:

```text
existing canonical object
```

or explicitly:

```text
UNKNOWN/GAP
```

Dangling references must not silently pass validation.

---

# 130. Alias Integrity Test

Every alias must resolve to:

```text
one canonical target
```

or be explicitly marked:

```text
AMBIGUOUS
```

---

# 131. Falsifiers

This naming contract fails for its declared scope if:

```text
two distinct Matrix objects receive the same canonical ID

one CellID resolves to multiple coordinates

one coordinate produces multiple canonical CellIDs

canonical aliases resolve unpredictably

external AMOS identities are silently overwritten

canonical references cannot be resolved

renaming destroys required provenance

namespace distinctions collapse materially distinct objects

generator output is nondeterministic

canonical identifiers depend on unstable conversational context
```

---

# 132. Gap Classes

Naming gaps should be classified:

```text
CRITICAL
DECISION_RELEVANT
EXPLANATORY
COSMETIC
```

Examples:

```text
CRITICAL:
duplicate CellID

DECISION_RELEVANT:
ambiguous authority namespace

EXPLANATORY:
missing human-readable description

COSMETIC:
inconsistent display capitalization
```

---

# 133. Gap Recording

Example:

```yaml
gap_id: GAP_NAMING_001

class: CRITICAL

issue:
  duplicate canonical identifier

affected_objects: []

status: DETECTED

evidence: []

repair_candidate: null
```

---

# 134. Naming Registry Object

Recommended machine representation:

```yaml
NamingRegistryEntry:

  canonical_id:

  canonical_name:

  object_class:

  namespace:

  fully_qualified_id:

  machine_reference:

  canonical_path:

  human_label:

  aliases: []

  semantic_origin:

  source_refs: []

  parent:

  dependencies: []

  status:

  provenance: []

  validation: []

  gap_status:
```

---

# 135. Primitive Registry Example

```yaml
canonical_id: L13_PREDICTION

symbol: L13

object_class: PRIMITIVE

namespace: AMOS_COGNITIVE_MATRIX

fully_qualified_id:
  AMOS:MATRIX:PRIMITIVE:L13

machine_reference:
  amos://matrix/primitive/L13

human_label:
  Prediction

canonical_path:
  25_COGNITIVE_MATRIX/01_PRIMITIVES/L13_PREDICTION/

aliases:
  - forecasting

semantic_origin:
  AMOS_COGNITIVE_MATRIX
```

---

# 136. Cell Registry Example

```yaml
canonical_id:
  CELL_L13_O08_C04_H

object_class:
  MATRIX_CELL

namespace:
  AMOS_COGNITIVE_MATRIX

coordinate:
  primitive: L13
  operation: O08
  control_plane: C04
  scale: H

fully_qualified_id:
  AMOS:MATRIX:CELL:CELL_L13_O08_C04_H

machine_reference:
  amos://matrix/cell/CELL_L13_O08_C04_H

structural_status:
  ADDRESSABLE

implementation_status:
  UNKNOWN

validation_status:
  UNVALIDATED

authority_status:
  NOT_APPLICABLE_UNTIL_EFFECT
```

---

# 137. Dependency on Matrix Contract

`NAMING_STANDARD.md` depends on:

```text
MATRIX_CONTRACT.md
```

for Matrix ontology and structural semantics.

If the Matrix Contract changes axis identity or cell construction, this naming standard must be revalidated.

---

# 138. Dependency on Primitive Registry

Primitive naming depends on:

```text
PRIMITIVE_REGISTRY.md
```

The naming standard defines grammar.

The registry defines current canonical members.

---

# 139. Dependency on Lifecycle Registry

Operation naming depends on:

```text
LIFECYCLE_OPERATION_REGISTRY.md
```

---

# 140. Dependency on Control-Plane Registry

Control-plane naming depends on:

```text
CONTROL_PLANE_REGISTRY.md
```

---

# 141. Dependency on Scale Registry

Scale naming depends on:

```text
SCALE_REGISTRY.md
```

---

# 142. Dependency on Cell Registry

Cell naming must remain synchronized with:

```text
AMOS_COGNITIVE_CELL_REGISTRY.json
```

and:

```text
CELL_INDEX.md
```

---

# 143. Dependency on Dependency Graph

Renames require dependency impact analysis through:

```text
09_DEPENDENCY_GRAPH/
```

because identifiers may appear as dependency endpoints.

---

# 144. Dependency on Routing

Bindings in:

```text
10_ROUTING/
```

must use canonical identifiers.

Aliases should not be used as durable routing keys.

---

# 145. Dependency on Validation

Naming correctness is validated through:

```text
11_VALIDATION/
```

Naming validation does not imply functional validation of the referenced object.

---

# 146. Dependency on Generators

Deterministic generators in:

```text
12_GENERATORS/
```

must implement this naming grammar.

Generator behavior must be tested against the registry rather than assumed correct.

---

# 147. Dependency Graph

Conceptual dependencies:

```text
CANON
 ↓
MATRIX_CONTRACT
 ↓
NAMING_STANDARD
 ↓
AXIS_REGISTRIES
 ↓
CELL_REGISTRY
 ↓
DEPENDENCY_GRAPH
 ↓
ROUTING
 ↓
VALIDATION
```

This graph represents structural dependence, not necessarily runtime call order.

---

# 148. Naming and Canon Firewall

If naming conventions conflict with source canon:

```text
DO NOT SILENTLY NORMALIZE CANON
```

Instead:

```text
preserve source identifier
+
record Matrix-compatible alias/reference
```

unless governance explicitly authorizes canonical migration.

---

# 149. Naming and Provenance Firewall

Renaming must not erase:

```text
original source term

original source identifier

semantic ancestry

transformation history
```

---

# 150. Naming and Causal Firewall

A name must never imply causal status.

Example:

```text
CAUSE_ENGINE
```

must not be interpreted as evidence that its outputs establish causality.

Object names are semantic labels.

Causal claims require causal evidence.

---

# 151. Naming and Empirical Firewall

Likewise:

```text
SUPER_CONSCIOUSNESS_ENGINE
```

or other corpus-defined names must not be treated as empirical proof of consciousness merely because the architecture uses that terminology.

Naming preserves corpus identity.

It does not validate the empirical interpretation.

---

# 152. Naming and Authority Firewall

Never infer:

```text
ADMIN
ROOT
GOVERNOR
CONTROL
EXECUTOR
```

as actual authority from a name.

Authority requires explicit infrastructure-governed evidence.

---

# 153. Naming and Security

Names may influence routing and permissions.

Therefore security-sensitive operations must use canonical IDs and explicit authority checks rather than natural-language labels.

Unsafe:

```text
if agent_name == "admin":
    allow()
```

Conceptually preferred:

```text
resolve identity
→ resolve authority
→ validate freshness
→ evaluate permission
```

---

# 154. Naming and Observability

Logs should record canonical IDs.

Example:

```yaml
event:
  cell_id: CELL_L18_O14_C08_L
  workflow_id: WF_GOVERNED_ACTION
  agent_id: AGENT_PLANNER
```

Human labels may be recorded additionally.

---

# 155. Naming and Replay

Replay requires stable identifiers.

Therefore canonical IDs must not depend on:

```text
current display label

UI ordering

temporary filename

conversation position

unstable natural-language descriptions
```

---

# 156. Naming and Selective Invalidation

When an identifier changes, affected dependencies should be located through explicit references.

Only dependent objects should be invalidated.

```text
RENAME
→ dependency descendants
```

not:

```text
RENAME
→ invalidate entire AMOS
```

unless global dependency is demonstrated.

---

# 157. Naming and Atomic Updates

A structural rename may require coordinated updates to:

```text
registry

path

dependency graph

routing bindings

tests

RSCFs

aliases

provenance
```

Partial rename states should not be treated as valid final state.

---

# 158. Naming and Freshness

Canonical identity may be stable while aliases or paths become stale.

Track independently:

```yaml
identity_freshness:
path_freshness:
alias_freshness:
registry_freshness:
```

---

# 159. Naming and Deprecation

Deprecated identity state:

```text
DEPRECATED
```

means:

```text
still resolvable
but no longer preferred
```

Deprecated does not necessarily mean invalid.

---

# 160. Naming and Supersession

Supersession means a successor object replaces another for a declared scope.

Record:

```yaml
superseded_id:
successor_id:
scope:
reason:
effective_state:
provenance:
```

---

# 161. Naming and Deletion

Canonical IDs with historical dependencies should not be casually deleted.

Prefer:

```text
DEPRECATED
SUPERSEDED
RETIRED
```

where lineage must remain reconstructable.

---

# 162. Naming and Matrix Generation

Generator algorithm:

```text
for primitive in primitive_registry:
    for operation in operation_registry:
        for control_plane in control_plane_registry:
            for scale in scale_registry:
                construct CellID
                validate grammar
                validate uniqueness
                register
```

This creates the addressable coordinate space.

---

# 163. Naming Generator Preconditions

```text
all axis registries valid

all symbols unique

ordering deterministic

naming grammar loaded

output namespace defined
```

---

# 164. Naming Generator Postconditions

```text
every generated CellID unique

every generated CellID parseable

every generated coordinate reversible

no registry member omitted

no undefined axis member introduced
```

---

# 165. Generator Failure

If a registry contains duplicate symbols:

```text
STOP
```

Do not generate guessed replacements.

---

# 166. Naming Search Priority

When resolving a name:

```text
1. fully qualified ID

2. canonical ID

3. canonical symbol

4. exact canonical name

5. registered alias

6. contextual semantic match

7. UNKNOWN
```

Contextual semantic matching must not automatically become canonical identity.

---

# 167. Naming Resolution Confidence

Suggested qualitative classes:

```text
EXACT

HIGH

CONDITIONAL

AMBIGUOUS

UNKNOWN
```

`EXACT` refers to identifier resolution, not empirical validity.

---

# 168. Human-Friendly Display Names

Machine identity and display name should remain separate.

Example:

```yaml
canonical_id:
  CELL_L13_O08_C04_H

display_name:
  High-Scale Reasoning Prediction Cell
```

Display names may evolve without changing identity.

---

# 169. Description Boundary

Descriptions explain identifiers.

Descriptions do not define identity unless the governing registry explicitly uses them as semantic definitions.

---

# 170. Abbreviation Standard

Abbreviations must be registered if used canonically.

Examples:

```text
MOC
RSCF
HML
GMEF
```

Unregistered abbreviations should not become durable machine identifiers.

---

# 171. Acronym Collision

If an acronym has multiple meanings:

```text
QUALIFY
```

Example conceptual form:

```text
CP_MATRIX
CP_INFRA
```

rather than ambiguous:

```text
CP
```

---

# 172. Reserved Prefixes

Recommended Matrix reserved prefixes:

```text
L
O
C
CELL
STATE
OP
INV
EQ
DEP
BIND
AGENT
SKILL
WF
PROTO
KERNEL
MEM
KNOW
EVID
PROV
RSCF
GAP
FAIL
REPAIR
TEST
VALIDATOR
VAL
AUTH
PROP
COMMIT
CANON_REF
_TMP
_DRAFT
```

---

# 173. Reserved Prefix Protection

A prefix must not be reused for a different object class without explicit architecture migration.

Example:

```text
GAP_
```

must continue to identify gaps.

---

# 174. Registry Integrity Rule

Canonical identity is established through:

```text
valid naming grammar
+
authoritative registry membership
+
semantic definition
+
provenance
```

not filename presence alone.

---

# 175. Naming Promotion Gate

A proposed canonical name may be promoted when:

```text
syntax valid

object class valid

namespace valid

semantic definition present

collision checks pass

provenance present

dependencies identified

required governance passed
```

---

# 176. Naming Rejection Gate

Reject or quarantine when:

```text
exact collision

semantic duplication unresolved

namespace unknown

source identity unknown

illegal syntax

ambiguous object class

canonical target already exists

provenance unavailable where required
```

---

# 177. Naming Gap Gate

If a proposed object appears necessary but semantics are incomplete:

```text
CREATE GAP
```

rather than inventing a canonical definition.

---

# 178. Matrix Naming Completeness

Naming architecture is `COMPLETE_FOR_SCOPE` when:

```text
all object classes have naming rules

all four Matrix axes have canonical identifiers

all cells can be deterministically named

all canonical IDs are unique

all aliases are resolvable or explicitly ambiguous

all cross-architecture references preserve namespaces

all naming changes preserve provenance

all required validators pass

no critical unresolved naming collision exists
```

---

# 179. RSCF Completion State

```yaml
claim_class: AMOS_MODEL

claim:
  The Naming Standard defines deterministic,
  namespace-aware, provenance-preserving identity
  conventions for the AMOS Cognitive Matrix.

scope:
  AMOS_OS/25_COGNITIVE_MATRIX

regime:
  structural architecture

freshness:
  dependent_on_current_matrix_registries

evidence:
  - Matrix axis structure
  - Matrix cell construction
  - AMOS architecture separation requirements
  - provenance and identity requirements

provenance:
  - Trang Phan AMOS/Trang corpus
  - AMOS Full Brain OS
  - AMOS CORE lineage
  - AMOS Cognitive Matrix architecture

dependencies:
  - MATRIX_CONTRACT
  - PRIMITIVE_REGISTRY
  - LIFECYCLE_OPERATION_REGISTRY
  - CONTROL_PLANE_REGISTRY
  - SCALE_REGISTRY
  - CELL_REGISTRY
  - DEPENDENCY_GRAPH
  - ROUTING
  - VALIDATION

competing:
  - globally unique opaque identifiers
  - UUID-only identity architecture
  - ontology-generated semantic URIs
  - graph-native identity without filesystem naming
  - content-addressed identity

falsifiers:
  - canonical IDs collide
  - cell IDs are nondeterministic
  - cell IDs cannot round-trip to coordinates
  - aliases resolve unpredictably
  - namespaces fail to distinguish different objects
  - canonical renaming destroys provenance
  - external identities are overwritten

confidence_ceiling:
  bounded by current registry,
  canon,
  semantic-definition,
  and provenance integrity
```

---

# 180. Current Gap Status

```yaml
gap_status:

  critical:
    - none established by this contract alone

  decision_relevant:
    - canonical machine URI implementation not yet demonstrated
    - runtime enforcement of naming rules requires executable validation
    - external AMOS subsystem namespace registry must remain synchronized

  explanatory:
    - additional domain-specific aliases may be required

  cosmetic:
    - display-name conventions may be extended
```

These gaps must not be represented as resolved without evidence.

---

# 181. Final Naming Contract

The canonical naming transformation is:

[
SemanticObject
\rightarrow
ObjectClass
\rightarrow
Namespace
\rightarrow
CanonicalID
\rightarrow
CanonicalPath
\rightarrow
MachineReference
]

subject to:

[
Unique(ID)
\land
Typed(ID)
\land
Resolvable(ID)
\land
ProvenanceBound(ID)
]

The AMOS Cognitive Matrix therefore follows these governing naming laws:

```text
IDENTIFY BEFORE ROUTING.

TYPE BEFORE NAMING.

NAMESPACE BEFORE MERGING.

SEARCH BEFORE CREATING.

PRESERVE SOURCE NAMES BEFORE NORMALIZING.

USE CANONICAL IDS FOR DURABLE REFERENCES.

USE ALIASES FOR DISCOVERY, NOT IDENTITY.

DO NOT INFER SEMANTIC EQUIVALENCE FROM SIMILAR NAMES.

DO NOT INFER DIFFERENT OBJECTS FROM DIFFERENT NAMES.

DO NOT INFER IMPLEMENTATION FROM ADDRESSABILITY.

DO NOT INFER VALIDATION FROM REGISTRATION.

DO NOT INFER AUTHORITY FROM ROLE NAMES.

DO NOT TURN PROPOSALS INTO COMMITS THROUGH LABELING.

DO NOT FORCE UNKNOWN NAMES INTO KNOWN CATEGORIES.

PRESERVE PROVENANCE THROUGH EVERY RENAME.

FAIL CLOSED ON UNRESOLVED IDENTITY COLLISION.
```

The central invariant is:

[
\boxed{
Canonical\ Identity
===================

Typed\ Name
+
Namespace
+
Semantic\ Definition
+
Registry\ Membership
+
Provenance
}
]

while always preserving:

```text
CANONICAL IDENTITY
!=
EMPIRICAL TRUTH

CANONICAL IDENTITY
!=
IMPLEMENTATION

CANONICAL IDENTITY
!=
VALIDATION

CANONICAL IDENTITY
!=
AUTHORITY
```

---

[[00_ROOT_MOC]]|[[AMOS MOC]]

---
**Related:** [[00_HOME]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: cognitive_matrix_naming_standard
node_type: note
path: 25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_NAMING_STANDARD.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
