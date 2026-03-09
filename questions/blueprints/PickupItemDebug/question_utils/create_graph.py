from blueprints.graph import Graph
from blueprints.node import Node

def create_solution_graph():
    g = Graph()

    n1 = Node("Overlap",  "blueprint/oncomponentbeginoverlap", 50,  200)
    n2 = Node("Cast",     "blueprint/cast_to_bp_player",       280, 200)
    n3 = Node("Sound",    "blueprint/playsoundatlocation",     510, 200)
    n4 = Node("Destroy",  "blueprint/destroyactor",            740, 200)

    g.nodes["Overlap"] = n1
    g.nodes["Cast"]    = n2
    g.nodes["Sound"]   = n3
    g.nodes["Destroy"] = n4

    g.links.extend([
        ("Overlap", 0, "Cast",    0),  # Exec       → Exec
        ("Overlap", 1, "Cast",    1),  # Other Actor → Object
        ("Cast",    0, "Sound",   0),  # Success     → Exec
        ("Sound",   0, "Destroy", 0),  # Out         → Exec
    ])

    return g

def create_initial_graph():
    g = Graph()

    n1 = Node("Overlap",  "blueprint/oncomponentbeginoverlap", 50,  200)
    n4 = Node("Destroy",  "blueprint/destroyactor",            510, 200)
    n3 = Node("Sound",    "blueprint/playsoundatlocation",     740, 200)

    g.nodes["Overlap"] = n1
    g.nodes["Sound"]   = n3
    g.nodes["Destroy"] = n4

    g.links.extend([
        ("Overlap", 0, "Destroy", 0),
        ("Destroy", 0, "Sound",   0),
    ])

    return g