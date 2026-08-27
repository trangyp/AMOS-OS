---
origin_architect: Hermes Agent (AMOS session)
provenance: user-supplied canonical v1.0 spec + schema; verified against cosmo-brain/executable_brain_model.py (v22)
confidence: 0.98
epistemic_class: OBSERVATION
conclusion_label: VERIFIED
tags: [canon-group/biology, canon/model, rscf/claim, rscf/provenance, rscf/state/observation, topic/2026-08-22-executable-brain-model-lineag, dated, dated/2026-08-22]
date: 2026-08-22
---

# Executable Brain Model — v1.0 Seed & v22 Lineage

> Canonical anchor for the brain's executable core. The v1.0 spec the user supplied is the **foundational seed**; the vault's `cosmo-brain/executable_brain_model.py` is its direct, faithful descendant.
> See also: 2026-08-22 Executable Code Internals · 2026-08-22 Devin Memory Update

## Core equation
`S_{t+1} = C(F(S_t, U_t))`
- `S_t` current cognitive state, `U_t` input
- `F` transformation stack, `C` control / integrity layer

## v1.0 layer contract (8 layers — the invariant skeleton)
1. **SignalNoiseLayer** — `SNR=Signal/Noise`; `clarity=max(0, signal-noise+baseline)`
2. **IntentLayer** — classify construction / explanation / mapping / repair / general_reasoning
3. **FractalArchitectureLayer** — recursion/nesting/self-reference detection; `x_{n+1}=f(x_n)`, `loop_risk≈recursion_depth+noise`
4. **NetworkLayer** — concept propagation; `x_{t+1}=Ax_t+u_t`
5. **DynamicLayer** — `load=noise+recursion_depth`; `confidence=clarity*(1-load)`
6. **ControlLayer** — `C(S)=interrupt if loop_risk>threshold`; flag low signal, preserve integrity
7. **PlanningLayer** — cognitive state → output plan
8. **MemoryLayer** — store/retrieve recent inputs (hash-encoded)

## v22 preservation (verified 2026-08-22)
All 8 v1.0 layers exist verbatim in `cosmo-brain/executable_brain_model.py` (70 classes total, compiles clean). Faithful extensions, NOT divergences:
- **MemoryLayer**: + decay (recency-weighted), dedup
- **IntentLayer**: + `governance` intent
- **NetworkLayer**: + `governance` graph node
- **ControlLayer**: + behavioral-loop detection (same-input-seen-N-times), thresholds codified (LOOP 0.85, CLARITY 0.25, CONF 0.25)
- **DynamicLayer**: confidence ceiling kept at 0.95 (AMOS RSCF "never claim 100%")

## Limits (from v1.0, still binding)
- Not a biological brain simulation.
- Not consciousness.
- Not medical / psychological diagnosis.
- AI agent architecture skeleton only.

## Files
- Seed spec/schema: user-supplied (v1.0).
- Evolved implementation: `cosmo-brain/executable_brain_model.py`.
- Schema: `cosmo-brain/brain_model_schema.json`.
- Integration layers: v1→v22 (law stack, reasoning loop, UBI, RSCF, etc. — see 2026-08-22 Brain Inventory).

## Links
- 2026-08-22 Brain Inventory
- 2026-08-22 Devin Memory Update
