from enum import Enum

from blueprints.pin_type import PinType
from blueprints.ue5_data_types import UE5DataType

class PinDirection(Enum):
    INPUT = "input"
    OUTPUT = "output"

class PinWidget(Enum):
    CHECKBOX = "checkbox"
    NUMBER = "number"
    TEXT = "text"
    DROPDOWN = "dropdown"

PIN_TYPES_TO_WIDGETS = {
    UE5DataType.STRING: PinWidget.TEXT,
    UE5DataType.BOOLEAN: PinWidget.TEXT,
    UE5DataType.TEXT: PinWidget.TEXT,
    UE5DataType.FLOAT: PinWidget.TEXT,
}

class Pin():
    def __init__(self, name, pin_type, pin_direction):
        self.name = name
        self.pin_type = pin_type
        self.pin_direction = pin_direction
        self._add_widget_type()

    def _add_widget_type(self):
        self.widget_type = None
        if self.pin_direction == PinDirection.INPUT:
            self.widget_type = PIN_TYPES_TO_WIDGETS.get(self.pin_type.ue5_data_type, None)
            
def InputPin(name, pin_type):
    return Pin(name, pin_type, PinDirection.INPUT)

def OutputPin(name, pin_type):
    return Pin(name, pin_type, PinDirection.OUTPUT)