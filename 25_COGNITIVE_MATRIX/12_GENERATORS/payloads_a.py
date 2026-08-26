"""Payloads A: primitives L00–L07. DERIVED/MODEL contract content."""
PAYLOADS = {}

def _base(pid, definition, purpose=None, scope=None, inputs=None, outputs=None, deps_up=None, deps_down=None, **kw):
    purpose = purpose or definition
    scope = scope or "Covers the operation contract for this lifecycle operator."
    inputs = inputs or ["Typed upstream structures"]
    outputs = outputs or ["Validated downstream artifacts"]
    deps_up = deps_up or []
    deps_down = deps_down or []
    return dict(
        pid=pid, definition=definition, purpose=purpose, scope=scope,
        inputs=inputs, outputs=outputs,
        deps_up=deps_up, deps_down=deps_down,
        semantics=kw.get("semantics", []),
        preconditions=kw.get("preconditions", ["Upstream package state is coherent and fresh."]),
        postconditions=kw.get("postconditions", ["Output claims carry provenance and confidence ceiling."]),
        state_vars=kw.get("state_vars", ["active_state", "last_update_epoch"]),
        transitions=kw.get("transitions", ["IDLE→ACTIVE on upstream signal", "ACTIVE→SETTLED after validation guard"]),
        invariants=kw.get("invariants", [(1, "No output without provenance."), (2, "UNKNOWN/GAP never reported as PASS.")]),
        failure_modes=kw.get("failure_modes", [
            ("01", "Stale upstream input consumed as fresh.", "freshness epoch check",
             "Quarantine input; re-fetch from source; log staleness delta."),
            ("02", "Silent drift of output schema.", "schema fingerprint comparison",
             "Restore from last-good snapshot; escalate to repair plane."),
        ]),
        recovery=kw.get("recovery", "Roll back to last validated state snapshot; re-run from upstream anchor."),
        control_planes=kw.get("control_planes", ["C04_REASONING"]),
        cp_roles=kw.get("cp_roles", {"C04_REASONING": "primary reasoning-plane owner for this primitive"}),
        agents=kw.get("agents", [f"{pid} contract steward agent — validates package coherence"]),
        skills=kw.get("skills", ["amos-cognitive-substrate-* governing skills per AMOS skill index"]),
        workflows=kw.get("workflows", [f"Contract validation workflow for {pid}"]),
        protocols=kw.get("protocols", [f"{pid} typed IO protocol (this contract)"]),
        tests=kw.get("tests", [
            f"{pid} output carries provenance fields under all input regimes",
            f"{pid} rejects stale/freshness-violating input",
            f"{pid} invariant set holds over fuzzed input corpus",
        ]),
        hml=kw.get("hml", {
            "H": f"{pid} governs system-level behavior at architecture scale.",
            "M": f"{pid} operates on subsystem objects at process scale.",
            "L": f"{pid} binds to concrete evidence items at detail scale.",
        }),
        variables=kw.get("variables", [f"{pid.lower()}_state", f"{pid.lower()}_confidence_ceiling"]),
        operators=kw.get("operators", [f"{pid}_APPLY", f"{pid}_VALIDATE"]),
        equations=kw.get("equations", "No measured equations at this layer; structural relations only."),
        memory=kw.get("memory", f"{pid} reads/writes through the memory plane with trust-state tagging."),
        state_ownership=kw.get("state_ownership", f"{pid} owns no global state; participates via the shared cognitive state vector."),
        authority=kw.get("authority", f"{pid} holds no autonomous authority; effects require C01_GOVERNANCE authorization."),
        observability=kw.get("observability", f"{pid}: invocation count, rejection count, staleness deltas, confidence ceilings."),
        translation_rules=kw.get("translation_rules", "H-level statements translate to M-level mechanisms and L-level evidence checks without changing claim class."),
    )

# ---------------- L00 ----------------
PAYLOADS["L00"] = _base(
    "L00", "REALITY_ENVIRONMENT",
    "Defines the boundary between the cognitive system and reality: everything the system can distinguish must arrive through an observation channel carrying evidence and provenance.",
    "Covers observation channels, environment contact surfaces, grounding receipts, and the reality-gate that separates SOURCE_CLAIM from OBSERVATION.",
    inputs=["Raw observations (typed, timestamped)", "Environment events"],
    outputs=["Grounded observation records", "Reality-contact receipts"],
    deps_up=[], deps_down=["L01_SENSING_OBSERVATION", "L19_OUTCOME_OBSERVATION"],
    semantics=[
        "An ungrounded statement has claim class MODEL at best, never SOURCE.",
        "The reality gate fails closed: unverifiable contact yields UNKNOWN/GAP, not assumption.",
    ],
    invariants=[(1, "Every claimed fact about the world enters via a receipted observation channel."),
                (2, "Reality gate failure = UNKNOWN/GAP, never silent assumption.")],
    failure_modes=[("01", "Hallucinated contact: model output treated as observation.", "provenance-channel audit",
                    "Revoke claim; mark channel compromised; quarantine dependent states."),
                   ("02", "Environment change undetected between epochs.", "epoch diffing",
                    "Force full re-observation before further inference.")],
    control_planes=["C07_PERCEPTION", "C09_KERNEL_CONTROL"],
    tests=["Injected fake observation without receipt is rejected by the gate",
           "Gate fail-closed behavior verified under channel loss",
           "Epoch-change detection fires within one cycle"],
)

