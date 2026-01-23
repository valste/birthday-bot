from datetime import date, timedelta
from typing import Any

from googleapiclient.discovery import Resource #python -m pip install google-auth google-auth-oauthlib google-auth-httplib2


def get_calendar_id_by_name(service: Resource, calendar_name: str) -> str:
    """
    Find a calendarId by its display name (summary), e.g. "My Birthdays".
    Python 3.12 typing and style.
    """
    page_token: str | None = None
    while True:
        resp: dict[str, Any] = service.calendarList().list(pageToken=page_token).execute()
        for cal in resp.get("items", []):
            if cal.get("summary") == calendar_name:
                return cal["id"]
        page_token = resp.get("nextPageToken")
        if not page_token:
            break
    raise ValueError(f'Calendar named "{calendar_name}" not found in calendarList.')


def create_my_birthdays_entry(
    service: Resource,
    *,
    calendar_name: str = "My Birthdays",
    person_name: str = "Maxim Stenske",
    event_date: date = date(2026, 1, 3),  # the next occurrence you want to create
    born_on: str = "03.01.2014",
    email: str = "maxim.stenske@gmail.com",
    relation: str = "son",
    hobbies: str = "soccer",
    greeting_style: str = "with love and proudness",
    # For all-day events, reminders are "minutes before midnight at start date".
    # "1 day before at 09:00" ≈ 15 hours before midnight => 900 minutes.
    reminder_minutes: int = 900,
) -> dict[str, Any]:
    """
    Creates an all-day, yearly repeating birthday event in the "My Birthdays" calendar.

    Matches your screenshot intent:
      - Title: "Birthday - <Name>"
      - All-day: event_date (end is exclusive)
      - Repeat: yearly
      - Availability: Free (transparent)
      - Reminder: approx "1 day before at 09:00" for an all-day event
      - Description: your custom fields
    """
    calendar_id = get_calendar_id_by_name(service, calendar_name)

    description = (
        f"born on: {born_on}\n"
        f"email: {email}\n"
        f"relation: {relation}\n"
        f"hobbies: {hobbies}\n"
        f"Style of the greeting message: {greeting_style}"
    )

    event_body: dict[str, Any] = {
        "summary": f"Birthday - {person_name}",
        "description": description,
        "start": {"date": event_date.isoformat()},  # all-day
        "end": {"date": (event_date + timedelta(days=1)).isoformat()},  # exclusive end date
        "recurrence": ["RRULE:FREQ=YEARLY"],
        "transparency": "transparent",  # doesn't block time ("Verfügbar")
        "visibility": "default",
        "reminders": {
            "useDefault": False,
            "overrides": [{"method": "popup", "minutes": reminder_minutes}],
        },
    }

    return service.events().insert(calendarId=calendar_id, body=event_body).execute()


# Example (assuming you already built an authenticated Calendar API service):
# created = create_my_birthdays_entry(service)
# print(created.get("htmlLink"))
