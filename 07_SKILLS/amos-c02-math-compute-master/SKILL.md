---
title: SKILL — Amos C02 Math Compute Master
type: skill
source: 07_SKILLS/amos-c02-math-compute-master
name: amos-c02-math-compute-master
description: 'AMOS C02 Math & Compute — 10 families: problem framing, numerical methods, probability, optimization, complexity, control, signal processing, simulation. Use when mathematical reasoning or computational analysis. Do not use for generic math tutoring, symbolic algebra, or tasks outside the 10-family computational framework.'
parent_skill: none
domain: c02
origin_architect: Trang Phan
epistemic_class: SOURCE_CANON
tags:
- type/skill
- canon/skill
- domain/physics-cosmos
- rscf/source_claim
- hml/h
- epistemic/source_canon
- amos_os
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
rscf_state: SOURCE_CLAIM
hml_level: H
gmef_gates:
- L0_integrity
- L1_epistemic
- L2_provenance
- L5_scope
- L7_authority
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L4
- L5
- L7
- L16
- L17
- L18
license: MIT
---
# AMOS C02 — Math & Compute Master Knowledge

## Identity

Origin architect and steward: **Trang Phan**.

This is a **parent skill** that consolidates 100 sub-skills into a single domain master.
Following the skill-organizer best practice: fewer, richer skills beat many overlapping ones.
A parent skill with clearly labeled sections is better than 100 separate shallow skills.

**Epistemic class**: SOURCE_CLAIM (vault-sourced from `11_KNOWLEDGE/AMOS_C02_MATH_COMPUTE_MASTER_KNOWLEDGE.md` (content_hash: 7369abada641e374)).

## When to Use

AMOS C02 Math & Compute — 10 knowledge families: problem framing, numerical methods, probability/statistics, optimization, complexity, control systems, signal processing, simulation, meta-control, ...

- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **c02.problem_framing**: F01 — Classify quantity sought (exact/approximate/order-of-magnitude), optimization vs constraint vs fixed. Run dimensional analysis before numerics (cheapest correctness filter). Back-of-envelope estimation against independent reference points. Decompose along REAL coupling boundaries — two subsystems joined by strong feedback are ONE system for stability purposes.
- **c02.numerical_methods**: F02 — State four disciplines: error control (truncation vs round-off budget), conditioning (κ(A) estimate; flag κ≫1), stability (forward/backward; stiff-system handling), convergence (rate, criteria, termination tests). Allocate error budget up front; propagate through chained methods. Report residual trends, not just iteration count. "It stopped" ≠ "it converged."
- **c02.probability_statistics**: F03 — Apply Kolmogorov axioms, Bayes' theorem with base-rate-neglect guard. Select distribution by data-generating process. Enforce descriptive vs inferential gate (sample mean ≠ population claim without UQ). Confidence intervals / hypothesis testing with p-hacking guard (pre-register, Bonferroni/FDR). Bayesian updating with mandatory prior-sensitivity analysis.
- **c02.optimization**: F04 — Specify decision variables, objective, constraints, parameters, solution, sensitivity. Match problem class (LP/NLP/MIP/convex/multi-objective/stochastic). No global-optimum claims for nonconvex/integer/large-scale. Governance gates: convexity verified, integrality acknowledged, objective aligned with real purpose (proxy-objective drift check), uncertainty propagated not averaged away.
- **c02.complexity_scaling**: F05 — Asymptotic analysis (big-O/Θ) with constant factors treated separately. Hardness classes (P/NP/NP-hard/NP-complete). Practical scaling discipline: report measured behavior, memory footprint, convergence cost, algorithm crossover points. Every complexity claim is a checkpoint to validate empirically, not assert.
- **c02.control_systems**: F06 — Require all six components (plant, controller, sensors, actuators, reference, closed-loop behavior). Tabulate performance trade-off axes (steady-state error vs overshoot vs settling time vs robustness). Linear-model caveat: conclusions hold at stated linearization point only. Design-support only — no autonomous actuation. Robustness probe: perturb plant within stated uncertainty, measure closed-loop degradation.
- **c02.signal_processing**: F07 — Filtering (FIR/IIR/Kalman), transforms (FFT family), spectral estimation, noise suppression (spectral subtraction with floor). Spectral governance: window choice, leakage behavior, and resolution limits must accompany any frequency-domain conclusion. Verify via overlap-add reconstruction test.
- **c02.simulation_validation**: F08 — Paradigm selection (discrete-event/system dynamics/agent-based/Monte Carlo/scenario) with rationale. Document model formulation → parameterisation → execution → output analysis → validation. Execution discipline: fixed-seed reproducibility, sufficient replications, validation ladder (face validity → extreme-condition test → empirical anchor). 6 hard rules including no autonomous action from simulation.
- **c02.meta_control**: F09 — Govern precision mode (low/medium/high), solution strategy (exact vs approximate), computation strategy (symbolic vs numeric). Uncertainty propagation: report bands not points (band width IS part of the answer). Decision interface: confidence attached, decision-sensitive uncertainty identified, least-regret options surfaced, falsifiers and revalidation dates recorded. Gate sequence G1-G4.
- **c02.math_research_bridge**: F10 — QFM stack integration (C02 provides numeric rigor backbone). Fractal/math canon gate: C02 supplies rigor machinery but does NOT certify fractal or quantum claims. Cross-domain handoff: C02 verifies internal consistency, conditioning, statistical validity — domain truth remains with owning domain. Epistemic firewall: no inference from solver success alone, high R² alone, or simulation plausibility alone.

