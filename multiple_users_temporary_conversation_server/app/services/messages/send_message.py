from app.services.states.ChatState import Chat
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

def send_message(state: Chat):
    model = ChatOpenAI(model='gpt-4o-mini-2024-07-18')

    messages = state['messages']

    result = model.invoke(messages)

    return {
        'messages': [ result ]
    }