---
type: registry
source: 01_CANON/05_VARIABLE_REGISTRY
artifact_id: AMOS-UNIT-REGISTRY
name: UNIT_REGISTRY
title: AMOS Unit Registry — Canonical Dimensions, Units, Scales, Conversion, and Measurement
  Semantics
document_version: 1.0.0
canon_version: 4.4
amos_core_target: v4.4
status: ACTIVE_CANON_CANDIDATE
conclusion_class: AMOS_MODEL
rscf_state: derived
canon_group: meta
canon_type: registry
origin_architect: Trang Phan
steward: Trang Phan
created: 2026-08-25
updated: 2026-08-25
tags:
- amos
- canon
- universe
- amos-os
- amos-core
- amos-core-v4-4
- registry
- units
- dimensions
- measurement
- quantities
- scales
- normalization
- conversion
- dimensional-analysis
- uncertainty
- provenance
- precision
- computational-units
- physical-units
- semantic-units
- rscf
- canon-group/meta
- canon/registry
- rscf/claim
- rscf/provenance
- rscf/state/derived
- readme
- architecture
- placement-rules
- amos-core-laws
- law-hierarchy
- cognitive-matrix-architecture
aliases:
- AMOS Unit Registry - Unit Registry - AMOS Measurement Registry - AMOS Quantity and
  Dimension
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# AMOS Unit Registry
**Origin architect / steward:** Trang Phan
> **Status:** `ACTIVE_CANON_CANDIDATE`
> **AMOS Core target:** `v4.4`
> **Conclusion class:** `AMOS_MODEL`
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# 0. Purpose

The **AMOS Unit Registry** defines the canonical semantic layer for quantities, dimensions, units, scales, normalized values, computational measures, rates, ratios, and conversions used throughout AMOS OS.

The registry exists to prevent silent errors such as:

```text
METERS
+
SECONDS
```

or:

```text
0.8 CONFIDENCE
=
80 METERS
```

or:

```text
10 MB
=
10 MiB
```

or:

```text
CELSIUS × 2
=
TWICE AS HOT
```

without an explicitly valid transformation.

Core law:

```text
VALUE
WITHOUT UNIT / SCALE / SEMANTIC TYPE
MAY BE INCOMPLETE.
```

For decision-relevant quantities:

```text
QUANTITY
=
VALUE
+
UNIT
+
DIMENSION
+
SCALE
+
SCOPE
+
PROVENANCE
+
UNCERTAINTY
```

where applicable.

---

# 1. Registry Boundary

The Unit Registry defines measurement semantics.

It does not create measurements.

```text
REGISTERED UNIT
!=
OBSERVED VALUE
```

It does not prove correctness.

```text
VALID UNIT
!=
VALID MEASUREMENT
```

It does not create empirical truth.

```text
DIMENSIONALLY VALID
!=
EMPIRICALLY VALID
```

It does not grant authority.

```text
UNIT
!=
AUTHORITY
```

---

# 2. Core Identity Law

AMOS distinguishes:

```text
QUANTITY
!=
VALUE
!=
UNIT
!=
DIMENSION
!=
SCALE
!=
DISPLAY FORMAT
!=
MEASUREMENT METHOD
!=
SEMANTIC MEANING
```

Example:

```text
quantity: distance
value: 100
unit: meter
dimension: length
display: "100 m"
```

These fields interact but remain distinct.

---

# 3. Canonical Quantity Object

A consequential measured quantity should conceptually support:

```yaml
quantity:
  quantity_id:
  semantic_name:

  value:
  unit:
  dimension:

  scale_type:
  normalization:

  uncertainty:
  precision:
  significant_figures:

  measurement_method:
  scope:
  regime:
  observed_at:

  provenance:

  conversion_history: []
```

Not every subsystem must serialize this exact schema.

The semantics are load-bearing.

---

# 4. Unit Record

A registered unit should eventually support:

```yaml
unit:
  unit_id:
  symbol:
  canonical_name:

  unit_type:
  dimension:

  base_definition:
  conversion_type:

  multiplier:
  offset:

  reference_unit:

  exact_conversion:
  approximate_conversion:

  aliases: []

  namespace:
  scope:

  provenance:
  standard_reference:

  status:
  introduced_in:
  supersedes:
```

---

# 5. Unit Classes

AMOS recognizes these high-level unit classes:

```text
PHYSICAL_STANDARD
COMPUTATIONAL
TEMPORAL
COUNT
RATIO
RATE
PROBABILITY
NORMALIZED
LOGARITHMIC
ORDINAL
CATEGORICAL
DOMAIN_LOCAL
AMOS_DERIVED
DIMENSIONLESS
```

These classes must not be silently conflated.

---

# 6. Physical Standard Units

Physical quantities should use established physical units when applicable rather than inventing AMOS-specific replacements.

Primary base dimensions commonly include:

```text
LENGTH
MASS
TIME
ELECTRIC_CURRENT
THERMODYNAMIC_TEMPERATURE
AMOUNT_OF_SUBSTANCE
LUMINOUS_INTENSITY
```

Canonical principle:

```text
EXISTING STANDARD UNIT
>
UNNECESSARY PROPRIETARY UNIT
```

unless a domain-local unit has a justified and explicitly scoped purpose.

---

# 7. Base Physical Units

Registry reference set:

| Dimension                 | Canonical unit | Symbol |
| ------------------------- | -------------- | ------ |
| Length                    | meter          | `m`    |
| Mass                      | kilogram       | `kg`   |
| Time                      | second         | `s`    |
| Electric current          | ampere         | `A`    |
| Thermodynamic temperature | kelvin         | `K`    |
| Amount of substance       | mole           | `mol`  |
| Luminous intensity        | candela        | `cd`   |

These are standard external measurement units referenced by AMOS, not inventions of AMOS.

---

# 8. Dimension Vectors

Physical dimensions may be represented as exponent vectors.

Conceptually:

```text
DIMENSION
=
L^a
M^b
T^c
I^d
Θ^e
N^f
J^g
```

where the symbols represent base dimensions.

Example:

```text
velocity
=
L · T^-1
```

Acceleration:

```text
L · T^-2
```

Force:

```text
M · L · T^-2
```

---

# 9. Dimensional Equality

Two quantities may be directly added or subtracted only when their dimensions are compatible.

```text
DIM(A)
=
DIM(B)
```

is normally required for:

```text
A + B
```

and:

```text
A - B
```

after valid conversion into compatible units.

---

# 10. Dimensional Firewall

Canonical laws:

```text
SAME NUMBER
!=
SAME QUANTITY
```

```text
SAME UNIT SYMBOL
!=
SAME SEMANTIC MEANING
```
```text
SAME DIMENSION
!=
SAME QUANTITY TYPE
```
Example:

```text
TORQUE
```

and:

```text
ENERGY
```

can share dimensional form while representing different semantic quantities.

Therefore dimensional equivalence alone does not prove semantic equivalence.

---

# 11. B3-Style Isomorphism Discipline

AMOS applies the same discipline used elsewhere for structurally similar spaces:

```text
STRUCTURAL / DIMENSIONAL KINSHIP
!=
MEANING IDENTITY
```

Therefore:

```text
SAME DIMENSION
```

must not silently become:

```text
SAME PHYSICAL ROLE
```

This prevents semantic conflation.

---

# 12. Derived Physical Units

Common derived reference units include:

