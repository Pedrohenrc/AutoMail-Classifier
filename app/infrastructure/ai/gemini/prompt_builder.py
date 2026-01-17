from app.domain.value_objects.classification import Classification
from app.infrastructure.ai.gemini.gemini_prompts import (
    PRODUCTIVE_RESPONSE_PROMPT,
    UNPRODUCTIVE_RESPONSE_PROMPT,
)

class GeminiPromptBuilder:

    @staticmethod
    def build(email_content: str, classification: Classification) -> str:
        if classification == Classification.PRODUTIVO:
            return PRODUCTIVE_RESPONSE_PROMPT.format(email=email_content)

        return UNPRODUCTIVE_RESPONSE_PROMPT.format(email=email_content)
