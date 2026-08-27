---
title: SKILL
type: skill
name: amos-information-geometry-mapper
description: Information Geometry Mapper — info capability. Use when executing the core capability within this domain. Use when amos-information-theory-master routes to this specialized capability.
parent_skill: amos-information-theory-master
domain: info
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-information-geometry-mapper]
---


# Information Geometry Mapper

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-information-theory-master`
- **Domain**: info
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Information theory engine for Information Geometry Mapper

## When to Use

- When measuring entropy and lacunarity: information content and gaps
- When analyzing information collapse topology and structure
- When controlling information exposure and disclosure
- When mapping information geometry: manifolds and projections
- When the parent skill (`amos-information-theory-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **information_geometry.measure_entropy**: Measure entropy and lacunarity: information content, gaps, and structure
- **information_geometry.analyze_topology**: Analyze information collapse topology: how information condenses and structures
- **information_geometry.control_exposure**: Control information exposure: what is revealed, to whom, and under what conditions
- **information_geometry.map_geometry**: Map information geometry: manifolds, distances, and projections in information space
- **information_geometry.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **information_geometry.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **information_geometry.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 423154ba73eef4b4) for the full vault-sourced domain knowledge (5769 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/misc/M/Money.md` (content_hash: 266ab144bfa15b1c) (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/universe-cosmos/Universe.md` (vault canon, SOURCE_CLAIM)

### Information Geometry Mapper

From Cosmo Brain Money.md: Information Geometry of Dominance with system state manifold, dominance region, fragility metric, curvature, geodesic cost. From Universe.md: Predictability functional for macroscopic inference.

**Information geometry of dominance equations** (AMOS_MODEL):
```
F(x) = 1 / d(x, ∂D)      (fragility metric)
κ = ∇²Φ(x)                (curvature of stability basin)
MC = ∫_γ |dx|             (geodesic migration cost)
∇E                        (entropy gradient)
∇Φ                        (dominance gradient)
D_KL(X||BTC)              (information divergence)
```
- D = dominance region, ∂D = dominance boundary, d(x, ∂D) = distance to boundary
- F(x) = fragility (inverse distance to boundary), κ = curvature, MC = migration cost

**Predictability functional** (from Universe.md):
```
I(t) = E[(∂/∂θ log p_θ(O_t))²]
```
- I(t) = predictability at time t, p_θ = parametric model, O_t = observation at time t

**Mapping protocol**:
1. **Define manifold**: define the system state manifold
2. **Identify regions**: identify dominance and stability regions
3. **Compute distances**: compute distances to boundaries
4. **Compute fragility**: compute fragility metrics
5. **Compute curvature**: compute curvature of stability basins
6. **Compute migration cost**: compute geodesic migration costs
7. **Map**: map the information geometry

**Mapping laws**:
- `GEOMETRY != TOPOLOGY`: geometry measures distances and curvatures; topology measures connectivity
- `INFORMATION != PHYSICAL**: information geometry is about information states; it is not physical geometry
- `FRAGILITY != INSTABILITY**: fragility is proximity to boundary; instability is actual collapse

### Epistemic Boundary

Information geometry mapping is an AMOS_MODEL. It does not prove the manifold is always well-defined, that the equations are empirically validated, or that fragility predicts collapse.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-f