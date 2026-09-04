---
title: 05 Provenance MOC
type: moc
source: 03_CONTROL_PLANE/05_PROVENANCE
tags:
  - 05-provenance
  - canon/control-plane
  - observed-read-set
  - provenance-ledger
  - read-set-validator
moc: true
rscf:
  state: DERIVED
  claim_class: EMPIRICAL
  provenance: AMOS_corpus
  scope: AMOS_general
---

# 05 Provenance — Map of Content

## Purpose

The Provenance sub-plane governs the **evidence chain** of the AMOS OS control plane. It records what was read, what was observed, what authority issued each decision, and what lineage connects a committed effect to its source claims. Provenance is the substrate that makes commit-time revalidation, replay, and rollback possible: without a verified read set and a tamper-evident ledger, the control plane cannot determine whether a committed effect remains valid or must be invalidated. The separability law requires: `PROVENANCE != AUTHORITY`. A provenance record establishes *what happened*, not *whether it was permitted* — permission is the domain of policy and authority.

## MECE Domain

This sub-plane belongs to the **B — Execution Core & Effect Governance** MECE domain (plane `03_CONTROL_PLANE`). Provenance sits at the center of the control-plane pipeline: it captures the read set before effect execution, validates it at commit time, and preserves the full lineage for post-commit audit, replay, and rollback. The provenance ledger is the durable evidence substrate that connects every committed effect to its causal history.

**Path:** `03_CONTROL_PLANE/05_PROVENANCE`
**Files:** 5 | **Subdirectories:** 1

## Files

- [[03_CONTROL_PLANE/05_PROVENANCE/CONTROL_PLANE_PROVENANCE_CONTRACT|CONTROL_PLANE_PROVENANCE_CONTRACT]] — The governed contract defining how provenance records are created, structured, validated, stored, queried, and invalidated. Specifies the interface between the provenance ledger and the commit, replay, and rollback subsystems. AMOS_MODEL; canonical status CONDITIONAL; implementation PARTIAL.
- [[03_CONTROL_PLANE/05_PROVENANCE/OBSERVED_READ_SET|OBSERVED_READ_SET]] — Defines the structure of a read set captured before effect execution: the set of state surfaces, their versions, and their observation timestamps. The read set is the precondition evidence that the commit gate revalidates to determine freshness. AMOS_MODEL; CONDITIONAL; implementation PARTIAL.
- [[03_CONTROL_PLANE/05_PROVENANCE/PROVENANCE_CONTROL_PLANE_README|PROVENANCE_CONTROL_PLANE_README]] — Package readme for the Provenance sub-plane. Describes the structural layout, file inventory, and governance role within the Control Plane.
- [[03_CONTROL_PLANE/05_PROVENANCE/PROVENANCE_LEDGER|PROVENANCE_LEDGER]] — The tamper-evident append-only ledger that records every provenance entry: read sets, authority witnesses, capability resolutions, policy decisions, and commit receipts. The ledger is the durable evidence substrate for audit, replay, and rollback. AMOS_MODEL; CONDITIONAL; implementation PARTIAL.
- [[03_CONTROL_PLANE/05_PROVENANCE/READ_SET_VALIDATOR|READ_SET_VALIDATOR]] — The validator that checks whether a captured read set remains valid at commit time. It compares the observed versions against current state to detect concurrent mutations that would invalidate the effect's preconditions. If validation fails, the commit gate blocks the effect. AMOS_MODEL; CONDITIONAL; implementation PARTIAL.

## Subdirectories

- [[03_CONTROL_PLANE/05_PROVENANCE/00_INDEX/PROVENANCE_MAP|PROVENANCE_MAP]] — `00_INDEX` subdirectory containing the structural navigation map for the Provenance sub-plane.

## Provenance in the Effect-Governance Pipeline

Provenance interacts with the control-plane pipeline at four critical stages:

1. **Pre-execution capture** — Before an effect is executed, the `OBSERVED_READ_SET` captures the state surfaces the effect depends on, with their versions and observation timestamps.
2. **Commit-time revalidation** — At commit time, the `READ_SET_VALIDATOR` checks whether the captured read set is still valid. If any observed state has been mutated by a concurrent transaction, the commit is blocked.
3. **Ledger append** — Upon successful commit, the full provenance record (read set, authority witness, capability chain, policy decision, commit receipt) is appended to the `PROVENANCE_LEDGER`.
4. **Post-commit query** — The ledger is queryable by replay, rollback, and audit subsystems to reconstruct causal history and determine safe recovery points.

## Relationships

- **Parent**: [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03 Control Plane MOC]] — the parent plane governing all effect-gating surfaces.
- **Commit**: [[03_CONTROL_PLANE/09_COMMIT/09_COMMIT_MOC|09 Commit MOC]] — consumes read-set validation results for finality eligibility.
- **Observability**: [[03_CONTROL_PLANE/07_OBSERVABILITY/07_OBSERVABILITY_MOC|07 Observability MOC]] — provides the monitor data that feeds into provenance records.
- **Replay**: [[03_CONTROL_PLANE/11_REPLAY/11_REPLAY_MOC|11 Replay MOC]] — uses the provenance ledger for deterministic replay.
- **Rollback**: [[03_CONTROL_PLANE/12_ROLLBACK/12_ROLLBACK_MOC|12 Rollback MOC]] — uses provenance lineage to determine safe rollback basins.
- **Semantic Transaction**: [[03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/06_SEMANTIC_TRANSACTION_MOC|06 Semantic Transaction MOC]] — records parameter provenance for multi-RSCF transactions.
- **Architecture**: [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|Full Brain OS MECE Architecture]] — assigns `03_CONTROL_PLANE` to the execution core domain.

## Epistemic Boundary

Provenance artifacts are AMOS_MODEL with canonical status CONDITIONAL and implementation PARTIAL. The ledger, read set, and validator are structurally present but do not by themselves prove that a deployed runtime captures complete read sets for every effect or that the ledger is truly tamper-evident under adversarial access. `PROVENANCE != AUTHORITY` — a provenance record establishes what occurred, not whether it was permitted. Permission requires separate policy and authority binding. The `claim_class: EMPIRICAL` on this MOC reflects that provenance records, when they exist, are observations of actual system state, not derived models.

______________________________________________________________________

**Parent:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
