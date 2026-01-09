from state import ChatState
from langchain_openai import ChatOpenAI
from tools import internet_search_tool, calculator, get_stock_price
from langgraph.prebuilt import ToolNode
from langsmith import traceable
from dotenv import load_dotenv
load_dotenv()

tools = [internet_search_tool, calculator, get_stock_price]
model = ChatOpenAI(model='gpt-4o-mini')
model_with_tools = model.bind_tools(tools)

def chat(state: ChatState):

    messages = state['messages']

    result = model_with_tools.invoke(messages)

    return {
        'messages': [result]
    }

tool_node = ToolNode(tools)