---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Consequential Effect Receipts
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

# CONSEQUENTIAL EFFECT RECEIPTS

## 0. Status

Knowledge-plane artifact. `AMOS_MODEL` · `CONDITIONAL` · implementation `PARTIAL`.

This is a **governing invariant** sourced from the AMOS Core Laws (L7 — Authority/Governance, L10 — Failure/Recovery) and the MECE architecture's commit firewall. It mandates that every consequential effect — any operation that produces a durable, externally visible, or irreversible state change — must produce a verifiable receipt before the effect is considered committed.

## 1. Purpose

`CONSEQUENTIAL EFFECT RECEIPTS` ensures that no durable effect enters the system without a cryptographic, replayable, and auditable receipt binding the effect to its authority, capability, epoch, state hash, and provenance chain. The receipt is not an afterthought log entry; it is a **load-bearing artifact** that the control plane requires before admitting the effect.

This invariant exists because without receipts, the system cannot distinguish:
- A committed effect from a proposed one (`PROPOSAL ≠ COMMIT`).
- An authorized effect from an unauthorized one (`CAPABILITY ≠ AUTHORITY`).
- A fresh effect from a stale replay (`PLANNING-TIME ALLOW ≠ COMMIT-TIME ALLOW`).
- A complete effect from a partial commit (`SILENT_PARTIAL_COMMIT`).

### Failure modes prevented

- `SILENT_PARTIAL_COMMIT` — an effect is partially applied without a record of what was committed and what was not.
- `AUTHORITY_ESCALATION` — an effect is committed without evidence of the authority grant under which it was admitted.
- `PROVENANCE_LOSS` — an effect's causal chain is lost, making rollback and audit impossible.
- `STALE_READ` — a replayed effect is committed again without freshness verification.

## 2. Definition

The invariant is formalized in the AMOS architecture's authority and commit firewall (Section 11):

```text
PROPOSAL != COMMIT
APPROVAL != FINALITY
MESSAGE != ARTIFACT
```

And in the Enforcement Root Attestation (v42+) receipt structure:

```text
R_receipt = BLAKE3(ArtifactID ∥ Epoch ∥ StateHash_{t-1} ∥ PayloadHash)
```

A **consequential effect receipt** is a typed record containing at minimum:

| Field | Description |
|---|---|
| `effect_id` | Unique identifier for the effect |
| `artifact_id` | The artifact producing the effect |
| `epoch` | The fencing epoch in which the effect was committed |
| `authority_ref` | The epoch-valid authority grant authorizing the effect |
| `capability_ref` | The capability module invoked |
| `state_hash_before` | Cryptographic hash of state before the effect |
| `state_hash_after` | Cryptographic hash of state after the effect |
| `payload_hash` | Hash of the effect payload |
| `integrity_hash` | BLAKE3/SHA-256 of the above fields |
| `provenance_chain` | Full ancestry from source claim to committed effect |
| `commit_timestamp` | Temporal marker for freshness verification |
| `rollback_delta` | Forward-apply and reverse-rollback deltas |

The receipt must be produced **before** the effect is considered committed, not after.

## 3. AMOS Architecture Context

| Domain | Planes | Role |
|---|---|---|
| **B — Execution Core & Effect Governance** | `03_CONTROL_PLANE`, `04_RUNTIME` | The control plane requires the receipt before admitting the effect; the runtime produces it |
| **D — Information, Memory, State & Model Substrate** | `12_STATE`, `16_SCHEMAS` | State and schema layers store and type the receipts |
| **F — Assurance, Learning & Lifecycle Evidence** | `17_OBSERVABILITY`, `20_OPERATIONS` | Observability and operations consume receipts for audit and recovery |

The governed end-to-end loop makes the receipt step explicit:

```text
→ COMMIT-TIME REVALIDATION
→ TOOL / INTERFACE EFFECT
→ OBSERVABILITY / TEST RECEIPT
```

The AGENTS.md contract also states: "Consequential effects require receipts appropriate to the active control-plane contract."

## 4. Invariants / Rules

1. **INV-CER-01**: `∀ effect e, Consequential(e) ⇒ ∃ receipt r: Bind(e, r) ∧ Verify(r.integrity_hash)`
2. **INV-CER-02**: A receipt must be produced before the effect is considered committed; `¬∃ receipt ⇒ effect_status = HELD`.
3. **INV-CER-03**: The receipt must bind both `authority_ref` and `capability_ref`; either missing ⇒ fail closed.
4. **INV-CER-04**: Receipts are immutable once written; they may be superseded by a new receipt but never silently altered.
5. **INV-CER-05**: The receipt's `state_hash_before` and `state_hash_after` must be cryptographically linked to the state journal; mismatch ⇒ `SILENT_PARTIAL_COMMIT` detected.
6. **INV-CER-06**: Receipts must be replayable; given a receipt, the system can reconstruct the effect and verify it against the current state.
7. **INV-CER-07**: The `rollback_delta` in the receipt must satisfy `Rollback(Δ) ∘ Apply(Δ) = I` (reversibility invariant).

## 5. Relationships

