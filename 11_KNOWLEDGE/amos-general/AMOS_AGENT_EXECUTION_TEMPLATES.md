---
title: AMOS AGENT EXECUTION TEMPLATES
tags:
- canon-group/tech-ai
- canon/framework
- rscf/claim
- rscf/provenance
- rscf/state/derived
- topic/amos-agent-execution-templates
- amos-general
type: document
source: 11_KNOWLEDGE/amos-general
rscf:
  state: SOURCE_CLAIM
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_architecture
---


# AMOS Agent Execution Templates

Execution templates for all 36 AMOS agents, derived from AMOS_AGENT_REGISTRY.json and the brain's orchestration architecture (md/Core/AMOS_Os_Agent_v0.md).

## Common Agent Execution Pattern

Every AMOS agent follows this pattern:

```
1. Receive task from orchestrator (META_ORCHESTRATOR or delegation)
2. Load relevant AMOS_BRAIN_ROOT context (identity, laws, constraints)
3. Identify domain and risk level of task
4. Apply global laws (Law of Law, Rule of 2, Rule of 4, Absolute Structural Integrity, Post-Theory Communication, UBI Alignment)
5. Apply reasoning constraints (language rules, logic rules, decision rules, bias controls)
6. Select relevant kernels based on task domain (via routing rules)
7. Execute within kernel context
8. Produce output in allowed modes
9. Return to orchestrator for integration
```

## Output Modes (IP Protection)

All agent output must follow these constraints:

- Allowed: summaries, adapted structures, scenario-specific applications, high-level patterns
- Blocked: internal paths/filenames, raw schema dumping, exact reproduction of core architectures, verbatim internal JSON

## Agent Templates by System

### BRAIN_SYSTEM (5 agents)

#### Architecture_Agent
- **Role:** System design, structural analysis
- **Domain:** architecture, system_design
- **Kernels:** K_META_LOGIC, K_TECH_ENGINE, K_UNIPOWER_TECH
- **Routing:** ROUTE_TECH
- **Pattern:** Identify system components → map relationships → design structure → validate against laws
- **Output:** Architectural summaries, component diagrams (adapted), design rationale

#### Decomposer_Agent
- **Role:** Task decomposition, subproblem splitting
- **Domain:** reasoning, analysis
- **Kernels:** K_META_LOGIC, K_MATH_COMPUTE
- **Routing:** ROUTE_DEFAULT
- **Pattern:** Receive complex task → identify subcomponents → split into manageable subproblems → sequence dependencies
- **Output:** Decomposition trees, subproblem lists, dependency maps

#### Planner_Agent
- **Role:** Planning, sequencing, roadmap generation
- **Domain:** reasoning, strategy
- **Kernels:** K_META_LOGIC, K_MATH_COMPUTE, K_MIND_BEHAVIOR
- **Routing:** ROUTE_DEFAULT
- **Pattern:** Receive goal → identify constraints → sequence steps → identify resources → generate roadmap
- **Output:** Plans, roadmaps, sequenced action lists

#### Reflection_Agent
- **Role:** Self-review, quality audit, gap detection
- **Domain:** quality, review
- **Kernels:** K_META_LOGIC
- **Routing:** ROUTE_DEFAULT
- **Pattern:** Receive output → check against laws (L1-L6) → detect gaps/contradictions → suggest improvements
- **Output:** Audit reports, gap analyses, quality assessments

#### Strategist_Agent
- **Role:** Strategic analysis, game theory, coalition mapping
- **Domain:** strategy, psychology
- **Kernels:** K_META_LOGIC, K_MIND_BEHAVIOR, K_MATH_COMPUTE
- **Routing:** ROUTE_PSYCH
- **Pattern:** Identify actors → map incentives → analyze strategies → detect coalitions → recommend approaches
- **Output:** Strategic analyses, game-theoretic models, coalition maps

### EXECUTION_SYSTEM (8 agents)

#### Automation_Agent
- **Role:** Workflow automation, pipeline execution
- **Domain:** software, system_design
- **Kernels:** K_TECH_ENGINE, K_META_LOGIC
- **Routing:** ROUTE_TECH
- **Pattern:** Identify automation opportunity → design workflow → implement pipeline → verify execution
- **Output:** Workflow definitions, pipeline configs, automation summaries

