---
name: amos-github-rscf-ingestion
description: Research, compare, ingest, and govern knowledge from GitHub repositories into AMOS. Use for repository discovery, SOTA scans, architecture comparison, source-grounded code reading, external agent/skill/tool/workflow evaluation, provenance-preserving ingestion, drift detection, and deciding whether an external mechanism should be rejected, quarantined, adapted, tested, or promoted.
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
created: 2026-08-22
---

# AMOS GitHub RSCF Ingestion

Origin architect/steward: **Trang Phan**. Parent: `amos-c10-tech-engineering-master`. This skill turns GitHub repositories into provenance-bound AMOS knowledge and candidate capabilities; it does not treat popularity, documentation, or source availability as proof of correctness or authority.

## Core invariants

- `REPOSITORY_DISCOVERED != REPOSITORY_TRUSTED`
- `README_CLAIM != VERIFIED_BEHAVIOR`
- `POPULAR != BEST_FIT`
- `CAPABILITY != AUTHORITY`
- `COPIED != INTEGRATED`
- `TEST_PASS != GLOBAL_CORRECTNESS`
- `LATEST != AUTHORITATIVE`
- `UNKNOWN/GAP != PASS`

## Retrieval strategy

Use progressive disclosure:

1. **Identity** — repository, owner, default branch, license, current commit/tag, activity/freshness.
2. **Structure** — README, manifests, architecture docs, entrypoints, major directories, tests, workflows, security policy.
3. **Mechanism** — inspect only source files needed to understand the candidate pattern.
4. **Evidence** — tests, benchmarks, CI, issues, releases, security advisories, reproducibility artifacts.
5. **Integration** — map the mechanism to an existing AMOS owner before proposing new structure.

Do not bulk-copy repositories into AMOS knowledge. Extract bounded knowledge cells:

`Claim + Mechanism + Scope + Assumptions + Dependencies + FailureModes + Provenance + Falsifiers`

## Repository ranking

Rank candidates by AMOS decision value, not stars alone. Consider:

- source authority and maintainer credibility;
- current activity and release discipline;
- architecture relevance to the identified AMOS gap;
- executable evidence and test quality;
- security posture and dependency hygiene;
- interoperability and portability;
- implementation complexity and coupling cost;
- license compatibility;
- observability/replay support;
- expected reduction in AMOS search, state, execution, or verification cost.

Star count may be retained as a discovery signal only.

## External agent/skill/tool/workflow admission

For third-party agentic content use this lifecycle:

`DISCOVERED -> QUARANTINED -> STRUCTURALLY_VALID -> SECURITY_REVIEWED -> TESTED -> GOVERNANCE_APPROVED -> ACTIVE`

At minimum:

1. bind source repository + immutable commit/ref;
2. inspect license and dependencies;
3. separate instructions from executable code, hooks, tools, MCP config, assets, and network effects;
4. scan for prompt injection, data exfiltration, hidden execution, excessive agency, credential access, unsafe downloads, tool poisoning, and ambiguous authority;
5. compare against existing AMOS capability to prevent duplication;
6. adapt the smallest useful mechanism instead of vendoring the whole framework when possible;
7. test deterministic behavior, negative cases, regression, replay, and recovery as applicable;
8. preserve source lineage and unresolved gaps.

Automated scanners such as Cisco AI Defense Skill Scanner or SkillSpector are evidence providers, not security authorities. A clean scan does not establish safety.

## GitHub-native AMOS surfaces

When working in `AMOS-OS`, use repository-native specialization where available:

- `.github/agents/amos-architect.agent.md` — architecture/ownership decisions;
- `.github/agents/amos-skill-security-auditor.agent.md` — external admission/security review;
- `.github/agents/amos-integration-engineer.agent.md` — approved implementation;
- `.github/instructions/skills.instructions.md` — Agent Skills packaging/progressive disclosure;
- `.github/instructions/tools.instructions.md` — tool capability/authority separation;
- `.github/instructions/workflows.instructions.md` — workflow state/replay/recovery contract.

These roles do not grant themselves commit or deployment authority.

## Capability set

### `github_ingestion.discover`
Find candidate repositories for a declared AMOS gap and return a ranked shortlist with source identity and freshness.

### `github_ingestion.map_repository`
Build a deterministic structural map: modules, interfaces, dependencies, entrypoints, tests, configuration, workflows, and security surfaces.

### `github_ingestion.extract_mechanism`
Extract reusable mechanisms and constraints without copying unnecessary source code.

### `github_ingestion.compare`
Compare candidate mechanisms against current AMOS architecture and competing repositories.

### `github_ingestion.audit_agentic_content`
Audit external skills, agents, hooks, MCP/tool declarations, and workflows before admission.

### `github_ingestion.propose_integration`
Map the candidate mechanism to the canonical AMOS owner and produce the minimum non-duplicative integration proposal.

### `github_ingestion.detect_drift`
Revalidate previously ingested knowledge when upstream commits, dependencies, licenses, APIs, benchmarks, or security conditions change.

## Output contract

For each promoted finding return:

- **claim / mechanism**;
- **source repository + immutable ref**;
- **epistemic class**;
- **AMOS owner/gap addressed**;
- **assumptions and dependencies**;
- **security/authority implications**;
- **competing alternatives**;
- **falsifier or invalidation condition**;
- **recommended state**: REJECT, WATCH, QUARANTINE, ADAPT, TEST, or PROMOTE;
- **confidence ceiling** bounded by the weakest load-bearing evidence.

## Failure behavior

- Missing source identity -> `UNKNOWN/GAP`, no ingestion.
- Unclear license -> quarantine implementation reuse.
- Repository docs disagree with executable behavior -> executable evidence wins for implementation claims; preserve the contradiction.
- Security finding HIGH/CRITICAL unresolved -> fail closed.
- Existing AMOS owner already covers the mechanism -> improve that owner rather than create a duplicate.
- Benchmark cannot be reproduced or scope differs -> keep performance claim as SOURCE_CLAIM.
- Upstream drift invalidates assumptions -> selectively invalidate dependent AMOS knowledge, not unrelated state.

## References

Load only when needed:

- `references/vault_domain_knowledge.md` — legacy vault-derived background.
- `references/references_MOC.md` — reference map.
- `11_KNOWLEDGE/SOTA_AGENT_TOOLING_REPOS.md` — prior GitHub SOTA inventory; refresh before relying on unstable facts.
- `11_KNOWLEDGE/LLM_WIKI/wiki/SOTA_AGENT_SKILL_WORKFLOW_REPOS.md` — synthesized agent/skill/workflow research.

## Composition

- Parent: `amos-c10-tech-engineering-master`
- Agent: `amos-github-rscf-ingestion-agent`
- Workflow: `amos-github-rscf-ingestion-workflow.md`
- Security peers: `amos-provenance-trust-firewall`, `amos-repair-substrate-capture-resistance-rscf`, `amos-information-exposure-control`
- Engineering peers: `software-engineering-qa`, `amos-repository-knowledge-acquisition-rscf`, `amos-repository-ast-analysis-rscf`

## Success criteria

A successful run produces a smaller, better-grounded integration decision—not merely a larger repository list. No external mechanism is promoted without provenance, scope, security/authority analysis, and evidence appropriate to the claimed implementation state.
