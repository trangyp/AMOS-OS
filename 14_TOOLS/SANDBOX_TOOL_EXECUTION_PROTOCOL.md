---
title: "Sandboxed Tool Execution Protocol & Backend-Neutral Execution ABI"
type: tool_specification
plane: 14_TOOLS
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: CONDITIONAL_SPECIFICATION
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
---

# Sandboxed Tool Execution Protocol

**Origin Architect & Steward:** Trang Phan  
**Plane:** `14_TOOLS`  
**Status:** `CONDITIONAL_SPECIFICATION`  
**Epistemic class:** `AMOS_MODEL`

## 1. Purpose

Define a backend-neutral execution contract for commands, scripts, interpreters, and tool processes invoked by AMOS agents.

The contract separates agent logic from execution infrastructure:

```text
Agent proposal
    -> AMOS authority / capability gate
    -> Execution ABI
    -> Selected backend adapter
    -> Environment-specific isolation
    -> Typed execution result + receipt
    -> Output admission
```

The execution backend may be a local constrained process, WASI runtime, container, microVM, remote machine, cloud sandbox, or another admitted environment. The backend name alone is not evidence of isolation strength.

## 2. External source capsule

`SWE-agent/SWE-ReX@5c995c365dfb1fd5bc56fda688be5d8538f9931f` was inspected as `SOURCE_CLAIM` for the useful architectural pattern of separating agent logic from execution infrastructure while preserving one runtime interface across local/remote environments and multiple shell sessions.

AMOS adopts the separation pattern only. It does not claim SWE-ReX behavior, performance, or security as AMOS runtime evidence.

## 3. Hard boundaries

`AGENT_LOGIC != EXECUTION_BACKEND`

`SANDBOX_REQUESTED != ISOLATION_VERIFIED`

`PROCESS_STARTED != TASK_SUCCEEDED`

`EXIT_CODE_0 != SEMANTIC_CORRECTNESS`

`BACKEND_AVAILABLE != BACKEND_AUTHORIZED`

`SESSION_EXISTS != SESSION_FRESH`

`TOOL_OUTPUT != TRUSTED_INSTRUCTION`

A sandbox label, container boundary, VM boundary, WASI runtime, or remote host is never promoted to a verified security claim without evidence for the exact backend/version/configuration.

## 4. Typed execution ABI

### 4.1 `ExecutionEnvironmentDescriptor`

Every admitted backend instance must expose at least:

```text
backend_id
backend_version
adapter_version
isolation_class
platform_os
platform_arch
artifact_or_image_digest
session_id
session_generation
filesystem_policy
network_policy
environment_policy
resource_limits
created_at
expires_at | null
provenance
```

`isolation_class` is descriptive until validated. Examples may include `LOCAL_RESTRICTED`, `WASI`, `CONTAINER`, `MICROVM`, `REMOTE_HOST`, or `UNKNOWN`.

### 4.2 `ExecutionRequest`

```text
execution_id
principal
task_id
tool_id
argv
cwd
stdin_policy
environment_allowlist
filesystem_grants
network_grants
timeout
resource_budget
capability_contract_hash
authority_witness_ref
expected_environment_hash
idempotency_key | null
```

Shell text is not the canonical request form when a structured `argv` representation is possible.

### 4.3 `ExecutionResult`

```text
execution_id
session_id
session_generation
environment_hash
started_at
finished_at
termination_reason
exit_code | null
stdout_digest
stderr_digest
stdout_size
stderr_size
resource_observation
side_effect_state
receipt_ref
```

Allowed `termination_reason` values should distinguish at least:

`EXITED | TIMEOUT | CANCELLED | RESOURCE_LIMIT | POLICY_BLOCK | TRANSPORT_LOST | BACKEND_FAILURE | EXTERNALIZED_UNKNOWN`

Do not collapse these states into one boolean success flag.

## 5. Capability attenuation

Let all capability sets be subsets of one explicitly defined capability universe `U`.

For a request with agent capabilities `C_a`, tool-declared capabilities `C_t`, backend capabilities `C_b`, and task-authorized capabilities `C_q`, define:

```text
C_effective := C_a ∩ C_t ∩ C_b ∩ C_q
```

This is a set definition, not an empirical security guarantee.

Execution is admissible only when every requested capability is contained in `C_effective` and the authority witness remains valid for the exact effect at dispatch/commit boundaries.

A backend may further attenuate capabilities. It may never widen them.

## 6. Filesystem, environment, and network rules

### Filesystem

