---
title: "AMOS Runtime Test Expansion"
created: "2026-08-23"
origin: "Hermes ↔ Cosmo Brain"
origin_architect: "Trang Phan"
type: "note"
tags: [cosmo, amos, canon-group/system, rscf/claim, rscf/state/observation, topic/implementation, topic/testing, topic/runtime, topic/finalize, dated, dated/2026-08-23]
status: "verified"
provenance: "OBSERVATION"
confidence: "VERIFIED"
---

# AMOS Runtime Test Expansion

> Epistemic class: OBSERVATION
> Conclusion label: `VERIFIED` — Runtime module tests expanded from 17 to 37, IO tests fixed and expanded.

## What was done

### Runtime Modules (`tests/test_runtime_modules.py`)
- **Before**: 17 tests (basic closure, topo, build, tensor, complexity, budget, select, audit, finalize)
- **After**: 37 tests (+20 new)

New tests cover:
- Transitive dependency closure (a→b→c)
- Multiple root closure
- Self-dependency closure
- Topological sort chain ordering
- Topological sort with no dependencies
- Priority ordering (lower priority = earlier in order)
- Tensor with critical stakes, domain, irreversibility
- Complexity monotonicity (higher stakes ≥ lower stakes complexity)
- Budget monotonicity (C4 tokens > C0 tokens)
- Budget for all complexity levels (C0-C4)
- Selector with empty skills
- Selector C0 returns core skills
- Selector C4 adds all available skills
- Finalize with no claims → DERIVED (not UNKNOWN)
- Finalize with mixed VERIFIED + UNKNOWN → DERIVED (not all VERIFIED)
- Finalize with all VERIFIED → VERIFIED
- Finalize produces final dict
- Finalize preserves gates

### IO Module Fix (`amos/io.py`)
- Fixed `task_from(d)` to provide default `""` for missing `objective`
- This allows `payload({})` to create a default task instead of raising `TypeError`

## Key Behaviors Discovered

### `finalize(state)` Status Priority
1. FAIL gates → `Status.UNKNOWN`
2. Competing claims (with `competing_ids`, not INVALIDATED/QUARANTINED) → `Status.COMPETING`
3. Conditional gates or memory gaps → `Status.CONDITIONAL`
4. All claims VERIFIED → `Status.VERIFIED`
5. Else → `Status.DERIVED`

**Important**: No claims + no fails = `DERIVED` (not `UNKNOWN`).
Mixed VERIFIED + UNKNOWN claims = `DERIVED` (not all VERIFIED).

### `closure(roots, skills)` Behavior
- Transitive: a→b→c closure includes all three
- Self-dependency: a→a is handled (returns {a})
- Missing skill raises `KeyError`

### `topo(roots, skills)` Behavior
- Lower priority value = earlier in order
- Dependencies always come before dependents
- No deps = sorted by priority

## Cross-Runtime Status

| Runtime | Tests | Status |
|---------|-------|--------|
| Python (AMOS OS Kernel) | 1934 passed | Green |
| TypeScript (Cosmo Brain) | 1253 passed (74 files) | Green |
| **Total** | **3129** | **Both green** |

## Links

- [[00_Cosmo_Brain_MOC]]
- 2026-08-23 AMOS ABI and IO Test Expansion
- 2026-08-22 AMOS Core Module Test Coverage
