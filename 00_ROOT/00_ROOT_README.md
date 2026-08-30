---
type: note
source: 00_ROOT
artifact_id: AMOS-OS-ROOT
name: AMOS_OS
title: AMOS OS — Governed Cognitive Operating Architecture (README)
document_version: 2.1.0
architecture_contract_version: 1.1.0
amos_core_target: v4.4
status: ACTIVE_ROOT
conclusion_class: AMOS_MODEL
rscf_state: derived
canon_group: tech-ai
canon_type: root-architecture
origin_architect: Trang Phan
steward: Trang Phan
created: 2026-08-25
updated: 2026-08-25
tags:
- amos
- amos-os
- root
- amos-os
- architecture
- cognitive-operating-system
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
- operating-model
- archive
- cognitive-matrix
- authority
- dependency-closure
- failure-recovery
- provenance-topology
- canon-group/tech-ai
- canon/architecture
- rscf/claim
- rscf/provenance
- rscf/state/derived
- topic/amos-os
- topic/system-architecture
- readme
- neural-network
- full-tree
- authoritative-state
- placement-rules
- roadmap
- amos-full-brain-os-architecture
- cognitive-matrix-architecture
aliases:
- AMOS OS - AMOS Operating System - AMOS Cognitive Operating System - AMOS System
  Root
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: root_index
---

# AMOS OS
**Origin architect / steward:** Trang Phan
> **Status:** `ACTIVE_ROOT`
> **AMOS_CORE target:** `v4.4`
> **Conclusion class:** `AMOS_MODEL`
AMOS OS is the governed infrastructure, cognition, knowledge, agent, skill, workflow, protocol, memory, state, control, runtime, tool, model, security, validation, and operations architecture of the AMOS ecosystem.
It is intentionally decomposed into authoritative planes so that semantic authority, computation, execution, knowledge, capability, and external effects remain distinguishable.
The governing priority is:
```text
INTEGRITY
>
COMPLETENESS
>
FLUENCY
>
SPEED
>
TOKEN SAVINGS
```
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: root_index
---


# 1. System Spine

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
PROTOCOLS / MODELS / DOMAIN ADAPTERS
↓
TOOLS / INTERFACES
↓
EXTERNAL EFFECTS
```

Cross-cutting substrates:

```text
MEMORY
KNOWLEDGE
STATE
PROVENANCE
SCHEMAS
OBSERVABILITY
SECURITY
TESTS
OPERATIONS
```

Evolution and specialization:

```text
DOMAINS
MODES
RESEARCH
OPERATING MODEL
ARCHIVE
COGNITIVE MATRIX
```

---

# 2. Core Separation Laws

```text
CANON != KERNEL
KERNEL != CONTROL_PLANE
CONTROL_PLANE != RUNTIME
RUNTIME != COGNITION

ORGAN != AGENT
AGENT != SKILL
SKILL != WORKFLOW
WORKFLOW != PROTOCOL

MEMORY != KNOWLEDGE
KNOWLEDGE != STATE
MEMORY != CANON

MODEL != OBSERVATION
MODEL != AUTHORITY

TOOL != PERMISSION
CAPABILITY != AUTHORITY

