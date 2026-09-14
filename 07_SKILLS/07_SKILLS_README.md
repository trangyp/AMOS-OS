---
title: "07 Skills — Plane README"
type: plane-readme
source: 07_SKILLS
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_GUIDANCE
epistemic_class: AMOS_MODEL
---

# 07 Skills — README

## Role

Skills encode reusable bounded capability: discoverable, composable, provenance-aware units of work used by AMOS agents and workflows.

```text
SKILL != AGENT
SKILL != WORKFLOW
SKILL != TOOL
SKILL != AUTHORITY
```

## Active repository contract

The detailed creation, migration, progressive-loading, external-source, and validation rules are owned by:

`[[07_SKILLS/SKILLS_README|SKILLS_README]]`

Do not maintain a second competing Skill schema in this file.

## Portable discovery surface

New or substantially migrated Skills use:

```yaml
---
name: lowercase-hyphenated-name
description: What the Skill does and the concrete conditions that trigger it.
---
```

AMOS-specific provenance, epistemic, parent/child, and governance metadata remain explicit in the body or appropriate companion artifacts.

## Inter-plane connections

- **Agents:** `[[06_AGENTS/06_AGENTS_MOC|06_AGENTS_MOC]]`
- **Agent systems/interoperability:** `[[06_AGENT_SYSTEMS/GITHUB_AGENT_SKILL_INTEROP|GITHUB_AGENT_SKILL_INTEROP]]`
- **Workflows:** `[[08_WORKFLOWS/08_WORKFLOWS_MOC|08_WORKFLOWS_MOC]]`
- **Tools:** `[[14_TOOLS/14_TOOLS_MOC|14_TOOLS_MOC]]`
- **Control plane:** `[[03_CONTROL_PLANE/02_CAPABILITY/CAPABILITY_MANIFEST|CAPABILITY_MANIFEST]]`

## Validation

```bash
python3 scripts/validate_agent_skill_surface.py --summary
```

Legacy schema warnings represent migration debt, not automatic invalidity. New portable Skills fail closed on malformed discovery metadata or missing bundled references.

______________________________________________________________________

**Parent:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
