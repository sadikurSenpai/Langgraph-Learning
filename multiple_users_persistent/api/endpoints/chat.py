from fastapi import APIRouter
router = APIRouter()

import uuid

from api.schemas.chat_schema import ChatSchema
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from api.schemas.chat_state import ChatState
from langgraph.checkpoint.memory import InMemorySaver
from services.nodes.chat import chat

graph = StateGraph(ChatState)
checkpointer = InMemorySaver()

graph.add_node('chat', chat)

graph.add_edge(START, 'chat')
graph.add_edge('chat', END)



@router.post('/chat', tags=['Chat'], response_model=dict)
def chat(request: ChatSchema):
    thread_id = request.thread_id
    if not thread_id:
        thread_id = str(uuid.uuid4())
    config = {
        'configurable': {
            'thread_id': thread_id
        }
    }
    workflow = graph.compile(checkpointer=checkpointer)
    user_message = HumanMessage(content=request.msg)
    result = workflow.invoke({
        'messages': [user_message]
    }, config=config)

    last_ai_message = next(
        msg for msg in reversed(result["messages"])
        if isinstance(msg, AIMessage)
    )

    return {
        'thread_id': thread_id,
        'msg': last_ai_message.content
    }