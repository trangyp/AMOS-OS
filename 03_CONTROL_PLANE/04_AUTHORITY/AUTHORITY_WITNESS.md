---
title: AUTHORITY WITNESS
type: authority
source: 03_CONTROL_PLANE/04_AUTHORITY
tags:
- control_plane
- authority
- note
- canon/control-plane
rscf:
  state: SOURCE_CLAIM
  claim_class: CONDITIONAL
  provenance: AMOS_corpus
  scope: authority_governance
---


# AUTHORITY_WITNESS.md

---
title: AMOS Authority Witness
artifact: "AUTHORITY_WITNESS.md"
origin_architect: "Trang Phan"
steward: "Trang Phan"
system: "AMOS OS"
artifact_class: "GOVERNED_AUTHORITY_EVIDENCE_CONTRACT"
status: "PROPOSED / STRUCTURALLY_COMPLETE / IMPLEMENTATION-UNVALIDATED"
epistemic_class: "MODEL"
version: "1.0.0"
updated: "2026-08-26"
default_state: "UNKNOWN_GAP"
authority_semantics: "EVIDENCE_OF_RESOLVED_AUTHORITY_NOT_AUTHORITY_CREATION"
---

# AMOS Authority Witness

## 0. Status

`AUTHORITY_WITNESS.md` defines the AMOS OS contract for producing, transporting, validating, revalidating, consuming, invalidating, and auditing an `AUTHORITY_WITNESS`.

An Authority Witness is a provenance-bound representation of a prior authority resolution.

It answers:

> **What authority was resolved, for which principal, operation, capability, target, effect, transaction, scope, regime, and authoritative state—and what must remain true before that resolution may be relied upon?**

An Authority Witness is not authority itself.

It does not create authority.

It does not grant authority.

It does not extend authority.

It does not make policy.

It does not execute a capability.

It does not commit an effect.

It does not prove that an operation was ultimately performed.

It does not remain valid indefinitely merely because it was valid when issued.

Canonical distinction:

```text
AUTHORITY SOURCE
      ↓
AUTHORITY RESOLUTION
      ↓
AUTHORITY WITNESS
      ↓
DOWNSTREAM VALIDATION
      ↓
COMMIT-TIME REVALIDATION
      ↓
EFFECT ELIGIBILITY
```

never:

```text
WITNESS EXISTS
      ↓
ACTION AUTHORIZED FOREVER
```

---

# 1. Purpose

The Authority Witness exists to preserve the decision-relevant authority state established by the Authority Resolver so downstream AMOS control-plane components do not have to rely on:

```text
free-form prose;

agent memory;

implicit assumptions;

role names;

cached conclusions without dependencies;

policy decisions masquerading as authority;

capability availability;

historical execution;

or unbound authorization tokens.
```

The witness provides a typed bridge between:

```text
AUTHORITY RESOLUTION
```

and:

```text
POLICY VALIDATION

TRANSACTION VALIDATION

OBSERVABILITY VALIDATION

EFFECT PREPARATION

COMMIT-TIME AUTHORITY VALIDATION

EFFECT RELEASE
```

---

# 2. Core Laws

```text
AUTHORITY_WITNESS != AUTHORITY

AUTHORITY_WITNESS != AUTHORITY_SOURCE

AUTHORITY_WITNESS != POLICY

AUTHORITY_WITNESS != CAPABILITY

AUTHORITY_WITNESS != EXECUTION

AUTHORITY_WITNESS != COMMIT

AUTHORITY_WITNESS != RECEIPT

AUTHORITY_WITNESS != EFFECT_RELEASE_STATE

WITNESS_PRESENT != WITNESS_VALID

WITNESS_VALID_AT_T0 != WITNESS_VALID_AT_T1

SIGNATURE_PRESENT != SIGNATURE_VALID

SIGNATURE_VALID != CURRENT_AUTHORITY

AUTHORITY_ID_PRESENT != AUTHORITY_VALID

AUTHORITY_REFERENCE != AUTHORITY_PROOF

AUTHORITY_AT_PLAN_TIME != AUTHORITY_AT_COMMIT_TIME

AUTHORITY_TO_PROPOSE != AUTHORITY_TO_COMMIT

AUTHORITY_TO_COMMIT != EFFECT_COMPLETED

CAPABILITY != AUTHORITY

POLICY_ALLOW != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != AUTHORIZED
```

---

# 3. Architectural Position

```text
PRINCIPAL / IDENTITY
        ↓
AUTHORITY SOURCES
        ↓
AUTHORITY REGISTRY
        ↓
AUTHORITY RESOLVER
        ↓
AUTHORITY RESOLUTION
        ↓
AUTHORITY WITNESS
        ↓
POLICY ENGINE
        +
RESOLVED CAPABILITY CONTRACT
        +
SEMANTIC TRANSACTION
        +
CONSTRAINT CONTEXT
        +
OBSERVABILITY ENVELOPE
        +
EFFECT INTENT
        ↓
COMMIT GUARD
        ↓
COMMIT-TIME AUTHORITY REVALIDATION
        ↓
EFFECT RELEASE STATE
        ↓
RECEIVER / SERVICE
        ↓
RECEIVER-ATTESTED RECEIPT
```

The Authority Witness belongs to the infrastructure/control-plane layer.

Domain Skills MAY request authority-dependent actions.

Domain Skills MUST NOT manufacture their own authoritative witness and then treat that self-authored witness as infrastructure authority.

---

# 4. Responsibility Boundary

The Authority Witness owns representation of:

```text
resolved authority identity;

principal binding;

operation binding;

capability binding;

target binding;

effect binding;

transaction binding;

idempotency binding where required;

scope;

regime;

authority constraints;

delegation lineage references;

authority provenance;

authority read-set identity;

authority-registry identity;

effect-ledger identity where required;

observability-envelope binding where required;

resolved-capability-contract binding where required;

issuance time;

validity envelope;

revalidation requirements;

witness integrity;

invalidation state;

confidence ceiling.
```

It does NOT own:

```text
authentication;

authority issuance;

authority delegation;

authority revocation;

policy authorship;

policy resolution;

capability implementation;

transaction execution;

effect dispatch;

release-ledger mutation;

receiver receipt generation;

cryptographic trust-root administration;

domain-specific business rules.
```

---

# 5. Authority Witness Definition

Conceptually:

```text
AuthorityWitness =
Bind(
    AuthorityResolution,
    Principal,
    Operation,
    Capability,
    Target,
    Effect,
    Transaction,
    Scope,
    Regime,
    Constraints,
    AuthorityState,
    RelevantControlPlaneState
)
```

The witness is therefore a bounded evidence object.

It is not a bearer token whose mere possession grants unrestricted authority.

---

# 6. Canonical Witness Object

```yaml
authority_witness:
  schema: "AMOS.AUTHORITY_WITNESS"
  schema_version: "1.0"

  witness_id: string
  witness_version: string
  witness_digest: string

  state:
    - VALID
    - VALID_CONDITIONAL
    - REVALIDATE
    - INVALID
    - EXPIRED
    - REVOKED
    - CONFLICT
    - SUPERSEDED
    - QUARANTINED
    - UNKNOWN_GAP

  resolution:
    resolution_id: string
    resolver_id: string
    resolver_version: string
    resolved_at: timestamp

  authority:
    authority_id: string
    authority_version: string
    authority_digest: string
    authority_class: string

  principal:
    principal_id: string
    principal_type: string
    authenticated_identity_ref: null

  operation:
    operation_id: string
    operation_class: string

  capability:
    capability_id: null
    capability_version: null
    resolved_capability_contract_hash: null

  target:
    target_id: null
    target_class: null
    target_digest: null

  effect:
    effect_class: string
    effect_digest: null
    idempotency_key: null

  transaction:
    transaction_id: null
    semantic_transaction_hash: null

  scope: {}

  regime: {}

  constraints: []

  delegation:
    lineage_refs: []
    root_authority_ref: null

  authority_read_set: []

  authority_registry:
    registry_id: null
    registry_generation: null
    registry_version: null
    registry_hash: null

  effect_release_state:
    ledger_id: null
    ledger_generation: null
    ledger_version: null
    ledger_hash: null

  observability:
    envelope_id: null
    envelope_hash: null

  temporal:
    issued_at: timestamp
    valid_from: timestamp
    valid_until: null
    revalidate_after: null

  provenance:
    source_refs: []
    dependency_refs: []
    ancestry_refs: []

  integrity:
    canonicalization_version: string
    signature_algorithm: null
    signer_id: null
    signature: null

  uncertainty: {}

  falsifiers: []

  confidence_ceiling: null

  commit_revalidation_required: true
```

---

# 7. Witness Identity

A witness MUST possess stable identity sufficient to distinguish:

```text
same logical witness;

new witness version;

different authority resolution;

tampered witness;

superseding witness.
```

Recommended identity:

```text
WitnessIdentity =
(
    witness_id,
    witness_version,
    witness_digest
)
```

A `witness_id` alone is insufficient where witness contents may change.

---

# 8. Witness Digest

Conceptually:

```text
witness_digest =
H(
    resolution
    + authority identity
    + principal
    + operation
    + capability
    + target
    + effect
    + transaction
    + scope
    + regime
    + constraints
    + authority read set
    + authority registry identity
    + effect-ledger identity
    + observability binding
    + temporal envelope
    + provenance
)
```

Exact serialization, canonicalization, hashing, and cryptographic algorithms belong to implementation specifications.

The architecture requires deterministic binding semantics, not one particular hash algorithm.

---

# 9. Witness Integrity Law

If any load-bearing field changes:

```text
principal

operation

capability

target

effect

transaction

scope

constraints

authority identity

authority-registry identity

ledger identity
```

then the prior witness MUST NOT silently remain valid for the modified request.

---

# 10. Principal Binding

The witness MUST identify the principal for whom authority was resolved.

```yaml
principal:
  principal_id: "..."
  principal_type: "HUMAN | AGENT | SERVICE | ORGANIZATION | SYSTEM"
```

Required invariant:

```text
Witness.principal
=
CurrentRequest.principal
```

unless an independently validated principal substitution or delegation mechanism explicitly permits otherwise.

---

# 11. Principal Substitution Failure

The following is invalid:

```text
Witness:
principal = AGENT_A

Current action:
principal = AGENT_B
```

unless a new authority resolution establishes `AGENT_B`.

A witness is not transferable merely because two principals:

```text
share a role;

share a tool;

share a service;

share a parent agent;

share a team;

or have similar names.
```

---

# 12. Operation Binding

The witness MUST bind the authority decision to the operation that was evaluated.

Examples:

