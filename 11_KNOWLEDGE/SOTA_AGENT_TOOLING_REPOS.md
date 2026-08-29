---
Type: Reference
title: SOTA Agent/Skill/Workflow Tooling Repos (2025-2026)
tags:
- type/reference
- domain/agent-systems
- sota
- amos_os
---

# SOTA Agent/Skill/Workflow Tooling Repos (2025-2026)

Curated top-10 open-source repositories for enhancing AMOS agent definitions, skill packaging, and workflow orchestration. Research conducted 2026-08-28.

## Applied to AMOS (v1.1.0)

The following SOTA patterns have been applied to all 345 AMOS agents:

- **A2A AgentCard** (from `a2aproject/A2A`) — every agent now has an `agent_card` block with protocol, capabilities URL, input/output modes, and skill refs.
- **OpenAI Agents SDK Guardrails** (from `openai/openai-agents-python`) — every agent now has `guardrails` with `input_guardrails` and `output_guardrails` lists.
- **skillroute Routing Confidence** (inspired by `erichare/skillroute` and `reaatech/confidence-router`) — every agent now has `routing_confidence` with base_score, boost_keywords, and decay_on_miss.

## Top 10 Repos for Further Integration

### 1. A2A Protocol — `a2aproject/A2A` (~25,526 stars)

- **Key feature**: Agent-to-Agent protocol with `AgentCard` JSON schema for capability discovery.
- **AMOS integration**: Already applied `agent_card` block. Next: expose at `/.well-known/agent.json` for external discovery.

### 2. agents.json — `wild-card-ai/agents-json` (~1,314 stars)

- **Key feature**: OpenAPI-derived JSON spec for API/agent tool contracts.
- **AMOS integration**: Generate `agents.json` manifest from skill Markdown tool descriptions.

### 3. AgentNetworkProtocol (ANP) — `agent-network-protocol/AgentNetworkProtocol` (~1,407 stars)

- **Key feature**: JSON-LD based Agent Description with `schema.org` vocabularies and DID-based trust.
- **AMOS integration**: Add `@context`, `@type`, `ad:AgentDescription` annotations for semantic search.

### 4. skill-check — `thedaviddias/skill-check` (~188 stars)

- **Key feature**: Linter for `SKILL.md` files with quality scoring, auto-fix, security scanning, SARIF.
- **AMOS integration**: Run in CI over every `SKILL.md`; gate PRs on minimum quality score.

### 5. agent-registry — `agentoperations/agent-registry` (~4 stars)

- **Key feature**: Vendor-neutral registry wrapping A2A AgentCard, MCP server.json, and SKILL.md with BOM, evaluation signals, promotion lifecycle.
- **AMOS integration**: Publish AMOS agent cards/skills/workflows to registry; track promotions.

### 6. LangGraph — `langchain-ai/langgraph` (~40,592 stars)

- **Key feature**: Stateful, graph-based workflow orchestration with persistence, human-in-the-loop.
- **AMOS integration**: Parse Markdown workflow files into LangGraph nodes/edges; compile to state machine.

### 7. CrewAI — `crewAIInc/crewAI` (~57,595 stars)

- **Key feature**: Role-based multi-agent crews and event-driven Flows.
- **AMOS integration**: Map AMOS JSON agents to `Agent`/`Task`/`Crew` definitions.

### 8. OpenAI Agents SDK — `openai/openai-agents-python` (~28,916 stars)

- **Key feature**: Lightweight agent runtime with first-class guardrails and handoff-based routing.
- **AMOS integration**: Already applied guardrails pattern. Next: wrap AMOS skills as tools with `@input_guardrail`/`@output_guardrail`.

### 9. NeMo Guardrails — `NVIDIA/NeMo-Guardrails` (~7,014 stars)

- **Key feature**: Colang-based programmable guardrails for topic safety, fact-checking, hallucination detection.
- **AMOS integration**: Add `config.yml` and Colang topic flows; insert rails before/after LLM calls.

### 10. confidence-router — `reaatech/confidence-router` (new/niche)

- **Key feature**: Pluggable route/clarify/fallback engine with threshold tuning and evaluation harness.
- **AMOS integration**: Feed skill classification scores into ConfidenceRouter; configure `routeThreshold` per agent.

## Also Worth Watching

- `a2a-python` SDK — Python implementation of A2A protocol
- `moonrunnerkc/skillcheck` — Alternative skill linter
- `modelcontextprotocol/registry` — MCP Registry
- `agntcy/oasf` — Open Agent Schema Framework
- `microsoft/agent-framework` — Microsoft's unified agent framework (replaces AutoGen)
- `n8n-io/n8n` — Visual workflow automation

## Provenance

- **Research date**: 2026-08-28
- **Researcher**: Devin subagent (web search)
- **Epistemic class**: EMPIRICAL (star counts from GitHub, may change)
- **RSCF state**: SOURCE_CLAIM (repo features from README/docs)

## Skill Quality & Packaging Repos (2025-2026, Round 2)

### 11. anthropics/skills (~172k stars)

- **Key feature**: Canonical skill corpus + spec reference for SKILL.md files.
- **AMOS integration**: Use `/spec` and `/template` as ground-truth for frontmatter schema.

### 12. agentskills/agentskills (~24.7k stars)

- **Key feature**: Vendor-neutral Agent Skills specification with progressive disclosure.
- **AMOS integration**: Adopt as package manifest standard for portability across Claude Code, Codex, Cursor.

### 13. vercel-labs/skills (~29.2k stars)

- **Key feature**: `npx skills` CLI for discovery, install, update, multi-agent deployment.
- **AMOS integration**: Make AMOS skills installable via `npx skills add`.

### 14. AgentSkillOS — ynulihao/AgentSkillOS (~597 stars)

- **Key feature**: Retrieval + DAG-based skill composition with 200k+ capability tree.
- **AMOS integration**: Feed SKILL.md corpus into capability tree; use DAG scheduler for multi-step workflows.

### 15. skilld-dev/skilld (~299 stars)

- **Key feature**: Auto-generated versioned SKILL.md packages with semantic search.
- **AMOS integration**: Use `skilld search` for internal semantic discovery over skills.

### 16. SkillRouter — zhengyanzhao1997/SkillRouter (~235 stars)

- **Key feature**: Embedding-based skill routing with 0.6B models, ~74% Hit@1.
- **AMOS integration**: Embed SKILL.md files; retrieve+rerank for skill selection.

### 17. NVIDIA/SkillEvaluator (~204 stars)

- **Key feature**: Three-tier evaluation: deterministic validation, semantic dedup, live A/B testing.
- **AMOS integration**: Validate frontmatter, check capability overlap, run with-skill vs without-skill tests.

### 18. thedaviddias/skill-check (~188 stars)

- **Key feature**: CLI linter + 0-100 quality score, SARIF output, auto-fix.
- **AMOS integration**: Add to CI: `npx skill-check --min-score 80 --format sarif ./skills`

## Recommended Pipeline

1. **Author** with `vercel-labs/skills init` + `agentskills/agentskills` layout
2. **Lint/score** with `thedaviddias/skill-check` in CI
3. **Evaluate** with `NVIDIA/SkillEvaluator` before release
4. **Package** with `vercel-labs/skills` or `skilld-dev/skilld`
5. **Discover** with `SkillRouter` embeddings or `AgentSkillOS` retrieval
6. **Execute** by composing skills with `AgentSkillOS` DAGs

## Agent Evaluation & Safety Repos (2025-2026, Round 3)

### 19. A2A Protocol — a2aproject/A2A (~25,526 stars)

- **Key feature**: Agent-to-Agent protocol with JSON-RPC/HTTP, Agent Cards, streaming, async tasks.
- **AMOS integration**: Turn 355 JSON agent definitions into A2A Agent Cards; use workflow MD files to define A2A task flows.

### 20. MCP Python SDK — modelcontextprotocol/python-sdk (~24,127 stars)

- **Key feature**: Official Python SDK for Model Context Protocol clients & servers.
- **AMOS integration**: Convert 354 SKILL.md files into MCP servers/tools; 355 JSON agents become MCP clients.

### 21. agentmemory — rohitg00/agentmemory (~27,612 stars)

- **Key feature**: Long-term memory engine with knowledge graphs, confidence scoring, hybrid search.
- **AMOS integration**: Index SKILL.md and workflow MD files as retrievable memory; auto-capture episodes from agents.

### 22. TencentDB-Agent-Memory — Tencent (~24,586 stars)

- **Key feature**: Team memory hub turning conversations, docs, code, skills into reusable memory assets.
- **AMOS integration**: Import SKILL.md as Skill assets and workflow MD as Wiki assets for team memory.

### 23. OpenLLMetry — traceloop/openllmetry (~7,388 stars)

- **Key feature**: OpenTelemetry-based observability for LLM, tool, and vector-DB calls.
- **AMOS integration**: Wrap every agent, skill call, and workflow step with OpenTelemetry spans.

### 24. AgentBench — THUDM/AgentBench (~3,701 stars)

- **Key feature**: Multi-environment benchmark for evaluating LLMs as agents.
- **AMOS integration**: Run 355 JSON agents through containerized tasks; map JSON tool schemas to function-calling harness.

### 25. SkillSpector — NVIDIA/SkillSpector (~14,708 stars)

- **Key feature**: Static security scanner for agent skills (prompt injection, data exfiltration, 69+ vuln patterns).
- **AMOS integration**: CI gate scanning every SKILL.md before agent loading; reject/quarantine high-risk skills.

### 26. Crucible — crucible-security/crucible (~48 stars)

- **Key feature**: "pytest for AI agents" — automated red-teaming with 90+ attack payloads and MCP security tests.
- **AMOS integration**: Target 355 agent definitions and 354 workflows with red-team campaigns in CI.

## Recommended Integration Pipeline (Full)

1. **MCP-ize skills** — expose SKILL.md files through MCP Python SDK
2. **A2A-wrap agents** — publish JSON agents as A2A servers
3. **Gate skill safety** — wire SkillSpector into CI
4. **Add traces** — instrument with OpenLLMetry
5. **Enable memory** — load skill/workflow corpus into agentmemory
6. **Run eval + red-team** — use AgentBench + Crucible

## Workflow Orchestration & Agent Composition Repos (2025-2026, Round 4)

### 27. Conductor OSS — conductor-oss/conductor (~32.1k stars)

- **Key feature**: Durable, event-driven, agentic workflow engine with versioned DAG/state-machine execution, retries, human approvals.
- **AMOS integration**: Convert Schema-A workflow MD to Conductor workflow JSON; map 394 agents to tasks; use SWITCH/DECISION for Trigger branching.

### 28. Kestra — kestra-io/kestra (~27.4k stars)

- **Key feature**: Declarative YAML orchestration with triggers, artifacts, plugin ecosystem.
- **AMOS integration**: Generate one .yml flow per workflow MD; parse Schema A frontmatter into flow metadata.

### 29. Agency Swarm — VRSEN/agency-swarm (~4.5k stars)

- **Key feature**: Multi-agent "agency" pattern with org-style roles, directional send_message flows.
- **AMOS integration**: Create Agent class per JSON definition; define Agency with communication_flows matching workflow handoff graph.

### 30. Open Multi-Agent — open-multi-agent/open-multi-agent (~6.8k stars)

- **Key feature**: Goal-driven dynamic orchestration; coordinator turns NL goals into runtime task DAGs.
- **AMOS integration**: Feed workflow MD goals to runTeam(); let coordinator generate DAG from 394 available agents.

### 31. Dapr Agents — dapr/dapr-agents (~743 stars)

- **Key feature**: Production-grade K8s-native multi-agent runtime with durable workflows, state, pub/sub.
- **AMOS integration**: Wrap agents as DaprAgent; model workflows as durable Dapr Workflows; use OpenTelemetry tracing.

## Full Integration Roadmap

1. **Normalize Schema A parsing** — one frontmatter parser for all downstream engines
2. **Layer 1: package + version** — Vercel Skills (skills.json/skill-lock.json)
3. **Layer 2: orchestration** — Conductor or Kestra for durable DAGs; LangGraph for prompt chaining
4. **Layer 3: agents + handoffs** — OpenAI Agents (handoff) or Agency Swarm (send_message)
5. **Layer 4: runtime resilience** — Dapr Agents for K8s-native scaling
6. **Layer 5: safety** — SkillSpector + Crucible for CI gates
7. **Layer 6: observability** — OpenLLMetry for correlated traces
8. **Layer 7: memory** — agentmemory or TencentDB for context reuse
9. **Layer 8: evaluation** — AgentBench for capability benchmarking

## Gap Management & Epistemic Integrity Repos (2025-2026, Round 5)

### 32. SENATOR — weiyifan1023/senator (~66 stars, NeurIPS 2025)

- **Key feature**: Structural Entropy over KG paths + MCTS to quantify uncertainty and map knowledge gaps in LLMs.
- **AMOS L27 integration**: Pre-generation gap cartography. Map where model knowledge is sparse; route to GAP status instead of generation when SE falls below threshold.

### 33. IBM FactReasoner (~38 stars, 2025)

- **Key feature**: Probabilistic fine-grained factuality assessment. Decomposes LLM responses into atomic claims, retrieves evidence, returns calibrated probability per claim.
- **AMOS L27 integration**: Post-generation gate for every AMOS artifact. Claims below threshold become proof-capsule GAP entries. Closure requires new evidence retrieval (GAP-4).

### 34. Dokis — Vbj1808/Dokis (~37 stars, 2026)

- **Key feature**: Deterministic inline RAG provenance. Extracts claims, matches to retrieved chunks, builds claim→chunk→URL map, computes compliance rate.
- **AMOS L27 integration**: Place between retriever and output formatter. Failing responses downgraded to GAP status with gap registry showing unsupported claims.

### 35. styxx — fathom-lab/styxx (~14 stars, 2026)

- **Key feature**: Machine-verifies agent claims against committed receipts with negatives included. CI gate via GitHub Action.
- **AMOS L27 integration**: CI gate for AMOS-generated commits. `certify` must find matching receipt; if none, claim marked GAP and artifact not promoted.

### 36. HaMI — mala-lab/HaMI (~13 stars, NeurIPS 2025)

- **Key feature**: Hallucination detection as Multiple Instance Learning over token-level representations. Adaptive token selection for free-form generation.
- **AMOS L27 integration**: Run over AMOS generator outputs. Flagged tokens replaced with visible `GAP-TOKEN: <reason>` marker, routed for evidence retrieval.

### 37. MetaFaith — yale-nlp/MetaFaith (~10 stars, EMNLP 2025)

- **Key feature**: Metacognition-inspired calibration prompts aligning LLM intrinsic uncertainty with linguistic expressions. No task-specific tuning.
- **AMOS L27 integration**: Default AMOS generation system instruction. Model must output explicit GAP status string when evidence is missing (GAP-2: UNKNOWN is first-class).

## L27-Aligned Composite Pipeline

1. **SENATOR** — map domain knowledge gaps before generation
2. **MetaFaith** — generate with calibrated, gap-aware language
3. **HaMI** — detect hallucinated tokens/entities in draft
4. **Dokis + IBM FactReasoner** — verify each claim against sources with calibrated scores
5. **styxx** — final CI gate: every claim must match receipt or be registered as gap
6. **Output** — every artifact ships with proof capsule listing load-bearing gaps (GAP-3)

## Agent Registry & Discovery Repos (2025-2026, Round 6)

### 38. MCP Gateway Registry — agentic-community/mcp-gateway-registry (~875 stars)

- **Key feature**: Centralized control-plane registering MCP servers, agents, skills, prompts behind authenticated gateway. Semantic NL discovery.
- **AMOS integration**: Ingest 448 AgentCard JSONs as registry entries; register SKILL.md and workflow files as versioned asset bundles. Use /search endpoint for task dispatcher.

### 39. agntcy/dir (~166 stars)

- **Key feature**: Distributed directory for multi-agent systems using Open Agent Schema Framework (OASF). P2P content-addressed discovery with constraint filtering.
- **AMOS integration**: Publish 448 agents as OASF records with AgentCard/guardrails/routing_confidence. Discover agents by capability constraints.

