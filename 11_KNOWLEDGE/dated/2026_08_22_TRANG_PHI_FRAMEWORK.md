---
title: 2026 08 22 TRANG PHI FRAMEWORK
type: trang-framework
origin_architect: Hermes Agent (AMOS session)
provenance: user-supplied canonical 17-group equation catalog (Trang ∅ Framework) + implemented & verified Python agent
confidence: 0.95
epistemic_class: SOURCE_DERIVED
conclusion_label: VERIFIED
tags: [canon-group/human-system, canon/metric, rscf/claim, rscf/provenance, rscf/state/observation, topic/2026-08-22-trang-phi-framework, dated, dated/2026-08-22]
date: 2026-08-22
---



# Trang ∅ Framework — 17-Group Equation Catalog & Trang Agent

> Canonical anchor for the Trang ∅ Framework (origin architect: Trang Phan), the founding fractal theory the brain already encodes (see `cosmo-brain/.../brain/20_state/ENTROPY_LACUNARITY.md` and `EQUATION_FIREWALL.md`).

## The 17 equation groups (user-supplied taxonomy)
0. Foundational definitions (S={L,M,H}, X∈{L,M,H})
1. Basic structure (partition 1.1; three-tier relation 1.2)
2. Entropy E (Shannon normalized 2.1; weighted total 2.2; golden-zone thresholds 2.3; dE/dt 2.4)
3. Lacunarity Λ (Var/Mean² 3.1/3.2; sigmoid E-Λ 3.3; thresholds 3.4)
4. Dynamics (evolution eq 4.1; mutation 4.2; selection 4.3; survival 4.4)
5. Tát 2 cross-validation (∧ of ≥2 sources 5.1; correctness prob 5.2)
6. Integration scale (quality Q 6.1; health 6.2)
7. Cascade (10 collapse stages 7.1; 12 recovery 7.2; transition 7.3)
8. LDAI (logical determinism 8.1–8.4)
9. FRAI (fractal reasoning 9.1–9.3)
10. ASEA (lacunarity adj 10.1; entropy adj 10.2; prune/add 10.3; hallucination 10.4; state 10.5; evolve 10.6; survival 10.7; Δw 10.8)
11. Universal constants (π, e, φ, 19, 137)
12. Framework constants (θ_hallucination=0.3, θ_rigid=0.05, θ_healthy_L/M/H, Λ_optimal=0.2, η=0.01)
13. Quantity links (E-Λ-Health 13.1; recovery R 13.2; dΛ/dt 13.3)
14. Confirmation checks (Tát 2 auto 14.1; inter-tier consistency 14.2)
15. Special phenomena (hallucination 15.1; belief drift 15.2; synchrony/telepathy 15.3)
16. Quantization (discrete energy 16.1; instantaneous step 16.2)
17. Master equation (dS/dt 17.1)

## Implemented & VERIFIED: Trang Agent (Python)
Location: `cosmo-brain/trang_agent/` — runs clean.
- `trang_agent_core.py`: decompose (1.1/9.1), calculate_entropy (2.1), calculate_lacunarity (3.1/3.2), entropy_lambda_relation (3.3), is_healthy (6.2).
- `trang_agent_reasoning.py`: survive_basic (4.4), t2_validate (5.1/14.1), detect_hallucination (15.1), belief_drift (15.2), ASEAState + evolve_asea (10.1/10.2/10.6), survive_asea (10.7).
- `trang_agent_population.py`: 100-agent genetic evolution, natural-selection survival + elite reproduction toward Λ_optimal.
- `trang_agent_main.py`: demo + sample config JSON.

**Verification result:** sample FOREX input analyzed; 100-agent population converges mean λ_target → 0.2 (Λ_optimal) over 20 generations.

## Equation-Firewall compliance (critical)
Per `EQUATION_FIREWALL.md`: every equation carries a status. The framework's thresholds (θ=0.3, E_golden=0.15, Λ_optimal=0.2) are **AMOS_MODEL / UNVERIFIED** — the framework's OWN symbolic definitions, NOT universally validated empirical facts. The code computes them as specified but does NOT assert they hold for all domains. Entropy/lacunarity require domain-specific definitions before numerical use.

## Framework mandates honored in code
- No "signal/noise" duality — only mutation & survival.
- No gradient descent — natural selection only (Δw = η·∇Survival, 10.8).
- Every decision requires Tát 2 (≥2 independent sources).
- Agent self-adjusts Λ (10.1) and E (10.2).


## Test & Improve log (2026-08-22, verified run)

**Tests added & passing:**
- `trang_agent_core.self_test()` — entropy (uniform n=4 → 1.0; single bin → 0.0), lacunarity (identical → 0.0; varied > 0), health (golden → ~1.0), decompose returns 3 tiers, constants (φ exact).
- `trang_agent_reasoning.self_test()` — Tát 2 (needs ≥2 sources), hallucination (E_H>0.3 ∧ Λ unstable), survive rules, belief_drift=0 at golden E.
- Determinism: `run_population(seed=42)` is now reproducible (injected `random.Random(seed)` per Eq 8.1 LDAI: same input → same output). Previously used global RNG → nondeterministic.
- Convergence: 100-agent population mean λ_target → 0.201 ≈ Λ_optimal (0.2) over 20 gens; passes across seeds 1/7/42/99/123; tiny pop (5) survives (no extinction bug).
- `python trang_agent_main.py` prints SELF-TESTS block: core/PASS, reasoning/PASS, determinism/PASS, convergence/PASS, OVERALL/PASS.

**Improvement made:**
- Fixed nondeterminism by replacing module-global `random` with an injected `random.Random(seed)` in `trang_agent_population.py` (Agent.mutate/step, run_population). This makes the agent a *verifiable* LDAI component.

**Known limitation (honest):**
- The `decompose()` token→mass proxy yields near-uniform distributions for natural-language input, so measured entropy is artificially high (0.8–0.99). This is a stand-in; real entropy/lacunarity require domain-specific mass definitions (per EQUATION_FIREWALL.md). The MATH itself is correct — only the decomposition heuristic is naive.

## Links
- 2026-08-22 Brain Inventory
- 2026-08-22 Executable Brain Model Lineage
- cosmo-brain/AMOS_MD_BRAIN_FULL_INFRA/brain/20_state/ENTROPY_LACUNARITY.md

---
**Links:** [[DATED_MOC]] | [[KNOWLEDGE_MOC]]
