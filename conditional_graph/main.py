
from langgraph.graph import StateGraph, START, END
from state import ReviewState
from nodes import find_sentiment, run_diagnosis, positive_response, negative_response, check_sentiment

graph = StateGraph(ReviewState)

graph.add_node("find_sentiment",find_sentiment)
graph.add_node("run_diagnosis",run_diagnosis)
graph.add_node("negative_response",negative_response)
graph.add_node("positive_response",positive_response)


graph.add_edge(START, "find_sentiment")
graph.add_conditional_edges("find_sentiment", check_sentiment)
graph.add_edge("run_diagnosis", "negative_response")
graph.add_edge("negative_response", END)
graph.add_edge("positive_response", END)

workflow = graph.compile()

initial_state = {
        'review': "I’ve been trying to log in for over an hour now, and the app keeps freezing on the authentication screen. I even tried reinstalling it, but no luck. This kind of bug is unacceptable, especially when it affects basic functionality."
}
result = workflow.invoke(initial_state)

print(result)




