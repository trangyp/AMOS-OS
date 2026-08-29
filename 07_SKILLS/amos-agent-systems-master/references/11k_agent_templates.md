---
title: 11k agent templates
type: reference
source: 07_SKILLS/amos-agent-systems-master/references
tags:
- reference
- amos-agent-systems-master
- type/skill
- amos-agent-systems-master-moc
- 00-home
- amos-rscf-nodes
- law-hierarchy
- references-moc
- 07-skills-moc
- trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# 11K Agent Templates

> Source: `/Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/Agent_Templates.md`
> Epistemic class: SOURCE_DERIVED

---
canon-group: meta
canon-type: framework
canon-status: active
canon-scope: agent-architecture
canon-layer: meta-agent
canon-owner: Trang Phan

artifact-id: AMOS-AGENT-TEMPLATES
artifact-type: framework-registry
artifact-class: agent-factory-architecture

version: "2.0.0"
schema-version: "1.0.0"
protocol-version: "1.0.0"
amos-core-target: "v4.4"

rscf-state: source-claim
rscf-class: STRUCTURAL_MODEL
rscf-confidence-ceiling: source-bounded
rscf-provenance-required: true

topic: agent-templates

tags:
  - canon-group/tech-ai
  - canon/framework
  - canon/agent
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - topic/agent-templates
  - topic/agent-architecture
  - topic/agent-factory
  - agents

created: 2026-08-22
updated: 2026-08-25
origin-architect: Trang Phan
steward: Trang Phan
---

# AMOS Agent Templates

> **Version:** `2.0.0`
> **Schema Version:** `1.0.0`
> **Protocol Version:** `1.0.0`
> **AMOS_CORE Target:** `v4.4`
> **Origin Architect:** Trang Phan
> **Classification:** `STRUCTURAL_MODEL`
> **RSCF State:** `SOURCE_CLAIM`

---

## 1. Purpose

**AMOS Agent Templates** defines the canonical structural templates used to instantiate, configure, validate, govern, version, and retire agents inside the AMOS ecosystem.

The framework does **not** define one universal agent implementation.

It defines the minimum structural contract from which specialized AMOS agents can be constructed without losing:

- identity;
- purpose;
- scope;
- authority;
- capability boundaries;
- dependency lineage;
- provenance;
- evidence classification;
- runtime constraints;
- input/output contracts;
- governance;
- validation;
- version identity;
- lifecycle state;
- rollback and retirement semantics.

The governing principle is:

```text
Agent
=
Identity
+ Purpose
+ Scope
+ Capabilities
+ Dependencies
+ Authority
+ State
+ Runtime
+ Governance
+ Evidence
+ Validation
+ Lifecycle
```

This is an **AMOS structural equation**, not an empirical law of all agent systems.

---

# 2. Canonical Position

```text
AMOS
└── Meta Architecture
    └── Agent Architecture
        ├── Agent Schema
        ├── Agent Templates
        ├── Agent Assembly
        ├── Agent Runtime
        ├── Agent Governance
        ├── Agent Validation
        └── Agent Lifecycle
```

`Agent Templates` sits between the abstract schema and concrete agent instances.

```text
AGENT_SCHEMA
      ↓
AGENT_TEMPLATE
      ↓
AGENT_CONFIGURATION
      ↓
AGENT_INSTANCE
      ↓
RUNTIME_VALIDATION
      ↓
GOVERNED_EXECUTION
```

Hard distinction:

```text
Schema
!=
Template
!=
Configuration
!=
Runtime Instance
```

---

# 3. Framework Invariants

Every AMOS agent template MUST preserve the following invariants.

## AT-I01 — Identity

Every agent has an explicit identity.

```text
AgentIdentity != implicit role inferred from prompt
```

---

## AT-I02 — Purpose

Every agent declares why it exists.

```text
AgentPurpose
=
DeclaredObjectiveSet
```

An agent without a bounded purpose is incomplete.

---

## AT-I03 — Scope

Every agent declares:

```text
IN_SCOPE
OUT_OF_SCOPE
```

Absence of an explicit exclusion does not automatically grant capability or authority.

---

## AT-I04 — Capability / Authority Separation

```text
CanPerform(x)
!=
AuthorizedToPerform(x)
```

Technical capability never creates authority.

---

## AT-I05 — Dependency Declaration

Every load-bearing runtime dependency must be identifiable.

```text
AgentValid
→
DependenciesResolvable
```

---

## AT-I06 — Provenance

Consequential claims and state transitions must remain traceable to their relevant sources.

```text
Claim
→ Source
→ Transformation
→ Dependency
→ Result
```

---

## AT-I07 — Evidence Boundary

Agent outputs must distinguish, where material:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN/GAP
```

---

## AT-I08 — Scope / Regime Boundary

An agent cannot silently generalize beyond its declared applicability envelope.

```text
ValidOutput
→
ScopeCompatible
∧ Reg

---
**MOC:**

## Related

-
```

---

**Related:** [[amos-agent-systems-master_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-agent-systems-master-11k-agent-templates
node_type: reference
path: 07_SKILLS/amos-agent-systems-master/references/11k_agent_templates.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
