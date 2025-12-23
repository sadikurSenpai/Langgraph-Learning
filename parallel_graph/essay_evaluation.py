from langgraph.graph import StateGraph, START, END
from nodes import generate_cow_feedback, generate_dot_feedback, generate_lol_feedback, generate_overall_feedback_and_avg_score
from state import EvaluateEssayState

graph = StateGraph(EvaluateEssayState)

graph.add_node('generate_cow_feedback', generate_cow_feedback)
graph.add_node('generate_dot_feedback', generate_dot_feedback)
graph.add_node('generate_lol_feedback', generate_lol_feedback)
graph.add_node('generate_overall_feedback_and_avg_score', generate_overall_feedback_and_avg_score)

graph.add_edge(START, 'generate_cow_feedback')
graph.add_edge(START, 'generate_dot_feedback')
graph.add_edge(START, 'generate_lol_feedback')
graph.add_edge('generate_cow_feedback', 'generate_overall_feedback_and_avg_score')
graph.add_edge('generate_dot_feedback', 'generate_overall_feedback_and_avg_score')
graph.add_edge('generate_lol_feedback', 'generate_overall_feedback_and_avg_score')
graph.add_edge('generate_overall_feedback_and_avg_score', END)

workflow = graph.compile()

essay = """Bangladesh: A Nation of Resilience and Promise

Bangladesh is a South Asian country known for its rich culture, strong sense of community, and remarkable resilience. Located on the fertile delta of the Ganges, Brahmaputra, and Meghna rivers, it is one of the most densely populated countries in the world. Despite limited resources and frequent natural challenges, Bangladesh has developed a strong identity built on courage, hard work, and hope.

The capital city, Dhaka, serves as the economic and political center of the country. Bangladesh gained independence in 1971 after a historic struggle, and since then it has focused on rebuilding and progressing as a sovereign nation. Over the years, the country has made significant advancements in education, women’s empowerment, healthcare, and economic growth, particularly through the garment industry and remittances from overseas workers.

Bangladesh is renowned for its vibrant culture. Bengali language and literature hold a special place in the hearts of its people, symbolized by the historic Language Movement of 1952. Festivals such as Pohela Boishakh, Eid-ul-Fitr, and Eid-ul-Adha reflect its cultural diversity and unity. Music, art, and traditional cuisine further enrich its national identity.

Nature also plays a major role in defining Bangladesh. The country is home to the Sundarbans, the largest mangrove forest in the world and habitat of the Royal Bengal Tiger. Its lush greenery, rivers, and rural landscapes provide beauty and livelihood to millions. However, Bangladesh often faces natural disasters such as floods and cyclones. Even so, the spirit of its people continues to demonstrate strength and adaptability.

Today, Bangladesh stands as a symbol of determination and development. With a growing economy, improving infrastructure, and a youthful population, the nation looks toward the future with ambition. Bangladesh may be small in size, but its history, culture, and resilience make it a country of great significance and promise."""
result = workflow.invoke(
    {'essay':essay}
)

print(result['overall_feedback'], result['avg_score'])
