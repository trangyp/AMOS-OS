---
title: VIETNAMESECOMMUNICATION
tags:
- misc
- reference
- general
- canon/knowledge
type: note
source: 11_KNOWLEDGE/misc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# VIETNAMESECOMMUNICATION

// Vietnamese Communication Pack
import { PackItem, PackCategory } from "../masterPacks";

export const vietnameseCommunicationPack: PackItem = {
  id: "vietnamese_communication",
  name: "Vietnamese Communication",
  category: PackCategory.CulturalIntelligence,
  children: [
    { id: "face_saving", name: "face-saving", category: PackCategory.CulturalIntelligence },
    { id: "indirect_disagreement", name: "indirect disagreement", category: PackCategory.CulturalIntelligence },
    { id: "relational_positioning", name: "relational positioning", category: PackCategory.CulturalIntelligence },
  ],
};

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]