from blueprints.pin_type import PIN_TYPES
from blueprints.pin import Pin

class NodeType:
    def __init__(self, type_name, title, inputs, outputs, color = "#007777"):
        self.type_name = type_name
        self.title = title
        # list of (name, type) tuples
        self.inputs = inputs
        self.outputs = outputs
        self.color = color

NODE_TYPES = {
    "blueprint/beginplay": NodeType(
        "blueprint/beginplay",
        "BeginPlay",
        [],
        [Pin("Out", PIN_TYPES["flow"]), Pin("Text", PIN_TYPES["text"])],
        "#770000"
    ),
    "blueprint/print": NodeType(
        "blueprint/print",
        "Print String",
        [Pin("In", PIN_TYPES["flow"]),Pin("Text", PIN_TYPES["text"])],
        [],
        "#007777"
    ),
    # Add more node types here
}

