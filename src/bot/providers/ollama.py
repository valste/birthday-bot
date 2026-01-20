import httpx
from bot.greetings import LLMProvider


class OllamaProvider(LLMProvider):
    def __init__(self, base_url: str, model: str = "llama3:instruct") -> None:
        self.base_url = base_url.rstrip("/")
        self.model = model

    async def generate(self, prompt: str, language: str | None = None) -> str:
        async with httpx.AsyncClient(base_url=self.base_url, timeout=60) as client:
            response = await client.post(
                "/api/generate",
                json={"model": self.model, "prompt": prompt},
            )
            response.raise_for_status()
            data = response.json()
            return data.get("response", "")
