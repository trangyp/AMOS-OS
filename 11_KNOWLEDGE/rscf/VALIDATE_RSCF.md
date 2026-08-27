---
tags: [rscf]
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
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
