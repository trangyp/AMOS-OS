---
title: "Research Papers Ingestion & Peer Review Contract"
type: control_contract
source: 22_RESEARCH/01_PAPERS
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_GOVERNING_CONTRACT
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 22_RESEARCH/RESEARCH_RESEARCH_CONTRACT
  scope: papers_ingestion
tags:
  - amos-os
  - research
  - papers
  - arxiv
---

# Research Papers Ingestion & Peer Review Contract

## 1. Mandate
Governs the intake, metadata extraction, mathematical parsing, and peer evaluation of scientific papers, arXiv preprints, and formal monographs.

## 2. Intake Invariants
1. Every ingested paper must be assigned an immutable RSCF identity: `arxiv-{arxiv_id}-{slug}`.
2. Abstract, methodology, proofs, and conclusions must be separated into distinct typed sections.
3. Claims cannot be promoted to verified truth merely by being published in high-impact venues (`M04: SOURCE_CLAIM != VERIFIED`).

## Contract Scope
This contract governs the full lifecycle of scientific paper ingestion within `22_RESEARCH/01_PAPERS`: from raw intake and identity assignment, through metadata extraction and mathematical parsing, to peer evaluation and archival. It binds all agents and processes that read, write, or route paper artifacts.

Scope inclusions:
- ArXiv preprints, formal monographs, and scientific papers.
- RSCF identity assignment and immutable provenance binding.
- Section separation (abstract, methodology, proofs, conclusions).
- Peer review evaluation and claim classification.

Scope exclusions:
- Canon promotion of paper claims to verified truth.
- Cross-plane dependency establishment for non-research artifacts.
- Runtime execution or deployment of research-derived models.

## Invariants
1. **Immutable identity**: every paper receives `arxiv-{arxiv_id}-{slug}` at intake; this identity never changes.
2. **Section separation**: abstract, methodology, proofs, and conclusions are distinct typed sections — never merged.
3. **No venue promotion**: publication venue impact does not upgrade `SOURCE_CLAIM` to `VERIFIED` (`M04`).
4. **Provenance preservation**: the original source URL, author list, and ingestion timestamp are immutable metadata.
5. **Claim classification**: every extracted claim retains its RSCF `claim_class` — never auto-promoted.
6. **Fail closed**: ambiguous or unparseable papers remain `UNKNOWN/GAP` until resolved by authoritative review.

## Validation Protocol
1. **Identity check**: confirm `arxiv-{arxiv_id}-{slug}` matches the source arXiv ID and is unique within the corpus.
2. **Section check**: verify abstract, methodology, proofs, and conclusions are present and typed correctly.
3. **Claim check**: verify no claim has been auto-promoted beyond `SOURCE_CLAIM` without peer review evidence.
4. **Provenance check**: confirm source URL, authors, and ingestion timestamp are present and immutable.
5. **Peer review check**: if peer evaluation has occurred, confirm the reviewer identity and evaluation timestamp are recorded.

## AMOS Integration
- Parent contract: [[22_RESEARCH/RESEARCH_RESEARCH_CONTRACT|RESEARCH_RESEARCH_CONTRACT]] — governing Research plane contract.
- Plane MOC: [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]] — Research plane navigation.
- Knowledge index: [[11_KNOWLEDGE/ARXIV_66K_INDEX_MANIFEST|ArXiv 66k Research Manifest]] — structured research index.
- Root navigation: [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] — vault-wide structural navigation.

## Epistemic Boundary
This contract is an `AMOS_MODEL` governing ingestion and peer review. It does not prove that ingested claims are true, that peer review is infallible, or that high-impact publication confers verification. `SOURCE_CLAIM != VERIFIED`, `PUBLISHED != PROVEN`, `PEER_REVIEWED != CANON`. Cross-plane dependencies require the referenced artifact's own typed contract.

---

**Parent:** [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
