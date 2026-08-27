---
title: "AMOS ABI and IO Test Expansion"
created: "2026-08-23"
origin: "Hermes ↔ Cosmo Brain"
origin_architect: "Trang Phan"
type: note
tags: [cosmo, amos, canon-group/system, rscf/claim, rscf/state/observation, topic/implementation, topic/testing, topic/abi, topic/io, dated, dated/2026-08-23]
status: "verified"
provenance: "OBSERVATION"
confidence: "VERIFIED"
---


# AMOS ABI and IO Test Expansion

> Epistemic class: OBSERVATION
> Conclusion label: `VERIFIED` — ABI registry tests expanded from 11 to 30, IO module tests expanded from 10 to 24.

## What was done

Expanded test coverage for two areas that had minimal tests:

### ABI Registries (`tests/test_abi_registries.py`)
- **Before**: 11 tests (basic discover, empty registry, nonexistent path)
- **After**: 30 tests (+19 new)

New tests cover:
- Nested directory discovery (rglob searches recursively)
- Same-name overwrite behavior (last wins)
- `discover()` returns `self.models`/`self.skills`/`self.tools` (not a copy)
- Empty paths list returns empty dict
- ModelManifest field validation (version, capabilities, max_context, etc.)
- SkillManifest field validation (executor, mutation_class)
- ToolManifest field validation (capability, consequence, reversible)
- ModelWorker with manifest still returns GAP (no transport configured)
- ModelWorker preserves payload, includes reason
- Multiple skills/tools in subdirectories

### IO Modules (`tests/test_io_modules.py`)
- **Before**: 10 tests (basic task/evidence/claim/payload)
- **After**: 24 tests (+14 new)

New tests cover:
- All Task fields (objective, domain, stakes, irreversibility, freshness_need, context)
- Empty objective string
- Extra fields silently ignored
- DERIVED epistemic for evidence
- Evidence with parent_ids
- Evidence preserves all fields
- Claim default epistemic (DERIVED)
- Claim COMPETING status
- Claim with premise_ids and competing_ids
- Multiple evidence and claims in payload
- Empty payload raises TypeError (Task requires objective)
- Evidence-only and claims-only payloads

## Key Behaviors Discovered

1. **`task_from(d)`** filters dict keys against `Task.__dataclass_fields__` —
   unknown keys are silently dropped, not raised as errors.
2. **`evidence_from(d)`** defaults `epistemic` to `SOURCE_CLAIM` if not provided.
3. **`claim_from(d)`** defaults `epistemic` to `DERIVED` and `status` to `DERIVED`.
4. **`payload(d)`** treats the dict itself as the task if no `"task"` key exists.
5. **Registry `discover()`** uses `rglob("*.json")` — recursive search.
   Same-name entries overwrite (last wins). Returns the internal dict, not a copy.
6. **`ModelWorker.request()`** always returns `UNKNOWN/GAP` — even with a manifest.
   This is a host integration point; the kernel owns schema and admission.

## Cross-Runtime Status

| Runtime | Tests | Status |
|---------|-------|--------|
| Python (AMOS OS Kernel) | 1934 passed | Green |
| TypeScript (Cosmo Brain) | 1253 passed (74 files) | Green |
| **Total** | **3129** | **Both green** |

## Links

- [[00_COSMO_BRAIN_MOC]]
- 2026-08-23 AMOS Authority and GMEF Gate Integration
- 2026-08-22 AMOS Core Module Test Coverage

---
**MOC:** [[DATED_MOC]]
