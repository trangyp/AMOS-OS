---
title: AMOS Agent Interoperability Compiler
type: tool
status: CONDITIONAL
origin_architect: Trang Phan
epistemic_class: AMOS_MODEL
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 07_SKILLS/amos-agent-interoperability-compiler/SKILL.md
    - a2aproject/A2A specification 1.0.0
    - modelcontextprotocol/python-sdk v2 documentation
    - traceloop/openllmetry documentation
  scope: agent_interoperability_projection
---

# AMOS Agent Interoperability Compiler

Deterministic standard-library compiler that validates AMOS agent metadata and emits bounded interoperability projections.

## Entry point

`07_SKILLS/amos-agent-interoperability-compiler/scripts/compile_interop.py`

## Execution envelope

Default `--check` and stdout projection mode are read-only local operations. They may read `06_AGENTS/**/*.json` but must not mutate repository state, call networks, load credentials, or grant authority.

Persistent `--output` writes are caller-authorized filesystem effects and must not be treated as implicit repository commit authority.

## Outputs

- `manifest` — normalized AMOS interoperability manifest.
- `a2a-candidate` — discovery projection explicitly labeled `A2A_CANDIDATE_NOT_CONFORMANT` until endpoint, transport, authentication, runtime handler, and protocol-schema checks exist.
- `mcp-candidate` — tool projection explicitly labeled `MCP_CANDIDATE_NOT_CALLABLE` until typed schemas, executable handlers, authority gates, and transport validation exist.

## Invariants

1. `CAPABILITY != AUTHORITY`.
2. `PROJECTION != PROTOCOL_CONFORMANCE`.
3. `MANIFEST != DEPLOYED_ENDPOINT`.
4. Missing identity, version, capability name, or side-effect declaration fails closed.
5. Internal reasoning, hidden prompts, private memory, credentials, and control-plane secrets are never projection fields.
6. Generated manifests preserve source path, declared version, governance state, and origin attribution.

## Evidence state

Local fixture execution has demonstrated positive compilation and negative fail-closed behavior. Repository-wide compatibility remains `UNKNOWN/GAP` until the GitHub Actions interoperability contract executes on the branch and until legacy agent metadata is assessed for schema completeness.
