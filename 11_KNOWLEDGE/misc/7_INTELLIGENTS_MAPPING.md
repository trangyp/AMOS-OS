---
title: 7 INTELLIGENTS MAPPING
tags:
- misc
- reference
- general
- canon/knowledge
type: document
source: 11_KNOWLEDGE/misc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# 7_Intelligents Engine Mapping

**Purpose**: Domain-specific engine integration with AMOS Brain cognitive layers.

**Location**: `/mnt/skills/user/_AMOS_CANON/7_INTELLIGENTS_MAPPING.md`

---

## Available Engines

### Economics & Finance
**File**: `Core/7_Intelligents/AMOS_Econ_Finance_Engine_v0.json`

**Kernels**:
- `ECON_MICRO_KERNEL` - Firms, households, markets
- `ECON_MACRO_KERNEL` - Growth, inflation, business cycles
- `ECON_PUBLIC_FINANCE_KERNEL` - Taxes, spending, debt
- `FINANCIAL_SYSTEM_KERNEL` - Banks, capital markets, risk

**Primitives**: preference, technology, constraint, equilibrium, output_gap, policy_rate, asset, liability, leverage, liquidity

**Use Cases**: Market analysis, investment strategy, fiscal policy, risk management

---

### Strategy & Game Theory
**File**: `Core/7_Intelligents/AMOS_Strategy_Game_Engine_v0.json`

**Kernels**:
- `GAME_NORMAL_FORM_KERNEL` - Finite games, payoffs, equilibrium
- `GAME_DYNAMICAL_KERNEL` - Repeated games, evolutionary dynamics
- `NEGOTIATION_KERNEL` - Bargaining, coalitions, signals

**Primitives**: player, strategy, payoff, information_set, state, update_rule, reservation_value, offer, threat_point

**Use Cases**: Competitive analysis, negotiation strategy, market entry decisions

---

### Society & Culture
**File**: `Core/7_Intelligents/AMOS_Society_Culture_Engine_v0.json`

**Kernels**:
- `SOC_INSTITUTIONAL_KERNEL` - States, markets, civil society
- `SOC_CULTURAL_NORMS_KERNEL` - Values, rituals, narratives
- `SOC_DEMOGRAPHIC_KERNEL` - Population dynamics, migration
- `SOC_MEDIA_KERNEL` - Information spread, agenda setting

**Primitives**: role, rule, resource_flow, symbol, script, identity_marker, cohort, fertility, attention, framing

**Use Cases**: Cultural trend analysis, demographic forecasting, media strategy

---

### Biology & Cognition
**File**: `Core/7_Intelligents/AMOS_Biology_And_Cognition_Engine_v0.json`

**Kernels**:
- `NEUROBIOLOGY_KERNEL` - Nervous system, perception, decision
- `EMOTIONAL_REGULATION_KERNEL` - Affect, mood, motivation
- `COGNITIVE_ARCHITECTURE_KERNEL` - Memory, attention, reasoning
- `SOMATIC_INTEGRATION_KERNEL` - Body state, health, stress

**Primitives**: neuron, pathway, receptor, affect, appraisal, arousal, working_memory, executive_control, interoception, allostasis

**Use Cases**: Emotional resonance design, cognitive load optimization, behavioral prediction

---

### Engineering & Mathematics
**File**: `Core/7_Intelligents/AMOS_Engineering_And_Mathematics_Engine_v0.json`

**Kernels**:
- `SYSTEMS_DYNAMICS_KERNEL` - Feedback, stability, control
- `OPTIMIZATION_KERNEL` - Linear, nonlinear, combinatorial
- `ALGORITHMICS_KERNEL` - Complexity, data structures, procedures
- `ABSTRACT_ALGEBRA_KERNEL` - Structures, morphisms, symmetries

**Primitives**: state_variable, feedback_loop, objective_function, constraint_set, complexity_class, data_structure, group, ring, field

**Use Cases**: System architecture, algorithm design, optimization problems

---

### Signal Processing
**File**: `Core/7_Intelligents/AMOS_Signal_Processing_Engine_v0.json`