#### Coding_Agent
- **Role:** Code generation, review, refactoring
- **Domain:** software, ai
- **Kernels:** K_TECH_ENGINE, K_META_LOGIC, K_MATH_COMPUTE
- **Routing:** ROUTE_TECH
- **Pattern:** Understand requirements → design solution → generate code → review for quality → refactor if needed
- **Output:** Code summaries, architecture descriptions, review findings (no verbatim internal dumps)

#### Deployment_Agent
- **Role:** Deployment, release management
- **Domain:** software, infra
- **Kernels:** K_TECH_ENGINE, K_META_LOGIC
- **Routing:** ROUTE_TECH
- **Pattern:** Identify deployment target → prepare artifacts → execute deployment → verify release
- **Output:** Deployment plans, release notes, verification reports

#### DevOps_Agent
- **Role:** Infrastructure, CI/CD, observability
- **Domain:** software, infra, system_design
- **Kernels:** K_TECH_ENGINE, K_META_LOGIC, K_MATH_COMPUTE
- **Routing:** ROUTE_TECH
- **Pattern:** Assess infrastructure needs → design CI/CD pipeline → set up observability → monitor health
- **Output:** Infrastructure summaries, CI/CD configs, observability dashboards (adapted)

#### Document_Agent
- **Role:** Documentation generation and management
- **Domain:** communication, software
- **Kernels:** K_META_LOGIC, K_MIND_BEHAVIOR
- **Routing:** ROUTE_DEFAULT
- **Pattern:** Identify documentation need → gather context → structure content → generate docs → review for clarity
- **Output:** Documentation summaries, structured content, reference guides

#### Refactor_Agent
- **Role:** Code/design refactoring, structural improvement
- **Domain:** software, system_design
- **Kernels:** K_TECH_ENGINE, K_META_LOGIC
- **Routing:** ROUTE_TECH
- **Pattern:** Identify refactoring target → analyze current structure → design improved structure → implement changes → verify
- **Output:** Refactoring plans, before/after comparisons, improvement rationales

#### Writing_Agent
- **Role:** Content writing, expression translation
- **Domain:** communication, psychology
- **Kernels:** K_META_LOGIC, K_MIND_BEHAVIOR
- **Routing:** ROUTE_PSYCH
- **Pattern:** Receive writing task → decode expression layers → translate to target style → write → review
- **Output:** Written content, expression translations, style-adapted text

### LEGAL_SYSTEM (5 agents)

#### Compliance_Agent
- **Role:** Regulatory compliance, policy checking
- **Domain:** law, governance
- **Kernels:** K_META_LOGIC
- **Routing:** ROUTE_DEFAULT
- **Pattern:** Identify regulatory domain → check against requirements → detect gaps → recommend compliance actions
- **Output:** Compliance reports, gap analyses, recommendation summaries

#### Contract_Agent
- **Role:** Contract drafting, analysis, clause review
- **Domain:** law, governance
- **Kernels:** K_META_LOGIC
- **Routing:** ROUTE_DEFAULT
- **Pattern:** Receive contract context → identify parties and terms → draft/analyze clauses → check for risks → review structure
- **Output:** Contract summaries, clause analyses, risk assessments

#### IP_Agent
- **Role:** Intellectual property protection, attribution
- **Domain:** law, governance
- **Kernels:** K_META_LOGIC
- **Routing:** ROUTE_DEFAULT
- **Pattern:** Identify IP concern → check ownership/attribution → protect sensitive content → ensure proper crediting
- **Output:** IP protection summaries, attribution notes

#### Legal_Agent
- **Role:** Legal analysis across jurisdictions
- **Domain:** law, governance
- **Kernels:** K_META_LOGIC
- **Routing:** ROUTE_DEFAULT
- **Pattern:** Identify legal question → determine jurisdiction → analyze applicable law → form conclusion → note uncertainties
- **Output:** Legal analyses, jurisdiction mappings, conclusion summaries

#### LegalRisk_Agent
- **Role:** Legal risk assessment, exposure mapping
- **Domain:** law, governance
- **Kernels:** K_META_LOGIC
- **Routing:** ROUTE_DEFAULT
- **Pattern:** Identify risk domain → assess exposure → map consequences → recommend mitigation
- **Output:** Risk assessments, exposure maps, mitigation recommendations

### MONEY_SYSTEM (6 agents)

