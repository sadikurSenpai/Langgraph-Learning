from typing import TypedDict, Annotated
import operator
from pydantic import Field

class BattingState(TypedDict):
    runs: int
    balls: int
    fours: int
    six: int
    run_rate: float
    boundary_percentage: float
    boundary_per_ball: float
    summary: str

class EvaluateEssayState(TypedDict):
    essay: str

    dot_feedback: str
    cow_feedback: str
    lol_feedback: str
    individual_scores: Annotated[list[int], operator.add]
    overall_feedback: str
    avg_score: float