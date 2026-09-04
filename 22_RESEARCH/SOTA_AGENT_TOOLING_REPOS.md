---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Sota Agent Tooling Repos
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

# SOTA Agent Tooling Repos

## 0. Status

`SOTA_AGENT_TOOLING_REPOS.md` defines the proposed AMOS OS **SOTA Agent Tooling**.

This artifact replaces a structural placeholder with substantive content.

```text
PLACEHOLDER != IMPLEMENTED
ADDRESSABLE != VALIDATED
DOCUMENTED != ENFORCED
MODEL != OBSERVATION
SOURCE_CLAIM != VERIFIED
CANON_CANDIDATE != CANONICAL
CAPABILITY != AUTHORITY
UNKNOWN/GAP != PASS
```

Origin architect / steward: **Trang Phan**

______________________________________________________________________

## 1. Purpose

The SOTA Agent Tooling Repos document catalogs state-of-the-art agent tooling repositories relevant to AMOS.

______________________________________________________________________

## 2. Formal Definition

### 2.1 Cataloged Repos

| Repo | Description | AMOS Integration |
|:---|:---|:---|
| agentoperations/agent-registry | Agent registry manifests | Agent Registry skill |
| wuyifeishu/nexus-agentos | Universal agent runtime | Nexus AgentOS skill |
| microsoft/conductor | Multi-agent workflow CLI | Microsoft Conductor skill |
| adegany/amos | Agent Memory OS | Agent Memory OS skill |
| rebootuser/LinEnum | Linux privilege enumeration | LinEnum skill |
| peass-ng/PEASS-ng | Privilege escalation suite | PEASS-ng skill |
| FareedKhan-dev/kimi-k3-in-c | C99 Kimi K3 inference | Kimi K3 skill |

### 2.2 SOTA Research Areas

- Multi-agent orchestration patterns
- Agent memory architectures
- Agent-to-agent protocols (A2A, ANP)
- Skill marketplace designs
- Agent observability and tracing

### 2.3 Integration Status

All cataloged repos have corresponding AMOS skills in `.devin/skills/`. Integration is AMOS_MODEL — architectural mapping, not runtime deployment.

______________________________________________________________________

## 3. Cross-References

- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- [[00_ROOT/AMOS MOC|AMOS MOC]]
- [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

______________________________________________________________________

## 4. Gaps

- Executable binding NOT_ESTABLISHED
- Canonical status CONDITIONAL
- Automated enforcement NOT_ESTABLISHED

______________________________________________________________________

## 5. Ingestion Rule

```yaml
AMOS_CANON_INGESTION_RULE:
  existing_file:
    preserve: true
    overwrite: false
  uncertainty:
    action:
      - MARK_GAP_OR_COMPETING
      - NEVER_INVENT_CANON
```

______________________________________________________________________

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] · [[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

______________________________________________________________________

RSCF-NODE

node_id: amos_22_research_sota_agent_tooling_repos

node_type: RESEARCH

path: 22_RESEARCH/SOTA_AGENT_TOOLING_REPOS.md

claim_class: AMOS_MODEL

rscf_state: DERIVED

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
