from pydantic import Field, BaseModel

class Evaluate(BaseModel):
    feedback: str = Field(description='Detailed feedbackfor the essay')
    score: int = Field(description='Score out of 10', ge=0, le=10)