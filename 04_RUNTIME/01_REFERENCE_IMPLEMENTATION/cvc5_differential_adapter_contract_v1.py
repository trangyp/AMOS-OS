"""Fail-closed cvc5 differential SMT adapter contract for AMOS.

Origin architect / steward: Trang Phan.

The adapter preserves cvc5 SAT/UNSAT/UNKNOWN as solver-scoped evidence. It is
intended for bounded differential checking of formulas already expressed in a
supported SMT theory. Solver agreement is evidence about an encoding, not proof
of empirical truth, causal effect, Canon status, or deployment authority.
"""
from __future__ import annotations

import importlib.util
import shutil
from typing import Any, Dict, Optional

SOURCE_PROVENANCE = {
    "project": "https://github.com/cvc5/cvc5",
    "result_api": "https://cvc5.github.io/docs/cvc5-1.1.2/api/python/base/result.html",
    "release_line": "cvc5-1.3.4 stable release observed 2026-05-07; later prerelease material is not an automatic dependency lock",
}
NATIVE_RESULTS = frozenset({"SAT", "UNSAT", "UNKNOWN"})


def binding_state(expected_version: Optional[str] = None) -> Dict[str, Any]:
    exe = shutil.which("cvc5")
    module_available = importlib.util.find_spec("cvc5") is not None
    if not exe and not module_available:
        return {
            "success": False,
            "status": "UNAVAILABLE_HOLD",
            "tool": "cvc5",
            "executable": None,
            "python_module_available": False,
            "expected_version": expected_version,
            "exact_version_bound": False,
            "authority_granted": False,
        }
    if not isinstance(expected_version, str) or not expected_version.strip():
        return {
            "success": False,
            "status": "HOLD_EXACT_VERSION_REQUIRED",
            "tool": "cvc5",
            "executable": exe,
            "python_module_available": module_available,
            "expected_version": expected_version,
            "exact_version_bound": False,
            "authority_granted": False,
        }
    observed = None
    if module_available:
        try:
            import cvc5  # type: ignore
            observed = str(getattr(cvc5, "__version__", "")) or None
        except Exception:
            observed = None
    if observed is None:
        return {
            "success": False,
            "status": "HOLD_VERSION_UNRESOLVED",
            "tool": "cvc5",
            "executable": exe,
            "python_module_available": module_available,
            "expected_version": expected_version,
            "exact_version_bound": False,
            "authority_granted": False,
        }
    match = observed == expected_version.strip()
    return {
        "success": match,
        "status": "BOUND_EXACT_VERSION" if match else "HOLD_VERSION_MISMATCH",
        "tool": "cvc5",
        "executable": exe,
        "python_module_available": module_available,
        "expected_version": expected_version.strip(),
        "observed_version": observed,
        "exact_version_bound": match,
        "authority_granted": False,
    }


def normalize_result(result: Any, *, theory_scope: str, unknown_explanation: Optional[str] = None) -> Dict[str, Any]:
    if not isinstance(theory_scope, str) or not theory_scope.strip():
        return {"success": False, "status": "ILL_TYPED_SCOPE", "authority_granted": False}
    token = str(result).strip().upper()
    if token not in NATIVE_RESULTS:
        return {"success": False, "status": "ILL_TYPED_SOLVER_RESULT", "observed": token, "authority_granted": False}
    if token == "UNKNOWN" and unknown_explanation is not None and not isinstance(unknown_explanation, str):
        return {"success": False, "status": "ILL_TYPED_UNKNOWN_EXPLANATION", "authority_granted": False}
    return {
        "success": True,
        "status": "SOLVER_RESULT_PRESERVED",
        "solver_result": token,
        "unknown_explanation": unknown_explanation if token == "UNKNOWN" else None,
        "theory_scope": theory_scope.strip(),
        "epistemic_class": "EXTERNAL_FORMAL_SOLVER_RESULT",
        "empirical_truth": "NOT_ESTABLISHED",
        "causal_inference": "NOT_ESTABLISHED",
        "canon_promoted": False,
        "authority_granted": False,
    }


def differential_verdict(reference_result: Any, cvc5_result: Any, *, theory_scope: str) -> Dict[str, Any]:
    """Compare native solver states without treating agreement as truth."""
    left = normalize_result(reference_result, theory_scope=theory_scope)
    right = normalize_result(cvc5_result, theory_scope=theory_scope)
    if not left.get("success") or not right.get("success"):
        return {
            "success": False,
            "status": "DIFFERENTIAL_INPUT_INVALID",
            "reference": left,
            "cvc5": right,
            "authority_granted": False,
        }
    same = left["solver_result"] == right["solver_result"]
    return {
        "success": same,
        "status": "AGREE" if same else "DISAGREE_REVIEW",
        "reference_result": left["solver_result"],
        "cvc5_result": right["solver_result"],
        "theory_scope": theory_scope.strip(),
        "agreement_is_truth": False,
        "authority_granted": False,
    }