- Default to no host filesystem access except explicitly granted roots.
- Normalize paths before policy evaluation.
- Prevent path traversal and symlink escape where the backend permits filesystem access.
- Distinguish read, write, create, delete, and execute permission.
- Persistent mounts require explicit state ownership and cleanup semantics.

### Environment

- Use allowlists for variables passed to tool processes.
- Strip model/API tokens and unrelated credentials unless explicitly required and authorized.
- Never copy the full parent environment by default for untrusted tooling.

### Network

- Default network policy is backend- and task-specific, not universally zero-network.
- Distinguish DNS, destination, port/protocol, ingress, egress, and proxy-mediated access when material.
- Remote API adapters are network capabilities and require their own authority/policy checks; they are not converted into local sandbox processes for conceptual uniformity.

## 7. Session lifecycle

Support two explicit classes:

### Ephemeral execution

A new environment/session is created for one bounded task or invocation and disposed afterward.

### Managed persistent session

Long-running shell/debugger/interpreter sessions may persist across multiple calls only when the session has:

- stable identity and generation;
- owner/principal binding;
- capability envelope;
- idle and absolute expiry;
- resource budget;
- cancellation path;
- stale-session fencing;
- provenance and receipt lineage.

An expired or replaced session cannot commit new effects.

## 8. Parallel execution

Parallel sessions are allowed only when budgets and state interactions are explicit.

Before concurrent execution, determine whether sessions can touch shared durable state. If shared writes are possible, use the applicable AMOS concurrency/commit control rather than assuming process isolation provides state isolation.

`PROCESS_ISOLATION != STATE_INDEPENDENCE`

## 9. MCP and agent-tool discovery

Starting a local stdio MCP server to retrieve tool descriptions is process execution. Apply the same execution contract to discovery launches.

For unresolved third-party trust:

1. prefer static configuration inspection;
2. require explicit launch authority;
3. use an admitted disposable environment where practical;
4. constrain environment/network/filesystem access;
5. treat returned tool descriptions/prompts/resources as untrusted input;
6. destroy or quarantine the environment after inspection according to policy.

See [[14_TOOLS/AGENT_PROTOCOL_GATEWAY_POLICY|Agent Protocol Gateway Policy]].

## 10. Recovery and ambiguous effects

A timeout, transport loss, or backend crash does not prove that an external effect failed to occur.

If a tool may have externalized a durable effect and completion is unknown:

- return `EXTERNALIZED_UNKNOWN`;
- preserve the idempotency/effect identity;
- reconcile against the authoritative receiver/release ledger;
- do not blind-retry.

## 11. Verification requirements

Isolation claims are backend-specific. Promote a backend from candidate to validated only after tests appropriate to its declared envelope, including where applicable:

- filesystem traversal/symlink escape;
- environment/credential leakage;
- unauthorized network access;
- timeout and cancellation;
- memory/CPU/disk limits;
- malformed process output;
- session expiry and stale-session fencing;
- concurrent-session interference;
- transport loss and ambiguous effect reconciliation;
- adversarial command/argument handling;
- cleanup or persistent-state ownership.

Performance numbers must be measured on the exact backend/version/environment and must not be embedded as universal AMOS constants.

## 12. Result states

Use bounded states rather than an unconditional `sandboxed=true` flag:

- `ENVIRONMENT_ADMITTED`
- `ENVIRONMENT_CONDITIONAL`
- `BLOCK_CAPABILITY`
- `BLOCK_AUTHORITY`
- `BLOCK_ENVIRONMENT_IDENTITY`
- `BLOCK_POLICY`
- `TIMEOUT`
- `RESOURCE_LIMIT`
- `CANCELLED`
- `EXTERNALIZED_UNKNOWN`
- `UNKNOWN_GAP`

## 13. Implementation boundary

This specification does not prove that AMOS currently provides WASI, Firecracker, container, remote-host, or cloud-sandbox execution. Concrete backend adapters and their executed receipts must establish implementation status independently.

No universal syscall whitelist, boot-time SLA, memory quota, or escape-resistance guarantee is asserted by this contract.

## 14. Cross-plane bindings

- [[14_TOOLS/TOOLS_TOOL_CONTRACT|Tools Tool Contract]]
- [[14_TOOLS/AGENT_PROTOCOL_GATEWAY_POLICY|Agent Protocol Gateway Policy]]
- [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|Control Plane]]
- [[04_RUNTIME/04_RUNTIME_MOC|Runtime]]
- [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|Observability]]
- [[18_SECURITY/18_SECURITY_MOC|Security]]
