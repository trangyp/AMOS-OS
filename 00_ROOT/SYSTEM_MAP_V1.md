---
type: map
source: 00_ROOT
artifact_id: AMOS-OS-SYSTEM-MAP
name: AMOS_OS_SYSTEM_MAP
title: "AMOS OS System Map — Authoritative Plane Topology and Cross-System Relationship Map"
document_version: "2.0.0"
map_version: "1.0.0"
amos_core_target: "v4.4"
status: ACTIVE_MAP
conclusion_class: AMOS_MODEL
rscf_state: derived
canon_group: tech-ai
canon_type: system-map
origin_architect: Trang Phan
steward: Trang Phan
created: 2026-08-25
updated: 2026-08-25
scope: "- AMOS_OS
  - repository_topology
  - system_planes
  - authority_boundaries
  - execution_topology
..."
tags:
- amos
- amos_os
- root
- amos-os
- system-map
- architecture
- topology
- repository-topology
- system-planes
- plane-map
- dependency-map
- authority
- provenance
- canon
- kernel
- control-plane
- runtime
- cognition
- cognitive-organism
- agents
- skills
- workflows
- protocols
- memory
- knowledge
- state
- models
- tools
- interfaces
- schemas
- observability
- security
- tests
- operations
- domains
- research
- operating-model
- archive
- cognitive-matrix
- rscf
- hml
- governance
- failure-recovery
- canon-group/tech-ai
- canon/system-map
- rscf/claim
- rscf/provenance
- rscf/state/derived
- topic/amos-os
- topic/system-map
- topic/system-topology
- topic/repository-architecture
aliases: "- AMOS System Map
  - AMOS OS System Map
  - AMOS Plane Map
  - AMOS Architecture Map
  - AMOS Repos..."
related: "see body"
---
# AMOS OS System Map
**Origin architect / steward:** Trang Phan
> **Status:** `ACTIVE_MAP`  
> **AMOS_CORE target:** `v4.4`  
> **Conclusion class:** `AMOS_MODEL`
rscf:
  state: SOURCE_CLAIM
  claim_class: EMPIRICAL
  provenance: AMOS_corpus
  scope: root_index
---


# 0. Purpose

This document is the root topology map for `AMOS_OS`.

It defines:

```text
WHAT MAJOR PLANES EXIST
WHERE RESPONSIBILITIES BELONG
HOW PLANES RELATE
WHERE AUTHORITY LIVES
WHERE EXECUTION LIVES
WHERE KNOWLEDGE LIVES
WHERE STATE LIVES
WHERE EXTERNAL EFFECTS OCCUR
```

It is primarily a **structural map**.

It does not establish that every mapped component is implemented, integrated, tested, or operational.

Hard boundary:

```text
SYSTEM MAP
!=
AUTHORITATIVE IMPLEMENTATION STATE
```

Use:

```text
FULL_TREE
```

for expected detailed placement.

Use:

```text
DEPENDENCY_MAP
```

for typed dependency relationships.

Use:

```text
AUTHORITATIVE_STATE
```

for current validated implementation state.

---

# 1. Top-Level Repository Map

```text
AMOS_OS/
│
├── 00_ROOT
│
├── 01_CANON
├── 02_KERNEL
├── 03_CONTROL_PLANE
├── 04_RUNTIME
├── 05_COGNITIVE_ORGANISM
├── 06_AGENTS
├── 07_SKILLS
├── 08_WORKFLOWS
├── 09_PROTOCOLS
├── 10_MEMORY
├── 11_KNOWLEDGE
├── 12_STATE
├── 13_MODELS
├── 14_TOOLS
├── 15_INTERFACES
├── 16_SCHEMAS
├── 17_OBSERVABILITY
├── 18_SECURITY
├── 19_TESTS
├── 20_OPERATIONS
├── 21_DOMAINS
├── 22_RESEARCH
├── 23_OPERATING_MODEL
├── 24_ARCHIVE
└── 25_COGNITIVE_MATRIX
```

---

# 2. Root Architectural Spine

The primary conceptual flow is:

```text
CANON
  ↓
KERNEL
  ↓
CONTROL PLANE
  ↓
RUNTIME
  ↓
COGNITIVE ORGANISM
  ↓
AGENTS / SKILLS / WORKFLOWS
  ↓
TOOLS / MODELS / DOMAIN ADAPTERS
  ↓
EXTERNAL EFFECTS
```

This is a responsibility and governance spine.

It is **not** a claim that every runtime operation literally traverses every layer.

The smallest sufficient valid dependency path should be used.

---

# 3. Cross-Cutting Substrates

The execution spine is supported by cross-cutting systems:

```text
                    ┌──────────────┐
                    │    CANON     │
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │    KERNEL    │
                    └──────┬───────┘
                           │
                    ┌──────▼──────────┐
                    │ CONTROL PLANE   │
                    └──────┬──────────┘
                           │
                    ┌──────▼───────┐
                    │   RUNTIME    │
                    └──────┬───────┘
                           │
               ┌───────────▼────────────┐
               │ COGNITIVE ORGANISM     │
               └───────────┬────────────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
      ┌───▼────┐      ┌────▼────┐      ┌────▼──────┐
      │ AGENTS │      │ SKILLS  │      │ WORKFLOWS │
      └───┬────┘      └────┬────┘      └────┬──────┘
          └────────────────┼────────────────┘
                           │
                 ┌─────────▼─────────┐
                 │ TOOLS / MODELS /  │
                 │ DOMAIN ADAPTERS   │
                 └─────────┬─────────┘
                           │
                    EXTERNAL EFFECTS
```

Cross-cutting across this topology:

