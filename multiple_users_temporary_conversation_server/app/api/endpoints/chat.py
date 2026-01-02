from fastapi import APIRouter
from fastapi.responses import JSONResponse, StreamingResponse
from app.api.schemas.chat import ChatRequest
from app.services.states.ChatState import Chat
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage
from app.services.messages.send_message import send_message

import uuid

router = APIRouter()

checkpointer = InMemorySaver()
chatbot = StateGraph(Chat)

# adding nodes
chatbot.add_node('send_message', send_message)

# adding edges
chatbot.add_edge(START, 'send_message')
chatbot.add_edge('send_message', END)



@router.post("/chat/", tags=['Chatting'])
async def chatt(request: ChatRequest):
    thread_id = request.thread_id
    if not thread_id:
        thread_id = str(uuid.uuid4())
    config = {
        "configurable": {
            'thread_id': thread_id
        }
    }

    workflow = chatbot.compile(checkpointer=checkpointer)
    
    user_message = HumanMessage(content=request.message)
    
    async def token_generator():
        async for event in workflow.astream_events({
            'messages': [user_message],
        }, config=config, version="v2"):
            kind = event["event"]
            if kind == "on_chat_model_stream":
                content = event["data"]["chunk"].content
                if content:
                    yield content

    return StreamingResponse(
        token_generator(),
        media_type="text/plain",
        headers={"X-Thread-ID": thread_id}
    )

