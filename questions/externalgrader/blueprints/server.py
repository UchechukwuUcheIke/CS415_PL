from graph.graph import Graph, graphs_equal
from graph.node import Node
from graph.node_type import generate_litegraph_registration_js
from graph.litegraph import from_litegraph_json, to_litegraph_json
import json

def create_graph():
    g = Graph()
    
    n1 = Node("A", "blueprint/print", 100, 200)
    n2 = Node("B", "blueprint/beginplay", 50, 200)
    
    g.nodes["A"] = n1
    g.nodes["B"] = n2
    g.links.append(("B", 0, "A", 0))
    
    return g

graph = create_graph()
def generate(data):
    litegraph_json = to_litegraph_json(graph)
    data["params"]["storage_key"] =  f"{data['variant_seed']}"
    #Jinja struggles with parsing JSON directly, so we stringify it
    data["params"]["initial_graph"] = json.dumps(litegraph_json)
    # Injects registered node types into question.html
    data["params"]["node_registration_js"] = generate_litegraph_registration_js()

def grade(data):
    student_graph_json = data["submitted_answers"]["student_graph"]
    student_graph = from_litegraph_json(json.loads(student_graph_json))
    
    final_score = 1 if graphs_equal(student_graph, graph) else 0
    data["score"] = final_score