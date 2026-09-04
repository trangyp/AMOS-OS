#!/usr/bin/env python3
"""Expand 01_CANON/06_GLOSSARY placeholder files with substantive glossary content."""

import os
from pathlib import Path

DIR = Path("/Users/mac/Documents/AMOS_OS/01_CANON/06_GLOSSARY")

GLOSSARIES = {
    "AMOS_FRAMEWORK_GLOSSARY.md": {
        "title": "AMOS Framework Glossary",
        "id": "amos_framework_glossary",
        "tags_extra": ["framework", "amos", "glossary"],
        "intro": "The AMOS Framework Glossary defines the canonical terminology used across the AMOS OS framework — covering core architectural concepts, structural primitives, and governance mechanisms.",
        "terms": [
            ("AMOS", "Autonomous Multi-Operational System — the complete cognitive architecture", "Core"),
            ("Canon", "Canonical law or principle that governs a domain of the system", "Governance"),
            ("Core Law", "Foundational law in the L0-L32 law hierarchy", "Governance"),
            ("Kernel", "The runtime kernel that enforces canonical laws during execution", "Runtime"),
            ("Control Plane", "The plane that manages authority, delegation, and policy", "Governance"),
            ("Runtime", "The execution engine that carries out governed operations", "Runtime"),
            ("RSCF", "Reasoning-Source-Claim-Freshness — epistemic classification framework", "Epistemic"),
            ("HML", "High/Mid/Low — three-speed validation lens for claim rigor", "Epistemic"),
            ("MECE", "Mutually Exclusive, Collectively Exhaustive — structural property", "Architecture"),
            ("GMEF", "Governed Mutation Evolution Framework — governs system self-modification", "Evolution"),
            ("MOC", "Map of Content — navigational index for a vault section", "Navigation"),
            ("Plane", "A top-level architectural division (Canon, Kernel, Control, Runtime)", "Architecture"),
            ("Segment", "A sub-division within a plane", "Architecture"),
            ("Artifact", "A typed, provenance-stamped document in the vault", "Structure"),
            ("Receipt", "A cryptographic record of a consequential action", "Audit"),
            ("Checkpoint", "A verified state snapshot for recovery", "Recovery"),
            ("Epoch", "A causal epoch — a validity interval for causal state", "Causality"),
            ("Shard", "A locally-finalized partition of system state", "Distributed"),
            ("MVCC", "Multi-Version Concurrency Control", "Concurrency"),
            ("CAS", "Compare-And-Swap — atomic concurrency primitive", "Concurrency"),
            ("ALU", "Absolute Logic Unit — irreducible logic primitive (19 total)", "Logic"),
            ("UML", "Universal Meta-Law — governing meta-law (7 total)", "Logic"),
            ("UOP", "Universal Operator Primitive — operational primitive (6 total)", "Logic"),
            ("LoL", "Law of Law — the highest-order meta-law", "Logic"),
            ("R2", "Rule of 2 — minimum 2 independent sources for actionable claims", "Epistemic"),
            ("R4", "Rule of 4 — maximum 4 components per abstraction layer", "Architecture"),
            ("UBI", "Unified Biological Intelligence — 4-domain biological model", "Biology"),
            ("QLS", "Quantum Logic Structure — superposition reasoning framework", "Quantum"),
            ("QCLA", "Quantum Causality Layer Architecture — quantum causal model", "Quantum"),
            ("FRAI", "Fractal Reasoning AI — recursive self-similar reasoning", "Reasoning"),
            ("TSS", "The Trang System — governance and institutional framework", "Governance"),
            ("TPE", "Trang Prediction Engine — foresight and prediction system", "Reasoning"),
        ],
    },
    "UNIVERSE_OMEGA_GLOSSARY.md": {
        "title": "Universe/Omega Glossary",
        "id": "universe_omega_glossary",
        "tags_extra": ["universe", "omega", "glossary"],
        "intro": "The Universe/Omega Glossary defines terminology used in universe-level and Omega framework reasoning — covering the 7-Part Universe Canon, collapse dynamics, and risk tension architecture.",
        "terms": [
            ("Universe Canon", "The 7-part canonical specification of universe-level structure", "Universe"),
            ("Omega (Ω)", "System coherence/integrity measure [0,1]", "Omega"),
            ("P_collapse", "Collapse probability ~ (Ω·F·S)/(H·R)", "Omega"),
            ("P_recovery", "Recovery probability ~ (R·S)/(H·F)", "Omega"),
            ("URTA", "URTA Risk Tension Architecture — formal risk lattice", "Omega"),
            ("Cascade", "Fractal collapse-recovery structure across system scales", "Universe"),
            ("Collapse", "System failure event — loss of structural integrity", "Universe"),
            ("Recovery Basin", "Immutable state snapshot (M_0, S_0) for crisis de-escalation", "Recovery"),
            ("DMER", "Deterministic Multi-Epoch Recovery — Level 5 recovery protocol", "Recovery"),
            ("Viability", "Probability of continued coherent existence [0,1]", "Universe"),
            ("Topology", "Universe structural arrangement — how parts connect", "Universe"),
            ("Epoch", "Causal epoch — strict monotonic validity interval", "Causality"),
            ("P1 Reality", "External reality/environment boundary (Universe Canon Part 1)", "Universe"),
            ("P2 Flow", "Constrained throughput, conversion, bottleneck dynamics (Part 2)", "Universe"),
            ("P3 Structure", "Universe topology, component arrangement (Part 3)", "Universe"),
            ("P4 Behavior", "Universe behavior rules, state transitions (Part 4)", "Universe"),
            ("P5 Identity", "Universe identity preservation across change (Part 5)", "Universe"),
            ("P6 Enforcement", "Law stack enforcement, invariant verification (Part 6)", "Universe"),
            ("P7 Evolution", "Universe evolution, adaptation, learning (Part 7)", "Universe"),
            ("Omniverse", "Absolute Omniverse / U-Infinity — complete multimodal ontology", "Universe"),
        ],
    },
    "UBI_GLOSSARY.md": {
        "title": "UBI Glossary",
        "id": "ubi_glossary",
        "tags_extra": ["ubi", "biological", "glossary"],
        "intro": "The UBI (Unified Biological Intelligence) Glossary defines terminology for the 4 non-compensatory biological intelligence domains and their integration into cognitive architecture.",
        "terms": [
            ("UBI", "Unified Biological Intelligence — 4-domain biological model", "Core"),
            ("NBI", "Neurobiological Intelligence — cognitive, perceptual, executive function", "Domain"),
            ("NEI", "Neuroemotional Intelligence — emotional awareness, autonomic balance", "Domain"),
            ("SI", "Somatic Intelligence — body awareness, interoceptive accuracy", "Domain"),
            ("BEI", "Bioelectromagnetic Intelligence — cardiac electromagnetic coherence", "Domain"),
            ("Non-compensatory", "No domain can compensate for deficiency in another", "Property"),
            ("Substrate Distress", "Biological substrate under harmful stress (τ < 0.2)", "Safety"),
            ("Quadratic Emergence", "e = i² — emergence from interaction is quadratic", "Model"),
            ("40Hz Clock", "Gamma-band multi-agent synchronization frequency", "Synchronization"),
            ("Vagal Coherence", "Autonomic nervous system balance measure [0,1]", "Physiology"),
            ("Cognitive Load", "Current cognitive resource utilization [0,1]", "Cognition"),
            ("ConsentX", "Consent arbitration rooted in biological law and autonomic alignment", "Governance"),
            ("UBI Score", "Composite biological intelligence score = min(NBI, NEI, SI, BEI)", "Measurement"),
            ("Wearable Telemetry", "Continuous physiological monitoring interface", "Interface"),
        ],
    },
    "QLS_QCLA_GLOSSARY.md": {
        "title": "QLS/QCLA Glossary",
        "id": "qls_qcla_glossary",
        "tags_extra": ["qls", "qcla", "quantum", "glossary"],
        "intro": "The QLS/QCLA Glossary defines terminology for Quantum Logic Structure (QLS) and Quantum Causality Layer Architecture (QCLA) — AMOS quantum-analog reasoning frameworks.",
        "terms": [
            ("QLS", "Quantum Logic Structure — superposition reasoning framework", "Core"),
            ("QCLA", "Quantum Causality Layer Architecture — quantum causal model", "Core"),
            ("Superposition", "Multiple logic states held simultaneously before collapse", "QLS"),
            ("Collapse (M̂)", "Measurement operator that collapses superposition to one state", "QLS"),
            ("Entanglement", "Correlation between states such that measuring one determines the other", "QLS"),
            ("Coherence", "Ability to maintain superposition without premature collapse", "QLS"),
            ("QIC", "Quantum Information Channel — substrate for quantum logic operations", "Infrastructure"),
            ("QCLA Layer", "Causality layer index in the quantum causal architecture", "QCLA"),
            ("Causal Closure", "Whether a causal chain is complete (all effects have causes)", "QCLA"),
            ("Quantum Fractal", "Scale-invariant quantum logic decomposition (H/M/L)", "Fractal"),
            ("Lacunarity", "Texture analysis measure for gap detection in patterns", "Fractal"),
            ("M-hat", "Deterministic state collapse operator", "QLS"),
        ],
    },
    "TRANG_FRAMEWORK_GLOSSARY.md": {
        "title": "Trang Framework Glossary",
        "id": "trang_framework_glossary",
        "tags_extra": ["trang", "framework", "glossary"],
        "intro": "The Trang Framework Glossary defines terminology for the Trang Framework — the recursive ontology dynamics governing distinction, relation, constraint, memory, entropy, repair, recursion, selection, and consequence.",
        "terms": [
            ("Trang Framework", "Recursive ontology dynamics for complex system modeling", "Core"),
            ("Distinction (D)", "Operator that separates what is from what is not", "Primitive"),
            ("Relation (R)", "Operator that connects distinct entities", "Primitive"),
            ("Constraint (C)", "Operator that bounds allowed relations", "Primitive"),
            ("Memory (M)", "Operator that preserves state across time", "Primitive"),
            ("Entropy (H)", "Measure of disorder accumulation", "Primitive"),
            ("Repair", "Operator that corrects entropy growth", "Primitive"),
            ("Recursion", "Operator that repeats patterns at different scales", "Primitive"),
            ("Selection", "Operator that chooses among alternatives", "Primitive"),
            ("Consequence", "Operator that propagates effects of actions", "Primitive"),
            ("Trang Cascade", "Fractal time structure of collapse and recovery", "Dynamics"),
            ("Khung Trang", "Vietnamese: Trang Architecture — operational reality architecture", "Architecture"),
            ("Phuong Phap Trang", "Vietnamese: Trang Method — brain loop methodology", "Method"),
            ("Tát 2", "Vietnamese: Rule of 2 — confirmation by 2 independent sources", "Epistemic"),
            ("FPR", "First Principle Reasoning — reasoning from irreducible truths", "Method"),
            ("LDAI", "Logical-Decision-AI formalization", "Reasoning"),
        ],
    },
    "TSS_TPE_GLOSSARY.md": {
        "title": "TSS/TPE Glossary",
        "id": "tss_tpe_glossary",
        "tags_extra": ["tss", "tpe", "governance", "glossary"],
        "intro": "The TSS/TPE Glossary defines terminology for The Trang System (TSS) governance framework and Trang Prediction Engine (TPE) foresight system.",
        "terms": [
            ("TSS", "The Trang System — governance and institutional framework", "Core"),
            ("TPE", "Trang Prediction Engine — foresight and prediction system", "Core"),
            ("Seven Cycles", "C1-C7 evolutionary cycles of The Trang System", "Evolution"),
            ("13 Institutions", "Governing institutions of the TSS", "Governance"),
            ("9 Entity Types", "Entity types in the TSS governance economy", "Governance"),
            ("Omega/H/F/S", "TSS risk vectors: coherence, entropy, force, stability", "Risk"),
            ("Strategic Foresight", "Multi-dimensional lifecycle state tracking", "Prediction"),
            ("Modular Decoupling", "Gate: Omega > 0.7 required for modular separation", "Architecture"),
            ("Multi-Horizon Planning", "Intervention planning across multiple time horizons", "Prediction"),
            ("Trang Legacy", "1000-year horizon optimization for survivability", "Strategy"),
        ],
    },
    "NEUROSYNCAI_GLOSSARY.md": {
        "title": "NeuroSyncAI Glossary",
        "id": "neurosyncai_glossary",
        "tags_extra": ["neurosyncai", "neuroscience", "bci", "glossary"],
        "intro": "The NeuroSyncAI Glossary defines terminology for the NeuroSyncAI framework — brain-computer interface and neural synchronization AI systems.",
        "terms": [
            ("NeuroSyncAI", "Neural synchronization AI framework for BCI systems", "Core"),
            ("BCI", "Brain-Computer Interface — direct neural communication pathway", "BCI"),
            ("Neural Sync", "Synchronization between biological neurons and AI systems", "BCI"),
            ("Neuroprosthetic", "Artificial device replacing or augmenting neural function", "BCI"),
            ("Neural Decoder", "AI system that translates neural signals to commands", "BCI"),
            ("Neural Encoder", "AI system that translates commands to neural stimulation", "BCI"),
            ("Closed-Loop BCI", "BCI with real-time feedback from neural response", "BCI"),
            ("Neural Lace", "Fine-mesh neural interface for distributed brain recording", "BCI"),
            ("Neural Dust", "Millimeter-scale wireless neural sensors", "BCI"),
            ("Neurograins", "Micrometer-scale neural recording/stimulation nodes", "BCI"),
            ("Cortical Decoder", "AI decoder for cortical neural activity patterns", "BCI"),
            ("Neural Plasticity", "Brain's ability to reorganize neural connections", "Neuroscience"),
            ("Synaptic Weight", "Strength of connection between two neurons", "Neuroscience"),
            ("Neural Oscillation", "Rhythmic neural activity (delta, theta, alpha, beta, gamma)", "Neuroscience"),
            ("Gamma Band", "40Hz neural oscillation associated with conscious awareness", "Neuroscience"),
        ],
    },
    "HERITAGE_GLOSSARY.md": {
        "title": "Heritage Glossary",
        "id": "heritage_glossary",
        "tags_extra": ["heritage", "ancestral", "cultural", "glossary"],
        "intro": "The Heritage Glossary defines terminology for heritage decision intelligence — 32-layer ancestral decision systems, civilizational shock-damping, and polycentric village topology.",
        "terms": [
            ("Heritage Decision", "Decision rooted in ancestral/civilizational wisdom", "Core"),
            ("32-Layer Hierarchy", "Ancestral decision intelligence layer structure", "Structure"),
            ("Shock-Damping", "Civilizational shock absorption capacity", "Resilience"),
            ("Polycentric Village", "Decentralized village network topology", "Topology"),
            ("Source Independence", "Independence of historical provenance sources", "Audit"),
            ("Decision Receipt", "Immutable permanent record of ancestral decisions", "Audit"),
            ("Hydrological Buffering", "Water resource resilience architecture", "Resilience"),
            ("Survival Invariant", "What must hold for civilizational survival", "Invariant"),
            ("Civilizational Shock", "Large-scale disruption to civilizational continuity", "Risk"),
            ("Ancestral Wisdom", "Accumulated decision intelligence across generations", "Knowledge"),
        ],
    },
    "ALIASES.md": {
        "title": "Aliases",
        "id": "aliases",
        "tags_extra": ["aliases", "naming", "glossary"],
        "intro": "The Aliases registry defines alternative names for canonical AMOS terms, ensuring that searches and references using different terminology resolve to the correct canonical entity.",
        "terms": [
            ("AMOS OS", "→ AMOS (Autonomous Multi-Operational System)", "Alias"),
            ("Full Brain OS", "→ AMOS Brain Master OS", "Alias"),
            ("Super Mind OS", "→ AMOS Engines Master", "Alias"),
            ("Omega Infinity Stack", "→ Omega Quantum Stack", "Alias"),
            ("Rule of Two", "→ Rule of 2 (R2)", "Alias"),
            ("Rule of Four", "→ Rule of 4 (R4)", "Alias"),
            ("Trang Tát 2", "→ Rule of 2 (R2)", "Alias"),
            ("Khung Trang", "→ Trang Architecture / Trang Framework", "Alias"),
            ("Phương Pháp Trang", "→ Trang Method", "Alias"),
            ("Kien Truc Trang", "→ Trang Architecture", "Alias"),
            ("Bio-Logic", "→ Bio-Logical Architecture", "Alias"),
            ("Cognitive Vault", "→ AMOS OS Obsidian Vault", "Alias"),
            ("Cosmo Brain", "→ _00_Cosmo brain vault", "Alias"),
            ("MURK", "→ Absolute Logic Kernel (19 primitives)", "Alias"),
            ("Go Board", "→ 19×19 formal reasoning board", "Alias"),
        ],
    },
    "CROSS_FRAMEWORK_ALIAS_TABLE.md": {
        "title": "Cross-Framework Alias Table",
        "id": "cross_framework_alias_table",
        "tags_extra": ["aliases", "crosswalk", "framework", "glossary"],
        "intro": "The Cross-Framework Alias Table maps equivalent terms across different AMOS frameworks, ensuring consistent reference when concepts appear under different names in different canons.",
        "terms": [
            ("Coherence", "Omega: Ω | UBI: — | Trang: — | RSCF: confidence_ceiling", "Crosswalk"),
            ("Entropy", "Omega: H | UBI: — | Trang: H operator | RSCF: —", "Crosswalk"),
            ("Stability", "Omega: S | UBI: SI score | Trang: — | RSCF: scope", "Crosswalk"),
            ("Reserves", "Omega: R | UBI: — | Trang: R (Relation) | RSCF: —", "Crosswalk"),
            ("Force", "Omega: F | UBI: — | Trang: — | RSCF: —", "Crosswalk"),
            ("Distinction", "Omega: — | UBI: — | Trang: D | RSCF: —", "Crosswalk"),
            ("Memory", "Omega: — | UBI: — | Trang: M | RSCF: provenance", "Crosswalk"),
            ("Repair", "Omega: recovery | UBI: — | Trang: Repair | RSCF: —", "Crosswalk"),
            ("Recursion", "Omega: cascade | UBI: fractal | Trang: Recursion | RSCF: —", "Crosswalk"),
            ("Selection", "Omega: — | UBI: — | Trang: Selection | RSCF: —", "Crosswalk"),
            ("Collapse", "Omega: P_collapse | UBI: τ<0.2 | Trang: Cascade | RSCF: UNKNOWN/GAP", "Crosswalk"),
            ("Emergence", "Omega: — | UBI: e=i² | Trang: — | RSCF: —", "Crosswalk"),
        ],
    },
}

