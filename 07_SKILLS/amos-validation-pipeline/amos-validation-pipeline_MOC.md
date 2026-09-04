---
title: Validation Pipeline — MOC
type: moc
source: 07_SKILLS/amos-validation-pipeline
moc: true
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---
# Validation Pipeline — Map of Content

**Path:** `07_SKILLS/amos-validation-pipeline`

## Role

10-stage fail-fast validation + GMEF (Governed Machine Evolution Framework) authorization for candidate artifacts, code changes, evolution steps, and promoted claims. Each stage is a gate: a failure stops the pipeline and routes the candidate to repair or rejection.

## When to Use

- A candidate artifact, code change, or evolution step must be validated before promotion or execution.
- A promoted claim needs epistemic, structural, and authority checks.
- A GMEF mutation requires gate-by-gate clearance.
- A runtime or kernel effect needs pre-commit validation.

## Files

- [[07_SKILLS/amos-validation-pipeline/SKILL|Validation Pipeline SKILL]] — canonical skill definition
- [[07_SKILLS/amos-validation-pipeline/amos-validation-pipeline_MOC|Validation Pipeline MOC]] — this index

## Pipeline Stages

| Stage | Purpose | Failure Outcome |
|-------|---------|-----------------|
| 1. Identity | Verify artifact/agent identity and version | reject / re-authenticate |
| 2. Scope | Confirm task within declared capability envelope | reject / escalate |
| 3. Source | Validate source claims and provenance | mark `UNKNOWN/GAP` |
| 4. RSCF | Check epistemic state, confidence, and claim class | reject / re-classify |
| 5. Structural | Lint, parse, and validate schema / wikilinks | repair / reject |
| 6. Canonical | Check against `01_CANON` and authority | reject / supersede |
| 7. Semantic | Validate meaning and non-contradiction | flag `COMPETING` |
| 8. Runtime | Test executable or simulate behavior | rollback / reject |
| 9. Safety | Run safety and adversarial checks | fail-closed |
| 10. Commit | Finalize with receipt and causal epoch | abort if any prior gate failed |

## Cross-Plane Bindings

- **Tests:** [[19_TESTS/19_TESTS_MOC|19_TESTS_MOC]]
- **Governance:** [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C01_GOVERNANCE/C01_GOVERNANCE_MOC|C01_GOVERNANCE_MOC]]
- **GMEF:** [[01_CANON/04_INFRASTRUCTURE_CANON/GMEF_CANON|GMEF_CANON]]
- **Promotion gates:** [[25_COGNITIVE_MATRIX/11_VALIDATION/PROMOTION_GATES|PROMOTION_GATES]]
- **Audit / repair:** [[07_SKILLS/amos-audit-repair-master/SKILL|amos-audit-repair-master]]
- **Parent skill:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Governance Notes

- This skill is `AMOS_MODEL` / `DERIVED`.
- Executable closure is not established by this specification.
- All routed tasks must preserve RSCF epistemic boundaries.
- `TEST_SPECIFIED != TEST_EXECUTED`; `PROPOSAL != COMMIT`.

## Parent

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