| Quantity        | Unit    | Symbol |
| --------------- | ------- | ------ |
| Frequency       | hertz   | `Hz`   |
| Force           | newton  | `N`    |
| Pressure        | pascal  | `Pa`   |
| Energy          | joule   | `J`    |
| Power           | watt    | `W`    |
| Electric charge | coulomb | `C`    |
| Voltage         | volt    | `V`    |
| Resistance      | ohm     | `Ω`    |

These remain standard external units.

---

# 13. Prefixes

Metric prefixes may modify compatible units.

Examples:

```text
kilo = 10^3
mega = 10^6
giga = 10^9

milli = 10^-3
micro = 10^-6
nano = 10^-9
```

A prefix changes scale.

It does not change the underlying dimension.

---

# 14. Prefix Firewall

```text
1 km
=
1000 m
```

but:

```text
km
!=
m
```

as unit expressions.

Both share:

```text
DIMENSION = LENGTH
```

---

# 15. Exact Conversion

A conversion is `EXACT` where its relationship is definitionally exact within the applicable standard.

Conceptually:

```yaml
conversion:
  source_unit:
  target_unit:
  type: EXACT
  multiplier:
  offset:
```

Exact conversion does not remove source measurement uncertainty.

---

# 16. Approximate Conversion

A conversion is approximate when approximation is introduced by:

```text
EMPIRICAL CONSTANT
ROUNDING
MODEL
TRUNCATION
CALIBRATION
CONTEXTUAL ASSUMPTION
```

Approximation must remain explicit.

```text
APPROXIMATE
!=
EXACT
```

---

# 17. Conversion Provenance

For consequential conversions, preserve:

```text
SOURCE UNIT

TARGET UNIT

CONVERSION RULE

CONVERSION VERSION

ROUNDING

PRECISION

ORIGINAL VALUE
```

Never destroy the original quantity merely because a converted representation is more convenient.

---

# 18. Conversion Chain

Conceptually:

```text
SOURCE VALUE
↓
SOURCE UNIT
↓
CONVERSION RULE
↓
TARGET VALUE
↓
TARGET UNIT
```

A converted result should remain traceable to the original where required.

---

# 19. Affine Units

Not all conversions are pure multiplication.

For affine conversion:

```text
y
=
a·x + b
```

The offset matters.

Temperature scales are canonical examples.

Therefore:

```text
UNIT CONVERSION
!=
ALWAYS MULTIPLICATIVE
```

---

# 20. Temperature Firewall

Differences and absolute temperatures must be distinguished.

```text
TEMPERATURE VALUE
!=
TEMPERATURE DIFFERENCE
```

An affine-scale absolute temperature cannot always be manipulated as though its scale had an absolute zero at numeric zero.

---

# 21. Logarithmic Units

Some domain quantities may use logarithmic scales.

Conceptually:

```text
L
=
k log(x / x_ref)
```

Such values cannot be treated as ordinary linear quantities without transformation.

Canonical rule:

```text
LOGARITHMIC SCALE
!=
LINEAR SCALE
```

---

# 22. Scale Types

AMOS recognizes at least:

```text
NOMINAL
ORDINAL
INTERVAL
RATIO
LOGARITHMIC
BINARY
NORMALIZED
PROBABILISTIC
```

Operations allowed on a value depend on scale type.

---

# 23. Nominal Scale

Nominal values classify.

Examples:

```text
RED
GREEN
BLUE
```

or:

```text
PERCEPTION
HYPOTHESIS
RISK
```

Canonical law:

```text
CATEGORY LABEL
!=
NUMERICAL QUANTITY
```

---

# 24. Ordinal Scale

Ordinal values support ordering but not necessarily meaningful interval arithmetic.

Example:

```text
LOW
MEDIUM
HIGH
```

may imply:

```text
LOW < MEDIUM < HIGH
```

but does not imply:

```text
HIGH - MEDIUM
=
MEDIUM - LOW
```

---

# 25. Interval Scale

Interval scales support meaningful differences.

They do not necessarily support meaningful ratios.

Canonical firewall:

```text
DIFFERENCE VALID
!=
RATIO VALID
```

---

# 26. Ratio Scale

Ratio scales have meaningful zero and permit ratio interpretation when the underlying measurement semantics support it.

Conceptually:

```text
2x
```

has a meaningful interpretation only where the scale supports ratios.

---

# 27. Count Units

Discrete counts should be typed as counts.

Examples:

```text
cell
edge
node
agent
request
token
event
revision
RSCF
hypothesis
```

Count units are normally dimensionless mathematically but semantically typed.

Therefore:

```text
10 cells
!=
10 agents
```

even though both contain the numeric value `10`.

---

# 28. Typed Counts

Preferred pattern:

```yaml
quantity:
  value: 361
  unit: cell
  quantity_type: BOARD_CELL_COUNT
```

rather than:

```yaml
value: 361
```

when the count's meaning is load-bearing.

---

# 29. Ratio

A ratio compares compatible or explicitly related quantities.

Conceptually:

```text
R
=
A / B
```

A ratio may be dimensionless while retaining semantic identity.

Examples:

```text
SPARSITY_RATIO

SUCCESS_RATE

UTILIZATION

ERROR_FRACTION
```

Canonical law:

```text
DIMENSIONLESS
!=
SEMANTICALLY UNDEFINED
```

---

# 30. Percentage

Percentage is a presentation of a ratio.

```text
100%
=
1
```

for a normalized fraction scale.

Therefore:

```text
80%
=
0.8
```

only where both represent the same normalized quantity.

---

# 31. Percentage Firewall

Do not confuse:

```text
PERCENT
```

with:

```text
PERCENTAGE POINT
```

Example:

```text
20% → 30%
```

means:

```text
+10 percentage points
```

and:

```text
+50% relative increase
```

These are different quantities.

---

# 32. Probability

Probability values normally satisfy:

```text
0 <= P <= 1
```

when represented as normalized probability.

Probability is dimensionless but semantically typed.

```text
P = 0.8
```

must not automatically be interpreted as AMOS confidence unless the relevant model explicitly defines that relationship.

---

# 33. Confidence

AMOS confidence is an epistemic quantity.

It is not automatically a calibrated probability.

Canonical firewall:

```text
CONFIDENCE
!=
PROBABILITY
```

unless a specific subsystem establishes a calibration mapping.

Likewise:

```text
CONFIDENCE
!=
AUTHORITY
```

---

# 34. Confidence Scale

Where normalized confidence is used:

```text
0 <= C <= 1
```

may be a valid local model.

But the registry must preserve whether the value is:

```text
CALIBRATED_PROBABILITY
HEURISTIC_CONFIDENCE
MODEL_SCORE
HUMAN_RATING
DERIVED_CONFIDENCE
```

These are not interchangeable.

---

# 35. Normalized Values

A normalized quantity should declare its normalization.

Conceptually:

```yaml
normalized_quantity:
  value:
  range: [0, 1]
  source_quantity:
  normalization_method:
  reference_min:
  reference_max:
```

Without the mapping, normalized values may not be interpretable.

---

# 36. Normalization Firewall

```text
0.8
```

by itself is ambiguous.

It might represent:

```text
80%
0.8 probability
0.8 confidence
0.8 activation
0.8 saturation
0.8 similarity
0.8 normalized risk
```

Therefore:

```text
NORMALIZED NUMBER
!=
SEMANTIC IDENTITY
```

