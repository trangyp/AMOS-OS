---
title: 14_TOOLS — Host Capabilities & Sandboxed Adapters
type: architecture_specification
source: 14_TOOLS
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE
    - 18_SECURITY/SECURITY_SECURITY_CONTRACT
  scope: tools_architecture
tags:
  - amos-os
  - tools
  - sandboxing
  - capability-adapters
---

# 14_TOOLS — Master Tool Architecture

## 1. Plane Purpose

The `14_TOOLS` plane defines external capability adapters, CLI wrappers, web connectors, and filesystem utilities available to AMOS agents under strict security governance.

This plane is the boundary between the AMOS cognitive organism and the external world. Every tool invocation passes through capability-scoped sandboxing, telemetry emission, and least-privilege enforcement before reaching the host system.

```text
TOOL_ACCESS != TOOL_PERMISSION
CAPABILITY != AUTHORITY
INVOCATION != SUCCESS
DOCUMENTED != IMPLEMENTED
```

---

## 2. Architecture Overview

The tools architecture is organized around a five-tier sandbox hierarchy, a formal admission criteria set, and a master tool registry. Each tool is wrapped in an adapter that enforces parameter validation, timeout bounds, failure mode containment, and telemetry emission before any host interaction occurs.

---

## 3. Key Components

### 3.1 Tool Sandbox Tiers

```text
TIER 0: PURE INFERENCE (No external tool access)
TIER 1: READ-ONLY OBSERVATION (File viewing, search, read-only API query)
TIER 2: BOUNDED MUTATION (Workspace file editing, sandboxed Python scripts)
TIER 3: SYSTEM CONVENTIONAL (Package installations, external API mutations)
TIER 4: HIGH-STAKES GOVERNANCE (Canon amendment, destructive deletion, credentials)
```

Each tier requires progressively stronger authorization:
- Tiers 0-1: Agent-level capability tokens (D0-D1).
- Tier 2: Orchestrator-signed capability token (D3).
- Tier 3: Orchestrator-signed token with security plane consultation.
- Tier 4: Origin Architect explicit signature (D4).

### 3.2 Tool Admission Criteria

Before any tool is registered in `TOOL_REGISTRY_MASTER.md`:
1. It must have a formal JSON schema defining parameters and return types.
2. It must have a bounded failure mode and timeout specification.
3. It must emit full execution telemetry to `17_OBSERVABILITY`.
4. It must enforce least-privilege scoping.
5. It must pass security review by the Security Council governance forum.

### 3.3 Tool Registry

The `TOOL_REGISTRY_MASTER.md` maintains the canonical list of all admitted tools with:
- Tool identifier and version hash.
- Sandbox tier assignment.
- Capability scope (filesystem paths, network endpoints, system calls).
- Adapter interface schema.
- Telemetry emission contract.

---

## 4. Navigation

- **Tool Registry:** [[14_TOOLS/TOOL_REGISTRY_MASTER|TOOL_REGISTRY_MASTER]]
- **Tools MOC:** [[14_TOOLS/14_TOOLS_MOC|14_TOOLS_MOC]]
- **Security Plane:** [[18_SECURITY/18_SECURITY_MOC|18_SECURITY_MOC]]
- **Observability:** [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]]
- **Runtime (Sandboxing):** [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME_MOC]]
- **Cognitive Organism (Action Organ):** [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]]
- **Root Architecture:** [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]]

---

## 5. Status & Gaps

- **Status:** `ACTIVE_SPECIFICATION` — sandbox tier hierarchy and admission criteria are documented.
- **Registry Completeness:** The tool registry master is specified but the full inventory of admitted tools with JSON schemas is not yet complete.
- **WASI Sandbox Integration:** Tier 2 sandboxed execution is specified to use WASI-based microVMs. Integration with the runtime plane's sandbox environment is `DOCUMENTED != IMPLEMENTED`.
- **Telemetry Pipeline:** Tool telemetry emission to `17_OBSERVABILITY` is specified. The actual telemetry pipeline with OpenTelemetry-compatible trace spans is not yet operationalized.
- **Tier 4 Enforcement:** High-stakes governance tools require D4 (Origin Architect) signatures. The cryptographic signature verification pipeline for D4 tool authorization is specified but not yet integrated with the control plane.
