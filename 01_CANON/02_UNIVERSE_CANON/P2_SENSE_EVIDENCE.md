Below is the **full replacement content** for:

`01_CANON/02_UNIVERSE_CANON/P2_SENSE_EVIDENCE.md`

`P2 Sense / Evidence` should be the Universe Canon plane that governs **how external state becomes admissible evidence inside AMOS**. P1 establishes that reality/environment is not identical to the internal world model; P2 defines the intervening epistemic pipeline: sensing, observation, reporting, measurement, extraction, provenance, calibration, uncertainty, independence, contradiction, evidence fusion, falsification, and admission into RSCF reasoning. It must explicitly prevent source claims, model outputs, repeated copies, or generated summaries from masquerading as independent observations. That separation follows the Full Brain operating rules.  The declared primary Full Brain source remains `AMOS_FULL_BRAIN_OS.json`; preserving AMOS structures does not establish external empirical validity. 

````md
---
id: AMOS-CANON-U-P2-SENSE-EVIDENCE
title: "AMOS OS — P2 Sense / Evidence"

tags:
  - canon
  - universe_canon
  - sense
  - evidence
  - observation
  - measurement
  - provenance
  - uncertainty
  - validation
  - epistemics
  - rscf
  - hml
  - note

origin_architect: "Trang Phan"
artifact_type: "universe_canon_plane"

class: "CANON_MODEL"
conclusion_class: "DERIVED"
canon_status: "CONDITIONAL"
validation_status: "ARCHITECTURE_DEFINED"
implementation_status: "PARTIAL_OR_UNKNOWN"
empirical_status: "NOT_ESTABLISHED_BY_THIS_ARTIFACT"
gap_status: "OPEN"

path: "01_CANON/02_UNIVERSE_CANON/P2_SENSE_EVIDENCE.md"

parent:
  - "01_CANON"
  - "01_CANON/02_UNIVERSE_CANON"

contract:
  - "CANON_UNIVERSE_CANON_CONTRACT.md"

upstream:
  - "P1_REALITY_ENVIRONMENT.md"

related:
  - "00_ROOT/00_ROOT_MOC.md"
  - "00_ROOT/00_ROOT_REGISTRY.md"
  - "00_ROOT/00_ROOT_PROVENANCE.md"
  - "00_ROOT/00_ROOT_STATUS.md"
  - "00_ROOT/00_ROOT_LIFECYCLE.md"
  - "02_KERNEL/03_CAUSAL"
  - "02_KERNEL/09_INTEGRATION"
  - "07_PROVENANCE"
  - "09_DEPENDENCY_GRAPH"
  - "11_VALIDATION"
  - "18_OBSERVABILITY"
  - "21_DOMAINS"
  - "22_RESEARCH"
  - "AMOS_RSCF_NODES"

scope:
  - sensing
  - evidence
  - observation
  - measurement
  - source_claims
  - reports
  - instruments
  - telemetry
  - sensors
  - documents
  - datasets
  - experiments
  - tests
  - model_outputs
  - provenance
  - evidence_topology
  - source_ancestry
  - independence
  - correlation
  - sybil_hardening
  - calibration
  - error
  - noise
  - uncertainty
  - hidden_state
  - missingness
  - confidence
  - freshness
  - evidence_fusion
  - contradiction
  - falsification
  - evidence_admission
  - evidence_rejection
  - evidence_decay
  - revalidation
  - observation_context
  - regime
  - evidence_scope

hard_rule: "EVIDENCE MUST REMAIN TYPED, PROVENANCE-AWARE, SCOPE-BOUNDED, AND INDEPENDENCE-AWARE"

RSCF-NODE:
  node_id: p2_sense_evidence
  node_type: note
  claim_class: AMOS_MODEL

RSCF-RELATIONS:
  - "INDEXED_BY: [[00-Home]]"
  - "INDEXED_BY: [[AMOS_RSCF_NODES]]"
  - "DEPENDS_ON: [[P1_REALITY_ENVIRONMENT]]"
---

# P2 Sense / Evidence

**Class:** `CANON_MODEL`

**Origin architect / steward:** Trang Phan

**Architecture status:** `DEFINED`

**Canon status:** `CONDITIONAL`

**Empirical status:** `NOT ESTABLISHED BY THIS ARTIFACT`

---

# 1. Purpose

`P2 Sense / Evidence` defines how AMOS converts contact with reality, sources, measurements, tools, observations, and reports into typed evidence suitable for reasoning.

P2 answers:

```text
What was sensed?

What was observed?

What was merely reported?

What was measured?

What instrument or source produced it?

What transformation occurred before AMOS received it?

How old is it?

What uncertainty applies?

What scope does it support?

What regime was active?

What calibration supports it?

Is it direct evidence or derived evidence?

Are apparently different sources actually independent?

Do they share ancestry?

Was a model output mistaken for observation?

Was a summary mistaken for a source?

What contradicts the evidence?

What would falsify the interpretation?

How strong may downstream confidence become?

When does evidence become stale?

When must evidence be revalidated?

When should evidence be rejected or quarantined?
````

Its governing function is:

```text
REALITY / ENVIRONMENT
        ↓
SENSING
        ↓
OBSERVATION
        ↓
MEASUREMENT / REPORT
        ↓
PROVENANCE
        ↓
EVIDENCE TYPING
        ↓
QUALITY / SCOPE / FRESHNESS
        ↓
INDEPENDENCE ANALYSIS
        ↓
RSCF-ELIGIBLE EVIDENCE
```

---

# 2. Foundational Boundary

P1 establishes:

```text
REALITY
!=
MODEL_OF_REALITY
```

P2 adds:

```text
REALITY
!=
OBSERVATION
```

and:

```text
OBSERVATION
!=
EVIDENCE INTERPRETATION
```

Therefore:

```text
R
→ Observation(R)
→ EvidenceRepresentation
→ ModelUpdate
```

contains multiple transformations.

Each must remain visible.

---

# 3. Sense Definition

Within AMOS, `Sense` is the acquisition interface through which a system receives information about a state not already contained in its active internal representation.

Conceptually:

```text
Sense:
ExternalState
→
InternalSignal
```

This is an architecture-level abstraction.

It does not imply literal biological senses.

---

# 4. Sense Is Interface-Dependent

A sensing channel may be:

```text
human observation

instrument

sensor

API

document

database

telemetry stream

experiment

tool result

user report

image

audio

event log
```

The meaning and reliability of the resulting evidence depend on the channel.

---

# 5. AMOS Capability Boundary

AMOS should only claim observations available through:

```text
provided context

authorized tools

explicit data

connected evidence sources
```

The Full Brain operating contract does not imply unrestricted sensing, embodiment, or private-data access. 

Therefore:

```text
NO ACCESS
!=
NEGATIVE OBSERVATION
```

and:

```text
NOT RETRIEVED
!=
NOT PRESENT
```

---

# 6. Evidence Definition

Evidence is:

```text
a provenance-bearing information object
that can support,
challenge,
constrain,
or falsify
a claim within a declared scope.
```

Evidence is claim-relative.

The same observation may be strong evidence for one claim and weak evidence for another.

---

# 7. Evidence Is Not Truth

Mandatory:

```text
EVIDENCE
!=
TRUTH
```

Evidence changes rational support.

It does not automatically prove a conclusion.

---

# 8. Evidence Is Not Claim

```text
EVIDENCE
!=
CLAIM
```

Example:

```text
Observation:
temperature = 38.2°C
```

is different from:

```text
Claim:
the system is overheating.
```

The second requires interpretation, thresholds, scope, and model assumptions.

---

# 9. Evidence Is Not Explanation

```text
EVIDENCE
!=
MECHANISM
```

Seeing two variables co-vary does not identify why they co-vary.

---

# 10. P2 Evidence Classes

P2 should distinguish at minimum:

```text
DIRECT_OBSERVATION

MEASUREMENT

SOURCE_CLAIM

REPORT

TEST_RESULT

EXPERIMENT_RESULT

DATASET_RECORD

TELEMETRY

DOCUMENTARY_EVIDENCE

DERIVED_EVIDENCE

MODEL_OUTPUT

SIMULATION_OUTPUT

VALIDATION_RESULT

NEGATIVE_EVIDENCE

ABSENCE_OF_EVIDENCE

UNKNOWN
```

---

# 11. DIRECT_OBSERVATION

Information obtained directly through an available observation interface.

Still subject to:

```text
observer limitations

