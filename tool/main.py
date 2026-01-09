from langgraph.graph import StateGraph, START, END
from state import ChatState
from nodes import chat, tool_node
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import tools_condition
from langsmith import traceable
import os

os.environ['LANGCHAIN_PROJECT'] = 'Query with Tools'

graph = StateGraph(ChatState)

graph.add_node('chat', chat)
graph.add_node("tools", tool_node)

graph.add_edge(START, 'chat')
graph.add_conditional_edges('chat', tools_condition)
graph.add_edge('tools', 'chat')


workflow = graph.compile()

@traceable(name='Query invokation')
def invokation():
    result = workflow.invoke({
        'messages': [HumanMessage(content="What's the stock of Microsoft today? I want to buy 50. What will be cost of mine")]
    })
    print(result)
    print()
    print()
    print(result['messages'][-1].content)


invokation()