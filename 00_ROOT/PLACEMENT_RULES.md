````markdown
---
artifact_id: AMOS-OS-PLACEMENT-RULES
name: AMOS_OS_PLACEMENT_RULES
title: "AMOS OS Placement Rules — Canonical Ownership, Layer Assignment, and Artifact Routing Standard"

document_version: "2.0.0"
placement_standard_version: "1.0.0"
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
  - artifact_placement
  - repository_ownership
  - layer_assignment
  - cross_layer_routing
  - dependency_direction
  - migration
  - archive
  - provenance

tags:
  - amos
  - amos-os
  - placement
  - placement-rules
  - repository
  - architecture
  - ownership
  - dependency-routing
  - canon
  - kernel
  - control-plane
  - runtime
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
  - provenance
  - rscf
  - hml
  - governance
  - migration
  - canon-group/tech-ai
  - canon/standard
  - rscf/claim
  - rscf/provenance
  - rscf/state/derived
  - topic/amos-os
  - topic/placement-rules
  - topic/repository-architecture

aliases:
  - AMOS Placement Rules
  - AMOS OS Placement Standard
  - AMOS Artifact Placement Rules
  - AMOS Repository Ownership Rules
  - AMOS Layer Routing Standard

related:
  - "[[00_ROOT/MOC.md|MOC]]"
  - "[[00_ROOT/ARCHITECTURE.md|Architecture]]"
  - "[[00_ROOT/FULL_TREE.md|Full Tree]]"
  - "[[00_ROOT/SYSTEM_MAP.md|System Map]]"
  - "[[00_ROOT/DEPENDENCY_MAP.md|Dependency Map]]"
  - "[[00_ROOT/AUTHORITATIVE_STATE.md|Authoritative State]]"
  - "[[00_ROOT/NAMING_STANDARD.md|Naming Standard]]"
  - "[[00_ROOT/ROADMAP.md|Roadmap]]"
  - "[[00_ROOT/NEURAL_NETWORK.md|Neural Network]]"
---

# AMOS OS Placement Rules

> **Status:** `ACTIVE_STANDARD`  
> **Placement standard version:** `1.0.0`  
> **AMOS_CORE target:** `v4.4`  
> **Origin architect / steward:** Trang Phan  
> **Conclusion class:** `AMOS_MODEL`

---

# 0. Purpose

This standard defines where AMOS OS artifacts belong and which architectural layer owns them.

Placement is based on:

```text
SEMANTIC RESPONSIBILITY
+
AUTHORITY
+
STATE OWNERSHIP
+
EXECUTION ROLE
+
LIFECYCLE
````

not merely:

```text
filename
file extension
implementation language
historical folder
```

The core rule is:

> **Place an artifact according to the responsibility it owns, not according to every subsystem it happens to interact with.**

---

# 1. Canonical Placement Table

| Artifact                                          | Canonical location      |
| ------------------------------------------------- | ----------------------- |
| Source law / official definition                  | `01_CANON`              |
| Deterministic operator / invariant engine         | `02_KERNEL`             |
| Policy / authority / commit / provenance control  | `03_CONTROL_PLANE`      |
| Execution harness / scheduler / router            | `04_RUNTIME`            |
| Cognitive subsystem                               | `05_COGNITIVE_ORGANISM` |
| Role-based worker                                 | `06_AGENTS`             |
| Reusable procedure                                | `07_SKILLS`             |
| Multi-step orchestration graph                    | `08_WORKFLOWS`          |
| Interaction contract                              | `09_PROTOCOLS`          |
| Persistent memory                                 | `10_MEMORY`             |
| Evidence / claims / RSCFs / framework knowledge   | `11_KNOWLEDGE`          |
| Authoritative / working / shadow / recovery state | `12_STATE`              |
| Foundation/domain/calibration model registry      | `13_MODELS`             |
| Tools/connectors/external effectors               | `14_TOOLS`              |
| API/MCP/user/agent interfaces                     | `15_INTERFACES`         |
| Typed schemas                                     | `16_SCHEMAS`            |
| Traces/metrics/logs/health                        | `17_OBSERVABILITY`      |
| AuthN/AuthZ/secrets/threat model                  | `18_SECURITY`           |
| Verification / benchmarks                         | `19_TESTS`              |
| Deployment / runbooks / incidents                 | `20_OPERATIONS`         |
| Domain adapters                                   | `21_DOMAINS`            |
| Papers / experiments / external evidence          | `22_RESEARCH`           |
| Roles / decision rights / governance forums       | `23_OPERATING_MODEL`    |
| Legacy / deprecated / superseded                  | `24_ARCHIVE`            |
| Cross-cognitive topology / matrix relations       | `25_COGNITIVE_MATRIX`   |

---

# 2. Placement Firewall

Placement must preserve these distinctions:

```text
CANON
!=
KERNEL
```

```text
KERNEL
!=
CONTROL PLANE
```

```text
CONTROL PLANE
!=
RUNTIME
```

```text
AGENT
!=
SKILL
```

```text
SKILL
!=
WORKFLOW
```

```text
MEMORY
!=
KNOWLEDGE
!=
STATE
```

```text
MODEL
!=
EVIDENCE
```

```text
TOOL
!=
INTERFACE
```

```text
TEST
!=
OBSERVABILITY
```

```text
RESEARCH
!=
CANON
```

```text
ARCHIVE
!=
ACTIVE SOURCE OF TRUTH
```

---

# 3. Placement Decision Rule

For artifact (A), define:

[
Owner(A)
========

\arg\max_L
ResponsibilityMatch(A,L)
]

where `L` is one AMOS OS architectural layer.

An artifact should have:

```text
ONE PRIMARY OWNER
```

even when it has multiple dependencies.

Cross-cutting behavior should be represented through:

```text
dependencies
references
registries
RSCF relations
protocols
```

rather than uncontrolled duplication.

---

# 4. Primary Ownership Rule

Every nontrivial artifact should answer:

```text
WHO OWNS THIS?
```

The owner is the layer whose removal would make the artifact's **primary purpose** meaningless.

Examples:

```text
A policy evaluator
→ CONTROL_PLANE
```

because its primary purpose is policy enforcement.

```text
A parser used by the policy evaluator
→ KERNEL
```

if the parser itself is a deterministic reusable operator.

```text
A policy-evaluation workflow
→ WORKFLOWS
```

if its purpose is sequencing multiple policy stages.

---

# 5. Cross-Layer Reference Rule

Interaction does not imply ownership.

Example:

```text
Investment_Agent
uses
MarketDataTool
```

Correct placement:

```text
Investment_Agent
→ 06_AGENTS

