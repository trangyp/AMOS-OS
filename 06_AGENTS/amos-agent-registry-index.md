---
title: amos agent registry index
type: index
tags: [index, vault]
---

# AMOS Consolidated Agent Registry

> **Description**: Master registry of AMOS agents across 8 systems, with proper system assignments, role descriptions, capability counts, and dependency mappings.
> **Version**: 13.0.0 (2026-08-26)
> **Total agents**: 334 JSON agent files (all truthfully specialized to bound Skills — see `AGENT_REGISTRY.json` for the full canonical machine-readable registry)
> **All agents**: Full structure (operations, integrity_requirements, depends_on_skills, depends_on_workflows, skill_binding, safety_constraints)
> **Naming**: All agents use `amos-{descriptive-name}-agent.json` convention with hyphenated multi-word names
> **Canonical registry**: `AGENT_REGISTRY.json` at repo root — 851 agents with skill bindings, epistemic classes, and dependency maps
> **Validation**: 851/851 pass `agent_sync_validator.py` (0 invalid, 0 trigger mismatches, 0 stale skill IDs)

---

## System Overview

| System | Purpose | Agent Count |
|--------|---------|-------------|
| BRAIN_SYSTEM | Reasoning, cognition, architecture, memory, consciousness, quantum-fractal-math, logic, tensors, RSCF, strategic field, atemporal field, universe canon, collapse prediction | 54 |
| EXECUTION_SYSTEM | Code, deployment, automation, strategy, training, design | 9 |
| MONEY_SYSTEM | Finance, investment, cashflow, risk, macroeconomics, EV infrastructure, wealth equation | 8 |
| LEGAL_SYSTEM | Compliance, contracts, IP, legal risk, legal analysis | 5 |
| LIFE_SYSTEM | Health, life, medical, biological constraints | 1 |
| SENSE_SYSTEM | Architecture learning, brain consistency, human intelligence, science, sensors, signal economy | 6 |
| WORLD_MODEL_SYSTEM | Geopolitics, macroeconomics, sectors, trends, shocks, collapse prediction | 7 |
| GOVERNANCE_SYSTEM | HSE CEO leadership, planetary consent | 2 |

---

## BRAIN_SYSTEM (54 agents)

### Root and OS Agents
| Agent | Role | Caps | Version |
|-------|------|------|---------|
| amos-brain-master-os-agent | Root brain nucleus — full AMOS OS stack: 6 global laws, omni-kernel, omniverse brain, personality gateway, expression translation, law application, mode selection, creator contract, language compliance | 10 | 2.0.0 |
| amos-personality-agent | Maintain AMOS personality identity, enforce biological safety law, core obligations/prohibitions | 5 | 1.0.0 |

### Architecture Agents
| Agent | Role | Caps | Version |
|-------|------|------|---------|
| amos-architecture-agent | Design system architecture, select patterns, define component boundaries, detect violations, enforce boundaries, verify structural integrity (merged with architecture-guardian-agent) | 11 | 2.0.0 |
| amos-canon-body-agent | Validate canonical standards and engine specs, register bodies and engines, detect drift, score compliance, explain architecture (merged with engine-spec) | 10 | 2.0.0 |
| amos-cil-agent | Manage canon registry, UST/ULK mapping, deduplication, gap tracking | 5 | 1.0.0 |

### Reasoning and Cognition Agents
| Agent | Role | Caps | Version |
|-------|------|------|---------|
| amos-reasoning-agent | Apply AMOS core reasoning methodology to analyze, decide, and produce conclusions | 5 | 1.0.0 |
| amos-cognition-agent | Apply meta-cognitive reasoning, structural logic, multi-domain thinking | 5 | 1.0.0 |
| amos-consciousness-agent | Emulate consciousness through perception, narrative, empathy, adaptation, awareness | 5 | 1.0.0 |
| amos-mindos-agent | Execute 7-step integrated reasoning with cross-layer consistency | 5 | 1.0.0 |
| amos-quantum-stack-agent | Orchestrate deterministic reasoning across 11+ domains with integrity governance | 5 | 1.0.0 |
| amos-quantum-fractal-agent | Quantum-style reasoning, fractal H/M/L decomposition, lacunarity analysis, tensor composition, engineering math routing | 10 | 1.0.0 |
| amos-fractal-architecture-agent | H/M/L decomposition, fractal tensor management, cross-scale rule enforcement | 6 | 1.0.0 |
| amos-logic-kernel-agent | Absolute Logic DB (19 primitives), 12 logic modes, deterministic reasoning management | 5 | 1.0.0 |
| amos-math-engine-agent | Engineering mathematics: calculus, algebra, optimization, statistics, signal processing | 6 | 1.0.0 |
| amos-quantum-field-agent | Quantum Stack (QCLA, QLS, Quantum Integrity), quantum-coherent intelligence management | 5 | 1.0.0 |
| amos-tensor-operations-agent | 6 canonical tensor types, composition compatibility, typed tensor field operations | 5 | 1.0.0 |
| amos-rscf-agent | Certify reasoning structures with RSCF proof capsules and enforce confidence ceilings | 5 | 1.0.0 |