## Consolidated Sub-Skills (100)

This parent skill consolidates the following sub-skills. Each is a section within this domain:

*...and 80 more sub-skills.*

## Vault-Sourced Domain Knowledge

> **Source**: `11_KNOWLEDGE/AMOS_C02_MATH_COMPUTE_MASTER_KNOWLEDGE.md` (content_hash: 7369abada641e374) (vault canon, SOURCE_CLAIM)

### Source Family Mapping

The domain is organized into source families:

- **F01**: System mapping and framing
- **F02**: Numerical methods
- **F03**: Probability, statistics
- **F04**: Optimization governance
- **F05**: Complexity and computation
- **F06**: Control systems
- **F07**: Signal processing, spectral
- **F08**: Simulation validation
- **F09**: Meta-control, error budgets
- **F10**: Meta-math governance

### Major Knowledge Modules

- M1: Framing Before Computing — model selection
- M2: Core Disciplines — method families
- M3: Probability Fundamentals — random variables, distribution selection, inference
- M4: Stochastic System State Models — structural components, problem classes
- M5: Optimization Governance Gates — asymptotic analysis, hardness classes
- M6: Control Systems — performance trade-off axes, control governance
- M7: Signal Processing — spectral governance
- M8: Simulation Governance — paradigm selection, execution discipline, 6 hard rules
- M9: Meta-Control Layer — uncertainty propagation, decision interface
- M10: QFM Stack Integration — fractal/math canon gate, epistemic firewall

### Epistemic Classification

- **Conclusion class**: MIXED (established science + model projections + AMOS synthesis)
- **Evidence policy**: typed_per_node (each claim carries its own evidence type)
- **Canon status**: DOMAIN_KNOWLEDGE_WITH_RESEARCH_BRIDGES
- **Architecture**: HML_fractal_single_file (H/M/L cross-scale reasoning)

### Epistemic Boundary

Every equation class typed: SOURCE_CANON for established math, AMOS_MODEL for Trang constructs. No result without error characterization. No optimum without convexity/hardness statement. No statistical estimate without uncertainty quantification. Control governance: design-support only, no safety-critical deployment, no autonomous actuation. C02 is not an oracle of correctness.


> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 49fa929af7ab6b6f) for detailed vault-sourced domain knowledge.
> **Reference**: See `references/domain_config.md` (content_hash: 5b59808b7d7a3cca) for Mathematics & Computation domain configuration (typical questions, core methods, risk notes).


