---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: validate rscf
type: reference
source: 07_SKILLS/amos-rscf-epistemic-master/references
tags:
  - reference
  - amos-rscf-epistemic-master
  - type/skill
  - system-scan-agent
  - automation-profiles
  - amos-simulation-kernel-v0-math-foundations
  - law-hierarchy
  - trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# Validate RSCF

> Source: `_00_Cosmo brain/rscf/validate_rscf.md`
> Epistemic class: SOURCE_DERIVED

______________________________________________________________________

## tags: [rscf]

## validate_rscf

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

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS · SYSTEM_SCAN_AGENT · AUTOMATION_PROFILES

______________________________________________________________________

## **MOC:** references_MOC

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-rscf-epistemic-master-validate-rscf
node_type: reference
path: 07_SKILLS/amos-rscf-epistemic-master/references/validate_rscf.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