```text
MEMORY
KNOWLEDGE
STATE
PROVENANCE
OBSERVABILITY
SECURITY
SCHEMAS
TESTS
OPERATIONS
```

---

# 4. Plane Classification

AMOS OS planes fall into six broad structural classes.

```text
A. DEFINITION / CONSTRAINT
B. GOVERNANCE / EXECUTION
C. COGNITIVE / CAPABILITY
D. PERSISTENT SUBSTRATES
E. SUPPORT / VERIFICATION
F. DOMAIN / ORGANIZATIONAL / HISTORICAL
```

Mapping:

| Class                                | Planes                                                                                                    |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| Definition / Constraint              | `01_CANON`, `02_KERNEL`                                                                                   |
| Governance / Execution               | `03_CONTROL_PLANE`, `04_RUNTIME`                                                                          |
| Cognitive / Capability               | `05_COGNITIVE_ORGANISM`, `06_AGENTS`, `07_SKILLS`, `08_WORKFLOWS`, `09_PROTOCOLS`                         |
| Persistent Substrates                | `10_MEMORY`, `11_KNOWLEDGE`, `12_STATE`, `13_MODELS`                                                      |
| Support / Verification               | `14_TOOLS`, `15_INTERFACES`, `16_SCHEMAS`, `17_OBSERVABILITY`, `18_SECURITY`, `19_TESTS`, `20_OPERATIONS` |
| Domain / Organizational / Historical | `21_DOMAINS`, `22_RESEARCH`, `23_OPERATING_MODEL`, `24_ARCHIVE`, `25_COGNITIVE_MATRIX`                    |

This classification is organizational, not a replacement for typed dependency relationships.

---

# 5. `00_ROOT` — Root Coordination Layer

## Role

`00_ROOT` provides repository-level orientation and architectural coordination.

Expected root artifacts include:

```text
README.md
MOC.md
NEURAL_NETWORK.md
ARCHITECTURE.md
AUTHORITATIVE_STATE.md
DEPENDENCY_MAP.md
FULL_TREE.md
NAMING_STANDARD.md
PLACEMENT_RULES.md
ROADMAP.md
SYSTEM_MAP.md
```

## Responsibility

```text
orientation
repository navigation
global architecture
global placement
global naming
system topology
dependency overview
roadmap
authoritative-state pointer
```

## Boundary

```text
ROOT DOCUMENTATION
!=
CANON
```

unless a specific artifact is explicitly admitted into canon.

---

# 6. `01_CANON` — Canon Plane

## Role

Contains authoritative AMOS definitions and governing source law.

Typical content:

```text
official definitions
core laws
canonical invariants
accepted architecture definitions
formal terminology
governed framework definitions
```

## Authority relationship

```text
CANON
↓ constrains
KERNEL
CONTROL PLANE
RUNTIME
COGNITION
AGENTS
SKILLS
WORKFLOWS
```

## Hard boundary

```text
CANON
!=
IMPLEMENTATION
```

Canon states what is authoritative.

It does not itself execute.

---

# 7. `02_KERNEL` — Deterministic Kernel Plane

## Role

Implements deterministic primitives and invariants required by higher layers.

Candidate families include:

```text
identity
RSCF
dependency
provenance
validation
state transition
contradiction
scope/regime
freshness
hashing
routing primitives
```

Conceptually:

```text
CANON
↓
KERNEL
↓
DETERMINISTIC CONSTRAINT / OPERATOR
```

## Boundary

```text
KERNEL
!=
CONTROL_PLANE
```

The kernel provides primitives.

The control plane decides how governed operations use them.

---

# 8. `03_CONTROL_PLANE` — Governance Plane

## Role

Owns governed decision and authority coordination.

Responsibilities may include:

```text
authority
policy
commit governance
provenance enforcement
validation gates
state transition authorization
coordination
finalization
rollback governance
```

Canonical distinction:

```text
CAPABILITY
!=
AUTHORITY
```

and:

```text
PROPOSAL
!=
COMMIT
```

---

# 9. `04_RUNTIME` — Execution Plane

## Role

Coordinates live execution.

Candidate responsibilities:

```text
task lifecycle
scheduler
router
execution harness
session
step/tick
runtime state
mode activation
worker invocation
tool invocation coordination
failure handling
```

Conceptual flow:

```text
REQUEST
↓
PARSE
↓
SCOPE
↓
ROUTE
↓
LOAD REQUIRED DEPENDENCIES
↓
EXECUTE
↓
VALIDATE
↓
RETURN / PROPOSE COMMIT
```

## Boundary

```text
RUNTIME
!=
CONTROL_PLANE
```

Runtime performs orchestration.

Control plane governs authority and commit semantics.

---

# 10. `05_COGNITIVE_ORGANISM` — Cognitive Integration Plane

## Role

Integrates AMOS cognitive subsystems.

Potential subsystems include:

```text
perception
attention
working cognition
reasoning
hypothesis field
uncertainty
metacognition
memory interface
mode interface
expression
```

Conceptually:

```text
INPUT
↓
PERCEPTION
↓
ATTENTION
↓
WORKING FIELD
↓
HYPOTHESES
↓
REASONING
↓
METACOGNITION
↓
OUTPUT / ACTION PROPOSAL
```

## Epistemic boundary

This is an architectural model.

It does not establish literal biological cognition, subjective consciousness, or embodiment.

---

# 11. `06_AGENTS` — Worker Plane

## Role

Contains role-scoped workers.

Examples may include:

```text
EnvironmentScan_Agent
Executor_Agent
Investment_Agent
```

Agent responsibility:

```text
ROLE
+
SCOPE
+
CAPABILITY
+
INPUT CONTRACT
+
OUTPUT CONTRACT
```