---

# 37. AMOS Activation

Where AMOS cognitive field components use activation values, the preferred semantic type is:

```text
COGNITIVE_ACTIVATION
```

with the implementation-defined scale preserved.

If current implementation uses:

```text
0 <= activation <= 1
```

that is an implementation contract, not a universal law unless canonically bound.

---

# 38. Attention Priority

Attention priority is a model-derived ranking quantity.

It may be:

```text
DIMENSIONLESS
```

but must remain semantically typed as:

```text
ATTENTION_PRIORITY
```

It must not automatically be compared to confidence, risk, or probability merely because all use numeric values.

---

# 39. Risk Scores

Risk may be represented through:

```text
PROBABILITY
IMPACT
EXPECTED LOSS
ORDINAL CLASS
NORMALIZED SCORE
```

These are distinct.

Canonical firewall:

```text
RISK_SCORE
!=
RISK_PROBABILITY
```

and:

```text
RISK_CLASS
!=
EXPECTED LOSS
```

---

# 40. Composite Scores

A composite score should preserve its equation or mapping.

Conceptually:

```text
S
=
w1·x1
+
w2·x2
+
...
+
wn·xn
```

If component quantities use incompatible scales, normalization or transformation must be justified.

---

# 41. Composite Score Firewall

```text
NUMERICALLY COMBINABLE
!=
SEMANTICALLY COMBINABLE
```

A formula can execute while remaining conceptually invalid.

Dimensional and semantic checks precede fluency of computation.

---

# 42. Rates

A rate is:

```text
QUANTITY
/
REFERENCE QUANTITY
```

often time.

Examples:

```text
requests / second
tokens / second
errors / minute
events / epoch
```

Rate denominator must remain explicit.

---

# 43. Throughput

Throughput is a constrained rate of successful flow.

Examples:

```text
requests/s
bytes/s
tokens/s
items/min
```

Within AMOS 7-Part persistence reasoning, throughput may be relevant to `Flow`, but the numerical unit remains domain-specific.

---

# 44. Latency

Latency should use temporal units.

Examples:

```text
ns
µs
ms
s
```

Canonical law:

```text
LATENCY VALUE
WITHOUT ENVIRONMENT
MAY BE INCOMPLETE
```

Latency claims should inherit where relevant:

```text
HARDWARE
SOFTWARE
LOAD
NETWORK
PERCENTILE
SAMPLE WINDOW
```

---

# 45. Percentile Latency

Distinguish:

```text
MEAN LATENCY

MEDIAN LATENCY

P95 LATENCY

P99 LATENCY

MAX LATENCY
```

These are not interchangeable.

A value such as:

```text
100 ms
```

is incomplete when the aggregation statistic materially affects interpretation.

---

# 46. Time Units

Reference temporal units include:

```text
nanosecond
microsecond
millisecond
second
minute
hour
day
```

But durations and timestamps are different semantic types.

```text
DURATION
!=
TIMESTAMP
```

---

# 47. Timestamp

A timestamp requires a time reference.

Conceptually:

```yaml
timestamp:
  instant:
  timezone:
  clock_system:
  precision:
```

Canonical law:

```text
TIME VALUE
WITHOUT TIME REFERENCE
MAY BE AMBIGUOUS
```

---

# 48. Duration

Duration measures elapsed time.

It is independent of calendar representation when expressed as physical elapsed time.

Canonical firewall:

```text
DURATION
!=
CALENDAR DATE
```

---

# 49. Epoch

`epoch` may be a count/order marker rather than physical time.

Examples:

```text
CAUSAL_EPOCH
TRAINING_EPOCH
STATE_EPOCH
```

Therefore:

```text
EPOCH
!=
SECOND
```

unless a specific mapping exists.

---

# 50. Step

`step` is a discrete progression count.

Examples:

```text
runtime step
cognition step
simulation step
workflow step
```

Canonical law:

```text
STEP COUNT
!=
ELAPSED TIME
```

unless step duration is explicitly defined.

---

# 51. Sequence Number

A sequence number identifies ordering.

```text
SEQ_100
```

does not imply:

```text
100 seconds
```

or:

```text
epoch 100
```

Order and physical time are different dimensions.

---

# 52. Computational Information Units

AMOS should distinguish decimal and binary information units.

Reference:

```text
bit
byte
```

Decimal prefixes:

```text
kB = 10^3 bytes
MB = 10^6 bytes
GB = 10^9 bytes
TB = 10^12 bytes
```

Binary prefixes:

```text
KiB = 2^10 bytes
MiB = 2^20 bytes
GiB = 2^30 bytes
TiB = 2^40 bytes
```

---

# 53. Byte Firewall

Canonical law:

```text
MB != MiB
```

and:

```text
GB != GiB
```

unless a local system explicitly abuses notation, in which case the ambiguity should be documented rather than silently normalized.

---

# 54. Bit / Byte Firewall

```text
8 bits
=
1 byte
```

for an octet-based byte.

But:

```text
Mb
!=
MB
```

Case matters.

---

# 55. Token

`token` is a model/runtime-specific count unit.

Canonical firewall:

```text
TOKEN
!=
CHARACTER

TOKEN
!=
WORD

TOKEN
!=
BYTE
```

Conversions between these depend on tokenizer/model/content.

Therefore no universal token-to-word conversion should be canonized.

---

# 56. Context Length

Context capacity should be typed as:

```text
TOKEN_COUNT
```

or another explicit implementation unit.

A context-length value must inherit the relevant tokenizer/model version when necessary.

---

# 57. Operations

Computational operations may be counted as:

```text
operation
instruction
FLOP
request
transaction
evaluation
```

These units are not interchangeable.

---

# 58. FLOP Firewall

A FLOP count measures floating-point operation quantity under a defined convention.

It does not directly establish:

```text
LATENCY

ENERGY

MODEL QUALITY

COST
```

without additional evidence.

---

# 59. Memory Capacity

Computational memory/storage capacity should preserve whether a value refers to:

```text
LOGICAL SIZE

ALLOCATED SIZE

RESIDENT SIZE

COMPRESSED SIZE

TRANSFER SIZE

PERSISTED SIZE
```

These may differ significantly.

---

# 60. Board Coordinate Units

For 19×19 strategic/cognitive grids:

```text
row
column
cell
edge
```

are structural coordinate/count semantics.

Canonical constants may include where applicable:

```text
BOARD_SIZE = 19

TOTAL_CELLS = 361
```

for a 19×19 square grid.

These counts are derived from geometry:

```text
19 × 19 = 361
```

The meaning of each cell remains subsystem-specific.

---

# 61. 19×19 Semantic Firewall

AMOS may have multiple 19×19 systems.

Canonical rule:

```text
SAME 19×19 ADDRESS SPACE
!=
SAME SEMANTICS
```

Therefore:

```text
MURK CELL
!=
SEMANTIC MATRIX CELL
!=
GO BOARD CELL
!=
COGNITION FIELD CELL
!=
A-MATRIX ELEMENT
```

unless a specific mapping is explicitly defined.

---

# 62. Coordinate Representation

A coordinate should preserve:

```text
ROW
COLUMN
INDEXING CONVENTION
BOARD SIZE
```

Potential conventions:

```text
0-based
1-based
letter-number
serialized key
```

Canonical law:

```text
(row=1,col=1)
```

is ambiguous without indexing convention.

---

# 63. Sparse Field Metrics

