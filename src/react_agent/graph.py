"""This module defines the state graph for the react agent."""

from langgraph.graph import END, START, StateGraph
from langgraph.prebuilt import tools_condition

from react_agent.configuration import Configuration
from react_agent.nodes import generate_response, react_tools_node
from react_agent.state import ReactGraphAnnotation

builder = StateGraph(ReactGraphAnnotation, config_schema=Configuration)

builder.add_node("generate_response", generate_response)

builder.add_edge(START, "generate_response")
builder.add_edge("generate_response", END)

react_graph = builder.compile()

react_graph.name = "react_agent"