instrument limitations

sampling

context

interpretation
```

---

# 12. MEASUREMENT

An observation mapped onto a defined quantity or category through a measurement procedure.

Measurement should ideally specify:

```text
variable

unit

instrument

method

calibration

time

error
```

---

# 13. SOURCE_CLAIM

A claim asserted by a source.

Example:

```text
Document X states Y.
```

This establishes strongly that:

```text
X asserted Y
```

but not necessarily that:

```text
Y is true.
```

---

# 14. REPORT

A statement describing an alleged observation, event, state, or result.

Reports may be:

```text
first-hand

second-hand

aggregated

institutional

automated
```

and must preserve that distinction.

---

# 15. TEST_RESULT

Output of a defined test.

A test result is evidence only for properties that the test actually measures.

---

# 16. EXPERIMENT_RESULT

Result from an intervention or experimental protocol.

Its strength depends on:

```text
design

controls

measurement

sample

confounding

analysis

replication
```

---

# 17. DATASET_RECORD

A record from a dataset.

Dataset evidence requires provenance to:

```text
collection

transformation

labeling

version

sampling
```

where material.

---

# 18. TELEMETRY

Runtime or operational observations.

Examples:

```text
latency

memory usage

failure count

sensor state

request rate

system health
```

Telemetry is time- and environment-sensitive.

---

# 19. DOCUMENTARY_EVIDENCE

Evidence contained in:

```text
documents

contracts

papers

logs

policies

records

archives
```

Document existence and document claims must be separated.

---

# 20. DERIVED_EVIDENCE

Evidence produced through transformation of upstream evidence.

Examples:

```text
aggregation

statistical analysis

feature extraction

summary

classification

inference
```

Derived evidence inherits upstream limitations.

---

# 21. MODEL_OUTPUT

Prediction or inference generated by a model.

Mandatory:

```text
MODEL_OUTPUT
!=
OBSERVATION
```

unless the model output is itself the object being observed.

---

# 22. SIMULATION_OUTPUT

State generated inside a simulation.

Mandatory:

```text
SIMULATION_OUTPUT
!=
EXTERNAL EMPIRICAL EVIDENCE
```

It may support:

```text
model behavior

consistency

possibility

sensitivity analysis
```

but not automatically real-world truth.

---

# 23. VALIDATION_RESULT

Evidence concerning whether a target satisfies a defined validator.

Validation remains scoped to:

```text
target

version

profile

environment

time
```

---

# 24. NEGATIVE_EVIDENCE

Evidence that tends to disconfirm or reduce support for a claim.

Example:

```text
Claim predicts event X.

High-sensitivity measurement fails to observe X.
```

This may be meaningful negative evidence.

---

# 25. ABSENCE OF EVIDENCE

Failure to possess evidence.

Mandatory:

```text
ABSENCE_OF_EVIDENCE
!=
EVIDENCE_OF_ABSENCE
```

unless detection conditions make non-observation informative.

---

# 26. UNKNOWN Evidence Class

If evidence type cannot be established:

```text
evidence_class: UNKNOWN
```

Do not infer evidence strength from formatting, file type, or source reputation alone.

---

# 27. Observation Object

Recommended:

```yaml
observation:

  observation_id: null

  target: null

  variable: null

  observed_value: null

  observed_at: null

  observer_or_instrument: null

  method: null

  unit: null

  uncertainty: null

  environment: null

  regime: null

  provenance: []

  calibration_ref: null

  raw_ref: null
```

---

# 28. Evidence Object

Recommended:

```yaml
evidence:

  evidence_id: null

  evidence_class: null

  claim_refs: []

  content_ref: null

  source_id: null

  source_version: null

  observation_ref: null

  method: null

  scope: null

  regime: null

  captured_at: null

  freshness: null

  uncertainty: {}

  provenance: []

  ancestors: []

  correlation_group: null

  independence_status: null

  transformations: []

  quality_flags: []

  falsifier_relevance: []

  status: null
```

---

# 29. Observation Identity

Each important observation should have a stable ID.

This allows AMOS to distinguish:

```text
same observation reused
```

from:

```text
independent observation repeated.
```

---

# 30. Evidence Identity

Evidence identity should survive:

```text
format conversion

movement

indexing

citation

summarization
```

where logical evidence identity remains unchanged.

---

# 31. Raw vs Processed Evidence

Mandatory:

```text
RAW_EVIDENCE
!=
PROCESSED_EVIDENCE
```

Processed evidence should link back to raw evidence where available.

---

# 32. Raw Evidence

Closest recoverable representation to the original observation or source output.

Examples:

```text
sensor reading

original transcript

original dataset row

raw test output

original document
```

---

# 33. Processed Evidence

May include:

```text
cleaned data

normalized values

aggregated metrics

summaries

feature vectors

classified observations
```

---

# 34. Transformation Visibility

Every material processing step should remain visible.

Conceptually:

```text
Raw
→ Cleaned
→ Normalized
→ Aggregated
→ Interpreted
```

Each step can introduce error.

---

# 35. Evidence Transformation Object

```yaml
evidence_transformation:

  transformation_id: null

  input_evidence: []

  output_evidence: null

  operation: null

  actor_or_tool: null

  version: null

  assumptions: []

  lossiness: null

  semantic_change: null

  performed_at: null
```

---

# 36. Sense Channel

A sense channel represents a route through which evidence enters AMOS.

Examples:

```text
S_visual

S_audio

S_document

S_sensor

S_api

S_database

S_user_report

S_runtime

S_experiment
```

These names are architectural abstractions.

---

# 37. Sense Channel Contract

Each channel should ideally define:

```text
input type

observable variables

resolution

latency

error

access boundary

calibration

failure modes
```

---

# 38. Channel Coverage

A channel can only observe part of reality.

Mandatory:

```text
SENSOR COVERAGE
!=
REALITY COVERAGE
```

---

# 39. Blind Region

A channel has a blind region when relevant states cannot be observed through it.

Represent:

```text
Blind(SenseChannel)
```

where consequential.

---

# 40. Resolution

Resolution defines the smallest distinguishable difference or structural detail for a sensing method.

Insufficient resolution can merge distinct states.

---

# 41. Sensitivity

Sensitivity concerns ability to detect a target when it exists.

---

# 42. Specificity

Specificity concerns ability to reject non-target states.

---

# 43. False Positive

Measurement/sensor indicates a state that is absent.

---

# 44. False Negative

Measurement/sensor fails to detect a state that exists.

---

# 45. Detection Threshold

Some observation systems only detect states above:

```text
θ_detect
```

Non-observation below the threshold is not evidence of absence.

---

# 46. Dynamic Range

A sensor may fail:

```text
below lower bound

above saturation limit
```

Both matter.

---

# 47. Saturation

When sensor output stops meaningfully increasing despite stronger input.

Saturation can hide important state variation.

---

# 48. Calibration

Calibration binds instrument output to a reference.

Conceptually:

```text
ObservedValue
→ CalibrationMapping
→ EstimatedQuantity
```

---

# 49. Calibration Object

```yaml
calibration:

  calibration_id: null

  instrument_id: null

  reference_standard: null

  method: null

  performed_at: null

  valid_until: null

  error_model: null

  provenance: []
```

---

# 50. Calibration Freshness

A previously calibrated instrument can drift.

Therefore:

```text
CALIBRATED_ONCE
!=
CALIBRATED_FOREVER
```

---

# 51. Instrument Drift

Sensor/instrument characteristics can change over time.

Possible causes:

```text
wear

temperature

software update

aging

environment

configuration
```

---

# 52. Measurement Error

P2 should distinguish:

```text
systematic error

random error

sampling error

instrument error

processing error

labeling error

transcription error

model error
```

---

# 53. Systematic Error

Bias consistently shifts observations.

Repeated measurements do not eliminate it.

---

# 54. Random Error

Variation around the target quantity/state.

May decrease with repeated independent measurement under suitable assumptions.

---

# 55. Sampling Error

Observed sample differs from target population/state.

---

# 56. Processing Error

Transformation introduces distortion.

Examples:

```text
wrong normalization

truncation

unit conversion error

schema mismatch

aggregation error
```

---

# 57. Label Error

Recorded category differs from target truth/category.

Important in:

```text
datasets

classification tasks

human annotation
```

---

# 58. Missing Data

Missingness should be typed where material.

Possible:

```text
missing completely at random

