---
title: SKILL
type: skill
name: amos-arxiv-multistage-order-causal-discovery-rscf
description: Arxiv Multistage Order Causal Discovery — arxiv research capability. Use when arxiv research, paper analysis, or literature review. Use when amos-knowledge-research-master routes to this specialized capability.
parent_skill: amos-knowledge-research-master
domain: arxiv
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-arxiv-multistage-order-causal-discovery-rscf]
---


# Arxiv: multistage Order Causal Discovery Rscf

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-knowledge-research-master`
- **Domain**: arxiv
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Arxiv research paper RSCF skill for Arxiv: multistage Order Causal Discovery Rscf

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
**Links:** [[07_SKILLS_MOC]]
