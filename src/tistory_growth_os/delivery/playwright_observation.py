from dataclasses import dataclass, field
from datetime import datetime

from ..domain.ids import MediaId
from .playwright_saved_reservation import SavedReservationSnapshot
from .reservation_readback import (
    ReservationContent, ReservationMedia, ReservationObservation, ReservationTarget, SavedVisibility,
)


@dataclass(frozen=True, slots=True)
class UploadedAsset:
    asset_id: MediaId
    source_url: str = field(repr=False)
    filename: str


def reservation_observation(
    snapshot: SavedReservationSnapshot,
    uploads: tuple[UploadedAsset, ...],
    observed_at: datetime,
) -> ReservationObservation | None:
    if (len(uploads) != 4 or len({item.asset_id for item in uploads}) != 4
            or len({item.source_url for item in uploads}) != 4
            or any(not item.asset_id.strip() or not item.filename.strip() for item in uploads)
            or len(snapshot.content.media) != 4
            or snapshot.settings.scheduled_at is None
            or not 0 <= snapshot.representative_index < 4):
        return None
    mapped: list[ReservationMedia] = []
    for image in snapshot.content.media:
        matches = tuple(item for item in uploads
                        if item.source_url == image.source_url and item.filename == image.filename)
        if len(matches) != 1:
            return None
        mapped.append(ReservationMedia(matches[0].asset_id, image.alt))
    content = ReservationContent(
        snapshot.content.title, snapshot.content.body_sha256, tuple(mapped),
        mapped[snapshot.representative_index].asset_id, snapshot.manager.category,
        snapshot.settings.home_topic, tuple(sorted(snapshot.tags.tags)),
    )
    identity = snapshot.manager.post_id
    target = ReservationTarget(identity, f'https://nedamma.tistory.com/{identity}',
                               snapshot.settings.scheduled_at, content)
    return ReservationObservation(target, SavedVisibility.SCHEDULED, observed_at)
