import google.generativeai as genai
from google.api_core import exceptions
from app.interfaces.ai_classifier import AIClassifier
from app.domain.classification import Classification
from app.core.config import GEMINI_API_KEY, GEMINI_MODEL

class GeminiClassifier(AIClassifier):

    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel(GEMINI_MODEL)

    def classify(self, email_text: str) -> Classification:
        try:
            prompt = (
                "Você é um classificador de emails corporativos especializado em triagem de produtividade.\n"
                "Sua tarefa é analisar o conteúdo do email e decidir se ele é 'produtivo' ou 'improdutivo'.\n\n"
                "Definições:\n"
                "- produtivo: Emails que contêm tarefas, decisões, solicitações de trabalho, feedback relevante ou informações cruciais.\n"
                "- improdutivo: SPAM, notificações automáticas irrelevantes, conversas paralelas sem objetivo de trabalho ou correntes.\n\n"
                "Regras restritas:\n"
                "1. Responda APENAS com uma das palavras: 'produtivo' ou 'improdutivo'.\n"
                "2. Não inclua pontuação, explicações ou saudações.\n\n"
                f"Email para análise:\n'''{email_text}'''"
            )

            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0,
                )
            )

            raw_result = response.text.strip().lower()
            
            return Classification.from_string(raw_result)

        except exceptions.ResourceExhausted:
            raise Exception("Limite de cota do Gemini atingido.")
        except exceptions.ServiceUnavailable:
            raise Exception("O serviço do Gemini está temporariamente fora do ar.")
        except Exception as e:
            raise Exception(f"Erro inesperado na classificação: {str(e)}")