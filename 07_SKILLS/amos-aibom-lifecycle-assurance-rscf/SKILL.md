---
title: SKILL
type: skill
name: amos-aibom-lifecycle-assurance-rscf
description: AIBOM Lifecycle Assurance — RSCF epistemic capability. Use when classifying claims by epistemic state, validating outputs against epistemic and scope constraints, or analyzing evidence structure. Use when amos-rscf-epistemic-master routes to this ...
parent_skill: amos-rscf-epistemic-master
domain: rscf
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-aibom-lifecycle-assurance-rscf]
---


# Aibom Lifecycle Assurance Rscf

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-rscf-epistemic-master`
- **Domain**: rscf
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

RSCF epistemic engine for AIBOM Lifecycle Assurance — supply-chain governance for AI systems

## When to Use

- When classifying AIBOM lifecycle claims by epistemic state and binding them to evidence
- When validating evidence chains for provenance, freshness, scope, and regime validity
- When tracing AIBOM output provenance to vault sources and content hashes
- When assessing confidence ceilings based on epistemic class and evidence strength
- When detecting falsifiers and downgrading confidence as counter-evidence emerges
- When managing AIBOM lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating AIBOM outputs against domain constraints and epistemic class
- When the parent skill (`amos-rscf-epistemic-master`) routes to this specialized capability

## Capabilities

- **aibom_lifecycle.classify_claim**: Classify claims by epistemic state (VERIFIED, DERIVED, MODEL, UNKNOWN/GAP) and bind to evidence
- **aibom_lifecycle.validate_evidence**: Validate evidence chains: provenance, freshness, scope, and regime validity
- **aibom_lifecycle.trace_provenance**: Trace output provenance to vault sources and tag with content_hash
- **aibom_lifecycle.assess_confidence**: Assess confidence ceiling based on epistemic class and evidence strength
- **aibom_lifecycle.detect_falsifier**: Detect falsifiers and downgrade confidence when counter-evidence emerges
- **aibom_lifecycle.manage_lifecycle**: Manage AIBOM lifecycle: classify, validate, trace, assess, detect
- **aibom_lifecycle.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration
- **aibom_lifecycle.validate_outputs**: Validate AIBOM outputs against domain constraints and epistemic class

## Vault-Sourced Content

### Source 1: Assurance, Debt Registers & Maturity Governance

> Path: `dated/2026-08-22/2026-08-22 Assurance Debt Governance.md` | Size: 3711 chars | Match score: 5 | content_hash: a774828e5c7e1e7d

# Assurance, Debt Registers & Maturity Governance


## Overview

The Assurance, Debt Registers & Maturity Governance module provides the final
layer of the AMOS OS Kernel's governance stack. It ensures that assurance
cases are properly reviewed, debt is tracked and managed, components reach
appropriate maturity levels before promotion, evidence/benchmarks/policies
are kept current, obsolete architecture is detected, and simplification
opportunities are pursued.

## Subsystems

### 301 — Independent Falsifier Manager
Tracks independent falsifier access for scientific claims.
Gate: CONDITIONAL if pending falsifier access.

### 302 — Red-Team Independence Manager
Ensures red teams are independent from the development team.
Gate: FAIL if non-independent red teams detected.

### 303 — Assurance Case Manager
Manages assurance cases (draft/under_review/approved/rejected/expired).
Gate: CONDITIONAL if unapproved or expired cases.

### 304 — Certification Profile Manager
Tracks certifications (standard/level/certifier/valid_until).
Gate: CONDITIONAL if expired certifications.

### 305 — Residual Risk Acceptance Manager
Tracks residual risk acceptance by designated authority.
Gate: CONDITIONAL if unaccepted residual risks.

### 306 — Known Gap Disclosure Manager
Ensures known gaps are disclosed to appropriate audiences.
Gate: FAIL if undisclosed known gaps.

### 307-310 — Debt Register Manager
Tracks four types of debt: epistemic, governance, security, architecture.
Gate: FAIL if debt amount > 0.75 threshold.

### 311 — Debt Interaction Manager
Analyzes interactions between different types of debt.
Gate: CONDITIONAL if high-severity interactions (> 0.5).

### 312 — Maturity State Manager
Tracks component maturity (experimental/prototype/beta/production/legacy/deprecated).
Gate: CONDITIONAL if immature components in use.

### 313 — Promotion Evidence Manager
Manages promotion evidence standards (pending/promoted/demoted/quarantined/rejected).
Gate: CONDITIONAL if pending promotions.

### 314 — Demotion/Quarantine Manager
Manages demotion and quarantine rules with authority tracking.
Gate: FAIL if quarantined without authority; CONDITIONAL if quarantined with authority.

### 315 — Continuous Re