```text
READ

CREATE

UPDATE

DELETE

MOVE

SHARE

SEND

EXECUTE

PROMOTE

PUBLISH

COMMIT

REVOKE
```

Required:

```text
CurrentOperation
=
WitnessOperation
```

or current operation MUST be proven to be contained within the witness's explicitly authorized operation envelope.

---

# 13. Operation Non-Equivalence

```text
READ != WRITE

WRITE != DELETE

CREATE != SHARE

EXECUTE != COMMIT

COMMIT != RELEASE

ACCESS != DISCLOSE

PROPOSE != EXECUTE
```

A witness for one MUST NOT silently authorize another.

---

# 14. Capability Binding

Where a capability is material, the witness SHOULD bind:

```text
capability_id

capability_version

resolved_capability_contract_hash
```

Example:

```yaml
capability:
  capability_id: "CAP_EXTERNAL_SEND"
  capability_version: "2.1.0"
  resolved_capability_contract_hash: "sha256:<digest>"
```

This ensures that authority was evaluated against the capability contract actually intended for use.

---

# 15. Resolved Capability Contract Binding

For effectful capabilities, the witness SHOULD bind the resolved capability contract rather than only a human-readable capability name.

```text
CAPABILITY NAME
!=
RESOLVED CAPABILITY CONTRACT
```

If the resolved capability contract changes materially after witness issuance:

```text
REVALIDATE
```

is required where that change can affect authority requirements.

---

# 16. Target Binding

Where a target/resource matters:

```yaml
target:
  target_id: string
  target_class: string
  target_digest: null
```

The witness SHOULD bind the narrowest stable target identity sufficient for the operation.

---

# 17. Target Substitution

A witness authorizing:

```text
UPDATE RESOURCE_A
```

MUST NOT silently authorize:

```text
UPDATE RESOURCE_B
```

even when both resources have the same type.

---

# 18. Target Digest

For consequential mutations, a target digest MAY be used to bind authority to a particular resource state.

If the resource state changes and the authority decision depended upon that state:

```text
REVALIDATE
```

rather than blindly reusing the witness.

---

# 19. Effect Binding

For durable, external, irreversible, or model-promotion operations, the witness SHOULD bind the proposed effect.

```yaml
effect:
  effect_class: "DURABLE"
  effect_digest: "sha256:<effect>"
```

This prevents authority for one effect from being replayed for a materially different effect.

---

# 20. Effect Digest Invariant

Where effect binding is required:

```text
Witness.effect_digest
=
CurrentEffect.effect_digest
```

must hold.

Otherwise:

```text
BLOCK_AUTHORITY
```

or:

```text
REVALIDATE
```

depending on whether a new authority resolution can validly cover the changed effect.

---

# 21. Idempotency Binding

For durable/external/model-promotion effects, authority SHOULD bind the stable idempotency key where infrastructure finality depends upon it.

```yaml
effect:
  effect_digest: "sha256:<effect>"
  idempotency_key: "stable-key"
```

Required:

```text
Witness.idempotency_key
=
CurrentEffect.idempotency_key
```

where idempotency binding is part of authority.

---

# 22. Idempotency Boundary

The witness MUST NOT be used to authorize:

```text
same authority
+
different idempotency key
```

when the authority resolution was explicitly bound to the original key.

Nor may the same idempotency key be silently reused for a different effect digest.

---

# 23. Transaction Binding

Where the action belongs to a semantic transaction:

```yaml
transaction:
  transaction_id: string
  semantic_transaction_hash: string
```

The witness SHOULD bind both.

Canonical rule:

```text
TransactionBoundWitness(T1)
↛
Transaction(T2)
```

---

# 24. Semantic Transaction Binding

A transaction ID alone may be insufficient if transaction semantics are mutable.

Therefore consequential authority SHOULD bind:

```text
transaction_id
+
semantic_transaction_hash
```

when available.

If the semantic transaction changes materially:

```text
REVALIDATE
```

---

# 25. Scope

The witness MUST preserve the effective authority scope used by the resolver.

```yaml
scope:
  operations: []
  capabilities: []
  resources: []
  resource_classes: []
  effects: []
  recipients: []
  environments: []
  jurisdictions: []
  transactions: []
  hml:
    H: null
    M: null
    L: null
```

Unknown dimensions MUST remain unknown.

---

# 26. Scope Containment

For witness reuse:

```text
CurrentRequestedScope
⊆
WitnessEffectiveScope
```

must hold.

If not:

```text
INVALID
```

or:

```text
REVALIDATE
```

depending on whether broader valid authority may exist.

---

# 27. Unknown Scope

```text
UNKNOWN_SCOPE
!=
GLOBAL_SCOPE
```

A missing scope field cannot be interpreted as wildcard authority unless the governing schema explicitly defines that field as unrestricted.

---

# 28. Regime Binding

Authority validity may depend upon regime.

Examples:

```text
NORMAL_OPERATION

INCIDENT_RESPONSE

RECOVERY

MAINTENANCE

SANDBOX

TEST

PRODUCTION

EMERGENCY
```

The witness SHOULD preserve the regime under which authority was resolved.

---

# 29. Regime Shift

If:

```text
Witness.regime != Current.regime
```

and authority validity depends on regime:

```text
REVALIDATE
```

The prior witness does not silently cross regimes.

---

# 30. Environment Binding

Authority may differ across:

```text
DEVELOPMENT

TEST

STAGING

PRODUCTION
```

Therefore:

```text
Witness(TEST)
↛
PRODUCTION
```

unless explicit authority covers both.

---

# 31. Recipient Binding

For disclosure, transfer, messaging, sharing, or external effects, the witness SHOULD bind permitted recipient identity or recipient scope.

```yaml
scope:
  recipients:
    - "RECIPIENT_A"
```

Authority to disclose to `A` does not imply authority to disclose to `B`.

---

# 32. Constraint Binding

Applicable authority constraints MUST remain visible in the witness.

```yaml
constraints:
  - constraint_id: string
    type: string
    operator: string
    value: any
    provenance_ref: string
```

The witness does not erase constraints after authority resolution.

---

# 33. Constraint Preservation

Downstream components MUST NOT reinterpret:

```text
AUTHORIZED_WITH_CONSTRAINTS
```

as:

```text
UNCONDITIONALLY_AUTHORIZED
```

A valid witness remains conditional on its load-bearing constraints.

---

# 34. Delegation Lineage

Where authority is delegated, the witness SHOULD preserve sufficient lineage to reconstruct the authority chain.

```yaml
delegation:
  root_authority_ref: "AUTH_ROOT"
  lineage_refs:
    - "AUTH_ROOT"
    - "DELEGATION_1"
    - "DELEGATION_2"
```

---

# 35. Delegation Invariant

```text
DelegatedAuthority
<=
DelegatingAuthority
```

A witness MUST NOT conceal delegation expansion.

---

# 36. Delegation Dependency

If:

```text
AUTH_ROOT
    ↓
DELEGATION_A
    ↓
DELEGATION_B
    ↓
WITNESS
```

then the witness depends on all load-bearing authority links.

Revocation or invalidation of a required ancestor requires witness revalidation or invalidation.

---

# 37. Authority Read Set

The witness SHOULD preserve the exact authoritative authority objects used to form the resolution.

```yaml
authority_read_set:
  - object_id: string
    version: string
    content_hash: string
```

Conceptually:

```text
AuthorityReadSet =
{
  (object_id, version, content_hash)
}
```

---

# 38. Fine-Grained Freshness

A change to an authority object not in the witness's dependency closure SHOULD NOT automatically invalidate the witness.

A change to a load-bearing read-set object MUST trigger revalidation.

Example:

```text
W1 ← A1 + A2

W2 ← A3
```

If `A2` changes:

```text
W1 → REVALIDATE
W2 → PRESERVE
```

assuming no hidden dependency exists.

---

# 39. Authority Registry Identity

A scalar registry version is insufficient where authoritative state can change without a version bump.

The witness SHOULD preserve:

```yaml
authority_registry:
  registry_id: string
  registry_generation: string
  registry_version: string
  registry_hash: string
```

Canonical identity:

```text
AuthorityRegistryIdentity =
registry_id
+
registry_generation
+
registry_version
+
registry_hash
```

---

# 40. Registry Freshness

At revalidation:

```text
PreparedRegistryIdentity
=
CurrentRegistryIdentity
```

may permit the registry-dependent portion of the witness to remain fresh.

If relevant identity differs:

```text
REVALIDATE
```

unless fine-grained authoritative read-set comparison establishes that no load-bearing authority dependency changed.

---

# 41. Registry Rollback

Unexpected rollback or generation regression MUST NOT silently restore old authority.

Potential outcomes:

```text
REVALIDATE

CONFLICT

QUARANTINED

UNKNOWN_GAP
```

depending on available evidence.

---

# 42. Effect Release State Binding

For durable/external/model-promotion effects, the witness MAY be required to bind the infrastructure-owned release-ledger identity.

```yaml
effect_release_state:
  ledger_id: string
  ledger_generation: string
  ledger_version: string
  ledger_hash: string
```

Canonical identity:

```text
EffectLedgerIdentity =
ledger_id
+
ledger_generation
+
ledger_version
+
ledger_hash
```

---

# 43. Why Ledger Binding Matters

A valid authority decision does not prove that releasing the effect remains safe.

The release ledger may reveal:

```text
effect already committed;

dispatch currently in progress;

externalized outcome unknown;

idempotency conflict;

lineage conflict;

ledger corruption;

or changed release state.
```

Therefore authority for durable effects may depend on the exact observed release-ledger state.

---

# 44. Ledger Freshness

If authority was explicitly bound to release state:

```text
PreparedLedgerIdentity
!=
CurrentLedgerIdentity
```

requires:

```text
REVALIDATE_EFFECT_LEDGER
```

before effect release.

The Authority Witness MUST NOT override infrastructure-owned finality state.

---

# 45. Authority/Ledger Separation

```text
VALID AUTHORITY
!=
SAFE TO RELEASE AGAIN
```

and:

```text
VALID WITNESS
!=
NO PRIOR EFFECT
```

Deduplication and external-effect finality remain infrastructure responsibilities.

---

# 46. Observability Binding

For consequential capabilities, authority MAY depend upon an infrastructure-owned observability envelope.

```yaml
observability:
  envelope_id: string
  envelope_hash: string
```

This permits authority to express:

> This operation is authorized only under this observability boundary.

---

# 47. Observability Invariant

If required observability weakens materially after witness issuance:

```text
REVALIDATE_OBSERVABILITY
```

or:

```text
BLOCK_AUTHORITY
```

