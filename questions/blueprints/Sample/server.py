from blueprints.graph import Graph, graphs_equal
from blueprints.node import Node
from blueprints.litegraph_utils import from_litegraph_json, to_litegraph_json, generate_litegraph_registration_js
import json

def create_graph():
    g = Graph()
    
    n1 = Node("Overlap", "blueprint/oncomponentbeginoverlap", 50, 200)
    n2 = Node("Cast", "blueprint/cast_to_bp_player", 250, 200)
    n3 = Node("Damage", "blueprint/applydamage", 450, 200)
    
    g.nodes["Overlap"] = n1
    g.nodes["Cast"] = n2
    g.nodes["Damage"] = n3

    g.links.extend([
        ("Overlap", 0, "Cast", 0),   # Exec → Exec
        ("Overlap", 1, "Cast", 1),   # Other Actor → Object
        ("Cast", 0, "Damage", 0),    # Cast Success → Exec
        ("Cast", 2, "Damage", 1),    # As BP_Player → Damaged Actor
    ])
    
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