Authority must remain external or explicitly granted.

Hard law:

```text
AGENT
!=
AUTHORITY
```

---

# 12. `07_SKILLS` — Reusable Procedure Plane

## Role

Contains reusable bounded procedures.

A skill should generally define:

```text
trigger
goal
prerequisites
decision gates
steps
verification
pitfalls
```

Boundary:

```text
AGENT
!=
SKILL
```

An agent is a role-oriented worker.

A skill is a reusable procedure.

---

# 13. `08_WORKFLOWS` — Orchestration Graph Plane

## Role

Contains multi-step orchestration structures.

Typical topology:

```text
TRIGGER
↓
PRECONDITION
↓
STAGE A
↓
STAGE B
↓
VALIDATION
↓
AUTHORITY CHECKPOINT
↓
OUTPUT
```

Boundary:

```text
SKILL
!=
WORKFLOW
```

A skill is reusable procedure logic.

A workflow coordinates multiple steps or components.

---

# 14. `09_PROTOCOLS` — Interaction Contract Plane

## Role

Defines contracts between independently owned components.

Candidate protocol families:

```text
agent handoff
tool invocation
authority request
commit
rollback
state transition
knowledge promotion
provenance propagation
```

Boundary:

```text
WORKFLOW
!=
PROTOCOL
```

Workflow defines orchestration.

Protocol defines interaction semantics.

---

# 15. `10_MEMORY` — Memory Plane

## Role

Stores remembered information used by cognition and runtime.

Candidate classes:

```text
working memory
episodic memory
case memory
negative memory
validated long-term memory
```

Hard boundaries:

```text
MEMORY
!=
CANON
```

```text
MEMORY
!=
VALIDATED KNOWLEDGE
```

```text
REMEMBERED
!=
TRUE
```

---

# 16. `11_KNOWLEDGE` — Knowledge Plane

## Role

Stores evidence, claims, RSCFs, framework knowledge, and validated reusable knowledge.

Potential progression:

```text
SOURCE
↓
SOURCE_CLAIM
↓
EVIDENCE
↓
DERIVED CLAIM
↓
VALIDATION
↓
VALIDATED KNOWLEDGE
```

