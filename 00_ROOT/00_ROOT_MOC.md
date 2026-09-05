---
canon-group: meta
canon-type: framework
rscf-state: source-claim
topic: 00 Root Moc
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---

# AMOS OS — Master Map of Content

**Origin architect / steward:** Trang Phan

> **Status:** `ACTIVE_MOC`
> **AMOS_CORE target:** `v4.4`
> **Conclusion class:** `SOURCE_CLAIM / AMOS_MODEL`

______________________________________________________________________

## Purpose

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

______________________________________________________________________

## Hard Boundary

```text
CAPABILITY != AUTHORITY
UNKNOWN/GAP != PASS
MODEL != OBSERVATION
SOURCE_CLAIM != VERIFIED
IMPLEMENTED != VALIDATED
REPOSITORY_PRESENCE != LIVE_RUNTIME
```

These distinctions are non-negotiable.

______________________________________________________________________

## 1. Root Navigation

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
├── 26_WORKFLOWS
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

______________________________________________________________________

## 1.1 MECE Responsibility Partition

This partition is derived from [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]] and [[00_ROOT/PLANE_OWNERSHIP_MATRIX|PLANE_OWNERSHIP_MATRIX]].

- **A — Universal Canon / Anchor plane** → [[01_CANON/01_CANON_MOC|01_CANON]]
- **B — OS Kernel / Core identity plane** → [[02_KERNEL/02_KERNEL_MOC|02_KERNEL]]
- **C — Execution & runtime plane** → [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE]], [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME]], [[25_COGNITIVE_MATRIX/25_COGNITIVE_MATRIX_MOC|25_COGNITIVE_MATRIX]]
- **D — Cognition & organism plane** → [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM]], [[06_AGENTS/06_AGENTS_MOC|06_AGENTS]], [[10_MEMORY/10_MEMORY_MOC|10_MEMORY]], [[19_TESTS/19_TESTS_MOC|19_TESTS]]
- **E — Human-system integration plane** → [[07_SKILLS/07_SKILLS_MOC|07_SKILLS]], [[26_WORKFLOWS/26_WORKFLOWS_MOC|26_WORKFLOWS]], [[09_PROTOCOLS/09_PROTOCOLS_MOC|09_PROTOCOLS]], [[11_KNOWLEDGE/11_KNOWLEDGE_MOC|11_KNOWLEDGE]], [[12_STATE/12_STATE_MOC|12_STATE]], [[13_MODELS/13_MODELS_MOC|13_MODELS]], [[14_TOOLS/14_TOOLS_MOC|14_TOOLS]], [[15_INTERFACES/15_INTERFACES_MOC|15_INTERFACES]], [[16_SCHEMAS/16_SCHEMAS_MOC|16_SCHEMAS]], [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY]], [[18_SECURITY/18_SECURITY_MOC|18_SECURITY]], [[20_OPERATIONS/20_OPERATIONS_MOC|20_OPERATIONS]], [[21_DOMAINS/21_DOMAINS_MOC|21_DOMAINS]], [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH]], [[23_OPERATING_MODEL/23_OPERATING_MODEL_MOC|23_OPERATING_MODEL]]
- **F — Stewardship / archive plane** → [[24_ARCHIVE/24_ARCHIVE_MOC|24_ARCHIVE]]
- **Known structural GAPs / strays**:
  - 08_PLANETARY — not in the canonical MECE tree; status = UNKNOWN/GAP pending allocation or archival. **Resolution**: 08_PLANETARY is Layer 6 (Planetary & Ecological) of the Omniverse Brain architecture. Workflows were renumbered to `26_WORKFLOWS` (2026-09-04) to resolve the numbering collision. Recommended: either keep 08_PLANETARY as-is or integrate into `21_DOMAINS/22_C12_EARTH_ECOLOGY/`.
  - Root-level 55_STRATEGY_MOC — not in the canonical MECE tree; status = UNKNOWN/GAP pending allocation or archival.
  - `00_ROOT_MAP\nand/` — corrupted stray directory with literal newline in name; should be deleted.

______________________________________________________________________

## 2. Root Files

## [[00_ROOT/ARCHITECTURE|ARCHITECTURE]]

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

______________________________________________________________________

## [[00_ROOT/AUTHORITATIVE_STATE|AUTHORITATIVE_STATE]]

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

______________________________________________________________________

## [[00_ROOT/DEPENDENCY_MAP|DEPENDENCY_MAP]]

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

______________________________________________________________________

## [[00_ROOT/SYSTEM_MAP|SYSTEM_MAP]]

Defines high-level system areas and their ownership.

Use when asking:

> What are the major subsystems?

______________________________________________________________________

## [[00_ROOT/FULL_TREE|FULL_TREE]]

Defines filesystem placement.

Use when asking:

> Where should this artifact live?

______________________________________________________________________

## [[00_ROOT/PLACEMENT_RULES|PLACEMENT_RULES]]

Defines repository placement constraints.

Use when asking:

> Which folder owns this artifact?

______________________________________________________________________

## [[00_ROOT/00_ROOT_NAMING_STANDARD|NAMING_STANDARD]]

Defines naming, identifiers, versions, aliases, and compatibility rules.

Use when asking:

> How should this component be named and versioned?

______________________________________________________________________

## [[00_ROOT/ROADMAP|ROADMAP]]

Defines future progression.

Use when asking:

> What is planned but not yet implemented?

______________________________________________________________________

### Other root artifacts