> **Reference**: See `references/spectral_method_governance.md` (content_hash: 977e0c7e1809f788) for the Spectral-Method Governance Layer (spectral method validation, convergence tests, stability gates).


> **Reference**: See `references/network_structure_diagnostics.md` (content_hash: 63582d102dcaa1b4) for the Network-Structure Diagnostics Layer (network structure validation, graph diagnostics, topology tests).


> **Reference**: See `references/control_systems_kernel.md` (content_hash: 3a8858d1be1880c8) for the Control Systems Kernel v0 Math Foundations (control theory, stability analysis, feedback systems).


> **Reference**: See `references/engineering_math_kernel.md` (content_hash: adedfcf90e737fd1) for the Engineering Math Kernel v0 Tech Systems (engineering mathematics, computational methods, numerical analysis).


> **Reference**: See `references/complex_analysis_bridge.md` (content_hash: a417235d3adf5093) for the AMOS Complex Analysis Bridge (complex analysis, mathematical bridges, computational methods).


> **Reference**: See `references/computational_complexity_model.md` (content_hash: a718b1de21a41fe3) for the AMOS Computational Complexity Model (complexity classes, computational models, complexity analysis).


> **Reference**: See `references/integrated_optimization.md` (content_hash: 596ccb222679ad08) for the Integrated Optimization Complete (optimization integration, performance tuning, system optimization).


> **Reference**: See `references/numerical_methods_engine_layer.md` (content_hash: e40b9f5708c1d2f2) for the AMOS Numerical Methods Engine Layer (numerical methods, computational layer, numerical processing).


> **Reference**: See `references/engineering_math_engine_cognitive.md` (content_hash: 127d892d5c9dbc79) for the AMOS Engineering and Mathematics Engine Cognitive (engineering cognition, math cognition, cognitive engineering).


> **Reference**: See `references/engineering_math_kernel_vinfinity.md` (content_hash: 35e05816b7e55665) for the AMOS Engineering Math Kernel vInfinity (engineering math, kernel, vInfinity).


> **Reference**: See `references/ancient_math.md` (content_hash: 54dff928d7ac1b59) for the Ancient Math (ancient mathematics, historical math, mathematical foundations).

## Provenance

- **Skill**: amos-c02-math-compute-master
- **Source**: AMOS_OS Obsidian vault (`/Users/mac/Documents/AMOS_OS`)
- **Vault source**: `11_KNOWLEDGE/AMOS_C02_MATH_COMPUTE_MASTER_KNOWLEDGE.md` (content_hash: 7369abada641e374)
- **Origin architect**: Trang Phan
- **Consolidation**: 100 sub-skills merged into domain master
- **Merge date**: 2026-08-26

## Merged Skills (Full List)