MarketDataTool
→ 14_TOOLS
```

Do not place both inside the same folder merely because they interact.

---

# 6. No-Duplication Rule

Do not create independent copies of one authoritative artifact in multiple planes.

Bad:

```text
03_CONTROL_PLANE/AUTHORITY.md
06_AGENTS/AUTHORITY.md
21_DOMAINS/AUTHORITY.md
```

when all three claim to be authoritative.

Preferred:

```text
03_CONTROL_PLANE/AUTHORITY.md
```

with references from agents/domains.

Hard rule:

```text
CrossLayerUse
!=
CrossLayerDuplication
```

---

# 7. Canon — `01_CANON`

Place here when the artifact defines:

```text
official law
canonical definition
irreducible invariant
semantic identity
high-governance architecture law
authoritative ontology
```

Examples:

```text
AMOS Core Laws
7-Part Persistence Canon
Cognition Canon
Authority Canon
H/M/L Canon
```

Do not place here merely because an artifact is important.

Hard rule:

```text
IMPORTANT
!=
CANONICAL
```

A candidate canon remains in:

```text
22_RESEARCH
```

or another appropriate draft location until admitted.

---

# 8. Canon Admission Boundary

`01_CANON` should contain artifacts with explicit canon status.

Minimum metadata:

```yaml
status:
conclusion_class:
source:
provenance:
owner:
version:
```

Unknown or experimental material should not be promoted by filename alone.

```text
*_CANON.md
```

does not establish canon status.

---

# 9. Kernel — `02_KERNEL`

Place deterministic or tightly constrained reusable primitives here.

Examples:

```text
logic operators
RSCF operators
state-transition primitives
normalizers
validators
dependency algorithms
hashing / identity primitives
deterministic routing utilities
```

Kernel should contain mechanisms, not high-level authority.

---

# 10. Kernel Firewall

```text
DETERMINISTIC OPERATION
→ KERNEL
```

```text
POLICY ABOUT WHETHER OPERATION MAY RUN
→ CONTROL_PLANE
```

Example:

```text
calculate_dependency_closure()
→ KERNEL
```

```text
decide_whether_dependency_closure_is_sufficient_for_commit()
→ CONTROL_PLANE
```

---

# 11. Control Plane — `03_CONTROL_PLANE`

Place artifacts here when they own:

```text
authority
policy
admission
commit rules
permission
governance
risk escalation
provenance admission
lifecycle transition authority
resource governance
```

Examples:

```text
AUTHORITY_CONTRACT.md
COMMIT_GATE.md
POLICY_ENGINE.py
PROVENANCE_ADMISSION.md
MODE_GOVERNANCE.md
```

Hard boundary:

```text
CAPABILITY
!=
AUTHORITY
```

---

# 12. Control Plane vs Security

Security owns security-specific enforcement and threat controls.

Control Plane owns broader system governance.

Example:

```text
May agent execute?
→ CONTROL_PLANE
```

```text
Does credential permit operation?
→ SECURITY
```

They may both be load-bearing.

Do not collapse them.

---

# 13. Runtime — `04_RUNTIME`

Place active orchestration machinery here.

Examples:

```text
scheduler
execution loop
task runner
router
session manager
tick engine
epoch manager
runtime harness
runtime registry
```

Runtime performs active coordination under control-plane constraints.

---

# 14. Runtime Firewall

```text
Policy
→ CONTROL_PLANE
```

```text
Policy execution machinery
→ RUNTIME
```

```text
Policy evaluation primitive
→ KERNEL
```

The three layers may cooperate but retain separate ownership.

---

# 15. Cognitive Organism — `05_COGNITIVE_ORGANISM`

Place coordinated cognitive subsystems here.

Examples:

```text
attention
working cognition
hypothesis field
cognitive state integration
metacognition
perception integration
cognition-memory bridge
```

Do not automatically place all AI logic here.

A role-based worker still belongs in:

```text
06_AGENTS
```

---

# 16. Cognitive Organism vs Models

A cognitive subsystem that runs and maintains cognitive state:

```text
→ 05_COGNITIVE_ORGANISM
```

A mathematical representation of cognition:

```text
→ 13_MODELS
```

Example:

```text
CognitionField runtime
→ 05_COGNITIVE_ORGANISM
```

```text
CognitionField mathematical model
→ 13_MODELS
```

---

# 17. Agents — `06_AGENTS`

Place role-oriented active workers here.

Examples:

```text
EnvironmentScan_Agent
Executor_Agent
Investment_Agent
Research_Agent
Validator_Agent
```

An agent is defined primarily by:

```text
ROLE
+
SCOPE
+
INPUT/OUTPUT
+
CAPABILITY
```

not by a reusable procedure.

---

# 18. Agent vs Skill

Use:

```text
06_AGENTS
```

when the artifact represents:

> **Who/what role performs work?**

Use:

```text
07_SKILLS
```

when the artifact represents:

> **How is a bounded capability performed?**

Example:

```text
Investment_Agent
→ 06_AGENTS
```

```text
portfolio-risk-analysis skill
→ 07_SKILLS
```

---

# 19. Skills — `07_SKILLS`

Place reusable bounded procedures here.

A skill should normally define:

```text
trigger
goal
prerequisites
domain model
steps
decision gates
verification
pitfalls
```

Examples:

```text
amos-phase-c-cognition-field
amos-7-part-universe-canon-full
amos-19x19-family-complete
```

Skill placement is independent of the agent that may invoke it.

---

# 20. Skill vs Workflow

Skill:

```text
bounded reusable capability
```

Workflow:

```text
multi-step orchestration across capabilities
```

Example:

```text
validate RSCF claim
→ SKILL
```

```text
ingest → validate → promote → index
→ WORKFLOW
```

---

# 21. Workflows — `08_WORKFLOWS`

Place orchestration graphs/processes here.

A workflow may coordinate:

```text
agents
skills
tools
protocols
tests
state transitions
```

Typical shape:

```text
TRIGGER
↓
PRECONDITION
↓
STAGE 1
↓
STAGE 2
↓
VALIDATION
↓
COMMIT
↓
VERIFICATION
```

---

# 22. Protocols — `09_PROTOCOLS`

Place interaction contracts here.

Examples:

```text
agent handoff
state synchronization
commit protocol
tool invocation contract
multi-agent coordination
request/response contract
```

Protocol answers:

> **How do components interact?**

Workflow answers:

> **In what sequence is work performed?**

---

# 23. Memory — `10_MEMORY`

Place retained experience here.

Examples:

```text
episodic memory
case memory
negative memory
working-memory persistence
historical agent experience
```

Memory is persistent or retained context whose role is remembering.

Hard rule:

```text
REMEMBERED
!=
VALIDATED
```

---

# 24. Knowledge — `11_KNOWLEDGE`

Place evidence, claims, RSCFs, framework knowledge, and validated reusable information here.

Examples:

```text
RSCF nodes
knowledge capsules
framework documentation
evidence packages
claim registries
validated concept notes
```

Knowledge should preserve:

```text
source
claim class
provenance
scope
freshness
dependencies
```

---

# 25. Knowledge vs Research

Research:

```text
candidate / experimental / external evidence under study
```

Knowledge:

```text
admitted reusable information
```

Research may become knowledge only after promotion.

---

# 26. State — `12_STATE`

Place current system state here.

Possible state classes:

```text
AUTHORITATIVE
WORKING
SHADOW
RECOVERY
PENDING
COMMITTED
QUARANTINED
```

Examples:

```text
runtime state snapshot
active mode state
current authority state
working hypothesis state
recovery checkpoint
```

---

# 27. State vs Memory

State answers:

> What is currently true for the running/system configuration?

Memory answers:

> What has been retained from past context or experience?

Do not store current authoritative state only in memory.

---

# 28. State vs Ledger

Current state belongs in:

```text
12_STATE
```

Historical append/replay record may belong with the owning subsystem or:

```text
17_OBSERVABILITY
20_OPERATIONS
11_KNOWLEDGE
```

depending on semantics.

A ledger's owner is determined by what it records.

---

# 29. Models — `13_MODELS`

Place formal models and model registries here.

Examples:

```text
risk models
causal models
simulation models
forecast models
cognitive models
calibration models
foundation model registry
```

Models may consume evidence but do not own evidence.

---

# 30. Model vs Domain

A generic financial-risk model:

```text
13_MODELS
```

A finance-specific adapter that maps domain objects into generic risk-model inputs:

```text
21_DOMAINS
```

The domain layer specializes; the model layer defines reusable formal machinery.

---

# 31. Tools — `14_TOOLS`

Place capabilities that interact with deterministic external systems or perform bounded effects here.

Examples:

```text
connectors
filesystem adapters
API clients
compilers
database adapters
browser adapters
execution adapters
market-data connectors
```

Hard boundary:

```text
TOOL ACCESS
!=
AUTHORITY
```

---

# 32. Tool vs Agent

Tool:

```text
provides capability
```

Agent:

```text
uses capability toward scoped objectives
```

Example:

```text
Google Drive connector
→ TOOL
```

```text
DocumentManagement_Agent
→ AGENT
```

---

# 33. Interfaces — `15_INTERFACES`

Place user/system-facing boundary contracts here.

Examples:

```text
REST API
MCP
CLI
UI adapter
public agent interface
external service interface
```

Interface defines how a consumer accesses capability.

Tool defines implementation that performs capability.

---

# 34. Schemas — `16_SCHEMAS`

Place typed structural definitions here.

Examples:

```text
AGENT_SCHEMA
MODE_SCHEMA
RSCF_SCHEMA
EXECUTION_REQUEST_SCHEMA
STATE_SCHEMA
```

Schemas should not own runtime behavior.

---

# 35. Observability — `17_OBSERVABILITY`

Place telemetry and runtime evidence here.

Examples:

```text
logs
traces
metrics
health checks
runtime diagnostics
audit telemetry
```

Hard rule:

```text
OBSERVABILITY
!=
SOURCE OF POLICY AUTHORITY
```

---

# 36. Observability vs Provenance

Operational trace:

```text
17_OBSERVABILITY
```

Knowledge/evidence provenance record:

```text
11_KNOWLEDGE
```

Provenance admission policy:

```text
03_CONTROL_PLANE
```

Provenance implementation primitive:

```text
02_KERNEL
```

One concept may span several layers with different responsibilities.

---

# 37. Security — `18_SECURITY`

Place security-specific controls here.

Examples:

```text
authentication
authorization mechanics
secret storage
threat models
security policy implementation
input-hardening rules
security audit rules
```

Security may be cross-cutting, but its authoritative implementations should remain centralized.

---

# 38. Tests — `19_TESTS`

Place verification artifacts here when they test other components.

Examples:

```text
unit tests
integration tests
regression suites
benchmarks
property tests
failure/recovery tests
adversarial tests
```

Small colocated tests may remain next to code if implementation tooling requires that arrangement, but canonical test indexing belongs here.

---

# 39. Operations — `20_OPERATIONS`

Place deployment and lifecycle operations here.

Examples:

```text
deployment
runbooks
backup
restore
migration
incident response
release
rollback
maintenance
```

Operations manage active systems.

They do not redefine canon.

---

# 40. Domains — `21_DOMAINS`

Place domain-specific adapters, ontologies, mappings, and specialization here.

Examples:

```text
finance adapters
legal domain overlays
biology adapters
strategy domain routing
mode families
domain-specific mappings
```

Generic reusable engines should remain in their primary architectural plane.

---

# 41. Domain Adapter Rule

A domain adapter translates:

```text
DOMAIN SEMANTICS
↔
CORE AMOS CONTRACT
```

Example:

```text
financial instrument
→ generic model input
```

belongs in domain specialization when the translation is finance-specific.

---

# 42. Modes Placement

Mode families belong under domain/mode architecture when they represent behavioral configuration rather than independent agents.

Example:

```text
21_DOMAINS/45_MODES/
```

A mode family may contain:

```text
MODE_FAMILY_SPEC.md
MODE_FAMILY_REGISTRY.md
```

Individual mode implementations may link into runtime/control-plane components while remaining semantically owned by the mode family.

---

# 43. Research — `22_RESEARCH`

Place experimental, exploratory, and externally sourced research here.

Examples:

```text
papers
literature reviews
candidate laws
experiments
prototype algorithms
unverified external claims
benchmarks under study
```

Research may inform canon, models, or knowledge but does not automatically become any of them.

---

# 44. Research Promotion Path

```text
RESEARCH
↓
SOURCE BINDING
↓
PROVENANCE
↓
VALIDATION
↓
SCOPE / REGIME CHECK
↓
KNOWLEDGE
↓ optional governance
CANON
```

No direct promotion should bypass validation.

---

# 45. Operating Model — `23_OPERATING_MODEL`

Place human/system governance structures here.

Examples:

```text
roles
responsibilities
decision rights
review forums
change-control boards
stewardship
maintenance ownership
```

This differs from `03_CONTROL_PLANE`.

`03_CONTROL_PLANE` is machine/runtime governance architecture.

`23_OPERATING_MODEL` is organizational governance architecture.

---

# 46. Archive — `24_ARCHIVE`

Place superseded, deprecated, legacy, or historical artifacts here.

Examples:

```text
old versions
retired architectures
migration snapshots
deprecated agents
historical canon
legacy schemas
```

Archive preserves provenance and lineage.

Hard rule:

```text
ARCHIVE
!=
DELETE
```

---

# 47. Archive Firewall

Moving to archive should preserve:

```text
artifact ID
prior path
version
supersession relation
provenance
reason
date
```

Do not silently erase historical lineage.

---

# 48. Cognitive Matrix — `25_COGNITIVE_MATRIX`

Place cross-cognitive relation maps here.

Examples:

```text
agent ↔ mode relations
mode ↔ memory relations
attention ↔ reasoning relations
knowledge ↔ cognition relations
cognition ↔ domain relations
```

This layer represents cross-cutting cognitive topology.

It must not become a duplicate source of truth.

---

# 49. Multi-Role Artifact Rule

Some artifacts legitimately span multiple concerns.

Example:

```text
AUTHORITY_VALIDATION_PROTOCOL
```

could involve:

```text
CONTROL_PLANE
PROTOCOLS
SECURITY
```

Primary placement should be determined by its principal responsibility.

If it defines the interaction:

```text
→ 09_PROTOCOLS
```

If it defines policy:

```text
→ 03_CONTROL_PLANE
```

If it implements credential verification:

```text
→ 18_SECURITY
```

Cross-link the others.

---

# 50. Code Placement Rule

Programming language does not determine architectural ownership.

A Python file may belong to:

```text
02_KERNEL
03_CONTROL_PLANE
04_RUNTIME
05_COGNITIVE_ORGANISM
06_AGENTS
14_TOOLS
18_SECURITY
```

depending on responsibility.

Therefore:

```text
.py
!=
KERNEL
```

and:

```text
.json
!=
SCHEMA
```

---

# 51. Markdown Placement Rule

Markdown is also not a semantic type.

A `.md` file may represent:

```text
canon
architecture
knowledge
workflow
protocol
research
test plan
runbook
```

Placement is determined by content responsibility.

---

# 52. Registry Placement

A registry belongs with the entities it governs.

Examples:

```text
Agent Registry
→ 06_AGENTS
```

```text
Skill Registry
→ 07_SKILLS
```

```text
Mode Family Registry
→ 21_DOMAINS/.../MODES
```

```text
Model Registry
→ 13_MODELS
```

Do not put every registry into one global folder unless it is explicitly a cross-system registry.

---

# 53. Index Placement

Indexes belong near the namespace they index.

Example:

```text
02_KERNEL/00_INDEX/KERNEL_MAP.md
```

rather than one enormous global index for every subsystem.

Root MOC should link to plane indexes.

---

# 54. Map Placement

Topology maps should be colocated with their ownership scope.

Examples:

```text
00_ROOT/SYSTEM_MAP.md
02_KERNEL/00_INDEX/KERNEL_MAP.md
03_CONTROL_PLANE/00_INDEX/CONTROL_PLANE_MAP.md
```

Cross-system maps belong at the highest common owner.

---

# 55. Ledger Placement

A ledger belongs with the semantics it records.

Examples:

```text
execution ledger
→ runtime / observability / operations depending contract

