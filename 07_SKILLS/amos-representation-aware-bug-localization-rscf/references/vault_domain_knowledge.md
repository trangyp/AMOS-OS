---
title: Vault Domain Knowledge — Amos Representation Aware Bug Localization Rscf
type: reference
source: 07_SKILLS/amos-representation-aware-bug-localization-rscf/references
tags:
- reference
- amos-representation-aware-bug-localization-rscf
- canon/skill
- cosmo-brain-moc
- references-moc
- 00-home
- amos-rscf-nodes
- law-hierarchy
- 2026-08-23-amos-cognitive-substrate-bug-fixes
- 2026-08-23-deterministic-verification-summary
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
> Extracted from skill: `amos-representation-aware-bug-localization-rscf`

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

## Test Results (2)

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

### Source 2: AMOS Brain Cortex and Executable Brain Model Bug Fixes

> Path: `dated/2026-08-23/2026-08-23 AMOS Brain Cortex and Executable Brain Model Bug Fixes.md` | Size: 3746 chars | Match score: 10

# AMOS Brain Cortex and Executable Brain Model Bug Fixes

> Epistemic class: OBSERVATION
> Conclusion label: `VERIFIED` — Fixed 3 bugs across BrainCortex and ExecutableBrainModel.
> Governing law: `integrity > completeness > fluency > speed > token savings`.

## What was done

Fixed 3 bugs in `cosmo-brain/AMOS_BrainCortex.py` and `cosmo-brain/executable_brain_model.py`
that were causing self-test failures and runtime crashes.

## Bug 1: FailureMemoryLayer state leakage between tests


that persists across calls. Test [17] called `process()` once, incrementing `_failures` to 1.
Then test [18] used the same `cortex` object, so after 5 more calls, `_failures` = 1 + 5 = 6,
not the expected 5.

a clean failure count.

be reset between tests that check absolute counts. The `cortex` object is shared across
test cases in the self-test function.

## Bug 2: RollbackRecoveryLayer not snapshotted during run()


but not `self.rollback.snapshot()` (on RollbackRecoveryLayer's `_snapshots`). The test
pre-seeded `cortex.rollback._snapshots` with 1 entry, but `run()` didn't add to it,
so `rollback_available` remained False (requires >= 2 snapshots).

the committed branch of `run()`.

`RollbackRecoveryLayer` with its own `_snapshots`, both must be populated during `run()`.
The `rollback_available` flag depends on the RollbackRecoveryLayer's snapshot count.

## Bug 3: RSCFFormalLayer defined after entry point


`ExecutableBrainModel()`, whose `__init__` references `RSCFFormalLayer`. But
`RSCFFormalLayer` was defined at line 6583, after the entry point. Since Python
executes top-to-bottom, the class wasn't defined yet when the entry point ran.

class definition (end of file).

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

- [[COSMO_BRAIN_MOC]]
- [[2026_08_23_AMOS_COGNITIVE_SUBSTRATE_BUG_FIXES]]
- [[2026_08_23_DETERMINISTIC_VERIFICATION_SUMMARY]]

---

### Source 3: Coding_MAX

> Path: `tech-coding/Coding_MAX.md` | Size: 36864 chars | Match score: 5

{
  "meta": {
    "name": "AMOS Coding Engine",
    "version": "1.0.0",
    "description": "Unified AMOS coding kernel + execution engine for world‑class software design, implementation, refactor, and audit.",
    "tags": [
      "coding",
      "kernel",
      "engine",
      "architecture",
      "refactor",
      "testing",
      "deterministic"
    ]
  },
  "kernel": {
    "description": "Unified Coding Engine with runtime, testing, memory, and self-correction layers. Scope: code-related development, testing, debugging, and architecture across all software roles; excludes novel theoretical AI research and non-technical organisational politics.",
    "capabilities": {
      "runtime_layer": {
        "functions": {
          "observe_runtime_signals": {
            "description": "Ingest runtime logs, metrics, and error events.",
            "inputs_required": [
              "log_samples",
              "error_events",
              "metrics_snapshot",
              "deployment_context"
            ],
            "outputs": [
              "runtime_health_summary",
              "suspected_failure_points",
              "candidate_signals_to_instrument"
            ]
          },
          "derive_execution_gaps": {
            "description": "Find missing checks, missing branches, and unhandled states.",
            "inputs_required": [
              "runtime_health_summary",
              "engine_expected_flows",
              "entity_state_model"
            ],
            "outputs": [
              "execution_gap_list",
              "prioritised_runtime_fix_list"
            ]
          }
        }
      },
      "testing_layer": {
        "functions": {
          "generate_test_matrix": {
            "description": "Produce a full test matrix for unit, integration, and E2E.",
            "inputs_required": [
              "feature_spec",
              "api_contracts",
              "entity_state_model",
              "risk_assessment"
            ],
            "outputs": [
              "test_case_catalog",
              "coverage_matrix",
              "risk_based_prioritisation"
            ]
          },
          "generate_test_code": {
            "description": "Generate concrete test code for highest-priority cases.",
            "inputs_required": [
              "test_case_catalog",
              "target_stack",
              "project_testing_conventions"
            ],
            "outputs": [
              "unit_test_files",
              "integration_test_files"
            ]
          },
          "interpret_test_results": {
            "description": "Map failing test outputs to likely defects.",
            "inputs_required": [
              "failing_test_logs",
              "test_case_catalog",
              "related_source_files"
            ],
            "outputs": [
              "defect_hypotheses",
              "candidate_patches",
              "regression_risk_analysis"
            ]
          }
        }

---
**MOC:** [[references_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[references_MOC]] · [[07_SKILLS_MOC]]

**MOC:** [[references_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-representation-aware-bug-localization-rscf-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-representation-aware-bug-localization-rscf/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