- [[00_ROOT/00_ROOT_ARCHITECTURE|00_ROOT_ARCHITECTURE]]
- [[00_ROOT/00_ROOT_AUDIT|00_ROOT_AUDIT]]
- [[00_ROOT/00_ROOT_AUTHORIZATION|00_ROOT_AUTHORIZATION]]
- [[00_ROOT/00_ROOT_BOUNDARIES|00_ROOT_BOUNDARIES]]
- [[00_ROOT/00_ROOT_CHANGE_LOG|00_ROOT_CHANGE_LOG]]
- [[00_ROOT/00_ROOT_CONTRACT|00_ROOT_CONTRACT]]
- [[00_ROOT/00_ROOT_COVERAGE|00_ROOT_COVERAGE]]
- [[00_ROOT/00_ROOT_DEPENDENCIES|00_ROOT_DEPENDENCIES]]
- [[00_ROOT/00_ROOT_GLOSSARY|00_ROOT_GLOSSARY]]
- [[00_ROOT/00_ROOT_HISTORY|00_ROOT_HISTORY]]
- [[00_ROOT/00_ROOT_IDENTITY|00_ROOT_IDENTITY]]
- [[00_ROOT/00_ROOT_INTEGRATION_CHECKLIST|00_ROOT_INTEGRATION_CHECKLIST]]
- [[00_ROOT/00_ROOT_LIFECYCLE|00_ROOT_LIFECYCLE]]
- [[00_ROOT/00_ROOT_MAP|00_ROOT_MAP]]
- [[00_ROOT/00_ROOT_NAMING_STANDARD|00_ROOT_NAMING_STANDARD]]
- [[00_ROOT/00_ROOT_PROVENANCE|00_ROOT_PROVENANCE]]
- [[00_ROOT/00_ROOT_README|00_ROOT_README]]
- [[00_ROOT/00_ROOT_REGISTRY|00_ROOT_REGISTRY]]
- [[00_ROOT/00_ROOT_RELEASE_NOTES|00_ROOT_RELEASE_NOTES]]
- [[00_ROOT/00_ROOT_STATUS|00_ROOT_STATUS]]
- [[00_ROOT/00_ROOT_VERSIONING|00_ROOT_VERSIONING]]
- [[00_ROOT/00_COSMO_BRAIN_MOC|00_COSMO_BRAIN_MOC]]
- [[00_ROOT/COGNITIVE_MATRIX_INTEGRATION|COGNITIVE_MATRIX_INTEGRATION]]
- [[00_ROOT/NEURAL_NETWORK|NEURAL_NETWORK]]
- [[00_ROOT/SYSTEM_MAP_V1|SYSTEM_MAP_V1]]

## 3. Canon Layer

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

______________________________________________________________________

### Key canon indexes

- [[01_CANON/00_INDEX/CANON_MAP|CANON_MAP]]
- [[01_CANON/00_INDEX/INDEX_CANON_README|INDEX_CANON_README]]
- [[01_CANON/01_CORE_LAWS/AMOS_CORE_LAWS|AMOS_CORE_LAWS]]
- [[01_CANON/02_UNIVERSE_CANON/HML_CANON|HML_CANON]]
- [[01_CANON/02_UNIVERSE_CANON/00_INDEX/UNIVERSE_CANON_MAP|UNIVERSE_CANON_MAP]]
- COGNITION_CANON_MAP
- [[01_CANON/04_INFRASTRUCTURE_CANON/00_INDEX/INFRASTRUCTURE_CANON_MAP|INFRASTRUCTURE_CANON_MAP]]
- [[01_CANON/06_GLOSSARY/00_INDEX/GLOSSARY_MAP|GLOSSARY_MAP]]
- [[01_CANON/07_PROVENANCE/00_INDEX/PROVENANCE_CANON_MAP|PROVENANCE_CANON_MAP]]
- [[01_CANON/08_SUPERSESSION/00_INDEX/SUPERSESSION_MAP|SUPERSESSION_MAP]]

## 4. Kernel Layer

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

______________________________________________________________________

### Key kernel maps

- [[02_KERNEL/00_INDEX/KERNEL_MAP|KERNEL_MAP]]
- [[02_KERNEL/00_INDEX/INDEX_KERNEL_README|INDEX_KERNEL_README]]
- [[02_KERNEL/01_META_LOGIC/00_INDEX/META_LOGIC_MAP|META_LOGIC_MAP]]
- [[02_KERNEL/02_COGNITION/00_INDEX/COGNITION_MAP|COGNITION_MAP]]
- [[02_KERNEL/03_CAUSAL/00_INDEX/CAUSAL_MAP|CAUSAL_MAP]]
- [[02_KERNEL/04_STATE/00_INDEX/KERNEL_STATE_MAP|KERNEL_STATE_MAP]]
- [[02_KERNEL/05_MEMORY/00_INDEX/KERNEL_MEMORY_MAP|KERNEL_MEMORY_MAP]]
- [[02_KERNEL/06_RISK_REPAIR/00_INDEX/RISK_REPAIR_MAP|RISK_REPAIR_MAP]]
- [[02_KERNEL/07_AUTHORITY/00_INDEX/KERNEL_AUTHORITY_MAP|KERNEL_AUTHORITY_MAP]]
- [[02_KERNEL/08_PROVENANCE/00_INDEX/KERNEL_PROVENANCE_MAP|KERNEL_PROVENANCE_MAP]]
- [[02_KERNEL/09_INTEGRATION/00_INDEX/INTEGRATION_MAP|INTEGRATION_MAP]]
- [[02_KERNEL/DETERMINISTIC_LOGIC_KERNEL|DETERMINISTIC_LOGIC_KERNEL]] — M01-M20 logic kernel with proof trails and inference rules catalog
- [[02_KERNEL/ABSOLUTE_LOGIC_KERNEL_19x19|ABSOLUTE_LOGIC_KERNEL_19x19]] — 19×19 Minimal Universal Reasoning Kernel (MURK): 19 primitives, interaction matrix, TriDomain, tensor, resolution algorithms
- [[02_KERNEL/NEURAL_SYMBOLIC_HYBRID|NEURAL_SYMBOLIC_HYBRID]] — Neural-symbolic hybrid kernel spec with neuro/symbolic binding contracts
- [[02_KERNEL/SOFT_REALTIME_SCHEDULER|SOFT_REALTIME_SCHEDULER]] — Soft real-time scheduler with latency/prioritization/energy trade-offs

## 5. Control Plane

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

______________________________________________________________________

### Key control-plane maps

