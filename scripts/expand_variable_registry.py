#!/usr/bin/env python3
"""Expand 01_CANON/05_VARIABLE_REGISTRY placeholder files with substantive content."""

import os
from pathlib import Path

DIR = Path("/Users/mac/Documents/AMOS_OS/01_CANON/05_VARIABLE_REGISTRY")

# Variable registry content definitions
REGISTRIES = {
    "OMEGA_VARIABLE_REGISTRY.md": {
        "title": "Omega Variable Registry",
        "id": "omega_variable_registry",
        "tags_extra": ["omega", "universe", "collapse", "risk-tension"],
        "purpose": "The Omega Variable Registry defines the canonical variables used in AMOS universe-level reasoning, particularly the Omega collapse probability model and risk tension architecture (URTA).",
        "variables": [
            ("Omega (Ω)", "System coherence / integrity measure", "[0, 1]", "Ω = 1.0 → fully coherent; Ω = 0.0 → total collapse"),
            ("F", "External force / perturbation magnitude", "ℝ⁺", "Higher F → greater collapse pressure"),
            ("S", "System stability / structural resistance", "ℝ⁺", "Higher S → greater resistance to collapse"),
            ("H", "Entropy / disorder accumulation", "ℝ⁺", "Higher H → greater internal disorder"),
            ("Reserves (R)", "Recovery reserve capacity", "ℝ⁺", "Higher R → greater recovery margin"),
            ("P_collapse", "Collapse probability", "[0, 1]", "P_collapse ~ (Ω·F·S)/(H·R)"),
            ("P_recovery", "Recovery probability", "[0, 1]", "P_recovery ~ (R·S)/(H·F)"),
            ("τ (tau)", "Time-to-collapse window", "ℝ⁺ (seconds)", "τ < 0.2 → substrate distress veto threshold"),
        ],
        "formal": """### 2.1 Collapse Probability Model

$$P_{\\text{collapse}} \\sim \\frac{\\Omega \\cdot F \\cdot S}{H \\cdot R}$$

Where:
- $\\Omega$ — system coherence (higher = more coherent, but also more to lose)
- $F$ — external force magnitude
- $S$ — structural stability
- $H$ — entropy accumulation
- $R$ — recovery reserves

### 2.2 Recovery Probability

$$P_{\\text{recovery}} \\sim \\frac{R \\cdot S}{H \\cdot F}$$

### 2.3 Viability Condition

$$\\text{Viable}(S) \\iff P_{\\text{collapse}} < \\theta_{\\text{collapse}} \\wedge P_{\\text{recovery}} > \\theta_{\\text{recovery}}$$

Where $\\theta_{\\text{collapse}}$ and $\\theta_{\\text{recovery}}$ are domain-specific thresholds.""",
    },
    "RSCF_VARIABLE_REGISTRY.md": {
        "title": "RSCF Variable Registry",
        "id": "rscf_variable_registry",
        "tags_extra": ["rscf", "epistemic", "claim", "provenance"],
        "purpose": "The RSCF Variable Registry defines the canonical variables used in RSCF (Reasoning-Source-Claim-Freshness) epistemic classification and claim discipline.",
        "variables": [
            ("state", "RSCF state kind", "{SOURCE_CLAIM, OBSERVATION, DERIVED, MODEL, DECISION, COMPETING, UNKNOWN/GAP}", "Epistemic state of the claim"),
            ("claim_class", "Classification of the claim type", "{STRUCTURAL, EMPIRICAL, DERIVED, AMOS_MODEL, CANONICAL_INVARIANT, ...}", "What kind of claim is being made"),
            ("provenance", "Source lineage", "List[Source]", "Chain of sources supporting the claim"),
            ("scope", "Applicability domain", "String", "Domain where the claim is valid"),
            ("regime", "Operational regime", "{canon, runtime, control, kernel, ...}", "Regime under which the claim operates"),
            ("freshness", "Temporal validity", "{EVERGREEN, SEASONAL, EPHEMERAL, STALE}", "How long the claim remains valid"),
            ("falsifiers", "Conditions that would disprove", "List[Condition]", "What would prove this claim false"),
            ("confidence_ceiling", "Maximum confidence allowed", "[0, 1]", "Upper bound on confidence given evidence"),
            ("provenance_independence", "Source independence status", "{ESTABLISHED, NOT_ESTABLISHED, PARTIAL}", "Whether sources are independent"),
        ],
        "formal": """### 2.1 RSCF State Machine

```text
SOURCE_CLAIM → OBSERVATION → DERIVED → MODEL → DECISION
                                                    ↓
                                              COMPETING → UNKNOWN/GAP
```

### 2.2 Confidence Ceiling Rule

$$\\text{Confidence}(c) \\leq \\text{ConfidenceCeiling}(c) = f(\\text{state}(c), \\text{provenance\_independence}(c))$$

### 2.3 Freshness Decay

$$\\text{Valid}(c, t) \\iff t - \\text{Timestamp}(c) \\leq \\text{ValidityWindow}(\\text{freshness}(c))$$""",
    },
    "UBI_VARIABLE_REGISTRY.md": {
        "title": "UBI Variable Registry",
        "id": "ubi_variable_registry",
        "tags_extra": ["ubi", "biological", "intelligence", "neuroscience"],
        "purpose": "The UBI (Unified Biological Intelligence) Variable Registry defines the canonical variables used in biological intelligence reasoning across the 4 non-compensatory domains: NBI, NEI, SI, BEI.",
        "variables": [
            ("NBI", "Neurobiological Intelligence score", "[0, 1]", "Cognitive, perceptual, and executive function"),
            ("NEI", "Neuroemotional Intelligence score", "[0, 1]", "Emotional awareness and autonomic balance"),
            ("SI", "Somatic Intelligence score", "[0, 1]", "Body awareness and interoceptive accuracy"),
            ("BEI", "Bioelectromagnetic Intelligence score", "[0, 1]", "Cardiac electromagnetic coherence"),
            ("UBI_total", "Unified Biological Intelligence total", "[0, 1]", "Non-compensatory: min(NBI, NEI, SI, BEI)"),
            ("cognitive_load", "Current cognitive load", "[0, 1]", "0.7 = high-load threshold"),
            ("vagal_coherence", "Vagal tone coherence", "[0, 1]", "Autonomic nervous system balance"),
            ("tau (τ)", "Substrate distress indicator", "[0, 1]", "τ < 0.2 → substrate distress veto"),
            ("e", "Quadratic emergence factor", "ℝ", "e = i² (emergence from interaction)"),
            ("clock_40hz", "40Hz multi-agent clock pacing", "Hz", "Gamma-band synchronization frequency"),
        ],
        "formal": """### 2.1 Non-Compensatory Domain Rule

$$\\text{UBI}_{\\text{total}} = \\min(\\text{NBI}, \\text{NEI}, \\text{SI}, \\text{BEI})$$

No domain can compensate for deficiency in another. A low score in any domain caps the total.

### 2.2 Substrate Distress Veto

$$\\tau < 0.2 \\implies \\text{VetoAllConsequentialActions}()$$

### 2.3 Quadratic Emergence

$$e = i^2$$

Where $i$ is the interaction intensity. Emergence is quadratic, not linear — interactions produce disproportionate effects.""",
    },
    "QLS_QCLA_VARIABLE_REGISTRY.md": {
        "title": "QLS/QCLA Variable Registry",
        "id": "qls_qcla_variable_registry",
        "tags_extra": ["qls", "qcla", "quantum", "logic", "causality"],
        "purpose": "The QLS/QCLA Variable Registry defines the canonical variables used in Quantum Logic Structure (QLS) and Quantum Causality Layer Architecture (QCLA) reasoning.",
        "variables": [
            ("|ψ⟩", "Quantum logic state vector", "ℂⁿ", "Superposition of logic states"),
            ("P(|ψ_i⟩)", "Probability of state |ψ_i⟩", "[0, 1]", "Σ P(|ψ_i⟩) = 1"),
            ("M̂", "Measurement/collapse operator", "Matrix", "Applied to collapse superposition"),
            ("Entangle(a,b)", "Entanglement between a and b", "{0, 1}", "1 = entangled, 0 = independent"),
            ("Coherence", "Quantum coherence measure", "[0, 1]", "Ability to maintain superposition"),
            ("CausalDepth", "Causal chain depth", "ℤ⁺", "Number of causal hops from origin"),
            ("CausalClosure", "Causal closure status", "{OPEN, CLOSED, PARTIAL}", "Whether causal chain is complete"),
            ("QCLA_layer", "Causality layer index", "ℤ⁺", "Which QCLA layer governs this causal relation"),
        ],
        "formal": """### 2.1 Superposition State

$$|\\psi\\rangle = \\sum_i \\alpha_i |\\psi_i\\rangle, \\quad \\sum_i |\\alpha_i|^2 = 1$$

### 2.2 Collapse Rule (M̂-hat)

$$\\text{Collapse}(|\\psi\\rangle, \\hat{M}) = |\\psi_k\\rangle \\text{ where } k = \\arg\\max_k |\\langle \\psi_k | \\hat{M} | \\psi \\rangle|^2$$

### 2.3 Entanglement Constraint

$$\\text{Entangle}(a, b) = 1 \\implies \\text{Measure}(a) \\text{ determines } \\text{Measure}(b)$$

### 2.4 Causal Closure

$$\\text{CausalClosure} = \\text{CLOSED} \\iff \\forall\\, \\text{effect } e, \\exists\\, \\text{cause } c : c \\to e$$""",
    },
    "TRANG_VARIABLE_REGISTRY.md": {
        "title": "Trang Variable Registry",
        "id": "trang_variable_registry",
        "tags_extra": ["trang", "framework", "cascade", "distinction"],
        "purpose": "The Trang Variable Registry defines the canonical variables used in the Trang Framework — the recursive ontology dynamics governing distinction, relation, constraint, memory, entropy, repair, recursion, selection, and consequence.",
        "variables": [
            ("D", "Distinction operator", "Operator", "Separates what is from what is not"),
            ("R", "Relation operator", "Operator", "Connects distinct entities"),
            ("C", "Constraint operator", "Operator", "Bounds what relations are allowed"),
            ("M", "Memory operator", "Operator", "Preserves state across time"),
            ("H", "Entropy measure", "ℝ⁺", "Disorder accumulation"),
            ("Repair", "Repair operator", "Operator", "Corrects entropy growth"),
            ("Recursion", "Recursion operator", "Operator", "Repeats patterns at different scales"),
            ("Selection", "Selection operator", "Operator", "Chooses among alternatives"),
            ("Consequence", "Consequence operator", "Operator", "Propagates effects of actions"),
            ("Cascade_level", "Cascade depth level", "ℤ⁺", "Which level of the fractal cascade"),
        ],
        "formal": """### 2.1 Trang Framework Composition

$$\\text{Trang} = D \\circ R \\circ C \\circ M \\circ H \\circ \\text{Repair} \\circ \\text{Recursion} \\circ \\text{Selection} \\circ \\text{Consequence}$$

### 2.2 Cascade Dynamics

$$\\text{Collapse}(L_i) \\to \\text{Recovery}(L_{i-1}) \\to \\text{Rebuild}(L_i) \\to \\text{Evolve}(L_{i+1})$$

Each cascade level can collapse and recover independently, with recovery propagating upward.

### 2.3 Distinction-Relation Duality

$$\\forall\\, x, y : D(x) \\neq D(y) \\implies \\exists\\, R(x, y) \\lor \\exists\\, R(y, x) \\lor \\nexists\\, R(x, y)$$

Distinct entities may or may not be related, but relation requires distinction.""",
    },
    "UNIVERSE_VARIABLE_REGISTRY.md": {
        "title": "Universe Variable Registry",
        "id": "universe_variable_registry",
        "tags_extra": ["universe", "canon", "structure", "topology"],
        "purpose": "The Universe Variable Registry defines the canonical variables used in universe-level structural reasoning — the 7-Part Universe Canon, universe topology, and universe identity architecture.",
        "variables": [
            ("U", "Universe (system under consideration)", "System", "The bounded system being reasoned about"),
            ("P1-P7", "Seven universe canon parts", "{Reality, Flow, Structure, Behavior, Identity, Enforcement, Evolution}", "The 7 parts of the Universe Canon"),
            ("Topology", "Universe topological structure", "Graph", "How universe parts connect"),
            ("Boundary", "Universe boundary definition", "Set", "What is inside vs outside the universe"),
            ("Invariant", "Universe invariant set", "Set[Property]", "Properties that must hold for the universe"),
            ("Epoch", "Universe causal epoch", "ℤ⁺", "Current causal epoch number"),
            ("Viability", "Universe viability measure", "[0, 1]", "Probability of continued coherent existence"),
        ],
        "formal": """### 2.1 Seven-Part Universe Canon

```text
P1: Reality     — external reality/environment boundary
P2: Flow        — constrained throughput, conversion, bottleneck dynamics
P3: Structure   — universe topology, component arrangement
P4: Behavior    — universe behavior rules, state transitions
P5: Identity    — universe identity preservation across change
P6: Enforcement — law stack enforcement, invariant verification
P7: Evolution   — universe evolution, adaptation, learning
```

### 2.2 Universe Viability

$$\\text{Viability}(U) = \\prod_{i=1}^{7} \\text{PartHealth}(P_i)$$

All 7 parts must be healthy for universe viability. Failure in any part reduces overall viability.

### 2.3 Epoch Monotonicity

$$\\text{Epoch}(t_2) > \\text{Epoch}(t_1) \\iff t_2 > t_1$$

Causal epochs are strictly monotonic — no epoch may decrease.""",
    },
    "GMEF_VARIABLE_REGISTRY.md": {
        "title": "GMEF Variable Registry",
        "id": "gmef_variable_registry",
        "tags_extra": ["gmef", "evolution", "mutation", "governance"],
        "purpose": "The GMEF (Governed Mutation Evolution Framework) Variable Registry defines the canonical variables used in governing changes to systems that can themselves alter — reasoning rules, models, policies, parameters, capabilities, architecture, and governance mechanisms.",
        "variables": [
            ("MutationClass", "Mutation classification", "{M0, M1, M2, M3, M4, M5}", "M0 = never autonomous; M5 = fully autonomous"),
            ("Burden", "Mutation burden score", "ℝ⁺", "log2(depth+1) + 2*consequence + 2*irreversibility"),
            ("Depth", "Reasoning depth", "ℤ⁺", "How deep in the reasoning chain"),
            ("Consequence", "Consequence magnitude", "[0, 1]", "Impact severity of the mutation"),
            ("Irreversibility", "Irreversibility measure", "[0, 1]", "How hard to undo"),
            ("AutonomousEnvelope", "Autonomous action envelope", "{depth≤2, consequence≤0.35, irreversibility≤0.20}", "Bounds for autonomous action"),
            ("TrustedCore", "Trusted core preservation", "{PRESERVED, VIOLATED}", "Whether trusted core is intact"),
            ("EvolutionDebt", "Accumulated evolution debt", "ℝ⁺", "Technical debt from mutations"),
        ],
        "formal": """### 2.1 Mutation Burden

$$\\text{Burden} = \\log_2(\\text{Depth} + 1) + 2 \\cdot \\text{Consequence} + 2 \\cdot \\text{Irreversibility}$$

### 2.2 Autonomous Envelope

$$\\text{Autonomous} \\iff \\text{Depth} \\leq 2 \\wedge \\text{Consequence} \\leq 0.35 \\wedge \\text{Irreversibility} \\leq 0.20$$

### 2.3 Escalation Rule

$$\\text{MutationClass} \\in \\{M0, M1, M2\\} \\lor \\text{Burden} > \\theta \\implies \\text{Escalate to user}$$""",
    },
    "BIO_LOGICAL_VARIABLE_REGISTRY.md": {
        "title": "Bio-Logical Variable Registry",
        "id": "bio_logical_variable_registry",
        "tags_extra": ["bio-logical", "biology", "neuroscience", "canon"],
        "purpose": "The Bio-Logical Variable Registry defines the canonical variables used in bio-logical architecture reasoning — translating biological logic into cognitive architecture primitives.",
        "variables": [
            ("CellIntelligence", "Cell intelligence measure", "[0, 1]", "Single-cell cognitive capacity"),
            ("NeuralCoherence", "Neural coherence measure", "[0, 1]", "Neural network synchronization quality"),
            ("GenomicStability", "Genomic stability score", "[0, 1]", "DNA integrity measure"),
            ("Morphogenesis", "Morphogenetic field strength", "ℝ⁺", "Developmental pattern formation"),
            ("BioElectromagnetic", "Bioelectromagnetic field strength", "ℝ⁺", "Endogenous electromagnetic field"),
            ("Neuroplasticity", "Neuroplasticity index", "[0, 1]", "Neural adaptation capacity"),
            ("Homeostasis", "Homeostatic balance", "[0, 1]", "Internal equilibrium maintenance"),
            ("Allostasis", "Allostatic load", "ℝ⁺", "Adaptive stress response cost"),
        ],
        "formal": """### 2.1 Bio-Logical Translation

$$\\text{BioLogic}(b) \\to \\text{CognitivePrimitive}(c) : c = \\phi(b)$$

Where $\\phi$ is the bio-logical translation function mapping biological processes to cognitive architecture primitives.

### 2.2 Homeostatic Balance

$$\\text{Homeostasis} = 1 - |\\text{SetPoint} - \\text{CurrentValue}| / \\text{SetPoint}$$

### 2.3 Allostatic Load

$$\\text{AllostaticLoad} = \\sum_{i} w_i \\cdot \\text{StressResponse}_i$$

Cumulative cost of adaptive stress responses across all systems.""",
    },
    "HERITAGE_VARIABLE_REGISTRY.md": {
        "title": "Heritage Variable Registry",
        "id": "heritage_variable_registry",
        "tags_extra": ["heritage", "ancestral", "decision", "cultural"],
        "purpose": "The Heritage Variable Registry defines the canonical variables used in heritage decision intelligence — 32-layer ancestral decision intelligence, civilizational shock-damping, and polycentric village topology.",
        "variables": [
            ("Layer", "Heritage decision layer", "ℤ⁺ [1-32]", "32-layer ancestral decision hierarchy"),
            ("ShockDamping", "Shock-damping coefficient", "ℝ⁺", "Civilizational shock absorption capacity"),
            ("VillageTopology", "Polycentric village topology", "Graph", "Decentralized village network structure"),
            ("SourceIndependence", "Provenance source independence", "[0, 1]", "Independence of historical sources"),
            ("DecisionReceipt", "Immutable decision receipt", "Hash", "Permanent record of ancestral decisions"),
            ("HydrologicalBuffer", "Hydrological buffering capacity", "ℝ⁺", "Water resource resilience"),
            ("SurvivalInvariant", "Historical survival invariant", "Property", "What must hold for civilizational survival"),
        ],
        "formal": """### 2.1 Heritage Decision Layer

$$\\text{Layer}_{i} : \\text{Decision}_{i} \\to \\text{Wisdom}_{i} \\to \\text{Layer}_{i+1}$$

Each layer transforms decisions into wisdom that feeds the next layer.

### 2.2 Shock Damping

$$\\text{DampedShock}(s) = s \\cdot e^{-\\alpha \\cdot \\text{ShockDamping}}$$

Where $\\alpha$ is the damping coefficient and $s$ is the raw shock magnitude.

### 2.3 Source Independence Audit

$$\\text{Trusted}(h) \\iff \\text{SourceIndependence}(h) > 0.8 \\wedge \\text{DecisionReceipt}(h) \\text{ is valid}$$""",
    },
    "CROSS_CANON_SYMBOL_CROSSWALK.md": {
        "title": "Cross-Canon Symbol Crosswalk",
        "id": "cross_canon_symbol_crosswalk",
        "tags_extra": ["crosswalk", "symbol", "translation", "canon"],
        "purpose": "The Cross-Canon Symbol Crosswalk defines the mapping between symbols used in different AMOS canonical frameworks — ensuring that the same concept uses consistent notation across all canons.",
        "variables": [
            ("Symbol", "Canonical symbol", "String", "The notation used in a specific canon"),
            ("Canon", "Source canon", "{Omega, UBI, QLS, Trang, Universe, RSCF, GMEF, ...}", "Which canon uses this symbol"),
            ("Meaning", "Symbol meaning", "String", "What the symbol represents"),
            ("CrosswalkTarget", "Equivalent symbol in another canon", "String", "The same concept in a different canon's notation"),
            ("ConflictType", "Type of cross-canon conflict", "{NOTATION, SEMANTIC, SCOPE, NONE}", "Whether symbols conflict"),
        ],
        "formal": """### 2.1 Crosswalk Mapping

$$\\text{Crosswalk}(s, c_1, c_2) = (s, c_1) \\to (s', c_2) : \\text{Meaning}(s, c_1) = \\text{Meaning}(s', c_2)$$

### 2.2 Conflict Detection

$$\\text{Conflict}(s, c_1, c_2) \\iff \\text{Meaning}(s, c_1) \\neq \\text{Meaning}(s, c_2)$$

### 2.3 Known Crosswalks

| Symbol | Omega Canon | UBI Canon | Trang Canon | RSCF Canon |
|:---|:---|:---|:---|:---|
| H | Entropy | — | Entropy operator | — |
| Ω | Coherence | — | — | — |
| τ | Time window | Substrate distress | — | — |
| R | Reserves | — | Relation operator | — |
| S | Stability | SI score | — | Scope |
| e | — | Emergence (i²) | — | — |
| D | — | — | Distinction | — |
| M | — | — | Memory | — |""",
    },
}

