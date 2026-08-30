---
Type: Workflow
Skill: kimi-k3-in-c
Agent: amos-kimi-k3-in-c-agent
Trigger: When the kimi-k3-in-c C99 inference engine needs building, testing, running,
  or diagnosing without requiring the full 1.56 TB checkpoint.
Version: 1.0.0
title: Kimi K3 in C Workflow
tags:
- type/workflow
- domain/tech-engineering
- amos-os
- skill
type: workflow
source: 08_WORKFLOWS
rscf:
  state: AMOS_MODEL
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: workflow_process
---

# Workflow: Kimi K3 in C

## Preconditions

- The bound skill exists and is loaded.
- The bound agent is available and has valid content_hash.
- The query falls within the skill's declared scope (build, test, run, diagnose, budget, info, preset, verify).
- The repository is present or can be cloned from FareedKhan-dev/kimi-k3-in-c.

## Orchestration Pattern

1. **Load skill** — Read kimi-k3-in-c SKILL.md and verify capabilities match the request.
2. **Classify request** — Map to one of: build, test, run, diagnose, budget, info, preset, verify.
3. **Check preconditions** — Verify toolchain (C99 compiler, make, libm, pthread), storage, and RAM.
4. **Execute capability** — Run the matching command with appropriate flags.
5. **Validate output** — Check for expected pass/fail signals (e.g., `ALL WEIGHTLESS TESTS PASSED`).
6. **Report results** — Return structured output with epistemic class and provenance.

## Evaluation Gates

- **G1 (Build)**: `make -j` exits 0 and produces `bin/k3` binary.
- **G2 (Test)**: `make -B -j test` outputs `ALL WEIGHTLESS TESTS PASSED`.
- **G3 (Scope)**: No claim beyond repository contents or AMOS_MODEL labels.
- **G4 (Safety)**: No autonomous checkpoint download; user confirmation required.
- **G5 (Provenance)**: All figures tagged SOURCE_CLAIM (repository) or AMOS_MODEL (local).

## Error Handling

- **Build failure**: Report compiler errors, suggest platform-specific fixes (e.g., `OMP_CFLAGS= OMP_LDFLAGS=` on macOS without libomp).
- **Test failure**: Report which weightless tests failed, suggest checking source integrity.
- **Missing checkpoint**: Inform user of 1.56 TB requirement, do not auto-download.
- **Missing libomp**: Suggest `brew install libomp` or single-threaded build.

## Human-in-the-Loop

- Checkpoint download (1.56 TB) requires explicit user confirmation.
- Storage and bandwidth verification before any download.
- Preset selection for memory-constrained environments.

## Monitoring

- Build exit code and binary presence.
- Test suite pass/fail counts.
- Memory budget computation results.
- Doctor script diagnostics output.

## Composition

- Can be invoked by amos-c10-tech-engineering-master for C inference engine tasks.
- Can delegate to amos-os-runtime-master for runtime execution monitoring.
- No delegation to non-AMOS skills.

## Related

- [[08_WORKFLOWS/08_WORKFLOWS_MOC|08_WORKFLOWS_MOC]]

---

**MOC:** [[08_WORKFLOWS/law-stack-enforcement-pipeline/law-stack-enforcement-pipeline_MOC|law-stack-enforcement-pipeline_MOC]] · [[00_ROOT/00_HOME|00_HOME]]