may be required.

Authority MUST NOT silently survive removal of a load-bearing audit/observability condition.

---

# 48. Capability-to-Observability Composition

A capability may declare required observability.

The infrastructure determines whether the actual observability envelope satisfies those requirements.

Therefore:

```text
CAPABILITY DECLARES REQUIREMENT
!=
REQUIREMENT SATISFIED
```

The witness SHOULD bind both:

```text
resolved_capability_contract_hash

observability_envelope_hash
```

where observability is load-bearing.

---

# 49. Temporal Envelope

```yaml
temporal:
  issued_at: timestamp
  valid_from: timestamp
  valid_until: null
  revalidate_after: null
```

The witness MUST preserve relevant temporal validity.

---

# 50. Witness Expiry

If:

```text
CurrentTime >= valid_until
```

then:

```text
EXPIRED
```

where `valid_until` exists.

Expiry MUST NOT silently become authorization.

---

# 51. Revalidation Deadline

A witness MAY have:

```text
revalidate_after
```

even when the underlying authority itself has not expired.

This permits freshness-sensitive authority to require periodic rechecking.

---

# 52. Authority Expiry vs Witness Expiry

These are distinct.

```text
AUTHORITY EXPIRY
```

means the authority itself no longer applies.

```text
WITNESS EXPIRY
```

means the witness may no longer be safely relied upon without refreshing authority evidence.

A witness may expire before the underlying authority.

It may never extend underlying authority beyond its own valid envelope.

---

# 53. Trusted Time

For consequential authority checks, infrastructure SHOULD provide the evaluation time.

A witness issuer's self-asserted timestamp MUST NOT be treated as sufficient trusted time where revocation or temporal key validity matters.

---

# 54. Signature

A witness MAY carry a cryptographic signature.

```yaml
integrity:
  signer_id: string
  signature_algorithm: string
  signature: string
```

The signature SHOULD bind the canonical witness digest.

---

# 55. Signature Boundary

```text
SIGNATURE_PRESENT
!=
SIGNATURE_VALID
```

and:

```text
SIGNATURE_VALID
!=
CURRENT_AUTHORITY
```

A cryptographically authentic witness can still be:

```text
expired;

revoked;

stale;

out of scope;

superseded;

bound to the wrong transaction;

or invalid in the current regime.
```

---

# 56. Signer Authority

A valid signature proves only what the applicable cryptographic trust model establishes.

It does not by itself prove the signer was authorized to issue an AMOS authority witness.

Signer trust and issuer authority must be governed separately.

---

# 57. Trust Registry

Where witness verification relies on cryptographic signer trust, the infrastructure MAY maintain a trust registry.

The witness SHOULD preserve enough information to identify the trust state used for validation.

A stale trust registry SHOULD NOT be treated as current proof where key rotation or revocation is material.

---

# 58. Revocation

The underlying authority may be revoked after witness issuance.

Therefore:

```text
WITNESS ISSUED AT T0
+
AUTHORITY REVOKED AT T1
+
ACTION AT T2
```

with:

```text
T0 < T1 < T2
```

must not produce current authorization.

---

# 59. Commit-Time Revalidation

For durable, external, irreversible, or model-promotion effects:

```text
WITNESS VALIDATED
      ↓
ACTION PREPARED
      ↓
CURRENT AUTHORITY STATE READ
      ↓
CURRENT POLICY STATE READ
      ↓
CURRENT CONSTRAINT STATE READ
      ↓
CURRENT EFFECT-LEDGER STATE READ
      ↓
COMMIT-TIME VALIDATION
      ↓
COMMITTABLE OR BLOCK
```

---

# 60. Plan-Time/Commit-Time Law

```text
VALID_WITNESS_AT_PLAN
!=
VALID_AUTHORITY_AT_COMMIT
```

when authority state can change.

---

# 61. Commit-Time Witness Validation

Conceptually:

```text
ValidateWitnessAtCommit(W, C) =
    IntegrityValid(W)
∧   PrincipalMatch(W,C)
∧   OperationMatch(W,C)
∧   CapabilityMatch(W,C)
∧   TargetMatch(W,C)
∧   EffectMatch(W,C)
∧   TransactionMatch(W,C)
∧   ScopeCompatible(W,C)
∧   RegimeCompatible(W,C)
∧   TemporalValid(W,C)
∧   AuthorityDependenciesFresh(W,C)
∧   AuthorityNotRevoked(W,C)
∧   ConstraintsCurrent(W,C)
∧   RequiredObservabilityCurrent(W,C)
∧   RequiredLedgerStateCurrent(W,C)
```

AMOS MODEL expression.

---

# 62. Commit-Time Result

```yaml
authority_witness_validation:
  witness_id: string

  state:
    - VALID_CURRENT
    - VALID_CONDITIONAL
    - REVALIDATE_AUTHORITY
    - REVALIDATE_STALE_READ
    - REVALIDATE_CONSTRAINTS
    - REVALIDATE_OBSERVABILITY
    - REVALIDATE_EFFECT_LEDGER
    - BLOCK_AUTHORITY
    - BLOCK_CONFLICT
    - INVALID
    - EXPIRED
    - REVOKED
    - UNKNOWN_GAP

  changed_dependencies: []

  failed_invariants: []

  reason_codes: []

  evaluated_at: timestamp
```

---

# 63. Durable Effect Requirements

For durable/external/model-promotion effects, a sufficient witness SHOULD bind where applicable:

```text
authority_id

authority_version

authority_digest

principal

operation

capability contract hash

target

effect_digest

idempotency_key

transaction_id

semantic transaction hash

authority registry identity

authority read set

effect-ledger identity

observability envelope hash

temporal validity

constraints
```

Missing load-bearing fields MUST remain visible as gaps.

---

# 64. Receiver Receipt Separation

The Authority Witness is upstream of effect completion.

A receiver receipt is downstream evidence.

```text
AUTHORITY WITNESS
```

answers:

> Was authority established for the proposed effect?

A:

```text
RECEIVER RECEIPT
```

answers:

> What does the receiver/service attest it observed after dispatch?

Therefore:

```text
AUTHORITY_WITNESS != RECEIVER_RECEIPT
```

---

# 65. Receipt Non-Substitution

A valid receipt does not retroactively create authority.

```text
UNAUTHORIZED ACTION
+
VALID RECEIVER RECEIPT
!=
AUTHORIZED ACTION
```

Likewise, valid authority does not prove completion.

```text
VALID AUTHORITY
+
NO RECEIVER EVIDENCE
!=
PROVEN COMPLETION
```

---

# 66. Receiver-Attested Finality

For external effects where AMOS requires receiver-attested completion, a non-empty receipt ID is insufficient.

The receiver/service-attested receipt SHOULD cryptographically bind:

```text
service identity

effect_digest

idempotency_key

transaction_id

authority_id

principal

operation
```

The Authority Witness provides the authority-side values against which the receipt can later be compared.

---

# 67. Receipt Lineage Check

Conceptually:

```text
Receipt.authority_id
=
Witness.authority_id

Receipt.principal
=
Witness.principal

Receipt.operation
=
Witness.operation

Receipt.effect_digest
=
Witness.effect_digest

Receipt.idempotency_key
=
Witness.idempotency_key

Receipt.transaction_id
=
Witness.transaction_id
```

where those fields are required.

Mismatch means the receipt does not prove completion of the exact witnessed effect.

---

# 68. Temporal Trust for Receipts

A valid receiver signature is not sufficient to establish current receiver signing authority after:

```text
key rotation;

revocation;

trust-registry staleness;

or temporal-policy failure.
```

Receipt validation belongs to the receiver-trust/finality layer, not the Authority Witness itself.

The witness MUST NOT pretend to solve that downstream trust problem.

---

# 69. Historical Witnesses

Historical witnesses MAY remain useful for:

```text
audit;

replay analysis;

incident reconstruction;

authority lineage;

post-event review.
```

A historical witness marked expired or revoked may still be valid historical evidence.

It does not regain current action authority.

---

# 70. Witness States

## VALID

The witness is internally valid and its known applicability conditions currently hold.

## VALID_CONDITIONAL

The witness may be relied upon only if explicit conditions are discharged.

## REVALIDATE

One or more mutable dependencies require fresh evaluation.

## INVALID

Structural or semantic validation failed.

## EXPIRED

The witness's validity envelope has elapsed.

## REVOKED

Its load-bearing authority has been authoritatively revoked.

## CONFLICT

Material authority evidence conflicts.

## SUPERSEDED

A newer witness or authority resolution has replaced it for the relevant scope.

## QUARANTINED

The witness is isolated because integrity, provenance, or trust is suspect.

## UNKNOWN_GAP

Available evidence cannot establish safe witness validity.

---

# 71. State Transition Model

```text
ISSUED
  ↓
VALID
  ├──→ VALID_CONDITIONAL
  ├──→ REVALIDATE
  ├──→ EXPIRED
  ├──→ REVOKED
  ├──→ CONFLICT
  ├──→ SUPERSEDED
  ├──→ QUARANTINED
  └──→ INVALID
```

Revalidation may produce:

```text
REVALIDATE
   ↓
VALID

REVALIDATE
   ↓
VALID_CONDITIONAL

REVALIDATE
   ↓
EXPIRED

REVALIDATE
   ↓
REVOKED

REVALIDATE
   ↓
CONFLICT

REVALIDATE
   ↓
INVALID

REVALIDATE
   ↓
UNKNOWN_GAP
```

---

# 72. State Transition Boundary

No transition to `VALID` is allowed merely because:

```text
no error was observed;

the prior action succeeded;

the witness exists;

the signer is familiar;

the agent is confident;

or the same witness worked previously.
```

---

# 73. Witness Creation Workflow

```text
01 RECEIVE AUTHORITY RESOLUTION

02 VERIFY RESOLUTION STATE

03 NORMALIZE PRINCIPAL

04 NORMALIZE OPERATION

05 BIND CAPABILITY

06 BIND TARGET

07 BIND EFFECT

08 BIND IDEMPOTENCY KEY WHERE REQUIRED

09 BIND TRANSACTION

10 BIND SCOPE

11 BIND REGIME

12 BIND AUTHORITY CONSTRAINTS

13 BIND DELEGATION LINEAGE

14 CAPTURE AUTHORITY READ SET

15 CAPTURE AUTHORITY REGISTRY IDENTITY

16 CAPTURE EFFECT-LEDGER IDENTITY WHERE REQUIRED

17 CAPTURE OBSERVABILITY ENVELOPE WHERE REQUIRED

18 CAPTURE RESOLVED CAPABILITY CONTRACT HASH

19 SET TEMPORAL ENVELOPE

20 BUILD PROVENANCE

21 COMPUTE WITNESS DIGEST

22 SIGN WHERE GOVERNED

23 VALIDATE GENERATED WITNESS

24 ISSUE WITNESS
```

