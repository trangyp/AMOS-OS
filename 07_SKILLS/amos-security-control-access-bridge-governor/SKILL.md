---
title: SKILL
type: skill
name: amos-security-control-access-bridge-governor
description: Security-Control-Access Bridge Governor — cross-domain capability bridging C09 Org-Law-Policy (policy definition), C10 Tech-Engineering (access control mechanisms), and Runtime Enforcement (enforcement attestation). Governs the unified policy-to-enforcement pipeline: C09 policy → translate to mechanism → C10 mechanism → validate enforcement → Runtime enforcement → audit feedback → C09 policy. Enforces policy-mechanism match (every mechanism has a policy), mechanism-enforcement match (every enforcement matches mechanism), and no layer drift. Use when security policies need to be translated to access control mechanisms, when mechanisms need runtime enforcement validation, or when the full policy-to-enforcement pipeline needs governance. Use when amos-security-safety-master routes to this specialized capability.
parent_skill: amos-security-safety-master
domain: cross-domain (C09 → C10 → Runtime)
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
claim_ceiling: 0.9
status: production_ready
created: 2026-08-27
tags: [note, amos-security-control-access-bridge-governor]
---


# Security-Control-Access Bridge Governor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-security-safety-master`
- **Domain**: cross-domain (C09 Org-Law-Policy → C10 Tech-Engineering → Runtime Enforcement)
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from C09, C10, and Runtime enforcement knowledge)

Bridges the security-control-access pipeline across three layers. C09 defines organizational policy, compliance requirements, and legal obligations. C10 implements access control mechanisms, security architecture, and fail-closed design. Runtime Enforcement provides enforcement attestation (ERA/ETC), capability-bound governance, and audit trails. This governor ensures that policy flows to mechanism, mechanism flows to enforcement, and enforcement feeds back to policy — with no layer drift.

## The Problem This Skill Solves

The `_00_Cosmo brain` exploration identified: *"Security and Control and Access: Security policies, access control mechanisms, and runtime enforcement are separate layers without unified policy-to-enforcement pipelines."*

Specifically:

1. **C09's policy definitions have no bridge to C10's access control mechanisms** — policies are written but not automatically translated to implementable mechanisms
2. **C10's access control mechanisms have no bridge to runtime enforcement validation** — mechanisms are implemented but not verified at runtime
3. **Runtime enforcement has no feedback bridge to C09 policy** — enforcement failures don't automatically inform policy updates
4. **No unified pipeline connects all three layers** — each operates in isolation, creating security gaps

## The Pipeline

```text
C09 Policy
    → TRANSLATE → C10 Access Control Mechanism
    → VALIDATE → Runtime Enforcement (ERA/ETC)
    → AUDIT → Audit Feedback
    → UPDATE → C09 Policy
    → (loop repeats)
```

The pipeline has 4 transition types:

- **TRANSLATE**: C09 policy to C10 access control mechanism (policy → mechanism mapping)
- **VALIDATE**: C10 mechanism to runtime enforcement verification (mechanism → enforcement check)
- **AUDIT**: Runtime enforcement to audit feedback (enforcement → compliance report)
- **UPDATE**: Audit feedback to C09 policy (audit → policy revision)

## When to Use

- When C09 security policies need to be translated to C10 access control mechanisms
- When C10 mechanisms need runtime enforcement validation
- When runtime enforcement failures need to feed back to C09 policy
- When governing the full policy-to-enforcement pipeline (PIPELINE_PERMITTED / BLOCKED / CONDITIONAL)
- When detecting layer drift between policy, mechanism, and enforcement
- When auditing the full pipeline for compliance
- When the parent skill (`amos-security-safety-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **sca_bridge.translate_policy_to_mechanism**: Translate C09 policy into C10 access control mechanisms. Maps policy requirements to implementable mechanisms (RBAC, ABAC, capability bounds, fail-closed design). Returns mechanism specification + policy-mechanism mapping.
- **sca_bridge.validate_mechanism_enforcement**: Validate C10 mechanism is correctly enforced at runtime. Checks enforcement attestation (ERA), enforcement trust contract (ETC), capability-bound governance. Returns enforcement validation result + attestation chain.
- **sca_bridge.govern_pipeline**: Govern the full pipeline (PIPELINE_PERMITTED / BLOCKED / CONDITIONAL). Block if: policy-mechanism mismatch, mechanism-enforcement mismatch, layer drift, audit failure. Returns pipeline 