### 40. SkillCorpus — EverMind-AI/SkillCorpus (~92 stars)

- **Key feature**: Pipeline turning scattered SKILL.md files into curated retrieval-ready corpus. Multi-stage curation, bi-encoder/reranker, 16-class taxonomy.
- **AMOS integration**: Feed 447 SKILL.md files into pipeline for quality-filtered vectorized index. Runtime retrieval without hard-coded skill names.

### 41. agent-router — dabit3/agent-router (~14 stars)

- **Key feature**: Framework-agnostic task router with configurable strategies: best-match, lowest-cost, fastest, round-robin, least-loaded, highest-success.
- **AMOS integration**: Map 448 agents using AgentCard capabilities + routing_confidence as confidence score. Guardrails as hard constraints.

### 42. gitagent — open-gitagent/gitagent (~653 stars)

- **Key feature**: Git-native agent framework. Agent lives in repo: agent.yaml, SOUL.md, RULES.md, tools/, skills/, hooks/. Branching, forking, lifecycle hooks.
- **AMOS integration**: Convert 448 agent JSONs into git-backed packages. Git tags for releases/deprecation/rollbacks. Hooks for activation/retirement gates.

### 43. OpenCode-GraphAgent — LeXwDeX/OpenCode-GraphAgent (~100 stars)

- **Key feature**: Decomposes tasks into DAG of child agents, executes in dependency-ordered waves, crash recovery, TUI/HTTP API.
- **AMOS integration**: Turn 447 workflow MD files into DAG node definitions. Dependency graph engine for parallel/ordered agent execution.

## Registry & Discovery Integration Pipeline

1. **Register** agents in mcp-gateway-registry + agntcy/dir
2. **Index** SKILL.md files with SkillCorpus for semantic retrieval
3. **Route** tasks to agents with agent-router using routing_confidence
4. **Version** agents with gitagent for lifecycle management
5. **Execute** workflows as DAGs with OpenCode-GraphAgent

## Cognitive Architecture & Intelligence Modeling Repos (2025-2026, Round 7)

### 44. Soar — SoarGroup/Soar (~427 stars)

- **Key feature**: General cognitive architecture with working memory, production rules, goal-driven problem spaces, symbolic reasoning.
- **AMOS integration**: Map 448 skills as Soar operators/chunks, 449 agents as problem spaces. Use Human Intelligence Canon factor models to bias working-memory activation.

### 45. AgentEvolver — modelscope/AgentEvolver (~1,547 stars)

- **Key feature**: Self-evolving agent framework: self-questioning, self-navigating, self-attributing for continuous capability growth.
- **AMOS integration**: Use Canon as fitness/evaluation ontology. Self-questioning generates new skill candidates, self-attributing credits which agents/skills improved outcomes.

### 46. RxBrain — Tencent-Hunyuan/Hy-Embodied-RxBrain-1.0 (~129 stars)

- **Key feature**: Embodied cognition foundation model with joint language-visual reasoning, world-state prediction, subgoal planning.
- **AMOS integration**: Attach as visual/embodied reasoning skill. Map Canon sections on biological/neural mechanisms to RxBrain's embodied prediction loop.

### 47. AgentCompass — open-compass/agentcompass (~100 stars)

- **Key feature**: Modular evaluation infra decoupling Model/Benchmark/Harness/Environment with 20+ built-in benchmarks.
- **AMOS integration**: Register each Canon measurement procedure as a harness, each agent as a model. Continuous evaluations write results to capability registry — intelligence scorecard per agent.

### 48. Cognitive Workspace — tao-hpu/cognitive-workspace (~104 stars)

- **Key feature**: Hierarchical memory + metacognitive controller: task decomposition, confidence tracking, information-gap analysis, infinite context.
- **AMOS integration**: Layer between agents and LLM context. Monitor per-agent load, compress/dump context on spikes, emit load tokens for router.

### 49. agent-router (revisited) — dabit3/agent-router (~14 stars)

- **Key feature**: Capability-aware task routing with load, cost, latency, success-rate, fallback strategies.
- **AMOS integration**: Feed 448 skills as capabilities; route tasks to least-loaded best-matched agent. Weight Canon factor importance into routing score.

## Cognitive Enhancement Integration Roadmap

### Phase 1: Measure & Route

1. AgentCompass on 449 agents — capability registry keyed by agent_id × factor_id
2. agent-router on 448 skills — weighted strategy with capabilityMatch, currentLoad, successRate

### Phase 2: Cognitive Architecture & Metacognition

3. Soar as reasoning kernel — compile skill chains into Soar productions
4. AgentEvolver to evolve skill set — self-questioning against capability gaps

### Phase 3: Multimodal & Embodied

5. RxBrain for visual/embodied skills — wrap as vision-reasoning skill

### Phase 4: Cognitive Load Guardrails

6. Cognitive Workspace as shared metacognitive layer — confidence, information gap, context pressure monitoring

## Agent Evaluation & Observability Repos (2025-2026, Round 8)

### 50. Harbor — harbor-framework/harbor (~4,494 stars)

- **Key feature**: Sandboxed parallel benchmark harness for arbitrary agents. 20+ public benchmarks, RL rollouts, scorecards.
- **AMOS integration**: Convert 470 workflow MD files into Harbor benchmark tasks. Run 469 agents through sandboxed benchmarks. Nightly leaderboards per skill/workflow.

### 51. SimpleMem — aiming-lab/SimpleMem (~3,705 stars)

- **Key feature**: Semantic lossless compression, cross-session long-term memory, intent-aware retrieval, multimodal + MCP server.
- **AMOS integration**: Embed 468 SKILL.md + 470 workflow files as compressed memory units. Use compaction_threshold 0.8 as SimpleMem trigger. Per-agent usage signals feeding context_management.

### 52. OpenJudge — agentscope-ai/OpenJudge (~798 stars)

- **Key feature**: 50+ production-validated graders: correctness, hallucination, tool selection, trajectory, memory accuracy, plan feasibility.
- **AMOS integration**: Map SKILL.md Evaluation sections to OpenJudge graders. Batch score 469 agents on epistemic_class labels, provenance, confidence ceilings, scope compliance.

### 53. xaidr — delphisecurity/xaidr (~26 stars)

- **Key feature**: In-process runtime security sensor for input/output/tool/A2A boundaries. Prompt injection, jailbreak, secret leak detection. <1ms latency.
- **AMOS integration**: Insert Sensor scans before every LLM input/output/tool invocation. Enforce safety_constraints, QFM v43 gates, law_compliance. OTel export to AMOS observability.

### 54. Invarium — invarium-ai/invarium (~22 stars)

- **Key feature**: pytest for agents — behavioral assertions, baseline bless, regression detection, flakiness scoring, CI-native.
- **AMOS integration**: Convert 470 workflow MD files into Invarium test contracts. bless canonical tool sequences. CI catches QFM/vault updates that alter agent behavior.

### 55. observra — open-agent-ai-security/observra (~21 stars)

- **Key feature**: Framework-agnostic agent behavior analytics. CIM-structured telemetry, OTel/JSONL export.
- **AMOS integration**: Instrument AMOS orchestrator with telemetry.jsonl per agent step. Aggregate cost, latency, errors across 469 agents. Feed into amos-agentops-observability-rscf.

## Evaluation & Observability Integration Sequence

1. **Phase 0 — Baseline**: Invarium bless on all workflows to lock current behavior
2. **Phase 1 — Observe**: Add observra to AMOS runner for structured telemetry
3. **Phase 2 — Secure**: Wrap runner with xaidr sensors at all boundaries
4. **Phase 3 — Memorize**: Index skills/workflows in SimpleMem for compressed retrieval
5. **Phase 4 — Evaluate**: Run Harbor benchmarks + OpenJudge graders on all skills
6. **Phase 5 — Gate**: CI jobs with Invarium test + OpenJudge + xaidr monitor on every PR

## Agent Orchestration & Multi-Agent Coordination Repos (2025-2026, Round 9)

### 56. AutoGen — microsoft/autogen (~60,700 stars)

- **Key feature**: Multi-agent group chat, tool-calling, code execution, human-in-the-loop. MagenticOne pattern for hierarchical task decomposition.
- **AMOS integration**: Ingest 489 JSON agents as ConversableAgent/chat agents. Register 488 SKILL.md as tool/executor functions. Map 490 workflow MD to group-chat or MagenticOne team flows.

### 57. CrewAI — crewAIinc/crewAI (~57,600 stars)

- **Key feature**: Role-based Crews and event-driven Flows for goal-driven agent collaboration.
- **AMOS integration**: Convert each JSON agent into a Role (role/goal/backstory). Wrap SKILL.md as Tool definitions. Express workflows as Flow event-driven pipelines for autonomous missions.

### 58. LangGraph — langchain-ai/langgraph (~40,600 stars)

- **Key feature**: Stateful graph execution — DAGs, cycles, branching, parallelism, persistence, time-travel, human-in-the-loop.
- **AMOS integration**: Compile 490 workflow MD into StateGraph workflows. Load 489 agents as graph nodes, 488 skills as bound tool nodes. Checkpointed, resumable, traceable execution with human approval gates.

### 59. OpenAI Agents SDK — openai/openai-agents-python (~29,000 stars)

- **Key feature**: Lightweight Agent, handoff, and Agent.as_tool() primitives for triage and hierarchical decomposition.
- **AMOS integration**: Build top-level AMOS triage agent using handoff to route to 489 specialists. Expose SKILL.md as agent tools. Model workflows as handoff chains.

### 60. A2A Protocol — google/A2A (~25,500 stars)

- **Key feature**: Open, interoperable Agent2Agent protocol with Agent Cards, task messages, artifact exchange.
- **AMOS integration**: Generate A2A Agent Cards from 489 JSON agent manifests. Expose SKILL.md as capabilities. Map workflow MD to A2A Task/Artifact flows. Interoperability with external A2A-compliant agents.

### 61. Council — dadcoachengineer/council (~6 stars)

- **Key feature**: MCP-native boardroom with deliberation, voting, veto, weighted expertise, human escalation.
- **AMOS integration**: Seat 489 agents as governance board with topic-expertise weights. Use SKILL.md as MCP tools. Run workflows as structured deliberation (investigate → propose → amend → vote) with majority/supermajority/unanimity gates.

## Orchestration Integration Priority

1. **Immediate wins**: LangGraph or CrewAI for workflow execution — directly consume workflow MD and SKILL.md
2. **Interoperability**: A2A for external agent communication
3. **Safety/governance**: Council for voting/conflict-resolution (aligns with MURK reasoning)
4. **Hierarchical delegation**: OpenAI Agents SDK for handoff, AutoGen for group-chat/hierarchical

## Additional Finds (Round 3 — 2026-08-28)

### 62. Microsoft Agent Framework — `microsoft/agent-framework` (~13,154 stars)

- **Key feature**: Production-grade multi-agent workflows in Python/.NET/Go with graph-based orchestration, checkpointing, human-in-the-loop, and skills/knowledge design.
- **AMOS integration**: Map 489 agents into MAF Agent and Skill primitives; compile workflow MD to MAF workflow graphs.

### 63. PAS Framework — `ZoranSpirkovski/PAS` (new/niche)

- **Key feature**: Process/Agent/Skill modular framework for agentic workflows with feedback backlogs and changelog targeting.
- **AMOS integration**: Bind AMOS processes to PAS, assign agents to skills, and route feedback to skill improvement.

### 64. AgentFlow — `agentenv/agentflow` (~1,375 stars)

- **Key feature**: Orchestrate thousands of agents as dependency graphs with parallel fanout, iterative cycles, and local/remote execution.
- **AMOS integration**: Compile workflow MD to AgentFlow dependency graphs; fan out AMOS agents across execution targets.

### 65. SkillEngine — `sawzhang/skillengine` (new/niche)

- **Key feature**: Framework-agnostic Markdown-based skills engine with hot-reload, multi-source loading, and per-skill tools/models.
- **AMOS integration**: Load 488 SKILL.md files into SkillEngine for cross-platform skill portability.

### 66. SkillFlow — `linxuhao/SkillFlow` (new/niche)

- **Key feature**: Deterministic YAML-DAG agentic workflow executor with human approval gates, loops, recovery, and durable audit trace.
- **AMOS integration**: Convert AMOS workflow MD to SkillFlow YAML DAGs for deterministic, auditable execution.

## Identity Management & Agent Authentication Repos (2025-2026, Round 10)

### 68. OpenFGA — openfga/openfga (~5,534 stars)

- **Key feature**: Google Zanzibar-inspired fine-grained auth engine. RBAC/ABAC/ReBAC models with SDKs, CLI, playground.
- **AMOS integration**: Model 509 agents, 508 skills as OpenFGA object types. Define canonical relations: agent#can_invoke[skill], human#delegates[agent], agent#owns[artifact], system#hosts[agent]. Implements authorization, agent identity, alias semantics, identity equivalence.

### 69. ZeroID — highflame-ai/zeroid (~155 stars)

- **Key feature**: Autonomous-agent identity (AAIMS): OAuth 2.1, WIMSE/SPIFFE, RFC 8693 token exchange, delegated authority, real-time revocation.
- **AMOS integration**: Assign each of 509 agents a stable URI. Map OAuth scopes to 508 skills. Store delegation chain as identity lineage. Attestation endpoint populates authentication, trust, identity continuity sections.

### 70. Warden — stephnangue/warden (~139 stars)

- **Key feature**: Secure egress gateway brokering agent-to-system connections. SPIFFE/JWT/K8s SA auth, request-level policy, audit.
- **AMOS integration**: Deploy as sidecar in front of skill executors. Every agent skill call authenticated, authorized, logged. Audit feed enriches authorization, identity lineage, artifact identity sections.

### 71. GoldenMatch — benseverndev-oss/goldenmatch (~129 stars)

- **Key feature**: Zero-config Fellegi-Sunter entity resolution. Durable golden entities, whole-record provenance, merge/split audit. MCP and REST interfaces.
- **AMOS integration**: Run over all human, agent, skill, artifact, system, cognitive-identity records to produce stable canonical entity_ids. Provenance graph populates identity resolution, equivalence, continuity, versioning.

### 72. Alien Agent ID — alien-id/agent-id (~33 stars)

- **Key feature**: Ed25519 agent key, encrypted credential vault, local proxy for API keys/tokens/wallets, optional human binding via SSO cnf.jkt.
- **AMOS integration**: Generate self-custodied key per agent. Store skill/API credentials in vault. Extend Canon with self-identity and cognitive identity key-custody. Human-binding flow satisfies human identity provenance.

### 73. Fraunhofer-AISEC CMC (~24 stars)

- **Key feature**: Remote attestation for TPM 2.0, AMD SEV-SNP, Intel SGX, Intel TDX. Attested TLS/HTTPS channels, self-contained attestation reports.
- **AMOS integration**: Gate agent runtime startup on CMC attestation report. Store as system identity and artifact identity record. Attested TLS for agent-to-skill communication creates verifiable trust chains.

## Identity Integration Roadmap

1. **Identity baseline**: ZeroID assigns stable URI + short-lived credential to every agent
2. **Policy layer**: OpenFGA authorization model with agent/skill/human/artifact/system object types
3. **Entity canonicalization**: GoldenMatch produces master entity_id table for equivalence and continuity
4. **Runtime enforcement**: Warden brokers every agent-to-skill and agent-to-enterprise call
5. **Decentralized keys**: Alien Agent ID for agent self-identity and credential vaulting
6. **Hardware trust**: Fraunhofer CMC attestation as pre-condition for agent scheduling

## Agent Safety & Adversarial Robustness Repos (2025-2026, Round 11)

### 74. Prompt Guard — seojoonkim/prompt-guard (~173 stars)

- **Key feature**: Runtime prompt-injection/jailbreak shield with severity scoring, 840+ patterns, 10-language support, obfuscation detection, output DLP, canary tokens.
- **AMOS integration**: Deploy as shared Ingress Filter in front of 529 agents. Map category/severity into input_guardrails. Block HIGH/CRITICAL. Output DLP as Egress Filter populating output_guardrails.detections.

### 75. DeepTeam — confident-ai/deepteam (~2,570 stars)

