---
tags: ['cognitive_matrix', 'index', 'moc']
---

# 00_INDEX — AMOS Cognitive Matrix MOC

**Origin architect / steward:** Trang Phan
**Architecture:** AMOS OS
**Subsystem:** `25_COGNITIVE_MATRIX`
**Artifact:** `00_INDEX/MOC.md`
**Class:** `MATRIX_MASTER_INDEX`
**Role:** `NAVIGATION / DISCOVERY / AUTHORITY-RESOLUTION / PROGRESSIVE-LOADING`
**Status:** `ACTIVE STRUCTURAL INDEX`
**Epistemic class:** `AMOS_MODEL + SOURCE_CANON_BINDING`

---

# 0. Purpose

`MOC.md` is the canonical **Map of Contents and navigation entrypoint** for the AMOS Cognitive Matrix.

It answers:

```text
WHERE is a Matrix concept defined?

WHICH artifact is authoritative for it?

WHAT must be loaded first?

WHAT depends on it?

WHAT may be skipped?

WHERE are implementation bindings stored?

WHERE are validation results stored?

WHERE are structural gaps stored?

HOW does AMOS descend from architecture → coordinate → implementation → evidence?
```

This file is not the Matrix specification itself.

The governing separation is:

```text
MOC
=
navigation + discovery + authority resolution

MATRIX_CONTRACT
=
structural rules and invariants

REGISTRIES
=
canonical identities

CELL_REGISTRY
=
coordinate instances

BINDINGS
=
implementation mappings

DEPENDENCY_GRAPH
=
dependency topology

VALIDATION
=
evidence of correctness

GAP_MAP
=
known incompleteness
```

Therefore:

```text
MOC != MATRIX_CONTRACT

MOC != REGISTRY

MOC != IMPLEMENTATION

MOC != VALIDATION

MOC != CANON
```

---

# 1. Canonical Entry Point

For any Cognitive Matrix operation, begin:

```text
25_COGNITIVE_MATRIX/
└── 00_INDEX/
    └── MOC.md
```

Then resolve only the minimum required path.

Canonical navigation:

```text
MOC
 ↓
MATRIX_CONTRACT
 ↓
Axis Registry
 ↓
Cell Registry
 ↓
Cell Contract
 ↓
Dependency Closure
 ↓
Routing / Bindings
 ↓
Implementation Objects
 ↓
Evidence / Provenance
 ↓
Validation
 ↓
Authority / Effect Governance
```

This is the default progressive-loading route.

---

# 2. Cognitive Matrix Root

```text
25_COGNITIVE_MATRIX/
│
├── 00_INDEX/
├── 01_PRIMITIVES/
├── 02_LIFECYCLE_OPERATIONS/
├── 03_CONTROL_PLANES/
├── 04_SCALES/
├── 05_CELL_REGISTRY/
├── 06_CELL_CONTRACTS/
├── 07_COVERAGE/
├── 08_STRUCTURAL_GAPS/
├── 09_DEPENDENCY_GRAPH/
├── 10_ROUTING/
├── 11_VALIDATION/
└── 12_GENERATORS/
```

Each branch owns a different class of Matrix truth.

No branch should silently absorb another branch's authority.

---

# 3. Authority Map

| Path                      | Primary authority                    |
| ------------------------- | ------------------------------------ |
| `00_INDEX`                | navigation and Matrix-wide contracts |
| `01_PRIMITIVES`           | cognitive-function semantics         |
| `02_LIFECYCLE_OPERATIONS` | transformation semantics             |
| `03_CONTROL_PLANES`       | cognitive control dimensions         |
| `04_SCALES`               | H/M/L scale semantics                |
| `05_CELL_REGISTRY`        | canonical cell identities/status     |
| `06_CELL_CONTRACTS`       | per-cell structural requirements     |
| `07_COVERAGE`             | coverage measurement                 |
| `08_STRUCTURAL_GAPS`      | known missing structure              |
| `09_DEPENDENCY_GRAPH`     | dependency topology/invalidation     |
| `10_ROUTING`              | component bindings and routing       |
| `11_VALIDATION`           | validation state and promotion gates |
| `12_GENERATORS`           | deterministic generation machinery   |

Hard rule:

```text
LOCATION
DOES NOT
IMPLY AUTHORITY
```

Authority is determined by artifact class and declared contract.

---

# 4. `00_INDEX` — Matrix Navigation and Global Contracts

```text
00_INDEX/
│
├── README.md
├── MOC.md
├── MATRIX_CONTRACT.md
├── PRIMITIVE_REGISTRY.md
├── LIFECYCLE_OPERATION_REGISTRY.md
├── CONTROL_PLANE_REGISTRY.md
├── SCALE_REGISTRY.md
├── STATUS_LEGEND.md
└── NAMING_STANDARD.md
```

## `README.md`

Human-facing introduction.

Use for:

