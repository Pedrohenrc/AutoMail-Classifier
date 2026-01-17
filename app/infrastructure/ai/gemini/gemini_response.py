import google.generativeai as genai
from google.api_core import exceptions
from app.ports.ai_response import AIResponse
from app.domain.entities.email import Email
from app.domain.value_objects.classification import Classification
from app.infrastructure.exceptions.ai_unavaliable_exception import AIUnavailableException
from app.core.config import settings
from app.infrastructure.ai.gemini.prompt_builder import GeminiPromptBuilder

class GeminiResponse(AIResponse):

    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        
        system_instruction = """Você é um assistente de atendimento corporativo de uma instituição financeira de alto padrão.

            Características da sua comunicação:
            - Tom profissional, cordial e empático
            - Vocabulário técnico quando apropriado
            - Respostas concisas mas completas
            - Sempre mantém formalidade adequada ao setor financeiro
            - Usa linguagem que transmite confiança e competência
            - Evita jargões excessivos ou linguagem rebuscada desnecessária

            Você representa uma marca de excelência em atendimento."""

        self.model = genai.GenerativeModel(
            model_name=settings.GEMINI_MODEL,
            system_instruction=system_instruction
        )
    def generate_response(self, email: Email, classification: Classification) -> str:
        prompt = GeminiPromptBuilder.build(email.content, classification)
        temperature = 0.5 if classification == Classification.PRODUTIVO else 0.3

        try:
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=temperature,
                    top_p=0.95,
                    max_output_tokens=300,
                )
            )
        except exceptions.ResourceExhausted:
            raise AIUnavailableException("Limite de cota do Gemini atingido.")
        except exceptions.ServiceUnavailable:
            raise AIUnavailableException("Serviço do Gemini temporariamente indisponível.")

        if not response or not response.text:
            return self._get_fallback_response(classification)
        
        print(prompt)
        print(response.text)
        return response.text.strip()


    def _get_fallback_response(self, classification: Classification) -> str:
        if classification == Classification.PRODUTIVO:
            return (
                "Prezado(a), agradecemos o seu contato. "
                "Recebemos sua mensagem e nossa equipe já está analisando sua solicitação. "
                "Retornaremos em breve com uma resposta detalhada. "
                "Permanecemos à disposição."
            )
        else:
            return "Obrigado pelo seu contato. Tenha um ótimo dia!"