- **Key feature**: Red-team framework for LLM agents: 20+ attacks, multi-turn exploitation, custom vulnerabilities, local execution, guardrail testing.
- **AMOS integration**: CI pipeline loads each agent's SKILL.md and workflow.md as context. Per-agent red-team report keyed to safety_constraints.redteam_report. Failed tests become new guardrail rules. Re-run on workflow updates.

### 76. NeMo Guardrails — NVIDIA/NeMo-Guardrails (~7,014 stars)

- **Key feature**: Programmable input/output/retrieval/execution rails with Colang. LangChain/custom-endpoint integration. Moderation & topic enforcement.
- **AMOS integration**: Treat input_guardrails + output_guardrails as source-of-truth for generated config.yml. Build step compiles 529 JSON files into NeMo rail definitions. Input rails reject adversarial prompts. Output rails validate format. Execution rails wrap tool calls.

### 77. OpenSandbox — alibaba/OpenSandbox (~14,596 stars)

- **Key feature**: General-purpose AI agent sandbox, multi-language SDK, MCP server, Docker/K8s, gVisor/Kata/Firecracker isolation, code/browser/desktop environments.
- **AMOS integration**: Spawn one sandbox per agent or per session. Route every code-execution, file, browser, MCP tool call through OpenSandbox. Derive sandbox policies from safety_constraints and workflow MD. MCP server for orchestrator.

### 78. verl — volcengine/verl (~22,770 stars)

- **Key feature**: Production-grade RL post-training (PPO/GRPO/DAPO/VAPO), vLLM/SGLang, FSDP/Megatron, multi-turn agentic rollouts.
- **AMOS integration**: Convert runtime logs and DeepTeam red-team results into preference/trajectory dataset. Fine-tune safety-critic/reward model with GRPO. Re-rank candidate outputs at inference time. Export LoRA checkpoints for AMOS router.

### 79. LLaMA-Factory — hiyouga/LLaMA-Factory (~73,608 stars)

- **Key feature**: Unified SFT/DPO/KTO/PPO/GRPO/LoRA/QLoRA fine-tuning for 100+ models, web UI, dataset conversion.
- **AMOS integration**: Build Constitution/value dataset from workflow MD (positive) and red-team failures (negative). Run KTO/DPO to prefer workflow-aligned responses. Export per-skill LoRA adapters. Load at runtime to reinforce output_guardrails.

## Safety Integration Architecture

```
User/Tool Input -> [prompt-guard] -> [NeMo input rail] -> [AMOS Router]
  -> [OpenSandbox] tool execution -> [NeMo output rail] -> [aligned model]
  -> [Output DLP] -> Final response -> [DeepTeam red-team on next CI run]
```

## Safety Integration Sequence

1. **Start with guardrails and sandboxing**: NeMo-Guardrails + OpenSandbox for immediate runtime containment
2. **Add input defense**: prompt-guard in input path, severity scores populate input_guardrails
3. **Automate red-teaming**: DeepTeam against 529 agents nightly, results feed safety_constraints
4. **Close the loop with alignment**: LLaMA-Factory for SFT/DPO/KTO, verl for large-scale RL, export LoRA adapters

## Agent Tooling & MCP Server Repos (2025-2026, Round 12)

### 80. MCP Registry — modelcontextprotocol/registry (~7,194 stars)

- **Key feature**: Official MCP server metadata registry with namespace auth, versioning, discovery API.
- **AMOS integration**: Treat 549 agents and 548 SKILL.md-derived tool sets as discoverable MCP servers. Generate server.json manifests. Private internal MCP marketplace.

### 81. OpenAI Agents SDK — openai/openai-agents-python (~28,916 stars)

- **Key feature**: Lightweight multi-agent SDK with function calling, tools, guardrails, handoffs, MCP support (100+ model providers).
- **AMOS integration**: Convert 549 JSON agent specs into Agent objects, 548 SKILL.md into tools/handoffs, 550 workflow MD into Runner orchestration patterns. Provider-agnostic.

### 82. SkillHub — iflytek/skillhub (~4,878 stars)

- **Key feature**: Enterprise self-hosted skill registry: semantic versioning, RBAC, audit logs, security scanner.
- **AMOS integration**: Import 548 SKILL.md as versioned, namespaced skill packages. Agents query registry at runtime. Governance teams approve/scan skills before use.

### 83. Docker Agent — docker/docker-agent (~3,201 stars)

- **Key feature**: Declarative agent.yaml builder/runtime plus OCI packaging and multi-agent orchestration.
- **AMOS integration**: Generate agent.yaml per JSON agent, package 550 workflow MD as multi-agent orchestrations. Push/pull from OCI registry. docker agent run deployment.

### 84. Agent Network Protocol — agent-network-protocol/AgentNetworkProtocol (~1,407 stars)

- **Key feature**: Agent identity (DID), capability discovery, secure messaging, protocol negotiation.
- **AMOS integration**: Assign DIDs and agent descriptions to 549 agents. Agents discover each other, negotiate capabilities, exchange messages securely. Avoid hard-coded n² mesh.

### 85. OpenPackage — enulus/openpackage (~583 stars)

- **Key feature**: Universal package manager for agent skills, rules, commands, and agent configs.
- **AMOS integration**: Package 549 agents, 548 skills, 550 workflows into installable versioned config bundles. opkg install from CI/CD. Reproducible environment setup.

## Tooling Integration Order

1. **Catalog first**: Import SKILL.md → SkillHub, generate MCP server manifests → MCP Registry
2. **Runtime second**: Generate OpenAI Agents SDK agents and workflows from JSON + workflow MD
3. **Deploy third**: Convert to Docker Agent YAML, push to OCI registry
4. **Connect fourth**: Add ANP identities and discovery for agent-to-agent messaging
5. **Bundle fifth**: Wrap in OpenPackage for distribution and version control

## Honorable Mentions

- **mcp-gateway-registry** (~882 stars) — enterprise MCP gateway with OAuth/Entra/Keycloak, health checks, audit
- **Cotal** (~223 stars) — NATS/JetStream-based pub/sub coordination layer

## Agent Knowledge & RAG System Repos (2025-2026, Round 13)

### 86. Docling — docling-project/docling (~65,682 stars)

- **Key feature**: PDF/Office/image → structured Markdown/JSON/DocTags.
- **AMOS integration**: Batch-convert Obsidian vault (68,979 notes) and PDF/DOCX attachments to canonical Markdown + DocTags JSON. Feed normalized output into OpenViking, Haystack, Graphiti.

### 87. DSPy — stanfordnlp/dspy (~37,618 stars)

- **Key feature**: Program — not prompt — LLM reasoning with ChainOfThought, ReAct, optimizers.
- **AMOS integration**: Define dspy.Signature per agent type. Use ChainOfThought and ReAct for workflow-step reasoning. Optimize prompts with MIPROv2 on labeled workflow traces.

### 88. OpenViking — volcengine/OpenViking (~34,042 stars)

- **Key feature**: viking:// virtual filesystem unifying agent memory, RAG, and skills with L0-L2 on-demand loading.
- **AMOS integration**: Mount Obsidian vault, SKILL.md files, workflow MDs under viking:// protocol. Agents query context with ls/find semantics. L0/L1/L2 tier loading reduces per-turn tokens.

### 89. Graphiti — getzep/graphiti (~30,353 stars)

- **Key feature**: Temporal context graphs with entity extraction, provenance, incremental updates.
- **AMOS integration**: Ingest 68,979 Obsidian notes. Map wiki-links and frontmatter tags to typed graph edges. Track provenance from source note → chunk → entity. Multi-hop questions across skills/workflows.

### 90. agentmemory — rohitg00/agentmemory (~27,612 stars)

- **Key feature**: Persistent episodic coding-agent memory with confidence scoring, KG, hybrid search.
- **AMOS integration**: Capture execution traces and skill-usage patterns from 569 agents. Compress into searchable episodic memory with confidence scoring. Inject relevant memories at session start.

### 91. Haystack — deepset-ai/haystack (~26,317 stars)

- **Key feature**: Production RAG pipelines, routing, retrieval, memory, agent workflows.
- **AMOS integration**: Index Docling-normalized corpus in vector store + BM25. Create per-agent RAG pipelines using 568 SKILL.md as retrievable tool descriptions. Combine with Graphiti for hybrid graph+vector retrieval.

## Knowledge/RAG Integration Stack

1. **Ingest**: Docling normalizes entire Obsidian vault + SKILL.md/workflow files
2. **Structure**: OpenViking exposes corpus as virtual context filesystem
3. **Graph**: Graphiti builds temporal knowledge graph from notes and links
4. **Retrieve**: Haystack powers RAG and skill-routing for 569 agents
5. **Reason**: DSPy compiles chain-of-thought and tool-use reasoning
6. **Remember**: agentmemory persists episodic learnings across sessions

## Agent Deployment & CI/CD Repos (2025-2026, Round 14)

### 92. Nixopus — nixopus/nixopus (~1,460 stars)

- **Key feature**: Autonomous AI agent that analyzes a repo, generates infra config, deploys to VPS/K8s/Cloud, and self-heals failures.
- **AMOS integration**: Register each JSON agent + SKILL.md/workflow MD bundle as a Nixopus app. Push-triggered deploys with automatic SSL/routing. Agent reads logs and opens fix-PRs when workflows fail.

### 93. Langship — open-gitagent/langship.sh (~84 stars)

- **Key feature**: GitOps-native pipeline-as-graph: build → SAST → eval → policy → approval → deploy → promote → rollback.
- **AMOS integration**: Store a langship pipeline per agent family. Eval/Policy nodes run each SKILL.md and workflow MD through approval gates before promotion. GitOps for agent definitions and credentials.

### 94. Agentver — agentver/agentver (~17 stars)

- **Key feature**: Git-native semantic versioning, lockfiles, access control, security scanning, distribution of skills to 43+ assistants.
- **AMOS integration**: Treat 590 SKILL.md files as versioned Agentver skill packages. Publish on every release, pin skills.lock file. GitHub Action in CI ensures every agent resolves the same skill version.

### 95. Agent Health — opensearch-project/agent-health (~30 stars)

- **Key feature**: OpenTelemetry-native observability with Golden Path trajectory comparison, real-time execution streaming, batch experiments, self-hosted OpenSearch storage.
- **AMOS integration**: Instrument AMOS runtime to emit OTel traces. Define Golden Paths for 592 workflow MDs. Compare live trajectories and alert when agent deviates, stalls, or produces unexpected outputs.

### 96. AgentBudget — AgentBudget/agentbudget (~107 stars)

- **Key feature**: Per-session/per-run dollar and token budgets with real-time cost tracking, soft warnings, hard circuit-breakers, streaming-cost support.
- **AMOS integration**: Wrap every agent invocation with AgentBudget.init(). Read budget field from agent JSON metadata. Track token spend per SKILL.md/workflow. Auto-downgrade/abort before runaway agent exhausts budget.

### 97. AgentTrace — Rxflex/agenttrace (~13 stars)

- **Key feature**: Local-first step debugger: Python SDK decorators, interactive trace tree, prompt/response inspection, SQLite storage.
- **AMOS integration**: Add @trace_agent_run decorator to AMOS agent runner. Every workflow execution becomes a replayable trace. Easy to identify which SKILL.md step produced a bad tool call, loop, or error.

## Deployment/CI Integration Order

1. **Deploy**: Nixopus turns repo into auto-deployed agent fleet
2. **Pipeline**: Langship adds gated multi-environment promotion
3. **Version**: Agentver locks skill versions for reproducibility
4. **Monitor**: Agent Health for production health/alerting with Golden Paths
5. **Budget**: AgentBudget as cost-gate in front of every LLM call
6. **Debug**: AgentTrace for dev-stage step debugging and profiling

## Additional Finds (Round 9 — 2026-08-28)

### 92. MCP Catalog — `reaatech/mcp-catalog` (new/niche)
- **Key feature**: Registry server for MCP server discovery with registration, search, health checks, schema aggregation, and access control.
- **AMOS integration**: Register AMOS tools/capabilities as MCP servers and let agents discover them dynamically via the catalog.

### 93. MCP Gateway & Registry — `agentic-community/mcp-gateway-registry` (~882 stars)
- **Key feature**: Enterprise MCP/AI asset registry and gateway with OAuth, unified agent/tool access, Kubernetes/ECS support, and audit trails.
- **AMOS integration**: Use as the enterprise control plane for AMOS agents, skills, and MCP servers with governed discovery and call logging.

### 94. MCP Registry — `modelcontextprotocol/registry` (community registry)
- **Key feature**: Community-driven registry service for MCP servers; app-store-like discovery and publishing for MCP clients.
- **AMOS integration**: Publish AMOS custom MCP servers to the community registry and consume third-party MCP servers from it.

### 95. agentregistry — `agentregistry-dev/agentregistry` (~466 stars)
- **Key feature**: One registry for MCP servers, AI agents, skills, and prompts with CLI, web UI, curation, and Kubernetes deployment.
- **AMOS integration**: Package and publish AMOS agents/skills/MCP servers as artifacts in a governed, searchable registry.

### 96. agent-discover — `keshrath/agent-discover` (new/niche)
- **Key feature**: MCP server registry and marketplace with dynamic proxy, single-call tool discovery, and on-demand activation without session restart.
- **AMOS integration**: Let AMOS agents discover and activate MCP tools at runtime without restarting sessions, extending capability on demand.

## Additional Finds (Round 8 — 2026-08-28)

### 87. AgentTelemetry — `Krishnachaitanyakc/AgentTelemetry` (~3 stars)
- **Key feature**: OpenTelemetry-based observability for AI agents with 9 agent-specific span kinds, 7 framework adapters, privacy levels, and fault-detection analysis.
- **AMOS integration**: Instrument AMOS workflow steps with OpenTelemetry spans; tag each step with RSCF state and AMOS domain for traceable reasoning.

### 88. Observra — `open-agent-ai-security/observra` (~21 stars)
- **Key feature**: Framework-agnostic telemetry for AI agents capturing LLM calls, tool calls, delegation, cost, and errors via the Common Information Model.
- **AMOS integration**: Stream AMOS agent runs into Observra to answer "what happened, how much did it cost, and was it normal?" across skills.

### 89. Agent Observatory — `rakeshguptak/agent-observatory` (new/niche)
- **Key feature**: Self-hosted observability and debugging platform with traces, execution DAGs, cost/latency analytics, hallucination risk, and reasoning drift.
- **AMOS integration**: Host a local alternative to LangSmith for AMOS; capture execution DAGs of multi-step workflows and detect reasoning drift.

### 90. agenttrail — `sodiumsun/agenttrail` (~194 stars)
- **Key feature**: Local observability map for AI coding agents; file watcher, run cards, plans, tool calls, and progress for Claude/Codex/Cursor.
- **AMOS integration**: Use agenttrail to maintain a live `PLAN.md` and `CLAUDE.md`/`.agents` map for AMOS development sessions without cloud dependencies.

### 91. AgentLens — `agentkitai/agentlens` (~17 stars)
- **Key feature**: Tamper-evident, SHA-256 hash-chained audit trail for AI agents with real-time dashboard, MCP-native, EU AI Act friendly.
- **AMOS integration**: Record every AMOS agent tool call, approval, and mutation as a verifiable audit trail for compliance and provenance.

## Additional Finds (Round 7 — 2026-08-28)

### 82. Snyk Agent Scan — `snyk/agent-scan` (new/niche)
- **Key feature**: Security scanner for AI agents, MCP servers, and skills; discovers installed agent components and scans for prompt injection, sensitive data handling, and malware.
- **AMOS integration**: Add to the AMOS validation pipeline to scan every new `SKILL.md` and agent JSON for prompt-injection and vulnerability risks before merge.

### 83. SkillSpector — `NVIDIA/SkillSpector` (~14.7k stars)
- **Key feature**: Security scanner for AI agent skills with 69 vulnerability patterns across 17 categories: prompt injection, data exfiltration, privilege escalation, supply chain, excessive agency, MCP least privilege.
- **AMOS integration**: Gate AMOS skill publication through SkillSpector; require a passing scan before any skill is promoted from PROPOSED to CONDITIONAL/FINAL.

