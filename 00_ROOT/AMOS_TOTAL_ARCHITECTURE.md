---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Amos Total Architecture
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# AMOS Total Architecture — Unified Full Brain OS Specification

**Origin architect / steward:** Trang Phan  
**Status:** `POPULATED_ARCHITECTURE`  
**Lineage target:** `AMOS Core v4.4`  
**Epistemic classification:** `AMOS_MODEL`  

---

## 1. Executive Architectural Overview

The **AMOS Total Architecture** establishes the comprehensive, mutually exclusive and collectively exhaustive (MECE) systems model for AMOS OS.

The numbered planes of AMOS (`00_ROOT` through `25_COGNITIVE_MATRIX`) are **physical and operational namespaces**, not twenty-five peer cognitive systems and not a single linear call chain.

```text
FUNCTIONAL OWNERSHIP != PHYSICAL STORAGE
AUTHORITY PRECEDENCE != STRUCTURAL CONTAINMENT
RUNTIME CALL ORDER   != ONTOLOGICAL DEPENDENCE
EVIDENCE / RECEIPT   != CAPABILITY SPECIFICATION
```

The Total Architecture models governed cognitive computing across three macro-systems, six MECE functional domains, and cross-cutting substrate invariants.

---

## 2. The Tripartite Full Brain Model

The architecture separates cognition, runtime state, and physical effect governance into three distinct systems:

```text
┌────────────────────────────────────────────────────────────────────────┐
│                              AMOS BRAIN                                │
│ Representation · Cognition · Coordination · Capability · World Models  │
│ (05 Cognitive Organism, 25 Cognitive Matrix, 11 Knowledge, 13 Models)  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ (Proposals / Inferences)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                             AMOS RUNTIME                               │
│ Typed Reasoning State · RSCF Algebra · H/M/L · Memory · Replay · State │
│     (04 Runtime, 09 Protocols, 10 Memory, 12 State, 16 Schemas)        │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ (Execution Batches / Transactions)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                          AMOS CONTROL / BODY                           │
│ Authority Grants · Capability Leases · Semantic Commit · Gated Effects │
│  (03 Control Plane, 14 Tools, 15 Interfaces, 18 Security, 23 Op Model) │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Six MECE Functional Responsibility Domains

Every numbered physical plane in AMOS OS belongs to exactly **one** primary responsibility domain:

### Domain A — Normative & Governance Definition
*Owns:* Admitted definitions, core laws, lineage, decision rights, and organizational accountability.
* **`01_CANON`**: Admitted laws, axioms, invariances, variable registries, glossary, and supersession.
* **`23_OPERATING_MODEL`**: Roles, decision rights, governance forums, escalation protocols, and service levels.
* *Explicit non-ownership:* Runtime execution, empirical validation, cognitive inference, external effects.

### Domain B — Execution Core & Effect Governance
*Owns:* Deterministic reasoning primitives, active execution lifecycle, and durable-effect authorization.
* **`02_KERNEL`**: Deterministic logic kernels (QLS, ULK), algebraic state-integrity primitives.
* **`03_CONTROL_PLANE`**: Authority enforcement, semantic transactions, commit-time revalidation, finality gates.
* **`04_RUNTIME`**: Bounded execution lifecycle, task scheduling, replay/recovery basins, and runtime state transitions.
* *Explicit non-ownership:* Domain-specific truth, cognitive strategy, canon creation without review.

### Domain C — Cognitive Capability & Orchestration
*Owns:* Cognitive loops, specialized actor identities, capability libraries, and workflow state transitions.
* **`05_COGNITIVE_ORGANISM`**: Persistent cognitive loops, perceptual organs, supervisory cognition, self-regulation.
* **`06_AGENTS`**: Bounded worker, orchestrator, and auditor identities.
* **`07_SKILLS`**: Versioned, reusable capability procedures and tool recipes.
* **`26_WORKFLOWS`**: Multi-step process orchestration and state-machine transitions.
* **`21_DOMAINS`**: Specialist domain taxonomy and subject-matter knowledge routing.
* **`25_COGNITIVE_MATRIX`**: Fractal cognitive coordinate decomposition (19×19 field and scales).
* *Explicit non-ownership:* Durable authority grants, platform-level state commit.

### Domain D — Information, Memory, State & Model Substrate
*Owns:* Persisted knowledge representations, versioned state epochs, and system simulations.
* **`10_MEMORY`**: Governed temporal persistence, episodic/semantic retrieval, working memory buffers.
* **`11_KNOWLEDGE`**: Cross-domain knowledge graph, research synthesis, claim networks, and arXiv integration.
* **`12_STATE`**: Machine state snapshots, epochs, identity ledgers, and divergence trackers.
* **`13_MODELS`**: Explicit mathematical models, causal diagrams, and simulation systems.
* **`16_SCHEMAS`**: Canonical tensor contracts, JSON schemas, and structured record definitions.
* *Explicit non-ownership:* Policy decision rights, truth promotion without verification.

### Domain E — Interaction, Security & Effect Adapters
*Owns:* Physical I/O adapters, component communication handoffs, and boundary defense.
* **`09_PROTOCOLS`**: Standard communication contracts, handoff schemas, and wire protocols.
* **`14_TOOLS`**: Concrete host tool implementations, CLI drivers, and MCP executors.
* **`15_INTERFACES`**: Typed UI/UX surfaces, API boundaries, and multimodal interaction points.
* **`18_SECURITY`**: Access control lists, cryptographic trust roots, credential firewalls, isolation perimeters.
* *Explicit non-ownership:* Domain semantics, execution scheduling.

### Domain F — Assurance, Learning & Lifecycle Evidence
*Owns:* Telemetry, test harnesses, recovery operations, research acquisition, and historical archive.
* **`17_OBSERVABILITY`**: Telemetry pipelines, distributed traces, audit logs, failure diagnostics.
* **`19_TESTS`**: Formal test suites, regression test benches, metamorphic verification harnesses.
* **`20_OPERATIONS`**: Runbooks, incident handling, backup procedures, maintenance schedules, audit ledgers.
* **`22_RESEARCH`**: Active external research intake, experimental evaluation, literature benchmarks.
* **`24_ARCHIVE`**: Historical deprecations, superseded artifacts, legacy lineages.
* *Explicit non-ownership:* Root authority, live execution gating.

---

## 4. Plane Ownership Completeness Check

```text
Domain A: {01, 23}
Domain B: {02, 03, 04}
Domain C: {05, 06, 07, 08, 21, 25}
Domain D: {10, 11, 12, 13, 16}
Domain E: {09, 14, 15, 18}
Domain F: {17, 19, 20, 22, 24}

