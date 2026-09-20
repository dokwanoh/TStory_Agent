from dataclasses import dataclass
from datetime import datetime
from typing import Protocol, assert_never

from ..domain.ids import PostId
from ..domain.publishing_future import VerificationStatus
from .new_reservation_identity import NewReservationIntent, SavedIdentity, bind_new_reservation
from .reservation_execution import ExecutionResult, ExecutionState
from .reservation_readback import (
    DailySlot, ReservationObservation, ReservationTarget, verify_reservation,
)
from .save_intents import SaveIntentJournal


class NewReservationSurface(Protocol):
    def now(self) -> datetime: ...
    def stopped(self) -> bool: ...
    def authorize(self, request: NewReservationIntent, now: datetime) -> tuple[str, ...]: ...
    def inventory(self) -> frozenset[PostId] | None: ...
    def prepare(self, request: NewReservationIntent) -> None: ...
    def save(self, request: NewReservationIntent) -> SavedIdentity | None: ...
    def readback(self, target: ReservationTarget) -> ReservationObservation | None: ...


@dataclass(frozen=True, slots=True)
class NewReservationResult:
    execution: ExecutionResult
    target: ReservationTarget | None = None


@dataclass(frozen=True, slots=True)
class NewReservationExecutor:
    journal: SaveIntentJournal
    surface: NewReservationSurface

    def run(self, request: NewReservationIntent, *, dry_run: bool = True) -> NewReservationResult:
        if dry_run:
            return NewReservationResult(ExecutionResult(ExecutionState.DRY_RUN))
        reasons = self._gate(request)
        if reasons:
            return NewReservationResult(ExecutionResult(ExecutionState.BLOCKED, reasons))
        slot = DailySlot(request.scheduled_at)
        if not self.journal.claim(slot.key, request.package_digest):
            return NewReservationResult(ExecutionResult(ExecutionState.HELD, ("existing_intent",)))
        prior = self.surface.inventory()
        if prior is None:
            return NewReservationResult(ExecutionResult(ExecutionState.BLOCKED, ("inventory_required",)))
        reasons = self._gate(request)
        if reasons:
            return NewReservationResult(ExecutionResult(ExecutionState.BLOCKED, reasons))
        self.surface.prepare(request)
        reasons = self._gate(request)
        if reasons:
            return NewReservationResult(ExecutionResult(ExecutionState.BLOCKED, reasons))
        saved = self.surface.save(request)
        if saved is None:
            return NewReservationResult(ExecutionResult(ExecutionState.UNKNOWN, ("missing_save_identity",)))
        if saved.post_id in prior:
            return NewReservationResult(ExecutionResult(ExecutionState.MISMATCH, ("identity_preexisting",)))
        target = bind_new_reservation(request, saved, prior)
        observation = self.surface.readback(target)
        check = verify_reservation(target, observation, self.surface.now())
        match check.status:
            case VerificationStatus.VERIFIED:
                execution = ExecutionResult(ExecutionState.VERIFIED)
            case VerificationStatus.MISMATCH:
                execution = ExecutionResult(ExecutionState.MISMATCH, check.mismatches)
            case VerificationStatus.UNKNOWN:
                execution = ExecutionResult(ExecutionState.UNKNOWN, check.mismatches)
            case _:
                assert_never(check.status)
        return NewReservationResult(execution, target)

    def _gate(self, request: NewReservationIntent) -> tuple[str, ...]:
        now = self.surface.now()
        reasons = self._stop_reasons(request, now)
        if reasons:
            return reasons
        reasons = self.surface.authorize(request, now)
        return reasons or self._stop_reasons(request, self.surface.now())

    def _stop_reasons(self, request: NewReservationIntent, now: datetime) -> tuple[str, ...]:
        if self.surface.stopped():
            return ("kill_switch",)
        if now.utcoffset() is None:
            return ("timezone_required",)
        if now >= request.scheduled_at:
            return ("slot_expired",)
        return ()