PROPOSAL != COMMIT
IMPLEMENTED != VALIDATED
PLACEHOLDER != IMPLEMENTED
UNKNOWN/GAP != PASS
```

These boundaries are structural invariants, not stylistic preferences.

---

# 3. Root Plane Map

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

# 4. Plane Responsibilities

| Plane                   | Primary responsibility                                            |
| ----------------------- | ----------------------------------------------------------------- |
| `00_ROOT`               | architecture, navigation, ownership maps, standards               |
| `01_CANON`              | source laws, official definitions, semantic invariants            |
| `02_KERNEL`             | deterministic operators and invariant machinery                   |
| `03_CONTROL_PLANE`      | authority, policy, admission, commit governance                   |
| `04_RUNTIME`            | live scheduling, routing, execution coordination                  |
| `05_COGNITIVE_ORGANISM` | integrated cognition subsystems                                   |
| `06_AGENTS`             | scoped role-based workers                                         |
| `07_SKILLS`             | reusable bounded capabilities                                     |
| `08_WORKFLOWS`          | multi-step orchestration                                          |
| `09_PROTOCOLS`          | interaction and handoff contracts                                 |
| `10_MEMORY`             | retained experience                                               |
| `11_KNOWLEDGE`          | evidence, claims, RSCFs, validated knowledge                      |
| `12_STATE`              | current authoritative/working/recovery state                      |
| `13_MODELS`             | formal representations, simulations, estimators                   |
| `14_TOOLS`              | connectors and bounded external capabilities                      |
| `15_INTERFACES`         | APIs, MCP, CLI, UI and external boundaries                        |
| `16_SCHEMAS`            | typed structural contracts                                        |
| `17_OBSERVABILITY`      | logs, traces, metrics and health                                  |
| `18_SECURITY`           | authentication, authorization mechanics, secrets, threat controls |
| `19_TESTS`              | verification, benchmarks and regression                           |
| `20_OPERATIONS`         | deployment, migration, incidents, rollback                        |
| `21_DOMAINS`            | domain specialization and adapters                                |
| `22_RESEARCH`           | experiments, papers, candidate models, unresolved claims          |
| `23_OPERATING_MODEL`    | human roles, decision rights and stewardship                      |
| `24_ARCHIVE`            | superseded, legacy and historical artifacts                       |
| `25_COGNITIVE_MATRIX`   | cross-cognitive topology and relations                            |

---

# 5. Canon

`CANON` defines what AMOS treats as governing semantic structure.

Canon may contain:

```text
laws
definitions
invariants
ontologies
identity contracts
governance principles
```

Hard boundary:

```text
CANON
!=
IMPLEMENTATION
```

A canonical specification can exist while executable support remains incomplete.

---

# 6. Kernel

`KERNEL` owns deterministic or tightly constrained machinery.

Examples:

```text
normalization
RSCF operations
dependency closure
state-transition primitives
validation operators
identity functions
provenance graph functions
```

Kernel should answer:

> **How is a primitive operation computed?**

not:

> **Is the operation authorized?**

---

# 7. Control Plane

`CONTROL_PLANE` owns:

```text
authority
policy
admission
routing governance
commit permission
resource governance
mode governance
risk escalation
provenance admission
lifecycle authority
```

Hard boundary:

```text
WORKER CAPABILITY
!=
CONTROL-PLANE AUTHORITY
```

---

# 8. Runtime

`RUNTIME` owns active coordination:

```text
session
task
step
tick
epoch
scheduler
router
runtime registry
execution state
commit state
failure state
recovery state
```

Hard boundary:

```text
ARCHITECTURE
!=
LIVE RUNTIME
```

---

# 9. Cognitive Organism

The Cognitive Organism coordinates cognitive subsystems such as:

```text
perception
attention
working cognition
hypothesis management
reasoning
metacognition
memory interaction
uncertainty handling
expression coordination
```

This is a structural cognition model.

It does not by itself establish:

```text
biological consciousness
subjective experience
embodiment
autonomous external agency
```

---

# 10. Agents

Agents are scoped workers.

Minimum contract:

```yaml
Agent:
  agent_id:
  version:
  role:
  scope:
  inputs:
  outputs:
  capabilities:
  dependencies:
  authority:
  memory_policy:
  provenance_policy:
  tests:
  failure_modes:
  recovery:
```

Hard boundary:

```text
AGENT NAME
!=
CAPABILITY

