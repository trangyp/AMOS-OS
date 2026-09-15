# Upstream Mechanisms

All entries are `SOURCE_CLAIM` mechanisms, not inherited AMOS authority.

- `openai/openai-agents-python@fbf59a40e9da5adb88d370fefaeaae0478376d4a`: interrupted runs preserve run state and turn budgets; terminal lifecycle effects are not blindly replayable.
- `microsoft/agent-framework@91b3c8b02248e675079419635eceabc7d067bf7c`: workflow checkpoint save/load symmetry and restoration validation.
- `langchain-ai/langgraph@230927fb3a9ac9b2893a30322b4dfea7cdea9a8f`: checkpoint-backed interrupt/resume boundaries.

AMOS adaptation: recovery budget continuity, explicit fenced state transitions, independent assisted-recovery evidence, and terminal surrender semantics.
