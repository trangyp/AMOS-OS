---
type: rule
source: 00_ROOT
artifact_id: AMOS-OS-ROOT
name: AMOS_OS
title: AMOS OS — Placement Rules
document_version: 2.0.0
architecture_contract_version: 1.0.0
amos_core_target: v4.4
status: ACTIVE_ROOT
conclusion_class: AMOS_MODEL
rscf_state: derived
canon_group: tech-ai
canon_type: root-architecture
origin_architect: Trang Phan
steward: Trang Phan
created: '2026-08-25'
updated: '2026-08-25'
tags:
- amos
- amos_os
- root
- amos-os
- operating-system
- cognitive-operating-system
- system-architecture
- infrastructure
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
- provenance
- rscf
- gmef
- hml
- observability
- security
- tests
- operations
- domains
- modes
- research
- archive
- cognitive-matrix
- governance
- authority
- provenance-topology
- dependency-closure
- failure-recovery
- canon-group/tech-ai
- canon/architecture
- rscf/claim
- rscf/provenance
- rscf/state/derived
- topic/amos-os
- topic/system-architecture
- topic/cognitive-infrastructure
- 00-root-moc
- neural-network
- architecture
- full-tree
- system-map
- dependency-map
- authoritative-state
- 00-root-naming-standard
- roadmap
- canon-map
- kernel-map
- control-plane-map
- runtime-map
- cognitive-organism-map
- agent-map
- skill-map
- workflow-map
- protocol-map
- memory-memory-map
- amos-full-brain-os-architecture
- state-state-map
- model-map
- tool-map
- interface-map
- schema-map
- observability-observability-map
- security-map
- test-map
- operations-map
- domain-alias-map
- index-research-readme
- operating-model
- legacy-archive-readme
- cognitive-matrix-architecture
- amos-moc
- 00-home
- amos-rscf-nodes
- 00-cosmo-brain-moc
aliases:
- AMOS OS - AMOS Operating System - AMOS Cognitive Operating System - AMOS Universal
  Operating
---

# AMOS OS
**Origin architect / steward:** Trang Phan
> **Status:** `ACTIVE_ROOT`
> **AMOS_CORE target:** `v4.4`
> **Conclusion class:** `AMOS_MODEL`
AMOS OS is the governed infrastructure, cognition, knowledge, agent, skill, workflow, memory, control, runtime, and operations architecture of the AMOS ecosystem.
It is intentionally separated into authoritative planes so that:
```text
KNOWLEDGE
does not become
AUTHORITY
CAPABILITY
does not become
PERMISSION
RUNTIME
does not become
CANON
MODEL
does not become
OBSERVATION
```
The operating principle is:
> **Integrity > completeness > fluency > speed > token savings.**
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: root_index
---


# 1. Root Architecture

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

Cross-cutting substrates:

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

Supporting evolutionary planes:

```text
DOMAINS
RESEARCH
OPERATING MODEL
ARCHIVE
COGNITIVE MATRIX
```

---

# 2. Critical Laws

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

MODEL != OBSERVATION

MODEL != AUTHORITY

TOOL != PERMISSION

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

IMPLEMENTATION != VALIDATION

PLACEHOLDER != IMPLEMENTATION

UNKNOWN/GAP != PASS
```

---

# 3. System Purpose

AMOS OS exists to provide a stable architecture for:

```text
reasoning
coordination
knowledge
memory
state
authority
execution
validation
recovery
evolution
```

while preserving explicit ownership and provenance.

Its role is not to merge every subsystem into one engine.

Its role is to ensure those subsystems can compose without losing their boundaries.

---

# 4. Architectural Principle

AMOS OS follows:

```text
SEPARATE RESPONSIBILITY
+
EXPLICIT INTERFACE
+
TYPED STATE
+
GOVERNED AUTHORITY
+
PERSISTENT PROVENANCE
+
LOCAL FAILURE RECOVERY
```

The system should become more capable by adding composable layers, not by weakening separation.

---

# 5. Primary Planes

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
25_COGNITIVE_MATRIX
```

Each plane has one primary responsibility.

---

# 6. `00_ROOT`

Root owns cross-system orientation.

```text
README
MOC
NEURAL_NETWORK
ARCHITECTURE
FULL_TREE
SYSTEM_MAP
DEPENDENCY_MAP
AUTHORITATIVE_STATE
NAMING_STANDARD
PLACEMENT_RULES
ROADMAP
```

Root should not contain arbitrary implementation logic.

---

# 7. `01_CANON`

Canon defines what AMOS says must remain structurally true.

Canon owns:

```text
laws
definitions
semantic invariants
identity contracts
architecture laws
governance principles
```

Hard rule:

```text
CANON
defines semantics

CANON
does not prove implementation
```

---

# 8. `02_KERNEL`

Kernel owns deterministic or tightly constrained operators.

Examples:

```text
normalization
RSCF operations
dependency closure
validation primitives
state transition functions
hashing
identity resolution
provenance graph operations
```

Kernel should be reusable across higher layers.

---

# 9. Kernel Firewall

```text
Mechanism
→ KERNEL

Permission
→ CONTROL PLANE

Execution
→ RUNTIME
```

Example:

```text
calculate dependency closure
→ KERNEL

decide closure is sufficient
→ CONTROL PLANE

run admitted task
→ RUNTIME
```

---

# 10. `03_CONTROL_PLANE`

Control Plane owns:

```text
authority
policy
admission
routing governance
commit permission
mode governance
risk escalation
resource governance
provenance admission
lifecycle decisions
```

Central rule:

```text
WorkerCapability
!=
ControlPlaneAuthority
```

---

# 11. Authority Boundary

No agent, skill, model, or tool should self-promote into authority.

```text
AGENT
may propose

SKILL
may compute

MODEL
may estimate

TOOL
may provide capability

CONTROL PLANE
decides whether action is admissible
```

---

# 12. `04_RUNTIME`

Runtime owns live orchestration.

Examples:

