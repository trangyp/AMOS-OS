---
title: 08 Effects MOC
type: moc
source: 03_CONTROL_PLANE/08_EFFECTS
tags:
  - 08-effects
  - canon/control-plane
  - effect-intent
  - effect-manifest
  - effect-release-state
moc: true
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# 08 Effects — Map of Content

## Purpose

The Effects sub-plane governs the **lifecycle of consequential external effects** within the AMOS OS control plane. An effect is any state transition that crosses the system boundary — a write to external storage, an API call, a physical actuation, a message sent to an external agent. The Effects sub-plane ensures that no effect is released unless it has passed through the full governance pipeline: task contract, capability resolution, policy evaluation, authority witness, provenance capture, and commit-time freshness revalidation. The separability law requires: `ENFORCEMENT != CONSEQUENCE`. An effect may be enforcement-approved but still have unintended consequences; the effect manifest bounds the consequence space.

## MECE Domain

This sub-plane belongs to the **B — Execution Core & Effect Governance** MECE domain (plane `03_CONTROL_PLANE`). Effects is the final gate before a consequential action reaches the commit subsystem. It transforms an authorized intention into a bounded, manifest-validated, release-state-tracked effect that the commit gate can finalize or reject. Without this gate, authority and policy decisions would be unbound from the actual effect they authorize — the enforcement root attestation requires that the effect intent, release state, and enforcement chain are all independently verified.

**Path:** `03_CONTROL_PLANE/08_EFFECTS`
**Files:** 5 | **Subdirectories:** 1

## Files

- [[03_CONTROL_PLANE/08_EFFECTS/CONTROL_PLANE_EFFECTS_CONTRACT|CONTROL_PLANE_EFFECTS_CONTRACT]] — The governed contract defining how effects are declared, intent-validated, manifest-bound, release-state-tracked, and committed. Specifies the interface between the effects sub-plane and the commit, observability, and rollback subsystems. AMOS_MODEL; canonical status CONDITIONAL; implementation PARTIAL.
- [[03_CONTROL_PLANE/08_EFFECTS/EFFECTS_CONTROL_PLANE_README|EFFECTS_CONTROL_PLANE_README]] — Package readme for the Effects sub-plane. Describes the structural layout, file inventory, and governance role within the Control Plane.
- [[03_CONTROL_PLANE/08_EFFECTS/EFFECT_INTENT|EFFECT_INTENT]] — The declared intention of a consequential action: what state surfaces it will modify, what external systems it will contact, what effect class it belongs to, and what preconditions must hold. The intent is validated against the capability manifest and policy before any release state is created. AMOS_MODEL; CONDITIONAL; implementation PARTIAL.
- [[03_CONTROL_PLANE/08_EFFECTS/EFFECT_MANIFEST|EFFECT_MANIFEST]] — The manifest of all declared effect classes, their scopes, their consequence bounds, and their required governance gates. The manifest is the authoritative registry of what kinds of effects the system may produce and what validation each kind requires. AMOS_MODEL; CONDITIONAL; implementation PARTIAL.
- [[03_CONTROL_PLANE/08_EFFECTS/EFFECT_RELEASE_STATE|EFFECT_RELEASE_STATE]] — The tracked state of an effect after it has been released but before it is committed. The release state records whether the effect is pending, in-flight, committed, rolled back, or failed. This is the object that the enforcement root attestation binds to the enforcement chain measurement. AMOS_MODEL; CONDITIONAL; implementation PARTIAL.

## Subdirectories

- [[03_CONTROL_PLANE/08_EFFECTS/00_INDEX/EFFECTS_MAP|EFFECTS_MAP]] — `00_INDEX` subdirectory containing the structural navigation map for the Effects sub-plane.

## Effect Lifecycle in the Governance Pipeline

The effect lifecycle within the control plane operates as follows:

1. **Intent declaration** — An agent declares an `EFFECT_INTENT` specifying the target state surfaces, effect class, and preconditions.
2. **Manifest validation** — The intent is validated against the `EFFECT_MANIFEST` to confirm the effect class is declared and the consequence bounds are within scope.
3. **Capability binding** — The resolved capability from [[03_CONTROL_PLANE/02_CAPABILITY/02_CAPABILITY_MOC|02 Capability MOC]] is bound to the intent.
4. **Policy evaluation** — The bound intent is evaluated by [[03_CONTROL_PLANE/03_POLICY/03_POLICY_MOC|03 Policy MOC]] for governance compliance.
5. **Authority witness** — An authority witness from [[03_CONTROL_PLANE/04_AUTHORITY/04_AUTHORITY_MOC|04 Authority MOC]] attests that the holder is authorized.
6. **Release state creation** — Upon passing all gates, an `EFFECT_RELEASE_STATE` is created, binding the intent to the enforcement chain measurement.
7. **Commit** — The release state is presented to [[03_CONTROL_PLANE/09_COMMIT/09_COMMIT_MOC|09 Commit MOC]] for finality.

## Relationships

- **Parent**: [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03 Control Plane MOC]] — the parent plane governing all effect-gating surfaces.
- **Capability**: [[03_CONTROL_PLANE/02_CAPABILITY/02_CAPABILITY_MOC|02 Capability MOC]] — resolves the capability bound to the effect intent.
- **Policy**: [[03_CONTROL_PLANE/03_POLICY/03_POLICY_MOC|03 Policy MOC]] — evaluates whether the effect intent is permitted.
- **Authority**: [[03_CONTROL_PLANE/04_AUTHORITY/04_AUTHORITY_MOC|04 Authority MOC]] — provides the authority witness for the effect.
- **Commit**: [[03_CONTROL_PLANE/09_COMMIT/09_COMMIT_MOC|09 Commit MOC]] — finalizes the effect release state.
- **Observability**: [[03_CONTROL_PLANE/07_OBSERVABILITY/07_OBSERVABILITY_MOC|07 Observability MOC]] — monitors the effect release state for commit-time revalidation.
- **Rollback**: [[03_CONTROL_PLANE/12_ROLLBACK/12_ROLLBACK_MOC|12 Rollback MOC]] — uses effect release state for rollback eligibility.
- **Architecture**: [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|Full Brain OS MECE Architecture]] — assigns `03_CONTROL_PLANE` to the execution core domain.

## Epistemic Boundary

Effects artifacts are AMOS_MODEL with canonical status CONDITIONAL and implementation PARTIAL. The intent, manifest, and release state are structurally present but do not by themselves prove that a deployed runtime enforces the full effect lifecycle at every boundary. The enforcement root attestation (v42+) requires that the currently executing enforcement chain is independently identified and measured — an effect cannot become authoritative merely because AMOS approved it. `ENFORCEMENT != CONSEQUENCE` — even a fully governed effect may produce unintended consequences in the external world; the manifest bounds but does not eliminate consequence risk.

______________________________________________________________________

**Parent:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
