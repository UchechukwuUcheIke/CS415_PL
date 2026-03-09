from blueprints.graph import Graph
from blueprints.node import Node

def create_solution_graph():
    g = Graph()
    n1 = Node("Tick",         "blueprint/eventtick",       50,  100)
    n2 = Node("Check",        "blueprint/float_less_than", 280, 200)
    n3 = Node("Branch",       "blueprint/branch",          280, 100)
    n4 = Node("Add",          "blueprint/float_add",       510, 100)
    n5 = Node("SetHealth",    "blueprint/sethealth",       740, 100)
    n6 = Node("GetHealth",    "blueprint/gethealth",       280, 300)
    n7 = Node("GetMaxHealth", "blueprint/getmaxhealth",    280, 400)
    n8 = Node("RegenAmount",  "blueprint/regenamount",     280, 500)

    g.nodes["Tick"]         = n1
    g.nodes["Check"]        = n2
    g.nodes["Branch"]       = n3
    g.nodes["Add"]          = n4
    g.nodes["SetHealth"]    = n5
    g.nodes["GetHealth"]    = n6
    g.nodes["GetMaxHealth"] = n7
    g.nodes["RegenAmount"]  = n8

    g.links.extend([
        ("Tick",      0, "Branch", 0),  # Exec        → In
        ("GetHealth", 0, "Check",  0),  # Health value → A
        ("GetMaxHealth", 0, "Check", 1),# Max Health   → B
        ("Check",     0, "Branch", 1),  # Result       → Condition
        ("GetHealth", 0, "Add",    0),  # Health value → A
        ("RegenAmount",0, "Add",   1),  # Regen value  → B
        ("Add",       0, "SetHealth", 1), # Result     → Health
        ("Branch",    0, "SetHealth", 0), # True(Exec) → In (exec)
        
    ])

    return g

def create_initial_graph():
    g = Graph()
    n1 = Node("Tick",         "blueprint/eventtick",       50,  100)
    n2 = Node("Check",        "blueprint/float_less_than", 280, 300)
    n3 = Node("Branch",       "blueprint/branch",          280, 100)
    n4 = Node("Add",          "blueprint/float_add",       510, 200)
    n5 = Node("SetHealth",    "blueprint/sethealth",       740, 100)
    n6 = Node("GetHealth",    "blueprint/gethealth",       50, 300)
    n7 = Node("GetMaxHealth", "blueprint/getmaxhealth",    50, 400)
    n8 = Node("RegenAmount",  "blueprint/regenamount",     50, 500)

    g.nodes["Tick"]         = n1
    g.nodes["Check"]        = n2
    g.nodes["Branch"]       = n3
    g.nodes["Add"]          = n4
    g.nodes["SetHealth"]    = n5
    g.nodes["GetHealth"]    = n6
    g.nodes["GetMaxHealth"] = n7
    g.nodes["RegenAmount"]  = n8

    g.links.extend([
        ("Tick",         0, "Branch",    0),  # Exec          → In        (given)
        ("GetHealth",    0, "Add",       0),  # Health value  → A         (given)
        ("RegenAmount",  0, "Add",       1),  # Regen value   → B         (given)
        ("Add",          0, "SetHealth", 1),  # Result        → Health    (given)
        ("Branch",       0, "SetHealth", 0),  # True (Exec)   → In        (given)
    ])

    return g