from graph.link import Link
from graph.node import Node
from graph.pin import Pin

class Graph:
    def __init__(self):
        self.nodes = []
        self.links = []  # (from_node, from_pin, to_node, to_pin)
    
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