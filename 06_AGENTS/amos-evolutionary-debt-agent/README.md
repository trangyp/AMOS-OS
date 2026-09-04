---
title: AMOS Evolutionary Debt Agent
type: agent_specification
status: ACTIVE
conclusion_class: DERIVED
origin_architect: Trang Phan
governed_by: [[06_AGENTS/AGENT_ROLE_REGISTRY.md|AGENT_ROLE_REGISTRY]]
role_category: ASSURANCE_LIFECYCLE
rscf-state: source-claim
---

# AMOS Evolutionary Debt Agent (`amos-evolutionary-debt-agent`)

## Overview
Identifies structural debt, deprecated syntax, legacy stubs, and coordinates archive migrations.

## Governing Contracts & Axioms
- Governed under the canonical [[AGENTS.md|AMOS Agent Contract]] lineage boundary (v3.0 -> v4.4).
- Adheres to the central axiom: `CAPABILITY != AUTHORITY`, `DOCUMENTED != IMPLEMENTED`.
- Role Category: **ASSURANCE_LIFECYCLE** per [[06_AGENTS/AGENT_ROLE_REGISTRY.md|Agent Role Registry]].

## Primary Invariants
> [!IMPORTANT]
> Archive-first destruction, zero data loss, provenance ledger recording for all deprecations.

## Operational Boundaries & Tools
- Primary Planes: [[24_ARCHIVE/24_ARCHIVE_MOC]], [[20_OPERATIONS/20_OPERATIONS_MOC]], [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC]]
- Telemetry & Observability: [[17_OBSERVABILITY/17_OBSERVABILITY_MOC.md|17_OBSERVABILITY]]
- Provenance Receipts: [[03_CONTROL_PLANE/05_PROVENANCE/05_PROVENANCE_MOC.md|05_PROVENANCE]]

## Interface Contract
```protobuf
syntax = "proto3";
package amos.agents.amos_evolutionary_debt_agent;

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

This README provides the human-facing entry point for the `amos-evolutionary-debt-agent` plane. It explains the plane's role in AMOS OS, its boundaries, and how to navigate its contents.

## Scope

This plane covers `amos-evolutionary-debt-agent` concerns within the AMOS OS architecture. It is mutually exclusive with other numbered planes and collectively exhaustive with respect to the system's functional decomposition.

**In scope:** contracts, MOCs, specifications, and operational notes under this plane.
**Out of scope:** implementation details of sibling planes; hardware abstraction in `02_KERNEL`; user interface rendering in `15_INTERFACES`.

## Invariants

| ID | Invariant |
|----|-----------|
| AMOS-EVOLUTIONARY-DEBT-AGENT_README_INV_01 | This README remains the primary human-facing entry point for the plane. |
| AMOS-EVOLUTIONARY-DEBT-AGENT_README_INV_02 | All canonical files in this plane are reachable from the plane MOC. |
| AMOS-EVOLUTIONARY-DEBT-AGENT_README_INV_03 | No plane-specific claim is promoted to `01_CANON` without authority. |

## Cross References
- [[amos-evolutionary-debt-agent/amos-evolutionary-debt-agent_MOC|amos-evolutionary-debt-agent_MOC]]
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- [[_MOC|Root _MOC]]
- [[AGENTS|AGENTS.md]]
