---
title: SKILL
type: skill
name: amos-boundary-scope-master
description: AMOS Boundary & Scope — scope regimes, boundary admission, context continuity, capability bounds. Use for scope analysis, boundary reasoning, or context management.
parent_skill: none
domain: boundary
origin_architect: Trang Phan
epistemic_class: SOURCE_CANON
tags: [note, amos-boundary-scope-master]
---

# L5 Scope, Regime, and Temporal Laws

## Identity

Origin architect and steward: **Trang Phan**.

This is a **parent skill** that consolidates 2 sub-skills into a single domain master.
Following the skill-organizer best practice: fewer, richer skills beat many overlapping ones.
A parent skill with clearly labeled sections is better than 2 separate shallow skills.

**Epistemic class**: SOURCE_CLAIM (vault-sourced from `01_CANON/01_CORE_LAWS/L5_SCOPE_REGIME.md`).

## When to Use

- When evaluating scope boundaries, context continuity, or capability bounds
- When determining whether a query falls inside or outside a declared scope regime
- When managing boundary admission, ingress/egress, and permeability
- When detecting identity drift, scope creep, or context discontinuity
- When a child skill routes a boundary or scope question to this master
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **boundary_scope.evaluate_influence**: Evaluate whether memory may influence a pending action through the AMOS Boundary & Scope consent, provenance, and risk gates.
- **boundary_scope.validate_gates**: Validate AMOS Boundary & Scope decisions against hard partition gates, epistemic class preservation, and consent state requirements.
- **boundary_scope.analyze_state**: Analyze AMOS Boundary & Scope memory state: working, episodic, semantic stores, consolidation, and retrieval graph health.
- **boundary_scope.trace_provenance**: Trace AMOS Boundary & Scope memory entries to source, encoding operation, consolidation history, and field-level lineage.
- **boundary_scope.assess_claim**: Assess AMOS Boundary & Scope memory claims for epistemic class, freshness, contradiction status, and confidence ceiling.
- **boundary_scope.manage_lifecycle**: Manage AMOS Boundary & Scope lifecycle: encode, normalize, admit, consolidate, index, retrieve, filter, update.
- **boundary_scope.detect_drift**: Detect memory drift: stale entries, broken provenance, epistemic class erosion, and context discontinuity.
- **boundary_scope.escalate_gaps**: Escalate AMOS Boundary & Scope memory gaps: flag UNKNOWN/GAP entries, quarantine untrusted data, trigger memory repair.
- **boundary_scope.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Domain Knowledge

> **Source**: `_00_Cosmo brain/misc/B/BOUNDARY_IDENTITY.md` (vault canon, SOURCE_CLAIM, content_hash: f487341d92a82385)

### Boundary Model

`B_i = <Inside, Outside, Ingress, Egress, Permissions, Permeability>`

A boundary is defined by:
- **Inside**: what is within the boundary's scope
- **Outside**: what is outside the boundary's scope
- **Ingress**: rules for admitting new elements
- **Egress**: rules for removing elements
- **Permissions**: what operations are authorized within the boundary
- **Permeability**: degree to which the boundary allows exchange

### Boundary Health

`BoundaryHealth = Integrity × Selectivity × AdaptivePermeability`

- **Integrity**: boundary maintains its identity under perturbation
- **Selectivity**: boundary correctly distinguishes inside from outside
- **AdaptivePermeability**: boundary can adjust permeability without losing identity

### Failure Regimes

- `permeability → 1`: identity leakage (boundary becomes meaningless)
- `permeability → 0`: adaptive rigidity (boundary cannot adapt)

### Identity Drift

Identity drift above tolerance triggers one of:
1. **Clarification**: refine the identity definition
2. **Split**: divide into multiple distinct boundaries
3. **Ontology revision**: update the taxonomy
4. **Merge**: combine with another boundary
5. **Quarantine**: isolate the drifting boundary
6. **Retirement**: decommission the boundary

### Distinction Function

`Distinct(R_i, R_j) = 1` only when a structurally relevant property differs.

Identity is defined by:
- Positive identity conditions (what makes it what it is)
- Negative/exclusion conditions (what makes it not-something-else)
- Invariants (what must remain unchanged)

## Consolidated Sub-Skills (2)

This parent skill consolidates the following sub-skills. Each is a section within this domain:



> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 7da6df099a658e6d) for additional vault-sourced domain knowledge.


> **Reference**: See `references/boundary_identity.md` (content_hash: 1d7f33221b789ce7) for the Boundary Identity (boundary identity, scope boundaries, identity-boundary mapping).

## Provenance

- **Skill**: amos-boundary-scope-master
- **Source**: AMOS_OS Obsidian vault (`/Users/mac/Documents/AMOS_OS`)
- **Vault s
- [[AGENT_TEMPLATE]]
