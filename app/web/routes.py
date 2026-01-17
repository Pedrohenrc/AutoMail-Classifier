from fastapi import APIRouter, Form, HTTPException, UploadFile, File, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from typing import Optional

from app.infrastructure.exceptions.ai_unavaliable_exception import AIUnavailableException
from app.use_cases.analyze_email_use_case import AnalyzeEmailUseCase
from app.infrastructure.ai.gemini.gemini_classifier import GeminiClassifier
from app.infrastructure.ai.gemini.gemini_response import GeminiResponse
from app.infrastructure.file_reader.file_reader_factory import FileReaderFactory

templates = Jinja2Templates(directory="app/web/templates")

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):

    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/")
async def analyze_email(
    email_text: Optional[str] = Form(None),
    email_file: Optional[UploadFile] = File(None)
):  
    try:
        content = await _extract_email_content(email_text, email_file)
        
        if not content or not content.strip():
            raise HTTPException(
                status_code=400,
                detail="Por favor, forneça um email para análise (texto ou arquivo)."
            )
        
        use_case = AnalyzeEmailUseCase(
            classifier=GeminiClassifier(),
            responder=GeminiResponse()
        )
        
        result = use_case.execute(content)
        
        return JSONResponse(
            status_code=200,
            content={
                "classification": result.classification.value,
                "suggested_response": result.suggested_response
            }
        )
    
    except AIUnavailableException as e:
        raise HTTPException(
            status_code=503,
            detail=f"Serviço de IA temporariamente indisponível: {str(e)}"
        )
    
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro inesperado: {str(e)}"
        )


async def _extract_email_content(
    email_text: Optional[str],
    email_file: Optional[UploadFile]
) -> str:
    if email_file and email_file.filename:
        factory = FileReaderFactory()
        
        try:
            content = factory.read_file(
                filename=email_file.filename,
                file=email_file.file
            )
            return content
            
        except ValueError as e:
            raise ValueError(str(e))
        
        finally:
            await email_file.close()
    
    elif email_text:
        return email_text.strip()
    else: 
        raise ValueError("Forneça um email (texto ou arquivo) para análise.")