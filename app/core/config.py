from pydantic import BaseModel


class AppMetadata(BaseModel):
    project_name: str = "chatbot-soporte-tecnico-ia"
    version: str = "0.1.0"
    academic_mode: bool = True