missing conditionally

missing structurally

unknown missingness mechanism
```

Do not assume missing values are neutral.

---

# 59. Missingness Bias

Absence of records may correlate with the phenomenon being measured.

This can distort evidence.

---

# 60. Evidence Noise

Noise is variation not carrying relevant signal for the target inference.

Noise classification is claim-relative.

---

# 61. Signal

Signal is variation carrying information relevant to the target claim.

---

# 62. Signal-to-Noise

Conceptually:

```text
SNR
=
RelevantSignal
/
EffectiveNoise
```

Exact metrics remain domain-specific.

---

# 63. Signal Below Noise

If decision-relevant difference is smaller than measurement uncertainty:

```text
CONCLUSION STRENGTH
MUST BE LIMITED.
```

---

# 64. Evidence Scope

Every evidence object should specify what it can support.

Possible dimensions:

```text
population

system

environment

scale

time

regime

measurement method

version
```

---

# 65. Scope Inheritance

A derived claim cannot silently expand evidence scope.

```text
Evidence:
system A under regime R
```

does not establish:

```text
all systems in all regimes.
```

---

# 66. Regime Binding

Evidence obtained under one regime may not transfer to another.

Example:

```text
benchmark in laboratory
```

does not automatically imply:

```text
production performance.
```

---

# 67. Temporal Binding

Evidence may be valid only within a time range.

Examples:

```text
market conditions

software behavior

legal rules

ecological state

deployment configuration
```

---

# 68. Freshness

P2 evidence should carry a freshness state where time matters.

Suggested:

```text
CURRENT

AGING

STALE

HISTORICAL

TIME_INVARIANT_WITHIN_SCOPE

UNKNOWN
```

---

# 69. Evidence Decay

Some evidence loses decision value over time.

Conceptually:

```text
EvidenceUtility(t)
↓
```

as the world changes.

No universal decay equation is assumed.

---

# 70. Historical Evidence

Old evidence can remain valid for historical claims even if stale for current decisions.

---

# 71. Source Identity

Each evidence item should identify its source.

Source identity should not be inferred solely from:

```text
URL

file path

display name
```

when stronger provenance is available.

---

# 72. Source Version

Evidence derived from a mutable source should bind the exact source version or timestamp where relevant.

---

# 73. Source Type

Possible:

```text
PRIMARY

SECONDARY

TERTIARY

MIRROR

AGGREGATOR

MODEL_GENERATED

USER_SUPPLIED

INSTRUMENT

DATABASE

UNKNOWN
```

---

# 74. Primary Source

Closest recoverable origin for the relevant claim or observation.

Primary is claim-relative.

---

# 75. Secondary Source

Reports, analyzes, interprets, or summarizes primary material.

---

# 76. Mirror

Replica of another source.

Mandatory:

```text
MIRROR
!=
INDEPENDENT SOURCE
```

---

# 77. Aggregator

Combines other sources.

Its apparent multiplicity may hide shared ancestry.

---

# 78. Model-Generated Source

Content generated by a model.

It should retain provenance to:

```text
inputs

model/tool

generation process
```

where consequential.

---

# 79. User-Supplied Source

Material supplied by the user.

AMOS may treat it as authoritative for:

```text
what the user supplied
```

but should not independently verify external factual claims unless requested and evidence exists.

---

# 80. Evidence Provenance

Minimum:

```yaml
provenance:

  source_id: null

  source_version: null

  origin_ref: null

  parent_evidence: []

  transformation_chain: []

  captured_at: null

  actor_or_tool: null
```

---

# 81. Evidence Ancestry

Evidence may derive from other evidence.

Example:

```text
Sensor A
→ Database B
→ Dashboard C
→ Report D
```

These are four representations but may contain one observation lineage.

---

# 82. Common-Ancestor Detection

Before treating evidence as independent:

```text
find shared ancestors.
```

---

# 83. Independence Status

Suggested:

```text
INDEPENDENT

PARTIALLY_INDEPENDENT

SHARED_ANCESTRY

CORRELATED

DEPENDENT

UNKNOWN
```

---

# 84. Independence Must Be Demonstrated

Mandatory:

```text
MULTIPLE SOURCES
!=
INDEPENDENT SOURCES
```

---

# 85. Correlation Sources

Evidence may correlate because of:

```text
shared raw data

shared instrument

shared reporter

shared organization

shared model

shared preprocessing

shared assumptions

common event
```

---

# 86. Correlation Group

Recommended:

```yaml
correlation_group:

  group_id: null

  common_ancestor: null

  members: []

  shared_mechanism: null

  correlation_risk: null
```

---

# 87. Sybil Evidence Problem

One source can be copied into many apparently distinct sources.

Example:

```text
Original claim
→ article
→ repost
→ generated summary
→ forum quote
```

Naive counting gives:

```text
5 sources
```

Proper provenance analysis may reveal:

```text
1 original lineage.
```

---

# 88. Sybil-Hardening Rule

```text
SOURCE COUNT
MUST NOT SUBSTITUTE
FOR INDEPENDENT LINEAGE COUNT.
```

---

# 89. Evidence Family

Evidence sharing a meaningful origin may be grouped into one family for support accounting.

---

# 90. Independent Confirmation

Independent confirmation requires sufficiently independent:

```text
observation

data

measurement path

analysis path

source ancestry
```

relative to the claim.

---

# 91. Replication

Replication should distinguish:

```text
same data reanalysis

same experiment rerun

independent experiment

independent institution

independent method
```

These have different evidential value.

---

# 92. Same-Data Replication

Can test analysis robustness.

It does not provide independent data.

---

# 93. Independent Data Replication

Stronger evidence for generality when scope matches.

---

# 94. Methodological Independence

Different measurement methods converging may reduce shared-method bias.

---

# 95. Triangulation

Triangulation combines materially different evidence paths.

Example:

```text
instrument measurement

independent observational dataset

mechanistic prediction
```

where each addresses the claim through a different route.

---

# 96. Evidence Fusion

Evidence fusion combines compatible evidence without erasing provenance or correlation.

Conceptually:

```text
EvidenceSet
→
CompatibilityCheck
→
IndependenceCheck
→
ScopeCheck
→
Fusion
```

---

# 97. Evidence Fusion Boundary

Do not average incompatible evidence merely because numbers are available.

Check:

```text
same variable?

same unit?

same population?

same regime?

same measurement definition?
```

---

# 98. Evidence Conflict

Evidence conflicts when two evidence items imply incompatible states within the same relevant scope.

---

# 99. Apparent Conflict

May result from:

```text
different times

different scales

different units

different definitions

different populations

different regimes
```

Resolve these before declaring contradiction.

---

# 100. Genuine Evidence Conflict

If evidence remains incompatible after alignment:

```text
preserve CONFLICTING / COMPETING
```

rather than selecting one for fluency.

---

# 101. Conflict Object

```yaml
evidence_conflict:

  conflict_id: null

  evidence_a: null
  evidence_b: null

  target_claim: null

  scope_alignment: null
  regime_alignment: null
  temporal_alignment: null

  possible_explanations: []

  discriminating_test: null

  status: OPEN
```

---

# 102. Evidence Challenge

For consequential evidence ask:

```text
Could the source be wrong?

Could the measurement be miscalibrated?

Could the data be stale?

Could the evidence share ancestry with supposed corroboration?

Could processing introduce bias?

Could scope differ?

Could the measurement capture a proxy rather than the target?

Could the result be confounded?

Could missing data change interpretation?
```

---

# 103. Measurement Target

P2 should distinguish:

```text
construct
```

from:

```text
measurement proxy.
```

Example:

```text
"trust"
```

may be represented by a survey score.

Mandatory:

```text
PROXY
!=
TARGET CONSTRUCT
```

---

# 104. Operationalization

A claim becomes empirically testable only when terms map to observable procedures.

Operationalization should specify:

```text
what is measured

how

with what threshold

under which conditions
```

---

# 105. Proxy Validity

A proxy must be validated for the use being made of it.

---

# 106. Construct Drift

The meaning of a metric may change across environments or populations.

---

# 107. Measurement Invariance

Cross-group or cross-regime comparison may require showing that the measurement represents the same construct comparably.

---

# 108. Unit Discipline

Measured quantities should preserve units.

Mandatory:

```text
5 kg
+
3 seconds
```

is invalid without a transformation producing commensurate quantities.

---

# 109. Unit Metadata

Recommended:

```yaml
measurement:
  value: null
  unit: null
  unit_system: null
  conversion_ref: null
