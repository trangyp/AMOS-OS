---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: conditional
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: AMOS_MODEL
topic: C01 Governance Control Planes Cognitive Matrix Definition
created: 2026-08-22
updated: 2026-09-14
---

# C01 — Governance

**Package:** `C01_GOVERNANCE`  
**Class:** `COGNITIVE_MATRIX_CONTROL_PLANE`  
**Origin architect / steward:** Trang Phan  
**Status:** `EXECUTABLE_BOUNDED_REFERENCE / TESTED_LOCAL_SEMANTICS`

## Scope

C01 validates a bounded authority request. It does not infer authority from confidence, capability, model output, or successful tests.

A request may produce a fresh `AuthorityWitness` only when all of the following hold:

1. the enforcement root is externally attested;
2. the enforcement root is agent-write-excluded;
3. the observed precedence version equals the expected precedence version;
4. the governance epoch is fresh;
5. the requested authority scopes are explicit and unique;
6. the policy hash is explicit;
7. the state version is explicit;
8. a consequential-decision receipt is present.

## Receipt identity

The bounded reference computes a deterministic governance receipt

`R = SHA256(canonical_json(decision_receipt_id, enforcement_root_id, policy_hash, precedence_version, principal, request_id, sorted(scopes), state_version))`.

This receipt binds the validated request identity. It is not a receiver receipt and does not prove that any external effect occurred.

## Authority boundary

A successful C01 result creates only a scoped, state-bound authority witness.

```text
MODEL_CONFIDENCE != AUTHORITY
CAPABILITY != AUTHORITY
TEST_PASS != AUTHORITY
C01_AUTHORITY != C08_STAGE
C01_AUTHORITY != EFFECT_COMMIT
```

Downstream effect release still requires the infrastructure commit/finality controls.

## Executable binding

Reference runtime:

`04_RUNTIME/01_REFERENCE_IMPLEMENTATION/c01_governance_runtime.py`

Adversarial tests:

`04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_c01_governance_runtime.py`

The GitHub reference-runtime lane passed the adversarial C01 test revision on 2026-09-14. This supports only the tested bounded implementation semantics.

## Remaining gaps

- cryptographic enforcement-root attestation is not implemented here;
- external trust-root independence is not established;
- distributed revocation/finality is not established;
- policy correctness itself is not proved by this validator;
- production authorization deployment remains separately governed.

These remain `UNKNOWN/GAP` outside the local bounded reference.

[[25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_MOC|COGNITIVE_MATRIX_MOC]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