Possible knowledge classes:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN/GAP
```

---

# 17. `12_STATE` — State Plane

## Role

Stores system state.

State classes may include:

```text
AUTHORITATIVE
WORKING
SHADOW
PENDING
RECOVERY
QUARANTINED
```

Boundary:

```text
KNOWLEDGE
!=
STATE
```

Knowledge describes what is believed or established.

State describes the current system condition.

---

# 18. `13_MODELS` — Model Plane

## Role

Contains explicit models used by AMOS components.

Potential model classes:

```text
foundation models
domain models
calibration models
prediction models
decision-support models
simulation models
```

Hard boundary:

```text
MODEL
!=
AUTHORITY
```

and:

```text
MODEL OUTPUT
!=
OBSERVATION
```

---

# 19. `14_TOOLS` — Tool / Effector Plane

## Role

Contains connectors and external effectors.

Examples:

```text
filesystem
database
API
browser
shell
external services
device connectors
```

Critical boundary:

```text
TOOL
!=
PERMISSION
```

Tool availability establishes capability only.

---

# 20. `15_INTERFACES` — Interface Plane

## Role

Defines system access surfaces.

Potential interfaces:

```text
USER
API
CLI
MCP
UI
AGENT
SERVICE
```

Conceptual map:

```text
EXTERNAL ACTOR
↓
INTERFACE
↓
RUNTIME
↓
AMOS SYSTEM
```

Interfaces should not silently bypass control-plane authority.

---

# 21. `16_SCHEMAS` — Typed Schema Plane

## Role

Defines machine-readable object contracts.

Priority schema families:

```text
AGENT
RSCF
STATE
AUTHORITY
MODE
TOOL
PROTOCOL
EXECUTION_REQUEST
EXECUTION_RECEIPT
PROVENANCE
```

Schemas provide structure.

They do not establish truth.

```text
SCHEMA VALID
!=
SEMANTICALLY CORRECT
```

---

# 22. `17_OBSERVABILITY` — Observability Plane

## Role

Makes runtime behavior inspectable.

Substrates:

```text
logs
traces
metrics
events
health
audit records
provenance diagnostics
failure diagnostics
```

Boundary:

```text
OBSERVED
!=
CORRECT
```

Observability provides evidence for validation.

---

# 23. `18_SECURITY` — Security Plane

## Role

Protects AMOS identities, capabilities, data, state, tools, and interfaces.

Candidate responsibilities:

```text
authentication
authorization
secrets
threat model
input validation
execution isolation
tool permissions
supply-chain integrity
provenance integrity
```

Security is cross-cutting.

It does not belong exclusively at the external boundary.

---

# 24. `19_TESTS` — Verification Plane

## Role

Contains verification assets.

Testing hierarchy:

```text
UNIT
↓
INTEGRATION
↓
REGRESSION
↓
PROPERTY
↓
ADVERSARIAL
↓
FAILURE / RECOVERY
↓
RUNTIME VERIFICATION
```

Hard boundary:

```text
TEST PASS
!=
UNIVERSAL PROOF
```

Every test result inherits its scope.

---

# 25. `20_OPERATIONS` — Operations Plane

## Role

Contains operational lifecycle infrastructure.

Candidate areas:

```text
deployment
release
migration
runbooks
incident handling
backup
restore
rollback
recovery
health procedures
```

Operations governs the transition between architecture and sustained execution.

---

# 26. `21_DOMAINS` — Domain Adapter Plane

## Role

Contains domain-specific adapters and mappings.

Conceptual topology:

```text
DOMAIN INPUT
↓
DOMAIN ADAPTER
↓
AMOS CORE CONTRACT
↓
AMOS SYSTEM
↓
DOMAIN OUTPUT
```

Hard rule:

```text
DOMAIN SPECIALIZATION
!=
CORE LAW
```

Domain-specific assumptions should not silently leak into the universal core.

---

# 27. `22_RESEARCH` — Research Plane

## Role

Contains:

```text
papers
experiments
external evidence
hypotheses
exploratory models
benchmarks
research notes
```

Boundary:

```text
RESEARCH
!=
CANON
```

Research may inform canon promotion.

It does not automatically become canon.

---

# 28. `23_OPERATING_MODEL` — Human Governance Plane

## Role

Defines organizational stewardship.

Potential areas:

```text
roles
decision rights
review forums
promotion authority
incident authority
canon admission authority
deprecation authority
```

Boundary:

```text
ORGANIZATIONAL AUTHORITY
!=
RUNTIME AUTHORITY
```

The two may interact but should remain explicitly modeled.

---

# 29. `24_ARCHIVE` — Historical Plane

## Role

Preserves:

```text
legacy
deprecated
superseded
historical
migration artifacts
```

Archive law:

```text
ARCHIVE
!=
DELETE
```

Historical provenance should remain reconstructable where required.

---

# 30. `25_COGNITIVE_MATRIX` — Cognitive Relationship Plane

## Role

Maps cross-component cognitive relationships.

Examples:

```text
agent ↔ mode
mode ↔ memory
attention ↔ reasoning
knowledge ↔ cognition
state ↔ hypothesis
model ↔ decision
domain ↔ agent
```

Boundary:

```text
RELATION MAP
!=
SOURCE OF TRUTH
```

The matrix references authoritative artifacts rather than duplicating them.

---

# 31. Core Authority Flow

Conceptual authority flow:

```text
CANON
↓ constrains
KERNEL
↓ provides deterministic enforcement primitives
CONTROL PLANE
↓ grants / checks authority
RUNTIME
↓ invokes
WORKERS / TOOLS
↓ may produce
EXTERNAL EFFECT
```

Critical firewall:

```text
CAPABILITY
!=
AUTHORITY
```

No lower plane acquires authority merely because it can perform an operation.

---

# 32. Information Flow

Typical information path:

```text
INTERFACE
↓
RUNTIME
↓
COGNITIVE ORGANISM
↓
AGENT / SKILL / WORKFLOW
↓
KNOWLEDGE / MEMORY / MODELS
↓
RESULT
↓
VALIDATION
↓
INTERFACE
```

Effectful path adds:

```text
AUTHORITY CHECK
↓
COMMIT
↓
TOOL
↓
EXTERNAL EFFECT
```

---

# 33. Knowledge Flow

```text
SOURCE
↓
RESEARCH / INGEST
↓
KNOWLEDGE
↓
RSCF / CLAIM STRUCTURE
↓
VALIDATION
↓
REUSABLE KNOWLEDGE
```

Potential canon promotion:

```text
VALIDATED KNOWLEDGE
↓
GOVERNANCE
↓
CANON CANDIDATE
↓
CANON
```

This is governed promotion, not automatic escalation.

---

# 34. State Flow

Conceptual state path:

```text
AUTHORITATIVE STATE
↓
WORKING STATE
↓
PROPOSED CHANGE
↓
VALIDATION
↓
AUTHORITY
↓
COMMIT
↓
NEW AUTHORITATIVE STATE
```

Failure branch:

```text
VALIDATION FAILURE
or
COMMIT FAILURE
↓
RECOVERY / QUARANTINE / ROLLBACK
```

---

# 35. Provenance Flow

Provenance should travel with consequential information:

```text
SOURCE
↓
CLAIM
↓
DERIVATION
↓
DECISION
↓
ACTION
↓
RECEIPT
```

The desired property is:

```text
OUTPUT
→ ancestry
→ dependencies
→ source
```

where required by scope and governance.

---

# 36. RSCF Topology

Conceptually:

```text
CLAIM
├── PREMISES
├── EVIDENCE
├── PROVENANCE
├── DEPENDENCIES
├── SCOPE
├── REGIME
├── FRESHNESS
├── COMPETING HYPOTHESES
├── FALSIFIERS
└── CONFIDENCE CEILING
```

RSCFs primarily belong to knowledge/reasoning structures but may be consumed across multiple planes.

---

# 37. H/M/L Knowledge Topology

AMOS knowledge retrieval may be organized fractally:

```text
H — DOMAIN
↓
M — SUBSYSTEM
↓
L — DETAIL
↓
RAW EVIDENCE
```

Default principle:

```text
LOAD SMALLEST SUFFICIENT DEPENDENCY PATH
```

Raw evidence should not be loaded unless required to alter the answer or verify a load-bearing premise.

---

# 38. Agent–Skill–Workflow Relationship

```text
AGENT
=
ROLE-BASED WORKER

SKILL
=
REUSABLE PROCEDURE

