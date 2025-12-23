from state import BattingState, EvaluateEssayState
from evaluate_schema import Evaluate
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model='gpt-4o')

def calculate_run_rate(state: BattingState):
    run_rate = (state['runs']/state['balls'])*100
    return {'run_rate':run_rate}

def calculate_boundary_percentage(state: BattingState):
    boundary_percentage = ((state['fours']*4 + state['six']*6)/state['runs'])*100
    return {'boundary_percentage':boundary_percentage}

def calculate_boundary_per_ball(state: BattingState):
    boundary_per_ball = state['balls']/(state['fours'] + state['six'])
    return {'boundary_per_ball':boundary_per_ball}

def generate_summary(state: BattingState):
    summary = f"""
Runs: {state['runs']}\n
Balls: {state['balls']}\n
Run Rate: {state['run_rate']}\n
Boundary Percentage: {state['boundary_percentage']}\n
Boundary in the next {state['boundary_per_ball']} Balls
"""
    return {'summary':summary}






def generate_dot_feedback(state: EvaluateEssayState):
    structured_llm = llm.with_structured_output(Evaluate)
    prompt = f"""
'Evaluate the depth of thought of the following essay and provide a feedback and assign a score out of 10 \n {state["essay"]}
"""
    result = structured_llm.invoke(prompt)
    return {'dot_feedback':result.feedback, 'individual_scores':[result.score]}

def generate_cow_feedback(state: EvaluateEssayState):
    structured_llm = llm.with_structured_output(Evaluate)
    prompt = f"""
'Evaluate the clarifty of writing of the following essay and provide a feedback and assign a score out of 10 \n {state["essay"]}
"""
    result = structured_llm.invoke(prompt)
    return {'cow_feedback':result.feedback, 'individual_scores':[result.score]}

def generate_lol_feedback(state: EvaluateEssayState):
    structured_llm = llm.with_structured_output(Evaluate)
    prompt = f"""
'Evaluate the level of language of the following essay and provide a feedback and assign a score out of 10 \n {state["essay"]}
"""
    result = structured_llm.invoke(prompt)
    return {'lol_feedback':result.feedback, 'individual_scores':[result.score]}

def generate_overall_feedback_and_avg_score(state: EvaluateEssayState):
    structured_llm = llm.with_structured_output(Evaluate)
    prompt = f'Based on the following feedbacks create a summarized feedback \n depth of thought feedback - {state["dot_feedback"]} \n clarity of writing feedback - {state["cow_feedback"]} \n level of language feedback - {state["lol_feedback"]}'

    result = structured_llm.invoke(prompt)

    avg_score = sum(state['individual_scores'])/len(state['individual_scores'])
    return {'overall_feedback':result.feedback, 'avg_score':avg_score}


    
