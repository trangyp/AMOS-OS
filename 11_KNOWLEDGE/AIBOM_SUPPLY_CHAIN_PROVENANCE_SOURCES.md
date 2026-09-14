---
title: AIBOM Supply-Chain Provenance Sources
type: knowledge
status: SOURCE_CLAIM_REGISTRY
origin_architect: Trang Phan
---

# AIBOM supply-chain provenance sources

Pinned primary-source snapshots used to strengthen the AMOS AIBOM lifecycle layer on 2026-09-14:

- `CycloneDX/specification@595d98f16159bdf7463adc140509ded479130b8b` — component/dependency formats, machine-learning-model and model-card representation.
- `spdx/spdx-spec@c07600f239fbd9377be2195f4660887cfee72b78` — SPDX specification; signing/attestation work includes `d99772ca9816b1615c0e53a94525550054e6a83c`.
- `anchore/syft@ee05a595b664a512ac2a3add5a00faae2818c6d4` — package/file inventory, relationships and evidence; partial parsing should remain visible.
- `in-toto/attestation@2dcd055e9f72e746687c306e35f4e59720ff45be` — Statement/v1 subject/digest/predicate envelope.
- `slsa-framework/slsa@54b88b009fd45acb331c7e6578a526e0f36e0430` — build/dependency provenance model.
- `actions/attest@60c80190bb1a4fb35e5724ede753db5656412b68` — current GitHub artifact-attestation implementation surface.
- `actions/attest-build-provenance@9d57eef8c06cd9d6b433effeeb7a6a77b3ff94ad` — wrapper/documentation evidence connecting artifact digest, SLSA predicate, in-toto and Sigstore; new implementations route to `actions/attest`.
- `sigstore/cosign@633e8f4303b7db64c369bdfa315374a8bd511ac6` — signature/transparency verification ecosystem.
- `google/osv-scanner@e840a6e8adb14b7777c78e26cfbf6e2abc1d1fc6` — OSV-Scanner v2.6.0 source snapshot on 2026-09-14.

These sources provide mechanisms and format semantics only. Repository popularity, upstream claims, signatures, SBOM completeness, scanner findings or attestations do not grant AMOS authority or deployment validity.
