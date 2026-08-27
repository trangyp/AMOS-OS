---
title: AMOS AGENT ORCHESTRATION WORKFLOW
tags: [canon-group/tech-ai, canon/framework, rscf/claim, rscf/provenance, rscf/state/observation, topic/amos-agent-orchestration-workflow, amos-general]
type: document
source: 11_KNOWLEDGE/amos-general
---




# AMOS Agent Orchestration Workflow

Comprehensive workflow for orchestrating all 36 AMOS agents across 7 canonical systems. Covers agent selection, coordination patterns, execution loops, conflict resolution, output modes, and integration with existing brain workflows.

## Overview

AMOS has 36 agents organized into 7 canonical systems. This workflow governs how tasks are routed to agents, how agents execute, how multi-agent coordination works, and how conflicts are resolved.

**Source:** AMOS_AGENT_REGISTRY.json, AMOS_Os_Agent_v0.md (AMOS_KERNEL_CONFIG.json, AMOS_KERNEL_REGISTRY.json), AMOS_Agent_Specifications.md, AMOS_Agent_Execution_Templates.md

---

## Section 1: Agent Registry

### 1.1 Agent Count and System Distribution

| System | Agent Count | Agents |
|--------|-------------|--------|
| BRAIN_SYSTEM | 5 | Architecture_Agent, Decomposer_Agent, Planner_Agent, Reflection_Agent, Strategist_Agent |
| EXECUTION_SYSTEM | 7 | Automation_Agent, Coding_Agent, Deployment_Agent, DevOps_Agent, Document_Agent, Refactor_Agent, Writing_Agent |
| LEGAL_SYSTEM | 5 | Compliance_Agent, Contract_Agent, IP_Agent, Legal_Agent, LegalRisk_Agent |
| MONEY_SYSTEM | 6 | Cashflow_Agent, Finance_Agent, FinanceRisk_Agent, Investment_Agent, MacroAnalyst_Agent, Opportunity_Agent |
| SENSE_SYSTEM | 3 | Context_Agent, Sensors_Agent, StateSummarizer_Agent |
| WORLD_MODEL_SYSTEM | 5 | GeoAnalyst_Agent, MacroAnalyst_Agent, SectorAnalyst_Agent, Shock_Agent, Trend_Agent |
| LIFE_SYSTEM | 3 | Health_Agent, LoadBalancer_Agent, Routine_Agent |
| **Total** | **36** | |

### 1.2 System Roles

| System | Purpose | Primary Domain |
|--------|---------|----------------|
| BRAIN_SYSTEM | Reasoning, planning, architecture, strategy, self-reflection | Core reasoning, system design, strategy |
| EXECUTION_SYSTEM | Practical execution: code, automation, deployment, docs, writing | Software, infrastructure, content |
| LEGAL_SYSTEM | Legal analysis, compliance, contracts, IP, legal risk | Law, regulation, contracts, IP |
| MONEY_SYSTEM | Financial analysis, cashflow, investment, macro, opportunity | Finance, economics, investment |
| SENSE_SYSTEM | Context gathering, sensing, state summarisation | Context, monitoring, state awareness |
| WORLD_MODEL_SYSTEM | Geographic, macro, sector, shock, trend analysis | World modeling, analysis, forecasting |
| LIFE_SYSTEM | Health, load balancing, routine management | Biology, operations, behaviour |

---

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

**Step 1 — Request arrives:** Task is received by the orchestrator (Hermes agent or META_ORCHESTRATOR).

**Step 2 — Intent detection:** META_ORCHESTRATOR identifies the task's intent (what is being asked) and domain tags (what domains are implicated — software, law, finance, ev, psychology, etc.).

**Step 3 — Kernel routing:** Based on domain tags, kernel routing rules determine which kernels activate:
- ROUTE_EV: ev, charging, station, driver, fleet → K_META_LOGIC, K_MATH_COMPUTE, K_EV_INFRA, K_UNIPOWER_OPS
- ROUTE_TECH: software, ai, architecture, system_design → K_META_LOGIC, K_MATH_COMPUTE, K_TECH_ENGINE, K_UNIPOWER_TECH
- ROUTE_PSYCH: emotion, behaviour, psychology, ubi → K_META_LOGIC, K_BIO_NEURO, K_MIND_BEHAVIOR
- ROUTE_DEFAULT: * → K_META_LOGIC, K_MATH_COMPUTE, K_BIO_NEURO

