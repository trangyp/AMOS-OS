---
title: AMOS AIBOM Provenance Verifier
type: tool
status: IMPLEMENTED_LOCAL_REFERENCE
epistemic_class: AMOS_MODEL
origin_architect: Trang Phan
---

# AMOS AIBOM Provenance Verifier

## Tier

`T1` for local manifest parsing, normalization, receipt validation, hash/lineage checking and manifest comparison.

External SBOM generation, hosted vulnerability databases, cryptographic signature verification, transparency-log queries, artifact-attestation APIs or registry calls are separate `T3` operations and require their own authority/credentials.

## Capabilities

- `AIBOM_NORMALIZE_LOCAL`
- `CYCLONEDX_JSON_IMPORT_LOCAL`
- `SPDX_JSON_IMPORT_LOCAL`
- `IN_TOTO_SUBJECT_BIND_VALIDATE`
- `AIBOM_STRUCTURAL_VERIFY`
- `AIBOM_POLICY_GAP_AUDIT`
- `VULNERABILITY_APPLICABILITY_CLASSIFY`
- `OUTPUT_BINDING_VALIDATE`
- `AIBOM_DRIFT_COMPARE`
- `AIBOM_LEDGER_VERIFY`

## Not capabilities

- mint signing identity or credentials;
- perform or claim cryptographic verification without external verifier evidence;
- query external vulnerability databases without separate T3 authority;
- prove semantic correctness, safety, exploitability or absence of vulnerabilities;
- deploy, merge or promote artifacts;
- convert inventory presence into authority.

## Firewalls

`LOCAL_PARSE != EXTERNAL_SCAN`

`DIGEST_MATCH != SIGNATURE_VERIFIED`

`SIGNATURE_VERIFIED != SEMANTIC_CORRECTNESS`

`VULNERABILITY_ID_MATCH != VULNERABILITY_APPLICABLE`

`AIBOM_SEALED != POLICY_COMPLETE`

`POLICY_COMPLETE != DEPLOYMENT_VALIDITY`

`AIBOM_EVIDENCE != AUTHORITY`
