class PinType:
    def __init__(self, name, pin_type, color):
        self.name = name
        self.pin_type = pin_type
        self.color = color

PIN_TYPES = {
    "flow": PinType("Text", "event", "#ffffff"),
    "text": PinType("Text", "string", "#ff96ff"),
}