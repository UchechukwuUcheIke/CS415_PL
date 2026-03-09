from blueprints.graph import Graph
from blueprints.node import Node

def create_solution_graph():
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

def create_initial_graph():
    g = Graph()
    
    n1 = Node("Overlap", "blueprint/oncomponentbeginoverlap", 50, 200)
    n3 = Node("Damage", "blueprint/applydamage", 450, 200)
    
    g.nodes["Overlap"] = n1
    g.nodes["Damage"] = n3

    g.links.extend([
        ("Overlap", 0, "Damage", 0),   # Exec → Exec
        ("Overlap", 1, "Damage", 1),    # As BP_Player → Damaged Actor
    ])
    
    return g