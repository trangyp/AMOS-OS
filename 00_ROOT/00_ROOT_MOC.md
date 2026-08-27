---
type: note
aliases:
- AMOS MOC
- AMOS OS MOC
- AMOS Master Index
- AMOS Root Map
- AMOS OS Navigation Hub
- MOC
amos_core_target: v4.4
artifact_id: AMOS-OS-MOC
canon_group: tech-ai
canon_type: navigation
conclusion_class: SOURCE_CLAIM / AMOS_MODEL
created: 2026-08-25
document_version: 2.0.0
moc_version: 1.0.0
name: AMOS_OS_MOC
origin_architect: Trang Phan
related:
- '[[00_HOME]]'
- '[[ARCHITECTURE]]'
- '[[FULL_TREE]]'
- '[[SYSTEM_MAP]]'
- '[[AUTHORITATIVE_STATE]]'
- '[[DEPENDENCY_MAP]]'
- 'NAMING_STANDARD'
- '[[PLACEMENT_RULES]]'
- '[[ROADMAP]]'
- '[[RSCF_NODE_INDEX]]'
- 'GMEF'
- '[[HML_CANON]]'
- 'COSMO_BRAIN_MOC|00 Cosmo Brain MOC'
- 'KNOWLEDGE_MOC|11_KNOWLEDGE MOC'
- '[[AMOS_OBSIDIAN_LINKING_PLUGINS]]'
- '[[AMOS_LAYER_MAPS]]'
rscf_state: derived
scope:
- AMOS_OS
- root_navigation
- architecture_navigation
- dependency_navigation
- governance_navigation
- runtime_navigation
- cognitive_navigation
- knowledge_navigation
status: ACTIVE_MOC
steward: Trang Phan
tags: [amos, amos_os, root, amos-os, moc, map-of-content, root-index, architecture, system-map, dependency-map, navigation, canon, kernel, control-plane, runtime, cognitive-organism, agents, skills, workflows, protocols, memory, knowledge, state, models, tools, interfaces, schemas, observability, security, tests, operations, domains, research, operating-model, archive, cognitive-matrix, rscf, gmef, hml, provenance, authority, lifecycle, failure-recovery, canon-group/tech-ai, canon/navigation, rscf/claim, rscf/provenance, rscf/state/derived, topic/amos-os, topic/moc, topic/root-navigation]
title: AMOS OS — Master Map of Content
updated: 2026-08-26
---



# AMOS OS — Master Map of Content

**Origin architect / steward:** Trang Phan

> **Status:** `ACTIVE_MOC`  
> **AMOS_CORE target:** `v4.4`  
> **Conclusion class:** `SOURCE_CLAIM / AMOS_MODEL`

---

# Purpose

This MOC is the root navigation and structural orientation layer for `AMOS_OS`.

It defines where to find:

- system architecture;
- canon;
- kernel logic;
- control-plane authority;
- runtime;
- cognitive-organism components;
- agents;
- reusable skills;
- workflows;
- protocols;
- memory;
- knowledge;
- state;
- models;
- tools;
- interfaces;
- schemas;
- observability;
- security;
- tests;
- operations;
- domains;
- research;
- operating-model material;
- archive lineage;
- cognitive matrix integration.

It also defines the minimum contract expected of every major AMOS component:

```text
ROLE
+
INTERFACES
+
DEPENDENCIES
+
INVARIANTS
+
AUTHORITY
+
PROVENANCE
+
TESTS
+
FAILURE
+
RECOVERY
```

The Full Brain OS source is treated as a structural orchestration specification, not evidence of literal consciousness, embodiment, or autonomous authority. 

---

# Hard Boundary

```text
CAPABILITY != AUTHORITY
UNKNOWN/GAP != PASS
MODEL != OBSERVATION
SOURCE_CLAIM != VERIFIED
IMPLEMENTED != VALIDATED
REPOSITORY_PRESENCE != LIVE_RUNTIME
```

These distinctions are non-negotiable.

---

# 1. Root Navigation