provenance ledger
→ knowledge or control plane depending whether evidence or admission

migration ledger
→ operations
```

Do not classify by suffix alone.

---

# 56. Source Code vs Contract

Executable code and its contract may live in different but linked artifacts.

Example:

```text
02_KERNEL/K_RSCF.py
16_SCHEMAS/RSCF_NODE_SCHEMA.json
09_PROTOCOLS/RSCF_VALIDATION_PROTOCOL.md
19_TESTS/test_rscf.py
```

This is intentional separation of responsibility.

---

# 57. Implementation vs Specification

Specification should live with the owner of the semantics.

Implementation should live with the owner of the runtime responsibility.

When they are the same subsystem, colocate them.

When not, use explicit dependency links.

---

# 58. H/M/L Placement

Placement may also be understood recursively.

```text
H
=
CANON / ARCHITECTURE / DOMAIN
```

```text
M
=
KERNEL / CONTROL PLANE / RUNTIME / AGENT FAMILY
```

```text
L
=
COMPONENT / TOOL / STATE OBJECT / EVIDENCE ITEM
```

H/M/L describes scale.

It does not replace semantic ownership.

---

# 59. Dependency Direction

Preferred high-level direction:

```text
CANON
↓
KERNEL
↓
CONTROL PLANE
↓
RUNTIME
↓
COGNITIVE ORGANISM / AGENTS
↓
SKILLS / WORKFLOWS
↓
TOOLS / INTERFACES
```

Supporting planes:

```text
MEMORY
KNOWLEDGE
STATE
MODELS
SCHEMAS
OBSERVABILITY
SECURITY
TESTS
OPERATIONS
```

Dependencies may cross this tree, but circular ownership should be minimized.

---

# 60. Dependency Inversion Warning

A foundational layer should not depend on a high-level worker merely to access its own primitive.

Bad:

```text
KERNEL
→ imports AGENT
```

for kernel logic.

Preferred:

```text
AGENT
→ imports KERNEL
```

unless a deliberately inverted interface contract exists.

---

# 61. Placement and Authority

Placement never grants authority.

Example:

```text
file in 03_CONTROL_PLANE
```

does not automatically make its content authoritative.

Authority still depends on:

```text
status
provenance
version
governance
runtime admission
```

Hard rule:

```text
LOCATION
!=
AUTHORITY
```

---

# 62. Placement and Epistemic Status

A file in `01_CANON` may still be:

```text
PLACEHOLDER
DRAFT
UNKNOWN/GAP
```

if metadata says so.

A file in `22_RESEARCH` may contain externally verified evidence.

Therefore:

```text
FOLDER
!=
CONCLUSION CLASS
```

---

# 63. Placement and Lifecycle

Artifact lifecycle and folder placement are separate axes.

Example:

```yaml
path: 06_AGENTS/INVESTMENT/INVESTMENT_AGENT.md
status: REGISTERED_STUB
```

The location says:

```text
agent ownership
```

The status says:

```text
implementation maturity
```

---

# 64. Temporary Artifacts

Temporary outputs should not silently enter canonical folders.

Examples:

```text
generated draft
scratch analysis
migration staging
test output
```

should use appropriate temporary/runtime/research/operations placement until admitted.

---

# 65. Generated Artifact Rule

Generated files must declare where they belong before persistence.

Pipeline:

```text
GENERATE
↓
CLASSIFY
↓
VALIDATE
↓
PLACE
↓
INDEX
```

Not:

```text
GENERATE
↓
DROP INTO ROOT
```

---

# 66. Root Folder Rule

`00_ROOT` is reserved for cross-system architecture/navigation/governance entrypoints.

Typical files:

```text
README.md
MOC.md
ARCHITECTURE.md
FULL_TREE.md
SYSTEM_MAP.md
DEPENDENCY_MAP.md
AUTHORITATIVE_STATE.md
NAMING_STANDARD.md
PLACEMENT_RULES.md
ROADMAP.md
NEURAL_NETWORK.md
```

Do not place domain implementations or arbitrary knowledge notes in root.

---

# 67. Root Pollution Firewall

Root placement requires:

```text
cross-system scope
```

or:

```text
root navigation/governance responsibility
```

If a file only concerns one subsystem, it belongs in that subsystem.

---

# 68. README Rule

A `README.md` belongs inside the folder it explains.

A README is:

```text
local orientation
```

not necessarily authoritative specification.

Use a dedicated contract file for formal semantics.

---

# 69. MOC Rule

A `MOC.md` is a navigational artifact.

Place it at the namespace root it maps.

Example:

```text
00_ROOT/MOC.md
```

for full AMOS OS.

Subsystem MOCs may live in their subsystem.

---

# 70. Placeholder Placement

A placeholder belongs in the final intended canonical location.

Example:

```text
03_CONTROL_PLANE/AUTHORITY_CONTRACT.md
```

with:

```yaml
status: PLACEHOLDER
```

rather than:

```text
00_ROOT/TODO_AUTHORITY.md
```

This reduces future migration.

---

# 71. Placeholder Firewall

Placeholder presence means:

```text
POSITION RESERVED
```

not:

```text
CAPABILITY IMPLEMENTED
```

Hard rule:

```text
PLACEHOLDER
!=
PASS
```

---

# 72. Missing Artifact Rule

When the expected owner is known but the artifact does not exist:

```text
MISSING
=
UNKNOWN/GAP
```

A placeholder may be created if the role is structurally established.

Do not invent detailed canon solely to fill a folder.

---

# 73. Unknown Owner Rule

If placement is ambiguous:

```text
DO NOT GUESS
```

Classify:

```text
UNKNOWN/GAP
```

and identify the decision-relevant distinction.

Example:

```text
Is this file policy or mechanism?
```

That determines:

```text
CONTROL_PLANE vs KERNEL
```

---

# 74. Placement Conflict

A placement conflict exists when multiple layers plausibly claim ownership.

Record:

```yaml
PlacementConflict:
  artifact:
  candidate_owners: []
  decision_axis:
  current_status: COMPETING