```

---

# 110. Normalization

Normalized values should retain mapping to original units/range.

```text
normalized value
!=
unitless semantic equivalence.
```

---

# 111. Threshold Evidence

Threshold-based decisions should state:

```text
threshold value

source

justification

measurement error

sensitivity around threshold
```

---

# 112. Borderline Evidence

If measurement uncertainty overlaps decision threshold:

```text
CONDITIONAL
```

or additional measurement may be required.

---

# 113. Evidence Quality Dimensions

P2 should assess quality across multiple dimensions rather than one universal score.

Potential dimensions:

```text
relevance

directness

measurement quality

provenance integrity

independence

freshness

coverage

resolution

replicability

scope compatibility
```

---

# 114. No Universal Evidence Score

Mandatory:

```text
ONE NUMBER
CANNOT ALWAYS REPRESENT
ALL EVIDENCE QUALITY DIMENSIONS.
```

---

# 115. Evidence Uncertainty Vector

Recommended:

```yaml
uncertainty:

  measurement: null

  sampling: null

  source: null

  processing: null

  model: null

  scope: null

  temporal: null

  regime: null

  provenance_independence: null
```

---

# 116. Confidence Ceiling

Downstream confidence cannot exceed load-bearing evidence support.

Conceptually:

```text
C_claim
≤
min(
  C_evidence,
  C_provenance,
  C_measurement,
  C_scope,
  C_freshness
)
```

where these dimensions are load-bearing.

---

# 117. Derived Evidence Ceiling

A summary cannot become more reliable than the evidence it summarizes merely through better wording.

---

# 118. Evidence Multiplication Boundary

```text
COPYING EVIDENCE
DOES NOT MULTIPLY
INDEPENDENT SUPPORT.
```

---

# 119. Source Reputation

Source reputation may inform priors or scrutiny.

It cannot override contradictory direct evidence automatically.

---

# 120. Authority Boundary

A source may be authoritative for:

```text
its own policy

its own data

its own decision
```

without being authoritative for unrelated external claims.

---

# 121. Popularity Boundary

```text
MANY PEOPLE SAY X
```

is evidence of:

```text
many people saying X
```

not necessarily evidence that `X` is true.

---

# 122. Consensus

Consensus may be meaningful when built from genuinely independent expertise/evidence.

But consensus should retain:

```text
domain

method

time

scope
```

---

# 123. Benchmark Evidence

Benchmark result must include where material:

```text
benchmark version

dataset

hardware

software

configuration

metric

baseline

run conditions
```

---

# 124. Benchmark Boundary

```text
BENCHMARK SUCCESS
!=
UNIVERSAL PERFORMANCE
```

---

# 125. Runtime Evidence

Runtime evidence is especially environment-sensitive.

Example:

```text
latency = 10 ms
```

requires:

```text
hardware

load

network

dataset/request profile

measurement interval
```

for meaningful generalization.

---

# 126. Experimental Evidence

Experimental evidence should capture:

```text
hypothesis

protocol

intervention

control

measurement

sample

analysis

result
```

---

# 127. Observational Evidence

Observation without intervention can support:

```text
association

distribution

temporal pattern
```

but causal claims need more discipline.

---

# 128. Causal Evidence

Causal evidence may arise from:

```text
randomized experiment

natural experiment

validated intervention design

strong mechanistic evidence

appropriate causal identification
```

depending on domain.

---

# 129. Causal Firewall

Mandatory:

```text
OBSERVATION
+
SEQUENCE
+
CORRELATION
!=
CAUSATION
```

---

# 130. Confounding

A third variable may explain apparent association.

Represent:

```text
C
→ A
C
→ B
```

rather than assuming:

```text
A → B.
```

---

# 131. Mediation

A causal path may operate through intermediate variable:

```text
A
→ M
→ B
```

---

# 132. Feedback

Evidence may reflect:

```text
A → B
```

and:

```text
B → A.
```

Static correlation can obscure feedback.

---

# 133. Selection Bias

Observed evidence may differ because inclusion into the dataset depends on the target variables.

---

# 134. Survivorship Bias

Only surviving/visible cases may be observed.

---

# 135. Reporting Bias

Evidence may be more likely to appear when results are:

```text
interesting

positive

politically useful

commercially favorable
```

---

# 136. Publication Bias

Published literature may overrepresent significant/positive results.

---

# 137. Confirmation Bias

Reasoner may preferentially select evidence supporting an existing model.

P2 should actively search for disconfirming evidence for consequential claims.

---

# 138. Adversarial Evidence Search

For important conclusions:

```text
find strongest support
↓
find strongest contradiction
↓
compare provenance
↓
compare independence
↓
compare scope
↓
retain weakest accurate conclusion class
```

---

# 139. Falsifier

A falsifier is evidence condition that would undermine a claim.

Every consequential empirical model should expose falsifiers where possible.

---

# 140. Falsifier Object

```yaml
falsifier:

  falsifier_id: null

  claim_id: null

  expected_observation: null

  measurement_method: null

  threshold: null

  scope: null

  regime: null
```

---

# 141. Failed Prediction

If a model makes a clear prediction and evidence contradicts it:

```text
model support must decrease
```

unless the failure can be traced to an invalid test condition.

---

# 142. Prediction Specificity

A model that predicts almost any outcome is weakly falsifiable.

---

# 143. Prospective Evidence

Evidence defined before outcome is observed is stronger against hindsight adaptation.

---

# 144. Retrospective Evidence

Can still be useful but is more vulnerable to:

```text
selection

overfitting

post-hoc explanation
```

---

# 145. Data Leakage

Prediction/test evidence is invalidated when information from evaluation data leaked into model construction in a way that defeats the test.

---

# 146. Training/Test Independence

For machine-learning validation:

```text
training data
```

and:

```text
evaluation data
```

should have appropriate independence.

---

# 147. Test Contamination

Repeated reuse of one benchmark can produce hidden overfitting.

---

# 148. Evidence Reuse

Reusing evidence across conclusions is allowed.

But confidence calculations must account for shared dependence.

---

# 149. Evidence Dependency

A conclusion may depend on multiple evidence objects.

The dependency graph should record load-bearing relations where material.

---

# 150. Evidence Admission State

Suggested:

```text
CANDIDATE

ADMITTED

ADMITTED_WITH_CONDITIONS

QUARANTINED

REJECTED

STALE

SUPERSEDED

UNKNOWN
```

---

# 151. Candidate Evidence

Discovered but not yet sufficiently typed or provenance-resolved.

---

# 152. Admitted Evidence

Meets requirements for its declared use.

---

# 153. Admitted With Conditions

Usable only under explicit limitations.

---

# 154. Quarantined Evidence

Potentially valuable but currently unsafe to rely upon because of:

```text
hash mismatch

provenance conflict

unknown manipulation

calibration failure

scope ambiguity
```

---

# 155. Rejected Evidence

Not admissible for the intended claim/use.

Rejection should preserve reason.

---

# 156. Stale Evidence

Previously valid but no longer fresh enough for current use.

---

# 157. Superseded Evidence

A corrected or more authoritative version exists.

Historical evidence remains addressable.

---

# 158. Evidence Admission Gate

Before admitting consequential evidence:

```text
resolve identity
↓
classify evidence
↓
resolve source
↓
resolve provenance
↓
check transformation
↓
check measurement
↓
check scope
↓
check regime
↓
check freshness
↓
check independence
↓
check contradiction
↓
admit / condition / quarantine / reject
```

---

# 159. Evidence Admission Object

```yaml
evidence_admission:

  evidence_id: null

  status: null

  intended_claims: []

  checks:
    identity: null
    provenance: null
    measurement: null
    scope: null
    regime: null
    freshness: null
    independence: null
    contradiction: null

  conditions: []

  admitted_at: null
```

---

# 160. Revalidation

Evidence should be revalidated when:

```text
source changes

instrument changes

calibration expires

environment changes

regime changes

processing pipeline changes

critical contradiction appears

version changes
```

---

# 161. Evidence Revocation

If evidence is discovered to be invalid:

```text
REVOKE
↓
TRACE DEPENDENT CLAIMS
↓
CHECK INDEPENDENT SUPPORT
↓
DOWNGRADE ONLY UNSUPPORTED DESCENDANTS
```

---

# 162. Local Invalidation

Core law:

```text
BAD EVIDENCE
DOES NOT INVALIDATE
UNRELATED CLAIMS.
```

---

# 163. Evidence Supersession

A corrected dataset/report should preserve:

```text
old version