```text
AMOS_OS/
│
├── 00_ROOT
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

# 2. Root Files

## [[ARCHITECTURE]]

Defines:

```text
system boundary
layer ownership
H/M/L decomposition
control plane vs worker plane
runtime boundaries
failure/recovery architecture
authority separation
```

Use when asking:

> How is AMOS OS structurally organized?

---

## [[AUTHORITATIVE_STATE]]

Defines:

```text
what exists
what is implemented
what is tested
what is active
what is deprecated
what remains UNKNOWN/GAP
```

Use when asking:

> What is currently real in the repository/runtime?

---

## [[DEPENDENCY_MAP]]

Defines:

```text
component dependencies
load-bearing prerequisites
optional dependencies
cross-layer dependencies
dependency closure
failure propagation
```

Use when asking:

> What depends on what?

---

## [[SYSTEM_MAP]]

Defines high-level system areas and their ownership.

Use when asking:

> What are the major subsystems?

---

## [[FULL_TREE]]

Defines filesystem placement.

Use when asking:

> Where should this artifact live?

---

## [[PLACEMENT_RULES]]

Defines repository placement constraints.

Use when asking:

> Which folder owns this artifact?

---

## NAMING_STANDARD

Defines naming, identifiers, versions, aliases, and compatibility rules.

Use when asking:

> How should this component be named and versioned?

---

## [[ROADMAP]]

Defines future progression.

Use when asking:

> What is planned but not yet implemented?

---


### Other root artifacts

- [[00_ROOT_ARCHITECTURE]]
- [[00_ROOT_AUDIT]]
- [[00_ROOT_AUTHORIZATION]]
- [[00_ROOT_BOUNDARIES]]
- [[00_ROOT_CHANGE_LOG]]
- [[00_ROOT_CONTRACT]]
- [[00_ROOT_COVERAGE]]
- [[00_ROOT_DEPENDENCIES]]
- [[00_ROOT_GLOSSARY]]
- [[00_ROOT_HISTORY]]
- [[00_ROOT_IDENTITY]]
- [[00_ROOT_INTEGRATION_CHECKLIST]]
- [[00_ROOT_LIFECYCLE]]
- [[00_ROOT_MAP]]
- [[00_ROOT_NAMING_STANDARD]]
- [[00_ROOT_PROVENANCE]]
- [[00_ROOT_README]]
- [[00_ROOT_REGISTRY]]
- [[00_ROOT_RELEASE_NOTES]]
- [[00_ROOT_STATUS]]
- [[00_ROOT_VERSIONING]]
- [[00_COSMO_BRAIN_MOC]]
- [[COGNITIVE_MATRIX_INTEGRATION]]
- [[NEURAL_NETWORK]]
- [[SYSTEM_MAP_V1]]
# 3. Canon Layer

## `01_CANON`

Canonical artifacts define high-governance semantics.

Expected areas may include:

```text
CORE LAWS
H/M/L
COGNITION
CONTROL PLANE
AUTHORITY
PERSISTENCE
PROVENANCE
STATE
FAILURE / RECOVERY
```

Canon establishes:

```text
definitions
invariants
constraints
identity
semantic boundaries
```

Hard rule:

```text
Canon
!=
Implementation
```

A canonical definition may exist even when runtime support remains incomplete.

---


### Key canon indexes

- [[CANON_MAP]]
- [[INDEX_CANON_README]]
- [[AMOS_CORE_LAWS]]
- [[HML_CANON]]
- [[UNIVERSE_CANON_MAP]]
- COGNITION_CANON_MAP
- [[INFRASTRUCTURE_CANON_MAP]]
- [[GLOSSARY_MAP]]
- [[PROVENANCE_CANON_MAP]]
- [[SUPERSESSION_MAP]]
# 4. Kernel Layer

## `02_KERNEL`

The kernel owns constrained computational primitives.

Typical responsibilities:

```text
normalization
logic
RSCF
claim handling
dependency evaluation
provenance operations
state-transition primitives
validation primitives
routing primitives
```

AMOS_CORE lineage progresses from deterministic reasoning through recursive RSCF/HML, provenance topology, persistent provenance, transactional concepts, epoch finality, and proof-based coordination avoidance. This is a preserved architecture lineage, not a claim that every repository component implements all those mechanisms literally.

---


### Key kernel maps

- [[KERNEL_MAP]]
- [[INDEX_KERNEL_README]]
- [[META_LOGIC_MAP]]
- [[COGNITION_MAP]]
- [[CAUSAL_MAP]]
- [[KERNEL_STATE_MAP]]
- [[KERNEL_MEMORY_MAP]]
- [[RISK_REPAIR_MAP]]
- [[KERNEL_AUTHORITY_MAP]]
- [[KERNEL_PROVENANCE_MAP]]
- [[INTEGRATION_MAP]]
# 5. Control Plane

## `03_CONTROL_PLANE`

Control plane owns:

```text
authority
routing
admission
policy
permission
commit gates
risk escalation
mode governance
tool governance
lifecycle governance
```

Hard boundary:

```text
WORKER CAPABILITY
!=
CONTROL-PLANE AUTHORITY
```

A worker may know how to perform an operation without being authorized to commit it.

---


### Key control-plane maps

- [[CONTROL_PLANE_MAP]]
- [[INDEX_CONTROL_PLANE_README]]
- [[TASK_CONTRACT_MAP]]
- [[CAPABILITY_MAP]]
- [[POLICY_MAP]]
- [[CONTROL_PLANE_AUTHORITY_MAP]]
# 6. Runtime

## `04_RUNTIME`

Runtime owns live system evolution:

```text
session
task
step
tick
epoch
active mode
current state
execution trace
commit state
failure state
recovery state
```

Hard rule:

```text
Design
!=
Live Runtime
```

---


### Key runtime maps

- [[RUNTIME_MAP]]
- [[INDEX_RUNTIME_README]]
- [[RUNTIME_RUNTIME_CONTRACT]]
# 7. Cognitive Organism

## `05_COGNITIVE_ORGANISM`

Coordinates higher-order cognition.

Possible subsystems:

```text
perception
attention
working cognition
hypothesis management
memory access
reasoning
metacognition
uncertainty
identity continuity models
expression coordination
```

AMOS Full Brain OS should be interpreted structurally; its declared biological, emotional, somatic, and consciousness-adjacent layers are model lenses unless separately validated. 

---


### Key cognitive organism indexes

- [[COGNITIVE_ORGANISM_MAP]]
- [[INDEX_COGNITIVE_ORGANISM_README]]
- [[INDEX_COGNITIVE_ORGANISM_COGNITIVE_ORGANISM_CONTRACT]]
# 8. Agents

## `06_AGENTS`

Agents are scoped active components.

Every agent should declare:

```yaml
Agent:
  identity:
  role:
  scope:
  inputs:
  outputs:
  dependencies:
  permissions:
  authority:
  memory_policy:
  provenance:
  tests:
  failure_modes:
  recovery:
```

Hard rule:

```text
AgentName
!=
AgentCapability
```

and:

```text
AgentCapability
!=
AgentAuthority
```

---


### Key agents indexes

- [[AGENT_MAP]]
- [[INDEX_AGENTS_README]]
- [[INDEX_AGENTS_AGENT_CONTRACT]]
# 9. Skills

## `07_SKILLS`

Skills encode reusable bounded capability.

Expected skill contract:

```yaml
Skill:
  name:
  version:
  trigger:
  purpose:
  prerequisites:
  source:
  domain_model:
  decision_gates:
  steps:
  verification:
  pitfalls:
  dependencies:
  conclusion_class:
```

Skills should be:

```text
scoped
versioned
composable
provenance-aware
epistemically gated
```

---


### Key skills indexes

- [[SKILL_MAP]]
- [[INDEX_SKILLS_README]]
- [[INDEX_SKILLS_SKILL_CONTRACT]]
# 10. Workflows

## `08_WORKFLOWS`

Workflows coordinate multi-step execution.

Typical pattern:

```text
TRIGGER
↓
PRECONDITIONS
↓
RETRIEVE
↓
TRANSFORM
↓
VALIDATE
↓
COMMIT / EXPORT
↓
VERIFY
↓
STORE LEARNING
```

---


### Key workflows indexes

- [[WORKFLOW_MAP]]
- [[INDEX_WORKFLOWS_README]]
- [[INDEX_WORKFLOWS_WORKFLOW_CONTRACT]]
# 11. Protocols

## `09_PROTOCOLS`

Protocols define interaction and handoff contracts.

Examples:

```text
agent ↔ agent
agent ↔ skill
agent ↔ tool
runtime ↔ control plane
runtime ↔ state
knowledge ↔ provenance
authority ↔ execution
```

A protocol should specify:

```text
message
state
acknowledgement
timeout
retry
failure
commit
rollback
```

---


### Key protocols indexes

- [[PROTOCOL_MAP]]
- [[INDEX_PROTOCOLS_README]]
- [[INDEX_PROTOCOLS_PROTOCOL_CONTRACT]]
# 12. Memory

## `10_MEMORY`

Memory retains experience.

Possible classes:

```text
working
episodic
case
long-term
negative
authority-sensitive
```

Hard boundary:

```text
Memory
!=
Knowledge
```

A remembered claim is not automatically validated.

---


### Key memory indexes

- [[MEMORY_MEMORY_MAP]]
- [[INDEX_MEMORY_README]]
- [[INDEX_MEMORY_MEMORY_CONTRACT]]
# 13. Knowledge

## `11_KNOWLEDGE`

Knowledge contains governed reusable claims.

Every consequential knowledge item should carry:

```yaml
Knowledge:
  claim:
  claim_class:
  source:
  provenance:
  scope:
  regime:
  freshness:
  dependencies:
  competing_claims:
  falsifiers:
  validation_state:
```

Knowledge promotion:

```text
RAW
↓
SOURCE_CLAIM
↓
EVIDENCE
↓
PROVENANCE CHECK
↓
CONTRADICTION CHECK
↓
SCOPE / REGIME CHECK
↓
VALIDATED KNOWLEDGE
```

---


### Key knowledge indexes

- [[KNOWLEDGE_MOC]]
# 14. State

## `12_STATE`

State represents current authoritative runtime/system condition.

Possible classes:

```text
session state
runtime state
agent state
mode state
task state
authority state
model state
commit state
lifecycle state
```

Hard boundary:

```text
State
!=
Memory
!=
Knowledge
```

---


### Key state indexes

- [[STATE_STATE_MAP]]
- [[INDEX_STATE_README]]
- [[INDEX_STATE_STATE_CONTRACT]]
# 15. Models

## `13_MODELS`

Models represent structured interpretations or simulations.

Models should declare:

```text
assumptions
scope
regime
inputs
outputs
dependencies
validity
falsifiers
```

Hard rule:

```text
MODEL
!=
OBSERVATION
```

---


### Key models indexes

- [[MODEL_MAP]]
- [[INDEX_MODELS_README]]
- [[INDEX_MODELS_MODEL_CONTRACT]]
# 16. Tools

## `14_TOOLS`

- [[AMOS_OBSIDIAN_LINKING_PLUGINS]] — Obsidian linking plugin stack and Templater starter (vault/brain surface)

Tools provide deterministic or external capability.

Examples:

```text
filesystem
database
browser
search
compiler
calculator
API
connector
runtime executor
```

Hard rule:

```text
Tool Available
!=
Tool Authorized
```

---


### Key tools indexes

- [[TOOL_MAP]]
- [[INDEX_TOOLS_README]]
- [[INDEX_TOOLS_TOOL_CONTRACT]]
# 17. Interfaces

## `15_INTERFACES`

Interfaces define external boundaries.

Includes:

```text
API
CLI
UI
agent interfaces
tool interfaces
external-system contracts
```

---


### Key interfaces indexes

- [[INTERFACE_MAP]]
- [[INDEX_INTERFACES_README]]
- [[INDEX_INTERFACES_INTERFACE_CONTRACT]]
# 18. Schemas

## `16_SCHEMAS`

Schemas define typed contracts.

Every major schema should declare:

```text
schema ID
version
required fields
optional fields
validation
compatibility
migration rules
```

---


### Key schemas indexes

- [[SCHEMA_MAP]]
- [[INDEX_SCHEMAS_README]]
- [[INDEX_SCHEMAS_SCHEMA_CONTRACT]]
# 19. Observability

## `17_OBSERVABILITY`

Observability provides evidence of runtime behavior.

Owns:

```text
logs
traces
metrics
health
events
audit records
failure diagnostics
provenance diagnostics
```

Hard boundary:

```text
Observed
!=
Correct
```

---


### Key observability indexes

- [[OBSERVABILITY_OBSERVABILITY_MAP]]
- [[INDEX_OBSERVABILITY_README]]
- [[INDEX_OBSERVABILITY_OBSERVABILITY_CONTRACT]]
# 20. Security

## `18_SECURITY`

Security owns:

```text
identity
permission
access
secret handling
tool boundaries
input validation
execution isolation
provenance integrity
supply-chain integrity
```

Core principle:

```text
least privilege
+
bounded scope
+
revocability
+
traceability
```

---


### Key security indexes

- [[SECURITY_MAP]]
- [[INDEX_SECURITY_README]]
- [[INDEX_SECURITY_SECURITY_CONTRACT]]
# 21. Tests

## `19_TESTS`

Testing progression:

```text
unit
↓
integration
↓
regression
↓
property
↓
adversarial
↓
failure/recovery
↓
runtime verification
```

Hard rule:

```text
TestPass
!=
UniversalProof
```

---


### Key tests indexes

- [[TEST_MAP]]
- [[INDEX_TESTS_README]]
- [[INDEX_TESTS_TEST_CONTRACT]]
# 22. Operations

## `20_OPERATIONS`

Operations owns lifecycle execution:

```text
deployment
migration
release
backup
restore
incident handling
maintenance
rollback
promotion
deprecation
```

---


### Key operations indexes

- [[OPERATIONS_MAP]]
- [[INDEX_OPERATIONS_README]]
- [[INDEX_OPERATIONS_OPERATIONS_CONTRACT]]
# 23. Domains

## `21_DOMAINS`

Domain-specific specialization lives here.

Domains may include:

```text
logic
math
physics
biology
cognition
society
economics
law
strategy
engineering
design
ecology
```

AMOS Full Brain OS describes broad coverage across these types of domains, but availability does not mean automatic activation. 

Hard routing rule:

```text
LoadDomain
only if
DomainCanMateriallyChangeOutcome
```

---


### Key domains indexes

- [[DOMAIN_ALIAS_MAP]]
- [[INDEX_DOMAINS_README]]
- [[INDEX_DOMAINS_DOMAIN_ALIAS_CONTRACT]]
# 24. Modes

Mode families typically live inside the domain architecture.

Modes alter runtime behavior without necessarily becoming separate agents.

Examples:

```text
reasoning modes
attention modes
epistemic modes
decision modes
scale modes
world-model modes
recovery modes
freshness modes
lifecycle modes
```

Hard rule:

```text
MODE
!=
AGENT
```

unless explicitly defined as one.

---

# 25. Research

## `22_RESEARCH`

Research contains candidate or experimental work.

Research may contain:

```text
candidate laws
new equations
experimental models
hypotheses
prototype engines
benchmark experiments
unresolved theory
```

Hard boundary:

```text
Research
!=
Canon
```

Promotion requires validation.

---


### Key research indexes

- [[RESEARCH_RESEARCH_MAP]]
- [[INDEX_RESEARCH_README]]
- [[INDEX_RESEARCH_RESEARCH_CONTRACT]]
# 26. Operating Model

## `23_OPERATING_MODEL`

Defines how humans and system governance interact.

Possible contents:

```text
roles
responsibilities
decision rights
authority
review cadence
change control
maintenance
stewardship
```

---


### Key operating model indexes

- [[OPERATING_MODEL_MAP]]
- [[INDEX_OPERATING_MODEL_README]]
- [[INDEX_OPERATING_MODEL_OPERATING_MODEL_CONTRACT]]
# 27. Archive

## `24_ARCHIVE`

Archive preserves superseded lineage.

Includes:

```text
old versions
deprecated architecture
retired components
migration records
historical canon
legacy runtime
```

Hard rule:

```text
Archived
!=
Active
```

---


### Key archive indexes

- [[ARCHIVE_MAP]]
- [[INDEX_ARCHIVE_README]]
- [[INDEX_ARCHIVE_ARCHIVE_CONTRACT]]
# 28. Cognitive Matrix

## `25_COGNITIVE_MATRIX`

Cross-links cognitive components.

May map:

```text
agents
modes
attention
memory
state
knowledge
hypotheses
models
domains
reasoning
```

It is a relationship map, not an unrestricted second ontology.

---


### Key cognitive matrix indexes

- [[COGNITIVE_MATRIX_MAP]]
- [[INDEX_COGNITIVE_MATRIX_README]]
- [[INDEX_COGNITIVE_MATRIX_COGNITIVE_MATRIX_CONTRACT]]
# 29. H/M/L Map

AMOS uses recursive H/M/L decomposition.

```text
H
=
governing law
mission
architecture
canon
macro constraints

