#!/usr/bin/env python3
"""
AMOS ULK ALU-02 bounded first-order unification reference checker.

Origin architect / steward: Trang Phan.
Status: CANDIDATE / PARTIAL_EXECUTABLE_EVIDENCE if validation passes.
Scope: finite first-order term unification with occurs-check.
Non-claims: not a complete FOL theorem prover, not quantifier reasoning,
not model finding, not canon promotion, not authority.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Any, Tuple, Optional

Term = Dict[str, Any]
Subst = Dict[str, Term]

class UnificationError(ValueError):
    pass

def is_var(t: Term) -> bool:
    return isinstance(t, dict) and set(t.keys()) == {"var"} and isinstance(t["var"], str) and bool(t["var"])

def is_const(t: Term) -> bool:
    return isinstance(t, dict) and set(t.keys()) == {"const"} and isinstance(t["const"], str) and bool(t["const"])

def is_fun(t: Term) -> bool:
    return (
        isinstance(t, dict)
        and set(t.keys()) == {"fun", "args"}
        and isinstance(t["fun"], str)
        and bool(t["fun"])
        and isinstance(t["args"], list)
    )

def validate_term(t: Term) -> None:
    if is_var(t) or is_const(t):
        return
    if is_fun(t):
        for a in t["args"]:
            validate_term(a)
        return
    raise UnificationError(f"Malformed term: {t!r}")

def term_eq(a: Term, b: Term) -> bool:
    return a == b

def walk(t: Term, s: Subst) -> Term:
    seen = set()
    while is_var(t) and t["var"] in s:
        v = t["var"]
        if v in seen:
            raise UnificationError("Cyclic substitution detected")
        seen.add(v)
        t = s[v]
    return t

def apply_subst(t: Term, s: Subst) -> Term:
    t = walk(t, s)
    if is_fun(t):
        return {"fun": t["fun"], "args": [apply_subst(a, s) for a in t["args"]]}
    return copy_term(t)

def copy_term(t: Term) -> Term:
    if is_var(t):
        return {"var": t["var"]}
    if is_const(t):
        return {"const": t["const"]}
    if is_fun(t):
        return {"fun": t["fun"], "args": [copy_term(a) for a in t["args"]]}
    raise UnificationError(f"Malformed term: {t!r}")

def occurs(var: str, t: Term, s: Subst) -> bool:
    t = walk(t, s)
    if is_var(t):
        return t["var"] == var
    if is_const(t):
        return False
    if is_fun(t):
        return any(occurs(var, a, s) for a in t["args"])
    raise UnificationError(f"Malformed term: {t!r}")

def normalize_subst(s: Subst) -> Subst:
    out = {v: apply_subst(t, s) for v, t in s.items()}
    # Remove trivial self-bindings if any.
    return {v: t for v, t in out.items() if not (is_var(t) and t["var"] == v)}

def bind_var(v: str, t: Term, s: Subst) -> Subst:
    t = walk(t, s)
    if is_var(t) and t["var"] == v:
        return s
    if occurs(v, t, s):
        raise UnificationError(f"Occurs-check failed: {v} occurs in {t!r}")
    ns = dict(s)
    ns[v] = copy_term(t)
    return normalize_subst(ns)

def unify_terms(a: Term, b: Term, s: Optional[Subst] = None) -> Subst:
    validate_term(a); validate_term(b)
    s = {} if s is None else normalize_subst(dict(s))
    a = walk(a, s); b = walk(b, s)

    if term_eq(a, b):
        return normalize_subst(s)
    if is_var(a):
        return bind_var(a["var"], b, s)
    if is_var(b):
        return bind_var(b["var"], a, s)
    if is_const(a) and is_const(b):
        raise UnificationError(f"Constant mismatch: {a!r} vs {b!r}")
    if is_fun(a) and is_fun(b):
        if a["fun"] != b["fun"] or len(a["args"]) != len(b["args"]):
            raise UnificationError("Function symbol/arity mismatch")
        for xa, xb in zip(a["args"], b["args"]):
            s = unify_terms(apply_subst(xa, s), apply_subst(xb, s), s)
        return normalize_subst(s)
    raise UnificationError(f"Type mismatch: {a!r} vs {b!r}")

def check_unifies(a: Term, b: Term, s: Subst) -> bool:
    return apply_subst(a, s) == apply_subst(b, s)

def run_request(req: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(req, dict) or set(req.keys()) != {"left", "right"}:
        return {"success": False, "status": "REJECT_MALFORMED_REQUEST", "substitution": None}
    try:
        s = unify_terms(req["left"], req["right"])
        ok = check_unifies(req["left"], req["right"], s)
        return {
            "success": bool(ok),
            "status": "UNIFIED" if ok else "INTERNAL_CHECK_FAILED",
            "substitution": s if ok else None,
            "scope": "bounded_first_order_term_unification_with_occurs_check",
        }
    except UnificationError as e:
        return {
            "success": False,
            "status": "NOT_UNIFIABLE_OR_INVALID",
            "diagnostic": str(e),
            "substitution": None,
            "scope": "bounded_first_order_term_unification_with_occurs_check",
        }

if __name__ == "__main__":
    import sys, json
    req = json.load(sys.stdin)
    print(json.dumps(run_request(req), sort_keys=True))