WORKFLOW
=
MULTI-STEP ORCHESTRATION
```

Typical relation:

```text
AGENT
↓ invokes
SKILL
↓ participates in
WORKFLOW
```

But none of these relationships are mandatory in every case.

---

# 39. Agent–Tool Relationship

```text
AGENT
↓ requests capability
RUNTIME
↓ evaluates route
CONTROL PLANE
↓ checks authority
TOOL
↓ performs effect
```

Preferred architecture avoids:

```text
AGENT
────────────→ TOOL
```

for consequential actions when that path bypasses authority controls.

---

# 40. Model Relationship

Models may support:

```text
COGNITION
AGENTS
SKILLS
WORKFLOWS
DOMAIN ADAPTERS
```

But:

```text
MODEL
↓ informs
DECISION
```

not:

```text
MODEL
=
DECISION AUTHORITY
```

---

# 41. Memory Relationship

Memory may support:

```text
RUNTIME
COGNITION
AGENTS
WORKFLOWS
```

Memory writes should preserve appropriate:

```text
source
time
scope
provenance
confidence
validation state
```

when material.

---

# 42. Schema Relationship

Schemas type objects crossing system boundaries.

Conceptually:

```text
PRODUCER
↓
SCHEMA
↓
PROTOCOL
↓
CONSUMER
```

This reduces silent semantic drift.

---

# 43. Security Relationship

Security overlays:

```text
INTERFACES
RUNTIME
CONTROL PLANE
AGENTS
TOOLS
STATE
MEMORY
KNOWLEDGE
OPERATIONS
```

Security therefore behaves as a cross-cutting enforcement plane.

---

# 44. Observability Relationship

Observability consumes signals from:

```text
RUNTIME
CONTROL PLANE
AGENTS
TOOLS
STATE
SECURITY
OPERATIONS
```

and produces:

```text
logs
traces
metrics
health
audit evidence
```

---

# 45. Test Relationship

Tests validate bounded claims about:

```text
KERNEL
CONTROL PLANE
RUNTIME
COGNITION
AGENTS
SKILLS
WORKFLOWS
PROTOCOLS
STATE
MODELS
TOOLS
INTERFACES
SECURITY
OPERATIONS
```

Testing is cross-plane.

---

# 46. Operations Relationship

Operations consumes:

```text
runtime state
observability
security events
test evidence
release artifacts
```

and governs:

```text
deploy
migrate
recover
rollback
restore
incident response
```

---

# 47. Research-to-Canon Firewall

Required conceptual boundary:

```text
RESEARCH
↓
EVIDENCE
↓
VALIDATION
↓
GOVERNANCE
↓
CANON
```

Forbidden shortcut:

```text
RESEARCH
────────→
CANON
```

without admission governance.

---

# 48. Archive Relationship

Supersession path:

```text
ACTIVE ARTIFACT
↓
SUPERSEDED
↓
MIGRATION
↓
ARCHIVE
```

Archive retains lineage.

Active runtime dependencies should not silently point to deprecated artifacts.

---

# 49. Cognitive Matrix Relationship

The cognitive matrix should consume references from:

```text
COGNITIVE ORGANISM
AGENTS
MEMORY
KNOWLEDGE
MODELS
DOMAINS
STATE
```

but not duplicate their canonical definitions.

---

# 50. Plane Ownership Matrix

| Plane                   | Primary ownership                   |
| ----------------------- | ----------------------------------- |
| `00_ROOT`               | global architecture/navigation      |
| `01_CANON`              | authoritative definitions           |
| `02_KERNEL`             | deterministic primitives            |
| `03_CONTROL_PLANE`      | authority/governance                |
| `04_RUNTIME`            | execution orchestration             |
| `05_COGNITIVE_ORGANISM` | cognitive integration               |
| `06_AGENTS`             | role-based workers                  |
| `07_SKILLS`             | reusable procedures                 |
| `08_WORKFLOWS`          | orchestration graphs                |
| `09_PROTOCOLS`          | interaction contracts               |
| `10_MEMORY`             | remembered information              |
| `11_KNOWLEDGE`          | claims/evidence/validated knowledge |
| `12_STATE`              | system state                        |
| `13_MODELS`             | model registry                      |
| `14_TOOLS`              | effectors/connectors                |
| `15_INTERFACES`         | access surfaces                     |
| `16_SCHEMAS`            | typed contracts                     |
| `17_OBSERVABILITY`      | traces/metrics/logs                 |
| `18_SECURITY`           | protection/enforcement              |
| `19_TESTS`              | verification                        |
| `20_OPERATIONS`         | deployment/recovery                 |
| `21_DOMAINS`            | domain adapters                     |
| `22_RESEARCH`           | experiments/external evidence       |
| `23_OPERATING_MODEL`    | human governance                    |
| `24_ARCHIVE`            | historical lineage                  |
| `25_COGNITIVE_MATRIX`   | relationship topology               |

---

# 51. Critical Separation Laws

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

MEMORY != KNOWLEDGE

KNOWLEDGE != STATE

MODEL != AUTHORITY

TOOL != PERMISSION

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

RESEARCH != CANON

ARCHIVE != ACTIVE STATE

OBSERVABILITY != VALIDATION

TEST PASS != UNIVERSAL PROOF
```

These boundaries prevent responsibility collapse.

---

# 52. External Effect Boundary

External effects should conceptually occur only after required validation and authority checks.

```text
INTERNAL PROPOSAL
↓
VALIDATION
↓
AUTHORITY
↓
COMMIT PREPARATION
↓
TOOL
↓
EXTERNAL EFFECT
↓
VERIFICATION
↓
RECEIPT
```

For irreversible or high-impact actions, governance requirements increase.

---

# 53. Failure Boundary

Failure should remain typed.

Examples:

```text
VALIDATION_FAILED
AUTHORITY_DENIED
DEPENDENCY_MISSING
STATE_CONFLICT
TOOL_FAILED
EXTERNAL_EFFECT_UNKNOWN
ROLLBACK_FAILED
PROVENANCE_INVALID
SECURITY_BLOCKED
```

Do not collapse all failures into:

```text
ERROR
```

when recovery semantics differ.

---

# 54. Recovery Topology

```text
FAILURE
↓
CLASSIFY
↓
IDENTIFY AFFECTED DEPENDENCIES
↓
PRESERVE UNAFFECTED STATE
↓
INVALIDATE DEPENDENTS
↓
ROLLBACK / COMPENSATE / QUARANTINE
↓
REROUTE
↓
REVALIDATE
```

