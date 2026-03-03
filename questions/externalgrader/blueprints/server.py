from graph.graph import Graph
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

    g.nodes.append(n1)
    g.nodes.append(n2)

    g.links.append(("B", 0, "A", 0))  # BeginPlay.Exec -> PrintString.Text
    return g

def normalize_litegraph(graph: dict) -> dict:
    """
    Convert LiteGraph serialized dict into canonical form
    that ignores IDs, positions, ordering, etc.
    """

    # --- Normalize Nodes ---
    nodes = []
    id_to_type = {}

    for node in graph.get("nodes", []):
        node_type = node["type"]
        id_to_type[node["id"]] = node_type

        nodes.append({
            "type": node_type,
            "properties": node.get("properties", {}),
            "inputs": [inp["name"] for inp in node.get("inputs", [])],
            "outputs": [out["name"] for out in node.get("outputs", [])],
        })

    # Sort nodes to remove ordering effects
    nodes.sort(key=lambda n: json.dumps(n, sort_keys=True))

    # --- Normalize Links ---
    links = []

    for link in graph.get("links", []):
        # LiteGraph link format:
        # [link_id, origin_id, origin_slot, target_id, target_slot, type]

        _, origin_id, origin_slot, target_id, target_slot, *_ = link

        links.append({
            "from_type": id_to_type[origin_id],
            "from_slot": origin_slot,
            "to_type": id_to_type[target_id],
            "to_slot": target_slot,
        })

    # Sort links
    links.sort(key=lambda l: json.dumps(l, sort_keys=True))

    return {
        "nodes": nodes,
        "links": links
    }

def litegraphs_equal(g1: dict, g2: dict) -> bool:
    n1 = normalize_litegraph(g1)
    n2 = normalize_litegraph(g2)
    return n1 == n2

graph = create_graph()
def generate(data):
    litegraph_json = to_litegraph_json(graph)
    #Jinja struggles with parsing JSON directly, so we stringify it
    data["params"]["initial_graph"] = json.dumps(litegraph_json)

def grade(data):

    print(data["submitted_answers"])
    student_graph_json = data["submitted_answers"]["student_graph"]
    student_graph = json.loads(student_graph_json)

    print(student_graph)
    print(to_litegraph_json(graph))
    final_score = 1 if litegraphs_equal(student_graph, to_litegraph_json(graph)) else 0
    data["score"] = final_score