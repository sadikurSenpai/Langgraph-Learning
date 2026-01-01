from typing import TypedDict, Annotated
from operator import add

class ItemsWithoutReducer(TypedDict):
    items : list[str]


class ItemsWithReducer(TypedDict):
    items : Annotated[list[str], add]