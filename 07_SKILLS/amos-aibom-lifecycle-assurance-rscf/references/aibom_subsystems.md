---
title: aibom subsystems
type: reference
tags: [reference, amos-aibom-lifecycle-assurance-rscf]
---

# AIBOM Subsystem Map (Gaps 101-110)

> Source: `cosmo-brain/AMOS_OS_KERNEL/amos/governance/aibom.py`
> Epistemic class: SOURCE_CANON

## 10 Subsystems

| # | Subsystem | Function |
|---|-----------|----------|
| 101 | AIBOMBuilder | Complete manifest of models, data, code, libs, config |
| 102 | DependencyGraph | Transitive dependency graph with cycle detection |
| 103 | RuntimeFingerprinter | Execution environment fingerprint |
| 104 | BOMComponentRegistry | Typed components with source hashes |
| 105 | OutputBinder | Outputs bound to runtime fingerprint |
| 106 | VulnerabilityIntelligence | Ongoing CVE/security status for dependencies |
| 107 | ArtifactSigner | Cryptographic identity for production artifacts |
| 108 | OutputProvenance | Prove which runtime produced an important artifact |
| 109 | DependencyRevocation | Compromised dependency invalidates downstream outputs |
| 110 | ReproducibilityVerifier | Independent build reproduces artifact identity |

## Gate Behavior

The AIBOMGovernor aggregates all subsystems into a gate that `AmosKernel.run()` evaluates.
It ensures every task execution has a valid AIBOM with no unpatched critical vulnerabilities
before proceeding.

- **PASS**: AIBOM complete, all dependencies traced, no critical vulnerabilities
- **CONDITIONAL**: Pending falsifier access or unverified component
- **FAIL**: Unpatched critical vulnerability, missing AIBOM, or compromised dependency

## Component Types

- MODEL: Trained model with weights, architecture, training data reference
- DATA: Dataset with source, version, hash, license
- CODE: Source code with repository, commit hash, build hash
- LIBRARY: Third-party library with version, hash, CVE status
- CONFIG: Configuration with version, hash, environment binding

---
**MOC:** [[references_MOC]]
