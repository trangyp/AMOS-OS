---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Vault Domain Knowledge
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

# Auto Tag Plugin for Obsidian.md

External source: https://github.com/CtrlAltFocus/obsidian-plugin-auto-tag

## Overview

The Auto Tag plugin for Obsidian assists users in automatically generating tags for notes. It can analyze the full note or a selected portion and insert the generated tags into the note's YAML frontmatter.

## Features

- **Automatic Tag Generation**: Analyze the entire note or just a selected portion to generate relevant tags.
- **Frontmatter Integration**: Automatically inserts tags into the note's frontmatter. If frontmatter doesn't exist, the plugin creates it.
- **OpenAI Powered**: Utilizes OpenAI's API to ensure accurate and relevant tag suggestions.
- **Demo Mode**: Try out the plugin's functionality and settings combinations without needing an API key.

## Tag Options

- **Tag Format**: choose between kebab-case, snake_case, camelCase, PascalCase, and more.
- **Language detection**: returns tags in the detected language of the note.
- **Preview before insertion**: preview the tags before they are inserted into the note (and accept/ignore each tag).

## Getting Started

1. Install from Obsidian's community plugins list.
1. Create an OpenAI API key at https://platform.openai.com.
1. Configure billing and a maximum monthly spend.
1. Enter the API key in the plugin settings.
1. Open a note, optionally select text, and trigger the "Auto Tag" command.

## Cost Notes

- Demo mode is enabled by default.
- Full mode requires OpenAI billing and incurs cost.
- GPT-3.5 is cheap and sufficient for most cases.
- Set a low monthly limit to start.

## Release Notes (selected)

- 0.3.0 — loading state, better query, predictability/creativity toggle, cost estimation popup.
- 0.2.11 — multi-lingual tags.
- 0.2.10 — tag format choice.
- 0.2.9 — fix multi-word tags with spaces.
- 0.2.6 — first public release.

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] · references_MOC · SKILL

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: obsidian-plugin-auto-tag_vault_domain_knowledge
node_type: reference
path: 07_SKILLS/obsidian-plugin-auto-tag/references/vault_domain_knowledge.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
- RELATED_TO: SKILL
