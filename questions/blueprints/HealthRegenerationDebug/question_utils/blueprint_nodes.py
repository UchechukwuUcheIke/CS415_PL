from blueprints.node_type import NODE_TYPES, NodeType
from blueprints.pin import InputPin, OutputPin
from blueprints.pin_type import PIN_TYPES
from blueprints.ue5_data_types import UE5DataType

NODES_TO_REGISTER = [
    NODE_TYPES["blueprint/beginplay"],
    NODE_TYPES["blueprint/print"],
    NODE_TYPES["blueprint/cast_to_bp_player"],
    NODE_TYPES["blueprint/oncomponentbeginoverlap"],
    NODE_TYPES["blueprint/destroyactor"],
    NODE_TYPES["blueprint/eventtick"],
    NODE_TYPES["blueprint/branch"],
    NODE_TYPES["blueprint/float_add"],
    NODE_TYPES["blueprint/sethealth"],
    NODE_TYPES["blueprint/gethealth"],
    NODE_TYPES["blueprint/getmaxhealth"],
    NODE_TYPES["blueprint/float_less_than"],
    NODE_TYPES["blueprint/regenamount"]
]