---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 06 Agents Readme
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

# 06 Agents — README

## Role

Agents are scoped active components — the actors that perform operations within AMOS OS. Every agent declares identity, role, scope, inputs, outputs, dependencies, permissions, authority, memory policy, provenance, tests, failure modes, and recovery.

## Hard Rules

```
AgentName != AgentCapability
AgentCapability != AgentAuthority
```

## Structure

```
06_AGENTS/
├── 00_INDEX/              ← Agent registry and navigation
├── AGENT_MAP.md           ← Master agent registry
├── AGENTS_README.md       ← This file
├── AGENT_CONTRACT.md      ← Agent contract specification
└── [agent-specific files]
```

## Agent Contract Template

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

## Inter-Plane Connections

- **Cognitive Organism:** [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]] — Cognitive organism coordinates agents
- **Skills:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] — Agents use skills
- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] — Control plane authorizes agents

______________________________________________________________________

**Parent:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