```text
sessions
tasks
steps
ticks
epochs
schedulers
routers
execution harnesses
active mode
commit state
recovery state
```

Hard rule:

```text
ArchitectureSpecification
!=
LiveRuntimeState
```

---

# 13. Runtime State Machine

Generic lifecycle:

```text
UNINITIALIZED
↓
INITIALIZING
↓
READY
↓
ACTIVE
↓
VALIDATING
↓
COMMITTING
↓
COMMITTED
```

Failure branches:

```text
BLOCKED
DEGRADED
FAILED
IN_DOUBT
ROLLING_BACK
ROLLED_BACK
QUARANTINED
TERMINATED
```

---

# 14. `05_COGNITIVE_ORGANISM`

The Cognitive Organism coordinates cognitive subsystems.

Potential layers:

```text
perception
attention
working cognition
hypotheses
reasoning
metacognition
memory interaction
uncertainty
identity continuity models
expression
```

This is an architectural model.

It does not by itself establish literal biological consciousness or subjective experience.

---

# 15. Cognitive Organism Firewall

```text
COGNITIVE ORGANISM
!=
AGENT
```

The organism is system-level cognitive coordination.

An agent is a scoped role-based worker.

---

# 16. `06_AGENTS`

Agents perform scoped work.

Every agent should define:

```text
identity
role
scope
inputs
outputs
capabilities
dependencies
authority boundary
memory policy
provenance
tests
failure modes
recovery
```

---

# 17. Agent Firewall

```text
AgentName
!=
Capability

Capability
!=
Authority

AgentOutput
!=
Commit
```

An `Executor_Agent` is not automatically a live executor.

An `Investment_Agent` is not automatically a financial adviser or trading system.

Implementation evidence determines capability.

---

# 18. `07_SKILLS`

Skills are reusable procedures.

A skill answers:

> **How do we perform a bounded capability?**

Expected structure:

```text
trigger
purpose
prerequisites
domain model
decision gates
steps
verification
pitfalls
dependencies
conclusion class
```

---

# 19. Agent vs Skill

```text
AGENT
=
who/what role performs work

SKILL
=
how a bounded capability is performed
```

An agent may invoke many skills.

A skill may be reused by many agents.

---

# 20. `08_WORKFLOWS`

Workflows sequence multiple steps or capabilities.

Typical:

```text
TRIGGER
↓
PRECONDITIONS
↓
RETRIEVAL
↓
ANALYSIS
↓
VALIDATION
↓
COMMIT / EXPORT
↓
VERIFY
↓
STORE LEARNING
```

---

# 21. Skill vs Workflow

```text
SKILL
=
bounded capability

WORKFLOW
=
orchestration across capabilities
```

A workflow may invoke:

```text
agents
skills
tools
protocols
tests
state transitions
```

---

# 22. `09_PROTOCOLS`

Protocols define interaction contracts.

Examples:

```text
agent ↔ agent
agent ↔ skill
agent ↔ tool
runtime ↔ state
control plane ↔ runtime
authority ↔ execution
knowledge ↔ provenance
```

Protocol answers:

> **How do independent components exchange state or control?**

---

# 23. Workflow vs Protocol

```text
WORKFLOW
=
sequence

PROTOCOL
=
interaction contract
```

A workflow may follow several protocols.

A protocol can exist independently of a particular workflow.

---

# 24. `10_MEMORY`

Memory stores retained experience.

Possible classes:

```text
working memory
episodic memory
case memory
negative memory
validated long-term memory
```

Hard rule:

```text
REMEMBERED
!=
VALIDATED
```

---

# 25. Memory vs Knowledge

```text
MEMORY
=
what the system retained

KNOWLEDGE
=
what the system admitted as reusable evidence/claims
```

A memory may later become knowledge after validation.

---

# 26. `11_KNOWLEDGE`

Knowledge stores:

```text
evidence
claims
RSCFs
framework knowledge
validated mappings
source-bound concept notes
knowledge capsules
```

Important knowledge should carry:

```text
claim class
source
provenance
scope
regime
freshness
dependencies
falsifiers
competing claims
```

---

# 27. Epistemic Classes

AMOS uses typed evidence classes.

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

# 28. `12_STATE`

State represents what is currently active or authoritative.

Possible state classes:

```text
AUTHORITATIVE
WORKING
SHADOW
PENDING
RECOVERY
COMMITTED
QUARANTINED
```

Examples:

```text
active session state
agent state
mode state
authority state
runtime state
working hypotheses
commit state
```

---

# 29. Memory / Knowledge / State Firewall

```text
MEMORY
!=
KNOWLEDGE
!=
STATE
```

Example:

```text
historical user preference
→ MEMORY

validated principle
→ KNOWLEDGE

currently selected operating mode
→ STATE
```

---

# 30. `13_MODELS`

Models represent structured interpretations.

Examples:

```text
causal models
world models
risk models
forecast models
simulation models
cognitive models
domain models
calibration models
```

Hard rule:

```text
MODEL
!=
OBSERVATION
```

---

# 31. Model Contract

A consequential model should identify:

```text
model_id
version
purpose
scope
inputs
outputs
assumptions
regime
dependencies
calibration
falsifiers
limitations
```

---

# 32. Model Authority Firewall

```text
HighModelConfidence
!=
Authority
```

A model may support a proposal.

It cannot grant itself execution permission.

---

# 33. `14_TOOLS`

Tools provide capability.

Examples:

```text
filesystem
browser
search
database
compiler
calculator
API connector
market data
external executor
```

Hard rule:

```text
TOOL AVAILABLE
!=
TOOL PERMITTED
```

---

# 34. Tool vs Permission

```text
Tool
→ provides capability

Control Plane
→ decides admissibility

Security
→ validates access / credentials

Runtime
→ coordinates invocation
```

This separation prevents capability leakage into authority.

---

# 35. `15_INTERFACES`

Interfaces expose AMOS boundaries.

Examples:

```text
API
MCP
CLI
UI
agent interfaces
tool interfaces
external service contracts
```

Interface defines how external callers communicate with a system.

---

