import os
from health_assistant.data_processing import process_user_data
from health_assistant.rag_system import create_rag_system
from health_assistant.config import set_openai_key
from langchain_openai import ChatOpenAI
from langgraph.graph import Graph, StateGraph
from typing import TypedDict, Annotated
from typing_extensions import TypedDict

# Get the API key
api_key = set_openai_key()
print(api_key)

llm = ChatOpenAI(
    model_name="gpt-4",
    api_key=api_key
)

rag_chain = create_rag_system(llm)

# Define the state structure
class State(TypedDict):
    user_data: dict
    query: str
    response: str

# Update the functions to work with state
def process_data(state: State) -> State:
    processed_data = process_user_data(state['user_data'])
    state['processed_data'] = processed_data
    return state

def generate_health_schedule(state: State) -> State:
    response = rag_chain.invoke(state['query'])
    state['response'] = response
    return state

# Create the graph
workflow = StateGraph(State)

# Add nodes
workflow.add_node("process_data", process_data)
workflow.add_node("generate_health_schedule", generate_health_schedule)

# Add edges
workflow.set_entry_point("process_data")
workflow.add_edge("process_data", "generate_health_schedule")
workflow.set_finish_point("generate_health_schedule")

# Compile the graph
app = workflow.compile()

# Example usage
user_profile = {
    'sleep_quality': [6.5, 7, 8, 6, 7.5],
    'steps': [10000, 12000, 9500, 11000, 12500],
    'heart_rate': [65, 70, 68, 72, 69]
}
user_query = "Create a wellness plan for improving sleep quality and menstrual cycle health."

# Run the graph with initial state
initial_state = State(
    user_data=user_profile,
    query=user_query,
    response=""
)

# Execute the workflow
final_state = app.invoke(initial_state)

print("Personalized Health Schedule with RAG:", final_state['response'])
