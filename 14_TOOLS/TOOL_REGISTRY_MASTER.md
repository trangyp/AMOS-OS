---
title: "AMOS OS Tool Registry Master"
type: registry
aliases:
  - TOOL_REGISTRY_MASTER
  - Tool Registry Master
source: 14_TOOLS
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
conclusion_class: AMOS_MODEL
rscf:
  state: AMOS_MODEL
  claim_class: AMOS_MODEL
  provenance:
    - 14_TOOLS/14_TOOLS_MOC
    - 14_TOOLS/TOOLS_TOOL_CONTRACT
    - 14_TOOLS/SANDBOX_TOOL_EXECUTION_PROTOCOL
    - 18_SECURITY/18_SECURITY_MOC
  scope: 14_tools_registry
---

# AMOS OS Tool Registry Master

## 1. Registry boundary

`TOOL_REGISTRY_MASTER` is the active AMOS **declared tool-capability registry**. Registry presence establishes a named capability contract and maximum intended effect class. It does not by itself prove that a tool is installed, deployed, benchmarked, isolated, authorized for the current task, or safe.

```text
REGISTERED != INSTALLED
INSTALLED != AVAILABLE
AVAILABLE != AUTHORIZED
AUTHORIZED != SAFE
DECLARED_LIMIT != MEASURED_LIMIT
RECEIPT_SPECIFIED != RECEIPT_EMITTED
```

Consequential invocation remains subordinate to `03_CONTROL_PLANE` authority and freshness checks.

## 2. Effect-tier model

The tier is a maximum intended effect class, not proof of a specific sandbox technology.

```text
T0 = informational/schema only
T1 = read-only/local analysis
T2 = bounded ephemeral computation
T3 = external network/API interaction
T4 = consequential durable/external mutation
```

A tool may operate below its registered ceiling. It may not silently exceed it.

```text
CAPABILITY_CEILING != CURRENT_AUTHORITY
```

## 3. Master registered tools

| Tool ID | Entry | Tier | Declared capability | Evidence state |
| :--- | :--- | :--- | :--- | :--- |
| `amos-llm-wiki` | [[14_TOOLS/AMOS_LLM_WIKI_TOOL]] | T1 | `FS_READ_VAULT` | See tool-local evidence |
| `amos-obsidian-linking` | [[14_TOOLS/AMOS_OBSIDIAN_LINKING_PLUGINS]] | T1 | `FS_READ_VAULT \| AST_PARSE` | See tool-local evidence |
| `amos-agent-interop-compiler` | [[14_TOOLS/AMOS_AGENT_INTEROPERABILITY_COMPILER]] | T1 | `FS_READ_AGENT_METADATA \| MANIFEST_VALIDATE \| MANIFEST_COMPILE` | Executable local contract; protocol/deployment conformance not implied |
| `amos-agent-trace-audit` | [[14_TOOLS/AGENT_TRACE_OBSERVABILITY_CONTRACT]] | T1 | `TRACE_PARSE \| TRACE_VALIDATE \| MISSINGNESS_CLASSIFY \| RECEIPT_HASH` | Executable local reference + regression tests |
| `amos-wasi-micro-sandbox` | [[14_TOOLS/AMOS_SELF_HEALING_AUTONOMOUS_WASI_MICRO_SANDBOX_GUIDE]] | T2 | `WASI_EPHEMERAL \| NO_NET` | Implementation/limits require tool-local receipt |
| `amos-sandbox-execution` | [[14_TOOLS/SANDBOX_TOOL_EXECUTION_PROTOCOL]] | T2 | `BOUNDED_EXECUTION` | Backend-neutral execution ABI; isolation must be verified per backend |
| `amos-simulation-kernel` | [[14_TOOLS/SIMULATION_KERNEL_DISCRETE_SYSTEM_DYNAMICS]] | T2 | `SIMULATION_COMPUTE` | See tool-local evidence |
| `amos-github-research` | [[14_TOOLS/GITHUB_REPOSITORY_RESEARCH_ADAPTER]] | T3 | `GITHUB_REPO_DISCOVERY \| GITHUB_SOURCE_READ \| GITHUB_COMMIT_READ \| GITHUB_PR_READ` | Connector-scoped read evidence; read != write authority |
| `amos-fix-zeromq` | [[15_INTERFACES/FOREX_FIX44_ZEROMQ_SOCKET_ADAPTER]] | T3 | `NETWORK_FEED_ADAPTER` | Validate against current domain/runtime evidence before reuse |
| `amos-bci-decoder` | [[15_INTERFACES/BCI_EXPRESSION_GATEWAY_ADAPTER]] | T3 | `BCI_INPUT_ADAPTER` | Validate against current domain/runtime evidence before reuse |
| `amos-cas-epoch-engine` | [[12_STATE/DISTRIBUTED_SNAPSHOT_AND_CAS_EPOCH_ENGINE]] | T4 | `CAS_COMMIT \| EPOCH_BUMP` | Consequential; commit-time authority required |

