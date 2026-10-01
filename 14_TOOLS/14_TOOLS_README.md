---
title: "14 Tools — README"
type: readme
source: 14_TOOLS
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE
conclusion_class: AMOS_MODEL
epistemic_class: AMOS_MODEL
---

# 14 Tools — README

## 1. Role

The Tools Plane represents deterministic executors and external capability transports: filesystem, database, browser, search, compiler, calculator, API, connector, MCP server, and runtime executor surfaces.

Tools execute bounded operations. They do not decide their own authority.

```text
TOOL_AVAILABLE != TOOL_AUTHORIZED
TOOL_DISCOVERED != TOOL_SELECTED
TOOL_SELECTED != TOOL_INVOKED
TOOL_INVOKED != TOOL_SUCCEEDED
TOOL_SUCCEEDED != OUTPUT_VERIFIED
CREDENTIAL != AMOS_AUTHORITY
```

## 2. Tool categories

| Category | Description | Examples |
| --- | --- | --- |
| Storage | Filesystem/database operations | file read/write, SQL, blob storage |
| Retrieval | Search/lookup | code search, vector search, web retrieval |
| Computation | Deterministic or bounded computation | calculator, solver, compiler |
| Communication | Network/message transport | HTTP, queue, RPC |
| Transformation | Parsing/serialization/conversion | JSON, document conversion |
| Verification | Testing/static/dynamic checks | schema validator, linter, test runner |
| Integration | External service connectors | GitHub, calendar, email |
| Tool protocol | Capability discovery/invocation transport | MCP server/client |

A single provider may expose tools across multiple categories/effect classes. Do not authorize the provider as one blanket capability when finer partitioning exists.

## 3. Capability/authority pipeline

```text
AGENT/WORKFLOW REQUEST
-> TOOL DISCOVERY
-> NORMALIZE TOOL DESCRIPTOR
-> RESOLVE AMOS CAPABILITY
-> RESOLVE PRINCIPAL/CREDENTIAL CONTEXT
-> RESOLVE AMOS AUTHORITY
-> VALIDATE BUDGET + INPUT PROVENANCE
-> EXECUTE
-> CLASSIFY OUTPUT/EFFECT
-> OBSERVE
-> COMMIT/RECONCILE WHEN CONSEQUENTIAL
```

## 4. Credentials versus authority

External systems may use reusable credentials such as:

```text
OAuth access/session token
GitHub App installation token
fine-grained PAT
API key
service identity
```

Those credentials establish an external principal and upper-bound service permissions. They do **not** constitute AMOS task/effect authority.

Conceptually:

```text
ExternalCredentialScope
  intersection
AMOSCapabilityScope
  intersection
FreshAMOSAuthority
  -> EligibleToolInvocation
```

For consequential effects, AMOS authority should bind the operation/effect and be revalidated at commit. The underlying provider credential need not be single-use.

## 5. MCP/tool-server boundary

MCP-like servers publish typed tool/context capabilities. AMOS treats them as transport/providers:

```text
ToolServer -> ToolDescriptors
```

not:

```text
ToolServer -> Authority
```

For each discovered tool normalize:

- provider identity/version;
- upstream tool name;
- input/output schema identity;
- effect class;
- data/sensitivity scope;
- principal/credential context;
- provenance requirements;
- AMOS capability mapping;
- authority requirements.

Unknown effect class fails closed before mutation.

## 6. GitHub MCP

The governed candidate adapter is:

`[[14_TOOLS/GITHUB_MCP_ADAPTER|GITHUB_MCP_ADAPTER]]`

It separates GitHub repository reads, collaboration reads, CI/security reads, collaboration writes, repository writes, and merge/release effects instead of exposing one undifferentiated `github` permission.

Its upstream source identity is pinned in `11_KNOWLEDGE/EXTERNAL_AGENT_SOURCE_REGISTRY.json`.

## 7. Tool lifecycle

Track independent state dimensions rather than one convenience label:

```text
declaration
implementation
availability
validation
governance
revocation
```

Typical operational lifecycle may include:

```text
DECLARED -> AVAILABLE -> ACTIVE -> DEGRADED/THROTTLED -> DEPRECATED -> RETIRED
```

But a tool can be implemented and available while still unvalidated or unauthorized.

## 8. Effect classes

At minimum distinguish:

```text
T0 / INFORMATIONAL
T1 / READ_ONLY_LOCAL
T2 / EPHEMERAL_COMPUTE
T3 / EXTERNAL_NETWORK_OR_API
T4 / CONSEQUENTIAL_MUTATION
```

A T3 provider can expose both read and write operations; effect classification is per capability/invocation, not merely per transport.

See `[[14_TOOLS/TOOL_REGISTRY_MASTER|TOOL_REGISTRY_MASTER]]` for the registry/envelope specification.

## 9. Output epistemics

Tool output begins as an observation/result of an operation.

```text
TOOL_OUTPUT != TRUTH
API_SUCCESS != SEMANTIC_CORRECTNESS
REMOTE_STATUS != CURRENT_AFTER_DELAY
TELEMETRY_PRESENT != OBSERVABILITY_COMPLETE
```

Attach source identity, time, scope, and uncertainty needed for downstream reasoning.

## 10. Side-effect finality

For durable/external mutation:

- use a stable effect identity/idempotency strategy where supported;
- bind exact target/resource state when possible;
- revalidate authority and mutable constraints before dispatch;
- distinguish dispatch from confirmed completion;
- reconcile ambiguous effects rather than blind retry;
- preserve receiver/service evidence when available.

## 11. Resource and failure controls

Tool invocation should declare/enforce material bounds:

- timeout;
- memory/CPU where locally enforceable;
- request/rate budget;
- retry budget;
- data egress scope;
- filesystem/network scope;
- failure classification;
- rollback/reconciliation strategy for mutation.

A timeout is not proof that no external effect occurred.

## 12. Inter-plane connections

- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Agents:** [[06_AGENTS/06_AGENTS_MOC|06_AGENTS_MOC]]
- **Agent systems:** [[06_AGENT_SYSTEMS/GITHUB_AGENT_SKILL_INTEROP|GITHUB_AGENT_SKILL_INTEROP]]
- **Workflows:** [[08_WORKFLOWS/08_WORKFLOWS_MOC|08_WORKFLOWS_MOC]]
- **Protocols:** [[09_PROTOCOLS/09_PROTOCOLS_MOC|09_PROTOCOLS_MOC]]
- **Security:** [[18_SECURITY/18_SECURITY_MOC|18_SECURITY_MOC]]
- **Observability:** [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]]

## 13. Hard invariants

1. Capability never grants authority.
2. External credential scope never expands AMOS task scope.
3. Tool discovery never grants invocation permission.
4. Tool output is classified before promotion into knowledge/decision state.
5. Mutation uses commit-time authority/constraint revalidation.
6. Ambiguous external effects are reconciled before retry.
7. Provider/tool version and schema drift can invalidate prior adapters.
8. Observability gaps remain visible.
9. Secret material never enters source-controlled tool descriptors or logs.
10. Registered/available does not imply empirically reliable.

______________________________________________________________________

**Master registry:** [[14_TOOLS/TOOL_REGISTRY_MASTER|TOOL_REGISTRY_MASTER]]  
**Parent:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
