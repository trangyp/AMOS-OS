---
title: 00 Mode Index MOC
type: moc
source: 03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX
tags:
  - canon/control-plane
  - mode-admission-queue
  - mode-coverage-matrix
  - mode-dependency-graph
  - mode-discovery-queue
  - mode-extension-protocol
  - mode-ontology
  - mode-placeholder-audit-2026-08-25
  - mode-revalidation-schedule
  - mode-transition-matrix
moc: true
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# 00 Mode Index — Map of Content

**Path:** `03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX`
**Files:** 15 | **Subdirectories:** 0

## Purpose

This MOC indexes the mode registry and lifecycle infrastructure for the
AMOS control-plane commit layer. Modes are typed reasoning/execution
states that govern how the system commits, transitions, and validates
cognitive operations. The mode index is the authoritative catalog of all
known modes, their ontological classification, dependency structure,
coverage, and lifecycle queues (discovery, admission, revalidation).

## MECE Domain

**Control Plane dimension — Commit / Mode Lifecycle.**

Within the MECE architecture the control plane owns authority, capability
grants, semantic transactions, and commit/finality eligibility. This MOC
occupies the **mode-lifecycle** slice: it catalogs the ontology of modes,
their transitions, composition rules, and falsifiability registry, ensuring
that every commit-time mode is explicitly registered, dependency-traced,
and coverage-audited rather than implicitly assumed.

## Mode Categories

- **Ontology & Registry** — MODE_ONTOLOGY, MODE_REGISTRY define what a mode
  is and enumerate all known modes.
- **Lifecycle Queues** — MODE_DISCOVERY_QUEUE, MODE_ADMISSION_QUEUE,
  MODE_REVALIDATION_SCHEDULE govern the pipeline from candidate detection
  to validated admission.
- **Structure & Dependencies** — MODE_DEPENDENCY_GRAPH,
  MODE_COMPOSITION_REGISTRY, MODE_TRANSITION_MATRIX map how modes relate,
  compose, and transition.
- **Quality & Coverage** — MODE_COVERAGE_MATRIX, MODE_GAP_REGISTRY,
  MODE_FALSIFIER_REGISTRY, MODE_CONFLICT_REGISTRY track completeness and
  falsifiability.
- **Extension & Audit** — MODE_EXTENSION_PROTOCOL,
  MODE_PLACEHOLDER_AUDIT_2026-08-25 govern how new modes are added and
  audited.

## Files

- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_ADMISSION_QUEUE|MODE_ADMISSION_QUEUE]] — queue of modes awaiting admission approval
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_COMPOSITION_REGISTRY|MODE_COMPOSITION_REGISTRY]] — registry of valid mode compositions
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_CONFLICT_REGISTRY|MODE_CONFLICT_REGISTRY]] — detected conflicts between modes
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_COVERAGE_MATRIX|MODE_COVERAGE_MATRIX]] — matrix of mode coverage across domains
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_DEPENDENCY_GRAPH|MODE_DEPENDENCY_GRAPH]] — directed graph of mode dependencies
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_DISCOVERY_QUEUE|MODE_DISCOVERY_QUEUE]] — queue of newly discovered mode candidates
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_EXTENSION_PROTOCOL|MODE_EXTENSION_PROTOCOL]] — protocol for extending the mode set
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_FALSIFIER_REGISTRY|MODE_FALSIFIER_REGISTRY]] — registry of falsifiers per mode
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_GAP_REGISTRY|MODE_GAP_REGISTRY]] — registry of identified mode gaps
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_INDEX_COMMIT_CONTROL_PLANE_README|MODE_INDEX_COMMIT_CONTROL_PLANE_README]] — README for the mode index commit subdomain
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_ONTOLOGY|MODE_ONTOLOGY]] — ontological definition of what constitutes a mode
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_PLACEHOLDER_AUDIT_2026-08-25|MODE_PLACEHOLDER_AUDIT_2026-08-25]] — audit of placeholder modes as of 2026-08-25
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_REGISTRY|MODE_REGISTRY]] — canonical registry of all admitted modes
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_REVALIDATION_SCHEDULE|MODE_REVALIDATION_SCHEDULE]] — schedule for periodic mode revalidation
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_TRANSITION_MATRIX|MODE_TRANSITION_MATRIX]] — matrix of valid mode-to-mode transitions

## Relationships

- **Parent commit:** [[03_CONTROL_PLANE/09_COMMIT/09_COMMIT_MOC|09_COMMIT_MOC]]
- **Control plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Mode ontology:** [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_ONTOLOGY|MODE_ONTOLOGY]]
- **Mode registry:** [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_REGISTRY|MODE_REGISTRY]]
- **Root navigation:** [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]

## Epistemic Boundary

Mode index artifacts are **DERIVED** from the AMOS corpus. A registered
mode is a documentary claim about a reasoning/execution state type, not
proof that the mode has been executed or validated at runtime.
`REGISTERED != VALIDATED`; `SPECIFIED != EXECUTED`. Placeholder modes
remain explicitly flagged until falsifier evidence is produced.

______________________________________________________________________

**Parent:** [[03_CONTROL_PLANE/09_COMMIT/09_COMMIT_MOC|09_COMMIT_MOC]]
