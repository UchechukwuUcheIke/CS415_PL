from blueprints.link import Link
from blueprints.node import Node

class Graph:
    def __init__(self):
        self.nodes = {}
        self.links = []
        self._next_id = 0
    
    def add_node(self, node_type, x=0, y=0):
        node_id = self._next_id
        self._next_id += 1

        node = Node(node_id, node_type, x, y)
        self.nodes[node_id] = node
        return node
    
    def connect(self, from_node, from_pin, to_node, to_pin):
        # Validate pins exist
        if from_pin not in [p[0] for p in from_node.type.outputs]:
            raise ValueError("Invalid output pin")

        if to_pin not in [p[0] for p in to_node.type.inputs]:
            raise ValueError("Invalid input pin")

        # Validate types match
        out_type = dict(from_node.type.outputs)[from_pin]
        in_type = dict(to_node.type.inputs)[to_pin]

        if out_type != in_type:
            raise ValueError("Pin types do not match")

        self.links.append(
            Link(from_node, from_pin, to_node, to_pin)
        )

def graphs_equal(g1, g2):
    # Same number of nodes
    if len(g1.nodes) != len(g2.nodes):
        return False
    
    # Compare node types (order doesn't matter)
    types1 = sorted(n.type_name for n in g1.nodes.values())
    types2 = sorted(n.type_name for n in g2.nodes.values())
    if types1 != types2:
        return False
    
    # Same number of links
    if len(g1.links) != len(g2.links):
        return False
    
    # Normalize links: (from_type, from_slot_index, to_type, to_slot_index)
    def normalize_links(graph):
        links = []
        for from_id, from_slot, to_id, to_slot in graph.links:
            from_node = graph.nodes[from_id]
            to_node = graph.nodes[to_id]
            links.append((
                from_node.type_name,
                from_slot,  # slot index
                to_node.type_name,
                to_slot     # slot index
            ))
        return sorted(links)
    
    return normalize_links(g1) == normalize_links(g2)