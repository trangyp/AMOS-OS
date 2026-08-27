---
title: IOS REVERSE ENGINEERING
tags: [engine, processing, runtime, canon/knowledge]
type: document
source: 11_KNOWLEDGE/engine
rscf:
  state: AMOS_MODEL
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: engine_specification

---


# iOS Reverse Engineering
* iOS/Android app is a binary
* Few more steps in comparison to web testing
* Jailbreak iOS / root android first
   	* most apps have detection for this
   	* you need to bypass that before you test
   	* checkrain, bootrain, uncover applications for jail breaking
   	* exploit something in bootloader, inject the exploit (respring) -> can't restart the phone after that
* Once jailbroken, it installs Cydia.
   	* Package manager/app store
* Equivallent to Cydia in Android is Magisk
* Certificate pinning
   	* Cert list in browser
   	* install your own root CA -> browser thinks you are safe.
   	* hard coding an expected cert into the binary
   	* certain apps will only send traffic to approved servers -> hard code your own cert to sit and MNM -> allows you to intercept traffic
   	* on iOS -> iOS SSL kill switch, Liberty
* Decompilation
   	* IOS is hard
   	* Ida (paid/expensive tool for reverse enginerring)
   	* Ghidra (open source equivalent by RSA)
* Reversing application binary
   	* Jailbreak/ root device
   	* decompile (easy in android, way harder for iOS)
   	*

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[ENGINE_MOC]]

---
**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