CAPABILITY
!=
AUTHORITY
```

---

# 11. Skills

Skills encode reusable procedures.

Minimum contract:

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

A skill provides capability.

It does not grant authority.

---

# 12. Workflows

Workflows coordinate multiple operations.

```text
TRIGGER
↓
PRECONDITIONS
↓
RETRIEVAL
↓
TRANSFORMATION
↓
VALIDATION
↓
COMMIT / OUTPUT
↓
VERIFY
↓
STORE LEARNING
```

Workflow:

```text
!=
Skill
!=
Protocol
```

---

# 13. Protocols

Protocols define component interaction semantics.

Examples:

```text
agent ↔ agent
agent ↔ skill
agent ↔ tool
runtime ↔ state
control plane ↔ runtime
authority ↔ executor
knowledge ↔ provenance
```

A protocol should define:

```text
participants
messages
preconditions
state transitions
timeouts
retries
failures
commit semantics
rollback semantics
```

---

# 14. Memory / Knowledge / State

These are independent planes.

```text
MEMORY
=
what was retained

KNOWLEDGE
=
what was admitted as reusable evidence/claims

STATE
=
what is currently active or authoritative
```

Therefore:

```text
MEMORY
!=
KNOWLEDGE
!=
STATE
```

---

# 15. Epistemic Classes

AMOS distinguishes:

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

Critical invariant:

```text
UNKNOWN/GAP
!=
PASS
```

---

# 16. Proof Capsule

A consequential conclusion should conceptually retain:

```yaml
ProofCapsule:
  claim:
  conclusion_class:

  premises: []
  evidence: []
  provenance: []

  scope:
  regime:
  temporal_validity:

  dependencies: []

  competing_hypotheses: []

  falsifiers: []

  confidence_ceiling:
```

---

# 17. Confidence Ceiling

Derived confidence may not exceed the weakest load-bearing premise unless that premise is independently revalidated.

Conceptually:

```text
Confidence(Result)
<=
WeakestLoadBearingPremise
```

This prevents fluent synthesis from laundering weak evidence into strong claims.

---

# 18. Provenance Topology

AMOS tracks provenance as a graph rather than a flat citation count.

Important evidence should retain:

```text
source identity
source ancestry
dependency edges
freshness
scope
regime
correlation risk
```

Hard rule:

```text
10 DESCENDANTS OF ONE SOURCE
!=
10 INDEPENDENT SOURCES
```

---

# 19. RSCF

RSCF is a first-class recursive claim/state structure.

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

If a load-bearing premise fails:

```text
INVALIDATE THAT PREMISE
+
ITS DEPENDENT DESCENDANTS
```

not unrelated reasoning branches.

---

# 20. Competing Hypotheses

AMOS does not force convergence when evidence does not discriminate.

```text
H1
H2
H3
```

may remain:

```text
COMPETING
```

The preferred next action is the cheapest high-information discriminating test.

---

# 21. Causal Firewall

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

Critical law:

```text
STRUCTURAL SIMILARITY
!=
CAUSATION
```

Cross-domain mappings remain `MODEL` unless independently validated.

---

# 22. Scope / Regime Firewall

Consequential claims should retain an applicability envelope.

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

A regime shift may invalidate a previously valid conclusion.

---

# 23. Freshness

Evidence and state may be:

```text
CURRENT
FRESH
AGING
STALE
EXPIRED
UNKNOWN
```

Hard boundary:

```text
STALE
!=
CURRENT
```

Load-bearing stale premises require revalidation before consequential reuse.

---

# 24. H/M/L Architecture

AMOS recursively decomposes systems into:

```text
H
=
high-level law
mission
macro field
domain

M
=
mediating subsystem
architecture
institution
coordination layer

L
=
local component
action
event
claim
evidence item
```

For AMOS OS:

```text
H
=
CANON / ARCHITECTURE / DOMAIN

M
=
KERNEL / CONTROL PLANE / RUNTIME / ORGAN / AGENT FAMILY

L
=
COMPONENT / TOOL CALL / STATE UPDATE / CLAIM / EVENT
```

---

# 25. H/M/L Integrity

A local optimization is acceptable only if higher-scale viability remains intact.

```text
Accept(LocalChange)
iff