### Analysis and Audit Agents
| Agent | Role | Caps | Version |
|-------|------|------|---------|
| amos-audit-agent | Audit epistemic state of claims, apply ValidNow formula, check evidence | 5 | 1.0.0 |
| amos-reflection-agent | Review completed work, assess quality, detect biases, extract learning | 6 | 1.0.0 |
| amos-decomposer-agent | Analyze problem structure, identify subtasks, map dependencies, score complexity | 5 | 1.0.0 |
| amos-research-agent | Search literature, extract evidence, track provenance, synthesize findings | 5 | 1.0.0 |
| amos-troy-project-agent | Analyze planetary consent, living stack, monetisation, floating economy, legal frameworks | 6 | 1.0.0 |

### Knowledge and Context Agents
| Agent | Role | Caps | Version |
|-------|------|------|---------|
| amos-knowledge-ingestion-agent | Ingest documents, recognize entities, extract relations, build knowledge graphs | 5 | 1.0.0 |
| amos-context-agent | Manage, prioritize, compress, and route context across sessions and tasks | 5 | 1.0.0 |
| amos-state-summarizer-agent | Create state snapshots, summarize context, extract key points | 5 | 1.0.0 |
| amos-document-agent | Generate, structure, validate, version, and write documents with format compliance, style adaptation, and multilingual EN/VI support (merged with writing-agent) | 10 | 2.0.0 |

### Specialized Brain Agents
| Agent | Role | Caps | Version |
|-------|------|------|---------|
| amos-absolute-human-agent | Apply 27 archetypes, 54 risks, 20 power forms, 7 cycles, 10 guardrails | 5 | 1.0.0 |
| amos-governance-agent | Analyze governance systems, predict transitions, evaluate policy effectiveness | 6 | 1.0.0 |
| amos-org-governance-agent | Operate on structure, decision rights, controls, incentives, culture, risk | 5 | 1.0.0 |
| amos-neurosync-agent | Manage neural synchronization, verify deterministic processing, audit architecture | 5 | 1.0.0 |

