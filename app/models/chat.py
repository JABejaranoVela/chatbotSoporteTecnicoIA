from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, description="User message to process.")


class ChatResponse(BaseModel):
    answer: str
    category: str
    matched: bool
    normalized_message: str
    source: str