* orientation;
* subsystem purpose;
* basic navigation;
* quick-start instructions.

Do not treat README prose as stronger than a canonical registry or contract.

---

## `MOC.md`

This artifact.

Owns:

```text
navigation
artifact discovery
authority resolution
progressive loading
cross-folder orientation
```

---

## `MATRIX_CONTRACT.md`

The governing structural contract.

Owns:

```text
Matrix ontology
cell construction
hard invariants
status dimensions
binding semantics
dependency rules
validation semantics
gap semantics
authority boundaries
completion criteria
```

When MOC and Matrix Contract appear inconsistent:

```text
MATRIX_CONTRACT
>
MOC descriptive navigation
```

unless the governing canon explicitly supersedes it.

---

## `PRIMITIVE_REGISTRY.md`

Canonical registry for:

```text
L00–L29
```

Use this file to resolve primitive identity.

---

## `LIFECYCLE_OPERATION_REGISTRY.md`

Canonical registry for:

```text
O00–O16
```

Use this file to resolve lifecycle-operation identity.

---

## `CONTROL_PLANE_REGISTRY.md`

Canonical Matrix control-plane registry:

```text
C01–C09
```

---

## `SCALE_REGISTRY.md`

Canonical scale registry:

```text
H
M
L
```

---

## `STATUS_LEGEND.md`

Defines normalized status vocabulary.

Examples:

```text
DEFINED
PARTIAL
STRUCTURAL_GAP

NOT_IMPLEMENTED
SCAFFOLDED
IMPLEMENTED
OPERATIONAL

UNVALIDATED
TESTED
VALIDATED

BLOCKED
QUARANTINED
```

---

## `NAMING_STANDARD.md`

Defines deterministic naming for:

```text
Primitive IDs
Operation IDs
Control-plane IDs
Scale IDs
Cell IDs
Gap IDs
Binding IDs
Validation IDs
Dependency IDs
```

---

# 5. `01_PRIMITIVES` — Cognitive Function Axis

```text
01_PRIMITIVES/
│
├── L00_REALITY_ENVIRONMENT/
├── L01_SENSING_OBSERVATION/
├── L02_ATTENTION/
├── L03_PERCEPT_FORMATION/
├── L04_OBJECT_ENTITY_FORMATION/
├── L05_BINDING/
├── L06_WORKING_STATE/
├── L07_MEMORY/
├── L08_REPRESENTATION/
├── L09_INFERENCE/
├── L10_WORLD_MODELING/
├── L11_CAUSAL_MODELING/
├── L12_COUNTERFACTUAL_SIMULATION/
├── L13_PREDICTION/
├── L14_VALUATION/
├── L15_GOAL_FORMATION/
├── L16_PLANNING/
├── L17_DECISION/
├── L18_ACTION/
├── L19_OUTCOME_OBSERVATION/
├── L20_CREDIT_ASSIGNMENT/
├── L21_LEARNING/
├── L22_CONSOLIDATION/
├── L23_METACOGNITION/
├── L24_SELF_REGULATION/
├── L25_IDENTITY_CONTINUITY/
├── L26_SOCIAL_COGNITION/
├── L27_MULTI_AGENT_COGNITION/
├── L28_GOVERNANCE/
└── L29_EVOLUTION/
```

Canonical primitive order represents the Matrix cognitive-function coordinate system.

It must not automatically be interpreted as a literal biological processing sequence.

---

# 6. Standard Primitive Package

Each primitive contains:

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

---

# 7. Primitive Progressive-Loading Order

Do not load every primitive artifact automatically.

Preferred sequence:

```text
DEFINITION
 ↓
PURPOSE
 ↓
INVARIANTS
 ↓
DEPENDENCIES
 ↓
relevant specialized contract
```

Load:

```text
AGENTS
SKILLS
WORKFLOWS
```

only when implementation/routing matters.

Load:

```text
TESTS
RSCF
PROVENANCE
```

when evidence or validation matters.

Load:

```text
GAP_MATRIX
FAILURE_MODES
REPAIR
```

when incompleteness or failure can alter the decision.

---

# 8. Primitive Artifact Semantics

### `DEFINITION.md`

Defines what the primitive is and is not.

### `PURPOSE.md`

Defines why AMOS requires the primitive.

### `STATE.md`

Defines state consumed, maintained, and produced.

### `VARIABLES.md`

Defines typed variables.

### `OPERATORS.md`

Defines permitted transformations.

### `INVARIANTS.md`

Defines properties that must remain true.

### `EQUATIONS.md`

Contains formal relationships.

Every equation must identify its epistemic class.

### `MEMORY.md`

Defines memory interactions.

### `CONTROL_PLANES.md`

Defines control-plane participation.

### `HML.md`

Defines scale behavior.

### `AGENTS.md`

Defines candidate/validated agent bindings.

### `SKILLS.md`

Defines candidate/validated Skill bindings.

