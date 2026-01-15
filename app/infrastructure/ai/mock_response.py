from app.ports.ai_response import AIResponder
from app.domain.entities.email import Email
from app.domain.value_objects.classification import Classification


class MockResponder(AIResponder):

    def generate_response(
        self,
        email: Email,
        classification: Classification
    ) -> str:

        if classification == Classification.PRODUTIVO:
            return (
                "Olá!\n\n"
                "Recebemos sua solicitação e ela será analisada pela nossa equipe. "
                "Em breve retornaremos com uma atualização.\n\n"
                "Atenciosamente,\n"
                "Equipe de Suporte"
            )

        return (
            "Olá!\n\n"
            "Agradecemos sua mensagem.\n\n"
            "Atenciosamente,\n"
            "Equipe"
        )
