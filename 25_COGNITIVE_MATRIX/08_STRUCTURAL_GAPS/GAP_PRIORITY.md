---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Gap Priority
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - cognitive-matrix
updated: 2026-09-14
---

# GAP_PRIORITY — Bounded Executable Contract

**Origin architect / steward:** Trang Phan  
**Class:** `COGNITIVE_MATRIX_CONTRACT`  
**Status:** `IMPLEMENTED_BOUNDED / VALIDATED_BOUNDED`  
**Runtime binding:** `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/cognitive_matrix_runtime.py`  
**Validation binding:** `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_cognitive_matrix_runtime.py`

## Scope

Ranks already-identified repair gaps. It does not discover truth, establish causation, promote Canon, or grant execution authority.

## Typed input

For each gap `g`, the runtime requires normalized values in `[0,1]`:

- `S(g)`: safety consequence
- `F(g)`: downstream dependency fan-out
- `I(g)`: irreversibility
- `U(g)`: unresolved uncertainty
- `T(g)`: staleness
- `H(g)`: user/system impact
- `C(g)`: normalized repair effort

A gap also carries a typed `GapKind` and stable `gap_id`.

## AMOS_MODEL equation

The bounded prioritisation model is

\[
U_g = 0.30S_g + 0.20F_g + 0.15I_g + 0.15U_g^{(unc)} + 0.10T_g + 0.10H_g
\]

and

\[
E_g = \frac{U_g}{1+C_g}.
\]

The superscript on `U_g^(unc)` distinguishes uncertainty from the urgency score `U_g`.

Because all six urgency inputs lie in `[0,1]` and the non-negative weights sum to `1`, `U_g` lies in `[0,1]`. Since `C_g` lies in `[0,1]`, `E_g` also lies in `[0,1]`.

This is an **AMOS design model**, not an empirical universal law.

## Safety override

If `S(g) >= 0.90`, the gap enters critical tier `0` before ordinary efficiency ordering. This prevents low repair cost from outranking a high-consequence defect.

Within a tier, deterministic ordering uses:

1. higher `E_g`;
2. higher `U_g`;
3. lexical `gap_id` as the final deterministic tie-break.

## Hard invariants

- `PRIORITY != TRUTH`.
- `PRIORITY != AUTHORITY`.
- Missing or non-finite inputs fail closed.
- Inputs outside `[0,1]` fail closed.
- Safety-critical gaps cannot be demoted solely by effort.
- Ranking cannot silently rewrite `GapKind`.
- The scoring model remains `AMOS_MODEL` unless independently validated for a domain.

## Executed validation

2026-09-14 bounded replay covered:

- score bounds;
- critical-tier override;
- deterministic ranking;
- 128 binary boundary corners of the seven normalized inputs;
- coefficient sum `= 1.0`;
- observed urgency range `[0,1]`;
- observed efficiency range `[0,1]`;
- zero boundary violations.

## RSCF boundary

`IMPLEMENTED_BOUNDED / VALIDATED_BOUNDED` applies only to the reference runtime functions `score_gap` and `prioritize_gaps`. It does not imply that all Cognitive Matrix gaps have been populated or that the whole matrix is validated.

[[25_COGNITIVE_MATRIX/08_STRUCTURAL_GAPS/08_STRUCTURAL_GAPS_MOC|08_STRUCTURAL_GAPS_MOC]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
