from state import BlogState
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model='gpt-4o')

def create_outline(state: BlogState):
    topic = state["topic"]
    prompt = f"Create an outline for a blog about {topic}"

    outline_text = llm.invoke(prompt).content

    return {"outline": outline_text}