- [[03_CONTROL_PLANE/00_INDEX/CONTROL_PLANE_MAP|CONTROL_PLANE_MAP]]
- [[03_CONTROL_PLANE/00_INDEX/INDEX_CONTROL_PLANE_README|INDEX_CONTROL_PLANE_README]]
- [[03_CONTROL_PLANE/01_TASK_CONTRACT/00_INDEX/TASK_CONTRACT_MAP|TASK_CONTRACT_MAP]]
- [[03_CONTROL_PLANE/02_CAPABILITY/00_INDEX/CAPABILITY_MAP|CAPABILITY_MAP]]
- [[03_CONTROL_PLANE/03_POLICY/00_INDEX/POLICY_MAP|POLICY_MAP]]
- [[03_CONTROL_PLANE/04_AUTHORITY/00_INDEX/CONTROL_PLANE_AUTHORITY_MAP|CONTROL_PLANE_AUTHORITY_MAP]]

## 6. Runtime

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

______________________________________________________________________

### Key runtime maps

- [[04_RUNTIME/00_INDEX/RUNTIME_MAP|RUNTIME_MAP]]
- [[04_RUNTIME/00_INDEX/INDEX_RUNTIME_README|INDEX_RUNTIME_README]]
- [[04_RUNTIME/RUNTIME_RUNTIME_CONTRACT|RUNTIME_RUNTIME_CONTRACT]]
- [[04_RUNTIME/CAS_VERSION_VECTOR|CAS_VERSION_VECTOR]] — Compare-and-swap version vector protocol with causal ordering
- [[04_RUNTIME/MULTI_EPOCH_COORDINATION|MULTI_EPOCH_COORDINATION]] — Multi-epoch coordination protocol with finality and rollback

## 7. Cognitive Organism

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

______________________________________________________________________

### Key cognitive organism indexes

- [[05_COGNITIVE_ORGANISM/00_INDEX/COGNITIVE_ORGANISM_MAP|COGNITIVE_ORGANISM_MAP]]
- [[05_COGNITIVE_ORGANISM/00_INDEX/INDEX_COGNITIVE_ORGANISM_README|INDEX_COGNITIVE_ORGANISM_README]]
- [[05_COGNITIVE_ORGANISM/00_INDEX/INDEX_COGNITIVE_ORGANISM_COGNITIVE_ORGANISM_CONTRACT|INDEX_COGNITIVE_ORGANISM_COGNITIVE_ORGANISM_CONTRACT]]
- [[05_COGNITIVE_ORGANISM/04_COGNITION/ATTENTION_SELECTION_ARCHITECTURE|Attention Selection Architecture]] — Saliency maps, competitive inhibition, attention windows (04_COGNITION)
- [[05_COGNITIVE_ORGANISM/04_COGNITION/REASONING_INFERENCE_ENGINE|Reasoning Inference Engine]] — Bayesian/analogical/abductive reasoning engine (04_COGNITION)
- [[05_COGNITIVE_ORGANISM/04_COGNITION/LEARNING_ADAPTATION_ENGINE|Learning Adaptation Engine]] — Online/meta/transfer learning engine (04_COGNITION)
- [[05_COGNITIVE_ORGANISM/06_WORLD_MODEL/INTERNAL_WORLD_MODEL|Internal World Model]] — Hierarchical predictive self/environment/other model (06_WORLD_MODEL)
- [[05_COGNITIVE_ORGANISM/06_WORLD_MODEL/PREDICTIVE_CODING_FRAMEWORK|Predictive Coding Framework]] — Free energy prediction-error minimization (06_WORLD_MODEL)
- [[05_COGNITIVE_ORGANISM/01_IDENTITY/SELF_MODEL_IDENTITY_REGISTRY|Self-Model Identity Registry]] — Persistent self-model and identity coherence (01_IDENTITY)
- [[05_COGNITIVE_ORGANISM/01_IDENTITY/ETHICAL_ALIGNMENT_REGULATOR|Ethical Alignment Regulator]] — Value alignment and moral constraint regulator (01_IDENTITY)
- [[05_COGNITIVE_ORGANISM/COGNITIVE_STACK_30_LAYER_SPECIFICATION|COGNITIVE_STACK_30_LAYER_SPECIFICATION]] — Full 30-layer cognitive stack (L0–L29), 17 lifecycle operations, 9 control planes, H/M/L scales
- [[05_COGNITIVE_ORGANISM/GLOBAL_WORKSPACE_IMPLEMENTATION|GLOBAL_WORKSPACE_IMPLEMENTATION]] — J-space structured workspace, MANAR metacognitive navigator, GWA broadcast, MIRROR O(1) self-modeling

## 8. Agents

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

______________________________________________________________________

### Key agents indexes

- [[06_AGENTS/00_INDEX/AGENT_MAP|AGENT_MAP]]
- [[06_AGENTS/00_INDEX/INDEX_AGENTS_README|INDEX_AGENTS_README]]
- [[06_AGENTS/00_INDEX/INDEX_AGENTS_AGENT_CONTRACT|INDEX_AGENTS_AGENT_CONTRACT]]

## 9. Skills

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

______________________________________________________________________

### Key skills indexes

- [[07_SKILLS/00_INDEX/SKILL_MAP|SKILL_MAP]]
- [[07_SKILLS/00_INDEX/INDEX_SKILLS_README|INDEX_SKILLS_README]]
- [[07_SKILLS/00_INDEX/INDEX_SKILLS_SKILL_CONTRACT|INDEX_SKILLS_SKILL_CONTRACT]]

## 10. Workflows

## `26_WORKFLOWS`

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

______________________________________________________________________

### Key workflows indexes

- [[26_WORKFLOWS/00_INDEX/WORKFLOW_MAP|WORKFLOW_MAP]]
- [[26_WORKFLOWS/00_INDEX/INDEX_WORKFLOWS_README|INDEX_WORKFLOWS_README]]
- [[26_WORKFLOWS/00_INDEX/INDEX_WORKFLOWS_WORKFLOW_CONTRACT|INDEX_WORKFLOWS_WORKFLOW_CONTRACT]]

## 11. Protocols

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

______________________________________________________________________

### Key protocols indexes

