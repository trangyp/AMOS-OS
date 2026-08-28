---
title: SKILL — Amos Information Geometry Mapper
type: skill
source: 07_SKILLS/amos-information-geometry-mapper
name: amos-information-geometry-mapper
description: Information Geometry Mapper — info capability. Use when executing the core capability within this domain. Use when amos-information-theory-master routes to this specialized capability. Do not use for generic tasks outside info domain.
parent_skill: amos-information-theory-master
domain: info
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/information-theory
- rscf/source_claim
- hml/m
- epistemic/source_claim
- amos_os
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
rscf_state: SOURCE_CLAIM
hml_level: M
gmef_gates:
- L0_integrity
- L1_epistemic
- L2_provenance
- L5_scope
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L4
- L5
- L16
- L17
license: MIT
---

# Information Geometry Mapper

## Identity

Origin architect: **Trang Phan**. Domain: info. Parent: amos-information-theory-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.
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

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-information-geometry-mapper_MOC]]

## Examples

- **Scenario**: When measuring entropy and lacunarity: information content and gaps
  - **Input**: A query matching this skill's domain (info)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When analyzing information collapse topology and structure
  - **Input**: A query matching this skill's domain (info)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When controlling information exposure and disclosure
  - **Input**: A query matching this skill's domain (info)
  - **Output**: Structured result with epistemic labels and provenance


## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

## Anti-Patterns

- **Do not use** for tasks outside the info domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-information-theory-master` — routes to this skill when info specialization is needed
- **Peers**: Other skills in the `info` domain may be composed in sequence
- **Orchestrator**: The parent skill or `AMOS_HOME` orchestrates routing
- **Workflow**: Each skill has a corresponding workflow in `08_WORKFLOWS/`
- **Agent**: Each skill has a corresponding agent in `06_AGENTS/`


## Evaluation

### Success Criteria

- Output includes epistemic class label (SOURCE/DERIVED/AMOS_MODEL/EMPIRICAL)
- Output includes provenance reference to source evidence
- Output includes confidence ceiling (capped at 0.95 for DERIVED, 1.0 for SOURCE_CANON)
- Output includes gap flags for unresolved unknowns
- Output does not exceed declared scope

### Failure Modes

- **Overreach**: Output claims validity beyond its epistemic class
- **Scope creep**: Output addresses questions outside the declared domain
- **Provenance loss**: Output cannot trace back to source evidence
- **Confidence inflation**: Output confidence exceeds the weakest-premise ceiling


## Error Handling

- **On scope violation**: Reject the query and route back to parent skill
- **On missing evidence**: Flag as GAP and reduce confidence ceiling to 0.5
- **On contradiction**: Flag as CRITICAL_GAP and halt until resolved
- **On provenance loss**: Mark output as UNKNOWN and require human review
- **On drift**: Trigger drift alignment via `amos-ai-drift-alignment-governor`


## Do not use

- For generic information analysis outside the information theory framework
- To claim empirical validation of entropy or complexity theories
- As a substitute for domain-specific information or complexity evidence
- Outside information theory domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `[[amos-information-geometry-mapper_MOC]]` — skill Map of Content
- `amos-information-theory-master` — parent skill
- `[[amos-information-geometry-mapper-workflow]]` — corresponding workflow
- `amos-information-geometry-mapper-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-information-geometry-mapper
node_type: skill
path: 07_SKILLS/amos-information-geometry-mapper/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