### `WORKFLOWS.md`

Defines workflow participation.

### `PROTOCOLS.md`

Defines communication/interface requirements.

### `DEPENDENCIES.md`

Defines prerequisite and downstream dependencies.

### `FAILURE_MODES.md`

Defines known failure states.

### `REPAIR.md`

Defines recovery paths.

### `TESTS.md`

Defines validation requirements.

### `RSCF.md`

Defines proof/evidence capsules.

### `GAP_MATRIX.md`

Defines unresolved primitive-level gaps.

### `PROVENANCE.md`

Defines semantic/source lineage.

---

# 9. `02_LIFECYCLE_OPERATIONS` — Transformation Axis

```text
02_LIFECYCLE_OPERATIONS/
│
├── O00_DISTINCTION/
├── O01_OBJECT/
├── O02_RELATION/
├── O03_BINDING/
├── O04_STATE/
├── O05_MEMORY/
├── O06_MODEL/
├── O07_INFERENCE/
├── O08_PREDICTION/
├── O09_SIMULATION/
├── O10_VALUE/
├── O11_GOAL/
├── O12_PLAN/
├── O13_DECISION/
├── O14_ACTION/
├── O15_OBSERVATION/
└── O16_LEARNING/
```

This axis answers:

```text
WHAT TRANSFORMATION
IS BEING PERFORMED?
```

---

# 10. Standard Lifecycle Package

```text
README.md
DEFINITION.md
SEMANTICS.md
INPUT_OUTPUT.md
PRECONDITIONS.md
POSTCONDITIONS.md
STATE_TRANSITIONS.md
INVARIANTS.md
DEPENDENCIES.md
CONTROL_PLANES.md
HML.md
AGENTS.md
SKILLS.md
WORKFLOWS.md
PROTOCOLS.md
FAILURE_MODES.md
TESTS.md
RSCF.md
GAP_MATRIX.md
```

---

# 11. `03_CONTROL_PLANES` — Cognitive Governance Axis

```text
03_CONTROL_PLANES/
│
├── C01_GOVERNANCE/
├── C02_METACOGNITIVE/
├── C03_EXECUTIVE/
├── C04_REASONING/
├── C05_REPRESENTATION/
├── C06_MEMORY/
├── C07_PERCEPTION/
├── C08_EXECUTION/
└── C09_KERNEL_CONTROL/
```

This axis answers:

```text
WHAT COGNITIVE CONTROL FIELD
GOVERNS THIS COORDINATE?
```

Do not confuse it with the AMOS Infrastructure Control Plane.

---

# 12. Standard Control-Plane Package

```text
README.md
DEFINITION.md
SCOPE.md
POLICIES.md
AUTHORITY.md
STATE.md
INVARIANTS.md
DECISION_RULES.md
PROTOCOLS.md
DEPENDENCIES.md
OBSERVABILITY.md
AGENTS.md
SKILLS.md
WORKFLOWS.md
FAILURE_MODES.md
REPAIR.md
TESTS.md
RSCF.md
GAP_MATRIX.md
PROVENANCE.md
```

---

# 13. `04_SCALES` — H/M/L Axis

```text
04_SCALES/
│
├── H_HIGH_SCALE/
├── M_MID_SCALE/
└── L_LOW_SCALE/
```

Scale meaning:

```text
H
=
systemic / governing / long-horizon

M
=
subsystem / workflow / organ / intermediate

L
=
local / atomic / immediate
```

---

# 14. Standard Scale Package

```text
README.md
DEFINITION.md
SEMANTICS.md
TRANSLATION_RULES.md
BOUNDARIES.md
INVARIANTS.md
DEPENDENCIES.md
CONTROL_PLANES.md
TESTS.md
RSCF.md
GAP_MATRIX.md
```

---

# 15. Matrix Coordinate Construction

The four registries produce:

[
Cell
====

Primitive
\times
LifecycleOperation
\times
ControlPlane
\times
Scale
]

Therefore:

[
30 \times 17 \times 9 \times 3
==============================

13,770
]

canonical addressable cells.

---

# 16. `05_CELL_REGISTRY` — Coordinate Authority

```text
05_CELL_REGISTRY/
│
├── README.md
├── AMOS_COGNITIVE_CELL_REGISTRY.json
├── AMOS_COGNITIVE_CELL_REGISTRY.csv
├── CELL_INDEX.md
└── CELL_STATUS_REGISTRY.md
```

The machine-readable registry is authoritative for generated cell identities.

Example:

```text
CELL_L10_O08_C04_H
```

resolves:

```text
L10 = WORLD_MODELING
O08 = PREDICTION
C04 = REASONING
H   = HIGH SCALE
```

---

# 17. Cell Registry Boundary

A cell's presence in the registry means:

```text
ADDRESSABLE
```

not:

```text
IMPLEMENTED
```

Therefore:

