#!/usr/bin/env python3
"""Add-only canon placeholder generator v2 — second batch.

Adds the expanded framework-depth placeholder files from the second ingestion
request. Reuses the v1 content builder for identical placeholder format.

Rules (unchanged):
  - existing_file   : PRESERVE, NEVER overwrite (skip silently)
  - new_file        : write typed, plane-aware placeholder content
  - duplicate_check : skip if file already exists, report as SKIPPED_PRESERVE

All new files carry status: PLACEHOLDER · canonical_status: UNKNOWN/GAP ·
implementation_status: NOT_ESTABLISHED · executable_binding: NOT_ESTABLISHED.
PLACEHOLDER != IMPLEMENTED.
"""
import os
import sys
import importlib.util
from datetime import date

ROOT = str(__import__("pathlib").Path(__file__).resolve().parents[1])
TODAY = date.today().isoformat()

# Reuse v1 builder
_spec = importlib.util.spec_from_file_location(
    "v1", os.path.join(ROOT, "scripts", "add_canon_placeholders_v1.py")
)
v1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(v1)

build_content = v1.build_content
node_id = v1.node_id
artifact_kind = v1.artifact_kind

# ---------------------------------------------------------------------------
# Second-batch manifest: (relative_path, framework_family, claim_class)
# ---------------------------------------------------------------------------
FILES = [
    # 00_ROOT — expanded registries, graphs, binding maps
    ("00_ROOT/AMOS_TOTAL_ARCHITECTURE.md", "AMOS Total Architecture", "AMOS_MODEL"),
    ("00_ROOT/AMOS_TOTAL_FRAMEWORK_REGISTRY.md", "AMOS Total Framework Registry", "AMOS_MODEL"),
    ("00_ROOT/AMOS_TOTAL_ENGINE_REGISTRY.md", "AMOS Total Engine Registry", "AMOS_MODEL"),
    ("00_ROOT/AMOS_TOTAL_KERNEL_REGISTRY.md", "AMOS Total Kernel Registry", "AMOS_MODEL"),
    ("00_ROOT/AMOS_TOTAL_OS_REGISTRY.md", "AMOS Total OS Registry", "AMOS_MODEL"),
    ("00_ROOT/AMOS_TOTAL_PROTOCOL_REGISTRY.md", "AMOS Total Protocol Registry", "AMOS_MODEL"),
    ("00_ROOT/AMOS_TOTAL_DOMAIN_REGISTRY.md", "AMOS Total Domain Registry", "AMOS_MODEL"),
    ("00_ROOT/AMOS_TOTAL_HERITAGE_REGISTRY.md", "AMOS Total Heritage Registry", "AMOS_MODEL"),
    ("00_ROOT/AMOS_TOTAL_UBI_REGISTRY.md", "AMOS Total UBI Registry", "AMOS_MODEL"),
    ("00_ROOT/AMOS_TOTAL_UNIVERSE_REGISTRY.md", "AMOS Total Universe Registry", "AMOS_MODEL"),
    ("00_ROOT/AMOS_TOTAL_TRANG_REGISTRY.md", "AMOS Total Trang Registry", "AMOS_MODEL"),
    ("00_ROOT/AMOS_TOTAL_RELATION_GRAPH.md", "AMOS Total Relation Graph", "AMOS_MODEL"),
    ("00_ROOT/AMOS_TOTAL_DEPENDENCY_GRAPH.md", "AMOS Total Dependency Graph", "AMOS_MODEL"),
    ("00_ROOT/AMOS_TOTAL_LINEAGE_GRAPH.md", "AMOS Total Lineage Graph", "AMOS_MODEL"),
    ("00_ROOT/AMOS_TOTAL_PROVENANCE_GRAPH.md", "AMOS Total Provenance Graph", "AMOS_MODEL"),
    ("00_ROOT/AMOS_TOTAL_SUPERSESSION_GRAPH.md", "AMOS Total Supersession Graph", "AMOS_MODEL"),
    ("00_ROOT/AMOS_TOTAL_CROSSWALK.md", "AMOS Total Crosswalk", "AMOS_MODEL"),
    ("00_ROOT/AMOS_CANON_RUNTIME_BINDING_MAP.md", "AMOS Canon-Runtime Binding Map", "AMOS_MODEL"),
    ("00_ROOT/AMOS_CANON_KNOWLEDGE_BINDING_MAP.md", "AMOS Canon-Knowledge Binding Map", "AMOS_MODEL"),
    ("00_ROOT/AMOS_CANON_DOMAIN_BINDING_MAP.md", "AMOS Canon-Domain Binding Map", "AMOS_MODEL"),
    ("00_ROOT/AMOS_NATIVE_CANON_VS_EXTERNAL_EVIDENCE.md", "AMOS Native Canon vs External Evidence", "AMOS_MODEL"),
    ("00_ROOT/AMOS_ORPHAN_FRAMEWORK_REGISTRY.md", "AMOS Orphan Framework Registry", "AMOS_MODEL"),
    ("00_ROOT/AMOS_MISSING_CANON_REGISTRY.md", "AMOS Missing Canon Registry", "AMOS_MODEL"),
    ("00_ROOT/AMOS_CANON_COMPLETENESS_STATUS.md", "AMOS Canon Completeness Status", "AMOS_MODEL"),
    ("00_ROOT/COSMO_BRAIN_AMOS_OS_MASTER_BINDING.md", "Cosmo Brain AMOS OS Master Binding", "AMOS_MODEL"),

    # 01_CANON/00_INDEX — expanded registries
    ("01_CANON/00_INDEX/CANON_MASTER_INDEX.md", "Canon Master Index", "AMOS_MODEL"),
    ("01_CANON/00_INDEX/CANON_FRAMEWORK_REGISTRY.md", "Canon Framework Registry", "AMOS_MODEL"),
    ("01_CANON/00_INDEX/CANON_ENGINE_REGISTRY.md", "Canon Engine Registry", "AMOS_MODEL"),
    ("01_CANON/00_INDEX/CANON_KERNEL_REGISTRY.md", "Canon Kernel Registry", "AMOS_MODEL"),
    ("01_CANON/00_INDEX/CANON_OS_REGISTRY.md", "Canon OS Registry", "AMOS_MODEL"),
    ("01_CANON/00_INDEX/CANON_PROTOCOL_REGISTRY.md", "Canon Protocol Registry", "AMOS_MODEL"),
    ("01_CANON/00_INDEX/CANON_DOMAIN_REGISTRY.md", "Canon Domain Registry", "AMOS_MODEL"),
    ("01_CANON/00_INDEX/CANON_ALIAS_REGISTRY.md", "Canon Alias Registry", "AMOS_MODEL"),
    ("01_CANON/00_INDEX/CANON_LINEAGE_REGISTRY.md", "Canon Lineage Registry", "AMOS_MODEL"),
    ("01_CANON/00_INDEX/CANON_PROVENANCE_REGISTRY.md", "Canon Provenance Registry", "AMOS_MODEL"),
    ("01_CANON/00_INDEX/CANON_SOURCE_REGISTRY.md", "Canon Source Registry", "AMOS_MODEL"),
    ("01_CANON/00_INDEX/CANON_STATUS_REGISTRY.md", "Canon Status Registry", "AMOS_MODEL"),
    ("01_CANON/00_INDEX/CANON_SUPERSESSION_REGISTRY.md", "Canon Supersession Registry", "AMOS_MODEL"),
    ("01_CANON/00_INDEX/CANON_COMPETING_DEFINITIONS.md", "Canon Competing Definitions", "AMOS_MODEL"),

    # 01_CANON/01_CORE_LAWS — expanded law families
    ("01_CANON/01_CORE_LAWS/META_LAWS_CANON.md", "Meta-Laws Canon", "AMOS_MODEL"),
    ("01_CANON/01_CORE_LAWS/STRUCTURAL_INTEGRITY_CANON.md", "Structural Integrity Canon", "AMOS_MODEL"),
    ("01_CANON/01_CORE_LAWS/EPISTEMIC_INTEGRITY_CANON.md", "Epistemic Integrity Canon", "AMOS_MODEL"),
    ("01_CANON/01_CORE_LAWS/CAUSAL_INTEGRITY_CANON.md", "Causal Integrity Canon", "AMOS_MODEL"),
    ("01_CANON/01_CORE_LAWS/PROVENANCE_INTEGRITY_CANON.md", "Provenance Integrity Canon", "AMOS_MODEL"),
    ("01_CANON/01_CORE_LAWS/LOAD_CAPACITY_CANON.md", "Load Capacity Canon", "AMOS_MODEL"),
    ("01_CANON/01_CORE_LAWS/FEEDBACK_CANON.md", "Feedback Canon", "AMOS_MODEL"),
    ("01_CANON/01_CORE_LAWS/DIFFERENCE_RELATION_BOUNDARY_CANON.md", "Difference-Relation-Boundary Canon", "AMOS_MODEL"),
    ("01_CANON/01_CORE_LAWS/COLLAPSE_CANON.md", "Collapse Canon", "AMOS_MODEL"),
    ("01_CANON/01_CORE_LAWS/RECOVERY_CANON.md", "Recovery Canon", "AMOS_MODEL"),
    ("01_CANON/01_CORE_LAWS/EMERGENCE_CANON.md", "Emergence Canon", "AMOS_MODEL"),
    ("01_CANON/01_CORE_LAWS/STABILITY_CANON.md", "Stability Canon", "AMOS_MODEL"),
    ("01_CANON/01_CORE_LAWS/CORE_LAW_CROSSWALK.md", "Core Law Crosswalk", "AMOS_MODEL"),

    # 01_CANON/02_UNIVERSE_CANON — deeper canonical sources (P1-P7 already exist, not duplicated)
    ("01_CANON/02_UNIVERSE_CANON/ABSOLUTE_OMNIVERSE_U_INFINITY.md", "Absolute Omniverse / U-Infinity", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/UNIVERSE_LOGIC_KERNEL.md", "Universe Logic Kernel", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/UNIVERSAL_FIELD_ARCHITECTURE.md", "Universal Field Architecture", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/TRANG_REALITY_ARCHITECTURE.md", "TRANG Reality Architecture", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/TRANG_ZERO_FRAMEWORK.md", "TRANG Zero Framework", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/KHUNG_TRANG_MASTER.md", "Khung Trang Master", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/KHUNG_TRANG_EQUATIONS.md", "Khung Trang Equations", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/UNIVERSE_STRUCTURE_TREE.md", "Universe Structure Tree", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/UNIVERSE_INTERACTION_ENGINE.md", "Universe Interaction Engine", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/UNIVERSE_BEHAVIOUR_ENGINE.md", "Universe Behaviour Engine", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/UNIVERSE_CAUSALITY_ARCHITECTURE.md", "Universe Causality Architecture", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/UNIVERSE_IDENTITY_ARCHITECTURE.md", "Universe Identity Architecture", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/UNIVERSE_INFORMATION_ARCHITECTURE.md", "Universe Information Architecture", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/UNIVERSE_BOUNDARY_ARCHITECTURE.md", "Universe Boundary Architecture", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/UNIVERSE_TIME_ARCHITECTURE.md", "Universe Time Architecture", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/UNIVERSE_TOPOLOGY_ARCHITECTURE.md", "Universe Topology Architecture", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/UNIVERSE_EMERGENCE_ARCHITECTURE.md", "Universe Emergence Architecture", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/UNIVERSE_COLLAPSE_ARCHITECTURE.md", "Universe Collapse Architecture", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/UNIVERSE_RECOVERY_ARCHITECTURE.md", "Universe Recovery Architecture", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/OMEGA_MASTER_CANON.md", "Omega Master Canon", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/OMEGA_QUANTUM_STACK.md", "Omega Quantum Stack", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/UNIVERSAL_OPERATORS.md", "Universal Operators", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/UNIVERSAL_PATTERN_FAMILIES.md", "Universal Pattern Families", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/UNIVERSE_EQUATION_REGISTRY.md", "Universe Equation Registry", "AMOS_MODEL"),

    # 01_CANON/03_COGNITION_CANON — individual cognitive architecture files
    ("01_CANON/03_COGNITION_CANON/AMOS_FULL_BRAIN_OS_CANON.md", "AMOS Full Brain OS Canon", "AMOS_MODEL"),
    ("01_CANON/03_COGNITION_CANON/AMOS_COGNITION_CANON.md", "AMOS Cognition Canon", "AMOS_MODEL"),
    ("01_CANON/03_COGNITION_CANON/AMOS_EMOTION_CANON.md", "AMOS Emotion Canon", "AMOS_MODEL"),
    ("01_CANON/03_COGNITION_CANON/AMOS_ATTENTION_CANON.md", "AMOS Attention Canon", "AMOS_MODEL"),
    ("01_CANON/03_COGNITION_CANON/AMOS_PERCEPTION_CANON.md", "AMOS Perception Canon", "AMOS_MODEL"),
    ("01_CANON/03_COGNITION_CANON/AMOS_19X19_COGNITIVE_FIELD.md", "AMOS 19x19 Cognitive Field", "AMOS_MODEL"),
    ("01_CANON/03_COGNITION_CANON/AMOS_CROSS_SPECIES_FUNCTIONAL_MODE_MODEL.md", "AMOS Cross-Species Functional Mode Model", "AMOS_MODEL"),
    ("01_CANON/03_COGNITION_CANON/COGNITIVE_CANON_RELATION_MAP.md", "Cognitive Canon Relation Map", "AMOS_MODEL"),

    # 01_CANON/04_INFRASTRUCTURE_CANON — expanded infrastructure canon
    ("01_CANON/04_INFRASTRUCTURE_CANON/CANON_INTEGRATION_LAYER.md", "Canon Integration Layer", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/CAUSAL_EPOCH_FINALITY_CANON.md", "Causal Epoch Finality Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/HARDENED_SHARD_FINALIZATION_CANON.md", "Hardened Shard Finalization Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/PROOF_BASED_COORDINATION_AVOIDANCE.md", "Proof-Based Coordination Avoidance", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/PROVENANCE_TOPOLOGY_CANON.md", "Provenance Topology Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/SYBIL_HARDENING_CANON.md", "Sybil Hardening Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/COMPETING_HYPOTHESES_CANON.md", "Competing Hypotheses Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/EPISTEMIC_REGIME_CANON.md", "Epistemic Regime Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/CAUSAL_LINEAGE_CANON.md", "Causal Lineage Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/DOMAIN_CANON_PROGRAMMING.md", "Domain Canon Programming", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/AMOS_INFRASTRUCTURE_ARCHITECTURE.md", "AMOS Infrastructure Architecture", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/AMOS_ORCHESTRATION_REGULATOR_CANON.md", "AMOS Orchestration Regulator Canon", "AMOS_MODEL"),

    # 01_CANON/07_PROVENANCE — expanded provenance infrastructure
    ("01_CANON/07_PROVENANCE/ORIGIN_ARCHITECT_REGISTRY.md", "Origin Architect Registry", "AMOS_MODEL"),
    ("01_CANON/07_PROVENANCE/ORIGINAL_SOURCE_REGISTRY.md", "Original Source Registry", "AMOS_MODEL"),
    ("01_CANON/07_PROVENANCE/NATIVE_CANON_SOURCE_REGISTRY.md", "Native Canon Source Registry", "AMOS_MODEL"),
    ("01_CANON/07_PROVENANCE/DERIVED_CANON_SOURCE_REGISTRY.md", "Derived Canon Source Registry", "AMOS_MODEL"),
    ("01_CANON/07_PROVENANCE/HERITAGE_SOURCE_REGISTRY.md", "Heritage Source Registry", "AMOS_MODEL"),
    ("01_CANON/07_PROVENANCE/FRAMEWORK_ANCESTRY_GRAPH.md", "Framework Ancestry Graph", "AMOS_MODEL"),
    ("01_CANON/07_PROVENANCE/PROVENANCE_ROOT_REGISTRY.md", "Provenance Root Registry", "AMOS_MODEL"),
    ("01_CANON/07_PROVENANCE/FILE_HASH_REGISTRY.md", "File Hash Registry", "AMOS_MODEL"),
    ("01_CANON/07_PROVENANCE/CANON_HASH_REGISTRY.md", "Canon Hash Registry", "AMOS_MODEL"),
    ("01_CANON/07_PROVENANCE/VERSION_HASH_REGISTRY.md", "Version Hash Registry", "AMOS_MODEL"),
    ("01_CANON/07_PROVENANCE/IP_OWNERSHIP_REGISTRY.md", "IP Ownership Registry", "AMOS_MODEL"),
    ("01_CANON/07_PROVENANCE/LICENSE_REGISTRY.md", "License Registry", "AMOS_MODEL"),
    ("01_CANON/07_PROVENANCE/SOURCE_TO_CANON_MAP.md", "Source-to-Canon Map", "AMOS_MODEL"),
    ("01_CANON/07_PROVENANCE/CANON_TO_SOURCE_MAP.md", "Canon-to-Source Map", "AMOS_MODEL"),

    # 05_COGNITIVE_ORGANISM — engine and binding files at organism root
    ("05_COGNITIVE_ORGANISM/FULL_BRAIN_OS_RUNTIME_BINDING.md", "Full Brain OS Runtime Binding", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/COGNITION_ENGINE.md", "Cognition Engine", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/EMOTION_ENGINE.md", "Emotion Engine", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/HUMAN_INTELLIGENCE_ENGINE.md", "Human Intelligence Engine", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/SUPER_MIND_ENGINE.md", "Super Mind Engine", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/SUPER_CONSCIOUSNESS_ENGINE.md", "Super Consciousness Engine", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/IDENTITY_ENGINE.md", "Identity Engine", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/MEMORY_ENGINE.md", "Memory Engine", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/PERCEPTION_ENGINE.md", "Perception Engine", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/ATTENTION_ENGINE.md", "Attention Engine", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/PREDICTION_ENGINE.md", "Prediction Engine", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/INTUITION_ENGINE.md", "Intuition Engine", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/INSTINCT_ENGINE.md", "Instinct Engine", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/METACOGNITIVE_ENGINE.md", "Metacognitive Engine", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/WORLD_MODEL_ENGINE.md", "World Model Engine", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/HOMEOSTASIS_ENGINE.md", "Homeostasis Engine", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/REPAIR_ENGINE.md", "Repair Engine", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/UBI_ORGANISM_BINDING.md", "UBI Organism Binding", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/NBI_ORGANISM_BINDING.md", "NBI Organism Binding", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/NEI_ORGANISM_BINDING.md", "NEI Organism Binding", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/SI_ORGANISM_BINDING.md", "SI Organism Binding", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/BEI_ORGANISM_BINDING.md", "BEI Organism Binding", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/NEUROSYNCAI_ORGANISM_BINDING.md", "NeuroSyncAI Organism Binding", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/CROSS_SPECIES_MODE_ENGINE.md", "Cross-Species Mode Engine", "AMOS_MODEL"),

    # 11_KNOWLEDGE/05_FRAMEWORKS — Heritage family
    ("11_KNOWLEDGE/05_FRAMEWORKS/HERITAGE_INTELLIGENCE_MASTER.md", "Heritage Intelligence Master", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/HERITAGE_ZERO_FRAMEWORK.md", "Heritage Zero Framework", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/HERITAGE_PATTERN_INTELLIGENCE.md", "Heritage Pattern Intelligence", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/HERITAGE_FRACTAL_MATHEMATICS.md", "Heritage Fractal Mathematics", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/HERITAGE_SPATIAL_INTELLIGENCE.md", "Heritage Spatial Intelligence", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/HERITAGE_VIETNAMESE_HISTORY.md", "Heritage Vietnamese History", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/HERITAGE_CIVILIZATION_SYSTEM.md", "Heritage Civilization System", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/HERITAGE_MUSIC_ACOUSTIC_INTELLIGENCE.md", "Heritage Music/Acoustic Intelligence", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/HERITAGE_SYMBOLIC_SYSTEMS.md", "Heritage Symbolic Systems", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/HERITAGE_HANDBOOK.md", "Heritage Handbook", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/HERITAGE_TO_TRANG_ZERO_BINDING.md", "Heritage-to-Trang-Zero Binding", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/HERITAGE_TO_TSS_BINDING.md", "Heritage-to-TSS Binding", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/HERITAGE_TO_AMOS_BINDING.md", "Heritage-to-AMOS Binding", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/HERITAGE_LINEAGE.md", "Heritage Lineage", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/HERITAGE_PROVENANCE.md", "Heritage Provenance", "AMOS_MODEL"),

    # 11_KNOWLEDGE/05_FRAMEWORKS — UBI family
    ("11_KNOWLEDGE/05_FRAMEWORKS/UBI_MASTER.md", "UBI Master", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/UNIFIED_BIOLOGICAL_INTELLIGENCE.md", "Unified Biological Intelligence", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/UBI_OMNIS.md", "UBI OMNIS", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/UBI_SUPER.md", "UBI SUPER", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/AMOS_UBI_SUPER_ENGINE.md", "AMOS UBI SUPER Engine", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/NBI_NEUROBIOLOGICAL_INTELLIGENCE.md", "NBI Neurobiological Intelligence", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/NEI_NEUROEMOTIONAL_INTELLIGENCE.md", "NEI Neuroemotional Intelligence", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/SI_SOMATIC_INTELLIGENCE.md", "SI Somatic Intelligence", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/BEI_BIOELECTROMAGNETIC_INTELLIGENCE.md", "BEI Bioelectromagnetic Intelligence", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/UBI_HOMEOSTASIS.md", "UBI Homeostasis", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/UBI_ENTROPY_CORRECTION.md", "UBI Entropy Correction", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/UBI_FRACTAL_ARCHITECTURE.md", "UBI Fractal Architecture", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/UBI_BIOLOGICAL_PROGRAMMING.md", "UBI Biological Programming", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/UBI_ABSOLUTE_BIOLOGICAL_INTEGRITY.md", "UBI Absolute Biological Integrity", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/UBI_SCORE.md", "UBI Score", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/UBI_WEARABLE.md", "UBI Wearable", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/UBI_CROSS_SPECIES_FUNCTIONAL_MODES.md", "UBI Cross-Species Functional Modes", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/UBI_NEUROSYNCAI_BINDING.md", "UBI-NeuroSyncAI Binding", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/UBI_CONSENTX_BINDING.md", "UBI-ConsentX Binding", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/UBI_ID_EXCHANGE_BINDING.md", "UBI-ID-Exchange Binding", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/UBI_RATPAK_BINDING.md", "UBI-RatPAK Binding", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/UBI_COGNITION_BINDING.md", "UBI-Cognition Binding", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/UBI_EMOTION_BINDING.md", "UBI-Emotion Binding", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/UBI_FULL_BRAIN_BINDING.md", "UBI-Full-Brain Binding", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/UBI_LINEAGE.md", "UBI Lineage", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/UBI_PROVENANCE.md", "UBI Provenance", "AMOS_MODEL"),

    # 11_KNOWLEDGE/05_FRAMEWORKS — Trang system family
    ("11_KNOWLEDGE/05_FRAMEWORKS/PHUONG_PHAP_TRANG.md", "Phuong Phap Trang", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/TRANG_ZERO_FRAMEWORK.md", "TRANG Zero Framework", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/KHUNG_TRANG.md", "Khung Trang", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/TRANG_REALITY_ARCHITECTURE.md", "TRANG Reality Architecture", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/TRANG_GRAND_SYSTEM.md", "TRANG Grand System", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/TRANG_GRAND_SYSTEM_CODEX.md", "TRANG Grand System Codex", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/TRANG_GRAND_SYSTEM_LOGIC_SPECIFICATION.md", "TRANG Grand System Logic Specification", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/TSS_THE_TRANG_SYSTEM.md", "TSS — The Trang System", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/TSS_META_LAWS.md", "TSS Meta-Laws", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/TSS_SEVEN_CYCLES.md", "TSS Seven Cycles", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/TPE_TRANG_PREDICTION_ENGINE.md", "TPE — Trang Prediction Engine", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/TSS_TPE_INTEGRATION.md", "TSS-TPE Integration", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/FPR_FIRST_PRINCIPLE_REASONING.md", "FPR — First-Principle Reasoning", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/FRAI_FRACTAL_REASONING_AI.md", "FRAI — Fractal Reasoning AI", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/LDAI_LOGICALLY_DETERMINISTIC_AI.md", "LDAI — Logically Deterministic AI", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/ASEA_ADAPTIVE_SELF_EVOLUTION_AI.md", "ASEA — Adaptive Self-Evolution AI", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/TRANG_CASCADE.md", "TRANG Cascade", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/TRANG_LACUNARITY.md", "TRANG Lacunarity", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/TRANG_LMH_ARCHITECTURE.md", "TRANG LMH Architecture", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/TRANG_EQUATION_REGISTRY.md", "TRANG Equation Registry", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/TRANG_FRAMEWORK_LINEAGE.md", "TRANG Framework Lineage", "AMOS_MODEL"),

    # 11_KNOWLEDGE/05_FRAMEWORKS — non-Trang/non-UBI families
    ("11_KNOWLEDGE/05_FRAMEWORKS/NEUROSYNCAI_MASTER.md", "NeuroSyncAI Master", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/NEUROSYNCAI_DUAL_SYSTEM_ARCHITECTURE.md", "NeuroSyncAI Dual-System Architecture", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/NEUROSYNCAI_RECOVERY_ENGINE.md", "NeuroSyncAI Recovery Engine", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/CONSENTX.md", "ConsentX", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/ID_EXCHANGE.md", "ID Exchange", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/RATPAK.md", "RatPAK", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/PSI_MASTER.md", "PSI Master", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/QLS_MASTER.md", "QLS Master", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/QCLA_MASTER.md", "QCLA Master", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/UBA_UNIVERSAL_BIOLOGICAL_ARCHITECTURE.md", "UBA — Universal Biological Architecture", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/BIO_LOGICAL_COMPUTING.md", "Bio-Logical Computing", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/BIO_LOGICAL_ARCHITECTURE.md", "Bio-Logical Architecture", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/DOMAIN_CANON_PROGRAMMING.md", "Domain Canon Programming", "AMOS_MODEL"),

    # 25_COGNITIVE_MATRIX — expanded cross-system matrices
    ("25_COGNITIVE_MATRIX/TOTAL_CANON_MATRIX.md", "Total Canon Matrix", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/TOTAL_FRAMEWORK_MATRIX.md", "Total Framework Matrix", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/TOTAL_ENGINE_MATRIX.md", "Total Engine Matrix", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/TOTAL_KERNEL_MATRIX.md", "Total Kernel Matrix", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/AMOS_X_TRANG_REALITY.md", "AMOS × TRANG Reality", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/AMOS_X_HERITAGE.md", "AMOS × Heritage", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/AMOS_X_UBI.md", "AMOS × UBI", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/AMOS_X_NEUROSYNCAI.md", "AMOS × NeuroSyncAI", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/AMOS_X_UNIVERSE_CANON.md", "AMOS × Universe Canon", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/AMOS_X_OMEGA.md", "AMOS × Omega", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/AMOS_X_QLS.md", "AMOS × QLS", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/AMOS_X_QCLA.md", "AMOS × QCLA", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/AMOS_X_TSS.md", "AMOS × TSS", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/AMOS_X_TPE.md", "AMOS × TPE", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/UBI_X_COGNITION.md", "UBI × Cognition", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/UBI_X_EMOTION.md", "UBI × Emotion", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/UBI_X_FULL_BRAIN.md", "UBI × Full Brain", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/UBI_X_NEUROSYNCAI.md", "UBI × NeuroSyncAI", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/HERITAGE_X_TRANG_ZERO.md", "Heritage × Trang Zero", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/HERITAGE_X_TSS.md", "Heritage × TSS", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/REALITY_X_ULK.md", "Reality × ULK", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/ULK_X_RSCF.md", "ULK × RSCF", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/RSCF_X_GMEF.md", "RSCF × GMEF", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/CORE_X_RUNTIME.md", "Core × Runtime", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/CORE_X_CONTROL_PLANE.md", "Core × Control Plane", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/CANON_X_KNOWLEDGE.md", "Canon × Knowledge", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/CANON_X_DOMAINS.md", "Canon × Domains", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/PROVENANCE_X_CONFIDENCE.md", "Provenance × Confidence", "AMOS_MODEL"),
]


def main():
    created = 0
    skipped = 0
    dirs_made = []
    created_files = []
    skipped_files = []
    errors = []

    for relpath, subject, claim_class in FILES:
        abspath = os.path.join(ROOT, relpath)
        if os.path.exists(abspath):
            skipped += 1
            skipped_files.append(relpath)
            continue
        d = os.path.dirname(abspath)
        if not os.path.isdir(d):
            os.makedirs(d, exist_ok=True)
            dirs_made.append(os.path.dirname(relpath))
        try:
            content = build_content(relpath, subject, claim_class)
            with open(abspath, "w", encoding="utf-8") as f:
                f.write(content)
            created += 1
            created_files.append(relpath)
        except Exception as e:
            errors.append((relpath, str(e)))

    print(f"PASS2_TOTAL_MANIFEST_ENTRIES: {len(FILES)}")
    print(f"PASS2_CREATED: {created}")
    print(f"PASS2_SKIPPED_PRESERVE: {skipped}")
    print(f"PASS2_DIRS_MADE: {len(dirs_made)}")
    print(f"PASS2_ERRORS: {len(errors)}")
    if dirs_made:
        print("\n--- directories created ---")
        for d in dirs_made:
            print(f"  {d}")
    if skipped_files:
        print(f"\n--- skipped (already exist, preserved) [{len(skipped_files)}] ---")
        for s in skipped_files:
            print(f"  {s}")
    if errors:
        print("\n--- errors ---")
        for rp, err in errors:
            print(f"  {rp}: {err}")

    report_dir = os.path.join(ROOT, "scripts", "_add_canon_report")
    os.makedirs(report_dir, exist_ok=True)
    with open(os.path.join(report_dir, "pass2_created.txt"), "w") as f:
        f.write("\n".join(created_files))
    with open(os.path.join(report_dir, "pass2_skipped.txt"), "w") as f:
        f.write("\n".join(skipped_files))
    with open(os.path.join(report_dir, "pass2_dirs_made.txt"), "w") as f:
        f.write("\n".join(dirs_made))
    print(f"\nReports written to {report_dir}/pass2_*")


if __name__ == "__main__":
    main()