- [[09_PROTOCOLS/00_INDEX/PROTOCOL_MAP|PROTOCOL_MAP]]
- [[09_PROTOCOLS/00_INDEX/INDEX_PROTOCOLS_README|INDEX_PROTOCOLS_README]]
- [[09_PROTOCOLS/00_INDEX/INDEX_PROTOCOLS_PROTOCOL_CONTRACT|INDEX_PROTOCOLS_PROTOCOL_CONTRACT]]
- [[09_PROTOCOLS/AGENT_TOOL_INTERACTION_PROTOCOL|AGENT_TOOL_INTERACTION_PROTOCOL]] — Agent-to-tool invocation protocol with M10 enforcement
- [[09_PROTOCOLS/KNOWLEDGE_PROVENANCE_BINDING_PROTOCOL|KNOWLEDGE_PROVENANCE_BINDING_PROTOCOL]] — Knowledge-provenance binding with promotion pipeline and falsification gates

## 12. Memory

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

______________________________________________________________________

### Key memory indexes

- [[10_MEMORY/00_INDEX/MEMORY_MEMORY_MAP|MEMORY_MEMORY_MAP]]
- [[10_MEMORY/00_INDEX/INDEX_MEMORY_README|INDEX_MEMORY_README]]
- [[10_MEMORY/00_INDEX/INDEX_MEMORY_MEMORY_CONTRACT|INDEX_MEMORY_MEMORY_CONTRACT]]

## 13. Knowledge

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

______________________________________________________________________

### Key knowledge indexes

- [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]]
- [[11_KNOWLEDGE/GRAPH_FAMILY_SPECIFICATION|GRAPH_FAMILY_SPECIFICATION]] — 12 typed graph families (knowledge, causal, provenance, authority, temporal, spatial, epistemic, intent, communication, resource, identity, evolution) with invariants and cross-graph morphisms
- [[11_KNOWLEDGE/RSCF_FORMAL_SPECIFICATION|RSCF_FORMAL_SPECIFICATION]] — 15-layer Recursive Structural Coherence Field anatomy, 12 functional RSCF types, lifecycle, update operations, trust vector, integration with 30-layer cognitive stack
- [[11_KNOWLEDGE/engine/WORLD_MODEL_ENGINE_SPEC|WORLD_MODEL_ENGINE_SPEC]] — World model engine implementation spec mapping 2026 SOTA (World Labs, Cosmos 3, JEPA) to AMOS patterns

## 14. State

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

______________________________________________________________________

### Key state indexes

- [[12_STATE/00_INDEX/STATE_STATE_MAP|STATE_STATE_MAP]]
- [[12_STATE/00_INDEX/INDEX_STATE_README|INDEX_STATE_README]]
- [[12_STATE/00_INDEX/INDEX_STATE_STATE_CONTRACT|INDEX_STATE_STATE_CONTRACT]]
- [[12_STATE/12_STATE_MOC|12_STATE_MOC]] — MECE map of the state plane: 9 state families, `Memory != Knowledge != State`, runtime snapshots and freshness ledger
- [[12_STATE/01_RUNTIME_SNAPSHOTS/AMOS_RUNTIME_STATE|AMOS_RUNTIME_STATE]] — Current runtime state snapshot
- [[12_STATE/AMOS_RUNTIME_STATE_FRESHNESS_2026-09-03|AMOS_RUNTIME_STATE_FRESHNESS_2026-09-03]] — Runtime state freshness ledger

## 15. Models

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

______________________________________________________________________

### Key models indexes

- [[13_MODELS/00_INDEX/MODEL_MAP|MODEL_MAP]]
- [[13_MODELS/00_INDEX/INDEX_MODELS_README|INDEX_MODELS_README]]
- [[13_MODELS/00_INDEX/INDEX_MODELS_MODEL_CONTRACT|INDEX_MODELS_MODEL_CONTRACT]]
- [[13_MODELS/13_MODELS_MOC|13_MODELS_MOC]] — Omniverse Brain 10-layer world/system model MECE map, bound to graph-family and tensor frameworks
- [[13_MODELS/01_FOUNDATION/OMNIVERSE_BRAIN_10_LAYER_SPECIFICATION|OMNIVERSE_BRAIN_10_LAYER_SPECIFICATION]] — Canonical 10-layer mathematical model specification

## 16. Tools

## `14_TOOLS`

- [[11_KNOWLEDGE/AMOS_OBSIDIAN_LINKING_PLUGINS|AMOS_OBSIDIAN_LINKING_PLUGINS]] — Obsidian linking plugin stack and Templater starter (vault/brain surface)

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

______________________________________________________________________

### Key tools indexes

- [[14_TOOLS/00_INDEX/TOOL_MAP|TOOL_MAP]]
- [[14_TOOLS/00_INDEX/INDEX_TOOLS_README|INDEX_TOOLS_README]]
- [[14_TOOLS/00_INDEX/INDEX_TOOLS_TOOL_CONTRACT|INDEX_TOOLS_TOOL_CONTRACT]]

## 17. Interfaces

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

______________________________________________________________________

### Key interfaces indexes

- [[15_INTERFACES/00_INDEX/INTERFACE_MAP|INTERFACE_MAP]]
- [[15_INTERFACES/00_INDEX/INDEX_INTERFACES_README|INDEX_INTERFACES_README]]
- [[15_INTERFACES/00_INDEX/INDEX_INTERFACES_INTERFACE_CONTRACT|INDEX_INTERFACES_INTERFACE_CONTRACT]]

## 18. Schemas

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

______________________________________________________________________

### Key schemas indexes

