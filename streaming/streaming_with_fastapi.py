from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from dotenv import load_dotenv

from langgraph.graph import StateGraph, START, END
from state import BlogState
from nodes import create_outline

load_dotenv()

app = FastAPI()

graph = StateGraph(BlogState)
graph.add_node("create_outline", create_outline)
graph.add_edge(START, "create_outline")
graph.add_edge("create_outline", END)

workflow = graph.compile()


@app.get("/chat/{topic}")
def chat(topic: str):

    def token_generator():
        for chunk, meta in workflow.stream(
            {
                'topic': topic
            }, 
            stream_mode="messages"
        ):
            if chunk.content:
                yield chunk.content

    return StreamingResponse(
        token_generator(),
        media_type="text/plain"
    )
