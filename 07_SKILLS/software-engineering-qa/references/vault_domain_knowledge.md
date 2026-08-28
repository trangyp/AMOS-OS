---
title: "Vault Domain Knowledge — Software Engineering Qa"
type: reference
source: 07_SKILLS/software-engineering-qa/references
tags: [reference, software-engineering-qa, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `software-engineering-qa`

## Vault-Sourced Domain Knowledge

> **Source**: `11_KNOWLEDGE/AMOS_C10_TECH_ENGINEERING_MASTER_KNOWLEDGE.md` from the AMOS_OS Obsidian vault.

### Claim Classes (C10)
- **VERIFIED** — strongly supported engineering result within a stated regime.
- **DERIVED** — mathematical or logical consequence of stated premises/model.
- **MODEL** — representation useful within stated scope.
- **CONDITIONAL** — dependent on explicit assumptions, workload, or regime.
- **COMPETING** — unresolved alternatives (e.g., monolith vs microservices).
- **UNKNOWN/GAP** — insufficient evidence or unresolved mechanism.

### Architecture Design Discipline (H2)
- Every architecture decision requires explicit functional requirements, non-functional requirements, constraints, and scale assumptions.
- **Rule of 2**: at least two architectural approaches must be held concurrently until trade-offs are explicit.
- **Pattern selection discipline**: `selected_pattern + rejected_alternatives + why`.
- **Validation firewall**: architecture output is design, not a working system. Every recommendation carries assumptions stated, alternatives compared, uncertainty labelled, validation and implementation acknowledged.

### Integration Contracts (H5)
- No direct calls without a contract. Every integration declares data shapes, SLA, failure semantics, and rejection protocol.
- Rejects are REASONED (documented reason codes), never silent.
- Circuit breaker lifecycle: closed -> open on failure threshold -> half_open after cooldown.

### Security Architecture (H6)
- Trust boundary mapping by data sensitivity and authority level.
- Least-privilege surface minimization — each list starts empty and earns entries.
- Fail-closed verification — timeout = deny, parse failure = deny, unknown state = deny.
- Living threat model — ranked by impact x reachability.

### Engineering Causal Firewall (H7)

Do not infer causation from:
- correlation between metrics alone
- before/after deployment sequence alone
- benchmark fit alone
- mechanistic plausibility alone

Causal evidence draws from controlled experiments, canary rollouts with holdout, incident replication, and convergent independent telemetry.

### Data Pipeline Quality (H3)
- Quality dimensions: validity, completeness, accuracy, consistency, freshness.
- Stale data served without staleness flags is worse than explicit unavailability.
- Pipelines require declared trigger semantics, retry policy, idempotency of writes, dead-letter paths, and backfill capability.
- Two datasets derived from the same upstream feed are not independent confirmation of anything.

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
node_id: software-engineering-qa-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/software-engineering-qa/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