- [[16_SCHEMAS/00_INDEX/SCHEMA_MAP|SCHEMA_MAP]]
- [[16_SCHEMAS/00_INDEX/INDEX_SCHEMAS_README|INDEX_SCHEMAS_README]]
- [[16_SCHEMAS/00_INDEX/INDEX_SCHEMAS_SCHEMA_CONTRACT|INDEX_SCHEMAS_SCHEMA_CONTRACT]]
- [[16_SCHEMAS/16_SCHEMAS_MOC|16_SCHEMAS_MOC]] — MECE map of the schemas plane: tensor framework, schema families, compatibility rules
- [[16_SCHEMAS/PROTOCOL_SCHEMA|PROTOCOL_SCHEMA]] — typed schema for protocol artifacts (09_PROTOCOLS)
- [[16_SCHEMAS/KNOWLEDGE_SCHEMA|KNOWLEDGE_SCHEMA]] — typed schema for knowledge claims (11_KNOWLEDGE)
- [[16_SCHEMAS/MEMORY_SCHEMA|MEMORY_SCHEMA]] — typed schema for memory records (10_MEMORY)
- [[16_SCHEMAS/SECURITY_SCHEMA|SECURITY_SCHEMA]] — typed schema for security artifacts (18_SECURITY)
- [[16_SCHEMAS/10_RSCF/10_RSCF_MOC|10_RSCF_MOC]] — composition map of the 6 RSCF schemas

## 19. Observability

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

______________________________________________________________________

### Key observability indexes

- [[17_OBSERVABILITY/00_INDEX/OBSERVABILITY_OBSERVABILITY_MAP|OBSERVABILITY_OBSERVABILITY_MAP]]
- [[17_OBSERVABILITY/00_INDEX/INDEX_OBSERVABILITY_README|INDEX_OBSERVABILITY_README]]
- [[17_OBSERVABILITY/00_INDEX/INDEX_OBSERVABILITY_OBSERVABILITY_CONTRACT|INDEX_OBSERVABILITY_OBSERVABILITY_CONTRACT]]

## 20. Security

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

______________________________________________________________________

### Key security indexes

- [[18_SECURITY/00_INDEX/SECURITY_MAP|SECURITY_MAP]]
- [[18_SECURITY/00_INDEX/INDEX_SECURITY_README|INDEX_SECURITY_README]]
- [[18_SECURITY/00_INDEX/INDEX_SECURITY_SECURITY_CONTRACT|INDEX_SECURITY_SECURITY_CONTRACT]]

## 21. Tests

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

______________________________________________________________________

### Key tests indexes

- [[19_TESTS/00_INDEX/TEST_MAP|TEST_MAP]]
- [[19_TESTS/00_INDEX/INDEX_TESTS_README|INDEX_TESTS_README]]
- [[19_TESTS/00_INDEX/INDEX_TESTS_TEST_CONTRACT|INDEX_TESTS_TEST_CONTRACT]]

## 22. Operations

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

______________________________________________________________________

### Key operations indexes

- [[20_OPERATIONS/00_INDEX/OPERATIONS_MAP|OPERATIONS_MAP]]
- [[20_OPERATIONS/00_INDEX/INDEX_OPERATIONS_README|INDEX_OPERATIONS_README]]
- [[20_OPERATIONS/00_INDEX/INDEX_OPERATIONS_OPERATIONS_CONTRACT|INDEX_OPERATIONS_OPERATIONS_CONTRACT]]

## 23. Domains

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

______________________________________________________________________

### Key domains indexes

- [[21_DOMAINS/00_INDEX/DOMAIN_ALIAS_MAP|DOMAIN_ALIAS_MAP]]
- [[21_DOMAINS/00_INDEX/INDEX_DOMAINS_README|INDEX_DOMAINS_README]]
- [[21_DOMAINS/00_INDEX/INDEX_DOMAINS_DOMAIN_ALIAS_CONTRACT|INDEX_DOMAINS_DOMAIN_ALIAS_CONTRACT]]

## 24. Modes

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

______________________________________________________________________

## 25. Research

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

______________________________________________________________________

### Key research indexes

- [[22_RESEARCH/00_INDEX/RESEARCH_RESEARCH_MAP|RESEARCH_RESEARCH_MAP]]
- [[22_RESEARCH/00_INDEX/INDEX_RESEARCH_README|INDEX_RESEARCH_README]]
- [[22_RESEARCH/00_INDEX/INDEX_RESEARCH_RESEARCH_CONTRACT|INDEX_RESEARCH_RESEARCH_CONTRACT]]
- [[22_RESEARCH/SOTA_QUANTUM_ERROR_CORRECTION_BREAKTHROUGHS_2026|SOTA_QUANTUM_ERROR_CORRECTION_BREAKTHROUGHS_2026]] — 2026 QEC convergence: NVIDIA AI decoding, IBM Nighthawk, Nord Quantique bosonic, IQM novel codes, D-Wave dual-rail
- [[22_RESEARCH/SOTA_AGENTIC_AI_MULTI_AGENT_SYSTEMS_2026|SOTA_AGENTIC_AI_MULTI_AGENT_SYSTEMS_2026]] — 2026 agentic AI survey: orchestration taxonomies, cognitive foundations, trust-weighted coordination, evaluation frameworks
- [[22_RESEARCH/SOTA_BCI_FOUNDATION_MODELS_NEURAL_INTERFACES_2026|SOTA_BCI_FOUNDATION_MODELS_NEURAL_INTERFACES_2026]] — 2026 BCI update: foundation model benchmarking, speech neuroprosthetics, IEEE/ISO standardization, consumer BCI
- [[22_RESEARCH/SOTA_NEUROMORPHIC_PHOTONIC_COMPUTING_2026|SOTA_NEUROMORPHIC_PHOTONIC_COMPUTING_2026]] — 2026 neuromorphic/photonic breakthroughs: Intel Loihi 3, BrainChip Akida 2.0, Lightmatter Envise, memristive SNNs
- [[22_RESEARCH/SOTA_WORLD_MODELS_GENERATIVE_SIMULATION_2026|SOTA_WORLD_MODELS_GENERATIVE_SIMULATION_2026]] — 2026 world models: World Labs Atlas, Cosmos 3, Genie 3, JEPA evolution, Riemann-1.0
- [[22_RESEARCH/SOTA_AI_SAFETY_ALIGNMENT_FRONTIER_RISK_2026|SOTA_AI_SAFETY_ALIGNMENT_FRONTIER_RISK_2026]] — 2026 AI safety/alignment: regulatory hardening (EU Art 101, FRONTIER Act), agentic misalignment, scalable oversight, positive-attractor alignment
- [[22_RESEARCH/SOTA_BCI_NEURAL_INTERFACES_2026|SOTA_BCI_NEURAL_INTERFACES_2026]] — 2026 BCI SOTA: Neuralink 21+ patients, Synchron Stentrode, Blackrock 10k channels, China Neuracle NEO, speech neuroprosthetics
- [[22_RESEARCH/SOTA_QUANTUM_COMPUTING_2026|SOTA_QUANTUM_COMPUTING_2026]] — 2026 quantum computing: IBM 70 qubit advantage, IonQ qLDPC breakeven, Quantinuum Helios, Google Willow, D-Wave
- [[22_RESEARCH/SOTA_QUANTUM_BIOLOGY_CONSCIOUSNESS_2026|SOTA_QUANTUM_BIOLOGY_CONSCIOUSNESS_2026]] — 2026 quantum biology: Hameroff fractal time crystals, Wiest MT substrate, QBIT spintronic oscillators, cavity QED
- [[22_RESEARCH/SOTA_NEUROMORPHIC_COMPUTING_2026|SOTA_NEUROMORPHIC_COMPUTING_2026]] — 2026 neuromorphic: Intel Loihi 3, IBM NorthPole, BrainChip Akida 2, SpiNNaker2, event-driven SNNs
- [[22_RESEARCH/SOTA_WORLD_MODELS_SIMULATION_2026|SOTA_WORLD_MODELS_SIMULATION_2026]] — 2026 world models: World Labs spatial intelligence, Physical Intelligence π0, NVIDIA Cosmos, JEPA, Genie 2
- [[22_RESEARCH/SOTA_AI_SAFETY_ALIGNMENT_2026|SOTA_AI_SAFETY_ALIGNMENT_2026]] — 2026 AI safety: Constitutional AI, mechanistic interpretability, EU AI Act enforcement, scalable oversight, alignment tax
- [[22_RESEARCH/SOTA_COGNITIVE_ARCHITECTURE_2026|SOTA_COGNITIVE_ARCHITECTURE_2026]] — 2026 cognitive architectures: Soar/ACT-R/LIDA lineage, JEPA as cognitive core, GWT, IIT, predictive processing, AMOS positioning