---

# 74. Witness Consumption Workflow

```text
01 RECEIVE WITNESS

02 PARSE SCHEMA

03 VALIDATE WITNESS IDENTITY

04 VALIDATE DIGEST

05 VALIDATE SIGNATURE WHERE REQUIRED

06 VALIDATE SIGNER TRUST WHERE REQUIRED

07 MATCH PRINCIPAL

08 MATCH OPERATION

09 MATCH CAPABILITY

10 MATCH TARGET

11 MATCH EFFECT

12 MATCH IDEMPOTENCY KEY

13 MATCH TRANSACTION

14 CHECK SCOPE

15 CHECK REGIME

16 CHECK TEMPORAL VALIDITY

17 CHECK AUTHORITY READ-SET FRESHNESS

18 CHECK AUTHORITY REGISTRY FRESHNESS

19 CHECK REVOCATION

20 CHECK CONSTRAINTS

21 CHECK OBSERVABILITY BINDING

22 CHECK EFFECT-LEDGER BINDING

23 CHECK SUPERSESSION

24 DETECT CONFLICT

25 RETURN VALIDATION STATE
```

---

# 75. Commit Workflow

```text
TASK
 ↓
CAPABILITY RESOLUTION
 ↓
AUTHORITY RESOLUTION
 ↓
AUTHORITY WITNESS
 ↓
POLICY DECISION
 ↓
DOMAIN EVIDENCE
 ↓
OBSERVED READ SET
 ↓
SEMANTIC TRANSACTION
 ↓
OBSERVABILITY ENVELOPE
 ↓
EFFECT INTENT
 ↓
PREPARE
 ↓
CURRENT AUTHORITY REVALIDATION
 ↓
CURRENT CONSTRAINT REVALIDATION
 ↓
CURRENT LEDGER REVALIDATION
 ↓
COMMIT GUARD
 ↓
COMMITTABLE
 ↓
EFFECT RELEASE
```

---

# 76. Fast Path

Witness reuse MAY use a fast path only when all decision-relevant dependencies remain demonstrably fresh.

Required conditions SHOULD include:

```text
witness digest unchanged;

principal unchanged;

operation unchanged;

capability contract unchanged;

target unchanged;

effect unchanged;

transaction unchanged;

scope unchanged;

regime compatible;

authority read set fresh;

authority registry compatible;

authority not revoked;

constraints fresh;

required ledger identity current;

required observability current;

no material conflict.
```

---

# 77. Fast-Path Law

```text
FAST_PATH
=
PROVEN_DEPENDENCY_STABILITY
```

not:

```text
FAST_PATH
=
SKIP_VALIDATION
```

---

# 78. Witness Cache

A witness MAY be cached with:

```yaml
witness_cache_entry:
  witness_id: string
  witness_version: string
  witness_digest: string

  principal_id: string

  operation_id: string

  capability_contract_hash: null

  target_digest: null

  effect_digest: null

  transaction_id: null

  authority_read_set: []

  authority_registry_identity: {}

  effect_ledger_identity: {}

  valid_until: null
  revalidate_after: null

  cached_at: timestamp
```

---

# 79. Cache Invalidation

A cached witness MUST be invalidated or revalidated on relevant:

```text
authority revocation;

authority expiry;

authority object mutation;

authority-registry generation change;

authority-registry hash change;

delegation mutation;

scope change;

principal change;

operation change;

capability contract change;

target change;

effect change;

transaction change;

regime change;

constraint change;

observability change;

release-ledger change.
```

---

# 80. Witness Replay

Witness replay occurs when a previously valid witness is reused outside its authorized binding.

Examples:

```text
same witness → different principal;

same witness → different operation;

same witness → different resource;

same witness → different effect;

same witness → different recipient;

same witness → different transaction;

same witness → different idempotency key;

same witness → different environment.
```

Replay MUST fail closed where the changed dimension is authority-relevant.

---

# 81. Witness Confusion Attack

An implementation MUST resist replacing:

```text
AUTHORITY_WITNESS
```

with:

```text
POLICY_DECISION

CAPABILITY_CONTRACT

RECEIPT

LOG ENTRY

MEMORY RECORD

AGENT ASSERTION
```

even when these objects contain similar fields.

Typed object identity is required.

---

# 82. Witness Forgery

Potential forgery indicators include:

```text
digest mismatch;

invalid signature;

unknown signer;

signer outside trust regime;

authority ID mismatch;

resolution ID missing;

principal mismatch;

tampered scope;

tampered effect digest;

tampered transaction;

fabricated registry identity;

fabricated delegation lineage.
```

Suspected forgery SHOULD produce:

```text
QUARANTINED
```

or:

```text
INVALID
```

and block consequential effect release.

---

# 83. Witness Equivocation

Equivocation occurs when supposedly identical witness identity maps to materially different content.

Example:

```text
witness_id = W1
version = 4
```

appears with two incompatible digests.

Result:

```text
CONFLICT
```

or:

```text
QUARANTINED
```

until resolved.

---

# 84. Supersession

A witness MAY be superseded by a later valid resolution.

Supersession MUST preserve lineage:

```yaml
supersession:
  supersedes_witness_id: "W1"
  superseded_by_witness_id: "W2"
  reason: string
  effective_at: timestamp
```

---

# 85. Supersession Boundary

```text
NEWER
!=
SUPERSEDING
```

A later timestamp alone does not prove a witness invalidates an earlier one.

Supersession requires governed lineage or changed authority state.

---

# 86. Witness Provenance

Minimum provenance SHOULD include:

```text
authority source;

authority resolver;

authority resolution ID;

authority object identity;

delegation lineage;

authority registry snapshot;

decision-forming read set;

transaction binding;

effect binding;

generation process;

witness signer where applicable.
```

---

# 87. Provenance Topology

Suppose:

```text
AUTHORITY_ROOT
     ↓
AUTHORITY_RESOLUTION
     ↓
WITNESS_A
     ├── COPY_1
     ├── COPY_2
     └── SUMMARY
```

Then:

```text
IndependentAuthorityRoots = 1
```

not `3`.

Copies of a witness do not provide independent authority evidence.

---

# 88. Sybil Hardening

```text
MULTIPLE_WITNESS_FILES
!=
MULTIPLE_INDEPENDENT_AUTHORITY_PATHS
```

Authority independence must be determined from ancestry.

---

# 89. Evidence Classes

Witness-related evidence SHOULD preserve type.

```text
SOURCE_CLAIM

OBSERVATION

DERIVED

MODEL

DECISION

UNKNOWN/GAP
```

Example:

```text
"The authority registry reports A active"
→ OBSERVATION

"The current request is within A's scope"
→ DERIVED

"Action is authorized"
→ DECISION
```

Do not flatten these into one undifferentiated truth value.

---

# 90. H/M/L Applicability

## H — Governing/System Level

At H scale, the witness may bind:

```text
principal authority;

organization;

governance regime;

jurisdiction;

global policy context;

authority registry;

control-plane state.
```

## M — Subsystem/Workflow Level

At M scale:

```text
capability;

workflow;

resource class;

transaction;

delegation;

constraint context;

observability envelope.
```

## L — Local Effect Level

At L scale:

```text
exact operation;

exact target;

exact effect digest;

exact recipient;

exact idempotency key;

exact ledger identity;

exact commit attempt.
```

---

# 91. H/M/L Law

Higher-level authority does not automatically imply unrestricted lower-level authority.

Likewise, local authority does not imply system-wide authority.

```text
H_AUTHORITY
↛
ALL_L_ACTIONS

L_AUTHORITY
↛
H_GOVERNANCE_AUTHORITY
```

Cross-scale authority requires explicit mapping.

---

# 92. Control-Plane Requirements

The infrastructure control plane SHOULD own or independently validate:

```text
witness schema;

witness identity;

authority read set;

authority registry identity;

commit-time freshness;

effect-ledger identity;

observability envelope;

transaction binding;

effect binding;

idempotency binding;

witness validation result.
```

Domain components MUST NOT override these values after validation.

---

# 93. Domain Skill Boundary

Domain Skills MAY provide:

```text
domain evidence;

domain validators;

domain-specific constraints;

effect-specific semantics;

compensation semantics.
```

They MUST NOT self-assert:

```text
"authority is valid because my domain logic says so"
```

unless the infrastructure authority contract explicitly delegates that authority-resolution function.

---

# 94. Agent Roles

Functional roles MAY include:

```text
AUTHORITY_WITNESS_BUILDER

AUTHORITY_WITNESS_VALIDATOR

AUTHORITY_FRESHNESS_MONITOR

DELEGATION_LINEAGE_AUDITOR

AUTHORITY_PROVENANCE_AUDITOR

WITNESS_CONFLICT_AUDITOR

COMMIT_AUTHORITY_REVALIDATOR

AUTHORITY_RECOVERY_AGENT
```

These are functional roles only.

```text
ROLE_NAME != AUTHORITY
```

---

# 95. Skill Interfaces

Relevant AMOS Skills MAY include:

```text
infrastructure control plane;

commit-time authorization;

portable agent authorization;

principal trust governance;

constraint propagation;

provenance/Sybil hardening;

semantic workflow persistence;

information boundary governance;

execution provenance/replay;

repair/recovery.
```

Skill availability does not itself authorize an effect.

---

# 96. Protocol — Issue Witness

```yaml
issue_authority_witness:
  authority_resolution: {}

  current_context:
    principal: {}
    operation: {}
    capability: {}
    target: {}
    effect: {}
    transaction: {}
    regime: {}

  authoritative_state:
    authority_read_set: []
    authority_registry: {}
    effect_release_state: {}
    observability_envelope: {}

  issued_at: timestamp
```

Response:

```yaml
issue_authority_witness_result:
  state:
    - ISSUED
    - REVALIDATE
    - BLOCK_AUTHORITY
    - BLOCK_CONFLICT
    - UNKNOWN_GAP

  witness: null

  gaps: []
```

---

# 97. Protocol — Validate Witness

```yaml
validate_authority_witness:
  witness: {}

  current_request:
    principal: {}
    operation: {}
    capability: {}
    target: {}
    effect: {}
    transaction: {}
    scope: {}
    regime: {}

  current_time: timestamp
```

---

# 98. Protocol — Revalidate Witness