```

Resolve by primary responsibility.

---

# 75. Tie-Break Rule

When two placements remain plausible:

1. identify what responsibility is load-bearing;
2. identify which layer owns that responsibility;
3. place there;
4. reference the other layer.

If still unresolved:

```text
COMPETING
```

is valid.

---

# 76. Migration Rule

Moving an artifact between layers is an architectural migration.

It should preserve:

```text
artifact ID
provenance
version lineage
previous path
references
dependencies
```

unless semantic identity intentionally changes.

---

# 77. Migration Classes

```text
P0 — local organizational move
P1 — namespace move
P2 — layer ownership change
P3 — semantic ownership change
P4 — public/external contract move
```

Validation increases with class.

---

# 78. Layer Ownership Change

Moving:

```text
06_AGENTS
→
02_KERNEL
```

is not merely a filesystem move.

It asserts:

```text
this artifact is no longer primarily a role-based worker;
it is now a deterministic kernel primitive.
```

That requires semantic review.

---

# 79. Rename vs Move

```text
Rename
=
representation change
```

```text
Move
=
location/ownership context change
```

Both may occur together but should be tracked independently.

---

# 80. Cross-Plane Composition

Complex capabilities should be composed rather than collapsed.

Example:

```text
INVESTMENT CAPABILITY
├── Agent        → 06_AGENTS
├── Skill        → 07_SKILLS
├── Workflow     → 08_WORKFLOWS
├── Protocol     → 09_PROTOCOLS
├── Knowledge    → 11_KNOWLEDGE
├── Model        → 13_MODELS
├── Market tool  → 14_TOOLS
├── Schema       → 16_SCHEMAS
├── Tests        → 19_TESTS
└── Domain map   → 21_DOMAINS
```

This is expected architectural separation.

---

# 81. Component Family Rule

A large capability may have a family root or MOC that links its cross-plane artifacts.

Do not physically colocate everything only to simplify navigation.

Use:

```text
MOC
REGISTRY
RSCF relations
DEPENDENCY_MAP
```

to reconstruct the family.

---

# 82. Cognitive Matrix Exception

`25_COGNITIVE_MATRIX` exists specifically for cross-cutting cognitive relationships.

It may link artifacts across planes but should not duplicate them.

Example:

```text
ATTENTION MODE
↔
COGNITIVE FIELD
↔
AGENT
```

The matrix stores relation topology, not independent copies.

---

# 83. Provenance Placement

Provenance has multiple layers.

```text
provenance data / evidence lineage
→ 11_KNOWLEDGE
```

```text
provenance validation primitive
→ 02_KERNEL
```

```text
provenance admission policy
→ 03_CONTROL_PLANE
```

```text
runtime provenance trace
→ 17_OBSERVABILITY
```

Do not collapse these.

---

# 84. RSCF Placement

RSCF knowledge nodes:

```text
→ 11_KNOWLEDGE
```

RSCF deterministic operators:

```text
→ 02_KERNEL
```

RSCF schema:

```text
→ 16_SCHEMAS
```

RSCF tests:

```text
→ 19_TESTS
```

RSCF governance:

```text
→ 03_CONTROL_PLANE
```

This separation is intentional.

---

# 85. GMEF Placement

Similar pattern:

```text
GMEF model/knowledge
→ 11_KNOWLEDGE / 13_MODELS
```

```text
GMEF mutation/admission rules
→ 03_CONTROL_PLANE
```

```text
GMEF executable transformation primitives
→ 02_KERNEL
```

Placement depends on exact responsibility.

---

# 86. External Evidence Placement

Raw or external evidence under investigation:

```text
22_RESEARCH
```

After governed admission:

```text
11_KNOWLEDGE
```

Do not treat external material as internal canon merely because it has been imported.

---

# 87. Benchmark Placement

Benchmark definitions and results primarily used for verification:

```text
19_TESTS
```

Benchmark research comparing external systems:

```text
22_RESEARCH
```

Operational runtime performance telemetry:

```text
17_OBSERVABILITY
```

Same word, different ownership.

---

# 88. Incident Placement

Current incident response/runbook:

```text
20_OPERATIONS
```

Security incident threat details:

```text
18_SECURITY
```

Incident telemetry:

```text
17_OBSERVABILITY
```

Learned validated incident lessons:

```text
11_KNOWLEDGE
```

---

# 89. Recovery Placement

Recovery **state**:

```text
12_STATE
```

Recovery **workflow**:

```text
08_WORKFLOWS
```

Recovery **operations runbook**:

```text
20_OPERATIONS
```

Recovery **policy**:

```text
03_CONTROL_PLANE
```

Recovery **test**:

```text
19_TESTS
```

---

# 90. Authority Placement

Authority model:

```text
03_CONTROL_PLANE
```

Authority schema:

```text
16_SCHEMAS
```

Authority runtime state:

```text
12_STATE
```

Authority audit telemetry:

```text
17_OBSERVABILITY
```

Authority security implementation:

```text
18_SECURITY
```

Authority organizational decision rights:

```text
23_OPERATING_MODEL
```

---

# 91. Tool Permission Placement

Tool implementation:

```text
14_TOOLS
```

Tool interface:

```text
15_INTERFACES
```

Tool schema:

```text
16_SCHEMAS
```

Tool authority:

```text
03_CONTROL_PLANE
```

Tool credential handling:

```text
18_SECURITY
```

Tool execution telemetry:

```text
17_OBSERVABILITY
```

---

# 92. Mode Placement

Mode definition:

```text
21_DOMAINS/.../MODES
```

Mode runtime state:

```text
12_STATE
```

Mode switching policy:

```text
03_CONTROL_PLANE
```

Mode transition runtime:

```text
04_RUNTIME
```

Mode schema:

```text
16_SCHEMAS
```

Mode tests:

```text
19_TESTS
```

---

# 93. Agent Placement Decomposition

Agent definition:

```text
06_AGENTS
```

Agent capability procedure:

```text
07_SKILLS
```

Agent orchestration:

```text
08_WORKFLOWS
```

Agent communication:

```text
09_PROTOCOLS
```

Agent state:

```text
12_STATE
```

Agent schema:

```text
16_SCHEMAS
```

Agent traces:

```text
17_OBSERVABILITY
```

Agent tests:

```text
19_TESTS
```

---

# 94. Domain Separation

Domain-specific content should not leak upward unless it is truly reusable.

Example:

```text
finance-specific order model
```

may belong in:

```text
21_DOMAINS/FINANCE
```

while generic transaction state machinery belongs in:

```text
02_KERNEL / 04_RUNTIME
```

Hard rule:

```text
OneDomainUse
does not automatically justify
CorePlacement
```

---

# 95. Promotion to Core

A domain-specific artifact may move into kernel/canon only if:

```text
cross-domain reuse established
semantic abstraction defined
domain assumptions removed or typed
tests generalized
governance review passed
```

Do not promote merely because the artifact is successful in one domain.

---

# 96. Core-to-Domain Fork

If core logic needs domain specialization:

```text
CORE PRIMITIVE
↓
DOMAIN ADAPTER
```

Do not duplicate and mutate the core implementation inside every domain.

---

# 97. Dependency Closure Rule

Before moving an artifact, identify:

```text
incoming dependencies
outgoing dependencies
registries
wiki links
runtime imports
schemas
tests
provenance references
```

A move is complete only when dependency closure is preserved.

---

# 98. Placement Audit

A repository placement audit should examine:

```text
wrong layer
duplicate authority
orphan artifact
root pollution
domain leakage
archived active dependency
research treated as canon
memory treated as knowledge
state stored as documentation only
missing schemas
missing tests
```

---

# 99. Audit Result Classes

```text
CORRECT
CONDITIONAL
MISPLACED
DUPLICATED
ORPHANED
LEGACY
UNKNOWN/GAP
```

Do not force `CORRECT` when ownership is ambiguous.

---

# 100. Placement Failure Registry

```text
P001 ROOT_POLLUTION
P002 WRONG_LAYER
P003 DUPLICATE_AUTHORITY
P004 DUPLICATE_IMPLEMENTATION
P005 ORPHAN_ARTIFACT
P006 KNOWLEDGE_MEMORY_COLLAPSE
P007 STATE_MEMORY_COLLAPSE
P008 MODEL_EVIDENCE_COLLAPSE
P009 RESEARCH_CANON_LEAK
P010 AGENT_SKILL_COLLAPSE
P011 KERNEL_POLICY_LEAK
P012 CONTROL_PLANE_RUNTIME_COLLAPSE
P013 TOOL_AUTHORITY_LEAK
P014 ARCHIVE_ACTIVE_REFERENCE
P015 DOMAIN_CORE_LEAK
P016 SCHEMA_IMPLEMENTATION_COLLAPSE
P017 PROVENANCE_LOCATION_AMBIGUITY
P018 PLACEMENT_WITHOUT_OWNER
P019 MOVE_WITH_BROKEN_REFERENCES
P020 UNKNOWN_OWNER_PROMOTED_TO_PASS
```

---

# 101. Placement Validation Result

```yaml
PlacementValidation:
  artifact_id:
  current_path:

  semantic_type:

  expected_owner:

  current_owner:

  result:
    CORRECT
    CONDITIONAL
    MISPLACED
    COMPETING
    UNKNOWN/GAP

  dependencies: []

  conflicts: []

  migration_required:

  notes:
```

---

# 102. Placement Invariants

```text
PL01 OneArtifactHasOnePrimaryOwner
PL02 CrossLayerUse != CrossLayerOwnership
PL03 Location != Authority
PL04 Folder != EpistemicClass
PL05 Filename != SemanticType
PL06 Extension != Layer
PL07 Canon != Implementation
PL08 Kernel != Policy
PL09 ControlPlane != Runtime
PL10 Agent != Skill
PL11 Skill != Workflow
PL12 Workflow != Protocol
PL13 Memory != Knowledge
PL14 Knowledge != State
PL15 Model != Evidence
PL16 Tool != Interface
PL17 Research != Canon
PL18 Archive != Active
PL19 Placeholder != Implementation
PL20 Missing != Pass
PL21 DomainUse != CoreOwnership
PL22 Move != Rename
PL23 MoveMayChangeOwnershipSemantics
PL24 ProvenanceMustSurviveMove
PL25 DependenciesMustSurviveMove
PL26 CrossCuttingRelationsUseLinksNotDuplication
PL27 UnknownOwnerRemainsUNKNOWN/GAP
PL28 TestsDoNotOwnImplementation
PL29 ObservabilityDoesNotOwnPolicy
PL30 SecurityDoesNotReplaceControlPlane
```

---

# 103. Naming Prefixes

Canonical structural prefixes:

```text
K_   Kernel
CP_  Control plane
RT_  Runtime
A_   Agent
S_   Skill
WF_  Workflow
P_   Protocol
M_   Memory
```

Recommended additional prefixes where useful:

```text
KN_  Knowledge
ST_  State
MD_  Model
T_   Tool
IF_  Interface
SC_  Schema
OBS_ Observability
SEC_ Security
OP_  Operations
D_   Domain adapter
```

Prefixes are optional conventions, not substitutes for actual folder ownership.

---

# 104. Prefix Firewall

A file named:

```text
K_VALIDATOR.py
```

inside:

```text
06_AGENTS
```

does not automatically become kernel-owned.

Prefix, path, and semantic role should agree.

If they conflict:

```text
AUDIT
```

rather than assuming either representation is correct.

---

# 105. Canonical Filename Rule

Canonical active filenames should not carry historical version suffixes.

Preferred:

```text
ARCHITECTURE.md
AUTHORITY_CONTRACT.md
MODE_FAMILY_REGISTRY.md
```

not:

```text
ARCHITECTURE_v2.md
AUTHORITY_CONTRACT_v4.md
MODE_FAMILY_REGISTRY_FINAL.md
```

Evolution belongs in metadata and provenance.

---

# 106. No Filename Version Suffix Rule

Canonical filenames should remain stable across compatible evolution.

Track:

```text
document_version
component_version
schema_version
hash
revision
supersession
change record
```

instead.

Hard rule:

```text
FileNameVersion
!=
CanonicalVersionAuthority
```

---

# 107. Exception — Parallel Versions

Versioned filenames may be used when multiple versions intentionally coexist.

Example:

```text
schemas/archive/AGENT_SCHEMA_v1.json
schemas/archive/AGENT_SCHEMA_v2.json
```

but the canonical active pointer remains stable.

---

# 108. Supersession Rule

When an artifact is replaced:

```text
NEW
SUPERSEDES
OLD
```

Preserve:

```text
old artifact
old hash
old version
reason
replacement ID
migration date
```

The old artifact may move to `24_ARCHIVE`.

---

# 109. Archive Dependency Rule

Active artifacts should not depend on archived implementations unless explicitly marked compatibility/legacy.

If they do:

```text
LEGACY_DEPENDENCY
```

must be visible.

---

# 110. Root-to-Leaf Placement Flow

When classifying a new artifact:

```text
WHAT IS ITS PRIMARY PURPOSE?
↓
IS IT A LAW/DEFINITION?
  → CANON