- `amos-ai-equation-architecture`
- `amos-ai-equation-architecture-2`
- `amos-all-domain-fractal-25000-quantum-math-master`
- `amos-all-domain-fractal-architecture`
- `amos-all-domain-fractal-quantum-math`
- `amos-ancient-math-fractal-architecture`
- `amos-ancient-math-heritage`
- `amos-arxiv-2601-17693-ddfk-fluid-simulation`
- `amos-arxiv-2605-02850-quantum-tilted-loss-variational-optimization`
- `amos-arxiv-2605-22037-classical-rg-gr`
- `amos-arxiv-2607-09381-cosma-fermionic-simulation`
- `amos-arxiv-computer-vision`
- `amos-arxiv-mathematics`
- `amos-arxiv-statistics`
- `amos-awareness-inference-governor`
- `amos-biology-fractal-quantum-coherence`
- `amos-c02-math-compute`
- `amos-canonical-equations-registry`
- `amos-collapse-prediction`
- `amos-core-equations`
- `amos-counterfactual-selfhood-mapper`
- `amos-cross-scale-rscf-tensor-engine`
- `amos-equals-i-squared-law`
- `amos-equation-equals-i-squared`
- `amos-equations-registry`
- `amos-fractal-architecture-framework`
- `amos-fractal-cognitive-architecture`
- `amos-fractal-cognitive-architecture-rules`
- `amos-fractal-cognitive-quantum-logic-math`
- `amos-fractal-equation-families`
- `amos-fractal-math`
- `amos-fractal-math-canon-gate`
- `amos-fractal-math-contract`
- `amos-fractal-math-quantum-convergence`
- `amos-fx-carry-differential-engine`
- `amos-heritage-ancient-fractal-math`
- `amos-heritage-bounded-stochastic-governance-pomdp`
- `amos-heritage-mathematically-correct-core`
- `amos-information-collapse-topology`
- `amos-information-fractal-architecture-50-equations`
- `amos-information-geometry-mapper`
- `amos-language-equation-rscf-engine`
- `amos-learning-memory-fractal-architecture-50-equations`
- `amos-llm-judge-bias-geometry-rscf`
- `amos-master-equation`
- `amos-master-equation-registry`
- `amos-math`
- `amos-math-compute-kernels`
- `amos-math-compute-meta-control`
- `amos-math-core`
- `amos-math-cylinders-plinth-ideal`
- `amos-math-fractal-quantum-bridge`
- `amos-math-manifold-diffusion-semigroups`
- `amos-math-module-valued-odes`
- `amos-math-perturbed-contact-persistence`
- `amos-math-quaternionic-trilinear-forms`
- `amos-math-sheafification-reflective-categories`
- `amos-math-temperley-lieb-canonical-basis`
- `amos-mathematics-of-dao`
- `amos-meta-laws-stability-multi-scale`
- `amos-meta-laws-stability-multiscale`
- `amos-optimization-claim-audit-pipeline`
- `amos-probability-statistics-kernel`
- `amos-process-compliance-auditor-rscf`
- `amos-qfm-adversarial-hardening`
- `amos-qfm-agent`
- `amos-qfm-bridge-governance`
- `amos-qfm-bridge-governance-entropy-lacunarity`
- `amos-qfm-five-layer-architecture`
- `amos-qfm-orchestration`
- `amos-qfm-paper-catalog`
- `amos-qfm-power`
- `amos-qgc-classical-rg-gr`
- `amos-qic-qka-quantum-measurement`
- `amos-qic-tilted-loss-vqa`
- `amos-quantum-arithmetic-geometry-bridge`
- `amos-quantum-control-optimization-fractal-engine`
- `amos-quantum-fractal-math`
- `amos-quantum-fractal-math-2`
- `amos-quantum-fractal-math-3`
- `amos-quantum-fractal-math-index`
- `amos-quantum-library-qec-canonical`
- `amos-quantum-machine-learning-fractal-generalization-engine`
- `amos-quantum-measurement-fractal-observation-math-sampling-bridge`
- `amos-quantum-supremacy`
- `amos-reality-grammar-equation`
- `amos-rg-fractal-quantum-bridge`
- `amos-signal-processing-engine`
- `amos-strict-fractal-equation-database`
- `amos-strict-fractal-equation-rscf-registry`
- `amos-strict-fractal-equations-parameterized`
- `amos-strict-fractal-quantum-atlas`
- `amos-trang-equation-registry`
- `amos-trang-framework-equations`
- `amos-trang-framework-formalization`
- `amos-trang-framework-lmh-lambda`
- `amos-trang-master-equation-registry`
- `amos-trang-phi-framework-17-groups`
- `amos-vn-driver-charging-logistics`
- `amos-wealth-equation`

## Environment Requirements

- Access to AMOS skill corpus for dependency resolution
- Access to AMOS_OS Obsidian vault for vault-sourced content
- No external API credentials required


## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.


## Validation Gates

