from fastapi import APIRouter, Form, HTTPException
from fastapi.responses import HTMLResponse
from app.infrastructure.exceptions.ai_unavaliable_exception import AIUnavailableException
from app.use_cases.analyze_email_use_case import AnalyzeEmailUseCase
from app.infrastructure.ai.openai_classifier import OpenAIClassifier
from app.infrastructure.ai.openai_response import OpenAIResponse

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def index():
    return """
    <html>
        <body>
            <h2>Classificador de Emails</h2>
            <form method="post">
                <textarea name="email_text" rows="10" cols="60"></textarea><br><br>
                <button type="submit">Analisar</button>
            </form>
        </body>
    </html>
    """


@router.post("/", response_class=HTMLResponse)
def analyze_email(email_text: str = Form(...)):
    use_case = AnalyzeEmailUseCase(
        classifier=OpenAIClassifier(),
        responder=OpenAIResponse()
    )
    try:
        result = use_case.execute(email_text)
        return f"""
        <html>
            <body>
                <h2>Resultado</h2>
                <p><strong>Classificação:</strong> {result.classification.value}</p>
                <p><strong>Resposta sugerida:</strong></p>
                <pre>{result.suggested_response}</pre>
                <br>
                <a href="/">Voltar</a>
            </body>
        </html>
        """
    except AIUnavailableException:
        raise HTTPException(
            status_code=503,
            detail="Serviço de IA temporariamente indisponível"
        )
