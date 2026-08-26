"""Payloads D2: lifecycle operations O09–O16."""
from payloads_a import _base

PAYLOADS = {}

PAYLOADS["O09"] = _base(
    "O09", "SIMULATION",
    "Runs counterfactual/what-if evaluations over models with pessimism-corrected verdicts.",
    invariants=[(1, "Stable verdicts require all branches stable.")],
    deps_up=["O06_MODEL", "O07_INFERENCE"], deps_down=["O10_VALUE"],
)

PAYLOADS["O10"] = _base(
    "O10", "VALUE",
    "Assigns value/risk under declared preferences with explicit conflict surfacing.",
    invariants=[(1, "Conflicts surface as fronts; ethical constraints are vetoes.")],
    deps_up=["O08_PREDICTION", "O09_SIMULATION"], deps_down=["O11_GOAL"],
)

PAYLOADS["O11"] = _base(
    "O11", "GOAL",
    "Forms typed goals with falsifiable success criteria and cycle-free decomposition.",
    invariants=[(1, "No goal cycles (transitive self-dependence = defect).")],
    deps_up=["O10_VALUE"], deps_down=["O12_PLAN"],
)

PAYLOADS["O12"] = _base(
    "O12", "PLAN",
    "Synthesizes feasible, contingency-embedded action sequences.",
    invariants=[(1, "Feasibility enforced at full precision."),
                (2, "Every plan carries an abort path.")],
    deps_up=["O11_GOAL"], deps_down=["O13_DECISION"],
)

PAYLOADS["O13"] = _base(
    "O13", "DECISION",
    "Selects among alternatives with receipted rationale and authority check.",
    invariants=[(1, "Rejections carry rationale; decisions carry receipts.")],
    deps_up=["O12_PLAN"], deps_down=["O14_ACTION"],
)

PAYLOADS["O14"] = _base(
    "O14", "ACTION",
    "Executes decisions under capability≠authority discipline.",
    invariants=[(1, "Per-task authority grant required; denial reasons stated.")],
    deps_up=["O13_DECISION"], deps_down=["O15_OBSERVATION"],
)

PAYLOADS["O15"] = _base(
    "O15", "OBSERVATION",
    "Grounds action outcomes via reality channels and closes the loop.",
    invariants=[(1, "Ungrounded outcomes stay PENDING, never scored.")],
    deps_up=["O14_ACTION"], deps_down=["O16_LEARNING"],
)

PAYLOADS["O16"] = _base(
    "O16", "LEARNING",
    "Updates structure from outcome credit within mutation-gated, rollback-capable evolution.",
    invariants=[(1, "Mutation gate precedes every update; updates reversible until validated.")],
    deps_up=["O15_OBSERVATION"], deps_down=["O05_MEMORY"],
)