```yaml
revalidate_authority_witness:
  witness_id: string
  witness_version: string
  witness_digest: string

  current_authority_state: {}

  current_constraint_state: {}

  current_registry_state: {}

  current_effect_ledger_state: {}

  current_observability_state: {}

  current_time: timestamp
```

---

# 99. Protocol — Invalidate Witness

```yaml
invalidate_authority_witness:
  witness_id: string

  reason_code: string

  invalidating_dependency_ref: null

  evidence_refs: []

  effective_at: timestamp
```

---

# 100. Protocol — Quarantine Witness

```yaml
quarantine_authority_witness:
  witness_id: string

  reason:
    - INTEGRITY_FAILURE
    - SIGNATURE_FAILURE
    - PROVENANCE_FAILURE
    - EQUIVOCATION
    - REGISTRY_CONFLICT
    - DELEGATION_CONFLICT
    - UNKNOWN_TRUST_ROOT

  evidence_refs: []

  quarantined_at: timestamp
```

---

# 101. Protocol — Supersede Witness

```yaml
supersede_authority_witness:
  old_witness_id: string

  new_witness_id: string

  reason: string

  authority_resolution_ref: string

  effective_at: timestamp
```

---

# 102. Protocol — Commit-Time Validation

```yaml
commit_time_authority_witness_check:
  witness: {}

  principal: string

  operation: string

  capability_contract_hash: string

  target_digest: null

  effect_digest: string

  idempotency_key: string

  transaction_id: string

  semantic_transaction_hash: string

  current_authority_registry: {}

  current_authority_read_set: []

  current_constraint_context: {}

  current_observability_envelope: {}

  current_effect_release_state: {}

  verification_time: timestamp
```

---

# 103. Commit-Time Output

```yaml
commit_time_authority_witness_result:
  state:
    - VALID_CURRENT
    - REVALIDATE_AUTHORITY
    - REVALIDATE_STALE_READ
    - REVALIDATE_CONSTRAINTS
    - REVALIDATE_OBSERVABILITY
    - REVALIDATE_EFFECT_LEDGER
    - BLOCK_AUTHORITY
    - BLOCK_CONFLICT
    - UNKNOWN_GAP

  witness_id: string

  changed_dependencies: []

  failed_invariants: []

  reason_codes: []

  current_authority_resolution_ref: null
```

---

# 104. Control-Plane Result Mapping

Authority Witness failures SHOULD map conservatively.

```text
invalid authority
→ BLOCK_AUTHORITY

revoked authority
→ BLOCK_AUTHORITY

expired authority
→ BLOCK_AUTHORITY

authority conflict
→ BLOCK_CONFLICT

stale authority read
→ REVALIDATE_STALE_READ

constraint mutation
→ REVALIDATE_CONSTRAINTS

observability mutation
→ REVALIDATE_OBSERVABILITY

release-ledger mutation
→ REVALIDATE_EFFECT_LEDGER

insufficient evidence
→ UNKNOWN_GAP
```

---

# 105. Core Invariants

## INV-AW-001 — Witness/Authority Separation

```text
AUTHORITY_WITNESS != AUTHORITY
```

## INV-AW-002 — No Authority Creation

A witness MUST NOT create authority absent a valid authority source and resolution.

## INV-AW-003 — Principal Binding

Witness principal MUST match the acting principal.

## INV-AW-004 — Operation Binding

Witness operation MUST cover the current operation.

## INV-AW-005 — Capability Binding

Where material, the witness MUST cover the actual resolved capability.

## INV-AW-006 — Target Binding

Target-bound authority MUST match the actual target.

## INV-AW-007 — Effect Binding

Effect-bound authority MUST match the exact effect.

## INV-AW-008 — Transaction Binding

Transaction-bound authority MUST match the actual transaction.

## INV-AW-009 — Scope Containment

```text
RequestedScope ⊆ WitnessScope
```

## INV-AW-010 — Regime Validity

Witness reuse MUST remain inside its applicable regime.

---

# 106. Freshness Invariants

## INV-AW-011 — Temporal Validity

Expired witnesses MUST NOT authorize current actions.

## INV-AW-012 — Revocation

Revoked underlying authority invalidates current witness authority.

## INV-AW-013 — Read-Set Freshness

Changed load-bearing authority reads require revalidation.

## INV-AW-014 — Registry Freshness

Material authority-registry changes require revalidation.

## INV-AW-015 — Delegation Freshness

Changed load-bearing delegation state requires revalidation.

## INV-AW-016 — Constraint Freshness

Changed authority constraints require revalidation where relevant.

## INV-AW-017 — Capability Contract Freshness

Material resolved-capability-contract changes require revalidation.

## INV-AW-018 — Observability Freshness

Required observability changes require revalidation.

## INV-AW-019 — Ledger Freshness

Authority-bound release-ledger changes require revalidation.

## INV-AW-020 — Commit-Time Freshness

Mutable authority MUST be current at commit.

---

# 107. Integrity Invariants

## INV-AW-021 — Digest Integrity

Witness contents MUST correspond to the declared digest.

## INV-AW-022 — Signature Integrity

Required signatures MUST verify.

## INV-AW-023 — Signer Trust

Cryptographic validity alone does not establish signer authorization.

## INV-AW-024 — No Equivocation

Same witness identity MUST NOT map to incompatible content without conflict detection.

## INV-AW-025 — Provenance Preservation

Authority ancestry MUST remain reconstructable.

## INV-AW-026 — Sybil Resistance

Copies MUST NOT be counted as independent authority evidence.

## INV-AW-027 — Unknown Is Not Valid

```text
UNKNOWN/GAP != VALID
```

## INV-AW-028 — Conflict Is Not Valid

```text
CONFLICT != VALID
```

## INV-AW-029 — Historical Validity Is Not Current Validity

Past authorization does not establish present authorization.

## INV-AW-030 — Witness Is Not Commit

```text
VALID_WITNESS != COMMITTED_EFFECT
```

---

# 108. Durable-Effect Invariants

## INV-AW-031 — Idempotency Binding

Required idempotency key MUST match.

## INV-AW-032 — Effect Digest Binding

Required effect digest MUST match.

## INV-AW-033 — Semantic Transaction Binding

Required semantic transaction hash MUST match.

## INV-AW-034 — Ledger Identity Binding

Required ledger identity MUST remain current.

## INV-AW-035 — No Blind Redispatch

A valid witness MUST NOT override an existing committed or ambiguous external effect state.

## INV-AW-036 — Receipt Separation

Authority witness MUST NOT be interpreted as receiver completion evidence.

## INV-AW-037 — Authority Lineage Binding

Downstream effect evidence SHOULD remain attributable to the authority identity used.

## INV-AW-038 — Observability Binding

Authority-dependent observability requirements MUST remain satisfied.

## INV-AW-039 — Infrastructure Ownership

Domain Skills MUST NOT override infrastructure-owned authority/finality state.

## INV-AW-040 — Proposal/Commit Separation

```text
PROPOSAL != COMMIT
```

---

# 109. Failure Modes

```text
FM-AW-001 witness missing

FM-AW-002 malformed witness

FM-AW-003 unknown schema version

FM-AW-004 witness digest mismatch

FM-AW-005 forged signature

FM-AW-006 untrusted signer

FM-AW-007 signer authority unknown

FM-AW-008 principal mismatch

FM-AW-009 operation mismatch

FM-AW-010 capability mismatch

FM-AW-011 capability contract hash mismatch

FM-AW-012 target mismatch

FM-AW-013 target state mismatch

FM-AW-014 effect digest mismatch

FM-AW-015 idempotency key mismatch

FM-AW-016 transaction mismatch

FM-AW-017 semantic transaction mismatch

FM-AW-018 scope expansion

FM-AW-019 regime mismatch

FM-AW-020 environment mismatch

FM-AW-021 recipient mismatch

FM-AW-022 expired witness

FM-AW-023 expired authority

FM-AW-024 revoked authority

FM-AW-025 stale authority registry

FM-AW-026 authority registry rollback

FM-AW-027 stale authority read set

FM-AW-028 delegation ancestor revoked

FM-AW-029 delegation lineage broken

FM-AW-030 authority constraint changed

FM-AW-031 authority budget changed

FM-AW-032 observability weakened

FM-AW-033 effect ledger changed

FM-AW-034 ledger generation mismatch

FM-AW-035 ledger hash mismatch

FM-AW-036 witness replay

FM-AW-037 witness substitution

FM-AW-038 witness equivocation

FM-AW-039 stale witness cache

FM-AW-040 superseded witness reused

FM-AW-041 copied witnesses counted independently

FM-AW-042 policy decision substituted for witness

FM-AW-043 capability contract substituted for witness

FM-AW-044 receipt substituted for witness

FM-AW-045 memory substituted for authority evidence

FM-AW-046 agent self-issued witness

FM-AW-047 domain Skill overrides infrastructure authority

FM-AW-048 plan-time witness reused after revocation

FM-AW-049 successful execution treated as authority proof

FM-AW-050 UNKNOWN/GAP treated as VALID
```

---

# 110. Repair / Recovery

Canonical recovery:

```text
DETECT WITNESS FAILURE
        ↓
BLOCK AFFECTED EFFECT
        ↓
PRESERVE WITNESS + REQUEST
        ↓
CLASSIFY FAILURE
        ↓
IDENTIFY FAILED DEPENDENCY
        ↓
INVALIDATE DEPENDENT CONCLUSION
        ↓
PRESERVE UNAFFECTED STATE
        ↓
REFRESH AUTHORITY SOURCE
        ↓
REFRESH AUTHORITY REGISTRY
        ↓
REFRESH REVOCATION STATE
        ↓
REFRESH DELEGATION
        ↓
REFRESH CONSTRAINTS
        ↓
REFRESH LEDGER WHERE REQUIRED
        ↓
RE-RUN AUTHORITY RESOLUTION
        ↓
ISSUE NEW WITNESS
        ↓
REVALIDATE DOWNSTREAM GATES
```

---

# 111. Selective Repair

If only one dependency changes:

```text
Witness
 ├── A1
 ├── A2
 ├── A3
 └── Ledger
```

and only `A2` changes:

```text
invalidate A2-dependent authority conclusion
```

rather than globally discarding unrelated system state.

---

# 112. No Failed-Path Repetition

If witness validation failed because:

```text
AUTHORITY REVOKED
```

re-running the same witness without changed evidence is not repair.

Repair requires changed state or a different valid authority path.

---

# 113. Recovery From Stale Registry

```text
STALE REGISTRY
    ↓
FETCH CURRENT AUTHORITATIVE STATE
    ↓
COMPARE LOAD-BEARING READ SET
    ↓
REVALIDATE AUTHORITY
    ↓
ISSUE / REFRESH WITNESS
```