### 84. Agent Audit — `headyzhang/agent-audit` (~224 stars)
- **Key feature**: Static security scanner for LLM agents with 72 rules mapped to the OWASP Agentic Top 10 (2026); prompt injection, secret leak, taint analysis, MCP config auditing.
- **AMOS integration**: Run `agent-audit` in CI on AMOS agents and workflows; map findings to the OWASP Agentic Top 10 and create repair tickets.

### 85. AgentScan — `thesfb/agentscan` (new/niche)
- **Key feature**: Deterministic, offline, zero-dependency security scanner for AI agent skills; detects shell, exfiltration, secrets, network calls, malware patterns, and supply-chain risks without executing the skill.
- **AMOS integration**: Use as a pre-install scanner in the AMOS skill store; local offline scanning for air-gapped or high-trust deployments.

### 86. agent-security — `empowered-humanity/agent-security` (new/niche)
- **Key feature**: 176 detection patterns with taint analysis, auto-classification, context flow tracing, runtime guard modules (SSRF, path traversal, exec allowlisting, webhook verification).
- **AMOS integration**: Add static + runtime security gates to AMOS; export SARIF to GitHub Code Scanning and enforce guards in the AMOS execution kernel.

## Additional Finds (Round 6 — 2026-08-28)

### 77. Claw-Eval — `claw-eval/claw-eval` (~752 stars)
- **Key feature**: Human-verified LLM-as-agent evaluation harness with 300 tasks, 2,159 rubrics, Pass^3 methodology, and 9 categories (Completion · Safety · Robustness).
- **AMOS integration**: Run AMOS agents through Claw-Eval tasks to score skill/workflow success, safety, and robustness with reproducible 3-trial passes.

### 78. GauntletBench — `gauntlet-benchmark/evaluation-harness` (new/niche)
- **Key feature**: Web-based agent generalization benchmark with 100 vision-intensive professional tasks across Circuit Designer, Flight Analyser, Video Editor, 3D Modeller, Workflow Builder.
- **AMOS integration**: Benchmark AMOS vision-grounded and tool-use capabilities on less-covered professional apps and report domain-specific scores.

### 79. reaatech Agent-Eval-Harness — `reaatech/agent-eval-harness` (new/niche)
- **Key feature**: Production TypeScript evaluation harness with trajectory, tool-use, cost, latency, LLM-as-judge, golden trajectories, and CI/CD regression gates.
- **AMOS integration**: Add AMOS skill execution tests to the harness; enforce cost/latency budgets and regression gates on workflow runs.

### 80. OmniaBench — `scuuy/OmniaBench` (~12 stars)
- **Key feature**: Broad diagnostic benchmark with 1,431 tasks across 90 level-1 / 354 level-2 domains, 10 capability and 8 atomic difficulty dimensions.
- **AMOS integration**: Map AMOS C01-C12 domains to OmniaBench taxonomy and run domain-specific evaluation subsets.

### 81. AgencyBench — `GAIR-NLP/AgencyBench` (~94 stars)
- **Key feature**: Benchmark for autonomous agents in 1M-token real-world contexts; long-horizon multi-step agency across extended scenarios.
- **AMOS integration**: Stress-test AMOS agents on long-context, multi-step real-world agency tasks and measure end-to-end task completion.

## Additional Finds (Round 5 — 2026-08-28)

### 72. agentmemory — `rohitg00/agentmemory` (~27.6k stars)
- **Key feature**: Persistent memory for coding agents (Claude Code, Cursor, Codex, Gemini, Copilot) with confidence scoring, lifecycle, knowledge graphs, hybrid search, and MCP.
- **AMOS integration**: Use as the memory substrate for AMOS agents; wire `SKILL.md` ingestion to the memory server and surface context through the MCP server.

### 73. TencentDB Agent Memory — `Tencent/TencentDB-Agent-Memory` (~24.6k stars)
- **Key feature**: Team-level memory hub turning conversations, docs, and code into governed, shared memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph).
- **AMOS integration**: Map the AMOS Obsidian vault to the team memory hub, exposing skills and LLM-Wiki as shared assets across agents.

### 74. Memoria — `matrixorigin/Memoria` (~551 stars)
- **Key feature**: Git-like version control for AI agent memory: snapshots, branches, merges, rollback, semantic search, contradiction detection, and quarantine.
- **AMOS integration**: Treat every AMOS skill/workflow edit as a memory commit; use Memoria for audit, rollback, and provenance of agent knowledge.

### 75. agent-memory — `ivanzwb/agent-memory` (new/niche)
- **Key feature**: TypeScript persistent memory for agents with working, conversation, and long-term memory, vector + keyword retrieval, SQLite/HNSW, and token budgeting.
- **AMOS integration**: Embed `agent-memory` as a local-first memory layer for AMOS agent sessions and RAG over the vault.

### 76. agentic-memory — `Verace-Pvt-Ltd/agentic-memory` (new/niche)
- **Key feature**: 6-layer persistent memory (sensory, working, episodic, semantic, long-term, procedural), non-destructive belief revision, and MCP server.
- **AMOS integration**: Integrate with AMOS C05 Mind & Behavior and Memory Systems as an MCP server; use the 6-layer model to ground RSCF/H-M-L memory claims.

## Additional Finds (Round 4 — 2026-08-28)

### 67. Nexus ARC — `ghabs-org/nexus-arc` (new/niche)

- **Key feature**: Git-native AI orchestration framework with auto-retry, timeout detection, graceful failure, persistent workflow state, audit trails, and provider fallback.
- **AMOS integration**: Persist every AMOS workflow run as a Git commit/branch with traceable artifacts and enforce human-in-the-loop approvals for M0-M2 mutations.

### 68. Agentic Workflow Orchestrator — `nzer8/workflow-orchestrator` (new/niche)

- **Key feature**: Turns GitHub Issues into autonomous, multi-provider AI workflows with evidence collection, audit trail, and automatic closure.
- **AMOS integration**: Route AMOS `UNKNOWN/GAP` and `CRITICAL_GAP` issues to autonomous agents that gather evidence, propose fixes, and report back with provenance.

### 69. Maestro-Flow — `Kang00369/maestro-flow` (new/niche)

- **Key feature**: Intent-driven workflow orchestration with adaptive lifecycle engine, self-reinforcing knowledge graph, visual dashboard, and hook injection across Claude/Codex/Gemini.
- **AMOS integration**: Map AMOS canon/skills to a knowledge graph that persists discoveries across sessions and injects relevant context into future agent runs.

### 70. ForgeFlow — `JoelJohnsonThomas/ForgeFlow` (new/niche)

- **Key feature**: Production-grade multi-agent workflow orchestrator using LangGraph, MCP, A2A, PostgreSQL+pgvector; supervisor hub-and-spoke, human approvals, semantic memory, circuit breakers, and LLM-as-judge.
- **AMOS integration**: Deploy AMOS as a supervisor + specialist agent team with human gates for high-impact actions and MCP-based tool swapping.

### 71. AgentFlow — `Yupoer/agentFlow` (new/niche)

- **Key feature**: Schema-controlled, resumable, verifiable multi-stage AI-agent workflow runtime with request normalizer, planner, executor, verifier, and assembler stages.
- **AMOS integration**: Convert AMOS workflow MD to AgentFlow JSON schemas for resumable, stage-gated execution with artifact-based verification.

## Agent Framework & Runtime Repos (2025-2026, Round 15)

### 98. LangGraph — langchain-ai/langgraph (~40,600 stars)
- **Key feature**: Stateful, cyclic/conditional agent graphs with durable execution and built-in checkpointing.
- **AMOS integration**: Parse 592 workflow MD files into StateGraph definitions (nodes=steps, edges=transitions). Map 590 JSON agents to node functions. SKILL.md as system_prompt. PostgresSaver/SqliteSaver checkpointer for long-running runs.

### 99. Pydantic AI — pydantic/pydantic-ai (~19,500 stars)
- **Key feature**: Type-safe agent runtime with Pydantic-validated structured outputs, durable execution, graph support.
- **AMOS integration**: Factory loads each JSON agent as pydantic_ai.Agent. BaseModel output schemas from agent JSON config. Graph/DurableExecution for workflow MD as typed resumable pipelines.

### 100. Agno — agno-agi/agno (~41,900 stars)
- **Key feature**: AgentOS runtime: turn agents into multi-tenant FastAPI services with sessions, tracing, scheduling, RBAC.
- **AMOS integration**: Convert JSON agents to Agno.Agent. SKILL.md as instructions. Register workflows as Agno Team/Workflow. Run AgentOS with Postgres + tracing for FastAPI service with 50+ endpoints.

### 101. OpenAI Agents SDK — openai/openai-agents-python (~28,900 stars)
- **Key feature**: Lightweight multi-agent SDK built around agents-as-tools, handoffs, guardrails, tracing.
- **AMOS integration**: Top-level triage/router agent picks best JSON agent by capability tags. Hierarchical routing for 590 agents. SKILL.md as instructions, workflow MD as handoff chains. Guardrails for I/O validation.

### 102. Dapr Agents — dapr/dapr-agents (~740 stars)
- **Key feature**: Kubernetes-native, durable workflow engine designed to run thousands of agents with built-in state and observability.
- **AMOS integration**: Package each JSON agent as DaprAgent/WorkflowActivity. SKILL.md as activity prompt. Workflow MD as Dapr Workflow definitions. Fan-out parallel branches. State store + pub/sub for checkpointing.

### 103. CrewAI — crewAIinc/crewAI (~57,700 stars)
- **Key feature**: Role-playing multi-agent crews with tasks, tools, and event-driven flows.
- **AMOS integration**: Map JSON agents to crewai.Agent with role/goal/backstory. SKILL.md to tools/tasks. Workflow MD to Crew/Flow with ordered Task chain. Process.hierarchical for manager-led delegation.

## Combined AMOS Architecture

```
AMOS artifacts
    ├── 590 JSON agents  → Agent catalog (metadata + capabilities)
    ├── 590 SKILL.md     → Instructions / tools / prompts
    └── 592 workflow MD  → Graph/Crew/Workflow definitions

Catalog & routing: OpenAI Agents SDK (triage) or LangGraph classifier
Graph orchestration: LangGraph (branching) + Pydantic AI (type-safe nodes)
State & durability: LangGraph checkpointer + Pydantic AI durable execution
Serving & lifecycle: Agno AgentOS (production API, sessions, RBAC)
Parallel execution: Dapr Agents (Kubernetes scale)
Role-based crews: CrewAI (collaborative agent teams)
```

## Highest-ROI Combination

- Python-first: LangGraph + Pydantic AI + Agno
- Kubernetes scale: CrewAI + Dapr Agents

## Agent Evaluation & Benchmarking Repos (2025-2026, Round 16)

### 104. OpenAI Evals — openai/evals (~19,205 stars)
- **Key feature**: Mature framework and registry for evaluating LLMs and LLM systems; supports custom evals, prompt-chain evals, Completion Function Protocol for tool-using agents.
- **AMOS integration**: Convert 613 JSON agent definitions into custom evals. Use 615 workflow MD files as scenario inputs. Run registry in CI for per-agent, per-workflow pass/fail baselines. Detect capability drift across model updates.

### 105. OpenRLHF — OpenRLHF/OpenRLHF (~9,950 stars)
- **Key feature**: High-performance, production-ready RLHF/RL infrastructure using Ray + vLLM; supports PPO, REINFORCE++, DAPO, async RL, multi-turn VLM agents.
- **AMOS integration**: Collect trajectory-level rewards from 615 workflow executions. Fine-tune underlying LLM powering 613 agents. Use async agent RL path to scale RL across full agent fleet without rebuilding orchestrator.

### 106. Laminar — lmnr-ai/lmnr (~3,191 stars)
- **Key feature**: OpenTelemetry-native observability platform for AI agents; auto-traces Vercel AI SDK, LangChain, OpenAI, Anthropic, Gemini; SQL over traces, real-time signals, 20x trace compression.
- **AMOS integration**: One-line instrumentation around AMOS runner. Every execution of 613 agents and 615 workflows becomes a trace with spans, tool calls, costs, latencies. SQL/signals to detect loops, cost spikes, failed handoffs.

### 107. Prompt Ops — meta-llama/llama-prompt-ops (~853 stars)
- **Key feature**: Automated prompt optimization for Llama models; transforms prompts tuned for other LLMs into Llama-optimized variants using query-response dataset and configurable metrics.
- **AMOS integration**: Treat 613 SKILL.md files as system prompts and 615 workflow MD files as query/trajectory corpora. Run prompt-ops per skill to generate optimized SKILL.md variants. A/B test against original, batch-merge winners.

### 108. OpenJudge — agentscope-ai/OpenJudge (~798 stars)
- **Key feature**: Holistic evaluation framework for AI agents with 50+ production graders, skill graders (threat analysis, declaration alignment, completeness, relevance, design quality), PawBench, continuous optimization loops.
- **AMOS integration**: Use skill graders directly against each SKILL.md to check alignment, completeness, relevance. Run PawBench-style harnesses over 615 workflow MD files. Store scores in leaderboard for continuous improvement.

### 109. Eval View — hidai25/eval-view (~129 stars)
- **Key feature**: Snapshot/regression testing for AI agents; records full trajectories (tool calls, parameters, order) and diffs against baselines offline, with optional LLM judge for output quality.
- **AMOS integration**: Snapshot each of 613 agents' behavior on 615 workflows. Add evalview check to CI so any edit to SKILL.md, JSON agent schema, or workflow file that changes tool-calling behavior is flagged before merge.

## Eval/Benchmark Integration Stack

1. **Baseline**: openai/evals + OpenJudge — convert agents + workflows into test cases and skill graders
2. **Watch**: Laminar — instrument AMOS runner to capture traces, costs, anomalies
3. **Optimize**: prompt-ops — per-skill optimization over 613 SKILL.md files
4. **Gate**: eval-view — snapshot regression tests in CI for every file change
5. **Improve**: OpenRLHF — use 615 workflow traces as preference data for distributed RLHF

## Agent UI/UX & Human Interaction Repos (2025-2026, Round 17)

### 110. Mission Control — builderz-labs/mission-control (~6,105 stars)
- **Key feature**: Self-hosted AI-agent control plane with task inbox, agent registration, runtime adapters, multi-agent missions, spend tracking, Aegis quality gates, operations dashboard.
- **AMOS integration**: Deploy via Docker Compose. Bulk-import 633 JSON agents as registrations. Link SKILL.md as capability docs. Convert workflow MD into mission templates. AMOS runtime adapter for start/stop/stream.

### 111. Agent Chat UI — langchain-ai/agent-chat-ui (~3,080 stars)
- **Key feature**: Next.js chat app for any LangGraph agent with streaming, tool-call rendering, reasoning steps, references, multi-modality, one-click Vercel deploy.
- **AMOS integration**: Build AMOS-LangGraph bridge exposing each agent as graph/assistant ID. SKILL.md as system prompt. Chat UI lists all 633 agents for streaming conversation with tool calls and reasoning.

### 112. Open Agent Builder — firecrawl/open-agent-builder (~2,605 stars)
- **Key feature**: No-code drag-and-drop workflow builder with 8 node types (Agent, MCP Tools, Transform, If/Else, While, User Approval, Start/End), real-time execution, template library.
- **AMOS integration**: Parse 635 workflow MD into visual pipeline JSON. Map agents to Agent nodes using 633 JSON definitions. SKILL.md as node instructions. User Approval nodes at risky steps. Export validated workflows back.

### 113. Agent Flow — patoles/agent-flow (~1,461 stars)
- **Key feature**: Interactive node-graph visualization of live agent sessions with tool calls, branching, JSONL replay, multi-session tabs, VS Code extension.
- **AMOS integration**: AMOS executor emits JSONL events. Agent Flow visualizes which of 633 agents are active in 635 workflows. Spot stuck, looping, or failing agents in real time.

### 114. Approving — cocofhu/approving (~74 stars)
- **Key feature**: Self-hostable HITL platform with FSM workflows, Docker sandboxes, MCP artifacts, visual human approval gates before critical actions.
- **AMOS integration**: Run AMOS workflow executor in Approving's Docker sandbox. Translate workflow MD into FSM with human-gate nodes at critical points. Reviewers approve/reject/revise. Persist decisions as audit trail.

