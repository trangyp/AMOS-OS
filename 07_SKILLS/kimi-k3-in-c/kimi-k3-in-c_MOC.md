---
title: Kimi K3 in C — Skill Map of Content
type: moc
skill_id: kimi-k3-in-c
source: 07_SKILLS/kimi-k3-in-c
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_MOC
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  provenance: authoritative_AMOS_OS_structure
  scope: active__AMOS_OS
---
# Kimi K3 in C — Skill Map of Content

**Path:** `07_SKILLS/kimi-k3-in-c`
**Epistemic class:** SOURCE_CLAIM · **H/M/L:** L · **Version:** 1.1.0

## Purpose

Build, test, and run the FareedKhan-dev/kimi-k3-in-c C99 Kimi K3 inference engine. Weightless tests need no checkpoint; full generation requires the 1.56 TB model. Do not use for training, fine-tuning, or non-C99 inference.

## When To Use

- Build the `bin/k3` engine from source.
- Run the weightless test suite (no model weights required).
- Probe memory budgets, list presets, or run the doctor script.
- Prepare a machine before downloading the 1.56 TB checkpoint.

## Do Not Use

- To claim the open-source engine is the official Moonshot Kimi K3 product.
- To download or store 1.56 TB checkpoints without verifying storage and bandwidth.
- For generic LLM fine-tuning, training, or non-inference tasks.

## Capabilities / Operations

- **k3_in_c.build**: Compile the engine.
- **k3_in_c.test**: Run the weightless test suite and report gates.
- **k3_in_c.run**: Execute `bin/k3` with a local model once a checkpoint is present.
- **k3_in_c.diagnose**: Run `scripts/k3-doctor.sh` (Linux only) to check the toolchain and storage. On macOS it exits immediately; use `bin/k3 --list-presets` and `df -h` instead.
- **k3_in_c.budget**: Compute memory budgets with `tools/budget.py <model_dir>` after a checkpoint is present (needs `.safetensors` shards).
- **k3_in_c.info**: Show presets, version, help, and architecture notes.
- **k3_in_c.preset**: Select or validate `--preset` memory configurations.
- **k3_in_c.verify**: Confirm a downloaded checkpoint's byte totals and shard sizes.

## Validation Gates

- **L0 Integrity**: Build artifacts and test outputs accounted for; no silent failures
- **L1 Epistemic**: Repository claims tagged SOURCE_CLAIM; local build commands tagged AMOS_MODEL
- **L5 Scope**: Confined to kimi-k3-in-c repository operations; no scope creep into other inference engines
- **L7 Authority**: No autonomous checkpoint download; user confirmation required for 1.56 TB storage

## Files in this skill

- [[07_SKILLS/kimi-k3-in-c/SKILL.md|SKILL]]
- `07_SKILLS/kimi-k3-in-c/scripts/hooks/hooks_config.yaml`
- `07_SKILLS/kimi-k3-in-c/scripts/hooks/post_tool_use.py`
- `07_SKILLS/kimi-k3-in-c/scripts/hooks/pre_tool_use.py`
- `07_SKILLS/kimi-k3-in-c/scripts/hooks/stop.py`


## Related

- **Parent MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