**Kernels**:
- `TIME_FREQUENCY_KERNEL` - Fourier, wavelets, spectra
- `FILTERING_KERNEL` - Noise reduction, extraction, enhancement
- `DETECTION_ESTIMATION_KERNEL` - Hypothesis testing, parameter estimation
- `MULTI_CHANNEL_KERNEL` - Arrays, MIMO, beamforming

**Primitives**: signal, noise, spectrum, impulse_response, transfer_function, likelihood, prior, posterior, covariance, eigenvalue

**Use Cases**: Data analysis, pattern recognition, system identification

---

### Numerical Methods
**File**: `Core/7_Intelligents/AMOS_Numerical_Methods_Engine_v0.json`

**Kernels**:
- `SOLVERS_KERNEL` - Linear, nonlinear, differential equations
- `QUADRATURE_KERNEL` - Integration, Monte Carlo, sampling
- `DISCRETIZATION_KERNEL` - Finite differences, elements, volumes
- `STABILITY_ACCURACY_KERNEL` - Error analysis, conditioning

**Primitives**: matrix, vector, iteration, convergence, truncation_error, condition_number, mesh, basis_function, quadrature_rule, variance

**Use Cases**: Simulation, computation, numerical analysis

---

### Deterministic Logic & Law
**File**: `Core/7_Intelligents/AMOS_Deterministic_Logic_And_Law_Engine_v0.json`

**Kernels**:
- `PROPOSITIONAL_LOGIC_KERNEL` - Boolean, truth, inference
- `PREDICATE_LOGIC_KERNEL` - Quantifiers, domains, models
- `LEGAL_NORMS_KERNEL` - Rules, rights, obligations
- `JURISPRUDENCE_KERNEL` - Interpretation, precedent, reasoning

**Primitives**: proposition, connective, quantifier, predicate, rule, case, precedent, jurisdiction, liability, remedy

**Use Cases**: Formal verification, legal analysis, compliance checking

---

### Mechanical & Structural
**File**: `Core/7_Intelligents/AMOS_Mechanical_Structural_Engine_v0.json`

**Kernels**:
- `STATICS_KERNEL` - Forces, moments, equilibrium
- `DYNAMICS_KERNEL` - Motion, vibration, response
- `MATERIALS_KERNEL` - Stress, strain, failure
- `STRUCTURES_KERNEL` - Beams, trusses, frames

**Primitives**: force, moment, stress, strain, displacement, velocity, acceleration, mass, stiffness, damping

**Use Cases**: Physical system design, structural analysis

---

### Physics & Cosmos
**File**: `Core/7_Intelligents/AMOS_Physics_Cosmos_Engine_v0.json`

**Kernels**:
- `CLASSICAL_MECHANICS_KERNEL` - Newtonian, Lagrangian, Hamiltonian
- `ELECTROMAGNETISM_KERNEL` - Fields, waves, optics
- `THERMODYNAMICS_KERNEL` - Energy, entropy, heat
- `COSMOLOGY_KERNEL` - Space-time, expansion, structure

**Primitives**: position, momentum, energy, field, potential, wave, entropy, temperature, spacetime_metric, redshift

**Use Cases**: Physical modeling, cosmological analysis

---

### Electrical & Power
**File**: `Core/7_Intelligents/AMOS_Electrical_Power_Engine_v0.json`

**Kernels**:
- `CIRCUIT_ANALYSIS_KERNEL` - AC/DC, transients, steady-state
- `POWER_SYSTEMS_KERNEL` - Generation, transmission, distribution
- `ELECTRONICS_KERNEL` - Devices, amplifiers, digital
- `CONTROL_SYSTEMS_KERNEL` - Feedback, stability, response

**Primitives**: voltage, current, resistance, impedance, power, frequency, phase, gain, bandwidth, settling_time

**Use Cases**: Electrical design, power system analysis, control design

---

### Design Language
**File**: `Core/7_Intelligents/AMOS_Design_Language_Engine_v0.json`