For a sparse field:

```text
active_count
```

is a count.

A sparsity/occupancy ratio should explicitly define the numerator.

Example:

```text
active_ratio
=
active_cells / total_cells
```

If `sparsity_ratio` is used to mean that quantity, its local convention must remain explicit because mathematical literature may use "sparsity" differently.

---

# 64. Density vs Sparsity

Possible definitions:

```text
density
=
active / total
```

```text
sparsity
=
1 - density
```
But if an implementation defines:

```text
sparsity_ratio
=
active / total
```

the registry must preserve the implementation contract rather than silently changing it.

Semantic mismatch should be documented.

---

# 65. Graph Counts

Graph quantities may include:

```text
node
edge
degree
path
component
cycle
```

A count remains semantically typed.

Example:

```text
684 edges
```

does not imply anything about:

```text
EDGE WEIGHT
EDGE DIRECTION
EDGE SEMANTICS
```

without additional definitions.

---

# 66. Probability vs Frequency

Empirical frequency:

```text
count(event) / count(trials)
```

may estimate probability under assumptions.

Canonical firewall:

```text
OBSERVED FREQUENCY
!=
TRUE PROBABILITY
```

unless the inferential model justifies that interpretation.

---

# 67. Score vs Measurement

A score is often model-derived.

A measurement is observation-derived.

```text
SCORE
!=
MEASUREMENT
```

A score may be useful without having a physical unit.

---

# 68. Index

An index combines or transforms values into a reference number.

Examples:

```text
health index
risk index
complexity index
alignment index
```

Every index should preserve:

```text
INPUTS
WEIGHTS
TRANSFORMATION
NORMALIZATION
VERSION
```

when load-bearing.

---

# 69. Index Versioning

Changing an index formula creates a new semantic version of the index.

Canonical rule:

```text
SAME DISPLAY NAME
+
DIFFERENT EQUATION
=
DIFFERENT VERSIONED METRIC
```

Historical values should not be compared without compatibility analysis.

---

# 70. Unit Versioning

Units based on stable external standards normally do not need AMOS-specific semantic versioning.

AMOS-local units or scales do.

Conceptually:

```yaml
amos_unit:
  unit_id:
  semantic_version:
  definition:
  conversion_rule:
  introduced_in:
  superseded_by:
```

---

# 71. Unit Aliases

Aliases must resolve to one semantic unit identity.

```text
ALIAS
→
CANONICAL UNIT
```

Aliases must not silently create alternate conversion semantics.

---

# 72. Namespace Collision

The same symbol can mean different things in different domains.

Examples:

```text
m
```

may mean meter in unit notation but may also appear as an ordinary mathematical variable.

```text
C
```

may mean coulomb, confidence, capacitance variable, or generic constant depending on namespace.

Therefore:

```text
SYMBOL TEXT
!=
UNIT IDENTITY
```

Use context or namespace qualification where ambiguity matters.

---

# 73. Qualified Unit Identity

Preferred machine-readable pattern:

```text
SI:m
SI:kg
SI:s

AMOS:confidence
AMOS:activation
AMOS:rscf_count
AMOS:cognitive_step
```

The exact namespace syntax is an implementation choice.

Semantic qualification is the requirement.

---

# 74. Measurement Method

A measurement result inherits its method.

Conceptually:

```yaml
measurement:
  quantity:
  value:
  unit:
  method:
  instrument:
  calibration:
  environment:
  uncertainty:
```

Canonical law:

```text
VALUE + UNIT
MAY STILL BE INCOMPLETE
WITHOUT METHOD
```

for consequential measurement claims.

---

# 75. Instrument

Measurements may depend on an instrument or computational procedure.

Examples:

```text
sensor
benchmark
parser
model
estimator
human rating
algorithm
```

Instrument identity should be preserved when it can materially alter the value.

---

# 76. Calibration

Calibration establishes mapping between instrument output and a reference.

```text
RAW SIGNAL
↓
CALIBRATION
↓
MEASUREMENT
```

Canonical firewall:

```text
INSTRUMENT OUTPUT
!=
CALIBRATED QUANTITY
```

unless calibration is established.

---

# 77. Precision

Precision describes resolution or repeatability properties.

It is not the same as accuracy.

```text
PRECISION
!=
ACCURACY
```

---

# 78. Accuracy

Accuracy concerns closeness to an applicable reference or true value under a declared framework.

A highly precise measurement can still be inaccurate.

```text
HIGH PRECISION
!=
HIGH ACCURACY
```

---

# 79. Resolution

Resolution is the smallest distinguishable increment under a measurement system.

```text
RESOLUTION
!=
UNCERTAINTY
```

although they may interact.

---

# 80. Significant Figures

Reported significant figures should not exceed justified precision.

Canonical law:

```text
MORE DIGITS
!=
MORE INFORMATION
```

False precision must not be introduced during conversion.

---

# 81. Rounding

Rounding should preserve:

```text
ROUNDING METHOD
DECIMAL PLACES / SIGNIFICANT FIGURES
```

where materially relevant.

Repeated conversion should preferably use the highest available internal precision and round only at presentation boundaries.

---

# 82. Uncertainty

Measurement uncertainty should remain attached to the quantity where consequential.

Conceptually:

```text
x ± u
```

or a richer distribution/interval model.

Canonical law:

```text
VALUE
!=
EXACT VALUE
```

unless exactness is justified.

---

# 83. Interval

An uncertainty interval must declare semantics.

Examples:

```text
RANGE
CONFIDENCE INTERVAL
CREDIBLE INTERVAL
TOLERANCE
MIN/MAX BOUNDS
```

These are not interchangeable.

---

# 84. Error

`error` may mean:

```text
MEASUREMENT ERROR
MODEL ERROR
RESIDUAL
ABSOLUTE ERROR
RELATIVE ERROR
SYSTEM FAILURE
```

The term must be typed.

---

# 85. Absolute Error

Conceptually:

```text
E_abs
=
|x_est - x_ref|
```

with the same unit as the quantity.

---

# 86. Relative Error

Conceptually:

```text
E_rel
=
|x_est - x_ref| / |x_ref|
```

when the denominator is valid.

Relative error is dimensionless.

---

# 87. Zero-Denominator Firewall

Ratios are undefined when the required denominator is zero.

```text
A / 0
=
UNDEFINED
```

not:

```text
0
```

or:

```text
PASS
```

Canonical law:

```text
UNDEFINED
!=
ZERO
```

---

# 88. Missing Value Firewall

Distinguish:

```text
0
NULL
MISSING
UNKNOWN
UNDEFINED
NOT_APPLICABLE
```

These are separate states.

Canonical law:

```text
MISSING
!=
ZERO
```

and:

```text
UNKNOWN/GAP
!=
ZERO
```

---

# 89. Infinite Values

Infinity is not an ordinary finite measurement.

```text
∞
```

may be used mathematically where defined.

It should not silently represent:

```text
VERY LARGE
UNKNOWN
OVERFLOW
UNBOUNDED OBSERVATION
```

unless explicitly modeled.

---

# 90. Bounds

Quantities may carry:

```yaml
bounds:
  lower:
  upper:
  lower_inclusive:
  upper_inclusive:
```

Bounds may arise from:

```text
PHYSICS
SCHEMA
MODEL
POLICY
NORMALIZATION
OBSERVATION
```

The source of the bound matters.

---