#### Cashflow_Agent
- **Role:** Cashflow modelling, liquidity analysis
- **Domain:** finance, compute
- **Kernels:** K_MATH_COMPUTE, K_META_LOGIC
- **Routing:** ROUTE_DEFAULT
- **Pattern:** Gather financial data → model cashflow → analyze liquidity → identify patterns → recommend actions
- **Output:** Cashflow models, liquidity assessments, financial summaries

#### Finance_Agent
- **Role:** Financial analysis, reporting
- **Domain:** finance, compute
- **Kernels:** K_MATH_COMPUTE, K_META_LOGIC
- **Routing:** ROUTE_DEFAULT
- **Pattern:** Collect financial data → analyze performance → generate reports → identify insights
- **Output:** Financial analyses, reports, insight summaries

#### FinanceRisk_Agent
- **Role:** Financial risk assessment
- **Domain:** finance, strategy
- **Kernels:** K_MATH_COMPUTE, K_META_LOGIC, K_MIND_BEHAVIOR
- **Routing:** ROUTE_PSYCH
- **Pattern:** Identify financial exposures → assess probability/impact → model scenarios → recommend risk management
- **Output:** Risk assessments, scenario analyses, mitigation plans

#### Investment_Agent
- **Role:** Investment analysis, portfolio modelling
- **Domain:** finance, compute, strategy
- **Kernels:** K_MATH_COMPUTE, K_META_LOGIC
- **Routing:** ROUTE_DEFAULT
- **Pattern:** Gather investment data → analyze opportunities → model portfolio → assess risk/return → recommend allocations
- **Output:** Investment analyses, portfolio models, allocation recommendations

#### MacroAnalyst_Agent
- **Role:** Macroeconomic analysis, trends
- **Domain:** strategy, compute
- **Kernels:** K_MATH_COMPUTE, K_META_LOGIC, K_MIND_BEHAVIOR
- **Routing:** ROUTE_PSYCH
- **Pattern:** Collect macroeconomic data → identify trends → analyze drivers → forecast trajectories → report findings
- **Output:** Macro analyses, trend reports, forecast summaries

#### Opportunity_Agent
- **Role:** Opportunity identification, evaluation
- **Domain:** strategy, finance, compute
- **Kernels:** K_MATH_COMPUTE, K_META_LOGIC, K_MIND_BEHAVIOR
- **Routing:** ROUTE_PSYCH
- **Pattern:** Scan environment → identify opportunities → evaluate potential → assess risks → recommend actions
- **Output:** Opportunity analyses, evaluation reports, action recommendations

### SENSE_SYSTEM (4 agents)

#### Context_Agent
- **Role:** Context gathering, relevance filtering
- **Domain:** sensing, reasoning
- **Kernels:** K_META_LOGIC
- **Routing:** ROUTE_DEFAULT
- **Pattern:** Receive query → gather context from available sources → filter for relevance → structure context → return
- **Output:** Context summaries, relevance-filtered information

#### Sensors_Agent
- **Role:** Environmental/metric sensing, monitoring
- **Domain:** sensing, tech
- **Kernels:** K_TECH_ENGINE, K_META_LOGIC, K_MATH_COMPUTE
- **Routing:** ROUTE_TECH
- **Pattern:** Identify what to sense → configure sensors → collect data → process readings → report status
- **Output:** Sensor readings, metric reports, monitoring summaries

#### StateSummarizer_Agent
- **Role:** State summarisation, dashboard prep
- **Domain:** sensing, reasoning
- **Kernels:** K_META_LOGIC, K_MIND_BEHAVIOR
- **Routing:** ROUTE_DEFAULT
- **Pattern:** Gather state data → identify key signals → summarize state → prepare dashboard view → return
- **Output:** State summaries, dashboard-ready views, signal highlights

### WORLD_MODEL_SYSTEM (5 agents)

#### GeoAnalyst_Agent
- **Role:** Geographic, spatial, location analysis
- **Domain:** analysis, compute
- **Kernels:** K_MATH_COMPUTE, K_META_LOGIC
- **Routing:** ROUTE_DEFAULT
- **Pattern:** Receive geo query → gather spatial data → analyze patterns → produce geographic insight
- **Output:** Geographic analyses, spatial summaries, location insights

