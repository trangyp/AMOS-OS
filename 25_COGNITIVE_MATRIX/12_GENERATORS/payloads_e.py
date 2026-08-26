"""Payloads E: control planes C01–C09 + scales H/M/L."""
from payloads_a import _base

PAYLOADS = {}

PAYLOADS["C01"] = _base(
    "C01", "GOVERNANCE",
    "The supreme authority plane: encodes laws, resolves precedence, grants/denies authority, and vetoes unconditionally.",
    "Covers law-stack enforcement (Law of Law, Rule of 2/4), authority envelopes, enforcement-root attestation, and fail-closed defaults.",
    inputs=["Canon laws & policies", "Authorization requests", "Enforcement attestations"],
    outputs=["Authority decisions", "Vetoes", "Precedence resolutions"],
    deps_up=[], deps_down=["C03_EXECUTIVE", "C08_EXECUTION", "L28_GOVERNANCE"],
    semantics=[
        "Ethical veto overrides all output metrics absolutely.",
        "Reasoning-shape is not authorization: passing a gate pattern does not grant effect rights.",
        "Fail-closed: absent authority = denial with stated reason.",
    ],
    invariants=[(1, "Enforcement roots are attested and agent-write-excluded."),
                (2, "Precedence order is declared, deterministic, and immutable at runtime."),
                (3, "Every consequential decision carries a receipt.")],
    failure_modes=[("01", "Transitive bypass of one-hop gating.", "full-path gate audit",
                    "Close escape path; re-audit all effect paths."),
                   ("02", "Mutable enforcement root.", "root attestation epoch check",
                    "Freeze; restore sealed baseline; investigate writer."),
                   ("03", "Silent authority expansion.", "envelope diffing",
                    "Revoke; log as governance violation into G3.")],
    control_planes=["C09_KERNEL_CONTROL"],
    tests=["Ethical veto beats best-metric alternative in adversarial suite",
           "Root tamper detected within one epoch",
           "Denials always carry reasons"],
)

PAYLOADS["C02"] = _base(
    "C02", "METACOGNITIVE",
    "Owns self-monitoring: confidence calibration, drift detection, anomaly interrupts.",
    "Covers monitor registry, interrupt taxonomy, and self-report calibration discipline.",
    inputs=["Internal traces", "Outcome history"],
    outputs=["Interrupts", "Calibration reports"],
    deps_up=[], deps_down=["C03_EXECUTIVE", "L23_METACOGNITION"],
    semantics=["Self-reports are predictions: they are scored like any forecast."],
    invariants=[(1, "Confidence cap enforced mechanically (0.95)."),
                (2, "Unresolved anomaly halts escalation (fail-closed interrupts).")],
    control_planes=["C01_GOVERNANCE"],
)

PAYLOADS["C03"] = _base(
    "C03", "EXECUTIVE",
    "Coordinates goal selection, planning, and resource arbitration across the system.",
    inputs=["Goals", "Plans", "Budgets"],
    outputs=["Arbitrated execution directives"],
    deps_up=["C01_GOVERNANCE"], deps_down=["C08_EXECUTION"],
    semantics=["Resource arbitration is zero-sum and priority-floored for safety tasks."],
    control_planes=["C01_GOVERNANCE"],
)

PAYLOADS["C04"] = _base(
    "C04", "REASONING",
    "Hosts inference, causal modeling, simulation, and derivation-lineage discipline.",
    inputs=["Knowledge structures", "Queries"],
    outputs=["Derived claims with lineage"],
    deps_up=["C05_REPRESENTATION"], deps_down=[],
    semantics=["All derived claims carry lineage and inherit minimum premise confidence."],
    control_planes=["C01_GOVERNANCE"],
)

PAYLOADS["C05"] = _base(
    "C05", "REPRESENTATION",
    "Governs internal encodings and cross-representation translation fidelity.",
    inputs=["Structures to encode"],
    outputs=["Typed representations", "Translation receipts"],
    semantics=["Translation never silently changes claim class or drops information without logging."],
    control_planes=["C04_REASONING"],
)

PAYLOADS["C06"] = _base(
    "C06", "MEMORY",
    "Owns durable storage, trust lifecycle, consolidation thresholds, retrieval diversity.",
    inputs=["Write candidates", "Retrieval queries"],
    outputs=["Stored objects", "Evidence sets"],
    invariants=[(1, "Trust-state assignment precedes any write."),
                (2, "Contradiction quota ≥1 when contradictions exist.")],
    control_planes=["C01_GOVERNANCE"],
)

PAYLOADS["C07"] = _base(
    "C07", "PERCEPTION",
    "Channels reality contact into typed observations via grounding gates.",
    inputs=["Raw observations"],
    outputs=["Grounded typed observations"],
    semantics=["Reality gate fails closed."],
    control_planes=["C09_KERNEL_CONTROL"],
)

PAYLOADS["C08"] = _base(
    "C08", "EXECUTION",
    "Executes authorized effects through tools/effectors with transactional safety.",
    inputs=["Authorized actions"],
    outputs=["Effect results", "Execution receipts"],
    invariants=[(1, "No external write passes can_write/can_delete checks."),
                (2, "Partial failures invoke compensation paths.")],
    control_planes=["C01_GOVERNANCE", "C09_KERNEL_CONTROL"],
)

PAYLOADS["C09"] = _base(
    "C09", "KERNEL_CONTROL",
    "Lowest-level control: boot integrity, kernel state ownership, substrate health.",
    inputs=["Kernel telemetry"],
    outputs=["Boot verdicts", "Substrate health reports"],
    semantics=["Boot is fail-closed: unresolved kernel anomalies prevent subsystem start."],
    control_planes=["C01_GOVERNANCE"],
)

# ---- Scales ----
_scales_common = dict(control_planes=["C01_GOVERNANCE"], cp_roles={"C01_GOVERNANCE": "scale-governance owner"})

PAYLOADS["SCALE_H"] = _base(
    "H", "HIGH_SCALE",
    "H scale governs system-level structure: laws, architectures, cross-domain composition.",
    scope="Applies where claims span whole systems or canon layers; strictness ladder: exact > statistical > metaphorical.",
    inputs=["System-level artifacts"],
    outputs=["Governed system structures"],
    hml={"H": "This package IS the H scale.", "M": "H-level rules bind M mechanisms.", "L": "H-level laws constrain what L evidence may support."},
    **_scales_common,
)

PAYLOADS["SCALE_M"] = _base(
    "M", "MID_SCALE",
    "M scale covers intermediate/subsystem objects and processes — the mechanism layer.",
    scope="Subsystem contracts, operators, package mechanics.",
    inputs=["Subsystem artifacts"],
    outputs=["Mechanism definitions"],
    hml={"H": "M translates H intent into mechanisms.", "M": "This package IS the M scale.", "L": "M mechanisms instantiate over L evidence."},
    **_scales_common,
)

PAYLOADS["SCALE_L"] = _base(
    "L", "LOW_SCALE",
    "L scale binds concrete evidence, measurements, and detail-level verification.",
    scope="Evidence items, measured values, per-artifact validation.",
    inputs=["Evidence records"],
    outputs=["Verified details"],
    hml={"H": "L evidence supports but never overrides H law.", "M": "L instantiates M mechanisms.", "L": "This package IS the L scale."},
    **_scales_common,
)
