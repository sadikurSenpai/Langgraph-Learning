from langgraph.graph import StateGraph, START, END
from nodes import calculate_boundary_per_ball, calculate_boundary_percentage, calculate_run_rate, generate_summary
from state import BattingState

graph = StateGraph(BattingState)

graph.add_node('calculate_run_rate', calculate_run_rate)
graph.add_node('calculate_boundary_percentage', calculate_boundary_percentage)
graph.add_node('calculate_boundary_per_ball', calculate_boundary_per_ball)
graph.add_node('generate_summary', generate_summary)

graph.add_edge(START, 'calculate_run_rate')
graph.add_edge(START, 'calculate_boundary_percentage')
graph.add_edge(START, 'calculate_boundary_per_ball')
graph.add_edge('calculate_run_rate', 'generate_summary')
graph.add_edge('calculate_boundary_percentage', 'generate_summary')
graph.add_edge('calculate_boundary_per_ball', 'generate_summary')
graph.add_edge('generate_summary', END)

workflow = graph.compile()

result = workflow.invoke(
    {
        'runs': 50,
        'balls':25,
        'fours':4,
        'six':4
    }
)

print(result['summary'])