# 36. `16_SCHEMAS`

Schemas define typed structures.

Examples:

```text
AGENT_SCHEMA
STATE_SCHEMA
RSCF_NODE_SCHEMA
MODE_SCHEMA
EXECUTION_REQUEST_SCHEMA
AUTHORITY_SCHEMA
```

Schema does not own runtime behavior.

---

# 37. `17_OBSERVABILITY`

Observability records system behavior.

```text
logs
traces
metrics
events
health
runtime diagnostics
audit telemetry
```

Hard rule:

```text
OBSERVED
!=
CORRECT
```

Observability supplies evidence for validation.

---

# 38. `18_SECURITY`

Security owns security-specific controls.

Examples:

```text
authentication
authorization mechanics
secrets
credential handling
threat models
input hardening
least privilege
execution isolation
```

---

# 39. Security vs Control Plane

```text
SECURITY
=
security validity

CONTROL PLANE
=
system admissibility
```

A request may be cryptographically authorized but still violate system policy.

Likewise, policy allowance does not replace credential validation.

---

# 40. `19_TESTS`

Tests verify implementation.

Testing progression:

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

Hard rule:

```text
TEST PASS
!=
UNIVERSAL PROOF
```

---

# 41. `20_OPERATIONS`

Operations owns lifecycle execution.

Examples:

```text
deployment
migration
backup
restore
runbooks
incidents
rollback
release
maintenance
recovery
```

Operations manages the deployed system.

It does not redefine canon.

---

# 42. `21_DOMAINS`

Domains specialize AMOS.

Examples may include:

```text
logic
mathematics
physics
biology
cognition
society
economics
finance
law
strategy
engineering
design
ecology
```

Only domains capable of materially affecting a task should be activated.

---

# 43. Domain Adapter Rule

Domain adapters translate:

```text
DOMAIN SEMANTICS
↔
CORE AMOS CONTRACT
```

Domain-specific assumptions should not silently enter core kernel logic.

---

# 44. Modes

Modes configure behavior.

Examples:

```text
reasoning modes
attention modes
epistemic modes
decision modes
scale modes
world-model modes
recovery modes
execution modes
freshness modes
lifecycle modes
```

Hard rule:

```text
MODE
!=
AGENT
```

unless a mode actually has an independent agent contract.

---

# 45. `22_RESEARCH`

Research stores experimental or not-yet-promoted material.

Examples:

```text
papers
experiments
candidate laws
new models
prototype systems
external evidence
benchmark studies
unresolved hypotheses
```

Hard rule:

```text
RESEARCH
!=
CANON
```

---

# 46. Research Promotion Path

```text
RESEARCH
↓
SOURCE BINDING
↓
FORMALIZATION
↓
PROVENANCE
↓
CONTRADICTION CHECK
↓
SCOPE / REGIME CHECK
↓
VALIDATION
↓
KNOWLEDGE
↓
OPTIONAL CANON GOVERNANCE
↓
CANON
```

---

# 47. `23_OPERATING_MODEL`

Operating Model defines organizational governance.

Examples:

```text
roles
responsibilities
decision rights
review forums
change control
maintenance
stewardship
```

This is distinct from runtime control-plane authority.

---

# 48. `24_ARCHIVE`

Archive preserves superseded lineage.

```text
legacy systems
deprecated components
old architecture
historical canon
migration snapshots
retired schemas
```

Hard rule:

```text
ARCHIVE
!=
DELETE
```

---

# 49. Archive Lineage

A superseded artifact should retain:

```text
artifact_id
version
old path
superseded_by
reason
date
provenance
```

Historical identity should remain recoverable.

---

# 50. `25_COGNITIVE_MATRIX`

The Cognitive Matrix stores cross-cognitive topology.

Possible relationships:

```text
agent ↔ mode
mode ↔ memory
attention ↔ cognition
knowledge ↔ reasoning
state ↔ hypotheses
domain ↔ agent
model ↔ cognition
```

It does not become a duplicate source of truth.

---

# 51. H/M/L Architecture

AMOS recursively decomposes systems into:

```text
H
=
high-level law / mission / macro context

M
=
mediating subsystem / architecture / coordination layer

L
=
local component / action / evidence / event
```

For AMOS OS:

```text
H
=
CANON
ARCHITECTURE
DOMAIN

M
=
KERNEL
CONTROL PLANE
RUNTIME
COGNITIVE ORGANISM
AGENT FAMILY

L
=
COMPONENT
TOOL CALL
STATE UPDATE
CLAIM
EVENT
```

---

# 52. H/M/L Integrity Rule

A local improvement is valid only if it does not destroy higher-level integrity.

```text
Accept(LocalChange)
only if

L remains viable
∧
M remains viable
∧
H remains viable
```

Therefore:

```text
speed gain
```

must be rejected if it causes:

```text
authority bypass
provenance loss
state corruption
canon violation
semantic drift
unrecoverable mutation
```

---

# 53. Fractal Retrieval

Preferred retrieval path:

```text
BOOTSTRAP
↓
H
↓
M
↓
L
↓
RAW EVIDENCE
```

Only descend when deeper retrieval can materially change the answer.

Raw evidence should not be loaded by default merely because it exists.

---

# 54. Smallest Sufficient Proof Scope

AMOS v4.4 operating principle:

```text
USE THE SMALLEST PROOF SCOPE
THAT CAN SAFELY SUPPORT THE RESULT
```

Local reasoning is permitted only when:

```text
dependency closure
scope compatibility
regime compatibility
freshness
provenance sufficiency
non-conflict
```

are established.

---

# 55. Escalation Conditions

Escalate when:

```text
shared evidence ancestry
contradictory evidence
stale state
regime shift
causal ambiguity
governance impact
irreversible action
dependency ambiguity
scope mismatch
```

Fast path does not mean skipping validation.

---

# 56. RSCF

RSCF is a first-class reasoning/provenance structure.

Important conclusions should conceptually carry:

```yaml
RSCF:
  claim:
  claim_class:
  premises:
  evidence:
  provenance:
  scope:
  regime:
  temporal_validity:
  dependencies:
  competing_hypotheses:
  falsifiers:
  confidence_ceiling:
```

---

# 57. Selective Invalidation

If premise `P` fails:

```text
INVALIDATE P
+
INVALIDATE DEPENDENTS(P)
```

Do not invalidate unrelated branches.

This enables local repair rather than destructive global recomputation.

---

# 58. Provenance Topology

AMOS treats source ancestry as load-bearing.

Hard rule:

```text
10 copies of one source
!=
10 independent confirmations
```

Important evidence should track:

```text
source identity
source ancestry
dependency edges
freshness
scope
regime
correlation risk
```

---

# 59. Confidence Ceiling

Derived confidence cannot exceed the weakest load-bearing premise unless that premise is independently revalidated.

Conceptually:

```text
Confidence(Result)
<=
min(
  Confidence(load-bearing premises)
)
```

unless independent evidence raises the floor.

---

# 60. Competing Hypotheses

AMOS must preserve incompatible hypotheses when evidence cannot discriminate.

```text
H1
H2
H3
```

may remain:

```text
COMPETING
```

instead of forcing:

```text
WINNER
```

The preferred next step is the cheapest high-information discriminating test.

---

# 61. Causal Firewall

AMOS distinguishes:

```text
association
correlation
mechanism
enabling condition
necessary condition
sufficient condition
mediation
confounding
feedback
causal effect
```

Hard rule:

```text
STRUCTURAL SIMILARITY
!=
CAUSATION
```

---

# 62. Scope / Regime Firewall

Important conclusions inherit:

```yaml
Applicability:
  system:
  population:
  environment:
  scale:
  time:
  regime:
  measurement_method:
  assumptions:
```

A regime change can invalidate previously valid conclusions.

---

# 63. Freshness

State and evidence should carry freshness where relevant.

Possible:

```text
CURRENT
FRESH
AGING
STALE
EXPIRED
UNKNOWN
```

Hard rule:

```text
STALE
!=
CURRENT
```

---

# 64. Freshness Revalidation

When a load-bearing premise becomes stale:

```text
REVALIDATE
```

before consequential reuse.

Do not silently carry old confidence into a changed regime.

---

# 65. GMEF

GMEF governs model/evolution lineage.

Conceptual path:

```text
CURRENT MODEL
↓
MUTATION PROPOSAL
↓
EVALUATION
↓
VALIDATION
↓
ADMISSION / REJECTION
↓
NEW VERSION OR ROLLBACK
```

Evolution must remain governed.

---

# 66. Governed Evolution

Self-modification should not mean unrestricted mutation.

Required controls may include:

```text
proposal identity
source
diff
dependencies
tests
compatibility
authority
rollback
provenance
```

Hard rule:

```text
EVOLUTION
!=
UNBOUNDED SELF-MODIFICATION
```

---

# 67. Transaction Boundary

For coupled consequential state changes:

```text
ALL REQUIRED CHANGES
```

should either become authoritative together or fail according to an explicit transaction policy.

Possible semantics:

```text
ATOMIC
SAGA / COMPENSATION
BEST_EFFORT
```

Do not imply atomicity without implementation.

---

# 68. MVCC / CAS Concepts

AMOS may use concepts such as:

```text
MVCC
CAS
state versions
epochs
fencing
```

to reason about concurrent state.

Architecture concept:

```text
ObservedVersion
must still satisfy
CommitPrecondition
```

at commit time.

These patterns do not prove the current runtime literally implements a distributed database.

---

# 69. Epoch Finality

Consequential state may carry:

```text
epoch
parent
commit status
finality
```

to distinguish:

```text
current
stale
superseded
committed
in_doubt
```

---

# 70. Proposal / Commit Firewall

```text
PROPOSAL
!=
COMMIT
```

General path:

```text
CANDIDATE
↓
VALIDATION
↓
AUTHORITY
↓
PREPARE
↓
REVALIDATE
↓
COMMIT
↓
VERIFY
↓
RECEIPT
```

---

# 71. External Effects

External effects may include:

```text
file mutation
database mutation
message send
financial action
external API write
deployment
security configuration
physical-system action
```

Such actions require stronger governance than read-only reasoning.

---

# 72. Reversibility

Every consequential effect should be classed:

```text
REVERSIBLE
PARTIALLY_REVERSIBLE
COMPENSATABLE
IRREVERSIBLE
UNKNOWN
```

Hard rule:

```text
UNKNOWN REVERSIBILITY
+
HIGH IMPACT
→
ESCALATE
```

---

# 73. Failure Architecture

Failure handling:

```text
DETECT
↓
CLASSIFY
↓
FREEZE AFFECTED EDGE
↓
PRESERVE VALID STATE
↓
INVALIDATE DEPENDENTS
↓
ROLL BACK / COMPENSATE
↓
REROUTE
↓
REVALIDATE
```

---

# 74. Recovery Principle

Prefer recovery that is:

```text
local
reversible
dependency-aware
provenance-preserving
```

Global recomputation is a last resort.

---

# 75. Failure States

```text
BLOCKED
FAILED
PARTIAL
DEGRADED
IN_DOUBT
ROLLING_BACK
ROLLED_BACK
COMPENSATED
QUARANTINED
RECOVERING
RESTORED
```

Do not collapse materially different failure states into generic `ERROR`.

---

# 76. `IN_DOUBT`

`IN_DOUBT` is required when the system cannot establish whether an external effect occurred.

Hard rule:

```text
UNKNOWN OUTCOME
!=
FAILED
```

and:

```text
UNKNOWN OUTCOME
!=
SUCCESS
```

---

# 77. Observability vs Provenance

```text
TRACE
=
operational history

PROVENANCE
=
epistemic / lineage history
```

They may overlap but are not equivalent.

---

# 78. Security Invariant

Security should preserve:

```text
least privilege
bounded scope
revocability
traceability
failure isolation
secret minimization
```

Tool possession or credentials must not silently create unrestricted authority.

---

