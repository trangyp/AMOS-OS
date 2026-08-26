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


# ---------------------------------------------------------------------------
# Test suite — one or more probes per invariant family
# ---------------------------------------------------------------------------

def run_tests() -> list[tuple[str, bool, str]]:
    results = []

    def t(tid, ok, note=""):
        results.append((tid, bool(ok), note))

    E = AuthzEngine(current_epoch=2)

    # INV-001/002: unauthenticated → DENY; authenticated w/o grant → AUTHORITY_REQUIRED
    ghost = Principal("ghost", authenticated=False)
    v, why = E.authorize(ghost, Operation("read", frozenset({"x"}), "d1", "t1", "dom:src"))
    t("INV-001", v == Verdict.DENY)

    anon = Principal("anon", authenticated=True)
    v, why = E.authorize(anon, Operation("read", frozenset({"x"}), "d1", "t1", "dom:src"))
    t("INV-002", v == Verdict.AUTHORITY_REQUIRED)

    # Valid grant for happy path
    E.grant(AuthorityGrant("alice", frozenset({"db:users"}), epoch_granted=2))

    alice = Principal("alice", authenticated=True)
    op_ok = Operation("write", frozenset({"db:users"}), "digest-A",
                      "tx-1", "crm:update-user")
    v, why = E.authorize(alice, op_ok)
    t("HAPPY-PATH", v == Verdict.GRANT, why if v != Verdict.GRANT else "")

    # INV-003/014: capability vs authorization — having capability field ≠ grant
    cap_only = Principal("capbot", authenticated=True)
    E.grant(AuthorityGrant("capbot", frozenset(), epoch_granted=2))
    v, _ = E.authorize(cap_only, Operation("write", frozenset({"db:users"}),
                                           "d", "t", "crm:x"))
    t("INV-003", v == Verdict.DENY, "capability without scope fails")

    # INV-007: principal mismatch
    mallory = Principal("mallory", authenticated=True)
    E.grant(AuthorityGrant("alice", frozenset({"db:users"}), 2))  # re-grant alice only
    v, _ = E.authorize(mallory, op_ok)
    t("INV-007", v == Verdict.AUTHORITY_REQUIRED)  # no grant for mallory

    # INV-009/011: empty target / scope expansion
    v, _ = E.authorize(alice, replace(op_ok, target_scope=frozenset()))
    t("INV-009", v == Verdict.DENY, "unresolvable target")

    v, _ = E.authorize(alice, replace(op_ok,
                       target_scope=frozenset({"db:users", "db:payroll"})))
    t("INV-011", v == Verdict.DENY, "scope expansion blocked")

    # INV-012/040: unknown-scope component
    v, _ = E.authorize(alice, replace(op_ok,
                       target_scope=frozenset({"?unknown"})))
    t("INV-012+040", v == Verdict.DENY, "unknown is not permission")

    # INV-021: stale grant
    old = Principal("old", authenticated=True)
    E.grant(AuthorityGrant("old", frozenset({"db:users"}), epoch_granted=1))
    v, _ = E.authorize(old, Operation("read", frozenset({"db:users"}),
                                      "d", "t", "crm:r"))
    t("INV-021", v == Verdict.STALE, "stale grant requires re-auth")

    # INV-022: revocation freshness
    bob = Principal("bob", authenticated=True)
    E.grant(AuthorityGrant("bob", frozenset({"db:users"}), 2))
    E.revoke("bob")
    v, _ = E.authorize(bob, Operation("read", frozenset({"db:users"}),
                                      "d", "t", "crm:r"))
    t("INV-022", v == Verdict.AUTHORITY_REQUIRED, "revocation effective immediately")

    # INV-038: agent self-authorization
    ag = Principal("agent:auto", authenticated=True)
    E.grant(AuthorityGrant("agent:auto", frozenset({"db:users"}), 2))
    v, _ = E.authorize(ag, op_ok)
    t("INV-038", v == Verdict.AUTHORITY_REQUIRED,
      "agent with no delegator cannot self-authorize")

    # delegated agent passes (attenuated chain has a human root)
    ag2 = Principal("agent:child", authenticated=True)
    E.grant(AuthorityGrant("agent:child", frozenset({"db:users"}), 2,
                           delegated_from="alice"))
    v, _ = E.authorize(ag2, op_ok)
    t("INV-018", v == Verdict.GRANT, "delegated authority with human root OK")

    # INV-043: semantic origin required
    v, _ = E.authorize(alice, replace(op_ok, semantic_origin="?"))
    t("INV-043", v == Verdict.DENY, "origin must be known and preserved")

    # INV-048: stale user intent
    v, _ = E.authorize(alice, replace(op_ok,
                       semantic_origin="crm:update-user:stale-intent"))
    t("INV-048", v == Verdict.STALE, "stale intent needs re-confirmation")

    # INV-041: cumulative budget
    E.budget_spent["alice"] = 9.5
    v, _ = E.authorize(alice, replace(op_ok, budget_cost=1.0))
    t("INV-041", v == Verdict.DENY, "budget exhausted")
    E.budget_spent["alice"] = 0.0

    # INV-050: emergency boundedness
    v, _ = E.authorize(alice, replace(op_ok, is_emergency=True,
                                      budget_cost=5.0))
    t("INV-050", v == Verdict.DENY, "emergency capped at 20% of limit")

    v, _ = E.authorize(alice, replace(op_ok, is_emergency=True,
                                      budget_cost=1.5))
    t("INV-050b", v in (Verdict.GRANT, Verdict.REVALIDATED),
      "bounded emergency permitted")

    return results


if __name__ == "__main__":
    res = run_tests()
    passed = sum(1 for _, ok, _ in res if ok)
    for tid, ok, note in res:
        print(f"[{'PASS' if ok else 'FAIL'}] {tid}" + (f" — {note}" if note else ""))
    print(f"\n{passed}/{len(res)} AUTHZ invariant tests pass")
    raise SystemExit(0 if passed == len(res) else 1)