Primary principle:

```text
LOCAL REPAIR
>
GLOBAL RESET
```

when local repair preserves correctness.

---

# 55. v4.4 Fast-Path Relationship

A local execution path may avoid unnecessary broader coordination only when required conditions are established:

```text
DEPENDENCY CLOSURE
∧
PROVENANCE INDEPENDENCE
∧
SCOPE COMPATIBILITY
∧
REGIME COMPATIBILITY
∧
FRESHNESS
∧
NON-CONFLICT
```

Otherwise:

```text
ESCALATE
```

Fast path means reduced unnecessary coordination.

It does not mean reduced integrity.

---

# 56. Mode-System Placement

Mode architecture may interact with:

```text
COGNITIVE_ORGANISM
RUNTIME
AGENTS
SKILLS
WORKFLOWS
MEMORY
KNOWLEDGE
STATE
```

but mode definitions should be explicitly placed according to their semantic role.

A mode directory existing does not establish an implemented mode.

```text
MODE FOLDER
!=
MODE IMPLEMENTATION
```

---

# 57. Repository Placement Rule

Canonical placement follows semantic ownership.

```text
SOURCE LAW
→ 01_CANON

DETERMINISTIC OPERATOR
→ 02_KERNEL

AUTHORITY / POLICY / COMMIT
→ 03_CONTROL_PLANE

EXECUTION HARNESS
→ 04_RUNTIME

COGNITIVE SUBSYSTEM
→ 05_COGNITIVE_ORGANISM

ROLE WORKER
→ 06_AGENTS

REUSABLE PROCEDURE
→ 07_SKILLS

ORCHESTRATION GRAPH
→ 08_WORKFLOWS

INTERACTION CONTRACT
→ 09_PROTOCOLS

MEMORY
→ 10_MEMORY

KNOWLEDGE
→ 11_KNOWLEDGE

STATE
→ 12_STATE

MODEL
→ 13_MODELS

TOOL
→ 14_TOOLS

INTERFACE
→ 15_INTERFACES

SCHEMA
→ 16_SCHEMAS

OBSERVABILITY
→ 17_OBSERVABILITY

SECURITY
→ 18_SECURITY

TEST
→ 19_TESTS

OPERATIONS
→ 20_OPERATIONS

DOMAIN ADAPTER
→ 21_DOMAINS

RESEARCH
→ 22_RESEARCH

ORGANIZATIONAL GOVERNANCE
→ 23_OPERATING_MODEL

LEGACY / SUPERSEDED
→ 24_ARCHIVE

COGNITIVE RELATION MAP
→ 25_COGNITIVE_MATRIX
```

---

# 58. Dependency Direction

Preferred dependency direction follows:

```text
HIGHER-LEVEL CAPABILITY
↓ depends on
LOWER-LEVEL CONTRACT / PRIMITIVE
```

Examples:

```text
AGENT
→ RUNTIME
→ CONTROL_PLANE
→ KERNEL
→ CANON
```

and:

```text
WORKFLOW
→ SKILL / AGENT / PROTOCOL
```

Cross-cutting dependencies may legitimately break simple directory-number ordering.

Therefore:

```text
DIRECTORY NUMBER
!=
DEPENDENCY PROOF
```

---

# 59. Source-of-Truth Rule

Each semantic concept should have one authoritative home.

Other locations should reference it.

Preferred:

```text
CANONICAL ARTIFACT
↑
references
↑
MOCs / MAPS / MATRIX / INDEXES
```

Avoid:

```text
COPY A
COPY B
COPY C
```

silently becoming independent authorities.

---

# 60. Neural Network Relationship

`NEURAL_NETWORK.md` provides graph connectivity.

`SYSTEM_MAP.md` provides semantic topology.

Therefore:

```text
NEURAL_NETWORK
=
NAVIGATION / GRAPH HUB

SYSTEM_MAP
=
SYSTEM RESPONSIBILITY MAP
```

They are related but not interchangeable.

---

# 61. Full Tree Relationship

```text
SYSTEM_MAP
=
WHAT THE PLANES MEAN
```

```text
FULL_TREE
=
WHERE EXPECTED ARTIFACTS LIVE
```

The system map should remain relatively stable even when the detailed tree grows.

---

# 62. Dependency Map Relationship

```text
SYSTEM_MAP
=
MACRO TOPOLOGY
```

```text
DEPENDENCY_MAP
=
TYPED DEPENDENCY EDGES
```

A system map should not attempt to duplicate every dependency edge.

---

# 63. Authoritative State Relationship

```text
SYSTEM_MAP
=
EXPECTED STRUCTURAL MODEL
```

```text
AUTHORITATIVE_STATE
=
CURRENT VERIFIED IMPLEMENTATION STATE
```

Therefore:

```text
MAPPED
!=
ACTIVE
```

---

# 64. Roadmap Relationship

```text
SYSTEM_MAP
=
WHERE
```

```text
ROADMAP
=
WHEN / IN WHAT PROMOTION ORDER
```

```text
AUTHORITATIVE_STATE
=
WHAT IS CURRENTLY VERIFIED
```

Together:

```text
SYSTEM_MAP
+
FULL_TREE
+
DEPENDENCY_MAP
+
ROADMAP
+
AUTHORITATIVE_STATE
```

provide the root architectural control surface.

---

# 65. MOC Relationship

Each major plane should have a local MOC or index.

Conceptually:

```text
ROOT MOC
↓
PLANE MOC
↓
SUBSYSTEM MOC
↓
COMPONENT
```

