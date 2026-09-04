---
title: AMOS CORE V4 4
artifact: "AMOS_CORE_V4_4.md"
artifact_id: "amos_11_knowledge_amos_core_v4_4"
origin_architect: "Trang Phan"
steward: "Trang Phan"
system: "AMOS OS"
plane: "11_KNOWLEDGE"
segment: "11_KNOWLEDGE"
artifact_kind: "ARTIFACT"
path: "11_KNOWLEDGE/AMOS_CORE_V4_4.md"

tags:
  - amos_os
  - 11_knowledge
  - artifact
  - canon_placeholder
  - rscf

version: "0.1.0"
updated: "2026-09-04"

status: "CANON_REFERENCE"
epistemic_class: "AMOS_MODEL"
canonical_status: "CANON_REFERENCE"
implementation_status: "NOT_ESTABLISHED"
validation_status: "NOT_ESTABLISHED"
executable_binding: "NOT_ESTABLISHED"
ingestion_action: "ADD_ONLY"
---

# AMOS CORE V4.4 — Canonical Reference

## 0. Status (updated 2026-09-04)

This artifact was an ADD-ONLY placeholder. The canonical specification it reserves a slot for **exists** in the corpus: [[00_ROOT/AMOS_CORE_v4_4|AMOS_CORE_v4_4]] (`00_ROOT/AMOS_CORE_v4_4.md`, ~37KB, `CANON_SPEC` / `AMOS_SYSTEM_CORE` / provenance `AMOS_ENGINEERING`).

This file is now a **canonical reference note** — it points to and summarizes the canonical spec rather than duplicating it (per the ingestion rule: one canonical node, all provenance linked, no duplicate canon).

## 1. Canonical target

**[[00_ROOT/AMOS_CORE_v4_4|AMOS Core v4.4 — Coordination-Avoidance Runtime Architecture]]**

Source-declared classification of the canonical spec:

```yaml
rscf:
  state: CANON_SPEC
  claim_class: AMOS_SYSTEM_CORE
  provenance: AMOS_ENGINEERING
```

## 2. What the canonical spec establishes (summary)

The v4.4 spec defines a decentralized, coordination-avoiding execution architecture for parallel subagents that maintains causal consistency without centralized serialization as the default path. Its major sections:

- **Coordination avoidance & proof-based coordination avoidance** — operations proceed without live coordination when a proof capsule discharges the coordination obligation.
- **Parallel subagent model, dependency closure, provenance independence** — subagents execute in parallel only under declared dependency closure; correlated provenance is not independent confirmation.
- **Causal consistency, causal lineage, locality of failure** — causal order is the correctness contract; failures are contained at the smallest causal scope.
- **Conflict model & non-conflict requirement** — conflicts are defined and required to be absent at commit, not resolved afterward.
- **Scope / regime / freshness firewalls** — every object carries scope, regime, and freshness boundaries that bound its authority.
- **Atomic multi-RSCF reasoning** — coupled commits are all-or-none (see [[02_KERNEL/ATOMIC_MULTI_RSCF|ATOMIC_MULTI_RSCF]]).
- **MVCC/CAS architectural concepts** — modeled as reasoning patterns, not host guarantees (see [[01_CANON/01_CORE_LAWS/L23_MVCC_CAS|L23]]).
- **Stale-read protection, proposal≠commit, authority firewall, commit preconditions, failed-premise semantics** — the commit-gate discipline.
- **Causal epochs & shard-local finalization** — epoch finality (L24) and shard-local finalize rules (L25) as governance patterns.

## 3. Epistemic boundary (carried from the canonical spec)

```text
Architecture specification != proof of deployed implementation
MODEL != DEPLOYED_RUNTIME
```

The canonical spec itself is `AMOS_MODEL`-class: it describes the architecture but does not establish an executing runtime.

## 4. Lineage

AMOS_CORE lineage: v3.0 → v4.4 (current canonical target). Do not claim or apply post-v4.4 canonical labels (e.g., v4.8-style versions) without governed successor evidence.

---

RSCF-NODE

node_id: amos_11_knowledge_amos_core_v4_4

node_type: artifact

path: 11_KNOWLEDGE/AMOS_CORE_V4_4.md

claim_class: AMOS_MODEL

rscf_state: canon_reference

canonical_status: CANON_REFERENCE

RSCF-RELATIONS:

  - INDEXED_BY: [[00_ROOT/00_HOME]]

  - INDEXED_BY: [[AMOS_RSCF_NODES]]

  - GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY]]
