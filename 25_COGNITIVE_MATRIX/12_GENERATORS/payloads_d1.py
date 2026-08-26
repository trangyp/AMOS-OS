"""Payloads D1: lifecycle operations O00–O08."""
from payloads_a import _base

PAYLOADS = {}

PAYLOADS["O00"] = _base(
    "O00", "DISTINCTION",
    "The foundational operation: drawing a boundary that makes something distinguishable from what it is not.",
    "Covers distinction creation, scope typing, and distinctness verification.",
    inputs=["Candidate object", "Scope declaration"],
    outputs=["Distinction record", "Typed boundary"],
    deps_up=[], deps_down=["O01_OBJECT", "O02_RELATION"],
    semantics=["A distinction is only valid within a declared scope; cross-scope equivalence requires reconciliation."],
    invariants=[(1, "is_distinct_from checks scope compatibility before equivalence."),
                (2, "Wildcard scopes never silently merge cross-regime claims.")],
    failure_modes=[("01", "Cross-regime conflation via loose scope.", "scope-compat gate",
                    "Block; require explicit regime tags on both sides."),
                   ("02", "Distinction without repair capacity behind it.", "DMER L3 check",
                    "Flag exposure: resolution growth must pair with repair growth.")],
    control_planes=["C04_REASONING", "C05_REPRESENTATION"],
)

PAYLOADS["O01"] = _base(
    "O01", "OBJECT",
    "Forms and maintains typed objects from distinctions — the unit of reference in the substrate.",
    inputs=["Distinction records"],
    outputs=["Typed objects"],
    deps_up=["O00_DISTINCTION"], deps_down=["O02_RELATION", "O03_BINDING"],
)

PAYLOADS["O02"] = _base(
    "O02", "RELATION",
    "Creates typed directed links among objects with semantic-compatibility enforcement.",
    inputs=["Objects", "Relation types"],
    outputs=["Typed relations"],
    deps_up=["O01_OBJECT"], deps_down=["O03_BINDING", "O07_INFERENCE"],
)

PAYLOADS["O03"] = _base(
    "O03", "BINDING",
    "Composes objects and relations into bound structures under tensor-composition governance.",
    semantics=["Same-name axes do not prove same meaning; composition passes the 5-check gate."],
    invariants=[(1, "Composition requires domain match + declared semantics + provenance class inheritance."),
                (2, "Silent composition invalidates the output (G11).")],
    deps_up=["O01_OBJECT", "O02_RELATION"], deps_down=["O04_STATE", "O06_MODEL"],
)

PAYLOADS["O04"] = _base(
    "O04", "STATE",
    "Establishes and transitions typed state for bound structures.",
    invariants=[(1, "State transitions preserve type integrity."),
                (2, "Invalid data never enters to propagate (write-time checks).")],
    deps_up=["O03_BINDING"], deps_down=["O05_MEMORY", "O07_INFERENCE"],
)

PAYLOADS["O05"] = _base(
    "O05", "MEMORY",
    "Persists structures with trust-state lifecycle and retrieval diversity guarantees.",
    invariants=[(1, "Contradiction quota enforced at retrieval."),
                (2, "Falsified content marked REVOKED/FALSIFIED, never silently removed.")],
    deps_up=["O04_STATE"], deps_down=["O06_MODEL", "O07_INFERENCE"],
)

PAYLOADS["O06"] = _base(
    "O06", "MODEL",
    "Constructs structural models over stored structures; always MODEL-class output.",
    invariants=[(1, "Model artifacts never claim SOURCE class.")],
    deps_up=["O05_MEMORY"], deps_down=["O07_INFERENCE", "O08_PREDICTION"],
)

PAYLOADS["O07"] = _base(
    "O07", "INFERENCE",
    "Applies rules over models/structures with lineage and conditional-carry propagation.",
    invariants=[(1, "Derived confidence ≤ min premise confidence."),
                (2, "CONDITIONAL-ON carried through all dependents.")],
    deps_up=["O05_MEMORY", "O06_MODEL"], deps_down=["O08_PREDICTION", "O09_SIMULATION"],
)

PAYLOADS["O08"] = _base(
    "O08", "PREDICTION",
    "Emits forecasts with uncertainty bands and horizon discipline.",
    invariants=[(1, "No bandless predictions.")],
    deps_up=["O07_INFERENCE"], deps_down=["O10_VALUE"],
)
