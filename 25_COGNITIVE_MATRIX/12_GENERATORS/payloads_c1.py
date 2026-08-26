"""Payloads C1: primitives L17–L22."""
from payloads_a import _base

PAYLOADS = {}

PAYLOADS["L17"] = _base(
    "L17", "DECISION",
    "Selects one action/plan among candidates under uncertainty, with recorded rationale.",
    "Covers decision policy, tie-breaking, and decision-receipt emission.",
    inputs=["Feasible plans", "Valued estimates"],
    outputs=["Selected action", "Decision receipt"],
    deps_up=["L16_PLANNING", "L14_VALUATION"], deps_down=["L18_ACTION"],
    semantics=["Every consequential decision emits a receipt: alternatives considered, rejection rationale, evidence used."],
    invariants=[(1, "Rejection requires stated rationale (no silent elimination)."),
                (2, "Decisions under irreducible uncertainty record the uncertainty class.")],
    failure_modes=[("01", "Rubber-stamp selection with no real comparison.", "alternative-set audit",
                    "Reject receipt; force genuine comparison."),
                   ("02", "Decision executed without authorization scope.", "authority check (C01)",
                    "Halt; escalate to governance plane.")],
    control_planes=["C03_EXECUTIVE", "C01_GOVERNANCE"],
)

PAYLOADS["L18"] = _base(
    "L18", "ACTION",
    "Executes selected decisions through effectors/tools under capability and authority bounds.",
    "Covers action dispatch, capability gating, and execution receipts.",
    inputs=["Selected action", "Capability grants"],
    outputs=["Execution results", "Effect receipts"],
    deps_up=["L17_DECISION"], deps_down=["L19_OUTCOME_OBSERVATION"],
    semantics=["Capability ≠ authority: having the ability to act does not authorize the effect."],
    invariants=[(1, "No effect executes without a per-task authority grant; denial reasons are always stated."),
                (2, "External writes are gated by can_write/can_delete checks.")],
    failure_modes=[("01", "Effect lands outside declared scope.", "scope assertion post-check",
                    "Roll back if possible; revoke grant; log violation."),
                   ("02", "Tool failure mid-action leaves partial state.", "transactional wrapper",
                    "Invoke compensation path; mark state for repair review.")],
    control_planes=["C08_EXECUTION", "C01_GOVERNANCE"],
)

PAYLOADS["L19"] = _base(
    "L19", "OUTCOME_OBSERVATION",
    "Observes the real results of actions and closes the perception–action loop.",
    "Covers outcome grounding, delay handling, and confounder exposure.",
    inputs=["Effect receipts", "Environment observations"],
    outputs=["Grounded outcomes"],
    deps_up=["L18_ACTION", "L00_REALITY_ENVIRONMENT"], deps_down=["L20_CREDIT_ASSIGNMENT"],
    semantics=["An outcome not grounded via L00 channels is an assumed outcome and is tagged as such."],
    invariants=[(1, "Outcome records link back to the originating effect receipt."),
                (2, "Delayed outcomes keep pending status rather than being scored prematurely.")],
    failure_modes=[("01", "Confounder credited as outcome cause.", "confounder review",
                    "Flag attribution; route to causal analysis."),
                   ("02", "Premature scoring of pending outcomes.", "pending-state guard",
                    "Restore pending; recompute when grounded.")],
    control_planes=["C07_PERCEPTION", "C08_EXECUTION"],
)

PAYLOADS["L20"] = _base(
    "L20", "CREDIT_ASSIGNMENT",
    "Attributes success/failure across the chain of decisions and components that produced an outcome.",
    "Covers temporal credit decay, counterfactual attribution, and blame-symmetry rules.",
    inputs=["Grounded outcomes", "Decision/action lineage"],
    outputs=["Credit/blame assignments"],
    deps_up=["L19_OUTCOME_OBSERVATION"], deps_down=["L21_LEARNING"],
    semantics=["Credit follows the lineage graph with decay over distance, not recency alone."],
    invariants=[(1, "Blame and credit use symmetric standards (no self-serving asymmetry)."),
                (2, "Attribution beyond lineage resolution depth is marked UNKNOWN/GAP.")],
    failure_modes=[("01", "Recency bias overweights last step.", "lineage-weight audit",
                    "Recompute with decay model; log correction."),
                   ("02", "Shared-cause double counting.", "independence check (DMER L5)",
                    "Deduplicate by failure-mode independence before scoring.")],
    control_planes=["C03_EXECUTIVE", "C04_REASONING"],
)

PAYLOADS["L21"] = _base(
    "L21", "LEARNING",
    "Updates models, policies, and representations from credit-assigned experience within bounded evolution rules.",
    "Covers update gating, catastrophic-forgetting protection, and evolution-authority checks.",
    inputs=["Credit assignments", "Current model state"],
    outputs=["Updated models/policies", "Evolution log entries"],
    deps_up=["L20_CREDIT_ASSIGNMENT"], deps_down=["L22_CONSOLIDATION", "L29_EVOLUTION"],
    semantics=["Learning updates are mutations: they pass through mutation gates and are reversible until validated."],
    invariants=[(1, "No update bypasses the mutation gate (canon law stack)."),
                (2, "Updates remain rollback-capable until promoted by validation evidence.")],
    failure_modes=[("01", "Single anomalous event drives large update.", "update-magnitude bound",
                    "Clamp magnitude; require corroboration."),
                   ("02", "New learning erases prior competence.", "regression suite on core tasks",
                    "Revert update; add replay of core corpus.")],
    control_planes=["C01_GOVERNANCE", "C02_METACOGNITIVE"],
)

PAYLOADS["L22"] = _base(
    "L22", "CONSOLIDATION",
    "Promotes repeatedly-validated working knowledge into durable memory structures.",
    "Covers consolidation thresholds, deduplication at write time, and index maintenance.",
    inputs=["Validated learning updates"],
    outputs=["Consolidated memory objects"],
    deps_up=["L21_LEARNING", "L07_MEMORY"], deps_down=["L07_MEMORY"],
    semantics=["Only knowledge surviving repeated validation crosses the consolidation threshold."],
    invariants=[(1, "Consolidation requires threshold confirmations, never single-shot promotion."),
                (2, "Consolidated items are de-duplicated against existing store (isomorphic claims merge).")],
    failure_modes=[("01", "Noise consolidated into canon.", "threshold audit",
                    "Demote item to PROVISIONAL; raise threshold temporarily."),
                   ("02", "Duplicate canonical entries fragment retrieval.", "dedup hash audit",
                    "Merge entries; preserve both provenance chains.")],
    control_planes=["C06_MEMORY"],
)
