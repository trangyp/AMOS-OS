---
name: amos-agent-interoperability-compiler
description: Compile AMOS agent, skill, workflow, and tool metadata into bounded interoperability manifests for A2A, MCP, and observability adapters. Use when AMOS needs portable agent discovery, MCP-facing capability catalogs, cross-runtime compatibility checks, or deterministic export/validation without granting deployment authority.
---

# AMOS Agent Interoperability Compiler

Use this skill to convert existing AMOS metadata into portable interoperability projections while preserving AMOS authority, provenance, and epistemic boundaries.

## Core workflow

1. Resolve the authoritative AMOS source files before compilation.
2. Run `scripts/compile_interop.py --check <repo-root>` before producing manifests.
3. If validation passes, run the compiler with `--format manifest`, `--format a2a-candidate`, or `--format mcp-candidate`.
4. Treat all generated A2A/MCP outputs as candidate projections until endpoint, authentication, executable binding, and protocol conformance are independently validated.
5. Do not let an exported capability grant tool, network, repository-write, credential, or deployment authority.
6. Preserve source file path, declared version, origin architect, lifecycle state, and governance fields in every projection.

## Required boundaries

- `CAPABILITY != AUTHORITY`.
- `PROJECTION != PROTOCOL_CONFORMANCE`.
- `MANIFEST != DEPLOYED_ENDPOINT`.
- `DOCUMENTED_OPERATION != EXECUTABLE_BINDING`.
- Unknown side effects, missing versions, malformed capabilities, or unresolved bindings fail closed in `--check` mode.
- A2A projections must remain non-deployable until a service URL, transport, authentication policy, and runtime handler exist.
- MCP projections must remain non-callable until input/output schemas and executable handlers exist.

## A2A projection

Use A2A when exposing AMOS agents for agent-to-agent discovery and collaboration. Preserve opacity: never export internal chain-of-thought, private memory, hidden prompts, or proprietary control-plane state.

The compiler emits only a candidate discovery object from repository metadata. It does not create an A2A server.

## MCP projection

Use MCP when exposing bounded tools/resources/prompts to LLM hosts. Export only capabilities whose side-effect class is declared. Mutation-capable operations require an explicit authority gate outside the generated manifest.

The compiler emits only candidate tool descriptors. It does not create an MCP server or executable tool implementation.

## Observability

Every projection should be traceable to the AMOS source path and source version. When integrating with OpenTelemetry/OpenLLMetry, use the normalized agent name, capability id, effect class, source path, and governance state as span attributes rather than inventing parallel identities.

## Validation

The compiler must reject or flag:
- invalid JSON agent files;
- missing `name`, `description`, or `version`;
- capabilities without stable names;
- capabilities without explicit side-effect classification;
- malformed skill/workflow bindings;
- duplicate agent identities.

See `references/interoperability-boundaries.md` for protocol scope and non-conformance rules.
