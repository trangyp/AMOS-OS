---
title: AMOS API Gateway Agent
type: agent_specification
status: ACTIVE
conclusion_class: DERIVED
origin_architect: Trang Phan
governed_by: [[06_AGENTS/AGENT_ROLE_REGISTRY.md|AGENT_ROLE_REGISTRY]]
role_category: ADAPTER_INTERFACE
rscf-state: source-claim
---

# AMOS API Gateway Agent (`amos-api-gateway-agent`)

## Overview
Manages incoming and outgoing IPC/HTTP/gRPC interfaces, rate limiting, and schema translation.

## Governing Contracts & Axioms
- Governed under the canonical [[AGENTS.md|AMOS Agent Contract]] lineage boundary (v3.0 -> v4.4).
- Adheres to the central axiom: `CAPABILITY != AUTHORITY`, `DOCUMENTED != IMPLEMENTED`.
- Role Category: **ADAPTER_INTERFACE** per [[06_AGENTS/AGENT_ROLE_REGISTRY.md|Agent Role Registry]].

## Primary Invariants
> [!IMPORTANT]
> mTLS verification, token bucket rate enforcement, strict payload schema validation.

## Operational Boundaries & Tools
- Primary Planes: [[15_INTERFACES/15_INTERFACES_MOC]], [[09_PROTOCOLS/09_PROTOCOLS_MOC]], [[18_SECURITY/18_SECURITY_MOC]]
- Telemetry & Observability: [[17_OBSERVABILITY/17_OBSERVABILITY_MOC.md|17_OBSERVABILITY]]
- Provenance Receipts: [[03_CONTROL_PLANE/05_PROVENANCE/05_PROVENANCE_MOC.md|05_PROVENANCE]]

## Interface Contract
```protobuf
syntax = "proto3";
package amos.agents.amos_api_gateway_agent;

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

This README provides the human-facing entry point for the `amos-api-gateway-agent` plane. It explains the plane's role in AMOS OS, its boundaries, and how to navigate its contents.

## Scope

This plane covers `amos-api-gateway-agent` concerns within the AMOS OS architecture. It is mutually exclusive with other numbered planes and collectively exhaustive with respect to the system's functional decomposition.

**In scope:** contracts, MOCs, specifications, and operational notes under this plane.
**Out of scope:** implementation details of sibling planes; hardware abstraction in `02_KERNEL`; user interface rendering in `15_INTERFACES`.

## Invariants

| ID | Invariant |
|----|-----------|
| AMOS-API-GATEWAY-AGENT_README_INV_01 | This README remains the primary human-facing entry point for the plane. |
| AMOS-API-GATEWAY-AGENT_README_INV_02 | All canonical files in this plane are reachable from the plane MOC. |
| AMOS-API-GATEWAY-AGENT_README_INV_03 | No plane-specific claim is promoted to `01_CANON` without authority. |

## Cross References
- [[amos-api-gateway-agent/amos-api-gateway-agent_MOC|amos-api-gateway-agent_MOC]]
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- [[_MOC|Root _MOC]]
- [[AGENTS|AGENTS.md]]