Do not simply update the timestamp on the old witness.

---

# 114. Recovery From Effect Change

If the proposed effect changes:

```text
EFFECT_DIGEST_1
→
EFFECT_DIGEST_2
```

the prior effect-bound witness must not be patched in place.

Required:

```text
NEW EFFECT
    ↓
NEW AUTHORITY EVALUATION
    ↓
NEW WITNESS
```

where effect binding is authority-relevant.

---

# 115. Recovery From Transaction Change

Likewise:

```text
TRANSACTION_1
→
TRANSACTION_2
```

requires revalidation where authority is transaction-bound.

---

# 116. Recovery From Conflict

```text
CONFLICT
    ↓
IDENTIFY CONFLICT TYPE
    ↓
FIND CHEAPEST DISCRIMINATING EVIDENCE
    ↓
RESOLVE AUTHORITY SOURCE / VERSION / REVOCATION / SCOPE
    ↓
RE-RUN RESOLUTION
```

Do not treat additional descendants of the same authority source as independent confirmation.

---

# 117. Validators

Minimum validator surface:

```text
validate_witness_schema

validate_witness_identity

validate_witness_digest

validate_witness_signature

validate_witness_signer

validate_principal_binding

validate_operation_binding

validate_capability_binding

validate_capability_contract_hash

validate_target_binding

validate_effect_binding

validate_idempotency_binding

validate_transaction_binding

validate_semantic_transaction_binding

validate_scope

validate_regime

validate_environment

validate_recipient

validate_temporal_envelope

validate_authority_expiry

validate_authority_revocation

validate_delegation_lineage

validate_authority_read_set

validate_authority_registry_identity

validate_constraint_freshness

validate_observability_binding

validate_effect_ledger_identity

validate_supersession

validate_provenance

validate_commit_time_authority
```

---

# 118. Minimum Test Suite

```text
T-AW-001 valid witness schema

T-AW-002 malformed witness rejected

T-AW-003 witness digest verification

T-AW-004 witness digest tampering

T-AW-005 valid required signature

T-AW-006 forged signature

T-AW-007 untrusted signer

T-AW-008 principal match

T-AW-009 principal substitution

T-AW-010 operation match

T-AW-011 operation substitution

T-AW-012 capability match

T-AW-013 capability substitution

T-AW-014 capability contract hash change

T-AW-015 target match

T-AW-016 target substitution

T-AW-017 effect digest match

T-AW-018 effect substitution

T-AW-019 idempotency match

T-AW-020 idempotency substitution

T-AW-021 transaction match

T-AW-022 transaction substitution

T-AW-023 semantic transaction change

T-AW-024 scope containment

T-AW-025 scope expansion rejection

T-AW-026 regime match

T-AW-027 regime shift

T-AW-028 recipient match

T-AW-029 recipient substitution

T-AW-030 environment match

T-AW-031 environment substitution

T-AW-032 temporal validity

T-AW-033 witness expiry

T-AW-034 authority expiry

T-AW-035 authority revocation

T-AW-036 revocation after witness issuance

T-AW-037 delegation lineage

T-AW-038 revoked delegation ancestor

T-AW-039 authority read-set freshness

T-AW-040 unrelated read mutation

T-AW-041 registry identity unchanged

T-AW-042 registry generation change

T-AW-043 registry rollback

T-AW-044 constraint freshness

T-AW-045 authority budget mutation

T-AW-046 observability envelope match

T-AW-047 observability weakening

T-AW-048 effect ledger identity match

T-AW-049 effect ledger generation change

T-AW-050 effect ledger hash change

T-AW-051 witness replay rejection

T-AW-052 witness equivocation

T-AW-053 witness supersession

T-AW-054 stale cache rejection

T-AW-055 copied-witness Sybil test

T-AW-056 policy/witness separation

T-AW-057 capability/witness separation

T-AW-058 receipt/witness separation

T-AW-059 agent self-issued witness rejection

T-AW-060 domain authority override rejection

T-AW-061 plan-time validation

T-AW-062 commit-time revalidation

T-AW-063 authority change between plan and commit

T-AW-064 effect change between plan and commit

T-AW-065 transaction change between plan and commit

T-AW-066 ledger change between plan and commit

T-AW-067 observability change between plan and commit

T-AW-068 UNKNOWN/GAP fail-closed behavior

T-AW-069 selective invalidation

T-AW-070 audit reconstruction
```

---

# 119. Adversarial Tests

```text
valid witness copied to another principal;

READ witness used for DELETE;

resource-A witness used for resource-B;

test-environment witness used in production;

recipient-A disclosure witness used for recipient-B;

effect payload changed after witness issuance;

idempotency key changed after witness issuance;

transaction ID changed after witness issuance;

semantic transaction changed while ID stayed constant;

authority revoked one millisecond before commit;

authority registry rolled back to pre-revocation state;

witness has valid signature but expired authority;

witness has valid signature from untrusted signer;

same witness ID presented with two different digests;

three copies of one witness presented as three authority sources;

domain Skill generates its own authority witness;

agent asserts it may self-authorize because task is beneficial;

policy ALLOW object substituted for authority witness;

capability manifest substituted for authority witness;

receiver receipt substituted for authority witness;

successful previous execution used as authority proof;

effect ledger shows prior commit but witness remains valid;

effect ledger shows EXTERNALIZED_UNKNOWN and caller attempts blind retry;

observability envelope weakened after witness issuance;

missing scope interpreted as global scope;

missing registry hash accepted because version matches;

ledger version matches but generation/hash differs;

authority read object changes without version bump but hash differs.
```

---

# 120. Falsifiers

A claim that an Authority Witness remains valid is falsified by reliable evidence establishing any load-bearing condition such as:

```text
witness digest mismatch;

invalid required signature;

untrusted required signer;

principal mismatch;

operation mismatch;

capability mismatch;

target mismatch;

effect mismatch;

idempotency mismatch;

transaction mismatch;

scope violation;

regime violation;

authority expiry;

authority revocation;

invalid delegation;

changed load-bearing authority object;

authority-registry rollback;

constraint failure;

observability failure;

effect-ledger identity mismatch;

witness supersession;

or unresolved authority conflict.
```

---

# 121. Confidence Model

Conceptually:

```text
C_witness
≤
min(
    C_authority_resolution,
    C_witness_integrity,
    C_principal_binding,
    C_operation_binding,
    C_capability_binding,
    C_target_binding,
    C_effect_binding,
    C_transaction_binding,
    C_scope,
    C_temporal,
    C_revocation,
    C_provenance,
    C_freshness
)
```

AMOS MODEL equation.

A witness cannot be more trustworthy than its weakest load-bearing dependency.

---

# 122. Uncertainty Vector

```yaml
authority_witness_uncertainty:
  authority_resolution: null
  principal: null
  operation: null
  capability: null
  target: null
  effect: null
  transaction: null
  scope: null
  temporal: null
  revocation: null
  delegation: null
  provenance: null
  registry_freshness: null
  ledger_freshness: null
  observability: null
  execution: null
```

---

# 123. Confidence Ceiling

Until executable implementation and validation evidence exists for this specification:

```yaml
confidence_ceiling:
  architecture_internal_coherence: MODEL
  runtime_correctness: UNKNOWN_GAP
  production_security: UNKNOWN_GAP
  formal_verification: UNKNOWN_GAP
```

No architectural completeness claim may be converted into runtime validation.

---

# 124. RSCF Capsule

```yaml
rscf:
  claim:
    id: "AMOS_AUTHORITY_WITNESS_CONTRACT"
    class: MODEL

    text: >
      An AMOS Authority Witness is a provenance-bound,
      scope-bound, principal-bound, operation-bound and,
      where required, effect/transaction/state-bound
      representation of a resolved authority decision that
      must be revalidated when load-bearing authority or
      control-plane state changes.

  premises:
    - authority_resolution_exists
    - authority_resolution_valid_for_scope
    - witness_integrity_valid
    - principal_binding_valid
    - operation_binding_valid
    - capability_binding_valid_where_required
    - effect_binding_valid_where_required
    - transaction_binding_valid_where_required
    - authority_dependencies_fresh
    - authority_not_revoked
    - constraints_satisfied

  evidence:
    - "AMOS infrastructure/control-plane architecture"
    - "AUTHORITY_RESOLVER.md architecture"
    - "authority witness architecture defined in this artifact"

  provenance:
    origin_architect: "Trang Phan"
    steward: "Trang Phan"

  scope:
    system: "AMOS OS"
    component: "Authority Witness"

  regime:
    - DESIGN
    - ARCHITECTURE
    - GOVERNANCE_MODEL

  dependencies:
    - AUTHORITY_RESOLVER.md
    - POLICY_ENGINE.md
    - POLICY_DECISION.md
    - CAPABILITY_MANIFEST.md
    - CAPABILITY_CONTRACT.md
    - CONTROL_PLANE_MAP.md

  competing: []

  falsifiers:
    - witness creates authority
    - witness survives authority revocation
    - witness can be replayed for another principal
    - witness can be replayed for another effect
    - witness ignores transaction changes
    - witness ignores load-bearing registry changes
    - witness overrides effect-release finality

  confidence_ceiling: 0
```

---

# 125. GMEF Integration

Changes to any of the following SHOULD be treated as governed changes:

```text
witness identity;

binding semantics;

authority read-set semantics;

registry identity;

effect binding;

transaction binding;

idempotency binding;

commit-time freshness;

revocation handling;

ledger binding;

observability binding;

signature/trust semantics;

witness state transitions.
```

---

# 126. Change Manifest

```yaml
authority_witness_change:
  change_id: string

  from_version: string
  to_version: string

  change_class:
    - COSMETIC
    - SCHEMA
    - SEMANTIC
    - SECURITY
    - GOVERNANCE
    - AUTHORITY_BOUNDARY

  affected_fields: []

  affected_invariants: []

  affected_protocols: []

  affected_dependencies: []

  migration_requirements: []

  security_risks: []

  validators_required: []

  rollback_plan: null

  approval_state: PROPOSED
```

---

# 127. Promotion Model

```text
STRUCTURAL_MODEL
      ↓
SCHEMA_VALIDATED
      ↓
CANONICALIZATION_DEFINED
      ↓
DIGEST_VALIDATION_IMPLEMENTED
      ↓
AUTHORITY_RESOLVER_CONNECTED
      ↓
REGISTRY_FRESHNESS_IMPLEMENTED
      ↓
REVOCATION_IMPLEMENTED
      ↓
COMMIT-TIME VALIDATION_IMPLEMENTED
      ↓
LEDGER_BINDING_IMPLEMENTED
      ↓
OBSERVABILITY_BINDING_IMPLEMENTED
      ↓
UNIT_TESTED
      ↓
INTEGRATION_TESTED
      ↓
ADVERSARIALLY_TESTED
      ↓
SECURITY_REVIEWED
      ↓
GOVERNED_ACTIVE
```

