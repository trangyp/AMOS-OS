---
title: O13 Decision MOC
type: moc
source: 25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O13_DECISION
tags:
  - o13-decision
  - domain/cognitive-matrix
moc: true
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# O13 Decision — Map of Content

**Path:** `25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O13_DECISION`
**Files:** 20 | **Subdirectories:** 1

## Files

- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O13_DECISION/COGNITIVE_MATRIX_O13_DECISION_CONTRACT|COGNITIVE_MATRIX_O13_DECISION_CONTRACT]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O13_DECISION/O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_AGENTS|O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_AGENTS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O13_DECISION/O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_CONTROL_PLANES|O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_CONTROL_PLANES]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O13_DECISION/O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_DEFINITION|O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_DEFINITION]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O13_DECISION/O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_DEPENDENCIES|O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_DEPENDENCIES]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O13_DECISION/O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_FAILURE_MODES|O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_FAILURE_MODES]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O13_DECISION/O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_GAP_MATRIX|O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_GAP_MATRIX]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O13_DECISION/O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_HML|O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_HML]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O13_DECISION/O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_INPUT_OUTPUT|O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_INPUT_OUTPUT]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O13_DECISION/O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_INVARIANTS|O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_INVARIANTS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O13_DECISION/O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_POSTCONDITIONS|O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_POSTCONDITIONS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O13_DECISION/O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_PRECONDITIONS|O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_PRECONDITIONS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O13_DECISION/O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_PROTOCOLS|O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_PROTOCOLS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O13_DECISION/O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_README|O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_README]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O13_DECISION/O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_RSCF|O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_RSCF]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O13_DECISION/O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_SEMANTICS|O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_SEMANTICS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O13_DECISION/O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_SKILLS|O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_SKILLS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O13_DECISION/O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_STATE_TRANSITIONS|O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_STATE_TRANSITIONS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O13_DECISION/O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_TESTS|O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_TESTS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O13_DECISION/O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_WORKFLOWS|O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_WORKFLOWS]]

## Purpose & Definition

O13 Decision is the **fourteenth lifecycle operation** — it selects among the plans produced by O12 and commits to a specific course of action. Decision is the cognitive act of commitment: it transforms a set of possibilities into a single chosen path. In AMOS, decisions are not arbitrary selections; they are governed by the capability-bound governance kernel (v4.8) which enforces mutation classification (M0-M5), burden computation, mandatory gates, and non-compensatory refusals.

Decisions carry authority — they authorize the transition from planning to execution. A decision in AMOS is a governed commit: it includes the selected plan, the governance verdict, the authority chain, and the proof-carrying commit metadata. Decisions feed directly into [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION/O14_ACTION_MOC|O14 Action]] for execution.

## Key Sub-artifacts and Their Roles
See the **Files** section above for the complete list of 20 sub-artifacts. Key artifacts:
| `DEFINITION` | Formal specification of decision types, governance rules, and commit semantics |
| `CONTRACT` | Input/output contract binding decision to the lifecycle |
| `PRECONDITIONS` | Requires validated plans from O12 with feasibility and risk assessments |
| `POSTCONDITIONS` | Output decisions carry governance verdict, authority chain, and commit metadata |
| `INVARIANTS` | Decision integrity: decisions must be governance-approved before execution |

*...and remaining artifacts (PROTOCOLS, FAILURE_MODES, HML, GAP_MATRIX, DEPENDENCIES, AGENTS, CONTROL_PLANES, SKILLS, WORKFLOWS, TESTS, RSCF, README) — see Files section.*

## Input/Output Contracts

- **Input:** Validated plans from [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O12_PLAN/O12_PLAN_MOC|O12 Plan]] with feasibility, risk, and resource assessments.
- **Output:** Governed decisions — selected plans with governance verdicts, authority chains, mutation classifications, and proof-carrying commit metadata. Registered for O14 Action execution.
- **Contract:** `COGNITIVE_MATRIX_O13_DECISION_CONTRACT` — binds decision to lifecycle and governance invariants.

## Cross-references to Lifecycle Operations

- **Predecessor:** [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O12_PLAN/O12_PLAN_MOC|O12 Plan]] — provides validated plans for decision selection.
- **Successor:** [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O14_ACTION/O14_ACTION_MOC|O14 Action]] — executes the committed decision.
- **Chain position:** O00->O01->O02->O03->O04->O05->O06->O07->O08->O09->O10->O11->O12->**O13**->O14->O15

## Canonical Laws

- **L7 (Observability Law):** Decision evaluation and commitment are observable and auditable.
- **L17 (Model Provenance Law):** Decisions carry provenance linking them to their source plans and governance verdicts.
- **L31 (Value Contestability Law):** Decision alternatives must be preserved until discriminating governance evidence exists.
- **CAPABILITY != AUTHORITY:** The system's capability to execute a plan does not grant authority to commit; authority requires governance approval.
- **PROPOSAL != COMMIT:** A plan proposal is not a commit without governance approval and proof-carrying metadata.
- Applicable: L0-L16 operational, L17-L32 governance constraints. The 8 mandatory gates and 6 non-compensatory refusals from the decision protocol are enforced here.

## AMOS Architectural Alignment

O13 Decision sits in `02_LIFECYCLE_OPERATIONS` within the 25-plane MECE architecture. It is the primary touchpoint for [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C01_GOVERNANCE/C01_GOVERNANCE_MOC|C01 Governance]] (authority, policy, decision rules) and [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C09_KERNEL_CONTROL/C09_KERNEL_CONTROL_MOC|C09 Kernel Control]] (kernel-level enforcement). The AMOS capability-bound governance kernel (v4.8), enforcement root attestation (v42+), and enforcement trust contract (v43) all operate at this lifecycle stage.

## Implementation Status and Open Questions

- **Status:** `DERIVED` — decision governance is specified and the enforcement root attestation has 30 self-tests, but end-to-end lifecycle integration is not verified. `TEST_SPECIFIED != TEST_EXECUTED` at lifecycle level.
- **Open questions:** How are decision deadlocks resolved in multi-agent settings? What is the escalation path for M0-M2 mutations? How are rollback decisions triggered and executed?
- **Gaps:** See `GAP_MATRIX` sub-artifact for the full inventory.

## Related Skills, Agents & Workflows

- **Skills:** `amos-capability-bound-governance`, `amos-validation-pipeline`, `amos-evolution-receipt`, `amos-decision-logger`, `amos-audit-trail`
- **Agents:** `amos-decision-agent.json`, `amos-governance-agent.json`
- **Workflows:** `amos-decision-evaluation.json`, `amos-governance-commit.json`

## Subdirectories

- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O13_DECISION/00_INDEX/INDEX_O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_README|INDEX_O13_DECISION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_README]] — 00_INDEX

______________________________________________________________________

**Parent:** [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/02_LIFECYCLE_OPERATIONS_MOC|02_LIFECYCLE_OPERATIONS_MOC]]