The GitHub research adapter is read-only by registry contract. Repository mutation is a distinct T4 effect class and requires separate authority.

The interoperability compiler remains T1 while checking metadata or writing projections to stdout/ephemeral scratch. Persisting generated output into authoritative repository state is a separate write effect.

The trace auditor remains T1. It validates supplied trace artifacts but does not attach to live processes, export telemetry, or commit effects.

## 4. Tool descriptor model

The following schema is an AMOS model for normalized tool registration; it is not evidence that every registered tool uses Protocol Buffers at runtime.

```protobuf
syntax = "proto3";
package amos.tools.registry;

enum ExecutionTier {
  TIER_UNSPECIFIED = 0;
  TIER_0_INFORMATIONAL = 1;
  TIER_1_READ_ONLY = 2;
  TIER_2_BOUNDED_COMPUTE = 3;
  TIER_3_EXTERNAL_NETWORK = 4;
  TIER_4_CONSEQUENTIAL_MUTATION = 5;
}

message ToolDescriptor {
  string tool_id = 1;
  string display_name = 2;
  string version = 3;
  ExecutionTier max_effect_tier = 4;
  repeated string declared_capabilities = 5;
  string input_schema_ref = 6;
  string output_schema_ref = 7;
  string implementation_identity = 8;
}

message ToolExecutionReceipt {
  string execution_id = 1;
  string tool_id = 2;
  string implementation_identity = 3;
  string environment_identity = 4;
  string status = 5;
  string input_digest = 6;
  string output_digest = 7;
  string authority_decision_id = 8;
  string effect_state = 9;
}
```

Fields may be unavailable for a particular adapter; missing values remain explicit rather than fabricated.

## 5. Registry invariants

1. **Least privilege** — invocation must remain within the intersection of registered capability, task authority, backend capability, and policy constraints.
2. **Fail closed** — unregistered consequential effect or unresolved authority does not execute by registry implication.
3. **Read/write separation** — discovery/read capability never implies mutation authority.
4. **Projection separation** — A2A/MCP candidate manifests do not imply protocol conformance, deployed handlers, credentials, or invocation authority.
5. **Isolation evidence** — requesting a sandbox does not prove isolation; backend evidence is required.
6. **Receipt honesty** — if receipt emission, signature, environment identity, or raw outputs are unavailable, preserve `UNKNOWN/GAP`.
7. **Observability separation** — tool success telemetry does not prove semantic correctness or effect finality.
8. **Limits are evidence-bound** — memory, timeout, latency, throughput, and reliability figures require executed environment-bound measurements before being treated as facts.

## 6. Capability attenuation

For capabilities represented in one common universe `U`, the effective capability set may be modeled as:

```text
C_effective := C_registered ∩ C_authorized ∩ C_backend ∩ C_policy
```

This is a set definition. It does not claim that every AMOS host already enforces the intersection automatically.

## 7. Cross-plane bindings

- [[14_TOOLS/14_TOOLS_MOC|Master Tools MOC]]
- [[14_TOOLS/TOOLS_TOOL_CONTRACT|Tool Contract]]
- [[14_TOOLS/GITHUB_REPOSITORY_RESEARCH_ADAPTER|GitHub Research Adapter]]
- [[14_TOOLS/AMOS_AGENT_INTEROPERABILITY_COMPILER|Agent Interoperability Compiler]]
- [[14_TOOLS/AGENT_TRACE_OBSERVABILITY_CONTRACT|Agent Trace Observability Contract]]
- [[14_TOOLS/SANDBOX_TOOL_EXECUTION_PROTOCOL|Sandbox Tool Execution Protocol]]
- [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|Control Plane]]
- [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|Observability]]
- [[18_SECURITY/18_SECURITY_MOC|Security]]