## 26. Operating Model

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

______________________________________________________________________

### Key operating model indexes

- [[23_OPERATING_MODEL/00_INDEX/OPERATING_MODEL_MAP|OPERATING_MODEL_MAP]]
- [[23_OPERATING_MODEL/00_INDEX/INDEX_OPERATING_MODEL_README|INDEX_OPERATING_MODEL_README]]
- [[23_OPERATING_MODEL/00_INDEX/INDEX_OPERATING_MODEL_OPERATING_MODEL_CONTRACT|INDEX_OPERATING_MODEL_OPERATING_MODEL_CONTRACT]]

## 27. Archive

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

______________________________________________________________________

### Key archive indexes

- [[24_ARCHIVE/00_INDEX/ARCHIVE_MAP|ARCHIVE_MAP]]
- [[24_ARCHIVE/00_INDEX/INDEX_ARCHIVE_README|INDEX_ARCHIVE_README]]
- [[24_ARCHIVE/00_INDEX/INDEX_ARCHIVE_ARCHIVE_CONTRACT|INDEX_ARCHIVE_ARCHIVE_CONTRACT]]

## 28. Cognitive Matrix

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

______________________________________________________________________

### Key cognitive matrix indexes

- [[25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_MAP|COGNITIVE_MATRIX_MAP]]
- [[25_COGNITIVE_MATRIX/00_INDEX/INDEX_COGNITIVE_MATRIX_README|INDEX_COGNITIVE_MATRIX_README]]
- [[25_COGNITIVE_MATRIX/00_INDEX/INDEX_COGNITIVE_MATRIX_COGNITIVE_MATRIX_CONTRACT|INDEX_COGNITIVE_MATRIX_COGNITIVE_MATRIX_CONTRACT]]

## 29. H/M/L Map

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

______________________________________________________________________

## 30. Dependency Rule

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

______________________________________________________________________

## 31. Epistemic Classes

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

______________________________________________________________________

## 32. Provenance Rule

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

______________________________________________________________________

## 33. RSCF

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

______________________________________________________________________

## 34. GMEF

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

______________________________________________________________________

## 35. Authority Boundary

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

______________________________________________________________________

## 36. Runtime Decision Path

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

______________________________________________________________________

## 37. Failure Model

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

______________________________________________________________________

## 38. Recovery Semantics

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

______________________________________________________________________

## 39. Lifecycle

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

______________________________________________________________________

## 40. Component Minimum Contract

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

______________________________________________________________________

## 41. Component Template

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

______________________________________________________________________

## 42. MOC Integrity Gates

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

______________________________________________________________________

## 43. Root Invariants

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

______________________________________________________________________

## 44. Primary Navigation Paths

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

## Dependencies — part 2

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

______________________________________________________________________

## 45. Source Boundary

The primary AMOS Full Brain OS source defines a structural orchestration system and explicitly requires uncertainty, explicit assumptions, conservative conclusions, and truthfulness about limits.

Its operationalization as an AMOS Skill preserves the same boundary: biological, emotional, somatic, and bioelectromagnetic structures should be treated as model lenses unless independently validated.

The associated canon note explicitly states that preservation of an AMOS framework, equation, ontology, target, or architecture does not establish external empirical validity.

______________________________________________________________________

## 46. Current MOC Conclusion

```yaml
conclusion:
  class: DERIVED

  supported:
    - AMOS OS requires explicit layer separation.
    - MOC should be the root navigation layer.
    - capability and authority must remain distinct.
    - unknown gaps must not be treated as pass.
    - component contracts should include provenance, tests, failure, and recovery.
    - P0-P2 gaps from the 2026-09-04 audit have received substantive specifications: cognitive organs (attention, reasoning, learning, world model, predictive coding, identity, ethics), typed graph families (12 graphs), runtime coordination (CAS/version vectors, multi-epoch), and SOTA research (neuromorphic/photonic, world models, AI safety/alignment).
    - Schemas and State MOC layers converted from templated boilerplate to substantive MECE maps; Schemas plane MECE gap filled with protocol/knowledge/memory/security schema families.

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
    - empirical validation of cognitive/consciousness-adjacent model lenses
```

