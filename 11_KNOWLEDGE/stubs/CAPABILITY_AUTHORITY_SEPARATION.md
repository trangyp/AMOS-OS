---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Capability Authority Separation
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# CAPABILITY AUTHORITY SEPARATION

## 0. Status

Knowledge-plane artifact. `AMOS_MODEL` · `CONDITIONAL` · implementation `PARTIAL`.

This is a **governing invariant** sourced from the AMOS Core Laws (L7 — Authority / Governance) and the MECE architecture's authority firewall. It is not a convenience convention; it is a constitutional separation that prevents capability possession from being conflated with authorization to act.

## 1. Purpose

`CAPABILITY · AUTHORITY SEPARATION` establishes that the **possession of a capability** (the ability to perform an operation) and the **grant of authority** (the permission to perform that operation in a given epoch, scope, and context) are distinct, independently verifiable, and must both be satisfied before any durable effect is committed.

This invariant exists because without it, any agent or component that *can* do something would be treated as *authorized* to do it — collapsing the distinction between reachability and permission and enabling silent authority escalation.

### Failure mode prevented

`AUTHORITY_ESCALATION` — an agent with capability access bypasses the control-plane authorization gate because the system conflates "can do" with "may do."

## 2. Definition

The invariant is formalized in the AMOS architecture as:

```text
CAPABILITY != AUTHORITY
IDENTITY != CAPABILITY
TRUST SCORE != ROOT KEY
PLANNING-TIME ALLOW != COMMIT-TIME ALLOW
```

And in the Enforcement Root Attestation (v42+) separability law:

```text
Capability != Reachability != Identity != Authority
            != Observability != Enforcement != Commitment != Consequence
```

**Capability** = a typed, versioned procedure module (skill, tool, workflow) that can perform an operation. Owned by planes `07_SKILLS`, `14_TOOLS`, `26_WORKFLOWS`.

**Authority** = an epoch-valid, scope-bound grant issued by the `03_CONTROL_PLANE` that permits a specific identity to invoke a capability for a specific effect class. Authority is never implied by capability possession; it must be explicitly granted, freshness-checked, and revalidated at commit time.

## 3. AMOS Architecture Context

This invariant sits at the intersection of three MECE partition domains:

| Domain | Planes | Role |
|---|---|---|
| **B — Execution Core & Effect Governance** | `02_KERNEL`, `03_CONTROL_PLANE`, `04_RUNTIME` | Enforces the separation at commit time |
| **C — Cognitive Capability & Orchestration** | `05_COGNITIVE_ORGANISM`, `06_AGENTS`, `07_SKILLS` | Possesses capabilities but cannot self-authorize |
| **E — Interaction, Security & Effect Adapters** | `18_SECURITY` | Enforces trust-boundary checks |

The governed end-to-end loop makes the separation explicit at two critical points:

1. **PROPOSE → RUNTIME BINDS STATE** — the runtime binds the agent's capability to the current state but does not grant authority.
2. **CONTROL-PLANE AUTHORITY / FRESHNESS / CONFLICT CHECK → COMMIT-TIME REVALIDATION** — the control plane independently verifies authority before any durable effect is admitted.

No arrow in the loop silently upgrades capability to authority.

## 4. Invariants / Rules

1. **INV-CAS-01**: `∀ op, Capability(op) ∧ ¬Authority(op, epoch, scope) ⇒ ¬MayCommit(op)`
2. **INV-CAS-02**: Authority must be epoch-valid; stale authority tokens are rejected at commit time.
3. **INV-CAS-03**: Authority is scope-bound; cross-scope invocation requires an explicit bridge, not implicit transfer.
4. **INV-CAS-04**: Planning-time allowance does not survive to commit time; commit-time revalidation is mandatory.
5. **INV-CAS-05**: Capability modules (skills, tools) cannot create infrastructure authority — they are deployment/capability representations, not root authority.
6. **INV-CAS-06**: Cognitive components (`05_COGNITIVE_ORGANISM`) cannot authorize their own durable effects; their default authority is cognitive/proposal only.

## 5. Relationships