IS IT A DETERMINISTIC PRIMITIVE?
  → KERNEL

IS IT AUTHORITY/POLICY?
  → CONTROL PLANE

IS IT EXECUTION ORCHESTRATION?
  → RUNTIME

IS IT COGNITIVE SUBSYSTEM?
  → COGNITIVE ORGANISM

IS IT A ROLE?
  → AGENT

IS IT A REUSABLE PROCEDURE?
  → SKILL

IS IT A MULTI-STEP GRAPH?
  → WORKFLOW

IS IT AN INTERACTION CONTRACT?
  → PROTOCOL

IS IT RETAINED EXPERIENCE?
  → MEMORY

IS IT REUSABLE CLAIM/EVIDENCE?
  → KNOWLEDGE

IS IT CURRENT SYSTEM CONDITION?
  → STATE

IS IT A FORMAL REPRESENTATION?
  → MODEL

IS IT A CAPABILITY CONNECTOR?
  → TOOL

IS IT AN EXTERNAL BOUNDARY?
  → INTERFACE

IS IT A DATA CONTRACT?
  → SCHEMA

IS IT TELEMETRY?
  → OBSERVABILITY

IS IT SECURITY CONTROL?
  → SECURITY

IS IT VERIFICATION?
  → TESTS

IS IT DEPLOYMENT/LIFECYCLE?
  → OPERATIONS

IS IT DOMAIN SPECIALIZATION?
  → DOMAINS

IS IT EXPERIMENTAL?
  → RESEARCH

IS IT ORGANIZATIONAL GOVERNANCE?
  → OPERATING MODEL

IS IT SUPERSEDED?
  → ARCHIVE
