"""Executable bounded AMOS URK/Core-19 repair runtime.

Origin architect / steward: Trang Phan.

This module is an AMOS_MODEL reference implementation for the repaired bounded
Core-19 substrate. It does not promote canon and does not claim complete ULK
fragment implementations. Current fragment execution status is delegated to the
evidence-bound ULK execution registry so this snapshot cannot become a second
stale status owner.

Mathematical type firewall:
- an indexed coordinate/data field is not automatically an algebraic tensor;
- structural adjacency is not point-set topology or causality;
- a named invariant or governance rule is not a theorem merely by declaration.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from itertools import product
from typing import Dict, Iterator, Mapping, Optional, Tuple

ACTIVE_AMOS_CORE_BASELINE = "v4.4"
CANONICAL_ULK_VERSION = "2.1.0"
REPAIR_SPEC_DATE = "2026-09-14"
REPAIR_STATUS = "ACTIVE_REPAIR_SPEC/AMOS_MODEL"


class Core19(Enum):
    P01_EXISTENCE = 1
    P02_COMPETING = 2
    P03_CAUSALITY = 3
    P04_TEMPORAL = 4
    P05_INFORMATIONAL = 5
    P06_TOPOLOGICAL = 6
    P07_IDENTITY = 7
    P08_CONVERGENCE = 8
    P09_DIVERGENCE = 9
    P10_PARADOX = 10
    P11_POSITIVE_LOGIC = 11
    P12_NEGATIVE_LOGIC = 12
    P13_ZERO_LOGIC = 13
    P14_DUAL_LOGIC = 14
    P15_MULTI_LOGIC = 15
    P16_META_LOGIC = 16
    P17_SUPRA_LOGIC = 17
    P18_ANTI_LOGIC = 18
    P19_NULL_LOGIC = 19


class P02Candidate(Enum):
    NON_EXISTENCE = "NonExistence"
    DISTINCTION = "Distinction"


@dataclass(frozen=True)
class P02Binding:
    namespace: str
    version: str
    candidate: Optional[P02Candidate] = None

    @property
    def resolved(self) -> bool:
        return self.candidate is not None


class P02BindingRegistry:
    """Namespace/version-local P02 bindings; no global winner exists by default."""

    def __init__(self, bindings: Optional[Mapping[Tuple[str, str], P02Candidate]] = None):
        self._bindings: Dict[Tuple[str, str], P02Candidate] = dict(bindings or {})

    def bind(self, namespace: str, version: str, candidate: P02Candidate) -> None:
        key = _binding_key(namespace, version)
        existing = self._bindings.get(key)
        if existing is not None and existing is not candidate:
            raise ValueError(f"conflicting P02 binding for {key}: {existing.value} vs {candidate.value}")
        self._bindings[key] = candidate

    def resolve(self, namespace: str, version: str) -> P02Binding:
        key = _binding_key(namespace, version)
        return P02Binding(key[0], key[1], self._bindings.get(key))


def _binding_key(namespace: str, version: str) -> Tuple[str, str]:
    namespace = namespace.strip()
    version = version.strip()
    if not namespace or not version:
        raise ValueError("P02 binding requires non-empty namespace and version")
    return namespace, version


@dataclass(frozen=True)
class Truth4:
    """Four-valued evidence pair: support for truth and support for falsity."""

    supports_true: bool
    supports_false: bool

    def neg(self) -> "Truth4":
        return Truth4(self.supports_false, self.supports_true)

    def join_information(self, other: "Truth4") -> "Truth4":
        return Truth4(
            self.supports_true or other.supports_true,
            self.supports_false or other.supports_false,
        )

    def leq_information(self, other: "Truth4") -> bool:
        return (
            (not self.supports_true or other.supports_true)
            and (not self.supports_false or other.supports_false)
        )

    @property
    def is_paradox(self) -> bool:
        return self.supports_true and self.supports_false

    @property
    def is_null(self) -> bool:
        return not self.supports_true and not self.supports_false


TRUTH4_NEITHER = Truth4(False, False)
TRUTH4_TRUE_ONLY = Truth4(True, False)
TRUTH4_FALSE_ONLY = Truth4(False, True)
TRUTH4_BOTH = Truth4(True, True)
TRUTH4_DOMAIN = (TRUTH4_NEITHER, TRUTH4_TRUE_ONLY, TRUTH4_FALSE_ONLY, TRUTH4_BOTH)


class UnaryKind(Enum):
    ATOM = "atom"
    NOT = "not"
    NLOGIC = "nlogic"


@dataclass(frozen=True)
class UnaryExpr:
    kind: UnaryKind
    atom_id: Optional[str] = None
    child: Optional["UnaryExpr"] = None

    def __post_init__(self) -> None:
        if self.kind is UnaryKind.ATOM:
            if not self.atom_id or self.child is not None:
                raise ValueError("ATOM requires atom_id and no child")
        else:
            if self.child is None or self.atom_id is not None:
                raise ValueError(f"{self.kind.value} requires one child and no atom_id")

    @staticmethod
    def atom(name: str) -> "UnaryExpr":
        name = name.strip()
        if not name:
            raise ValueError("atom name must be non-empty")
        return UnaryExpr(UnaryKind.ATOM, atom_id=name)

    @staticmethod
    def not_(child: "UnaryExpr") -> "UnaryExpr":
        return UnaryExpr(UnaryKind.NOT, child=child)

    @staticmethod
    def nlogic(child: "UnaryExpr") -> "UnaryExpr":
        return UnaryExpr(UnaryKind.NLOGIC, child=child)


def _toggle_not(expr: UnaryExpr) -> UnaryExpr:
    if expr.kind is UnaryKind.NOT:
        assert expr.child is not None
        return expr.child
    return UnaryExpr.not_(expr)


def normalize_unary(expr: UnaryExpr) -> UnaryExpr:
    """Normalize the repaired bounded NOT/NLOGIC fragment.

    Rewrite precedence is intentional:
      1. NLOGIC(NLOGIC(x)) reduces before child descent.
      2. Strict subterms are then normalized.
      3. A single NLOGIC toggles normalized truth negation.
    """
    if expr.kind is UnaryKind.ATOM:
        return expr

    assert expr.child is not None
    if expr.kind is UnaryKind.NLOGIC and expr.child.kind is UnaryKind.NLOGIC:
        assert expr.child.child is not None
        return normalize_unary(expr.child.child)

    normalized_child = normalize_unary(expr.child)
    if expr.kind is UnaryKind.NOT:
        return _toggle_not(normalized_child)
    if expr.kind is UnaryKind.NLOGIC:
        return _toggle_not(normalized_child)
    raise AssertionError(f"unhandled unary kind: {expr.kind}")


def unary_depth(expr: UnaryExpr) -> int:
    if expr.kind is UnaryKind.ATOM:
        return 0
    assert expr.child is not None
    return 1 + unary_depth(expr.child)


class CellStatus(Enum):
    UNBOUND = "UNBOUND"
    SOURCE_CLAIM = "SOURCE_CLAIM"
    AMOS_MODEL = "AMOS_MODEL"
    DERIVED = "DERIVED"
    VERIFIED_BOUNDED = "VERIFIED_BOUNDED"
    COMPETING = "COMPETING"
    FALSIFIED = "FALSIFIED"


@dataclass(frozen=True)
class MatrixCell:
    row: Core19
    col: Core19
    status: CellStatus = CellStatus.UNBOUND
    semantic_claim_id: Optional[str] = None
    source_id: Optional[str] = None


def matrix_indices() -> Iterator[Tuple[Core19, Core19]]:
    yield from product(Core19, repeat=2)


def matrix_coordinate_count() -> int:
    return sum(1 for _ in matrix_indices())


@dataclass(frozen=True)
class CoordinateFieldCoordinate:
    """Six-axis coordinate in the URK partial data field.

    This is an indexed coordinate only. It carries no tensor-product,
    multilinearity, scalar-field, covariance/contravariance, or basis semantics.
    """

    row: Core19
    col: Core19
    scale: str
    context: str
    regime: str
    observer: str

    def __post_init__(self) -> None:
        named = {
            "scale": self.scale,
            "context": self.context,
            "regime": self.regime,
            "observer": self.observer,
        }
        for axis, value in named.items():
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{axis} must be an explicit non-empty index")


# Compatibility alias only. Historical callers used TensorCoordinate for an
# indexed field coordinate. The alias does not grant algebraic tensor semantics.
TensorCoordinate = CoordinateFieldCoordinate


@dataclass(frozen=True)
class TensorDeclaration:
    """Evidence references required before algebraic tensor language is admissible.

    The referenced witnesses are claim identities, not proofs by string presence.
    Structural completeness therefore remains AMOS_MODEL metadata until the
    referenced mathematical evidence is independently validated.
    """

    scalar_structure_id: str
    axis_module_structure_ids: Tuple[str, ...]
    multilinearity_witness_id: str
    tensor_product_witness_id: str
    coordinate_basis_witness_id: Optional[str] = None

    def __post_init__(self) -> None:
        fields = (
            self.scalar_structure_id,
            self.multilinearity_witness_id,
            self.tensor_product_witness_id,
        )
        if any(not isinstance(value, str) or not value.strip() for value in fields):
            raise ValueError("tensor declaration requires non-empty structural witness ids")
        if not self.axis_module_structure_ids:
            raise ValueError("tensor declaration requires at least one module/vector-space axis witness")
        if any(not isinstance(value, str) or not value.strip() for value in self.axis_module_structure_ids):
            raise ValueError("tensor axis witness ids must be non-empty")
        if self.coordinate_basis_witness_id is not None and not self.coordinate_basis_witness_id.strip():
            raise ValueError("coordinate basis witness id must be non-empty when supplied")

    def structural_failures(self, *, axis_count: int, coordinates_used: bool) -> Tuple[str, ...]:
        failures = []
        if not isinstance(axis_count, int) or axis_count < 1:
            failures.append("TENSOR_AXIS_COUNT")
        elif len(self.axis_module_structure_ids) != axis_count:
            failures.append("TENSOR_AXIS_MODULE_WITNESS_COUNT")
        if coordinates_used and self.coordinate_basis_witness_id is None:
            failures.append("TENSOR_COORDINATE_BASIS_WITNESS")
        return tuple(failures)


@dataclass(frozen=True)
class TensorStructureReceipt:
    """Receipt for structural tensor declaration checks, not theorem verification."""

    declaration: TensorDeclaration
    axis_count: int
    coordinates_used: bool
    status: str = "STRUCTURALLY_TYPED_AMOS_MODEL"


def bind_tensor_structure(
    declaration: TensorDeclaration,
    *,
    axis_count: int,
    coordinates_used: bool = False,
) -> TensorStructureReceipt:
    failures = declaration.structural_failures(
        axis_count=axis_count,
        coordinates_used=coordinates_used,
    )
    if failures:
        raise ValueError(";".join(failures))
    return TensorStructureReceipt(declaration, axis_count, coordinates_used)


@dataclass(frozen=True)
class StructuralAdjacencyEdge:
    src: Core19
    dst: Core19
    relation_id: str
    status: CellStatus

    def __post_init__(self) -> None:
        if not isinstance(self.relation_id, str) or not self.relation_id.strip():
            raise ValueError("structural adjacency relation_id must be non-empty")


# Compatibility alias only. Historical TopologyEdge meant graph/relation
# adjacency; it is not a point-set topology edge and does not imply causality.
TopologyEdge = StructuralAdjacencyEdge


@dataclass(frozen=True)
class SelectiveInvalidationGate:
    """Governance gate for dependency-based stale propagation.

    This encodes when the AMOS_MODEL invalidation rule may be executed. It is not
    a mathematical axiom that invalid parent claims make descendants false.
    """

    dependency_orientation_bound: bool
    state_epoch_bound: bool
    closure_algorithm_bound: bool
    validation_receipt_bound: bool

    def enforceable(self) -> bool:
        return all(
            (
                self.dependency_orientation_bound,
                self.state_epoch_bound,
                self.closure_algorithm_bound,
                self.validation_receipt_bound,
            )
        )


class LogicFragment(Enum):
    CLASSICAL_PROPOSITIONAL = "ClassicalPropositional"
    FIRST_ORDER_UNIFICATION = "FirstOrderUnification"
    TEMPORAL_LTL = "TemporalLTL"
    EPISTEMIC_MODAL = "EpistemicModal"
    NON_MONOTONIC_DUNG = "NonMonotonicDung"
    DEPENDENT_TYPE = "DependentType"
    QUANTUM_LOGIC = "QuantumLogic"
    CATEGORICAL_TOPOS = "CategoricalTopos"


class ImplementationStatus(Enum):
    EXECUTABLE_BOUNDED = "EXECUTABLE_BOUNDED"
    EXECUTABLE_BOUNDED_CANDIDATE_REBOUND = "EXECUTABLE_BOUNDED_CANDIDATE_REBOUND"
    CANONICAL_BOUNDED_CLAIM_REBIND_PENDING = "CANONICAL_BOUNDED_CLAIM_REBIND_PENDING"
    SPECIFICATION_ONLY = "SPECIFICATION_ONLY"


def implementation_status(fragment: LogicFragment) -> ImplementationStatus:
    """Project current status from the single ULK execution-evidence owner."""
    from ulk_fragment_execution_registry import Fragment, execution_binding

    current = execution_binding(Fragment(fragment.value)).status.value
    return ImplementationStatus(current)


@dataclass(frozen=True)
class PromotionEvidence:
    source_resolved: bool
    semantics_typed: bool
    assumptions_bound: bool
    equations_checked: bool
    counterexamples_checked: bool
    implementation_receipt: bool
    canon_authority: bool

    def promotable(self) -> bool:
        return all(
            (
                self.source_resolved,
                self.semantics_typed,
                self.assumptions_bound,
                self.equations_checked,
                self.counterexamples_checked,
                self.implementation_receipt,
                self.canon_authority,
            )
        )


def validate_runtime_invariants() -> Tuple[str, ...]:
    """Return bounded invariant failures. Empty tuple means these checks passed."""
    failures = []

    if len(Core19) != 19:
        failures.append("CORE19_COUNT")
    if matrix_coordinate_count() != 361:
        failures.append("MATRIX_COORDINATE_COUNT")

    for value in TRUTH4_DOMAIN:
        if value.neg().neg() != value:
            failures.append("TRUTH4_NEGATION_INVOLUTION")
            break

    atom = UnaryExpr.atom("x")
    probes = [
        atom,
        UnaryExpr.not_(atom),
        UnaryExpr.nlogic(atom),
        UnaryExpr.nlogic(UnaryExpr.nlogic(atom)),
        UnaryExpr.not_(UnaryExpr.nlogic(UnaryExpr.not_(atom))),
    ]
    for probe in probes:
        normalized = normalize_unary(probe)
        if normalize_unary(normalized) != normalized:
            failures.append("NORMALIZE_IDEMPOTENCE")
            break
        if normalize_unary(UnaryExpr.nlogic(UnaryExpr.nlogic(probe))) != normalized:
            failures.append("NLOGIC_INVOLUTION")
            break

    probe_coord = CoordinateFieldCoordinate(
        Core19.P01_EXISTENCE,
        Core19.P03_CAUSALITY,
        "H",
        "ctx",
        "normal",
        "obs",
    )
    if not isinstance(probe_coord, CoordinateFieldCoordinate):
        failures.append("COORDINATE_FIELD_IDENTITY")

    gate = SelectiveInvalidationGate(True, True, True, True)
    if not gate.enforceable():
        failures.append("SELECTIVE_INVALIDATION_GATE")

    return tuple(dict.fromkeys(failures))
