---
artifact_id: AMOS-OBSIDIAN-LINKING-PLUGINS
conclusion_class: DECISION / AMOS_MODEL
confidence: DERIVED
document_version: 1.0.0
name: AMOS_Obsidian_Linking_Plugins
origin_architect: Trang Phan
provenance: USER_REQUEST / COMMUNITY_PLUGIN_REGISTRY
status: active
steward: Trang Phan
tags:
- obsidian
- vault
- linking
- plugins
- moc
- templater
- smart-connections
- dataview
- canon-group/tech-ai
- canon/tooling
- rscf/claim
- rscf/provenance
- rscf/state/derived
- topic/obsidian-linking
title: AMOS Obsidian — Linking Plugin Stack
type: reference
---
# AMOS Obsidian — Linking Plugin Stack

**Purpose:** Use Obsidian as the persistent brain surface for AMOS. This note configures the linking plugin stack and provides a starter Templater script so new notes are born already connected to the MOC network.

---

## Enabled community plugins

| Rank | Plugin ID | Display name | Purpose | Best for |
|------|-----------|--------------|---------|----------|
| 1 | `smart-connections` | Smart Connections | Semantic / AI related-note discovery | Intelligent suggestions |
| 2 | `autolink` | Autolink | Auto-convert matching text to `[[links]]` | Bulk cleanup of existing notes |
| 3 | `templater-obsidian` | Templater | JS-driven note creation with links | Full automation |
| 4 | `quickadd` | QuickAdd | One-shortcut capture + templater | Fast structured creation |
| 5 | `various-complements` | Various Complements | Faster `[[...]]` autocomplete | Manual linking speed |
| 6 | `obisidian-note-linker` | Note Linker | Suggest missed note-to-note links | Discovering missed connections |
| 7 | `dataview` | Dataview | Dynamic link lists / auto-MOCs | Auto-updating indexes |
| 8 | `copilot` | Copilot | AI writing assistant + link suggestions | Link insertion while writing |
| 9 | `knowledge-graph-analysis` | Knowledge Graph Analysis | Graph metrics and link insights | Understanding link topology |

### Combination to run
- **Smartest linking:** `smart-connections`
- **Bulk fix:** `autolink`
- **Max automation:** `templater-obsidian` + `quickadd`
- **Fast manual linking:** `various-complements`

---

## Core plugins used for linking

- **Backlink** (`backlink: true`) — shows who links to the current note.
- **Outgoing link** (`outgoing-link: true`) — surfaces unlinked mentions and notes to connect.
- **Graph** (`graph: true`) — global and local graph views for link topology.
- **Page preview** (`page-preview: true`) — hover previews of linked notes.

---

## Templater starter script: "linked-note"

Save as a template under `Templates/linked-note.md` (or any `tp.file.folder` you configure), then bind it to `QuickAdd` or a hotkey.

```markdown
---
created: "<% tp.date.now("YYYY-MM-DD") %>"
origin_architect: Trang Phan
type: note
status: draft
tags: [note, linkme]
provenance: MODEL
confidence: DERIVED
related:
  - "[[00 Cosmo Brain MOC]]"
  - "[[00-Home]]"
---

# <% tp.file.title %>

> Epistemic class: MODEL
> Confidence: DERIVED

## Purpose

## Links
- [[00 Cosmo Brain MOC]]
- [[00-Home]]

## Notes

```

**What it does:**
1. Sets standard AMOS provenance frontmatter.
2. Pre-links the note to the root MOC and the Cosmo Brain MOC.
3. Normalizes title from the new note name.

---


> **Template file:** [[Templates/linked-note.md|Templates/linked-note.md]] — save this as a Templater template and bind it to QuickAdd or a hotkey.
## Recommended first-run checklist

1. Install and enable the above community plugins from `Settings → Community plugins`.
2. Run **Smart Connections** once and let it build the local embedding index.
3. Run **Autolink** (or **Note Linker**) across a sample folder first to audit behavior before bulk-linking.
4. Configure **QuickAdd** to call the `linked-note` Templater template.
5. Use **Dataview** to add an auto-updating MOC query, e.g.:
   ```dataview
   TABLE file.mtime AS Updated, tags
   FROM #moc OR #canon-group/tech-ai
   SORT file.name ASC
   ```
6. Periodically run `Find orphaned files and broken links` to keep the graph clean.

---


> **Pre-configured:** Templater is already set to use the `Templates` folder (`.obsidian/plugins/templater-obsidian/data.json`).
## Related

- [[00 Cosmo Brain MOC]]
- [[00_ROOT_MOC]]
- [[00-Home]]
- [[AMOS_Layer_Maps]] — top-level AMOS layer map index
- [[11_KNOWLEDGE/11_KNOWLEDGE_MOC.md|11_KNOWLEDGE MOC]] — the knowledge layer index
- [[AMOS_Templates]] — AMOS template index