```

---

# 111. Decision Examples

## Example A — `Executor_Agent.py`

Primary role:

```text
role-based execution worker
```

Placement:

```text
06_AGENTS
```

Its authority policy remains:

```text
03_CONTROL_PLANE
```

Its external effect adapter remains:

```text
14_TOOLS
```

---

## Example B — `evaluate_move_firewall()`

If deterministic comparison logic:

```text
02_KERNEL
```

If policy determining whether a move may commit:

```text
03_CONTROL_PLANE
```

The word `firewall` alone does not determine placement.

---

## Example C — `AMOS_CognitionField.py`

If it owns live cognitive field state and cognitive update behavior:

```text
05_COGNITIVE_ORGANISM
```

Its formal tensor/model documentation may also link to:

```text
13_MODELS
```

without duplication.

---

## Example D — Agent schema

```text
AGENT_SCHEMA.json
→ 16_SCHEMAS
```

Agent implementation:

```text
06_AGENTS
```

Agent registry:

```text
06_AGENTS
```

Agent tests:

```text
19_TESTS
```

---

## Example E — Investment research paper

Raw/external paper:

```text
22_RESEARCH
```

Validated extracted claims:

```text
11_KNOWLEDGE
```

Investment Agent:

```text
06_AGENTS
```

Portfolio model:

```text
13_MODELS
```

Market connector:

```text
14_TOOLS
```

---

# 112. Ambiguity Resolution Matrix

| Question                                           | If yes | Placement               |
| -------------------------------------------------- | ------ | ----------------------- |
| Is it authoritative semantics?                     | yes    | `01_CANON`              |
| Is it deterministic mechanism?                     | yes    | `02_KERNEL`             |
| Does it decide permission/policy?                  | yes    | `03_CONTROL_PLANE`      |
| Does it schedule/execute runtime work?             | yes    | `04_RUNTIME`            |
| Does it maintain cognitive subsystem state?        | yes    | `05_COGNITIVE_ORGANISM` |
| Is it a role-based worker?                         | yes    | `06_AGENTS`             |
| Is it reusable procedure?                          | yes    | `07_SKILLS`             |
| Is it multi-stage orchestration?                   | yes    | `08_WORKFLOWS`          |
| Is it interaction contract?                        | yes    | `09_PROTOCOLS`          |
| Is it retained experience?                         | yes    | `10_MEMORY`             |
| Is it evidence/claim knowledge?                    | yes    | `11_KNOWLEDGE`          |
| Is it current system state?                        | yes    | `12_STATE`              |
| Is it formal model?                                | yes    | `13_MODELS`             |
| Does it provide external/deterministic capability? | yes    | `14_TOOLS`              |
| Does it expose a boundary?                         | yes    | `15_INTERFACES`         |
| Does it define structure/type?                     | yes    | `16_SCHEMAS`            |
| Is it telemetry?                                   | yes    | `17_OBSERVABILITY`      |
| Is it security-specific?                           | yes    | `18_SECURITY`           |
| Does it verify behavior?                           | yes    | `19_TESTS`              |
| Does it manage deployment/lifecycle?               | yes    | `20_OPERATIONS`         |
| Is it domain specialization?                       | yes    | `21_DOMAINS`            |
| Is it exploratory/unvalidated research?            | yes    | `22_RESEARCH`           |
| Is it organizational governance?                   | yes    | `23_OPERATING_MODEL`    |
| Is it superseded/legacy?                           | yes    | `24_ARCHIVE`            |
| Is it cognitive cross-link topology?               | yes    | `25_COGNITIVE_MATRIX`   |

---

# 113. Placement Promotion Gate

Before moving an artifact into a more authoritative layer:

```text
IDENTITY KNOWN
∧ PRIMARY RESPONSIBILITY KNOWN
∧ PROVENANCE PRESERVED
∧ DEPENDENCIES KNOWN
∧ CONFLICTS RESOLVED
∧ REFERENCES REPAIRABLE
```

Additional requirements:

```text
RESEARCH → KNOWLEDGE
requires validation
```

```text
KNOWLEDGE → CANON
requires governance/canon admission
```

```text
DOMAIN → KERNEL
requires cross-domain abstraction evidence
```

---

# 114. Placement Demotion

Artifacts may move downward/outward when scope is discovered to be narrower.

Example:

```text
generic kernel algorithm
```

found to depend on finance-specific assumptions:

```text
02_KERNEL
→
21_DOMAINS/FINANCE
```

This is correction, not failure.

---

# 115. Placement Recovery

If a placement migration fails:

```text
STOP FURTHER MOVES
↓
PRESERVE CURRENT TREE
↓
COMPARE AGAINST MIGRATION MANIFEST
↓
RESTORE SAFE PATHS
↓
REPAIR REFERENCES
↓
REVALIDATE DEPENDENCY GRAPH
```

Avoid partial layer migration.

---

# 116. Placement Manifest

```yaml
PlacementMigration:
  migration_id:

  artifact_id:

  old_path:
  old_owner:

  new_path:
  new_owner:

  semantic_identity_changed: false

  reason:

  dependencies_before: []
  dependencies_after: []

  references_updated: []

  provenance_preserved: true

  validation:

  rollback:
```

---

# 117. Placement Test Suite

```text
T01 root files restricted to root concerns
T02 canon drafts rejected from active canon
T03 deterministic primitives classified as kernel
T04 authority logic classified as control plane
T05 runtime scheduler classified as runtime
T06 cognitive subsystem classified correctly
T07 agent vs skill distinction
T08 skill vs workflow distinction
T09 workflow vs protocol distinction
T10 memory vs knowledge distinction
T11 knowledge vs state distinction
T12 model vs evidence distinction
T13 tool vs interface distinction
T14 research vs canon distinction
T15 archive active dependency detection
T16 duplicate-authority detection
T17 domain-to-core leakage detection
T18 artifact primary-owner uniqueness
T19 cross-layer references preserved
T20 move manifest validity
T21 broken-link detection after move
T22 provenance persistence after move
T23 unknown owner remains UNKNOWN/GAP
T24 placeholder does not count as implementation
T25 canonical filename has no improper version suffix
```

---

# 118. Placement Audit Output

```yaml
AMOSPlacementAudit:
  scanned_artifacts:

  correctly_placed:

  conditional:

  misplaced:

  duplicated:

  orphaned:

  cross_layer_conflicts:

  unknown_owner:

  migration_candidates: []

  critical_gaps: []

  conclusion_class:
```

---

# 119. Hard Placement Laws

```text
P01 PRIMARY RESPONSIBILITY DETERMINES OWNER

P02 ONE ARTIFACT SHOULD HAVE ONE PRIMARY OWNER

P03 CROSS-LAYER USE DOES NOT CREATE CROSS-LAYER OWNERSHIP

P04 LOCATION DOES NOT GRANT AUTHORITY

P05 FOLDER DOES NOT DETERMINE EPISTEMIC CLASS

P06 FILE EXTENSION DOES NOT DETERMINE LAYER

P07 CANON DOES NOT MEAN IMPLEMENTED

P08 KERNEL MUST NOT ABSORB POLICY

P09 CONTROL PLANE MUST NOT ABSORB ALL RUNTIME

P10 AGENT MUST NOT ABSORB SKILLS/TOOLS/AUTHORITY

P11 MEMORY MUST NOT SUBSTITUTE FOR KNOWLEDGE

P12 KNOWLEDGE MUST NOT SUBSTITUTE FOR STATE

P13 MODEL MUST NOT SUBSTITUTE FOR EVIDENCE

P14 RESEARCH MUST NOT SILENTLY BECOME CANON

P15 ARCHIVE MUST PRESERVE LINEAGE

P16 PLACEHOLDER MUST NOT COUNT AS IMPLEMENTATION

P17 UNKNOWN OWNER MUST REMAIN UNKNOWN/GAP

P18 MOVES MUST PRESERVE PROVENANCE

P19 MOVES MUST PRESERVE DEPENDENCY CLOSURE

P20 VERSION EVOLUTION MUST NOT REQUIRE CANONICAL FILENAME CHURN

P21 DOMAIN-SPECIFIC SUCCESS DOES NOT PROVE CORE-GENERALITY

P22 RELATIONSHIPS SHOULD BE LINKS, NOT DUPLICATED SOURCES OF TRUTH

P23 RUNTIME STATE BELONGS IN STATE, NOT ONLY DOCUMENTATION

P24 TESTS VERIFY OWNERS; THEY DO NOT OWN THE IMPLEMENTATION

