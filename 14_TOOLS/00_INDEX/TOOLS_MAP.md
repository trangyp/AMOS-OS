---
title: TOOLS_MAP (Alias)
type: redirect
target: "[[14_TOOLS/00_INDEX/TOOL_MAP]]"
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_REDIRECT
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: active__AMOS_OS
---
# TOOL MAP

**Path:** `14_TOOLS/00_INDEX/TOOLS_MAP.md`
**Type:** Map of Content

## Overview

The `TOOLS_MAP` is the canonical navigation index for the `14_TOOLS` plane of the AMOS Full Brain OS. It provides fast navigation across tool contracts, policies, operational notes, and sub-MOCs without loading raw evidence. The tools plane governs all external and internal tools that AMOS agents and subsystems may use, ensuring that every tool is registered, classified, evaluated, and maintained through a formal lifecycle.

### Purpose

This MOC indexes the `00_INDEX` control surface of the AMOS Full Brain OS. It provides fast navigation across contracts, policies, operational notes, and sub-MOCs without loading raw evidence.

### MECE scope

- This MOC owns navigation links for files in its directory.
- It does not own implementation, runtime authority, or canon promotion.
- Sub-MOCs recursively own narrower scopes.

### Invariants

- All listed files belong to the same directory scope.
- No file is promoted to canon status merely by being listed.
- Parent/child MOC links must remain acyclic.

---

## Taxonomy

### Tools Classification

The tools plane partitions all tools into five mutually exclusive categories:

| Category | Description | Examples | AMOS Application |
| :--- | :--- | :--- | :--- |
| **Development** | Tools for building, testing, and deploying AMOS components | Compilers, linters, test runners, build systems | Skill development, agent creation, workflow validation |
| **Operations** | Tools for running, monitoring, and maintaining AMOS systems | Deployment managers, monitoring dashboards, log aggregators | Runtime monitoring, state management, observability |
| **Research** | Tools for knowledge acquisition, literature review, and experimentation | Search engines, paper databases, experiment frameworks | Knowledge plane ingestion, canon validation, hypothesis testing |
| **Analysis** | Tools for data processing, statistical analysis, and visualization | Data pipelines, statistical packages, graphing tools | Telemetry analysis, UBI score computation, incident analysis |
| **Communication** | Tools for inter-agent, human-agent, and external communication | Message queues, API gateways, notification systems | Agent coordination, human interaction engine, external interfaces |

### Tools Registry

The tools registry is the authoritative catalog of all tools approved for use within AMOS. Each entry contains:

- **Tool ID** — unique identifier within the tools plane.
- **Name and version** — tool name and semantic version.
- **Category** — one of the five classification categories above.
- **Capability envelope** — what the tool can do (read/write/execute boundaries).
- **Tier** — Tier 1 (sandboxed, no external I/O), Tier 2 (sandboxed with limited external I/O), Tier 3 (unsandboxed, requires explicit authorization).
- **Owning domain** — the AMOS domain that governs this tool's usage.
- **Status** — `EVALUATE`, `APPROVED`, `DEPLOYED`, `MAINTAINED`, `DEPRECATED`, or `RETIRED`.
- **Provenance** — origin, approval record, and version history.

### Sub-MOCs and Indices

- [[14_TOOLS/00_INDEX/TOOL_MAP.md|TOOL MAP]] — Navigation map for the `14_TOOLS/00_INDEX` segment of the Tools plane.

### Contracts

- [[14_TOOLS/00_INDEX/INDEX_TOOLS_TOOL_CONTRACT.md|INDEX TOOLS TOOL CONTRACT]] — This index resolves by basename within its own directory. Cross-plane resolution goes through 00_ROOT/00_HOME and 00_ROOT/AMOS_RSCF_NODES.

### Readmes and Guides

