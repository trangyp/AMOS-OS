---
schema_version: 1.0
title: SKILL — Amos Information Theory Master
type: skill
source: 07_SKILLS/amos-information-theory-master
name: amos-information-theory-master
description: AMOS Information Theory — entropy, complexity, information boundaries, information collapse topology, exposure control. Use when information-theoretic analysis, entropy reasoning, or complexity meas... Do not use for generic statistics, probability theory, or tasks outside AMOS information-theoretic framework.
parent_skill: none
domain: information
origin_architect: Trang Phan
epistemic_class: SOURCE_CANON
tags:
- type/skill
- canon/skill
- domain/information-theory
- rscf/source_claim
- hml/m
- epistemic/source_canon
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

# L6 Uncertainty Laws

## Identity

Origin architect: **Trang Phan**. Domain: information. Parent: none. Epistemic class: SOURCE_CANON. H/M/L: M.
## When to Use

- When performing information-theoretic analysis, entropy reasoning, or complexity measurement
- When evaluating information boundaries, exposure control, or information collapse topology
- When analyzing entropy-lacunarity relationships and structural persistence
- When measuring AI output integrity through entropy and validation alignment
- When a child skill routes an information theory or entropy task to this master
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **info_theory.measure_entropy**: Measure Shannon entropy, conditional entropy, and mutual information for distributions and signals
- **info_theory.analyze_complexity**: Analyze Kolmogorov complexity, computational complexity, and information-theoretic complexity bounds
- **info_theory.map_boundaries**: Map information boundaries: exposure control, information collapse topology, and information geometry
- **info_theory.assess_claim**: Assess information theory claims for epistemic class, evidence strength, and regime validity
- **info_theory.manage_lifecycle**: Manage information theory lifecycle: measure, analyze, map, validate, and govern
- **info_theory.detect_drift**: Detect drift in entropy measurements, complexity bounds, or information boundary consistency
- **info_theory.classify_claim**: Classify information-theoretic claims by epistemic state (VERIFIED, DERIVED, MODEL, UNKNOWN/GAP)
- **info_theory.validate_outputs**: Validate information theory outputs against domain constraints and epistemic class

## Vault-Sourced Domain Knowledge

> **Sources**: `_00_Cosmo brain/misc/E/ENTROPY_LACUNARITY.md` (content_hash: a859135f66fe21d5), `_00_Cosmo brain/architecture/ai_entropy_architecture 2.md` (content_hash: 3b09ceb0cbe19fda) (vault canon, SOURCE_CLAIM)

### Entropy and Lacunarity Equations

These quantities are domain-sensitive. Do not confuse AMOS structural proxies with thermodynamic entropy or formal mathematical lacunarity unless definitions match.

- `E_X = -(1/ln N) Σ_i p_i ln p_i` — normalized Shannon entropy (AMOS_MODEL)
- `E_total = w_L E_L + w_M E_M + w_H E_H` — weighted cross-scale entropy (AMOS_MODEL)
- `Λ_X = Var(Mass)/Mean(Mass)^2` — lacunarity (AMOS_MODEL)
- `Λ_X ≈ 1/(1+e^{-k(E_X-0.5)})` — framework approximation linking entropy to lacunarity (AMOS_MODEL)

### Structural Persistence

`PV = (BoundaryIntegrity × MemoryContinuity × RepairCapacity × RelationCoherence) / (EntropyLoad × ContradictionDensity × FragmentationPressure × ObserverVariance)`

Sustained viability requires repair capacity/rate to exceed degradation/entropy accumulation.

### AI Entropy Architecture

Core law: `AI = Intent + Context + Memory + Reasoning + Tooling + Entropy + Validation + Permission + Output`

**Main law**: AI output is not trusted because it is fluent. It is trusted only when intent, grounding, validation, calibration, and permission align.

**H/M/L Integrity Levels**:
- **L (low)**: unclear intent, missing context, high hallucination risk
- **M (medium)**: fluent but uncertain, plausible output, weak grounding, hidden entropy
- **H (high)**: grounded, scoped, validated, calibrated output

**Fractal Scales**: token → sentence → answer → conversation → memory → tool_call → agent_loop → system

### Key Templates

| ID | Name | Formula | Layer |
|----|------|---------|-------|
| AIE001 | intent_alignment | IA = match(user_intent, model_interpretation) | intent |
| AIE002 | context_completeness | CC = available_context / required_context | context |
| AIE003 | memory_relevance | MR = relevant_memory / used_memory | memory |
| AIE004 | memory_conflict | MC = conflicting_memory / total_memory | memory_entropy |
| AIE005 | retrieval_grounding | RG = grounded_claims / total_claims | grounding |

## Consolidated Sub-Skills (3)

This parent skill consolidates the following sub-skills. Each is a section within this domain:

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: b0dda351f49405e2) for detailed vault-sourced domain knowledge.
> Load only when specific domain detail is decision-relevant.


> **Reference**: Se
- [[AGENT_TEMPLATE]]

---
**MOC:** [[amos-information-theory-master_MOC]]

## Examples

- **Scenario**: When performing information-theoretic analysis, entropy reasoning, or complexity measurement
  - **Input**: A query matching this skill's domain (information)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When evaluating information boundaries, exposure control, or information collapse topology
  - **Input**: A query matching this skill's domain (information)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When analyzing entropy-lacunarity relationships and structural persistence
  - **Input**: A query matching this skill's domain (information)
  - **Output**: Structured result with epistemic labels and provenance


## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

## Anti-Patterns

- **Do not use** for tasks outside the information domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `none` — routes to this skill when information specialization is needed
- **Peers**: Other skills in the `information` domain may be composed in sequence
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

- For generic analysis outside the information framework
- To claim empirical validation without domain-specific evidence
- As a substitute for domain-specific evidence
- Outside information domain reasoning

## References

- `references/hermes_omni_signal.md` — loaded on demand
- `references/information_measure_governance.md` — loaded on demand
- `references/qfm_bridge_entropy_lacunarity.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `references/regime_freshness.md` — loaded on demand
- `references/signals.md` — loaded on demand
- `references/types_of_signals.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `` — skill Map of Content
- `none` — parent skill
- `` — corresponding workflow
- `amos-information-theory-master-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-information-theory-master
node_type: skill
path: 07_SKILLS/amos-information-theory-master/[[SKILL]].md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