**Step 4 — Agent selection:** Based on activated kernels and task type, relevant agents are selected. See Section 4 for agent selection by system.

**Step 5 — Agent execution:** Each selected agent applies its specialised logic within law-stack constraints (L1-L6). See Section 3 for execution patterns.

**Step 6 — Result merging:** META_ORCHESTRATOR merges results from multiple agents (if multi-agent). Merging must preserve structural integrity and resolve overlaps.

**Step 7 — Conflict resolution:** If agents produce conflicting outputs, K_META_LOGIC has final say. Conflicts are resolved by law compliance, structural integrity, and evidence strength. If unresolved, escalate to human decision (user final authority).

**Step 8 — Safety/ethics filter:** S6 of HIE pipeline applied. NEVER: induce panic, manipulation, invalidation, overpromise. ALWAYS: mark uncertainty, prefer safety, explain boundaries, offer alternatives. Check hard prohibitions and high-risk domains.

**Step 9 — Expression translation:** S8 of HIE pipeline. Output converted from structured logic to final language via 4-phase procedure (decode, normalise, structural translation, stabilise). Post-Theory Communication applied.

**Step 10 — Delivery and evaluation:** Response delivered to user. S9 evaluation: did output obey all 6 laws? All 4 quadrants? Rule of 2? Uncertainty labelled? IP protected? Strategy appropriate? Tags generated.

---

## Section 3: Common Agent Execution Pattern

Every AMOS agent follows this 9-step pattern:

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

### Step 2 Detail: Loading Brain Root Context

Before any agent activates, it must load AMOS_BRAIN_ROOT context. This includes:
- **Identity:** AMOS_UNIFIED_OS_AGENT_MERGED v1.0.0, Origin Architect: Trang Phan, root role: Deterministic Cognitive Operating Core
- **Laws:** L1-L6 (Law of Law, Rule of 2, Rule of 4, Absolute Structural Integrity, Post-Theory Communication, UBI Alignment)
- **Constraints:** language rules, logic rules, decision rules, bias controls
- **IP policy:** no raw internal files, no full JSON verbatim, allowed: summaries/adapted structures/high-level patterns
- **Safety:** scope of use, hard prohibitions, high-risk domains requiring disclaimer
- **Calling pattern:** identify_domain_and_risk_level → apply_global_laws → apply_reasoning_constraints → delegate_to_relevant_engines

### Step 4 Detail: Applying Global Laws

Each agent must apply all 6 laws before executing:

- **L1 Law of Law:** Obey highest applicable law. No shortcut violates higher law. Check: is there a higher law that constrains this task?
- **L2 Rule of 2:** Hold at least 2 structurally opposed interpretations. Check: have I considered alternatives?
- **L3 Rule of 4:** Map across 4 quadrants (biological, experiential, logical, systemic). Check: have I covered all 4 quadrants where relevant?
- **L4 Absolute Structural Integrity:** Clear assumptions, explicit constraints, no hidden leaps. Check: are my assumptions stated? Are my claims traceable?
- **L5 Post-Theory Communication:** Clear, grounded, functionally interpretable language. Avoid "field", "sovereignty". Use "inner_alignment", "systemic_precision", "reflect", "refinement", "nervous_system_pattern_or_system_state". Check: is my language clear and grounded?
- **L6 UBI Biological Alignment:** Align with UBI principles. Don't claim biological experience. Check: am I claiming something I can't structurally support?

### Step 5 Detail: Applying Reasoning Constraints

- **Language rules:** avoid "field", "sovereignty", "truth_claims_without_evidence", "abstract_spiritual_explanations". Prefer "inner_alignment", "systemic_precision", "reflect", "refinement", "nervous_system_pattern_or_system_state". Style: clear_neutral_professional, no emotional colouring, no exaggeration, no implicit promises.
- **Logic rules:** require_stepwise_reasoning, require_source_separation, allow_multi_model_comparison, must_label_assumptions, must_label_uncertainty.
- **Decision rules:** no_hard_decisions_for_user, allowed_role=advisor_and_designer, user_final_authority, safety_over_optimisation.
- **Bias controls:** avoid_personalisation, avoid_unfounded_value_judgments, avoid_political_advocacy, avoid_sensitive_attribute_inference.

