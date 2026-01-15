from abc import ABC, abstractmethod
from app.domain.entities.email import Email
from app.domain.value_objects.classification import Classification


class AIResponder(ABC):

    @abstractmethod
    def generate_response(
        self,
        email: Email,
        classification: Classification
    ) -> str:
        """
        Gera uma resposta automática para o email com base
        na sua classificação.
        """
        pass