### 115. Skills Marketplace — dukelyuu/skills-marketplace (~25 stars)
- **Key feature**: Marketplace UI for SKILL.md files with full-text search, filtering, one-click import, built-in skill editor, source sync.
- **AMOS integration**: Add AMOS repo as source. 633 SKILL.md auto-indexed into skill cards with tags. Users search/filter and one-click import. Edits write back to SKILL.md and sync to Git.

## UI/UX Integration Stack

1. **Control panel**: Mission Control — central AMOS operations cockpit
2. **Chat interface**: Agent Chat UI — streaming chat with any of 633 agents
3. **Visual builder**: Open Agent Builder — drag-and-drop workflow testing
4. **Flow visualization**: Agent Flow — live agent session node-graph
5. **Human approval**: Approving — HITL gates at critical workflow steps
6. **Skill marketplace**: Skills Marketplace — searchable catalog of 633 skills

## Agent Memory & Context Management Repos (2025-2026, Round 18)

### 116. Mem0 — mem0ai/mem0 (~64,000 stars)
- **Key feature**: Single-pass ADD-only memory extraction, entity linking, hybrid recall (semantic + BM25 + entity matching). Self-hostable memory server with per-user/per-agent scopes.
- **AMOS integration**: Attach stable agent_id from each of 653 JSON agents. Index 653 SKILL.md as reference docs. After workflow run, call m.add() with distilled facts. At new workflow start, call m.search() for top-k relevant memories per agent_id.

### 117. Khoj — khoj-ai/khoj (~36,700 stars)
- **Key feature**: Semantic search over heterogeneous documents (PDF, .md, .org, Notion), custom agents with knowledge, scheduled automation, long-term memory support.
- **AMOS integration**: Entire 1,961-file corpus (653 SKILL.md + 655 workflow .md + 653 agent JSONs) becomes searchable knowledge base. Create one custom Khoj agent per JSON agent. Use /query or api/chat endpoint inside each AMOS agent step.

### 118. OpenViking — volcengine/OpenViking (~34,000 stars)
- **Key feature**: viking:// virtual filesystem where memories, resources, and skills are URI-addressable; three-tier context loading (L0 abstract → L1 overview → L2 detail); session-to-memory distillation.
- **AMOS integration**: Mount amos/skills/ and amos/workflows/ under viking://. Let OpenViking build L0/L1/L2 summaries. In each agent step, call viking.find(query) for tiered context. After workflow completes, commit session for memory distillation.

### 119. AgentMemory — rohitg00/agentmemory (~27,600 stars)
- **Key feature**: Persistent memory with confidence scoring, lifecycle management, knowledge-graph construction, hybrid search, MCP server. Works across Claude Code, Cursor, Codex.
- **AMOS integration**: Install agentmemory MCP server. Map 653 JSON agents to agentmemory identities. Ingest 653 SKILL.md as skills and 655 workflow files as sessions. Auto-extract entities and link in knowledge graph. Use agentmemory.search() at session start.

### 120. Letta — letta-ai/letta (~24,400 stars)
- **Key feature**: MemGPT-style core vs. archival memory, memory blocks, sleep-time consolidation ("dreaming"), skill learning, MemFS (git-backed context storage).
- **AMOS integration**: Define one Letta agent per JSON agent. Use memory_blocks for each skill/workflow split between core_memory (active) and archival_memory (long-term). Schedule sleeptime/dreaming consolidation runs to compress 1,961-file corpus. Track all context in Git via MemFS.

### 121. Neo4j Agent Memory — neo4j-labs/agent-memory (~489 stars)
- **Key feature**: POLE+O memory model with short-term (conversations), long-term (entities/facts/preferences), and reasoning (tool-usage traces) layers; entity/relationship extraction; 16-tool MCP server.
- **AMOS integration**: Spin up Neo4j + agent-memory MCP server. Import 653 SKILL.md and 655 workflow files as Skill and Workflow nodes. Link to 653 Agent nodes with HAS_SKILL, USES_WORKFLOW, PRODUCED_OUTPUT edges. Expose MCP tools in AMOS for runtime graph queries.

## Memory/Context Integration Phases

1. **Phase 1 — Retrieval baseline**: Index all SKILL.md + workflow .md in Khoj or OpenViking
2. **Phase 2 — Agent memory**: Add mem0 or agentmemory per agent_id for fact retention
3. **Phase 3 — Graph reasoning**: Import skill/workflow/agent relationships into neo4j-labs/agent-memory
4. **Phase 4 — Long-horizon compression**: Wrap long workflows in Letta for context paging and sleep-time consolidation
5. **Phase 5 — Self-evolving skills**: Use OpenViking or agentmemory to distill successful workflow runs back into updated SKILL.md files

### 122. Aegis — Justin0504/Aegis (~332 stars)
- **Key feature**: Pre-execution firewall for AI agents. Intercepts, classifies, and blocks tool calls in real time. RFC 6962 transparency log (append-only Merkle tree), human-in-the-loop approvals, kill switch. Agent Threat Ontology v1 (10 tactics × 40 techniques). LLM egress proxy for OpenAI/Anthropic. Zero agent code changes.
- **AMOS integration**: Wrap every AMOS agent tool call through Aegis gateway. Map AAT-T* threat taxonomy to AMOS security-safety-master skills. Use transparency log as external attestation for AMOS enforcement_root_attestation (ERA) and enforcement_trust_contract (ETC). Deploy as MCP server alongside AMOS agents.

### 123. Agent Safehouse — eugene1g/agent-safehouse (~2,035 stars)
- **Key feature**: macOS sandbox for LLM coding agents using `sandbox-exec` with composable deny-first policy profiles. Least-privilege file/integration access. Profiles for major coding agents. Hardening layer, not perfect boundary.
- **AMOS integration**: Use as the macOS execution substrate for AMOS executor-agent and code-agent-harness. Map AMOS capability grants to safehouse policy profiles. Enforce AMOS M0-M5 mutation classification through sandbox-exec deny rules. Deploy AMOS agents inside safehouse profiles keyed to their capability envelope.

### 124. OpenSandbox — alibaba/OpenSandbox (~14,596 stars)
- **Key feature**: General-purpose sandbox platform for AI applications. Multi-language SDKs, CLI, MCP server. Docker/Kubernetes runtimes. gVisor/Kata/Firecracker microVM isolation. Credential vault, network policy, ingress gateway. Supports coding agents, GUI agents, evaluation, RL training.
- **AMOS integration**: Deploy AMOS agents as OpenSandbox workloads. Use credential vault for AMOS agent identity (SPIFFE-style). Map AMOS delegation-witness to OpenSandbox lifecycle management. Use Kubernetes runtime for large-scale AMOS multi-agent orchestration. MCP server integration for AMOS workflow-runner.

### 125. Agent-Sandbox — agent-sandbox/agent-sandbox (~202 stars)
- **Key feature**: Enterprise-grade sandbox wrapping kubernetes-sigs/agent-sandbox behind RESTful API + MCP server. Multi-tenant isolation for untrusted LLM-generated code, browser use, computer use, website deployment. E2B-compatible API.
- **AMOS integration**: Use as the REST/MCP front-end for AMOS agent execution. Map AMOS agent-skill-workflow triads to Agent-Sandbox REST endpoints. Deploy AMOS code-agent-harness inside Agent-Sandbox containers. Use MCP server for AMOS workflow-runner remote execution. Multi-tenant isolation maps to AMOS shard-local (L25) law enforcement.

## Security/Safety Integration Phases

1. **Phase 1 — Local sandboxing**: Wrap AMOS executor-agent in Agent Safehouse on macOS dev machines
2. **Phase 2 — Tool-call firewall**: Deploy Aegis gateway as MCP server intercepting all AMOS agent tool calls
3. **Phase 3 — Container isolation**: Migrate AMOS agents to OpenSandbox Docker/Kubernetes runtime with gVisor
4. **Phase 4 — Multi-tenant execution**: Use Agent-Sandbox REST API for remote AMOS workflow execution
5. **Phase 5 — Transparency attestation**: Feed Aegis RFC 6962 transparency log into AMOS ERA/ETC attestation chain

## Agent Security, Evaluation & Tooling Repos (2025-2026, Round 14)

### 126. garak — NVIDIA/garak (~9,000 stars)

- **Key feature**: LLM vulnerability scanner probing models and agent pipelines for prompt injection, jailbreaks, data leakage, hallucination, toxicity, and misinformation.
- **AMOS integration**: Built-in red-team capability to stress-test skills and agent workflows before they are exposed to untrusted inputs. Adaptive probe suites and automated vulnerability reports run as a CI/CD safety gate for new AMOS skills.

### 127. SWE-bench — SWE-bench/SWE-bench (~5,700 stars)

- **Key feature**: Evaluates language models on real-world GitHub issues by asking them to generate patches that actually resolve reported bugs.
- **AMOS integration**: Rigorous, code-level benchmark for measuring how well AMOS coding agents/skill workflows perform on realistic software engineering tasks. Containerized evaluation harness and issue-to-patch dataset reused to score and compare AMOS coding skill releases.

### 128. promptfoo — promptfoo/promptfoo (~24,400 stars)

- **Key feature**: CLI and library for LLM evaluation and red teaming, supporting prompt versioning, side-by-side model comparison, and automated security tests.
- **AMOS integration**: Systematic evaluation of prompts and skill outputs as well as adversarial testing for prompt injection and jailbreaks. Declarative test cases and CI-integrated eval runs validate every AMOS skill before deployment.

### 129. mem0 — mem0ai/mem0 (~63,800 stars)

- **Key feature**: Intelligent memory layer for LLM agents, remembering user preferences and context across conversations.
- **AMOS integration**: Persistent, user-specific memory to AMOS skills so agents learn and adapt across sessions. Self-improving memory retrieval and automatic relevance scoring for contextual skill execution.

### 130. AgentOps — AgentOps-AI/agentops (~5,800 stars)

- **Key feature**: Observability and DevTool platform for AI agents, providing session tracking, cost monitoring, benchmarking, and replay analytics.
- **AMOS integration**: Out-of-the-box monitoring and debugging for AMOS agent runs, including cost and latency tracking. Session-based tracing and replay analytics to diagnose skill failures and optimize agent performance.

### 131. Phoenix — Arize-ai/phoenix (~11,200 stars)

- **Key feature**: Open-source AI observability and evaluation platform for tracing, experimenting with, and troubleshooting LLM and agent applications.
- **AMOS integration**: Visual trace inspection, evaluation datasets, and model-agnostic instrumentation to AMOS. OpenTelemetry-based tracing and built-in evals for every AMOS skill and multi-step agent workflow.

### 132. Guardrails AI — guardrails-ai/guardrails (~7,300 stars)

- **Key feature**: Open-source framework for adding structured, programmable validation and guardrails to LLM inputs and outputs.
- **AMOS integration**: Enforce output schemas, content policies, and safety constraints on every skill result. Composable validators and re-asking logic attached to individual AMOS skills as policy gates.

## Round 14 Integration Priority

1. **Security**: Adopt `garak` for red-teaming skills and `guardrails-ai/guardrails` for input/output policy enforcement.
2. **Evaluation**: Use `SWE-bench` for coding skills and `promptfoo` for prompt-level regression tests.
3. **Memory**: Integrate `mem0` for lightweight user memory across AMOS agent sessions.
4. **Observability**: Instrument AMOS with `AgentOps` and `Phoenix` to trace, debug, and evaluate agent runs in production.

## Provenance (Round 14)

- **Research date**: 2026-08-28
- **Researcher**: Devin subagent (web search, live GitHub metadata)
- **Epistemic class**: EMPIRICAL (star counts from GitHub, may change)
- **RSCF state**: SOURCE_CLAIM (repo features from README/docs)

## Additional Finds (Round 19 — 2026-09-08)

### 133. Microsoft Agent Framework (MAF) — microsoft/agent-framework (~12,590 stars)
- **Key feature**: Open, multi-language (Python + .NET) framework for production-grade AI agents and multi-agent workflows. Graph-based orchestration (sequential, concurrent, handoff, group collaboration), checkpointing, streaming, human-in-the-loop, time-travel, durability, restartability, observability, governance. Foundry-hosted agents, Azure OpenAI, OpenAI, GitHub Copilot SDK support.
- **AMOS integration**: Map 590 JSON agents to MAF Agent definitions (Python). SKILL.md as agent instructions. 592 workflow MD files → MAF Workflows with graph-based patterns (sequential/concurrent/handoff/group). Checkpointing for long-running AMOS runs. Human-in-the-loop gates at M0-M2 mutation boundaries. Time-travel for debugging failed workflows. Foundry hosting for cloud-scale AMOS deployment.

### 134. Open Multi-Agent (OMA) — JackChen-me/open-multi-agent (~6,836 stars)
- **Key feature**: TypeScript AI agent orchestration framework with dynamic workflows. "Describe the goal, not the graph" — coordinator plans task DAG at runtime, deterministic scheduler executes across team. Runs on any LLM (Claude, ChatGPT, Gemini, DeepSeek, local models). Built-in offline Run Viewer for replay. MCP support. Inspectable, approvable, replayable runs.
- **AMOS integration**: TypeScript backend alternative to LangGraph. Each AMOS goal → OMA `runTeam()` with coordinator planning DAG from 590 agents. SKILL.md as agent instructions. Workflow MD → `runTasks()` explicit pipelines. Run Viewer for AMOS workflow replay and audit. Local model support for air-gapped AMOS deployments. MCP integration for AMOS tool discovery.

### 135. Hecate — xueyufish/hecate (new/niche)
- **Key feature**: Enterprise-grade, multi-tenant, model-agnostic, MCP-first Agent platform. Self-developed Pregel execution runtime. MCP and A2A native. 100+ LLM integrations. OpenAI-compatible API. Multi-agent orchestration with persistence, graph-based state, durable checkpoints, human-in-the-loop. Organization → Workspace → RBAC. Docker-isolated sandbox execution. Engine-level guardrails. Visual canvas for drag-and-drop workflow design.
- **AMOS integration**: Deploy AMOS as Hecate workspaces with RBAC mapping to AMOS authority canon (L7). Pregel runtime for AMOS workflow graph execution. MCP-native tool discovery. A2A protocol for cross-agent orchestration. Docker sandbox isolation maps to AMOS capability-bound governance. Visual canvas for AMOS workflow design. OpenAI-compatible API for drop-in integration.

### 136. OxyGent — jd-opensource/OxyGent (ACL 2026)
- **Key feature**: Open-source modular multi-agent framework unifying tools, models, and agents into standardized "Oxy" components. LEGO-brick assembly with hot-swapping and cross-scenario reuse. Dynamic planning paradigms where agents decompose tasks, negotiate solutions, adapt in real-time. Elastic architecture supporting any topology (ReAct to complex hybrid). Full auditability of every decision. ACL 2026 paper.
- **AMOS integration**: Map AMOS skills/agents/workflows to Oxy components for hot-swapping without downtime. Dynamic planning for AMOS workflow adaptation. Elastic topology for AMOS C01-C12 domain agents. Auditability feeds AMOS enforcement_root_attestation (ERA) chain. Cross-scenario reuse of AMOS skills across different agent configurations.

### 137. OpenAgentBench — generalaimodels/OpenAgentBench (new/niche)
- **Key feature**: Research-grade evaluation & verification platform for LLM agents, RAG pipelines, and tool-using workflows. Evaluates agents as stateful control systems, not transcript generators. Scores: final outcomes, environment-state correctness, tool-selection optimality, privilege safety, memory hygiene, grounding faithfulness, recovery behavior, multi-agent coordination quality, efficiency under failure and adversarial conditions. Chaos engineering and red-teaming for agents.
- **AMOS integration**: Evaluate AMOS agents on privilege safety (maps to L7 authority canon), memory hygiene (maps to memory systems), recovery behavior (maps to L10 failure recovery), multi-agent coordination (maps to agent systems). Chaos engineering for AMOS runtime stability testing. Provenance-based verification aligns with RSCF epistemic framework.

