---
title: SKILL — Amos Universe Viability Modeler
type: skill
source: 07_SKILLS/amos-universe-viability-modeler
name: amos-universe-viability-modeler
description: Universe Viability Modeler — canon and universe capability. Use when canon reasoning, universe-level
  analysis, or invariant verification. Use when amos-canon-universe-master routes to this specialized
  capability.
parent_skill: amos-canon-universe-master
domain: canon
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/canon-universe
- rscf/source_claim
- hml/h
- epistemic/source_claim
- amos_os
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
rscf_state: SOURCE_CLAIM
hml_level: H
gmef_gates:
- L0_integrity
- L1_epistemic
- L2_provenance
- L3_dependency
- L5_scope
- L7_authority
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L3
- L4
- L5
- L7
- L16
- L17
- L18
- L19
---

# Universe Viability Modeler

## Identity

Origin architect: **Trang Phan**. Domain: canon. Parent: amos-canon-universe-master. Epistemic class: SOURCE_CLAIM. H/M/L: H.
## When to Use

- When compiling canonical structure from vault sources
- When checking canon consistency for contradictions and gaps
- When enforcing canon invariants across all parts
- When navigating canon to locate parts for any topic
- When the parent skill (`amos-canon-universe-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **universe_viability.compile_canon**: Compile canonical structure from sources into a consistent, navigable canon
- **universe_viability.check_consistency**: Check canon consistency: no contradictions, no gaps, no orphan references
- **universe_viability.enforce_invariant**: Enforce canon invariants: structural laws that must hold across all parts
- **universe_viability.navigate_canon**: Navigate canon: locate the canonical part for any topic or query
- **universe_viability.validate_substrate**: Validate canonical software substrate against canon requirements
- **universe_viability.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **universe_viability.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **universe_viability.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: e03cad8ab8a9d16a) for the full vault-sourced domain knowledge (8097 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/trang/Khung trang.md` (content_hash: 314ed5686de64eef) (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/trang/Trang Reality Architecture AMOS Corpus.md` (content_hash: a301bb507d36dda4) (vault canon, SOURCE_CLAIM)

### Universe Viability Modeler

From Trang Khung Trang: Universe viability as whether a possible universe can sustain persistent recursive structure under entropy pressure. From Trang Reality Architecture AMOS Corpus: Universe ensemble modeling.

**Universe viability definition**: A universe is viable if it can sustain persistent recursive structure under entropy pressure.

**8 Viability requirements**:
1. **Stable recurrence**: the universe supports stable recursive patterns
2. **Memory retention**: the universe can retain information over time
3. **Coherent transformation**: transformations in the universe are coherent
4. **Causal continuity**: causality is continuous (no causal breaks)
5. **Identity persistence**: identities can persist over time
6. **Scalable complexity**: complexity can scale without collapse
7. **Observer compatibility**: the universe supports observers
8. **Correction capacity**: the universe supports error correction

**Viability equation** (AMOS_MODEL):
```
V = coherence × transformability × persistence × entropy_tolerance × recursive_repair_capacity
```

**Universe ensemble**: `Ω = set of possible recursive law-spaces`

**Law-space includes**: causal rules, transformation permissions, conservation behavior, entropy behavior, recurrence conditions, dimensional constraints, interaction coupling, stability thresholds

**Viability laws**:
- `VIABLE != ACTUAL`: a viable universe is possible; it is not necessarily actual
- `VIABILITY != OPTIMALITY**: viability means sustainable; it does not mean optimal
- `ENSEMBLE != MULTIVERSE**: the ensemble is a model space; it is not a claim about physical multiverses

### Epistemic Boundary

Universe viability modeling is an AMOS_MODEL. It does not prove our universe is viable, that the viability equation is empirically validated, or that the ensemble is physically real.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confide

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-universe-viability-modeler_MOC]]

## Examples

- **Scenario**: When compiling canonical structure from vault sources
  - **Input**: A query matching this skill's domain (canon)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When checking canon consistency for contradictions and gaps
  - **Input**: A query matching this skill's domain (canon)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When enforcing canon invariants across all parts
  - **Input**: A query matching this skill's domain (canon)
  - **Output**: Structured result with epistemic labels and provenance


## Validation Gates

- **L0 Integrity**: All 7 parts accounted for; no part silently dropped
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope; no scope creep
- **L7 Authority**: No autonomous action beyond authority boundary

## Anti-Patterns

- **Do not use** for tasks outside the canon domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-canon-universe-master` — routes to this skill when canon specialization is needed
- **Peers**: Other skills in the `canon` domain may be composed in sequence
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


## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `[[amos-universe-viability-modeler_MOC]]` — skill Map of Content
- `amos-canon-universe-master` — parent skill
- `[[amos-universe-viability-modeler-workflow]]` — corresponding workflow
- `amos-universe-viability-modeler-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-universe-viability-modeler
node_type: skill
path: 07_SKILLS/amos-universe-viability-modeler/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
