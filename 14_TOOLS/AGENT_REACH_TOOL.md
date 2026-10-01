---
title: "Agent Reach Governed External Tool Integration"
type: tool-integration
aliases:
  - AGENT_REACH_TOOL
  - Agent Reach
source: 14_TOOLS
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: CONDITIONAL
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
external_source:
  repository: Panniantong/Agent-Reach
  version: 1.5.0
  commit: da5044d26fc6adddb6554d5679c94ac22e76e428
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  scope: agent_reach_external_tool_integration
---

# Agent Reach Governed External Tool Integration

## 1. Purpose

Agent Reach is admitted into AMOS OS as an **external toolchain manager**, not as a universal internet-access wrapper.

Upstream Agent Reach selects, installs, configures, and health-checks tools such as `yt-dlp`, `gh`, `mcporter`, OpenCLI, and platform-specific CLIs. After installation, those upstream tools are invoked directly. Therefore AMOS MUST preserve:

```text
AGENT_REACH_MANAGER != UPSTREAM_TOOL
TOOL_DISCOVERY != TOOL_AUTHORITY
TOOL_INSTALLED != TOOL_AUTHORIZED
HEALTH_CHECK_PASS != EFFECT_AUTHORITY
```

Every upstream tool discovered or installed by Agent Reach requires its own AMOS capability/authority decision before consequential invocation.

## 2. Pinned external identity

```yaml
external_provider:
  provider_id: external-agent-reach
  provider_type: EXTERNAL_SYSTEM
  repository: Panniantong/Agent-Reach
  upstream_version: 1.5.0
  pinned_commit: da5044d26fc6adddb6554d5679c94ac22e76e428
  package_url: https://github.com/Panniantong/Agent-Reach/archive/da5044d26fc6adddb6554d5679c94ac22e76e428.zip
  minimum_python: "3.10"
  license: MIT
```

The pinned commit is part of the AMOS dependency identity. A different upstream commit is a different candidate dependency and MUST be revalidated before promotion.

## 3. Capability split

### 3.1 `agent-reach-health`

```yaml
capability:
  tool_id: agent-reach-health
  provider_id: external-agent-reach
  tier: T3_EXTERNAL_NETWORK
  capabilities:
    - inspect_environment
    - report_channel_health
    - report_missing_dependencies
    - inspect_upstream_version
  side_effects: false
  epistemic_output: OBSERVATION
  authority_required:
    - network:read
    - process:execute:agent-reach
  failure_behavior: FAIL_CLOSED
```

The admitted diagnostic command is:

```bash
agent-reach install --env=auto
```

No `--system` flag is present. Upstream defines the command without `--system` as safe/check-only mode.

### 3.2 `agent-reach-bootstrap`

```yaml
capability:
  tool_id: agent-reach-bootstrap
  provider_id: external-agent-reach
  tier: T4_CONSEQUENTIAL_STATE_MUTATION
  capabilities:
    - install_pinned_user_package
    - replace_mismatched_agent_reach_version
  side_effects: true
  epistemic_output: EFFECT
  authority_required:
    - host:user-package:write
    - process:execute:python
    - network:read:github
  failure_behavior: FAIL_CLOSED
```

The AMOS bootstrap installs only the pinned Agent Reach Python package into either `pipx` or the isolated `~/.agent-reach-venv` fallback. It does **not** authorize Agent Reach system installation.

## 4. Explicit non-authority boundary

The following are **not** implicitly authorized by this integration:

- `agent-reach install --system`;
- operating-system package installation;
- global npm package installation;
- browser-cookie extraction or import;
- login/session reuse;
- Twitter/X, Reddit, Facebook, Instagram, XiaoHongShu, or other authenticated platform access;
- creation of external posts, comments, issues, pull requests, or messages;
- proxy configuration;
- API-key ingestion;
- persistent credential writes;
- invocation of an upstream tool solely because Agent Reach reports it available.

These require separately resolved AMOS capabilities, scope, authority, provenance, and effect handling.

## 5. Runtime bootstrap

Reference implementation:

```text
04_RUNTIME/01_BOOT/agent_reach_bootstrap.py
```

Safe inspection:

```bash
python 04_RUNTIME/01_BOOT/agent_reach_bootstrap.py
```

Explicit pinned package installation:

```bash
python 04_RUNTIME/01_BOOT/agent_reach_bootstrap.py --apply
```

The bootstrap intentionally exposes no `--system` option.

## 6. Dependency invariants

```text
INV-AR-01: upstream repository + pinned commit + expected version form one dependency identity.
INV-AR-02: version mismatch fails closed unless --apply is explicitly supplied.
INV-AR-03: bootstrap MUST NOT emit or execute `agent-reach install --system`.
INV-AR-04: Agent Reach availability MUST NOT grant authority to any upstream tool.
INV-AR-05: authenticated channel configuration requires separate user authority and secret-handling controls.
INV-AR-06: safe diagnostics are OBSERVATION; installation is EFFECT.
INV-AR-07: upstream dependency drift invalidates the prior validation result until revalidated.
```

## 7. Validation

GitHub CI gate:

```text
.github/workflows/agent-reach-integration-gate.yml
```

The gate installs the exact pinned upstream archive into an ephemeral virtual environment, verifies `Agent Reach v1.5.0`, then executes the AMOS bootstrap in check-only mode.

Validation state remains `PARTIALLY_VALIDATED` until the GitHub workflow produces a passing run for the committed integration. A passing CI run proves only the scoped package/bootstrap contract on that runner; it does not prove authenticated channel availability or production-host compatibility.

## 8. Provenance

Primary external source:

```text
https://github.com/Panniantong/Agent-Reach
commit da5044d26fc6adddb6554d5679c94ac22e76e428
```

AMOS bindings:

- [[14_TOOLS/TOOL_REGISTRY_MASTER]]
- [[14_TOOLS/TOOLS_TOOL_CONTRACT]]
- [[14_TOOLS/14_TOOLS_MOC]]
- [[03_CONTROL_PLANE/02_CAPABILITY/CAPABILITY_MANIFEST]]
- [[04_RUNTIME/01_BOOT/agent_reach_bootstrap.py]]

## 9. Promotion boundary

This integration promotes only a pinned, governed mechanism for installing and checking Agent Reach. It does not promote Agent Reach, its upstream tools, or any platform backend into unrestricted AMOS authority.
