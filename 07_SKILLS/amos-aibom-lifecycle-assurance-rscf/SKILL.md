---
name: amos-aibom-lifecycle-assurance-rscf
description: Construct, normalize, validate, diff, and audit AI Bills of Materials and AI/software supply-chain evidence across source, code, Skills, agents, workflows, tools, models, datasets, dependencies, runtimes, containers, configs, build artifacts, attestations, vulnerabilities, and execution outputs. Use for AIBOM/SBOM lifecycle assurance, build/runtime identity, CycloneDX or SPDX intake, in-toto/SLSA attestations, signature evidence, vulnerability applicability, dependency drift, output binding, reproducibility closure, and supply-chain promotion checks where inventory, provenance, trust, completeness, authority, and semantic correctness must remain distinct.
---

# AMOS AIBOM Lifecycle Assurance

Origin architect: **Trang Phan**.

Treat the AIBOM as an evidence-bound lifecycle graph, not a package list and not an authorization token.

## Operating sequence

1. **Bind identity.** Resolve repository/source ref, build ID, environment ID, root artifact and policy requirements.
2. **Inventory.** Record typed components and digests. Preserve AI-specific objects such as models, datasets, model-card evidence, runtime/configuration and outputs separately from ordinary packages.
3. **Normalize.** Import supported CycloneDX/SPDX evidence into AMOS component and relationship types without erasing source format or source reference.
4. **Bind provenance.** Attach in-toto Statement/v1 evidence to exact component digests. Record signature verification only when an external verifier identity/version/evidence reference exists.
5. **Bind vulnerability evidence.** Record scanner/version/database snapshot plus version/configuration applicability. Preserve `UNKNOWN` when applicability is unresolved.
6. **Seal.** Seal only structurally valid manifests. Keep policy completeness separate from structural integrity.
7. **Verify.** Validate manifest hash, lineage, attestation binding, vulnerability attribution and compact receipt semantics with `scripts/audit_rscf.py`.
8. **Bind outputs.** Bind execution output hashes to the exact sealed AIBOM hash and, when available, trace/evaluation receipt identity.
9. **Diff lifecycle state.** Compare sealed manifests only within compatible source identity. Report material drift without manufacturing causality.
10. **Conclude narrowly.** State executed evidence, gaps, invalidators and authority boundary.

Use `scripts/aibom.py` for deterministic local lifecycle operations and `scripts/audit_rscf.py` for receipt validation.

## Typed state

Use these component kinds when applicable:

`SOURCE_REPO | CODE | SKILL | AGENT | WORKFLOW | TOOL | MODEL | DATASET | DEPENDENCY | RUNTIME | CONFIG | CONTAINER | BUILD_ARTIFACT | OUTPUT | OTHER`

Use explicit relations such as:

`DEPENDS_ON | BUILT_FROM | TRAINED_ON | CONFIGURED_BY | EXECUTES_ON | PACKAGED_IN | PRODUCES | USES_TOOL | EVALUATED_BY | DERIVED_FROM | DESCRIBES | CONTAINS`

Do not collapse model lineage, data lineage, software dependency, build identity, runtime identity, configuration and output provenance into one field.

## Hard invariants

- `BOM_PRESENT != COMPLETE_INVENTORY`
- `SBOM_PARSEABLE != TRUSTED`
- `DIGEST_MATCH != SIGNATURE_VERIFIED`
- `SIGNATURE_VERIFIED != SEMANTIC_CORRECTNESS`
- `ATTESTATION_PRESENT != ATTESTATION_VERIFIED`
- `PROVENANCE_VERIFIED != REPRODUCIBLE`
- `VULNERABILITY_ID_MATCH != VULNERABILITY_APPLICABLE`
- `SCANNER_NO_FINDINGS != NO_VULNERABILITIES`
- `MODEL_CARD_PRESENT != MODEL_SAFE`
- `BUILD_ATTESTATION != RUNTIME_IDENTITY`
- `RUNTIME_IDENTITY != OUTPUT_BINDING`
- `OUTPUT_BOUND != OUTPUT_CORRECT`
- `AIBOM_SEALED != POLICY_COMPLETE`
- `AIBOM_SEALED != DEPLOYMENT_AUTHORITY`
- `INVENTORY != AUTHORITY`

Missing evidence is `UNKNOWN/GAP`; it is never a pass.

## Structural integrity vs policy completeness

Keep two independent gates:

**Structural integrity** requires a valid root, digest syntax, closed recorded relations, bound attestation subjects, support for any claimed external signature verification, valid vulnerability attribution states, and a valid sealed manifest hash.

**Policy completeness** evaluates required evidence dimensions independently: attestation, verified signature, vulnerability evidence, environment identity, output binding and replay evidence.

A structurally valid AIBOM may be sealed while `policy_complete=false`. Never rewrite that state as VERIFIED.

## Vulnerability applicability

For component-present state `C`, version match `V`, and configuration match `G`:

- if any of `C,V,G` is unknown, applicability is `UNKNOWN`;
- otherwise applicability is `APPLICABLE` iff `C and V and G`;
- otherwise it is `NOT_APPLICABLE`.

A scanner finding must retain scanner identity/version, vulnerability database snapshot and evidence reference.

## Attestation and signature boundary

Accept only explicitly typed evidence. The portable runtime understands in-toto Statement/v1 subject-digest binding. `VERIFIED_EXTERNAL` means an external verifier was observed and its identity/version/evidence reference were captured; the local reference runtime does not itself perform cryptographic verification.

Cryptographic verification proves a bounded identity/integrity claim. It does not prove model safety, code correctness, absence of vulnerabilities, benchmark validity, authorization or deployment fitness.

## Reproducibility closure

Represent closure as a boolean vector rather than a decorative scalar:

`component_inventory, environment_identity, model_lineage, runtime_capture, output_binding, replay_evidence`.

`closed` is true only if every required dimension is true. Preserve each failing dimension so repair remains localizable.

## Lifecycle drift

Compare sealed manifests only when source repository identity is compatible. Preserve added, removed, digest-changed, version-changed and kind-changed component sets. Highlight changes in models, datasets, runtimes, configs, containers and build artifacts as material drift.

`AIBOM_DRIFT_DOES_NOT_IDENTIFY_CAUSE`.

## Privacy and persistence

Default to metadata, hashes and evidence references. Do not persist credentials, tokens, raw prompts, raw model outputs, hidden reasoning or secrets in the AIBOM runtime or receipts.

## Evidence classes

Keep these distinct:

- `SOURCE_CLAIM`: statements from external specifications/repositories.
- `OBSERVATION`: executed parser/validator/test/runtime evidence.
- `DERIVED`: conclusions that follow from bound evidence.
- `AMOS_MODEL`: AMOS-specific representation or policy semantics.
- `UNKNOWN/GAP`: unresolved evidence or unsupported claim.

No source or test grants authority.

## Required references

Read `references/assurance-boundaries.md` for state/equation semantics and `references/upstream-mechanisms.md` when source provenance or format boundaries matter.
