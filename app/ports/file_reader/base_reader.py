from abc import ABC, abstractmethod
from typing import BinaryIO


class BaseFileReader(ABC):
    """
    Interface abstrata para leitores de arquivo.
    
    Permite adicionar novos formatos (DOCX, EML, etc.) 
    sem modificar o código existente (Open/Closed Principle).
    """
    
    @abstractmethod
    def can_read(self, filename: str) -> bool:
        """
        Verifica se este leitor suporta o arquivo.
        
        Args:
            filename: Nome do arquivo
            
        Returns:
            True se o leitor suporta este formato
        """
        pass
    
    @abstractmethod
    def read(self, file: BinaryIO) -> str:
        """
        Lê o conteúdo do arquivo e retorna como texto.
        
        Args:
            file: Arquivo binário para leitura
            
        Returns:
            Conteúdo do arquivo como string
            
        Raises:
            ValueError: Se o arquivo não puder ser lido
        """
        pass