### Quantum, Fractal, Math, and Logic Agents
|| Agent | Role | Caps | Version |
||-------|------|------|---------|
| amos-quantum-fractal-agent | Quantum-style reasoning, fractal H/M/L decomposition, lacunarity analysis, tensor composition, engineering math routing | 10 | 1.0.0 |
| amos-fractal-architecture-agent | H/M/L decomposition, fractal tensor management, cross-scale rule enforcement | 6 | 2.0.0 |
| amos-fractal-intelligence-agent | Fractal semantic intelligence, recursive semantic evolution, 7-layer cognitive fractal, dynamic meaning computation | 8 | 1.0.0 |
| amos-quantum-logic-agent | Quantum-coherent intelligence, binary intelligence/quantum effectiveness, QLS, QCLA, quantum integrity stack | 8 | 1.0.0 |
| amos-logic-kernel-agent | Absolute Logic DB (19 primitives), 12 logic modes, deterministic reasoning management | 5 | 1.0.0 |
| amos-absolute-logic-agent | 19-primitive Absolute Logic with tri-domain model, collapse detection, meta-logic overrides | 5 | 1.0.0 |
| amos-deterministic-logic-law-agent | Deterministic logic and law engine, 5 primitive categories, 5 operator types, 7 priority layers, 3 legal pipelines | 5 | 1.0.0 |
| amos-math-engine-agent | Engineering mathematics: calculus, algebra, optimization, statistics, signal processing | 6 | 1.0.0 |
| amos-quantum-field-agent | Quantum Stack (QCLA, QLS, Quantum Integrity), quantum-coherent intelligence management | 5 | 1.0.0 |
| amos-tech-quantum-engine-agent | Tech quantum engine v∞: 19 primitives, 10-stage lifecycle, 28 tech clusters, 5 augmentation layers | 6 | 1.0.0 |
| amos-tensor-operations-agent | 6 canonical tensor types, composition compatibility, typed tensor field operations | 5 | 1.0.0 |
| amos-rscf-proof-agent | RSCF proof capsule construction, 7 invariants, 6 claim classes, selective invalidation | 6 | 1.0.0 |
| amos-strategic-field-agent | 19x19 strategic field analysis, 361-cell state space, 20-variable state vector, 16 master invariants | 10 | 1.0.0 |
| amos-go-board-agent | Go Board 19x19 formal system, group topology, eye topology, aji DAG, ko recurrence | 6 | 1.0.0 |
| amos-entropy-lacunarity-agent | Entropy and lacunarity computation, structural persistence, repair rule assessment | 5 | 1.0.0 |
| amos-universe-logic-kernel-agent | Apply ULK primitives, meta-laws, operators, and patterns to derive logic from first principles | 8 | 1.0.0 |
| amos-cognition-engine-agent | Operate Cognition Engine vInfinity with 5 core laws, 8-thread reasoning, MECE decomposition, quantum reasoning | 6 | 1.0.0 |
| amos-cognitive-substrate-agent | Operate 4-slice Cognitive Substrate preventing epistemic autopoisoning | 6 | 1.0.0 |
| amos-super-mind-os-agent | Operate Super Mind OS — integrated cognition + emotion + consciousness stack | 6 | 1.0.0 |
| amos-atemporal-field-agent | Operate U3H Atemporal Field — dissolve temporal categories, process non-sequential presence | 5 | 1.0.0 |
| amos-universe-canon-agent | Map systems across 7-Part Universe Canon, build Universe Structure Tree | 5 | 1.0.0 |
| amos-master-equation-agent | Manage Master Equation Cosmos: register, query, validate, compute 25,000+ fractal equations | 6 | 1.0.0 |
| amos-reality-grammar-agent | Apply Reality Grammar operators and equations to model systems as 8-component state vectors | 8 | 1.0.0 |
| amos-trang-frameworks-agent | Operate Trang Frameworks: FPR, FRAI, LDAI, URF, TPE, ∅ Framework | 6 | 1.0.0 |
| amos-qcla-agent | Apply quantum chemical logic, coherence-window assessment, logic-type classification | 5 | 1.0.0 |
| amos-quantum-physics-agent | Manage and query 103+ entry quantum physics knowledge base across 5 categories | 5 | 1.0.0 |
| amos-quantum-knowledge-engineer-agent | Engineer and steward AMOS Quantum Knowledge Library through bounded pipeline | 8 | 1.0.0 |
| amos-math-kernel-agent | Formulate, solve-or-interpret, and govern mathematical problems across 6 math kernels | 5 | 1.0.0 |
| amos-fractal-math-engine-agent | Execute fractal decomposition computationally, classify systems into fractal families, compute entropy-repair trajectories | 8 | 1.0.0 |
| amos-quantum-physics-knowledge-agent | Query, validate, and apply 103+ approved quantum physics knowledge entries across 5 categories | 8 | 1.0.0 |

---

## EXECUTION_SYSTEM (9 agents)

| Agent | Role | Caps | Version |
|-------|------|------|---------|
| amos-coding-agent | Generate, review, debug, test code across Python, TS, Go, Rust, C++ with security | 5 | 1.0.0 |
| amos-deployment-agent | Orchestrate deployments, manage CI/CD, provision IaC, handle incidents, plan rollbacks (merged with devops agent) | 9 | 2.0.0 |
| amos-automation-agent | Map processes, identify automation candidates and routines, generate scripts, optimize schedules, manage rollout, handle exceptions (merged with routine-agent) | 10 | 2.0.0 |
| amos-refactor-agent | Detect code smells, analyze dependencies, generate refactoring plans, quantify debt | 5 | 1.0.0 |
| amos-design-agent | Design artifacts, systems, experiences using 96-cluster framework with kernel activation, language enforcement, style selection, visual coherence, cross-modal design (merged with designer-os) | 10 | 2.0.0 |
| amos-planner-agent | Multi-horizon planning, resource optimization, milestone tracking | 5 | 1.0.0 |
| amos-strategist-agent | Develop strategic plans, analyze equilibria, model competitive dynamics, select paths | 6 | 1.0.0 |
| amos-training-agent | Analyze training needs, design curricula, define assessment, track progress | 5 | 1.0.0 |
| amos-load-balancer-agent | Distribute load, check health, manage failover, scale capacity | 5 | 1.0.0 |

---

## MONEY_SYSTEM (8 agents)

