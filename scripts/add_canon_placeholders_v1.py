#!/usr/bin/env python3
"""Add-only canon placeholder generator v1.

Creates the ADD-ONLY canon/registry/framework .md files specified in the
AMOS_OS_ADD_ONLY_CANON_FILE_MANIFEST into the EXISTING folder structure.

Rules (per AMOS_CANON_INGESTION_RULE):
  - existing_folder : preserve (only mkdir missing subfolders needed by new files)
  - existing_file   : preserve, NEVER overwrite
  - new_file        : write typed, plane-aware placeholder content
  - duplicate_check : skip if file already exists, report as SKIPPED_PRESERVE

Placeholder content follows the established fill_placeholder_contracts_v2.py
conventions: YAML frontmatter + Purpose + governing boundaries + contract
discipline + gaps + promotion-gate checklist + RSCF-NODE footer.

Epistemic class stays AMOS_MODEL; canonical_status UNKNOWN/GAP; executable
binding NOT_ESTABLISHED unless a receipt exists. These are PLACEHOLDERS, not
canon — PLACEHOLDER != IMPLEMENTED.
"""
import os
import sys
from datetime import date

ROOT = "/Users/mac/Documents/AMOS_OS"
TODAY = date.today().isoformat()

# ---------------------------------------------------------------------------
# Plane metadata (top-level folder -> (plane_name, plane_description))
# ---------------------------------------------------------------------------
PLANES = {
    "00_ROOT": ("Root", "vault-wide identity, architecture map, authoritative state pointers, and release governance"),
    "01_CANON": ("Canon", "canonical laws, universe/cognition/infrastructure canons, variable registry, glossary, provenance lineage, and supersession"),
    "02_KERNEL": ("Kernel", "kernel-plane reasoning primitives: meta-logic, cognition, causality, state, memory, risk-repair, authority, provenance, integration"),
    "03_CONTROL_PLANE": ("Control Plane", "governance surfaces that gate effects: task contracts, capability, policy, authority, provenance, semantic transactions, observability, effects, commit, exposure, replay, rollback"),
    "04_RUNTIME": ("Runtime", "execution substrate binding kernel contracts to runnable operators under v4.4 runtime rules"),
    "05_COGNITIVE_ORGANISM": ("Cognitive Organism", "the organism-level cognitive assembly above kernels and below agents"),
    "06_AGENTS": ("Agents", "agent specifications, capability envelopes, and delegation boundaries"),
    "07_SKILLS": ("Skills", "host skill packages exposing workflows; deployment infrastructure, never truth authorities"),
    "08_WORKFLOWS": ("Workflows", "multi-step orchestration definitions with typed stages and rollback basins"),
    "09_PROTOCOLS": ("Protocols", "inter-component communication and handshake protocols"),
    "10_MEMORY": ("Memory", "durable memory stores, trust classes, admission, retrieval, and conflict policy"),
    "11_KNOWLEDGE": ("Knowledge", "knowledge base integration: claims, RSCF indices, framework nodes, domain knowledge"),
    "12_STATE": ("State", "authoritative state records and state-versioned artifacts"),
    "13_MODELS": ("Models", "model registries and model-output vs observation firewalls"),
    "14_TOOLS": ("Tools", "tool bindings; tool availability is never permission"),
    "15_INTERFACES": ("Interfaces", "cross-boundary message schemas and interface contracts"),
    "16_SCHEMAS": ("Schemas", "typed artifact schemas and compatibility rules"),
    "17_OBSERVABILITY": ("Observability", "metrics, logs, traces, health signals — observations, never authority"),
    "18_SECURITY": ("Security", "threat surface, fail-closed gates, attestation, and secrets status"),
    "19_TESTS": ("Tests", "test taxonomy, coverage declarations, negative coverage, and receipts"),
    "20_OPERATIONS": ("Operations", "operational runbooks, recovery procedures, maintenance passes"),
    "21_DOMAINS": ("Domains", "C-family domain engine mappings (C01-C12) and domain canons onto the OS planes"),
    "22_RESEARCH": ("Research", "research questions, experiments, competing models, validation, benchmarks"),
    "23_OPERATING_MODEL": ("Operating Model", "roles, decision rights, governance forums, escalation paths, service levels"),
    "24_ARCHIVE": ("Archive", "superseded, deprecated, experimental, and legacy artifacts"),
    "25_COGNITIVE_MATRIX": ("Cognitive Matrix", "primitives L00-L29, lifecycle operations, control planes, scales, cell registry, routing, validation, generators"),
}

DISCIPLINE = ("Typed artifacts · provenance stamped · epistemic class declared · "
              "confidence ceiling · fail-closed on UNKNOWN/GAP · receipts for "
              "consequential effects · rollback basin before mutation.")

RECEIPTS = "[[ROUTING_POLICY_VALIDATION_RECEIPT]] · [[AUTHZ_ENGINE_VALIDATION_RECEIPT]]"

