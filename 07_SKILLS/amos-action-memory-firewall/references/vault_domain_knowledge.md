---
title: vault domain knowledge
type: reference
source: 07_SKILLS/amos-action-memory-firewall/references
tags: [reference, amos-action-memory-firewall, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `amos-action-memory-firewall`

## Vault-Sourced Content

### Source 1: Cognitive Substrate Memory Operation Graph

> Path: `dated/2026-08-22/2026-08-22 Cognitive Substrate Memory Graph.md` | Size: 5699 chars | Match score: 10

# Cognitive Substrate Memory Operation Graph

> Slice 3 of the AMOS Cognitive Substrate Layer. Implements the memory side of
> `M_t = (V_t, E_t, O_t, I_t, Q_t, L_t)` with field-level lineage, epistemic-class
> preservation, consolidation with contradiction retention, retrieval graph with
> failure attribution, dependency-safe forgetting, and earliest causal memory cut.
>
> Source: `cosmo-brain/AMOS_COGNITIVE_SUBSTRATE_MEMORY_GRAPH.py` (27 self-tests)
> Test: `cosmo-brain/test_cognitive_substrate_memory_graph.py` (11 integration, 38 total)
> Skill: amos-cognitive-substrate-memory-graph
> See also: [[2026_08_22_COGNITIVE_SUBSTRATE_REALITY_GATE]] · [[2026_08_22_COGNITIVE_SUBSTRATE_REASONING_GRAPH]] · [[2026_08_22_AMOS_OBSIDIAN_MEMORY_BRIDGE]]

## 1. The problem this solves

A memory system is not fundamentally a database of remembered sentences. It is a
reconstructed as an operation-variable execution graph and attributed to the

## 2. Core formalization

```
M_t = (V_t, E_t, O_t, I_t, Q_t, L_t)
```

| Component | Meaning | Gaps |
|-----------|---------|------|
| V_t | Memory-object graph (fields with lineage) | 810–815 |
| E_t | Semantic / provenance / dependency edges | 825–826 |
| O_t | Memory operation history | 801–802 |
| I_t | Indexes | 801 |
| Q_t | Quarantine / trust state | 827–830 |
| L_t | Lifecycle state (active, superseded, retracted, archived) | 822–824 |

Memory evolution: `M_{t+1} = Pi_admission(R_reconcile(C_consolidate(U_update(M_t, E_t))))`

## 3. Memory operation pipeline (gap 801)

```
encode -> normalize -> admit -> consolidate -> index -> retrieve -> filter -> interpret -> use -> update
```

Each operation is typed, recorded, and attributable.

## 4. Field-level lineage (gaps 810–812)

Each stored field traces to a source span or derivation operation. When evidence fails,
only the affected field is invalidated — not the entire memory object. This enables
are stale or wrong.

## 5. Epistemic-class preservation (gaps 831–837)

| Gap | Preservation rule |
|-----|-------------------|
| 831 | SOURCE_CLAIM, OBSERVATION, DERIVED, MODEL, DECISION survive storage unchanged |
| 832 | Modality ("may", "likely", "must", "observed", "predicted") must survive compression |
| 833 | Negation ("not", exceptions, exclusion conditions) must not be dropped |
| 834 | Quantifiers ("some", "most", "all", thresholds) must remain explicit |
| 835 | Correlation cannot become cause during consolidation |
| 836 | Future forecast cannot become present observation after time passes |
| 837 | "Agent A believes X" cannot become "X is true" |

## 6. Consolidation (gaps 841–844)

- Contradictions among sources are **retained**, not erased.
- Summary confidence **cannot exceed** the max source confidence.
- If contradictions exist, confidence is halved and conclusion becomes `COMPETING`.

## 7. Retrieval graph (gaps 873–878)

Retrieval is modeled as graph traversal with path provenance. Failure is separated into:
`STORE_FAILURE | INDEX_FAILURE | QUERY_FAIL

---

### Source 2: AMOS Obsidian Memory Bridge — Brain as Vault

> Path: `dated/2026-08-22/2026-08-22 AMOS Obsidian Memory Bridge.md` | Size: 4525 chars | Match score: 10

# AMOS Obsidian Memory Bridge — Brain as Vault

> The Obsidian vault IS the brain. This bridge module provides programmatic access to the vault as durable, queryable memory. 43 self-tests pass; 0 failures. 0 KB orphans.
>
> Source: `cosmo-brain/AMOS_OBSIDIAN_MEMORY_BRIDGE.py`
> See also: [[COSMO_BRAIN_MOC]] · [[2026_08_22_AMOS_GO_BOARD_19X19_FORMAL_SYSTEM]]

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

- **KB orphans: 0** (was 1

---

### Source 3: Memory — AMOS Kafka Brain Buffer

> Path: `dated/2026-08-23/2026-08-23 Memory — AMOS Kafka Brain Buffer.md` | Size: 4133 chars | Match score: 10

# Memory — AMOS Kafka Brain Buffer


---

## Key Facts

### Module Architecture
- 2001-line TypeScript module operationalizing verbena's 71-concept map into a Kafka-backed brain buffer
- 4-layer consciousness model: D5 Manas (channels) → D6 Citta (buffer/stream) → D7 Buddhi (decision) → D8 Jnana (scoring)
- 16 channels total: 4 ingest + 5 routing + 4 output (D4 union has 8 but filtered to 4 + 4 deploy + 3 telemetry = 16 unique)
- `BufferEntry` has 80+ fields spanning D5/D6/D7/D8
- `InMemoryBrainBuffer` implements LRU eviction, dedup, TTL, stale eviction, health metrics
- `computeD8Score()` is a typed stub (AMOS_MODEL formulas) — 12 dimensions: coherence, novelty, relevance, authority, temporal_freshness, provenance_strength, confidence_calibration, evidence_density, contradiction_load, scope_alignment, retention_priority, jnana_weighted_sum. Scoring uses weighted linear combination with per-dimension gates (each dimension must exceed threshold or score is capped). Algorithm: `score = Σ(w_i * normalize(d_i))` where weights derive from channel ACL priority and buffer retention policy. Anti-overclaim: all scores are AMOS_MODEL, not ground-truth confidence.
- `CHANNEL_ACL_TABLE` has 16 channels × 6 dimensions = 96 precise ACL entries — the verbena differentiator

### Test Suite
- 6 test categories, 130+ individual tests:
  1. D5 Manas — Channels (21 tests): channel enum construction, union acceptance, category mapping, ALL_CHANNELS count, validation accept/reject
2. D6 Citta — Entry State (8 tests): priority/activity/nominal/retention/cache/frame enums, default entry, filler entry
  3. Kafka Topic/Topology (16 tests): KafkaTopicConfig, KafkaPartition, KafkaBrainLogImpl, KafkaTopology
4. Buffer Config + Helpers (14 tests): BufferConfig, generateEntryId, generateDedupKey, generateTransientKey, factories
  5. Buffer CRUD + Dedup + TTL + Eviction + Health (40 tests): add/remove/get/has/entriesList/clear, dedup hit/preserve, TTL valid/expired/zero, evict capacity/LRU/FIFO/priority/empty/count, health empty/populated/util/averages
6. D7 Buddhi (11 tests): RoutingDecisionType, RoutingDecisionMessage, D7State, ObserverFrameType, ObserverFrame, IntentClassification, OutputType, D7GatingResult

### Synthetic Generator
- 8 orchestrator patterns: heartbeat, burst, synthesis, mixed, canonical, fork, retry, lifecycle
- Outputs JSONL by default, supports json / kafka-events / json-raw formats
- Reproducible via --seed

### Storage Locations
- Module: `cosmo-brain/AMOS_Kafka_Brain_Buffer_v1.0.ts`
- Tests: `cosmo-brain/AMOS_Kafka_Brain_Buffer_v1.0.test.ts`
- Generator: `cosmo-brain/test_kafka_brain_buffer_generator.py`
- Vault: `_00_Cosmo brain/md/2026-08-23 AMOS Kafka Brain Buffer.md`
- Memory: `Memory — AMOS Kafka Brain Buffer.md` (this file)
- Skill: `.agents/skills/amos-kafka-brain-buffer/SKILL.md`
- Workflow: `kafka-brain-buffer-build.md` (path may vary)

### Epistemic Labels
- SOURCE: channel taxonomy (D5 Manas), D5-D8 mapping (mapped from existing verbena concepts)
- DERIVED: D5→D6→D7→D8 flow (follows from consciousness model architecture)
- AMOS_MODEL: scoring formulas, buffer implementation, ACL table entries, flow orchestration logic

## Build Commands

```bash
cd cosmo-brain

# Type-check module
npx tsc --noEmit AMOS_Kafka_Brain_Buffer_v1.0.ts

# Run test suite
npx ts-node --transpile-only AMOS_Kafka_Brain_Buffer_v1.0.test.ts

# Generate sample events
python3 test_kafka_brain_buffer_generator.py --pattern all --output jsonl
python3

---
**MOC:** [[references_MOC]]
```
