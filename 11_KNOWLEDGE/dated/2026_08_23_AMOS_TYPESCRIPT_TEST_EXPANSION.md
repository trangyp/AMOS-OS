---
title: "AMOS TypeScript Test Expansion — Type Guards, Safety Filter, Meta-Logic"
created: "2026-08-23"
origin: "Hermes ↔ Cosmo Brain"
origin_architect: "Trang Phan"
type: note
source: 11_KNOWLEDGE/dated
tags: [cosmo, amos, canon-group/tech-ai, rscf/claim, rscf/state/observation, topic/typescript, topic/testing, topic/type-guards, topic/safety-filter, topic/meta-logic, dated, dated/2026-08-23, canon/knowledge]
status: "verified"
provenance: "OBSERVATION"
confidence: "VERIFIED"
rscf:
  state: SOURCE_CLAIM
  claim_class: EMPIRICAL
  provenance: AMOS_corpus
  scope: temporal_log
---


# AMOS TypeScript Test Expansion — Type Guards, Safety Filter, Meta-Logic

> Epistemic class: OBSERVATION
> Conclusion label: `VERIFIED` — Added 115 TypeScript tests across 3 new test files.
> TypeScript test count: 1195 → 1253 (+58 net, 115 new tests, some refactoring).
> Governing law: `integrity > completeness > fluency > speed > token savings`.

## What was done

Created 3 new TypeScript test files covering previously untested core modules:
`core/type-guards.ts`, `core/reasoning/safety-filter.ts`, and
`core/reasoning/meta-logic.ts`.

## New Test Files

### 1. `tests/unit/type-guards.test.ts` — 39 tests

Covers all 16 exported functions from `core/type-guards.ts`:
- **Type guards**: `isRecord`, `isString`, `isNumber`, `isBoolean`,
  `isNumberArray`, `isStringArray`
- **Coercion helpers**: `asString`, `asBoolean`, `asNumber`, `asNumberOrNull`,
  `asRecord`, `asStringArray`, `asNumberArray`, `asUnion`
- **Utilities**: `typedEntries`, `pickTopEntry`

Key test cases:
- `isRecord` rejects arrays and null
- `isNumber` returns true for NaN (per JS spec)
- `asNumberArray` returns zero-filled array of specified length for invalid input
- `pickTopEntry` caps confidence at 1.0 and sorts entries descending

### 2. `tests/unit/safety-filter.test.ts` — 37 tests

Covers `core/reasoning/safety-filter.ts` — the Cosmo Safety and Claim Filter:
- **filterOutput**: clean output, blocked claims, warnings, risk levels
- **replaceDiagnosticLanguage**: emotional → acoustic terminology
- **SAFE_EXPLANATIONS**: pitchRange, energy, continuity, harmonicity
- **SAFETY_FILTER_VERSION**: version string

Key test cases:
- Emotional diagnosis claims blocked with "high" risk level
- Medical claims blocked with "critical" risk level
- Trauma claims blocked with "critical" risk level
- Human review required for >2 blocked claims
- Disclaimers appended for resonance_interpretation, artwork_explanation, comparison_result
- Comparative/absolute/scientific language triggers warnings

### 3. `tests/unit/meta-logic.test.ts` — 39 tests

Covers `core/reasoning/meta-logic.ts` — the Cosmo Meta-Logic Reasoning Kernel:
- **Constants**: META_LOGIC_VERSION, LOGIC_MODE_PROPERTIES, CURRENT_OPERATIONAL_MODE
- **Operational modes**: SAFE_INTROSPECTION_ONLY, EXTERNAL_WRITE_LOW_RISK, EXPERIMENTAL_BUILD
- **Law of Law**: contradiction detection, assumption explicitness
- **Rule of 2**: structural opposite generation (positive/negative, growth/decline, etc.)
- **Rule of 4**: quadrant mapping (biological, experiential, logical, systemic)
- **Signal Fidelity**: emotional/medical/spiritual claim detection
- **Combined reason()**: all 4 laws, confidence calculation, uncertainty collection

Key test cases:
- Risk score thresholds: 0.3 (SAFE), 0.6 (EXTERNAL_WRITE), 0.9 (EXPERIMENTAL)
- No operational mode allows external deletes
- Law of Law detects contradictions via word-boundary negation
- Rule of 2 generates structural opposites for known patterns
- Rule of 4 detects causal ("because") and conditional ("if/then") structures
- Signal Fidelity detects simulated emotion and unsupported medical claims

## Test Results

| Suite | Before | After |
|-------|--------|-------|
| TypeScript total | 1195 | 1253 (+58 net) |
| Test files | 71 | 74 (+3) |
| New tests | — | 115 (39 + 37 + 39) |

## Cross-Runtime Total

| Runtime | Count |
|---------|-------|
| Python kernel tests | 2015 |
| Cognitive substrate tests | 271 |
| TypeScript tests | 1392 |
| Kafka Brain Buffer (tsx) | 180 |
| **Cross-runtime total** | **3858** |
| Plus deterministic verification | +359 |
| **Grand total** | **4217** |

## Key Lessons

1. **Type guard `isNumber(NaN)` returns true**: Per JavaScript spec, `typeof NaN === "number"`.
   This is intentional — tests should verify this behavior, not "fix" it.

2. **Safety filter risk levels**: `medical_claim` and `trauma_claim` → critical;
   `emotional_diagnosis` → high; other blocked → medium; warnings only → low.

3. **Operational modes never allow external deletes**: All 3 modes
   (SAFE_INTROSPECTION_ONLY, EXTERNAL_WRITE_LOW_RISK, EXPERIMENTAL_BUILD) have
   `allowExternalDelete: false`. Only writes are gated by mode.

4. **Rule of 2 structural opposites**: The `generateStructuralOpposite` function
   uses a pattern list (positive/negative, increases/decreases, etc.). Unknown
   patterns get `[Structural opposite of]` prefix.

5. **Law of Law word-boundary negation**: Uses `\bnot\b` regex to avoid false
   positives on "notable", "note", "nothing". This is critical for correct
   contradiction detection.

## Links

- [[00_COSMO_BRAIN_MOC]]
- 2026-08-23 AMOS Brain Cortex and Executable Brain Model Bug Fixes
- 2026-08-23 AMOS Expression Translation Test Expansion
- 2026-08-23 Deterministic Verification Summary

---
**MOC:** [[DATED_MOC]]
