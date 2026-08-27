---
title: SKILL
type: skill
name: amos-information-exposure-control
description: Information Exposure Control — info capability. Use when executing the core capability within this domain. Use when amos-information-theory-master routes to this specialized capability.
parent_skill: amos-information-theory-master
domain: info
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-information-exposure-control]
---


# Information Exposure Control

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-information-theory-master`
- **Domain**: info
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Information theory engine for Information Exposure Control

## When to Use

- When measuring entropy and lacunarity: information content and gaps
- When analyzing information collapse topology and structure
- When controlling information exposure and disclosure
- When mapping information geometry: manifolds and projections
- When the parent skill (`amos-information-theory-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **information_exposure.measure_entropy**: Measure entropy and lacunarity: information content, gaps, and structure
- **information_exposure.analyze_topology**: Analyze information collapse topology: how information condenses and structures
- **information_exposure.control_exposure**: Control information exposure: what is revealed, to whom, and under what conditions
- **information_exposure.map_geometry**: Map information geometry: manifolds, distances, and projections in information space

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: e5b0b8a7a7332c2e) for the full vault-sourced domain knowledge (8923 chars).
- **information_exposure.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **information_exposure.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **information_exposure.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/amos-general/A/PROTECTED/AMOS_PROTECTED_KNOWLEDGE_TRAINING_CONTROL_ARCHITECTURE_MAX_DETAIL.md` (content_hash: 4e3fde2833882d11) (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/security/Bounded Intelligence Security™ (BIS™).md` (content_hash: 6258a1ebb7a6cc96) (vault canon, SOURCE_CLAIM)

### Information Exposure Control

From Cosmo Brain Protected Knowledge Training Control Architecture: Governed knowledge-exposure system with typed knowledge objects and semantic-origin lineage. From BIS: Bounded Intelligence Security.

**Exposure control architecture**:
- **Typed knowledge objects**: all knowledge is typed with exposure classification
- **Semantic-origin lineage**: every knowledge object has a semantic origin lineage
- **Origin equivalence classes**: knowledge objects grouped by origin equivalence
- **Information classification**: knowledge classified by exposure level
- **Least privilege**: exposure follows least privilege principle
- **Capability attenuation**: capabilities attenuated by exposure rules

**Exposure control laws**:
- `INTERNAL != EXTERNAL`: internal information is not external information; exposure rules differ
- `DECLARED != UNDECLARED`: only declared information can be exposed; undeclared exposure is a violation
- `SCOPE_BOUND`: exposure is valid only within declared scope and audience

**Anti-exfiltration**:
- **Output-only behavioral definition**: the system is defined by its outputs, not its internal state
- **Human-embedded final enforcement**: humans are the final enforcement layer
- **Ephemeral enforcement**: some enforcement is ephemeral (not persisted)

**Exposure accounting**:
- **Semantic transaction validation**: validate that transactions don't expose undeclared information
- **Multi-origin atomic reservations**: atomic reservations for multi-origin knowledge
- **Commit-time revalidation**: revalidate exposure at commit time
- **Provenance topology**: track exposure through provenance topology
- **Receiver-bound release**: release is bound to declared receivers

### Epistemic Boundary

Information exposure control is a security construct. It does not prove all exposure is controlled, that boundaries are always correct, or that violations are always detected.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag rout

---
**Links:** [[07_SKILLS_MOC]]
