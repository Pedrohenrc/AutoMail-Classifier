from typing import BinaryIO
from app.ports.file_reader.base_reader import BaseFileReader


class TxtReader(BaseFileReader):
    def can_read(self, filename: str) -> bool:
        return filename.lower().endswith('.txt')
    
    def read(self, file: BinaryIO) -> str:
        try:
            content_bytes = file.read()

            try:
                return content_bytes.decode('utf-8')
            except UnicodeDecodeError:
                return content_bytes.decode('latin-1')
                
        except Exception as e:
            raise ValueError(f"Erro ao ler arquivo TXT: {str(e)}")