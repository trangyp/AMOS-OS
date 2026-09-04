---
title: AMOS Plane Ownership Matrix
type: architecture_registry
source: 00_ROOT
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_DERIVED_REGISTRY
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
updated: 2026-09-03
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE
    - 11_KNOWLEDGE/AMOS_FULL_BRAIN_OS_ARCHITECTURE
    - 11_KNOWLEDGE/AMOS_INFRASTRUCTURE_FULL_BRAIN_AGENT_ARCHITECTURE_ROUND11
  scope: physical_plane_primary_ownership
---

# AMOS Plane Ownership Matrix

This registry assigns **one primary responsibility domain and one primary functional ownership
statement to every numbered physical plane**.

## 1. MECE responsibility domains

```text
A NORMATIVE & GOVERNANCE DEFINITION
B EXECUTION CORE & EFFECT GOVERNANCE
C COGNITIVE CAPABILITY & ORCHESTRATION
D INFORMATION / MEMORY / STATE / MODEL SUBSTRATE
E INTERACTION / SECURITY / EFFECT ADAPTERS
F ASSURANCE / LEARNING / LIFECYCLE EVIDENCE
```

Each numbered plane belongs to exactly one domain.

## 2. Ownership matrix

| Plane | Domain | Primary functional ownership | Explicit non-ownership |
|---|---|---|---|
| 01 Canon | A | admitted AMOS definitions, laws, lineage and supersession | runtime execution; empirical proof |
| 02 Kernel | B | deterministic reasoning/state-integrity primitives | domain truth; external effect authority by itself |
| 03 Control Plane | B | authority, semantic transaction, commit/finality eligibility | cognition; domain inference |
| 04 Runtime | B | bounded execution lifecycle, replay/recovery and typed runtime transitions | canon admission; root trust creation |
| 05 Cognitive Organism | C | persistent cognitive loop, organs and supervisory cognition | durable-effect authorization |
| 06 Agents | C | bounded goal-bearing worker/orchestrator/auditor identities | root authority; skill semantics |
| 07 Skills | C | versioned reusable capability procedures | durable authority |
| 08 Workflows | C | explicit process/state-transition orchestration | domain truth; canon semantics |
| 09 Protocols | E | cross-component interaction and handoff semantics | workflow ownership; policy authority |
| 10 Memory | D | governed temporal persistence and retrieval | state authority; truth promotion |
| 11 Knowledge | D | source/evidence/claim/relationship knowledge substrate | canon admission; effect authority |
| 12 State | D | current/historical state identity, versions and epochs | memory semantics; policy ownership |
| 13 Models | D | explicit source-bound/system/domain models and simulations | observation; empirical truth |
| 14 Tools | E | host capabilities and effect-adapter implementations/descriptions | effect authorization |
| 15 Interfaces | E | typed semantic boundaries between systems | domain/canon semantics |
| 16 Schemas | D | typed records, tensors and contract schemas | semantic truth; runtime evidence |
| 17 Observability | F | telemetry, receipts, traces and failure visibility | authorization; causal proof by itself |
| 18 Security | E | protected-boundary, identity/access and trust-domain constraints | general canon replacement |
| 19 Tests | F | executable checks and bounded validation evidence | universal correctness |
| 20 Operations | F | runbooks, incidents, maintenance, recovery and audit lineage | canon/architecture authority |
| 21 Domains | C | specialist domain ownership and routing | infrastructure finality |
| 22 Research | F | research acquisition, experiment and validation lifecycle | automatic canon promotion |
| 23 Operating Model | A | roles, decision rights, forums, escalation and service expectations | platform/root authority by itself |
| 24 Archive | F | historical/superseded lineage retention | current authority |
| 25 Cognitive Matrix | C | fractal cognitive coordinate/routing decomposition | effect authorization |

## 3. Completeness check

```text
A = {01, 23}
B = {02, 03, 04}
C = {05, 06, 07, 08, 21, 25}
D = {10, 11, 12, 13, 16}
E = {09, 14, 15, 18}
F = {17, 19, 20, 22, 24}
```

All planes `01..25` occur exactly once.

`00_ROOT` is excluded because it is the navigation/authority-pointer meta-plane rather than a numbered
functional plane.

## 4. Conflict-resolution rule

When an artifact appears to fit multiple planes, classify by the **state, decision, capability or
effect it owns**, not by vocabulary.

Examples:

- an FX model is owned by Models/Domain capability; a workflow invoking it remains Workflow;
- a memory-validation receipt is Test/Observability evidence, not Memory ownership;
- an agent calling a tool remains an Agent; the adapter remains Tool; authority remains Control Plane;
- a governance document defining human decision rights belongs Operating Model, while infrastructure
  effect authorization belongs Control Plane;
- a source document about a model belongs Knowledge when acting as evidence and Models when acting as
  an explicit executable/conceptual model object; use one primary artifact owner and cross-link the
  other role.

## 5. Primary-owner contract

```yaml
ownership:
  primary_plane: REQUIRED
  primary_responsibility: REQUIRED
  dependency_planes: []
  interface_planes: []
  authority_plane: null
  evidence_plane: null
  supersedes: []
  provenance: REQUIRED
```

A secondary dependency never acquires ownership merely by being load-bearing.

## 6. Authority firewall

```text
PRIMARY OWNERSHIP != EXCLUSIVE DEPENDENCY
DEPENDENCY != AUTHORITY
CAPABILITY != AUTHORITY
STORAGE LOCATION != FUNCTIONAL OWNERSHIP
CROSS-LINK != DUPLICATED AUTHORITY
OBSERVED != AUTHORIZED
```

## 7. Full Brain mapping

The three Full Brain systems use, but do not replace, the MECE physical partition:

```text
BRAIN
  primary cognitive ownership -> Domain C
  information/model dependency -> Domain D
  interface dependency -> Domain E

RUNTIME
  primary execution ownership -> Domain B
  state/schema dependency -> Domain D
  protocol dependency -> Domain E

CONTROL/BODY
  primary authority ownership -> Domain B / 03_CONTROL_PLANE
  security/effect dependency -> Domain E
  organizational constraints -> Domain A / 23_OPERATING_MODEL
```

This mapping is many-to-one across architectural views. The **plane partition remains MECE**.

## 8. Navigation

- [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]]
- [[00_ROOT/ARCHITECTURE|ARCHITECTURE]]
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]

**Parent:** [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
