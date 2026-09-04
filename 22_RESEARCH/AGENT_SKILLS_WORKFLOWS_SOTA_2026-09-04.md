---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Agent Skills Workflows Sota 2026 09 04
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

# Agent Skills and Workflows — SOTA Research Dossier

## Boundary

This dossier records external arXiv research relevant to `07_SKILLS` and `26_WORKFLOWS`.
It is not AMOS canon and does not establish that reported benchmark results transfer to AMOS.

```text
PAPER CLAIM != AMOS VALIDATION
BENCHMARK RESULT != UNIVERSAL VALIDITY
REUSABLE SKILL != SAFE SKILL
WORKFLOW GRAPH != EXECUTED WORKFLOW
```

## Skill ecosystem findings

### Agent Skills ecosystem analysis — arXiv:2602.08004
Reported: analysis of 40,285 public skills; strong category concentration and intent-level redundancy; many skills remain within ordinary prompt budgets; some expose state-changing/system-level actions.

AMOS implications:
- registry size is not capability diversity;
- intent redundancy should be measured separately from identity count;
- state-changing skills need stronger effect typing and authority gates;
- context footprint is a governed runtime resource.

### SkillCommit — arXiv:2608.15165
Reported: online skill evolution; preserve case-specific patches first; retrieve related skills; use cross-instance replay and mechanism checks; generalize only if behavior across constituent cases is preserved.

AMOS implications:
- semantic similarity alone is insufficient for merging;
- scope expansion needs behavioral compatibility evidence;
- local patches, generalized skills and superseded variants remain separately recoverable.

### SkillCraft — arXiv:2603.00718
Reported: benchmark for acquiring/reusing higher-level tool compositions; evaluates structural/compositional difficulty and cross-task reuse; reports major efficiency gains from saved/reused skills on its benchmark.

AMOS implications:
- skill quality includes composition/reuse, not only isolated success;
- saved skills need applicability, invalidation and dependency checks;
- efficiency should be measured with correctness and safety.

### SkillOps — arXiv:2605.13716
Reported: skill libraries as self-maintaining software ecosystems; introduces library-level skill technical debt; typed skill contracts and hierarchical ecosystem graphs; diagnoses utility, compatibility, risk and validation.

AMOS implications:
- `07_SKILLS` needs library-health governance;
- technical debt includes redundancy, stale dependencies, validation gaps, unsafe effects and retrieval pollution;
- maintenance is distinct from task-time skill use;
- graph structure enables impact analysis and selective invalidation.

## Workflow findings

### Agent Workflow survey — arXiv:2508.01186
Reported: classifies workflows by functional capabilities and architectural features; highlights planning, collaboration, API/tool integration, orchestration flows, specification languages, optimization, security, standardization and multimodality.

AMOS implications:
- functional purpose and orchestration topology should be separate axes;
- standardization/versioning and security are first-class workflow concerns.

### Flow — arXiv:2501.07834
Reported: workflows as activity-on-vertex graphs; dynamic task reallocation; modularity, parallelism, dependency complexity and error tolerance.

AMOS implications:
- topology should be explicit/versioned;
- topology changes need dependency, validation and rollback semantics;
- parallelism follows dependency independence, not assumption.

### VeriMAP — arXiv:2510.17109
Reported: verification-aware planning; task decomposition with explicit dependencies and passing criteria; verification functions for intermediate outputs and handoffs.

AMOS implications:
- acceptance criteria belong in the plan before execution;
- handoff verification differs from final validation;
- planner-defined validation is not automatically independent evidence.

### ALAS — arXiv:2511.03094
Reported: separates planning from non-circular validation; uses versioned execution logs and restore points; localized repair; explicit retry, timeout, backoff, idempotency, compensation and loop guards.

AMOS implications:
- workflow IR should expose versioned execution state;
- repair targets the smallest affected subgraph;
- retry/idempotency/compensation belong in the workflow contract.

## Derived AMOS requirements

### Skills
```text
IDENTITY
→ CONTRACT
→ PAYLOAD/HOST BINDING
→ BEHAVIORAL VALIDATION
→ TASK ADMISSION
→ OBSERVED UTILITY
→ LIBRARY HEALTH
→ PATCH / ABSTRACT / QUARANTINE / SUPERSEDE
```

Library-level dimensions:
utility; behavioral compatibility; dependency compatibility; redundancy/overlap; context footprint; retrieval quality; composition quality; validation coverage; effect/security risk; freshness; technical debt; supersession lineage.

### Workflows
```text
OBJECTIVE
→ TYPED GRAPH / STATE MACHINE
→ PRECONDITIONS
→ DEPENDENCY + PARALLELISM ANALYSIS
→ VALIDATION FUNCTIONS
→ EXECUTION
→ VERSIONED OBSERVATION
→ LOCAL REPAIR / COMPENSATION
→ FINALITY / RECEIPT
```

## Research-to-AMOS firewall

These findings remain `SOURCE_CLAIM` and `DERIVED/AMOS_MODEL` until AMOS-specific implementations are versioned, executed, tested and receipt-bound.

## Source registry
- arXiv:2602.08004 — Agent Skills: A Data-Driven Analysis of Claude Skills for Extending Large Language Model Functionality
- arXiv:2608.15165 — SkillCommit: Evolving Agent Skills through Behaviorally Validated Scope Expansion
- arXiv:2603.00718 — SkillCraft: Can LLM Agents Learn to Use Tools Skillfully?
- arXiv:2605.13716 — SkillOps: Managing LLM Agent Skill Libraries as Self-Maintaining Software Ecosystems
- arXiv:2508.01186 — A Survey on Agent Workflow -- Status and Future
- arXiv:2501.07834 — Flow: A Modular Approach to Automated Agentic Workflow Generation
- arXiv:2510.17109 — Verification-Aware Planning for Multi-Agent Systems
- arXiv:2511.03094 — ALAS: Transactional and Dynamic Multi-Agent LLM Planning

---
RSCF-NODE
node_id: agent_skills_workflows_sota_2026_09_04
node_type: research_dossier
path: 22_RESEARCH/AGENT_SKILLS_WORKFLOWS_SOTA_2026-09-04.md
claim_class: SOURCE_CLAIM