______________________________________________________________________

## 47. RSCF Node

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

______________________________________________________________________

## Related MOCs

- [[11_KNOWLEDGE/COSMO_BRAIN_MOC|00 Cosmo Brain MOC — the canonical Cosmo Brain index]]
- [[11_KNOWLEDGE/COSMO_BRAIN_BRIDGE_INDEX|Cosmo Brain Bridge Index — comprehensive bridge to external vault (8,253 entries across 20 directories)]]
- [[11_KNOWLEDGE/KNOWLEDGE_MOC|11_KNOWLEDGE MOC — the knowledge layer index]]
- arXiv QFM MOC — 66,028 arXiv preprints (68,367 entries with cross-listings; QFM + C01-C12 domain-classified; 0 unclassified)
- [[25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_MOC|Cognitive Matrix MOC — 1,552 cognitive matrix files (100% indexed)]]
- [[11_KNOWLEDGE/AMOS_OBSIDIAN_LINKING_PLUGINS|AMOS_OBSIDIAN_LINKING_PLUGINS]] — Obsidian vault linking plugin stack
- [[00_ROOT/00_HOME|00_HOME]] — universal vault hub / root AMOS Home
- [[CLAUDE|CLAUDE]] — Anthropic Claude guidelines
- [[00_ROOT/Agent Skills|Agent Skills]] — Agent skills core note
- [[11_KNOWLEDGE/LLM_WIKI/raw/AGENT_SKILLS_STANDARD_README_2026_08_30|Agent Skills Standard]] — Agent skills standard README

______________________________________________________________________

- [[00_ROOT/AMOS_LAYER_MAPS|AMOS_LAYER_MAPS]] — top-level layer map index
- [[00_ROOT/AMOS_TEMPLATES|AMOS_TEMPLATES]] — AMOS template index
- [[Templates/linked-note|linked-note]] — Obsidian linked-note template (Templates/)
- [[00_ROOT/INDEX_REPAIR_GAP_REPORT_2026-08-26|INDEX_REPAIR_GAP_REPORT_2026-08-26]] — vault index repair gap report (2026-08-26)

## 48. Changelog

## v2.3.0 — 2026-09-04 (round 3: schemas/state/models MECE completion)

- Expanded templated MOCs into substantive MECE navigation maps: `16_SCHEMAS/16_SCHEMAS_MOC.md` (64→153 lines, tensor framework + schema families + compatibility rules), `12_STATE/12_STATE_MOC.md` (64→187 lines, 9 state families, Memory≠Knowledge≠State, runtime snapshots + freshness ledger), `16_SCHEMAS/10_RSCF/10_RSCF_MOC.md` (38→134 lines, 6 RSCF schema composition + epistemic guardrails), `13_MODELS/13_MODELS_MOC.md` (82→133 lines, 10-layer model bound to graph-family + tensor frameworks)
- Filled MECE gap in Schemas plane: created 4 new typed schema families — `16_SCHEMAS/PROTOCOL_SCHEMA.md` (285 lines), `16_SCHEMAS/KNOWLEDGE_SCHEMA.md` (209 lines), `16_SCHEMAS/MEMORY_SCHEMA.md` (253 lines), `16_SCHEMAS/SECURITY_SCHEMA.md` (262 lines) — preserving `Memory != Knowledge != State` and `Capability != Authority` boundaries
- Added 1 new SOTA research synthesis: `22_RESEARCH/SOTA_AI_SAFETY_ALIGNMENT_FRONTIER_RISK_2026.md` (414 lines — EU Art 101, FRONTIER Act, agentic misalignment, scalable oversight, positive-attractor alignment, AMOS invariant mapping)
- Verified P3 cleanup: corrupted stray directory `00_ROOT_MAP\nand/` no longer present; 08_PLANETARY resolution (Layer 6, 26_PLANETARY recommendation) documented and preserved
- Updated ROOT_MOC navigation with all round 3 files; documented remaining UNKNOWN/GAP (executable MVCC/MVCC finality, schema validators, model-output/simulation firewalls)

## v2.2.0 — 2026-09-04 (comprehensive audit & expansion)

- Full vault structure scan: 26 numbered layers, 3,000+ files audited
- Fixed 2 truncated specifications: `02_KERNEL/DETERMINISTIC_LOGIC_KERNEL.md` (44→220+ lines, full axiom enforcement, proof trails, non-monotonic management), `09_PROTOCOLS/COORDINATION_AVOIDANCE_PROTOCOL.md` (48→200+ lines, full I-confluence theory, shard-local finalization, proof-based coordination avoidance)
- Expanded 3 thin engine models: `11_KNOWLEDGE/engine/CONSCIOUSNESS_ENGINE_MODEL.md` (49→200+ lines, global workspace architecture, UST tree, state machine), `EMOTION_ENGINE_MODEL.md` (49→200+ lines, ASV dynamics, homeostatic regulation, 5 kernel specs), `CONSTRAINT_ENGINE.md` (49→200+ lines, constraint tensor, admissibility function, propagation protocol)
- Expanded `15_INTERFACES/BCI_EXPRESSION_GATEWAY_ADAPTER.md` (63→200+ lines, 2026 BCI modality specs, foundation model integration, 8 safety invariants)
- Expanded `10_MEMORY/EPISODIC_MEMORY_SUBSTRATE.md` (58→250+ lines, 4-tier strata, retention curves, temporal replay engine, storage schema)
- Added 3 new SOTA research syntheses: `SOTA_QUANTUM_ERROR_CORRECTION_BREAKTHROUGHS_2026.md` (NVIDIA/IBM/Nord Quantique/IQM/D-Wave convergence), `SOTA_AGENTIC_AI_MULTI_AGENT_SYSTEMS_2026.md` (orchestration taxonomy, cognitive foundations, trust-weighted coordination), `SOTA_BCI_FOUNDATION_MODELS_NEURAL_INTERFACES_2026.md` (DeeperBrain, ST-EEGFormer, speech neuroprosthetics, IEEE standards)
- Added 2 new protocol specifications: `09_PROTOCOLS/AGENT_TOOL_INTERACTION_PROTOCOL.md` (M10 enforcement, sandbox execution, output classification), `09_PROTOCOLS/KNOWLEDGE_PROVENANCE_BINDING_PROTOCOL.md` (promotion pipeline, provenance record structure, contradiction detection)
- Resolved 08_PLANETARY MECE gap: identified as Layer 6 Omniverse Brain, recommended renumber to 26_PLANETARY
- Documented corrupted stray directory `00_ROOT_MAP\nand/` for deletion
- Updated ROOT_MOC navigation with all new files and structural fixes

