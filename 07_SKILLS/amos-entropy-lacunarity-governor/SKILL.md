---
schema_version: 1.0
title: SKILL — Amos Entropy Lacunarity Governor
type: skill
source: 07_SKILLS/amos-entropy-lacunarity-governor
name: amos-entropy-lacunarity-governor
description: Entropy Lacunarity Governor — info capability. Use when executing the core capability within this domain. Use when amos-information-theory-master routes to this specialized capability. Do not use for generic tasks outside info domain.
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
steward: Trang Phan
---

# Entropy Lacunarity Governor

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

- **entropy_lacunarity.measure_entropy**: Measure entropy and lacunarity: information content, gaps, and structure
- **entropy_lacunarity.analyze_topology**: Analyze information collapse topology: how information condenses and structures
- **entropy_lacunarity.control_exposure**: Control information exposure: what is revealed, to whom, and under what conditions
- **entropy_lacunarity.map_geometry**: Map information geometry: manifolds, distances, and projections in information space
- **entropy_lacunarity.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **entropy_lacunarity.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **entropy_lacunarity.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 1ecf25a924ddcd61) for the full vault-sourced domain knowledge (5720 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/amos-general/A/Vortical/AMOS_Vortical_Persistence_Deep_RSCF_Architecture.md` (content_hash: f9b18a9e22c3fb1d) (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/dated/2026-08-25/2026-08-25 QFM Bridge Governance and Entropy-Lacunarity Skill.md` (content_hash: 11c66249785d6312) (vault canon, SOURCE_CLAIM)

### Entropy Lacunarity Governor

From Cosmo Brain Vortical Persistence RSCF Architecture: AMOS Entropy/Lacunarity Governor as runtime alignment component. From QFM Bridge Governance: Entropy/lacunarity proxies with bridge discipline.

**Lacunarity formula** (SOURCE_DERIVED):
```
Λ(r) = Var[M_r] / E[M_r]² + 1
```
- Λ(r) = lacunarity at scale r, M_r = mass at scale r, Var = variance, E = expectation

**AMOS lacunarity hypothesis** (AMOS_MODEL): persistence may correlate with regime-specific structural-gap distribution.

**Strict AMOS usage required** -- must specify:
- representation, measurement scale, segmentation, estimator, temporal sampling, null model, uncertainty, comparator systems

**Entropy typing**:
- **Physical entropy**: thermodynamic entropy (physics claim)
- **AMOS structural entropy**: structural complexity measure (AMOS_MODEL)

**Bridge discipline** (from QFM Bridge Governance):
- **Family ≠ identity**: shared mathematical structure does NOT permit transferring numeric values between contexts
- **B5 entropy/lacunarity proxies**: SOURCE equations, MODEL-gated usage
- **Unfalsifiable-as-used → MODEL**: failure to construct a wrong-conclusion case reduces claim weight rather than raising it

**Governor laws**:
- `PHYSICAL_ENTROPY != STRUCTURAL_ENTROPY`: physical entropy is thermodynamic; structural entropy is informational
- `LACUNARITY != COMPLEXITY**: lacunarity measures gap distribution; complexity measures overall structure
- `PROXY != VALUE**: entropy/lacunarity are proxies; they are not direct measurements

### Epistemic Boundary

Entropy lacunarity governance is an AMOS_MODEL. It does not prove lacunarity predicts persistence, that the formula is universally applicable, or that structural entropy equals physical entropy.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overre

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-entropy-lacunarity-governor_MOC]]

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
- `` — skill Map of Content
- `amos-information-theory-master` — parent skill
- `` — corresponding workflow
- `amos-entropy-lacunarity-governor-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-entropy-lacunarity-governor
node_type: skill
path: 07_SKILLS/amos-entropy-lacunarity-governor/[[SKILL]].md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
