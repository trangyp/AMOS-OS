---
name: agent-naming-audit
version: 1.0.0
source: AGENT_SCHEMA.md, Agent_Templates.md, amos-agent-registry-index.md
description: AMOS agent naming and structure audit produced from .devin/agents across the vault.
---

# AMOS Agent Naming Audit

## Scope
- Tree scanned: `.devin/agents`
- Total agent JSON files: 834
- Non-JSON or unreadable: 0

## Issue Summary (before / after)

| Issue | Before | After | Notes |
|-------|-------:|------:|-------|
| Files with `name` not matching filename | 213 | 0 | All `name` fields normalized to filename slug |
| Files missing required schema fields | 407 | 0 | All 834 now satisfy the Agent Structure Standard |
| Short `description` (< 80 chars) | 78 | 0 | Re-extracted from `## Description` / `## Identity` / `## Purpose`; fallback contextualized for no-skill cases |
| Placeholder `Agent for amos-...` descriptions | 209 | 0 | First pass already cleared; re-verified clean |
| Double `amos-` prefix files | 0 | 0 | Prior pass removed `amos-amos-*` doubles |
| JSON parse errors | 0 | 0 | — |

## Decorative / Source-Protected Filename Terms

228 agent filenames contain decorative or depth/suffix tokens. These were **not** renamed automatically because they may be source-defined:

| Token | Count | Examples |
|-------|------:|----------|
| `super` | 31 | `amos-c01-meta-logic-super-agent` |
| `full` | 19 | `amos-fractal-runtime-cells-full-agent` |
| `x100k` | 11 | `amos-brain-superxc-ubi-cognitive-max-agent` (compound) |
| `x1000` | 3 | `amos-orchestrator-routing-x1000-agent` |
| `x3000` | 3 | `amos-c03-physics-cosmos-x3000-agent` |
| `50000` | 2 | `amos-wealth-game-50000-fractal-quantum-economy-agent` |
| `30000` | 2 | `amos-strict-fractal-30000-quantum-atlas-agent` |
| `25000` | 2 | `amos-math-fractal-25000-quantum-bridge-agent` |
| `5000` | 1 | `amos-fractal-architecture-framework-5000-agent` |
| `vinfinity` | 9 | `amos-universe-kernel-vinfinity-agent` |
| `v0`, `v1`, `v2` | 33 | `amos-control-systems-kernel-v0-agent` |
| `omega` | 5 | `amos-omega-thinking-engine-with-coding-agent` |
| `master` | 4 | `amos-quantum-fractal-math-master-agent` |
| `ultimate` | 2 | `amos-quantum-fractal-math-ultimate-agent` |
| `core7` | 4 | `amos-quantum-stack-core7-agent` |
| `domains7` | 2 | `amos-unified-coding-engine-v0-domains7-agent` |
| `cognitive4` | 3 | `amos-electrical-power-engine-v0-cognitive4-agent` |

## Rename / Normalization Manifest

- **Filename renames applied:** none
- **`name` field normalizations applied:** 213
  - Missing `amos-` prefix added where filename had it but `name` did not (e.g., `unipower-unitaxi-mece-agent` → `amos-unipower-unitaxi-mece-agent`)
  - Title/role strings that appeared in the `name` slot were moved to `role`
  - All `name` fields now equal `filename_without_extension`

## Enhancement Pass

Every agent was brought to the `Agent Structure Standard`:

- `name`, `description`, `version`, `author`, `system`, `role` populated
- `capabilities` normalized to object array with `name`, `description`, `inputs`, `outputs`
- `operations` populated with `entry_point`, `protocol`, `scope`, `exclusions`
- `integrity_requirements` normalized to at least 3 key/value entries
- `depends_on_skills` and `depends_on_workflows` added if missing
- Legacy `dependencies` / `entry_points` arrays were preserved and mapped into the standard fields where applicable
- Original `procedures` blocks were retained inside `operations` as extra context when present

### v2 — SKILL.md Real-Content Re-fill

After the structural pass, every agent was re-visited against its matching `.devin/skills/` file:

- 670 agents matched a `SKILL.md` and had `description`, `role`, `capabilities`, `operations` (`protocol`, `scope`, `exclusions`), `integrity_requirements`, `depends_on_skills`, and `depends_on_workflows` re-populated from that skill.
- 164 agents had no matching skill and kept original/fallback content, with missing standard fields backfilled.
- 74 short descriptions were extended from skill body sections (`## Description`, `## Identity`, `## Purpose`).
- 69 remaining short descriptions were expanded with a generated contextual fallback.
- Legacy `procedures` and `entry_points` arrays were preserved as `operations.procedures` extras.
- `depends_on_skills` were rebuilt from `## Related Skills` or legacy `dependencies`.
- `depends_on_workflows` were matched against the actual `.devin/workflows/` inventory.

### v3 — Capability Source and Exclusion Split

A further pass focused on the two examples you corrected (`amos-information-measure-governance-agent` and `amos-validation-pipeline-agent`):

- `capabilities` now prioritize `## Capabilities`, then `## Key Operations`, then `## Steps` / `## Operations` before falling back to `## Core Components`.
- 660 agents had `operations.exclusions` split from `## Anti-Overclaim` / `## Invariants` into a list of separate strings (sentences / clauses).
- `integrity_requirements` are now populated from the same split invariants.
- `depends_on_skills` now includes the matching skill itself plus `## Related Skills`.
- All 834 agents were re-verified: `name` matches filename, all required schema fields present, `exclusions` is an array, descriptions ≥ 80 chars.

## Registry Note

The current canonical count in `amos-agent-registry-index.md` is **674** agents. The actual on-disk count is **834**. The registry should be updated or split into `canonical` vs `full` counts if the 674 number is meant to track only the canonical subset.

## Next Steps

1. Review the 228 decorative/suffix agent filenames for source-protected vs cosmetic terms.
2. Decide whether to rename files to the `amos-{role}-agent` plain form and update any in-vault wikilinks.
3. Verify `depends_on_workflows` mappings against the actual `.devin/workflows/` inventory.
4. Refresh `amos-agent-registry-index.md` to reflect the full 834-agent set if desired.
