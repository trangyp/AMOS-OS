---
title: "AMOS Brain Cortex and Executable Brain Model Bug Fixes"
created: "2026-08-23"
origin: "Hermes ↔ Cosmo Brain"
origin_architect: "Trang Phan"
type: "note"
tags: [cosmo, amos, canon-group/tech-ai, rscf/claim, rscf/state/observation, topic/bugfix, topic/brain-cortex, topic/executable-brain-model, dated, dated/2026-08-23]
status: "verified"
provenance: "OBSERVATION"
confidence: "VERIFIED"
---

# AMOS Brain Cortex and Executable Brain Model Bug Fixes

> Epistemic class: OBSERVATION
> Conclusion label: `VERIFIED` — Fixed 3 bugs across BrainCortex and ExecutableBrainModel.
> Governing law: `integrity > completeness > fluency > speed > token savings`.

## What was done

Fixed 3 bugs in `cosmo-brain/AMOS_BrainCortex.py` and `cosmo-brain/executable_brain_model.py`
that were causing self-test failures and runtime crashes.

## Bug 1: FailureMemoryLayer state leakage between tests

**Location**: `AMOS_BrainCortex.py` self-test [18] (line 470)

**Problem**: The `FailureMemoryLayer` has internal state (`_failures`, `_total_attempts`)
that persists across calls. Test [17] called `process()` once, incrementing `_failures` to 1.
Then test [18] used the same `cortex` object, so after 5 more calls, `_failures` = 1 + 5 = 6,
not the expected 5.

**Fix**: Reset `cortex.failure_memory = FailureMemoryLayer()` before test [18] to get
a clean failure count.

**Key lesson**: Layers with internal state (FailureMemoryLayer, RollbackRecoveryLayer) must
be reset between tests that check absolute counts. The `cortex` object is shared across
test cases in the self-test function.

## Bug 2: RollbackRecoveryLayer not snapshotted during run()

**Location**: `AMOS_BrainCortex.run()` (line 150-153)

**Problem**: The `run()` method called `self.snapshot()` (on BrainCortex's `_snapshots`)
but not `self.rollback.snapshot()` (on RollbackRecoveryLayer's `_snapshots`). The test
pre-seeded `cortex.rollback._snapshots` with 1 entry, but `run()` didn't add to it,
so `rollback_available` remained False (requires >= 2 snapshots).

**Fix**: Added `self.rollback.snapshot(snap)` call alongside `self.snapshot(snap)` in
the committed branch of `run()`.

**Key lesson**: When a BrainCortex has both its own `_snapshots` list and a
`RollbackRecoveryLayer` with its own `_snapshots`, both must be populated during `run()`.
The `rollback_available` flag depends on the RollbackRecoveryLayer's snapshot count.

## Bug 3: RSCFFormalLayer defined after entry point

**Location**: `executable_brain_model.py` — `RSCFFormalLayer` at line 6583, entry point at line 6512

**Problem**: The `if __name__ == "__main__"` block at line 6512 tried to instantiate
`ExecutableBrainModel()`, whose `__init__` references `RSCFFormalLayer`. But
`RSCFFormalLayer` was defined at line 6583, after the entry point. Since Python
executes top-to-bottom, the class wasn't defined yet when the entry point ran.

**Fix**: Moved the `if __name__ == "__main__"` block to after the `RSCFFormalLayer`
class definition (end of file).

**Key lesson**: In Python, `if __name__ == "__main__"` blocks are executed top-to-bottom
like any other code. If a class is defined later in the file, it won't be available
when the entry point runs. Always place entry points after all class definitions,
or use a `main()` function called at the end.

## Test Results

| Suite | Before | After |
|-------|--------|-------|
| AMOS_BrainCortex.py self-tests | 69/71 (2 failed) | 71/71 |
| executable_brain_model.py | Crash (NameError) | Runs successfully |
| test_brain_model_determinism.py | 13/13 | 13/13 |
| test_deterministic_improvements.py | 28/28 | 28/28 |

## Links

- [[00_COSMO_BRAIN_MOC]]
- 2026-08-23 AMOS Cognitive Substrate Bug Fixes
- 2026-08-23 Deterministic Verification Summary

---
**MOC:** [[DATED_MOC]]
