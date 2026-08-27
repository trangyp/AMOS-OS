---
title: vault domain knowledge
type: reference
source: 07_SKILLS/amos-security-control-access-bridge-governor/references
tags: [reference, amos-security-control-access-bridge-governor, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Vault Domain Knowledge — Security-Control-Access Bridge Governor

> **Source**: AMOS_OS Obsidian vault and Cosmo Brain vault

## 1. C09 Security Policy Layer (SOURCE_CLAIM)

### Control Framework

- **Preventive**: stop errors before occurrence (approvals, segregation of duties)
- **Detective**: find errors after occurrence (reconciliation, monitoring, audit)
- **Corrective**: fix and prevent recurrence (remediation, process redesign)

### Control Levels

- Strategic (board oversight, risk appetite)
- Tactical (management controls, policy enforcement)
- Operational (front-line checks)
- Automated (system-enforced validation)

### Design Principles

- Segregation of duties: no single person controls an entire transaction end-to-end
- Authorization thresholds: above-threshold actions require higher approval
- Documentation: decisions and transactions recorded contemporaneously
- Monitoring: ongoing verification that controls actually operate
- Independent review: assurance functions separate from operations reviewed

### Risk Gating

- Actions under uncertainty carry explicit risk assessment before selection
- Blocked by gate rule if risk assessment is missing

## 2. C10 Access Control Mechanism Layer (SOURCE_CLAIM)

### Access Control Components

- **Authentication**: identifies and confirms user
- **Session Management**: identifies which HTTP requests are made by same user
- **Access Control**: determines whether a user can carry out an action

### Prevention Principles

- Do not rely on obfuscation for access control
- All non-publicly accessible resources should be denied by default
- Use single application-wide mechanisms for enforcing access controls
- Mandate developers to declare allowed access for each resource and deny by default
- Audit and test to ensure they are working as designed

### Access Control Types (from Cosmo brain control/ directory)

- Vertical access control
- Horizontal access control
- Context-dependent access control
- CORS access control
- DOM-based access control

## 3. Runtime Enforcement Layer (SOURCE_CLAIM)

### Capability-Bound Governance Kernel v4.8

- All decisions pass through the capability-bound governance kernel
- Capability != Authority (having a capability does not authorize its use)
- Durable commit requires fresh effect-bound authority
- Enforcement Root Attestation (ERA) binds authority to enforcement measurement

### Enforcement Trust Contract (v43)

- An effect cannot become authoritative merely because AMOS approved it
- AMOS must establish the currently executing enforcement chain is the same trusted chain
- MayExternalize_v43 = 18-term conjunction + EnforcementTrustContractValid + DelegationWitnessValid

### Separability Law

Capability != Reachability != Identity != Authorization != Delegation != Observability != Enforcement != Finality != Consequence

## 4. The Pipeline Gap

From _00_Cosmo brain exploration:

> "Security ↔ Control ↔ Access: Security policies, access control mechanisms, and runtime enforcement are separate layers without unified policy-to-enforcement pipelines."

Specifically:

1. C09 defines security policy but has no bridge to C10's technical access control implementation
2. C10 has access control mechanisms but has no bridge back to C09's policy definitions
3. Runtime enforcement enforces decisions but has no bridge to verify enforcement matches policy and mechanism
4. No unified pipeline connects all three layers

## 5. Pipeline Transition Rules

### Translate Policy to Mechanism (C09 to C10)

- Input: C09 policy (authorization thresholds, segregation of duties, control types)
- Output: C10 mechanism specs (authentication, session rules, access matrices)
- Rule: every policy element must have a corresponding mechanism element
- Gate: policy must be sufficient (not UNKNOWN/GAP)

### Validate Mechanism Enforcement (C10 to Runtime)

- Input: C10 mechanism spec
- Output: runtime enforcement validation (VALID / MISMATCH / MISSING)
- Rule: enforcement must match mechanism specification exactly
- Gate: mechanism must be implemented (not MISSING)

### Audit Pipeline (Full)

- Input: access decision record
- Output: audit report with compliance status
- Rule: every access decision has traceable policy origin, matching mechanism, verified enforcement
- Gate: all three layers must be present and aligned

## 6. Anti-Overclaim Boundaries

- C09 policy is CONDITIONAL on jurisdiction and organizational context
- C10 mechanism specs are DERIVED from policy but may have implementation gaps
- Runtime enforcement is VERIFIED only when enforcement receipt exists
- No enforcement claim beyond what the mechanism actually enforces
- No policy claim promoted to enforcement guarantee without implementation evidence
- Separability law: capability != authority != enforcement

## 7. Security Models from Cosmo Brain (Cosmo brain: security/Access_Control-Priv_Esc--Security_Models.md)

Formally defined access control rules independent of tech + implementation platform:

### Access Control Models

- **Programmatic Access Control**: Matrix of user privileges stored in DB applied programmatically. Includes roles, groups, individual users, collections, workflows, processes. Granular.
- **Discretionary Access Control (DAC)**: Constraints based on users or named groups. Owners of resources/functions delegate access permissions. Very complex to design and manage.
- **Mandatory Access Control (MAC)**: Centrally controlled system of controls. Very different from DAC. Associated with military clearance-based systems.
- **Role-based Access Control (RBAC)**: Named roles designed to which access privileges assigned. Users assigned 1+ roles. Enhanced management over models. Easy to revoke and define group membership.

### Access Control Types (Cosmo brain: control/ directory)

- **Vertical access control** — different privilege levels (admin vs user)
- **Horizontal access control** — same level but different resources (user A vs user B)
- **Context-dependent access control** — access depends on application state/context
- **CORS access control** — cross-origin resource sharing
- **DOM-based access control** — client-side access control

### Prevention Principles (from Access_Control-Priv_Esc.md)

- Do not rely on obfuscation for access control
- All non-publicly accessible resources should be denied by default
- Use single application-wide mechanisms for enforcing access controls
- Mandate developers to declare allowed access for each resource and deny by default
- Audit and test to ensure they are working as designed

## 8. Bounded Intelligence Security (Cosmo brain: security/Bounded Intelligence Security™ (BIS™).md)

The BIS™ framework defines bounded intelligence security principles:

- Security models must be formally defined independent of implementation
- Access control is dependent on authentication and session management
- Authentication identifies and confirms user
- Session management identifies which requests are made by same user
- Access control determines whether a user can carry out an action

## 9. Risk Compliance Model (Cosmo brain: security/Risk_Compliance_Model.md)

The risk compliance model defines:

- Sector profiles with regulation and compliance requirements
- Market structure analysis with risk and crisis assessment
- Technology and data governance
- Workforce and skills security
- Sustainability and ESG compliance
- Operations models and processes

## 10. Cross-Domain Composition

This skill should be used in conjunction with `amos-cross-domain-tensor-composition-governor` when the cross-domain composition involves C09/C10/Runtime tensors. The composition governor validates axis compatibility; this bridge governor provides the domain-specific pipeline logic.

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