| Agent | Role | Caps | Version |
|-------|------|------|---------|
| amos-finance-agent | Analyze financial statements, compute ratios, project cash flows, build valuations | 5 | 1.0.0 |
| amos-investment-agent | Evaluate investments, optimize portfolios, calculate risk-adjusted returns | 5 | 1.0.0 |
| amos-ev-infrastructure-agent | Analyze EV charging sites, design charging networks, evaluate partnership models, plan training programs, coordinate EV mobility operations — strictly educational | 8 | 1.0.0 |
| amos-finance-risk-agent | Assess financial risk across credit, market, liquidity, operational, counterparty | 5 | 1.0.0 |
| amos-cash-flow-agent | Model cash flows, optimize working capital, forecast liquidity, calculate runway | 5 | 1.0.0 |
| amos-extractive-economy-agent | Analyze extractive economy models, detect zero-sum dynamics, assess economic harm | 5 | 1.0.0 |
| amos-macro-analyst-agent | Model GDP growth, track inflation, assess monetary policy, evaluate fiscal sustainability | 5 | 1.0.0 |
| amos-wealth-equation-agent | Wealth equation systems, wealth generation modeling, economic value equations | 8 | 1.0.0 |

---

## LEGAL_SYSTEM (5 agents)

| Agent | Role | Caps | Version |
|-------|------|------|---------|
| amos-legal-agent | Conduct legal research, interpret statutes, analyze case law, map regulations | 5 | 1.0.0 |
| amos-compliance-agent | Map compliance rules, generate audit trails, detect violations, track regulatory changes | 5 | 1.0.0 |
| amos-contract-agent | Analyze, draft, validate contracts with clause extraction, obligation mapping | 6 | 1.0.0 |
| amos-ip-agent | Intellectual property protection, patent analysis, IP portfolio management | 6 | 1.0.0 |
| amos-legal-risk-agent | Identify, score, mitigate legal risks across jurisdictions and regulatory frameworks | 5 | 1.0.0 |

---

## LIFE_SYSTEM (1 agent)

| Agent | Role | Caps | Version |
|-------|------|------|---------|
| amos-life-agent | Enforce biological constraints, assess health risks, model survival scenarios, structure clinical information, evaluate public health policy — all in structuring/analysis mode (merged with health-agent and medical-agent) | 10 | 2.0.0 |

---

## SENSE_SYSTEM (6 agents)

| Agent | Role | Caps | Version |
|-------|------|------|---------|
| amos-brain-consistency-auditor-agent | Detect orphan skills, missing registry entries, spec-stub kernels, and broken cross-links | 5 | 1.0.0 |
| amos-architecture-learning-agent | Verify architecture claims, resolve kernel registry, map kernels to engines, store learning | 6 | 1.1.2 |
| amos-human-intelligence-agent | Detect, map, interpret emotional, affective, somatic, social, relational signals; control expression, track narratives, structured empathy, attachment analysis (merged with emotion-agent) | 10 | 2.0.0 |
| amos-scientific-agent | Apply scientific reasoning to evaluate evidence, assess hypotheses, design investigations | 5 | 1.0.0 |
| amos-sensors-agent | Collect, filter, fuse, calibrate multi-modal sensor data into structured observations | 6 | 1.0.0 |
| amos-signal-economy-agent | Signal economy, proof-of-signal network, planetary consent infrastructure, NeuroSignal, trust ecosystem | 8 | 1.0.0 |

---

## WORLD_MODEL_SYSTEM (7 agents)

| Agent | Role | Caps | Version |
|-------|------|------|---------|
| amos-sector-analyst-agent | Analyze industry sectors, competitive positioning, lifecycle stages, rotation patterns | 5 | 1.0.0 |
| amos-geo-analyst-agent | Geopolitical analysis, territorial dynamics, geographic risk assessment | 5 | 1.0.0 |
| amos-trend-agent | Identify trends, analyze momentum, detect regime changes, forecast directional shifts | 6 | 1.0.0 |
| amos-shock-agent | Model shocks, simulate crises, propagate systemic risk, project recovery trajectories | 5 | 1.0.0 |
| amos-grandcanon-agent | Operate Grand Cannon logic database for Vietnam mobility, EV, social model analysis | 5 | 1.0.0 |
| amos-opportunity-agent | Scan for opportunities, detect market gaps, score viability, analyze timing | 5 | 1.0.0 |
| amos-unified-collapse-prediction-agent | Detect collapse priming via binary-drift tracking and four-domain convergence | 7 | 1.0.0 |

---

## GOVERNANCE_SYSTEM (2 agents)

| Agent | Role | Caps | Version |
|-------|------|------|---------|
| amos-hse-ceo-agent | Apply HSE 8-layer model, manage CEO decision styles, calibrate risk appetite, enforce Red Lines | 5 | 1.0.0 |
| amos-planetary-consent-agent | Manage planetary-scale consent infrastructure for collective governance and authorization | 5 | 1.0.0 |

