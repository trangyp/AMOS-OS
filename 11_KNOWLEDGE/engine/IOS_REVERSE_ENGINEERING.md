---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Ios Reverse Engineering
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# iOS Reverse Engineering

- iOS/Android app is a binary
- Few more steps in comparison to web testing
- Jailbreak iOS / root android first
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
  - Jailbreak/ root device
  - decompile (easy in android, way harder for iOS)
  *

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS · SYSTEM_SCAN_AGENT · AUTOMATION_PROFILES

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/engine/ENGINE_MOC|ENGINE_MOC]]

______________________________________________________________________

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