new version

correction

reason

effective time
```

---

# 164. Evidence Repair

If provenance or metadata is incomplete:

```text
recover source
↓
recover version
↓
recover transformation
↓
reassess support
```

Do not fabricate missing lineage.

---

# 165. P2 H/M/L Structure

P2 can be applied recursively:

```text
H:
evidence architecture / epistemic strategy

M:
evidence channels, datasets, validation systems

L:
individual observation or measurement
```

---

# 166. H-Level Evidence

Examples:

```text
body of scientific evidence

multi-source operational state

institutional evidence ecosystem
```

---

# 167. M-Level Evidence

Examples:

```text
specific experiment family

sensor network

dataset

monitoring subsystem
```

---

# 168. L-Level Evidence

Examples:

```text
one measurement

one document statement

one observation

one log event
```

---

# 169. H/M/L Independence Warning

Many L-level observations may belong to one M-level source lineage.

Counting them as independent H-level confirmation can be wrong.

---

# 170. Evidence Topology

P2 should reason about topology:

```text
evidence nodes

source nodes

transformation nodes

common ancestors

dependency edges

contradiction edges
```

not merely evidence lists.

---

# 171. Evidence Graph Edges

Suggested:

```text
OBSERVED_BY

REPORTED_BY

MEASURED_BY

DERIVED_FROM

TRANSFORMED_BY

SUPPORTS

CHALLENGES

FALSIFIES

CORRELATED_WITH

SHARES_ANCESTOR_WITH

SUPERSEDES

VALIDATED_BY
```

---

# 172. Evidence Support Edge

```text
Evidence E
SUPPORTS
Claim C
```

must be scope-aware.

---

# 173. Challenge Edge

```text
Evidence E
CHALLENGES
Claim C
```

does not necessarily falsify it completely.

---

# 174. Falsification Edge

Reserved for evidence satisfying the declared invalidation condition strongly enough within scope.

---

# 175. Evidence Contradiction Graph

Conflicts should remain explicit rather than being hidden during synthesis.

---

# 176. Evidence Query

Conceptual operations:

```text
GET_EVIDENCE(claim)

GET_RAW_EVIDENCE(id)

TRACE_EVIDENCE_SOURCE(id)

TRACE_EVIDENCE_ANCESTRY(id)

CHECK_EVIDENCE_FRESHNESS(id)

CHECK_EVIDENCE_SCOPE(id)

CHECK_EVIDENCE_INDEPENDENCE(set)

FIND_CONTRADICTING_EVIDENCE(claim)

FIND_FALSIFIERS(claim)
```

---

# 177. Evidence Fast Path

Existing evidence may be reused without full re-analysis only when:

```text
same target claim

same scope

same regime

source unchanged

freshness valid

provenance valid

independence assumptions unchanged

no new contradiction
```

---

# 178. Evidence Escalation

Escalate validation when:

```text
stakes high

evidence weak

evidence stale

sources conflict

provenance uncertain

causality claimed

irreversible action depends on result

regime changed
```

---

# 179. P2 RSCF Contract

Important conclusions should reference evidence through RSCF:

```yaml
rscf:

  claim: null

  claim_class: null

  evidence:
    - evidence_id: null
      role: SUPPORT
      independence_status: null

  provenance: []

  scope: null

  regime: null

  freshness: null

  dependencies: []

  competing: []

  falsifiers: []

  uncertainty:
    measurement: null
    source: null
    model: null
    scope: null
    temporal: null
    causal: null
    provenance_independence: null

  confidence_ceiling: null
```

---

# 180. Evidence Sufficiency

Evidence is sufficient when it supports the level of conclusion required for the current objective.

Therefore:

```text
EVIDENCE SUFFICIENCY
IS DECISION-RELATIVE.
```

---

# 181. Claim Sufficiency

A descriptive question may need less evidence than:

```text
irreversible deployment

medical decision

legal claim

financial action

canon promotion
```

---

# 182. Action Sufficiency

Even with uncertainty, action may be justified if:

```text
cost of waiting is high

action is reversible

downside bounded

monitoring exists
```

This is a decision-layer rule, not evidence inflation.

---

# 183. Strong Evidence / Weak Action Boundary

Strong evidence does not automatically authorize action.

Mandatory:

```text
EVIDENCE
!=
AUTHORITY
```

---

# 184. Weak Evidence / Safe Experiment

Weak evidence may justify:

```text
low-risk experiment
```

while not justifying:

```text
irreversible commitment.
```

---

# 185. Evidence Archive

Superseded or stale evidence should remain historically recoverable.

---

# 186. Evidence Tombstone

If evidence must be removed:

```yaml
evidence_tombstone:

  evidence_id: null

  removed_at: null

  reason: null

  replacement: null

  authority_ref: null
```

where allowed.

---

# 187. P2 Invariants

## Typing invariant

```text
every consequential evidence object has a type
```

## Provenance invariant

```text
load-bearing evidence retains source lineage
```

## Observation invariant

```text
observation != interpretation
```

## Model invariant

```text
model output != observation
```

## Independence invariant

```text
independence must be demonstrated
```

## Scope invariant

```text
evidence cannot silently expand scope
```

## Regime invariant

```text
cross-regime use requires validation
```

## Freshness invariant

```text
dynamic evidence expires
```

## Causal invariant

```text
association does not become causation
```

## Contradiction invariant

```text
conflicting evidence remains visible
```

## Local invalidation invariant

```text
revoked evidence invalidates only dependent conclusions
```

## Gap invariant

```text
missing evidence remains UNKNOWN/GAP
```

---

# 188. P2 State Variables

Conceptual variables may include:

```text
E_q      = evidence quality vector

E_f      = evidence freshness

E_u      = uncertainty vector

E_i      = independence status

E_c      = correlation risk

E_s      = scope compatibility

E_r      = regime compatibility

E_m      = measurement reliability

E_p      = provenance integrity

E_cov    = coverage

E_res    = resolution

E_lat    = observation latency
```

These are architecture variables, not validated universal scalar metrics.

---

# 189. P2 Operators

Architecture-level semantic operators:

```text
SENSE()

OBSERVE()

MEASURE()

REGISTER_OBSERVATION()

REGISTER_EVIDENCE()

CLASSIFY_EVIDENCE()

TRACE_SOURCE()

TRACE_ANCESTRY()

CHECK_CALIBRATION()

CHECK_UNITS()

CHECK_ERROR()

CHECK_FRESHNESS()

CHECK_SCOPE()

CHECK_REGIME()

CHECK_INDEPENDENCE()

GROUP_CORRELATED_EVIDENCE()

DETECT_CONTRADICTION()

SEARCH_DISCONFIRMING_EVIDENCE()

REGISTER_FALSIFIER()

ADMIT_EVIDENCE()

QUARANTINE_EVIDENCE()

REJECT_EVIDENCE()

SUPERSEDE_EVIDENCE()

REVOKE_EVIDENCE()

TRACE_DEPENDENT_CLAIMS()

AUDIT_EVIDENCE()
```

These are semantic contracts, not claims of implemented runtime functions.

---

# 190. P2 Workflow — Sense

```text
DEFINE TARGET
↓
SELECT CHANNEL
↓
OBSERVE
↓
CAPTURE RAW STATE
↓
REGISTER TIME / METHOD
↓
REGISTER PROVENANCE
↓
TYPE OBSERVATION
```

---

# 191. P2 Workflow — Measurement

```text
DEFINE VARIABLE
↓
DEFINE UNIT
↓
SELECT INSTRUMENT
↓
CHECK CALIBRATION
↓
MEASURE
↓
CAPTURE ERROR
↓
STORE RAW RESULT
↓
REGISTER EVIDENCE
```

---

# 192. P2 Workflow — Source Claim

```text
READ SOURCE
↓
IDENTIFY EXACT CLAIM
↓
REGISTER SOURCE VERSION
↓
CLASSIFY SOURCE
↓
TRACE ANCESTRY
↓
PRESERVE AS SOURCE_CLAIM
↓
SEEK EXTERNAL SUPPORT IF NEEDED
```

---

# 193. P2 Workflow — Evidence Fusion

```text
COLLECT EVIDENCE
↓
ALIGN CLAIM
↓
ALIGN SCOPE
↓
ALIGN REGIME
↓
ALIGN TIME
↓
CHECK PROVENANCE
↓
CHECK SHARED ANCESTRY
↓
CHECK CONTRADICTIONS
↓
FUSE ONLY COMPATIBLE SUPPORT
```

---

# 194. P2 Workflow — Contradiction

```text
DETECT CONFLICT
↓
CHECK UNITS
↓
CHECK DEFINITIONS
↓
CHECK TIME
↓
CHECK SCOPE
↓
CHECK REGIME
↓
CHECK SOURCE VERSION
↓
CHECK CALIBRATION
↓
IF STILL CONFLICTING:
  PRESERVE COMPETING
  SEEK DISCRIMINATING TEST
