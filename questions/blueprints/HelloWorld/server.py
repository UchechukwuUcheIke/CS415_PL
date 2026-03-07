from blueprints.graph import Graph, graphs_equal
from blueprints.node import Node
from blueprints.litegraph_utils import from_litegraph_json, to_litegraph_json, generate_litegraph_registration_js
import json

def create_solution_graph():
    g = Graph()
    
    n1 = Node("A", "blueprint/print", 100, 200)
    n2 = Node("B", "blueprint/beginplay", 50, 200)
    
    g.nodes["A"] = n1
    g.nodes["B"] = n2
    g.links.append(("B", 0, "A", 0))
    
    return g

def create_initial_graph():
    g = Graph()
    
    n1 = Node("A", "blueprint/print", 400, 200)
    n2 = Node("B", "blueprint/beginplay", 50, 200)
    
    g.nodes["A"] = n1
    g.nodes["B"] = n2
    
    return g

solution_graph = create_solution_graph()
initial_graph = create_initial_graph()

def generate(data):
    data["params"]["storage_key"] =  f"{data['variant_seed']}"
    #Jinja struggles with parsing JSON directly, so we stringify it
    litegraph_json = to_litegraph_json(initial_graph)
    data["params"]["initial_graph"] = json.dumps(litegraph_json)
    # Injects registered node types into question.html
    data["params"]["node_registration_js"] = generate_litegraph_registration_js()

def grade(data):
    student_graph_json = data["submitted_answers"]["student_graph"]
    student_graph = from_litegraph_json(json.loads(student_graph_json))
    
    final_score = 1 if graphs_equal(student_graph, solution_graph) else 0
    data["score"] = final_score