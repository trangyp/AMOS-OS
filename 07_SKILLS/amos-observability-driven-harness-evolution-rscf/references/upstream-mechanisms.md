# Upstream mechanisms and provenance

All external repository mechanisms below are `SOURCE_CLAIM` inputs. They do not grant AMOS authority and their benchmark claims are not independently verified here.

## Agentic Harness Engineering

Source inspected: `china-qijizhifeng/agentic-harness-engineering@8b2a55d97590363fe50c3cc6b5e833b020a4bb4c`.

Adapted mechanisms:

- explicit harness component classes;
- change manifests with failure evidence, root cause, targeted fix, expected fixes, and at-risk regressions;
- comparison of predicted changes against later evaluation outcomes;
- file-level/revertible harness evolution.

The source component vocabulary maps to AMOS as:

- system rules/system prompt -> `SYSTEM_PROMPT`;
- tool descriptions -> `TOOL_DESCRIPTION`;
- tool implementations -> `TOOL_IMPLEMENTATION`;
- middleware -> `MIDDLEWARE`;
- skills -> `SKILL`;
- sub-agents -> `SUB_AGENT_CONFIG`;
- long-term memory -> `LONG_TERM_MEMORY`.

Commit `faf44bc4aea57413c520bc5711c6ebf628e0da1e` is useful evidence that component detection itself can drift: it repaired missing detection of `LongTermMEMORY.md`. AMOS therefore requires explicit registered paths rather than relying only on filename heuristics.

Do not promote reported AHE benchmark gains into AMOS evidence unless rerun under an exact comparable harness/environment.

## NexAU

Source inspected: `nex-agi/NexAU@4d3767e41f43b617f484c75ae1b51704dee26ff0`.

Adapted mechanisms:

- typed, separately declared contributions for system-prompt fragments, tools, skills, sub-agents, and middleware;
- fail-fast behavior for undeclared configuration variables;
- strict manifest/config handling rather than silently accepting unknown fields.

AMOS uses these as support for explicit surface declaration and fail-closed unknown-component behavior.

## Harbor

Source inspected: `harbor-framework/harbor@4008e2df847e445b0b3c41cff852b5460a62bfb7`.

The commit repairs multi-step evaluation leakage where a shared verifier could leave `/tests` and `/logs/verifier` visible to the next agent phase. The repair tracks whether shared verifier state actually exists, sanitizes it before the next agent phase, and avoids deleting agent-owned state when no shared verifier ran.

AMOS adapts the stronger invariant:

`VERIFIER_OR_REWARD_LEAKAGE_INVALIDATES_COMPARATIVE_EVIDENCE`.

Isolation evidence must therefore distinguish shared/separate/single-step modes and prove prior test/reward artifacts are hidden without destroying legitimate agent-owned state.

## Internal AMOS dependencies

- Interactive evaluation runtime lineage: `trangyp/AMOS-OS@b86cfae1dc5628a9249ef6fd587c836eac127443` (PR #19).
- Evaluator calibration runtime lineage: `trangyp/AMOS-OS@aa46e695f6dc6f1cd4860e36758ff8074aa5a0d4` (PR #22).

PR #19 supplies bounded run/comparison receipts. PR #22 supplies held-out evaluator reliability evidence. Neither grants mutation, write, merge, deployment, or canonical authority.

## AMOS extension classes

The following are AMOS integration extensions, not upstream AHE/NexAU source classes:

`AGENT_CONFIG | WORKFLOW | POLICY_CONFIG | TOOL_REGISTRY`.

They exist because AMOS stores consequential harness behavior in those repository control surfaces. Their inclusion is an `AMOS_MODEL` design choice.
