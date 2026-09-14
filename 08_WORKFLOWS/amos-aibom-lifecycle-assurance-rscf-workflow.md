---
title: amos-aibom-lifecycle-assurance-rscf-workflow
type: workflow
skill: amos-aibom-lifecycle-assurance-rscf
agent: amos-aibom-lifecycle-assurance-rscf-agent
status: IMPLEMENTED_LOCAL_REFERENCE
version: 3.0.0
origin_architect: Trang Phan
epistemic_class: AMOS_MODEL
---

# Workflow: AMOS AIBOM Lifecycle Assurance

## Objective

Produce the narrowest defensible AI/software supply-chain evidence object while keeping inventory, provenance, cryptographic verification, vulnerability applicability, reproducibility, runtime identity, output binding and authority separate.

## State machine

```text
INTAKE
  -> BIND_IDENTITY
  -> INVENTORY
  -> NORMALIZE
  -> PROVENANCE_BIND
  -> VULNERABILITY_BIND
  -> STRUCTURAL_GATE
  -> SEAL
  -> VERIFY
  -> OUTPUT_BIND
  -> DRIFT_GATE
  -> RECEIPT
  -> TERMINAL
```

## Gates

### G1 — Identity

Bind repository/source ref, build ID, root component and policy. Missing load-bearing identity -> `UNKNOWN/GAP`.

### G2 — Inventory

Record component type, source format/reference and digest when available. Do not turn missing digests into synthetic identity.

### G3 — Provenance

An in-toto attestation must bind a subject SHA-256 to the recorded component digest. `VERIFIED_EXTERNAL` requires external verifier identity, version and evidence reference.

### G4 — Vulnerability

Record scanner identity/version and database snapshot. Applicability is tri-state and remains `UNKNOWN` if version/configuration evidence is incomplete.

### G5 — Structural integrity

Require root presence, digest syntax, closed recorded relations, valid attestation binding, supported signature claims, valid vulnerability attribution state and manifest-hash integrity.

### G6 — Policy completeness

Evaluate attestation, verified signature, vulnerability evidence, environment identity, output binding and replay evidence independently. A structural PASS cannot compensate for a required policy gap.

### G7 — Sealing

Seal immutable canonical manifest content only after structural integrity passes. `SEALED != POLICY_COMPLETE`.

### G8 — Output binding

Bind execution output hash to the exact sealed AIBOM hash. Trace/evaluation receipt identity may be attached when available. `OUTPUT_BOUND != OUTPUT_CORRECT`.

### G9 — Lifecycle drift

Compare only sealed manifests with compatible source repository identity. Return explicit component drift; do not infer cause.

## Deterministic checks

```bash
python 07_SKILLS/amos-aibom-lifecycle-assurance-rscf/scripts/aibom.py --self-test
python 07_SKILLS/amos-aibom-lifecycle-assurance-rscf/scripts/audit_rscf.py --self-test
python -m unittest -v 19_TESTS/test_aibom_lifecycle_runtime.py
```

## Terminal statuses

- `STRUCTURALLY_VALID`
- `POLICY_COMPLETE`
- `POLICY_INCOMPLETE`
- `INVALIDATED_EVIDENCE`
- `NOT_COMPARABLE`
- `UNKNOWN/GAP`

These are evidence statuses, not authority states.

## Recovery

- malformed or sensitive raw persisted fields -> reject;
- missing component identity -> preserve gap;
- attestation subject mismatch -> reject attestation;
- unsupported signature claim -> reject claim;
- stale/tampered sealed manifest -> invalidate evidence;
- source identity mismatch -> `NOT_COMPARABLE`;
- external scanner/verifier unavailable -> preserve `UNKNOWN/GAP` rather than fabricate evidence.

## Terminal invariants

`AIBOM_EVIDENCE != AUTHORITY`

`POLICY_COMPLETE != DEPLOYMENT_VALIDITY`

`SIGNATURE_VERIFIED != SEMANTIC_CORRECTNESS`
