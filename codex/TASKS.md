# Tasks

## Milestone 1: Google API Integration
- [ ] Implement OAuth flow for Calendar/Gmail/Drive.
- [ ] Read calendar events for next-day birthdays.
- [ ] Parse and validate metadata (required fields).

## Milestone 2: LLM and Prompting
- [ ] Implement provider interface selection (Ollama/OpenAI).
- [ ] Build prompt with metadata and prior greetings.
- [ ] Enforce difference from previous 3 years.

## Milestone 3: Gmail Drafts
- [ ] Create draft email with subject and body.
- [ ] Ensure label `birthday` exists and apply it.

## Milestone 4: History Sync
- [ ] Download `greetings_history.json` from Drive to cache.
- [ ] Update history with new greeting and upload back.

## Milestone 5: Scheduling and CLI
- [ ] Implement daily scheduler (day-before at 06:00 local time).
- [ ] Provide `--once` and `--schedule` CLI paths.

## Milestone 6: Tests and Hardening
- [ ] Unit tests for metadata parsing and prompt building.
- [ ] Integration test stubs for Google API calls (mocked).
- [ ] Logging and error handling for skipped events.
