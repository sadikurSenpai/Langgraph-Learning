from typing import Optional
from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    thread_id: Optional[str] = Field(None, description="Thread id to maintain the conversation")
    message: str = Field(description="The message which the user wants to send to LLM")