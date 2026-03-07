from blueprints.pin_type import PIN_TYPES
from blueprints.pin import InputPin, OutputPin
from blueprints.ue5_data_types import UE5DataType

class NodeType:
    def __init__(self, type_name, title, inputs, outputs, color = "#007777"):
        self.type_name = type_name
        self.title = title
        self.inputs = inputs
        self.outputs = outputs
        self.color = color

NODE_TYPES = {
    "blueprint/beginplay": NodeType(
        "blueprint/beginplay",
        "Begin Play",
        [],
        [
            OutputPin("Out", PIN_TYPES[UE5DataType.EXEC])
        ],
        "#770000"
    ),
    "blueprint/print": NodeType(
        "blueprint/print",
        "Print String",
        [
            InputPin("In", PIN_TYPES[UE5DataType.EXEC]), 
            InputPin("Text", PIN_TYPES[UE5DataType.STRING])
        ],
        [],
        "#007777"
    ),
    "blueprint/branch": NodeType(
        "blueprint/branch",
        "Branch",
        [
            InputPin("In", PIN_TYPES[UE5DataType.EXEC]), 
            InputPin("Condition", PIN_TYPES[UE5DataType.BOOLEAN])
        ],
        [
            OutputPin("True", PIN_TYPES[UE5DataType.EXEC]), 
            OutputPin("False", PIN_TYPES[UE5DataType.EXEC])
        ],
        "#333333"
    ),
    # Add more node types here
    # ----------------------------
    # OnComponentBeginOverlap
    # ----------------------------
    "blueprint/oncomponentbeginoverlap": NodeType(
        "blueprint/oncomponentbeginoverlap",
        "On Component Begin Overlap",
        [],
        [
            OutputPin("Exec", PIN_TYPES[UE5DataType.EXEC]),
            OutputPin("Other Actor", PIN_TYPES[UE5DataType.OBJECT_REFERENCE])
        ],
        "#770000"
    ),

    # ----------------------------
    # Cast To BP_Player
    # ----------------------------
    "blueprint/cast_to_bp_player": NodeType(
        "blueprint/cast_to_bp_player",
        "Cast To BP_Player",
        [
            InputPin("In", PIN_TYPES[UE5DataType.EXEC]),
            InputPin("Object", PIN_TYPES[UE5DataType.OBJECT_REFERENCE])
        ],
        [
            OutputPin("Cast Succeeded", PIN_TYPES[UE5DataType.EXEC]),
            OutputPin("Cast Failed", PIN_TYPES[UE5DataType.EXEC]),
            OutputPin("As BP_Player", PIN_TYPES[UE5DataType.OBJECT_REFERENCE])
        ],
        "#007777"
    ),

    # ----------------------------
    # Apply Damage
    # ----------------------------
    "blueprint/applydamage": NodeType(
        "blueprint/applydamage",
        "Apply Damage",
        [
            InputPin("In", PIN_TYPES[UE5DataType.EXEC]),
            InputPin("Damaged Actor", PIN_TYPES[UE5DataType.OBJECT_REFERENCE]),
            InputPin("Base Damage", PIN_TYPES[UE5DataType.FLOAT])
        ],
        [
            OutputPin("Out", PIN_TYPES[UE5DataType.EXEC])
        ],
        "#007777"
    ),
}