# 91. Valid Range

A schema-valid range is not necessarily a physically valid range.

```text
SCHEMA VALID
!=
DOMAIN VALID
```

Example:

```text
0 <= x <= 1
```

may be structurally valid while semantically invalid for a specific observation.

---

# 92. Canonical Dimensional Validation

Before applying an equation:

```text
LEFT-HAND DIMENSION
=
RIGHT-HAND DIMENSION
```

should hold for physical equations unless the formulation explicitly uses normalized or abstract variables.

Dimensional mismatch is a structural warning.

---

# 93. Abstract AMOS Equations

Many AMOS model equations use normalized or abstract quantities.

Example:

```text
L(X)
=
I(X) · S(X)
```

where:

```text
I
S
L
```

may be dimensionless model quantities.

The registry must not reinterpret abstract model variables as SI physical quantities without canonical evidence.

---

# 94. Model Quantity Firewall

```text
MODEL SCORE
!=
PHYSICAL QUANTITY
```

and:

```text
DIMENSIONLESS MODEL VARIABLE
!=
EMPIRICAL PROBABILITY
```

unless validation establishes the mapping.

---

# 95. Unit Safety in APIs

Interfaces carrying quantities should prefer explicit unit fields.

Preferred:

```json
{
  "value": 250,
  "unit": "ms"
}
```

over:

```json
{
  "latency": 250
}
```

when unit ambiguity is possible.

---

# 96. Unit Safety in Schemas

Typed schemas should constrain:

```text
QUANTITY TYPE
UNIT
VALID RANGE
NULLABILITY
PRECISION
```

where materially necessary.

Schema validation cannot prove empirical correctness.

---

# 97. Unit Safety in Storage

Persistent values should not lose unit identity.

Bad:

```text
42
```

when the field's meaning cannot be reconstructed.

Better:

```yaml
value: 42
unit: ms
quantity_type: LATENCY
```

---

# 98. Unit Safety in Logs

Operational logs should preserve units for numerical telemetry.

Example:

```text
latency_ms=42
```

is preferable to:

```text
latency=42
```

when field schemas are not otherwise available.

---

# 99. Unit Safety in Metrics

Metric names or metadata should distinguish:

```text
seconds
milliseconds
bytes
requests
ratios
percent
counts
```

Prometheus-style naming or another implementation convention may be adopted separately.

This canon does not mandate a specific telemetry platform.

---

# 100. Unit Safety in Models

Model inputs should preserve expected scale.

Example:

```text
temperature_kelvin
```

must not silently receive:

```text
temperature_celsius
```

even though both represent temperature.

---

# 101. Unit Safety in Workflows

Workflow edges passing numerical values should preserve quantity metadata where ambiguity can alter behavior.

Conceptually:

```text
STEP A
  output: 10 ms
↓
STEP B
  expects: seconds
```

requires conversion before consumption.

---

# 102. Unit Safety in Agents

Agents should not infer missing load-bearing units from numeric values when multiple interpretations are plausible.

Example:

```text
"limit = 100"
```

may require clarification or schema lookup if it could mean:

```text
100 USD
100 requests
100 ms
100 MB
100%
```

---

# 103. Unit Safety in Cognition

Cognition must preserve scale when comparing values.

Canonical law:

```text
NUMERIC MAGNITUDE
WITHOUT SEMANTIC NORMALIZATION
CANNOT JUSTIFY COMPARISON
```

---

# 104. Unit Safety in RSCF

A load-bearing quantitative premise should conceptually carry:

```yaml
premise:
  quantity:
  value:
  unit:
  uncertainty:
  provenance:
  scope:
  freshness:
```

where applicable.

This allows later revalidation.

---

# 105. Unit Conversion as Derived Claim

A conversion result is:

```text
DERIVED
```

from:

```text
SOURCE VALUE
+
CONVERSION RULE
```

If either changes, the converted result may require recomputation.

---

# 106. Conversion Dependency

Conceptually:

```text
Q_source
↓
CONVERSION C
↓
Q_target
```

If `C` changes:

```text
Q_target
```

must be invalidated or recomputed where load-bearing.

---

# 107. Currency Units

Currency quantities require explicit currency identity.

Examples:

```text
USD
AUD
VND
EUR
```

Canonical firewall:

```text
100 USD
!=
100 AUD
```

Conversion requires an exchange rate and time context.

---

# 108. Currency Conversion

Currency conversion is time-sensitive.

Conceptually:

```text
TARGET
=
SOURCE × FX_RATE(t)
```

Therefore:

```text
FX CONVERSION
```

inherits:

```text
RATE
TIME
SOURCE
MARKET / PROVIDER
```

It is not a timeless exact conversion.

---

# 109. Monetary Scale

Money should distinguish:

```text
NOMINAL VALUE
REAL VALUE
PRESENT VALUE
FUTURE VALUE
```

when financial reasoning requires it.

These are not interchangeable merely because the currency symbol is identical.

---

# 110. Cost Units

Operational cost should preserve:

```text
CURRENCY
PERIOD
RESOURCE
BILLING MODEL
```

Examples:

```text
USD / month
USD / 1M tokens
USD / request
USD / GPU-hour
```

---

# 111. Energy Units

Energy should use explicit units such as:

```text
J
Wh
kWh
```

where applicable.

Power and energy are distinct:

```text
W
!=
Wh
```

Canonical law:

```text
POWER
!=
ENERGY
```

---

# 112. Data Rate vs Data Quantity

Distinguish:

```text
MB
```

from:

```text
MB/s
```

Canonical law:

```text
DATA SIZE
!=
DATA RATE
```

---

# 113. Frequency

Frequency has units such as:

```text
Hz
=
s^-1
```

A frequency is not a duration.

Conceptually:

```text
period
=
1 / frequency
```

when the reciprocal relationship applies.

---

# 114. Throughput vs Latency

These are different system properties.

```text
HIGH THROUGHPUT
```

does not guarantee:

```text
LOW LATENCY
```

Canonical firewall:

```text
THROUGHPUT
!=
LATENCY
```

---

# 115. Capacity vs Utilization

Capacity is available maximum/resource envelope.

Utilization is used fraction or amount.

```text
UTILIZATION
=
USED / CAPACITY
```

when defined.

Canonical firewall:

```text
UTILIZATION
!=
CAPACITY
```

---

# 116. Availability Measures

Availability may be represented as a ratio:

```text
availability
=
available_time / total_time
```

under an explicitly defined measurement model.

A value such as:

```text
99.9%
```

is incomplete without:

```text
TIME WINDOW
SERVICE DEFINITION
FAILURE CRITERIA
```

---

# 117. Reliability Measures

Reliability may be modeled through different quantities.

Examples:

```text
failure rate
MTBF
success probability
survival function
```

No single universal AMOS reliability unit is asserted here.

---

# 118. MTTR

Mean time to recovery/repair uses a time unit.

But the exact semantic expansion must be explicit if an acronym may vary by domain.

Canonical law:

```text
ACRONYM
!=
UNAMBIGUOUS SEMANTICS
```

---

# 119. Domain-Local Units

A domain may define specialized units if:

```text
STANDARD UNIT IS INSUFFICIENT
AND
SEMANTIC PURPOSE IS EXPLICIT
AND
CONVERSION / INTERPRETATION IS DOCUMENTED
```

Domain-local units must not silently escape their scope.

---

# 120. AMOS-Derived Units

