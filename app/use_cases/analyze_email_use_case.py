from dataclasses import dataclass

from app.domain.entities.email import Email
from app.domain.value_objects.classification import Classification
from app.ports.ai_classifier import AIClassifier
from app.ports.ai_response import AIResponder


@dataclass
class AnalyzeEmailResult:
    classification: Classification
    suggested_response: str


class AnalyzeEmailUseCase:
    def __init__(
        self,
        classifier: AIClassifier,
        responder: AIResponder
    ):
        self.classifier = classifier
        self.responder = responder

    def execute(self, email_text: str) -> AnalyzeEmailResult:
        email = Email(content=email_text)

        classification = self.classifier.classify(
            email.normalized_content()
        )

        response = self.responder.generate_response(
            email=email,
            classification=classification
        )

        return AnalyzeEmailResult(
            classification=classification,
            suggested_response=response
        )