# ---------------- L01 ----------------
PAYLOADS["L01"] = _base(
    "L01", "SENSING_OBSERVATION",
    "Converts raw environmental contact into typed, normalized observation records suitable for downstream perception.",
    "Covers sensor normalization, typing, deduplication, and freshness stamping of observations.",
    inputs=["Grounded observation records (from L00)"],
    outputs=["Typed normalized observations", "Freshness stamps"],
    deps_up=["L00_REALITY_ENVIRONMENT"], deps_down=["L02_ATTENTION", "L03_PERCEPT_FORMATION"],
    semantics=["Observations are immutable once stamped; correction creates a superseding record, never an edit."],
    invariants=[(1, "Observation immutability: corrections supersede, they do not overwrite."),
                (2, "Every observation carries a freshness epoch.")],
    failure_modes=[("01", "Duplicate observations inflate evidence weight.", "deduplication hash audit",
                    "Collapse duplicates; recompute evidence weights."),
                   ("02", "Clock skew corrupts ordering.", "monotonic sequence check",
                    "Re-order by logical clock; flag skewed sources.")],
    control_planes=["C07_PERCEPTION"],
)

# ---------------- L02 ----------------
PAYLOADS["L02"] = _base(
    "L02", "ATTENTION",
    "Allocates finite processing capacity over available observations according to salience and goal relevance.",
    "Covers salience scoring, capacity budgets, and attention switching policy.",
    inputs=["Normalized observations", "Goal context", "Capacity budget"],
    outputs=["Attention-weighted observation subset", "Salience scores"],
    deps_up=["L01_SENSING_OBSERVATION", "L15_GOAL_FORMATION"],
    deps_down=["L03_PERCEPT_FORMATION", "L06_WORKING_STATE"],
    semantics=["Attention is zero-sum: capacity given to one stream is removed from another."],
    invariants=[(1, "Total allocated attention ≤ capacity budget."),
                (2, "Safety-critical signals are never starved (priority floor).")],
    failure_modes=[("01", "Attention capture by high-salience but irrelevant stimulus.", "goal-relevance cross-check",
                    "Rebalance toward goal-relevant streams; log capture event."),
                   ("02", "Priority floor violated during load spike.", "floor assertion",
                    "Preempt non-critical streams immediately.")],
    control_planes=["C03_EXECUTIVE", "C07_PERCEPTION"],
    variables=["attention_budget", "salience_weights", "priority_floor"],
    equations="Σ w_i ≤ B_budget; w_i ≥ p_floor for safety-critical i.",
)

# ---------------- L03 ----------------
PAYLOADS["L03"] = _base(
    "L03", "PERCEPT_FORMATION",
    "Binds attended raw features into candidate percepts — structured hypotheses about what is present.",
    "Covers feature binding, percept candidacy, and ambiguity retention.",
    inputs=["Attention-weighted observations"],
    outputs=["Candidate percepts with ambiguity scores"],
    deps_up=["L02_ATTENTION"], deps_down=["L04_OBJECT_ENTITY_FORMATION", "L05_BINDING"],
    semantics=["Ambiguity is preserved downstream rather than resolved prematurely."],
    invariants=[(1, "Premature disambiguation below threshold is prohibited."),
                (2, "Each percept retains its constituent-feature lineage.")],
    failure_modes=[("01", "False binding merges unrelated features.", "lineage consistency check",
                    "Split percept; penalize binding rule; log merge error."),
                   ("02", "Ambiguity lost in transit.", "ambiguity-score propagation check",
                    "Restore ambiguity metadata from upstream record.")],
    control_planes=["C07_PERCEPTION", "C05_REPRESENTATION"],
)

