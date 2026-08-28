---
title: CAUSAL
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


# CAUSAL

LEVEL={"descriptive":0,"association":1,"correlation":2,"enabling":3,
       "mediator":4,"confounder":4,"mechanism":5,"intervention_effect":6}

class CausalGraph:
    def __init__(self): self.edges=[]
    def add(self,a,b,kind,evidence_level=0,scope="unspecified",regime="unspecified"):
        self.edges.append({"a":a,"b":b,"kind":kind,"evidence_level":evidence_level,"scope":scope,"regime":regime})
    def licensed(self,kind,evidence_level): return evidence_level>=LEVEL.get(kind,0)
    def ancestors(self,node):
        out=set(); changed=True
        while changed:
            changed=False
            for e in self.edges:
                if e["b"]==node or e["b"] in out:
                    if e["a"] not in out: out.add(e["a"]); changed=True
        return out

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]