---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Cross Plane Resolution
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

# CROSS PLANE RESOLUTION

## 0. Status

Knowledge-plane artifact. `AMOS_MODEL` · `CONDITIONAL` · implementation `PARTIAL`.

This is a **governing invariant** sourced from the MECE architecture's strict responsibility partition. It defines how references that span multiple physical planes are resolved without violating the MECE boundary that assigns each plane exactly one responsibility domain.

## 1. Purpose

`CROSS PLANE RESOLUTION` establishes the protocol for resolving a reference, query, or operation that touches artifacts in more than one physical plane. Because the AMOS architecture enforces a strict MECE partition — every numbered plane owns exactly one responsibility domain — cross-plane operations cannot be handled by implicit dual ownership. They require an explicit, typed dependency edge with authority, freshness, and scope verification at each plane boundary.

This invariant exists because without it, cross-plane references would silently blur responsibility boundaries, creating:
- **Implicit dual ownership** — two planes both believe they own the same artifact.
- **Authority leakage** — a cognitive plane's capability is treated as authority in a control-plane context.
- **Scope leak** — an artifact resolved in one regime is applied in another without a bridge.

### Failure modes prevented

- `SCOPE_LEAK` — cross-plane reference carries scope from one plane into another without explicit bridge.
- `AUTHORITY_ESCALATION` — a plane with capability but not authority resolves a cross-plane reference as if authorized.
- `REGIME_DRIFT` — resolution in one regime is applied in another without verification.
- `STALE_READ` — a cross-plane reference resolves to a stale version of the target artifact.

## 2. Definition

The MECE architecture states:

```text
FUNCTIONAL OWNERSHIP
!= PHYSICAL STORAGE
!= AUTHORITY PRECEDENCE
!= RUNTIME CALL ORDER
!= EVIDENCE / VALIDATION STATUS
```

And the partition invariant:

```text
{01..25} = A ∪ B ∪ C ∪ D ∪ E ∪ F
A ∩ B ∩ C ∩ D ∩ E ∩ F = ∅
```

Cross-plane resolution is the process of traversing a typed dependency edge from one plane to another while preserving:
1. The authority context of the originating plane.
2. The ownership boundary of the target plane.
3. The freshness and scope of both planes.
4. The epistemic class of the resolved artifact.

A cross-plane resolution is **valid** only if:
- The dependency edge is explicitly declared (not inferred).
- The target plane's ownership is respected (the originating plane does not acquire ownership by resolving).
- Authority is revalidated at the target plane boundary.
- The resolution result carries the RSCF metadata of both planes.

## 3. AMOS Architecture Context

| Domain | Planes | Role in cross-plane resolution |
|---|---|---|
| **A — Normative & Governance** | `01_CANON`, `23_OPERATING_MODEL` | Provides the laws that govern cross-plane edges |
| **B — Execution Core & Effect Governance** | `02_KERNEL`, `03_CONTROL_PLANE` | Enforces authority revalidation at plane boundaries |
| **D — Information, Memory, State & Model Substrate** | `11_KNOWLEDGE`, `13_MODELS`, `12_STATE` | Stores the typed dependency edges |
| **E — Interaction, Security & Effect Adapters** | `09_PROTOCOLS`, `18_SECURITY` | Defines the handoff semantics for cross-plane traversal |

The architecture's functional field table (Section 3) shows that every field has **one primary physical owner** with **many typed dependencies**. Cross-plane resolution is the mechanism that traverses those dependency edges.

```text
ONE PRIMARY OWNER + MANY TYPED DEPENDENCIES
```

## 4. Invariants / Rules

1. **INV-CPR-01**: A cross-plane reference must be an explicitly declared dependency edge; inferred or implicit cross-plane references are invalid.
2. **INV-CPR-02**: The originating plane does not acquire ownership of the target artifact by resolving the reference.
3. **INV-CPR-03**: Authority must be revalidated at the target plane boundary; the originating plane's authority context does not transfer automatically.
4. **INV-CPR-04**: The resolution result must carry the RSCF metadata (scope, regime, freshness, epistemic class) of both the originating and target planes.
5. **INV-CPR-05**: Cross-regime resolution requires an explicit bridge; a reference valid in regime R1 must be independently verified in regime R2.
6. **INV-CPR-06**: If the target artifact is `UNKNOWN/GAP`, the resolution fails closed — no fabrication of the target is permitted.
7. **INV-CPR-07**: The resolution path must be acyclic; circular cross-plane references indicate a structural error and must be detected and rejected.

