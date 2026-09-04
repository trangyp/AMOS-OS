---
title: H/M/L Canon — MOC
type: moc
source: 07_SKILLS/amos-hml-canon
moc: true
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---
# H/M/L Canon — Map of Content

**Path:** `07_SKILLS/amos-hml-canon`

## Role

Fractal knowledge resolution and retrieval architecture (High / Mid / Low) for scale-invariant claim validation. H/M/L is the AMOS discipline for assigning the right validation rigor and retrieval depth to a claim based on its scale, consequence, and available evidence.

## When to Use

- Resolving claims across H/M/L scales.
- Validating scale-invariant knowledge.
- Deciding whether a claim needs high-detail proof (L), mid-level model validation (M), or broad canonical sweep (H).
- Compressing H-level abstractions to M/L execution detail or lifting M/L evidence to H-level summaries.

## Files

- [[07_SKILLS/amos-hml-canon/SKILL|H/M/L Canon SKILL]] — canonical skill definition
- [[07_SKILLS/amos-hml-canon/amos-hml-canon_MOC|H/M/L Canon MOC]] — this index

## H/M/L Lenses

| Scale | Rigor | Use Case | Validation Focus |
|-------|-------|----------|------------------|
| H (High) | Broad, canonical | System invariants, law families, universe-scale contracts | Consistency, authority, lineage |
| M (Mid) | Structural, model | Subsystems, agents, skills, workflows | Composition, traceability, test evidence |
| L (Low) | Executable, detailed | Code, data, runtime traces, receipts | Empirical execution, witnesses, logs |

## Cross-Scale Rules

- A claim validated at L can support an M claim only if the M claim is within the L-claim's provenance scope.
- A claim validated at M can support an H claim only if the H abstraction does not introduce new assertions beyond the M evidence.
- Scale promotion requires a governed promotion gate, not just lexical summary.
- Scale demotion (H → M → L) must preserve the weakest load-bearing evidence.

## Cross-Plane Bindings

- **Canon:** [[01_CANON/02_UNIVERSE_CANON/HML_CANON|HML_CANON]]
- **High scale:** [[25_COGNITIVE_MATRIX/04_SCALES/H_HIGH_SCALE/H_HIGH_SCALE_MOC|H_HIGH_SCALE_MOC]]
- **Mid scale:** [[25_COGNITIVE_MATRIX/04_SCALES/M_MID_SCALE/M_MID_SCALE_MOC|M_MID_SCALE_MOC]]
- **Low scale:** [[25_COGNITIVE_MATRIX/04_SCALES/L_LOW_SCALE/L_LOW_SCALE_MOC|L_LOW_SCALE_MOC]]
- **Validation:** [[07_SKILLS/amos-validation-pipeline/amos-validation-pipeline_MOC|amos-validation-pipeline_MOC]]
- **Parent skill:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Governance Notes

- This skill is `AMOS_MODEL` / `DERIVED`.
- Executable closure is not established by this specification.
- All routed tasks must preserve RSCF epistemic boundaries.
- `H/M/L != TRUTH`; H/M/L is a validation-rigor lens, not an epistemic shortcut.

## Parent

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
