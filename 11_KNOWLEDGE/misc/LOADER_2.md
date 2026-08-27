---
title: LOADER 2
tags: [misc]
type: note
source: 11_KNOWLEDGE/misc
---


"""LEGACY: Central loader/registry for AMOS brain frameworks.

Canonical framework handling now lives under ``amos_system.frameworks`` and
the OMEGA brain engines/specs. This module is retained for reference only.
"""

from __future__ import annotations

from typing import Any, Dict, Tuple

FRAMEWORK_REGISTRY: Dict[str, Tuple[str, str]] = {
    "academic_writing_kernal_engine_v0": (
        "AMOS_Academic_Writing_Kernal_Engine_v0.json",
        ".frameworks.academic_writing_kernal_engine_v0",
    ),
    "audit_quality_engine_v0": (
        "AMOS_Audit_Quality_Engine_v0.json",
        ".frameworks.audit_quality_engine_v0",
    ),
    "automation_kernel_v0": (
        "AMOS_Automation_Kernel_v0.json",
        ".frameworks.automation_kernel_v0",
    ),
    "bizfin_pack_v0": (
        "AMOS_BIZFIN_Pack_v0.json",
        ".frameworks.bizfin_pack_v0",
    ),
    "bizfin_engine_v0": (
        "AMOS_Bizfin_Engine_v0.json",
        ".frameworks.bizfin_engine_v0",
    ),
    "brain_master_os_v0": (
        "AMOS_Brain_Master_Os_v0.json",
        ".frameworks.brain_master_os_v0",
    ),
    "coding_engine_v0": (
        "AMOS_Coding_Engine_v0.json",
        ".frameworks.coding_engine_v0",
    ),
    "coding_kernel_v0": (
        "AMOS_Coding_Kernel_v0.json",
        ".frameworks.coding_kernel_v0",
    ),
    "cognition_engine_v0": (
        "AMOS_Cognition_Engine_v0.json",
        ".frameworks.cognition_engine_v0",
    ),
    "consciousness_engine_v0": (
        "AMOS_Consciousness_Engine_v0.json",
        ".frameworks.consciousness_engine_v0",
    ),
    "design_engine_v0": (
        "AMOS_Design_Engine_v0.json",
        ".frameworks.design_engine_v0",
    ),
    "design_kernel_v0": (
        "AMOS_Design_Kernel_v0.json",
        ".frameworks.design_kernel_v0",
    ),
    "documentation_kernel_v0": (
        "AMOS_Documentation_Kernel_v0.json",
        ".frameworks.documentation_kernel_v0",
    ),
    "emotion_engine_v0": (
        "AMOS_Emotion_Engine_v0.json",
        ".frameworks.emotion_engine_v0",
    ),
    "engineering_math_kernel_v0": (
        "AMOS_Engineering_Math_Kernel_v0.json",
        ".frameworks.engineering_math_kernel_v0",
    ),
    "gov_pack_v0": (
        "AMOS_GOV_Pack_v0.json",
        ".frameworks.gov_pack_v0",
    ),
    "gov_engine_v0": (
        "AMOS_Gov_Engine_v0.json",
        ".frameworks.gov_engine_v0",
    ),
    "human_pack_v0": (
        "AMOS_HUMAN_Pack_v0.json",
        ".frameworks.human_pack_v0",
    ),
    "human_engine_v0": (
        "AMOS_Human_Engine_v0.json",
        ".frameworks.human_engine_v0",
    ),
    "human_intelligence_engine_v0": (
        "AMOS_Human_Intelligence_Engine_v0.json",
        ".frameworks.human_intelligence_engine_v0",
    ),
    "max_expanded": (
        "AMOS_MAX_EXPANDED.json",
        ".frameworks.max_expanded",
    ),
    "medical_clinical_kernel_v0": (
        "AMOS_Medical_Clinical_Kernel_v0.json",
        ".frameworks.medical_clinical_kernel_v0",
    ),
    "mind_os_v0": (
        "AMOS_Mind_Os_v0.json",
        ".frameworks.mind_os_v0",
    ),
    "national_brain_engine_v0": (
        "AMOS_National_Brain_Engine_v0.json",
        ".frameworks.national_brain_engine_v0",
    ),
    "national_brain_pack_v0": (
        "AMOS_National_Brain_Pack_v0.json",
        ".frameworks.national_brain_pack_v0",
    ),
    "os_agent_v0": (
        "AMOS_Os_Agent_v0.json",
        ".frameworks.os_agent_v0",
    ),
    "personality_engine_v0": (
        "AMOS_Personality_Engine_v0.json",
        ".frameworks.personality_engine_v0",
    ),
    "quantum_stack_v0": (
        "AMOS_Quantum_Stack_v0.json",
        ".frameworks.quantum_stack_v0",
    ),
    "science_engine_v0": (
        "AMOS_Science_Engine_v0.json",
        ".frameworks.science_engine_v0",
    ),
    "scientific_kernel_v0": (
        "AMOS_Scientific_Kernel_v0.json",
        ".frameworks.scientific_kernel_v0",
    ),
    "species_interaction_core_engine_v0": (
        "AMOS_Species_Interaction_Core_Engine_v0.json",
        ".frameworks.species_interaction_core_engine_v0",
    ),
    "tech_architecture_kernel_v0": (
        "AMOS_Tech_Architecture_Kernel_v0.json",
        ".frameworks.tech_architecture_kernel_v0",
    ),
    "tech_expanded_design_engine_v0": (
        "AMOS_Tech_Expanded_Design_Engine_v0.json",
        ".frameworks.tech_expanded_design_engine_v0",
    ),
    "tech_quantum_engine_v0": (
        "AMOS_Tech_Quantum_Engine_v0.json",
        ".frameworks.tech_quantum_engine_v0",
    ),
    "unified_coding_engine_v0": (
        "AMOS_Unified_Coding_Engine_v0.json",
        ".frameworks.unified_coding_engine_v0",
    ),
    "vietnamese_writing_engine_v0": (
        "AMOS_Vietnamese_Writing_Engine_v0.json",
        ".frameworks.vietnamese_writing_engine_v0",
    ),
    "vn_legal_engine_v0": (
        "AMOS_Vn_Legal_Engine_v0.json",
        ".frameworks.vn_legal_engine_v0",
    ),
    "vomni_kernel_v0": (
        "AMOS_Vomni_Kernel_v0.json",
        ".frameworks.vomni_kernel_v0",
    ),
}


def list_frameworks() -> list[str]:
    """Return a sorted list of legacy framework identifiers."""
    return sorted(FRAMEWORK_REGISTRY.keys())

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
