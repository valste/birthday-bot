from datetime import datetime, timedelta
from typing import Any


def parse_event_metadata(description: str) -> dict[str, str]:
    metadata: dict[str, str] = {}
    for line in description.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip().lower()] = value.strip()
    return metadata


def fetch_upcoming_birthdays(service: Any, calendar_id: str, *, now: datetime | None = None) -> list[dict[str, Any]]:
    now = now or datetime.now(datetime.timezone.utc)
    window_start = now
    window_end = now + timedelta(days=2)
    # Placeholder: replace with google calendar API call
    _ = (service, calendar_id, window_start, window_end)
    return []
