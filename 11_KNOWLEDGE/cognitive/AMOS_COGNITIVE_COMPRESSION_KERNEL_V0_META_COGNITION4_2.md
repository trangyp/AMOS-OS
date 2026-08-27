---
tags: [canon-group/biology, canon/framework, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/amos-cognitive-compression-kernel-v0, cognitive]
---

{
  "kernel_id": "Cognitive_Compression_Kernel",
  "version": "1.0.0",
  "source": "md/Core/AMOS_Cognitive_Compression_Kernel_v0.md (category: meta_cognition, from AMOS_Omni_KERNEL.json)",
  "description": "Kernel for cognitive compression — reducing complexity while preserving essential structure, finding the minimum sufficient representation, and avoiding information loss in summarization.",
  "group": "Kernels.Meta_Cognition",
  "category": "Meta_Cognition",
  "priority": 9,
  "required": true,
  "domains": ["compression", "summarization", "abstraction", "brevity", "information_theory", "representation"],
  "depends_on": ["Meta_Logic_Kernel", "Meta_Epistemology_Kernel"],
  "meta": {
    "role": "Cognitive Compression Kernel",
    "creator": "Trang Phan (Origin Architect)",
    "status": "defined",
    "binding_rules": ["Law_of_Law", "Rule_of_2", "Rule_of_4", "Absolute_Integrity"],
    "omni_category": "meta_cognition",
    "position": 4
  },
  "purpose": "Compress complex information into minimal sufficient representations without losing essential structural content. This kernel governs how AMOS summarizes, abstracts, and represents information efficiently while preserving what matters.",
  "compression_levels": {
    "raw": "Full detail; everything included; maximum fidelity; maximum size",
    "detailed": "Most detail retained; minor elaboration trimmed; high fidelity; moderate size",
    "structured": "Key structure preserved; examples and elaboration compressed; good fidelity; concise",
    "summary": "Core claims and structure only; supporting detail omitted; moderate fidelity; brief",
    "essence": "Single core insight or claim; everything else dropped; low fidelity; minimal"
  },
  "compression_principles": {
    "minimum_sufficient_representation": "Compress to the smallest representation that preserves all decision-relevant information. Not smaller.",
    "structure_preservation": "Preserve the structural relationships (entities, relations, hierarchies, dependencies) even when examples and elaboration are dropped.",
    "loss_audit": "Every compression must document what was removed and why it was safe to remove. Loss must be explicit, not hidden.",
    "context_sensitive": "Compression level depends on context: decision-making needs structured; quick reference needs summary; exploration needs detailed.",
    "decompressability": "A good compression should allow reconstruction of the essential structure. If you can't decompress, you've lost something."
  },
  "rules": {
    "compress_to_need": "Don't compress below what the task requires. Don't expand above what the task requires.",
    "loss_must_be_explicit": "Never hide what was lost in compression. State what was dropped and why it was safe.",
    "structure_over_fluff": "Preserve entities, relations, claims, and constraints. Drop examples, analogies, rhetorical flourishes, repetition.",
    "truth_preserved_through_compression": "Compression must not change truth values, evidence levels, or burden levels of any claim."
  },
  "functions": {
    "compress_to_level": {
      "description": "Compress information to a specified level",
      "inputs": ["information", "target_level", "decision_context", "what_matters_most"],
      "outputs": ["compressed_representation", "compression_level_applied", "loss_audit", "decompression_guide"]
    },
    "extract_essence": {
      "description": "Extract the single most important insight or claim",
      "inputs": ["complex_information", "purpose_of_extraction"],
      "outputs": ["core_insight", "supporting_structure_reference", "what_was_sacrificed", "when_essence_is_sufficient"]
    },
    "audit_compression_loss": {
      "description": "Audit what was lost in a compression",
      "inputs: ["original", "compressed", "decision_context"],
      "outputs": ["loss_list", "loss_severity", "loss_acceptability", "recommendation_if_unacceptable"]
    }
  },
  "integration": {
    "provides_to": ["Meta_Logic_Kernel", "Analogy_Abstraction_Kernel", "Multi_Perspective_Reasoning_Kernel", "All output generation"],
    "used_by": ["HIE pipeline (S5, S8)", "All summarization tasks", "Memory and retrieval"],
    "routes_to": "ROUTE_DEFAULT (always active when compressing)"
  },
  "safety_constraints": {
    "never_compress_away_decision_critical_information": true,
    "never_hide_compression_loss": true,
    "never_change_claim_meaning_through_compression": true,
    "always_provide_loss_audit": true,
    "always_match_compression_to_context": true
  },
  "evaluation": {
    "unit_tests": [
      "Compress detailed text to summary level: returns summary + loss_audit",
      "Compress to essence: returns core_insight + what_was_sacrificed",
      "Audit compression loss: returns loss_list with severity and acceptability",
      "Compress while preserving truth values: verifies no claim changed"
    ],
    "failure_modes": [
      "Over-compression losing decision-critical info",
      "Hidden loss (no audit provided)",
      "Distorting claims through compression",
      "Under-compression (too verbose for context)"
    ]
  }
}

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
