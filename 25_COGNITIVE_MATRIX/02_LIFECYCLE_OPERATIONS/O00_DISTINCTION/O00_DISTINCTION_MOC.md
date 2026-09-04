---
title: O00 Distinction MOC
type: moc
source: 25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O00_DISTINCTION
tags:
  - o00-distinction
  - domain/cognitive-matrix
moc: true
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# O00 Distinction — Map of Content

**Path:** `25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O00_DISTINCTION`
**Files:** 20 | **Subdirectories:** 1

## Files

- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O00_DISTINCTION/COGNITIVE_MATRIX_O00_DISTINCTION_CONTRACT|COGNITIVE_MATRIX_O00_DISTINCTION_CONTRACT]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O00_DISTINCTION/O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_AGENTS|O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_AGENTS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O00_DISTINCTION/O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_CONTROL_PLANES|O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_CONTROL_PLANES]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O00_DISTINCTION/O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_DEFINITION|O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_DEFINITION]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O00_DISTINCTION/O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_DEPENDENCIES|O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_DEPENDENCIES]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O00_DISTINCTION/O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_FAILURE_MODES|O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_FAILURE_MODES]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O00_DISTINCTION/O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_GAP_MATRIX|O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_GAP_MATRIX]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O00_DISTINCTION/O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_HML|O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_HML]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O00_DISTINCTION/O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_INPUT_OUTPUT|O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_INPUT_OUTPUT]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O00_DISTINCTION/O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_INVARIANTS|O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_INVARIANTS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O00_DISTINCTION/O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_POSTCONDITIONS|O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_POSTCONDITIONS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O00_DISTINCTION/O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_PRECONDITIONS|O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_PRECONDITIONS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O00_DISTINCTION/O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_PROTOCOLS|O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_PROTOCOLS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O00_DISTINCTION/O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_README|O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_README]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O00_DISTINCTION/O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_RSCF|O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_RSCF]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O00_DISTINCTION/O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_SEMANTICS|O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_SEMANTICS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O00_DISTINCTION/O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_SKILLS|O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_SKILLS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O00_DISTINCTION/O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_STATE_TRANSITIONS|O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_STATE_TRANSITIONS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O00_DISTINCTION/O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_TESTS|O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_TESTS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O00_DISTINCTION/O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_WORKFLOWS|O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_WORKFLOWS]]

## Purpose & Definition

O00 Distinction is the **entry point of the cognitive lifecycle** — the foundational act of separating figure from ground, self from other, signal from noise. Without distinction, no downstream operation can proceed because there is no differentiated content to operate on. In AMOS, distinction is the zeroth-order cognitive act that bootstraps the entire O00–O15 lifecycle chain by producing the minimal discriminated units that all subsequent operations consume.

Distinction is governed by the principle that **to observe is to distinguish** — every observation implicitly draws a boundary, and every boundary creates the possibility of relation, object, and state. This operation is both the origin and the terminus of the cycle: O15 Observation feeds back into O00 to re-initiate distinction with updated priors.

## Key Sub-artifacts and Their Roles
See the **Files** section above for the complete list of 20 sub-artifacts. Key artifacts:
| `DEFINITION` | Formal specification of the distinction operation and its semantics |
| `CONTRACT` | Input/output contract binding this operation to the lifecycle chain |
| `PRECONDITIONS` | Conditions that must hold before distinction can execute |
| `POSTCONDITIONS` | Guarantees that hold after distinction completes |
| `INVARIANTS` | Properties preserved across all distinction executions |

*...and remaining artifacts (PROTOCOLS, FAILURE_MODES, HML, GAP_MATRIX, DEPENDENCIES, AGENTS, CONTROL_PLANES, SKILLS, WORKFLOWS, TESTS, RSCF, README) — see Files section.*

## Input/Output Contracts

- **Input:** Raw sensory stream or prior-cycle observation from [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/O15_OBSERVATION_MOC|O15 Observation]]. On the first cycle, input is an unstructured phenomenal field with no prior distinctions.
- **Output:** A set of discriminated tokens — minimal units of difference that carry enough information for O01 Object to identify and constitute objects. Each token includes a boundary descriptor and a salience weight.
- **Contract:** `COGNITIVE_MATRIX_O00_DISTINCTION_CONTRACT` — binds the operation to lifecycle invariants and RSCF provenance.

## Cross-references to Lifecycle Operations

- **Predecessor:** [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/O15_OBSERVATION_MOC|O15 Observation]] — closes the previous cycle and feeds observations back as raw material for re-distinction.
- **Successor:** [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O01_OBJECT/O01_OBJECT_MOC|O01 Object]] — consumes discriminated tokens to constitute identifiable objects.
- **Cycle:** O00 is the head of the O00→O15 cognitive lifecycle. The full chain is: O00→O01→O02→O03→O04→O05→O06→O07→O08→O09→O10→O11→O12→O13→O14→O15→O00.

## Canonical Laws

- **L0 (Distinction Law):** Every cognitive act begins with a distinction; without distinction there is no content. This is the axiomatic root of the AMOS cognitive matrix.
- **L1 (Identity Law):** A distinguished entity maintains identity across the lifecycle until explicitly revised.
- **L7 (Observability Law):** Distinction is itself observable — the act of distinguishing produces a trace that can be inspected by governance and memory operations.
- Applicable laws from the AMOS law stack: L0–L7 foundational, L8–L16 operational, L17–L32 governance-level constraints on distinction authority.

## AMOS Architectural Alignment

O00 Distinction resides in the **25_COGNITIVE_MATRIX** plane, specifically under `02_LIFECYCLE_OPERATIONS`. It aligns with the 25-plane MECE architecture as the first lifecycle operation in the cognitive matrix. The distinction operation is cross-cut by control planes including [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C01_GOVERNANCE/C01_GOVERNANCE_MOC|C01 Governance]] (authority to distinguish), [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C07_PERCEPTION/C07_PERCEPTION_MOC|C07 Perception]] (sensory input to distinction), and [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C05_REPRESENTATION/C05_REPRESENTATION_MOC|C05 Representation]] (how distinctions are encoded).

## Implementation Status and Open Questions

- **Status:** `DERIVED` — the distinction operation is specified in the AMOS corpus but does not have independently verified executable closure. `DOCUMENTED != IMPLEMENTED`.
- **Open questions:** How are distinction boundaries computed in the presence of continuous sensory fields? What is the minimal sufficient distinction for bootstrapping the lifecycle? How does distinction handle adversarial inputs designed to corrupt boundary detection?
- **Gaps:** See `GAP_MATRIX` sub-artifact for the full gap inventory.

## Related Skills, Agents & Workflows

- **Skills:** `amos-distinction-engine`, `amos-perception-binding`, `amos-salience-detection`
- **Agents:** `amos-distinction-agent.json`, `amos-perception-agent.json`
- **Workflows:** `amos-distinction-workflow.json`, `amos-cognitive-cycle-bootstrap.json`

## Subdirectories

- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O00_DISTINCTION/00_INDEX/INDEX_O00_DISTINCTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_README|O00 Distinction Index README]] — 00_INDEX

______________________________________________________________________

**Parent:** [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/02_LIFECYCLE_OPERATIONS_MOC|02_LIFECYCLE_OPERATIONS_MOC]]
