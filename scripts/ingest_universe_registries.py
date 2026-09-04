#!/usr/bin/env python3
"""
Ingest and convert AMOS-UNIVERSE master JSON registries into rich canonical AMOS Markdown files.
"""

import os, json
from pathlib import Path

vault = Path('/Users/mac/Library/CloudStorage/GoogleDrive-phanqtrang@gmail.com/My Drive/_AMOS_OS')
drive = Path('/Users/mac/Library/CloudStorage/GoogleDrive-phanqtrang@gmail.com/My Drive')
u_dir = drive / 'AMOS-UNIVERSE'

def write_md(rel_path, content):
    p = vault / rel_path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content.strip() + '\n', encoding='utf-8')
    print(f"[INGESTED] {rel_path}")

# 1. automation_profiles.json -> 11_KNOWLEDGE/stubs/automation_profiles.md & 07_SKILLS/AUTOMATION_PROFILES.md
if (u_dir / 'automation_profiles.json').exists():
    data = json.load(open(u_dir / 'automation_profiles.json'))
    md = """---
title: "AMOS Automation Profiles Master Registry"
type: registry
source: 11_KNOWLEDGE
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_REGISTRY
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - AMOS-UNIVERSE/automation_profiles.json
  scope: automation_profiles
tags:
  - amos-os
  - automation
  - profiles
  - workflows
---

# AMOS Automation Profiles Master Registry

> **Origin Architect / Steward:** Trang Phan  
> **AMOS_CORE Target:** `v4.4`  
> **Conclusion Class:** `AMOS_MODEL`

## 1. Profiles Specification

```json
""" + json.dumps(data, indent=2) + """
```

## 2. Integration & Execution

- **Governed By:** [[08_WORKFLOWS/08_WORKFLOWS_MOC|08_WORKFLOWS_MOC]]
- **Executed In:** [[04_RUNTIME/RUNTIME_README|RUNTIME_README]]
"""
    write_md('11_KNOWLEDGE/stubs/automation_profiles.md', md)
    write_md('08_WORKFLOWS/AUTOMATION_PROFILES.md', md)

# 2. amos_modes.json -> 21_DOMAINS/45_MODES/AMOS_MODES_REGISTRY.md & 11_KNOWLEDGE/stubs/amos_modes.md
if (u_dir / 'amos_modes.json').exists():
    data = json.load(open(u_dir / 'amos_modes.json'))
    md = """---
title: "AMOS Modes Master Registry"
type: registry
source: 21_DOMAINS/45_MODES
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_REGISTRY
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - AMOS-UNIVERSE/amos_modes.json
  scope: amos_modes
tags:
  - amos-os
  - modes
  - cognitive-modes
---

# AMOS Modes Master Registry

> **Origin Architect / Steward:** Trang Phan  
> **AMOS_CORE Target:** `v4.4`  
> **Conclusion Class:** `AMOS_MODEL`

## 1. Operating Modes

```json
""" + json.dumps(data, indent=2) + """
```

## 2. Cross-Plane Bindings

- **Organism Modes:** [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]]
- **Domain Mapping:** [[21_DOMAINS/00_INDEX/DOMAIN_EXTENSION_PROTOCOL|DOMAIN_EXTENSION_PROTOCOL]]
"""
    write_md('21_DOMAINS/45_MODES/AMOS_MODES_REGISTRY.md', md)
    write_md('11_KNOWLEDGE/stubs/amos_modes.md', md)

# 3. canonical_body_registry.json -> 01_CANON/02_UNIVERSE_CANON/CANONICAL_BODY_REGISTRY.md & 11_KNOWLEDGE/stubs/canonical_body_registry.md
if (u_dir / 'canonical_body_registry.json').exists():
    data = json.load(open(u_dir / 'canonical_body_registry.json'))
    md = """---
title: "AMOS Canonical Body Master Registry"
type: registry
source: 01_CANON/02_UNIVERSE_CANON
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_REGISTRY
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - AMOS-UNIVERSE/canonical_body_registry.json
  scope: universe_canon_bodies
tags:
  - amos-os
  - canon
  - bodies
  - universe-canon
---

# AMOS Canonical Body Master Registry

> **Origin Architect / Steward:** Trang Phan  
> **AMOS_CORE Target:** `v4.4`  
> **Conclusion Class:** `AMOS_MODEL`

## 1. Canonical Bodies Specification

```json
""" + json.dumps(data, indent=2) + """
```

## 2. Universal Integration

- **Universe Canon:** [[01_CANON/02_UNIVERSE_CANON/02_UNIVERSE_CANON_MOC|02_UNIVERSE_CANON_MOC]]
- **Cognitive Organs:** [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]]
"""
    write_md('01_CANON/02_UNIVERSE_CANON/CANONICAL_BODY_REGISTRY.md', md)
    write_md('11_KNOWLEDGE/stubs/canonical_body_registry.md', md)

# 4. AMOS_CANONICAL_GLOSSARY.json -> 01_CANON/06_GLOSSARY/AMOS_CANONICAL_GLOSSARY_EXPANDED.md
if (u_dir / 'AMOS_CANONICAL_GLOSSARY.json').exists():
    data = json.load(open(u_dir / 'AMOS_CANONICAL_GLOSSARY.json'))
    md = """---
title: "AMOS Canonical Glossary — Comprehensive Terms"
type: glossary
source: 01_CANON/06_GLOSSARY
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_GLOSSARY
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - AMOS-UNIVERSE/AMOS_CANONICAL_GLOSSARY.json
  scope: canonical_glossary
tags:
  - amos-os
  - canon
  - glossary
  - definitions
---

# AMOS Canonical Glossary — Comprehensive Terms

> **Origin Architect / Steward:** Trang Phan  
> **AMOS_CORE Target:** `v4.4`  
> **Conclusion Class:** `AMOS_MODEL`

## 1. Canonical Terminology

```json
""" + json.dumps(data, indent=2) + """
```

## 2. Glossary Index

- **Glossary MOC:** [[01_CANON/06_GLOSSARY/06_GLOSSARY_MOC|06_GLOSSARY_MOC]]
- **Root Map:** [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
"""
    write_md('01_CANON/06_GLOSSARY/AMOS_CANONICAL_GLOSSARY_EXPANDED.md', md)

print("Universe registries ingested successfully!")
