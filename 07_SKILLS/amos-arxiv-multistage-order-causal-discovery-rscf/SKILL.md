---
schema_version: 1.0
title: SKILL — Amos Arxiv Multistage Order Causal Discovery Rscf
type: skill
source: 07_SKILLS/amos-arxiv-multistage-order-causal-discovery-rscf
name: amos-arxiv-multistage-order-causal-discovery-rscf
description: Arxiv Multistage Order Causal Discovery — arxiv research capability.
  Use when arxiv research, paper analysis, or literature review. Use when amos-knowledge-research-master
  routes to this specialized capability. Do not use for generic tasks outside arxiv
  domain.
parent_skill: amos-knowledge-research-master
domain: arxiv
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- type/skill
- domain/knowledge-research
- epistemic/source_claim
- hml/m
- epistemic/source_claim
- amos-os
- law-hierarchy
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

# Arxiv: multistage Order Causal Discovery Rscf

## Identity

Origin architect: **Trang Phan**. Domain: arxiv. Parent: amos-knowledge-research-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.
## When to Use

- When arxiv research paper rscf skill for arxiv: multistage order causal discovery rscf is needed within the arxiv domain
- When the parent skill (`amos-knowledge-research-master`) routes to this specialized capability
- When a query requires arxiv-specific reasoning grounded in vault sources
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **multistage_order.analyze_paper**: Analyze arxiv papers: extract claims, methods, evidence, and limitations
- **multistage_order.classify_research**: Classify research by epistemic state: established, emerging, speculative, refuted
- **multistage_order.assess_reproducibility**: Assess reproducibility: can the results be independently verified?
- **multistage_order.trace_literature**: Trace literature chains: citations, dependencies, and influence networks
- **multistage_order.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **multistage_order.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **multistage_order.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Operations

1. **multistage_order.analyze_paper**: Analyze arxiv papers: extract claims, methods, evidence, and limitations
2. **multistage_order.classify_research**: Classify research by epistemic state: established, emerging, speculative, refuted
3. **multistage_order.assess_reproducibility**: Assess reproducibility: can the results be independently verified?
4. **multistage_order.trace_literature**: Trace literature chains: citations, dependencies, and influence networks
5. **multistage_order.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
6. **multistage_order.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
7. **multistage_order.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/_arxiv_md/` (arxiv research papers indexed in the AMOS vault) (SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Multistage Order Causal Discovery

From arxiv research: Multistage causal discovery methods for identifying causal orderings from observational data.

**Causal discovery model**:
- **Stage 1 -- Independence**: identify conditional independencies in the data
- **Stage 2 -- Order**: determine causal ordering from independence structure
- **Stage 3 -- Structure**: identify specific causal relationships given the ordering
- **Stage 4 -- Validation**: validate the discovered causal structure

**RSCF integration**:
- Causal claims are DERIVED from data, not OBSERVED
- Confidence ceiling: causal discovery confidence <= data quality * method reliability
- Falsifier: alternative causal structures that fit the data equally well
- Scope: causal claims valid only within the data's scope and regime

**Law**: `CORRELATION != CAUSATION`. Causal discovery methods attempt to go beyond correlation, but results are MODEL, not fact.

### Epistemic Boundary

Multistage causal discovery is an analytical method. It does not prove causation, that the discovered structure is unique, or that the method is always correct.

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
> **Reference**: See `references/causal_discovery_spec.md` (content_hash: d5761d3443e83ddf) for the JSON specification.

Benchmark results are preserved only within their tested operationalization and are not universal guarantees.

---

---

### Source 2: AMOS_CORE v3.4.1 — Distributed Causal Evolution Runtime

> Path: `amos-general/A/CORE/AMOS_CORE v3.4.1 — Distributed Causal Evolution Runtime.md` | Size: 76005 chars | Match score: 10 | content_hash: fa45f5b18b536485

"""
AMOS_CORE v3 – Deterministic Reasoning Kernel (Clean Single-File Version)

Status:
- Executable Python module (no external dependencies beyond stdlib).
- Canon-aligned structure with:
    - Core-19 logic + rewrite system
    - Knowledge base + entailment + contradiction detection
- TSS-style system state
    - Task + engine API
- Minimal translation layer (NL <-> logic stubs)
    - Drift / integrity audit hooks
- Placeholders for higher layers (universe, multi-agent, compression) as stubs

This file is designed as a stabl

---
**Links:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Related

- [[07_SKILLS/amos-arxiv-multistage-order-causal-discovery-rscf/amos-arxiv-multistage-order-causal-discovery-rscf_MOC|amos-arxiv-multistage-order-causal-discovery-rscf_MOC]]

## Examples

- **Scenario**: When arxiv research paper rscf skill for arxiv: multistage order causal discovery rscf is needed within the arxiv domain
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

- `references/causal_discovery_spec.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `` — skill Map of Content
- `amos-knowledge-research-master` — parent skill
- `` — corresponding workflow
- `amos-arxiv-multistage-order-causal-discovery-rscf-agent` — corresponding agent
---

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-arxiv-multistage-order-causal-discovery-rscf
node_type: skill
path: 07_SKILLS/amos-arxiv-multistage-order-causal-discovery-rscf/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