## 5. Relationships

- **Governed by**: [[01_CANON/01_CANON_README|01_CANON_README]] — canon defines the laws governing cross-plane edges.
- **Enforced by**: [[03_CONTROL_PLANE/03_CONTROL_PLANE_README|CONTROL_PLANE_README]] — control plane revalidates authority at boundaries.
- **Protocol defined by**: [[09_PROTOCOLS/09_PROTOCOLS_README|09_PROTOCOLS_README]] — protocols define handoff semantics.
- **Security boundary**: [[18_SECURITY/18_SECURITY_README|18_SECURITY_README]] — security enforces trust-boundary checks at plane crossings.
- **Related concept**: [[11_KNOWLEDGE/stubs/CROSS_PLANE_MODEL_RESOLUTION|CROSS_PLANE_MODEL_RESOLUTION]] — specialized cross-plane resolution for model artifacts.
- **Related concept**: [[11_KNOWLEDGE/stubs/LOCAL_BASENAME_RESOLUTION|LOCAL_BASENAME_RESOLUTION]] — intra-plane resolution that cross-plane resolution builds upon.
- **Architecture reference**: [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]] — Section 2 (MECE partition), Section 3 (functional fields).

## 6. What Happens When Violated

| Violation | Consequence |
|---|---|
| Implicit cross-plane reference | `SCOPE_LEAK` — undeclared dependency creates hidden coupling |
| Authority not revalidated at boundary | `AUTHORITY_ESCALATION` — originating plane's authority leaks to target |
| Circular cross-plane reference | `STRUCTURAL_ERROR` — infinite resolution loop, system must detect and reject |
| Target artifact fabricated | `UNKNOWN_AS_VALID` — missing artifact invented to complete resolution |

In all cases, the system must **fail closed**: the resolution is rejected, the originating operation is held, and a receipt recording the violation is emitted.

## 7. Worked Semantics

Given a cross-plane resolution operation:

1. **Admit** — resolve the originating reference by id + version; unresolved id ⇒ `UNKNOWN/GAP`, fail closed.
2. **Identify target plane** — the dependency edge explicitly names the target plane and artifact.
3. **Verify edge** — the dependency edge must be declared in the schema; undeclared edges are rejected.
4. **Revalidate authority** — at the target plane boundary, authority is independently checked; the originating plane's authority does not transfer.
5. **Resolve target** — the target artifact is resolved in its owning plane, with its own RSCF metadata.
6. **Merge metadata** — the resolution result carries RSCF metadata from both planes, with confidence ≤ weakest load-bearing premise.
7. **Commit or hold** — on any failed check: preserve unaffected state, invalidate dependent descendants only, record receipt.

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

Implementation binding, empirical validation, and cross-artifact consistency checks remain `OPEN` (`UNKNOWN/GAP`). The MECE partition is structurally coherent in the vault, but a deployed cross-plane resolution engine with cycle detection and authority revalidation is not yet established.

## 11. Falsifiers

- **F1**: canonical source contradicts declared semantics.
- **F2**: executed test violates a stated invariant (e.g., a cross-plane reference resolves without authority revalidation).
- **F3**: artifact promotes `UNKNOWN` to `PASS`.

## 12. RSCF Status

```text
state:          DERIVED
claim_class:    DERIVED
provenance:     AMOS_corpus
scope:          AMOS_general
```

This artifact is a `DERIVED` knowledge-plane representation of the MECE architecture's cross-plane dependency protocol. It does not promote to `SOURCE_CLAIM` without governed successor evidence.

## 13. Cross-Plane Bindings

- Governed by canon — [[01_CANON/01_CANON_README|01_CANON_README]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- Kernel interaction — [[02_KERNEL/02_KERNEL_README|KERNEL_README]]
- Control-plane gates — [[03_CONTROL_PLANE/03_CONTROL_PLANE_README|CONTROL_PLANE_README]]
- Observed by — [[17_OBSERVABILITY/17_OBSERVABILITY_README|17_OBSERVABILITY_README]] · never treated as authority
- Recovered via operations — [[20_OPERATIONS/20_OPERATIONS_README|20_OPERATIONS_README]]
