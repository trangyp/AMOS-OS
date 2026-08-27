---
title: 2026 08 22 OBSIDIAN AS COSMO BRAIN OPERATING MANUAL
type: manual
source: 11_KNOWLEDGE/dated
origin_architect: Trang Phan
provenance: amos-obsidian-vault-config skill + cosmo-obsidian-memory skill + AMOS_OBSIDIAN_MEMORY_BRIDGE.py implementation
confidence: 0.95
epistemic_class: SOURCE_DERIVED
conclusion_label: VERIFIED_PRESENT
tags: [canon-group/human-system, canon/narrative, rscf/claim, rscf/provenance, rscf/state/observation, topic/2026-08-22-obsidian-as-cosmo-brain-opera, dated, dated/2026-08-22]
date: 2026-08-22
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: temporal_log
---


# Obsidian as Cosmo Brain — Operating Manual

> The Obsidian vault is the durable brain substrate for the AMOS/Cosmo system. Runtime cognition lives in the executable brain model; persistent knowledge, decisions, and provenance live in the user’s own Obsidian knowledge graph.
>
> Source: `cosmo-brain/AMOS_OBSIDIAN_MEMORY_BRIDGE.py` · `scripts/obsidian-health-check.sh`
> See also: cosmo-obsidian-memory · 2026-08-22 19x19 AI Cognitive Field · 2026-08-22 AMOS Go Board 19x19 Formal System

## 1. Vault layout

| Location | Purpose |
|----------|---------|
| `_00_Cosmo brain/md/*.md` | Durable knowledge notes |
| `daily/<YYYY-MM-DD>.md` | Dated decisions and actions |
| `_00_Cosmo brain/md/00_Cosmo_Brain_MOC.md` | Master map of content |
| `.obsidian/` | Vault configuration, graph, hotkeys, bookmarks |
| `scripts/obsidian-health-check.sh` | 100+ structural checks |

## 2. Health check

```bash
cd /Users/mac/Downloads/stitch_project_cosmo
sh scripts/obsidian-health-check.sh
```

Checks: config files, CSS snippets, templates, graph presets, MOCs, canvases, reference docs, daily notes, knowledge base, `.gitignore`.

## 3. Python bridge

`cosmo-brain/AMOS_OBSIDIAN_MEMORY_BRIDGE.py`

```python
from AMOS_OBSIDIAN_MEMORY_BRIDGE import ObsidianBrain

brain = ObsidianBrain()

# Read a note
note = brain.get("00 Cosmo Brain MOC")
print(note.frontmatter, note.wikilinks)

# Search by title or tag
hits = brain.find(title="19x19")
tagged = brain.notes_by_tag("ai-cognition")

# Tag index and related notes
idx = brain.tag_index()
related = brain.related_notes("19×19 AI Cognitive Field", depth=1)

# Create a note
path = brain.create_note(
    "New Memory",
    "# New Memory\n\n[[00_COSMO_BRAIN_MOC]]",
    {"epistemic_class": "MODEL", "tags": ["memory"]}
)

# Update MOC and daily
brain.append_to_moc("New Memory")
brain.append_daily("Created New Memory")
```

## 4. Note conventions

### Frontmatter

```yaml
---
origin_architect: Trang Phan
provenance: <source>
confidence: 0.92
eplistemic_class: SOURCE | DERIVED | MODEL | UNKNOWN
tags: [memory, tag]
date: 2026-08-22
---
```

### Epistemic classes

| Class | Meaning |
|-------|---------|
| `SOURCE` | Directly from an AMOS/Trang source |
| `DERIVED` | Follows from source + geometry/relations |
| `MODEL` | New formal machinery to make things executable |
| `UNKNOWN` | Gap or pending evidence |

### Wikilinks

Use `Note Title` to connect notes. The MOC should never be an island.

## 5. Workflow

1. **Test** — run health check before and after changes.
2. **Store** — write a note with frontmatter and wikilinks.
3. **Link** — add the note to `00_Cosmo_Brain_MOC.md` in the relevant section.
4. **Log** — add a one-line entry to `daily/<YYYY-MM-DD>.md`.
5. **Verify** — run `AMOS_OBSIDIAN_MEMORY_BRIDGE.py` self-test.

## 6. Conclusion class

This manual and the bridge are `AMOS MODEL / DERIVED`. The layout and config are derived from the existing vault; the bridge is new executable formalization.

---
**MOC:** [[DATED_MOC]]
