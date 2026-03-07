from enum import Enum

class PinType:
    def __init__(self, pin_type, color, shape):
        self.name = pin_type.value
        self.color = color
        self.shape = shape.value

class Shape(Enum):
    BOX = "LiteGraph.BOX_SHAPE"
    ROUND = "LiteGraph.ROUND_SHAPE"
    CIRCLE = "LiteGraph.CIRCLE_SHAPE"
    CARD = "LiteGraph.CARD_SHAPE"
    ARROW = "LiteGraph.ARROW_SHAPE"
    GRID = "LiteGraph.GRID_SHAPE"

class Type(Enum):
    EXEC = "event"
    STRING = "string"
    NUMBER = "number"
    BOOL = "bool"
    VECTOR = "vector"
    OBJECT = "object"
    ANY = -1

PIN_TYPES = {
    "flow": PinType(Type.EXEC, "#ffffff", Shape.ARROW),
    "text": PinType(Type.STRING, "#ff96ff", Shape.CIRCLE),
}