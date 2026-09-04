---
title: AMOS Knowledge Research Master
aliases:
  - amos-knowledge-research-master
  - 07_SKILLS/amos-knowledge-research-master
type: redirect
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 07_SKILLS/amos-knowledge-research-master/SKILL.md
  scope: 07_SKILLS
---
# AMOS Knowledge Research Master

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **Domain:** `knowledge`
> **Epistemic Class:** `AMOS_MODEL`
> **Claim Class:** `DERIVED`
> **Governing Plane:** `07_SKILLS`

---

## Purpose

This redirect anchors the AMOS Knowledge and Research master skill, the root authority for Obsidian vault integration, arxiv research, knowledge indexing, curation, and RAG best practices. It treats the 68,979-note vault as a reasoning brain. It routes all knowledge-research queries to the canonical SKILL.md and its 143 consolidated sub-skills.

## Domain Coverage

1. Vault knowledge integration: read, parse, index Markdown files with provenance and epistemic class
2. Knowledge entry validation: provenance, epistemic class, freshness, dependency chain
3. Knowledge graph analysis: MOC structure, orphan notes, wikilink health, knowledge frontier
4. Provenance tracing to vault source paths, arxiv papers, and derivation chain
5. Knowledge claim assessment: source quality, citation completeness, scope validity
6. Knowledge lifecycle management: ingest, index, curate, validate, update, archive
7. Drift detection: stale entries, broken wikilinks, orphan notes, provenance decay

## Key Capabilities

| Capability | Function |
| :--- | :--- |
| `knowle_research.integrate_vault` | Integrate vault knowledge: read, parse, index with provenance |
| `knowle_research.validate_knowledge` | Validate knowledge entries for provenance, freshness, dependencies |
| `knowle_research.analyze_knowledge` | Analyze knowledge graph: MOC structure, orphan notes, wikilink health |
| `knowle_research.assess_knowledge_claim` | Assess knowledge claims for source quality and citation completeness |
| `knowle_research.detect_knowledge_drift` | Detect stale entries, broken wikilinks, orphan notes, provenance decay |

## MECE Mapping to AMOS Planes

- **11_KNOWLEDGE**: Knowledge plane and MOC hierarchy
- **07_SKILLS**: Procedural capability registry (this plane)
- **22_RESEARCH**: Research integration and arxiv paper processing
- **10_MEMORY**: Memory store integration for knowledge persistence
- **17_OBSERVABILITY**: Receipt sealing for knowledge lifecycle events

## Epistemic Boundaries

- `CAPABILITY != AUTHORITY`: Implementing a procedure does not confer execution rights
- `DOCUMENTED != IMPLEMENTED`: Skill specification presence does not prove runtime deployment
- `SKILL != AGENT`: This skill is a passive procedure; agents invoke it, it never self-triggers
- Domain claims remain `DERIVED` until independently validated against vault sources

## Sub-Skill Consolidation

This master skill consolidates 143 sub-skills under the `knowledge` domain. Each sub-skill inherits the master's epistemic boundaries and RSCF state classification while maintaining its own capability scope and validation gates.

## Navigation

- **Canonical SKILL:** [[07_SKILLS/amos-knowledge-research-master/SKILL.md|AMOS Knowledge Research Master SKILL.md]]
- **Agent Template:** [[07_SKILLS/amos-knowledge-research-master/AGENT_TEMPLATE.md|AMOS Knowledge Research Master AGENT_TEMPLATE]]
- **MOC:** [[07_SKILLS/amos-knowledge-research-master/amos-knowledge-research-master_MOC|amos-knowledge-research-master_MOC]]
- **Skills MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
- **Skill Contract:** [[07_SKILLS/SKILLS_SKILL_CONTRACT|SKILLS_SKILL_CONTRACT]]
- **Vault Source:** [[11_KNOWLEDGE/11_KNOWLEDGE_MOC|11_KNOWLEDGE_MOC]]
- **AMOS Home:** [[00_ROOT/00_HOME|00_HOME]]
- **RSCF Registry:** [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