TEMPLATE = '''---
title: {title}
type: glossary
source: 01_CANON/06_GLOSSARY
artifact: {filename}
artifact_id: amos_01_canon_06_glossary_{id}
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 01_CANON
segment: 01_CANON/06_GLOSSARY
artifact_kind: GLOSSARY
path: 01_CANON/06_GLOSSARY/{filename}
tags:
  - amos-os
  - canon
  - glossary
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

`{filename}` defines the proposed AMOS OS **{title_short}** glossary.

This artifact replaces a structural placeholder with substantive content.

```text
PLACEHOLDER != IMPLEMENTED
ADDRESSABLE != VALIDATED
DOCUMENTED != ENFORCED
MODEL != OBSERVATION
SOURCE_CLAIM != VERIFIED
CANON_CANDIDATE != CANONICAL
CANONICAL != EMPIRICAL_TRUTH
CAPABILITY != AUTHORITY
UNKNOWN/GAP != PASS
```

Origin architect / steward: **Trang Phan**

______________________________________________________________________

## 1. Purpose

{intro}

______________________________________________________________________

## 2. Term Definitions

| Term | Definition | Category |
|:---|:---|:---|
{term_table}

______________________________________________________________________

## 3. Usage Notes

- All terms in this glossary are AMOS_MODEL unless otherwise stated
- Terms marked as "Core" are foundational to the framework
- Terms marked as "Alias" are alternative names for canonical terms
- Terms marked as "Crosswalk" map concepts across different canons
- No term in this glossary should be interpreted as empirical truth

______________________________________________________________________

## 4. Cross-References

- See [[01_CANON/06_GLOSSARY/CANONICAL_GLOSSARY|CANONICAL_GLOSSARY]] for the master glossary
- See [[01_CANON/06_GLOSSARY/CANON_ALIASES|CANON_ALIASES]] for canonical aliases
- See [[01_CANON/06_GLOSSARY/DEPRECATED_TERMS|DEPRECATED_TERMS]] for deprecated terminology
- See [[01_CANON/05_VARIABLE_REGISTRY/UNIVERSAL_VARIABLE_REGISTRY|UNIVERSAL_VARIABLE_REGISTRY]] for variable definitions

______________________________________________________________________

## 5. Gaps

- Canonical status CONDITIONAL — proposed specification, not yet promoted to full canon
- Cross-glossary consistency validation NOT_ESTABLISHED
- Automated term resolution NOT_ESTABLISHED

______________________________________________________________________

## 6. Ingestion Rule

```yaml
AMOS_CANON_INGESTION_RULE:
  existing_folder:
    preserve: true
  existing_file:
    preserve: true
    overwrite: false
  new_framework:
    action: ADD_FILE_TO_EXISTING_FOLDER
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

node_id: amos_01_canon_06_glossary_{id}

node_type: glossary

path: 01_CANON/06_GLOSSARY/{filename}

claim_class: AMOS_MODEL

rscf_state: DERIVED

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

______________________________________________________________________

**MOC:** [[01_CANON/06_GLOSSARY/06_GLOSSARY_MOC|06_GLOSSARY_MOC]]
'''


def expand_file(filepath, content_def):
    filename = os.path.basename(filepath)
    title = content_def["title"]
    title_short = title.replace(" Glossary", "").replace(" Aliases", "").replace(" Table", "")

    tags_extra = ""
    if "tags_extra" in content_def:
        tags_extra = "\n  - " + "\n  - ".join(content_def["tags_extra"])

    term_table = ""
    for term in content_def["terms"]:
        name, defn, cat = term
        term_table += f"| {name} | {defn} | {cat} |\n"

    content = TEMPLATE.format(
        title=title,
        title_short=title_short,
        filename=filename,
        id=content_def["id"],
        tags_extra=tags_extra,
        intro=content_def["intro"],
        term_table=term_table.rstrip(),
    )

    with open(filepath, "w") as f:
        f.write(content)
    return len(content)


def main():
    expanded = 0
    for filename, content_def in GLOSSARIES.items():
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