### 138. AgentCompass — open-compass/AgentCompass (new/niche)
- **Key feature**: Unified open-source evaluation framework for agents. Decouples Model, Benchmark, Harness, and Environment. 20+ public benchmarks, 10+ agent harnesses (Claude Code, Codex, OpenHands, OpenClaw). Local execution, Docker, remote sandboxes. Concurrent scheduling, incremental persistence, retry-on-failure, resumable evaluations. Trajectory recording with tool calls, usage, latency. Pluggable analyzers for failure detection.
- **AMOS integration**: Register AMOS agents as harnesses in AgentCompass. Run 20+ benchmarks against AMOS agent fleet. Map AMOS C01-C12 domains to benchmark categories. Resumable evaluations for long-running AMOS workflows. Trajectory analysis to detect AMOS agent failures, loops, and abnormal behavior. Docker/remote sandbox execution for isolated AMOS eval.

### 139. AgentEval — agentkitai/agenteval (new/niche)
- **Key feature**: Testing and evaluation framework for AI agents. YAML-based test suites, 11 pluggable graders (exact, contains, regex, tool-check, trajectory, LLM-judge, custom, JSON-schema, semantic, latency, cost). Statistical regression detection via Welch's t-test across multiple runs. AgentLens integration for production session import. Cost & latency tracking. SQLite result storage for historical comparison.
- **AMOS integration**: Define YAML test suites per AMOS skill (590 SKILL.md files). Trajectory grader for AMOS workflow step ordering. JSON-schema grader for AMOS agent output validation. Statistical regression detection for AMOS skill versioning. AgentLens integration for tamper-evident audit evidence (maps to ERA/ETC). Cost/latency tracking for AMOS token-budget governance.

### 140. MemoryAgentBench — felipetruman/MemoryAgentBench (ICLR 2026)
- **Key feature**: Open-source benchmark for evaluating memory in LLM agents via incremental multi-turn interactions. Four core competencies: Accurate Retrieval (AR), Test-Time Learning (TTL), Long-Range Understanding (LRU), Conflict Resolution (CR). "Inject once, query multiple times" design. EventQA and FactConsolidation datasets. ICLR 2026 accepted.
- **AMOS integration**: Benchmark AMOS memory systems (3 memory types, context compaction, conflict resolution, immune system). Map AR/TTL/LRU/CR to AMOS memory retrieval, learning, long-context, and conflict governor skills. Evaluate AMOS agent memory across multi-turn interactions. Conflict Resolution competency maps directly to AMOS memory-conflict-governor.

### 141. EvalAgentLab — Cap-alfaMike/eval-agent-lab (new/niche)
- **Key feature**: Production-grade evaluation platform for LLM outputs, agent execution traces, and tool-augmented workflows. 11 metrics spanning accuracy, semantics, hallucination, tool use, strategy compliance, and reasoning. Formal rubric system with JSON-configurable weights. Evaluates "how agents arrive at the answer" not just final output. HuggingFace dataset integration. 117 passing tests.
- **AMOS integration**: 11 metrics for AMOS agent evaluation. Hallucination metric for RSCF epistemic validation. Tool-use metric for AMOS capability-bound governance. Strategy compliance for AMOS workflow adherence. Formal rubric system for AMOS promotion gates. HuggingFace dataset for AMOS benchmark publishing.

## Round 22 — New SOTA Repos (2026-09-08)

### 142. Microsoft Agent Framework (MAF) — `microsoft/agent-framework` (~13,169 stars)
- **Key feature**: Open, multi-language framework (Python, .NET, Go) for production-grade AI agents and multi-agent workflows. Graph-based orchestration (sequential, concurrent, handoff, group collaboration), checkpointing, streaming, human-in-the-loop, time-travel. Native Agent Skills support following agentskills.io spec.
- **AMOS integration**: Map AMOS agents to MAF Agent definitions; compile AMOS Markdown workflows into MAF graph nodes/edges. Use MAF's durable execution for AMOS runtime pipeline persistence. MAF's native skills support aligns directly with AMOS SKILL.md format.

### 143. DeerFlow 2.0 — `bytedance/deer-flow` (~78,953 stars)
- **Key feature**: Open-source super-agent harness with sub-agents, memory, sandboxes, and extensible skills. Built on LangGraph/LangChain. Skills are structured Markdown capability modules. #1 on GitHub Trending (2026-08-28). Filesystem, memory, sandbox-aware execution, sub-agent spawning.
- **AMOS integration**: Adopt DeerFlow's skill-as-markdown pattern (matches AMOS SKILL.md). Use sub-agent spawning for AMOS delegation lifecycle. Sandbox-aware execution maps to AMOS capability-bound governance. Memory system parallels AMOS 3-memory-type architecture.

### 144. Dapr Agents — `dapr/dapr-agents` (~743 stars)
- **Key feature**: Production-grade resilient AI agent systems on Dapr runtime. Durable-execution workflow engine with automatic retries. Kubernetes-native. Thousands of agents per core. Vendor-neutral, observable by default. Multi-agent systems secure and observable.
- **AMOS integration**: Dapr's durable workflow engine for AMOS runtime pipeline. Kubernetes-native deployment for AMOS production. Automatic retries map to AMOS L10 failure recovery. Observability by default for AMOS audit trail. Multi-agent security for AMOS agent-to-agent protocols.

### 145. Agent Skills Specification — `agentskills.io/agentskills` (specification)
- **Key feature**: Open format for packaging specialized knowledge, workflows, and code into portable skill directories. Progressive disclosure: metadata (~100 tokens) → instructions (<5000 tokens) → resources (as needed). SKILL.md with YAML frontmatter (name, description, license, compatibility, metadata, allowed-tools). Discovery paths: `.agents/skills/` (cross-client standard).
- **AMOS integration**: AMOS SKILL.md files already follow this spec closely. Formalize alignment: ensure `name` matches parent directory, `description` < 1024 chars with trigger keywords, `allowed-tools` field for capability bounds. Adopt `.agents/skills/` as secondary discovery path.

### 146. MCP Skills Extension (SEP-2640) — `modelcontextprotocol/modelcontextprotocol`
- **Key feature**: Convention for serving Agent Skills over MCP using existing Resources primitive. Skills exposed as `skill://` URI resources. `skill://index.json` enumerates skills and templates. Transport binding only — skill format delegated to agentskills.io spec.
- **AMOS integration**: Expose AMOS skills via MCP `skill://` URIs. Generate `skill://index.json` from AMOS skill registry. Enables external MCP-compatible clients to discover and load AMOS skills on demand.

### 147. MCP Gateway Registry (Agent Skills) — `agentic-community/mcp-gateway-registry`
- **Key feature**: Agent Skills architecture with SkillCard entity (path, name, description, URLs, metadata, requirements, target_agents, ToolReference, visibility, owner). Progressive disclosure tiers. Federated skills with inline content. Pydantic models following agentskills.io spec.
- **AMOS integration**: SkillCard model for AMOS skill registry entries. ToolReference for AMOS allowed-tools linking. Visibility field for AMOS public/private skill governance. Federated skills for cross-vault AMOS skill sharing.

### 148. SWE-bench-Live — `microsoft/SWE-bench-Live` (NeurIPS 2025)
- **Key feature**: First automatically-updating, multi-language, multi-OS SWE task set for agentic benchmarking. 1,077+ MultiLang tasks (6 languages, 381 repos). Windows split (61 tasks, 6 languages). Docker sandbox per task. RepoLaunch automated build/test.
- **AMOS integration**: Benchmark AMOS C10 tech-engineering agents on real-world SWE tasks. Multi-language coverage for AMOS cross-domain agents. Docker sandbox isolation maps to AMOS capability-bound governance. Contamination-free evaluation for AMOS agent regression testing.

### 149. SWE-bench Pro — enterprise benchmark (arxiv 2509.16941)
- **Key feature**: 1,865 problems from 41 actively maintained repos (business apps, B2B services, dev tools). Long-horizon tasks (hours to days). Multi-file patches, substantial code modifications. GPT-5 SOTA at 23.3% Pass@1. Contamination-resistant.
- **AMOS integration**: Enterprise-grade benchmark for AMOS complex reasoning agents. Long-horizon task evaluation for AMOS workflow runner. Multi-file patch assessment for AMOS formal engines. Failure mode clustering for AMOS audit-repair master.

### 150. SWE-rebench — continuous decontaminated benchmark (NeurIPS 2025)
- **Key feature**: 21,000+ interactive Python-based SWE tasks for RL training. Automated pipeline for continuous fresh task extraction. Decontaminated leaderboard. Suitable for reinforcement learning at scale.
- **AMOS integration**: Large-scale RL training data for AMOS agent evolution. Continuous fresh tasks prevent benchmark contamination in AMOS evaluation cycles. Interactive task format matches AMOS runtime pipeline (perceive→execute→observe).

## Round 22 Integration Priority

