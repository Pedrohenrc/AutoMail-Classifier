from io import BytesIO
from typing import BinaryIO
from app.ports.file_reader.base_reader import BaseFileReader

try:
    from pypdf import PdfReader as PyPdfReader
    from pypdf.errors import PdfReadError
except ImportError:
    PyPdfReader = None
    PdfReadError = None


class PdfReader(BaseFileReader):
    def __init__(self):
        if PyPdfReader is None:
            raise RuntimeError(
                "pypdf não está instalado. Execute: pip install pypdf"
            )

    def can_read(self, filename: str) -> bool:
        return filename.lower().endswith(".pdf")

    def read(self, file: bytes) -> str:
        try:
            reader = PyPdfReader(BytesIO(file)) 

            text_parts = []
            for page in reader.pages:
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

        except PdfReadError as e:
            raise ValueError(
                f"Erro ao ler PDF: arquivo corrompido ou inválido - {str(e)}"
            )

        except Exception as e:
            raise ValueError(
                f"Erro inesperado ao processar PDF: {str(e)}"
            )
