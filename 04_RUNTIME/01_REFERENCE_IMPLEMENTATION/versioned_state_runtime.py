"""Bounded in-memory MVCC/CAS state substrate for AMOS OS.

Origin architect / steward: Trang Phan.

This is a deterministic single-process reference implementation for versioned
state transitions. It is not a distributed consensus system, durable database,
or external-effect executor.

Hard boundaries:
- PROPOSAL != COMMIT
- CAS_OK iff EXPECTED_VERSION == CURRENT_VERSION
- SNAPSHOT_READ != CURRENT_STATE
- INTERNAL_STATE_COMMIT != EXTERNAL_EFFECT_AUTHORIZATION
- LOCAL_ATOMICITY != DISTRIBUTED_CONSENSUS
- TEST_PASS != PRODUCTION_DURABILITY
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Mapping, Optional, Tuple


@dataclass(frozen=True)
class EpochVector:
    state_epoch: int
    causal_epoch: int
    policy_epoch: int
    provenance_epoch: int

    def __post_init__(self) -> None:
        for value in (
            self.state_epoch,
            self.causal_epoch,
            self.policy_epoch,
            self.provenance_epoch,
        ):
            if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                raise ValueError("epochs must be non-negative integers")


@dataclass(frozen=True)
class VersionedValue:
    value: object
    version: int

    def __post_init__(self) -> None:
        if not isinstance(self.version, int) or isinstance(self.version, bool) or self.version < 0:
            raise ValueError("version must be a non-negative integer")


@dataclass(frozen=True)
class StateSnapshot:
    values: Mapping[str, VersionedValue]
    epochs: EpochVector


@dataclass(frozen=True)
class WriteIntent:
    key: str
    expected_version: int
    new_value: object

    def __post_init__(self) -> None:
        if not self.key.strip():
            raise ValueError("write key must be explicit")
        if not isinstance(self.expected_version, int) or isinstance(self.expected_version, bool) or self.expected_version < 0:
            raise ValueError("expected_version must be a non-negative integer")


@dataclass(frozen=True)
class StateTransaction:
    transaction_id: str
    read_versions: Mapping[str, int]
    writes: Tuple[WriteIntent, ...]
    expected_epochs: EpochVector
    external_effects: bool = False

    def __post_init__(self) -> None:
        if not self.transaction_id.strip():
            raise ValueError("transaction_id must be explicit")
        if not self.writes:
            raise ValueError("transaction requires at least one write")
        write_keys = [intent.key for intent in self.writes]
        if len(set(write_keys)) != len(write_keys):
            raise ValueError("transaction write keys must be unique")
        for key, version in self.read_versions.items():
            if not key.strip():
                raise ValueError("read key must be explicit")
            if not isinstance(version, int) or isinstance(version, bool) or version < 0:
                raise ValueError("read versions must be non-negative integers")


class CommitStatus(Enum):
    COMMITTED = "COMMITTED"
    CONFLICT = "CONFLICT"
    EXTERNAL_AUTHORITY_REQUIRED = "EXTERNAL_AUTHORITY_REQUIRED"
    EPOCH_MISMATCH = "EPOCH_MISMATCH"


@dataclass(frozen=True)
class CommitReceipt:
    transaction_id: str
    status: CommitStatus
    versions_after: Mapping[str, int]
    reason: str


class MVCCStateStore:
    """Single-process reference store with atomic transaction preflight.

    All validation is completed before any write is applied. A conflicting
    transaction therefore produces no partial writes in this reference model.
    """

    def __init__(self, initial: Optional[Mapping[str, object]] = None, *, epochs: Optional[EpochVector] = None) -> None:
        self._state: Dict[str, VersionedValue] = {}
        for key, value in (initial or {}).items():
            if not key.strip():
                raise ValueError("state key must be explicit")
            self._state[key] = VersionedValue(value, 0)
        self._epochs = epochs or EpochVector(0, 0, 0, 0)
        self._receipts: Dict[str, Tuple[StateTransaction, CommitReceipt]] = {}

    @property
    def epochs(self) -> EpochVector:
        return self._epochs

    def get(self, key: str) -> VersionedValue:
        return self._state[key]

    def snapshot(self, keys: Optional[Tuple[str, ...]] = None) -> StateSnapshot:
        selected = tuple(sorted(self._state)) if keys is None else keys
        if len(set(selected)) != len(selected):
            raise ValueError("snapshot keys must be unique")
        values = {key: self._state[key] for key in selected}
        return StateSnapshot(values, self._epochs)

    def compare_and_swap(self, key: str, expected_version: int, new_value: object) -> bool:
        current = self._state.get(key)
        if current is None:
            if expected_version != 0:
                return False
            self._state[key] = VersionedValue(new_value, 1)
        else:
            if current.version != expected_version:
                return False
            self._state[key] = VersionedValue(new_value, current.version + 1)
        self._epochs = EpochVector(
            self._epochs.state_epoch + 1,
            self._epochs.causal_epoch,
            self._epochs.policy_epoch,
            self._epochs.provenance_epoch,
        )
        return True

    def validate_read_set(self, read_versions: Mapping[str, int]) -> Tuple[str, ...]:
        conflicts = []
        for key, expected in sorted(read_versions.items()):
            current = self._state.get(key)
            actual = 0 if current is None else current.version
            if actual != expected:
                conflicts.append(key)
        return tuple(conflicts)

    def _epoch_matches(self, expected: EpochVector) -> bool:
        return expected == self._epochs

    def commit(self, transaction: StateTransaction) -> CommitReceipt:
        prior = self._receipts.get(transaction.transaction_id)
        if prior is not None:
            prior_tx, prior_receipt = prior
            if prior_tx != transaction:
                raise ValueError("transaction_id reuse with different payload")
            return prior_receipt

        if transaction.external_effects:
            receipt = CommitReceipt(
                transaction.transaction_id,
                CommitStatus.EXTERNAL_AUTHORITY_REQUIRED,
                {key: value.version for key, value in self._state.items()},
                "external effects require a separate authority/effect commit runtime",
            )
            self._receipts[transaction.transaction_id] = (transaction, receipt)
            return receipt

        if not self._epoch_matches(transaction.expected_epochs):
            receipt = CommitReceipt(
                transaction.transaction_id,
                CommitStatus.EPOCH_MISMATCH,
                {key: value.version for key, value in self._state.items()},
                "expected epoch vector does not match current epoch vector",
            )
            self._receipts[transaction.transaction_id] = (transaction, receipt)
            return receipt

        conflicts = set(self.validate_read_set(transaction.read_versions))
        for intent in transaction.writes:
            current = self._state.get(intent.key)
            actual = 0 if current is None else current.version
            if actual != intent.expected_version:
                conflicts.add(intent.key)

        if conflicts:
            receipt = CommitReceipt(
                transaction.transaction_id,
                CommitStatus.CONFLICT,
                {key: value.version for key, value in self._state.items()},
                "version conflict: " + ",".join(sorted(conflicts)),
            )
            self._receipts[transaction.transaction_id] = (transaction, receipt)
            return receipt

        # Atomic in this single-threaded reference: validation above completes
        # before the first mutation below.
        for intent in transaction.writes:
            current = self._state.get(intent.key)
            next_version = 1 if current is None else current.version + 1
            self._state[intent.key] = VersionedValue(intent.new_value, next_version)

        self._epochs = EpochVector(
            self._epochs.state_epoch + 1,
            self._epochs.causal_epoch,
            self._epochs.policy_epoch,
            self._epochs.provenance_epoch,
        )
        receipt = CommitReceipt(
            transaction.transaction_id,
            CommitStatus.COMMITTED,
            {key: value.version for key, value in self._state.items()},
            "internal state transaction committed after full version/epoch preflight",
        )
        self._receipts[transaction.transaction_id] = (transaction, receipt)
        return receipt

    def advance_nonstate_epochs(
        self,
        *,
        causal_epoch: Optional[int] = None,
        policy_epoch: Optional[int] = None,
        provenance_epoch: Optional[int] = None,
    ) -> EpochVector:
        """Explicitly advance non-state epochs; no implicit equality mapping exists."""
        next_causal = self._epochs.causal_epoch if causal_epoch is None else causal_epoch
        next_policy = self._epochs.policy_epoch if policy_epoch is None else policy_epoch
        next_provenance = self._epochs.provenance_epoch if provenance_epoch is None else provenance_epoch
        if next_causal < self._epochs.causal_epoch or next_policy < self._epochs.policy_epoch or next_provenance < self._epochs.provenance_epoch:
            raise ValueError("epochs may not move backward in this reference runtime")
        self._epochs = EpochVector(
            self._epochs.state_epoch,
            next_causal,
            next_policy,
            next_provenance,
        )
        return self._epochs