TEMPLATE = '''---
title: {title}
type: variable
source: 01_CANON/05_VARIABLE_REGISTRY
artifact: {filename}
artifact_id: amos_01_canon_05_variable_registry_{id}
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 01_CANON
segment: 01_CANON/05_VARIABLE_REGISTRY
artifact_kind: REGISTRY
path: 01_CANON/05_VARIABLE_REGISTRY/{filename}
tags:
  - amos-os
  - canon
  - universe
  - registry
  - rscf
  - canon/universe
  - placeholder_expanded
  - law-hierarchy{tags_extra}
version: 1.0.0
updated: '2026-09-04'
status: SUBSTANTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
canonical_status: CONDITIONAL
implementation_status: NOT_ESTABLISHED
validation_status: NOT_ESTABLISHED
executable_binding: NOT_ESTABLISHED
ingestion_action: ADD_ONLY
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
  regime: canon
  confidence_ceiling: source_supported
  provenance_independence: NOT_ESTABLISHED
---

# {title}

## 0. Status

`{filename}` defines the proposed AMOS OS **{title_short}** variable registry.

This artifact replaces a structural placeholder with substantive content. It does not, by its own existence, establish final AMOS canon, executable enforcement, empirical validity, or runtime implementation.

```text
PLACEHOLDER != IMPLEMENTED
ADDRESSABLE != VALIDATED
DOCUMENTED != ENFORCED
MODEL != OBSERVATION
SOURCE_CLAIM != VERIFIED
CANON_CANDIDATE != CANONICAL
CANONICAL != EMPIRICAL_TRUTH
CAPABILITY != AUTHORITY
AUTHORIZATION != COMMIT
PROPOSAL != COMMIT
IMPLEMENTED != VALIDATED
LOGGED != APPROVED
UNKNOWN/GAP != PASS
```

Origin architect / steward: **Trang Phan**

______________________________________________________________________

## 1. Purpose

{purpose}

______________________________________________________________________

## 2. Formal Definition

{formal}

______________________________________________________________________

## 3. Variable Table

| Variable | Description | Type/Range | Notes |
|:---|:---|:---|:---|
{variable_table}

______________________________________________________________________

## 4. Application Domains

### 4.1 Canonical Reasoning

These variables are used in canonical reasoning across the AMOS OS. They provide the canonical notation for concepts that appear in multiple frameworks.

### 4.2 Cross-Canon Translation

When reasoning crosses canon boundaries (e.g., from Omega to UBI), this registry provides the canonical variable mapping.

### 4.3 Validation

When validating AMOS reasoning, the variable registry ensures that:
- Variables are used consistently across canons
- Symbol conflicts are detected and resolved
- Variable types and ranges are respected

______________________________________________________________________

## 5. Non-Purpose

This registry MUST NOT be used to claim:
- That these variables are physically real (they are AMOS_MODEL)
- That the mathematical formulas are empirically validated
- That the variable definitions are final and immutable
- That runtime enforcement is implemented

______________________________________________________________________

## 6. Gaps

- Executable binding NOT_ESTABLISHED — variables are defined but not enforced by runtime code
- Canonical status CONDITIONAL — proposed specification, not yet promoted to full canon
- Cross-canon validation NOT_ESTABLISHED — automated cross-canon consistency checking is not implemented
- Empirical validation NOT_ESTABLISHED — variables have not been empirically tested

______________________________________________________________________

## 7. Promotion-Gate Checklist

- [x] substantive content populated from AMOS corpus sources
- [x] formal definition provided (§2)
- [x] variable table provided (§3)
- [x] application domains specified (§4)
- [ ] typed schema bound to this artifact
- [ ] identity + versioning implemented
- [ ] negative cases covered (missing · malformed · stale · unauthorized input)
- [ ] provenance edges persisted and validated
- [ ] executed validation receipt specific to this artifact
- [ ] unresolved critical gaps registered as UNKNOWN/GAP (visible)

______________________________________________________________________

## 8. Cross-Plane Bindings

- Governed by — [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- Related to — [[01_CANON/05_VARIABLE_REGISTRY/UNIVERSAL_VARIABLE_REGISTRY|UNIVERSAL_VARIABLE_REGISTRY]]
- Related to — [[01_CANON/05_VARIABLE_REGISTRY/SYMBOL_REGISTRY|SYMBOL_REGISTRY]]
- Related to — [[01_CANON/05_VARIABLE_REGISTRY/UNIT_REGISTRY|UNIT_REGISTRY]]
- Observed by — [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]]

______________________________________________________________________

## 9. Ingestion Rule

```yaml
AMOS_CANON_INGESTION_RULE:
  existing_folder:
    preserve: true
  existing_file:
    preserve: true
    overwrite: false
  new_framework:
    action: ADD_FILE_TO_EXISTING_FOLDER
  master_source:
    action: NORMALIZE_TO_RSCF_FILE
  framework_existing_in_multiple_sources:
    action:
      - CREATE_ONE_CANONICAL_NODE
      - LINK_ALL_SOURCE_PROVENANCE
      - DO_NOT_CREATE_DUPLICATE_CANON
  uncertainty:
    action:
      - MARK_GAP_OR_COMPETING
      - NEVER_INVENT_CANON
```

______________________________________________________________________

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] · [[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

______________________________________________________________________

RSCF-NODE

node_id: amos_01_canon_05_variable_registry_{id}

node_type: registry

path: 01_CANON/05_VARIABLE_REGISTRY/{filename}

claim_class: AMOS_MODEL

rscf_state: DERIVED

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

______________________________________________________________________

**MOC:** [[01_CANON/05_VARIABLE_REGISTRY/05_VARIABLE_REGISTRY_MOC|05_VARIABLE_REGISTRY_MOC]]
'''