Viable(L)
∧
Viable(M)
∧
Viable(H)
```

Therefore local speed gains are rejected if they cause:

```text
authority bypass
provenance loss
semantic drift
security regression
state corruption
irrecoverable mutation
```

---

# 26. Fractal Retrieval

Preferred retrieval:

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

Raw evidence is not loaded by default.

Descend only when additional detail can materially alter the result.

---

# 27. v4.4 Fast Path

The v4.4 fast path uses the smallest sufficient proof scope.

Local reasoning is allowed only when:

```text
dependency closure
provenance independence
scope compatibility
regime compatibility
freshness
non-conflict
```

are established.

Escalate when there is:

```text
shared evidence ancestry
conflicting evidence
stale evidence
cross-regime reasoning
governance impact
irreversible action
ambiguous dependency
```

Fast path means:

```text
LESS UNNECESSARY COORDINATION
```

not:

```text
LESS INTEGRITY
```

---

# 28. GMEF / Governed Evolution

Evolution should preserve:

```text
proposal
mutation
evaluation
validation
admission
rejection
lineage
rollback
```

Canonical pattern:

```text
CURRENT
↓
PROPOSAL
↓
TEST
↓
VALIDATE
↓
ADMIT / REJECT
↓
NEW VERSION / ROLLBACK
```

Hard boundary:

```text
EVOLUTION
!=
UNCONTROLLED SELF-MODIFICATION
```

---

# 29. Transaction and Commit Boundary

For consequential state changes:

```text
PROPOSAL
↓
VALIDATION
↓
AUTHORITY
↓
PREPARE
↓
REVALIDATION
↓
COMMIT
↓
VERIFY
↓
RECEIPT
```

Critical law:

```text
PROPOSAL
!=
COMMIT
```

---

# 30. MVCC / CAS Concepts

Where concurrent state exists, AMOS may reason in terms of:

```text
state versions
epochs
MVCC
CAS
fencing
parent state
commit preconditions
```

Core invariant:

```text
OBSERVED STATE VERSION
must still satisfy
COMMIT PRECONDITION
```

at commit time.

These are architectural concepts unless executable support is independently verified.

---

# 31. External Effects

External effects include:

```text
file mutation
database write
message send
financial action
API write
deployment
security configuration
physical-system action
```

Effectful actions require stronger governance than analysis.

---

# 32. Reversibility

Effects should be typed:

```text
REVERSIBLE
PARTIALLY_REVERSIBLE
COMPENSATABLE
IRREVERSIBLE
UNKNOWN
```

Hard rule:

```text
HIGH IMPACT
+
UNKNOWN REVERSIBILITY
→
ESCALATE
```

---

# 33. Failure and Recovery

Failure flow:

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

Preferred recovery is:

```text
LOCAL
REVERSIBLE
DEPENDENCY-AWARE
PROVENANCE-PRESERVING
```

---

# 34. Failure States

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

Important:

```text
UNKNOWN OUTCOME
!=
SUCCESS

UNKNOWN OUTCOME
!=
FAILURE
```

When final state cannot be established, use:

```text
IN_DOUBT
```

---

# 35. Models

Models represent possible, estimated, simulated, or interpreted worlds.

A model should declare:

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
```

Critical law:

```text
MODEL
!=
OBSERVATION
```

---

# 36. Tools

Tools provide capability.

```text
TOOL
→ CAPABILITY

CONTROL PLANE
→ ADMISSIBILITY

SECURITY
→ ACCESS VALIDITY

RUNTIME
→ INVOCATION
```

Critical law:

```text
TOOL ACCESS
!=
PERMISSION
```

---

# 37. Security

Security should preserve:

```text
least privilege
bounded scope
revocability
traceability
secret minimization
failure isolation
```

Possession of credentials does not itself establish authorization to use them for a given action.

---

# 38. Observability

Observability records:

```text
logs
traces
metrics
events
health
diagnostics
audit records
```

Hard boundary:

```text
OBSERVED
!=
CORRECT
```

Observability provides evidence for validation; it does not replace validation.

