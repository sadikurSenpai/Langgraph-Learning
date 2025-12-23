from langgraph.graph import StateGraph, START, END
from state import BlogState
from nodes import create_outline, write_blog, evaluate
from dotenv import load_dotenv
load_dotenv()

graph = StateGraph(BlogState)

graph.add_node('create_outline', create_outline)
graph.add_node('write_blog', write_blog)
graph.add_node('evaluate', evaluate)

graph.add_edge(START, 'create_outline')
graph.add_edge('create_outline', 'write_blog')
graph.add_edge('write_blog', 'evaluate')
graph.add_edge('evaluate', END)

workflow = graph.compile()

result = workflow.invoke({'topic':'Generative AI Jobs Prediction in Bangladesh for 2026'})
print(result)