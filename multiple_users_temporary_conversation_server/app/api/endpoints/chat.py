from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.api.schemas.chat import ChatRequest
from app.services.states.ChatState import Chat
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage
from app.services.messages.send_message import send_message

router = APIRouter()

checkpointer = InMemorySaver()
chatbot = StateGraph(Chat)

# adding nodes
chatbot.add_node('send_message', send_message)

# adding edges
chatbot.add_edge(START, 'send_message')
chatbot.add_edge('send_message', END)



@router.post("/chat/", tags=['Chatting'])
def chatt(request: ChatRequest):
    thread_id = request.thread_id
    config = {
        "configurable": {
            'thread_id': thread_id
        }
    }

    workflow = chatbot.compile(checkpointer=checkpointer)
    
    user_message = HumanMessage(content=request.message)
    result = workflow.invoke({
        'messages': [user_message],
    }, config=config)

    return JSONResponse(
        status_code=200,
        content={
            'message': result['messages'][-1].content,
            'thread_id': thread_id
        }
    )