# 79. Knowledge Harvest

Canonical path:

```text
EPHEMERAL OUTPUT
↓
PERSISTENT EVIDENCE
↓
PROVENANCE
↓
VALIDATION
↓
VALIDATED KNOWLEDGE
```

Documentation claims remain:

```text
SOURCE_CLAIM
```

until validated.

---

# 80. Memory Promotion

```text
MEMORY
↓
EVIDENCE REVIEW
↓
PROVENANCE CHECK
↓
VALIDATION
↓
KNOWLEDGE
```

Do not promote remembered information by repetition.

---

# 81. Research Promotion

```text
RESEARCH
↓
EVIDENCE
↓
FORMALIZATION
↓
FALSIFIERS
↓
VALIDATION
↓
KNOWLEDGE
↓
GOVERNANCE
↓
CANON
```

---

# 82. Domain Promotion

A domain-specific mechanism may enter core only if:

```text
cross-domain reuse established
domain assumptions removed or typed
scope generalized
tests generalized
dependencies known
governance accepted
```

Success in one domain is not proof of universality.

---

# 83. Version Axes

AMOS maintains separate version dimensions.

```text
AMOS_CORE_VERSION
ARCHITECTURE_VERSION
DOCUMENT_VERSION
COMPONENT_VERSION
SCHEMA_VERSION
MODEL_VERSION
PROTOCOL_VERSION
WORKFLOW_VERSION
SKILL_VERSION
DATASET_VERSION
```

These must not be collapsed.

---

# 84. Canonical Filename Rule

Canonical filenames should remain stable.

Prefer:

```text
ARCHITECTURE.md
```

with:

```yaml
document_version: "2.0.0"
```

rather than:

```text
ARCHITECTURE_v2_FINAL.md
```

Evolution is carried through:

```text
metadata
hashes
revision history
supersession
provenance
change records
```

---

# 85. Identity Firewall

Distinct fields:

```text
filename
path
artifact_id
registry_name
semantic_identity
version_identity
runtime_instance_id
provenance_identity
```

Hard rule:

```text
PATH
!=
IDENTITY
```

---

# 86. Placement Rule

Artifacts belong where their primary responsibility is owned.

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

WHAT EXPOSES?
→ INTERFACE

WHAT TYPES?
→ SCHEMA

WHAT OBSERVES?
→ OBSERVABILITY

WHAT SECURES?
→ SECURITY

WHAT VERIFIES?
→ TESTS

WHAT OPERATES?
→ OPERATIONS

WHAT SPECIALIZES?
→ DOMAINS

WHAT EXPLORES?
→ RESEARCH

WHAT GOVERNS ORGANIZATIONALLY?
→ OPERATING MODEL

WHAT IS SUPERSEDED?
→ ARCHIVE
```

---

# 87. Root Dependency Graph

```text
01_CANON
   ↓
02_KERNEL
   ↓
03_CONTROL_PLANE
   ↓
04_RUNTIME
   ↓
05_COGNITIVE_ORGANISM
   ↓
06_AGENTS
   ↓
07_SKILLS / 08_WORKFLOWS / 09_PROTOCOLS
   ↓
14_TOOLS / 15_INTERFACES
```

Cross-cutting:

```text
10_MEMORY
11_KNOWLEDGE
12_STATE
13_MODELS
16_SCHEMAS
17_OBSERVABILITY
18_SECURITY
19_TESTS
20_OPERATIONS
```

Evolution / specialization:

```text
21_DOMAINS
22_RESEARCH
23_OPERATING_MODEL
24_ARCHIVE
25_COGNITIVE_MATRIX
```

---

# 88. Minimum Reasoning Path

For low-risk work:

```text
INPUT
↓
OBJECTIVE
↓
SCOPE
↓
REQUIRED DEPENDENCIES
↓
MINIMUM EVIDENCE
↓
REASON
↓
VALIDATE
↓
RETURN
```

Do not activate every AMOS subsystem by default.

---

# 89. Consequential Reasoning Path

For high-stakes work:

```text
INPUT
↓
OBJECTIVE
↓
SCOPE
↓
STAKE CLASS
↓
AUTHORITY
↓
DEPENDENCY CLOSURE
↓
EVIDENCE
↓
PROVENANCE
↓
COMPETING HYPOTHESES
↓
CAUSAL CHECK
↓
REGIME CHECK
↓
SENSITIVITY
↓
ADVERSARIAL VALIDATION
↓
DECISION
↓
OPTIONAL EFFECT
↓
RECEIPT
↓
POST-CONDITION VALIDATION
```

---

# 90. Sensitivity Rule

Identify the smallest premise, threshold, or observation capable of changing the conclusion.

Test that first.

If the outcome flips easily:

```text
CONDITIONAL
```

If it survives plausible perturbation:

```text
ROBUST WITHIN DECLARED SCOPE
```

---

# 91. Adversarial Validation

Consequential conclusions should be challenged for:

```text
contradiction
shared source ancestry
stale premises
scope leakage
hidden dependency
causal overreach
stronger alternatives
regime mismatch
```

If the challenge succeeds:

```text
downgrade
condition
preserve COMPETING
or
return UNKNOWN/GAP
```

---

# 92. Capability Limits

AMOS OS architecture does not establish:

```text
literal consciousness
subjective experience
embodiment
perfect prediction
perfect knowledge
unbounded autonomous agency
automatic external authority
complete implementation
universal empirical validity
```

These claims require independent evidence.

---

# 93. Structural Model Firewall

AMOS may contain:

```text
biological models
cognitive models
quantum-fractal models
somatic models
consciousness models
universal architecture models
```

These are treated as:

```text
MODEL
```

unless independently validated as empirical claims.

---

# 94. Repository Presence Firewall

```text
FILE EXISTS
!=
COMPONENT IMPLEMENTED
```

```text
COMPONENT IMPLEMENTED
!=
TESTED
```

```text
TESTED
!=
VALIDATED FOR ALL USES
```

```text
VALIDATED FOR SCOPE
!=
UNIVERSAL
```

---

# 95. Placeholder Rule

A placeholder reserves architecture.

```text
PLACEHOLDER
=
EXPECTED POSITION EXISTS
```

not:

```text
PLACEHOLDER
=
CAPABILITY EXISTS
```

Unknown detail remains:

```text
UNKNOWN/GAP
```

---

# 96. Authoritative State

Current implementation status belongs in:

```text
AUTHORITATIVE_STATE
```

not inferred from architecture.

Architecture says:

> What should exist and how should it be separated?

Authoritative State says:

> What currently exists and is verified?

---

# 97. Dependency Map

Load-bearing dependencies belong in:

```text
DEPENDENCY_MAP
```

A semantic link is not automatically a dependency.

```text
RELATED_TO
!=
DEPENDS_ON
```

---

# 98. Neural Network

The vault navigation topology belongs in:

```text
NEURAL_NETWORK
```

Its graph edges improve discoverability.

They do not establish:

```text
causation
runtime dependency
authority
validation
```

---

# 99. MOC

The root map of content is:

```text

