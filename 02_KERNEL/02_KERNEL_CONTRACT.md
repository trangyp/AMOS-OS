---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 02 Kernel Contract
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
updated: 2026-09-14
---
---
---

# 02 Kernel — Plane Contract

## 1. Identity

| Field | Value |
|-------|-------|
| Plane | 02_KERNEL |
| Role | Typed computational and logical primitive specifications plus bounded reference bindings |
| Owner | Trang Phan (origin architect) |
| Active AMOS_CORE target | v4.4 |
| Canonical ULK owner | `ULK_LOGIC_KERNEL.md` v2.1.0 |

## 2. Role

The Kernel plane defines and binds reusable computational primitives for AMOS OS. A kernel artifact may be a source specification, AMOS_MODEL, bounded executable reference, formally proved object, or unresolved gap. The plane does **not** imply that every AMOS computation is deterministic, fully validated, recoverable, canon-compliant, or authorized merely because a kernel document exists.

Kernel execution claims are admitted per primitive and per implementation identity. External solvers, probabilistic/LLM workers, heuristic algorithms, and environment-dependent operations retain their own determinism and guarantee classes.

## 3. Interfaces

### Inputs

- Source/canon definitions from `01_CANON`, with source/canon precedence preserved
- Control-plane proposals and authorized commands from `03_CONTROL_PLANE`
- Runtime state and implementation identities from `04_RUNTIME`
- Typed problem state, assumptions, scope, regime, provenance, and freshness

### Outputs

- Bounded logical/computational results with explicit result class
- Proposed state transitions or validation evidence
- Failure/UNKNOWN/GAP/COMPETING signals
- Provenance and observability records

Kernel output is not automatically a commit, empirical fact, canon promotion, or authority witness.

## 4. Hard invariants

- **KERNEL-01 — typed determinism:** a primitive may be called deterministic only when its transition/function contract is deterministic for the declared inputs, state, ordering assumptions, and environment. `KERNEL_PRESENT != DETERMINISTIC`.
- **KERNEL-02 — provenance:** consequential reusable results require traceable source/implementation/state identity. Missing provenance blocks promotion; it does not fabricate a result.
- **KERNEL-03 — failure honesty:** detected failures are classified; undetected failure remains possible unless coverage proves otherwise. `FAILURE_HANDLER_EXISTS != ALL_FAILURES_DETECTED`. Recovery success must be demonstrated per failure class.
- **KERNEL-04 — authority separation:** capability and validation never mint authority. Consequential effects require an applicable fresh authority witness at the control/commit boundary.
- **KERNEL-05 — canon separation:** kernel results may be checked against applicable canon, but no runtime or test proves universal canon compliance for every inference. Candidate/source material cannot self-promote.
- **KERNEL-06 — mathematics firewall:** mathematical notation, indexed records, graph adjacency, point-set topology, logical implication, reachability, and causality remain distinct unless explicit mathematical mappings license composition.
- **KERNEL-07 — logic-family separation:** canonical ULK ALUs, ULMK Atomic Logic Units, Core-19 semantic primitives, and executable AMOS_CORE AST constructors are separate namespaces.
- **KERNEL-08 — bounded proof:** `TEST_PASS != TRUTH`, `FORMAL_PROOF != EMPIRICAL_VALIDITY`, and `BOUNDED_EXECUTION != GLOBAL_SOUNDNESS_OR_COMPLETENESS`.
- **KERNEL-09 — stale dependency semantics:** dependency failure normally makes dependent results `STALE/REVALIDATE`; falsity requires stronger semantics/evidence.
- **KERNEL-10 — authority of structure:** topology/graph/tensor representations carry only the semantics explicitly defined by their contracts.

## 5. Active logic interpretation

Current governed logic routing follows:

1. `ULK_LOGIC_KERNEL.md` v2.1.0 as canonical root ULK.
2. Candidate repair overlays and `_00_AMOS_CANON:` revisions as candidate/source evidence, not automatic canon.
3. Eight ULK fragment bindings remain bounded by their individual execution registries.
4. Core-19 `19 x 19 = 361` is cardinal arithmetic for the relation-field address space; unknown semantic cells remain UNKNOWN rather than invented.
5. P02 remains `COMPETING` across historical Absolute/MURK `NonExistence` and living-map Core-19 `Distinction` unless source/version resolves the lineage.
6. Finite-trace temporal execution is not ordinary infinite-word LTL model checking.

## 6. Lifecycle

```text
SOURCE/SPECIFY
  -> TYPE + BIND ASSUMPTIONS
  -> IMPLEMENT (when applicable)
  -> EXECUTE TESTS / PROOF
  -> CHALLENGE
  -> CLASSIFY BOUNDED RESULT
  -> AUTHORITY GATE (if consequential)
  -> COMMIT/DEPLOY (outside kernel authority)
  -> OBSERVE / REVALIDATE / REPAIR
```

No stage may be inferred merely from the existence of the previous stage.

## 7. Current bounded evidence

Examples of executable bounded evidence include the Core-19 Boolean firewall, finite relation algebra/topology checks, eight-ALU fragment registry, Cognitive Matrix dependency/validation runtimes, mathematical type firewall, and algorithm ingress/runtime tests under `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/`.

These artifacts establish only their tested domains. They do not prove universal reasoning correctness, universal recovery, general intelligence, or production deployment validity.

## 8. Open gaps

- Complete formal semantics/proofs for every claimed nonclassical logic fragment
- Proof-producing or independently verified backends for fragments currently checked only by bounded reference implementations
- Complete runtime provenance/receipt persistence across all kernel calls
- Independent coverage evidence for failure detection/recovery classes
- Complete commit-time authority integration for all consequential paths
- Repository-wide elimination or quarantine of stale source overclaims

______________________________________________________________________

**Parent:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
