---
title: SKILL
type: skill
source: 07_SKILLS/amos-cross-domain-tensor-composition-governor
name: amos-cross-domain-tensor-composition-governor
description: Cross-Domain Tensor Composition Governor — RSCF epistemic capability. Governs when and how typed tensors (T_R, T_F, T_E, T_C, T_G, T_M) from different AMOS domains (C01-C12) can be composed. Enforces the tensor compatibility invariant, epistemic class preservation across domain boundaries, the weakest-load-bearing-edge confidence rule, and cross-domain provenance tracking. Use when composing claims, evidence, or reasoning across two or more AMOS domains. Use when amos-rscf-epistemic-master routes to this specialized capability.
parent_skill: amos-rscf-epistemic-master
domain: cross-domain
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-cross-domain-tensor-composition-governor, canon/skill]
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: "1.1.0"
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

## Related

- [[amos-cross-domain-tensor-composition-governor_MOC]]

## Examples

- **Scenario**: When composing claims, evidence, or reasoning outputs from two or more AMOS domains (C01-C12)
  - **Input**: A query matching this skill's domain (cross-domain)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When a reasoning task spans domain boundaries (e.g., C04 biology + C05 mind, C07 econ + C08 strategy, C03 physics + C02 math)
  - **Input**: A query matching this skill's domain (cross-domain)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When validating that a claim from domain A is being used within its valid scope in domain B
  - **Input**: A query matching this skill's domain (cross-domain)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the cross-domain domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `[[amos-rscf-epistemic-master]]` — routes to this skill when cross-domain specialization is needed
- **Peers**: Other skills in the `cross-domain` domain may be composed in sequence
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
- `[[amos-cross-domain-tensor-composition-governor_MOC]]` — skill Map of Content
- `[[amos-rscf-epistemic-master]]` — parent skill
- `[[amos-cross-domain-tensor-composition-governor-workflow]]` — corresponding workflow
- `[[amos-cross-domain-tensor-composition-governor-agent]]` — corresponding agent

