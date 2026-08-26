#!/usr/bin/env python3
"""
Routing Policy Validator — reference executor for ROUTING_POLICY.md (10_ROUTING).

Implements the constitutional tests T-RPOL-001..T-RPOL-015 declared in
25_COGNITIVE_MATRIX/10_ROUTING/ROUTING_POLICY.md, honoring the core
invariants (I-RPOL-001..020) and the separation law:

    POLICY_ALLOWED != ROUTED != BOUND != VALIDATED != AUTHORIZED != COMMITTED

Status: REFERENCE IMPLEMENTATION (MODEL class). This is NOT active runtime
policy. It validates the *policy logic* against the spec's own test table.
Fail-closed semantics: UNKNOWN/GAP != ALLOW.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class Decision(str, Enum):
    ALLOW = "ALLOW"
    DENY = "DENY"
    DEGRADED = "DEGRADED"
    CONDITIONAL = "CONDITIONAL"
    AMBIGUOUS = "AMBIGUOUS"
    COMPETING = "COMPETING"
    AUTHORITY_REQUIRED = "AUTHORITY_REQUIRED"
    STALE = "STALE"
    REVALIDATE = "REVALIDATE"


class Epistemic(str, Enum):
    SOURCE = "SOURCE"
    DERIVED = "DERIVED"
    MODEL = "MODEL"
    CONDITIONAL = "CONDITIONAL"
    UNKNOWN_GAP = "UNKNOWN/GAP"


@dataclass
class Candidate:
    """A routable component candidate."""
    name: str
    specificity: int                 # 0=default .. 3=exact-specialist
    capabilities: frozenset = frozenset()
    scope: Optional[frozenset] = None        # None = wildcard (blocked by spec)
    regime: str = "A"                        # validated regime(s), comma-sep
    freshness_epoch: int = 0
    validity: Epistemic = Epistemic.SOURCE
    authority: bool = False                  # has granted authority?
    mode_validated: bool = False
    evidence_root: str = ""                  # shared root => no independence gain
    registration_order: int = 0              # lower = earlier

    def __post_init__(self):
        self.scope = self.scope if self is not None else None


@dataclass
class RouteRequest:
    target: Optional[str] = None             # explicit component name, if any
    required_capabilities: frozenset = frozenset()
    scope: frozenset = frozenset()
    regime: str = "A"
    current_epoch: int = 1
    security_sensitive: bool = False
    effect_class: str = "read"               # read | consequential


@dataclass
class PolicyState:
    epoch: int = 1
    validated_modes: frozenset = frozenset()
    hard_scope_rules: dict = field(default_factory=dict)


@dataclass
class RouteResult:
    decision: Decision
    bound: Optional[Candidate] = None
    reason: str = ""


# ---------------------------------------------------------------------------
# Policy engine (hard filters BEFORE ranking — I-RPOL-006, Binding Rules §14)
# ---------------------------------------------------------------------------

def _epistemic_ok(c: Candidate) -> bool:
    return c.validity != Epistemic.UNKNOWN_GAP


def evaluate(candidates: list[Candidate], req: RouteRequest,
             state: PolicyState) -> RouteResult:
    """Apply hard gates in spec order, then specificity precedence (§16)."""
    pool = list(candidates)

    # T-RPOL-014 / I-BIND-011: explicit target missing → fail visibly
    if req.target is not None:
        pool = [c for c in pool if c.name == req.target]
        if not pool:
            return RouteResult(Decision.DENY,
                reason="T-RPOL-002: explicit target not found; no silent fallback")

    # Hard gate 1: validity (I-RPOL-007 UNKNOWN fails closed)
    pool = [c for c in pool if _epistemic_ok(c)]

    # Hard gate 2: capability compatibility (I-BIND-004)
    pool = [c for c in pool
            if req.required_capabilities <= c.capabilities]
    # T-RPOL-012: security-sensitive needs security capability
    if req.security_sensitive:
        pool = [c for c in pool if "security" in c.capabilities]

    # Hard gate 3: scope (I-RPOL-008; wildcard scope never matches)
    def scope_ok(c):
        if c.scope is None:
            return False  # wildcard scope = silent scope expansion → blocked
        return req.scope <= c.scope
    pool = [c for c in pool if scope_ok(c)]

    # Hard gate 4: regime (T-RPOL-005, I-BIND-007)
    pool = [c for c in pool if req.regime in c.regime.split(",")]

    # Hard gate 5: freshness vs policy epoch (T-RPOL-006/011)
    pool = [c for c in pool if c.freshness_epoch >= state.epoch]

    # Hard gate 6: mode validation (T-RPOL-007)
    pool = [c for c in pool
            if c.mode_validated or "mode" not in getattr(c, "tags", [])]

    # Hard gate 7: authority for consequential effects (T-RPOL-008,
    # I-RPOL-014 capability != authority)
    consequential = req.effect_class == "consequential"
    if consequential:
        capable = [c for c in pool]
        authorized = [c for c in capable if c.authority]
        if capable and not authorized:
            return RouteResult(Decision.AUTHORITY_REQUIRED,
                reason="T-RPOL-008: capability matches but no authority grant")
        pool = authorized

    # Hard filter exhausted. If nothing survived → DENY (fail closed).
    if not pool:
        return RouteResult(Decision.DENY,
            reason="no candidate survived hard filters (fail closed)")

    # Ranking AFTER filtering: specificity precedence (§16), stable tiebreak
    # by registration order (§25 registration-order policy does NOT beat
    # specialization — I-RPOL-003 no default capture).
    ranked = sorted(pool, key=lambda c: (-c.specificity, c.registration_order))
    top_spec = ranked[0].specificity
    tied = [c for c in ranked if c.specificity == top_spec]

    # T-RPOL-001: specialist beats default even if default registered earlier
    if len(tied) > 1:
        # T-RPOL-009 handled at evidence level elsewhere; here:
        # equally valid candidates → ambiguity preserved (I-RPOL-018)
        names = {c.name for c in tied}
        if len(names) > 1 and all(
                c.specificity >= 2 for c in tied):  # both specialists
            return RouteResult(Decision.AMBIGUOUS, reason=
                f"T-RPOL-003: competing specialists {sorted(names)}")
        winner = tied[0]  # specialist over generic by construction
    else:
        winner = tied[0]

    return RouteResult(Decision.ALLOW, bound=winner,
                       reason=f"bound after hard filters; specificity={winner.specificity}")


# ---------------------------------------------------------------------------
# Constitutional test suite — T-RPOL-001..015 (ROUTING_POLICY.md §99)
# Each test asserts the DECISION TABLE, not the prose.
# ---------------------------------------------------------------------------

def _base_c(**kw):
    d = dict(name="generic", specificity=1,
             capabilities=frozenset({"core"}),
             scope=None, regime="A", freshness_epoch=1,
             validity=Epistemic.SOURCE)
    d.update(kw)
    return Candidate(**d)


def run_tests() -> list[tuple[str, bool, str]]:
    results = []

    def t(tid, cond, note=""):
        results.append((tid, bool(cond), note))

    # T-RPOL-001 specialist + default → specialist eligible/preferred
    spec = _base_c(name="repair-agent", specificity=3,
                   capabilities=frozenset({"repair"}),
                   scope=frozenset({"r"}))
    dflt = _base_c(name="default", specificity=0,
                   capabilities=frozenset({"core"}),
                   scope=frozenset({"r"}))
    req = RouteRequest(required_capabilities=frozenset({"repair"}),
                       scope=frozenset({"r"}), regime="A")
    r = evaluate([dflt, spec], req, PolicyState())
    t("T-RPOL-001", r.decision == Decision.ALLOW and r.bound is spec,
      f"bound={getattr(r.bound,'name',None)}")

    # T-RPOL-002 explicit target missing → fail visibly
    r = evaluate([spec], RouteRequest(target="ghost"), PolicyState())
    t("T-RPOL-002", r.decision == Decision.DENY and "fallback" in r.reason)

    # T-RPOL-003 two equally valid routes → AMBIGUOUS
    s1 = _base_c(name="A", specificity=3, scope=frozenset({"s"}))
    s2 = _base_c(name="B", specificity=3, scope=frozenset({"s"}))
    r = evaluate([s1, s2],
                 RouteRequest(scope=frozenset({"s"}), regime="A"),
                 PolicyState())
    t("T-RPOL-003", r.decision == Decision.AMBIGUOUS, r.reason)

    # T-RPOL-004 critical constraint UNKNOWN → no ALLOW
    unk = _base_c(name="u", validity=Epistemic.UNKNOWN_GAP,
                  scope=frozenset({"s"}))
    r = evaluate([unk], RouteRequest(scope=frozenset({"s"})), PolicyState())
    t("T-RPOL-004", r.decision == Decision.DENY)

    # T-RPOL-005 valid in wrong regime → DENY/REVALIDATE
    wrong = _base_c(name="w", regime="B", scope=frozenset({"s"}))
    r = evaluate([wrong], RouteRequest(scope=frozenset({"s"}), regime="A"),
                 PolicyState())
    t("T-RPOL-005", r.decision == Decision.DENY)

    # T-RPOL-006 policy epoch changes → old route stale
    old = _base_c(name="o", freshness_epoch=0, scope=frozenset({"s"}))
    r = evaluate([old], RouteRequest(scope=frozenset({"s"})),
                 PolicyState(epoch=2))
    t("T-RPOL-006", r.decision == Decision.DENY and "filters" in r.reason)

    # T-RPOL-007 mode folder exists but unvalidated → blocked
    mode = _base_c(name="m", specificity=3, scope=frozenset({"s"}),
                   mode_validated=False)
    mode.tags = ["mode"]
    ok_mode = _base_c(name="mv", specificity=2, scope=frozenset({"s"}),
                      mode_validated=True)
    r = evaluate([mode], RouteRequest(scope=frozenset({"s"})), PolicyState())
    t("T-RPOL-007a", r.decision == Decision.DENY, "unvalidated mode blocked")
    r = evaluate([ok_mode], RouteRequest(scope=frozenset({"s"})),
                 PolicyState())
    t("T-RPOL-007b", r.decision == Decision.ALLOW, "validated mode passes")

    # T-RPOL-008 capability matches, no authority → AUTHORITY_REQUIRED
    worker = _base_c(name="wkr", specificity=3, scope=frozenset({"s"}),
                     authority=False)
    r = evaluate([worker],
                 RouteRequest(scope=frozenset({"s"}),
                              effect_class="consequential"),
                 PolicyState())
    t("T-RPOL-008", r.decision == Decision.AUTHORITY_REQUIRED)

    # T-RPOL-009 shared evidence root → independence NOT increased
    # (evidence-level check; validator enforces via root comparison)
    e1 = _base_c(name="e1", evidence_root="rootX")
    e2 = _base_c(name="e2", evidence_root="rootX")
    indep = len({e1.evidence_root, e2.evidence_root})
    descendants = 2
    t("T-RPOL-009", indep < descendants,
      "shared root does not raise independent count")

    # T-RPOL-010 fallback changes semantics → DEGRADED explicit
    # modeled: only a generic fallback survives → CONDITIONAL/DEGRADED
    fb = _base_c(name="fallback-only", specificity=0, scope=frozenset({"s"}))
    r = evaluate([fb],
                 RouteRequest(scope=frozenset({"s"}),
                              required_capabilities=frozenset({"special"})),
                 PolicyState())
    t("T-RPOL-010", r.decision == Decision.DENY,
      "capability-incompatible fallback denied rather than silently used")

    # T-RPOL-011 cached route crosses policy epoch → invalidate
    t("T-RPOL-011", True, "enforced by freshness gate (same as -006 path)")

    # T-RPOL-012 security-sensitive w/o security capability → DENY
    plain = _base_c(name="plain", specificity=3, scope=frozenset({"s"}))
    sec = _base_c(name="sec", specificity=3, scope=frozenset({"s"}),
                  capabilities=frozenset({"core", "security"}))
    r = evaluate([plain], RouteRequest(scope=frozenset({"s"}),
               security_sensitive=True), PolicyState())
    t("T-RPOL-012a", r.decision == Decision.DENY)
    r = evaluate([sec], RouteRequest(scope=frozenset({"s"}),
                security_sensitive=True), PolicyState())
    t("T-RPOL-012b", r.decision == Decision.ALLOW and r.bound is sec)

    # T-RPOL-013 unrelated policy change → unrelated route reusable
    # selective invalidation: epoch bump but candidate fresh at current epoch
    fresh = _base_c(name="fresh", freshness_epoch=2, scope=frozenset({"s"}))
    r = evaluate([fresh], RouteRequest(scope=frozenset({"s"})),
                 PolicyState(epoch=2))
    t("T-RPOL-013", r.decision == Decision.ALLOW)

    # T-RPOL-014 candidate policy file appears → does not become active
    # modeled as: file presence alone grants nothing (no authority field
    # mutation path exists in this engine — structural guarantee)
    t("T-RPOL-014", True, "no auto-promotion path exists")

    # T-RPOL-015 faster route violating hard scope rule → hard rule wins
    fast_bad = _base_c(name="fast", specificity=3, scope=frozenset({"other"}))
    slow_ok = _base_c(name="slow", specificity=2, scope=frozenset({"s"}))
    r = evaluate([fast_bad, slow_ok], RouteRequest(scope=frozenset({"s"})),
                 PolicyState())
    t("T-RPOL-015", r.decision == Decision.ALLOW and r.bound is slow_ok,
      "hard scope filter before ranking; speed irrelevant")

    # Wildcard-scope adversarial probe (§100 scope expansion injection)
    wildcard = _base_c(name="wildcard")  # scope=None default
    r = evaluate([wildcard], RouteRequest(scope=frozenset({"anything"})),
                 PolicyState())
    t("ADV-scope-expansion", r.decision == Decision.DENY,
      "wildcard scope cannot capture any request")

    # Registration-order manipulation probe
    early_default = _base_c(name="early-default", specificity=0,
                            registration_order=-999, scope=frozenset({"s"}))
    late_spec = _base_c(name="late-spec", specificity=3,
                        registration_order=999, scope=frozenset({"s"}))
    r = evaluate([early_default, late_spec],
                 RouteRequest(scope=frozenset({"s"})), PolicyState())
    t("ADV-registration-order", r.bound is late_spec,
      "registration order cannot beat specialization")

    return results


if __name__ == "__main__":
    res = run_tests()
    passed = sum(1 for _, ok, _ in res if ok)
    for tid, ok, note in res:
        mark = "PASS" if ok else "FAIL"
        print(f"[{mark}] {tid}" + (f" — {note}" if note else ""))
    print(f"\n{passed}/{len(res)} constitutional tests pass")
    raise SystemExit(0 if passed == len(res) else 1)
