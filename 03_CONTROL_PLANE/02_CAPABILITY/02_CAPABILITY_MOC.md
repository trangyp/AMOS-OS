---
title: 02 Capability MOC
type: moc
source: 03_CONTROL_PLANE/02_CAPABILITY
tags:
  - 02-capability
  - canon/control-plane
  - capability-manifest
  - capability-resolver
moc: true
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# 02 Capability — Map of Content

## Purpose

The Capability sub-plane governs how **capabilities** — typed, scoped, revocable permissions to perform consequential operations — are declared, discovered, resolved, and admitted within the AMOS OS control plane. A capability is not authority; it is a bounded permission envelope that must be combined with identity, policy, and commit-time freshness to authorize an effect. This sub-plane enforces the separability law: `CAPABILITY != REACHABILITY != IDENTITY != AUTHORITY`. No agent acquires durable-effect authority merely by holding a capability.

## MECE Domain

This sub-plane belongs to the **B — Execution Core & Effect Governance** MECE domain (plane `03_CONTROL_PLANE`). The Control Plane owns authorization, semantic transaction, commit-time revalidation, and finality eligibility. Capability admission is the first gate in the effect-governance pipeline: before any effect is committed, the requesting agent's capability must be resolved against the manifest, validated against policy, and bound to an authority witness.

**Path:** `03_CONTROL_PLANE/02_CAPABILITY`
**Files:** 4 | **Subdirectories:** 1

## Files

- [[03_CONTROL_PLANE/02_CAPABILITY/CAPABILITY_CONTROL_PLANE_README|CAPABILITY_CONTROL_PLANE_README]] — Package readme for the Capability sub-plane. Describes the structural layout, file inventory, and governance role of this segment within the Control Plane.
- [[03_CONTROL_PLANE/02_CAPABILITY/CAPABILITY_MANIFEST|CAPABILITY_MANIFEST]] — Defines the AMOS OS manifest structure for discovering, indexing, resolving, validating, governing, versioning, and auditing capabilities. The manifest is the authoritative registry of all declared capabilities, their scopes, attenuation chains, and lifecycle states.
- [[03_CONTROL_PLANE/02_CAPABILITY/CAPABILITY_RESOLVER|CAPABILITY_RESOLVER]] — The resolver maps a requested operation to a concrete capability grant at runtime. It performs scope matching, attenuation validation, temporal validity checks, and delegation-chain verification before returning a resolved capability or failing closed.
- [[03_CONTROL_PLANE/02_CAPABILITY/CONTROL_PLANE_CAPABILITY_CONTRACT|CONTROL_PLANE_CAPABILITY_CONTRACT]] — The governed contract defining how a capability may be represented, discovered, selected, invoked, supervised, validated, revoked, and audited. This is the canonical interface contract between capability holders and the control-plane enforcement chain.

## Subdirectories

- [[03_CONTROL_PLANE/02_CAPABILITY/00_INDEX/CAPABILITY_MAP|CAPABILITY_MAP]] — `00_INDEX` subdirectory containing the structural navigation map for the Capability sub-plane.

## Capability Admission Pipeline

The capability admission flow within the control plane operates as follows:

1. **Declaration** — A capability is declared in the `CAPABILITY_MANIFEST` with its scope, effect class, attenuation rules, and delegation parent.
2. **Resolution** — At runtime, `CAPABILITY_RESOLVER` maps the agent's request to a matching capability grant, checking temporal validity and delegation chain integrity.
3. **Policy Binding** — The resolved capability is passed to [[03_CONTROL_PLANE/03_POLICY/03_POLICY_MOC|03 Policy MOC]] for policy evaluation against active governance rules.
4. **Authority Witness** — The capability is bound to an authority witness from [[03_CONTROL_PLANE/04_AUTHORITY/04_AUTHORITY_MOC|04 Authority MOC]] to establish that the holder is authorized, not merely capable.
5. **Effect Gating** — The bound capability-authority pair is presented to [[03_CONTROL_PLANE/08_EFFECTS/08_EFFECTS_MOC|08 Effects MOC]] for effect-intent validation before release.

## Relationships

- **Parent**: [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03 Control Plane MOC]] — the parent plane that governs all effect-gating surfaces.
- **Policy**: [[03_CONTROL_PLANE/03_POLICY/03_POLICY_MOC|03 Policy MOC]] — evaluates whether a resolved capability is permitted under active policy.
- **Authority**: [[03_CONTROL_PLANE/04_AUTHORITY/04_AUTHORITY_MOC|04 Authority MOC]] — binds identity and delegation witnesses to capabilities.
- **Effects**: [[03_CONTROL_PLANE/08_EFFECTS/08_EFFECTS_MOC|08 Effects MOC]] — consumes resolved capabilities for effect-intent gating.
- **Provenance**: [[03_CONTROL_PLANE/05_PROVENANCE/05_PROVENANCE_MOC|05 Provenance MOC]] — records the capability resolution chain as provenance evidence.
- **Cognitive Organism**: [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05 Cognitive Organism MOC]] — agents that hold and exercise capabilities.
- **Architecture**: [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|Full Brain OS MECE Architecture]] — assigns `03_CONTROL_PLANE` to the execution core domain.

## Epistemic Boundary

Capability admission is an AMOS_MODEL artifact with canonical status CONDITIONAL and implementation PARTIAL. The manifest, resolver, and contract are structurally present but do not by themselves prove that a deployed runtime enforces capability checks at every effect boundary. The separability law (`CAPABILITY != AUTHORITY`) is a normative invariant, not an empirical guarantee. End-to-end capability enforcement requires independent evidence that the enforcement chain (refmon, runtime, egress guard) is the same trusted chain to which the capability was issued.

______________________________________________________________________

**Parent:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
