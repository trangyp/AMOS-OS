---
title: "AMOS GitHub Agent and Skill Interoperability Contract"
type: architecture
origin_architect: Trang Phan
steward: Trang Phan
status: CANDIDATE_IMPLEMENTED_CONTRACT
epistemic_class: AMOS_MODEL
source_registry: 11_KNOWLEDGE/EXTERNAL_AGENT_SOURCE_REGISTRY.json
---

# AMOS GitHub Agent and Skill Interoperability Contract

## 1. Purpose

This contract turns external GitHub agent/skill ecosystems into a typed **interoperability surface** for AMOS OS without making any external framework an AMOS authority source.

The contract is informed by pinned observations from the external source registry and by existing AMOS capability/authority rules.

```text
EXTERNAL SOURCE != AMOS CANON
EXTERNAL POPULARITY != VALIDATION
CAPABILITY != AUTHORITY
DISCOVERY != ADMISSION
INSTALLABLE != SAFE
AGENT MESSAGE != AUTHORITY
TOOL AVAILABLE != TOOL PERMITTED
TEST PASS != PRODUCTION VALIDITY
```

## 2. Portable resource ABI

AMOS recognizes six portable repository resource classes plus protocol/runtime support objects:

```text
AGENT
  role-specific reasoning/execution policy

SKILL
  reusable task capability with instructions and optional scripts/references/assets

INSTRUCTION
  ambient or path-scoped behavioral constraint

WORKFLOW
  explicit state/transition graph coordinating agents, skills, tools, checks, and human gates

PLUGIN
  distribution bundle containing one or more governed resources

TOOL_SERVER
  external capability transport such as MCP

PROTOCOL
  cross-runtime interoperability contract such as A2A or MCP

RUNTIME
  execution substrate implementing agent/workflow semantics

OBSERVABILITY
  traces, spans, events, checkpoints, receipts, or evaluation surfaces
```

A repository object may implement multiple classes, but the classes MUST remain separately addressable.

## 3. External-to-AMOS mapping

| External mechanism | AMOS mapping | AMOS boundary |
| --- | --- | --- |
| Agent Skills `SKILL.md` bundle | `07_SKILLS/<skill>/SKILL.md` + optional one-level resources | Skill never mints authority |
| GitHub Copilot custom agent | `.github/agents/*.agent.md` + `06_AGENTS`/`06_AGENT_SYSTEMS` identity | Agent is a role/policy proposal surface |
| Agent instructions | `.github/copilot-instructions.md` or path-scoped instructions | Instruction precedence remains below AMOS canon/control plane |
| Agent workflow graph | `08_WORKFLOWS` | Workflow owns sequencing, not commit authority |
| MCP server | `14_TOOLS` / `15_INTERFACES` | Tool discovery/transport does not authorize invocation |
| A2A Agent Card/task | `06_AGENT_SYSTEMS` / `09_PROTOCOLS` / `15_INTERFACES` | Remote agent remains opaque and independently authorized |
| Runtime checkpoint/session | `04_RUNTIME` / `12_STATE` | Checkpoint state cannot override authoritative AMOS state |
| Trace/telemetry | `17_OBSERVABILITY` | Observability evidence is not effect authority |

## 4. Skill contract

A new AMOS Skill SHOULD use the portable minimum frontmatter:

```yaml
---
name: lowercase-hyphenated-name
description: What the skill does and the concrete conditions that trigger it.
---
```

The entrypoint SHOULD contain only:

```text
purpose
non-purpose
trigger
inputs
outputs
runtime sequence
hard invariants
resource-loading rules
failure behavior
composition boundary
```

Large evidence, canon extracts, examples, and implementation detail SHOULD move to `references/`. Deterministic fragile operations SHOULD move to `scripts/`.

Legacy AMOS skills may be migrated incrementally. Legacy metadata is not deleted merely to satisfy this contract.

## 5. Agent contract

A repository-local agent is an execution role, not a principal that can self-authorize.

Minimum conceptual state:

```text
AgentRole = (
  identity,
  purpose,
  allowed task classes,
  readable resources,
  proposed tools,
  output contract,
  escalation conditions,
  stop conditions
)
```

The effective capability set is bounded by AMOS after host/runtime resolution:

```text
EffectiveCapability
  subset-or-equal
DeclaredAgentCapability
  intersection
ResolvedAMOSCapability
  intersection
FreshAuthorityScope
```

