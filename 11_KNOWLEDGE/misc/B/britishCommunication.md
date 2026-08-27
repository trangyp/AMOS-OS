---
tags: [misc]
---
// British Communication Pack
import { PackItem, PackCategory } from "../masterPacks";

export const britishCommunicationPack: PackItem = {
  id: "british_communication",
  name: "British Communication",
  category: PackCategory.CulturalIntelligence,
  children: [
    { id: "sarcasm", name: "sarcasm", category: PackCategory.CulturalIntelligence },
    { id: "understatement", name: "understatement", category: PackCategory.CulturalIntelligence },
    { id: "indirect_criticism", name: "indirect criticism", category: PackCategory.CulturalIntelligence },
    { id: "dry_humor", name: "dry humor", category: PackCategory.CulturalIntelligence },
  ],
};

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