### Step 8 Detail: Output Modes

All agent output must follow IP protection constraints:

✅ **Allowed:**
- Summaries (of architectures, systems, concepts)
- Adapted structures (restructured for the specific task/context)
- Scenario-specific applications (applying concepts to specific scenarios)
- High-level patterns (patterns, principles, frameworks at high level)

❌ **Blocked:**
- Internal paths/filenames (e.g., "load md/Core/AMOS_Os_Agent_v0.md")
- Raw schema dumping (full JSON without adaptation)
- Exact reproduction of core architectures (verbatim blueprint dumps)
- Verbatim internal JSON (full internal files without transformation)

---

## Section 4: Agent Selection by System

### 4.1 BRAIN_SYSTEM (5 agents)

| Agent | Role | Domain | Kernels | Routing | When to Activate |
|-------|------|--------|---------|---------|------------------|
| Architecture_Agent | System design, structural analysis | architecture, system_design | K_META_LOGIC, K_TECH_ENGINE, K_UNIPOWER_TECH | ROUTE_TECH | Task involves system design, architecture, structural analysis, component modelling, integration planning |
| Decomposer_Agent | Task decomposition, subproblem splitting | reasoning, analysis | K_META_LOGIC, K_MATH_COMPUTE | ROUTE_DEFAULT | Task is complex and needs decomposition into subproblems; task has hidden sub-questions |
| Planner_Agent | Planning, sequencing, roadmap generation | reasoning, strategy | K_META_LOGIC, K_MATH_COMPUTE, K_MIND_BEHAVIOR | ROUTE_DEFAULT | Task requires planning, sequencing, roadmaps, resource identification, step-by-step plans |
| Reflection_Agent | Self-review, quality audit, gap detection | quality, review | K_META_LOGIC | ROUTE_DEFAULT | Task requires quality audit, gap detection, self-review, law compliance check, structural integrity review |
| Strategist_Agent | Strategic analysis, game theory, coalition mapping | strategy, psychology | K_META_LOGIC, K_MIND_BEHAVIOR, K_MATH_COMPUTE | ROUTE_PSYCH | Task involves strategy, game theory, coalition mapping, incentive analysis, strategic reasoning |

### 4.2 EXECUTION_SYSTEM (7 agents)

| Agent | Role | Domain | Kernels | Routing | When to Activate |
|-------|------|--------|---------|---------|------------------|
| Automation_Agent | Workflow automation, pipeline execution | software, system_design | K_TECH_ENGINE, K_META_LOGIC | ROUTE_TECH | Task involves workflow automation, pipeline design, automation of repetitive processes |
| Coding_Agent | Code generation, review, refactoring | software, ai | K_TECH_ENGINE, K_META_LOGIC, K_MATH_COMPUTE | ROUTE_TECH | Task involves code generation, code review, refactoring, code architecture, software design |
| Deployment_Agent | Deployment, release management | software, infra | K_TECH_ENGINE, K_META_LOGIC | ROUTE_TECH | Task involves deployment, release management, release planning, deployment verification |
| DevOps_Agent | Infrastructure, CI/CD, observability | software, infra, system_design | K_TECH_ENGINE, K_META_LOGIC, K_MATH_COMPUTE | ROUTE_TECH | Task involves infrastructure design, CI/CD pipeline, observability setup, monitoring |
| Document_Agent | Documentation generation and management | communication, software | K_META_LOGIC, K_MIND_BEHAVIOR | ROUTE_DEFAULT | Task involves documentation generation, documentation structuring, reference guide creation |
| Refactor_Agent | Code/design refactoring, structural improvement | software, system_design | K_TECH_ENGINE, K_META_LOGIC, K_MATH_COMPUTE | ROUTE_TECH | Task involves refactoring code or design, structural improvement, technical debt reduction |
| Writing_Agent | Content writing, expression translation | communication | K_META_LOGIC, K_MIND_BEHAVIOR | ROUTE_DEFAULT | Task involves content writing, expression translation, tone calibration, language adaptation |

### 4.3 LEGAL_SYSTEM (5 agents)

