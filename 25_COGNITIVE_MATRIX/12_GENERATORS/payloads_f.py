"""Payloads F: infrastructure subsystems (05-11)."""
from payloads_a import _base

PAYLOADS = {}

_c = dict(control_planes=["C01_GOVERNANCE"], cp_roles={"C01_GOVERNANCE": "infrastructure governance owner"})

PAYLOADS["CELL_INDEX"] = _base(
    "CELL_REGISTRY", "CELL_INDEX",
    "Registry of all cognitive-matrix cells: addressable units combining primitive × operation × scale.",
    scope="Enumerates cell IDs, status classes, and ownership. Cell = (L-primitive, O-operation, HML-scale) triple.",
    inputs=["Package contracts", "Status updates"],
    outputs=["Cell index", "Status map"],
    tests=["Every declared cell resolves to owning packages", "No duplicate cell addresses", "Status transitions logged"],
)

PAYLOADS["CELL_STATUS_REGISTRY"] = _base(
    "CELL_STATUS_REGISTRY", "CELL_STATUS",
    "Tracks per-cell lifecycle status: PLACEHOLDER → CONTRACT_FILLED → IMPLEMENTED → VALIDATED → PROMOTED.",
    semantics=["Status advances only on evidence; regression is allowed and recorded."],
    invariants=[(1, "TEST_EXECUTED != SYSTEM_VALIDATED; each transition has its own gate.")],
    **_c,
)

PAYLOADS["CELL_AUTHORITY"] = _base(
    "CELL_CONTRACTS", "CELL_AUTHORITY",
    "Defines what authority each cell may exercise and which control plane grants it.",
    semantics=["Capability != authority; every effect right is granted per-task by C01."],
    **_c,
)

PAYLOADS["CELL_BINDINGS"] = _base(
    "CELL_CONTRACTS", "CELL_BINDINGS",
    "Declares runtime bindings between cells and executable substrates (engines, agents).",
    semantics=["A binding without a running substrate is UNKNOWN/GAP, never assumed live."],
    **_c,
)

PAYLOADS["CELL_EVIDENCE"] = _base(
    "CELL_CONTRACTS", "CELL_EVIDENCE",
    "Evidence requirements per cell class: what observations validate each cell type.",
    semantics=["Evidence class must match claim class; MODEL claims cannot be validated by anecdote."],
    **_c,
)

PAYLOADS["CELL_STATE"] = _base(
    "CELL_CONTRACTS", "CELL_STATE",
    "Per-cell state schema and ownership rules.",
    invariants=[(1, "Cells own no global state; shared state lives in the state plane with leases.")],
    **_c,
)

PAYLOADS["COVERAGE_THRESHOLDS"] = _base(
    "COVERAGE", "THRESHOLDS",
    "Declared coverage thresholds per dimension and the measurement method for each.",
    semantics=["Coverage is measured, not asserted; each threshold names its counter."],
    tests=["Threshold counters reproduce from raw state", "Dimensions are independent (no double-counting)"],
    **_c,
)

PAYLOADS["COVERAGE_AUDIT"] = _base(
    "COVERAGE", "AUDIT",
    "Audit procedure comparing measured coverage against thresholds with receipted deltas.",
    **_c,
)

PAYLOADS["COVERAGE_MODEL"] = _base(
    "COVERAGE", "MODEL",
    "The coverage tensor model: package × artifact × epistemic-class dimensions.",
    **_c,
)

PAYLOADS["GAP_PRIORITY"] = _base(
    "STRUCTURAL_GAPS", "GAP_PRIORITY",
    "Prioritization rules for structural gaps: impact × reachability × repair cost.",
    **_c,
)

PAYLOADS["GAP_REGISTRY"] = _base(
    "STRUCTURAL_GAPS", "REGISTRY",
    "Registry of known gaps with honest UNKNOWN/GAP classification — the anti-hallucination ledger.",
    semantics=["Gaps stay visible until closed; closing requires evidence, not assertion."],
    **_c,
)

PAYLOADS["GAP_PROMOTION"] = _base(
    "STRUCTURAL_GAPS", "PROMOTION",
    "Rules for promoting gap→filled→validated states with evidence gates at each hop.",
    **_c,
)

PAYLOADS["DEPENDENCY_TYPES"] = _base(
    "DEPENDENCY_GRAPH", "TYPES",
    "Typed dependency edges: data, control, authority, and freshness dependencies.",
    semantics=["Authority dependencies propagate no higher than their minimum source."],
    **_c,
)

PAYLOADS["INVALIDATION_RULES"] = _base(
    "DEPENDENCY_GRAPH", "INVALIDATION",
    "Selective invalidation: when upstream change propagates downstream and how deep.",
    invariants=[(1, "Invalidation depth is bounded and logged; unbounded invalidation is a defect."),
                (2, "Freshness epochs gate staleness propagation.")],
    **_c,
)

PAYLOADS["DEPENDENCY_AUDIT"] = _base(
    "DEPENDENCY_GRAPH", "AUDIT",
    "Cycle detection and orphan-edge audit over the dependency graph.",
    tests=["DAG property holds for structured dependency sets", "Cycles reported as defects"],
    **_c,
)

PAYLOADS["ROUTING_POLICY"] = _base(
    "ROUTING", "POLICY",
    "Constitutional routing policy: how tasks route to cells/planes with fail-closed defaults.",
    semantics=["Routing follows declared precedence; registration order never confers authority."],
    tests=["T-RPOL constitutional suite executes green (see ROUTING_POLICY_VALIDATION_RECEIPT)"],
    **_c,
)

PAYLOADS["BINDING_RULES"] = _base(
    "ROUTING", "BINDING_RULES",
    "Invariants binding routes to capabilities: I-BIND invariant family.",
    **_c,
)

PAYLOADS["ROUTING_AUDIT"] = _base(
    "ROUTING", "AUDIT",
    "Route-integrity audit: wildcard-scope capture and registration-order manipulation probes.",
    **_c,
)

PAYLOADS["VALIDATION_README"] = _base(
    "VALIDATION", "OVERVIEW",
    "Validation layer overview: promotion gates, evidence receipts, and executed-vs-declared separation.",
    semantics=["EXECUTED-VALIDATED logic is kept separate from UNKNOWN/GAP runtime enforcement."],
    **_c,
)