```

---

# 195. P2 Workflow — Evidence Revocation

```text
DETECT INVALID EVIDENCE
↓
VERIFY FAILURE
↓
MARK REVOKED
↓
TRACE DEPENDENT CLAIMS
↓
CHECK ALTERNATIVE SUPPORT
↓
DOWNGRADE ONLY AFFECTED CLAIMS
↓
PERSIST REVOCATION PROVENANCE
```

---

# 196. P2 Workflow — Revalidation

```text
TRIGGER
↓
LOAD ORIGINAL EVIDENCE
↓
CHECK SOURCE
↓
CHECK VERSION
↓
CHECK CALIBRATION
↓
CHECK FRESHNESS
↓
CHECK ENVIRONMENT / REGIME
↓
REPEAT VALIDATION
↓
UPDATE STATUS
```

---

# 197. P2 Evidence Audit

Audit should verify:

```text
evidence typed?

observation separated from interpretation?

source resolvable?

source version known?

raw evidence recoverable?

transformation chain visible?

measurement units defined?

calibration valid?

error represented?

scope declared?

regime declared?

freshness adequate?

independence demonstrated?

shared ancestry detected?

contradictions preserved?

falsifiers represented?

confidence ceiling respected?
```

---

# 198. Evidence Audit Capsule

```yaml
evidence_audit:

  audit_id: null

  target_claim: null

  evidence_checked: []

  source_findings: []

  provenance_findings: []

  calibration_findings: []

  measurement_findings: []

  scope_findings: []

  regime_findings: []

  freshness_findings: []

  independence_findings: []

  contradiction_findings: []

  gaps: []

  result: null

  confidence_ceiling: null
```

---

# 199. P2 Finding Classes

```text
UNTYPED_EVIDENCE

SOURCE_UNRESOLVED

SOURCE_VERSION_UNKNOWN

RAW_EVIDENCE_MISSING

UNDECLARED_TRANSFORMATION

MODEL_OUTPUT_AS_OBSERVATION

SOURCE_CLAIM_AS_FACT

SUMMARY_AS_PRIMARY_SOURCE

MIRROR_AS_INDEPENDENT_SOURCE

SHARED_ANCESTRY_UNDISCLOSED

FALSE_INDEPENDENCE

CALIBRATION_EXPIRED

UNIT_UNDEFINED

DIMENSIONAL_MISMATCH

MEASUREMENT_ERROR_MISSING

SCOPE_LEAKAGE

REGIME_LEAKAGE

STALE_EVIDENCE

LATENCY_UNMODELED

MISSING_DATA_BIAS

CONTRADICTION_SUPPRESSED

CAUSAL_OVERREACH

ABSENCE_EVIDENCE_CONFUSION

CONFIDENCE_INFLATION

UNKNOWN_SUPPRESSED
```

---

# 200. Critical P2 Findings

Block consequential use when:

```text
load-bearing evidence source unknown

measurement meaning undefined

critical calibration invalid

evidence is materially stale

independence falsely assumed

major contradiction unresolved

model output is sole supposed observation

scope mismatch changes conclusion

causal claim relies only on association

critical raw evidence integrity fails
```

---

# 201. P2 Tests

Minimum:

```text
evidence typing test

source resolution test

version test

raw/processed test

transformation test

measurement test

unit test

calibration test

error test

freshness test

scope test

regime test

independence test

common-ancestor test

contradiction test

absence-of-evidence test

falsifier test

confidence-ceiling test
```

---

# 202. Evidence Typing Test

Every consequential evidence object must map to a known class or `UNKNOWN`.

---

# 203. Source Resolution Test

Can the evidence source be recovered?

If not:

```text
PROVENANCE GAP
```

---

# 204. Version Test

Mutable source evidence should identify exact version/time where material.

---

# 205. Raw/Processed Test

Processed evidence should reference its upstream input.

---

# 206. Transformation Test

Material transformations should be visible.

---

# 207. Measurement Test

Can the measurement procedure be described?

---

# 208. Unit Test

Quantitative physical variables should have valid units or explicit normalization.

---

# 209. Calibration Test

Instrument calibration should remain valid for the observation.

---

# 210. Error Test

Measurement uncertainty should not be omitted where decision-relevant.

---

# 211. Freshness Test

Dynamic evidence should remain current enough for use.

---

# 212. Scope Test

Evidence scope must cover the intended claim.

---

# 213. Regime Test

Evidence obtained under incompatible regime requires revalidation or explicit conditional use.

---

# 214. Independence Test

Supposed independent evidence must pass ancestry/correlation review.

---

# 215. Common-Ancestor Test

If multiple evidence objects share the same load-bearing ancestor:

```text
do not count them as fully independent.
```

---

# 216. Contradiction Test

Material contradictory evidence must remain visible.

---

# 217. Absence Test

Before treating non-observation as evidence of absence check:

```text
sensor sensitivity

coverage

detection threshold

observation duration

sampling
```

---

# 218. Falsifier Test

Claim should expose what evidence would weaken or invalidate it where applicable.

---

# 219. Confidence Ceiling Test

Conclusion confidence may not exceed load-bearing evidence confidence without independent revalidation.

---

# 220. P2 Failure Modes

## F01 — Source-Claim Inflation

A source assertion treated as measured fact.

## F02 — Observation/Interpretation Collapse

Inference presented as direct observation.

## F03 — Model/Observation Collapse

Model prediction treated as empirical measurement.

## F04 — Simulation/Reality Collapse

Simulation output used as external evidence without validation.

## F05 — Summary Laundering

Summary treated as original source.

## F06 — Evidence Sybil Attack

One source copied into many apparent confirmations.

## F07 — Independence Assumption

Independence assigned without ancestry analysis.

## F08 — Source Reputation Substitution

Authority reputation replaces evidence quality.

## F09 — Popularity Substitution

Repetition replaces evidence.

## F10 — Calibration Blindness

Instrument drift ignored.

## F11 — Unit Error

Quantities compared or combined incorrectly.

## F12 — Error Suppression

Measurement uncertainty hidden.

## F13 — Missingness Blindness

Missing-data mechanism ignored.

## F14 — Staleness Failure

Old evidence used as current.

## F15 — Scope Inflation

Local result generalized universally.

## F16 — Regime Inflation

One regime's evidence transferred to another.

## F17 — Correlation/Causation Collapse

Association treated causally.

## F18 — Absence Confusion

Lack of observation treated as proof of absence.

## F19 — Contradiction Suppression

Conflicting evidence removed for narrative consistency.

## F20 — Confidence Inflation

Derived certainty exceeds load-bearing evidence.

## F21 — Validation Mismatch

Evidence validates a different property than claimed.

## F22 — Unknown Suppression

Evidence gap filled by fluent assumption.

---

# 221. P2 Falsifiers

This architecture should be revised if:

```text
evidence typing does not improve epistemic discipline

source ancestry cannot distinguish copies from independent observations

scope/freshness metadata does not affect valid use

raw/processed separation cannot be maintained

correlation analysis systematically misclassifies independence

contradiction preservation prevents valid synthesis without adding integrity

confidence ceilings cannot be operationalized usefully

evidence revocation cannot support local invalidation
```

---

# 222. P2 Uncertainty Vector

Track when material:

```yaml
uncertainty:

  sensing: null

  measurement: null

  sampling: null

  source: null

  processing: null

  interpretation: null

  scope: null

  temporal: null

  regime: null

  causal: null

  provenance_independence: null
```

---

# 223. P2 Sensitivity

For a consequential claim identify:

```text
which evidence item,
measurement assumption,
source,
threshold,
or independence assumption
could flip the conclusion.
```

Check that first.

---

# 224. High-Stakes Evidence Standard

For decisions involving:

```text
health

