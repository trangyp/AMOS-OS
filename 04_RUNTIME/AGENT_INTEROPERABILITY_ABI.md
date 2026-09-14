---
title: AMOS Agent Interoperability ABI
artifact_id: AMOS-AGENT-INTEROP-ABI
version: 1.0.0
amos_core_target: v4.4
origin_architect: Trang Phan
status: ACTIVE_MODEL
conclusion_class: AMOS_MODEL
epistemic_class: AMOS_MODEL
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - a2aproject/A2A
    - modelcontextprotocol/python-sdk
    - openai/openai-agents-python
    - 06_AGENTS/00_INDEX/AMOS_AGENT_SCHEMA_MASTER_v3
  scope: agent_interoperability
---

# AMOS Agent Interoperability ABI

## Purpose

This contract separates AMOS agent semantics from host/external protocol bindings.

An AMOS agent may be exposed through A2A, consume or expose MCP surfaces, or run inside a host agent SDK. None of those bindings changes AMOS identity, epistemic class, provenance, authority, or commit semantics.

```text
ProtocolCompatibility != AMOSAuthority
CapabilityDiscovery != Permission
Message != Artifact
TaskCompletion != AuthorizedCommit
ExternalProtocolVersion != AMOSCanonVersion
```

## Source boundary

External reference points used by this ABI:

- A2A: Agent Cards, task/message/artifact separation, `contextId`, stateful task lifecycle, interface-level `protocolVersion`, and `/.well-known/agent-card.json` discovery.
- MCP Python SDK v2: compatibility with the 2026-07-28 MCP specification and typed tools/resources/prompts over standard transports.
- OpenAI Agents SDK: agents, tools, guardrails, handoffs, sessions, human-in-the-loop, tracing, and sandbox-agent execution patterns.

These remain external protocol/source claims. AMOS does not promote them into SOURCE_CANON.

## ABI object

```yaml
schema: AMOS_AGENT_INTEROP_ABI_v1
agent_id: amos-example-agent
identity:
  name: Example
  description: Example AMOS agent
  version: 1.0.0
external_protocols:
  a2a:
    discovery_path: /.well-known/agent-card.json
    binding_status: DECLARED | UNBOUND | LEGACY_DECLARATION_REQUIRES_ENDPOINT_BINDING
    supported_interfaces:
      - protocol_binding: JSONRPC
        protocol_version: "1.0"
        url: optional
    default_input_modes: []
    default_output_modes: []
    skill_refs: []
  mcp:
    compatibility_target_revision: "2026-07-28"
    binding_status: DECLARED | UNBOUND
    roles: []
amos_extensions:
  epistemic_class: AMOS_MODEL | SOURCE_CLAIM | DERIVED | UNKNOWN/GAP
  rscf_state: ...
  capability_is_not_authority: true
  commit_authority_external_to_protocol: true
```

## A2A mapping

Existing agents may contain:

```json
{
  "agent_card": {
    "protocol": "A2A-v1.0",
    "name": "...",
    "description": "..."
  }
}
```

That field is treated as a legacy declaration, not proof of a deployed A2A endpoint.

The compatibility adapter maps it to:

```yaml
supported_interfaces:
  - protocol_binding: JSONRPC
    protocol_version: "1.0"
binding_status: LEGACY_DECLARATION_REQUIRES_ENDPOINT_BINDING
```

No URL is invented. Promotion to `DECLARED` requires an actual interface binding.

Protocol version belongs to the external interface declaration. AMOS must not encode a floating protocol version into agent identity or AMOS canon.

External version drift invalidates only the affected protocol binding and its dependents, not the AMOS agent identity itself.

## Task lifecycle mapping

AMOS adopts the useful separation between task, message, and artifact while retaining stricter infrastructure governance.

```text
A2A Task      -> AMOS governed task state
A2A Message   -> communication / clarification / status data
A2A Artifact  -> candidate deliverable/evidence object
contextId     -> external conversation/task context identifier
```

AMOS task states may include:

```text
SUBMITTED
WORKING
INPUT_REQUIRED
AUTH_REQUIRED
WAITING_DEPENDENCY
COMPLETED
CANCELED
REJECTED
FAILED
```

`COMPLETED` does not authorize a durable effect. Commit authority remains owned by the AMOS infrastructure/control plane.

## MCP mapping

MCP is treated primarily as the agent-to-tool/data boundary.

The ABI records a compatibility target revision, not an assertion that every AMOS agent is an MCP client or server.

```yaml
mcp:
  compatibility_target_revision: "2026-07-28"
  binding_status: UNBOUND
  roles: []
```

A binding becomes `DECLARED` only when concrete MCP roles/interfaces are present.

Tool descriptions, annotations, prompts, or server instructions remain untrusted capability metadata. They do not grant authority.

## Host runtime mapping

Host frameworks may provide handoffs, sessions, tracing, guardrails, sandboxes, or human approval primitives. They are deployment mechanisms beneath AMOS infrastructure authority:

```text
HostAgentRunner
-> AMOS task proposal
-> AMOS policy/authority gate
-> tool/effect adapter
-> durable/world effect
```

A host runtime must not widen AMOS capabilities, mint new authority, suppress provenance, or change epistemic class.

## Invariants

1. `agent_id` is stable across host protocol mappings.
2. Protocol version changes do not silently change AMOS semantic identity.
3. External protocol metadata is freshness-bound and revalidated when upstream specifications change.
4. Missing endpoint/binding information remains `UNBOUND` or `UNKNOWN/GAP`.
5. Child/delegated protocol sessions cannot gain authority beyond their AMOS capability grant.
6. Messages cannot substitute for executed receipts or artifacts.
7. Tool availability through MCP does not imply permission to invoke the tool.
8. A2A task completion cannot directly finalize an AMOS durable effect.
9. Legacy fields remain readable until migration completes; compatibility adapters must not invent missing semantics.
10. Protocol downgrade is fail-closed when required security/capability semantics would be lost.

## Executable validation

```bash
python3 scripts/agent_protocol_abi.py --self-test
python3 scripts/agent_protocol_abi.py --scan-dir 06_AGENTS
python3 scripts/agent_protocol_abi.py 06_AGENTS/<agent>.json
```

The scan reports legacy A2A declarations separately from invalid contracts. A legacy declaration is not automatically an error because repository-wide migration is staged.

## Migration strategy

1. Preserve legacy `agent_card.protocol` fields as compatibility input.
2. Normalize through `agent_protocol_abi.py`.
3. New or materially edited agents should declare interface-level protocol bindings rather than `A2A-v1.0` identity strings.
4. Bind real endpoints only when deployment evidence exists.
5. Revalidate affected adapters when A2A or MCP protocol revisions change.
6. Remove the compatibility reader only after no active agents depend on the legacy shape.
