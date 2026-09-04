---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Agentskills Io Specification 2026 08 30
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

# Agent Skills Specification — Raw Capture

Source: `https://agentskills.io/specification`

## Format Specification

An Agent Skill is a directory containing at minimum a `SKILL.md` file.

### Directory Structure

```text
skill-name/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable scripts
├── references/       # Optional: reference documentation
└── assets/           # Optional: templates and static assets
```

### Frontmatter Fields

`SKILL.md` requires YAML frontmatter:

- `name`: Lowercase, hyphen-separated identifier matching the directory name.
- `description`: 1-2 sentence summary of what the skill does and when to activate it.
- `license`: Optional SPDX license identifier.
- `version`: Semantic version string.

### Progressive Disclosure Protocol

1. **Discovery**: Agent inspects available skill names and descriptions.
1. **Activation**: Agent views `SKILL.md` when intent matches description.
1. **Execution**: Agent follows instructions and executes bundled scripts as required.