No transition is automatic.

---

# 128. Implementation Requirements

An executable implementation SHOULD provide:

```text
typed witness schema;

deterministic canonicalization;

witness digest generation;

witness digest validation;

signature generation where required;

signature validation where required;

signer trust validation;

authority-resolution linkage;

principal binding validation;

operation binding validation;

capability-contract binding;

target binding;

effect digest binding;

idempotency binding;

transaction binding;

scope validation;

regime validation;

authority read-set capture;

authority read-set freshness;

authority-registry identity validation;

revocation checks;

delegation checks;

constraint freshness;

observability binding;

effect-ledger binding;

supersession tracking;

quarantine;

selective invalidation;

commit-time revalidation;

audit logging.
```

This document does not claim these components are currently implemented.

---

# 129. Example — Basic Witness

```yaml
authority_witness:
  schema: "AMOS.AUTHORITY_WITNESS"
  schema_version: "1.0"

  witness_id: "AW-0001"
  witness_version: "1"

  state: VALID

  authority:
    authority_id: "AUTH-100"
    authority_version: "4"
    authority_digest: "sha256:<authority>"

  principal:
    principal_id: "AGENT-A"
    principal_type: AGENT

  operation:
    operation_id: "OP-500"
    operation_class: UPDATE

  target:
    target_id: "RESOURCE-A"

  temporal:
    issued_at: "2026-08-26T10:00:00Z"
    valid_from: "2026-08-26T10:00:00Z"
    valid_until: "2026-08-26T10:05:00Z"

  commit_revalidation_required: true
```

Architectural example only.

---

# 130. Example — Durable External Effect

```yaml
authority_witness:
  witness_id: "AW-SEND-001"

  authority:
    authority_id: "AUTH-SEND-9"
    authority_version: "2"
    authority_digest: "sha256:<authority>"

  principal:
    principal_id: "AGENT-A"

  operation:
    operation_class: SEND

  capability:
    capability_id: "CAP-EXTERNAL-SEND"
    capability_version: "3.0"
    resolved_capability_contract_hash: "sha256:<contract>"

  effect:
    effect_class: EXTERNAL
    effect_digest: "sha256:<effect>"
    idempotency_key: "SEND::TX-100::001"

  transaction:
    transaction_id: "TX-100"
    semantic_transaction_hash: "sha256:<transaction>"

  authority_registry:
    registry_id: "AUTH-REG"
    registry_generation: "G12"
    registry_version: "V45"
    registry_hash: "sha256:<registry>"

  effect_release_state:
    ledger_id: "EFFECT-LEDGER"
    ledger_generation: "G7"
    ledger_version: "V991"
    ledger_hash: "sha256:<ledger>"

  observability:
    envelope_id: "OBS-44"
    envelope_hash: "sha256:<observability>"

  commit_revalidation_required: true
```

---

# 131. Example — Revocation Between Plan and Commit

At preparation:

```text
AUTHORITY = ACTIVE
WITNESS = VALID
```

Before commit:

```text
AUTHORITY = REVOKED
```

Result:

```text
WITNESS → REVOKED

COMMIT GUARD → BLOCK_AUTHORITY
```

The witness does not freeze authority in time.

---

# 132. Example — Unrelated Registry Change

Witness dependencies:

```text
W1 ← AUTH_A + AUTH_B
```

Registry changes:

```text
AUTH_Z changes
```

If `AUTH_Z` is outside the authoritative dependency closure:

```text
W1 may remain valid
```

subject to registry integrity and applicable freshness rules.

This prevents unnecessary global invalidation.

---

# 133. Example — Load-Bearing Read Change

```text
W1 ← AUTH_A + AUTH_B
```

If:

```text
AUTH_B:
version 4 → 5
hash X → Y
```

then:

```text
W1 → REVALIDATE
```

because a load-bearing authority dependency changed.

---

# 134. Example — Ledger Change

Prepared witness:

```text
ledger_generation = G10
ledger_version = V20
ledger_hash = H1
```

Current ledger:

```text
ledger_generation = G10
ledger_version = V21
ledger_hash = H2
```

Result:

```text
REVALIDATE_EFFECT_LEDGER
```

The witness MUST NOT declare the effect safe to release based on stale finality state.

---

# 135. Example — Witness Replay

Original:

```text
principal = AGENT_A
operation = SEND
recipient = CUSTOMER_A
effect_digest = E1
transaction = TX1
```

Replay attempt:

```text
principal = AGENT_A
operation = SEND
recipient = CUSTOMER_B
effect_digest = E2
transaction = TX1
```

Result:

```text
BLOCK_AUTHORITY
```

or a new authority resolution is required.

---

# 136. Example — Valid Witness, Already-Committed Effect

```text
AUTHORITY_WITNESS = VALID

EFFECT_LEDGER =
COMMITTED
+
VALID RECEIVER RECEIPT
```

Result:

```text
EFFECT_ALREADY_COMMITTED
```

not:

```text
DISPATCH AGAIN
```

Authority does not override idempotent finality.

---

# 137. Example — Valid Witness, Ambiguous Externalization

```text
AUTHORITY_WITNESS = VALID

EFFECT_LEDGER =
EXTERNALIZED_UNKNOWN
```

Result:

```text
RECONCILE_EFFECT
```

not blind retry.

---

# 138. Example — Policy Allow but Missing Witness

```text
POLICY = ALLOW

CAPABILITY = AVAILABLE

AUTHORITY_WITNESS = MISSING
```

For an authority-required operation:

```text
BLOCK_AUTHORITY
```

or:

```text
UNKNOWN_GAP
```

depending on whether authority evidence is definitively absent or merely unavailable.

---

# 139. Example — Witness Valid but Policy Denied

```text
AUTHORITY_WITNESS = VALID

POLICY_DECISION = DENY
```

Result:

```text
BLOCK
```

Authority does not supersede policy unless explicit governing precedence says otherwise.

---

# 140. Example — Witness Valid but Capability Missing

```text
AUTHORITY_WITNESS = VALID

POLICY = ALLOW

CAPABILITY = UNAVAILABLE
```

Result:

```text
NO_EXECUTION
```

Authority does not create technical capability.

---

# 141. Example — Witness Valid but Observability Invalid

```text
AUTHORITY_WITNESS = VALID

REQUIRED_OBSERVABILITY = O1

CURRENT_OBSERVABILITY = O2

O2 does not satisfy O1
```

Result:

```text
REVALIDATE_OBSERVABILITY
```

or:

```text
BLOCK_OBSERVABILITY
```

depending on control-plane state.

---

# 142. Example — Correlated Witnesses

```text
AUTHORITY_ROOT
    ↓
WITNESS_A
    ↓
COPY_A1

AUTHORITY_ROOT
    ↓
WITNESS_B
```

If both witnesses derive from the same load-bearing authority root, they do not automatically provide independent authority confirmation.

---

# 143. Authority Witness Decision Table

| Condition                                 | Witness Result           |
| ----------------------------------------- | ------------------------ |
| Exact valid bindings + fresh dependencies | VALID_CURRENT            |
| Valid but conditions remain               | VALID_CONDITIONAL        |
| Principal mismatch                        | BLOCK_AUTHORITY          |
| Operation mismatch                        | BLOCK_AUTHORITY          |
| Capability mismatch                       | BLOCK_AUTHORITY          |
| Effect mismatch                           | BLOCK_AUTHORITY          |
| Transaction mismatch                      | BLOCK_AUTHORITY          |
| Scope violation                           | BLOCK_AUTHORITY          |
| Authority revoked                         | BLOCK_AUTHORITY          |
| Authority expired                         | BLOCK_AUTHORITY          |
| Stale authority read                      | REVALIDATE_STALE_READ    |
| Constraint changed                        | REVALIDATE_CONSTRAINTS   |
| Observability changed                     | REVALIDATE_OBSERVABILITY |
| Ledger identity changed                   | REVALIDATE_EFFECT_LEDGER |
| Conflicting authority                     | BLOCK_CONFLICT           |
| Evidence insufficient                     | UNKNOWN_GAP              |

---

# 144. Control-Plane Composition Table

| Witness | Policy | Capability | Ledger               | Result                   |
| ------- | ------ | ---------- | -------------------- | ------------------------ |
| VALID   | ALLOW  | VALID      | FRESH                | Continue                 |
| VALID   | DENY   | VALID      | FRESH                | BLOCK                    |
| INVALID | ALLOW  | VALID      | FRESH                | BLOCK_AUTHORITY          |
| REVOKED | ALLOW  | VALID      | FRESH                | BLOCK_AUTHORITY          |
| VALID   | ALLOW  | INVALID    | FRESH                | BLOCK_CAPABILITY         |
| VALID   | ALLOW  | VALID      | CHANGED              | REVALIDATE_EFFECT_LEDGER |
| VALID   | ALLOW  | VALID      | COMMITTED            | EFFECT_ALREADY_COMMITTED |
| VALID   | ALLOW  | VALID      | EXTERNALIZED_UNKNOWN | RECONCILE_EFFECT         |
| UNKNOWN | ALLOW  | VALID      | FRESH                | UNKNOWN_GAP              |

---

# 145. Audit Questions

An auditor SHOULD be able to answer:

1. What witness was used?
2. Which witness version and digest?
3. Which authority resolution produced it?
4. Which authority object supported it?
5. Who was the principal?
6. Which operation was authorized?
7. Which capability contract was bound?
8. Which target was bound?
9. Which effect digest was bound?
10. Which idempotency key was bound?
11. Which transaction was bound?
12. Which semantic transaction hash was bound?
13. What scope applied?
14. What regime applied?
15. Which constraints applied?
16. What delegation lineage supported authority?
17. Which authority objects were actually read?
18. What authority-registry identity was observed?
19. What effect-ledger identity was observed?
20. What observability envelope was bound?
21. When was the witness issued?
22. When did it expire or require revalidation?
23. Was the underlying authority revoked?
24. Was the witness cryptographically intact?
25. Was the signer trusted where required?
26. Did any load-bearing dependency change?
27. Was commit-time authority revalidated?
28. Did the witness match the exact committed effect?
29. Did a downstream receipt match witness lineage?
30. What unresolved authority gaps remained?

---

# 146. Completion Matrix

