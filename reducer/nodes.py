from state import ItemsWithoutReducer, ItemsWithReducer

def with_node_A(state: ItemsWithReducer):
    return {
        'items': ['Item A']
    }

def with_node_B(state: ItemsWithReducer):
    return {
        'items': ['Item B']
    }

def without_node_A(state: ItemsWithoutReducer):
    return {
        'items': ['Item A']
    }

def without_node_B(state: ItemsWithoutReducer):
    return {
        'items': ['Item B']
    }