- **Governs**: [[03_CONTROL_PLANE/03_CONTROL_PLANE_README|CONTROL_PLANE_README]] — the control plane is the sole issuer of authority grants.
- **Constrained by**: [[01_CANON/01_CORE_LAWS/AMOS_CORE_LAWS|AMOS_CORE_LAWS]] — L7 (Authority/Governance) law family.
- **Enforced through**: [[02_KERNEL/02_KERNEL_README|KERNEL_README]] — kernel primitives enforce the separation at the deterministic execution layer.
- **Observed by**: [[17_OBSERVABILITY/17_OBSERVABILITY_README|17_OBSERVABILITY_README]] — observability records capability invocations and authority grants separately; observation never creates authority.
- **Related concept**: [[11_KNOWLEDGE/stubs/CONSEQUENTIAL_EFFECT_RECEIPTS|CONSEQUENTIAL_EFFECT_RECEIPTS]] — receipts must record both the capability invoked and the authority grant under which it was invoked.
- **Architecture reference**: [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]] — Section 11 (Authority and commit firewall).

## 6. What Happens When Violated

| Violation | Consequence |
|---|---|
| Capability treated as authority | `AUTHORITY_ESCALATION` — agent performs un-authorized durable effects |
| Planning-time allow treated as commit-time allow | `STALE_READ` — committed effect based on revoked or expired grant |
| Cognitive component self-authorizes | `SILENT_PARTIAL_COMMIT` — durable effect admitted without control-plane gate |
| Trust score treated as root key | `PROVENANCE_LOSS` — identity-based trust bypasses cryptographic authority verification |

In all cases, the system must **fail closed**: the effect is held, not committed, and a receipt recording the violation is emitted to `17_OBSERVABILITY`.

## 7. Worked Semantics

Given an operation invoking a capability within the Knowledge plane:

1. **Admit** — resolve the capability artifact by id + version; unresolved id ⇒ `UNKNOWN/GAP`, fail closed.
2. **Bind scope** — declare domain / regime / H-M-L applicability before any mutation.
3. **Check authority** — `authority_ref` must be epoch-valid and scope-matching; capability alone never authorizes.
4. **Validate preconditions** — dependency closure traversed to the smallest result-changing set.
5. **Propose** — candidate state is non-authoritative until control-plane gates pass (`PROPOSAL ≠ COMMIT`).
6. **Commit or hold** — on any failed premise: preserve unaffected state, invalidate dependent descendants only, record receipt.

## 8. Promotion-Gate Checklist

- [ ] typed schema bound to this artifact
- [ ] identity + versioning implemented
- [ ] negative cases covered (missing · malformed · stale · unauthorized input)
- [ ] provenance edges persisted and validated
- [ ] rollback basin demonstrated for consequential effects
- [ ] executed validation receipt specific to this artifact
- [ ] unresolved critical gaps registered as `UNKNOWN/GAP` (visible)

## 9. Validation

No artifact-specific executor yet; executed OS validators exist as pattern ([[ROUTING_POLICY_VALIDATION_RECEIPT]] · [[AUTHZ_ENGINE_VALIDATION_RECEIPT]]). Required tests before promotion: identity, type-contract, negative-case (missing/malformed/stale input), authority boundary, rollback.

## 10. Gaps

Implementation binding, empirical validation, and cross-artifact consistency checks remain `OPEN` (`UNKNOWN/GAP`). The separability law is proven in the enforcement root attestation self-tests (v42+, 30 tests) but the full OS-wide enforcement chain closure is not yet established.

## 11. Falsifiers

- **F1**: canonical source contradicts declared semantics.
- **F2**: executed test violates a stated invariant.
- **F3**: artifact promotes `UNKNOWN` to `PASS`.

## 12. RSCF Status

```text
state:          DERIVED
claim_class:    DERIVED
provenance:     AMOS_corpus
scope:          AMOS_general
```

This artifact is a `DERIVED` knowledge-plane representation of the `SOURCE_CLAIM` invariant in [[01_CANON/01_CORE_LAWS/AMOS_CORE_LAWS|AMOS_CORE_LAWS]] (L7). It does not promote to `SOURCE_CLAIM` without governed successor evidence.

## 13. Cross-Plane Bindings

- Governed by canon — [[01_CANON/01_CANON_README|01_CANON_README]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- Kernel interaction — [[02_KERNEL/02_KERNEL_README|KERNEL_README]]
- Control-plane gates — [[03_CONTROL_PLANE/03_CONTROL_PLANE_README|CONTROL_PLANE_README]]
- Observed by — [[17_OBSERVABILITY/17_OBSERVABILITY_README|17_OBSERVABILITY_README]] · never treated as authority
- Recovered via operations — [[20_OPERATIONS/20_OPERATIONS_README|20_OPERATIONS_README]]
