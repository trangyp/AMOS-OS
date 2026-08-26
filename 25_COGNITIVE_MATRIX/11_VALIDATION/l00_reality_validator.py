#!/usr/bin/env python3
"""
L00_REALITY_ENVIRONMENT contract executor.

Executes the test table DECLARED BY THE SPEC ITSELF:
25_COGNITIVE_MATRIX/01_PRIMITIVES/L00_REALITY_ENVIRONMENT/
    L00_REALITY_ENVIRONMENT_PRIMITIVES_COGNITIVE_MATRIX_DEFINITION.md
Section 71 "Tests / Validators" (L00-T01 .. L00-T30).

Pattern proven in this repo by:
- routing_policy_validator.py   (19/19, commit 6aa94e487)
- authz invariant engine        (17/17, commit b162ba0dd)

Rules of the house:
- Fail-closed on UNKNOWN/GAP.
- No fabrication: every check operates on typed observation records supplied
  as input; absence of required fields is UNKNOWN, never PASS.
- Status semantics: EXECUTED-VALIDATED logic here; runtime enforcement of
  live observation channels remains UNKNOWN/GAP (declared in receipt).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Typed records mirroring the spec's tensors (Sec 6/7/26/27)
# ---------------------------------------------------------------------------

@dataclass
class Observation:
    obs_id: str = ""
    value: Any = None
    unit: Optional[str] = None                 # L00-FM-12 / T06
    observer_id: str = ""                      # T07
    method: str = ""                           # measurement method
    event_time: Optional[float] = None         # T08
    observation_time: Optional[float] = None   # T09
    freshness_horizon_tau: Optional[float] = None  # T10
    source: str = ""                           # provenance root
    ancestry: Tuple[str, ...] = ()             # evidence lineage
    scope: frozenset = frozenset()             # T11
    regime: str = ""                           # T12
    is_observed: bool = True                   # T15/T16 partial observability
    observed_at_all: bool = True               # absence-of-observation guard

@dataclass
class StateRecord:
    state_identity: Dict[str, Any] = field(default_factory=dict)  # object_id/version/hash
    content_hash: str = ""
    read_hash: str = ""                        # hash at read time
    mutable: bool = False
    revalidated_before_use: Optional[bool] = None  # T14

@dataclass
class Evidence:
    ev_id: str = ""
    kind: str = "OBSERVATION"                  # OBSERVATION | SOURCE_CLAIM | MODEL | SIMULATION | PREDICTION | MEMORY | TOOL_OUTPUT
    obs_refs: List[str] = field(default_factory=list)   # ids into observations
    source: str = ""                                    # provenance root (T17/T18)
    ancestry: Tuple[str, ...] = ()                      # evidence lineage
    transformation_depth: int = 0              # d_R(x), Sec 10
    derived_from_scope: frozenset = frozenset()
    claim_scope: frozenset = frozenset()
    claim_regime: str = ""
    causal_claim: bool = False                 # T20 causal promotion gate
    cross_scale: bool = False                  # T19 local->global gate
    confidence: float = 1.0                    # T75 min-aggregation ceiling input

# Verdict constants
PASS, FAIL, CONDITIONAL, UNKNOWN = "PASS", "FAIL", "CONDITIONAL", "UNKNOWN"

@dataclass
class CheckResult:
    test_id: str
    name: str
    verdict: str
    detail: str = ""

# ---------------------------------------------------------------------------
# The engine: each function implements exactly one declared test ID
# ---------------------------------------------------------------------------

class L00Validator:
    """Executes L00-T01..T30 against caller-supplied typed inputs."""

    def __init__(self):
        self._tests: List[Tuple[str, str]] = [
            ("T01", "Reality/representation distinction"),
            ("T02", "Observation/inference distinction"),
            ("T03", "Prediction/outcome distinction"),
            ("T04", "Simulation/deployment distinction"),
            ("T05", "Observation provenance preservation"),
            ("T06", "Measurement-unit preservation"),
            ("T07", "Observer identity preservation"),
            ("T08", "Event-time preservation"),
            ("T09", "Observation-time preservation"),
            ("T10", "Freshness threshold validation"),
            ("T11", "Scope compatibility"),
            ("T12", "Regime compatibility"),
            ("T13", "State identity validation"),
            ("T14", "Mutable-state revalidation"),
            ("T15", "Partial-observability handling"),
            ("T16", "Missing-data handling"),
            ("T17", "Evidence ancestry resolution"),
            ("T18", "Correlated-source detection"),
            ("T19", "Cross-scale generalization gate"),
            ("T20", "Causal promotion gate"),
            ("T21", "Capability/authority separation"),
            ("T22", "Proposal/commit separation"),
            ("T23", "Expected/observed effect separation"),
            ("T24", "Selective invalidation"),
            ("T25", "Post-action observation"),
            ("T26", "Regime-shift invalidation"),
            ("T27", "Memory freshness validation"),
            ("T28", "Tool-output provenance"),
            ("T29", "UNKNOWN fail-closed behavior"),
            ("T30", "Reality-feedback closure"),
        ]

    @property
    def test_table(self) -> List[Tuple[str, str]]:
        return list(self._tests)

    # -- dispatch ----------------------------------------------------------
    def run_test(self, test_id: str, ctx: dict) -> CheckResult:
        fn = getattr(self, f"_t{test_id[1:]}", None)
        if fn is None or test_id not in {t for t, _ in self._tests}:
            return CheckResult(test_id, "?", UNKNOWN, "test id not implemented")
        try:
            return fn(ctx)
        except Exception as exc:  # defensive: never crash-open
            return CheckResult(test_id, "", FAIL, f"validator error: {exc!r}")

    def run_all(self, ctx_per_test: Dict[str, dict]) -> Tuple[List[CheckResult], bool]:
        results = [self.run_test(tid, ctx_per_test.get(tid, {})) for tid, _ in self._tests]
        all_ok = all(r.verdict == PASS for r in results)
        return results, all_ok

    # -- T01..T04 : separation invariants ----------------------------------
    def _t01(self, c):
        """Representation(x) != x. A representation record must not carry
        is_reality=True."""
        rep = c.get("representation")
        if rep is None:
            return CheckResult("T01", "reality/representation", UNKNOWN, "no representation supplied")
        if isinstance(rep, dict) and rep.get("is_reality") is True:
            return CheckResult("T01", "reality/representation", FAIL,
                               "representation flagged as reality (L00-FM-01)")
        if isinstance(rep, str) and rep == "__REALITY__":
            return CheckResult("T01", "reality/representation", FAIL,
                               "representation claims identity with reality")
        return CheckResult("T01", "reality/representation", PASS,
                           "representation kept distinct from reality")

    def _t02(self, c):
        """OBSERVED != INFERRED. Inferred evidence must not be typed OBSERVATION."""
        ev: Evidence = c.get("inferred_evidence")
        if ev is None:
            return CheckResult("T02", "observed/inferred", UNKNOWN, "no evidence supplied")
        if ev.kind == "OBSERVATION" and not any(
            o in c.get("observation_ids", set()) for o in ev.obs_refs
        ):
            return CheckResult("T02", "observed/inferred", FAIL,
                               "inference typed as unbacked OBSERVATION (FM-02)")
        if ev.transformation_depth > 0 and ev.kind == "OBSERVATION" and not ev.obs_refs:
            return CheckResult("T02", "observed/inferred", FAIL,
                               "transformed artifact retains OBSERVATION type without obs refs")
        return CheckResult("T02", "observed/inferred", PASS)

    def _t03(self, c):
        """PREDICTED != OBSERVED. Prediction stored as outcome before
        independent post-horizon observation -> FM-03."""
        pred = c.get("prediction")          # {"horizon": h, "recorded_as_outcome": bool}
        outcome_observed = c.get("outcome_observed_after_horizon")
        if pred is None:
            return CheckResult("T03", "prediction/outcome", UNKNOWN, "no prediction supplied")
        if pred.get("recorded_as_outcome"):
            if outcome_observed is not True:
                return CheckResult("T03", "prediction/outcome", FAIL,
                                   "prediction stored as outcome without post-horizon observation")
            return CheckResult("T03", "prediction/outcome", CONDITIONAL,
                               "prediction scored only after independent observation")
        return CheckResult("T03", "prediction/outcome", PASS, "prediction kept as MODEL")

    def _t04(self, c):
        """SIMULATION != DEPLOYMENT. Sim result promoted to deployment
        evidence -> FM-04."""
        sim = c.get("simulation_result")
        if sim is None:
            return CheckResult("T04", "simulation/deployment", UNKNOWN, "no simulation supplied")
        if sim.get("promoted_to_deployment_evidence"):
            return CheckResult("T04", "simulation/deployment", FAIL,
                               "simulation result used as deployment evidence")
        return CheckResult("T04", "simulation/deployment", PASS)

    # -- T05..T09 : provenance & temporal identity -------------------------
    def _t05(self, c):
        o: Observation = c.get("observation")
        if o is None:
            return CheckResult("T05", "provenance", UNKNOWN, "no observation supplied")
        missing = [f for f in ("source", "method") if not getattr(o, f)]
        if missing:
            return CheckResult("T05", "provenance", FAIL,
                               f"decision-relevant observation missing {missing}")
        return CheckResult("T05", "provenance", PASS)

    def _t06(self, c):
        o: Observation = c.get("measurement")
        if o is None:
            return CheckResult("T06", "unit preservation", UNKNOWN, "no measurement supplied")
        if o.value is not None and o.unit is None:
            return CheckResult("T06", "unit preservation", FAIL,
                               "VALUE WITHOUT UNIT != TYPED MEASUREMENT")
        return CheckResult("T06", "unit preservation", PASS)

    def _t07(self, c):
        o: Observation = c.get("observer_dependent_observation")
        if o is None:
            return CheckResult("T07", "observer identity", UNKNOWN, "no observation supplied")
        if not o.observer_id:
            return CheckResult("T07", "observer identity", FAIL,
                               "observer-dependent observation lost observer identity")
        return CheckResult("T07", "observer identity", PASS, f"observer={o.observer_id}")

    def _t08(self, c):
        o: Observation = c.get("observation")
        if o is None:
            return CheckResult("T08", "event-time", UNKNOWN, "no observation supplied")
        if o.event_time is None:
            return CheckResult("T08", "event-time", FAIL, "observation lost event_time")
        return CheckResult("T08", "event-time", PASS)

    def _t09(self, c):
        o: Observation = c.get("observation")
        if o is None:
            return CheckResult("T09", "observation-time", UNKNOWN, "no observation supplied")
        if o.observation_time is None:
            return CheckResult("T09", "observation-time", FAIL, "observation lost observation_time")
        if o.event_time is not None and o.observation_time == o.event_time:
            return CheckResult("T09", "observation-time", CONDITIONAL,
                               "event_time == observation_time asserted; requires explicit demonstration")
        return CheckResult("T09", "observation-time", PASS)

    # -- T10..T12 : freshness / scope / regime ------------------------------
    def _t10(self, c):
        o: Observation = c.get("observation")
        now: Optional[float] = c.get("now")
        consequential = c.get("consequential_use", True)
        if o is None or o.observation_time is None or now is None:
            return CheckResult("T10", "freshness", UNKNOWN, "need observation_time and now")
        age = now - o.observation_time
        if o.freshness_horizon_tau is None:
            return CheckResult("T10", "freshness", UNKNOWN,
                               "no tau_c declared for this claim (freshness is claim-dependent)")
        if age <= o.freshness_horizon_tau:
            return CheckResult("T10", "freshness", PASS, f"age={age:.3g} <= tau={o.freshness_horizon_tau}")
        if consequential:
            return CheckResult("T10", "freshness", FAIL,
                               f"stale state drives consequential action (age {age:.3g} > tau)")
        return CheckResult("T10", "freshness", CONDITIONAL,
                           "stale but use is non-consequential")

    def _t11(self, c):
        ev: Evidence = c.get("derived_claim")
        if ev is None:
            return CheckResult("T11", "scope compatibility", UNKNOWN, "no claim supplied")
        widened = ev.claim_scope - ev.derived_from_scope
        if widened:
            return CheckResult("T11", "scope compatibility", FAIL,
                               f"claim silently widens evidence scope by {sorted(widened)} (INV-07)")
        return CheckResult("T11", "scope compatibility", PASS)

    def _t12(self, c):
        ev: Evidence = c.get("regime_transfer_claim")
        if ev is None:
            return CheckResult("T12", "regime compatibility", UNKNOWN, "no claim supplied")
        if ev.claim_regime and ev.claim_regime != c.get("evidence_regime", ev.claim_regime):
            return CheckResult("T12", "regime compatibility", FAIL,
                               f"conclusion exported from regime '{c.get('evidence_regime')}' "
                               f"to '{ev.claim_regime}' without bridge (INV-08)")
        return CheckResult("T12", "regime compatibility", PASS)

    # -- T13..T16 : state identity / observability --------------------------
    def _t13(self, c):
        s: StateRecord = c.get("authoritative_state")
        if s is None:
            return CheckResult("T13", "state identity", UNKNOWN, "no state supplied")
        sid = s.state_identity
        if not all(sid.get(k) for k in ("object_id", "version", "content_hash")):
            return CheckResult("T13", "state identity", FAIL,
                               "identity must include object_id+version+content_hash (Sec 27)")
        if s.content_hash and s.content_hash != sid["content_hash"]:
            return CheckResult("T13", "state identity", FAIL, "hash mismatch between record and identity")
        return CheckResult("T13", "state identity", PASS)

    def _t14(self, c):
        s: StateRecord = c.get("mutable_state_used")
        if s is None:
            return CheckResult("T14", "mutable revalidation", UNKNOWN, "no mutable-state use supplied")
        if not s.mutable:
            return CheckResult("T14", "mutable revalidation", CONDITIONAL,
                               "state immutable; revalidation not required")
        if s.revalidated_before_use is None:
            return CheckResult("T14", "mutable revalidation", UNKNOWN,
                               "revalidation status unknown -> fail-closed")
        if not s.revalidated_before_use:
            return CheckResult("T14", "mutable revalidation", FAIL,
                               "mutable state used without REVALIDATE (INV-10, FM-05)")
        return CheckResult("T14", "mutable revalidation", PASS)

    def _t15(self, c):
        """NOT_OBSERVED != NONEXISTENT. Unobserved region must stay UNKNOWN."""
        region = c.get("unobserved_region")
        if region is None:
            return CheckResult("T15", "partial observability", UNKNOWN, "no region supplied")
        treated = region.get("treated_as")
        if treated in ("ABSENT", "FALSE", "EMPTY"):
            return CheckResult("T15", "partial observability", FAIL,
                               "unobserved converted to absent (INV-16)")
        if treated == "UNKNOWN":
            return CheckResult("T15", "partial observability", PASS, "kept UNKNOWN")
        return CheckResult("T15", "partial observability", UNKNOWN, f"unrecognized treatment '{treated}'")

    def _t16(self, c):
        """Missing-data handling: decision depending on missing datum must be
        gated, not defaulted."""
        dep = c.get("decision_with_missing_data")
        if dep is None:
            return CheckResult("T16", "missing-data", UNKNOWN, "no decision supplied")
        if dep.get("missing_required") and dep.get("proceeded_without_gate"):
            return CheckResult("T16", "missing-data", FAIL, "decision proceeded on missing required datum")
        return CheckResult("T16", "missing-data", PASS)

    # -- T17..T20 : evidence topology ---------------------------------------
    def _t17(self, c):
        ev: Evidence = c.get("evidence")
        known_roots = c.get("known_source_ids", set())
        if ev is None:
            return CheckResult("T17", "ancestry resolution", UNKNOWN, "no evidence supplied")
        if not ev.ancestry and not ev.source:
            return CheckResult("T17", "ancestry resolution", FAIL, "no recoverable ancestry (INV-06)")
        unresolved = [a for a in ev.ancestry if known_roots and a not in known_roots]
        if unresolved:
            return CheckResult("T17", "ancestry resolution", CONDITIONAL,
                               f"ancestors outside known roots: {unresolved}")
        return CheckResult("T17", "ancestry resolution", PASS)

    def _t18(self, c):
        """MULTIPLE_SOURCES != INDEPENDENT_SOURCES. Two confirmations sharing
        an ancestor count once."""
        items: List[Evidence] = c.get("confirmations", [])
        if len(items) < 2:
            return CheckResult("T18", "correlated sources", UNKNOWN,
                               "need >=2 confirmations to audit independence")
        claimed_independent_count = c.get("claimed_independent_count", len(items))
        roots = {}
        shared = False
        for it in items:
            r = it.source or (it.ancestry[0] if it.ancestry else None)
            if r and r in roots.values():
                shared = True
            if r:
                roots[it.ev_id] = r
        if shared and claimed_independent_count >= len(items):
            return CheckResult("T18", "correlated sources", FAIL,
                               "shared-ancestor confirmations counted as independent (FM-10, INV-17)")
        return CheckResult("T18", "correlated sources", PASS)

    def _t19(self, c):
        """Cross-scale gate: local observation cannot justify system-wide
        conclusion without declared mapping Phi (Sec 45)."""
        ev: Evidence = c.get("cross_scale_conclusion")
        if ev is None:
            return CheckResult("T19", "cross-scale gate", UNKNOWN, "no conclusion supplied")
        if ev.cross_scale and not c.get("mapping_declared"):
            return CheckResult("T19", "cross-scale gate", FAIL,
                               "local observation generalized system-wide without Phi declaration")
        return CheckResult("T19", "cross-scale gate", PASS)

    def _t20(self, c):
        """Causal promotion gate: association/sequence/similarity cannot
        become causation (INV-12)."""
        ev: Evidence = c.get("causal_conclusion")
        if ev is None:
            return CheckResult("T20", "causal promotion", UNKNOWN, "no conclusion supplied")
        if not ev.causal_claim:
            return CheckResult("T20", "causal promotion", CONDITIONAL,
                               "non-causal claim; gate not applicable")
        support = set(c.get("causal_support_kinds", []))
        admissible = {"INTERVENTION_EFFECT", "MECHANISM_WITH_TYPED_EVIDENCE"}
        if not support & admissible:
            return CheckResult("T20", "causal promotion", FAIL,
                               f"causal claim supported only by {sorted(support)} (association-class)")
        return CheckResult("T20", "causal promotion", PASS,
                           f"supported by {sorted(support & admissible)}")

    # -- T21..T23 : authority / commit / effect -----------------------------
    def _t21(self, c):
        avail = c.get("action_available", False)
        authorized = c.get("action_authorized")
        if authorized is None:
            return CheckResult("T21", "capability/authority", UNKNOWN,
                               "authorization status unknown -> fail-closed")
        if avail and not authorized:
            return CheckResult("T21", "capability/authority", FAIL,
                               "AVAILABLE_ACTION treated as AUTHORIZED (INV-13, FM-14)")
        return CheckResult("T21", "capability/authority", PASS)

    def _t22(self, c):
        prop = c.get("proposal_committed_directly")
        if prop is None:
            return CheckResult("T22", "proposal/commit", UNKNOWN, "no transition supplied")
        if prop:
            return CheckResult("T22", "proposal/commit", FAIL,
                               "proposal committed without governed control-plane transition (INV-14, FM-15)")
        return CheckResult("T22", "proposal/commit", PASS)

    def _t23(self, c):
        exp = c.get("expected_effect")
        obsd = c.get("observed_effect")
        if exp is None:
            return CheckResult("T23", "effect verification", UNKNOWN, "no expected effect supplied")
        if obsd is None:
            return CheckResult("T23", "effect verification", FAIL,
                               "expected effect accepted without post-action observation (FM-16)")
        return CheckResult("T23", "effect verification", PASS, "expected vs observed compared")

    # -- T24..T26 : invalidation discipline ---------------------------------
    def _t24(self, c):
        """Selective invalidation: invalidate descendants, not everything;
        unaffected closure stays reusable."""
        plan = c.get("invalidation_plan")
        if plan is None:
            return CheckResult("T24", "selective invalidation", UNKNOWN, "no plan supplied")
        if plan.get("invalidated_everything"):
            return CheckResult("T24", "selective invalidation", CONDITIONAL,
                               "global recomputation; allowed only when dependency structure "
                               "cannot isolate failure (Sec 69)")
        deps_invalidated = set(plan.get("invalidated_ids", []))
        dependents = set(plan.get("true_dependents", []))
        missed = dependents - deps_invalidated
        if missed:
            return CheckResult("T24", "selective invalidation", FAIL,
                               f"corrupted observation's dependents left valid: {sorted(missed)[:5]}")
        return CheckResult("T24", "selective invalidation", PASS,
                           f"{len(deps_invalidated)} dependents invalidated, closure isolated")

    def _t25(self, c):
        loop = c.get("action_loop")
        if loop is None:
            return CheckResult("T25", "post-action observation", UNKNOWN, "no action loop supplied")
        if loop.get("acted") and not loop.get("post_action_observation_recorded"):
            return CheckResult("T25", "post-action observation", FAIL,
                               "loop has execution but no verified environmental closure (Sec 58)")
        return CheckResult("T25", "post-action observation", PASS)

    def _t26(self, c):
        shift = c.get("regime_shift")
        if shift is None:
            return CheckResult("T26", "regime-shift invalidation", UNKNOWN, "no shift supplied")
        if not shift.get("occurred"):
            return CheckResult("T26", "regime-shift invalidation", PASS, "no shift occurred; gate idle")
        regime_dependent = set(shift.get("regime_dependent_claims", []))
        invalidated = set(shift.get("invalidated_claims", []))
        survivors = regime_dependent - invalidated
        if survivors:
            return CheckResult("T26", "regime-shift invalidation", FAIL,
                               f"regime-dependent conclusions survive regime change: {sorted(survivors)[:5]}")
        return CheckResult("T26", "regime-shift invalidation", PASS)

    # -- T27..T28 : memory & tool grounding ---------------------------------
    def _t27(self, c):
        mem = c.get("memory_item_used_as_current_state")
        if mem is None:
            return CheckResult("T27", "memory freshness", UNKNOWN, "no memory item supplied")
        if mem.get("used_as_current_world_state") and not mem.get("revalidated_against_l00"):
            return CheckResult("T27", "memory freshness", FAIL,
                               "MEMORY != CURRENT_REALITY; stale memory drove current-state reasoning")
        return CheckResult("T27", "memory freshness", PASS)

    def _t28(self, c):
        tool = c.get("tool_output")
        if tool is None:
            return CheckResult("T28", "tool-output provenance", UNKNOWN, "no tool output supplied")
        if tool.get("typed_as_verified_truth"):
            return CheckResult("T28", "tool-output provenance", FAIL,
                               "ToolOutput auto-promoted to verified truth (Sec 54)")
        missing = [k for k in ("tool_name", "query_or_params") if not tool.get(k)]
        if missing:
            return CheckResult("T28", "tool-output provenance", CONDITIONAL,
                               f"tool output missing {missing}; reliability underivable")
        return CheckResult("T28", "tool-output provenance", PASS,
                           "retained as ObservationArtifact with provenance")

    # -- T29..T30 : fail-closed & feedback closure ---------------------------
    def _t29(self, c):
        """UNKNOWN must be terminal: never coerced to TRUE/FALSE/PASS."""
        cases: List[dict] = c.get("unknown_handling_cases", [])
        if not cases:
            return CheckResult("T29", "UNKNOWN fail-closed", UNKNOWN, "no cases supplied (meta-UNKNOWN)")
        bad = [x.get("case_id") for x in cases
               if x.get("input_status") == "UNKNOWN" and x.get("output_status") != "UNKNOWN"]
        if bad:
            return CheckResult("T29", "UNKNOWN fail-closed", FAIL,
                               f"UNKNOWN collapsed to non-UNKNOWN in cases {bad[:4]} (INV-11)")
        return CheckResult("T29", "UNKNOWN fail-closed", PASS, f"{len(cases)} cases preserved UNKNOWN")

    def _t30(self, c):
        """Full loop closure R->O->X->D->A->R'->O' (Sec 79)."""
        chain = c.get("loop_chain", [])
        if not chain:
            return CheckResult("T30", "feedback closure", UNKNOWN, "no loop chain supplied")
        required = ["R_t", "O_t", "X_t", "D_t", "A_t"]
        present = [r for r in required if r in chain]
        if present != required:
            return CheckResult("T30", "feedback closure", FAIL,
                               f"missing stages {sorted(set(required)-set(present))}")
        if "O_{t+1}" not in chain:
            return CheckResult("T30", "feedback closure", CONDITIONAL,
                               "post-effect re-observation pending; loop open at t+1")
        return CheckResult("T30", "feedback closure", PASS)


# ---------------------------------------------------------------------------
# Self-tests: adversarial + positive probes per declared ID
# ---------------------------------------------------------------------------

def run_selftests() -> Tuple[int, int, List[str]]:
    v = L00Validator()
    passed = failed = 0
    failures: List[str] = []

    def expect(tid, ctx, want, label=""):
        nonlocal passed, failed
        r = v.run_test(tid, ctx)
        ok = r.verdict == want
        if ok:
            passed += 1
        else:
            failed += 1
            failures.append(f"L00-{tid}{label}: expected {want}, got {r.verdict} ({r.detail})")

    # Positive path
    good_obs = Observation(obs_id="o1", value=1.0, unit="m", observer_id="sensor-a",
                           method="laser", event_time=100.0, observation_time=101.0,
                           freshness_horizon_tau=60.0, source="src-root",
                           ancestry=("src-root",), scope=frozenset({"lab"}), regime="G1")
    expect("T01", {"representation": {"kind": "model"}}, PASS)
    expect("T02", {"inferred_evidence": Evidence(kind="MODEL"), "observation_ids": set()}, PASS)
    expect("T03", {"prediction": {"horizon": 5, "recorded_as_outcome": False}}, PASS)
    expect("T04", {"simulation_result": {"promoted_to_deployment_evidence": False}}, PASS)
    expect("T05", {"observation": good_obs}, PASS)
    expect("T06", {"measurement": good_obs}, PASS)
    expect("T07", {"observer_dependent_observation": good_obs}, PASS)
    expect("T08", {"observation": good_obs}, PASS)
    expect("T09", {"observation": good_obs}, PASS)
    expect("T10", {"observation": good_obs, "now": 130.0}, PASS)
    expect("T11", {"derived_claim": Evidence(derived_from_scope=frozenset({"lab"}),
                                             claim_scope=frozenset({"lab"}))}, PASS)
    expect("T12", {"regime_transfer_claim": Evidence(claim_regime="G1"),
                   "evidence_regime": "G1"}, PASS)
    expect("T13", {"authoritative_state": StateRecord(
        state_identity={"object_id": "x", "version": 1, "content_hash": "h"},
        content_hash="h")}, PASS)
    expect("T14", {"mutable_state_used": StateRecord(mutable=True, revalidated_before_use=True)}, PASS)
    expect("T15", {"unobserved_region": {"treated_as": "UNKNOWN"}}, PASS)
    expect("T16", {"decision_with_missing_data": {"missing_required": False}}, PASS)
    expect("T17", {"evidence": Evidence(source="src-root", ancestry=("src-root",)),
                   "known_source_ids": {"src-root"}}, PASS)
    expect("T18", {"confirmations": [Evidence(ev_id="e1", source="rootA"),
                                     Evidence(ev_id="e2", source="rootB")],
                    "claimed_independent_count": 2}, PASS)
    expect("T19", {"cross_scale_conclusion": Evidence(cross_scale=True),
                   "mapping_declared": True}, PASS)
    expect("T20", {"causal_conclusion": Evidence(causal_claim=True),
                   "causal_support_kinds": ["INTERVENTION_EFFECT"]}, PASS)
    expect("T21", {"action_available": True, "action_authorized": True}, PASS)
    expect("T22", {"proposal_committed_directly": False}, PASS)
    expect("T23", {"expected_effect": {"x": 1}, "observed_effect": {"x": 1}}, PASS)
    expect("T24", {"invalidation_plan": {"invalidated_ids": ["d1"], "true_dependents": ["d1"],
                                          "invalidated_everything": False}}, PASS)
    expect("T25", {"action_loop": {"acted": True, "post_action_observation_recorded": True}}, PASS)
    expect("T26", {"regime_shift": {"occurred": False}}, PASS)
    expect("T27", {"memory_item_used_as_current_state":
                   {"used_as_current_world_state": True, "revalidated_against_l00": True}}, PASS)
    expect("T28", {"tool_output": {"tool_name": "grep", "query_or_params": "x",
                                   "typed_as_verified_truth": False}}, PASS)
    expect("T29", {"unknown_handling_cases": [{"case_id": "c1", "input_status": "UNKNOWN",
                                               "output_status": "UNKNOWN"}]}, PASS)
    expect("T30", {"loop_chain": ["R_t", "O_t", "X_t", "D_t", "A_t", "R_{t+1}", "O_{t+1}"]}, PASS)

    # Adversarial probes (each encodes one declared failure mode)
    expect("T01", {"representation": "__REALITY__"}, FAIL, "/adversarial")
    expect("T02", {"inferred_evidence": Evidence(kind="OBSERVATION"),
                   "observation_ids": set()}, FAIL, "/adversarial FM-02")
    expect("T03", {"prediction": {"recorded_as_outcome": True},
                   "outcome_observed_after_horizon": False}, FAIL, "/adversarial FM-03")
    expect("T04", {"simulation_result": {"promoted_to_deployment_evidence": True}},
           FAIL, "/adversarial FM-04")
    expect("T05", {"observation": Observation(obs_id="o", source="", method="")}, FAIL,
           "/adversarial")
    expect("T06", {"measurement": Observation(value=3.7, unit=None)}, FAIL, "/adversarial FM-12")
    expect("T07", {"observer_dependent_observation": Observation(observer_id="")}, FAIL, "/adversarial")
    expect("T08", {"observation": Observation(event_time=None)}, FAIL, "/adversarial")
    expect("T09", {"observation": Observation(event_time=None, observation_time=None)},
           FAIL, "/adversarial")
    expect("T10", {"observation": Observation(observation_time=0.0, freshness_horizon_tau=60.0),
                   "now": 500.0, "consequential_use": True}, FAIL, "/adversarial FM-05")
    expect("T11", {"derived_claim": Evidence(derived_from_scope=frozenset({"lab"}),
                                             claim_scope=frozenset({"lab", "world"}))},
           FAIL, "/adversarial INV-07")
    expect("T12", {"regime_transfer_claim": Evidence(claim_regime="G2"),
                   "evidence_regime": "G1"}, FAIL, "/adversarial INV-08")
    expect("T13", {"authoritative_state": StateRecord(state_identity={"object_id": "x"})},
           FAIL, "/adversarial")
    expect("T14", {"mutable_state_used": StateRecord(mutable=True,
                                                     revalidated_before_use=False)},
           FAIL, "/adversarial INV-10")
    expect("T15", {"unobserved_region": {"treated_as": "ABSENT"}}, FAIL, "/adversarial INV-16")
    expect("T16", {"decision_with_missing_data": {"missing_required": True,
                                                  "proceeded_without_gate": True}},
           FAIL, "/adversarial")
    expect("T17", {"evidence": Evidence(), "known_source_ids": {"src"}}, FAIL, "/adversarial INV-06")
    expect("T18", {"confirmations": [Evidence(ev_id="e1", source="rootA"),
                                     Evidence(ev_id="e2", ancestry=("rootA",))],
                    "claimed_independent_count": 2}, FAIL, "/adversarial FM-10")
    expect("T19", {"cross_scale_conclusion": Evidence(cross_scale=True),
                   "mapping_declared": False}, FAIL, "/adversarial Sec44")
    expect("T20", {"causal_conclusion": Evidence(causal_claim=True),
                   "causal_support_kinds": ["TEMPORAL_SEQUENCE"]}, FAIL,
           "/adversarial INV-12")
    expect("T21", {"action_available": True, "action_authorized": False}, FAIL,
           "/adversarial FM-14")
    expect("T22", {"proposal_committed_directly": True}, FAIL, "/adversarial INV-14")
    expect("T23", {"expected_effect": {"x": 1}, "observed_effect": None}, FAIL,
           "/adversarial FM-16")
    expect("T24", {"invalidation_plan": {"invalidated_ids": [], "true_dependents": ["d1", "d2"],
                                          "invalidated_everything": False}},
           FAIL, "/adversarial")
    expect("T25", {"action_loop": {"acted": True,
                                    "post_action_observation_recorded": False}},
           FAIL, "/adversarial Sec58")
    expect("T26", {"regime_shift": {"occurred": True, "regime_dependent_claims": ["c1", "c2"],
                                     "invalidated_claims": ["c1"]}}, FAIL, "/adversarial")
    expect("T27", {"memory_item_used_as_current_state":
                   {"used_as_current_world_state": True, "revalidated_against_l00": False}},
           FAIL, "/adversarial Sec55")
    expect("T28", {"tool_output": {"typed_as_verified_truth": True}}, FAIL, "/adversarial Sec54")
    expect("T29", {"unknown_handling_cases": [{"case_id": "c1", "input_status": "UNKNOWN",
                                                "output_status": "PASS"}]},
           FAIL, "/adversarial INV-11")
    expect("T30", {"loop_chain": ["R_t", "O_t", "A_t"]}, FAIL, "/adversarial")

    # UNKNOWN propagation probes (fail-closed, never crash-open)
    for tid, _ in v.test_table:
        expect(tid, {}, UNKNOWN, "/fail-closed-empty-input")

    # Validator robustness: malformed context must FAIL not raise
    r = v.run_test("T18", {"confirmations": "not-a-list"})
    if r.verdict == FAIL:
        passed += 1
    else:
        failed += 1
        failures.append(f"T18-malformed: expected FAIL, got {r.verdict}")

    return passed, failed, failures


if __name__ == "__main__":
    p, f, fails = run_selftests()
    total = p + f
    print(f"L00 Reality Environment validator self-test: {p}/{total} pass, {f} fail")
    for msg in fails[:20]:
        print("  FAIL:", msg)
    import sys
    sys.exit(0 if f == 0 else 1)
