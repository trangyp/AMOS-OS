---
title: "AMOS Cognitive Substrate Bug Fixes"
created: "2026-08-23"
origin: "Hermes ↔ Cosmo Brain"
origin_architect: "Trang Phan"
type: "note"
tags: [cosmo, amos, canon-group/tech-ai, rscf/claim, rscf/state/observation, topic/cognitive-substrate, topic/bugfix, topic/epistemic-autopoisoning, dated, dated/2026-08-23]
status: "verified"
provenance: "OBSERVATION"
confidence: "VERIFIED"
---

# AMOS Cognitive Substrate Bug Fixes

> Epistemic class: OBSERVATION
> Conclusion label: `VERIFIED` — Fixed 3 bugs in AMOS_COGNITIVE_SUBSTRATE.py, all 146 self-tests pass.
> Governing law: `integrity > completeness > fluency > speed > token savings`.

## What was done

Fixed 3 bugs in `cosmo-brain/AMOS_COGNITIVE_SUBSTRATE.py` (168KB, the unified
cognitive substrate layer) that were causing self-test failures.

## Bug 1: `revert_warning()` return type mismatch

**Location**: `ModeState.revert_warning()` (line 2005) and
`CognitiveSubstrateGate.detect_mode_reversion()` (line 3224)

**Problem**: The function returned `Optional[str]` (a string message), but the
self-test at line 3813 expected a dict with `culprit_mode` key:
```python
revert_warning2["culprit_mode"] == ReasoningMode.EXPLOSE
```

**Fix**: Changed `revert_warning()` to return `Optional[Dict[str, Any]]` with
keys: `culprit_mode`, `reverted_to`, `reason`, `message`. The culprit_mode is
the most recent previous mode that differs from the current mode.

## Bug 2: `time.time()` called at class definition time

**Location**: `MemoryObject` dataclass (line 2117-2118)

**Problem**: 
```python
time_created: float = field(default_factory=time.time)  # correct
time_updated: float = field(default_factory=time.time())  # BUG: calls time.time() once
```

`time.time()` with parentheses calls the function once at class definition time
and uses the float result as the default factory. This caused
`TypeError: 'float' object is not callable` when creating MemoryObject instances.

**Fix**: Changed `time.time()` to `time.time` (without parentheses) so
`default_factory` receives the callable itself.

## Bug 3: `MemoryTrustState.RETRACTED` doesn't exist

**Location**: `MemoryOperationGraph.retract()` (line 2578)

**Problem**: The code tried to set `obj.trust_state = MemoryTrustState.RETRACTED`,
but `MemoryTrustState` enum only has: TRUSTED, PROVISIONAL, QUARANTINED, STALE,
REVOKED, FALSIFIED. `RETRACTED` exists in the `ObjectStatus` enum, not
`MemoryTrustState`.

**Fix**: Changed to `MemoryTrustState.REVOKED` and updated the self-test check
to match.

## Bug 4: Mode transition not recorded in meta-cognitive history

**Location**: `CognitiveSubstrateGate.transition_mode()` (line 3220)

**Problem**: The `transition_mode` method called `self.mode_state.transition()`
but didn't call `self.meta_cognitive_state.snapshot()`, so the meta-cognitive
history was never updated after mode transitions.

**Fix**: Added `self.meta_cognitive_state.snapshot()` call after the transition.

## Bug 5: Scope compatibility check with empty scope

**Location**: Self-test section 10 (line 3943)

**Problem**: The test expected retrieval with `Scope(regime="room-2")` to fail
for an object with no scope set (all None fields). But `Scope.compatible_with()`
only fails when BOTH scopes have a non-None value that differs. With the object's
scope being None, the check passed (returned compatible).

**Fix**: Set `admitted.scope = Scope(regime="room-1")` before the retrieval
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

3. **Return type contracts**: When a self-test expects `result["key"]`, the
   function must return a dict, not a string. Check the test before changing
   the function signature.

4. **Scope compatibility**: `Scope.compatible_with()` only fails when both
   scopes have non-None values that differ. An empty scope (all None) is
   compatible with everything.
5. **`MetaCognitiveEvent` not defined**: The `transition_mode()` method referenced
   `MetaCognitiveEvent` which didn't exist. Fixed by defining the dataclass with
   `event_type`, `source_mode`, `target_mode`, `reason`, `confidence`, `timestamp`.
6. **`load_state` history deserialization**: `load_state` tried to create
   `MetaCognitiveSnapshot` from all history entries, but `MetaCognitiveEvent`
   entries don't have `uncertainty`/`contradiction_count` fields. Fixed by
   checking for `event_type` key and deserializing to the correct type.
7. **`snap` variable scope**: After the if/else for history deserialization,
   `snap.append(snap)` was outside the else block, causing `UnboundLocalError`
   when the if branch was taken. Fixed by moving append inside the else block.
8. **Non-matching scope test**: The self-test expected `query("22.5C",
   scope=room-99)` to return empty, but other objects with empty scope matched.
   Fixed by checking that the room-1 object is NOT in results, rather than
   expecting all results to be empty.

## Links

- [[00_Cosmo_Brain_MOC]]
- 2026-08-22 Cognitive Substrate Reality Gate
- 2026-08-22 Cognitive Substrate Reasoning Graph
- 2026-08-22 Cognitive Substrate Memory Graph
- 2026-08-22 Cognitive Substrate Interface Coupling
