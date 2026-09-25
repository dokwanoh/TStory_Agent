from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
from typing import Final, TypedDict

from .contracts.json_decode import JsonDecodeError, parse_json
from .learning_snapshot import Snapshot, decode_snapshot

MAX_BYTES: Final = 1_000_000


class Advisory(TypedDict):
    status: str
    production_applied: bool
    comparison_eligible: bool
    input_sha256: str
    calendar_day: str
    source: str
    surface: str
    timezone: str
    header_updated_at_display: str
    detail_exact_update_time: str | None
    observed_lead_titles: list[str]
    next_action: str
    limitations: list[str]


def advise(snapshot: Snapshot, digest: str) -> Advisory:
    limitations = list(snapshot.limitations)
    limitations.extend([
        "post_ids_unjoined", "unequal_post_age", "calendar_day_not_first_seven_days",
        "aggregate_channels_not_post_attribution", "descriptive_not_causal_or_forecast",
    ])
    if not snapshot.interval_complete:
        limitations.append("partial_day")
    if snapshot.truncated:
        limitations.append("truncated_table_absent_rows_unknown")
    if snapshot.detail_cutoff is None:
        limitations.append("detail_cutoff_unknown_header_not_substitute")
    highest = max((row.views for row in snapshot.rows), default=0)
    leads = [row.title for row in snapshot.rows if row.views == highest and highest > 0]
    return Advisory(
        status="descriptive_only", production_applied=False, comparison_eligible=False,
        input_sha256=digest, calendar_day=snapshot.day.isoformat(), source="tistory",
        surface="https://nedamma.tistory.com/manage/statistics/blog", timezone="Asia/Seoul",
        header_updated_at_display=snapshot.header_updated_at_display,
        detail_exact_update_time=snapshot.detail_cutoff,
        observed_lead_titles=leads,
        next_action=(
            "표시된 조회수가 가장 많은 글의 독자 질문을 후속 조사 참고로만 사용하세요. "
            + "새 이슈·원문·기존 글과의 차별성을 확인하고, 실제 선정에는 자동 반영하지 않습니다."
            if leads else "관측된 양수 조회 행이 없어 참고 후보를 제안하지 않습니다."
        ),
        limitations=limitations,
    )


class Arguments(argparse.Namespace):
    snapshot: Path = Path()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Private, read-only Tistory snapshot advisory; never invokes production. "
        + "Output contains private titles; keep stdout local, outside public logs/Git.",
    )
    _ = parser.add_argument("snapshot", type=Path)
    args = parser.parse_args(namespace=Arguments())
    try:
        with args.snapshot.open("rb") as stream:
            raw = stream.read(MAX_BYTES + 1)
        if len(raw) > MAX_BYTES:
            print(json.dumps({"status": "unavailable", "reason": "input_too_large", "production_applied": False}))
            return 2
        snapshot = decode_snapshot(parse_json(raw))
    except (OSError, JsonDecodeError, RecursionError):
        print(json.dumps({"status": "unavailable", "reason": "input_unavailable_or_invalid", "production_applied": False}))
        return 2
    print(json.dumps(advise(snapshot, sha256(raw).hexdigest()), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
