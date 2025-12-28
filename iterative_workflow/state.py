from typing import TypedDict, Literal

class TweetState(TypedDict):
    topic: str
    tweet: str
    evaluation: Literal['approved', 'needs_improvement']
    feedback: str
    iter: int
    max_iter: int