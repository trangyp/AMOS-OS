"""Typed URK coordinate-field and structural-adjacency reference runtime.

Origin architect / steward: Trang Phan.

Bounded AMOS_MODEL implementation. The canonical runtime objects here are an
indexed partial coordinate/data field and a structural adjacency relation store.
Neither object is automatically an algebraic tensor, point-set topology, causal
graph, or logical entailment relation. Historical tensor/topology names remain as
compatibility aliases only.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Generic, Optional, Tuple, TypeVar

from core19_runtime import (
    CellStatus,
    CoordinateFieldCoordinate,
    Core19,
    StructuralAdjacencyEdge,
    matrix_indices,
)

T = TypeVar("T")


class CoordinateConflictError(ValueError):
    pass


@dataclass(frozen=True)
class CoordinateFieldEntry(Generic[T]):
    coordinate: CoordinateFieldCoordinate
    value: T
    status: CellStatus
    source_id: Optional[str] = None


class URKCoordinateFieldStore(Generic[T]):
    """Sparse partial field over Core19 x Core19 x scale x context x regime x observer.

    Sparse storage is intentional: absence means UNBOUND, not zero or false.
    Coordinates are immutable once bound unless the exact same entry is replayed.
    The storage shape alone supplies no algebraic tensor semantics.
    """

    def __init__(self) -> None:
        self._entries: Dict[CoordinateFieldCoordinate, CoordinateFieldEntry[T]] = {}

    def bind(self, entry: CoordinateFieldEntry[T]) -> None:
        previous = self._entries.get(entry.coordinate)
        if previous is not None and previous != entry:
            raise CoordinateConflictError(f"coordinate already bound: {entry.coordinate}")
        self._entries[entry.coordinate] = entry

    def get(self, coordinate: CoordinateFieldCoordinate) -> Optional[CoordinateFieldEntry[T]]:
        return self._entries.get(coordinate)

    def status(self, coordinate: CoordinateFieldCoordinate) -> CellStatus:
        entry = self.get(coordinate)
        return CellStatus.UNBOUND if entry is None else entry.status

    def __len__(self) -> int:
        return len(self._entries)

    def entries(self) -> Tuple[CoordinateFieldEntry[T], ...]:
        return tuple(
            self._entries[key]
            for key in sorted(
                self._entries,
                key=lambda c: (
                    c.row.value,
                    c.col.value,
                    c.scale,
                    c.context,
                    c.regime,
                    c.observer,
                ),
            )
        )


# Historical compatibility names. These aliases deliberately do not create a
# TensorDeclaration or tensor-product witness.
TensorEntry = CoordinateFieldEntry
URKTensorStore = URKCoordinateFieldStore


@dataclass(frozen=True)
class StructuralAdjacencyCell:
    row: Core19
    col: Core19
    edge: StructuralAdjacencyEdge

    def __post_init__(self) -> None:
        if self.edge.src is not self.row or self.edge.dst is not self.col:
            raise ValueError("structural adjacency endpoints must equal matrix coordinate")


class StructuralAdjacencyStore:
    """Sparse 19x19 typed relation field.

    Coordinate presence means a typed relation has been bound. It does not imply
    causality, point-set openness, metric distance, reachability, or a proven
    semantic law. Derived graph properties require separate algorithms/evidence.
    """

    def __init__(self) -> None:
        self._cells: Dict[Tuple[Core19, Core19], StructuralAdjacencyCell] = {}

    def bind(self, cell: StructuralAdjacencyCell) -> None:
        key = (cell.row, cell.col)
        previous = self._cells.get(key)
        if previous is not None and previous != cell:
            raise CoordinateConflictError(
                f"structural adjacency coordinate already bound: {cell.row.name},{cell.col.name}"
            )
        self._cells[key] = cell

    def get(self, row: Core19, col: Core19) -> Optional[StructuralAdjacencyCell]:
        return self._cells.get((row, col))

    def status(self, row: Core19, col: Core19) -> CellStatus:
        cell = self.get(row, col)
        return CellStatus.UNBOUND if cell is None else cell.edge.status

    def populated_count(self) -> int:
        return len(self._cells)

    @staticmethod
    def coordinate_count() -> int:
        return sum(1 for _ in matrix_indices())

    def unbound_count(self) -> int:
        return self.coordinate_count() - self.populated_count()

    def populated_cells(self) -> Tuple[StructuralAdjacencyCell, ...]:
        return tuple(
            self._cells[key]
            for key in sorted(self._cells, key=lambda p: (p[0].value, p[1].value))
        )


# Historical compatibility names. A TopologyMatrixStore is structurally an
# adjacency store only; actual point-set topology belongs to finite_topology_runtime.py.
TopologyCell = StructuralAdjacencyCell
TopologyMatrixStore = StructuralAdjacencyStore


def validate_coordinate_topology_invariants() -> Tuple[str, ...]:
    failures = []
    coordinates = tuple(matrix_indices())
    if len(coordinates) != 361:
        failures.append("CORE19_PAIR_COORDINATE_COUNT")
    if len(set(coordinates)) != 361:
        failures.append("CORE19_PAIR_COORDINATE_UNIQUENESS")

    base = (Core19.P01_EXISTENCE, Core19.P02_COMPETING)
    a = CoordinateFieldCoordinate(*base, "H", "ctx", "r", "obs")
    b = CoordinateFieldCoordinate(*base, "M", "ctx", "r", "obs")
    c = CoordinateFieldCoordinate(*base, "H", "ctx2", "r", "obs")
    d = CoordinateFieldCoordinate(*base, "H", "ctx", "r2", "obs")
    e = CoordinateFieldCoordinate(*base, "H", "ctx", "r", "obs2")
    if len({a, b, c, d, e}) != 5:
        failures.append("COORDINATE_AXIS_IDENTITY")

    matrix = StructuralAdjacencyStore()
    if matrix.coordinate_count() != 361 or matrix.unbound_count() != 361:
        failures.append("STRUCTURAL_ADJACENCY_PARTIAL_SEMANTICS")

    if URKTensorStore is not URKCoordinateFieldStore:
        failures.append("LEGACY_TENSOR_ALIAS_DRIFT")
    if TopologyMatrixStore is not StructuralAdjacencyStore:
        failures.append("LEGACY_TOPOLOGY_ALIAS_DRIFT")

    return tuple(failures)


# Backward-compatible function name. The canonical semantics are coordinate
# field + structural adjacency; this alias must not be cited as tensor/topology proof.
validate_tensor_topology_invariants = validate_coordinate_topology_invariants
