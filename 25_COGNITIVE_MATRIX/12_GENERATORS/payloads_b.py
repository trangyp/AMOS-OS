"""Payloads B: primitives L08–L16. DERIVED/MODEL contract content."""
from payloads_a import _base

PAYLOADS = {}

PAYLOADS["L08"] = _base(
    "L08", "REPRESENTATION",
    "Chooses and maintains the internal encodings in which knowledge, state, and predictions are expressed.",
    "Covers representation selection, encoding compatibility, and cross-representation translation.",
    inputs=["Entities, relations, percepts"],
    outputs=["Typed representations", "Translation receipts"],
    deps_up=["L04_OBJECT_ENTITY_FORMATION"], deps_down=["L09_INFERENCE", "L10_WORLD_MODELING"],
    semantics=["A representation is a lens: it makes some structure explicit and hides other structure."],
    invariants=[(1, "Cross-representation translation must not silently change claim class."),
                (2, "Representation choice is recorded with the artifacts it produces.")],
    failure_modes=[("01", "Lossy translation presented as lossless.", "round-trip fidelity test",
                    "Downgrade translated claims; mark information delta."),
                   ("02", "Wrong lens for regime (e.g. continuous repr for discrete domain).", "regime-lens check",
                    "Switch representation; recompute affected derivations.")],
    control_planes=["C05_REPRESENTATION"],
)

PAYLOADS["L09"] = _base(
    "L09", "INFERENCE",
    "Derives new claims from stored/working knowledge under declared inference rules with provenance propagation.",
    "Covers rule-gated deduction, abductive candidacy, and derivation-lineage tracking.",
    inputs=["Knowledge base slice", "Inference rules"],
    outputs=["Derived claims with lineage", "Confidence updates"],
    deps_up=["L05_BINDING", "L07_MEMORY", "L08_REPRESENTATION"], deps_down=["L10_WORLD_MODELING", "L13_PREDICTION"],
    semantics=["Every derived claim inherits the minimum confidence of its premises and records its rule chain."],
    invariants=[(1, "Derived claim confidence ≤ min(premise confidences) unless an explicit strengthening rule applies."),
                (2, "Conditional-on-carry: conclusions from unproven conjectures carry CONDITIONAL-ON tags transitively.")],
    failure_modes=[("01", "Rule applied outside its validity regime.", "regime-condition check",
                    "Retract conclusion; log regime violation."),
                   ("02", "Conjecture slippage: conditional result used unconditionally.", "CONDITIONAL-ON audit",
                    "Hard block; escalate as Signal Fidelity violation.")],
    control_planes=["C04_REASONING"],
)

PAYLOADS["L10"] = _base(
    "L10", "WORLD_MODELING",
    "Maintains a structured predictive model of the environment at multiple scales.",
    "Covers model composition across scales and model-environment mismatch tracking.",
    inputs=["Derived claims", "Observation stream"],
    outputs=["World-model state", "Mismatch signals"],
    deps_up=["L09_INFERENCE", "L01_SENSING_OBSERVATION"], deps_down=["L11_CAUSAL_MODELING", "L13_PREDICTION"],
    semantics=["Model ≠ territory: every world-model artifact carries MODEL class regardless of fit quality."],
    invariants=[(1, "World-model outputs are always MODEL class; SOURCE class is reserved for observations."),
                (2, "Persistent mismatch above threshold triggers model revision, not data dismissal.")],
    failure_modes=[("01", "Overfit model explains past but fails forward.", "held-out validation",
                    "Penalize complexity; revert to simpler structure."),
                   ("02", "Model treated as reality (reification).", "claim-class gate",
                    "Strip reified claims; restore MODEL tagging.")],
    control_planes=["C04_REASONING", "C05_REPRESENTATION"],
)

PAYLOADS["L11"] = _base(
    "L11", "CAUSAL_MODELING",
    "Represents mechanisms and interventions, distinguishing causation from correlation.",
    "Covers causal graph maintenance, intervention semantics, and confounder handling.",
    inputs=["World-model state", "Intervention records"],
    outputs=["Causal graphs", "Mechanism hypotheses"],
    deps_up=["L10_WORLD_MODELING"], deps_down=["L12_COUNTERFACTUAL_SIMULATION", "L13_PREDICTION"],
    semantics=["Correlation licenses prediction only; causal claims require mechanism or intervention evidence."],
    invariants=[(1, "Causal edges require named evidence class (mechanism/intervention/RCT); observational-only edges stay correlational."),
                (2, "Confounded relations are tagged, never silently promoted to causal.")],
    failure_modes=[("01", "Correlation promoted to causation.", "evidence-class gate",
                    "Demote edge; require mechanism study before promotion."),
                   ("02", "Collider conditioning induces spurious links.", "graph-structure check",
                    "Retract induced edges; flag analysis path.")],
    control_planes=["C04_REASONING"],
)

