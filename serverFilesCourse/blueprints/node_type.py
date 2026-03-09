from blueprints.pin_type import PIN_TYPES
from blueprints.pin import InputPin, OutputPin
from blueprints.ue5_data_types import UE5DataType
from blueprints.ue5_data_type_color import UE5DataTypeColor

class NodeType:
    def __init__(self, type_name, title, inputs, outputs, color = UE5DataTypeColor.DARK_RED):
        self.type_name = type_name
        self.title = title
        self.inputs = inputs
        self.outputs = outputs
        self.color = color.value

NODE_TYPES = {
    "blueprint/beginplay": NodeType(
        "blueprint/beginplay",
        "Begin Play",
        [],
        [
            OutputPin("Out", PIN_TYPES[UE5DataType.EXEC])
        ],
        UE5DataTypeColor.DARK_RED
    ),
    "blueprint/print": NodeType(
        "blueprint/print",
        "Print String",
        [
            InputPin("In", PIN_TYPES[UE5DataType.EXEC]), 
            InputPin("Text", PIN_TYPES[UE5DataType.STRING])
        ],
        [],
        UE5DataTypeColor.CORNFLOWER_BLUE
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
        UE5DataTypeColor.GREY
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
        UE5DataTypeColor.DARK_RED
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
        UE5DataTypeColor.TEAL_GREEN
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
        UE5DataTypeColor.CORNFLOWER_BLUE
    ),
    "blueprint/cast_to_bp_player": NodeType(
        "blueprint/cast_to_bp_player",
        "Cast To BP_Player",
        [
            InputPin("In", PIN_TYPES[UE5DataType.EXEC]),
            InputPin("Object", PIN_TYPES[UE5DataType.OBJECT_REFERENCE]),
        ],
        [
            OutputPin("Success", PIN_TYPES[UE5DataType.EXEC]),
            OutputPin("Fail", PIN_TYPES[UE5DataType.EXEC]),
            OutputPin("As BP_Player", PIN_TYPES[UE5DataType.OBJECT_REFERENCE]),
        ],
        UE5DataTypeColor.TEAL_GREEN
    ),
    "blueprint/playsoundatlocation": NodeType(
        "blueprint/playsoundatlocation",
        "Play Sound at Location",
        [
            InputPin("In", PIN_TYPES[UE5DataType.EXEC]),
            InputPin("Sound", PIN_TYPES[UE5DataType.OBJECT_REFERENCE]),
            InputPin("Location", PIN_TYPES[UE5DataType.VECTOR]),
        ],
        [
            OutputPin("Out", PIN_TYPES[UE5DataType.EXEC]),
        ],
        UE5DataTypeColor.TEAL_GREEN
    ),
    "blueprint/destroyactor": NodeType(
        "blueprint/destroyactor",
        "Destroy Actor",
        [
            InputPin("In", PIN_TYPES[UE5DataType.EXEC]),
        ],
        [
            OutputPin("Out", PIN_TYPES[UE5DataType.EXEC]),
        ],
        UE5DataTypeColor.DARK_RED
    ),
    "blueprint/inputaction_interact": NodeType(
        "blueprint/inputaction_interact",
        "IA_Left Click",
        [],
        [
            OutputPin("Triggered", PIN_TYPES[UE5DataType.EXEC]),
        ],
        UE5DataTypeColor.DARK_RED
    ),
    "blueprint/flipflop": NodeType(
        "blueprint/flipflop",
        "Flip Flop",
        [
            InputPin("In", PIN_TYPES[UE5DataType.EXEC]),
        ],
        [
            OutputPin("A", PIN_TYPES[UE5DataType.EXEC]),
            OutputPin("B", PIN_TYPES[UE5DataType.EXEC]),
        ],
        UE5DataTypeColor.GREY
    ),

    "blueprint/eventtick": NodeType(
        "blueprint/eventtick",
        "Event Tick",
        [],
        [
            OutputPin("Out", PIN_TYPES[UE5DataType.EXEC]),
        ],
        UE5DataTypeColor.DARK_RED
    ),
    "blueprint/float_less_than": NodeType(
        "blueprint/float_less_than",
        "Float < Float",
        [
            InputPin("A", PIN_TYPES[UE5DataType.FLOAT]),
            InputPin("B", PIN_TYPES[UE5DataType.FLOAT]),
        ],
        [
            OutputPin("Result", PIN_TYPES[UE5DataType.BOOLEAN]),
        ],
        UE5DataTypeColor.DARK_GREEN
    ),
    "blueprint/float_add": NodeType(
        "blueprint/float_add",
        "Float + Float",
        [
            InputPin("A", PIN_TYPES[UE5DataType.FLOAT]),
            InputPin("B", PIN_TYPES[UE5DataType.FLOAT]),
        ],
        [
            OutputPin("Result", PIN_TYPES[UE5DataType.FLOAT]),
        ],
        UE5DataTypeColor.DARK_GREEN
    ),
    "blueprint/sethealth": NodeType(
        "blueprint/sethealth",
        "Set Health",
        [
            InputPin("In",     PIN_TYPES[UE5DataType.EXEC]),
            InputPin("Health", PIN_TYPES[UE5DataType.FLOAT]),
        ],
        [
            OutputPin("Out", PIN_TYPES[UE5DataType.EXEC]),
        ],
        UE5DataTypeColor.DARK_GREEN
    ),

    "blueprint/gethealth": NodeType(
        "blueprint/gethealth",
        "Get Health",
        [],
        [
            OutputPin("Health", PIN_TYPES[UE5DataType.FLOAT]),
        ],
        UE5DataTypeColor.DARK_GREEN
    ),

    "blueprint/getmaxhealth": NodeType(
        "blueprint/getmaxhealth",
        "Get Max Health",
        [],
        [
            OutputPin("Health", PIN_TYPES[UE5DataType.FLOAT]),
        ],
        UE5DataTypeColor.DARK_GREEN
    ),
    "blueprint/regenamount": NodeType(
        "blueprint/regenamount",
        "Regen Amount",
        [],
        [
            OutputPin("Out", PIN_TYPES[UE5DataType.FLOAT])
        ],
        UE5DataTypeColor.DARK_GREEN
    ),
    "blueprint/setactorrotation_open": NodeType(
        "blueprint/setactorrotation_open",
        "Set Actor Rotation (Open)",
        [
            InputPin("In",PIN_TYPES[UE5DataType.EXEC]),
        ],
        [
            OutputPin("Out", PIN_TYPES[UE5DataType.EXEC]),
        ],
        UE5DataTypeColor.LIGHT_GREEN
    ),
    # Set Actor Rotation Closed
    "blueprint/setactorrotation_closed": NodeType(
        "blueprint/setactorrotation_closed",
        "Set Actor Rotation (Closed)",
        [
            InputPin("In", PIN_TYPES[UE5DataType.EXEC]),
        ],
        [
            OutputPin("Out", PIN_TYPES[UE5DataType.EXEC]),
        ],
        UE5DataTypeColor.LIGHT_GREEN
    ),
}

