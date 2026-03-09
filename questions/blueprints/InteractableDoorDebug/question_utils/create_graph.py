from blueprints.graph import Graph
from blueprints.node import Node

def create_solution_graph():
    g = Graph()

    n1 = Node("Input",       "blueprint/inputaction_interact",    50,  200)
    n2 = Node("FlipFlop",    "blueprint/flipflop",                280, 200)
    n3 = Node("RotateOpen",  "blueprint/setactorrotation_open",   510, 120)
    n4 = Node("RotateClosed","blueprint/setactorrotation_closed", 510, 300)

    g.nodes["Input"]        = n1
    g.nodes["FlipFlop"]     = n2
    g.nodes["RotateOpen"]   = n3
    g.nodes["RotateClosed"] = n4

    g.links.extend([
        ("Input",    0, "FlipFlop",    0),  # Triggered → In
        ("FlipFlop", 0, "RotateOpen",  0),  # A         → In (Open)
        ("FlipFlop", 1, "RotateClosed",0),  # B         → In (Closed)
    ])

    return g

def create_initial_graph():
    g = Graph()
    
    n1 = Node("Tick",        "blueprint/eventtick",               50,  200)
    n2 = Node("FlipFlop",    "blueprint/flipflop",                280, 200)
    n3 = Node("RotateOpen",  "blueprint/setactorrotation_open",   510, 120)
    n4 = Node("RotateClosed","blueprint/setactorrotation_closed", 510, 300)

    g.nodes["Tick"]         = n1
    g.nodes["FlipFlop"]     = n2
    g.nodes["RotateOpen"]   = n3
    g.nodes["RotateClosed"] = n4

    g.links.extend([
        ("Tick",     0, "FlipFlop",     0),  # Out → In          (buggy connection)
        ("FlipFlop", 0, "RotateOpen",   0),  # A   → In (Open)   (given)
        ("FlipFlop", 1, "RotateClosed", 0),  # B   → In (Closed) (given)
    ])

    return g