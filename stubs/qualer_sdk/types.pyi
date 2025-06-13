from collections.abc import Mapping, MutableMapping
from http import HTTPStatus
from typing import IO, BinaryIO, Generic, Literal, TypeVar

from attrs import define

__all__ = ["UNSET", "File", "FileTypes", "RequestFiles", "Response", "Unset"]

class Unset:
    def __bool__(self) -> Literal[False]: ...

UNSET: Unset
FileContent = IO[bytes] | bytes | str
FileTypes = (
    tuple[str | None, FileContent, str | None]
    | tuple[str | None, FileContent, str | None, Mapping[str, str]]
)
RequestFiles = list[tuple[str, FileTypes]]

@define
class File:
    payload: BinaryIO
    file_name: str | None = ...
    mime_type: str | None = ...
    def to_tuple(self) -> FileTypes: ...

T = TypeVar("T")

@define
class Response(Generic[T]):
    status_code: HTTPStatus
    content: bytes
    headers: MutableMapping[str, str]
    parsed: T | None
