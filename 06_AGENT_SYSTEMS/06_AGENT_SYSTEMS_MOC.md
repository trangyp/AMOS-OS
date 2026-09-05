---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 06 Agent Systems/06 Agent Systems Moc
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---

# 06 Agent Systems — Map of Content

> [!ABSTRACT] Agent Systems Plane Executive Summary
> The **Agent Systems Plane** (`06_AGENT_SYSTEMS`) owns agent fabrication, delegation lifecycle, agency-consequence modeling, and agent-economy governance. It defines the construction contract for agents, the lifecycle through which agents are proposed, admitted, activated, delegated, revoked, and archived, and the constitutional governance that bounds agent economies.
> Core invariant:
> $$\text{CAPABILITY} \neq \text{AUTHORITY} \neq \text{AGENCY} \neq \text{CONSEQUENCE}$$

---

## 1. Core Artifacts

| Artifact | Description |
|---|---|
| [[06_AGENT_SYSTEMS/AGENT_SCHEMA\|Agent Schema]] | Agent construction contract: IDENTITY + OBJECTIVE + CAPABILITIES + CONSTRAINTS |
| [[06_AGENT_SYSTEMS/DELEGATION_LIFECYCLE\|Delegation Lifecycle]] | Lifecycle: PROPOSED → ADMITTED → ACTIVE → DELEGATING → REVOKED → ARCHIVED |
| [[06_AGENT_SYSTEMS/AGENCY_CONSEQUENCE_TENSOR\|Agency Consequence Tensor]] | 9-axis tensor mapping agency decisions to consequence dimensions |
| [[06_AGENT_SYSTEMS/AGENT_ECONOMY_GOVERNANCE\|Agent Economy Governance]] | Constitutional governance for agent economies and multi-agent coordination |

---

## 2. Inbound & Outbound Interfaces

- **Control Plane Gates:** [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|Control Plane Contract]]
- **Runtime Sandbox:** [[04_RUNTIME/RUNTIME_RUNTIME_CONTRACT|Runtime Contract]]
- **Security Boundary:** [[18_SECURITY/SECURITY_SECURITY_CONTRACT|Security Contract]]
- **Lifecycle Governance:** [[18_LIFECYCLE/PROMOTION_GATES|Promotion Gates]]
- **Protocols:** [[23_PROTOCOLS/A2A_PROTOCOL_SPEC|A2A Protocol]]

---

## 3. Key Invariants

1. Every agent carries a typed schema binding (IDENTITY, OBJECTIVE, CAPABILITIES, CONSTRAINTS).
2. Delegation is temporal, revocable, and attenuation-bound: `ChildScope(t) ⊆ ParentScope(t)`.
3. Agency consequences are measured across 9 axes; no single axis may override non-compensatory refusals.
4. Agent economies operate under constitutional governance; no agent may self-promote authority.

---

## 4. Cross-References

- [[00_ROOT/00_ROOT_MOC|Root MOC]]
- [[AMOS_HOME|AMOS Home]]
- [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|Law Hierarchy]]
- [[06_AGENTS/06_AGENTS_MOC|06 Agents MOC (legacy)]]

---

## 5. Gaps

- Agent economy runtime enforcement: UNKNOWN/GAP
- A2A protocol binding to agent schema: CONDITIONAL (specification only)
- Agency consequence tensor empirical validation: NOT_ESTABLISHED

---

## 6. Ingestion Rule

This MOC is a navigation artifact. Content files in this directory are AMOS_MODEL specifications unless promoted via the promotion-gate checklist. Do not infer implementation from specification.

---

> **RSCF-NODE** | state: OBSERVATION | claim_class: OBSERVATION | provenance: amos_architecture_2026-09-04 | scope: AMOS_general | confidence_ceiling: source_supported | provenance_independence: NOT_ESTABLISHED
