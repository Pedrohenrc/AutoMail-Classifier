from typing import BinaryIO, List
from app.ports.file_reader.base_reader import BaseFileReader
from .txt_reader import TxtReader
from .pdf_reader import PdfReader


class FileReaderFactory:
    
    def __init__(self):
        self._readers: List[BaseFileReader] = []
        self._register_default_readers()
    
    def _register_default_readers(self):
        self._readers.append(TxtReader())
        
        try:
            self._readers.append(PdfReader())
        except RuntimeError:            pass
    
    def register_reader(self, reader: BaseFileReader):
        self._readers.append(reader)
    
    def read_file(self, filename: str, file: BinaryIO) -> str:

        for reader in self._readers:
            if reader.can_read(filename):
                return reader.read(file)
        
        supported_formats = self._get_supported_formats()
        raise ValueError(
            f"Formato não suportado: {filename}. "
            f"Formatos aceitos: {', '.join(supported_formats)}"
        )
    
    def _get_supported_formats(self) -> List[str]:
        formats = []
        if any(isinstance(r, TxtReader) for r in self._readers):
            formats.append('.txt')
        if any(isinstance(r, PdfReader) for r in self._readers):
            formats.append('.pdf')
        return formats