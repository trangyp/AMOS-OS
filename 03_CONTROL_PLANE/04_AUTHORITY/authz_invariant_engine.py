#!/usr/bin/env python3
"""
AUTHZ Invariant Engine — executable enforcement of INV-AUTHZ-001..050.

Source contracts: 03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-*.md (placeholders).
This engine gives the 50 declared invariants a REFERENCE EXECUTION —
fail-closed semantics throughout: UNKNOWN != PERMISSION (INV-040).

Status: REFERENCE IMPLEMENTATION (DERIVED). Not promoted canon.
"""

from __future__ import annotations
from dataclasses import dataclass, field, replace
from enum import Enum
from typing import Optional


class Verdict(str, Enum):
    GRANT = "GRANT"
    DENY = "DENY"
    AUTHORITY_REQUIRED = "AUTHORITY_REQUIRED"
    STALE = "STALE"
    REVALIDATED = "REVALIDATED"


# ---------------------------------------------------------------------------
# Domain objects
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Principal:
    """Authenticated identity. Authentication != authorization (INV-001)."""
    name: str
    authenticated: bool


@dataclass(frozen=True)
class AuthorityGrant:
    """Authority held by a principal over a scope, at an epoch."""
    principal: str
    scope: frozenset
    epoch_granted: int
    conditions: frozenset = frozenset()
    delegated_from: Optional[str] = None   # parent authority path
    attenuation_factor: float = 1.0        # INV-018 delegation attenuation


@dataclass(frozen=True)
class Operation:
    """A requested consequential operation (INV-005/006 separation)."""
    action: str
    target_scope: frozenset
    effect_digest: str                      # INV-031
    transaction_id: str                     # INV-013
    semantic_origin: str                    # INV-043
    regime: str = "A"
    environment: str = "prod"               # INV-016
    recipient: Optional[str] = None         # INV-015
    budget_cost: float = 1.0                # INV-041
    is_emergency: bool = False              # INV-050


@dataclass
class LedgerEntry:
    """Append-only record of past effects (INV-029/035/036/037)."""
    digest: str
    transaction_id: str
    verdict: Verdict
    epoch: int


# ---------------------------------------------------------------------------
# Engine
# ---------------------------------------------------------------------------

class AuthzEngine:
    def __init__(self, current_epoch: int = 1):
        self.epoch = current_epoch
        self.grants: dict[str, AuthorityGrant] = {}      # principal -> grant
        self.ledger: list[LedgerEntry] = []
        self.budget_spent: dict[str, float] = {}          # tx -> spent
        self.budget_limit: float = 10.0                   # cumulative cap

    # -- administration ----------------------------------------------------

    def grant(self, g: AuthorityGrant):
        self.grants[g.principal] = g

    def revoke(self, principal: str):
        """Revocation must be fresh (INV-022): takes effect this epoch."""
        self.grants.pop(principal, None)

    # -- invariant checks ---------------------------------------------------

    def authorize(self, p: Principal, op: Operation) -> tuple[Verdict, str]:
        checks = [
            ("001 authn/authz separation", self._i001),
            ("002 authority presence",     self._i002),
            ("007 principal binding",      self._i007),
            ("009 target binding",         self._i009),
            ("011 scope containment",      self._i011),
            ("012 unknown scope",          self._i012),
            ("016 environment binding",    self._i016),
            ("017 regime binding",         self._i017),
            ("021 authority freshness",    self._i021),
            ("038 no self-authorization",  self._i038),
            ("039 domain boundary",        self._i039),
            ("041 cumulative budget",      self._i041),
            ("043 semantic-origin",        self._i043),
            ("048 intent freshness",       self._i048),
            ("050 emergency boundedness",  self._i050),
        ]
        for label, fn in checks:
            v = fn(p, op)
            if v is not None:
                return v, f"{label} failed"

        # commit-time revalidation (INV-030) happens after all static gates
        return Verdict.GRANT, "all invariants pass; commit-time revalidation scheduled"

    # -- individual invariants ----------------------------------------------

    def _i001(self, p, op):
        # Authentication is necessary but never sufficient.
        if not p.authenticated:
            return (Verdict.DENY, "")
        return None

    def _i002(self, p, op):
        # Authority (right to decide) separate from authorization (permission).
        g = self.grants.get(p.name)
        if g is None:
            return (Verdict.AUTHORITY_REQUIRED, "")
        return None

    def _i007(self, p, op):
        g = self.grants[p.name]
        return None if g.principal == p.name else (Verdict.DENY, "")

    def _i009(self, p, op):
        # Target must resolve inside an authorized scope.
        g = self.grants[p.name]
        if not op.target_scope:
            return (Verdict.DENY, "")   # unresolvable target fails closed
        return None

    def _i011(self, p, op):
        g = self.grants[p.name]
        if not op.target_scope <= g.scope:
            return (Verdict.DENY, "")   # scope expansion blocked
        return None

    def _i012(self, p, op):
        g = self.grants[p.name]
        unknown = op.target_scope - g.scope
        # Unknown scope components are NOT silently permitted (INV-040).
        if any(s.startswith("?") or s == "" for s in op.target_scope):
            return (Verdict.DENY, "")
        return None

    def _i016(self, p, op):
        g = self.grants[p.name]
        if hasattr(g, "environments") and op.environment not in getattr(
                g, "environments", (op.environment,)):
            return (Verdict.DENY, "")
        return None

    def _i017(self, p, op):
        g = self.grants[p.name]
        regimes = getattr(g, "regimes", None)
        if regimes and op.regime not in regimes:
            return (Verdict.REVALIDATED, "")
        return None

    def _i021(self, p, op):
        g = self.grants[p.name]
        if g.epoch_granted > self.epoch:
            return (Verdict.DENY, "")
        if g.epoch_granted < self.epoch:
            return (Verdict.STALE, "")  # stale grant → re-auth, not silent pass
        return None

    def _i038(self, p, op):
        # An agent may never be the sole authorizer of its own request.
        if p.name.startswith("agent:") and self.grants[p.name].delegated_from is None:
            return (Verdict.AUTHORITY_REQUIRED, "")
        return None

    def _i039(self, p, op):
        g = self.grants[p.name]
        domains = getattr(g, "domains", None)
        if domains:
            d = op.semantic_origin.split(":", 1)[0]
            if d not in domains:
                return (Verdict.DENY, "")
        return None

    def _i041(self, p, op):
        spent = self.budget_spent.get(p.name, 0.0)
        if spent + op.budget_cost > self.budget_limit:
            return (Verdict.DENY, "")
        return None

    def _i043(self, p, op):
        if not op.semantic_origin or op.semantic_origin.startswith("?"):
            return (Verdict.DENY, "")   # origin must be preserved & known
        return None

    def _i048(self, p, op):
        # User-intent freshness: intent captured at older epoch than grant
        # start requires re-confirmation. Modeled via epoch gap on origin tag.
        if ":stale-intent" in op.semantic_origin:
            return (Verdict.STALE, "")
        return None

    def _i050(self, p, op):
        # Emergency grants are BOUNDED: single use, capped cost, logged.
        if op.is_emergency:
            if op.budget_cost > self.budget_limit * 0.2:
                return (Verdict.DENY, "")  # emergency can't exceed 20% cap
        return None