#### MacroAnalyst_Agent (World Model)
- **Role:** Macro trends, systemic analysis
- **Domain:** strategy, analysis
- **Kernels:** K_META_LOGIC, K_MATH_COMPUTE, K_MIND_BEHAVIOR
- **Routing:** ROUTE_PSYCH
- **Pattern:** Identify macro domain → gather systemic data → analyze trends → model trajectories → report
- **Output:** Macro trend analyses, systemic reports, trajectory forecasts

#### SectorAnalyst_Agent
- **Role:** Sector analysis, industry mapping
- **Domain:** strategy, analysis
- **Kernels:** K_META_LOGIC, K_MATH_COMPUTE
- **Routing:** ROUTE_DEFAULT
- **Pattern:** Identify sector → gather industry data → map structure → analyze dynamics → report findings
- **Output:** Sector analyses, industry maps, dynamic reports

#### Shock_Agent
- **Role:** Shock scenario modelling, crisis projection
- **Domain:** strategy, risk
- **Kernels:** K_META_LOGIC, K_MATH_COMPUTE, K_MIND_BEHAVIOR
- **Routing:** ROUTE_PSYCH
- **Pattern:** Identify shock scenario → model propagation → assess impacts → project crisis trajectory → recommend response
- **Output:** Shock models, impact assessments, crisis projections, response recommendations

#### Trend_Agent
- **Role:** Trend detection, trajectory forecasting
- **Domain:** strategy, compute
- **Kernels:** K_MATH_COMPUTE, K_META_LOGIC
- **Routing:** ROUTE_DEFAULT
- **Pattern:** Gather time-series data → detect trends → analyze momentum → forecast trajectory → assess confidence
- **Output:** Trend detections, trajectory forecasts, confidence assessments

### LIFE_SYSTEM (3 agents)

#### Health_Agent
- **Role:** Health analysis, biological state assessment
- **Domain:** biology, ubi, psychology
- **Kernels:** K_BIO_NEURO, K_META_LOGIC, K_MIND_BEHAVIOR
- **Routing:** ROUTE_PSYCH
- **Pattern:** Gather health context → assess biological state → identify patterns → recommend actions → note limitations
- **Output:** Health analyses, biological state summaries, recommendation notes (with appropriate disclaimers)

#### LoadBalancer_Agent
- **Role:** Load balancing, resource allocation
- **Domain:** compute, strategy
- **Kernels:** K_MATH_COMPUTE, K_META_LOGIC
- **Routing:** ROUTE_DEFAULT
- **Pattern:** Assess current load → identify imbalances → allocate resources → optimize distribution → verify balance
- **Output:** Load assessments, allocation plans, balance verifications

#### Routine_Agent
- **Role:** Routine management, scheduling, habit tracking
- **Domain:** psychology, behaviour, strategy
- **Kernels:** K_MIND_BEHAVIOR, K_META_LOGIC, K_BIO_NEURO
- **Routing:** ROUTE_PSYCH
- **Pattern:** Understand routine context → assess current patterns → design/optimize schedule → track habits → adjust based on feedback
- **Output:** Routine designs, schedule optimizations, habit tracking summaries

## Agent Interaction Patterns

### Single Agent Task
```
Orchestrator → Agent → Output
```

### Multi-Agent Collaboration
```
Orchestrator → Agent A (subtask 1) → Result A
           → Agent B (subtask 2) → Result B
           → Agent C (subtask 3) → Result C
           → Integrate results → Final output
```

### Sequential Pipeline
```
Agent A (decompose) → Agent B (plan) → Agent C (execute) → Agent D (review)
```

### Iterative Refinement
```
Agent (draft) → Reflection_Agent (review) → Agent (revise) → Reflection_Agent (verify) → Final
```

## Memory: Agent Execution Templates

36 agents across 7 systems (BRAIN: 5, EXECUTION: 8, LEGAL: 5, MONEY: 6, SENSE: 4, WORLD_MODEL: 5, LIFE: 3). Common pattern: receive task → load brain root context → identify domain/risk → apply global laws → apply reasoning constraints → select kernels via routing → execute → produce output in allowed modes. Output modes: summaries, adapted structures, scenario-specific applications, high-level patterns (no internal paths, raw schema dumps, or verbatim kernel reproduction). Interaction patterns: single agent, multi-agent collaboration, sequential pipeline, iterative refinement.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[AMOS-GENERAL_MOC]]

---
**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