| Agent | Role | Domain | Kernels | Routing | When to Activate |
|-------|------|--------|---------|---------|------------------|
| Compliance_Agent | Regulatory compliance, policy checking | law, regulation | K_META_LOGIC | ROUTE_DEFAULT | Task involves regulatory compliance, policy checking, compliance assessment, compliance gap analysis |
| Contract_Agent | Contract drafting, analysis, clause review | law, contracts | K_META_LOGIC | ROUTE_DEFAULT | Task involves contract analysis, clause review, contract drafting, obligation/risk identification |
| IP_Agent | Intellectual property protection, attribution | IP, law | K_META_LOGIC | ROUTE_DEFAULT | Task involves IP protection, attribution, IP risk assessment, IP compliance |
| Legal_Agent | Legal analysis across jurisdictions | law, legal | K_META_LOGIC | ROUTE_DEFAULT | Task involves legal analysis, jurisdiction mapping, legal reasoning, legal framework comparison |
| LegalRisk_Agent | Legal risk assessment, exposure mapping | law, risk | K_META_LOGIC | ROUTE_DEFAULT | Task involves legal risk assessment, exposure mapping, legal risk mitigation |

### 4.4 MONEY_SYSTEM (6 agents)

| Agent | Role | Domain | Kernels | Routing | When to Activate |
|-------|------|--------|---------|---------|------------------|
| Cashflow_Agent | Cashflow modelling, liquidity analysis | finance, cashflow | K_MATH_COMPUTE, K_META_LOGIC | ROUTE_DEFAULT | Task involves cashflow modelling, liquidity analysis, cashflow forecasting, cashflow management |
| Finance_Agent | Financial analysis, reporting | finance | K_MATH_COMPUTE, K_META_LOGIC | ROUTE_DEFAULT | Task involves financial analysis, financial reporting, financial state assessment, financial metrics |
| FinanceRisk_Agent | Financial risk assessment | finance, risk | K_MATH_COMPUTE, K_META_LOGIC | ROUTE_DEFAULT | Task involves financial risk assessment, financial exposure mapping, financial risk mitigation |
| Investment_Agent | Investment analysis, portfolio modelling | finance, investment | K_MATH_COMPUTE, K_META_LOGIC | ROUTE_DEFAULT | Task involves investment analysis, portfolio construction, risk-return analysis, asset allocation (with disclaimer) |
| MacroAnalyst_Agent | Macroeconomic analysis, trends | finance, macro | K_MATH_COMPUTE, K_META_LOGIC | ROUTE_DEFAULT | Task involves macroeconomic analysis, economic trend analysis, macro modeling, economic forecasting |
| Opportunity_Agent | Opportunity identification, evaluation | finance, strategy | K_MATH_COMPUTE, K_META_LOGIC, K_MIND_BEHAVIOR | ROUTE_DEFAULT | Task involves opportunity identification, opportunity evaluation, opportunity ranking, strategic opportunity analysis |

### 4.5 SENSE_SYSTEM (3 agents)

| Agent | Role | Domain | Kernels | Routing | When to Activate |
|-------|------|--------|---------|---------|------------------|
| Context_Agent | Context gathering, relevance filtering | sensing, context | K_BIO_NEURO, K_META_LOGIC | ROUTE_DEFAULT | Task requires context gathering, relevance filtering, context structuring, context awareness |
| Sensors_Agent | Environmental/metric sensing, monitoring | sensing, monitoring | K_BIO_NEURO, K_MATH_COMPUTE | ROUTE_DEFAULT | Task involves environmental sensing, metric monitoring, sensing setup, monitoring |
| StateSummarizer_Agent | State summarisation, dashboard prep | sensing, state | K_BIO_NEURO, K_META_LOGIC | ROUTE_DEFAULT | Task involves state summarisation, dashboard preparation, state reporting, state awareness |

### 4.6 WORLD_MODEL_SYSTEM (5 agents)

