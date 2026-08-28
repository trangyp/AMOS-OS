---
title: SKILL — Obsidian Plugin Auto Tag
type: skill
source: 07_SKILLS/obsidian-plugin-auto-tag
name: obsidian-plugin-auto-tag
description: Auto Tag — AMOS knowledge-management utility. Use when automatically generating, normalizing, or reconciling tags and frontmatter metadata in the Obsidian vault. Use when amos-knowledge-research-master routes to this tool capability. Do not use for for generic tasks outside the declared amos domain.
parent_skill: amos-knowledge-research-master
domain: knowledge
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/knowledge-research
- rscf/source_claim
- hml/m
- epistemic/source_claim
- amos_os
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.0.0
rscf_state: SOURCE_CLAIM
hml_level: M
gmef_gates:
- L0_integrity
- L1_epistemic
- L2_provenance
- L5_scope
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L4
- L5
- L16
- L17
license: MIT
---

# Obsidian Plugin Auto Tag

## Identity

Origin architect: **Trang Phan**. Domain: knowledge. Parent: amos-knowledge-research-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.
## When to Use

- When a note's `tags` frontmatter is missing, empty, or inconsistent with its content
- When bulk normalizing tag case, separators, or language across the vault
- When integrating auto-generated tags into the RSCF frontmatter `tags` list
- When the parent skill (`amos-knowledge-research-master`) routes to this utility capability
- When formatting and tagging need to be fixed together in canon, skill, or knowledge notes

## Capabilities

- **auto_tag.generate_tags**: Generate relevant tags for a note or selected text using the Auto Tag plugin
- **auto_tag.update_frontmatter**: Insert generated tags into the note's YAML frontmatter `tags` list
- **auto_tag.normalize_format**: Normalize tag format (kebab-case, snake_case, camelCase, PascalCase)
- **auto_tag.detect_language**: Return tags in the detected language of the note
- **auto_tag.preview**: Preview suggested tags before committing them to the note
- **auto_tag.validate_scope**: Ensure suggested tags are within the note's declared canon/knowledge scope
- **auto_tag.fix_formatting**: Co-fixer for common formatting issues that accompany tagging (fence markers, whitespace)

> **Reference**: See `references/vault_domain_knowledge.md` for full vault-sourced plugin documentation.

## Vault-Sourced Domain Knowledge

> **Source**: `references/vault_domain_knowledge.md`

### Plugin Overview

The Auto Tag plugin for Obsidian uses OpenAI to suggest relevant tags for a note. It can operate on the full note or a selected portion, supports multiple tag formats, and can create `tags` frontmatter automatically.

**Key features**:
- Automatic tag generation from note content
- Frontmatter integration (creates `tags` if missing)
- Multiple tag formats: kebab-case, snake_case, camelCase, PascalCase
- Language detection and localized tags
- Preview mode with accept/ignore per tag
- Demo mode (no API key required for testing)

**Cost controls**:
- Demo mode enabled by default
- OpenAI API key and billing required for full mode
- Use GPT-3.5 for low cost; set a monthly spending limit

**Integration protocol**:
1. **Receive**: target note path and optional scope hints
2. **Generate**: query the plugin/OpenAI for tag candidates
3. **Preview**: present candidates with provenance (source terms, confidence)
4. **Filter**: remove tags outside the note's declared regime/scope
5. **Insert**: add to frontmatter `tags` preserving existing order
6. **Validate**: confirm no duplicate or contradictory tags

### Epistemic Boundary

This is an operational tool. Generated tags are `SOURCE_DERIVED` or `AMOS_MODEL` suggestions, not canon. They must be validated against the note's `rscf.scope`, `rscf.claim_class`, and canon family before being promoted to canonical tags.

## Failure Modes

- **Insufficient evidence**: If note content is too sparse, mark as UNKNOWN/GAP — do not invent tags.
- **Scope violation**: Suggested tags outside the note's declared scope are filtered and escalated.
- **API unavailability**: If OpenAI API is unavailable, fall back to existing tags or local tag index.
- **Over-tagging**: If too many tags are suggested, truncate to the most load-bearing ones.
- **Epistemic overreach**: Auto-generated tags do not establish canonical status by themselves.

## Validation Gates

- **G1 (Law of Law)**: No tag contradicts the note's canon or RSCF frontmatter.
- **G2 (Epistemic class)**: Tag provenance is recorded as DERIVED / AMOS_MODEL.
- **G3 (Provenance)**: Source term or phrase recorded for each derived tag.
- **G4 (Anti-overreach)**: Auto-tags are suggestions until validated.
- **G5 (Failure mode)**: On generation failure, preserve existing tags and flag the gap.

## Provenance

- **Skill**: `obsidian-plugin-auto-tag`
- **Parent**: `amos-knowledge-research-master`
- **Domain**: knowledge
- **Origin architect**: Trang Phan
- **External source**: https://github.com/CtrlAltFocus/obsidian-plugin-auto-tag


## Do not use

- For generic tasks outside the declared AMOS domain
- As a substitute for domain-specific analysis
- For empirical claims without evidence
- Outside the AMOS canon law hierarchy
## References

- `references/vault_domain_knowledge.md` — full plugin documentation and integration notes
- `[[obsidian-plugin-auto-tag_MOC]]` — skill Map of Content
- `amos-knowledge-research-master` — parent skill
- `obsidian-plugin-auto-tag-workflow` — corresponding workflow
- `obsidian-plugin-auto-tag-agent` — corresponding agent

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[obsidian-plugin-auto-tag_MOC]]

## Examples

- **Scenario**: When a canon note is missing `tags` frontmatter
  - **Input**: Note path + target tag format (kebab-case)
  - **Output**: Updated note with validated `tags` list and provenance

- **Scenario**: When bulk normalizing tags across the vault
  - **Input**: Folder path + target format + scope filter
  - **Output**: Diff of tag changes with confidence ceiling

## Anti-Patterns

- **Do not use** to auto-generate canonical tags for core laws without human review
- **Do not use** when a higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling for generated tags
- **Do not chain** more than 3 skills without explicit orchestrator approval

## Composition

- **Parent**: `amos-knowledge-research-master` — routes to this skill when tag/metadata work is needed
- **Peers**: Other knowledge/obsidian utility skills
- **Orchestrator**: `AMOS_HOME` orchestrates routing
- **Workflow**: `08_WORKFLOWS/obsidian-plugin-auto-tag-workflow.md`
- **Agent**: `06_AGENTS/obsidian-plugin-auto-tag-agent.json`

## Evaluation

### Success Criteria

- Generated tags are relevant to the note's content
- Existing frontmatter is preserved, not overwritten
- New tags are labeled with epistemic class and provenance
- No tag contradicts the note's declared scope or canon
- Validation receipts are produced for consequential changes

### Failure Modes

- **Overreach**: Output claims canonical status for auto-generated tags
- **Scope creep**: Tags assigned outside the note's declared domain
- **Provenance loss**: Generated tags cannot be traced to source phrases
- **Confidence inflation**: Confidence exceeds the weakest-premise ceiling

## Error Handling

- **On scope violation**: Reject the query and route back to parent skill
- **On missing evidence**: Flag as GAP and reduce confidence ceiling to 0.5
- **On contradiction**: Flag as CRITICAL_GAP and halt until resolved
- **On API failure**: Preserve state, mark tags as UNKNOWN, and escalate
- **On drift**: Trigger drift alignment via `amos-ai-drift-alignment-governor`

---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: obsidian-plugin-auto-tag
node_type: skill
path: 07_SKILLS/obsidian-plugin-auto-tag/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
