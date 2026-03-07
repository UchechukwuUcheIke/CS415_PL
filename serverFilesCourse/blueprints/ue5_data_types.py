from enum import Enum

class UE5DataType(Enum):
    # Basic types
    EXEC = "event"
    BOOLEAN = "Boolean"
    INTEGER = "Integer"
    FLOAT = "Float"
    STRING = "String"
    NAME = "Name"
    TEXT = "Text"

    # Math / Struct types
    VECTOR = "Vector"
    VECTOR2D = "Vector2D"
    ROTATOR = "Rotator"
    TRANSFORM = "Transform"
    COLOR = "Color"
    LINEAR_COLOR = "LinearColor"
    QUATERNION = "Quaternion"

    # Object / Actor references
    OBJECT_REFERENCE = "ObjectReference"
    ACTOR_REFERENCE = "ActorReference"
    CLASS_REFERENCE = "ClassReference"

    # Containers
    ARRAY = "Array"
    SET = "Set"
    MAP = "Map"

    # Special Blueprint types
    ENUM = "Enum"
    STRUCT = "Struct"
    INTERFACE = "Interface"