M
=
kernel
control plane
runtime
agents
protocols
translation layers

L
=
events
tool calls
state changes
messages
individual reasoning operations
```

Hard rule:

```text
Local optimization
must not
damage M or H integrity.
```

---

# 30. Dependency Rule

A component may operate locally only when its load-bearing dependency closure is valid.

```text
LOCAL EXECUTION ALLOWED
iff
DEPENDENCY CLOSURE
∧ SCOPE COMPATIBLE
∧ REGIME COMPATIBLE
∧ FRESHNESS VALID
∧ PROVENANCE ACCEPTABLE
∧ NO MATERIAL CONFLICT
```

Otherwise:

```text
ESCALATE
```

---

# 31. Epistemic Classes

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

Hard rule:

```text
UNKNOWN/GAP
!=
PASS
```

---

# 32. Provenance Rule

Consequential claims should retain:

```text
claim
source
source ancestry
dependencies
scope
regime
freshness
falsifiers
```

Hard boundary:

```text
10 descendants of 1 source
!=
10 independent sources
```

---

# 33. RSCF

Important conclusions should conceptually carry:

```yaml
RSCF:
  claim:
  claim_class:
  premises:
  evidence:
  provenance:
  dependencies:
  scope:
  regime:
  freshness:
  competing:
  falsifiers:
  confidence_ceiling:
```

If a premise fails:

```text
invalidate only dependent descendants
```

---

# 34. GMEF

GMEF governs model or state evolution.

It should preserve:

```text
mutation
proposal
evaluation
admission
rejection
lineage
rollback
```

Hard boundary:

```text
Evolution
!=
Ungoverned Self-Modification
```

---

# 35. Authority Boundary

Every action with external consequence should answer:

```text
WHO authorizes?
WHAT action?
WHICH scope?
UNTIL WHEN?
UNDER WHAT limits?
HOW revoked?
```

Suggested shape:

```yaml
Authority:
  authority_id:
  principal:
  allowed_actions:
  prohibited_actions:
  scope:
  limits:
  valid_from:
  valid_until:
  revoked:
  provenance:
```

---

# 36. Runtime Decision Path

```text
REQUEST
↓
OBJECTIVE
↓
SCOPE
↓
STAKES
↓
DEPENDENCY CLOSURE
↓
MINIMUM REQUIRED EVIDENCE
↓
REASONING
↓
COMPETING HYPOTHESES
↓
VALIDATION
↓
AUTHORITY GATE
↓
DECISION
↓
OPTIONAL EXECUTION
↓
RECEIPT
```

---

# 37. Failure Model

Failure path:

```text
DETECT
↓
CLASSIFY
↓
FREEZE AFFECTED EDGE
↓
INVALIDATE DEPENDENT STATE
↓
ROLL BACK
↓
REROUTE
↓
REVALIDATE
```

Hard rule:

```text
Do not recompute everything
when local repair is sufficient.
```

---

# 38. Recovery Semantics

Preferred recovery is:

```text
local
reversible
dependency-aware
provenance-preserving
```

Possible states:

```text
DEGRADED
RECOVERING
REVALIDATING
RESTORED
QUARANTINED
```

---

# 39. Lifecycle

Recommended artifact lifecycle:

```text
PLACEHOLDER
↓
DRAFT
↓
SOURCE_BOUND
↓
MODEL
↓
IMPLEMENTED
↓
TESTED
↓
VALIDATED_FOR_SCOPE
↓
ACTIVE
↓
DEPRECATED
↓
ARCHIVED
```

Not all artifacts need every stage.

---

# 40. Component Minimum Contract

Every nontrivial AMOS component should eventually answer all of the following.

## Identity

```text
What is it?
Who owns it?
What version?
```

## Role

```text
Why does it exist?
```

## Scope

```text
What is in scope?
What is out of scope?
```

## Interfaces

```text
What enters?
What leaves?
```

## Dependencies

```text
What must exist first?
```

## Invariants

```text
What must always remain true?
```

## Authority

```text
What may it do?
What may it not do?
```

## Provenance

```text
Where did its claims and state come from?
```

## Tests

```text
How do we know it behaves as intended?
```

## Failure

```text
How can it fail?
```

## Recovery

```text
How is valid state restored?
```

---

# 41. Component Template

```yaml
Component:
  artifact_id:
  name:
  version:

  origin_architect:
    Trang Phan

  system:
  category:

  role:

  scope:
    in_scope: []
    out_of_scope: []

  interfaces:
    inputs: []
    outputs: []

  dependencies:
    required: []
    optional: []

  invariants: []

  authority:
    allowed: []
    prohibited: []

  provenance:
    sources: []
    lineage: []

  epistemic_state:

  tests:
    unit: []
    integration: []
    regression: []

  failure_modes: []

  recovery:

  lifecycle_state:

  conclusion_class:
```

---

# 42. MOC Integrity Gates

The MOC is structurally valid only if:

```text
G1 root layers are discoverable
G2 major ownership boundaries are explicit
G3 capability/authority separation is preserved
G4 unknowns remain visible
G5 navigation does not imply implementation
G6 canon and runtime remain distinct
G7 memory/knowledge/state remain distinct
G8 provenance requirements are retained
G9 failure/recovery paths are represented
G10 cross-links resolve or remain explicitly GAP
```

---

# 43. Root Invariants

```text
M01 CAPABILITY != AUTHORITY
M02 UNKNOWN/GAP != PASS
M03 MODEL != OBSERVATION
M04 SOURCE_CLAIM != VERIFIED
M05 IMPLEMENTATION != VALIDATION
M06 REPOSITORY_PRESENCE != RUNTIME
M07 CANON != IMPLEMENTATION
M08 MEMORY != KNOWLEDGE
M09 KNOWLEDGE != STATE
M10 TOOL_ACCESS != TOOL_PERMISSION
M11 AGENT_NAME != CAPABILITY
M12 AGENT_CAPABILITY != AUTHORITY
M13 PROPOSAL != COMMIT
M14 TEST_PASS != UNIVERSAL_PROOF
M15 MULTIPLE_COPIES != INDEPENDENT_EVIDENCE
M16 FAST_PATH != SKIP_VALIDATION
M17 LOCAL_GAIN_CANNOT_BREAK_HIGHER_SCALE_INTEGRITY
M18 FAILED_PREMISE_INVALIDATES_DEPENDENTS_ONLY
M19 STALE_EVIDENCE_REQUIRES_REVALIDATION
M20 IRREVERSIBLE_ACTION_REQUIRES_STRONGER_GOVERNANCE
```

---

# 44. Primary Navigation Paths

## Architecture

```text
ARCHITECTURE
→ SYSTEM_MAP
→ FULL_TREE
```

## Implementation state

```text
AUTHORITATIVE_STATE
→ implementation records
→ tests
```

## Placement

```text
FULL_TREE
→ PLACEMENT_RULES
→ NAMING_STANDARD
```

## Dependencies

```text
DEPENDENCY_MAP
→ component
→ prerequisite
```

## Governance

```text
CONTROL_PLANE_CANON
→ AUTHORITY_CANON
→ security / runtime
```

## Cognition

```text
COGNITION_CANON
→ COGNITIVE_ORGANISM_CANON
→ agents / modes / memory
```

## Evidence

```text
RSCF_NODE_INDEX
→ provenance
→ knowledge
```

---

# 45. Source Boundary

The primary AMOS Full Brain OS source defines a structural orchestration system and explicitly requires uncertainty, explicit assumptions, conservative conclusions, and truthfulness about limits. 

Its operationalization as an AMOS Skill preserves the same boundary: biological, emotional, somatic, and bioelectromagnetic structures should be treated as model lenses unless independently validated. 

The associated canon note explicitly states that preservation of an AMOS framework, equation, ontology, target, or architecture does not establish external empirical validity. 

---

# 46. Current MOC Conclusion

```yaml
conclusion:
  class: DERIVED

  supported:
    - AMOS OS requires explicit layer separation.
    - MOC should be the root navigation layer.
    - capability and authority must remain distinct.
    - unknown gaps must not be treated as pass.
    - component contracts should include provenance, tests, failure, and recovery.

  not_established:
    - every linked component exists
    - every linked file is populated
    - every runtime is live
    - every dependency is implemented
    - every model is empirically validated

  unresolved:
    - exhaustive implementation audit
    - exact active dependency graph
    - exact component-level validation status
```

---

# 47. RSCF Node

```yaml
node_id: AMOS_OS_MOC

node_type: map_of_content

domain: AMOS_OS

functional_type:
  NAVIGATION
  GOVERNANCE_INDEX

lifecycle_stage:
  ACTIVE

origin_architect:
  Trang Phan

claim_class:
  AMOS_MODEL

claim: >
  The AMOS OS MOC is the root navigation layer connecting architecture,
  canon, kernel, control plane, runtime, cognitive systems, agents,
  reusable capabilities, persistence layers, models, tools, governance,
  tests, operations, domains, research, and archival lineage while
  preserving capability/authority and unknown/pass boundaries.

dependencies:
  - "ARCHITECTURE"
  - "SYSTEM_MAP"
  - "FULL_TREE"
  - "AUTHORITATIVE_STATE"
  - "DEPENDENCY_MAP"

invariants:
  - CAPABILITY != AUTHORITY
  - UNKNOWN/GAP != PASS
  - MODEL != OBSERVATION
  - IMPLEMENTATION != VALIDATION
  - REPOSITORY_PRESENCE != LIVE_RUNTIME

falsifiers:
  - root architecture is superseded
  - canonical ownership boundaries materially change
  - repository structure is replaced by a new approved topology

confidence_ceiling:
  navigation_structure: high
  implementation_completeness: unknown
