---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 02 Kernel Readme
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

# 02 Kernel — README

## Role

The Kernel layer defines typed computational and logical primitives used by AMOS OS and binds them to bounded executable references where implementation evidence exists. It is not a blanket guarantee that every AMOS computation is deterministic, correct, recoverable, canon-compliant, or authorized.

Runtime use must preserve these distinctions:

```text
SPECIFICATION != IMPLEMENTATION
IMPLEMENTATION != VALIDATION
VALIDATION != TRUTH
CAPABILITY != AUTHORITY
SOURCE_CLAIM != CANON
GRAPH/ADJACENCY != POINT-SET TOPOLOGY
REACHABILITY != ENTAILMENT != CAUSALITY
INDEXED FIELD != ALGEBRAIC TENSOR
```

## Scope

### In scope

- Logic and meta-logic specifications with per-fragment execution bounds
- Core-19 semantic registry and executable AMOS_CORE syntax, kept as separate namespaces
- State/concurrency primitives such as CAS/MVCC where explicitly implemented
- Memory operation contracts and bounded lifecycle executors
- Risk/repair primitives and recovery contracts
- Authority-checking primitives without authority self-minting
- Provenance/source tracking
- Cross-layer integration contracts
- Mathematical type, scope, and assumption firewalls

### Out of scope

- Claiming every runtime path is deterministic
- Treating LLM/probabilistic/external solver behavior as deterministic without a specific contract
- Universal failure detection/recovery guarantees
- Autonomous canon promotion
- Effect/deployment authority
- Empirical truth or causal truth from logical/graph structure alone
- Full semantic completion merely because a file or executor exists

## Logic namespace guards

Do not merge these by name or cardinality:

1. **Canonical root ULK** — `ULK_LOGIC_KERNEL.md` v2.1.0, eight logic-engine ALUs.
2. **ULMK** — separate source family with eight Atomic Logic Units plus meta-laws/operators/patterns.
3. **Core-19 semantic registry** — P01–P19 living-map vocabulary; 19×19 gives 361 possible ordered relation addresses, not 361 known semantics.
4. **Executable AMOS_CORE AST** — implementation syntax with its own supported fragment boundary.

Historical Absolute/MURK P02 `NonExistence` versus living-map P02 `Distinction` remains `COMPETING` unless the requested lineage/version resolves it.

## Structure

```text
02_KERNEL/
├── 00_INDEX/                  navigation indices
├── 01_META_LOGIC/             logic, meta-logic, repair overlays
├── 02_COGNITION/              cognitive computation contracts
├── 03_CAUSAL/                 causal-model contracts; not inferred from graph reachability
├── 04_STATE/                  state transition primitives
├── 05_MEMORY/                 computational memory operations
├── 06_RISK_REPAIR/            failure/repair contracts
├── 07_AUTHORITY/              permission validation primitives
├── 08_PROVENANCE/             source/provenance primitives
├── 09_INTEGRATION/            cross-layer composition
├── K_CAS.md
├── K_MVCC.md
├── MVCC_CAS.md
├── K_FAILURE_RECOVERY.md
├── DETERMINISTIC_LOGIC_KERNEL.md
└── additional source/model/kernel artifacts
```

## Key governed surfaces

| Surface | Bounded role | Boundary |
|---|---|---|
| ULK logic kernel | fragment routing/specification | each ALU keeps its own proof/execution scope |
| Core-19 runtime | bounded executable logic subset | nonclassical/meta nodes are not silently reduced to Boolean SAT |
| CAS/MVCC | state/concurrency primitives | implementation identity and concurrency assumptions matter |
| Failure/repair | recovery mechanisms | handler existence does not prove total failure coverage |
| Authority | permission checks | capability/validation cannot mint authority |
| Canon admission | candidate eligibility | candidate cannot self-promote to Canon |
| Provenance | source lineage | provenance does not itself establish truth |

## Execution and evidence

Executable reference implementations live primarily under `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/` and related subsystem runtime owners. A documentation surface may therefore have an executor elsewhere; use the machine-checkable execution registries rather than assuming file locality.

For mathematical claims, require definitions, domains/types, assumptions, derivation or executable recalculation, counterexample search, and result classification. For consequential claims, carry scope, regime, freshness, provenance, and authority separately.

## Inter-plane connections

- **Canon:** [[01_CANON/01_CANON_MOC|01_CANON_MOC]] — source/canon precedence and admissibility boundaries
- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] — policy/authority/commit orchestration
- **Runtime:** [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME_MOC]] — executable implementations and state
- **Cognitive Matrix:** [[25_COGNITIVE_MATRIX/25_COGNITIVE_MATRIX_MOC|25_COGNITIVE_MATRIX_MOC]] — typed plane/cell routing and validation

______________________________________________________________________

**Parent:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
