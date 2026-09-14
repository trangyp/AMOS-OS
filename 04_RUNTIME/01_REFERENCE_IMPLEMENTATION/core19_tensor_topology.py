"""Typed URK tensor and Core-19 topology-matrix reference runtime.

Origin architect / steward: Trang Phan.

Bounded AMOS_MODEL implementation. This module enforces coordinate identity and
partial semantics; it does not claim that all 361 Core-19 pair coordinates have
known semantics and it does not infer causality from topology.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Generic, Optional, Tuple, TypeVar

from core19_runtime import CellStatus, Core19, TensorCoordinate, TopologyEdge, matrix_indices

T = TypeVar("T")


class CoordinateConflictError(ValueError):
    pass


@dataclass(frozen=True)
class TensorEntry(Generic[T]):
    coordinate: TensorCoordinate
    value: T
    status: CellStatus
    source_id: Optional[str] = None


class URKTensorStore(Generic[T]):
    """Sparse typed tensor over Core19 x Core19 x scale x context x regime.

    Sparse storage is intentional: absence means UNBOUND, not zero or false.
    Coordinates are immutable once bound unless the exact same entry is replayed.
    """

    def __init__(self) -> None:
        self._entries: Dict[TensorCoordinate, TensorEntry[T]] = {}

    def bind(self, entry: TensorEntry[T]) -> None:
        previous = self._entries.get(entry.coordinate)
        if previous is not None and previous != entry:
            raise CoordinateConflictError(f"tensor coordinate already bound: {entry.coordinate}")
        self._entries[entry.coordinate] = entry

    def get(self, coordinate: TensorCoordinate) -> Optional[TensorEntry[T]]:
        return self._entries.get(coordinate)

    def status(self, coordinate: TensorCoordinate) -> CellStatus:
        entry = self.get(coordinate)
        return CellStatus.UNBOUND if entry is None else entry.status

    def __len__(self) -> int:
        return len(self._entries)

    def entries(self) -> Tuple[TensorEntry[T], ...]:
        return tuple(
            self._entries[key]
            for key in sorted(
                self._entries,
                key=lambda c: (c.row.value, c.col.value, c.scale, c.context, c.regime),
            )
        )


@dataclass(frozen=True)
class TopologyCell:
    row: Core19
    col: Core19
    edge: TopologyEdge

    def __post_init__(self) -> None:
        if self.edge.src is not self.row or self.edge.dst is not self.col:
            raise ValueError("topology edge endpoints must equal matrix coordinate")


class TopologyMatrixStore:
    """Sparse 19x19 typed relation field.

    Coordinate presence means a typed relation has been bound. It does not imply
    causality, openness, metric distance, or a proven semantic law.
    """

    def __init__(self) -> None:
        self._cells: Dict[Tuple[Core19, Core19], TopologyCell] = {}

    def bind(self, cell: TopologyCell) -> None:
        key = (cell.row, cell.col)
        previous = self._cells.get(key)
        if previous is not None and previous != cell:
            raise CoordinateConflictError(f"topology coordinate already bound: {cell.row.name},{cell.col.name}")
        self._cells[key] = cell

    def get(self, row: Core19, col: Core19) -> Optional[TopologyCell]:
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

    def populated_cells(self) -> Tuple[TopologyCell, ...]:
        return tuple(self._cells[key] for key in sorted(self._cells, key=lambda p: (p[0].value, p[1].value)))


def validate_tensor_topology_invariants() -> Tuple[str, ...]:
    failures = []
    coordinates = tuple(matrix_indices())
    if len(coordinates) != 361:
        failures.append("CORE19_PAIR_COORDINATE_COUNT")
    if len(set(coordinates)) != 361:
        failures.append("CORE19_PAIR_COORDINATE_UNIQUENESS")

    a = TensorCoordinate(Core19.P01_EXISTENCE, Core19.P02_COMPETING, "H", "ctx", "r")
    b = TensorCoordinate(Core19.P01_EXISTENCE, Core19.P02_COMPETING, "M", "ctx", "r")
    c = TensorCoordinate(Core19.P01_EXISTENCE, Core19.P02_COMPETING, "H", "ctx2", "r")
    d = TensorCoordinate(Core19.P01_EXISTENCE, Core19.P02_COMPETING, "H", "ctx", "r2")
    if len({a, b, c, d}) != 4:
        failures.append("TENSOR_AXIS_IDENTITY")

    matrix = TopologyMatrixStore()
    if matrix.coordinate_count() != 361 or matrix.unbound_count() != 361:
        failures.append("TOPOLOGY_PARTIAL_SEMANTICS")

    return tuple(failures)
