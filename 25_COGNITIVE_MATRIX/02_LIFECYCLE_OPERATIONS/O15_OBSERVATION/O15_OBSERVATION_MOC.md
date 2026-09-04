---
title: O15 Observation MOC
type: moc
source: 25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION
tags:
  - o15-observation
  - domain/cognitive-matrix
moc: true
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# O15 Observation — Map of Content

**Path:** `25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION`
**Files:** 20 | **Subdirectories:** 1

## Files

- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/COGNITIVE_MATRIX_O15_OBSERVATION_CONTRACT|COGNITIVE_MATRIX_O15_OBSERVATION_CONTRACT]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_AGENTS|O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_AGENTS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_CONTROL_PLANES|O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_CONTROL_PLANES]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_DEFINITION|O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_DEFINITION]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_DEPENDENCIES|O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_DEPENDENCIES]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_FAILURE_MODES|O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_FAILURE_MODES]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_GAP_MATRIX|O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_GAP_MATRIX]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_HML|O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_HML]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_INPUT_OUTPUT|O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_INPUT_OUTPUT]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_INVARIANTS|O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_INVARIANTS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_POSTCONDITIONS|O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_POSTCONDITIONS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_PRECONDITIONS|O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_PRECONDITIONS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_PROTOCOLS|O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_PROTOCOLS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_README|O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_README]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_RSCF|O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_RSCF]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_SEMANTICS|O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_SEMANTICS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_SKILLS|O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_SKILLS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_STATE_TRANSITIONS|O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_STATE_TRANSITIONS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_TESTS|O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_TESTS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_WORKFLOWS|O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_WORKFLOWS]]

## Purpose & Definition

O15 Observation is the **sixteenth and final lifecycle operation** — it observes the effects of actions executed by O14 and the state of the world, producing the raw material for the next cognitive cycle. Observation is the closing act of the cognitive cycle: it captures what happened, compares it to what was predicted, and generates the prediction-error signals that drive learning and model revision.

Observation feeds back into [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O00_DISTINCTION/O00_DISTINCTION_MOC|O00 Distinction]] to re-initiate the cognitive cycle with updated priors. The observation operation is the primary source of ground truth in AMOS — it is where the system's internal models meet external reality. Observation is governed by the principle that observation is never theory-free: every observation is shaped by the observer's current models, expectations, and distinction criteria.

## Key Sub-artifacts and Their Roles
See the **Files** section above for the complete list of 20 sub-artifacts. Key artifacts:
| `DEFINITION` | Formal specification of observation types, sensing modalities, and error metrics |
| `CONTRACT` | Input/output contract binding observation to the lifecycle |
| `PRECONDITIONS` | Requires either executed actions from O14 or an active sensing cycle |
| `POSTCONDITIONS` | Output observations carry timestamps, confidence, and prediction-error signals |
| `INVARIANTS` | Observation integrity: observations must be faithful to the sensed phenomena within sensor limits |

*...and remaining artifacts (PROTOCOLS, FAILURE_MODES, HML, GAP_MATRIX, DEPENDENCIES, AGENTS, CONTROL_PLANES, SKILLS, WORKFLOWS, TESTS, RSCF, README) — see Files section.*

## Input/Output Contracts

- **Input:** Executed actions and effect receipts from [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION/O14_ACTION_MOC|O14 Action]]. Also retrieves predictions from [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O08_PREDICTION/O08_PREDICTION_MOC|O08 Prediction]] for prediction-error computation.
- **Output:** Observation records — timestamped captures of world state with confidence, prediction-error signals, and feedback packets. Fed back to O00 Distinction to re-initiate the cognitive cycle.
- **Contract:** `COGNITIVE_MATRIX_O15_OBSERVATION_CONTRACT` — binds observation to lifecycle invariants.

## Cross-references to Lifecycle Operations

- **Predecessor:** [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION/O14_ACTION_MOC|O14 Action]] — provides executed actions whose effects are observed.
- **Successor:** [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O00_DISTINCTION/O00_DISTINCTION_MOC|O00 Distinction]] — re-initiates the cognitive cycle with observation-informed priors.
- **Prediction feedback:** [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O08_PREDICTION/O08_PREDICTION_MOC|O08 Prediction]] — observations are compared to predictions to generate prediction-error signals.
- **Cycle closure:** O15 is the tail of the O00->O15 cognitive lifecycle. The full cycle is: O00->O01->O02->O03->O04->O05->O06->O07->O08->O09->O10->O11->O12->O13->O14->**O15**->O00.

## Canonical Laws

- **L7 (Observability Law):** Observation itself is observable; the act of observing produces a trace that can be inspected by governance and memory operations.
- **L25 (Prediction-Error Law):** Prediction errors are non-erasable signals that drive model revision; suppression of prediction errors is prohibited.
- **L0 (Distinction Law):** Every observation implicitly draws a boundary; observation and distinction are two aspects of the same cognitive act.
- **L8 (Provenance Law):** Every observation carries provenance metadata linking it to its sensing event and sensor modality.
- Applicable: L0-L16 operational, L17-L32 governance constraints on observation authority and sensor integrity.

## AMOS Architectural Alignment

O15 Observation sits in `02_LIFECYCLE_OPERATIONS` within the 25-plane MECE architecture. It is primarily governed by [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C07_PERCEPTION/C07_PERCEPTION_MOC|C07 Perception]] (sensory processing, sensor fusion) and [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C01_GOVERNANCE/C01_GOVERNANCE_MOC|C01 Governance]] (observation authority). The observation-prediction feedback loop connects O15 to O08, creating the learning dynamic that drives model revision across cycles.

## Implementation Status and Open Questions

- **Status:** `DERIVED` — observation is specified but executable closure is not verified. `DOCUMENTED != IMPLEMENTED`.
- **Open questions:** How are observation biases detected and corrected? What is the sensor fusion policy for conflicting modalities? How are observation gaps (missing data) handled without suppressing prediction errors?
- **Gaps:** See `GAP_MATRIX` sub-artifact for the full inventory.

## Related Skills, Agents & Workflows

- **Skills:** `amos-observation-capture`, `amos-prediction-error`, `amos-sensor-fusion`, `amos-feedback-generation`
- **Agents:** `amos-observation-agent.json`, `amos-perception-agent.json`
- **Workflows:** `amos-observation-cycle.json`, `amos-feedback-loop.json`

## Subdirectories

- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O15_OBSERVATION/00_INDEX/INDEX_O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_README|INDEX_O15_OBSERVATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_README]] — 00_INDEX

______________________________________________________________________

**Parent:** [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/02_LIFECYCLE_OPERATIONS_MOC|02_LIFECYCLE_OPERATIONS_MOC]]