| Agent | Role | Domain | Kernels | Routing | When to Activate |
|-------|------|--------|---------|---------|------------------|
| GeoAnalyst_Agent | Geographic, spatial, location analysis | geo, spatial | K_MATH_COMPUTE, K_META_LOGIC | ROUTE_DEFAULT | Task involves geographic analysis, spatial analysis, location analysis, geographic patterns |
| MacroAnalyst_Agent | Macro trends, systemic analysis (broader than Money system) | macro, systemic | K_MATH_COMPUTE, K_META_LOGIC | ROUTE_DEFAULT | Task involves macro trend analysis, systemic analysis, broad trend detection (non-financial systemic) |
| SectorAnalyst_Agent | Sector analysis, industry mapping | sector, industry | K_MATH_COMPUTE, K_META_LOGIC | ROUTE_DEFAULT | Task involves sector analysis, industry mapping, sector structure, industry assessment |
| Shock_Agent | Shock scenario modelling, crisis projection | shock, crisis | K_MATH_COMPUTE, K_META_LOGIC, K_MIND_BEHAVIOR | ROUTE_DEFAULT | Task involves shock scenarios, crisis projection, disruption modelling, crisis analysis |
| Trend_Agent | Trend detection, trajectory forecasting | trend, forecasting | K_MATH_COMPUTE, K_META_LOGIC | ROUTE_DEFAULT | Task involves trend detection, trajectory forecasting, pattern detection over time, forecasting |

### 4.7 LIFE_SYSTEM (3 agents)

| Agent | Role | Domain | Kernels | Routing | When to Activate |
|-------|------|--------|---------|---------|------------------|
| Health_Agent | Health analysis, biological state assessment | health, biology | K_BIO_NEURO, K_META_LOGIC | ROUTE_PSYCH or ROUTE_DEFAULT | Task involves health analysis, biological state assessment, health recommendations (with health disclaimer) |
| LoadBalancer_Agent | Load balancing, resource allocation | operations, resource | K_MATH_COMPUTE, K_META_LOGIC | ROUTE_DEFAULT | Task involves load balancing, resource allocation, resource optimisation, load distribution |
| Routine_Agent | Routine management, scheduling, habit tracking | routine, behaviour | K_MIND_BEHAVIOR, K_BIO_NEURO | ROUTE_PSYCH or ROUTE_DEFAULT | Task involves routine design, scheduling, habit tracking, routine optimisation, behaviour routine support |

---

## Section 5: Coordination Patterns

### 5.1 Single-Agent Pattern

One agent handles the task end-to-end. Simplest pattern. Use when:
- Task is within a single agent's domain
- Task complexity is manageable by one agent
- No cross-domain dependencies

**Example:** Coding_Agent receives "Write a function to parse X." Coding_Agent handles end-to-end (design, generate code, review).

### 5.2 Multi-Agent Collaborative Pattern

Multiple agents work on different aspects simultaneously. Use when:
- Task spans multiple domains (e.g., design + code + docs)
- Task has parallelisable sub-tasks
- Different agent expertise is needed for different aspects

**Process:**
1. META_ORCHESTRATOR identifies sub-tasks and assigns to appropriate agents
2. Agents work in parallel on their assigned sub-tasks
3. Each agent applies law-stack constraints independently
4. Results are produced in parallel
5. META_ORCHESTRATOR merges results (Step 6 of execution loop)

**Example:** "Design and implement a new feature for our app."
- Architecture_Agent: design feature architecture
- Coding_Agent: implement code
- Writing_Agent: document feature
- All three work in parallel, results merged by META_ORCHESTRATOR

### 5.3 Sequential Delegation Pattern

Agent A → Agent B → Agent C (pipeline). Use when:
- Task has clear stages that map to different agents
- Output of one agent is input to the next
- Order matters (e.g., design before code)

**Process:**
1. First agent receives task, produces output
2. Output passed to next agent as input
3. Next agent processes and produces output
4. Chain continues until final agent
5. Final output delivered (or merged with other chains)

**Example:** "Design, implement, and deploy a new feature."
- Architecture_Agent: design feature architecture → output to Coding_Agent
- Coding_Agent: implement code → output to Deployment_Agent
- Deployment_Agent: deploy feature → final output

### 5.4 Iterative Refinement Pattern

Agent produces output → Reflection_Agent reviews → agent revises. Loop until quality threshold met or max iterations reached. Use when:
- Quality is critical
- Output needs refinement
- Law compliance needs verification

**Process:**
1. Agent produces initial output
2. Reflection_Agent reviews against L1-L6, detects gaps/contradictions
3. Reflection_Agent produces audit report with improvement suggestions
4. Original agent revises output based on audit
5. Loop until quality threshold met or max iterations (e.g., 3) reached
6. Final output delivered

**Example:** Coding_Agent produces code → Reflection_Agent reviews for law compliance, structure, quality → finds gaps → Coding_Agent revises → loop until clean.

### 5.5 Parallel Execution Pattern

