from dataclasses import dataclass


@dataclass(frozen=True)
class Email:
    content: str

    def __post_init__(self):
        if not self.content or not self.content.strip():
            raise ValueError("Email content cannot be empty.")

    def normalized_content(self):
        return self.content.strip()