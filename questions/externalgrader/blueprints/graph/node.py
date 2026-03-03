class Node:
    def __init__(self, id, type_name, x=0, y=0):
        self.id = id
        self.type_name = type_name
        self.inputs = []   # list of input pin names
        self.outputs = []  # list of output pin names
        self.x = x
        self.y = y