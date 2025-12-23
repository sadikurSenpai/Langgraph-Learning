from langgraph.graph import StateGraph, START, END
from state import BMIState
from nodes import calculate_bmi, label_bmi

# 1. Define the graph
graph = StateGraph(BMIState)

# 2. Define the nodes
graph.add_node('calculate_bmi', calculate_bmi)
graph.add_node('label', label_bmi)

# 3. Define the edges
graph.add_edge(START, 'calculate_bmi')
graph.add_edge('calculate_bmi', 'label')
graph.add_edge('label', END)

# 4. Compile the graph
workflow = graph.compile()

# 5. Execute the graph
initial_state = {'height':1.75, 'weight':68}
final_state = workflow.invoke(initial_state)
print(final_state)



