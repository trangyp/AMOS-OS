# GitHub Agent/Skill Mechanism Transfer Matrix

Use this reference only after the main Skill identifies a real AMOS capability gap.

## Source-to-mechanism matrix

| Source family | Mechanism worth transferring | AMOS target | Do not transfer blindly |
| --- | --- | --- | --- |
| Agent Skills repositories | Small `SKILL.md` entrypoint, bundled references/scripts/assets, task-specific loading | `07_SKILLS` | vendor-specific assumptions; mixed-license files |
| GitHub custom agents | File-based specialized agent roles | `.github/agents`, `06_AGENTS`, `06_AGENT_SYSTEMS` | model/tool names as authority |
| OpenAI Agents SDK | explicit handoffs, agents-as-tools, guardrails, HITL, sessions, tracing, sandbox task workers | `06_AGENT_SYSTEMS`, `08_WORKFLOWS`, `17_OBSERVABILITY` | provider runtime as AMOS control plane |
| Google ADK | graph routing, fan-out/fan-in, loops, retries, task delegation, tool confirmation | `04_RUNTIME`, `08_WORKFLOWS` | implicit authority in workflow node execution |
| Microsoft Agent Framework | checkpointing, time-travel inspection, middleware, OpenTelemetry, declarative roles | `04_RUNTIME`, `08_WORKFLOWS`, `17_OBSERVABILITY` | cloud/provider coupling not required by AMOS |
| LangGraph | durable state machine, interrupt/resume, stateful long-running execution | `04_RUNTIME`, `12_STATE` | checkpoint state as authorization freshness |
| A2A | Agent Cards, task lifecycle, streaming/push, opaque remote-agent collaboration | `06_AGENT_SYSTEMS`, `09_PROTOCOLS`, `15_INTERFACES` | advertised capability as trust or permission |
| MCP | typed tool/context server transport | `14_TOOLS`, `15_INTERFACES` | tool discovery as invocation permission |
| GitHub MCP | GitHub-native repo/PR/workflow/security tools and native auth scoping | `14_TOOLS`, `18_SECURITY` | PAT/OAuth scope as AMOS task authority |

## Selection rule

For candidate mechanism `m` and AMOS target `a`, transfer only when all are satisfied:

```text
Gap(a)
AND DistinctValue(m, a)
AND SourcePinned(m)
AND LicenseCompatible(m)
AND AuthorityPreserved(m, a)
AND ValidationPlanExists(m, a)
```

This is a decision rule, not an empirical equation.

## Preferred architecture decisions

### Skills

Prefer progressive loading:

```text
metadata -> SKILL.md -> targeted reference -> raw evidence
```

Keep deterministic validation in scripts. Do not make `SKILL.md` a corpus dump.

### Agents

Prefer narrow roles with explicit stop/escalation conditions. Separate implementer and reviewer roles when review independence matters.

### Workflows

Prefer explicit state graphs and durable checkpoints. Revalidate authority and mutable dependencies after resume.

### Tools

Normalize external tools into AMOS capability/effect classes before invocation. Read/write/merge/release classes should not share one blanket permission.

### Protocols

Use A2A for external agent collaboration semantics and MCP for tool/context transport. Do not collapse them into one namespace.

### Observability

Adopt traces/checkpoints/events as evidence carriers. Telemetry existence does not prove coverage, correctness, or authorization.

## Rejection conditions

Reject or quarantine a transfer when:
- no immutable source identity exists;
- license scope is incompatible or unknown for copied material;
- the candidate duplicates a stronger existing AMOS owner;
- it requires ambient credentials or authority;
- it bypasses commit-time authorization;
- the source's checkpoint/session state is treated as current truth;
- tests cannot distinguish the claimed improvement from baseline behavior;
- the source pattern expands scope more than the identified gap requires.
