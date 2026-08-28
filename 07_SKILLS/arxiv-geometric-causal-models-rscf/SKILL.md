---
title: SKILL — Arxiv Geometric Causal Models Rscf
type: skill
source: 07_SKILLS/arxiv-geometric-causal-models-rscf
name: arxiv-geometric-causal-models-rscf
description: Geometric Causal Models — arxiv research capability. Use when arxiv research,
  paper analysis, or literature review. Use when amos-knowledge-research-master routes
  to this specialized capability.
parent_skill: amos-knowledge-research-master
domain: arxiv
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/knowledge-research
- canon-group/tech-ai
- topic/knowledge-management
- capability/arxiv-research
- topic/research
- capability/causal-reasoning
- capability/markdown_brain_adaptation
- capability/historical_gap
- capability/benchmark_boundary
- rscf/epistemic
- rscf/T-topology
- rscf/M-memory
- rscf/K-compression
- rscf/G-relation
- rscf/type-model
- sota/progressive-disclosure
- sota/anti-patterns
- amos_os
- arxiv-geometric-causal-models-rscf
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
---







# Arxiv: geometric Causal Models Rscf

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-knowledge-research-master`
- **Domain**: arxiv
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Arxiv research paper RSCF skill for Arxiv: geometric Causal Models Rscf

## When to Use

- When arxiv research paper rscf skill for arxiv: geometric causal models rscf is needed within the arxiv domain
- When the parent skill (`amos-knowledge-research-master`) routes to this specialized capability
- When a query requires arxiv-specific reasoning grounded in vault sources
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **geometric_causal.analyze_paper**: Analyze arxiv papers: extract claims, methods, evidence, and limitations
- **geometric_causal.classify_research**: Classify research by epistemic state: established, emerging, speculative, refuted
- **geometric_causal.assess_reproducibility**: Assess reproducibility: can the results be independently verified?
- **geometric_causal.trace_literature**: Trace literature chains: citations, dependencies, and influence networks
- **geometric_causal.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **geometric_causal.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **geometric_causal.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/_arxiv_md/` (arxiv research papers indexed in the AMOS vault) (SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C02_MATH_COMPUTE_MASTER_KNOWLEDGE.md` (content_hash: 7369abada641e374) (vault canon, SOURCE_CLAIM)

### Geometric Causal Models

From arxiv research: Geometric approaches to causal modeling using manifold structure.

**Geometric causal model**:
- **Causal manifold**: causal relationships form a manifold structure
- **Geometric distance**: distance between causal structures measured geometrically
- **Manifold projection**: project data onto causal manifold to identify structure
- **Curvature analysis**: analyze manifold curvature to understand causal complexity

**Model properties**:
- **Manifold structure**: causal relationships have geometric structure
- **Distance metric**: distance between causal models is well-defined
- **Continuity**: small changes in data lead to small changes in causal structure
- **Identifiability**: causal structure is identifiable under declared conditions

**RSCF laws**:
- `GEOMETRIC != CAUSAL`: geometric structure is not causal structure; it is a representation
- `MANIFOLD != REALITY`: the causal manifold is a model, not reality
- `DISTANCE != DIFFERENCE`: geometric distance is not semantic difference

### Epistemic Boundary

Geometric causal models are an analytical method. They do not prove causation, that the manifold structure is correct, or that geometric distance captures causal difference.

## Focus
- quorum certification
- causal epochs
- closed membership
- deterministic conflict ordering
- compact epoch encoding

## Markdown brain adaptation
Use epoch-style finality for conflicting coordinated updates when independence cannot be proven.

## Historical gap
Caller-supplied shard subset could omit touched shard; transaction-ID equivocation across disjoint payloads.

## Benchmark boundary
> **Reference**: See `references/geometric_causal_spec.md` (content_hash: d5761d3443e83ddf) for the JSON specification.

Benchmark results are preserved only within their tested operationalization and are not universal guarantees.

---

---

### Source 3: RSCF — Resonance Scan Causal Field

> Path: `rscf/SKILL (rscf).md` | Size: 1071 chars | Match score: 10 | content_hash: 8aa6adf7742ea031

# RSCF — Resonance Scan Causal Field

## Purpose
RSCF (Resonance Scan Causal Field) is the AMOS proof capsule format for
evidence-grounded claims. It provides a structured way to make, audit, and
invalidate claims with dependencies, scope, freshness, competing explanations,
falsifiers, and confidence ceilings.

## Structure
- **Claim**: The assertion being made
- **Evidence**: Supporting evidence with provenance
- **Scope**: Domain and regime boundaries
- **Freshness**: Temporal validity of the evidence
- **Competing**: Alternative explanations
-

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[arxiv-geometric-causal-models-rscf_MOC]]

## Examples

- **Scenario**: When arxiv research paper rscf skill for arxiv: geometric causal models rscf is needed within the arxiv domain
  - **Input**: A query matching this skill's domain (arxiv)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When the parent skill (`amos-knowledge-research-master`) routes to this specialized capability
  - **Input**: A query matching this skill's domain (arxiv)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When a query requires arxiv-specific reasoning grounded in vault sources
  - **Input**: A query matching this skill's domain (arxiv)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the arxiv domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-knowledge-research-master` — routes to this skill when arxiv specialization is needed
- **Peers**: Other skills in the `arxiv` domain may be composed in sequence
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

- `references/geometric_causal_spec.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `[[arxiv-geometric-causal-models-rscf_MOC]]` — skill Map of Content
- `amos-knowledge-research-master` — parent skill
- `[[arxiv-geometric-causal-models-rscf-workflow]]` — corresponding workflow
- `arxiv-geometric-causal-models-rscf-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: arxiv-geometric-causal-models-rscf
node_type: skill
path: 07_SKILLS/arxiv-geometric-causal-models-rscf/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