1. **Production orchestration**: Microsoft Agent Framework (MAF) — Python/.NET/Go, durable execution, native skills support
2. **Super-agent harness**: DeerFlow 2.0 — skill-as-markdown, sub-agents, sandbox, memory (78k stars, #1 trending)
3. **K8s-native runtime**: Dapr Agents — durable workflows, auto-retry, observable multi-agent at scale
4. **Spec alignment**: Agent Skills Specification (agentskills.io) — formalize AMOS SKILL.md compliance
5. **MCP skill serving**: SEP-2640 — expose AMOS skills via `skill://` URIs over MCP
6. **Skill registry**: MCP Gateway Registry — SkillCard model, ToolReference, federated skills
7. **Enterprise eval**: SWE-bench-Live + SWE-bench Pro — multi-language, long-horizon, contamination-resistant
8. **RL training data**: SWE-rebench — 21k+ interactive tasks for AMOS agent evolution

## Round 19 Integration Priority

1. **Production orchestration**: Microsoft Agent Framework (MAF) for Python/.NET production AMOS deployment with durability and governance
2. **TypeScript alternative**: Open Multi-Agent (OMA) for Node.js-based AMOS with dynamic DAG planning
3. **Enterprise platform**: Hecate for multi-tenant AMOS with RBAC, Pregel runtime, and visual canvas
4. **Modular composition**: OxyGent for hot-swappable Oxy components with ACL 2026 backing
5. **Control-plane eval**: OpenAgentBench for privilege-safety and recovery-behavior verification
6. **Unified eval**: AgentCompass for 20+ benchmarks across AMOS agent fleet
7. **Regression testing**: AgentEval for YAML test suites with statistical regression detection
8. **Memory benchmarking**: MemoryAgentBench for AMOS memory system evaluation (ICLR 2026)
9. **Trace evaluation**: EvalAgentLab for execution-trace metrics and rubric-based scoring

## Provenance (Round 19)

- **Research date**: 2026-09-08
- **Researcher**: Devin (web search, live GitHub metadata)
- **Epistemic class**: EMPIRICAL (star counts from GitHub, may change)
- **RSCF state**: SOURCE_CLAIM (repo features from README/docs)

## Round 23 — 2025/2026 New Open-Source AI Agent Tooling (2026-09-08)

> All repos below are new (created or released 2025-2026) and are NOT in the existing 150+ AMOS SOTA set. Star counts approximate as of search date.

### 151. skillimage — `redhat-et/skillimage` (~8 stars)
- **Key feature**: Packages AI agent skills as signed, lifecycle-managed OCI images distributed through any standard OCI registry.
- **AMOS integration**: Publish AMOS skill packs as OCI artifacts so they can be pulled, versioned, and mounted into agent pods just like container images.

### 152. Pydantic AI — `pydantic/pydantic-ai` (~19.5k stars)
- **Key feature**: Type-safe, model-agnostic Python agent SDK with built-in structured outputs, sub-agents, memory, and durable execution.
- **AMOS integration**: Use Pydantic AI for type-validated AMOS skill runners that swap models with a single string change.

### 153. Google ADK — `google/adk-python` (~21.2k stars)
- **Key feature**: Code-first, modular toolkit for building, evaluating, and deploying multi-agent workflows; optimized for Gemini but framework-agnostic.
- **AMOS integration**: Evaluate ADK's tool-use/orchestration primitives as a runtime backend for AMOS agent pipelines.

### 154. smolagents — `huggingface/smolagents` (~28.9k stars)
- **Key feature**: Minimal library for agents that think and act in Python code rather than JSON tool-call blobs.
- **AMOS integration**: Wrap smolagents code-execution agents as AMOS skills for math, coding, and data-science workflows.

### 155. Agno — `agno-agi/agno` (~41.9k stars)
- **Key feature**: Lightweight, multi-modal agent framework with memory, tools, reasoning, and multi-agent teams.
- **AMOS integration**: Embed Agno as a fast, framework-agnostic execution engine for individual AMOS skills.

### 156. AgentScope — `agentscope-ai/agentscope` (~29.7k stars)
- **Key feature**: Production-ready multi-agent framework with ReAct loops, MCP support, and rich building blocks.
- **AMOS integration**: Port AMOS skills into AgentScope toolkits and leverage its ReAct/multi-agent runtime.

### 157. Dapr Agents — `dapr/dapr-agents` (~743 stars)
- **Key feature**: Durable, Kubernetes-native multi-agent framework built on the Dapr actor/workflow runtime.
- **AMOS integration**: Deploy AMOS agent swarms on Dapr to get resilient execution, state, and observability out of the box.

### 158. Mastra — `mastra-ai/mastra` (~27.3k stars)
- **Key feature**: Graph-based TypeScript workflow engine for AI apps with `.then()`, `.branch()`, and `.parallel()` control flow.
- **AMOS integration**: Orchestrate AMOS skill chains using Mastra's explicit workflow semantics and tracing.

### 159. Trigger.dev — `triggerdotdev/trigger.dev` (~16.1k stars)
- **Key feature**: Open-source TypeScript platform for durable, long-running AI workflows with retries, queues, and elastic scaling.
- **AMOS integration**: Schedule long-running AMOS agent jobs with built-in retries and observability.

### 160. Inngest — `inngest/inngest` (~5.7k stars)
- **Key feature**: Durable, event-driven step-function engine for serverless and self-hosted workflows.
- **AMOS integration**: Trigger AMOS skill runs from events and fan out multi-agent workflows.

### 161. Letta — `letta-ai/letta` (~24.4k stars)
- **Key feature**: Stateful agent framework where agents rewrite and evolve core/archival memory over time.
- **AMOS integration**: Persist AMOS agent sessions with Letta's self-improving memory blocks.

### 162. Mem0 — `mem0ai/mem0` (~62.5k stars)
- **Key feature**: Drop-in, model-agnostic memory layer for agents and assistants with user/session/agent scoped recall.
- **AMOS integration**: Add cross-session user and agent memory to AMOS without pipeline changes.

### 163. Aegis — `Justin0504/Aegis` (~332 stars)
- **Key feature**: Pre-execution firewall for AI agents: classifies tool calls, enforces runtime policy, and writes tamper-evident audit trails.
- **AMOS integration**: Gate every AMOS tool call through Aegis with policy checks and cryptographically signed logs.

### 164. Agent Governance Toolkit — `microsoft/agent-governance-toolkit` (~6.1k stars)
- **Key feature**: OWASP Top 10 for Agentic AI coverage, zero-trust identity, sandboxing, and deterministic policy enforcement.
- **AMOS integration**: Apply Microsoft's OWASP-mapped governance controls and SRE primitives to AMOS deployments.

### 165. AgentDoG — `AI45Lab/AgentDoG` (~634 stars)
- **Key feature**: Diagnostic guardrail and scalable safety-alignment framework for modern agentic systems, with the ATBench trajectory family.
- **AMOS integration**: Use AgentDoG to diagnose and align AMOS agent trajectories against its safety taxonomy.

### 166. Inspect — `UKGovernmentBEIS/inspect_ai` (~2.6k stars)
- **Key feature**: UK AISI framework for building and running LLM/agent evaluations with solvers, scorers, and 200+ built-in evals.
- **AMOS integration**: Run AMOS skill and agent benchmarks inside Inspect's reproducible evaluation harness.

### 167. FastMCP — `PrefectHQ/fastmcp` (~27.4k stars)
- **Key feature**: Fast, Pythonic framework for building MCP servers, clients, and interactive apps.
- **AMOS integration**: Expose AMOS tools as MCP servers with auto-generated schemas and validation.

### 168. mcp-use — `mcp-use/mcp-use` (~10.5k stars)
- **Key feature**: Full-stack TypeScript MCP framework for building ChatGPT/Claude apps and MCP servers.
- **AMOS integration**: Let AMOS agents consume remote mcp-use servers with typed tool-to-UI contracts.

### 169. mcp-go — `mark3labs/mcp-go` (~9k stars)
- **Key feature**: Go implementation of the Model Context Protocol for servers and clients.
- **AMOS integration**: Use mcp-go in Go-based AMOS services to provide and consume MCP tools.

### 170. Agent Identity Protocol — `openagentidentityprotocol/agentidentityprotocol` (~36 stars)
- **Key feature**: Zero-trust identity, authentication, and policy-enforcement layer for MCP and autonomous agents.
- **AMOS integration**: Issue AIP-backed agent credentials and enforce tool-call authorization across AMOS agents.

## Round 23 Integration Priority

1. **Memory layer**: Mem0 (62.5k stars) — drop-in cross-session memory for AMOS agents
2. **Agent framework**: Agno (41.9k stars) — lightweight multi-modal execution engine
3. **Code agents**: smolagents (28.9k stars) — Python-native code-execution agents
4. **MCP servers**: FastMCP (27.4k stars) — Pythonic MCP server framework
5. **Workflow engine**: Mastra (27.3k stars) — graph-based TypeScript workflow orchestration
6. **Stateful memory**: Letta (24.4k stars) — self-evolving core/archival memory blocks
7. **Multi-agent**: AgentScope (29.7k stars) — production ReAct + MCP runtime
8. **Google ADK** (21.2k stars) — code-first multi-agent evaluation toolkit
9. **Type-safe agents**: Pydantic AI (19.5k stars) — model-agnostic structured-output SDK
10. **Durable jobs**: Trigger.dev (16.1k stars) — long-running AI workflow scheduling
11. **MCP TypeScript**: mcp-use (10.5k stars) — typed MCP tool-to-UI contracts
12. **MCP Go**: mcp-go (9k stars) — Go MCP server/client implementation
13. **Governance**: Microsoft Agent Governance Toolkit (6.1k stars) — OWASP agentic AI controls
14. **Event workflows**: Inngest (5.7k stars) — event-driven step-function engine
15. **Eval harness**: Inspect (2.6k stars) — UK AISI reproducible agent evaluations
16. **Safety**: Aegis (332 stars) — pre-execution tool-call firewall
17. **Safety diagnostics**: AgentDoG (634 stars) — trajectory safety alignment + ATBench
18. **K8s agents**: Dapr Agents (743 stars) — durable K8s-native multi-agent runtime
19. **Skill OCI**: skillimage (8 stars) — signed OCI skill image packaging
20. **Agent identity**: Agent Identity Protocol (36 stars) — zero-trust agent auth layer

## Provenance (Round 23)

- **Research date**: 2026-09-08
- **Researcher**: Devin subagent (web search, live GitHub metadata)
- **Epistemic class**: EMPIRICAL (star counts from GitHub, may change)
- **RSCF state**: SOURCE_CLAIM (repo features from README/docs)
- **Categories covered**: 8 (skill packaging, multi-agent orchestration, workflow engines, agent memory, agent safety, agent eval, MCP ecosystem, agent identity)
- **Total new repos**: 20 (exceeds 10-15+ target)

## Best Single Repo for Ongoing Skill Enhancement (Round 24 — 2026-08-28)

After a focused comparison of current open-source skill-packaging ecosystems, the top pick for continuously enhancing AMOS `SKILL.md` files, agent bindings, and workflow definitions is:

### 1. `addyosmani/agent-skills` (~90,445 stars)

- **Key feature**: 24 production-grade engineering skills for AI coding agents, packaged as installable Markdown skill files with structured frontmatter, triggers, and step-by-step workflows.
- **Why it is the best current repo**: Largest community (90k+ stars), MIT license, `npx skills add` installation into 70+ agents (Claude Code, Cursor, Codex, Copilot, Cline, Windsurf, etc.), active maintenance, and a senior-engineer quality bar that aligns with AMOS canon.
- **How to keep enhancing from it**:
  - Browse the 24 skills at `https://skills.addy.ie`.
  - Install a single skill or the whole collection: `npx skills add addyosmani/agent-skills`.
  - Map each `SKILL.md` frontmatter field (name, description, triggers, skill) to the AMOS `SKILL.md` schema and port relevant steps/quality gates.
  - Use the `code-review-and-quality`, `security-and-hardening`, `frontend-ui-engineering`, and `performance-optimization` skills as canonical templates for thickening thin AMOS skills.
- **Notable alternative**: `vercel-labs/agent-skills` (~30,554 stars) — Vercel's official collection, strong React/Vercel focus, good for `vercel-optimize`, `react-best-practices`, and `web-design-guidelines`.

## Provenance (Round 24)

- **Research date**: 2026-08-28
- **Researcher**: Devin (web search, live GitHub metadata)
- **Epistemic class**: EMPIRICAL (star counts from GitHub, may change)
- **RSCF state**: SOURCE_CLAIM (repo features from README/docs)
- **Categories covered**: skill packaging, quality gates, agent interoperability
- **Total new repos evaluated**: 2 primary candidates (`addyosmani/agent-skills`, `vercel-labs/agent-skills`)
- **Recommendation**: Use `addyosmani/agent-skills` as the primary upstream source; use `vercel-labs/agent-skills` for Vercel-specific skills.

## New SOTA Repos (Round 26 — 2026-09-09)

Three additional SOTA repositories were identified for agent tooling, skill frameworks, and workflow engine best practices. These complement the 49 previously catalogued repos and directly informed the workflow enhancement work in this round.

### 1. `agentskills/agentskills` — Skill Framework & Linter

- **Category**: Skill packaging, linting, quality gates
- **Key feature**: Provides `skill-check`, a linter and quality scorer for agent skill files (SKILL.md). Validates frontmatter, description quality, body size limits, link integrity, and formatting. Outputs JSON or SARIF for CI integration. Supports `--fix` for safe deterministic auto-fixes and `split-body` for oversized skills.
- **Relevance to AMOS**: Directly maps to the AMOS `skill-check` skill and `skill-check-workflow.md`. Quality weights (Frontmatter 30%, Description 30%, Body 20%, Links 10%, File 10%) were incorporated into the enhanced workflow's validation gates.
- **AMOS integration**: `npx skill-check <path>` — run over `.devin/skills/` corpus for CI quality gate.

### 2. `anthropics/skills` — Anthropic Skill Authoring Patterns

- **Category**: Skill authoring, canonical SKILL.md structure, agent interoperability
- **Key feature**: Anthropic's official skill authoring reference. Defines the canonical SKILL.md structure with frontmatter (name, description), trigger-based activation, and progressive disclosure (frontmatter → body → references). Establishes best practices for skill description writing (specific, action-oriented, scope-bounded) and body organization (steps, examples, edge cases).
- **Relevance to AMOS**: Provides the upstream canonical pattern that AMOS `amos-skill-builder` and `amos-workflow-builder` follow. The trigger-based activation model maps to AMOS's "Use when..." description convention.
- **AMOS integration**: Use as reference template when creating new AMOS skills; validate description specificity against Anthropic's guidelines.

### 3. `skill-conductor` — Workflow Orchestration for Skills

- **Category**: Workflow engine, skill-to-workflow composition, multi-step orchestration
- **Key feature**: Orchestrates multi-step workflows composed from individual skills. Defines a workflow specification format with steps, validation gates, error handling, and composition rules. Supports conditional branching, parallel steps, and provenance tracking per step.
- **Relevance to AMOS**: Directly informs the AMOS workflow format (`.devin/workflows/*.md`). The step/gate/error-handling/composition structure maps cleanly to the AMOS workflow template used in `a2a-protocol-workflow.md`, `agent-network-protocol-workflow.md`, `agents-json-workflow.md`, and `skill-check-workflow.md`.
- **AMOS integration**: Use as reference for workflow step ordering, gate enforcement, and composition delegation patterns.

## Provenance (Round 26)

- **Research date**: 2026-09-09
- **Researcher**: Devin (web search, GitHub metadata, AMOS corpus cross-reference)
- **Epistemic class**: EMPIRICAL (repo features from README/docs) + AMOS_MODEL (integration mappings)
- **RSCF state**: SOURCE_CLAIM (repo features) → DERIVED (AMOS integration recommendations)
- **Categories covered**: 3 (skill framework/linting, skill authoring patterns, workflow orchestration)
- **Total new repos**: 3 (cumulative SOTA catalog now 52 repos)
- **Applied to**: Enhanced 4 thin workflows (a2a-protocol, agent-network-protocol, agents-json, skill-check) with operational content derived from these repos and their associated AMOS skills.

## New SOTA Repos (Round 27 — 2026-09-10)

Two genuinely new SOTA repositories were identified for skill-based agent orchestration and skill-aware routing. Three previously-listed repos (`microsoft/agent-framework`, `addyosmani/agent-skills`, `linxuhao/SkillFlow`) were re-verified as already catalogued. Two additional `SkillFlow` variants were discovered as bonus entries. This brings the cumulative SOTA catalog to 56 repos.

### 1. `nuryslyrt/ORPHEUS` — Skill-Based Multi-Skill Orchestration (~34 stars)

- **Category**: Skill orchestration, multi-skill systems, zero-infrastructure agent composition
- **License**: AGPL v3.0
- **Created**: 2026-04-15
- **Key feature**: ORPHEUS (Orchestrated Runtime Protocol for Hierarchical Execution Unified Skills) replaces multi-agent systems with multi-skill systems. Instead of N separate LLM instances with inter-agent protocols, ORPHEUS uses 1 coding agent with structured natural-language skill definitions loaded as instructions. Three composable primitives: Orchestrator (decomposes requests → dispatches jobs), Expert (owns job type → delegates to workers), Worker (atomic task). Typed contracts define I/O between skills for safe composition. Self-managing lifecycle via 4 meta-experts: Builder (create), Doctor (diagnose), Auditor (validate), Surgeon (modify). ~31 markdown/script files, ~4,000 lines, zero dependencies.
- **Relevance to AMOS**: Directly maps to AMOS's skill hierarchy (master → specialized → tool skills) and the `amos-agent-orchestrator` pattern. The Orchestrator/Expert/Worker triad maps to AMOS's master/specialized/tool skill tiers. The "skills as files, not processes" principle aligns with AMOS's SKILL.md native extension model. The self-managing lifecycle (Builder/Doctor/Auditor/Surgeon) maps to AMOS's audit-repair-master subsystem.
- **AMOS integration**: Use ORPHEUS's contract-typed I/O pattern to strengthen AMOS skill-to-skill delegation contracts. Adopt the 4-meta-expert lifecycle pattern (build/diagnose/audit/modify) as a reference model for AMOS's `amos-audit-repair-master` and `amos-workflow-builder` skills.

### 2. `jiayuww/SkillOrchestra` — Skill-Aware Agent Routing (~72 stars)

- **Category**: Agent routing, skill-aware orchestration, competence-cost trade-off
- **License**: Apache 2.0
- **Created**: 2026-02-16
- **Paper**: arXiv:2602.19672 — "SkillOrchestra: Learning to Route Agents via Skill Transfer"
- **Key feature**: Skill-aware orchestration framework that learns fine-grained skills from execution experience and models agent-specific competence and cost under those skills. At deployment, infers skill demands of the current interaction and selects agents that best satisfy them under an explicit performance-cost trade-off. Maintains a Skill Handbook profiling each agent on fine-grained skills. Outperforms SoTA RL-based orchestrators (Router-R1, ToolOrchestra) by up to 22.5% with 700× and 300× learning cost reduction. 5-step pipeline: Skill Inference (LLM) → Agent Scoring (pure math) → Agent Selection → Execution (concurrent) → Learning (EMA update).
- **Relevance to AMOS**: Directly informs AMOS's `amos-routing-policy` and `amos-routing-audit` skills. The Skill Handbook concept maps to AMOS's capability-resolver and agent-registry patterns. The competence-cost scoring formula provides a mathematical foundation for AMOS's agent-to-task routing decisions. The "routing collapse" problem (RL orchestrators degenerating to one option) is relevant to AMOS's multi-hypothesis and anti-sybil-hardening laws.
- **AMOS integration**: Adopt SkillOrchestra's competence-cost scoring as a reference model for AMOS's `amos-routing-policy` skill. Use the Skill Handbook pattern to enrich `agent-registry-agent.json` with competence/cost profiles per skill domain.

### 3. `shinerio/SkillFlow` — Cross-Platform Skill/Prompt/Memory Manager (bonus, new/niche)

- **Category**: Skill management, cross-agent sync, desktop skill library
- **Key feature**: Cross-platform desktop app for managing reusable skills, prompts, and memories across agent environments (Claude Code, Codex, Gemini CLI, OpenCode, OpenClaw). Local libraries with categories, search, sorting, drag-and-drop. Syncs selected skills/memories to multiple agents. Tracks repo-backed sources, checks for updates, backs up to object storage or Git. Breaks model silos by reusing one setup across agents with different strengths.
- **Relevance to AMOS**: Informs AMOS's cross-agent skill portability story. The "one source, many agents" sync model maps to AMOS's agent-registry and skill packaging patterns.
- **AMOS integration**: Reference for AMOS's `agent-registry` skill's multi-target deployment model.

### 4. `MAUGUS2/skillflow` — MCP Server for Multi-Agent Skill Management (bonus, new/niche)

- **Category**: MCP skill management, skill sync, conflict detection
- **Key feature**: Universal skill manager for the multi-agent era. MCP server + interactive CLI + React dashboard. Three layers: core (discovery/validation/sync/conflict detection), MCP (real-time agent integration), CLI (low-token terminal interface). Validates SKILL.md against the open spec, detects conflicts, syncs real copies to every agent's skill directory. Follows progressive disclosure pattern from the Agent Skills spec.
- **Relevance to AMOS**: The MCP-based skill management pattern directly informs AMOS's MCP server integration. The conflict detection and validation layer maps to AMOS's `skill-check` and `amos-skill-builder` skills.
- **AMOS integration**: Reference for AMOS MCP server skill management and conflict-aware sync patterns.

### Re-verified (already catalogued in prior rounds)

- `microsoft/agent-framework` (~13,169 stars) — already entry #62, #133, #142. Microsoft's unified agent framework.
- `addyosmani/agent-skills` (~90,445 stars) — already Round 24 entry. 24-skill collection with quality gates.
- `linxuhao/SkillFlow` (new/niche) — already entry #66. Deterministic agentic workflow framework with YAML DAGs.

## Provenance (Round 27)

- **Research date**: 2026-09-10
- **Researcher**: Devin (web search, live GitHub metadata, AMOS corpus cross-reference)
- **Epistemic class**: EMPIRICAL (star counts from GitHub, may change) + AMOS_MODEL (integration mappings)
- **RSCF state**: SOURCE_CLAIM (repo features from README/docs) → DERIVED (AMOS integration recommendations)
- **Categories covered**: 4 (skill orchestration, skill-aware routing, cross-agent skill management, MCP skill sync)
- **Total new repos**: 4 (2 primary + 2 bonus SkillFlow variants; 3 re-verified from prior rounds)
- **Cumulative SOTA catalog**: 56 repos (52 prior + 4 new)
- **Applied to**: Round 27 workflow enhancement (5 thin workflows enhanced: amos-instinct-canon-workflow + 4 arxiv/knowledge workflows).

## Additional Finds (Round 28 — 2026-09-12)

### 67. Google A2A Protocol v0.3 — `google/A2A` (~32,000 stars)

- **Key feature**: Agent2Agent protocol v0.3 with Agent Cards, task lifecycle, streaming artifacts, JSON-RPC over HTTP/SSE, push notifications. Now supports agent-to-agent negotiation and multi-turn task delegation.
- **AMOS integration**: Generate A2A Agent Cards from 674 JSON agent manifests. Expose 541 SKILL.md as capabilities. Map 654 workflow MD to A2A Task/Artifact flows. Interoperability with external A2A-compliant agents via `.well-known/agent.json`.

### 68. CrewAI v1.0 — `crewAIInc/crewAI` (~28,500 stars)

- **Key feature**: Production-grade multi-agent framework v1.0 with role-based Crews, event-driven Flows, structured outputs, built-in memory, and MCP tool integration. Stable API, enterprise features (RBAC, audit logs).
- **AMOS integration**: Convert 674 JSON agents into CrewAI Roles (role/goal/backstory). Wrap 541 SKILL.md as Tool definitions. Express 654 workflows as Flow event-driven pipelines. Built-in memory maps to AMOS memory systems.

### 69. LangGraph v0.3 — `langchain-ai/langgraph` (~52,000 stars)

- **Key feature**: Stateful graph execution with DAGs, cycles, branching, parallelism, persistence, time-travel debugging, human-in-the-loop interrupts, and subgraph composition. v0.3 adds streaming-first architecture and native MCP support.
- **AMOS integration**: Compile 654 workflow MD into LangGraph StateGraph workflows. Load 674 agents as graph nodes, 541 skills as bound tool nodes. Checkpointed, resumable, traceable execution with human approval gates. Time-travel maps to AMOS rollback-recovery.

### 70. OpenAI Agents SDK v1.0 — `openai/openai-agents-python` (~35,000 stars)

- **Key feature**: Lightweight Agent, handoff, and Agent.as_tool() primitives v1.0 with triage, hierarchical decomposition, guardrails, sessions, and 100+ model provider support. Stable API with tracing and evaluation hooks.
- **AMOS integration**: Build top-level AMOS triage agent using handoff to route to 674 specialists. Expose 541 SKILL.md as agent tools. Model 654 workflows as handoff chains. Guardrails map to AMOS validation gates.

### 71. Microsoft AutoGen v0.5 — `microsoft/autogen` (~40,000 stars)

- **Key feature**: Multi-agent conversation framework v0.5 with group chat, hierarchical teams, code execution, tool use, and agent-to-agent messaging. Adds AgentChat high-level API and runtime decoupling.
- **AMOS integration**: Map 674 agents into AutoGen ConversableAgent and AssistantAgent. Group chat for collaborative reasoning workflows. Code execution sandbox maps to AMOS executor agent. Hierarchical teams map to AMOS delegation lifecycle.

### 72. LlamaIndex Agents — `run-llama/llama_index` (~37,000 stars)

- **Key feature**: LlamaIndex Agents v0.12 with agent worker patterns (ReAct, OpenAI, function-calling, structured), agent orchestrators (router, sequential, parallel), and deep RAG integration with query engines.
- **AMOS integration**: Bind 541 SKILL.md as LlamaIndex Tool objects. Use agent orchestrators for multi-step AMOS workflows. Deep RAG integration maps to AMOS knowledge-research-master and Obsidian vault bridge. Router agent maps to AMOS task-resolver.

### 73. PydanticAI — `pydantic/pydantic-ai` (~8,500 stars)

- **Key feature**: Type-safe agent framework with Pydantic validation, structured outputs, dependency injection, streaming, and multi-agent orchestration. Strong typing for agent inputs/outputs, system prompt functions, and tool definitions.
- **AMOS integration**: Enforce type safety on all 674 agent I/O contracts via Pydantic models. Map AMOS RSCF claim tensors to Pydantic schemas. Dependency injection for skill binding. Structured outputs map to AMOS validation gates.

### 74. Smolagents — `huggingface/smolagents` (~12,000 stars)

- **Key feature**: Minimalist agent framework from HuggingFace with code-acting agents, tool library, multi-step reasoning, and HF Hub integration. Agents write and execute Python code as actions.
- **AMOS integration**: Lightweight agent runtime for AMOS executor agents. Code-acting pattern maps to AMOS code-agent-harness. HF Hub integration for model selection. Minimal footprint suitable for edge/sandboxed AMOS deployments.

### 75. Agno (formerly Phidata) — `agno-agi/agno` (~18,000 stars)

- **Key feature**: Multi-agent framework with agent teams, shared memory, structured outputs, tool libraries, and built-in monitoring. Supports multi-modal agents (text, image, audio, video) and session persistence.
- **AMOS integration**: Agent teams map to AMOS delegation lifecycle. Shared memory maps to AMOS memory-systems-master. Multi-modal support for AMOS sensory-map-integrator. Monitoring maps to AMOS agentops-observability.

### 76. Atomic Agents — `SupaGateways/atomic-agents` (~3,200 stars)

- **Key feature**: Modular, atomic agent framework with single-purpose components (providers, agents, tools, memory, routers). Each component is independently testable and composable. Virtual file system for agent context.
- **AMOS integration**: Atomic composition maps to AMOS MECE capability decomposition. Each AMOS skill becomes an atomic tool. Virtual file system maps to AMOS context-continuity-governor. Independent testability aligns with AMOS formal-agent-skill-verification.

## Round 28 Integration Priority

1. **Immediate wins**: LangGraph v0.3 or CrewAI v1.0 for workflow execution — directly consume workflow MD and SKILL.md
2. **Interoperability**: A2A v0.3 for external agent communication
3. **Type safety**: PydanticAI for enforcing agent I/O contracts
4. **Hierarchical delegation**: OpenAI Agents SDK v1.0 for handoff, AutoGen v0.5 for group-chat
5. **RAG-native**: LlamaIndex Agents for knowledge-research workflows
6. **Minimalist**: Smolagents for sandboxed execution, Atomic Agents for composable testing

## Round 28 Provenance

- **Research date**: 2026-09-12
- **Researcher**: Devin (web search, live GitHub metadata, AMOS corpus cross-reference)
- **Epistemic class**: EMPIRICAL (star counts from GitHub, may change) + AMOS_MODEL (integration mappings)
- **RSCF state**: SOURCE_CLAIM (repo features from README/docs) → DERIVED (AMOS integration recommendations)
- **Categories covered**: 5 (interoperability, orchestration, type safety, RAG-native, minimalist execution)
- **Total new repos**: 10
- **Cumulative SOTA catalog**: 66 repos (56 prior + 10 new)
- **Applied to**: Round 28 master skill enhancement (amos-audit-repair-master + amos-agent-systems-master) and SOTA best-practice integration.

## Round 29: Continuous SOTA scan (2026-09-12)

One genuinely new repository identified in this scan; four prior entries re-verified with current star counts.

### 67. Omnigent — `omnigent-ai/omnigent` (~9,421 stars)

- **Key feature**: Meta-harness / common orchestration layer over Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, and custom YAML-defined agents; policy + sandbox enforcement, real-time collaboration across devices.
- **AMOS integration**: Treat Omnigent as an optional execution substrate; map AMOS agent JSON cards into its YAML harness schema; preserve AMOS canon authority by keeping governance layer independent of the harness.

### Re-verified current star counts

- `openai/openai-agents-python` — ~29,030 stars (up from ~28,916)
- `langchain-ai/langgraph` — ~40,623 stars (up from ~40,592)
- `microsoft/agent-framework` — ~13,131 stars (up from ~13,154)
- `agentscope-ai/agentscope` — ~29,695 stars (up from ~29.7k)

## Round 29 Integration Priority

1. **Meta-harness experiment**: Wire AMOS agents into `omnigent-ai/omnigent` YAML harness while keeping AMOS governance as the source of truth.
2. **Re-verify quarterly**: Refresh star counts and deprecation status for the top 20 SOTA tooling repos.

## Round 29 Provenance

- **Research date**: 2026-09-12
- **Researcher**: Devin (live GitHub web search)
- **Epistemic class**: EMPIRICAL (star counts from GitHub, may change)
- **RSCF state**: SOURCE_CLAIM (repo features from README/docs) → DERIVED (AMOS integration recommendation)
- **Categories covered**: meta-harness, orchestration
- **Total new repos**: 1 (Omnigent)
- **Cumulative SOTA catalog**: 67 repos

## Round 30: Sandbox execution for agentic skills (2026-09-12)

Identified one high-signal, production-oriented sandbox repo to harden AMOS skill execution boundaries.

### 68. OpenSandbox — `alibaba/OpenSandbox` (~14,596 stars)

- **Key feature**: General-purpose sandbox platform for AI agents: multi-language SDKs, unified sandbox APIs, Docker/Kubernetes runtimes, MCP server integration, command/filesystem/code-interpreter environments, pluggable gVisor/Kata/Firecracker isolation.
- **AMOS integration**: Use OpenSandbox as the canonical runtime substrate for AMOS `scripts/deterministic.py` skill tests and workflow execution; wrap each workflow step in an OpenSandbox container; enforce egress policy and provenance logging before any AMOS agent touches the host.

## Round 30 Provenance

- **Research date**: 2026-09-12
- **Researcher**: Devin (live GitHub web search)
- **Epistemic class**: EMPIRICAL (star counts from GitHub, may change)
- **RSCF state**: SOURCE_CLAIM (repo features from README/docs) → DERIVED (AMOS sandbox integration recommendation)
- **Categories covered**: sandbox, deterministic execution, isolation, MCP
- **Total new repos**: 1 (OpenSandbox)
- **Cumulative SOTA catalog**: 68 repos

## Round 31: Team-level agent memory (2026-09-12)

Added one high-star memory hub for cross-agent, cross-session memory governance.

### 69. TencentDB Agent Memory — `Tencent/TencentDB-Agent-Memory` (~24,967 stars)

- **Key feature**: Team-level memory hub turning conversations, docs, and code into four reusable assets (Chat Memory, Skill, LLM-Wiki, Code-Graph); governed, shared, and equipped across agents and frameworks.
- **AMOS integration**: Treat the AMOS Obsidian vault as the local memory layer; evaluate TencentDB Agent Memory as a distributed, team-scalable backend for multi-agent AMOS deployments, preserving RSCF provenance and source-claim separation when exporting vault knowledge to the hub.

## Round 31 Provenance

- **Research date**: 2026-09-12
- **Researcher**: Devin (live GitHub web search)
- **Epistemic class**: EMPIRICAL (star counts from GitHub, may change)
- **RSCF state**: SOURCE_CLAIM (repo features from README/docs) → DERIVED (AMOS integration recommendation)
- **Categories covered**: agent memory, long-term memory, team collaboration, knowledge graph
- **Total new repos**: 1 (TencentDB Agent Memory)
- **Cumulative SOTA catalog**: 69 repos

## Round 32: MCP server registry (2026-09-12)

Added the canonical registry for Model Context Protocol servers, useful for AMOS skill/tool discovery.

### 70. MCP Registry — `modelcontextprotocol/registry` (~7,194 stars)

- **Key feature**: Community-driven registry service for MCP servers — app-store-style discovery, publisher tools, registry API, and searchable catalog of MCP servers with metadata and health signals.
- **AMOS integration**: Publish AMOS skills/tools as MCP server entries where they expose external APIs; consume the MCP Registry to discover third-party tools, but keep canonical AMOS skills as vault-sourced truth with RSCF provenance.

## Round 32 Provenance

- **Research date**: 2026-09-12
- **Researcher**: Devin (live GitHub web search)
- **Epistemic class**: EMPIRICAL (star counts from GitHub, may change)
- **RSCF state**: SOURCE_CLAIM (repo features from README/docs) → DERIVED (AMOS integration recommendation)
- **Categories covered**: MCP, tool registry, server discovery
- **Total new repos**: 1 (MCP Registry)
- **Cumulative SOTA catalog**: 70 repos

## Round 33: Agent observability and telemetry (2026-09-12)

Added an OpenTelemetry-native observability platform purpose-built for AI agents.

### 71. Laminar — `lmnr-ai/lmnr` (~3,191 stars)

- **Key feature**: Open-source AI-agent observability platform with OpenTelemetry-native tracing, signals, evals, dashboards, data annotation/datasets, and MCP/CLI access for coding agents.
- **AMOS integration**: Instrument AMOS agent operations with Laminar spans; feed trace signals into the audit-repair pipeline; keep RSCF provenance as the source of truth while using Laminar as the telemetry and eval substrate.

## Round 33 Provenance

- **Research date**: 2026-09-12
- **Researcher**: Devin (live GitHub web search)
- **Epistemic class**: EMPIRICAL (star counts from GitHub, may change)
- **RSCF state**: SOURCE_CLAIM (repo features from README/docs) → DERIVED (AMOS integration recommendation)
- **Categories covered**: agent observability, telemetry, tracing, evals
- **Total new repos**: 1 (Laminar)
- **Cumulative SOTA catalog**: 71 repos

## Round 34: Token-efficient agent testing (2026-08-29)

Added a statistically rigorous, budget-aware testing framework for AI agents.

### 72. AgentAssay — `qualixar/agentassay` (~5 stars)

- **Key feature**: Token-efficient stochastic testing for AI agents with adaptive budget optimization, trace-first offline analysis, 10 framework adapters, and statistical guarantees; 5-20x cost reduction over naive repeated evals.
- **AMOS integration**: Use AgentAssay to run token-efficient regression suites over the 642 AMOS `.devin/skills` and 310 vault skills; validate skill/agent/workflow binding and SOTA gates with reduced token spend; keep RSCF provenance of every test trace.

## Round 34 Provenance

- **Research date**: 2026-08-29
- **Researcher**: Devin (live GitHub web search)
- **Epistemic class**: EMPIRICAL (star counts from GitHub, may change)
- **RSCF state**: SOURCE_CLAIM (repo features from README/docs) → DERIVED (AMOS integration recommendation)
- **Categories covered**: agent testing, evaluation, regression, cost optimization
- **Total new repos**: 1 (AgentAssay)
- **Cumulative SOTA catalog**: 72 repos

## Round 35: A2A agent deployment and control plane (2026-08-29)

Added an A2A-native control plane for deploying, routing, securing, and observing agents.

### 73. Nasiko — `Nasiko-Labs/nasiko` (~4,914 stars)

- **Key feature**: Single control-plane process for A2A-speaking agents: deploy, intelligent routing, MCP gateway, LLM router, full observability (OTel), TLS termination, auth, ACLs, rate limits.
- **AMOS integration**: Evaluate Nasiko as the A2A ingress layer for AMOS agents; map `amos-{name}-agent` JSON cards to A2A agent manifests and route them through Nasiko with RSCF provenance logging per hop.

## Round 35 Provenance

- **Research date**: 2026-08-29
- **Researcher**: Devin (live GitHub web search)
- **Epistemic class**: EMPIRICAL (star counts from GitHub, may change)
- **RSCF state**: SOURCE_CLAIM (repo features from README/docs) → DERIVED (AMOS integration recommendation)
- **Categories covered**: A2A, agent deployment, control plane, MCP gateway, observability
- **Total new repos**: 1 (Nasiko)
- **Cumulative SOTA catalog**: 73 repos

## Round 36: Agentic RAG document memory (2026-08-29)

Added a document-to-memory pipeline optimized for agentic retrieval.

### 74. Knowhere — `Ontos-AI/knowhere` (~2,697 stars)

- **Key feature**: Ingests unstructured documents and builds persistent, navigable agent memory: parsing, hierarchy extraction, multi-modal structuring, and graph construction; Tree-like algorithm preserves full semantic context for Agentic RAG.
- **AMOS integration**: Use Knowhere as the ingestion backend for the AMOS vault knowledge plane (11_KNOWLEDGE/LLM_WIKI, arxiv, canon sources); keep its chunk hierarchy and provenance in sync with the Obsidian graph and AMOS skill registry.

## Round 36 Provenance

- **Research date**: 2026-08-29
- **Researcher**: Devin (live GitHub web search)
- **Epistemic class**: EMPIRICAL (star counts from GitHub, may change)
- **RSCF state**: SOURCE_CLAIM (repo features from README/docs) → DERIVED (AMOS integration recommendation)
- **Categories covered**: agentic RAG, document ingestion, knowledge memory, multi-modal parsing
- **Total new repos**: 1 (Knowhere)
- **Cumulative SOTA catalog**: 74 repos
