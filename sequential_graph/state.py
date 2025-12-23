from typing import TypedDict

class BMIState(TypedDict):
    height: float
    weight: float
    bmi: float
    category: str


class LLM_QA(TypedDict):
    question: str
    answer: str


class BlogState(TypedDict):
    topic: str
    outline: str
    blog: str
    score: int