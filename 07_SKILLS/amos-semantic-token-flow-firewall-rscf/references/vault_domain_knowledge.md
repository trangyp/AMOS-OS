---
title: Vault Domain Knowledge — Amos Semantic Token Flow Firewall Rscf
type: reference
source: 07_SKILLS/amos-semantic-token-flow-firewall-rscf/references
tags:
- reference
- amos-semantic-token-flow-firewall-rscf
- canon/skill
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `amos-semantic-token-flow-firewall-rscf`

## Vault-Sourced Content

### Source 1: CSRF--CSRF_tokens

> Path: `misc/CS/CSRF--CSRF_tokens.md` | Size: 1703 chars | Match score: 10 | content_hash: c03504fb30225ae0

## CSRF tokens
What are they?

How should the tokens be generated

How are the tokens transmitted?

How should the tokens be validated?

---

---

### Source 2: AMOS Token and Context Governor

> Path: `misc/TO/TOKEN.md` | Size: 1147 chars | Match score: 10 | content_hash: 1b42a1453132a3d6

# AMOS Token and Context Governor

## Objective
Maximize decision-relevant information per token without deleting load-bearing structure.

## Priority score
Retain context in this order:
1. objective and hard constraints
2. decision-changing evidence
3. unresolved contradictions
4. load-bearing premises
5. provenance/freshness/scope
6. active hypotheses
7. required implementation details
8. reusable summaries
9. examples/background
10. redundant narrative

## Progressive disclosure
Do not load raw evidence by default.
Use:
`capsule -> relevant H -> relevant M -> relevant L -> raw`

## Drop rule
Drop an item only if removing it cannot reasonably change:
- answer
- decision
- confidence
- safety
- falsifier
- implementation correctness

## Context pressure
When context is near capacity:
- preserve constraints over prose,
- preserve dependency edges over explanations,
- preserve unresolved conflict over resolved history,
- snapshot before major compression.

---

---

### Source 3: ArenaSim — Resource Consumption Across AMOS Semantic Types

> Path: `dated/2026-08-22/2026-08-22-ArenaSim-Resource-Consumption-Semantic-Types.md` | Size: 36424 chars | Match score: 7 | content_hash: 6792fec113e6fa9d

# ArenaSim — Resource Consumption Across AMOS Semantic Types


semantic type's resource consumption (time, memory, social bandwidth) under
competitive pressure. Founding claim: semantic type distinctions (MODEL ≠ ENGINE
≠ AGENT ≠ PROTOCOL) produce empirically distinct resource consumption signatures.*

---

## tl;dr

ArenaSim runs from `cosmo/ArenaSim.py` (~1085 lines). It instantiates 7+ arenas,
each annotated with an AMOS semantic type. The MultiArenaRunner runs all arenas for
N steps, collecting per-step resource metrics. The CosmoBrainArena (`cosmo/CosmoBrainArena.py`,
~394 lines) is the AMOS component wrapper that frames the results as normative
hypotheses and validates each arena against AIMS v1.0.

ComponentManifest validations. Deterministic (same seed → same trace hash; different
seed → different hash).

Plus: CWS ENGINE+AGENT composition (`cosmo/CivilizationWithSpecialists.py`, 280 lines,
`cosmo/test_cws.py`, 8 tests, 8/8 PASS) — tests ENGINE+AGENT. Finding: ENGINE structure
CONSTRAINS AGENT time (-14%). 8/8 tests pass.

Plus: NetworkedEcology PROTOCOL+MODEL composition (`cosmo/NetworkedEcology.py`, 370 lines,
`cosmo/test_networked_ecology.py`, 8 tests, 8/8 PASS) — tests PROTOCOL+MODEL. Finding:
PROTOCOL adds STRUCTURED social (0.0022) — non-zero but 15× lower than AGENT social
(0.0332). 8/8 tests pass.

Plus: Arena Composition Algebra v2 (`cosmo/composition_algebra_v2.py`, 272 lines) —
formalises all three type-pair compositions. KEY FINDING: each type pair produces a unique
composition signature; composition is NOT commutative.

---

## The 7+ Arenas

| Arena Class | AMOS Semantic Type | Competitive Regime | What It Tests |
|:------------|:-------------------|:-------------------|:--------------|
| `MarketArena` | MODEL | Order book, price/volume/volatility | Do MODEL arenas consume zero social bandwidth? |
| `EcoArena` | MODEL | Organisms, energy, births/deaths | Does population survive under resource constraints? |
| `EcoSystemArena` | MODEL + PROTOCOL (alliances) | Ecology + social hierarchy + alliances | Does social bandwidth emerge when alliances are added? |
| `CivilArena` | ENGINE | 5 institutions with authority/knowledge/rules | Does ENGINE produce the highest memory consumption? |
| `NetworkArena` | PROTOCOL | Nodes, edges, messages, bandwidth | Does PROTOCOL produce moderate social bandwidth? |
| `DecisionArena` | AGENT | Weighted voting, authority+knowledge | Does AGENT produce the highest time consumption? |
| `CollectiveArena` | AGENT | Specializations, shared memory, tasks | Does AGENT produce the highest social bandwidth? |
| `HybridArena` | MODEL + AGENT | Ecology competition + agent specialization | Does MODEL substrate boost AGENT social? (Answer: YES, ×2) |
| `CivilizationWithSpecialists` | ENGINE + AGENT | Institutions + specialization + shared memory | Does ENGINE structure constrain AGENT time? (Answer: YES, -14%) |
| `NetworkedEcology` | PROTOCOL + MODEL | Ecology competition + network message passing | Does PRO

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[references_MOC]] · [[07_SKILLS_MOC]]

**MOC:** [[references_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-semantic-token-flow-firewall-rscf-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-semantic-token-flow-firewall-rscf/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
