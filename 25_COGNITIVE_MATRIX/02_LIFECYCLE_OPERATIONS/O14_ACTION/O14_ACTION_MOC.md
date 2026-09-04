---
title: O14 Action MOC
type: moc
source: 25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION
tags:
  - o14-action
  - domain/cognitive-matrix
moc: true
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# O14 Action — Map of Content

**Path:** `25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION`
**Files:** 20 | **Subdirectories:** 1

## Files

- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION/COGNITIVE_MATRIX_O14_ACTION_CONTRACT|COGNITIVE_MATRIX_O14_ACTION_CONTRACT]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION/O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_AGENTS|O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_AGENTS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION/O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_CONTROL_PLANES|O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_CONTROL_PLANES]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION/O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_DEFINITION|O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_DEFINITION]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION/O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_DEPENDENCIES|O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_DEPENDENCIES]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION/O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_FAILURE_MODES|O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_FAILURE_MODES]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION/O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_GAP_MATRIX|O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_GAP_MATRIX]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION/O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_HML|O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_HML]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION/O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_INPUT_OUTPUT|O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_INPUT_OUTPUT]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION/O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_INVARIANTS|O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_INVARIANTS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION/O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_POSTCONDITIONS|O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_POSTCONDITIONS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION/O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_PRECONDITIONS|O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_PRECONDITIONS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION/O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_PROTOCOLS|O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_PROTOCOLS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION/O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_README|O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_README]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION/O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_RSCF|O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_RSCF]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION/O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_SEMANTICS|O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_SEMANTICS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION/O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_SKILLS|O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_SKILLS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION/O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_STATE_TRANSITIONS|O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_STATE_TRANSITIONS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION/O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_TESTS|O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_TESTS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION/O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_WORKFLOWS|O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_WORKFLOWS]]

## Purpose & Definition

O14 Action is the **fifteenth lifecycle operation** — it executes the committed decisions from O13 in the world. Action is the output stage of the cognitive cycle: it translates governed decisions into concrete effects, whether they are physical actions, digital writes, API calls, or communication acts. Every action in AMOS is governed, logged, and reversible (where possible) through the rollback and recovery system.

Actions produce effects that are observed by [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/O15_OBSERVATION_MOC|O15 Observation]], closing the cognitive cycle. The action-observation loop is the primary mechanism by which the system learns from its interventions in the world. Actions are also the primary point of externalization, where the enforcement root attestation (ERA) and enforcement trust contract (ETC) verify that the enforcement chain is trusted before any effect is released.

## Key Sub-artifacts and Their Roles
See the **Files** section above for the complete list of 20 sub-artifacts. Key artifacts:
| `DEFINITION` | Formal specification of action types, execution semantics, and effect contracts |
| `CONTRACT` | Input/output contract binding action execution to the lifecycle |
| `PRECONDITIONS` | Requires a governed decision from O13 with commit metadata and authority chain |
| `POSTCONDITIONS` | Executed actions produce effect receipts with integrity hashes and provenance |
| `INVARIANTS` | Action integrity: no action may execute without governance approval and enforcement trust validation |

*...and remaining artifacts (PROTOCOLS, FAILURE_MODES, HML, GAP_MATRIX, DEPENDENCIES, AGENTS, CONTROL_PLANES, SKILLS, WORKFLOWS, TESTS, RSCF, README) — see Files section.*

## Input/Output Contracts

- **Input:** Governed decisions from [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O13_DECISION/O13_DECISION_MOC|O13 Decision]] with commit metadata, authority chains, and selected plans.
- **Output:** Effect receipts — records of executed actions with integrity hashes, provenance, and observability metadata. Effects are observed by O15 Observation. Failed actions produce rollback records.
- **Contract:** `COGNITIVE_MATRIX_O14_ACTION_CONTRACT` — binds action execution to lifecycle, governance, and enforcement trust invariants.

## Cross-references to Lifecycle Operations

- **Predecessor:** [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O13_DECISION/O13_DECISION_MOC|O13 Decision]] — provides governed decisions for action execution.
- **Successor:** [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/O15_OBSERVATION_MOC|O15 Observation]] — observes the effects of executed actions.
- **Cycle closure:** O14 Action -> O15 Observation -> O00 Distinction (re-entry into the cognitive cycle with updated priors).
- **Chain position:** O00->O01->O02->O03->O04->O05->O06->O07->O08->O09->O10->O11->O12->O13->**O14**->O15

## Canonical Laws

- **L7 (Observability Law):** Action execution and effect production are observable and auditable.
- **L15 (Memory Integrity Law):** Effect receipts are non-erasable; provenance is immutable once recorded.
- **CAPABILITY != REACHABILITY:** The capability to execute an action does not imply reachability to the effect target.
- **ENFORCEMENT != COMMITMENT:** Enforcement of an action is distinct from the commitment to its effect; both must be independently verified.
- **MayExternalize:** 18-term conjunction (v42) or 20-term conjunction (v43) must be satisfied before any action may externalize an effect.
- Applicable: L0-L16 operational, L17-L32 governance constraints. The enforcement root attestation and enforcement trust contract are the primary governance mechanisms at this stage.

## AMOS Architectural Alignment

O14 Action sits in `02_LIFECYCLE_OPERATIONS` within the 25-plane MECE architecture. It is the primary externalization point, governed by [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C01_GOVERNANCE/C01_GOVERNANCE_MOC|C01 Governance]] (action authority) and [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C09_KERNEL_CONTROL/C09_KERNEL_CONTROL_MOC|C09 Kernel Control]] (kernel-level execution safety). The enforcement root attestation (v42+), enforcement trust contract (v43), and release ledger all operate at this lifecycle stage to prevent unauthorized externalization.

## Implementation Status and Open Questions

- **Status:** `DERIVED` — action execution is specified and the enforcement root attestation has 30 self-tests + 300k deterministic fuzz passes, but end-to-end lifecycle integration is not verified. `TEST_SPECIFIED != TEST_EXECUTED` at lifecycle level.
- **Open questions:** How are partial execution failures handled atomically? What is the rollback policy for irreversible actions? How are concurrent actions from multiple agents serialized?
- **Gaps:** See `GAP_MATRIX` sub-artifact for the full inventory. Hardware/root-of-trust compromise remains UNKNOWN/GAP.

## Related Skills, Agents & Workflows

- **Skills:** `amos-rollback-recovery`, `amos-evolution-receipt`, `amos-enforcement-root-attestation`, `amos-audit-trail`, `amos-decision-logger`
- **Agents:** `amos-action-agent.json`, `amos-enforcement-agent.json`
- **Workflows:** `amos-action-execution.json`, `amos-rollback-recovery.json`

## Subdirectories

- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION/00_INDEX/INDEX_O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_README|INDEX_O14_ACTION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_README]] — 00_INDEX

______________________________________________________________________

**Parent:** [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/02_LIFECYCLE_OPERATIONS_MOC|02_LIFECYCLE_OPERATIONS_MOC]]