```

It provides navigation.

It does not replace owning subsystem specifications.

---

# 100. Naming Standard

Naming identity rules are governed by:

```text

```

Key invariant:

```text
Filename
!=
ArtifactIdentity
```

---

# 101. Placement Rules

Repository ownership is governed by:

```text
PLACEMENT_RULES
```

Key invariant:

```text
PrimaryResponsibility
determines
PrimaryOwner
```

---

# 102. Full Tree

Filesystem expectations belong in:

```text
FULL_TREE
```

Hard rule:

```text
EXPECTED TREE
!=
VERIFIED POPULATED TREE
```

---

# 103. System Map

Plane-level navigation belongs in:

```text
SYSTEM_MAP
```

This root file should not duplicate every subsystem map.

---

# 104. Roadmap

Future work belongs in:

```text
ROADMAP
```

Hard rule:

```text
PLANNED
!=
IMPLEMENTED
```

---

# 105. Core Operating Invariants

```text
OS01 CANON != KERNEL
OS02 KERNEL != CONTROL_PLANE
OS03 CONTROL_PLANE != RUNTIME
OS04 RUNTIME != COGNITION
OS05 ORGAN != AGENT
OS06 AGENT != SKILL
OS07 SKILL != WORKFLOW
OS08 WORKFLOW != PROTOCOL
OS09 MEMORY != KNOWLEDGE
OS10 KNOWLEDGE != STATE
OS11 MODEL != OBSERVATION
OS12 MODEL != AUTHORITY
OS13 TOOL != PERMISSION
OS14 CAPABILITY != AUTHORITY
OS15 PROPOSAL != COMMIT
OS16 RESEARCH != CANON
OS17 PLACEHOLDER != IMPLEMENTATION
OS18 IMPLEMENTED != VALIDATED
OS19 UNKNOWN/GAP != PASS
OS20 PATH != IDENTITY
OS21 LINK != DEPENDENCY
OS22 CORRELATION != CAUSATION
OS23 MULTIPLE COPIES != INDEPENDENT EVIDENCE
OS24 STALE != CURRENT
OS25 LOCAL OPTIMIZATION CANNOT BREAK HIGHER-SCALE INTEGRITY
OS26 FAILED PREMISE INVALIDATES DEPENDENTS ONLY
OS27 HIGH-IMPACT ACTION REQUIRES STRONGER GOVERNANCE
OS28 FAST PATH REQUIRES PROOF OF LOCAL SUFFICIENCY
OS29 PROVENANCE MUST SURVIVE TRANSFORMATION
OS30 ARCHIVE MUST PRESERVE LINEAGE
```

---

# 106. Failure Registry

```text
OS-F001 CANON_KERNEL_COLLAPSE
OS-F002 KERNEL_POLICY_LEAK
OS-F003 CONTROL_RUNTIME_COLLAPSE
OS-F004 AGENT_SELF_AUTHORIZATION
OS-F005 TOOL_PERMISSION_LEAK
OS-F006 MEMORY_KNOWLEDGE_COLLAPSE
OS-F007 KNOWLEDGE_STATE_COLLAPSE
OS-F008 MODEL_OBSERVATION_COLLAPSE
OS-F009 RESEARCH_CANON_LEAK
OS-F010 PLACEHOLDER_PROMOTED_AS_IMPLEMENTATION
OS-F011 UNKNOWN_PROMOTED_TO_PASS
OS-F012 STALE_STATE_REUSE
OS-F013 PROVENANCE_LOSS
OS-F014 SOURCE_CORRELATION_OVERCOUNT
OS-F015 CAUSAL_OVERREACH
OS-F016 SCOPE_LEAKAGE
OS-F017 REGIME_MISMATCH
OS-F018 BROKEN_DEPENDENCY_CLOSURE
OS-F019 PARTIAL_COMMIT
OS-F020 IN_DOUBT_HIDDEN
OS-F021 ROLLBACK_FAILURE
OS-F022 AUTHORITY_STALE
OS-F023 ARCHIVED_DEPENDENCY_ACTIVE
OS-F024 DOMAIN_CORE_LEAK
OS-F025 VERSION_IDENTITY_COLLAPSE
OS-F026 PATH_IDENTITY_COLLAPSE
OS-F027 BROKEN_SUPERSESSION_LINEAGE
OS-F028 TEST_SCOPE_OVERCLAIM
OS-F029 FAST_PATH_WITHOUT_PROOF
OS-F030 GLOBAL_RECOMPUTATION_WHEN_LOCAL_REPAIR_SUFFICIENT
```

---

# 107. Validation Pipeline

```text
IDENTITY
↓
SCOPE
↓
DEPENDENCIES
↓
EVIDENCE
↓
PROVENANCE
↓
FRESHNESS
↓
REGIME
↓
CONTRADICTION
↓
CAUSALITY
↓
SENSITIVITY
↓
AUTHORITY
↓
RESULT
```

---

# 108. Component Minimum Contract

Every consequential AMOS component should eventually define:

```yaml
Component:
  artifact_id:
  version:
  owner:
  role:
  scope:
  inputs:
  outputs:
  dependencies:
  capabilities:
  authority:
  state:
  provenance:
  tests:
  failure_modes:
  recovery:
  lifecycle:
  conclusion_class:
