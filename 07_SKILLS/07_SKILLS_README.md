---
canon-group: meta
canon-type: framework
rscf-state: source-claim
topic: 07 Skills Readme
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---

# 07 Skills — README

## Role

Skills encode reusable bounded capability — named, versioned, composable, provenance-aware, and epistemically gated units of work that agents can invoke.

## Skill Contract

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

## Properties

- Scoped: clear boundaries on what the skill does
- Versioned: explicit version tracking
- Composable: skills can be combined
- Provenance-aware: every skill invocation is traceable
- Epistemically gated: conclusion class is always declared

## Inter-Plane Connections

- **Agents:** [[06_AGENTS/06_AGENTS_MOC|06_AGENTS_MOC]] — Agents use skills
- **Workflows:** [[26_WORKFLOWS/26_WORKFLOWS_MOC|26_WORKFLOWS_MOC]] — Skills compose into workflows

______________________________________________________________________

**Parent:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
