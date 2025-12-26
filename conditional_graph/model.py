from pydantic import BaseModel, Field
from typing import Literal

class Sentiment(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="The sentiment of a review")

class DiagnosisSchema(BaseModel):
    issue_type: Literal["UX", "Performance", "Bug", "Support", "Other"] = Field(description='The category of issue mentioned in the review')
    tone: Literal["angry", "frustrated", "disappointed", "calm"] = Field(description='The emotional tone expressed by the user')
    urgency: Literal["low", "medium", "high"] = Field(description='How urgent or critical the issue appears to be')