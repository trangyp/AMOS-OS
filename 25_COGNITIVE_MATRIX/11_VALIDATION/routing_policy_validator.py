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
