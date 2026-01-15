from app.ports.ai_classifier import AIClassifier
from app.domain.value_objects.classification import Classification


class MockClassifier(AIClassifier):

    def classify(self, email_text: str) -> Classification:
        text = email_text.lower()

        productive_keywords = [
            "status",
            "chamado",
            "suporte",
            "erro",
            "problema",
            "solicito",
            "atualização",
            "atualizacao",
            "dúvida",
            "duvida"
        ]

        for keyword in productive_keywords:
            if keyword in text:
                return Classification.PRODUTIVO

        return Classification.IMPRODUTIVO