safety

law

finance

critical infrastructure

irreversible deployment

canon promotion
```

increase requirements for:

```text
directness

freshness

independence

calibration

validation

adversarial challenge
```

---

# 225. Reversible Experiment Standard

Weak evidence may be sufficient for:

```text
small

contained

reversible

instrumented
```

experiments.

That does not increase the underlying evidence class.

---

# 226. P2 Agent

A Sense / Evidence agent may:

```text
collect evidence

type evidence

trace provenance

check source versions

identify raw vs processed evidence

check freshness

check measurement metadata

detect shared ancestry

detect contradictions

search disconfirming evidence

propose evidence admission state
```

---

# 227. P2 Agent Authority

Default:

```text
READ_ONLY
```

or:

```text
PROPOSE_ONLY
```

The agent should not independently promote:

```text
MODEL → VERIFIED

RESEARCH → CANON
```

without required validation/governance.

---

# 228. P2 Agent Contract

```yaml
agent:

  role: sense_evidence_steward

  default_authority: PROPOSE_ONLY

  read_access:
    - provided_context
    - authorized_tools
    - source_registry
    - provenance
    - evidence_registry
    - validation
    - environment_state

  write_access:
    - evidence_admission_proposals
    - evidence_quality_findings

  canon_promotion:
    authority: NONE

  world_action:
    authority: NONE_UNLESS_EXTERNAL_EXECUTOR_AUTHORIZES

  escalation: required

  termination: required

  audit_log: required
```

---

# 229. Evidence Registry

A derived implementation may maintain:

```text
P2_EVIDENCE/
│
├── EVIDENCE_REGISTRY
├── OBSERVATION_REGISTRY
├── SOURCE_REGISTRY
├── CALIBRATION_REGISTRY
├── CORRELATION_GROUPS
├── CONTRADICTION_REGISTRY
├── FALSIFIER_REGISTRY
├── EVIDENCE_GAPS
└── HISTORY
```

This is a proposed physical architecture, not asserted as existing canon.

---

# 230. Evidence Registry Entry

```yaml
evidence_registry_entry:

  evidence_id: null

  evidence_class: null

  logical_target: null

  source_ref: null

  provenance_ref: null

  observation_ref: null

  scope: null

  regime: null

  freshness: null

  independence_status: null

  admission_status: null

  superseded_by: null
```

---

# 231. Evidence SSOT Boundary

An evidence registry may have its own current authoritative state.

But:

```text
EVIDENCE_REGISTRY_SSOT
!=
TRUTH_SSOT
```

It only defines the current registered evidence state.

---

# 232. Evidence Lifecycle

Suggested:

```text
DISCOVERED
↓
CANDIDATE
↓
TYPED
↓
PROVENANCE_RESOLVED
↓
ADMITTED
↓
CURRENT
↓
AGING
↓
STALE
↓
SUPERSEDED / ARCHIVED
```

Possible:

```text
QUARANTINED

REVOKED

REJECTED

CONFLICTING
```

---

# 233. Evidence Lifecycle Boundary

A stale evidence object is not erased.

Its admissibility changes by use.

---

# 234. Evidence Provenance Persistence

Evidence lineage should survive:

```text
rename

move

format conversion

summary

version update

archive
```

---

# 235. Evidence Correction

If evidence metadata or interpretation was wrong:

```text
record correction

preserve old assessment

link replacement
```

Do not silently rewrite history.

---

# 236. Evidence and P1

P1 provides:

```text
external/environmental state target
```

P2 provides:

```text
evidence about that target.
```

Therefore:

```text
P1
=
WHAT MAY BE OUT THERE

P2
=
WHAT SUPPORT DO WE HAVE
FOR SAYING WHAT IS OUT THERE
```

---

# 237. Evidence and P3+

Downstream Universe Canon planes should consume P2 evidence rather than bypassing it.

Conceptually:

```text
P1 Reality / Environment
        ↓
P2 Sense / Evidence
        ↓
P3+ Representation / Model / Decision
```

---

# 238. P2 Canon Boundary

P2 may define canonical evidence-handling rules.

It must not declare:

```text
every registered observation is true.
```

---

# 239. AMOS Source Boundary

The primary Full Brain source is `AMOS_FULL_BRAIN_OS.json`. 

Its architecture can be admitted as:

```text
SOURCE_DEFINED AMOS CORPUS
```

while external scientific validity remains separately typed.

---

# 240. AMOS Corpus Evidence

For corpus questions:

```text
AMOS source file
```

may be primary evidence for:

```text
what AMOS canon says.
```

It is not automatically primary evidence for:

```text
how external reality behaves.
```

---

# 241. P2 Core Laws

```text
REALITY
!=
OBSERVATION
```

```text
OBSERVATION
!=
INTERPRETATION
```

```text
INTERPRETATION
!=
FACT
```

```text
SOURCE_CLAIM
!=
OBSERVATION
```

```text
REPORT
!=
DIRECT_MEASUREMENT
```

```text
MODEL_OUTPUT
!=
OBSERVATION
```

```text
SIMULATION
!=
EXPERIMENT
```

```text
SUMMARY
!=
PRIMARY_SOURCE
```

```text
MIRROR
!=
INDEPENDENT_SOURCE
```

```text
MULTIPLE_FILES
!=
MULTIPLE_EVIDENCE_ROOTS
```

```text
MULTIPLE_CITATIONS
!=
INDEPENDENT_CONFIRMATION
```

```text
INDEPENDENCE
MUST BE DEMONSTRATED
```

```text
POPULARITY
!=
EVIDENCE_STRENGTH
```

```text
AUTHORITY
!=
UNIVERSAL_CORRECTNESS
```

```text
ABSENCE_OF_EVIDENCE
!=
EVIDENCE_OF_ABSENCE
```

```text
CORRELATION
!=
CAUSATION
```

```text
CALIBRATED_ONCE
!=
CALIBRATED_FOREVER
```

```text
OLD_EVIDENCE
!=
CURRENT_STATE
```

```text
PROXY
!=
TARGET_CONSTRUCT
```

```text
BENCHMARK_SUCCESS
!=
UNIVERSAL_VALIDITY
```

```text
REPRODUCIBLE
!=
TRUE
```

```text
EVIDENCE
!=
AUTHORITY_TO_ACT
```

```text
DERIVED_CONFIDENCE
<=
WEAKEST_LOAD_BEARING_EVIDENCE
UNLESS
INDEPENDENTLY_REVALIDATED
```

```text
UNKNOWN/GAP
!=
PASS
```

---

# 242. Minimum P2 Evidence Contract

Before AMOS relies materially on evidence, it should be able to answer:

```text
WHAT exactly was observed or reported?

WHAT is the evidence class?

WHAT is the source?

WHICH source version?

WHO or WHAT produced it?

WHEN was it produced?

WHEN was it observed?

HOW was it measured?

WHAT instrument or channel was used?

WHAT unit applies?

WHAT calibration applies?

WHAT error applies?

WHAT raw evidence exists?

WHAT transformations occurred?

WERE any transformations lossy?

WHAT assumptions were introduced?

WHAT scope does the evidence cover?

WHAT regime produced it?

IS it fresh enough?

WHAT evidence ancestry exists?

DO corroborating sources share ancestry?

ARE they actually independent?

WHAT contradictions exist?

WHAT missing data exists?

WHAT bias may exist?

WHAT claim does the evidence support?

WHAT claim does it challenge?

WHAT would falsify the interpretation?

WHAT confidence ceiling does it impose?

WHAT happens if this evidence is revoked?
```

If load-bearing answers are missing:

```text
P2 EVIDENCE STATE
=
PARTIAL
CONDITIONAL
QUARANTINED
CONFLICTING
or
UNKNOWN/GAP
```

not:

```text
VERIFIED FACT
```

---

# 243. P2 Decision Table

```text
Directly measured?
→ MEASUREMENT / OBSERVATION

Source says it happened?
→ SOURCE_CLAIM / REPORT

Calculated from evidence?
→ DERIVED_EVIDENCE

Generated by predictive model?
→ MODEL_OUTPUT

Produced inside simulation?
→ SIMULATION_OUTPUT

Original source available?
→ bind primary provenance

Only summary available?
→ use as secondary/derived evidence

Multiple sources share raw source?
→ SHARED_ANCESTRY

Independence unclear?
→ UNKNOWN independence

