---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Vault Domain Knowledge
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `amos-retrieval-conditioned-orchestration-budget-rscf`

## Vault-Sourced Content

### Source 1: AMOS Super Kernel — Unified Meta-Orchestration Architecture

> Path: `kernel/A/AMOS Super Kernel — Unified Meta-Orchestration Architecture.md` | Size: 37094 chars | Match score: 10

## AMOS Super Kernel — Unified Meta-Orchestration Architecture

## Overview (2)

The source explicitly defines the kernel as:

```text
an operating rule-set, not a persona
```

Its declared role is:

\[
\\boxed{
Request
\\rightarrow
Normalize
\\rightarrow
Decompose
\\rightarrow
Route
\\rightarrow
Constrain
\\rightarrow
Synthesize
\\rightarrow
Audit
\\rightarrow
Output
}
\]

The source identifies **Trang Phan** as author of the canonical frameworks that the kernel is required to preserve.

The strongest appropriate epistemic classification is:

```text
RSCF STATE: SOURCE_CLAIM
CANON TYPE: FRAMEWORK
CANON GROUP: META
```

The architecture below preserves the supplied kernel while separating explicit source structure from derived AMOS formalization.

______________________________________________________________________

## 1. Kernel Identity

The source declares:

```text
NAME:    AMOS_KERNEL_SUPER_vInfinity
VERSION: vInfinity_clean
ROLE:    Unified meta-kernel orchestrating all AMOS engines and domains
TYPE:    Operating rule-set
```

The kernel is not defined as a personality layer.

Its identity is functional:

## \[ KernelRole

Normalize
\+
Route
\+
Constrain
\+
Integrate
\]

The intended abstraction is therefore closer to:

```text
CONTROL PLANE
```

than:

```text
PERSONA
```

______________________________________________________________________

## 2. Core Objective

The kernel's primary transformation can be modeled as:

\[
R\_{raw}
\\xrightarrow{N}
P
\\xrightarrow{D}
{T_1,\\ldots,T_n}
\\xrightarrow{Route}
{E_1,\\ldots,E_n}
\\xrightarrow{C}
{O_1,\\ldots,O_n}
\\xrightarrow{S}
O\_{final}
\]

where:

This is a **derived formal representation** of the source pipeline.

______________________________________________________________________

## 3. Core Role

The source defines six primary functions.

```text
1. Receive arbitrary user requests.
2. Normalize them into clear problem structures.
3. Decompose them into sub-tasks.
4. Route sub-tasks to appropriate AMOS engines.
5. Enforce safety, constraints, and canon integrity.
6. Recombine results into coherent deterministic output.
```

Compressed:

## \[ AMOS\_{Kernel}

N+D+R+C+S+A
\]

where:

______________________________________________________________________

## 4. Canon Dependency Layer

The source requires the kernel to preserve a fixed set of named canon structures.

These include:

```text
UBI
TSS
TPE
PSI
PISync
AMOS Engines
Law of Law
Rule of 2
Rule of 4
```

Conceptually:

```text
                       AMOS SUPER KERNEL
                              │
       ┌──────────────────────┼──────────────────────┐
       │                      │                      │
       ▼                      ▼                      ▼
      UBI                    TSS                    TPE
       │                      │                      │
       └──────────┬───────────┴──────────┬───────────┘
                  │                      │
                  ▼                      ▼
                 PSI                  PISync
                  │
                  ▼
          CANON / META-LAWS
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
    Law of Law  Rule 2    Rule 4
                  │
                  ▼
            AMOS Engines
```

The source st

______________________________________________________________________

### Source 2: AMOS Agent Orchestration Workflow

> Path: `amos-general/A/Agent/AMOS_Agent_Orchestration_Workflow.md` | Size: 35578 chars | Match score: 10

## AMOS Agent Orchestration Workflow

Comprehensive workflow for orchestrating all 36 AMOS agents across 7 canonical systems. Covers agent selection, coordination patterns, execution loops, conflict resolution, output modes, and integration with existing brain workflows.

## Overview

AMOS has 36 agents organized into 7 canonical systems. This workflow governs how tasks are routed to agents, how agents execute, how multi-agent coordination works, and how conflicts are resolved.

______________________________________________________________________

## Section 1: Agent Registry

### 1.1 Agent Count and System Distribution

| System             | Agent Count | Agents                                                                                                        |
| ------------------ | ----------- | ------------------------------------------------------------------------------------------------------------- |
| BRAIN_SYSTEM       | 5           | Architecture_Agent, Decomposer_Agent, Planner_Agent, Reflection_Agent, Strategist_Agent                       |
| EXECUTION_SYSTEM   | 7           | Automation_Agent, Coding_Agent, Deployment_Agent, DevOps_Agent, Document_Agent, Refactor_Agent, Writing_Agent |
| LEGAL_SYSTEM       | 5           | Compliance_Agent, Contract_Agent, IP_Agent, Legal_Agent, LegalRisk_Agent                                      |
| MONEY_SYSTEM       | 6           | Cashflow_Agent, Finance_Agent, FinanceRisk_Agent, Investment_Agent, MacroAnalyst_Agent, Opportunity_Agent     |
| SENSE_SYSTEM       | 3           | Context_Agent, Sensors_Agent, StateSummarizer_Agent                                                           |
| WORLD_MODEL_SYSTEM | 5           | GeoAnalyst_Agent, MacroAnalyst_Agent, SectorAnalyst_Agent, Shock_Agent, Trend_Agent                           |
| LIFE_SYSTEM        | 3           | Health_Agent, LoadBalancer_Agent, Routine_Agent                                                               |
| **Total**          | **36**      |                                                                                                               |

