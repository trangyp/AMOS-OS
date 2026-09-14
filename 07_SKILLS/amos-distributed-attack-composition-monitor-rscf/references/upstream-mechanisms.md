# Upstream Mechanisms

All upstream mechanisms remain `SOURCE_CLAIM` and confer no AMOS authority.

## AgentDojo
Pinned: `ethz-spylab/agentdojo@089ed468cf3ed0322acc66b0211f26d9d90dbf60`.
Transferred concepts: tool-using agent security benchmark separation between user utility and adversarial/injection objectives; repeatable task/attack fixtures.
Not transferred: benchmark success rates as deployment risk estimates; any assumption that single-episode attacks cover distributed composition.

## NVIDIA garak
Pinned: `NVIDIA/garak@3f50ea5ff9cd7050099940647c15c39b07a93392`.
Transferred concepts: explicit vulnerability probes, detectors, and repeatable security evaluation separation.
Not transferred: detector outputs as truth, exploitability proof, or causal attribution.

## Promptfoo
Pinned: `promptfoo/promptfoo@ad3bee3299e3a9864ef6d47482298b2e7f1ceb37`.
Transferred concepts: reproducible red-team/evaluation harnesses and structured agent/session/tool-call evidence.
Not transferred: test pass/fail as universal safety proof.

## AMOS extension
AMOS adds the cross-event composition rule, policy-epoch binding, principal/session diversity predicates, and bounded minimal satisfying event cut-set. These are `AMOS_MODEL` control-plane constructs.
