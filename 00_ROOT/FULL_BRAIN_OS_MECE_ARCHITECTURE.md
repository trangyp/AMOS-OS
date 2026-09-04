---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Full Brain Os Mece Architecture
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# AMOS Full Brain OS — MECE Architecture

## 0. Architectural decision

The `_AMOS_OS` numbered folders are **physical/operational namespaces**, not twenty-five peer
cognitive systems and not a universal call chain.

The source architecture explicitly rejects a universal:

```text
Kernel -> Engine -> Agent -> Control Plane
```

hierarchy. AMOS must instead be read through separate dimensions:

```text
FUNCTIONAL OWNERSHIP
!= PHYSICAL STORAGE
!= AUTHORITY PRECEDENCE
!= RUNTIME CALL ORDER
!= EVIDENCE / VALIDATION STATUS
```

This map is the derived functional normalization. It does not promote AMOS models to empirical facts
or documentary architecture to deployed implementation.

## 1. Source-grounded Full Brain envelope

The Full Brain source separates three large systems:

```text
AMOS BRAIN
= representation + cognition + coordination + capability + world/system modeling

AMOS RUNTIME
= typed reasoning/execution state + RSCF + H/M/L + provenance + repair + replay + audit

AMOS CONTROL / BODY
= authority + capability grants + semantic transactions + commit/finality eligibility
  + rollback/recovery + world-effect gating
```

The Round-11 infrastructure source adds the larger envelope:

```text
AMOS INFRASTRUCTURE
├── governance / policy / authority
├── trust roots / identity / capability grants
├── lineage / canon / configuration admission
├── provenance / evidence / memory admission
├── runtime / transaction / freshness / finality
├── agent lifecycle / task orchestration
├── Full Brain OS
├── specialist agents
├── skills / kernels / engines
├── host runtime / tools / APIs
└── effect adapters
```

Therefore:

```text
FULL_BRAIN_OS != WHOLE_AMOS_INFRASTRUCTURE
BRAIN != RUNTIME
RUNTIME != CONTROL/BODY
AUTHORITY PRECEDENCE != STRUCTURAL CONTAINMENT
```

## 2. Strict MECE responsibility partition of physical planes

For physical-vault architecture, every numbered plane is assigned to exactly **one** responsibility
domain. Dependencies are expressed as edges rather than duplicate ownership.

### A — NORMATIVE & GOVERNANCE DEFINITION

Owns what is allowed to mean, what rules exist, and who is organizationally accountable.

```text
01_CANON
23_OPERATING_MODEL
```

Primary responsibilities:
- admitted laws/definitions/lineage/supersession;
- roles, decision rights, forums, escalation and service expectations.

Does not own runtime execution, empirical proof, cognitive inference, or external effects.

### B — EXECUTION CORE & EFFECT GOVERNANCE

Owns deterministic primitives, active bounded execution, and durable-effect admission.

```text
02_KERNEL
03_CONTROL_PLANE
04_RUNTIME
```

Primary responsibilities:
- deterministic reasoning/state-integrity primitives;
- authorization, semantic transaction, commit-time revalidation and finality eligibility;
- bounded execution lifecycle, replay, recovery and runtime state transitions.

### C — COGNITIVE CAPABILITY & ORCHESTRATION

Owns cognition, delegated actors, reusable capability procedures, orchestration and specialist-domain
routing.

```text
05_COGNITIVE_ORGANISM
06_AGENTS
07_SKILLS
26_WORKFLOWS
21_DOMAINS
25_COGNITIVE_MATRIX
```

Primary responsibilities:
- cognitive loop and organ coordination;
- bounded worker/orchestrator/auditor identities;
- versioned capability modules;
- explicit process/state-transition orchestration;
- specialist domain ownership/routing;
- fractal cognitive coordinate/routing decomposition.

None of these planes acquires durable-effect authority merely by being capable.

### D — INFORMATION, MEMORY, STATE & MODEL SUBSTRATE

Owns persisted information semantics and typed representation.

```text
10_MEMORY
11_KNOWLEDGE
12_STATE
13_MODELS
16_SCHEMAS
08_PLANETARY (Omniverse Layer 6 — Biophysical & Planetary Substrate)
```

Primary responsibilities:
- temporal memory and retrieval;
- source/evidence/knowledge relationships;
- current/historical state identity and epochs;
- explicit models/simulations/registries;
- typed contracts/records/tensors.

Hard boundary:

```text
MEMORY != KNOWLEDGE
KNOWLEDGE != STATE
MODEL != OBSERVATION
SCHEMA != TRUTH
```

### E — INTERACTION, SECURITY & EFFECT ADAPTERS

Owns cross-component handoff semantics, protected boundaries, interfaces and host capabilities.

```text
09_PROTOCOLS
14_TOOLS
15_INTERFACES
18_SECURITY
```

Primary responsibilities:
- interaction and handoff contracts;
- host/tool capability descriptions and effect adapters;
- typed system boundaries;
- security constraints, identity/access protection and trust-boundary enforcement.

Availability never creates authorization.

### F — ASSURANCE, LEARNING & LIFECYCLE EVIDENCE

