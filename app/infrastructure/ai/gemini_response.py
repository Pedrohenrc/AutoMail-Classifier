import google.generativeai as genai
from google.api_core import exceptions
from app.ports.ai_response import AIResponse
from app.domain.entities.email import Email
from app.domain.value_objects.classification import Classification
from app.core.config import settings

class GeminiResponse(AIResponse):
    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(
            model_name=settings.GEMINI_MODEL,
            system_instruction="Você é um assistente de atendimento corporativo focado em eficiência e cordialidade."
        )

    def generate_response(
        self,
        email: Email,
        classification: Classification
    ) -> str:
        
        if classification == Classification.PRODUTIVO:
            contexto = (
                "Este é um email PRODUTIVO. Gere uma resposta educada, profissional e objetiva, "
                "confirmando o recebimento e informando que a solicitação será analisada pela equipe técnica."
            )
        else:
            contexto = (
                "Este é um email IMPRODUTIVO (SPAM ou irrelevante). Gere uma resposta muito curta, "
                "educada e cordial, apenas agradecendo o contato, sem prometer ações futuras ou análises."
            )

        prompt = (
            f"Instrução específica: {contexto}\n\n"
            "Conteúdo do email recebido:\n"
            "---"
            f"{email.content}"
            "---"
            "\n\nEscreva a resposta final diretamente, sem comentários adicionais:"
        )

        try:
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.4,
                    top_p=0.95,
                    max_output_tokens=256,
                )
            )

            if not response.text:
                return "Obrigado pelo seu contato."

            return response.text.strip()

        except exceptions.ResourceExhausted:
            raise Exception("Limite de cota do Gemini atingido durante a geração da resposta.")
        except Exception as e:
            raise Exception(f"Falha na geração de resposta com Gemini: {str(e)}")