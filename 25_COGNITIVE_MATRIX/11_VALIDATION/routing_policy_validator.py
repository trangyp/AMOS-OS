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