---

# 39. Tests

Verification progresses through:

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
RUNTIME
```

Critical law:

```text
TEST PASS
!=
UNIVERSAL VALIDITY
```

All test claims inherit their tested scope.

---

# 40. Domains

Domains specialize AMOS without redefining core semantics.

Possible domains include:

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

Only domains that can materially alter the result should be activated.

---

# 41. Modes

Modes alter operating behavior.

Possible families:

```text
reasoning
attention
epistemic
decision
scale
world-model
recovery
execution
freshness
lifecycle
```

Hard rule:

```text
MODE
!=
AGENT
```

unless explicitly defined as an independent agent.

---

# 42. Research

Research stores:

```text
candidate laws
hypotheses
experiments
papers
prototype models
unresolved frameworks
external evidence
```

Hard boundary:

```text
RESEARCH
!=
CANON
```

Promotion requires evidence and governance.

---

# 43. Knowledge Promotion

Canonical path:

```text
EPHEMERAL OUTPUT
↓
SOURCE / EVIDENCE
↓
PROVENANCE
↓
CONTRADICTION CHECK
↓
SCOPE / REGIME CHECK
↓
VALIDATION
↓
VALIDATED KNOWLEDGE
```

Documentation or README claims remain `SOURCE_CLAIM` until validated.

---

# 44. Research-to-Canon Promotion

```text
RESEARCH
↓
SOURCE BINDING
↓
FORMALIZATION
↓
FALSIFIERS
↓
VALIDATION
↓
KNOWLEDGE
↓
GOVERNANCE REVIEW
↓
CANON
```

No direct promotion from hypothesis to canon.

---

# 45. Placement Law

Artifact ownership follows primary responsibility.

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

# 46. Identity Firewall

These are distinct:

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

Renaming or moving an artifact must not silently rewrite semantic identity or provenance.

---

# 47. Versioning

Version dimensions may include:

```text
amos_core_target
architecture_version
document_version
component_version
schema_version
model_version
protocol_version
skill_version
workflow_version
dataset_version
```

They are independent axes.

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
ARCHITECTURE_FINAL_v2.md
```

---

# 48. Placeholder Rule

A placeholder means:

```text
EXPECTED ARCHITECTURAL POSITION EXISTS
```

It does not mean:

```text
IMPLEMENTATION EXISTS
```

Therefore:

```text
PLACEHOLDER
!=
IMPLEMENTED

UNKNOWN/GAP
!=
PASS
```

---

# 49. Authoritative State Firewall

Architecture defines:

> **What should exist and how responsibilities are separated.**

`AUTHORITATIVE_STATE.md` defines:

> **What currently exists, is implemented, tested, validated, active, deprecated, or missing.**

Never infer implementation from architecture alone.

---

# 50. Capability Limits

AMOS OS architecture does not establish:

```text
literal consciousness
subjective experience
biological embodiment
perfect knowledge
perfect prediction
unbounded autonomous agency
automatic external authority
complete implementation
universal empirical validity
```

Cognitive, biological, emotional, somatic, quantum-fractal, or consciousness-related structures remain `MODEL` where not independently validated.

---

# 51. Adaptive Complexity

AMOS reasoning may operate at different complexity levels:

```text
C0 — Direct
C1 — Compact
C2 — Structured
C3 — Deep
C4 — Maximum
```

Escalate for:

```text
high stakes
irreversibility
novelty
weak evidence
stale evidence
contradiction
causal ambiguity
scope mismatch
competing models
governance impact
```

De-escalate when outcome-changing uncertainty is resolved.

---

# 52. Stop Condition

Reasoning should stop when:

```text
CLAIM SUFFICIENCY
∧
DECISION SUFFICIENCY
∧
ACTION SUFFICIENCY
```

are reached.

Do not expand merely because additional AMOS modules exist.

---

# 53. Gap Priority

Gaps are classified:

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

# 54. Anti-Fabrication Laws

