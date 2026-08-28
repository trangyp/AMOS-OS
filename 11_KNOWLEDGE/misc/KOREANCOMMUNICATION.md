---
title: KOREANCOMMUNICATION
tags: [misc, reference, general, canon/knowledge]
type: note
source: 11_KNOWLEDGE/misc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# KOREANCOMMUNICATION

// Korean Communication Pack
import { PackItem, PackCategory } from "../masterPacks";

export const koreanCommunicationPack: PackItem = {
  id: "korean_communication",
  name: "Korean Communication",
  category: PackCategory.CulturalIntelligence,
  children: [
    { id: "age_hierarchy", name: "age hierarchy", category: PackCategory.CulturalIntelligence },
    { id: "emotional_calibration", name: "emotional calibration", category: PackCategory.CulturalIntelligence },
    { id: "workplace_politeness", name: "workplace politeness", category: PackCategory.CulturalIntelligence },
  ],
};

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]