Union(A..F) = {01, 02, ..., 25}  (Exhaustive)
Intersection(Any Pair) = ∅        (Mutually Exclusive)
00_ROOT = Meta-Plane (Root navigation, authority pointers, master index)
```

---

## 5. Architectural Invariants

Every operation touching AMOS must satisfy the ten structural invariants:

1. **Hierarchy of Truth:** `CANON > KERNEL > CONTROL PLANE > RUNTIME > CAPABILITY > ADAPTERS`.
2. **Authority Decoupling:** Capability does not grant authority (`CAPABILITY != AUTHORITY`).
3. **Commit Discipline:** Proposals are non-committal until control-plane gates validate (`PROPOSAL != COMMIT`).
4. **Epistemic Honesty:** Gaps and uncertainties are preserved explicitly (`UNKNOWN/GAP != PASS`).
5. **Reversibility Basin:** Consequential mutations must define a rollback basin prior to execution.
6. **Provenance Chain:** Every derived claim must trace its dependency closure back to admitted sources.
7. **Failure Locality:** Failures in specialist cognition (Domain C) must be isolated by Runtime (Domain B).
8. **Freshness Enforcement:** State changes invalidate stale cache records across registry surfaces.
9. **Single Stewardship:** Trang Phan remains the sole origin architect and steward of AMOS.
10. **Archive Preservation:** Historical lineage is never deleted; superseded versions migrate to `24_ARCHIVE`.

---

## 6. Governed Retrieval Protocol

When traversing the AMOS Brain:

$$\text{AUTHORITATIVE\_STATE} \longrightarrow \text{00\_ROOT\_MOC} \longrightarrow \text{Plane MOC} \longrightarrow \text{Contract} \longrightarrow \text{Detail} \longrightarrow \text{Raw Evidence}$$

* **H (High-level):** Resolve the primary functional domain and plane.
* **M (Mid-level):** Inspect the plane's MOC and Contract surface.
* **L (Low-level):** Read the minimum set of detailed notes required to satisfy the goal.
* **Raw Evidence:** Only inspect raw empirical logs or source texts when load-bearing to the decision.

---

## 7. Related Master Surfaces

- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC — Authoritative Structural Navigation]]
- [[00_ROOT/AUTHORITATIVE_STATE|AUTHORITATIVE_STATE — Active Authority Pointers]]
- [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE — Detailed MECE Model]]
- [[00_ROOT/PLANE_OWNERSHIP_MATRIX|PLANE_OWNERSHIP_MATRIX — Responsibility Mappings]]
- [[00_ROOT/FULL_BRAIN_SOURCE_MAP|FULL_BRAIN_SOURCE_MAP — Provenance Master]]
- [[00_ROOT/CONTENT_DEPTH_STANDARD|CONTENT_DEPTH_STANDARD — Artifact Quality Rules]]
- [[01_CANON/03_COGNITION_CANON/FULL_BRAIN_OS_CANON|FULL_BRAIN_OS_CANON — Canonical Specification]]
- [[11_KNOWLEDGE/AMOS_FULL_BRAIN_OS_ARCHITECTURE|AMOS_FULL_BRAIN_OS_ARCHITECTURE — Full Brain Knowledge Base]]
- [[00_ROOT/ARXIV_RSCF_KNOWLEDGE_NODE|ARXIV_RSCF_KNOWLEDGE_NODE — Arvix Research Corpus (66,026 Papers)]]

---

RSCF-NODE
node_id: amos_00_root_amos_total_architecture
node_type: architecture
path: 00_ROOT/AMOS_TOTAL_ARCHITECTURE.md
claim_class: AMOS_MODEL
rscf_state: active_specification
canonical_status: AMOS_MODEL
RSCF-RELATIONS:
- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- DERIVED_FROM: [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]]
- DERIVED_FROM: [[00_ROOT/PLANE_OWNERSHIP_MATRIX|PLANE_OWNERSHIP_MATRIX]]
- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