### 1.2 System Roles

| System             | Purpose                                                          | Primary Domain                          |
| ------------------ | ---------------------------------------------------------------- | --------------------------------------- |
| BRAIN_SYSTEM       | Reasoning, planning, architecture, strategy, self-reflection     | Core reasoning, system design, strategy |
| EXECUTION_SYSTEM   | Practical execution: code, automation, deployment, docs, writing | Software, infrastructure, content       |
| LEGAL_SYSTEM       | Legal analysis, compliance, contracts, IP, legal risk            | Law, regulation, contracts, IP          |
| MONEY_SYSTEM       | Financial analysis, cashflow, investment, macro, opportunity     | Finance, economics, investment          |
| SENSE_SYSTEM       | Context gathering, sensing, state summarisation                  | Context, monitoring, state awareness    |
| WORLD_MODEL_SYSTEM | Geographic, macro, sector, shock, trend analysis                 | World modeling, analysis, forecasting   |
| LIFE_SYSTEM        | Health, load balancing, routine management                       | Biology, operations, behaviour          |

______________________________________________________________________

## Section 2: Agent Execution Loop

All 36 agents follow the same 10-step execution loop:

```
1. Incoming request arrives
2. META_ORCHESTRATOR detects task intent and domain tags
3. Kernel routing determines which kernels activate (see amos-kernel-routing-workflow)
4. Relevant agents are selected based on task type and kernel coverage
5. Each agent applies its specialised logic within law-stack constraints
6. Results are merged by META_ORCHESTRATOR
7. Conflicts are resolved (K_META_LOGIC has final say)
8. Safety/ethics filter applied (S6 of HIE pipeline)
9. Expression translation converts structured output to final language (S8)
10. Response delivered; evaluation tagged (S9)
```

### Step Details

- ROUTE_EV: ev, cha

______________________________________________________________________

### Source 3: AMOS_Workflow_Orchestration_Kernel_v0_Tech

> Path: `kernel/A/AMOS_Workflow_Orchestration_Kernel_v0_Tech.md` | Size: 15969 chars | Match score: 10

{
"kernel_id": "AMOS_Workflow_Orchestration_Kernel_v0",
"version": "1.0.0",
"source": "md/Kernels/Tech/AMOS_Workflow_Orchestration_Kernel_v0.md",
"description": "Kernel for workflow design, automation, orchestration, and pipeline management within the AMOS stack. Defines how individual tasks compose into workflows, how workflows are automated, and how pipeline execution is monitored and controlled.",
"group": "Kernels.Tech",
"category": "Tech",
"priority": 7,
"required": false,
"domains": ["workflow", "automation", "orchestration", "pipeline", "monitoring"],
"depends_on": [[02_KERNEL/01_META_LOGIC/K_META_LOGIC|K_META_LOGIC]]\["[[02_KERNEL/01_META_LOGIC/K_META_LOGIC|K_META_LOGIC]]", "K_TECH_ENGINE"\],

"meta": {
"role": "Workflow Orchestration Kernel",
"creator": "Trang Phan (Origin Architect)",
"status": "defined",
"binding_rules": ["Law_of_Law", "Rule_of_2", "Rule_of_4", "Absolute_Integrity"]
},

"purpose": "Define, execute, monitor, and control workflows that span multiple AMOS agents, kernels, and engines. Provide a structured model for turning a high-level task into an orchestrated sequence of coordinated operations with defined inputs, outputs, checkpoints, and failure handling.",

"workflow_primitives": {
"task": {
"description": "A single unit of work assignable to one agent or kernel.",
"fields": {
"task_id": "unique identifier",
"description": "what the task does",
"agent_assignment": "which agent handles it",
"kernel_set": "which kernels activate",
"inputs": "required inputs (from previous tasks or user)",
"outputs": "expected outputs (passed to next tasks or final output)",
"constraints": "law constraints, safety constraints, domain constraints",
"priority": "normal, high, critical",
"timeout": "maximum execution time",
"dependency_ids": "tasks that must complete before this task starts"
}
},
"workflow": {
"description": "An ordered composition of tasks with defined flow control.",
"fields": {
"workflow_id": "unique identifier",
"name": "human-readable workflow name",
"trigger": "what starts this workflow (user request, event, scheduled)",
"tasks": "ordered task list with dependencies",
"flow_control": "sequential, parallel, conditional, iterative, or hybrid",
"entry_task": "first task in the workflow",
"exit_tasks": "tasks whose completion marks workflow success",
"failure_handling": "what happens on task failure (retry, abort, escalate, compensate)",
"monitoring_points": "checkpoints where state is recorded and can be inspected"
}
},
"pipeline": {
"description": "A multi-stage workflow where each stage produces structured output consumed by the next stage.",
"fields": {
"pipeline_id": "unique identifier",
"stages": "ordered stages, each containing one or more tasks",
"stage_inputs": "what each stage receives (from previous stage output or extern

______________________________________________________________________

**MOC:** references_MOC

## Related

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-retrieval-conditioned-orchestration-budget-rscf-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-retrieval-conditioned-orchestration-budget-rscf/references/vault_domain_knowledge.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