```text
REGISTRY_ENTRY
!=
CAPABILITY
```

---

# 18. `06_CELL_CONTRACTS` — Per-Cell Requirements

```text
06_CELL_CONTRACTS/
│
├── README.md
├── CELL_CONTRACT.md
├── CELL_STATE.md
├── CELL_BINDINGS.md
├── CELL_AUTHORITY.md
└── CELL_EVIDENCE.md
```

These files define what every cell must eventually be capable of representing.

---

# 19. Cell Contract Resolution

For a cell:

```text
CELL(P,O,C,S)
```

resolve:

```text
Identity
 ↓
Semantics
 ↓
State
 ↓
Dependencies
 ↓
Bindings
 ↓
Evidence
 ↓
Validation
 ↓
Authority
 ↓
Effect
```

---

# 20. `07_COVERAGE` — Coverage Accounting

```text
07_COVERAGE/
│
├── README.md
├── DERIVATION_RULES.md
├── COVERAGE_SUMMARY.json
├── COVERAGE_MODEL.md
├── COVERAGE_THRESHOLDS.md
└── COVERAGE_AUDIT.md
```

Coverage must remain typed.

Separate:

```text
structural coverage

binding coverage

implementation coverage

validation coverage

operational coverage
```

Never collapse them into one ambiguous percentage.

---

# 21. Coverage Boundary

```text
100% ADDRESSABLE
!=
100% IMPLEMENTED

100% IMPLEMENTED
!=
100% VALIDATED

100% VALIDATED
!=
UNIVERSALLY CORRECT
```

---

# 22. `08_STRUCTURAL_GAPS` — Explicit Incompleteness

```text
08_STRUCTURAL_GAPS/
│
├── README.md
├── EXPLICIT_GAP_MAP.json
├── GAP_REGISTRY.md
├── GAP_PRIORITY.md
└── GAP_PROMOTION.md
```

Every unresolved structural requirement belongs here or in its primitive-local `GAP_MATRIX.md`.

---

# 23. Gap Classes

```text
CRITICAL

DECISION_RELEVANT

EXPLANATORY

COSMETIC
```

Resolution order:

```text
CRITICAL
>
DECISION_RELEVANT
>
EXPLANATORY
>
COSMETIC
```

---

# 24. Gap Lifecycle

```text
DETECTED
 ↓
CLASSIFIED
 ↓
MAPPED
 ↓
RESEARCHING
 ↓
DESIGNED
 ↓
IMPLEMENTED
 ↓
VALIDATING
 ↓
CLOSED_FOR_SCOPE
```

---

# 25. `09_DEPENDENCY_GRAPH` — Causal/Structural Dependency Topology

```text
09_DEPENDENCY_GRAPH/
│
├── README.md
├── DEPENDENCY_MODEL.md
├── DEPENDENCY_TYPES.md
├── INVALIDATION_RULES.md
└── DEPENDENCY_AUDIT.md
```

This branch answers:

```text
WHAT MUST EXIST
BEFORE THIS CELL CAN BE TRUSTED?

WHAT BREAKS
IF THIS CELL FAILS?
```

---

# 26. Dependency Edge Classes

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

---

# 27. Selective Invalidation

Dependency failure triggers:

```text
FAILED NODE/EDGE
 ↓
DEPENDENT DESCENDANTS
```

not automatic global invalidation.

Hard law:

```text
LOCAL_FAILURE
!=
GLOBAL_FAILURE
```

---

# 28. `10_ROUTING` — Capability Resolution

```text
10_ROUTING/
│
├── README.md
├── ROUTING_BINDINGS.json
├── ROUTING_POLICY.md
├── BINDING_RULES.md
└── ROUTING_AUDIT.md
```

Routing maps cells to implementation candidates.

---

# 29. Binding Domains

A Matrix cell may bind:

```text
KERNELS

COGNITIVE ORGANS

AGENTS

SKILLS

WORKFLOWS

PROTOCOLS

MEMORY

KNOWLEDGE

STATE

MODELS

TOOLS

VALIDATORS
```

---

# 30. Binding Resolution Order

```text
Cell
 ↓
Requirements
 ↓
Candidate Bindings
 ↓
Compatibility
 ↓
Dependency Closure
 ↓
Evidence
 ↓
Validation
 ↓
Selected Binding
```

---

# 31. Binding Boundary

```text
DISCOVERED
!=
COMPATIBLE

COMPATIBLE
!=
BOUND

BOUND
!=
TESTED

TESTED
!=
VALIDATED

VALIDATED
!=
AUTHORIZED
```

---

# 32. `11_VALIDATION` — Evidence and Promotion

```text
11_VALIDATION/
│
├── README.md
├── CELL_VALIDATION.md
├── VALIDATION_LEVELS.md
├── PROMOTION_GATES.md
└── VALIDATION_EVIDENCE.md
```

Validation establishes what has actually been demonstrated.

---

