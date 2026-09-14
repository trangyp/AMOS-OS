"""Bounded ALU-06 dependent Pi-type checker.

Origin architect / steward: Trang Phan.

This is a small executable reference calculus for a bounded dependent-type
fragment. It uses de Bruijn indices, predicative universes, dependent Pi types,
lambda abstraction/application, Nat, and beta-definitional equality.

It is not Lean/Coq, not a complete Calculus of Constructions implementation,
and not evidence of full ULK ALU-06 completion.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple, Union


class TypeCheckError(ValueError):
    pass


@dataclass(frozen=True)
class Universe:
    level: int

    def __post_init__(self) -> None:
        if self.level < 0:
            raise ValueError("universe level must be nonnegative")


@dataclass(frozen=True)
class Bound:
    index: int

    def __post_init__(self) -> None:
        if self.index < 0:
            raise ValueError("de Bruijn index must be nonnegative")


@dataclass(frozen=True)
class Pi:
    domain: "Term"
    codomain: "Term"


@dataclass(frozen=True)
class Lam:
    domain: "Term"
    body: "Term"


@dataclass(frozen=True)
class App:
    fn: "Term"
    arg: "Term"


@dataclass(frozen=True)
class NatType:
    pass


@dataclass(frozen=True)
class NatLit:
    value: int

    def __post_init__(self) -> None:
        if self.value < 0:
            raise ValueError("Nat literal must be nonnegative")


Term = Union[Universe, Bound, Pi, Lam, App, NatType, NatLit]
Context = Tuple[Term, ...]  # nearest binder first; entries stored at binding time


def shift(delta: int, cutoff: int, term: Term) -> Term:
    """Shift free de Bruijn indices >= cutoff by delta."""
    if isinstance(term, Bound):
        if term.index < cutoff:
            return term
        new_index = term.index + delta
        if new_index < 0:
            raise TypeCheckError("invalid negative de Bruijn index after shift")
        return Bound(new_index)
    if isinstance(term, Pi):
        return Pi(shift(delta, cutoff, term.domain), shift(delta, cutoff + 1, term.codomain))
    if isinstance(term, Lam):
        return Lam(shift(delta, cutoff, term.domain), shift(delta, cutoff + 1, term.body))
    if isinstance(term, App):
        return App(shift(delta, cutoff, term.fn), shift(delta, cutoff, term.arg))
    return term


def substitute(index: int, replacement: Term, term: Term) -> Term:
    """Capture-free substitution for one de Bruijn variable."""
    if isinstance(term, Bound):
        return replacement if term.index == index else term
    if isinstance(term, Pi):
        return Pi(
            substitute(index, replacement, term.domain),
            substitute(index + 1, shift(1, 0, replacement), term.codomain),
        )
    if isinstance(term, Lam):
        return Lam(
            substitute(index, replacement, term.domain),
            substitute(index + 1, shift(1, 0, replacement), term.body),
        )
    if isinstance(term, App):
        return App(
            substitute(index, replacement, term.fn),
            substitute(index, replacement, term.arg),
        )
    return term


def beta_substitute(body: Term, arg: Term) -> Term:
    """Substitute arg for Bound(0) in body and discharge the binder."""
    return shift(-1, 0, substitute(0, shift(1, 0, arg), body))


def normalize(term: Term, fuel: int = 2048) -> Term:
    """Full beta normalization for the bounded calculus."""
    if fuel <= 0:
        raise TypeCheckError("normalization fuel exhausted")
    if isinstance(term, Pi):
        return Pi(normalize(term.domain, fuel - 1), normalize(term.codomain, fuel - 1))
    if isinstance(term, Lam):
        return Lam(normalize(term.domain, fuel - 1), normalize(term.body, fuel - 1))
    if isinstance(term, App):
        fn = normalize(term.fn, fuel - 1)
        arg = normalize(term.arg, fuel - 1)
        if isinstance(fn, Lam):
            return normalize(beta_substitute(fn.body, arg), fuel - 1)
        return App(fn, arg)
    return term


def definitionally_equal(left: Term, right: Term) -> bool:
    return normalize(left) == normalize(right)


def _expect_universe(term: Term, context: Context) -> int:
    inferred = normalize(infer(term, context))
    if not isinstance(inferred, Universe):
        raise TypeCheckError(f"expected a type whose type is a Universe, got {inferred!r}")
    return inferred.level


def infer(term: Term, context: Context = ()) -> Term:
    """Infer the type of term under a well-formed de Bruijn context."""
    if isinstance(term, Universe):
        return Universe(term.level + 1)
    if isinstance(term, NatType):
        return Universe(0)
    if isinstance(term, NatLit):
        return NatType()
    if isinstance(term, Bound):
        if term.index >= len(context):
            raise TypeCheckError(f"unbound de Bruijn index {term.index}")
        return shift(term.index + 1, 0, context[term.index])
    if isinstance(term, Pi):
        u = _expect_universe(term.domain, context)
        v = _expect_universe(term.codomain, (term.domain,) + context)
        return Universe(max(u, v))
    if isinstance(term, Lam):
        _expect_universe(term.domain, context)
        body_type = infer(term.body, (term.domain,) + context)
        return Pi(term.domain, body_type)
    if isinstance(term, App):
        fn_type = normalize(infer(term.fn, context))
        if not isinstance(fn_type, Pi):
            raise TypeCheckError(f"application expects Pi type, got {fn_type!r}")
        arg_type = infer(term.arg, context)
        if not definitionally_equal(arg_type, fn_type.domain):
            raise TypeCheckError(
                f"application argument type mismatch: expected {fn_type.domain!r}, got {arg_type!r}"
            )
        return beta_substitute(fn_type.codomain, term.arg)
    raise TypeCheckError(f"unsupported term {term!r}")


def check(term: Term, expected: Term, context: Context = ()) -> bool:
    _expect_universe(expected, context)
    inferred = infer(term, context)
    if not definitionally_equal(inferred, expected):
        raise TypeCheckError(f"type mismatch: expected {expected!r}, got {inferred!r}")
    return True


def validate_reference_invariants() -> tuple[str, ...]:
    failures = []
    nat = NatType()
    identity = Lam(nat, Bound(0))
    try:
        if infer(identity) != Pi(nat, nat):
            failures.append("NAT_IDENTITY_TYPE_MISMATCH")
        beta = App(identity, NatLit(3))
        if normalize(beta) != NatLit(3):
            failures.append("BETA_REDUCTION_MISMATCH")
        dependent_identity = Lam(Universe(0), Lam(Bound(0), Bound(0)))
        expected = Pi(Universe(0), Pi(Bound(0), Bound(1)))
        if infer(dependent_identity) != expected:
            failures.append("DEPENDENT_IDENTITY_TYPE_MISMATCH")
    except Exception as exc:
        failures.append(f"REFERENCE_EXCEPTION:{type(exc).__name__}")
    return tuple(failures)
