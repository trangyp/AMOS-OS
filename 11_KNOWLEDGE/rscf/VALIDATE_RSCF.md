---
title: VALIDATE RSCF
tags: [rscf, epistemic, claim, canon/knowledge]
type: document
source: 11_KNOWLEDGE/rscf
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: epistemic_framework

---


# validate_rscf

```python
#!/usr/bin/env python3
import json, sys
REQ={"claim_id","claim","class","premises","evidence","scope","regime","dependencies","falsifiers","confidence_ceiling"}
CLASSES={"VERIFIED","DERIVED","MODEL","CONDITIONAL","COMPETING","UNKNOWN/GAP"}
def main():
    if len(sys.argv)!=2:
        print("usage: validate_rscf.py capsule.json"); return 2
    x=json.load(open(sys.argv[1],encoding="utf-8"))
    missing=REQ-set(x)
    if missing:
        print("INVALID missing:",sorted(missing)); return 1
    if x["class"] not in CLASSES:
        print("INVALID class"); return 1
    c=x["confidence_ceiling"]
    if not isinstance(c,(int,float)) or not 0<=c<=1:
        print("INVALID confidence_ceiling"); return 1
    print("VALID RSCF capsule"); return 0
if __name__=="__main__": raise SystemExit(main())


```

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[rscf_MOC]]