```

---

## Related MOCs

- [[COSMO_BRAIN_MOC|00 Cosmo Brain MOC — the canonical Cosmo Brain index]]
- [[COSMO_BRAIN_BRIDGE_INDEX|Cosmo Brain Bridge Index — comprehensive bridge to external vault (8,253 entries across 20 directories)]]
- [[KNOWLEDGE_MOC|11_KNOWLEDGE MOC — the knowledge layer index]]
- arXiv QFM MOC — 66,028 arXiv preprints (68,367 entries with cross-listings; QFM + C01-C12 domain-classified; 0 unclassified)
- [[COGNITIVE_MATRIX_MOC|Cognitive Matrix MOC — 1,552 cognitive matrix files (100% indexed)]]
- [[AMOS_OBSIDIAN_LINKING_PLUGINS]] — Obsidian vault linking plugin stack
- [[00_HOME]] — universal vault hub (00_ROOT)
- [[00_HOME]] — root AMOS Home

---

- [[AMOS_LAYER_MAPS]] — top-level layer map index
- [[AMOS_TEMPLATES]] — AMOS template index
- [[linked-note]] — Obsidian linked-note template (Templates/)
- [[INDEX_REPAIR_GAP_REPORT_2026-08-26]] — vault index repair gap report (2026-08-26)
# 48. Changelog

## v2.1.0 — 2026-08-26 (index repair)

* extended `ARXIV_QFM_MOC.md` with 44,264 missing arXiv entries (pass 1); content-based reclassification of 26,136 papers from "Other" into Quantum/Fractal/Math/QFM (pass 2); C01-C12 domain classification of 18,969 papers (pass 3a); manual classification of final 26 (pass 3b); 66,028/66,028 files indexed (100%), 0 unclassified;
* audited `25_COGNITIVE_MATRIX/COGNITIVE_MATRIX_MOC.md`: 3 unindexed files added; 1,551/1,551 files now indexed (100%);
* created `11_KNOWLEDGE/Cosmo_Brain_BRIDGE_INDEX.md` — comprehensive bridge index to external symlinked Cosmo Brain vault: 8,253 entries covering all meaningful subdirectories; 1 genuine broken link fixed;
* audited ALL 28 top-level vault zones: 8 unindexed files found across 00_ROOT, 06_AGENTS, 07_SKILLS, 08_WORKFLOWS, Templates; all 8 fixed;
* removed 12 stale arXiv MOC entries pointing to non-existent files;
* repaired 1,107 broken wiki-links across 82+ navigation files: section-style links → file links, skill display names → bridge index, concept abbreviations → plain text, path-style links → correct filenames;
* fixed 8 case-mismatch broken links in `11_KNOWLEDGE_MOC.md` (files existed but with different casing);
* escaped 6 math notation false-positive wiki-links in arxiv paper (formal power series double-brackets → backslash-escaped);
* fixed 4 stale MOC descriptions (bridge count 2,844→8,253, arXiv count 66,042→66,028/68,367);
* vault-wide: 0 unindexed, 0 unclassified, 0 orphans, 0 stale entries, 0 broken links;
* fixed external Cosmo_Brain vault MOCs: 29 arXiv MOCs (66,026 paper links de-wikilinked + redirect notices), 00-Home.md (2,304 agent refs de-wikilinked, 2 path-fixed to .json), 02-Skills-MOC.md (772 de-wikilinked, 6 path-fixed to SKILL.md), 147 remaining MOCs (9 case-fixed, 647 de-wikilinked) — total 69,759 broken links → 0 real broken links.

## v2.0.0 — 2026-08-25

* expanded minimal MOC into AMOS OS root navigation contract;
* added full root layer map;
* added root-file navigation;
* added Canon / Kernel / Control Plane / Runtime mapping;
* added Cognitive Organism / Agents / Skills / Workflows / Protocols;
* added Memory / Knowledge / State separation;
* added Models / Tools / Interfaces / Schemas;
* added Observability / Security / Tests / Operations;
* added Domains / Modes / Research / Operating Model / Archive / Cognitive Matrix;
* added H/M/L map;
* added dependency-closure rule;
* added epistemic classes;
* added provenance contract;
* added RSCF and GMEF positioning;
* added authority contract;
* added runtime decision path;
* added failure and recovery semantics;
* added lifecycle;
* added component minimum contract and reusable component template;
* added MOC integrity gates;
* added 20 root invariants;
* added primary navigation paths;
* added source and empirical-validity boundary;
* added conclusion and unresolved-gap section;
* added RSCF node;
* added expanded related tags and links.

## v1.0.0

Initial content:

```text
Purpose
Hard Boundary:
CAPABILITY != AUTHORITY
UNKNOWN/GAP != PASS
```

---

**Related:** [[00_HOME]] · [[ARCHITECTURE]] · [[FULL_TREE]] · [[SYSTEM_MAP]] · [[AUTHORITATIVE_STATE]] · [[DEPENDENCY_MAP]] · NAMING_STANDARD · [[PLACEMENT_RULES]] · [[ROADMAP]] · [[RSCF_NODE_INDEX]] · GMEF · [[HML_CANON]] · [[CONTROL_PLANE_CANON]] · [[AUTHORITY_CANON]] · [[COGNITION_CANON]] · [[COGNITIVE_ORGANISM_CANON]]

```
```

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: 00_root_moc
node_type: note
path: 00_ROOT/00_ROOT_MOC.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[00_COSMO_BRAIN_MOC]]