```text
ABSENCE OF CONTRADICTION
!=
PROOF

STRUCTURAL SIMILARITY
!=
CAUSATION

FORMAL EQUATION
!=
EMPIRICAL LAW

BENCHMARK SUCCESS
!=
UNIVERSAL VALIDITY

REPORTED LATENCY
!=
HARDWARE-INDEPENDENT GUARANTEE

DISTRIBUTED TEST
!=
FORMAL PROOF
```

unless separately established.

---

# 55. Anti-Regression

No optimization may weaken:

```text
factual support
scope correctness
contradiction visibility
provenance recoverability
causal discipline
authority boundaries
security
repairability
```

If it does:

```text
ROLL BACK
```

---

# 56. Root Invariants

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
OS16 IMPLEMENTED != VALIDATED
OS17 RESEARCH != CANON
OS18 PLACEHOLDER != IMPLEMENTATION
OS19 UNKNOWN/GAP != PASS
OS20 PATH != IDENTITY
OS21 LINK != DEPENDENCY
OS22 CORRELATION != CAUSATION
OS23 COPIES != INDEPENDENT EVIDENCE
OS24 STALE != CURRENT
OS25 LOCAL OPTIMIZATION CANNOT BREAK HIGHER-SCALE INTEGRITY
OS26 FAILED PREMISE INVALIDATES DEPENDENTS ONLY
OS27 IRREVERSIBLE ACTION REQUIRES STRONGER GOVERNANCE
OS28 FAST PATH REQUIRES PROOF OF LOCAL SUFFICIENCY
OS29 PROVENANCE MUST SURVIVE TRANSFORMATION
OS30 ARCHIVE MUST PRESERVE LINEAGE
```

---

# 57. Failure Registry

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
OS-F010 PLACEHOLDER_PROMOTED_AS_IMPLEMENTED
OS-F011 UNKNOWN_PROMOTED_TO_PASS
OS-F012 STALE_STATE_REUSE
OS-F013 PROVENANCE_LOSS
OS-F014 CORRELATED_SOURCE_OVERCOUNT
OS-F015 CAUSAL_OVERREACH
OS-F016 SCOPE_LEAKAGE
OS-F017 REGIME_MISMATCH
OS-F018 BROKEN_DEPENDENCY_CLOSURE
OS-F019 PARTIAL_COMMIT
OS-F020 HIDDEN_IN_DOUBT_STATE
OS-F021 ROLLBACK_FAILURE
OS-F022 STALE_AUTHORITY
OS-F023 ACTIVE_ARCHIVE_DEPENDENCY
OS-F024 DOMAIN_CORE_LEAK
OS-F025 VERSION_IDENTITY_COLLAPSE
OS-F026 PATH_IDENTITY_COLLAPSE
OS-F027 BROKEN_SUPERSESSION_LINEAGE
OS-F028 TEST_SCOPE_OVERCLAIM
OS-F029 FAST_PATH_WITHOUT_PROOF
OS-F030 GLOBAL_RECOMPUTATION_WHEN_LOCAL_REPAIR_SUFFICIENT
```

---

# 58. 7-Part Persistence Mapping

| Part              | AMOS OS mapping                                      |
| ----------------- | ---------------------------------------------------- |
| I — Constraint    | canon, schemas, policy, security, authority          |
| II — Flow         | data, evidence, state transitions, messages, effects |
| III — Structure   | planes, components, agents, interfaces               |
| IV — Enforcement  | control plane, validation, security                  |
| V — Time          | versions, epochs, freshness, lifecycle               |
| VI — Adaptation   | learning, models, recovery, governed evolution       |
| VII — Termination | rollback, failure, deprecation, archive              |

**Conclusion class:** `AMOS_MODEL`

---

# 59. Master RSCF Node

