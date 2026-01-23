# Birthday Bot PRD (TZ)

## Overview
A local-first birthday agent that reads structured birthday events from Google Calendar, generates personalized greetings with an LLM, and saves the result as a Gmail inbox message (UNREAD) labeled `birthday` for manual review and forwarding on the actual birthday. Greetings are generated the day before the birthday. A Drive-hosted `greetings_history.json` is used to prevent repetition over the last three years.

## Goals
- Automatically find upcoming birthdays from a designated Google Calendar.
- Generate a localized, relationship-aware greeting using structured metadata in the event description.
- Insert a Gmail inbox message (UNREAD) the day before the birthday and label it `birthday`.
- Store and compare greetings in `greetings_history.json` on Google Drive to avoid repeats (3-year window).
- Run locally with minimal dependencies and support Ollama by default, OpenAI optional.

## Non-Goals
- Automatic sending of emails on the birthday (user forwards manually).
- Full CRM or contact management system.
- Multichannel delivery beyond email.

## Users
- Single user (owner) who wants automated, reviewable birthday greetings.

## Event Metadata Contract
Calendar event description must contain:
- born on: DD.MM.YYYY
- email: user@example.com
- language: e.g., german
- relationship: e.g., son
- hobbies: e.g., soccer
- style of the greeting message: e.g., playfully, with love and proudness

## Functional Requirements
- Poll Calendar daily for birthdays occurring the next day.
- Parse description metadata; validate required keys.
- Build a prompt that includes:
  - Metadata
  - Prior greetings (last 3 years) for the same person
  - Instruction to avoid repetition
- Generate greeting with LLM (Ollama default, OpenAI optional).
- Insert Gmail message into INBOX:
  - Subject: dynamic (e.g., "It is your birthday today, Maxim!")
  - Body: greeting only
  - Label: `birthday`
  - From and to are the user (self-addressed)
- Update `greetings_history.json` in Drive and local cache.

## Non-Functional Requirements
- Local-first; no server deployment required.
- Deterministic scheduling and time zone awareness.
- Reasonable latency per greeting (<= 10s per message under normal conditions).
- Safe failure behavior: log and skip, do not send.

## Data Model
`greetings_history.json`:
{
  "Full Name": [
    {"DD.MM.YYYY": "Greeting text"},
    {"DD.MM.YYYY": "Greeting text"}
  ]
}

## Integrations
- Google Calendar API: read events.
- Gmail API: insert message into INBOX + label.
- Google Drive API: read/write history file.
- LLM: Ollama local HTTP API; OpenAI if configured.

## Scheduling and Time Zones (TZ)
- Default job runs at 06:00 local time.
- Birthday detection uses local calendar timezone and generates day-before.
- If timezone metadata is missing, assume system local timezone.

## Risks
- Missing or malformed metadata leads to skipped greetings.
- OAuth token expiry or API quota limits.
- History file drift if Drive sync fails.

## Acceptance Criteria
- When a calendar event has valid metadata and the birthday is tomorrow, an unread inbox message labeled `birthday` appears in Gmail with a personalized greeting.
- Greeting differs from the last 3 years for the same person.
- `greetings_history.json` is updated on Drive and cached locally.
