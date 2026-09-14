"""Machine-checkable execution topology for Cognitive Matrix control planes.

Origin architect / steward: Trang Phan.

This registry records bounded implementation evidence only. It does not promote
any control-plane contract into SOURCE_CANON and does not grant authority.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Tuple


@dataclass(frozen=True)
class ControlPlaneBinding:
    plane: str
    role: str
    implementation_path: str
    test_path: str
    bounded_status: str = "EXECUTABLE_BOUNDED_REFERENCE"
    canon_promoted: bool = False


BINDINGS: Dict[str, ControlPlaneBinding] = {
    "C01": ControlPlaneBinding("C01", "GOVERNANCE", "04_RUNTIME/01_REFERENCE_IMPLEMENTATION/c01_governance_runtime.py", "04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_c01_governance_runtime.py"),
    "C02": ControlPlaneBinding("C02", "METACOGNITIVE", "04_RUNTIME/01_REFERENCE_IMPLEMENTATION/c02_metacognitive_runtime.py", "04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_c02_metacognitive_runtime.py"),
    "C03": ControlPlaneBinding("C03", "EXECUTIVE", "04_RUNTIME/01_REFERENCE_IMPLEMENTATION/c03_executive_runtime.py", "04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_c03_executive_runtime.py"),
    "C04": ControlPlaneBinding("C04", "REASONING", "04_RUNTIME/01_REFERENCE_IMPLEMENTATION/c04_reasoning_runtime.py", "04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_c04_reasoning_runtime.py"),
    "C05": ControlPlaneBinding("C05", "REPRESENTATION", "04_RUNTIME/01_REFERENCE_IMPLEMENTATION/c05_representation_runtime.py", "04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_c05_representation_runtime.py"),
    "C06": ControlPlaneBinding("C06", "MEMORY", "10_MEMORY/memory_lifecycle_runtime.py", "10_MEMORY/test_memory_lifecycle_runtime.py"),
    "C07": ControlPlaneBinding("C07", "PERCEPTION", "04_RUNTIME/01_REFERENCE_IMPLEMENTATION/c07_perception_runtime.py", "04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_c07_perception_runtime.py"),
    "C08": ControlPlaneBinding("C08", "EXECUTION_STAGING", "04_RUNTIME/01_REFERENCE_IMPLEMENTATION/c08_execution_runtime.py", "04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_c08_execution_runtime.py"),
    "C09": ControlPlaneBinding("C09", "KERNEL_CONTROL", "04_RUNTIME/01_REFERENCE_IMPLEMENTATION/c09_kernel_control_runtime.py", "04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_c09_kernel_control_runtime.py"),
}


def validate_control_plane_registry(repo_root: Path | None = None) -> Tuple[str, ...]:
    root = repo_root or Path(__file__).resolve().parents[2]
    failures = []
    expected = tuple(f"C{i:02d}" for i in range(1, 10))
    if tuple(sorted(BINDINGS)) != expected:
        failures.append("CONTROL_PLANE_SET_MISMATCH")
    roles = [binding.role for binding in BINDINGS.values()]
    if len(roles) != len(set(roles)):
        failures.append("CONTROL_PLANE_ROLE_COLLISION")
    for plane, binding in BINDINGS.items():
        if binding.plane != plane:
            failures.append(f"{plane}_IDENTITY_MISMATCH")
        if binding.canon_promoted:
            failures.append(f"{plane}_IMPLEMENTATION_MUST_NOT_SELF_PROMOTE_CANON")
        if binding.bounded_status != "EXECUTABLE_BOUNDED_REFERENCE":
            failures.append(f"{plane}_STATUS_MISMATCH")
        if not (root / binding.implementation_path).is_file():
            failures.append(f"{plane}_IMPLEMENTATION_MISSING")
        if not (root / binding.test_path).is_file():
            failures.append(f"{plane}_TEST_MISSING")
    return tuple(failures)


def coverage_vector(repo_root: Path | None = None) -> Tuple[int, int, int]:
    """Return (declared_planes, implementation_files_present, test_files_present)."""
    root = repo_root or Path(__file__).resolve().parents[2]
    implementations = sum((root / b.implementation_path).is_file() for b in BINDINGS.values())
    tests = sum((root / b.test_path).is_file() for b in BINDINGS.values())
    return (len(BINDINGS), implementations, tests)
