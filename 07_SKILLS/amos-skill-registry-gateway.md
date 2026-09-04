---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Amos Skill Registry Gateway
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

# AMOS Skill Registry Gateway

## When to Use

- When you need to discover what AMOS skills are available
- When you need to find a skill for a specific domain or capability
- When you need to fetch a skill on demand instead of loading all skills

## Registry Summary

- **Total skills**: 342
- **Total domains**: 42
- **Registry version**: 1.0.0

## Domain Catalog

| Domain | Skill Count |
|--------|------------|
|  | 1 |
| agent | 9 |
| arxiv | 41 |
| audit | 23 |
| boundary | 12 |
| c01 | 2 |
| c02 | 1 |
| c03 | 1 |
| c04 | 7 |
| c05 | 10 |
| c06 | 5 |
| c07 | 1 |
| c08 | 4 |
| c09 | 4 |
| c10 | 33 |
| c11 | 1 |
| c12 | 1 |
| canon | 12 |
| causal | 8 |
| cross-domain | 1 |
| cross-domain (C04 Bio-Neuro ↔ C03 Physics-Cosmos) | 1 |
| cross-domain (C05 → Memory → Knowledge) | 1 |
| cross-domain (C05→C01→C10) | 1 |
| cross-domain (C06 Vietnamese ↔ Global) | 1 |
| cross-domain (C09 → C10 → Runtime) | 1 |
| econ | 4 |
| engines-master | 5 |
| formal | 15 |
| fractal | 5 |
| fx | 20 |
| info | 5 |
| information | 1 |
| knowledge | 14 |
| mckinsey | 24 |
| memory | 7 |
| mind_behavior | 1 |
| rscf | 26 |
| runtime | 19 |
| security | 8 |
| skill | 1 |
| trang | 4 |
| workflow | 1 |

## How to Fetch

1. **Search**: Browse the catalog above to find the domain you need
2. **Select**: Pick the skill name from the domain's skill list
3. **Load**: Read the skill's `SKILL.md` from `07_SKILLS/<skill-name>/SKILL.md`
4. **Validate**: Check the skill's epistemic class and scope before use

## Supported Platforms

This registry supports installation to multiple agent platforms:

| Platform | Install Directory |
|----------|------------------|
| claude-code | .claude/skills |
| claude-chat | .devin/skills |
| github-copilot | .agents/skills |
| cursor | .cursor/skills |
| codex | .codex/skills |
| gemini-cli | .gemini/skills |
| windsurf | .codeium/windsurf/skills |
| cline | .cline/skills |

## Anti-Patterns

- Do NOT load all skills at once — use fetch-on-demand
- Do NOT skip epistemic class validation when loading a skill
- Do NOT use a skill outside its declared domain scope

## Provenance

- **Registry generated**: 2026-09-03T12:47:32.994468+00:00
- **Source**: AMOS_OS Obsidian vault
- **Steward**: Trang Phan
