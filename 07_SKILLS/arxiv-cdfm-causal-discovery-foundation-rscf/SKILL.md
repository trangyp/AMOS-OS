---
schema_version: 1.0
title: SKILL — Arxiv Cdfm Causal Discovery Foundation Rscf
type: skill
source: 07_SKILLS/arxiv-cdfm-causal-discovery-foundation-rscf
name: arxiv-cdfm-causal-discovery-foundation-rscf
description: Cdfm Causal Discovery Foundation — arxiv research capability. Use when
  arxiv research, paper analysis, or literature review. Use when amos-knowledge-research-master
  routes to this specialized capability. Do not use for generic tasks outside arxiv
  domain.
parent_skill: amos-knowledge-research-master
domain: arxiv
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/knowledge-research
- rscf/source_claim
- hml/m
- epistemic/source_claim
- amos_os
- 07-skills-moc
- 00-home
- amos-rscf-nodes
- law-hierarchy
- references-moc
- arxiv-cdfm-causal-discovery-foundation-rscf-moc
- trang-framework-recursive-ontology-dynamics
- skill
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

# Arxiv: cdfm Causal Discovery Foundation Rscf

## Identity

Origin architect: **Trang Phan**. Domain: arxiv. Parent: amos-knowledge-research-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.
## When to Use

- When arxiv research paper rscf skill for arxiv: cdfm causal discovery foundation rscf is needed within the arxiv domain
- When the parent skill (`amos-knowledge-research-master`) routes to this specialized capability
- When a query requires arxiv-specific reasoning grounded in vault sources
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **cdfm_causal.analyze_paper**: Analyze arxiv papers: extract claims, methods, evidence, and limitations
- **cdfm_causal.classify_research**: Classify research by epistemic state: established, emerging, speculative, refuted
- **cdfm_causal.assess_reproducibility**: Assess reproducibility: can the results be independently verified?
- **cdfm_causal.trace_literature**: Trace literature chains: citations, dependencies, and influence networks
- **cdfm_causal.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **cdfm_causal.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **cdfm_causal.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/_arxiv_md/` (arxiv research papers indexed in the AMOS vault) (SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### CDFM Causal Discovery Foundation

From arxiv research: Causal Discovery Foundation Models for identifying causal structure from data.

**Causal discovery model**:
- **Observational data**: identify causal structure from observational data (no interventions)
- **Interventional data**: identify causal structure from interventional data (with interventions)
- **Hybrid data**: combine observational and interventional data for better discovery

**Foundation model approach**:
- **Pre-training**: pre-train on large datasets to learn causal patterns
- **Fine-tuning**: fine-tune on specific domains for better performance
- **Transfer**: transfer causal knowledge across domains

**RSCF integration**:
- Causal claims are DERIVED from data, not OBSERVED
- Confidence ceiling: causal discovery confidence <= data quality * method reliability
- Falsifier: alternative causal structures that fit the data equally well
- Scope: causal claims valid only within the data's scope and regime

**Law**: `CORRELATION != CAUSATION`. Causal discovery methods attempt to go beyond correlation, but results are MODEL, not fact.

### Epistemic Boundary

CDFM causal discovery is an analytical method. It does not prove causation, that the discovered structure is unique, or that the method generalizes across domains.

## Summary

Implemented the 3 remaining placeholder discovery modes in
`AMOS_GapRegistry.py`'s `GapDiscoveryEngine` class:
- **Compliance-driven**: diffs current capabilities against external requirements
- **Contradiction-driven**: maps detected conflicts to missing resolution mechanisms
- **Temporal**: re-verifies claims whose validity has expired

All 6 discovery modes are now operational. GAP-MGMT-001 coverage status
upgraded from NOT_COVERED to COVERED.

## What Was Done

### 3 New Discovery Methods

#### 1. `discover_compliance_driven(compliance_spec)`
- **Input**: compliance spec with standard name and requirements list
- **Each requirement**: id, description, component, current_coverage
- **Output**: gap candidates for NOT_COVERED and PARTIALLY_COVERED requirements
- **Impact**: HIGH for NOT_COVERED, MEDIUM for PARTIALLY_COVERED
- **Provenance**: `compliance_driven:{standard}`

#### 2. `discover_contradiction_driven(conflict)`
- **Input**: conflict dict with type, description, component, resolution_attempted, missing_mechanism
- **Output**: gap candidate for missing resolution mechanism
- **Impact**: from conflict severity (default MEDIUM)
- **Provenance**: `contradiction_driven:{conflict_type}`

#### 3. `discover_temporal(expiry_report)`
- **Input**:

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[arxiv-cdfm-causal-discovery-foundation-rscf_MOC]]

## Examples

- **Scenario**: When arxiv research paper rscf skill for arxiv: cdfm causal discovery foundation rscf is needed within the arxiv domain
  - **Input**: A query matching this skill's domain (arxiv)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When the parent skill (`amos-knowledge-research-master`) routes to this specialized capability
  - **Input**: A query matching this skill's domain (arxiv)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When a query requires arxiv-specific reasoning grounded in vault sources
  - **Input**: A query matching this skill's domain (arxiv)
  - **Output**: Structured result with epistemic labels and provenance


## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

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


## Do not use

- For generic document conversion outside arXiv/RSCF framework
- To alter or fabricate scientific claims (source-faithful only)
- As a substitute for domain-specific peer review or validation
- Outside knowledge research domain reasoning

## References

- `references/cdfm_causal_spec.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `` — skill Map of Content
- `amos-knowledge-research-master` — parent skill
- `` — corresponding workflow
- `arxiv-cdfm-causal-discovery-foundation-rscf-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: arxiv-cdfm-causal-discovery-foundation-rscf
node_type: skill
path: 07_SKILLS/arxiv-cdfm-causal-discovery-foundation-rscf/[[SKILL]].md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