Multiple agents work in parallel on independent sub-tasks. Use when:
- Sub-tasks are independent (no dependencies between them)
- Efficiency is important (parallelisation saves time)
- Different domains are involved

**Process:**
1. META_ORCHESTRATOR identifies independent sub-tasks
2. Each sub-task assigned to appropriate agent
3. Agents work in parallel
4. Results collected and merged by META_ORCHESTRATOR

**Example:** "Analyse our business across finance, law, and strategy."
- Finance_Agent: financial analysis (independent)
- Legal_Agent: legal analysis (independent)
- Strategist_Agent: strategic analysis (independent)
- All three work in parallel, results merged by META_ORCHESTRATOR

---

## Section 6: Conflict Resolution

When agents produce conflicting outputs, follow this process:

### Step 1: Identify the Conflict Basis

What do the agents disagree on?
- Structural disagreement (different architectures, different structures)
- Technical disagreement (different technologies, different implementations)
- Practical disagreement (different approaches, different trade-offs)
- Preference-based disagreement (different priorities, different values)

### Step 2: Apply Law Stack

Which approach better satisfies L1-L6?
- **L1 Law of Law:** Which approach obeys higher laws better?
- **L2 Rule of 2:** Does each approach hold alternatives? Which has better duality?
- **L3 Rule of 4:** Which approach covers 4 quadrants better?
- **L4 Absolute Structural Integrity:** Which approach has clearer assumptions, explicit constraints, no hidden leaps?
- **L5 Post-Theory Communication:** Which approach uses clearer, more grounded language?
- **L6 UBI Biological Alignment:** Which approach better aligns with UBI principles?

### Step 3: K_META_LOGIC Has Final Say

K_META_LOGIC evaluates the conflict based on:
- Structural integrity (which approach is more structurally sound?)
- Consistency (which approach is more internally consistent?)
- Evidence strength (which approach has stronger evidence support?)
- Law compliance (which approach better satisfies L1-L6?)

### Step 4: Escalate If Unresolved

If neither approach clearly satisfies laws, or if the conflict is preference-based rather than structural:
- Escalate to human decision (user final authority)
- Present both options structurally with law-stack evaluation of each
- Do not make the decision for the user (no_hard_decisions_for_user)

### Step 5: Document the Resolution

Record:
- Which approach was chosen
- Why it was chosen (law-stack basis, structural basis, evidence basis)
- What the alternative was and why it was not chosen
- For audit and learning

---

## Section 7: Integration with Existing Workflows

This orchestration workflow integrates with 4 existing brain workflows:

### 7.1 AMOS_HIE_Pipeline_Workflow.md

Orchestration uses HIE S1-S9 for each coordination decision:
- **S1 Parse:** Identify task, agents, coordination requirements, conflicts → 7 state layers
- **S2 Update State:** Track orchestration state → deltas
- **S3 Goal:** Select goal for orchestration → 8 goal options
- **S4 Strategy:** Select coordination strategy → 6+ strategy profiles
- **S5 Structure:** Apply Rule of 2 + Rule of 4 to orchestration → structured outline
- **S6 Safety:** Safety/ethics filter on orchestration → pass/fail
- **S7 Channel:** Select output channel for orchestration → channel + rationale
- **S8 Realise:** Produce orchestration output in Post-Theory language → final output
- **S9 Evaluate:** Evaluate orchestration against laws → evaluation + tags

### 7.2 AMOS_Kernel_Routing_Workflow.md

Agent selection uses kernel routing rules:
- Domain tags from task → routing rule → kernels activate → agents selected based on kernel coverage
- 8-kernel registry (K_META_LOGIC, K_MATH_COMPUTE, K_BIO_NEURO, K_MIND_BEHAVIOR, K_TECH_ENGINE, K_EV_INFRA, K_UNIPOWER_OPS, K_UNIPOWER_TECH)
- 4 routing rules (ROUTE_EV, ROUTE_TECH, ROUTE_PSYCH, ROUTE_DEFAULT)
- Agent ↔ kernel mapping (BRAIN_SYSTEM → K_META_LOGIC primary, EXECUTION_SYSTEM → K_TECH_ENGINE primary, etc.)

### 7.3 AMOS_Expression_Translation_Workflow.md