```

---

# 109. Agent Minimum Contract

```yaml
Agent:
  agent_id:
  version:

  role:
  system:

  in_scope: []
  out_of_scope: []

  inputs: []
  outputs: []

  capabilities: []

  dependencies: []

  authority:
    allowed: []
    prohibited: []

  memory_policy:

  provenance_policy:

  tests: []

  failure_modes: []

  recovery:
```

---

# 110. Skill Minimum Contract

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

---

# 111. Workflow Minimum Contract

```yaml
Workflow:
  workflow_id:
  version:
  trigger:
  preconditions:
  stages:
  tools:
  checkpoints:
  authority:
  rollback:
  verification:
  outputs:
  provenance:
```

---

# 112. Protocol Minimum Contract

```yaml
Protocol:
  protocol_id:
  version:

  participants: []

  messages: []

  preconditions: []

  state_transitions: []

  timeout:

  retry:

  failure:

  commit:

  rollback:
```

---

# 113. Model Minimum Contract

```yaml
Model:
  model_id:
  version:
  purpose:
  scope:
  regime:
  inputs:
  outputs:
  assumptions:
  dependencies:
  calibration:
  limitations:
  falsifiers:
  status:
```

---

# 114. Tool Minimum Contract

```yaml
Tool:
  tool_id:
  version:
  capability:
  interface:
  inputs:
  outputs:
  authority_required:
  side_effects:
  idempotency:
  rollback:
  security:
  provenance:
```

---

# 115. State Minimum Contract

```yaml
State:
  state_id:
  version:
  state_class:
  owner:
  epoch:
  parent:
  created_at:
  freshness:
  authority:
  provenance:
  status:
```

---

# 116. Proof Capsule

A consequential conclusion should be reconstructable as:

```yaml
ProofCapsule:
  claim:
  class:

  premises: []

  evidence: []

  provenance: []

  scope:

  temporal_validity:

  regime:

  dependencies: []

  competing_explanations: []

  falsifiers: []

  confidence_ceiling:
```

---

# 117. Stop Conditions

Reasoning should stop when:

```text
Claim Sufficiency
+
Decision Sufficiency
+
Action Sufficiency
```

are achieved.

Do not continue expanding reasoning merely because more AMOS modules exist.

---

# 118. Gap Priority

Classify gaps:

```text
CRITICAL
DECISION-RELEVANT
EXPLANATORY
COSMETIC
```

Resolve in that order.

If a critical gap cannot be closed:

```text
RETURN UNKNOWN/GAP
+
MINIMUM MISSING INFORMATION
```

---

# 119. Anti-Fabrication

AMOS OS must not bridge missing logic with fluent prose.

Hard rules:

```text
ABSENCE OF CONTRADICTION
!=
PROOF
```

```text
BENCHMARK SUCCESS
!=
UNIVERSAL VALIDITY
```

```text
STRUCTURAL EQUATION
!=
EMPIRICAL LAW
```

```text
REPORTED LATENCY
!=
HARDWARE-INDEPENDENT GUARANTEE
```

```text
DISTRIBUTED TEST
!=
FORMAL PROOF
```

unless formal proof exists.

---

# 120. Anti-Regression

No optimization may weaken:

```text
factual support
scope correctness
contradiction visibility
provenance recoverability
causal discipline
security
authority boundaries
repairability
user fit
```

If it does:

```text
ROLL BACK
```

---

# 121. 7-Part Persistence Mapping

| Persistence Part  | AMOS OS                                    |
| ----------------- | ------------------------------------------ |
| I — Constraint    | canon, schemas, authority, security        |
| II — Flow         | data, evidence, control, state transitions |
| III — Structure   | planes, modules, agents, interfaces        |
| IV — Enforcement  | control plane, validation, security        |
| V — Time          | versions, epochs, freshness, lifecycle     |
| VI — Adaptation   | learning, models, recovery, evolution      |
| VII — Termination | rollback, failure, deprecation, archive    |

This is an `AMOS_MODEL` mapping.

---

# 122. Root RSCF Node

```yaml
node_id: AMOS_OS_ROOT

node_type: operating_architecture

domain: AMOS_OS

functional_type:
  ROOT_SYSTEM
  COGNITIVE_INFRASTRUCTURE
  GOVERNANCE_ARCHITECTURE

lifecycle_stage:
  ACTIVE_ROOT

origin_architect:
  Trang Phan

claim_class:
  AMOS_MODEL

claim: >
  AMOS OS is a governed multi-plane operating architecture separating
  canon, deterministic kernel mechanisms, control-plane authority,
  runtime execution, cognitive coordination, agents, reusable procedures,
  memory, knowledge, state, models, tools, interfaces, validation,
  operations, domains, research, and historical lineage.

premises:
  - architectural responsibilities must remain separable
  - capability and authority are distinct
  - models and evidence are distinct
  - memory, knowledge, and state are distinct
  - provenance and dependency closure are load-bearing
  - failure should be locally recoverable where possible

dependencies:
  - "ARCHITECTURE"
  - ""
  - "SYSTEM_MAP"
  - "DEPENDENCY_MAP"
  - "AUTHORITATIVE_STATE"
  - ""
  - "PLACEMENT_RULES"

hard_invariants:
  - CAPABILITY != AUTHORITY
  - PROPOSAL != COMMIT
  - MODEL != OBSERVATION
  - MEMORY != KNOWLEDGE
  - KNOWLEDGE != STATE
  - PLACEHOLDER != IMPLEMENTATION
  - UNKNOWN/GAP != PASS
  - PATH != IDENTITY
  - LINK != DEPENDENCY
  - CORRELATION != CAUSATION

does_not_establish:
  - literal biological consciousness
  - subjective experience
  - complete runtime implementation
  - autonomous external authority
  - universal empirical validity