Evidence outside scope?
→ do not generalize

Evidence stale?
→ historical or revalidate

Measurement uncertainty crosses threshold?
→ CONDITIONAL

Strong contradiction exists?
→ COMPETING / investigate

Sensor could not have detected absence?
→ no evidence-of-absence claim

All required checks pass?
→ ADMITTED for declared scope
```

---

# 244. P2 Admission Decision Table

```text
Source unresolved?
→ QUARANTINE / GAP

Evidence type unknown?
→ CANDIDATE / UNKNOWN

Raw evidence integrity failed?
→ REJECT / QUARANTINE

Calibration invalid?
→ CONDITION / REJECT

Scope mismatch?
→ RESTRICT SCOPE

Regime mismatch?
→ REVALIDATE

Stale?
→ STALE / REVALIDATE

Shared ancestry hidden?
→ DOWNGRADE INDEPENDENCE

Contradictory evidence unresolved?
→ COMPETING

Causal claim but evidence associational?
→ DOWNGRADE CLAIM TYPE

All requirements sufficient?
→ ADMIT
```

---

# 245. P2 RSCF Completion State

The placeholder:

```text
claim_class: AMOS_MODEL
```

can now be expanded to:

```yaml
claim_class: DERIVED

evidence:
  - AMOS Full Brain OS operating rules
  - AMOS Full Brain primary source declaration
  - Universe Canon Contract
  - P1 Reality / Environment
  - Root Provenance architecture
  - Root Status architecture
  - Validation architecture
  - Dependency architecture

provenance:
  origin_architect: Trang Phan
  transformation: p2_sense_evidence_architecture_completion
  source_basis:
    - AMOS_FULL_BRAIN_OS.json
  status: derived_from_amos_corpus

scope:
  branch: 01_CANON
  subbranch: 02_UNIVERSE_CANON
  artifact: P2_SENSE_EVIDENCE
  role: sensing_observation_measurement_and_evidence_admission_contract

regime:
  architecture: AMOS OS

freshness:
  revalidate_on:
    - universe_canon_change
    - evidence_policy_change
    - provenance_policy_change
    - validation_policy_change
    - P1_contract_change
    - source_topology_change
    - core_lineage_change

dependencies:
  - CANON_UNIVERSE_CANON_CONTRACT
  - P1_REALITY_ENVIRONMENT
  - AMOS_FULL_BRAIN_OS
  - AMOS_OS_KERNEL_v4.4
  - 00_ROOT_PROVENANCE
  - 00_ROOT_STATUS
  - 09_DEPENDENCY_GRAPH
  - 11_VALIDATION

competing:
  - flat_evidence_list
  - citation_count_as_confidence
  - source_reputation_as_truth
  - model_outputs_as_observation
  - all_sources_independent_by_default
  - evidence_without_scope_or_freshness

falsifiers:
  - typed evidence does not improve epistemic reliability
  - provenance topology cannot distinguish copies from independent evidence
  - evidence scope/freshness cannot be applied operationally
  - contradiction preservation prevents any useful synthesis
  - independence checking cannot meaningfully alter confidence
  - evidence revocation cannot support local downstream invalidation

confidence_ceiling:
  architecture: CONDITIONAL
  exact_evidence_schema: DERIVED
  exact_independence_engine: UNKNOWN
  exact_evidence_quality_aggregation: UNKNOWN
  exact_calibration_runtime: UNKNOWN
  exact_live_evidence_registry: UNKNOWN
```

---

# 246. Known Gaps

The following remain `UNKNOWN/GAP` until explicit canon or implementation defines them:

```text
exact canonical evidence schema

exact evidence-ID format

exact observation-ID format

exact source-ID format

exact evidence registry backend

exact evidence-quality calculation

exact confidence aggregation

exact independence scoring

exact correlation detection algorithm

exact Sybil-hardening algorithm

exact calibration registry

exact measurement-error model library

exact sensor adapter system

exact evidence freshness policy

exact contradiction-resolution engine

exact causal evidence classifier

exact evidence-fusion algorithm

exact automated falsifier engine

exact admission authority roles

exact evidence retention policy

exact evidence redaction policy

exact live raw-evidence storage layer
```

Do not fabricate these as implemented.

---

# 247. Completion Status

This artifact should no longer remain:

```text
STATUS: PLACEHOLDER
```

at the architecture-contract level.

It may become:

```yaml
class: CANON_MODEL

architecture_status: DEFINED

source_status: DERIVED_FROM_SOURCE

canon_status: CONDITIONAL

implementation_status: PARTIAL_OR_UNKNOWN

validation_status: ARCHITECTURE_DEFINED

p2_contract_status: DEFINED

evidence_schema_status: DERIVED_CONDITIONAL

evidence_registry_status: UNKNOWN_OR_PARTIAL

sense_runtime_status: UNKNOWN_OR_PARTIAL

independence_engine_status: UNKNOWN/GAP

evidence_fusion_engine_status: UNKNOWN/GAP

empirical_validation_of_amos_native_evidence_formalisms: NOT_ESTABLISHED
```

---

# 248. Final Contract

`P2 Sense / Evidence` is the **epistemic intake and evidence-integrity plane** of the AMOS Universe Canon.

Its role is to preserve the full path:

```text
REALITY / ENVIRONMENT
        ↓
SENSING CHANNEL
        ↓
RAW OBSERVATION
        ↓
MEASUREMENT / REPORT
        ↓
SOURCE IDENTITY
        ↓
PROVENANCE
        ↓
TRANSFORMATION
        ↓
EVIDENCE OBJECT
        ↓
SCOPE / REGIME / FRESHNESS
        ↓
INDEPENDENCE / CORRELATION
        ↓
CONTRADICTION / FALSIFIER
        ↓
RSCF SUPPORT
```

without collapsing these layers.

The correct relationship is:

```text
P1 REALITY / ENVIRONMENT
=
WHAT EXTERNAL STATE MAY EXIST

P2 SENSE / EVIDENCE
=
WHAT CONTACT AND SUPPORT WE ACTUALLY HAVE

PROVENANCE
=
WHERE THAT SUPPORT CAME FROM

VALIDATION
=
WHAT THE SUPPORT HAS BEEN SHOWN TO JUSTIFY

RSCF
=
HOW THE SUPPORT PARTICIPATES IN A CLAIM

CANON
=
WHAT AMOS CURRENTLY GOVERNS AS AUTHORITATIVE
WITHIN DECLARED SCOPE
```

The governing P2 principle is:

```text
DO NOT LET
A SOURCE CLAIM,
A MODEL OUTPUT,
A SUMMARY,
A COPY,
A REPOST,
OR A REPEATED DESCENDANT

BECOME
AN APPARENT INDEPENDENT OBSERVATION

MERELY BECAUSE
ITS SURFACE REPRESENTATION
LOOKS DIFFERENT.
```

The Sense / Evidence law is:

```text
SENSE WHAT IS ACCESSIBLE.

PRESERVE THE RAW SIGNAL.

TYPE THE OBSERVATION.

IDENTIFY THE SOURCE.

TRACE THE ANCESTRY.

RECORD THE TRANSFORMATIONS.

MEASURE THE ERROR.

BOUND THE SCOPE.

CHECK THE REGIME.

CHECK THE FRESHNESS.

DEMONSTRATE INDEPENDENCE.

KEEP CONTRADICTIONS VISIBLE.

DEFINE FALSIFIERS.

LET EVIDENCE CHANGE THE MODEL.

NEVER LET THE MODEL
REWRITE THE EVIDENCE
TO PROTECT ITSELF.
```

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---

**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

RSCF-NODE

node_id: p2_sense_evidence

node_type: note

path: 01_CANON/02_UNIVERSE_CANON/P2_SENSE_EVIDENCE.md

RSCF-RELATIONS:

* INDEXED_BY: [[00-Home]]

* INDEXED_BY: [[AMOS_RSCF_NODES]]

* DEPENDS_ON: [[P1_REALITY_ENVIRONMENT]]

claim_class: AMOS_MODEL

```

**Conclusion class:** `DERIVED / CONDITIONAL`. This turns P2 from a placeholder into the full **sensing, measurement, evidence-admission, provenance-topology, and independence-control plane** between external reality and downstream AMOS reasoning. It preserves the Full Brain requirement to distinguish observations, source claims, models, derived conclusions, and unknowns instead of silently upgrading one into another. 
```
