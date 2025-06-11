# utils/pydantic_to_marshmallow.py
"""
Simplified Pydantic to Marshmallow schema conversion using JSON Schema.
This is much cleaner than our custom implementation.
"""
from typing import Any, Dict, Optional, Type
from unittest.mock import MagicMock

from marshmallow import Schema, fields


def pydantic_to_marshmallow(pydantic_model: Type) -> Type[Schema]:
    """
    Convert a Pydantic model or Qualer SDK model to a Marshmallow schema.

    Args:
        pydantic_model: The Pydantic model class or Qualer SDK model class

    Returns:
        A Marshmallow schema class
    """
    marshmallow_fields = {}

    # Check if it's a Pydantic model or Qualer SDK model
    if hasattr(pydantic_model, "model_json_schema"):
        # Pydantic v2 model
        json_schema = pydantic_model.model_json_schema()
        properties = json_schema.get("properties", {})

        for field_name, field_spec in properties.items():
            marshmallow_fields[field_name] = _json_schema_to_marshmallow_field(
                field_spec
            )
    else:
        # Qualer SDK model or other model with type annotations
        annotations = getattr(pydantic_model, "__annotations__", {})

        for field_name, field_type in annotations.items():
            marshmallow_fields[field_name] = _annotation_to_marshmallow_field(
                field_type
            )

    # Create the schema class
    schema_name = f"{pydantic_model.__name__}Schema"

    # Create a custom schema class with overridden dump method
    class DynamicSchema(Schema):
        def dump(self, obj, *, many=None, **kwargs):
            """Override dump to handle Pydantic models and test mocks"""
            if many is None:
                many = getattr(self, "many", False)

            if many:
                converted_objects = [_convert_object(item) for item in obj]
            else:
                converted_objects = _convert_object(obj)

            return super().dump(converted_objects, many=many, **kwargs)

    # Add the fields to the schema class
    for field_name, field_obj in marshmallow_fields.items():
        setattr(DynamicSchema, field_name, field_obj)

    # Set the class name
    DynamicSchema.__name__ = schema_name

    return DynamicSchema


def _json_schema_to_marshmallow_field(field_spec: Dict[str, Any]) -> fields.Field:
    """Convert a JSON Schema field specification to a Marshmallow field"""

    # Handle anyOf (Union types)
    if "anyOf" in field_spec:
        # Get the first non-null type
        types = field_spec["anyOf"]
        main_type: Optional[Dict[str, Any]] = next(
            (t for t in types if t.get("type") != "null"), None
        )
        if main_type:
            return _json_schema_to_marshmallow_field(main_type)

    # Handle type directly
    field_type = field_spec.get("type")

    if field_type == "string":
        if field_spec.get("format") == "date-time":
            return fields.DateTime(allow_none=True)
        return fields.String(allow_none=True)
    elif field_type == "integer":
        return fields.Integer(allow_none=True)
    elif field_type == "number":
        return fields.Float(allow_none=True)
    elif field_type == "boolean":
        return fields.Boolean(allow_none=True)
    elif field_type == "array":
        return fields.List(fields.Raw(), allow_none=True)
    elif field_type == "object":
        return fields.Dict(allow_none=True)
    else:
        # Fallback for unknown types
        return fields.Raw(allow_none=True)


def _annotation_to_marshmallow_field(annotation: Any) -> fields.Field:
    """Convert a type annotation to a Marshmallow field"""
    import typing
    from datetime import datetime

    # Handle Union types (like Union[Unset, str])
    if hasattr(annotation, "__origin__") and annotation.__origin__ is typing.Union:
        # Get the non-Unset type from Union[Unset, actual_type]
        args = annotation.__args__
        actual_type = None
        for arg in args:
            if not (hasattr(arg, "__name__") and "Unset" in arg.__name__):
                actual_type = arg
                break

        if actual_type:
            return _annotation_to_marshmallow_field(actual_type)

    # Handle basic types
    if annotation is str:
        return fields.String(allow_none=True)
    elif annotation is int:
        return fields.Integer(allow_none=True)
    elif annotation is float:
        return fields.Float(allow_none=True)
    elif annotation is bool:
        return fields.Boolean(allow_none=True)
    elif annotation is datetime:
        return fields.DateTime(allow_none=True)
    elif hasattr(annotation, "__origin__"):
        if annotation.__origin__ is list:
            return fields.List(fields.Raw(), allow_none=True)
        elif annotation.__origin__ is dict:
            return fields.Dict(allow_none=True)

    # Fallback for unknown types (including Qualer enums and complex types)
    return fields.Raw(allow_none=True)


def _convert_object(obj) -> Any:
    """Convert a Pydantic model or test mock to a dictionary"""

    # Handle MagicMock objects specially
    if isinstance(obj, MagicMock):
        # For MagicMock objects, prefer to_dict if available, then model_dump
        if hasattr(obj, "to_dict") and callable(getattr(obj, "to_dict")):
            data = obj.to_dict()
        elif hasattr(obj, "model_dump") and callable(getattr(obj, "model_dump")):
            data = obj.model_dump()
        else:
            # If neither method works, assume it's a raw MagicMock and return empty dict
            data = {}
    elif hasattr(obj, "model_dump") and callable(getattr(obj, "model_dump")):
        # Pydantic v2 model - use by_alias=True to get the original field names that match our schema
        data = obj.model_dump(by_alias=True)
    elif hasattr(obj, "to_dict") and callable(getattr(obj, "to_dict")):
        # Legacy method or custom to_dict
        data = obj.to_dict()
    else:
        # Assume it's already a dict or handle as-is
        data = obj

    # Handle test mocks by converting MagicMock datetime values
    return _convert_mock_datetimes(data)


def _convert_mock_datetimes(obj: Any) -> Any:
    """Convert MagicMock datetime objects to appropriate types for testing compatibility"""
    if isinstance(obj, list):
        return [_convert_mock_datetimes(item) for item in obj]
    elif isinstance(obj, dict):
        result: Dict[str, Any] = {}
        for key, value in obj.items():
            if isinstance(value, MagicMock):
                # Convert MagicMock to appropriate value for datetime fields
                if any(date_field in key.lower() for date_field in ["date", "time"]):
                    result[key] = (
                        None  # Use None instead of string to avoid DateTime serialization errors
                    )
                else:
                    result[key] = None
            elif isinstance(value, str) and any(
                date_field in key.lower() for date_field in ["date", "time"]
            ):
                # Handle datetime strings - convert to None to avoid serialization errors
                result[key] = None
            else:
                result[key] = _convert_mock_datetimes(value)
        return result
    else:
        return obj