- **Required by**: [[03_CONTROL_PLANE/03_CONTROL_PLANE_README|CONTROL_PLANE_README]] — the control plane gates commit on receipt existence.
- **Stored in**: [[12_STATE/12_STATE_README|12_STATE_README]] — state journal persists receipts.
- **Typed by**: [[16_SCHEMAS/16_SCHEMAS_README|16_SCHEMAS_README]] — schemas define the receipt structure.
- **Audited by**: [[17_OBSERVABILITY/17_OBSERVABILITY_README|17_OBSERVABILITY_README]] — observability consumes receipts for trace analysis.
- **Recovered via**: [[20_OPERATIONS/20_OPERATIONS_README|20_OPERATIONS_README]] — operations uses receipts for rollback and incident response.
- **Related concept**: [[11_KNOWLEDGE/stubs/CAPABILITY_AUTHORITY_SEPARATION|CAPABILITY_AUTHORITY_SEPARATION]] — receipts must record both capability and authority.
- **Related concept**: [[11_KNOWLEDGE/stubs/EPOCH_SEPARATION|EPOCH_SEPARATION]] — receipts bind effects to fencing epochs.
- **Architecture reference**: [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]] — Section 11 (Authority and commit firewall).

## 6. What Happens When Violated

| Violation | Consequence |
|---|---|
| Effect committed without receipt | `SILENT_PARTIAL_COMMIT` — no audit trail, no rollback path |
| Receipt missing authority_ref | `AUTHORITY_ESCALATION` — effect admitted without authorization evidence |
| Receipt state hash mismatch | `STALE_READ` — effect applied to unexpected state, possible corruption |
| Receipt not replayable | `PROVENANCE_LOSS` — causal chain broken, rollback impossible |
| Rollback delta non-reversible | `IRREVERSIBLE_EFFECT` — state cannot be restored to pre-effect baseline |

In all cases, the system must **fail closed**: the effect is held, not committed, and an alert is raised to `17_OBSERVABILITY` and `20_OPERATIONS`.

## 7. Worked Semantics

Given a consequential effect within the Knowledge plane:

1. **Admit** — resolve the effect artifact by id + version; unresolved id ⇒ `UNKNOWN/GAP`, fail closed.
2. **Bind scope** — declare domain / regime / H-M-L applicability before any mutation.
3. **Check authority** — `authority_ref` must be epoch-valid; capability alone never authorizes.
4. **Compute state hashes** — capture `state_hash_before` before applying the effect.
5. **Apply effect** — produce the state mutation delta (forward-apply + reverse-rollback).
6. **Compute receipt** — `R = BLAKE3(ArtifactID ∥ Epoch ∥ StateHash_{before} ∥ PayloadHash)`.
7. **Verify integrity** — `Verify(R.integrity_hash)` must pass before commit.
8. **Commit or hold** — on any failed check: preserve unaffected state, invalidate dependent descendants only, record the failed receipt with violation details.

## 8. Promotion-Gate Checklist

- [ ] typed schema bound to this artifact
- [ ] identity + versioning implemented
- [ ] negative cases covered (missing · malformed · stale · unauthorized input)
- [ ] provenance edges persisted and validated
- [ ] rollback basin demonstrated for consequential effects
- [ ] executed validation receipt specific to this artifact
- [ ] unresolved critical gaps registered as `UNKNOWN/GAP` (visible)

## 9. Validation

No artifact-specific executor yet; executed OS validators exist as pattern ([[ROUTING_POLICY_VALIDATION_RECEIPT]] · [[AUTHZ_ENGINE_VALIDATION_RECEIPT]]). The Enforcement Root Attestation (v42+) includes a `RELEASE_LEDGER` with receipt semantics: same key+digest → `ALREADY_COMMITTED`, same key+different → `BLOCK`, crash → `RECONCILE_EFFECT`. Required tests before promotion: identity, type-contract, negative-case, authority boundary, rollback.

## 10. Gaps

Implementation binding, empirical validation, and cross-artifact consistency checks remain `OPEN` (`UNKNOWN/GAP`). The enforcement trust contract (v43) establishes receipt semantics in the brain source code (54 self-tests, 300k fuzz), but OS-wide receipt production and verification closure is not yet established.

## 11. Falsifiers

- **F1**: canonical source contradicts declared semantics.
- **F2**: executed test violates a stated invariant (e.g., an effect is committed without a verifiable receipt).
- **F3**: artifact promotes `UNKNOWN` to `PASS`.

## 12. RSCF Status

```text
state:          DERIVED
claim_class:    DERIVED
provenance:     AMOS_corpus
scope:          AMOS_general
```

This artifact is a `DERIVED` knowledge-plane representation of the `SOURCE_CLAIM` invariant in [[01_CANON/01_CORE_LAWS/AMOS_CORE_LAWS|AMOS_CORE_LAWS]] (L7, L10). It does not promote to `SOURCE_CLAIM` without governed successor evidence.

## 13. Cross-Plane Bindings

- Governed by canon — [[01_CANON/01_CANON_README|01_CANON_README]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- Kernel interaction — [[02_KERNEL/02_KERNEL_README|KERNEL_README]]
- Control-plane gates — [[03_CONTROL_PLANE/03_CONTROL_PLANE_README|CONTROL_PLANE_README]]
- Observed by — [[17_OBSERVABILITY/17_OBSERVABILITY_README|17_OBSERVABILITY_README]] · never treated as authority
- Recovered via operations — [[20_OPERATIONS/20_OPERATIONS_README|20_OPERATIONS_README]]
