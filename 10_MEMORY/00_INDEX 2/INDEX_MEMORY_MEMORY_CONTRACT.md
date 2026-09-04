---
title: Memory Index Contract
type: index_contract
source: 10_MEMORY/00_INDEX
status: ACTIVE
conclusion_class: AMOS_MODEL
origin_architect: Trang Phan
---
# Memory Index Contract

The `00_INDEX` layer owns only navigation, naming, and resolution metadata.

## Hard boundaries
- It may point to artifacts; it may not redefine their semantics.
- It may report missing, duplicate, stale, or ambiguous targets.
- It may not authorize effects, promote canon, validate a model, or commit state.
- If two targets resolve to the same expected identity, preserve the conflict until authoritative lineage resolves it.
- Missing targets remain `UNKNOWN/GAP`; never synthesize replacement content from filenames.

The governing normative contract remains `../MEMORY_MEMORY_CONTRACT.md`.

## Contract Scope
This contract bounds the `00_INDEX` layer of `10_MEMORY` exclusively to navigation, naming, and identity-resolution metadata. It governs how index entries are created, resolved, and reported — not how memory artifacts themselves are authored or promoted.

Scope inclusions:
- Index entry creation, update, and retirement.
- Ambiguity and conflict detection during target resolution.
- Stale-link and missing-target reporting.
- Topology description for the Memory Map.

Scope exclusions:
- Artifact semantics, canon promotion, or epistemic class upgrade.
- Effect authorization, state commit, or model validation.
- Content synthesis from filenames or partial metadata.

## Invariants
1. `INDEXED != AUTHORITATIVE` — presence in the index does not confer authority.
2. `LINKED != VALIDATED` — a wikilink is a navigation pointer, not a validation proof.
3. `PRESENT != CURRENT` — an entry may exist while its target is stale.
4. Missing targets remain `UNKNOWN/GAP`; the index must never fabricate replacement content.
5. Duplicate or ambiguous targets are preserved as conflicts until lineage resolves them.
6. The index layer may not redefine the semantics of any artifact it points to.

## Validation Protocol
1. **Resolution check**: every index entry must resolve to exactly one target artifact or be marked `UNKNOWN/GAP`.
2. **Freshness check**: target `status` and `conclusion_class` are read from the artifact itself, not cached or inferred by the index.
3. **Conflict check**: if two entries resolve to the same expected identity, the conflict is surfaced — not silently deduplicated.
4. **Boundary check**: confirm the index has not authored semantic content, promoted canon, or committed state.

## AMOS Integration
- Parent contract: [[10_MEMORY/00_INDEX 2/MEMORY_MEMORY_MAP|Memory Map]] — topology surface for this index.
- Governing plane contract: [[10_MEMORY/MEMORY_MEMORY_CONTRACT|MEMORY_MEMORY_CONTRACT]] — normative Memory plane contract.
- Plane MOC: [[10_MEMORY/10_MEMORY_MOC|10_MEMORY_MOC]] — Memory plane map of content.
- Root navigation: [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] — vault-wide structural navigation.

## Epistemic Boundary
This contract is a `DERIVED` navigation contract. It does not prove that indexed artifacts are implemented, current, or authoritative. It does not establish cross-plane dependencies — those must be proven by each referenced artifact's own typed contract and provenance. Index completeness is not system completeness.

---

**Parent:** [[10_MEMORY/10_MEMORY_MOC|10_MEMORY_MOC]]