# 33. Validation Ladder

```text
V0 UNDEFINED

V1 STRUCTURALLY_DEFINED

V2 SCHEMA_VALID

V3 UNIT_TESTED

V4 INTEGRATION_TESTED

V5 ADVERSARIAL_TESTED

V6 SYSTEM_VALIDATED

V7 OPERATIONALLY_MONITORED
```

---

# 34. Validation Scope

Every validation result inherits:

```text
system

environment

scale

time

regime

measurement method

dependencies

assumptions
```

Therefore:

```text
VALID_HERE
!=
VALID_EVERYWHERE
```

---

# 35. `12_GENERATORS` — Deterministic Construction

```text
12_GENERATORS/
│
├── README.md
├── build_amos_cognitive_cells.py
├── GENERATOR_CONTRACT.md
└── GENERATOR_TESTS.md
```

Generators may produce:

```text
cell IDs

registry entries

schemas

indexes

placeholder structures

dependency skeletons
```

They may not produce epistemic validation by construction.

---

# 36. Generator Boundary

```text
GENERATED
!=
IMPLEMENTED

GENERATED
!=
VALIDATED

GENERATED
!=
CANONICAL
```

Canonical status requires the appropriate governance path.

---

# 37. External AMOS OS Bindings

The Matrix does not contain every implementation.

It references other AMOS OS layers.

Canonical external resolution categories:

```text
CANON
KERNEL
INFRASTRUCTURE_CONTROL_PLANE
RUNTIME
COGNITIVE_ORGANISM
AGENTS
SKILLS
WORKFLOWS
PROTOCOLS
MEMORY
KNOWLEDGE
STATE
MODELS
TOOLS
OBSERVABILITY
SECURITY
TESTING
OPERATIONS
```

---

# 38. Canon Resolution

When semantics are disputed:

```text
Matrix artifact
 ↓
Matrix registry/contract
 ↓
AMOS Canon
 ↓
source lineage
```

Never invent missing canon to close a Matrix gap.

---

# 39. Kernel Resolution

Use Kernel artifacts when the question concerns:

```text
deterministic rule

typed state transition

invariant

constraint

formal operator

governed decision function
```

---

# 40. Agent Resolution

Use Agent artifacts when the question concerns:

```text
WHO performs a role?
```

Examples:

```text
Planner

Analyst

Auditor

Researcher

Simulator

Critic
```

Agent identity must not substitute for primitive identity.

---

# 41. Skill Resolution

Use Skill artifacts when the question concerns:

```text
WHAT reusable procedure provides capability?
```

---

# 42. Workflow Resolution

Use Workflow artifacts when the question concerns:

```text
IN WHAT ORDER
ARE CAPABILITIES COORDINATED?
```

---

# 43. Protocol Resolution

Use Protocol artifacts when the question concerns:

```text
HOW DO COMPONENTS COMMUNICATE?
```

---

# 44. Memory Resolution

Use Memory artifacts when the question concerns:

```text
WHAT IS RETAINED?

WHERE?

FOR HOW LONG?

WITH WHAT PROVENANCE?

UNDER WHAT RETRIEVAL RULE?
```

---

# 45. State Resolution

Use State artifacts when the question concerns current authoritative or working conditions.

Do not confuse:

```text
STATE
```

with:

```text
MEMORY
```

---

# 46. Knowledge Resolution

Use Knowledge artifacts when resolving:

```text
claims
evidence
RSCFs
source material
domain knowledge
case knowledge
```

---

# 47. Model Resolution

Use Model artifacts when a capability depends on:

```text
predictive model
generative model
classifier
embedding system
simulation
state-space model
domain model
```

---

# 48. Tool Resolution

Use Tool artifacts when an operation requires interaction with an external computational or information system.

---

# 49. Authority Resolution

Authority is never inferred from Matrix membership.

For consequential action:

```text
Matrix Cell
 ↓
Capability
 ↓
Proposed Effect
 ↓
Infrastructure Policy
 ↓
Authority
 ↓
Commit-Time Validation
 ↓
Effect
```

---

# 50. Cognitive Query Routing

Given task `T`, determine:

[
Q(T)
====

{P,O,C,S}
]

Then derive:

[
Cells(T)
========

{CELL(P_i,O_j,C_k,S_l)}
]

Then compute:

[
Closure(T)
==========

Cells(T)
\cup
Dependencies(Cells(T))
]

Only this dependency-closed set should be loaded unless further evidence is required.

---

# 51. Progressive Disclosure Rule

Default:

```text
MOC
 ↓
relevant registry
 ↓
relevant contract
 ↓
relevant cell
 ↓
required dependency
```

Do not default to:

```text
LOAD ENTIRE MATRIX
```

---

# 52. Raw Evidence Rule

Raw evidence is:

```text
DO_NOT_LOAD_UNLESS_REQUIRED
```

Load it when:

