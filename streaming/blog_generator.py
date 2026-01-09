from langgraph.graph import StateGraph, START, END
from state import BlogState
from nodes import create_outline
from dotenv import load_dotenv
load_dotenv()

graph = StateGraph(BlogState)

graph.add_node('create_outline', create_outline)

graph.add_edge(START, 'create_outline')
graph.add_edge('create_outline', END)

workflow = graph.compile()

for chunk, meta in workflow.stream(
    {"topic": "Generative AI Jobs Prediction in Bangladesh for 2026"},
    stream_mode="messages",
):
    if chunk.content:
        print(chunk.content, end="", flush=True)
