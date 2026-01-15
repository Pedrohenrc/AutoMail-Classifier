from enum import Enum


class Classification(Enum):
    PRODUTIVO = "produtivo"
    IMPRODUTIVO = "improdutivo"

    @classmethod
    def from_string(cls, value: str) -> "Classification":
        try:
            return cls(value.lower())
        except ValueError:
            raise ValueError(f"Invalid classification: {value}")