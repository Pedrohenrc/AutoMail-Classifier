from typing import BinaryIO
from app.ports.file_reader.base_reader import BaseFileReader

try:
    import PyPDF2
except ImportError:
    PyPDF2 = None


class PdfReader(BaseFileReader):
    def __init__(self):
        if PyPDF2 is None:
            raise RuntimeError(
                "PyPDF2 não está instalado. "
                "Execute: pip install PyPDF2"
            )
    
    def can_read(self, filename: str) -> bool:
        """Verifica se o arquivo é .pdf"""
        return filename.lower().endswith('.pdf')
    
    def read(self, file: BinaryIO) -> str:
        try:
            pdf_reader = PyPDF2.PdfReader(file)
            
            text_parts = []
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)
            
            full_text = "\n".join(text_parts)
            
            if not full_text.strip():
                raise ValueError(
                    "O PDF não contém texto extraível. "
                    "Pode ser um PDF escaneado (imagem)."
                )
            
            return full_text
            
        except PyPDF2.errors.PdfReadError as e:
            raise ValueError(f"Erro ao ler PDF: arquivo corrompido ou inválido - {str(e)}")
        except Exception as e:
            raise ValueError(f"Erro inesperado ao processar PDF: {str(e)}")