# ---------------- L04 ----------------
PAYLOADS["L04"] = _base(
    "L04", "OBJECT_ENTITY_FORMATION",
    "Consolidates stable percepts into persistent entities with identity across time.",
    "Covers entity identity, persistence criteria, and identity-continuity tracking.",
    inputs=["Candidate percepts", "Existing entity registry"],
    outputs=["Persistent entities", "Identity continuity links"],
    deps_up=["L03_PERCEPT_FORMATION"], deps_down=["L05_BINDING", "L08_REPRESENTATION", "L25_IDENTITY_CONTINUITY"],
    semantics=["Entity identity persists only while continuity evidence remains above threshold."],
    invariants=[(1, "One entity cannot hold contradictory identity anchors simultaneously."),
                (2, "Identity merges require explicit reconciliation, never silent fusion.")],
    failure_modes=[("01", "Identity fragmentation: one entity splits into duplicates.", "registry dedup audit",
                    "Merge with reconciliation record; preserve both histories."),
                   ("02", "Identity theft: two entities collapse incorrectly.", "anchor-conflict detection",
                    "Split entities; quarantine affected relations.")],
    control_planes=["C05_REPRESENTATION", "C06_MEMORY"],
)

# ---------------- L05 ----------------
PAYLOADS["L05"] = _base(
    "L05", "BINDING",
    "Establishes typed relations among entities: the relation layer of the cognitive substrate.",
    "Covers relation formation, typing, directionality, and consistency enforcement.",
    inputs=["Entities", "Co-occurrence and causal cues"],
    outputs=["Typed directed relations"],
    deps_up=["L04_OBJECT_ENTITY_FORMATION"], deps_down=["L06_WORKING_STATE", "L09_INFERENCE", "L11_CAUSAL_MODELING"],
    semantics=["Relations are typed and directed; same-name axes do not prove same meaning (tensor-composition law)."],
    invariants=[(1, "Relation composition requires domain/semantic compatibility checks."),
                (2, "Contradictory relations coexist only with conflict tags.")],
    failure_modes=[("01", "Type confusion across composition.", "axis-semantics check",
                    "Block composition; route through tensor governance."),
                   ("02", "Undirected shortcut loses causal direction.", "directionality audit",
                    "Restore directionality from derivation record.")],
    control_planes=["C05_REPRESENTATION", "C04_REASONING"],
)

# ---------------- L06 ----------------
PAYLOADS["L06"] = _base(
    "L06", "WORKING_STATE",
    "Maintains the active task context: the small, fast state currently being reasoned over.",
    "Covers working-set membership, decay, and context switches.",
    inputs=["Percepts, entities, relations", "Task goals"],
    outputs=["Active working context"],
    deps_up=["L02_ATTENTION", "L05_BINDING"], deps_down=["L07_MEMORY", "L09_INFERENCE", "L16_PLANNING"],
    semantics=["Working state decays unless refreshed; decay rate is a governed parameter, not noise."],
    invariants=[(1, "Working-set size ≤ declared capacity bound."),
                (2, "Context switch preserves a resumable checkpoint.")],
    failure_modes=[("01", "Working-set overflow drops critical context.", "capacity monitor",
                    "Evict lowest-salience item; checkpoint evictees to L07."),
                   ("02", "Checkpoint loss on interruption.", "checkpoint persistence test",
                    "Restore from last durable checkpoint; mark gap in continuity.")],
    control_planes=["C03_EXECUTIVE", "C06_MEMORY"],
    variables=["working_set", "decay_rate", "checkpoint_epoch"],
)

# ---------------- L07 ----------------
PAYLOADS["L07"] = _base(
    "L07", "MEMORY",
    "Durable storage of consolidated knowledge with trust-state lifecycle (TRUSTED → PROVISIONAL → QUARANTINED → …).",
    "Covers write gating, consolidation thresholds, retrieval diversity, and falsification handling.",
    inputs=["Consolidation candidates", "Retrieval queries"],
    outputs=["Stored knowledge objects", "Retrieved evidence sets"],
    deps_up=["L06_WORKING_STATE", "L22_CONSOLIDATION"], deps_down=["L09_INFERENCE", "L20_CREDIT_ASSIGNMENT"],
    semantics=["Memory writes pass through trust gates; retrieval enforces contradiction quotas so stored conflicts surface."],
    invariants=[(1, "No write bypasses trust-state assignment."),
                (2, "Retrieval must include at least one contradicting view when one exists (contradiction quota)."),
                (3, "Falsified items are marked REVOKED/FALSIFIED, never deleted silently.")],
    failure_modes=[("01", "Quarantined content leaks into trusted retrieval.", "trust-state filter audit",
                    "Purge leak path; re-run retrieval integrity suite."),
                   ("02", "Memory monoculture: single-source dominance.", "diversity metric",
                    "Inject competing-hypothesis retrieval; log dominance warning."),
                   ("03", "Silent corruption of stored object.", "checksum verification",
                    "Restore from snapshot; investigate writer chain.")],
    control_planes=["C06_MEMORY", "C01_GOVERNANCE"],
    variables=["trust_state_map", "consolidation_threshold", "retrieval_diversity_min"],
)
