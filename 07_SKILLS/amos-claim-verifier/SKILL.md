---
title: SKILL
type: skill
source: 07_SKILLS/amos-claim-verifier
name: amos-claim-verifier
description: Claim Verifier — audit and repair capability. Use when auditing, failure analysis, gap discovery, or repair allocation. Use when amos-audit-repair-master routes to this specialized capability.
parent_skill: amos-audit-repair-master
domain: audit
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-claim-verifier, canon/skill]
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: "1.1.0"
---


# Claim Verifier

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-audit-repair-master`
- **Domain**: audit
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Audit and verification engine for Claim Verifier

## When to Use

- When auditing claims against evidence and provenance
- When detecting gaps in capabilities, evidence, tests, or monitors
- When allocating repair resources to highest-leverage gaps
- When verifying gap closure across the full lifecycle chain
- When the parent skill (`amos-audit-repair-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **claim_verifier.audit_claim**: Audit claims against evidence, provenance, and epistemic class
- **claim_verifier.detect_gap**: Detect gaps: missing capabilities, missing evidence, missing tests, missing monitors
- **claim_verifier.allocate_repair**: Allocate repair resources to highest-leverage gaps and failure modes
- **claim_verifier.verify_closure**: Verify gap closure: requirement → capability → component → test → evidence
- **claim_verifier.benchmark_forensics**: Benchmark forensic analysis: trace performance regressions to root causes
- **claim_verifier.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **claim_verifier.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **claim_verifier.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 6b68ea4d10bd5a2d) for the full vault-sourced domain knowledge (7115 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/amos-general/A/Vortical/AMOS_Vortical_Persistence_Deep_RSCF_Architecture.md` (content_hash: f9b18a9e22c3fb1d) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C01_META_LOGIC_MASTER_KNOWLEDGE.md` (content_hash: ff5575df755d7e25) (vault canon, SOURCE_CLAIM)

### Claim Verifier

From Cosmo Brain Vortical Persistence RSCF Architecture: Claim verification with epistemic typing and quarantine. From C01 Meta Logic: 5 meta-laws.

**Claim verification model**:
- **Claim parsing**: parse the claim into components (subject, predicate, object, scope, regime)
- **Epistemic typing**: type the claim with epistemic class (SOURCE_CLAIM, DOMAIN_EMPIRICAL, AMOS_MODEL, DERIVED, COMPETING, UNKNOWN/GAP, DECISION)
- **Load-bearing statement typing**: identify which statements are load-bearing
- **Quarantine**: quarantine unvalidated claims

**5 Meta-laws for verification**:
1. **Law of Law**: no unresolved contradictions within the claim
2. **Rule of 2**: at least 2 independent supports for the claim
3. **Rule of 4**: check 4 dimensions: scope, regime, evidence, falsifier
4. **Signal Fidelity Preservation**: no loss of signal fidelity through verification
5. **Structural Integrity**: the claim's structure is maintained under verification

**Verification protocol**:
1. **Parse**: parse the claim into components
2. **Type**: type the claim with epistemic class
3. **Check evidence**: check if the claim has sufficient evidence
4. **Trace provenance**: trace the claim's provenance to its source
5. **Check scope**: check if the claim is within its declared scope
6. **Check falsifier**: check if the claim has a declared falsifier
7. **Check confidence**: check if confidence does not exceed evidence support
8. **Quarantine**: quarantine if verification fails

**Verification outcome**: VERIFIED, PARTIALLY_VERIFIED, UNVERIFIED, CONTRADICTED, UNKNOWN

**Verification law**: `VERIFIED != TRUE`. A verified claim has passed verification gates; it is not proven true.

### Epistemic Boundary

Claim verification is an epistemic governance construct. It does not prove claims are true, that all verification dimensions are covered, or that verification is always correct.

## Failure Modes
- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgra

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-claim-verifier_MOC]]

## Examples

- **Scenario**: When auditing claims against evidence and provenance
  - **Input**: A query matching this skill's domain (audit)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When detecting gaps in capabilities, evidence, tests, or monitors
  - **Input**: A query matching this skill's domain (audit)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When allocating repair resources to highest-leverage gaps
  - **Input**: A query matching this skill's domain (audit)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the audit domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `[[amos-audit-repair-master]]` — routes to this skill when audit specialization is needed
- **Peers**: Other skills in the `audit` domain may be composed in sequence
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
- `[[amos-claim-verifier_MOC]]` — skill Map of Content
- `[[amos-audit-repair-master]]` — parent skill
- `[[amos-claim-verifier-workflow]]` — corresponding workflow
- `[[amos-claim-verifier-agent]]` — corresponding agent

