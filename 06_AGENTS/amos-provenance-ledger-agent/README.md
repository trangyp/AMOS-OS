---
title: AMOS Provenance Ledger Agent
type: agent_specification
status: ACTIVE
conclusion_class: DERIVED
origin_architect: Trang Phan
governed_by: [[06_AGENTS/AGENT_ROLE_REGISTRY.md|AGENT_ROLE_REGISTRY]]
role_category: CORE_GOVERNANCE
rscf-state: source-claim
---

# AMOS Provenance Ledger Agent (`amos-provenance-ledger-agent`)

## Overview
Maintains tamper-evident cryptographic provenance chains, RSCF receipts, and audit ledgers.

## Governing Contracts & Axioms
- Governed under the canonical [[AGENTS.md|AMOS Agent Contract]] lineage boundary (v3.0 -> v4.4).
- Adheres to the central axiom: `CAPABILITY != AUTHORITY`, `DOCUMENTED != IMPLEMENTED`.
- Role Category: **CORE_GOVERNANCE** per [[06_AGENTS/AGENT_ROLE_REGISTRY.md|Agent Role Registry]].

## Primary Invariants
> [!IMPORTANT]
> Immutable append-only receipt hashes, Merkle root verification, CAS lineage integrity.

## Operational Boundaries & Tools
- Primary Planes: [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC]], [[16_SCHEMAS/16_SCHEMAS_MOC]], [[20_OPERATIONS/20_OPERATIONS_MOC]]
- Telemetry & Observability: [[17_OBSERVABILITY/17_OBSERVABILITY_MOC.md|17_OBSERVABILITY]]
- Provenance Receipts: [[03_CONTROL_PLANE/05_PROVENANCE/05_PROVENANCE_MOC.md|05_PROVENANCE]]

## Interface Contract
```protobuf
syntax = "proto3";
package amos.agents.amos_provenance_ledger_agent;

message AgentTaskRequest {
  string task_id = 1;
  string session_id = 2;
  string target_uri = 3;
  bytes input_tensor = 4;
  map<string, string> context_metadata = 5;
}

message AgentTaskResponse {
  string task_id = 1;
  enum Status {
    SUCCESS = 0;
    VERIFICATION_FAILED = 1;
    INVARIANT_BREACH = 2;
    TIMEOUT = 3;
  }
  Status status = 2;
  bytes result_payload = 3;
  string receipt_hash = 4;
  double confidence_score = 5;
}
```

## Navigation
- Return to: [[06_AGENTS/06_AGENTS_MOC.md|06_AGENTS MOC]], [[00_ROOT/00_ROOT_MOC.md|Root MOC]].

## Purpose

This README provides the human-facing entry point for the `amos-provenance-ledger-agent` plane. It explains the plane's role in AMOS OS, its boundaries, and how to navigate its contents.

## Scope

This plane covers `amos-provenance-ledger-agent` concerns within the AMOS OS architecture. It is mutually exclusive with other numbered planes and collectively exhaustive with respect to the system's functional decomposition.

**In scope:** contracts, MOCs, specifications, and operational notes under this plane.
**Out of scope:** implementation details of sibling planes; hardware abstraction in `02_KERNEL`; user interface rendering in `15_INTERFACES`.

## Invariants

| ID | Invariant |
|----|-----------|
| AMOS-PROVENANCE-LEDGER-AGENT_README_INV_01 | This README remains the primary human-facing entry point for the plane. |
| AMOS-PROVENANCE-LEDGER-AGENT_README_INV_02 | All canonical files in this plane are reachable from the plane MOC. |
| AMOS-PROVENANCE-LEDGER-AGENT_README_INV_03 | No plane-specific claim is promoted to `01_CANON` without authority. |

## Cross References
- [[amos-provenance-ledger-agent/amos-provenance-ledger-agent_MOC|amos-provenance-ledger-agent_MOC]]
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- [[_MOC|Root _MOC]]
- [[AGENTS|AGENTS.md]]
