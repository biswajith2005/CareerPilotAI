import json

from google import genai

from config.settings import GEMINI_API_KEY, GEMINI_MODEL
from config.prompts import RESUME_ANALYSIS_PROMPT


class AIService:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate_response(self, prompt: str) -> str:
        try:
            response = self.client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
            )
            return response.text
        except Exception as e:
            message = str(e)
            if "503" in message:
                raise RuntimeError(
                    "Gemini is currently experiencing high demand. Please try again in a few moments."
                )
            raise RuntimeError(message)

    def analyze_resume(self, resume_text: str) -> dict:

        prompt = RESUME_ANALYSIS_PROMPT.format(
            resume=resume_text
        )

        response = self.generate_response(prompt)

        response = response.replace("```json", "")
        response = response.replace("```", "").strip()

        return json.loads(response)


ai_service = AIService()