**Kernels**:
- `VISUAL_GRAMMAR_KERNEL` - Form, color, composition
- `TYPOGRAPHY_KERNEL` - Fonts, hierarchy, readability
- `INTERACTION_KERNEL` - Affordances, feedback, flow
- `AESTHETICS_KERNEL` - Beauty, proportion, harmony

**Primitives**: shape, color, texture, contrast, alignment, hierarchy, affordance, feedback, gestalt, proportion

**Use Cases**: UI/UX design, visual communication, brand identity

---

## Skill-to-Engine Mapping

### McKinsey Consultant (Analytical Mode)
**Primary Engines**:
- `AMOS_Econ_Finance_Engine` - Market/financial analysis
- `AMOS_Strategy_Game_Engine` - Competitive strategy
- `AMOS_Society_Culture_Engine` - Demographic/cultural trends

**Activation**:
```python
activate_amos_brain(mode="analytical")
# Auto-loads Econ_Finance + Strategy_Game + Society_Culture kernels
```

---

### Mimeng Writing (Creative Mode)
**Primary Engines**:
- `AMOS_Society_Culture_Engine` - Cultural norms, media
- `AMOS_Biology_And_Cognition_Engine` - Emotional processing

**Activation**:
```python
activate_amos_brain(mode="creative")
# Auto-loads Society_Culture + Biology_And_Cognition kernels
```

---

### Shutdown Tracker (Technical Mode)
**Primary Engines**:
- `AMOS_Econ_Finance_Engine` - Financial system analysis
- `AMOS_Numerical_Methods_Engine` - Data computation
- `AMOS_Signal_Processing_Engine` - Trend detection

**Activation**:
```python
activate_amos_brain(mode="technical")
# Auto-loads Econ_Finance + Numerical_Methods + Signal_Processing kernels
```

---

### Code Architect (Technical Mode)
**Primary Engines**:
- `AMOS_Engineering_And_Mathematics_Engine` - System design
- `AMOS_Deterministic_Logic_And_Law_Engine` - Formal verification
- `AMOS_Numerical_Methods_Engine` - Algorithm optimization

**Activation**:
```python
activate_amos_brain(mode="technical")
# Auto-loads Engineering_Math + Deterministic_Logic + Numerical_Methods kernels
```

---

## Cross-Domain Combinations

### Strategic Mode (New)
For complex multi-domain problems:

**Engines**: Strategy_Game + Econ_Finance + Society_Culture + Deterministic_Logic

**Use Case**: Market entry strategy with regulatory analysis

---

### Scientific Mode (New)
For research and analysis:

**Engines**: Physics_Cosmos + Engineering_Math + Numerical_Methods + Signal_Processing

**Use Case**: Scientific modeling and simulation

---

## Engine Selection Heuristics

### Problem Analysis → Engine Selection

| Problem Domain | Primary Engine | Secondary Engine |
|----------------|----------------|------------------|
| Market analysis | Econ_Finance | Strategy_Game |
| Competitive strategy | Strategy_Game | Econ_Finance |
| Cultural trends | Society_Culture | Biology_And_Cognition |
| Emotional design | Biology_And_Cognition | Society_Culture |
| System architecture | Engineering_Math | Deterministic_Logic |
| Data analysis | Signal_Processing | Numerical_Methods |
| Physical systems | Physics_Cosmos | Mechanical_Structural |
| Electrical design | Electrical_Power | Engineering_Math |
| Legal/compliance | Deterministic_Logic | Society_Culture |
| Visual design | Design_Language | Biology_And_Cognition |

---

## Integration with Brain Interface

### Layer 1 (Meta-Logic) + Engines
- Apply Rule of 2 using engine-specific primitives
- Rule of 4 with domain-specific quadrants

### Layer 2 (Structural) + Engines
- Problem decomposition using engine primitives
- Risk lattice with domain-specific failure modes

### Layer 4 (Quantum) + Engines
- Hypothesis superposition with engine-backed weights
- Multi-scenario analysis across engine domains

---

## Version

- **Version**: 1.0.0
- **Date**: 2026-04-13
- **Compatible**: AMOS Brain Interface v1.0+
- **Engines**: 12 total from 7_Intelligents/

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