AMOS may define derived internal semantic units such as:

```text
cognitive_step
rscf_count
hypothesis_count
active_cell
trajectory_step
causal_epoch
proof_capsule_count
```

These are structural/operational units, not SI physical units.

---

# 121. No Fake Physicalization

Canonical law:

```text
ABSTRACT AMOS METRIC
!=
PHYSICAL LAW
```

A model variable should not be given physical interpretation merely because it is written mathematically.

---

# 122. No Fake Quantification

If a concept is not operationally measured:

```text
DO NOT INVENT A NUMBER
```

Example:

```text
"system integrity = 0.8734"
```

is unjustified unless a defined measurement/model produces it.

Canonical law:

```text
FORMULA AVAILABLE
!=
MEASUREMENT AVAILABLE
```

---

# 123. Measurement Provenance

Consequential quantitative claims should preserve:

```text
WHO / WHAT MEASURED

WHAT WAS MEASURED

WHEN

WHERE

HOW

WITH WHAT INSTRUMENT / MODEL

IN WHICH UNIT

WITH WHAT UNCERTAINTY
```

---

# 124. Evidence Class

Measured quantities may be classified:

```text
OBSERVATION
```

Converted quantities:

```text
DERIVED
```

Modeled estimates:

```text
MODEL
```

Documentation values:

```text
SOURCE_CLAIM
```

until verified.

---

# 125. Freshness

Many quantities are freshness-bound.

Examples:

```text
price
latency
availability
CPU usage
exchange rate
active user count
system state
```

Canonical law:

```text
VALID QUANTITY AT t1
!=
CURRENT QUANTITY AT t2
```

when the underlying system can change.

---

# 126. Regime Dependence

Measurements can depend on regime.

Example:

```text
latency(normal_load)
!=
latency(peak_load)
```

Therefore:

```text
MEASUREMENT
```

should inherit regime where material.

---

# 127. Scope Dependence

Measurements should preserve scope.

Example:

```text
CPU utilization
```

could mean:

```text
one core
one process
one host
one cluster
```

Without scope the same numeric value may mean different things.

---

# 128. Aggregation

Aggregation functions include:

```text
SUM
MEAN
MEDIAN
MIN
MAX
PERCENTILE
COUNT
RATE
```

Aggregation must preserve unit semantics.

Example:

```text
mean(latency_ms)
```

remains in:

```text
ms
```

---

# 129. Invalid Aggregation

Not every scale permits every aggregation.

Examples:

```text
MEAN(category)
```

is generally invalid.

```text
MEAN(ordinal class)
```

may be semantically questionable unless the scale defines interval meaning.

---

# 130. Weighted Aggregation

Weighted quantities require weight semantics.

Conceptually:

```text
X
=
Σ wi xi
```

with:

```text
Σ wi = 1
```

where normalized weighting is intended.

Weights themselves require provenance when decision-relevant.

---

# 131. Unit Cancellation

For physical or mathematically typed quantities:

```text
(A unit U) / (B unit U)
```

may produce a dimensionless ratio.

But semantic identity can remain.

Example:

```text
successful_requests / total_requests
```

is dimensionless but means:

```text
SUCCESS_RATE
```

---

# 132. Dimensional Analysis Gate

Before accepting a quantitative equation, test:

```text
1. ARE ADDITIONS DIMENSIONALLY COMPATIBLE?

2. ARE MULTIPLICATIONS INTENDED?

3. ARE DENOMINATORS VALID?

4. ARE AFFINE UNITS HANDLED CORRECTLY?

5. ARE NORMALIZED VARIABLES DECLARED?

6. ARE LOG SCALES TREATED CORRECTLY?

7. ARE MODEL SCORES BEING CONFUSED WITH MEASUREMENTS?

8. ARE CONVERSIONS TRACEABLE?
```

---

# 133. Quantity Comparison Gate

Before comparing:

```text
A > B
```

verify:

```text
SAME / COMPARABLE QUANTITY TYPE
+
COMPATIBLE UNITS
+
COMPATIBLE SCALE
+
COMPATIBLE SCOPE
+
COMPATIBLE REGIME
+
SUFFICIENT FRESHNESS
```

where relevant.

---

# 134. Unit Conversion Gate

Before converting:

```text
SOURCE UNIT
↓
TARGET UNIT
```

verify:

```text
DIMENSION COMPATIBLE

CONVERSION DEFINED

CONVERSION TYPE KNOWN

OFFSET HANDLED

PRECISION PRESERVED

CONTEXT SUFFICIENT
```

---

# 135. Registry Statuses

Unit lifecycle states may include:

```text
PLACEHOLDER

DRAFT

CANDIDATE

ACTIVE

DEPRECATED

SUPERSEDED

ARCHIVED
```

Unit lifecycle state must not be confused with epistemic conclusion class.

---

# 136. Deprecated Unit

A deprecated AMOS-local unit should preserve:

```yaml
deprecated_unit:
  unit_id:
  former_definition:
  deprecated_at:
  replacement:
  conversion:
  reason:
  provenance:
```

Historical interpretation must remain possible.

---

# 137. Unit Supersession

```text
UNIT DEFINITION A
↓
SUPERSEDED_BY
↓
UNIT DEFINITION B
```

does not erase historical values expressed under A.

Migration requires explicit conversion or compatibility analysis.

---

# 138. Unit Schema Version

The registry schema version is separate from unit definition versions.

```text
REGISTRY_SCHEMA_VERSION
!=
UNIT_VERSION
```

and:

```text
UNIT_VERSION
!=
AMOS_CORE_VERSION
```

---

# 139. Machine-Readable Registry Example

```yaml
units:
  - unit_id: UNIT-SI-METER
    symbol: m
    canonical_name: meter
    unit_type: PHYSICAL_STANDARD
    dimension: LENGTH
    namespace: SI
    status: ACTIVE

  - unit_id: UNIT-SI-SECOND
    symbol: s
    canonical_name: second
    unit_type: TEMPORAL
    dimension: TIME
    namespace: SI
    status: ACTIVE

  - unit_id: UNIT-COMP-BYTE
    symbol: B
    canonical_name: byte
    unit_type: COMPUTATIONAL
    dimension: INFORMATION
    namespace: COMPUTE
    status: ACTIVE

  - unit_id: UNIT-AMOS-COGNITIVE-STEP
    symbol: cognitive_step
    canonical_name: Cognitive Step
    unit_type: AMOS_DERIVED
    dimension: COUNT
    namespace: AMOS_COGNITION
    status: CANDIDATE

  - unit_id: UNIT-AMOS-CONFIDENCE
    symbol: confidence
    canonical_name: AMOS Confidence
    unit_type: NORMALIZED
    dimension: DIMENSIONLESS
    namespace: AMOS_EPISTEMIC
    status: CANDIDATE
```

---

# 140. Required Registry Invariants

