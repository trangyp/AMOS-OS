---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 06 Agent Systems/Agent Schema
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---

# Agent Schema — Construction Contract

## 0. Status

AMOS_MODEL specification for agent construction. Canonical status: CONDITIONAL. Implementation: PARTIAL. This specification defines the mandatory schema for all AMOS agents. `DOCUMENTED ≠ IMPLEMENTED`. `CAPABILITY ≠ AUTHORITY`.

## 1. Purpose

Define the mandatory construction contract for every AMOS agent. An agent is not valid unless it carries all four schema components: IDENTITY, OBJECTIVE, CAPABILITIES, CONSTRAINTS. This schema is the load-bearing artifact for agent fabrication, delegation, and economy governance.

## 2. Formal Definition

### 2.1 Schema Components

| Component | Fields | Required | Description |
|---|---|---|---|
| **IDENTITY** | agent_id, agent_name, lineage, epoch | YES | Unique identity and provenance chain |
| **OBJECTIVE** | task_objective, scope, stakes, freshness | YES | What the agent is authorized to pursue |
| **CAPABILITIES** | capability_set, skill_bindings, tool_access | YES | Declared capabilities (not authority) |
| **CONSTRAINTS** | mutation_class_limit, depth_limit, consequence_ceiling, irreversibility_ceiling | YES | Hard bounds on agent behavior |

### 2.2 Identity Contract

```
IDENTITY = {
  agent_id: <uuid>,
  agent_name: <string>,
  lineage: [<parent_agent_id>, ...],
  epoch: <causal_epoch>,
  spiffe_id: <optional>,
  provenance_hash: <sha256>
}
```

### 2.3 Objective Contract

```
OBJECTIVE = {
  task_objective: <natural_language>,
  scope: <AMOS_general | subsystem_specific>,
  stakes: <0.0..1.0>,
  freshness: <timestamp>,
  authority_ref: <authority_artifact_id>
}
```

### 2.4 Capabilities Contract

```
CAPABILITIES = {
  capability_set: [<capability_token>, ...],
  skill_bindings: [<skill_id>, ...],
  tool_access: [<tool_id>, ...],
  h_m_l_resolution: <H | M | L>
}
```

### 2.5 Constraints Contract

| Constraint | Default | Description |
|---|---|---|
| mutation_class_limit | M2 | Maximum mutation class agent may execute |
| depth_limit | 2 | Maximum delegation depth |
| consequence_ceiling | 0.35 | Maximum consequence score |
| irreversibility_ceiling | 0.20 | Maximum irreversibility score |
| non_compensatory_refusals | 6 | Hard gates that cannot be overridden |

### 2.6 Validation Rules

1. All four components must be present and non-empty.
2. `capability_set` must be a subset of granted capabilities (not requested).
3. `authority_ref` must be epoch-valid; capability alone never authorizes.
4. `consequence_ceiling` and `irreversibility_ceiling` must not exceed autonomous envelope.
5. `lineage` must form a valid DAG (no cycles).

## 3. AMOS Architecture Integration

- **Control Plane:** Agent schema is validated by the authority engine before admission.
- **Runtime:** Runtime sandbox enforces constraints at execution time.
- **Security:** Capability tokens are verified by the security plane.
- **Lifecycle:** Schema is bound at PROPOSED state and locked at ADMITTED state.
- **Delegation:** Child agent schema must satisfy `ChildScope(t) ⊆ ParentScope(t)`.

## 4. Cross-References

- [[00_ROOT/00_ROOT_MOC|Root MOC]]
- [[AMOS_HOME|AMOS Home]]
- [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|Law Hierarchy]]
- [[06_AGENT_SYSTEMS/06_AGENT_SYSTEMS_MOC|Agent Systems MOC]]
- [[06_AGENT_SYSTEMS/DELEGATION_LIFECYCLE|Delegation Lifecycle]]
- [[06_AGENTS/AMOS_AGENT_SCHEMA_FULL|Legacy Agent Schema Full]]
- [[03_CONTROL_PLANE/04_AUTHORITY/AUTHZ_ENGINE_VALIDATION_RECEIPT|AuthZ Engine]]

## 5. Gaps

- Runtime enforcement of schema constraints: UNKNOWN/GAP
- Schema versioning and migration: NOT_ESTABLISHED
- Empirical validation of schema completeness: NOT_ESTABLISHED

## 6. Ingestion Rule

This is an AMOS_MODEL specification. Do not infer implementation from specification. Promotion requires executed validation receipt specific to this artifact.

---

> **RSCF-NODE** | state: OBSERVATION | claim_class: OBSERVATION | provenance: amos_architecture_2026-09-04 | scope: AMOS_general | confidence_ceiling: source_supported | provenance_independence: NOT_ESTABLISHED
