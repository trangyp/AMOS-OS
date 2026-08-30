---
title: ios reverse engineering
type: reference
source: 07_SKILLS/amos-security-safety-master/references
tags:
- reference
- amos-security-safety-master
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

# iOS Reverse Engineering

> Source: `_00_Cosmo brain/engine/I/iOS_Reverse_Engineering.md`
> Epistemic class: SOURCE_DERIVED

---
tags: [engine]
---
# iOS Reverse Engineering — part 2
- iOS/Android app is a binary
- Few more steps in comparison to web testing
- jail-break iOS / root Android first
   	- most apps have detection for this
   	- you need to bypass that before you test
   	- checkrain, bootrain, uncover applications for jail breaking
   	- exploit something in bootloader, inject the exploit (respring) -> can't restart the phone after that
- Once jailbroken, it installs Cydia.
   	- Package manager/app store
- Equivallent to Cydia in Android is Magisk
- Certificate pinning
   	- Cert list in browser
   	- install your own root CA -> browser thinks you are safe.
   	- hard coding an expected cert into the binary
   	- certain apps will only send traffic to approved servers -> hard code your own cert to sit and MNM -> allows you to intercept traffic
   	- on iOS -> iOS SSL kill switch, Liberty
- Decompilation
   	- IOS is hard
   	- Ida (paid/expensive tool for reverse enginerring)
   	- Ghidra (open source equivalent by RSA)
- Reversing application binary
   	- jail-break / root device
   	- decompile (easy in android, way harder for iOS)
   	*

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS · SYSTEM_SCAN_AGENT · AUTOMATION_PROFILES

---
**MOC:** references_MOC
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-security-safety-master-ios-reverse-engineering
node_type: reference
path: 07_SKILLS/amos-security-safety-master/references/ios_reverse_engineering.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
