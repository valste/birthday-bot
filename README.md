# Birthday Bot

Local-first birthday greeting generator using Google Calendar, Gmail drafts, and Drive history with Ollama default and OpenAI optional.

## Highlights
- Read structured birthday events from Google Calendar and validate required metadata.
- Generate localized greetings through a provider interface (Ollama by default; OpenAI selectable).
- Prevent repeats by comparing against `greetings_history.json` stored on Google Drive and cached locally.
- Save Gmail drafts with a `birthday` label for manual review/forwarding on the day.
- Run day-before jobs via APScheduler; optional FastAPI/CLI hooks for manual runs.

## Quickstart
1) Install Python 3.11+ and create a virtualenv.
2) `pip install -r requirements.txt`
3) Copy `.env.example` to `.env` and fill Google creds, Drive file id, and LLM provider settings.
4) Place Google OAuth `credentials.json` in the project root; first run will complete the installed-app flow.
5) Run `python -m bot.main --once` to generate immediately or `python -m bot.main --schedule` to start the scheduler.
