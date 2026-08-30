---
schema_version: 1.0
title: SKILL
name: kimi-k3-in-c
description: Build, test, and run the FareedKhan-dev/kimi-k3-in-c C99 Kimi K3 inference
  engine. Weightless tests need no checkpoint; full generation requires the 1.56 TB
  model. Do not use for training, fine-tuning, or non-C99 inference.
license: MIT
steward: Trang Phan
version: 1.1.0
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
rscf_state: DERIVED
hml_level: L
tags:
- c99
- inference
- kimi-k3
- weightless-test
- model-free
- operational
- readme
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
type: skill
source: 07_SKILLS/kimi-k3-in-c
---

# Kimi K3 in C

## Identity

Operational skill for the FareedKhan-dev/kimi-k3-in-c Kimi K3 C99 inference engine. Origin: repository README and source (SOURCE_CLAIM). This skill is an AMOS operational wrapper, not a Moonshot product claim.

## When to Use

- Build the `bin/k3` engine from source.
- Run the weightless test suite (no model weights required).
- Probe memory budgets, list presets, or run the doctor script.
- Prepare a machine before downloading the 1.56 TB checkpoint.

## Capabilities

- **k3_in_c.build**: Compile the engine.
- **k3_in_c.test**: Run the weightless test suite and report gates.
- **k3_in_c.run**: Execute `bin/k3` with a local model once a checkpoint is present.
- **k3_in_c.diagnose**: Run `scripts/k3-doctor.sh` (Linux only) to check the toolchain and storage. On macOS it exits immediately; use `bin/k3 --list-presets` and `df -h` instead.
- **k3_in_c.budget**: Compute memory budgets with `tools/budget.py <model_dir>` after a checkpoint is present (needs `.safetensors` shards).
- **k3_in_c.info**: Show presets, version, help, and architecture notes.
- **k3_in_c.preset**: Select or validate `--preset` memory configurations.
- **k3_in_c.verify**: Confirm a downloaded checkpoint's byte totals and shard sizes.

## Operations

1. **k3_in_c.build**: Compile the engine.
2. **k3_in_c.test**: Run the weightless test suite and report gates.
3. **k3_in_c.run**: Execute `bin/k3` with a local model once a checkpoint is present.
4. **k3_in_c.diagnose**: Run `scripts/k3-doctor.sh` (Linux only) to check the toolchain and storage. On macOS it exits immediately; use `bin/k3 --list-presets` and `df -h` instead.
5. **k3_in_c.budget**: Compute memory budgets with `tools/budget.py <model_dir>` after a checkpoint is present (needs `.safetensors` shards).
6. **k3_in_c.info**: Show presets, version, help, and architecture notes.
7. **k3_in_c.preset**: Select or validate `--preset` memory configurations.
8. **k3_in_c.verify**: Confirm a downloaded checkpoint's byte totals and shard sizes.

## Build

```bash
cd <repo>
make -j OMP_CFLAGS= OMP_LDFLAGS=
```

On macOS/arm64 with Homebrew `libomp`:

```bash
make -j
```

Requires: C99 compiler, `make`, `libm`, `pthread`. OpenMP is optional; without it the engine compiles single-threaded but still passes weightless tests.

## Test

```bash
make -B -j test OMP_CFLAGS= OMP_LDFLAGS=
```

Expected verdict: `ALL WEIGHTLESS TESTS PASSED` and `ENGINE MATCHES THE REFERENCE EXACTLY`.

## Run

Full generation requires the 1.56 TB checkpoint:

```bash
export HF_TOKEN=hf_...
./scripts/download-model.sh ~/k3model
./scripts/pack-trunk.sh ~/k3model ~/k3trunk
./bin/k3 ~/k3model --trunk ~/k3trunk --preset laptop \
  --tok ~/k3model --prompt "The capital of France is" --gen 8 --incremental
```

Use `--ids` to bypass the tokenizer and run ids-to-ids with no checkpoint vocabulary.

## Notes

- The open-source repository is a C99 inference implementation (SOURCE_CLAIM).
- The `2.78T parameters / 8.24 GB peak RSS` claim is from the repository author (SOURCE_CLAIM), not independently reproduced here.
- The memory-ladder, cache, and trunk-streaming behavior are documented in `docs/` (SOURCE_CLAIM).
- `scripts/k3-doctor.sh` is Linux-only; it uses `/proc/meminfo`, `O_DIRECT`, and GNU `stat`/`df` (OBSERVATION: exits immediately on Darwin).
- `tools/budget.py` requires a model directory containing `.safetensors` shards; it cannot budget from the repository alone.

## Validation Gates

- **L0 Integrity**: Build artifacts and test outputs accounted for; no silent failures
- **L1 Epistemic**: Repository claims tagged SOURCE_CLAIM; local build commands tagged AMOS_MODEL
- **L5 Scope**: Confined to kimi-k3-in-c repository operations; no scope creep into other inference engines
- **L7 Authority**: No autonomous checkpoint download; user confirmation required for 1.56 TB storage

## Do not use

- To claim the open-source engine is the official Moonshot Kimi K3 product.
- To download or store 1.56 TB checkpoints without verifying storage and bandwidth.
- For generic LLM fine-tuning, training, or non-inference tasks.

## Provenance

- **Source**: FareedKhan-dev/kimi-k3-in-c repository
- **Epistemic class**: SOURCE_CLAIM
- **Origin architect**: FareedKhan

## Related resources

- **Best available C99 inference implementation**: `https://github.com/FareedKhan-dev/kimi-k3-in-c` (portable C99, no BLAS/GPU, weightless tests, 1.56 TB checkpoint for full generation).
- **Official model canon**: `https://github.com/MoonshotAI/Kimi-K3` — Moonshot AI model card, API, and vLLM/SGLang recipes. This is the upstream model, not the C99 engine; do not conflate the two.
- **Build/test reference for this skill**: the FareedKhan-dev repository README, `docs/`, `scripts/k3-doctor.sh`, `tools/budget.py`, and the weightless test suite.

---

**MOC:** references_MOC · [[00_ROOT/00_HOME|00_HOME]]
