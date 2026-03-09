from enum import Enum
from blueprints.ue5_data_types import UE5DataType

class PinType:
    def __init__(self, ue5_data_type, litegraph_data_type, color, shape):
        self.ue5_data_type = ue5_data_type
        self.litegraph_data_type = litegraph_data_type.value
        self.color = color
        self.shape = shape.value

class PinWidget(Enum):
    CHECKBOX = "checkbox"
    NUMBER = "number"
    TEXT = "text"
    DROPDOWN = "dropdown"

class Shape(Enum):
    BOX = "LiteGraph.BOX_SHAPE"
    ROUND = "LiteGraph.ROUND_SHAPE"
    CIRCLE = "LiteGraph.CIRCLE_SHAPE"
    CARD = "LiteGraph.CARD_SHAPE"
    ARROW = "LiteGraph.ARROW_SHAPE"
    GRID = "LiteGraph.GRID_SHAPE"

class LitegraphDataType(Enum):
    EVENT = "event"
    STRING = "string"
    NUMBER = "number"
    BOOL = "bool"
    VECTOR = "vector"
    OBJECT = "object"
    ANY = -1

PIN_TYPES = {
    UE5DataType.EXEC: PinType(
        UE5DataType.EXEC, 
        LitegraphDataType.EVENT, 
        "#ffffff", 
        Shape.ARROW
        ),
    UE5DataType.STRING: PinType(
        UE5DataType.STRING, 
        LitegraphDataType.STRING, 
        "#ff96ff", 
        Shape.CIRCLE
        ),
    UE5DataType.BOOLEAN: PinType(
        UE5DataType.BOOLEAN, 
        LitegraphDataType.BOOL, 
        "#550000", 
        Shape.CIRCLE
        ),
    UE5DataType.TEXT: PinType(
        UE5DataType.TEXT, 
        LitegraphDataType.STRING, 
        "#ff96ff", 
        Shape.CIRCLE
        ),
    UE5DataType.OBJECT_REFERENCE: PinType(
        UE5DataType.OBJECT_REFERENCE, 
        LitegraphDataType.OBJECT, 
        "#00A3FF", 
        Shape.CIRCLE
        ),
    UE5DataType.FLOAT: PinType(
        UE5DataType.FLOAT, 
        LitegraphDataType.NUMBER, 
        "#9FFF3A", 
        Shape.CIRCLE
        ),
    UE5DataType.VECTOR: PinType(
        UE5DataType.VECTOR, 
        LitegraphDataType.VECTOR, 
        "#F6C320", 
        Shape.CIRCLE
        ),
    
}