```text
UNIT-001 VALUE != QUANTITY

UNIT-002 UNIT != DIMENSION

UNIT-003 DIMENSIONAL EQUIVALENCE != SEMANTIC EQUIVALENCE

UNIT-004 VALID UNIT != VALID MEASUREMENT

UNIT-005 DIMENSIONALLY VALID != EMPIRICALLY VALID

UNIT-006 REGISTERED != VERIFIED

UNIT-007 NORMALIZED VALUE != PROBABILITY

UNIT-008 CONFIDENCE != PROBABILITY UNLESS CALIBRATED

UNIT-009 CONFIDENCE != AUTHORITY

UNIT-010 MODEL SCORE != PHYSICAL QUANTITY

UNIT-011 COUNT TYPES MUST NOT SILENTLY CONFLATE

UNIT-012 MB != MiB

UNIT-013 BIT != BYTE

UNIT-014 TOKEN != WORD

UNIT-015 TOKEN != CHARACTER

UNIT-016 DURATION != TIMESTAMP

UNIT-017 STEP != ELAPSED TIME

UNIT-018 EPOCH != PHYSICAL TIME

UNIT-019 POWER != ENERGY

UNIT-020 DATA SIZE != DATA RATE

UNIT-021 THROUGHPUT != LATENCY

UNIT-022 CAPACITY != UTILIZATION

UNIT-023 PERCENT != PERCENTAGE POINT

UNIT-024 PRECISION != ACCURACY

UNIT-025 RESOLUTION != UNCERTAINTY

UNIT-026 MISSING != ZERO

UNIT-027 UNKNOWN/GAP != ZERO

UNIT-028 UNDEFINED != ZERO

UNIT-029 APPROXIMATE != EXACT

UNIT-030 SAME SYMBOL != SAME UNIT IDENTITY

UNIT-031 SAME 19×19 ADDRESS SPACE != SAME SEMANTICS

UNIT-032 MORE DIGITS != MORE INFORMATION

UNIT-033 FORMULA AVAILABLE != MEASUREMENT AVAILABLE

UNIT-034 LOCAL UNIT != GLOBAL UNIT

UNIT-035 CONVERSION MUST PRESERVE PROVENANCE WHEN LOAD-BEARING

UNIT-036 MEASUREMENT VALIDITY IS SCOPE-BOUNDED

UNIT-037 MEASUREMENT VALIDITY IS REGIME-AWARE

UNIT-038 MEASUREMENT VALIDITY MAY BE FRESHNESS-BOUNDED

UNIT-039 QUANTIFICATION MUST NOT BE FABRICATED

UNIT-040 OPTIMIZATION MUST NOT REMOVE LOAD-BEARING UNIT SEMANTICS
```

---

# 141. Validation Matrix

| Dimension   | Required question                                   |
| ----------- | --------------------------------------------------- |
| Quantity    | What is being measured?                             |
| Value       | What is the numeric/categorical value?              |
| Unit        | In what unit is it expressed?                       |
| Dimension   | What dimensional class does it belong to?           |
| Scale       | Nominal, ordinal, interval, ratio, log, normalized? |
| Method      | How was it measured or computed?                    |
| Scope       | What system/population/resource does it describe?   |
| Time        | When was it valid?                                  |
| Regime      | Under what conditions?                              |
| Uncertainty | What uncertainty or tolerance applies?              |
| Precision   | How many digits are justified?                      |
| Provenance  | Where did the value come from?                      |
| Conversion  | Was it transformed from another unit?               |
| Version     | Which metric/unit definition applies?               |

---

# 142. Unit Test Families

A mature implementation should test:

```text
UNIT REGISTRATION

UNIT IDENTITY

SYMBOL COLLISIONS

DIMENSION COMPATIBILITY

EXACT CONVERSIONS

AFFINE CONVERSIONS

APPROXIMATE CONVERSIONS

ROUND-TRIP CONVERSIONS

PRECISION PRESERVATION

NULL / MISSING HANDLING

ZERO-DENOMINATOR HANDLING

RANGE VALIDATION

NORMALIZED VALUE VALIDATION

PROBABILITY RANGE VALIDATION

PERCENT / FRACTION CONVERSION

DECIMAL / BINARY BYTE PREFIXES

TIMESTAMP / DURATION SEPARATION

COUNT TYPE SAFETY

19×19 COORDINATE TYPE SAFETY

UNIT VERSION MIGRATION

DEPRECATED UNIT RESOLUTION

PROVENANCE PRESERVATION
```

---

# 143. Adversarial Unit Tests

High-value cases include:

```text
1000 MB TREATED AS 1000 MiB

80% TREATED AS 80.0 NORMALIZED

0.8 CONFIDENCE TREATED AS 0.8 PROBABILITY

CELSIUS VALUES MULTIPLIED AS ABSOLUTE RATIO SCALE

TOKEN COUNT TREATED AS WORD COUNT

STEP COUNT TREATED AS SECONDS

19×19 GO CELL TREATED AS COGNITION FIELD CELL

SAME DIMENSION USED TO CLAIM SAME SEMANTICS

NULL INPUT TREATED AS ZERO

DIVISION BY ZERO TREATED AS ZERO

ROUNDED VALUE REPORTED WITH FAKE PRECISION

STALE EXCHANGE RATE USED AS TIMELESS CONVERSION

MODEL SCORE PRESENTED AS PHYSICAL MEASUREMENT

UNIT REMOVED DURING SERIALIZATION

CONVERSION HISTORY LOST

METRIC FORMULA CHANGED WITHOUT VERSION CHANGE
```

---

# 144. Anti-Fabrication Rules

Do not invent:

```text
UNITS

CONVERSION FACTORS

CALIBRATION CONSTANTS

PRECISION

UNCERTAINTY

MEASUREMENT VALUES

NORMALIZATION RULES

SCALE DEFINITIONS
```

merely to complete a schema.

If a load-bearing quantity lacks its unit:

```text
UNIT = UNKNOWN/GAP
```

is preferable to guessing.

---

# 145. Gap Classification

Unit-related gaps may be:

```text
CRITICAL
```

when the missing unit can reverse meaning or cause unsafe action.

```text
DECISION-RELEVANT
```

when the missing scale/conversion may alter the decision.

```text
EXPLANATORY
```

when interpretation is reduced but action remains unchanged.

```text
COSMETIC
```

when only presentation formatting is absent.

Resolve in that order.

---

# 146. RSCF Node

```yaml
node_id: AMOS_UNIT_REGISTRY

functional_type:
  - UNIT_REGISTRY
  - DIMENSION_REGISTRY
  - QUANTITY_SEMANTICS_REGISTRY
  - MEASUREMENT_GOVERNANCE_MODEL

lifecycle_stage:
  CANON_CANDIDATE

origin_architect:
  Trang Phan

steward:
  Trang Phan

amos_core_target:
  v4.4

claim_class:
  AMOS_MODEL

claim: >
  AMOS OS requires a typed unit and quantity registry that preserves
  dimension, unit identity, scale, conversion semantics, precision,
  uncertainty, scope, regime, freshness, provenance, and version
  boundaries so that numerically compatible values are not silently
  treated as semantically equivalent quantities.

critical_invariants:
  - VALUE != QUANTITY
  - UNIT != DIMENSION
  - DIMENSIONAL EQUIVALENCE != SEMANTIC EQUIVALENCE
  - VALID UNIT != VALID MEASUREMENT
  - NORMALIZED VALUE != PROBABILITY
  - CONFIDENCE != AUTHORITY
  - SAME SYMBOL != SAME UNIT IDENTITY
  - APPROXIMATE != EXACT
  - MISSING != ZERO
  - UNKNOWN/GAP != ZERO
  - QUANTIFICATION MUST NOT BE FABRICATED
  - CONVERSION MUST PRESERVE LOAD-BEARING PROVENANCE

dependencies:
  - SYMBOL_REGISTRY
  - INVARIANT_REGISTRY
  - AMOS_CORE_LAWS
  - HML_CANON
  - PERSISTENCE_CANON
  - SCHEMA_MAP
  - PROVENANCE

known_gaps:
  - Full inventory of AMOS-local metric units requires corpus extraction.
  - Exact normalization contracts for all existing AMOS metrics require source binding.
  - Full unit collision analysis across the AMOS corpus remains incomplete.
  - Machine-readable registry schema requires final schema binding.
  - Historical metric definition versions require provenance reconstruction.

does_not_establish:
  - measurement correctness
  - empirical validation
  - calibration correctness
  - complete AMOS unit inventory
  - implementation completeness
```