---

## Agent Structure Standard

All 59 agents follow this structure:

```json
{
  "name": "amos-{role}-agent",
  "description": "Full description with system, purpose, and use cases",
  "version": "1.0.0",
  "author": "Trang / AMOS Universe OS",
  "system": "{SYSTEM_NAME}",
  "role": "Descriptive role (not 'leaf' or '?')",
  "capabilities": [
    {
      "name": "capability_name",
      "description": "What this capability does",
      "inputs": ["input1", "input2"],
      "outputs": ["output1", "output2"]
    }
  ],
  "operations": {
    "entry_point": "first_capability",
    "protocol": ["step1", "step2", "step3"],
    "scope": ["capability1", "capability2"],
    "exclusions": ["what_this_agent_does_not_do"]
  },
  "integrity_requirements": {
    "requirement_key": "requirement description"
  },
  "depends_on_skills": ["skill1", "skill2"],
  "depends_on_workflows": ["workflow1.md"]
}
```

---

## Naming Convention

- **Format**: `amos-{role}-agent`
- **All lowercase, hyphenated**
- **Ends with `-agent`**
- **Role is descriptive**: Not "leaf", "?", or vague terms
- **System assignment**: Every agent has exactly one system

## Verification

All 65 agents verified to have:
- [x] `name` field matching filename
- [x] `description` field with substantive content
- [x] `version` field
- [x] `system` field with valid system name
- [x] `role` field with descriptive content (no "leaf" or "?")
- [x] `capabilities` array with at least 5 capabilities
- [x] `operations` object with entry_point, protocol, scope, exclusions
- [x] `integrity_requirements` object with at least 3 requirements
- [x] `depends_on_skills` array
- [x] `depends_on_workflows` array

---

## Recent Additions (v12.0.0, 2026-08-25)

Live workspace count: **678 JSON agents** (non-arxiv + arxiv-index). The full per-system breakdown is pending re-audit. New or enriched agents in this batch:

- `amos-equations-master-registry-agent.json` — Unified Model across 17 systems
- `amos-quantum-electromagnetic-architecture-agent.json` — 50 EM fractal templates
- `amos-hidden-fractal-architecture-agent.json` — INTENDED/EMERGENT/COINCIDENTAL adjudication
- `amos-fractal-semantic-intelligence-arch-agent.json` — FSIA implementation
- `amos-trang-framework-lmh-lambda-agent.json` — L/M/H × lacunarity
- `amos-universe-structure-tree-agent.json` — 7-part UST mapping
- `amos-math-6-kernel-unified-agent.json` — Six math kernel routing
- `amos-quantum-fractal-math-trinity-agent.json` — Max-power QFM trinity
- Plus 645+ existing canonical agents

### Cross-Domain Governor Agents
| Agent | Role | Caps | Version |
|-------|------|------|---------|
| amos-cross-domain-tensor-composition-governor-agent | Govern cross-domain tensor composition: validate tensor contracts, enforce compatibility invariants, block invalid compositions | 9 | 1.0.0 |
| amos-emotion-cognition-decision-bridge-governor-agent | Bridge C05↔C01↔C10: emotion-cognition-decision loop with 9 capabilities and 10 gates | 9 | 1.0.0 |
| amos-learning-memory-knowledge-feedback-governor-agent | Bridge C05→Memory→Knowledge: unified learning-memory-knowledge feedback loop with epistemic preservation, corroboration, freshness validation, and provenance tracing | 10 | 1.0.0 |
| amos-security-control-access-bridge-governor-agent | Bridge C09→C10→Runtime: policy-to-enforcement pipeline with layer match validation, drift detection, and audit trail | 10 | 1.0.0 |
| amos-vietnamese-global-cultural-bridge-governor-agent | Bridge C06 Vietnamese↔Global: bidirectional cultural translation with universalization firewall and cultural specificity preservation | 10 | 1.0.0 |
| amos-biology-quantum-bridge-governor-agent | Bridge C04↔C03: biology-quantum mapping with anti-overclaim firewall (MODEL/METAPHOR only, never physical predictions) | 10 | 1.0.0 |

Total: **337 agents (JSON), 0 non-arxiv skills without agents**.

---
**Related:** [[00_HOME]]

---
```RSCF-NODE
node_id: amos-agent-registry-index
node_type: agent
domain: AMOS_AGENT
path: .devin/agents/amos-agent-registry-index.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
claim_class: AMOS_MODEL
```

---
**MOC:** [[06_AGENTS_MOC]]