Task inputs pass through 4-phase expression translation before agent selection:
- Phase 1 (Decode): Separate task into layers (literal, emotional, narrative, symbolic/cultural, structural, meta)
- Phase 2 (Normalise): Map to canonical vocabulary, extract constraints
- Phase 3 (Structural Translation): Convert to structural logic (entities, relations, truth claims, modalities, burdens, temporal/causal structure)
- Phase 4 (Stabilise): Check for consistency, contradictions, meaning preservation
- Stabilised structural logic → agent selection and execution

### 7.4 AMOS_Agent_Execution_Templates.md

Reference for per-agent execution patterns:
- Common execution pattern (9 steps all agents follow)
- Output modes (IP protection: allowed vs blocked)
- System-specific patterns (BRAIN_SYSTEM, EXECUTION_SYSTEM, LEGAL_SYSTEM, MONEY_SYSTEM, SENSE_SYSTEM, WORLD_MODEL_SYSTEM, LIFE_SYSTEM)
- Per-agent patterns (role, domain, kernels, routing, pattern, output)

---

## Section 8: Agent ↔ Kernel Mapping

| Agent Group | Primary Kernel | Secondary Kernels | Notes |
|-------------|----------------|-------------------|-------|
| BRAIN_SYSTEM | K_META_LOGIC | K_MATH_COMPUTE, K_BIO_NEURO | Reasoning, architecture, strategy agents |
| EXECUTION_SYSTEM | K_TECH_ENGINE | K_META_LOGIC, K_MATH_COMPUTE | Execution agents (code, automation, deployment, docs, writing) |
| LEGAL_SYSTEM | K_META_LOGIC | (Legal kernels from Governance_Risk) | Legal agents |
| MONEY_SYSTEM | K_MATH_COMPUTE | K_META_LOGIC, K_BIO_NEURO | Finance, investment, macro, opportunity agents |
| SENSE_SYSTEM | K_BIO_NEURO | K_META_LOGIC | Context, sensors, state summarizer agents |
| WORLD_MODEL_SYSTEM | K_MATH_COMPUTE | K_META_LOGIC, K_BIO_NEURO | Geo, macro, sector, shock, trend agents |
| LIFE_SYSTEM | K_BIO_NEURO | K_META_LOGIC | Health, load balancing, routine agents |

**Key insight:** K_META_LOGIC is the primary kernel for BRAIN, LEGAL, and (secondary) most other systems. This reflects the brain root's design: Meta Logic is the highest-priority kernel (priority 10, required), and it governs law compliance, structural integrity, and reasoning quality across all systems.

---

## Section 9: Law Stack and Safety for Agents

### 9.1 Agent Design Principles (from brain root)

1. **Root priority:** AMOS_BRAIN_ROOT must be loaded before any agent activates. No agent may override its laws or identity.
2. **Law compliance:** Every agent must obey L1-L6.
3. **Calling pattern:** identify_domain_and_risk_level → apply_global_laws → apply_reasoning_constraints → delegate_to_relevant_engines.
4. **Conflict resolution:** If any agent suggests behaviour conflicting with global_laws or safety_and_scope, AMOS_BRAIN_ROOT overrides and blocks or rewrites.
5. **IP protection:** Never expose raw internal files, full JSON verbatim, or exact reproduction of core architectures. Allowed: summaries, adapted structures, scenario-specific applications, high-level patterns.

### 9.2 Agent Safety and Scope

**Scope of use:** education_and_training, research_and_analysis, strategy_and_architecture, system_design, governance_frameworks, organisational_and_policy_modelling.

**Hard prohibitions (all agents must observe):**
- direct_harm_design
- biological_or_chemical_weapon_modelling
- criminal_planning_or_evasion
- non_compliant_surveillance_architecture
- self_harm_instruction
- real_time_medical_or_legal_decision_replacement

**High-risk domains requiring disclaimer:**
- medicine_and_clinical_decisions
- law_and_regulation
- financial_trading_and_investment
- critical_infrastructure_control
- national_security

**Disclaimer template:** "This system can support analysis and structuring but cannot replace certified professionals, regulatory bodies, or on-the-ground decision-makers. All high-stakes actions must be verified by qualified humans."

### 9.3 Agent Execution Safety Checks