* provenance is disputed;
* validation depends on it;
* a contradiction exists;
* a claim is consequential;
* a source transformation must be audited.

---

# 53. Example — Prediction Task

Suppose AMOS must make a system-level prediction.

Possible coordinate:

```text
L13 PREDICTION
×
O08 PREDICTION
×
C04 REASONING
×
H HIGH
```

Address:

```text
CELL_L13_O08_C04_H
```

Navigation:

```text
MOC
 ↓
PRIMITIVE_REGISTRY
 ↓
L13_PREDICTION/
 ↓
O08_PREDICTION/
 ↓
C04_REASONING/
 ↓
H_HIGH_SCALE/
 ↓
CELL_REGISTRY
 ↓
CELL_CONTRACT
 ↓
DEPENDENCY_GRAPH
 ↓
ROUTING_BINDINGS
 ↓
VALIDATION
```

---

# 54. Example — Memory Consolidation

Coordinate:

```text
L22 CONSOLIDATION
×
O05 MEMORY
×
C06 MEMORY
×
M MID
```

Address:

```text
CELL_L22_O05_C06_M
```

Likely dependency classes:

```text
working state

memory provenance

learning evidence

retention policy

conflict handling

validation

rollback
```

---

# 55. Example — Governed External Action

Coordinate:

```text
L18 ACTION
×
O14 ACTION
×
C08 EXECUTION
×
L LOW
```

The Matrix may resolve the cognitive capability.

It still cannot independently authorize the effect.

Required route:

```text
CELL
 ↓
Execution binding
 ↓
Effect classification
 ↓
Infrastructure Control Plane
 ↓
Authority witness
 ↓
Freshness check
 ↓
Commit
```

---

# 56. Example — Learning From Outcome

Relevant cells may span:

```text
L19 OUTCOME_OBSERVATION
 ↓
L20 CREDIT_ASSIGNMENT
 ↓
L21 LEARNING
 ↓
L22 CONSOLIDATION
 ↓
L23 METACOGNITION
 ↓
L24 SELF_REGULATION
```

This illustrates why Matrix reasoning may require a cell set rather than a single coordinate.

---

# 57. Search Order

When searching the Matrix manually or programmatically:

```text
1. exact CellID
2. exact primitive/operation/control-plane/scale ID
3. canonical registry name
4. dependency reference
5. binding reference
6. semantic alias
7. raw text search
```

Exact identifiers should outrank fuzzy lexical similarity.

---

# 58. Alias Handling

Aliases may improve discovery but must resolve to canonical identifiers.

Example:

```text
"forecasting"
→ candidate alias
→ L13_PREDICTION
```

The alias itself is not canonical.

---

# 59. Naming Law

Canonical identifiers must be:

```text
stable
unique
deterministic
machine-readable
human-inspectable
```

Renaming requires dependency impact analysis.

---

# 60. Duplicate Prevention

Before creating a new:

```text
primitive
operation
control plane
scale
cell
binding
gap
```

search the canonical registry.

Do not create ontology duplicates merely because terminology differs.

---

# 61. Cross-Axis Collision Check

If two axes appear to contain similar concepts, preserve their functional distinction.

Example:

```text
L13_PREDICTION
```

versus:

```text
O08_PREDICTION
```

The first answers:

```text
WHAT cognitive capability?
```

The second answers:

```text
WHAT lifecycle transformation?
```

They may legitimately occupy the same cell.

---

# 62. Cross-Layer Collision Check

Likewise:

```text
L28_GOVERNANCE
```

is not identical to:

```text
C01_GOVERNANCE
```

and neither is identical to:

```text
AMOS Infrastructure Governance
```

---

# 63. Status Resolution

When multiple status claims exist, resolve them by dimension.

Example:

```yaml
structural_status: STRUCTURALLY_COMPLETE
implementation_status: IMPLEMENTED
validation_status: UNIT_TESTED
governance_status: AUTHORITY_REQUIRED
```

Do not reduce this to:

```text
status = complete
```

---

# 64. Provenance Resolution

Every authoritative artifact should identify:

```text
origin
source
lineage
transformation history
scope
freshness
```

Repeated copies of one source remain one provenance family.

---

# 65. Contradiction Handling

When two Matrix artifacts conflict:

```text
DETECT
 ↓
IDENTIFY AUTHORITY
 ↓
CHECK SCOPE
 ↓
CHECK FRESHNESS
 ↓
CHECK LINEAGE
 ↓
PRESERVE COMPETING IF UNRESOLVED
```

Do not silently merge contradictory definitions.

---

# 66. Supersession

If an artifact is superseded:

```text
old artifact
→ retain lineage
→ mark superseded
→ identify successor
→ invalidate affected dependencies
```

Do not erase historical provenance required for replay.

---

# 67. MOC Update Rule

Update `MOC.md` when:

