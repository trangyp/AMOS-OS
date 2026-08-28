---
title: 2026 08 22 AMOS OBSIDIAN MEMORY BRIDGE
type: memory
source: 11_KNOWLEDGE/dated
origin_architect: Trang Phan
provenance: cosmo-brain/AMOS_OBSIDIAN_MEMORY_BRIDGE.py
confidence: 0.95
epistemic_class: SOURCE_DERIVED
conclusion_label: "VERIFIED_PRESENT"
tags:
- canon-group/tech-ai
- cosmo-brain
- memory-bridge
- obsidian
- persistence
- rscf/state/observation
- canon/os-module
- rscf/claim
- rscf/provenance
- topic/2026-08-22-amos-obsidian-memory-bridge
- dated
- dated/2026-08-22
date: 2026-08-22
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: temporal_log
---


# AMOS Obsidian Memory Bridge — Brain as Vault

> The Obsidian vault IS the brain. This bridge module provides programmatic access to the vault as durable, queryable memory. 43 self-tests pass; 0 failures. 0 KB orphans.
>
> Source: `cosmo-brain/AMOS_OBSIDIAN_MEMORY_BRIDGE.py`
> See also: [[00_COSMO_BRAIN_MOC]] · 2026-08-22 AMOS Go Board 19x19 Formal System

## 1. Architecture

```
ObsidianBrain (class)
├── all_notes() → Iterator[VaultNote]
├── find(title, tag) → List[VaultNote]
├── get(title) → Optional[VaultNote]
├── tag_index() → Dict[str, List[str]]
├── notes_by_tag(tag) → List[VaultNote]
├── related_notes(title, depth) → Dict[str, List[str]]
├── create_note(title, body, frontmatter) → VaultNote
├── append_to_moc(wikilink) → bool
├── append_daily(line) → Path
├── health_check() → Dict[str, Any]
├── backlink_graph(title, depth) → Dict[str, List[str]]
├── orphan_notes() → List[str]              [file-based resolution]
├── tag_statistics() → Dict[str, Any]
├── vault_summary() → Dict[str, Any]
├── search_notes(query, limit) → List[Dict]
├── recent_notes(limit) → List[Dict]
├── knowledge_frontier(min, max, limit) → List[Dict]
└── tag_cloud(min_count, limit) → List[Dict]
```

## 2. VaultNote model

```python
@dataclass
class VaultNote:
    path: Path
    title: str
    frontmatter: Dict[str, Any]
    body: str
    wikilinks: List[str]
```

- Title: first H1 or filename (separator lines `===`/`---`/`***` skipped)
- Frontmatter: YAML between `---` markers
- Wikilinks: all `target` and `alias` patterns

## 3. Orphan detection (file-based)

The `orphan_notes()` method uses **file-based resolution**:
1. Build `basename → set of filepaths` index
2. Build `relpath_noext → filepath` index
3. For each note, resolve wikilinks to filepaths via both indexes
4. A note is orphan if it has 0 outgoing AND 0 incoming resolved links

This matches the external file-based audit script exactly. Both report **0 KB orphans**.

## 4. Brain introspection methods

| Method | Returns | Purpose |
|--------|---------|---------|
| `vault_summary()` | dict | MOC exists, total notes/tags, orphan count, graph connected, top tags |
| `tag_statistics()` | dict | Total tags, top 10, singleton count, avg notes per tag |
| `tag_cloud(min_count)` | list | Tag frequency cloud filtered by minimum note count |
| `recent_notes(limit)` | list | Recently modified notes sorted by file mtime |
| `knowledge_frontier(min, max)` | list | Weakly-connected notes that need more links |
| `search_notes(query)` | list | Text search across all notes with snippets |

## 5. Test results

| Suite | Tests | Status |
|-------|-------|--------|
| `AMOS_OBSIDIAN_MEMORY_BRIDGE.py` self-test | 43 | PASS |
| MURK Engine | 10 | PASS |
| Brain Integration | 9 | PASS |
| MURK Comprehensive | 110 | PASS |
| Go Board self-test | 226 | PASS |
| Go Board comprehensive | 190 | PASS |
| MURK↔GoBoard integration | 251 | PASS |
| **Grand total** | **839** | **PASS** |

## 6. Vault graph health

- **KB orphans: 0** (was 1108 before MOC connectors)
- **Bridge orphans: 0**
- **RSCF MOC orphans: 0**
- **1399 KB files all connected to graph**
- **134 RSCF MOCs all have incoming links**
- Tags migrated to RSCF structural taxonomy (canon-group, rscf/, topic/)

## 7. Self-test categories

| Category | Tests | What it checks |
|----------|-------|----------------|
| B1-B2 | 3 | Health check, MOC loading |
| B3-B4 | 3 | 19x19 notes exist, AI cognitive note |
| B5-B7 | 3 | MOC graph, tag index |
| B8-B9 | 2 | Notes by tag, related notes |
| B6 (temp) | 3 | Create note, readback, MOC append |
| B10 | 2 | Orphan detection (file-based) |
| B11 | 4 | Tag statistics |
| B12 | 5 | Vault summary |
| B13 | 3 | Search notes |
| B14 | 4 | Recent notes |
| B15 | 3 | Knowledge frontier |
| B16 | 4 | Tag cloud |
| B17 | 3 | Vault summary with MOC + graph |
| **Total** | **43** | **All pass** |

## 8. Conclusion class

`AMOS MODEL / DERIVED`. The bridge provides deterministic, file-based access to the Obsidian vault as brain memory. Orphan detection, tag statistics, and search are executable formalizations of vault health metrics.

---
**MOC:** [[DATED_MOC]]