PAYLOADS["L12"] = _base(
    "L12", "COUNTERFACTUAL_SIMULATION",
    "Runs what-if scenarios over causal/world models to evaluate alternatives without real-world cost.",
    "Covers scenario construction, simulation honesty rules, and pessimism correction.",
    inputs=["Causal/world models", "Scenario parameters"],
    outputs=["Simulated outcomes", "Simulation-honesty annotations"],
    deps_up=["L11_CAUSAL_MODELING"], deps_down=["L14_VALUATION", "L16_PLANNING"],
    semantics=["Simulations are optimistic by nature; verdicts use worst-branch reasoning where stakes are high."],
    invariants=[(1, "Stable verdicts require ALL branches stable (simulation pessimism rule)."),
                (2, "Simulated outcomes are never reported as observed outcomes.")],
    failure_modes=[("01", "Best-case branch cherry-picked.", "branch-coverage audit",
                    "Re-run with full branch enumeration; annotate selection bias."),
                   ("02", "Unmodeled coupling invalidates independence assumptions.", "coupling review",
                    "Add coupling terms or bound the claim.")],
    control_planes=["C04_REASONING", "C03_EXECUTIVE"],
)

PAYLOADS["L13"] = _base(
    "L13", "PREDICTION",
    "Emits calibrated forecasts with uncertainty quantification and resolution tracking.",
    "Covers forecast emission, calibration scoring, and horizon discipline.",
    inputs=["World/causal models", "Current evidence"],
    outputs=["Calibrated predictions", "Uncertainty bounds"],
    deps_up=["L09_INFERENCE", "L10_WORLD_MODELING"], deps_down=["L19_OUTCOME_OBSERVATION", "L20_CREDIT_ASSIGNMENT"],
    semantics=["A prediction without uncertainty bounds is a claim, not a forecast."],
    invariants=[(1, "All predictions carry interval/band estimates."),
                (2, "Backtested accuracy only from held-out evaluation; in-sample accuracy labeled as such.")],
    failure_modes=[("01", "Overconfident narrow bands.", "calibration curve audit",
                    "Widen via recalibration; log miscalibration event."),
                   ("02", "Horizon confusion (short-term skill sold as long-term).", "horizon stratification",
                    "Split scores by horizon; retract conflated claims.")],
    control_planes=["C04_REASONING"],
)

PAYLOADS["L14"] = _base(
    "L14", "VALUATION",
    "Assigns value/cost/risk to states and outcomes under declared preference structures.",
    "Covers utility assignment, risk weighting, and value-conflict surfacing.",
    inputs=["Predictions", "Preference structure"],
    outputs=["Valued outcome estimates", "Conflict flags"],
    deps_up=["L12_COUNTERFACTUAL_SIMULATION", "L13_PREDICTION"], deps_down=["L15_GOAL_FORMATION", "L17_DECISION"],
    semantics=["Value conflicts are surfaced explicitly, never averaged into a single scalar."],
    invariants=[(1, "Multi-objective conflicts surface as fronts with declared weights, not hidden sums."),
                (2, "Ethical constraints act as vetoes, not penalty terms.")],
    failure_modes=[("01", "Scalarization hides a dominant trade-off.", "front inspection",
                    "Restore multi-objective view; surface conflict."),
                   ("02", "Risk weights drift without authorization.", "weight-change audit",
                    "Revert weights; require governance sign-off.")],
    control_planes=["C01_GOVERNANCE", "C03_EXECUTIVE"],
)

PAYLOADS["L15"] = _base(
    "L15", "GOAL_FORMATION",
    "Converts values and context into explicit, typed goals with success criteria.",
    "Covers goal decomposition, priority ordering, and goal-conflict detection.",
    inputs=["Valued outcome estimates", "Context"],
    outputs=["Typed goal set with success criteria"],
    deps_up=["L14_VALUATION"], deps_down=["L06_WORKING_STATE", "L16_PLANNING"],
    semantics=["A goal without a falsifiable success criterion is a wish, not a goal."],
    invariants=[(1, "Every goal carries measurable success/failure criteria."),
                (2, "Goal cycles are defects: no goal may depend on itself transitively.")],
    failure_modes=[("01", "Vague criteria allow retroactive success claims.", "criterion check",
                    "Reject goal until criteria are measurable."),
                   ("02", "Subgoal drift away from parent intent.", "alignment check",
                    "Prune drifting subgoals; log drift distance.")],
    control_planes=["C03_EXECUTIVE"],
)

PAYLOADS["L16"] = _base(
    "L16", "PLANNING",
    "Constructs action sequences that satisfy goals under resource and feasibility constraints.",
    "Covers plan synthesis, feasibility gating, and contingency embedding.",
    inputs=["Goal set", "Action repertoire", "Constraints"],
    outputs=["Feasible plans with contingencies"],
    deps_up=["L15_GOAL_FORMATION", "L12_COUNTERFACTUAL_SIMULATION"], deps_down=["L17_DECISION", "O12_PLAN"],
    semantics=["Plans carry their assumptions; executing a plan outside its assumption envelope requires replanning."],
    invariants=[(1, "No plan step may violate a hard constraint (feasibility fail-closed)."),
                (2, "Every plan embeds at least one abort/contingency path.")],
    failure_modes=[("01", "Slightly-infeasible plan accepted.", "feasibility precision check",
                    "Reject; regenerate within full-precision constraints."),
                   ("02", "Stale plan executed after environment change.", "epoch binding",
                    "Halt execution; trigger replanning.")],
    control_planes=["C03_EXECUTIVE", "C08_EXECUTION"],
)
