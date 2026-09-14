---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_executable_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Coverage Model
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
canonical_status: CONDITIONAL
---

# COVERAGE_MODEL — Executable Scoped-Completeness Model

Origin architect / steward: **Trang Phan**

## Status

`IMPLEMENTED_BOUNDED / LOCALLY_VALIDATED / NOT_CANON_PROMOTED`

Reference runtime:
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/cognitive_matrix_coverage_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_cognitive_matrix_coverage_runtime.py`

Coverage is structural and scoped. It is not proof that a claim is true, empirically valid, safe to deploy, or canonically authoritative.

## Required object types

A declared scope contains finite requirements `R = {r_1, ..., r_n}`. Each requirement binds:
- requirement ID;
- artifact kind;
- required active stage;
- criticality;
- explicit dependencies.

Active stage chain:

```text
CONTRACT_ONLY < IMPLEMENTED_BOUNDED < VALIDATED_BOUNDED < GOVERNED_BOUNDED
```

Exception states are **not** points on that promotion chain:

```text
UNBOUND | STALE | COMPETING | FALSIFIED | QUARANTINED
```

They cannot be converted into higher active stages by rank arithmetic.

## Dependency topology matrix

For an ordered requirement list `(r_1,...,r_n)`, define the directed adjacency matrix

`A in {0,1}^{n x n}`

by

`A[i,j] = 1` iff `r_i` directly depends on `r_j`.

Boolean transitive closure is

`C = A OR A^2 OR ... OR A^n`,

where multiplication and addition are interpreted over the Boolean semiring.

`C[i,j] = 1` therefore means that `r_i` depends on `r_j` through a path of length at least one. A nonzero diagonal entry `C[i,i]=1` marks a dependency cycle.

**Firewall:** dependency reachability is not causal evidence.

## Stage sufficiency

Define the active-stage rank only on the active chain:

- `rho(CONTRACT_ONLY)=1`
- `rho(IMPLEMENTED_BOUNDED)=2`
- `rho(VALIDATED_BOUNDED)=3`
- `rho(GOVERNED_BOUNDED)=4`

For an acyclic declared scope, let `BaseSat(r_i)` mean:
1. exactly one record resolves for `r_i`;
2. the record is structurally valid;
3. the record is in an active stage;
4. `rho(current_i) >= rho(required_i)`.

Then

`Sat(r_i) := BaseSat(r_i) AND AND_{j: C[i,j]=1} BaseSat(r_j)`.

If a dependency is undeclared or the dependency topology is cyclic, the runtime does not manufacture a fixed point; it preserves `UNKNOWN/GAP`.

## Completion states

- `COMPLETE_FOR_SCOPE`: every declared requirement is satisfied and no unresolved blocker exists.
- `CONDITIONAL`: only explanatory/cosmetic gaps remain.
- `INCOMPLETE`: a critical or decision-relevant requirement has a known missing/below-stage dependency.
- `CONTRADICTORY`: an in-scope required record is `FALSIFIED`.
- `UNKNOWN/GAP`: a critical or decision-relevant result depends on unresolved cycle, duplicate binding, undeclared dependency, invalid record, `STALE`, `COMPETING`, or `QUARANTINED` state.

## Non-equivalences

```text
FILE_EXISTS != CONTRACT_COMPLETE
CONTRACT_COMPLETE != IMPLEMENTED
IMPLEMENTED != VALIDATED
VALIDATED != GOVERNED
GOVERNED != CANONICAL
COVERAGE != TRUTH
TOPOLOGY != CAUSALITY
UNKNOWN/GAP != ZERO
```

A percentage is not a promotion criterion. The runtime reports explicit required/satisfied counts only as descriptive counts; completion status is determined by typed gates and dependency closure.

## Executed evidence

Local bounded verification on 2026-09-14:
- 19 coverage-runtime tests passed, 0 failed;
- 5,000 seeded random dependency graphs matched independent DFS reachability checks, 0 observed closure mismatches;
- 128 active-stage/receipt promotion-state checks, 0 observed invalid promotions.

These are local executable receipts, not GitHub Actions evidence and not universal AMOS correctness.

## RSCF boundary

`SOURCE_CANON != AMOS_MODEL != EXECUTED_BOUNDED != EMPIRICAL_TRUTH`.

The 2026-09-14 `_00_AMOS_CANON` material is used as `ACTIVE_REPAIR_SPEC / AMOS_MODEL` input. Canon promotion remains under canon governance.

[[25_COGNITIVE_MATRIX/07_COVERAGE/07_COVERAGE_MOC|07_COVERAGE_MOC]] · [[25_COGNITIVE_MATRIX/08_STRUCTURAL_GAPS/08_STRUCTURAL_GAPS_MOC|08_STRUCTURAL_GAPS_MOC]]
