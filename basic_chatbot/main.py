from langgraph.graph import StateGraph, START, END
from state import Chat
from nodes import send_message
from langchain_core.messages import HumanMessage

chatbot = StateGraph(Chat)

# adding nodes
chatbot.add_node('send_message', send_message)

# adding edges
chatbot.add_edge(START, 'send_message')
chatbot.add_edge('send_message', END)

# compile
workflow = chatbot.compile()

# execution
result = workflow.invoke({
    'messages': HumanMessage(content="Hi there!")
})

print(result['messages'][-1].content)