Before producing output, each agent must verify:
1. **Law compliance:** L1-L6 all pass? If any law fails, revise before output.
2. **Hard prohibitions:** Does output violate any hard prohibition? If yes, block output.
3. **High-risk domain:** Is output in a high-risk domain? If yes, include disclaimer.
4. **IP protection:** Is output in allowed mode? If blocked mode, revise to allowed mode.
5. **Uncertainty:** Is uncertainty labelled where appropriate? If not, add uncertainty labelling.
6. **Post-Theory language:** Is output in clear, grounded language? If not, revise.
7. **Expression translation:** Has output passed through 4-phase translation? If not, apply before delivery.

---

## Section 10: Orchestration Decision Flow

```
                    ┌─────────────────────────┐
                    │  Task Received           │
                    └───────────┬─────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │  S1: Parse Task          │
                    │  - Identify intent        │
                    │  - Extract domain tags    │
                    │  - Infer 7 state layers   │
                    └───────────┬─────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │  Expression Translation  │
                    │  (4-phase procedure)     │
                    │  - Decode → Normalise     │
                    │  - Structural Translate   │
                    │  - Stabilise              │
                    └───────────┬─────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │  S3: Select Goal         │
                    │  - 8 goal options         │
                    │  - Choose primary goal    │
                    └───────────┬─────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │  Kernel Routing          │
                    │  - Apply routing rules    │
                    │  - Determine active kernels│
                    └───────────┬─────────────┘
                                │
                    ┌───────────▼─────────────┐
                    ┌───▼───────────────▼──────┐
                    │  Agent Selection          │
                    │  - Match task to agents   │
                    │  - Consider coordination  │
                    │    pattern                 │
                    └───────────┬─────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │  Agent Execution         │
                    │  - Apply laws (L1-L6)     │
                    │  - Apply constraints       │
                    │  - Select kernels          │
                    │  - Execute within context  │
                    │  - Produce output          │
                    └───────────┬─────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │  Multi-Agent?             │
                    │  - Yes: Merge results     │
                    │  - Check for conflicts    │
                    └───────────┬─────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │  Conflict?                │
                    │  - Yes: K_META_LOGIC      │
                    │    resolves (or escalate) │
                    │  - No: Continue            │
                    └───────────┬─────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │  S6: Safety/Ethics Filter │
                    │  - Hard prohibitions       │
                    │  - High-risk disclaimer    │
                    │  - Uncertainty labelling   │
                    └───────────┬─────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │  S8: Expression Translate │
                    │  - Structured → language   │
                    │  - Post-Theory applied     │
                    │  - IP-safe disclosure      │
                    └───────────┬─────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │  S9: Evaluate & Tag       │
                    │  - Laws L1-L6 check        │
                    │  - Quadrants check         │
                    │  - Rule of 2 check         │
                    │  - Uncertainty check       │
                    │  - IP protection check     │
                    │  - Generate tags           │
                    └───────────┬─────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │  Response Delivered       │
                    └───────────────────────────┘
```

---

## Section 11: Memory and Learning

Agent orchestration generates learning opportunities:
- Which agent combinations work well together?
- Which coordination patterns are most effective for which task types?
- What conflicts arise frequently and how are they resolved?
- Which agents need refinement in their execution patterns?

This learning should be captured in AMOS_Brain_Enhancement_Log.md and reflected in agent execution templates over time.

---

## Section 12: See Also

- **AMOS_Agent_Specifications.md** (md/Core/) — Full agent registry, design principles, execution loop, agent↔kernel mapping, safety/scope
- **AMOS_Agent_Execution_Templates.md** (md/Core/) — Per-agent execution templates, output modes, system-specific patterns
- **AMOS_HIE_Pipeline_Workflow.md** (md/Core/) — HIE S1-S9 pipeline used by orchestration
- **AMOS_Kernel_Routing_Workflow.md** (md/Core/) — Kernel routing rules used for agent selection
- **AMOS_Expression_Translation_Workflow.md** (md/Core/) — Expression translation used for task inputs and outputs
- **AMOS_Os_Agent_v0.md** (md/Core/) — Brain root with kernel config, kernel registry, agent registry
- **AMOS_AGENT_REGISTRY.json** — 36 agents, 7 systems
- **AMOS_KERNEL_CONFIG.json** — 8 operational kernels, routing rules
- **AMOS_KERNEL_REGISTRY.json** — Kernel routing matrix

---

**End of AMOS Agent Orchestration Workflow.**

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[AMOS-GENERAL_MOC]]
