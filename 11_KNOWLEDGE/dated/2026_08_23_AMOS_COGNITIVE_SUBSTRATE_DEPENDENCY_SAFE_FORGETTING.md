---
title: "AMOS Cognitive Substrate Dependency-Safe Forgetting"
created: "2026-08-23"
origin: "Hermes ↔ Cosmo Brain"
origin_architect: "Trang Phan"
type: note
tags: [cosmo, amos, canon-group/tech-ai, rscf/claim, rscf/state/observation, topic/cognitive-substrate, topic/forgetting, topic/dependency-analysis, topic/memory-stats, dated, dated/2026-08-23]
status: "verified"
provenance: "OBSERVATION"
confidence: "VERIFIED"
---


# AMOS Cognitive Substrate Dependency-Safe Forgetting

> Epistemic class: OBSERVATION
> Conclusion label: `VERIFIED` — Added get_dependents(), dependency_safe_forget(),
> get_memory_stats(), and 10 new self-tests. Cognitive substrate self-tests: 136 → 146.
> Governing law: `integrity > completeness > fluency > speed > token savings`.

## What was done

Extended the unified `AMOS_COGNITIVE_SUBSTRATE.py` MemoryOperationGraph with
dependency analysis, dependency-safe forgetting, and memory statistics
introspection. Also fixed a duplicate `self.mode_state` initialization.

## New Methods

### 1. `get_dependents(mid)` — Dependency analysis (gap 892)

```python
def get_dependents(self, mid: str) -> List[str]:
```

Finds all objects that depend on the given object. An object B depends on A if:
- A appears in B's `evidence`, `proof`, or `links` lists
- B was composed, decomposed, or branched from A (checked via operation history)

Returns a list of dependent object MIDs.

### 2. `dependency_safe_forget(mid, reason)` — Safe forgetting (gaps 891-893)

```python
def dependency_safe_forget(self, mid: str, reason: str = "dependency-safe forget")
    -> Tuple[bool, str, List[str]]:
```

Checks if any other objects depend on this one before evicting. If dependents
exist, returns `(False, reason, blocked_by_list)`. If no dependents, archives
then evicts the object, returns `(True, "forgotten", [])`.

This implements the gap 891-893 requirement that forgetting must be
dependency-safe — you cannot forget an object that other objects depend on
without first handling those dependencies.

### 3. `get_memory_stats()` — Memory introspection

```python
def get_memory_stats(self) -> Dict[str, Any]:
```

Returns statistics about the memory graph:
- `total_objects`: Number of objects in the graph
- `total_operations`: Total operation records across all objects
- `trust_state_distribution`: Count of objects per trust state
- `epistemic_class_distribution`: Count of objects per epistemic class
- `operations_recorded`: Total operations in the operation log

## Bug Fix

### Duplicate `self.mode_state` initialization

The `CognitiveIntegrityGate.__init__()` had `self.mode_state = ReasoningModeState()`
on two consecutive lines (lines 2889-2890). Removed the duplicate.

## Test Results

| Suite | Before | After |
|-------|--------|-------|
| AMOS_COGNITIVE_SUBSTRATE.py self-tests | 136 | 146 (+10) |
| test_cognitive_substrate_reality_gate.py | 26 | 26 |
| test_cognitive_substrate_reasoning_graph.py | 29 | 29 |
| test_cognitive_substrate_memory_graph.py | 38 | 38 |
| test_cognitive_substrate_interface.py | 32 | 32 |
| **Total cognitive substrate** | **261** | **271 (+10)** |

## New Self-Tests Added (10)

1. `get_dependents returns empty for standalone object`
2. `get_dependents finds decomposed children`
3. `dependency_safe_forget fails for object with dependents`
4. `dependency_safe_forget returns blocked_by list`
5. `dependency_safe_forget succeeds for standalone object`
6. `dependency_safe_forget returns empty blocked_by for standalone`
7. `memory stats has total_objects`
8. `memory stats has total_operations`
9. `memory stats has trust_state_distribution`
10. `memory stats has epistemic_class_distribution`

## Key Design Decisions

1. **Dependency detection via multiple channels**: Dependencies are detected
   through evidence/proof/links lists AND through operation history (compose,
   decompose, branch operations). This ensures all dependency types are caught.

2. **Archive before evict**: `dependency_safe_forget` archives the object
   first (preserving it in the archive) before evicting. This follows the
   pattern: archive → evict, not just delete. The object can be resurrected
   from the archive if needed.

3. **Non-destructive stats**: `get_memory_stats` is read-only and doesn't
   modify any state. It's safe to call at any time for monitoring.

## Links

- [[00_COSMO_BRAIN_MOC]]
- 2026-08-23 AMOS Cognitive Substrate Query and Tag Retrieval
- 2026-08-23 AMOS Cognitive Substrate Bug Fixes
- 2026-08-22 Cognitive Substrate Memory Graph
- AMOS_Cognitive_Substrate_v2_Implementation_Notes

---
**MOC:** [[DATED_MOC]]
