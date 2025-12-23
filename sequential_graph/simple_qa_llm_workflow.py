from langgraph.graph import StateGraph, START, END
from state import LLM_QA
from nodes import llm_qa

# define
graph = StateGraph(LLM_QA)

# add node
graph.add_node('llm_qa', llm_qa)

# add edge
graph.add_edge(START, 'llm_qa')
graph.add_edge('llm_qa', END)

# compile
workflow = graph.compile()

# execute
initial_state = {'question':'Is there any possibility of earth hitting any black hole'}
result = workflow.invoke(initial_state)
print(result)