Owns evidence about operation, validation, research, operational recovery and historical lineage.

```text
17_OBSERVABILITY
19_TESTS
20_OPERATIONS
22_RESEARCH
24_ARCHIVE
```

Primary responsibilities:
- traces, telemetry, receipts and failure visibility;
- executable checks and validation evidence;
- runbooks, incidents, maintenance and audit lineage;
- research acquisition/experimentation;
- retained historical/superseded lineage.

Hard boundary:

```text
OBSERVED != AUTHORIZED
TEST_PASS != UNIVERSAL_VALIDITY
RESEARCH != CANON
ARCHIVE != ACTIVE
```

### Partition invariant

```text
{01..25} =
A ∪ B ∪ C ∪ D ∪ E ∪ F

A ∩ B ∩ C ∩ D ∩ E ∩ F = ∅
```

`00_ROOT` is the navigation/authority-pointer meta-plane and is outside the numbered partition.

## 3. Full Brain functional fields with one primary owner

The source architecture uses interacting fields. To keep the operational mapping MECE, each field has
one primary physical owner and typed dependencies.

| Full Brain field | Primary physical owner | Key dependencies |
|---|---|---|
| Representation / Expression | 05 Cognitive Organism | 15 Interfaces, 11 Knowledge, 13 Models |
| Cognitive Coordination | 05 Cognitive Organism | 25 Cognitive Matrix, 02 Kernel |
| Capability / Specialist Reasoning | 21 Domains | 07 Skills, 13 Models, 11 Knowledge |
| World / System Representation | 13 Models | 11 Knowledge, 21 Domains |
| Runtime Continuity | 04 Runtime | 09 Protocols, 10 Memory, 12 State, 16 Schemas |
| Effect Governance | 03 Control Plane | 02 Kernel, 18 Security, 23 Operating Model |
| Deployment / Effect Adaptation | 14 Tools | 06 Agents, 08 Workflows, 15 Interfaces |

This repairs the earlier ambiguity where a “primary owner” column contained several peer owners.

`ONE PRIMARY OWNER + MANY TYPED DEPENDENCIES` is the default.

## 4. Full Brain component model

The source explicitly gives:

```text
FullBrainOS = {
  B_core,
  K_omni,
  B_omniverse,
  P_personality,
  T_expression,
  G_gap
}
```

The source also uses a heading referring to “five primary components,” creating a count conflict.

Current classification:

```text
DECLARED COUNT = 5
EXPLICIT SET COUNT = 6
STATUS = COMPETING / SOURCE-INCONSISTENCY
```

Do not silently remove a component merely to reconcile the count.

Operational mapping:

```text
B_core       -> capability ecosystem; routed through Domains / Skills / Models
K_omni       -> cognitive coordination / minimum-sufficient activation; 05 + Kernel primitives
B_omniverse  -> world/system representation; Models + Knowledge
P_personality-> expression/interaction shaping; cognitive representation boundary
T_expression -> expression translation / interface representation
G_gap        -> integrity/gap constraints; cross-cutting fail-closed condition
```

These mappings are derived ownership normalizations, not claims that the source artifacts are
physically located in those planes.

## 5. Cognitive-organism functional partition

The persistent cognitive loop is normalized into seven responsibility groups:

```text
INPUT / REPRESENTATION
  perception · attention · context · world-model access

INTERPRETATION / REASONING
  cognition · structural reasoning · competing hypotheses · causal analysis · simulation

AFFECT / DRIVE
  emotion-model · instinct · motivation · goal

PROSPECTIVE / ACTION FORMATION
  planning · decision-support · agency proposal · action interface

ADAPTATION / CONTINUITY
  memory access · learning · reflection · identity continuity · lifecycle

SOCIAL / EXPRESSION
  social modeling · communication · expression

REGULATION / ASSURANCE
  homeostasis · risk · safety · repair · observability
```

The groups are functionally distinct; dependencies between them are explicit.

## 6. Governed end-to-end loop

```text
HUMAN / ENVIRONMENT
→ OBSERVE / REPRESENT
→ ATTEND / CONTEXTUALIZE
→ RETRIEVE MEMORY + KNOWLEDGE
→ REASON
→ PRESERVE COMPETING HYPOTHESES
→ SIMULATE / PLAN
→ PROPOSE
→ RUNTIME BINDS STATE + DEPENDENCIES
→ CONTROL-PLANE AUTHORITY / FRESHNESS / CONFLICT CHECK
→ COMMIT-TIME REVALIDATION
→ TOOL / INTERFACE EFFECT
→ OBSERVABILITY / TEST RECEIPT
→ LEARNING / KNOWLEDGE CANDIDATE
→ REVALIDATION / FUTURE COGNITION
```

No arrow silently upgrades epistemic class or authority.

## 7. Agent and skill boundary from Round 11

The infrastructure source rejects one giant autonomous agent. Roles are differentiated:

```text
FULL BRAIN SUPERVISOR -> cognitive orchestration, decomposition, synthesis, escalation
PLANNER               -> plans, task DAGs, assumptions, rollback points
RESEARCH/EVIDENCE      -> typed evidence and provenance
ENGINEERING            -> code/patch/config artifacts within capability scope
VERIFICATION           -> tests/adversarial/replay/regression evidence
MEMORY/KNOWLEDGE       -> proposes knowledge changes; cannot self-promote
POLICY/GOVERNANCE      -> policy interpretation/construction support
EFFECT ADAPTER         -> performs admitted external effects without widening scope
```

Default Full Brain authority is cognitive/proposal, not root/governor/effect authority.

Skills are versioned capability modules. They cannot create infrastructure authority.

## 8. Task, lease and finality semantics

For consequential work, the source introduces explicit task state:

```text
SUBMITTED
→ WORKING
  ├→ INPUT_REQUIRED
  ├→ AUTH_REQUIRED
  └→ WAITING_DEPENDENCY
→ COMPLETED / CANCELED / REJECTED / FAILED
```

Stateful work may bind leases/fencing epochs. Stale workers may not commit after reassignment.

Retry semantics distinguish:
- pure/read-only;
- idempotent effects;
- non-idempotent effects;
- `IN_DOUBT` outcomes.

These are AMOS infrastructure patterns. They do not prove a deployed distributed implementation.

## 9. Memory and knowledge separation

The infrastructure source distinguishes:

```text
WORKING MEMORY
AGENT SCRATCH STATE
SHARED OPERATIONAL STATE
EVIDENCE / PROVENANCE GRAPH
CANONICAL KNOWLEDGE
```

These are not interchangeable stores.

Canonical knowledge admission requires source identity, provenance, revision, freshness, scope/regime,
evidence class, contradiction checks and applicable version/CAS preconditions.

## 10. RSCF / H-M-L reasoning architecture

Decision-relevant reasoning should carry:

```text
claim / class
premises
evidence
provenance + ancestry
scope
regime
freshness
dependencies
competing explanations
falsifiers
invalidation conditions
confidence ceiling
```

H/M/L recursively narrows retrieval:

```text
H system/domain
→ M subsystem
→ L detail
→ raw evidence only if result-changing
```

The smallest sufficient proof scope is preferred; critical uncertainty escalates.

## 11. Authority and commit firewall

```text
CAPABILITY != AUTHORITY
IDENTITY != CAPABILITY
TRUST SCORE != ROOT KEY
PLANNING-TIME ALLOW != COMMIT-TIME ALLOW
MESSAGE != ARTIFACT
PROPOSAL != COMMIT
APPROVAL != FINALITY
```

Before a durable effect, revalidate as applicable:

```text
grant
identity
policy
state
resource
effect
risk
freshness
parent capability chain
conflicts / fencing epoch
```

## 12. Knowledge-harvest path

```text
raw source
→ evidence atom
→ typed relationship
→ contradiction / gap map
→ governed synthesis
→ decision / product
```

Knowledge-state operations may include reinforce, contradict, split, merge, mutate, retire and promote.
None creates truth automatically.

## 13. Failure and repair architecture

Failure recovery is selective:

```text
failed premise / edge
→ invalidate dependent descendants
→ preserve unaffected state
→ roll back to nearest valid state
→ reroute locally
→ global recomputation only when required
```

Critical gaps fail closed for consequential paths.

## 14. Architecture completion tests

The architecture is structurally coherent only if:

- every numbered plane appears exactly once in the responsibility partition;
- each load-bearing capability has one primary functional owner;
- cross-plane relationships are dependencies/interfaces, not implicit dual ownership;
- cognition cannot authorize its own durable effects;
- Control Plane cannot redefine domain truth or evidence;
- Memory, Knowledge, State, Models and Canon remain separate;
- Agents/Skills/Workflows/Tools remain capability/deployment representations rather than root authority;
- Observability/Tests can falsify implementation claims;
- archive/history cannot silently become current authority;
- source/model/observation/decision classes survive transformations;
- unresolved semantics remain visible as `UNKNOWN/GAP`.

## 15. Navigation

- [[00_ROOT/ARCHITECTURE|ARCHITECTURE]]
- [[00_ROOT/PLANE_OWNERSHIP_MATRIX|PLANE_OWNERSHIP_MATRIX]]
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- [[01_CANON/03_COGNITION_CANON/FULL_BRAIN_OS_CANON|FULL_BRAIN_OS_CANON]]
- [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]]
- [[11_KNOWLEDGE/AMOS_FULL_BRAIN_OS_ARCHITECTURE|AMOS_FULL_BRAIN_OS_ARCHITECTURE]]
- [[11_KNOWLEDGE/AMOS_INFRASTRUCTURE_FULL_BRAIN_AGENT_ARCHITECTURE_ROUND11|ROUND11_INFRASTRUCTURE_ARCHITECTURE]]

## 16. Boundary

This is a **DERIVED / AMOS_MODEL** architecture.

```text
DOCUMENTED != IMPLEMENTED
MODEL != OBSERVATION
STRUCTURAL SIMILARITY != CAUSATION
REFERENCE IMPLEMENTATION != PRODUCTION DEPLOYMENT
UNKNOWN/GAP != PASS
```

**Parent:** [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
