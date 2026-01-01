from langgraph.graph import StateGraph, START, END
from state import Chat
from nodes import send_message
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver
chatbot = StateGraph(Chat)

checkpointer = InMemorySaver()

# adding nodes
chatbot.add_node('send_message', send_message)

# adding edges
chatbot.add_edge(START, 'send_message')
chatbot.add_edge('send_message', END)

# compile
workflow = chatbot.compile(checkpointer=checkpointer)


# chatting
thread_id = 'sadik'
config = {
        'configurable': {
            'thread_id': thread_id
        }
    }
while True:
    user_message = input("User: ")
    if user_message.strip().lower() in ['quit', 'bye', 'exit']:
        break
    
    user_message = HumanMessage(content=user_message)
    result = workflow.invoke({
        'messages': [user_message],
    }, config=config)

    print(f"AI: {result['messages'][-1].content}")


print(workflow.get_state(config))