```yaml
node_id: AMOS_OS_ROOT
node_type: operating_architecture
domain: AMOS_OS

functional_type:
  - ROOT_SYSTEM
  - COGNITIVE_INFRASTRUCTURE
  - GOVERNANCE_ARCHITECTURE

lifecycle_stage: ACTIVE_ROOT

origin_architect: Trang Phan
steward: Trang Phan

claim_class: AMOS_MODEL

claim: >
  AMOS OS is a governed multi-plane operating architecture separating
  canonical semantics, deterministic mechanisms, control-plane authority,
  runtime execution, cognitive coordination, role-based agents, reusable
  procedures, persistent memory, validated knowledge, current state,
  formal models, external tools, interfaces, validation, security,
  operations, domain specialization, research, and historical lineage.

premises:
  - capability and authority are distinct
  - model and observation are distinct
  - memory, knowledge, and state are distinct
  - provenance and dependency closure are load-bearing
  - failure should be locally recoverable where possible
  - local optimization may not weaken higher-scale integrity

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
  - full implementation of every declared plane
  - autonomous external authority
  - universal empirical validity

confidence_ceiling:
  architecture_model: high
  implementation_completeness: UNKNOWN/GAP
  empirical_universality: not_claimed
```

---

# 60. Changelog

## v2.1.0 — 2026-08-25

- hardened root plane boundaries;
- added explicit protocol layer to system spine;
- expanded Memory / Knowledge / State separation;
- added Proof Capsule contract;
- added confidence ceiling;
- added provenance topology;
- added competing-hypothesis handling;
- added causal and scope/regime firewalls;
- added freshness and revalidation;
- added H/M/L integrity model;
- added fractal retrieval path;
- added v4.4 smallest-sufficient-proof fast path;
- added governed GMEF evolution;
- added transaction, MVCC/CAS, and epoch concepts as architecture models rather than implementation claims;
- added external-effect reversibility;
- added explicit `IN_DOUBT` handling;
- added knowledge/research promotion paths;
- added adaptive-complexity levels;
- added stop conditions;
- added gap prioritization;
- added anti-fabrication and anti-regression rules;
- expanded root invariants and failure registry;
- added 7-Part persistence mapping;
- strengthened master RSCF node;
- retained explicit capability limits.

## v2.0.0 — 2026-08-25

Expanded the initial root note into a governed AMOS OS architecture document.

## v1.0.0

Initial root definition:

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

---

# 61. Final Operating Law

AMOS OS can be compressed to:

