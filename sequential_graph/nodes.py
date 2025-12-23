from state import BMIState, LLM_QA, BlogState
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model='gpt-4o')

def calculate_bmi(state: BMIState) -> BMIState:
    height = state['height']
    weight = state['weight']
    state['bmi'] = weight / (height**2)
    return state


def label_bmi(state:BMIState)->BMIState:
    bmi = state['bmi']
    if bmi <= 18.5:
        state['category'] = 'underweight'
    elif bmi < 24:
        state['category'] = 'healthy'
    else:
        state['category'] = 'overweight'
    return state


def llm_qa(state:LLM_QA)->LLM_QA:
    llm = ChatOpenAI(model='gpt-4o')
    # for chunk in llm.stream(state['question']):
    #     print(chunk.text, end="", flush=True)
    state['answer'] = llm.invoke(state['question']).content
    return state

def create_outline(state: BlogState)->BlogState:
    topic = state['topic']
    prompt = f"Create an outline for a blog about {topic}"
    state['outline'] = llm.invoke(prompt).content
    return state
def write_blog(state: BlogState)->BlogState:
    topic = state['topic']
    outline = state['outline']
    prompt = f"Write a detailed blog of the topic: {topic}\nYou should and should write in the following outline: {outline}"
    state['blog'] = llm.invoke(prompt).content
    return state
def evaluate(state: BlogState)->BlogState:
    topic = state['topic']
    outline = state['outline']
    blog = state['blog']
    prompt = f"Evaluate the blog based on the topic, and outline. Give a integar score from 1-100.\ntopic:{topic}\noutline:{outline}\nblog:{blog}"
    state['score']=llm.invoke(prompt).content
    return state


    