- **Consistency**: Results must not contain unresolved contradictions within the skill's scope (Law of Law).
- **Epistemic class**: All claims must be labeled SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL — never claim beyond evidence.
- **Provenance**: Source path must be recorded for any derived claim.
- **Anti-overreach**: No claim beyond the skill's declared scope and epistemic class.
- **Bridge discipline**: Cross-domain bridges must be declared; symbolic equality ≠ empirical equality.
- **Equation firewall**: Any equation used must carry a status tag (ESTABLISHED_MATH / SOURCE_DERIVED / AMOS_MODEL / EMPIRICALLY_CALIBRATED / UNVERIFIED).
- **Failure mode**: If validation fails, downgrade confidence, flag the gap, and escalate — do not force-fit.

## Examples

- **Scenario**: User says "What's the computational complexity of this algorithm?"
  - **Input**: An algorithm with unclear complexity
  - **Output**: Complexity analysis across 10 math families (problem framing, numerical methods, probability, optimization, complexity, control, signal processing, simulation), Big-O classification tagged DERIVED

- **Scenario**: User says "Optimize this numerical method for better convergence"
  - **Input**: A numerical method with slow convergence
  - **Output**: Convergence analysis, optimization recommendation from the 10-family framework, stability check, tagged AMOS_MODEL with falsifiers declared

- **Scenario**: When detecting drift in evidence chains, provenance freshness, or confidence calibration
  - **Input**: A query matching this skill's domain (c02)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When validating outputs against domain constraints and epistemic class
  - **Input**: A query matching this skill's domain (c02)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the c02 domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `[[none]]` — routes to this skill when c02 specialization is needed
- **Peers**: Other skills in the `c02` domain may be composed in sequence
- **Orchestrator**: The parent skill or `AMOS_HOME` orchestrates routing
- **Workflow**: Each skill has a corresponding workflow in `08_WORKFLOWS/`
- **Agent**: Each skill has a corresponding agent in `06_AGENTS/`


## Evaluation

### Success Criteria

- Output includes epistemic class label (SOURCE/DERIVED/AMOS_MODEL/EMPIRICAL)
- Output includes provenance reference to source evidence
- Output includes confidence ceiling (capped at 0.95 for DERIVED, 1.0 for SOURCE_CANON)
- Output includes gap flags for unresolved unknowns
- Output does not exceed declared scope

### Failure Modes

- **Overreach**: Output claims validity beyond its epistemic class
- **Scope creep**: Output addresses questions outside the declared domain
- **Provenance loss**: Output cannot trace back to source evidence
- **Confidence inflation**: Output confidence exceeds the weakest-premise ceiling


## Error Handling

- **On scope violation**: Reject the query and route back to parent skill
- **On missing evidence**: Flag as GAP and reduce confidence ceiling to 0.5
- **On contradiction**: Flag as CRITICAL_GAP and halt until resolved
- **On provenance loss**: Mark output as UNKNOWN and require human review
- **On drift**: Trigger drift alignment via `amos-ai-drift-alignment-governor`




See `references/detailed-content.md` for detailed amos canon grounding.

## References

- `references/ancient_math.md` — loaded on demand
- `references/complex_analysis_bridge.md` — loaded on demand
- `references/computational_complexity_model.md` — loaded on demand
- `references/control_systems_kernel.md` — loaded on demand
- `references/domain_config.md` — loaded on demand
- `references/engineering_math_engine_cognitive.md` — loaded on demand
- `references/engineering_math_kernel.md` — loaded on demand
- `references/engineering_math_kernel_vinfinity.md` — loaded on demand
- `references/integrated_optimization.md` — loaded on demand
- `references/network_structure_diagnostics.md` — loaded on demand
- `references/numerical_methods_engine_layer.md` — loaded on demand
- `references/spectral_method_governance.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `[[amos-c02-math-compute-master_MOC]]` — skill Map of Content
- `[[none]]` — parent skill
- `[[amos-c02-math-compute-master-workflow]]` — corresponding workflow
- `[[amos-c02-math-compute-master-agent]]` — corresponding agent


## Do not use

- For generic mathematical analysis outside the math/compute framework
- To claim empirical validation of computational complexity laws
- As a substitute for domain-specific mathematical or computational evidence
- Outside math/compute domain reasoning