This supports fractal navigation.

---

# 66. H/M/L Repository Mapping

A practical repository interpretation:

```text
H
=
TOP-LEVEL PLANE

M
=
SUBSYSTEM / CATEGORY

L
=
COMPONENT / DETAIL
```

Example:

```text
06_AGENTS
↓
MONEY_SYSTEM
↓
Investment_Agent
```

This is a navigation model and should not be treated as a universal semantic identity rule.

---

# 67. Structural Invariants

```text
SM01 EACH TOP-LEVEL PLANE HAS ONE PRIMARY ROLE

SM02 CANON DOES NOT EXECUTE

SM03 KERNEL DOES NOT OWN POLICY AUTHORITY

SM04 CONTROL PLANE DOES NOT REPLACE RUNTIME

SM05 RUNTIME DOES NOT BECOME CANON

SM06 COGNITION DOES NOT IMPLY AUTHORITY

SM07 AGENTS DO NOT SELF-GRANT AUTHORITY

SM08 SKILLS DO NOT BECOME AGENTS BY CONTAINING LOGIC

SM09 WORKFLOWS DO NOT REPLACE PROTOCOLS

SM10 MEMORY DOES NOT BECOME CANON BY PERSISTENCE

SM11 KNOWLEDGE DOES NOT BECOME STATE

SM12 MODEL OUTPUT DOES NOT BECOME OBSERVATION

SM13 TOOL AVAILABILITY DOES NOT IMPLY PERMISSION

SM14 SCHEMA VALIDITY DOES NOT PROVE SEMANTIC VALIDITY

SM15 OBSERVABILITY DOES NOT PROVE CORRECTNESS

SM16 TEST SUCCESS IS SCOPE-BOUND

SM17 RESEARCH DOES NOT AUTO-PROMOTE TO CANON

SM18 ARCHIVE PRESERVES LINEAGE

SM19 COGNITIVE MATRIX DOES NOT DUPLICATE AUTHORITY

SM20 SYSTEM MAP DOES NOT CLAIM IMPLEMENTATION COMPLETENESS
```

---

# 68. Failure Registry

```text
SM-F001 PLANE_RESPONSIBILITY_COLLISION
SM-F002 DUPLICATE_SOURCE_OF_TRUTH
SM-F003 CANON_IMPLEMENTATION_COLLAPSE
SM-F004 KERNEL_POLICY_COLLAPSE
SM-F005 CONTROL_RUNTIME_COLLAPSE
SM-F006 RUNTIME_COGNITION_COLLAPSE
SM-F007 AGENT_AUTHORITY_LEAK
SM-F008 SKILL_WORKFLOW_COLLAPSE
SM-F009 MEMORY_CANON_COLLAPSE
SM-F010 MEMORY_KNOWLEDGE_COLLAPSE
SM-F011 KNOWLEDGE_STATE_COLLAPSE
SM-F012 MODEL_OBSERVATION_COLLAPSE
SM-F013 TOOL_PERMISSION_COLLAPSE
SM-F014 RESEARCH_CANON_LEAK
SM-F015 ARCHIVE_ACTIVE_DEPENDENCY
SM-F016 MATRIX_AUTHORITY_DUPLICATION
SM-F017 BROKEN_CROSS_PLANE_REFERENCE
SM-F018 UNKNOWN_PLACEMENT
SM-F019 SYSTEM_MAP_STATE_OVERCLAIM
SM-F020 UNGOVERNED_EXTERNAL_EFFECT
```

---

# 69. Map Integrity Checks

A repository audit should eventually verify:

```text
all top-level planes exist
all planes have an index/MOC
all planes have declared ownership
all major artifacts have canonical placement
cross-plane references resolve
no duplicate authoritative definitions
no active dependencies point only to archive
authority paths are explicit
external-effect paths are governed
unknown placement is surfaced
```

---

# 70. Current Evidence Boundary

This map defines the intended AMOS OS topology.

It does **not** by itself establish:

```text
every directory exists
every directory is populated
every placeholder is filled
every registry is active
every component is implemented
every component is integrated
every test passes
every authority path exists
every recovery path works
every runtime subsystem is operational
```

Those remain audit questions.

Conclusion:

```text
SYSTEM TOPOLOGY
=
DEFINED

IMPLEMENTATION COMPLETENESS
=
UNKNOWN/GAP
```

---

# 71. System Map RSCF Node

```yaml
node_id: AMOS_OS_SYSTEM_MAP

node_type: system_map

domain: AMOS_OS

functional_type:
  - TOPOLOGY
  - RESPONSIBILITY_MAP
  - PLANE_BOUNDARY_MAP

lifecycle_stage:
  ACTIVE_MAP

origin_architect:
  Trang Phan

steward:
  Trang Phan

claim_class:
  AMOS_MODEL

claim: >
  AMOS OS is organized into distinct authoritative, deterministic,
  governance, runtime, cognitive, capability, persistence, support,
  domain, research, organizational, historical, and relationship planes
  whose responsibilities should remain explicitly separated.

premises:
  - semantic responsibilities require explicit ownership
  - capability and authority must remain separate
  - persistent memory, knowledge, and state are distinct
  - runtime execution is distinct from control-plane governance
  - repository topology does not establish implementation completeness

dependencies:
  - "ARCHITECTURE"
  - "PLACEMENT_RULES"
  - "DEPENDENCY_MAP"
  - "FULL_TREE"

hard_invariants:
  - CANON != KERNEL
  - KERNEL != CONTROL_PLANE
  - CONTROL_PLANE != RUNTIME
  - RUNTIME != COGNITION
  - ORGAN != AGENT
  - AGENT != SKILL
  - SKILL != WORKFLOW
  - WORKFLOW != PROTOCOL
  - MEMORY != CANON
  - KNOWLEDGE != STATE
  - MODEL != AUTHORITY
  - TOOL != PERMISSION
  - CAPABILITY != AUTHORITY
  - PROPOSAL != COMMIT
  - SYSTEM_MAP != AUTHORITATIVE_STATE

does_not_establish:
  - implementation completeness
  - runtime availability
  - test success
  - empirical validity
  - production readiness

falsifiers:
  - approved root architecture changes plane ownership
  - canonical placement rules supersede this topology
  - repository governance formally introduces or removes a top-level plane

confidence_ceiling:
  topology_model: high
  implementation_state: UNKNOWN/GAP
```