falsifiers:
  - approved architecture supersedes the declared plane boundaries
  - implementation requirements demonstrate an incompatible ownership model
  - canonical governance adopts a conflicting authority topology

confidence_ceiling:
  architecture_model: high
  implementation_completeness: unknown_until_audited
  empirical_universality: not_claimed
```

---

# 123. Changelog

## v2.0.0 — 2026-08-25

Expanded the root AMOS OS note into the full operating architecture contract.

Added:

* document and architecture-contract versioning;
* complete root metadata;
* full authoritative-plane map;
* root responsibilities;
* Canon / Kernel / Control Plane separation;
* Runtime architecture;
* Cognitive Organism boundary;
* Agents / Skills / Workflows / Protocols;
* Memory / Knowledge / State separation;
* Models / Tools / Interfaces / Schemas;
* Observability / Security / Tests / Operations;
* Domains / Modes / Research / Operating Model / Archive / Cognitive Matrix;
* H/M/L decomposition;
* fractal retrieval;
* smallest-sufficient-proof fast path;
* escalation conditions;
* RSCF;
* selective invalidation;
* provenance topology;
* confidence ceiling;
* competing hypotheses;
* causal firewall;
* scope/regime firewall;
* freshness and revalidation;
* GMEF/governed evolution;
* transaction/MVCC/CAS conceptual boundaries;
* epoch/finality semantics;
* proposal/commit firewall;
* external-effect governance;
* reversibility;
* failure and recovery;
* `IN_DOUBT`;
* knowledge harvest;
* research/domain promotion;
* version and identity firewalls;
* root dependency graph;
* minimum and consequential reasoning paths;
* sensitivity and adversarial validation;
* capability limits;
* repository/placeholder boundaries;
* 30 core operating invariants;
* 30 failure classes;
* minimum contracts for components, agents, skills, workflows, protocols, models, tools, and state;
* proof capsule;
* stop conditions;
* gap priority;
* anti-fabrication;
* anti-regression;
* 7-Part persistence mapping;
* master RSCF node.

## v1.0.0

Initial root note defined:

```text
AMOS OS
authoritative planes
cross-cutting substrates
critical separation laws
```

---

# 124. Final Operating Law

AMOS OS can be compressed to:

```text
CANON
defines what must remain true

KERNEL
computes deterministic primitives

CONTROL PLANE
decides what may happen

RUNTIME
coordinates what is happening

COGNITIVE ORGANISM
integrates cognition

AGENTS
perform scoped roles

SKILLS
provide reusable capability

WORKFLOWS
orchestrate capability

PROTOCOLS
govern interaction

MEMORY
retains experience

KNOWLEDGE
retains governed claims

STATE
represents current condition

MODELS
represent possible or interpreted worlds

TOOLS
provide external capability

INTERFACES
expose boundaries

SCHEMAS
type structures

OBSERVABILITY
records behavior

SECURITY
protects boundaries

TESTS
verify behavior

OPERATIONS
maintains continuity

DOMAINS
specialize

RESEARCH
explores

OPERATING MODEL
governs stewardship

ARCHIVE
preserves lineage

COGNITIVE MATRIX
maps cross-cognitive relations
```

The governing invariant is:

> **AMOS OS may grow recursively, but no layer may gain capability by silently absorbing the authority, identity, provenance, or responsibilities of another layer.**

The second invariant is:

> **Every consequential result must remain traceable from current state and evidence through its dependencies, reasoning, validation, and authority boundary.**

The third invariant is:

> **Unknowns remain visible, competing hypotheses remain competing until discriminated, and local optimization may never weaken global integrity.**

---

**Related:** [[00_ROOT_MOC]]|MOC · [[NEURAL_NETWORK]]|Neural Network · [[ARCHITECTURE]]|Architecture · [[FULL_TREE]]|Full Tree · [[SYSTEM_MAP]]|System Map · [[DEPENDENCY_MAP]]|Dependency Map · [[AUTHORITATIVE_STATE]]|Authoritative State · [[00_ROOT_NAMING_STANDARD]]|Naming Standard · PLACEMENT_RULES|Placement Rules · [[ROADMAP]]|Roadmap · [[CANON_MAP]]|CANON · [[KERNEL_MAP]]|KERNEL · [[CONTROL_PLANE_MAP]]|CONTROL_PLANE · [[RUNTIME_MAP]]|RUNTIME · [[COGNITIVE_ORGANISM_MAP]]|COGNITIVE_ORGANISM · [[AGENT_MAP]]|[[AGENTS]] · [[SKILL_MAP]]|SKILLS · [[WORKFLOW_MAP]]|WORKFLOWS · [[PROTOCOL_MAP]]|PROTOCOLS · [[MEMORY_MEMORY_MAP]]|MEMORY · [[AMOS_FULL_BRAIN_OS_ARCHITECTURE]]|KNOWLEDGE · [[STATE_STATE_MAP]]|STATE · [[MODEL_MAP]]|MODELS · [[TOOL_MAP]]|TOOLS · [[INTERFACE_MAP]]|INTERFACES · [[SCHEMA_MAP]]|SCHEMAS · [[OBSERVABILITY_OBSERVABILITY_MAP]]|OBSERVABILITY · [[SECURITY_MAP]]|SECURITY · [[TEST_MAP]]|TESTS · [[OPERATIONS_MAP]]|OPERATIONS · [[DOMAIN_ALIAS_MAP]]|DOMAINS · [[INDEX_RESEARCH_README]]|RESEARCH · [[OPERATING_MODEL]]|[[OPERATING_MODEL]] · [[LEGACY_ARCHIVE_README]]|ARCHIVE · [[COGNITIVE_MATRIX_ARCHITECTURE]]|COGNITIVE_MATRIX

```
```

---

[[00_ROOT_MOC]]|[[AMOS MOC]]

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: placement_rules
node_type: note
path: 00_ROOT/PLACEMENT_RULES.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[00_COSMO_BRAIN_MOC]]
