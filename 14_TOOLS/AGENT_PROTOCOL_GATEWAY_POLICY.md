---
title: AMOS Agent Protocol Gateway Policy
type: tool_policy
source: 14_TOOLS
origin_architect: Trang Phan
steward: Trang Phan
status: CONDITIONAL_SPECIFICATION
epistemic_class: AMOS_MODEL
---

# AMOS Agent Protocol Gateway Policy

This policy governs MCP, A2A, and agent-to-model traffic at an AMOS protocol boundary. It defines an adapter/enforcement surface beneath the AMOS infrastructure control plane; it does not grant final effect authority.

## External source capsules

Mechanisms were inspected from these public sources and remain `SOURCE_CLAIM` until independently validated in AMOS:

- `agentgateway/agentgateway@5e5633bffe6dc5fdd29256648987197f366e462a` — protocol gateway patterns for MCP/A2A routing, authentication, policy/RBAC, rate limiting, and OpenTelemetry.
- `snyk/agent-scan@73ceb7119825edf06e6800f0acfe284a4cc9c842` — agent/MCP/skill discovery and the explicit warning that stdio MCP discovery can execute configured commands.

No external branding or claimed performance result is promoted into AMOS canon.

## Authority topology

```text
Agent / Host
    -> Protocol Gateway
    -> Typed Capability / Evidence
    -> AMOS Infrastructure Control Plane
    -> Effect Executor / Remote Service
```

The gateway may authenticate, filter, route, meter, redact, and observe traffic. It may not mint AMOS commit authority or treat successful authentication as sufficient authorization for a durable effect.

`AUTHENTICATED != AUTHORIZED`

`GATEWAY_ROUTE != COMMIT_AUTHORITY`

`TOOL_DISCOVERED != TOOL_TRUSTED`

`MCP_CONFIG_PARSED != MCP_SERVER_EXECUTED`

`TOOL_DESCRIPTION != TRUSTED_INSTRUCTION`

`DISCOVERY != EXECUTION_FREE`

## Admission pipeline

1. **Static discovery** — parse manifests/configuration without launching local commands when possible.
2. **Transport classification** — distinguish local stdio, HTTP, Streamable HTTP/SSE, A2A, and provider-native connectors. Do not apply one execution policy to all transports.
3. **Identity and source binding** — bind server/agent identity, source configuration, version/ref where available, and current trust state.
4. **Launch gate for local stdio** — starting a configured command is an execution effect. Require explicit execution authority. When source trust is unresolved, launch only inside an approved disposable sandbox or return `QUARANTINE`.
5. **Capability acquisition** — retrieve tool/skill/agent metadata only after the transport gate passes.
6. **Instruction-taint admission** — descriptions, prompts, resources, and returned text are untrusted data. They must not override system/user/control-plane instructions or silently widen authority.
7. **Policy gate** — apply gateway-local authentication, route allowlists, rate/budget limits, content guards, and transport policy.
8. **Control-plane gate** — consequential calls are proposals until the AMOS infrastructure control plane validates authority, provenance, freshness, semantic transaction state, and effect-release state.
9. **Output admission** — validate schema/effect class, attach provenance, preserve taint, and fail closed on ambiguous classification.
10. **Observability** — emit bounded telemetry with correlation identity while redacting credentials and protected payloads. Telemetry is evidence, not authority.

## Transport-specific rules

### Local stdio MCP

- Treat `command + args + environment + working directory` as an executable effect descriptor.
- Do not auto-launch an untrusted server merely to inspect its tool descriptions.
- Strip or explicitly allow credentials passed to the subprocess.
- Bind launch receipts to the exact command/configuration identity.
- Reconcile ambiguous process state before retrying effectful tools.

### Remote MCP / HTTP

- Validate endpoint identity and authentication separately from AMOS authorization.
- Bound redirects, timeouts, response size, and allowed egress destinations.
- Treat server-provided tool descriptions and schemas as untrusted external input until admitted.

### A2A

- Agent Card discovery describes offered capability; it does not prove runtime implementation, trust, or authorization.
- Preserve task identity and terminal-state semantics across handoffs.
- Do not expose hidden prompts, private memory, internal chain-of-thought, control-plane secrets, or credentials through interoperability metadata.

## Gateway-local policy is not global authority

Gateway RBAC/CEL-style policy, API keys, JWTs, OAuth scopes, rate limits, and provider guardrails may reduce the admissible action set. They do not replace AMOS commit-time authorization.

A lower layer may only tighten authority:

```text
EffectivePermission <= GatewayPolicy <= ControlPlaneAuthority
```

The relation above is an AMOS policy-order model, not an empirical claim about any external gateway implementation.

## Result states

Return one of:

- `ADMIT_READ_ONLY`
- `ADMIT_PROPOSAL_ONLY`
- `REQUIRE_EXECUTION_AUTHORITY`
- `REQUIRE_CONTROL_PLANE_AUTHORITY`
- `QUARANTINE_UNTRUSTED_SERVER`
- `BLOCK_TOOL_INSTRUCTION_TAINT`
- `BLOCK_SCHEMA_OR_EFFECT_AMBIGUITY`
- `REVALIDATE_IDENTITY_OR_POLICY`
- `UNKNOWN_GAP`

Do not convert an unresolved state to PASS for availability or convenience.

## Implementation boundary

This file is a policy contract. It does not prove that AMOS currently runs a production MCP/A2A gateway. Promotion to implemented runtime requires a concrete adapter, transport tests, adversarial instruction/tool-poisoning tests, authority integration, observability evidence, rollback/recovery behavior, and an executed receipt bound to the exact runtime artifact.

## Cross-plane bindings

- [[14_TOOLS/TOOLS_TOOL_CONTRACT|Tool contract]]
- [[14_TOOLS/SANDBOX_TOOL_EXECUTION_PROTOCOL|Sandbox execution contract]]
- [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|Infrastructure control plane]]
- `07_SKILLS/amos-agent-interoperability-compiler` — bounded manifest projection only