- [[14_TOOLS/00_INDEX/INDEX_TOOLS_README.md|INDEX TOOLS README]] — This index resolves by basename within its own directory. Cross-plane resolution goes through 00_ROOT/00_HOME and 00_ROOT/AMOS_RSCF_NODES.

### Tools-to-Skill Mapping

Each tool in the registry maps to one or more skills in the [[07_SKILLS/07_SKILLS_MOC|Skills]] plane. The mapping is bidirectional:

- **Skill → Tool:** Each skill declares the tools it requires in its `SKILL.md` frontmatter (`required_tools` field).
- **Tool → Skill:** The tools registry records which skills depend on each tool, enabling impact analysis when a tool is deprecated or retired.

This mapping ensures that tool lifecycle changes (deprecation, retirement, version upgrades) are propagated to all dependent skills for validation.

### Tools Lifecycle

Every tool progresses through a five-stage lifecycle:

| Stage | Entry Criteria | Exit Criteria | Governance |
| :--- | :--- | :--- | :--- |
| **1. Evaluate** | Tool proposed with capability description and use case | Security review, capability assessment, and tier classification complete | Tools plane steward review |
| **2. Approve** | Evaluation passed, capability envelope defined, tier assigned | Contract signed, provenance recorded, tool ID assigned | Capability-bound governance kernel authorization |
| **3. Deploy** | Approval complete, integration tests passed | Tool is live and available to authorized skills and agents | Control plane commit gate |
| **4. Maintain** | Tool is in active use | Version upgrades, security patches, capability adjustments | Periodic review by tools plane steward |
| **5. Retire** | Tool is deprecated or superseded | All dependent skills notified and migrated, tool removed from active registry | Archive-first; provenance preserved in [[24_ARCHIVE/24_ARCHIVE_MOC|24_ARCHIVE]] |

Lifecycle transitions are atomic, logged with BLAKE3 receipts, and persisted in the [[12_STATE/12_STATE_MOC|State Plane]]. A tool cannot skip stages — retirement requires explicit deprecation first.

### Gaps

- This MOC reflects the current file inventory; missing `SKILL.md`, `CONTRACT.md`, or `README.md` files in `00_INDEX` are recorded as `UNKNOWN/GAP` unless a governing artifact exists.

---

## AMOS Integration

The tools plane is the canonical source of truth for what tools exist, what they can do, and who is allowed to use them. It integrates with:

- **Skills plane** ([[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]): Skills declare required tools; the tools registry validates availability and tier compatibility.
- **Agents plane** ([[06_AGENTS/AGENT_ROLE_REGISTRY|AGENT_ROLE_REGISTRY]]): Agent roles are constrained to use only tools within their capability envelope.
- **Runtime** ([[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME_MOC]]): The runtime enforces tool tier restrictions at execution time — Tier 3 tools require explicit per-execution authorization.
- **Control Plane** ([[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]): Tool deployment and retirement require control plane commit gates.
- **Domains** ([[21_DOMAINS/21_DOMAINS_MOC|21_DOMAINS_MOC]]): Each tool is owned by a domain, which governs its usage policies and capability envelope.

---

## Related

- **Parent MOC:** [[14_TOOLS/14_TOOLS_MOC|14_TOOLS_MOC]]
- **AMOS Home:** [[00_ROOT/00_HOME|00_HOME]]
- **RSCF Registry:** [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] — skills plane (tools-to-skill mapping)
- [[06_AGENTS/AGENT_ROLE_REGISTRY|AGENT_ROLE_REGISTRY]] — agent tool capability envelopes
- [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME_MOC]] — runtime tool tier enforcement
- [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] — tool deployment commit gates
- [[21_DOMAINS/21_DOMAINS_MOC|21_DOMAINS_MOC]] — domain-owned tool governance
- [[12_STATE/12_STATE_MOC|12_STATE_MOC]] — tool lifecycle receipt persistence
- [[24_ARCHIVE/24_ARCHIVE_MOC|24_ARCHIVE_MOC]] — retired tool archival
