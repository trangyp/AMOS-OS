---
title: 21 Simulation Modes MOC
type: moc
source: 03_CONTROL_PLANE/09_COMMIT/21_SIMULATION_MODES
tags:
  - 21-simulation-modes
  - canon/control-plane
moc: true
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# 21 Simulation Modes — Map of Content

**Path:** `03_CONTROL_PLANE/09_COMMIT/21_SIMULATION_MODES`
**Files:** 3 | **Subdirectories:** 0

## Purpose

Simulation modes run forward models of system state to predict commit outcomes, enabling the orchestrator to evaluate candidate commits against simulated futures before finalization. These modes define the operational patterns that the commit orchestrator activates when a commit phase requires predictive evaluation — running the commit's effects through a simulation layer to assess consequences, detect potential conflicts, and estimate resource impact before the commit is externalized. They ensure that commits with high consequence or irreversibility scores are evaluated against simulated futures, providing the governance kernel with predictive evidence to inform its approval decision.

## MECE Domain

This mode belongs to the B — Execution Core & Effect Governance MECE domain, within the 03_CONTROL_PLANE/09_COMMIT sub-plane.

## Files

- [[03_CONTROL_PLANE/09_COMMIT/21_SIMULATION_MODES/SIMULATION_MODES_COMMIT_CONTROL_PLANE_MODE_FAMILY_REGISTRY|SIMULATION_MODES_COMMIT_CONTROL_PLANE_MODE_FAMILY_REGISTRY]] — Catalogs all simulation modes with their activation criteria, simulation-depth invariants, and model-fidelity transition rules.
- [[03_CONTROL_PLANE/09_COMMIT/21_SIMULATION_MODES/SIMULATION_MODES_COMMIT_CONTROL_PLANE_MODE_FAMILY_SPEC|SIMULATION_MODES_COMMIT_CONTROL_PLANE_MODE_FAMILY_SPEC]] — Defines the formal properties, preconditions, postconditions, and safety invariants for each simulation mode, including simulation fidelity and prediction-confidence thresholds.
- [[03_CONTROL_PLANE/09_COMMIT/21_SIMULATION_MODES/SIMULATION_MODES_COMMIT_CONTROL_PLANE_README|SIMULATION_MODES_COMMIT_CONTROL_PLANE_README]] — Provides an overview of the simulation mode family, its role in predictive commit evaluation, and integration guidance for the commit orchestrator.

## Mode Behavior

Simulation modes activate when the commit orchestrator enters a phase that requires predictive evaluation — typically for commits with consequence > 0.35 or irreversibility > 0.20, or when the governance kernel requests forward-model evidence. The mode governs the execution of the simulation layer: selecting the appropriate simulation depth, running the forward model against the current world model state, and collecting prediction results including estimated consequences, conflict probabilities, and resource impact. The mode blocks any commit whose simulation results indicate unacceptable consequences, and it blocks commits where simulation fidelity is insufficient to support a governance decision. Mode exit occurs when simulation results are delivered to the governance kernel and the commit transitions to the authorization phase.

## Relationships

- **Parent:** [[03_CONTROL_PLANE/09_COMMIT/09_COMMIT_MOC|09_COMMIT_MOC]]
- **Mode Index:** [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/00_MODE_INDEX_MOC|00_MODE_INDEX_MOC]]
- **GMEF Law:** [[01_CANON/01_CORE_LAWS/L18_GMEF|L18_GMEF]] — GMEF gate compliance for mode activation
- **Related Family — World Model Modes:** [[03_CONTROL_PLANE/09_COMMIT/12_WORLD_MODEL_MODES/12_WORLD_MODEL_MODES_MOC|12_WORLD_MODEL_MODES_MOC]]
- **Related Family — Counterfactual Modes:** [[03_CONTROL_PLANE/09_COMMIT/22_COUNTERFACTUAL_MODES/22_COUNTERFACTUAL_MODES_MOC|22_COUNTERFACTUAL_MODES_MOC]]
- **Related Family — Validation Modes:** [[03_CONTROL_PLANE/09_COMMIT/26_VALIDATION_MODES/26_VALIDATION_MODES_MOC|26_VALIDATION_MODES_MOC]]

## Commit Phase Integration

This mode family integrates into the AMOS commit lifecycle during the predictive evaluation phase — typically after pre-commit validation but before authorization. The orchestrator activates the appropriate simulation mode, which runs the forward model against the current world model state and collects prediction results. The simulation results are delivered to the governance kernel as evidence inputs for the authorization decision. The mode ensures that simulation depth and fidelity are appropriate for the commit's consequence and irreversibility scores before the commit proceeds to finalization.

## Epistemic Boundary

`DOCUMENTED != IMPLEMENTED` — The simulation mode family is structurally documented in the vault corpus, but its executable forward-model simulation mechanisms in a deployed runtime are not established merely by documentation presence.

`CAPABILITY != AUTHORITY` — The simulation mode family describes capability patterns for predictive commit evaluation; it does not by itself authorize or block commits. Simulation results are evidence inputs to the governance kernel, not authoritative decisions.