P25 OBSERVABILITY REPORTS BEHAVIOR; IT DOES NOT GOVERN IT
```

---

# 120. RSCF Node

```yaml
node_id: AMOS_OS_PLACEMENT_RULES

node_type: placement_standard

domain: AMOS_OS

functional_type:
  REPOSITORY_GOVERNANCE
  OWNERSHIP_ROUTING

lifecycle_stage:
  ACTIVE_STANDARD

origin_architect:
  Trang Phan

claim_class:
  AMOS_MODEL

claim: >
  AMOS OS artifacts should be placed according to their primary semantic
  responsibility and ownership boundary, with canon, mechanism, authority,
  runtime execution, cognition, agents, capabilities, state, knowledge,
  models, tools, verification, domains, research, operations, and archive
  kept structurally distinct.

premises:
  - semantic responsibilities are separable across AMOS OS layers
  - cross-layer dependency does not imply shared ownership
  - duplicate authoritative copies create drift risk
  - placement affects architectural clarity and dependency governance
  - artifact identity should survive safe moves

dependencies:
  - "[[00_ROOT/ARCHITECTURE.md]]"
  - "[[00_ROOT/FULL_TREE.md]]"
  - "[[00_ROOT/SYSTEM_MAP.md]]"
  - "[[00_ROOT/DEPENDENCY_MAP.md]]"
  - "[[00_ROOT/NAMING_STANDARD.md]]"
  - "[[00_ROOT/AUTHORITATIVE_STATE.md]]"

hard_invariants:
  - Capability != Authority
  - Memory != Knowledge
  - Knowledge != State
  - Model != Evidence
  - Research != Canon
  - Placeholder != Implementation
  - Location != Authority
  - UnknownOwner != Pass

does_not_establish:
  - complete repository compliance
  - correctness of all current placements
  - implementation completeness
  - runtime availability of every listed subsystem

falsifiers:
  - approved root architecture adopts materially different ownership boundaries
  - canonical FULL_TREE supersedes these placement rules
  - executable dependency constraints require a reviewed alternative ownership model

confidence_ceiling:
  placement_architecture: high
  repository_compliance: unknown_until_audited
```

---

# 121. Changelog

## v2.0.0 — 2026-08-25

Expanded the original placement table into a complete AMOS OS ownership and routing standard.

Added:

* full metadata and versioning;
* primary ownership rule;
* placement firewall;
* canonical responsibility map for `01–25`;
* Canon / Kernel / Control Plane separation;
* Runtime and Cognitive Organism boundaries;
* Agent / Skill / Workflow / Protocol separation;
* Memory / Knowledge / State separation;
* Models / Tools / Interfaces / Schemas;
* Observability / Security / Tests / Operations;
* Domains / Research / Operating Model / Archive / Cognitive Matrix;
* cross-layer composition rules;
* RSCF/GMEF/provenance placement;
* state/recovery/authority decomposition;
* mode placement;
* tool permission separation;
* registry/index/map/ledger placement;
* code/Markdown extension firewall;
* root pollution prevention;
* placeholder placement;
* placement conflict and tie-break rules;
* migration classes;
* layer ownership migration rules;
* archive lineage rules;
* domain-to-core promotion rules;
* dependency closure;
* placement audit model;
* failure registry;
* expanded naming prefixes;
* no canonical filename version suffix rule;
* supersession semantics;
* root-to-leaf decision tree;
* ambiguity-resolution table;
* promotion/demotion gates;
* migration manifest;
* 25-test placement suite;
* 25 hard placement laws;
* RSCF node.

## v1.0.0

Initial placement contract defined:

```text
01_CANON             source laws
02_KERNEL            deterministic operators
03_CONTROL_PLANE     policy/authority
04_RUNTIME           runtime harness
05_COGNITIVE_ORGANISM
06_AGENTS
07_SKILLS
08_WORKFLOWS
09_PROTOCOLS
10_MEMORY
11_KNOWLEDGE
12_STATE
13_MODELS
14_TOOLS
15_INTERFACES
16_SCHEMAS
17_OBSERVABILITY
18_SECURITY
19_TESTS
20_OPERATIONS
21_DOMAINS
22_RESEARCH
23_OPERATING_MODEL
24_ARCHIVE
```

and the original prefix / no-filename-version rules.

---

# 122. Final Placement Law

The entire standard reduces to:

```text
WHAT DEFINES?
→ CANON

WHAT COMPUTES?
→ KERNEL

WHAT GOVERNS?
→ CONTROL PLANE

WHAT RUNS?
→ RUNTIME

WHAT COGNIZES?
→ COGNITIVE ORGANISM

WHO WORKS?
→ AGENT

HOW IS CAPABILITY REUSED?
→ SKILL

HOW ARE STEPS ORCHESTRATED?
→ WORKFLOW

HOW DO COMPONENTS INTERACT?
→ PROTOCOL

WHAT IS REMEMBERED?
→ MEMORY

WHAT IS KNOWN?
→ KNOWLEDGE

WHAT IS CURRENT?
→ STATE

WHAT REPRESENTS?
→ MODEL

WHAT PROVIDES CAPABILITY?
→ TOOL

WHAT EXPOSES A BOUNDARY?
→ INTERFACE

WHAT TYPES DATA?
→ SCHEMA

WHAT OBSERVES?
→ OBSERVABILITY

WHAT SECURES?
→ SECURITY

WHAT VERIFIES?
→ TESTS

WHAT OPERATES THE SYSTEM?
→ OPERATIONS

WHAT SPECIALIZES?
→ DOMAINS

WHAT EXPLORES?
→ RESEARCH

WHO GOVERNS ORGANIZATIONALLY?
→ OPERATING MODEL

WHAT IS SUPERSEDED?
→ ARCHIVE
```

The primary invariant is:

> **Every artifact should live where its primary responsibility is owned, while its dependencies and relationships remain explicit links rather than duplicated sources of truth.**

The second invariant is:

> **Placement expresses architectural ownership; it does not by itself prove authority, implementation, validation, or epistemic truth.**

The third invariant is:

> **If ownership cannot be established from source-backed semantics, preserve `UNKNOWN/GAP` instead of placing by intuition.**

The fourth invariant is:

> **Canonical filenames remain stable; evolution is recorded through metadata, provenance, supersession, hashes, revisions, and change records rather than filename-version churn.**

---

**Related:** [[00_ROOT/MOC.md|MOC]] · [[00_ROOT/ARCHITECTURE.md|Architecture]] · [[00_ROOT/FULL_TREE.md|Full Tree]] · [[00_ROOT/SYSTEM_MAP.md|System Map]] · [[00_ROOT/DEPENDENCY_MAP.md|Dependency Map]] · [[00_ROOT/AUTHORITATIVE_STATE.md|Authoritative State]] · [[00_ROOT/NAMING_STANDARD.md|Naming Standard]] · [[00_ROOT/ROADMAP.md|Roadmap]] · [[00_ROOT/NEURAL_NETWORK.md|Neural Network]] · [[01_CANON/00_INDEX/CANON_MAP.md|CANON]] · [[02_KERNEL/00_INDEX/KERNEL_MAP.md|KERNEL]] · [[03_CONTROL_PLANE/00_INDEX/CONTROL_PLANE_MAP.md|CONTROL_PLANE]] · [[21_DOMAINS/00_INDEX/DOMAIN_ALIAS_MAP.md|DOMAINS]] · [[24_ARCHIVE/00_LEGACY/README.md|ARCHIVE]]

```
```
