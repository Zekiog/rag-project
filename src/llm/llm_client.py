import os

from openai import OpenAI

class LLMClient:
    def __init__(self, model: str = "gpt-4o-mini", temperature: float = 0.2):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model
        self.temperature = temperature

    def complete(self, prompt: str) -> str:
        resp = self.client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            messages=[{"role": "user", "content": prompt}])
        return resp.choices[0].message.content
