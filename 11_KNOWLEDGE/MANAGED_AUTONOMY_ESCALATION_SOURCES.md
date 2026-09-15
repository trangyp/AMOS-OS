# Managed Autonomy Escalation Sources

All upstream entries are `SOURCE_CLAIM` mechanisms. AMOS inherits no external authority or deployment claim.

- `openai/openai-agents-python@fbf59a40e9da5adb88d370fefaeaae0478376d4a`: run lifecycle exposes max-turn bounds, interruptions, guardrails, handoffs, and resume semantics; interrupted state preserves run budget rather than silently resetting it.
- `microsoft/agent-framework@91b3c8b02248e675079419635eceabc7d067bf7c`: checkpoint save/load symmetry, restoration validation, and long-running workflow recovery mechanics.
- `langchain-ai/langgraph@230927fb3a9ac9b2893a30322b4dfea7cdea9a8f`: explicit checkpoint-backed interrupt/resume boundaries and state history.

AMOS adaptation: five-state lifecycle, monotonic recovery counters, fenced transition receipts, independent assisted-recovery evidence, and terminal surrender requiring a new lifecycle identity.
