---
title: SKILL
type: skill
name: amos-cross-domain-tensor-composition-governor
description: Cross-Domain Tensor Composition Governor — RSCF epistemic capability. Governs when and how typed tensors (T_R, T_F, T_E, T_C, T_G, T_M) from different AMOS domains (C01-C12) can be composed. Enforces the tensor compatibility invariant, epistemic class preservation across domain boundaries, the weakest-load-bearing-edge confidence rule, and cross-domain provenance tracking. Use when composing claims, evidence, or reasoning across two or more AMOS domains. Use when amos-rscf-epistemic-master routes to this specialized capability.
parent_skill: amos-rscf-epistemic-master
domain: cross-domain
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-cross-domain-tensor-composition-governor]
---


# Cross-Domain Tensor Composition Governor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-rscf-epistemic-master`
- **Domain**: cross-domain (meta-domain spanning C01-C12)
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS tensor contracts and 12 domain master knowledge files)

Governs cross-domain tensor composition — the operation of combining typed tensors (Claim, Evidence, Relation, Governance, Memory, Fractal) originating from different AMOS domain engines (C01-C12) into a unified reasoning result, while preserving epistemic integrity, scope boundaries, and provenance chains across domain boundaries.

## The Problem This Skill Solves

The AMOS architecture has 12 domain engines (C01-C12), each with its own claim classes, evidence classes, scope/regime definitions, and epistemic boundaries. When a reasoning task requires knowledge from multiple domains (e.g., C04 biology + C05 mind + C09 governance for a bioethics decision), the tensors from each domain must be composed. The tensor contracts file states the critical invariant:

> **"Tensor composition is prohibited until shared axes are semantically compatible. Same-name axes do not prove same meaning."**

No existing skill governs this composition operation. Only 3 cross-domain skills exist out of 270+ (~1.1%), and none enforce the compatibility invariant or the weakest-load-bearing-edge confidence rule.

## When to Use

- When composing claims, evidence, or reasoning outputs from two or more AMOS domains (C01-C12)
- When a reasoning task spans domain boundaries (e.g., C04 biology + C05 mind, C07 econ + C08 strategy, C03 physics + C02 math)
- When validating that a claim from domain A is being used within its valid scope in domain B
- When tracing provenance chains that cross domain boundaries
- When enforcing the "weakest load-bearing edge" confidence rule across composed domains
- When detecting cross-domain epistemic overreach (a MODEL claim from domain A treated as VERIFIED in domain B)
- When classifying the type of cross-domain bridge (analogy, isomorphism, causal, informational, structural)
- When the parent skill (`amos-rscf-epistemic-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **cross_domain.validate_axis_compatibility**: Validate that shared axes between two domain tensors are semantically compatible (not just name-matching). Checks scope, regime, causal_level, time, observer, and provenance axes for semantic equivalence, not lexical identity.
- **cross_domain.govern_composition**: Govern when tensors from different domains can be composed. Enforces the compatibility invariant: composition is blocked until all shared axes are verified semantically compatible. Returns COMPOSITION_PERMITTED / COMPOSITION_BLOCKED / COMPOSITION_CONDITIONAL.
- **cross_domain.detect_epistemic_overreach**: Detect when a claim from domain A is being used beyond its epistemic class or scope in domain B. Flags class promotion (MODEL→VERIFIED), scope expansion, regime mismatch, and falsifier neglect across boundaries.
- **cross_domain.trace_cross_domain_provenance**: Trace provenance chains across domain boundaries. Records the full derivation path from source domain through bridge to consuming domain, preserving source paths, content hashes, and epistemic class at each hop.
- **cross_domain.enforce_weakest_edge**: Enforce the "weakest load-bearing edge" confidence rule across composed domains. The confidence of a cross-domain composition cannot exceed the confidence of its weakest load-bearing premise, traced across all domain boundaries.
- **cross_domain.classify_bridge**: Classify the type of cross-domain bridge being attempted: ANALOGY (structural similarity, no causal claim), ISOMORPHISM (formal equivalence, proven), CAUSAL (causal chain crosses boundary), INFORMATIONAL (information flow, no causal claim), STRUCTURAL (shared structural pattern). Each type ha

---
**Links:** [[07_SKILLS_MOC]]