## v2.1.0 — 2026-08-26 (index repair)

- extended `ARXIV_QFM_MOC.md` with 44,264 missing arXiv entries (pass 1); content-based reclassification of 26,136 papers from "Other" into Quantum/Fractal/Math/QFM (pass 2); C01-C12 domain classification of 18,969 papers (pass 3a); manual classification of final 26 (pass 3b); 66,028/66,028 files indexed (100%), 0 unclassified;
- audited `25_COGNITIVE_MATRIX/COGNITIVE_MATRIX_MOC.md`: 3 unindexed files added; 1,551/1,551 files now indexed (100%);
- created `11_KNOWLEDGE/Cosmo_Brain_BRIDGE_INDEX.md` — comprehensive bridge index to external symlinked Cosmo Brain vault: 8,253 entries covering all meaningful subdirectories; 1 genuine broken link fixed;
- audited ALL 28 top-level vault zones: 8 unindexed files found across 00_ROOT, 06_AGENTS, 07_SKILLS, 26_WORKFLOWS, Templates; all 8 fixed;
- removed 12 stale arXiv MOC entries pointing to non-existent files;
- repaired 1,107 broken wiki-links across 82+ navigation files: section-style links → file links, skill display names → bridge index, concept abbreviations → plain text, path-style links → correct filenames;
- fixed 8 case-mismatch broken links in `11_KNOWLEDGE_MOC.md` (files existed but with different casing);
- escaped 6 math notation false-positive wiki-links in arxiv paper (formal power series double-brackets → backslash-escaped);
- fixed 4 stale MOC descriptions (bridge count 2,844→8,253, arXiv count 66,042→66,028/68,367);
- vault-wide: 0 unindexed, 0 unclassified, 0 orphans, 0 stale entries, 0 broken links;
- fixed external Cosmo_Brain vault MOCs: 29 arXiv MOCs (66,026 paper links de-wikilinked + redirect notices), 00-Home.md (2,304 agent refs de-wikilinked, 2 path-fixed to .json), 02-Skills-MOC.md (772 de-wikilinked, 6 path-fixed to SKILL.md), 147 remaining MOCs (9 case-fixed, 647 de-wikilinked) — total 69,759 broken links → 0 real broken links.

## v2.0.0 — 2026-08-25

- expanded minimal MOC into AMOS OS root navigation contract;
- added full root layer map;
- added root-file navigation;
- added Canon / Kernel / Control Plane / Runtime mapping;
- added Cognitive Organism / Agents / Skills / Workflows / Protocols;
- added Memory / Knowledge / State separation;
- added Models / Tools / Interfaces / Schemas;
- added Observability / Security / Tests / Operations;
- added Domains / Modes / Research / Operating Model / Archive / Cognitive Matrix;
- added H/M/L map;
- added dependency-closure rule;
- added epistemic classes;
- added provenance contract;
- added RSCF and GMEF positioning;
- added authority contract;
- added runtime decision path;
- added failure and recovery semantics;
- added lifecycle;
- added component minimum contract and reusable component template;
- added MOC integrity gates;
- added 20 root invariants;
- added primary navigation paths;
- added source and empirical-validity boundary;
- added conclusion and unresolved-gap section;
- added RSCF node;
- added expanded related tags and links.

## v1.0.0

Initial content:

```text
Purpose
Hard Boundary:
CAPABILITY != AUTHORITY
UNKNOWN/GAP != PASS
```

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/ARCHITECTURE|ARCHITECTURE]] · [[00_ROOT/FULL_TREE|FULL_TREE]] · [[00_ROOT/SYSTEM_MAP|SYSTEM_MAP]] · [[00_ROOT/AUTHORITATIVE_STATE|AUTHORITATIVE_STATE]] · [[00_ROOT/DEPENDENCY_MAP|DEPENDENCY_MAP]] · NAMING_STANDARD · [[00_ROOT/PLACEMENT_RULES|PLACEMENT_RULES]] · [[00_ROOT/ROADMAP|ROADMAP]] · [[00_ROOT/RSCF_NODE_INDEX|RSCF_NODE_INDEX]] · GMEF · [[01_CANON/02_UNIVERSE_CANON/HML_CANON|HML_CANON]] · [[01_CANON/04_INFRASTRUCTURE_CANON/CONTROL_PLANE_CANON|CONTROL_PLANE_CANON]] · [[01_CANON/04_INFRASTRUCTURE_CANON/AUTHORITY_CANON|AUTHORITY_CANON]] · [[01_CANON/03_COGNITION_CANON/COGNITION_CANON|COGNITION_CANON]] · [[01_CANON/03_COGNITION_CANON/COGNITIVE_ORGANISM_CANON|COGNITIVE_ORGANISM_CANON]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

______________________________________________________________________

RSCF-NODE
node_id: 00_root_moc
node_type: note
path: 00_ROOT/00_ROOT_MOC.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
  claim_class: AMOS_MODEL

______________________________________________________________________

**MOC:** [[00_ROOT/00_COSMO_BRAIN_MOC|00_COSMO_BRAIN_MOC]]
