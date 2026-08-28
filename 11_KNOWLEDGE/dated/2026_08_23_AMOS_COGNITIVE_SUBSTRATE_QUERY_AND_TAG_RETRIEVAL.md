---
title: AMOS Cognitive Substrate Query and Tag Retrieval
created: '2026-08-23'
origin: Hermes ↔ Cosmo Brain
origin_architect: Trang Phan
type: note
source: 11_KNOWLEDGE/dated
tags:
- cosmo
- amos
- canon-group/tech-ai
- rscf/claim
- rscf/state/observation
- topic/cognitive-substrate
- topic/memory-retrieval
- topic/query-filtering
- dated
- dated/2026-08-23
- canon/knowledge
status: verified
provenance: OBSERVATION
confidence: VERIFIED
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: temporal_log
---


# AMOS Cognitive Substrate Query and Tag Retrieval

> Epistemic class: OBSERVATION
> Conclusion label: `VERIFIED` — Added query() and retrieve_by_tag() methods with
> scope/epistemic filtering, MetaCognitiveEvent class, and 19 new self-tests.
> Cognitive substrate self-tests: 117 → 136 (all pass).
> Governing law: `integrity > completeness > fluency > speed > token savings`.

## What was done

Extended the unified `AMOS_COGNITIVE_SUBSTRATE.py` MemoryOperationGraph with
content-based query retrieval, tag-based retrieval, and a MetaCognitiveEvent
class for typed mode-transition events.

## New Methods

### 1. `query()` — Content-based query retrieval (gap 879)

```python
def query(self, query_terms: str, scope: Optional[Scope] = None,
          epistemic_class: Optional[EpistemicClass] = None,
          trust_states: Optional[Set[MemoryTrustState]] = None,
          limit: int = 10) -> List[MemoryObject]:
```

- Lexical match: splits query into terms, matches against content terms
- Filters by scope compatibility, epistemic class, and trust state
- Returns objects sorted by overlap score (descending)
- Only returns TRUSTED and PROVISIONAL objects by default

### 2. `retrieve_by_tag()` — Tag-based retrieval (gap 880)

```python
def retrieve_by_tag(self, tag: str, scope: Optional[Scope] = None,
                    epistemic_class: Optional[EpistemicClass] = None,
                    limit: int = 10) -> List[MemoryObject]:
```

- Finds objects with matching tag
- Filters by scope and epistemic class
- Excludes QUARANTINED, REVOKED, FALSIFIED objects
- Returns up to `limit` results

### 3. `MetaCognitiveEvent` — Typed mode-transition event (gap 778)

```python
@dataclass
class MetaCognitiveEvent:
    event_type: str
    source_mode: str = ""
    target_mode: str = ""
    reason: str = ""
    confidence: float = 0.5
    timestamp: float = field(default_factory=time.time)
```

Unlike `MetaCognitiveSnapshot` (which captures state), `MetaCognitiveEvent`
captures transitions. The `transition_mode()` method now appends a
`MetaCognitiveEvent` to the metacognitive history before taking a snapshot.

## Key Design Decisions

1. **Empty scope = universally compatible**: Objects with no scope set (all None
   fields) are compatible with any query scope. This is by design — empty scope
   means "applies everywhere". Only objects with explicit scope values are
   filtered by scope mismatch.

2. **Trust state filtering**: `query()` only returns TRUSTED and PROVISIONAL
   objects by default. QUARANTINED, REVOKED, FALSIFIED, and STALE objects are
   excluded unless explicitly requested via `trust_states` parameter.

3. **Lexical matching**: The query uses simple term overlap scoring. This is
   intentionally simple — the cognitive substrate is a mechanistic reasoning
   layer, not a search engine. Semantic matching would require embedding
   comparison which is a higher-level concern.

4. **MetaCognitiveEvent vs MetaCognitiveSnapshot**: Events capture transitions
   (what changed), snapshots capture state (what is). Both are stored in the
   same `metacognitive_history` list. The `load_state()` method handles both
   types by checking for the `event_type` field.

## Bug Fixes Applied

1. **`MetaCognitiveEvent` not defined**: The user's `transition_mode()` update
   referenced `MetaCognitiveEvent` which didn't exist. Created the dataclass.

2. **`metacognitive_history` type hint**: Changed from `List[MetaCognitiveSnapshot]`
   to `List[Any]` to accept both snapshots and events.

3. **`load_state()` KeyError**: The deserialization tried to access
   `hdata["uncertainty"]` which doesn't exist in event entries. Fixed to check
   for `event_type` field and deserialize accordingly.

## Test Results

| Suite | Before | After |
|-------|--------|-------|
| AMOS_COGNITIVE_SUBSTRATE.py self-tests | 117 | 136 (+19) |
| test_cognitive_substrate_reality_gate.py | 26 | 26 |
| test_cognitive_substrate_reasoning_graph.py | 29 | 29 |
| test_cognitive_substrate_memory_graph.py | 38 | 38 |
| test_cognitive_substrate_interface.py | 32 | 32 |
| **Total cognitive substrate** | **242** | **261 (+19)** |

## New Self-Tests Added (19)

1. `direct retrieve with matching scope succeeds`
2. `direct retrieve with mismatched scope returns None`
3. `direct retrieve with matching epistemic class succeeds`
4. `direct retrieve with mismatched epistemic class returns None`
5. `direct retrieve with both filters matching succeeds`
6. `direct retrieve with scope mismatch + epistemic match returns None`
7. `direct retrieve with no filters succeeds`
8. `direct retrieve of non-existent mid returns None`
9. `query returns results for matching content`
10. `query returns empty for non-matching content`
11. `query with epistemic filter returns results`
12. `query with non-matching epistemic filter returns empty`
13. `query with matching scope returns results`
14. `admitted object appears in query with matching scope`
15. `admitted object excluded from query with non-matching scope`
16. `retrieve_by_tag returns results for existing tag`
17. `retrieve_by_tag returns empty for non-existent tag`
18. `retrieve_by_tag with matching epistemic returns results`
19. `retrieve_by_tag with non-matching epistemic returns empty`

## Links

- [[00_COSMO_BRAIN_MOC]]
- 2026-08-23 AMOS Cognitive Substrate Bug Fixes
- 2026-08-22 Cognitive Substrate Memory Graph
- 2026-08-22 Cognitive Substrate Interface Coupling
- AMOS_Cognitive_Substrate_v2_Implementation_Notes

---
**MOC:** [[DATED_MOC]]
