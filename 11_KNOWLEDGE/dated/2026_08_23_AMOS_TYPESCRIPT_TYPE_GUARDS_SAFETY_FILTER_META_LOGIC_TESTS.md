---
title: "AMOS TypeScript Type-Guards + Safety-Filter + Meta-Logic Test Expansion"
created: "2026-08-23"
origin: "Hermes ↔ Cosmo Brain"
origin_architect: "Trang Phan"
type: note
source: 11_KNOWLEDGE/dated
tags:
- cosmo
- amos
- canon-group/tech-ai
- rscf/claim
- rscf/state/observation
- topic/typescript
- topic/type-guards
- topic/safety-filter
- topic/meta-logic
- topic/testing
- dated
- dated/2026-08-23
- canon/knowledge
status: "verified"
provenance: "OBSERVATION"
confidence: "VERIFIED"
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: temporal_log
---


# AMOS TypeScript Type-Guards + Safety-Filter + Meta-Logic Test Expansion

> Epistemic class: OBSERVATION
> Conclusion label: `VERIFIED` — Added 4 new TypeScript test files (119 tests):
> type-guards (39), safety-filter (37), meta-logic (39), meta-logic-bug (4).
> TypeScript: 1195 → 1253 (+58 net). Total: 3400 → 3458.
> Governing law: `integrity > completeness > fluency > speed > token savings`.

## What was done

Added 4 new TypeScript test files covering type guards, safety filter,
meta-logic reasoning, and a meta-logic word-boundary bug regression.

## New Test Files

### 1. `tests/unit/type-guards.test.ts` (39 tests)

Tests `core/type-guards.ts` (100 lines):
- `isRecord`, `isString`, `isNumber`, `isBoolean`, `isNumberArray`, `isStringArray`
- `asString`, `asBoolean`, `asNumber`, `asNumberOrNull`, `asRecord`,
  `asStringArray`, `asNumberArray`
- Tests type narrowing, safe coercion, null handling, edge cases

### 2. `tests/unit/safety-filter.test.ts` (37 tests)

Tests `core/reasoning/safety-filter.ts` (205 lines):
- `filterOutput` — clean output passes, diagnostic language replaced
- `SAFETY_FILTER_VERSION`, `SAFE_EXPLANATIONS`
- `SafetyFilterInput` type, `OutputType` handling
- Tests filtering of diagnostic language, safe replacement explanations

### 3. `tests/unit/meta-logic.test.ts` (39 tests)

Tests `core/reasoning/meta-logic.ts` (407 lines):
- `META_LOGIC_VERSION`, `LOGIC_MODE_PROPERTIES`, `OPERATIONAL_MODES`
- `CURRENT_OPERATIONAL_MODE`, `isRiskScoreAcceptable`
- `canWriteExternally`, `canDeleteExternally`
- `applyLawOfLaw`, `applyRuleOf2`, `applyRuleOf4`, `applySignalFidelity`
- `reason` function with `ReasoningInput` type

### 4. `tests/unit/meta-logic-bug.test.ts` (4 tests)

Regression test for `applyLawOfLaw` word-boundary bug:
- Bug: substring match on 'not' caused false positives ("notable", "note")
- Negation check only inspected the claim, not the evidence
- Tests that "notable" is NOT flagged as a contradiction
- Tests that "note" is NOT flagged as a contradiction

## Test Results

| Suite | Before | After |
|-------|--------|-------|
| TypeScript (vitest) | 1195 (73 files) | 1253 (74 files, +58) |
| Python kernel (pytest) | 1934 | 1934 |
| Cognitive substrate | 271 | 271 |
| **Total** | **3400** | **3458** |

## Cross-Runtime Status

| Runtime | Tests | Status |
|---------|-------|--------|
| Python (AMOS OS Kernel) | 1934 passed | Green |
| Cognitive Substrate | 271 passed | Green |
| TypeScript (Cosmo Brain) | 1253 passed (74 files) | Green |
| **Total** | **3458** | **All green** |

## Grand Total (with deterministic verification)

| Runtime | Tests |
|---------|-------|
| Python kernel (pytest) | 1934 |
| Cognitive substrate (self-tests + pytest) | 271 |
| TypeScript (vitest) | 1253 |
| Deterministic verification | 359 |
| **Grand total** | **3817** |

## Key Source Modules

- `core/type-guards.ts` (100 lines) — runtime type guards and safe coercions
- `core/reasoning/safety-filter.ts` (205 lines) — diagnostic language filtering
- `core/reasoning/meta-logic.ts` (407 lines) — meta-logic reasoning with 5 laws

## Verification

```bash
cd cosmo-brain
npx vitest run --reporter=default
# Expected: 74 files, 1253 passed, 0 failed
```

## Links

- [[00_COSMO_BRAIN_MOC]]
- 2026-08-23 AMOS Kafka Brain Buffer
- 2026-08-23 AMOS Cognitive Substrate Dependency-Safe Forgetting

## Update (2026-08-23)

After Kafka Brain Buffer test suite (180 tests) was added, totals updated:
- TypeScript: 1253 (vitest) + 180 (tsx standalone) = 1433
- Total verified: 1934 + 271 + 1433 = 3638
- Grand total with deterministic verification: 3638 + 359 = 3997
- See 2026-08-23 AMOS Kafka Brain Buffer Test Suite for details

---
**MOC:** [[DATED_MOC]]