Host-specific tool lists are therefore upper bounds, never final permission.

## 6. Handoff semantics

AMOS distinguishes three relations:

### 6.1 Local handoff

```text
Agent_A --HANDOFF--> Agent_B
```

The task changes cognitive owner. Authority MUST be re-resolved for Agent B.

### 6.2 Agent as tool

```text
Agent_A --CALLS_AS_SPECIALIST--> Agent_B
```

Agent A remains workflow owner; Agent B returns a bounded result. Agent B cannot inherit Agent A's ambient authority.

### 6.3 External A2A delegation

```text
AMOS Agent --A2A_TASK--> Remote Agent
```

The remote agent is treated as an external principal/service. Agent Card discovery establishes advertised capability only. Authentication, authorization, data-disclosure scope, task freshness, and returned provenance are checked independently.

## 7. Tool-protocol semantics

MCP-like tool discovery is modeled as:

```text
ToolServer -> ToolDescriptors
```

not:

```text
ToolServer -> Permission
```

Every discovered external tool is resolved through the AMOS tool/capability registry before invocation.

For a write or external side effect:

```text
Discover
-> Resolve capability
-> Resolve principal
-> Validate authority
-> Validate parameters/provenance
-> Stage effect
-> Commit-time revalidation
-> Dispatch
-> Receipt/reconciliation
```

## 8. Workflow runtime semantics

External workflow frameworks contribute useful implementation patterns:

- graph routing;
- sequential/concurrent execution;
- fan-out/fan-in;
- retry with bounded budgets;
- checkpoints and resume;
- human interrupts;
- nested workflows;
- explicit handoffs;
- durable sessions;
- tracing and evaluation.

AMOS adopts these as implementation patterns under its own state/control planes.

A checkpoint is represented as a recoverable workflow state:

```text
Checkpoint = (
  workflow_id,
  task_id,
  node_id,
  state_hash,
  dependency_versions,
  authority_epoch_observed,
  provenance_refs,
  created_at
)
```

Resume MUST revalidate mutable dependencies and authority. A historical checkpoint cannot freeze authorization.

## 9. Source admission

External resources enter AMOS through:

```text
DISCOVER
-> PIN SOURCE
-> CLASSIFY RESOURCE
-> LICENSE CHECK
-> EXTRACT MECHANISM
-> COMPARE TO AMOS
-> QUARANTINE CONFLICTS
-> IMPLEMENT ADAPTER OR NATIVE CONTRACT
-> VALIDATE
-> REVIEW
-> PROMOTE OR REJECT
```

Raw external agent/skill files MUST NOT be mass-installed into active AMOS runtime merely because they are public, popular, or installable.

## 10. GitHub-native repository surface

AMOS repositories MAY expose host-native resources:

```text
.github/agents/*.agent.md
.github/copilot-instructions.md
.github/workflows/*.yml
07_SKILLS/*/SKILL.md
```

These improve repository operation for compatible GitHub clients. They remain projections of AMOS semantics, not canonical replacements for `01_CANON`, `03_CONTROL_PLANE`, or authoritative runtime state.

## 11. Required validation

Any change to GitHub agents, skills, workflows, or external source pins SHOULD pass:

```text
scripts/validate_external_agent_sources.py
scripts/validate_agent_skill_surface.py
scripts/validate_workflow_references.py
python -m compileall scripts
```

Validation results are scoped executable evidence only.

## 12. Failure behavior

- unknown external provenance -> `QUARANTINED`
- mutable branch ref without captured commit -> `UNKNOWN/GAP`
- incompatible license -> `BLOCK_ADMISSION`
- agent requests undeclared authority -> `BLOCK_AUTHORITY`
- discovered tool outside resolved capability -> `BLOCK_CAPABILITY`
- stale checkpoint authority -> `REVALIDATE`
- workflow references missing executable -> `BLOCK_WORKFLOW`
- external pattern conflicts with higher AMOS invariant -> preserve AMOS invariant and record `COMPETING`/rejection

## 13. Provenance

Pinned external source identities are maintained in:

`11_KNOWLEDGE/EXTERNAL_AGENT_SOURCE_REGISTRY.json`

The registry is an observation/provenance object. Changes to it do not by themselves activate software, install Skills, or grant authority.
