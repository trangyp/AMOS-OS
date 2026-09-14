# Upstream mechanism provenance

External material is `SOURCE_CLAIM`. Mechanisms are adapted; upstream code is not vendored.

## CycloneDX specification

Pinned snapshot: `CycloneDX/specification@595d98f16159bdf7463adc140509ded479130b8b`.

Adapted mechanisms:
- component/dependency graph representation;
- SHA-256 component hashes;
- `machine-learning-model` component type;
- model-card fields for intended use, limitations, bias/ethical considerations, training parameters and datasets.

AMOS preserves model-card evidence as a hash/reference by default rather than copying sensitive/raw card content into receipts.

## SPDX specification

Pinned snapshot: `spdx/spdx-spec@c07600f239fbd9377be2195f4660887cfee72b78`.

Relevant mechanism boundary: SPDX package/checksum/relationship inventory remains distinct from trust. The 2026-08-25 source commit `d99772ca9816b1615c0e53a94525550054e6a83c` added signing/attestation sections, reinforcing that document representation and attestation are separate evidence surfaces.

## Anchore Syft

Pinned snapshot: `anchore/syft@ee05a595b664a512ac2a3add5a00faae2818c6d4`.

Adapted mechanisms:
- package/file cataloging before relationship derivation;
- explicit package/file evidence and digests;
- partial/unknown parsing evidence should remain visible rather than producing a falsely complete inventory.

Syft is an upstream ecosystem source, not an AMOS runtime dependency in this Skill.

## in-toto Attestation

Pinned snapshot: `in-toto/attestation@2dcd055e9f72e746687c306e35f4e59720ff45be`.

Adapted Statement v1 envelope:
- `_type = https://in-toto.io/Statement/v1`;
- `subject[]` with named artifact digest;
- `predicateType`;
- typed `predicate`.

AMOS local runtime validates subject SHA-256 binding but does not perform cryptographic signature verification itself.

## SLSA

Pinned snapshot: `slsa-framework/slsa@54b88b009fd45acb331c7e6578a526e0f36e0430`.

Adapted mechanisms:
- provenance and dependency evidence are build-context evidence;
- dependency track and build provenance should not be collapsed into runtime/output identity;
- generation and verification remain distinct operations.

## GitHub artifact attestations

Current implementation source: `actions/attest@60c80190bb1a4fb35e5724ede753db5656412b68`.

Wrapper evidence: `actions/attest-build-provenance@9d57eef8c06cd9d6b433effeeb7a6a77b3ff94ad` states build provenance binds a named artifact+digest to an SLSA predicate in in-toto format and that new implementations should use `actions/attest`.

AMOS does not require this hosted action for local reference validation and does not treat a GitHub attestation as deployment authority.

## Sigstore Cosign

Pinned snapshot: `sigstore/cosign@633e8f4303b7db64c369bdfa315374a8bd511ac6`.

Adapted boundary:
- signature verification is cryptographic identity/integrity evidence;
- verifier identity/version and evidence reference must be retained;
- signature validity is not semantic correctness, vulnerability absence, or authorization.

## OSV-Scanner

Pinned current release snapshot: `google/osv-scanner@e840a6e8adb14b7777c78e26cfbf6e2abc1d1fc6` (`v2.6.0`, 2026-09-14).

Adapted boundary:
- vulnerability evidence is scanner/version/database-snapshot bound;
- finding identifier alone does not prove applicability;
- configuration and component/version evidence remain explicit;
- no-finding output is not proof of no vulnerability.
