from _typeshed import Incomplete

from .utils import deepupdate as deepupdate

class ArgumentsMixin:
    ARGUMENTS_PARSER: Incomplete
    def arguments(
        self,
        schema,
        *,
        location: str = "json",
        content_type: Incomplete | None = None,
        required: bool = True,
        description: Incomplete | None = None,
        example: Incomplete | None = None,
        examples: Incomplete | None = None,
        **kwargs,
    ): ...