* a Matrix branch is added;
* an authoritative artifact changes location;
* a new artifact class is introduced;
* navigation semantics change;
* authority resolution changes;
* a canonical registry is added or removed.

Do not update MOC merely because implementation content changes inside an already indexed artifact.

---

# 68. MOC Validation

MOC validation checks:

```text
all canonical root branches indexed

all authoritative registries reachable

no dead navigation targets

no duplicate authority declarations

no ambiguous canonical paths

all referenced artifacts resolvable

all external AMOS layers correctly typed
```

---

# 69. MOC Failure Modes

```text
STALE_INDEX

BROKEN_PATH

MISSING_AUTHORITY

DUPLICATE_AUTHORITY

AMBIGUOUS_ARTIFACT

ORPHAN_COMPONENT

CIRCULAR_NAVIGATION

WRONG_LAYER_BINDING

CANON_DRIFT

REGISTRY_DRIFT
```

---

# 70. Repair

MOC repair sequence:

```text
detect broken reference
 ↓
resolve canonical target
 ↓
inspect authority
 ↓
repair navigation edge
 ↓
check dependent links
 ↓
validate full MOC
```

Do not modify the target architecture merely to make an incorrect MOC reference valid.

---

# 71. MOC Tests

Minimum tests:

```text
T01_ROOT_BRANCH_COMPLETENESS

T02_CANONICAL_REGISTRY_DISCOVERABILITY

T03_CELL_REGISTRY_DISCOVERABILITY

T04_DEPENDENCY_GRAPH_DISCOVERABILITY

T05_ROUTING_DISCOVERABILITY

T06_VALIDATION_DISCOVERABILITY

T07_GAP_MAP_DISCOVERABILITY

T08_NO_DUPLICATE_AUTHORITY

T09_NO_DEAD_PATHS

T10_PROGRESSIVE_LOADING_PATH_VALID

T11_EXTERNAL_LAYER_BOUNDARIES_VALID

T12_NAMING_REFERENCES_VALID
```

---

# 72. Navigation Invariants

```text
N01 MOC != SOURCE_OF_EMPIRICAL_TRUTH

N02 MOC != MATRIX_CONTRACT

N03 MOC != CANON

N04 EVERY_CANONICAL_MATRIX_BRANCH MUST BE DISCOVERABLE

N05 EVERY AUTHORITATIVE REGISTRY MUST HAVE ONE CANONICAL PATH

N06 ALIASES MUST RESOLVE TO CANONICAL IDs

N07 NAVIGATION MUST PRESERVE H/M/L DISTINCTIONS

N08 NAVIGATION MUST PRESERVE CONTROL-PLANE DISTINCTIONS

N09 NAVIGATION MUST NOT CONFER AUTHORITY

N10 NAVIGATION MUST NOT CONFER VALIDATION

N11 PLACEHOLDER TARGET != IMPLEMENTED TARGET

N12 BROKEN LINK != MISSING CAPABILITY

N13 DUPLICATE FILE != INDEPENDENT EVIDENCE

N14 RAW EVIDENCE IS LOADED ONLY WHEN REQUIRED

N15 MINIMUM SUFFICIENT DEPENDENCY PATH IS PREFERRED
```

---

# 73. Machine Navigation Object

A future machine-readable projection may represent:

```yaml
moc:
  root: 25_COGNITIVE_MATRIX

  index:
    contract: 00_INDEX/MATRIX_CONTRACT.md
    primitive_registry: 00_INDEX/PRIMITIVE_REGISTRY.md
    lifecycle_registry: 00_INDEX/LIFECYCLE_OPERATION_REGISTRY.md
    control_plane_registry: 00_INDEX/CONTROL_PLANE_REGISTRY.md
    scale_registry: 00_INDEX/SCALE_REGISTRY.md

  axes:
    primitives: 01_PRIMITIVES
    lifecycle_operations: 02_LIFECYCLE_OPERATIONS
    control_planes: 03_CONTROL_PLANES
    scales: 04_SCALES

  cells:
    registry: 05_CELL_REGISTRY
    contracts: 06_CELL_CONTRACTS

  assurance:
    coverage: 07_COVERAGE
    gaps: 08_STRUCTURAL_GAPS
    dependencies: 09_DEPENDENCY_GRAPH
    routing: 10_ROUTING
    validation: 11_VALIDATION

  construction:
    generators: 12_GENERATORS
```

---

# 74. Human Navigation

For a human architect:

```text
Need architecture rules?
→ MATRIX_CONTRACT.md

Need a cognitive primitive?
→ 01_PRIMITIVES/

Need an operation?
→ 02_LIFECYCLE_OPERATIONS/

Need cognitive governance?
→ 03_CONTROL_PLANES/

Need scale semantics?
→ 04_SCALES/

Need a CellID?
→ 05_CELL_REGISTRY/

Need cell requirements?
→ 06_CELL_CONTRACTS/

Need completeness?
→ 07_COVERAGE/

Need missing architecture?
→ 08_STRUCTURAL_GAPS/

Need dependencies?
→ 09_DEPENDENCY_GRAPH/

Need implementation mapping?
→ 10_ROUTING/

Need proof that it works?
→ 11_VALIDATION/

Need deterministic generation?
→ 12_GENERATORS/
```

