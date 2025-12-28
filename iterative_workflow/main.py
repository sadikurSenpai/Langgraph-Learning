from langgraph.graph import StateGraph, START, END
from state import TweetState
from nodes import generate_tweet, evaluate_tweet, optimize_tweet, route_node


graph = StateGraph(TweetState)

graph.add_node('generate', generate_tweet)
graph.add_node('evaluate', evaluate_tweet)
graph.add_node('optimize', optimize_tweet)


graph.add_edge(START, 'generate')
graph.add_edge('generate', 'evaluate')
graph.add_conditional_edges('evaluate', route_node, {'approved':END, 'needs_improvement': 'optimize'})
graph.add_edge('optimize', 'evaluate')

workflow = graph.compile()

result = workflow.invoke({
    'topic': 'Shadikur as an AI Developer',
    'iteration': 0,  # Start with iteration 0
    'max_iteration': 5  # Set a maximum number of iterations
})

print(result)





