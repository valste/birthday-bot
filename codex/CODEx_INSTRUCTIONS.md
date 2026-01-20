# Codex Instructions

## Repository Intent
This repo contains a local-first birthday greeting agent. Keep the solution simple and reliable; avoid premature abstractions.

## Default Stack
- Python 3.11+
- APScheduler (daily job)
- Google APIs: Calendar, Gmail, Drive
- LLM provider: Ollama default, OpenAI optional

## Configuration
- `.env` for runtime settings (see `.env.example`).
- Google OAuth `credentials.json` stored at repo root.
- Tokens cached under `.tokens/` (gitignored).

## LLM Provider Selection
- `LLM_PROVIDER=ollama` is default. Use `OLLAMA_BASE_URL`.
- If `LLM_PROVIDER=openai`, require `OPENAI_API_KEY`.

## Behavior Requirements
- Generate greetings the day before the birthday.
- Only create Gmail drafts; do not auto-send.
- Use `greetings_history.json` on Drive to avoid repeating the last 3 years.
- Keep prompts concise and include prior greetings to avoid duplication.

## File Ownership
- Core logic lives under `src/bot/`.
- Integration stubs in `calendar.py`, `gmail.py`, `drive.py` should be implemented before adding new modules.

## Coding Style
- Keep functions small and testable.
- Prefer explicit validation of required metadata.
- Add only minimal comments when logic is not obvious.

## Safety
- If any external API fails, log and skip rather than failing the whole run.
- Never send email automatically.