# ---------------------------------------------------------------------------
# Full ADD-ONLY file manifest: (relative_path, framework_family, claim_class)
# framework_family drives the "Subject" line; claim_class is AMOS_MODEL unless
# the artifact is explicitly a registry/index (still AMOS_MODEL · derived).
# ---------------------------------------------------------------------------
FILES = [
    # 00_ROOT
    ("00_ROOT/AMOS_TOTAL_CANON_INDEX.md", "AMOS Total Canon", "AMOS_MODEL"),
    ("00_ROOT/AMOS_ALL_FRAMEWORKS_INDEX.md", "AMOS All Frameworks", "AMOS_MODEL"),
    ("00_ROOT/AMOS_TOTAL_SYSTEM_LINEAGE.md", "AMOS Total System Lineage", "AMOS_MODEL"),
    ("00_ROOT/AMOS_CANON_TO_RUNTIME_MAP.md", "AMOS Canon-to-Runtime Map", "AMOS_MODEL"),
    ("00_ROOT/AMOS_FRAMEWORK_DEPENDENCY_MASTER.md", "AMOS Framework Dependency Master", "AMOS_MODEL"),
    ("00_ROOT/AMOS_FRAMEWORK_ALIAS_MASTER.md", "AMOS Framework Alias Master", "AMOS_MODEL"),
    ("00_ROOT/AMOS_FRAMEWORK_STATUS_MASTER.md", "AMOS Framework Status Master", "AMOS_MODEL"),
    ("00_ROOT/AMOS_FRAMEWORK_PLACEMENT_MASTER.md", "AMOS Framework Placement Master", "AMOS_MODEL"),
    ("00_ROOT/AMOS_ORIGIN_HERITAGE_MASTER.md", "AMOS Origin Heritage Master", "AMOS_MODEL"),
    ("00_ROOT/AMOS_NATIVE_VS_EXTERNAL_KNOWLEDGE.md", "AMOS Native vs External Knowledge", "AMOS_MODEL"),
    ("00_ROOT/COSMO_BRAIN_TO_AMOS_OS_BINDING.md", "Cosmo Brain to AMOS OS Binding", "AMOS_MODEL"),
    ("00_ROOT/TOTAL_CORPUS_COVERAGE.md", "Total Corpus Coverage", "AMOS_MODEL"),
    # 01_CANON/00_INDEX
    ("01_CANON/00_INDEX/AMOS_ALL_FRAMEWORKS_CANON_HIERARCHY.md", "AMOS All Frameworks Canon Hierarchy", "AMOS_MODEL"),
    ("01_CANON/00_INDEX/CANON_FAMILY_REGISTRY.md", "Canon Family Registry", "AMOS_MODEL"),
    ("01_CANON/00_INDEX/CANON_OBJECT_REGISTRY.md", "Canon Object Registry", "AMOS_MODEL"),
    ("01_CANON/00_INDEX/CANON_RELATION_REGISTRY.md", "Canon Relation Registry", "AMOS_MODEL"),
    ("01_CANON/00_INDEX/CANON_VERSION_REGISTRY.md", "Canon Version Registry", "AMOS_MODEL"),
    ("01_CANON/00_INDEX/CANON_HERITAGE_REGISTRY.md", "Canon Heritage Registry", "AMOS_MODEL"),
    ("01_CANON/00_INDEX/CANON_IP_REGISTRY.md", "Canon IP Registry", "AMOS_MODEL"),
    ("01_CANON/00_INDEX/CANON_TRADENAME_REGISTRY.md", "Canon Tradename Registry", "AMOS_MODEL"),
    ("01_CANON/00_INDEX/CANON_ACTIVE_LEGACY_MATRIX.md", "Canon Active vs Legacy Matrix", "AMOS_MODEL"),
    ("01_CANON/00_INDEX/CANON_SOURCE_COVERAGE.md", "Canon Source Coverage", "AMOS_MODEL"),
    ("01_CANON/00_INDEX/CANON_COMPLETENESS_AUDIT.md", "Canon Completeness Audit", "AMOS_MODEL"),
    # 01_CANON/01_CORE_LAWS
    ("01_CANON/01_CORE_LAWS/ABSOLUTE_LOGIC_CANON.md", "Absolute Logic Canon", "AMOS_MODEL"),
    ("01_CANON/01_CORE_LAWS/UNIVERSE_LOGIC_KERNEL_CANON.md", "Universe Logic Kernel Canon", "AMOS_MODEL"),
    ("01_CANON/01_CORE_LAWS/ABSOLUTE_INTEGRITY_CANON.md", "Absolute Integrity Canon", "AMOS_MODEL"),
    ("01_CANON/01_CORE_LAWS/ABSOLUTE_STRUCTURAL_INTEGRITY_CANON.md", "Absolute Structural Integrity Canon", "AMOS_MODEL"),
    ("01_CANON/01_CORE_LAWS/BIO_LOGICAL_LAWS_CANON.md", "Bio-Logical Laws Canon", "AMOS_MODEL"),
    ("01_CANON/01_CORE_LAWS/RULE_OF_2_CANON.md", "Rule of 2 Canon", "AMOS_MODEL"),
    ("01_CANON/01_CORE_LAWS/RULE_OF_4_CANON.md", "Rule of 4 Canon", "AMOS_MODEL"),
    ("01_CANON/01_CORE_LAWS/CORE19_CANON.md", "CORE-19 Canon", "AMOS_MODEL"),
    ("01_CANON/01_CORE_LAWS/LOAD_CAPACITY_FEEDBACK_CANON.md", "Load Capacity Feedback Canon", "AMOS_MODEL"),
    ("01_CANON/01_CORE_LAWS/COLLAPSE_RECOVERY_CANON.md", "Collapse Recovery Canon", "AMOS_MODEL"),
    ("01_CANON/01_CORE_LAWS/IDENTITY_CONTINUITY_CANON.md", "Identity Continuity Canon", "AMOS_MODEL"),
    ("01_CANON/01_CORE_LAWS/CANON_LAW_CROSSWALK.md", "Canon Law Crosswalk", "AMOS_MODEL"),
    # 01_CANON/02_UNIVERSE_CANON
    ("01_CANON/02_UNIVERSE_CANON/ABSOLUTE_OMNIVERSE_U_INFINITY_CANON.md", "Absolute Omniverse / U-Infinity Canon", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/UNIVERSE_TOTAL_CANON.md", "Universe Total Canon", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/SEVEN_PART_UNIVERSE_CANON_MASTER.md", "Seven-Part Universe Canon Master", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/SEVEN_PART_UNIVERSE_CANON_V2.md", "Seven-Part Universe Canon v2", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/UNIVERSAL_FIELD_ARCHITECTURE_CANON.md", "Universal Field Architecture Canon", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/UNIVERSE_STRUCTURE_TREE_CANON.md", "Universe Structure Tree Canon", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/UNIVERSE_INTERACTION_CANON.md", "Universe Interaction Canon", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/UNIVERSE_BEHAVIOUR_CANON.md", "Universe Behaviour Canon", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/OMEGA_ARCHITECTURE_CANON.md", "Omega Architecture Canon", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/OMEGA_QUANTUM_STACK_CANON.md", "Omega Quantum Stack Canon", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/QUANTUM_CAUSAL_ARCHITECTURE_CANON.md", "Quantum Causal Architecture Canon", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/QCLA_CANON.md", "QCLA Canon", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/QLS_CANON.md", "QLS Canon", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/URK_CANON.md", "URK Canon", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/ULK_CANON.md", "ULK Canon", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/REALITY_ARCHITECTURE_CANON.md", "Reality Architecture Canon", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/TRANG_ZERO_FRAMEWORK_CANON.md", "Trang Zero Framework Canon", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/KHUNG_TRANG_CANON.md", "Khung Trang Canon", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/KHUNG_TRANG_EQUATIONS_CANON.md", "Khung Trang Equations Canon", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/REALITY_FIELD_CAUSALITY_CANON.md", "Reality Field Causality Canon", "AMOS_MODEL"),
    ("01_CANON/02_UNIVERSE_CANON/UNIVERSE_CANON_LINEAGE.md", "Universe Canon Lineage", "AMOS_MODEL"),
    # 01_CANON/03_COGNITION_CANON
    ("01_CANON/03_COGNITION_CANON/AMOS_FULL_BRAIN_OS_MASTER_CANON.md", "AMOS Full Brain OS Master Canon", "AMOS_MODEL"),
    ("01_CANON/03_COGNITION_CANON/AMOS_SUPER_MIND_OS_CANON.md", "AMOS Super Mind OS Canon", "AMOS_MODEL"),
    ("01_CANON/03_COGNITION_CANON/AMOS_SUPER_CONSCIOUSNESS_CANON.md", "AMOS Super Consciousness Canon", "AMOS_MODEL"),
    ("01_CANON/03_COGNITION_CANON/AMOS_HUMAN_INTELLIGENCE_CANON.md", "AMOS Human Intelligence Canon", "AMOS_MODEL"),
    ("01_CANON/03_COGNITION_CANON/AMOS_COGNITION_MASTER_CANON.md", "AMOS Cognition Master Canon", "AMOS_MODEL"),
    ("01_CANON/03_COGNITION_CANON/AMOS_EMOTION_MASTER_CANON.md", "AMOS Emotion Master Canon", "AMOS_MODEL"),
    ("01_CANON/03_COGNITION_CANON/AMOS_PERSONALITY_CANON.md", "AMOS Personality Canon", "AMOS_MODEL"),
    ("01_CANON/03_COGNITION_CANON/AMOS_IDENTITY_CANON.md", "AMOS Identity Canon", "AMOS_MODEL"),
    ("01_CANON/03_COGNITION_CANON/AMOS_INSTINCT_CANON.md", "AMOS Instinct Canon", "AMOS_MODEL"),
    ("01_CANON/03_COGNITION_CANON/AMOS_INTUITION_CANON.md", "AMOS Intuition Canon", "AMOS_MODEL"),
    ("01_CANON/03_COGNITION_CANON/AMOS_CONSCIOUSNESS_CANON.md", "AMOS Consciousness Canon", "AMOS_MODEL"),
    ("01_CANON/03_COGNITION_CANON/AMOS_METACOGNITION_CANON.md", "AMOS Metacognition Canon", "AMOS_MODEL"),
    ("01_CANON/03_COGNITION_CANON/AMOS_MEMORY_CANON.md", "AMOS Memory Canon", "AMOS_MODEL"),
    ("01_CANON/03_COGNITION_CANON/AMOS_WORLD_MODEL_CANON.md", "AMOS World Model Canon", "AMOS_MODEL"),
    ("01_CANON/03_COGNITION_CANON/AMOS_PREDICTION_CANON.md", "AMOS Prediction Canon", "AMOS_MODEL"),
    ("01_CANON/03_COGNITION_CANON/AMOS_LEARNING_CANON.md", "AMOS Learning Canon", "AMOS_MODEL"),
    ("01_CANON/03_COGNITION_CANON/AMOS_AGENCY_CANON.md", "AMOS Agency Canon", "AMOS_MODEL"),
    ("01_CANON/03_COGNITION_CANON/AMOS_HOMEOSTASIS_CANON.md", "AMOS Homeostasis Canon", "AMOS_MODEL"),
    ("01_CANON/03_COGNITION_CANON/AMOS_COGNITIVE_FIELD_CANON.md", "AMOS Cognitive Field Canon", "AMOS_MODEL"),
    ("01_CANON/03_COGNITION_CANON/CROSS_SPECIES_FUNCTIONAL_MODE_CANON.md", "Cross-Species Functional Mode Canon", "AMOS_MODEL"),
    # 01_CANON/04_INFRASTRUCTURE_CANON
    ("01_CANON/04_INFRASTRUCTURE_CANON/AMOS_CORE_V3_TO_V4_4_LINEAGE.md", "AMOS Core v3 to v4.4 Lineage", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/AMOS_CORE_V4_4_CANON.md", "AMOS Core v4.4 Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/CANON_INTEGRATION_LAYER_CANON.md", "Canon Integration Layer Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/DOMAIN_CANON_PROGRAMMING_CANON.md", "Domain Canon Programming Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/UNIVERSAL_BIO_LOGICAL_ARCHITECTURE.md", "Universal Bio-Logical Architecture", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/BIO_LOGICAL_COMPUTING_CANON.md", "Bio-Logical Computing Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/BIO_LOGICAL_ARCHITECTURE_CANON.md", "Bio-Logical Architecture Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/COGNITIVE_SYSTEMS_ARCHITECTURE_CANON.md", "Cognitive Systems Architecture Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/AMOS_ORGANISM_OS_CANON.md", "AMOS Organism OS Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/AMOS_BRAIN_MASTER_OS_CANON.md", "AMOS Brain Master OS Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/AMOS_MIND_OS_CANON.md", "AMOS Mind OS Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/AMOS_OS_AGENT_CANON.md", "AMOS OS Agent Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/AMOS_QUANTUM_STACK_CANON.md", "AMOS Quantum Stack Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/AMOS_GOD_MODE_RUNTIME_CANON.md", "AMOS God Mode Runtime Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/AMOS_EXPRESSION_TRANSLATION_CANON.md", "AMOS Expression Translation Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/RSCF_CANON.md", "RSCF Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/GMEF_CANON.md", "GMEF Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/MVCC_CANON.md", "MVCC Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/CAS_CANON.md", "CAS Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/CAUSAL_EPOCH_CANON.md", "Causal Epoch Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/ATOMIC_MULTI_RSCF_CANON.md", "Atomic Multi-RSCF Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/SHARD_LOCAL_FINALITY_CANON.md", "Shard-Local Finality Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/PROOF_COORDINATION_AVOIDANCE_CANON.md", "Proof Coordination Avoidance Canon", "AMOS_MODEL"),
    ("01_CANON/04_INFRASTRUCTURE_CANON/PERSISTENT_PROVENANCE_CANON.md", "Persistent Provenance Canon", "AMOS_MODEL"),
    # 01_CANON/05_VARIABLE_REGISTRY
    ("01_CANON/05_VARIABLE_REGISTRY/TRANG_VARIABLE_REGISTRY.md", "TRANG Variable Registry", "AMOS_MODEL"),
    ("01_CANON/05_VARIABLE_REGISTRY/UBI_VARIABLE_REGISTRY.md", "UBI Variable Registry", "AMOS_MODEL"),
    ("01_CANON/05_VARIABLE_REGISTRY/HERITAGE_VARIABLE_REGISTRY.md", "Heritage Variable Registry", "AMOS_MODEL"),
    ("01_CANON/05_VARIABLE_REGISTRY/UNIVERSE_VARIABLE_REGISTRY.md", "Universe Variable Registry", "AMOS_MODEL"),
    ("01_CANON/05_VARIABLE_REGISTRY/QLS_QCLA_VARIABLE_REGISTRY.md", "QLS/QCLA Variable Registry", "AMOS_MODEL"),
    ("01_CANON/05_VARIABLE_REGISTRY/OMEGA_VARIABLE_REGISTRY.md", "Omega Variable Registry", "AMOS_MODEL"),
    ("01_CANON/05_VARIABLE_REGISTRY/BIO_LOGICAL_VARIABLE_REGISTRY.md", "Bio-Logical Variable Registry", "AMOS_MODEL"),
    ("01_CANON/05_VARIABLE_REGISTRY/RSCF_VARIABLE_REGISTRY.md", "RSCF Variable Registry", "AMOS_MODEL"),
    ("01_CANON/05_VARIABLE_REGISTRY/GMEF_VARIABLE_REGISTRY.md", "GMEF Variable Registry", "AMOS_MODEL"),
    ("01_CANON/05_VARIABLE_REGISTRY/CROSS_CANON_SYMBOL_CROSSWALK.md", "Cross-Canon Symbol Crosswalk", "AMOS_MODEL"),
    # 01_CANON/06_GLOSSARY
    ("01_CANON/06_GLOSSARY/AMOS_FRAMEWORK_GLOSSARY.md", "AMOS Framework Glossary", "AMOS_MODEL"),
    ("01_CANON/06_GLOSSARY/TRANG_FRAMEWORK_GLOSSARY.md", "TRANG Framework Glossary", "AMOS_MODEL"),
    ("01_CANON/06_GLOSSARY/UBI_GLOSSARY.md", "UBI Glossary", "AMOS_MODEL"),
    ("01_CANON/06_GLOSSARY/HERITAGE_GLOSSARY.md", "Heritage Glossary", "AMOS_MODEL"),
    ("01_CANON/06_GLOSSARY/UNIVERSE_OMEGA_GLOSSARY.md", "Universe/Omega Glossary", "AMOS_MODEL"),
    ("01_CANON/06_GLOSSARY/QLS_QCLA_GLOSSARY.md", "QLS/QCLA Glossary", "AMOS_MODEL"),
    ("01_CANON/06_GLOSSARY/NEUROSYNCAI_GLOSSARY.md", "NeuroSyncAI Glossary", "AMOS_MODEL"),
    ("01_CANON/06_GLOSSARY/TSS_TPE_GLOSSARY.md", "TSS/TPE Glossary", "AMOS_MODEL"),
    ("01_CANON/06_GLOSSARY/CROSS_FRAMEWORK_ALIAS_TABLE.md", "Cross-Framework Alias Table", "AMOS_MODEL"),
    # 01_CANON/07_PROVENANCE
    ("01_CANON/07_PROVENANCE/TRANG_ORIGIN_PROVENANCE.md", "TRANG Origin Provenance", "AMOS_MODEL"),
    ("01_CANON/07_PROVENANCE/AMOS_CORE_LINEAGE_PROVENANCE.md", "AMOS Core Lineage Provenance", "AMOS_MODEL"),
    ("01_CANON/07_PROVENANCE/HERITAGE_PROVENANCE.md", "Heritage Provenance", "AMOS_MODEL"),
    ("01_CANON/07_PROVENANCE/UBI_PROVENANCE.md", "UBI Provenance", "AMOS_MODEL"),
    ("01_CANON/07_PROVENANCE/NEUROSYNCAI_PROVENANCE.md", "NeuroSyncAI Provenance", "AMOS_MODEL"),
    ("01_CANON/07_PROVENANCE/UNIVERSE_CANON_PROVENANCE.md", "Universe Canon Provenance", "AMOS_MODEL"),
    ("01_CANON/07_PROVENANCE/TSS_TPE_PROVENANCE.md", "TSS/TPE Provenance", "AMOS_MODEL"),
    ("01_CANON/07_PROVENANCE/QLS_QCLA_PROVENANCE.md", "QLS/QCLA Provenance", "AMOS_MODEL"),
    ("01_CANON/07_PROVENANCE/FRAMEWORK_IP_LINEAGE.md", "Framework IP Lineage", "AMOS_MODEL"),
    ("01_CANON/07_PROVENANCE/SOURCE_ANCESTRY_GRAPH.md", "Source Ancestry Graph", "AMOS_MODEL"),
    ("01_CANON/07_PROVENANCE/PROVENANCE_INDEPENDENCE_REGISTRY.md", "Provenance Independence Registry", "AMOS_MODEL"),
    # 01_CANON/08_SUPERSESSION
    ("01_CANON/08_SUPERSESSION/AMOS_CORE_VERSION_LINEAGE.md", "AMOS Core Version Lineage", "AMOS_MODEL"),
    ("01_CANON/08_SUPERSESSION/AMOS_FRAMEWORK_SUPERSESSION.md", "AMOS Framework Supersession", "AMOS_MODEL"),
    ("01_CANON/08_SUPERSESSION/TRANG_FRAMEWORK_SUPERSESSION.md", "TRANG Framework Supersession", "AMOS_MODEL"),
    ("01_CANON/08_SUPERSESSION/UBI_SUPERSESSION.md", "UBI Supersession", "AMOS_MODEL"),
    ("01_CANON/08_SUPERSESSION/HERITAGE_SUPERSESSION.md", "Heritage Supersession", "AMOS_MODEL"),
    ("01_CANON/08_SUPERSESSION/UNIVERSE_CANON_SUPERSESSION.md", "Universe Canon Supersession", "AMOS_MODEL"),
    ("01_CANON/08_SUPERSESSION/ACTIVE_VS_LEGACY_CANON.md", "Active vs Legacy Canon", "AMOS_MODEL"),
    ("01_CANON/08_SUPERSESSION/COMPETING_DEFINITION_REGISTRY.md", "Competing Definition Registry", "AMOS_MODEL"),
    # 02_KERNEL/01_META_LOGIC
    ("02_KERNEL/01_META_LOGIC/K_UNIVERSE_LOGIC_KERNEL.md", "Kernel · Universe Logic Kernel", "AMOS_MODEL"),
    ("02_KERNEL/01_META_LOGIC/K_ABSOLUTE_LOGIC.md", "Kernel · Absolute Logic", "AMOS_MODEL"),
    ("02_KERNEL/01_META_LOGIC/K_BIO_LOGICAL_COMPUTING.md", "Kernel · Bio-Logical Computing", "AMOS_MODEL"),
    ("02_KERNEL/01_META_LOGIC/K_QUANTUM_LOGIC_SYSTEM.md", "Kernel · Quantum Logic System (QLS)", "AMOS_MODEL"),
    ("02_KERNEL/01_META_LOGIC/K_QCLA.md", "Kernel · QCLA", "AMOS_MODEL"),
    ("02_KERNEL/01_META_LOGIC/K_IRREDUCIBLE_SYSTEMS.md", "Kernel · Irreducible Systems", "AMOS_MODEL"),
    ("02_KERNEL/01_META_LOGIC/K_DIRECTED_SYSTEMAL_INTELLIGENCE.md", "Kernel · Directed Systemal Intelligence", "AMOS_MODEL"),
    # 02_KERNEL/02_COGNITION
    ("02_KERNEL/02_COGNITION/K_HUMAN_INTELLIGENCE.md", "Kernel · Human Intelligence", "AMOS_MODEL"),
    ("02_KERNEL/02_COGNITION/K_EMOTION_NEI.md", "Kernel · Emotion / NEI", "AMOS_MODEL"),
    ("02_KERNEL/02_COGNITION/K_COGNITION_NBI.md", "Kernel · Cognition / NBI", "AMOS_MODEL"),
    ("02_KERNEL/02_COGNITION/K_SOMATIC_SI.md", "Kernel · Somatic Intelligence / SI", "AMOS_MODEL"),
    ("02_KERNEL/02_COGNITION/K_BIOELECTROMAGNETIC_BEI.md", "Kernel · Bioelectromagnetic Intelligence / BEI", "AMOS_MODEL"),
    ("02_KERNEL/02_COGNITION/K_CONSCIOUSNESS.md", "Kernel · Consciousness", "AMOS_MODEL"),
    ("02_KERNEL/02_COGNITION/K_PERSONALITY.md", "Kernel · Personality", "AMOS_MODEL"),
    ("02_KERNEL/02_COGNITION/K_METACOGNITIVE_LOOP.md", "Kernel · Metacognitive Loop", "AMOS_MODEL"),
    # 02_KERNEL/03_CAUSAL
    ("02_KERNEL/03_CAUSAL/K_REALITY_CAUSALITY.md", "Kernel · Reality Causality", "AMOS_MODEL"),
    ("02_KERNEL/03_CAUSAL/K_QUANTUM_CAUSALITY.md", "Kernel · Quantum Causality", "AMOS_MODEL"),
    ("02_KERNEL/03_CAUSAL/K_BIOLOGICAL_CAUSALITY.md", "Kernel · Biological Causality", "AMOS_MODEL"),
    ("02_KERNEL/03_CAUSAL/K_CROSS_SCALE_CAUSALITY.md", "Kernel · Cross-Scale Causality", "AMOS_MODEL"),
    # 02_KERNEL/06_RISK_REPAIR
    ("02_KERNEL/06_RISK_REPAIR/K_ABSOLUTE_BIOLOGICAL_INTEGRITY.md", "Kernel · Absolute Biological Integrity", "AMOS_MODEL"),
    ("02_KERNEL/06_RISK_REPAIR/K_UBI_HOMEOSTASIS.md", "Kernel · UBI Homeostasis", "AMOS_MODEL"),
    ("02_KERNEL/06_RISK_REPAIR/K_UBI_ENTROPY_CORRECTION.md", "Kernel · UBI Entropy Correction", "AMOS_MODEL"),
    ("02_KERNEL/06_RISK_REPAIR/K_NEUROSYNCAI_RECOVERY.md", "Kernel · NeuroSyncAI Recovery", "AMOS_MODEL"),
    # 02_KERNEL/09_INTEGRATION
    ("02_KERNEL/09_INTEGRATION/K_CIL.md", "Kernel · Canon Integration Layer (CIL)", "AMOS_MODEL"),
    ("02_KERNEL/09_INTEGRATION/K_DCP.md", "Kernel · Domain Canon Programming (DCP)", "AMOS_MODEL"),
    ("02_KERNEL/09_INTEGRATION/K_UBA.md", "Kernel · UBA", "AMOS_MODEL"),
    ("02_KERNEL/09_INTEGRATION/K_UBI_BINDING.md", "Kernel · UBI Binding", "AMOS_MODEL"),
    ("02_KERNEL/09_INTEGRATION/K_HERITAGE_BINDING.md", "Kernel · Heritage Binding", "AMOS_MODEL"),
    ("02_KERNEL/09_INTEGRATION/K_TSS_TPE_BINDING.md", "Kernel · TSS/TPE Binding", "AMOS_MODEL"),
    ("02_KERNEL/09_INTEGRATION/K_NEUROSYNCAI_BINDING.md", "Kernel · NeuroSyncAI Binding", "AMOS_MODEL"),
    ("02_KERNEL/09_INTEGRATION/K_UNIVERSE_AMOS_BINDING.md", "Kernel · Universe-AMOS Binding", "AMOS_MODEL"),
    # 03_CONTROL_PLANE/03_POLICY
    ("03_CONTROL_PLANE/03_POLICY/CANON_POLICY.md", "Canon Policy", "AMOS_MODEL"),
    ("03_CONTROL_PLANE/03_POLICY/HERITAGE_POLICY.md", "Heritage Policy", "AMOS_MODEL"),
    ("03_CONTROL_PLANE/03_POLICY/UBI_INTEGRITY_POLICY.md", "UBI Integrity Policy", "AMOS_MODEL"),
    ("03_CONTROL_PLANE/03_POLICY/NEUROSYNCAI_GOVERNANCE_POLICY.md", "NeuroSyncAI Governance Policy", "AMOS_MODEL"),
    ("03_CONTROL_PLANE/03_POLICY/BIO_LOGICAL_GOVERNANCE_POLICY.md", "Bio-Logical Governance Policy", "AMOS_MODEL"),
    # 03_CONTROL_PLANE/04_AUTHORITY
    ("03_CONTROL_PLANE/04_AUTHORITY/CANON_AUTHORITY_CHAIN.md", "Canon Authority Chain", "AMOS_MODEL"),
    ("03_CONTROL_PLANE/04_AUTHORITY/ORIGIN_ARCHITECT_AUTHORITY.md", "Origin Architect Authority", "AMOS_MODEL"),
    ("03_CONTROL_PLANE/04_AUTHORITY/FRAMEWORK_AUTHORITY_REGISTRY.md", "Framework Authority Registry", "AMOS_MODEL"),
    # 03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION
    ("03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/MULTI_RSCF_TRANSACTION.md", "Multi-RSCF Transaction", "AMOS_MODEL"),
    ("03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/CANON_SEMANTIC_TRANSACTION.md", "Canon Semantic Transaction", "AMOS_MODEL"),
    ("03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/CROSS_FRAMEWORK_TRANSACTION.md", "Cross-Framework Transaction", "AMOS_MODEL"),
    # 03_CONTROL_PLANE/09_COMMIT
    ("03_CONTROL_PLANE/09_COMMIT/CAUSAL_EPOCH_FINALITY.md", "Causal Epoch Finality", "AMOS_MODEL"),
    ("03_CONTROL_PLANE/09_COMMIT/SHARD_LOCAL_FINALIZATION.md", "Shard-Local Finalization", "AMOS_MODEL"),
    ("03_CONTROL_PLANE/09_COMMIT/PROOF_BASED_COORDINATION_AVOIDANCE.md", "Proof-Based Coordination Avoidance", "AMOS_MODEL"),
    # 03_CONTROL_PLANE/12_ROLLBACK
    ("03_CONTROL_PLANE/12_ROLLBACK/CANON_LOCAL_INVALIDATION.md", "Canon Local Invalidation", "AMOS_MODEL"),
    ("03_CONTROL_PLANE/12_ROLLBACK/FRAMEWORK_LINEAGE_ROLLBACK.md", "Framework Lineage Rollback", "AMOS_MODEL"),
    # 04_RUNTIME/01_BOOT
    ("04_RUNTIME/01_BOOT/CANON_BOOTSTRAP.md", "Canon Bootstrap", "AMOS_MODEL"),
    ("04_RUNTIME/01_BOOT/FULL_BRAIN_BOOTSTRAP.md", "Full Brain Bootstrap", "AMOS_MODEL"),
    ("04_RUNTIME/01_BOOT/UBI_BOOTSTRAP.md", "UBI Bootstrap", "AMOS_MODEL"),
    ("04_RUNTIME/01_BOOT/UNIVERSE_CANON_BOOTSTRAP.md", "Universe Canon Bootstrap", "AMOS_MODEL"),
    # 04_RUNTIME/02_ROUTER
    ("04_RUNTIME/02_ROUTER/CANON_ROUTER.md", "Canon Router", "AMOS_MODEL"),
    ("04_RUNTIME/02_ROUTER/FRAMEWORK_ROUTER.md", "Framework Router", "AMOS_MODEL"),
    ("04_RUNTIME/02_ROUTER/RSCF_ROUTER.md", "RSCF Router", "AMOS_MODEL"),
    ("04_RUNTIME/02_ROUTER/HML_ROUTER.md", "HML Router", "AMOS_MODEL"),
    # 04_RUNTIME/06_EXECUTION
    ("04_RUNTIME/06_EXECUTION/FRACTAL_RUNTIME.md", "Fractal Runtime", "AMOS_MODEL"),
    ("04_RUNTIME/06_EXECUTION/ADAPTIVE_COMPLEXITY_RUNTIME.md", "Adaptive Complexity Runtime", "AMOS_MODEL"),
    ("04_RUNTIME/06_EXECUTION/FAST_PATH_RUNTIME.md", "Fast-Path Runtime", "AMOS_MODEL"),
    ("04_RUNTIME/06_EXECUTION/ADVERSARIAL_VALIDATION_RUNTIME.md", "Adversarial Validation Runtime", "AMOS_MODEL"),
    ("04_RUNTIME/06_EXECUTION/UNCERTAINTY_VECTOR_RUNTIME.md", "Uncertainty Vector Runtime", "AMOS_MODEL"),
    ("04_RUNTIME/06_EXECUTION/SENSITIVITY_RUNTIME.md", "Sensitivity Runtime", "AMOS_MODEL"),
    # 04_RUNTIME/09_FINALIZATION
    ("04_RUNTIME/09_FINALIZATION/PROOF_CAPSULE_FINALIZER.md", "Proof Capsule Finalizer", "AMOS_MODEL"),
    ("04_RUNTIME/09_FINALIZATION/CAUSAL_EPOCH_FINALIZER.md", "Causal Epoch Finalizer", "AMOS_MODEL"),
    ("04_RUNTIME/09_FINALIZATION/LOCAL_PROOF_FINALIZER.md", "Local Proof Finalizer", "AMOS_MODEL"),
    # 05_COGNITIVE_ORGANISM/01_IDENTITY
    ("05_COGNITIVE_ORGANISM/01_IDENTITY/IDENTITY_CONTINUITY_MODEL.md", "Identity Continuity Model", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/01_IDENTITY/DIRECTED_SYSTEMAL_IDENTITY.md", "Directed Systemal Identity", "AMOS_MODEL"),
    # 05_COGNITIVE_ORGANISM/04_COGNITION
    ("05_COGNITIVE_ORGANISM/04_COGNITION/AMOS_COGNITION_ENGINE.md", "AMOS Cognition Engine", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/04_COGNITION/NBI_ENGINE.md", "NBI Engine", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/04_COGNITION/HUMAN_INTELLIGENCE_ENGINE.md", "Human Intelligence Engine", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/04_COGNITION/FIRST_PRINCIPLES_REASONING.md", "First-Principles Reasoning", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/04_COGNITION/FRACTAL_REASONING.md", "Fractal Reasoning", "AMOS_MODEL"),
    # 05_COGNITIVE_ORGANISM/06_WORLD_MODEL
    ("05_COGNITIVE_ORGANISM/06_WORLD_MODEL/TRANG_REALITY_ARCHITECTURE_BINDING.md", "TRANG Reality Architecture Binding", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/06_WORLD_MODEL/UNIVERSE_CANON_WORLD_MODEL.md", "Universe Canon World Model", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/06_WORLD_MODEL/UNIVERSAL_FIELD_WORLD_MODEL.md", "Universal Field World Model", "AMOS_MODEL"),
    # 05_COGNITIVE_ORGANISM/07_EMOTION_REGULATION
    ("05_COGNITIVE_ORGANISM/07_EMOTION_REGULATION/AMOS_EMOTION_ENGINE.md", "AMOS Emotion Engine", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/07_EMOTION_REGULATION/NEI_ENGINE.md", "NEI Engine", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/07_EMOTION_REGULATION/BIOLOGICAL_EMOTION_REGULATION.md", "Biological Emotion Regulation", "AMOS_MODEL"),
    # 05_COGNITIVE_ORGANISM/15_HOMEOSTASIS
    ("05_COGNITIVE_ORGANISM/15_HOMEOSTASIS/UBI_HOMEOSTASIS.md", "UBI Homeostasis", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/15_HOMEOSTASIS/ABSOLUTE_BIOLOGICAL_INTEGRITY.md", "Absolute Biological Integrity", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/15_HOMEOSTASIS/SOMATIC_INTELLIGENCE_SI.md", "Somatic Intelligence (SI)", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/15_HOMEOSTASIS/BIOELECTROMAGNETIC_INTELLIGENCE_BEI.md", "Bioelectromagnetic Intelligence (BEI)", "AMOS_MODEL"),
    # 05_COGNITIVE_ORGANISM/16_REPAIR
    ("05_COGNITIVE_ORGANISM/16_REPAIR/UBI_RECOVERY_ENGINE.md", "UBI Recovery Engine", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/16_REPAIR/BIOLOGICAL_ENTROPY_CORRECTION.md", "Biological Entropy Correction", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/16_REPAIR/NEUROSYNCAI_RECOVERY_BINDING.md", "NeuroSyncAI Recovery Binding", "AMOS_MODEL"),
    # 05_COGNITIVE_ORGANISM/18_LIFECYCLE
    ("05_COGNITIVE_ORGANISM/18_LIFECYCLE/COGNITIVE_ORGANISM_EVOLUTION.md", "Cognitive Organism Evolution", "AMOS_MODEL"),
    ("05_COGNITIVE_ORGANISM/18_LIFECYCLE/BIOLOGICAL_COGNITIVE_LIFECYCLE.md", "Biological Cognitive Lifecycle", "AMOS_MODEL"),
    # 11_KNOWLEDGE/02_CLAIMS
    ("11_KNOWLEDGE/02_CLAIMS/CANON_CLAIM_REGISTRY.md", "Canon Claim Registry", "AMOS_MODEL"),
    ("11_KNOWLEDGE/02_CLAIMS/HERITAGE_CLAIM_REGISTRY.md", "Heritage Claim Registry", "AMOS_MODEL"),
    ("11_KNOWLEDGE/02_CLAIMS/UBI_CLAIM_REGISTRY.md", "UBI Claim Registry", "AMOS_MODEL"),
    ("11_KNOWLEDGE/02_CLAIMS/FRAMEWORK_CLAIM_REGISTRY.md", "Framework Claim Registry", "AMOS_MODEL"),
    # 11_KNOWLEDGE/03_RSCF
    ("11_KNOWLEDGE/03_RSCF/CANON_RSCF_INDEX.md", "Canon RSCF Index", "AMOS_MODEL"),
    ("11_KNOWLEDGE/03_RSCF/AMOS_RSCF_INDEX.md", "AMOS RSCF Index", "AMOS_MODEL"),
    ("11_KNOWLEDGE/03_RSCF/HERITAGE_RSCF_INDEX.md", "Heritage RSCF Index", "AMOS_MODEL"),
    ("11_KNOWLEDGE/03_RSCF/UBI_RSCF_INDEX.md", "UBI RSCF Index", "AMOS_MODEL"),
    ("11_KNOWLEDGE/03_RSCF/TRANG_REALITY_RSCF_INDEX.md", "TRANG Reality RSCF Index", "AMOS_MODEL"),
    ("11_KNOWLEDGE/03_RSCF/UNIVERSE_RSCF_INDEX.md", "Universe RSCF Index", "AMOS_MODEL"),
    ("11_KNOWLEDGE/03_RSCF/TSS_TPE_RSCF_INDEX.md", "TSS/TPE RSCF Index", "AMOS_MODEL"),
    ("11_KNOWLEDGE/03_RSCF/QLS_QCLA_RSCF_INDEX.md", "QLS/QCLA RSCF Index", "AMOS_MODEL"),
    ("11_KNOWLEDGE/03_RSCF/NEUROSYNCAI_RSCF_INDEX.md", "NeuroSyncAI RSCF Index", "AMOS_MODEL"),
    # 11_KNOWLEDGE/05_FRAMEWORKS
    ("11_KNOWLEDGE/05_FRAMEWORKS/UBA_FRAMEWORK.md", "UBA Framework", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/BIO_LOGICAL_COMPUTING_FRAMEWORK.md", "Bio-Logical Computing Framework", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/BIO_LOGICAL_ARCHITECTURE_FRAMEWORK.md", "Bio-Logical Architecture Framework", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/DOMAIN_CANON_PROGRAMMING_DCP.md", "Domain Canon Programming (DCP)", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/COGNITIVE_SYSTEMS_ARCHITECTURE.md", "Cognitive Systems Architecture", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/AMOS_ORGANISM_OS_FRAMEWORK.md", "AMOS Organism OS Framework", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/AMOS_MIND_OS_FRAMEWORK.md", "AMOS Mind OS Framework", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/AMOS_OS_AGENT_FRAMEWORK.md", "AMOS OS Agent Framework", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/UBI_FRAMEWORK.md", "UBI Framework", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/ABSOLUTE_BIOLOGICAL_INTEGRITY_FRAMEWORK.md", "Absolute Biological Integrity Framework", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/UBI_SCORE_FRAMEWORK.md", "UBI Score Framework", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/UBI_WEARABLE_FRAMEWORK.md", "UBI Wearable Framework", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/QLS_FRAMEWORK.md", "QLS Framework", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/PSI_FRAMEWORK.md", "PSI Framework", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/NEUROSYNCAI_FRAMEWORK.md", "NeuroSyncAI Framework", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/FIRST_PRINCIPLES_ARTICULATION.md", "First-Principles Articulation", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/POST_THEORY_COMMUNICATION.md", "Post-Theory Communication", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/IRREDUCIBLE_SYSTEMS_ARCHITECTURE.md", "Irreducible Systems Architecture", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/DIRECTED_SYSTEMAL_INTELLIGENCE.md", "Directed Systemal Intelligence", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/METACOGNITIVE_LOOP.md", "Metacognitive Loop", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/DESIGN_FOR_ABSOLUTE_INTEGRITY.md", "Design for Absolute Integrity", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/ABSOLUTE_STRUCTURAL_INTEGRITY.md", "Absolute Structural Integrity", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/NEUTRAL_INTERFACE_TRAINING_PROTOCOL.md", "Neutral Interface Training Protocol", "AMOS_MODEL"),
    ("11_KNOWLEDGE/05_FRAMEWORKS/LAWFUL_SYSTEM_PERCEPTION_MODEL.md", "Lawful System Perception Model", "AMOS_MODEL"),
    # 11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE
    ("11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/HERITAGE_INTELLIGENCE.md", "Heritage Intelligence", "AMOS_MODEL"),
    ("11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/HERITAGE_FRACTAL_MATHEMATICS.md", "Heritage Fractal Mathematics", "AMOS_MODEL"),
    ("11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/HERITAGE_SPATIAL_INTELLIGENCE.md", "Heritage Spatial Intelligence", "AMOS_MODEL"),
    ("11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/HERITAGE_CIVILIZATION_HISTORY.md", "Heritage Civilization History", "AMOS_MODEL"),
    ("11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/HERITAGE_MUSIC_ACOUSTIC_RULES.md", "Heritage Music/Acoustic Rules", "AMOS_MODEL"),
    ("11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/HERITAGE_PATTERN_SYSTEMS.md", "Heritage Pattern Systems", "AMOS_MODEL"),
    ("11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/UBI_NEUROBIOLOGICAL_INTELLIGENCE.md", "UBI Neurobiological Intelligence", "AMOS_MODEL"),
    ("11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/UBI_NEUROEMOTIONAL_INTELLIGENCE.md", "UBI Neuroemotional Intelligence", "AMOS_MODEL"),
    ("11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/UBI_SOMATIC_INTELLIGENCE.md", "UBI Somatic Intelligence", "AMOS_MODEL"),
    ("11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/UBI_BIOELECTROMAGNETIC_INTELLIGENCE.md", "UBI Bioelectromagnetic Intelligence", "AMOS_MODEL"),
    # 13_MODELS/01_FOUNDATION
    ("13_MODELS/01_FOUNDATION/TRANG_REALITY_ARCHITECTURE_MODEL.md", "TRANG Reality Architecture Model", "AMOS_MODEL"),
    ("13_MODELS/01_FOUNDATION/UNIVERSAL_FIELD_ARCHITECTURE_MODEL.md", "Universal Field Architecture Model", "AMOS_MODEL"),
    ("13_MODELS/01_FOUNDATION/ABSOLUTE_OMNIVERSE_MODEL.md", "Absolute Omniverse Model", "AMOS_MODEL"),
    ("13_MODELS/01_FOUNDATION/UBA_MODEL.md", "UBA Model", "AMOS_MODEL"),
    ("13_MODELS/01_FOUNDATION/BIO_LOGICAL_COMPUTING_MODEL.md", "Bio-Logical Computing Model", "AMOS_MODEL"),
    # 13_MODELS/04_DOMAIN
    ("13_MODELS/04_DOMAIN/UBI_MODEL_REGISTRY.md", "UBI Model Registry", "AMOS_MODEL"),
    ("13_MODELS/04_DOMAIN/HERITAGE_MODEL_REGISTRY.md", "Heritage Model Registry", "AMOS_MODEL"),
    ("13_MODELS/04_DOMAIN/TSS_MODEL_REGISTRY.md", "TSS Model Registry", "AMOS_MODEL"),
    ("13_MODELS/04_DOMAIN/TPE_MODEL_REGISTRY.md", "TPE Model Registry", "AMOS_MODEL"),
    ("13_MODELS/04_DOMAIN/QLS_MODEL_REGISTRY.md", "QLS Model Registry", "AMOS_MODEL"),
    ("13_MODELS/04_DOMAIN/QCLA_MODEL_REGISTRY.md", "QCLA Model Registry", "AMOS_MODEL"),
    ("13_MODELS/04_DOMAIN/NEUROSYNCAI_MODEL_REGISTRY.md", "NeuroSyncAI Model Registry", "AMOS_MODEL"),
    # 13_MODELS/05_CALIBRATION
    ("13_MODELS/05_CALIBRATION/UBI_SCORE_CALIBRATION.md", "UBI Score Calibration", "AMOS_MODEL"),
    ("13_MODELS/05_CALIBRATION/CONFIDENCE_CEILING_CALIBRATION.md", "Confidence Ceiling Calibration", "AMOS_MODEL"),
    ("13_MODELS/05_CALIBRATION/PROVENANCE_INDEPENDENCE_CALIBRATION.md", "Provenance Independence Calibration", "AMOS_MODEL"),
    # 16_SCHEMAS/10_RSCF
    ("16_SCHEMAS/10_RSCF/proof_capsule.schema.md", "Proof Capsule Schema", "AMOS_MODEL"),
    ("16_SCHEMAS/10_RSCF/provenance_topology.schema.md", "Provenance Topology Schema", "AMOS_MODEL"),
    ("16_SCHEMAS/10_RSCF/competing_hypothesis.schema.md", "Competing Hypothesis Schema", "AMOS_MODEL"),
    ("16_SCHEMAS/10_RSCF/causal_epoch.schema.md", "Causal Epoch Schema", "AMOS_MODEL"),
    ("16_SCHEMAS/10_RSCF/rscf_transaction.schema.md", "RSCF Transaction Schema", "AMOS_MODEL"),
    ("16_SCHEMAS/10_RSCF/framework_node.schema.md", "Framework Node Schema", "AMOS_MODEL"),
    # 16_SCHEMAS/11_OBSERVABILITY
    ("16_SCHEMAS/11_OBSERVABILITY/canon_health.schema.md", "Canon Health Schema", "AMOS_MODEL"),
    ("16_SCHEMAS/11_OBSERVABILITY/provenance_health.schema.md", "Provenance Health Schema", "AMOS_MODEL"),
    # 21_DOMAINS/02_RESEARCH
    ("21_DOMAINS/02_RESEARCH/CANON_VALIDATION.md", "Canon Validation", "AMOS_MODEL"),
    ("21_DOMAINS/02_RESEARCH/FRAMEWORK_VALIDATION.md", "Framework Validation", "AMOS_MODEL"),
    ("21_DOMAINS/02_RESEARCH/HERITAGE_RESEARCH_METHOD.md", "Heritage Research Method", "AMOS_MODEL"),
    # 21_DOMAINS/04_STRATEGY
    ("21_DOMAINS/04_STRATEGY/TSS_DOMAIN_MODEL.md", "TSS Domain Model", "AMOS_MODEL"),
    ("21_DOMAINS/04_STRATEGY/TPE_DOMAIN_MODEL.md", "TPE Domain Model", "AMOS_MODEL"),
    ("21_DOMAINS/04_STRATEGY/SEVEN_CYCLES_DOMAIN_MODEL.md", "Seven Cycles Domain Model", "AMOS_MODEL"),
    ("21_DOMAINS/04_STRATEGY/DIRECTED_SYSTEMAL_INTELLIGENCE_DOMAIN.md", "Directed Systemal Intelligence Domain", "AMOS_MODEL"),
    # 21_DOMAINS/05_DESIGN
    ("21_DOMAINS/05_DESIGN/IRREDUCIBLE_SYSTEMS_DESIGN.md", "Irreducible Systems Design", "AMOS_MODEL"),
    ("21_DOMAINS/05_DESIGN/DESIGN_FOR_ABSOLUTE_INTEGRITY.md", "Design for Absolute Integrity", "AMOS_MODEL"),
    ("21_DOMAINS/05_DESIGN/BIO_LOGICAL_ARCHITECTURE_DESIGN.md", "Bio-Logical Architecture Design", "AMOS_MODEL"),
    # 21_DOMAINS/06_BIOLOGY
    ("21_DOMAINS/06_BIOLOGY/UBI_DOMAIN_CANON.md", "UBI Domain Canon", "AMOS_MODEL"),
    ("21_DOMAINS/06_BIOLOGY/UBI_OMNIS.md", "UBI OMNIS", "AMOS_MODEL"),
    ("21_DOMAINS/06_BIOLOGY/UBI_SUPER.md", "UBI SUPER", "AMOS_MODEL"),
    ("21_DOMAINS/06_BIOLOGY/NBI.md", "NBI (Neurobiological Intelligence)", "AMOS_MODEL"),
    ("21_DOMAINS/06_BIOLOGY/NEI.md", "NEI (Neuroemotional Intelligence)", "AMOS_MODEL"),
    ("21_DOMAINS/06_BIOLOGY/SI.md", "SI (Somatic Intelligence)", "AMOS_MODEL"),
    ("21_DOMAINS/06_BIOLOGY/BEI.md", "BEI (Bioelectromagnetic Intelligence)", "AMOS_MODEL"),
    ("21_DOMAINS/06_BIOLOGY/ABSOLUTE_BIOLOGICAL_INTEGRITY.md", "Absolute Biological Integrity", "AMOS_MODEL"),
    ("21_DOMAINS/06_BIOLOGY/BIOLOGICAL_PROGRAMMING.md", "Biological Programming", "AMOS_MODEL"),
    ("21_DOMAINS/06_BIOLOGY/UBI_ENTROPY_CORRECTION.md", "UBI Entropy Correction", "AMOS_MODEL"),
    ("21_DOMAINS/06_BIOLOGY/UBI_FRACTAL_ARCHITECTURE.md", "UBI Fractal Architecture", "AMOS_MODEL"),
    ("21_DOMAINS/06_BIOLOGY/CROSS_SPECIES_FUNCTIONAL_MODE_MODEL.md", "Cross-Species Functional Mode Model", "AMOS_MODEL"),
    ("21_DOMAINS/06_BIOLOGY/UBI_NEUROSYNCAI_INTEGRATION.md", "UBI NeuroSyncAI Integration", "AMOS_MODEL"),
    ("21_DOMAINS/06_BIOLOGY/UBI_CONSENTX_INTEGRATION.md", "UBI ConsentX Integration", "AMOS_MODEL"),
    ("21_DOMAINS/06_BIOLOGY/UBI_ID_EXCHANGE_INTEGRATION.md", "UBI ID Exchange Integration", "AMOS_MODEL"),
    ("21_DOMAINS/06_BIOLOGY/UBI_RATPAK_INTEGRATION.md", "UBI RatPAK Integration", "AMOS_MODEL"),
    # 21_DOMAINS/07_HEALTHCARE
    ("21_DOMAINS/07_HEALTHCARE/AMOS_MEDICAL_CLINICAL_KERNEL.md", "AMOS Medical Clinical Kernel", "AMOS_MODEL"),
    ("21_DOMAINS/07_HEALTHCARE/UBI_HEALTH_APPLICATION.md", "UBI Health Application", "AMOS_MODEL"),
    ("21_DOMAINS/07_HEALTHCARE/BIOLOGICAL_INTEGRITY_HEALTH_MODEL.md", "Biological Integrity Health Model", "AMOS_MODEL"),
    # 21_DOMAINS/08_LEGAL
    ("21_DOMAINS/08_LEGAL/AMOS_LEGAL_KERNEL.md", "AMOS Legal Kernel", "AMOS_MODEL"),
    ("21_DOMAINS/08_LEGAL/VN_LEGAL_ENGINE.md", "VN Legal Engine", "AMOS_MODEL"),
    ("21_DOMAINS/08_LEGAL/CANON_IP_GOVERNANCE.md", "Canon IP Governance", "AMOS_MODEL"),
    # 21_DOMAINS/09_FINANCE
    ("21_DOMAINS/09_FINANCE/MACRO_ECONOMY_KERNEL.md", "Macro Economy Kernel", "AMOS_MODEL"),
    ("21_DOMAINS/09_FINANCE/OMEGA_FX_STRUCTURAL_OS.md", "Omega FX Structural OS", "AMOS_MODEL"),
    ("21_DOMAINS/09_FINANCE/TRANG_ZERO_FOREX.md", "Trang Zero Forex", "AMOS_MODEL"),
    # 21_DOMAINS/10_CUSTOM
    ("21_DOMAINS/10_CUSTOM/HERITAGE_INTELLIGENCE_DOMAIN.md", "Heritage Intelligence Domain", "AMOS_MODEL"),
    ("21_DOMAINS/10_CUSTOM/PLANETARY_SYNCHRONIZATION_INTERFACE.md", "Planetary Synchronization Interface", "AMOS_MODEL"),
    ("21_DOMAINS/10_CUSTOM/NEUROSYNCAI_DOMAIN.md", "NeuroSyncAI Domain", "AMOS_MODEL"),
    ("21_DOMAINS/10_CUSTOM/DOMAIN_CANON_PROGRAMMING.md", "Domain Canon Programming", "AMOS_MODEL"),
    # 22_RESEARCH/01_PAPERS
    ("22_RESEARCH/01_PAPERS/NATIVE_CANON_SOURCE_REGISTRY.md", "Native Canon Source Registry", "AMOS_MODEL"),
    ("22_RESEARCH/01_PAPERS/EXTERNAL_EVIDENCE_SOURCE_REGISTRY.md", "External Evidence Source Registry", "AMOS_MODEL"),
    # 22_RESEARCH/03_COMPETING_MODELS
    ("22_RESEARCH/03_COMPETING_MODELS/CANON_COMPETING_DEFINITIONS.md", "Canon Competing Definitions", "AMOS_MODEL"),
    ("22_RESEARCH/03_COMPETING_MODELS/UBI_COMPETING_MODELS.md", "UBI Competing Models", "AMOS_MODEL"),
    ("22_RESEARCH/03_COMPETING_MODELS/HERITAGE_COMPETING_MODELS.md", "Heritage Competing Models", "AMOS_MODEL"),
    ("22_RESEARCH/03_COMPETING_MODELS/REALITY_ARCHITECTURE_COMPETING_MODELS.md", "Reality Architecture Competing Models", "AMOS_MODEL"),
    # 22_RESEARCH/04_VALIDATION
    ("22_RESEARCH/04_VALIDATION/FRAMEWORK_EMPIRICAL_STATUS.md", "Framework Empirical Status", "AMOS_MODEL"),
    ("22_RESEARCH/04_VALIDATION/CANON_SOURCE_CLAIM_AUDIT.md", "Canon Source Claim Audit", "AMOS_MODEL"),
    ("22_RESEARCH/04_VALIDATION/CROSS_FRAMEWORK_VALIDATION.md", "Cross-Framework Validation", "AMOS_MODEL"),
    # 24_ARCHIVE/00_LEGACY
    ("24_ARCHIVE/00_LEGACY/AMOS_CORE_HISTORICAL_INDEX.md", "AMOS Core Historical Index", "AMOS_MODEL"),
    ("24_ARCHIVE/00_LEGACY/TRANG_FRAMEWORK_HISTORICAL_INDEX.md", "TRANG Framework Historical Index", "AMOS_MODEL"),
    ("24_ARCHIVE/00_LEGACY/UBI_HISTORICAL_INDEX.md", "UBI Historical Index", "AMOS_MODEL"),
    ("24_ARCHIVE/00_LEGACY/HERITAGE_HISTORICAL_INDEX.md", "Heritage Historical Index", "AMOS_MODEL"),
    # 24_ARCHIVE/01_DEPRECATED
    ("24_ARCHIVE/01_DEPRECATED/DEPRECATED_FRAMEWORK_REGISTRY.md", "Deprecated Framework Registry", "AMOS_MODEL"),
    # 24_ARCHIVE/02_SUPERSEDED
    ("24_ARCHIVE/02_SUPERSEDED/SUPERSEDED_CANON_REGISTRY.md", "Superseded Canon Registry", "AMOS_MODEL"),
    ("24_ARCHIVE/02_SUPERSEDED/SUPERSEDED_FRAMEWORK_REGISTRY.md", "Superseded Framework Registry", "AMOS_MODEL"),
    # 24_ARCHIVE/03_EXPERIMENTAL
    ("24_ARCHIVE/03_EXPERIMENTAL/EXPERIMENTAL_FRAMEWORK_REGISTRY.md", "Experimental Framework Registry", "AMOS_MODEL"),
    # 25_COGNITIVE_MATRIX
    ("25_COGNITIVE_MATRIX/AMOS_X_UBI_MATRIX.md", "AMOS × UBI Matrix", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/AMOS_X_HERITAGE_MATRIX.md", "AMOS × Heritage Matrix", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/AMOS_X_TRANG_REALITY_MATRIX.md", "AMOS × TRANG Reality Matrix", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/AMOS_X_UNIVERSE_CANON_MATRIX.md", "AMOS × Universe Canon Matrix", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/AMOS_X_TSS_TPE_MATRIX.md", "AMOS × TSS/TPE Matrix", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/AMOS_X_QLS_QCLA_MATRIX.md", "AMOS × QLS/QCLA Matrix", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/AMOS_X_NEUROSYNCAI_MATRIX.md", "AMOS × NeuroSyncAI Matrix", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/UBI_X_NEUROSYNCAI_MATRIX.md", "UBI × NeuroSyncAI Matrix", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/UBI_X_FULL_BRAIN_MATRIX.md", "UBI × Full Brain Matrix", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/UBI_X_EMOTION_MATRIX.md", "UBI × Emotion Matrix", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/UBI_X_COGNITION_MATRIX.md", "UBI × Cognition Matrix", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/HERITAGE_X_TRANG_ZERO_MATRIX.md", "Heritage × Trang Zero Matrix", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/HERITAGE_X_TSS_MATRIX.md", "Heritage × TSS Matrix", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/REALITY_X_ULK_MATRIX.md", "Reality × ULK Matrix", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/REALITY_X_RSCF_MATRIX.md", "Reality × RSCF Matrix", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/UNIVERSE_X_OMEGA_MATRIX.md", "Universe × Omega Matrix", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/CORE_X_CONTROL_PLANE_MATRIX.md", "Core × Control Plane Matrix", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/CORE_X_RUNTIME_MATRIX.md", "Core × Runtime Matrix", "AMOS_MODEL"),
    ("25_COGNITIVE_MATRIX/TOTAL_CANON_RELATION_MATRIX.md", "Total Canon Relation Matrix", "AMOS_MODEL"),
]


def plane_of(relpath):
    top = relpath.split("/")[0]
    return PLANES.get(top, ("Unknown Plane", "unclassified plane"))


def artifact_kind(basename):
    b = basename[:-3] if basename.endswith(".md") else basename
    ub = b.upper()
    if ub.startswith("INDEX") or ub.endswith("_INDEX"):
        return "INDEX"
    for token, kind in (
        ("README", "README"), ("CONTRACT", "CONTRACT"), ("MAP", "MAP"),
        ("REGISTRY", "REGISTRY"), ("_LEDGER", "LEDGER"), ("_LOG", "LOG"),
        ("_HISTORY", "HISTORY"), ("_AUDIT", "AUDIT"), ("_POLICY", "POLICY"),
        ("_LIFECYCLE", "LIFECYCLE"), ("_SPEC", "SPEC"), ("_TESTS", "TESTS"),
        ("_RULES", "RULES"), ("_GATES", "GATES"), ("MATRIX", "MATRIX"),
        ("LINEAGE", "LINEAGE"), ("SUPERSESSION", "SUPERSESSION"),
        ("PROVENANCE", "PROVENANCE"), ("GLOSSARY", "GLOSSARY"),
        ("CROSSWALK", "CROSSWALK"), ("CROSSWALK", "CROSSWALK"),
        ("BINDING", "BINDING"), ("FRAMEWORK", "FRAMEWORK"),
        ("CANON", "CANON"), ("MODEL", "MODEL"), ("SCHEMA", "SCHEMA"),
        ("ENGINE", "ENGINE"), ("KERNEL", "KERNEL"), ("ROUTER", "ROUTER"),
        ("RUNTIME", "RUNTIME"), ("FINALIZER", "FINALIZER"),
        ("FINALITY", "FINALITY"), ("FINALIZATION", "FINALIZATION"),
        ("BOOTSTRAP", "BOOTSTRAP"), ("RECOVERY", "RECOVERY"),
        ("REASONING", "REASONING"), ("CALIBRATION", "CALIBRATION"),
        ("DOMAIN", "DOMAIN"), ("VALIDATION", "VALIDATION"),
        ("METHOD", "METHOD"), ("DESIGN", "DESIGN"), ("PROGRAMMING", "PROGRAMMING"),
        ("INTEGRATION", "INTEGRATION"), ("APPLICATION", "APPLICATION"),
        ("GOVERNANCE", "GOVERNANCE"), ("ARCHITECTURE", "ARCHITECTURE"),
        ("INTELLIGENCE", "INTELLIGENCE"), ("CONTINUITY", "CONTINUITY"),
        ("COMMUNICATION", "COMMUNICATION"), ("ARTICULATION", "ARTICULATION"),
        ("PROTOCOL", "PROTOCOL"), ("PERCEPTION", "PERCEPTION"),
        ("REGULATION", "REGULATION"), ("EVOLUTION", "EVOLUTION"),
        ("COVERAGE", "COVERAGE"), ("AUDIT", "AUDIT"),
    ):
        if token in ub:
            return kind
    return "ARTIFACT"


def node_id(relpath):
    base = os.path.basename(relpath)[:-3]
    return "amos_" + relpath.replace("/", "_").replace(".md", "").lower().replace("-", "_")


def build_content(relpath, subject, claim_class):
    pname, pdesc = plane_of(relpath)
    basename = os.path.basename(relpath)
    kind = artifact_kind(basename)
    title = subject
    top = relpath.split("/")[0]
    seg = os.path.dirname(relpath)
    node = node_id(relpath)

    fm = (
        "---\n"
        f"title: \"{title}\"\n"
        f"artifact: \"{basename}\"\n"
        f"artifact_id: \"{node}\"\n"
        f"origin_architect: \"Trang Phan\"\n"
        f"steward: \"Trang Phan\"\n"
        f"system: \"AMOS OS\"\n"
        f"plane: \"{top}\"\n"
        f"segment: \"{seg}\"\n"
        f"artifact_kind: \"{kind}\"\n"
        f"path: \"{relpath}\"\n"
        "\n"
        "tags:\n"
        f"  - amos_os\n"
        f"  - {top.lower()}\n"
        f"  - {kind.lower()}\n"
        f"  - canon_placeholder\n"
        f"  - rscf\n"
        "\n"
        f"version: \"0.1.0\"\n"
        f"updated: \"{TODAY}\"\n"
        "\n"
        "status: \"PLACEHOLDER\"\n"
        f"epistemic_class: \"{claim_class}\"\n"
        "canonical_status: \"UNKNOWN/GAP\"\n"
        "implementation_status: \"NOT_ESTABLISHED\"\n"
        "validation_status: \"NOT_ESTABLISHED\"\n"
        "executable_binding: \"NOT_ESTABLISHED\"\n"
        "ingestion_action: \"ADD_ONLY\"\n"
        "---\n"
    )

    body = []
    body.append(f"# {title}\n")
    body.append("## 0. Status\n")
    body.append(
        f"`{basename}` is an **ADD-ONLY placeholder** for the **{pname}** plane "
        f"segment at `{seg}`.\n"
    )
    body.append(
        "It marks a canonical slot reserved by the AMOS canon-ingestion manifest "
        "for the framework family named above. It is NOT populated canon, NOT "
        "validated, and NOT enforced.\n"
    )
    body.append("The governing boundaries are:\n")
    body.append("```text\n"
                "PLACEHOLDER != IMPLEMENTED\n\n"
                "ADDRESSABLE != VALIDATED\n\n"
                "DOCUMENTED != ENFORCED\n\n"
                "MODEL != OBSERVATION\n\n"
                "SOURCE_CLAIM != VERIFIED\n\n"
                "CANON_CANDIDATE != CANONICAL\n\n"
                "CANONICAL != EMPIRICAL_TRUTH\n\n"
                "CAPABILITY != AUTHORITY\n\n"
                "AUTHORIZATION != COMMIT\n\n"
                "PROPOSAL != COMMIT\n\n"
                "IMPLEMENTED != VALIDATED\n\n"
                "LOGGED != APPROVED\n\n"
                "UNKNOWN/GAP != PASS\n"
                "```\n")
    body.append("Origin architect / steward:\n\n**Trang Phan**\n")
    body.append("---\n")
    body.append("## 1. Purpose\n")
    body.append(
        f"This artifact reserves the **{subject}** slot within the {pname} plane. "
        f"The {pname} plane governs {pdesc}.\n"
    )
    body.append(
        "Substantive content (canonical definitions, laws, registries, schemas, "
        "models, or bindings) is to be populated from verified native-canon "
        "sources under the AMOS_CANON_INGESTION_RULE. This placeholder does not, "
        "by its existence, establish canon, empirical validity, or runtime "
        "enforcement.\n")
    body.append("---\n")
    body.append("## 2. Non-Purpose\n")
    body.append("This placeholder MUST NOT be used to claim:\n")
    body.append(
        "* universal laws of reality;\n"
        "* scientific proof;\n"
        "* biological truth;\n"
        "* mathematical theoremhood;\n"
        "* philosophical certainty;\n"
        "* runtime enforcement that has not been implemented;\n"
        "* final canonical status;\n"
        "* authority merely from architectural importance;\n"
        "* or successful validation merely because the slot is addressable.\n")
    body.append("---\n")
    body.append("## 3. Ingestion Rule\n")
    body.append("```yaml\n"
                "AMOS_CANON_INGESTION_RULE:\n"
                "  existing_folder:\n"
                "    preserve: true\n"
                "  existing_file:\n"
                "    preserve: true\n"
                "    overwrite: false\n"
                "  new_framework:\n"
                "    action: ADD_FILE_TO_EXISTING_FOLDER\n"
                "  master_source:\n"
                "    action: NORMALIZE_TO_RSCF_FILE\n"
                "  framework_existing_in_multiple_sources:\n"
                "    action:\n"
                "      - CREATE_ONE_CANONICAL_NODE\n"
                "      - LINK_ALL_SOURCE_PROVENANCE\n"
                "      - DO_NOT_CREATE_DUPLICATE_CANON\n"
                "  historical_source:\n"
                "    action:\n"
                "      - LINK_TO_CANON\n"
                "      - RECORD_LINEAGE\n"
                "      - PRESERVE_HERITAGE\n"
                "  external_research:\n"
                "    action:\n"
                "      - KEEP_OUT_OF_NATIVE_CANON\n"
                "      - LINK_AS_EVIDENCE\n"
                "  duplicate_filename:\n"
                "    action:\n"
                "      - COMPARE_CONTENT_AND_LINEAGE\n"
                "      - DO_NOT_OVERWRITE\n"
                "  uncertainty:\n"
                "    action:\n"
                "      - MARK_GAP_OR_COMPETING\n"
                "      - NEVER_INVENT_CANON\n"
                "```\n")
    body.append("---\n")
    body.append("## 4. Contract discipline\n")
    body.append(DISCIPLINE + "\n")
    body.append("---\n")
    body.append("## 5. Gaps\n")
    body.append(
        f"Executable binding NOT_ESTABLISHED. Canonical status UNKNOWN/GAP. "
        f"Substantive content pending native-canon source ingestion. "
        f"Validation receipt required before promotion: {RECEIPTS}.\n")
    body.append("---\n")
    body.append("## 6. Worked semantics (target)\n")
    body.append(
        f"Given an operation touching `{top} · {kind}` within the {pname} plane:\n"
        "1. **Admit** — resolve the artifact by id + version; unresolved id ⇒ `UNKNOWN/GAP`, fail closed.\n"
        "2. **Bind scope** — declare domain / regime / H-M-L applicability before any mutation.\n"
        "3. **Check authority** — authority_ref must be epoch-valid; capability alone never authorizes.\n"
        "4. **Validate preconditions** — dependency closure traversed to the smallest result-changing set.\n"
        "5. **Propose** — candidate state is non-authoritative until gates pass (`PROPOSAL ≠ COMMIT`).\n"
        "6. **Commit or hold** — on any failed premise: preserve unaffected state, invalidate dependent descendants only, record receipt.\n")
    body.append("---\n")
    body.append("## 7. Promotion-gate checklist\n")
    body.append(
        "- [ ] substantive content populated from verified native-canon source\n"
        "- [ ] typed schema bound to this artifact\n"
        "- [ ] identity + versioning implemented\n"
        "- [ ] negative cases covered (missing · malformed · stale · unauthorized input)\n"
        "- [ ] provenance edges persisted and validated\n"
        "- [ ] rollback basin demonstrated for consequential effects\n"
        "- [ ] executed validation receipt specific to this artifact\n"
        "- [ ] unresolved critical gaps registered as UNKNOWN/GAP (visible)\n")
    body.append("---\n")
    body.append("## 8. Cross-plane bindings (target)\n")
    body.append(
        "- Governed by canon — [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|AMOS Core Laws]] · [[LAW_HIERARCHY]]\n"
        "- Kernel interaction — [[KERNEL_README]]\n"
        "- Control-plane gates — [[CONTROL_PLANE_README]]\n"
        "- Observed by — [[OBSERVABILITY_README]] · never treated as authority\n"
        "- Recovered via operations — [[OPERATIONS_README]]\n")
    body.append("---\n")
    body.append("[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]\n")
    body.append("---\n")
    body.append("**Related:** [[00_ROOT/00-Home]] · [[AMOS_RSCF_NODES]]\n")
    body.append("---\n")
    body.append("RSCF-NODE\n")
    body.append(f"node_id: {node}\n")
    body.append(f"node_type: {kind.lower()}\n")
    body.append(f"path: {relpath}\n")
    body.append(f"claim_class: {claim_class}\n")
    body.append("rscf_state: placeholder\n")
    body.append("canonical_status: UNKNOWN/GAP\n")
    body.append("RSCF-RELATIONS:\n")
    body.append("  - INDEXED_BY: [[00_ROOT/00-Home]]\n")
    body.append("  - INDEXED_BY: [[AMOS_RSCF_NODES]]\n")
    body.append("  - GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY]]\n")

    return fm + "\n" + "\n".join(body) + "\n"


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
        except Exception as e:  # noqa: BLE001
            errors.append((relpath, str(e)))

    print(f"TOTAL_MANIFEST_ENTRIES: {len(FILES)}")
    print(f"CREATED: {created}")
    print(f"SKIPPED_PRESERVE: {skipped}")
    print(f"DIRS_MADE: {len(dirs_made)}")
    print(f"ERRORS: {len(errors)}")
    if dirs_made:
        print("\n--- directories created ---")
        for d in dirs_made:
            print(f"  {d}")
    if errors:
        print("\n--- errors ---")
        for rp, err in errors:
            print(f"  {rp}: {err}")
    # write report files for verification
    report_dir = os.path.join(ROOT, "scripts", "_add_canon_report")
    os.makedirs(report_dir, exist_ok=True)
    with open(os.path.join(report_dir, "created.txt"), "w") as f:
        f.write("\n".join(created_files))
    with open(os.path.join(report_dir, "skipped.txt"), "w") as f:
        f.write("\n".join(skipped_files))
    with open(os.path.join(report_dir, "dirs_made.txt"), "w") as f:
        f.write("\n".join(dirs_made))
    print(f"\nReports written to {report_dir}/")


if __name__ == "__main__":
    main()
