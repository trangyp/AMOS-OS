---
title: 09 Governance Modes MOC
type: moc
source: 03_CONTROL_PLANE/09_COMMIT/09_GOVERNANCE_MODES
tags:
  - 09-governance-modes
  - canon/control-plane
moc: true
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# 09 Governance Modes — Map of Content

**Path:** `03_CONTROL_PLANE/09_COMMIT/09_GOVERNANCE_MODES`
**Files:** 3 | **Subdirectories:** 0

## Purpose

Governance modes define the authoritative decision-making patterns that the commit orchestrator uses to approve, defer, or reject commits during the commit lifecycle. These modes encode the governance rules, authority envelopes, and capability-bound checks that determine whether a commit may proceed to finalization. They serve as the primary control surface through which the AMOS capability-bound governance kernel (v4.8) exerts its authority over commit-time mutations, ensuring that every commit satisfies the 8 mandatory gates and 6 non-compensatory refusals before being externalized.

## MECE Domain

This mode belongs to the B — Execution Core & Effect Governance MECE domain, within the 03_CONTROL_PLANE/09_COMMIT sub-plane.

## Files

- [[03_CONTROL_PLANE/09_COMMIT/09_GOVERNANCE_MODES/GOVERNANCE_MODES_COMMIT_CONTROL_PLANE_MODE_FAMILY_REGISTRY|GOVERNANCE_MODES_COMMIT_CONTROL_PLANE_MODE_FAMILY_REGISTRY]] — Catalogs all governance modes in this family with their activation criteria, invariants, transition rules, and authority envelope boundaries.
- [[03_CONTROL_PLANE/09_COMMIT/09_GOVERNANCE_MODES/GOVERNANCE_MODES_COMMIT_CONTROL_PLANE_MODE_FAMILY_SPEC|GOVERNANCE_MODES_COMMIT_CONTROL_PLANE_MODE_FAMILY_SPEC]] — Defines the formal properties, preconditions, postconditions, and safety invariants for each governance mode in the family.
- [[03_CONTROL_PLANE/09_COMMIT/09_GOVERNANCE_MODES/GOVERNANCE_MODES_COMMIT_CONTROL_PLANE_README|GOVERNANCE_MODES_COMMIT_CONTROL_PLANE_README]] — Provides an overview of the governance mode family, its role in the commit lifecycle, and integration guidance for the commit orchestrator.

## Mode Behavior

Governance modes activate when the commit orchestrator enters a phase that requires authoritative decision-making — typically during the pre-commit validation and authorization phases. Each mode governs a specific governance pattern: strict-gate enforcement, delegated authority, capability-bound checks, or escalation routing. The mode evaluates the commit against its governance rules and produces one of three outcomes: APPROVED (commit may proceed), DEFERRED (commit awaits additional evidence or authority), or BLOCKED (commit fails a non-compensatory refusal). Governance modes block any commit that exceeds the autonomous envelope (depth > 2, consequence > 0.35, irreversibility > 0.20) without explicit escalation, and they block all M0-class mutations unconditionally. Mode exit occurs when the governance decision is recorded and the commit transitions to the next lifecycle phase.

## Relationships

- **Parent:** [[03_CONTROL_PLANE/09_COMMIT/09_COMMIT_MOC|09_COMMIT_MOC]]
- **Mode Index:** [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/00_MODE_INDEX_MOC|00_MODE_INDEX_MOC]]
- **GMEF Law:** [[01_CANON/01_CORE_LAWS/L18_GMEF|L18_GMEF]] — GMEF gate compliance for mode activation
- **Control Plane Contract:** [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|CONTROL_PLANE_CONTROL_PLANE_CONTRACT]]
- **Related Family — Validation Modes:** [[03_CONTROL_PLANE/09_COMMIT/26_VALIDATION_MODES/26_VALIDATION_MODES_MOC|26_VALIDATION_MODES_MOC]]
- **Related Family — Scope Regime Modes:** [[03_CONTROL_PLANE/09_COMMIT/25_SCOPE_REGIME_MODES/25_SCOPE_REGIME_MODES_MOC|25_SCOPE_REGIME_MODES_MOC]]

## Commit Phase Integration

This mode family integrates into the AMOS commit lifecycle during the pre-commit authorization phase. When a commit enters a phase that requires governance decision-making, the orchestrator activates the appropriate governance mode, which evaluates the commit against its rule set and produces an APPROVED, DEFERRED, or BLOCKED outcome. The governance decision is recorded as a commit-time receipt with full provenance, ensuring auditability and replay capability. All governance gate evaluations must complete before the commit proceeds to finalization.

## Epistemic Boundary

`DOCUMENTED != IMPLEMENTED` — The governance mode family is structurally documented in the vault corpus, but its executable enforcement in a deployed runtime is not established merely by documentation presence.

`CAPABILITY != AUTHORITY` — The governance mode family describes capability patterns for commit-time decision-making; it does not by itself confer authority to any agent or system. Authority must be independently established through the enforcement root attestation and delegation witness chain.