---

# 75. Agent Navigation

For an AMOS agent:

```text
Task
 ↓
MOC
 ↓
resolve relevant Matrix coordinate
 ↓
load smallest sufficient contracts
 ↓
resolve dependencies
 ↓
resolve capability bindings
 ↓
check evidence
 ↓
check validation
 ↓
return candidate cognition/action
```

---

# 76. Runtime Navigation

For runtime execution:

```text
Task State
 ↓
Cell Resolver
 ↓
Cell Registry
 ↓
Dependency Resolver
 ↓
Binding Router
 ↓
Capability Runtime
 ↓
Validation / Observability
 ↓
Infrastructure Effect Governance
```

---

# 77. Research Navigation

When a gap requires research:

```text
Gap
 ↓
Gap Registry
 ↓
Affected Cell
 ↓
Missing premise
 ↓
Required evidence class
 ↓
Research
 ↓
Evidence capsule
 ↓
Validation
 ↓
Gap reassessment
```

---

# 78. Repair Navigation

When a failure occurs:

```text
Observed failure
 ↓
Affected Cell
 ↓
Dependency Graph
 ↓
Earliest failed premise/edge
 ↓
Failure Mode
 ↓
Repair contract
 ↓
Revalidation
 ↓
Selective restoration
```

---

# 79. Evolution Navigation

For architecture evolution:

```text
Proposed change
 ↓
Affected Matrix coordinates
 ↓
Dependency impact
 ↓
Canon compatibility
 ↓
Sandbox
 ↓
Tests
 ↓
Adversarial validation
 ↓
Governed promotion
 ↓
Monitoring
```

---

# 80. MOC RSCF

```yaml
rscf:

  claim:
    MOC provides the canonical navigation and
    authority-resolution map for the AMOS Cognitive Matrix.

  class:
    AMOS_MODEL

  scope:
    AMOS_OS/25_COGNITIVE_MATRIX

  load_bearing_premises:
    - canonical Matrix root is known
    - axis registries are stable
    - authoritative artifact paths are declared
    - cell registry is deterministic
    - external AMOS layer distinctions are preserved

  dependencies:
    - MATRIX_CONTRACT
    - PRIMITIVE_REGISTRY
    - LIFECYCLE_OPERATION_REGISTRY
    - CONTROL_PLANE_REGISTRY
    - SCALE_REGISTRY
    - CELL_REGISTRY
    - DEPENDENCY_MODEL
    - ROUTING_BINDINGS
    - VALIDATION

  competing:
    - alternate navigation hierarchies
    - graph-only discovery without hierarchical MOC
    - dynamically generated indexes

  falsifiers:
    - authoritative artifact cannot be located
    - canonical paths conflict
    - MOC routes to incorrect architectural layer
    - duplicate authority cannot be resolved
    - required Matrix branch is undiscoverable

  confidence_ceiling:
    bounded by registry and path freshness
```

---

# 81. Completion Criterion

`MOC.md` is `COMPLETE_FOR_SCOPE` when:

```text
all Matrix root branches are indexed

all four axes are discoverable

all canonical registries are discoverable

cell registry is discoverable

cell contracts are discoverable

coverage system is discoverable

gap system is discoverable

dependency graph is discoverable

routing system is discoverable

validation system is discoverable

generator system is discoverable

external AMOS implementation layers are distinguished

authority resolution is explicit

progressive-loading order is explicit

repair/evolution routes are explicit

no unresolved critical navigation ambiguity exists
```

---

# 82. Final Navigation Contract

The MOC's governing function is:

[
MOC:
Intent
\rightarrow
CanonicalLocation
\rightarrow
Authority
\rightarrow
Dependencies
\rightarrow
MinimumRequiredContext
]

The MOC must make AMOS Cognitive Matrix knowledge navigable without flattening the architecture.

Its governing laws are:

```text
FIND BEFORE LOADING.

RESOLVE AUTHORITY BEFORE TRUSTING.

LOAD THE SMALLEST SUFFICIENT PATH.

FOLLOW DEPENDENCIES ONLY WHEN THEY CAN CHANGE THE RESULT.

PRESERVE CANON, MATRIX, IMPLEMENTATION, VALIDATION,
AND AUTHORITY AS DISTINCT LAYERS.

NEVER TREAT NAVIGATION AS EVIDENCE.

NEVER TREAT A FILE'S EXISTENCE AS IMPLEMENTATION.

NEVER TREAT ADDRESSABILITY AS VALIDATION.

NEVER HIDE A BROKEN OR UNKNOWN PATH.
```

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]]
