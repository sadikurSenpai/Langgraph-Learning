from langgraph.graph import StateGraph
from state import TweetState
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

graph = StateGraph(TweetState)

model = ChatOpenAI(model='gpt-4o')

print(model.invoke("Hi!!").content)