def expand_file(filepath, content_def):
    filename = os.path.basename(filepath)
    title = content_def["title"]
    title_short = title.replace(" Variable Registry", "").replace(" Crosswalk", "")

    tags_extra = ""
    if "tags_extra" in content_def:
        tags_extra = "\n  - " + "\n  - ".join(content_def["tags_extra"])

    # Build variable table
    var_table = ""
    for var in content_def["variables"]:
        name, desc, vtype, notes = var
        var_table += f"| {name} | {desc} | {vtype} | {notes} |\n"

    content = TEMPLATE.format(
        title=title,
        title_short=title_short,
        filename=filename,
        id=content_def["id"],
        tags_extra=tags_extra,
        purpose=content_def["purpose"],
        formal=content_def["formal"],
        variable_table=var_table.rstrip(),
    )

    with open(filepath, "w") as f:
        f.write(content)
    return len(content)


def main():
    expanded = 0
    for filename, content_def in REGISTRIES.items():
        filepath = DIR / filename
        if filepath.exists():
            size = expand_file(str(filepath), content_def)
            print(f"Expanded {filename}: {size} bytes")
            expanded += 1
        else:
            print(f"WARNING: {filename} not found")
    print(f"\nTotal expanded: {expanded}")


if __name__ == "__main__":
    main()
