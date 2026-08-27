---
title: SKILL
type: skill
source: 07_SKILLS/amos-security-safety-master
name: amos-security-safety-master
description: "AMOS Security & Safety — adversarial robustness, privacy, safety firewalls, immune systems, drift alignment. Use for security analysis, safety verification, or adversarial defense."
parent_skill: none
domain: security
origin_architect: Trang Phan
epistemic_class: SOURCE_CANON
tags: [note, amos-security-safety-master, canon/skill]
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: "1.1.0"
---


# SECURITY README

## Identity

Origin architect and steward: **Trang Phan**.

This is a **parent skill** that consolidates 2 sub-skills into a single domain master.
Following the skill-organizer best practice: fewer, richer skills beat many overlapping ones.
A parent skill with clearly labeled sections is better than 2 separate shallow skills.

**Epistemic class**: SOURCE_CLAIM (vault-sourced from `18_SECURITY/SECURITY_README.md`).

## When to Use

AMOS Security & Safety — adversarial robustness, privacy, safety firewalls, immune systems, drift alignment. Use for security analysis, safety verification, or adversarial defense.
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **security_safety.evaluate_influence**: Evaluate whether memory may influence a pending action through the AMOS Security & Safety consent, provenance, and risk gates.
- **security_safety.validate_gates**: Validate AMOS Security & Safety decisions against hard partition gates, epistemic class preservation, and consent state requirements.
- **security_safety.analyze_state**: Analyze AMOS Security & Safety memory state: working, episodic, semantic stores, consolidation, and retrieval graph health.
- **security_safety.trace_provenance**: Trace AMOS Security & Safety memory entries to source, encoding operation, consolidation history, and field-level lineage.
- **security_safety.assess_claim**: Assess AMOS Security & Safety memory claims for epistemic class, freshness, contradiction status, and confidence ceiling.
- **security_safety.manage_lifecycle**: Manage AMOS Security & Safety lifecycle: encode, normalize, admit, consolidate, index, retrieve, filter, update.
- **security_safety.detect_drift**: Detect memory drift: stale entries, broken provenance, epistemic class erosion, and context discontinuity.
- **security_safety.escalate_gaps**: Escalate AMOS Security & Safety memory gaps: flag UNKNOWN/GAP entries, quarantine untrusted data, trigger memory repair.
- **security_safety.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Consolidated Sub-Skills (2)

This parent skill consolidates the following sub-skills. Each is a section within this domain:

## Vault-Sourced Domain Knowledge

> **Source**: `18_SECURITY/SECURITY_README.md` from the AMOS_OS Obsidian vault.
> This is substantive domain knowledge, not script-generated content.

# SECURITY README

## Purpose
`SECURITY README` is the package readme for the **Security** plane segment at `18_SECURITY`.
The Security plane governs threat surface, fail-closed gates, attestation, and secrets status. Normative load-bearing content lives in the sibling contract(s); this readme orients navigation.

## Sibling artifacts
- [[SECURITY_SECURITY_CONTRACT]]

## Contract discipline
Typed artifacts · provenance stamped · epistemic class declared · confidence ceiling · fail-closed on UNKNOWN/GAP · receipts for consequential effects · rollback basin before mutation.

## Gaps
Executable binding PARTIAL unless an executed validation receipt exists for this subsystem ([[ROUTING_POLICY_VALIDATION_RECEIPT]] · [[AUTHZ_ENGINE_VALIDATION_RECEIPT]]).

## Worked semantics
Given an operation touching `SECURITY · README` within the Security plane:
1. **Admit** — resolve the artifact by id + version; unresolved id ⇒ `UNKNOWN/GAP`, fail closed.
2. **Bind scope** — declare domain / regime / H-M-L applicability before any mutation.
3. **Check authority** — authority_ref must be epoch-valid; capability alone never authorizes.
4. **Validate preconditions** — dependency closure traversed to the smallest result-changing set.
5. **Propose** — candidate state is non-authoritative until gates pass (`PROPOSAL ≠ COMMIT`).
6. **Commit or hold** — on any failed premise: preserve unaffected state, invalidate dependent descendants only, record receipt.

## Promotion-gate checklist
- [ ] typed schema bound to this artifact
- [ ] identity + versioning implemented
- [ ] negative cases covered (missing · malformed · stale · unauthorized input)
- [ ] provenance edges persisted and validated
- [ ] rollback basin demonstrated for consequential effects
- [ ] executed validation receipt specific to this artifact
- [ ] unresolved critical gaps registered as UNKNOWN/GAP (visible)

## Cross-plane bindings
- Governed by canon — [[LAW_HIERARCHY|AMOS Core Laws]] · [[LAW_HIERARCHY]]
- Kernel interaction — [[KERNEL_README]]
- Control-plane gates — [[CONTROL_PLANE_README]]
- Observed by — [[OBSERVABILITY_README]] · never treated as authority
- Recovered via operations —
- [[AGENT_TEMPLATE]]

---
**MOC:** [[amos-security-safety-master_MOC]]

## Examples

- **Scenario**: When validating outputs against domain constraints and epistemic class
  - **Input**: A query matching this skill's domain (security)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the security domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `[[none]]` — routes to this skill when security specialization is needed
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


## References

- `references/access_control.md` — loaded on demand
- `references/access_control_priv_esc.md` — loaded on demand
- `references/access_control_security_models.md` — loaded on demand
- `references/adversarial_robustness_governance.md` — loaded on demand
- `references/adversarial_validation.md` — loaded on demand
- `references/beyond_blockchain_bio_security.md` — loaded on demand
- `references/blockchain_hackable_security.md` — loaded on demand
- `references/bounded_intelligence_security.md` — loaded on demand
- `references/cors_security.md` — loaded on demand
- `references/crisis_management_engine.md` — loaded on demand
- `references/defense_security_civil_protection.md` — loaded on demand
- `references/horizontal_access_control.md` — loaded on demand
- `references/institutional_digital_security.md` — loaded on demand
- `references/ios_reverse_engineering.md` — loaded on demand
- `references/language_overlay_ip_security.md` — loaded on demand
- `references/ldap_security.md` — loaded on demand
- `references/oauth_openid_connect.md` — loaded on demand
- `references/omega_crypto_internet.md` — loaded on demand
- `references/omega_crypto_structural_engine.md` — loaded on demand
- `references/privacy_compliance_licensing.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `references/risk_compliance_engine.md` — loaded on demand
- `references/risk_compliance_engine_layer.md` — loaded on demand
- `references/risk_compliance_engine_v0.md` — loaded on demand
- `references/risk_compliance_kernel.md` — loaded on demand
- `references/security_architecture_kernel.md` — loaded on demand
- `references/shellshock.md` — loaded on demand
- `references/tech_safe_honest_societies.md` — loaded on demand
- `references/web_cache_poisoning.md` — loaded on demand
- `[[amos-security-safety-master_MOC]]` — skill Map of Content
- `[[none]]` — parent skill
- `[[amos-security-safety-master-workflow]]` — corresponding workflow
- `[[amos-security-safety-master-agent]]` — corresponding agent

