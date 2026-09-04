---
title: AMOS Agent Systems Master
aliases:
  - amos-agent-systems-master
  - 07_SKILLS/amos-agent-systems-master
type: redirect
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 07_SKILLS/amos-agent-systems-master/SKILL.md
  scope: 07_SKILLS
---
# AMOS Agent Systems Master

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **Domain:** `agent`
> **Epistemic Class:** `AMOS_MODEL`
> **Claim Class:** `DERIVED`
> **Governing Plane:** `07_SKILLS`

---

## Purpose

This redirect anchors the AMOS Agent Systems master skill, the root authority for agent fabrication, delegation, agency-consequence tensors, agent economy governance, and agent-to-agent protocols. It routes all agent-system queries to the canonical SKILL.md and its consolidated sub-skills.

## Domain Coverage

1. Agent fabrication with schema, capabilities, side-effect classification, and governance metadata
2. Task delegation with scope bounds, authority gates, and consequence tensor tracking
3. Agent composition validation: MECE coverage, skill binding integrity, capability bounds
4. Agent provenance tracing to source skills and vault provenance chains
5. Agent lifecycle management: fabricate, activate, promote, retire, archive
6. Drift detection: capability creep, scope expansion, governance decay, content hash tampering
7. Gap escalation: orphan agents, broken skill bindings, missing capabilities, repair triggers

## Key Capabilities

| Capability | Function |
| :--- | :--- |
| `agent_systems.fabricate_agent` | Fabricate agents with proper schema and governance metadata |
| `agent_systems.delegate_task` | Delegate tasks with scope bounds and consequence tensors |
| `agent_systems.validate_agent_composition` | Validate MECE coverage and skill binding integrity |
| `agent_systems.trace_agent_provenance` | Trace capabilities and delegation chain to source |
| `agent_systems.detect_agent_drift` | Detect capability creep, scope expansion, governance decay |

## MECE Mapping to AMOS Planes

- **06_AGENTS**: Calling entities that invoke this skill through capability tokens
- **07_SKILLS**: Procedural capability registry (this plane)
- **03_CONTROL_PLANE**: Authority and capability token issuance
- **17_OBSERVABILITY**: Receipt sealing for agent lifecycle events
- **01_CANON**: Law hierarchy governing agent authority bounds

## Epistemic Boundaries

- `CAPABILITY != AUTHORITY`: Implementing a procedure does not confer execution rights
- `DOCUMENTED != IMPLEMENTED`: Skill specification presence does not prove runtime deployment
- `SKILL != AGENT`: This skill is a passive procedure; agents invoke it, it never self-triggers
- Domain claims remain `DERIVED` until independently validated against vault sources

## Sub-Skill Consolidation

This master skill consolidates 11 sub-skills under the `agent` domain. Each sub-skill inherits the master's epistemic boundaries and RSCF state classification while maintaining its own capability scope and validation gates.

## Navigation

- **Canonical SKILL:** [[07_SKILLS/amos-agent-systems-master/SKILL.md|AMOS Agent Systems Master SKILL.md]]
- **Agent Template:** [[07_SKILLS/amos-agent-systems-master/AGENT_TEMPLATE.md|AMOS Agent Systems Master AGENT_TEMPLATE]]
- **MOC:** [[07_SKILLS/amos-agent-systems-master/amos-agent-systems-master_MOC|amos-agent-systems-master_MOC]]
- **Skills MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
- **Skill Contract:** [[07_SKILLS/SKILLS_SKILL_CONTRACT|SKILLS_SKILL_CONTRACT]]
- **Vault Source:** [[06_AGENTS/AGENTS_README|AGENTS_README]]
- **AMOS Home:** [[00_ROOT/00_HOME|00_HOME]]
- **RSCF Registry:** [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
