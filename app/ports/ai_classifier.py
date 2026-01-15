from abc import ABC, abstractmethod
from app.domain.value_objects.classification import Classification


class AIClassifier(ABC):

    @abstractmethod
    def classify(self, email_text: str) -> Classification:
        """
        Recebe o vindo do email e retorna sua classificação.
        """
        pass
