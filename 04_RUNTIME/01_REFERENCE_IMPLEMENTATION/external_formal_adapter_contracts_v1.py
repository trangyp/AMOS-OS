"""Fail-closed external formal-tool adapter contracts for AMOS ULK.

Origin architect / steward: Trang Phan.

These adapters discover and fingerprint external tools. They do not claim a
proof/model-check result unless the required executable exists and a caller
provides a separately validated invocation/evidence path.
"""
from __future__ import annotations
import hashlib
import shutil
import subprocess
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional


@dataclass(frozen=True)
class ToolBinding:
    tool: str
    executable: Optional[str]
    observed_version: Optional[str]
    status: str
    license_gate: str
    semantic_scope: str
    authority_granted: bool = False


def _version(executable: str, *args: str) -> Optional[str]:
    try:
        p = subprocess.run([executable, *args], capture_output=True, text=True, timeout=5, check=False)
    except Exception:
        return None
    text = (p.stdout or p.stderr or "").strip()
    return text.splitlines()[0] if text else None


def spot_binding() -> ToolBinding:
    exe = shutil.which("ltl2tgba")
    if not exe:
        return ToolBinding(
            "Spot", None, None, "UNAVAILABLE_HOLD",
            "GPLv3 distribution/linking review required before deployment",
            "future-time LTL/PSL and omega-automata only; no empirical temporal truth",
        )
    return ToolBinding(
        "Spot", exe, _version(exe, "--version"), "DISCOVERED_NOT_PROOF_BOUND",
        "GPLv3 distribution/linking review required before deployment",
        "future-time LTL/PSL and omega-automata only; no empirical temporal truth",
    )


def lean_binding() -> ToolBinding:
    exe = shutil.which("lean")
    if not exe:
        return ToolBinding(
            "Lean4", None, None, "UNAVAILABLE_HOLD", "DEPENDENCY_LOCK_REQUIRED",
            "kernel-checked propositions encoded in the selected Lean environment only",
        )
    return ToolBinding(
        "Lean4", exe, _version(exe, "--version"), "DISCOVERED_NOT_PROOF_BOUND",
        "DEPENDENCY_LOCK_REQUIRED",
        "kernel-checked propositions encoded in the selected Lean environment only",
    )


def file_sha256(path: str) -> str:
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(path)
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def binding_report() -> dict:
    return {"spot": asdict(spot_binding()), "lean4": asdict(lean_binding())}
