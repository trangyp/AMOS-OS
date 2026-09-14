# AIBOM assurance boundaries

## State separation

Let `M` be one AIBOM manifest and define boolean structural predicates:

- `S`: schema/typed-state validity
- `R`: declared root component exists
- `H`: recorded digests are syntactically valid and sealed manifest hash matches canonical content
- `L`: recorded relationship endpoints are present
- `A`: attestation subjects bind to recorded component digests
- `G`: every claimed `VERIFIED_EXTERNAL` signature has verifier identity, version and evidence reference
- `V`: vulnerability records bind to known components and valid applicability states

The local structural gate is the logical conjunction

`I(M) := S ∧ R ∧ H ∧ L ∧ A ∧ G ∧ V`.

This is an AMOS reference-runtime definition, not a universal AIBOM standard.

## Policy completeness

For policy dimensions `P={attestation, verified_signature, vulnerability_evidence, environment_identity, output_binding, replay_evidence}`, let `q_p(M)` be true when either dimension `p` is not required or its required evidence is present.

`C_P(M) := ∧_{p in P} q_p(M)`.

`I(M)` and `C_P(M)` are intentionally distinct. A manifest may satisfy `I(M)=true` while `C_P(M)=false`.

## Vulnerability applicability

For tri-state inputs `V` (version match), `G` (configuration match), and `C` (component present):

- if any input is unknown, return `UNKNOWN`;
- otherwise `APPLICABLE := V ∧ G ∧ C`;
- otherwise return `NOT_APPLICABLE`.

Do not infer absence of vulnerability from scanner silence.

## Reproducibility closure

Use vector

`r(M) = (inventory, environment, model_lineage, runtime_capture, output_binding, replay)`.

The reference runtime defines `closed(M)` as the conjunction of all vector entries. Do not compress missing dimensions into one score when repair or attribution needs their identity.

## Identity topology

A minimal lifecycle topology is:

`source -> build artifact -> sealed AIBOM -> runtime execution -> output`

with separately typed side evidence for dependencies, model/data lineage, configuration, attestations, vulnerabilities, traces and evaluations.

Do not infer a missing edge from temporal adjacency.

## Firewalls

- `DIGEST_MATCH != SIGNATURE_VERIFIED`
- `SIGNATURE_VERIFIED != SEMANTIC_CORRECTNESS`
- `ATTESTATION_PRESENT != ATTESTATION_VERIFIED`
- `PROVENANCE_VERIFIED != REPRODUCIBLE`
- `BUILD_ATTESTATION != RUNTIME_IDENTITY`
- `OUTPUT_BOUND != OUTPUT_CORRECT`
- `AIBOM_SEALED != POLICY_COMPLETE`
- `POLICY_COMPLETE != DEPLOYMENT_VALIDITY`
- `AIBOM_EVIDENCE != AUTHORITY`
