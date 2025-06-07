from office365.runtime.client_object_collection import (
    ClientObjectCollection as ClientObjectCollection,
)
from typing import TypeVar

T = TypeVar("T")

class TaxonomyItemCollection(ClientObjectCollection[T]): ...
