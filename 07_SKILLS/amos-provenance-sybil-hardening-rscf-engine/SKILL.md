---
schema_version: 1.0
title: SKILL — Amos Provenance Sybil Hardening Rscf Engine
type: skill
source: 07_SKILLS/amos-provenance-sybil-hardening-rscf-engine
name: amos-provenance-sybil-hardening-rscf-engine
description: Provenance Sybil Hardening — security and safety capability. Use when
  security analysis, safety verification, or adversarial defense. Use when amos-security-safety-master
  routes to this specialized capability. Do not use for generic tasks outside security
  domain.
parent_skill: amos-security-safety-master
domain: security
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/security-safety
- rscf/source_claim
- hml/h
- epistemic/source_claim
- amos_os
- 07-skills-moc
- 00-home
- amos-rscf-nodes
- law-hierarchy
- references-moc
- amos-provenance-sybil-hardening-rscf-engine-moc
- trang-framework-recursive-ontology-dynamics
- skill
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
rscf_state: SOURCE_CLAIM
hml_level: H
gmef_gates:
- L0_integrity
- L1_epistemic
- L2_provenance
- L5_scope
- L7_authority
- L23_mvcc_cas
collapse_class: fail_closed
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L4
- L5
- L7
- L16
- L17
- L18
- L23
license: MIT
steward: Trang Phan
---

# Provenance Sybil Hardening Rscf Engine

## Identity

Origin architect: **Trang Phan**. Domain: security. Parent: amos-security-safety-master. Epistemic class: SOURCE_CLAIM. H/M/L: H.
## When to Use

- When detecting adversarial activity: attacks, probes, manipulation
- When quantifying adversarial entropy and attack surface
- When governing principal-trust relationships: delegation, revocation
- When monitoring distributed attack composition: multi-stage threats
- When the parent skill (`amos-security-safety-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **provenance_sybil.detect_adversary**: Detect adversarial activity: attacks, probes, and manipulation attempts
- **provenance_sybil.quantify_entropy**: Quantify adversarial entropy: uncertainty, information leakage, and attack surface
- **provenance_sybil.govern_trust**: Govern principal-trust relationships: delegation, revocation, and audit
- **provenance_sybil.monitor_attack**: Monitor distributed attack composition: multi-stage, multi-vector threats
- **provenance_sybil.replay_provenance**: Replay execution provenance: trace and verify every action for integrity
- **provenance_sybil.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **provenance_sybil.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **provenance_sybil.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Operations

1. **provenance_sybil.detect_adversary**: Detect adversarial activity: attacks, probes, and manipulation attempts
2. **provenance_sybil.quantify_entropy**: Quantify adversarial entropy: uncertainty, information leakage, and attack surface
3. **provenance_sybil.govern_trust**: Govern principal-trust relationships: delegation, revocation, and audit
4. **provenance_sybil.monitor_attack**: Monitor distributed attack composition: multi-stage, multi-vector threats
5. **provenance_sybil.replay_provenance**: Replay execution provenance: trace and verify every action for integrity
6. **provenance_sybil.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
7. **provenance_sybil.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
8. **provenance_sybil.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Content

### Source 1: v3.7.1 — Provenance Topology Hardened Runtime

> Path: `misc/V/V3_7_1.md` | Size: 1467 chars | Match score: 9 | content_hash: 497a4dd5c70d0081

# v3.7.1 — Provenance Topology Hardened Runtime

## Focus
- root-content fingerprints
- Sybil alias collapse
- cycle/missing-parent/equivocation rejection

## Known gap at this version
Recursive Python traversal failed around depth ~3000.

## Brain adaptation
Treat this runtime stage as a loadable reasoning capability. Preserve the later lineage improvements; never regress to an earlier weakness when a later module corrects it.

## Benchmark record
> **Reference**: See `references/sybil_hardening_spec.md` (content_hash: 5dacd8a6a7b937d4) for the JSON specification.

Benchmark claims are bounded to the recorded test corpus/environment and must not be generalized universally.

---

---

### Source 2: AMOS Provenance and Trust

> Path: `brain/P/PROVENANCE (AMOS_MD_BRAIN).md` | Size: 1161 chars | Match score: 9 | content_hash: e6058f84799a8578

# AMOS Provenance and Trust

## Trust is local
Trust is typed, scoped, provenance-aware, regime-aware, and freshness-bounded.

## Evidence identity
Track when material:
- source identity
- source type
- parent/ancestor source
- timestamp/version
- environment/regime
- transformation history
- independence status

## Sybil hardening
Multiple documents, posts, agents, or summaries descending from the same origin count as correlated support, not independent confirmation.

Authority, popularity, repetition, or paraphrase do not prove independence.

## Independence test
Before aggregating support ask:
1. Do sources share a parent?
2. Do they share a dataset, benchmark, fixture, model output, or press release?
3. Is one merely summarizing another?
4. Were they independently measured?
5. Do they fail independently?

If unknown, mark provenance independence as uncertain.

## Freshness
A stale source can remain historically accurate but lose applicability in a changed regime.

---

---

### Source 3: AMOS_CORE v3.9 — Persistent Incremental Provenance Runtime

> Path: `amos-general/A/CORE/AMOS_CORE v3.9 — Persistent Incremental Provenance Runtime.md` | Size: 127625 chars | Match score: 8 | content_hash: a182e8c6905ed6dd

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
    - D

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-provenance-sybil-hardening-rscf-engine_MOC]]

## Examples

- **Scenario**: When detecting adversarial activity: attacks, probes, manipulation
  - **Input**: A query matching this skill's domain (security)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When quantifying adversarial entropy and attack surface
  - **Input**: A query matching this skill's domain (security)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When governing principal-trust relationships: delegation, revocation
  - **Input**: A query matching this skill's domain (security)
  - **Output**: Structured result with epistemic labels and provenance


## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

## Anti-Patterns

- **Do not use** for tasks outside the security domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-security-safety-master` — routes to this skill when security specialization is needed
- **Peers**: Other skills in the `security` domain may be composed in sequence
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

- For generic security analysis outside the AMOS security framework
- To claim empirical validation of adversarial defense theories
- As a substitute for domain-specific security or safety evidence
- Outside security/safety domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/sybil_hardening_spec.md` — loaded on demand
- `` — skill Map of Content
- `amos-security-safety-master` — parent skill
- `` — corresponding workflow
- `amos-provenance-sybil-hardening-rscf-engine-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-provenance-sybil-hardening-rscf-engine
node_type: skill
path: 07_SKILLS/amos-provenance-sybil-hardening-rscf-engine/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
