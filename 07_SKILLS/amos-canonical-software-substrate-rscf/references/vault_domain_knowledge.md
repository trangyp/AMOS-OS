---
title: Vault Domain Knowledge — Amos Canonical Software Substrate Rscf
type: reference
source: 07_SKILLS/amos-canonical-software-substrate-rscf/references
tags:
- reference
- amos-canonical-software-substrate-rscf
- type/skill
- 2026-08-22-amos-obsidian-memory-bridge
- references-moc
- 00-home
- amos-rscf-nodes
- law-hierarchy
- 2026-08-22-cognitive-substrate-reality-gate
- 2026-08-22-cognitive-substrate-reasoning-graph
- 07-skills-moc
- trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `amos-canonical-software-substrate-rscf`

## Vault-Sourced Content

### Source 1: AMOS Cognitive Substrate Bug Fixes

> Path: `dated/2026-08-23/2026-08-23 AMOS Cognitive Substrate Bug Fixes.md` | Size: 5985 chars | Match score: 10

# AMOS Cognitive Substrate Bug Fixes

> Epistemic class: OBSERVATION
> Conclusion label: `VERIFIED` — Fixed 3 bugs in AMOS_COGNITIVE_SUBSTRATE.py, all 146 self-tests pass.
> Governing law: `integrity > completeness > fluency > speed > token savings`.

## What was done (2)

Fixed 3 bugs in `cosmo-brain/AMOS_COGNITIVE_SUBSTRATE.py` (168KB, the unified
cognitive substrate layer) that were causing self-test failures.

## Bug 1: `revert_warning()` return type mismatch

`CognitiveSubstrateGate.detect_mode_reversion()` (line 3224)

self-test at line 3813 expected a dict with `culprit_mode` key:
```python
revert_warning2["culprit_mode"] == ReasoningMode.EXPLOSE
```

keys: `culprit_mode`, `reverted_to`, `reason`, `message`. The culprit_mode is
the most recent previous mode that differs from the current mode.

## Bug 2: `time.time()` called at class definition time


```python
time_created: float = field(default_factory=time.time)  # correct
time_updated: float = field(default_factory=time.time())  # BUG: calls time.time() once
```

`time.time()` with parentheses calls the function once at class definition time
and uses the float result as the default factory. This caused
`TypeError: 'float' object is not callable` when creating MemoryObject instances.

`default_factory` receives the callable itself.

## Bug 3: `MemoryTrustState.RETRACTED` doesn't exist


but `MemoryTrustState` enum only has: TRUSTED, PROVISIONAL, QUARANTINED, STALE,
REVOKED, FALSIFIED. `RETRACTED` exists in the `ObjectStatus` enum, not
`MemoryTrustState`.

to match.

## Bug 4: Mode transition not recorded in meta-cognitive history


but didn't call `self.meta_cognitive_state.snapshot()`, so the meta-cognitive
history was never updated after mode transitions.


## Bug 5: Scope compatibility check with empty scope


for an object with no scope set (all None fields). But `Scope.compatible_with()`
only fails when BOTH scopes have a non-None value that differs. With the object's
scope being None, the check passed (returned compatible).

tests so the scope compatibility check has a real value to compare against.

## Test Results

| Suite | Before | After |
|-------|--------|-------|
| AMOS_COGNITIVE_SUBSTRATE.py self-tests | 123/125 (crash) | 146/146 |
| test_cognitive_substrate_reality_gate.py | 26 | 26 |
| test_cognitive_substrate_reasoning_graph.py | 29 | 29 |
| test_cognitive_substrate_memory_graph.py | 38 | 38 |
| test_cognitive_substrate_interface.py | 32 | 32 |
| **Total cognitive substrate** | **240** | **271** |

## Key Lessons

1. **`default_factory=time.time()` vs `time.time`**: The first calls the function
   once at definition time; the second passes the callable. Always use
   `field(default_factory=time.time)` for dataclass timestamp fields.

2. **Enum membership**: Before using `EnumClass.MEMBER`, verify the member exists
   in that specific enum class. `RETRACTED` was in `ObjectStatus`, not
   `MemoryTrustState`.

3. **Return type contracts**: When a self-test expects `result["key"

---

### Source 2: AMOS Cognitive Substrate Query and Tag Retrieval

> Path: `dated/2026-08-23/2026-08-23 AMOS Cognitive Substrate Query and Tag Retrieval.md` | Size: 5905 chars | Match score: 10

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
   (w

---

### Source 3: Cognitive Substrate Memory Operation Graph

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
> See also: 2026_08_22_COGNITIVE_SUBSTRATE_REALITY_GATE · 2026_08_22_COGNITIVE_SUBSTRATE_REASONING_GRAPH · 2026_08_22_AMOS_OBSIDIAN_MEMORY_BRIDGE

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
**MOC:** references_MOC
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-canonical-software-substrate-rscf-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-canonical-software-substrate-rscf/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
