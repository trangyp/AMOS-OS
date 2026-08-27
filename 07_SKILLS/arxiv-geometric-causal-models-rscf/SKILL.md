---
title: SKILL
type: skill
name: arxiv-geometric-causal-models-rscf
description: Geometric Causal Models — arxiv research capability. Use when arxiv research, paper analysis, or literature review. Use when amos-knowledge-research-master routes to this specialized capability.
parent_skill: amos-knowledge-research-master
domain: arxiv
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, arxiv-geometric-causal-models-rscf]
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