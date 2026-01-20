from typing import Protocol


class LLMProvider(Protocol):
    async def generate(self, prompt: str, language: str | None = None) -> str:  # pragma: no cover - interface only
        ...


def build_prompt(metadata: dict[str, str], history_snippets: list[str]) -> str:
    parts = [
        "You are a warm birthday greeter.",
        "Compose a short, personalized email body only.",
        "Use the provided language and relationship for tone.",
        "Avoid repeating previous greetings; keep it fresh.",
    ]
    if history_snippets:
        parts.append("Recent greetings to avoid repeating:")
        parts.extend(history_snippets)
    parts.append(f"Metadata: {metadata}")
    return "\n".join(parts)