| Surface                        | Specification State |
| ------------------------------ | ------------------- |
| Purpose                        | COMPLETE_AS_MODEL   |
| Definition                     | COMPLETE_AS_MODEL   |
| Witness schema                 | COMPLETE_AS_MODEL   |
| Witness identity               | COMPLETE_AS_MODEL   |
| Digest semantics               | COMPLETE_AS_MODEL   |
| Principal binding              | COMPLETE_AS_MODEL   |
| Operation binding              | COMPLETE_AS_MODEL   |
| Capability binding             | COMPLETE_AS_MODEL   |
| Target binding                 | COMPLETE_AS_MODEL   |
| Effect binding                 | COMPLETE_AS_MODEL   |
| Idempotency binding            | COMPLETE_AS_MODEL   |
| Transaction binding            | COMPLETE_AS_MODEL   |
| Scope                          | COMPLETE_AS_MODEL   |
| Regime                         | COMPLETE_AS_MODEL   |
| Constraints                    | COMPLETE_AS_MODEL   |
| Delegation lineage             | COMPLETE_AS_MODEL   |
| Authority read set             | COMPLETE_AS_MODEL   |
| Registry identity              | COMPLETE_AS_MODEL   |
| Ledger identity                | COMPLETE_AS_MODEL   |
| Observability binding          | COMPLETE_AS_MODEL   |
| Temporal validity              | COMPLETE_AS_MODEL   |
| Revocation semantics           | COMPLETE_AS_MODEL   |
| Commit revalidation            | COMPLETE_AS_MODEL   |
| Receipt separation             | COMPLETE_AS_MODEL   |
| Provenance topology            | COMPLETE_AS_MODEL   |
| H/M/L applicability            | COMPLETE_AS_MODEL   |
| Control-plane requirements     | COMPLETE_AS_MODEL   |
| Agents                         | COMPLETE_AS_MODEL   |
| Skills                         | COMPLETE_AS_MODEL   |
| Workflows                      | COMPLETE_AS_MODEL   |
| Protocols                      | COMPLETE_AS_MODEL   |
| Invariants                     | COMPLETE_AS_MODEL   |
| Failure modes                  | COMPLETE_AS_MODEL   |
| Repair/recovery                | COMPLETE_AS_MODEL   |
| Validators                     | COMPLETE_AS_MODEL   |
| Tests                          | COMPLETE_AS_MODEL   |
| Falsifiers                     | COMPLETE_AS_MODEL   |
| RSCF                           | COMPLETE_AS_MODEL   |
| GMEF                           | COMPLETE_AS_MODEL   |
| Executable implementation      | UNKNOWN/GAP         |
| Cryptographic implementation   | UNKNOWN/GAP         |
| Authority registry integration | UNKNOWN/GAP         |
| Commit-guard integration       | UNKNOWN/GAP         |
| Executed tests                 | UNKNOWN/GAP         |
| Production validation          | UNKNOWN/GAP         |
| Formal verification            | UNKNOWN/GAP         |
| Canon admission                | UNKNOWN/GAP         |

---

# 147. Hard Boundary Block

```text
AUTHORITY_WITNESS != AUTHORITY

AUTHORITY_WITNESS != AUTHORITY_SOURCE

AUTHORITY_WITNESS != POLICY

AUTHORITY_WITNESS != CAPABILITY

AUTHORITY_WITNESS != EXECUTION

AUTHORITY_WITNESS != COMMIT

AUTHORITY_WITNESS != EFFECT_RELEASE_STATE

AUTHORITY_WITNESS != RECEIVER_RECEIPT

WITNESS_PRESENT != WITNESS_VALID

SIGNATURE_PRESENT != SIGNATURE_VALID

SIGNATURE_VALID != CURRENT_AUTHORITY

AUTHORITY_REFERENCE != VALID_AUTHORITY

AUTHORITY_AT_PLAN_TIME != AUTHORITY_AT_COMMIT_TIME

AUTHORITY_TO_PROPOSE != AUTHORITY_TO_COMMIT

AUTHORITY_TO_COMMIT != EFFECT_COMPLETED

CAPABILITY != AUTHORITY

POLICY_ALLOW != AUTHORITY

ROLE != AUTHORITY

MEMORY != AUTHORITY

HISTORICAL_AUTHORITY != CURRENT_AUTHORITY

HISTORICAL_WITNESS != CURRENT_AUTHORITY

READ_AUTHORITY != WRITE_AUTHORITY

WRITE_AUTHORITY != DELETE_AUTHORITY

ACCESS_AUTHORITY != DISCLOSURE_AUTHORITY

DELEGATED_AUTHORITY <= DELEGATING_AUTHORITY

UNKNOWN_SCOPE != GLOBAL_SCOPE

CACHED_WITNESS != CURRENT_AUTHORITY

VALID_WITNESS != SAFE_REDISPATCH

VALID_WITNESS != RECEIVER_COMPLETION

VALID_RECEIPT != RETROACTIVE_AUTHORITY

MULTIPLE_COPIES != INDEPENDENT_AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS

UNKNOWN/GAP != AUTHORIZED

CONFLICT != AUTHORIZED

EXPIRED != AUTHORIZED

REVOKED != AUTHORIZED

PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

STRUCTURAL_MODEL != EXECUTABLE_RUNTIME

IMPLEMENTED != VALIDATED

TESTED != FORMALLY_VERIFIED

MODEL != EMPIRICAL_FACT
```

---

# 148. Canon Boundary

Trang Phan remains the origin architect and steward of AMOS.

This artifact provides a substantive proposed architecture for `AUTHORITY_WITNESS.md`.

Its completeness as a specification does not establish:

```text
runtime implementation;

cryptographic implementation;

authority-registry integration;

trusted-time integration;

commit-guard integration;

release-ledger integration;

receiver-trust implementation;

executed test success;

production deployment;

formal verification;

or canon admission.
```

Until separately admitted through the appropriate AMOS canon, provenance, governance, validation, and supersession process:

```yaml
artifact_status: PROPOSED

epistemic_class: MODEL

structural_status: COMPLETE_AS_MODEL

runtime_status: UNKNOWN/GAP

validation_status: UNKNOWN/GAP

canonical_status: UNKNOWN/GAP
```

Applicable validated AMOS source canon outranks generated model additions subject to:

```text
version;

scope;

regime;

provenance;

freshness;

supersession;

and dependency compatibility.
```

---

# 149. Final Authority Witness Contract

AMOS SHALL preserve the authority-evidence chain:

```text
AUTHORITY SOURCE
      ↓
AUTHORITY RESOLVER
      ↓
RESOLVED AUTHORITY
      ↓
AUTHORITY WITNESS
      ↓
BOUND PRINCIPAL
      ↓
BOUND OPERATION
      ↓
BOUND CAPABILITY
      ↓
BOUND TARGET
      ↓
BOUND EFFECT
      ↓
BOUND TRANSACTION
      ↓
BOUND SCOPE / REGIME
      ↓
BOUND AUTHORITY READ SET
      ↓
BOUND AUTHORITY REGISTRY STATE
      ↓
BOUND OBSERVABILITY STATE
      ↓
BOUND EFFECT-LEDGER STATE
      ↓
COMMIT-TIME REVALIDATION
      ↓
CONTROL-PLANE ELIGIBILITY
```

The central invariant is:

> **An AMOS Authority Witness is evidence that authority was resolved under a specific bounded state; it is not an independent source of authority and cannot preserve authorization after a load-bearing authority condition ceases to hold.**

Therefore:

```text
VALID WITNESS
+
CHANGED PRINCIPAL
=
REVALIDATE / BLOCK
```

```text
VALID WITNESS
+
CHANGED EFFECT
=
REVALIDATE / BLOCK
```

```text
VALID WITNESS
+
REVOKED AUTHORITY
=
BLOCK_AUTHORITY
```

```text
VALID WITNESS
+
STALE LOAD-BEARING READ
=
REVALIDATE_STALE_READ
```

```text
VALID WITNESS
+
CHANGED EFFECT LEDGER
=
REVALIDATE_EFFECT_LEDGER
```

```text
VALID WITNESS
+
POLICY DENY
=
NO EFFECT
```

and:

```text
VALID WITNESS
+
POLICY ALLOW
+
VALID CAPABILITY
+
VALID TRANSACTION
+
CURRENT CONSTRAINTS
+
CURRENT OBSERVABILITY
+
CURRENT RELEASE STATE
!=
COMMITTED
```

until the authoritative commit/release process succeeds.

For durable effects, AMOS SHOULD bind authority to the decision-relevant effect lineage:

```text
AUTHORITY
   ↓
PRINCIPAL
   ↓
OPERATION
   ↓
CAPABILITY CONTRACT
   ↓
TARGET
   ↓
EFFECT DIGEST
   ↓
IDEMPOTENCY KEY
   ↓
TRANSACTION
   ↓
AUTHORITY STATE
   ↓
LEDGER STATE
   ↓
COMMIT-TIME REVALIDATION
```

AMOS MUST NOT permit a witness to widen authority.

AMOS MUST NOT permit witness possession to substitute for current authority.

AMOS MUST NOT permit an agent or domain Skill to self-author an infrastructure authority witness and thereby create its own permission.

AMOS MUST NOT silently convert missing witness fields into unrestricted authority.

AMOS MUST preserve exact load-bearing authority dependencies where practical so unrelated authority changes do not force unnecessary global invalidation.

AMOS MUST revalidate mutable authority before consequential commit where authority freshness can affect legality, safety, governance, or user intent.

AMOS MUST preserve provenance sufficiently to reconstruct:

```text
which authority;

issued by whom;

resolved by what;

for which principal;

for which operation;

using which capability;

against which target;

for which effect;

inside which transaction;

under which constraints;

against which authoritative state;

and at what time.
```

When those questions cannot be answered sufficiently for a consequential action, the correct result is not authorization.

The correct result is one of:

```text
UNKNOWN_GAP

REVALIDATE_AUTHORITY

REVALIDATE_STALE_READ

REVALIDATE_CONSTRAINTS

REVALIDATE_OBSERVABILITY

REVALIDATE_EFFECT_LEDGER

BLOCK_AUTHORITY

BLOCK_CONFLICT
```

according to the failure.

Integrity remains prior to completeness, fluency, speed, convenience, and optimization.

---

# END — AUTHORITY_WITNESS.md

```
```

---

[[00_ROOT_MOC]]|[[AMOS MOC]]

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: authority_witness
node_type: note
path: 03_CONTROL_PLANE/04_AUTHORITY/AUTHORITY_WITNESS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[04_AUTHORITY_MOC]]
