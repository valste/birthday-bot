from collections.abc import Iterable
from openai import OpenAI
from bot.greetings import LLMProvider


class OpenAIProvider(LLMProvider):
    def __init__(self, api_key: str, model: str = "gpt-4o-mini") -> None:
        self.client = OpenAI(api_key=api_key)
        self.model = model

    async def generate(self, prompt: str, language: str | None = None) -> str:
        resp = self.client.responses.create(
            model=self.model,
            input=prompt,
        )
        text_chunks: Iterable[str] = []
        if hasattr(resp, "output"):
            text_chunks = [segment.text for segment in resp.output_text_chunks]
        return "".join(text_chunks)
