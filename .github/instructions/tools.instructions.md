---
description: AMOS external tool, connector, MCP, CLI, API, and runtime adapter integration rules.
applyTo: '14_TOOLS/**'
---

# AMOS Tool Integration Instructions

Tools expose capability; the control plane grants authority.

## Registration

Before adding a tool:
- search for an existing canonical owner;
- identify exact upstream repository/version/commit when external;
- classify tool tier and side effects;
- declare inputs, outputs, dependencies, resource limits, epistemic output class, failure modes, and authority requirements;
- prefer a narrow adapter over vendoring an upstream repository.

## External dependencies

Use immutable pins for security-sensitive or reproducibility-critical integrations. Floating `main`, `latest`, remote install scripts, and unverified binaries are not acceptable production pins.

No credentials, cookies, tokens, or secrets may be committed. Local authentication state must remain outside repository state.

## Execution boundary

Tool discovery or health checks must not silently perform installation, authentication, global configuration, destructive mutation, or durable external effects. Split those into distinct capabilities with distinct authority classes.

## Output handling

Classify tool output as OBSERVATION, DERIVED, MODEL, EFFECT, or UNKNOWN/GAP before reasoning consumes it. Preserve exact source/tool identity and timestamp where freshness matters.

## Validation

At minimum test missing tool, malformed input, unauthorized use, timeout, non-zero exit, stale dependency, duplicate effect, and version mismatch when relevant.
