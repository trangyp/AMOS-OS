"""Fail-closed Z3 muZ adapter contract for AMOS ULK/URK research lanes.

Origin architect / steward: Trang Phan.

muZ is treated as an external solver capability for Datalog / Constrained Horn
Clause fixed-point queries. Solver answers remain theory/program scoped and never
become empirical causation, Canon status, or effect authority.
"""
from __future__ import annotations

import importlib.util
import shutil
from typing import Any, Dict, Optional

SOURCE_PROVENANCE = {
    "guide": "https://microsoft.github.io/z3guide/docs/fixedpoints/intro/",
    "syntax": "https://microsoft.github.io/z3guide/docs/fixedpoints/syntax/",
    "pdr": "https://microsoft.github.io/z3guide/docs/fixedpoints/engineforpdr/",
}
NATIVE_RESULTS = frozenset({"SAT", "UNSAT", "UNKNOWN"})


def binding_state(expected_version: Optional[str] = None) -> Dict[str, Any]:
    exe = shutil.which("z3")
    module_available = importlib.util.find_spec("z3") is not None
    if not exe and not module_available:
        return {
            "success": False,
            "status": "UNAVAILABLE_HOLD",
            "tool": "Z3_muZ",
            "executable": None,
            "python_module_available": False,
            "expected_version": expected_version,
            "exact_version_bound": False,
            "capabilities": ["DATALOG", "CONSTRAINED_HORN_CLAUSES", "FIXEDPOINT", "PDR_SPACER"],
            "authority_granted": False,
        }
    if not isinstance(expected_version, str) or not expected_version.strip():
        return {
            "success": False,
            "status": "HOLD_EXACT_VERSION_REQUIRED",
            "tool": "Z3_muZ",
            "executable": exe,
            "python_module_available": module_available,
            "expected_version": expected_version,
            "exact_version_bound": False,
            "authority_granted": False,
        }
    observed = None
    if module_available:
        try:
            import z3  # type: ignore
            observed = str(z3.get_version_string())
        except Exception:
            observed = None
    if observed is None:
        return {
            "success": False,
            "status": "HOLD_VERSION_UNRESOLVED",
            "tool": "Z3_muZ",
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
        "tool": "Z3_muZ",
        "executable": exe,
        "python_module_available": module_available,
        "expected_version": expected_version.strip(),
        "observed_version": observed,
        "exact_version_bound": match,
        "authority_granted": False,
    }


def normalize_fixedpoint_result(result: Any, *, query_scope: str) -> Dict[str, Any]:
    """Preserve native three-valued solver state without epistemic promotion."""
    if not isinstance(query_scope, str) or not query_scope.strip():
        return {"success": False, "status": "ILL_TYPED_SCOPE", "authority_granted": False}
    token = str(result).strip().upper()
    if token not in NATIVE_RESULTS:
        return {
            "success": False,
            "status": "ILL_TYPED_SOLVER_RESULT",
            "observed": token,
            "authority_granted": False,
        }
    return {
        "success": True,
        "status": "SOLVER_RESULT_PRESERVED",
        "solver_result": token,
        "query_scope": query_scope.strip(),
        "epistemic_class": "EXTERNAL_FORMAL_SOLVER_RESULT",
        "empirical_truth": "NOT_ESTABLISHED",
        "causal_inference": "NOT_ESTABLISHED",
        "canon_promoted": False,
        "authority_granted": False,
    }
