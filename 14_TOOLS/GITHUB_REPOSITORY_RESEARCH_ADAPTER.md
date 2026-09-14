---
title: GitHub Repository Research Adapter
type: tool
source: 14_TOOLS
origin_architect: Trang Phan
steward: Trang Phan
status: CONDITIONAL
epistemic_class: AMOS_MODEL
---

# GitHub Repository Research Adapter

## Purpose

Expose bounded GitHub repository discovery and source reading to AMOS research/engineering workflows without conflating repository access with repository mutation authority.

## Tool identity

```yaml
tool_id: amos-github-research
provider_type: EXTERNAL_SYSTEM
execution_tier: T3_EXTERNAL_NETWORK
capability_mask:
  - GITHUB_REPO_DISCOVERY
  - GITHUB_SOURCE_READ
  - GITHUB_COMMIT_READ
  - GITHUB_PR_READ
  - GITHUB_WORKFLOW_STATUS_READ
maximum_effect_class: E0_READ_ONLY
```

Read-only use is the default capability represented by this adapter. Write actions such as branch creation, file mutation, pull-request creation, issue comments, merges, releases, or workflow dispatch are separate effectful capabilities and must not inherit authority from this read adapter.

## Inputs

- repository search query or exact repository identity;
- optional owner/org scope;
- optional immutable branch/tag/commit ref;
- target research question or AMOS gap;
- freshness requirement.

## Outputs

Outputs are `OBSERVATION` or `SOURCE_CLAIM` until transformed by an AMOS reasoning layer. Preserve:

- repository owner/name;
- path;
- branch/tag/commit when available;
- retrieval timestamp/epoch;
- source URL/API identity;
- uncertainty when content is partial or truncated.

## Invariants

- `READ_ACCESS != WRITE_AUTHORITY`
- `REPOSITORY_EXISTS != SOURCE_TRUSTED`
- `README != IMPLEMENTATION`
- `STAR_COUNT != TECHNICAL_VALIDITY`
- `DEFAULT_BRANCH != IMMUTABLE_PROVENANCE`
- `SEARCH_RESULT != COMPLETE_CORPUS`

## Failure behavior

- unresolved repository/ref -> `UNKNOWN/GAP`;
- private/inaccessible source -> do not substitute public mirrors as equivalent evidence;
- truncated content -> fetch targeted files/ranges before making exact claims;
- unstable claim -> bind to commit and revalidate freshness;
- write required -> escalate to a separately authorized GitHub mutation capability.

## Consumers

- `amos-github-rscf-ingestion`
- `amos-research-agent`
- repository engineering/audit skills
- GitHub-native AMOS agents under `.github/agents/`

## Provenance boundary

This adapter describes AMOS governance around a GitHub connector/API capability. It does not claim GitHub guarantees correctness, provenance independence, security, or completeness of hosted repository content.
