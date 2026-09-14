"""Machine-checkable execution ownership for the 12 Cognitive Matrix planes.

Origin architect / steward: Trang Phan.

Registry coverage means each plane has a bounded executable owner and regression
surface where one exists. It does NOT mean every artifact or domain semantic in
that plane is implemented, validated, authorized, canonical, or production-ready.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Mapping, Tuple


class PlaneStatus(Enum):
    BOUNDED_REFERENCE = "BOUNDED_REFERENCE"
    BOUNDED_PARTIAL = "BOUNDED_PARTIAL"
    BOUNDED_GENERATOR_GUARDED = "BOUNDED_GENERATOR_GUARDED"


@dataclass(frozen=True)
class PlaneBinding:
    plane_id: str
    name: str
    executor_paths: Tuple[str, ...]
    test_paths: Tuple[str, ...]
    status: PlaneStatus
    semantic_completion: bool = False
    canon_authority: bool = False
    effect_authority: bool = False

    def __post_init__(self) -> None:
        if not self.plane_id.strip() or not self.name.strip():
            raise ValueError("plane identity must be explicit")
        if not self.executor_paths or not self.test_paths:
            raise ValueError("plane binding requires executor and regression paths")
        for paths, label in ((self.executor_paths, "executor"), (self.test_paths, "test")):
            if any(not path.strip() for path in paths):
                raise ValueError(f"{label} paths must be non-empty")
            if len(set(paths)) != len(paths):
                raise ValueError(f"{label} paths must be unique")
        if self.semantic_completion:
            raise ValueError("registry binding may not claim full semantic completion")
        if self.canon_authority or self.effect_authority:
            raise ValueError("execution registry may not mint canon/effect authority")


_REF = "04_RUNTIME/01_REFERENCE_IMPLEMENTATION/"

PLANE_BINDINGS: Mapping[str, PlaneBinding] = {
    "01_PRIMITIVES": PlaneBinding(
        "01_PRIMITIVES",
        "Primitives L00-L29",
        (_REF + "primitive_contract_runtime.py",),
        (_REF + "test_primitive_contract_runtime.py",),
        PlaneStatus.BOUNDED_PARTIAL,
    ),
    "02_LIFECYCLE_OPERATIONS": PlaneBinding(
        "02_LIFECYCLE_OPERATIONS",
        "Lifecycle operations O00-O16",
        (_REF + "lifecycle_operation_runtime.py",),
        (_REF + "test_lifecycle_operation_runtime.py",),
        PlaneStatus.BOUNDED_PARTIAL,
    ),
    "03_CONTROL_PLANES": PlaneBinding(
        "03_CONTROL_PLANES",
        "Control planes C01-C09",
        (
            _REF + "control_plane_execution_registry.py",
            "10_MEMORY/memory_lifecycle_runtime.py",
        ),
        (
            _REF + "test_control_plane_execution_registry.py",
            "10_MEMORY/test_memory_lifecycle_runtime.py",
        ),
        PlaneStatus.BOUNDED_REFERENCE,
    ),
    "04_SCALES": PlaneBinding(
        "04_SCALES",
        "H-M-L scales",
        (_REF + "scale_contract_runtime.py",),
        (_REF + "test_scale_contract_runtime.py",),
        PlaneStatus.BOUNDED_PARTIAL,
    ),
    "05_CELL_REGISTRY": PlaneBinding(
        "05_CELL_REGISTRY",
        "Cell registry",
        (_REF + "matrix_registry_runtime.py",),
        (_REF + "test_matrix_registry_runtime.py",),
        PlaneStatus.BOUNDED_REFERENCE,
    ),
    "06_CELL_CONTRACTS": PlaneBinding(
        "06_CELL_CONTRACTS",
        "Cell contracts",
        (_REF + "cognitive_matrix_contract_runtime.py",),
        (_REF + "test_cognitive_matrix_contract_runtime.py",),
        PlaneStatus.BOUNDED_PARTIAL,
    ),
    "07_COVERAGE": PlaneBinding(
        "07_COVERAGE",
        "Coverage",
        (_REF + "cognitive_matrix_runtime.py",),
        (_REF + "test_cognitive_matrix_runtime.py",),
        PlaneStatus.BOUNDED_REFERENCE,
    ),
    "08_STRUCTURAL_GAPS": PlaneBinding(
        "08_STRUCTURAL_GAPS",
        "Structural gaps",
        (
            _REF + "cognitive_matrix_runtime.py",
            _REF + "cognitive_matrix_contract_runtime.py",
        ),
        (
            _REF + "test_cognitive_matrix_runtime.py",
            _REF + "test_cognitive_matrix_contract_runtime.py",
        ),
        PlaneStatus.BOUNDED_REFERENCE,
    ),
    "09_DEPENDENCY_GRAPH": PlaneBinding(
        "09_DEPENDENCY_GRAPH",
        "Dependency graph",
        (
            _REF + "cognitive_matrix_runtime.py",
            _REF + "cognitive_matrix_contract_runtime.py",
        ),
        (
            _REF + "test_cognitive_matrix_runtime.py",
            _REF + "test_cognitive_matrix_contract_runtime.py",
        ),
        PlaneStatus.BOUNDED_REFERENCE,
    ),
    "10_ROUTING": PlaneBinding(
        "10_ROUTING",
        "Routing",
        (_REF + "cognitive_matrix_runtime.py",),
        (_REF + "test_cognitive_matrix_runtime.py",),
        PlaneStatus.BOUNDED_PARTIAL,
    ),
    "11_VALIDATION": PlaneBinding(
        "11_VALIDATION",
        "Validation and promotion gates",
        (
            _REF + "cognitive_matrix_runtime.py",
            _REF + "cognitive_matrix_contract_runtime.py",
        ),
        (
            _REF + "test_cognitive_matrix_runtime.py",
            _REF + "test_cognitive_matrix_contract_runtime.py",
        ),
        PlaneStatus.BOUNDED_PARTIAL,
    ),
    "12_GENERATORS": PlaneBinding(
        "12_GENERATORS",
        "Governed generators",
        ("25_COGNITIVE_MATRIX/12_GENERATORS/fill_matrix.py",),
        (_REF + "test_cognitive_matrix_generator_guard.py",),
        PlaneStatus.BOUNDED_GENERATOR_GUARDED,
    ),
}

EXPECTED_PLANES = tuple(f"{index:02d}_" for index in range(1, 13))


def validate_plane_registry(repo_root: Path) -> Tuple[str, ...]:
    failures = []
    if len(PLANE_BINDINGS) != 12:
        failures.append("PLANE_COUNT")

    prefixes = tuple(sorted(key[:3] for key in PLANE_BINDINGS))
    expected = tuple(f"{index:02d}_" for index in range(1, 13))
    if prefixes != expected:
        failures.append("PLANE_ID_SEQUENCE")

    for plane_id, binding in PLANE_BINDINGS.items():
        if plane_id != binding.plane_id:
            failures.append(f"PLANE_ID_MISMATCH:{plane_id}")
        if binding.semantic_completion:
            failures.append(f"SEMANTIC_COMPLETION_OVERCLAIM:{plane_id}")
        if binding.canon_authority:
            failures.append(f"CANON_AUTHORITY_OVERCLAIM:{plane_id}")
        if binding.effect_authority:
            failures.append(f"EFFECT_AUTHORITY_OVERCLAIM:{plane_id}")
        for path in binding.executor_paths:
            if not (repo_root / path).is_file():
                failures.append(f"MISSING_EXECUTOR:{plane_id}:{path}")
        for path in binding.test_paths:
            if not (repo_root / path).is_file():
                failures.append(f"MISSING_TEST:{plane_id}:{path}")

    return tuple(failures)


def execution_coverage() -> Tuple[int, int, int]:
    """Return declared planes, planes with executors, planes with tests."""
    declared = len(PLANE_BINDINGS)
    with_executor = sum(bool(binding.executor_paths) for binding in PLANE_BINDINGS.values())
    with_tests = sum(bool(binding.test_paths) for binding in PLANE_BINDINGS.values())
    return declared, with_executor, with_tests
