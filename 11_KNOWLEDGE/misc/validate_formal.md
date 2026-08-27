---
tags: [misc]
---
# validate_formal

```python
#!/usr/bin/env python3
import json,sys
REQ={"object_id","object_type","class","invariants","scope","regime","provenance"}
def main():
    if len(sys.argv)!=2:
        print("usage: validate_formal.py object.json"); return 2
    x=json.load(open(sys.argv[1],encoding="utf-8"))
    missing=REQ-set(x)
    if missing:
        print("INVALID missing:",sorted(missing)); return 1
    if x["class"] not in {"VERIFIED","DERIVED","MODEL","CONDITIONAL","COMPETING","UNKNOWN/GAP"}:
        print("INVALID class"); return 1
    if not isinstance(x["invariants"],list) or not x["invariants"]:
        print("INVALID invariants"); return 1
    print("VALID formal object"); return 0
if __name__=="__main__": raise SystemExit(main())


```

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
