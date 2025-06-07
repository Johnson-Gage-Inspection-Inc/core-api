import marshmallow as ma
from _typeshed import Incomplete

class Upload(ma.fields.Field):
    format: Incomplete
    def __init__(self, format: str = "binary", **kwargs) -> None: ...
