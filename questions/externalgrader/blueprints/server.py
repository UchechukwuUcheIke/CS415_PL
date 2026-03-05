from graph.graph import Graph, graphs_equal
from graph.node import Node
from graph.litegraph import from_litegraph_json, to_litegraph_json
import json

def create_graph():
    g = Graph()
    
    n1 = Node("A", "blueprint/print", 100, 200)
    n1.inputs = ["Text"]
    n1.outputs = []
    
    n2 = Node("B", "blueprint/beginplay", 50, 200)
    n2.inputs = []
    n2.outputs = ["Exec"]
    
    g.nodes["A"] = n1  # Use dict, not append
    g.nodes["B"] = n2
    
    g.links.append(("B", 0, "A", 0))
    
    return g

graph = create_graph()
def generate(data):
    litegraph_json = to_litegraph_json(graph)
    #Jinja struggles with parsing JSON directly, so we stringify it
    data["params"]["initial_graph"] = json.dumps(litegraph_json)

def grade(data):

    print(data["submitted_answers"])
    student_graph_json = data["submitted_answers"]["student_graph"]
    student_graph = from_litegraph_json(json.loads(student_graph_json))

    #TODO: Last thing: we need an effective way to compare the student graph with the actual graph
    print(to_litegraph_json(graph))
    print(student_graph_json)
    
    final_score = 1 if graphs_equal(student_graph, graph) else 0
    data["score"] = final_score