---

# 147. Promotion Gate

Promotion:

```text
ACTIVE_CANON_CANDIDATE
→
ACTIVE_CANON
```

requires at minimum:

```text
CORPUS QUANTITY EXTRACTION
↓
UNIT EXTRACTION
↓
DIMENSION CLASSIFICATION
↓
SCALE CLASSIFICATION
↓
COLLISION ANALYSIS
↓
NORMALIZATION AUDIT
↓
CONVERSION AUDIT
↓
PROVENANCE BINDING
↓
VERSION RECONSTRUCTION
↓
SCHEMA VALIDATION
↓
CANON REVIEW
```

Unknown unit semantics must remain unresolved rather than being invented during promotion.

---

# 148. Changelog

## v1.0.0 — 2026-08-25

Expanded the original placeholder into an AMOS Core v4.4-aligned Unit Registry candidate.

Added:

- canonical quantity identity model;
- unit record schema;
- physical, computational, temporal, count, ratio, rate, normalized, logarithmic, and domain-local unit classes;
- base and derived physical unit references;
- dimensional vectors;
- dimensional/semantic firewall;
- exact and approximate conversions;
- affine conversions;
- scale classes;
- typed counts;
- percentage and probability rules;
- confidence/probability firewall;
- normalized AMOS quantities;
- rate, throughput, and latency units;
- timestamps, durations, epochs, and step distinctions;
- decimal/binary data units;
- token semantics;
- 19×19 coordinate/count semantics;
- graph count typing;
- scores and index versioning;
- measurement method and calibration;
- precision/accuracy/resolution distinctions;
- uncertainty and interval semantics;
- missing/zero/undefined firewall;
- dimensional-analysis gates;
- currency and cost units;
- infrastructure quantity semantics;
- schema/API/storage/logging unit safety;
- provenance-aware conversion;
- freshness, regime, and scope requirements;
- unit invariants;
- test families;
- adversarial tests;
- anti-fabrication rules;
- promotion gate.

---

# 149. Canonical Summary

A complete quantity is not merely:

```text
42
```

It is conceptually:

```text
QUANTITY
=
VALUE
+
UNIT
+
DIMENSION
+
SCALE
+
CONTEXT
```

and for consequential measurement:

```text
QUANTITY
=
VALUE
+
UNIT
+
DIMENSION
+
SCALE
+
METHOD
+
UNCERTAINTY
+
SCOPE
+
REGIME
+
TIME
+
PROVENANCE
```

Canonical evaluation path:

```text
INPUT VALUE
↓
IDENTIFY QUANTITY
↓
IDENTIFY UNIT
↓
IDENTIFY DIMENSION
↓
IDENTIFY SCALE
↓
VALIDATE RANGE
↓
VALIDATE SCOPE / REGIME
↓
VALIDATE CONVERSION
↓
PRESERVE PRECISION / UNCERTAINTY
↓
PRESERVE PROVENANCE
↓
USE IN REASONING
```

Core laws:

```text
VALUE != QUANTITY

UNIT != DIMENSION

SAME NUMBER != SAME QUANTITY

SAME DIMENSION != SAME SEMANTICS

VALID UNIT != VALID MEASUREMENT

DIMENSIONALLY VALID != EMPIRICALLY VALID

NORMALIZED VALUE != PROBABILITY

CONFIDENCE != PROBABILITY UNLESS CALIBRATED

CONFIDENCE != AUTHORITY

MODEL SCORE != PHYSICAL QUANTITY

MB != MiB

TOKEN != WORD

STEP != TIME

EPOCH != SECOND

DURATION != TIMESTAMP

PERCENT != PERCENTAGE POINT

PRECISION != ACCURACY

MISSING != ZERO

UNKNOWN/GAP != ZERO

APPROXIMATE != EXACT

FORMULA AVAILABLE != MEASUREMENT AVAILABLE

QUANTIFICATION MUST NOT BE FABRICATED
```

Canonical objective:

```text
TYPE EVERY LOAD-BEARING QUANTITY.

NAME ITS UNIT.

NAME ITS DIMENSION.

NAME ITS SCALE.

PRESERVE ITS ORIGINAL VALUE.

PRESERVE ITS CONVERSION HISTORY.

PRESERVE ITS UNCERTAINTY.

PRESERVE ITS SCOPE.

PRESERVE ITS REGIME.

PRESERVE ITS FRESHNESS.

PRESERVE ITS PROVENANCE.

DO NOT CONFUSE
NUMERICAL EQUALITY
WITH SEMANTIC EQUALITY.

DO NOT CONFUSE
DIMENSIONAL COMPATIBILITY
WITH CAUSAL OR CONCEPTUAL IDENTITY.

DO NOT TURN
A SCORE INTO A MEASUREMENT,
A CONFIDENCE INTO A PROBABILITY,
A TOKEN INTO A WORD,
A STEP INTO TIME,
OR A MISSING VALUE INTO ZERO.

WHEN THE UNIT OR SCALE
IS LOAD-BEARING AND UNKNOWN,
KEEP IT UNKNOWN/GAP.
```

---

**Related:** README|AMOS OS · [[ARCHITECTURE]]|Architecture · [[00_ROOT_NAMING_STANDARD]]|Naming Standard · [[PLACEMENT_RULES]]|Placement Rules · [[CANON_MAP]]|Canon Map · [[AMOS_CORE_LAWS|AMOS Core Laws]] · [[INVARIANT_REGISTRY]]|Invariant Registry · [[LAW_HIERARCHY]]|Law Hierarchy · [[SYMBOL_REGISTRY]]|Symbol Registry · [[HML_CANON]]|H/M/L Canon · [[PERSISTENCE_CANON]]|Persistence Canon · [[COGNITION_CANON]]|Cognition Canon · [[INFRASTRUCTURE_CANON]]|Infrastructure Canon · [[KERNEL_MAP]]|Kernel Map · [[RUNTIME_MAP]]|Runtime Map · [[COGNITIVE_ORGANISM_MAP]]|Cognitive Organism Map · Knowledge Map · [[STATE_STATE_MAP]]|State Map · [[MODEL_MAP]]|Model Map · [[SCHEMA_MAP]]|Schema Map · [[OBSERVABILITY_OBSERVABILITY_MAP]]|Observability Map · [[TEST_MAP]]|Test Map · [[INDEX_RESEARCH_README]]|Research · [[COGNITIVE_MATRIX_ARCHITECTURE]]|Cognitive Matrix

```text
```

---

[[00_ROOT_MOC]]|[[AMOS MOC]]

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: unit_registry
node_type: note
path: 01_CANON/05_VARIABLE_REGISTRY/UNIT_REGISTRY.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[05_VARIABLE_REGISTRY_MOC]]
