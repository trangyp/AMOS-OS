---
title: "08 Workflows — README"
type: readme
source: 08_WORKFLOWS
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: workflows_readme
---

# 08 Workflows — README

## Role

Workflows coordinate multi-step execution — sequences of operations that transform inputs to outputs through defined stages.

## Typical Pattern

```
TRIGGER → PRECONDITIONS → RETRIEVE → TRANSFORM → VALIDATE → COMMIT/EXPORT → VERIFY → STORE LEARNING
```

## Inter-Plane Connections

- **Skills:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] — Workflows compose skills
- **Protocols:** [[09_PROTOCOLS/09_PROTOCOLS_MOC|09_PROTOCOLS_MOC]] — Workflows follow protocols

## Workflow Architecture

- Workflows are multi-step execution sequences that transform inputs to outputs through defined, governed stages — each stage is an atomic unit with preconditions, effects, and validation gates.
- The canonical workflow pattern is: `TRIGGER → PRECONDITIONS → RETRIEVE → TRANSFORM → VALIDATE → COMMIT/EXPORT → VERIFY → STORE LEARNING`.
- Workflows are registered artifacts with RSCF blocks — they carry `state`, `claim_class`, `provenance`, and `scope` metadata like all AMOS artifacts.
- Workflow execution is observed by the [[20_OPERATIONS/20_OPERATIONS_MOC|20_OPERATIONS]] plane, producing execution traces and learning records.

## Workflow Validation

- Every workflow must pass validation before activation: structural integrity (all stages defined), dependency closure (all referenced skills and agents exist), and authority verification (the workflow's mutation class is within the autonomous envelope).
- Validation follows the 10-stage pipeline — see [[25_COGNITIVE_MATRIX/11_VALIDATION/11_VALIDATION_MOC|11_VALIDATION_MOC]] — with depth determined by the workflow's consequence and irreversibility scores.
- Failed workflow validation produces a failure memory record (GMEF-mandatory, non-erasable) — see [[02_KERNEL/05_MEMORY/05_MEMORY_MOC|05_MEMORY_MOC]].

## Workflow-Agent-Skill Binding (1:1:1)

- Each workflow stage binds to exactly one agent and one skill — the `1:1:1` binding principle ensures traceability and accountability.
- An agent may participate in multiple stages of a workflow, but each stage has exactly one primary agent and one primary skill.
- The binding is enforced at commit time: a stage without a valid agent-skill binding cannot execute — see [[02_KERNEL/07_AUTHORITY/07_AUTHORITY_MOC|07_AUTHORITY_MOC]].
- Skill activation is routed through the domain skill router — see [[23_OPERATING_MODEL/23_OPERATING_MODEL_MOC|23_OPERATING_MODEL_MOC]] — ensuring the activated skill matches the current operating domain.

## Inter-Plane Connections (Extended)

- **Agents:** [[06_AGENTS/06_AGENTS_MOC|06_AGENTS_MOC]] — Workflows bind agents to execution stages.
- **Skills:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] — Workflows compose skills into multi-step sequences.
- **Runtime:** [[04_RUNTIME/04_RUNTIME_README|04_RUNTIME_README]] — Runtime executes workflow stages as ticks and steps.
- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] — Control plane gates each workflow stage transition.

______________________________________________________________________


## Workflows Plane README

### Architecture

AMOS workflows are declarative process definitions that orchestrate skills, agents, and tools across the AMOS OS. Every workflow is bound to one or more agents and depends on one or more skills.

### Workflow registry
- **696 canonical workflow definitions** in `.devin/workflows/`
- **0 validation errors**, 0 broken agent dependencies
- **1 master index** + operational workflows
- **Consistent `amos-*` naming** (all renamed in audit pass)

### Workflow lifecycle
```
DEFINE → VALIDATE → BIND → DEPLOY → EXECUTE → MONITOR → REPAIR → RETIRE
```

### Workflow types
- **RSCF workflows**: epistemic validation workflows (context-compaction, interprocedural-callgraph, etc.)
- **Domain workflows**: domain-specific process definitions (C01-C12 + specialist)
- **Operational workflows**: vault operations, audit, sync, maintenance
- **Research workflows**: arXiv ingestion, SOTA research, knowledge harvest

### SOTA workflow orchestration
- **Temporal**: durable execution; workflow-as-code; automatic retry, compensation, saga; SDKs (Go, Python, TS)
- **Airflow**: DAG-based; operators; XCom; scheduling; Apache project; extensive provider ecosystem
- **Dagster**: asset-based; software-defined assets; partitions; backfilling; data platform
- **Prefect**: Python-native; flow/task; deployment; work pools; events
- **Argo Workflows**: Kubernetes-native; DAG; templates; CI/CD; data pipelines

### AMOS Integration
- **Workflows MOC**: [[08_WORKFLOWS/08_WORKFLOWS_MOC|08_WORKFLOWS_MOC]]
- **Skills MOC**: [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
- **Agents MOC**: [[06_AGENTS/06_AGENTS_MOC|06_AGENTS_MOC]]
- **RSCF workflows**: [[08_WORKFLOWS/amos-context-compaction-recoverability-rscf-workflow|Context Compaction RSCF Workflow]], [[08_WORKFLOWS/amos-interprocedural-callgraph-rscf-workflow|Interprocedural Callgraph RSCF Workflow]]

### Invariants
1. `DEFINED != VALIDATED` — workflow definition does not guarantee validation
2. `VALIDATED != DEPLOYED` — validation does not guarantee deployment
3. All workflow claims must cite provenance (definition, agents, skills, validation status)
4. `CAPABILITY != AUTHORITY` — workflow capability does not grant execution authority


**Parent:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
