---
title: 10 Routing MOC
type: moc
source: 25_COGNITIVE_MATRIX/10_ROUTING
tags:
  - 10-routing
  - domain/cognitive-matrix
  - binding-rules
  - routing-audit
  - routing-policy
moc: true
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# 10 Routing — Map of Content

## Purpose

The Routing sub-plane governs the **cognitive routing layer** of the AMOS Cognitive Matrix. It defines how a cognitive request — an observation to process, a decision to make, an effect to authorize — is routed through the matrix's primitives, scales, control planes, and cells to reach the appropriate processing surface. Routing is the connective tissue of the matrix: without it, cognitive requests would have no path from entry to resolution. The routing system ensures that every request passes through the required governance gates in the correct order, respecting dependency ordering, scale banding, and control-plane authority.

## MECE Domain

This sub-plane belongs to the **C — Cognitive Capability & Orchestration** MECE domain (plane `25_COGNITIVE_MATRIX`). The Cognitive Matrix is the fractal coordinate and routing decomposition layer. Routing is the active navigation surface within the matrix: it uses the structural maps provided by the Index, the dependency topology from the Dependency Graph, and the scale banding from Scales to compute the path a cognitive request must follow.

**Path:** `25_COGNITIVE_MATRIX/10_ROUTING`
**Files:** 5 | **Subdirectories:** 1

## Files

- [[25_COGNITIVE_MATRIX/10_ROUTING/BINDING_RULES|BINDING_RULES]] — The rules that bind a cognitive request to its routing path. Binding rules determine which primitives, control planes, and scales a request must traverse based on its type, consequence class, and authority requirements. A binding rule is a declarative specification: "requests of type X with consequence level Y must traverse control plane Z at scale H."
- [[25_COGNITIVE_MATRIX/10_ROUTING/COGNITIVE_MATRIX_ROUTING_CONTRACT|COGNITIVE_MATRIX_ROUTING_CONTRACT]] — The governed contract defining how routing paths are declared, validated, enforced, and audited within the Cognitive Matrix. Specifies the interface between the routing system and the cognitive organism's request dispatch, the control plane's governance gates, and the dependency graph's ordering constraints.
- [[25_COGNITIVE_MATRIX/10_ROUTING/ROUTING_AUDIT|ROUTING_AUDIT]] — The audit process that verifies routing integrity: checks that all declared routing paths are valid (no dead ends, no cycles, no missing gates), that binding rules are consistent with dependency ordering, and that no routing path bypasses a required governance gate. Audit failures are registered as structural gaps.
- [[25_COGNITIVE_MATRIX/10_ROUTING/ROUTING_COGNITIVE_MATRIX_README|ROUTING_COGNITIVE_MATRIX_README]] — Package readme for the Routing sub-plane. Describes the structural layout, file inventory, and the role of cognitive routing within the Cognitive Matrix.
- [[25_COGNITIVE_MATRIX/10_ROUTING/ROUTING_POLICY|ROUTING_POLICY]] — The policy layer that governs routing decisions: which routing paths are active, which are deprecated, which require authority override, and how routing conflicts are resolved when multiple paths are eligible. Routing policy is evaluated at request dispatch time and can dynamically alter the routing path based on current system state.

## Subdirectories

- [[25_COGNITIVE_MATRIX/10_ROUTING/00_INDEX/ROUTING_MAP|ROUTING_MAP]] — `00_INDEX` — structural navigation map for the Routing sub-plane.

## Routing Pipeline

The cognitive routing pipeline operates as follows:

1. **Request intake** — A cognitive request enters the matrix with a type (observation, decision, effect), consequence class, and authority context.
2. **Binding** — `BINDING_RULES` match the request to its required routing path: which primitives to invoke, which control planes to traverse, and which scale band to apply.
3. **Policy evaluation** — `ROUTING_POLICY` evaluates whether the bound path is active, deprecated, or requires override. Policy may redirect the request to an alternative path if the primary path is unavailable.
4. **Path traversal** — The request traverses the bound path, passing through each required governance gate in dependency-respecting order (validated against the [[25_COGNITIVE_MATRIX/09_DEPENDENCY_GRAPH/09_DEPENDENCY_GRAPH_MOC|Dependency Graph]]).
5. **Audit** — `ROUTING_AUDIT` records the traversed path for post-hoc verification that no gates were bypassed.

## Relationships

- **Parent**: [[25_COGNITIVE_MATRIX/25_COGNITIVE_MATRIX_MOC|25 Cognitive Matrix MOC]] — the parent plane for the fractal cognitive coordinate system.
- **Dependency Graph**: [[25_COGNITIVE_MATRIX/09_DEPENDENCY_GRAPH/09_DEPENDENCY_GRAPH_MOC|09 Dependency Graph MOC]] — routing paths must respect dependency ordering.
- **Scales**: [[25_COGNITIVE_MATRIX/04_SCALES/04_SCALES_MOC|04 Scales MOC]] — routing binds requests to scale bands.
- **Control Planes**: [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/03_CONTROL_PLANES_MOC|03 Control Planes MOC]] — routing paths traverse control-plane gates.
- **Structural Gaps**: [[25_COGNITIVE_MATRIX/08_STRUCTURAL_GAPS/08_STRUCTURAL_GAPS_MOC|08 Structural Gaps MOC]] — routing audit failures are registered as gaps.
- **Validation**: [[25_COGNITIVE_MATRIX/11_VALIDATION/11_VALIDATION_MOC|11 Validation MOC]] — validates that routing paths are complete and correct.
- **Cognitive Organism**: [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05 Cognitive Organism MOC]] — the organism whose cognitive requests are routed.
- **Control Plane**: [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03 Control Plane MOC]] — the governance gates that routing paths traverse.
- **Architecture**: [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|Full Brain OS MECE Architecture]] — assigns `25_COGNITIVE_MATRIX` to the cognitive capability domain.

## Epistemic Boundary

Routing artifacts are AMOS_MODEL with DERIVED claim class. The binding rules, routing policy, and audit process are governance specifications, not empirical claims that a deployed runtime routes every request through the declared path. `DOCUMENTED != IMPLEMENTED` — a declared routing path does not prove that the runtime dispatcher enforces it. Routing bypass (a request reaching an effect gate without traversing the required control-plane gates) is a known risk that the `ROUTING_AUDIT` is designed to detect but cannot fully eliminate without runtime enforcement. The separability law applies: `ROUTING != ENFORCEMENT` — routing declares the path; enforcement guarantees it is followed.

______________________________________________________________________

**Parent:** [[25_COGNITIVE_MATRIX/25_COGNITIVE_MATRIX_MOC|25_COGNITIVE_MATRIX_MOC]]
