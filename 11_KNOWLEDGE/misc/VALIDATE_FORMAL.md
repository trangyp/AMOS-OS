---
title: VALIDATE FORMAL
tags: [misc, reference, general]
type: document
source: 11_KNOWLEDGE/misc
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
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