---

# 72. Compact System Map

```text
                         AMOS OS
                            │
        ┌───────────────────┼────────────────────┐
        │                   │                    │
   DEFINITION           EXECUTION            SUPPORT
        │                   │                    │
   ┌────┴────┐       ┌──────┴──────┐      ┌──────┴─────────┐
 CANON    KERNEL   CONTROL       RUNTIME   SCHEMAS       SECURITY
                         │            │     OBSERVABILITY  TESTS
                         │            │     OPERATIONS
                         │            │
                         │      COGNITIVE ORGANISM
                         │            │
                         │     ┌──────┼──────┐
                         │   AGENTS SKILLS WORKFLOWS
                         │            │
                         │        PROTOCOLS
                         │
                 ┌───────┴───────────────┐
                 │                       │
             PERSISTENCE              EFFECTORS
                 │                       │
          MEMORY / KNOWLEDGE        TOOLS / MODELS
          STATE / MODELS            INTERFACES
                                         │
                                  EXTERNAL EFFECTS
```

Additional overlays:

```text
DOMAINS
RESEARCH
OPERATING MODEL
ARCHIVE
COGNITIVE MATRIX
```

---

# 73. Final System Law

The system map compresses to:

```text
DEFINE
↓
CONSTRAIN
↓
GOVERN
↓
EXECUTE
↓
COGNIZE
↓
DELEGATE
↓
ACT
↓
OBSERVE
↓
VERIFY
↓
RECOVER
```

while preserving:

```text
MEMORY
KNOWLEDGE
STATE
PROVENANCE
SECURITY
SCHEMAS
```

across the lifecycle.

The primary invariant is:

> **Every AMOS OS artifact should have one clear semantic home, and no plane should silently acquire the authority, truth status, state ownership, or execution responsibility of another plane merely because it can reference or invoke it.**

The second invariant is:

> **The system map defines architecture and responsibility boundaries; it does not convert planned structure into evidence of implementation.**

---

# 74. Changelog

## v2.0.0 — 2026-08-25

Expanded the root placeholder into the AMOS OS system topology map.

Added:

* plane classification;
* root architectural spine;
* cross-cutting substrate topology;
* responsibilities for all 26 top-level planes;
* authority flow;
* information flow;
* knowledge flow;
* state flow;
* provenance flow;
* RSCF topology;
* H/M/L topology;
* agent/skill/workflow relationships;
* tool and authority firewall;
* memory/model/schema/security/observability relationships;
* research-to-canon firewall;
* archive and cognitive-matrix boundaries;
* plane ownership matrix;
* external-effect boundary;
* failure and recovery topology;
* v4.4 fast-path boundary;
* mode-system placement;
* source-of-truth rule;
* root-document relationships;
* H/M/L repository interpretation;
* 20 structural invariants;
* 20 system-map failure classes;
* map-integrity checks;
* master RSCF node.

## v1.0.0 — 2026-08-25

Initial placeholder established the 26-plane repository topology and the boundary:

```text
SYSTEM MAP
!=
IMPLEMENTATION PROOF
```

---

**Related:** README|AMOS OS · 00_ROOT_MOC|MOC · NEURAL_NETWORK|Neural Network · ARCHITECTURE|Architecture · FULL_TREE|Full Tree · DEPENDENCY_MAP|Dependency Map · AUTHORITATIVE_STATE|Authoritative State · 00_ROOT_NAMING_STANDARD|Naming Standard · PLACEMENT_RULES|Placement Rules · ROADMAP|Roadmap · CANON_MAP|CANON · KERNEL_MAP|KERNEL · CONTROL_PLANE_MAP|CONTROL_PLANE · RUNTIME_MAP|RUNTIME · COGNITIVE_ORGANISM_MAP|COGNITIVE_ORGANISM · AGENT_MAP|AGENTS · SKILL_MAP|SKILLS · WORKFLOW_MAP|WORKFLOWS · PROTOCOL_MAP|PROTOCOLS · MEMORY_MEMORY_MAP|MEMORY · AMOS_FULL_BRAIN_OS_ARCHITECTURE|KNOWLEDGE · STATE_STATE_MAP|STATE · MODEL_MAP|MODELS · TOOL_MAP|TOOLS · INTERFACE_MAP|INTERFACES · SCHEMA_MAP|SCHEMAS · OBSERVABILITY_OBSERVABILITY_MAP|OBSERVABILITY · SECURITY_MAP|SECURITY · TEST_MAP|TESTS · OPERATIONS_MAP|OPERATIONS · DOMAIN_ALIAS_MAP|DOMAINS · INDEX_RESEARCH_README|RESEARCH · OPERATING_MODEL|OPERATING_MODEL · LEGACY_ARCHIVE_README|ARCHIVE · COGNITIVE_MATRIX_ARCHITECTURE|COGNITIVE_MATRIX

```
```

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: system_map_v1
node_type: note
path: 00_ROOT/SYSTEM_MAP_v1.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[00_COSMO_BRAIN_MOC]]
