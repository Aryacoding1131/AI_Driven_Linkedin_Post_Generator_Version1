from workflow import graph

# Save the workflow as a PNG image
png_data = graph.get_graph().draw_mermaid_png()

with open("langgraph_workflow.png", "wb") as f:
    f.write(png_data)

print("Graph saved as langgraph_workflow.png")