```text
CANON
defines what must remain true

KERNEL
computes constrained primitives

CONTROL PLANE
decides what may happen

RUNTIME
coordinates what is happening

COGNITIVE ORGANISM
integrates cognitive state

AGENTS
perform scoped roles

SKILLS
provide reusable capability

WORKFLOWS
sequence capability

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
provide bounded capability

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
preserves continuity

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

The primary law is:

> **No AMOS layer may gain convenience by silently absorbing the identity, authority, provenance, state ownership, or responsibilities of another layer.**

The second law is:

> **Every consequential conclusion or effect must remain traceable through its load-bearing evidence, dependencies, scope, regime, validation, authority boundary, and resulting state transition.**

The third law is:

> **AMOS expands recursively only when expansion preserves integrity, contradiction visibility, provenance recoverability, causal discipline, scope correctness, and repairability.**

---

**Related:** [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]|MOC · [[00_ROOT/NEURAL_NETWORK|NEURAL_NETWORK]]|Neural Network · [[00_ROOT/ARCHITECTURE|ARCHITECTURE]]|Architecture · [[00_ROOT/FULL_TREE|FULL_TREE]]|Full Tree · [[00_ROOT/SYSTEM_MAP|SYSTEM_MAP]]|System Map · [[00_ROOT/DEPENDENCY_MAP|DEPENDENCY_MAP]]|Dependency Map · [[00_ROOT/AUTHORITATIVE_STATE|AUTHORITATIVE_STATE]]|Authoritative State · [[00_ROOT/00_ROOT_NAMING_STANDARD|00_ROOT_NAMING_STANDARD]]|Naming Standard · [[00_ROOT/PLACEMENT_RULES|PLACEMENT_RULES]]|Placement Rules · [[00_ROOT/ROADMAP|ROADMAP]]|Roadmap · [[01_CANON/00_INDEX/CANON_MAP|CANON_MAP]]|CANON · [[02_KERNEL/00_INDEX/KERNEL_MAP|KERNEL_MAP]]|KERNEL · [[03_CONTROL_PLANE/00_INDEX/CONTROL_PLANE_MAP|CONTROL_PLANE_MAP]]|CONTROL_PLANE · [[04_RUNTIME/00_INDEX/RUNTIME_MAP|RUNTIME_MAP]]|RUNTIME · [[05_COGNITIVE_ORGANISM/00_INDEX/COGNITIVE_ORGANISM_MAP|COGNITIVE_ORGANISM_MAP]]|COGNITIVE_ORGANISM · [[06_AGENTS/00_INDEX/AGENT_MAP|AGENT_MAP]]|[[AGENTS|AGENTS]] · [[07_SKILLS/00_INDEX/SKILL_MAP|SKILL_MAP]]|SKILLS · [[08_WORKFLOWS/00_INDEX/WORKFLOW_MAP|WORKFLOW_MAP]]|WORKFLOWS · [[09_PROTOCOLS/00_INDEX/PROTOCOL_MAP|PROTOCOL_MAP]]|PROTOCOLS · [[10_MEMORY/00_INDEX/MEMORY_MEMORY_MAP|MEMORY_MEMORY_MAP]]|MEMORY · [[11_KNOWLEDGE/AMOS_FULL_BRAIN_OS_ARCHITECTURE|AMOS_FULL_BRAIN_OS_ARCHITECTURE]]|KNOWLEDGE · [[12_STATE/00_INDEX/STATE_STATE_MAP|STATE_STATE_MAP]]|STATE · [[13_MODELS/00_INDEX/MODEL_MAP|MODEL_MAP]]|MODELS · [[14_TOOLS/00_INDEX/TOOL_MAP|TOOL_MAP]]|TOOLS · [[15_INTERFACES/00_INDEX/INTERFACE_MAP|INTERFACE_MAP]]|INTERFACES · [[16_SCHEMAS/00_INDEX/SCHEMA_MAP|SCHEMA_MAP]]|SCHEMAS · [[17_OBSERVABILITY/00_INDEX/OBSERVABILITY_OBSERVABILITY_MAP|OBSERVABILITY_OBSERVABILITY_MAP]]|OBSERVABILITY · [[18_SECURITY/00_INDEX/SECURITY_MAP|SECURITY_MAP]]|SECURITY · [[19_TESTS/00_INDEX/TEST_MAP|TEST_MAP]]|TESTS · [[20_OPERATIONS/00_INDEX/OPERATIONS_MAP|OPERATIONS_MAP]]|OPERATIONS · [[21_DOMAINS/00_INDEX/DOMAIN_ALIAS_MAP|DOMAIN_ALIAS_MAP]]|DOMAINS · [[22_RESEARCH/00_INDEX/INDEX_RESEARCH_README|INDEX_RESEARCH_README]]|RESEARCH · [[23_OPERATING_MODEL/00_INDEX/OPERATING_MODEL|OPERATING_MODEL]]|[[23_OPERATING_MODEL/00_INDEX/OPERATING_MODEL|OPERATING_MODEL]] · [[24_ARCHIVE/00_LEGACY/LEGACY_ARCHIVE_README|LEGACY_ARCHIVE_README]]|ARCHIVE · [[25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_ARCHITECTURE|COGNITIVE_MATRIX_ARCHITECTURE]]|COGNITIVE_MATRIX

```
```

---

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]|[[00_ROOT/AMOS MOC|AMOS MOC]]

---
**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: 00_root_readme
node_type: note
path: 00_ROOT/00_ROOT_README.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
  - INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[00_ROOT/00_COSMO_BRAIN_MOC|00_COSMO_BRAIN_MOC]]
