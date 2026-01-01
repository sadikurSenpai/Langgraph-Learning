from state import ItemsWithoutReducer, ItemsWithReducer
from langgraph.graph import StateGraph, START, END
from nodes import with_node_A, with_node_B, without_node_A, without_node_B

print("Without Reducer; We are adding two items A, and B")


# creating
without_reducer_graph = StateGraph(ItemsWithoutReducer)
with_reducer_graph = StateGraph(ItemsWithReducer)

# adding nodes of both
without_reducer_graph.add_node('nodeA', without_node_A)
without_reducer_graph.add_node('nodeB', without_node_B)

with_reducer_graph.add_node('nodeA', with_node_A)
with_reducer_graph.add_node('nodeB', with_node_B)

# adding edges of both
without_reducer_graph.add_edge(START, 'nodeA')
without_reducer_graph.add_edge('nodeA', 'nodeB')
without_reducer_graph.add_edge('nodeB', END)

with_reducer_graph.add_edge(START, 'nodeA')
with_reducer_graph.add_edge('nodeA', 'nodeB')
with_reducer_graph.add_edge('nodeB', END)


# compile 
without_workflow = without_reducer_graph.compile()
with_workflow = with_reducer_graph.compile()


# execute
print()
print("Without Reducer:")
result = without_workflow.invoke({
    'items': []
})
print(result)
print()
print()

print("With Reducer")
result = with_workflow.invoke({
    'items': []
})
print(result)
