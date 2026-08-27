---
title: SKILL
type: skill
name: arxiv-cdfm-causal-discovery-foundation-rscf
description: Cdfm Causal Discovery Foundation — arxiv research capability. Use when arxiv research, paper analysis, or literature review. Use when amos-knowledge-research-master routes to this specialized capability.
parent_skill: amos-knowledge-research-master
domain: arxiv
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, arxiv-cdfm-causal-discovery-foundation-rscf]
---


# Arxiv: cdfm Causal Discovery Foundation Rscf

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-knowledge-research-master`
- **Domain**: arxiv
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Arxiv research paper RSCF skill for Arxiv: cdfm Causal Discovery Foundation Rscf

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
