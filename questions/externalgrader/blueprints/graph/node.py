from graph.node_type import NodeType, NODE_TYPES

class Node:
    def __init__(self, id, type_name, x=0, y=0):
        self.id = id
        self.type_name = type_name
        
        # Auto-populate inputs/outputs from node type
        if type_name in NODE_TYPES:
            node_type = NODE_TYPES[type_name]
            self.inputs = [name for name, _, _ in node_type.inputs]
            self.outputs = [name for name, _, _ in node_type.outputs]
        else:
            self.inputs = []
            self.outputs = []
        
        self.x = x
        self.y = y